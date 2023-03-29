from django.shortcuts import render


def error_404_view(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)


def error_500_view(request, *args, **argv):
    """ 500 error page """
    return render(request, '500.html', status=500)
