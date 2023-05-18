from .models import datas
from .serializers import dataserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def datas_list(request):
    if request.method == 'GET':
        dataserial = datas.objects.all()
        serializer = dataserializer(dataserial, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def datas_detail(request,id):
    try:
        dataserial = datas.objects.get(id=id)
    except datas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = dataserializer(dataserial)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = dataserializer(dataserial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dataserial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)