import tkinter as tk
from tkinter import ttk, messagebox

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Control de Asistencias")
        self.root.geometry("800x500")
        self.root.configure(bg="#f5e6ff")  

        encabezado = tk.Label(
            root,
            text="Bienvenido al sistema de registro de empleados",
            font=("Arial", 16, "bold"),
            bg="#b57edc",  
            fg="white",
            pady=10
        )
        encabezado.pack(fill=tk.X)

        self.main_frame = tk.Frame(root, bg="#f5e6ff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.panel_derecho = tk.Frame(self.main_frame, bg="#dab6fc", width=200)
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.panel_derecho, text="Menú", font=("Arial", 14, "bold"), bg="#dab6fc").pack(pady=20)

        boton_color = "#b57edc"
        for texto, comando in [
            ("Registro de Empleado", self.abrir_registro),
            ("Vacaciones", self.funcion_vacaciones),
            ("Historial", self.mostrar_historial)
        ]:
            tk.Button(
                self.panel_derecho,
                text=texto,
                bg=boton_color,
                fg="white",
                font=("Arial", 10, "bold"),
                width=20,
                command=comando
            ).pack(pady=10)

        tk.Button(
            self.panel_derecho,
            text="Salir",
            bg="#a266c2",
            fg="white",
            font=("Arial", 10, "bold"),
            width=20,
            command=root.quit
        ).pack(side=tk.BOTTOM, pady=20)

    def abrir_registro(self):
        nueva_ventana = tk.Toplevel(self.root)
        RegistroTrabajador(nueva_ventana)

    def mostrar_historial(self):
        try:
            with open("registro_trabajadores.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            ventana_historial = tk.Toplevel(self.root)
            ventana_historial.title("Historial de Trabajadores")
            ventana_historial.geometry("600x400")

            texto = tk.Text(ventana_historial, wrap="word", font=("Arial", 10))
            texto.insert("1.0", contenido if contenido else "No hay registros todavía.")
            texto.config(state="disabled")
            texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        except FileNotFoundError:
            messagebox.showinfo("Historial", "Aún no hay registros guardados.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al abrir el archivo: {str(e)}")

    def funcion_vacaciones(self):
        ventana_vacaciones = tk.Toplevel(self.root)
        ventana_vacaciones.title("Seleccionar Periodo Vacacional")
        ventana_vacaciones.geometry("450x250")
        ventana_vacaciones.configure(bg="#f5e6ff")
 
        tk.Label(
            ventana_vacaciones,
            text="Selecciona un periodo vacacional",
            font=("Arial", 14, "bold"),
            bg="#b57edc",
            fg="white",
            pady=10
        ).pack(fill=tk.X)

        opciones = {
            "Periodo 1 (12-feb-2024 al 23-feb-2024)": ("12-feb-2024", "23-feb-2024", "26-feb-2024"),
            "Periodo 2 (26-feb-2024 al 08-mar-2024)": ("26-feb-2024", "08-mar-2024", "11-mar-2024")
        }

        seleccion = tk.StringVar()
        combo = ttk.Combobox(ventana_vacaciones, textvariable=seleccion, values=list(opciones.keys()), state="readonly", width=40)
        combo.pack(pady=20)

        def mostrar_seleccion():
            periodo = seleccion.get()
            if periodo:
               inicio, fin, reanudar = opciones[periodo]
               messagebox.showinfo("Periodo Seleccionado", f"Has elegido:\nInicio: {inicio}\nTérmino: {fin}\nReanudando: {reanudar}")
            else:
               messagebox.showwarning("Sin selección", "Por favor, selecciona un periodo vacacional.")

        tk.Button(
            ventana_vacaciones,
            text="Seleccionar",
            bg="#b57edc",
            fg="white",
            font=("Arial", 10, "bold"),
            width=20,
            command=mostrar_seleccion
        ).pack(pady=10)

class RegistroTrabajador:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro del Trabajador")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5e6ff")

        self.campos = {
            "Nombre": tk.StringVar(),
            "Fecha de nacimiento": tk.StringVar(),
            "Tipo de contratación": tk.StringVar(),
            "Sexo": tk.StringVar(),
            "Último grado de estudio": tk.StringVar(),
            "Cédula profesional": tk.StringVar(),
            "Domicilio": tk.StringVar(),
            "Teléfono": tk.StringVar(),
            "Correo electrónico": tk.StringVar(),
            "Fecha de ingreso": tk.StringVar(),
            "Jornada": tk.StringVar()
        }

        fila = 0
        for campo, var in self.campos.items():
            tk.Label(root, text=campo + ":", bg="#f5e6ff").grid(row=fila, column=0, padx=10, pady=5, sticky="e")
            if campo == "Tipo de contratación":
                opciones = ["Basificados", "Homologados", "Regularizados", "Contrato", "Suplente"]
                entrada = ttk.Combobox(root, textvariable=var, values=opciones, state="readonly")
            elif campo == "Sexo":
                opciones = ["Masculino", "Femenino"]
                entrada = ttk.Combobox(root, textvariable=var, values=opciones, state="readonly")
            elif campo == "Jornada":
                opciones = [
                    "Matutino (7:00-2:30)",
                    "Vespertino (2:00-8:30)",
                    "Nocturno (Lun-Mie-Vie)",
                    "Nocturno (Mar-Jue-Sab)",
                    "Jornada Acumulada",
                    "Jornada Acumulada Especial",
                    "Jornada Mixta"
                ]
                entrada = ttk.Combobox(root, textvariable=var, values=opciones, state="readonly")
            else:
                entrada = tk.Entry(root, textvariable=var)
            entrada.grid(row=fila, column=1, padx=10, pady=5)
            fila += 1

        tk.Button(
            root,
            text="Guardar",
            bg="#b57edc",
            fg="white",
            font=("Arial", 10, "bold"),
            width=20,
            command=self.guardar_datos
        ).grid(row=fila, column=0, columnspan=2, pady=20)

    def guardar_datos(self):
        try:
            for campo, var in self.campos.items():
                if not var.get().strip():
                    raise ValueError(f"El campo '{campo}' no puede estar vacío.")

            with open("registro_trabajadores.txt", "a", encoding="utf-8") as archivo:
                archivo.write("=== Registro de Trabajador ===\n")
                for campo, var in self.campos.items():
                    archivo.write(f"{campo}: {var.get()}\n")
                archivo.write("\n")

            messagebox.showinfo("Éxito", "Datos guardados correctamente.")
            self.root.destroy()

        except ValueError as ve:
            messagebox.showerror("Error de validación", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
