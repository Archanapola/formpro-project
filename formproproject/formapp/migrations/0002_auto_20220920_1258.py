# Generated by Django 3.1 on 2022-09-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
                ('sage', models.IntegerField()),
                ('smobile', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='StudentForm',
        ),
    ]
