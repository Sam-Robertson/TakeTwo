

from django.shortcuts import render
from django.http import HttpResponse
from LeadWebsite.models import Lead

def indexPageView(request) :
    return render(request, 'websitePages/index.html')       



def addLeadView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new lead object from the model (like a new record)
        new_lead = Lead()
        
        #Store the data from the form to the new object's attributes (like columns)
        new_lead.userName = request.POST.get('userName')
        new_lead.userPhone = request.POST.get('userPhone')
        new_lead.userEmail = request.POST.get('userEmail')
        new_lead.userAddress = request.POST.get('userAddress')

    
        new_lead.save()
    # add alert here 
    return render(request, 'websitePages/index.html', context)