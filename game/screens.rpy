init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)






style apoiase_text:


    size 12

style wp:
    background "#FFF"
    left_padding 2
    right_padding 2
    top_padding 2
    bottom_padding 2
    xalign 0.0

style wp_left:
    xsize 10
    ysize 22
    background "celular/wp-balao-left.png"

style wp_right:
    xsize 10
    ysize 22
    background "celular/wp-balao-right.png"

style wpmc:
    background "#e1ffc7"
    left_padding 2
    right_padding 2
    top_padding 2
    bottom_padding 2
    xalign 0.0

style wp_mc_left:
    xsize 10
    ysize 22
    background "celular/wp-balaomc-left.png"

style wp_mc_right:
    xsize 10
    ysize 22
    background "celular/wp-balaomc-right.png"

style celular_msg:
    size 15
    color "#000"

style celular_msg_mc:
    size 15
    xalign 1.0

    color "#000"

style tela_texto:
    size 22
    color "#999"
    xalign 0.5

style tela_padrao:
    color "#999"
    xalign 0.5
    yalign 0.5
    xminimum 610
    xmaximum 610
    yminimum 260
    ymaximum 260
    xpadding 20
    ypadding 30
    background Frame("extra/frame_background_600x250.png")


















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):

        add SideImage() xalign 0.0 yalign 1.0

    else:

        add SideImage() xalign 0.0 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width











default timeout = 5.0



default timeout_label = None

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if timeout_label is not None:

        bar:
            xalign 0.5
            ypos 400
            xsize 740
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action Jump(timeout_label)




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 200

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Voltar") action Rollback()
            textbutton _("Histórico") action ShowMenu('history')
            textbutton _("Pular") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Salvar") action ShowMenu('save')

            textbutton _("Cheats") action Show('cheats_screen')

            textbutton _("Menu") action ShowMenu('preferences')

        vbox:
            style_prefix "quick"

            xalign 1.0
            yalign 0

            spacing 5

            hbox:
                style_prefix "quick"

                imagebutton auto "extra/botao_voltar_%s.png" action Rollback()
                imagebutton auto "extra/botao_pular_%s.png" action Skip() alternate Skip(fast=True, confirm=False)
                imagebutton auto "extra/botao_salvar_%s.png" action ShowMenu('salvar')

                imagebutton auto "extra/botao_carregar_%s.png" action ShowMenu('carregar')
                imagebutton auto "extra/botao_esconder_%s.png" action [Hide("say"), Hide("choice"), SetVariable("show_quick_menu", False)]

                textbutton _("Cheats") action Show('cheats_screen')














            hbox:

                xalign 0.985

                vbox:

                    if tempo <= 1:

                        add "extra/tempo_1.png"

                    elif tempo == 2:

                        add "extra/tempo_2.png"

                    else:

                        add "extra/tempo_3.png"



                    frame:

                        xysize (50,50)
                        background Frame("extra/calendario.png")

                        text "[dia]" size 20 xalign 0.5 yalign 0.7

                imagebutton auto "extra/celular_menu_%s.png" action Show("menu_celular")

            imagebutton idle "extra/botao_geiko.webp":
                action OpenURL("https://www.linktr.ee/geikogames/")
                xalign 0.98

    frame:
        xalign 1.0
        yalign 1.0
        xpadding 10
        ypadding 10
        background None

        imagebutton auto "extra/botao_menu_%s.png" action ShowMenu("menu_novidades")




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")











screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:



            if persistent.quincy_morte and not persistent.quincy_especial:

                imagebutton auto "extra/botao_quincy_%s.png" action Jump("quincy_morte_evento")

            if renpy.variant("mobile"):

                if not renpy.can_load("None-continue"):

                    imagebutton auto "extra/botao_novojogo_%s.png" action Start()

                else:

                    imagebutton auto "extra/botao_continuar_%s.png" action ShowMenu('carregar')



                    imagebutton auto "extra/botao_novojogo_%s.png" action Start()











            else:

                imagebutton auto "extra/botao_jogar_%s.png" action Start()

                imagebutton auto "extra/botao_continuar_%s.png" action ShowMenu("load")

        else:

            imagebutton auto "extra/botao_continuar_%s.png" action ShowMenu("load")



            imagebutton auto "extra/botao_salvar_%s.png" action ShowMenu("save")







        imagebutton auto "extra/botao_geiko_%s.webp" action OpenURL("https://www.geiko.net/jogos")



        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        if not renpy.variant("mobile"):

            if not main_menu:

                textbutton _("Menu Principal") action MainMenu()



        imagebutton auto "extra/botao_nuvem_%s.png" action Call("baixar_nuvem")



        if renpy.variant("pc"):

            if not main_menu:


                textbutton _("Controles") action ShowMenu("help")


            textbutton _("Sair") action Quit(confirm=not main_menu)

    vbox:

        style_prefix "navigation"

        xpos gui.navigation_xpos
        xalign 0
        yalign 0.85

        text "Baixe a versão premium":
            style "apoiase_text"

        imagebutton auto "extra/apoiase_botao_%s.png":

            style "apoiase_button"

            action OpenURL("https://apoia.se/geiko")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")








screen main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background


    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation









    textbutton _("Voltar"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("Sobre"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versão [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"





define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size











screen save():
    tag menu


    use file_slots(_("Salvar"))


screen load():
    tag menu


    use file_slots(_("Continuar"))


screen file_slots(title):

    if not renpy.android:

        default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Saves Automáticos"), quick=_("Outros Saves"))

        use game_menu(title):

            fixed:



                order_reverse True


                button:
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value


                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time} %d/%m/%y, %H:%M"), empty=_("espaço vazio")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)


                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")





                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")









screen preferences():
    tag menu


    use game_menu(_("Configurações"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Exibição")
                        textbutton _("Janela") action Preference("display", "window")
                        textbutton _("Tela Cheia") action Preference("display", "fullscreen")








                vbox:
                    style_prefix "check"
                    label _("Pular")
                    textbutton _("Texto") action Preference("skip", "toggle")
                    textbutton _("Escolhas") action Preference("after choices", "toggle")
                    textbutton _("Transições") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Velocidade do Texto")

                    bar value Preference("text speed")

                    label _("Tempo do Avanço Automático")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume da Música")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume dos Efeitos Sonoros")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume das Vozes")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mutar"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():
    tag menu



    predict False

    use game_menu(_("Histórico"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("Você ainda não começou o game :(")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Controles"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Controle") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Avança o diálogo e mostra a interface.")

    hbox:
        label _("Espaço")
        text _("Avança o diálogo sem fazer escolhas.")

    hbox:
        label _("Setas")
        text _("Navega pela interface.")

    hbox:
        label _("Esc")
        text _("Abre o menu do jogo.")

    hbox:
        label _("Ctrl")
        text _("Mantenha pressionado para Pular (defina o que pular na aba Opções).")

    hbox:
        label _("Tab")
        text _("Alterna entre as configurações do Pular.")

    hbox:
        label _("Page Up")
        text _("Retorna para o diálogo passado.")

    hbox:
        label _("Page Down")
        text _("Avança para o próximo diálogo já lido.")

    hbox:
        label "H"
        text _("Esconde a interface.")

    hbox:
        label "S"
        text _("Tira uma screenshot.")

    hbox:
        label "V"
        text _("Liga ou desliga a {a=https://www.renpy.org/l/voicing}voz automática de leitura{/a}.")


screen mouse_help():

    hbox:
        label _("LMB (Clique Esquerdo)")
        text _("Avança o diálogo e mostra a interface.")

    hbox:
        label _("MMB (Cique do Meio)")
        text _("Esconde a interface.")

    hbox:
        label _("RMB (Clique Direito)")
        text _("Abre o menu do jogo.")

    hbox:
        label _("Roda do Mouse Para Cima")
        text _("Retorna para o diálogo passado.")

    hbox:
        label _("Roda do Mouse Para Baixo")
        text _("Avança para o próximo diálogo já lido.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Sim") action yes_action
            textbutton _("Não") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 6

        text _("Pulando")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 450




screen quick_menu():
    variant "touch"
    zorder 200

    if show_quick_menu:

        vbox:
            style_prefix "quick"
            xalign 1.0
            yalign 0
            spacing 5

            hbox:
                style_prefix "quick"
                spacing 5
                imagebutton auto "extra/botao_voltar_%s.png" action Rollback()
                imagebutton auto "extra/botao_pular_%s.png" action Skip() alternate Skip(fast=True, confirm=False)
                imagebutton auto "extra/botao_salvar_%s.png" action ShowMenu('salvar')
                imagebutton auto "extra/botao_carregar_%s.png" action ShowMenu('carregar')
                imagebutton auto "extra/botao_esconder_%s.png" action [Hide("say"), Hide("choice"), SetVariable("show_quick_menu", False)]

            hbox:
                xalign 0.97

                vbox:
                    if tempo <= 1:
                        add "extra/tempo_1.png"
                    elif tempo == 2:
                        add "extra/tempo_2.png"
                    else:
                        add "extra/tempo_3.png"

                    frame:
                        xysize (50,50)
                        background Frame("extra/calendario.png")
                        text "[dia]" size 20 xalign 0.5 yalign 0.7

                imagebutton auto "extra/celular_menu_%s.png" action Show("menu_celular")

            imagebutton idle "extra/botao_geiko.webp":
                action OpenURL("https://www.linktr.ee/geikogames/")
                xalign 0.98

        frame:
            xalign 0.0
            yalign 1.0
            background None
            xpadding 20
            ypadding 20
            textbutton _("Cheats") style "touch_cheat_button" action Show('cheats_screen')

        frame:
            xalign 1.0
            yalign 1.0
            xpadding 10
            ypadding 5
            background None
            imagebutton auto "extra/botao_menu_%s.png" action ShowMenu("menu_novidades")

    elif not show_quick_menu and not proibido_salvar:

        imagemap:

            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Call("mostrar_janelas")

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style touch_cheat_button:
    variant "touch"
    background None
    hover_background Solid("#ffffff20")
    padding (10, 20)
    xalign 0.0

style touch_cheat_button_text:
    variant "touch"
    color "#ffffff"
    size 32
    outlines [(2, "#00000060", 0, 0)]

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
