from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, man, woman, kids, login, register, profile, exit, admin, serie, add_serie, del_serie, tilla, view_tilla, add_tilla, mod_tilla, del_tilla

urlpatterns = [
    path('', home, name='home'),
    path('man', man, name='man'),
    path('woman', woman, name='woman'),
    path('kids', kids, name='kids'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile'),
    path('logout/', exit, name='exit'),
    path('admin', admin, name='admin'),
    path('serie', serie, name='serie'),
    path('add_serie', add_serie, name='add_serie'),
    path('del_serie/<id>/', del_serie, name='del_serie'),
    path('tilla', tilla, name='tilla'),
    path('view_tilla/<id>/', view_tilla, name='view_tilla'),
    path('add_tilla', add_tilla, name='add_tilla'),
    path('mod_tilla/<id>/', mod_tilla, name='mod_tilla'),
    path('del_tilla/<id>/', del_tilla, name='del_tilla'),
]