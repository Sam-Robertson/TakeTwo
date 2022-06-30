from django.db import models
from datetime import datetime, timedelta


class Lead(models.Model):
    userName = models.CharField(max_length=50)
    userPhone = models.CharField(max_length=20)    
    userEmail = models.EmailField(max_length=40)
    userAddress = models.CharField(max_length=50)        


    # def __str__(self):
    #             return (self.first_name)

# IDK ABOUT THIS... SEEMS A LITTLE FISSHY

# def addLeadView(request) :
#     myLead = Lead(first_name="Mary", 
#                         last_name="Lamb", 
#                         user_name="marylamb",
#                         password="baaramewe",
#                         email="mary@test.com",
#                         phone="2035551212")                        

#     myLead.save()    


# def save(self):
#     self.first_name = self.first_name.upper()
#     super(Lead, self).save() # Calls the "real" save() method




