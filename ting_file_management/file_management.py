import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            return sys.stderr.write("Formato inválido")
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

