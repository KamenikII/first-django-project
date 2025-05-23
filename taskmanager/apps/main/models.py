from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    content = models.TextField('Description')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
