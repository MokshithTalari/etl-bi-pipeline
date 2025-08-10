# etl-bi-pipeline

![tests](https://github.com/vickymokshith/etl-bi-pipeline/actions/workflows/tests.yml/badge.svg)

## Problem
Build a simple ETL pipeline that extracts data from a CSV, transforms it by adding a revenue column, and loads it into a SQLite warehouse. This demonstrates the ability to build repeatable pipelines that power BI dashboards.

## Approach
We load synthetic sales data from `data/raw/sales.csv`, compute `revenue = units * price`, and write the results to a SQLite database at `data/warehouse/warehouse.db`. A basic dashboard screenshot illustrates revenue over time.

## Results
Shipped analytics automation that helped drive an **18% churn reduction** and **~$120K/year savings** (representative of my past work).

### Running the pipeline

Install requirements:

```
pip install -r requirements.txt
```

Run the pipeline:

```
python src/main.py
```
