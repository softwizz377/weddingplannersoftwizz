from django.contrib import admin
from planner.models import ContactUs,Booking,Feedback, Gallery, Vendorcategory, Vendordetail

# Register your models here.




	
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
	list_display=('name','email','phone','message',)
	
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display=('name','email','date','time','Bookingfor',)
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	pass    

@admin.register(Vendorcategory)
class VendorcategoryAdmin(admin.ModelAdmin):
	pass    

@admin.register(Vendordetail)
class VendordetailAdmin(admin.ModelAdmin):
	pass        