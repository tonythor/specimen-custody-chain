import streamlit as st
import datetime
from db_construct import setup_db
import sqlite3


if 'conn' not in st.session_state:
    st.session_state['conn'] = setup_db()

# Function to display a date input field
def date_input(label, key):
    return st.text_input(label, key=key, value='', placeholder='DD MMM YYYY')


def create_new_record_form():
    with st.form(key='data_entry_form'):
        # Three-column layout for the top part of the form
        col1, col2, col3 = st.columns(3)
        with col1:
            first_name = st.text_input('First Name')
        with col2:
            last_name = st.text_input('Last Name')
        with col3:
            salutation = st.selectbox('Salutation', ('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.'))

        col1, col2 = st.columns([2, 1])
        with col1:
            collection_time = st.time_input('Collection Time')
        with col2:
            collection_date = st.date_input('Collection Date', datetime.date.today())

        # The rest of the form in a single column layout
        record_number = st.text_input('Record Number')
        study_code = st.text_input('Study Code')
        site_id = st.text_input('Site ID')
        site_address = st.text_input('Site Address')
        patient_initials = st.text_input('Patient Initials')
        patient_id = st.text_input('Patient ID')
        random_id = st.text_input('Random ID')

        col1, col2 = st.columns(2)
        with col1:
            dob = st.date_input('Date of Birth (DOB)', datetime.date.today())
        with col2:
            pediatric_dob = st.date_input('Pediatric Date of Birth', datetime.date.today())
        
        req_number = st.text_input('Request Number')

        # Submit button
        submit_button = st.form_submit_button(label='Submit')



    if submit_button:
        try:
            insert_sql = '''INSERT INTO patient (first_name, last_name, salutation) VALUES (?, ?, ?)'''
            st.session_state['conn'].execute(insert_sql, (first_name, last_name, salutation))
            st.session_state['conn'].commit()
            st.success("Form Submitted Successfully!")
            st.write("### Form Data:")
            st.write(f"Record Number: {record_number}")
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
    create_new_record_form()

elif choice == "Show All Records":
    st.header('All Records')
    show_all_records()

elif choice == "Transmit":
    st.header('Transmit Data')
    # transmit_data()
# streamlit run ./src/app.py 