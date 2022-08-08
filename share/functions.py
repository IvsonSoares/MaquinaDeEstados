def string_in_L(string):
  """
    Verifica Se os caracteres contidos na string de entrada
    fazem parte do conjunto L
  """
  valida_char = True
  conjunto_L = ['a','b','c']
  for char in string:
    if char not in conjunto_L:
      print(f" O caracter '{char}' não Pertence ao conjunto -> {conjunto_L}")
      valida_char = False
      return valida_char
  return valida_char  

def b_count(string):
  """
    Recebe uma string de entrada e
    inicia a contagem de caracteres 'b' após o reconhecimento de
    algum caracter 'a'

    *retorna True caso para cada todos os 'a', haja pelo menos
    2 'b' consecutivos
  """
  count_b = 0
  start_count_b = False
  valid_string = False
  
  for char in string:
    if start_count_b and char == 'b':
      count_b = count_b + 1
      if count_b > 1:
        valid_string = True
      else:
        valid_string = False
      
    if char == 'a':
      count_b = 0
      start_count_b = True
      valid_string = False
      #fazer algo
      
  return valid_string

def valida_string(string):
  """
    Recebe uma string e reconhece se a mesma está
    dentro ou não do padrão esperado de um conjunto L
  """
  if string_in_L(string) and b_count(string):
    print(f"{string}: Pertence ao conjunto L")
  else:
    print(f"{string}: Não Pertence ao conjunto L")
    