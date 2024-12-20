import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def validar_cpf(cpf):
    """Valida o formato do CPF (apenas números)."""
    return len(cpf) == 11 and cpf.isdigit()

def cadastrar_aluno():
    """Cadastra um novo aluno no sistema."""
    nome = simpledialog.askstring("Cadastro de Aluno", "Digite o nome do aluno:")
    if not nome:
        return

    while True:
        cpf = simpledialog.askstring("Cadastro de Aluno", "Digite o CPF do aluno (apenas números):")
        if cpf and validar_cpf(cpf):
            break
        messagebox.showerror("Erro", "CPF inválido. Certifique-se de digitar 11 números.")

    numero_matricula = simpledialog.askstring("Cadastro de Aluno", "Digite o número de matrícula do aluno:")
    if not numero_matricula:
        return

    while True:
        data_nascimento = simpledialog.askstring("Cadastro de Aluno", "Digite a data de nascimento do aluno (DD/MM/AAAA):")
        try:
            if data_nascimento:
                data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                break
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. Use o formato DD/MM/AAAA.")

    turma = simpledialog.askstring("Cadastro de Aluno", "Digite a turma do aluno:")
    if not turma:
        return

    aluno = {
        "nome": nome,
        "cpf": cpf,
        "numero_matricula": numero_matricula,
        "data_nascimento": data_nascimento,
        "turma": turma
    }
    alunos.append(aluno)
    messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

def listar_alunos():
    """Exibe todos os alunos cadastrados."""
    if not alunos:
        messagebox.showinfo("Lista de Alunos", "Nenhum aluno cadastrado.")
        return

    lista = "\n".join([
        f"{idx + 1}. Nome: {aluno['nome']}, CPF: {aluno['cpf']}, Matrícula: {aluno['numero_matricula']}, "
        f"Data de Nascimento: {aluno['data_nascimento'].strftime('%d/%m/%Y')}, Turma: {aluno['turma']}"
        for idx, aluno in enumerate(alunos)
    ])
    messagebox.showinfo("Lista de Alunos", lista)

def buscar_aluno():
    """Busca um aluno pelo número de matrícula."""
    matricula = simpledialog.askstring("Buscar Aluno", "Digite o número de matrícula do aluno:")
    if not matricula:
        return

    for aluno in alunos:
        if aluno['numero_matricula'] == matricula:
            detalhes = (f"Nome: {aluno['nome']}\nCPF: {aluno['cpf']}\nMatrícula: {aluno['numero_matricula']}\n"
                        f"Data de Nascimento: {aluno['data_nascimento'].strftime('%d/%m/%Y')}\nTurma: {aluno['turma']}")
            messagebox.showinfo("Aluno Encontrado", detalhes)
            return

    messagebox.showinfo("Buscar Aluno", "Aluno não encontrado.")

def sair():
    """Fecha o aplicativo."""
    root.destroy()

# Lista para armazenar os alunos
alunos = []

# Interface gráfica
root = tk.Tk()
root.title("Sistema de Cadastro de Alunos")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

btn_cadastrar = tk.Button(frame, text="Cadastrar Aluno", command=cadastrar_aluno)
btn_cadastrar.pack(fill="x", pady=5)

btn_listar = tk.Button(frame, text="Listar Alunos", command=listar_alunos)
btn_listar.pack(fill="x", pady=5)

btn_buscar = tk.Button(frame, text="Buscar Aluno", command=buscar_aluno)
btn_buscar.pack(fill="x", pady=5)

btn_sair = tk.Button(frame, text="Sair", command=sair)
btn_sair.pack(fill="x", pady=5)

root.mainloop()