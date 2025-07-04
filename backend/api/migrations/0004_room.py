# Generated by Django 5.2.3 on 2025-06-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_patient_abnormal_pap_patient_first_sexual_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied'), ('cleaning', 'Cleaning')], default='available', max_length=20)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
