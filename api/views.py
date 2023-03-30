from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getNoteDetail, updateNote, deleteNote, getNotesList, createNewNote


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


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        return getNotesList(request)

    if request.method == "POST":
        return createNewNote(request)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        return getNoteDetail(request, pk)

    if request.method == "PUT":
        return updateNote(request, pk)

    if request.method == "DELETE":
        return deleteNote(request, pk)


"""
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
 
    return Response(serializer.data) """
