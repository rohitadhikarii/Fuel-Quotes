# Generated by Django 5.0.3 on 2024-04-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
