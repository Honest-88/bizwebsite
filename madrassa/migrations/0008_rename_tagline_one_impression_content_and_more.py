# Generated by Django 4.1.1 on 2022-10-11 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madrassa', '0007_rename_content_welcome_content_one_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impression',
            old_name='tagline_one',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='impression',
            old_name='image_one',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='image_two',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_five',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_four',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_three',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='tagline_two',
        ),
    ]
