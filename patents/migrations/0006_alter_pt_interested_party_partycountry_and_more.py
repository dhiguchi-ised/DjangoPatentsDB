# Generated by Django 4.1.7 on 2023-03-24 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patents', '0005_alter_pt_interested_party_partycountry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pt_interested_party',
            name='partycountry',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='pt_interested_party',
            name='partyname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]