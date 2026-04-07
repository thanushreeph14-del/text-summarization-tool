"""
Core text summarization module using NLP techniques
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from config import MODEL_NAME, MAX_LENGTH, MIN_LENGTH, MIN_TEXT_LENGTH
import heapq


class TextSummarizer:
    """Text summarization using extractive NLP techniques"""
    
    def __init__(self):
        """Initialize the summarizer"""
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
    
    def validate_text(self, text):
        """Validate input text"""
        if not text or not isinstance(text, str):
            raise ValueError("Input must be a non-empty string")
        
        if len(text) < MIN_TEXT_LENGTH:
            raise ValueError(f"Text must be at least {MIN_TEXT_LENGTH} characters")
        
        return True
    
    def _preprocess_text(self, text):
        """Preprocess text for summarization"""
        # Tokenize into sentences
        sentences = sent_tokenize(text)
        
        # Get stopwords
        stop_words = set(stopwords.words('english'))
        
        # Calculate word frequencies
        word_frequencies = {}
        for sentence in sentences:
            words = word_tokenize(sentence.lower())
            for word in words:
                if word not in stop_words and word.isalnum():
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
        
        # Normalize frequencies
        if word_frequencies:
            max_frequency = max(word_frequencies.values())
            for word in word_frequencies:
                word_frequencies[word] = word_frequencies[word] / max_frequency
        
        return sentences, word_frequencies
    
    def _score_sentences(self, sentences, word_frequencies):
        """Score sentences based on word frequencies"""
        sentence_scores = {}
        
        for i, sentence in enumerate(sentences):
            words = word_tokenize(sentence.lower())
            score = 0
            
            for word in words:
                if word in word_frequencies:
                    score += word_frequencies[word]
            
            sentence_scores[i] = score
        
        return sentence_scores
    
    def summarize(self, text, max_length=MAX_LENGTH, min_length=MIN_LENGTH):
        """
        Summarize the input text using extractive summarization
        
        Args:
            text (str): Input text to summarize
            max_length (int): Maximum length of summary (in words)
            min_length (int): Minimum length of summary (in words)
            
        Returns:
            str: Summarized text
        """
        self.validate_text(text)
        
        try:
            # Preprocess text
            sentences, word_frequencies = self._preprocess_text(text)
            
            if len(sentences) <= 3:
                # If text is short, return first few sentences
                summary_sentences = sentences[:2] if len(sentences) > 1 else sentences
            else:
                # Score sentences
                sentence_scores = self._score_sentences(sentences, word_frequencies)
                
                # Get top sentences
                num_sentences = max(2, min(5, len(sentences) // 3))
                top_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
                top_sentences.sort()  # Keep original order
                
                summary_sentences = [sentences[i] for i in top_sentences]
            
            # Join sentences and limit length
            summary = ' '.join(summary_sentences)
            
            # Truncate if too long
            words = summary.split()
            if len(words) > max_length:
                words = words[:max_length]
                summary = ' '.join(words)
                # Ensure it ends with a complete sentence
                if not summary.endswith('.'):
                    summary = summary.rsplit('.', 1)[0] + '.'
            
            return summary if summary else "Summary could not be generated."
        
        except Exception as e:
            raise RuntimeError(f"Summarization failed: {str(e)}")
    
    def summarize_batch(self, texts, max_length=MAX_LENGTH, min_length=MIN_LENGTH):
        """
        Summarize multiple texts
        
        Args:
            texts (list): List of texts to summarize
            max_length (int): Maximum length of summary
            min_length (int): Minimum length of summary
            
        Returns:
            list: List of summarized texts
        """
        summaries = []
        for text in texts:
            try:
                summary = self.summarize(text, max_length, min_length)
                summaries.append(summary)
            except Exception as e:
                summaries.append(f"Error: {str(e)}")
        
        return summaries
