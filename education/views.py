from django.shortcuts import render


def education(request):
    context = {}
    template = 'education/education.html'
    return render(request, template, context)
