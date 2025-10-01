from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None
    height = None
    weight = None

    if request.method == "POST":
            height = float(request.POST.get("height"))
            weight = float(request.POST.get("weight"))
            bmi = round(weight / ((height/100) ** 2), 2)
            print(f"height : {height} cm, weight : {weight} kg, bmi : {bmi}")
    return render(request, "myapp/math.html",{"bmi": bmi})