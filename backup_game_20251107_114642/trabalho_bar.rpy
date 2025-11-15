label trabalho_inicio:

    call checa_logado from _call_checa_logado_6

    "Hora de ganhar uma grana."

    call anuncio from _call_anuncio_7

    "..."

    $ proibido_salvar = True
    $ show_quick_menu = False

    call checa_tempo from _call_checa_tempo_8

    $ renpy.choice_for_skipping()

    python:
        if renpy.android:
            tbtempo = PythonSDLActivity.checkTBtempoNext()

    "..."

    "Opa! Tô vendo o [gar]."

    $ renpy.choice_for_skipping()

    if not tbtempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        mc concentrando "Pensando bem, nem tô afim agora. Faz pouco tempo que eu trabalhei e tô de boa."

        "Outra hora eu volto pra ganhar mais uma graninha."

        scene black with Dissolve(1.0)

        p rindo "O [mc] pode trabalhar uma vez a cada {b}3 horas do mundo real{/b}."

        p rindo "Vá com calma que você vai conseguir juntar aquela fortuna!"

        p "Use o app Relógio no celular do [mc] para ver quando o próximo turno de trabalho estará disponível."

        p "E não se esqueça que é possível usar dinheiro do seu mundo para deixar o [mc] rico."

        p "Até!"

        jump call_cidade

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("trabalho_bar","fabricio","personagem")

    python:
        if renpy.android:
            PythonSDLActivity.setTBtempoNext()

    if tempo == 1:

        mc normal "Bom dia, [gar]."

        show garcom chamando with dissolve

        gar "Bom dia, senhor [mc]. Ainda não estamos abertos. Se você está aqui a essa hora, veio para me ajudar, estou correto?"

        mc "É isso aí."

        gar "Perfeito. Ontem tivemos uma festa especial durante a madrugada e deixaram uma bagunça lá atrás."

        gar "Você por ventura poderia me auxiliar a deixar tudo em ordem?"

        mc "Com certeza."

    elif tempo == 3:

        "Ainda tem cliente. Vou esperar até todos saírem."

        "..."

        "Pronto. Só ficou o [gar]."

        mc normal "Boa noite, [gar]."

        show garcom diabolico with dissolve

        gar "Que honra recebê-lo neste humilde antro de banais prazeres. Você sabe que já estamos fechados. Veio para me auxiliar, correto?"

        mc "Sim. Tô precisando da grana."

        gar "Seu auxílio vem em hora deveras propícia, senhor [mc]."

        gar "Preciso deixar o bar em ordem para uma festa especial que teremos nesta madrugada."

        mc "Pode deixar comigo."

    gar "Serei eternamente grato."

    mc "Tô indo lá começar. Até daqui a pouco."

    jump trabalho_bar_itens

label trabalho_bar_itens:

    $ tb_items = 0
    $ bar_item_1 = False
    $ bar_item_2 = False
    $ bar_item_3 = False
    $ bar_item_4 = False
    $ bar_item_5 = False
    $ bar_item_6 = False
    $ bar_item_7 = False
    $ bar_item_8 = False
    $ bar_item_9 = False
    $ bar_item_10 = False

    $ rand_n_item = renpy.random.randint(1,3)

    if rand_n_item == 1:

        $ rand_item_max = 5

    elif rand_n_item == 2:

        $ rand_item_max = 4

    elif rand_n_item == 3:

        $ rand_item_max = 3

    label tb_escolhe:

        $ rand_item = renpy.random.randint(1,10)

        if rand_item == 1:

            if not bar_item_1:

                $ bar_item_1 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 2:

            if not bar_item_2:

                $ bar_item_2 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 3:

            if not bar_item_3:

                $ bar_item_3 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 4:

            if not bar_item_4:

                $ bar_item_4 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 5:

            if not bar_item_5:

                $ bar_item_5 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 6:

            if not bar_item_6:

                $ bar_item_6 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 7:

            if not bar_item_7:

                $ bar_item_7 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 8:

            if not bar_item_8:

                $ bar_item_8 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 9:

            if not bar_item_9:

                $ bar_item_9 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if rand_item == 10:

            if not bar_item_10:

                $ bar_item_10 = True
                $ tb_items += 1
            else:


                jump tb_escolhe

        if tb_items == rand_item_max:

            jump trabalho_bar_tela
        else:


            jump tb_escolhe

label trabalho_bar_tela:



    show screen tb_angulo_2

    scene pub fundao with dissolve

    $ renpy.pause()

    "..."



screen tb_angulo_2():
    tag trab_bar

    zorder 100
    modal True

    add "images/bar/bar_angulo2.jpg" at cidade_trans

    imagebutton auto "extra/botao_desistir_%s.png":
        xalign 0.05
        yalign 0.95
        at cidade_trans
        action Call("trabalho_bar_desistiu")

    if bar_item_1:

        imagebutton auto "images/bar/item1_%s.png":
            xalign 0.05
            yalign 0.52
            at cidade_trans
            action [ SetVariable("bar_item_1", False), Call("tb_item_pegou") ]

    if bar_item_2:

        imagebutton auto "images/bar/item2_%s.png":
            xalign 0.3
            yalign 0.8
            at cidade_trans
            action [ SetVariable("bar_item_2", False), Call("tb_item_pegou") ]

    if bar_item_3:

        imagebutton auto "images/bar/item3_%s.png":
            xalign 0.24
            yalign 0.25
            at cidade_trans
            action [ SetVariable("bar_item_3", False), Call("tb_item_pegou") ]

    if bar_item_4:

        imagebutton auto "images/bar/item4_%s.png":
            xalign 0.95
            yalign 0.54
            at cidade_trans
            action [ SetVariable("bar_item_4", False), Call("tb_item_pegou") ]

    if bar_item_5:

        imagebutton auto "images/bar/item5_%s.png":
            xalign 0.15
            yalign 0.56
            at cidade_trans
            action [ SetVariable("bar_item_5", False), Call("tb_item_pegou") ]

    if bar_item_6:

        imagebutton auto "images/bar/item6_%s.png":
            xalign 0.5
            yalign 0.59
            at cidade_trans
            action [ SetVariable("bar_item_6", False), Call("tb_item_pegou") ]

    if bar_item_7:

        imagebutton auto "images/bar/item5_%s.png":
            xalign 0.4
            yalign 0.5
            at cidade_trans
            action [ SetVariable("bar_item_7", False), Call("tb_item_pegou") ]

    if bar_item_8:

        imagebutton auto "images/bar/item3_%s.png":
            xalign 0.6
            yalign 0.9
            at cidade_trans
            action [ SetVariable("bar_item_8", False), Call("tb_item_pegou") ]

    if bar_item_9:

        imagebutton auto "images/bar/item4_%s.png":
            xalign 0.41
            yalign 0.555
            at cidade_trans
            action [ SetVariable("bar_item_9", False), Call("tb_item_pegou") ]

    if bar_item_10:

        imagebutton auto "images/bar/item1_%s.png":
            xalign 0.85
            yalign 0.474
            at cidade_trans
            action [ SetVariable("bar_item_10", False), Call("tb_item_pegou") ]

label tb_item_pegou:

    $ tb_items -= 1

    if tb_items == 4:

        $ renpy.notify("Você lavou e colocou o objeto no lugar, faltam mais 4 itens")

    if tb_items == 3:

        $ renpy.notify("Você lavou e colocou o objeto no lugar, faltam mais 3 itens")

    if tb_items == 2:

        $ renpy.notify("Você lavou e colocou o objeto no lugar, faltam mais 2 itens")

    if tb_items == 1:

        $ renpy.notify("Você lavou e colocou o objeto no lugar, falta apenas 1 item agora")

    if tb_items <= 0:

        hide screen tb_angulo_2

        scene pub fundao with dissolve

        mc concentrando "Ufa... Acho que limpei tudo por hoje."

        mc normal "Deixa eu avisar o [gar]."

        jump trabalho_bar_finalizar

    "..."

label trabalho_bar_desistiu:

    scene pub fundao with dissolve

    hide screen tb_angulo_2

    mc desculpa "Será que eu devo encerrar o turno sem ter arrumado tudo?"

    menu:
        "Sim. Encerrar turno":


            jump trabalho_bar_finalizar
        "Não. Voltar ao trabalho":


            jump trabalho_bar_tela

label trabalho_bar_finalizar:

    $ renpy.block_rollback()

    $ tempo += 1

    scene pub geral with Dissolve(1.0)

    mc concentrando "Terminei. Acho que arrumei tudo."

    if tb_items == 0:

        show garcom diabolico with dissolve

        gar "Muito bom!"

        if premium:

            $ tb_cash = rand_item_max * 18
        else:


            $ tb_cash = rand_item_max * 9

        gar "Aqui está seu pagamento. C$ [tb_cash] pelo trabalho que você teve hoje."

        mc normal "Valeu."

        gar "Obrigado pelo excelente trabalho. Até mais, [mc]."

        mc normal "Até."
    else:


        show garcom confabulando with dissolve

        gar "Hoje ficou faltando coisa."

        mc envergonhado "Mals..."

        gar "Não se preocupe. Nem todos podem ter os olhos que eu tenho."

        mc zerado "Ser xereta igual você, você quer dizer, né?"

        gar "{i}Cof{/i}"

        gar "Enfim, eis a parte que lhe cabe neste latifúndio."

        mc desconfiado "Como?"

        if premium:

            $ tb_cash = (rand_item_max - tb_items) * 18
        else:


            $ tb_cash = (rand_item_max - tb_items) * 9

        gar "Aqui está seu dinheiro. C$ [tb_cash] pelo seu trabalho hoje."

        mc normal "Valeu!"

        gar "Muito obrigado pela ajuda. Até mais, [mc]."

        mc normal "Até, [gar]!"

    python:
        if renpy.android:
            PythonSDLActivity.ganhaCash(tb_cash)
            cash = PythonSDLActivity.pegaCash()
            tb_mais += 1

    $ renpy.block_rollback()

    play sound "extra/carta.mp3"

    if premium:

        "{b}Como você joga a versão premium, recebeu C$ [tb_cash]. O dobro! É possível trabalhar novamente daqui 3 horas.{/b}"
    else:


        "{b}Você recebeu C$ [tb_cash]. É possível trabalhar novamente daqui 3 horas. Use o app Relógio no celular para saber quando for a hora.{/b}"

        "{b}Não se esqueça que na versão premium você ganha o dobro de C$ trabalhando no bar! É muita diferença no longo prazo!{/b}"

    "{b}Depois de trabalhar, agora você tem C$ [cash] no total.{/b}"

    $ proibido_salvar = False
    $ show_quick_menu = True

    jump call_cidade

    return

label trabalho_bar_introducao:

    "A vida não tá fácil. A grana que eu ganho na revista paga o aluguel, a luz e a pizza."

    "Não consigo comer no Tadaima e nem me divertir no Cassino. Não consigo fazer merda nenhuma."

    "O que adianta viver em uma ilha paradisíaca se não tenho grana pra curtir nada?"

    scene pub dois with Dissolve(1.0)

    mc concentrando "Foda..."

    gar "Impossível deixar de notar a tristeza em seu olhar, senhor [mc]."

    mc desconfiado "[gar]..."

    show garcom confabulando with Dissolve(1.0)

    gar "É sempre incrível ter presenças ilustres como a sua nesta humilde residência."

    mc concentrando "Não tô muito pra conversa maluca hoje..."

    gar "O peso dos problemas materiais lhe afligem o âmago, senhor?"

    mc desconfiado "Se você está querendo dizer que ser pobre tá me incomodando, é isso mesmo."

    show garcom chamando with dissolve

    gar "Talvez eu tenha a resposta para seu problema."

    mc normal "Você pode me emprestar uma grana?"

    gar "De forma alguma, senhor [mc]."

    mc preocupado "Mas então..."

    gar "O que eu proponho é uma parceria em benefício mútuo."

    mc desconfiado "Que tipo de parceria?"

    gar "Eu promovo algumas... {b}festas especiais{/b}... aqui no bar praticamente toda madrugada."

    gar "De forma que o bar precisa estar devidamente apresentável para meus convidados."

    gar "Este estabelecimento também deve estar preparado para receber seus clientes ordinários na tarde do dia seguinte."

    mc "Não sei se estou entendendo..."

    gar "Trocando por palavras mundanas, o que eu preciso é de alguém que me auxilie na árdua tarefa de manter o local limpo."

    mc "Você quer ajuda pra limpar o bar?"

    gar "Eu não poderia resumir de forma mais adequada."

    mc concentrando "Hmmm...."

    gar "O senhor aceita o convite?"

    mc normal "Contanto que eu seja livre pra trabalhar quando eu quiser, eu topo, sim."

    mc "Porque as celebridades vêm em primeiro lugar, e por isso não quero me comprometer com um horário fixo."

    gar "Estou de acordo. Você poderá atuar nos dias que achar melhor, nos períodos da manhã, antes do bar abrir, ou da noite, depois que todos se forem."

    mc "Entendi. Então {b}cedo{/b}, antes de abrir, e à {b}noite{/b}, quando o bar for fechar."

    gar "Isso mesmo. Você receberá {b}R$ 3{/b} por cada peça de louça ou garrafas que você lavar e guardar."

    mc normal "Acho que está de bom tamanho."

    "Muquirana..."

    gar "Eu sei que não é muito, mas o trabalho será pouco também."

    mc envergonhado "Ah, tô ligado. Está excelente."

    show garcom diabolico with dissolve

    gar "Então o pacto está selado."

    gar "Venha que vou lhe explicar o trabalho."

    menu:
        "Ok. Quero aprender como fazer o trabalho.":


            mc normal "Ok. Vamos lá."

            gar "Venha comigo."

            jump trabalho_bar_intro_tuto
        "Eu já sei o que tenho que fazer.":


            mc normal "Acho que eu entendi como funciona. Pode ficar tranquilo."

            gar "Excelente!"

            jump trabalho_bar_introducao_fim

label trabalho_bar_intro_tuto:

    scene pub fundao with Dissolve(3.0)

    gar "É aqui que você vai trabalhar. A maior parte da bagunça acontece aqui atrás."

    mc desconfiado "Aqui é o único lugar que eu preciso limpar?"

    gar "A parte da frente do bar você pode deixar comigo."

    mc normal "Beleza."

    gar "Nesta sua primeira vez, terão apenas duas coisas para você lavar e guardar. Duas conchas, uma azul e uma vermelha."

    gar "Basta você apertar nelas e você terá terminado. Me avise quando pegar as duas. Bom trabalho."

    "{b}Para terminar o trabalho, aperte com seu dedo sobre os itens que estão fora de lugar{/b}"

    "{b}Os itens aparecem em lugares aleatórios e você precisa apertar EXATAMENTE sobre eles para funcionar.{/b}"

    "{b}Se você não encontrar algum dos itens, basta apertar no botão DESISTIR para continuar com o jogo.{/b}"

    "{b}Se você desistir, você receberá um valor proporcional aos itens que você limpou.{/b}"

    $ bar_item_t1 = True
    $ bar_item_t2 = True

    scene pub fundao

    show screen tb_intro_screen

    scene pub fundao

    $ renpy.pause()

    "..."

screen tb_intro_screen():
    tag trab_bar

    zorder 100
    modal True

    add "images/bar/bar_angulo2.jpg" at cidade_trans

    if bar_item_t1:

        imagebutton auto "images/bar/item1_%s.png":
            xalign 0.05
            yalign 0.52
            at cidade_trans
            action [ SetVariable("bar_item_t1", False), Call("tb_t_item_pegou") ]

    if bar_item_t2:

        imagebutton auto "images/bar/item4_%s.png":
            xalign 0.95
            yalign 0.54
            at cidade_trans
            action [ SetVariable("bar_item_t2", False), Call("tb_t_item_pegou") ]

label tb_t_item_pegou:

    $ renpy.notify("Você lavou e colocou o objeto no lugar, falta mais um apenas")

    if not bar_item_t1 and not bar_item_t2:

        $ renpy.notify("Você terminou o trabalho")

        scene pub fundao

        hide screen tb_intro_screen

        scene pub fundao with dissolve

        mc concentrando "Terminei. Peguei os dois."

        show garcom confabulando with dissolve

        gar "Exuberante atuação, senhor [mc]."

        mc envergonhado "Obrigado. Mas foi bem simples na verdade..."

        gar "E será isso todas as vezes. Mas serão mais peças para você lavar e guardar."

        mc normal "Sem problemas."

        gar "Vamos lá na frente."

        jump trabalho_bar_introducao_fim

label trabalho_bar_introducao_fim:

    scene pub geral with Dissolve(1.0)

    show garcom diabolico with dissolve

    gar "Então estamos combinados. Pode iniciar quando seu coração desejar."

    mc normal "Obrigado pela oportunidade, [gar]."

    gar "Quem encontra-se agradecido neste momento sou eu, senhor [mc]."

    gar "Sua ajuda será de imensurável serventia."

    mc normal "Então tá. Falou."

    gar "Até breve."

    hide garcom with dissolve

    "Boa! O pagamento é pouco, mas é igual Uber, se tu trabalhar igual condenado dá pra ganhar alguma coisa."

    "Essa grana vai liberar muitas novidades pra mim na ilha. Vou poder fazer compras, comer comida boa, conhecer novas pessoas."

    "Preciso trabalhar o máximo que eu puder e juntar o máximo de grana pra estar preparado."

    mc charmoso "Bora, [mc]!"

    scene black with Dissolve(1.0)

    p rindo "Agora o [mc] pode trabalhar de manhã e de noite no bar do [gar]. Aproveite essa chance!"

    p "Se ele juntar dinheiro suficiente, você vai poder comprar roupas, conhecer novos personagens e até mesmo comprar uma casa!"

    p "Além de claro se esbaldar jogando no Cassino. Não tenha preguiça e se prepare para o futuro! Trabalhe sempre que tiver um tempo!"

    p "Mas se trabalhar por mixaria não é sua cara, saiba que você pode fazer o [mc] ficar rico usando dinheiro do seu mundo."

    p "Dê uma olhada na Loja no Menu e garanta uma vida de marajá sem ter que arcar com a parte ruim."

    p "Como CH é desenvolvido por apenas uma pessoa, e sem muitos recursos, todo dinheiro que você usa no game ajuda no desenvolvimento."

    p "Você estará contribuindo para que o jogo continue sendo atualizado com novos lugares e novos personagens."

    p "Boa sorte!"

    $ trabalho_bar = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("trabalho_bar_introducao","fabricio","personagem")

    $ tempo += 1

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
