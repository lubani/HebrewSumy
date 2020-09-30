from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import hebrew_tokenizer as ht
import requests
import string
# for removing punctuations from text
translator = str.maketrans("", "", string.punctuation)

# Increase this variable to get more summary and reduce this to get less summary
SENTENCES_COUNT = 3


if __name__ == "__main__":
    # url in hebrew language
    url = "https://he.wikipedia.org/wiki/%D7%93%D7%95%D7%A0%D7%9C%D7%93_%D7%98%D7%A8%D7%90%D7%9E%D7%A4"
    parser = HtmlParser.from_url(url, None)

    stemmer = Stemmer("Hebrew")
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words("Hebrew")

    # Must set the encoding to [utf-8] for hebrew language
    file = open("output.txt","w",encoding='utf-8')
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        # printing the text from the sentence object
        print(sentence._text)
        # writing the result into the file as well
        file.write(sentence._text)
    file.close()
