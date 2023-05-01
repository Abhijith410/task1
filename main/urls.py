from django.urls import path
from . import views
app_name = 'task1'

urlpatterns = [
    path('Home/', views.Homepage, name = "homepage"),
    path('login/', views.Login, name = "login"),
    path('signup/', views.Signup, name = "signup"),
    path('patient/', views.Pathome, name = "patient"),
    path('patblog/', views.Patblog, name = "patblog"),
    path('patblogdetails/<int:blogid>', views.Patblogdetails, name = "patblogdetails"),
    path('doctor/', views.Dochome, name = "doctor"),
    path('doc/', views.Doctor, name = "doc"),
    path('logout/', views.Logout, name = "logout"),
    path('dblog/', views.Doctorblog, name = "dblog"),
    path('addblog/', views.Doctoraddblog, name = "addblog"),
    path('editblog/<int:blogid>', views.Doctoreditblog, name = "editblog"),
    path('blogdetails/<int:blogid>', views.Blogdetails, name = "blogdetails"),
]    