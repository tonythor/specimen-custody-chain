import sqlite3
import logging

def setup_db():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:', check_same_thread=False)

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
            patient_id INTEGER, 
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
        """,
        "INSERT INTO weight_units (weight_units) VALUES ('kg')",
        "INSERT INTO weight_units (weight_units) VALUES ('lb')",
        "INSERT INTO height_units (height_units) VALUES ('cm')",
        "INSERT INTO height_units (height_units) VALUES ('in')",
        
        """INSERT INTO patient (patient_init, first_name, last_name, salutation, patient_weight, patient_height, patient_dob, patient_age, pediatric_dob, street_address) VALUES ('JD', 'John', 'Doe', 'Mr.', 70, 170, '1985-06-15', 37, NULL, '1234 Elm St')""",
        
        """INSERT INTO patient (patient_init, first_name, last_name, salutation, patient_weight, patient_height, patient_dob, patient_age, pediatric_dob, street_address) VALUES ('JS', 'Jane', 'Smith', 'Ms.', 60, 160, '1990-07-20', 32, NULL, '5678 Maple Ave')""",
        
        """INSERT INTO visit (patient_id, visit_code, first_morning_void, site_nurse_signature, collection_date, collection_time, pregnancy, hemoglobin_a1c, fasting_status, optional_testing) VALUES (1, 'V001', 'Yes', 'Nurse Joy', '2023-04-01', '08:00', 'No', '5.7', 'Yes', 'Blood test')""",
        
        """INSERT INTO visit (patient_id, visit_code, first_morning_void, site_nurse_signature, collection_date, collection_time, pregnancy, hemoglobin_a1c, fasting_status, optional_testing) VALUES (2, 'V002', 'No', 'Nurse Nick', '2023-04-02', '09:00', 'No', '5.9', 'No', 'Urine test')"""
    ]

    for command in sql_commands:
        cursor_obj.execute(command)

    # Commit the changes and close the connection
    conn.commit()
    logging.info("database set up")
    return conn
