def exibir_dados(*maria, **jose):
    print("Argumentos posicionais (maria):", maria)
    print("Argumentos nomeados (jose):", jose)
    print("-" * 40)


exibir_dados(10, 20, nome="Alice", idade=30)
exibir_dados(20, 10,  idade=30, nome="Alice")
exibir_dados("Python", linguagem="programação", versao=3.9)
exibir_dados(1, 2, 3, cidade="São Paulo", pais="Brasil")
exibir_dados()
exibir_dados(42, resposta="A vida, o universo e tudo mais")
exibir_dados("Teste", valor=100, ativo=True)

