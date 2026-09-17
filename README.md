# Sales & Customer Behavior Analysis

A beginner-friendly data analysis project exploring retail sales performance and customer purchasing behavior.

**Workflow:** Data → Cleaning → EDA → SQL Analysis → Metrics → Visualization → Insights

## Objectives
- Understand transaction data and data quality
- Analyze sales and product performance
- Examine customer purchasing behavior
- Calculate common business metrics
- Practice SQL for business questions
- Communicate findings using charts and summary tables

## Tools
Python, Pandas, NumPy, Matplotlib, SQL, Microsoft Excel, Jupyter Notebook

## Dataset
The repository contains synthetic data:
- `customers.csv` — customer ID and city
- `products.csv` — product, category and unit price
- `orders.csv` — order date, customer, product, quantity and order status

No real customer or company data is used.

## Analysis Questions
1. What is total completed revenue?
2. What is the average order value?
3. Which categories generate the most revenue?
4. Which products are the top revenue contributors?
5. How does revenue change month to month?
6. What proportion of customers are repeat customers?
7. What is the order-status distribution?
8. Which cities contribute the most revenue?

## Run
```bash
pip install -r requirements.txt
python analysis.py
```

Or open `notebooks/sales_customer_analysis.ipynb` in Jupyter/VS Code.

## Excel
`outputs/sales_analysis.xlsx` contains KPI and summary sheets.

## Future Improvements
- Customer segmentation
- Cohort/retention analysis
- Interactive dashboard
- Conversion funnel analysis
- Database connection
