#MultiHash versão 0.1

#Um simples programa para calcular
#as checksums de múltiplos arquivos

#Autor: Bruno Marques Sales
#E-mail: sales.bruno.marques@gmail.com
#Local: Natal, RN, Brasil.

#bibliotecas necessárias
from hashlib import sha512, md5
from pathlib import Path
from datetime import datetime

#função para gerar uma lista com os nomes de todos os arquivos do diretório
def get_file_list(str_path="."):
  p = Path(str_path)
  list_of_files = []
  for child in p.iterdir():
    if (not child.is_dir()) and (not child.suffix.startswith(".py")):
      name_of_file = child.name
      list_of_files.append(name_of_file)
  return list_of_files

#função para calcular os hashes de uma lista de arquivos
def calculate_hash(list_of_files):
  report = []
  i = 1
  for file_name in list_of_files:
    print("Calculando hashes... Arquivo " + str(i) + " de " + str(len(list_of_files)))
    #abre o arquivo, faz a leitura em binário e fecha
    opened_file = open(file_name, 'rb')
    read_file = opened_file.read()
    opened_file.close()
    #------------------------------------------------

    #instancia os objetos para cálculo dos hashes
    sha512_hash = sha512()
    md5_hash = md5()
    #--------------------------------------------

    #calcula os hashes
    sha512_hash.update(read_file)
    md5_hash.update(read_file)
    #----------------------------

    #gera a string do hash em hexadecimal
    file_sha512_hash = sha512_hash.hexdigest()
    file_md5_hash = md5_hash.hexdigest()
    #-------------------------------------

    #prepara uma lista com os resultados
    result = [file_name, file_sha512_hash, file_md5_hash]
    
    #armazena o resultado para o arquivo atual em uma "lista-relatório"
    report.append(result)

    i += 1
  return report

#função para salvar o relatório de hashes em um arquivo texto
def save_report(report):
  #gerando o nome do arquivo de saída no formato report_DD-MM-YYYY_HH-MM-SS
  date_and_time = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
  report_file_name = "report_" + date_and_time + ".txt"
  #------------------------------------------------------------------------
  
  #abrindo o arquivo
  #(como o nome depende da hora atual, o arquivo provavelmente será criado)
  report_file = open(report_file_name, "a")
  for line in report:
    report_file.write("Nome do arquivo: " + line[0] + "\n")
    report_file.write("SHA-512: " + line[1] + "\n")
    report_file.write("MD5: " + line[2] + "\n")
    report_file.write("\n")
  report_file.close()

#função para gerar o relatório com uma única chamada
def generate_report():
  save_report(calculate_hash(get_file_list()))