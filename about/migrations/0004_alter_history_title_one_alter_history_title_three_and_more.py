# Generated by Django 4.1.1 on 2022-10-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_history_remove_about_us_brief_hsitory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='title_one',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='title_three',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='title_two',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
