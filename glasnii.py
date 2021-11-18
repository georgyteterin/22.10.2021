glasnii = ('а','у','е','ы','о','э','я','ё','и','ю', 'А','У','Е','Ы','О','Э','Я','Ё','И','Ю' )
soglasnii = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ')

def gl(pred):
    counter = 0
    for i in (pred):
        if i in glasnii:
            counter += 1
    return counter


def sogl(pred):
    counter = 0
    for i in (pred):
        if i in soglasnii:
            counter += 1
    return counter

pred = str(input('Введите предложение: '))
question = str(input('Хотите узнать кол-во гласных или согласных? '))
if question == 'гласных':
  print(gl(pred))
if question == 'согласных': 
  print(sogl(pred))