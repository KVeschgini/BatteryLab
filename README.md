# BatteryLab: Your virtual toolkit for hands-on statistical exploration.

Welcome to **BatteryLab**, a virtual environment designed for students to learn statistical tests. This platform offers you a hands-on experience with sample data to improve your practical knowledge in the field.

## Overview

At the heart of BatteryLab is a function named `run_test`. This function simulates a test on a battery pack. By using a voucher code, you can retrieve sample data to practice and understand statistical tests better.

## Usage

To start with, ensure you have imported the `batterylab` module in your environment. Once done, you can use the `run_test` function as demonstrated below:

### Importing the Module

```python
from batterylab import run_test
```

### Running the Test

Use your provided voucher to call the `run_test` function.

```python
# Using a voucher to retrieve sample data
data = run_test(voucher="YOUR_VOUCHER_CODE_HERE")

print(data)
```

Replace `YOUR_VOUCHER_CODE_HERE` with the actual voucher code provided to you.

## Function Details

Here's a brief overview of the `run_test` function:

```python
def run_test(voucher=""):
    """
    Conduct a test on a battery pack by sending a GET request with a voucher.

    Args:
        voucher (str): Voucher code for conducting the test.

    Returns:
        dict: The parsed JSON response from the test endpoint.
    """
```

**Parameters:**

- `voucher (str)`: The voucher code used for conducting the test. This is an optional parameter; however, using a valid voucher will give you access to the sample data.

**Returns:**

- `dict`: The parsed JSON response from the test endpoint, which contains the sample data.
