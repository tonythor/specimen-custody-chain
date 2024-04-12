import streamlit as st
import datetime
from db_construct import setup_db
import sqlite3


# Assuming 'setup_db' is defined in 'db_construct'
from db_construct import setup_db

if 'conn' not in st.session_state:
    st.session_state['conn'] = setup_db()

# Function to display a date input field
def date_input(label, key):
    return st.text_input(label, key=key, value='')

def create_new_record_form(form_key):
    with st.form(key=form_key):
        # Three-column layout for the top part of the form
        col1, col2, col3 = st.columns(3)
        with col1:
            patient_id = st.text_input('Patient ID')
        with col2:
            patient_initials = st.text_input('Patient Initials')
        with col3:
            salutation = st.selectbox('Gender', ('Male', 'Female'))

        col1, col2 = st.columns(2)
        with col1:
        # This study code will be used to generate the requisition number
        # Requisition number = study_code + record_number
        # record_number will be the primary key in the SQL table and will be unique
            study_code = st.selectbox('Study', ('A1001', 'A2001', 'A3001', 'A4001',
                                                'B1001', 'B2001', 'B3001', 'B4001',
                                                'C1001', 'C2001', 'C3001', 'C4001',
                                                'D1001', 'D2001', 'D3001', 'D4001'))
        with col2:
            visit = st.selectbox('Visit Code', ('UNSA', 'UNSB', 'UNSC', 'UNSD', 
                                                'V101', 'V102', 'V103', 'V104',
                                                'V201', 'V202', 'V203', 'V204',
                                                'V301', 'V302', 'V303', 'V304',
                                                'V401', 'V402', 'V403', 'V404'))

        col1, col2, col3 = st.columns(3)
        with col1:
            collection_date = st.date_input('Collection Date', format="DD-MM-YYYY")
        with col2:
            collection_time = st.time_input('Blood Collection Time')
        with col3:
            urine_time = st.time_input('Urine Collection Time')
        

        # Optional fields
        height = st.text_input('Height (cm)')
        col1, col2 = st.columns([1,2])
        with col1:
            weight = st.text_input('Weight')
        with col2:
            weight_unit = st.selectbox('Weight Units', ('NA', 'Pounds', 'Kilograms'))
        fmv = st.selectbox('First Morning Void', ('NA', 'Yes', 'No'))

        
        
        fasting_status = st.selectbox('Fasting Status', ('NA', 'Yes', 'No'))

        # Choose between DOB and Pediatric DOB
        dob_choice = st.radio("Select Patient Age Category:", ('Adult', 'Pediatric'))

        # Display the appropriate date input field based on the choice
        # THIS DOES NOT WORK AS EXPECTED. IT SHOULD ONLY DISPLAY ONE TYPE OF DOB AFTER SELECTION. FIX LATER.
        # Or we could just keep DOB without the distinction of adult vs pediatric (just for this project)
        #if dob_choice == 'Adult':
        #    dob = st.date_input('Date of Birth', format="DD-MM-YYYY")
        #    pediatric_dob = None
        #else:
        #    dob = None
        #    pediatric_dob = st.date_input('Pediatric Date of Birth', format="DD-MM-YYYY")

        # Define the start and end years
        start_year = 1920
        end_year = 2024

        # Generate a list of date options for the first of January for each year
        date_options = [datetime.date(year, 1, 1) for year in range(end_year, start_year - 1, -1)]

        # Format the date options as strings
        date_options_formatted = [date.strftime('%m-%d-%Y') for date in date_options]

        dob = st.selectbox('DOB', date_options_formatted)

        age = st.text_input('Age (years)')


        blood_options = ('Chemistry', 'Hematology', 'Hemoglobin A1C', 'HIV',
                        'PT/INR/APTT', 'Vitamin D', 'Troponin', 'Renal Panel',
                        'Ferritin', 'BNP', 'Pregnancy', 'Osmolality', 'PK')
        blood_tests = st.multiselect('Blood Tests', blood_options, key=f"{form_key}blood")

        urine_options = ('Urinalysis', 'Creatinine', 'Urine Protein',
                         'Cortisol', 'Ketones', 'Microalbumin', 'Ethyl Gluconoride')
        urine_tests = st.multiselect('Urine Tests', urine_options, key=f"{form_key}urine")

        stool_options = ('Fecal Calprotectin', 'Fecal Lactoferrin', 'Fecal Fat', 'FOBT', 'Fecal pH')
        stool_tests = st.multiselect('Stool Tests', stool_options, key=f"{form_key}stool")

        tissue_options = ('Biopsy', 'TMA', 'Electron Microscopy', 'ICC', 'Mass Spectrometry',
                          'Molecular Genetic', 'PCR')
        tissue_options = st.multiselect('Tissue Tests', tissue_options, key=f"{form_key}tissue")

        specimen_options = ('5 mL SST', '2.5 mL SST', '3 mL EDTA', '2 mL EDTA',
                            '10 mL Boritex', '10 mL Urine Aliquot', '30 mL Urine Aliquot',
                            '30 mL Stool Aliquot', '3.5 mL FBA', 'FRZ 5 mL Cryovial',
                            'FRZ 3 mL Cryovial', 'FRZ 2 mL Cryovial', 'FRZ 5 mL FBA', 'FRZ 3.5 mL FBA',
                            'Tissue Biopsy')
        specimens_sent = st.multiselect('Specimens Sent for Testing', specimen_options, key=f"{form_key}specimen")

        signature = st.text_input('Signature')


        # Submit button
        submit_button = st.form_submit_button(label='Submit', use_container_width=True)

    if submit_button:
        try:
            insert_sql = '''INSERT INTO patient (patient_id, patient_initials) VALUES (?, ?)'''
            st.session_state['conn'].execute(insert_sql, (patient_id, patient_initials))
            st.session_state['conn'].commit()
            st.success("Form Submitted Successfully!")
            st.write("### Form Data:")
            # st.write(f"Record Number: {record_number}")
            # ... (display other form fields if necessary) ...
        except sqlite3.Error as e:
            st.error(f"An error occurred: {e}")

def show_all_records():
    records = st.session_state['conn'].execute("SELECT * FROM patient").fetchall()
    st.write("All Records:", records)

def transmit_data():
    st.write("Data transmission logic goes here")

# Main App Layout
st.sidebar.image("./src/img/logo.png", use_column_width=True)
st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose a page:", ["New Record", "Show All Records", "Transmit"])

if choice == "New Record":
    st.header('New Specimen Entry')
    create_new_record_form("new_record_form")

elif choice == "Show All Records":
    st.header('All Records')
    show_all_records()

elif choice == "Transmit":
    st.header('Transmit Data')
    # transmit_data()
