from django.shortcuts import render


def interests(request):
    context = {}
    template = 'interests/interests.html'
    return render(request, template, context)
