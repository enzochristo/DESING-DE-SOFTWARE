def compromisso_no_periodo(horarios,dia,periodo):
    for hora in range(len(horarios)):
        if hora == periodo:
            for days in range(len(horarios[hora])):
                if days == dia:
                  if horarios[hora][days] == '':
                    return 'Livre'
                  else:
                    return horarios[hora][days]

            
print(compromisso_no_periodo([['GDE', 'Tópicos', 'NatDes', 'Tópicos', ''], ['DesSoft', 'GDE', 'DesSoft', 'InstruMed', 'NatDes'], ['ModSim', '', '', '', ''], ['', 'ModSim', '', 'ModSim', 'InstruMed']],1,0))

def compromisso_no_periodo(horarios,dia,periodo):
   i = 0 
   days = 0
   while i < len(horarios):
    if periodo >=1:
      i += 1
    if i == periodo:
         while days < len(horarios[0]):
            if dia >=1:
             days += 1
            if days == dia:
               if horarios[periodo][days] == '':
                  return 'Livre'
               else:
                return horarios[periodo][days]
            

print(compromisso_no_periodo([['GDE', 'Tópicos', 'NatDes', 'Tópicos', ''], ['DesSoft', 'GDE', 'DesSoft', 'InstruMed', 'NatDes'], ['ModSim', '', '', '', ''], ['', 'ModSim', '', 'ModSim', 'InstruMed']],1,0))
