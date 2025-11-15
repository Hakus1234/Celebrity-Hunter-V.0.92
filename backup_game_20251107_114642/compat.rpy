init -999 python:
    import renpy
    from renpy import exports as _renpy_exports

    if not hasattr(renpy, "music"):
        try:
            from renpy.audio import music as _renpy_music
            renpy.music = _renpy_music
        except Exception:
            try:
                renpy.music = _renpy_exports.music
            except Exception:
                pass

    if not hasattr(renpy, "get_side_image"):
        try:
            renpy.get_side_image = _renpy_exports.get_side_image
        except Exception:
            try:
                from renpy.display import image as _renpy_image
                renpy.get_side_image = _renpy_image.get_side_image
            except Exception:
                pass

    if not hasattr(renpy, "has_screen"):
        try:
            renpy.has_screen = _renpy_exports.has_screen
        except Exception:
            pass

    if not hasattr(renpy, "load_module"):
        try:
            renpy.load_module = _renpy_exports.load_module
        except Exception:
            pass

    if not hasattr(renpy, "get_mode"):
        try:
            renpy.get_mode = _renpy_exports.get_mode
        except Exception:
            pass

    if not hasattr(renpy, "has_label"):
        try:
            renpy.has_label = _renpy_exports.has_label
        except Exception:
            pass

    if not hasattr(renpy, "context"):
        try:
            renpy.context = _renpy_exports.context
        except Exception:
            pass

    if not hasattr(renpy, "variant"):
        try:
            renpy.variant = _renpy_exports.variant
        except Exception:
            pass

    if not hasattr(renpy, "sound"):
        try:
            from renpy.audio import sound as _renpy_sound
            renpy.sound = _renpy_sound
        except Exception:
            try:
                renpy.sound = _renpy_exports.sound
            except Exception:
                pass

    if not hasattr(renpy, "list_files"):
        try:
            renpy.list_files = _renpy_exports.list_files
        except Exception:
            pass

    if not hasattr(renpy, "can_fullscreen"):
        try:
            renpy.can_fullscreen = _renpy_exports.can_fullscreen
        except Exception:
            pass

    if not hasattr(renpy, "get_screen"):
        try:
            renpy.get_screen = _renpy_exports.get_screen
        except Exception:
            pass

    if not hasattr(renpy, "has_image"):
        try:
            renpy.has_image = _renpy_exports.has_image
        except Exception:
            pass
    if not hasattr(renpy, "image"):
        try:
            renpy.image = _renpy_exports.image
        except Exception:
            pass

    if not hasattr(renpy, "predict_screen"):
        try:
            renpy.predict_screen = _renpy_exports.predict_screen
        except Exception:
            pass
    if not hasattr(renpy, "execute_default_statement"):
        try:
            renpy.execute_default_statement = _renpy_exports.execute_default_statement
        except Exception:
            pass

    if not hasattr(renpy, "restart_interaction"):
        try:
            renpy.restart_interaction = _renpy_exports.restart_interaction
        except Exception:
            pass
    if not hasattr(renpy, "change_language"):
        try:
            renpy.change_language = _renpy_exports.change_language
        except Exception:
            pass
    if not hasattr(renpy, "start_predict_screen"):
        try:
            renpy.start_predict_screen = _renpy_exports.start_predict_screen
        except Exception:
            pass
    if not hasattr(renpy, "block_rollback"):
        try:
            renpy.block_rollback = _renpy_exports.block_rollback
        except Exception:
            pass
    if not hasattr(renpy, "get_filename_line"):
        try:
            renpy.get_filename_line = _renpy_exports.get_filename_line
        except Exception:
            pass
    for _name in dir(_renpy_exports):
        if _name.startswith('_'):
            continue
        if hasattr(renpy, _name):
            continue
        try:
            setattr(renpy, _name, getattr(_renpy_exports, _name))
        except Exception:
            pass
    for _name in ("rollback", "menu", "say"):
        exported = getattr(_renpy_exports, _name, None)
        current = getattr(renpy, _name, None)
        if exported is not None and (current is None or not callable(current)):
            setattr(renpy, _name, exported)

