[CONTENIDO]
import os
from flask import Flask, request, jsonify
from web_crawler import CrawlWebsite
from nlp_processor import ProcessText
from relevance_scoring_engine import CalculateRelevance
from recommendation_system import GenerateRecommendations

app = Flask(__name__)

@app.route('/generate_links', methods=['POST'])
def generate_links():
    website_url = request.json['websiteUrl']
    
    # Step 1: Crawl Website
    crawler = CrawlWebsite()
    data_store = crawler.run(website_url)
    
    # Step 2: Process Text
    nlp_processor = ProcessText()
    semantic_features = nlp_processor.analyze(data_store['pages'])
    
    # Step 3: Calculate Relevance
    relevance_engine = CalculateRelevance()
    relevancies = relevance_engine.evaluate(semantic_features, data_store['keywords'])
    
    # Step 4: Generate Recommendations
    recommendation_system = GenerateRecommendations(relevancies)
    optimized_links = recommendation_system.generate(data_store['content'])
    
    return jsonify({
        'optimizedLinks': optimized_links,
        'message': 'Internal link optimization suggestions generated successfully.'
    })

if __name__ == '__main__':
    app.run(debug=True)