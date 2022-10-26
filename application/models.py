from django.db import models
from datetime import datetime



class Application_Form(models.Model):
    child_full_name = models.CharField(max_length=1000, blank=True, null=True)
    emergency_numbers = models.CharField(max_length=1000, blank=True, null=True)
    cell_numbers = models.CharField(max_length=1000, blank=True, null=True)
    email_address = models.CharField(max_length=1000, blank=True, null=True)
    grade_applied_for = models.CharField(max_length=1000, blank=True, null=True)
    highest_grade_passed = models.CharField(max_length=1000,blank=True, null=True)
    year_grade_passed = models.CharField(max_length=1000,blank=True, null=True)
    accession_no = models.CharField(max_length=1000,blank=True, null=True)
    first_name = models.CharField(max_length=1000,blank=True, null=True)
    last_name = models.CharField(max_length=1000,blank=True, null=True)
    other_names = models.CharField(max_length=1000,blank=True, null=True)
    date_of_birth = models.CharField(max_length=1000,blank=True, null=True)
    gender = models.CharField(max_length=1000,blank=True, null=True)
    race = models.CharField(max_length=1000,blank=True, null=True)
    citizenship = models.CharField(max_length=1000,blank=True, null=True)
    province_of_residence = models.CharField(max_length=1000,blank=True, null=True)
    physical_address = models.TextField(max_length=1000,blank=True, null=True)
    city_or_suburb = models.CharField(max_length=1000,blank=True, null=True)
    postal_code = models.CharField(max_length=1000,blank=True, null=True)
    home_langauge = models.CharField(max_length=1000,blank=True, null=True)
    preferred_lang_of_instruction = models.CharField(max_length=1000,blank=True, null=True)
    any_deceased_parent = models.CharField(max_length=1000,blank=True, null=True)
    mode_of_transport = models.CharField(max_length=1000,blank=True, null=True)
    religion = models.CharField(max_length=1000,blank=True, null=True)
    pre_primary_education = models.CharField(max_length=1000,blank=True, null=True)
    name_of_previous_school = models.CharField(max_length=1000,blank=True, null=True)
    previous_school_address = models.TextField(max_length=1000,blank=True, null=True)
    country_province_and_code = models.CharField(max_length=1000,blank=True, null=True)
    medical_aid_number = models.CharField(max_length=1000,blank=True, null=True)
    medical_aid_name = models.CharField(max_length=1000,blank=True, null=True)
    medical_aid_main_member = models.CharField(max_length=1000,blank=True, null=True)
    doctor_name = models.CharField(max_length=1000,blank=True, null=True)
    doctor_address = models.TextField(max_length=1000,blank=True, null=True)
    doctor_phone_number = models.CharField(max_length=1000,blank=True, null=True)
    medical_condition = models.CharField(max_length=1000,blank=True, null=True)
    dexterity_of_learner = models.CharField(max_length=1000,blank=True, null=True)
    registered_for_social_grant = models.CharField(max_length=1000,blank=True, null=True)
    copy_of_immunisation_records = models.FileField(max_length=1000,upload_to="application/forms", blank=True, null=True)
    progress_report_previous_school = models.FileField(max_length=1000,upload_to="application/forms", blank=True, null=True)
    copy_of_birth_certificate = models.FileField(max_length=1000,upload_to="application/forms", blank=True, null=True)
    transfer_letter_previous_school = models.FileField(max_length=1000,upload_to="application/forms", blank=True, null=True)
    number_of_other_children_at_mayfair = models.CharField(max_length=1000,blank=True, null=True)
    enter_their_names = models.TextField(max_length=1000,blank=True, null=True)
    parent_first_name = models.CharField(max_length=1000,blank=True, null=True)
    parent_second_name = models.CharField(max_length=1000,blank=True, null=True)
    parent_gender = models.CharField(max_length=1000,blank=True, null=True)
    parent_race = models.CharField(max_length=1000,blank=True, null=True)
    home_language = models.CharField(max_length=1000,blank=True, null=True)
    identification_number = models.CharField(max_length=1000,blank=True, null=True)
    passport_number = models.CharField(max_length=1000,blank=True, null=True)
    occupation = models.CharField(max_length=1000,blank=True, null=True)
    employer = models.CharField(max_length=1000,blank=True, null=True)
    surname_of_spouse = models.CharField(max_length=1000,blank=True, null=True)
    spouse_first_name = models.CharField(max_length=1000,blank=True, null=True)
    spouse_id_number = models.CharField(max_length=1000,blank=True, null=True)
    marital_status_of_parent = models.CharField(max_length=1000,blank=True, null=True)
    relationship_to_learner = models.CharField(max_length=1000,blank=True, null=True)
    date_applied = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Application Form'
            verbose_name_plural = 'Application Form'


    def __str__(self):
        return self.child_full_name

