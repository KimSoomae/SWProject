# Generated by Django 2.2.7 on 2019-12-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('qxp', models.CharField(max_length=255)),
                ('total', models.CharField(max_length=255)),
                ('groupname_budget', models.CharField(max_length=255)),
                ('people', models.CharField(default=0, max_length=255)),
            ],
        ),
    ]
