label natasha_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("na1_save", extra_info="na1_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ natasha_e1 = "iniciado"

    "Será que a [d] vai se apresentar hoje? Tô afim de ouvir uma música de gente chique hoje."

    "Nada de batida, hoje eu tô fino. Quero ouvir alguma coisa com alma, com letra, com sentimento."

    "..."

    scene jazz geral with Dissolve(1.0)

    "..."

    "Merda!"

    "Hoje não tem show da [d]. Meeee.... É triste não ter uma garota linda pra ver... e música boa pra ouvir..."

    mc desconfiado "Hm?"

    scene natasha_jazz with Dissolve(1.0)

    pause

    mc surpreso "!"

    "Quem é essa agora? Que mina linda!"

    "Que as outras não ouçam..."

    "Ela tem bastante estilo também. Deve ser uma das ricaças que se hospedam aqui."

    "Poder conversar com ela seria massa. Até agora eu não conversei com ninguém que realmente tem grana pra se hospedar no cassino."

    mc envergonhado "Não tem nada de errado em uma conversa amistosa, certo?"

    "E talvez possa até rolar um lance mais íntimo..."

    if priscila_namoro:

        "O que eu tô pensando?!"

        "Eu e a [c] tamo firme..."

        "Tenho que pensar muito bem no que eu vou fazer com outras garotas."

    elif sayuri_namoro:

        "O que eu tô pensando?!"

        "Eu e a [s] tamo firme..."

        "Tenho que ver muito bem o que eu vou fazer com outras garotas. Não quero magoar ela."

    elif julia_namoro:

        "O que eu tô pensando?!"

        "Eu e a [g] tamo firme... pelo menos eu acho..."

        "Tenho que ver muito bem o que eu vou fazer com outras garotas. Não quero magoar ela."

    elif maria_namoro:

        "O que eu tô pensando?!"

        "Eu e a [ma] tamo firme..."

        "Tenho que ver muito bem o que eu vou fazer com outras garotas. Não quero magoar ela."

    "Bom... é só uma conversa amistosa. Nada mais que isso."

    "Só que eu vou falar o quê? Caraca, tô parecendo igual aquela noite que eu falei com a [c] no bar pela primeira vez."

    "Mas é pior ainda porque dessa vez eu realmente não tenho motivo nenhum pra falar com ela..."

    menu:
        "Foda-se. Quem não cola não sai da escola":


            $ natasha_evento = 1

            "Não adianta ficar pensando muito. O máximo que pode acontecer é ela começar a gritar e chamar a polícia."

            mc angustiado "!"

            play sound "audio/som_35_passos.mp3"

            "..."
        "Não quero parecer um stalker. Quem sabe outra hora":


            "Melhor deixar pra outra hora. Vai que a gente se encontra em uma oportunidade melhor."

            "Se eu chegar assim ela só vai me achar um escroto."

            $ natasha_falou = True

            jump cassino_jazz

label natasha_evento:

    hide screen cassino_tela

    if natasha_falou:

        "Melhor eu dar um tempo pra ela. Amanhã se pá eu volto."

        show screen cassino_tela
        with dissolve

        pause

    elif natasha_evento == 7:

        scene natasha_jazz with Dissolve(1.0)

        "Eu acho que vou dar um tempo pra ela."

        "A gente avançou muito, mas enquanto a [na] não resolver esse pepino não vai dar pra gente progredir."

        "Será que tem alguma forma de eu ajudar ela nisso?"

        jump natasha_evento2

    elif natasha_evento == 8:

        "Eu ainda não descobri nada sobre o Barão."

        "Ela precisa de ajuda pra descobrir uma forma de falar com ele fora do cassino."

        "Preciso falar com pessoas que talvez tenham alguma relação com o Barão ou que saibam mais sobre a ilha do que eu."

        "Talvez eu precise falar com várias pessoas, mas eu vou descobrir!"

        "Assim que eu encontrar uma dica boa o suficiente, venho e falo com a [na] de novo."

        if natasha_e2 == "chefe":

            "Eu falei com o chefe... mas não foi o suficiente."

            "Agora preciso entrevistar alguém que seja mais próximo do Barão."

            "Será que {b}ela{/b} falaria comigo?"

        elif natasha_e2 == "patricia":

            "Aquela moça que eu sempre encontro na entrada não falou muito..."

            "Talvez eu tenha que falar com alguém de fora do Cassino."

            "Falar com alguém que tenha informações exclusivas sobre as pessoas. Mas quem?!"

        elif natasha_e2 == "fabricio":

            "O [gar] falou um monte de besteira que eu não sei se realmente tem sentido..."

            "Mas ele falou que talvez o próximo passo esteja bem perto..."

            "Será que ele quis dizer aqui mesmo no cassino?"

            "Hmm... tem alguém que não me falou sobre o Barão ainda. Talvez ela..."

        elif natasha_e2 == "ana":

            "A [ana] me ajudou pra caramba."

            "Agora preciso reunir tudo o que eu descobri e confirmar o local encontrando o Barão lá."

            "Preciso ir no local certo, na hora certa."

            "Assim que eu confirmar, vou poder falar com a [na]. Eu sinto que tô muito perto."

            "Não vejo a hora de ver a cara dela quando eu descobrir o que ela precisa."

        show screen cassino_tela
        with dissolve

        pause

    elif natasha_evento == 9:

        jump cassino_jazz



    call checa_logado from _call_checa_logado_5



    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    python:
        if renpy.android:
            natasha_db = PythonSDLActivity.pegaNatasha()

    if natasha_vez < natasha_db:

        "{b}Você já esperou para falar com a [na] [natasha_db] vezes. Mas neste gameplay você falou [natasha_vez] vezes com ela.{/b}"

        "{b}Como não é preciso esperar duas vezes pelo mesmo evento, você pode continuar a história sem esperar novamente.{/b}"

        $ natasha_vez += 1

        python:
            if renpy.android:
                renpy.block_rollback()

        jump natasha_evento_ok

    call checa_tempo from _call_checa_tempo_6

    python:
        if renpy.android:
            ntempo = PythonSDLActivity.checkNtempoNext()

    if not ntempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        "Não quero forçar a barra. Vou dar um tempo e venho falar com ela depois."

        show black with Dissolve(1.0)

        p rindo "O [mc] pode falar com a [na] uma vez a cada 3 horas do mundo real."

        p "Use o app Relógio no celular do [mc] para ver quando será possível falar com ela novamente."

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        label libera_natasha_coins:

            p "Ou você pode liberar o próximo evento agora mesmo usando Celebrity Coins."

        if persistent.coins >= 500:

            p "Liberar o próximo evento usará 500 Celebrity Coins"

            menu:
                "Liberar evento":


                    $ proibido_salvar = True
                    $ show_quick_menu = False

                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaNTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    "{b}Você usou 500 Celebrity Coins para liberar o próximo evento{/b}"

                    $ renpy.block_rollback()

                    hide black with dissolve

                    "Pensando bem, quem não arrisca não petisca. Deixa eu ir falar com ela."

                    "..."

                    jump natasha_evento_continua
                "Agora não. Vou esperar o tempo.":


                    "{b}Você escolheu não liberar o próximo evento{/b}"

                    jump cassino_jazz
        else:


            p lecionando "Você precisa de ao menos {b}500 Celebrity Coins{/b} para liberar o próximo evento."

            p "Você pode comprar Celebrity Coins com dinheiro do {b}seu{/b} mundo."

            p "Assim você pode continuar a história agora mesmo e ainda colabora com o desenvolvimento de CH."

            menu:
                "Ok. Quero comprar.":


                    p rindo "Legal!"

                    call comprar_coins from _call_comprar_coins_4

                    p "Se você comprou, agora pode avançar o tempo usando Celebrity Coins."

                    hide black with dissolve

                    jump libera_natasha_coins
                "A vida é dura. Tô sem grana pra isso agora.":


                    p rindo "Não tem problema."

                    p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais."

                    jump cassino_jazz

    label natasha_evento_continua:

        python:
            if renpy.android:
                renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("natasha_evento","natasha","personagem")

    python:
        if renpy.android:
            PythonSDLActivity.setNtempoNext()
            natasha_vez += 1
            nnext = PythonSDLActivity.pegaNNext()
            renpy.block_rollback()



    label natasha_evento_ok:

        $ natasha_falou = True

    scene natasha_jazz with Dissolve(1.0)

    if natasha_evento > 1 and natasha_evento < 6:

        "Ela tá de novo sentada no mesmo lugar e deve ser o mesmo drink."

    elif natasha_evento >= 6:

        "Então ela continua vindo aqui pro cassino. Que massa."

    if natasha_evento == 1:

        "Tomara que eu consiga desenrolar alguma coisa com ela."

    elif natasha_evento < 6:

        mc preocupado "{i}glup{/i}"





    play sound "audio/som_35_passos.mp3"

    "..."



    if natasha_evento == 3:

        scene natasha_jazz_close with Dissolve(1.0)

        mc normal "Boa noite."

        na "Boa noite."

        mc "Eu só vim dar um alô mesmo. Vou pedir alguma coisa pra mim. O seu parece muito bom."

        na "Ah! Isso aqui? Eu pedi ele uma vez e agora a garçonete acha que é meu preferido..."

        mc normal "Haha."

        na "Olha."

    elif natasha_evento == 4:

        scene natasha_jazz_close with Dissolve(1.0)

        mc charmoso "Boa noite, [na]."

        na "Oi. Curtindo a noite de novo?"

        mc charmoso "Sempre."

        mc "Tô incomodando?"

        na "Não. Pode se sentar."

        mc "Opa."



    if natasha_evento == 0:

        "E agora? Será que eu falo com ela?"

        "Vou falar. Não tem porque não arriscar."

        "E também não adianta ficar pensando muito. O máximo que pode acontecer é ela começar a gritar e chamar a polícia."

        mc angustiado "!"

        $ natasha_evento = 1

        play sound "audio/som_35_passos.mp3"

        "..."

    if natasha_evento == 1:

        $ natasha_evento = 2

        scene natasha_jazz_close with Dissolve(1.0)

        pause

        "Mano, ela é ainda mais linda do que parecia de longe."

        "Ela tá te olhando! Fala alguma coisa, idiota!"

        menu:
            "Boa noite.":


                mc normal "Boa noite."

                na "?"

                mc "..."

                na "??"

                mc surpreso "Ah!"

                mc envergonhado "Você também veio ver o show da [d]?"

                na "Eu pensei que hoje não teria show dela."

                mc normal "Ah! Verdade..."

                na "..."
            "Tá calor aqui, né?":


                $ natasha_seducao += 1

                mc normal "Puxa. Tá quente aqui, não tá?"

                na "Está um pouco, sim. Achei que fosse da bebida."

                mc charmoso "O que você tá tomando?"

                na "Foi uma das moças que trabalham aqui que me deu. Não sei muito bem o que é. Parece que todos os drinks aqui têm nomes estranhos."

                mc normal "É verdade. Cuidado com o 'prego enferrujado'."

                na "Contanto que não tenha um prego dentro de verdade..."

                mc "Sim."

                na "..."
            "Você também gosta de jazz?":


                mc charmoso "Oi. Você também curte jazz?"

                na "Como?"

                mc "Aqui no Jazz Corner toca jazz."

                na "Ah! É verdade. Que desatenção..."

                mc "Pensando muito nas coisas?"

                na "Acho que sim..."

                na "..."

        mc envergonhado "É..."

        mc normal "Eu tava pensando em ver o show da [d], mas acabou que ela não vai se apresentar hoje."

        na "Pois é..."

        mc charmoso "E você? Tá planejando fazer o quê?"

        mc "Sem querer me intrometer. Só por curiosidade pra saber se eu tenho alguma ideia."

        na "Hm?"

        na "Desculpa, o que você disse?"

        mc "Perguntei quais são seus planos. Estou meio sem saber o que fazer agora que não tem show."

        na "Você está em um cassino. Coisas para fazer é o que não falta."

        menu:
            "Infelizmente o dinheiro...":


                mc envergonhado "Até que eu queria, mas cadê o dinheiro?"

                na "Entendo. Nem todo mundo tem dinheiro para jogar fora, certo?"

                mc normal "Disse tudo."

                mc "Parece que a gente ganha o suficiente só pra querer apostar de novo."
            "E dar todo meu dinheiro pro Barão?":


                $ natasha_seducao += 1

                mc desconfiado "E dar meu suado dinheiro pro Barão? Nem fodendo."

                na "{i}Rsrs{/i}... eu entendo."

                mc serio "Essas mulheres vestidas de empregadas, como um grande parque de diversão adulto."

                mc "Eu não concordo com nada disso."

                na "Olha só. E não é que tem alguém que realmente conseguiu quebrar o feitiço?"

                mc charmoso "Haha... tipo isso."
            "E você? Joga?":


                mc charmoso "E você? Joga?"

                na "Não. Não é coisa para mim. Eu sou assalariada e ainda não estou podendo gastar meu pagamento nesse tipo de coisa."

                mc "Mas e a chance de ficar rica?"

                na "Você acredita nisso?"

        na "Com certeza eles usam algum sistema que é muito bem controlado. Eu tenho certeza que existe menos aleatoriedade do que a gente pensa."

        na "Ninguém vai investir milhões em algo desse tamanho e colocar a renda dele baseada em sorte. Você pode ter certeza disso."

        mc desconfiado "Pensando por esse lado realmente faz sentido."

        na "Eu pessoalmente não jogo e não pretendo dar mais dinheiro para eles."

        mc charmoso "Vou pensar nisso."

        na "Bom. Eu vou terminar meu drink e ir embora. Já folguei demais por uma noite."

        mc charmoso "Obrigado pela conversa. Até uma próxima."

        na "Boa noite."

        "Talvez eu consiga falar com ela de novo outro dia."

        "Eu tenho que voltar aqui no {b}Cassino de noite quando NÃO tiver show da [d]{/b}."

        "Essa mulher parece super incrível, além de ser linda. Ela é meio fria, mas eu dou um jeito nisso."

        "Ser um jornalista tem seu lado bom também."

        "Agora é melhor eu picar a mula antes que ela me ache um doido de ficar parado aqui."

        jump cassino_jazz

    if natasha_evento == 2:

        scene natasha_jazz_close with Dissolve(1.0)

        pause

        mc charmoso "Boa noite."

        na "Hm?"

        na "Ah! O rapaz da outra noite."

        mc "Isso isso. E você no mesmo lugar. Não tô vendo nenhum prego enferrujado no copo, então deve ser o mesmo drink também."

        na "Olha só. Você acertou."

        mc normal "Iei! Parabéns pra mim?"

        na "Estou impressionada com sua astúcia."

        menu:
            "Obrigado. Eu sou chamado de 007 da rua.":


                mc tarado "Valeu. Não é à toa que eu sou conhecido como 007 da rua lá onde eu moro."

                na "Não me diga..."

                mc charmoso "Muitos dizem que eu tenho um sexto sentido."
            "Eu tô sentindo uma certa ironia?":


                $ natasha_seducao += 1

                mc envergonhado "É uma certa ironia que eu tô sentindo?"

                na "De forma alguma."

                mc "..."

        na "..."

        "Essa moça não tá dando muito espaço."

        "Ela parece que não tá curtindo muito meu papo."

        "Será que é muito cedo para eu pedir pra sentar com ela?"

        "Mas não adianta eu ficar aqui em pé parecendo um espírito obsessor. E agora?"

        menu:
            "Não posso ter medo. No máximo ela vai negar":


                mc charmoso "Eu vou pedir um drink também."
            "Melhor não acelerar as coisas":


                $ natasha_seducao += 1

                mc envergonhado "Bom, acho que já te incomodei muito. Aproveite seu drink que eu vou pedir um também."

        if natasha_seducao >= 4:

            $ natasha_evento = 3
        else:


            $ natasha_evento = 3

            mc "Daí talvez eu pudesse sentar com você?"

            na "Ah. Eu vou só terminar aqui e já estou de saída. Quem sabe uma outra noite?"

            mc "Entendo. Claro."

            mc "Tenha um bom drink e uma boa noite."

            na "Obrigada. Você também."

            "É. Acho que não rolou."

            "Mas não vou desistir. Eu sou cabeça dura. Você me aguarde, moça maravilhosa do cabelo loiro."

            jump cassino_jazz

    if natasha_evento == 3:

        na "Se você quiser, pode se sentar comigo até terminar sua bebida."

        mc charmoso "Seria um prazer."

        na "Fique à vontade."

        mc "Então com licença."

        scene natasha_sentada_incomodada with Dissolve(1.0)

        pause

        na "..."

        "..."

        "Que merda. Tá um climão."

        "Preciso falar sobre alguma coisa. Mas a situação aqui tá super delicada."

        "Ela sente que ela tá tipo fazendo um favor falando comigo. Se eu acelerar as coisas ela vai só se cansar e me chutar."

        "Tá na hora de baixar o Don Juan e levar a conversa com maestria."

        label natasha_e1_conversa:

            pass

        if natasha_pontos == 0:

            "Certo. Como eu começo?"

        elif natasha_pontos == 4:

            jump natasha_e1_continua
        else:


            "Sobre o que eu falo agora?"

        menu:

            "No que você trabalha?" if not na1_p3:

                $ na1_p3 = True

                mc "E no que você trabalha?"

                if natasha_pontos < 2:

                    na "Não sei se quero falar sobre isso ainda..."
                else:


                    $ natasha_seducao += 1

                    na "Trabalho..."

                mc charmoso "Não precisa ficar assim. Não estou pedindo nenhum segredo de Estado."

                show natasha_sentada_surpresa with dissolve

                na "Por que eu teria um segredo de Estado?"

                mc envergonhado "É só uma forma de falar."

                na "..."

                scene natasha_sentada_falando with dissolve

                na "Seria chato entrar em detalhes, mas posso dizer que eu trabalho como funcionária pública."

                mc surpreso "Então você realmente sabe segredos de Estado!"

                na "..."

                mc envergonhado "Você é uma mulher meio séria, né?"

                na "Acredito que sim... Por que?"

                mc charmoso "Eu não tô falando como algo ruim. Mas estou tentando acostumar com esse seu jeito ainda."

                mc "As pessoas- pelo menos as pessoas que eu conheço- nenhuma delas é séria como você."

                if v15_fim:

                    mc envergonhado "Talvez uma moça lá do trabalho."

                    mc desconfiado "Pensando bem, vocês são um tanto parecidas. Ela também leva o trabalho bem à sério."

                    na "Isso não é nada fora do normal."

                    mc normal "Não sei. Você é séria de uma forma diferente."

                scene natasha_sentada_incomodada with dissolve

                na "..."

                mc desculpa "Desculpa. Não queria falar como um insulto."

                na "Não se preocupe. Esse é o menor dos meus problemas."

                mc "Como assim? Você tá passando por alguma barra?"

                na "Não. Esquece isso."

                mc "Hm... ok."

                "O clima ficou uma merda de novo."

                $ natasha_pontos += 1

                jump natasha_e1_conversa

            "Você tá solteira?" if not na1_p4:

                $ na1_p4 = True

                mc charmoso "E com relação ao amor? Tá saindo com alguém? Você namora?"

                if natasha_pontos < 3:

                    scene natasha_sentada_incomodada with dissolve

                    na "Eu realmente não quero falar sobre a minha vida pessoal com você."

                    mc desculpa "Ah, claro. Desculpa."

                    mc charmoso "Eu só tava querendo puxar assunto."

                    na "Tudo bem. Podemos falar de outra coisa."

                    mc charmoso "Tem uma coisa que eu sei..."
                else:


                    $ natasha_seducao += 1

                    na "Você não acha essa pergunta pessoal demais, não?"

                    mc charmoso "Não falo com segundas intenções e nem pra xeretar. É porque realmente é difícil de entender uma mulher bonita igual você sozinha."

                    show natasha_sentada_surpresa with dissolve

                    na "!"

                    mc desconfiado "Que foi?"

                    na "Nada..."

                    mc charmoso "Pode falar."

                    scene natasha_sentada_pensando with dissolve

                    na "Como você consegue falar algo assim de forma tão casual?"

                    mc desconfiado "Falar o que?"

                    na "O que você acabou de falar."

                    mc "..."

                    mc "Que você é uma mulher bonita?"

                    na "Isso."

                    mc charmoso "Não tô falando nada de mais. Só tô sendo sincero."

                mc "Normalmente garotas bonitas não ficam sozinhas por muito tempo."

                mc desconfiado "Pensando bem, é raro ver as pessoas saindo sozinhas, ponto."

                scene natasha_sentada_falando with dissolve

                na "Acho que você tem razão. Pode parecer um pouco solitário sair de casa sozinho."

                na "Mas eu não vejo você acompanhado. Nem hoje e nem na outra noite."

                mc envergonhado "É verdade. Acho que eu sou meio sozinho..."

                na "No meu modo de ver, as pessoas não gostam de ficar sozinhas porque elas têm problemas com elas mesmas."

                na "O ser humano é uma criatura social. É em sociedade que usamos nossas principais habilidades."

                na "Se os seres humanos não tivessem se aglutinado, provavelmente a raça teria desaparecido."

                mc desconfiado "Do jeito que você tá falando, você meio então é à favor de não ficarmos sozinhos."

                scene natasha_sentada_pensando with dissolve

                na "De forma alguma."

                mc zerado "Mas-"

                na "Não é porque a comunidade nos faz mais fortes, que precisamos estar acompanhados o tempo todo."

                "Ela tá se empolgando e nessa posição o decote dela tá abrindo."

                "Será que se eu der uma olhadinha ela vai perceber?"

                menu:
                    "Olhar para o decote":


                        "Acho que ela nem vai perceber."

                        show natasha_close_busto1 with Dissolve(1.0)

                        pause

                        "Uou. São incríveis."

                        "Bem que nossa conversa podia esquentar um pouco..."

                        mc tarado "..."

                        na "Oi?"

                        mc surpreso "Ah!"

                        hide natasha_close_busto1 with Dissolve(1.0)

                        mc envergonhado "E-eu entendi. Mas! Mas..."
                    "Continuar prestando atenção":


                        $ natasha_seducao += 1

                        "Você não é um tarado, [mc]! Se comporte!"

                        na "Ficar sozinho às vezes é importante para podermos organizar nossos pensamentos."

                        na "A gente precisa aprender a escutar nossa voz também e não só a voz dos outros."

                        mc charmoso "Caraca. Você falou igual uma palestrante agora."

                        na "Me deixa. Você que puxou o assunto."

                mc "Mas eu concordo com você. Ficar sozinho pode até deixar a gente com medo às vezes, mas a gente precisa aguentar."

                na "Mais ou menos isso."

                $ natasha_pontos += 1

                jump natasha_e1_conversa

            "O que você gosta de fazer?" if not na1_p2:

                $ na1_p2 = True

                if natasha_pontos < 1:

                    mc charmoso "O que você curte fazer?"

                    na "A gente nem sabe o nome um do outro ainda. É assim que as pessoas começam as conversas hoje em dia?"

                    mc envergonhado "Haha. Não sabia que tinha uma fórmula."

                    na "..."

                    mc normal "E então?"

                    na "Bom..."
                else:


                    $ natasha_seducao += 1

                    mc charmoso "O que você curte fazer?"

                    na "Eu?"

                    na "Hmm..."

                scene natasha_sentada_falando with dissolve

                na "Meu trabalho ocupa grande parte do meu tempo."

                mc desculpa "Acho que o de todo mundo..."

                na "Acho que sim..."

                mc desconfiado "Você está aqui a trabalho?"

                scene natasha_sentada_incomodada with dissolve

                na "Não. É por outro motivo."

                mc "..."

                na "Mas eu não quero falar sobre isso, tudo bem?"

                mc desculpa "Claro. Desculpa qualquer coisa."

                na "..."

                $ natasha_pontos += 1

                jump natasha_e1_conversa

            "Meu nome é [mc]. Muito prazer." if not na1_p1:

                $ na1_p1 = True

                $ natasha_pontos += 1

                mc envergonhado "Acho que nem perguntei seu nome ainda. Meu nome é [mc]. Prazer."

                $ na_nome = "Natasha"

                na "Pode me chamar de [na]."

                mc normal "Parece nome de uma agente secreta."

                show natasha_sentada_surpresa with dissolve

                na "Como?"

                mc normal "Sei lá. Só me pareceu."

                na "Sei..."

                mc surpreso "Ah!!"

                na "!"

                mc normal "O nome da Viúva Negra não é Natasha?"

                na "Viúva Negra? Quem é essa?"

                mc desconfiado "Aquela dos quadrinhos."

                na "Ah! Sei! É Natasha o nome dela?"

                mc charmoso "Sim."

                show natasha_sentada_pensando with dissolve

                na "Ufa... você me assustou."

                mc desconfiado "Assustei? Por que?"

                na "Esse papo de viúva negra aí."

                mc normal "Haha! Não vai me dizer que você é medrosa."

                na "Um pouco..."

                mc charmoso "Não se preocupe. Seu segredo está seguro comigo."

                na "Obrigada. Você é um cavalheiro."

                jump natasha_e1_conversa

        label natasha_e1_continua:

            mc envergonhado "Acabei fazendo uma entrevista com você e nem pedi bebida."

            mc charmoso "Agora eu vou deixar você sozinha que eu incomodei demais."

            mc "Se eu der sorte- e você azar- eu acabo te encontrando de novo."

            if natasha_seducao >= 8:

                $ natasha_evento = 4

                na "Não está incomodando. Pode ficar e tomar alguma coisa."

                mc charmoso "Eu tô curtindo muito falar com você, mas não quero forçar a barra."

                scene natasha_sentada_preocupada with dissolve

                na "Sendo sincera com você, quando você chegou pensei que fosse só um idiota querendo dar em cima."

                na "Mas eu estava enganada."

                "Estava? Certeza?"

                scene natasha_sentada_sorrindo with dissolve

                na "Você não avançou o sinal e tem conversado direitinho comigo."

                na "Desculpa por julgar você sem saber."

                mc charmoso "Relaxa. Se você pensou isso é porque tem seus motivos."

                na "Pior é que eu tenho, mas não justifica. Você é um cara bacana, [mc]."

                na "Faz tempo que eu não conversava com um homem como você."

                mc envergonhado "Agora é você que tá falando coisa que dá vergonha."

                na "Olha aí. Temos até algo em comum."
            else:


                $ natasha_evento = 4

                na "Eu também vou terminar aqui e ir para casa."

                na "Boa noite. A gente se vê."

                mc "Boa noite, [na]."

                jump cassino_jazz

    if natasha_evento == 4:

        $ natasha_evento = 5

        mc charmoso "Desculpa perguntar isso assim, mas o que você vem fazer aqui sozinha à noite?"

        scene natasha_sentada_incomodada with dissolve

        na "Você é um stalker agora?"

        mc envergonhado "Não! Haha! Só curiosidade mesmo."

        na "E você? O que vem fazer aqui?"

        menu:
            "Eu perguntei primeiro.":


                $ natasha_seducao += 1

                mc charmoso "Ei! Não é justo. Eu perguntei primeiro."

                na "Não importa. Você é um cavalheiro e vai responder antes."

                mc charmoso "Eu sou, sim, um cavalheiro, e você é uma dama, mas aqui não tem essa, não. Direitos iguais."

                mc charmoso "Eu perguntei antes, você responde antes."

                na "Então o homem tem personalidade."

                na "Tudo bem..."
            "Quem sabe a gente encontra uma garota linda sozinha.":


                $ natasha_seducao += 2

                mc charmoso "Bom, eu perguntei antes, mas vou ser um cavalheiro e responder."

                mc "Eu gosto de conversar, trocar ideia, conhecer novas pessoas."

                mc "A gente nunca sabe quando pode aparecer uma garota linda sozinha tomando um drink."

                scene natasha_sentada_surpresa with dissolve

                na "..."

                mc charmoso "Pra mim, uma boa conversa com alguém interessante é a melhor forma de passar a noite."

                mc charmoso "Nem preciso dizer que acertei o jackpot esta noite, né?"

                if natasha_seducao >= 6:

                    scene natasha_sentada_interessada with dissolve

                    na "Você realmente não tem problema em falar essas coisas, né?"

                    mc charmoso "Como eu sempre falo, só estou sendo sincero."

                    mc "Você não é só linda, você é interessante, e sabe conversar."

                    na "Tenho que admitir que você também é interessante..."

                    mc "Que bom."
                else:


                    na "Você não gosta de perder suas chances, né?"

                    mc "Com certeza. Quando eu encontro alguém interessante, não posso marcar bobeira."

                    na "E você é bem aberto quanto a isso."

                    mc "Sou só um cara sincero."
            "Eu gosto da vida noturna.":


                mc charmoso "Eu sou atraído pela vida noturna. As músicas, a luz, a bebida, o clima."

                scene natasha_sentada_pensando with dissolve

                na "Isso tudo é um pouco demais pra mim. Eu prefiro algo mais na minha."

                mc charmoso "Isso explica porque você tá aqui sozinha."

                mc envergonhado "E eu aqui te incomodando."

                na "Já falei que não é incômodo. Companhia nem sempre é ruim."

                mc charmoso "Que bom."

        scene natasha_sentada_preocupada with dissolve

        na "Estar aqui no cassino tanto hoje como nas outras noites tem a ver com meu trabalho."

        mc desconfiado "Sério?"

        mc charmoso "Parece o tipo de trabalho que eu adoraria ter que fazer."

        na "Não é bem assim. Eu até gostaria de te contar, mas a gente mal se conhece."

        mc normal "Por mim esse não é o problema."

        na "Não? E por que?"

        mc charmoso "Eu adoraria conhecer você melhor."

        scene natasha_sentada_pensando with dissolve

        na "Você parece uma pessoa bem cuca fresca."

        mc desconfiado "Como assim? Cuca fresca?"

        scene natasha_sentada_sorrindo with dissolve

        na "{i}Rsrs{/i}"

        na "Não é nada. Me desculpa."

        mc desconfiado "?"

        na "Acho que alguns trabalhos são mais pesados do que outros. É isso que quero dizer."

        mc zerado "Você não faz ideia do que meu trabalho me faz fazer."

        scene natasha_sentada_falando with dissolve

        na "E sobre o que é seu trabalho? O que você faz além de abordar mulheres sozinhas no cassino?"

        mc concentrando "Pelo que eu me lembre das minhas tarefas, é praticamente isso."

        na "Engraçadinho. Estou falando de verdade. Qual é seu trabalho?"

        mc envergonhado "Bom, eu sou um jornalista..."

        na "Puxa, [mc]. Isso é interessante."

        mc "Nem tanto. Eu trabalho em uma revista sobre famosos."

        na "Ah! Eu sei."

        na "Seu chefe e a [jc] são bem conhecidos."

        mc "Verdade?"

        na "Pensando bem no seu nome agora... você é o [mcc], né? Eu já li matérias que você descobriu."

        mc charmoso "Opa. É uma honra."

        scene natasha_sentada_surpresa with dissolve

        na "Seu trabalho também parece bem estressante."

        mc zerado "Nem fala. O que esse povo apronta pra mim não é fácil, [na]."

        na "Só que você está ficando famoso no meio. Nem faz tanto tempo assim que você começou e muitos já conhecem seu nome."

        mc desconfiado "Você acha?"

        na "Sim. E não falo só de mim. Muitos dos meus parceiros já comentaram sobre você por algum motivo."

        "Parceiros? Muitos? O que ela quer dizer?"

        na "Você está em uma posição muito interessante, tendo acesso a informações privilegiadas."

        mc envergonhado "E por que isso seria interessante pra qualquer pessoa que não trabalhe com fofoca?"

        na "Você tá brincando?"

        scene natasha_sentada_falando with dissolve

        na "Existe muitos outros que se benificiariam de informações como essas."

        na "Principalmente quando são informações que envolvem figurões da cidade."

        mc desconfiado "Ainda não entendi. Quem poderia usar essas informações?"

        na "Você não consegue pensar em ninguém?"

        mc concentrando "..."

        "O que será que ela quer dizer?"

        "Pra quem será que essas informações seriam importantes além de revistas, sites e tals?"

        mc desconfiado "Não consigo mesmo."

        scene natasha_sentada_incomodada with dissolve

        na "Tudo bem."

        na "Desculpa ficar insistindo."

        mc charmoso "Relaxa."

        mc "Chega de falar de trabalho."

        mc "O que você curte de música? Provavelmente você gosta de jazz."

        scene natasha_sentada_falando with dissolve

        na "Pra falar a verdade eu não sou muito de ouvir música."

        mc desconfiado "Como assim?"

        na "Eu não escuto música. Não tenho banda preferida, ou estilo musical que eu acompanho."

        na "Normalmente eu só ligo na rádio e na maioria das vezes é pra ouvir notícias."

        mc preocupado "Nossa..."

        na "Isso é muito ruim?"

        menu:
            "Com certeza. Você é uma aberração.":


                $ natasha_seducao += 1

                mc surpreso "Óbvio! Você é uma aberração!"

                na "..."

                mc charmoso "Você sabe que eu tô brincando."

                na "Não sei, não."

                mc "Sei lá. É que música é tipo algo espiritual. Dependendo da música que você gosta, a gente pode saber mais sobre a gente mesmo."

                na "Não me diga... E você acredita em horóscopo também."

                mc zerado "Tô falando sério..."

                mc charmoso "Você é uma mulher séria, muito bem resolvida, com muita classe."

                mc "Eu diria que você gosta de... musicais tipo Os Miseráveis. Ou músicas românticas igual Frank Sinatra."

                na "Hmm..."

                scene natasha_sentada_sorrindo with dissolve

                na "Parecem boas sugestões, mas eu não sei. Vou baixar e ouvir. Se eu realmente gostar, vai ser incrível."

                mc charmoso "Eu sei que você vai gostar. Eu tô vendo nos seus olhos."

                na "Meus olhos? Sei..."

                mc charmoso "..."

                na "Mas não vou esquecer que você me chamou de aberração."
            "Claro que não. Cada um gosta do que gosta.":


                mc envergonhado "Não, não. Imagina. Cada um gosta de uma coisa. E daí que você não curte música?"

                na "Eu tô sentindo um pouco de ironia no seu tom."

                mc "Claro que não!"

                na "Hmm..."
            "Assim... é um pouco triste, né?":


                mc envergonhado "Assim, é um pouco triste, né? Parece que você perdeu a alma."

                na "Que exagero..."

                mc normal "Música é tipo a essência da alma."

                na "Você tá querendo dizer que eu estou morta por dentro?"

                mc envergonhado "..."

                na "Absurdo..."

        mc feliz "Haha! Não precisa ficar preocupada assim."

        na "Não sei. Depois de uma dessas às vezes é até bom repensar sobre a vida."

        mc charmoso "Ah tá. Você também é bem sarcástica."

        scene natasha_sentada_sorrindo with dissolve

        na "Eu não. Só tô sendo sincera."

        mc charmoso "Beleza..."

        mc concentrando "Agora acho que vou nessa."

        if natasha_seducao >= 6:

            na "Mas já? Achei que não fosse do seu feitio deixar uma garota sozinha."

            mc charmoso "Sair na hora certa também faz parte da conquista."

            scene natasha_sentada_meudeus with dissolve

            na "Se você diz, eu acredito..."

            mc charmoso "Você é uma companhia incrível, [na]. Espero que a gente possa se ver outra noite."

            na "Eu vou estar sempre aqui pelos próximos dias. Você sabe onde me encontrar."

            mc normal "Boa noite."

            na "Boa noite, [mc]."
        else:


            na "Eu vou terminar minha bebida e sair também."

            mc charmoso "Mas eu estou sempre por aqui. Quem sabe a gente não se encontra de novo."

            na "Legal. Boa noite, [mc]."

            mc "Boa noite, [na]."

        scene jazz corner with Dissolve(1.0)

        "Ufa. Minha conversa com a [na] rendeu mais do que eu imaginava."

        "Ela já não tá mais fria igual no começo."

        "Apesar que eu ainda não consegui descobrir o que tá rolando com ela."

        "Minha curiosidade jornalística não vai deixar eu só esquecer isso. Tenho que descobrir o que ela faz aqui sozinha toda noite."

        "Hmm..."

        jump cassino_jazz

    if natasha_evento == 5:

        $ natasha_evento = 6

        scene jazz corner with Dissolve(1.0)

        "Opa! Tem alguém chegando."

        mc surpreso "!"

        scene natasha_diana_jazz with Dissolve(2.0)

        pause

        mc desconfiado "Hm?"

        "[d]!?"

        "O que será que elas tão conversando?"

        menu:
            "Tentar ouvir a conversa":


                $ natasha_xeretou = True

                "O duro é que não tem onde me esconder aqui. Vou ficar olhando pro outro lado e fingindo que nem vi elas."

                mc zerado "Obviamente que não vai funcionar, mas foda-se."

                "Dizem que a curiosidade matou o gato. Se eu morrer hoje..."

                "..."

                na "{size=17}...sabe que não precisa passar por isso.{/size}"

                d "{size=17}Eu sei, obrigada.{/size}"

                na "{size=17}Então?{/size}"

                d "{size=17}Vai ser mais fácil assim. Não se preocupe.{/size}"

                na "{size=17}Você não confia na gente? Não confia em mim?{/size}"

                d "{size=17}Isso é maior que sua insegurança, [na].{/size}"

                na "{size=17}Não estou falando de mim! Isso aqui é sobre você!{/size}"

                d "{size=17}Eu sei. Desculpa.{/size}"

                na "{size=17}A gente não sabe até onde ele vai com você. Só ver as outras garotas.{/size}"

                d "{size=17}Acho que ele não tem coragem de chegar a isso.{/size}"

                na "{size=17}Eu não teria tanta certeza se fosse você.{/size}"

                d "{size=17}...{/size}"

                d "{size=17}Mesmo assim eu prefiro que continue assim. Além de que agora não são só vocês do meu lado.{/size}"

                na "{size=17}Você tá falando sério? Você realmente confia nele?{/size}"

                d "{size=17}Shh!{/size}"

                na "{size=17}Ah! Verdade.{/size}"

                d "{size=17}Vou pro quarto. Boa noite, [na]. E obrigada de novo por tudo. Você sabe o quanto você é importante pra mim.{/size}"

                na "{size=17}Não faço mais que minha obrigação.{/size}"

                d "{size=17}Até outro dia.{/size}"

                na "{size=17}Até.{/size}"
            "Deixar elas conversarem em paz":


                "Não é legal se intrometer nas coisas assim. Além de ser falta de cavalheirismo, é coisa de pessoa xereta."

                "Vou só esperar elas conversarem. Hmm... tem aquele bar também. Vou descer."

                play sound "audio/som_35_passos.mp3"

                "..."

                scene jazz_bar angulo2 with Dissolve(1.0)

                "Então a [na] conhece a [d]. E por que será que ela vem aqui."

                if not gold_card:

                    ate "Boa noite, senhor."

                    mc surpreso "Eita!"

                    mc desculpa "Boa noite."
                else:


                    ate "Boa noite, senhor [mc]."

                    mc surpreso "Eita!"

                    mc desculpa "Boa noite, [ate]."

                show atendente cassino_contrariada with dissolve

                ate "Aconteceu alguma coisa?"

                mc envergonhado "Ah! Não... Só tava pensando aqui."

                ate "Certo..."

                mc desconfiado "E por que você tá aqui? Agora você atende neste bar?"

                ate "Às vezes eles me tiram da recepção e me mandam pra cá."

                mc normal "Entendi."

                menu:
                    "Eu gostei da mudança. Assim te vejo mais.":


                        $ atendente_seducao += 1

                        mc charmoso "Eu gostei. Assim te vejo na entrada e aqui também."

                        show atendente cassino_timida with dissolve

                        ate "Assim você me deixa sem jeito, senhor."

                        ate "Eu fico feliz que o senhor goste da minha presença."
                    "Quem que organiza vocês aqui?":


                        mc desconfiado "E quem que organiza vocês no cassino? Tem tipo um chefe das garotas?"

                        ate "Isso. Nós temos um gerente do cassino. Ele é responsável por quase tudo por aqui."

                        mc "Ele parece ter bastante poder."

                        ate "Sim. Ele reporta tudo o que acontece diretamente pro Barão as pessoas dizem."

                        mc charmoso "Obrigado. Desculpa a xeretice."

                        ate "Não tem problema. Estou aqui pra servir o senhor."

                ate "Meu trabalho é sempre fazer os senhores se sentirem bem."

                ate "QUALQUER coisa que precisar, é só me falar, tudo bem?"

                mc charmoso "Qualquer coisa mesmo?"

                ate "Qu-qualquer... Estou à sua disposição."

                mc "Ok. Temos que conversar mais vezes."

                ate "Si-sim..."

                "Acho que deu o tempo pra elas conversarem."

                mc charmoso "Vou subir. Boa noite e bom trabalho."

                ate "Até mais, senhor."

                play sound "audio/som_35_passos.mp3"

                "..."

        scene jazz corner with Dissolve(1.0)

        "..."

        scene natasha_jazz_close with Dissolve(1.0)

        mc charmoso "Boa noite, [na]."

        na "Boa noite. Tudo bem, [mc]?"

        mc "Sim. E você?"

        na "Tudo bem."

        mc "Posso sentar?"

        na "Claro. À vontade."

        if natasha_xeretou:

            scene natasha_sentada_incomodada with dissolve

            na "Eu vi que você estava bisbilhotando minha conversa com a [d]."

            mc envergonhado "Ah! Imaginei..."

            na "E mesmo assim ficou ouvindo."

            mc "A curiosidade foi maior. Perdão."

            na "Deu pra escutar alguma coisa?"

            mc desculpa "Um pouco, mas nada que quis dizer algo."

            na "Que bom."
        else:


            $ natasha_seducao += 2

            scene natasha_sentada_sorrindo with dissolve

            na "Eu vi que você chegou enquanto eu conversava com a [d]. Obrigada por deixar a gente conversar."

            na "Imagino que seja complicado para um paparazzo."

            mc envergonhado "Nem fala..."

            na "Mas eu achei muito bacana de sua parte, de verdade. Não imaginei que você aguentaria."

            mc zerado "Ei..."

            scene natasha_sentada_meudeus with dissolve

            na "{i}Rsrs{/i}"

            na "Desculpa. Mas a gente pode dizer que eu caí do cavalo."

            mc charmoso "E caiu mesmo."

        mc desconfiado "Mas é algo que eu não possa saber?"

        scene natasha_sentada_falando with dissolve

        na "Assim..."

        na "A [d] disse que vocês se conhecem, né?"

        mc normal "Sim."

        na "Ela inclusive disse que você presenciou uma cena um pouco problemática."

        "Será que ela tá falando daquela noite que o Barão tratou mal a [d]?"

        "Mas por que a [d] contaria isso pra [na]? Será que elas são tão próximas assim?"

        na "[mc]?"

        mc surpreso "Si-sim!"

        menu:
            "Foi algo envolvendo o Barão...":


                mc desculpa "Foi algo envolvendo o Barão uma noite aí, mas não foi nada de mais."

                na "Sei. Foi o que ela me disse mesmo."

                mc "Mas ela nem ligou, então eu deixei quieto."
            "Não foi nada...":


                "Não sei se eu confio na [na] dessa forma ainda."

                mc desculpa "Não foi nada que mereça ser mencionado."

                na "Certeza?"

                mc "Sim. É coisa da [d]."

        na "Entendo..."

        scene natasha_sentada_pensando with dissolve

        na "Eu sei que pode parecer estranho, mas eu e a [d] estamos trabalhando juntas em algo."

        na "Ela disse que eu posso confiar em você, mas eu ainda não tenho certeza disso."

        mc serio "Como assim? Por que, não?"

        na "Por favor, não tome isso como uma injúria."

        mc "Alguém diz que você não é confiável. Você quer que eu veja isso como um elogio?"

        scene natasha_sentada_falando with dissolve

        na "Eu sei. Você tem todo o direito de não concordar, mas é um requisito do meu trabalho."

        na "Se eu confiasse em todo mundo, provavelmente eu não poderia atuar como eu atuo."

        mc desconfiado "Isso é muito vago. Você só tá se enrolando."

        scene natasha_sentada_incomodada with dissolve

        na "Merda..."

        mc preocupado "Olha. Não tô falando isso por criancice."

        na "Sei..."

        mc serio "Pra mim a [d] é uma amiga."

        if diana_e2 == "seducao" or diana_e3 == "seducao":

            mc serio "Talvez até mais do que isso."

            na "?"
        else:


            $ natasha_seducao += 1

            mc serio "Eu conversei a sério com ela e não tem nada a ver com meu trabalho."

            na "..."

        mc "Pra mim é importante entender o que tá havendo com ela."

        mc desculpa "E agora que eu tô conversando com você, eu queria que você confiasse em mim, poxa."

        scene natasha_sentada_surpresa with dissolve

        na "Que eu confiasse em você?"

        na "Por que você se importaria com o que eu acho de você?"

        menu:
            "Porque no fundo eu sou um cara sério.":


                $ natasha_seducao += 1

                mc serio "Porque eu sou um cara sério. Não quero que os outros fiquem me julgando como um mentiroso que não dá pra confiar."

                mc "Isso é realmente algo que eu não brinco."

                scene natasha_sentada_sorrindo with dissolve

                na "Entendi. Desculpa. Eu também ficaria irritada se me falassem algo assim."

                na "Às vezes eu não consigo pensar se o que eu falo vai incomodar alguém."

                mc desculpa "Tudo bem."

                mc desculpa "Você é uma mulher direta. Eu acho isso muito especial, ainda mais nos dias de hoje."
            "Porque eu quero ajudar a [d].":


                mc serio "Porque eu também quero ajudar a [d]."

                mc "Se vocês estão fazendo algo que vai ajudar ela a realizar o que ela tá planejando, também quero fazer parte."

                mc "Não quero ser deixado de lado só porque você acha que eu não sou 'confiável'."

                scene natasha_sentada_preocupada with dissolve

                na "Entendi. Desculpa. Eu também ficaria irritada se me falassem algo assim."

                na "Às vezes eu não consigo pensar se o que eu falo vai incomodar alguém."

                mc desculpa "Tudo bem."

                mc desculpa "Você é uma mulher direta. Eu acho isso muito especial, ainda mais nos dias de hoje."
            "Porque eu achei você uma garota interessante.":


                $ natasha_seducao += 2

                mc desculpa "Ué. Sei lá. Eu te achei uma garota interessante. Eu só queria que você me achasse um cara legal também."

                scene natasha_sentada_sorrindo with dissolve

                na "Interessante?"

                mc desculpa "Você sabe conversar. Parece uma mulher decidida, adulta. Seu jeito até me parece um pouco a [d]."

                mc "Você tem classe e, não quero ficar repetindo, mas você é linda. Eu queria que você ficasse impressionada comigo assim."

        if natasha_seducao >= 9:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("natasha1_seducao","natasha","personagem")

            $ natasha_e1 = "seducao"

            scene natasha_sentada_interessada with dissolve

            na "[mc]."

            mc serio "Que foi?"

            na "Por que você faz isso? É de propósito?"

            mc "O que você quer dizer?"

            na "Você fica falando essas coisas, sobre eu ser bonita e diferente, sei lá, especial."

            na "Você não percebeu que eu fico sem jeito?"

            mc charmoso "Mas você sabe por que eu falo essas coisas, né?"

            na "Eu não estou acostumada com flerte e esse tipo de conversa. Eu tento ao máximo me manter séria, mas você continua com isso."

            mc charmoso "E qual é o problema de uma conversa com segundas intenções? Você não precisa fazer nada que você não quiser."

            na "Eu sei, mas é que- sei lá- eu não me sinto bem nesses casos."

            na "Não é que você esteja me chateando, mas essa situação... tipo..."

            mc "Calma. Respira. Posso sentar do seu lado?"

            na "Pode. Mas por que?"

            mc "Eu vou te explicar um negócio e não quero falar alto."

            na "T-tá. Mas sem graça."

            mc "Claro."

            "..."

            scene natasha_close_normal with Dissolve(1.0)

            pause

            "Então é isso. No fundo a [na] não tem experiência nenhuma com esse tipo de coisa."

            "Ela se esforçou pra manter a pose, mas acho que eu apertei demais."

            mc charmoso "Olha. A gente é adulto. E é normal a gente sentir algo diferente quando dois adultos estão conversando e rola uma química."

            mc "Você mexeu comigo. E eu queria que você sentisse o mesmo."

            mc "Eu não sou um cara querendo se aproveitar de você. Eu só queria que você sentisse o mesmo que eu tô sentindo."

            na "Eu não tenho experiência com isso, [mc]. Quase ne-nenhuma..."

            mc "Não tem problema. Você é uma mulher incrível. Eu te disse. E daí que você não tem experiência com essas coisas?"

            scene natasha_close_interessada with Dissolve(1.0)

            pause

            na "Eu também achei você um cara especial. Fazia muito tempo que eu não sentia isso."

            na "Fiquei um pouco nervosa. Mas você tá sendo muito legal comigo."

            na "Eu..."

            "Opa. Ela tá se inclinando e nem tá percebendo o decote..."

            "Será que... Acho que ela nem vai reparar... e do jeito que as coisas tão, ela nem vai ligar."

            menu:
                "Olhar para o busto da [na]":


                    "Não aguento!"

                    scene natasha_close_busto2 with Dissolve(1.0)

                    pause

                    "Uou... incríveis."

                    "O que eu não daria pra enfiar minha cara no meio deles..."

                    na "[mc]?"

                    mc surpreso "Oi!"

                    scene natasha_mc_desculpa with vpunch

                    na "Me desculpa! Eu não sei o que eu tava pensando!"

                    mc preocupado "Não, [na]! Calma!"

                    na "Eu não tô pronta pra uma coisa assim! A gente se fala outra noite!"

                    scene jazz corner with hpunch

                    mc angustiado "[na]!"

                    "Merda! O que aconteceu?!"

                    "Será que eu estraguei tudo? Mas eu só desviei o olhar alguns segundos..."

                    "O que será que foi?"

                    "Que saco..."

                    jump cassino_jazz
                "Manter o foco nos olhos dela":


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("natasha1_beijo","natasha","personagem")

                    $ na1_beijo = True

                    "Não tenho nem que pensar. A mina já tá mó nervosa. Não vou causar mais ainda."

                    na "Não sei se eu estou pronta pra algo assim."

                    mc charmoso "Ninguém nunca tá pronto 'pra algo assim', [na]."

                    mc "A gente só deixa as coisas acontecerem."

                    mc "Esquece."

                    na "Mas eu tô com tanta vergonha..."

                    mc "Não pensa nisso. Só fecha os olhos. Me dá sua mão."

                    scene black with dissolve

                    "..."

                    scene natasha_mc_beijo with Dissolve(2.0)

                    pause

                    "Hmm..."

                    "Ela parecia tão nervosa, mas o beijo dela não tem um pingo de medo."

                    "É como se ela tivesse certeza de que tá fazendo o que quer fazer."

                    na "Você parece mais nervoso do que eu."

                    mc "Acho que eu tô mesmo..."

                    na "Você tá se saindo bem. Se acalma."

                    "Maldita..."

                    scene natasha_close_normal with Dissolve(1.0)

                    na "Foi melhor do que eu imaginei."

                    "Ela parece tão diferente."

                    "Será que ela realmente tava nervosa?"

                    mc charmoso "Mereci até um elogio?"

                    na "Sim. Você se comportou como um homem de verdade."

                    mc safado "A gente não precisa parar só com um beijo."

                    scene natasha_close_interessada with dissolve

                    na "Também acho."

                    na "Eu tenho um quarto aqui no hotel do cassino. Quer passar lá?"

                    mc safado "Com certeza."

                    na "É o quarto-"
        else:


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("natasha1_amizade","natasha","personagem")

            $ natasha_e1 = "amizade"

            scene natasha_sentada_meudeus with dissolve

            na "Sabe, [mc]... você é um cara muito diferente do que eu pensei que fosse a princípio."

            na "Eu acho que eu já te falei isso na outra noite, mas eu realmente pensei que você fosse um babaca querendo um alvo fácil pra comer."

            mc zerado "Ei..."

            na "{i}Rsrs{/i}"

            scene natasha_sentada_preocupada with dissolve

            na "Eu me sinto uma boba agora por pensar isso de você."

            na "Eu fui muito mesquinha e, na verdade, eu acho que me senti superior a você porque você veio falar comigo."

            na "Só que, se você pensar bem, ir falar com alguém que você não conhece é um ato muito corajoso."

            na "Parece que sempre quem vai atrás fica do lado vulnerável. E a pessoa procurada se acha importante demais."

            scene natasha_sentada_sorrindo with dissolve

            na "Mas isso é só um pensamento pretensioso, você não acha?"

            na "Quem se arrisca e vai atrás é quem é o verdadeiro vencedor. Quem fica sentado só sendo procurado não entende isso."

            na "E ainda mais nesse tempo que a gente vive!"

            na "Veja como paredes que enclausuravam homens e mulheres em seus papéis estão ficando cada vez mais frágeis."

            na "Hoje em dia não tem mais por que uma mulher ficar sentada esperando. Se a gente gosta de alguém a gente precisa ir atrás."

            na "E você fez isso. E desculpa por quase dar uma palestra aqui."

            na "Mas só estou falando isso tudo pra você saber que eu admiro muito você. E eu fui uma idiota me achando superior."

            mc charmoso "[na]..."

            scene natasha_sentada_preocupada with dissolve

            na "Você tem todo o direito de ficar chateado comigo. Me desculpa."

            mc envergonhado "Eu fico feliz de você reconhecer a dificuldade que é iniciar um papo..."

            mc charmoso "Mas em nenhum momento eu senti que você tava se achando. Você só tava com um pé atrás. Só isso."

            na "[mc]..."

            scene natasha_sentada_meudeus with dissolve

            na "Obrigada por ser tão legal. Acho que você é o homem mais maduro que eu já conheci..."

            mc envergonhado "Não precisa vir com sarcasmo também."

            na "Estou falando sério, bobo."

            na "E eu acho que pode rolar até algo en-"

        $ renpy.vibrate(1)

        play sound "audio/som_3_celular.mp3"

        mc desconfiado "Hm?"

        na "É o meu."

        scene jazz corner with Dissolve(1.0)

        pause

        scene natasha_mc_desculpa with Dissolve(1.0)

        na "Infelizmente vou ter que resolver um negócio urgente, [mc]."

        na "Obrigada pela companhia. Eu acho que vou ter que continuar vindo pro cassino durante a noite, então a gente ainda vai se ver."

        mc preocupado "Mas o qu-"

        na "Desculpa. Mas eu tenho que resolver isso agora. Você sabe onde me encontrar. Boa noite."

        play sound "audio/som_35_passos.mp3"

        scene jazz corner with Dissolve(1.0)

        mc desconfiado "O que foi isso bem agora?"

        mc zerado "Por que eu tenho a impressão que algo sempre atrapalha quando eu tô quase nos finalmentes com alguém?"

        "Que merda..."

        jump cassino_jazz

    if natasha_evento == 6:

        $ natasha_evento = 7

        scene natasha_jazz_close with Dissolve(1.0)

        mc charmoso "Boa noite, [na]."

        na "Oi, [mc]. Senta aí."

        mc "Com licença."

        scene natasha_sentada_sorrindo with dissolve

        na "Tudo bem com você?"

        if natasha_e1 == "seducao":

            "Depois do que aconteceu ontem, nem sei como falar com ela..."

            mc envergonhado "Tudo legal, e você?"
        else:


            "Ontem ela se abriu pra caramba comigo. Dá pra ver que ela tá bem diferente."

            mc normal "Tudo bem. E você como tá?"

        na "Tudo legal."

        mc desconfiado "E aí? O que aconteceu ontem?"

        scene natasha_sentada_incomodada with dissolve

        na "Ah. Desculpa ter saído daquele jeito. Eu precisava resolver um problema envolvendo trabalho."

        mc preocupado "Isso acontece sempre?"

        na "Sabe... na verdade sim. A qualquer momento eles podem me chamar."

        mc desculpa "Entendo."

        scene natasha_sentada_preocupada with dissolve

        na "Só queria que você soubesse que você não fez nada errado ontem."

        na "Eu realmente tive que atender um chamado do trabalho."

        scene natasha_sentada_meudeus with dissolve

        na "Gostei muito da nossa noite ontem..."

        if na1_beijo:

            "Acho que ela tá falando do nosso beijo."

            mc safado "Eu também gostei muito."
        else:


            mc normal "Eu também gostei."

        na "Que bom."

        na "E eu não quero só ficar esperando você tomar a dianteira."

        scene natasha_sentada_sorrindo with dissolve

        na "Eu quero conhecer mais você. Quem sabe a gente possa até se encontrar em outros lugares."

        mc normal "E tomar outra coisa?"

        na "{i}Rsrs{/i}... Sim! Eu estou precisando experimentar outros drinks urgente."

        mc normal "Combinado."

        mc charmoso "Onde você quer ir hoje?"

        scene natasha_sentada_falando with dissolve

        na "Hm.. na verdade eu não vou poder hoje."

        mc desculpa "Sério?"

        na "Nosso passeio vai ter que esperar um tempo."

        na "Eu preciso resolver um assunto aqui no Cassino do Barão antes."

        mc desconfiado "Que assunto?"

        scene natasha_sentada_preocupada with dissolve

        na "Desculpa, mas eu não posso te falar."

        mc serio "..."

        na "Não é que eu não confie em você. Mas são determinações do meu trabalho."

        mc desculpa "Ok. Eu acredito em você."

        na "Obrigada."

        mc "Mas eu ainda não sei no que você trabalha."

        scene natasha_sentada_surpresa with dissolve

        na "Ah! É..."

        na "Eu já te disse que sou uma funcionária pública."

        mc desconfiado "Eu sei. Mas o que isso significa? Provavelmente você não trabalha no almoxarifado."

        na "Não."

        mc "Então?"

        scene natasha_sentada_meudeus with dissolve

        na "Você é mesmo insistente, né?"

        mc envergonhado "Tudo culpa sua que não fala logo."

        na "Isso é tudo o que você vai saber por enquanto. Eu prometo que não trabalho pra NASA ou pra Mossad, ok?"

        mc "Tá..."

        na "Fiquei muito feliz quando vi você. Espero que quando isso acabar a gente possa realmente se conhecer melhor."

        mc charmoso "Eu também. De vez em quando eu passo aqui no Cassino, ok?"

        na "Tá legal. Vou estar por aqui."

        na "Agora eu vou terminar meu drink e sair."

        mc "Trabalho chama?"

        na "Você já entendeu..."

        mc "A gente se fala, [na]."

        na "Boa noite, [mc]."

        scene jazz corner with Dissolve(1.0)

        "..."

        scene natasha_jazz with Dissolve(1.0)

        "Parece que ela vai continuar aqui por mais um tempo. Por que ela queria que eu saísse?"

        "No que será que ela tá envolvida?"

        "Funcionária pública... atende chamados inesperados..."

        "Trabalha passando a noite bebendo no cassino..."

        mc zerado "Que porra de trabalho é esse?"

        "Essa mulher é um mistério, eu ainda vou descobrir qual é a dela."

        if na1_beijo:

            "E depois daquele beijo, não vou te largar tão fácil, [na]."

        scene black with dissolve

        "..."



        label na1_premium1:

            pass

        menu:
            "Que trabalho a Natasha tem que fazer aqui? (+18)":








                na "Então finalmente você resolveu aparecer..."

                $ ba_nome = "Barão"

                scene natasha1_premium1 with Dissolve(1.0)

                pause

                ba "Quanto tempo mais você vai ficar me esperando sentada naquela mesma mesa, tomando o mesmo drink?"

                na "Você sabe que quando ele me ordena uma coisa, eu preciso cumprir."

                ba "Eu queria uma assistente igual a você..."

                na "Não me venha com brincadeira. Você tem dinheiro de sobra pra ter quantas assistentes você quiser."

                ba "Mas quantas seriam eficientes e gostosas iguais a você?"

                na "E quantas aguentariam o jeito que você trata as mulheres? A Diana que o diga..."

                ba "Não tô gostando do tom da sua voz. Trabalhar com o engomadinho tá fazendo você se achar melhor que os outros."

                na "Estou sendo sincera com você, só isso. Você entende que ele não gosta nem um pouco desse tipo de coisa."

                ba "Por que você não chega mais perto?"

                scene natasha1_premium2 with hpunch

                pause

                na "Ei!"

                ba "Além de tudo... você ainda cheira bem pra caralho..."

                na "Me solta. Para de brincadeira."

                ba "Quem tá brincando com a sorte aqui é você, mulher. Com quem você acha que tá falando?"

                na "D-desculpa se eu falei alguma coisa. Me solta, por favor."

                ba "Eu achei que você ia aguentar pelo menos mais um pouquinho..."

                na "Isso aqui não é um jogo pra mim. Eu sou só uma secretária! Só tô dando o recado dele!"

                ba "Mas aposto que você adora ter esse poder nas mãos, hm?"

                na "E-ele só falou pra eu ficar de olho em você! Você sabe que tem coisa demais em jogo aqui!"

                ba "O pai dele sabia muito melhor como agradar seus apoiadores."

                na "E-eu vou passar seu recado pra ele. Pode deixar."

                ba "Sabe... ele até me mandava umas garotas pra mostrar a importância do cassino... agora... não tem mais nada disso."

                na "Barão... você pode se divertir com quem quiser... você não pre-"

                scene natasha1_premium3 with hpunch

                pause

                ba "Chega! Sua voz tá começando a me irritar!"

                na "Ai!"

                ba "O que seria da prefeitura sem meu dinheiro, hein?! Será que vocês se esqueceram disso?!"

                na "Isso é demais!"

                ba "Você é demais... olha pra essa pele perfeita... de onde você é, hein? Como é seu nome mesmo?"

                na "N-natasha... eu so imigrante."

                ba "Isso eu sei. Você deve ter vindo de muito longe. Uma das melhores da sua espécie."

                na "Ngh... me solta."

                ba "Calma que a gente tá só começando..."

                menu:
                    "Continuar vendo":


                        scene natasha1_premium4 with Dissolve(1.0)

                        pause

                        ba "Quem sabe ele não tem mandou aqui pra isso, né não?"

                        na "Você já foi muito longe! Isso é assédio!"

                        ba "Hahaha! Vai me falar que ele não faz a mesma coisa com você!"

                        na "Nunca ele colocou a mão em mim assim!"

                        ba "Então ele é um idiota! Olha pra esses peitos! Você acha que eu ia deixar você ir embora assim?!"

                        ba "Eu vou dar uma boa olhada em tudo... e se você se comportar... olhar é tudo o que eu vou fazer..."

                        na "Para!"

                        ba "Nada disso. Se você continuar mal criada assim, eu vou te punir!"

                        scene natasha1_premium5 with hpunch

                        pause

                        na "Aii!"

                        ba "Você não quer trabalhar pra mim aqui? Eu posso te dar muito mais dinheiro que ele!"

                        na "Eu nunca trabalharia pra um abusador igual você!"

                        ba "Olha só se ela ainda não tem veneno!"

                        na "Isso é um absurdo! Eu só vim te entregar um recado! Olha o que você tá fazendo!"

                        ba "Eu vou ser sincero. Eu gosto quando vocês brigam e se debatem desse jeito."

                        ba "Dobrar esse tipo de mulher brava só mostra como eu sou ainda mais poderoso."

                        na "Você é maluco!"

                        ba "Hahaha! Me dá isso aqui!"

                        scene natasha1_premium6 with hpunch

                        pause

                        na "Não!"

                        ba "Você não vai precisar disso aqui. Isso eu te garanto."

                        na "O prefeito nunca vai te perdoar! Você sabe disso!"

                        ba "O prefeito, o prefeito... foi ele que te colocou nesse lugar."

                        ba "Deixa eu te falar uma coisa, porque parece que você não entendeu ainda."

                        ba "Você tá lidando com coisas que você não tem nem ideia. Pessoas que estão em outro mundo, entendeu?"

                        scene black with dissolve

                        scene natasha1_premium7 with Dissolve(1.0)

                        pause

                        ba "Você não passa de uma pobre mulher jogada em um universo que você nem tem ideia."

                        ba "Você é igual qualquer uma dessas coitadas que trabalham pra mim. Vocês valem menos do que as fichas plásticas do cassino."

                        ba "Eu faço o que eu quiser com você. E ninguém pode fazer nada contra mim. Nem mesmo o Donatello."

                        na "Ugh..."

                        ba "Qual grana você acha que permite ele pagar aqueles anúncios nas redes sociais? Que compra os santinhos e paga as viagens de jatinho dele?"

                        ba "Sem mim ele não seria nada. E nem você."

                        ba "Então deixa eu dar ua boa olhada naquilo que eu tô pagando... pra ver se vale a pena pagar de novo daqui uns anos..."

                        na "Você..."

                        scene black with dissolve

                        scene natasha1_premium8 with Dissolve(1.0)

                        pause

                        na "Nggh... eu sou uma pessoa... eu não sou uma coisa..."

                        ba "É... é o que as pessoas dizem... mas será que é mesmo?"

                        na "Como você pode ter uma cabeça tão distorcida?"

                        ba "Hah... se eu tenho o prefeito na minha mão, a polícia, os juízes... quem vai me impedir de fazer o que eu quiser?"

                        na "Sua consciência?!"

                        ba "HAHAHA!"

                        ba "É... parece que o Donatello realmente acertou em cheio contratando você..."

                        ba "Muito bem. Será que você entendeu seu lugar agora?"

                        menu:
                            "Entendi. Desculpa, senhor.":


                                na "E-eu entendi... eu não tô no mesmo mundo do senhor... me desculpa..."

                                ba "Olha só... e não é que ela aprendeu?"
                            "Cala a boca, nojento!":


                                na "Você não passa de um nojento! Você pode ter dinheiro e poder, mas sua alma é podre e não vale um centavo!"

                                ba "E você podia sair dessa sem se machucar, idiota!"

                                scene natasha1_premium9 with hpunch

                                pause

                                na "AAGHH!"

                                ba "O que eu te falei?! Se você se comportasse eu ia só olhar!"

                                na "Nnghhh!"

                                na "Quando ele souber disso, ele vai acabar com essa espelunca!"

                                ba "Ainda insistindo nessa?! Você acha que ele vai se vingar de mim?!"

                                na "Ele não é um panaca igual você!"

                                ba "Se fazendo de forte, né?! Ainda se achando melhor do que eu?! Toma essa, vadia!"

                                scene natasha1_premium10 with vpunch

                                pause

                                na "P-PARAA!!! AANGHH!"

                                ba "Agora, sim! É isso que você ganha por querer me desafiar."

                                ba "E acho bom você lembrar disso numa próxima. Você não é nada."

                        ba "Muito bem... pode descansar."

                        scene black with dissolve

                        scene natasha1_premium11 with Dissolve(1.0)

                        pause

                        na "Aah... nngh..."

                        ba "E fala uma coisa pra ele. Quando o príncipe tiver algo pra me dizer, acho bom ele vir falar cara-a-cara."

                        ba "Se ele acha que pode mandar a secretária dele vir lidar comigo, como se eu fosse de segundo escalão, isso vai acontecer de novo."

                        ba "Ter que lidar com pessoas como você, se achando no mesmo nível que eu... me irrita."

                        ba "Passar bem."

                        scene black with dissolve
                    "Já vi o que precisava":


                        scene black with dissolve
            "Eu não tenho interesse nisso":


                pass

        $ v22_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v22_fim","natasha","personagem")

        jump cassino_jazz

label natasha_evento2:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("na2_save", extra_info="na2_save")

    $ estou_na_cidade = False
    $ natasha_e2 = "iniciado"
    $ natasha_evento = 8

    "Ela disse que tem algo pra resolver aqui no cassino... mas o que será que é?"

    "Eu vejo ela sentada quase todas as noites aqui... sem falar com ninguém, sem ler ou escrever qualquer coisa..."

    "Que trabalho será esse?"

    "Ah! Teve aquela vez que ela conversou com a [d]..."

    if natasha_xeretou:

        "Eu fiquei escutando a conversa..."

        "A [na] parecia preocupada com alguma coisa. Eu lembro dela falando tipo 'olhe pras outras garotas'."

        "Que outras garotas? E de quem ela tava falando?"
    else:


        "Eu decidi não ficar escutando elas, então não sei o que elas falaram... mas a [na] parecia preocupada."

        "Será que ela tá preocupada com a [d]?"

    "Depois daquela noite no quarto da [d] que eu escutei o Barão falando aquelas coisas... tratando ela daquele jeito..."

    "Será que a [d] tá passando por alguma barra?"

    if v26_fim:

        "E na pizzaria também! A [d] queria falar alguma coisa que deixou ela muito nervosa."

    "Que merda será que tá acontecendo nesse cassino?"

    "Se eu pudesse ajudar a [na]... talvez eu acabasse ajudando a [d] também."

    "Mas ela é tão fechada. Não acho que ela aceitaria ajuda..."

    "Bom... não custa nada tentar."

    scene natasha_jazz_close with Dissolve(1.0)

    mc charmoso "Boa noite, [na]."

    na "Ah! Oi, [mc]. Boa noite."

    mc desconfiado "O que foi? Tá meio desligada?"

    na "Eu? Imagina..."

    mc charmoso "Algum avanço com o trabalho?"

    na "Que nada..."

    mc envergonhado "Então tudo bem. Não quero te atrapalhar. Vou indo nessa."

    na "Não, não. Sente um pouco."

    mc normal "Vou sentar então. Licença."

    na "Toda."

    scene natasha_sentada_sorrindo with Dissolve(1.0)

    mc normal "Opa."

    na "E aí? Como estão as coisas?"

    mc "Correndo como sempre."

    na "Não me diga... você tem cara de quem leva uma boa vida, [mc]."

    mc zerado "Você acha mesmo?"

    na "Eu falo isso como um elogio. Você não tem a face de alguém que está em constante provação."

    scene natasha_sentada_incomodada with Dissolve(1.0)

    na "Diferente de mim. Eu não consigo me livrar dessas olheiras de forma alguma."

    mc envergonhado "..."

    menu:
        "Isso mostra que você trabalha bastante. É bom.":


            mc charmoso "Isso são marcas de quem tá na luta. É uma boa coisa."

            na "Hm..."

            na "Eu queria poder trabalhar um pouco menos."

            mc envergonhado "Imagino..."
        "Que nada. Você tá exagerando.":


            mc charmoso "Você tá exagerando... não tem nada aí."

            na "Sei... eu consigo ler sua expressão, [mc]."

            mc envergonhado "S-sério?"

            na "Você é um livro aberto. Mais do que imagina."

            mc "Haha..."

    na "..."

    "Melhor eu falar logo de uma vez."

    mc normal "[na]... eu tava pensando se talvez eu poderia te ajudar... de alguma forma..."

    scene natasha_sentada_pensando with Dissolve(1.0)

    na "Me ajudar? Como assim?"

    mc envergonhado "Não sei... com esse trabalho que você parece enrolada."

    na "Esse é um novo tipo de cantada?"

    mc "Haha... não, não."

    na "..."

    na "[mc]... você nem faz ideia do que eu faço, certo?"

    mc "Certo..."

    na "Ent-"

    mc normal "Mas eu sou um jornalista. Eu tenho fontes e tenho um poder especial de falar com as pessoas. Isso pode ser útil em várias coisas."

    na "Incrivelmente, você tem alguma razão nisso."

    mc "Então! Quem sabe..."

    na "..."

    na "Eu agradeço, de verdade. É até interessante como você parece se importar de verdade comigo."

    mc envergonhado "Isso é estranho?"

    scene natasha_sentada_falando with Dissolve(1.0)

    na "É um pouco, sim, [mc]. Em um mundo onde as pessoas estão cada vez mais se preocupando só com elas mesmas..."

    mc desculpa "Isso não é legal."

    na "Mas é bom saber que ainda tem gente que consegue se preocupar com os outros de verdade. Sem querer nada em troca."

    menu:
        "Talvez eu queira algo em troca...":


            mc tarado "Quem disse que eu não quero nada em troca?"

            scene natasha_sentada_sorrindo with dissolve

            na "Você é bobo, isso sim."

            mc zerado "Ei..."

            na "Eu sei que talvez você tenha um interesse em mim, mas não sinto que é por isso que você tá me ajudando."

            mc desconfiado "Hm?"

            na "Eu sinto que mesmo que você me ajudasse e depois eu te desse um pé, você não ficaria bravo comigo."

            mc "Bravo? Acho que não..."

            na "Você vê a diferença?"

            mc envergonhado "Sinceramente... acho que não..."

            na "Bobo..."
        "Isso não é nada.":


            mc envergonhado "Isso não é nada... Eu não fico pensando nisso."

            na "O que torna ainda mais incrível."

            na "Esse negócio de conseguir esquecer um pouco suas próprias coisas e pensar no que o outro tá vivendo, isso é algo muito bacana."

            na "Pelo menos pra mim... é algo muito bacana."

            mc "Você tá me deixando com vergonha. Vamo parar de falar disso."

            scene natasha_sentada_sorrindo with dissolve

            na "Você quem manda."

    mc envergonhado "Mas e aí? Posso fazer algo ou não?"

    na "Vai insistir nisso?"

    mc "Talvez..."

    na "..."

    na "Quanto você conhece o Cassino do Barão?"

    mc desconfiado "Hmm... um tanto. Já joguei aqui, já conversei com algumas das garotas que trabalham, conheço a [d]..."

    na "E o Barão? Você conhece ele?"

    mc envergonhado "Nunca vi o sujeito..."

    scene natasha_sentada_surpresa with Dissolve(1.0)

    na "Sério isso?"

    mc desconfiado "Sim. Por que?"

    na "Por nada. É que ele é um sujeito famoso, né? Acho que qualquer pessoa na ilha reconheceria ele."

    mc "Interessante você falar isso... eu realmente nunca vi ou ouvi falarem nada sobre ele. Até mesmo na revista."

    na "Engraçado... nunca teria imaginado."

    mc "Isso muda alguma coisa?"

    scene natasha_sentada_falando with Dissolve(1.0)

    na "A verdade é que eu preciso conversar com o Barão."

    mc desconfiado "Conversar?"

    na "Mas não pode ser aqui no Cassino. Eu preciso falar com ele, mas fora daqui."

    mc "Por que?"

    na "Tem a ver com o meu trabalho e infelizmente eu não posso te explicar."

    na "[mc]... você realmente tem um jeito diferente de falar com as pessoas. Será que... você conseguiria descobrir uma forma?"

    mc "Descobrir uma forma de falar com o Barão fora do cassino? É isso que você tá perguntando?"

    na "Exatamente."

    na "Talvez as garotas que trabalham aqui saibam alguma coisa. Ou {b}alguém na sua revista{/b}..."

    mc "Hmm... talvez..."

    na "Se você conseguir qualquer coisa nesse sentido, por favor me avise."

    mc normal "Ok. Pode deixar."

    scene natasha_sentada_preocupada with dissolve

    na "Olha... isso que eu estou lhe pedindo está fora do protocolo. Ninguém pode saber que eu pedi isso, tudo bem? Você me promete?"

    "Protocolo?"

    mc desconfiado "Ok."

    mc charmoso "Pode confiar em mim, [na]. Vou descobrir alguma coisa e te falo. E ninguém vai saber. Pode ficar tranquila."

    scene natasha_sentada_sorrindo with dissolve

    na "Qualquer coisa que você descobrir, venha falar comigo, tudo bem?"

    mc charmoso "Pode deixar."

    na "É interessante pensar que tem alguém me ajudando... obrigada, [mc]."

    mc envergonhado "Vamos ver se eu realmente vou ajudar em alguma coisa."

    na "Você já está. Até mais."

    mc normal "Até, [na]. Assim que eu descobrir algo te aviso."

    scene jazz geral with Dissolve(1.0)

    "Encontrar uma forma de falar com o Barão fora do cassino... por que ela quer falar com ele?"

    "Será que a [na] faz negócios com ele? Não... se ela fizesse ela saberia onde encontrar ele."

    "Ou talvez..."

    "Preciso tentar encontrar alguém que saiba algo sobre ele. Ela disse pra eu ver aqui no Cassino ou na redação..."

    "Talvez alguém com mais experiência sobre a ilha possa me ajudar."

    "Nem acredito que eu realmente posso ajudar a [na]. E talvez eu acabe encontrando algo muito interessante no meio disso."

    "Quem sabe uma {b}pauta pra revista{/b}..."

    jump cassino_jazz

label natasha_e2_barao_chefao:

    $ natasha_e2 = "conversa"
    $ natasha_evento = 9

    "Será que ele realmente vai aparecer?"

    mc surpreso "!"

    "Pera! Tem alguém sentado alí!"

    mc serio "Preciso chegar mais perto..."

    "..."

    scene chefao_barao_pizzaria with Dissolve(1.0)

    pause

    mc "Eita... quem são?"

    mc "Opa... é aquele cara."

    if v31_fim:

        "Esse é o chefe do [mar]... O que ele quer com esse homem?"

    ba "... sabe que eu não curto que me chamem pelo nome!"

    to "Você realmente não espera que eu te chame de 'Barão', certo?"

    "Barão?!"

    ba "Eu sei... pode falar 'você', só não fala a porra do meu nome!"

    to "Tudo bem, 'Barão'..."

    $ ba_nome = "Barão"

    ba "Engraçado..."

    to "Você é um homem ocupado. Tem certeza que quer gastar seu tempo em brigas fúteis?"

    ba "E você? Não tá ocupado?"

    to "Eu? Eu estou aqui quase toda a noite. Tem gente que acha que eu sou o segurança da pizzaria."

    ba "HAHAHAHA!"

    ba "Você fala cada coisa, Tony."

    $ to_nome = "Tony"

    to "Só estou sendo sincero com você. Já aconteceu mais vezes do que você imagina."

    "Será que esse homem realmente é o Barão?"

    scene chefao_barao_pizzaria2 with Dissolve(1.0)

    pause

    to "Você está totalmente fora do contexto."

    ba "Quê?"

    to "Primeiro, olhe para sua roupa. Você não tem vergonha de andar assim na rua?"

    ba "Eu sou um personagem, [to]! Um personagem! Eu preciso me vestir assim."

    to "Segundo, essa arma. Por que você precisa trazer isso em um restaurante familiar?"

    ba "Nunca se sabe quando eu vou precisar usar uma arma aqui."

    to "Você me ofende."

    ba "Com todo o respeito, eu sei com quem eu tô mexendo."

    to "Terceiro, você não precisa sentar com os pés na mesa."

    ba "E você não precisa ser chato assim. Você pode parar de falar de mim?"

    to "Então você quer falar do quê?"

    ba "A garota começou a dar trabalho."

    to "Você sabe que isso era uma possibilidade quando ela chegasse a certa idade."

    ba "Ela quer sair da jogada."

    to "Certa ela."

    ba "Como certa?! Não foi esse o combinado!"

    to "Não interprete minhas palavras da forma errada. A garota é sua, você faz o que quer com ela. O que ela quer não importa."

    to "Contanto que você siga os termos estabelecidos no contrato. As sacerdotisas precisam-"

    ba "Ah... entendi. Mas isso vai dar dor de cabeça."

    to "Repito, você sabia isso desde o começo. Você escolheu ser o protetor dela."

    ba "Caralho você... tudo bem. Eu vou dar um jeito."

    to "Muito bem. O que mais?"

    ba "Era só isso."

    to "Não é não."

    ba "Por que? Você tem algo pra mim?"

    to "Sim."

    scene chefao_barao_pizzaria3 with Dissolve(1.0)

    pause

    to "Dois dos meus contatos na polícia disseram que existe uma ovelha negra no rebanho."

    ba "?!"

    ba "Quê?! Como?!"

    to "A ovelha não é daqui."

    ba "[to]! Você precisa fazer alguma coisa! É por isso que você tá aqui!"

    to "Eu sei. Mas isso está fora do meu alcance."

    ba "Você não é barato, [to]! Você sabe disso! Nã-"

    to "A ovelha é estrangeira. Ela não responde às autoridades daqui."

    ba "Não creio... Que-"

    to "Provavelmente a Interpol junto da agência regional. Pelo menos é o que os contatos disseram."

    ba "Mas por que?"

    to "A polícia não recebe mensagem deles há meses. Aparentemente eles deixaram de contar com nossa cooperação."

    ba "Será que eles descobriram?"

    to "Descobrir? Não... mas devem estar suspeitando."

    ba "Isso é ruim, [to]. Tem muita coisa em jogo aqui."

    to "Não se preocupe. Eu vou garantir que tudo permaneça como está, mas você precisa me ajudar a te ajudar."

    ba "Ok. O que eu faço?"

    to "A garota. Não pressione. As roupas, a arma, as garotas. Pare com tudo isso."

    ba "Mas-"

    to "É apenas por um tempo. Até eu descobrir mais sobre isso."

    ba "Espera! Você acha que pode ter alguém atrás de mim?"

    to "Acho."

    ba "Vai se foder, [to]! Não acredito!"

    ba "Por que eu te pago?!"

    to "..."

    ba "Eu não quero ficar preso nesse país de merda!"

    ba "Isso é culpa sua!"

    to "..."

    ba "..."

    to "Acabou?"

    ba "Caralho..."

    to "Eu vou fazer meu trabalho, mas você faça o seu. Não exagere."

    ba "Eu trago o dinheiro, [to]! Os idiotas gastam tudo o que tem lá!"

    ba "Eu sugo eles ao máximo! Eu faço eles se sentirem deuses naquele inferno! Eu TÔ FAZENDO MINHA PARTE!"

    ba "E você? O que tá fazendo?!!"

    to "Eu sei que você está bravo, mas isso não muda o fato que você vai ter que tomar cuidado."

    ba "Não acredito nessa merda!"

    to "Agora vai. Passou tempo demais."

    ba "Isso não vai ficar assim, [to]. Você dá seu jeito."

    to "Vamos. Eu estou indo também."

    ba "Bah!"

    scene black with dissolve

    "..."

    scene pizzaria_out_noite with Dissolve(1.0)

    "Que merda foi essa?"

    "Ovelha negra? O que ele quis dizer com isso?"

    "Foda-se isso agora! Eu achei o Barão! Eu tenho que falar pra [na]!"

    "Pera..."

    "Será que eu realmente falo pra ela? Isso parece algo muito grande..."

    "Se eu guardar pra mim... talvez eu possa usar isso depois. Mas com certeza vai ferrar minha relação com ela."

    "Se eu contar, vou ganhar vários pontos, mas vou perder exclusividade de uma informação valiosíssima."

    "O que eu faço, merda?!"

    menu:
        "Contar para a [na] sobre a conversa":


            $ natasha_e2 = "positivo"

            "Eu tenho que contar pra [na]. Nem tem o que pensar."

            "Eu entrei nessa pra ajudar ela e era justamente isso que ela tava procurando!"

            "Tenho certeza que isso vai deixar ela doida. Vou agora pro cassino. Tomara que ela teja lá."

            scene black with dissolve

            "..."

            "..."

            mc surpreso "[na]!"

            na "[mc]?"

            scene natasha_jazz_close with Dissolve(1.0)

            na "Por que está gritando? O que foi?"

            mc charmoso "Vem comigo. Tenho um negócio pra te contar no caminho."

            na "Eu não posso sai-"

            mc "Vem logo!"

            na "Ei!"

            scene black with dissolve

            mc "Eu descobri um lance sobre o Barão que você não vai acreditar."

            na "O quê?"

            "..."

            "..."

            scene natasha_pizzaria_pensando with Dissolve(2.0)

            pause

            na "Então foi aqui..."

            mc normal "Sim."

            na "..."

            mc charmoso "O que achou?"

            na "Incrível, [mc]. Em alguns dias você conseguiu descobrir algo que eu não consegui em semanas."

            na "Você é um excelente investigador."

            mc "Valeu."

            na "Eu vou ter que fazer algumas coisas, mas essa sua informação é essencial. Finalmente vou poder dar continuidade."

            na "Então..."

            na "Infelizmente não vou mais te ver, [mc]."

            mc desconfiado "Como?"

            na "Desculpa, você foi um rapaz incrível. E eu agradeço do fundo do meu coração. Mas a gente se separa aqui."

            na "Tome cuidado, [mc]. Essas pessoas... elas vivem em outro mundo."

            na "Adeus."

            mc angustiado "[na]!"

            scene black with Dissolve(1.0)

            scene pizzaria_out_noite with Dissolve(1.0)

            "Por quê?"

            "Eu achei que ela... O que eu fiz de errado?"

            "E do jeito que ela falou... parece algo perigoso..."

            "Eu não quero me meter nisso... eu só queria ajudar ela... e agora isso?!"
        "Não contar e manter o segredo para você":


            $ natasha_e2 = "negativo"

            "Não vou contar. Eu acho que eu posso ganhar mais com essa informação do que só uns pontos com ela."

            "Talvez essa informação vá valer algo pro chefe, pra [d] ou pra muitas outras pessoas. Não vou gastar isso com a [na]."

            "Vou deixar a [na] pra lá por enquanto."

            "Tenho que pensar direito no que eu ouvi e o que toda essa merda quer dizer."

    "Tudo isso é loucura demais, mano! Pior é que é certeza que eu posso me FERRAR se eu não tomar cuidado."

    "Imagina acabar morto?"

    "Não quero nem pensar nisso, cara..."

    "O que eu fiz pra cair nesse buraco?"

    scene black with Dissolve(1.5)





    menu:
        "O que será que aconteceu com a Natasha?":


            scene na4_img7 with Dissolve(1.0)

            pause 1.0

            na "Senhor... eu preciso falar com você..."



            "Donatello" "O que foi?"

            na "É sobre o Barão..."

            "Donatello" "Você passou pra ele o que eu te pedi?"

            scene black with dissolve

            scene natasha2_premium1 with Dissolve(1.0)

            pause

            na "Sim, senhor... ele me evitou por vários dias... mas eu finalmente consegui falar com ele."

            "Donatello" "Muito bem. E como foi? Ele entendeu?"

            na "Senhor... ele... fez coisas horríveis comigo."

            "Donatello" "Como?!"

            na "Ele ficou irritado por eu ter falado aquilo com ele... ele... foi horrível, senhor."

            "Donatello" "Eu não acredito... então ele não entendeu nada do que queríamos."

            na "Não... eu falei pra ele que ele ia se arrepender, que eu trabalhava pro senhor e nem assim..."

            "Donatello" "Aquele homem não tem limites. Colocando aquelas mãos imundas em você."

            "Donatello" "Ele chegou a..."

            na "Não, senhor... ele disse que era apenas um aviso... pra eu nunca mais aparecer."

            "Donatello" "Muito bem. Você nunca mais vai precisar ir atrás dele. Qualquer coisa eu mandarei ele vir aqui."

            "Donatello" "E o resto? Descobriu com quem ele está falando?"

            if natasha_e2 == "positivo":

                na "Sim. E foi graças a um paparazzo."

                "Donatello" "Não me diga..."

                na "Ele tá falando com o dono da Pizzaria Alighieri. Você sabe quem é ele?"

                "Donatello" "Tony..."

                na "Sim. Era esse mesmo o nome."

                "Donatello" "Ele é um zé ninguém que deu sorte no casamento. Agora ele... faz certas coisas..."

                na "Sorte no casamento?"

                "Donatello" "Sim. Diferente da maioria dos nossos aliados, ele não nasceu no nosso círculo. Ele acabou casando com uma Alighieri e acabou entrando."

                "Donatello" "Só que a mulher morreu e ele assumiu a pizzaria. Como ele sabia demais, deixaram ele cuidando de certos assuntos."

                na "Envolvendo a polícia..."

                "Donatello" "Isso mesmo. Ele garante que nada respingue em nós, entende?"

                na "Sim..."

                "Donatello" "Se o Barão foi falar com ele, então deve tá acontecendo alguma coisa."

                na "Eles tão com medo que tenha algum policial fora do esquema querendo saber demais."

                "Donatello" "Se o Tony tá envolvido, é melhor que nós fiquemos bem longe. Não podemos saber mais do que devemos."
            else:


                na "Não muito... eu sei que ele tá falando com alguém fora do Cassino."

                "Donatello" "Onde que ele tava?"

                na "Não sei... eu sinto que um paparazzo pode ter conseguido algo, mas ele não me falou nada ainda."









                "Donatello" "Então fique de olho. Se ele te falar, você me conta tudo."

                na "Pode deixar, senhor."

            "Donatello" "Nós temos uma imagem para proteger. Não podemos nos envolver nessa sujeira toda. Minha reeleição está em jogo."

            na "Sim, senhor. E o que eu faço agora?"

            "Donatello" "Parece que nosso lado está com algumas feridas, mas tudo sob controle. Eu acho que você deveria focar no Distrito."

            "Donatello" "Ganhe a confiança deles e veja se devemos nos preocupar."

            "Donatello" "Temos que manter tudo em ordem, [na]. Qualquer peça que se movimentar fora do planejado pode derrubar nosso castelo de cartas."

            na "Tudo bem, senhor. Cuidarei disso."

            "Donatello" "Enquanto eles estiverem quietos no canto deles tudo estará dançando conforme a música."

            "Donatello" "Mas se pessoas estranhas estiverem em contato ou se eles planejarem algo fora do que lhes é cabido, me avise por favor."

            na "Muito bem. Começarei isso hoje a noite ainda."

            "Donatello" "Perfeito. Agora, de volta aos trabalhos do dia-a-dia. Eu só confio em você para cuidar das minhas coisas."

            label na2_premium1:

                pass

            menu:
                "Muito bem. Vou trabalhar.":


                    na "Vou continuar com meu trabalho então, senhor."

                    "Donatello" "Boa garota."
                "E a vingança contra o Barão?":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_38

                        jump na2_premium1

                    na "Senhor prefeito... e quanto ao Barão? E o que ele fez... o senhor não pretende retaliar?"

                    "Donatello" "Veja bem, [na]..."

                    scene natasha2_premium2 with hpunch

                    pause

                    na "Ah!?"

                    "Donatello" "Pessoas como eu e o Barão... estamos acostumados a usar garotas como você, entende?"

                    na "S-senhor! O que significa isso?!"

                    "Donatello" "Você desperta esse tipo de coisa nos homens... você é linda... tem um corpo perfeito..."

                    "Donatello" "O Barão é muito importante pra reeleição. E a gente não quer irritar ele por pouco."

                    "Donatello" "O ideal seria que você aprendesse a usar tudo o que você tem pra atingir nossos objetivos..."

                    na "O senhor... o senhor nunca f-fez nada assim..."

                    scene natasha2_premium3 with hpunch

                    pause

                    "Donatello" "Pois é... pode ter sido culpa minha no fim..."

                    na "Por favor, senhor!"

                    "Donatello" "Eu devia ter ensinado você sobre essas coisas antes... você... quer aprender?"

                    na "Senhor! Nós trabalhamos juntos! Isso não é permitido!"

                    "Donatello" "As leis param de fazer sentido quando você ingressa certos círculos, [na]..."

                    "Donatello" "E você precisa entender tudo isso se você quer ser uma boa secretária..."

                    "Donatello" "Digo... você não quer me decepcionar, certo?"

                    menu:
                        "Senhor! Não posso aceitar isso!":


                            na "Não! M-melhor eu voltar ao trabalho! Tem muita coisa pra eu fazer!"

                            "Donatello" "É uma pena... mas é você quem escolhe..."
                        "Eu quero meu emprego...":


                            na "Eu quero continuar trabalhando pro senhor... mas... aceitando esse tipo de coisa?"

                            "Donatello" "Isso... não é brigando que você vai chegar lá, minha querida."

                            "Donatello" "Pessoas como o Barão precisam ser agradadas... é preciso fazer política pra conquistá-las."

                            scene natasha2_premium4 with Dissolve(1.0)

                            pause

                            "Donatello" "Deste jeito que eu tô fazendo com você agora..."

                            na "S-senhor prefeito! Aí não!"

                            "Donatello" "Eu só quero que você se sinta bem... eu tô te ensinando uma lição..."

                            na "Isso é inapropriado e errado, senhor. Com todo o respeito... o senhor não pode continuar com isso."

                            "Donatello" "Você não tá ouvindo nada do que eu digo? O que é uma relação rápida comparada com o que você pode conseguir?"

                            na "Vender meu corpo, senhor... é isso que o senhor tá dizendo?"

                            "Donatello" "Qual o problema? Sexo, prazer... também são uma moeda de troca, como dinheiro e poder..."

                            "Donatello" "Por exemplo... se você aceitar me servir completamente... eu posso garantir que o Barão pague pelo que ele fez."

                            na "Você entende como isso é errado?"

                            "Donatello" "Esqueça 'certo e errado'. Pense em você... o que você quer? Tá em suas mãos, [na]..."

                            "Donatello" "De um lado, um trabalho que você ama e o poder de se vingar... do outro... não sobra nada, mas é o 'certo'. Hm?"

                            menu:
                                "De jeito nenhum. Eu não posso fazer isso.":


                                    na "Não funciona assim pra mim, prefeito... eu não conseguiria..."

                                    "Donatello" "Muito bem. A escolha é sua, minha querida. Mas eu vou pensar muito bem em como as coisas vão continuar..."

                                    na "P-por favor..."
                                "...":


                                    na "Eu..."

                                    "Donatello" "Você não foi contra? É um começo. Estamos negociando... excelente..."

                                    scene black with dissolve

                                    scene natasha2_premium5 with Dissolve(1.0)

                                    pause

                                    na "Hmmm!"

                                    "Donatello" "Não se preocupe que você não vai precisar fazer nada hoje..."

                                    na "N-não?"

                                    "Donatello" "Você sempre foi uma excelente secretária. E imaginar que o Barão fez algo contra você... aquele idiota."

                                    "Donatello" "O mínimo que eu posso fazer é te pedir desculpas, minha querida."

                                    na "A-ah... senhor..."

                                    "Donatello" "Você perdoa seu chefe?"

                                    na "Claro... hmm... n-não precisa se desculpar... não precisa disto!"

                                    "Donatello" "Eu vou cuidar muito bem de você... e vou te ensinar como ser a secretária de um homem poderoso como eu..."

                                    na "Ai... e-eu não tenho certeza se a gente devia..."

                                    "Donatello" "Logo logo você vai ter certeza. Você vai ver como a vida é bem mais fácil assim, [na]."

                                    scene black with Dissolve(1.0)

                                    na "Nngh... prefeito..."
        "Eu preciso focar nas minhas coisas.":


            pass



    scene black with Dissolve(3.0)

    $ tempo = 3

    $ v29_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v29_fim","final","local")



    jump call_cidade

label natasha_evento3:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("na3_save", extra_info="na3_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ natasha_e3 = "evento"

    "É... Como eu vim parar aqui?"

    $ na3_beijo = False
    $ na3_seducao = False
    $ na3_banheira = False

    "..."

    mc envergonhado "O que eu tô falando? Eu sei o que eu tô fazendo aqui..."

    mc concentrando "Procurando pautas pra revista."

    "Mentiroso. Você sabe muito bem o que você veio procurar aqui."

    "Não tem nada de errado um homem adulto querer se divertir um pouco."

    if priscila_namoro or sayuri_namoro or julia_namoro or diana_namoro or maria_namoro or nathan_namoro:

        "Seria melhor se eu não tivesse namorando..."

        "Que merda... por que um cara comprometido tá no distrito dos prazeres?"

    "Pensando aqui... talvez eu possa me divertir um pouco só bebendo... e talvez dando uma olhadinha, certo?"

    "Eu não preciso necessariamente me envolver com alguém. Só beber, talvez falar com meu mano [us]."

    "Talvez encontrar um figurão fazendo alguma coisa errada que me ajude a me manter no emprego. Essa seria uma boa mesmo."

    if xiang_evento > 0:

        "Ah! Ou a [i]... saudades daquela lá. É estranha, mas é linda... e até que ela é sexy."

    "Vou dar uma passada no clube."

    scene distrito esquina with Dissolve(2.0)

    mc normal "E aí, [mon]? Boa noite."

    show montanha normal with dissolve

    mon "Fala, maninho. Veio curtir o clube?"

    mc "Pois é."

    mon "Hoje a entrada tá por conta da casa."

    mc surpreso "Sério?!"

    mon "É. A Madame tá querendo fazer uma surpresa pros frequentadores. Pode entrar sem pagar nada hoje."

    mc normal "Que beleza. Agora curti."

    mon "Só que hoje não tem drink de graça, viu?"

    mc "Haha... seria pedir de mais, né?"

    mon "Então fique à vontade, [mc]. A casa é sua."

    mc "Valeu."

    scene black with Dissolve(1.0)

    scene distrito_clube pub with Dissolve(1.0)

    pause

    "Não tem bebida de graça, mas com o dinheiro que eu ia gastar pra entrar dá pra eu tomar uma boa."

    mc zerado "Espera... agora eu entendi tudo..."

    "Essa [nora] não brinca com dinheiro. Se bem que manter isso aqui não deve ser simples."

    "Vou sentar no lugar de se-"

    mc desconfiado "Hm?"

    scene na3_bar1 with Dissolve(1.0)

    pause

    "Espera... essa é aquela moça do Cassino. A [na]!"

    if na1_beijo:

        "A gente até ficou lá no Jazz Corner. Foi uma vez, mas foi muito bom."

    "O que ela tá fazendo aqui?"

    "Se pá ela nem quer falar comigo, senão ela teria me chamado pra vir aqui também."

    "Se bem que... quem chama alguém pra vir em um clube de BDSM? Nunca ia imaginar que ela era chegada nessas coisas."

    "Parece que quando o assunto é sexo a gente não conhece ninguém."

    "Enfim... será que eu chamo ela ou deixo ela quieta?"

    menu:
        "Vou dar um boa noite.":


            $ natasha_seducao += 2

            "Vou só dar um boa noite como quem não quer nada. Vamo ver como a coisa evolui."

            "Se tem uma coisa que eu aprendi aqui na ilha é que quem não chora não mama."

            mc concentrando "{i}puuufff{/i}"

            mc charmoso "Bora."

            scene na3_bar2 with Dissolve(1.0)

            pause

            mc charmoso "Oi, [na]. Boa noite."
        "Deixa ela lá. Vou me divertir sozinho.":


            "Deixa ela. Se ela não comentou nada, é porque não quer companhia. Não adianta eu forçar."

            "Vou sentar aqui e ficar na minha."

            mc normal "Boa noite, [nora]."

            scene na3_bar3 with Dissolve(1.0)

            nora "Bem-vindo, jovem. Hoje o Black Cash não está."

            mc "Tudo bem. Eu só tava querendo beber alguma coisa e curtir a noite mesmo."

            nora "Deu sorte de vir hoje. Você viu que a entrada tá de graça, né?"

            mc "Pois é. Gostei."

            nora "Aproveita esse dinheiro pra ver um show das meninas. Você gosta daquela [i], né?"

            mc "Eu não diria isso, [nora] haha..."

            nora "Não seja tímido, menino. Na sua idade, todo homem pensa assim. São questões do corpo. Não se esqueça que o ser humano é um animal."

            mc "Verdade."

            nora "Mas se você não tá afim de ver uma garota nessas condições, tem uma jovem terrivelmente linda sentada logo ali."

            mc "Ah... eu vi..."

            nora "E tá esperando o quê?"

            mc "Sei lá, [nora]. Eu-"

            nora "Deixa comigo. A [nora] vai dar uma ajudinha."

            mc "N-não é-"

            nora "Pode deixar."

            scene distrito_clube pub with Dissolve(1.0)

            "Não era bem isso que eu queria... eu devia ter falado pra ela..."

            "Por que eu sou tão bundão às vezes?"

            nora "Garoto, vem aqui."

            mc angustiado "Ai ai..."

            scene na3_bar2 with Dissolve(1.0)

            pause

            mc envergonhado "O-oi. Boa noite, [na]."

    na "[mc]. Que surpresa encontrar você aqui."

    "Por que a expressão dela parece completamente o contrário?"

    mc envergonhado "Pois é... eu também venho aqui."

    na "Essa é minha primeira vez aqui na verdade."

    mc charmoso "O lugar é bacana... se você... gosta de bebida forte e mulheres seminuas..."

    na "Os dois tópicos estão quase no topo da minha lista."

    mc envergonhado "Haha..."

    na "Me fala. Então você conhece o pessoal daqui?"

    mc normal "Sim. O [mon], a [nora]. Tem o [us] e as garotas também. Eu conheço duas delas."

    na "Perfeito."

    mc desconfiado "Hm?"

    na "Por que você não senta comigo?"

    mc charmoso "Só passei pra dar um alô mesmo. Não quero atrapalhar."

    na "De forma alguma. Eu preciso de companhia pra noite. A não ser que você já tenha planos."

    menu:
        "Seria um prazer.":


            $ natasha_seducao += 1

            mc charmoso "Seria um prazer tomar alguma coisa com você."

            na "Que bom. Então senta aqui. Vamos trocar uma ideia."

            "T-trocar ideia?! Isso tem outro significado pra mim."
        "Se você insiste.":


            mc charmoso "Se você insisti, eu posso, sim."

            na "Isso. Senta e vamos beber."

            mc "Opa."

    mc charmoso "Com licença."

    scene na3_bar4 with Dissolve(1.0)

    pause

    mc "Então... Bom, nada."

    na "Que foi? Quer falar alguma coisa?"

    mc "Tá bom. Já que comecei, deixa eu falar. Não quero que você ache que eu tô julgando, mas não imaginei que você viria pra cá."

    na "Você achou que eu fosse uma madame de cassino?"

    mc "É. Desculpa se pareceu preconceito ou alguma coisa assim."

    na "Não se preocupe, [mc]. A gente conversou bastante lá. Eu sei que você é um rapaz decente."

    mc "Valeu."

    na "Acho que qualquer pessoa pode querer se divertir um pouco."

    mc "Isso com certeza."

    na "Mas e você? Pelo jeito gosta desse tipo de coisa."

    menu:
        "Eu gosto bastante. Curtir é comigo.":


            mc "Eu curto. Pode me chamar pro que for que eu participo. Pode ser no cassino, no puteiro, tamo aí."

            na "Parece divertido..."
        "Mais ou menos. Eu prefiro a bebida.":


            $ natasha_seducao += 2

            mc "Não é tanto assim. Eu venho mais pela bebida e pra ver o pessoal."

            na "Entendi. Mantendo as coisas nos limites?"

            mc "Isso."

            na "Eu também prefiro viver assim."
        "Nada. Aqui é última opção mesmo.":


            $ natasha_seducao += 1

            mc "Pra falar a verdade, aqui é minha última opção. Prefiro ficar mais na ilha ou um restaurante mais pra lá."

            na "Não é assim também. Aqui é bacana."

            mc "É, mas não é minha praia."

            na "Entendi..."

    mc "Mas se é sua primeira vez, então ainda tá em fase de testes."

    scene na3_bar6 with Dissolve(1.0)

    pause

    na "Podemos dizer que sim. Por enquanto o clima está agradável."

    mc normal "Pois é. Quando alguém fala que foi pro distrito a gente imagina um monte de coisa, né?"

    mc charmoso "No fundo é só um lugar normal... com um pouco mais de prazer..."

    na "Sim. Às vezes a gente tem essas coisas dentro da gente, daí quando vê como é de verdade até se assusta."

    na "Isso é uma coisa que eu aprendi na prática. Até pelo meu trabalho, eu sempre tive que ir a vários lugares diferentes."

    mc "Interessante. Hoje você vai me falar com o que você trabalha?"

    na "Eu já disse que meu trabalho não tem graça. Eu faço algumas coisas pra uns engravatados, só isso."

    mc desconfiado "Esse seu trabalho paga pra você tomar drinks no cassino e no inferninho?"

    na "Bom..."

    scene na3_bar5 with Dissolve(1.0)

    pause

    na "Não é tão bom assim como pode parecer."

    mc desculpa "Eu sei. Tô zuando."

    na "Acho que você é a primeira pessoa que eu vejo dessa forma."

    mc desconfiado "De que forma?"

    na "Desculpa. Quero dizer, duas vezes em locais diferentes. Isso é bem raro pra mim."

    menu:
        "Sério isso?":


            $ natasha_seducao += 1

            mc "Verdade isso? Por que? Você trabalha em vários lugares diferentes?"

            na "Sim. Eu preciso estar constantemente me movendo pelo país."

            mc desconfiado "Você não trabalha em banco ou alguma coisa assim."

            na "[mc]..."

            mc envergonhado "Ok, eu sei..."
        "Bom saber que eu marquei sua vida.":


            mc charmoso "É bom saber que eu fui marcante pra sua vida."

            na "..."

            "Acho que ela não tá muito no clima pra brincadeira."

            na "Eu sei que parece bobeira. Meu trabalho não é ruim, mas cansa às vezes."

            mc desculpa "Sei."

    mc charmoso "Se alguém me falasse que eu teria que trabalhar durante a noite visitando vários lugares pelo país não ía parecer terrível."

    na "E não é. Eu só acabo perdendo um pouco da minha vida pessoal."

    mc desculpa "Você é meio workaholic?"

    na "Não. Bom... eu acho que não. O trabalho não é minha vida. É só... não sei... algo que eu tenho que fazer."

    mc zerado "Parece bem workaholic pra mim."

    na "É difícil de explicar."

    mc charmoso "Bom. Dá pra ver que esse assunto não é fácil pra você. E se a gente pedir alguma coisa pra beber?"

    na "É uma boa."

    mc normal "[nora]!"

    scene na3_bar7 with Dissolve(1.0)

    pause

    nora "Estão prontos pra pedir alguma coisa?"

    mc "Sim. Minha amiga aqui tá se sentindo meio down, traz uma bem forte por favor."

    nora "Você quer nossa especialidade?"

    na "Antes da bebida, queria dar os parabéns pra senhora."

    nora "Filha?"

    na "Com todo o respeito, a senhora já tem uma certa idade e fica a noite toda servindo. Isso não deve ser fácil."

    mc "N-natasha?!"

    nora "Ora, calma. Ela tá me elogiando."

    na "Claro. Quem dera eu aguentasse esse tranco daqui uns anos."

    nora "Pra ser sincera, eu preferiria estar em casa vendo a novela. Adoro drama."

    nora "Só que como eu vou fazer isso? Deixar uma dessas malucas atendendo no balcão?"

    nora "A forma que elas aprenderam atender clientes não serve aqui no balcão. Abrir perna e subir no pau não ajuda muito."

    "Essa velha..."

    na "Hahaha... imagino. Mas posso falar uma coisa pra senhora?"

    nora "Pode me chamar de [nora], filha."

    na "Desculpa. [nora], eu tenho bastante vontade de trabalhar aqui, sabia?"

    nora "Minha filha! Não fale isso nem brincando. Você tá devendo pra alguém?"

    na "Não."

    nora "Você tá ilegal no país ou precisa pagar a cirurgia caríssima da sua mãe?"

    na "Não. Por que?"

    nora "Então por que você quer essa vida, garota?"

    na "D-desculpa... eu só... pensei que seria divertido. É uma coisa tão diferente."

    "O que a [na] tá falando?"

    scene na3_bar8 with Dissolve(1.0)

    pause

    nora "Olha, filha. Eu não sou sua mãe e nem queria ser, mas o que você vê nessas suas séries e a realidade são bem diferentes."

    nora "Isso aqui é trabalho pesado. O que essas garotas passam não é fácil. Elas ralam muito e não ganham tão bem assim."

    nora "A maioria tá na dívida fodida. E ter que cuidar disso tudo é ainda menos divertido."

    na "Entendi... não queria falar merda."

    nora "Tá perdoada. Você ainda é uma criança."

    na "E como a senhora aguenta manter tudo nos trilhos?"

    nora "Não é fácil, não, querida. É preciso pulso firme. Não só com as meninas, mas com os usuários também. Tem muito velho folgado."

    nora "Acham que dinheiro compra tudo. São grossos, nojentos, e quanto mais macho, mais querem enfiar algo na bunda."

    "Como a conversa chegou nisso?"

    na "E você que cuida disso tudo?"

    nora "Claro. Quem mais?"

    na "E o dinheiro também. Tudo você."

    nora "Sim. Tá vendo por que eu não posso ver a novela? Mas o último capítulo eu não perco. Já são mais de 50 anos, filha. Nunca perdi."

    na "E vem muito figurão aqui?"

    nora "Figurão? Ei, [mc]! Essa moça trabalha na sua revista?"

    mc desconfiado "Hm? Não..."

    nora "Então é policial. Não para de me interrogar aqui."

    na "Haha... desculpa, [nora]. Não queria incomodar."

    nora "Olha pra esse homão da porra do seu lado. Eu vou trazer a bebida de vocês e vê se dá mole pra ele."

    na "Com certeza. Esse aqui é pra casar."

    nora "Xii... quando uma garota fala isso de você, filho... é porque ela não quer nada."

    mc "M-mas-"

    nora "Tô brincando! Mas se você enrolar demais, ela vai se cansar."

    na "Ouviu, [mc]?"

    mc "[na]?"

    nora "Eu vou deixar vocês. Já volto."

    scene na3_bar4 with Dissolve(1.0)

    pause

    mc "Você tá legal?"

    na "Tô. Acho que essa conversa me deixou um pouco animada, só isso."

    menu:
        "Eu gostei de você assim.":


            mc "Eu gostei de você assim. Mais animada, interessada."

            na "Obrigada..."

            mc "Que foi?"

            na "Nada."

            mc "Hm."
        "Caraca. Nem tá parecendo você.":


            $ natasha_seducao += 2

            mc "Essa aí não era a [na] que eu conheço."

            na "Imagino... eu não costumo ouvir tanto minha voz desse jeito. É até estranho."

            mc "Então-"

            na "Não se preocupe com isso, [mc]."

            mc "Ok, então."
        "Melhor não falar nada":


            $ natasha_seducao += 1

            "Vou ficar na minha. Mas que ela tava bem diferente ela tava."

            mc "..."

            na "..."

            mc "É..."

    na "[mc]..."

    mc charmoso "Oi?"

    scene na3_bar9 with Dissolve(1.0)

    pause

    na "Você acha que eu sou muito estranha?"

    mc charmoso "Estranha? Por que?"

    na "Eu não sou muito boa em lidar com as pessoas. Eu já fiz vários testes psicológicos e sempre dá inabilidade social."

    mc "Conversando com a [nora] você parecia bem enturmada."

    na "Não. É diferente. Esse caso não conta."

    na "Quando a gente conversa. Você... o que você sente?"

    mc desconfiado "O que eu sinto?"

    na "É. O que você sente conversando comigo?"

    mc envergonhado "Eu não sei exatamente como responder isso..."

    if na1_beijo:

        mc charmoso "Mas... você esqueceu que a gente se beijou?"

        na "Ah... n-não."

        mc "Eu achei incrível aquelas noites com você. Você foi meio defensiva no começo, mas acho que no fim você se abriu comigo."

        na "Sei... eu não sei por que a gente se beijou. Eu não estava esperando aquilo."

        mc charmoso "Às vezes as coisas só acontecem, sabe?"

        na "Eu não entendo muito isso, mas talvez seja verdade. E tirando isso?"

    mc normal "Assim, Se eu tivesse que falar algo, eu diria que você é na sua. Você é uma mulher compenetrada."

    na "Acredito que sim..."

    mc "Você parece sempre focada no que tem que fazer. Você também não abre muita brexa pra gente se aproximar."

    na "..."

    mc "Você é linda, charmosa, mas esse seu jeito pode afastar um pouco as pessoas."

    na "E você? Digo... você vai se afastar?"

    mc envergonhado "Eu? Acho que eu sou meio insistente..."

    na "Isso é bom, [mc]."

    mc "Até eu começar a encher seu saco..."

    na "Não. Você tem razão no que você falou. Eu tenho bastante dificuldade em me abrir e me relacionar."

    na "Pessoas assim, iguais a mim, precisam de pessoas insistentes. E é engraçado... Você é estranho, sabe?"

    mc zerado "Acho que eu já ouvi isso antes..."

    na "Eu não falo isso como uma coisa ruim. Você é só diferente... eu me sinto à vontade falando com você."

    scene na3_bar10 with Dissolve(1.0)

    pause

    mc "Agora não sei se você tá me elogiando ou não..."

    na "Eu sinto que a conversa flui quando eu estou falando com você. Normalmente minhas conversas não são assim."

    na "É normal ficar aquele silêncio chato e desconfortável. Parece que nem eu e nem a pessoa sabemos como conversar."

    mc "Acho que jornalista tem esse poder de tá sempre falando..."

    na "Mas você não fala demais. É na medida certa. Acho que... uma das causas... é que você presta atenção."

    na "Tô pensando isso agora. Quando eu falo, eu sinto que você realmente me escuta. Você me responde com algo sempre interessante."

    mc "É o mínimo, né?"

    na "Hoje em dia não é tão mínimo assim. Várias vezes eu falo com alguém e a pessoa simplesmente pega o celular ou só fica no 'a-hã'."

    na "Pra uma pessoa que já tem dificuldade... isso é muito difícil."

    mc "Bom, pode ficar tranquila. Eu acho conversar com você super interessante. Inclusive ainda pretendo descobrir seu trabalho."

    na "Ideia fixa..."

    nora "Jovens. A bebida chegou."

    scene na3_bar11 with Dissolve(1.0)

    pause

    na "Opa! Tava ansiosa pra experimentar!"

    mc "[nora]... essa é A BEBIDA?"

    nora "Sim. Nossa especialidade."

    mc "N-natasha... acho melhor você não beber isso."

    na "Eu já ouvi falarem muito desse drink, mas nunca experimentei. Eu tô super ansiosa, [mc]."

    "Se a [na] tomar isso ela vai ficar louca. Eu não posso deixar is-"

    "Pera! Se ela ficar louca... huhuhu... Não! Não posso me aproveitar dela assim. Mas se ela se soltasse só um pouquinho..."

    "Merda... E agora? O que eu falo pra ela?"

    menu:
        "Eu acho que você não deve beber.":


            $ natasha_seducao += 1

            mc "Eu acho que você não devia beber, não... isso aí é forte pra caramba."

            na "Mais que os drinks do cassino?"

            mc "Haha! Muito mais, [na]. Sem comparação."

            nora "O garoto tem razão. Você vai sentir a cabeça um pouco mais leve."

            mc "É um pouco pior que isso."

            na "Hmmm... hoje eu quero me divertir, [mc]. Eu vou tomar."

            mc "V-você tem certeza?"
        "É uma experiência única. Vai firme.":


            mc "Essa bebida aí é do cão. Você vai ter uma experiência que nunca teve antes."

            na "Tá me deixando empolgada!"

            mc "Vai firme."

    na "Sim. Passa pra cá."

    nora "Vou pegar. Um segundo."

    scene black with dissolve

    na "{i}gulp{/i}"

    scene na3_bar12 with Dissolve(1.0)

    pause

    na "{i}puuaahhh{/i}"

    na "Caraca... o que tá acontecendo?!"

    mc preocupado "[na]..."

    nora "Hahaha... boa sorte com a garota agora."

    na "Meu Deus, [mc]. Minha cabeça tá girando!"

    mc "Tudo bem. É normal."

    na "Poxa vida! Eu sinto um negócio nas minhas pernas..."

    mc envergonhado "..."

    na "Fazia muito tempo que eu não me sentia assim. É muito bom..."

    na "[nora], tem certeza que eu não posso trabalhar aqui? Eu posso deixar um homem louco..."

    nora "Não duvido, filha. Você parece de porcelana. Mas tá mais pra uma puta de luxo."

    na "Será que é mais gostoso sair com alguém só por dinheiro?"

    nora "Hahaha! Você tem espírito, garota."

    na "[nora]... como eu entro nessa vida? Como você escolha uma garota?"

    nora "Eu... espera. Você é realmente bem xereta, hein?"

    na "Eu só queria uma chance..."

    nora "Ainda com isso na cabeça, menina? Você se comporte."

    mc "[na], você precisa pegar leve. Sua cabeça não tá certa agora."

    na "[mc]..."

    scene na3_bar13 with Dissolve(1.0)

    pause

    na "Você pagaria pra ir pra cama comigo?"

    mc envergonhado "Que pergunta..."

    na "Por favor me responde..."

    menu:
        "Prefiro não responder isso.":


            mc envergonhado "Olha, eu prefiro não responder isso. Não tem nada a ver essa pergunta."

            na "Como assim?! Eu quero saber se você transaria comigo se eu fosse uma garota de programa."

            mc "[na]... eu não me sinto confortável de falar sobre isso com você. A gente nem se conhece direito."

            na "Tudo bem. Mas eu esperava mais confiança de você, [mc]."

            mc "Haha... ok."
        "Não. Não curto pagar por sexo.":


            $ natasha_seducao += 1

            mc charmoso "Não. Mas não por sua causa. Eu não curto pagar por sexo."

            na "Mesmo se fosse pra transar comigo?"

            mc "Mesmo se fosse você. Eu disse que não tem nada a ver com você ou com qualquer outra garota, é uma questão de princípio."

            na "Não sei... acho que se você olhasse pras minhas pernas agora... talvez você mudasse de ideia."

            mc envergonhado "Haha... quem sabe... mas acho que não."
        "Claro que eu pagaria.":


            $ natasha_seducao += 2

            mc safado "Eu pagaria com certeza. Só me falar o valor."

            na "Hmmm... e se eu cobrasse... C$ 2.000? Ainda aceitaria?"

            mc charmoso "Com certeza. Se eu pudesse, eu pagava com a minha casa pra ter uma noite com você."

            na "Talvez... se a [nora] permitir, quem sabe..."

            nora "Essa garota tá fora de controle! Essa vai ser boa."

    mc envergonhado "[na]... você não tá pensando direito."

    na "Claro que tô, [mc]. Eu só tô um pouco mais feliz. Mas ainda é minha cabeça."

    mc "Essa pergunta..."

    na "Que foi? Uma garota não pode querer saber se um homem interessante pagaria pra fazer sexo com ela?"

    mc "Talvez... mas chegar a perguntar... aí já é outra história. Essa bebida realmente é uma coisa de louco."

    na "Eu só sei que eu tô adorando tudo isso. A sensação é indescritível. Esse calor subindo do meio das minhas pernas até minha cabeça..."

    na "Quem dera eu pudesse me sentir assim todos os dias."

    nora "..."

    na "Se pelo menos eu pudesse mostrar pra [nora] que eu levo jeito..."

    mc preocupado "[na]... Acho que a gente dev-"

    ce "Com licença."

    mc surpreso "Você!"

    scene na3_bar14 with Dissolve(1.0)

    pause

    ce "Desculpa, mas não consegui deixar de escutar vocês conversando."

    na "Nossa... garota, você trabalha aqui."

    nora "[ce], o que você quer? Eu já disse que não quero ver você vestindo isso."

    ce "Eu só queria conversar com essa mulher linda por um segundo."

    mc "Com a [na]?"

    ce "Então seu nome é [na]? Você é maravilhosa. Com certeza deixaria qualquer homem louco."

    nora "..."

    na "Obrigada. Você também, garota. Olha pra esse corpo. Quem dera eu tivesse um corpo desses."

    ce "[mc], posso roubar ela rapidinho?"

    menu:
        "Claro. Fique à vontade.":


            mc "Claro. Se ela quiser, não vou interromper as garotas."

            ce "Obrigada. Eu acho que ela vai gostar bastante do que eu vou falar."

            mc "Hmm..."
        "Ela tá meio alta. O que é?":


            $ natasha_seducao += 1

            mc "Olha, [ce], ela tá meio alta. Não sei se é uma boa agora."

            na "Você sabe que você não é meu pai, né? Ela só tá sendo educada."

            ce "Vai ser melhor ainda com ela assim."

            ce "Ela disse que queria trabalhar aqui. Daí eu pensei que talvez ela possa mostrar os dotes dela."

            mc "Você tá falando sério? Assim? Do nada?"

            ce "É só uma brincadeira. E nem tem muita gente no clube hoje."

            mc "Olha, eu sei lá. Mas eu não sou o pai dela mesmo."

            ce "Eu prometo que vai ser rapidinho. E acho que você vai gostar."

            mc "Ok..."

    ce "É [na], né? Pode vir comigo?"

    na "Claro, linda."

    ce "Eu vou te mostrar uma coisa interessante. Vem."

    nora "[ce]... não apronte..."

    scene na3_bar15 with Dissolve(1.0)

    pause

    "O que será que elas estão falando? Queria saber..."

    "A [na] parece, sei lá... fora da minha realidade. Quando eu tô com ela eu sinto que não importa o que eu fale, nada muda o que ela tá pensando."

    "É realmente complicado ficar com alguém assim."

    "Mas ela é tão gata, linda mesmo. E esse charme dela. Bem que podia rolar alguma coisa com a gente..."

    if na1_beijo:

        "E a gente se beijou aquela vez. Mas eu sinto ela exatamente igual antes. Será que ela não gostou?"

    "Agora, essa bebida... ela tá realmente parecendo outra pessoa. É uma doideira. De onde será que veio essa merda?"

    "Se bem que... quando a [nora] estava perto ela já parecia meio diferente. Parecia mais alegre."

    "Será que ela é meio quietona só comigo? Será que eu tô pegando pesado com ela? Não acho, mas sei lá..."

    nora "Você vai deixar essas duas sozinhas desse jeito?"

    mc "Que foi?"

    nora "A [ce] é uma garota problemática. Eu fico sempre com os dois olhos em cima dela."

    "Eu lembro do [us] falando que a [ce] é um caso diferente aqui. Que ela não se apresentava igual outras garotas."

    "O que será que ele tava querendo dizer com isso?"

    nora "Parece que elas terminaram."

    mc desconfiado "O que será que elas vão fazer?"

    scene distrito_clube visao with Dissolve(1.0)

    pause

    ce "[mc]. Pode vir aqui?"

    mc desconfiado "No palco?"

    ce "Isso. Vem aqui com a gente."

    mc surpreso "V-vocês vão subir?!"

    na "Calma, [mc]. Você vai ver."

    scene na3_bar16 with Dissolve(1.0)

    pause

    mc "O que você tá fazendo aí?"

    na "A [ce] é uma garota que trabalha aqui."

    mc "Eu sei. Tô perguntando você, [na]."

    na "Ah. Ela só me chamou pra gente se divertir um pouco."

    mc "Tá. E vai ser no palco?"

    na "Você já vai ver. Aposto que você vai gostar, [mc]."

    menu:
        "Tô meio preocupado com você [na]...":


            mc "É... eu tô meio preocupado com você, [na]. Aquela bebida é meio forte."

            na "Não se preocupe comigo. Acho que até o efeito já tá passando."

            mc "Até seu jeito de falar mudou."

            na "Por que você tem que ser assim tão controlador?"

            mc "Controlador? Eu só... tudo bem, deixa pra lá."
        "Se for envolver você e essa barra com certeza.":


            $ natasha_seducao += 1

            mc "Olha, se esse planinho de vocês envolver essa barra americana e você... só falar onde eu assino."

            na "Parece que você matou a charada."

            mc "Ainda não tô acreditando que é isso mesmo."

    na "Só curte o show, bobinho."

    "Bobinho? Essa mina tá muito doida. A [na] nunca ia falar desse jeito."

    "Se bem que pensando aqui... talvez o melhor é só aproveitar mesmo. Ela é adulta, se ela quer dançar foda-se."

    "O problema é que isso é um lance totalmente diferente pra ela eu acho. E se ela vai passar muita vergonha?"

    "Uma gata dessas passando vergonha... que pecado."

    ce "[na]. Faz o primeiro movimento que eu falei pra ele."

    na "Perfeito."

    scene na3_bar17 with Dissolve(1.0)

    pause

    "U-uou..."

    ce "Isso, [na]. Você tá demais, garota. Não tá, [mc]?"

    mc "E-eu..."

    menu:
        "...":


            mc "..."

            na "[mc]?"

            mc "Eu-"
        "T-tá sexy...":


            $ natasha_seducao += 2

            mc "V-você tá bem s-sexy, [na]..."

            na "Obrigada, senhor. Será que você não tem um trocado aí?"

            mc "E-eu... é..."

    ce "Você deixou ele paralizado."

    na "Prepara o bolso... eu tô só começando."

    ce "Vou deixar o palco pra você. Arrebenta, gata."

    window hide

    pause

    scene na3_bar18 with Dissolve(1.0)

    pause

    "Caraca... a [na] leva jeito pra isso..."

    window hide

    pause

    scene na3_bar19 with Dissolve(1.0)

    pause

    "Homem" "{i}Fiu-fiuuuu{/i}"

    "Senhor" "Nossa! Quem é essa delícia?!"

    na "..."

    window hide

    pause

    scene na3_bar20 with Dissolve(1.0)

    pause

    "Homem" "Gostosa! Que raba, hein?!"

    "A [na] tá fazendo sucesso..."

    "Senhor" "Essa aí se sentar nem levanta mais depois!"

    "Homem" "Haha! Na sua idade, tu que não levanta!"

    "Mano, eu sei que ela tá sexy e tudo, mas esses caras também são escroto. Não pode só ver?"

    "É como se esses caras precisassem mostrar pros outros que eles gostam de mulher. No fundo deve ser tudo enrustido."

    window hide

    pause

    scene na3_bar21 with Dissolve(1.0)

    pause

    ce "E aí? Gostaram da [na]?!"

    "Homem" "Muito gostosa!"

    "Senhor" "Aprovada!"

    ce "Uma última pra vocês. Só porque são um público tão fofo e especial."

    ce "{size=20}Abaixa bem devagar.{/size}"

    na "{size=20}Tá.{/size}"

    window hide

    pause

    scene na3_bar22 with Dissolve(1.0)

    pause

    "Opa!"

    "Homem" "Opa!"

    "Senhor" "Opa!"

    window hide

    pause

    scene black with Dissolve(1.0)

    "Caralho... a [na] foi bem demais. Sinceramente, não esperava isso não. Se pá ela vai convencer a [nora]."

    "Se eu-"

    ce "[mc]. Vem aqui com a gente."

    mc desconfiado "T-tá."

    scene na3_bar23 with Dissolve(1.0)

    pause

    ce "Garota... você foi incrível."

    na "Obrigada pela ajuda."

    ce "Não foi nada. Foi bacana, não foi, [mc]?"

    mc normal "Caraca, [na]. Você realmente leva jeito pra coisa."

    na "O que você quer dizer com isso?"

    mc charmoso "Que eu gostei bastante da sua apresentação."

    na "Devido às circunstâncias, isso é meio inapropriado, não acha?"

    mc preocupado "M-mas-"

    na "[ce]... você acha que isso é suficiente?"

    ce "Não sei, por isso chamei o [mc]. Ele parecia tá gostando."

    mc envergonhado "..."

    ce "Mas com certeza ela vai lembrar de você. Isso eu tenho certeza."

    na "Faça a sondagem e me fale qualquer coisa, ok?"

    ce "Pode deixar."

    "Quê? Que tá acontecendo aqui?"

    mc desconfiado "Você tá legal, [na]?"

    na "Sim. só um segundo. Nós já conversamos, ok?"

    mc preocupado "O-ok."

    scene na3_bar24 with Dissolve(1.0)

    pause

    ce "O [mc] tá com você?"

    na "Não. Mas ele é confiável."

    ce "Eu também achei quando vi ele com o Black Cash."

    na "Então fica certo assim. Preciso que você me passe tudo o que acontece."

    ce "Aliás, conseguiram uma foto da sua amiga. Eu tenho quase certeza que vi alguém com um celular."

    na "Isso é muito sério, [ce]. Eu não acredito que preciso ficar me preocupando com isso."

    ce "Eu tava com ela, e senti uma coisa. Quando olhei pra trás tinha um vulto, mas eu vi de relance. Acho que era um celular."

    na "Como que alguém consegue fazer isso aqui? Vocês precisam de câmeras."

    ce "Câmeras? Aqui? Você acha que alguém ia fazer o que faz sabendo que tem câmera aqui?"

    ce "Além do mais, essa pica é de vocês. Eu só atendo quem me procura."

    na "Eu sei... se você descobrir alguma coisa me fala."

    ce "Certo. E sobre aquele outro neg-"

    na "Falamos isso da outra vez, ok? Agora... eu sinto que tem gente demais olhando pra gente."

    "Acho que essa foi pra mim. Melhor eu dar o fora daqui."

    "Ou..."

    menu:
        "Eu vou esperar pra lá, pessoal.":


            $ natasha_seducao += 2

            mc charmoso "Agora que já dei minha opinião super relevante, vou esperar vocês lá no bar."

            ce "Não precisa, [mc]. A gente só tá conversando."

            mc "Relaxa. Acho que vou beber algo."

            na "Eu já vou sair também."

            mc "Ok, te espero lá."

            ce "Se a gente não se ver mais, até outro dia."

            mc "Até."

            scene black with Dissolve(1.0)

            scene na3_bar25 with Dissolve(1.0)

            pause

            "O que será que tá acontecendo aqui? Uma hora a [na] parece louca pela bebida e agora ela voltou ao normal."

            "Certeza que a bebida ainda tá fazendo efeito. O efeito demora horas pra passar."

            "Sei lá..."

            "Não consigo juntar os pontos. Não sei o que ela tá fazendo aqui no clube. Não sei por que ela quis beber isso ou dançar pole dance."

            "Também não sei como elas viraram amigas assim de uma hora pra outra..."

            "Eu só queria passar um tempo massa com a [na], mas parece que nunca dá certo."

            "Aahhh..."
        "Foda-se, vou ficar.":


            "Tenho nada com essas duas. Eu vou é ficar e xeretar mesmo. Sou um jornalista ou não?"

            ce "Ela tá olhando, mas não tem problema. Não dá pra ouvir."

            ce "Eu vou precisar de ajuda pra tirar elas daqui. Certeza que ninguém vai ficar feliz com isso."

            na "Você diz... eles?"

            ce "Claro. Não é só uma questão com quem é daqui. Isso envolve eles também."

            na "Concordo. Se a gente for fazer, vai precisar de uma boa operação..."

            ce "Sim..."

            na "Não desista. Calma, a gente tá dando um jeito nisso. Com sua ajuda, sei que as coisas vão progredir."

            ce "Ok. Eu vou continuar o tanto que eu puder."

            na "Obrigada. Falo isso em nome de todos. Sem você nunca daria certo."

            ce "Eu também vou tirar algo pra mim, então não precisa agradecer."

            na "Então é isso. Eu volto logo."

            ce "Tá bom. Até outro dia, [mc]."

            mc charmoso "Opa. Até."

    na "Vamos?"

    mc "Opa, claro."

    scene black with Dissolve(1.0)

    "..."

    scene distrito2 with Dissolve(1.0)

    pause

    na "Então... Eu gostei do clube e você?"

    mc envergonhado "Curti também. Mas..."

    menu:
        "Pra onde a gente tá indo?":


            mc desconfiado "Pra onde a gente vai agora?"

            na "A noite ainda tem um tempo. Tava pensando em andar um pouco. O que você acha?"

            mc charmoso "É uma boa. Vamos, sim."
        "Melhor eu ficar quieto e seguir ela":


            "Vou ficar de boa e deixar ela guiar."

    scene na3_rua1 with Dissolve(1.0)

    pause

    "Mano... ainda não entendi o que rolou lá com a [ce] e a [na]. Eu tô me sentindo tão fora da curva, sei lá..."

    mc "..."

    na "Tudo bem? Você parece meio quieto."

    mc "É que... [na]... o que aconteceu lá no clube?"

    na "Que foi?"

    mc "Você sabe do que eu tô falando. Foi tudo muito estranho."

    na "Bom... não sei o que te falar. Eu estava lá pelo meu trabalho, e quando você chegou eu pensei em me divertir um pouco."

    na "Acho que aquela bebida é meio forte demais."

    mc "Você não tá sentindo mais nada?"

    na "Ah! Sim, estou. Não tão forte quanto antes, mas ainda sinto, sim."

    mc "Sei..."

    na "[mc]... eu sei que pode parecer tudo meio estranho, mas essa sou eu. Se você gostar da minha companhia, a gente podia se ver mais vezes."

    na "Só que... se você não gostar de sair comigo... eu vou entender também."

    mc "Não é isso. Eu só, sei lá, me sinto meio de fora das suas coisas. Não sei nada sobre você eu acho."

    mc "Não sei seu trabalho, não sei por que você vai no Cassino do Barão ou por que tava no clube de sadomasoquismo hoje."

    mc "É um pouco cansativo sempre se sentir por fora."

    na "Entendo... desculpa."

    mc "Não tô pedindo desculpas. Eu só queria... eu acho que o que eu queria era que você me incluísse mais nas suas coisas."

    mc "Quem sabe contar alguma coisa que me ajude a entender hoje."

    scene na3_rua2 with Dissolve(1.0)

    pause

    na "Desculpa por tratar você como um burro, [mc]."

    na "Eu pensei que talvez você fosse só ignorar tudo e curtir comigo. Mas parece que você não consegue."

    mc "..."

    na "Acho que eu só estava buscando uma companhia ingênua o suficiente pra que a gente pudesse ficar só na superfície."

    na "Mas você não consegue, né?"

    mc "Não sei. Mas o negócio é que eu prefiro saber sobre as pessoas que eu conheço."

    na "Você sabe que isso não é o mais normal. Muitos iam ficar felizes em só tomar uns drinks, quem sabe algo a mais. Mas só isso."

    na "Você não precisa transformar todas as pessoas que você sai em um grande confidente."

    mc "Sei... mas eu te devolvo a pergunta. Por que você é assim? Por que você gosta de manter as coisas na superfície?"

    na "Porque é mais fácil. Você tem suas coisas, eu tenho as minhas. A gente não precisa um mexendo nas coisas dos outros. Eu não vejo nada de errado nisso."

    mc "Não é que é errado ou certo. Mas você às vezes não tem vontade de compartilhar suas coisas com alguém?"

    na "Não. Quando eu tentei fazer isso sempre deu algo errado... pra mim ou pra pessoa. Eu não quero viver isso de novo."

    mc "Você deve me achar um chato então."

    na "Não sei se... pensando bem, [mc]... Acho que é a primeira vez que uma pessoa dá tanta atenção pra mim assim."

    mc "Hm?"

    scene na3_rua3 with hpunch

    pause

    mc "A-ai. [na]?"

    na "Não sei se é a bebida... mas ouvir você falando assim me deixou com tanta vontade de beijar."

    mc "S-sério?!"

    na "Você mexe muito comigo, [mc]. Eu nunca me senti assim antes."

    menu:
        "E-e-e-eu!":


            mc "E-e-e-eu!"

            na "Sim, [mc]. Você. Eu tô louca pra beijar você agora."

            mc "N-natasha!! E-eu!"
        "Você também mexe comigo.":


            $ natasha_seducao += 2

            mc "Você também mexe muito comigo."

            na "Que bom. Eu fico feliz. Eu quero muito beijar você agora."

            mc "A-agora?"
        "Eu não vejo você dessa forma...":


            mc "E-eu agradeço, mas eu não vejo você assim. D-desculpa."

            na "Não fale isso, [mc]. Eu quero tanto você."

            mc "N-natasha! N-não tô entendendo."

    na "Eu tô sentindo um quente no meu corpo. Achei que já tinha passado o efeito da bebida. [mc]... será que a culpa é sua?"

    mc "Você quer fazer isso agora m-"

    na "Pega em mim, [mc]. Por favor. Aperta minha bunda agora!"

    mc "Natasha, não se-"

    na "Levanta minha saia e me sente, seu gostoso!"

    "O-o que eu faço? A mina tá no grau!"

    menu:
        "Não quero fazer as coisas assim.":


            "É tentador, mas não. Preciso colocar a cabeça no lugar. Óbvio que tá rolando alguma coisa aqui."

            mc "Eu não tô entendendo, [na]. E-eu não quero."
        "Se é ela que tá pedindo... demorou.":


            $ natasha_seducao += 2

            mc "Então vem aqui!"

            scene na3_rua4 with Dissolve(1.0)

            pause

            na "Isso, delícia! Que pegada!"

            mc "..."

            na "Isso, me pega..."

            "Eu não sei o que eu faço! Ela tá louca!"

            mc "[na]... e-eu..."

            na "Ai! Assim! Vem mais perto!"

            mc "!"

    na "{size=20}[mc]... presta atenção.{/size}"

    mc "{size=20}T-tá.{/size}"

    na "{size=20}O segurança do clube tá ali na esquina.{/size}"

    mc "Q-quê?!"

    scene na3_rua5 with Dissolve(1.0)

    pause

    na "{size=20}Xiu! Só fingi que a gente tá se pegando.{/size}"

    mc "{i}gulp{/i}"

    mc "{size=20}O-ok...{/size}"

    na "Você tá me deixando louca. Me pega logo."

    mc "P-pode deixar. Você tá me... deixando louco também. Ui."

    na "{size=20}'Ui'? Sério?{/size}"

    mc "{size=20}V-você me deixou nervoso!{/size}"

    na "Isso. Fala no meu ouvido, fala... eu tô toda arrepiada."

    mc "{size=20}Você é boa nisso... Você tá me dei-{/size}"

    na "{size=20}Calma. É só até ele ter certeza que a gente tá se beijando. Vê se se esforça também.{/size}"

    mc "O-ok... vou deixar você louca... baby..."

    na "..."

    "Merda! Eu nem sei o que eu tô falando! Eu sou só um cara normal! Não o 007!"

    "Já sei! E s-se eu só beijar ela!? Eu não vou precisar falar nada!"

    "N-não! Isso não seria certo... mas ela tá esperando eu falar alguma coisa e eu não sei o que falar! Eu tô tremendo!"

    na "[mc]... você quer?"

    "Cala a cabeça e toma uma decisão, idiota!"

    menu:
        "Não! Isso não é certo!":


            mc "E-eu gosto muito de você, [na]. Eu tô curtindo muito nossa noite."

            na "Você queria me embebedar lá no clube, né, safadinho?"

            mc "I-imagina..."

            na "Você fica tão fofo quando tá com vergonha."

            mc "Eu... você vai ver o que é fofo daqui a pouco."

            na "Hmm... alguém tá se animando..."

            mc "Se você continuar roçando em mim assim... ele vai ficar animado rapidinho."

            na "{size=20}Ele não tá indo...{/size}"

            mc "{size=20}E agora?{/size}"
        "Beijar ela":














            $ natasha_seducao += 2
            $ na3_beijo = True

            "Eu vou beijar ela. É s-só pelas aparências!"

            mc "Amor, eu não aguento mais."

            na "Isso, que-"

            mc "Vem aqui."

            scene na3_rua6 with Dissolve(1.0)

            pause

            na "Hmm!"

            mc "É isso que você queria, né, amor?"

            if natasha_seducao >= 20:

                na "Você me pegou de jeito..."

                mc "Não tava esperando, né?"

                na "Não... e isso é raro..."

                mc "{size=20}Tá funcionando?{/size}"

                na "Não importa. Deixa eu aproveitar mais um pouco."

                window hide

                pause

                scene na3_rua7 with Dissolve(1.0)

                pause

                mc "{size=20}A-assim ele vai acreditar.{/size}"

                na "{size=20}Vamos fingir mais um pouco pra garantir.{/size}"

                mc "{size=20}Por mim tá excelente.{/size}"

                na "{size=20}Então me beija.{/size}"

                window hide

                pause

                scene na3_rua4 with Dissolve(1.0)
            else:


                na "Isso. Me beija!"

                window hide

                pause

                scene na3_rua5 with Dissolve(1.0)

                na "Tá bom."

    na "Acho que eu não quero dormir em casa hoje, gato."

    mc "Quer ir pra minha casa?"

    na "Não... acho que eu não consigo esperar pra sentir você, bebê. Eu quero ir pro motel."

    mc "M-motel?!"

    na "Que foi? Eu não mereço um quarto legal?"

    mc "C-claro que merece."

    na "Então vamo logo, gostoso."

    mc "Vamos!"

    scene black with Dissolve(1.0)

    na "Esse aqui parece bom. Vem, vem!"

    mc preocupado "Você viu o preço a cada 4 horas?!"

    na "Vai valer à pena, docinho."

    mc "!"

    pause

    scene motel_geral with Dissolve(1.0)

    pause

    "Não acredito que eu tô em um quarto de motel com a [na]. Como as coisas chegaram a isso?"

    "Acho que eu nunca... nunca fui num motel com uma garota... o que eu falo?"

    mc envergonhado "Opa. O quarto é bonito..."

    "Isso é o melhor que você pensou, cara?"

    na "Aquele segurança era chato."

    mc envergonhado "Ah, o [mon]... ele parece um cara tão legal."

    na "Deve ser mesmo, mas ele é bem insistente. Deixa eu ver essa cama."

    "C-cama?!"

    scene motel_cama with Dissolve(1.0)

    "Cama de motel... A gente podia..."

    "Q-q-que que eu tô pensando?"

    na "Com licença."

    mc surpreso "Opa."

    scene na3_motel1 with Dissolve(1.0)

    pause

    na "Aahhh... finalmente eu tô deitada."

    mc envergonhado "Dia corrido?"

    na "Ah? Sim... muito... e não só hoje. Faz uns três dias que eu não durmo."

    mc surpreso "O loko! Três dias?!"

    na "Sim. Mas tudo bem... eu tô acostumada. Mas quando eu deito, eu tenho uma sensação tão boa."

    na "É como se toda a adrenalina deixasse meu corpo..."

    "Ela tá tão em êxtase que nem percebeu que eu posso ver tudo..."

    menu:
        "Melhor eu responder ela":


            mc normal "Entendi. Acho que você pode descansar um pouco agora."

            na "Nem pensar."
        "Admirar o corpo da [na]":


            $ natasha_seducao += 1

            scene na3_motel2 with Dissolve(1.0)

            pause

            "Só uma olhadinha... ela não vai perceber."

            "A [na] é perfeita. Esbelta, com essas pernas... ela seria uma excelente modelo."

            "A pele dela também é bem clarinha, tem até umas marquinhas."

            mc "..."

            window hide

            pause

    na "Você tem que falar comigo pra eu não dormir."

    mc envergonhado "O-ok."

    mc "Não sei que assunto a gente pode falar num motel."

    if na3_beijo:

        na "Olha..."

        scene na3_motel3 with Dissolve(1.0)

        pause

        na "Não esperava que você fosse me beijar daquele jeito aquela hora."

        mc envergonhado "Pra falar a verdade, nem eu... você falou pra eu interpretar e eu não sabia o que falar."

        na "Não é qualquer um que teria coragem de tomar a iniciativa assim, [mc]."

        na "Às vezes eu acho que você se dá pouco crédito. Você é um homem corajoso."

        mc charmoso "Obrigado. É mais legal quando os outros falam bem da gente ao invés da gente mesmo."

        na "Acho que eu entendo o que você quer dizer, mas confiança é importante."

        mc "É. Mas gente que se acha demais às vezes só esconde sua inabilidade."

        na "Talvez..."

        if na1_beijo:

            mc charmoso "Esse já foi nosso segundo beijo. A gente já pode considerar uma amizade colorida?"

            na "Haha... parece uma questão de conceito, mas antes de ter uma amizade colorida a gente precisa ver se a gente tem uma amizade."

            mc zerado "Isso foi meio frio."

    mc desculpa "Você... me considera um amigo?"

    scene na3_motel4 with Dissolve(1.0)

    pause

    na "Que tipo de pergunta é essa?"

    mc normal "Ué? É uma pergunta normal e você falou pra puxar conversa. Eu sou um amigo pra você ou um conhecido? Ou um nada?"

    na "Não sei... você é um conhecido..."

    if na1_beijo or na3_beijo:

        mc "Mesmo depois do nosso beijo?"

        if not na1_beijo:

            na "Aquele beijo não conta, [mc]..."

            mc charmoso "Tem certeza?"

        na "O que você quer dizer? Que a gente é tipo... como eles falam? Ficantes?"

        mc charmoso "Legal. Eu fico satisfeito sendo seu ficante..."

        na "Você fica? E eu devia me sentir lisongeada com isso?"

        mc "É sempre bom ter um cara nos seus pés."

        na "Haha... você tá exagerando agora."

        mc "Bom, se você acha, eu não..."
    else:


        mc envergonhado "Conhecido parece tão distante..."

        na "Ficou triste com isso?"

        mc charmoso "E se eu fosse seu... seu parceiro de esquemas?"

        na "Parceiro de esquema? A gente nem sabe o que isso quer dizer."

        mc envergonhado "Hmm..."

        na "Talvez só parceiro. Nos filmes policiais eles se chamam de parceiros, você já viu?"

        mc surpreso "Com certeza! E depois de hoje então!"

        na "Melhorou?"

        mc normal "Muito. De 'conhecido' pra 'parceiro'. Estou caminhando bem."

    na "Você é divertido, [mc]. Eu lembro da nossa conversa no Cassino, eu gostei bastante de passar tempo contigo."

    mc normal "Bacana. A gente podia fazer isso mais vezes."

    scene na3_motel5 with Dissolve(1.0)

    pause

    na "Não é assim tão fácil infelizmente..."

    mc charmoso "Por quê? É só a gente marcar um horário, um local e estar lá. Não me parece tão difícil."

    na "Eu não tenho tempo pra dormir. Imagina me encontrar com alguém, ter uma relação... mesmo que seja de amizade..."

    mc desculpa "As coisas tão assim mesmo?"

    na "Sim. Mas isso é algo que eu sabia quando comecei. Essa é a vida que eu escolhi pra mim."

    na "Eu sabia que eu ia ter que desistir de relacionamentos e qualquer outra coisa que não envolvesse trabalho."

    na "Até hoje eu vivi bem com isso."

    mc normal "ISso é uma coisa boa pelo menos."

    na "É... mas eu nunca tinha encontrado a mesma pessoa duas vezes igual você..."

    mc desconfiado "Hm? Posso sentar com você?"

    na "Claro. Fique à vontade."

    scene na3_motel6 with Dissolve(1.0)

    pause

    na "O que eu tava querendo dizer é que é mais fácil aceitar uma vida longe das pessoas quando você se mantém distante delas."

    na "Não sei se tudo mundo é assim, mas às vezes eu penso em encontrar alguém... talvez ter uma família. Eu não sou mais tão jovem."

    menu:
        "Mentira. Você tá muito bem.":


            $ natasha_seducao += 1

            mc charmoso "Que isso? Você tá brincando, [na]. Você tem a mente afiada, é linda, gostosa... nem vou falar mais pra não perder a linha."

            na "Obrigada... mas eu não tenho mais 18 anos, [mc]. Bem mais que isso aliás."
        "Acho que eu entendo.":


            $ natasha_seducao += 1

            mc desculpa "Acho que eu entendo o que você tá querendo dizer."

            mc "Parece que a vida tem tipo um calendário e tá todo mundo seguindo ele."

            na "Exatamente."

    na "Eu tô em uma idade onde as pessoas já tem marido, filhos. E eu não tenho nada. Eu fiquei pra trás. Eu tô muito longe disso tudo inclusive."

    na "Não tenho nenhum plano nesse sentido. E se você me perguntar... sinceramente eu nem quero isso."

    na "Eu gosto da minha vida como ela é agora. Eu estou cansada, de verdade, mas eu me sinto bem nessa vida. Não consigo me imaginar de outra forma."

    mc normal "Poxa, então tá tudo certo, [na]. Por que você quer mudar isso?"

    na "Porque às vezes... quando a gente encontra alguém legal... a gente pensa como nossa vida seria se fosse diferente."

    mc envergonhado "Não sei se eu entendi..."

    na "Eu sou uma pessoa que não gosta muito de meias palavras, [mc]."

    mc charmoso "Eu já percebi isso."

    na "Você é um cara legal. Eu me sinto bem com você. E eu fico um pouco triste de pensar que minha vida não permita passar mais tempo com você."

    mc envergonhado "Uou... isso foi bem direto mesmo. Eu nem sei direito o que falar. Obrigado..."

    na "Não é pra agradecer."

    mc normal "Olha... e eu tive uma ideia aqui."

    na "O que?"

    mc charmoso "Se realmente a gente não vai se ver de novo, e se a gente aproveitasse aquela banheira ali agora?"

    na "Agora?"

    mc "Claro. É agora ou nunca."

    scene na3_motel7 with Dissolve(1.0)

    pause

    na "Está me chamando pra entrar na jacuzzi em um quarto de motel? [mc], quais suas intenções comigo?"

    "Olhando pra [na] assim... puta que pariu... como ela é linda... que mina perfeita, mano."

    "Que homem não ia querer entrar numa banheira com ela?"

    "Mas será que eu devo? A gente pode ser só amigos também... Ela é super inteligente, interessante, e com certeza tá metida em alguma coisa grande."

    "Só de estar com ela com certeza eu tenho uma boa chance de achar pautas pra revista."

    menu:
        "É só pra gente se divertir mesmo.":


            mc normal "Sem segundas intenções. Só pra gente se divertir mesmo."

            na "Sério? Você tá sendo sincero comigo."

            mc "Eu juro."

            na "Então combinado. Acredito que vai ser divertido."

            mc "Opa. Tenho certeza que vai. Você primeiro por favor."

            na "Pode ir entrando que eu tenho que colocar meu sutiã. Sorte que eu trouxe ele."

            mc "Tá ok."

            jump na3_banheira
        "Você sabe o que eu quero.":


            $ na3_seducao = True

            mc charmoso "Você sabe muito bem o que eu quero."

            $ renpy.notify("Natasha está lembrando de suas ações passadas")

            na "Foi o que eu pensei. Mas você entendeu tudo o que eu disse, né?"

            mc "Sim. Acho que a gente pode se divertir como adultos... pelo menos hoje."

            na "[mc]..."

            if natasha_seducao >= 20:

                na "Eu aceito. A sua sorte é que eu trouxe um sutiã pra usar."

                mc charmoso "Sorte a minha. Mas se preferir entrar sem, eu não vou achar ruim."

                na "Talvez outro dia. Vamos?"

                mc "As damas primeiro."

                jump na3_banheira
            else:


                na "Bom, [mc]... acho que não. Quem sabe um outro dia, se a gente acabar novamente em um motel."

                mc envergonhado "Certeza? A água deve estar uma delícia."

                scene na3_motel4 with Dissolve(1.0)

                na "Imagino que sim, mas eu realmente não conseguiria relaxar. Temos que ficar de olho se alguém for entrar aqui."

                mc preocupado "Você acha que tem chance?"

                na "É uma chance pequena, mas mesmo assim é melhor ficar de olho."

                mc desculpa "Ok..."

                na "Por que você não me conta sobre suas aventuras de paparazzo?"

                mc envergonhado "Ixi... quantas horas a gente vai ficar aqui mesmo?"

                na "É tanto assim?"

                mc "Pior que é."

                na "Agora fiquei interessada, pode começar."

                mc concentrando "Bom... tudo começou no dia que eu ia ser despedido..."

                scene black with Dissolve(1.0)

                "..."

                na "Não creio!"

                mc envergonhado "Pois é..."

                jump natasha_e3_final

    label na3_banheira:

        $ na3_banheira = True

        scene black with Dissolve(1.0)

        "..."

        scene na3_motel8 with Dissolve(1.0)

        pause

        na "Que delícia, [mc]! Se eu soubesse que a água tivesse assim, não ia nem ter que pensar."

        mc charmoso "Eu disse."

        na "Você tinha toda razão. Só uma idiota negaria uma maravilha dessas..."

        na "Eu sinto a água batendo no meu corpo... é uma sensação incrível."

        mc "..."

        na "Eu estou parecendo uma idiota por falar tanto só de entrar na água aquecida?"

        mc charmoso "Idiota, não. Mas tá parecendo uma criança que ganhou seu primeiro videogame."

        na "Eu sabia que eu estava parecendo algo estranho... mas eu não consegui só manter pra mim essa sensação."

        mc charmoso "Não esquente. Foi fofo."

        if na3_seducao:

            scene na3_motel9 with Dissolve(1.0)

            pause

            na "E agora que estamos aqui? Eu estou super relaxando... o que você quer fazer?"

            mc charmoso "Seria um pecado atacar você agora que você tá se divertindo tanto. Vou deixar você curtir um pouco antes."

            na "Como você é bonzinho."

            mc "Nada como paparicar uma garota antes de levar ela pra cama."

            na "Você não tem nem vergonha de falar isso assim?"

            mc "É incrível como você é sincera. Tô tentando fazer o mesmo. Ser direto e mostrar segurança. Eu sou inabalável."

            na "Você sabia que quando a gente tem que falar algo, é porque a gente tá inseguro sobre aquilo, certo?"

            mc desconfiado "Hmm..."

            na "Não precisa ficar assim. Você ganhou pontos pela sinceridade."

            mc charmoso "Ok. Eu aceito. Mas acho que eu posso melhorar ainda mais sua estadia na banheira."

            na "Acho improvável, mas qual é sua proposta?"
        else:


            mc normal "Já que a gente tá aqui pra se divertir, tive uma ideia."

            na "Certo. O quê?"

        mc "Vou fazer uma massagem nos seus pés."

        na "Hmmm... você realmente sabe como fazer massagem?"

        if mc_massagem > 0:

            mc charmoso "Eu faço aulas. Não sou qualquer estranho com tara por pés. Você vai ver que eu sei o que eu tô fazendo."
        else:


            mc envergonhado "Não, mas se eu te machucar ou qualquer coisa me fala e eu paro."

        na "Ok. Como dizem, entrou na água é pra se molhar. Quero ver seu toque dos deuses."

        mc charmoso "Pode deixar. Deite e relaxe."

        scene na3_motel10 with Dissolve(1.0)

        pause

        mc "Pode me dar aqui."

        na "Boa sorte..."

        "Agora é a hora da verdade."

        if na3_seducao:

            "Motel... banheira aquecida... massagem... Cara, isso vai acabar muito bem."

            "É só eu não estragar tudo."
        else:


            "..."

        mc "E aí? Tá gostoso?"

        na "... Tá sim..."

        na "É interessante como só ter alguém tocando na gente pode ser tão diferente..."

        if na3_seducao:

            "Isso! Acho que tô indo bem!"

            "Ela tá relaxada... eu tô pegando nela, ela não tá achando estranho... ela parece bem relaxada mesmo..."

            "Agora eu posso avançar um pouco... talvez pegar na perna dela..."

        if mc_massagem > 4:

            "As aulas com a [m] tão surtindo efeito!"

        mc "Que bom que você tá curtindo."

        na "... Sim..."

        na "Hmm..."

        "Acho que eu nunca vi a [na] tão de boa assim. Normalmente ela é tão tensa, sempre com aquela expressão de preocupada."

        "Agora ver ela sorrindo assim... com os olhos fechados..."

        "Dá até uma felicidade, sei lá, ver alguém tão de boa assim."

        if na3_seducao:

            "Hora do próximo passo. Vou subir pra perna dela e talvez já ir pra um beijo... será que é demais?"

            "Melhor eu começar perguntando. Assim ela sabe o que eu tô pensando."

            mc charmoso "Posso massagear suas pernas agora? Ou suas costas?"
        else:


            mc normal "Quer que eu massageie suas costas? É melhor que os pés ainda."

        na "..."

        mc desconfiado "[na]?"

        na "..."

        if na3_seducao:

            mc zerado "N-não acredito... Sério isso?"

            na "..."

            mc concentrando "Claro que isso ia acontecer comigo..."

            mc zerado "Nem sei por que ainda crio expectativas..."

            "Talvez se eu tentar acordar ela..."

            mc normal "[na]. Ei..."

            na "..."

            "Tá bom..."
        else:


            "Caraca... será que ela dormiu? Tô ficando bom nisso de massagem mesmo."

        "Ela disse que tava cansada mesmo. Fazer o quê."



        label na3_premium1:

            pass

        menu:
            "Tentar acordar ela de novo":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_39

                    jump na3_premium1

                "Talvez... se eu chegar mais perto..."

                na "Huhuhu..."

                mc "N-natasha?"

                na "Você tava preocupado assim de me acordar?"

                mc "Pois é..."

                na "O que você queria fazer?"

                mc "Eu queria massagear... outra parte..."

                na "Tudo bem... vem aqui."

                scene black with dissolve

                scene natasha3_premium1 with Dissolve(1.0)

                pause

                na "Ai..."

                mc "Eu... você é linda demais, Natasha..."

                na "Acho incrível que a gente tá nesse clima até agora... em um motel... e você ainda não fez nada..."

                mc "Será que eu sou bundão demais? Eu só... não queria te pressionar, sabe?"

                na "Você não é 'bundão', [mc]... pelo contrário... você é o homem mais corajoso que eu vi na capital até agora."

                na "Se você soubesse a quantidade de gente mesquinha... de homens nojentos que eu encontrei..."

                mc "Eu não sou eles. Eu nunca machucaria você, [na]."

                na "Engraçado que eu acredito em você. Quando é você quem fala isso, realmente parece de verdade."

                mc "Eu falo isso... mas eu tô muito afim de ficar contigo..."

                na "Desde o cassino?"

                mc "Sim... desde aquela noite que a gente... eu acho que a gente tem muita química."

                na "Eu tô afim de descobrir se a gente tem mesmo... o que você acha?"

                scene natasha3_premium2 with Dissolve(1.0)

                pause

                na "Hmmm..."

                mc "Eu também quero descobrir, [na]..."

                na "Melhor ainda descobrir na prática.. nnghh..."

                mc "Sim... você é tão gostosa."

                mc "Esse era o momento que eu tava esperando desde que você me seduziu lá no cassino."

                na "Hmm... eu te seduzi, é? Acho que foi você que me conquistou."

                mc "Eu não sei o que um cara como eu fez pra poder ficar com uma mulher perfeita igual você."

                na "Beijar bem desse jeito é uma das coisas... ah..."

                mc "Então deixa eu focar nisso."

                na "Isso... me beija toda aí, [mc]..."

                na "Aah..."

                na "E se a gente continuar fora da piscina?"

                mc "Claro. Onde você quiser."

                na "Vem."

                scene black with dissolve

                scene natasha3_premium3 with Dissolve(1.0)

                pause

                na "Hmmm!"

                mc "Assim que você queria?"

                na "Assim mesmo. Deixa eu sentir sua boca, sua língua... aah..."

                mc "Você é gostosa demais. Eu quero você inteira."

                na "Então me beija mais. Me deixa pronta pra você, [mc]."

                mc "Nnghh!"

                na "Aah!"

                "Eu realmente tô ficando com ela! Não acredito!"

                "A Natasha é tão perfeita... não vejo a hora de tirar essa roupa dela e experimentar tudo."

                "E pensar que eu ia pegar uma gata dessas. Uma mulher que tá em outro nível assim."

                "Eu vou provar pra ela que eu sou o melhor homem que ela já ficou!"

                mc "Deixa eu tirar isso aqui de você. Deixa eu ver você melhor."

                scene natasha3_premium4 with Dissolve(1.0)

                pause

                na "Ah..."

                na "Pode fazer o que você quiser, só não para de me beijar."

                mc "Não paro."

                na "Eu tô cada vez mais molhada, [mc]..."

                "Ela tá me chamando pra ir até o fim. É isso que ela tá falando?"

                "Ela disse que os homens foram cuzões com ela. Será que eu devia tomar cuidado agora?"

                "Será que beijar é o suficiente pra esse primeiro encontro aqui?"

                na "Eu nunca... beijei alguém assim... aah... tô até sem ar, gostoso."

                mc "Você quer mais? Quer sentir mais gostoso?"

                na "O que você quer?"

                "Ela tá deixando pra mim... e agora? O que eu faço?"

                menu:
                    "Eu vou continuar só beijando":


                        mc "Pra mim, só beijar você já é demais. Você é deliciosa."

                        na "Então beija... vamo se pegar até amanhecer!"

                        mc "Hmmmm!"
                    "Eu vou tirar toda a roupa dela":


                        mc "Eu quero tudo. Eu vou tirar tudo e aproveitar tudo."

                        na "Espera..."

                        mc "Hm?"

                        scene black with dissolve

                        na "Eu tiro... olha aqui."

                        scene natasha3_premium5 with Dissolve(1.0)

                        pause

                        na "Você quer?"

                        mc "É o que eu mais quero no mundo!"

                        na "Então vem..."

                        mc "Deixa eu admirar mais um pouco..."

                        na "Você vai me deixar com vergonha assim..."

                        mc "Não precisa ter vergonha. Você é uma obra de arte, [na]."

                        na "Você continua me elogiando desse jeito..."

                        mc "Isso não tem nada de elogio. É a mais pura verdade."

                        na "[mc]..."

                        mc "Você não sabe como eu tô afim de ter você inteira. E eu quero que você aproveite também."

                        na "Eu tô pronta. Eu quero você dentro de mim agora."

                        mc "Então tá. Eu também tô pronto. Aqui vou eu."

                        scene black with dissolve

                        scene natasha3_premium6 with Dissolve(1.0)

                        pause

                        na "A-aangh!"

                        mc "Eu tô dentro de você, [na]! Você é uma delícia!"

                        na "Eu tô sentindo você dentor de mim! Nghh!"

                        na "Você também é uma delícia. Me come, [mc]."

                        mc "Nnnghh!"

                        na "Aahhn! Aaahn!"

                        "Que delícia de buceta que ela tem!"

                        na "Ainn! Hmmm!"

                        mc "Como você geme gostoso."

                        na "É porque tá bom assim! Ahnnn!"

                        mc "Eu sei! Tá bom mesmo! Eu vou fazer mais!"

                        na "Aaaiign!"

                        scene natasha3_premium7 with Dissolve(1.0)

                        pause

                        na "Ai, [mc]! Ahnn!"

                        mc "Não consigo parar de olhar pra você mesmo te comendo!"

                        na "Hmmnn!"

                        na "Você gosta tanto assim?!"

                        mc "Aah! Eu ainda não tô acreditando que eu tô transando com você!"

                        na "Você tá! Aaahhn! Continua assim! Tá bom demais!"

                        menu:
                            "Continuar até ela gozar":


                                mc "Você vai gozar gostoso, [na]!"

                                na "Eu vô! NNGHH!!"

                                na "ASSIM! VAII!! AANNH!!!"

                                na "METE GOSTOSO!!!"

                                mc "AAAGHH!"

                                scene natasha3_premium10 with hpunch

                                pause

                                na "AAAANNNGH!!!!"

                                mc "Tô gozando também! AAGH!!!"

                                na "Aaaghh! Aaahnn..."

                                na "Que delícia! Que delícia, [mc]! Tô gozando de verdade!"

                                na "AAAINNNN!!!"

                                na "Aah... aaah..."
                            "Meter mais forte":


                                mc "Eu não consigo parar! Eu quero mais!"

                                na "[mc]?!"

                                scene natasha3_premium8 with hpunch

                                pause

                                na "Aii! Calma!"

                                mc "Você é gostosa demais, [na]!"

                                na "Nnnghh! Você parece um animal!"

                                mc "Eu tô excitado demais! Você é gostosa demais!"

                                na "Ahn! Aaii!"

                                mc "Eu vou gozar!!!"

                                na "Goza! Goza, gostoso!"

                                scene natasha3_premium9 with hpunch

                                pause

                                mc "AAGHH!"

                                na "NNGHH!!!"

                                mc "Que delícia!"

                                na "Sim! Sim... nnghh..."

                                mc "Foi incrível... você gostou também?"

                                na "Claro! Nghh... ainda tô sentindo, [mc]..."

                                mc "Hmmm..."

                scene black with Dissolve(1.0)

                "..."

                scene natasha3_premium11 with Dissolve(1.0)

                na "Você fez muito mais do que eu imaginava, [mc]..."

                mc "E olha só pra isso... eu fiquei com uma deusa..."

                na "Você gosta?"

                mc "Gostar? Olha pra isso aí... é a coisa mais linda que já entrou no Distrito."

                na "Não exagera... aquelas garotas do clube são lindas também, mas obrigada pelo elogio."

                mc "Você não entende como você é perfeita, [na]..."

                na "Você que foi perfeito esta noite. Fazia muito tempo que eu queria ter um momento íntimo decente com alguém."

                na "Aliás... depois dessa... acho que eu vou dar um pulo na banheira."

                mc "Boa ideia."

                na "Se fosse possível... eu ia querer repetir a dose com você outro dia..."

                mc "E por que não?"

                na "Vamos ver... quem sabe, né? Agora deixa eu me lavar..."

                scene black with Dissolve(1.0)

                "..."

                na "Natasha?"
            "Deixa quieto.":


                pass

                "Acho que eu só vou ajeitar ela."

                mc normal "Upa."

        scene na3_motel11 with Dissolve(1.0)

        pause

        na "Hmm..."

        mc normal "Parece um anjo..."

        "Mas será que faz bem ela dormir assim? Hmm..."

        "Acho que no caso da [na], dormir na banheira é o menor dos problemas. Pra quem não descansa há três dias..."

        "Viver desse jeito... desistir de tudo pra realizar um serviço bem feito. Não deve ser fácil..."

        "Espero que ela realmente seja feliz assim..."

        mc normal "Não esquenta, [na]. Eu vou ficar de olho em você."

        scene black with Dissolve(1.0)

        na "Eu adoro... seu cabelo comprido..."

        mc desconfiado "Hm?"

        "..."

        "..."

        scene na3_motel11 with Dissolve(1.0)

        pause

        "Melhor eu acordar ela. Já vai dar 4 horas."

        mc normal "[na]."

        na "..."

        mc normal "[na]!"

        na "Hm?"

        mc "A hora."

        na "Eu dormi? Hmm... m-mas-"

        mc charmoso "Calma. Eu fiquei de olho em tudo. Deu tudo certo."

        jump natasha_e3_final


















































    label natasha_e3_final:

        scene black with Dissolve(1.0)

    na "Opa. Vai dar as quatro horas. Vamos?"

    mc charmoso "Vamo."

    na "Espero que aquele segurança não esteja nos esperando até agora."

    "..."

    scene distrito geral with Dissolve(2.0)

    na "A noite foi muito melhor do que eu imaginei, [mc]. Eu agradeço de verdade pela companhia."

    mc normal "Eu me diverti bastante também."

    mc charmoso "Eu sei que provavelmente não vai acontecer, mas espero que a gente acabe se reencontrando."

    na "Eu gostaria também. Logo logo o sol vai nascer, vê se descansa um pouco."

    mc charmoso "Até um dia, [na]."

    na "Até, [mc]."

    scene black with Dissolve(1.0)

    scene mc onibus_noite with Dissolve(1.0)

    "Que noite intensa."

    "E mesmo depois de todo esse tempo com a [na] ainda não sei qual é a dela."

    "Talvez a gente nunca se encontre de novo. Mas eu torço pra que ela fique bem e seja feliz."

    "Nunca imaginei que tivesse tanta coisa acontecendo aqui na cidade. Trabalhar como paparazzo realmente abriu um novo mundo pra mim."

    "Tô ansioso pro que pode acontecer em seguida."

    scene black with Dissolve(3.0)

    $ dia += 1
    $ tempo = 1

    $ v37_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v37_fim","final","local")

    scene black with Dissolve(3.0)



    jump call_cidade

label natasha_evento4:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("na4_save", extra_info="na4_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ natasha_e4 = "evento"

    "Uaaah..."

    "A [w] me mandou ir pra redação correndo hoje. Ela tinha alguma coisa muito importante pra me falar."

    scene black with dissolve

    "..."

    scene trabalho geral with Dissolve(1.0)

    pause

    "Espero que não seja pra me levar pra ela me mandar pro RH. Já tá bom demais o pai dela tentando me mandar pra rua."

    "Se a filha também..."

    if v47_fim:

        "A gente teve uma boa conversa na casa dela aquele dia. Nunca imaginei que a [w] ia me levar pra casa."

        if sofia_namoro:

            "A gente até assumiu um namoro... aquilo foi uma oficialização, certo?"

            "Nunca vi namorar uma pessoa que você nem sequer deu um beijinho..."

            "Tá parecendo webnamoro dessa Geração Y... millennials..."

    "Será que a [re] sabe de alguma coisa?"

    scene so4_recepecionista5 with Dissolve(1.0)

    pause

    menu:
        "Bom dia, [re].":


            mc normal "Oi, [re]. Bom dia."

            re "Oi."
        "Você tá linda como sempre.":


            mc charmoso "Sem querer cruzar a linha aqui, você tá linda. Você tá sempre bem. Parabéns."

            re "Você sabe que isso é assédio sexual no trabalho, certo?"

            mc desculpa "Foi mal. Acho que eu exagerei."

            re "Desculpa por quê? Eu adoro quando vocês me elogiam. E você nem foi grosseiro."

            mc charmoso "Bom saber que eu acertei."

            re "Haha... o que foi?"

    mc desconfiado "Você sabe se a [w] chamou alguém pra conversar hoje? Alguém comentou alguma coisa?"

    re "Ela chamou você?"

    mc "Chamou."

    re "Por que?"

    mc "Pior é que eu não sei. Queria saber se você sabia..."

    re "Hmm... ninguém falou nada. Deve ser alguma coisa só com você mesmo."

    mc preocupado "Pior é que tô meio preocupado."

    re "Eu ficaria. Parece sério. Ela não costuma chamar as pessoas assim. E quando ela fala com alguém é pra descer o sarrafo."

    mc "Eu sei..."

    re "Bom, eu mandarei flores pra sua família."

    mc zerado "Ei."

    re "Brincadeira. Para de ser covarde e vai logo ver o que ela quer."

    mc envergonhado "Acho que é uma boa mesmo. Valeu por nada."

    re "Por 'nada'? Eu vi você me secando. Isso não conta?"

    menu:
        "Depois eu pago uma cerva pra você.":


            mc charmoso "Tá certa. Depois eu pago uma cerva pra você no bar ali da praça."

            re "Cerveja? Nossa... tá bom, né? Se você acha que é isso que eu tô valendo. Melhor que nada."

            mc safado "Você é fogo, isso sim."

            re "Vai logo e para de dar em cima de mim assim."

            mc "..."
        "Não viaja.":


            mc zerado "Secando? Não viaja, [re]..."

            re "Eu viajando? Você quer dizer que é viagem me secar? Tá me chamando de feia?"

            mc concentrando "Eu não... nem sei o que eu vou responder pra isso."

            re "Você é muito sem graça, [mc]."

            mc envergonhado "Ok..."

    scene trabalho angulo with Dissolve(1.0)

    pause

    mc desconfiado "[w]? Tá aí na sua sala?"

    w "[mc]. Que bom que você chegou cedo."

    w "Só um segundo."

    scene so5_img11 with Dissolve(1.0)

    pause

    w "Obrigada por ter aparecido cedo assim."

    mc envergonhado "Você falou pra eu chegar antes porque tinha um negócio importante."

    w "Então. Eu tenho uma notícia séria pra dar pra você."

    mc preocupado "Que foi?"

    w "Você não vai ser mais paparazzo."

    mc angustiado "Quê?!"

    w "Eu conversei com meu pai e convenci ele."

    mc "Não é desse tipo de convencimento que eu tô precisando, [w]!"

    w "Eu falei pra ele que tá na hora da gente trazer algumas coisas na revista que não seja entretenimento."

    mc desconfiado "Hm?"

    w "Não falar só de fofoca e xeretisse dos famosos. Quem sabe ter uma pequena seção pra falar sobre outras coisas."

    mc "Tipo?"

    w "Tipo política."

    mc zerado "Política, [w]?"

    w "Você falou igualzinho ele."

    mc envergonhado "..."

    menu:
        "Não sei se política tem a ver.":


            mc envergonhado "Você realmente acha que tem a ver?"

            mc "Digo, o público que quer ler sobre o beijo da [sc] e os rolos da [cc] vai querer saber de política?"

            w "Não substime seu público, [mc]. Além de que como a gente vai saber se a gente não fizer um teste?"

            mc "Sei lá... nem sempre a gente precisa experimentar algo pra saber que vai dar merda. Merda, por exemplo."

            w "Não é à toa que você trabalha aqui."

            mc "Por quê?"

            w "Seu jeito de falar é igualzinho do meu pai. Não acredito..."

            mc desconfiado "Você acha? Eu e o velho?"

            w "Incrível, né?"

            mc "Sinceramente, não sei o que pensar disso."
        "Se você acha que dá certo...":


            mc "Olha, se você acha... eu apoio..."

            w "Eu sei que parece um pouco diferente do que a gente tá acostumado a abordar."

            w "No máximo que a gente fala é uns negócio de polícia quando tem escândalo. Política pura seria uma primeira vez."

            w "Mas eu realmente quero testar isso."

            mc charmoso "Se você tá determinada a fazer isso, então bora."

            w "Obrigada por confiar. Porque você vai ser importante."

            mc desconfiado "Eu?"

    w "É importante você comprar a ideia porque eu vou precisar de você mesmo pra isso funcionar."

    mc desconfiado "..."

    w "Meu pai falou que não ia pagar outro jornalista pra correr atrás disso, que seria o ideal, obviamente."

    w "Então, pra convencer ele, eu falei que ia mandar alguém daqui mesmo."

    mc desconfiado "Hmm... não sei se eu tô gostando do rumo dessa conversa."

    w "Vai ter mais trabalho pra fazer."

    mc "Hmm..."

    w "E claro que não vai ter aumento no salário. Meu pai não ia deixar, né?"

    mc zerado "HHMMM..."

    w "Então... daí eu dei seu nome pra ele, tá legal?"

    mc "Eu sabia."

    w "Vai ser um trabalho tranquilo. Eu prometo."

    mc "Qual é o trabalho?"

    scene so5_img10 with Dissolve(1.0)

    w "Vai ter uma coletiva de imprensa na prefeitura hoje. Eu quero que você participe."

    mc desconfiado "A gente vai fazer cobertura de coisa institucional assim?"

    w "Isso é pra agradar eles. A gente não tem a melhor das relações com a prefeitura."

    mc "O Donatello não vai com a nossa cara?"

    w "A gente nunca foi atrás deles, né? Eles têm uma relação muito melhor com a Faux."

    mc envergonhado "Claro que tem..."

    w "Então eu vou precisar que você vá até a prefeitura e passe a tarde toda no evento. Só pra eles verem que a gente tá lá."

    mc preocupado "O dia todo lá?"

    w "Por favor, [mc]. Eu preciso da sua ajuda! Você não vai ganhar dinheiro, mas vai ter minha gratidão!"

    "Cada uma que aparece... dinheiro que é bom, cadê?"

    menu:

        "Tudo pra minha namorada." if sofia_namoro:

            mc charmoso "Como eu posso negar um pedido da minha namorada assim?"

            w "V-você tá louco?! F-falar desse jeito aqui?!"

            mc "Que foi? Namorar não é crime."

            w "A gente tá no trabalho! Você precisa me tratar igual!"

            mc "Você que tá gritando."

            w "Culpa sua, idiota!"

            w "Ok... desculpa... eu devia ter te avisado. Mas chega disso agora, ok?"

            mc "Pode deixar."

            w "Promete?"

            mc "Sim. Prometido."

            w "Tá bom."
        "Ok. Pode contar comigo.":


            mc charmoso "Pode contar comigo."

            w "Muito obrigada, [mc]. De verdade!"

            mc zerado "Trabalhar de graça não tá certo, né? Mas tá bom..."

            w "Eu sei que não tá certo. Mais trabalho precisa ser remunerado de forma correta."

            mc "Pois é..."

            w "Mas eu prometo que é só dessa vez. Só pra provar pro meu pai que a gente pode pelo menos fazer um teste."

            mc envergonhado "Combinado. Vou levar isso como um favor pra você."
        "Melhor pedir pra outro. Não quero entrar nessa.":


            "Mais trabalho sem ganhar nada? Esse povo acha que eu sou idiota?"

            mc desculpa "Desculpa, [w], mas mais trabalho pra mim não dá."

            scene so5_img9 with Dissolve(1.0)

            w "[mc]... eu preciso de você nessa."

            mc desculpa "Não quero decepcionar você e nem parecer um idiota, mas não acho certo trabalhar mais sem receber mais."

            mc "Isso não é profissional."

            w "V-você tem razão. Desculpa pedir isso pra você. Vou falar com outro. E obrigada por ser sincero comigo."

            mc normal "De boa. E desculpa por não entrar nessa contigo."

            w "Tudo bem. Pode voltar aos seus negócios, tá?"

            mc "Valeu, até mais."

            "{b}Atenção. Essa escolha vai encerrar o encontro antecipadamente e pode te bloquear de outros eventos no futuro{/b}"

            "{b}Não é recomendado escolher esta opção se é sua primeira vez jogando{/b}"

            "Bora sair daqui. Tenho outras coisas pra fazer."

            scene black with dissolve

            "..."

            jump natasha_e4_final

    w "Ufa. Sem você não sei como ia ser isso."

    w "Você é a pessoa que eu mais confio aqui, [mc]. O Ronaldo é um bom repórter, mas não é a mesma coisa."

    w "A gente já passou por mais coisas juntos."

    mc "É verdade. Eu fico feliz de você confiar em mim."

    mc envergonhado "Só não sabia que ia vir mais trabalho com isso..."

    w "Tá bom. Já pode parar de reclamar."

    w "Seu trabalho é lá na prefeitura. Você sabe como chegar lá, né?"

    mc "Pode deixar. Vou de busão, mas vou."

    w "Se você vai de ônibus é melhor você sair daqui agora. Demora um pouco pra chegar lá."

    mc normal "Eu já vou pra lá então."

    w "Boa sorte."

    mc "Valeu."

    w "E, [mc]..."

    mc desconfiado "Hm?"

    w "A intenção é melhorar nossa imagem com a prefeitura. Pelo amor de tudo que é mais sagrado, não estrague mais ainda."

    mc envergonhado "Ei. Pode confiar em mim."

    if sofia_namoro:

        mc charmoso "Fica bem, amor."

        w "[mc]!"

    mc normal "Tchau!"

    scene black with dissolve

    "..."

    call locomocao from _call_locomocao_10

    scene cidade centro9 with Dissolve(1.0)

    pause

    "Prefeitura... então a [w] quer melhorar nossa imagem com eles."

    "Será que ela tem noção que eles tão tramando contra a revista?"

    "O Donatello, a Faux, e até a [j]. Todos juntos pra assumir a revista e controlar todos os meios de comunicação da capital."

    "Se eles controlarem a informação, eles vão poder fazer tudo o que eles quiserem e ninguém vai saber."

    "Eu preciso decidir de que lado eu vou ficar nessa história."

    "O Lucca da Faux falou pra eu ajudar na missão deles. Se eu colaborar, eles vão ter um lugar bom pra mim na nova revista."

    "O Barão, o [gus], o Tony, a Blergh! e todos essa galera deve tá junta pra assumir o controle da ilha e da cidade."

    "Agora... eu vou ficar com eles ou contra eles?"

    "Eu preciso pensar muito bem qual vai ser a melhor decisão pra mim."

    "Agora deixa eu entrar. Quero ser o primeiro na coletiva. Ganhar aqueles pontos que a [w] pediu."

    scene black with dissolve

    scene na4_img1 with Dissolve(2.0)

    pause

    "Primeiro tem que passar lá com o guarda."

    scene prefeitura guarda with Dissolve(1.0)

    pause

    mc normal "Olá."

    "Policial" "Bem vindo. Qual é o motivo da visita por favor?"

    menu:
        "Eu vim pra coletiva.":


            mc "Eu vim pra coletiva de imprensa que vai ter. Eu trabalho na revista da ilha."

            "Policial" "Posso ver sua identificação?"

            mc desconfiado "Identificação?"

            mc normal "Ah. Claro. Toma."

            "Policial" "..."

            "Policial" "Está tudo ok. Pode passar."

            mc "Valeu."
        "Eu vim participar de um golpe de Estado.":


            mc tarado "Eu vim fazer parte de um golpe de Estado pra depor o prefeito."

            "Policial" "Por favor. Eu peço que você se remova agora mesmo."

            mc angustiado "E-era brincadeira. Eu vim pela coletiva de imprensa. Eu trabalho na revista da ilha."

            "Policial" "Por favor, deixe-me ver uma identificação."

            mc preocupado "Tá aqui."

            "Policial" "..."

            "Policial" "Ok. Pode passar. Por favor, evite atitudes como essa aqui dentro."

            mc concentrando "Desculpa."

    "Policial" "Acho que eu nunca vi ninguém da revista de vocês aqui."

    mc envergonhado "Verdade. A gente não costuma cobrir política."

    mc normal "Mas queremos mudar isso agora. Dar mais atenção a esses assuntos."

    "Policial" "Hm... ok. Pode passar."

    mc desconfiado "Ok... obrigado."

    scene black with dissolve

    scene na4_img2 with Dissolve(1.0)

    pause

    "Acho que vai começar logo logo."

    "Tô achando bem vazio até. Tem um cara com uma câmera ali."

    mc zerado "E tem uma repórter da Faux ali... e outro ali..."

    "Um é do jornal, outro da TV e acho que tem outra da Faux ali que é da rádio."

    "Nossa... e da nossa revista tem... eu. É duro competir com esses caras em cobertura."

    "Acho que essa é a primeira cobertura jornalística que eu faço tirando a faculdade."

    "Normalmente eles mandam alguém organizar os jornalistas, colocar tudo no lugar, pra autoridade poder falar."

    "Imagino que vai ser alguém da assessoria de imprensa do governo. Pra isso existe a secretaria de comunicação."

    "Quem será que é? Acho que eu não conheço ninguém que trabalha aqui."

    "???" "Muito bem. Peço a atenção de todos."

    "Opa. Tem alguém vindo."

    scene na4_img3 with Dissolve(1.0)

    pause

    "???" "A coletiva já vai começar. Normalmente nós oferecemos releases, mas desta vez será apenas um anúncio rápido."

    "Jornalista" "Cadê a Vera?"

    "???" "Hoje eu vou assumir o evento. Até por ser uma coisa menor. Foi um pedido do prefeito."

    "Jornalista" "Hm..."

    mc desconfiado "Ainda não consegui ver quem é."

    "???" "Vocês podem se organizar aqui. Logo logo o prefeito virá se pronunciar."

    "Jornalista" "Você não pode nem falar sobre o que vai ser?"

    "???" "Não. O prefeito quer ele próprio anunciar o assunto."

    "Jornalista" "Vocês tão sendo bem misteriosos sobre isso. Normalmente a Vera já passa tudo pra gente."

    "???" "Entendo, mas prometo que logo vocês vão saber de tudo."

    "???" "Com licença, agora eu vou falar com os outros."

    "Jornalista" "Hm..."

    scene na4_img2 with Dissolve(1.0)

    "Foi bom eu ter conseguido a conversa deles. Agora eu tô por dentro."

    "Então essa mulher trabalha direto pro prefeito? Ela parece importante. Pelo menos acima da assessoria de imprensa."

    "Seria uma boa conhe-"

    mc surpreso "!!!"

    scene na4_img4 with Dissolve(1.0)

    pause

    "???" "Olá?"

    mc "N-natasha!"

    na "[mc]... é você."

    mc "É você!"

    na "Qual a surpresa?"

    mc "Eu pensei qu-"

    na "Eu não disse que era funcionária pública? Eu lembro que eu te falei alguma coisa assim."

    mc "Então esse tipo de funcionária..."

    na "O que você pensou que fosse?"

    menu:
        "Uma agente secreta internacional.":


            $ natasha_seducao += 2

            mc "Falando a verdade, eu achei que você fosse uma agente secreta internacional trabalhando pro governo mundial."

            na "Haha... de onde você tira isso, [mc]?"

            mc "Sei lá. Achei estranho você ficar investigando o Barão e tal."

            if v37_fim:

                mc "E também lá no Distrito. Tudo aquilo foi bem estranho, fala aí."

            na "Acho que você tá tentando ler demais nas entrelinhas. Eu só gosto de um pouco de aventura nas horas vagas."

            mc "Então é isso... diversão..."

            na "Você não parece convencido."

            mc "Se você diz..."
        "Algo menos burocrático.":


            mc "Sei lá... alguma coisa menos burocrática."

            na "Só por que eu passava a noite no Cassino a trabalho?"

            mc "Eu nunca entendi esse seu trabalho direito. Quem sai no meio da noite por causa de trabalho?"

            na "Como assim quem sai? Isso não é normal?"

            mc "Ah, para, [na]. Agora você só tá tirando com a minha cara."

    na "Acho que eu não tenho chances contra esse seu senso jornalístico."

    mc "Você só precisa contar uma mentira mais consistente."

    na "Se você não acredita, logo logo eu provo pra você. Inclusive, não vai dar pra conversar com você agora. O prefeito deve estar pronto."

    na "Olha o que eu tenho que cuidar aqui, [mc]. Até um outro dia."

    menu:
        "V-vamos conversar depois?":


            mc "E s-se a gente se falasse depois do evento? Trocar uma ideia depois do trabalho."

            na "Desculpa, [mc]. Mas eu tenho outras coisas pra fazer. Fica pra uma próxima."

            mc "Tudo bem. É uma pena, mas tá legal."
        "Ok. A gente se fala.":


            $ natasha_seducao += 2

            mc "Tá legal. A gente se vê um dia aí."

    na "Até."

    scene na4_img2 with Dissolve(1.0)

    pause

    "A [na] é sempre assim. Quando eu acho que eu tô avançando com ela, ela dá uma cortada clássica e requintada."

    "Será que um dia eu ainda vou ter uma chance com essa mulher?"

    "É impossível qualquer homem resistir a essa garota. Ela é linda, misteriosa e tem um ar de perfeição, que é duro explicar."

    "Ela parece aquelas mulheres intocáveis que a gente só pode ver..."

    if na1_beijo:

        "Se bem que naquela noite no Cassino eu dei uma boa tocada na boca dela."

    "Eu queria me aproximar mais dela."

    "E que história é essa de secretária do prefeito? Eu nunca ia imaginar isso. Que doideira."

    na "Atenção, todos. Por favor, vamos iniciar o evento."

    mc normal "Opa. Aí vem o figura."

    scene na4_img5 with Dissolve(1.0)

    pause

    na "Amigos da imprensa, agora teremos um pronunciamento do nosso prefeito Basilio Donatello."

    prc "Muito obrigado por terem aparecido, amigos dos mais variados meios de comunicação."

    prc "Recebi a incrível notícia que até mesmo a revista da ilha, que normalmente apenas no ignora, enviou um correspondente."

    mc surpreso "A-ah!"

    prc "Obrigado por ter vindo, jovem. Sua presença é muito importante."

    menu:
        "Obrigado, senhor prefeito.":


            mc charmoso "Obrigado, senhor prefeito. Nossa revista está muito interessada no que o senhor tem a dizer."

            prc "Seu comentário soa irônico, jovem, sendo que vocês nunca acompanham nada do que eu digo."

            "Jornalistas" "Hahaha..."

            prc "Mas hoje é um grande dia. Por isso vamos deixar essa passar."
        "...":


            $ natasha_seducao += 2

            mc envergonhado "..."

    prc "Bem, o que eu tenho a dizer a vocês muitos de vocês já especularam. É algo que está na boca do povo há um tempo."

    prc "E finalmente estamos prontos para revelar oficialmente a finalização da maior obra já feita em nossa cidade."

    prc "Iniciada pelo meu pai, Stefano Donatello, e finalmente finalizada sob minha administração, vamos todos conhecê-la."

    prc "Trata-se, nada mais, nada menos, que o Aeroporto Internacional Stefano Donatello."

    "Jornalistas" "Finalmente..."

    "Aeroporto? Aeroporto... eu já ouvi bastante gente falando disso."

    prc "O maior aeroporto do país, talvez do mundo, estará localizado em nossa prestigiosa ilha e servirá como um sinal de avanço."

    prc "Nosso aeroporto atual está há anos atendendo a demanda, mas nossa intenção é ampliar nosso alcance."

    prc "Vamos oferecer mais serviços e mais opções de translados e escalas do que qualquer outra cidade de nosso continente."

    prc "Esperamos que o grande fluxo de passageiros movimentem ainda mais as atrações de nossa ilha paradisíaca."

    prc "Isso trará grande arrecadação para todos os nossos comerciantes e prestadores de serviço, assim como aumentar nossa arrecadação pública."

    prc "Hoje eu vim apenas para anunciar oficialmente e marcar com vocês e toda nossa população o dia do grande lançamento."

    prc "Todas as informações serão repassadas a vocês no dia da inauguração. Espero que vocês estejam tão empolgados quanto eu."

    prc "Agora eu responderei algumas perguntas de vocês. Só vamos tomar cuidado para não darmos spoilers demais."

    prc "Tenho que deixar o principal para a inauguração. Vocês me entendem, não é mesmo?"

    prc "Muito bem, [na], eu vou deixar você organizando. Por favor."

    na "Sim, senhor."

    "Jornalista da Faux" "Aqui, querida, por favor!"

    na "Eu gostaria de começar com o rapaz da revista que nunca vem. Vamos dar as honras a ele."

    mc surpreso "E-eu?!"

    na "Por favor. Você tem alguma pergunta?"

    scene na4_img6 with Dissolve(1.0)

    pause

    prc "Vá em frente, jovem."

    "Pergunta? O que eu pergunto? Eu nem sei direito o que isso tudo significa. É só um aeroporto. Eu nem tenho dinheiro pra pegar avião."

    "A única vez que eu viajei foi com a [c] e ela que pagou tudo, claro."

    "Se eu não perguntar nada vai ficar feio. Se eu fizer a pergunta errada eu posso cagar na nossa relação com a prefeitura. A [w] me mata."

    "O que eu pergunto?!"

    menu:
        "Por que não melhorar o aeroporto que já tem?":


            mc desconfiado "Eu queria saber por que seu pai resolver criar um novo aeroporto ao invés de melhorar o que já tem."

            mc "Não seria mais barato ampliar e aperfeiçoar o já existente, ao invés de criar um concorrente, vamos dizer assim, do zero?"

            "Jornalistas" "..."

            prc "Veja, jovem, essa não é a primeira pergunta que viria na minha cabeça nessa situação."

            "Repórter Desconhecida" "Mas é uma excelente pergunta! O senhor não pretende responder?"

            prc "Nós responderemos todas as perguntas. Não temos nada a esconder. Mas peço a educação de esperarem sua vez."

            prc "Muito bem. Por que criar um novo aeroporto? O ex-prefeito não tirou essa ideia do chapéu."

            prc "Essas escolhas são feitas com base em estudos técnicos fundamentados pelas nossas secretarias."

            prc "Nossos profissionais fazem levantamentos sérios e analisando custos e potenciais recursos gerados, chegamos a essa conclusão."

            prc "Isso foi feito na administração anterior, então estamos apenas seguindo o processo. Respondido?"

            mc normal "Obrigado."

            "Repórter Desconhecida" "Com licença. Isso pareceu meio vago. Nós temos acesso a esses estudos?"

            prc "[na]."
        "Quais as vantagens do novo aeropoto?":


            mc normal "Eu gostaria de saber quais as vantagens desse novo aeroporto em comparação com o que já existe."

            prc "Essa, com certeza, é uma excelente pergunta."

            prc "O novo aeroporto tem uma localização muito mais adequada para estimular os negócios mais importantes da nossa capital."

            prc "Nossa ilha está cheia de atrações, como o Cassino, hotels e outros locais onde os passageiros poderão fazer escalas."

            prc "A localização do novo aeroporto vai proporcionar muito mais dividendos para nossos moradores."

            "Repórter Desconhecida" "Mas, em número de atrações, a parte continental da cidade não tem mais opções?"

            "Repórter Desconhecida" "Você vai estar levando os passageiros para longe do centro real da cidade."

            "Jornalistas" "..."

            prc "Eu lembro de você. Sempre com perguntas assim."

            "Repórter Desconhecida" "O senhor pode responder?"

            prc "Espere sua vez de perguntar, por favor. Seja educada como o jovem da revista."

            "Repórter Desconhecida" "..."
        "Melhor não perguntar nada.":


            $ natasha_seducao += 2

            mc preocupado "Eu n-não tenho nenhuma pergunta!"

            na "Tem certeza?"

            "Repórter da Faux" "Por que mandaram esse cara? A revista tem a [j]..."

            mc zerado "Ei... eu ouvi isso."

    na "Tudo bem. Vamos para o próximo."

    "Repórter Desconhecida" "Posso perguntar? Com licença."

    prc "Tudo bem. Acho melhor pararmos por aqui, já que temos uma pessoa que não sabe como funciona uma coletiva."

    "Repórter Desconhecida" "Quê?! É só uma pergunta! Ele pôde perguntar!"

    na "O prefeito foi bem claro. A coletiva está encerrada."

    prc "Só quero deixar claro que vamos voltar a conversar em breve. O dia da inauguração será enviado em press release."

    prc "Nos veremos lá e será um grande dia para nossa cidade. Estamos sempre pensando no futuro e no bem de nossa cidade."

    prc "Até uma próxima oportunidade."

    "Acabou..."

    scene na4_img2 with Dissolve(1.0)

    pause

    "Então era isso. Assim que funciona uma coletiva de verdade."

    "Até que foi interessante."

    "E eu tive a chance de ver a [na]. Foi por pouco tempo, mas assim ela não esquece de mim pelo menos."

    "Bom. É hora de voltar."

    scene black with dissolve

    pause

    "???" "Ei."

    scene na4_img4 with Dissolve(1.0)

    pause

    mc surpreso "Natasha!"

    na "Oi. Desculpa te assustar."

    mc envergonhado "Acho que eu exagerei um pouco. Tava pensando aqui."

    na "Será que você tem um tempo agora?"

    mc desconfiado "Agora?"

    menu:
        "Eu sempre tenho tempo pra você.":


            $ natasha_seducao += 2

            mc charmoso "Eu sempre tenho tempo pra você."

            na "E você continua não perdendo uma chance de dar em cima."

            mc "Só de garotas lindas e misteriosas iguais você."

            na "Misteriosa? Eu ganhei esse adjetivo agora?"

            mc "Agora? Você é misteriosa desde aquele primeiro drink no bar do cassino, gata."

            na "Tudo bem. Entendi que você quer passar um tempo comigo. Mas, infelizmente, não sou eu."
        "Tempo pra quê?":


            mc desconfiado "O que você precisa?"

    na "Quem te chamou foi o prefeito Donatello. Ele quer falar alguma coisa com você."

    mc surpreso "S-sério?!"

    na "Ele só me pediu pra buscar você. Ele não tem muito tempo, então seria bom a gente se apressar, se você puder."

    mc desconfiado "O que ele quer comigo?"

    na "Não sei. Ele não falou nada. Se você pudesse, você me ajudaria."

    menu:
        "Ok. Eu vou falar com ele.":


            mc normal "Opa. Pode deixar. Tô me sentindo importante agora."

            na "E é mesmo. Faz tempo que eu não vejo ele querendo falar com alguém que ele não conhece assim."
        "Vou fazer isso por você.":


            $ natasha_seducao += 2

            mc charmoso "Tudo bem. Se isso vai ajudar você. Eu faço, sim."

            na "Obrigada, [mc]. Ele não tolera muito que falhem com ele. Se você não fosse, ia ser uma marquinha vermelha na minha ficha."

            mc "Não se preocupe. Eu vou lá."
        "Você acha perigoso?":


            mc preocupado "V-você acha que pode ser perigoso? Eu não sei se esses caras gostam de mim."

            na "Não precisa se preocupar. Nós estamos na prefeitura. No máximo, ele pode te ameaçar verbalmente."

            mc angustiado "Não sei se eu quero isso!"

            na "Mas não tem porque ele fazer isso. O senhor Donatello não é uma má pessoa. Além de que você é só um repórter, [mc]."

            mc envergonhado "Você tem razão. Eu tô com medo demais..."

    na "Podemos subir então?"

    mc charmoso "Claro. Vamos."

    scene black with dissolve

    scene na4_img7 with Dissolve(2.0)

    pause

    mc normal "Até que é bem grande aqui."

    na "Sim. A prefeitura da nossa cidade é um pouco diferente. Tem muita coisa aqui."

    na "Não é só o poder Executivo que fica nesse prédio. Digo, não é só o prefeito e as secretarias."

    na "O Judiciário também fica aqui."

    mc "Verdade... quem será que olha quem?"

    na "Quem? Ah... verdade... talvez você tenha uma ideia."

    mc desconfiado "Hm?"

    na "Ok. É aqui."

    na "Não precisa ficar nervoso com isso. Ele é uma pessoa acessível com gente que ele não conhece."

    na "Deve ser mania de político, mas ele fala bastante, dá bastante risada. Não precisa se preocupar."

    na "Só seja você e responda o que ele perguntar."

    menu:
        "Eu dou conta de uma conversa.":


            $ natasha_seducao += 2

            mc "Você que não precisa se preocupar. Eu sou formado em comunicação. Eu sei como conversar, tá legal?"

            na "Tem razão. Desculpa por tratar você igual um zé ninguém."

            mc "Bom, você fica fofa preocupada."

            na "Deixe as cantadas pra quando a gente tiver sozinhos."

            mc "Então a gente vai ficar sozinhos mesmo..."

            na "Deus..."
        "Valeu pela preocupação e pelas dicas.":


            mc "Obrigado por se preocupar e tentar me ajudar."

            na "Às vezes eu posso ser um pouco exagerada. Mas é melhor prevenir do que remediar, não é verdade?"

            mc "Se preocupar demais vai te dar rugas na testa. Eu já não falei isso pra você?"

            na "Eu acho que já. Você é tão corajoso às vezes."

            mc "Haha..."

    na "Deixa eu avisar ele. Com licença."

    "..."

    "Falar com o prefeito. O que será que o tal [prc] quer com um jornalista novato que nem eu?"

    "Eu sei que eu cavoquei muita coisa deles nos últimos meses. Mas é impossível que eles realmente estejam com medo de mim."

    "A não ser qu-{nw}"

    na "Pronto. Pode entrar."

    mc normal "Ok."

    scene black with dissolve

    scene na4_img8 with Dissolve(1.0)

    pause

    prc "Bem vindo, jornalista. Entre, por favor."

    mc normal "Obrigado, senhor prefeito [prc]."

    pr "Não precisa me chamar assim, [pr] é o bastante."

    mc envergonhado "Tá certo..."

    pr "Serei sincero com você. Normalmente eu sou mais educado, porém hoje o dia está bem corrido."

    pr "Eu lhe chamei para perguntar o motivo da sua vinda à coletiva."

    pr "Digo, é a primeira vez na minha administração que sua revista manda alguém para um evento."

    "Por que ele quer saber isso? Será que eu falo a verdade pra ele? A [w] pediu pra eu melhorar nossa relação..."

    "E talvez ser sincero vai ajudar a [na] e fazer eu ganhar pontos com ela... Ou o contrário? Eu tenho que pensar bem nisso."

    mc envergonhado "Então..."

    menu:
        "Queremos melhorar nossa relação com vocês.":


            mc charmoso "Sim, eu sei que a relação da revista com a prefeitura não tem sido das melhores, mas é isso que queremos mudar."

            mc "Minha vinda é justamente pra melhorar nossa relação. Queremos estar mais presentes nos assuntos da sua administração."

            mc "Espero que essa vinda seja o começo de uma boa relação entre a revista e o senhor."

            pr "Isso é realmente promissor, amigo."

            pr "Isso foi algo que meu pai não conseguiu, nem nos tempos dele. Ter uma amizade com a sua revista seria algo novo."

            pr "Espero que não acabe nesse primeiro passo."

            mc "Se depender da gente, acredito que não, senhor."

            pr "Perfeito."
        "Não sei. Só cumpro ordens.":


            $ natasha_seducao += 2

            mc desculpa "Desculpa, mas eu não sei responder isso."

            mc "Minha editora me mandou cobrir o evento, mas ela não falou porque."

            mc normal "Eu sou só um pauteiro, na verdade. Eu tento encontrar coisas sobre famosos na ilha."

            mc envergonhado "Até me contarem alguma coisa, todo mundo já ficou sabendo haha..."

            pr "Entendi. Vou pedir pra Vera entrar em contato com a sua redação e falar com sua editora."

            pr "Como é o nome dela? Achei que o velho chefe ainda mandasse lá."

            mc "Ele ainda é o editor, mas agora nós temos uma gerente de produção. Ela que manda a gente pra cá e pra lá."

            pr "Ah, ok. E o nome dela?"

            "Droga... falar o nome da [w] assim? Será uma boa? {w}Merda, eu tenho que falar. Não dá pra falar que eu não sei."

            mc desculpa "É [w]."

            pr "Ok. Falaremos com ela."

    scene na4_img9 with Dissolve(1.0)

    pause

    pr "Sabe uma coisa... espera. Desculpa, como é seu nome? Que falta de atenção a minha. Mil perdões."

    mc normal "Não esquenta com isso. Meu nome é [mcc]."

    pr "Posso te chamar de [mc]?"

    mc "Claro."

    pr "E esta é a [na]. Uma assistente e tanto. Não tem nada que eu peça pra essa mulher que ela não consiga realizar."

    pr "Não importa a hora do dia, não importa o lugar que seja. Ela faz de tudo, e faz de tudo com um capricho..."

    mc normal "A [na] com certeza parece uma mulher bem capaz, mesmo."

    pr "Vocês se conhecem?"

    na "Sim, senhor. Eu encontrei o senhor [mc] no Cassino da ilha."

    pr "Interessante."

    pr "Bom, voltando ao que eu ia mencionar antes, para que possamos encerrar este encontro..."

    pr "Meu governo tem laços em várias áreas da cidade. Nós somos muito bem vistos pela grande maioria da população."

    pr "Nossa taxa de aprovação está estável, em um ponto excelente, com quase 70%% de bom ou ótimo."

    mc normal "Isso parece bom mesmo."

    pr "E o restante fica praticamente no regular. O que sobra muito pouco para ruim ou péssimo, que é um feito e tanto."

    pr "Nós só conseguimos isso graças a boa comunicação que temos com os cidadãos."

    pr "Por muito tempo, desde tempos anteriores ao meu pai, a Faux News tem sido uma grande parceira."

    pr "Não que eles sejam amigos nossos, mas eles são amigos da verdade. E a verdade está do lado do meu governo."

    pr "Isso porque fazemos o bem para nossa população."

    mc desconfiado "..."

    pr "Agora... bom, talvez seja melhor sentarmos. Tudo bem para você?"

    mc normal "Claro."

    pr "Eu sinto que eu me empolgo um pouco e fico palestrando sozinho. Venham, vocês dois, sentem aqui comigo."

    scene black with dissolve

    scene na4_img10 with Dissolve(1.0)

    pause

    pr "Muito bem. Antes de eu voltar a falar e falar, que é algo que eu gosto muito pelo visto."

    pr "Você acha que eu falo muito, [na]?"

    na "Deve estar na sua veia de político. Mas é um dos seus charmes."

    pr "Essa garota me mima demais, [mc]. Você tá vendo."

    na "Só estou sendo sincera com você, bobo."

    "A [na] falando assim? Que diferente..."

    pr "Eu não costumo fazer isso. Mas você tem ouvido tão atentamente, que vou deixar você falar também."

    mc envergonhado "Eu não sei sobre o quê eu poderia falar, senhor."

    pr "Faça uma pergunta então. Vocês são jornalistas são bom com perguntas."

    scene na4_img10 with vpunch

    mc surpreso "A-ai!"

    pr "Algum problema, [mc]?"

    "A [na] me chutou! Por quê?"

    "Será que ela quer que eu pergunte? Ou não pergunte? Como eu vou entender uma bicuda na canela?"

    menu:
        "Eu não tenho nenhuma pergunta.":


            $ natasha_seducao += 2

            mc envergonhado "Eu prefiro só ouvir mesmo, sabe? Eu não tenho pergunta pra fazer."

            pr "Verdade? Interessante, isso é raro vindo de um jornalista, não é?"

            mc "Verdade... normalmente a gente é cheio de perguntas."

            pr "Você não tá querendo ficar quietinho pra fazer uma boa impressão, certo?"

            mc "Não é isso... eu só tô interessado no que você tava falando mesmo."

            pr "Se você diz, melhor pra mim. Eu posso falar mais haha!"

            na "Haha... você encontrou um bom amigo."

            pr "Não é? É disso que eu preciso. Pessoas que queiram ficar do meu lado."
        "Como sua família se mantém no poder?":


            mc desconfiado "Já que eu posso perguntar, eu queria saber sua opinião sobre como a família Donatello se mantém no poder."

            mc "Vocês estão no comando da cidade há mais de uma década, pelo que eu vi. Como você vê isso?"

            pr "Hmm... essa é uma pergunta interessante. E inclusive é algo que já me perguntaram diversas vezes."

            pr "A resposta rápida é que nossa administração é como um restaurante que usa bons ingredientes."

            mc "Hm? Restaurante? Ingredientes?"

            pr "Sim. Pense, se você pede comida em um restaurante e percebe que os ingredientes são de segunda, você provavelmente não vai voltar lá."

            pr "O lucro do restaurante pode ser maior, pois ele pagou menos por aqueles ingredientes em comparação com quem comprou os melhores."

            pr "Mas, mesmo ganhando menos no curto prazo, o restaurante bom garante que o cliente sempre volte, ganhando mais no longo prazo."

            pr "Eu acredito que foi isso que os Donatello fizeram desde o primeiro a assumir o comando, meu avô."

            pr "Mesmo não sendo a administração mais pomposa, as pessoas perceberam que o governo usava ingredientes de primeira."

            pr "Ele foi reeleito, e quando meu pai assumiu, nas eleições posteriores, ele só seguiu a mesma receita."

            pr "Meu pai foi diferente de meu avô em vários aspectos. Ele gastou muito mais, mas ele usou o que meu avô tinha guardado."

            pr "Eu tento seguir o que aprendi com eles. E espero que meu sucessor faça o mesmo."

            na "Incrível analogia."

            mc normal "Obrigado pela resposta."

            pr "Vocês são uma excelente platéia."

    scene na4_img11 with Dissolve(1.0)

    pause

    pr "Inclusive, falando em bons ouvintes, aquela repórter hoje mais cedo... que falta de compostura."

    na "Tem razão. Ela falou quando devia ter ficado quieta."

    pr "Vou mandar a Vera entrar em contato com o veículo dela e dizer que não aceitaremos mais elas nos nossos eventos."

    pr "Não precisamos de jornalistas fazendo perguntas que não são bem vindas. Quero dizer, na hora que não devem."

    na "Concordo. Ela precisa aprender o lugar dela."

    pr "Muito bem, [mc]."

    pr "Se me permite, então, gostaria de ver você mais vezes em nossos eventos. Ter você mais próximo de nós."

    pr "Aliás, isso era algo que eu não queria revelar assim a você, mas parece que olhar pra você me faz querer falar."

    mc desconfiado "Hm?"

    pr "Eu conhecia seu nome, antes de você se apresentar."

    mc "Sério?"

    pr "Sim. Mas, por favor, não me tome por um stalker. Seu nome apareceu em várias pautas da revista."

    mc envergonhado "Ah... então você lê a revista?"

    pr "Infelizmente, não tenho tempo. Mas minha equipe de comunicação separa as principais notícias do dia e me envie um resumo."

    pr "Um dia, a Vera me trouxe seu nome em uma conversa. 'Esse garoto... ele tá aparecendo bastante', ela disse."

    pr "Ela notou que várias das suas matérias tinham informações bem pessoais sobre as celebridades. Coisa rara."

    mc "Você acha?"

    pr "Normalmente os paparazzi trazem informações que podem ser vistas, mas você conseguiu coisas que só podem ser ouvidas."

    pr "Você deve ser realmente um bom ouvinte. E eu lembrei isso bem agora. Eu senti uma vontade de me abrir com você."

    pr "Se eu não tivesse passado por uma série de treinamentos de media, eu poderia ter escorregado aqui. É sério."

    pr "O que você acha disso?"

    menu:
        "Eu nunca tinha pensado nisso.":


            $ natasha_seducao += 2

            mc envergonhado "Sinceramente, senhor, eu nunca tinha pensado nisso. Mas é verdade. As pessoas acabam contando as coisas pra mim."

            pr "Parece ser um talento nato. Algo que vem de dentro. Você precisa cuidar muito bem dessa habilidade."

            mc "Pode deixar. Vou fazer o dá."
        "É uma técnica que desenvolvi.":


            mc tarado "É uma técnica que eu desenvolvi nos meus anos como jornalista."

            pr "Técnica... então é algo consciente, que você sabe a hora certa de usar."

            mc surpreso "Ai!"

            "A [na] me chutou de novo!"

            mc tarado "S-sim... eu sei como usar e tirar informações das pessoas."

            pr "Realmente surprendeente."
        "As pessoas dizem que eu sou estranho.":


            mc zerado "Normalmente, quando eu converso com os outros, as pessoas me chamam de cara estranho. Vê se pode..."

            na "Haha..."

            pr "Não é motivo para dar risada, [na]."

            na "Desculpe."

    pr "A maioria das pessoas não sabe dar valor ao que importa. Essa é uma capacidade que eu teria muito interesse."

    na "[pr]."

    pr "Sim?"

    scene na4_img12 with Dissolve(1.0)

    pause

    na "Eu entendo que este jornalista tenha um jeito cativante. Mas ele acabou de se formar. Não acho que seja tudo isso."

    mc zerado "Ei..."

    pr "Não se preocupe, [mc]. A [na] é assim. Ela fala sem rodeios."

    na "Minha intenção não é fazer pouco do seu trabalho, mas nós precisamos ter muito cuidado com quem contamos como aliados."

    pr "É importante ter precaução. Isso eu concordo. Mas também é preciso arriscar na hora certa."

    pr "Como eu disse anteriormente, a fama deste jovem precede ele, como a Vera mesmo notou. E não é só isso."

    pr "Existem coisas que mesmo você não sabe, [na]. O [mc] está mais envolvido em nossos assuntos do que você imagina."

    mc desculpa "..."

    na "Desculpa se eu me intrometi."

    pr "Não tem o que se desculpar. E você tem razão, e por isso mesmo quis trazer ele aqui hoje."

    pr "O momento da verdade está se aproximando, [mc]. Você se enfiou em várias histórias, e todas elas se cruzam em algum ponto."

    pr "Por mais distantes e desconexas que pareçam, certas pessoas estão com o destino entralaçado, esperando o ponto de intersecção."

    mc envergonhado "Não sei seu eu tô entendendo..."

    pr "Todas as vidas são como caminhos, cujo condutor é o tempo, e andam em uma única direção, até o fim da jornada."

    pr "Durante esse caminho, existe um ponto que eu chamo de Encruzilhada. É o ponto mais importante nesse trajeto, onde você pode mudar a direção."

    pr "E sua Encruzilhada está muito perto, [mc]. Eu espero que quando ela chegar, você escolha a direção correta."

    pr "Entendeu agora? O que você me diz?"

    menu:
        "Vou escolher o caminho certo.":


            $ natasha_seducao += 2

            mc charmoso "Não se preocupe, senhor. Eu vou escolher o 'caminho certo'."

            pr "Perfeito. Era o que eu queria ouvir de você hoje."

            pr "O caminho certo sempre trará mais frutos que a outra opção. Não deve se esquecer disso."

            mc "Não vou."
        "Na hora eu vejo o que eu faço.":


            mc envergonhado "Acho melhor deixar as coisas rolarem e na hora eu vejo o que eu faço."

            pr "Isso é um pouco displicente de sua parte, não acha? Não seria melhor se comprometer agora?"

            mc "Eu realmente preciso ver o que tem pra mim nos dois lados."

            pr "Talvez eu tenha subestimado sua sagacidade. Enfim..."

    pr "Agora sim. Estou pronto para continuar minha rotina."

    pr "[na], eu vou pedir que você acompanhe o [mc] até a saída e tranque tudo por favor."

    scene na4_img13 with Dissolve(1.0)

    pause

    na "Pode deixar, [pr]. Eu vou organizar sua agenda pra quando você chegar amanhã. E vou cuidar do visitante também."

    pr "[mc]. Desculpe-me por deixar você assim. Agradeço por aceitar meu convite."

    mc normal "Está tudo bem, senhor. Foi uma boa conversa."

    pr "Concordo. Eu acredito que vamos nos ver novamente antes do que você imagina. Mantenha a cabeça no lugar até lá."

    pr "Adeus."

    na "Até amanhã."

    mc "Até."

    "{i}katchak{/i}"

    mc normal "Ele foi..."

    na "Calma... vamos dar uns segundos... às vezes ele esquece alguma coisa."

    "..."

    mc desconfiado "[na]?"

    scene na4_img14 with vpunch

    pause

    mc "N-natasha!"

    na "..."

    mc "Tá tudo legal?"

    na "Meu Deus... isso foi pesado demais..."

    mc "Você tá bem?"

    na "Eu só preciso de um minuto."

    menu:
        "...":


            $ natasha_seducao += 2

            mc "..."
        "Posso fazer alguma coisa?":


            mc "Que que foi? Posso te ajudar?"

            na "Não... só um instante."

            mc "Ok..."
        "O que você tá sentindo?":


            mc "Você tá sentindo o quê? Tontura? Falta de ar?"

            na "Não é nada. Só espera um pouco..."

            mc "Tá legal."

    na "..."

    na "Estou melhor. Eu só precisava respirar um pouco. Mas tá quente demais aqui."

    mc "Essa jaqueta parece bem quente mesmo. E tá calor."

    menu:
        "Tira esse casaco e fica de blusa.":


            mc "Melhor você tirar essa jaqueta. Só tem a gente mesmo aqui."

            na "Você acha que é seguro?"

            mc "É a sala do prefeito, né? Acho que ninguém vai entrar aqui."

            na "Isso é verdade. Eu nunca vi isso acontecendo. É uma boa ideia."
        "Melhor a gente tomar cuidado.":


            $ natasha_seducao += 2

            mc "E-eu ia falar pra você ficar à vontade, mas aqui é meio perigoso, né?"

            na "Concordo. Mas tá difícil pra eu respirar."

            mc "Calma que eu vou fechar a porta pra você. Assim você fica tranquila."

            na "Obrigada, [mc]."

    scene na4_img15 with Dissolve(1.0)

    pause

    na "Agora está melhorando."

    mc normal "Fica à vontade. Tá tudo legal."

    na "Nem parece que eu que trabalho aqui e você é o estranho."

    mc desculpa "O que aconteceu? A gente pode conversar?"

    na "Agora que ele foi, podemos conversar em paz."

    na "Eu estava preocupada que você acabasse falando alguma coisa que não devia."

    na "Eu odeio quando a situação não depende de mim. Eu fico extremamente nervosa quando preciso contar com os outros."

    mc envergonhado "E você não confia em mim pelo jeito."

    na "Não é nada especial. Eu não confio em ninguém, [mc]. E isso devia ser regra para todo mundo."

    mc "Parece um pouco dark demais pensar assim."

    na "Isso é algo que você aprende na vida. Mas eu não sei porque eu estou falando isso pra você."

    na "A questão é que você conhece mais sobre mim do que o [pr] sabe. Quanto mais você falasse, maior a chance de ferrar tudo."

    menu:
        "Eu nunca prejudicaria você.":


            $ natasha_seducao += 2

            mc preocupado "Eu nunca falaria algo que ia prejudicar você."

            na "Não por vontade própria, mas tem muita coisa em jogo aqui, [mc]."

            mc desculpa "Acho que eu entendo... mesmo sem saber eu podia falar alguma merda."

            na "Exatamente. Por isso foi tão tenso."
        "Do que você tem medo?":


            mc preocupado "Do que você tem tanto medo?"

            na "Não quero falar sobre isso. Mas só pra você entender, meu medo é jogar fora muita coisa que eu construí aqui na prefeitura."

            mc desculpa "Acho que eu saquei."
        "Você precisa relaxar um pouco.":


            mc envergonhado "Você precisa relaxar um pouco, [na]. Você vai ter um treco um dia desses ainda."

            na "Não sei se você fala isso sério ou só pra avacalhar mesmo."

            mc desculpa "É sério, poxa."

            na "Você é de outro mundo, [mc]. Eu vivo esquecendo disso."

    na "Mas não adianta a gente ficar pensando nisso agora. Tudo passou e foi melhor do que eu imaginava."

    mc normal "Parece uma boa notícia."

    scene na4_img16 with Dissolve(1.0)

    pause

    na "Incrível como você consegue cativar as pessoas. Nem mesmo um homem treinado como ele não conseguiu se controlar."

    mc "Você parece impressionada."

    na "Quem não ficaria? Meu trabalho seria muito mais fácil se eu tivesse essa sua capacidade."

    mc "Então essa é sua profissão? Você é uma faz-tudo do prefeito da cidade? Quem diria..."

    na "É. Agora você que parece impressionado."

    mc "Você tá no topo da cidade. Quem não acharia impressionante?"

    na "Ser a cadelinha de um poderoso não é o melhor dos trabalhos. O [pr] é um homem bem ativo. Todo meu dia eu gasto fazendo coisa pra ele."

    "A [na] é uma empregada do prefeito, que deve ser um dos cabeças da cidade. Isso quer dizer que..."

    mc "Então você tá do lado dos italianos?"

    na "O que você quer dizer com isso?"

    mc "Não se faça de boba, [na]. Eu sei que o prefeito faz parte de um grupo de poderosos que mandam na cidade."

    mc "Ele pode vir com aquele papo de 'restaurante', mas eu sei que uma gaivota só não faz verão. Ele tem as costas quentes."

    na "Hmm... não sei o que você espera que eu responda."

    mc "Eu só quero que você fale à verdade."

    na "A verdade é que eu trabalho pra ele. Apenas isso. O que isso quer dizer na sua cabeça, é entre você e você."

    menu:
        "Eu entendi o que isso quer dizer.":


            mc desculpa "Ok, pra meio entendedor, meia palavra é o suficiente. Eu entendi o que você quis dizer."

            na "Muito bem. Agora que a gente encerrou isso, acho que podemos ir."
        "Vamos parar de falar disso.":


            $ natasha_seducao += 2

            mc charmoso "Você tem razão. Eu cansei desse assunto e tá tudo muito bem explicado já."

            na "Perfeito. Eu prefiro manter as coisas de forma simples e direta."

    mc "A gente podia aproveitar e conversar sobre outras coisas então."

    na "Aqui?"

    mc "Eu sei que você não vai querer ir pro bar, que você tá correndo com o trabalho. Então, a gente pode fazer nossa happy hour aqui mesmo."

    scene na4_img17 with Dissolve(1.0)

    pause

    na "Happy Hour? Só você mesmo... E sobre o que você ia querer falar nessa nossa happy hour?"

    mc charmoso "Hmm..."

    menu:
        "Tá saindo com alguém?":


            $ natasha_seducao += 2

            mc charmoso "O que eu mais queria saber é se você tá saindo com alguém..."

            na "Esse tipo de pergunta revela bastante sobre suas intenções com todo esse papo."

            mc "A é? É só uma pergunta inocente pra puxar conversa. Namoro e qual série que você tá assistindo não pode faltar."

            na "É assim que funcionam as conversas então?"
        "O que você tem feito além de trabalhar?":


            mc normal "O que você tá fazendo além de trabalhar?"

            na "Muito pouco. Eu gosto de ler no meu tempo livre."

            mc normal "Olha aí. Uma coisa que eu não sabia sobre você."

            na "Eu gosto de livros de mistério e investigação. Tem um inclusive um detetive que eu gosto muito."

            mc "Quem é?"

            na "Dizem que ele existe de verdade. Ele viveu na capital aqui há alguns anos e ele resolveu diversos casos."

            na "Daí um autor aqui da cidade romantizou alguns dos casos dele e escreveu esse livro."

            na "Mas dizem que é tudo baseado em casos reais que aconteceram aqui na capital mesmo."

            mc "Nossa. Parece interessante mesmo."

    na "Sabe, [mc]... Eu realmente não tenho muitas oportunidades de conversar com as pessoas assim."

    na "Talvez conversar com alguém assim, sem motivo... acaba fazendo bem, né?"

    mc charmoso "Claro. Às vezes, quando a vida tá esmagando, a gente precisa mudar um pouco o pensamento."

    mc "Quando a gente tá numa situação difícil, parece que é impossível ver fora do problema."

    mc "É nessas horas que a gente precisa fazer o contrário. Se preocupar demais torna as coisas ainda mais pesadas."

    mc "Por isso, a gente tem que ter coragem de não fazer nada. Se afastar um pouco e recuperar as energias."

    na "Ter coragem pra não fazer nada? Parece contraditório, [mc]."

    mc envergonhado "Verdade... mas se você pensar faz sentido."

    mc normal "Quando a gente tá muito atolado num buraco, a gente tem que sair do buraco, ou vai ficar tudo escuro."

    mc "Agora, se você sair do buraco, e olhar junto com a luz, você vai ver muito melhor."

    mc "Por isso que eu acho que quando a coisa tá muito difícil, não adianta ficar pensando e pensando no problema."

    mc "Bora fazer outra coisa. Se divertir um pouco, e depois voltar com tudo pra resolver esse problema."

    na "Acredito ainda ser um pouco irresponsável. Mas não diria que não faz sentido. Você tem alguma coisa aí."

    na "Então... se eu estiver nesse buraco... o que você me aconselharia fazer para me divertir?"

    mc charmoso "Puxa... essa é uma boa pergunta... E eu tenho a resposta certa pra você."

    na "Tem? O que você me recomenda, doutor?"

    "Boa! Essa é minha chance. Se eu quero alguma coisa com a [na], essa é a hora certa."

    "A [na] é uma garota maravilhosa, muito inteligente, segura de si. É o tipo de mulher que você só encontra uma na vida."

    "E normalmente um cara que nem eu nunca ia ter a chance de ficar com ela assim."

    call namorando from _call_namorando_2

    if namorando:

        "O problema é que eu já tô comprometido. Será que eu quero me meter em mais um romance?"

        "A não ser que seja só uma ficada... mesmo assim, seria cuzão demais da minha parte."

    "O que eu respondo pra ela? Eu tomo a iniciativa ou não?"

    menu:
        "Dizem que um beijo é a melhor forma.":


            mc charmoso "Olha... eu ouvi que a melhor forma da gente esvaziar a cabeça é com uma emoção bem forte."

            mc "Daqui sua mão. Eu vou te mostrar."

            na "O que você vai aprontar?"

            scene black with dissolve

            mc safado "Vem aqui."

            scene na4_img18 with Dissolve(1.0)

            pause

            na "Por que eu tava suspeitando que a gente ia acabar assim?"

            mc "Nada como um beijo bem dado e uma boa pegada pra gente esquecer o resto."

            na "Se alguém entrar aqui eu vou ser despedida."

            mc "Provavelmente eu também... mas vai valer à pena, eu prometo."

            na "[mc]... eu..."

            if natasha_seducao >= 38:

                $ natasha_e4 = "seducao"

                na "Não vou mentir... eu quero te beijar agora. Eu estou precisando muito disso. E não só de um beijo. Eu preciso de mais."

                mc "Então deixa eu cuidar de você."

                na "Eu não posso colocar tudo a perder. Por mais que eu queira, meu trabalho é tudo pra mim."

                if na1_beijo:

                    mc "Lembra quando a gente se beijou no Cassino?"

                    na "Lembro..."

                elif na3_beijo:

                    mc "Lembra do nosso beijo lá no Distrito? Pra despistar o Montanha?"

                    na "Sim..."
                else:


                    mc "Vai ser rápido. E você vai se sentir melhor. Eu prometo."

                    na "Se você pudesse me garantir isso..."

                    "Droga... se eu tivesse beijado ela antes... talvez agora eu pudesse falar algo pra ela."

                    "Eu impressionei ela hoje, eu tenho certeza, mas eu precisava ter tido algo quente com ela antes!"

                    "Se desse pra voltar no tempo! Que droga!"

                    jump natasha_e4_falhou

                mc "Não foi bom?"

                na "Claro que foi."

                mc "Só deixa eu fazer isso de novo. Eu prometo que você vai se sentir melhor."

                scene na4_img19 with Dissolve(1.0)

                pause

                na "Eu sei que o certo é não aceitar esse seu convite...{w} Mas por que eu não consigo?"

                mc "Porque você experimentou a fruta e gostou... e agora não consegue não provar de novo. É a minha teoria."

                na "Você é um jornalista mesmo. Sabe sempre a coisa certa pra falar."

                mc "Minha boca não serve só pra falar, sabia?"

                na "Então me mostra pra que ela serve. Eu tô cansada de te ouvir já, mesmo."

                mc "Você também... vem aqui."

                scene na4_img20 with Dissolve(1.0)

                pause

                na "Era exatamente isso que eu precisava. Da sua boca, [mc]."

                mc "Então aproveita. Eu tô aqui pra você."

                window hide

                pause

                "Não acredito que eu tenho a chance de ficar de novo com uma mulher maravilhosa como a [na]."

                "Tô começando a achar que eu realmente tô levando jeito. Quem ia imaginar que eu ia chegar nisso..."

                na "Ei."

                mc "Hm?"

                na "Sua cabeça tem que estar totalmente em mim agora."

                mc "C-com certeza."

                if natasha_e2 == "positivo":

                    mc "Lembra quando eu te contei sobre o Barão?"

                    na "Sim."

                    mc "Você só pegou a informação e sumiu por um tempo sem falar nada."

                    na "Eu sei..."

                    mc "Tá na hora de pagar."

                    na "Pode cobrar então."

                    mc "Que garota de honra."

                    scene na4_img21 with Dissolve(1.0)

                    pause

                na "Se a gente continuar assim eu não vou querer parar no beijo."

                mc "Mais uma razão pra eu continuar."

                window hide

                pause

                na "Tá bom. Chega. P-por favor. Eu não consigo mais pensar."

                mc "[na]..."



                label na4_premium1:

                    pass

                menu:
                    "Eu não quero que você pense.":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_40

                            jump na4_premium1

                        mc "Mas eu não quero que você pense. Eu quero que você deixe eu pegar você."

                        na "Ah, [mc]... mais ainda?"

                        scene black with dissolve

                        scene natasha4_premium1 with Dissolve(1.0)

                        pause

                        mc "É disso que eu tô falando."

                        na "A-ah... meu pescoço..."

                        mc "Você gosta?"

                        na "Eu nem sei mais... hmmm... o que tá acontecendo... m-minha roupa?"

                        mc "Só curte."

                        na "É perigoso demais, [mc]... se alguém pega a gente aqui... se o prefeito... hmm..."

                        mc "O risco vale à pena, não vale?"

                        na "Você é louco... esse é o pior... nnghh... lugar do mundo pra gente fazer isso!"

                        mc "Você vai correr de mim se eu não fizer isso agora."

                        na "Hmmm... você é impossível, isso sim..."

                        scene natasha4_premium2 with Dissolve(1.0)

                        pause

                        na "Ah... sua sorte é que eu não aguento... no pescoço assim..."

                        mc "Te deixa quente, é?"

                        na "Muito... eu já tô toda molhada, [mc]..."

                        mc "Valeu por falar. Porque é importante pro que eu quero fazer."

                        na "Mais? Nnghh... isso é d-demais."

                        mc "Ninguém vai pegar a gente, [na]. Fica tranquila."

                        na "Não. Se o prefeito aparecer é fim da linha. Ele... nunca ia aceitar algo assim."

                        mc "É só um emprego. Hmm..."

                        na "Aah... não... me demitir é o mínimo... hmmm... esse homem é capaz de coisa muito pior."

                        mc "Você tá viajando."

                        na "Para... já tá bom..."

                        "Eu não quero parar agora... de jeito nenhum. Mas será que é perigoso mesmo?"

                        "Se ele me pegar com a secretária dele assim... será que ele manda alguém dar um tiro na minha cabeça?"

                        menu:
                            "Vale à pena correr o risco.":


                                mc "Você vai ver que vai compensar, [na]..."

                                na "Não... como assim?"

                                mc "Tira isso aqui e deixa eu te mostrar."

                                scene black with dissolve

                                na "!"

                                scene natasha4_premium3 with Dissolve(1.0)

                                pause

                                na "M-minha... aaah..."

                                mc "Eu sabia que você tava gostando... o pescoço é bom, né?"

                                na "Não... hmmm... aí, não..."

                                mc "É difícil resistir aqui, né?"

                                na "Claro... você mexe tão gostoso... hmmmm..."

                                mc "Aproveita... entra no clima..."

                                na "Eu tô deixando você enfiar o dedo em mim na sala do meu chefe... o prefeito da capital... mais louca que isso eu não fico."

                                mc "Falando assim... você deve tá bem louca mesmo."

                                na "Nnnhhaa.... aahn..."

                                mc "Você não sentiu tudo ainda..."

                                scene natasha4_premium4 with Dissolve(1.0)

                                pause

                                na "Ai, [mc]... c-cuidado... aaahnn..."

                                mc "Claro... eu faço com carinho pra você, gata."

                                na "Hmmnnng... tá tão bom... eu tô quase gozando só com isso..."

                                mc "Calma que a gente só tá começando. Eu quero ir até o fim."

                                na "Você é maluco... nnnghh..."

                                mc "Maluco de tesão por você, gostosa. Não aguento mais esperar pra experimentar essa bucetinha outra vez..."

                                na "Aahnn... nnnghh..."

                                na "Me beija."

                                na "Me beija que eu vou gozar!"

                                scene black with dissolve

                                scene natasha4_premium5 with Dissolve(1.0)

                                pause

                                na "Nngh... que delícia... que delícia, [mc]!"

                                mc "Então goza... goza pra eu saber que você não aguenta."

                                na "Nngghh! Tô quase!"

                                mc "Me beija então."

                                na "Aahh! Aaahnnnn!"

                                na "Isso! Continua mexendo aí! Me fode com sua mão! Aannnghh!"

                                mc "Vai! Goza pra mim!"

                                na "NNNGHHHHHHHHHHHHH!!"

                                scene natasha4_premium5 with vpunch

                                na "AAAGGGHHNNN!!!"

                                mc "Gostoso?"

                                na "Ai... hnng... muito... você é perfeito..."

                                mc "Você que é perfeita."

                                na "E agora?"

                                menu:
                                    "Tô satisfeito. Bora parar aqui.":


                                        mc "Pra mim tá excelente, [na]..."

                                        na "Você foi demais, [mc]... eu nunca vou esquecer o que você fez aqui..."

                                        mc "Respira um pouco que você tá precisando."
                                    "Agora é a minha vez.":


                                        mc "Que bom que você gostou... mas a gente não vai parar aqui, né?"

                                        na "Depois dessa delícia, eu não vou te deixar na mão..."

                                        scene black with dissolve

                                        scene natasha4_premium6 with Dissolve(1.0)

                                        pause

                                        mc "A-ah..."

                                        na "Mmnnnhh..."

                                        mc "Que delícia, [na]..."

                                        na "É sua vez de gozar agora, gostoso."

                                        mc "Desse jeito eu gozo mesmo..."

                                        na "Deixa eu aproveitar um pouquinho antes..."

                                        mc "Mmnngg... não me provoca assim..."

                                        na "E não é só nele, não... eu cuido das suas bolas também..."

                                        scene natasha4_premium7 with Dissolve(1.0)

                                        pause

                                        mc "Aah... como você faz gostoso."

                                        na "Eu faço tudo pra você. Você gosta da minha boca no seu pau?"

                                        mc "Eu adoro... você chupa gostoso pra caralho."

                                        na "Hmmm... que bom..."

                                        mc "Aagh... continua fazendo assim."

                                        na "Você vai segurar?"

                                        mc "Eu quero... mas não sei quanto tempo..."

                                        na "Se quiser pode jorrar tudo na minha boca."

                                        mc "Nnghh!"

                                        scene natasha4_premium8 with Dissolve(1.0)

                                        pause

                                        mc "Se continuar assim..."

                                        na "Ou será que você prefere sentir minha..."

                                        mc "Aagh... que dúvida cruel, gostosa."

                                        na "O que você prefere? Gozar na minha boca ou dentro de mim?"

                                        mc "E dá pra escolher entre duas coisas tão deliciosas?"

                                        na "Você vai ter que escolher..."

                                        mc "Eu quero gozar logo, mas também quero aproveitar sua buceta delícia."

                                        na "A decisão é toda sua... eu tô pronta pra você..."

                                        "O que eu faço?"

                                        menu:
                                            "Jogar ela na mesa e continuar":


                                                mc "Não vou conseguir parar aqui, amor. Deixa eu sentir sua xotinha!"

                                                na "Ela é tua. Ela tá molhada. Faz o que você quiser com ela."

                                                scene black with dissolve

                                                scene natasha4_premium9 with Dissolve(1.0)

                                                pause

                                                na "Aaahhnn! Era isso que você queria?!"

                                                mc "Isso! Eu precisava sentir você de novo!"

                                                na "Melhor pra mim! Hmm! Que eu posso sentir essa delícia! Ahnn!"

                                                mc "Você quer chegar lá de novo?"

                                                na "Sim! Com seu pau agora! Nnghh!"

                                                mc "Eu vou dar o que você quer então!"

                                                na "Isso! Hmmm! Assim mesmo!"

                                                scene natasha4_premium10 with Dissolve(1.0)

                                                pause

                                                na "Nnghnhh!!! Assim mesmo! Com vontade!"

                                                mc "Eu não vou aguentar muito mais, [na]! Eu já tava quase gozando só com a sua chupada!"

                                                na "Vai mais um pouco! Aahnn! Deixa eu sentir mais!"

                                                mc "Se você gemer assim, daí que eu não aguento!"

                                                na "Hmmm! Nnnghh! Mais um pouco, gostoso!"

                                                mc "Vai sair, gostosa! Você é boa demais, caralho!"

                                                na "Annghh! NGGHH!!"

                                                mc "Tá vindo, [na]! Vai sair!"

                                                na "Eu quero! NNGHH! Joga em mim, delícia! NNNGHHHHHHHHH!!!"

                                                scene natasha4_premium11 with hpunch

                                                pause

                                                mc "AAGGHHHH!!!"

                                                na "NNNGHH!!! ASSIMM!!!"

                                                mc "Tô gozando dentro de você, safada!"

                                                na "Tô gozando de novooonnn!! HMMMM!!!"

                                                na "Aah... aah... tudo dentro de mim..."

                                                mc "Sim... um monte de porra pra você..."

                                                na "Aaii... duas vezes... essa foi demais, [mc]..."

                                                mc "Eu também achei, gostosa... você foi bem demais..."

                                                na "Parece que a gente realmente tem química, né?"

                                                mc "Agora tá comprovado..."
                                            "Gozar na boca dela":


                                                mc "Eu queria te comer, mas não aguento! Preciso encher sua boca!"

                                                na "Então vai! Me dá tudo!"

                                                mc "Nnghh! Continua chupando e mexendo nas minhas bolas! AAGH!"

                                                na "Uhum! Mmggh!"

                                                mc "Assim! Vai! Tá saindo!"

                                                scene natasha4_premium8 with vpunch

                                                mc "AAAGHH!"

                                                na "Nnnghh! Quanta porra!"

                                                mc "Aaghhh... aahh... que gozada..."

                                                na "Adorei..."
                            "Melhor a gente parar aqui...":


                                mc "Você tá certa. Melhor a gente parar por aqui... mas na próxima..."

                                na "Na próxima a gente vai até o fim. A gente faz tudo o que você quiser..."

                                mc "Hmmm..."

                        scene black with dissolve

                        scene natasha4_premium12 with Dissolve(1.0)

                        pause

                        na "Ah... que loucura... sorte que ninguém pegou a gente..."

                        mc "Sorte mesmo..."

                        na "Mas, olha... você tinha razão."

                        mc "No quê?"

                        na "Eu precisava mesmo de uma... pegação."

                        mc "Eu disse. Você tem que me ouvir mais vezes."

                        na "Vou tentar lembrar disso na próxima vez... se tiver uma..."

                        mc "Claro que vai... eu nunca vou deixar uma mulher perfeita igual você escapar assim..."

                        mc "Toda vez que eu olho pra você eu ainda fico bobo como você é perfeita."

                        na "Não precisa ficar me elogiando... você já conseguiu o que você queria."

                        mc "Já falei que não é elogio... é como você é mesmo..."

                        na "Ok... agora é melhor a gente não abusar também."
                    "Tudo bem...":


                        mc "Ok..."

                        na "Deixa eu falar."

                        scene na4_img19 with Dissolve(1.0)

                        na "Você tinha razão."

                        mc "No quê?"

                        na "Eu precisava mesmo de uma... pegação."

                        mc "Eu disse. Você tem que me ouvir mais vezes."

                        na "Mas da próxima vez. Hoje a gente para aqui."

                        mc "Mas olha como eu tô aqui em baixo. Você vai perder essa chance?"

                        na "É tentador, mas vamos deixar a parte final pra próxima."

                        mc "Se é o jeito..."

                na "Vem. Vamos nos ajeitar."

                scene black with dissolve

                pause 0.5
            else:


                na "Não vou mentir... eu quero te beijar agora. Eu estou precisando muito disso. E não só de um beijo. Eu preciso de mais."

                mc "Então deixa eu cuidar de você."

                na "Eu não posso colocar tudo a perder. Por mais que eu queira, meu trabalho é tudo pra mim."

                mc "Vai ser rápido. E você vai se sentir melhor. Eu prometo."

                na "Se você fosse o homem certo pra mim, talvez. Mas eu não sinto que vai acontecer dessa vez."

                "Droga... Talvez se eu tivesse feito as coisas de uma outra forma hoje, talvez eu pudesse ter impressionado mais ela."

                label natasha_e4_falhou:

                    pass

                mc "Tudo bem... você cortou meu barato, mas eu não vou desistir assim."

                na "Você é um homem e tanto. Mas as coisas são complicadas..."

                mc "Tudo bem."

                scene black with dissolve

                scene na4_img22 with Dissolve(1.0)

                pause

                jump natasha_e4_amizade
        "A gente podia beber juntos um dia desses.":


            label natasha_e4_amizade:

                pass

            $ natasha_e4 = "amizade"

            mc normal "E se a gente bebesse juntos um dia desses?"

            na "Tipo no Cassino?"

            mc "Isso aí. Jogar conversa fora com alguém é uma das melhores formas da gente dar uma desconectada de tudo."

            na "E você sairia comigo? Eu não sou a melhor companhia."

            mc "Claro. Você é mais legal do que imagina, [na]. Você é quietona, mas fala muito bem."

            na "Você é bonzinho demais, [mc]. Até mais do que seria conveniente pra você."

            scene na4_img22 with Dissolve(1.0)

            pause

            na "Eu falo isso porque as pessoas costumam pisar nas pessoas boas, nas pessoas que se mostram vulneráveis."

            na "Quando você demonstra pra alguém que ama ela, ela se sente no direito de te ferir."

            na "E é por isso que você não pode mostrar seus sentimentos. Nem mesmo pra mim."

            mc desculpa "Você é uma pessoa boa, [na]. E viver com medo desse jeito, só vai fazer você sentir sozinha e acuada."

            na "Eu sei... mas a gente precisa fazer isso, [mc]. É o único jeito da gente evitar situações horríveis."

            mc "Você... aconteceu alguma coisa com você, [na]?"

            na "Não... isso é uma coisa que eu nunca teria coragem de falar. Nem pra você, [mc]."

            mc concentrando "Ok... mas eu acho que um dia você vai falar pra mim, sim."

            na "Desculpa, mas não tenha esperanças quanto a isso."

            mc charmoso "Eu só preciso provar pra você, que seus sentimentos tão seguros comigo."

            mc "Eu não sei o que aconteceu com você no passado, mas um dia você vai ver que existem pessoas boas também."

            mc envergonhado "Talvez não no mundo que você tá acostumada, mas existem pessoas boas também."

            mc "Não existe pessoa perfeita, completamente boa, mas tem gente bacana, que pelo menos não vai foder você por se abrir."

            na "Vamos ver, [mc]... vamos ver..."

            mc desculpa "Acho que por hoje tá legal."

            na "Será que a gente pode ficar só mais um pouco aqui? Não precisa falar nada."

            mc normal "Claro."

            na "Eu... tô gostando de ficar sentada aqui com você. Só mais um pouco."

            scene black with dissolve

            "Eu queria saber o que aconteceu com a [na] que deixou ela assim..."

            "Mas, por enquanto, tudo o que eu posso fazer é ficar do lado dela, pelo menos mais um pouco."

            "..."

    scene na4_img23 with Dissolve(1.0)

    pause

    na "Eu só tenho a agradecer, [mc]."

    mc normal "E cuidado sair sem a jaqueta."

    na "Verdade. Isso só prova como você me deixou menos tensa."

    mc charmoso "Fico feliz em saber."

    na "Talvez esquecer um pouco os problemas e só espairecer um pouco realmente tenha suas vantagens."

    mc "Eu disse. Contanto que você não exagere e se meta em um problema maior ainda, tá tudo massa."

    mc envergonhado "Mas, olhando pra você, eu não preciso nem falar isso."

    na "Eu sei que na maioria das vezes eu sou tensa demais. Talvez um dia eu acabe mudando."

    mc "Só de ouvir você falar 'talvez' em uma frase mostra que você tá diferente. Normalmente você é tão assertiva."

    na "Nunca tinha reparado."

    na "Mas agora a gente tem que ir."

    mc desculpa "Uma pena..."

    na "Só que... eu imagino que não vai demorar muito pra gente se ver de novo. Principalmente depois do que o [pr] disse."

    mc preocupado "O que será que ele quer comigo?"

    na "A gente vai saber logo. Eu tenho uma ideia, mas eu não quero trair o chefe. Eu sou a mão direita dele, né?"

    mc envergonhado "Uma pena..."

    na "Ele é um bom prefeito. Você só precisa estar do lado certo, como ele disse."

    mc desculpa "Vamos ver..."

    mc normal "Até mais, [na]. Não vejo a hora de te ver de novo."

    na "Não pensei que fosse falar isso de novo um dia, mas eu também, [mc]."

    mc "Tchau."

    scene black with dissolve

    "Esse foi um dia e tanto. Eu tenho que voltar voando."

    pause 1.0

    scene na4_img7 with Dissolve(1.0)

    pause





    label na4_premium2:

        pass

    menu:
        "Será que nosso encontro deu problema pra Natasha? (+18)":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_41

                jump na4_premium2

            pr "Final do expediente é minha hora preferida..."

            na "Senhor..."

            pr "Você ficou um tempo falando com aquele jornalista, né? Vocês têm alguma coisa?"

            na "Claro que não... ele só pode ser um aliado importante."

            pr "Eu acredito em você, gatinha... mas eu tenho ciúmes. Você é perfeita demais."

            scene black with dissolve

            scene natasha4_premium13 with Dissolve(1.0)

            pause

            na "Você sabe que eu só trabalho pro senhor, prefeito..."

            pr "Só trabalho? Eu queria que você quisesse ficar comigo também."

            na "..."

            pr "Mas eu aceito nosso acordo... desde aquele dia que você aceitou ser uma boa secretária... você tá fazendo um trabalho excelente."

            na "É pra isso que eu tô aqui. Esse é meu trabalho."

            pr "Ver você toda entregue assim... hmm... é ainda mais gostoso, [na]."

            na "O senhor pode fazer o que você quiser comigo."

            pr "A gente precisa falar sobre o Distrito. Mas deixa pra depois, né?"

            menu:
                "É urgente. Melhor falarmos agora.":


                    na "Eu acho que o melhor é a gente falar agora, senhor..."

                    pr "Poxa... se você acha importante assim... deixamos nossa brincadeira pra outro dia..."

                    pr "Mas você não pode se vestir até acabar."

                    na "O-ok..."
                "O senhor é quem manda.":


                    na "O senhor que sabe..."

                    pr "Você sabe o que eu quero. Eu sempre quero seu corpo antes de qualquer coisa."

                    pr "Mas eu prometo que eu vou ser rápido. Você já me deixou duro o suficiente, meu bem."

                    pr "Vai pra mesa. Deixa eu te pegar por trás."

                    na "Uhum..."

                    scene black with dissolve

                    scene natasha4_premium14 with Dissolve(1.0)

                    pause

                    na "Nnghh!"

                    pr "Assim mesmo, querida! Você é a melhor secretária do mundo!"

                    na "Aggnh! Nnnghh!"

                    pr "A melhor buceta do mundo também! Nunca eu comi uma funcionária gostosa igual você!"

                    na "Aah! Aahnn!"

                    pr "Isso! Geme pro papai, amor!"

                    scene natasha4_premium15 with Dissolve(1.0)

                    pause

                    pr "Toda vez que a gente transa eu não aguento mais que alguns minutos dentro de você!"

                    na "Nnghh! S-sim!"

                    pr "Que magia é essa que você tem que faz meu pau querer gozar rápido desse jeito?!"

                    na "Ahhn! Você me acha bonita, senhor?! Hmm!"

                    pr "Bonita?! Ngh! Você é a coisa mais linda que já pisou na Terra, garota! Poder transar com você é a maior benção do mundo!"

                    na "Então goza em mim, chefe!"

                    pr "Aghh! Pede mais uma vez que você vai ter!"

                    na "Goza na sua secretária!"

                    pr "A-aghh!"

                    scene natasha4_premium16 with hpunch

                    pause

                    pr "Aaghhhhh!"

                    na "Nggh!!!"

                    pr "Tá saindo! Que delícia! AAGHH!!"

                    pr "Te comer é a melhor coisa do mundo, [na]!"

                    na "Mmm..."

                    pr "Aah... aah..."

                    pr "A melhor contratação da história da prefeitura... aah..."

                    pr "Eu fico imaginando o que meu pai faria se conhecesse você... mmnn..."

                    na "S-senhor..."

                    pr "Hora do assunto sério. Deixa eu colocar minha calça."

                    na "E e-"

                    pr "Você não coloca roupa ainda. Me fala peladinha assim... deixa eu te admirar mais um pouco."

                    na "Tá."

            scene black with dissolve

            scene natasha4_premium17 with Dissolve(1.0)

            pause

            pr "O que você conseguiu pra mim no Distrito?"

            na "Eu tenho uma informante lá dentro. E já consegui algumas coisas com ela."

            pr "Perfeito. Quais as novidades?"

            na "Tudo parece normal por enquanto. Mas esse jornalista de hoje. O [mc]. Parece que ele tá metido em algo lá também."

            pr "Quem é esse rapaz? Eu nunca tinha ouvido falar dele antes. E você não é a primeira que cita ele pra mim."

            pr "Ele não tá na nossa folha, né?"

            na "Não."

            pr "Ele parece um garoto ambicioso. Eu acho que a gente pode trazer ele pro nosso lado. Eu conto com você nessa também."

            na "Posso..."

            pr "Eu não queria, mas se for necessário, você sabe que pode usar todas suas armas."

            na "Pode deixar, senhor. Eu vou garantir que nossos interesses sejam cumpridos."

            pr "É nisso que eu gosto de você, além dessa perfeição toda. Você é dura quando precisar ser, [na]. Tem tudo sob controle."

            na "Obrigada, prefeito."

            na "Mas o Gustav e o Barão continuam preocupando... o que fazer com eles? Não seria melhor salvar as garotas?"

            scene natasha4_premium18 with Dissolve(1.0)

            pr "Aqueles dois... Por que a elite sempre é atrasada e mesquinha? Só ter um pouco de dinheiro que a pessoa se torna uma idiota."

            pr "Eles não entendem que o poder das sombras é muito mais importante que toda essa exibição."

            na "Nós realmente precisamos do dinheiro deles?"

            pr "Claro. Não só para a reeleição, mas para manter a máquina operando. Nossa ação com a Faux está custando uma nota."

            na "Entendo... mas falta pouco agora, certo?"

            pr "Sim. Aquela revista... ela é a última que ainda tem alguma ameaça contra nós."

            pr "Mas quando tirarmos o velho da jogada e viermos com a proposta, os acionistas vão aceitar na hora."

            pr "Mas os dois precisam parar de causar dor de cabeça. Eu não tenho tempo pra lidar com isso."

            na "E ainda tem aquela ovelha negra que o Tony disse."

            pr "Nem me lembre disso. Se realmente tem alguém aqui na capital querendo destruir tudo que minha família construiu essas décadas todas..."

            na "Não se preocupe, senhor. Você vai dar um jeito. Você vai manter o império como seu pai e seu avô fizeram."

            pr "É o que eu espero. Pra isso eu preciso que os pilares continuem sustentando nossa dinastia."

            pr "Eu conto com você, [na]. Mantenha o Barão na linha, o Distrito e tente descobrir quem é essa ovelha negra de alguma forma."

            pr "Não dá pra confiar só no Tony. Como eu disse, ele não passa de um homem ordinário que deu sorte no casamento."

            na "Vou dar meu melhor, prefeito."

            pr "Agora vamos continuar. Temos que manter a cidade andando ou os votos não virão."
        "Ela consegue se cuidar sozinha.":


            "Nah... ela sabe se virar."

    label natasha_e4_final:

        pass



    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    $ tempo = 3

    $ v49_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v49_fim","final","local")

    call checa_final from _call_checa_final_8

    jump call_cidade

label natasha_18_distrito:

    $ natasha18 = 1

    "{b}Um tempo atrás...{/b}"

    scene distrito_clube geral with Dissolve(1.0)

    pause 0.5

    "Nora" "Aquela só faz o que ela quer... não adianta você insistir."

    ce "Tudo bem... eu vou atender ela..."

    "Nora" "Que seja, pirralha."

    scene black with dissolve

    scene natasha3_premium12 with Dissolve(1.0)

    pause

    na "Então é você que vai me atender."

    ce "Eu tô aqui pra servir, senhorita..."

    na "Boa garota. Você vai obedecer tudo o que eu mandar?"

    ce "Tudo o que a senhora quiser... é pra isso que eu sirvo."

    na "Excelente. Eu preciso de uma boa garota igual você hoje."

    ce "Eu nasci pra isso, mestra. Pra ser uma boa garota pra você."

    na "Agora me diga... você vai responder tudo o que eu perguntar pra você?"

    ce "Com certeza... mas a senhorita não prefere que eu cuide de outra forma... muito mais... prazerosa?"

    na "Talvez... mas antes, eu preciso deixar uma coisa bem clara com você."

    ce "Hm? Tem certeza que a senhorita entende o que nós fazemos aqui?"

    na "Olha... eu não estou aqui pra uma sessão comum do seu trabalho... que eu imagino que seja incrível."

    ce "Claro que não, senhorita... ninguém está..."

    na "Mas você vai fingir que tudo tá acontecendo igual sempre... vai me servir igual serve todo mundo aqui, ok?"

    ce "Claro... faz de conta..."

    na "O que eu vou te falar é muito importante. E pode mudar sua vida pra sempre."

    ce "Você quer me tirar daqui e me fazer sua esposa? Você é tão generosa, senhorita..."

    scene natasha3_premium13 with Dissolve(1.0)

    na "Você não tá levando minhas palavras à sério."

    ce "Por que você não deixa eu te atender e daí você me fala tudo isso..."

    menu:
        "Nada disso. Assim tá bom.":


            na "Não precisa. Primeiro eu quero que você me escute com atenção."

            ce "Que seja..."
        "Ok... vem aqui.":


            na "Você venceu... pode me atender enquanto eu falo..."

            ce "Muito melhor assim."

            scene black with dissolve

            scene natasha3_premium14 with Dissolve(1.0)

            pause

            ce "Não é muito melhor assim?"

            na "Claro que é. Mas você vai ouvir o que eu tenho pra falar?"

            ce "Com certeza..."

    na "Olha... eu fiquei sabendo que uma mulher loira de cabelo curto veio até aqui... e você atendeu ela."

    ce "Não posso falar sobre nossos clientes..."

    na "Vocês tiveram uma conversa diferente, antes dela abusar de você, certo?"

    ce "Senhorita... por favor..."

    na "Você disse que ia me obedecer."

    ce "Mas isso..."

    na "Tudo bem. Deixa pra lá e me escuta."

    na "Eu trabalho pra uma pessoa poderosa. E essa pessoa quer garantir que as coisas certas aconteçam."

    ce "O que isso quer dizer? Eu não acredito em pessoas boazinhas."

    na "Ele é um homem preocupado com a cidade. E ele tem medo que o Distrito esteja preparando algo."

    ce "Que que tem a ver comigo isso aí?"

    na "Você não quer me ajudar? Se você fizer um pequeno favor pra mim... ele vai te recompensar muito bem."

    ce "Vem aqui..."

    scene black with dissolve

    scene natasha3_premium15 with Dissolve(1.0)

    pause

    na "Hmm..."

    ce "Você tá falando sério? Essa pessoa aí... realmente precisa de mim?"

    na "Sim."

    ce "Se é verdade... o que vocês precisam de mim?"

    na "Isso não é pra hoje..."

    na "Eu vou voltar aqui outras vezes... e eu quero que você sempre venha me atender."

    ce "Isso não vai ser nenhum problema... você é muito linda. Uma das mulheres mais perfeitas que eu já vi."

    na "Obrigada... você é maravilhosa também."

    na "E daí... nas próximas vezes que eu vier... eu vou te explicar com calma. E você vê o que você acha."

    ce "Tudo bem... eu sempre achei a vida aqui muito sem graça. Eu gostaria de participar de alguma coisa diferente."

    na "E você vai... pode ter certeza."

    label na3_premium2:

        ce "Então tá... e agora?"

    menu:
        "Agora você me atende. Eu quero me sentir bem.":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_42

                jump na3_premium2

            na "Agora que a gente resolveu a parte chata... eu quero me sentir bem. Vem aqui."

            ce "E-ei... sem troca desse tipo... não posso beijar."

            na "Você quer me beijar... eu sei..."

            scene black with dissolve

            scene natasha3_premium16 with Dissolve(1.0)

            pause

            ce "Hmmm..."

            ce "Eu não faço isso... só pra você saber... é só porque você é... hmm... maravilhosa..."

            na "Parece que ser eu tem suas vantagens... e eu vou aproveitar também..."

            ce "Ah... faz tempo que eu não fico com alguém assim... os clientes não me excitam..."

            na "Tá parecendo que eu te excito."

            ce "É... tá parecendo..."

            na "Deixa eu ter certeza então... e fazer o que eu quero com você."

            ce "O que você quer?"

            na "Sentir mais sua boca deliciosa."

            ce "Vem... pode sentir..."

            scene black with dissolve

            scene natasha3_premium17 with Dissolve(1.0)

            pause

            ce "Ah... que delícia..."

            na "Você tá me deixando quente demais."

            ce "Esse é meu trabalho... hmmm..."

            na "Eu queria ser uma boa profissional igual você."

            ce "Você também tá me deixando molhada, gostosa... sua língua... brincar com ela é uma delícia."

            na "Hmm... você é perfeita... seu corpo carnudo... sua pele..."

            ce "Pode pegar. Eu sou só sua, senhorita."

            scene natasha3_premium18 with Dissolve(1.0)

            pause

            ce "Ah... ahnn..."

            ce "Você tá me deixando no clima de verdade..."

            na "Uhum..."

            ce "Fazia tanto tempo... hmmm... que eu não sentia esse fogo no meio das pernas."

            na "Ah... fala assim..."

            ce "Você gosta de me deixar excitada?"

            na "Gosto. Eu fico excitada também."

            ce "Eu tô molhadinha pra você, me amor."

            na "Isso... fica molhada pra mim."

            ce "Chega."

            scene black with dissolve

            scene natasha3_premium19 with Dissolve(1.0)

            pause

            na "Que foi, minha linda? Acabou meu tempo?"

            ce "Chega de me beijar."

            na "Tudo bem..."

            ce "Eu quero mais. Tira minha roupa."

            na "!"

            na "Verdade?"

            ce "Sim... olha pra mim... olha como você me deixou..."

            menu:
                "Tirar a roupa dela":


                    na "Seu desejo é uma ordem, querida."

                    ce "Isso."

                    scene black with dissolve

                    scene natasha3_premium20 with Dissolve(1.0)

                    pause

                    na "Hmm..."

                    ce "Olha bem pra mim..."

                    na "Que coisa linda..."

                    ce "Gostou?"

                    na "Mais do que eu gostei... eu desejo ela..."

                    ce "Você vai pegar?"

                    na "Eu adoraria... mas a gente não pode exagerar hoje."

                    ce "Foda-se o que a velha vai pensar... só me pega..."

                    na "Não... a gente precisa ir com calma, delícia."

                    ce "Vem logo..."

                    na "Na próxima."

                    scene natasha3_premium21 with Dissolve(1.0)

                    pause

                    ce "Não me deixa assim, gostosa!"

                    ce "Que maldade! Eu tô de perna aberta pra você!"

                    na "Até."

                    ce "Afe... você vai me pagar!"

                    na "..."

                    ce "Cruel... huhu..."
                "Melhor não exagerar e ir embora":


                    na "Vai ter que ficar pra próxima."

                    ce "Como assim?"

                    na "Logo logo a gente continua..."

                    ce "Não acredito... tudo bem..."
        "Eu vou embora. Só vim falar isso.":


            na "Eu termninei o que eu vim fazer. Eu vou pagar e tô indo embora."

            ce "Ela pode achar estranho..."

            na "Diga que você é melhor no seu trabalho do que ela imaginava..."

            ce "Haha... tudo bem..."

    ce "A gente se vê, gata."

    scene black with Dissolve(1.0)

    pause 1.0

    "{b}Voltando ao presente...{/b}"

    pause 1.0

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
