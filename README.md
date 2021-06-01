# Cálculo de redes no padrão IPv4

Tem como entrada um endereço de rede e uma máscara (as entradas são tratadas para evitar erros)

Tem um output do seguinte formato:

***DADOS DE ENTRADA***
# Número IP: X.X.X.X
# Máscara: X

***RESULTADOS***
# IP da rede: X.X.X.X
# Gateway: X.X.X.X
# Broadcast: X.X.X.X
# IPs disponíveis: X.X.X.X a X.X.X.X

Para esse programa, o endereço do gateway é sempre o primeiro IP disponível e o Broadcast o último ip disponível, os demais IPs são o intervalo dos dois.
