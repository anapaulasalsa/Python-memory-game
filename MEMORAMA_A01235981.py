#Se importa el módulo random para poner de forma aleatoria las
#cartas en el tablero
import random
#El módulo sys es usado en este programa para la función exit, que cuando
#el jugador desea salir, el programa se deja de correr
import sys


#Esta función es para mostrarle las reglas
#al jugador, abre un archivo ya hecho
#y se le hace llamar en el main
def reglas():
    myFile = open('reglas.txt',encoding = 'utf8')
    datos = myFile.read()
    print(datos)
    myFile.close
    print()

#Esta función es para que el jugador elija si quiere
#que su memorama sea de figuras o de números
#Regresa la opción escogida al main, denominada 'tab'
def tema():
    print('\n')
    print('Elige el tema de tu memorama:')
    print('1. Letras')
    print('2. Figuras')
    print('3. Salir')
    tab =(input('Opción: '))
    
    while tab.isalpha() or tab == '':
        print('Opción no válida, intenta de nuevo')
        print('\n')
        input('<Enter> para continuar')
        tema()
    
    tab = int(tab)
        
    if tab == 1:
        return(tab)
    elif tab == 2:
        return(tab)
    elif tab==3:
        print('Regresa pronto!')
        sys.exit()
    else:
        print('Opción no válida, intenta de nuevo')
        print('\n')
        input('<Enter> para continuar')
        tema()
     
#En esta función se forma y se muestra el tablero ya listo para empezar a jugar
#Tiene renglones (A-F) y columnas (0-6)            
def imptab(tabtab):
    print('')
    print(' |',end='')
    for x in range(6):
        print(' ' + str(x),end='')
    print('\n','--------------')
    fila = 'A'
    for i in range(6):
        print(fila + '|',end='')
        fila = chr(ord(fila)+1)
        for j in range(6):
            print(' ' + tabtab[1][i][j],end='')
        print('',end='\n')

#En esta función se encuentra todo nuestro juego
def coord(tabtab):
    pares = 18
    intentos = 0
        

#Primero se le pide la columna y el renglon de la primera carta que quiere voltear
    while tabtab[1] != tabtab[0]:
        print('Coordenadas de 1era carta:')
        columna = (input(('Columna (Tiene que ser número): ')))
        renglon = input('Renglon (Tiene que ser letra mayus): ')
        
#Luego se comprueba de que el valor dado por el jugador si es un número y un string, respectivamente       
        while columna.isalpha() or renglon.isdigit() or len(renglon) > 1 or renglon == '' or columna == '':
            print('\n' ,' Valores de coordenada incorrectos',end='\n')
            columna = (input(('Columna (Tiene que ser número): ')))
            renglon = input('Renglon (Tiene que ser letra mayus): ')
            
         
#Aquí se le resta 65 al chr de la letra dada para encontrar
#su valor númerico en el rango de 0-6
        renglon = ord(renglon) - 65
        columna = int(columna)

#Aquí se comprueba que las coordenadas dadas están dentro del rango del tablero
#Si no, se le vuelve a pedir las coordenadas
        while columna > 5 or columna < 0 or renglon > 5 or renglon < 0:
            print('\n','Coordenadas dadas están fuera del rango',end='\n')
            columna = (input(('Columna (Tiene que ser número): ')))
            renglon = input('Renglon (Tiene que ser letra mayus): ')
            while columna.isalpha() or renglon.isdigit() or len(renglon) > 1 or renglon == '' or columna == '':
                print('\n' ,' Valores de coordenada incorrectos',end='\n')
                columna = (input(('Columna (Tiene que ser número): ')))
                renglon = input('Renglon (Tiene que ser letra mayus): ')
           
            renglon = ord(renglon) - 65
            columna = int(columna)

#En caso de que el usuario escoja voltear una carta que ya volteó antes, se le volverá a pedir las coordenadas
        while tabtab[1][renglon][columna] != 'X':
            print('\n','Elige una carta que no esté volteada',end='\n')
            print('Coordenadas de 1era carta:')
            columna =(input(('Columna (Tiene que ser número): ')))
            renglon = input('Renglon (tiene que ser letra mayus): ')
            renglon = ord(renglon) - 65
            columna= int(columna)
            while columna > 5 or columna < 0 or renglon > 5 or renglon < 0:
                print('\n','Coordenadas dadas están fuera del rango')
                columna = (input(('Columna (Tiene que ser número): ')))
                renglon = input('Renglon (Tiene que ser letra mayus): ')
                renglon = ord(renglon) - 65
                columna = int(columna)        
          
#Aquí muestra la casilla que el jugador eligió voltear        
        tabtab[1][renglon][columna] = tabtab[0][renglon][columna]
        imptab(tabtab)
        
        posicion1 = tabtab[1][renglon][columna]

#Se repite el mismo proceso para la 2da carta
        print('Coordenadas de 2da carta:')
        columna2 = (input(('Columna (Tiene que ser número): ')))
        renglon2 = input('Renglon (tiene que ser letra mayus): ')

        
        while columna2.isalpha() or renglon2.isdigit() or len(renglon2) > 1 or renglon2 == '' or columna2 == '':
            print('\n',' Valores de coordenada incorrectos',end='\n')
            columna2 = (input(('Columna (Tiene que ser número): ')))
            renglon2 = input('Renglon (Tiene que ser letra mayus): ')        
        
        renglon2 = ord(renglon2) - 65
        columna2 = int(columna2)

        while columna2 > 5 or columna2 < 0 or renglon2 > 5 or renglon2 < 0:
            print('\n','Coordenadas dadas están fuera del rango')
            columna2 = (input(('Columna (Tiene que ser número): ')))
            renglon2 = input('Renglon (Tiene que ser letra mayus): ')
            while columna2.isalpha() or renglon2.isdigit() or len(renglon2) > 1 or renglon2 == '' or columna2 == '':
                print('\n' ,' Valores de coordenada incorrectos',end='\n')
                columna2 = (input(('Columna (Tiene que ser número): ')))
                renglon2 = input('Renglon (Tiene que ser letra mayus): ')
           
            
            renglon2 = ord(renglon2) - 65
            columna2 = int(columna2)
            
        while tabtab[1][renglon2][columna2] != 'X':
            print('\n','Elige una carta que no esté volteada',end='\n')
            print('Coordenadas de 2da carta:')
            
            columna2 =(input(('Columna (Tiene que ser número): ')))
            renglon2 = input('Renglon (tiene que ser letra mayus): ')
            renglon2 = ord(renglon2) - 65
            columna2= int(columna2)         
            while columna2 > 5 or columna2 < 0 or renglon2 > 5 or renglon2 < 0:
                print('\n','Coordenadas dadas están fuera del rango')
                columna2 = (input(('Columna (Tiene que ser número): ')))
                renglon2 = input('Renglon (Tiene que ser letra mayus): ')
                renglon2 = ord(renglon2) - 65
                columna2 = int(columna2)        
          

      
    
#Se voltea la segunda carta
        tabtab[1][renglon2][columna2] = tabtab[0][renglon2][columna2]
        imptab(tabtab)
        
        posicion2 = tabtab[1][renglon2][columna2]
        
        intentos += 1
        
        while intentos % 3 == 0:
            continuar = input('¿Quieres seguir jugando? (si/no): ')
            if continuar == '' or continuar.isdigit():
                print('Opción no válida, intente de nuevo')
                continuar = input('¿Quieres seguir jugando? (si/no): ')
            elif continuar == 'si':
                break
            elif continuar == 'no':
                print('\n')
                print('Gracias por jugar!! Fue un gusto')
                sys.exit()
            else:
                print('Opción no válida, intente de nuevo')
                continuar = input('¿Quieres seguir jugando? (si/no): ')
                
            

#Si las dos cartas volteadas no son las mismas, las vuelve a voltear
#Si las cartas eran las mismas, se quedan volteadas y te dice cuantas parejas
#le quedan por encontrar        
        if posicion1 != posicion2:
            tabtab[1][renglon][columna] = ('X')
            tabtab[1][renglon2][columna2] = ('X')
            print('\n','Inténtalo de nuevo')
            print('Intentos: ',intentos,end='\n')
        else:
            pares = pares - 1
            print('Excelente!',pares, 'pares por encontrar')
            print('Intentos: ',intentos)
            
            #Se vuelve a repetir el proceso

#Cuando ya se encontraron todas, te dice cuantos intentos necesitaste
# y te da la opción de volver al inicio o salir del juego
        
    print ('Necesitaste ', intentos, ' intentos para ganar, felicidades!')
    print('\n')
    print('Gracias por jugar, regresa pronto!')
    sys.exit()
                
    return (coord(tabtab))

def main():
    k = 0
    tablero = []
    #Tabtab representa la lista en donde se almacenará el tablero para mostrar
    tabtab = []
    #Los dos tableros (letras y figuras) están en su respectivo carácter, en la función del tablero se les cambia a su string
    #Se multiplica por 2 para tener sus parejas y se barajean aleatoriamente
    letras = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114]
    tablero1 = letras * 2
    random.shuffle(tablero1)
    
    figuras= [9827,9824,9787,9734,9688,9675,8889,8779,9838,9670,10047,8486,9786,10226,8661,9673,8646,9791]
    tablero2 = figuras* 2
    random.shuffle(tablero2)
    
    print('MEMORAMA'.center(50))
    print(('Autor: ' + miNombreCompleto).center(50))
    print(('Matricula: ' + miMatricula).center(50))
    print('')
    print('Opciones')
    print('1. Reglas del juego')
    print('2. Empieza juego')
    print('0. Salir')
    opcion = (input('Opción: '))
    
    #Primero, se debe de comprobar que la opcion que da el jugador
    #sea un número, y en caso de que sea un string, le de la opción
    #de hacerlo de nuevo
    
    while opcion.isalpha() or opcion == '':
        print('Opción no válida, intenta de nuevo')
        print('\n')
        input('<Enter> para continuar')
        main()
    
    opcion = int(opcion)
        
    if opcion == 0:
            pass
    else:
        if opcion == 1:
            reglas()
            input('<Enter> para regresar')
            main()
        elif opcion == 2:
            print('\n','Empezando partida...')
            
#Aquí se la hace llamar a la función en donde se elige el tema del memorama
            temajuego = tema()
            
            if temajuego == 1:
                tablero = tablero1
            else:
                tablero = tablero2
            
            
 #Aquí se forma el tablero (6x6) antes de voltear alguna carta
            for i in range(2):
                tabtab.append([])
                for j in range (6):
                    tabtab[i].append([])
                    for k in range(6):
                        tabtab[i][j].append('X')
#Aquí se forma el tablero acomodando nuestra lista de figuras o letras aleatoriamente
                    
            k = 0
            for i in range(6):
                for j in range(6):
                    tabtab[0][i][j] = chr(tablero[k])
                    k = k+1

#Aquí hacemos llamar a las funciones que nos muestran el tablero y hacen funcionar el juego
            imptab(tabtab)
            coord(tabtab)
            print('Gracias por jugar, regresa pronto!')
            sys.exit()
        
        else:     
            print('Opción no válida, intenta de nuevo')
            print('\n')
            input('<Enter> para continuar')
            main()
            
miNombreCompleto = 'Ana Paula Salas Bonilla'
miMatricula = 'A01235981'

if __name__ == '__main__':
    main()

