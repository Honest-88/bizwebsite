# Generated by Django 4.0.3 on 2022-03-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_alter_slider_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_mission',
            old_name='phone_number',
            new_name='pass_rate',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='achievements',
        ),
        migrations.RemoveField(
            model_name='impression',
            name='pass_rate',
        ),
        migrations.AddField(
            model_name='our_mission',
            name='achievements',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
