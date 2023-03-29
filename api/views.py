from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])  # specify HTTP request types allowed to this view
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns array of all notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) # many=True because we are serializing multiple objects. Will return back a queryset
    return Response(serializer.data) # serializer is an object so this returns the data to frontend

@api_view(["GET"])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)