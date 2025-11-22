import sqlite3
from datetime import datetime

DB_FILE = "db/calculator.db"


def initialize_db():
    """Create the operations table if it does not exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS operations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value1 REAL NOT NULL,
        value2 REAL NOT NULL,
        operation TEXT NOT NULL,
        result REAL NOT NULL,
        created_at TEXT NOT NULL
    );
    """
    )

    conn.commit()
    conn.close()


def save_operation(value1: float, value2: float, operation: str, result: float):
    """Insert an operation into SQLite."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO operations (value1, value2, operation, result, created_at)
        VALUES (?, ?, ?, ?, ?)
    """,
        (value1, value2, operation, result, datetime.utcnow().isoformat()),
    )

    conn.commit()
    conn.close()


def get_all_operations():
    """Fetch the list of all stored operations."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, value1, value2, operation, result, created_at FROM operations"
    )
    rows = cursor.fetchall()

    conn.close()
    return rows
