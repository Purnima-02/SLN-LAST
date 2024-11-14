# Generated by Django 5.0.7 on 2024-11-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seetha', '0002_alter_carloan_ref_1_person_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clbasicdetail',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clbasicdetail',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=10, null=True),
        ),
    ]
