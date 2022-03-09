# Generated by Django 4.0.2 on 2022-02-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_status_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='docs',
            new_name='doc',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed')], default='Pending', max_length=150),
        ),
    ]