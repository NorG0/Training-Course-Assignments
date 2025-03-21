import os

import pygame

class AudioPlayer:
    """Lớp cha quản lý chức năng phát nhạc"""
    def __init__(self):
        pygame.mixer.init()
        self.is_paused = False

    def load(self, file_path):
        """Tải file nhạc"""
        pygame.mixer.music.load(file_path)

    def play(self):
        """Phát nhạc"""
        pygame.mixer.music.play()

    def pause(self):
        """Tạm dừng nhạc"""
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("⏸ Nhạc đã tạm dừng.")

    def resume(self):
        """Tiếp tục nhạc"""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            print("▶ Nhạc tiếp tục phát.")

    def stop(self):
        """Dừng nhạc"""
        pygame.mixer.music.stop()
        print("⏹ Nhạc đã dừng.")


    def search(self, song_name, directory="."):
        matching_files = []

        # Duyệt qua thư mục và các thư mục con
        for root, _, files in os.walk(directory):
            for file in files:
                if song_name.lower() in file.lower():
                    matching_files.append(os.path.join(root, file))

        if matching_files:
            print(f"🎵 Tìm thấy {len(matching_files)} file:")
            for file in matching_files:
                print(f"- {file}")
        else:
            print(f"❌ Không tìm thấy file nào với từ khóa '{song_name}'.")

        return matching_files


