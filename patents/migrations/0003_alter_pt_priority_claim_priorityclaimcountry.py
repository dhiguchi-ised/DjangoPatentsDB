# Generated by Django 4.1.7 on 2023-03-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0002_alter_pt_priority_claim_priorityclaimcalendardate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_priority_claim',
            name='priorityclaimcountry',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
