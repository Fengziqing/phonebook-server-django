from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ApiForPhonebook.models import People
from ApiForPhonebook.serializers import PeopleSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def PeopleApi(request,requestId=0):
    if request.method == 'GET':
        people = People.objects.all()
        people_serializer = PeopleSerializer(people, many=True)
        return JsonResponse(people_serializer.data, safe=False)
    elif request.method == 'POST':
        people_data = JSONParser().parse(request)
        people_serializer = PeopleSerializer(data=people_data)
        if people_serializer.is_valid():
            people_serializer.save()
            return JsonResponse(people_serializer.data, safe=False)
            # 'safe=False' for serialization
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        people_data = JSONParser().parse(request)
        people = People.objects.get(id=people_data['id'])
        people_serializer = PeopleSerializer(people, data=people_data)
        if people_serializer.is_valid():
            people_serializer.save()
            return JsonResponse(people_serializer.data, safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        people = People.objects.get(id=requestId)
        people.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
