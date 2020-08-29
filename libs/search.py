import os
import requests

ADDRESS_URL = "https://atlas.microsoft.com/search/address/json"
REVERSE_GEO_URL = "https://atlas.microsoft.com/search/address/reverse/json"

API_VERISON = "1.0"


def address(address: str):
    result = requests.get(
        ADDRESS_URL,
        params={
            "api-version": API_VERISON,
            "subscription-key": os.getenv("SUBSCRIPTION_ID"),
            "query": address,
        },
    )
    if result.status_code == 200:
        return result.json()
    raise Exception(result.json())


def reverse_geo(latitude: float, longitude: float, optional_params: dict = {}):
    params = optional_params
    params.update(
        {
            "api-version": API_VERISON,
            "subscription-key": os.getenv("SUBSCRIPTION_ID"),
            "query": f"{str(latitude)},{str(longitude)}",
        }
    )
    result = requests.get(REVERSE_GEO_URL, params=params)
    if result.status_code == 200:
        return result.json()
    raise Exception(result.json())
