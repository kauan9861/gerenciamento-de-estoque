import json

funci_programa = 1

# repeticao principal
while funci_programa == 1:

    comando_interacao = int(input("gerenciamento de estoque  |  1 - adicionar  2 - remover 3 - ver estoque 4 - fechar programa : "))

    if comando_interacao == 1:

        sair = False

        while sair == False:

            nome = input("gerenciamento de estoque  |  Digite o nome do produto: ")
            idade = int(input("gerenciamento de estoque  |  Digite o quantidade do produto: "))

            # funcao responsavel por abrir modificar e persistir os dados no Json

            def adicionar():

                # esta funcao apenas retorna a lista com os dados
                def ret_lista():
                    return {
                        "nome": nome,
                        "idade": idade
                    }

                with open("db.json", "r") as arquivo:
                    json_arquivo = json.load(arquivo)

                json_arquivo["dados"].append(ret_lista())

                with open("db.json", "w") as arquivo:
                    json.dump(json_arquivo, arquivo, indent=4)

            adicionar()

            # sistema de menu "sair ou continuar"

            comando_sair = input("deseja sair?[s/n]")

            if comando_sair == "s":
                sair = True
            else:
                sair = False

    # sistema de remocao de dados
    elif comando_interacao == 2:

        with open("db.json", "r") as arquivo1:
            dados_remover_json = json.load(arquivo1)

        dado_remover = input("gerenciamento de estoque  |  solicite o produto a ser removido : ")

        for item in dados_remover_json["dados"]:
            if item["nome"] == dado_remover:
                dados_remover_json["dados"].remove(item)

        with open("db.json", "w") as arquivo2:
            json.dump(dados_remover_json, arquivo2, indent=4)

    # apenas mostra a listaguem de estoque
    elif comando_interacao == 3:

        with open("db.json", "r") as arquivo2:
            json_lista = json.load(arquivo2)

        for item in json_lista["dados"]:
            print(item)

    elif comando_interacao == 4:
        print("programa encerrado")
        funci_programa = 0