# Generated by Django 4.1.1 on 2022-09-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_alter_slider_tagline_one_alter_slider_tagline_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider_three',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tagline_one', models.TextField(blank=True, max_length=200, null=True)),
                ('tagline_two', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Slider three',
                'verbose_name_plural': 'Slider three',
            },
        ),
        migrations.CreateModel(
            name='Slider_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('tagline_one', models.TextField(blank=True, max_length=200, null=True)),
                ('tagline_two', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Slider two',
                'verbose_name_plural': 'Slider two',
            },
        ),
        migrations.RenameModel(
            old_name='Slider',
            new_name='Slider_one',
        ),
        migrations.AlterModelOptions(
            name='slider_one',
            options={'verbose_name': 'Slider one', 'verbose_name_plural': 'Slider one'},
        ),
    ]
