# Generated by Django 2.1.5 on 2019-04-16 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RFID', '0021_auto_20190415_2110'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='records',
            unique_together={('user_id', 'object_id', 'date', 'time')},
        ),
    ]
