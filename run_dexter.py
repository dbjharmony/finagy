#!/usr/bin/env python3
"""
Simple script to run FinAgy queries from the command line.
Usage: python3 run_finagy.py "your question here"
"""

import os
import sys
sys.path.insert(0, '/Users/dusanjovanovic/Code/acceletores/dexter/src')

from dotenv import load_dotenv
load_dotenv()

from finagy.agent import Agent

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 run_finagy.py 'your question here'")
        print("\nExample queries:")
        print("  python3 run_finagy.py \"What is Apple's current market cap?\"")
        print("  python3 run_finagy.py \"Compare Tesla and Ford's P/E ratios\"")
        print("  python3 run_finagy.py \"Show me Microsoft's latest quarterly earnings\"")
        return
    
    query = " ".join(sys.argv[1:])
    print(f"Query: {query}\n")
    
    try:
        agent = Agent()
        agent.run(query)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
