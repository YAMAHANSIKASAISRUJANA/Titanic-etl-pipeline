
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config import DB_CONFIG

def load(df, table_name="passengers", if_exists="replace"):
    connection_url = URL.create(
        drivername="mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"]
    )

    engine = create_engine(connection_url)
    try:
        df.to_sql(name=table_name, con=engine, if_exists=if_exists, index=False)
        print(f"Successfully loaded {len(df)} rows into '{table_name}'.")
    finally:
        engine.dispose()

