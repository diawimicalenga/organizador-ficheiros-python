from pathlib import Path

pasta = Path.cwd()

ficheiros = [f for f in pasta.iterdir() if f.is_file()]

print("=== ORGANIZADOR DE FICHEIROS ===")

if len(ficheiros) == 0:
    print("Não existem ficheiros na pasta.")
else:
    for ficheiro in ficheiros:
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        print("Tamanho:", ficheiro.stat().st_size, "bytes")

        if ficheiro.suffix == ".py":
            print("Tipo: Ficheiro Python")

        elif ficheiro.suffix == ".txt":
            print("Tipo: Ficheiro de Texto")

        elif ficheiro.suffix == ".csv":
            print("Tipo: Ficheiro CSV")

        print("----------------------")

    print("Total de ficheiros:", len(ficheiros))
