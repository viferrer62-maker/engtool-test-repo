def calcular_total(itens):
    total = 0
    for item in itens:
        if item['tipo'] == 'A':
            if item['ativo']:
                if item['preco'] > 0:
                    total += item['preco']
                else:
                    total += 0
            else:
                total += 0
        elif item['tipo'] == 'B':
            total += item['preco'] * 0.9
    return total
