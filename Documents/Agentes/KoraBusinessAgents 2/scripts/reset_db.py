# scripts/reset_db.py

import sqlite3
import subprocess
import sys

DB_PATH = "data/mvp.db"  # ajusta la ruta

from init_db import main as init_db


def drop_all_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = OFF;")

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)

    tables = cursor.fetchall()

    for (table_name,) in tables:
        print(f"DROP TABLE {table_name}")
        cursor.execute(f'DROP TABLE IF EXISTS "{table_name}";')

    conn.commit()
    conn.close()


def main() -> None:
    print("Limpiando tablas...")
    drop_all_tables()

    print("Recreando tablas...")
    init_db()

    print("Reset de DB completado correctamente.")


if __name__ == "__main__":
    main()