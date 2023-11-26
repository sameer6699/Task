from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from nltk.corpus import wordnet
nltk.download('wordnet')


# Function to get synonyms using WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Function to index documents using Whoosh
def create_index():
    schema = Schema(title=TEXT(stored=True), content=TEXT)
    ix = create_in("indexdir", schema)
    writer = ix.writer()

    documents = [
        {"title": "Document 1", "content": "Python is a programming language."},
        {"title": "Document 2", "content": "Java is another programming language."},
        {"title": "Document 3", "content": "Python and Java are widely used."},
        {"title": "Document 4", "content": "Programming languages are essential for software development."},
        {"title": "Document 5", "content": "Learning multiple languages enhances programming skills."},
    ]

    for doc in documents:
        writer.add_document(title=doc["title"], content=doc["content"])

    writer.commit()

# Function to perform search and ranking using Whoosh
def search_and_rank(query_str):
    ix = open_dir("indexdir")
    searcher = ix.searcher(weighting=scoring.TF_IDF())

    query = QueryParser("content", ix.schema).parse(query_str)
    results = searcher.search(query, terms=True)

    ranked_results = [(result["title"], result.score) for result in results]

    searcher.close()

    return ranked_results

# Main function
def main():
    # Create index
    create_index()

    # Perform search
    query = "programming languages"
    print(f"Searching for: {query}")
    results = search_and_rank(query)

    print("\nSearch Results:")
    for title, score in results:
        print(f"{title} - Score: {score:.4f}")

if __name__ == "__main__":
    main()
