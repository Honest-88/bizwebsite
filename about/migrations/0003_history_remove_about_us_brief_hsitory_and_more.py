# Generated by Django 4.1.1 on 2022-10-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_about_us_brief_hsitory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content_one', models.TextField(blank=True, max_length=5000, null=True)),
                ('title_one', models.TextField(blank=True, max_length=5000, null=True)),
                ('content_two', models.TextField(blank=True, max_length=5000, null=True)),
                ('title_two', models.TextField(blank=True, max_length=5000, null=True)),
                ('content_three', models.TextField(blank=True, max_length=5000, null=True)),
                ('title_three', models.TextField(blank=True, max_length=5000, null=True)),
                ('content_four', models.TextField(blank=True, max_length=5000, null=True)),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Brief History',
                'verbose_name_plural': 'Brief History',
            },
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='brief_hsitory',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='image_two',
        ),
    ]
