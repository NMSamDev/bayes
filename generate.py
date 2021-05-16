import csv
import string
import sys
import codecs
import hashlib
import collections

# Diccionarios para contar las palabras segun su clasificacion
countP = dict()     # Positivo
countN = dict()     # Negativo
count = dict()      # Todos

# 1 es positivo
# 0 es negativo

# Cuenta las palabras segun su clasificacion
def word_count(str, clase):
    words = []
    words = str.split()
    
    for word in words:
        # Todos
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        # Positivos
        if(clase == 1):
            if word in countP:
                countP[word] += 1
            else:
                countP[word] = 1
        # Negativos
        else:
            if word in countN:
                countN[word] += 1
            else:
                countN[word] = 1

# Lectura de los datos
with open('./sentiment_labelled/amazon_cells_labelled.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')

    entrada = dict()  # Diccionario para asignar id con su respectiva palabra
    saveIn = [] # Guarda diccionario entrada en una lista
    
    w = []
    temp = ""
    posW = []
    negW = []
    pos = 0
    neg = 0

    for line in csv_reader:
        w = ''.join([i for i in line[0] if i not in string.punctuation]).lower()
        entrada["id"] = hashlib.md5(w.encode()).hexdigest()
        entrada["word"] = w
        entrada["clase"] = int(line[1])
        saveIn.append(dict(entrada))

    # Ordenamos por el id descendente para que nuestra eleccion tenga aleartoriedad
    saveIn = sorted(saveIn, key=lambda k: k['id']) 
    
    test = [] # Test
    training = [] # Training
    for i in range(0, 1000):
        if(i < 100):
            test.append(saveIn[i])
        else:
            training.append(saveIn[i])
    
    # print(len(test))
    # print(len(training))
    
    # Imprime la lista Training
    # for x in training:
    #     print(x['id'], x['clase'])

    # print(countN.keys())

    for line in training:
        w = line['word']
        word_count(w, line["clase"])
        if(line["clase"] == 1):
            posW.append(w)
            pos+=1
        else:
            negW.append(w)
            neg+=1
    
    



# Parte que aun no se usa

# with open('clasification.csv', 'w') as new_file:
#     headers = ['Palabra', 'FrecPos', 'FrecNeg', 'LogPos', 'LogNeg']
#     csv_writer = csv.DictWriter(new_file, fieldnames=headers)
#     csv_writer.writeheader()
#     for line in csv_reader:
#         newData.append({
#         # line[headers[0]]
#         }
#         )

# for line in newData:
#     csv_writer.writerow(line)

