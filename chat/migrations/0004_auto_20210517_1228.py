# Generated by Django 2.2.10 on 2021-05-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210517_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_id',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
    ]