import ollama 
from flask import Flask,request

app = Flask(__name__)

@app.route("/customizarPergunta",methods=["POST"])
def pergunta():
    try:
        body = request.json
        perfil = body['perfil']
        pergunta = body['pergunta']
        res = ollama.chat(model='llama3.2:1b',messages=[
            {
                'role': 'user',
                'content': "presonalize a pergunta levando em conta o perfil, não me de a resposta , apenas personalize a pergunta; \n\n"
                "Perfil: "+perfil+"\n\nPergunta: "+pergunta,
            }
        ])
        return res['message']['content']
    except Exception as e :
        print(e)
        return ""

@app.route("/verificarResposta",methods=["POST"])
def reposta():
    try:
        body = request.json
        perfil = body['perfil']
        pergunta = body['pergunta']
        resposta = body['resposta']
        res = ollama.chat(model='llama3.2:1b',messages=[
            {
                'role': 'user',
                'content': "Comente sobre a resposta dada pelo aluno; \n\n"+"\n\nPerfil: "+perfil+"\n\nPergunta: "+pergunta+"\n\n\nResposta: "+resposta,
            },
            {
                'role':'assistant',
                'content': 'Pergunta: '
            }
        ])
        return {
                "resposta":res['message']['content']
            }
    except:
        return ""

app.run(debug=True)