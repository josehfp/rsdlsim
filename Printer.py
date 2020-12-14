# Constantes de Text Color
TC_BLACK = 30
TC_RED = 31
TC_GREEN = 32
TC_YELLOW = 33
TC_BLUE = 34
TC_PURPLE = 35
TC_CYAN = 36
TC_WHITE = 37
# Constantes de BackGound Color
BG_DEFAULT = 48
BG_BLACK = 40
BG_RED = 41
BG_GREEN = 42
BG_YELLOW = 43
BG_BLUE = 44
BG_PURPLE = 45
BG_CYAN = 46
BG_WHITE = 47
# Text Style
TS_NORMAL = 0
TS_BOLD = 1
TS_UNDERLINE = 2
# Ao usar um stilo, se altera todos os textos depois dele.
# É necessário voltar o texto ao normal usando esse código
RETURN_TO_DEFAULT_TEXT = "\033[" + str(TS_NORMAL) + ";" + str(TC_WHITE) + ";" + str(BG_DEFAULT) + "m"


def color_string(text, text_style, text_color, background_color):
    return "\033[" + str(text_style) + ";" + str(text_color) + ";" + str(background_color) + "m" \
           + text + RETURN_TO_DEFAULT_TEXT


def bluebg_txt(text):
    return color_string(text, TS_BOLD, TC_BLACK, BG_BLUE)


def redbg_txt(text):
    return color_string(text, TS_BOLD, TC_BLACK, BG_RED)


def greenbg_txt(text):
    return color_string(text, TS_BOLD, TC_BLACK, BG_GREEN)
