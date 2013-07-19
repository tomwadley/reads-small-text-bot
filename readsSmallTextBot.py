import praw
import json
import time
import re

p = re.compile('(?:\^[^\^]*){2}\^(.*)')

def get_config():
  json_data = open('config.json', 'r').read()
  config = json.loads(json_data)
  return config

def get_suped(comment):
  sup_words = [word for word in comment.split() if word.count('^') >= 3]
  unreadable_fragments = [p.findall(word)[0] for word in sup_words]
  results = [" ".join(filter(None, word.split('^'))) for word in unreadable_fragments]
  return results

def build_comment(suped):
  return "\n\n".join(suped)

def login():
  print 'Loading config'
  config = get_config()
  print 'Logging in to Reddit as ' + config['username']
  r = praw.Reddit('ReadsSmallTextBot - reads sup text - by /u/doogle88 v 0.1')
  r.login(config['username'], config['password'])
  print 'Done'
  return r

def run_bot():
  r = login()
  already_done = []

  while True:
    subreddit = r.get_subreddit('botcirclejerk')
    print 'Getting submissions'
    for submission in subreddit.get_hot(limit=10):
      print 'Getting comments for: ' + submission.id
      flat_comments = praw.helpers.flatten_tree(submission.comments)
      for comment in flat_comments:
        suped = get_suped(comment.body)
        if suped and submission.id not in already_done:
          print 'Suped comment found: ' + comment.id
          msg = build_comment(suped)
          comment.reply(msg)
          already_done.append(comment.id)
    time.sleep(1800)

if __name__ == '__main__':
  run_bot()

