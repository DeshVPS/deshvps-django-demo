from django.db import connection
from django.shortcuts import redirect, render

from .models import Note


def index(request):
    if request.method == "POST" and request.POST.get("text", "").strip():
        Note.objects.create(text=request.POST["text"].strip()[:200])
        return redirect("index")
    return render(request, "notes/index.html", {"notes": Note.objects.order_by("-created")[:20], "engine": connection.vendor})
