from flask import Flask, render_template,request,redirect,url_for
import os
from procesar_texto import ProcesarTexto

app = Flask(__name__)

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html',techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result',methods=['GET', 'POST'])
def result():
    content = request.form['content']
    proccess=ProcesarTexto(content)
    total_words=proccess.number_of_words()
    total_character=proccess.number_of_characters()
    most_frequent_word=proccess.frequency_words()
    density=round(proccess.lexical_density(),2)

    return render_template('result.html',content=content, total_words=total_words,total_character=total_character,most_frequent_word=most_frequent_word,density=density)

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    port=int(os.environ.get("PORT",5000))
    app.run(debug=True, host='0.0.0.0',port=port)


