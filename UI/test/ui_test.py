import pygame_gui
import pygame


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


class Window:
    def __init__(self, screen, buttons={}, entries={}):
        self.buttons = buttons
        self.entries = entries
        self.screen = screen


def main():
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

    buttons = {}
    entries = {}
    selects = {}
    sliders = {}
    windows = {}
    # labels = {}
    dropdowns = {}

    # sebebini anlayamadığım bir şekilde x+32, y+64 yapmam gerekiyor
    # (310, 64)

    windows["weightEdit"] = pygame_gui.elements.UIWindow(
        rect=pygame.Rect((0, 0), (342, 124)),
        manager=manager,
    )

    entries["weightEdit"] = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((5, 5), (200, 29)),
        container=windows["weightEdit"],
        manager=manager,
    )

    buttons["weightEdit"] = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((210, 5), (95, 29)),
        container=windows["weightEdit"],
        manager=manager,
        text='ok',
    )

    sliders["weightEdit"] = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((5, 39), (300, 20)),
        container=windows["weightEdit"],
        value_range=(-20.0, 20.0),
        manager=manager,
        start_value=0,
    )

    dropdowns["test"] = pygame_gui.elements.UIDropDownMenu(
        relative_rect=pygame.Rect((500, 100), (100, 20)),
        options_list=["1", "2", "3", "4"],
        starting_option="select",
        manager=manager,
    )

    selects["test"] = pygame_gui.elements.UISelectionList(
        relative_rect=pygame.Rect((100, 500), (100, 100)),
        item_list=["1", "2", "3", "4"],
        manager=manager,
    )

    # links["test"] = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((100, 500), (100, 50)), text="LABEL TUNAPRO", manager=manager)

    # activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
    # activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
    # activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
    # deactivate: text_box.set_active_effect(None)

    clock = pygame.time.Clock()
    isRunning = True

    while isRunning:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

            if event.type == pygame.USEREVENT:
                if event.ui_element == buttons["weightEdit"]:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        print('ok')

                if event.ui_element == entries["weightEdit"]:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        print("Entered text:", event.text)

                    # if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    #     print("Changed text:", event.text)

                if event.ui_element == sliders["weightEdit"]:
                    if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                        print('current slider value:', event.value)

                if event.ui_element == dropdowns["test"]:
                    if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                        print("Selected option:", event.text)

                if event.ui_element == selects["test"]:
                    if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                        print("Selected item:", event.text)

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == "__main__":
    main()