# Generated by Django 2.2.4 on 2022-06-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoNinja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='old dojo', max_length=60),
        ),
    ]
