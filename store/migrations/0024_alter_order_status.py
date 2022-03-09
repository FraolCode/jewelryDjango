# Generated by Django 4.0.2 on 2022-02-10 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Out for Shipping', 'Out for Shipping')], default='Pending', max_length=150),
        ),
    ]
