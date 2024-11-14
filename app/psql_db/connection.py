import os
from typing import List

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from app.psql_db.models import Base

load_dotenv(verbose=True)

engine = create_engine(os.environ['PSQL_URL'])
inspector = inspect(engine)
session_maker = sessionmaker(bind=engine)

TABLES_NAME = ['emails', 'locations', 'devices_info', 'hostage_sentences', 'explosive_sentences']


def drop_tables():
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS explosive_sentences CASCADE"))
        connection.execute(text("DROP TABLE IF EXISTS hostage_sentences CASCADE"))
        connection.execute(text("DROP TABLE IF EXISTS emails CASCADE"))
        connection.execute(text("DROP TABLE IF EXISTS locations CASCADE"))
        connection.execute(text("DROP TABLE IF EXISTS devices_info CASCADE"))
        print("All tables have been dropped successfully.")


def create_tables():
    Base.metadata.create_all(engine)
    print("All tables have been created successfully.")


def is_all_tables_exist(table_names: List[str] = TABLES_NAME) -> bool:
    existing_tables = inspector.get_table_names()
    return all(table in existing_tables for table in table_names)


def create_tables_if_not_exist():
    if not is_all_tables_exist():
        drop_tables()
        create_tables()
        print('All tables have been dropped & created successfully.')


if __name__ == "__main__":
    print(is_all_tables_exist())
    create_tables_if_not_exist()
