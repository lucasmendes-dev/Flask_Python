from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

lista_usuarios = ["Lucas", "Maria", "Luan", "Nair", "Dilton"]

app.config['SECRET_KEY'] = 'de31e7c94ed3196b52d6cdad88d5062f'  #através do secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():    
    return render_template('contato.html')

@app.route('/lista_usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()
    
    if form_login.validate_on_submit() and 'submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')   #.data = resultado que o user preencheu
        return redirect(url_for('home'))
        
    if form_criar_conta.validate_on_submit() and 'submit_criar_conta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criar_conta.email.data}', 'alert-success')   #alert-success do bootstrap
        return redirect(url_for('home'))
        
    return render_template('login.html', form_login=form_login, form_criar_conta=form_criar_conta)



if __name__ == '__main__':
    app.run(debug=True)
