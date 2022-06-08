import csv
import json
import os


class GenerateFile():
    def __init__(self) -> None:
        pass

    def checar_diretorio(self, dir_name):
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)

    def apend_file_csv(self, path, conteudo, mode='a', fields=None):
        dir = './temp'
        self.checar_diretorio(dir)

        if fields == None:
            fields = conteudo[0].keys()

        has_file = os.path.isfile(path)
        with open(path, mode, encoding='utf-8', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields, delimiter=';')
            if not has_file or mode != 'a':
                writer.writeheader()
            writer.writerows(conteudo)

    def apend_file_json(self, path, conteudo, mode=None):
        dir = './temp'
        self.checar_diretorio(dir)

        if mode == None:
            mode = 'r+' if os.path.isfile(path) else 'a'

        with open(path, mode, encoding='utf-8') as file:
            if mode == 'r+':
                try:
                    file_data = json.load(file)
                    for d in conteudo:
                        file_data.append(d)
                    file.seek(0)
                    json.dump(file_data, file, indent=4, ensure_ascii=False)
                except:
                    input(
                        'Erro ao ler o arquivo, por favor apague o arquivo no diretório e tente novamente, pressione enter para continuar...')
            else:
                json.dump(conteudo, file, indent=4, ensure_ascii=False)
