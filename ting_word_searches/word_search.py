from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    file_path = instance.queue[0]

    text = txt_importer(file_path)
    if any(word.lower() in line.lower() for line in text):
        occurrences = [
            {"linha": i+1}
            for i, line in enumerate(text)
            if word.lower() in line.lower()
        ]

        return [{
            "palavra": word,
            "arquivo": file_path,
            "ocorrencias": occurrences
        }]
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
