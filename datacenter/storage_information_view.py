from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_users = Visit.objects.filter(leaved_at__isnull=True)
    now = timezone.now()

    non_closed_visits = [{"who_entered": user.passcard.owner_name, "date": user.entered_at, "duration": now - user.entered_at} for user in non_closed_users]

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
