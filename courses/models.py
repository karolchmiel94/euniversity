from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from utils.model_utilities import TimeStampMixin

from .fields import OrderField


class Subject(TimeStampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Module(TimeStampMixin):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Content(TimeStampMixin):
    module = models.ForeignKey(
        Module, related_name='contents', on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('text', 'video', 'image', 'file')},
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(TimeStampMixin):
    owner = models.ForeignKey(
        User, related_name='%(class)s_related', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
