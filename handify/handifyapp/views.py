from django.shortcuts import render
from django.views import *
from handifyapp.models import *
from django.http import HttpResponse
from handifyapp.forms import *


class LoginView(View):
    def get(self,request):
        return render(request,'Administration/login.html')
    def post(self,request):
        uname = request.POST['Username']
        passw = request.POST['Password']
        obj = LoginTable.objects.get(Username=uname, Password=passw)
        
        request.session['userid']= obj.id
        if obj.UserType == 'admin':
            return HttpResponse('''<script>alert("Welcome back");window.location='/AdminHome'</script>''')
        elif obj.UserType == 'user':
            return HttpResponse('''<script>alert("Welcome back");window.location='/UserHome'</script>''')    
        else:
            return HttpResponse('''<script>alert("user not found");window.location='/'</script>''')
class FeedbackView(View):
    def get(self,request):
        feedback=FeedbackTable.objects.all()
        return render(request,'Administration/feedback.html',{'obj':feedback})

class ComplaintsView(View):
    def get(self,request):
        complaints=ComplaintsTable.objects.all()
        return render(request,'Administration/complaints.html',{'obj':complaints})


class AdminHome(View):
    def get(self,request):
        return render(request,'Administration/AdminHome.html')        

class ComplaintView(View):
    def get(self,request):
        return render(request,'user/complaint.html')  

    def post(self,request):
            login_id = request.session.get('userid')
            if not login_id:
                return redirect('/login')


            complaint_text  = request.POST.get('complaints')

            user = UserTable.objects.get(LOGINID__id=login_id)

            ComplaintsTable.objects.create(
                USERID=user,
                Complaints=complaint_text
            )               
            return HttpResponse('''<script>alert("complaint sended successfully");window.location='/'</script>''')

class RatingView(View):
    def get(self, request):
        return render(request, 'user/rating.html')

    def post(self, request):
        rating = request.POST.get('rating')
        feedback = request.POST.get('feedback')
        userid = request.session.get('userid')

        if userid:
            user = UserTable.objects.get(LOGINID__id=userid)
            FeedbackTable.objects.create(
                Feedback=feedback,
                Rating=rating,
                USERID=user,
                
            )
            return HttpResponse(
                '''<script>alert("Feedback sent successfully");window.location='/'</script>'''
            )
        else:
            return HttpResponse(
                '''<script>alert("Feedback failed");window.location='/'</script>'''
            )
class UserView(View):
    def get(self,request):
        users=UserTable.objects.all()
        return render(request,'Administration/viewuser.html',{'obj':users})   

class CompReply(View):
    def post(self,request,complaint_id):
        reply =request.POST['Reply']
        obj = ComplaintsTable.objects.get(id=complaint_id)
        obj.Reply=reply
        obj.save()
        return HttpResponse('''<script>alert("reply sended successfully");window.location='/complaints'</script>''')

class UserHome(View):
    def get(self,request):
        return render(request,'user/UserHome.html') 

class UserRegister(View):
    def get(self,request):
        return render(request,'user/register.html')

    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)   
            login_obj = LoginTable.objects.create(
                Username=request.POST['uname'],
                Password=request.POST['passw'],
                UserType='user'
            )       
            f.LOGINID = login_obj
            f.save()
            return HttpResponse('''<script>alert("Registration Successfull");window.location='/'</script>''')
        else:
            return HttpResponse('''<script>alert("Not registered");window.location='/'</script>''')        