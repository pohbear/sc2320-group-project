import csv
import os

import requests
import yfinance as yf
import pandas as pd

# ticker = "^GSPC"  # S&P 500 index


# date range
start = "2023-01-01"
end = "2026-04-01"

output_file = "ticker_data.csv"

def read_ticker_list(filename):
    if not os.path.exists(filename):
        print(f"Ticker list file '{filename}' not found.")
        return []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        tickers = [row[0].strip() for row in reader if row and row[0].strip()]
        ticker_set = set(tickers)
        return ticker_set
    
def write_ticker_list(filename, tickers):
    with open(filename, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker"])
        for ticker in tickers:
            writer.writerow([ticker])

def get_ticker_data(ticker, start, end):
    df = yf.download(
        ticker,
        start=start,
        end=end,
        interval="1d",
        auto_adjust=True,
        actions=True,
        progress=False,
        multi_level_index=False,
    )

    if df is None or df.empty:
        print(f"No data found for {ticker} between {start} and {end}.")
        return None

    # reset index to have date as a column, and then add ticker as column
    # df = df.reset_index()
    # df.insert(0, "Ticker", ticker)

    # df["return_1d"] = df["Close"].pct_change()
    # df["return_5d_fwd"] = df["Close"].shift(-5) / df["Close"] - 1
    # df["return_20d_fwd"] = df["Close"].shift(-20) / df["Close"] - 1
    # df["return_60d_fwd"] = df["Close"].shift(-60) / df["Close"] - 1

    return df
    

    

def get_snp_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    tables = pd.read_html(response.text)
    sp500_table = tables[0]

    tickers = sp500_table["Symbol"].tolist()
    tickers = [t.replace(".", "-") for t in tickers]

    print(sp500_table.head())
    print(tickers[:5])
    print(len(tickers))

    tickers_df = pd.DataFrame(tickers, columns=["Ticker"])
    tickers_df.to_csv("sp500_tickers.csv", index=False)
    return tickers_df

if __name__ == "__main__":
    

    ticker_list = read_ticker_list("base_tickers.csv")
    for ticker in ticker_list:
        t = get_ticker_data(ticker, start, end)
        filename = output_file if output_file else f"{ticker}_{start}_{end}_data.csv"
        if t is None:
            with open("error_tickers.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([ticker])
        else:
            # save to CSV
            with open("valid_tickers.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([ticker])
            t.to_csv(filename, mode="a", index=False, header=not os.path.exists(filename))
            print(t.head())
            print(f"Saved {len(t)} rows to {filename}")

    ##### USED TO GET CLEANED TICKER LIST FROM RAW CAPITOL TRADE DATA #####
    ##### STILL NEED TO CLEAN THE TICKER LIST MANUALLY TO FIX ERRORS BEFORE USING IT TO GET DATA #####
    # ticker_list = read_ticker_list("capitol_trades_tickers.csv")
    # write_ticker_list("cleaned_tickers.csv", ticker_list)

    ##### TESTING #####
    # test = 'AAPL'
    # data = get_ticker_data(test, start, end)
    # print(data)
    # get_snp_tickers()
    


