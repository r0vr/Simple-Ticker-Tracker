# Simple Ticker Tracker
# Owen Pearson
# 1aWeek Project - Week 2

import yfinance as yf
import pandas as pd
import json
import shutil
import os
from pathlib import Path
from datetime import date
from datetime import datetime

# Error codes
ERROR_INVALID_TICKER = "Invalid ticker"
ERROR_INVALID_CHOICE = "Invalid choice"


# Get ticker
def get_stock():
    tick = input("Input ticker: ")
    tick = tick.upper()

    return tick


# Serializing all SEC data to json format
def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    else:
        return TypeError(f"Type {type(obj)} not serializable")


# Check if stock exists
def valid_checker(tick):
    tick_check = yf.Ticker(tick)
    tick_info = tick_check.history(period="1d")
    if tick_info.empty:
        return ERROR_INVALID_TICKER


# Create dir for stock if none exists
def ticker_dir(tick):
    dir_path = f"data/{tick}"
    os.makedirs(dir_path, exist_ok=True)


# Chose whether to view data or get new data
def choose():
    print("1. View saved data")
    print("2. Get new data")
    choice = input(">> ")
    return choice


# Get and print stock data
# TODO: Add more options for data
def get_stock_data(tick):
    """
    Get data for the ticker given by the user
    All data is available to be saved to .csv
    or .json files inside a directory for the
    ticker inside "data".

    """
    df = yf.Ticker(tick)
    while True:
        print(f"Please choose what data to get for {tick}")
        print("1. Income Statement")
        print("2. Analyst Price Targets")
        print("3. History")
        print("4. Info")
        print("5. SEC Filings")
        print("6. Financials")
        choice = input(">> ")

        if choice == "1":
            # Company income statemnts
            dfst = df.income_stmt
            dfst.to_csv(f"{tick}_income_stmt.csv")
            shutil.move(f"{tick}_income_stmt.csv", f"data/{tick}")
            print(f"{tick} income statemnt CSV created")
        elif choice == "2":
            print(df.analyst_price_targets)
        elif choice == "3":
            # Range for statements from single day, months, year to date,
            # up to 10 years
            print("Enter range for ticker history")
            print("1d")
            print("5d")
            print("1mo")
            print("5mo")
            print("1y")
            print("10y")
            print("ytd")
            history_range = input(">> ")
            if history_range == "1d":
                dfc = df.history(period="1d")
            elif history_range == "5d":
                dfc = df.history(period="5d")
            elif history_range == "1mo":
                dfc = df.history(period="1mo")
            elif history_range == "1y":
                dfc = df.history(period="1y")
            elif history_range == "10y":
                dfc = df.history(period="10y")
            elif history_range == "ytd":
                dfc = df.history(period="ytd")
            else:
                print("Invalid range")
            dfc.to_csv(f"{tick}_history_{history_range}.csv")
            shutil.move(f"{tick}_history_{history_range}.csv", f"data/{tick}")
            print(f"{tick} history data CSV created")

        elif choice == "4":
            # Get info about company in json format
            dfi = df.info
            with open(f"{tick}_info.json", "w") as f:
                json.dump(dfi, f, indent=0, default=json_serial)
            shutil.move(f"{tick}_info.json", f"data/{tick}")
            print(f"{tick}_info.json file created")
        elif choice == "5":
            # SEC Filing records in json format
            df = df.sec_filings
            with open(f"{tick}_sec.json", "w") as f:
                json.dump(df, f, indent=0, default=json_serial)
            shutil.move(f"{tick}_sec.json", f"data/{tick}")
            print(f"JSON file created for {tick} filings.")
        elif choice == "6":
            # Company financials in csv format
            dfi = df.financials
            dfi.to_csv(f"{tick}_financials.csv")
            shutil.move(
                f"{tick}_financials.csv",
                f"data/{tick}",
            )
            print(f"{tick} financials CSV created")
        else:
            return ERROR_INVALID_CHOICE
        return


def view_stock_data():
    """
    View saved stock data in the form of
    .csv and .json files. The user will
    input the ticker, and if the ticker
    matches a directory name in /data,
    the contents of the directory will
    be displayed for the user to choose
    from.
    """
    dir_path = Path("data")
    dir_contents = os.listdir(dir_path)
    print(dir_contents)
    print("Select ticker")
    choice = input(">> ")
    try:  # Check if user input matches dir name
        directories = [
            d for d in dir_contents if os.path.isdir(os.path.join(dir_path, d))
        ]

        # If user input matches a directory name,
        # display directory contents.
        if choice in directories:
            dir_match = os.path.join(dir_path, choice)
            new_dir_contents = os.listdir(dir_match)
            print(new_dir_contents)
            print("Select a file to view")
            file_choice = input(">> ")

            # If user input matches file name,
            # display file
            for file_choice in new_dir_contents:
                file = os.path.join(dir_match, file_choice)
                if file.endswith(".csv"):  # Check if file is CSV
                    df = pd.read_csv(file)
                    print(df)
                elif file.endswith(".json"):  # Check if file is JSON
                    df = pd.read_json(file)
                    print(df)
                else:
                    return ERROR_INVALID_CHOICE

        else:
            return ERROR_INVALID_TICKER
    except Exception as e:
        return e


def main():
    try:
        print("+=========================+")
        print("Simple Ticker Tracker")
        print("+=========================+")
        choice = choose()
        if choice == "1":
            view_stock_data()
        elif choice == "2":
            tick = get_stock()
            valid_checker(tick)
            if valid_checker(tick) == ERROR_INVALID_TICKER:
                return None
            ticker_dir(tick)
            get_stock_data(tick)
        else:
            return ERROR_INVALID_CHOICE

    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
