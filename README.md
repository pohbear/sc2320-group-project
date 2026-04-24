# Congressional Trading Performance & Anomaly Detection

## Overview

This project investigates the trading activities of U.S. Congress members to determine whether they demonstrate an unfair informational advantage in the stock market. By analyzing public disclosure data (from Capitol Trades) alongside historical market data (S&P 500) and sector classifications, this project aims to uncover anomalous trading patterns and quantify the extent to which politicians outperform the broader market baseline.

The analysis is structured sequentially—progressing from raw data ingestion and feature engineering to statistical hypothesis testing and advanced machine learning modeling. Ultimately, the project seeks to identify which politicians exhibit the most statistically significant and highly unusual returns (using Wilcoxon tests and DBSCAN clustering) and attempts to predict future stock outperformance using a Random Forest Classifier. The results provide quantitative evidence regarding whether specific domain knowledge (such as congressional committee assignments) translates into market outperformance.

## Data Sources

| Data | Where It Came From |
|---|---|
| Congressional trade disclosures | [Capitol Trades](https://www.capitoltrades.com) — scraped automatically |
| Stock price history | Yahoo Finance |

---

## How It Works (layman)

**Step 1 — Clean the data**
Fix messy dates, remove junk trades, standardise formats.

**Step 2 — Explore the data**
Charts showing who trades most, buy vs sell ratios, how late politicians file.

**Step 3 — Measure each trade**
For every trade, calculate whether the stock moved more than usual during the secret window. Also build a "Z_CAR" score that measures sustained drift over the entire window rather than just checking one lucky day.

**Step 4 — Test statistically**
Run a formal statistical test per politician. Apply a correction to make sure we aren't flagging people by random chance.

**Step 5 — Find the outliers**
Group all politicians by their overall trading behaviour. Flag the ones who don't fit any normal group.

**Step 6 — Build a prediction model**
Train a machine learning model to predict whether a BUY trade will beat the S&P 500. The model's top predictors were all blind-spot derived metrics — confirming the blind spot window contains real signal.

---

## Project Structure

```
├── nb1_data_preperation.ipynb
├── nb2_eda.ipynb
├── nb3_feature_engineering.ipynb
├── nb4_hypothesis_test.ipynb
├── nb5_dbscan.ipynb
├── nb6_random_forest.ipynb
├── requirements.txt
└── data/
    ├── raw/                  ← original downloaded files
    ├── processed/            ← cleaned input files
    └── output/               ← all charts and result CSVs
```

> Run notebooks in order 1 → 6. Each notebook depends on outputs from the previous one.

---

## Installation

To set up the project locally, please ensure you have Python installed. You can install all necessary dependencies by running the following commands in your terminal:

```bash
# Clone the repository (if applicable)
# git clone <repository_url>
# cd sc2320-group-project

# It is recommended to use a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

*(Note: In our notebook, there is no pip installation cells, so please do install all the required dependencies on your environment before running the cells.)*

## Usage

This project is structured as a pipeline of numbered Jupyter Notebooks. To reproduce the analysis or explore the data, start a Jupyter Notebook server:

```bash
jupyter notebook
```
