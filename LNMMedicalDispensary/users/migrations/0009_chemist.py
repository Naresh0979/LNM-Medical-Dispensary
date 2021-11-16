# Generated by Django 3.2.7 on 2021-11-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20211116_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('Cid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
            ],
        ),
    ]
