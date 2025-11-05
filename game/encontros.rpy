label ligar_priscila:

    if v6_fim and estou_na_cidade and not priscila_chutado:



        "Talvez agora seja uma boa hora pra chamar a [c] pra fazer alguma coisa."

        "O que eu vou fazer com ela hoje?"

        menu:
            "Chamar ela pra sair":


                jump encontro_priscila
            "Oferecer para fazer uma massagem":


                jump massagem_priscila









    elif priscila_chutado:

        "Eu e a [c] acabamos de terminar o namoro. Acho que não seria legal ligar pra ela."

        "Tenho que resolver isso antes de ligar pra ela de novo."

        mc concentrando "Se eu pudesse voltar no tempo e evitar que ela me chutasse..."

        jump call_cidade
    else:


        "Eu ainda não conheço ela o suficiente pra ligar e marcar alguma coisa."

        "Preciso continuar saindo com ela daí quem sabe eu tenha coragem de chamar ela nos próximos dias."

        jump call_cidade

label massagem_priscila:

    if tempo > 2:

        "Ixi. Já tá meio tarde pra isso. Melhor eu ligar amanhã durante a manhã ou a tarde."

        jump call_cidade

    if massagem_priscila_1vez:

        "Talvez eu possa oferecer uma massagem pra ela. E foi ela mesmo que me deu de presente o curso."

        "Deixa eu ligar."

        "Smartphone" "Tuu.... Tuuu...."

        c "Oi, [mc]!"

        mc normal "Tudo bem?"

        c "Tudo sim. E você?"

        mc "Também. Tava pensando se você não quer uma seção gratuita de massagem pelas mãos do mestre [mcc]."

        c "Uou! É um convite muito tentador!"

        c "Você está fazendo as aulas daquele curso? Que legal!"

        if mc_massagem == 0:

            mc envergonhado "Na verdade eu ainda não fiz nenhuma aula..."

            c "Sério?"

            mc "Mas eu achei que mesmo assim..."

            c "Você não quer me massagear, você quer amassar minhas costas."

            mc "Hehe..."

            c "Quando você tiver feito pelo menos uma aula, a gente vai lá onde você faz o curso e eu deixo."

            mc charmoso "Combinado. Você vai receber a melhor massagem da sua vida."

            c "Quero só ver."

            mc normal "Até mais tarde."

            c "Beijo!"

            "Então eu preciso começar esse curso o mais rápido possível."

            "Poder fazer massagem na [c] com certeza vai me deixar a gente mais íntimos, seja como amigos ou até algo mais."

            "O salão onde eles dão o curso fica no mesmo prédio onde eu moro."

            if massagista_negado > 0:

                "O problema é que eu passei lá e a moça não quis me atender."

                "Parece que eu tenho que encontrar ela pela cidade."

                "Talvez eu devesse olhar o {b}parque durante a noite{/b} e o {b}Tadaima logo pela manhã{/b}."
            else:


                "Preciso passar lá e trocar meu vale pelo curso."

            jump call_cidade
        else:


            mc feliz "Sim! O curso foi bem legal."

            if mc_massagem < 2:

                mc "Por enquanto eu já fiz uma aula só. Mas já aprendi um bocado."
            else:


                mc "Eu já fiz [mc_massagem] aulas. Estou aprendendo bem rápido."

            c "Isso é muito bacana, [mc]. Claro que eu topo. Estou ansiosa para sentir suas técnicas."

            mc normal "Então a gente se encontra no salão da [m] em meia hora?"

            c "Combinado. Tchau."

            mc "Até daqui a pouco."

            "Legal. Poder fazer massagem na [c] com certeza vai me deixar a gente mais íntimos, seja como amigos ou até algo mais."

            scene salao geral with Dissolve(1.0)

            mc normal "A [m] foi muito bacana em deixar a gente usar este espaço."

            show priscila feliz with dissolve

            c "Sim. Ela é um pouco estranha, mas é muito gente fina."

            mc charmoso "E você? Tá pronta pra massagem da sua vida?"

            if priscila_seducao_evento > 0:

                show priscila seduzida with dissolve

                c "Esse negócio de massagem me deixa um pouco sem jeito."

                c "Você pegando em mim... Sei lá..."

                mc charmoso "A [m] diz que a massagem serve pra várias coisas, inclusive pra apimentar as coisas."

                c "Ai, [mc]... cuidado comigo."

                mc "Pode deixar."
            else:


                c "Com certeza. Estou confiando que você vai fazer uma massagem caprichada."

                mc "Pode confiar."

            mc "Pode deitar ali e ficar à vontade."

            c "Ok."

            menu:
                "Você pode tirar a roupa se preferir.":


                    mc charmoso "Você pode tirar a roupa se você quiser, assim você sente melhor a massagem."

                    c "Quem sabe se você realmente me provar que é um massagista profissional, eu possa tirar."

                    c "Mas hoje de jeito nenhum."

                    mc envergonhado "Ok. Como você se sentir mais à vontade."

                    c "Obrigada. Você tá indo muito bem."
                "Agora é só ficar à vontade.":


                    mc charmoso "Agora é só relaxar e ficar à vontade, ok?"

                    c "Ok. Tá dando um friozinho na barriga."

                    mc normal "É tranquilo."

            mc normal "Então vou começar."

            c "Tá..."

            scene massagem priscila1 with Dissolve(3.0)

            pause

            c "Ai!"

            mc "O que foi? Algum problema?"

            c "Não. Só assustei um pouco. Desculpa."

            mc "Ah, tudo bem. Só fica relaxada."

            c "Ok..."

            "..."

            if mc_massagem >= 4:

                c "Até que tô gostando..."

                mc "Eu sabia que você ia gostar."

                c "Não quero ser chata, mas ainda falta um pouco pra você chegar no nível da [m]."

                mc "Eu imagino que sim. Eu estou na aula [mc_massagem] ainda."
            else:


                c "Ai..."

                mc "Desculpa. Te machuquei?"

                c "Um pouco."

                c "Você ainda tá no começo, né?"

                mc "Sim. Ainda tô na aula [mc_massagem]."

                c "Ainda tem um bocado pra melhorar."

            "..."

            "..."

            mc "Terminei."

            c "Ok."

            scene salao massagem with Dissolve(1.0)

            mc envergonhado "E aí, o que achou?"

            show priscila incerta with dissolve

            c "Acho que pra sua primeira vez está bom."

            mc "Sério?"

            c "Sim."

            mc normal "Então não vai fugir da próxima vez que eu te chamar."

            c "Claro que não. Você tem potencial. E eu quero ver melhorando conforme você for progredindo nas aulas."

            mc charmoso "Pode deixar que eu vou surpreender você."

            c "Tenho certeza que vai!"

            mc normal "Vamos nessa, então?"

            c "Vamos."

            scene salao geral with Dissolve(1.0)

            mc normal "Tchau, [m]!"

            c "Obrigada, [m]."

            m "Falous, galerinha. Podem vir sempre que precisarem."

            mc "Valeu."

            mc "Beijos, Pri."

            c "Beijão!"

            "..."

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("priscila_massagem_1vez","priscila","personagem")

            $ massagem_priscila_1vez = False

            $ tempo += 1
            $ dia_priscila = dia + 1

            jump call_cidade
    else:


        p rindo "Você poderá continuar a praticar massagem com a [c] na próxima atualização."

        p "As atualizações são publicadas a cada 15 dias, ok? Todo dia 1 e dia 15 de cada mês."

        p "Deixe o app instalado para receber notificações com notícias."

        p "Você também pode ver imagens exclusivas no nosso Insta/Face {b}@celebrityhuntergame{/b}."

        p "Agora pode continuar o game!"

        jump call_cidade

label encontro_priscila:

    call checa_logado from _call_checa_logado_2

    "..."

    "Deixa eu ver se a [c] tá afim de fazer alguma coisa juntos hoje."





    "Smartphone" "Tuu.... Tuuu...."

    c "Alô? [mc]?"





    call anuncio from _call_anuncio_3

    mc normal "Sou eu. Tudo bem?"

    c "Tudo legal! E você, como tá?"

    c "Já tava ficando com saudades de você..."

    mc normal "Eu também."



    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    call checa_tempo from _call_checa_tempo_3

    python:
        if renpy.android:
            etempo = PythonSDLActivity.checkEPtempoNext()
            ep_pontos = PythonSDLActivity.pegaEPpontos()

    mc normal "Tava pensando aqui... Quer fazer alguma coisa comigo agora?"

    c "Hmm..."

    if not etempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        c "Agora não vai dar, [mc]. Desculpa!"

        mc envergonhado "Tudo bem! Não esquente."

        c "Mas me liga outra hora, tá? Eu quero muito ver você."

        mc "Ok."

        scene black with Dissolve(1.0)

        p rindo "O [mc] pode chamar a [c] para sair uma vez a cada {b}12 horas do mundo real{/b}."

        p rindo "Vá com calma que você vai conseguir acertar todas as perguntas dela e ver uma cena secreta!"

        p lecionando "Use o app Relógio no celular do [mc] para ver quando o próximo encontro estará disponível"

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        p "Ou você pode liberar o próximo encontro agora mesmo usando Celebrity Coins"

        if persistent.coins >= 500:

            "{b}Liberar o próximo encontro usará 500 Celebrity Coins{/b}"

            menu:
                "Liberar encontro com a [c]":


                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaEPTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    "{b}Você usou 500 Celebrity Coins para liberar o próximo encontro com a [c]{/b}"

                    p rindo "Agora eu vou levar o [mc] para o começo da ligação para se encontrar com a [c]."

                    $ renpy.block_rollback()

                    if tempo < 3:

                        scene mapa cidade with Dissolve(1.0)
                    else:


                        scene mapa cidade_noite with Dissolve(1.0)

                    jump encontro_priscila
                "Agora não. Vou esperar o tempo":


                    p rindo "Você escolheu não liberar o próximo encontro agora, né? Sem problemas!"
        else:


            p "Você precisa de ao menos {b}500 Celebrity Coins{/b} para liberar o próximo encontro."

            p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja. Acesse o Menu para saber mais"

        p "Xau xau!"

        jump call_cidade
    else:


        c "Claro! O que você tá pensando?"

    if persistent.priscila_encontro_1vez and ep_pontos <= 0:

        jump priscila_encontro_1vez
    else:


        "Onde que a gente pode ir desta vez?"











    menu:

        "Bar" if tempo > 1:

            mc normal "Pensei em a gente beber alguma coisa no bar. O que me diz?"

            c "Eu tô dentro!"

            c "Te encontro lá em meia hora?"

            mc "Tá excelente pra mim."

            c "Ok. Até daqui a pouquinho."

            mc "Até!"

            "..."

            scene black with Dissolve(1.0)

            $ nandom = renpy.random.randint(1,3)

            "Opa. Ela tá chegando."

            if nandom == 1:

                scene pub geral with Dissolve(1.0)

                show priscila feliz with dissolve

                c "Oie!"

                mc normal "Oi! Tudo bem?"

                c "O que você acha hoje a gente sentar aqui mesmo?"

                mc "Por mim tá excelente."

                c "Eu gosto muito de vir aqui no bar com você."

                mc charmoso "Eu também gosto muito. Bom... eu gosto de ir em qualquer lugar com você..."

                c "Ai, [mc]..."

            elif nandom == 2:

                scene pub booth with Dissolve(1.0)

                c "Oi, [mc]. Tudo legal?"

                mc normal "Tudo sim."

                show priscila n_feliz with dissolve

                c "Foi aqui que a gente sentou no nosso primeiro encontro não foi?"

                mc "Verdade. E você tava usando essa mesma roupa se eu não me engano."

                c "Verdade?"

                show priscila n_brava with dissolve

                c "Ei!"

                c "Isso é uma crítica? Tá falando que eu não troco de roupa?"

                mc surpreso "Claro que não!"

                c "Ok..."

                show priscila n_hehe with dissolve

                c "Tá pronto?"

            elif nandom == 3:

                scene pub dois with Dissolve(1.0)

                mc normal "Oi, Pri."

                show priscila d_feliz with dissolve

                c "Olá! Que saudades."

                mc "Eu também tava."

                c "Quis sentar aqui no fundo hoje?"

                mc "Sim. Tudo bem pra você?"

                c "Claro!"

                show priscila d_hehe with dissolve

                c "Hmm...."

                c "Eu tava pensando se..."

                mc charmoso "Você quer continuar com nosso jogo?"

                c "..."
        "Parque":


            mc charmoso "O que você acha da gente ir no parque hoje?"

            c "Eu adoro o parque! Com certeza!"

            mc "Então tá combinado. A gente se encontra lá daqui a pouco."

            c "Ok. Beijo!"

            mc "Beijo."

            "..."

            scene black with Dissolve(1.0)

            "..."

            if tempo < 3:

                scene parque dia with Dissolve(1.0)

                "..."

                "Ela tá vindo ali."

                show priscila incerta with dissolve

                c "Oi."

                mc normal "Tudo bem?"

                c "Tudo..."

                c "Só tô me sentindo meio boba porque tava sentindo saudades de você."

                "Ela é muito fofa..."

                mc "Você é muito fofa, isso sim. Eu também tava."

                show priscila feliz with dissolve

                c "Hehe."

                c "Eu gosto muito daqui. Essa ilha é realmente muito bonita."

                mc charmoso "A gente devia vir aqui durante a noite também. As luzes são demais."

                c "Então não esqueça de me ligar durante a noite pra gente vir aqui ver."

                mc "Combinado."
            else:


                $ nandom = renpy.random.randint(1,2)

                if nandom == 1:

                    scene parque noite with Dissolve(1.0)

                    "O parque durante a noite é muito massa. Opa, lá vem ela."

                    mc normal "Boa noite, Pri."

                    show priscila d_feliz with dissolve

                    c "Boa noite, [mc]. Tudo bacana?"

                    mc "Tudo sim."

                    c "O parque é realmente muito bonito durante a noite."

                    show priscila d_brava with dissolve

                    c "Eu só nunca consegui entender essa estátua no meio."

                    c "Você sabe o que é isso?"

                    mc zerado "Parece um polvo, mas não tenho certeza."

                    c "Muito estranho..."

                    show priscila d_chateada with dissolve

                    c "Desculpe por falar sobre isso durante nosso encontro."

                    mc envergonhado "Eu sempre reparei nisso também, mas nunca comentei."

                    c "Hehe."

                elif nandom == 2:

                    scene parque banco_noite with Dissolve(1.0)

                    "Hoje vou esperar ela sentado aqui."

                    c "Bú!"

                    mc surpreso "Ouu!"

                    c "Hehe. Te assustei?"

                    mc desconfiado "Claro..."

                    c "Que bom."

                    show priscila n_hehe with dissolve

                    c "Eu peguei você diretinho..."

                    mc envergonhado "Eu achei que você ia vir dali, como sempre."

                    c "Pois é. Eu dei a volta na praça pra te assustar mesmo."

                    mc "..."

                    show priscila n_excitada with dissolve

                    c "Foi bem engraçado."

                    mc "Ok. Você me pegou. Parabéns."

                    c "Não precisa ficar ranzinza."

        "Praia" if tempo < 3:

            mc feliz "Bateu aquela vontade de ir pra praia. Topa?"

            c "Com certeza! Foi tão especial quando a gente foi lá!"

            mc normal "Fechou. Posso passar aí no hotel te pegar?"

            c "Ok. Até daqui a pouquinho."

            mc "Até!"

            "..."

            scene black with Dissolve(1.0)

            if tempo == 1:

                "..."

                scene praia dia with Dissolve(1.0)

                show priscila cansada with dissolve

                c "Eu adoro a praia! Aaaahhh..."

                mc envergonhado "Você realmente gosta da praia, hein?"

                c "Eu gosto muito!"

                c "O fofinho da areia, o sol, o som das ondas, os bichos voando ali fazendo aquele barulho estranho..."

                mc feliz "Ok ok, entendi."

                show priscila sexy with dissolve

                c "Eu acho que você prefere esta vista aqui, né?"

                mc surpreso "..."

                c "Cuidado desmaiar aí..."

                mc charmoso "Tenho que tomar cuidado mesmo."

                show priscila feliz with dissolve

                c "Certo!"

            elif tempo == 2:

                $ nandom = renpy.random.randint(1,2)

                if nandom == 1 and not p3_escolha == "amigo":

                    scene praia tarde with Dissolve(1.0)

                    c "..."

                    mc desconfiado "Tá meio quieta..."

                    show priscila d_excitada with dissolve

                    c "É que este lugar... naquela tarde..."

                    mc charmoso "Você fica sem jeito?"

                    c "Com certeza..."

                    mc "..."

                    c "Vamos trocar de assunto!!!"

                    show priscila d_excitada with dissolve

                    "..."
                else:


                    scene praia r_interior with Dissolve(1.0)

                    c "É..."

                    mc desconfiado "O que foi?"

                    show priscila preocupada with dissolve

                    c "Tem certeza que a gente pode comer aqui?"

                    c "Tudo parece tão caro..."

                    "Pior é que ela tem razão..."

                    mc normal "Não esquente."

                    c "O que você acha de eu pagar a conta?"

                    mc envergonhado "Não seria legal de minha parte fazer..."

                    show priscila brava with dissolve

                    c "[mc]! Não vai me dizer que você é desses machistas que acham que mulher não pode fazer nada."

                    mc desculpa "Claro que não. Só quero ser legal contigo."

                    c "Então para de ser tonto e querer pagar todas as vezes."

                    mc envergonhado "Ok..."

                    show priscila feliz with dissolve

                    c "Hoje é por minha conta, ok?"

                    mc normal "Certo. Se você acha que tudo bem."

                    c "Claro! Ser uma modelo super-famosa tem seu lado bom também, né?"

                    c "Dinheiro não falta."

                    mc zerado "..."

                    "Queria ter 10 por cento do que essa menina deve ter no banco..."

        "Tadaima" if tempo < 3:

            mc normal "A gente podia comer naquele restaurante japonês que tem perto do parque."

            c "Excelente ideia!"

            mc "A gente se encontra em uma hora?"

            c "Pra mim tá perfeito."

            mc "Ok. Beijos."

            c "Beijão!"

            scene black with Dissolve(1.0)

            $ nandom = renpy.random.randint(1,2)

            if nandom == 1:

                if tempo == 1:

                    scene tadaima restaurante with Dissolve(1.0)

                    mc feliz "Eu acho o Tadaima muito massa."

                    show priscila impressionada with dissolve

                    c "Este lugar é muito lindo."

                    c "Parece que eu fui pro oriente mesmo..."

                    mc normal "..."

                    mc "Vamos pedir alguma coisa?"

                    show priscila feliz with dissolve

                    c "Vamos."

                    c "Ah! Acho que a Karli trabalha aqui de manhã. É minha amiga."

                    show priscila feliz at direita with move

                    show karli kimono at entra_esquerda with dissolve

                    "Karli" "Oi, [c]!"

                    c "Oi, Karli! Pode trazer alguma coisa pra gente beber?"

                    "Karli" "Claro. Volto já."

                    hide karli with dissolve

                    show priscila feliz at centro with move

                    c "Enquanto a gente espera..."

                elif tempo == 2:

                    scene tadaima restaurante with Dissolve(1.0)

                    "Toda vez que eu venho aqui eu tenho um gelo na barriga..."

                    show priscila incerta with dissolve

                    c "O que foi, [mc]?"

                    mc envergonhado "Não é nada não..."

                    "Não é hora de ficar pensando em economizar dinheiro."

                    mc normal "Eu só ainda fico meio bobo de pensar que tô saindo com uma garota linda que nem você."

                    c "Para de tentar me conquistar..."

                    mc desculpa "Mas é sério..."

                    c "Para de ser bobo. Você é muito bacana, charmoso e eu te acho gatinho também."

                    mc envergonhado "..."

                    c "..."

                    mc normal "Ok. Vou pedir alguma coisa pra gente."

                    show priscila feliz with dissolve

                    c "Legal!"

                    c "Enquanto a bebida não chega."

            elif nandom == 2:

                scene tadaima vip with Dissolve(1.0)

                c "..."

                show priscila d_surpresa with dissolve

                c "..."

                mc desconfiado "Que foi?"

                c "Esse lugar parece tão exclusivo..."

                mc feliz "Haha..."

                show priscila d_brava with dissolve

                c "Que que foi?"

                mc normal "Acho interessante você ficar impressionada assim sendo que você deve visitar vários lugares muito mais chiques."

                show priscila d_preocupada with dissolve

                c "Me deixa..."

                mc "..."

                c "As coisas são diferentes quando a gente tá acompanhada com alguém que a gente gosta..."

                mc desculpa "..."

                mc charmoso "Eu imagino que minha companhia deva ser o maior destaque mesmo."

                c "Não vamos exagerar."

                show priscila d_hehe with dissolve

                "..."

        "Templo" if not sayuri_evento1_check:

            mc normal "Hoje quero te levar em um lugar muito especial."

            c "Sério? Onde?!"

            mc charmoso "No templo chinês."

            c "Eita! Se você acha que vai ser legal, ok."

            mc normal "Vai ser um lugar bem diferente."

            mc "A gente precisa pegar o busão até a Cidade Chinesa e de lá precisamos andar 10 quilômetros de uma montanha."

            c "O-ok..."

            mc "Eu te espero na frente do seu prédio, tá?"

            c "Certo. Me dá só uma meia hora."

            mc "Fechado. Até daqui a pouco."

            c "Até."

            scene black with Dissolve(1.0)

            $ nandom = renpy.random.randint(1,2)

            if nandom == 1:

                scene chinatown geral with dissolve

                c "{i}puf puf{/i}"

                show priscila cansada with dissolve

                c "Não tô aguentando mais, [mc]..."

                mc concentrando "Pior é que eu não tô também..."

                mc "Tô achando que eu fiz a gente descer no ponto errado. Não lembro de ter andado tudo isso da outra vez..."

                show priscila impressionada with dissolve

                c "Olha! Tem uma barraquinha de alguma coisa pra comer ali."

                c "O que acha da gente comer algo e voltar?"

                mc "Também acho a melhor coisa..."

                show priscila feliz with dissolve

                c "Só que antes. Temos que fazer o que a gente sempre faz nos encontros."

            elif nandom == 2:

                scene templo normal with dissolve

                "[mc] e [c]" "{i}puf puf{/i}"

                show priscila chorando with dissolve

                c "Nem acredito que conseguimos..."

                mc concentrando "Meu Deus... Parabéns pra gente..."

                c "A gente merece mesmo."

                show priscila impressionada with dissolve

                c "UoOoU!"

                mc normal "Sua reação foi exatamente igual a minha..."

                c "Puxa, que lugar bacana!"

                mc "Valeu a pena ter vindo?"

                show priscila feliz with dissolve

                c "Com certeza!"

                c "Eu nunca tinha visto algo assim na vida."

                mc charmoso "Que bom que você gostou."

    $ nandom = renpy.random.randint(1,2)

    $ proibido_salvar = True
    $ show_quick_menu = False

    python:
        if renpy.android:
            ep_pontos = PythonSDLActivity.pegaEPpontos()
            PythonSDLActivity.setEPtempoNext()

    if nandom == 1:

        c "E então? Pronto para continuar nosso jogo?"

        mc charmoso "Com certeza."

        c "O que você vai querer hoje? Perguntar alguma coisa sobre mim ou responder uma pergunta minha?"
    else:


        mc normal "Eu quero continuar com nosso jogo de acertar tudo sobre você."

        c "Eu adoro essa nossa brincadeira."

        c "O que você vai querer dessa vez? Quer que fale algo sobre mim ou quer tentar advinhar algo?"

    if ep_pontos == 10:

        c "Não! Pera..."

        c "Você conseguiu! Você já acertou tudo!"



        jump priscila_encontro_final

    elif ep_pontos > 5:

        c "Uou! Você já acertou mais da metade das perguntas que eu pensei..."

        c "Você acertou... [ep_pontos] coisas."

        c "Tá indo bem."

        mc normal "Valeu."

    elif ep_pontos <= 5:

        c "Você acertou [ep_pontos] coisas sobre mim até agora. Ainda falta um bocadinho, hein?"

        mc charmoso "Não tem problema. Não vou desistir."

        c "Assim que se fala."

    c "E então? O que você vai querer hoje?"

    menu:
        "Quero que você fale algo sobre você.":


            jump encontro_priscila_informacao
        "Quero que você me faça uma pergunta.":


            c "Combinado!"

            c "Tenho que pensar uma coisa que você ainda não acertou..."

            jump encontro_priscila_pergunta_pre

    label encontro_priscila_pergunta_pre:

        $ renpy.block_rollback()

        python:
            if renpy.android:
                ep_p_1 = PythonSDLActivity.pegaEPp1()
                ep_p_2 = PythonSDLActivity.pegaEPp2()
                ep_p_3 = PythonSDLActivity.pegaEPp3()
                ep_p_4 = PythonSDLActivity.pegaEPp4()
                ep_p_5 = PythonSDLActivity.pegaEPp5()
                ep_p_6 = PythonSDLActivity.pegaEPp6()
                ep_p_7 = PythonSDLActivity.pegaEPp7()
                ep_p_8 = PythonSDLActivity.pegaEPp8()
                ep_p_9 = PythonSDLActivity.pegaEPp9()
                ep_p_10 = PythonSDLActivity.pegaEPp10()

        jump encontro_priscila_pergunta

    label encontro_priscila_pergunta:

        $ pe_p_max = 10

        $ pe_num = renpy.random.randint(1,pe_p_max)

        if pe_num == 1:

            if not ep_p_1:

                c "Certo..."

                c "Hoje eu quero saber se você sabe quantos anos eu tenho."

                mc serio "Quantos... Eu acho que..."

                menu:
                    "19 anos":


                        jump encontro_priscila_acertou
                    "20 anos":


                        jump encontro_priscila_errou
                    "21 anos":


                        jump encontro_priscila_errou
                    "24 anos":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 2:

            if not ep_p_2:

                c "Hoje vou te perguntar..."

                c "Qual é minha comida preferida?"

                mc normal "O que será que você mais gosta de comer?"

                menu:
                    "Bolo de chocolate":


                        jump encontro_priscila_errou
                    "Uma saladinha":


                        jump encontro_priscila_errou
                    "Fast food":


                        jump encontro_priscila_errou
                    "Pizza":


                        jump encontro_priscila_acertou
            else:


                jump encontro_priscila_pergunta


        elif pe_num == 3:

            if not ep_p_3:

                c "Essa aqui você não pode errar de jeito nenhum, hein?"

                c "Qual é meu nome completo?"

                mc surpreso "Seu nome?!"

                mc desculpa "É..."

                menu:
                    "Priscila Fontanela":


                        $ renpy.block_rollback()

                        c "Sério, mesmo?! Meu nome?!"

                        jump encontro_priscila_errou
                    "Priscila Isabelli":


                        $ renpy.block_rollback()

                        c "Sério, mesmo?! Meu nome?!"

                        jump encontro_priscila_errou
                    "Priscila Fontinelli":


                        jump encontro_priscila_acertou
                    "Priscila Fondarelli":


                        $ renpy.block_rollback()

                        c "Sério, mesmo?! Meu nome?!"

                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 4:

            if not ep_p_4:

                c "O que você acha de me falar..."

                c "O dia e o mês em que eu nasci."

                mc normal "Hmmm..."

                menu:
                    "4 de abril":


                        jump encontro_priscila_errou
                    "15 de julho":


                        jump encontro_priscila_acertou
                    "9 de junho":


                        jump encontro_priscila_errou
                    "13 de setembro":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 5:

            if not ep_p_5:

                c "Você acredita na influência dos signos?"

                mc desconfiado "Sei lá..."

                c "Eu acredito muito neles."

                mc normal "Certo."

                c "Então quero que você saiba meu signo. Você sabe?"

                menu:
                    "Câncer":


                        jump encontro_priscila_acertou
                    "Escorpião":


                        jump encontro_priscila_errou
                    "Peixes":


                        jump encontro_priscila_errou
                    "Gêmeos":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 6:

            if not ep_p_6:

                c "Você lembra quando eu te disse que eu pedir meu BV?"

                mc desconfiado "Até isso eu tenho que saber?"

                c "Claro! A brincadeira é pra você saber tudinho sobre mim."

                mc normal "Ok. Vou acertar."

                mc "Você estava com..."

                menu:
                    "11 anos":


                        jump encontro_priscila_errou
                    "16 anos":


                        jump encontro_priscila_errou
                    "18 anos":


                        jump encontro_priscila_errou
                    "14 anos":


                        jump encontro_priscila_acertou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 7:

            if not ep_p_7:

                c "Eu adoro animais."

                mc normal "Eu também!"

                c "Que bacana! Eles são muito fofurinhas. Mas você sabe se eu tenho um de estimação?"

                "Hmmm... Ela viaja bastante. Não saberia responder..."

                c "Se eu tiver, quero que você me fale qual é."

                menu:
                    "Não tem animal de estimação":


                        jump encontro_priscila_errou
                    "Um gato":


                        jump encontro_priscila_errou
                    "Um cachorro":


                        jump encontro_priscila_acertou
                    "Um aquário com peixinhos":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 8:

            if not ep_p_8:

                c "Hoje vou ter perguntar uma coisa bem tonta."

                c "Qual é minha cor preferida?"

                mc desconfiado "Até isso?"

                c "Se quiser desistir..."

                mc serio "Não, não. Vou acertar tudo!"

                "Hmm... A cor preferida dela..."

                menu:
                    "Rosa":


                        jump encontro_priscila_errou
                    "Roxo":


                        jump encontro_priscila_acertou
                    "Verde":


                        jump encontro_priscila_errou
                    "Vermelho":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 9:

            if not ep_p_9:

                c "Vou fazer uma pergunta sobre o que eu gosto de fazer."

                mc charmoso "Além de falar comigo, é claro."

                c "Tá se achando muito."

                c "Quero que você me fale qual é meu filme preferido."

                mc concentrando "Seu filme preferido. Deixa eu pensar..."

                menu:
                    "Como perder um homem em 10 dias":


                        jump encontro_priscila_errou
                    "O diabo veste prada":


                        jump encontro_priscila_acertou
                    "Os normais: o filme":


                        jump encontro_priscila_errou
                    "Como se fosse a primeira vez":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        elif pe_num == 10:

            if not ep_p_10:

                c "Agora uma pergunta mais séria."

                c "Você acha que em questõe sociais, eu sou de direita ou de esquerda? Ou nenhum dos dois?"

                mc zerado "Certeza que quer falar de política?"

                c "Não é meu assunto preferido, mas você tem que saber tudo. Você não acha?"

                mc envergonhado "Acho que sim..."

                "Será que a [c] é de direita ou de esquerda? Mano, nem eu entendo isso direito..."

                menu:
                    "Esquerda":


                        jump encontro_priscila_acertou
                    "Direita":


                        jump encontro_priscila_errou
                    "Não se importa com política":


                        jump encontro_priscila_errou
            else:


                jump encontro_priscila_pergunta

        c "Certo! Então se prepara."

        c "Hmmm..."

        c "Pergunta..."

    label encontro_priscila_informacao:

        $ renpy.block_rollback()




        python:
            if renpy.android:
                PythonSDLActivity.setEPtempoNext()

        mc normal "Hoje eu vou querer que você me fale algo sobre você."

        c "Legal. E o que você quer saber hoje?"

        label ep_info:

            menu:
                "Qual é seu nome completo?":


                    $ renpy.block_rollback()

                    c "Sério mesmo, [mc]?"

                    mc envergonhado "Ué. Melhor garantir."

                    c "Ok. Meu nome é {b}[cc]{/b}."

                    mc normal "Eu já sabia. Era só pra confirmar absoluto absolutíssimo."

                    c "Tá certo, tá certo."

                    jump ep_info_depois
                "Quantos anos você tem?":


                    $ renpy.block_rollback()

                    c "Eu achei que isso seria fácil pra um paparazzo."

                    mc normal "Eu lembro de ter lido em algum lugar. Mas é melhor garantir."

                    c "Tem razão. Eu tenho {b}19 anos{/b}."

                    mc "Você ainda é novinha."

                    c "Falou o idoso..."

                    mc zerado "..."

                    jump ep_info_depois
                "Qual sua comida preferida?":


                    $ renpy.block_rollback()

                    c "Minha comida preferida?"

                    mc normal "Deve ser algo bem light pra você manter esse seu corpo."

                    c "Na verdade é {b}pizza{/b}."

                    mc surpreso "Quê!?"

                    c "Pois é. Eu não resisto à pizza... Falar disso já tá me deixando com fome."

                    c "Vamos pedir alguma coisa?"

                    mc normal "Ok..."

                    jump ep_info_depois
                "Quando você nasceu?":


                    $ renpy.block_rollback()

                    c "Eu nasci no dia {b}15 de julho{/b}. E esse não é um dia normal."

                    mc normal "Não? Por quê?"

                    c "É quando se comemora o Dia do Homem."

                    c "Irônico, não é? Uma garota nascer no Dia do Homem."

                    mc "É. Paradoxal."

                    jump ep_info_depois
                "Qual é seu signo?":


                    $ renpy.block_rollback()

                    c "Meu signo é um dos mais problemáticos."

                    c "Eu sou de {b}Câncer{/b}."

                    c "A gente é meio sentimental, mas gostamos de forma muito intensa dos nossos amigos."

                    mc normal "Você é uma pessoa muito bacana mesmo."

                    jump ep_info_depois
                "Nenhuma destas acima":


                    jump ep_info_dois

        label ep_info_dois:

            menu:
                "Com quantos anos você deu seu primeiro beijo?":


                    $ renpy.block_rollback()

                    c "Você acha que isso é coisa que se pergunte?"

                    mc normal "Se você quer que eu saiba tudo sobre você, tenho que saber essas coisas também."

                    c "Tem razão. Eu dei meu primeiro beijo com {b}14 anos{/b}. Era um rapazinho lá da escola."

                    mc "Meio tarde até."

                    c "E quando foi o seu?"

                    mc "Segredo."

                    c "..."

                    jump ep_info_depois
                "Você tem animal de estimação?":


                    $ renpy.block_rollback()

                    c "Sim! Eu tenho!"

                    c "Infelizmente eu não posso ver ele muito por que tô sempre viajando. Mas sempre que dá passo em casa pra ver ele."

                    c "É um {b}cachorrinho{/b}!"

                    mc normal "Que gracinha..."

                    jump ep_info_depois
                "Qual é sua cor preferida?":


                    $ renpy.block_rollback()

                    c "É a cor da roupa que eu tava usando quando a gente se viu pela primeira vez no bar."

                    mc desconfiado "Que era..."

                    c "Já esqueceu qual era a roupa?"

                    mc desculpa "Desculpa..."

                    c "Tudo bem, [mc]. Minha cor preferida é o {b}Roxo{/b}."

                    mc normal "Mais uma coisa que eu sei sobre você."

                    c "Verdade. Só não vai esquecer."

                    jump ep_info_depois
                "E o seu filme preferido?":


                    $ renpy.block_rollback()

                    c "Meu filme preferido? Você não vai acreditar."

                    mc normal "É uma comédia romântica bem tontinha eu aposto."

                    c "Não. É o filme {b}O Diabo Veste Prada{/b}."

                    mc desconfiado "Eita..."

                    c "Pois é. Um dia eu ainda te explico o porquê."

                    mc normal "Combinado."

                    jump ep_info_depois
                "Nenhuma destas acima":


                    jump ep_info

        jump encontro_priscila_encerrar

    label ep_info_depois:

        c "E hoje é só isso que eu vou te contar."

        mc preocupado "Mas..."

        c "Uma pergunta por dia. E não esquece de anotar em algum lugar pra não ter que perguntar a mesma."

        mc normal "Ok."

        c "E agora eu tô afim de beber alguma coisa."

        mc "Fechou."

        jump encontro_priscila_encerrar

    label encontro_priscila_acertou:

        $ renpy.block_rollback()

        if pe_num == 1:

            c "Isso mesmo! Eu tenho 19 anos."

            c "Mas essa era fácil também, hein?"

            mc normal "Não importa. Acerto é acerto."

            c "Tem razão."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp1()
                    PythonSDLActivity.ganhaEPpontos()
                    PythonSDLActivity.setEPtempoNext()

        elif pe_num == 2:

            c "Acertou! O que eu mais gosto é de pizza!"

            c "Não imaginei que você ia saber essa."

            mc desconfiado "Só não sei como você mantém esse corpo assim..."

            c "Muita malhação e água!"

            mc normal "Bom saber."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp2()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 3:

            c "Ufa! Se errasse essa hein..."

            mc envergonhado "Pois é..."

            "Graças a Deus eu acertei essa."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp3()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 4:

            c "Que bom que você lembrou!"

            mc normal "Hehe. Claro que eu ia lembrar."

            c "Fico muito feliz, [mc]."

            mc "Eu realmente me importo quando o assunto é você."

            c "Ah, seu xavequeiro..."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp4()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 5:

            c "Isso mesmo! Eu sou de câncer."

            mc normal "Que bacana."

            c "As câncerianas são garotas mais fechadas e emotivas, mas a gente tem muito carinho."

            mc tarado "..."

            c "Ei! Não pense em besteira!"

            mc charmoso "Tô brincando. Você realmente é uma pessoa muito carinhosa."

            c "Obrigada!"

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp5()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 6:

            c "Certinho."

            mc tarado "Sou foda!"

            c "Falou em safadeza você lembra, né?"

            mc envergonhado "Nada a ver... Eu acerto todas igualzinho."

            c "Vamos ver. Vou ficar de olho."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp6()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 7:

            c "Au-au! Acertou em cheio!"

            mc normal "Que legal. E como é o nome dele?"

            c "Ele é um vira-lata chamado Toby."

            mc normal "Deve ser uma gracinha."

            c "Olha aqui uma foto dele..."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp7()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 8:

            c "Ding-ding!"

            c "Eu sei que essa foi bobeira, mas eu queria que você soubesse mesmo assim."

            mc normal "Não se preocupe com isso. Nosso jogo é justamente pra essas coisas bobas também."

            c "Obrigada, [mc]."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp8()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 9:

            c "Exatamente. O Diabo Veste Prada!"

            mc desconfiado "Mas eu pensei que seus filmes preferidos fossem comédias românticas..."

            c "E são. Só que faz um tempo minha agente pediu para eu assistir esse filme porque eu tava pensando muita asneira."

            c "E desde que eu assisti virou meu filme preferido, mesmo não sendo comédia romântica."

            mc normal "Interessante..."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp9()
                    PythonSDLActivity.ganhaEPpontos()


        elif pe_num == 10:

            c "Então... não que eu saiba muito sobre esses assuntos."

            mc envergonhado "Eu também não manjo muito."

            c "Mas pelo que eu leio, a esquerda defende mais os direitos dos gays, dos indígenas e das minorias."

            c "E eu me identifico mais com isso. Eu queria que essas pessoas tivessem mais ajuda do governo."

            mc normal "Sei lá. Mas você não tem medo desse negócio de comunismo?"

            c "Não sei também. Eu nunca li nada sobre comunismo hehe..."

            mc concentrando "Pra falar a verdade eu também não. A gente só vê coisa na internet de vez em quando."

            c "Verdade."

            mc normal "Eu nunca pensei muito nisso. Talvez eu devesse ler melhor antes de tomar um lado."

            c "Sei lá se a gente devia pensar nisso também como uma luta de um contra o outro."

            c "Mas desculpa por deixar a conversa assim muito séria."

            mc normal "Relaxa. Falar sobre outras coisas de vez em quando não vai matar ninguém."

            python:
                if renpy.android:
                    PythonSDLActivity.acertaEPp10()
                    PythonSDLActivity.ganhaEPpontos()


        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("encontro_priscila","priscila","personagem")
                ep_pontos = PythonSDLActivity.pegaEPpontos()

        $ renpy.block_rollback()

        jump encontro_priscila_encerrar

    label encontro_priscila_errou:

        python:
            if renpy.android:
                PythonSDLActivity.setEPtempoNext()

        $ renpy.block_rollback()

        $ ep_enum = renpy.random.randint(1,5)

        if ep_enum == 1:

            c "Haha! Quase lá, [mc]!"

            c "Quem sabe na próxima, né?"

            mc preocupado "Eu achei que ia acertar essa..."

            c "Não fique assim. Essa é a graça do jogo!"

        elif ep_enum == 2:

            c "Nada disso, [mc]!"

            c "Sinceramente, pensei que você fosse acertar essa, bobinho."

            mc zerado "Também achei..."

            c "Hehe, não faça essa cara de peixe morto. É pra isso que o jogo serve!"

            mc concentrando "Ok... A próxima vou acertar."

            c "Tenho certeza que sim!"

            c "E não esqueça de me perguntar o que você ainda não souber ou não lembrar."

            mc normal "Verdade. Vou te perguntar."

        elif ep_enum == 3:

            c "Errrrrrou!"

            mc serio "Droga!"

            c "Calma, [mc]!"

            mc envergonhado "Desulpa... É que essa tava na ponta da língua."

            c "Eu entendo. Mas não fique assim! Eu acho divertido quando você erra também."

            mc desconfiado "Por quê?"

            c "Porque assim a gente pode continuar brincando..."

            mc feliz "Você é muito bonitinha, [c]..."

            c "Não fale assim!"

            c "..."

        elif ep_enum == 4:

            c "Na-na-ni-na-neca."

            mc concentrando "Errei..."

            c "Mas foi perto."

            c "Você está lembrando de anotar em algum lugar o que eu te falo?"

            c "Assim depois você pode colar."

            mc normal "E eu posso colar?"

            c "Não. Mas eu posso fingir que não tô vendo..."

            mc normal "Você é muito linda."

            c "Obrigada. Não é fácil ser linda desse jeito, mesmo."

            mc feliz "..."
        else:


            c "Raspando! Mas não..."

            mc desculpa "Que merda..."

            c "Mas você tá muito perto de conseguir! Não quero que desista!"

            mc charmoso "Pode ter certeza que não vou desistir."

            c "Que bom! Só não vale olhar na internet, hein?"

            mc desconfiado "Olhar o quê?"

            c "Não sei por que eu disse isso..."

            c "..."

        jump encontro_priscila_encerrar

    label encontro_priscila_encerrar:

        $ proibido_salvar = False
        $ show_quick_menu = True
        $ dia_priscila = dia + 1

        show black with Dissolve(1.0)

        "{b}Depois de mais um tempo conversando, o encontro chega ao fim{/b}"

        $ tempo += 1

        hide black with Dissolve(1.0)

        c "Gostei muito do nosso passeio, hoje."

        mc feliz "Eu também curti."

        c "Vou estar ansiosa esperando você me chamar de novo!"

        mc normal "Pode deixar. Logo eu ligo, ok?"

        scene black with Dissolve(1.0)

        $ renpy.block_rollback()

        c "Até outra hora, [mc]! Beijão!"

        mc "Beijos, [c]."

        jump call_cidade

label priscila_encontro_final:

    $ proibido_salvar = False
    $ show_quick_menu = True

    if not priscila_ef_check:

        $ priscila_ef_check = True

        c "Acho que você sabe mais sobre mim do que minha mãe!"

        mc charmoso "Eu disse que eu ia conseguir..."

        c "Acho que tá na hora da sua recompensa."

        mc surpreso "..."

        c "Vamos lá no meu quarto no hotel e eu te conto o que é."

        mc surpreso "..."

        c "Não precisa ter um treco, [mc]..."

        scene black with Dissolve(1.0)

        if tempo < 3:

            scene parque dia with Dissolve(1.0)
        else:


            scene parque noite with Dissolve(1.0)

        "Caraca... Tamo indo no ap dela. Só nós dois..."

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_encontro_final","priscila","personagem")

        "..."

        scene hotel recepcao with Dissolve(1.0)

        "O que será que é minha surpresa? Mano, que nervoso só de pensar."

        c "..."

        "Ela não fala nada. Será que ela tá nervosa também?"

        "..."

        c "Chegamos."

        scene hotel loft with Dissolve(3.0)

        mc normal "Uou. Que lugar bacana."

        c "Pode sentar e ficar à vontade que eu vou preparar sua surpresa e já volto."

        mc preocupado "Ai..."

        c "Não precisa ficar nervoso, [mc]. Tenho certeza que você vai gostar muito."

        mc envergonhado "Ok..."

        "..."

        c "Estou quase pronta. Pode fechar os olhos?"

        scene black with dissolve

        mc concentrando "Sim."

        mc "Estão fechados."

        "..."

        c "Certo. Agora segue minha voz. Vem aqui."

        mc "Ok... Estou indo..."

        c "Dá aqui sua mão. Vem, vem. Agora fica aqui."

        mc "Certo."

        c "Agora pode abrir e olhar pra frente."

        scene priscila e_pose1 with Dissolve(2.0)

        pause

        mc surpreso "..."

        mc "Tu tá linda!"

        c "Obrigada. Todo mundo adora quando eu uso essa roupa."

        c "E pela primeira vez tô usando longe das câmeras, só pra você."

        mc charmoso "Obrigado, [c]. Eu realmente achei muito especial."

        c "Não achou nada que ainda não acabou. Pode fechar o olho de novo que tenho mais uma pose pra você."

        mc surpreso "..."

        c "Tá. Pode fechar os olhos e a boca também, bobinho."

        scene black with dissolve

        mc concentrando "Pronto."

        c "Deixa eu pensar numa pose. Ok. Esta você vai gostar mais."

        mc "{i}gulp{/i}"

        c "Ok. Pode abrir."

        scene priscila e_pose2 with Dissolve(2.0)

        pause

        mc surpreso "..."

        c "O que achou deste ângulo?"

        menu:
            "Você tá linda.":


                mc surpreso "Você tá linda!"

                c "Eu sabia que você ia gostar. Esta roupa encanta qualquer um que vê."

                mc "Com certeza!"
            "Muito gostosa.":


                mc safado "Muito gostosa..."

                c "Ai, [mc]. Não precisa me comer com os olhos também..."

                mc "Não tá fácil."
            "Você é muito fofa.":


                mc normal "Você é muito fofa mesmo."

                c "Obrigada, [mc]."

        c "Já que você foi gentil comigo, vou fazer uma pose especial extra."

        c "Pode..."

        scene black with dissolve

        mc concentrando "Já fechei."

        c "Rsrs... Tá ansioso, é?"

        mc "Com certeza."

        c "Tá. Vou me ajeitar aqui. Só um segundinho."

        "..."

        c "Ok. Tô pronta."

        c "Essa aqui vai ser sua preferida, tenho certeza."

        c "Pode olhar."

        scene priscila e_pose3 with Dissolve(2.0)

        pause

        mc charmoso "Que que é isso... Que visão..."

        mc "Você é incrível, [c]."

        c "E é só pra você."

        if p3_confissao:

            c "Pra você que é meu verdadeiro amigo."

            c "Alguém que me ouviu e com quem eu pude contar."

            if priscila_e3_beijo:

                scene hotel loft with Dissolve(1.0)

                show priscila e_feliz with dissolve

                c "E mais do que isso. Que é mais do que um amigo pra mim."

                c "Aquele nosso beijo na praia..."

                c "Acho que foi o momento mais feliz da minha vida."
        else:


            scene hotel loft with Dissolve(1.0)

            show priscila e_feliz with dissolve

        c "Você teve paciência e descobriu tudo sobre mim. Isso é algo que eu nunca vou esquecer, [mc]."

        c "Não pode ter mais prova de que você gosta de mim. Tanto esforço nessa brincadeirinha boba."

        mc charmoso "Não achei nada bobo. Achei muito especial conhecer você melhor."

        if priscila_e3_beijo:

            mc "E eu também não consigo esquecer nosso beijo na praia."

            mc "O que você acha de você sentar comigo, aqui? Vem cá."

            c "Ok..."

            hide priscila with dissolve

            mc "Você sabe que eu gosto demais de você."

            c "Eu também."

            mc "Mas só falar não adianta. Deixa eu mostrar pra você."

            c "Ai, [mc]..."

            "..."

            scene priscila e_beijo with Dissolve(3.0)

            pause

            c "Hmmm..."

            mc "..."

            "Uma garota tão linda, incrível e especial, aceitando me beijar assim. Eu sou um cara de muita sorte..."

            "Quero proteger ela de tudo e ser um cara que mereça realmente ficar com ela."

            window hide

            pause

            scene hotel loft with Dissolve(1.0)

            c "Você sabe como me deixar zonza, [mc]..."

            mc charmoso "Você também me deixa assim."

            show priscila e_feliz with dissolve

        c "Eu adorei cada segundo do nosso jogo. O que você achou do seu prêmio?"

        mc normal "Eu adorei demais."

        c "Obrigada por tudo."

        mc normal "Não tem o que agradecer. Eu curti muito."

        c "Ok. Agora vou ter que me aprontar pra mais um ensaio. Você me liga depois?"

        mc charmoso "Com certeza. Bom trabalho."

        c "Beijos!"

        mc "Beijão."

        $ tempo += 1

        jump call_cidade
    else:


        c "Você vai querer seu prêmio novamente? A gente pode ir no meu apartamento e eu poso pra você outra vez."

        c "Eu adoro! E você vai poder me ver gatinha de novo!"

        mc charmoso "Em todos os sentidos."

        menu:
            "Sim. Quero ver de novo.":


                c "Vamos lá pro quarto do meu hotel então."

                mc charmoso "Combinado."

                scene black with Dissolve(3.0)

                scene hotel loft with Dissolve(1.0)

                c "Vou me trocar. Pode fechar os olhos."

                scene black with dissolve

                mc concentrando "Pronto."

                c "Agora pode abrir."

                scene priscila e_pose1 with Dissolve(2.0)

                pause

                scene black with dissolve

                scene priscila e_pose2 with Dissolve(2.0)

                pause

                scene black with dissolve

                scene priscila e_pose3 with Dissolve(2.0)

                pause

                scene hotel loft with Dissolve(1.0)

                show priscila e_feliz with dissolve

                c "Eu adoro posar pra você, [mc]. Sempre que quiser é só falar, tá?"

                mc charmoso "Com certeza."

                c "Até a próxima. Beijããooo!!"

                mc "Beijos, [c]."

                $ tempo += 1

                jump call_cidade
            "Não. Vamos deixar pra uma outra hora.":


                c "Ok."

                jump encontro_priscila_encerrar

label priscila_encontro_1vez:

    mc charmoso "O que você acha da gente ir no bar, que é onde a gente conversou pela primeira vez?"

    c "A primeira vez que a gente conversou foi na redação!"

    if orelha_porta:

        c "Você tava paradão lá e eu trombei em você enquanto gritava com seu chefe."

    mc envergonhado "Verdade. Voce até me chamou de gato..."

    c "Quem diria que a gente ia se conhecer assim..."

    mc charmoso "É verdade."

    c "Mas não dá pra gente sair na redação da sua revista, então o bar tá excelente pra mim!"

    mc normal "Combinado. Em meia hora então?"

    c "Ok. Te encontro lá. Beijo!"

    mc "Beijo."

    scene black with Dissolve(1.0)

    "..."

    scene pub geral with Dissolve(1.0)

    "Cheguei antes dela. Isso é sempre bom."

    "..."

    "Opa! Aí vem ela."

    show priscila feliz with dissolve

    c "Oi, [mc]! Demorei muito?"

    mc normal "Oi. Não. Acabei de chegar."

    c "Que bom."

    mc "Vamos sentar?"

    c "Vamos."

    scene pub booth with Dissolve(1.0)

    c "Esse lugar me traz lembranças..."

    mc "Pra mim também..."

    if priscila_e1 == "seducao":

        show priscila seduzida with dissolve

        c "Eu tenho vergonha só de lembrar..."

        mc charmoso "Eu realmente gostei bastante daquele encontro."

        c "Claro que você gostou... E... eu gostei também..."

        mc tarado "..."

    elif priscila_e1 == "amizade":

        show priscila incerta with dissolve

        c "Eu fui muito esquisita aquela noite, não fui?"

        mc normal "Esquisita?"

        c "Sim... aquele negócio de teste e depois deitei no seu colo..."

        mc charmoso "Não esquente com isso."

        c "Você foi muito bacana comigo aquela noite."

        mc "Não foi nada de mais. Eu gostei muito de poder estar com você."

        c "Obrigada..."

    mc normal "Faz tempo que eu queria te chamar pra sair."

    show priscila feliz with dissolve

    c "Verdade?"

    mc "Sim. Eu queria passar mais tempo com você. Conhecer você melhor."

    c "Ounnn... Você é um fofo, [mc]."

    c "Ah! O que você acha da gente fazer uma brincadeira então nos nossos encontros?"

    mc desconfiado "Brincadeira?"

    c "Sim. Tipo um jogo. Pra gente se conhecer melhor."

    mc normal "O que você tá pensando?"

    c "Assim. Você quer sair comigo mais vezes pra me conhecer melhor, não quer?"

    mc "Isso."

    show priscila preocupada with dissolve

    c "Então... em todo encontro eu vou deixar você escolher entre duas opções."

    c "Se você quer que eu diga alguma coisa sobre mim pra você me conhecer melhor."

    c "Ou se você quer responder uma pergunta sobre mim."

    c "Tá parecendo bobo demais?"

    menu:
        "Sim. É meio bobo...":


            mc envergonhado "Parece meio coisa de criança..."

            show priscila impressionada with dissolve

            c "Sé-sério?!"

            c "A gente não precisa..."

            mc normal "Mas eu não sou contra. Acho que é uma boa ideia. Vai deixar nossos encontros mais interessantes."

            show priscila preocupada with dissolve

            c "Tem certeza?"

            mc "Sim, pode ficar tranquila."

            c "Ok..."
        "Claro que não. Tô achando interessante.":


            mc "Relaxa. Tô achando interessante por enquanto."

            show priscila incerta with dissolve

            c "Que bom."

            c "Estava com medo que você achasse bobo demais."

    c "Então..."

    show priscila feliz with dissolve

    c "Se você conseguir responder 10 perguntas sobre mim é porque daí você me conhece de verdade."

    c "O que você acha?"

    mc surpreso "Responder 10 perguntas?!"

    c "Sim. Você vai ter que advinhar minha cor preferida, minha comida preferida, o dia em que eu nasci e um monte de coisas sobre mim!"

    mc "..."

    show priscila provocando with dissolve

    c "Acha que consegue?"

    menu:
        "Claro que eu consigo.":


            mc charmoso "Claro que eu vou conseguir. Pode apostar que eu vou saber tudo sobre você."

            c "Vamos ver..."
        "Vamos ver...":


            mc preocupado "Vamos ver se eu consigo..."

            c "Já tá desistindo antes de começar?"

            mc "..."

    c "E se você conseguir acertar tudo eu vou ter uma surpresa pra você no final!"

    mc charmoso "Opa! Que surpresa?"

    c "Não posso falar agora..."

    c "Mas eu acho que você vai gostar muito!"

    mc surpreso "Combinado!"

    show priscila cansada with dissolve

    c "Mas por hoje tá bom. Na próxima vez a gente começa, tudo bem?"

    mc normal "Combinado."

    c "Quero tomar alguma coisa bem gelada. Você me acompanha?"

    mc "Claro. Deixa eu chamar o [gar]."

    scene black with Dissolve(1.0)

    gar "Senhor [mc]! Senhorita [c]! Que alegria inigualável vê-los juntos neste dia de imensurável amor e paixão!"

    mc zerado "..."

    "{b}Depois de alguns drinks gelados e de uma conversa improdutiva com o [gar], [mc] e [c] terminaram o encontro e se despediram{/b}"

    "..."

    p rindo "Oi! Olha eu de novo!"

    p lecionando "Para começar seus encontros com a [c] e advinhar 10 coisas sobre ela é só apertar no celular quando você estiver no centro da ilha."

    p "Só que existe um tempo que você tem que esperar entre um encontro e outro."

    p "Mais especificamente, você precisa esperar {b}12 horas da vida real{/b} antes dela aceitar o próximo encontro com você."

    p rindo "Não esqueça de voltar ao game a cada 12 horas e terminar sua brincadeira com ela para ver a surpresa que ela tem para você!"

    p "Bom game!"

    $ dia_priscila = dia + 1
    $ persistent.priscila_encontro_1vez = False

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("priscila_encontro_1vez","priscila","personagem")
            PythonSDLActivity.setEPtempoNext()

    $ renpy.block_rollback()

    jump call_cidade

label encontro_priscila_tutorial:

    p rindo "Oi, bonitinho! É a [p] de novo para te ensinar algo bacana sobre o game."

    p "A partir de agora você poderá chamar a [c] para sair. Vocês podem ter encontros em vários lugares da ilha."

    p lecionando "É só apertar abrir o celular, ali do lado da data, e escolher a opção {b}Telefone{/b} e depois o botão da [c]."

    p "Você pode tanto passear com ela, como oferecer para fazer massagens, caso você já tenha começado o curso."

    p rindo "Ah! Para fazer esses conteúdos extras, você precisa estar conectado à internet, ok?"

    p rindo "Ela está doidinha para sair com você! Aproveite!"

    $ ep_tutorial = True

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
