from django.db import models

# Each class is a table in the database, each attribute is a column in the table, and each instance is a row in the table.


class Note(models.Model):
    body = models.TextField(
        null=True, blank=True
    )  # null=True means that the body field can be empty, blank=True means that the body field can be empty when the form is submitted.
    updated = models.DateTimeField(
        auto_now=True
    )  # auto_now=True means that the updated field will be updated every time the Note is saved.
    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=True means that the created field will be updated when the Note is created.

    def __str__(self):
        return self.body[:50]
