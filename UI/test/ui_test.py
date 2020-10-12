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

####################################################################################################

# EVENT HANDLING:
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

####################################################################################################

# UI ELEMENTS CREATION:
# self.entry = pygame_gui.elements.UITextEntryLine(
#     relative_rect=pygame.Rect((5, 47), (200, 29)),
#     manager=manager,
#     container=self,
# )

# self.button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect((210, 47), (95, 29)),
#     manager=manager,
#     container=self,
#     text='ok',
# )

# self.slider = pygame_gui.elements.UIHorizontalSlider(
#     relative_rect=pygame.Rect((5, 81), (300, 20)),
#     value_range=(-20.0, 20.0),
#     manager=manager,
#     container=self,
#     start_value=0,
# )

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

# links["test"] = pygame_gui.elements.UITextBox(
#     relative_rect=pygame.Rect((100, 500), (100, 50)),
#     text="LABEL TUNAPRO",
#     manager=manager,
# )

# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_OUT)
# activate: text_box.set_active_effect(pygame_gui.TEXT_EFFECT_FADE_IN)
# deactivate: text_box.set_active_effect(None)

####################################################################################################


class UIWeight:
    def __init__(self, value: float):
        self.value = value


class EditWeightWindow(pygame_gui.elements.UIWindow):
    # yapf: disable
    def __init__(self, manager, *args, start_pos=(0, 0), title="Edit Weight Element", weight=None, **kwargs):
        # yapf: enable
        rect = pygame.Rect(start_pos, (342, 162))
        # 310, 104

        super().__init__(*args,
                         rect=rect,
                         manager=manager,
                         window_display_title=title,
                         **kwargs)

        # Y PLANLAMA
        # 5 (offset)
        # 37 (32 text)
        # 42 (offset)
        # 71 (29 entry-button)
        # 76 (offset)
        # 96 (20 slider)
        # 102 (offset)

        # self.label.set_text(str)
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((5, 5), (300, 32)),
            manager=manager,
            container=self,
            text="Not Initialized",
        )

        # self.entry.get_text()
        # self.entry.set_text(str)
        # self.entry.set_allowed_characters("1234567890-.")
        # self.entry.validate_text_string() # her değişimde yapılabilir
        self.entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((5, 42), (200, 29)),
            manager=manager,
            container=self,
        )
        self.entry.set_allowed_characters(list("1234567890-."))

        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((210, 42), (95, 29)),
            manager=manager,
            container=self,
            text='ok',
        )

        # self.slider.set_current_value(float)
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((5, 76), (300, 20)),
            value_range=(-20.0, 20.0),
            manager=manager,
            container=self,
            start_value=0,
        )

        self.elements = [self.label, self.entry, self.button, self.slider]
        self._weight = None
        # self.disable_all()
        self.current_value = 0.0
        self.weight = weight

    def enable_elements(self):
        for element in self.elements:
            element.enable()

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if type(value) == UIWeight:
            self._weight = value
            self.adapt_all(self._weight.value)
            # İki seçenek var ama ben windowların kilitli olmasını tercih ederim
            # self.enable()

            self.disable()
            self.enable_elements()

        else:
            self.disable()

    def enter(self, value):
        # print(value)
        self.weight.value = value

    def handle(self, event):
        if event.ui_element == self.button:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                self.enter(self.current_value)

        if event.ui_element == self.entry:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if self.entry.validate_text_string(event.text):
                    self.adapt_all(event.text, entry_set_text=False)
                    self.enter(event.text)

            if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if self.entry.validate_text_string(event.text):
                    self.adapt_all(event.text, entry_set_text=False)

        if event.ui_element == self.slider:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                self.adapt_all(event.value)

    def adapt_all(self, value, entry_set_text=True):
        value = f"{value}"  # hMmmmMmM
        try:
            float(value)
            # buffer overflow go brrr
            if len(value) > 30: 
                value = value[:30]
        except:
            pass
        else:
            self.current_value = value

            if self.slider.value_range[0] > float(value):
                self.slider.set_current_value(self.slider.value_range[0])
            elif self.slider.value_range[1] < float(value):
                self.slider.set_current_value(self.slider.value_range[1])
            else:
                self.slider.set_current_value(float(value))

            self.label.set_text(f"VALUE: {value}")

            if entry_set_text:
                self.entry.set_text(value)


def main():
    manager, window_surface, background, clock = pygame_init()

    # sebebini anlayamadığım bir şekilde x+30, y+60 yapmam gerekiyor
    edit_weight_window = EditWeightWindow(start_pos=(0, 0),
                                          manager=manager,
                                          weight=UIWeight(0.0))

    windows = [edit_weight_window]

    isRunning = True
    while isRunning:
        isRunning = runTime(
            clock,
            manager,
            window_surface,
            background,
            windows,
        )


def runTime(
    clock,
    manager,
    window_surface,
    background,
    windows,
):
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.USEREVENT:
            for window in windows:
                if event.ui_element in window.elements:
                    window.handle(event)

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