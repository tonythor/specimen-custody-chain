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
        col1, col2, col3= st.columns(3)
        with col2:
          patient_initials = st.text_input('Patient Initials')
        with col1:
          patient_id = st.text_input('Patient ID')
        with col3:
            salutation = st.selectbox('Gender', ('Male', 'Female'))

        # Three-column layout for the top part of the form
        col1, col2, col3 = st.columns(3)
        with col2:
            first_name = st.text_input('First Name')
        with col3:
            last_name = st.text_input('Last Name')
        with col1:
            salutation = st.selectbox('Salutation', ('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.'))
        col1, col2, col3= st.columns(3)
        with col3:
         height = st.text_input('Height (cm)')
        with col1:
            weight = st.text_input('Weight')
        with col2:
            weight_unit = st.selectbox('Weight Units', ('NA', 'Pounds', 'Kilograms'))
        col1, col2, col3 = st.columns(3)
        with col1:
            dob = st.date_input('Date of Birth (DOB)', datetime.date.today())
        with col2:
            pediatric_dob = st.date_input('Pediatric Date of Birth', datetime.date.today())
        with col3:
             age = st.text_input('Age (years)')
        street_address = st.text_input('Street Address')
        col1,col2, col3=st.columns(3)
        with col3:
            pregnancy = st.selectbox('Pregnant', ('NA', 'Yes', 'No'))
        with col2:
            fmv = st.selectbox('First Morning Void', ('NA', 'Yes', 'No'))
        with col1:
            visit_code = st.text_input('Visit Code')
        col1, col2,col3= st.columns(3)
        with col1:
            hemoglobin_a1c = st.text_input('Hemoglobin A1C')
        with col2:
            fasting_status=st.selectbox('Fasting', ('NA', 'Yes', 'No'))
        with col3:
            optional_testing=st.selectbox('Optional Test', ('NA', 'Yes', 'No'))
            
        col1, col2, col3= st.columns([1,2,3])
        with col1:
             visit_collection_time = st.time_input('Visit Coll Time')
        with col2:
            visit_collection_date = st.date_input(' Visit Collection Date', datetime.date.today())
        with col3:
          site_nurse_signature = st.text_input('Site Nurse Signature')
    
          
        col1, col2,col3 = st.columns(3)
        with col1:
            study_collection_time = st.text_input(' Study Colllection Time')
        with col2:
            study_collection_date = st.text_input('Study Collection Date', datetime.date.today())
        with col3:
          study_site_nurse_signature = st.text_input(' Study Site Nurse Signature')
           

        # The rest of the form in a single column layout
        record_number = st.text_input('Record Number')
        study_code = st.text_input('Study Code')
        site_id = st.text_input('Site ID')
       
        # patient_initials = st.text_input('Patient Initials')
        # patient_id = st.text_input('Patient ID')
        random_id = st.text_input('Random ID')

     
        
        req_number = st.text_input('Request Number')

        # Submit button
        submit_button = st.form_submit_button(label='Submit')



    if submit_button:
        try:
           
            patient_insert_sql = '''INSERT INTO patient (patient_init, salutation, patient_weight, patient_height, patient_dob, patient_age,pediatric_dob,street_address,first_name,last_name) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?)'''
            st.session_state['conn'].execute(patient_insert_sql, ( patient_initials, salutation,weight,height, dob,age, pediatric_dob,street_address,first_name,last_name))
            st.session_state['conn'].commit()
            visit_insert_sql ='''INSERT INTO visit(visit_code,first_morning_void,pregnancy,hemoglobin_a1c,fasting_status,optional_testing) VALUES(?, ?, ?, ?, ?, ?)'''
            st.session_state['conn'].execute(visit_insert_sql, ( visit_code, fmv,pregnancy,hemoglobin_a1c,fasting_status, optional_testing))
            st.session_state['conn'].commit()
            study_insert_sql ='''INSERT INTO study(collection_time,collection_date,site_nurse_signature) VALUES(?, ?, ?)'''
            st.session_state['conn'].execute(study_insert_sql, (study_collection_time,study_collection_date,study_site_nurse_signature))
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
