# RealTimeANAlyst
# 📊 Call Center Hourly Performance Aggregator

> Production-ready Python data pipeline engineered to transform raw call center interval logs into clean hourly operational telemetry, enabling accurate workforce management (WFM), business intelligence (BI), and performance analytics.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Engineering-green)]()
[![License](https://img.shields.io/badge/License-MIT-orange)]()

---

## Overview

Contact center reporting platforms often export operational metrics at granular interval levels, making trend analysis and executive reporting difficult.

This project automates the ingestion, cleansing, normalization, aggregation, and KPI computation of raw workforce management datasets into a structured hourly performance report suitable for:

* Workforce Management (WFM)
* Business Intelligence (BI) Dashboards
* Operational Reporting
* Forecasting and Capacity Planning
* Contact Center Performance Reviews

The pipeline is designed using vectorized Pandas operations to ensure efficiency, maintainability, and scalability.

---

## Business Problem

Raw contact center exports typically contain:

* Multiple time intervals per hour
* Inconsistent datetime formatting
* Human-readable column names
* KPI values mixed with traffic counters
* Manual Excel-based aggregation requirements

These challenges introduce:

* Reporting delays
* Human error
* Inconsistent KPI calculations
* Reduced operational visibility

This solution eliminates manual processing by generating a standardized hourly dataset automatically.

---

## Solution Architecture

```text
┌──────────────────────┐
│    Raw Data.csv      │
│  Contact Center Log  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Datetime Processing  │
│ Date + Start Time    │
│ Timestamp Creation   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Schema Normalization │
│ Column Standardizing │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Hourly Aggregation   │
│ Sum & Mean Metrics   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ KPI Computation      │
│ AHT, ASA, SL, OCC    │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────────┐
│ hourly_performance_report  │
│      CSV Output            │
└────────────────────────────┘
```

---

## Core Features

### Automated Datetime Standardization

Combines:

* Date
* Start Time

into a unified timestamp object using optimized Pandas datetime processing.

---

### Intelligent Aggregation Strategy

The pipeline differentiates between:

#### Volume Metrics

Aggregated using SUM

Examples:

* Offered Calls
* Answered Calls
* Abandoned Calls

#### Performance Metrics

Aggregated using MEAN

Examples:

* AHT
* Service Level
* ASA
* Availability Time

This preserves statistical accuracy.

---

### KPI Calculation Engine

The solution automatically calculates operational KPIs including:

#### Abandonment Rate

```text
Abandoned Calls ÷ Offered Calls × 100
```

Measures customer attrition before agent connection.

---

#### Service Level %

```text
Answered Within Target ÷ Total Offered × 100
```

Measures service efficiency.

---

#### Average Handle Time (AHT)

```text
Talk Time + Hold Time + Wrap Time
```

Measures average interaction duration.

---

#### Average Speed of Answer (ASA)

```text
Total Wait Time ÷ Answered Calls
```

Measures customer wait experience.

---

#### Occupancy %

```text
Handle Time ÷ (Handle Time + Available Time)
```

Measures resource utilization efficiency.

---

## Project Structure

```text
call-center-hourly-performance-aggregator/

├── Raw Data.csv
│
├── app.py
│
├── hourly_performance_report.csv
│
├── README.md
│
└── requirements.txt
```

---

## Data Transformation Matrix

| Source Column | Target Metric         | Aggregation Method |
| ------------- | --------------------- | ------------------ |
| Offered Calls | Offered_Calls         | SUM                |
| ACD Calls     | Answered_Calls        | SUM                |
| Aban Calls    | Abandoned_Calls       | SUM                |
| ACD Time      | Handle_Time           | MEAN               |
| Service Level | Service_Level_Percent | MEAN               |
| Avg Speed Ans | ASA                   | MEAN               |
| Avail Time    | Available_Time        | MEAN               |

---

## Technology Stack

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| Python                | Core Programming Language      |
| Pandas                | Data Transformation Engine     |
| CSV                   | Source & Target Storage Format |
| Datetime              | Temporal Normalization         |
| Vectorized Operations | High Performance Processing    |

---

## Getting Started

### Prerequisites

* Python 3.10+
* Pip Package Manager

---

### Clone Repository

```bash
git clone https://github.com/Tonny-Ooko/call-center-hourly-performance-aggregator.git

cd call-center-hourly-performance-aggregator
```

---

### Create Virtual Environment

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install pandas
```

Or:

```bash
pip install -r requirements.txt
```

---

### Execute Pipeline

```bash
python app.py
```

---

## Input File

Place the source file in the project root:

```text
Raw Data.csv
```

The script automatically loads, transforms, aggregates, and exports the final report.

---

## Output File

Generated automatically:

```text
hourly_performance_report.csv
```

Example:

| Hour  | Offered Calls | Answered Calls | Service Level % | AHT | ASA | Occupancy % |
| ----- | ------------- | -------------- | --------------- | --- | --- | ----------- |
| 08:00 | 124           | 118            | 95.2            | 312 | 18  | 78.6        |
| 09:00 | 147           | 140            | 96.8            | 305 | 16  | 81.2        |

---

## Performance Considerations

The pipeline uses vectorized Pandas transformations instead of iterative row processing.

Benefits:

* Faster execution
* Lower memory overhead
* Better scalability
* Cleaner maintenance

Suitable for:

* Daily operational reporting
* Historical trend analysis
* Workforce planning
* Executive KPI dashboards

---

## Future Enhancements

Potential production upgrades:

* PostgreSQL Integration
* Automated Scheduling (Cron / Airflow)
* Dashboard Integration (Power BI / Tableau)
* Data Validation Framework
* Multi-Site Contact Center Support
* Cloud Storage Integration (AWS S3 / Azure Blob)
* REST API Export Layer
* Docker Containerization

---

## Engineering Principles

This project follows:

* Separation of Concerns
* Data Quality First
* Vectorized Processing
* Reproducible Analytics
* Maintainable Transformation Logic

---

## License

MIT License

---

## Author

Designed and implemented as a data engineering solution for transforming raw contact center operational logs into actionable business intelligence datasets.
