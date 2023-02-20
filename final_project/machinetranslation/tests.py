import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english(None), None)
        self.assertNotEqual(french_to_english("None"), "")
        self.assertNotEqual(french_to_english("None"), None)
        self.assertEqual(french_to_english(""), "")  

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertEqual(english_to_french(None), None)
        self.assertNotEqual(english_to_french(None), "Néant")
        self.assertNotEqual(english_to_french("None"), "")
        self.assertNotEqual(english_to_french("None"), None)
        self.assertEqual(english_to_french(""), "")

if __name__ == '__main__':
    unittest.main()
