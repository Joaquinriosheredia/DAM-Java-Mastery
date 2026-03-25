[CONTENIDO]
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BertTokenizer, BertModel

class ProcessText:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def analyze(self, pages_content):
        semantic_features = {}
        
        for page_id, content in enumerate(pages_content.values(), start=1):
            doc = self.nlp(content)
            
            # Extracting basic NLP features
            tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
            lemmas = ' '.join([token.lemma_ for token in doc])
            
            # Semantic analysis with BERT
            inputs = self.tokenizer.encode_plus(
                content, 
                add_special_tokens=True,
                return_tensors="pt"
            )
            
            outputs = self.model(**inputs)
            semantic_embeddings = outputs.last_hidden_state
            
            semantic_features[page_id] = {
                'tokens': tokens,
                'lemmas': lemmas,
                'semantic_embedding': semantic_embeddings.detach().numpy()[0]
            }
        
        return semantic_features