from flask import Flask,request,render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
response = []



@app.route('/')
def home_page():
    return render_template('home.html',survey= survey)


# @app.route('start',method=['POST'])
# def start_survey():
#     return redirect('/questions/0')

@app.route('/questions')
def show_questions():
    # if (len(response) == len(survey.questions)):
    #     return redirect('surveyCompletion.html')
    # question = survey.questions[num]
    # res = request.form.get['someName'].value
    # response.append(res)
    # print(response)
    return render_template('questions.html',survey= survey)


@app.route('/questions/2',methods=['post'])
def next_question():
    answer = request.form['Name']
    response.append(answer)
    print(response)
    return redirect('/questions/2')


@app.route('/questions/2')
def question2():
    return render_template('surveyCompletion.html')

@app.route('/answers',methods=['POST'])
def save_answer():
    return render_template('answers.html',response= response)



