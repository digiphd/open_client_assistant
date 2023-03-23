import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ChatbotError(Exception):
    """Custom exception class for chatbot-related errors."""
    pass

def handle_error(error):
    """Log and handle errors."""
    logging.error(error)