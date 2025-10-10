# filter_plugins/cluster_filters.py
def proximo_indice(indice_atual, alphabet):
    """
    Calcula o próximo índice alfabético
    a -> b, b -> c, ..., z -> aa, aa -> ab, ..., az -> ba
    """
    if not indice_atual or indice_atual == '':
        return 'a'
    
    if indice_atual == 'z':
        return 'aa'
    
    # Índices simples (a-y)
    if len(indice_atual) == 1 and indice_atual in alphabet:
        idx = alphabet.index(indice_atual)
        return alphabet[idx + 1]
    
    # Índices duplos (aa-zz) - para expansão futura
    if len(indice_atual) == 2:
        first, second = indice_atual[0], indice_atual[1]
        if second != 'z':
            return first + alphabet[alphabet.index(second) + 1]
        else:
            return alphabet[alphabet.index(first) + 1] + 'a'
    
    return 'a'  # fallback

class FilterModule:
    def filters(self):
        return {'proximo_indice': proximo_indice}