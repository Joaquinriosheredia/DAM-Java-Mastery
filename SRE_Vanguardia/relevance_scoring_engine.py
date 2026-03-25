[CONTENIDO]
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class CalculateRelevance:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def evaluate(self, semantic_features, keywords):
        tfidf_matrix = self.vectorizer.fit_transform(keywords.values())
        
        relevancies = {}
        
        for page_id, features in semantic_features.items():
            # Compute TF-IDF similarity
            content_tfidf = self.vectorizer.transform([features['lemmas']])
            similarities = cosine_similarity(tfidf_matrix, content_tfidf)
            
            relevancies[page_id] = {
                'tfidf': np.array(similarities).flatten().tolist(),
                'semantic_embedding': features['semantic_embedding']
            }
        
        return relevancies

def cosine_similarity(A, B):
    numerator = np.dot(A.T, B)
    normA = np.linalg.norm(A, axis=1)[:, None]
    normB = np.linalg.norm(B, axis=0)[None, :]
    
    return (numerator / (normA * normB)).flatten()