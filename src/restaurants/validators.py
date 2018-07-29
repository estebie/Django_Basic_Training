from django.core.exceptions import ValidationError

CATEGORIES = ['Asian', 'American', 'Japanese', 'Italian', 'Whatever']

def validate_category(value):
    cat = value.capitalize()
    if value not in CATEGORIES and cat in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")