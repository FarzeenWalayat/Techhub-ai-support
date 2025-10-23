import os
from pathlib import Path

class KnowledgeBase:
    """Load and manage TechHub's knowledge base"""
    
    def __init__(self, kb_path="data/knowledge_base"):
        self.kb_path = kb_path
        self.faqs = {}
        self.all_content = ""
        self.load_knowledge_base()
    
    def load_knowledge_base(self):
        """Load all FAQ files from knowledge base folder"""
        print("📚 Loading Knowledge Base...")
        
        # Load the main FAQ file
        faq_file = os.path.join(self.kb_path, "techhub_faqs.txt")
        
        if os.path.exists(faq_file):
            with open(faq_file, 'r', encoding='utf-8') as f:
                self.all_content = f.read()
            print(f"✅ Loaded: techhub_faqs.txt")
        else:
            print(f"❌ Warning: {faq_file} not found")
        
        print(f"📖 Knowledge Base Size: {len(self.all_content)} characters")
    
    def get_context(self):
        """Return the full knowledge base context"""
        return self.all_content
    
    def get_relevant_info(self, query):
        """Search knowledge base for relevant information"""
        query_lower = query.lower()
        relevant_lines = []
        
        for line in self.all_content.split('\n'):
            if any(word in query_lower for word in query_lower.split()):
                relevant_lines.append(line)
        
        return '\n'.join(relevant_lines[:10])
    
    def get_summary(self):
        """Get summary of knowledge base"""
        lines = self.all_content.split('\n')
        sections = [line for line in lines if line.startswith('SECTION')]
        
        return {
            'total_sections': len(sections),
            'total_size': len(self.all_content),
            'sections': sections
        }


if __name__ == "__main__":
    kb = KnowledgeBase()
    summary = kb.get_summary()
    
    print("\n" + "="*50)
    print("KNOWLEDGE BASE SUMMARY")
    print("="*50)
    print(f"✅ Sections Found: {summary['total_sections']}")
    print(f"✅ Total Content Size: {summary['total_size']} characters")
    print("\nSections:")
    for section in summary['sections']:
        print(f"  - {section}")
    
    print("\n" + "="*50)
    print("TEST SEARCH")
    print("="*50)
    test_query = "shipping"
    results = kb.get_relevant_info(test_query)
    print(f"\nSearch for '{test_query}':")
    print(results[:500] + "...")