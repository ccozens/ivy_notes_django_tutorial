# Notes app

This app was written following [Dennis Ivy's youtube tutorial](https://www.youtube.com/watch?v=tYKRAXIio28&t=61s). The react standalone is [here](https://github.com/ccozens/ivy_notes_react_tutorial).

## CORS

CORS error occured when trying to call django rest api running on localhost://8000. Need to install [cors-headers](https://github.com/adamchainz/django-cors-headers) to specifically permit it.

## Deploying as a single app

1. copy react app into django folder: `cp -a ivy_notes_react_tutorial/* ivy_notes_django_tutorial/frontend/` (note followed by `rm -r ivy_notes_react_tutorial/node_modules/` to remove node_nodules from standalone app).
