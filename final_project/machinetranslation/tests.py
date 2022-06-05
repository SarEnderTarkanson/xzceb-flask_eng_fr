import unittest

from translator import english_french,french_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_french('Hello'), 'Bonjour')
        self.assertEqual(english_french('Hello'), 'Salut')

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_english('Bonjour'), 'Hello')
        self.assertEqual(french_english('Salut'), 'Hello')

if __name__ == '__main__':
    unittest.main()