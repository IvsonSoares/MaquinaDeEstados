def start(string):
  """
    @Node Start - Passo inicial
    1- caso a string seja diferente de 'a',
       a maquina 3 sera acionada
    2- Caso contrario, a maquina 1 sera acionada,
       para seguir o fluxo de verificacao
  """

  contador = [0]
  maquinas_de_estado = {
    'maquina_1': 1, 
    'maquina_2': 2, 
    'maquina_3': 3, 
    'maquina_4': 4
  }

  if chars_in_set(string):
    if(string[contador[0]] == 'a'):
      move_string_reader(contador)
      s_1(string, contador, maquinas_de_estado)
    else:
      move_string_reader(contador)
      s_3(string, contador, maquinas_de_estado)
  else:
    print(f"{string}: nao percente ao conjunto L")


def s_1(string, contador, maquinas_de_estado):
  """
    @Primeira maquina de estados,
    1- caso a string seja diferente de 'b',
       a maquina continua no mesmo estado
    2- caso o char na posicao x seja 'b',
       a maquina avanca para o estado 2
  """
  if final_da_string(string, contador, maquinas_de_estado['maquina_1']):
    return

  if(string[contador[0]] == 'b'):
    move_string_reader(contador)
    s_2(string, contador, maquinas_de_estado)
  else:
    move_string_reader(contador)
    s_4(string, contador, maquinas_de_estado)

def s_2(string, contador, maquinas_de_estado):
  """
    @Segunda maquina de estados,
    1- caso a string seja diferente de 'b',
       a maquina retorna para o estado 1
    2- caso o char na posicao x seja 'b',
       a maquina avanca para o estado 3
  """
  
  if final_da_string(string, contador, maquinas_de_estado['maquina_2']):
    return

  if(string[contador[0]] == 'b'):
    move_string_reader(contador)
    s_3(string, contador, maquinas_de_estado)
  else:
    move_string_reader(contador)
    s_4(string, contador, maquinas_de_estado)


def s_3(string, contador, maquinas_de_estado):
  """
    @Terceira maquina de estados,
    1- caso a string seja diferente de 'b',
       a maquina retorna para o estado 1
    2- caso o char na posicao x seja 'b',
       a maquina continua no mesmo estado   
  """
  
  if final_da_string(string, contador, maquinas_de_estado['maquina_3']):
    return

  if(string[contador[0]] != 'a'):
    move_string_reader(contador)
    #outra maquina para finalizar
    s_3(string, contador, maquinas_de_estado)
  else:
    move_string_reader(contador)
    s_1(string, contador, maquinas_de_estado)

def s_4(string, contador, maquinas_de_estado):
  """
    @Terceira maquina de estados,
    1- caso a string seja diferente de 'b',
       a maquina retorna para o estado 1
    2- caso o char na posicao x seja 'b',
       a maquina continua no mesmo estado   
  """
  
  if final_da_string(string, contador, maquinas_de_estado['maquina_4']):
    return
  
  move_string_reader(contador)
  s_4(string, contador, maquinas_de_estado)

def chars_in_set(string):
  for i in string:
    if i not in ['a', 'b', 'c']:
      return False
  return True

def final_da_string(string, contador, maquina_estado):
  final_char = False
  if contador[0] >= len(string):
    if maquina_estado == 3:
      print(f"{string}: percente ao conjunto L")
    else:
      print(f"{string}: nao percente ao conjunto L")
    final_char = True
    
  return final_char

def move_string_reader(contador):
  contador[0] = contador[0] + 1