label cenario_distrito_tempo:

    if tempo < 3:

        "Visitar o Distrito de manhã ou à tarde pode chamar muita atenção. Melhor ir lá só durante a noite."

        jump cenario_onibus_menu
    else:


        "Ir pro Distrito vai usar um período do meu dia. Quando eu voltar, vou direto pra cama..."

        menu:
            "Pegar o ônibus até o Distrito":


                if xiang_escape >= 5 and not xiang_fim:

                    if distrito_liberou:

                        $ xiang_on = False

                        "Mesmo com o rolo da Xiang, agora o Black Cash precisa de mim. Eles não vão me pegar."
                    else:


                        "Depois do que aconteceu lá quando eu salvei a [i] eu não volto lá nem ferrando."

                        "E é bom eu ficar de olho aberto... mesmo aqui na ilha eu acho que eles podem vir atrás de mim."

                        jump cenario_onibus_menu

                $ tempo += 1

                "Sempre dá um frio na barriga ir pra lá."

                "Agora é esperar o busão."

                call cena_onibus from _call_cena_onibus_8

                jump cenario_distrito
            "Vou deixar pra outro dia.":


                "Acho que não vou lá agora, não. Sem saco pra isso hoje."

                jump cenario_onibus_menu

label cenario_distrito:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("cenario_distrito","distrito","cenario")

    if premium and natasha18 == 0:

        call natasha_18_distrito from _call_natasha_18_distrito

    scene distrito geral with Dissolve(2.0)

    $ randis = renpy.random.randint(1,5)

    if randis == 1:

        "Muita gente de terno pra variar..."

    elif randis == 2:

        "Como que eu nunca tinha ouvido falar deste lugar?"

    elif randis == 3:

        "Fico pensando o que esses outros estabelecimentos fazem... Tenho que descobrir um dia aí."

    elif randis == 4:

        "E pensar que o [us] tá envolvido com quem manda em tudo isto aqui."

    elif randis == 5:

        "Um pouco de diversão adulta não faz mal a ninguém."

        mc envergonhado "..."

    if natasha_evento >= 8 and natasha_e3 == "nada":

        jump natasha_evento3

    menu:
        "Visitar o Clube de BDSM":


            "..."

            jump clube_bdsm_entrada
        "Voltar para a ilha":


            "Tá tarde. Melhor voltar pra ilha."

            jump call_cidade

label clube_bdsm_entrada:

    if bdsm_1vez == 0:

        if stifler_e1 != "puritano":

            "Eu lembro mais ou menos onde fica o lugar... eu não prestei tanta atenção naquela primeira vez que eu vim aqui com o [us]."
        else:


            "Da outra vez eu não quis ir lá com o [us]. Agora vou ter que descobrir o caminho até o clube."

        "Acho que é por aqui..."

        "..."

        $ bdsm_1vez = 1
    else:


        mc normal "Agora eu sei exatamente onde o clube fica."

        mc zerado "Pensando bem, não sei por que eu teria orgulho disso..."

    scene distrito esquina with Dissolve(2.0)

    if bdsm_1vez <= 1:

        if stifler_e1 != "puritano":

            "Ah! Era bem aqui... bem do lado desse sex shop."

            mc safado "Sex shop... será que eu vou vir comprar algo aqui pra alguém um dia?"

            "Agora não é hora de viajar."
        else:


            "Pelo nome, deve ser bem aqu-"

        mc surpreso "AH!"

        show montanha emburrado with Dissolve(1.0)

        mon "Boa noite, senhor. O que foi?"

        if stifler_e1 != "puritano":

            mc envergonhado "Nã-não é nada. Só tinha esquecido que você ficava aqui..."
        else:


            mc preocupado "Nã-não-não é nada..."

        show montanha normal with dissolve

        if stifler_e1 != "puritano":

            mon "Ah! Você é o amigo do Black Cash!"

            mon "Seja bem-vindo ao {b}Clube de Sadomasoquismo{/b}."

            mc normal "Valeu. Ele tá aqui?"

            mon "Não vi ele entrando. Talvez ele chegue mais tarde."

            mc "Beleza, valeu."
        else:


            mon "Seja bem-vindo ao {b}Clube de Sadomasoquismo{/b}."

            mc normal "Valeu."

        if stifler_e1 != "puritano":

            mon "Pode entrar. Fiq-"

            show montanha emburrado with dissolve

            mon "Epa! Na verdade ele disse que você precisa pagar se quiser entrar."

            mon "Desculpa maninho, mas ordens são ordens."

            "Maldito [us]..."
        else:


            mon "Se você quer curtir uma noite diferenciada em nosso clube, existe uma pequena taxa."

        mc serio "E quanto é pra entrar?"

        mon "É coisa pouca. São apenas {b}R$ 10{/b} e você ainda tem direito a um drink na faixa e ver as garotas se apresentando."

        "Realmente não é caro pelo que eles oferecem..."

        mc desconfiado "É bem barato..."

        mon "Com certeza. Mas claro que você tem que pagar um adicional caso você queira algo a mais com as garotas, entende maninho?"

        mc safado "Entendo..."

        show montanha rindo with dissolve

        $ mon_nome = "Montanha"

        mon "A galera me conhece como Montanha. Prazer."

        mc normal "Prazer, [mon]. Eu sou o [mc]."

        if stifler_e1 != "puritano":

            mon "Espero ver você mais vezes, [mc]. Ainda mais que você é mano do Black Cash."

            mc "Pode deixar."

        $ bdsm_1vez = 2
    else:


        "Esse segurança sempre me assusta... [mon]... vê se isso é nome..."

        show montanha normal with dissolve

        if distrito_liberou:

            mon "Olha só. O maninho por aqui."

            if black_salva > 0:

                mon "Obrigado pelo que você fez pela mana Diana, amigo."

                mc "De nada, Montanha. Ela merecia."
            else:


                mon "Qual a boa, mano [mc]? Tem gente te esperando?"

                mc "Sim."
        else:


            mon "Fala aí, mano [mc]. Como vai?"

            mc normal "Tudo legal, [mon]. E você?"

            mon "Tudo na santa paz."

            mc "Bacana."

            mon "Veio ver as garotas nesta noite linda?"

    label clube_grana:

        python:
            if renpy.android:
                distrito_db = PythonSDLActivity.pegaDistrito()
                distrito_soma = distrito + 1

        if distrito_soma < distrito_db:

            "{b}Você já pagou para entrar no clube de BDSM [distrito_db] vezes. Mas neste gameplay você entrou apenas [distrito] vezes.{/b}"

            "{b}Como não é preciso pagar duas vezes pelo mesmo evento, você pode entrar sem esperar novamente.{/b}"

            $ distrito += 1

            python:
                if renpy.android:
                    renpy.block_rollback()

            jump clube_bdsm

        python:
            if renpy.android:
                cash = PythonSDLActivity.pegaCash()

        "Tem uma taxa de {b}C$ 10{/b} para entrar no clube."

        "Eu tô com {b}C$ [cash]{/b}..."

        if cash >= 10:

            "Tá tranquilo."
        else:


            "O foda é que não dá pra eu pagar nem essa mixaria."

            mc preocupado "..."

            show black with Dissolve(1.0)

            p lecionando "Ixi. O [mc] tá pobre que só ele..."

            p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

            p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

            p "Além de avançar na história agora mesmo, você ainda contribui com o desenvolvimento de CH."

            p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

            menu:
                "Sim. Tô com uma graninha sobrando aqui.":


                    p rindo "Que bom!"

                    call comprar_cash from _call_comprar_cash_4

                    p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                    hide black with dissolve

                    jump clube_grana
                "Não. Tô pobre igual a ele...":


                    p rindo "Não esquente."

                    p "Trabalhe sempre que possível no bar e vá juntando seus reais. Logo logo você já vai estar com grana suficiente."

                    p "Demora, mas vale a pena!"

                    hide black with dissolve

                    mon "E então? Vai entrar?"

                    jump clube_bdsm_entrada_sair

        mon "E então? Vai entrar?"

        menu:
            "Pagar {b}R$ 10{/b} e entrar no clube.":


                mc charmoso "Vou sim. Tá na mão."

                mon "Bom divertimento, maninho."

                "..."

                python:
                    if renpy.android:
                        PythonSDLActivity.usaCash(10)
                        PythonSDLActivity.addDistrito
                        PythonSDLActivity.registraEvento("clube_bdsm_pagou","blackcash","personagem")
                        distrito += 1

                    renpy.block_rollback()

                jump clube_bdsm

            "Quem está no clube hoje?" if bdsm_1vez >= 4:

                mon "Deixa eu lembrar..."

                if celeste_on:

                    mon "Que raridade! A [ce] tá aí hoje. Tome cuidado com ela, maninho..."

                if xiang_on:

                    mon "Hoje é noite da [i] se apresentar. Ela já tá aí."

                if stifler_on:

                    mon "Hoje seu mano Black Cash tá curtindo o clube."

                jump clube_grana
            "Agora não, [mon]. Tenho outras coisas pra fazer.":


                label clube_bdsm_entrada_sair:

                    mc normal "Só vim te dar um alô mesmo. Tenho outras coisas pra fazer agora."

                show montanha rindo with dissolve

                mon "De boa, [mc]. Vê se passa depois aí."

                mc "Demorou. Até, [mon]."

                mon "Até, maninho."

                jump cenario_distrito

label clube_bdsm:

    $ renpy.block_rollback()

    scene distrito_clube geral with Dissolve(1.0)

    if bdsm_1vez <= 2:

        "Primeira vez que eu venho sozinho aqui. Dá ainda mais medo."

        "Essas gaiolas penduradas... as correntes..."

        "É um cenário bem diferente do que eu tô acostumado."

        "Será que algum dia eu vou me acostumar com tudo isso?"

        $ bdsm_1vez = 3
    else:


        "Acho que vai ser impossível eu me acostumar com a vibe deste lugar..."

    "Deixa eu sentar ali no bar."

    scene distrito_clube pub with Dissolve(1.0)

    "Opa!"

    label bdsm_clube_bar:

        show mc bdsm_angulo_sul with dissolve

    if bdsm_1vez <= 3 and not stifler_e2_fim:

        "E agora? O que eu-"

        nora "Boa noite, rapaz."

        mc "Ah?"

        nora "Você parece um tanto quanto perturbado."

        show mc bdsm_nora with Dissolve(1.0)

        mc "Ah! Boa noite, senhora."

        nora "Posso te ajudar com alguma coisa?"

        mc "É... Eu-"

        nora "Vou pegar sua bebida."

        mc "Mas-"

        nora "Não se preocupe, a primeira é por conta da casa."

        "..."

        nora "Aqui está."

        mc "O-obrigado."

        scene mc bdsm_bebendo_normal with Dissolve(1.0)

        pause

        mc "Isso aqui tá bem gostoso, mas é forte pra caramba."

        nora "É algo especial que eu criei."

        mc "A senhora que criou? E o que vai?"

        nora "Não pense muito nisso. Ela é composta por treze ingredientes diferentes e mais um elemento secreto."

        "Treze ingredientes? Isso me-"

        nora "Mas eu recomendo que você não beba muito. Principalmente se você não está acostumado."

        mc "O-ok..."

        nora "Eu vou deixar você em paz. Qualquer coisa me chame."

        mc "Obrigado. Pode deixar."

        "..."

        "Ufa... esse treco desce queimando... e minha cabeça tá rodando, só que parece que eu parei bem na hora certa."

        "Um gole a mais e eu tenho a impressão que eu teria ficado louco."

        scene distrito_clube pub with Dissolve(1.0)

        show mc bdsm_angulo_sul with dissolve

        "Ufa... Tô me sentindo melhor."

        "Voz conhecida" "Bu!"

        mc "[us]?!"

        us "Quem mais?"

        show mc bdsm_blackcash with Dissolve(1.0)

        mc "Fala aí, mano!"

        us "Beleza?"

        $ bdsm_1vez = 4

        jump stifler_evento2

    "E agora? O que eu vou fazer hoje?"

    menu:

        "Ver apresentação da Xiang" if xiang_on and xiang_show:

            $ xiang_show = False

            "Opa! Hoje é dia de apresentação da [i]."

            "Não perco por nada."

            scene xiang pole_fundo with Dissolve(2.0)

            "..."

            "Vai começar daqui a pouco."

            "Opa! Aí vem ela."

            scene xiang pole_1 with Dissolve(1.0)

            $ renpy.pause(delay=5, hard=True)

            pause

            scene xiang pole_2 with Dissolve(1.0)

            $ renpy.pause(delay=5, hard=True)

            pause

            scene xiang pole_3 with Dissolve(1.0)

            $ renpy.pause(delay=5, hard=True)

            pause

            scene xiang pole_4 with Dissolve(1.0)

            $ renpy.pause(delay=5, hard=True)

            pause

            "Show incrível! A [i] é demais."

            i "..."

            if xiangu_evento == 3 and xiang_evento == 3 and not xiang_xiangu:

                mc normal "[i]!"

                i "?"

                "Acho que ela me ouviu."

                mc normal "Eu conheci uma chinesa chamada [xu] na Cidade Chinesa! Quero falar com você sobre ela!"

                i "!"

                i "..."

                scene xiang pole_fundo with Dissolve(1.0)

                mc zerado "Foi embora sem falar nada..."

                "Com certeza ela me ouviu. E o que eu disse mexeu com ela. Deu pra ver na cara dela."

                "Talvez agora ela aceite falar comigo em particular. Eu devia tentar marcar com ela."

                $ xiang_xiangu = True

                jump clube_bdsm

            scene xiang pole_fundo with Dissolve(1.0)

            mc zerado "Foi embora sem falar nada..."

            jump clube_bdsm

        "Pagar um show particular da Xiang" if xiang_on:

            if xiang_evento >= 10:

                if xiang_escape >= 4:

                    if not xiang_fim:

                        pass
                    else:


                        "Eu não salvei a [i]... acho melhor eu me afastar dela..."

                        "Se ela tinha o sonho de sair daqui comigo, então ver ela só vai trazer mais dor pra garota."

                        "Eu nunca vou falar com ela assim de novo."

                        jump bdsm_clube_bar
                else:


                    if not xiang_fim:

                        "Eu preciso encontrar uma forma de tirar a [i] dessa. Não adianta eu voltar aqui agora."

                        "Tem que ter um jeito. Não tá certo as coisas continuarem assim. Me espere, [i]. Eu vou voltar."

                        jump bdsm_clube_bar
                    else:


                        "Eu não salvei a [i]... acho melhor eu me afastar dela..."

                        "Se ela tinha o sonho de sair daqui comigo, então ver ela só vai trazer mais dor pra garota."

                        "Eu nunca vou falar com ela assim de novo."

                        jump bdsm_clube_bar

            if xiang_evento >= 4:

                if xiang_evento == 10:

                    "É hora de começar com o plano de tirar a [i] daqui. Eu tenho que agir o mais normal possível."
                else:


                    "O que será que deu errado da outra vez? Será que eu tenho que fazer alguma coisa com ela lá?"

                    "Eu tenho que tentar de novo."
            else:


                "Vou tentar marcar um show particular com a [i]. É aquela senhora que cuida disso."

            mc "[nora]."

            show mc bdsm_nora with Dissolve(1.0)

            nora "Boa noite, jovem. Como posso te ajudar hoje?"

            mc "Você acha que a [i] pode fazer um show particular pra mim agora?"

            python:

                renpy.choice_for_skipping()

                if renpy.android:
                    xiang_evento_db = PythonSDLActivity.pegaXiang()

            if xiang_evento < xiang_evento_db and not xiang_errou:

                "{b}Você já pagou pelo show da Xiang [xiang_evento_db] vezes. Mas neste gameplay você viu a apresentação dela [xiang_evento] vezes.{/b}"

                "{b}Como não é preciso pagar duas vezes pela mesma coisa, você pode continuar a história sem pagar novamente.{/b}"

                jump xiang_show_inicio

            if xiang_evento == 3 and xiangu_evento <= 3 and not xiang_xiangu:

                if xiangu_evento == 3:

                    "Agora que eu consegui informações da [xu] talvez a [i] fale comigo. Mas é melhor eu falar pra ela antes."

                    "Talvez eu devesse falar com ela durante uma das {b}apresentações no palco{/b}."

                    "Quem sabe se eu citar a [xu] ela tenha alguma reação. Não pode ser só coincidência que duas chinesas tenham a mesma tatuagem."
                else:


                    nora "Você vai ter que me desculpar, jovem. Mas a garota não tá se sentindo bem nos últimos dias."

                    mc "Sério?! O que aconteceu com ela?"

                    nora "Nunca vi a fedelha desse jeito antes. Acho que algum cliente mexeu com ela ou algo assim."

                    mc "Isso é horrível!"

                    nora "Não é pra tanto. Ela vai se recuperar."

                    nora "Ela continua se apresentando no palco. Mas não quer ver ninguém em particular."

                    "Tenho a impressão que a [nora] não tá nem aí pra [i]."

                    "Hmmm... tenho que tentar alguma coisa que faça a [i] falar comigo."

                    "Ela é uma chinesa. Talvez, se eu me envolver mais nas coisas da Cidade Chinesa, eu descubra algo que chame a atenção dela."

                    "{b}Tome banhos de saúde e beleza e trabalhe com o Bao Chang na Cidade Chinesa para liberar o resto da história da [i]{/b}"

                jump bdsm_clube_bar

            elif xiang_evento == 3 and xiangu_evento <= 3 and xiang_xiangu:

                nora "Muito estranho... ela não quer ver ninguém. A não ser que seja você..."

                nora "O que aconteceu entre vocês?"

                mc "Não faço ideia."

                nora "Hmmm..."

                "Ter falado da [xu] com certeza fez efeito."

                mc "Então eu posso ver ela?"









            nora "Com certeza. É pra isso que ela tá aqui."

            if xiang_evento > 3 and xiang_evento < 8:

                nora "Mas ela só aceita fazer um show particular pra você."

                nora "Acho bom ela mudar de ideia logo. Não vou continuar alimentando uma boca inútil."

            elif xiang_evento >= 8:

                nora "Sorte dela que ela voltou a atender todos os clientes. Odeio garotas imprestáveis."

            label xiang_show_grana:

                nora "O bom é que o preço do showzinho dela é bem barato. Qualquer um pode pagar. É {b}C$ 50{/b}."

            python:
                if renpy.android:
                    cash = PythonSDLActivity.pegaCash()

            "Eu tô com {b}C$ [cash]{/b}..."

            if cash >= 50:

                "Beleza. Dá pra eu pagar pelo show. "
            else:


                "Tô sem grana pra ver o show da [i]..."

                mc "Que merda..."

                show black with Dissolve(1.0)

                p lecionando "Ixi. O [mc] não está com essa corda toda, não..."

                p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

                p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

                p "Além de avançar na história agora mesmo, você ainda contribui com o desenvolvimento de CH."

                p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

                menu:
                    "Sim. Tô com uma graninha sobrando aqui.":


                        p rindo "Que bom!"

                        call comprar_cash from _call_comprar_cash_5

                        p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                        hide black with dissolve

                        jump xiang_show_grana
                    "Não. Tô pobre igual a ele...":


                        p rindo "Não esquente."

                        p "Trabalhe sempre que possível no bar e vá juntando seus reais. Logo logo você já vai estar com grana suficiente."

                        p "Demora, mas vale a pena!"

                        hide black with dissolve

                        jump bdsm_clube_bar

            mc "Eu tô com a grana aqui."

            nora "Posso chamar ela pra você?"

            $ renpy.choice_for_skipping()

            python:
                if renpy.android:
                    cash = PythonSDLActivity.pegaCash()

            menu:

                "Sim. Quero um show particular da Xiang." if cash >= 50:

                    $ proibido_salvar = True
                    $ show_quick_menu = False

                    mc "Sim. Pode avisar ela."

                    nora "Pode ir sentar que eu chamo ela pra você."

                    mc "Obrigado."

                    python:
                        if renpy.android:
                            PythonSDLActivity.usaCash(50)

                    $ renpy.block_rollback()

                    jump xiang_show_inicio
                "Pensando bem, deixa pra outra hora.":


                    mc "Pensando bem, acho que vou deixar pra outra hora."

                    nora "Sem problemas. Ela vai estar pronta pra você sempre que você quiser."

                    mc "Ok..."

                    jump bdsm_clube_bar

        "Falar com o [us]" if stifler_on and stifler_falou:

            $ stifler_falou = False

            "Tenho que aproveitar que o [us] tá aqui pra bater um papo."

            mc "Mano [us]! Chega aí!"

            if nathan_stifler == 0 and nathan_e8 != "nada":

                $ nathan_stifler = 1

                jump n8_distrito

            if stifler_conversa == 0:

                show mc bdsm_blackcash with Dissolve(1.0)

                us "Fala aí, [mc]. A coisa tá corrida, por isso precisa ser jogo rápido."

                mc "Beleza."

                mc "Como tão as coisas? Tá acelerado..."

                us "Correria como sempre."

                mc "Por que você tá sempre correndo nesses últimos dias?"

                us "Muito trabalho, [mc]. Tem que fazer uma cobrança aqui, outra ali..."

                mc "Cobrança?"

                us "Como eu posso explicar?"

                us "..."

                us "Às vezes os clientes não pagam o que prometem, entende? Daí eu tenho que ir lá receber."

                mc "Certo..."

                mc "Mas e se eles não te pagarem? Porque se já deram calote da primeira vez..."

                us "Daí a gente precisa receber de um jeito ou de outro. Ou se não a [nora] vai querer receber de mim."

                mc "De você?!"

                us "Bom, passa aí outra hora e te explico melhor."

                us "Vou indo nessa. Grande abraço."

                mc "Até a próxima, [us]."

                "Até agora eu não entendi no que o [us] trabalha aqui no Distrito. Cobranças?"

                $ stifler_conversa = 1

                jump bdsm_clube_bar

            elif stifler_conversa == 1:

                "Até agora eu não entendi no que o [us] trabalha aqui no Distrito. Cobranças?"

                show stifler bdsm_bar with Dissolve(1.0)

                us "E aí, mano? Tudo na santa paz?"

                mc "Os problemas de sempre."

                us "Pela sua cara, ou é dinheiro ou é mulher."

                mc "Os dois..."

                us "Haha!"

                mc "Não quero te atrasar porque sei que tu tá enrolado, mas queria saber mais sobre seu trabalho aqui."

                us "Claro. Eu trabalho fazendo cobranças e outros serviços externos."

                mc "Ok..."

                us "Tipo, pegar um lance e trazer pra cá ou levar alguma coisa pra alguém."

                mc "Tipo um motoboy."

                us "Mais ou menos. Eu realmente sou tipo um garoto de recados. Só que é um pouco mais complicado do que isso."

                us "Nem sempre minha visita tá me esperando. E nem sempre eles querem me receber."

                mc "Como assim, mano? Que viagem..."

                us "Pois é... tipo quando você tá esperando o oficial de justiça e não quer receber ele."

                mc "Mas por que eles não querem falar contigo?"

                us "Cara, deixa pra próxima. Tenho que ir nessa."

                mc "Valeu, grande abraço."

                hide stifler with dissolve

                $ stifler_conversa = 2

                jump bdsm_clube_bar

            elif stifler_conversa == 2:

                "Então o [us] trabalha tipo como um secretário, mas fazendo coisa externa. Tipo visitando clientes e talz."

                "Acho que já tô entendendo melhor. Sinceramente, eu esperava que fosse algo mais glamuroso."

                show stifler bdsm_bar with Dissolve(1.0)

                mc "Opa!"

                us "E aí?"

                us "Pensando na vida?"

                mc "Tipo isso hehe..."

                mc "Tava aqui tentando entender seu trabalho aqui no clube."

                us "Certo..."

                nora "Acho que eu posso ajudar com isso."

                show mc bdsm_nora with Dissolve(1.0)

                mc "[nora]!"

                nora "Boa noite, garotos."

                us "Fala aí, [nora]."

                nora "O BlackCash chegou aqui parecendo um pedaço de merda, mas hoje ele se tornou peça fundamental da nossa casa."

                us "Merda... pegou pesado, hein."

                nora "Peguei não, filho. Você estava na merda mesmo."

                us "Pior é que é verdade..."

                mc "Eu lembro que você me contou do fim da sua carreira..."

                us "Ah, mano. É uma história triste. Deixa quieto."

                nora "Não fale isso. Tudo o que aconteceu com você é parte da sua história e é parte do que você é hoje."

                nora "Se você negar sua história, vai negar uma parte de você."

                us "Se a senhora diz..."

                mc "Ela tá certa, [us]. Você não precisa se sentir mal por isso."

                us "Me deixem."

                us "Não importa o que aconteceu. Eu tô feliz aqui agora. Eu vou dar minha vida se for preciso pra proteger o Distrito."

                nora "E é por isso que você é tão importante pra gente, filho."

                nora "Agora você tem que ir, não tem?"

                us "Pior que é verdade. Vou nessa galera. Fui!"

                hide stifler with dissolve

                mc "O trabalho do [us] é perigoso?"

                nora "Tudo é perigoso nesta vida, jovem. Mas eu perdi tempo demais falando com você. Tenho que resolver algo."

                mc "Ok. Boa noite, [nora]."

                nora "Boa noite, filho."

                $ stifler_conversa = 3

                jump bdsm_clube_bar

            elif stifler_conversa == 3:

                "O [us] parece que tá na correria hoje pra variar. Melhor deixar pra falar com ele outro dia."

                jump bdsm_clube_bar

        "Falar com a [ce]" if celeste_on and celeste_falou:

            $ celeste_falou = False

            if xiang_escape >= 4 or xiang_fim:

                "Eu não posso mais falar com a [ce]. Nunca mais. Foi o que a gente acertou."

                "Vou deixar ela em paz e esquecer que a gente já se conheceu um dia."

                jump bdsm_clube_bar

            if stifler_e1 != "puritano" or celeste_conheceu:

                "Parece que a [ce] tá aqui hoje. Caraca, é muito raro ver ela no clube."

                "Vou lá chamar ela."

                scene distrito_clube pub with Dissolve(1.0)

                "..."

                show mc bdsm_celeste with Dissolve(1.0)

                ce "Oi..."

                if celeste_conversa == 0:

                    mc "Tudo bem com você, [ce]?"

                    ce "Tudo bem. Só que é perigoso a gente conversar muito."

                    mc "Por que?"

                    ce "..."

                    if celeste_fotos:

                        ce "{size=15}Você publicou na sua revista as informações que eu te passei?{/size}"

                        if celeste_atencao == 1:

                            mc "Sim. Por que?"

                            ce "Eu ainda não li a matéria."

                            mc "O chefe ficou um tanto estranho quando eu entreguei. Ele disse que era preciso confirmar se as fotos eram verdadeiras."

                            ce "Você entregou as fotos pra ele?"

                            mc "Sim."

                            ce "Merda... então ele também tá envolvido. Vai ser mais complicado do que eu imaginava."

                            mc "Como assim? No que o chefe tá envolvido?"

                            ce "[mc]... é [mc], né?"

                            mc "Isso."

                            ce "Ainda é cedo pra eu ter certeza. Vamos esperar mais um pouco. Às vezes ele realmente só tá checando as fotos."

                            ce "Da próxima vez que a gente se ver a gente decide o que fazer."

                            mc "Ok... mas você tá me dando um pouco de medo."

                            ce "Não tenho tempo pra ser psicóloga, [mc]. Se você quer me ajudar, vire homem."

                            mc "O-ok..."

                            ce "Quando cair da gente se ver de novo no clube me chame."

                            ce "Adeus."

                            show mc bdsm_angulo_sul with Dissolve(1.0)

                            "O que foi isso? O que a [ce] tá tramando?"

                            "Parece que tem algo a ver com o chefe também."

                            "Espero que eu encontre ela aqui de novo logo. É difícil ela passar por aqui. Vou precisar de um pouco de sorte."

                            "E passar aqui todos os dias também..."

                            $ celeste_conversa = 1

                            jump bdsm_clube_bar
                        else:


                            mc "Ainda não."

                            ce "Por que?"

                            mc "Não sei... essas informações parecem perigosas. Fala de gente grande, entende?"

                            ce "Eu sei. E por isso é tão importante."

                            ce "Só venha falar comigo depois de ter publicado a matéria."

                            ce "Não podemos ser vistos juntos assim por nada. Por favor."

                            mc "Ce-certo..."

                            jump bdsm_clube_bar
                    else:


                        call celeste_e1_conversa from _call_celeste_e1_conversa

                        jump clube_bdsm

                elif celeste_conversa == 1:

                    mc "Oi. Tudo bem?"

                    ce "Tudo."

                    mc "Você fala isso, mas você sempre parece nervosa. O que tá acontecendo?"

                    ce "..."

                    ce "Vem comigo, [mc]."

                    scene distrito_clube visao with Dissolve(1.0)

                    mc serio "Aqui?"

                    show celeste incerta with Dissolve(1.0)

                    ce "Aqui tá bom."

                    ce "..."

                    ce "Não tem ninguém olhando."

                    mc preocupado "Você vai me falar o que tá havendo?"

                    ce "Só escuta."

                    ce "Já passou tempo demais, você não acha? Sua revista já deveria ter publicado a matéria."

                    mc serio "Normalmente eles publicam primeiro no site, que não tem tanta visibilidade antes de sair na revista impressa."

                    ce "Entendo. Mas nem no site tá ainda."

                    mc desculpa "Isso é estranho, mesmo... Uma pauta bomba dessas eles publicariam na hora eu imagino."

                    ce "Exatamente. Eu tenho certeza que seu chefe tá acobertando o diretor do banco."

                    mc surpreso "Quê?!"

                    ce "Xiu!"

                    mc desculpa "Desculpa, mas por que o chefe teria o rabo preso com esse diretor?"

                    ce "Existem vários motivos, mas um deles com certeza é o mais provável."

                    ce "Você parece uma criança, [mc]... Você não sabe nada da guerra entre as gangues?"

                    mc desconfiado "Gangues?"

                    ce "..."

                    ce "A [nora] tá começando a olhar pra cá. Isso é muito ruim. Melhor pararmos por aqui."

                    ce "Eu vou falar mais sobre isso com você outro dia."

                    mc preocupado "Mas por que você parece tão aflita?"

                    ce "Não pense nisso. Não vai ajudar em nada você ficar preocupado comigo."

                    mc "Só q-"

                    ce "Chega. Vamos falar mais uma outra oportunidade."

                    ce "Obrigada pela ajuda. Espero que as coisas corram bem."

                    mc "[ce]..."

                    $ celeste_conversa = 2

                    jump clube_bdsm

                elif celeste_conversa == 2:

                    if bao_evento == 6:

                        $ celeste_conversa = 3

                        mc "Oi. Eu tenho um negócio sério pra falar com você."

                        ce "Eu tô pegando uma vibração boa de você. Tô sentindo que a hora chegou."

                        mc "Não sei se é o que você tava esperando, mas eu tô com uma loucura na cabeça."

                        ce "Calma. Eu vou fingir pra [nora] que eu vou te atender. Vai indo pra lá."

                        mc "T-tá."

                        scene distrito_clube pub with Dissolve(1.0)

                        ce "Eu vou apanhar daquele sujeitinho ali. Não interrompa."

                        nora "Daquele ali? Não creio. Aquele moleque é um frouxo."

                        ce "Talvez eu desperte essa vontade nas pessoas..."

                        nora "Verdade? Eu devia ter batido mais em você quando era pequena, isso sim."

                        ce "Seja como for, velha, não interrompa."

                        nora "Não se preocupe. Se você tem tanta tara por ser abusada, eu não quero nem saber."

                        scene black with dissolve

                        scene mc_celeste1 with dissolve

                        pause

                        mc "U-uou..."

                        ce "Que foi? Você já me viu várias vezes assim."

                        menu:
                            "E toda vez eu fico excitado.":


                                mc "E toda vez eu fico excitado. Você é muito gata, [ce]."

                                ce "Calma... calma... eu tô assim pra [nora] achar que você tá me batendo."
                            "Eu prefiro você com mais roupa.":


                                mc "Sendo sincero, eu prefior você com mais roupa."

                                ce "Eu não ligo, mas a [nora] precisa acreditar que você tá batendo em mim agora."

                        ce "Ela não pode suspeitar que a gente fala sobre outras coisas."

                        mc "A-ah..."

                        ce "Não se preocupe. Você não precisa bater de verdade."

                        "Ah..."

                        menu:
                            "E se eu quiser?":


                                mc "Mas e se eu quiser dar..."

                                ce "Nem termine essa frase. Se você quiser bater em alguém, tem várias garotas aqui pra você escolher."

                                ce "Em mim você não vai relar, entendeu?"

                                mc "Tudo bem..."

                                "Que ia ser interessante, com certeza ia..."
                            "Deixa pra lá...":


                                mc "Que bom."

                        ce "Mas o que você queria me falar de sério?"

                        mc "É mais complicado do que parece. É uma coisa maior que o Distrito. Envolve o outro lado da cidade."

                        mc "Só que resumindo, eu quero tirar a Xiang daqui."

                        ce "Hmm... você entende que essas garotas são propriedades da [nora], né? Você não pode só 'levar' elas."

                        mc "Ninguém pode ser propriedade de ninguém, [ce]. Isso é crime."

                        ce "Verdade? Tem gente que faz coisa errada no mundo? Que coisa, hein?"

                        mc "..."

                        ce "A [nora] é responsável pelo maior clube do Distrito. Ela é tipo uma rainha aqui."

                        ce "Você entende que figurões do mercado financeiro, da política, ricos, pobres, até os italianos vêm aqui."

                        ce "Rola muito dinheiro nesse clube, [mc]. Muita gente depende do sucesso dela. Ela não vai só desistir da [i] assim."

                        mc "Eu sei... por isso que eu preciso de ajuda."

                        ce "E é muito maior que isso. Você sabe, a [i] é a única oriental que trabalha no Distrito. E não é coincidência."

                        ce "A presença dela aqui é muito valiosa pra [nora]. Muito mais do que uma prostituta rara."

                        mc "Então não dá? É isso?"

                        scene mc_celeste2 with Dissolve(1.0)

                        ce "Claro que não dá. Tem coisas que não dá pra mexer, [mc]. Você é só um cara de uma revista. Você não é o Rambo."

                        mc "Eu sei... por isso que eu vim falar com você. Você conhece os lances que rolam aqui."

                        mc "E você sempre pareceu querer ver as coisas acontecerem. Com a pauta que você me deu e tudo."

                        ce "É. Eu vivi aqui a minha vida toda. Eu sei como as coisas são. Por isso que eu tô falando."

                        ce "Mesmo que você traga a polícia. A polícia é corrupta. Ela tá na mão dos italianos. E os italianos gostam do clube."

                        ce "Então é isso. Não dá, entendeu?"

                        mc "Se nem a polícia..."

                        "Então não dá pra tirar a [i] daqui. Não dá pra levar ela pra He Xiangu no portal e é isso... acabou..."

                        "Eu também não sei o que eu tava pensanod. Como que uma pessoa ia fazer isso se até a polícia tá no jogo."

                        ce "Olha... certas coisas a gente só tem que deixar pra trás. Não adianta ficar se coisando por causa disso."

                        ce "Era uma ideia infantial desde o começo. A vida não é fácil."

                        menu:
                            "Você tem razão.":


                                mc "Você tá certa. Não tem como uma pessoa fazer um resgate desses."

                                ce "Quanto mais cedo você entender melhor."
                            "Eu não desisti ainda.":


                                mc "Eu não desisti ainda, [ce]. Eu vou dar um jeito de tirar ela daqui. Tem muita coisa em jogo."

                                ce "Tanto faz. Logo logo você vai cair na realidade."

                        mc "..."

                        ce "Você é um bom jornalista, [mc]. Mas não tente fazer aquilo que não tem a ver com você."

                        ce "Não existem heróis nesse mundo."

                        ce "Não vem mais falar comigo sobre isso. Agora, se a matéria que eu passei der alguma coisa daí você me procura."

                        mc "Hmm... tá."

                        scene black with dissolve

                        scene distrito_clube geral with Dissolve(1.0)

                        "Merda... eu achei que a [ce] ia dar um jeito. Mas talvez ela tenha razão."

                        "Eu sou só um paparazzo. Não adianta eu querer abraçar o mundo..."

                        "Ou adianta?"

                        "Se alguém nessa ilha pudesse me ajudar... quem seria?"

                        "Se a polícia tá corrompida, eu preciso de alguém de fora dela. Alguém que tenha poder, mas esteja fora."

                        "Alguém que tá fora desse rolo das gangues da capital..."

                        "Hmm..."

                        if no2_evento and nona_aceitou:

                            $ xiang_escape = 1

                            "A juíza! Claro! Pensa! Ela me salvou da prisão aquela vez!"

                            "Ela tem poder e não parece que é corrupta... mesmo ela tendo uns gostos estranhos..."

                            "Eu podia falar com ela na Prefeitura e ver se ela pode fazer alguma coisa. Eu preciso explicar pra ela!"

                            "Tá... tenho que ir atá a prefeitura e de lá entrar na área de julgamento. A sala dela fica no segundo andar."

                            "É isso. Quem sabe ela me ajuda... tomara..."

                            "Agora... o que ela vai querer em troca? Putz..."
                        else:




                            "Droga... não vem nada na minha cabeça..."

                            "{b}Para ajudar a Xiang, você precisa ter feito uma série de eventos específicos durante o jogo{/b}"

                            "{b}Você precisa conhecer a Nona e aceitar ajudar ela recebendo a pauta no fliperama no primeiro encontro{/b}"

                            "{b}Você também precisa aceitar fazer a visita no banco com ela quando ela te perguntar{/b}"

                            "{b}Faça esses eventos e fale com a Celeste novamente para continuar{/b}"

                            "{b}Se você já passou por esses eventos, mas fez outras coisas, será preciso reiniciar{/b}"

                            "Melhor eu esquecer isso mesmo... não tem como fazer..."

                        scene black with dissolve

                        jump clube_bdsm
                    else:


                        mc "Oi, [ce]."

                        ce "Acho melhor a gente não falar por um tempo, [mc]."

                        ce "A [nora] já está começando a olhar feio pra mim. Ela não pode suspeitar de nada."

                        ce "Quando você tiver pronto pra acabar com tudo, você me procura, ok?"

                        mc surpreso "C-como é que é?!"

                        ce "Eu tô vendo de quem você tá se aproximando aqui. E quando chegar a hora você vai precisar de mim."

                        mc desconfiado "Certo..."

                        ce "Presta atenção. Quando você quiser fazer algo de verdade aqui no Distrito, me procura."

                        ce "Até lá não fale comigo."

                        mc normal "Ok. Se cuida."

                        ce "Obrigada. Você também."

                        "{b}Descubra mais sobre a Cidade Chinesa para continuar sua história a Celeste{/b}"

                        jump bdsm_clube_bar

                elif celeste_conversa == 3:

                    if xiang_escape < 3:

                        ce "Alguma coisa que me interessa?"

                        mc "Ainda tô querendo ajuda a Xiang a sair daqui."

                        ce "Eu já mandei você parar de me procurar pra falar sobre isso. Que saco."

                        scene distrito_clube geral with Dissolve(1.0)

                        "Merda... será que não adianta continuar? Melhor parar aqui?"

                        "Ou adianta?"

                        "Se alguém nessa ilha pudesse me ajudar... quem seria?"

                        "Se a polícia tá corrompida, eu preciso de alguém de fora dela. Alguém que tenha poder, mas esteja fora."

                        "Alguém que tá fora desse rolo das gangues da capital..."

                        "Hmm..."

                        if no2_evento and nona_aceitou and not xiang_fim:

                            $ xiang_escape = 1

                            "A juíza! Claro! Pensa! Ela me salvou da prisão aquela vez!"

                            "Ela tem poder e não parece que é corrupta... mesmo ela tendo uns gostos estranhos..."

                            "Eu podia falar com ela na Prefeitura e ver se ela pode fazer alguma coisa. Eu preciso explicar pra ela!"

                            "Tá... tenho que ir atá a prefeitura e de lá entrar na área de julgamento. A sala dela fica no segundo andar."

                            "É isso. Quem sabe ela me ajuda... tomara..."

                            "Agora... o que ela vai querer em troca? Putz..."
                        else:


                            "Droga... não vem nada na minha cabeça..."

                            "{b}Para ajudar a Xiang, você precisa ter feito uma série de eventos durante o jogo{/b}"

                            "{b}Você precisa conhecer a Nona e aceitar ajudar ela recebendo a pauta no fliperama no primeiro encontro{/b}"

                            "{b}Você também precisa aceitar fazer a visita no banco com ela quando ela te perguntar{/b}"

                            "{b}Faça esses eventos e fale com a Celeste novamente para continuar{/b}"

                            "{b}Se você já passou por esses eventos, mas fez outras coisas, será preciso reiniciar{/b}"

                            "Melhor eu esquecer isso mesmo... não tem como fazer..."

                        scene black with dissolve

                        jump clube_bdsm
                    else:


                        $ xiang_escape = 4

                        jump xiang_escape2
            else:


                ce "Você."

                mc "Eu?!"

                $ ce_nome = "Celeste"

                ce "Pode me chamar de [ce]."

                call celeste_e1_conversa from _call_celeste_e1_conversa_1

                $ celeste_conheceu = True

                jump clube_bdsm
        "Deixar o Clube de BDSM":


            jump bdsm_sair

label bdsm_sair:

    "Bateu aquele sono agora. Bora pra ilha."

    "..."

    $ xiang_show = True
    $ stifler_falou = True
    $ celeste_falou = True
    $ proibido_salvar = False
    $ show_quick_menu = True

    scene distrito esquina with Dissolve(1.0)

    mc normal "[mon], vou indo nessa."

    show montanha normal with dissolve

    mon "Boa noite, maninho. Valeu pela visita."

    mc "A gente se fala."

    mon "Com certeza."

    mc "Falous!"

    hide montanha with dissolve

    jump call_cidade

label xiang_show_inicio:

    $ renpy.choice_for_skipping()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("xiang_historia","xiang","personagem")

    $ renpy.block_rollback()

    if xiang_evento == 0:

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        "Desde a primeira vez que eu vi essa garota na outra noite eu fiquei muito intrigado."

        "Parece até uma garota muda..."

        if stifler2_xiang and xiang_flor:

            "Ela só falou alguma coisa sobre a tatuagem de flor dela. E mais nada."

        mc zerado "Se eu não me engano ela disse a palavra 'pronta' também..."

        show xiang andando with moveinbottom

        mc surpreso "[i]!"

        mc envergonhado "E-eu tava falando alto? Eu..."

        i "..."

        mc normal "..."

        i "..."

        mc surpreso "Desculpa! Eu tô na sua frente!"

        hide xiang with dissolve

        "Não é por nada não, mas se essa mina não fosse gata pra caramba ela não ia ter chance de seduzir ninguém desse jeito."

        i "Pronta..."

        "Ela falou de novo!"

        mc zerado "A mesma palavra..."

        scene xiang show1_1 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        scene xiang show1_2 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        scene xiang show1_3 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        "..."

        if stifler2_xiang:

            "Eu tenho a impressão que ela fez os mesmos movimentos do show anterior..."

            "Tipo... EXATAMENTE os mesmos. Não sei se isso é chato ou é sensacional."
        else:


            "Uou! Eu devia ter visto isso antes! Simplesmente incrível!"

        "Ops... acho que ela já tá acabando."

        "Não sei como puxar conversa com ela."

        i "..."

        mc envergonhado "Ops, desculpa ficar no caminho."

        scene xiang mc_olhando with Dissolve(3.0)

        pause

        if xiang_flor:

            mc "[i]... É..."

            mc "Essa sua tatuagem..."

            i "Flor..."

            "Ela falou de novo!"

            mc "Isso! Ela... é a {b}flor de lótus{/b}, certo?"

            i "Lótus..."

            mc "Ah, legal! Então eu acertei."

            i "Venha mais vezes... tarado..."

            mc "Tarado?!"

            mc "Que stripper chama seu cliente de tarado?"

            if xiangu_flor:

                "CALMA! PERA! QUÊ?!"

                "Eu acho que essa é a mesma tatuagem que tem nas costas da [xu]!"

                "Impossível! Que cagada! Que massa! Não acredito!"

                "Eu tenho quase certeza que é exatamente a mesma tattoo..."

                "Preciso falar com essa [i] de novo. Preciso saber a relação entre as duas."

                "Quem diria que a resposta seria uma stripper..."

                mc zerado "Parece até coisa de videogame..."

            python:
                if renpy.android:
                    xiang_evento_db = PythonSDLActivity.pegaXiang()
                    
                    if xiang_evento == xiang_evento_db:
                        PythonSDLActivity.addXiang()

                xiang_evento += 1
                xiang_errou = False
        else:


            $ xiang_errou = True

            "Essa mina é gata demais."

            menu:
                "Focar na tatuagem das costas.":


                    $ xiang_flor = True

                    "Essa tatuagem..."

                    show xiang_close costas_acima with Dissolve(1.0)

                    pause

                    "Uma flor... O que será que ela significa?"

                    "Preciso voltar aqui e tentar descobrir mais sobre ela."
                "Focar mais pra baixo...":


                    mc safado "..."

                    show xiang_close costas_close with Dissolve(1.0)

                    pause

                    "Meu Deus! Eu tenho que voltar aqui com certeza!"

                    "Ela pode cobrar quanto ela quiser, se eu tiver tá valendo."

                    "Mas eu devia olhar para aquela flor da próxima vez."

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        "Foi embora..."

        "Essa garota parece de outro mundo."

        "Pensando bem... pelo nome [i]... ela deve ser chinesa. O que uma chinesa tá fazendo aqui trabalhando no Distrito?"

        "Preciso ver ela de novo. Meu sentido paparazzo tá me dizendo que tem caroço nesse angu."

        jump bdsm_sair

    elif xiang_evento == 1:

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        "Da outra vez ela disse para eu voltar aqui."

        mc zerado "E me chamou de tarado..."

        "Bom... um cara em um clube de sadomasoquismo pagando para ver uma mina abrir as pernas pra ele... não sei se ela tá mentindo..."

        "Mas e daí que sou tarado?!"

        mc serio "Enquanto eu não tiver prejudicando ninguém, o que que tem um pouco de taradisse, hein?!"

        i "..."

        mc surpreso "[i]!"

        show xiang andando with dissolve

        i "Tarado..."

        mc desconfiado "De novo?"

        i "..."

        "Pelo menos ela falou alguma coisa."

        mc envergonhado "Eu tô na sua frente de novo, né?"

        i "..."

        mc "Pode passar e se arrumar na jaula..."

        show xiang costas with dissolve

        i "Não..."

        mc desconfiado "Como?"

        i "Hoje vou deitar no banco."

        i "Pode olhar pra mim."

        hide xiang with dissolve

        "Tudo isso aqui é pra eu olhar pra ela. Como assim 'posso' olhar?"

        "Tenho cada vez mais certeza que essa mina é doida."

        "Deixa eu sentar."

        scene xiang show2_fundo with Dissolve(1.0)

        "Acho que ela vai deitar neste banco."

        mc safado "Tô muito ansioso..."

        i "Pronta..."

        mc safado "Lá vem ela."

        scene xiang show2_1 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        scene xiang show2_2 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        scene xiang show2_3 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        i "..."

        mc tarado "Uou... isso foi incrível, [i]."

        i "..."

        i "Gostou?"

        "Ela realmente quer saber minha opinião?"

        menu:
            "Claro que gostei. Você é muito sexy.":


                mc safado "Eu achei tudo incrível. Você é muito sexy."

                i "..."

                mc normal "Mas, se me permite uma dica..."

                i "..."
            "Eu sinto que tá faltando alguma coisa...":


                mc desculpa "Eu achei que você foi incrível nos movimentos, mas acho que tá faltando alguma coisa..."

                i "..."

        mc desculpa "Talvez você poderia se abrir um pouco mais."

        i "Falar mais?"

        i "Hmmm..."

        mc "..."

        i "Vou sair."

        mc envergonhado "Ah! Ok..."

        scene xiang mc_olhando with Dissolve(3.0)

        pause

        "Não tenho mais dúvida de que tem algo de errado com essa garota."

        "Trabalhar em um lugar como este pode mexer um pouco com você, mas a esse ponto?"

        "Eu sinto que tem algo a mais nessa história. Eu preciso desvendar o que tá havendo com ela."

        mc zerado "Mesmo que eu acabe sem um tostão no bolso..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 2:

        $ renpy.block_rollback()

        scene xiang show2_fundo with Dissolve(2.0)

        "..."

        "Da outra vez eu disse que ela precisava se abrir mais e eu tive a impressão que ela pensou no que eu falei."

        "Quem sabe ela não começa a conversar comigo agora..."

        mc zerado "Até parece..."

        i "Tarado..."

        scene distrito_clube visao with Dissolve(1.0)

        show xiang ignorando with dissolve

        pause

        mc desconfiado "Ei! Ainda me chamando assim?"

        i "Você gasta dinheiro pra ver uma mulher abrindo as pernas."

        mc zerado "Às vezes a verdade dói, sabia?"

        show xiang costas with dissolve

        i "..."

        mc zerado "Não me critique e depois me ignore..."

        i "Vem. Vou abrir as pernas pra você."

        mc surpreso "Qu-quê?!"

        hide xiang with dissolve

        "Que susto... na verdade ela só vai continuar posando como sempre, mas ela falando desse jeito me assustou."

        scene xiang show2_fundo with Dissolve(1.0)

        "..."

        i "Vou começar."

        mc safado "Fique à vontade..."

        scene xiang show2_1 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        i "Eu adoro abrir as pernas assim..."

        mc safado "..."

        scene xiang show2_2 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        i "Olha como a minha bunda fica gostosa desse jeito..."

        mc tarado "Com certeza..."

        scene xiang show2_3 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        i "Você quer me beijar?"

        mc surpreso "E-e-eu?!"

        i "Posso chegar mais perto?"

        mc "Co-com certeza."

        i "..."

        scene xiang show2_4 with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        pause

        i "Olha bem pro meu decote..."

        i "Consegue ver meus peitos?"

        mc safado "Consigo..."

        i "Hmmm..."

        "Espera... será que ela tá assim por que eu disse pra ela falar mais?"

        mc desculpa "[i]... Você tá falando por que eu disse isso da outra vez?"

        i "..."

        mc envergonhado "Você não precisa falar se não quiser."

        i "..."

        mc normal "Você é linda. E tenho certeza que nenhum homem vai deixar de te ver só por causa disso."

        i "..."

        i "Vou embora."

        mc desconfiado "T-tá certo."

        scene xiang mc_olhando with Dissolve(3.0)

        pause

        "Não sei como explicar, mas ver ela se esforçando assim... foi fofo..."

        i "Obrigada."

        mc "Ah?"

        mc "De boa. Não precisa agradecer."

        i "Qual é seu nome?"

        mc "Eu me chamo [mc]... [mcc]."

        i "Eu sou {b}[i], A Flor de Lótus{/b}."

        mc "Flor de lótus?"

        i "Eu tenho outros movimentos pra você ver."

        i "Venha mais vezes, [mc]."

        mc "Pode deixar."

        i "Tchau."

        "[i], A Flor de Lótus. Finalmente ela tá falando comigo."

        "A garota mais misteriosa que eu vi na minha vida..."

        if xeena_encontro:

            "Se bem que aquela mina encima do poste no condomínio da [j] também foi bem estranha."

            "O mundo tem cada coisa..."

        if xiangu_evento > 0:

            "E também não dá pra esquecer da [xu]. Tô achando que na verdade ELA é a mais estranha..."

            "E pensar que eu ainda não consegui nada sobre a tatuagem. O que eu tô fazendo?!"

            "Não posso deixar de perguntar isso pra [i] da próxima vez."

        "Tô ansioso pra ver ela de novo."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()







        jump bdsm_sair

    elif xiang_evento == 3:

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        "Tô me sentindo nervoso agora que vou ver ela."

        "[i] e [xu]... até o nome é parecido."

        mc zerado "O problema é que ela praticamente nem fala..."

        "Opa! Aí vem ela."

        show xiang andando with dissolve

        i "..."

        mc normal "Oi, [i]. Tudo bem?"

        i "..."

        mc envergonhado "Quer passar?"

        i "..."

        show xiang costas with dissolve

        i "Hoje vou posar diferente pra você."

        i "Vem."

        mc "Ok."

        "Cristo..."

        i "Senta."

        scene xiang show3_fundo with Dissolve(1.0)

        i "Vou começar."

        mc normal "Ok."

        scene xiang show3_1 with Dissolve(1.0)

        pause

        i "..."

        i "Tava com saudades de ver você."

        mc charmoso "Verdade?"

        i "Sim. Eu gosto de posar pra você."

        i "Eu gosto quando você me vê."

        i "Quer ver minha bunda?"

        menu:
            "Com certeza.":


                mc safado "Com certeza."

                i "Que bom."
            "Só posa. Não precisa falar nada.":


                mc desculpa "Pode só continuar posando. Não precisa falar."

                i "Obrigada. Mas eu gosto."

                mc "..."
            "...":


                mc desculpa "..."

        scene xiang show3_2 with Dissolve(1.0)

        pause

        "Que traseira..."

        i "Tá vendo minha flor?"

        "Essa frase tem mais de um significado..."

        mc normal "Sim. A flor de lótus."

        i "Sim... a flor de lótus é um símbolo."

        mc surpreso "É sobre isso que quero falar com você!"

        i "Não. Agora é hora do show particular. Só vê."

        mc envergonhado "Ok..."

        "Acho que vou ter que ir devagar com ela."

        i "Agora olha de mais perto..."

        scene xiang show3_3 with Dissolve(1.0)

        pause

        menu:
            "Simplesmente deliciosa.":


                mc tarado "Deliciosa você."

                i "Você gosta, né?"

                mc "Claro."

                i "Quer pegar também?"

                mc safado "Sim!"

                i "Não pode..."

                "Afe!"

                mc zerado "..."

                mc envergonhado "Você tá aprendendo como provocar..."
            "...":


                mc envergonhado "..."

        i "..."

        i "Pode olhar bem..."

        window hide

        pause

        i "Pronto."

        scene xiang show3_1 with Dissolve(1.0)

        i "Gostou do show?"

        mc normal "Sim. Eu sinto que você tá se soltando mais."

        i "..."

        i "Agora eu vou embora."

        mc envergonhado "Tá."

        "Ela fala de uma forma tão estranha que chega a ser engraçada..."

        i "Tchau."

        scene xiang show3_fundo with Dissolve(1.0)

        "Ela já foi. E eu não consegui informação alguma sobre a tatuagem."

        "Mas o [chi] disse pra eu não desistir. E eu não vou. Ela vai soltar o que eu quero, ou não me chamo [mcc]."

        "..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 4:

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        mc concentrando "Não posso voltar de mãos abanando."

        "..."

        show xiang andando with dissolve

        i "..."

        mc normal "Boa noite, [i]."

        i "..."

        mc envergonhado "Hoje queria falar com você antes do show."

        i "..."

        mc "Não vou deixar você passar."

        i "?"

        mc normal "Tô falando sério."

        show xiang ignorando with dissolve

        i "Tarado paga pelo show, mas não quer show... Burro..."

        mc zerado "Ei..."

        i "..."

        mc desculpa "Eu quero saber sobre sua tatuagem."

        i "?"

        mc desculpa "Quando você fez ela? E qual é o significado dela? O que ela quer dizer?"

        i "..."

        i "Não vou responder."

        mc preocupado "Que?! Por que?!"

        i "Você é meu cliente, não meu amigo."

        mc angustiado "Mas-"

        i "Quer dança ou não?"

        "Nossa. Essa doeu..."

        mc concentrando "Quero."

        i "Com licença."

        mc desculpa "Claro..."

        hide xiang with dissolve

        "Puxa... Ela não precisava ter falado assim comigo."

        "..."

        scene xiang show3_fundo with Dissolve(1.0)

        i "Olha bem."

        scene xiang show3_2 with Dissolve(1.0)

        pause

        mc desculpa "..."

        i "Agora só pra você..."

        scene xiang show3_3 with Dissolve(1.0)

        pause

        i "Gostou?"

        menu:
            "...":


                mc serio "..."
            "Gostei...":


                mc desculpa "Gostei..."

        scene xiang show3_1 with Dissolve(1.0)

        i "O que foi?"

        mc desculpa "..."

        i "Não abri as pernas suficientes pra você?"

        i "E assim?"

        scene xiang show3_4 with Dissolve(1.0)

        pause

        i "Dá pra me ver todinha..."

        mc bravo "Não é isso, [i]!"

        i "?"

        scene xiang show3_1 with Dissolve(1.0)

        i "..."

        menu:
            "Não é nada. Esquece...":


                mc desculpa "Não é nada. Só esquece."

                i "..."
            "Você me deixou mal hoje.":


                mc bravo "Você me deixou mal hoje do jeito que você falou."

                mc "Eu sei que a gente não é amigos, mas poxa! Precisava falar assim?"

                i "..."

        mc desculpa "Eu queria saber mais sobre você e sobre a Cidade Chinesa. Só isso."

        i "..."

        i "Terminei. Vou indo nessa."

        mc desculpa "Ok..."

        scene xiang show3_fundo with Dissolve(1.0)

        "Que merda..."

        "Acho que eu não vou conseguir nada com ela."

        "Nem sei se vou voltar mais aqui. Perdeu toda a graça..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 5:

        $ renpy.block_rollback()

        "..."

        scene xiang show3_fundo with Dissolve(1.0)

        "Nem sei o que vim fazer aqui. A [i] não fala comigo. E não consigo mais curtir as apresentações dela."

        "..."

        i "Oi."

        scene xiang show3_1 with Dissolve(1.0)

        mc desculpa "Oi."

        i "Vou fazer uma apresentação incrível hoje. Pode começar olhando pro meu maior segredo."

        scene xiang show3_4 with Dissolve(1.0)

        pause

        "De novo isso?"

        mc desculpa "..."

        i "..."

        scene xiang show3_1 with Dissolve(1.0)

        i "Você tá estranho."

        mc desculpa "Achei que talvez você pudesse me ajudar com uma coisa. Mas parece que eu cheguei ao fim da linha."

        i "..."

        mc "Na verdade nem foi culpa sua. Acho que eu que coloquei expectativa demais nisso tudo."

        mc "Você tá certa. A gente não é amigos. Você não tem porque contar qualquer coisa pra um cara que paga pra ver suas partes íntimas."

        i "[mc]..."

        mc desconfiado "Você sabe meu nome?"

        scene xiang show3_fundo with Dissolve(1.0)

        i "Senta aqui."

        mc "Ok."

        scene xiang show2_fundo with Dissolve(1.0)

        mc desculpa "Que foi?"

        scene xiang show2_4 with Dissolve(1.0)

        i "Eu gosto de você."

        mc desconfiado "?"

        i "Você é tarado, mas também não é."

        mc zerado "..."

        i "Você é diferente dos outros."

        i "Os outros só querem ver e pegar em mim. Mas você gosta da minha flor e quer saber sobre ela."

        i "Isso nunca aconteceu comigo antes."

        mc desculpa "[i]..."

        menu:
            "Sentar ao lado dela":


                mc normal "Deixa eu sentar do seu lado."

                scene xiang mc_sentados with Dissolve(1.0)

                pause
            "Continuar onde está":


                "Melhor não abusar, justo agora que ela tá falando comigo."

                "..."

        i "Eu não sei o que achar disso. Por isso eu falei aquilo da outra vez. Me desculpa."

        "Não acredito que eu fiz isso."

        "Essa garota trabalha todas as noites se exibindo para estranhos, sendo provavelmente abusada verbalmente por idiotas..."

        "Passa mó barra nessa vida..."

        "Só porque essa mina foi um pouco grossa comigo... eu... que moro numa ilha paradisíaca... fico todo doído."

        "Eu sou um babaca."

        mc "Eu agradeço, mas não precisa pedir desculpas, [i]. Eu que fui idiota e infantil."

        mc "Você não precisa falar nada pra mim que não quiser. Sua vida já é difícil demais sem um idiota te enchendo."

        i "..."

        i "Você é engraçado, [mc]."

        mc "?"

        i "Parece que você realmente se preocupa comigo."

        mc "Mas eu me preocupo."

        i "Por quê? A gente nem se conhece. Você só paga pra me ver."

        mc "Não sei. Uma jovem igual você, vivendo uma coisa dessas... sei lá."

        i "..."

        mc "..."

        i "Você quer ser meu amigo?"

        mc "Claro."

        i "Então tá. Agora a gente é amigos. Só que eu tenho que ir. Não posso ficar tempo demais."

        mc "Ok..."

        i "Vem aqui."

        mc "?"

        scene xiang mc_olhando with Dissolve(1.0)

        i "Olha..."

        i "A Cidade Chinesa tem um segredo muito maior do que você imagina..."

        i "A lenda da [xu] é falsa."

        mc "É isso que eu tô tentando provar, mas todas as pessoas que eu converso falam o contrário."

        mc "Como você sabe que ela realmente não é a da lenda? Tem pessoas que dizem que viram ela com a mesma aparência depois de décadas!"

        i "Eu não tenho provas. Mas eu sei que é mentira. Não tem jeito. Você vai ter que tirar isso dela."

        mc "Dela?"

        i "Da própria garota que se faz de [xu]. Se você não tem provas, ela é a única que vai convencer os outros da verdade."

        mc "Mas ela mesm-"

        i "Ela não é uma garota ruim. Ela só não sabe."

        mc "Como? Você conhece ela? Como assim ela não sabe?"

        i "Quando você conseguir algo novo sobre aquela moça, venha me contar. Talvez eu possa ajudar você mais."

        mc "Ok. Obrigado, [i]."

        i "Até mais, amigo."

        mc "Até."

        scene distrito_clube pub with Dissolve(1.0)

        show mc bdsm_angulo_sul with dissolve

        "..."

        "Quem diria que a [i] sabia falar desse jeito?"

        "Então ela acha que tudo não passa de uma grande mentira. Isso é óbvio. É impossível que realmente existam imortais no mundo."

        "Eu passei tempo demais com aqueles doidos. Começou a me afetar."

        "Então quer dizer que eu vou ter que fazer a própria fake [xu] me contar a verdade. E depois convencer ela a falar para todos."

        "Com certeza não vai ser uma tarefa fácil..."

        "Preciso continuar tomando banho na [li] e trabalhando com o [chi]."

        "Todas as informações que eu conseguir vão ser úteis."

        "Mas o principal agora é {b}falar com a [xu] no portal de novo{/b}."

        "Ah! E qual será o grande mistério da Cidade Chinesa que a [i] falou?"

        "Pensar em todas essas coisas tá me deixando com dor de cabeça."

        "AH! Eu também não quer abandonar a [i]. Ela parece tão jovem e precisa de ajuda aqui."

        "Se eu conseguir aliviar um pouco o dia dela conversando com ela, já fico feliz."

        "Além de que ela é super gatinha e quem sabe... talvez a gente até pudesse ser algo mais."

        mc "Mas se eu escolher isso... eu vou ter que vencer ciúme..."

        "Não vejo a hora de ver ela de novo!"

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 6:

        $ renpy.block_rollback()

        scene distrito_clube visao with Dissolve(1.0)

        "Hoje eu vou esquecer a Cidade Chinesa e focar na [i]. Ela me ajudou bastante e também tá sofrendo aqui."

        "A [nora] disse que ela não tá aceitando outros shows particulares. Não sei porque, mas por um lado eu fico meio feliz."

        "Só que óbvio que isso não vai ser bom pra ela. A véia não vai aceitar isso por muito tempo."

        i "Olá, amigo."

        scene xiang_pe2 with Dissolve(1.0)

        pause

        mc normal "Oi, [i]."

        i "Pronto para o show?"

        menu:
            "Tô louco pra ver seu show.":


                mc safado "Eu tô doido pra ver seu show. Tava muito ansioso pra ver você."

                i "Que bom. Eu quero me mostrar pra você também."
            "Você prefere conversar?":


                mc charmoso "Se você preferir, a gente pode conversar nesse tempo."

                i "Não. Primeiro o show e depois conversa."

                mc envergonhado "Ok..."

        i "Hoje é você que vai me falar o que você quer ver."

        mc desconfiado "Eu?"

        i "Sim. Agora o show é especial. Você manda na [i]."

        mc envergonhado "E o que eu posso escolher?"

        i "Pode escolher se a [i] vai pra gaiola, se a [i] senta ou se a [i] deita."

        mc "E-entendi..."

        i "Depois, você vai poder pegar na [i] também. Pode pegar no meu corpo. Meu corpo é seu, amigo."

        mc surpreso "M-meu?! I-isso parece demais, [i]!"

        i "Você pode tudo a partir de hoje... a [i] é sua."

        "O que essa garota quer dizer com isso? Será que ela sabe o que tá falando?"

        i "O que você quer da [i] hoje?"

        "Pra quem não falava nada, até que ela tá bem matraca..."

        "Bom, eu gastei minha grana e ela parece empolgada. Acho que eu vou aproveitar."

        mc safado "Então vamo logo que eu quero ver você bem de pertinho hoje."

        i "Assim mesmo. Me olha de pertinho, amigo..."

        $ area_xiang = "agachada"
        $ xiang_pose = 1

        call xiang_escolhe_pose from _call_xiang_escolhe_pose

        i "Amigo... posso fazer uma coisa?"

        mc desconfiado "Hm? Pod-"

        scene xiang_evento4 with hpunch

        pause

        mc "X-xiang!"

        i "Eu quero chegar mais perto de você. Posso?"

        mc "Pode... mas..."

        i "Não tem problema. Pode pegar na [i]... agora a gente é amigos. Amigos são assim, não são?"

        mc "Calma... Não é exatamente assim..."

        i "Eu ouvi que amigos confiam um nos outros e se abraçam e dividem as coisas..."

        i "Por isso eu quero que você pegue na [i] e me abrace e faça tudo o que você quiser comigo."

        mc "Eu... eu não sei."

        i "Você não é amigo da [i]?"

        "Essa garota... será que ela tá fazendo isso de propósito? É impossível alguém ser tão sem noção."

        mc "Sou. Mas não é assim que funciona, [i]."

        i "Então explica. Fala como que funciona."

        scene xiang_evento5 with Dissolve(1.0)

        pause

        mc "Ok... eu vou explicar."

        i "Posso ficar aqui deitada?"

        mc "P-pode..."

        i "Então fala."

        mc "Amigos são pessoas que se gostam e se ajudam. Ser um amigo é querer que a outra pessoa seja feliz e apoiar ela no que ela precisar."

        i "Mas eu posso te ajudar?"

        mc "Claro que pode. Mas acho que não agora."

        i "..."

        mc "Agora é você quem precisa de ajuda, [i]. Você tá presa aqui? Você gosta de trabalhar aqui?"

        i "A [i]..."

        mc "A [nora] disse que você não faz show particular pra ninguém. Por que você não faz mais?"

        i "Por que você tá me perguntando isso? Você não entende?"

        mc "Eu quero entender. Por isso tô perguntando."

        i "Você é burro..."

        mc "Ei... me fala o que tá acontecendo, [i]."

        i "Não! Você não entende? Você é burro? Você é meu amigo!"

        mc "Ok, calma. Esquece isso. Por que você não faz igual eu? Me chama pelo meu nome. Meu nome é [mc]."

        i "Eu sei..."

        mc "Por que você não me chama assim então?"

        scene xiang_evento6 with Dissolve(1.0)

        pause

        i "T-tá... eu chamo... [mc]..."

        mc "Isso. Isso é coisa de amigo. Chamar pelo nome, normal..."

        i "Tá legal. É nossa coisa de amigo, [mc]..."

        mc "Isso já é um começo. Agora, outra coisa é que você não precisa ficar em cima de mim assim."

        i "Mas eu gosto... eu quero encostar em você. Você não gosta?"

        menu:
            "Isso não é apropriado.":


                mc "[i], não é essa a questão. Não é se eu gosto ou não. É que não é apropriado."

                mc "Se você quer ter uma relação de amigo, a gente precisa conversar normal."

                i "Não... por favor, [mc]. Por favor, deixa eu encostar em você."
            "Eu gosto, claro.":


                mc "Claro eu gosto. Eu adoro na verdade. Você me deixa louco."

                i "Então... eu fico feliz..."

        mc "Mas você entende? Isso tem uma conotação sexual, ainda mais aqui no clube."

        i "Mas o clube é pra isso. Todo mundo pega nas garotas."

        mc "Por isso mesmo. Os clientes não são amigos."

        i "Mas você é."

        mc "Mas é por iss... tudo bem. Se você quer isso, tudo bem. Mas só aqui no clube."

        mc "Se algum dia a gente se ver fora daqui, a gente não vai fazer isso."

        i "Nem abraçar a [i] você vai fazer?"

        mc "Ok. Um abraço. Bem rápido."

        i "Tá bom."

        mc "E eu também quero poder recusar ver seu show se eu não me sentir à vontade."

        i "Quê?!"

        mc "Talvez eu queira só falar com você."

        i "Tá bom... então tá bom de conversa por hoje."

        mc "[i]! Espera!"

        scene black with Dissolve(1.0)

        scene xiang mc_olhando with Dissolve(1.0)

        i "Eu vou esperar você, [mc]. Não me deixe sozinha."

        mc "O-ok... eu vou voltar, [i]."

        "O que acontece com essa garota? O que acontece com essa cidade?"

        scene black with Dissolve(1.0)

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 7:

        $ renpy.block_rollback()

        nora "Acho que ela viu a gente conversando e tá te esperando ali."

        mc "Vou ver."

        scene xiang_pe1 with Dissolve(1.0)

        pause

        "Ela tá ali mesmo. Tá parecendo bem ansiosa pra me ver..."

        "A [i] sempre pareceu uma garota muito firme. Aquele jeito misterioso dela de nunca falar nada me passou uma visão errada."

        "Agora que ela tá se abrindo, dá pra ver que ela é bem estranha... com todo o respeito!"

        "Parece que ela não cresceu igual as outras pessoas. É a primeira coisa que me vem na cabeça."

        "Como uma adulta não sabe direito como funciona a... 'amizade'? Isso é muito coisa de filme."

        "Eu preciso tomar muito cuidado com ela. Não quero piorar a situação. Agora deixa eu ir antes que ela estranhe."

        scene xiang_pe2 with Dissolve(1.0)

        mc normal "Oi, [i]."

        i "Oi, [mc]..."

        mc "Aprendeu me chamar pelo nome?"

        i "Sim. Eu tava ansiosa pra ver você."

        mc charmoso "Eu também."

        i "Você disse que... você vai querer ver meu show?"

        menu:
            "Sim. Com certeza.":


                mc safado "Claro que eu vou querer. Perder a chance de ver minha garota posando pra mim?"

                i "Ai... eu também quero mostrar tudo pra você. O que eu faço hoje?"

                call xiang_escolhe_pose from _call_xiang_escolhe_pose_1

                i "Agora... a outra parte..."

                mc desconfiado "Hm?"
            "Hoje quero só conversar.":


                mc normal "Hoje eu vim só pra conversar com você."

                i "Verdade? Você não quer ver a [i]?"

                mc envergonhado "Eu acho melhor a gente só conversar."

                i "Tudo bem... mas então a [i] quer a outra parte."

                mc "E o que seria?"

        i "Eu quero pegar em você, [mc]."

        mc envergonhado "[i]..."

        i "Você disse que a [i] ia poder..."

        mc "Ok..."

        i "Senta no chão. [i] vai sentar no seu colo."

        mc surpreso "C-como?!"

        i "Vai, [mc]."

        "Meu Deus..."

        mc envergonhado "Ok..."

        scene xiang_evento1 with Dissolve(1.0)

        pause

        i "É gostoso quando a [i] senta assim em você? Os clientes sempre gostaram."

        mc "Eu gosto, sim. Mas você tem certeza?"

        i "Eu não quero mais pegar em ninguém, [mc]. Só em você. E eu quero que você pegue em mim também."

        mc "Então é isso? É por isso que você não quer ver outros clientes?"

        i "Sim... agora que a gente é amigo, a [i] não pode mais se envolver com outros homens."

        mc "Entendi... só pra ter certeza... você tá falando sério."

        i "Como assim? Por que você não liga pro que eu falo?"

        mc "Tá. Entendi. Olha, [i]... eu não sei quem falou isso pra você... mas essa pessoa não foi sincera."

        i "Ela mentiu?"

        mc "Sim... ou talvez ela só não soubesse também."

        i "Ela... não sabia? Então o que ela me ensinou é mentira?"

        mc "Calma. Eu não sei o que ela te ensinou. Mas o que eu posso te ensinar é que amizade não funciona desse jeito."

        mc "A gente pode ter um amigo ou uma amiga e se relacionar com outras pessoas."

        i "Então você não vai querer deixar de ser meu amigo se eu ver os clientes?"

        "Por um lado é bem legal saber que eu tenho uma garota de programa exclusiva... não dá pra negar."

        "Mas eu não posso deixar ela se ferrar com a [nora] por causa disso."

        scene xiang_evento2 with Dissolve(1.0)

        pause

        mc "Claro que não. Eu vou continuar sendo seu amigo mesmo assim."

        i "Mesmo sabendo que os homens vão pegar em mim? Que eles vão olhar pra [i] e pensar em coisas safadas?"

        mc "Mesmo assim."

        i "Então... será que a gente não é amigo?"

        mc "Já falei que isso não tem nada a ver com ser amigo."

        mc "Ser amigo é ajudar outra pessoa e ter alguém quando a gente tá com problemas. É alguém que a gente gosta e confia."

        i "Então é isso..."

        mc "Sim. É isso aí. E até melhor você trabalhar, assim você deixa a [nora] contente e você ficando bem me deixa feliz. Tá vendo?"

        i "Acho que eu entendi..."

        mc "Aliás, [i]... você conversa com as outras garotas aqui?"

        i "Não."

        mc "E com a [nora]?"

        i "Um pouco. Mas só o que eu preciso."

        mc "E você vive aqui no clube mesmo?"

        i "..."

        mc "Que foi?"

        scene xiang_evento3 with Dissolve(1.0)

        pause

        i "[mc]... Eu não sei se eu posso te falar essas coisas..."

        mc "Por quê?"

        i "A [nora] não deixa a gente falar nada sobre o que acontece com quem trabalha aqui."

        menu:
            "Amigos contam as coisas uns pros outros.":


                mc "Mas os amigos contam as coisas uns pros outros. A gente confia um no outro."

                i "E se ela ficar brava?"

                mc "Ela não precisa saber. Eu prometo que não vou contar."

                i "Tudo bem. Se os amigos fazem assim... a [i] e as garotas moram todas em uma casa aqui perto."

                mc "E vocês podem sair?"

                i "N-não! A gente só vem da casa pra cá trabalhar e volta."

                mc "Vocês então não podem sair? Ir fazer uma compra ou pra outra parte da cidade?"

                i "Não."
            "Se você prefere, não precisa falar.":


                mc "Se você acha que vai dar problema, não precisa falar, ok?"

                i "Tudo bem... a [nora] não deixa a gente falar sobre isso. Ela fica muito brava quando a gente não obedece."

                mc "A situação é complicada assim, [i]?"

                i "Ela odeia quando a gente não faz o que ela manda. Ela diz que é nossa dona."

                mc "Entendi..."

        "Olha a situação dessas garotas... eu sabia que tinha alguma coisa de errado aqui."

        "A [i] não conversa com as garotas, vive seguindo as ordens da [nora], não tem contato com outras pessoas..."

        "Isso não pode ficar assim."

        mc "[i], isso não tá certo. Isso não é vida."

        i "Mas eu sempre vivi assim."

        mc "Isso é o pior. Mas a gente vai dar um jeito."

        i "É perigoso, [mc]. A [nora] odeia quando alguém tenta mudar alguma coisa aqui."

        mc "Eu sei. Mas é pra isso que os amigos servem. Eu vou dar um jeito, [i]."

        i "Tá..."

        mc "Acho que deu o tempo, né?"

        i "Sim. Mas eu posso ficar assim mais um tempinho? Eu gosto de olhar pra você."

        mc "Tá bom."

        window hide

        pause

        scene black with Dissolve(1.0)

        mc "Tchau, [i]."

        i "Volta logo."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 8:

        $ renpy.block_rollback()

        "Ainda não tô acreditando no que a [i] falou na outra noite. A [nora] deve ser um monstro."

        nora "O que foi, jovem?"

        mc "Nada. Eu vou lá esperar ela."

        nora "Fique à vontade. Nosso clube é feito para você."

        mc "..."

        scene distrito_clube visao with Dissolve(1.0)

        "Eu quero tirar a [i] daqui. Ela não merece passar por isso."

        "Ela ainda é jovem e nem sabe como é o mundo lá fora. Fico pensando como ela acabou nessa vida."

        "A tatuagem de lótus, a história da [xu]... eu só consigo pensar que a [i] veio da Cidade Chinesa."

        "Agora, o que ela tem a ver com a história da mulher imortal e todo aquele rolo da [s], [fen] e os outros eu não sei."

        i "Oi."

        scene xiang_pe3 with Dissolve(1.0)

        pause

        i "[mc]? Boa noite."

        "O que eu sei é que eu quero que ela tenha uma vida boa. Uma vida longe de tudo isso que ela viveu."

        mc normal "Boa noite, amiga."

        i "Você chamou a [i] de amiga."

        mc "Sim. Porque a gente é amigos, ué."

        i "Você ainda não tinha chamado a [i] assim. Eu fiquei feliz, [mc]."

        mc normal "Desculpa. Você sempre foi minha amiga."

        i "Que bom. Agora olha aqui."

        scene xiang_pe4 with Dissolve(1.0)

        pause

        mc surpreso "Q-que foi?!"

        i "Pronto pro seu show? Hoje eu quero deixar você ainda mais excitado, [mc]."

        menu:
            "Não vejo a hora.":


                mc safado "Não vejo a hora de você posar pra mim."

                i "Então vamos começar logo. O que você quer fazer com a [i] hoje?"

                call xiang_escolhe_pose from _call_xiang_escolhe_pose_2

                i "Eu gostei de ver o jeito que você me olhava."

                mc safado "..."

                i "Agora eu quero conversar e abraçar você, [mc]."

                mc charmoso "Claro."
            "Prefiro ficar na conversa.":


                mc envergonhado "..."

                mc "Você realmente aprendeu a ser sexy, [i]. Mas eu realmente prefiro ficar na conversa."

                i "Tem certeza? Eu gosto quando você me vê."

                mc normal "Tenho. E eu gosto de conversar com você."

                i "Eu também gosto. Mas eu quero sentar no seu colo enquanto a gente conversa."

                mc envergonhado "Tem certeza?"

                i "Tenho."

        i "Vem. Senta aqui."

        scene xiang_evento7 with Dissolve(1.0)

        pause

        i "Eu voltei a ver os clientes. Tudo bem mesmo pra você?"

        mc "Tudo. Eu falei que tá tudo legal."

        i "[mc]... se amigos podem sair com os outros... o que é um 'casal'?"

        mc "Um casal?"

        i "Eu escuto as garotas falando que elas queriam encontrar um homem ou uma mulher que elas amem pra ser um casal."

        mc "AAH!"

        i "!"

        mc "Acho que agora eu entendi! Você não tá falando de 'amizade'! Você tá falando de 'namoro'!"

        i "Namoro..."

        mc "Acho que é isso pelo menos. Quando duas pessoas que se conhecem querem levar a relação pra algo mais íntimo, a gente chama de namoro."

        i "Algo íntimo é o que eu faço com os clientes, certo? A gente é namorado?"

        mc "Não... não é isso, [i]."

        "Eu ainda não acredito como essa mina pode não saber coisas tão básicas. Não saber a diferença entre amizade e namoro?"

        "Que tipo de educação essa garota recebeu? Em que tipo de lugar ela cresceu?"

        mc "Olha... você nunca conversou isso com suas amigas?"

        scene xiang_evento8 with Dissolve(1.0)

        pause

        i "[i] nunca teve uma amiga. Você é minha primeira amiga."

        mc "Entendi... e sua mãe?"

        i "Eu... não lembro da minha mãe. Acho que eu nunca conversei com ela."

        mc "Nossa, [i]... desculpa... eu nem sei o que falar."

        i "O que aconteceu?"

        mc "Nada... é que eu nunca achei que ia ter que explicar isso pra alguém com sua idade."

        i "Eu gosto quando você me ensina as coisas, [mc]. Você é a pessoa mais inteligente que eu já conheci."

        i "As garotas não falam sobre essas coisas e os clientes quase não falam nada, só como a [i] é gostosa e eles queriam comer."

        mc "Sei... Tudo bem, [i]. Tá sendo uma novidade pra mim também, mas é legal."

        mc "Eu quero que você aprenda o que você precisa e se cuide mais. Eu quero que sua vida melhore."

        i "Mas e o namoro? É sobre isso que eu queria saber, [mc]..."

        mc "Ah! Verdade. Então... namoro é quando duas pessoas que se gostam resolvem... como eu posso falar... ir pra um novo nível."

        i "Novo nível? O que é isso?"

        mc "Não. Não é bem isso. Namoro é quando você encontra uma pessoa que você gosta muito e sente uma coisa especial por ela."

        mc "Daí, se essa pessoa também sente algo especial por você, vocês decidem namorar e viram um casal."

        mc "É mais ou menos isso. Tem gente que namora com mais de uma pessoa ao mesmo tempo, mas o mais comum é namorar só uma pessoa."

        scene xiang_evento9 with Dissolve(1.0)

        pause

        i "Uma pessoa especial..."

        i "Você é minha pessoa especial, [mc]."

        mc "X-xiang... eu..."

        i "Eu gosto de conversar com você, gosto de tocar em você, eu adoro quando você aperta a [i] e quando me olha."

        i "Eu queria poder ficar o tempo todo abraçada com você. Queria que você tivesse dinheiro pra pagar 24 horas de show comigo."

        mc "..."

        i "[mc]... Eu sou sua pessoa especial também?"

        "Eu sabia que ia acabar nisso. Como eu posso responder isso pra ela? Não posso falar que sim sem pensar direito, mas não posso negar."

        "Se eu só falar que não, o que vai acontecer com o coração dela? Agora que ela começou a falar... destruir isso?"

        mc "[i]... eu não sei."

        i "Não sabe?"

        mc "Não sei... isso é algo que não é fácil de responder."

        mc "Eu gosto de conversar com você também e te acho uma garota muito especial. Você é sensual e linda. O sonho de qualquer homem."

        i "Então eu sou!"

        mc "Talvez... mas eu não posso responder isso agora. Me desculpa."

        i "Então a gente não pode namorar?"

        mc "Não. A gente não pode. Nós dois somos adultos, somos responsáveis por nossa vida, então não teria nenhum problema a gente namorar."

        i "Então você não quer? Eu não sou sua pessoa especial..."

        mc "Não é isso. Não é tão simples. Eu me sinto um pouco responsável por você. Eu que tô te falando tudo isso. Não sei se seria certo."

        i "Então, tchau."

        mc "Calma!"

        scene black with Dissolve(1.0)

        scene xiang mc_olhando with Dissolve(1.0)

        i "Pense o que você tem que pensar. Depois você responde a [i]. No próximo show."

        mc "Obrigado. Eu prometo que vou pensar nisso."

        i "Não deixe a [i] esperando, [mc]."

        mc "..."

        scene black with Dissolve(1.0)

        "Onde eu fui me meter..."

        "..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 9:

        $ renpy.block_rollback()

        nora "Ela passou o dia todo ali, na verdade... A menina tá cada vez mais estranha."

        scene xiang_pe1 with Dissolve(1.0)

        pause

        "Ixi... tem tanta coisa acontecendo que eu acabei nem pensando sobre o 'namoro' com a [i]."

        "O que eu falo pra ela?"

        mc charmoso "Boa noite, [i]."

        scene xiang_pe4 with Dissolve(1.0)

        pause

        i "Boa noite, [mc]."

        mc envergonhado "..."

        i "Hoje eu quero ir direto pro show. A [i] vai te conquistar."

        menu:
            "Hoje eu não quero show.":


                mc normal "Obrigado, mas eu paguei a hora pra conversar com voc-"
            "Eu também tô ansioso. Bora.":


                mc safado "Eu também tô muito ansioso pra ver você em todas as poses."

                i "Hoje eu sou sua, [mc]. Vou fazer o que você mandar. Pode pedir o que quiser."

                call xiang_escolhe_pose from _call_xiang_escolhe_pose_3

                i "Então eu vou-"

        scene xiang_evento13 with hpunch

        pause

        mc "X-xiang!?"

        i "Eu fui sua... agora você é meu, [mc]. Você vai ser meu namorado. Só meu."

        mc "O que aconteceu? Você tá mais-"

        i "Eu conversei... pela primeira vez... eu conversei com as outras garotas e eu disse que queria namorar você."

        mc "S-sério?!"

        i "Elas disseram que o homem é burro e aceita qualquer coisa quando uma mulher domina ele pelo sexo."

        i "É isso que eu vou fazer. Eu vou usar meu corpo pra obrigar você a ficar comigo."

        mc "[i]... não digo que as garotas estejam erradas... mas nem todo homem é assim."

        mc "Além de que eu não aceitaria transar com você assim. Então não adianta."

        i "M-mas! E-eu-"

        mc "Tá tudo bem. Eu vou te explicar tudo. Só que antes, você tem que fazer um favor pra mim."

        i "Não foi assim que a [i] planejou que ia acontecer..."

        mc "Não tem problema nenhum. Vai ser melhor do que você imaginou. Você vai ver."

        i "Hmm... o que você quer que eu faça?"

        mc "Eu quero que você saia de cima de mim."

        i "N-não! A [i] espera um monte pra poder pegar no [mc]! Não vou soltar!"

        mc "A gente vai ficar juntinhos. Mas de um jeito diferente."

        i "Como assim? Você promete?"

        mc "Prometo. Você vai ver. Agora dá licença rapidinho."

        i "T-tá."

        show black with Dissolve(1.0)

        mc charmoso "Agora vem aqui e deita assim. Dá sua mão."

        i "A-assim? Nessa posição?"

        mc "Isso."

        scene xiang_evento10 with Dissolve(1.0)

        pause

        i "Pra que isso?"

        mc "Eu quero que você faça um teste. Veja se você acha mais gostoso quando eu tô te pegando no meu colo ou desse jeito agora."

        i "Hmmm... você tá apertando minha mão..."

        mc "Tá doendo? Desculpa."

        i "Não! Tá gostoso... eu não lembro de apertarem a mão da [i] desse jeito antes..."

        mc "Não é gostoso?"

        i "..."

        i "Deitada no seu colo eu sinto bem diferente do que antes."

        mc "Pois é. É diferente, né?"

        i "Não é ruim... eu sinto que... eu sinto que você tá protegendo a [i]. Que eu tô descansando enquanto você tá olhando tudo."

        mc "E eu tô."

        i "Isso é bom... mas por que você tá fazendo isso? Minha mão é melhor que minha bunda?"

        mc "Haha... não é bem uma luta entre sua mão e sua bunda. É só uma sensação diferente. Mas eu quero saber o que você achou."

        i "A [i] pode ficar assim pensando mais um pouco?"

        mc "Claro. O tempo que você quiser."

        i "Tá..."

        window hide

        pause

        scene xiang_evento11 with Dissolve(1.0)

        pause

        "Eu fui sincero com ela. Ela é linda, sexy, é agradável de um jeito único que eu nunca imaginei que existiria."

        "Mas não tá certo. A [i] pode ser adulta o suficiente pra trabalhar num puteiro, mas ela tem a vivência de uma criança."

        "Talvez ela nem goste de mim de verdade. Talvez eu só seja o cara que ela se afeiçoou porque eu tô dando atenção pra ela."

        "Usar isso pra se aproveitar de uma garota é nojento. Não é esse tipo de cara que eu sou."

        "Eu sei que eu também tenho meus podres... e são vários... mas não isso. Não se aproveitar de uma jovem que não conhece o mundo."

        "Agora... como falar isso pra ela sem ferir essa pequena confiança que ela encontrou?"

        i "[mc]... uma vez, quando a [i] era criança, uma pessoa disse que era muito bom ter uma família."

        i "Que eram pessoas que davam atenção pra gente, carinho e protegiam a gente..."

        i "Eu nunca tive família. Então eu não sei se isso foi uma mentira também... mas se for verdade... acho que você é minha família."

        i "Quando eu deitei assim, eu senti que você gostava de mim e queria que a [i] ficasse bem."

        i "Eu não lembro se um dia alguém fez isso comigo. Mas é muito bom. Muito mesmo..."

        mc "Eu sabia que você ia gostar."

        i "Só que eu não sei o que é melhor... quando eu sento no seu colo eu sinto um bom diferente. São coisas diferentes..."

        i "Será que tem problema se a [i] não souber o que é melhor?"

        scene xiang_evento12 with Dissolve(1.0)

        pause

        mc "Não tem problema nenhum, [i]. Sentimentos são assim. Nem sempre a gente sabe o que a gente tá sentindo."

        mc "O importante é que a gente tenha pessoas que fazem a gente se sentir seguros, pra que a gente tente entender tudo isso."

        i "Mas e o teste? Não serviu pra nada então?"

        mc "Que nada. Foi muito bem sucedido. Eu queria que você visse outro lado que nossa relação pode ter."

        mc "A gente não sabe qual você gosta mais, mas pelo menos agora você pode pensar nisso."

        i "É... a [i] vai pensar."

        mc "Você tem todo tempo do mundo."

        i "Obrigada..."

        i "[mc]."

        mc "Oi?"

        i "Seria muito incrível se a [i] pudesse ver você mais vezes. Eu queria morar com você, pra poder deitar em você sempre que eu quisesse."

        mc "..."

        i "Você não quer?"

        mc "C-claro que eu quero."

        i "Mas se não dá, eu quero aproveitar essa hora que a [i] tem com você..."

        "Como eu imaginar que eu ia tá nessa situação com uma garota de programa?"

        "Acho que... no fim... eu também tô confuso com o que eu sinto pela [i]. Eu quero ser o amante ou o pai ou o irmão ou o amigo dela?"

        "Uma coisa eu sei. Eu vou tirar ela daqui. Mesmo que eu tenha que usar a revista pra benefício próprio."

        "Mesmo que eu acabe ferrando a [nora], o [us] e o Distrito junto. Ninguém merece essa vida. Agora eu tenho certeza disso."

        i "Droga. Acho que passou da hora..."

        mc "Logo eu volto, [i]."

        i "Tá... vou te esperar, [mc]."

        show black with Dissolve(1.0)

        "..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        jump bdsm_sair

    elif xiang_evento == 10:

        $ renpy.block_rollback()

        "Deixa eu ir lá. Eu preciso confirmar com a [i] que ela tá pronta."

        scene black with dissolve

        scene xiang_pe2 with Dissolve(1.0)

        mc normal "Oi."

        i "Boa noite, [mc]. Tava com saudades."

        mc "Own... eu também."

        i "Eu queria muito que você voltasse pra gente poder ficar mais um tempo juntos. Vem vem."

        mc "C-calma."

        scene xiang_evento6 with Dissolve(1.0)

        i "É gostoso sentir você, [mc]..."

        mc "Haha..."

        i "Por que você tá fugindo de mim?"

        mc "Não tô."

        i "Tá sim. Eu tô sentindo."

        mc "A gente tem uma coisa séria pra conversar. Você tá sabendo?"

        i "Deixa eu ficar com você um pouquinho..."

        mc "T-tá."

        menu:
            "Encosta a cabeça na minha perna.":


                mc "Vem aqui. Encosta sua cabeça na minha perna. Você gosta assim, não gosta?"

                i "Eu gosto... também..."

                mc "Então vem."

                scene xiang_evento12 with Dissolve(1.0)

                i "Hmm... é um bom diferente."

                mc "Eu sei..."
            "Vem. Senta no meu colo.":


                mc "Já que você quer tanto, vem aqui. Senta no meu colo."

                "Assim eu sinto um pouco ela também... que gostosa..."

                i "Eba!"

                scene xiang_evento8 with Dissolve(1.0)

                i "Ah... eu adoro quando você me pega, [mc]."

                mc "Eu também gosto de te pegar. Mas hoje eu não vim pra isso."

        mc "Agora escuta o que eu vou falar. Vai acontecer uma coisa muito importante daqui a pouco."

        i "Vai?"

        mc "Você não tá sabendo? Eu vou tirar você daqui."

        i "Hm... mas não pode. Eu sou da [nora]. Ela não deixa eu sair."

        mc "Eu sei. Por isso que a gente vai sair escondidos. A [ce] não te falou?"

        i "Não."

        mc "Como assim? Achei que você já ia tá sabendo."

        "Será que aconteceu alguma coisa com ela? E se... descobriram?"

        "Eu tô ficando com medo... será que é melhor eu dar o fora?"

        "Mas e se a [ce] tiver chamando o pessoal agora? Caraca... o que eu faço?"

        menu:
            "Eu vou embora. Mas eu volto.":


                mc "[i]... acho melhor eu dar o fora agora. Mas eu prometo que eu volto pra te levar."

                i "Mas já? Eu nem fiquei com você ainda..."

                mc "É. Mas eu volto. Logo logo. Só é tudo segredo, ok? Não fala pra ninguém o que eu disse."

                i "Por quê?"

                mc "Porque pode dá muito ruim se a [nora] ou o Black Cash descobrirem. Até o Montanha."

                i "Ok... [i] vai tentar. Mas se a senhora mandar... [i] vai ter que responder."

                mc "Não! Você fala outra coisa."

                i "A [i] sempre obedeceu as regras. Pode ter castigo se a gente não obedece."

                mc "[i]... não se preocupe. Vai dar tudo certo, ok? Só acredita em mim."

                i "Tá..."

                mc "Agora eu vou sair daqui, porque alguma coisa não tá certa. Mas eu volto amanhã ou depois. E a gente sai."

                i "Se é assim... [i] vai esperar você voltar, [mc]."

                mc "Isso. Logo logo eu volto."

                i "Tchau..."

                mc "Não fica assim. Eu volto."
            "Eu vou ficar e seguir o plano.":


                mc "Bom... se você não tá sabendo, então a [ce] não conseguiu falar pra você. Eu vou tentar te explicar."

                i "Pode falar... eu gosto de ouvir você falando."

                mc "[i]... presta atenção."

                i "Hmm..."

                "Vai ser difícil assim."

                mc "A gente vai dar o fora daqui quando a [nora] e os outros estiverem ocupados."

                mc "Quando todo mundo deixar o salão, você vai pegar suas coisas, colocar em algum lugar e me encontra lá daquele lado."

                mc "A gente vai sair daqui. Você entendeu?"

                i "A [i] ia ficar feliz de ir com o [mc]... mas a [nora] não ia gostar. Não parece certo."

                mc "Eu sei. E por isso mesmo que você não pode contar pra ela. É segredo."

                i "Por quê?"

                mc "Porque pode dá muito ruim se a [nora] ou o Black Cash descobrirem. Até o Montanha."

                i "Ok... [i] vai tentar. Mas se a senhora mandar... [i] vai ter que responder."

                mc "Não! Você fala outra coisa."

                i "A [i] sempre obedeceu as regras. Pode ter castigo se a gente não obedece."

                mc "[i]... não se preocupe. Vai dar tudo certo, ok? Só acredita em mim."

                i "Tá..."

                mc "Agora é só a gente esperar... alguma coisa vai acontecer logo logo e eles vão tudo deixar o salão."

                i "E eu vou ficar aqui enquanto isso."

                mc "Haha... ok..."

                "Agora é só esperar e fazer minha parte."

                "..."

                show black with dissolve

                scene xiang_evento10 with Dissolve(1.0)

                i "Hmm... tô adorando..."

                i "Só que nosso tempo vai acabar, [mc]... você vai voltar?"

                mc "Nossa... já passou tudo isso?"

                "Q-que que tá acontecendo? Por que não acontece nada?"

                i "[mc]?"

                mc "Eu não sei o que aconteceu, [i]..."

                i "Você vai voltar?"

                mc "Claro que eu vou. Mas o plano... ok... eu vou, mas eu volto, tá?"

                i "Vou tá te esperando. Tchau tchau."

                mc "Até..."

        show black with dissolve

        "O que que aconteceu?"

        "Tava tudo certo pra eu tirar ela daqui e agora isso?"

        "As coisas não podem ficar assim. Eu vou ter que voltar aqui e ver o que vai dar."

        "Só tomara que não dê merda..."

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        $ tempo = 4

        jump bdsm_sair

    elif xiang_evento == 11:

        python:
            if renpy.android:
                xiang_evento_db = PythonSDLActivity.pegaXiang()
                
                if xiang_evento == xiang_evento_db:
                    PythonSDLActivity.addXiang()

            xiang_evento += 1

        $ renpy.block_rollback()

        $ xiang_escape = 5

        $ xiang_show = True
        $ stifler_falou = True
        $ celeste_falou = True
        $ proibido_salvar = False
        $ show_quick_menu = True

        $ renpy.block_rollback()

        jump xiang_escape3



    elif xiang_evento >= 12:

        $ renpy.block_rollback()

        "..."

        show black with Dissolve(1.0)

        p rindo "A história da [i] continua nas próximas atualizações."

        p "Fique ligado no desenvolvimento de CH para ver o final de todas as histórias!"

        hide black with dissolve

        jump bdsm_sair

label xiang_escolhe_pose:

    hide screen xiang_tela with Dissolve(0.5)

    mc "Eu vou querer..."

    menu:

        "Gaiola" if xiang_evento >= 6:

            $ area_xiang = "gaiola"

            mc tarado "Vou querer você na gaiola."

            i "Sua [i] vai pra gaiola então..."

            mc safado "Isso. Boa garota."

            scene black with dissolve

            scene xiang_gaiola1 with Dissolve(2.0)

            pause

            show screen xiang_tela with Dissolve(0.5)

            pause

        "De quatro" if xiang_evento >= 7:

            $ area_xiang = "agachada"

            mc safado "Fica de quatro pra mim agora."

            i "Sim, eu fico."

            scene black with dissolve

            scene xiang_agachada1 with Dissolve(2.0)

            pause

            show screen xiang_tela with Dissolve(0.5)

            pause

        "Deitada" if xiang_evento >= 8:

            $ area_xiang = "deitada"

            mc safado "Agora eu quero que você deite pra mim."

            i "Eu obedeço."

            mc tarado "Assim mesmo."

            scene black with dissolve

            scene xiang_deitada1 with Dissolve(2.0)

            pause

            show screen xiang_tela with Dissolve(0.5)

            pause

        "Posando" if xiang_evento >= 9:

            $ area_xiang = "especial"

            mc charmoso "Posa pra eu ver seu corpo."

            i "Olha pra mim por favor."

            mc safado "..."

            scene black with dissolve

            scene xiang_especial1 with Dissolve(2.0)

            pause

            show screen xiang_tela with Dissolve(0.5)

            pause
        "Por hoje tá bom":


            mc charmoso "Por hoje tô de boa, [i]. Valeu."

            i "Tá..."

    return

label xiang_pose_evento:

    hide screen xiang_tela with Dissolve(0.5)



    if area_xiang == "deitada":



















        if xiang_pose == 1:

            scene xiang_deitada1 with Dissolve(2.0)

            pause

        elif xiang_pose == 2:

            scene xiang_deitada2 with Dissolve(2.0)

            pause
        else:


            scene xiang_deitada3 with Dissolve(2.0)

            pause

    elif area_xiang == "agachada":

        if xiang_pose == 1:

            scene xiang_agachada1 with Dissolve(2.0)

            pause

        elif xiang_pose == 2:

            scene xiang_agachada2 with Dissolve(2.0)

            pause
        else:


            scene xiang_agachada3 with Dissolve(2.0)

            pause

    elif area_xiang == "gaiola":

        if xiang_pose == 1:

            scene xiang_gaiola1 with Dissolve(2.0)

            pause

        elif xiang_pose == 2:

            scene xiang_gaiola2 with Dissolve(2.0)

            pause
        else:


            scene xiang_gaiola3 with Dissolve(2.0)

            pause

    elif area_xiang == "especial":

        if xiang_pose == 1:

            scene xiang_especial1 with Dissolve(2.0)

            pause

        elif xiang_pose == 2:

            scene xiang_especial2 with Dissolve(2.0)

            pause
        else:


            scene xiang_especial3 with Dissolve(2.0)

            pause

    show screen xiang_tela with Dissolve(0.5)

    pause

screen xiang_tela():
    tag xiang

    modal True
    zorder 99

    imagebutton auto "extra/xiang1_%s.webp":
        xalign 0.03
        yalign 0.97
        action [ SetVariable("xiang_pose", 1), Jump("xiang_pose_evento") ]

    imagebutton auto "extra/xiang2_%s.webp":
        xalign 0.12
        yalign 0.97
        action [ SetVariable("xiang_pose", 2), Jump("xiang_pose_evento") ]

    imagebutton auto "extra/xiang3_%s.webp":
        xalign 0.21
        yalign 0.97
        action [ SetVariable("xiang_pose", 3), Jump("xiang_pose_evento") ]

    imagebutton auto "extra/xiang4_%s.webp":
        xalign 0.9
        yalign 0.97
        action Jump("xiang_escolhe_pose")

label xiang_escape1:

    "Eu decidi vir aqui procurar ajuda da juíza Richter."

    "Ela é uma mulher estranha, mas eu aposto que ela tá do lado certo."

    if v54_fim:

        "No julgamento da Priscila ela quis realmente pegar o [gus]. Isso é um excelente sinal."

    "Mas se eu tiver errado e ela me entregar pra eles... eu posso acabar me ferrando nessa também."

    "Mas essa é minha única chance. Eu preciso da ajuda de alguém poderoso."

    "Tirar a [i] do Distrito sozinho é impossível. A Celeste foi bem clara quando disse que a [nora] nunca deixaria."

    "Ok... hora de falar com a [eli]."

    scene black with dissolve

    scene prefeitura geral with dissolve

    "Passando por aqui..."

    scene black with dissolve

    scene prefeitura guarda with dissolve

    mc "Olá."

    "Policial" "Bem-vindo. O que o senhor deseja?"

    mc "Será que a juíza [eli] Richter poderia me receber?"

    "Policial" "E quem é o senhor?"

    mc "Diga que é o [mcc]. Um conhecido."

    "Policial" "Vou entrar em contato. Só um segundo."

    show black with dissolve

    "Espero que ela me receba..."

    hide black with dissolve

    "Policial" "Ela disse que tem alguns minutinhos para o senhor. Mas seja breve."

    mc "S-sim. Obrigado."

    scene black with dissolve

    scene tribunal geral with dissolve

    "Aqui onde tem os julgamentos... a sala dela fica passando pela porta lá atrás."

    scene black with dissolve

    "{i}TOC TOC{/i}"

    mc preocupado "Senhora Richter. É o [mc]."

    eli "Entre."

    scene black with dissolve

    scene juiza sofa2 with dissolve

    eli "Meu tempo é curto. Qual o problema desta vez? Eu não pretendo tirar você da prisão novamente."

    mc "Na verdade não é um problema. Eu só quero fazer o que é certo."

    eli "Todo mundo sempre acha que está fazendo o certo, jovem. Até que a justiça prove o contrário."

    mc "É sério! Eu quero salvar uma pessoa que está vivendo sob situação de escravidão."

    eli "..."

    mc "Essa garota, chamada [i], ela foi traficada e agora vive como escravo em um clube de BDSM."

    eli "E daí?"

    mc "Como assim e daí?! A gente precisa fazer alguma coisa!"

    eli "E você quer ir lá salvar ela com suas próprias mãos. É isso?"

    mc "Q-qual outra escolha eu tenho? A polícia tá no esquema!"

    eli "As coisas não funcionam como você está pensando, garoto. Existe um sistema para manter a sociedade em ordem."

    eli "Já imaginou se todo mundo quisesse resolver as coisas com suas próprias mãos?"

    eli "Teria gente se matando nas ruas. Viveríamos em completa barbárie. O cidadão precisa obedecer as regras."

    mc "O que você sugere então?"

    eli "Esqueça isso seria a melhor opção. Mas, se você não consegue, você pode fazer uma denúncia."

    eli "Existe um telefone específico para denunciar trabalho escravo contemporâneo. Eu posso anotar pra você."

    eli "As autoridades vão iniciar uma investigação e se comprovado, tomarão as medidas cabíveis."

    mc "Então eles vão fazer mesmo?"

    scene juiza sofa1 with Dissolve(1.0)

    eli "Em uma cidade normal, é o que aconteceria. Mas não aqui, obviamente."

    mc "A-ah!"

    eli "Esta cidade está podre. Ela é quintal de poucos que a usam para ampliar seu poder e influência."

    eli "As estruturas foram corrompidas desde a base até o topo, ou seja, é impossível esperar algo justo disso."

    mc "Mas então..."

    eli "Mesmo assim, não cabe a nós fazermos coisas erradas porque os outros fazem errado."

    eli "Eu sou uma juíza incorruptível. E eu não vou manchar minha carreira porque você não aguenta a realidade."

    mc "Ngh!"

    "Merda... ela era minha única chance..."

    scene juiza sofa6 with Dissolve(1.0)

    mc surpreso "S-senhora?!"

    eli "Talvez... tenha algo em minhas mãos que pode, talvez, te ajudar, e não seria ilegal de forma alguma."

    mc "S-sério?"

    eli "Mas depende do quanto você está disposto a ter isso."

    mc envergonhado "Q-que você quer dizer?"

    eli "Meu sapato está castigando meu pé hoje... ele precisa de um carinho."

    mc "S-seu pé?"

    eli "O que você me diz? Eu posso te contar mais sobre essa ajuda enquanto você cuida dele."

    "Eu sabia que as coisas iam pra esse lado..."

    "É só pintar uma chance dela ser sadista e toda a pompa vai pro ralo."

    "Sem a ajuda dela eu nunca vou conseguir tirar a [i] do Distrito. Então não tem muita chance."

    "A não ser que eu desista de tudo. Será que salvar a [i] vale tudo isso?"

    "Bom... também não tem problema ser abusado um pouco... pode até ser um pouco excitante... sei lá..."

    eli "E então, garoto?"

    "O que eu faço?"

    menu:
        "Eu cuido deles...":


            $ xiang_escape = 3

            mc envergonhado "Ok... eu cuido deles pra você."

            eli "Perfeito. Então tira tudo e ajoelha na minha frente."

            mc surpreso "A-ah!"

            scene black with dissolve

            "Onde foi que eu me meti..."

            scene pri9_img10 with Dissolve(1.0)

            eli "Isso, meu cachorrinho. Lambe e late pra sua dona."

            mc "{i}Au au{/i}"

            eli "Assim mesmo. Você já aprendeu."

            eli "Agora eu vou te contar o que eu posso fazer pra te dar uma chance de tentar alguma coisa."

            eli "Adianto que é pouco o que eu posso fazer, mas é algo que apenas eu posso fazer."

            mc "Hmm..."

            eli "Só continua lambendo ele. Deixa eu eu falo."

            mc "Shim, shenhora."

            eli "Muito bem. Eu vou pedir que a polícia vá até esse clube fazer uma 'vistoria de rotina'."

            eli "Você sabe como a polícia está comprometida, logo não vai dar em nada. Mas eles não estarão sozinhos."

            eli "Um procurador vai estar com eles, então no mínimo eles vão ter que fingir estarem fazendo alguma coisa."

            mc "Hm..."

            eli "Eles vão convocar os responsáveis pelo estabelecimento. Vão fazer eles andar por todo o lugar."

            eli "Você vai ter cerca de uma hora pra tirar quem você quer de lá. O caminho vai estar livre pra você."

            eli "É provável que dê certo? Óbvio que não. Mas é como eu posso te ajudar."

            eli "Claro que se por um milagre der certo e você realmente tirar ela de lá, o resto é com você."

            eli "O Distrito não vai poder ir atrás dela? Eles vão reclamar pra polícia que uma escrava foi salva?"

            eli "Até pra eles seria demais atender um pedido absurdo desses. Mas os donos do clube poderiam te caçar pessoalmente."

            eli "Enfim, isso tudo agora é com você. Decida qual dia você quer minha ajuda e me avise."

            eli "Você foi um bom cãozinho. E eu posso fazer isso por você. E limpar essa cidade é algo que me agrada também."

            mc "Obrrgaduh, shenhora."

            eli "Agora pode parar. Você me deixou excitada o suficiente. Eu resolvo a partir daqui."

            "Ufa..."

            scene black with dissolve

            scene tribunal visao with dissolve

            "Então ela realmente vai ajudar!"

            "Eu vou ter uma chance de tirar a [i] de lá. E a [nora] vai tá ocupada com a vistoria. Provavelmente o Montanha também."

            "Vai ser minha chance de tirar ela de lá. Mas fazer isso sozinho ainda vai ser complicado demais."

            "Eu acho que eu vou contar tudo pra Celeste. Ela duvidou que eu ia conseguir, mas agora com essa talvez ela acabe comprando a ideia."

            "Ela tem acessos lá. Ela pode levar a [i] pra mim. Preparar ela e garantir que a gente tenha um caminho limpo pra fugir."

            "Ter alguém assim lá vai ser perfeito. Eu tenho que achar ela lá no clube e falar com ela! Ela precisa me ajudar!"

            scene black with dissolve

            jump cidade_prefeitura
        "Melhor não, senhora.":


            $ xiang_fim = True

            mc envergonhado "S-senhora, uma coisa não devia tá atrelada a outra. Isso não parece certo."

            eli "Eu já te falei o é o certo. Eu estou fazendo um favor a um conhecido. E eu quero um favor em troca."

            eli "Além de que você não passa de um zé ninguém. Se você não vai aceitar, saia logo daqui."

            mc "O-ok... obrigado por me ouvir."

            eli "Sujeitinho frouxo."

            mc serio "..."

            scene black with dissolve

            "Infelizmente eu não vou poder ajudar a [i] e nem o pessoal da Cidade Chinesa."

            "Mas pelo menos eu mantive minha dignidade intacta. Isso é o mais importante."

            jump cidade_prefeitura

label xiang_escape2:

    mc "Eu queria falar com você um negócio."

    ce "É sobre aquele lance de novo, né?"

    mc "É. Só qu-"

    ce "Não esquenta. Vai lá no mesmo lugar de antes. Já te encontro lá."

    mc "T-tá."

    scene black with dissolve

    "Eu achei que ela não ia querer falar comigo..."

    scene mc_celeste1 with dissolve

    mc "Eu achei que ia ser mais difícil falar com você."

    ce "E ia ser mesmo. Mas uma pessoa acabou me falando do seu plano."

    mc "Hm?"

    ce "Eu quero que você escute bem. A última coisa que a gente quer é que a [nora] desconfie de alguma coisa."

    ce "Eu vou fingir que eu só vim falar pra você que eu não tava no clima."

    ce "Vou fingir que eu perdi a paciência com você. E não é pra você me chamar de novo. Nunca mais."

    mc "N-nunca?"

    ce "Nunca."

    menu:
        "Eu achei que um dia a gente... você sabe...":


            mc "Eu tava pensando que talvez um dia a gente pudesse... você sabe... tomar uma coisa juntos."

            scene mc_celeste3 with Dissolve(1.0)

            pause

            ce "[mc]... eu sou areia demais pro seu caminhão."

            ce "Além de que... a gente gosta de coisas parecidas. Sinto até que a gente pode acabar sendo rivais logo logo."

            mc "C-como é?"

            "Não acredito... Então ela... espera... pensando agora... teve uma vez que o Black Cash falou... hm..."
        "Ok...":


            mc "Beleza. Eu prometo."

            mc "Vai ser uma pena. Você parecia uma mulher interessante."

            scene mc_celeste3 with Dissolve(1.0)

            pause

    ce "Você é uma pessoa que com certeza eu ia querer conversar mais vezes."

    ce "Mas depois do que vai acontecer aqui, eu aposto que você não vai ter coragem de pisar aqui de novo."

    mc "Então você tá sabendo?"

    ce "Pois é. Eu fiquei de garantir que você vai ter caminho livre pra sair com ela."

    ce "Eu também vou deixar ela avisada. Vou arrumar as coisas dela."

    ce "Vê se cuida bem da garota. Eu sei lá que sacanagem vocês faziam aqui, mas fora do clube ela é uma mulher comum."

    ce "Trate ela com carinho e respeito. Ou você não vai ser melhor que a velha."

    menu:
        "Com certeza.":


            mc "Pode confiar."
        "Talvez a gente...":


            mc "Bom... talvez a gente acabe ficando juntos..."

            ce "Se for a vontade dela, sem problemas. Só não seja um cuzão."

            mc "P-pode deixar."

    ce "É o mínimo que eu espero depois do que a gente vai fazer. Inclusive, falando de forma prática agora."

    ce "A coisa vai acontecer assim. Você vai vir aqui uma noite como se nada tivesse acontecido."

    ce "Vai chamar a menina como se fosse qualquer outro dia."

    ce "Eu estando aqui ou não, eu vou ver você entrando. Eu vou avisar o contato pra ele fazer a parte dele."

    ce "Quando o local for esvaziado, a garota vai pro quarto e você finge que vai sair, mas continua no prédio."

    ce "Vai pro banheiro ou fica em qualquer canto. A confusão vai ser grande, ninguém vai notar."

    ce "Dá uns 5 minutos. Confirma que não tem ninguém e vai pra aquele lado ali. Ela vai tá te esperando."

    ce "Você pega a menina e saiam pela entrada normal. Eu vou garantir que a velha e o Montanha não vão estar lá."

    ce "O mais perigoso é o Black Cash. Pode deixar que eu vou cuidar dele."

    mc "Caraca... parece uma operação de verdade."

    ce "Isso não é brincadeira. Olha. Se a [nora] ou o Black Cash te pegar, eles vão arrancar sua pele. Literalmente."

    ce "Essas pessoas não matam, elas te fazem implorar pela morte."

    ce "Eu nunca imaginei que você ia ter coragem pra fazer algo assim. Mas seguindo o plano tem uma chance de dar certo."

    mc "{i}gulp{/i}"

    ce "Ah! E se te pegarem, eu não sei nada sobre isso. Você vai morrer sozinho."

    ce "Por isso, decore bem o que eu te disse e siga os planos DIREITINHO. Qualquer passo errado pode ser sua morte."

    mc "T-tá."

    mc "Chamar a Xiang, esperar a batida acontecer, fingir que vou sair, depois ir procurar ela e dar o fora pela entrada."

    ce "Isso aí. Se você conseguir fazer isso, talvez vocês realmente saiam vivos e ela vai ter uma boa vida."

    ce "Agora vamos que eu falei demais. Adeus."

    mc "Adeus, [ce]. E valeu por tudo."

    scene black with dissolve

    scene distrito2 with dissolve

    "Nossa... nem acredito. Talvez eu realmente consiga tirar a [i] daqui."

    "Eu preciso decorar os procedimentos e voltar aqui e chamar a Xiang pra um show particular. É isso."

    "O resto eu vejo lá na hora. Bora!"

    $ tempo += 1

    jump call_cidade

label xiang_escape3:

    scene black with dissolve

    scene xiang_pe4 with Dissolve(1.0)

    i "Que bom que você voltou mesmo! Você tava estranho da outra vez."

    mc desculpa "Eu sei... desculpa... eu achei que ia acontecer alguma coisa, mas não aconteceu..."

    i "Hmmm... você quer mais do que sentir a [i]? Você esperava mais?"

    mc surpreso "N-não! Não é isso que eu tô comentando!"

    "Parece que a [i] ainda não tá ligada do que vai acontecer..."

    "A [nora] tá normal... a [i]... a [ce] não falou nada... Eu sinto que eu sou o único que tá pensando nisso."

    "Por que eu sinto que vai acontecer alguma coisa desagradável?"

    i "Vem! Deixa eu sentar em você!"

    mc "O-opa!"

    scene black with dissolve

    scene xiang_evento2 with Dissolve(1.0)

    i "Eu quero aproveitar o [mc] tudo o que eu puder..."

    "Tudo continua igual da outra vez... se continuar assim vai ser mais um encontro com a [i] e pronto!"

    menu:
        "A [ce] me ferrou...":


            "Eu vou ter que falar de novo com a [ce]. Eu não devia ter deixado na mão dela."

            "Ela que ficou de chamar... eu devia ter ficado com essa responsabilidade. Eu entreguei o principal pra ela."
        "Eu preciso confiar nela!":


            "Talvez tenha dado merda, mas não quer dizer que ela me traiu! Eu tenho que confiar na [ce]!"

            "Mas... e se..."

    i "[mc]... você tá pensando na [i]?"

    mc "[i]... agora não é hora."

    i "Como assim? Agora é nossa hora..."

    mc "Só que..."

    scene xiang_evento2 with vpunch

    nora "Todos pra fora agora!"

    mc "!"

    i "Hm?!"

    nora "Todas as garotas pro quarto! E vocês, seus safados! Saiam agora!"

    "Não acredito! D-deve ser a vistoria!"

    i "[mc]... eu vou ter que ir pro quarto..."

    mc "Eu sei. Tá acontecendo agora. Vai!"

    i "?"

    mc "Você não lembra?! Segue o plano!"

    i "Hmm... não tô entendendo..."

    nora "Olho puxado! Sai de cima dele e vai pro dormitório agora!"

    i "S-sim, senhora!"

    nora "E você sai daqui também!"

    mc "C-claro."

    i "Tchau, [mc]."

    scene black with dissolve

    scene distrito_clube geral with dissolve

    "Ok... tá acontecendo... eu preciso seguir com o plano perfeitamente."

    "Se eu errar algum passo, posso foder tudo. Eu vou ter que lembrar."

    "Tá todo mundo saindo. A [nora] foi lá pra frente. O que eu faço?"

    menu:
        "Sair do clube":




            "Eu lembro! Agora é a hora que eu saio do clube..."

            scene black with dissolve

            "..."

            "Espera... e a [i]?! Eu tô saindo sem ela!"

            jump xiang_escape_falha
        "Se esconder em algum lugar":




            "Eu me lembro. Agora é a hora que eu tenho que me esconder."
        "Procurar a Xiang":




            "Eu lembro. Agora eu tenho que ir procurar a [i] e tirar ela daqui."

            scene black with dissolve

            "..."

            "Homem" "Ei! Você! É pra todo mundo sair! Pra onde você tá indo?!"

            mc "A-ah! Verdade..."

            "Merda! Fui pego!"

            jump xiang_escape_falha

    scene black with dissolve

    scene distrito_clube visao with dissolve

    "Ok... acho que aqui ninguém vai me ver..."

    "Tá todo mundo saindo meio apressado... tem uns arrumando as calças. Aquele cara tá com um vermelho na coxa."

    "As garotas passaram por aquele lado depois do stage. Deve ser ali a entrada do dormitório."

    "Ok..."

    "Parece que todo mundo saiu. Ninguém veio atrás de mim. Tá dando certo por enquanto."

    "Vou dar mais um ou dois minutos... e daí o que eu faço em seguida?"

    menu:
        "Sair do clube":




            "Eu lembro! Agora é a hora que eu saio do clube..."

            scene black with dissolve

            "..."

            "Espera... e a [i]?! Eu tô saindo sem ela!"

            jump xiang_escape_falha
        "Continuar escondido até o fim":




            "É. Acho que é isso. Eu tenho continuar aqui até o final."

            show black with dissolve

            hide black with dissolve

            "Parece que o pessoal já tá voltando... quê?!"

            "Eu tinha que ter ido atrás da [i]! Como a gente vai sair agora?!"

            jump xiang_escape_falha
        "Procurar a Xiang":




            "Eu lembro. Agora eu tenho que ir procurar a [i] e tirar ela daqui."

    scene black with dissolve

    scene xiang_escape1 with dissolve

    pause

    "O problema é que ela nem sabia nada sobre a fuga..."

    "E se ela não aparecer? O plano vai ser tudo por nada. A gente não vai ter outra chance igual essa."

    "Será que foi a [ce] que não fez a parte dela? Ela parecia tão interessada..."

    "Hm?!"

    "É a [i] que eu tô vendo ali?"

    "Parece ela! Eu tenho que pegar ela e sair daqui!"

    scene black with dissolve

    scene xiang_escape2 with dissolve

    mc "[i]!"

    i "Oi, [mc]."

    mc "Você tá com uma mochila?! Tá pronta pra sair?!"

    i "É... falaram pra eu pegar minhas coisas. Que a gente tava indo embora."

    menu:
        "É isso mesmo. Bora.":


            mc "Isso aí. Eu tô aqui pra te levar embora."

            i "Ok..."
        "Foi a [ce]?":


            mc "Foi a [ce] que te avisou?"

            i "É. A gente nunca conversou direito antes, mas ela disse que eu ia embora daqui."

            i "Ela me deu umas roupas e essa mochila e falou pra eu te esperar aqui."

            "Boa! A [ce] não me traiu!"

    mc "Só que... eu nunca te perguntei uma coisa... e não tá certo eu decidir por você."

    mc "Você vai mesmo querer sair daqui? A escolha é sua."

    i "Eu nunca tive nada contra esse lugar. Eu só aceitei o que os mais velhos me disseram desde criança."

    mc "Então..."

    i "Eu sei que tem alguma de errado nisso tudo. Nunca ninguém ter perguntado o que eu queria."

    i "Mas eu poderia viver aqui pra sempre."

    mc "V-você vai ficar então?"

    i "Você foi a primeira pessoa que perguntou o que eu queria fazer."

    i "Desde pequena, onde eu nasci, me tiraram dos meus pais pra me treinar no templo."

    i "Depois fizeram exames comigo por um tempão. Eu vivia presa numa sala branca."

    i "E eu acabei aqui, tendo que obedecer a [nora]."

    scene xiang_escape3 with Dissolve(1.0)

    i "[mc]... eu nunca pude escolher nada que ia acontecer na minha vida."

    mc "Isso no tá certo. Você devia poder escolher suas coisas."

    mc "E mesmo quando você era criança, seus pais deveriam ter protegido você. Era a responsabilidade deles."

    i "É... mas não foi fácil pra eles também. Aquele lugar não é fácil."

    i "Mas o que eu queria falar é que... eu sei todo o trabalho que você e os outros tiveram pra me tirar daqui."

    i "E mesmo fazendo a coisa certa, você ainda me perguntou o que eu queria. Isso... foi muito legal."

    mc "É... mas... o que vai ser?"

    i "Claro que eu quero sair."

    mc "Sério?!"

    i "Ainda mais porque vai ser com você, [mc]."

    i "Se puder... eu queria ficar um tempo com você..."

    mc "C-comigo?"

    i "Você sabe que eu gosto de você. Antes de voltar pra onde eu nasci, eu queria viver com você. Por favor?"

    mc "[i]... e-eu não sei se isso ia ser certo. Até m-me embolei..."

    i "Só um pouco? Por favor!"

    "Caraca... meu plano era levar ela pra Cidade Chinesa... e agora?"

    if casa:

        "Bom... minha casa é bem grande. Ela pode ficar com o quarto e eu fico na sala."
    else:


        "Infelizmente minha casa só tem um cômodo. Não ia ser bacana viver com ela assim."

    menu:

        "Ok. Minha casa aguenta os dois." if casa:

            $ xiang_casa = True

            mc "Se você realmente quer ficar lá... ok..."

            i "Verdade?!"

            mc "Minha casa é grande. Você pode ficar no quarto e eu fico na sala."

            i "Mas eu queria dormir com você."

            mc "Xi-xiang? Depois a gente fala sobre isso. Melhor a gente sair."

            i "Tá."

        "Infelizmente minha casa é pequena." if not casa:

            mc "Desculpa, mas minha casa é pequena demais pra dois adultos. Não ia ser legal."

            i "[i] não liga. A gente dorme abraçados."

            mc "M-melhor não, [i]. Não ia pegar bem."

            mc "Você precisa se recuperar e ficar com um cara não vai ser o melhor agora."

            mc "Mas eu prometo que a gente vai se ver bastante lá, tá? Eu vou te visitar sempre."

            i "Promete?"

            mc "Prometido."

            i "Tá."
        "Melhor não.":


            mc "Desculpa, [i], mas acho que não seria o melhor pra gente."

            mc "Você precisa se recuperar e ficar com um cara não é o que você precisa agora."

            mc "Mas eu prometo que a gente vai se ver bastante lá, tá? Eu vou te visitar sempre."

            i "Promete?"

            mc "Prometido."

            i "Então tá."

    i "Acho que a gente pode ir."

    mc "É melhor. Antes que o pessoal comece a voltar da vistoria. Inclusive acho que a gente perdeu tempo demais."

    i "Mas não tem ninguém ainda. Tá bem quieto."

    mc "É nossa chance. Bora."

    scene black with dissolve

    "O principal a gente conseguiu. Que é passar da [nora]. Ela tá ocupada demais com o pessoal da [eli]."

    "Nosso caminho tá livre. Só falta o Montanha não tá lá agora."

    "???" "PARADOS AGORA! {nw}"

    scene xiang_escape4 with vpunch

    nora "Que porra de caralho que tá acontecendo aqui?!"

    mc "[nora]!? O q-que você tá fazendo aqui?!"

    nora "Eu sabia que essa 'vistoria' tava estranha demais! Mas esse tipo de truque não pega macaca velha!"

    nora "No meio da noite uma visita dessas?! E me levando pos cafundós? Muito engraçado!"

    nora "Eu sabia que tinha caroço nesse angu! Ah, eu sabia! Alguma coisa fez eu vir aqui! HAHA!"

    "Meu Deus! Tudo o que não podia acontecer!"

    "Ela vai me esfolar vivo!"

    nora "Acho bom vocês me explicarem exatamente o que tá acontecendo aqui."

    mc "É..."

    "A [nora] manda no Distrito. A [ce] avisou que se ela me pegasse ela ia me fazer implorar pra morrer!"

    "O que eu fiz de errado!? Por que ela tá aqui?!"

    nora "Fala logo!"

    menu:
        "Não é o que você tá pensando!":


            mc "Não é o que você tá pensando! A gente não tá fazendo nada!"

            nora "Ainda tem coragem de mentir?"
        "E-eu só tô seguindo ordens!":


            mc "E-eu só tô seguindo as ordens de outras pessoas! Eu não tenho culpa!"

            nora "Eu sabia que você era frouxo, mas esperava pelo menos um pouco mais de você."
        "Eu vim salvar ela!":


            mc "É o que você tá pensando! Eu vim tirar a [i] daqui!"

            i "Isso aí!"

    i "O [mc] veio me salvar. Isso que importa. Ele é meu herói."

    mc "[i]!"

    nora "Eu comprei essa garota. Você não tem o direito de levar ela daqui."

    nora "E você, puta, você sabe que não pode sair daqui sem minha permissão."

    i "[i] quer sair com o [mc]. Ela escolheu isso."

    nora "Não pode ser possível isso que eu tô ouvindo. Quando foi que você ficou tão corajosa, hein?!"

    i "O [mc] ajudou a [i] a ter escolha. E eu quero sair daqui e procurar outra vida."

    nora "E vocês acham que os dois iriam enganar todos nós. Me enganar ainda por cima?"

    mc "[nora]... coloque a mão na consciência. Prender a [i] não é certo."

    mc "Traficar seres humanos é contra todo tipo de lei. Deve tá cheio de garotas que trabalhariam aqui!"

    nora "Você não entende nada mesmo, né, garoto?"

    mc "Do que você tá falando?"

    scene xiang_escape5 with Dissolve(1.0)

    nora "Do que eu tô falando?! Você tá nessa a ilha há bastante tempo pra saber do que eu tô falando!"

    nora "A ilha é dividida entre grupos! É um triângulo perfeito!"

    "T-triângulo? Onde que eu já ouvi isso?"

    nora "'O triângulo precisa de três lados, mas são os vértices que sustentam sua forma'."

    nora "Você deveria saber o lema que mantém a Capital próspera do jeito que é. E você acha que vai acabar com isso agora?"

    menu:
        "Eu não tô entendendo nada.":


            mc "Eu realmente não tô entendendo nada do que tu tá falando..."

            nora "Eu sei que você só se faz de tonto pra gente baixar nossa guarda. Você é mais esperto do que parece."
        "Eu vou acabar com esse triângulo.":


            mc "Escuta aqui. Eu vou acabar com esse triângulo! Chega de vocês dominarem a cidade!"

            mc "Pessoas demais sofreram pra que vocês pudessem se manter no poder!"

            nora "HAHAHA! Não seja ridículo, menino! O que você pode contra as forças da capital?!"

            nora "Ridículo!"
        "Vou ficar quieto":


            "..."

            nora "Não tem nada pra falar agora? Foda-se!"

    nora "Eu vou te dar uma chance. Uma única chance."

    mc "{i}gulp{/i}"

    nora "Ou você deixa a garota aqui e continua vivo, podendo andar pela cidade..."

    mc "Ou...?"

    nora "Ou você continua com essa ideia ridícula e nunca mais vai ter vida fácil aqui."

    nora "Não é só no Distrito dos Prazeres, idiota. Em todos os lugares da cidade!"

    nora "Nosso poder vai muito além do que você imagina. E você vai viver olhando pro lado em cada esquina."

    nora "Quem sabe o próximo carro cruzando a rua não seja seu assassino... você imagina viver assim?!"

    mc "..."

    nora "Ah! Isso SE vocês fizerem o milagre de saírem daqui vivos!"

    i "[mc]... a gente vai sair, né?"

    mc "[i]... o plano não era pra ser assim... não era pra ela descobrir..."

    mc "O que vai acontecer comigo se eles vierem atrás de mim?"

    i "Mas... e a escolha da [i]?"

    mc "Minha nossa... o que eu faço?"

    "Salvar a Xiang e viver com medo ou desistir dessa idiotice e manter minha lealdade aos que mandam na ilha?"

    "Eu sinto que isso vai mudar minha vida aqui pra sempre!"

    nora "E então?! O que você vai me responder, [mc]?!"

    menu:
        "Eu vou levar ela.":


            mc "Você pode tentar me intimidar, mas você já se ferrou, [nora]. Eu e a [i] tamo saindo."
        "Eu vou obedecer você.":


            $ xiang_fim = True

            mc "Você tem razão... eu vou obedecer você. Eu não quero esse tipo de inimigo aqui."

            i "[mc]!"

            mc "Desculpa, [i]..."

            scene black with dissolve

            "Eu deixei a [i] lá... e... eu vou ter que esquecer ela, a He Xiangu e o pessoal da Cidade Chinesa."

            "Pelo menos eu não vou ter que viver igual um fugitivo. Eu não quero desafiar gente desse calibre."

            $ tempo += 1

            jump call_cidade

    scene xiang_escape6 with vpunch

    nora "Você só pode tá brincando!"

    i "[mc]... a pose..."

    mc "Ameaças é tudo o que sobrou pra você. O Montanha, o Black Cash tão enrolados com a vistoria, certo?"

    mc "Nem era pra você tá aqui. As garotas tão nos seus quartos, os clientes sairam. Não é você que vai parar a gente."

    nora "O Montanha pode tá lá, você me pegou com esse teatrinho. Mas eu sou suficiente pra acabar com você, pirralho!"

    nora "Não se vira a Rainha sendo uma frouxa igual você. Eu sei me defender muito bem!"

    mc "Você só pode tá brincando. Você vai querer brigar comigo mesmo? Eu sou um homem adulto!"

    nora "Logo logo eles vão voltar! Ou você passa por mim agora, ou pode dar adeus ao seu plano e a sua vida!"

    mc "Se não tem jeito, eu vou ter que bater em você mesmo! Mas eu não queria!"

    if mc_fisico > 100:

        "Eu tô treinando na academia... eu tô forte. Eu tô confiante."

        "Tá na hora de colocar meu treinamento à prova!"
    else:


        "Eu não sou o cara mais bombado de academia, mas o que importa?"

        "Não vai ser uma senhora que vai me parar."

    nora "Venha!"

    scene xiang_escape7 with hpunch

    mc "IIAAAHHH!"

    nora "AAGH!"

    mc "Toma essa!"

    i "[mc]!"

    mc "Peguei você!"

    nora "Seu fedelho!"

    mc "A perna!"

    scene xiang_escape8 with vpunch

    mc "ARGH!"

    nora "Idiota! Você acha mesmo que você vai me vencer?"

    mc "C-como?!"

    nora "Agora você vai morrer devagar! Eu vou tirar toda a pele do seu corpo com uma faca cega!"

    mc "N-não!"

    nora "Mas antes eu vou esmagar isso que você tem entre as pernas!"

    "O que eu podia ter escolhido diferente!?"

    nora "HAHAHA!"

    scene red with vpunch

    mc "AAAHHH!"

    scene xiang_escape9 with hpunch

    pause

    nora "{i}UGGH{/i}"

    mc "[i]?!"

    i "..."

    nora "ANGH!"

    scene xiang_escape10 with vpunch

    nora "Ughhh..."

    nora "..."

    mc "E-ela apagou?"

    i "Acho que sim."

    mc "[i]... o que foi aquilo?"

    i "Ela comemorou antes da hora, [mc]. Quando ela ia amassar seu pau, não teve como esquivar do meu chute."

    mc "Chute? Aquilo foi uma voadora espetacular. Onde você aprendeu isso?"

    i "Não sei..."

    mc "Mais importante... obrigado por salvar meu amigo."

    i "A gente não vai embora?"

    mc "Verdade. A [eli] disse que a gente ia ter uma hora mais ou menos, já deve ter quase passado isso."

    i "E a gente tem que passar pelo Montanha na entrada."

    mc "N-não! Ele não pode tá lá!"

    i "Vamos ver..."

    mc "Bora..."

    show black with dissolve

    "..."

    mc preocupado "A-ah!"

    scene distrito2 with Dissolve(1.0)

    i "Calma, [mc]... a gente saiu."

    mc concentrando "Ufa..."

    mc "A gente tem que sair voando daqui antes que eles encontrem a gente."

    show black with dissolve



    if xiang_casa:

        mc envergonhado "Você vai querer ir pra casa mesmo?"

        i "É. A Xiang queria."

        mc "Beleza... vamo lá."

        scene black with dissolve

        scene ap quarto with Dissolve(1.0)

        mc envergonhado "Ok... você pode ficar aqui no quarto. Eu vou dormir na sala."

        i "Mas a gente não pode dormir juntos? Igual lá no clube?"

        mc "D-de jeito nenhum. Você fica aqui. Você deve tá cansada. Amanhã a gente conversa."

        mc "Fecha a porta e descansa bem."

        i "Ok..."

        mc "Boa noite."

        scene black with dissolve

        scene ap mc_dormindo3 with dissolve

        mc "Nem acredito que a [i] tá aqui..."

        "Será que ela realmente quer ficar comigo? Ela parece bem sincera, mas será que ela sabe o que tá falando?"

        "Eu sinto que ela se afeiçoou em mim porque eu dei atenção pra ela... Isso não é gostar de verdade."

        "Eu tenho que pensar com calma."

        "Só que antes a gente precisa resolver o lance da Cidade Chinesa. Amanhã mesmo eu vou fazer isso..."

        scene black with dissolve

        scene ap sala with Dissolve(1.0)

        mc concentrando "Uaaa...."

        "Será que a [i] dormiu bem?"

        mc normal "[i]? Já acordou?"

        i "Hmmm... tô levantando... um segundo."

        scene black with dissolve

        scene xiang_ape1 with dissolve

        i "Bom dia, [mc]."

        mc surpreso "X-xiang?! Que roupa é essa?!"

        i "Que foi? É uma blusinha que as meninas me deram pra dormir."

        menu:
            "Você precisa arrumar a alça!":


                mc surpreso "A a-a-alça!"

                i "Não tem problema, [mc]. Eu não ligo de você olhar pra mim."

                mc envergonhado "Meu Deus... o que eu faço com você?"

                i "Eu tenho uma ideia."

                mc surpreso "D-depois você fala!"
            "Problema nenhum. Tá tudo certo.":


                mc tarado "Pensando bem, tá tudo certo. Eu quero que você fique bem à vontade, ok?"

                i "Obrigada."

                "Se as coisas continuarem assim vai ser difícil resistir..."

                "Mas agora eu tenho que focar no que interessa."

        mc normal "Primeiro a gente precisa levar você até a Cidade Chinesa. Imagino que você queira voltar pra lá."

        scene xiang_ape2 with Dissolve(1.0)
    else:


        mc normal "Ok. Aqui a gente já tá a salvo."

        i "Xiang quer ir na casa do [mc]."

        mc envergonhado "Eu já expliquei que não vai dar. Vou deixar você uma noite no hotel."

        mc normal "Tudo bem? Eu vou deixar tudo pago e amanhã cedo eu já venho te buscar."

        i "Tudo bem..."

        mc "Eu sei que faz tempo que você não fica sozinha, mas eu prometo que a primeira coisa de manhã eu venho te pegar."

        i "Não se preocupe. A [i] sabe se cuidar."

        mc envergonhado "Às vezes você parece criança, mas às vezes você parece mais adulta que eu, [i]."

        i "Hehe..."

        scene black with dissolve

        scene hotel recepcao with dissolve

        mc normal "Então ficou tudo certo. Bom descanso e até amanhã."

        i "Boa noite, [mc]. Fico te esperando amanhã cedinho."

        mc "Cedinho. Tchau tchau."

        i "Tchau."

        scene black with dissolve

        scene mc dormindo with dissolve

        mc "Nem acredito que a [i] fala aquelas coisas sobre a gente..."

        "Será que ela realmente quer ficar comigo? Ela parece bem sincera, mas será que ela sabe o que tá falando?"

        "Eu sinto que ela se afeiçoou em mim porque eu dei atenção pra ela... Isso não é gostar de verdade."

        "Eu tenho que pensar com calma."

        "Só que antes a gente precisa resolver o lance da Cidade Chinesa. Amanhã mesmo eu vou fazer isso..."

        scene black with dissolve

        $ dia += 1

        $ tempo = 1

        scene apartamento dia with dissolve

        mc concentrando "Uaaa...."

        "Será que a [i] dormiu bem? Vou lá rapidão."

        scene black with dissolve

        scene hotel recepcao with dissolve

        mc normal "Oi. Você podia chamar a hóspede do quarto 420 por favor?"

        "Recepcionista" "Vou chamar. Mas acho que vi ela tomando café da manhã. Vou pedir pra avisar que o senhor está aqui."

        mc "Valeu."

        show black with dissolve

        hide black with dissolve

        mc normal "[i]!"

        show xiang_new with dissolve

        i "Oi, [mc]. Bom dia."

        mc normal "Bom dia. Dormiu bem?"

        i "Dormi. Mas não via a hora de acordar e a gente se ver de novo."

        mc "Hehe..."

        mc "E então? Pronta pra ir pra Cidade Chinesa? Sua antiga casa?"

    i "[mc]..."

    i "Eu não pretendo voltar lá."

    mc desconfiado "C-como é?"

    i "Minha vida lá não era muito diferente da minha vida no clube da [nora]."

    i "Eu não me lembro tão bem. Eu era meio criança, mas eu fui separada dos meus pais e criada no templo."

    i "Eu nunca pude fazer o que eu queria. Eu não sei o que aconteceu com meus pais."

    i "Mas agora eu não sinto mais vontade de viver com eles. Faz tanto tempo..."

    mc normal "Eu não tinha pensado nisso ainda, [i]. O que você planeja fazer então?"

    if xiang_casa:

        i "Eu gostaria de continuar um tempo na sua casa..."

        mc envergonhado "Ok... fique o tempo que você precisar. Mas e depois?"

    i "Eu não sei ainda... mas talvez eu vá pra fora. Pra fora da cidade. Pra fora do país."

    mc "S-sério?"

    i "A [i] não tem dinheiro... mas eu vou juntar e talvez eu vá pra China."

    mc normal "Uou."

    i "Alguma coisa me faz ter vontade de ir lá e ver como é. Se realmente é igual a Cidade Chinesa."

    i "A [i] ainda não viveu sua própria vida. Não sei nada das coisas. E eu quero começar a vida lá."

    mc "Isso é bacana, [i]. Não vai ser fácil viajar, mas se você tiver paciência você vai conseguir."

    i "Tomara."

    mc desculpa "Mas antes eu queria pedir esse favor pra você. De ir comigo até a Cidade Chinesa."

    mc "Tem alguém lá que precisa te ver."

    i "Não vai ser fácil, [mc]. Eles realmente entram na cabeça deles."

    mc normal "Quando ela te ver, eu tenho certeza que ela vai cair na real e perceber que tão de tramóia pra vocês."

    i "Tomara..."

    mc "Então quando eu tiver pronto eu te aviso."

    i "Tá legal. Eu vou tá com você."

    mc "Demorou."

    "Agora é só ir até a He Xiangu no portal da Cidade Chinesa."

    "Vou falar com ela e apresentar a Xiang. Isso com certeza vai fazer ela cair na real e perceber que a Cidade Chinesa manipula eles."

    "Se a He Xiangu aceitar a verdade, ela vai convencer todo mundo da mentira e isso vai mudar a Cidade Chinesa pra sempre!"

    "Isso vai ajudar todo mundo de lá... inclusive a [s], a Fen Ju, a [ka]... não dá nem pra acreditar."

    "Bora lá!"

    scene black with dissolve

    "{b}Fale com a He Xiangu no portal de pedra na Cidade Chinesa para continuar a história delas{/b}"

    jump call_cidade

label xiang_escape4:

    "Agora eu tô com a [i]."

    if xiangu_promessa:

        "Eu prometi que só ia voltar aqui com ela. E agora ela tá aqui."
    else:


        "Eu disse que não ia prometer nada, mas acabei voltando com ela..."

    mc "[xu]!"

    scene black with dissolve

    mc "Por aqui."

    i "!"

    mc surpreso "!"

    scene chinatown xiangu_ameaca with vpunch

    xu "O que você tá fazendo aqui?"

    mc envergonhado "Eu quero te mostrar alguém. Abaixa a espada e dá uma olhada nela."

    xu "Hm?"

    scene xiang_xiangu1 with Dissolve(1.0)

    pause

    xu "Quem é essa garota?"

    i "..."

    xu "Eu tenho a impressão que eu te conheço... mas faz muito tempo."

    i "Você é a garota que eles... é isso... só pode ser."

    xu "Quem é você?! Fala logo!"

    i "Eles estavam me preparando para ser a próxima He Xiangu. Eu vivi anos e anos ouvindo a história."

    i "De como ela era boa e protegia nosso povo desde o começo. Como ela era amada e adorada por todos."

    xu "..."

    i "Eu decorei essa história... eles me obrigavam a ficar ouvindo o dia todo, vendo as mesmas imagens."

    i "Eles falaram que eu deveria entender logo quem eu era. Eles me afastaram da família."

    i "Foi horrível tudo isso. Mas a [i] ainda não sabia o que era vida. Tudo parecia normal."

    i "Eles fizeram isso com você também?"

    xu "Esse... é o treinamento que eu tive que passar para recuperar meu poder milenar."

    i "Então é isso... você é aquela menina que chegou depois. Você veio tomar meu lugar."

    xu "M-mentirosa! Eu sou a He Xiangu! Eu não sou a segunda opção!"

    i "Era pra eu estar no seu lugar hoje."

    i "Mas alguma coisa deu errado e eu acabei indo pra outro lugar. Um lugar branco onde eu vivia deitada."

    mc desconfiado "Hm?"

    i "Eu não era a He Xiangu. E você também não é. Eles só querem que a gente acredite nessa história."

    xu "Por que eu acreditaria em você? Só porque tem feições como a minha?"

    mc surpreso "A tatuagem! Mostra a tatuagem pra ela, [i]!"

    xu "Tatuagem?"

    mc normal "Ela tem uma marca dos deuses igual a sua, He Xiangu."

    i "Eu vou mostrar."

    scene xiang_xiangu1 with Dissolve(2.0)

    i "Veja! Você também tem essa marca, não tem?!"

    xu "A lótus... o símbolo da He Xiangu... m-mas... como?"

    mc surpreso "[i]! Você não precisava tirar a blusa pra mostrar! Dava pra ver!"

    i "Garota! Eu tô falando sério! Eu era igual você! A [i] passou pelas mesmas coisas que você!"

    xu "N-não... e-eles mentiram pra mim?"

    i "A [i] não sabe o porquê... mas eles fizeram a mesma coisa com nós duas..."

    xu "Então... tudo o que eu passei..."

    i "Enquanto você não aceitar a verdade, nunca vai conseguir viver sua vida de verdade!"

    i "Essas pessoas não tão nem aí pra gente! Eles criam deuses pra obrigar a gente a fazer o que eles querem!"

    i "A [i] não sabia disso também! Mas a vida no clube e o [mc] mostraram outra vida pra ela! Você pode ver também!"

    "Caraca... a [i] evoluiu bastante desde a primeira vez... ela nem tinha coragem de falar."

    "Agora ela tá mandando a braba na He Xiangu... ela realmente cresceu pra caralho..."

    xu "Nngg... c-como eu posso admitir que tudo o que eu vivi é uma mentira?"

    xu "Que as coisas que me ensinaram eram pra me dominar e doutrinar? I-isso é negar tudo o que eu vivi!"

    i "Eu sei! Não é fácil! Mas você pode conseguir!"

    xu "NÃO!"

    xu "Eu nunca vou acreditar nas suas palavras!"

    xu "Eu entendi... você é meu teste final... você é a versão distorcida de mim. Você é meu lado negro."

    mc preocupado "He Xi-xiangu... o que você tá..."

    scene xiang_xiangu3 with Dissolve(1.0)

    xu "Agora tudo faz sentido. Se eu conseguir matar meu lado negro, finalmente eu poderei voar."

    mc surpreso "N-não faça isso!"

    i "A-agh..."

    mc preocupado "Ela vai te fatiar, [i]!"

    i "Droga... a [i] acha que não foi uma boa ideia falar isso pra ela assim..."

    xu "O mundo tá cheio de impureza. A mão das trevas está em todos os lugares. E eu não posso cair em tentação."

    xu "Mas se eu fizer o que os deuses me pediram e purificar meu corpo de todo o mal, eu vou conseguir."

    mc preocupado "He Xiangu! Pense direito! Fazer o mal pros outros por causa dos deuses?!"

    mc "Você acha que eles realmente querem o mal dos outros?! Os deuses não eram pra ser do bem?!"

    xu "O mal deve ser tratado como mal. Pra ele só existe um caminho. Quem se converte e os inimigos."

    i "Parece que falar não vai resolver..."

    mc surpreso "E você ainda tá sem roupa!"

    xu "{i}fuuuuuuuuu{/i}"

    i "Ela tá se preparando pra atacar."

    i "Essa mulher tá em outro nível. Ela deve ter treinado com essa espada todos os dias por anos."

    mc preocupado "Então sai daí!"

    i "Não dá mais tempo. Se a [i] virar, ela corta a [i] em duas."

    "Eu não devia ter trazido a [i] direto pra cá assim! Talvez eu devesse ter falado com o [chi] antes!"

    i "[mc]... se acontecer alguma coisa com a [i], saiba que você é a pessoa que eu mais gostei até hoje."

    mc preocupado "Não fala isso, [i]!"

    "O que eu podia ter feito de diferente?!"

    xu "AAAAAAHHHHHHHHHHHHHHH!"

    mc "XIAAAANNNNG!"

    scene red with hpunch

    scene xiang_xiangu4 with Dissolve(1.0)

    pause

    mc "X-xiang!"

    mc "O que tá acontecendo!?"

    xu "Morra, infiel! Chega de impureza na minha vida!"

    i "A-agh!"

    mc "Nããããoooo!!!"

    scene black with vpunch

    mc preocupado "Xiang! Não!"

    scene xiang_xiangu5 with Dissolve(1.0)

    xu "Pare! Por favor!"

    i "?!"

    mc surpreso "Xiang! Você tá bem?! Ela não te cortou?!"

    i "Não... parece que não."

    mc "Ela cortou sua calça!"

    xu "Você... como você desviou? Em pleno ar?"

    i "Não sei. Eu só desviei."

    xu "C-como? Eu sou a He Xiangu... eu sou... uma lenda!"

    i "Isso é pra você aprender que nem tudo que as pessoas te falam é verdade."

    xu "Mas o templo... eles disseram que tinham a mensagem dos deuses..."

    i "Eles podem falar o que eles quiserem... não quer dizer que é verdade."

    i "E o problema não foi você. A [i] era igual você até ir pro mundo e conhecer outras pessoas."

    i "Se a [i] nunca tivesse conhecido outras pessoas, outras cabeças, eu seria assim pra sempre."

    xu "Então... é mesmo tudo mentira?"

    "Não acredito... a [i] tá fazendo a cabeça dela..."

    mc zerado "E fazendo todo esse discurso praticamente pelada... como pode?"

    "E a He Xiangu não usa calcinha nem nada? P-pera... O que eu tô pensando?"

    xu "Nada disso faz sentido... eu não tenho como acreditar em vocês assim..."

    xu "Eu cresci ouvindo a mesma coisa das pessoas mais velhas... é impossível pra mim trocar tudo assim."

    "???" "Não há problema algum mudarmos de opinião, jovem. Reconhecer o caminho errado e alterar a direção é um ato de coragem."

    mc surpreso "!!!"

    "???" "Veja só... sorte que eu trouxe este quimono... eu queria dar pra minha neta, mas achei que ela não era a pessoa certa."

    scene black with dissolve

    "..."

    scene xiang_xiangu6 with Dissolve(1.0)

    pause

    mc "[chi]... o que você tá fazendo aqui?"

    chi "Quando eu vi vocês passando em caminho ao templo, reconheci esta jovem de longe. Faz tempo, [i]."

    i "[i] não sabe quem é o senhor."

    chi "Naturalmente. Você era tão pequena. E depois... ninguém podia saber que eu estava envolvido."

    mc "O senhor pode ser mais claro no que você tá falando?"

    chi "O foco agora não sou eu, você ou a garota [i]. Mas esta outra ao lado."

    xu "Eu?"

    chi "É. Você. Não deve ter sido fácil ser derrotada por uma estranha desarmada."

    xu "Veio caçoar de mim, velho?"

    chi "Pelo contrário. O que eu quero dizer é que seria impossível você derrotar essa garota. Mesmo sendo tão habilidosa como é."

    xu "Como é? Por quê?"

    chi "Essa garota passou pela mesma coisa que você. Ela estava sendo preparada para ser a grande He Xiangu, como você foi."

    xu "Isso eles me disseram. Por que eu acreditaria em você?"

    chi "Porque eu escolhi você."

    xu "Me escolheu?"

    mc "V-você escolheu ela pra ser a He Xiangu?!"

    chi "Sim. Na verdade, eu escolhi as duas. Era minha responsabilidade como o mais sábio entre os Escolhidos."

    xu "O senhor?!"

    chi "Eu sei que minha aparência agora não ajuda, mas eu era o responsável por garantir a perpetuidade de nossa cultura."

    chi "Foi essa a missão que eu recebi quando eu nasci. E não foi simples abandonar isso e me tornar o que eu sou hoje."

    "Missão..."

    chi "Mas se eu consegui, você também consegue. Você é uma jovem com um grande futuro pela frente."

    chi "O que você vai fazer agora que conhece a verdade só depende de você."

    xu "Mas... então... se tudo isso é mentira, por que os Escolhidos mentiram pra mim? Por que tudo isso?"

    chi "Essa não é uma pergunta fácil de responder. Pra isso, nós teríamos que voltar até o princípio de tudo."

    menu:
        "A verdadeira história da He Xiangu?":


            mc "Você quer dizer a verdadeira história da He Xiangu?"

            chi "Exato."
        "A gente precisa mesmo?":


            mc "A gente precisa mesmo? Não é óbvio o que aconteceu?"

            chi "O que você diria?"

            mc "Que os líderes da Cidade Chinesa inventaram essa história pra fazer tudo mundo de idiota."

            chi "A lenda dos Imortais é muito anterior a este bairro, [mc]. Seria impossível inventarmos isso."

            xu "Óbvio... e uma história inventada nunca duraria todo esse tempo."

            mc "Então você tá falando que é verdade?"

            chi "Nós temos que ouvir de alguém que lembra dela pra nos contar."
        "Ficar em silêncio":


            "Melhor não me intrometer."

    xu "C-como você pretende isso? Isso aconteceu milhares de anos atrás."

    chi "E mesmo assim alguém aqui conhece ela. Ela só precisa lembrar."

    i "..."

    mc "[i]?"

    i "A [i]?"

    chi "Quem mais? Eu quero que você feche os olhos e toque do quimono que eu trouxe."

    i "Tá..."

    scene black with dissolve

    chi "Agora... aperte ele bem firme. E me fale o que vem na sua cabeça."

    "Que que tá acontecendo aqui?"

    chi "O que você enxerga?"

    i "Huh!"

    i "A [i] vê prédios... casas... mas elas são diferentes..."

    chi "Descreva esse cenário para nós, [i]."

    scene xiangu1 with Dissolve(1.0)

    "{i}Em um dos vilarejos da antiga China, no pé do Monte Penglai, vivia uma pequena comunidade{/i}"

    "{i}Quase todos habitantes eram trabalhadores da terra ou cuidadores de animais vivendo uma vida simples{/i}"

    "{i}A vila era liderada por uma família, que organizava e fazia a distribuição das colheitas{/i}"

    "{i}Conflitos de vários tipos surgiam entre os moradores daquele lugar, o que tornava a vida lá muito difícil{/i}"

    "{i}Homens e famílias se matavam por brigas baratas. E os tempos de seca e os longos invernos tornavam tudo pior{/i}"

    "{i}A família principal, no entanto, ostentava, sempre, grande fartura{/i}"





    scene xiangu2 with Dissolve(1.0)

    "{i}Um dia surgiu uma viajora. Uma garota que chegara de outra parte do país, talvez do mundo{/i}"

    "{i}Ela não era filha de ninguém daquela vila, tampouco parente ou conhecido que fosse{/i}"

    "{i}No começo, poucos tiveram coragem de falar com ela, por mais que sua feição fosse suave e sua voz mansa{/i}"

    "{i}Com o passar do tempo, a garota se mostrou extremamente habilidosa na lavoura e na caça{/i}"

    "{i}Parecia incansável, trabalhando por horas e horas ajudando todos aqueles que precisavam de uma mão amiga{/i}"

    scene xiangu3 with Dissolve(1.0)

    "{i}Não demorou muito para que a jovem se tornasse um símbolo para aquelas pessoas{/i}"

    "{i}Reverenciada por jovens e velhos, a mulher, entretanto, nunca se viu como diferente e continuou trabalhando como sempre{/i}"

    "{i}Ela, porém, nunca entregara o resultado de seu trabalho à família, levando tudo o que coletava diretamente aos moradores{/i}"

    "{i}No começo, o fato passou despercebido de todos, mas quando a notícia que uma nova figura surgia como liderança na vila...{/i}"

    "{i}... eles não aceitaram a ideia e a chamaram para uma conversa. A jovem foi humilde, mas taxativa:{/i}"

    "{i}'Eu não peço nada dos senhores, e portanto não devo nada aos senhores. Apenas me deixem trabalhar'{/i}"

    "{i}Eles tentaram explicar como a vida se dava naquele lugar do mundo, mas com pouco efeito. A jovem não se importava com as regras{/i}"

    "{i}Reconhecendo ser impossível domar o coração da mulher, a família não viu outra alternativa.{/i}"

    scene red with vpunch

    "{i}E empregaram todos seus esforços para assassiná-la{/i}"

    scene xiangu4 with Dissolve(1.0)

    "{i}'Infelizmente foi o único caminho. As pessoas não podem descobrir que elas não precisam de nós'{/i}"

    "{i}Disse um dos líderes da ilha{/i}"

    "{i}'Mas as pessoas amavam ela. O que eles vão fazer quando descobrirem?'{/i}"

    "{i}Respondeu outro membro da família{/i}"

    "{i}A família decidiu que seria prejudicial aos seus interesses perder o afeto dos moradores, então esconderam a morte da jovem{/i}"

    "{i}Disseram que ela estava em uma missão e retornaria depois de um tempo{/i}"

    scene xiangu1 with Dissolve(1.0)

    "{i}Naquela mesma noite uma casa foi atacada durante a noite. Os pais foram mortos e um bebê desapareceu{/i}"

    "{i}E alguns anos depois a jovem retornou de sua missão no monte para a alegria de todos{/i}"

    "{i}Ela estava um tanto diferente, sua voz era menos doce, mas trajava as mesmas roupas e empunhava a mesma espada{/i}"

    "{i}Desta vez, entretanto, ela trazia uma mensagem diferente:{/i}"

    "{i}'Sigam as palavras dos líderes e seremos felizes. Se vocês me amam, obedeçam nossos superiores'{/i}"

    "{i}E todos a seguiram por anos e ela nunca envelheceu, protegendo sempre todas as gerações dos moradores da vila{/i}"

    "{i}Sua lenda se espalhou e ela ficou conhecida como He Xiangu, a primeira Imortal{/i}"

    scene black with dissolve

    scene xiang_xiangu7 with Dissolve(1.0)

    i "Uau... o que foi isso? As palavras só vieram na cabeça da [i]."

    mc desconfiado "Então essa é a história da He Xiangu?"

    xu "Não foi essa a história que eu aprendi."

    chi "Obviamente. Apenas a verdadeira saberia a história real."

    mc "V-verdadeira?"

    xu "Então... você é a verdadeira He Xiangu?"

    i "Claro que não. Eu não sou imortal."

    xu "Então... o que isso quer dizer?"

    chi "A tradição da He Xiangu continuou por todos esses anos e nossos ancestrais trouxeram ela para este lado do mundo."

    xu "Então os Escolhidos tão me usando para manter todos obedecendo?"

    mc "[xu]... não é culpa sua."

    xu "Isso é muita maldade."

    i "Você precisa ver o que você vai fazer agora. Não perca mais seu tempo com eles."

    xu "De modo algum. Eu continuarei aqui. Eu preciso ter certeza do que tá acontecendo."

    i "Então você é mais corajosa que a [i]. Mas não tem muito o que descobrir agora..."

    xu "Eu... eu te agradeço. Por você ter feito isso por mim. Mesmo eu te atacando."

    i "A gente é bem parecida. Tomara que você seja feliz."

    chi "A sua hora de fazer o certo ainda vai chegar. Você ainda é importante aqui."

    xu "Eu ainda não sei o que é verdade e o que é mentira. Eu preciso de um tempo sozinha."

    xu "Uma última coisa que eu acabei não entendendo... a história da He Xiangu é verdade ou mentira?"

    i "Eu acho que é mentira. Mas o velho deve saber melhor."

    chi "Nós temos alguém aqui que pesquisou tudo isso com muito afinco e pode responder você melhor do que eu."

    xu "Quem?"

    mc "E-eu?"

    chi "Claro. Depois de tudo isso, qual a conclusão que você chegou?"

    mc "Hmm..."

    "Eu tô acompanhando a história da Cidade Chinesa faz tempo. Eu escutei o caso de muita gente."

    "Será que eu tenho uma resposta pra isso?"

    chi "Acho que a pergunta central neste caso é... a lenda da He Xiangu e dos Imortais é verdade ou não?"

    menu:
        "A lenda é verdadeira.":


            mc "Pra mim é difícil admitir isso... mas eu sinto que a lenda é verdadeira."

            mc "Os Escolhidos estão usando isso pra se manter no poder do bairro, mas a história é verdadeira."

            mc "Um dia existiu uma He Xiangu e ela foi muito boa pra população daquele lugar."

            mc "Eu não sei se ela era imortal, mas eu acho que os Imortais foram pessoas como ela, que ajudaram seu povo."

            mc "Eles foram tão importantes que deixaram uma marca que dura até hoje. Isso não é ser imortal?"

            chi "Eu não poderia falar melhor... será que foi isso mesmo que aconteceu?"

            mc "É a conclusão que eu vou levar pra mim."
        "Essa lenda é mentira.":


            mc "Eu não acho que é verdade. He Xiangu nunca existiu e isso é uma história que contaram a vocês."

            mc "Os Escolhidos usaram os Imortais pra encher esse lugar de mesticismo e explicar o inexplicável."

            mc "Assim como a família da história que a Xiang contou, eles usam a He Xiangu até hoje pra controlar o povo."

            mc "Quanto mais cedo as pessoas perceberem isso, melhor vai ser pra elas."

            chi "Eu não poderia falar melhor... será que foi isso mesmo que aconteceu?"

            mc "É a conclusão que eu vou levar pra mim."
        "Não faço ideia.":


            mc "Desculpa, [chi], pessoal, mas eu não consegui chegar a uma conclusão."

            mc "Eu tinha certeza que era mentira, mas depois de escutar a [i] e ver ela fazer certas coisas..."

            chi "Hohoho... não precisa se preocupar quanto a isso, jovem. Muitas vezes a verdade é complexa."

            mc "Hmm... é frustrante chegar aqui sem uma resposta, mas acho que é o mais justo."

            mc "Eu espero que eu ainda tenha a chance de descobrir isso."

    xu "Então é isso..."

    i "A [i] acha isso muito complicado, mas eu quero viver minha vida a partir de agora."

    if xiang_casa:

        i "E eu vou começar minha nova vida na casa do [mc]."

        mc "Haha... ok..."

    xu "E eu vou tirar a limpo tudo isso. Encontrar uma resposta que me satisfaça."

    chi "E meu trabalho está quase pronto. Mas eu ainda tenho algumas crianças para salvar."

    chi "Espero que você venha comigo, [mc]. Nosso trabalho ainda não acabou."

    mc preocupado "..."

    scene black with Dissolve(3.0)

    pause

    scene xiang_xiangu8 with Dissolve(1.0)

    "Uma pena que eu não descobri o que a He Xiangu acabou decidindo. Mas parece que nem ela sabe."

    "Imagina construir toda sua vida em cima de uma verdade e depois tudo desabar assim."

    "Mas eu fiquei muito feliz que a gente conseguiu colocar isso na cabeça dela. Pra quem queria me cortar em dois foi um avanço."

    "A [i] também mudou muito desde que a gente se conheceu. Aquela moça calada e medrosa acabou virando uma mulher e tanto."

    "O jeito que ela derrubou a [nora] e venceu a [xu]... parecia que ela tava lutando e dançando ballet ao mesmo tempo."

    "Nem tudo que ela me disse eu entendi... eu ainda acho que tem coisas que eu não descobri..."

    if xiang_casa:

        "Mas agora que ela tá em casa, acho que eu vou ter mais chances de falar com ela."
    else:


        "Uma pena que ela não vai ficar em casa... seria interessante conversar mais com ela."

    "Só que ela também tem que seguir com a vida dela. E seria bacana ela conseguir ir pra China."

    "E eu tenho coisas pra resolver na Cidade Chinesa ainda."

    "A [ka]... a Liling... a [s]... a Fen Ju... o [chi] disse que a gente ainda tem trabalho a fazer."

    "E a Mestra da [s]... o que ela vai fazer quando descobrir o que eu tô causando?"

    "Não quero nem pensar nisso agora..."

    scene black with dissolve

    $ tempo = 3

    jump call_cidade

label xiang_escape_falha:

    $ xiang_fim = True

    "Não era hora de fazer isso!"

    "Não!!! Eu perdi minha única chande de salvar a Xiang!"

    "Não acredito! Xiaaang!!!"

    $ tempo += 1

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
