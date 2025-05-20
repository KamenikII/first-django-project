from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    content = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"