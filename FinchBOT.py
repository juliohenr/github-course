#auhauh
# coding: utf-8
#oi
# # Data Set Treinamento
#oi
# In[1]:


dataset = [{'pattern': 'Você mora em um condomínio com vaga de garagem?',
  'id': 'PERGUNTA 1.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 2.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 1.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'ESSE BOT NÃO PODE TE AJUDAR', 'id': 'PERGUNTA 1.2'},
 {'pattern': 'Você tem uma dívida?',
  'id': 'PERGUNTA 2.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 3.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 3.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Você tem dinheiro para pagar a dívida?',
  'id': 'PERGUNTA 3.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 4.2.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 4.2.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Seu marido ou mulher tem uma dívida?',
  'id': 'PERGUNTA 3.2',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 3.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 4.1.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Você tem dinheiro para pagar a dívida? (RETORNO - 3.2)',
  'id': 'PERGUNTA 4.1.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 3.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 4.1.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Você pretende fazer um testamento?',
  'id': 'PERGUNTA 4.1.2',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 5.1.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 5.1.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'PROCURE UM ADVOGADO', 'id': 'PERGUNTA 4.2.1'},
 {'pattern': 'Você sabe o que é um bem de família?',
  'id': 'PERGUNTA 4.2.2',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 8.2.3'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 5.2.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Você sabe quem pode ser seu herdeiro?',
  'id': 'PERGUNTA 5.1.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 6.1.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 6.1.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'ESSE BOT NÃO PODE TE AJUDAR', 'id': 'PERGUNTA 5.1.2'},
 {'pattern': 'Você sabe se a matrícula da vaga é separada da matrícula do imóvel?',
  'id': 'PERGUNTA 5.2.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 6.2.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 6.2.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Bem de família é uma proteção que o direito brasileiro oferece a alguns bens tidos como essenciais  para que estes não possam ser penhorados. O imóvel de residência não pode ser penhorado, por ser, justamente, um bem de família.',
  'id': 'PERGUNTA 5.2.2',
  'response': {'Redirecionamento': {'redirect_id': 'PERGUNTA 7.1.2'}}},
 {'pattern': 'Na elaboração de um testamento, é importante ter em mente que a separação da vaga de garagem na matrícula da residência pode resultar no afastamento da proteção do bem de família da vaga.',
  'id': 'PERGUNTA 6.1.1',
  'response': {'redirecionamento': {'redirect_id': 'PERGUNTA 4.2.2'}}},
 {'pattern': 'Seus herdeiros são divididos em duas categorias: os legítimos e os testamentários. Os legítimos são aqueles determinados por lei, como os filhos. 50% da herança deve ser destinada a eles. A outra metade pode ser destinada a quem você quiser.',
  'id': 'PERGUNTA 6.1.2',
  'response': {'redirecionamento': {'redirect_id': 'PERGUNTA 6.1.1'}}},
 {'pattern': 'É separada?',
  'id': 'PERGUNTA 6.2.1',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 7.1.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 8.2.4'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Você está com a sua matrícula aí?',
  'id': 'PERGUNTA 6.2.2',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 7.2.1'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 7.2.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Sua vaga provavelmente não é considerada um bem de família. Recomendo que você procure um advogado: ele poderá te ajudar melhor!',
  'id': 'PERGUNTA 7.1.1'},
 {'pattern': 'Você sabe o que é uma execução?',
  'id': 'PERGUNTA 7.1.2',
  'response': {'AFIRMATIVO': {'redirect_id': 'PERGUNTA 8.2.3'},
   'NEGATIVO': {'redirect_id': 'PERGUNTA 8.2.2'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Verifique se na sua escritura há alguma indicação de que a vaga e o imóvel não são a mesma coisa, ou se toda a propriedade é tratada de maneira uniforme.',
  'id': 'PERGUNTA 7.2.1',
  'response': {'REDIRECIONAMENTO': {'redirect_id': 'PERGUNTA 6.2.1'}}},
 {'pattern': 'Recomendo que você procure um advogado: ele poderá te ajudar melhor!',
  'id': 'PERGUNTA 7.2.2'},
 {'pattern': 'Se você acha que pode ser executado, recomendo que você procure um advogado: ele poderá te ajudar melhor! Não esqueça de falar sobre a separação (ou não) da sua vaga na matrícula do imóvel.',
  'id': 'PERGUNTA 8.2.1'},
 {'pattern': 'Execução é o processo para cobrar uma dívida por meio do Poder Judiciário. Nessa etapa, a justiça pode vender propriedades da pessoa para angariar o dinheiro devido e sanar a dívida. Caso essa propriedade seja um bem de família, ela está protegida e não pode ser vendida. Recomendo que você procure um advogado: ele poderá te ajudar melhor!',
  'id': 'PERGUNTA 8.2.2',
  'response': {'Redirecionamento': {'redirect_id': 'PERGUNTA 8.2.3'}}},
 {'pattern': 'Vamos conferir se sua vaga é um bem de família.',
  'id': 'PERGUNTA 8.2.3',
  'response': {'Redirecionamento': {'redirect_id': 'PERGUNTA 5.2.1'}}},
 {'pattern': 'sua vaga é um bem de família.', 'id': 'PERGUNTA 8.2.4'},
 {'pattern': 'Desculpe-me, mas eu não entendi, você pode me responder com outras palavras?',
  'id': 'FORA DO CHECKLIST',
  'response': {'AFIRMATIVO': {'redirect_id': 'generico'},
   'NEGATIVO': {'redirect_id': 'NEGATIVO FORA DO CHECKLIST'}},
  'classes': {'AFIRMATIVO': ['Sim',
    'Uhum',
    'Com certeza',
    'Acho que sim',
    'Claro',
    'Lógico',
    'Pode ser',
    'Yes',
    'Claro que sim',
    'Lógico que sim',
    'Óbvio',
    'Óbvio que sim',
    'Na verdade sim',
    'Evidente',
    'Sim!',
    'Uhum!',
    'Com certeza!',
    'Acho que sim!',
    'Claro!',
    'Lógico!',
    'Pode ser!',
    'Yes!',
    'Claro que sim!',
    'Lógico que sim!',
    'Óbvio!',
    'Óbvio que sim!',
    'Na verdade sim!',
    'Evidente!',
    'S',
    'S!'],
   'NEGATIVO': ['Não',
    'Nope',
    'Nunca',
    'Claro que não',
    'No',
    'Óbvio que não',
    'Lógico que não',
    'Na verdade não',
    'Pode ser que não',
    'Não!',
    'Nope!',
    'Nunca!',
    'Claro que não!',
    'No!',
    'Óbvio que não!',
    'Lógico que não!',
    'Na verdade não!',
    'Pode ser que não!',
    'N',
    'Não faço ideia',
    'Acho que não',
    'N!',
    'Não faço ideia!',
    'Acho que não!']}},
 {'pattern': 'Okay, deixa pra próxima ;D', 'id': 'NEGATIVO FORA DO CHECKLIST'}]


# In[2]:


dataset=str(dataset)


# In[3]:


dataset=dataset.replace("'",'"')


# In[4]:


dataset


# # Class Finch Bot

# In[2]:


class FinchBot:
    
    def __init__(self):
        
        self.first_interaction = True
        self.current_question = None
        self.last_id = None
        self.pattern = None
        self.classes = None
        self.label2 = None
    
    def fit(self,dataset = None,respostaPadrao=None):
        
        import numpy as np
        import pickle
        from keras.preprocessing.text import Tokenizer
        from sklearn.feature_extraction.text import TfidfVectorizer
        from keras.models import Sequential
        from keras.layers import Dense
        from keras.utils import np_utils

              
        self.dataset=dataset
        
        
        def json_reader(dataset):

            import numpy as np

            amostras=[]
            perguntas=[]
            perguntasAssociadas=[]
            label=[]
            label2_reduzido=[]
            classes=[]
            cont=0

            for i in range(0,len(dataset)):
                
                if len(dataset[i])>3:

                    if 'response' in dataset[i]:

                        classes_temp = list(dataset[i]['classes'].keys())

                        cont2=0

                        amostras_temp=[]

                        for k in classes_temp:

                            amostras=amostras+dataset[i]['classes'][k]

                            amostras_temp=amostras_temp+dataset[i]['classes'][k]

                            label=label+(cont*np.ones(len(dataset[i]['classes'][k]))).tolist()

                            label2_reduzido.append(cont2)

                            cont+=1
                            cont2+=1

                        perguntas.append(dataset[i]['pattern'])


                        if len(classes_temp)>len(classes):

                            classes = classes_temp

                        for j in range(0,len(amostras_temp)):

                            perguntasAssociadas.append(dataset[i]['pattern'])

            return amostras,label,perguntas,perguntasAssociadas,classes,label2_reduzido

        def remove_acents_caracteres(file):

            import unicodedata

            for i in range(0,len(file)):

                for j in file[i]:

                    if j in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':

                        file[i]=file[i].replace(j,'')

                file[i]= unicodedata.normalize('NFKD',file[i]).encode('ASCII', 'ignore')
                file[i]=file[i].decode("utf-8")
                file[i]=file[i].lower()
                file[i]=file[i].replace(' ','')

            return file

        samples,label,questions,questions_vector,self.classes,self.label2=json_reader(self.dataset)
        
        #samples,label,questions,questions_vector = json_reader(dataset)
   
        vectorizer = TfidfVectorizer()
        vectorizer.fit_transform(questions)
        questions_vector=vectorizer.transform(questions_vector).toarray()
        questions_transformed=vectorizer.transform(questions).toarray()
        samples=remove_acents_caracteres(samples)

        tok = Tokenizer(num_words=len(samples))
        tok.fit_on_texts(samples) 

        with open('vectorizer.pickle', 'wb') as handle:
            pickle.dump(vectorizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # saving
        with open('tokenizer.pickle', 'wb') as handle:
            pickle.dump(tok, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        samples=tokenizer.texts_to_matrix(samples,mode='binary')

        x_train=np.concatenate((questions_vector,samples),axis=1)
        y_train = label
        num_classes = (np_utils.to_categorical(y_train)).shape[1]
        y_train=np_utils.to_categorical(y_train)

        model = Sequential()
        model.add(Dense(50, input_dim=x_train.shape[1], activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        model.fit(x_train,y_train, epochs=10, batch_size=10)
        # evaluate the model
        scores = model.evaluate(x_train, y_train)
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        
        model.save('my_model.h5') 
        
        #print('SCORE: {}'.format(RF.score(x_train,y_train)))
        
    
    def request(self, response = None):
        
        import pickle
        import numpy as np
        from keras.models import load_model
        
        def remove_acents_caracteres(file):

            import unicodedata

            for i in range(0,len(file)):

                for j in file[i]:

                    if j in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':

                        file[i]=file[i].replace(j,'')

                file[i]= unicodedata.normalize('NFKD',file[i]).encode('ASCII', 'ignore')
                file[i]=file[i].decode("utf-8")
                file[i]=file[i].lower()
                file[i]=file[i].replace(' ','')

            return file
        

        if self.first_interaction:
            self.current_question = dataset[0]
            self.pattern = self.current_question['pattern']
            self.last_id = self.current_question['id']
            self.first_interaction = False
            
        else:
         
            model = load_model('my_model.h5')
            
            with open('tokenizer.pickle', 'rb') as handle:
                
                tokenizer = pickle.load(handle)
                
            with open('vectorizer.pickle', 'rb') as handle:
                
                vectorizer = pickle.load(handle)
                
            
            self.pattern = self.current_question['pattern']
            
            file2 = remove_acents_caracteres([response])
            
            file1=tokenizer.texts_to_matrix(file2,mode='binary')
            
            question_transformed=vectorizer.transform([self.pattern]).toarray()
            
            amostra=np.concatenate((question_transformed,file1),axis=1)
            
            a=model.predict(amostra)
            
            a=np.argmax(a)
            
            key=self.classes[self.label2[int(a)]] 
            
            checkListConfirmed = False
            
            if 'classes' in self.current_question:

                for i in self.current_question['classes'][key]:

                    i2=remove_acents_caracteres([i])


                    if i2[0]==file2[0]:

                        checkListConfirmed = True

                        print("RESPOSTA: {}".format(key))

                        break
                    
            
            #-----------------------------------------------------
            #Interpreta padrão de resposta pela IA de similaridade
            #-----------------------------------------------------
            # Sim, é isso ai, exato.... equivale a 1
            # Não, não sou, e etc .... equivale a 0
            
            
            #if response == 'sim':
             #   print('resposta: sim')
              #  key = "yes"
            #elif response == "não":
             #   print('resposta: não')
              #  key = "no"
            #else:
             #   return "Desculpe não posso te ajudar :("
            #----------------------------------------------------- 
            
            
            if checkListConfirmed == True or not 'classes' in self.current_question:
            
                if 'response' in self.current_question:

                    if len(self.current_question['response'])>1:

                        redirect_id = self.current_question['response'][key]['redirect_id']
                        self.last_id = redirect_id
                        

                        search_redirect_question = list(filter(lambda question : question['id'] == self.last_id, self.dataset))


                        if search_redirect_question:

                            search_redirect_question = search_redirect_question[0]
                            self.current_question = search_redirect_question
                            self.pattern = search_redirect_question['pattern']
                            self.last_id = search_redirect_question['id']
                            self.first_interaction = False

                    else:

                        key = list(self.current_question['response'].keys())
                        key=key[0]
                        redirect_id = self.current_question['response'][key]['redirect_id']
                        self.last_id = redirect_id

                        search_redirect_question = list(filter(lambda question : question['id'] == self.last_id, self.dataset))


                        if search_redirect_question:

                            search_redirect_question = search_redirect_question[0]
                            self.current_question = search_redirect_question
                            self.pattern = search_redirect_question['pattern']
                            self.last_id = search_redirect_question['id']
                            self.first_interaction = False

                else:

                    return self.pattern
                
            else:
                    
                
                search_redirect_question = list(filter(lambda question : question['id']== "FORA DO CHECKLIST", self.dataset))
                

                if search_redirect_question:
                    

                    search_redirect_question = search_redirect_question[0]
                    
                    for jj in search_redirect_question['response'].keys():
                        
                        if search_redirect_question['response'][jj]['redirect_id']=='generico':
                            
                            search_redirect_question['response'][jj]['redirect_id']=self.last_id
                    
                    self.current_question = search_redirect_question
                    self.pattern = search_redirect_question['pattern']
                    self.last_id = search_redirect_question['id']
                    self.first_interaction = False 
        
                    
        return self.pattern


# # Treinar Bot

# In[3]:


finchBot = FinchBot()


# In[4]:


finchBot.fit(dataset)


# # Interagir com Bot

# ### O Bot irá devolver retornar uma pergunta padrão para iniciar o diálogo

# In[5]:


finchBot.request()


# ### A partir disso, ocorre o diálogo

# In[11]:


responder = "s"
finchBot.request(responder)


# In[12]:


responder = "nnjjn"
finchBot.request(responder)

