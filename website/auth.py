from flask import Blueprint, render_template, url_for, request, flash


auth = Blueprint('auth', __name__)
"""
<input type="submit" value="Selecionar" class="btn btn-secondary">
os = (lab,maq,prob,rep,stat,detalhes)
"""
os = ('1','1','1','1',"Pendente", "waow")
ar = []
lab = ""


@auth.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@auth.route('/reportar')
def reportar():
    return render_template('reportar.html', lab=lab)


@auth.route('/reportar', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        lab = str(request.form.get("lab"))
        maq = str(request.form.get("maq"))
        prob = str(request.form.get("prob"))
        detalhes = str(request.form.get("detalhes-os"))
        #os = (lab,maq,prob,'1',False, detalhes)
        #ar.append(os)
        from .database import Insert_OS, create_oss_table
        try: 
            create_oss_table()
        except:
            pass
        Insert_OS(lab, maq, prob, detalhes, "Pendente")
        if (lab >= "301") and (lab <= "309"):
            lab = '/imgs/lab302.png'
        else:
            lab = '/imgs/lab402.png'
    return render_template("reportar.html", lab = lab, os = os)


@auth.route('/consulta')
def consulta():
    from .database import Select_OS
    user = {
        "user": "jonas",
        "senha": "123",
        "email": "jonas@fatec",
        "admin": True
    }
    ar = Select_OS()
    return render_template('consulta.html', ar = ar, user = user)


@auth.route('/contato')
def contato():
    return render_template('contato.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('sign-up.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        # Pegar dados do usuário do banco de dados:
        # user = ?
        # if user:
        #     flash('Email already exists.', category='error')
        if len(email) < 4:
            flash('Seu email deve ter pelo menos 4 caracteres.', category='error')
        elif len(username) < 3:
            flash('Seu nome de usuário deve ter pelo menos 3 caracteres.', category='error')
        elif password1 != password2:
            flash('Senhas não coincidem.', category='error')
        elif len(password1) < 6:
            flash('Para sua segurança, crie uma senha de pelo menos 6 caracteres!', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            # Adicionar usuário ao banco de dados:
            # db.session.add(new_user)
            # db.session.commit()
            # login_user(new_user, remember=True)
            # flash('Account created!', category='success')
            # return redirect(url_for('views.home'))
    return render_template("sign-up.html") #user=current_user
    

