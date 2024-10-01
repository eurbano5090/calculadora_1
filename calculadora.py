import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi calculadora")
icon_path = "C:/Users/enurb/PycharmProjects/pythonProject2/calculadora.ico"

ventana.iconbitmap(icon_path)

# variables para calcualr
expresion = ''

# variable para almacenar el estado del visor
resultado_mostrado = False


def pulsar_tecla(tecla):
    global expresion, resultado_mostrado

    if (resultado_mostrado):
        if tecla.isdigit() or tecla == ',':
            expresion = str(tecla)
        else:
            expresion += str(tecla)
        resultado_mostrado = False
    else:
        expresion += str(tecla)
    visor_texto.set(expresion)


def limpiar():
    global expresion, resultado_mostrado

    expresion = ""
    visor_texto.set(expresion)
    resultado_mostrado = False


def evaluar():
    global expresion, resultado_mostrado

    try:
        resultado = eval(expresion)
        if (resultado == int(resultado)):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    except:
        visor_texto.set("Error")
        expresion = ''
        resultado_mostrado = False


# configuracion del tamaño de las filas y las columnas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# configuracion del visor
visor_texto = tk.StringVar()  # stringvar variable para guardar y configurar texto
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('courier', 24, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=8,
                 justify='right',
                 relief="sunken",
                 bg="#e8f0fe",
                 fg="#333333"
                 )
visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky='ew',
           padx=12,
           pady=12,
           )

# creacion de los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), (',', 4, 1), ('C', 4, 2), ('+', 4, 3),
]

# colores almacenados en variables
color_fondo_numero = '#D5D6D2'
color_fondo_operacion = '#A1D6E2'
color_fondo_especial = '#9890B6'
color_fondo_calcular = '#B0E57C'
color_fondo_presionado = '#6A51A3'
color_fondo_calcular_presionado = '#76C7C0'
color_texto_numero = '#101958'
color_texto_especial = '#101958'

# se muestran los botones
for (texto, fila, columna) in botones:
    if texto in ['/', '*', '+', '-']:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == 'C':
        comando = limpiar
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    elif texto == ',':
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial
    else:
        comando = lambda x=texto: pulsar_tecla(x)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero

    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('courier', 20, 'bold'),
              command=comando,
              bd=1,
              relief="raised",
              bg=color_fondo,
              fg=color_texto,
              activeforeground=color_texto_especial,
              activebackground=color_fondo_presionado,
              ).grid(row=fila,
                     column=columna,
                     sticky='nsew',
                     padx=2,
                     pady=2)

# boton =
tk.Button(ventana,
          text='=',
          padx=20,
          pady=10,
          font=('Helvetica', 20, 'bold'),
          bg=color_fondo_especial,
          activeforeground=color_fondo_calcular_presionado,
          command=evaluar,

          ).grid(row=5,
                 column=0,
                 columnspan=4,
                 sticky='ew',
                 pady=2,
                 padx=2)

# ejecutar la aplicacion
ventana.mainloop()
