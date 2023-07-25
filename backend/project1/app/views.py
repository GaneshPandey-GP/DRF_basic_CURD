from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def GetStudentInfo(requests):
    if requests.method=='GET':
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse({"Response":serializer.data})
    else:
         return JsonResponse({"Response":"{} Method not allowed".format(requests.method)})
    
@csrf_exempt
def InsertNewStudent(requests):
    if requests.method=='POST':
        body=requests.body
        _data=json.loads(body)
        serializer=StudentSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Response":"New User Added to the database."}) 
        else:
            return JsonResponse({"Error":serializer.errors}) 
    else:
         return JsonResponse({"Response":"{} Method not allowed".format(requests.method)})    




@csrf_exempt
def InsertNewStudent_inBulk(requests):
    if requests.method=='POST':
        body=requests.body
        _data=json.loads(body)
        serializer=StudentSerializer(data=_data["data"],many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Response":"New User Added to the database."}) 
        else:
            return JsonResponse({"Error":serializer.errors}) 
    else:
         return JsonResponse({"Response":"{} Method not allowed".format(requests.method)})    
    






@csrf_exempt
def UpdateStudent(requests):
    if requests.method=='POST':
        body=requests.body
        _data=json.loads(body)
        id=_data['id']
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Response":"Successfully Updated."}) 
        else:
            return JsonResponse({"Error":serializer.errors}) 
    else:
         return JsonResponse({"Response":"{} Method not allowed".format(requests.method)})    
    

@csrf_exempt
def DeleteInfo(requests):
    if requests.method=='DELETE':
        body=requests.body
        _data=json.loads(body)
        id=_data['id']
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({"Response":"Successfully Deleted."}) 
    else:
         return JsonResponse({"Response":"{} Method not allowed".format(requests.method)})    



    


