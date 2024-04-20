from random import randint
from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
        <h1>Всем привет!!!</h1>
        <h3>Мой первый проект на Django </h3>
        <p>Постпенно тут будет добавляться информация и контент</p>
    </body>
    </html>
    """
    logging.info('Заход на главную страницу')
    return HttpResponse(html)

def game(request):
    game_list=["Орел", "Решка"]
    res = randint(0,1)
    return HttpResponse(game_list[res])

def cub(request):
    res = randint(1,6)
    return HttpResponse(f"У вас выпал купибик = {res:.2f}")

def random_number(request):
    res = randint(0,100)
    return HttpResponse(f"Случайно число = {res:.2f}")

def about(request):
    html = """
        <html>
        <head><title>О себе</title></head>
        <body>
            <h1>Информация обо мне</h1>
            <h3>Меня зовут Александр. </h3>
             <p>Я обучаюсь на GeekBrains. Пока мало опыта, но есть мало знаний</p>
        </body>
        </html>
        """
    logging.info('Посещение страницы обо мне')
    return HttpResponse(html)

