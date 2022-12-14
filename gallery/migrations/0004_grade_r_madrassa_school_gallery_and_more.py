# Generated by Django 4.0.3 on 2022-04-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_rename_greenclubgallery_green_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade_R',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery/school')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Grade_R',
                'verbose_name_plural': 'Grade_R',
            },
        ),
        migrations.CreateModel(
            name='Madrassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery/Madrassa')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Madrassa',
                'verbose_name_plural': 'Madrassa',
            },
        ),
        migrations.CreateModel(
            name='School_Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery/school')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'School_Gallery',
                'verbose_name_plural': 'School_Gallery',
            },
        ),
        migrations.AlterModelOptions(
            name='green_club',
            options={'verbose_name': 'Green Club ', 'verbose_name_plural': 'Green Club'},
        ),
    ]
