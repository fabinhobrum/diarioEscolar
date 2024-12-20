from login import mostrar_tela_login

def main():
    mostrar_tela_login(callback_sucesso=lambda: print("Login bem sucedido!"))

if __name__ == "__main__":
    main()