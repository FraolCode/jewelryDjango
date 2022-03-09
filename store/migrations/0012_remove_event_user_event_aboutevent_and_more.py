# Generated by Django 4.0.2 on 2022-02-09 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_doc_event_docs_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='aboutEvent',
            field=models.CharField(choices=[('aboutUS', 'aboutUS'), ('discount', 'discount'), ('announcement', 'announcement')], default='discount', max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='product',
            field=models.ForeignKey(help_text='If you choose discount on Event', on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
