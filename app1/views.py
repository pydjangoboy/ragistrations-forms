from django.shortcuts import render


def ShowIndex(request):
    return render(request, 'index.html')


def ShowData(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    email = request.POST.get("t4")
    gender = request.POST.get("t5")
    desig = request.POST.get("t6")
    salary = request.POST.get("t7")
    uname = request.POST.get("t8")
    upass = request.POST.get("t9")

    dict = {
        'name': name,
        'age': age,
        'contact': contact,
        'email': email,
        'gender': gender,
        'designation': desig,
        'salary': salary,
        'username': uname,
        'user_password': upass,
    }
    return render(request, 'showdata.html',dict)
