from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('timer/', timer),
    path('contact/', contact),
    path('calculator/', calculator),
    path('calendar/', calendar),
    path('webhook/', webhook),
    path('countdown/', countdown),
    path('color-generator/', colorGenerator),
    path('screen-size/', screenSize),
    path('show-picture/', showPicture)
]