from django.shortcuts import render


def contact(request):
    """
    contact view
    """
    return render(request, 'contact/index.html')
