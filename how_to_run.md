# How to Run FinAgy

FinAgy is an autonomous financial research agent that performs deep analysis using task planning, introspection, and real-time market data. This guide shows you how to run it in Cursor.

## Prerequisites

- Python 3.9+ (tested with Python 3.9.6)
- OpenAI API key
- Alpha Vantage API key (free tier available)

## Setup

1. **Install Dependencies**
   ```bash
   pip3 install langchain langchain-openai openai prompt-toolkit pydantic python-dotenv requests
   ```

2. **Configure API Keys**
   - Copy the environment template:
     ```bash
     cp env.example .env
     ```
   - Edit `.env` file and add your API keys:
     ```
     OPENAI_API_KEY=your-openai-api-key
     FINANCIAL_DATASETS_API_KEY=your-alpha-vantage-api-key
     ```

3. **Get API Keys**
   - **OpenAI**: Get from https://platform.openai.com/api-keys
   - **Alpha Vantage**: Get free key from https://www.alphavantage.co/support/#api-key

## Running FinAgy

### Option 1: Command Line Queries (Recommended for Cursor)

Use the `run_finagy.py` script for specific queries:

```bash
python3 run_finagy.py "your question here"
```

**Examples:**
```bash
python3 run_finagy.py "What is Apple's current market cap?"
python3 run_finagy.py "Compare Tesla and Ford's P/E ratios"
python3 run_finagy.py "Show me Microsoft's latest quarterly earnings"
python3 run_finagy.py "What is Amazon's debt-to-equity ratio?"
```

**Help:**
```bash
python3 run_finagy.py
```

### Option 2: Interactive Mode

For a full interactive session (requires proper terminal):

```bash
PYTHONPATH=/Users/dusanjovanovic/Code/acceletores/dexter/src python3 -m finagy.cli
```

## What You Can Ask

FinAgy can handle various financial research queries:

### Market Data
- "What is [Company]'s current market cap?"
- "What is [Company]'s current stock price?"
- "Show me [Company]'s market valuation"

### Financial Ratios
- "What is [Company]'s P/E ratio?"
- "What is [Company]'s debt-to-equity ratio?"
- "Show me [Company]'s profit margins"

### Earnings & Financial Statements
- "Show me [Company]'s latest quarterly earnings"
- "What was [Company]'s revenue growth over the last 4 quarters?"
- "Analyze [Company]'s cash flow trends over the past year"

### Comparisons
- "Compare [Company A] and [Company B]'s revenue"
- "Compare Microsoft and Google's operating margins for 2023"
- "How do Tesla and Ford's P/E ratios compare?"

## How It Works

FinAgy automatically:

1. **Plans** - Breaks down your question into structured research tasks
2. **Executes** - Fetches data from Alpha Vantage API
3. **Validates** - Checks its own work and iterates if needed
4. **Analyzes** - Performs calculations and analysis
5. **Responds** - Provides comprehensive, data-rich answers

## Example Output

```
Query: What is Apple's current market cap?

╭─ Planned Tasks
│  + Fetch a snapshot of the most current financial metrics for Apple (AAPL), including market capitalization.
╰──────────────────────────────────────────────────

✓ Tasks planned
▶ Task: Fetch a snapshot of the most current financial metrics for Apple (AAPL), including market capitalization.
✓ Thinking ✓
✓ Optimizing tool call ✓
✓ Executing get_financial_metrics_snapshot ✓
✓ Validating ✓
✓ Completed │ Fetch a snapshot of the most current financial metrics for Apple (AAPL), including market capitalization.
✓ Answer ready

╔══════════════════════════════════════════════════════════════════════════════╗
║                                    ANSWER                                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║ Apple's current market capitalization is approximately $3.90 trillion USD    ║
║ as of the latest available data (June 30, 2025).                             ║
║                                                                              ║
║ Market Capitalization: $3,899,609,055,000                                    ║
║                                                                              ║
║ This figure reflects Apple's position as one of the most valuable            ║
║ publicly traded companies in the world. The market cap is calculated         ║
║ based on the total number of shares outstanding (14,840,390,000)             ║
║ multiplied by the current share price. Apple's valuation continues to        ║
║ lead the technology sector and the broader market.                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Make sure you're running from the project directory
   - Check that dependencies are installed

2. **API key errors**
   - Verify your `.env` file has the correct API keys
   - Check that the keys are valid and have sufficient credits

3. **Interactive mode not working in Cursor**
   - Use the `run_dexter.py` script instead
   - This is expected behavior in integrated terminals

### Getting Help

- Run `python3 run_dexter.py` without arguments to see usage examples
- Check the main README.md for more detailed information
- Ensure your API keys are properly configured in the `.env` file

## API Limits

- **Alpha Vantage Free Tier**: 5 API calls per minute, 500 calls per day
- **OpenAI**: Depends on your plan and usage

## Architecture

Dexter uses a multi-agent architecture:
- **Planning Agent**: Analyzes queries and creates structured task lists
- **Action Agent**: Selects appropriate tools and executes research steps  
- **Validation Agent**: Verifies task completion and data sufficiency
- **Answer Agent**: Synthesizes findings into comprehensive responses

---

**Ready to start?** Try: `python3 run_finagy.py "What is Apple's current market cap?"`
