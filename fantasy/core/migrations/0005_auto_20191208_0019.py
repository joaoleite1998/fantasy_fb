# Generated by Django 2.2.7 on 2019-12-08 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191208_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['pos_key']},
        ),
        migrations.RenameField(
            model_name='position',
            old_name='position_key',
            new_name='pos_key',
        ),
    ]
