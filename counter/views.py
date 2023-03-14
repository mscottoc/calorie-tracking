from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class asdffood:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

class asdfday:
    intake = dict()
    def __init__(self, date):
        self.date = date
    
    def add_food(self, food):
        if self.intake.get(food):
            self.intake.food += 1
        else:
            self.intake[food] = 1
        print(self.intake)


def hello_world(request):
    apple = {'name' : "Apple", 
             'calories' : 130, 
             'protein' : 1, 
             'carbs' : 34,
             'fat' : 0}
    today = { 'date' : '03/13/23',
              'meals' : [{'data' : apple,
                         'servings' : 1}]}
    yesterday ={'date' : '03/12/23',
                'meals' : [{'data' : apple,
                           'servings' : 2}]}
    profile = { 'name': 'Scott',
                'history': [today, yesterday]
            }
    for day in profile['history']:
        for food in day['meals']:
            day.update({'total' : {'calories' : food['data']['calories'] * food['servings']}})
    return render(request, 'results.html', profile)
