import pygame_gui
import pygame
from pygame_gui import elements
from pygame_gui.elements.ui_window import UIWindow


class colors:
    black = "#000000"
    dimgrey = "#696969"  # lmao
    darkslategray = "#2F4F4F"


TITLE = "TUNAPRO1234"
BACKGROUND = colors.darkslategray
WIDTH, HEIGHT = 600, 400
FULLSCREEN = False
"""
Hızlıca bir plan yapacağım

Neural ağları kontrol edebileceğimiz küçük bir framework

Ağların gelişimini görebileceğiz değiştirebileceğiz ve kaydedebileceğiz

Bunun için 
 -select box yapısı
 -başlatmak için buton 
 -kaydetme olayları için üstteki şeyden

Pencereler
 -tıkladığımız nöronun bilgilerini gösteren ve değiştirebilen bir pencere
 -tıkladığımız weightin değişmesini sağlayan bir pencere

Norön, katman ve ağ için pygame wrapperları yazacağım
Weigth için de bir class olur

Kaydetme olayına daha var
"""

# elements: dict: {"buttons": butonlar, "entries", entryler}


class EditWeightWindow(pygame_gui.elements.UIWindow):
    # yapf: disable
    def __init__(self, rect, manager, *args, title="Edit Weight Element", **kwargs):
        # yapf: enable
        super().__init__(*args,
                         rect=rect,
                         manager=manager,
                         window_display_title=title,
                         **kwargs)
        self.label = None

        self.entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((5, 47), (200, 29)),
            manager=manager,
            container=self,
        )

        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((210, 47), (95, 29)),
            manager=manager,
            container=self,
            text='ok',
        )

        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, 81), (300, 20)),
            value_range=(-20.0, 20.0),
            manager=manager,
            container=self,
            start_value=0,
        )

        self.ui_elements = [self.label, self.entry, self.button, self.slider]

    def handle(self, event):
        if event.ui_element == self.button:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                print('ok')

        if event.ui_element == self.entry:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                print("Entered text:", event.text)

            # if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            #     print("Changed text:", event.text)

        if event.ui_element == self.slider:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                print('current slider value:', event.value)


# dropdowns["test"] = pygame_gui.elements.UIDropDownMenu(
#     relative_rect=pygame.Rect((500, 100), (100, 20)),
#     options_list=["1", "2", "3", "4"],
#     starting_option="select",
#     manager=manager,
# )

# selects["test"] = pygame_gui.elements.UISelectionList(
#     relative_rect=pygame.Rect((100, 500), (100, 100)),
#     item_list=["1", "2", "3", "4"],
#     manager=manager,
# )

# links["test"] = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((100, 500), (100, 50)), text="LABEL TUNAPRO", manager=manager)

# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
# deactivate: text_box.set_active_effect(None)


def main():
    manager, window_surface, background, clock = pygame_init()

    # sebebini anlayamadığım bir şekilde x+32, y+64 yapmam gerekiyor
    window1 = EditWeightWindow(
        rect=pygame.Rect((0, 0), (342, 168)),
        manager=manager,
    )

    windows = [window1]

    isRunning = True
    while isRunning:
        isRunning = runTime(clock, manager, window_surface, background,
                            windows)


def runTime(clock, manager, window_surface, background, windows):

    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.USEREVENT:
            for window in windows:
                if event.ui_element in window.ui_elements:
                    window.handle(event)

            # if event.ui_element == buttons["weightEdit"]:
            #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            #         print('ok')

            # if event.ui_element == entries["weightEdit"]:
            #     if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            #         print("Entered text:", event.text)

            #     # if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            #     #     print("Changed text:", event.text)

            # if event.ui_element == sliders["weightEdit"]:
            #     if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            #         print('current slider value:', event.value)

            # if event.ui_element == dropdowns["test"]:
            #     if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            #         print("Selected option:", event.text)

            # if event.ui_element == selects["test"]:
            #     if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            #         print("Selected item:", event.text)

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
    return True


def pygame_init():
    pygame.init()
    pygame.display.set_caption(TITLE)

    if FULLSCREEN:
        window_surface = pygame.display.set_mode((WIDTH, HEIGHT),
                                                 pygame.FULLSCREEN)
    else:
        window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(pygame.Color(BACKGROUND))

    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return manager, window_surface, background, clock


if __name__ == "__main__":
    main()