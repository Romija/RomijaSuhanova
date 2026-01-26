import tkinter as tk #importē bibliotēku un lieto kodā tk 

logs=tk.Tk() #izveido galveno logu
logs.title("Tkinter paraugs") #nosaukums
logs.geometry("300x200") #izmērs

#funkcija, kas parāda sveicienu
def paradit_sveicienu():
    #mainīgais glabā txt, ko ievada lietotājs
    ievaditais = ievades_lauks.get()
    #apstrādāt kļūdes
    if ievaditais.strip()=="":
        rezultata_virkne.set("Nekas nav ievadīts.")
    else:
        rezultata_virkne.set("Sveiks, "+ievaditais+"!")

#jāizveido teksta virkne rezultātu attēlošanai
rezultata_virkne=tk.StringVar()
rezultata_virkne.set("rezultāts tiks rādīts šeit.")

#ievades lauks
ievades_lauks=tk.Entry(logs,width=25) #ievades lauka garums simbolos
ievades_lauks.pack(pady=10)

#izveidot pogu, kas izsauks funkciju
poga = tk.Button(logs,text="Parādīt sveicienu",command=paradit_sveicienu)
poga.pack(pady=5)

#izveidot logu rezultātam
rezultata_label = tk.Label(logs,textvariable = rezultata_virkne)
rezultata_label.pack(pady=10)


#obligātā rinda
logs.mainloop()