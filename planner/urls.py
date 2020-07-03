from django.urls import path, include
from planner import views
urlpatterns = [
    path('home/',views.Homepageview.as_view()),
	path('ContactUs/',views.ContactUspageview.as_view()),
	#path('insertContactUs',views.ContactUs),
    
	path('Services/',views.Servicespageview.as_view()),
	
	path('Feedback/',views.Feedbackpageview.as_view()),
	path('insertfeedback',views.insertfeedback),
	path('About/',views.Aboutpageview.as_view()),
	path('Gallery/',views.Gallerypageview.as_view()),
	path('Booking/',views.Bookingpageview.as_view()),
	path('insertBooking',views.insertBooking),
	path('Blog/',views.Blogpageview.as_view()),
	path('Vendors/',views.Vendorspageview.as_view()),
    path('Designs/',views.Designspageview.as_view()),
    path('vendordetail/<int:id>',views.showvendor),
	
	]


