from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from datetime import datetime
from application.models import Application_Form
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


def apply(request):
    if request.method == "POST":

        child_full_name = request.POST['child_full_name']
        emergency_numbers = request.POST['emergency_numbers']
        cell_numbers = request.POST['cell_numbers']
        email_address = request.POST['email_address']
        grade_applied_for = request.POST['grade_applied_for']
        highest_grade_passed = request.POST['highest_grade_passed']
        year_grade_passed = request.POST['year_grade_passed']
        accession_no = request.POST['accession_no']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        other_names = request.POST['other_names']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        race = request.POST['race']
        citizenship = request.POST['citizenship']
        province_of_residence = request.POST['province_of_residence']
        physical_address = request.POST['physical_address']
        city_or_suburb = request.POST['city_or_suburb']
        postal_code = request.POST['postal_code']
        home_langauge = request.POST['home_langauge']
        preferred_lang_of_instruction = request.POST['preferred_lang_of_instruction']
        any_deceased_parent = request.POST['any_deceased_parent']
        mode_of_transport = request.POST['mode_of_transport']
        religion = request.POST['religion']
        pre_primary_education = request.POST['pre_primary_education']
        name_of_previous_school = request.POST['name_of_previous_school']
        previous_school_address = request.POST['previous_school_address']
        country_province_and_code = request.POST['country_province_and_code']
        medical_aid_number = request.POST['medical_aid_number']
        medical_aid_name = request.POST['medical_aid_name']
        medical_aid_main_member = request.POST['medical_aid_main_member']
        doctor_name = request.POST['doctor_name']
        doctor_address = request.POST['doctor_address']
        doctor_phone_number = request.POST['doctor_phone_number']
        medical_condition = request.POST['medical_condition']
        dexterity_of_learner = request.POST['dexterity_of_learner']
        registered_for_social_grant = request.POST['registered_for_social_grant']
        copy_of_immunisation_records = request.FILES['copy_of_immunisation_records']
        progress_report_previous_school = request.FILES['progress_report_previous_school']
        copy_of_birth_certificate = request.FILES['copy_of_birth_certificate']
        transfer_letter_previous_school = request.FILES['transfer_letter_previous_school']
        number_of_other_children_at_mayfair = request.POST['number_of_other_children_at_mayfair']
        enter_their_names = request.POST['enter_their_names']
        parent_first_name = request.POST['parent_first_name']
        parent_second_name = request.POST['parent_second_name']
        parent_gender = request.POST['parent_gender']
        parent_race = request.POST['parent_race']
        home_language = request.POST['home_language']
        identification_number = request.POST['identification_number']
        passport_number = request.POST['passport_number']
        occupation = request.POST['occupation']
        employer = request.POST['employer']
        surname_of_spouse = request.POST['surname_of_spouse']
        spouse_first_name = request.POST['spouse_first_name']
        spouse_id_number = request.POST['spouse_id_number']
        marital_status_of_parent = request.POST['marital_status_of_parent']
        relationship_to_learner = request.POST['relationship_to_learner']



        apply = Application_Form.objects.create(child_full_name=child_full_name,emergency_numbers=emergency_numbers,cell_numbers=cell_numbers,email_address=email_address,grade_applied_for = grade_applied_for,highest_grade_passed = highest_grade_passed,
        year_grade_passed = year_grade_passed,accession_no = accession_no,first_name = first_name,last_name = last_name,other_names = other_names,date_of_birth = date_of_birth,gender = gender,race = race,citizenship = citizenship,
        province_of_residence = province_of_residence,physical_address = physical_address,city_or_suburb = city_or_suburb,postal_code = postal_code,home_langauge = home_langauge,preferred_lang_of_instruction = preferred_lang_of_instruction,any_deceased_parent = any_deceased_parent,
        mode_of_transport = mode_of_transport,religion = religion,pre_primary_education = pre_primary_education,name_of_previous_school = name_of_previous_school,previous_school_address = previous_school_address,country_province_and_code = country_province_and_code,
        medical_aid_number = medical_aid_number,medical_aid_name = medical_aid_name,medical_aid_main_member = medical_aid_main_member,doctor_name = doctor_name,doctor_address = doctor_address,doctor_phone_number = doctor_phone_number,
        medical_condition = medical_condition,dexterity_of_learner = dexterity_of_learner,registered_for_social_grant = registered_for_social_grant,copy_of_immunisation_records = copy_of_immunisation_records,progress_report_previous_school = progress_report_previous_school,
        copy_of_birth_certificate = copy_of_birth_certificate,transfer_letter_previous_school = transfer_letter_previous_school,number_of_other_children_at_mayfair = number_of_other_children_at_mayfair,enter_their_names = enter_their_names,
        parent_first_name = parent_first_name,parent_second_name = parent_second_name, parent_gender = parent_gender,parent_race = parent_race,home_language = home_language,identification_number = identification_number,passport_number = passport_number,
        occupation = occupation,employer = employer,surname_of_spouse = surname_of_spouse,spouse_first_name = spouse_first_name,spouse_id_number = spouse_id_number,marital_status_of_parent = marital_status_of_parent,relationship_to_learner = relationship_to_learner)

     
        send_mail(

            'New Student Application Form Submitted',
            'FROM SITE: (www.mayfairacademy.co.za) A new student has submitted an application form through your Website (www.mayfairacademy.co.za/admin) click, login here.',
            'applymayfair@gmail.com',
            ['info@mayfairacademy.co.za', 'mayfairacademy114@gmail.com'],
            fail_silently=False,
        )
        apply.save()
        messages.success(request, 'Form Submitted, Thanks for Applying we will get back to you soon')
    return render(request, "app/apply.html")


        










