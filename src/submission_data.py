class SubmissionData:
    def __init__(self, pk_specimen_id = None, first_name=None, last_name=None, salutation=None,
                 patient_weight=None, weight_unit="kg", patient_height=None, height_unit='cm', patient_dob=None, patient_age=None, pediatric_dob=None,
                 street_address=None, visit_code=None, first_morning_void=None, pregnancy=None,
                 hemoglobin_a1c=None, fasting_status=None, optional_testing=None, collection_date=None,
                 collection_time=None, site_nurse_signature=None, study_collection_date=None,
                 study_collection_time=None, study_site_nurse_signature=None, record_number=None, study_code=None,
                 site_id=None, random_id=None, req_number=None, visit_collection_date = None, visit_collection_time=None, patient_initials= None,
                  gender=None):
        self.pk_specimen_id = pk_specimen_id
        self.first_name = first_name
        self.last_name = last_name
        self.salutation = salutation
        self.patient_weight = patient_weight
        self.weight_unit = weight_unit
        self.patient_height = patient_height
        self.height_unit = height_unit
        self.patient_dob = patient_dob
        self.patient_age = patient_age
        self.pediatric_dob = pediatric_dob
        self.street_address = street_address
        self.visit_code = visit_code
        self.first_morning_void = first_morning_void
        self.pregnancy = pregnancy
        self.hemoglobin_a1c = hemoglobin_a1c
        self.fasting_status = fasting_status
        self.optional_testing = optional_testing
        self.collection_date = collection_date
        self.collection_time = collection_time
        self.site_nurse_signature = site_nurse_signature
        self.study_collection_date = study_collection_date
        self.study_collection_time = study_collection_time
        self.study_site_nurse_signature = study_site_nurse_signature
        self.record_number = record_number
        self.study_code = study_code
        self.site_id = site_id
        self.random_id = random_id
        self.req_number = req_number
        self.visit_collection_date = visit_collection_date
        self.visit_collection_time = visit_collection_time
        self.patient_initials = patient_initials
        self.gender = gender