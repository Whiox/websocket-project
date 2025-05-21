from django.db import models
from authentication.models import User


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название чата", max_length=100)
    participants = models.ManyToManyField(
        User,
        through='ChatMembership',
        related_name='chats'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

    def __str__(self):
        return self.name

    def __int__(self):
        return self.participants.count()

    @property
    def last_message(self):
        """Возвращает последнее сообщение в чате или None."""
        return self.messages.order_by('-created_at').first()

    def get_messages(self, limit: int = 50):
        """Возвращает последние `limit` сообщений, от самого старого к новому."""
        return self.messages.order_by('-created_at')[:limit][::-1]


class ChatMembership(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField("Модератор", default=False)

    class Meta:
        unique_together = ('user', 'chat')
        verbose_name = "Участник чата"
        verbose_name_plural = "Участники чата"

    def __str__(self):
        return f"{self.user.username} в {self.chat.name}"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    text = models.TextField("Текст сообщения")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField("Прочитано", default=False)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        preview = (self.text[:50] + '…') if len(self.text) > 50 else self.text
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.sender.username}: {preview}"
