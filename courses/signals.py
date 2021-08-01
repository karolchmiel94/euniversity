from django.db.models.signals import pre_save

from utils.generic_signals import ensure_unique_slug

from .models import Subject, Course

pre_save.connect(ensure_unique_slug, sender=Course)

pre_save.connect(ensure_unique_slug, sender=Subject)
