
"""
Подключите базу данных  и убедитесь, что она работает

Создайте модели

Наполните базу данных данными.

Создайте общий шаблон для страниц

– Вынесите в базовый шаблон общий html-код
– Вынесите в отдельный файл верхнее меню

Доработайте представление главной страницы

– Вынесите в подшаблон заголовочный блок
– Получите список категорий из модели категорий
– Передайте в шаблон main список категорий вместе с товарами
– Доработайте шаблон

Реализуйте добавление в корзину /addtocart/

– С кнопки на карточке товара мы переходим к добавлению товара
– id товара записывается в session["cart"]
– после этого выполняется redirect на страницу корзины
– в навигационном меню выводится количество товаров и сумма

Доработайте представление корзины

– Опишите форму заказа в файле forms.py
– Выведите форму в шаблоне cart.html
– Допишите логику 
– Добавьте форме валидацию
– Выведите ошибки валидации в шаблоне cart.html
 

Доработайте представление аутентификации

– Опишите форму аутентификации в файле forms.py
– Доработайте шаблон – выведите в нем форму
– Допишите логику представления – примите данные из формы
– Получите почту и пароль, превратите пароль в хеш
– Получите пароль из БД по введенной почте
– Сравните хеши, запишите пароли
– Если пароли совпадают, допишите информацию об id и почте пользователя в сессию
– Если пароли совпадают, сделайте редирект в личный кабинет
– Доработайте шаблон – выведите ошибки, если пароли не совпадают 

Доработайте представление регистрации

– Опишите форму аутентификации в файле forms.py
– Добавьте в форму валидацию логина (Email) и пароля (не короче 5 символов)
– Доработайте шаблон – выведите в нем форму
– Допишите логику представления – примите данные из формы
– Получите почту и пароль, превратите пароль в хеш
– Сохраните почту и пароль в БД

Доработайте представление личного кабинета

– Получите почту пользователя из сессии
– Получите список заказов из модели заказов по почте пользователя
– Доработайте шаблон account.html

Создайте админку

– добавьте административное представление для модели Пользователей
– добавьте административное представление для модели Категорий
– добавьте административное представление для модели Блюд
– добавьте административное представление для модели Заказов
"""