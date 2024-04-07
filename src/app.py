import streamlit as st
import sqlite3

conn = sqlite3.connect(':memory:')
cursor_obj = conn.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS PATIENT")
cursor_obj.execute("DROP TABLE IF EXISTS STUDY")
cursor_obj.execute("DROP TABLE IF EXISTS WEIGHT")
cursor_obj.execute("DROP TABLE IF EXISTS HEIGHT")
cursor_obj.execute("DROP TABLE IF EXISTS VISIT")

cursor_obj.execute('''CREATE TABLE IF NOT EXISTS PATIENT (
                PK_Patient_ID INTEGER PRIMARY KEY,
                FK_Patient_Weight_Units_ID INTEGER NOT NULL,
                FK_Patient_Height_Units_ID INTEGER NOT NULL,
                FK_VISIT_ID INTEGER NOT NULL,
                FK_STUDY_ID INTEGER NOT NULL,
                Patient_Init TEXT NOT NULL,
                Patient_Weight INTEGER NOT NULL,                
                Patient_Height INTEGER NOT NULL,                
                Patient_DOB TEXT NOT NULL,
                Patient_Age INTEGER NOT NULL,
                PEDIATRIC_DOB TEXT,
                STREET_ADDRESS TEXT,               
                FOREIGN KEY(FK_STUDY_ID) REFERENCES STUDY(PK_STUDY_ID),
                FOREIGN KEY(FK_VISIT_ID) REFERENCES VISIT(PK_VISIT_ID),
                FOREIGN KEY(FK_Patient_Weight_Units_ID) REFERENCES WEIGHT_UNITS(PK_WEIGHT_UNITS_ID),
                FOREIGN KEY(FK_Patient_Height_Units_ID) REFERENCES WEIGHT_UNITS(PK_HEIGHT_UNITS_ID)
            )''')

cursor_obj.execute('''CREATE TABLE IF NOT EXISTS HEIGHT_UNITS (
                PK_HEIGHT_UNITS_ID INTEGER PRIMARY KEY,
                HEIGHT_UNITS TEXT NOT NULL
            )''')

cursor_obj.execute('''CREATE TABLE IF NOT EXISTS WEIGHT_UNITS (
                PK_WEIGHT_UNITS_ID INTEGER PRIMARY KEY,
                WEIGHT_UNITS TEXT NOT NULL
            )''')

cursor_obj.execute('''CREATE TABLE IF NOT EXISTS VISIT (
                PK_VISIT_ID INTEGER PRIMARY KEY,
                VISIT_CODE TEXT NOT NULL,
                FIRST_MORNING_VOID TEXT NOT NULL,
                SITE_NURSE_SIGNATURE  TEXT NOT NULL,
                COLLECTION_DATE TEXT NOT NULL,
                COLLECTION_TIME TEXT NOT NULL,
                PREGNANCY TEXT NOT NULL,
                HEMOGLOBIN_A1C TEXT NOT NULL,
                FASTING_STATUS  TEXT NOT NULL,
                OPTIONAL_TESTING TEXT NOT NULL
            )''')

cursor_obj.execute('''CREATE TABLE IF NOT EXISTS STUDY (
                PK_STUDY_ID INTEGER PRIMARY KEY,
                COLLECTION_DATE TEXT NOT NULL,
                COLLECTION_TIME TEXT NOT NULL,
                SITE_NURSE_SIGNATURE  TEXT NOT NULL
            )''')
conn.commit()
conn.close()

# Title of the web page
st.title('Customer Support Form')

# Select box for problem type
problem_type = st.selectbox(
    'Select your problem type',
    ('Tech Support', 'Email', 'Phones', 'Other')
)

# Input box for problem description
problem_description = st.text_area("Describe your problem")

# Submit button
if st.button('Submit'):
    # You can process the form data here
    st.success(f"Your problem of type '{problem_type}' has been submitted successfully!")
    st.write(f"Problem Description: {problem_description}")
## from the virtualenv activated directory, run..
#

