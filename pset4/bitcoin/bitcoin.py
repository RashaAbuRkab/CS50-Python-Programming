import sys
import requests

def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to convert the argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Fetch the Bitcoin price
    try:
        price = get_bitcoin_price()
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    # Calculate the total cost
    total_cost = bitcoins * price

    # Print the result formatted with commas and four decimal places
    print(f"${total_cost:,.4f}")


def get_bitcoin_price():
    """Fetch the current Bitcoin price in USD."""
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    # Raise an exception if there's an issue with the request
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Extract the current price of Bitcoin in USD
    return data["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    main()
