# Generated by Django 5.0.7 on 2024-11-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anusha', '0004_alter_goldloanapplication_pan_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherbasicdetailform',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
