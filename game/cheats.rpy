init python:
    from renpy import exports as renpy_exports
    import renpy.store as _store
    from renpy.store import persistent

    class _CheatError(Exception):
        pass

    CHEAT_RESOURCES = [
        ("Cash", "cash", 1000, (0, 50000)),
        ("Coins", "persistent.coins", 1000, (0, 50000)),
        ("Credito Atual", "credito", 500, (0, 50000)),
        ("Credito Total", "credito_total", 500, (0, 50000)),
        ("MC Fisico", "mc_fisico", 5, (0, 500)),
    ]

    CHEAT_PROGRESS = [
        ("EP Pontos", "ep_pontos", 1, (0, 999)),
        ("Natasha Pontos", "natasha_pontos", 1, (0, 999)),
        ("Bao Pontos", "bao_pontos", 1, (0, 999)),
        ("Bao Evento", "bao_evento", 1, (0, 10)),
        ("Dia Bao", "dia_bao", 1, (0, 31)),
        ("Priscila Evento Amizade", "priscila_amizade_evento", 1, (0, 99)),
        ("Priscila Evento Seducao", "priscila_seducao_evento", 1, (0, 99)),
        ("Sayuri Evento Amizade", "sayuri_amizade_evento", 1, (0, 99)),
        ("Sayuri Evento Seducao", "sayuri_seducao_evento", 1, (0, 99)),
        ("Julia Evento Seducao", "julia_seducao_evento", 1, (0, 99)),
        ("Nathan Evento Amizade", "nathan_amizade_evento", 1, (0, 99)),
        ("Pixie Evento Amizade", "pixie_amizade_evento", 1, (0, 99)),
        ("Pixie Evento Seducao", "pixie_seducao_evento", 1, (0, 99)),
    ]

    CHEAT_RELATIONSHIPS = [
        ("Priscila Amizade", "priscila_amizade", 1, (0, 7)),
        ("Priscila Seducao", "priscila_seducao", 1, (0, 7)),
        ("Sayuri Amizade", "sayuri_amizade", 1, (0, 22)),
        ("Sayuri Seducao", "sayuri_seducao", 1, (0, 22)),
        ("Pixie Amizade", "pixie_amizade", 1, (0, 20)),
        ("Pixie Seducao", "pixie_seducao", 1, (0, 20)),
        ("Nathan Amizade", "nathan_amizade", 1, (0, 10)),
        ("Julia Seducao", "julia_seducao", 1, (0, 13)),
        ("Sofia Amizade", "sofia_amizade", 1, (0, 25)),
        ("Natasha Seducao", "natasha_seducao", 1, (0, 25)),
        ("Diana Seducao", "diana_seducao", 1, (0, 25)),
        ("Karli Seducao", "karli_seducao", 1, (0, 25)),
        ("Maria Seducao", "maria_seducao", 1, (0, 25)),
        ("Miranda Seducao", "miranda_seducao", 1, (0, 25)),
        ("Atendente Seducao", "atendente_seducao", 1, (0, 25)),
        ("Roxane Seducao", "roxane_seducao", 1, (0, 25)),
        ("Quincy Amizade", "quincy_amizade", 1, (0, 25)),
        ("Hacker Amizade", "hacker_amizade", 1, (0, 25)),
        ("Shoshana Amizade", "shoshana_amizade", 1, (0, 25)),
        ("Pixel Amizade", "pixel_amizade", 1, (0, 25)),
        ("Naru Amizade", "naru_amizade", 1, (0, 25)),
    ]

    CHEAT_TOGGLES = [
        ("Bao Introducao", "bao_introducao"),
        ("Thaynara Amizade", "thaynara_amizade"),
        ("Cassia Seducao", "cassia_seducao"),
        ("Liling Seducao", "liling_seducao"),
        ("NA3 Seducao", "na3_seducao"),
        ("H1 Seducao", "h1_seducao"),
        ("Apoiador", "persistent.apoiador"),
        ("Banned", "persistent.banned"),
        ("Daily Recompensa", "persistent.daily"),
    ]

    def cheat_display(var_path):
        try:
            value = cheat_get_value(var_path, 0)
        except _CheatError:
            value = "?"
        if isinstance(value, bool):
            return "ON" if value else "OFF"
        return str(value)
    def _cheat_resolve_path(var_path):
        var_path = var_path.strip()
        if not var_path:
            raise _CheatError("Nome da variavel vazio.")
        if var_path.startswith("persistent."):
            base = persistent
            attr = var_path.split(".", 1)[1]
        else:
            base = _store
            attr = var_path
        if not attr:
            raise _CheatError("Caminho invalido: {}".format(var_path))
        return base, attr

    def cheat_get_value(var_path, default=0):
        try:
            base, attr = _cheat_resolve_path(var_path)
            return getattr(base, attr)
        except _CheatError:
            raise
        except Exception:
            return default

    def cheat_set_value(var_path, value, clamp=None):
        base, attr = _cheat_resolve_path(var_path)
        if clamp is not None:
            lo, hi = clamp
            if lo is not None:
                value = max(lo, value)
            if hi is not None:
                value = min(hi, value)
        setattr(base, attr, value)
        renpy_exports.restart_interaction()
        renpy_exports.notify(u"{} = {}".format(var_path, value))

    def cheat_delta(var_path, amount, clamp=None):
        value = cheat_get_value(var_path, 0)
        if isinstance(value, bool):
            value = int(value)
        try:
            numeric = float(value)
        except Exception:
            numeric = 0
        numeric += amount
        if clamp is not None:
            lo, hi = clamp
            if lo is not None:
                numeric = max(lo, numeric)
            if hi is not None:
                numeric = min(hi, numeric)
        if isinstance(value, int):
            numeric = int(numeric)
        cheat_set_value(var_path, numeric, clamp=clamp)

    def cheat_toggle(var_path):
        value = cheat_get_value(var_path, False)
        cheat_set_value(var_path, not bool(value))

    def cheat_unlock_cards():
        total = 0
        for attr in dir(persistent):
            if attr.startswith("card_"):
                setattr(persistent, attr, True)
                total += 1
        renpy_exports.restart_interaction()
        renpy_exports.notify(u"Cartas liberadas ({})".format(total))

    def cheat_unlock_gallery():
        total = 0
        for attr in dir(persistent):
            if attr.endswith("_cena") or attr.startswith("garota_") or attr.startswith("priscila_cena") or attr.startswith("julia_cena"):
                try:
                    setattr(persistent, attr, True)
                    total += 1
                except Exception:
                    continue
        renpy_exports.restart_interaction()
        renpy_exports.notify(u"Cenas liberadas ({})".format(total))

    def cheat_clear_bans():
        persistent.banned = False
        persistent.daily = True
        renpy_exports.restart_interaction()
        renpy_exports.notify(u"Banimentos/cheques limpos.")

    def cheat_prompt_custom():
        try:
            name = renpy_exports.input("Nome da variavel (ex.: cash ou persistent.coins):", default="")
            if not name:
                renpy_exports.notify("Cancelado.")
                return
            value_text = renpy_exports.input("Novo valor para {}:".format(name), default="")
            if value_text is None:
                renpy_exports.notify("Cancelado.")
                return
            value_text = value_text.strip()
            if value_text.lower() in ("true", "verdadeiro"):
                value = True
            elif value_text.lower() in ("false", "falso"):
                value = False
            else:
                try:
                    value = int(value_text)
                except ValueError:
                    try:
                        value = float(value_text)
                    except ValueError:
                        value = value_text
            cheat_set_value(name, value)
        except _CheatError as exc:
            renpy_exports.notify(str(exc))

    def _set_flag(flag, value=True):
        for namespace in (_store, persistent):
            if hasattr(namespace, flag):
                current = getattr(namespace, flag)
                target = value
                if isinstance(current, bool):
                    target = bool(value)
                elif isinstance(current, (int, float)):
                    if isinstance(value, (int, float)) and not isinstance(value, bool):
                        target = value
                    else:
                        target = 999
                else:
                    target = value
                setattr(namespace, flag, target)

    def cheat_unlock_suits():
        suit_flags = [
            'roupa_blacktie', 'roupa_blazer', 'roupa_nathan',
            'd2_blacktie', 'd2_blazer', 'j4_blazer', 'n6_blazer'
        ]
        for flag in suit_flags:
            _set_flag(flag)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Ternos liberados!')

    def cheat_unlock_exploration():
        exploration_flags = [
            'fado_m4sangue', 'fado_caverna', 'fado_1vez', 'fado_convite',
            'fado_caverna_inv', 'fado_caverna_gate', 'fado_caverna_guardado',
            'fado_caverna_open', 'fado_caverna_sombra',
            'fang_treino', 'fang_guardado', 'fang_armado',
            'julia_fad_reuniao', 'julia_fad_sangue', 'julia_fad_investigacao',
            'fado_mapa1', 'fado_mapa2', 'fado_mapa3', 'fado_mapa4',
            'fado_cel_estudos', 'fado_convite',
            'mc_fisico', 'mc_forca', 'mc_sprint', 'ftempo', 'checatempo',
            'daily_collected', 'fang_convite', 'fado_convite_lido'
        ]
        fado_flags = [
            'fado_m1a1', 'fado_m1a2', 'fado_m1a3', 'fado_m1a4', 'fado_m1a5', 'fado_m1a6',
            'fado_m2a1', 'fado_m2a2', 'fado_m2a3', 'fado_m2a4', 'fado_m2a6',
            'fado_m3a1', 'fado_m3a2', 'fado_m3a3', 'fado_m3a4', 'fado_m3a5', 'fado_m3a7',
            'fado_m4a1', 'fado_m4a2', 'fado_m4a3',
            'fado_m1nota', 'fado_m2nota', 'fado_m3nota',
            'fado_m2cristal', 'fado_m3pedra', 'fado_m4sangue',
            'fado_precisa_maca', 'fado_maca', 'fado_faloumaca', 'fado_pixel_comeu'
        ]
        pixel_flags = [
            'pixel_amizade', 'pixel_evento', 'pixel_encontro',
            'pixel_maca', 'pixel_perguntou', 'pixel_conversa1vez'
        ]
        for namespace in (_store, persistent):
            for flag in exploration_flags + fado_flags + pixel_flags:
                if hasattr(namespace, flag):
                    current = getattr(namespace, flag)
                    if isinstance(current, bool):
                        setattr(namespace, flag, True)
                    elif isinstance(current, (int, float)):
                        setattr(namespace, flag, 999)
                    else:
                        setattr(namespace, flag, current)
        persistent.daily = True
        persistent.daily_collected = True
        renpy_exports.restart_interaction()
        renpy_exports.notify('Exploracoes liberadas!')

    def cheat_max_relationships():
        for _, var_path, _, clamp in CHEAT_RELATIONSHIPS:
            target = 999
            if clamp and len(clamp) > 1 and clamp[1] is not None:
                target = clamp[1]
            cheat_set_value(var_path, target, clamp)

    def cheat_unlock_characters():
        character_flags = {
            'priscila_e1': 'seducao',
            'sayuri_evento1_check': False,
            'v2_fim': True,
            'nathan_e1': 'seducao',
            'sayuri_e2': 'seducao',
            'diana_e1': 'seducao',
            'sofia_e1': 'seducao',
            'natasha_e1': 'seducao',
            'mc_massagem': 10,
            'thaynara_evento': 5,
            'stifler_e1': 'seducao',
            'maria_evento': 5,
            'quincy_e1': True,
            'banho_evento': 5,
            'v39_fim': True,
            'quincy_evento': 5,
            'fado_pixel_comeu': True,
            'ana_evento': 5,
            'tkf_evento1': True,
            'v30_fim': True
        }
        for flag, value in character_flags.items():
            _set_flag(flag, value)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Personagens liberados!')

    def cheat_unlock_finals():
        final_flags = [
            'diana_final1', 'diana_final2', 'diana_final3',
            'nathan_final1', 'nathan_final2', 'nathan_final3',
            'sayuri_final1', 'sayuri_final2', 'sayuri_final3',
            'julia_final1', 'julia_final2', 'julia_final3',
            'sofia_final2', 'sofia_final3'
        ]
        for flag in final_flags:
            _set_flag(flag, True)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Finais liberados!')

    def cheat_unlock_replays():
        replay_flags = [
            'priscila_cena1', 'priscila_cena2', 'priscila_cena3', 'priscila_cena4',
            'priscila_cena5', 'priscila_cena6', 'priscila_cena7', 'priscila_cena8',
            'priscila_cena9', 'priscila_cena10', 'priscila_cena11', 'priscila_cena12',
            'priscila_cena13', 'priscila_cena14', 'priscila_cena15',
            'priscila_cena16', 'priscila_cena17'
        ]
        for flag in replay_flags:
            _set_flag(flag, True)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Relembrar encontros liberado!')

    def cheat_unlock_pautas():
        pauta_flags = {
            'pauta_cassia': 999,
            'pauta_cassia_db': 999,
            'pautas': 999,
            'entregou_pauta': 999,
            'pauta_1vez': True,
            'favor_cassia_pauta': True,
            'pauta_fabricio': True,
            'hora_pauta': True,
            'pautas_liberado': True
        }
        for flag, value in pauta_flags.items():
            _set_flag(flag, value)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Pautas liberadas!')

    def cheat_unlock_car():
        car_flags = {
            'carro': True,
            'carro_evento': 999,
            'carro_gina': 999
        }
        for flag, value in car_flags.items():
            _set_flag(flag, value)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Carro liberado!')

    def cheat_unlock_house():
        house_flags = {
            'casa': True,
            'casa_comprada': True,
            'compra_casa_evento': True,
            'dormir_em_casa': True,
            'karli_casa': True,
            'xiang_casa': True,
            'xiang_casa_evento': 999,
            'k7_poscasa': True,
            'sem_casa': False
        }
        for flag, value in house_flags.items():
            _set_flag(flag, value)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Casa liberada!')

    def cheat_reset_progress():
        reset_lists = CHEAT_RESOURCES + CHEAT_PROGRESS + CHEAT_RELATIONSHIPS
        for _, var_path, _, clamp in reset_lists:
            target = 0
            if clamp and len(clamp) > 0 and clamp[0] is not None:
                target = clamp[0]
            cheat_set_value(var_path, target, clamp)
        for _, var_path in CHEAT_TOGGLES:
            cheat_set_value(var_path, False)
        renpy_exports.restart_interaction()
        renpy_exports.notify('Valores restaurados aos minimos.')


    CHEAT_UNLOCKERS = [
        ("Liberar todas as cartas", cheat_unlock_cards),
        ("Ativar todos os ternos", cheat_unlock_suits),
        ("Resetar valores principais", cheat_reset_progress),
        ("Liberacao completa de personagens", cheat_unlock_characters),
        ("Liberar finais", cheat_unlock_finals),
        ("Liberar relembrar encontros", cheat_unlock_replays),
        ("Liberar pautas", cheat_unlock_pautas),
        ("Liberar exploracoes", cheat_unlock_exploration),
        ("Liberar casa", cheat_unlock_house),
        ("Liberar carro", cheat_unlock_car),
        ("Liberar cenas ou galeria", cheat_unlock_gallery),
        ("Limpar verificacoes de banimento", cheat_clear_bans),
        ("Editar variavel manualmente...", cheat_prompt_custom),
    ]


style cheats_panel_frame:
    background Solid("#1a001acc")
    padding (30, 30)
    xsize 920
    ysize 600
    align (0.5, 0.5)

style cheats_title_text:
    color "#ff4fa6"
    size 40
    xalign 0.5

style cheats_value_text:
    color "#ffffff"
    size 22

style cheats_button:
    background Solid("#ff4fa6")
    padding (6, 14)
    hover_background Solid("#ff6fbc")
    insensitive_background Solid("#888888")

style cheats_button_text:
    color "#0b0b0b"
    size 18


screen cheats_screen():
    modal True
    tag cheats
    zorder 200

    add Solid("#000000a4")

    frame:
        style "cheats_panel_frame"

        vbox:
            spacing 20

            text "Cheats" style "cheats_title_text"

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                yinitial 0.0

                vbox:
                    spacing 12

                    for entry_title, var_path, step, clamp in CHEAT_RESOURCES + CHEAT_PROGRESS + CHEAT_RELATIONSHIPS:
                        $ current_val = cheat_display(var_path)
                        hbox:
                            spacing 12
                            text "{}: {}".format(entry_title, current_val) style "cheats_value_text"
                            textbutton "+{}".format(step) style "cheats_button" action Function(cheat_delta, var_path, step, clamp)
                            textbutton "-{}".format(step) style "cheats_button" action Function(cheat_delta, var_path, -step, clamp)
                            if clamp and len(clamp) > 1 and clamp[1] is not None:
                                textbutton "MAX" style "cheats_button" action Function(cheat_set_value, var_path, clamp[1], clamp)

                    null height 12

                    for entry_title, var_path in CHEAT_TOGGLES:
                        $ current_val = cheat_display(var_path)
                        hbox:
                            spacing 12
                            text "{}: {}".format(entry_title, current_val) style "cheats_value_text"
                            textbutton "Toggle" style "cheats_button" action Function(cheat_toggle, var_path)

                    null height 12

                    for entry_title, fn in CHEAT_UNLOCKERS:
                        textbutton entry_title style "cheats_button" action Function(fn)

            textbutton "Close" style "cheats_button" action Hide("cheats_screen")
