# Data Quality Assessment Report

## Project: Sales Data Cleaning Review

### Executive Summary
This report summarizes the data quality assessment performed on the sales dataset used for this portfolio project. The dataset contains 180 records and 16 columns, covering customer, order, product, and transaction information. The objective of the review was to identify structural, formatting, and value-level issues that could affect downstream analysis, business reporting, and data-driven decision-making.

The assessment found that 16 rows, or 8.89% of the dataset, contained at least one data quality issue. The most common problems were missing values, inconsistent text casing, duplicate records, invalid payment method labels, inconsistent order status values, and one negative quantity value. Although the dataset is relatively small, these issues are operationally significant because they can lead to inaccurate aggregation, misleading KPIs, and flawed customer or sales insights.

---

## 1. Scope and Objective
The purpose of this quality review was to evaluate the integrity of the source sales data before it was processed for analysis. The assessment focused on:

- identifying missing or incomplete records
- checking consistency in categorical values
- validating numeric fields and date format
- detecting duplicates and outliers
- reviewing fields expected to support customer and sales reporting

This review was completed as a practical data quality exercise and reflects the type of checks commonly performed during an analyst’s initial data validation step.

---

## 2. Data Profile

### Dataset overview
- Total rows: 180
- Total columns: 16
- Geographic scope: Arizona (AZ only)
- Data categories: customer details, transaction details, order status, product, sales representative, and payment information

### Key fields reviewed
- Customer ID
- Customer Name
- Email
- Phone
- Order Date
- City
- State
- Product
- Category
- Quantity
- Unit Price
- Sales Rep
- Customer Type
- Payment Method
- Order Status
- Discount

---

## 3. Methodology
The review was performed using a structured data quality approach:

1. Reviewed column structure and field types
2. Checked for missing values across all columns
3. Assessed duplicate records
4. Validated categorical consistency for payment method, customer type, category, and order status
5. Reviewed numeric fields for impossible or invalid values
6. Evaluated formatting consistency for fields such as phone numbers and dates
7. Documented findings and recommended remediation steps

---

## 4. Summary of Findings

### Overall Data Quality Snapshot

| Metric | Value |
| --- | ---: |
| Total rows | 180 |
| Total columns | 16 |
| Rows with at least one quality issue | 16 |
| Percentage impacted | 8.89% |
| Clean rows | 164 |
| Duplicate rows | 4 |
| Missing-value rows | 11 |
| Records with invalid numeric values | 1 |

### Quality Issue Summary

| Data Quality Area | Observation | Business Impact | Severity |
| --- | --- | --- | --- |
| Missing values | 11 rows had at least one missing field | Incomplete records and inconsistent reporting | Medium |
| Duplicates | 4 duplicated records identified | Can inflate transaction counts | Medium |
| Numeric anomalies | 1 record had a negative quantity | Invalid transaction data | High |
| Inconsistent labels | Payment method and order status contained multiple variants | Fragmented segmentation and reporting | High |
| Formatting inconsistencies | Text casing and field formatting varied across rows | Reduced readability and data consistency | Medium |
| Data type issues | Unit Price and Order Date required standardization | Errors in downstream aggregation | Medium |

### Overall data quality rate
- Rows with at least one quality issue: 16
- Percentage impacted: 8.89%
- Clean rows: 164

This indicates that the dataset is mostly usable but not yet suitable for analysis without a cleaning step.

---

## 5. Detailed Findings

### 5.1 Missing values
The dataset had a relatively low but meaningful number of missing values. The missing records were spread across several columns, including customer name, email, phone, order date, city, quantity, unit price, sales rep, payment method, and discount.

#### Missing value summary

| Column | Missing Count | % Missing |
| --- | ---: | ---: |
| Customer_ID | 0 | 0.00% |
| Customer_Name | 1 | 0.56% |
| Email | 2 | 1.11% |
| Phone | 1 | 0.56% |
| Order_Date | 1 | 0.56% |
| City | 1 | 0.56% |
| State | 0 | 0.00% |
| Product | 0 | 0.00% |
| Category | 0 | 0.00% |
| Quantity | 1 | 0.56% |
| Unit_Price | 1 | 0.56% |
| Sales_Rep | 1 | 0.56% |
| Customer_Type | 0 | 0.00% |
| Payment_Method | 1 | 0.56% |
| Order_Status | 0 | 0.00% |
| Discount | 1 | 0.56% |

#### Interpretation
Missing values are concentrated in operational and customer-contact fields, which could affect customer analysis, fulfillment workflows, and campaign follow-up. The dataset’s core transaction fields are mostly complete, but missing values still require handling before reporting.

### 5.2 Duplicate records
The dataset contained 4 duplicated rows. Duplicate entries are a data quality risk because they can incorrectly increase sales volume, customer counts, or return rates if not removed before analysis.

#### Impact
- inflated transaction totals
- duplicate customer/contact records
- inaccurate trend analysis over time

### 5.3 Numeric anomalies and invalid values
The Quantity column had a minimum value of -2.0, which is an invalid quantity for a customer order in this business context. This was the clearest data integrity issue in the numeric fields.

#### Quantity summary

| Metric | Value |
| --- | ---: |
| Mean | 4.704 |
| Median | 5.000 |
| Min | -2.000 |
| Max | 8.000 |

The negative value likely indicates a data-entry or transformation issue and should be reviewed with the source system to confirm whether it was intended or a recording error.

### 5.4 Inconsistent categorical values
Several categorical fields had multiple representations of the same value, which is a common issue in real-world datasets.

#### Payment Method variations
The Payment_Method field included inconsistent values such as:

- Credit Card
- Credit Card (lowercase)
- PayPal
- paypal
- CC
- Debit
- Debit Card
- Pay Pal
- Cash

This created multiple labels for the same logical categories and would cause grouping issues in reports if left untreated.

#### Order Status variations
The Order_Status field contained values such as:

- Completed
- Cancelled
- Pending
- complete
- cancelled
- pending
- CANCEL
- COMPLETED

This suggests inconsistent data entry and inconsistent case handling. Without standardization, sales reviews by order state would be fragmented and inaccurate.

#### Customer Type variations
The Customer_Type field included values such as:

- Returning
- New
- returning
- new
- Y
- N

These values represent the same logic with different encodings and case differences. Standardizing these labels is necessary for reliable segmentation.

### 5.5 Category inconsistency
The Category field had multiple variants such as:

- Accessories
- Computer
- Office
- accessories
- ACCESSORIES
- computers
- office

This is a typical example of poor data hygiene, where category values were entered inconsistently across the dataset. A cleaned category field is essential for product analysis and sales trend reporting.

### 5.6 Formatting issues
A number of fields had formatting problems that would negatively affect analysis and reporting:

- inconsistent capitalization for city, product, and sales representative names
- whitespace issues in text fields
- inconsistent phone number formatting
- varying date formatting and type interpretation

The dataset also showed a mix of string and numeric data types for several fields, indicating that a standardized transformation step is required before analysis.

---

## 6. Business Impact
The issues identified in this dataset have practical consequences for business reporting and analysis:

- sales totals may be overstated due to duplicate rows
- customer segmentation may be inaccurate due to inconsistent customer type labels
- order status reporting may be fragmented and misleading
- product analysis may be distorted by category inconsistencies
- payment method summaries could misrepresent customer preference trends
- missing values may affect customer outreach and retention analyses

If used without cleaning, these issues could reduce trust in dashboards, KPI reporting, and executive summaries.

---

## 7. Data Cleaning Approach
The remediation approach should include the following controls:

1. Standardize column names and remove whitespace
2. Convert text fields to consistent case and formatting rules
3. Normalize category values to a clean business vocabulary
4. Standardize order status values such as Completed, Cancelled, and Pending
5. Map payment values to consistent labels such as Credit Card, Debit Card, Cash, and PayPal
6. Remove duplicate rows based on business keys or full-record comparison
7. Replace missing values using domain logic or flag them for review
8. Correct negative quantity values and review source-system root cause
9. Convert Price, Quantity, and Discount to numeric types
10. Reformat phone numbers and date values to standard business formats

---

## 8. Recommended Quality Controls
To reduce recurrence, the following data validation rules should be implemented before future uploads:

- required values for Customer Name, Email, Quantity, Unit Price, and Order Date
- valid payment methods restricted to approved categories
- valid order status values from a controlled list
- category and product validation using master reference tables
- duplicate detection based on Customer ID and Order Date
- numeric validation for Quantity and Discount
- date validation to reject impossible or malformed dates
- standardized phone number pattern check

---

## 9. Conclusion
The dataset is usable for a data cleaning exercise and demonstrates many of the issues commonly seen in real business datasets. While the overall issue rate is moderate at 8.89%, the specific problems are significant enough to affect reporting quality if not addressed. The most important issues are duplicate records, inconsistent categorical values, and invalid numeric entries.

With a structured cleaning process and a few validation controls, the data can be transformed into a reliable source for sales analysis, reporting, and operational review. This project serves as a strong example of the type of quality review a data analyst would perform during the early stages of a data analysis workflow.

---

## 10. Final Assessment
Status: Requires cleaning before analysis

Data quality rating: Moderate

Recommended next step: standardize values, remove duplicates, validate numeric fields, and re-run quality checks before using the dataset for reporting or analysis.
