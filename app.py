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


@app.route('/start',methods=['POST'])
def start_survey():
    return redirect('/questions/0')



@app.route('/answer',methods=['POST'])
def collect_answers():
    answer = request.form['Name']
    response.append(answer)
    if(len(response) == len(survey.questions)):
        return redirect ('/complete')
    else:
        return redirect(f"/questions/{len(response)}")






@app.route('/questions/<int:n>')
def show_questions(n):  
    if (len(response) == len(survey.questions)):
            return redirect('/complete')

    if(response is None):
        return redirect('/')

    if(len(response) == len(survey.questions)):
        return redirect ('/complete')

    current_question = survey.questions[n]
    return render_template('questions.html', current_question= current_question )


@app.route('/complete')
def complete():
    return render_template('surveyCompletion.html')


    
    




