import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(result)
    sys.stdout.write(f"{result}\n")


def remove(instance):
    if not instance or len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    file = instance.dequeue()
    path_file = file["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(f"{instance.search(position)}\n")
    except IndexError:
        return sys.stderr.write("Posição inválida")
