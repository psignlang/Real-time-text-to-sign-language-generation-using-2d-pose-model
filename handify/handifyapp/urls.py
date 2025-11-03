
from django.urls import path
from handifyapp.views import *

urlpatterns = [
    path('',LoginView.as_view(),name='login'),
    path('feedback',FeedbackView.as_view(),name='feedback'),
    path('complaints',ComplaintsView.as_view(),name='complaints'),
    path('complaint',ComplaintView.as_view(),name='complaint'),
    path('register',UserRegister.as_view(),name='register'),
    path('viewuser',UserView.as_view(),name='viewuser'),
    path('AdminHome',AdminHome.as_view(),name='AdminHome'),
    path('CompReply/<int:complaint_id>',CompReply.as_view(),name='CompReply'),
    path('rating',RatingView.as_view(),name='rating'),
    path('UserHome',UserHome.as_view(),name='UserHome')

]
