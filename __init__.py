import sqlite3
import sqlalchemy

DB_NAME = "big_xyt.db"
LOG_FILE = "transactions.log"
LOG_FORMAT = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
DATABASE_PATH = f"sqlite:////{DB_NAME}"