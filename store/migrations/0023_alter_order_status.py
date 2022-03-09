# Generated by Django 4.0.2 on 2022-02-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
