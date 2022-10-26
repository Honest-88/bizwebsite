# Generated by Django 4.1.1 on 2022-09-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0011_rename_title_one_slider_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='tagline_five',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='image',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_four',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_one',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_three',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_two',
        ),
        migrations.AddField(
            model_name='impression',
            name='application_form',
            field=models.FileField(blank=True, upload_to='Application'),
        ),
    ]
