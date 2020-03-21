import datetime as dt
from django.shortcuts import render

def year(request):
    """
    Добавляет переменную с текущим годом.
    """
    current_year = dt.datetime.today().year
    #current_year = {'year': year}
    return {'year': current_year}
    # render(request, "footer.html", current_year)
    #HttpResponse(current_year)