from django.db import models

from .constants import TITLE_MAX_LENGTH, STATUS_MAX_LENGTH

class Task(models.Model):
    TODO = 'to do'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
    STATUS = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done')
        ]
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=STATUS_MAX_LENGTH, choices=STATUS,
                              default=TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'Задачи'
        
    def __str__(self) -> str:
        return self.title
