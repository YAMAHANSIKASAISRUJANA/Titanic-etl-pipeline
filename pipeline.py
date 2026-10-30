
from extract import extract
from transform import transform
from validate import validate
from load import load

def run_pipeline():
    print("\n========== ETL PIPELINE STARTED ==========\n")

    print("STEP 1: Extracting data...")
    raw = extract()

    print("\nSTEP 2: Transforming data...")
    clean = transform(raw)

    print("\nSTEP 3: Validating data...")
    validate(clean)

    print("\nSTEP 4: Loading data into MySQL...")
    load(clean)

    print("\n========== ETL PIPELINE COMPLETED ==========\n")

if __name__ == "__main__":
    run_pipeline()
