class ScreenManager:
    def __init__(self):
        self.screens: dict[str, Screen] = {}
        self.current_screen = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def set_screen(self, name):
        self.current_screen = self.screens[name]

    def handle_events(self, events):
        next_screen = self.current_screen.handle_events(events)
        if next_screen:
            self.set_screen(next_screen)

    def update(self):
        self.current_screen.update()

    def render(self, screen):
        self.current_screen.render(screen)


screen_manager = ScreenManager()


class Screen:
    def __init__(self, name=None):
        self.manager = screen_manager
        self.name = name or self.__class__.__name__
        self.manager.add_screen(self.name, self)

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass
