# Generated by Django 2.2.7 on 2019-12-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_budget_list_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget_list',
            name='state',
            field=models.IntegerField(max_length=3),
        ),
    ]