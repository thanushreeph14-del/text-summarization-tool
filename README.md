# Text summarization Tool
"Company":CODTECH IT SOLUTIONS PRIVATE LIMITED 
"NAME":THANUSHREE PH
"INTERN ID":CTIS7773
"DOMAIN":Artificial Intelligence
"DURATION":12 Weeks
"Mentor":NEELA SANTHOSH


<<<<<<< HEAD
# Text Summarization Tool

## 📋 Project Overview
A powerful Python tool that summarizes lengthy articles using state-of-the-art NLP techniques. This tool leverages transformer-based models to generate concise, accurate summaries while preserving the essential information from the original text.

## 🎯 Deliverable
**Python script showcasing input text and concise summaries** with automatic compression ratio calculation and interactive user mode.

## 📁 Project Structure
```
ph1/
├── main.py              # Main entry point with demo and interactive mode
├── summarizer.py        # Core summarization module
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🚀 Quick Start

### 1. Set Up Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Tool
```bash
python main.py
```

## 🔧 Technology Stack
- **Transformers**: Pre-trained BART model from Facebook/Meta
- **PyTorch**: Deep learning framework
- **NLTK**: Natural Language Toolkit for text processing
- **NumPy**: Numerical computing support

## 💡 Features

### ✨ Core Functionality
- **Abstract Summarization**: Uses transformer-based models for intelligent summaries
- **Batch Processing**: Summarize multiple texts efficiently
- **Text Validation**: Ensures input quality and minimum length requirements
- **GPU Support**: Automatic GPU detection for faster processing

### 🎮 User Interface
- **Demo Mode**: Pre-loaded sample articles for immediate demonstration
- **Interactive Mode**: User input for custom articles
- **Metrics Display**: Shows word count reduction percentage
- **User-Friendly Output**: Clear formatting with visual indicators

## ⚙️ Configuration
Edit `config.py` to customize:
- `MAX_LENGTH`: Maximum summary length (default: 150)
- `MIN_LENGTH`: Minimum summary length (default: 50)
- `MIN_TEXT_LENGTH`: Minimum input text length (default: 100)
- Model selection and other parameters

## 📊 Usage Example

```python
from summarizer import TextSummarizer

# Initialize summarizer
summarizer = TextSummarizer()

# Summarize text
text = "Your long article here..."
summary = summarizer.summarize(text)
print(summary)

# Batch summarization
texts = [text1, text2, text3]
summaries = summarizer.summarize_batch(texts)
```

## 🔍 How It Works
1. **Input Validation**: Checks text length and format
2. **Tokenization**: Breaks text into meaningful units
3. **Model Processing**: BART transformer model analyzes and generates summary
4. **Output**: Returns concise, coherent summary maintaining key points

## 📈 Performance
- **CPU Mode**: ~3-5 seconds per article (depending on length)
- **GPU Mode**: ~0.5-1 second per article
- **Summary Compression**: Typically 70-80% text reduction

## ⚠️ Requirements
- Python 3.8+
- 4GB RAM minimum (8GB+ recommended)
- Internet connection (for initial model download)

## 🐛 Troubleshooting
- If model fails to download: Check internet connection
- Out of memory errors: Reduce text length or use GPU
- Slow performance: Enable GPU support or reduce article length

## 📝 License
Open source project for educational and commercial use.

## 🤝 Support
For issues or improvements, refer to the code comments and configuration options.
=======
# text-summarization-tool
>>>>>>> ffcdabc0d7a4f8163cab0d64fc7c4114a116fc3c
