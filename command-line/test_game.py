import unittest
import game

from unittest import mock

class TestGameMethods(unittest.TestCase):

    def test_sanitize_1(self):
        game.sanitize('1')

    def test_sanitize_5(self):
        with self.assertRaises(Exception) as context:
            game.sanitize('5')        
        self.assertTrue('Argument outside of accepted range 0 - 4' in str(context.exception))

    def test_sanitize_abc(self):
        with self.assertRaises(Exception) as context:
            game.sanitize('abc')        
        self.assertTrue('Argument not a number' in str(context.exception))

    def mockRandomLizard(self, args):
        return "lizard", 3

    def mockRandomRock(self, args):
        return "rock", 2

    def test_playMe_lost(self):
        with mock.patch('random.choice', self.mockRandomLizard):
            game.playMe("Spock")        

    def test_playMe_win(self):
        with mock.patch('random.choice', self.mockRandomRock):
            game.playMe("Spock")        

if __name__ == '__main__':
    unittest.main()