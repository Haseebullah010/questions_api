from ast import GtE
from http.client import HTTPResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from questions_modules.models import QuestionNo_weighted_fever,options_questions,cough_questions

from django.core import serializers

# Create your views here.
@csrf_exempt
def fever(request):
    questions = cough_questions.objects.all()
    final_data1=[]
    for l in questions:
        options=[]
        all_option=options_questions.objects.filter(question=l.id)
        for data in all_option:
            options.append({
                "options_id":data.id,
                "options_data":data.option1,
            })
        final_data1.append({
                    "question_data":l.Question,
                    "question_id":l.id,
                    "option":options,
                    
                })
    
    return JsonResponse({"Questions":final_data1},safe=False)
    
    
@csrf_exempt
def abdominal(request):
    
    context ={
        "name":"hase"
    }
    return JsonResponse(context)

@csrf_exempt
def blood(request):
    context ={
        "name":"hase"
    }

    return JsonResponse(context)

@csrf_exempt
def cough(request):
    context ={
        "name":"hase"
    }

    return JsonResponse(context)