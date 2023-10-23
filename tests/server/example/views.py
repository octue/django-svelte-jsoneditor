import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .tasks import MyOnDemandTask


@require_http_methods(["POST"])
def enqueue_an_on_demand_task(_):
    """A simple view, demonstrating how to enqueue an on-demand task from a view

    In production, you'll want to protect this behind a layer of authentication so only users with permission can trigger tasks :)

    """
    MyOnDemandTask().enqueue(a=1)

    # Usually, you'll want to return a 201 "Accepted for Processing" code... but the response is entirely up to you :)
    now = datetime.datetime.now()
    return JsonResponse({"enqueued_at": now.isoformat()}, status=201)
