













define config.default_music_volume = 0.5
define config.default_sfx_volume = 1.0
define config.has_autosave = False

define config.name = _("Celebrity Hunter")





define gui.show_name = False



define config.version = "0.93"

if renpy.android:
    define config.hard_rollback_limit = 30




define gui.about = _p("""\

Veja imagens exclusivas da próxima atualização no {a=https://www.instagram.com/geikogames/}Instagram{/a} ou no {a=https://www.facebook.com/celebrityhuntergame}Facebook{/a}.

{b}Celebrity Hunter{/b} é gratuito e mantido pela contribuição de seus jogadores.

Você pode ser o primeiro a jogar as novas atualizações. Leia mais em nosso {a=https://www.geiko.net}site{/a}.

{b}Você deve ter mais de 18 anos para jogar{/b}

Este jogo contém cenas de natureza sexual adequadas para maiores de 18 anos. Entretanto, elas são opcionais.

Deixamos o mais claro possível por meio de escolhas quando um acontecimento pode resultar em cenas picantes.

{b}Créditos{/b}

Criação e desenvolvimento: {b}RB{/b}.

Ícones: Paomedia e outros artistas em Iconfinder.

Música de abertura: Heart Afire por Defqwop.""")





define build.name = "CelebrityHunter"







define config.has_sound = True
define config.has_music = True
define config.has_voice = False

default preferences.skip_unseen = True























define config.enter_transition = dissolve
define config.exit_transition = dissolve



define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 200





default preferences.afm_time = 15
















define config.save_directory = "CelebrityHunter-1530304914"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')











define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm46rQUQXE5F17kbE7+he5BJ6FODP3fi5AHaH6w4Dpl+AN4wSIaXar9GOGRe6cn/1mq4FgkPdQyOiN9PkENwy0wxkYW+YISPPkxGLu1XY8BVF7VgI95+rlBzu1CzsPxzbb919lFP8Vkkp7q3BgdsG5qBK3piBIUuMfY/pD5+e5XJye/zYTnDpFAw7hSRipWKG8ZaGjgOHTDIKMDUNZkbA6Y90GhRqyEwYUDILju8TWb2tqFy7OLBurqTuvM9pGgne0CLUDnLcstrQbIPwvjwwIHHpnHxe+jnHi95bUhZWrQ/6xPQQeYPKc3MA1NyskLu7lQIxJD6UKuOHywjadozYKQIDAQAB"

define build.google_play_salt = (19, 7, -10, 3, 5, 45, 15, 07, 19, 88, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
