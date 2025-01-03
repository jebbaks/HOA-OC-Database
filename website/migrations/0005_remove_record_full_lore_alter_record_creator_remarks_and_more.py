# Generated by Django 5.1.3 on 2025-01-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_record_creator_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='full_lore',
        ),
        migrations.AlterField(
            model_name='record',
            name='creator_remarks',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='lore_summary',
            field=models.CharField(max_length=100),
        ),
    ]