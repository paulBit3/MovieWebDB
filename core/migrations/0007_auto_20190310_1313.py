# Generated by Django 2.1.7 on 2019-03-10 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190310_1309'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
