# Titanic ETL Pipeline

## Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline using Python, Pandas, Seaborn, SQLAlchemy and MySQL.

The project extracts the Titanic dataset, performs data cleaning and transformation, validates the processed data, and loads it into a MySQL database.

It also demonstrates batch processing and provides a Jupyter Notebook containing the complete workflow with explanations and execution results.

## Technologies Used

- Python
- Pandas
- Seaborn
- SQLAlchemy
- MySQL
- MySQL Connector
- Jupyter Notebook
- MySQL Workbench

## Project Workflow

### 1. Data Extraction
- Loads the Titanic dataset using Seaborn.
- Extracts 891 passenger records with 15 columns.

### 2. Data Transformation
- Fills missing age values using the median.
- Fills missing embarked values using the mode.
- Removes unnecessary columns (`deck` and `embark_town`).
- Encodes gender values as male = 0 and female = 1.

### 3. Data Validation
- Checks whether missing values remain.
- Verifies that gender values are encoded as 0 or 1.

### 4. Data Loading
- Loads the cleaned dataset into the MySQL database.
- Creates the `passengers` table.

### 5. Batch Processing
- Processes the dataset in smaller batches.
- Loads the first batch using replace mode.
- Appends subsequent batches to the same table.

## Project Structure

```text
titanic-etl-pipeline/
│
├── Titanic_ETL_Pipeline.ipynb
├── config.example.py
├── extract.py
├── transform.py
├── validate.py
├── load.py
├── pipeline.py
├── batch_pipeline.py
├── test_connection.py
├── test_extract.py
├── test_transform.py
├── test_validate.py
├── README.md
└── .gitignore
```

## Jupyter Notebook

`Titanic_ETL_Pipeline.ipynb` contains the complete ETL workflow, including:
- Project introduction
- Database configuration
- MySQL connection testing
- Data extraction
- Data transformation
- Data validation
- Data loading
- Normal ETL pipeline
- Batch processing
- Database verification
- Conclusion

## Database Configuration

Database name: `titanic_db`

Tables:
- `passengers` – Normal ETL pipeline output.
- `passengers_batch` – Batch processing output.

Configure your local MySQL credentials in `config.py`, using `config.example.py` as a reference.

**Security:** Do not upload your actual database password or `config.py` to GitHub.

## Installation

Install the required packages:

```bash
pip install pandas seaborn sqlalchemy mysql-connector-python notebook
```

Create the MySQL database:

```sql
CREATE DATABASE titanic_db;
```

## How to Run

### Run the Python ETL pipeline

```bash
python pipeline.py
```

### Run batch processing

```bash
python batch_pipeline.py --batch-size 100 --table passengers_batch
```

### Open the Jupyter Notebook

```bash
jupyter notebook
```

Open `Titanic_ETL_Pipeline.ipynb` and run the cells in order.

## Database Verification

Execute these queries in MySQL Workbench:

```sql
USE titanic_db;

SHOW TABLES;

SELECT COUNT(*) FROM passengers;

SELECT COUNT(*) FROM passengers_batch;
```

Expected result after successful execution: 891 records in each table.

## Conclusion

This project demonstrates a complete ETL workflow using Python and MySQL, covering data extraction, cleaning, transformation, validation, database integration and batch processing.
