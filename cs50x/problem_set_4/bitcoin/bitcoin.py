import json
import requests
import sys

try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    elif len(sys.argv) > 1 and (sys.argv[1])[0].isdigit():
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = bitcoin.json()
        usd_price = float(json.dumps(data["bpi"]["USD"]["rate_float"])) * float(
            sys.argv[1]
        )
        print(f"${usd_price:,.4f}")
    else:
        print("Command-line argument is not a number")
        sys.exit(1)
except ValueError:
    print("U are dummb")
    sys.exit(1)
