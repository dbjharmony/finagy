import os
import requests

####################################
# API Configuration
####################################

alpha_vantage_api_key = os.getenv("FINANCIAL_DATASETS_API_KEY")  # Using same env var for simplicity


def call_api(function: str, params: dict) -> dict:
    """Helper function to call the Alpha Vantage API."""
    base_url = "https://www.alphavantage.co/query"
    params["apikey"] = alpha_vantage_api_key
    params["function"] = function
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

