# Generated by Django 4.1.7 on 2023-03-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_priority_claim',
            name='priorityclaimcalendardate',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='pt_priority_claim',
            name='priorityclaimcountry',
            field=models.CharField(max_length=65, null=True),
        ),
    ]
