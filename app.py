from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html', title='Войти')

@app.route('/register')
def register():
    return render_template('register.html', title='Регистрация')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Профиль')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html', title='Преподаватель')

@app.route('/teacher/evaluations')
def teacher_evaluations():
    return render_template('teacher_evaluations.html', title='Преподаватель - Оценки')

@app.route('/teacher/inquiry')
def teacher_inquiry():
    return render_template('teacher_inquiry.html', title='Преподаватель - Расписание')

@app.route('/teacher/homework')
def teacher_homework():
    return render_template('teacher_homework.html', title='Преподаватель - Домашнее задание')

@app.route('/teacher/homework/add')
def teacher_homework_add():
    return render_template('teacher_homework_add.html', title='Преподаватель - Добавить омашнее задание')

@app.route('/teacher/reports')
def teacher_reports():
    return render_template('teacher_reports.html', title='Преподаватель - Отчеты')


@app.route('/student')
def student():
    return render_template('student.html', title='Студент')

@app.route('/student/evaluations')
def student_evaluations():
    return render_template('student_evaluations.html', title='Студент - Оценки')

@app.route('/student/inquiry')
def student_inquiry():
    return render_template('student_inquiry.html', title='Студент - Расписание')

@app.route('/student/homework')
def student_homework():
    return render_template('student_homework.html', title='Студент - Домашнее задание')

if __name__ == '__main__':
    app.run(debug=True)

# if/else jinja teacher and student