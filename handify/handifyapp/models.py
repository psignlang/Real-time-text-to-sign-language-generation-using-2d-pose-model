from django.db import models

class LoginTable(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    UserType = models.CharField(max_length=100, null=True,blank=True)

class UserTable(models.Model):
    Name = models.CharField(max_length=100, null=True,blank=True)
    Email = models.CharField(max_length=100, null=True,blank=True)
    Gender = models.CharField(max_length=100, null=True,blank=True)
    Age = models.IntegerField(max_length=50, null=True,blank=True)
    LOGINID = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)

class ComplaintsTable(models.Model):
    Complaints = models.CharField(max_length=200,null=True,blank=True)
    Reply = models.CharField(max_length=200,null=True,blank=True)
    Date = models.DateField(null=True,blank=True, auto_now_add=True)
    USERID = models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    
class FeedbackTable(models.Model):
    Feedback = models.CharField(max_length=200,null=True,blank=True)   
    Rating = models.CharField(max_length=200,null=True,blank=True)
    Date = models.DateField(null=True,blank=True, auto_now_add=True)
    USERID = models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
