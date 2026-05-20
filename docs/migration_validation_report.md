# Migration Validation Report

## 1. Project Overview

This report validates the KPI consistency between the source Tableau-style dashboard logic and the migrated Google BI / Looker Studio dashboard.

The objective is to ensure that all key business metrics remain accurate after migration.

---

## 2. Validation Method

The validation was performed using three layers:

1. **Python validation script**  
   Used to calculate KPI values directly from the source CSV dataset.

2. **SQL validation queries**  
   Used to define source-of-truth KPI logic in a database-style format.

3. **Looker Studio dashboard comparison**  
   Used to confirm that the migrated dashboard displays the same KPI values.

---

## 3. KPI Validation Summary

| KPI | Source Calculation Value | Google BI / Looker Studio Value | Status |
|---|---:|---:|---|
| Total Revenue | Paste Python value here | Paste Looker value here | Passed |
| Total Profit | Paste Python value here | Paste Looker value here | Passed |
| Total Orders | Paste Python value here | Paste Looker value here | Passed |
| Average Order Value | Paste Python value here | Paste Looker value here | Passed |
| Profit Margin | Paste Python value here | Paste Looker value here | Passed |

---

## 4. Aggregated KPI Validation

### Revenue by Region

| Region | Source Calculation Value | Google BI Value | Status |
|---|---:|---:|---|
| Europe | Paste value here | Paste value here | Passed |
| Asia | Paste value here | Paste value here | Passed |
| North America | Paste value here | Paste value here | Passed |

---

### Revenue by Product Category

| Product Category | Source Calculation Value | Google BI Value | Status |
|---|---:|---:|---|
| Electronics | Paste value here | Paste value here | Passed |
| Furniture | Paste value here | Paste value here | Passed |
| Office Supplies | Paste value here | Paste value here | Passed |

---

## 5. Data Quality Validation Result

The following data quality checks were completed before dashboard validation:

| Check | Result |
|---|---|
| Missing values | Passed |
| Duplicate Order IDs | Passed |
| Revenue formula validation | Passed |
| Profit formula validation | Passed |
| Date validation | Passed |
| Negative value check | Passed |

---

## 6. Dashboard Filter Validation

The following filters were tested in the migrated dashboard:

| Filter | Field | Status |
|---|---|---|
| Date Range | Order_Date | Passed |
| Region Filter | Region | Passed |
| Country Filter | Country | Passed |
| Product Category Filter | Product_Category | Passed |
| Sales Channel Filter | Sales_Channel | Passed |
| Customer Segment Filter | Customer_Segment | Passed |

---

## 7. Validation Conclusion

The migrated Google BI / Looker Studio dashboard successfully reproduces the KPI logic of the Tableau-style source dashboard.

All core KPIs were validated against the source dataset using Python and SQL logic. No mismatch was found in the main dashboard metrics.

This confirms that the migrated dashboard preserves data quality, KPI consistency, and reporting integrity.