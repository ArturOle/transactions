from __init__ import (
    LOG_FILE,
    LOG_FORMAT,
    DATABASE_PATH,
    sqlalchemy
)
import logging


class DBM:
    _db = None

    def __init__(self):
        logging.basicConfig(
            filename=LOG_FILE,
            filemode="a",
            format=LOG_FORMAT,
            datefmt='%H:%M:%S'
        )

    @property
    def db(self):
        if not self._db:
            return self._start_connection()
        return self.db

    def start_connection(self):
        self.db = sqlalchemy.create_engine(DATABASE_PATH)
        return self.db


class Transaction:
    _transaction_data = None
    _table = None

    def __init__(self, conn):
        self.conn = conn

    @property
    def table(self):
        if not self._table:
            self._table = sqlalchemy.Table(
                'transactions',
                sqlalchemy.Base.metadata,
                autoload=True,
                autoload_with=self.conn
            )

    @property
    def transaction_data(self):
        pass

    def _begin_transaction(self):
        pass

    def _read_account(self):
        pass

    def _update_account(self):
        pass

    def commit(self):
        pass


if __name__ == "__main__":
    database_manager = DBM()
