import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    porter_stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    # Tokenize the text
    words = word_tokenize(text.lower())

    # Remove stop words, perform stemming, and lemmatization
    processed_words = [
        lemmatizer.lemmatize(porter_stemmer.stem(word))
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return processed_words

def create_inverted_index(corpus):
    inverted_index = {}

    for file_id in corpus.fileids():
        document = corpus.raw(file_id)
        processed_words = preprocess_text(document)

        for position, word in enumerate(processed_words):
            if word not in inverted_index:
                inverted_index[word] = []

            inverted_index[word].append((file_id, position))

    return inverted_index

def search_inverted_index(inverted_index, query, conjunction=True):
    query_words = preprocess_text(query)

    if conjunction:
        # AND query
        result_set = set(inverted_index[query_words[0]])

        for word in query_words[1:]:
            result_set.intersection_update(inverted_index.get(word, set()))
    else:
        # OR query
        result_set = set()

        for word in query_words:
            result_set.update(inverted_index.get(word, set()))

    return result_set

# Load Gutenberg corpus
gutenberg_corpus = gutenberg

# Create inverted index
index = create_inverted_index(gutenberg_corpus)

# Example search queries
query1 = "love and hate"
query2 = "love or hate"

# Search inverted index
result1 = search_inverted_index(index, query1, conjunction=True)
result2 = search_inverted_index(index, query2, conjunction=False)

# Display results
print(f"Search results for query '{query1}': {result1}")
print(f"Search results for query '{query2}': {result2}")
