# Generated by Django 4.0.5 on 2022-06-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.CharField(default='default message', max_length=1000),
            preserve_default=False,
        ),
    ]