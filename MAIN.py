from tkinter import *
import CONFIGURACIÓN
import UTILIDADES


ventana = Tk()
ventana.configure(bg="black")   
ventana.geometry(f'{CONFIGURACIÓN.ANCHO}x{CONFIGURACIÓN.ALTO}')  #
ventana.title("Juego Buscaminas")  
ventana.resizable(False, False)  


marco_superior = Frame(
    ventana,
    bg='black',
    width=CONFIGURACIÓN.ANCHO,
    height=UTILIDADES.altura_pct(25)  
)
marco_superior.place(x=0, y=0)


marco_izquierdo = Frame(
    ventana,
    bg='black',
    width=UTILIDADES.ancho_pct(25),   
    height=UTILIDADES.altura_pct(75)  
)
marco_izquierdo.place(x=0, y=UTILIDADES.altura_pct(25))


marco_central = Frame(
    ventana,
    bg='black',
    width=UTILIDADES.ancho_pct(75),   
    height=UTILIDADES.altura_pct(75)  
)
marco_central.place(
    x=UTILIDADES.ancho_pct(25),       
    y=UTILIDADES.altura_pct(25),      
)

ventana.mainloop()