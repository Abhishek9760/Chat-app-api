import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save


User = settings.AUTH_USER_MODEL


class Message(models.Model):
    author = models.ForeignKey(
        User,
        blank=False,
        null=False,
        related_name='author_messages',
        on_delete=models.CASCADE
    )
    content = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"By {self.author} - {self.content}"

    def last_50_messages():
        return Message.objects.order_by('-timestamp').all()[:50]


class Chat(models.Model):
    chat_id = models.TextField(
        null=True,
        blank=True,
        unique=True,
    )

    sender = models.ForeignKey(
        User, related_name='sender_user', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(
        User, related_name='receiver_user', on_delete=models.DO_NOTHING)
    message = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return f"Chat Room - {self.sender.username} & {self.receiver.username}"


def chat_pre_save_receiver(sender, instance, *args, **kwargs):
    sender_id, receiver_id = str(instance.sender.user_chat_id), str(
        instance.receiver.user_chat_id)
    if sender_id > receiver_id:
        instance.chat_id = sender_id + receiver_id
    else:
        instance.chat_id = receiver_id + sender_id


pre_save.connect(chat_pre_save_receiver, sender=Chat)
