""" This module translates text between English and French
   
It contains two functions:
    english_to_french(english_text)
    french_to_english(french_text)
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """ Translates English string into French and returns French as string
    
    Parameters
    ----------
    english_text : str
        English text to be translated.
        If an empty string, an empty string is returned.
        If None, None will be returned.
    
    """
    if english_text == "":
        return ""
    try:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    except ValueError as value_error_exception:
        print("Error:", value_error_exception)
        return None

def french_to_english(french_text):
    """ Translates French string into English and returns English as string
    
    Parameters
    ----------
    french_text : str
        French text to be translated.
        If an empty string, an empty string is returned.
        If None, None will be returned.
    
    """
    if french_text == "":
        return ""
    try:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except ValueError as value_error_exception:
        print("Error:", value_error_exception)
        return None
