# Generated by Django 2.2.7 on 2019-12-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191209_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='flex_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='qb_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='rb_one_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='rb_two_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='te_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='wr_one_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='wr_three_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='roster',
            name='wr_two_id',
            field=models.IntegerField(default=0),
        ),
    ]
