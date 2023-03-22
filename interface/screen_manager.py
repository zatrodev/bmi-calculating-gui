from interface.root import root


class ScreenManager():
    def __init__(self, root):
        self.root = root
        self.screens = {}
        self.current_screen = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def switch_screen(self, name):
        if self.current_screen is not None:
            self.current_screen.grid_remove()

        self.current_screen = self.screens[name]
        print(self.current_screen)
        self.current_screen.grid()


screen_manager = ScreenManager(root)
