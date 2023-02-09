from tkinter import Tk, Label, PhotoImage

# Crear la ventana
root = Tk()


# Crear una etiqueta para mostrar las coordenadas del ratón
label = Label(root, text="")
label.pack()


# Ajusta el tamaño y el color de la etiqueta
label.config(font=("OCRB", 8), fg="red")


# Cargar la imagen de fondo
image = PhotoImage(file="2.png")

label2 = Label(root, text="")
label2.pack()

# Asignar la imagen de fondo a la etiqueta y mostrarla en la ventana
label2.config(image=image)
label2.pack()

# Actualizar la etiqueta cada vez que se mueve el ratón
def update_label():
    x, y = root.winfo_pointerxy()
    label["text"] = f"Coordenadas del ratón: {x}, {y}"
    root.after(10, update_label)

update_label()
root.mainloop()
