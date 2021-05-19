# Generated by Django 2.2.10 on 2021-05-17 07:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210517_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_friends_+', to='accounts.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_chat_id',
            field=models.UUIDField(default=uuid.UUID('36fe3baf-249b-4229-a800-d7fc6f7582f2'), editable=False, null=True, unique=True),
        ),
    ]