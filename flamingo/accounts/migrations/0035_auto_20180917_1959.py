# Generated by Django 2.1 on 2018-09-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_remove_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='book_start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
    ]