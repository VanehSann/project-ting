def exists_word(word, instance):
    final_result = []
    for index in range(len(instance)):
        file = instance.search(index)
        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        line = 0
        for index in file["linhas_do_arquivo"]:
            line += 1
            if word.lower() in index.lower():
                result["ocorrencias"].append({"linha": line})

        if result["ocorrencias"]:
            final_result.append(result)
    return final_result


def search_by_word(word, instance):
    final_result = []
    for index in range(len(instance)):
        file = instance.search(index)
        pre_result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        line = 0
        for index in file["linhas_do_arquivo"]:
            line += 1
            if word.lower() in index.lower():
                pre_result["ocorrencias"].append(
                    {"linha": line, "conteudo": index}
                )

        if pre_result["ocorrencias"]:
            final_result.append(pre_result)
    return final_result
