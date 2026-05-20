# Google BI Dashboard User Training Guide

## 1. Purpose of This Guide

This guide helps business users understand how to use the migrated Google BI / Looker Studio sales dashboard.

The dashboard was migrated from a Tableau-style reporting environment to a Google BI / Looker Studio-style environment. The main goal is to keep the same business KPIs while giving users a new reporting interface.

---

## 2. Dashboard Overview

The dashboard provides a sales performance overview using the following business dimensions:

- Region
- Country
- Product Category
- Sales Channel
- Customer Segment
- Order Date

The dashboard helps users answer questions such as:

- How much revenue did we generate?
- Which region performed best?
- Which product category generated the highest revenue?
- Which sales channel was most profitable?
- How did revenue change over time?
- How do B2B and B2C customers compare?

---

## 3. Key KPI Cards

The top section of the dashboard contains KPI scorecards.

| KPI | Meaning |
|---|---|
| Total Revenue | Total sales revenue generated during the selected period |
| Total Profit | Revenue minus cost |
| Total Orders | Number of unique orders |
| Average Order Value | Average revenue generated per order |
| Profit Margin | Percentage of revenue that remains as profit |

---

## 4. KPI Definitions

| KPI | Formula |
|---|---|
| Total Revenue | SUM(Revenue) |
| Total Profit | SUM(Profit) |
| Total Orders | COUNT_DISTINCT(Order_ID) |
| Average Order Value | SUM(Revenue) / COUNT_DISTINCT(Order_ID) |
| Profit Margin | SUM(Profit) / SUM(Revenue) |

---

## 5. How to Use Dashboard Filters

The dashboard includes interactive filters.

| Filter | How to Use It |
|---|---|
| Date Range | Select the reporting period |
| Region Filter | Select one or more regions |
| Country Filter | Select one or more countries |
| Product Category Filter | Focus on specific product groups |
| Sales Channel Filter | Compare Online, Retail, and Partner channels |
| Customer Segment Filter | Compare B2B and B2C customers |

### Example

If you select:

- Region: Europe
- Product Category: Electronics
- Sales Channel: Online

Then the dashboard will only show online electronics sales from Europe.

---

## 6. How to Read the Charts

### Revenue by Region

This chart shows which region generated the most revenue.

Use it to compare regional sales performance.

---

### Revenue by Product Category

This chart compares sales across product groups such as Electronics, Furniture, and Office Supplies.

Use it to identify the strongest product category.

---

### Monthly Revenue Trend

This chart shows how revenue changed over time.

Use it to identify growth, decline, or seasonal patterns.

---

### Profit by Sales Channel

This chart compares profit across sales channels such as Online, Retail, and Partner.

Use it to understand which channel is most profitable.

---

### Revenue by Customer Segment

This chart compares revenue between B2B and B2C customers.

Use it to understand which customer segment contributes more revenue.

---

## 7. Common User Questions

### Why do numbers change when I select a filter?

The dashboard is interactive. When a filter is selected, all KPI cards and charts update based on the selected data.

---

### Why does the Google BI dashboard show different numbers than Tableau?

Possible reasons include:

- Different date range selected
- Different region or product filter selected
- Data refresh timing difference
- Changed KPI calculation logic
- Missing access to some data
- Source data update after migration

Users should first check whether the same filters are applied in both dashboards.

---

### What should I do if a KPI looks wrong?

Please create a support ticket and include:

- Dashboard name
- Screenshot of the issue
- Selected filters
- Expected value
- Actual value
- Date and time when the issue occurred

---

## 8. Basic Troubleshooting Checklist

Before raising a ticket, check:

| Check | Question |
|---|---|
| Date filter | Is the correct reporting period selected? |
| Region filter | Is the correct region selected? |
| Country filter | Is the correct country selected? |
| Product filter | Is the correct product category selected? |
| Data refresh | Was the dashboard recently updated? |
| Access rights | Do you have access to the expected data? |

---

## 9. Support Process

If the issue cannot be solved by checking filters, users should contact the BI support team.

A good support request should contain:

```text
Dashboard: Sales Performance Dashboard
Issue: Total Revenue looks different from Tableau
Expected Value: 125,000
Actual Value: 123,800
Filters Applied: Europe, Electronics, Online, January 2025
Screenshot: Attached
Business Impact: Monthly sales report cannot be finalized