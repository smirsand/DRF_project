import re

from rest_framework.exceptions import ValidationError


class VideoLinkLessonValidator:
    """
    Проверяет, содержит ли контент допустимые ссылки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r"(?i)^https?://(?:www\.)?youtube\.com(?:\S+)?$")
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None and not bool(reg.match(tmp_val)):
            raise ValidationError('Недопустимая ссылка')
        return tmp_val
