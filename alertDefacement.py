import urllib.request
import difflib
# Sull1v4nX Ejemplo 1 .. 
site= "https://www.sull1v4nx.site/"
page2 = urllib.request.urlopen(site).read().decode()


#GGuardar la pagina en un archivo
site_cod = open("site2.txt", "w")
site_cod.write(page2)
site_cod.close()


#Comparar archivos 

site_ori = open("original.txt").readlines()
site_val = open("site2.txt").readlines()



# lineas1=site_ori.splitlines()
# lienas2=site_val.splitlines()

# diferencia =difflib.HtmlDiff()



difer=""

for line in difflib.unified_diff(site_ori,site_val):
     print (line)
     log =open("logdef.txt","a")
     log.write(line)
     difer=line
log.close()




site_ori2 = open("original.txt","r")
site_val2 = open("site2.txt","r")
site_dife2 = open("logdef.txt","r")

linea_ori=len(site_ori2.readlines())
linea_val=len(site_val2.readlines())
linea_dif=len(site_dife2.readlines())

result = ((linea_dif/2) * 100) / (linea_ori)

print ("Original= {0} \n  Evaluado {1} \n Diferencia {2}\n Percentaje {3} \n Valores {4} ".format(linea_ori,linea_val,linea_dif,result,difer))

print("fin del programa")


