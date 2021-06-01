# João Pedro Marcelino de Sousa
# 2021

from numpy import binary_repr as representacao_binaria
from time import sleep

def decimal_para_binario(entrada):
    return ''.join([representacao_binaria(int(i), width=8) for i in entrada.split('.')])
        
def binario_para_decimal(entrada):
    numero_decimal = []
    try:
        for i in range(0, 33, 8):
            numero_decimal.append(str(int(entrada[i:i+8], 2)))
    except ValueError:
        numero_decimal.append('0')
    else:
        pass
    
    return '.'.join(numero_decimal[0:4])

def calcula_mascara_decimal(mascara):
    quantidade_bits_1 = ['1' for _ in range(mascara)]
    quantidade_bits_0 = ['0' for _ in range(32-mascara)]
    
    return binario_para_decimal(''.join(quantidade_bits_1 + quantidade_bits_0))

def calcula_endereco_rede(ip, mascara):
    bits_rede = ''.join([ip[i] for i in range(0, mascara)])
    bits_zero = ''.join(['0' for _ in range(32-mascara)])        
    
    return binario_para_decimal(bits_rede + bits_zero)


def calcula_ip(ip_rede, mascara): #ip_rede = ip da rede decimal, mascara = int
    ip_rede_binario = decimal_para_binario(ip_rede)[:mascara]
    
    bits_ip_gateway = ''.join(['0' if i != 31 else '1' for i in range(mascara, 32)])
    bits_primeiro_ip_disponivel = ''.join(['0' if i != 30 else '1' for i in range(mascara, 32)])
    bits_ultimo_ip_disponivel = ''.join(['1' if i != 31 else '0' for i in range(mascara, 32)])
    bits_ip_broadcast = ''.join(['1' for _ in range(mascara, 32)])

    ip_gateway = binario_para_decimal(ip_rede_binario + bits_ip_gateway)
    primeiro_ip_disponivel = binario_para_decimal(ip_rede_binario + bits_primeiro_ip_disponivel)
    ultimo_ip_disponivel = binario_para_decimal(ip_rede_binario + bits_ultimo_ip_disponivel)
    ip_broadcast = binario_para_decimal(ip_rede_binario + bits_ip_broadcast)

    return ip_gateway, primeiro_ip_disponivel, ultimo_ip_disponivel, ip_broadcast

def verificar_entrada(ip, mascara):
    try:
        if all(int(octeto) <= 255 and int(octeto) >= 0 for octeto in ip.split('.')) and mascara >= 1 and mascara <= 32:
            return True
    
    except Exception:
        pass
    
    print('Entrada(s) inválida(s)!\nTerminando o programa...')
    sleep(1)
    exit()

def mostrar_resultados(ip, mascara): #ip é o input decimal (string), máscara é o input decimal (int)
    ip_binario = decimal_para_binario(ip)
    mascara_decimal = calcula_mascara_decimal(mascara)
    endereco_rede_decimal = calcula_endereco_rede(ip_binario, mascara)
    ip_gateway, primeiro_ip, ultimo_ip, ip_broadcast = calcula_ip(endereco_rede_decimal, mascara)

    print('\n***DADOS DE ENTRADA***')
    print('# Número IP: {}'.format(ip))
    print('# Máscara: {}\n'.format(mascara))

    print('***RESULTADOS***')
    print('# IP da rede: {}'.format(endereco_rede_decimal))
    print('# Gateway: {}'.format(ip_gateway))
    print('# Broadcast: {}'.format(ip_broadcast))
    print('# IPs disponíveis: {} a {}\n'.format(primeiro_ip, ultimo_ip))
    

if __name__ == '__main__':
    # ip = input('Endereço de IP: ')
    # mascara = int(input('Máscara: '))

    ip = '192.168.10.10'
    mascara = 24

    if verificar_entrada(ip, mascara):
        mostrar_resultados(ip, mascara)
