import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
def show_hotkeys():

    print(" keys:")
    print(" SPACE - Play music")
    print(" S - Stop the music")
    print(" N - Next track")
    print(" P - Previous track")

show_hotkeys()

music_path = "/Users/azhardyusembaykyzy/Desktop/pp/lab7/"
musics = [f"{music_path}jennie - twin.mp3",
          f"{music_path}Gracie Abrams - That’s So True.mp3",
          f"{music_path}Paris Paloma - labour.mp3",
          f"{music_path}Same Old Love (Sefon.me).mp3",
          f"{music_path}Shawn Mendes - Stitches.mp3"]
track = 0

pygame.mixer.music.load(musics[track])  
pygame.mixer.music.play()

def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def next():
    global track
    track=(track+1)%len(musics)
    pygame.mixer.music.load(musics[track])
    play()
def prev():
    global track
    track=(track-1)%len(musics)
    pygame.mixer.music.load(musics[track])
    play()
run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                play()
            elif event.key==pygame.K_s:
                stop()
            elif event.key==pygame.K_n:
                next()
            elif event.key == pygame.K_p:
                prev()
    pygame.display.flip()
pygame.quit()