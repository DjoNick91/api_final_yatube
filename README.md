# Учебный проект Яндекс Практикума    

##  Это API для социальной сети Yatube   
Реализована возможность регистрации пользователей  через  отправку POST запросов.   
Для авторизованного пользователя есть возможность создавать посты, оставлять комментарии, и оформлять подписку на авторов.   
К посту можно добавлять изображение.   
Не авторизованные пользователи могут лишь просматривать посты и комментарии других  пользователей.   
При запросах постов реализована пагинация с limit и offset параметрами.   
Для защиты используется технология JSON Web Tokens(JWT).    
Подключена стандартная адмика Django.   


## Установка
1) Клонировать репозиторий на локальный компьютер `git@github.com:DjoNick91/api_final_yatube.git`
2) Создать виртуальное окружение `python -m venv env`
3) Активировать виртуальное окружение `source env/script/activate`
4) Установить зависимости `pip install -r requirements`  

## Использование     
Перейдите в папку с файлом __manage.py__ и выполните коммпанду `python manage.py runserver`   

## Документация    
<https://github.com/DjoNick91/api_final_yatube/blob/master/yatube_api/static/redoc.yaml>        

___Автор Евгений Ивашин___ <DjoNick91@gmail.com>