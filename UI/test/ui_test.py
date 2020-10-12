import pygame_gui
import pygame


class colors:
    black = "#000000"
    dimgrey = "#696969"  # lmao
    darkslategray = "#2F4F4F"


TITLE = "TUNAPRO1234"
BACKGROUND = colors.darkslategray
WIDTH, HEIGHT = 1920, 1080

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
    window_surface = pygame.display.set_mode((WIDTH, HEIGHT),
                                             pygame.FULLSCREEN)

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

    #yapf: disable
    entries["Hello"] = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400, 500), (200, 50)), manager=manager)

    buttons["Hello"] = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((605, 500), (95, 29)), text='ok', manager=manager)

    sliders["Hello"] = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((400, 534), (300, 20)), start_value=0, value_range=(-20.0, 20.0), manager=manager)

    dropdowns["Hello"] = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((500, 100), (100, 20)), options_list=["1", "2", "3", "4"], starting_option="select", manager=manager)

    selects["Hello"] = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((100, 500), (100, 100)), item_list=["1", "2", "3", "4"], manager=manager)

    # links["Hello"] = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((100, 500), (100, 50)), text="LABEL TUNAPRO", manager=manager)

    windows["Hello"] = pygame_gui.elements.UIWindow(rect=pygame.Rect((100, 100), (200, 200)), manager=manager, window_display_title="test", resizable=True)

    buttonRect = pygame.Rect(0, 0, 100, 20)
    buttonRect.bottomright = (-30, -20)

    anchors = {
        'left': 'right',
        'right': 'right',
        'top': 'bottom',
        'bottom': 'bottom'
    }

    pygame_gui.elements.UIButton(relative_rect=buttonRect, text='Hello', manager=manager, container=windows["Hello"], anchors=anchors)

    # yapf: enable

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
                if event.ui_element == buttons["Hello"]:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        print('Hello World!')

                if event.ui_element == dropdowns["Hello"]:
                    if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                        print("Selected option:", event.text)

                if event.ui_element == entries["Hello"]:
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                        print("Entered text:", event.text)

                    # if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    #     print("Changed text:", event.text)

                if event.ui_element == sliders["Hello"]:
                    if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                        print('current slider value:', event.value)

                if event.ui_element == selects["Hello"]:
                    if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                        print("Selected item:", event.text)

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


if __name__ == "__main__":
    main()