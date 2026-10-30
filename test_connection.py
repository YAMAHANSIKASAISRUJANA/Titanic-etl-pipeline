
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from config import DB_CONFIG

def test_mysql_connection():
    url = URL.create(
        "mysql+mysqlconnector",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"]
    )
    engine = create_engine(url)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT DATABASE(), VERSION()"))
            db, version = result.fetchone()
            print("MySQL connection successful!")
            print(f"Database: {db}")
            print(f"MySQL Version: {version}")
    except Exception as error:
        print(f"MySQL connection failed: {error}")
    finally:
        engine.dispose()

if __name__ == "__main__":
    test_mysql_connection()
