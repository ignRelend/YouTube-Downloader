import pygame, pytube, pyperclip, sys
from pygame.locals import *
from pathlib import Path

pygame.init()
pygame.font.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("YouTube Downloader")
font = pygame.font.SysFont("Comic Sans MS", 25)
pygame.display.set_icon(pygame.image.load('assets/YouTube.png').convert_alpha())
fps = 60
clock = pygame.time.Clock()
done = "Download"
time = 0

base_surf = pygame.image.load('assets/base.png').convert_alpha()
base_rect = base_surf.get_rect(center = (width / 2, height / 2))

download_surf = pygame.image.load('assets/download.png').convert_alpha()
download_surf = pygame.transform.scale(download_surf, (600, 600))
download_rect = download_surf.get_rect(center = (width / 2, height / 2 + 100))

success_surf = pygame.image.load('assets/success.png').convert_alpha()
success_surf = pygame.transform.scale(success_surf, (600, 600))
success_rect = success_surf.get_rect(center = (width / 2, height / 2 + 100))

failed_surf = pygame.image.load('assets/failed.png').convert_alpha()
failed_surf = pygame.transform.scale(failed_surf, (600, 600))
failed_rect = failed_surf.get_rect(center = (width / 2, height / 2 + 100))

def download_video(url):
    my_video = pytube.YouTube(url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(str(Path.home() / "Downloads"))

while True:
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    screen.blit(base_surf, base_rect)
    if done == "Download" and time < 1:
        screen.blit(download_surf, download_rect)
        if download_rect.collidepoint(mouse_pos):
            if mouse[0]:
                try:
                    download_video(pyperclip.paste())
                    done = "Done"
                    time = 300
                except Exception as e:
                    print(e)
                    done = "Failed"
                    time = 300
    if done == "Done":
        screen.blit(success_surf, success_rect)
    if done == "Failed":
        screen.blit(failed_surf, failed_rect)
    time -= 1
    if time < 1:
        done = "Download"
    pygame.display.flip()
    clock.tick(fps)