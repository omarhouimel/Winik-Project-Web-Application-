# Generated by Django 2.0.1 on 2018-02-14 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180213_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='password',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_name',
        ),
    ]
