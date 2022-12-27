import csv 
from csv import reader
import zipfile
from datetime import datetime
import os




route_extraction = 'C:/Users/mgarr/Downloads/temp'
rutas = 'C:/Users/mgarr/Downloads/'
def unzip(path):
    files=os.listdir(path)
    try:
        for file in files:
            if file.endswith('.zip'): 
                filePath=rutas+'/'+file
                zip_file = zipfile.ZipFile(filePath)
                for names in zip_file.namelist():
                    zip_file.extract(names,route_extraction)
                zip_file.close() 
    except FileNotFoundError:
        print("ARCHIVO NO ENCONTRADO")
unzip(rutas)
routes = 'C:/Users/mgarr/Downloads/temp/Optical_Power_Management_2022-11-30_17-24-32_DST.csv'
route = 'C:/Users/mgarr/Downloads/temp/'

csvFiles = []
for file in os.listdir(route):
        if file.endswith(".csv"):
            result =os.path.join(route, file)
            csvFiles.append(result)
            
if len(csvFiles)==0:
    print('Archivo CSV No encontrados')

try:
    for i in csvFiles:
        list = []
        with open(i) as f:
            reader = csv.reader(f)
            for row in reader:
                list.append(row)

        #rescato texto fila A columna 4
        date = list[3]
        #convierto a String 
        dateToString = "".join(date)
        #obtengo subcadenas según posición obteniendo fecha
        extract = dateToString[10:]
        extractDate = extract[:20]
        #print(extractDate)

        div2 = extractDate.split(" ")
        date_ = div2[1:2]
        hour = div2[2:3]

        convertToStringDate = "".join(date_)
        divDate = convertToStringDate.split("-")
        year ="".join(divDate[:1])
        month = "".join(divDate[1:2])
        day = "".join(divDate[2:3])
        extractHour = "".join(div2[2:3])
        delete = extractHour.split(":")
        toStringDelete = "".join(delete)

        dateFinal = year+month+day+toStringDelete



        for indice in range(10,len(list)):

            #-------CITY--------------------
            fileA = list[indice][0]
            separator = fileA.split(",")
            # Tenemos la lista (COLUMNA 'A')
            name = separator[0:1]
            #convierto la lista en string
            convertToString = "".join(name)
            #extraigo texto antes del "-"
            toArray = convertToString.split("-")
            city = toArray[0]
            #print(city)

            #-------SHELF0--------------------
            fileB = list[indice][1]
            #convertimos a string
            toStringShelf = "".join(fileB)
            #seleccionamos texto entes de "("
            divShelf = toStringShelf.split("(")
            #seleccionamos contenido en posicion
            resultShelf = divShelf[0]
            #print(resultShelf)


            idShelf = list[indice][1:2]
            toStringShelf = "".join(idShelf)
            divShelf=toStringShelf.split("-")
            id =divShelf[1]
            #print(id)

            #----------PORT------------------------
            port = list[indice][3]
            portToString = "".join(port)
            #convierto a array
            toArrayPort = portToString.split("(")
            #rescato id en posición 0
            port = toArrayPort[0]
            toStringPort = "".join(port)
            #print(toStringPort)

            #-----------SLOT ----------------------
            slot = "Slot"
        #-----------SLOT ----------------------
            port = "Port"

            nodo = city+"-"+resultShelf+"-"+slot+id+"-"+port+toStringPort
            #print(nodo)

            def process(numPosition):
                position = list[indice][numPosition]+"\n"
                textToString = "".join(position)
                replaceText = textToString.replace("/","None")
                textSpace = "".join(replaceText).replace('"','').split()
                textToString2= "".join(textSpace)
                return textToString2

            inputP = process(4) #--------------INPUT POWER------------------
            ri = process(5)  #-------------REFERENCE INPUT-----------------
            ipr = process(6) #--------------INPUT POWER REFERENCE-----------
            ipState = process(7) #--------------INPUT POWER STATE-----------
            ripl = process(8) #-------------REFERENCE INPUT POWER LOWER
            ripU = process(9) #-------------REFERENCE INPUT POWER UPPER
            iplT = process(10) #-------------INPUT POWER LOWER THRESHOLD
            minpl = process(11) #--------------MIN.VALUE OF INPUT POWER LOWER
            miplt = process(12) #--------------MAX VALUE OF INPUT POWER LOWER THRESCHOLD
            iput = process(13) #---------------INPUT POWER UPPER THRESHOLD
            miput = process(14) #---------------MIN VALUE OF INPUT POWER UPPER THRESHOLD
            maxIput = process(15) #---------------MAX VALUE OF INPUT POWER UPPER THRESHOLD
            maxPop = process(16) #---------------MAX PUMP OUTPUT POWER
            minPop = process(17) #---------------MIN PUMP OUTPUT POWER
            OutP = process(18) #---------------OUTPUT POWER--------------------
            rOP = process(19) #---------------REFERENCE OUTPUT POWER
            oPRVT = process(20) #---------------OUTPUT POWER REFERENCE VALUE TIME
            ops = process(21) #---------------OUTPUT POWER STATE
            oplt = process(22) #---------------OUTPUT POWER LOWER THRESHOLD
            oput = process(23) #---------------OUTPUT POWER UPPER THRESHOLD
            roplt = process(24) #---------------REFERENCE OUTPUT POWER LOWER THRESHOLD
            roput = process(25) #--------------REFERENCE OUTPUT POWER UPPER THRESCHOLD
            ipltd = process(26) #--------------INPUT POWER LOWER THRESHOLD DEFAULT
            iputd = process(27) #--------------INPUT POWER UPPER THRESHOLD DEFAULT
            CFPLaneIPL = process(28) #--------------CFP/LANE INPUT POWER LOWER THRESHOLD DEFAULT VALUE
            CFPULT = process(29) #--------------CFP/LANE INPUT POWER LOWER THRESHOLD DEFAULT VALUE

            docFinal = dateFinal+"|"+nodo+"|"+inputP+"|"+ri+"|"+ipr+"|"+ipState+"|"+ripl+"|"+ripU+"|"+iplT+"|"+minpl+"|"+miplt+"|"+iput+"|"+miput+"|"+maxIput+"|"+maxPop+"|"+minPop+"|"+OutP+"|"+rOP+"|"+oPRVT+"|"+ops+"|"+oplt+"|"+oput+"|"+roplt+"|"+roput+"|"+ipltd+"|"+iputd+"|"+CFPLaneIPL+"|"+CFPULT+"\n"
            toStringf = "".join(docFinal)

            #print(toStringf)
            with open("C:/Users/mgarr/OneDrive/Escritorio/indexes/nce_"+dateFinal+".txt", 'a+') as f:
                for i in toStringf:
                    f.write(i) 
except FileNotFoundError:
    msg = 'Archivos CSV no Encontrados'
    print(msg)