# Generated by Django 2.1 on 2018-09-19 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20180919_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='available',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Available', verbose_name='Is Available'),
        ),
    ]