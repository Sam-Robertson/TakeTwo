from django.urls import path
from .views import addLeadView, indexPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("", addLeadView, name="addLead")  
]                  
 