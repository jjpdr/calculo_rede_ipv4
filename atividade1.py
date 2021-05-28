'''
Entrada:
Número IP: 192.168.10.10
Máscara: 24
Saída:
IP da rede: 192.168.10.0
Gateway: 192.168.10.1
Broadcast: 192.168.10.255
IP’s disponíveis: 192.168.10.2 a 192.168.10.254
'''
import numpy as np

def decimal_para_binario(entrada):
    return ''.join([np.binary_repr(int(i), width=8) for i in entrada.split('.')])

def binario_para_decimal(entrada):
    numero_decimal = []
    try:
        for i in range(0, 33, 8):
            numero_decimal.append(str(int(entrada[i:i+8], 2)))
    except Exception:
        numero_decimal.append('0')
    else:
        pass
    
    return '.'.join(numero_decimal)

def calcula_mascara_decimal(mascara):
    quantidade_bits_1 = ['1' for _ in range(mascara)]
    quantidade_bits_0 = ['0' for _ in range(32-mascara)]

    return binario_para_decimal(''.join(quantidade_bits_1 + quantidade_bits_0))

def calcula_endereco_rede(ip, mascara):
    

if __name__ == '__main__':
    ip = '192.168.10.10' # 11000000 10101000 00001010 00001010
    mascara = 24

    print(aplica_mascara(ip, mascara))
    print(calcula_mascara_decimal(28))


