

screen menu_celular():
    tag celular

    zorder 100
    modal True
    predict False

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("menu_celular")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        vbox:

            xsize 299
            ysize 535
            xalign 0.5
            xanchor 0.5


            spacing 20

            hbox:

                xalign 0.5
                xanchor 0.5
                yalign 0.5
                yanchor 0.5
                spacing 20

                vbox:

                    spacing 5

                    if nona_e1 == "evento":

                        imagebutton auto "celular/user-icon_%s.png" action Show("celular_mc_copia")

                    else:

                        imagebutton auto "celular/user-icon_%s.png" action Show("celular_mc")

                    text "Perfil" size 13 xalign 0.5

                vbox:

                    spacing 5

                    imagebutton auto "celular/wp-icon_%s.png" action Show("menu_celular_wp")

                    text "Mensagens" size 13 xalign 0.5

                vbox:

                    spacing 5

                    imagebutton auto "celular/phone-icon_%s.png" action Show("menu_celular_fone")

                    text "Telefone" size 13 xalign 0.5

            hbox:

                xalign 0.5
                xanchor 0.5
                yalign 0.5
                yanchor 0.5
                spacing 20

                vbox:

                    spacing 5

                    imagebutton auto "celular/clock-icon_%s.png" action Show("menu_celular_relogio")

                    text "Relógio" size 13 xalign 0.5

                vbox:

                    spacing 5

                    imagebutton auto "celular/audio-icon_%s.png" action Show("menu_celular_musica")

                    text "Música" size 13 xalign 0.5

screen menu_celular_relogio():
    tag celular

    zorder 100
    modal True

    python:
        if renpy.android:
            fnext = PythonSDLActivity.pegaFNext()
            epnext = PythonSDLActivity.pegaEPNext()
            masnext = PythonSDLActivity.pegaMasNext()
            tbnext = PythonSDLActivity.pegaTBNext()
            mtnext = PythonSDLActivity.pegaMTNext()
            tlnext = PythonSDLActivity.pegaTLNext()

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("menu_celular_relogio")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 20
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"
        top_padding 30
        left_padding 10
        right_padding 10

        vbox:

            xsize 299





            spacing 30

            text "Relógio" xalign 0.5

            text "Veja a hora dos próximos eventos" text_align 0.5 xalign 0.5 xanchor 0.5 size 15

            text "Trabalho: [tbnext]" size 15

            text "Fadolândia: [fnext]" size 15

            text "Priscila: [epnext]" size 15

            text "Massagem: [masnext]" size 15

            text "Treino: [mtnext]" size 15

            text "Lámen: [tlnext]" size 15

            text "Sofia: [snext]" size 15

            text "[na]: [nnext]" size 15

screen menu_celular_fone():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Show("menu_celular")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        vbox:

            xsize 299
            ysize 535
            xalign 0.5
            xanchor 0.5


            spacing 20

            vbox:

                xalign 0.5
                xanchor 0.5
                yalign 0.5
                yanchor 0.5
                spacing 20

                if v6_fim and estou_na_cidade:

                    imagebutton auto "extra/celular_botao_priscila_%s.png" action [ Hide("menu_celular_fone"), Call("ligar_priscila") ]

                else:

                    text "Você ainda não pode {b}marcar encontros{/b} com ninguém" xalign 0.5 size 15

                    text "Continue a história para liberar" xalign 0.5 size 15

screen menu_celular_musica():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("menu_celular_musica")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        frame:

            xsize 317
            ysize 535
            background None
            yalign 0.5
            yanchor 0.5

            has vbox

            yalign 0.5
            yanchor 0.5
            xalign 0.5

            spacing 15

            hbox:

                spacing 5

                imagebutton auto "celular/audio-play_%s.png" action Play("music", "extra/music_1.mp3", selected="True")

                vbox:

                    yalign 0.5
                    yanchor 0.5

                    text "Defqwop" size 15
                    text "Heart Afire" size 20

            hbox:

                spacing 5



                imagebutton auto "celular/audio-play_%s.png" action Play("music", "audio/music_2.mp3", selected="True")

                vbox:

                    yalign 0.5
                    yanchor 0.5

                    text "Nurko & Last Heroes" size 15
                    text "Promise Me" size 20

            hbox:

                spacing 5

                imagebutton auto "celular/audio-play_%s.png" action Play("music", "audio/music_3.mp3", selected="True")

                vbox:

                    yalign 0.5
                    yanchor 0.5

                    text "Sonnengruss | Vijay & Sofia" size 15
                    text "Storyteller" size 20

            hbox:

                spacing 5

                imagebutton auto "celular/audio-stop_%s.png" action Stop("music")

                text "Parar reprodução" size 20 yalign 0.5 yanchor 0.5


screen menu_celular_wp():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Show("menu_celular")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        vbox:

            xalign 0.5
            yalign 0.1

            spacing 15

            hbox:

                spacing 5

                imagebutton auto "extra/celular_botao_mc_%s.png" action Show("celular_mc")



                if priscila_numero:

                    imagebutton auto "extra/celular_botao_priscila_%s.png" action Show("celular_priscila")

                if sayuri_numero:

                    imagebutton auto "extra/celular_botao_sayuri_%s.png" action Show("celular_sayuri")

            hbox:

                spacing 5

                if cassia_numero:

                    imagebutton auto "extra/celular_botao_cassia_%s.png" action Show("celular_cassia")

                if nathan_numero:

                    imagebutton auto "extra/celular_botao_nathan_%s.png" action Show("celular_nathan")

                if julia_numero:

                    imagebutton auto "extra/celular_botao_julia_%s.png" action Show("celular_julia")

            hbox:

                spacing 5

                if diana_numero:

                    imagebutton auto "extra/celular_botao_diana_%s.png" action Show("celular_diana")

screen celular_mc():
    tag celular

    zorder 100
    modal True
    predict False

    python:
        if renpy.android:
            persistent.coins = PythonSDLActivity.pegaMoedas(0)
            cash = PythonSDLActivity.pegaCash()
            mc_fisico = PythonSDLActivity.pegaFpontos()
            bao_pontos = PythonSDLActivity.pegaBao()
            
            if userlogado:
                useremail = PythonSDLActivity.pegaEmail()

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_mc")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        xsize 304
        ysize 590
        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        vbox:

            xalign 0.5
            xanchor 0.5
            spacing 30

            vbox:

                xalign 0.5
                xanchor 0.5

                add "extra/celular_botao_mc_idle.png" at center

                text "[mcc]" size 18

            hbox:

                spacing 50
                xalign 0.5
                xanchor 0.5

                vbox:

                    spacing 5

                    add "extra/coin_25.png" xalign 0.5 xanchor 0.5
                    text "[persistent.coins]" size 14 xalign 0.5 xanchor 0.5

                vbox:

                    spacing 5

                    add "extra/money.png" xalign 0.5 xanchor 0.5
                    text "[cash]" size 14 xalign 0.5 xanchor 0.5

            text "Habilidades" xalign 0.5 xanchor 0.5 size 18

            vbox:

                spacing 5

                text "Massagem: [mc_massagem]/10" size 14
                text "Físico: [mc_fisico]/500" size 14
                text "Bao Chang: [bao_pontos]/300" size 14






            text "Conta" xalign 0.5 xanchor 0.5 size 18

            if userlogado:

                text "E-mail: [useremail]" size 14

            else:

                imagebutton auto "extra/botao_login_%s.png" xalign 0.5 xanchor 0.5 action Call("fazer_login")

screen celular_mc_copia():
    tag celular

    zorder 100
    modal True
    predict False

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_mc_copia")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has frame

        xsize 304
        ysize 590
        top_margin 45
        left_margin 5
        background "celular/android-fundo.jpg"

        vbox:

            xalign 0.5
            xanchor 0.5
            spacing 30

            vbox:

                xalign 0.5
                xanchor 0.5

                add "extra/celular_botao_mc_idle.png" at center

                text "[mcc]" size 18

            hbox:

                spacing 50
                xalign 0.5
                xanchor 0.5

                vbox:

                    spacing 5

                    add "extra/coin_25.png" xalign 0.5 xanchor 0.5
                    text "[persistent.coins]" size 14 xalign 0.5 xanchor 0.5

                vbox:

                    spacing 5

                    add "extra/money.png" xalign 0.5 xanchor 0.5
                    text "[novo_cash]" size 14 xalign 0.5 xanchor 0.5

            text "Habilidades" xalign 0.5 xanchor 0.5 size 18

            vbox:

                spacing 5

                text "Massagem: [mc_massagem]/10" size 14
                text "Físico: [mc_fisico]/500" size 14
                text "Bao Chang: [bao_pontos]/300" size 14






            text "Conta" xalign 0.5 xanchor 0.5 size 18

            if userlogado:

                text "E-mail: [useremail]" size 14

            else:

                imagebutton auto "extra/botao_login_%s.png" xalign 0.5 xanchor 0.5 action Call("fazer_login")

screen celular_hacker():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_hacker")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_fantasma.png"
            text "$#&@!%" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if nona_e1 == "continua":

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Tudo bem [mc]" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Esse cara fala ne" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Ja resolvi seu problema" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Quando sair dai eu te chamo" style "celular_msg"
                        window style "wp_right"

                elif nona_e1 == "banco":

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Que bom que tudo foi resolvido" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Agora que eu tenho sua atencao" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "O que voce acha da gente se ver" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Vem me encontrar aqui no centro" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Onde os jogos se escondiam antes do celular" style "celular_msg"
                        window style "wp_right"

screen celular_diana():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_diana")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_diana.png"
            text "Diana" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if diana_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Como vai, [mc]? Tudo bem?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Eu vi a materia sobre mim no site" style "celular_msg"
                        window style "wp_right"



                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "O que vc acha de me ver cantar?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Uma apresentação apenas pra vc" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Aqui no Cassino amanha. Vc topa?" style "celular_msg"
                        window style "wp_right"

                    if diana_cel_msg1_r == "nada":

                        textbutton _("Responder") action [Hide("celular_diana"), Call("diana_cel_msg1_resposta")]

                    elif diana_cel_msg1_r == "seducao":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Com certeza." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Quero muito ver você cantando." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ótimo! Então eu te espero amanhã." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Vai ser no Jazz Corner 20h" style "celular_msg"
                            window style "wp_right"

                    elif diana_cel_msg1_r == "amizade":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Topo, sim." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Estou louco pra conhecer o Cassino." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Então te espero no Jazz Corner 20h" style "celular_msg"
                            window style "wp_right"

screen celular_julia():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_julia")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_julia.png"
            text "Júlia" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if julia_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "E ai bobao?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Olha quem n sai do cel" style "celular_msg"
                        window style "wp_right"

                    add "cards/full/card_505.jpg" size (300,169)

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Linda né?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Quando der passa no Tadaima" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Vem pra me dar um alo" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Eu trabalho todo dia a tarde" style "celular_msg"
                        window style "wp_right"

                    if julia_cel_msg1_resposta_check:

                        textbutton _("Responder") action [Hide("celular_julia"), Call("julia_cel_msg1_resposta")]

                    if julia_cel_msg1_r == "sim":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Valeu. Manda mais quando der." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Sabia qe vc ia gostar safado" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Mas nao esqece de mim" style "celular_msg"
                            window style "wp_right"

                    elif julia_cel_msg1_r == "nao":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Para de mandar foto assim." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não é certo com a [s]." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Para de ser sem graca" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text ":T" style "celular_msg"
                            window style "wp_right"

                if julia_cel_msg2:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    if julia_conversou:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Fala ai sr psicologico." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ta tendo uma palestra chatona hj" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Dai resolvi mandar pra vc" style "celular_msg"
                            window style "wp_right"

                        add "cards/full/card_508.jpg" size (300,169)

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "So linda fala ai" style "celular_msg"
                            window style "wp_right"

                    if julia_e1 == "seducao":

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Essa aqui eh pelo seu trabalho hj" style "celular_msg"
                            window style "wp_right"

                        add "images/julia selfie_calcinha.jpg" size (300,169)

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Pra te ajuda depois" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "N se preocupe q vai te mais" style "celular_msg"
                            window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Brigada por hj" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Vc foi muito bacana :*" style "celular_msg"
                        window style "wp_right"

                if julia_cel_msg3:

                    if not sayuri_e3 == "horrivel":

                        text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "eu vi a roupa que a [s] comprou" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "vc fez um bom trabalho" style "celular_msg"
                            window style "wp_right"

                        if sayuri_e3 == "beijo":

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "só que ela n para de suspirar" style "celular_msg"
                                window style "wp_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "ela ta mto esquisita" style "celular_msg"
                                window style "wp_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "aconteu alguma coisa q eu deva saber?" style "celular_msg"
                                window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "qer ver a premiacao comigo?" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "a gente pode ver aqui em casa" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "vamos estar so nos dois..." style "celular_msg"
                            window style "wp_right"

                if julia_cel_msg4:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    if s4_julia_good:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "ja tamo em casa. ta tudo legal" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "dsculpa por hj e valeu" style "celular_msg"
                            window style "wp_right"

                        if sayuri_intencao == "namoro":

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "eu n devia t feito o q eu fiz" style "celular_msg"
                                window style "wp_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "e vc fez o certo. n to triste to feliz" style "celular_msg"
                                window style "wp_right"

                        if julia_seducao >= 9:

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "e aqui uma recompensa p vc ;)" style "celular_msg"
                                window style "wp_right"

                            add "images/foto julia_cama.jpg" xalign 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "a say n consgiu te falar um treco" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "ela qria te chamar pra sair amnha" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "liga pra ela e n fala que fui eu." style "celular_msg"
                        window style "wp_right"

                    if julia_e1 == "seducao" or julia_e2 == "seducao":

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "beijo no pipi. qero sentir ele..." style "celular_msg"
                            window style "wp_right"

                if julia_cel_msg5 == "safado":

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        xalign 1.0
                        window style "wp_mc_left"
                        window style "wpmc":
                            text "Como tá minha sapeca? Pensando sacanagem?" style "celular_msg_mc"
                        window style "wp_mc_right"

                    if julia_cel_msg5_r:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "É... desculpa é a Carol..." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "A Ju deixou o cel comigo..." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Voce pode vir na faculdade agora?" style "celular_msg"
                            window style "wp_right"

                if julia_cel_msg5 == "amigo":

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        xalign 1.0
                        window style "wp_mc_left"
                        window style "wpmc":
                            text "Fala, Ju. Tudo legal com você?" style "celular_msg_mc"
                        window style "wp_mc_right"

                    if julia_cel_msg5_r:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Oi, [mc]. É a Carol." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "A Ju deixou o cel comigo..." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Voce pode vir na faculdade agora?" style "celular_msg"
                            window style "wp_right"

                if julia_cel_msg6:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Ei. Posso ligar?" style "celular_msg"
                        window style "wp_right"

                    if not julia_cel_msg6_r:

                        imagebutton auto "celular/botao_responder_%s.png" action [ Hide("celular_julia"), Jump("julia_evento5") ]

                    else:

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Claro. Estou esperando." style "celular_msg_mc"
                            window style "wp_mc_right"








screen celular_nathan():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_nathan")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_nathan.png"
            text "[n]" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if nathan_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Fala ae [mc]" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Olha o que o Fabricio me mandou" style "celular_msg"
                        window style "wp_right"

                    add "cards/full/card_506.jpg" size (300,169)

                    if n1_ajuda:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "E nao esquece que voce ia me ajudar" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "To contando com vc" style "celular_msg"
                            window style "wp_right"

                if nathan_cel_msg2:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        xalign 1.0
                        window style "wp_mc_left"
                        window style "wpmc":
                            text "Fala, cara. Como tão as coisas?" style "celular_msg_mc"
                        window style "wp_mc_right"

                    hbox:
                        xalign 1.0
                        window style "wp_mc_left"
                        window style "wpmc":
                            text "Tá tudo bem quanto ao rolo lá?" style "celular_msg_mc"
                        window style "wp_mc_right"

                    if nathan_cel_msg2_r:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ta tudo acontecendo ainda cara" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Vc pode me encontrar no bar" style "celular_msg"
                            window style "wp_right"

                        if nathan_cel_msg2_r2 == "nao":

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Não vai dar cara. Malz" style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "td bem" style "celular_msg"
                                window style "wp_right"

                        elif nathan_cel_msg2_r2 == "sim":

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Claro. Logo eu tô lá." style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "fechou to indo tambem" style "celular_msg"
                                window style "wp_right"

                if nathan_cel_msg3:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Fala [mc]. a audiencia é amanha" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "vc pode me encontrar no forum 14h?" style "celular_msg"
                        window style "wp_right"

                    if not nathan_cel_msg3_resposta:

                        imagebutton auto "celular/botao_responder_%s.png":
                            action [ Hide("celular_nathan"), Jump("nathan_cel_msg3_resposta") ]

                if nathan_cel_msg4:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "A audiencia deu tudo certo!" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "O que vc acha de cmoemorar?" style "celular_msg"
                        window style "wp_right"

                    if not nathan_cel_msg4_resposta:

                        imagebutton auto "celular/botao_responder_%s.png":
                            action [ Hide("celular_nathan"), Jump("nathan_evento5_pre") ]

                    else:

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Que bom que deu tudo certo!" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Vamos na pizzaria do centro?" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Fechou. Pizzaria na parte da tarde" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Te espero lá abs" style "celular_msg"
                            window style "wp_right"

                if nathan_cel_msg5:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Oi [mc] queria falar c vc" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Qnd der me liga?" style "celular_msg"
                        window style "wp_right"

                    if not nathan_cel_msg5_resposta:

                        imagebutton auto "celular/botao_responder_%s.png":
                            action [ Hide("celular_nathan"), Jump("nathan_evento6") ]



screen celular_cassia():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_cassia")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_cassia.png"
            text "[j]" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if cassia_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Ô, pombinho!" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "O [n] costuma aparecer no bar perto da redação durante a noite." style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "É sua chance! Vai lá!" style "celular_msg"
                        window style "wp_right"

                if cassia_cel_msg2:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Só quero avisar que a matéria já foi publicada" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Quem mandou não aceitar minha proposta?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Boa sorte com a bonequinha, pombinho" style "celular_msg"
                        window style "wp_right"

                if cassia_cel_msg3:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Oi, pombinho. Tava com saudades?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "A matéria sobre o [n] tá bombando no site" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Que acha de comemorar em casa?" style "celular_msg"
                        window style "wp_right"

                    if not cassia_cel_msg3_resposta_check:

                        textbutton _("Responder") action [Hide("celular_cassia"),
                                                                        Call("cassia_cel_msg3_resposta")]

                    if cassia_cel_msg3_r == "recusou":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "É melhor a gente não se ver." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Olha que você vai perder bebê" style "celular_msg"
                            window style "wp_right"

                        add "cassia_n_foto.jpg"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Tem certeza?" style "celular_msg"
                            window style "wp_right"

                    if cassia_cel_msg3_rA:

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Certo. Vou aí. Onde fica?" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Eu sabia que você ia querer" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Eu moro no condomínio Gênesis, Bloco 3, Ap 6" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Pode chegar umas 20h" style "celular_msg"
                            window style "wp_right"




screen celular_sayuri():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_sayuri")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_sayuri.png"
            text "[s]" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if sayuri_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Olo? Alo" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Voce ta ai ?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "jjjjjjjjjjj" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "naaaaaooo jjj" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text ":'(" style "celular_msg"
                        window style "wp_right"

                    if sayuri_cel_msg1_resposta_check:

                        textbutton _("Responder") action [Hide("celular_sayuri"),
                                                                        Call("sayuri_cel_msg1_resposta")]

                    if sayuri_cel_msg1_r == "amizade":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Oi, Sayuri. Aqui é o [mc]." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Tudo bem?" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Você tá legal? Recebi umas mensagens estranhas..." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ah obrigada por r espond jjj" style "celular_msg"
                            window style "wp_right"

                    if not sayuri_cel_msg1_r == "nada":

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "pri meir vez jj q escre vo no cel" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "ta tu do erad..... jj poss o ligar?" style "celular_msg"
                            window style "wp_right"

                        if sayuri_cel_msg2_resposta_check:

                            textbutton _("Responder") action [ Hide("celular_sayuri"), Call("sayuri_cel_msg2_resposta") ]

                if sayuri_cel_msg3:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Oi, [mc]." style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "É a [s], tudo bem?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "A [g] me disse que você foi com ela na faculdade." style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Obrigada por se entender com ela." style "celular_msg"
                        window style "wp_right"

                    if sayuri_cel_msg3_r == "nada":

                        textbutton _("Responder") action [ Hide("celular_sayuri"), Call("sayuri_cel_msg3_resposta") ]

                    if not sayuri_cel_msg3_r == "nada":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não foi nada de mais." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Encontrei ela no restaurante e ela me chamou." style "celular_msg_mc"
                            window style "wp_mc_right"

                        add "images/foto sayuri_close.jpg" xalign 0.5

                    if not sayuri_cel_msg3_r == "nada" and not sayuri_cel_msg3_r == "iniciando":

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "meu deus o que eu fiz" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "nao olhe" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "como eu apago issooo" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "naaaaooooo" style "celular_msg"
                            window style "wp_right"

                    if sayuri_cel_msg3_r == "linda":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Nossa! Você tá linda!" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Ver uma foto sua já melhorou meu dia!" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "e e e ee" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "n n n  n nao" style "celular_msg"
                            window style "wp_right"

                    elif sayuri_cel_msg3_r == "mentira":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não sei do que você tá falando." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não apareceu nada aqui." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "nao? ufa" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Não é nada." style "celular_msg"
                            window style "wp_right"

                    elif sayuri_cel_msg3_r == "normal":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Acho que você tirou uma selfie sem querer." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "É normal isso. Relaxa." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "o o o ok" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Desculpa. Foi sem querer." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não precisa se desculpar. Acontece :)" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text ":)" style "celular_msg"
                            window style "wp_right"

                if sayuri_cel_msg4:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Oi, [mc]. Tudo bem?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Você está tranquilo agora?" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Você pode ir no Tadaima a noite?" style "celular_msg"
                        window style "wp_right"

                    if sayuri_cel_msg4_r == "nada":

                        textbutton _("Responder") action [ Hide("celular_sayuri"), Call("sayuri_cel_msg4_resposta") ]

                    if sayuri_cel_msg4_r == "errado":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Com certeza. Tô passando aí depois." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Combinado. Até daqui a pouco." style "celular_msg"
                            window style "wp_right"

                    if sayuri_cel_msg4_r == "certo":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Se você for, eu também vou." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Eu vou estar! Logo a gente se vê." style "celular_msg"
                            window style "wp_right"

                if sayuri_cel_msg5:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    if not sayuri_adeus:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "[mc]... tudo bem?" style "celular_msg"
                            window style "wp_right"

                    else:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Oi. A gente precisa conversar." style "celular_msg"
                            window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Você pode me ligar?" style "celular_msg"
                        window style "wp_right"

                    if sayuri_cel_msg5_r == "nada":

                        imagebutton auto "celular/botao_responder_%s.png" action [ Hide("celular_priscila"), Jump("sayuri_evento6") ]

                    elif sayuri_cel_msg5_r == "respondido":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Claro. To ligando" style "celular_msg_mc"
                            window style "wp_mc_right"



screen celular_priscila():
    tag celular

    zorder 100
    modal True

    imagemap:

        xalign 0.5
        yalign 0.5

        auto "extra/celular_%s.png"
        hotspot (160, 635, 50, 55) action Hide("celular_priscila")

    frame:

        xsize 364
        ysize 620
        left_padding 20
        right_padding 40
        top_padding 30
        bottom_padding 0
        xalign 0.5
        background None

        has vbox

        frame:

            background "celular/wp-topo.jpg"
            top_margin 40
            xsize 317
            ysize 89
            left_margin 4

            has hbox

            xalign 0.15
            yalign 0.50
            spacing 10

            add "celular/botao_wp_priscila.png"
            text "[c]" yalign 0.45



        frame:

            background "celular/wp-fundo.jpg"
            xsize 317
            ysize 486
            left_margin 4

            has viewport id "celular_info"
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0
            xsize 310

            frame:

                left_padding 3
                right_padding 3
                background None
                xsize 310

                has vbox

                spacing 15
                xsize 303

                if priscila_cel_msg1:

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Oi [mc] :3" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Desculpa por ontm. brigada por me ajudar. te devo uma" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Eu ainda to na cidade vamos conversar mais depois Bj" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg1_resposta_check:

                        textbutton _("Responder") action [Hide("celular_priscila"),
                                                                        Call("priscila_cel_msg1_resposta")]

                    if priscila_cel_msg1_r == "amizade":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não tem o que agracer, Pri." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Vamos se encontrar sim." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Vc é um fofo :*" style "celular_msg"
                            window style "wp_right"

                    elif priscila_cel_msg1_r == "seducao":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Foi um prazer passar a noite com vc." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Também quero te ver de novo." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Vc me deixa >///<" style "celular_msg"
                            window style "wp_right"

                    elif priscila_cel_msg1_r == "zoado":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Como você conseguiu meu celular?" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "N seja bobo xD" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Eu liguei na sua revista >_<" style "celular_msg"
                            window style "wp_right"

                if priscila_cel_msg2:

                    if priscila_cel_msg2_n:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Oi olha eu aqui :3" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ontem foi... >///<" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "N tenho coragem de escrever!!" style "celular_msg"
                            window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Olha.." style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "To perto da praça do lado da sua revista" style "celular_msg"
                        window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Qr conversar agora?" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg2_resposta_check:

                        textbutton _("Responder") action [Hide("celular_priscila"),
                                                                        Call("priscila_cel_msg2_resposta")]

                    if priscila_cel_msg2_r == "amizade":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Claro!" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Já estou indo. Te vejo lá." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Legal! To chegando :*" style "celular_msg"
                            window style "wp_right"

                    if priscila_cel_msg2_r == "zoado":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Vou dar uma olhada aqui se dá..." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ok..." style "celular_msg"
                            window style "wp_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Acho que vai dar sim." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Vou só terminar aqui um negócio e já saio." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Ta. Brigada" style "celular_msg"
                            window style "wp_right"

                    if priscila_cel_msg2_r == "finalizado":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Olha. Ontem foi legal." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Mas não quero me envolver com você agora." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "..." style "celular_msg"
                            window style "wp_right"

                if priscila_cel_msg3:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Olha!" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg3_r == "amizade":

                        add "images/cel_foto_pri1_ami.jpg" xalign 0.5

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Presentinho p vc" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Pra alegrar seu dia :*" style "celular_msg"
                            window style "wp_right"

                        if priscila_cel_msg3_rA:

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Adorei. Você é linda" style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Fiquei mais feliz agora" style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "Era o q eu queria :)" style "celular_msg"
                                window style "wp_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "Bom dia! <3" style "celular_msg"
                                window style "wp_right"

                    if priscila_cel_msg3_r == "seducao":

                        add "images/cel_foto_pri1_sed.jpg" xalign 0.5

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Pra vc n esquecer o q eu tenho p vc" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text ">///<" style "celular_msg"
                            window style "wp_right"

                        if priscila_cel_msg3_rA:

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Você sabe como mexer comigo..." style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                xalign 1.0
                                window style "wp_mc_left"
                                window style "wpmc":
                                    text "Não vejo a hora de te ver de novo" style "celular_msg_mc"
                                window style "wp_mc_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "Vc tb mexe comigo" style "celular_msg"
                                window style "wp_right"

                            hbox:
                                window style "wp_left"
                                window style "wp":
                                    text "Vou te mandar mais foto depois..." style "celular_msg"
                                window style "wp_right"

                if priscila_cel_msg4:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Minha agente tirou" style "celular_msg"
                        window style "wp_right"

                    add "images/foto priscila_aviao.jpg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Ja tamo voando p captal :)" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg4_r == "cuzao":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Quase eu vejo seu peitão todo nessa foto '¬'" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "... --'" style "celular_msg"
                            window style "wp_right"

                    elif priscila_cel_msg4_r == "amizade":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Tô muito ansioso pra te ver" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Chega logo" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Eu q to!!!" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text ":*" style "celular_msg"
                            window style "wp_right"

                    elif priscila_cel_msg4_r == "seducao":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Só de ver sua foto já fico todo..." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Não vejo a hora de te ver ao vivo" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Aiii [mc] eu tb fico" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text ">///<" style "celular_msg"
                            window style "wp_right"

                    if priscila_cel_msg4_rA == "deboa":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Bom dia. Foi boa a viagem?" style "celular_msg_mc"
                            window style "wp_mc_right"

                    elif priscila_cel_msg4_rA == "desesperado":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Ainda não chegou? Cadê você???" style "celular_msg_mc"
                            window style "wp_mc_right"

                if priscila_cel_msg5:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Adeus [mc] obrigada por tudo" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg5_r:

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Como assim? Onde você tá indo?" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Fala comigo" style "celular_msg_mc"
                            window style "wp_mc_right"

                if priscila_cel_msg6:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    if priscila_namoro:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "oii amor!!! posso falar amor?" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "ja to com saudades </3" style "celular_msg"
                            window style "wp_right"

                    else:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Oi [mc]. tudo bem?" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Como ta meu melhor amigo?" style "celular_msg"
                            window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "voce pode ligar a tv??? rapido!" style "celular_msg"
                        window style "wp_right"

                    if priscila_cel_msg6_r == "nada":

                        imagebutton auto "celular/botao_responder_%s.png" action [ Hide("celular_priscila"),
                                                                        Jump("priscila_evento5") ]

                    elif priscila_cel_msg6_r == "viu":

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Acabei de ver. Vai ser incrível!" style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "que legal <333 posso te ligar?" style "celular_msg"
                            window style "wp_right"

                if priscila_cel_msg7:

                    text "-- Anteriores --" style "celular_msg" xalign 0.5 xanchor 0.5

                    if priscila_namoro:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "oi lindo. q sdds de vc <3" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Qr ir na grav cmg hj?" style "celular_msg"
                            window style "wp_right"

                    else:

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Oi! Td bem?" style "celular_msg"
                            window style "wp_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "Qr ir na grav cmg hj?" style "celular_msg"
                            window style "wp_right"

                    hbox:
                        window style "wp_left"
                        window style "wp":
                            text "Prmeto q vai ser mt legal!" style "celular_msg"
                        window style "wp_right"

                    if not priscila_cel_msg7_r:

                        imagebutton auto "celular/botao_responder_%s.png" action [ Hide("celular_priscila"),
                                                                        Jump("priscila_evento6") ]

                    else:

                        hbox:
                            xalign 1.0
                            window style "wp_mc_left"
                            window style "wpmc":
                                text "Tô passando aí no hotel." style "celular_msg_mc"
                            window style "wp_mc_right"

                        hbox:
                            window style "wp_left"
                            window style "wp":
                                text "To esperando ;*" style "celular_msg"
                            window style "wp_right"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
