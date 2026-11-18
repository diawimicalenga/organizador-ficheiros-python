from pathlib import Path

pasta = Path(".")

ficheiros = [item for item in pasta.iterdir() if item.is_file()]

print("=== ORGANIZADOR DE FICHEIROS ===")

for ficheiro in ficheiros:
    print(ficheiro.name)

print(f"\nTotal de ficheiros: {len(ficheiros)}")

contagem = {}

for ficheiro in ficheiros:
    extensao = ficheiro.suffix

    if extensao in contagem:
        contagem[extensao] += 1
    else:
        contagem[extensao] = 1

print("\n=== CONTAGEM POR EXTENSÃO ===")

for extensao, quantidade in contagem.items():
    print(f"{extensao}: {quantidade}")
    