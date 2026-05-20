# Tableau to Google BI Migration Plan

## 1. Project Overview

This project simulates the migration of a sales performance dashboard from a Tableau-style reporting environment to a Google BI / Looker Studio-style reporting environment.

The main objective is to ensure that business users receive the same trusted KPI results after migration. The focus is on dashboard recreation, KPI consistency, data quality, and validation.

---

## 2. Business Scenario

The company currently uses a Tableau dashboard to monitor sales performance across regions, countries, product categories, customer segments, and sales channels.

As part of a BI transformation project, this dashboard needs to be migrated to Google BI / Looker Studio.

The migration should ensure that:

- Existing KPIs are recreated correctly
- Dashboard filters behave consistently
- Calculated fields return the same results
- Data quality issues are identified before reporting
- Business users can continue using the dashboard with minimal confusion

---

## 3. Source Dashboard: Tableau-Style Dashboard

The existing Tableau-style dashboard contains the following components:

### KPI Cards

| KPI | Description |
|---|---|
| Total Revenue | Total sales revenue generated |
| Total Profit | Total profit after cost deduction |
| Total Orders | Number of unique orders |
| Average Order Value | Average revenue per order |
| Profit Margin | Profit as a percentage of revenue |

### Charts

| Chart | Purpose |
|---|---|
| Revenue by Region | Shows which region generates the most revenue |
| Revenue by Product Category | Compares sales performance across product categories |
| Monthly Revenue Trend | Shows revenue development over time |
| Profit by Sales Channel | Compares profitability between Online, Retail, and Partner channels |
| Revenue by Customer Segment | Compares B2B and B2C sales performance |

### Filters

| Filter | Purpose |
|---|---|
| Date Range | Allows users to select a reporting period |
| Region | Allows users to analyze a specific region |
| Country | Allows users to analyze a specific country |
| Product Category | Allows users to focus on one product group |
| Sales Channel | Allows users to compare Online, Retail, and Partner sales |
| Customer Segment | Allows users to filter B2B or B2C customers |

---

## 4. Target Dashboard: Google BI / Looker Studio

The target Google BI dashboard will recreate the same business logic using the same source dataset.

The dashboard should include:

- KPI scorecards
- Bar charts
- Time-series chart
- Interactive filters
- Consistent calculated fields
- Clear dashboard labels for business users

The Google BI dashboard should be easy for non-technical business users to understand and use.

---

## 5. KPI Calculation Logic

| KPI | Formula |
|---|---|
| Total Revenue | SUM(Revenue) |
| Total Profit | SUM(Profit) |
| Total Orders | COUNT_DISTINCT(Order_ID) |
| Average Order Value | SUM(Revenue) / COUNT_DISTINCT(Order_ID) |
| Profit Margin | SUM(Profit) / SUM(Revenue) |
| Revenue by Region | SUM(Revenue) grouped by Region |
| Revenue by Product Category | SUM(Revenue) grouped by Product_Category |
| Monthly Revenue Trend | SUM(Revenue) grouped by Month(Order_Date) |
| Profit by Sales Channel | SUM(Profit) grouped by Sales_Channel |
| Revenue by Customer Segment | SUM(Revenue) grouped by Customer_Segment |

---

## 6. Migration Validation Rules

After migration, each KPI must be checked between the source Tableau-style logic and the target Google BI dashboard.

A KPI is considered successfully migrated if:

- The value in the source calculation matches the value in the target dashboard
- The same filters produce the same filtered result
- The calculated fields use the same formula
- The dashboard uses the correct data source
- No duplicate or missing records affect reporting accuracy

---

## 7. Data Quality Checks Before Migration

Before creating the target dashboard, the dataset should be checked for:

| Check | Reason |
|---|---|
| Missing values | Missing values can produce incorrect dashboard results |
| Duplicate Order IDs | Duplicate orders can inflate revenue or order count |
| Revenue formula mismatch | Revenue should equal Quantity × Unit Price |
| Profit formula mismatch | Profit should equal Revenue - Cost |
| Invalid dates | Incorrect dates can break monthly trend analysis |
| Negative revenue | Revenue should not be negative in this sales dataset |
| Invalid categories | Region, Product Category, and Sales Channel should have valid values |

---

## 8. Migration Risks

| Risk | Impact | Mitigation |
|---|---|---|
| KPI formulas differ between Tableau and Google BI | Business users may see different numbers | Document and validate each KPI formula |
| Filters behave differently | Users may get unexpected dashboard results | Test filters one by one |
| Data refresh timing differs | Reports may show different values | Clearly document refresh rules |
| Access rights differ | Some users may not see the dashboard | Prepare security and access documentation |
| Users are unfamiliar with Google BI | Adoption may be slow | Create training material and user guide |

---

## 9. Success Criteria

The migration is successful if:

- All core KPIs are recreated in Google BI
- KPI values match the source calculation
- Filters work correctly
- Data quality checks pass
- Dashboard screenshots and validation results are documented
- Business users can understand how to use the new dashboard

---


This migration plan defines the source Tableau-style dashboard, target Google BI dashboard, KPI formulas, filters, validation rules, data quality checks, migration risks, and success criteria.

The purpose is to show that dashboard migration is not only about rebuilding charts. It also requires KPI validation, data quality checks, user understanding, and clear documentation.