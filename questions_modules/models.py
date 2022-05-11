from asyncio.windows_events import NULL
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model 


class QuestionNo_weighted_cough(models.Model):
    Question= models.CharField(max_length=1000)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100,null=True, blank=True)
    option3= models.CharField(max_length=100,null=True, blank=True)
    option4= models.CharField(max_length=100,null=True, blank=True)
    option5= models.CharField(max_length=100,null=True, blank=True)
    option6= models.CharField(max_length=100,null=True, blank=True)
    option7= models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return str(self.id)


        
class QuestionNo_weighted_abdominal(models.Model):
    Question= models.CharField(max_length=1000)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)

class QuestionNo_weighted_fever(models.Model):
    Question= models.CharField(max_length=1000)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)


class QuestionNo_blood(models.Model):
    Question= models.CharField(max_length=1000)
    option1= models.CharField(max_length=100)
    option2= models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return str(self.id)


class cough_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(cough_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)


