import sys
sys.path.append('.')

from openai import OpenAI
from core.knowledge_base import KnowledgeBase
from config import OPENAI_API_KEY, OPENAI_MODEL, CONFIDENCE_THRESHOLD, MAX_RESPONSE_LENGTH

class ResponseGenerator:
    """Generate natural responses based on NLP analysis"""
    
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL
        self.kb = KnowledgeBase()
        self.confidence_threshold = CONFIDENCE_THRESHOLD
    
    def generate_response(self, analysis):
        """Generate response based on NLP analysis"""
        
        query = analysis['query']
        intent = analysis['intent']
        context = analysis['context']
        entities = analysis['entities']
        
        system_prompt = f"""You are TechHub's professional customer service AI.
        
Business Name: TechHub Electronics
Your Role: Answer customer questions helpfully and professionally.

IMPORTANT RULES:
1. Be friendly but professional
2. Keep responses concise (under {MAX_RESPONSE_LENGTH} characters)
3. If you don't have information, suggest contacting support
4. Always be honest - never make up information
5. Reference the knowledge base information provided

Customer Query: {query}
Query Type: {intent}
Customer Info: {entities}

Here is relevant information from our knowledge base:
{context}

Generate a helpful, natural response based on this information."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=200,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
            )
            
            response_text = response.choices[0].message.content.strip()
            confidence = 0.95
            
        except Exception as e:
            print(f"API Error: {str(e)}")
            response_text = "I'm having trouble processing your request. Please contact support@techhub.com"
            confidence = 0.0
        
        return {
            'response': response_text,
            'confidence': confidence,
            'intent': intent,
            'needs_escalation': confidence < self.confidence_threshold
        }
    
    def format_response(self, response_data):
        """Format response for display"""
        
        formatted = f"""
CUSTOMER SERVICE RESPONSE
{'='*60}
Response: {response_data['response']}

Confidence: {response_data['confidence']*100:.0f}%
Intent: {response_data['intent']}
Escalation Needed: {'Yes' if response_data['needs_escalation'] else 'No'}
{'='*60}
        """
        return formatted


if __name__ == "__main__":
    print("Testing Response Generator...")
    print("="*60)
    
    from nlp_engine import NLPEngine
    
    nlp = NLPEngine()
    rg = ResponseGenerator()
    
    test_queries = [
        "How long does shipping take?",
        "What's your return policy?",
        "Is there a warranty?"
    ]
    
    for query in test_queries:
        print(f"\nCustomer: {query}")
        analysis = nlp.analyze_query(query)
        response = rg.generate_response(analysis)
        print(rg.format_response(response))