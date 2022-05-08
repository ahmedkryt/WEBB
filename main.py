import csv

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/guitar_lessons')
def guitar_lessons():
    return render_template('template.html')


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/css_for_form.css')}" />
                            <style>''' + """
                               body {
                                background: url(static/img/background_for_form.jpg) no-repeat;
                                background-size: 100% 115%;
                               }
                            """ + f'''
                            </style>
                            <title>Регистрация нового пользователя</title>
                          </head>
                          <body>
                            <h1><font color='white'>Привет! Прежде, чем воспользоваться БЕСПЛАТНЫМИ уроками,</font></h1>
                            <h1><font color='white'>ответь на пару вопросов!</font></h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                    required placeholder="Email (Введите номер карты)" name="email">
                                    <input type="password" class="form-control" id="password" 
                                    required placeholder="Пароль (CVV2)" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Сколько вам лет?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>-3 Юху!</option>
                                          <option><10</option>
                                          <option>>10<16</option>
                                          <option>>16<20</option>
                                          <option>В меру упитанный мужчина</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Напишите свои ожидания по курсу</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Загрузите аватар</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex"
                                           id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" 
                                          id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept"
                                        required='required'>
                                        <label class="form-check-label" 
                                        for="acceptRules">Правила пользования гитарой принимаю</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Перейти к урокам</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/{f.filename}', 'wb') as file:
            file.write(f.read())
        lst = []
        with open('static/csv/person.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';', quotechar='"')
            for i in reader:
                lst.append(i)
        if len(lst) == 0:
            with open('static/csv/person.csv', 'w', encoding='utf-8') as file:
                try:
                    file.write('email;password;class;about;accept;sex' + '\n')
                    file.write(request.form['email'] + ';')
                    file.write(request.form['password'] + ';')
                    file.write(request.form['class'] + ';')
                    file.write(request.form['about'] + ';')
                    file.write(request.form['accept'] + ';')
                    file.write(request.form['sex'] + '\n')
                except:
                    pass
            return render_template('1.html')

        else:
            with open('static/csv/person.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=';', quotechar='"')
                file_background = url_for('static', filename=f'{f.filename}')
                for i in reader:
                    return f'''<!doctype html>
                                       <html lang="en">
                                       <head>
                                       <meta charset="UTF-8">
                                       <title>Старый пользователь</title>
                                           <style>''' + '''
                                           body {
                                            background:''' + f'''url({file_background}) no-repeat;
                                            background-size: cover;''' + '''
                                           }''' + f'''
                                           </style>
                                       </head>
                                       <body>
                                       <font color='white'><h1>{i['email']}, это снова Вы!</font>
                                           <a href='guitar_lessons'>Твоя ссылка!</a></h1>
                                       </body>
                                       </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
