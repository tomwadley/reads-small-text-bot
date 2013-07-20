import unittest
import readsSmallTextBot

class TestReadsSmallTextBot(unittest.TestCase):

  def test_get_suped(self):
    r = readsSmallTextBot.get_suped('A test^^^comment for testing')
    self.assertItemsEqual(r, ['comment'])
    r = readsSmallTextBot.get_suped('No small text')
    self.assertItemsEqual(r, [])
    r = readsSmallTextBot.get_suped('A multi\nline ^^^comment')
    self.assertItemsEqual(r, ['comment'])
    r = readsSmallTextBot.get_suped('Only^really^small text^^should be^found^by^this^bot')
    self.assertItemsEqual(r, ['this bot'])
    r = readsSmallTextBot.get_suped('A test^^^comment for^^testing^this^bot')
    self.assertItemsEqual(r, ['comment this bot'])
    r = readsSmallTextBot.get_suped('A test^^^comment ^^^testing')
    self.assertItemsEqual(r, ['comment testing'])
    r = readsSmallTextBot.get_suped('A test^^^comment\n^^^testing')
    self.assertItemsEqual(r, ['comment', 'testing'])

  def test_build_comment(self):
    r = readsSmallTextBot.build_comment(['comment'])
    self.assertEquals('>comment', r)
    r = readsSmallTextBot.build_comment(['comment', 'this bot'])
    self.assertEquals('>comment\n\n>this bot', r)

if __name__ == '__main__':
  unittest.main()
