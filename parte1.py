import csv


path=("C:\\Users\\Pc\\Desktop\\project\\epicode_project\\covid\\owid-covid-data.csv")
with open(path,'r')as csv_file:
    csv_reader=csv.reader(csv_file)
    data=[]
    for row in csv_reader:
        data.append(row)            #viene creata una lista di liste
n=len(data)

intestazione=data[0]
i=0
for ele in intestazione:                    #stampa gli elementi della lista in posizione 1 
    print(intestazione[i],':',str(i))    
    i=i+1
    lista=intestazione

cols_to_del = [0, 10, 11, 12,13,14,15,16,18,20,22,24,27,28,30,37,40,41,42,43,44,46,47,63,64,65,66]
#ciclo per eliminare le colonne    
for col_index in range(len(cols_to_del)):
    print('col index',col_index)
    if cols_to_del !=0:
        cols_to_del[col_index]=cols_to_del[col_index]-1
    for j in range(len(data)):
        data[j].pop(cols_to_del[col_index])
        print(data[0][0])
       
            
            
   
  
        
        
        