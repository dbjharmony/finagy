from langchain.tools import tool
from typing import Literal, Optional
from pydantic import BaseModel, Field
from finagy.tools.api import call_api

####################################
# Tools
####################################

class FinancialStatementsInput(BaseModel):
    ticker: str = Field(description="The stock ticker symbol to fetch financial statements for. For example, 'AAPL' for Apple.")
    period: Literal["annual", "quarterly", "ttm"] = Field(description="The reporting period for the financial statements. 'annual' for yearly, 'quarterly' for quarterly, and 'ttm' for trailing twelve months.")
    limit: int = Field(default=10, description="The number of past financial statements to retrieve.")
    report_period_gt: Optional[str] = Field(default=None, description="Filter for financial statements with report periods after this date (YYYY-MM-DD).")
    report_period_gte: Optional[str] = Field(default=None, description="Filter for financial statements with report periods on or after this date (YYYY-MM-DD).")
    report_period_lt: Optional[str] = Field(default=None, description="Filter for financial statements with report periods before this date (YYYY-MM-DD).")
    report_period_lte: Optional[str] = Field(default=None, description="Filter for financial statements with report periods on or before this date (YYYY-MM-DD).")


def _create_params(
    ticker: str,
    period: Literal["annual", "quarterly", "ttm"],
    limit: int,
    report_period_gt: Optional[str],
    report_period_gte: Optional[str],
    report_period_lt: Optional[str],
    report_period_lte: Optional[str]
) -> dict:
    """Helper function to create params dict for Alpha Vantage API calls."""
    # Alpha Vantage uses different parameter names
    params = {"symbol": ticker}
    
    # Map period to Alpha Vantage format
    if period == "annual":
        params["period"] = "annual"
    elif period == "quarterly":
        params["period"] = "quarterly"
    else:  # ttm
        params["period"] = "quarterly"  # Alpha Vantage doesn't have TTM, use quarterly
    
    return params

@tool(args_schema=FinancialStatementsInput)
def get_income_statements(
    ticker: str,
    period: Literal["annual", "quarterly", "ttm"],
    limit: int = 10,
    report_period_gt: Optional[str] = None,
    report_period_gte: Optional[str] = None,
    report_period_lt: Optional[str] = None,
    report_period_lte: Optional[str] = None
) -> dict:
    """
    Fetches a company's income statements, 
    detailing its revenues, expenses, net income, etc. over a reporting period. 
    Useful for evaluating a company's profitability and operational efficiency.
    """
    params = _create_params(ticker, period, limit, report_period_gt, report_period_gte, report_period_lt, report_period_lte)
    data = call_api("INCOME_STATEMENT", params)
    return data.get("annualReports" if period == "annual" else "quarterlyReports", {})

@tool(args_schema=FinancialStatementsInput)
def get_balance_sheets(
    ticker: str,
    period: Literal["annual", "quarterly", "ttm"],
    limit: int = 10,
    report_period_gt: Optional[str] = None,
    report_period_gte: Optional[str] = None,
    report_period_lt: Optional[str] = None,
    report_period_lte: Optional[str] = None
) -> dict:
    """
    Retrieves a company's balance sheets, providing a snapshot of 
    its assets, liabilities, shareholders' equity, etc. at a specific point in time. 
    Useful for assessing a company's financial position.
    """
    params = _create_params(ticker, period, limit, report_period_gt, report_period_gte, report_period_lt, report_period_lte)
    data = call_api("BALANCE_SHEET", params)
    return data.get("annualReports" if period == "annual" else "quarterlyReports", {})

@tool(args_schema=FinancialStatementsInput)
def get_cash_flow_statements(
    ticker: str,
    period: Literal["annual", "quarterly", "ttm"],
    limit: int = 10,
    report_period_gt: Optional[str] = None,
    report_period_gte: Optional[str] = None,
    report_period_lt: Optional[str] = None,
    report_period_lte: Optional[str] = None
) -> dict:
    """
    Retrieves a company's cash flow statements, 
    showing how cash is generated and used across 
    operating, investing, and financing activities. 
    Useful for understanding a company's liquidity and solvency.
    """
    params = _create_params(ticker, period, limit, report_period_gt, report_period_gte, report_period_lt, report_period_lte)
    data = call_api("CASH_FLOW", params)
    return data.get("annualReports" if period == "annual" else "quarterlyReports", {})
