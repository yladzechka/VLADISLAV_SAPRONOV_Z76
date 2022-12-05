# Generated by Django 4.1.3 on 2022-11-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_id', models.IntegerField()),
                ('part', models.CharField(max_length=100)),
                ('cat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_numb', models.IntegerField()),
                ('cat_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
