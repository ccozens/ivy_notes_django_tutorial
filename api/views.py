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
    notes = Note.objects.all().order_by("-updated")  # orders by most recently updated
    serializer = NoteSerializer(
        notes, many=True
    )  # many=True because we are serializing multiple objects. Will return back a queryset
    return Response(
        serializer.data
    )  # serializer is an object so this returns the data to frontend


@api_view(["GET"])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateNote(request, pk):
    data = request.data  # get json data
    note = Note.objects.get(id=pk)  # get note
    serializer = NoteSerializer(
        instance=note, data=data
    )  # convert json to Python data form
    if serializer.is_valid():  # check data valid
        serializer.save()  # save returns an object instance, based on the validated data.
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted")


@api_view(["POST"])
def createNote(request):
    data = request.data  # json data
    note = Note.objects.create(
        body=data["body"]  # updated and created fields automatically generated
    )
    serializer = NoteSerializer(note, many=False)
 
    return Response(serializer.data)
