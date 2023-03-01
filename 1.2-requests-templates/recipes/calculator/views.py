from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
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


def main_page(request):
    return render(request, template_name='calculator/main_page.html')


def recipe_calculation(request, food):
    print("request =", request)
    quantity = int(request.GET.get('serving', 1))
    context = {
        # 'recipe': DATA[food],
        'recipe': {k: v * quantity for k, v in DATA[food].items()},
        'quantity': quantity,
    }
    print(context)
    return render(request, template_name='calculator/index.html', context=context)
