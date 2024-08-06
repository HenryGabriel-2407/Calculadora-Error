import customtkinter as ctk
from functools import partial

janela = ctk.CTk()
janela.geometry("400x400")
janela.title("Calculadora :D")

text_box = ctk.CTkTextbox(janela, width=350, height=100, font=("segoe ui", 14))
text_box.grid(row=1, column=0, columnspan= 4, sticky="ew")
text_box.configure(state="disabled")

def limpar():
    text_box.configure(state="normal")
    text_box.delete(1.0, ctk.END)
    text_box.configure(state="disabled")

def imprimir_erro():
    text_box.configure(state="normal")
    text_box.delete(1.0, ctk.END)
    text_box.insert(ctk.END, text="Usuário {pedro_gamer123} já calculou essa equação")
    text_box.configure(state="disabled")

def imprimir_calculando():
    text_box.configure(state="normal")
    text_box.delete(1.0, ctk.END)
    text_box.insert(ctk.END, text="Calculando a equação...")
    text_box.configure(state="disabled")
    janela.after(5000, imprimir_erro)

def verificar():
    text_atual = text_box.get(1.0, ctk.END).strip()
    if text_atual == "Usuário {pedro_gamer123} já calculou essa equação":
        limpar()
    else:
        pass

def imprimir(num):
    verificar()
    text_box.configure(state="normal")
    text_box.insert(ctk.END, text=num)
    text_box.configure(state="disabled")

botao_0 = ctk.CTkButton(janela, width=70, height=70, text="0", font=("segoe ui", 18), command=partial(imprimir, "0"))
botao_0.grid(row=5, column=1, sticky="w")
botao_1 = ctk.CTkButton(janela, width=70, height=70, text="1", font=("segoe ui", 18), command=partial(imprimir, "1"))
botao_1.grid(row=4, column=0, sticky="w")
botao_2 = ctk.CTkButton(janela, width=70, height=70, text="2", font=("segoe ui", 18), command=partial(imprimir, "2"))
botao_2.grid(row=4, column=1, sticky="w")
botao_3 = ctk.CTkButton(janela, width=70, height=70, text="3", font=("segoe ui", 18), command=partial(imprimir, "3"))
botao_3.grid(row=4, column=2, sticky="w")
botao_4 = ctk.CTkButton(janela, width=70, height=70, text="4", font=("segoe ui", 18), command=partial(imprimir, "4"))
botao_4.grid(row=3, column=0, sticky="w")
botao_5 = ctk.CTkButton(janela, width=70, height=70, text="5", font=("segoe ui", 18), command=partial(imprimir, "5"))
botao_5.grid(row=3, column=1, sticky="w")
botao_6 = ctk.CTkButton(janela, width=70, height=70, text="6", font=("segoe ui", 18), command=partial(imprimir, "6"))
botao_6.grid(row=3, column=2, sticky="w")
botao_7 = ctk.CTkButton(janela, width=70, height=70, text="7", font=("segoe ui", 18), command=partial(imprimir, "7"))
botao_7.grid(row=2, column=0, sticky="w")
botao_8 = ctk.CTkButton(janela, width=70, height=70, text="8", font=("segoe ui", 18), command=partial(imprimir, "8"))
botao_8.grid(row=2, column=1, sticky="w")
botao_9 = ctk.CTkButton(janela, width=70, height=70, text="9", font=("segoe ui", 18), command=partial(imprimir, "9"))
botao_9.grid(row=2, column=2, sticky="w")

botao_somar = ctk.CTkButton(janela, width=70, height=70, text="+", font=("segoe ui", 18), command=partial(imprimir, "+"))
botao_somar.grid(row=2, column=3, sticky="w")
botao_subtrair = ctk.CTkButton(janela, width=70, height=70, text="-", font=("segoe ui", 18), command=partial(imprimir, "-"))
botao_subtrair.grid(row=3, column=3, sticky="w")
botao_multiplicar = ctk.CTkButton(janela, width=70, height=70, text="x", font=("segoe ui", 18), command=partial(imprimir, "0"))
botao_multiplicar.grid(row=4, column=3, sticky="w")
botao_dividir = ctk.CTkButton(janela, width=70, height=70, text="/", font=("segoe ui", 18), command=partial(imprimir, "0"))
botao_dividir.grid(row=5, column=3, sticky="w")

botao_limpar = ctk.CTkButton(janela, width=70, height=70, text="C", text_color="red", font=("segoe ui", 18), command=limpar).grid(row=5, column=0, sticky="w")
botao_igual = ctk.CTkButton(janela, width=70, height=70, text="=", font=("segoe ui", 18), command=imprimir_calculando).grid(row=5, column=2, sticky="w")


janela.mainloop()