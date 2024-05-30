from tkinter import ttk,PhotoImage,Label,Button,Entry,Tk,Frame



ventana = Tk()
ventana.title('Inicio de sesion')
ventana.geometry('800x500')
ventana.config(bg='#fcfcfc',width=0, height=0)
  
logo=PhotoImage(file="logo.png")
frame_logo =Frame(ventana, bd=0, width=300,relief="solid", padx=10, pady=10, bg='#3a7ff6')
frame_logo.pack(side="left", expand="yes", fill="both")
label = Label(frame_logo, image=logo, bg='#3a7ff6')
label.place(x=0, y=0, relwidth=1, relheight=1)

frame_form = Frame(ventana, bd=0,relief="solid", bg='#fcfcfc')
frame_form.pack(side="right", expand="yes", fill="both")

frame_form_top =Frame(frame_form, height=50, bd=0, relief="solid", bg='black')
frame_form_top.pack(side="top", fill="x")
title = Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
title.pack(expand="yes", fill="both")
frame_form_fill = Frame(frame_form, height=50,  bd=0, relief="solid", bg='#fcfcfc')
frame_form_fill.pack(side="bottom", expand="yes", fill="both")

etiqueta_usuario = Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
etiqueta_usuario.pack(fill="x", padx=20, pady=5)
usuario = ttk.Entry(frame_form_fill, font=('Times', 14), textvariable="hola")
usuario.pack(fill="x", padx=20, pady=10)
etiqueta_password = Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
etiqueta_password.pack(fill="x", padx=20, pady=5)
password = ttk.Entry(frame_form_fill, font=('Times', 14))
password.pack(fill="x", padx=20, pady=10)
password.config(show="*")

inicio = Button(frame_form_fill, text="Iniciar sesion", font=('Times', 15), bg='#3a7ff6', bd=0, fg="#fff")
inicio.pack(fill="x", padx=20, pady=20)
        
        
inicio = Button(frame_form_fill, text="Registrar usuario", font=('Times', 15), bg='#fcfcfc', bd=0, fg="#3a7ff6")
inicio.pack(fill="x", padx=20, pady=20)
        

ventana.mainloop()
