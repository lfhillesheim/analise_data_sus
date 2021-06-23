
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
