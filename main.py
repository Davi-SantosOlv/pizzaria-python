#Imprimir um cardápio com pizzas e bebidas (as pizzas terão preço diferente de acordo com o tamanho)

#Fazer um pedido

#Guardar os dados dos produtos

cardapio = {
  'Pizza de Pepperoni': {
    'id':1,
    'preco':62
  },
  'Pizza Portuguesa': {
    'id':2,
    'preco':65
  },
  'Pizza Quatro Queijos': {
    'id':3,
    'preco':60
  },
  'Pizza Margherita': {
    'id':4,
    'preco':62
  },
  'Refrigerante 2L': {
    'id':5,
    'preco':10
  },
  'Suco Natural': {
    'id':6,
    'preco':13
  },
  'Taça de Vinho': {
    'id':7,
    'preco':21
  }
}

pedido = {
  'total':0,
  'itens':{}
}

def print_cardapio():
  print("___ CARDÁPIO ___")
  for item, info in cardapio.items():
    print(f"[{info.get('id')}] {item}: R${info.get('preco'):.2f}")
  print()

def fazer_pedido():
  produto = receber_int("Digite o número do produto que quer adicionar: ")
  qtd = receber_int("Digite a quantidade do produto: ")

  for item, info in cardapio.items():
    id = info.get('id')
    preco = info.get('preco')
    
    if not produto == id:
      continue
      
    if item in pedido.get('itens'):
      pedido['itens'][item] += qtd
    else:
      pedido['itens'][item] = qtd
    
    pedido['total'] += preco * qtd
    print("Produto adicionado")
    print()
    return

  print("Produto não encontrado")
  print()
  
def receber_int(string):
  while True:
      num = input(string)
  
      if not num.isdigit():
        print("Digite um número")
        continue
  
      num = int(num)
  
      if num <= 0:
        print("Digite um número maior ou igual a 1")
        continue
  
      return num

def print_pedido():
  for item in pedido.get('itens'):
    print(f"{item} - QTD: {pedido['itens'][item]}")
  print(f"TOTAL: R${pedido.get('total'):.2f}")
  print()

def main():
  while True:
    print("*** PIZZARIA ***")
    print("[A] Visualizar cardápio")
    print("[B] Fazer pedido")
    print("[C] Ver pedido")
    print("[D] Sair")
    opcao = input("Digite uma opção: ").lower()
    print()

    match (opcao):
      case 'a':
        print_cardapio()
      case 'b':
        fazer_pedido()
      case 'c':
        print_pedido()
      case 'd':
        break
      case _ :
        print("Opção inválida. Digite novamente")

if __name__ == '__main__':
  main()