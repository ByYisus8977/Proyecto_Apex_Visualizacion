from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Disciplina


@login_required
def tabla_crecimiento(request):
    return render(request, "tabla.html", {"disciplinas": Disciplina.objects.all()})
