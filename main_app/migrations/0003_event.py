# Generated by Django 4.0.2 on 2022-03-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_job_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('I', 'Interviews'), ('D', 'Deadlines')], default='I', max_length=1)),
                ('date', models.DateField(verbose_name='Event Date')),
                ('description', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.job')),
            ],
        ),
    ]
