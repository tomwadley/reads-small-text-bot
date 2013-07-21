import praw
import json
import time
import re
import sys
import traceback

p = re.compile('(?:\^[^\^]*){2}\^(.*)')

def get_config():
  print 'Loading config'
  json_data = open('config.json', 'r').read()
  config = json.loads(json_data)
  return config

def get_suped(comment):
  r = []
  for line in comment.split('\n'):
    sup_words = [word for word in line.split() if word.count('^') >= 3]
    unreadable_fragments = [p.findall(word)[0] for word in sup_words]
    results = [" ".join(filter(None, word.split('^'))) for word in unreadable_fragments]
    if results:
      r.append(" ".join(results))
  return r

def build_comment(suped):
  return "\n\n".join(['>' + line for line in suped])

def login(username, password):
  print 'Logging in to Reddit as ' + username
  r = praw.Reddit('ReadsSmallTextBot - reads sup text - by /u/doogle88 v 0.1'
                  'https://github.com/tomwadley/reads-small-text-bot')
  r.login(username, password)
  r.config.decode_html_entities = True
  print 'Done'
  return r

def run_bot():
  config = get_config()
  username = config['username']
  password = config['password']
  r = login(username, password)
  subreddits = config['subreddits']

  already_done = []

  while True:
    print 'Getting comments for ' + subreddits
    subreddit = r.get_subreddit(subreddits)
    comments = subreddit.get_comments(limit=None)

    for comment in comments:
      suped = get_suped(comment.body)
      if suped and comment.id not in already_done:
        if any(reply for reply in comment.replies if reply.author and reply.author.name == username):
          print 'Suped comment found: ' + comment.id + ' - skipping (already replied)'
        else:
          print 'Suped comment found: ' + comment.id + ' - replying'
          msg = build_comment(suped)
          comment.reply(msg)
        already_done.append(comment.id)

    time.sleep(10)

def bot_harness():
  while True:
    try:
      run_bot()
    except:
      exc_type, exc_value, exc_traceback = sys.exc_info()
      traceback.print_exception(exc_type, exc_value, exc_traceback)
      print 'Error - will sleep for 2 mins'
      time.sleep(120)
      pass

if __name__ == '__main__':
  bot_harness()

