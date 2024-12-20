import tkinter as tk
from tkinter import messagebox


# Função definir fonte padão
def fonte_padrao(tamanho=12):
    return("Arial", tamanho)


# Função tela de login
def mostrar_tela_login(callback_sucesso):
    """Exibe a tela de login e chama o callback em caso de sucesso."""
    def verificar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            root.destroy()
            callback_sucesso()
        else:
            messagebox.showerror("Login", "Usuário ou senha inválidos.")
    
    def sair():
        """Fecha a janela principal"""
        root.quit()
        root.destroy()


    # Função para dar animação ao botao
    def on_enter(event, button):
        button.config(bg="lightblue", relief="sunken")

    def on_leave(event, button):
        button.config(bg="SystemButtonFace", relief="raised")


    root = tk.Tk()
    root.title("Diario Digital ver.1.1")
    root.geometry("700x600") #Define tamanho da tela de login



    # Frame do usuário
    frame_usuario = tk.Frame(root)
    tk.Label(frame_usuario, text="Usuário:", fg="red", font=fonte_padrao(14)).pack(side=tk.LEFT, padx=5)
    entrada_usuario = tk.Entry(frame_usuario, width=40, font=fonte_padrao(12))
    entrada_usuario.pack(side=tk.LEFT)
    frame_usuario.place(x=150, y=100)  # Posições do frame de usuário

    # Frame da senha
    frame_senha = tk.Frame(root)
    tk.Label(frame_senha, text="Senha:", fg="red", font=fonte_padrao(14)).pack(side=tk.LEFT, padx=5)
    entrada_senha = tk.Entry(frame_senha, show="*", width=20, font=fonte_padrao(12))
    entrada_senha.pack(side=tk.LEFT)
    frame_senha.place(x=159, y=140)  # Posições do frame de senha

    # Botão de login
    botao_login = tk.Button(root, text="Login", command=verificar_login, width=10, font=fonte_padrao(14))
    botao_login.place(x=220, y=200)

    # Botao sair/fechar a tela
    botao_sair = tk.Button(root, text="Sair", command=sair, width=10, font=fonte_padrao(14))
    botao_sair.place(x=400, y=200)

    # Bind de evento movimento para o botao
    botao_login.bind("<Enter>", lambda event, button=botao_login: on_enter(event, button))
    botao_login.bind("<Leave>", lambda event, button=botao_login: on_leave(event, button))
    botao_sair.bind("<Enter>", lambda event, button=botao_sair: on_enter(event, button))
    botao_sair.bind("<Leave>", lambda event, button=botao_sair: on_leave(event, button))
    
 

    root.mainloop()
    root.destroy()


# Função para testar
def callback_sucesso():
    print("Login bem sucedido")

mostrar_tela_login(callback_sucesso)

