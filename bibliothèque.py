import tkinter as tk
from tkinter import filedialog
from tkinter .filedialog import asksaveasfile
from tkinter import END
from tkinter import ttk

root= tk.Tk()
root.geometry("1150x500")
root.title("Daniel")

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
def first_btnPage():
    text = tk.Label(main_frame, text="LIVRE D'HISTOIRE NATURELLE")
    text.pack()
    label = tk.Label(second_frame, text="")
    label.pack()

    def checkButton():
        if var1.get()==1 and var2.get()==0 and var3.get()==0:
            label.configure(text="HISTOIRE: Vous avez choisi LIVRE D'HISTOIRE NATURELLE, 2ème étagère droite")
        elif var1.get()==1 and var2.get()==1:
            label.configure(text="HISTOIRE: Veuillez choisir Oui ou Non")
        elif var1.get()==0 and var3.get()==1 and var4.get()==0:
            label.configure(text="HISTOIRE: Vous avez choisi le LIVRE DES AMERINDIENS, 8ème étagère gauche")
        elif var3.get()==1 and var4.get()==1:
            label.configure(text="HISTOIRE: Veuillez choisir Oui ou Non")
        elif var1.get()==0 and var2.get()==1:
            label.configure(text="HISTOIRE: Vous n'avez pas choisi de livre")
        elif var1.get()==0 and var3.get()==0:
            label.configure(text="HISTOIRE: Vous n'avez rien choisi")
        elif var1.get()==1 and var3.get()==1:
            label.configure(text="HISTOIRE: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get()==1 and var4.get()==1:
            label.configure(text="HISTOIRE: Veuillez choisir Oui ou Non")

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c = tk.Checkbutton(main_frame, text="OUI", variable=var1, onvalue=1, offvalue=0, command=checkButton)
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton)
    b.pack()

    text2 = tk.Label(main_frame, text="LIVRE DES AMERINDIENS")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()
def second_btnPage():
    text=tk.Label(main_frame,text="LIVRE D'ALGEBRE TOM1")
    text.pack()
    label=tk.Label(second_frame, text="")
    label.pack()
    def checkButton():
        if var1.get()==1 and var2.get()==0 and var3.get()==0:
            label.configure(text="MATH: Vous avez choisi le LIVRE D'ALGEBRE TOM1, 1ère étagère droite")
        elif var1.get()==1 and var2.get()==1:
            label.configure(text="MATH: Veuillez choisir Oui ou Non")
        elif var1.get()==0 and var3.get()==1 and var4.get()==0:
            label.configure(text="MATH: Vous avez choisi le LIVRE SUR LES INTEGRALES TOM2, 1ère étagère gauche")
        elif var3.get()==1 and var4.get()==1:
            label.configure(text="MATH: Veuillez choisir Oui ou Non")
        elif var1.get()==0 and var2.get()==1:
            label.configure(text="MATH: Vous n'avez pas choisi de livre")
        elif var1.get()==0 and var3.get()==0:
            label.configure(text="MATH: Vous n'avez rien choisi")
        elif var1.get()==1 and var3.get()==1:
            label.configure(text="MATH: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get()==1 and var4.get()==1:
            label.configure(text="MATH: Veuillez choisir Oui ou Non")
    var1= tk.IntVar()
    var2 = tk.IntVar()
    c= tk.Checkbutton(main_frame, text="OUI", variable=var1,onvalue=1, offvalue=0, command=checkButton )
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton )
    b.pack()


    text2 = tk.Label(main_frame, text="LIVRE SUR LES INTEGRALES TOM2")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()

def third_btnPage():
    text = tk.Label(main_frame, text="LIVRE DE JEAN-CLETTE")
    text.pack()
    label = tk.Label(second_frame, text="")
    label.pack()

    def checkButton():
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
            label.configure(text="ELECTRICITE: Vous avez choisi LE LIVRE DE JEAN-CLETTE, 4ème étagère droite")
        elif var1.get() == 1 and var2.get() == 1:
            label.configure(text="ELECTRICITE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var3.get() == 1 and var4.get() == 0:
            label.configure(text="ELEC: Vous avez choisi le LIVRE SUR LES MOTEURS ELECTRIQUES, 1ère étagère gauche")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="ELECTRICITE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var2.get() == 1:
            label.configure(text="ELECTRICITE: Vous n'avez pas choisi de livre")
        elif var1.get() == 0 and var3.get() == 0:
            label.configure(text="ELECTRICITE: Vous n'avez rien choisi")
        elif var1.get() == 1 and var3.get() == 1:
            label.configure(text="ELECTRICITE: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="Veuillez choisir Oui ou Non")

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c = tk.Checkbutton(main_frame, text="OUI", variable=var1, onvalue=1, offvalue=0, command=checkButton)
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton)
    b.pack()

    text2 = tk.Label(main_frame, text="LIVRE SUR LES MOTEURS ELECTRIQUES")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()
def fourth_btnPage():
    text = tk.Label(main_frame, text="LIVRE SUR LES ACIDES TOM3")
    text.pack()
    label = tk.Label(second_frame, text="")
    label.pack()

    def checkButton():
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
            label.configure(text="CHIMIE: Vous avez choisi le LIVRE SUR LES ACIDES TOM3, 1ère étagère droite")
        elif var1.get() == 1 and var2.get() == 1:
            label.configure(text="CHIMIE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var3.get() == 1 and var4.get() == 0:
            label.configure(text="CHIMIE: Vous avez choisi le livre PHYSIQUE QUANTIQUE ET CHIMIE, 6ème étagère droite")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="CHIMIE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var2.get() == 1:
            label.configure(text="CHIMIE: Vous n'avez pas choisi de livre")
        elif var1.get() == 0 and var3.get() == 0:
            label.configure(text="CHIMIE: Vous n'avez rien choisi")
        elif var1.get() == 1 and var3.get() == 1:
            label.configure(text="CHIMIE: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="CHIMIE: Veuillez choisir Oui ou Non")

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c = tk.Checkbutton(main_frame, text="OUI", variable=var1, onvalue=1, offvalue=0, command=checkButton)
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton)
    b.pack()

    text2 = tk.Label(main_frame, text="PHYSIQUE QUANTIQUE ET CHIMIE")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()
def fifth_btnPage():
    text = tk.Label(main_frame, text="LA PROGRAMMATION TOM2")
    text.pack()
    label = tk.Label(second_frame, text="")
    label.pack()

    def checkButton():
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
            label.configure(text="INFORMATIQUE: Vous avez choisi LA PROGRAMMATION TOM2, 5ème étagère gauche")
        elif var1.get() == 1 and var2.get() == 1:
            label.configure(text="INFORMATIQUE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var3.get() == 1 and var4.get() == 0:
            label.configure(text="INFORMATIQUE: Vous avez choisi LES INTERFACES GRAPHIQUES, 5ème étagère droite")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="INFORMATIQUE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var2.get() == 1:
            label.configure(text="CHIMIE: Vous n'avez pas choisi de livre")
        elif var1.get() == 0 and var3.get() == 0:
            label.configure(text="CHIMIE: Vous n'avez rien choisi")
        elif var1.get() == 1 and var3.get() == 1:
            label.configure(text="CHIMIE: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="CHIMIE: Veuillez choisir Oui ou Non")

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c = tk.Checkbutton(main_frame, text="OUI", variable=var1, onvalue=1, offvalue=0, command=checkButton)
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton)
    b.pack()

    text2 = tk.Label(main_frame, text="LES INTERFACES GRAPHIQUES")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()

def sixth_btnPage():
    text = tk.Label(main_frame, text="LE TRANSISTOR ET SON EVOLUTION")
    text.pack()
    label = tk.Label(second_frame, text="")
    label.pack()

    def checkButton():
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 0:
            label.configure(text="ELECTRONIQUE: Vous avez choisi LE TRANSISTOR ET SON EVOLUTION, 4ème étagère gauche")
        elif var1.get() == 1 and var2.get() == 1:
            label.configure(text="ELECTRONIQUE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var3.get() == 1 and var4.get() == 0:
            label.configure(text="ELECTRONIQUE: Vous avez choisi LES CIRCUITS INTEGRES, 1ère étagère droite")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="ELECTRONIQUE: Veuillez choisir Oui ou Non")
        elif var1.get() == 0 and var2.get() == 1:
            label.configure(text="ELECTRONIQUE: Vous n'avez pas choisi de livre")
        elif var1.get() == 0 and var3.get() == 0:
            label.configure(text="ELECTRONIQUE: Vous n'avez rien choisi")
        elif var1.get() == 1 and var3.get() == 1:
            label.configure(text="ELECTRONIQUE: On ne lu pas deux livres de la même rubrique, veuillez vous informez")
        elif var3.get() == 1 and var4.get() == 1:
            label.configure(text="ELECTRONIQUE: Veuillez choisir Oui ou Non")

    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c = tk.Checkbutton(main_frame, text="OUI", variable=var1, onvalue=1, offvalue=0, command=checkButton)
    c.pack()
    b = tk.Checkbutton(main_frame, text="NON", variable=var2, onvalue=1, offvalue=0, command=checkButton)
    b.pack()

    text2 = tk.Label(main_frame, text="LES CIRCUITS INTEGRES")
    text2.pack()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    d = tk.Checkbutton(main_frame, text="OUI", variable=var3, onvalue=1, offvalue=0, command=checkButton)
    d.pack()
    e = tk.Checkbutton(main_frame, text="NON", variable=var4, onvalue=1, offvalue=0, command=checkButton)
    e.pack()

def indicate(lb, page):
    hide_indicators()
    lb.config(bg="#158aff")
    delete_pages()
    page()
def hide_indicators():
    first_btn_indicate.config(bg="#c3c3c3")
    second_btn_indicate.config(bg="#c3c3c3")
    third_btn_indicate.config(bg="#c3c3c3")
    fourth_btn_indicate.config(bg="#c3c3c3")
    fifth_btn_indicate.config(bg="#c3c3c3")
    sixth_btn_indicate.config(bg="#c3c3c3")

options_frame = tk.Frame(root, bg="#c3c3c3")

first_btn=tk.Button(options_frame, text="Histoire", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command= lambda: indicate(first_btn_indicate, first_btnPage))
first_btn.place(x=10, y=50)
first_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
first_btn_indicate.place(x=3,y=50, width=5, height=40)

second_btn=tk.Button(options_frame, text="Mathématiques", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command=lambda: indicate(second_btn_indicate, second_btnPage))
second_btn.place(x=10, y=100)
second_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
second_btn_indicate.place(x=3, y=100, width=5, height=40)

third_btn=tk.Button(options_frame, text="Electricité", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command=lambda: indicate(third_btn_indicate, third_btnPage))
third_btn.place(x=10, y=150)
third_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
third_btn_indicate.place(x=3, y=150, width=5, height=40)

fourth_btn=tk.Button(options_frame, text="Chimie", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command=lambda: indicate(fourth_btn_indicate, fourth_btnPage))
fourth_btn.place(x=10, y=200)
fourth_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
fourth_btn_indicate.place(x=3, y=200, width=5, height=40)

fifth_btn=tk.Button(options_frame, text="Informatique", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command=lambda: indicate(fifth_btn_indicate, fifth_btnPage))
fifth_btn.place(x=10, y=250)
fifth_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
fifth_btn_indicate.place(x=3, y=250, width=5, height=40)

sixth_btn=tk.Button(options_frame, text="Electronique", font=("Bold",15), fg=("#158aff"), bd=0, bg="blue", command=lambda: indicate(sixth_btn_indicate, sixth_btnPage))
sixth_btn.place(x=10, y=300)
sixth_btn_indicate=tk.Label(options_frame,text="", bg="#c3c3c3")
sixth_btn_indicate.place(x=3, y=300, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=180, height=400)

main_frame=tk.Frame(root, highlightbackground="black", highlightthickness=4)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=400, width=500)

second_frame=tk.Frame(root, highlightbackground="black", highlightthickness=4)
second_frame.pack(side=tk.RIGHT)
second_frame.pack_propagate(False)
second_frame.configure(height=400, width=500)

note=tk.Label(second_frame, text="Inscrivez tous les livres choisis et enregistrer, svp!!!", height=4, font="Arial", fg="Red" )
note.pack()

def savefile():
    livre=text.get('1.0',END)
    fob=filedialog.asksaveasfile(filetypes=[('text file','*txt')], defaultextension='.txt', mode='w')

    try:
        fob.write(livre)
        fob.close()
        text.delete('1.0',END)
        text.update()
        savebutton.config(text="Patientez, svp")
        savebutton.after(5000, lambda: savebutton.config(text="Enregistrer"))
    except:
        print("Erreur")
text=tk.Text(second_frame, width=40, height=3)
text.pack()

savebutton = tk.Button(second_frame, text="Enregistrer", command=lambda: savefile(), width=20)
savebutton.pack()

regle=tk.Label(main_frame, text="veuillez respecter les règles d'approbations des livres", font="Arial")
regle.pack()



root.mainloop()
