from django.shortcuts import render
from .models import User


# Create your views here.
def all_users(request):
    user_male = User.objects.filter(gender=1)  # Пользователи мужского пола
    user_female = User.objects.filter(gender=2)  # Пользователи женского пола
    context = {
        'user_male': user_male,
        'user_female': user_female
    }

    return render(request=request, template_name='index.html', context=context)


def double_filter_man(request):
    template_ = 'double_filter_man.html'
    man = User.objects.filter(gender=1, age__gte=18)
    context = {
        'man': man
    }
    return render(request=request, template_name=template_, context=context)

def double_filter_woman(request):
    template_ = 'double_filter_women.html'
    woman = User.objects.filter(gender=2, age__gte=18)
    context = {
        'woman': woman
    }
    return render(request=request, template_name=template_, context=context)