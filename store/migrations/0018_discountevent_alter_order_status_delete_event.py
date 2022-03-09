# Generated by Django 4.0.2 on 2022-02-10 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_event_aboutevent_alter_event_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('expired', models.BooleanField(default=False, help_text='0 = Default, 1 = Discount Event expired')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ending_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
