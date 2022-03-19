from django.db import models

# Create your models here.


class Task(models.Model):
    URGENT = "u"
    NON_URGENT = "nu"
    GENRE = (
        (URGENT, "Urgent"),
        (NON_URGENT, "Non-Urgent"),
    )
    title = models.CharField(max_length=100)
    completed = models.BooleanField(
        default=False,
        blank=True,
        null=True,
    )
    types = models.CharField(
        max_length=15,
        choices=GENRE,
        default=NON_URGENT,
    )

    def __str__(self):
        return self.title
