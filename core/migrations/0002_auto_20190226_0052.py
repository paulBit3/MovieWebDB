# Generated by Django 2.1.7 on 2019-02-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('-year', 'title')},
        ),
    ]
