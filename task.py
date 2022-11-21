from __init__ import (
    sqlite3,
    DB_NAME,
    LOG_FILE,
    LOG_FORMAT
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

    def connect(self):
        pass

    @property
    def db(self):
        if not self._db:
            return self._start_connection()
        return self._db

    def start_connection(self):
        pass


class Transaction:
    _transaction_data = None
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

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
