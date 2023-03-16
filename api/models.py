from django.db import models

# Create your models here.
class TODO(models.Model):
    task=models.DateField(max_length=50)
    description=models.TextField(max_length=200)
    completed=models.BooleanField(50)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    def __str__(self) -> str:
        return {self.task}

