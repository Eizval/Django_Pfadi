from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProfileForm
from .models import Profile, Level


def profiles_list(request):
    # Filters
    name_q = request.GET.get("name", "").strip()
    phone_q = request.GET.get("phone", "").strip()
    lvl_q = request.GET.get("lvl")  # Level id (represents level+second_level)

    qs = Profile.objects.select_related("level").all()

    # Visibility rules
    if not request.user.is_authenticated:
        qs = qs.filter(visible=True)

    if name_q:
        qs = qs.filter(
            Q(name__icontains=name_q)
            | Q(second_name__icontains=name_q)
            | Q(last_name__icontains=name_q)
        )

    if phone_q:
        qs = qs.filter(phone_number__icontains=phone_q)

    if lvl_q:
        try:
            qs = qs.filter(level_id=int(lvl_q))
        except (TypeError, ValueError):
            pass

    levels = Level.objects.all().order_by("level", "second_level")

    selected_level_id = None
    try:
        selected_level_id = int(lvl_q) if lvl_q else None
    except (TypeError, ValueError):
        selected_level_id = None

    context = {
        "profiles": qs.order_by("last_name", "name"),
        "levels": levels,
        "filters": {
            "name": name_q,
            "phone": phone_q,
            "lvl": lvl_q or "",
        },
        "selected_level_id": selected_level_id,
    }
    return render(request, "profiles/list.html", context)


@login_required
def profile_add(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profiles")
    else:
        form = ProfileForm()
    return render(request, "profiles/form.html", {"form": form, "mode": "Add"})


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profiles/form.html", {"form": form, "mode": "Edit"})


@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        profile.delete()
        return redirect("profiles")
    return render(request, "profiles/confirm_delete.html", {"profile": profile})
