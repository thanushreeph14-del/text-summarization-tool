"""
Main script for Text Summarization Tool
Demonstrates input text and concise summaries
"""

from summarizer import TextSummarizer
from config import VERBOSE


def print_section(title):
    """Print a formatted section title"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def display_summary(original_text, summary):
    """Display original and summarized text"""
    original_words = len(original_text.split())
    summary_words = len(summary.split())
    reduction = round((1 - summary_words / original_words) * 100, 1)
    
    print(f"📄 ORIGINAL TEXT ({original_words} words):")
    print(f"{original_text[:200]}..." if len(original_text) > 200 else original_text)
    
    print(f"\n✏️  SUMMARY ({summary_words} words | {reduction}% reduction):")
    print(f"{summary}\n")


def main():
    """Main execution function"""
    
    print_section("TEXT SUMMARIZATION TOOL - NLP POWERED")
    
    # Initialize summarizer
    if VERBOSE:
        print("🚀 Loading summarization model...")
    
    try:
        summarizer = TextSummarizer()
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Sample texts for demonstration
    sample_texts = [
        """
        Artificial Intelligence (AI) is rapidly transforming industries worldwide. 
        Machine learning algorithms are now capable of processing vast amounts of data 
        and making predictions with remarkable accuracy. Natural Language Processing (NLP), 
        a subset of AI, enables computers to understand and generate human language. 
        Companies are leveraging these technologies to improve customer service, automate 
        routine tasks, and gain competitive advantages. However, ethical concerns about 
        data privacy, bias in algorithms, and job displacement remain critical challenges 
        that need to be addressed as AI continues to evolve.
        """,
        
        """
        Climate change is one of the most pressing challenges facing humanity today. 
        Rising global temperatures are causing unprecedented weather patterns, from severe 
        droughts to catastrophic floods. The scientific consensus indicates that human 
        activities, particularly the burning of fossil fuels, are the primary drivers of 
        climate change. Governments, businesses, and individuals are working together to 
        reduce carbon emissions and transition to renewable energy sources. International 
        agreements like the Paris Climate Accord represent global commitment to limiting 
        temperature rise, but more aggressive action is needed to prevent irreversible damage 
        to our planet and ecosystems.
        """,
        
        """
        The human brain is the most complex organ in the body, containing approximately 
        86 billion neurons that communicate through trillions of connections. Recent 
        neuroscience research has revealed how the brain processes information, stores memories, 
        and generates consciousness. Scientists are developing brain-computer interfaces that 
        could help people with paralysis regain mobility and restore sensory functions. 
        Understanding neural mechanisms is also crucial for treating neurodegenerative diseases 
        like Alzheimer's and Parkinson's. As technology advances, we're getting closer to 
        unlocking the secrets of human cognition and improving mental health outcomes.
        """
    ]
    
    # Process and display summaries
    print_section("DEMONSTRATION: ARTICLE SUMMARIZATION")
    
    for idx, text in enumerate(sample_texts, 1):
        print(f"\n📚 ARTICLE {idx}:")
        try:
            summary = summarizer.summarize(text.strip())
            display_summary(text.strip(), summary)
        except Exception as e:
            print(f"❌ Error summarizing article {idx}: {e}\n")
    
    # Interactive mode
    print_section("INTERACTIVE MODE")
    
    while True:
        user_choice = input("Would you like to summarize your own text? (yes/no): ").strip().lower()
        
        if user_choice in ['yes', 'y']:
            print("\n📝 Enter your text (press Enter twice to submit):")
            lines = []
            empty_lines = 0
            
            while True:
                line = input()
                if line == "":
                    empty_lines += 1
                    if empty_lines >= 2:
                        break
                else:
                    empty_lines = 0
                    lines.append(line)
            
            user_text = " ".join(lines)
            
            if user_text.strip():
                try:
                    print("\n⏳ Processing...\n")
                    summary = summarizer.summarize(user_text)
                    display_summary(user_text, summary)
                except Exception as e:
                    print(f"❌ Error: {e}\n")
            else:
                print("❌ No text provided.\n")
        
        elif user_choice in ['no', 'n']:
            print("\n👋 Thank you for using Text Summarization Tool!")
            break
        else:
            print("❌ Invalid input. Please enter 'yes' or 'no'.\n")


if __name__ == "__main__":
    main()
