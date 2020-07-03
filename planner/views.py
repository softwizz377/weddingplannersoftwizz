from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView
from planner.models import ContactUs, Booking, Feedback, Gallery, Vendorcategory, Vendordetail
from planner.forms import ContactUsform, Bookingform, Feedbackform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class Homepageview(TemplateView):
	template_name="home.html"
class ContactUspageview(TemplateView):
	template_name="ContactUs.html"
class Servicespageview(TemplateView):
	template_name="Services.html"
class Feedbackpageview(TemplateView):
	template_name="Feedback.html"
class Aboutpageview(TemplateView):
	template_name="About.html"
class Gallerypageview(ListView):
    template_name="Gallery.html"
    def get_queryset(self):
        return Gallery.objects.all()
class Bookingpageview(TemplateView):
	template_name="Booking.html"
class Blogpageview(TemplateView):
	template_name="Blog.html"
class Vendorspageview(ListView):
    template_name="Vendors.html"
    def get_queryset(self):
        return Vendorcategory.objects.all()
class Designspageview(TemplateView):
	template_name="Designs.html"
	
	
'''def ContactUs(request):
	if request.method=='POST':
		form=ContactUsform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/ContactUs')
			except:
				pass
	else:
		form=ContactUsform()
	return render(request,'ContactUs.html',{'form':form})

def insertContactUs(request):
    if request.method == "POST":
        form = ContactUsform(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/index')
            except:
                pass
    else:
        form = ContactUsform()
    return render(request, 'index.html', {'form': form})


'''
	
def insertBooking(request):
	if request.method=='POST':
		form=Bookingform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/paytm/')
			except:
				pass
	else:
		form=Bookingform()
	return render(request,'Booking.html',{'form':form})
	

def insertfeedback(request):
	if request.method=='POST':
		form=Feedbackform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/ContactUs')
			except:
				pass
	else:
		form=Feedbackform()
	return render(request,'ContactUs.html',{'form':form})

def showvendor(request, id):
    vendordetail= Vendordetail.objects.filter(vcategory=id)
    vendorcat=Vendorcategory.objects.get(id=id)
    context={
        'vendordetail':vendordetail,
        'vendorcat':vendorcat,
    }
    
    
    return render(request,'vendordetail.html',context)