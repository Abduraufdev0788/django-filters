from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Users
import json


def to_json(User:Users)->dict:
    return{
        "id":User.id,
        "first_name":User.first_name,
        "last_name":User.last_name,
        "email": User.email,
        "gender":User.gender,
        "rating":User.rating
    }

def add_user_view(request: HttpRequest):
    if request.method == 'POST':
        result = []
        bases = json.loads(request.body.decode())
        for data in bases:

            new_user = Users(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                gender=data['gender'],
                rating=data['rating']
            )
            new_user.save()
            result.append(to_json(new_user))

        return JsonResponse(data={'result': result, 'count': len(result)}, status=201)
    
    if request.method == "GET":
        params = request.GET
        gender = params.get("gender")
        if gender:
            users = Users.objects.filter(gender = gender)



        result = []
        for user in users:
            result.append(to_json(user))

        return JsonResponse(data={"count": len(result), "result": result}, status = 201)




