from utils.model_utilities import generate_unique_slug


def ensure_unique_slug(sender, instance, slug, **kwargs):
    print('pre_save')
    Klass = instance.__class__
    Klass.slug = generate_unique_slug(Klass, slug)
