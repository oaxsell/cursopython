"""
Filtros customizados para prefixos de cluster.
Localização: filter_plugins/cluster_filters.py
"""

from ansible.errors import AnsibleFilterError

def proximo_prefixo(self, prefixo_atual, numero_cluster, prefixo_por_tipo):
    # Se prefixo vazio ou None, retorna 'a'
    if not prefixo_atual:
        return prefixo_por_tipo
    
    # Validar prefixo
    if not isinstance(prefixo_atual, str):
        raise AnsibleFilterError(f"Prefixo inválido: '{prefixo_atual}'")
    
    # Validar número do cluster
    numero = int(numero_cluster)
    
    # Se número < 99, mantém o prefixo
    if numero < 99:
        return prefixo_atual
    
    # Se número == 99, incrementa
    return self.incrementar_prefixo(prefixo_atual)

def incrementar_prefixo(self, prefixo):
    # Validar prefixo
    if not prefixo or not isinstance(prefixo, str):
        raise AnsibleFilterError(f"Prefixo inválido: '{prefixo}'")
    
    # Validar apenas letras minúsculas
    if not prefixo.islower() or not prefixo.isalpha():
        raise AnsibleFilterError(f"Prefixo deve conter apenas letras minúsculas: '{prefixo}'")
    
    # Converter para lista de caracteres
    chars = list(prefixo)
    
    # Incrementar da direita para esquerda (como números)
    for i in range(len(chars) - 1, -1, -1):
        if chars[i] != 'z':
            # Incrementa o caractere atual
            chars[i] = chr(ord(chars[i]) + 1)
            return ''.join(chars)
        else:
            # Se é 'z', vira 'a' e continua o "carry"
            chars[i] = 'a'
    
    # Se chegou aqui, todos eram 'z' (ex: zz → aaa)
    return 'a' + ''.join(chars)

class FilterModule(object):
    def filters(self):
        return {
            'proximo_prefixo': self.proximo_prefixo,
            'incrementar_prefixo': self.incrementar_prefixo,
        }