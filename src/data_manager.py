from submission_data import SubmissionData
import pandas as pd

class DataManager:
    def __init__(self, connection):
        self.conn = connection

    def fetch_record_by_id(self, pk_specimen_id):
        query = "SELECT * FROM specimen_records WHERE pk_specimen_id = ? order by visit_collection_date desc"
        params = (pk_specimen_id,)
        record = pd.read_sql(query, self.conn, params=params)
        if not record.empty:
            record_dict = record.iloc[0].to_dict()
            # Remove the primary key field if it's not needed in SubmissionData
            # record_dict.pop('pk_specimen_id', None)
            return SubmissionData(**record_dict)
        else:
            return None

    def insert_new_record(self, data: SubmissionData):
        cursor = self.conn.cursor()
        sql = '''
        INSERT INTO specimen_records (
            patient_initials, first_name, last_name, salutation, patient_weight, patient_height, 
            patient_dob, patient_age, pediatric_dob, street_address, visit_code, first_morning_void, pregnancy,
            hemoglobin_a1c, fasting_status, optional_testing, visit_collection_date, visit_collection_time,
            site_nurse_signature, study_site_nurse_signature,
            record_number, study_code, site_id, random_id, req_number, gender
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(sql, (
            data.patient_initials, data.first_name, data.last_name, data.salutation, data.patient_weight, 
            data.patient_height, data.patient_dob.strftime('%Y-%m-%d') if data.patient_dob else None,
            data.patient_age, 
            data.pediatric_dob.strftime('%Y-%m-%d') if data.pediatric_dob else None,
            data.street_address, data.visit_code, data.first_morning_void, data.pregnancy, data.hemoglobin_a1c,
            data.fasting_status, data.optional_testing, 
            data.visit_collection_date.strftime('%Y-%m-%d') if data.visit_collection_date else None, 
            data.visit_collection_time.strftime('%H:%M') if data.visit_collection_time else None,
            data.site_nurse_signature, data.study_site_nurse_signature, data.record_number, data.study_code, 
            data.site_id, data.random_id, data.req_number, data.gender
        ))
        self.conn.commit()
        return cursor.lastrowid

    def update_record(self, pk_specimen_id, data: SubmissionData):
        cursor = self.conn.cursor()
        sql = '''
        UPDATE specimen_records SET
            patient_initials=?, first_name=?, last_name=?, salutation=?, patient_weight=?, patient_height=?,
            patient_dob=?, patient_age=?, pediatric_dob=?, street_address=?, visit_code=?,
            first_morning_void=?, pregnancy=?, hemoglobin_a1c=?, fasting_status=?, optional_testing=?,
            visit_collection_date=?, visit_collection_time=?, site_nurse_signature=?,
            study_site_nurse_signature=?, record_number=?, study_code=?, site_id=?, random_id=?, req_number=?, gender=?
        WHERE pk_specimen_id=?
        '''
        params = (
            data.patient_initials, data.first_name, data.last_name, data.salutation, data.patient_weight,
            data.patient_height,  data.patient_dob.strftime('%Y-%m-%d') if data.patient_dob else None, data.patient_age,
            data.pediatric_dob.strftime('%Y-%m-%d') if data.pediatric_dob else None,
            data.street_address, data.visit_code, data.first_morning_void, data.pregnancy, data.hemoglobin_a1c,
            data.fasting_status, data.optional_testing, data.visit_collection_date.strftime('%Y-%m-%d') if data.visit_collection_date else None,
            data.visit_collection_time.strftime('%H:%M') if data.visit_collection_time else None,
            data.site_nurse_signature, data.study_site_nurse_signature, data.record_number, data.study_code, data.site_id,
            data.random_id, data.req_number, data.gender, pk_specimen_id
        )

        # Print the query with parameters
        print("Executing SQL Query:")
        print(sql)
        print("With parameters:")
        print(params)

        # Execute the query with parameters
        cursor.execute(sql, params)
        self.conn.commit()

    def wipe_all_records(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM specimen_records")
        self.conn.commit()


    def get_all_records(self):
        query = "SELECT * FROM specimen_records ORDER BY pk_specimen_id DESC"
        try:
            return pd.read_sql(query, self.conn)
        except Exception as e:
            print(f"Failed to fetch all records: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on failure
