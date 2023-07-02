import os
import tkinter as tk
from tkinter import ttk
import threading

def open_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.startfile(folder_path)

def go_back():
    for widget in frame.winfo_children():
        widget.destroy()
    show_main_page()

def load_question(file_path):
    def execute_question():
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
        try:
            exec(code, globals())
        except Exception as e:
            print("Erro ao executar a questão:", e)

    thread = threading.Thread(target=execute_question)
    thread.start()

def show_question(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        question_content = file.read()
    print("Questão:")
    print(question_content)
    print("-----------------------------")

    btn_load_question = ttk.Button(frame, text="Carregar Questão", command=lambda path=file_path: load_question(path))
    btn_load_question.pack(pady=10)

def show_folder_content(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    for widget in frame.winfo_children():
        widget.destroy()

    label_folder = ttk.Label(frame, text="Conteúdo da pasta '{}'".format(folder_name), font=("Arial", 16, "bold"))
    label_folder.pack(pady=10)

    btn_back = ttk.Button(frame, text="Voltar", command=go_back)
    btn_back.pack(pady=10)

    file_names = os.listdir(folder_path)
    question_files = sorted([file_name for file_name in file_names if file_name.endswith(".py")], key=lambda x: x.lower())

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    question_list = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 12))
    question_list.pack(pady=5, padx=30, fill=tk.BOTH, expand=True)

    scrollbar.config(command=question_list.yview)

    for file_name in question_files:
        file_path = os.path.join(folder_path, file_name)
        question_list.insert(tk.END, file_name)

    def on_select(event):
        selected_index = question_list.curselection()
        if selected_index:
            selected_file = question_list.get(selected_index[0])
            file_path = os.path.join(folder_path, selected_file)
            show_question(file_path)

    question_list.bind("<<ListboxSelect>>", on_select)

def show_main_page():
    label_main = ttk.Label(frame, text="LISTAS DE ATIVIDADES EM PYTHON!", font=("Arial", 22, "bold"))
    label_main.pack(pady=20)

    label_credits = ttk.Label(frame, text="Gerlânio & Milleny", font=("Arial", 18, "italic"))
    label_credits.pack()

    for folder_name in folder_names:
        btn_folder = ttk.Button(frame, text=folder_name, command=lambda name=folder_name: show_folder_content(name))
        btn_folder.pack(pady=10)

window = tk.Tk()
window.title("Interface de Acesso às Pastas")

style = ttk.Style(window)
style.configure("TButton",
                font=("Arial", 12),
                padding=10)
style.configure("TLabel",
                font=("Arial", 14),
                padding=10)
style.configure("TListbox",
                font=("Arial", 12),
                padding=10)

frame = ttk.Frame(window, padding="30")
frame.pack(fill=tk.BOTH, expand=True)

folder_names = ["Lista 1", "Lista 2", "Lista 3", "Lista 4", "Lista 5", "Lista 6", "Lista 7"]

show_main_page()

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()