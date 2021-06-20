from django.core.exceptions import ValidationError
from django.utils import timezone


def year_validator(value):
    if value > timezone.now().year:
        params = {'value': value, }
        raise ValidationError('Год не может быть больше текущего',
                              params=params)


def score_validator(value):
    if not 1 <= value <= 10:
        params = {'value': value, }
        raise ValidationError('Оценка может быть от 1 до 10', params=params)
