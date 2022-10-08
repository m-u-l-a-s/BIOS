from flask import Blueprint, render_template, url_for, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        lab = request.form.get("lab")
        if (lab >= "301") and (lab <= "309"):
            lab = '/imgs/lab302.png'
        else:
            lab = '/imgs/lab402.png'
    return render_template("index.html", lab=lab)


@auth.route('/index', methods=['GET', 'POST'])
def root():
    return render_template('index.html', lab='imgs/logo_mulas.png')


@auth.route('/consulta')
def consulta():
    return render_template('consulta.html')


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
    
