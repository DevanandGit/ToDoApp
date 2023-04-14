from django.db import models

class AddActivity(models.Model):
    activity = models.CharField(max_length=300)
    deadline = models.DateField()

    def __str__(self) -> str:
        return f"{self.activity} need to complete before {self.deadline}"