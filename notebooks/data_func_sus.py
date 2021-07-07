
import pandas as pd
from datetime import date


def correcao_monetaria_ipca(valor_passado, ipca, data_passada, data_correcao):
  '''
  -------------------------------------------------------------------------
  Name: correcao monetaria
  -------------------------------------------------------------------------
  Função que busca no repositorio lfhillesheim/analise_data_sus/main/data/ipca_94-2021.csv os dados de IPCA e aplica correção monetária 
  -------------------------------------------------------------------------
  Parâmetros:
  @param valor_passado: valor na data passa
  @param ipca: tabela ipca
  @param data_passada : data passada  ano/mes
  @param data_correcao: data correcao ano/mes
  -------------------------------------------------------------------------
  Exemplo
  valor_pelo_ipca = correcao_monetaria(100, ipca, "2008/JAN", "2020/DEZ")
  '''
  
  
  i_passado = ipca.loc[data_passada][0]
  i_atual = ipca.loc[data_correcao][0]

  return  round(valor_passado * (i_atual/i_passado), 2)


def formata_uf_regiao_sus(df):
  
  
  
  regions = {"1":"Norte","2":'Nordeste',"3":'Sudeste',"4":'Sul',"5":'Centro-oeste'}
  df = df.rename(columns={"Unidade da Federação": "UF"})
  df.insert(0, 'regiao',  df.index.str.slice(0,1) ) 
  df.index = df.index.str.slice(3,)
  df = df.replace({"regiao" : regions})
  
  
  return df

def para_data(ano_mes: str):
  meses = {
  "Jan":1,
  "Fev":2,
  "Mar":3,
  "Abr":4,
  "Mai":5,
  "Jun":6,
  "Jul":7,
  "Ago":8,
  "Set":9,
  "Out":10,
  "Nov":11,
  "Dez":12,
  } 
  ano: int = int(ano_mes[:4])
  mes: str = ano_mes[5:]
  mes_numero: int = meses[mes]
  
  data = date(ano, mes_numero, 1)
  
  
  return data
