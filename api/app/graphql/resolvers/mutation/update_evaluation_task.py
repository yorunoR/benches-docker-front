from asgiref.sync import sync_to_async
from django.db.models import Avg
from strawberry import ID
from strawberry.types import Info

from libs.models import EvaluationTask, Rate
from libs.models.evaluation_task import Status as EvaluationTaskStatus


def convert_list_to_dict(input_list):
    result_dict = {item["answer__question__category"]: float(item["result"]) for item in input_list}
    return result_dict


def avg_points(evaluation_task):
    category_points_avg = (
        Rate.objects.filter(evaluation_task=evaluation_task)
        .exclude(point=0)
        .values("answer__question__category")
        .annotate(result=Avg("point"))
    )

    return convert_list_to_dict(category_points_avg)


def avg_processing_times(evaluation_task):
    category_processing_times_avg = (
        Rate.objects.filter(evaluation_task=evaluation_task)
        .exclude(point=0)
        .values("answer__question__category")
        .annotate(result=Avg("answer__processing_time"))
    )

    return convert_list_to_dict(category_processing_times_avg)


async def resolve(info: Info, id: ID):
    user = info.context.user
    evaluation_task = await EvaluationTask.objects.aget(id=id, user=user, status=EvaluationTaskStatus.COMPLETED)

    points = await sync_to_async(avg_points)(evaluation_task)
    processing_times = await sync_to_async(avg_processing_times)(evaluation_task)

    evaluation_task.points = points
    evaluation_task.processing_times = processing_times
    await sync_to_async(lambda: evaluation_task.save())()

    return evaluation_task
