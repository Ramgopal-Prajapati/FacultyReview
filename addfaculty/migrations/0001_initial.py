# Generated by Django 4.2.6 on 2023-11-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addfaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_Name', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Address', models.TextField(max_length=200)),
                ('Imgs', models.FileField(upload_to='static')),
            ],
        ),
    ]
