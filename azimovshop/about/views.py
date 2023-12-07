from django.shortcuts import render

def howtomakeorder(request):
    context = {}
    template = 'about/howtomakeorder.html'
    return render(request, template, context)


def howtopay(request):
    context = {}
    template = 'about/howtopay.html'
    return render(request, template, context)


def qanda(request):
    context = {}
    template = 'about/qanda.html'
    return render(request, template, context)


def rules(request):
    context = {}
    template = 'about/rules.html'
    return render(request, template, context)


def social_links(request):
    context = {}
    template = 'about/social_links.html'
    return render(request, template, context)


def history(request):
    context = {}
    template = 'about/history.html'
    return render(request, template, context)
