import csv
lista=[]
def maxim(lista):
    for x in lista:
        maximo=max(int(x["Porcentaje"]) for x in lista)
        print ("porcentaje mas alto: ", maximo)
def promedio(lista):
    acumula=0
    elementos=len(lista)
    for x in lista:
        acumula=int(x["Porcentaje"])+acumula
        prom=acumula/elementos
    print ("Promedio: ",prom)
while True:
    print (" Menu")
    print ("")
    print ("1 - Agregar plan ")
    print ("2 - Listar planes ")
    print ("3 - Eliminar plan por ID")
    print ("4- Generar bbdd")
    print ("5 - Cargar bbdd")
    print ("6 - Estadísticas")
    print ("0 - Salir")

    op=int(input("Ingrese una opcion: "))
    if op==1:
           print("")
           print ("Agregar plan")
           print("")
           idplan=int(input("Ingrese ID de PLan: "))
           nombre=input("Ingrese Nombre de Plan: ")
           porcentaje=int(input("Ingrese Porcentaje de efectvidad: "))
           if porcentaje==100:
               categoria=("Esclavitud")
           if porcentaje >=0 and porcentaje<=25:
                       categoria=("Chiste")
           if porcentaje >=26 and porcentaje<=50:
                       categoria=("Anectoda")
           if porcentaje >=51 and porcentaje<=75:
                           categoria=("Peligro")
           if porcentaje >=76 and porcentaje<=99:
               categoria=("Atencion")
  
                                   
           while porcentaje <=0 and pocentaje>=100:
                    print ("Porcentaje Fuera de rango")
                    porcentaje=int(input("Ingrese Porcentaje de efectvidad nuevamente: "))
        
           
           diccionario={"ID":idplan, "Nombre":nombre, "Porcentaje":porcentaje, "Categoria":categoria}
           lista.append(diccionario)
           
    elif op==2:
        print ("")
        print ("    Lista de Planes")
        print ("")
        for x in lista:
            print ("ID: ", x["ID"], "Nombre:", x["Nombre"], "Porcentaje: ", x["Porcentaje"], "Categoria :", x["Categoria"])
    elif op==3:
        
        print ("")
        print ("Eliminar Usuario")
        print ("")
        ide=int(input("Ingrese id a eliminar"))
        for x in lista:
                
                if ide==x:
                    print ("¿desea eliminar el plan?")
                    print ("1 - eliminar")
                    print ("2 - No eliminar")
                    op=int(input("ingrese una opcion"))
                    if op==1:
                               lista.remove(x)
                    elif op==2:
                               print ("volviendo al menu")
                               break
    elif op==4:
        with open ('listaplanes.csv','w',newline='') as listita:
            escritor_csv=csv.writer(listita)
            escritor_csv.writerows(lista)
            print ("se ha generado la bbdd")
    elif op==5:
        with open ('listaplanes.csv','r',newline='') as listita:
            lector_csv=csv.reader(listita)
            for i in lector_csv:
                lista.append(i)
            print ("bbdd cargada")

    elif op==6:
        promedio(lista)
        maxim(lista) 
        
    
        
        
                           
                    
               
            
           
           
