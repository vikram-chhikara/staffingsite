# Generated by Django 2.0.2 on 2018-03-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0013_applicant_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='resume_files/%Y/%m/%d/'),
        ),
    ]