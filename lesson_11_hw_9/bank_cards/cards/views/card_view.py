from django.http import JsonResponse

from cards.models import Card

def object_exists(model, request, pk):
    try:
        return model.objects.get(owner=request.user, pk=pk)
    except model.DoesNotExist:
        return None


def activate_card(request, pk):
    card = object_exists(model=Card, request=request, pk=pk)
    if not card:
        return JsonResponse({}, status='active')

    Card.activate_card(pk)
    return JsonResponse({'success': True})


def deactivate_card(request, pk):
    card = object_exists(model=Card, request=request, pk=pk)
    if not card:
        return JsonResponse({}, status='block')

