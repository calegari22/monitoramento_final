import csv
from datetime import datetime

def coletar_eventos():
    eventos = []

    eventos.append(("Login Inválido", datetime.now(), "Tentativa de login com senha incorreta"))
    eventos.append(("Execução Suspeita", datetime.now(), "Script desconhecido executado"))
    eventos.append(("Arquivo Modificado", datetime.now(), "Alteração no arquivo /etc/passwd"))

    with open("logs_coletados.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Tipo", "Data", "Descrição"])
        for e in eventos:
            writer.writerow(e)

if __name__ == "__main__":
    coletar_eventos()
    print("Logs coletados e salvos com sucesso!")
