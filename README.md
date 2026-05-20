# Tableau to Google BI Migration Demo

## Project Overview

This project demonstrates a simplified BI migration from a Tableau-style sales dashboard to a Google BI / Looker Studio-style dashboard. The focus is on maintaining data quality, KPI consistency, and dashboard integrity during migration.

## Business Scenario

A company is replacing Tableau dashboards with Google BI dashboards. The goal is to recreate existing sales KPIs, validate calculations, and prepare documentation for business users.

## Tools Used

- Python
- Pandas
- SQL
- Google Sheets
- Looker Studio / Google BI
- GitHub
- Markdown documentation

## Key Features

- Data quality validation
- KPI comparison between source and target dashboards
- SQL-based KPI validation
- Migration documentation
- User training guide
- Change management notes

## KPIs Validated

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin
- Revenue by Region
- Revenue by Product Category
- Monthly Revenue Trend

## Data Quality Checks

- Missing value check
- Duplicate Order ID check
- Revenue formula validation
- Profit formula validation
- Data type validation
- KPI consistency check

## Migration Validation Result

All core KPIs were successfully validated between the source Tableau-style dashboard and the target Google BI dashboard.

## Repository Structure

```text
data/
notebooks/
sql/
reports/
docs/
README.md

## Step 1: Source Dataset Creation

A synthetic sales dataset was created to simulate the source data used in an existing Tableau dashboard.

The dataset contains 500 sales transactions with fields such as order date, region, country, product category, product name, revenue, cost, profit, customer segment, and sales channel.

This dataset is used as the single source of truth for validating KPI consistency during the migration from a Tableau-style dashboard to a Google BI / Looker Studio dashboard.

## Step 2: Dashboard Migration Planning

A migration plan was created to define the existing Tableau-style dashboard and the target Google BI / Looker Studio dashboard.

The document includes:

- Source dashboard components
- Target dashboard requirements
- KPI calculation logic
- Dashboard filters
- Migration validation rules
- Data quality checks
- Migration risks and mitigation steps
- Success criteria

This step demonstrates the planning and documentation required before migrating a BI dashboard from one reporting tool to another.

## Step 3: Data Quality Validation

A Python validation script was created to check the quality and integrity of the source sales dataset before dashboard migration.

The script validates:

- Missing values
- Duplicate order IDs
- Revenue calculation logic
- Profit calculation logic
- Valid order dates
- Negative revenue, quantity, or unit price values
- Core KPI summary values

This step ensures that the dataset used for the Tableau-to-Google-BI migration is reliable and suitable for dashboard reporting.
## Step 4: SQL KPI Validation Queries

SQL validation queries were created to validate the core business KPIs used in the dashboard migration.

The SQL file includes queries for:

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin
- Revenue by Region
- Revenue by Country
- Revenue by Product Category
- Profit by Sales Channel
- Revenue by Customer Segment
- Monthly Revenue Trend
- Duplicate Order ID checks
- Revenue formula mismatch checks
- Profit formula mismatch checks
- Missing critical value checks
- Negative value checks

These queries simulate how KPI values can be independently validated before and after migrating a dashboard from Tableau to Google BI / Looker Studio.

## Step 5: Google BI / Looker Studio Dashboard

A Google BI / Looker Studio dashboard was created using the sales dataset as the data source.

The dashboard includes:

- Total Revenue scorecard
- Total Profit scorecard
- Total Orders scorecard
- Average Order Value scorecard
- Profit Margin scorecard
- Revenue by Region chart
- Revenue by Product Category chart
- Monthly Revenue Trend chart
- Profit by Sales Channel chart
- Revenue by Customer Segment chart
- Interactive filters for date, region, country, product category, sales channel, and customer segment

The dashboard recreates the same business logic defined in the Tableau-style migration plan.
![DEMO_REPORT](<Screenshot 2026-05-20 215817.png>)

## Step 6: Migration Validation Report

A migration validation report was created to compare KPI values from the source calculation layer with the migrated Google BI / Looker Studio dashboard.

The report validates:

- Total Revenue
- Total Profit
- Total Orders
- Average Order Value
- Profit Margin
- Revenue by Region
- Revenue by Product Category
- Dashboard filter behavior
- Data quality checks

The purpose of this step is to prove that the migrated dashboard preserves KPI consistency and data integrity.


---

# 3. Add Step 7 to `README.md`

Open your `README.md` and add this:

```markdown
## Step 7: User Training Guide

A user training guide was created to help business users understand and use the migrated Google BI / Looker Studio dashboard.

The guide includes:

- Dashboard overview
- KPI definitions
- Instructions for using filters
- Chart interpretation guidance
- Common user questions
- Troubleshooting checklist
- Support ticket instructions
- Suggested training session structure

This step demonstrates the ability to support end users during a BI transformation project.


---

# 3. Add Step 8 to `README.md`

Open your `README.md` and add:

```markdown
## Step 8: Change Management Documentation

Change management notes were created to support the business transition from a Tableau-style dashboard to a Google BI / Looker Studio-style dashboard.

The document includes:

- Migration context
- User-facing changes
- Key migration risks
- Communication plan
- Training plan
- Access and security considerations
- Operational support guidelines
- Support ticket template
- Post-migration review checklist
- Success criteria

This step demonstrates the ability to support both the technical and organizational sides of a BI transformation project.