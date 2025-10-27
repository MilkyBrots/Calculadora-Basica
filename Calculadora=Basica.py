from decimal import Decimal, getcontext, InvalidOperation
import tkinter as tk
from tkinter import messagebox

getcontext().prec = 1000

# Variables
def calcular(operacion):
    try:
        num1_text = entry_num1.get().strip()
        num2_text = entry_num2.get().strip()

        if num1_text == "" or num2_text == "":
            messagebox.showerror("Error", "Debe ingresar ambos números.")
            return

        num1 = Decimal(num1_text)
        num2 = Decimal(num2_text)

        # Operaciones basicas
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir entre cero.")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "Operación no válida.")
            return

        label_resultado.config(text=f"Resultado: {resultado}")

    except InvalidOperation:
        messagebox.showerror("Error", "Por favor ingresa números válidos (enteros o decimales).")


#Interfaz
ventana = tk.Tk()
ventana.title("Calculadora Decimal")
ventana.geometry("300x320")
ventana.config(bg="#f5f5f5")

tk.Label(ventana, text="Primer número:", bg="#f5f5f5", font=("Arial", 10)).pack(pady=5)
entry_num1 = tk.Entry(ventana, font=("Arial", 10))
entry_num1.pack()

tk.Label(ventana, text="Segundo número:", bg="#f5f5f5", font=("Arial", 10)).pack(pady=5)
entry_num2 = tk.Entry(ventana, font=("Arial", 10))
entry_num2.pack()

tk.Button(ventana, text="➕ Sumar", width=15, command=lambda: calcular("suma")).pack(pady=5)
tk.Button(ventana, text="➖ Restar", width=15, command=lambda: calcular("resta")).pack(pady=5)
tk.Button(ventana, text="✖ Multiplicar", width=15, command=lambda: calcular("multiplicacion")).pack(pady=5)
tk.Button(ventana, text="➗ Dividir", width=15, command=lambda: calcular("division")).pack(pady=5)

label_resultado = tk.Label(ventana, text="Resultado: ", bg="#f5f5f5", font=("Arial", 12, "bold"))
label_resultado.pack(pady=15)

ventana.mainloop()
