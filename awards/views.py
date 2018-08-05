from django.shortcuts import render


def awards(request):
    context = {}
    template = 'awards/awards.html'
    return render(request, template, context)

