import sqlite3
import logging

def setup_db():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor_obj = conn.cursor()

    # Execute SQL commands
    sql_commands = [
        "DROP TABLE IF EXISTS patient",
        "DROP TABLE IF EXISTS study",
        "DROP TABLE IF EXISTS weight_units",
        "DROP TABLE IF EXISTS height_units",
        "DROP TABLE IF EXISTS visit",
        """
        CREATE TABLE IF NOT EXISTS patient (
            pk_patient_id INTEGER PRIMARY KEY,
            patient_init TEXT,
            first_name TEXT,
            last_name TEXT,
            salutation TEXT,
            patient_weight INTEGER,
            patient_height INTEGER,
            patient_dob TEXT,
            patient_age INTEGER,
            pediatric_dob TEXT,
            street_address TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS height_units (
            pk_height_units_id INTEGER PRIMARY KEY,
            height_units TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS weight_units (
            pk_weight_units_id INTEGER PRIMARY KEY,
            weight_units TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS visit (
            pk_visit_id INTEGER PRIMARY KEY,
            visit_code TEXT,
            first_morning_void TEXT,
            site_nurse_signature TEXT,
            collection_date TEXT,
            collection_time TEXT,
            pregnancy TEXT,
            hemoglobin_a1c TEXT,
            fasting_status TEXT,
            optional_testing TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS study (
            pk_study_id INTEGER PRIMARY KEY,
            collection_date TEXT,
            collection_time TEXT,
            site_nurse_signature TEXT
        )
        """
    ]

    for command in sql_commands:
        cursor_obj.execute(command)

    # Commit the changes and close the connection
    conn.commit()
    logging.info("database set up")
    return conn
