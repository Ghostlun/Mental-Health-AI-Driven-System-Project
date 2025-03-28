# test_script.py
import nltk
from nltk.tokenize import sent_tokenize

# Force download of punkt again
nltk.download('punkt')

# Test sentence tokenization
text = "This is an example. Here is another sentence."
sentences = sent_tokenize(text)
print(sentences)