import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

trabajadores = []
asistencias = [] 

class Trabajador:
    def __init__(self, nombre, nacimiento, puesto, sexo, grado, cedula, domicilio, telefono, correo, ingreso):
        self.datos = {
            'Nombre': nombre,
            'Fecha de nacimiento': nacimiento,
            'Puesto': puesto,
            'Sexo': sexo,
            'Grado de estudios': grado,
            'Cédula profesional': cedula,
            'Domicilio': domicilio,
            'Teléfono': telefono,
            'Correo': correo,
            'Fecha de ingreso': ingreso
        }

def ventana_registro():
    ventana = tk.Toplevel(root)
    ventana.title("Registrar trabajador")
    ventana.geometry("400x600")
    ventana.configure(bg="#E6CCFF")

    etiquetas = [
        "Nombre", "Fecha de nacimiento", "Puesto", "Sexo",
        "Grado de estudios", "Cédula profesional (Sí/No)",
        "Domicilio", "Teléfono", "Correo", "Fecha de ingreso"
    ]

    entradas = []

    for texto in etiquetas:
        tk.Label(ventana, text=texto + ":", bg="#E6CCFF", font=("Arial", 10)).pack()
        entrada = tk.Entry(ventana)
        entrada.pack()
        entradas.append(entrada)

    def guardar():
        datos = [e.get() for e in entradas]
        if not all(datos):
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return
        t = Trabajador(*datos)
        trabajadores.append(t)
        messagebox.showinfo("Guardado", "Trabajador registrado con éxito.")
        for entrada in entradas:
            entrada.delete(0, tk.END)

    tk.Button(ventana, text="Guardar trabajador", command=guardar, bg="#B266FF", fg="white").pack(pady=10)

def ventana_mostrar():
    if not trabajadores:
        messagebox.showinfo("Sin registros", "No hay trabajadores registrados.")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Lista de trabajadores")

    tree = ttk.Treeview(ventana, columns=list(trabajadores[0].datos.keys()), show="headings")

    for key in trabajadores[0].datos.keys():
        tree.heading(key, text=key)
        tree.column(key, width=120)

    for t in trabajadores:
        tree.insert("", tk.END, values=list(t.datos.values()))

    tree.pack(padx=10, pady=10, fill='x')

def ventana_asistencia():
    if not trabajadores:
        messagebox.showwarning("Sin trabajadores", "No hay trabajadores registrados para tomar asistencia.")
        return

    ventana = tk.Toplevel(root)
    ventana.title("Registro de asistencia")

    checks = []
    nombres = []

    for t in trabajadores:
        nombre = t.datos['Nombre']
        var = tk.BooleanVar()
        chk = tk.Checkbutton(ventana, text=nombre, variable=var)
        chk.pack(anchor="w")
        checks.append(var)
        nombres.append(nombre)

    def guardar_asistencia_memoria():
        registro = {}
        for i, var in enumerate(checks):
            registro[nombres[i]] = "Presente" if var.get() else "Ausente"
        asistencias.append(registro)
        messagebox.showinfo("Asistencia guardada", "La asistencia ha sido registrada en memoria.")
        ventana.destroy()

    tk.Button(ventana, text="Guardar asistencia", command=guardar_asistencia_memoria, bg="#B266FF", fg="white").pack(pady=10)

root = tk.Tk()
root.title("Panel de trabajadores")
root.geometry("700x500")
root.configure(bg="#F0E6FF")

frame_contenido = tk.Frame(root, bg="#F0E6FF")
frame_contenido.pack(side="left", fill="both", expand=True)

menu_lateral = tk.Frame(root, width=200, bg="#D9B3FF")
menu_lateral.pack(side="right", fill="y")

tk.Label(menu_lateral, text="Menú", bg="#D9B3FF", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(menu_lateral, text="Registrar trabajador", command=ventana_registro, bg="#B266FF", fg="white").pack(pady=10, fill='x', padx=10)
tk.Button(menu_lateral, text="Mostrar trabajadores", command=ventana_mostrar, bg="#B266FF", fg="white").pack(pady=10, fill='x', padx=10)
tk.Button(menu_lateral, text="Registrar asistencia", command=ventana_asistencia, bg="#B266FF", fg="white").pack(pady=10, fill='x', padx=10)

root.mainloop()
