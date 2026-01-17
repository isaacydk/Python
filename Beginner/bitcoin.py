#home work
import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=6e8a2d635d901ccedfa725081a54d78e7553c2cd082272867070e46eccf3b914"
            )
    except requests.RequestException:
        sys.exit("requests Exception!!")
    
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total_value = price * n

    print(f"${price:,.4f}")
    
else:
    sys.exit("Missing command-line argument")