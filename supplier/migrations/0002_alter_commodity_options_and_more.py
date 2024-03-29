# Generated by Django 4.2.7 on 2024-03-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodity',
            options={'verbose_name_plural': 'Commodities'},
        ),
        migrations.RenameField(
            model_name='supplyrequest',
            old_name='commodity',
            new_name='commodities',
        ),
        migrations.AlterField(
            model_name='commodity',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price per each commodity', max_digits=10),
        ),
        migrations.AlterField(
            model_name='supplyrequest',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
