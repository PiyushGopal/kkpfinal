# Generated by Django 4.2.2 on 2023-06-24 15:28

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_profiles',
            name='hospital_address',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='hospital_profiles',
            name='hospital_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hospital_profiles',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]