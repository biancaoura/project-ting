import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def create_file_dict(path_file: str):
    file = txt_importer(path_file)
    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    return dict_file


def process(path_file: str, instance: Queue):
    if path_file not in instance.queue:
        instance.enqueue(path_file)
        dict_file = create_file_dict(path_file)
        print(dict_file, file=sys.stdout)


def remove(instance: Queue):
    if not len(instance):
        print("Não há elementos", file=sys.stdout)
        return

    file_path = instance.dequeue()
    print(f"Arquivo {file_path} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position: str):
    try:
        path_file = instance.search(position)
        dict_file = create_file_dict(path_file)
        print(dict_file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
