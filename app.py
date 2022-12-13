from flask import Flask,request,render_template,redirect,session
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
    session['response'] = []
    return redirect('/questions/0')



# @app.route('/answer',methods=['POST','GET'])
# def collect_answers():
#     if 'response' not in session:
#         session['response'] = []


#     if request.method == 'POST':
#         answer = request.form['Name']
#         if answer:
#             session['response'].append(answer)
        
#         return redirect(f"/questions/{len(session['response'])}")
#         # return redirect('/answer')
    
#     if(len(response) == len(survey.questions)):
#         return redirect ('/complete')
#     # else:
#     #     return redirect(f"/questions/{lensession['re]}")

@app.route('/answer', methods=['GET' ,'POST'])
def  save_answers():
    
    answer =request.form.get('Name')
    response = session['response']
    response.append(answer)
    session['response'] = response

    if(len(response) == len(survey.questions)):
        return redirect('/complete')
    else:
        return redirect(f"/questions/{len(response)}")





@app.route('/questions/<int:n>')
def show_questions(n):  
    if (len(response) == len(survey.questions)):
            return redirect('/complete')

    if(response is None):
        return redirect('/')



    current_question = survey.questions[n]
    return render_template('questions.html', current= current_question )


@app.route('/complete')
def complete():
    return render_template('surveyCompletion.html',response= response)


    
    




