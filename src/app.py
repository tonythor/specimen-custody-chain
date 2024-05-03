import streamlit as st
import datetime
from db_single_table import setup_db
from data_manager import DataManager
from submission_data import SubmissionData

if 'conn' not in st.session_state:
    st.session_state['conn'] = setup_db()

data_manager = DataManager(st.session_state['conn'])

def create_new_record_form():
    record = None
    if 'current_record' in st.session_state:
        record_id = st.session_state['current_record']
        record = data_manager.fetch_record_by_id(record_id)
        if record:
            print("Record fetched:", record.__dict__) 
        if record is None:
            st.error("Failed to load the record.")
            return
    with st.form(key='data_entry_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            pk_specimen_id = st.text_input('Specimen Id (do not edit)', value=record.pk_specimen_id if record else '')
            first_name = st.text_input('First Name', value=record.first_name if record else '')
            patient_weight = st.text_input('Weight (lbs)', value=str(record.patient_weight) if record else '')
            patient_dob = st.date_input('Date of Birth (DOB)', value=datetime.datetime.strptime(record.patient_dob, '%Y-%m-%d').date() if record else datetime.date.today())
            visit_code = st.text_input('Visit Code', value=record.visit_code if record else '')
            hemoglobin_a1c = st.text_input('Hemoglobin A1C', value=record.hemoglobin_a1c if record else '')
            visit_collection_time = st.time_input('Visit Collection Time', value=datetime.datetime.strptime(record.visit_collection_time, '%H:%M').time() if record else datetime.datetime.now().time())
            record_number = st.text_input('Record Number', value=record.record_number if record else '')
            random_id = st.text_input('Random ID', value=record.random_id if record else '')
        with col2:
            patient_initials = st.text_input('Patient Initials', value=record.patient_initials if record else '')
            last_name = st.text_input('Last Name', value=record.last_name if record else '')
            pediatric_dob = st.date_input('Pediatric Date of Birth', value=datetime.datetime.strptime(record.pediatric_dob, '%Y-%m-%d').date() if record and record.pediatric_dob else datetime.date.today())
            fmv = st.selectbox('First Morning Void', ('NA', 'Yes', 'No'), index=('NA', 'Yes', 'No').index(record.first_morning_void) if record else 0)
            fasting_status = st.selectbox('Fasting', ('NA', 'Yes', 'No'), index=('NA', 'Yes', 'No').index(record.fasting_status) if record else 0)
            visit_collection_date = st.date_input('Visit Collection Date', value=datetime.datetime.strptime(record.visit_collection_date, '%Y-%m-%d').date() if record else datetime.date.today())
            study_code = st.text_input('Study Code', value=record.study_code if record else '')
            req_number = st.text_input('Request Number', value=record.req_number if record else '')
            site_id = st.text_input('Site ID', value=record.site_id if record else '')
        with col3:
            salutation = st.selectbox('Salutation', ('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.'), index=('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.').index(record.salutation) if record else 0)
            gender_options = ('Male', 'Female', 'NonBinary')
            gender_index = gender_options.index(record.gender) if record and record.gender in gender_options else 0
            gender = st.selectbox('Gender', gender_options, index=gender_index)
            patient_height = st.text_input('Height (inches)', value=str(record.patient_height) if record else '')
            patient_age = st.text_input('Age (years)', value=str(record.patient_age) if record else '')
            street_address = st.text_input('Street Address', value=record.street_address if record else '')
            pregnancy = st.selectbox('Pregnant', ('NA', 'Yes', 'No'), index=('NA', 'Yes', 'No').index(record.pregnancy) if record else 0)
            optional_testing_options = ('NA', 'Yes', 'No')
            # Check if 'optional_testing' is set and is a valid option, otherwise default to 0 (which corresponds to 'NA')
            optional_testing_index = optional_testing_options.index(record.optional_testing) if record and record.optional_testing in optional_testing_options else 0
            optional_testing = st.selectbox('Optional Test', optional_testing_options, index=optional_testing_index)
            site_nurse_signature = st.text_input('Site Nurse Signature', value=record.site_nurse_signature if record else '')
            study_site_nurse_signature = st.text_input('Study Site Nurse Signature', value=record.study_site_nurse_signature if record else '')

        submitted = st.form_submit_button('Submit')
        if submitted:
            submission_data = SubmissionData(
                pk_specimen_id=pk_specimen_id, patient_initials=patient_initials, salutation=salutation,
                first_name=first_name, last_name=last_name, gender=gender,
                patient_weight=patient_weight, patient_height=patient_height,
                patient_dob=patient_dob, pediatric_dob=pediatric_dob, patient_age=patient_age,
                street_address=street_address, visit_code=visit_code,
                first_morning_void=fmv, pregnancy=pregnancy,
                hemoglobin_a1c=hemoglobin_a1c, fasting_status=fasting_status,
                optional_testing=optional_testing, visit_collection_date=visit_collection_date,
                visit_collection_time=visit_collection_time, site_nurse_signature=site_nurse_signature,
                study_site_nurse_signature=study_site_nurse_signature, record_number=record_number,
                study_code=study_code, site_id=site_id, random_id=random_id, req_number=req_number
            )
            if record:
                data_manager.update_record(record_id, submission_data)
            else:
                data_manager.insert_new_record(submission_data)
            st.success("Record saved successfully!")
                # Check if 'current_record' exists in session_state before deleting it
            if 'current_record' in st.session_state:
                    del st.session_state['current_record']  # Clear the record after processing
                # Redirect to a new record form
            st.session_state['page'] = 'new_record'  # Navigate back to a default view or refresh the current form view

def transmit_data():
    st.write("""
    This screen transmits all records directly to the testing station. 
    Feel free to transmit after specimens are shipped out for the day.
    """)
    if st.button("Transmit All Records"):
        data_manager.wipe_all_records()
        st.success("All records have been transmitted.")


def show_all_records():
    records = data_manager.get_all_records()
    if not records.empty:
        for index, row in records.iterrows():
            cols = st.columns([8, 1])
            with cols[0]:
                st.write(f"{row['pk_specimen_id']}/{row['visit_collection_date']} ||  {row['first_name']} {row['last_name']}")
            with cols[1]:
                if st.button("Edit", key=f"edit_{row['pk_specimen_id']}"):
                    st.session_state['current_record'] = row['pk_specimen_id']
                    st.session_state['page'] = 'edit_record'
                    st.experimental_rerun()
    else:
        st.write("No records found.")

def main_navigation():
    st.sidebar.image("./src/img/logo.png", use_column_width=True)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page:", ["New Record", "Show All Records", "Transmit"])

    if 'page' in st.session_state:
        if st.session_state['page'] == 'edit_record' or page == "New Record":
            st.header('Edit or New Specimen Entry')
            create_new_record_form()
        elif page == "Show All Records":
            st.header('All Records')
            show_all_records()
        elif page == "Transmit":
            st.header('Transmit Data')
            transmit_data()
            # Placeholder for transmit data functionality
    else:
        st.session_state['page'] = 'new_record'
        st.header('New Specimen Entry')
        create_new_record_form()

if __name__ == "__main__":
    main_navigation()
