# Generated by Django 4.0.2 on 2022-03-31 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='companies',
            field=models.ManyToManyField(to='main_app.Company'),
        ),
    ]
