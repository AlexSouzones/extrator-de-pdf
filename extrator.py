import os


def verificar_caminho(caminho):
  print("c", caminho)
  if os.path.exists(caminho):
      return (True, f"A pasta foi confirmada.")
  return (False, f"A pasta {caminho} não existe.")


def extrair_info(texto):

  projeto = texto[
    texto.find('Título do projeto:')+
    len('Título do projeto:'):
    texto.find('Professor responsável:')
    ]

  quantidade_de_alunos = texto[
    texto.find('Total de alunos no projeto')+
    len('Total de alunos no projeto'):
    texto.find('Número de assessoramentos com o professor')
    ].strip()

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
    texto.find("""Número total de atendimentos/consultorias/abordagens em todas as 
atividades/eventos/ações realizadas""")
    ].strip()
  
  numero_atendimentos = texto[
    texto.find("""Número total de atendimentos/consultorias/abordagens em todas as 
atividades/eventos/ações realizadas""")+
    len("""Número total de atendimentos/consultorias/abordagens em todas as 
atividades/eventos/ações realizadas"""):
    texto.find("""Houve parceria com profissionais fora da instituição? Se sim, com 
quantos?""")
    ].strip()
  
  parcerias_profi_fora = texto[
    texto.find("""Houve parceria com profissionais fora da instituição? Se sim, com 
quantos?""")+
    len("""Houve parceria com profissionais fora da instituição? Se sim, com 
quantos?"""):
    texto.find("""Houve parceria com empresas ou entidades privadas? Se sim, com 
quantos?""")
    ].strip()
  
  parcerias_empresas_entidades = texto[
    texto.find("""Houve parceria com empresas ou entidades privadas? Se sim, com 
quantos?""")+
    len("""Houve parceria com empresas ou entidades privadas? Se sim, com 
quantos?"""):
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
    texto.find("""• Execução do Projeto:""")
    ].strip()
  
  print(f"{projeto}\n{quantidade_de_alunos}\n{assessoramentos}\n{atividades_realizadas}\n{entidades_grupos_beneficiados}\n{publico_total}\n"
        f"{numero_atendimentos}\n{parcerias_profi_fora}\n{parcerias_empresas_entidades}\n{parceria_setor_publico}\n{parceria_terceiro_setor}\n"
        f"{material_didatico}\n{arrecadacao_donativos}")
  