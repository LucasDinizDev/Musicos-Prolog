from pyswip import Prolog

class Musico:
    def __init__(self, nome, instrumento, banda):
        self.nome = nome
        self.instrumento = instrumento
        self.banda = banda

class BaseDadosMusicos:
    def __init__(self):
        self.prolog = Prolog()
        self.inicializar_fatos_e_regras()

    def inicializar_fatos_e_regras(self):
        fatos = [
            ("john_lennon", "guitarra", "beatles"),
            ("paul_mccartney", "baixo", "beatles"),
            ("george_harrison", "guitarra", "beatles"),
            ("ringo_starr", "bateria", "beatles"),
            ("mick_jagger", "vocal", "rolling_stones"),
            ("keith_richards", "guitarra", "rolling_stones"),
            ("charlie_watts", "bateria", "rolling_stones")
        ]

        regras = [
            "toca_instrumento(X, Instrumento, Banda) :- musico(X, Instrumento, Banda)",
            "toca_guitarra(X) :- toca_instrumento(X, guitarra, _)",
            "toca_baixo(X) :- toca_instrumento(X, baixo, _)",
            "toca_bateria(X) :- toca_instrumento(X, bateria, _)",
            "toca_vocal(X) :- toca_instrumento(X, vocal, _)"
        ]

        for fato in fatos:
            self.prolog.assertz(f"musico({fato[0]}, {fato[1]}, {fato[2]})")
            self.prolog.assertz(f"toca_instrumento({fato[0]}, {fato[1]}, {fato[2]})")

        for regra in regras:
            self.prolog.assertz(regra)

    def consultar_instrumento_banda(self, instrumento, banda):
        consulta = f"toca_instrumento(Musico, {instrumento}, {banda})"
        return list(self.prolog.query(consulta))

    def consultar_banda(self, instrumento):
        consulta = f"toca_instrumento(Musico, {instrumento}, Banda)"
        return list(self.prolog.query(consulta))

    def consultar_instrumento(self, musico):
        consulta = f"toca_instrumento({musico}, Instrumento, Banda)"
        resultados = list(self.prolog.query(consulta))

        if resultados:
            resultado = resultados[0]
            instrumento = resultado.get("Instrumento", None)
            banda = resultado.get("Banda", None)

            if instrumento is not None and banda is not None:
                return {"Instrumento": instrumento, "Banda": banda}

        return None

    def adicionar_musico(self, nome, instrumento, banda):
        self.prolog.assertz(f"musico({nome}, {instrumento}, {banda})")
        self.prolog.assertz(f"toca_instrumento({nome}, {instrumento}, {banda})")

        print(f"Músico {nome} adicionado com sucesso!")

def obter_input(msg):
    return input(msg)

def main():
    base_dados_musicos = BaseDadosMusicos()

    while True:
        print("Escolha uma opção:")
        print("1. Consultar músicos que tocam um instrumento")
        print("2. Consultar músicos de uma banda que tocam um instrumento")
        print("3. Consultar instrumento e banda de um músico")
        print("4. Adicionar novo músico, instrumento e banda")
        print("5. Sair")

        escolha = obter_input("Digite o número da opção desejada: ")

        if escolha == "1":
            instrumento = obter_input("Digite o instrumento: ")
            resultado = base_dados_musicos.consultar_banda(instrumento)
            print(f"Músicos que tocam {instrumento}: {resultado}")
        elif escolha == "2":
            instrumento = obter_input("Digite o instrumento: ")
            banda = obter_input("Digite a banda: ")
            resultado = base_dados_musicos.consultar_instrumento_banda(instrumento, banda)
            print(f"Músicos de {banda} que tocam {instrumento}: {resultado}")
        elif escolha == "3":
            musico = obter_input("Digite o nome do músico: ")
            resultado = base_dados_musicos.consultar_instrumento(musico)

            if resultado:
                print(f"{musico} toca {resultado['Instrumento']} na banda {resultado['Banda']}")
            else:
                print(f"{musico} não encontrado.")
        elif escolha == "4":
            novo_musico = obter_input("Digite o nome do novo músico: ")
            novo_instrumento = obter_input(f"Digite o instrumento tocado por {novo_musico} (guitarra/baixo/bateria/vocal): ")
            nova_banda = obter_input(f"Digite a banda de {novo_musico}: ")

            base_dados_musicos.adicionar_musico(novo_musico, novo_instrumento, nova_banda)
        elif escolha == "5":
            print("Saindo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()