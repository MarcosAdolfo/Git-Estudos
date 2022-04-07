from pygame import mixer
mixer.init()
mixer.music.load('Romantica piano.mp3')
mixer.music.play()
print('\033[1;32;40m <<  < >  >>')
input()