import os
import keyboard
import pygame
import time


class AudioPlayer:

    def __init__(self):
        pygame.mixer.init()
        self.is_paused = False

    def load(self, file_path):
        pygame.mixer.music.load(file_path)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("⏸ Nhạc đã tạm dừng.")

    def resume(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("▶ Nhạc tiếp tục phát.")

    def stop(self):
        pygame.mixer.music.stop()
        print("⏹ Nhạc đã dừng.")


class Playlist:

    @staticmethod
    def search( song_name, directory="."):
        matching_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if song_name.lower() in file.lower():
                    matching_files.append((os.path.join(root, file)))

        if matching_files:
            print(f"🎵 Tìm thấy {len(matching_files)} file:")
            for file in matching_files:
                print(f"- {file}")
        else:
            print(f" Không tìm thấy file nào với từ khóa '{song_name}'.")

        return matching_files
    
    def __init__(self, folder_path,find_songs):
        self.folder_path = folder_path
        if find_songs:
            self.songs = find_songs
        else:
            self.songs = self.load_songs()
        self.current_index = 0


    def load_songs(self):
        
        return [f for f in os.listdir(self.folder_path) if f.endswith('.mp3')]

    def load_findsongs(self,songs):
        if songs: return songs

        return None

    def next_song(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            return self.songs[self.current_index]
        return None

    def previous_song(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)
            return self.songs[self.current_index]
        return None

    def get_current_song(self):
        if self.songs:
            return self.songs[self.current_index]
        return None

    def show_playlist(self):
        return self.songs

class MP3Player(AudioPlayer):
    
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def play(self):
        
        song = self.playlist.get_current_song()
        if song:
            file_path = os.path.join(self.playlist.folder_path, song)
            self.load(file_path)
            super().play()
            print(f"🎵 Đang phát: {song}")

    def play_indicate(self,current_song):
        if current_song:
            #file_path = os.path.join(self.playlist.folder_path, current_song)
            self.load(current_song)
            super().play()
            print(f"🎵 Đang phát: {current_song}")

    def next(self):
        self.stop()
        next_song = self.playlist.next_song()
        self.play()
        print(f"⏭ Chuyển sang bài: {next_song}")

    def previous(self):
        self.stop()
        prev_song = self.playlist.previous_song()
        self.play()
        print(f"⏮ Quay lại bài: {prev_song}")

    def mp3playercontrol(self):
        while True:
            if keyboard.is_pressed("space"):
                self.pause()
            elif keyboard.is_pressed("up"):
                self.resume()
            elif keyboard.is_pressed("left"):
                self.previous()
            elif keyboard.is_pressed("right"):
                self.next()
            elif keyboard.is_pressed("enter"):
                self.stop()
                print("Exiting... ")
                break



###Play music###
music_folder = "music"
# Add Playlist

# Control Function
while 1:
    try:
        search_input = input("Enter your song name or press Enter to play default playlist ")
        if search_input :
            song_results = Playlist.search(search_input,".")
            playlist = Playlist(music_folder,song_results)
            player = MP3Player(playlist)
            number = int(input("Enter number order of the song you want to play "))
            player.play_indicate(song_results[number - 1])
            if input("Enter 'end' to end") == "end":
                print("🎵 END!")
                player.pause()
    except:
        
    else:
        playlist = Playlist(music_folder,None)
        player = MP3Player(playlist)
        print("Playlist now:", playlist.show_playlist())
        player.play()
        player.mp3playercontrol()
