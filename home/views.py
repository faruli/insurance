from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('static/random_forest_regressor')

# Create your views here.
def index(request):
    #return HttpResponse("This is the home page")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("This is the about page")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is the contact page")
    return render(request, 'contact.html')

def login(request):
    #return HttpResponse("This is the login page")
    return render(request, 'login.html')

def register(request):
    #return HttpResponse("This is the register page")
    return render(request, 'register.html')

def prediction(request):
    #return HttpResponse("This is the prediction page")
    if request.method == "POST":
        #print("Enter into the post request")
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        #print(age, bmi, age, children, smoker, region)

        pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])
        #print(pred)
        output = {
            "output":pred
        }

        return render(request, 'prediction.html', output)

    else:
        return render(request, 'prediction.html')

