import os
from typing import List

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from app.psql_db.models import Base

load_dotenv(verbose=True)

engine = create_engine(os.environ['PSQL_URL'])
inspector = inspect(engine)
session_maker = sessionmaker(bind=engine)

TABLES_NAME = ['emails', 'locations', 'devices_info', 'sentences']

def drop_tables():
    Base.metadata.drop_all(engine)
    print("All tables have been dropped successfully.")


def create_tables():
    Base.metadata.create_all(engine)
    print("All tables have been created successfully.")


def is_all_tables_exist(table_names: List[str] = TABLES_NAME) -> bool:
    existing_tables = inspector.get_table_names()
    return all(table in existing_tables for table in table_names)


if __name__ == "__main__":
    check_result = is_all_tables_exist()
    print(check_result)
