# Generated by Django 2.2.10 on 2021-05-17 06:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210517_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_chat_id',
            field=models.UUIDField(default=uuid.UUID('cdb61195-808b-4f3b-a664-05c359666718'), editable=False, null=True, unique=True),
        ),
    ]
