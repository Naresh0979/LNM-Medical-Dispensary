# Generated by Django 3.2.7 on 2021-12-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20211218_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Doctorid',
            new_name='Did',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='Patientid',
            new_name='Pid',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mailid',
            field=models.CharField(max_length=20),
        ),
    ]