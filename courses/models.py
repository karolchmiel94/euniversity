from re import L
from django.db import models
from django.contrib.auth.models import User

from utils.model_utilities import TimeStampMixin


class Subject(TimeStampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title


class Course(TimeStampMixin):
    owner = models.ForeignKey(
        User, related_name='courses_created', on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, related_name='courses', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    overview = models.TextField()
