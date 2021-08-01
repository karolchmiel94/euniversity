import string
import random

from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def generate_random_string(size=8, chars=string.ascii_lowercase + string.digits) -> str:
    return "".join(random.choice(chars) for _ in range(size))


def generate_unique_slug(instance, title) -> str:
    slug = slugify(instance.title)
    Klass = instance.__class__

    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{random_string}".format(
            slug=slug, random_string=generate_random_string()
        )
        return new_slug
    else:
        return slug
