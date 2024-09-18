class Music:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

bilhetes = Music(name='Bilhetes', artist='Tiago Iorc', duration=4.52)

pausa = Music(name='Pausa', artist='Joyce Alane', duration=3.40)

tete = Music(name='Tetê', artist='Lucas Mamede', duration=4.05)

print(vars(bilhetes))