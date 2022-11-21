from __init__ import (
    sqlite3,
    DB_NAME
)


if __name__ == "__main__":
    db = sqlite3.connect(DB_NAME)
    db.execute(
        """
        CREATE TABLE accounts (
            account_id INTEGER NOT NULL,
            balance DECIMAL NOT NULL DEFAULT 0,
            PRIMARY KEY(account_id),
            CHECK(balance >= 0)
        );
        """
    )

    db.execute(
        """
        CREATE TABLE transaction (
            transaction_id INT NOT NULL PRIMARY KEY,
            account_from_id INTEGER NOT NULL,
            account_to_id INTEGER NOT NULL,
            amount DECIMAL NOT NULL, 
            changed_time TEXT NOT NULL,
            state TEXT NOT NULL
        );
        """
    )

