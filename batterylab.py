import requests
import json

def run_test(voucher=""):
    """
    Conduct a test on a battery pack by sending a GET request with a voucher.

    Args:
        voucher (str): Voucher code for conducting the test.

    Returns:
        dict: The parsed JSON response from the test endpoint.
    """

    endpoint_url = "https://batterylab.veschgini.com/"

    # Prepare the full URL with the voucher parameter
    full_url = f"{endpoint_url}?voucher={voucher}"

    # Make the GET request
    response = requests.get(full_url)

    # Try parsing the response as JSON
    try:
        result = response.json()
    except ValueError:
        raise Exception("Oops! The BatteryLab server is taking a short break. Please try connecting again later.")
        
    # If there's an error in the response, irrespective of the HTTP status code
    if 'error' in result:
        raise Exception(result['error'])

    # If the response status is not 200
    if response.status_code != 200:
        error_message = result.get('error', f"HTTP Error {response.status_code}: {response.reason}")
        raise Exception(error_message)

    return result
