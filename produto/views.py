
from django.shortcuts import render, redirect
from .models import Produto, Categoria, Opcoes, Adicional

def home(request):
    # Inicializa o carrinho na sessão, se não existir
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    # Busca todos os produtos e categorias no banco de dados
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    carrinho_count = len(request.session['carrinho'])

    # Renderiza a página inicial com os dados necessários
    return render(request, 'home.html', {
        'produtos': produtos,
        'categorias': categorias,
        'carrinho': carrinho_count
    })

def categorias(request, id):
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {
        'produtos': produtos,
        'carrinho': len(request.session['carrinho']),
        'categorias': categorias,
    })

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()

    return render(request, 'produto.html', {
        'produto': produto,
        'carrinho': len(request.session['carrinho']),
        'categorias': categorias,
        'erro': erro
    })



def add_carrinho(request):
    # Inicializa o carrinho na sessão se não existir
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)

    # Função para remover itens indesejados do dicionário
    def removeLixo(adicionais):
        adicionais = adicionais.copy()
        for chave in ['id', 'csrfmiddlewaretoken', 'observacoes', 'quantidade']:
            adicionais.pop(chave, None)
        return list(adicionais.items())

    adicionais = removeLixo(x)    

    id = int(x.get('id', ['0'])[0])
    produto = Produto.objects.filter(id=id).first()
    if not produto:
        return redirect(f'/produto/{id}?erro=produto_nao_encontrado')

    preco_total = produto.preco
    adicionais_verifica = Adicional.objects.filter(produto_id=id)
    aprovado = True

    # Verifica se os adicionais atendem os critérios de mínimo e máximo
    for adicional in adicionais_verifica:
        encontrou = False
        minimo = adicional.minimo
        maximo = adicional.maximo
        for nome, valores in adicionais:
            if adicional.nome == nome:
                encontrou = True
                if len(valores) < minimo or len(valores) > maximo:
                    aprovado = False
        if minimo > 0 and not encontrou:
            aprovado = False

    if not aprovado:
        return redirect(f'/produto/{id}?erro=1')

    # Otimização: Busca todas as opções de uma vez só
    opcoes_ids = [int(k) for _, j in adicionais for k in j]
    opcoes = {op.id: op.acrescimo for op in Opcoes.objects.filter(id__in=opcoes_ids)}

    for _, j in adicionais:
        for k in j:
            preco_total += opcoes.get(int(k), 0)

    # Troca IDs por nomes
    def troca_id_por_nome_adicional(adicionais):
        opcoes_nomes = {op.id: op.nome for op in Opcoes.objects.filter(id__in=opcoes_ids)}
        return [(i[0], [opcoes_nomes.get(int(j), "Desconhecido") for j in i[1]]) for i in adicionais]

    adicionais = troca_id_por_nome_adicional(adicionais)

    # Calcula o preço total considerando a quantidade
    preco_total *= int(x.get('quantidade', ['1'])[0])

    # Cria os dados do carrinho
    data = {
        'id_produto': id,
        'observacoes': x.get('observacoes', [''])[0],
        'preco': preco_total,
        'adicionais': adicionais,
        'quantidade': int(x.get('quantidade', ['1'])[0])
    }

    # Adiciona ao carrinho e salva na sessão
    request.session['carrinho'].append(data)
    request.session.save()

    return redirect('/ver_carrinho')


def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_motrar = []
    for i in request.session['carrinho']:
        prod = Produto.objects.filter(id=i['id_produto'])
        dados_motrar.append(
            {'imagem': prod[0].img.url,
             'nome': prod[0].nome_produto,
             'quantidade': i['quantidade'],
             'preco': i['preco'],
             'id': i['id_produto']
             }
        )
    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'carrinho.html', {
        'dados': dados_motrar,
        'total': total,
        'carrinho': len(request.session['carrinho']),
        'categorias': categorias,
    
    })

def remover_carrinho(request, id):
    request.session['carrinho'].pop(id)
    request.session.save()
    return redirect('/ver_carrinho')
