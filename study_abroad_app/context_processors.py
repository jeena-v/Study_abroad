# study_abroad_app/context_processors.py

def country_list(request):
    """
    Return a dict with all CountryPage objects for the navbar dropdown.
    Import models inside the function to avoid app-loading issues.
    """
    from .models import CountryPage
    return {
        'countries': CountryPage.objects.all()
    }

# context_processors.py
from .models import Service

def services_by_category(request):
    services = Service.objects.all()
    categories = {
        'Counselling': services.filter(category='counselling'),
        'Test Prep': services.filter(category='testprep'),
        'Other Services': services.filter(category='other'),
    }
    return {'services_by_category': categories}
