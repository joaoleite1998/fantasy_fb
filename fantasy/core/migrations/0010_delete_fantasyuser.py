# Generated by Django 2.2.7 on 2019-12-09 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('core', '0009_auto_20191209_0020'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FantasyUser',
        ),
    ]