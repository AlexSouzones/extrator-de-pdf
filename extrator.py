import os
from datetime import datetime
import planilha
import fitz
import terminal


hora_atual = datetime.now()
hora_atual = hora_atual.strftime("%H:%M")


def verificar_projeto(arquivo):
    doc = fitz.open(arquivo)  # Abre o arquivo PDF
    text = ""
    for pagina in doc.pages():
        text += pagina.get_text()
    text.replace("\n", " ").replace("  ", " ")
    if "Resumo de indicadores" in text and "Total de alunos no projeto" in text:
        return True
    return False
  

def verificar_caminho(caminho):
  if os.path.exists(caminho):
      return (True, f"{hora_atual} - A pasta foi confirmada para")
  return (False, f"{hora_atual} - A pasta não existe para")


def catalogar_projetos(caminho):
    arquivos_corretos = []
    if os.path.isdir(caminho):
      arquivos = os.listdir(caminho)
      for arquivo in arquivos:
        if verificar_projeto(f"{caminho}/{arquivo}"):
          arquivos_corretos.append(f"{caminho}/{arquivo}")
    return arquivos_corretos


def carregar_projetos(caminhos, label):
  qtd_projetos = len(caminhos)
  pjt_atual = 0
  for caminho in caminhos:
    pjt_atual += 1
    doc = fitz.open(caminho)  # Abre o arquivo PDF
    text = ""
    for pagina in doc.pages():
        text += pagina.get_text()
    terminal.app_logs(f"extraindo: {pjt_atual}/{qtd_projetos}", label)
    extrair_info(text)


def extrair_info(texto):

  
  dados_projeto = texto[texto.find("DADOS DO PROJETO DISCENTE")+len('DADOS DO PROJETO DISCENTE'):texto.find('LOCAL, DATA E HORÁRIO:')]
  projeto = dados_projeto[dados_projeto.find('NOME DO PROJETO:')+len('NOME DO PROJETO:'):dados_projeto.find('OBJETIVO:')].replace("\n", " ").replace("  ", " ").strip()
  texto = texto.replace("\n", " ").replace("  ", " ")
  quantidade_de_alunos = texto[texto.find('Total de alunos no projeto')+len('Total de alunos no projeto'):texto.find('Número de assessoramentos com o professor')].strip()
  

  assessoramentos = texto[
    texto.find('Número de assessoramentos com o professor')+
    len('Número de assessoramentos com o professor'):
    texto.find('Número total de atividades/eventos/ações realizados')
    ].strip()
  
 
  atividades_realizadas = texto[
    texto.find('Número total de atividades/eventos/ações realizados')+
    len('Número total de atividades/eventos/ações realizados'):
    texto.find('Número entidades/grupos beneficiadas')
    ].strip()
  
  entidades_grupos_beneficiados = texto[
    texto.find('Número entidades/grupos beneficiadas') +
    len('Número entidades/grupos beneficiadas'):
    texto.find("""Número total de público em todas as atividades/eventos/ações realizadas""")
    ].strip()
  
  publico_total = texto[
    texto.find('Número total de público em todas as atividades/eventos/ações realizadas')+
    len('Número total de público em todas as atividades/eventos/ações realizadas'):
    texto.find("""Número total de atendimentos/consultorias/abordagens em todas as atividades/eventos/ações realizadas""")
    ].strip()
  
  numero_atendimentos = texto[
    texto.find("""Número total de atendimentos/consultorias/abordagens em todas as atividades/eventos/ações realizadas""")+
    len("""Número total de atendimentos/consultorias/abordagens em todas as atividades/eventos/ações realizadas"""):
    texto.find("""Houve parceria com profissionais fora da instituição?""")
    ].strip()
  
  parcerias_profi_fora = texto[
    texto.find("""Houve parceria com profissionais fora da instituição? Se sim, com quantos?""")+
    len("""Houve parceria com profissionais fora da instituição? Se sim, com quantos?"""):
    texto.find("""Houve parceria com empresas ou entidades privadas? Se sim, com quantos?""")
    ].strip()
  
  if texto.find("""Houve parceria com profissionais fora da instituição? Se sim, com quantos?""") == -1:
     parcerias_profi_fora = texto[
    texto.find("""Houve parceria com profissionais fora da instituição? Se sim, com quantos?""")+
    len("""Houve parceria com profissionais fora da instituição? Se sim, com quantos?"""):
    texto.find("""Houve parceria com empresas ou entidades privadas? Se sim, com quantos?""")
    ].strip()
  
  parcerias_empresas_entidades = texto[
    texto.find("""Houve parceria com empresas ou entidades privadas? Se sim, com quantos?""")+
    len("""Houve parceria com empresas ou entidades privadas? Se sim, com quantos?"""):
    texto.find("""Houve parceria com setor público? Se sim, com quantos?""")
    ].strip()

  parceria_setor_publico = texto[
    texto.find("""Houve parceria com setor público? Se sim, com quantos?""")+
    len("""Houve parceria com setor público? Se sim, com quantos?"""):
    texto.find("""Houve parceria com 3º setor? Se sim, com quantos?""")
    ].strip()
  
  parceria_terceiro_setor = texto[
    texto.find("""Houve parceria com 3º setor? Se sim, com quantos?""")+
    len("""Houve parceria com 3º setor? Se sim, com quantos?"""):
    texto.find("""Houve produção de material didático? Se sim, quantos?""")
    ].strip()
  
  material_didatico = texto[
    texto.find("""Houve produção de material didático? Se sim, quantos?""")+
    len("""Houve produção de material didático? Se sim, quantos?"""):
    texto.find("""Houve arrecadação de donativos? Se sim, quantos?""")
    ].strip()
  
  arrecadacao_donativos = texto[
    texto.find("""Houve arrecadação de donativos? Se sim, quantos?""")+
    len("""Houve arrecadação de donativos? Se sim, quantos?"""):
    texto.find("""Houve arrecadação de donativos? Se sim, quantos?""")+
    len("""Houve arrecadação de donativos? Se sim, quantos?""")+
    4
    ].strip().replace("\n", "")
  
  # print(f"{projeto}\n{quantidade_de_alunos}\n{assessoramentos}\n{atividades_realizadas}\n{entidades_grupos_beneficiados}\n{publico_total}\n"
  #       f"{numero_atendimentos}\n{parcerias_profi_fora}\n{parcerias_empresas_entidades}\n{parceria_setor_publico}\n{parceria_terceiro_setor}\n"
  #       f"{material_didatico}\n{arrecadacao_donativos}")
  planilha.preencher_planilha(projeto, quantidade_de_alunos, assessoramentos, atividades_realizadas, entidades_grupos_beneficiados, publico_total, 
                              numero_atendimentos, parcerias_profi_fora, parcerias_empresas_entidades, parceria_setor_publico, parceria_terceiro_setor,
                              material_didatico, arrecadacao_donativos)
