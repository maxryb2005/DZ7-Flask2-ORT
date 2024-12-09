# Импортируем необходимые модули из библиотеки Flask
# Flask - это веб-фреймворк для разработки веб-приложений на Python
# render_template используется для рендеринга HTML-шаблонов
# redirect, url_for - используются для перенаправления пользователей
# request используется для обработки HTTP-запросов
# session позволяет сохранять данные на стороне сервера для текущего пользователя
from flask import Flask, render_template, redirect, url_for, request, session

# Определяем объект нашего приложения Flask
# __name__ передается для корректного определения корневого пути
app = Flask(__name__)

# Устанавливаем секретный ключ для приложения
# Секретный ключ используется для подписи сессионных данных и защиты от атак
app.secret_key = 'secret_tccc'  # Замените на уникальный ключ для повышения безопасности

# Словарь для хранения пользователей
# Здесь упрощенно хранятся имена пользователей и соответствующие пароли
users = {"Tanya": "Rockstar_75831"}


@app.route('/')
def index():
    # Обрабатываем запрос на корневой URL приложения
    # Отображаем HTML-шаблон index.html при заходе на главную страницу
    return render_template('index.html')


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    # Обрабатываем запросы на страницу авторизации
    if request.method == 'POST':  # Проверяем, пришел ли POST-запрос
        # Получаем имя пользователя и пароль из формы
        username = request.form.get('username')
        password = request.form.get('password')

        # Проверяем, есть ли введенные данные в словаре пользователей
        if username in users and users[username] == password:
            # Если данные корректны, сохраняем имя пользователя в сессию
            session['username'] = username
            # Перенаправляем на главную страницу
            return redirect(url_for('index'))
        else:
            # Если данные неверные, возвращаем сообщение об ошибке
            return "Неправильный логин или пароль. Введите заново."

    # Если запрос GET, отображаем HTML-шаблон для авторизации
    return render_template('authorization.html')


@app.route('/about')
def about():
    # Обрабатываем запрос на страницу 'О нас'
    # Возвращаем HTML-шаблон about.html
    return render_template('about.html')


@app.route('/moments')
def moments():
    # Обрабатываем запрос на страницу 'Моменты'
    # Возвращаем HTML-шаблон moments.html
    return render_template('moments.html')


@app.route('/logout')
def logout():
    # Обрабатываем запрос на выход из системы
    # Удаляем имя пользователя из сессии
    session.pop('username', None)
    # Перенаправляем на главную страницу после выхода
    return redirect(url_for('index'))


# Проверяем, если файл запущен напрямую
if __name__ == "__main__":
    # Запускаем Flask-приложение с включенным режимом отладки
    # Это позволяет видеть ошибки и перезагружать сервер при изменениях в коде
    app.run(debug=True)