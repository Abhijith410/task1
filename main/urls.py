from django.urls import path
from . import views
app_name = 'task1'

urlpatterns = [
    path('Home/', views.Homepage, name = "homepage"),
    path('login/', views.Login, name = "login"),
    path('signup/', views.Signup, name = "signup"),
    path('patient/', views.Pathome, name = "patient"),
    path('doctor/', views.Dochome, name = "doctor"),
    path('logout/', views.Logout, name = "logout"),
]    