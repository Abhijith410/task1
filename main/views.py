from django.shortcuts import render,redirect
from . models import *
# Create your views here.

def Homepage(request):
    return render(request, "files/home.html")

def Login(request):
    if request.method == 'POST':
        user_name = request.POST['logusername']
        pass_word = request.POST['loguserpass']
        try:
            log = Registration.objects.get(username = user_name, password = pass_word)
            request.session['session_id'] = log.id
            if log.usertype == 'Doctor':
                return redirect ('task1:doctor')
            elif(log.usertype == 'Patient'):
                return redirect ('task1:patient')
            else:
                return render (request, "files/login.html", {'fail':'Incorrect credentials'})
        except Registration.DoesNotExist:
            return render (request, "files/login.html", {'fail':'No user found'}) 
    return render(request, "files/login.html")

def Signup(request):
    message = ""
    if request.method == "POST":
        option = request.POST.get('options', None)
        f_name = request.POST['regfname']
        l_name = request.POST['reglname']
        e_mail = request.POST['regmail']
        add_ress = request.POST['regaddress']
        user_name = request.POST['regusername']
        pass_word = request.POST['regpass']
        confirm_password = request.POST['regconfpass']
        image_ = request.FILES['regimage']
        data = Registration(usertype = option, firstname = f_name, lastname = l_name, email = e_mail, address = add_ress, username = user_name, password = pass_word, confpassword = confirm_password, image = image_)
        if option == 'Doctor' or option == 'Patient':
            data.save()
            message = "Input registered successfully. Now you can login to your account."
        else:
            message = "Error. Choose usertype and try again."  
    return render(request, "files/signup.html", {'msg':message})

def Dochome(request):
    if 'session_id' in request.session:
        d_id = request.session['session_id']
        doctor = Registration.objects.filter(id = d_id).all()
        return render(request, "files/doctorhome.html", {'doc_data': doctor})
    else:
        return render(request, "files/login.html")

def Pathome(request):
    if 'session_id' in request.session:
        p_id = request.session['session_id']
        patient = Registration.objects.filter(id = p_id).all()
        return render(request, "files/patienthome.html", {'p_data': patient})
    else:
        return render(request, "files/login.html")

def Logout(request):
    del request.session['session_id']
    return redirect ('task1:login')