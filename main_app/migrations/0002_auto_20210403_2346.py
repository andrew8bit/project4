# Generated by Django 3.1.7 on 2021-04-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='summary',
            field=models.CharField(default='Please help find this missing person', max_length=100),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='last_seen',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]