from django.shortcuts import render


def contact(request):
    """
    contact view
    indi duzelmis olmalidi
    """
    return render(request, 'contact/index.html')
