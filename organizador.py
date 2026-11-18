from pathlib import Path

# Define a pasta
pasta = Path(".")

# Obtém apenas ficheiros
ficheiros = [item for item in pasta.iterdir() if item.is_file()]

# Apresenta resultados
print("=== ORGANIZADOR DE FICHEIROS ===")

for ficheiro in ficheiros:
    print(ficheiro.name)

print(f"Total de ficheiros: {len(ficheiros)}")