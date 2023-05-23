import pygame



class LoadingScreen:
    def __init__(self, background_image_path, screen_size=(800, 600), font_size=36):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.background_image = pygame.image.load(background_image_path).convert()
        self.font = pygame.font.Font(None, font_size)

    def show_loading_screen(self):
        text = self.font.render("Loading...", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def show_progress(self, progress):
        progress_text = self.font.render(f"Loading... {progress}%", True, (255, 255, 255))
        progress_rect = progress_text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(progress_text, progress_rect)
        pygame.display.flip()

    def run_loading(self):
        self.show_loading_screen()
        for i in range(10):
            pygame.time.delay(500)
            self.show_progress(i*10)
        pygame.quit()

loading_screen = LoadingScreen("background.png")
