import strawberry
from strawberry import auto

from libs.models import Question


@strawberry.django.type(Question)
class QuestionType:
    id: auto
    question_number: auto
    category: auto
    turns: list[str]