init python:

    config_verde_claro = "#cc0066"  
    config_verde_escuro = "#cc0033"  
    config_verde_brilhante = "#cc0099"  
    config_preto = "#000000"  
    config_preto_transparente = "#00000099"  
    config_cinza_escuro = "#222222"  
    config_branco = "#ffffff"  

screen menu_personagens():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 50
        xalign 0.5

        vbox:

            spacing 10
            xalign 0.5

            text "{b}Personagens e Finais{/b}" xalign 0.5
            text "Veja quais personagens você já encontrou e quantos ainda faltam" size 15 xalign 0.5
            text "{b}Aperte no botão do personagem{/b} para ver quais finais você já viveu ou ainda pode viver com ele" size 15 xalign 0.5


        vbox:

            xalign 0.5
            yalign 0.5
            spacing 20

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if priscila_e1 != "nada":

                    add "extra/celular_botao_priscila_idle.png"



                else:

                    add "extra/fantasma.png"

                if not sayuri_evento1_check:

                    imagebutton idle "extra/celular_botao_sayuri_idle.png" action ShowMenu("memorias_sayuri")



                else:

                    add "extra/fantasma.png"

                if v2_fim:

                    add "extra/celular_botao_cassia_idle.png"

                else:

                    add "extra/fantasma.png"

                if nathan_e1 != "nada":

                    imagebutton idle "extra/celular_botao_nathan_idle.png" action ShowMenu("memorias_nathan")



                else:

                    add "extra/fantasma.png"

                if sayuri_e2 != "nada":

                    imagebutton idle "extra/celular_botao_julia_idle.png" action ShowMenu("memorias_julia")

                else:

                    add "extra/fantasma.png"

                if diana_e1 != "nada":

                    imagebutton idle "extra/celular_botao_diana_idle.png" action ShowMenu("memorias_diana")

                else:

                    add "extra/fantasma.png"

                if sofia_e1 != "nada":

                    add "extra/botao_sofia_idle.png"

                else:

                    add "extra/fantasma.png"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if natasha_e1 != "nada":

                    add "extra/botao_natasha_idle.png"

                else:

                    add "extra/fantasma.png"

                if mc_massagem > 0:

                    add "extra/botao_karli_idle.png"

                else:

                    add "extra/fantasma.png"

                if thaynara_evento > 0:

                    add "extra/botao_thaynara_idle.png"

                else:

                    add "extra/fantasma.png"

                if stifler_e1 != "nada":

                    add "extra/botao_distrito_idle.png"

                else:

                    add "extra/fantasma.png"

                if maria_evento > 0:

                    add "extra/botao_maria_idle.png"

                else:

                    add "extra/fantasma.png"

                if quincy_e1:

                    add "extra/botao_selena_idle.png"

                else:

                    add "extra/fantasma.png"

                if banho_evento > 0:

                    add "extra/botao_china_idle.png"

                else:

                    add "extra/fantasma.png"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if v39_fim:

                    add "extra/botao_naru_idle.webp"

                else:

                    add "extra/fantasma.png"

                if quincy_evento > 0:

                    add "extra/botao_jones_idle.png"

                else:

                    add "extra/fantasma.png"

                if fado_pixel_comeu:

                    add "extra/botao_fadolandia_idle.png"

                else:

                    add "extra/fantasma.png"

                if ana_evento > 0:

                    add "extra/botao_ana_idle.png"

                else:

                    add "extra/fantasma.png"

                if tkf_evento1:

                    add "extra/botao_tkf_idle.png"

                else:

                    add "extra/fantasma.png"

                if v30_fim:

                    add "extra/botao_nona_idle.webp"

                else:

                    add "extra/fantasma.png"

                add "extra/fantasma.png"

screen memorias_priscila2():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/celular_botao_priscila_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena10:
                    imagebutton auto "extra/replay_pri10_%s.jpg" action Replay("priscila_e4_finalmorte")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena11:
                    imagebutton auto "extra/replay_pri11_%s.jpg" action Replay("priscila_e4_finalvence")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena12:
                    imagebutton auto "extra/replay_pri12_%s.jpg" action Replay("priscila_e5_cenaaviao")

                else:
                    add "extra/replay.jpg"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena13:
                    imagebutton auto "extra/replay_pri13_%s.jpg" action Replay("priscila_e5_cenasocou")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena14:
                    imagebutton auto "extra/replay_pri14_%s.jpg" action Replay("priscila_e5_replaybeijo")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena15:
                    imagebutton auto "extra/replay_pri15_%s.jpg" action Replay("priscila_e5_replaybeijoextra")

                else:
                    add "extra/replay.jpg"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena16:
                    imagebutton auto "extra/replay_pri16_%s.jpg" action Replay("priscila_e5_soco")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena17:
                    imagebutton auto "extra/replay_pri17_%s.jpg" action Replay("priscila_e5_replaychutado")

                else:
                    add "extra/replay.jpg"

        hbox:

            spacing 10
            xalign 0.5

            textbutton _("Página 1") action ShowMenu("memorias_priscila"):
                xalign 0.5

            text "|" xalign 0.5

            textbutton _("Página 2") action ShowMenu("memorias_priscila2") xalign 0.5

screen memorias_priscila():
    tag menu_aba

    zorder 99
    modal True



    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/celular_botao_priscila_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena1:
                    imagebutton auto "extra/replay_pri1_%s.jpg" action Replay("final_amizade")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena2:
                    imagebutton auto "extra/replay_pri2_%s.jpg" action Replay("priscila_e1_finalseducao")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena3:
                    imagebutton auto "extra/replay_pri3_%s.jpg" action Replay("priscila_e2_finalseducao")

                else:
                    add "extra/replay.jpg"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena4:
                    imagebutton auto "extra/replay_pri4_%s.jpg" action Replay("priscila_e2_finalamizade")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena5:
                    imagebutton auto "extra/replay_pri5_%s.jpg" action Replay("priscila_e3_finalamizade")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena6:
                    imagebutton auto "extra/replay_pri6_%s.jpg" action Replay("priscila_e3_finalbeijo")

                else:
                    add "extra/replay.jpg"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if persistent.priscila_cena7:
                    imagebutton auto "extra/replay_pri7_%s.jpg" action Replay("priscila_e3_sexo")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena8:
                    imagebutton auto "extra/replay_pri8_%s.jpg" action Replay("priscila_e4_amizade")

                else:
                    add "extra/replay.jpg"

                if persistent.priscila_cena9:
                    imagebutton auto "extra/replay_pri9_%s.jpg" action Replay("priscila_e4_namoro")

                else:
                    add "extra/replay.jpg"



        hbox:

            spacing 10
            xalign 0.5

            textbutton _("Página 1") action ShowMenu("memorias_priscila"):
                xalign 0.5

            text "|" xalign 0.5

            textbutton _("Página 2") action ShowMenu("memorias_priscila2") xalign 0.5

screen menu_replay():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 50
        xalign 0.5

        vbox:

            spacing 10
            xalign 0.5

            text "{b}Memórias{/b}" xalign 0.5
            text "Reveja cenas marcantes da sua história atual" size 15 xalign 0.5
            text "Encontre novos personagens e faça escolhas diferentes para liberar momentos únicos e especiais" size 15 xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 20

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if priscila_e1 != "nada":

                    imagebutton auto "extra/celular_botao_priscila_%s.png" action ShowMenu("memorias_priscila")

                else:

                    add "extra/fantasma.png"

                if not sayuri_evento1_check:

                    imagebutton auto "extra/celular_botao_sayuri_%s.png" action ShowMenu("memorias_sayuri")

                else:

                    add "extra/fantasma.png"

                if v2_fim:

                    imagebutton auto "extra/celular_botao_cassia_%s.png" action ShowMenu("memorias_cassia")

                else:

                    add "extra/fantasma.png"

                if nathan_e1 != "nada":

                    imagebutton auto "extra/celular_botao_nathan_%s.png" action ShowMenu("memorias_nathan")

                else:

                    add "extra/fantasma.png"

                if sayuri_e2 != "nada":

                    imagebutton auto "extra/celular_botao_julia_%s.png" action ShowMenu("memorias_julia")

                else:

                    add "extra/fantasma.png"

                if diana_e1 != "nada":

                    imagebutton auto "extra/celular_botao_diana_%s.png" action ShowMenu("memorias_diana")

                else:

                    add "extra/fantasma.png"

                if sofia_e1 != "nada":

                    imagebutton auto "extra/botao_sofia_%s.png" action ShowMenu("memorias_sofia")

                else:

                    add "extra/fantasma.png"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if natasha_e1 != "nada":

                    imagebutton auto "extra/botao_natasha_%s.png" action ShowMenu("memorias_natasha")

                else:

                    add "extra/fantasma.png"

                if mc_massagem > 0:

                    imagebutton auto "extra/botao_karli_%s.png" action ShowMenu("memorias_karli")

                else:

                    add "extra/fantasma.png"

                if thaynara_evento > 0:

                    imagebutton auto "extra/botao_thaynara_%s.png" action ShowMenu("memorias_thaynara")

                else:

                    add "extra/fantasma.png"

                if stifler_e1 != "nada":

                    imagebutton auto "extra/botao_distrito_%s.png" action ShowMenu("memorias_distrito")

                else:

                    add "extra/fantasma.png"

                if maria_evento > 0:

                    imagebutton auto "extra/botao_maria_%s.png" action ShowMenu("memorias_maria")

                else:

                    add "extra/fantasma.png"

                if quincy_e1:

                    imagebutton auto "extra/botao_selena_%s.png" action ShowMenu("memorias_selena")

                else:

                    add "extra/fantasma.png"

                if banho_evento > 0:

                    imagebutton auto "extra/botao_china_%s.png" action ShowMenu("memorias_china")

                else:

                    add "extra/fantasma.png"

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if quincy_evento > 0:

                    imagebutton auto "extra/botao_jones_%s.png" action ShowMenu("memorias_jones")

                else:

                    add "extra/fantasma.png"

                if fado_pixel_comeu:

                    imagebutton auto "extra/botao_fadolandia_%s.png" action ShowMenu("memorias_fadolandia")

                else:

                    add "extra/fantasma.png"

                if ana_evento > 0:

                    imagebutton auto "extra/botao_ana_%s.png" action ShowMenu("memorias_ana")

                else:

                    add "extra/fantasma.png"

                if tkf_evento1:

                    imagebutton auto "extra/botao_tkf_%s.png" action ShowMenu("memorias_tkf")

                else:

                    add "extra/fantasma.png"

                add "extra/fantasma.png"

screen memorias_sayuri():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        vbox:

            spacing 10
            xalign 0.5

            add "extra/celular_botao_sayuri_idle.png" xalign 0.5

            text "{b}Sayuri - A Atleta Chinesa{/b}" xalign 0.5
            text "Faça escolhas diferentes na sua história com ela para viver todos os finais" size 15 xalign 0.5

        text "Se você excluir o jogo, os dados desta página serão perdidos" size 15 xalign 0.5 yalign 1.0

        hbox:

            xalign 0.5
            yalign 0.6
            spacing 20

            vbox:

                spacing 5

                if persistent.sayuri_final1 or sayuri_final1:

                    add sayuri_final1_img

                    text "{b}Final 1{/b}" xalign 0.5

                    text "Imortal" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 1{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.sayuri_final2 or sayuri_final2:

                    add sayuri_final2_img

                    text "{b}Final 2{/b}" xalign 0.5

                    text "Fim da Dinastia" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 2{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.sayuri_final3 or sayuri_final3:

                    add sayuri_final3_img

                    text "{b}Final 3{/b}" xalign 0.5

                    text "Resistência Milenar" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 3{/b}" xalign 0.5

                    text "???" xalign 0.5
































screen memorias_cassia():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/celular_botao_cassia_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_nathan():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        vbox:

            spacing 10
            xalign 0.5

            add "extra/celular_botao_nathan_idle.png" xalign 0.5

            text "{b}Nathan - O Modelo Estrangeiro{/b}" xalign 0.5
            text "Faça escolhas diferentes na sua história com ele para viver todos os finais" size 15 xalign 0.5

        text "Se você excluir o jogo, os dados desta página serão perdidos" size 15 xalign 0.5 yalign 1.0

        hbox:

            xalign 0.5
            yalign 0.6
            spacing 20

            vbox:

                spacing 5

                if persistent.nathan_final1 or nathan_final1:

                    add nathan_final1_img

                    text "{b}Final 1{/b}" xalign 0.5

                    text "Finalmente Livre" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 1{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.nathan_final2 or nathan_final2:

                    add nathan_final2_img

                    text "{b}Final 2{/b}" xalign 0.5

                    text "Agente Internacional" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 2{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.nathan_final3 or nathan_final3:

                    add nathan_final3_img

                    text "{b}Final 3{/b}" xalign 0.5

                    text "Subindo ao Topo" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 3{/b}" xalign 0.5

                    text "???" xalign 0.5

screen memorias_julia():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        vbox:

            spacing 10
            xalign 0.5

            add "extra/celular_botao_julia_idle.png" xalign 0.5

            text "{b}Júlia - A Universitária Fogosa{/b}" xalign 0.5
            text "Faça escolhas diferentes na sua história com ela para viver todos os finais" size 15 xalign 0.5

        text "Se você excluir o jogo, os dados desta página serão perdidos" size 15 xalign 0.5 yalign 1.0

        hbox:

            xalign 0.5
            yalign 0.6
            spacing 20

            vbox:

                spacing 5

                if persistent.julia_final1 or julia_final1:

                    add julia_final1_img

                    text "{b}Final 1{/b}" xalign 0.5

                    text "Bentinho" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 1{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.julia_final2 or julia_final2:

                    add julia_final2_img

                    text "{b}Final 2{/b}" xalign 0.5

                    text "A Única Saída" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 2{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.julia_final3 or julia_final3:

                    add julia_final3_img

                    text "{b}Final 3{/b}" xalign 0.5

                    text "Essa É Ela" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 3{/b}" xalign 0.5

                    text "???" xalign 0.5

screen memorias_diana():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        vbox:

            spacing 10
            xalign 0.5

            add "extra/celular_botao_diana_idle.png" xalign 0.5

            text "{b}Diana - A Cantora do Cassino{/b}" xalign 0.5
            text "Faça escolhas diferentes na sua história com ela para viver todos os finais" size 15 xalign 0.5

        text "Se você excluir o jogo, os dados desta página serão perdidos" size 15 xalign 0.5 yalign 1.0

        hbox:

            xalign 0.5
            yalign 0.6
            spacing 20

            vbox:

                spacing 5

                if persistent.diana_final1 or diana_final1:

                    add diana_final1_img

                    text "{b}Final 1{/b}" xalign 0.5

                    text "Liberdade?" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 1{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.diana_final2 or diana_final2:

                    add diana_final2_img

                    text "{b}Final 2{/b}" xalign 0.5

                    text "Consequências" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 2{/b}" xalign 0.5

                    text "???" xalign 0.5

            vbox:

                spacing 5

                if persistent.diana_final3 or diana_final3:

                    add diana_final3_img

                    text "{b}Final 3{/b}" xalign 0.5

                    text "Sou Um Deles" xalign 0.5

                else:

                    add "extra/replay.jpg"

                    text "{b}Final 3{/b}" xalign 0.5

                    text "???" xalign 0.5

screen memorias_sofia():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_sofia_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_natasha():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_natasha_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_karli():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_karli_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_thaynara():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_thaynara_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_distrito():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_distrito_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_maria():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_maria_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_selena():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_selena_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_china():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_china_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_jones():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_jones_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

                if quincy_evento > 0:
                    imagebutton:
                        idle "quincy cassino_falando.jpg"
                        action [ SetVariable("memoria_img", "quincy cassino_falando.jpg"), SetVariable("memoria_menu", "memorias_jones"), ShowMenu("memorias_imagem") ]
                        at zoomM

                else:
                    add "extra/replay.jpg"

screen memorias_fadolandia():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_fadolandia_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_ana():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_ana_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_tkf():
    tag menu_aba

    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 30
        xalign 0.5

        add "extra/botao_tkf_idle.png" xalign 0.5

        vbox:

            xalign 0.5
            yalign 0.5
            spacing 10

            hbox:

                xalign 0.5
                yalign 0.5
                spacing 10

            text "{b}Memórias Indisponíveis{/b}" xalign 0.5

            text "As memórias deste personagem serão disponibilizadas em uma atualização futura" size 15 xalign 0.5 yalign 0.5

screen memorias_imagem():
    tag menu_aba

    zorder 99
    modal True

    imagebutton:
        idle "[memoria_img]"
        action ShowMenu(memoria_menu)

screen menu_salvar():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Salvar / Carregar{/b}" xalign 0.5
        text "Use os slots de salvamento abaixo para tentar vários caminhos diferentes!" size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            text "{b}Salvar Jogo{/b}" xalign 0.5

            text "Aperte um dos slots para salvar seu jogo" size 15 xalign 0.5

            grid 3 1:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(3 * 1):

                    $ slot = i + 1
                    $ numero_jogo = i + 1

                    button:
                        action FileSave(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text "Jogo [numero_jogo]":
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            text "{b}Carregar Jogo{/b}" xalign 0.5

            text "Aperte um dos slots para carregar seu jogo" size 15 xalign 0.5

            grid 3 1:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for o in range(3 * 1):

                    $ slot1 = o + 1
                    $ numero_jogo2 = o + 1

                    button:
                        action FileLoad(slot1)

                        has vbox

                        add FileScreenshot(slot1) xalign 0.5

                        text FileTime(slot1, format=_("{#file_time} %d/%m/%y, %H:%M"), empty=_("espaço vazio")):
                            style "slot_time_text"

                        text "Jogo [numero_jogo2]":
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:

                spacing 10
                xalign 0.5

                textbutton _("Página 1") action ShowMenu("menu_salvar"):
                    xalign 0.5

                text "|" xalign 0.5

                textbutton _("Página 2") action ShowMenu("menu_salvar2") xalign 0.5

screen menu_salvar2():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Salvar / Carregar - Página 2{/b}" xalign 0.5
        text "Use os slots de salvamento abaixo para tentar vários caminhos diferentes!" size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            text "{b}Salvar Jogo{/b}" xalign 0.5

            text "Aperte um dos slots para salvar seu jogo" size 15 xalign 0.5

            grid 3 1:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(3 * 1):

                    $ slot = i + 4
                    $ numero_jogo = i + 4

                    button:
                        action FileSave(slot, confirm=False)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text "Jogo [numero_jogo]":
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            text "{b}Carregar Jogo{/b}" xalign 0.5

            text "Aperte um dos slots para carregar seu jogo" size 15 xalign 0.5

            grid 3 1:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for o in range(3 * 1):

                    $ slot1 = o + 4
                    $ numero_jogo2 = o + 4

                    button:
                        action FileLoad(slot1, confirm=False)

                        has vbox

                        add FileScreenshot(slot1) xalign 0.5

                        text FileTime(slot1, format=_("{#file_time} %d/%m/%y, %H:%M"), empty=_("espaço vazio")):
                            style "slot_time_text"

                        text "Jogo [numero_jogo2]":
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            hbox:

                spacing 10
                xalign 0.5

                textbutton _("Página 1") action ShowMenu("menu_salvar"):
                    xalign 0.5

                text "|" xalign 0.5

                textbutton _("Página 2") action ShowMenu("menu_salvar2") xalign 0.5

screen menu_load():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Relembrar Encontros{/b}" xalign 0.5
        text "Reviva encontros para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 10
                xalign 0.5

                if renpy.can_load("p1_save"):

                    button:
                        action FileLoad("p1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p1_save.jpg"

                        text "Priscila - Primeiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("p2_save"):

                    button:
                        action FileLoad("p2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p2_save.jpg"

                        text "Priscila - Segundo Encontro":
                            style "slot_time_text"

                if renpy.can_load("n1_save"):

                    button:
                        action FileLoad("n1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n1_save.jpg"

                        text "Nathan - Primeiro Encontro":
                            style "slot_time_text"

            hbox:

                spacing 10
                xalign 0.5

                if renpy.can_load("p3_save"):

                    button:
                        action FileLoad("p3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p3_save.jpg"

                        text "Priscila - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("s1_save"):

                    button:
                        action FileLoad("s1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s1_save.jpg"

                        text "Sayuri - Primeiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("s2_save"):

                    button:
                        action FileLoad("s2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s2_save.jpg"

                        text "Sayuri - Segundo Encontro":
                            style "slot_time_text"

            hbox:

                spacing 10
                xalign 0.5

                if renpy.can_load("j1_save"):

                    button:
                        action FileLoad("j1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j1_save.jpg"

                        text "Júlia - Primeiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("m1_save"):

                    button:
                        action FileLoad("m1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/m1_save.jpg"

                        text "Karli - Aula Atual":
                            style "slot_time_text"

                if renpy.can_load("s3_save"):

                    button:
                        action FileLoad("s3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s3_save.jpg"

                        text "Sayuri - Terceiro Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load2():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Relembrar Encontros - Página 2{/b}" xalign 0.5
        text "Reviva encontros para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("j2_save"):

                    button:
                        action FileLoad("j2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j2_save.jpg"

                        text "Júlia - Segundo Encontro":
                            style "slot_time_text"

                if renpy.can_load("c1_save"):

                    button:
                        action FileLoad("c1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/c1_save.jpg"

                        text "Nathan (Cássia) - Segundo Encontro":
                            style "slot_time_text"

                if renpy.can_load("p4_save"):

                    button:
                        action FileLoad("p4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p4_save.jpg"

                        text "Priscila - Quarto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("s4_save"):

                    button:
                        action FileLoad("s4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s4_save.jpg"

                        text "Sayuri - Quarto Encontro":
                            style "slot_time_text"

                if renpy.can_load("j3_save"):

                    button:
                        action FileLoad("j3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j3_save.jpg"

                        text "Júlia - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("us1_save"):

                    button:
                        action FileLoad("us1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/us1_save.jpg"

                        text "Black Cash - Primeiro Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("d1_save"):

                    button:
                        action FileLoad("d1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d1_save.jpg"

                        text "Diana - Primeiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("us2_save"):

                    button:
                        action FileLoad("us2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/us2_save.jpg"

                        text "Black Cash - Segundo Encontro":
                            style "slot_time_text"

                if renpy.can_load("d2_save"):

                    button:
                        action FileLoad("d2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d2_save.jpg"

                        text "Diana - Segundo Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load3():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Relembrar Encontros - Página 3{/b}" xalign 0.5
        text "Reviva encontros para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("n3_save"):

                    button:
                        action FileLoad("n3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n3_save.jpg"

                        text "Nathan (Cássia) - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("p5_save"):

                    button:
                        action FileLoad("p5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p5_save.jpg"

                        text "Priscila - Quinto Encontro":
                            style "slot_time_text"

                if renpy.can_load("s5_save"):

                    button:
                        action FileLoad("s5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s5_save.jpg"

                        text "Sayuri - Quinto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("j4_save"):

                    button:
                        action FileLoad("j4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j4_save.jpg"

                        text "Júlia - Quarto Encontro":
                            style "slot_time_text"

                if renpy.can_load("d3_save"):

                    button:
                        action FileLoad("d3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d3_save.jpg"

                        text "Diana - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("n4_save"):

                    button:
                        action FileLoad("n4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n4_save.jpg"

                        text "Nathan - Quarto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("na1_save"):

                    button:
                        action FileLoad("na1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/na1_save.jpg"

                        text "Natasha - Primeiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("p6_save"):

                    button:
                        action FileLoad("p6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p6_save.jpg"

                        text "Priscila - Sexto Encontro":
                            style "slot_time_text"

                if renpy.can_load("s6_save"):

                    button:
                        action FileLoad("s6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s6_save.jpg"

                        text "Sayuri - Sexto Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load4():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Checkpoint Encontros - Página 4{/b}" xalign 0.5
        text "Volte em momentos marcantes para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("j5_save"):

                    button:
                        action FileLoad("j5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j5_save.jpg"

                        text "Júlia - Quinto Encontro":
                            style "slot_time_text"

                if renpy.can_load("d4_save"):

                    button:
                        action FileLoad("d4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d4_save.jpg"

                        text "Diana - Quarto Encontro":
                            style "slot_time_text"

                if renpy.can_load("n5_save"):

                    button:
                        action FileLoad("n5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n5_save.jpg"

                        text "Nathan - Quinto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("so3_save"):

                    button:
                        action FileLoad("so3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/so3_save.jpg"

                        text "Sofia - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("na2_save"):

                    button:
                        action FileLoad("na2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/na2_save.jpg"

                        text "Natasha - Segundo Encontro":
                            style "slot_time_text"

                if renpy.can_load("h1_save"):

                    button:
                        action FileLoad("h1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/h1_save.jpg"

                        text "[h_nome] - Primeiro Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("pex1_save"):

                    button:
                        action FileLoad("pex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/pex1_save.jpg"

                        text "Priscila - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("p7_save"):

                    button:
                        action FileLoad("p7_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p7_save.jpg"

                        text "Priscila - Sétimo Encontro":
                            style "slot_time_text"

                if renpy.can_load("s7_save"):

                    button:
                        action FileLoad("s7_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s7_save.jpg"

                        text "Sayuri - Sétimo Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load5():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Checkpoint Encontros - Página 5{/b}" xalign 0.5
        text "Volte em momentos marcantes para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("j6_save"):

                    button:
                        action FileLoad("j6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j6_save.jpg"

                        text "Júlia - Sexto Encontro":
                            style "slot_time_text"

                if renpy.can_load("sex1_save"):

                    button:
                        action FileLoad("sex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/sex1_save.jpg"

                        text "Sayuri - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("d5_save"):

                    button:
                        action FileLoad("d5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d5_save.jpg"

                        text "Diana - Quinto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("n6_save"):

                    button:
                        action FileLoad("n6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n6_save.jpg"

                        text "Nathan (Cássia) - Sexto Encontro":
                            style "slot_time_text"

                if renpy.can_load("jex1_save"):

                    button:
                        action FileLoad("jex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/jex1_save.jpg"

                        text "Júlia - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("so4_save"):

                    button:
                        action FileLoad("so4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/so4_save.jpg"

                        text "Sofia - Quarto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("dex1_save"):

                    button:
                        action FileLoad("dex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/dex1_save.jpg"

                        text "Diana - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("na3_save"):

                    button:
                        action FileLoad("na3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/na3_save.jpg"

                        text "Natasha - Terceiro Encontro":
                            style "slot_time_text"

                if renpy.can_load("h2_save"):

                    button:
                        action FileLoad("h2_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/h2_save.jpg"

                        text "[h_nome] - Segundo Encontro":
                            style "slot_time_text"


            use eventos_paginacao

screen menu_load6():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Checkpoint Encontros - Página 6{/b}" xalign 0.5
        text "Volte em momentos marcantes para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("y1_save"):

                    button:
                        action FileLoad("y1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/y1_save.jpg"

                        text "Naru - Encontro":
                            style "slot_time_text"

                if renpy.can_load("nex1_save"):

                    button:
                        action FileLoad("nex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/nex1_save.jpg"

                        text "Nathan - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("p8_save"):

                    button:
                        action FileLoad("p8_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p8_save.jpg"

                        text "Priscila - Oitavo Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("s8_save"):

                    button:
                        action FileLoad("s8_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s8_save.jpg"

                        text "Sayuri - Oitavo Encontro":
                            style "slot_time_text"

                if renpy.can_load("j7_save"):

                    button:
                        action FileLoad("j7_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j7_save.jpg"

                        text "Júlia - Sétimo Encontro":
                            style "slot_time_text"

                if renpy.can_load("d6_save"):

                    button:
                        action FileLoad("d6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/d6_save.jpg"

                        text "Diana - Sexto Encontro":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("soex1_save"):

                    button:
                        action FileLoad("soex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/soex1_save.jpg"

                        text "Sofia - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("n7_save"):

                    button:
                        action FileLoad("n7_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/n7_save.webp"

                        text "Nathan - Sétimo Encontro":
                            style "slot_time_text"

                if renpy.can_load("so5_save"):

                    button:
                        action FileLoad("so5_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/so5_save.webp"

                        text "Sofia - Quinto Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load7():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Checkpoint Encontros - Página 7{/b}" xalign 0.5
        text "Volte em momentos marcantes para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("na4_save"):

                    button:
                        action FileLoad("na4_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/na4_save.jpg"

                        text "Natasha - Quarto Encontro":
                            style "slot_time_text"

                if renpy.can_load("naex1_save"):

                    button:
                        action FileLoad("naex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/naex1_save.jpg"

                        text "Natasha - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("h3_save"):

                    button:
                        action FileLoad("h3_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/h3_save.webp"

                        text "Nona - Encontro 3":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("hex1_save"):

                    button:
                        action FileLoad("hex1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/hex1_save.webp"

                        text "Nona - Encontro Extra 1":
                            style "slot_time_text"

                if renpy.can_load("p9_save"):

                    button:
                        action FileLoad("p9_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/p9_save.webp"

                        text "Priscila - Encontro 9":
                            style "slot_time_text"

                if renpy.can_load("ma1_save"):

                    button:
                        action FileLoad("ma1_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/ma1_save.jpg"

                        text "Maria - Corrida":
                            style "slot_time_text"

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("s9_save"):

                    button:
                        action FileLoad("s9_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/s9_save.webp"

                        text "Sayuri - Nono Encontro":
                            style "slot_time_text"

                if renpy.can_load("j8_save"):

                    button:
                        action FileLoad("j8_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add "extra/j8_save.webp"

                        text "Júlia - Oitavo Encontro":
                            style "slot_time_text"

                if renpy.can_load("d7_save"):

                    button:
                        action FileLoad("d7_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add diana_encontro7_img

                        text "Diana - Sétimo Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen menu_load8():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has vbox

        spacing 10
        xalign 0.5

        text "{b}Checkpoint Encontros - Página 8{/b}" xalign 0.5
        text "Volte em momentos marcantes para tentar novas escolhas. Estes saves {b}não{/b} estão salvos na nuvem." size 15 xalign 0.5

        viewport id "encontros_load":
            xsize 820
            scrollbars None
            draggable True
            mousewheel True
            yinitial 1.0

            has vbox

            spacing 10
            xalign 0.5

            hbox:

                spacing 5
                xalign 0.5

                if renpy.can_load("n8_save"):

                    button:
                        action FileLoad("n8_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add nathan_encontro8_img

                        text "Nathan - Oitavo Encontro":
                            style "slot_time_text"

                if renpy.can_load("so6_save"):

                    button:
                        action FileLoad("so6_save", confirm=False, page="None", newest=False, slot=True)

                        has vbox

                        add sofia_encontro6_img

                        text "Sofia - Sexto Encontro":
                            style "slot_time_text"

            use eventos_paginacao

screen eventos_paginacao():

    hbox:

        spacing 10
        xalign 0.5

        textbutton _("P1") action ShowMenu("menu_load"):
            xalign 0.5

        text "|" xalign 0.5

        textbutton _("P2") action ShowMenu("menu_load2") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P3") action ShowMenu("menu_load3") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P4") action ShowMenu("menu_load4") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P5") action ShowMenu("menu_load5") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P6") action ShowMenu("menu_load6") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P7") action ShowMenu("menu_load7") xalign 0.5

        text "|" xalign 0.5

        textbutton _("P8") action ShowMenu("menu_load8") xalign 0.5

screen menu_loja():
    tag menu_aba

    predict False
    zorder 99
    modal True

    add "extra/menu_back.jpg" at menu_back

    use menu_sidebar

    frame style "menu_conteudo":

        has frame

        background None
        xpadding 30

        if userlogado and uid != "NOID":

            hbox:

                spacing 20

                vbox:

                    xsize 450
                    spacing 30

                    vbox:

                        spacing 5

                        hbox:

                            spacing 5

                            add "extra/coin_25.png"
                            text "{b}10.000 Celebrity Coins{/b}"

                        text "{b}Preço: R$ 9,90{/b}" size 15
                        text "Acelere seu progresso e complete o álbum de cartas" size 15
                        imagebutton auto "extra/botao_comprar_%s.png" action OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/e48c202266f44868b8ca')

                    vbox:

                        spacing 5

                        hbox:

                            spacing 5

                            add "extra/money.png"
                            text "{b}250 Celebrity Reais{/b}"

                        text "{b}Preço: 4,90{/b}" size 15
                        text "O valor exato para comprar roupas e melhorar o estilo" size 15
                        imagebutton auto "extra/botao_comprar_%s.png" action OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/6162f34edb7f4db7b58d')

                vbox:

                    spacing 30

                    vbox:

                        spacing 5

                        hbox:

                            spacing 5

                            add "extra/money.png"
                            text "{b}1.000 Celebrity Reais{/b}"

                        text "{b}Preço: R$ 17,90{/b}" size 15
                        text "Finalmente chegou a hora de curtir a vida adoidado" size 15
                        imagebutton auto "extra/botao_comprar_%s.png" action OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/20d774d587a142c78b9a')

                    vbox:

                        spacing 5

                        hbox:

                            spacing 5

                            add "extra/money.png"
                            text "{b}2.000 Celebrity Reais{/b}"

                        text "{b}Preço: R$ 29,90{/b}" size 15
                        text "É sua vez de ficar rico e conquistar o mundo!" size 15
                        imagebutton auto "extra/botao_comprar_%s.png" action OpenURL('https://play.geiko.net/comprar/celebrity-hunter/' + uid + '/1060ff0d8ff64c818c35')

            vbox:

                spacing 30


                yalign 0.49
                yanchor 0.0






                text "Compre com Cartão ou Pix com segurança e privacidade e receba os créditos {b}imediatamente{/b}":
                    size 17
                    xanchor 0.5
                    xalign 0.5

                text "{b}Saldo Atual{/b}":
                    xalign 0.5

                hbox:

                    xalign 0.5

                    spacing 20

                    hbox:

                        spacing 5

                        add "extra/coin_25.png"
                        text "{b}[persistent.coins]{/b}"

                    hbox:

                        spacing 5

                        add "extra/money.png"
                        text "{b}[cash]{/b}"

                text "Após a confirmação do pagamento, use o botão abaixo para receber seus créditos {b}automaticamente{/b}" size 17 xalign 0.5 xanchor 0.5

                imagebutton auto "extra/botao_atualizar_%s.webp" action Call("carrega_compra") xalign 0.5

            text "Algum problema com compras? Entre em contato pelo nosso {a=https://www.geiko.net/suporte/}{b}Suporte{/b}{/a}.":
                size 17
                yalign 1.0
                yanchor 0.0
                xanchor 0.5
                xalign 0.5

        else:

            vbox:

                spacing 5

                text "Para fazer compras você deve estar logado em sua conta. Assim elas ficam protegidas na nuvem." size 15 xalign 0.5 xanchor 0.5

                text ""

                imagebutton auto "extra/botao_login_%s.png" xalign 0.5 xanchor 0.5 action Jump("fazer_login_menu")

screen salvar():
    tag menu


    default page_name_value = FilePageNameInputValue(pattern=_("Salvar: Página {}"), auto=_("Saves Automáticos"), quick=_("Saves Rápidos"))

    fixed:

        order_reverse True

        vbox:

            spacing 20
            xalign 0.5

            input:
                style "page_label_text"
                value page_name_value
                xanchor 0.5
                xalign 0.5

            text "Aperte no espaço em que quer salvar seu progreesso" xanchor 0.5 xalign 0.5

            if premium:

                textbutton _("Salvar todos na Nuvem"):
                    action ShowMenu("salvar_nuvem")
                    xanchor 0.5
                    xalign 0.5
                    style "config_button"

            else:

                text "Estes saves são salvos na nuvem apenas na versão Premium" xanchor 0.5 xalign 0.5 size 14


        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileSave(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%d/%m/%Y, %H:%M"), empty=_("aperte para salvar")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        vbox:

            spacing 20
            xalign 0.5
            xanchor 0.5
            yalign 0.95

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing










                for page in range(1, 10):
                    textbutton "[page]":
                        action FilePage(page)
                        style "config_button"



            textbutton "Voltar ao Jogo >>":
                xalign 0.5
                xanchor 0.5
                action Return()
                style "config_button"

screen carregar():
    tag menu


    default page_name_value = FilePageNameInputValue(pattern=_("Carregar: Página {}"), auto=_("Saves Automáticos"), quick=_("Saves Rápidos"))

    fixed:

        order_reverse True

        vbox:

            spacing 20
            xalign 0.5

            input:
                style "page_label_text"
                value page_name_value
                xanchor 0.5
                xalign 0.5

            text "Aperte no progresso que quer carregar" xanchor 0.5 xalign 0.5

            if not premium:

                text "Estes saves não estão salvos na nuvem" xanchor 0.5 xalign 0.5 size 14

            textbutton _("Carregar progresso antigo"):
                action [ FileLoad("continue", confirm=False, page="None", newest=True, slot=False) ]
                xanchor 0.5
                xalign 0.5
                style "config_button"













        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.5

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileLoad(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{#file_time}%d/%m/%Y, %H:%M"), empty=_("nenhum save aqui")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)

        vbox:

            spacing 20
            xalign 0.5
            xanchor 0.5
            yalign 0.95

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing










                for page in range(1, 10):
                    textbutton "[page]":
                        action FilePage(page)
                        style "config_button"



            textbutton "Voltar ao Jogo >>":
                xalign 0.5
                xanchor 0.5
                action Return()
                style "config_button"



style config_button:
    idle_background Frame(Solid(config_verde_claro), 5, 5)
    hover_background Frame(Solid(config_verde_escuro), 5, 5)
    selected_background Frame(Solid(config_verde_claro), 5, 5)
    padding (20, 10)
    xminimum 50

style config_button_text:
    idle_color config_branco
    hover_color config_branco
    selected_color config_preto
    size 18
    xalign 0.5
    outlines [(1, config_preto, 0, 0)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
