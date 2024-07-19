import random

from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from cabinet.models import Contract, Finance
from users.forms import RegistrationForm, LoginForm
from users.models import User


def generate_unique_number() -> int:
    """Функция, которая генерирует случайное, уникальное число"""
    unique_number = ''
    for i in range(7):
        unique_number += str(random.randint(1, 9))
    if User.objects.filter(username=unique_number).exists():
        # Если число уже используется, генерируем другое
        return User.generate_unique_number()
    return int(unique_number)


def registration(request):
    """Представление регистрации пользователя"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = generate_unique_number()
            # Создание экземпляра пользователя без сохранения в базе данных
            user = User(**form.cleaned_data, username=login)
            # Устанавливаем пароль
            password = str(generate_unique_number())
            user.set_password(password)
            # Сохраняем пользователя в базе данных
            user.save()

            # Создаем договор
            title = f'{login}/{1}'
            contract = Contract.objects.create(title=title, owner=user)
            contract.save()

            # Создаем баланс к договору
            balance = Finance.objects.create(title=title, contract=contract)
            balance.save()

            # Сохраняем логин и пароль в сессии
            request.session['login'] = login
            request.session['password'] = password

            # Перенаправляем пользователя на страницу для отображения логина и пароля
            return redirect('show-login-password/')

    else:
        form = RegistrationForm()
    return render(request, 'users/registr_form.html', {'form': form})


def show_login_password(request):
    """Представление показа логина и пароля пользователю"""

    # Получаем логин и пароль из сессии
    login = request.session.get('login')
    password = request.session.get('password')

    # Проверяем и удаляем данные из сессии
    if login and password:
        del request.session['login']
        del request.session['password']

        # Записываем данные в контекст для последующей передачи в шаблон
        context = {
            'login': login,
            'password': password
        }
        return render(request, 'users/show_login_password.html', context)

    else:
        return redirect('registration')


def user_login(request):
    """Представление входа пользователя в систему"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Аутентифицируем пользователя
            user = authenticate(username=int(data['username']), password=data['password'])
            # Проверяем на наличие пользователя, если есть - авторизуем
            if user and user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('cabinet:cabinet'))
            else:
                return render(request, 'users/login_form.html', {'error': 'Неверный логин или пароль'})
    else:
        form = LoginForm()
        return render(request, 'users/login_form.html', {'form': form})


class LogoutView:
    """Представление выхода пользователя из системы"""
    pass
