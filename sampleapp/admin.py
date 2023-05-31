from django.contrib import admin
from .models import Signup,Schedule,Complaint,Contact

class SignupAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'address', 'number',)
    exclude=('password', 'confirmpassword')

admin.site.register(Signup)

admin.site.register(Schedule)

admin.site.register(Complaint)

admin.site.register(Contact)