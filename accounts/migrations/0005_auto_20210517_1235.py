# Generated by Django 2.2.10 on 2021-05-17 07:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210517_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_chat_id',
            field=models.UUIDField(default=uuid.UUID('95304e8d-d21b-4fdb-8d20-e1a96fa5ecaa'), editable=False, null=True, unique=True),
        ),
    ]
