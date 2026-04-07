#!/usr/bin/env python3
"""
Quick test script for text summarization
"""

from summarizer import TextSummarizer

def main():
    print("🚀 Testing Text Summarization Tool...")

    # Short test text
    test_text = """
    Artificial Intelligence is transforming industries worldwide.
    Machine learning algorithms can now process vast amounts of data
    and make predictions with remarkable accuracy. Companies are
    leveraging these technologies to improve efficiency and gain
    competitive advantages.
    """

    try:
        print("📦 Initializing summarizer...")
        summarizer = TextSummarizer()

        print("✏️  Summarizing test text...")
        summary = summarizer.summarize(test_text.strip())

        print("\n✅ SUCCESS! Text summarization is working.")
        print(f"📄 Original: {len(test_text.split())} words")
        print(f"✏️  Summary: {len(summary.split())} words")
        print(f"📝 Summary: {summary}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()