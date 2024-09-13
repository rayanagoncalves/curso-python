class Music:
    name = ''
    artist = ''
    duration = int

bilhetes = Music()
bilhetes.name = 'Bilhetes'
bilhetes.artist = 'Tiago Iorc'
bilhetes.duration = 4.52

pausa = Music()
pausa.name = 'Pausa'
pausa.artist = 'Joyce Alane'
pausa.duration = 3.40

tete = Music()
tete.name = 'Tetê'
tete.artist = 'Lucas Mamede'
tete.duration = 4.05
print(vars(bilhetes))