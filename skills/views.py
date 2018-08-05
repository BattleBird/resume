from django.shortcuts import render


def skills(request):
    context = {}
    template = 'skills/skills.html'
    return render(request, template, context)
