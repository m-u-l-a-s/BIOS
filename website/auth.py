from flask import Blueprint, render_template, url_for, request, flash
from datetime import datetime

auth = Blueprint('auth', __name__)
"""
<input type="submit" value="Selecionar" class="btn btn-secondary">
os = (lab,maq,prob,rep,stat,detalhes)

<!--<img src="../static/imgs/logo_mulas.png" id="logo">-->
"""
os = ('1','1','1','1',"Pendente", "waow")
ar = []
lab = "Laboratório"

linhas = 6
cols = 4
mntc = ["1","3","5","10",""]
reportados = ["2","4","8","18",""]

def converter(m):
    l = []
    for i in range(0,len(m)-1):
        l.append(int(m[i]))
    return l


user = {
    "user": "aluno", 
    "senha": "", 
    "email": "aluno@fatec.gov.sp.br", 
    "admin": False
}
admin = {
    "user": "admin", 
    "senha": "admin", 
    "email": "admin@fatec.gov.sp.br", 
    "admin": True
}


@auth.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@auth.route('/reportar')
def reportar():
    return render_template('reportar.html', lab=lab, linhas = linhas, cols = cols, mntc = converter(mntc), reportados = converter(reportados))


@auth.route('/reportar', methods=["GET", "POST"])
def gfg():
    from .database import Select_Lab
    if request.method == "POST":
        lab = str(request.form.get("lab"))
        maq = str(request.form.get("maq"))
        prob = str(request.form.get("prob"))
        detalhes = str(request.form.get("detalhes-os"))
        data = str(datetime.now())[:-7]
        status = "Pendente"
        if (not(lab == "" or maq == "" or prob == "" or detalhes == "")):
            from .database import Insert_OS, create_oss_table
            try: 
                create_oss_table()
            except:
                pass
            Insert_OS(lab, maq, prob, detalhes, data, status)   
        lab_info = Select_Lab(lab)
        print(lab_info)
        if len(lab_info) > 0:
            sala = Select_Lab(lab)[0][0]
            linhas = Select_Lab(lab)[0][1]
            cols = Select_Lab(lab)[0][2]
            reportados = Select_Lab(lab)[0][3]
            reportados = reportados.split(",")
            # reportados = [int(i) for i in reportados]
            mntc = Select_Lab(lab)[0][4]
            mntc = mntc.split(",")
            # mntc = [mntc[i:i+2] for i in range(0, len(mntc), 2)]
            # mntc = [int(i) for i in mntc]    
    return render_template("reportar.html",lab = lab,  os = os , linhas = linhas, cols = cols, mntc = converter(mntc), reportados = converter(reportados))

@auth.route('/img', methods=["GET", "POST"])
def img():
    if request.method == "POST":
        lab = str(request.form.get("lab"))
        print(lab)
        if (lab >= "301") and (lab <= "309"):
            lab = '/imgs/lab302.png'
        else:
            lab = '/imgs/lab402.png'
    return render_template("reportar.html", lab = lab, os = os, linhas = linhas, cols = cols, mntc = mntc, reportados = reportados)

@auth.route('/consulta')
def consulta(current_user = user):
    from .database import Select_OS, Select_Login

    ar = Select_OS()
    return render_template('consulta.html', ar = ar, user = current_user)


@auth.route('/contato')
def contato():
    return render_template('contato.html')

@auth.route('/edition', methods=['GET', 'POST'])
def edition():
    if request.method == 'POST':
        from .database import Insert_Lab, Select_Lab
        
        lab = str(request.form.get("lab"))

        if "salvar-layout" in request.form:
            # newlab = request.form.get("lab")
            num = str(request.form.get("num"))
            linhas = request.form.get("bancadas")
            colunas = request.form.get("maquinas")
            reportados = request.form.get("reportados")
            mntc = request.form.get("mntc")
            print("linhas: ",linhas)
            print(type(linhas))
            print("colunas: ", colunas)
            print("rep: ",reportados)
            print("mntc: ",mntc)

            if len(num) == 3:
                Insert_Lab(num, linhas, colunas, reportados, mntc)
                return render_template('edition.html', msg=f"Laboratório {num} alterado com sucesso!", num=num, reportados=reportados, mntc=mntc)

            else: return render_template('edition.html', erro=f"Não foi possível alterar o layout.", num=num, reportados=reportados, mntc=mntc)

        
        lab_info = Select_Lab(lab)
        print(lab_info)
        if len(lab_info) > 0:
            sala = Select_Lab(lab)[0][0]
            linhas = Select_Lab(lab)[0][1]
            cols = Select_Lab(lab)[0][2]
            reportados = Select_Lab(lab)[0][3]
            reportados = reportados.split(",")
            # reportados = [int(i) for i in reportados]
            mntc = Select_Lab(lab)[0][4]
            mntc = mntc.split(",")
            # mntc = [mntc[i:i+2] for i in range(0, len(mntc), 2)]
            # mntc = [int(i) for i in mntc]

            return render_template('edition.html', sala=sala, linhas=linhas, cols=cols, reportados=reportados, mntc=mntc)
            
        else: return render_template("edition.html", erro="Este laboratório ainda não foi registrado.")
    else: return render_template('edition.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # from .database import Select_Login

    if request.method == 'POST':
        # email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        if username == "admin" and password == "admin":
            return consulta(admin)
        else: 
            flash('Usuário não encontrado.', category='error')
    
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return render_template('sign-up.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    from .database import Insert_Login

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
            # Adicionar usuário ao banco de dados:
            Insert_Login(username, password1, email, False)
            flash('Conta criada!', category='success')
            # return redirect(url_for('views.home'))
    return render_template("sign-up.html") #user=current_user
    

