from __init__ import (
    sqlite3,
    DB_NAME
)


if __name__ == "__main__":
    try:
        con = sqlite3.connect(DB_NAME)
        cursor_object = con.cursor()
        cursor_object.executescript(
            """
            CREATE TABLE accounts (
                account_id INTEGER NOT NULL,
                balance DECIMAL NOT NULL DEFAULT 0,
                PRIMARY KEY(account_id)
            );


            CREATE TABLE transactions (
                transaction_id INTEGER NOT NULL,
                account_from_id INTEGER NOT NULL,
                account_to_id INTEGER NOT NULL,
                amount DECIMAL NOT NULL,
                changed_time TEXT NOT NULL,
                transaction_state TEXT NOT NULL,
                PRIMARY KEY(transaction_id),
                FOREIGN KEY(account_from_id) REFERENCES accounts(account_id),
                FOREIGN KEY(account_to_id) REFERENCES accounts(account_id)
            );
            """
        )
    except Exception as err:
        print(err)
