# Generated by Django 5.1.3 on 2024-12-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_full_lore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='lore_summary',
            field=models.TextField(default='WIP', max_length=100),
        ),
    ]
