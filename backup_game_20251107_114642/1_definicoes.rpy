init python:
    import random
    import time
    import renpy.store as _store

    class _OfflinePythonSDLActivity:
        def __init__(self):
            self._store = _store
            self._ensure_unlocks()

        def _ensure_unlocks(self):
            self._store.userlogado = True
            self._store.persistent.apoiador = True
            self._store.persistent.banned = False
            if not hasattr(self._store.persistent, "coins"):
                self._store.persistent.coins = 50
            if not hasattr(self._store, "cash"):
                self._store.cash = 0
            if not hasattr(self._store, "credito"):
                self._store.credito = 0

        def iniciaVariaveis(self):
            self._ensure_unlocks()

        def registraEvento(self, *args, **kwargs):
            return None

        def abreLogin(self, *args, **kwargs):
            self._ensure_unlocks()
            return True

        def pegaLogado(self, *args, **kwargs):
            self._ensure_unlocks()
            return True

        def pegaBacker(self, *args, **kwargs):
            self._ensure_unlocks()
            return True

        def pegaBanned(self, *args, **kwargs):
            self._store.persistent.banned = False
            return False

        def pegaEmail(self, *args, **kwargs):
            email = getattr(self._store, "useremail", None)
            if not email:
                email = "player@offline"
                self._store.useremail = email
            return email

        def pegaUid(self, *args, **kwargs):
            uid = getattr(self._store.persistent, "uid", None)
            if not uid:
                uid = "offline-uid"
                self._store.persistent.uid = uid
            return uid

        def pegaMoedas(self, *args, **kwargs):
            return getattr(self._store.persistent, "coins", 0)

        def usaMoedas(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            coins = getattr(self._store.persistent, "coins", 0)
            if valor > 0:
                coins = max(0, coins - valor)
                self._store.persistent.coins = coins
            return coins

        def addCoins(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            coins = getattr(self._store.persistent, "coins", 0) + max(0, valor)
            self._store.persistent.coins = coins
            return coins

        def pegaCredito(self, *args, **kwargs):
            return getattr(self._store, "credito", 0)

        def addCredito(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            credito = getattr(self._store, "credito", 0) + max(0, valor)
            self._store.credito = credito
            return credito

        def trocaCredito(self, *args, **kwargs):
            return self.pegaCredito()

        def pegaCreditoTotal(self, *args, **kwargs):
            return self.pegaCredito()

        def pegaCash(self, *args, **kwargs):
            return getattr(self._store, "cash", 0)

        def ganhaCash(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            cash = getattr(self._store, "cash", 0) + max(0, valor)
            self._store.cash = cash
            return cash

        def usaCash(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            cash = getattr(self._store, "cash", 0)
            if valor > 0:
                cash = max(0, cash - valor)
                self._store.cash = cash
            return cash

        def pegaLivros(self, *args, **kwargs):
            return 999

        def addLivros(self, *args, **kwargs):
            return 999

        def pegaGuia1(self, *args, **kwargs):
            self._store.persistent.guia1 = True
            return True

        def compraGuia1(self, *args, **kwargs):
            self._store.persistent.guia1 = True
            return True

        def pegaFpontos(self, *args, **kwargs):
            return getattr(self._store, "mc_fisico", 0)

        def addFpontos(self, quantidade=0, *args, **kwargs):
            valor = quantidade or (args[0] if args else 0) or kwargs.get("quantidade", 0)
            try:
                valor = int(valor)
            except Exception:
                valor = 0
            pontos = getattr(self._store, "mc_fisico", 0) + max(0, valor)
            self._store.mc_fisico = pontos
            return pontos

        def maisMpontos(self, *args, **kwargs):
            return 999

        def pegaMpontos(self, *args, **kwargs):
            return 999

        def loadVID(self, value):
            if not value:
                value = "VID-OFFLINE"
            self._store.persistent.vid = value
            return value

        def pegaVID(self, *args, **kwargs):
            vid = self._store.persistent.vid or "VID-OFFLINE"
            self._store.persistent.vid = vid
            return vid

        def loadAD(self, *args, **kwargs):
            return False

        def pegaAnuncio(self, *args, **kwargs):
            return False

        def salvaJogo(self, *args, **kwargs):
            return None

        def carregaJogo(self, *args, **kwargs):
            return None

        def salvaHist(self, *args, **kwargs):
            return None

        def setaSalvado(self, *args, **kwargs):
            return True

        def pegaSalvado(self, *args, **kwargs):
            return True

        def setDaily(self, *args, **kwargs):
            self._store.persistent.daily = True
            return True

        def checkDailyNext(self, *args, **kwargs):
            return True

        def tempoAgora(self, *args, **kwargs):
            return int(time.time())

        def __getattr__(self, name):
            if name.startswith("pegaCarta"):
                return lambda *args, **kwargs: True
            if name.startswith("ganhaCarta"):
                return lambda *args, **kwargs: True
            if name.startswith("compra"):
                return lambda *args, **kwargs: True
            if name.startswith("pegaPraia"):
                return lambda *args, **kwargs: True
            if name.startswith(("set", "add", "acerta", "avanca", "seta", "mais", "libera", "ganha", "load")):
                return lambda *args, **kwargs: True
            if name.startswith("check"):
                return lambda *args, **kwargs: True
            if name.startswith("pega"):
                return lambda *args, **kwargs: True
            return lambda *args, **kwargs: None

    PythonSDLActivity = _OfflinePythonSDLActivity()

    def prompt_store_input(var_name, prompt, length=15, allow=None):
        def _inner():
            current_value = getattr(store, var_name, "")
            new_value = renpy.input(prompt, default=current_value, length=length, allow=allow)
            if new_value is None:
                return
            new_value = new_value.strip()
            if not new_value:
                return
            setattr(store, var_name, new_value)

        renpy.invoke_in_new_context(_inner)
        renpy.restart_interaction()

    def prompt_store_input(var_name, prompt, length=15, allow=None):
        def _inner():
            current_value = getattr(_store, var_name, "")
            new_value = renpy.input(prompt, default=current_value, length=length, allow=allow)
            if new_value is None:
                return
            new_value = new_value.strip()
            if not new_value:
                return
            setattr(_store, var_name, new_value)

        renpy.invoke_in_new_context(_inner)
        renpy.restart_interaction()

    renpy.music.register_channel('Musica', mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)




    if renpy.android:
        config.has_autosave = False
        config.has_quicksave = False
        config.autosave_on_choice = False

    PythonSDLActivity.iniciaVariaveis()



    sayuri_final1_img = im.Scale("sayuri9_mc1.webp", 257, 145)
    sayuri_final2_img = im.Scale("sayuri_final20.webp", 257, 145)
    sayuri_final3_img = im.Scale("sayuri_final3_img2.webp", 257, 145)

    julia_final1_img = im.Scale("j8_mc_jogando2.webp", 257, 145)
    julia_final2_img = im.Scale("j8_final20.webp", 257, 145)
    julia_final3_img = im.Scale("julia_final3_img4.webp", 257, 145)

    diana_final1_img = im.Scale("diana7_img65.webp", 257, 145)
    diana_final2_img = im.Scale("diana7_img86.webp", 257, 145)
    diana_final3_img = im.Scale("diana7_img93.webp", 257, 145)

    nathan_final1_img = im.Scale("n8i74.webp", 257, 145)
    nathan_final2_img = im.Scale("n8i79.webp", 257, 145)
    nathan_final3_img = im.Scale("n8n9.webp", 257, 145)

    diana_encontro7_img = im.Scale("diana7_img11.webp", 257, 145)
    nathan_encontro8_img = im.Scale("n8_img17.webp", 257, 145)
    sofia_encontro6_img = im.Scale("sofiaf5.webp", 257, 145)



image ani01 = Movie(play="ani01.webm")
image ani02 = Movie(play="ani02.webm")
image ani03 = Movie(play="ani03.webm")
image ani04 = Movie(play="ani04.webm")
image ani05 = Movie(play="ani05.webm")
image ani06 = Movie(play="ani06.webm")
image ani07 = Movie(play="ani07.webm")
image ani08 = Movie(play="ani08.webm")
image ani09 = Movie(play="ani09.webm")
image ani10 = Movie(play="ani10.webm")
image ani11 = Movie(play="ani11.webm")
image ani12 = Movie(play="ani12.webm")
image ani13 = Movie(play="ani13.webm")
image ani14 = Movie(play="ani14.webm")
image ani15 = Movie(play="ani15.webm")
image ani16 = Movie(play="ani16.webm")
image ani17 = Movie(play="ani17.webm")
image ani18 = Movie(play="ani18.webm")
image ani19 = Movie(play="ani19.webm")
image ani20 = Movie(play="ani20.webm")
image ani21 = Movie(play="ani21.webm")

image n8i49 = Movie(play="n8_ani1.webm")
image n8i50 = Movie(play="n8_ani2.webm")
image n8i69 = Movie(play="ani25.webm")
image n8i71 = Movie(play="ani22.webm")
image n8i72 = Movie(play="ani23.webm")



image ani22 = Movie(play="/images/ani/ch_ani22.webm")
image ani23 = Movie(play="/images/ani/ch_ani23.webm")
image ani24 = Movie(play="/images/ani/ch_ani24.webm")
image ani25 = Movie(play="/images/ani/ch_ani25.webm")
image ani26 = Movie(play="/images/ani/ch_ani26.webm")
image ani27 = Movie(play="/images/ani/ch_ani27.webm")
image ani28 = Movie(play="/images/ani/ch_ani28.webm")
image ani29 = Movie(play="/images/ani/ch_ani29.webm")
image ani30 = Movie(play="/images/ani/ch_ani30.webm")
image ani31 = Movie(play="/images/ani/ch_ani31.webm")
image ani32 = Movie(play="/images/ani/ch_ani32.webm")
image ani33 = Movie(play="/images/ani/ch_ani33.webm")
image ani34 = Movie(play="/images/ani/ch_ani34.webm")
image ani35 = Movie(play="/images/ani/ch_ani35.webm")
image ani36 = Movie(play="/images/ani/ch_ani36.webm")
image ani37 = Movie(play="/images/ani/ch_ani37.webm")
image ani38 = Movie(play="/images/ani/ch_ani38.webm")
image ani39 = Movie(play="/images/ani/ch_ani39.webm")
image ani40 = Movie(play="/images/ani/ch_ani40.webm")
image ani41 = Movie(play="/images/ani/ch_ani41.webm")
image ani42 = Movie(play="/images/ani/ch_ani42.webm")
image ani43 = Movie(play="/images/ani/ch_ani43.webm")
image ani44 = Movie(play="/images/ani/ch_ani44.webm")
image ani45 = Movie(play="/images/ani/ch_ani45.webm")
image ani46 = Movie(play="/images/ani/ch_ani46.webm")
image ani47 = Movie(play="/images/ani/ch_ani47.webm")
image ani48 = Movie(play="/images/ani/ch_ani48.webm")
image ani49 = Movie(play="/images/ani/ch_ani49.webm")
image ani50 = Movie(play="/images/ani/ch_ani50.webm")

image dnew_ani01 = Movie(play="images/new/diana/dnew_ani01.webm", size = (1280, 720))
image dnew_ani02 = Movie(play="images/new/diana/dnew_ani02.webm", size = (1280, 720))
image dnew_ani03 = Movie(play="images/new/diana/dnew_ani03.webm", size = (1280, 720))
image dnew_ani04 = Movie(play="images/new/diana/dnew_ani04.webm", size = (1280, 720))
image dnew_ani05 = Movie(play="images/new/diana/dnew_ani05.webm", size = (1280, 720))
image dnew_ani06 = Movie(play="images/new/diana/dnew_ani06.webm", size = (1280, 720))
image dnew_ani07 = Movie(play="images/new/diana/dnew_ani07.webm", size = (1280, 720))
image dnew_ani08 = Movie(play="images/new/diana/dnew_ani08.webm", size = (1280, 720))
image dnew_ani09 = Movie(play="images/new/diana/dnew_ani09.webm", size = (1280, 720))
image dnew_ani10 = Movie(play="images/new/diana/dnew_ani10.webm", size = (1280, 720))
image dnew_ani11 = Movie(play="images/new/diana/dnew_ani11.webm", size = (1280, 720))
image dnew_ani12 = Movie(play="images/new/diana/dnew_ani12.webm", size = (1280, 720))
image dnew_ani13 = Movie(play="images/new/diana/dnew_ani13.webm", size = (1280, 720))
image dnew_ani14 = Movie(play="images/new/diana/dnew_ani14.webm", size = (1280, 720))
image dnew_ani15 = Movie(play="images/new/diana/dnew_ani15.webm", size = (1280, 720))
image dnew_ani16 = Movie(play="images/new/diana/dnew_ani16.webm", size = (1280, 720))
image dnew_ani17 = Movie(play="images/new/diana/dnew_ani17.webm", size = (1280, 720))
image dnew_ani18 = Movie(play="images/new/diana/dnew_ani18.webm", size = (1280, 720))

image jnew_ani01 = Movie(play="images/new/julia/jnew_ani01.webm", size = (1280, 720))
image jnew_ani02 = Movie(play="images/new/julia/jnew_ani02.webm", size = (1280, 720))
image jnew_ani03 = Movie(play="images/new/julia/jnew_ani03.webm", size = (1280, 720))
image jnew_ani04 = Movie(play="images/new/julia/jnew_ani04.webm", size = (1280, 720))
image jnew_ani05 = Movie(play="images/new/julia/jnew_ani05.webm", size = (1280, 720))
image jnew_ani06 = Movie(play="images/new/julia/jnew_ani06.webm", size = (1280, 720))
image jnew_ani07 = Movie(play="images/new/julia/jnew_ani07.webm", size = (1280, 720))
image jnew_ani08 = Movie(play="images/new/julia/jnew_ani08.webm", size = (1280, 720))
image jnew_ani09 = Movie(play="images/new/julia/jnew_ani09.webm", size = (1280, 720))
image jnew_ani10 = Movie(play="images/new/julia/jnew_ani10.webm", size = (1280, 720))
image jnew_ani11 = Movie(play="images/new/julia/jnew_ani11.webm", size = (1280, 720))
image jnew_ani12 = Movie(play="images/new/julia/jnew_ani12.webm", size = (1280, 720))
image jnew_ani13 = Movie(play="images/new/julia/jnew_ani13.webm", size = (1280, 720))
image jnew_ani14 = Movie(play="images/new/julia/jnew_ani14.webm", size = (1280, 720))
image jnew_ani15 = Movie(play="images/new/julia/jnew_ani15.webm", size = (1280, 720))
image jnew_ani16 = Movie(play="images/new/julia/jnew_ani16.webm", size = (1280, 720))
image jnew_ani17 = Movie(play="images/new/julia/jnew_ani17.webm", size = (1280, 720))
image jnew_ani18 = Movie(play="images/new/julia/jnew_ani18.webm", size = (1280, 720))
image jnew_ani19 = Movie(play="images/new/julia/jnew_ani19.webm", size = (1280, 720))
image jnew_ani20 = Movie(play="images/new/julia/jnew_ani20.webm", size = (1280, 720))
image jnew_ani21 = Movie(play="images/new/julia/jnew_ani21.webm", size = (1280, 720))
image jnew_ani22 = Movie(play="images/new/julia/jnew_ani22.webm", size = (1280, 720))
image jnew_ani23 = Movie(play="images/new/julia/jnew_ani23.webm", size = (1280, 720))
image jnew_ani24 = Movie(play="images/new/julia/jnew_ani24.webm", size = (1280, 720))
image jnew_ani25 = Movie(play="images/new/julia/jnew_ani25.webm", size = (1280, 720))
image jnew_ani26 = Movie(play="images/new/julia/jnew_ani26.webm", size = (1280, 720))
image jnew_ani27 = Movie(play="images/new/julia/jnew_ani27.webm", size = (1280, 720))
image jnew_ani28 = Movie(play="images/new/julia/jnew_ani28.webm", size = (1280, 720))
image jnew_ani29 = Movie(play="images/new/julia/jnew_ani29.webm", size = (1280, 720))
image jnew_ani30 = Movie(play="images/new/julia/jnew_ani30.webm", size = (1280, 720))
image jnew_ani31 = Movie(play="images/new/julia/jnew_ani31.webm", size = (1280, 720))
image jnew_ani32 = Movie(play="images/new/julia/jnew_ani32.webm", size = (1280, 720))
image jnew_ani33 = Movie(play="images/new/julia/jnew_ani33.webm", size = (1280, 720))

image nnew_ani01 = Movie(play="images/new/nathan/nnew_ani01.webm", size = (1280, 720))
image nnew_ani02 = Movie(play="images/new/nathan/nnew_ani02.webm", size = (1280, 720))
image nnew_ani03 = Movie(play="images/new/nathan/nnew_ani03.webm", size = (1280, 720))
image nnew_ani04 = Movie(play="images/new/nathan/nnew_ani04.webm", size = (1280, 720))
image nnew_ani05 = Movie(play="images/new/nathan/nnew_ani05.webm", size = (1280, 720))
image nnew_ani06 = Movie(play="images/new/nathan/nnew_ani06.webm", size = (1280, 720))
image nnew_ani07 = Movie(play="images/new/nathan/nnew_ani07.webm", size = (1280, 720))
image nnew_ani08 = Movie(play="images/new/nathan/nnew_ani08.webm", size = (1280, 720))
image nnew_ani09 = Movie(play="images/new/nathan/nnew_ani09.webm", size = (1280, 720))
image nnew_ani10 = Movie(play="images/new/nathan/nnew_ani10.webm", size = (1280, 720))
image nnew_ani11 = Movie(play="images/new/nathan/nnew_ani11.webm", size = (1280, 720))
image nnew_ani12 = Movie(play="images/new/nathan/nnew_ani12.webm", size = (1280, 720))
image nnew_ani13 = Movie(play="images/new/nathan/nnew_ani13.webm", size = (1280, 720))
image nnew_ani14 = Movie(play="images/new/nathan/nnew_ani14.webm", size = (1280, 720))
image nnew_ani15 = Movie(play="images/new/nathan/nnew_ani15.webm", size = (1280, 720))
image nnew_ani16 = Movie(play="images/new/nathan/nnew_ani16.webm", size = (1280, 720))
image nnew_ani17 = Movie(play="images/new/nathan/nnew_ani17.webm", size = (1280, 720))
image nnew_ani18 = Movie(play="images/new/nathan/nnew_ani18.webm", size = (1280, 720))
image nnew_ani19 = Movie(play="images/new/nathan/nnew_ani19.webm", size = (1280, 720))
image nnew_ani20 = Movie(play="images/new/nathan/nnew_ani20.webm", size = (1280, 720))
image nnew_ani21 = Movie(play="images/new/nathan/nnew_ani21.webm", size = (1280, 720))
image nnew_ani22 = Movie(play="images/new/nathan/nnew_ani22.webm", size = (1280, 720))
image nnew_ani23 = Movie(play="images/new/nathan/nnew_ani23.webm", size = (1280, 720))
image nnew_ani24 = Movie(play="images/new/nathan/nnew_ani24.webm", size = (1280, 720))
image nnew_ani25 = Movie(play="images/new/nathan/nnew_ani25.webm", size = (1280, 720))
image nnew_ani26 = Movie(play="images/new/nathan/nnew_ani26.webm", size = (1280, 720))
image nnew_ani27 = Movie(play="images/new/nathan/nnew_ani27.webm", size = (1280, 720))
image nnew_ani28 = Movie(play="images/new/nathan/nnew_ani28.webm", size = (1280, 720))
image nnew_ani29 = Movie(play="images/new/nathan/nnew_ani29.webm", size = (1280, 720))
image nnew_ani30 = Movie(play="images/new/nathan/nnew_ani30.webm", size = (1280, 720))
image nnew_ani31 = Movie(play="images/new/nathan/nnew_ani31.webm", size = (1280, 720))
image nnew_ani32 = Movie(play="images/new/nathan/nnew_ani32.webm", size = (1280, 720))
image nnew_ani33 = Movie(play="images/new/nathan/nnew_ani33.webm", size = (1280, 720))

image pnew_ani01 = Movie(play="images/new/priscila/pnew_ani01.webm", size = (1280, 720))
image pnew_ani02 = Movie(play="images/new/priscila/pnew_ani02.webm", size = (1280, 720))
image pnew_ani03 = Movie(play="images/new/priscila/pnew_ani03.webm", size = (1280, 720))
image pnew_ani04 = Movie(play="images/new/priscila/pnew_ani04.webm", size = (1280, 720))
image pnew_ani05 = Movie(play="images/new/priscila/pnew_ani05.webm", size = (1280, 720))
image pnew_ani06 = Movie(play="images/new/priscila/pnew_ani06.webm", size = (1280, 720))
image pnew_ani07 = Movie(play="images/new/priscila/pnew_ani07.webm", size = (1280, 720))
image pnew_ani08 = Movie(play="images/new/priscila/pnew_ani08.webm", size = (1280, 720))
image pnew_ani09 = Movie(play="images/new/priscila/pnew_ani09.webm", size = (1280, 720))
image pnew_ani10 = Movie(play="images/new/priscila/pnew_ani10.webm", size = (1280, 720))
image pnew_ani11 = Movie(play="images/new/priscila/pnew_ani11.webm", size = (1280, 720))
image pnew_ani12 = Movie(play="images/new/priscila/pnew_ani12.webm", size = (1280, 720))
image pnew_ani13 = Movie(play="images/new/priscila/pnew_ani13.webm", size = (1280, 720))
image pnew_ani14 = Movie(play="images/new/priscila/pnew_ani14.webm", size = (1280, 720))
image pnew_ani15 = Movie(play="images/new/priscila/pnew_ani15.webm", size = (1280, 720))
image pnew_ani16 = Movie(play="images/new/priscila/pnew_ani16.webm", size = (1280, 720))
image pnew_ani17 = Movie(play="images/new/priscila/pnew_ani17.webm", size = (1280, 720))
image pnew_ani18 = Movie(play="images/new/priscila/pnew_ani18.webm", size = (1280, 720))
image pnew_ani19 = Movie(play="images/new/priscila/pnew_ani19.webm", size = (1280, 720))

image snew_ani01 = Movie(play="images/new/sayuri/snew_ani01.webm", size = (1280, 720))
image snew_ani02 = Movie(play="images/new/sayuri/snew_ani02.webm", size = (1280, 720))
image snew_ani03 = Movie(play="images/new/sayuri/snew_ani03.webm", size = (1280, 720))
image snew_ani04 = Movie(play="images/new/sayuri/snew_ani04.webm", size = (1280, 720))
image snew_ani05 = Movie(play="images/new/sayuri/snew_ani05.webm", size = (1280, 720))
image snew_ani06 = Movie(play="images/new/sayuri/snew_ani06.webm", size = (1280, 720))
image snew_ani07 = Movie(play="images/new/sayuri/snew_ani07.webm", size = (1280, 720))
image snew_ani08 = Movie(play="images/new/sayuri/snew_ani08.webm", size = (1280, 720))
image snew_ani09 = Movie(play="images/new/sayuri/snew_ani09.webm", size = (1280, 720))
image snew_ani10 = Movie(play="images/new/sayuri/snew_ani10.webm", size = (1280, 720))
image snew_ani11 = Movie(play="images/new/sayuri/snew_ani11.webm", size = (1280, 720))
image snew_ani12 = Movie(play="images/new/sayuri/snew_ani12.webm", size = (1280, 720))
image snew_ani13 = Movie(play="images/new/sayuri/snew_ani13.webm", size = (1280, 720))
image snew_ani14 = Movie(play="images/new/sayuri/snew_ani14.webm", size = (1280, 720))
image snew_ani15 = Movie(play="images/new/sayuri/snew_ani15.webm", size = (1280, 720))
image snew_ani16 = Movie(play="images/new/sayuri/snew_ani16.webm", size = (1280, 720))
image snew_ani17 = Movie(play="images/new/sayuri/snew_ani17.webm", size = (1280, 720))
image snew_ani18 = Movie(play="images/new/sayuri/snew_ani18.webm", size = (1280, 720))
image snew_ani19 = Movie(play="images/new/sayuri/snew_ani19.webm", size = (1280, 720))
image snew_ani20 = Movie(play="images/new/sayuri/snew_ani20.webm", size = (1280, 720))
image snew_ani21 = Movie(play="images/new/sayuri/snew_ani21.webm", size = (1280, 720))
image snew_ani22 = Movie(play="images/new/sayuri/snew_ani22.webm", size = (1280, 720))
image snew_ani23 = Movie(play="images/new/sayuri/snew_ani23.webm", size = (1280, 720))

image sonew_ani01 = Movie(play="images/new/sofia/sonew_ani01.webm", size = (1280, 720))
image sonew_ani02 = Movie(play="images/new/sofia/sonew_ani02.webm", size = (1280, 720))
image sonew_ani03 = Movie(play="images/new/sofia/sonew_ani03.webm", size = (1280, 720))
image sonew_ani04 = Movie(play="images/new/sofia/sonew_ani04.webm", size = (1280, 720))
image sonew_ani05 = Movie(play="images/new/sofia/sonew_ani05.webm", size = (1280, 720))
image sonew_ani06 = Movie(play="images/new/sofia/sonew_ani06.webm", size = (1280, 720))
image sonew_ani07 = Movie(play="images/new/sofia/sonew_ani07.webm", size = (1280, 720))
image sonew_ani08 = Movie(play="images/new/sofia/sonew_ani08.webm", size = (1280, 720))
image sonew_ani09 = Movie(play="images/new/sofia/sonew_ani09.webm", size = (1280, 720))







default versao = "0.4"
default prox_versao = "0.5"
default dia_prox_versao = "1 de Abril de 2021"
default premium = True









default persistent.anuncio = False
default persistent.daily = False
default persistent.apoiador = True
default persistent.inicia = False


default daily = False
default compra_dezmil = False
default compra_anuncio = False
default compra_apoio = False

default persistent.coins = 50
default persistent.guia1 = False
default persistent.vid = False
default persistent.cartas_carregadas = False

default persistent.tutorial_cards = False
default persistent.gplay_1 = False

default persistent.mc_sexo = "nenhum"

default persistent.fadex_maca = False
default fadex_maca = False
default persistent.priscila_encontro_1vez = True
default persistent.gadgetalfa = False
default persistent.gadgetbeta = False
default persistent.gadgetgama = False
default persistent.banned = False
default persistent.demitido = False
default persistent.quincy_morte = False
default persistent.quincy_especial = False
default persistent.mc = "você"



default persistent.priscila_cena1 = False
default persistent.priscila_cena2 = False
default persistent.priscila_cena3 = False
default persistent.priscila_cena4 = False
default persistent.priscila_cena5 = False
default persistent.priscila_cena6 = False
default persistent.priscila_cena7 = False
default persistent.priscila_cena8 = False
default persistent.priscila_cena9 = False
default persistent.priscila_cena10 = False


default mtempo = False
default musica = "mus1"
default etempo = False
default userlogado = True
default useremail = "convidado"
default hora_pauta = False
default proibido_salvar = False
default tempoagora = 0
default checatempo = False
default tbtempo = False
default tltempo = False
default cash = 0
default novo_cash = 0
default roupa_blacktie = False
default roupa_blazer = False
default casa = False
default karli_casa = False
default ap_comodo = "nada"
default credito = 0
default credito_total = 0
default uid = "NOID"
default chovendo = False



default bar_item_1 = False
default bar_item_2 = False
default bar_item_3 = False
default bar_item_4 = False
default bar_item_5 = False
default bar_item_6 = False
default bar_item_7 = False
default bar_item_8 = False
default bar_item_9 = False
default bar_item_10 = False
default tb_items = 0
default a9009 = False
default a9010 = False



define liberar_carta = False

default persistent.card_1 = False
default persistent.card_2 = False
default persistent.card_3 = False
default persistent.card_4 = False
default persistent.card_5 = False
default persistent.card_501 = False
default persistent.card_502 = False
default persistent.card_503 = False
default persistent.card_504 = False
default persistent.card_505 = False
default persistent.card_506 = False
default persistent.card_507 = False
default persistent.card_508 = False
default persistent.card_509 = False
default persistent.card_510 = False
default persistent.card_1001 = False
default persistent.card_1002 = False
default persistent.card_1003 = False
default persistent.card_1004 = False
default persistent.card_1005 = False
default persistent.card_1006 = False
default persistent.card_1007 = False
default persistent.card_1008 = False
default persistent.card_1009 = False
default persistent.card_1010 = False
default persistent.card_1011 = False
default persistent.card_1012 = False
default persistent.card_1013 = False
default persistent.card_1014 = False
default persistent.card_1015 = False

default carta_full = ""



define mcantes = Character("Rapaz", image = "mc")
define p = Character("Pixie", image = "pixie")
define i = Character("[i_nome]")
define mc = Character("[mcpnome]", image = "mc")
define mcc = Character("[mcpnome] [mcsnome]")
define c = Character("[c_nome]", image = "priscila")
define cc = Character("[cc_nome]")
define ca = Character("[pri_apelido]")
define b = Character("Chefe")
define gar = Character("[garcomname]")
define sc = Character("Sayuri Ichigo")
define s = Character("Sayuri", image = "sayuri")
define j = Character("Cássia")
define jc = "a jornalista da câmera"
define n = Character("Nathan")
define nc = Character("Nathan Bryant")
define g = Character ("[gnome]", image = "garconete")
define ngep = Character("[nge]")
define m = Character("[m_nome]")
define gina = Character("[gina_nome]")
define a = Character("[a_nome]")
define mar = Character("Marco")
define d = Character("Diana")
define dc = Character("Diana Castro")
define f = Character("[f_nome]")
define x = Character("[x_nome]")
define ma = Character("Maria")
define ana = Character("Ana")
define chi = Character("[chi_nome]")
define fen = Character("[fen_nome]")
define mes = Character("[mes_nome]")
define t = Character("[t_nome]")
define us = Character("[us_nome]")
define ce = Character("[ce_nome]")
define o = Character("[o_nome]")
define mon = Character("[mon_nome]")
define ate = Character("[at_nome]", image = "ate")
define nora = Character("[nora_nome]")
define gi = Character("[gi_nome]")
define w = Character("[w_nome]")
define ag = Character("[ag_nome]")
define orc = Character("[orc_nome]")
define he = Character("[he_nome]")
define li = Character("[li_nome]")
define xu = Character("[xu_nome]")
define ka = Character("[ka_nome]")
define fado = Character("[fado_nome]")
define en = Character("[en_nome]")
define ina = Character("[ina_nome]")
define caio = Character("[caio_nome]")
define teo = Character("Téo")
define mari = Character("Mari")
define qui = Character("[qui_nome]")
define eli = Character("[eli_nome]")
define na = Character("[na_nome]")
define q = Character("[q_nome]")
define mo = Character("[mo_nome]")
define se = Character("Dra. Sellers")
define el = Character("Elena")
define to = Character("[to_nome]")
define lu = Character("[lu_nome]")
define ba = Character("[ba_nome]")
define h = Character("[h_nome]")
define sh = Character("Shoshana")
define ro = Character("Roxane")
define re = Character("Renata")
define ron = Character("Ronaldo")
define po = Character("[po_nome]")
define y = Character("[y_nome]")
define ta = Character("[ta_nome]")
define ve = Character("[ve_nome]")
define pr = Character("Basilio")
define prc = Character("Basilio Donatello")
define za = Character("[za_nome]")
define fn = Character("Letícia")
define mae = Character("Mãe")
define mr = Character("Mauro Ribeiro")

define diretor = Character("Gustav Aldebaran")
define gus = Character("Gustav")

define garcomname = "Garçom"

default mcpnome = "Você"
default mcsnome = ""

default gnome = "Garçonete"
default m_nome = "Garota"
default gina_nome = "Senhora"
default a_nome = "Miranda"
default f_nome = "Fada"
default x_nome = "Garota"
default t_nome = "garota do caixa"
default chi_nome = "Velho Chinês"
default fen_nome = "Garota Chinesa"
default mes_nome = "???"
default us_nome = "???"
default ce_nome = "Stripper"
default o_nome = "Estudante"
default at_nome = "Atendente"
default mon_nome = "Segurança"
default nora_nome = "Senhora"
default i_nome = "Stripper"
default gi_nome = "Voz Masculina"
default w_nome = "Garota"
default c_nome = "Priscila"
default cc_nome = "Priscila Fontinelli"
default ag_nome = "Garota"
default orc_nome = "Orc"
default he_nome = "Cavaleiro"
default li_nome = "Mulher"
default xu_nome = "Garota"
default ka_nome = "Garota"
default fado_nome = "???"
default en_nome = "Protetor dos Sumérios"
default ina_nome = "Mulher"
default caio_nome = "Caio"
default qui_nome = "Quincy Jones"
default eli_nome = "Elisabeth"
default na_nome = "Mulher"
default q_nome = "???"
default mo_nome = "Recepcionista"
default to_nome = "Homem"
default lu_nome = "Luca"
default ba_nome = "???"
default h_nome = "Garota"
default po_nome = "Policial"
default y_nome = "Garota"
default ta_nome = "Tatá"
default ve_nome = "Verônica"
default za_nome = "Zaza"

default carta_escolhida = 1



image sayuri carta = "cards/full/card_2.jpg"
image sayuri desmaio = "cards/full/card_503.jpg"
image sayuri chegada = "cards/full/card_1005.jpg"
image priscila parte2 = "cards/full/card_501.jpg"
image nathan cena_bebida = "cards/full/card_506.jpg"
image nathan cena = "cards/full/card_1007.jpg"
image apartamento cama_celular = "cards/full/card_1010.jpg"
image priscila inicio_deitada = "cards/full/card_507.jpg"
image julia selfie_universidade = "cards/full/card_508.jpg"
image massagem roupao_e1 = "cards/full/card_509.jpg"
image massagem kita = "cards/full/card_1013.jpg"
image priscila praia_bola = "cards/full/card_1014.jpg"
image priscila praia_sentados = "cards/full/card_1015.jpg"
image pub fundao = "images/bar/bar_angulo2.jpg"


image side mc normal = "mc_side_normal.png"
image side mc charmoso = "mc_side_charmoso.png"
image side mc tarado = "mc_side_tarado.png"
image side mc angustiado = "mc_side_angustiado.png"
image side mc triste = "mc_side_triste.png"
image side mc zerado = "mc_side_zero.png"
image side mc envergonhado = "mc_side_envergonhado.png"
image side mc desculpa = "mc_side_desculpa.png"
image side mc bravo = "mc_side_bravo.png"
image side mc feliz = "mc_side_feliz.png"
image side mc desconfiado = "mc_side_desconfiado.png"
image side mc surpreso = "mc_side_surpreso.png"
image side mc irritado = "mc_side_irritado.png"
image side mc muitofeliz = "mc_side_muitofeliz.png"
image side mc concentrando = "mc_side_concentrando.png"
image side mc safado = "mc_side_safado.png"
image side mc incomodado = "mc_side_incomodado.png"
image side mc serio = "mc_side_serio.png"
image side mc preocupado = "mc_side_preocupado.png"

image side priscila s_feliz = "priscila_side_feliz.png"
image side priscila triste = "priscila_side_triste.png"
image side priscila surpresa = "priscila_side_surpresa.png"

image side garconete desconfiada = "g_side_desconfiada.png"
image side garconete emburrada = "g_side_emburrada.png"
image side garconete normal = "g_side_provocando.png"

image side pixie rindo = "pixie_side_rindo.png"
image side pixie lecionando = "pixie_side_lecionando.png"

image side sayuri s_assustada = "s_side_assustada.png"

image side ate normal = "atendente_side_normal.png"

image mapa cidade = "images/mapa/mapa_cidade.jpg"
image mapa cidade_tarde = "images/mapa/cidade_tarde.jpg"
image mapa cidade_noite = "images/mapa/mapa_cidade_noite.jpg"



image n8_fab = im.Blur("n8_img18.webp", 1.15)



default namorando = False
default priscila_amizade = 0
default priscila_seducao = 0
default priscila_idiota = 0
default priscila_namoro = False
default sayuri_namoro = False
default priscila_desistiu = False
default priscila_amizade_total = 7
default priscila_seducao_total = 7
default priscila_amizade_evento = 0
default priscila_seducao_evento = 0
default pixie_amizade = 0
default pixie_seducao = 0
default pixie_amizade_evento = 0
default pixie_seducao_evento = 0
default sayuri_amizade = 0
default sayuri_seducao = 0
default sayuri_amizade_total = 22
default sayuri_amizade_evento = 0
default sayuri_seducao_evento = 0
default julia_seducao = 0
default julia_seducao_total = 13
default julia_seducao_evento = 0
default julia_amizade_evento = 0
default nathan_amizade = 0
default nathan_amizade_total = 10
default nathan_amizade_evento = 0
default karli_seducao = 0
default miranda_seducao = 0
default maria_seducao = 0
default thaynara_seducao = 0
default diana_seducao = 0
default diana_namoro = False
default atendente_seducao = 0
default sofia_amizade = 0
default pixel_amizade = 0
default natasha_seducao = 0
default quincy_amizade = 0
default hacker_amizade = 0
default shoshana_amizade = 0
default nathan_namoro = False
default roxane_seducao = 0
default naru_amizade = 0
default sofia_namoro = False
default tb_mais = 0

default priscila_neto = 0

default maria_evento = 0
default thaynara_evento = 0
default persistent.thaynara_evento = 0

default persistent.selena_morreu = False



default priscila_e1 = "nada"
default priscila_e2 = "nada"
default priscila_e3 = "nada"
default priscila_e5 = "nada"
default priscila_e7 = "nada"
default priscila_e8 = "nada"
default priscila_e9 = "nada"

default priscila_e6_ligacao_check = False
default priscila_e6_ligacao = False

default sayuri_e1 = "nada"
default sayuri_e2 = "nada"
default sayuri_e3 = "nada"
default sayuri_e4 = "nada"
default sayuri_e5 = "nada"
default sayuri_e7 = "nada"
default sayuri_e8 = "nada"
default sayuri_e9 = "nada"

default julia_e1 = "nada"
default julia_e2 = "nada"
default julia_e3 = "nada"
default julia_e4 = "nada"
default julia_e5 = "nada"
default julia_e6 = "nada"
default julia_e7 = "nada"
default julia_v8 = "nada"

default nathan_evento = False
default nathan_e1 = "nada"
default nathan_e2 = "nada"
default nathan_e3 = "nada"
default nathan_e4 = "nada"
default nathan_e5 = "nada"
default nathan_e6 = "nada"
default nathan_e7 = "nada"
default nathan_e8 = "nada"

default diana_e1 = "nada"
default diana_e2 = "nada"
default diana_e3 = "nada"
default diana_e4 = "nada"
default diana_e5 = "nada"
default diana_e6 = "nada"
default diana_e7 = "nada"

default pixie_e1 = "nada"
default pixie_e2 = "nada"
default pixie_e3 = False
default pixie_historia = 0

default cassia_e1 = "nada"

default stifler_e1 = "nada"

default sofia_e1 = "nada"
default sofia_e3 = "nada"
default sofia_e4 = "nada"
default sofia_e5 = "nada"

default natasha_e1 = "nada"
default natasha_e2 = "nada"
default natasha_e3 = "nada"
default natasha_e4 = "nada"

default nona_e1 = "nada"
default nona_e2 = "nada"
default nona_e3 = "nada"

default naru_e1 = "nada"



default show_quick_menu = True
default foi_despedido = False

default p1_quem = False
default p1_escolha2check = False
default p1_dificuldade = False
default p1_corpo = False
default p1_bebida = False
default p1_pixie_espiar = False
default notas_do_confinado1 = False
default notas_do_confinado2 = False
default notas_do_confinado3 = False
default v0 = False
default celular_notificacao = False
default ligacao_ativa = False

default nathan_garotas = 0
default nge = "Garotas"
default nathan_cassia = False
default nathan_e1_fim_garota = "Nada"
default n1_bebida = False
default n1_ajuda = False
default cassia_nathan1 = False
default cassia_nathan_entregou = False
default cassia_nathan_naoajudou = False
default cassia_priscila_avisou = False


default priscila_numero = False
default priscila_cel_msg1 = False
default priscila_cel_msg2 = False
default priscila_cel_msg2_n = False
default priscila_cel_msg3 = False
default priscila_cel_msg4 = False
default priscila_cel_msg5 = False
default priscila_cel_msg6 = False
default priscila_cel_msg7 = False
default priscila_cel_msg1_r = "nada"
default priscila_cel_msg2_r = "nada"
default priscila_cel_msg3_r = "nada"
default priscila_cel_msg4_r = "nada"
default priscila_cel_msg5_r = False
default priscila_cel_msg6_r = "nada"
default priscila_cel_msg7_r = False
default priscila_cel_msg3_rA = False
default priscila_cel_msg4_rA = "nada"
default priscila_cel_msg1_resposta_check = True
default priscila_cel_msg2_resposta_check = True


default sayuri_numero = False
default sayuri_cel_msg1 = False
default sayuri_cel_msg2 = False
default sayuri_cel_msg3 = False
default sayuri_cel_msg4 = False
default sayuri_cel_msg5 = False
default sayuri_cel_msg1_r = "nada"
default sayuri_cel_msg2_r = "nada"
default sayuri_cel_msg3_r = "nada"
default sayuri_cel_msg4_r = "nada"
default sayuri_cel_msg5_r = "nada"
default sayuri_cel_msg1_resposta_check = True
default sayuri_cel_msg2_resposta_check = True
default sayuri_cel_msg3_resposta_check = True


default cassia_numero = False
default cassia_cel_msg1 = False
default cassia_cel_msg2 = False
default cassia_cel_msg3 = False
default cassia_cel_msg3_resposta_check = False
default cassia_cel_msg3_r = "nada"
default cassia_cel_msg3_rA = False

default estou_na_cidade = False


default nathan_numero = False
default nathan_cel_msg1 = False
default nathan_cel_msg1_r = False
default nathan_cel_msg2 = False
default nathan_cel_msg2_r = False
default nathan_cel_msg2_r2 = "nada"
default nathan_cel_msg3 = False
default nathan_cel_msg3_resposta = False
default nathan_cel_msg4 = False
default nathan_cel_msg4_resposta = False
default nathan_cel_msg5 = False
default nathan_cel_msg5_resposta = False


default julia_numero = False
default julia_cel_msg1 = False
default julia_cel_msg2 = False
default julia_cel_msg3 = False
default julia_cel_msg4 = False
default julia_cel_msg5 = "nada"
default julia_cel_msg5_r = False
default julia_cel_msg6 = False
default julia_cel_msg6_r = False
default julia_cel_msg1_resposta_check = True
default desp = False
default julia_cel_msg1_r = "nada"


default diana_numero = False
default diana_cel_msg1 = False
default diana_cel_msg1_r = "nada"



default sayuri_p1 = True
default sayuri_p2 = False
default sayuri_p1_mentira = 0
default priscila_p1 = False
default priscila_p2 = False
default priscila_p3 = False
default nathan_p1 = False
default diana_p1 = False
default diana_p2 = False
default celeste_p1 = False
default hacker_p1 = False
default pautas = 0
default pautas_liberado = False
default entregou_pauta = 0
default priscila_atencao = 0
default sayuri_atencao = 0
default nathan_atencao = 0
default diana_atencao = 0
default celeste_atencao = 0
default caio_p1 = False
default distrito_atencao = 0
default fabricio_p1 = False
default fabricio_atencao = 0
default tkf_p1 = False
default tkf_atencao = 0
default hacker_atencao = 0
default distrito = 0
default distrito_soma = 0
default distrito_db = 0
default tony_p1 = 0


default fundo_especial = False
default sayuri_evento1_check = True
default sayuri_stalker = False
default quem_ligou = "priscila"
default e1_priscila_namorado = False
default resultado_encontro = "priscila"
default cassia_evento = False
default cassia_evento1 = False
default cassia_aceitou = False
default cassia_seducao = False
default v1_fim = False
default v2_fim = False
default v3_fim = False
default v4_fim = False
default v5_fim = False
default v6_fim = False
default v7_fim = False
default v8_fim = False
default v9_fim = False
default v10_fim = False
default v11_fim = False
default v12_fim = False
default v13_fim = False
default v14_fim = False
default v15_fim = False
default v16_fim = False
default v17_fim = False
default v18_fim = False
default v19_fim = False
default v20_fim = False
default v21_fim = False
default v22_fim = False
default v23_fim = False
default v24_fim = False
default v25_fim = False
default v26_fim = False
default v27_fim = False
default v28_fim = False
default v29_fim = False
default v30_fim = False
default v31_fim = False
default v32_fim = False
default v33_fim = False
default v34_fim = False
default v35_fim = False
default v36_fim = False
default v37_fim = False
default v38_fim = False
default v39_fim = False
default v40_fim = False
default v41_fim = False
default v42_fim = False
default v43_fim = False
default v44_fim = False
default v45_fim = False
default v46_fim = False
default v47_fim = False
default v48_fim = False
default v49_fim = False
default v50_fim = False
default v51_fim = False
default v52_fim = False
default v53_fim = False
default v54_fim = False
default v55_fim = False
default aviso_chefe = True
default aviso_chefe_1vez = True
default dormir_em_casa = False
default cidade_vez = 2
default sayuri_estudou = "nada"
default sayuri_calcinha = False
default massagista_bonita = False
default massagista_trabalha = False
default massagista_parque = False
default massagista_negado = 0
default karli_roupao = False
default karli_ajudou = False
default julia_inimigo = False
default julia_viutrocando = False
default julia_conversou = False
default priscila_e3_check = "nada"
default priscila_cassia_ignorou = False
default priscila_e3_ouviu = False
default marco_conheceu = False
default priscila_e3_beijo = False
default priscila_e3_sexo = False
default p3_confissao = False
default p3_escolha = "nada"
default aviso_final = False
default s3_mini = 0
default sayuri_intencao = "nada"
default se3_pelada = False
default julia_cel_msg3_evento = False
default j2_sayuri_avisou = False
default julia_e2_conversou = False
default j2_round = 1
default julia_e2_game = "nada"
default j2_mc_perdeu = False
default j2_recusou = "nada"
default j2_sayuri_traida = False
default j2_espiou = False
default massagem_priscila_1vez = True
default diana_conheceu = False
default mc_ja_tomou_banho = False
default ep_tutorial = False
default f1_poder = False
default f1_biquini = False
default f1_atencao = 0
default fadex_1vez = False
default fadex_caverna = False
default fadex_cabana = False
default fadex_monolito = False
default fadex_fonte = False
default pauta_1vez = False
default ep_pontos = 0
default nathan_perdoa = 0
default favor_cassia_pauta = False
default xeena_encontro = False
default priscila_ef_check = False
default fnext = "0"
default epnext = "0"
default masnext = "0"
default tbnext = "0"
default mtnext = "0"
default tlnext = "0"
default priscila_e4_check = "nada"
default p4_tempo = 0
default p_amigo = False
default miranda_sexo = False
default miranda_conversou = False
default p4_miranda_bar = False
default gadget2cena = False
default gadgetalfa = False
default gadgetbeta = False
default gadgetgama = False
default cena_gadget = False
default gadget_final = False
default gustav_derrotado = False
default miranda_pri_caso = False
default gina_biquini = False
default gina_procurou = False
default gina_idiota = False
default gina_segredo = False
default gina_atraido = False
default gina_massagem = False
default karli_sair = True
default karli_p_tadaima = False
default cassia_ponte = False
default s4_julia_good = False
default s4_fenju = False
default s4_cidade = False
default s4_chinatown = False
default s4_ofuro = False
default s4_mestra_xingou = False
default s4_chinatown_visita = False
default bar_item_t1 = False
default bar_item_t2 = False
default trabalho_bar = False
default thaynara_conheceu = False
default mercado_1vez = False
default stifler_conheceu = False
default stifler_e1_perguntas = 0
default stifler_mc_homens = False
default stifler1_striper = False
default celeste_fotos = False
default j3_dificuldade = 0
default j3_xereta = 0
default j3_chance = 0
default j3_ouviu_p1 = False
default j3_ouviu_p2 = False
default j3_ouviu_p3 = False
default j3_ouviu_p4 = False
default carol_reconheceu = False
default j3_cena = False
default j3_banho = False
default j3_investigou = 0
default j3_jogo = False
default j3_uma_pergunta = False
default d2_blacktie = False
default d2_blazer = False
default diana_e2_roupa = False
default diana_e2_roupa_evento = False
default adblock = False
default bdsm_1vez = 0
default xiang_flor = False
default stifler2_xiang = False
default stifler_e2_fim = False
default celeste_on = False
default xiang_on = False
default stifler_on = False
default xiang_show = True
default xiang_particular = True
default xiang_historia = 0
default stifler_conversa = 0
default stifler_falou = True
default celeste_conheceu = False
default celeste_conversa = 0
default celeste_falou = True
default stifler_e2_perguntas = False
default nathan_beijo = False
default maria_anda = None
default maria_esquerda = 0
default mc_esquerda = 0
default mc_velocidade = 0.001
default maria_velocidade = 0.001
default maria_lvl = 1
default maria_relacao = False
default maria_lvl1 = False
default maria_lvl2 = False
default maria_lvl3 = False
default maria_namoro = False
default treino_sucesso = False
default mttempo = 0
default maria_treinamento_lv1 = 0
default maria_treinamento_lv2 = 0
default mc_fisico_minimo = 6
default cassia_e2_plano = False
default cassia_e2_cassia = False
default n3_carreira = False
default n3_situacao = False
default n3_beijo = False
default n3_gravou = False
default nathan_e3_beijo = False
default visitou_museu = False
default casa_comprada = False
default compra_casa_evento = False
default sem_casa = False
default k7_continua = False
default k7_poscasa = False
default karli_morou = False
default tempo_karli = 1
default karli_esta = True
default karli_evento_auto = 0
default karli_evento_dia = False
default karli_evento_falar = 0
default karli_evento_comer = 0
default sofia_e1_count = 0
default sofia_e1_confiou = 0
default sofia_confiou = False
default sofia_e1_massageou = False
default sofia_evento_manha = False
default p1_descobriu = False
default p5_naoviajou = False
default p5_visita = 0
default p5_cidade = False
default p5_vale = False
default p5_ponte = False
default priscila_segredo = False
default conversou_gustav = False
default socou_gustav = False
default p5_beijo = False
default priscila_chutado = False
default priscila_reconquista = False
default karli_beijo = False
default karli_dancou = False
default chinatown_area = "geral"
default china_banho_1vez = False
default china_negra = False
default xiangu_evento = 0
default dia_xiangu = 0
default dia_bao = 0
default banho_evento = 0
default banho_evento_db = 0
default dia_banho = 0
default xiangu_p_lenda = False
default xiangu_p_imortal = False
default bao_pontos = 0
default bao_evento = 0
default lamen_trabalhou = 0
default bao_introducao = False
default lamen_rever = False
default liling_seducao = False
default xiangu_flor = False
default xiang_evento_db = 0
default xiang_evento = 0
default xiang_xiangu = False
default sayuri_beijo = False
default s5_rigida = False
default s5_ajudou = False
default fenju_naocontou = False
default fenju_coca = False
default karli_gina = False
default gina_bunda = False
default karli_declaracao = False
default sayuri_adeus = False
default fenju_treino = False
default fenju_evento = 0
default sayuri_contou_caio = False
default j4_guardacosta = False
default j4_intencao = False
default j4_conversa = False
default j4_juliacaio = False
default j4_interrompeu = False
default j4_roupa = False
default j4_bronca = False
default caio_negou = False
default j4_salvou = False
default julia_namoro = False
default j4_blazer = False
default pauta_fabricio = False
default pauta_cassia = 0
default pauta_cassia_db = 0
default diana3_promessa = False
default diana3_segredo = False
default diana3_beijo = False
default diana3_negou = False
default n4_juiza_pergunta = False
default juiza_fotos = False
default juiza_sucesso = False
default nathan_e4_beijo = False
default nathan_audiencia = False
default nathan_dossie = False
default sofia2_cassia = False
default natasha_falou = False
default natasha_evento = 0
default na1_p1 = False
default na1_p2 = False
default na1_p3 = False
default na1_p4 = False
default natasha_pontos = 0
default natasha_vez = 0
default natasha_db = 0
default ntempo = 0
default nnext = "0"
default snext = "0"
default natasha_xeretou = False
default na1_beijo = False
default xiang_errou = False
default thaynara_db = 0
default thaynara_check = 1
default thaynara_amizade = False
default quincy_e1 = False
default quincy_e2 = False
default quincy_e3 = False
default quincy_e4 = False
default quincy_e2_comecou = False
default priscila_reatou = False
default priscila_friendzone = False
default p6_julgamento = "nada"
default marco_gustav = False
default agata_priscila = False
default agata_beijo = False
default s6_beijo1 = False
default s6_fenju = False
default s6_ofuro_juntos = False
default s6_mudanca = False
default s6_declarou = False
default s6_beijo2 = False
default s6_fenju_spa1 = False
default s6_fenju_spa2 = False
default s6_fenju_direto = False
default sayuri_adeus_manteve = False
default se6_goodending = False
default j5_carol_contou = False
default j5_brigou_uni = False
default sofia_dia = 0
default sofia_vez = 0
default sofia_db = 0
default sofia_next = 5
default sofia_lvl = 0
default sofia_xp = 0
default stempo = 0
default sofia_imagem = "extra/sofia_lvl0.png"
default sofia_e2_good = False
default j5_cinema = False
default j5_beijo = False
default j5_banheiro = False
default j5_good = False
default j5_beijo2 = False
default j5_roupa = False
default area = "cidade"
default mapa = "cidade1"
default submapa = "nada"
default submapa2 = "nada"
default tkf_1vez = False
default moena_nome = False
default tkf_evento1 = False
default p6_denuncia = False
default praia_especial_1vez = False
default praia_especial = "priscila"
default j6_carol_beijinho = False
default agata_confessa = False
default miranda_sexo1 = False
default no2_evento = False
default sofia_premium = 0
default lua_especial = False
default mari_final = False
default caio_gi_contou = False
default sacerdotisas = 0
default julia_segredo = False
default carol_declarou = False
default livros_liberados = 0
default livros_liberados_db = 0
default j8_julia_ouviu = False
default julia_completo = False
default carro_evento = 0
default carro = False
default carro_gina = 0
default destino = ""
default d7_escolha = 0
default d7_avisa_barao = False
default d7_envelope = 0
default d7_agradece = False
default sayuri_terminou = False
default d7_faca = 0
default natasha_cobrou = False
default sayuri_cobrou = False
default na3_beijo = False
default na3_seducao = False
default na3_banheira = False
default diana_final1 = False
default diana_final2 = False
default diana_final3 = False
default persistent.diana_final1 = False
default persistent.diana_final2 = False
default d7_nat_prometeu = False
default natasha_entregou = False
default sofia_entregou = False
default d7_natasha_sexo = False
default black_salva = 0
default diana_terminou = False
default diana_final2_pre = False
default diana_grupo = False
default grupo_nathan = 0
default diana_negou = False
default diana_rompeu = False
default roxane_ouviu = False
default blergh_foto = False
default n8_grupo = False
default n8_convenceu = 0
default distrito_liberou = False
default nathan_stifler = 0
default n8_roupa = 0
default roupa_nathan = False
default nathan_final1 = False
default nathan_final2 = False
default nathan_final3 = False
default persistent.nathan_final1 = False
default persistent.nathan_final2 = False
default persistent.nathan_final3 = False
default roxane_distrito = False
default nathan_final_desistiu = False
default nathan_final_desistiu2 = False
default renata_prometeu = False
default sofia_evento6 = 0
default so6_mae_ligou = 0
default renata_seduziu = False
default sofia_final2_pre = False


default praia_escolhida = "priscila"
default praia_priscila = False
default praia_priscila_local = False
default praia_sayuri = False
default praia_sayuri_local = False
default praia_julia = False
default praia_julia_local = False
default praia_diana = False
default praia_diana_local = False
default praia_nathan = False
default praia_nathan_local = False
default praia_sofia = False
default praia_sofia_local = False
default praia_natasha = False
default praia_natasha_local = False
default praia_nona = False
default praia_nona_local = False

default diana_quente = False
default tony1 = False
default d4_desabafou = False
default academia = False
default maria_academia = 0
default folego = 50
default esteira_velo = 0.5
default menos_folego = 15
default treinando_sozinho = False
default fisico_recompensa = 5
default academia_maria_evento = False
default nathan_quente = False
default nathan_e5_beijo = False
default sofia_e3_chocada = False
default sofia_e3_transou = False
default sofia_beijo = False
default sofia_namorar = False
default sofia_e3_good = False
default randevent = 0
default sayuri_templo_abraco = False
default memoria_img = ""
default memoria_menu = ""
default sayuri_e2_beijo_julia = False
default h1_dinheiro = False
default h1_sonho = False
default h1_responsavel = "nada"
default h1_seducao = False
default p7_cassia = False
default p7_miranda = False
default p7_tony = False
default p7_perguntas = 0
default s7_vila = 0
default s7_continua = False
default j6_caio_perdoa = False
default j6_teo = False
default j6_final_mari = False
default j6_historia = False
default n6_blazer = False
default julia_sexo_praia = False
default venda_revista = 0
default p7_denunciou = False
default p9_depoimentos = 0
default julgamento_sucesso = 0
default p9_priscila = False
default p9_miranda = 0
default miranda_aviao = False
default xiang_escape = 0
default xiang_fim = False
default xiang_casa = False
default xiang_evento_dia = False
default xiang_casa_evento = 0
default j6_mari_serio = False
default natasha18 = 0
default videogame = 0
default s9_pedidos = 0
default s9_pedido1 = False
default s9_pedido2 = False
default s9_pedido3 = False
default s9_pedido4 = False
default s9_mestra = 0
default sayuri9_contra = False
default sayuri_fim = False
default xiangu_namoro = False
default sayuri9_mc_fala = False
default sayuri_final1 = False
default sayuri_final2 = False
default sayuri_final3 = False
default persistent.sayuri_final1 = False
default persistent.sayuri_final2 = False
default persistent.sayuri_final3 = False
default sayuri_casamento = False
default j8_faculdade = False
default j8_cinema = False
default j8_tadaima = False
default j8_negou = False
default j8_caio = False
default j8_mari = False
default caio_prometeu = 0
default julia_final1 = False
default julia_final2 = False
default julia_final3 = False
default persistent.julia_final1 = False
default persistent.julia_final2 = False
default persistent.julia_final3 = False
default chefe_saiu = False
default sofia_final2 = False
default sofia_final3 = False
default xiangu_partiu = False


default salvado = False
default aposta = 0
default ganhos = 0
default slot1 = ""
default slot2 = ""
default slot3 = ""
default slot_result1 = ""
default slot_result2 = ""
default slot_result3 = ""
default slots_ganhou = False
default randslotw = 0
default randslotl = 0
default credito_atual = 0
default credito_ganho = 0
default credito_gold = 10000
default credito_falta = 0
default casher_1vez = False
default cassino_area = ""
default cassino_1vez = False
default parar_vez = 0
default randanterior = 0
default randvezes = 1
default slotvezes = 0
default rand = 0
default slots_evento30_viu = False
default slots_evento = 0
default slots_ana_aviso = False
default cassino_drink = False
default gold_card = False
default silver_card = False
default credito_acumulado = 0
default cassino_2vez = False
default patricia_conheceu = False
default ana_evento = 0
default credito_ana = 0
default cassino_evento = "nada"
default cassino_regiao = "apostas"
default evento_c_ponte = 0
default show_diana = False
default quincy_evento = 0
default ana_sexy = 0
default ana_conversa = 0
default cassino_roupa = "normal"
default slots_controle = 0
default persistent.slot_controle = 0
default card = "Silver Card"


default fadolandia = 0
default fadolandia_db = 0
default fadolandia_soma = 0
default pixel_evento = 0
default fado_m1a1 = False
default fado_m1a2 = False
default fado_m1a3 = False
default fado_m1a4 = False
default fado_m1a5 = False
default fado_m1a6 = False
default fado_m2a1 = False
default fado_m2a2 = False
default fado_m2a3 = False
default fado_m2a4 = False
default fado_m2a6 = False
default fado_m3a1 = False
default fado_m3a2 = False
default fado_m3a3 = False
default fado_m3a4 = False
default fado_m3a5 = False
default fado_m3a7 = False
default fado_m4a1 = False
default fado_m4a2 = False
default fado_m4a3 = False
default mapa1_morte = False
default mapa2_morte = False
default mapa1_precisa_ponte = False
default mapa3_energizado = False
default fadolandia_galhos = False
default fadolandia_m1ponte = False
default fadolandia_cristal = False
default fadolandia_cristal_n = False
default fado_m1nota = False
default fado_m2nota = False
default fado_m3nota = False
default fado_m2cristal = False
default fado_m3pedra = False
default fado_m4sangue = False
default fado_precisa_maca = False
default fado_maca = False
default fado_faloumaca = False
default fado_pixel_comeu = False

default fado1 = False
default fadex_e1 = False
default fadex_e2 = False
default fadex_e3 = False
default fadex_e4 = False
default fadex_e5 = False
default fadex_d1 = False
default fadex_d2 = False
default fadex_d3 = False
default fadex_d4 = False
default fadex_d5 = False
default fadex_d6 = False
default fadex_c1 = False
default fadex_c2 = False
default fadex_c3 = False
default fadex_c4 = False
default fadex_c5 = False
default caverna_1vez = False
default pixel_encontro = False
default pixel_maca = False
default persistent.pixel_maca = False
default pixel_perguntou = False
default ftempo = False
default persistent.pixel_conversa1vez = False
default pixel_conversa1vez = False
default expo_cave = 0
default persistent.expo_cave = 0
default cave_mini_energia = 0
default cave_resposta = ""



default pratos_preparados = 0
default prato_escolhido = "Lámen"
default chasyu_target = 0
default men_target = 0
default naruto_target = 0
default nitamago_target = 0
default yakumi_target = 0
default chasyu = 0
default men = 0
default naruto = 0
default nitamago = 0
default yakumi = 0
default lamen_certo = 0
default tl_cash = 0
default tl_moral = 0







default cenario_trabalho_1vez = True
default cenario_trabalho_1vez_chefe = True
default cenario_bar_1vez = True
default garcom_1vez = True
default cenario_china_1vez = True
default cenario_tadaima_1vez = True
default cenario_fadolandia_1vez = True
default cenario_salao_1vez = True



default mc_graduacao = 0
default mc_massagem = 0
default mc_fisico = 1
default mc_massagem_db = 0
default mc_drink = 0

default iconchefe = 4
default dia = 1
default dia_sayuri = 99
default dia_cassia = 99
default dia_julia = 99
default dia_priscila = 99
default dia_priscila_evento = 1
default dia_karli = 99
default dia_maria = 1
default tempo = 1
default julia_final3_dia = dia + 5



layeredimage sofia_trabalhando:

    if sofia_lvl == 0:
        "sofia_mc_trabalhando1"

    elif sofia_lvl == 1:
        "sofia_mc_trabalhando2"

    elif sofia_lvl == 2:
        "sofia_mc_trabalhando3"

    if tempo == 2:
        "layer_tarde"

    elif tempo >= 3:
        "layer_noite"

layeredimage mc c_mc_drink:

    if cassino_roupa == "blacktie":
        "cassino_mc_drink_blacktie"

    elif cassino_roupa == "blazer":
        "cassino_mc_drink_blazer"

    elif cassino_roupa == "normal":
        "cassino_mc_drink"

layeredimage mc c_ana_mc:

    if cassino_roupa == "blacktie":
        "cassino_ana_mc_blacktie"

    elif cassino_roupa == "blazer":
        "cassino_ana_mc_blazer"

    elif cassino_roupa == "normal":
        "cassino_ana_mc"

layeredimage cassino_slots_mc:

    if cassino_roupa == "blacktie":
        "slots_mc_blacktie"

    elif cassino_roupa == "blazer":
        "slots_mc_blazer"

    elif cassino_roupa == "normal":
        "slots_mc"

layeredimage cassino_slot_jogando:

    if cassino_roupa == "blacktie":
        "slots_jogando_blacktie"

    elif cassino_roupa == "blazer":
        "slots_jogando_blazer"

    elif cassino_roupa == "normal":
        "slots_jogando"

layeredimage j4_mari_flertando:

    if j4_blazer:
        "mari_flertando_blazer"

    else:
        "mari_flertando"

layeredimage j4_beijo:

    if j4_blazer:
        "julia_e4_beijo_blazer"

    else:
        "julia_e4_beijo"

layeredimage j4_varanda:

    if j4_blazer:
        "julia_e4_varanda_blazer"

    else:
        "julia_e4_varanda"

layeredimage j4_sofa:

    if j4_blazer:
        "julia_e4_sofa_blazer"

    else:
        "julia_e4_sofa"

layeredimage j4_carregando:

    if j4_blazer:
        "julia_carregando_terno"

    else:
        "julia_carregando"

layeredimage mc_mari falando:

    if j4_blazer:
        "mc_mari_falando_terno"

    else:
        "mc_mari_falando"

layeredimage ape_geral:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")



    if casa:
        "ap sala"

    else:
        "ape"










layeredimage ape_new:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')









    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    if lua_especial and tempo >= 3:
        "fundo_especial"

    always:
        "ap_sala_new"




layeredimage ape_chuveiro:

    if casa:
        "ap mc_chuveiro"

    else:
        "mc banho"

layeredimage ape_tv:

    if casa:
        "ap mc_assistindo"

    else:
        "apartamento tv"

layeredimage ape_cama:

    if casa:
        "ap mc_dormindo2"

    else:
        "mc dormindo_dois"

layeredimage ape_celular:

    if casa:
        "ap mc_cel"

    else:
        "apartamento cama_celular"

layeredimage ape_celular_falando:

    if casa:
        "ap mc_cel_falando"

    else:
        "apartamento celular_falando"

layeredimage ape_pensando:

    if casa:
        "ap mc_cel"

    else:
        "apartamento cama_celular"

layeredimage academia:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group lugar:

        attribute academia1:
            "academia1"

    if tempo == 1:
        "academia1_maria"

    if tempo == 2:
        "layer_tarde"

    elif tempo >= 3:
        "layer_noite"

layeredimage ape_xiang:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group lugar:

        attribute um:
            "xiang_ape4"

        attribute ape5:
            "xiang_ape5"

        attribute ape6:
            "xiang_ape6"

        attribute ape7:
            "xiang_ape7"

        attribute ape8:
            "xiang_ape8"

        attribute ape9:
            "xiang_ape9"

        attribute ape10:
            "xiang_ape10"

        attribute ape11:
            "xiang_ape11"

        attribute ape12:
            "xiang_ape12"

        attribute ape13:
            "xiang_ape13"

        attribute ape14:
            "xiang_ape14"

        attribute ape15:
            "xiang_ape15"

        attribute ape16:
            "xiang_ape16"

        attribute ape17:
            "xiang_ape17"

        attribute ape18:
            "xiang_ape18"

layeredimage cidade:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if fundo_especial:
        "fundo_especial"

    if chovendo:
        "fundo_chuva"

    group lugar:

        attribute centro1:
            "cidade_centro1"

        attribute centro2:
            "cidade_centro2"

        attribute centro3:
            "cidade_centro3"

        attribute centro4:
            "cidade_centro4"

        attribute centro6:
            "cidade_centro6"

        attribute centro9:
            "cidade_centro9"

        attribute centro10:
            "cidade_centro10"

        attribute centro12:
            "cidade_centro12"

        attribute centro13:
            "cidade_centro13"

        attribute fliperama:
            "fliperama"

        attribute museu:
            "centro museu"

        attribute tkf:
            "cidade_tkf"

        attribute faux:
            "cidade_faux"

        attribute pizzaria:
            "cidade_pizzaria"

        attribute pizzaria_interior:
            "pizzaria_interior"

        attribute pizzaria_out_dia:
            "pizzaria_out_dia"

        attribute academia2:
            "academia2"

        attribute universidade:
            "universidade_fachada"

        attribute rua_trabalho1:
            "cidade rua_trabalho"

    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    if tempo == 2:
        "layer_tarde"

    elif tempo >= 3:
        "layer_noite"

layeredimage ilha:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if fundo_especial:
        "fundo_especial"

    if chovendo:
        "fundo_chuva"

    group lugar:

        attribute base:
            "ilha_base"

        attribute parque:
            "parque"

        attribute parque2:
            "parque_dois"

        attribute jato_geral:
            "jato geral"

        attribute vale:
            "vale orc"

        attribute praia_entrada:
            "cidade_praia"

        attribute praia:
            "praia_geral"

        attribute praia_gazebo:
            "praia_gazebo"

        attribute praia_gazebo_perto:
            "praia_gazebo_perto"

        attribute praia_quiosque:
            "praia_quiosque"

        attribute quincy_gazebo:
            "quincy_gazebo"

    if tempo == 2:
        "layer_tarde"

    elif tempo >= 3:
        "layer_noite"

    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

layeredimage chinatown:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"

    group lugar:

        attribute geral:
            "chinatown_geral"

        attribute lamen:
            "chinatown_lamen"

        attribute superior:
            "chinatown_superior"

        attribute rua:
            "chinatown_rua"

        attribute esquina:
            "chinatown_esquina"

        attribute entrada:
            "chinatown_entrada"

        attribute caminho:
            "chinatown_caminho"

        attribute templo:
            "chinatown_templo"

        attribute portal:
            "chinatown_portal"

        attribute portal_xiangu:
            "portal_xiangu"

        attribute xiangu_ameaca:
            "xiangu_ameaca"

        attribute templo_lateral:
            "templo_lateral"

        attribute treino_fenju:
            "f_treino_cenario"

        attribute vila_entrada:
            "vila_entrada"

        attribute vila_geral:
            "vila_geral"

        attribute vila_saida:
            "vila_saida"

        attribute vila_gazebo:
            "vila_gazebo"

        attribute vila_escada:
            "vila_escada"

        attribute jardim_geral:
            "jardim_geral"

        attribute jardim_porta:
            "jardim_porta"

        attribute banho_kaira2:
            "banho_kaira2"

        attribute kaira_massagem2:
            "kaira_massagem2"

    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    if tempo == 2:
        "layer_tarde"

    elif tempo >= 3:
        "layer_noite"

layeredimage xiang_casa1:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    always:
        "ape_xiang1"

layeredimage xiangu_casa1:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    always:
        "ape_xiangu1"

layeredimage xiangu_casa2:

    if tempo <= 1:
        Movie(play='fundo_1.webm')


    elif tempo == 2:
        Movie(play='fundo_2.webm')


    else:
        Movie(play='fundo_3.webm')


    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    always:
        "ape_xiangu2"





image black = "#000"
image white = "#ffffff"
image red = "#FF0000"
image logo = "extra/geiko.webp"

transform zoomM:
    zoom 0.2

transform rotate45:
    rotate 45

transform rotate90:
    rotate 90

transform rotate135:
    rotate 135

transform rotate180:
    rotate 180

transform rotate225:
    rotate 225

transform rotate270:
    rotate 270

transform rotate315:
    rotate 315

transform esquerda:
    xpos 250

transform direita:
    xpos 1050

transform centro:
    linear 0.5 xpos 640

transform baixo:
    ypos 150

transform entra_direita:
    xpos 450

transform entra_esquerda:
    xpos -450

transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label after_load:



    $ premium = True



    python:
        if renpy.android:
            persistent.banned = PythonSDLActivity.pegaBanned()

    if persistent.banned:
        $ persistent.banned = False

    if premium:

        python:
            if renpy.android:
                persistent.apoiador = PythonSDLActivity.pegaBacker()


        if renpy.variant("android") and not persistent.apoiador:

            jump nao_apoiador

    call dados_essenciais from _call_dados_essenciais

    return

label nao_apoiador:

    hide screen navegar
    hide screen menu_game
    hide screen quick_menu

    $ renpy.choice_for_skipping()

    $ email = PythonSDLActivity.pegaEmail()

    $ renpy.block_rollback()

    $ renpy.choice_for_skipping()

    scene black

    hide screen navegar
    hide screen menu_game
    hide screen quick_menu

    $ renpy.choice_for_skipping()

    hide screen quick_menu

    $ renpy.block_rollback()

    hide screen quick_menu

    $ renpy.choice_for_skipping()

    "O e-mail da sua conta não tem acesso ao jogo. Para jogar a versão premium de CH, você deve ter um apoio ativo no apoia.se/geiko."

    $ renpy.choice_for_skipping()

    hide screen quick_menu
    $ renpy.block_rollback()

    "Você está tentando acessar o jogo com o e-mail {b}[email]{/b}. Esse é o mesmo e-mail da sua conta do apoia.se? Se sim, beleza."

    "Veja também se você pediu o acesso ao CH no chat do apoia.se/geiko. Nosso atendente irá liberar sua conta quando você pedir."

    "Por último, recomendamos que você leia o {b}Guia para novos apoiadores{/b}. Tem várias dicas de como aproveitar seu apoio."

    menu:
        "Abrir o guia":


            $ renpy.notify("Links externos desativados nesta edicao.")
        "Outra hora":


            pass

    "Qualquer dúvida, entre em contato conosco pelo chat na sua conta do apoia.se. Vamos atender você com toda a atenção!"

    "Seu apoio é muito importante pra gente, e mais do que tudo queremos que você consiga jogar. Então não deixe de entrar em contato."

    $ renpy.quit()



    $ renpy.choice_for_skipping()

    $ renpy.block_rollback()

    $ renpy.choice_for_skipping()

    " "

    jump nao_apoiador

label splashscreen:

    return



label opening:

    jump before_main_menu

transform transform_blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

screen press_to_start():
    tag menu
    add "gui/main_menu.png"

    python:
        if renpy.android:
            userlogado = PythonSDLActivity.pegaLogado();

    if not userlogado:

        vbox:

            spacing 30
            xalign 0.5
            xanchor 0.5
            yalign 0.5
            yanchor 0.5

            add "extra/mensagem_menu.png" xalign 0.5 xanchor 0.5 at transform_blink

            imagebutton auto "extra/botao_login_%s.png" xalign 0.5 xanchor 0.5 action Call("fazer_login")

            imagebutton auto "extra/botao_convidado_%s.png" xalign 0.5 xanchor 0.5 action Call("login_convidado")

    else:

        add "extra/mensagem_inicial.png" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 at transform_blink

        imagemap:
            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Call("login_convidado")

label before_main_menu:



    $ premium = True



    if not persistent.aviso_inicial_v067:

        "???" "Ei... Ei!"

        "???" "Você mesmo!"

        "???" "Desculpe pela tela preta... Mas é que eu queria conversar com {b}você{/b} antes do jogo terminar de carregar."

        show pixie animada with dissolve

        "???" "Ufa. Bem melhor."

        p "Meu nome é Pixie, e eu logo vou te encontrar no jogo. Mas eu queria falar algo só entre a gente antes."





























































        p "Este jogo é desenvolvido por apenas {b}uma pessoa{/b}, o RB, desde 2018. Olha quantos anos! São mais de 70 horas de game pra você curtir!"

        p "CH já foi baixado mais de 3 milhões de vezes. Antes ele estava na Google Play, mas agora a própria {b}Geiko{/b} publica."

        p "Isso permite que o jogo possa ser adulto, com cenas explícitas de nudez, sexo, violência etc. Espero que você goste. Eu, pessoalmente, adoro."



        p "O game é grátis e não tem anúncios, tickets, energia e nada disso. Por isso, para que o RB possa continuar trabalhando nele, seu apoio é importante. "

        p "Se você puder, faça compras ou apoie o game para que o desenvolvedor possa continuar trabalhando nele."

        show pixie provocando with dissolve

        p "Uma última coisa importante. O game trata de temas adultos e é proibido para menores de 18 anos."



        p "Além disso, você precisa estar de acordo com os Termos de Uso e a Política de Privacidade da Geiko. Os dois estão em nosso site."

        menu:
            "Você é maior de idade e concorda com os termos?"
            "Sim, eu tenho 18 anos ou mais":





                pass
            "Não, buaaahh...":


                p "Crianças..."

                $ renpy.quit()













        p "Explicado isso, tenho certeza que você vai adorar. Até daqui a pouquinho! Com muita safadeza!"

        $ persistent.aviso_inicial_v067 = True

    $ renpy.choice_for_skipping()

    play music "extra/music_1.mp3"

    if renpy.variant("android"):

        call screen press_to_start

    scene black

    $ renpy.pause(1, hard=True)

    python:
        if renpy.android:
            userlogado = PythonSDLActivity.pegaLogado();

    if premium:

        if not userlogado:

            jump before_main_menu

    play sound "extra/logo.mp3"

    show white at transform_white
    $ renpy.pause(2, hard=True)

    call dados_essenciais from _call_dados_essenciais_1

    show logo at transform_logo
    $ renpy.pause(5, hard=True)

    if premium:

        python:
            if renpy.android:
                persistent.apoiador = PythonSDLActivity.pegaBacker()


        if renpy.variant("android") and not persistent.apoiador:

            jump nao_apoiador

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(2, hard=True)

    $ renpy.choice_for_skipping()

    python:
        if renpy.android:
            persistent.banned = PythonSDLActivity.pegaBanned()

    if persistent.banned:
        $ persistent.banned = False

    return

transform cidade_trans:
    on show:
        alpha 0
        linear 1.0 alpha 1

    on hide:
        linear 1.0 alpha 0

style menu_principal:
    xysize (1280,720)
    xalign 0
    yalign 0

style menu_conteudo:
    xysize (1280,720)
    left_margin 280
    ypadding 30

screen compra_carta():
    tag menu_aba

    predict False
    zorder 200
    modal True

    add "extra/menu_back.jpg" at menu_back

    frame:

        xysize (1280,720)
        background None

        has vbox

        frame:

            xysize (1280,720)
            xalign 0.5
            yalign 0.5
            background None

            has vbox

            xalign 0.5
            yalign 0.4

            spacing 10

            add "extra/black.jpg" at animacao_carta_black

            if carta_estrela == "1estrela":

                add "extra/estrela.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela

            elif carta_estrela == "2estrelas":

                hbox:

                    xalign 0.5
                    yalign 0.5

                    spacing 5

                    add "extra/estrela.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela
                    add "extra/estrela.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela

            elif carta_estrela == "3estrelas":

                hbox:

                    xalign 0.5
                    yalign 0.5

                    spacing 2

                    add "extra/estrela_colorida.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela
                    add "extra/estrela_colorida.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela
                    add "extra/estrela_colorida.png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_estrela







            add "cards/gacha/card_[carta_escolhida].png" xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 at animacao_carta

            text "{b}Parabéns!{/b} Você conseguiu a carta {b}[carta_nome]{/b}!" xalign 0.5 yalign 0.5 at espera_carta

            imagebutton auto "extra/botao_lojacartas_%s.png" xalign 0.5 yalign 0.5 action ShowMenu("menu_lojacartas") at espera_carta

            imagebutton auto "extra/botao_album_%s.png" xalign 0.5 yalign 0.5 action ShowMenu("menu_album") at espera_carta

screen menu_lojacartas():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    python:
        if renpy.android:
            persistent.coins = PythonSDLActivity.pegaMoedas(0)
            persistent.vid = PythonSDLActivity.pegaVID()



    frame style "menu_conteudo":

        text "Use suas {b}Celebrity Coins{/b} para abrir pacotes de cards e completar seu {b}Álbum{/b}!" xalign 0.5 size 20

        frame:

            xalign 0.5
            yalign 0.7
            background None

            has vbox

            xalign 0.5
            spacing 90

            vbox:

                xalign 0.5
                spacing 25

                hbox:

                    xalign 0.5
                    spacing 10

                    add "extra/celebrity_coin_30.png" xalign 0.5
                    text "{b}[persistent.coins]{/b}" xalign 0.5

                if persistent.coins > 9:

                    imagebutton auto "extra/botao_abrir_pacote_%s.png" action Call("compra_carta")

                else:

                    imagebutton auto "extra/botao_abrir_pacote_cinza_%s.png" action Notify("Você não tem moedas suficientes")

































            vbox:

                xalign 0.5
                spacing 10

                imagebutton auto "extra/botao_moedas_diarias_%s.png" action Call("ganha_daily") xalign 0.5

                text "Ganhe {b}50{/b} Celebrity Coins uma vez a cada 24 horas" xalign 0.5 size 15















screen menu_album():
    tag menu_aba

    predict False
    zorder 100
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    python:
        if renpy.android:
            persistent.card_1 = PythonSDLActivity.pegaCarta1()
            persistent.card_2 = PythonSDLActivity.pegaCarta2()
            persistent.card_3 = PythonSDLActivity.pegaCarta3()
            persistent.card_4 = PythonSDLActivity.pegaCarta4()
            persistent.card_5 = PythonSDLActivity.pegaCarta5()
            persistent.card_501 = PythonSDLActivity.pegaCarta501()
            persistent.card_502 = PythonSDLActivity.pegaCarta502()
            persistent.card_503 = PythonSDLActivity.pegaCarta503()
            persistent.card_504 = PythonSDLActivity.pegaCarta504()
            persistent.card_505 = PythonSDLActivity.pegaCarta505()
            persistent.card_506 = PythonSDLActivity.pegaCarta506()
            persistent.card_507 = PythonSDLActivity.pegaCarta507()
            persistent.card_508 = PythonSDLActivity.pegaCarta508()
            persistent.card_509 = PythonSDLActivity.pegaCarta509()
            persistent.card_510 = PythonSDLActivity.pegaCarta510()
            persistent.card_1001 = PythonSDLActivity.pegaCarta1001()
            persistent.card_1002 = PythonSDLActivity.pegaCarta1002()
            persistent.card_1003 = PythonSDLActivity.pegaCarta1003()
            persistent.card_1004 = PythonSDLActivity.pegaCarta1004()
            persistent.card_1005 = PythonSDLActivity.pegaCarta1005()
            persistent.card_1006 = PythonSDLActivity.pegaCarta1006()
            persistent.card_1007 = PythonSDLActivity.pegaCarta1007()
            persistent.card_1008 = PythonSDLActivity.pegaCarta1008()
            persistent.card_1009 = PythonSDLActivity.pegaCarta1009()
            persistent.card_1010 = PythonSDLActivity.pegaCarta1010()
            persistent.card_1011 = PythonSDLActivity.pegaCarta1011()
            persistent.card_1012 = PythonSDLActivity.pegaCarta1012()
            persistent.card_1013 = PythonSDLActivity.pegaCarta1013()
            persistent.card_1014 = PythonSDLActivity.pegaCarta1014()
            persistent.card_1015 = PythonSDLActivity.pegaCarta1015()

    frame style "menu_conteudo":

        viewport id "cards_menu":

            xsize 850

            scrollbars None
            draggable True
            mousewheel True

            has frame


            left_padding 20
            background None

            vbox:

                spacing 20

                vbox:

                    spacing 10
                    xalign 0.5

                    text "{b}Álbum de Cards Colecionáveis{/b}" xalign 0.5
                    text "Abra pacotes na {b}Loja de Cartas{/b} e complete sua coleção" size 15 xalign 0.5






                vbox:

                    spacing 5

                    hbox:

                        spacing 5

                        add "extra/estrela_colorida.png"
                        add "extra/estrela_colorida.png"
                        add "extra/estrela_colorida.png"

                    hbox:

                        spacing 5

                        if persistent.card_1:

                            imagebutton:
                                idle "cards/gacha/card_1.png"
                                action [ SetVariable("carta_full", "1"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_2:

                            imagebutton:
                                idle "cards/gacha/card_2.png"
                                action [ SetVariable("carta_full", "2"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_3:

                            imagebutton:
                                idle "cards/gacha/card_3.png"
                                action [ SetVariable("carta_full", "3"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_4:

                            imagebutton:
                                idle "cards/gacha/card_4.png"
                                action [ SetVariable("carta_full", "4"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_5:

                            imagebutton:
                                idle "cards/gacha/card_5.png"
                                action [ SetVariable("carta_full", "5"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                vbox:

                    spacing 5

                    hbox:

                        spacing 5

                        add "extra/estrela.png"
                        add "extra/estrela.png"

                    hbox:

                        spacing 5

                        if persistent.card_501:

                            imagebutton:
                                idle "cards/gacha/card_501.png"
                                action [ SetVariable("carta_full", "501"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_502:

                            imagebutton:
                                idle "cards/gacha/card_502.png"
                                action [ SetVariable("carta_full", "502"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_503:

                            imagebutton:
                                idle "cards/gacha/card_503.png"
                                action [ SetVariable("carta_full", "503"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_504:

                            imagebutton:
                                idle "cards/gacha/card_504.png"
                                action [ SetVariable("carta_full", "504"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_505:

                            imagebutton:
                                idle "cards/gacha/card_505.png"
                                action [ SetVariable("carta_full", "505"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                    hbox:

                        spacing 5

                        if persistent.card_506:

                            imagebutton:
                                idle "cards/gacha/card_506.png"
                                action [ SetVariable("carta_full", "506"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_507:

                            imagebutton:
                                idle "cards/gacha/card_507.png"
                                action [ SetVariable("carta_full", "507"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_508:

                            imagebutton:
                                idle "cards/gacha/card_508.png"
                                action [ SetVariable("carta_full", "508"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_509:

                            imagebutton:
                                idle "cards/gacha/card_509.png"
                                action [ SetVariable("carta_full", "509"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_510:

                            imagebutton:
                                idle "cards/gacha/card_510.png"
                                action [ SetVariable("carta_full", "510"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                vbox:
                    spacing 5

                    hbox:

                        spacing 5

                        add "extra/estrela.png"

                    hbox:

                        spacing 5

                        if persistent.card_1001:

                            imagebutton:
                                idle "cards/gacha/card_1001.png"
                                action [ SetVariable("carta_full", "1001"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1002:

                            imagebutton:
                                idle "cards/gacha/card_1002.png"
                                action [ SetVariable("carta_full", "1002"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1003:

                            imagebutton:
                                idle "cards/gacha/card_1003.png"
                                action [ SetVariable("carta_full", "1003"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1004:

                            imagebutton:
                                idle "cards/gacha/card_1004.png"
                                action [ SetVariable("carta_full", "1004"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1005:

                            imagebutton:
                                idle "cards/gacha/card_1005.png"
                                action [ SetVariable("carta_full", "1005"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                    hbox:

                        spacing 5

                        if persistent.card_1006:

                            imagebutton:
                                idle "cards/gacha/card_1006.png"
                                action [ SetVariable("carta_full", "1006"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1007:

                            imagebutton:
                                idle "cards/gacha/card_1007.png"
                                action [ SetVariable("carta_full", "1007"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1008:

                            imagebutton:
                                idle "cards/gacha/card_1008.png"
                                action [ SetVariable("carta_full", "1008"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1009:

                            imagebutton:
                                idle "cards/gacha/card_1009.png"
                                action [ SetVariable("carta_full", "1009"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1010:

                            imagebutton:
                                idle "cards/gacha/card_1010.png"
                                action [ SetVariable("carta_full", "1010"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                    hbox:

                        spacing 5

                        if persistent.card_1011:

                            imagebutton:
                                idle "cards/gacha/card_1011.png"
                                action [ SetVariable("carta_full", "1011"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1012:

                            imagebutton:
                                idle "cards/gacha/card_1012.png"
                                action [ SetVariable("carta_full", "1012"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1013:

                            imagebutton:
                                idle "cards/gacha/card_1013.png"
                                action [ SetVariable("carta_full", "1013"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1014:

                            imagebutton:
                                idle "cards/gacha/card_1014.png"
                                action [ SetVariable("carta_full", "1014"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

                        if persistent.card_1015:

                            imagebutton:
                                idle "cards/gacha/card_1015.png"
                                action [ SetVariable("carta_full", "1015"), ShowMenu("carta_full") ]

                        else:

                            add "cards/gacha/card.png"

        vbar value YScrollValue("cards_menu")

screen carta_full():
    tag menu_aba

    zorder 100

    add "cards/full/card_[carta_full].jpg"

    imagemap:

        ground "extra/transparent.png"
        hotspot (0, 0,1280, 720) focus_mask None action ShowMenu("menu_album")


screen menu_sidebar():

    zorder 100

    frame:
        xsize 250
        xalign 0
        yalign 0.5
        yanchor 0.5
        xpadding 10
        background None

        has vbox
        spacing 5

        imagebutton auto "extra/botao_novidades_%s.png" action ShowMenu("menu_novidades")
        imagebutton auto "extra/botao_loja_%s.png" action ShowMenu("menu_loja")
        imagebutton auto "extra/botao_encontros_%s.png" action ShowMenu("menu_load")
        if show_quick_menu:
            imagebutton auto "extra/botao_save_%s.png" action ShowMenu("menu_salvar")
        imagebutton auto "extra/botao_personagens_%s.webp" action ShowMenu("menu_personagens")
        imagebutton auto "extra/botao_album_%s.png" action ShowMenu("menu_album")
        imagebutton auto "extra/botao_lojacartas_%s.png" action ShowMenu("menu_lojacartas")

    frame:

        xalign 0.0
        yalign 1.0
        xpadding 10
        ypadding 10
        background None

        imagebutton auto "extra/botao_recomecar_%s.png" action ShowMenu("menu_recomecar")

    frame:
        xalign 1.0
        yalign 1.0
        xpadding 10
        ypadding 10
        background None

        imagebutton auto "extra/botao_menu_%s.png" action Return()

transform slot_img:
    linear 0.3 yzoom -1
    linear 0.3 yzoom 1
    repeat

transform treme_balada:
    ypos 0
    linear 0.05 ypos 10
    linear 0.05 ypos 0
    pause 0.5
    repeat

transform treme_vertical:
    ypos 0
    linear 0.05 ypos 10
    linear 0.05 ypos 0
    repeat

transform maria_anda_facil:
    xalign maria_point
    linear 2.0 xalign maria_point + maria_velocidade

transform diana_esquerda:
    xalign 1.0

    pause 3.0


    linear 15.0 xalign 0.0

transform diana_direita:
    xalign 0.0
    pause 3.0
    linear 15.0 xalign 1.0

transform cenario_esquerda:
    xalign 1.0
    linear 12.0 xalign 0.0

transform cenario_direita:
    xalign 0.0
    pause 2.0
    linear 12.0 xalign 1.0

transform cenario_volta_meio:

    linear 1.0 xalign 0.5

transform cena_sobe:
    yalign 1.0
    linear 3.0 yalign 0.0

transform cena_sobe_tudo:
    yalign 0.0
    linear 1.5 yoffset 150

transform cena_chacoalhando:
    linear 0.05 xpos -20
    linear 0.05 xpos +20
    repeat
    linear 3.0 yalign 0.5

transform cena_chega:
    yalign 1.0

    linear 1.0 yalign 0.0


transform animacao_carta_black:
    zoom 20
    alpha 0
    linear 0.5 alpha 1

    linear 0.5 alpha 0
    zoom 0

transform animacao_carta:
    alpha 1
    zoom 0
    pause 3.5

    linear 0.5 zoom 10
    linear 0.5 rotate 360
    linear 0.5 zoom 1

transform animacao_pixie:
    alpha 1
    zoom 0
    linear 0.2 zoom 20
    linear 0.2 alpha 0

transform animacao_estrela:
    alpha 1
    zoom 0
    pause 1
    linear 0.5 zoom 10
    linear 0.5 rotate 360
    linear 0.5 zoom 1
    pause 0.5
    linear 0.5 alpha 0

transform espera_carta:
    alpha 0
    pause 5.5
    linear 1.0 alpha 1

transform black_back:
    alpha 1

transform menu_back:
    xalign 0.0
    xoffset -500
    yalign 0.0
    linear 90 xoffset 0
    linear 90 xoffset -500
    repeat

transform nome_musica:
    xalign 0.0
    xoffset -400
    yalign 0.0
    linear 40 xoffset 800

    repeat

screen menu_principal():
    tag principal


    zorder 99
    modal True



    use menu_sidebar

screen menu_novidades():
    tag menu_aba

    zorder 100
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has hbox

        spacing 30
        yalign 0.5
        yanchor 0.5

        frame:

            xsize 300
            background None
            yalign 0.5
            yanchor 0.5

            has vbox

            spacing 10

            text "{b}Versão [config.version]{/b}" size 30
            text "{b}O que tem de novo?{/b}" size 20

            text "- 2º Final da Sofia Completo" size 15

            text "- Evento extra com a Xiang em casa" size 15

            text "(se a He Xiangu mora na sua casa)" size 15

































































            text "{b}Outros jogos da Geiko{/b}" size 15

            text "- Segredo de Priscila: {a=https://linktr.ee/geikogames}{b}Baixe Aqui{/b}{/a}" size 15

            text "- Encontros: {a=https://www.geiko.net/en/}{b}Baixe Aqui{/b}{/a}" size 15

            text "- Minha Garota: {a=https://linktr.ee/geikogames}{b}Baixe Aqui{/b}{/a}" size 15

            text "- NFC +18: {a=https://www.geiko.net/nfc/}{b}Baixe Aqui{/b}{/a}" size 15

            text "- Nautilus 05: {a=https://www.geiko.net/n05/}{b}Baixe Aqui{/b}{/a}" size 15

            text "- Nautilus 10: {a=https://www.geiko.net/npc/}{b}Baixe Aqui{/b}{/a}" size 15

            text "- Nautilus 20: {a=https://www.geiko.net/n20/}{b}Baixe Aqui{/b}{/a}" size 15



            text "{b}Celebrity Hunter tem 2.253 escolhas, 727.087 palavras e 3.863.655 caracteres{/b}" size 15

            text ""

            hbox:

                spacing 10

                vbox:

                    spacing 10

                    imagebutton auto "celular/wp-icon_%s.png" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "WhatsApp" size 13 xalign 0.5

                vbox:

                    spacing 10

                    imagebutton auto "celular/insta-icon_%s.png" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "Instagram" size 13 xalign 0.5

                vbox:

                    spacing 10

                    imagebutton auto "celular/face-icon_%s.png" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "Facebook" size 13 xalign 0.5

            hbox:

                spacing 10

                vbox:

                    spacing 10

                    imagebutton auto "celular/discord-icon_%s.png" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "Discord" size 13 xalign 0.5

                vbox:

                    spacing 10

                    imagebutton auto "celular/yt-icon_%s.png" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "YouTube" size 13 xalign 0.5

                vbox:

                    spacing 10

                    imagebutton idle "celular/jogos.webp" xalign 0.5 action Notify("Links externos desativados nesta edicao.")

                    text "Mais Jogos" size 13 xalign 0.5

        frame:

            xsize 600
            background None
            yalign 0.5
            yanchor 0.5

            has vbox

            spacing 30

            if premium:

                text "{b}VOCÊ ESTÁ JOGANDO A PREMIUM{/b}" size 30 xalign 0.5

            else:

                text "{b}VEJA TUDO NA VERSÃO PREMIUM{/b}" size 30 xalign 0.5

            add "extra/banner-apoio.webp"

            text "{b}Celebrity Hunter{/b} é feito por apenas uma pessoa. Seu apoio mantém o jogo vivo, além de garantir vantagens exclusivas!" size 15

            if premium:

                text "Obrigado pelo apoio! Aproveite todas as vantagens!" size 22

            else:

                text "Apoie com {b}R$ 10{/b} e saboreie a versão completa!" size 22

            hbox:

                frame:

                    xsize 300
                    background None
                    yalign 0.5
                    yanchor 0.5

                    has vbox

                    spacing 10

                    text "- Cenas +18 exclusivas" size 15

                    text "- Ganhe o dobro de C$ no bar" size 15

                    text "- Dicas onde encontrar pautas" size 15

                frame:

                    xsize 300
                    background None
                    yalign 0.5
                    yanchor 0.5

                    has vbox

                    spacing 10

                    text "- Facilidades para ver cenas" size 15

                    text "- Jogue meses antes dos outros" size 15

                    text "- + TODOS os jogos da Geiko" size 15

            if premium:

                imagebutton auto "extra/botao_saiba_mais_%s.png" action Notify("Links externos desativados nesta edicao.") xalign 0.5



            else:

                imagebutton auto "extra/botao_saiba_mais_%s.png" action Notify("Links externos desativados nesta edicao.") xalign 0.5

screen mostra_video():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    frame style "menu_conteudo":

        has vbox

        spacing 20
        xalign 0.5
        yalign 0.5

        text "{b}Parabéns!{/b} Você ganhou {b}30{/b} Celebrity Coins!" xalign 0.5 yalign 0.5 at espera_carta
        imagebutton auto "extra/botao_lojacartas_%s.png" xalign 0.5 yalign 0.5 action ShowMenu("menu_lojacartas") at espera_carta

screen menu_recomecar():
    tag menu_aba

    zorder 100
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5
        yalign 0.5
        yanchor 0.5

        text "Recomeçar a história para tentar novos caminhos?" xalign 0.5

        text "Recomeçar a história permite jogar todos os encontros novamente e fazer novas escolhas para ver o que acontece" size 15 xalign 0.5

        text "Você {b}NÃO{/b} perderá: Celebrity Reais, Coins, Pontos de Físico, Pontos com o Bao Chang" size 15 xalign 0.5

        text "Você {b}NÃO{/b} precisará pagar novamente: Apartamento, Roupas, Banhos, Pauta, Mercado, Shows da Xiang e outros gastos" size 15 xalign 0.5

        text "Também {b}NÃO{/b} será preciso esperar novamente: Massagem, Fadolândia, Natasha, Trabalho com a Sofia e outros tempos" size 15 xalign 0.5

        text "Não esqueça de usar aba {b}Linhas do Tempo{/b} para jogar vários caminhos diferentes sem perder nenhum" size 15 xalign 0.5

        imagebutton auto "extra/botao_recomecar_%s.png" action Call("reiniciar_jogo") xalign 0.5



















screen text_input_screen():

    modal True

    frame style "tela_padrao":

        has vbox
        spacing 18
        xalign 0.5

        text "Digite como deseja ser chamado" style "tela_texto" xalign 0.5

        vbox:
            spacing 8
            xalign 0.5
            text "Nome" style "tela_texto" xalign 0.5
            button:
                style "input_field_button"
                action Function(prompt_store_input, "mcpnome", "Digite o nome", 20)
                text (mcpnome if mcpnome else "Toque para digitar") style "input_field_text"

        vbox:
            spacing 8
            xalign 0.5
            text "Sobrenome" style "tela_texto" xalign 0.5
            button:
                style "input_field_button"
                action Function(prompt_store_input, "mcsnome", "Digite o sobrenome", 20)
                text (mcsnome if mcsnome else "Toque para digitar") style "input_field_text"

        vbox:
            xalign 0.5
            imagebutton auto "extra/botao_confirmar_%s.png" action [ Hide("text_input_screen"), Return() ] xalign 0.5


screen zeit_screen():

    modal True

    frame style "tela_padrao":

        has vbox
        spacing 18
        xalign 0.5
        text "{b}Reorganize as 9 letras abaixo e confirme{/b}" style "tela_texto" xalign 0.5 xanchor 0.5

        vbox:
            spacing 8
            xalign 0.5
            text "Escreva a palavra correta" style "tela_texto" xalign 0.5
            button:
                style "input_field_button"
                action Function(prompt_store_input, "cave_resposta", "Digite a palavra secreta", 9, allow="zeitgs")
                text (cave_resposta if cave_resposta else "Toque para digitar") style "input_field_text"

        vbox:
            xalign 0.5
            imagebutton auto "extra/botao_confirmar_%s.png" action [ Hide("zeit_screen"), Return() ] xalign 0.5

style input_field_button:
    background Solid("#ffffff22")
    padding (15, 18)
    xalign 0.5
    xminimum 450

style input_field_text:
    color "#ec2098"
    size 24
    xalign 0.5

screen confirmar_nome():

    frame style "tela_padrao":

        has vbox
        xalign 0.5
        spacing 20
        text "Seu nome será {b}[mcpnome]{/b} e seu sobrenome será {b}[mcsnome]{/b}. É isso mesmo?":
            style "tela_texto"
            xalign 0.5
        imagebutton:
            xalign 0.5
            auto "extra/botao_confirmar_%s.png"
            action [ Hide("confirmar_nome"), Return() ]
        imagebutton:
            xalign 0.5
            auto "extra/botao_tela_voltar_%s.png"
            action [ Hide("confirmar_nome"), Jump("escolhe_nome") ]

screen salvar_jogo():

    modal True

    frame style "tela_padrao":

        has vbox

        xalign 0.5
        xanchor 0.5
        spacing 20

        text "Deseja salvar seu progresso na história?" style "tela_texto" xalign 0.5 xanchor 0.5

        imagebutton:
            xalign 0.5
            auto "extra/botao_confirmar_%s.png"
            action [ Hide("salvar_jogo"), FileSave("continue", confirm=False, newest="True", page="None", cycle="False"), Notify("Jogo salvo. Use o botão Carregar ou Continuar para voltar aqui.") ]
        imagebutton:
            xalign 0.5
            auto "extra/botao_tela_voltar_%s.png"
            action [ Hide("salvar_jogo"), Return() ]

screen salvar_nuvem():

    modal True

    frame style "tela_padrao":

        has vbox

        xalign 0.5
        spacing 20

        text "O jogo foi salvo. Quer salvar na nuvem também?" style "tela_texto" xalign 0.5

        imagebutton:
            xalign 0.5
            auto "extra/botao_confirmar_%s.png"
            action [ Hide("salvar_nuvem"), Call("salvar_jogo") ]
        imagebutton:
            xalign 0.5
            auto "extra/botao_tela_voltar_%s.png"
            action [ Hide("salvar_nuvem"), Return() ]

screen avancar_massagem():

    modal True

    frame style "tela_padrao":

        has vbox

        xalign 0.5
        spacing 20

        text "Deseja usar {b}300 Celebrity Coins{/b} para liberar a próxima aula de massagem imediatamente?" style "tela_texto" xalign 0.5

        imagebutton:
            xalign 0.5
            auto "extra/botao_confirmar_%s.png"
            action [ Hide("avancar_massagem"), Call("avanca_massagem") ]
        imagebutton:
            xalign 0.5
            auto "extra/botao_tela_voltar_%s.png"
            action [ Hide("avancar_massagem"), Return() ]

screen menu_funcao():
    tag funcao

    zorder 91

    frame:

        background None
        left_padding 10



        if not renpy.variant("mobile"):

            imagebutton auto "extra/celular_menu_%s.png" action Show("menu_celular")



screen cidade():
    tag cidade

    zorder 90
    modal True













    if tempo > 3:

        imagemap:

            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Call("dormir")

    elif v6_fim and not ep_tutorial:

        imagemap:

            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Jump("encontro_priscila_tutorial")

    elif hora_pauta and tempo < 3:

        imagemap:

            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Call("chefe_game_over")

    else:

        if celular_notificacao:

            imagemap:
                ground "extra/transparent.png"
                hotspot (0, 0,1280, 720) focus_mask None action Call("cena_celular_notificacao")

        else:

            imagebutton auto "images/mapa/bar_%s.png":
                xpos 1000
                ypos 350
                action Call("cenario_bar")
                at cidade_trans

            imagebutton auto "images/mapa/trabalho_%s.png":
                xpos 750
                ypos 220
                action Call("cenario_trabalho")
                at cidade_trans

            imagebutton auto "images/mapa/onibus_%s.png":
                xpos 1050
                ypos 610
                action Jump("cenario_onibus")
                at cidade_trans

            imagebutton auto "images/mapa/parque_%s.png":
                xpos 550
                ypos 300
                action Call("cenario_parque")
                at cidade_trans

            if not casa:

                imagebutton auto "images/mapa/casa_%s.png":
                    xpos 310
                    ypos 100
                    action Call("cenario_casa")
                    at cidade_trans

            else:

                imagebutton auto "images/mapa/ap_%s.png":
                    xpos 610
                    ypos 100
                    action Call("cenario_ap")
                    at cidade_trans

            imagebutton auto "images/mapa/tadaima_%s.png":
                xpos 220
                ypos 270
                action Call("cenario_tadaima")
                at cidade_trans

            imagebutton auto "images/mapa/salao_%s.png":
                xpos 430
                ypos 180
                action Call("cenario_salao")
                at cidade_trans

            imagebutton auto "images/mapa/praia_%s.png":
                xpos 725
                ypos 605
                action Call("cenario_praia")
                at cidade_trans

            imagebutton auto "images/mapa/mercado_%s.png":
                xpos 1150
                ypos 470
                action Call("cenario_mercado")
                at cidade_trans

            imagebutton auto "images/mapa/cassino_%s.png":
                xpos 15
                ypos 370
                action Call("cassino_entrada")
                at cidade_trans

            if carro:

                imagebutton idle "images/botao_carro.webp":
                    xpos 620
                    ypos 220
                    action Call("cenario_estacionamento")
                    at cidade_trans

screen confirmar():
    tag pontos
    zorder 100
    modal True

    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.45

        has vbox

        spacing 25

        text "Este evento vai gastar um período do seu dia. Deseja prosseguir?"

        hbox:
            spacing 100
            xalign .5
            textbutton _("Sim") action [Hide("confirmar"),
                                            Call("cenario_chinatown")]
            textbutton _("Não") action [ Hide("confirmar"),
                                            Show("cidade") ]

screen menu_pontos():
    tag pontos

    zorder 100

    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.45

        has vbox

        spacing 10

        vbox:

            if resultado_encontro == "priscila":

                text "Sua relação com [c]:"
                text "Amizade: [priscila_amizade]/[priscila_amizade_total]"
                text "Sedução: [priscila_seducao]/[priscila_seducao_total]"

            elif resultado_encontro == "sayuri":

                vbox:

                    spacing 5

                    vbox:

                        text "Sua relação com [s]:"
                        text "Amizade: [sayuri_amizade]/[sayuri_amizade_total]"

                    vbox:

                        text "Sua relação com [g]:"
                        text "Sedução: [julia_seducao]/[julia_seducao_total]"

            elif resultado_encontro == "nathan":

                text "Sua relação com [n]:"
                text "Amizade: [nathan_amizade]/[nathan_amizade_total]"

        vbox:

            if resultado_encontro == "priscila":

                text "Cenas especiais vistas:"
                text "Amizade: [priscila_amizade_evento]"
                text "Sedução: [priscila_seducao_evento]"

            elif resultado_encontro == "sayuri":

                text "Cenas especiais vistas:"
                text "Amizade: [sayuri_amizade_evento]"

            elif resultado_encontro == "nathan":

                text "Cenas especiais vistas:"
                text "Amizade: [nathan_amizade_evento]"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
