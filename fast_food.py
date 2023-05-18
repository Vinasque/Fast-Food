def adicionar_pedido(numero_do_pedido, fila_de_pedidos):
    fila_de_pedidos.append(numero_do_pedido)
    print(f"Pedido {numero_do_pedido} adicionado")

def preparar_pedido(fila_de_pedidos):
    print(f"Pedido {fila_de_pedidos[0]} está pronto")
    fila_de_pedidos.remove(fila_de_pedidos[0])

def listar_pedidos_em_preparo(fila_de_pedidos):
    for pedido in fila_de_pedidos:
        print(f"Preparando {pedido}")

def verificar_pedido(numero_do_pedido, fila_de_pedidos):
    if fila_de_pedidos.count(numero_do_pedido) < 1:
        print("Pedido não existe")
    else:
        print("Seu pedido é o número", fila_de_pedidos.index(numero_do_pedido)+1, "da fila!")

pedidos_em_preparo = []

print("Digite 1 para listar pedidos.")
print("Digite 2 para adicionar um pedido.")
print("Digite 3 para preparar um pedido.")
print("Digite 4 para verificar um pedido.")
print("Digite 5 para encerrar o programa.")

while True:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        listar_pedidos_em_preparo(pedidos_em_preparo)
    elif opcao == 2:
        pedido = int(input("Digite o número do pedido: "))
        adicionar_pedido(pedido, pedidos_em_preparo)
    elif opcao == 3:
        preparar_pedido(pedidos_em_preparo)
    elif opcao == 4:
        pedido = int(input("Digite o número do pedido: "))
        verificar_pedido(pedido, pedidos_em_preparo)
    elif opcao == 5:
        print(opcao)
        break
    else:
        print("Opção incorreta. Digite outra vez.")
