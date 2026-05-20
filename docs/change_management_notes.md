# Change Management Notes

## 1. Purpose

This document outlines the change management considerations for migrating a Tableau-style sales dashboard to a Google BI / Looker Studio-style dashboard.

The goal is to ensure that business users can transition smoothly to the new dashboard while maintaining trust in KPI values, data quality, and reporting processes.

---

## 2. Migration Context

The organization is moving from a Tableau-style reporting environment to a Google BI / Looker Studio-style environment.

The migrated dashboard keeps the same core business KPIs, but users will interact with a new reporting interface.

The main focus areas are:

- KPI consistency
- Data integrity
- User adoption
- Clear communication
- Training and support
- Access control
- Operational stability

---

## 3. What Changes for Users

| Area | Previous State | New State |
|---|---|---|
| Reporting tool | Tableau-style dashboard | Google BI / Looker Studio-style dashboard |
| Dashboard layout | Existing Tableau layout | Recreated Google BI layout |
| Filters | Tableau filters | Looker Studio controls |
| KPI cards | Tableau KPI cards | Looker Studio scorecards |
| Access | Existing Tableau permissions | Google-based access permissions |
| Support | Existing BI support process | Updated support process for migrated dashboard |

---

## 4. What Stays the Same

The following business logic should remain unchanged:

- Total Revenue formula
- Total Profit formula
- Total Orders calculation
- Average Order Value calculation
- Profit Margin calculation
- Revenue by Region logic
- Revenue by Product Category logic
- Monthly Revenue Trend logic

Users should see the same business meaning, even though the reporting tool has changed.

---

## 5. Key Migration Risks

| Risk | Impact | Mitigation |
|---|---|---|
| KPI mismatch between old and new dashboard | Loss of trust in the migrated dashboard | Validate KPIs using Python and SQL before rollout |
| Users apply different filters | Users may see different numbers | Provide filter usage instructions |
| Users are unfamiliar with Google BI | Slow adoption and repeated support requests | Provide training guide and demo session |
| Data refresh timing differs | Dashboard values may not match at the same time | Document refresh schedule clearly |
| Access permissions are incorrect | Some users may not see required data | Review user access before go-live |
| Dashboard layout feels different | Users may struggle to find information | Keep layout simple and close to old dashboard |
| Missing documentation | Support team may receive unclear tickets | Provide troubleshooting and ticket templates |

---

## 6. Communication Plan

Before rollout, users should be informed about:

- Why the dashboard is being migrated
- When the new dashboard will be available
- Whether the old dashboard will still be accessible temporarily
- What KPIs are included
- How to use filters
- Whom to contact for support

Example communication message:

```text
Dear users,

As part of our BI transformation, the Sales Performance Dashboard has been migrated from a Tableau-style reporting environment to a Google BI / Looker Studio-style dashboard.

The new dashboard contains the same core KPIs, including Total Revenue, Total Profit, Total Orders, Average Order Value, and Profit Margin.

Please use the attached training guide to understand the new dashboard layout and filters. If you notice any data inconsistency, please raise a support ticket with a screenshot, selected filters, expected value, and actual value.

Best regards,
BI Support Team