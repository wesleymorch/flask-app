from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dicionário de dados dos times (PARA PASSAR PARA OS TEMPLATES)
dados_times = {
    'barcelona': {
        'id': 'barcelona',
        'nome': 'BARCELONA',
        'cor_principal': '#A50044', # Vinho
        'cor_secundaria': '#004D98', # Azul
        'logo_url': 'escudo_barcelona.png',
        'parallax_img': 'camp_nou.jpg', # CONFIRMAR: Esta imagem deve existir em static/
        'titulos_importantes':
            ['3X MUNDIAL DE CLUBES DA FIFA',
             '5X CHAMPIONS LEAGUE',
             '27X LA LIGA',
             '32X COPA DO REI',
             '15X SUPERCOPA DA ESPANHA',
             '5X SUPERCOPA DA UEFA',
             '4X RECOPA EUROPEIA',
             '3X COPA EVA DUARTE',
             '2X COPA DA LIGA'],
        'idolos_lista':
            ['LIONEL MESSI',
             'RONALDINHO GAÚCHO',
             'JOHAN CRUYFF',
             'XAVI HERNANDEZ',
             'ANDRÉS INIESTA',
             'LUIS SUÁREZ',
             'SERGIO BUSQUETS',
             'NEYMAR DOS SANTOS',
             'PEP GUARDIOLA'],
        'videos_galeria': [
            'https://www.youtube.com/embed/4JiX52LIEIU', #CHAMPIONS 2014/15
            'https://www.youtube.com/embed/nGa5Xq2nk6s', # CHAMPIONS 2010/11
            'https://www.youtube.com/embed/qBR-ycKq9hQ', # CHAMPIONS 2008/09
            'https://www.youtube.com/embed/dghDh1Nnkzo', # VIRADA HISTÓRICA
            'https://www.youtube.com/embed/cEgU7DSAAEg', # CHAMPIONS 2005/06
            'https://www.youtube.com/embed/UYPu3rMvcDs', # MUNDIAL CONTRA O SANTOS
            'https://www.youtube.com/embed/eB03Abwwtro', # MUNDIAL CONTRA O RIVER PLATE
            'https://www.youtube.com/embed/UJKaqiS637M', # PRIMEIRA CHAMPIONS DA HISTÓRIA
            'https://www.youtube.com/embed/BEqS6IloSLY', # PRIMEIRO MUNDIAL DE CLUBES DA FIFA DA HISTÓRIA
            'https://www.youtube.com/embed/70m1eDF7aSM', # BARCELONA VIRA CONTRA O BENFICA
            ],
        'imagens_galeria': [ # Exemplo, adicione os nomes dos seus arquivos de imagem
            'barcelona_galeria_1.jpg',
            'barcelona_galeria_2.jpg'
        ]
    },
    'corinthians': {
        'id': 'corinthians',
        'nome': 'CORINTHIANS',
        'cor_principal': '#000000', # Preto
        'cor_secundaria': '#FFFFFF', # Branco
        'logo_url': 'escudo_corinthians.png',
        'parallax_img': 'paralax.jpg', # CONFIRMAR: Esta imagem deve existir em static/
        'titulos_importantes':
            ['2x MUNDIAL DE CLUBES DA FIFA',
             '1X COPA LIBERTADORES DA AMÉRICA',
             '7x CAMPEONATO BRASILEIRO',
             '1X RECOPA SUL-AMERICANA',
             '3X COPA DO BRASIL',
             '1X SUPERCOPA DO BRASIL',
             '1X CAMPEONATO BRASILEIRO SÉRIE B',
             '31X CAMPEONATO PAULISTA'],
        'idolos_lista':
            ['CÁSSIO',
             'SÓCRATES',
             'RONALDO FENÔMENO',
             'MARCELINHO CARIOCA',
             'NETO',
             'RIVELLINO'],
        'videos_galeria': [ # Exemplo, adicione os seus URLs de vídeo
            'https://www.youtube.com/embed/EXEMPLO_VIDEO_CORINTHIANS_1',
            'https://www.youtube.com/embed/EXEMPLO_VIDEO_CORINTHIANS_2'
        ],
        'imagens_galeria': [ # Exemplo, adicione os nomes dos seus arquivos de imagem
            'corinthians_galeria_1.jpg',
            'corinthians_galeria_2.jpg'
        ]
    }
}

# Página Inicial (com o formulário de escolha do time)
@app.route('/')
def home():
    return render_template('index.html')

# Processamento da escolha de time (vindo do index.html)
@app.route('/confirmar-escolha', methods=['POST'])
def confirmar_escolha():
    time_escolhido_id = request.form.get('time')

    if time_escolhido_id in dados_times:
        return redirect(url_for('home_time', time_id=time_escolhido_id))
    else:
        return redirect(url_for('home'))

# --- ROTAS PARA AS PÁGINAS DOS TIMES E SUBPÁGINAS INTERNAS ---

# Rota genérica para a página principal de um time específico (ex: /barcelona, /corinthians)
@app.route('/<string:time_id>')
def home_time(time_id):
    if time_id in dados_times:
        time_info = dados_times[time_id]
        # Renderiza o template específico do time (barcelona.html ou corinthians.html)
        return render_template(f'{time_id}.html', time_info=time_info, tipo_pagina='Início')
    return redirect(url_for('home'))

# Página de Cadastro
@app.route('/<string:time_id>/cadastro')
def cadastro(time_id):
    if time_id in dados_times:
        time_info = dados_times[time_id]
        return render_template('cadastro.html', time_info=time_info, tipo_pagina='Cadastro')
    return redirect(url_for('home'))

# Processamento do Cadastro (rota POST)
@app.route('/<string:time_id>/cadastro_post', methods=['POST'])
def cadastro_post(time_id):
    if time_id in dados_times:
        nome = request.form.get('nome')
        email = request.form.get('email')
        print(f"Cadastro recebido para {time_id}: Nome={nome}, Email={email}")
        return render_template('sucesso.html', nome=nome, email=email, time_id=time_id) # Redireciona para página de sucesso
    return redirect(url_for('home'))

# Página de sucesso do cadastro (opcional, crie um `sucesso.html`)
@app.route('/<string:time_id>/sucesso')
def sucesso(time_id):
    # Esta rota pode ser usada se você quiser ter uma página de sucesso separada.
    # No exemplo acima, eu renderizei diretamente, mas se você redirecionar aqui,
    # precisará passar os dados via query params ou session.
    # Por simplicidade, eu fiz o render_template direto no cadastro_post.
    return redirect(url_for('home_time', time_id=time_id))


# Página de Títulos
@app.route('/<string:time_id>/titulos')
def titulos(time_id):
    if time_id in dados_times:
        time_info = dados_times[time_id]
        return render_template('titulos.html', time_info=time_info, tipo_pagina='Títulos')
    return redirect(url_for('home'))

# Página de Ídolos
@app.route('/<string:time_id>/idolos')
def idolos(time_id):
    if time_id in dados_times:
        time_info = dados_times[time_id]
        return render_template('idolos.html', time_info=time_info, tipo_pagina='Ídolos')
    return redirect(url_for('home'))

# Página da Galeria
@app.route('/<string:time_id>/galeria')
def galeria(time_id):
    if time_id in dados_times:
        time_info = dados_times[time_id]
        return render_template('galeria.html', time_info=time_info, tipo_pagina='Galeria')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)