# Ex.05 Design a Website for Server Side Processing
## Date:01.10.2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side. 


## FORMULA:
BMI = W/H<sup>2</sup>
<br> BMI --> Body Mass Index
<br> W --> Weight
<br> H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
    <style>
        body {
            background-color: #E3F2FD;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            background-color: #BBDEFB;
            width: 400px;
            padding: 25px;
            border-radius: 20px;
            text-align: center;
        }
        input {
            margin: 8px;
            padding: 10px;
            width: 50%;
        }
        input[type="submit"] {
            width: auto;
            background-color: Grey;
            color: white;
            cursor: pointer;
        }
        .result {
            margin-top: 10px;
            font-weight: 900;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>BMI CALCULATOR</h2>
        <h3>Name: Aashif ahamed S</h3>
        <h3>Reg No: 25013503</h3>

        <form method="post">
            {% csrf_token %}
            <label>Height (cm):</label><br>
            <input type="number" name="height" required>
            <br>
            <label>Weight (kg):</label>
            <br>
            <input type="number" name="weight" required>
            <br>
            <input type="submit" value="CALCULATE BMI">
        </form>
        
        <div class="result">
            Your BMI: {{ bmi }}
        </div>
    </div>
</body>
</html>

urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bmi/", views.bmi_calculator, name="bmi_calculator"),
]

views.py
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
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot (21).png>)

## HOMEPAGE:
![alt text](<Screenshot (22).png>)

## RESULT:
The program for performing server side processing is completed successfully.
