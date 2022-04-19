from bottle import route, run, request
from pessoa import Pessoa, save_pessoa


@route('/pessoa', method='POST')
def salvar_pessoa():
    nome = request.forms.get('nome')
    sobrenome = request.forms.get('sobrenome')
    email = request.forms.get('email')

    pessoa_1 = Pessoa(nome, sobrenome, email)
    save_pessoa(pessoa_1)
    return 'Pessoa Inserirda com Sucesso - Nome: {} | Sobrenome: {} | E-mail: {}'.format(nome, sobrenome, email)


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)