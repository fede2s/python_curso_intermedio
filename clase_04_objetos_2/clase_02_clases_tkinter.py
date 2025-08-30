from tkinter import *

class BotonB:
    def __init__(self, parent = None, *args, **kwargs) -> None:
        self.root=parent
        self.root.geometry("300x300")
        b1=Button(self.root, *args, **kwargs)
        b1.pack(side=LEFT)
        b1.config(command=self.callback)

    def callback(self, ):
        print("Chau")
        self.root.quit()

class MiBoton(BotonB):

    def callback(self,):
        print("estoy en mi boton")
        self.root.quit()
    
if __name__=="__main__":
    root = Tk()
    mi_app = BotonB(root, text="Hola botón")
    mi_app_2 = MiBoton(root, text="Mi boton")
    root.mainloop()