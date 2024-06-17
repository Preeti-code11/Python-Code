class Applicant:
    application_dict={'A:0','B:0','C:0'}
    applicant_id_count = 1000
    def __init__(self, applicant_name):
        self.__applicant_name = applicant_name

    def generate_applicant_id(self):
        applicant_id = applicant_id_count + 1

    def apply_for_job(self, job_band):
        if application_dict.value>5