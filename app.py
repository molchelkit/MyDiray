from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

func_name = 'student_evaluations'

@app.route('/')
def index():
    return redirect(url_for(func_name))
    # return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html', title='Войти')

@app.route('/register')
def register():
    return render_template('register.html', title='Регистрация')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html', title='Преподаватель')

@app.route('/teacher/evaluations')
def teacher_evaluations():
    return render_template('teacher_evaluations.html', title='Преподаватель - Оценки')




@app.route('/student')
def student():
    return render_template('student.html', title='Студент')

@app.route('/teacher/student/evaluations')
def student_evaluations():
    return render_template('student_evaluations.html', title='Студент - Оценки')

if __name__ == '__main__':
    app.run(debug=True)