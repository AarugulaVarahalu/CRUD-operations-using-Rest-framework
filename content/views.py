from django.shortcuts import render
from .serializer import DetailSerializer
from .models import Detail
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def contact_details(request):
    contacts = Detail.objects.all()
    serializer = DetailSerializer(contacts,many=True)
    
    return Response(serializer.data)


@api_view(['POST'])
def create_contact(request):
    serializer = DetailSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def update_contact(request, id):
    contacts = Detail.objects.get(id=id)
    serializer = DetailSerializer(instance=contacts, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_contact(request, id):
    contacts = Detail.objects.get(id=id)
    contacts.save()

    return Response('items got deleted!')

@api_view(['GET'])
def view_contact(request, id):
    contacts = Detail.objects.get(id=id)
    serializer = DetailSerializer(contacts)

    return Response(serializer.data)