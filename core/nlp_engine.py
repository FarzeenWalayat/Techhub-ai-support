import sys
sys.path.append('.')

import os
from openai import OpenAI
from core.knowledge_base import KnowledgeBase
from config import OPENAI_API_KEY, OPENAI_MODEL


class NLPEngine:
    """NLP Engine to understand and process customer queries"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
        self.kb = KnowledgeBase()
    
    def classify_intent(self, query):
        """Classify what the customer is asking about"""
        
        system_prompt = """You are a customer service classifier. 
        Classify the customer's question into ONE of these categories:
        - shipping_delivery
        - returns_refunds
        - product_availability
        - account_login
        - product_info
        - pricing
        - warranty
        - technical_support
        - general_inquiry
        
        Return ONLY the category name, nothing else."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=50,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
            )
            intent = response.choices[0].message.content.strip().lower()
        except Exception as e:
            print(f"⚠️ API Error: {str(e)}")
            intent = "general_inquiry"
        
        return intent
    
    def extract_entities(self, query):
        """Extract important information from the query"""
        
        system_prompt = """Extract key entities from the customer query.
        Return in format: entity_name: value
        Common entities: product, order_id, issue_type, urgency"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=100,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
            )
            entities_text = response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ API Error: {str(e)}")
            entities_text = "Unable to extract"
        
        return entities_text
    
    def get_relevant_context(self, query):
        """Get relevant information from knowledge base"""
        relevant_info = self.kb.get_relevant_info(query)
        return relevant_info
    
    def analyze_query(self, query):
        """Complete analysis of customer query"""
        
        print(f"\n🔍 Analyzing Query: '{query}'")
        print("="*60)
        
        intent = self.classify_intent(query)
        print(f"✅ Intent: {intent}")
        
        entities = self.extract_entities(query)
        print(f"✅ Entities: {entities}")
        
        context = self.get_relevant_context(query)
        print(f"✅ Relevant Info Found: {len(context)} characters")
        
        analysis = {
            'query': query,
            'intent': intent,
            'entities': entities,
            'context': context
        }
        
        return analysis


if __name__ == "__main__":
    print("🚀 Starting NLP Engine Test...")
    print("="*60)
    
    nlp = NLPEngine()
    
    test_queries = [
        "How long does shipping take?",
        "I want to return my laptop",
        "Is the iPhone 14 in stock?",
        "I forgot my password"
    ]
    
    for query in test_queries:
        analysis = nlp.analyze_query(query)
        print("="*60)
    
    print("✅ NLP Engine Test Complete!")