# Generated by Django 5.0.7 on 2024-11-13 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anusha', '0003_basicdetailform_expiry_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goldloanapplication',
            name='Pan_number',
            field=models.CharField(blank=True, default='', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='pan_card_number',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='otherloans',
            name='pan_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
