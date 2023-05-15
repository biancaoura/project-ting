import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    if path_file not in instance.queue:
        file = txt_importer(path_file)
        instance.enqueue(path_file)
        dict_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
        print(dict_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
