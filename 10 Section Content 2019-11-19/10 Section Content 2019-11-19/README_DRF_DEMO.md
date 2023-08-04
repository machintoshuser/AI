# section_10
# Django Part 2

1. Start a new project in PyCharm, using a pipenv environment. Install django, enter env, start a django project, and make initial migration.


```
pipenv install djangorestframework
pipenv install django
pipenv shell
django-admin startproject api_example
cd api_example
python manage.py migrate
```

2. Create a superuser
```
python manage.py createsuperuser
```

3. Start an app called "City"


```
python manage.py startapp city
```

4. Add city app and rest_framework to the project's `settings.py`


```python
INSTALLED_APPS = [
  ...
  'rest_framework',
  'city',
]
```

5. Add urls for city app.


In project's url.py:
```python
import django.urls.include
...
path('',include('city.urls'))
```

In city app directory: create new file `urls.py`.  
No need to add urls yet, just add:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
]
```

6. Add a model to city app for storing names and states.


In app's `models.py`:
```python
class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
```

7. Make a migration!


```
python manage.py makemigrations
python manage.py migrate
```

8. Register the model in admin.


In app's `admin.py`:
```python
from .models import City

admin.site.register(City)
```

9. Check out the admin page.


```
python manage.py runserver
```

10. Fix "citys"


In app's models.py in "City" class:
```python

class Meta:
     verbose_name_plural = 'Cities`
```

11. Create a serializer for "city".


Add a file `serializers.py` to the city app folder.
```python 
from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state')
```

12. Add a view.


In city apps `view.py`:
```python 
...
from rest_framework import viewsets
from .models import City
from .serializers import CitySerializer

# Create your views here.
class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
```

13. Make the view accessable via urls.


In the city app's `urls.py`:
```python
...
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('city', views.CityView)

urlpatterns = [
    path('',include(router.urls))
]
```

14. Check out our new view!


```python manage.py runserver```
Navigate to /city and play around with our new api. Add some cities from MA and other states.



15. Add a new view with just massachusetts states.


In the city app's views.py, add:
```python
class MACityView(viewsets.ModelViewSet):
    queryset = City.objects.filter(state__contains='MA')
    serializer_class = CitySerializer
```

16. Route the newly created view to a set of urls.


In the city app's `urls.py`:
```python
...
router.register('MAcity', views.MACityView)
```


17. Check out our new view!


```python manage.py runserver```
Navigate to /MAcity and play around with our new api. 


18. Add api documentation using swagger.


```
pip install django-rest-swagger
```
pipenv installing will throw an error


19. Add swagger to installed apps.


In project's `settings.py`:
```python
...
'rest_framework_swagger'
```


20. Add swagger to app's urls 


The final city app's `urls.py` should contain:
```python
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

router = routers.DefaultRouter()
routers.register('city',views.CityView, base_name='city')
routers.register('MAcity', views.MACityView, base_name='MAcity')

schema_view = get_schema_view(title='City API', renderer_classes = [SwaggerUIRenderer, OpenAPIRenderer])

urlpatterns = [
    path('city/', include(router.urls)),
    path('', schema_view, name = 'docs')
]
```


21. Check out our documentation!


```python manage.py runserver```


22. Add additional info to documentation.


In city app's `view.py`, in "CityView", add a docstring that uses a keyword.
```python 
    '''
    retrieve:
        Return a city instance
    '''
```
full list of operations can be found in the [docs](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)



