from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
#------------------------------------------------------------------------------------
print ("\nPARA DETENER EL BOT Ctrl + C\n")
print ("¡¡¡¡¡ATENCION!!!!!\n")
print ("EL NOMBRE DE LA CLASE DEL HTML DE WS CAMBIA PERIODICAMENTE, SI ALGO FALLA SOLO INSPECCIONEN EL NOMBRE DEL USUARIO Y COPIEN EL NOMBRE DE LA CLASE EN LA VARIABLE 'usuario' y el 'En Linea' en la variable que esta dentro de la funcion 'validarLinea' en la variable llamada 'linea' con eso se soluciona el error de las class, mas de eso no va ocurrir.")
num = input("\n INGRESE EL NUMERO DE TELEFONO DE LA PERSONA: ")
#------------------------------------------------------------------------------------
driver = webdriver.Edge(executable_path='msedgedriver')
#------------------------------------------------------------------------------------
def validarLinea():
    try:
        linea= driver.find_element_by_class_name('zzgSd._3e6xi')
    except:
        return 1
    return 0
#------------------------------------------------------------------------------------
def validarQR():
    try:
        elemento = driver.find_element_by_tag_name("canvas")
    except:
        return False
    return True
#------------------------------------------------------------------------------------
def bot(numero):
    #------------------------------------------------------------------------------------
    driver.get("https://wa.me/{}".format(numero))
    btn = driver.find_element_by_xpath("//*[@id='action-button']").click()
    time.sleep(1)
    btn = driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a").click()
    time.sleep(5)
    #------------------------------------------------------------------------------------
    espero = True
    while espero:
        print("ESTOY ESPERANDO")
        espero = validarQR()
        time.sleep(2)
        if espero == False:
            print("SE AUTENTICO")
            break 
    time.sleep(5)
    #------------------------------------------------------------------------------------
    con = 1
    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linea = True
    usuario = driver.find_element_by_class_name('_21nHd').text
    #------------------------------------------------------------------------------------
    while linea == True:
        print("VERIFICANDO CONEXION....")
        linea1 = validarLinea()
        time.sleep(2)
        if linea1 == 0 and con <= 1:
            print("{} ESTA EN LINEA".format(usuario))
            archivo = open ("log.txt","a")
            archivo.write("{} EN LINEA {} \n".format(usuario, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            archivo.close()
            con+=1
        elif linea1 == 1 and con > 1:
            print("{} NO ESTA EN LINEA".format(usuario))
            archivo = open ("log.txt","a")
            archivo.write("DEJO DE ESTAR EN LINEA {} \n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            archivo.close()
            con-=1
    #------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------           
bot(num)
#------------------------------------------------------------------------------------