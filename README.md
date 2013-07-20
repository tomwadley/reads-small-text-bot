# ReadsSmallTextBot

A Reddit bot which looks for comments containing at least level 3 superscript text (text with ^^^ before it) and replies with a full-sized version of that text.

## Setup

This bot is built using Python2 and [PRAW](https://github.com/praw-dev/praw). To install PRAW via pip:

    pip install praw

Before running the bot, you need to copy `config.json.example` to `config.json` and edit it with your desired Reddit account settings.

## Config

The config file uses json syntax. It must be called `config.json`. Copy `config.json.example` for reference.

- **username** - the Reddit account the bot should login with
- **password** - the password for the account
- **subreddits** - the subreddits the bot should operate in. Use "all" to have the bot search all subreddits. You can also use multi-reddits such as "test+botcirclejerk"

## Running

To start the bot run:

    python2 readsSmallTextBot.py

*Note: on most systems, `python2` is just called `python`*

## License

Just like PRAW, this code is released under the GNU GPLv3 (see COPYING)

