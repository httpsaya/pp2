import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Player')
screen.fill('pink2')

def play_a_different_song():
    global currently_playing_song, songs, current_song_index
    next_song_index = (current_song_index + 1) % len(songs)
    currently_playing_song = songs[next_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = next_song_index

def play_previous_song():
    global currently_playing_song, songs, current_song_index
    previous_song_index = (current_song_index - 1) % len(songs)
    currently_playing_song = songs[previous_song_index]
    pygame.mixer.music.load(currently_playing_song)
    pygame.mixer.music.play()
    current_song_index = previous_song_index

def stop_music():
    pygame.mixer.music.stop()

def play_pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

songs = ["NewJeans.mp3", "attention.mp3", "twice.mp3"]
current_song_index = 0
currently_playing_song = songs[current_song_index]
testFont = pygame.font.Font('C:/Users/admin/Desktop/pp2/lab7/font/pixel.ttf', 50)


player_surface = testFont.render("NewJeans", False, 'pink4')
player_surface1 = testFont.render("twice", False, 'pink4')
player_surface2 = testFont.render("attention", False, 'pink4')

player_rect = player_surface.get_rect(center = (400, 50))
player_rect1 = player_surface1.get_rect(topleft = (100, 100))
player_rect2 = player_surface2.get_rect(topleft = (600, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_pause_music()
            elif event.key == pygame.K_n:
                play_a_different_song()
            elif event.key == pygame.K_p:
                play_previous_song()
            elif event.key == pygame.K_s:
                stop_music()

    screen.blit(player_surface, player_rect)
    screen.blit(player_surface1, player_rect1)
    screen.blit(player_surface2, player_rect2)

    pygame.display.flip()

pygame.quit()
