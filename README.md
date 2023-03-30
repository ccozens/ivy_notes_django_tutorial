# Notes app

This app was written following [Dennis Ivy's youtube tutorial](https://www.youtube.com/watch?v=tYKRAXIio28&t=61s). The react standalone is [here](https://github.com/ccozens/ivy_notes_react_tutorial).

## CORS

CORS error occured when trying to call django rest api running on localhost://8000. Need to install [cors-headers](https://github.com/adamchainz/django-cors-headers) to specifically permit it.

## Deploying as a single app

1. copy react app into django folder: `cp -a ivy_notes_react_tutorial/* ivy_notes_django_tutorial/frontend/` (note followed by `rm -r ivy_notes_react_tutorial/node_modules/` to remove node_nodules from standalone app).
2. build react app: cd into frontend and `npm run build`
3. Set location of frontend static build files in django `settings.py`:

   ```python
   # line 59
   TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "frontend/build"],
        ....
    }

    # add at line 125
    STATICFILES_DIRS = [
        BASE_DIR / 'frontend/build/static'
    ]
   ```

4. Set react `index.html` as template view for django homepage. In `urls.py`:

   ```python
   # add import
   from django.views.generic import TemplateView

   # add urlpattern
   urlpatterns = [
       ...
       path("", TemplateView.as_view(template_name="index.html")),
   ]
   ```

At this point, you can switch between notes as react handles the routing, but when trying to go to note absolute URL or access PUT/POST django complains as it cannot find the route. This wouldn't occur if react app was deployed to netlify and Django app deployed elsewhere.
Few fixes:

1. don't add `path('note/<>')` to `urlpatterns.py`. Works, but means creating two different URL parths (1 in react, 1 in django).
2. Quick, but looks funny. Use hashrouter in React - change `import BrowserRouter as Router` to `import HashRouther as Router`. Now homepage changes to `http://localhost:8000/#/` to show react is dealing with the routing.
3. Go to Django, replicate every URL, and point to react project. For more, look up "react router URL issues server side rendering".

## Making apis RESTful
