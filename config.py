"""
Configuration settings for text summarization tool
"""

# Model configuration
MODEL_NAME = "facebook/bart-large-cnn"
MAX_LENGTH = 150
MIN_LENGTH = 50

# Text processing
MIN_TEXT_LENGTH = 100
CHUNK_SIZE = 1024

# Display settings
VERBOSE = True
