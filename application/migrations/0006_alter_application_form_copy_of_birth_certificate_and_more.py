# Generated by Django 4.0.3 on 2022-04-26 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_remove_application_form_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_form',
            name='copy_of_birth_certificate',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='application/forms'),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='copy_of_immunisation_records',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='application/forms'),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='progress_report_previous_school',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='application/forms'),
        ),
        migrations.AlterField(
            model_name='application_form',
            name='transfer_letter_previous_school',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to='application/forms'),
        ),
    ]
