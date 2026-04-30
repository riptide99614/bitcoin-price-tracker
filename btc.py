#!/usr/bin/env python3
"""Fetch the current BTC/USD spot price from CoinGecko."""

import requests
import sys


API_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_price():
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    try:
        r = requests.get(API_URL, params=params, timeout=5)
        r.raise_for_status()
        return r.json()["bitcoin"]["usd"]
    except requests.RequestException as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    price = get_price()
    print(f"BTC/USD: {price:,.2f}")


if __name__ == "__main__":
    main()
