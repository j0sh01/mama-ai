# Generated by Django 5.1.7 on 2025-07-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_patient_location_alter_patient_risk_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='risk_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
