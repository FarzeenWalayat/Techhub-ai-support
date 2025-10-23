import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==================== OPENAI SETTINGS ====================
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4-turbo")

# ==================== APPLICATION SETTINGS ====================
APP_NAME = os.getenv("APP_NAME", "TechHub Customer Service AI")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# ==================== DATABASE SETTINGS ====================
VECTOR_DB_TYPE = os.getenv("VECTOR_DB_TYPE", "chromadb")
VECTOR_DB_PATH = "data/vector_db"
KNOWLEDGE_BASE_PATH = "data/knowledge_base"

# ==================== BUSINESS SETTINGS (TechHub Specific) ====================
BUSINESS_NAME = "TechHub Electronics"
BUSINESS_DESCRIPTION = "Your trusted source for quality electronics and gadgets"

# Response configuration
CONFIDENCE_THRESHOLD = 0.7
MAX_RESPONSE_LENGTH = 500
RESPONSE_LANGUAGE = "english"

# Escalation settings
ENABLE_ESCALATION = True
ESCALATION_EMAIL = "support@techhub.com"
HUMAN_TEAM_AVAILABLE = True

# ==================== SUPPORTED CATEGORIES ====================
SUPPORT_CATEGORIES = [
    "shipping_delivery",
    "returns_refunds",
    "product_availability",
    "account_login",
    "product_info",
    "pricing",
    "warranty",
    "technical_support",
    "general_inquiry"
]

# ==================== LOGGING ====================
LOG_DIR = "logs"
LOG_FILE = f"{LOG_DIR}/techhub_support.log"

# Create directories if they don't exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(KNOWLEDGE_BASE_PATH, exist_ok=True)
os.makedirs(VECTOR_DB_PATH, exist_ok=True)

# ==================== VALIDATION ====================
def validate_config():
    """Check if all required settings are configured"""
    if not OPENAI_API_KEY:
        raise ValueError("ERROR: OPENAI_API_KEY not found in .env file")
    
    print("✅ Configuration loaded successfully")
    print(f"   Environment: {ENVIRONMENT}")
    print(f"   Model: {OPENAI_MODEL}")
    print(f"   Business: {BUSINESS_NAME}")

if __name__ == "__main__":
    validate_config()