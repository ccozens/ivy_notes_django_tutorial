from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def getNoteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk):
    data = request.data  # get json data
    note = Note.objects.get(id=pk)  # get note
    serializer = NoteSerializer(
        instance=note, data=data
    )  # convert json to Python data form
    if serializer.is_valid():  # check data valid
        serializer.save()  # save returns an object instance, based on the validated data.
    return Response(serializer.data)


def getNotesList(request):
    notes = Note.objects.all().order_by("-updated")  # orders by most recently updated
    serializer = NoteSerializer(
        notes, many=True
    )  # many=True because we are serializing multiple objects. Will return back a queryset
    return Response(
        serializer.data
    )  # serializer is an object so this returns the data to frontend


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted")


def createNewNote(request):
    data = request.data
    note = Note.objects.create(body=data["body"])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
