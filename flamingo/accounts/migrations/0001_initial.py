# Generated by Django 2.1 on 2018-09-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('car_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_available', models.BooleanField()),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
            ],
        ),
    ]