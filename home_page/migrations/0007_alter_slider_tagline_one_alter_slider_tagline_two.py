# Generated by Django 4.0.3 on 2022-05-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_testimonials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='tagline_one',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='tagline_two',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]