from re import sub

from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.filter()
def remove_accent(word):
    """
    Removes accents from the given word or phrase. If word is an instance of a class and is not a string type
    then, try to call it's __str__ (str()) method to get the word. If fail, return nothing.
    Else, return the word or phrase as is if no accent presented. Else the word or phrase without accents.
    This is applied ONLY for the Greek language where small accented letters (ά, ί etc) are transformed via CSS
    to uppercase letters but the accent remains making it look ugly (ΚΑΛΗΜΈΡΑ instead of ΚΑΛΗΜΕΡΑ).

                        REPLACEMENT TABLE
    ------------------------------------------------------------
    Small GR letter |  Unicode  |  Small GR letter  |  Unicode
     (with accent)  |           |     (wo accent)   |
    ------------------------------------------------------------
           ά        |  U+03AC   |         α         |   U+03B1
           έ        |  U+03AD   |         ε         |   U+03B5
           ή        |  U+03AE   |         η         |   U+03B7
           ί        |  U+03AF   |         ι         |   U+03B9
           ό        |  U+03CC   |         ο         |   U+03BF
           ύ        |  U+03CD   |         υ         |   U+03C5
           ώ        |  U+03CE   |         ω         |   U+03C9
    """
    if not (isinstance(word, str)):
        try:
            word = str(word)
        except AttributeError:
            return ''

    replacement_table = {  # Πεζά με τόνο
                           'ά': 'α',
                           'έ': 'ε',
                           'ή': 'η',
                           'ί': 'ι',
                           'ό': 'ο',
                           'ύ': 'υ',
                           'ώ': 'ω',
                           # Κεφαλαία με τόνο
                           'Ά': 'Α',
                           'Έ': 'Ε',
                           'Ή': 'Η',
                           'Ί': 'Ι',
                           'Ό': 'Ο',
                           'Ύ': 'Υ',
                           'Ώ': 'Ω',
    }
    for letter in replacement_table:
        word = sub(letter, replacement_table.get(letter), word)
    return word

# replacement_table = {u'\\u03ac': u'\\u03b1',
    #                      u'\\u03ad': u'\\u03b5',
    #                      u'\\u03ae': u'\\u03b7',
    #                      u'\\u03af': u'\\u03b9',
    #                      u'\\u03cc': u'\\u03bf',
    #                      u'\\u03cd': u'\\u03c5',
    #                      u'\\u03ce': u'\\u03c9'}
