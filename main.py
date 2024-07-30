import pygame
import os

#инициализация pygame
pygame.mixer.init()

#функции управления
def play_music(file_patch):
    if os.path.isfile(file_patch):
        pygame.mixer.music.load(file_patch)
        pygame.mixer.music.play()
        print(f"Playing {file_patch}")
    else:
        print("File not found!")

def pause_music():
    pygame.mixer.music.pause()
    print("Pause paused")

def unpause_music():
    pygame.mixer.music.unpause()
    print("Music unpaused")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped")

#основной цикл
def main():
    while True:
        print("\nSimple Console Audio Player")
        print("1. Play music")
        print("2. Pause music")
        print("3. Unpause music")
        print("4. Stop music")
        print("5. Exit")
        choice = input("Enter your console: ").strip()

        if choice == '1':
            file_path = input("Enter the path to the audio file: ").strip()
            play_music(file_path)
        elif choice == '2':
            pause_music()
        elif choice == '3':
            unpause_music()
        elif choice == '4':
            stop_music()
        elif choice == '5':
            stop_music()
            print("Exitting the player. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
