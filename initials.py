full_name= [str(name) for name in input("Введите ФИО: ", ).split()]
def initials(full_name):
    n1=tuple(full_name[0])
    n2=tuple(full_name[1])
    n3=tuple(full_name[2])
    return(print('Инициалы: ',n1[0]+'.',n2[0]+'.',n3[0]+'.'))

initials(full_name)