import sqlite3
import logging

def setup_db():
    # Connect to an in-memory SQLite database
    conn = sqlite3.connect(':memory:', check_same_thread=False)

    cursor_obj = conn.cursor()

    # Execute SQL commands
    sql_commands = [
        "DROP TABLE IF EXISTS specimen_records",
        """
        CREATE TABLE IF NOT EXISTS specimen_records (
            pk_specimen_id INTEGER PRIMARY KEY,
            patient_initials TEXT,
            first_name TEXT,
            last_name TEXT,
            salutation TEXT,
            patient_weight INTEGER,
            patient_height INTEGER,
            patient_dob TEXT,
            patient_age INTEGER,
            pediatric_dob TEXT,
            street_address TEXT,
            visit_code TEXT,
            first_morning_void TEXT,
            pregnancy TEXT,
            hemoglobin_a1c TEXT,
            fasting_status TEXT,
            optional_testing TEXT,
            visit_collection_date TEXT,
            visit_collection_time TEXT,
            site_nurse_signature TEXT,
            study_site_nurse_signature TEXT,
            record_number TEXT,  -- Additional fields can be added here if needed
            study_code TEXT,
            site_id TEXT,
            random_id TEXT,
            req_number TEXT,
            gender TEXT
        )
        """,
        """
        INSERT INTO specimen_records (
            patient_initials, first_name, last_name, salutation, patient_weight,
            patient_height,  patient_dob, patient_age, pediatric_dob, street_address, 
            visit_code, first_morning_void, pregnancy, hemoglobin_a1c, fasting_status, 
            optional_testing, visit_collection_date, visit_collection_time, 
            site_nurse_signature, 
            study_site_nurse_signature, record_number, study_code, site_id, 
            random_id, req_number, gender
        ) VALUES 
        ('JD', 'John', 'Doe', 'Mr.', 70,  170,  '1985-06-15', 37, NULL, '1234 Elm St', 
        'V001', 'Yes', 'No', '5.7', 'Yes', 'Blood test', '2023-04-01', '08:00', 
        'Nurse Joy',  'Nurse Joy', 'REC001', 'ST001', 'Site1', 'R001', 'REQ001', 'Male'),

        ('JS', 'Jane', 'Smith', 'Ms.', 60, 160,  '1990-07-20', 32, NULL, '5678 Maple Ave', 
        'V002', 'No', 'No', '5.9', 'No', 'Urine test', '2023-04-02', '09:00', 
        'Nurse Nick',  'Nurse Nick', 'REC002', 'ST002', 'Site2', 'R002', 'REQ002', 'Female'),

        ('LB', 'Liam', 'Brown', 'Dr.', 80,  180, '1988-03-25', 35, NULL, '9101 Oak Lane', 
        'V003', 'Yes', 'No', '5.2', 'Yes', 'DNA test', '2023-04-03', '10:00', 
        'Nurse Anne', 'Nurse Anne', 'REC003', 'ST003', 'Site1', 'R003', 'REQ003', 'NonBinary'),

        ('EM', 'Emma', 'Moore', 'Ms.', 55,  165, '1992-11-08', 30, NULL, '2345 Pine Road', 
        'V004', 'No', 'Yes', '6.1', 'Yes', 'Sugar level', '2023-04-04', '11:00', 
        'Nurse Pat', 'Nurse Pat', 'REC004', 'ST004', 'Site2', 'R004', 'REQ004', 'Female'),

        ('NO', 'Noah', 'Olson', 'Mr.', 90,  182,  '1984-07-19', 39, NULL, '3456 Cedar St.', 
        'V005', 'Yes', 'No', '5.5', 'No', 'Metabolic panel', '2023-04-05', '12:00', 
        'Nurse Sam',  'Nurse Sam', 'REC005', 'ST005', 'Site3', 'R005', 'REQ005', 'Male'),

        ('AM', 'Ava', 'Mason', 'Mrs.', 65,  155, '1993-10-22', 29, NULL, '4567 Spruce Blvd', 
        'V006', 'No', 'Yes', '4.8', 'No', 'Cholesterol test', '2023-04-06', '13:00', 
        'Nurse Kim',  'Nurse Kim', 'REC006', 'ST006', 'Site1', 'R006', 'REQ006', 'Female');
        """
    ]

    for command in sql_commands:
        cursor_obj.execute(command)

    # Commit the changes and close the connection
    conn.commit()
    logging.info("database set up")
    return conn
