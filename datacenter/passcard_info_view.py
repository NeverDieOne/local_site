from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def is_visit_long(visit, minutes=60):
    time_in_storage = get_duration(visit)
    return time_in_storage.seconds > minutes * 60


def get_duration(visit):
    if not visit.leaved_at:
        now = timezone.now()
        return now - visit.entered_at
    return visit.leaved_at - visit.entered_at


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = [{"date": visit.entered_at, "duration": get_duration(visit), "is_strange": is_visit_long(visit)} for visit in visits]

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
