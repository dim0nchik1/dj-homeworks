from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    recipe = {}
    servings = int(request.GET.get('servings', 1))
    for ingredients, quantity in DATA['omlet'].items():
        recipe[ingredients] = quantity * servings
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
def pasta(request):
    recipe = {}
    servings = int(request.GET.get('servings', 1))
    for ingredients, quantity in DATA['pasta'].items():
        recipe[ingredients] = quantity * servings
    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)
def buter(request):
    recipe = {}
    servings = int(request.GET.get('servings', 1))
    for ingredients, quantity in DATA['buter'].items():
        recipe[ingredients] = quantity * servings

    context = {
        'recipe': recipe,
    }
    return render(request, 'calculator/index.html', context)