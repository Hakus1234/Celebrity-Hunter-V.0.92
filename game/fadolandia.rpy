label fadolandia_m4sangue:

    hide screen fadolandia_tela

    if not fado_m4sangue:

        "O que isso aqui do lado da entrada da caverna?"

        "..."

    scene mapa4_sangue with Dissolve(2.0)

    pause

    if not fado_m4sangue:

        $ fado_m4sangue = True

        "Sangue?!"

        "É o que parece..."

        "O sangue tá super fresco. Como se tivesse acabado de escorrer."

        "Será que acabou de acontecer alguma coisa aqui na caverna?!"

        "Que merda..."

        "Esse sonho fica cada vez mais sinistro."

        "Todos esses lugares pra ir. E o jeito que parece que eu tenho consciência de tudo."

        "Na maioria dos sonhos que eu tenho eu nem percebo que eu tô sonhando..."

        "Como é possível que eu tenha tanta consciência assim do que tá acontecendo em um sonho?"

        "E como que eu me lembro de tudo quando tô aqui? Daí quando eu acordo eu esqueço o que sonhei..."

        "Acho que não adianta ficar pensando demais. Tenho que continuar."

        "Só que não tem nada pra eu fazer por esse lado agora. A caverna tampa o caminho. Deixa eu voltar."
    else:


        "O sangue continua aqui. Tão fresco quanto da outra vez que eu vi."

        "Como pode? Será que sangraram de novo no mesmo lugar?"

        "Loucura..."

        "Não tem nada pra eu fazer por aqui agora. Deixa eu voltar."

    jump fadolandia_m4a2

label fadolandia_m4caverna:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m4a3"

    hide screen fadolandia_tela

    if fado_precisa_maca:

        scene mapa4_area4 with Dissolve(2.0)

        pause

    play sound "audio/som_18_gotas.mp3"

    if not fado_precisa_maca:

        $ fado_precisa_maca = True

        scene black with Dissolve(2.0)

        "Aqui tá mesmo um breu total. Não tô enchergando é nada."

        "Mas não dá pra parar agora."

        "..."

        "Acho que meus olhos estão começando a se acostumar com a escuridão."

        scene mapa4_area4 with Dissolve(2.0)

        pause

        "Ufa. Tô enchergando alguma coisa pelo menos."

        "{i}Hic... sniff...{/i}"

        mc "Hâ?"

        "Tô escutando alguma coisa. Acho que tá vindo do interior."

        "..."

        "{i}Hic!{/i}"

        "Tô perto! Tá por aqui."

        "..."

        scene mapa4_pixel_chorando with Dissolve(2.0)

        pause

        "O que... uma menina? Asas? Cabelo rosa?"

        "Ela parece a Pi-"

        "Outra fada!!!"

        "{i}Sniff... hic... sniff...{/i}"

        "Ela tá chorando?"

        menu:
            "Oi... tudo bem?":


                $ pixel_amizade += 1

                mc "Oi... tudo bem com você?"

                f "Huh?"

                f "!"

                scene mapa4_pixel_assustada with Dissolve(1.0)

                pause

                f "..."
            "Ei! Tudo legal?!":


                mc "Ei! Aqui! Tudo legal?!"

                scene mapa4_pixel_assustada with vpunch

                f "!"

                mc "Calma! Calma!"

                f "..."

        mc "Você pode falar? Por que tava chorando?"

        f "..."

        f "Fome..."

        mc "Você tá com fome?"

        f "Fome..."

        mc "O que aconteceu com você? Você tá machucada?"

        f "Fome..."

        mc "Ok..."

        "Parece que não vou conseguir falar com ela enquanto não trouxer algo pra ela comer."

        "Mas como raios vou trazer alimento pra dentro de um sonho?"

        "Talvez... talvez eu possa encontrar comida DENTRO do sonho."

        if fado_m3a7:

            "Pera! O [fado] não tinha uma maçã com ele?!"

            show mapa3_fado_maca with dissolve

            "..."

            "Ele tava segurando ela."

            "Eu lembro daquela maçã..."

            hide mapa3_fado_maca with dissolve

            "Perfeito! Tomara que ele ainda tenha ela. Ou alguma outra maçã."
        else:


            "Meu sonho tem outros caminhos. Talvez eu devesse tentar ir pra outras áreas ver se encontro algo."

        "Depois de comer talvez ela possa falar mais sobre o que tá havendo."

        mc "Não se preocupe. Eu vou trazer comida pra você."

        f "Fome..."

        "..."

        mc "Até."

    elif fado_precisa_maca and not fado_pixel_comeu:

        "A fada tava por aqui..."

        "..."

        "Alí."

        scene mapa4_pixel_chorando with Dissolve(2.0)

        pause

        mc "Oi. Voltei."

        f "!"

        scene mapa4_pixel_assustada with Dissolve(2.0)

        pause

        f "Fome..."

        if fado_maca:

            $ fado_pixel_comeu = True

            mc "Eu trouxe uma maçã pra você. Toma."

            "..."

            scene mapa4_pixel_maca with Dissolve(2.0)

            pause

            f "..."

            f "{size=15}Posso comer?{/size}"

            mc "Claro. É pra você."

            f "{size=15}Obrigada.{/size}"

            f "{i}chomp chomp{/i}"

            f "{i}nom nom nom{/i}"

            "..."

            scene mapa4_pixel_assustada with Dissolve(2.0)

            f "{size=15}Obrigada mesmo.{/size}"

            mc "Tava boa?"

            f "Estava. Matou minha fome."

            mc "Que bom que você gostou."

            f "..."

            mc "Tudo bem?"

            f "Sim."

            mc "Posso me sentar do seu lado?"

            f "..."

            f "Tudo bem."

            "..."

            scene mapa4_pixel_mc with Dissolve(2.0)

            pause

            mc "Você tá legal? O que é esse machucado no seu rosto?"

            f "Foi ela que fez isso. Quando me baniu da vila."

            mc "Ela?"

            f "Sim. Quando aquela bruxa invadiu nossa terra, ela nos expulsou da vila e me machucou."

            f "Tive que correr para longe, ou ela ia acabar comigo. Então encontrei este lugar."

            mc "Isso parece horrível."

            f "Sim. E o pior é que não sei nada sobre minha irmã."

            mc "Irmã?!"

            f "Sim... mas não posso falar mais. Estou muito cansada."

            f "A maçã era tudo o que eu precisava. Obrigada, mas agora preciso descansar."

            mc "Tudo bem. Eu voltarei depois."

            mc "Você pode só me falar seu nome?"

            $ f_nome = "Pixel"

            f "Meu nome é [f]. Eu estou do seu lado há muito tempo."

            mc "Como assim?!"

            f "Outra hora..."

            mc "Tudo bem. Me perdoe. Até outra hora."

            f "Tudo bem. Bom dia, [mc]."

            scene mapa4_area4 with Dissolve(2.0)

            "..."

            "Como ela sabe meu nome? E como assim ela está do meu lado há muito tempo?"

            "Bom, depois eu pergunto pra ela."

            "Agora deixa eu acordar..."

            scene black with dissolve

            return
        else:


            "Não adianta eu voltar aqui enquanto eu não tiver algo pra ela comer."

            "Tenho que conseguir comida pra ela de qualquer jeito."

            mc "Logo eu trago algo pra você. Espera só mais um pouco."

            f "Fome..."

    elif fado_pixel_comeu and pixel_evento == 0:

        "No meu outro sonho eu ajudei a [f] e ela começou a falar comigo. Foi um grande avanço pra entender tudo isso."

        "Nunca que eu imaginei que iria encontrar outra fada além da [p]."

        "Ela parece tão sozinha e assustada. Preciso falar com ela de qualquer forma."

        "Talvez eu possa ajudar... E talvez ela possa me ajudar também hehe..."

        "Será que ela tá no mesmo lugar?"

        "..."

        "Pior que tá."

        scene mapa4_pixel_assustada with Dissolve(2.0)

        mc "Oi."

        f "Oi, [mc]. Tudo bem?"

        mc "Tudo."

        f "Vem aqui comigo."

        "..."

        scene mapa4_pixel_mc with Dissolve(2.0)

        pause

        mc "Tá tudo legal? O que foi?"

        f "Não é nada..."

        f "Você provavelmente tem várias perguntas pra mim."

        mc "Algumas, sim..."

        f "Vou tentar explicar tudo o que eu puder."

        label pixel_menu:

            menu:
                "O que você pode me falar sobre este lugar?":


                    mc "Eu queria saber mais sobre este lugar."

                    mc "Sei que é estranho, mas eu nunca tive um sonho onde eu tinha tanta consciência."

                    mc "E é também a primeira vez que eu tenho o mesmo sonho tantas vezes seguidas."

                    mc "Assim... Isto aqui é realmente um sonho meu?"

                    f "É e não é."

                    mc "Como assim?"

                    f "Não sei como explicar. Eu nunca expliquei isso para ninguém."

                    mc "Nenhum outro humano veio aqui?"

                    f "Não... Foi só depois que aquela maldita chegou que... Espera. Teve um outro humano, sim."

                    f "Foi logo que ela veio. Foi o primeiro. Eu vi ele algumas vezes antes dela me banir."

                    mc "O que aconteceu com ele?"

                    f "Ele se aproximou demais dela. Ele começou a vir várias e várias vezes, até que não vi mais ele."

                    mc "..."

                    f "Ele parecia ser inteligente. Ele conversou comigo algumas vezes. Mas ele se transformou."

                    f "Tome cuidado com ela, [mc]."

                    mc "Ok."

                    jump pixel_menu
                "O que você e sua irmã são, na verdade?":


                    mc "Desculpa se soar meio indelicado, mas... o que você e sua irmã são?"

                    f "Como assim o que eu sou?"

                    scene mapa4_pixel_mc2 with Dissolve(2.0)

                    f "Que pergunta besta, [mc] tehee..."

                    f "Eu sou sua {b}protetora{/b}, é claro. Minha irmã também."

                    mc "Quê?!"

                    f "Cada lugar chama a gente de uma forma: espírito protetor, anjo da guarda, consciência, energia interior..."

                    f "Somos nós que protegemos você das energias negativas e te ajudamos a tomar as melhores decisões para sua vida."

                    f "Nós moldamos sua energia e criamos seu campo de atração."

                    mc "..."

                    f "Não precisa fazer essa cara. Todas as pessoas têm um protetor. E não era para você saber da nossa existência."

                    f "Isso tudo tá acontecendo por causa dela. Da bruxa."

                    mc "..."

                    f "Que foi?"

                    mc "Isso tudo é demais pra mim..."

                    f "Você que perguntou."

                    mc "Pior é que é verdade..."

                    jump pixel_menu
                "Eu quero ajudar você a sair daqui.":


                    mc "Eu não quero que você continue triste aqui."

                    mc "Não importa o que eu tenha que fazer, eu vou tirar você daqui."

                    mc "E vou salvar sua irmã também."

                    scene mapa4_pixel_mc2 with Dissolve(2.0)

                    f "..."

                    f "Você faria isso pelas suas protetoras?"

                    mc "Claro."

                    f "Isso é muito legal de sua parte, [mc]."

                    f "Vamos descobrir como desfazer essa energia."

                    mc "Esse é o problema..."

                    f "Não seja ansioso. A maçã que você me deu vai durar muito tempo ainda. Nós fadas comemos muito pouco."

                    f "Eu vou pensar em alguma coisa e assim que tiver um plano eu te chamo e você vem."

                    mc "Ok. E pode ter certeza que vou tentar pensar em algo também."

                    f "A gente vai conseguir!"

                    jump pixel_menu
                "Não tenho mais perguntas.":


                    mc "Era isso que eu queria saber. Obrigado pela paciência."

        f "Você merece depois de tudo o que tá passando."

        f "Nada disso é normal. Não era para você ter estes sonhos e nem ter me visto."

        menu:
            "Entendo...":


                mc "Entendo..."

                f "..."
            "Mas eu gostei de te conhecer.":


                $ pixie_amizade += 1

                mc "Tem um lado bom... pelo menos eu conheci minha protetora [f]."

                f "Que fofo!"

                f "Eu nunca me preparei para conversar com meu protegido. Mas acho que estamos nos dando bem."

                mc "Estamos, sim."

        f "Assim que a gente acabar com a influência da bruxa, vai tudo voltar ao normal."

        mc "Vamos conseguir. Eu diss-"

        f "O que foi?"

        mc "Bateu um cansaço."

        f "Tudo bem. São informações demais para você."

        f "O que estamos fazendo aqui não é algo normal. Você está indo contra sua natureza conversando comigo."

        mc "Entendo..."

        f "Durma e amanhã conversamos mais."

        mc "Ok."

        f "Até depois, [mc]."

        mc "Até."

        $ pixel_evento = 1

        scene black with dissolve

        return

    elif pixel_evento == 1:

        "A [f] tem razão. Tem um vento gelado saindo do interior da caverna. E eu já tinha sentido antes."

        "Ela também falou que aqui o poder da bruxa tem menor intensidade."

        "Eu sinto que eu posso encontrar algo importante se eu investigar esta caverna."

        f "Oi, [mc]."

        mc "[f]! O que você tá fazendo aqui?!"

        show mapa4_pixel1 with Dissolve(2.0)

        pause

        f "Que foi? Não ficou feliz em me ver?"

        mc "Não é isso... só fiquei assustado porque é a primeira vez que não te vejo sentada no mesmo lugar."

        f "Ah... Se é isso, então tá."

        f "Eu cansei de ficar sentada choramingando."

        f "Eu quero fazer algo para que as coisas voltem ao normal."

        mc "Isso é incrível, [f]. Parabéns."

        f "Não precisa me elogiar. A culpa é minha e da minha irmã pelas coisas estarem assim."

        f "A gente devia estar protegendo você, mas fomos derrotadas pela bruxa."

        f "Agora eu preciso fazer algo para que tudo volte ao normal."

        mc "Você pretende sair da caverna?"

        f "É o que eu gostaria, mas não sei se tenho coragem."

        f "Me desculpe, [mc]."

        menu:
            "Precisamos de você mais do que nunca. Faça um esforço!":


                mc "Temos que fazer tudo que estiver ao nosso alcance para derrotar ela, [f]."

                mc "Você precisa dar o seu melhor!"

                f "Eu sei..."

                f "Eu vou dar o melhor melhor, [mc]."

                mc "Assim que se fala."
            "Tudo bem. Não seja tão dura com você.":


                $ pixel_amizade += 1

                mc "Não precisa se desculpar. Não seja tão dura com você mesma."

                mc "Nós vamos sair dessa. Você vai ver."

                f "Obrigada, [mc]."

                f "Vejo que eu e minha irmã fizemos um bom trabalho com você."

                mc "Hehe..."

        mc "Independente disso, eu tava pensando agora que talvez eu vá investigar esta caverna."

        f "Tem certeza? Esta caverna tem uma grande fonte de magia vindo do seu interior."

        mc "Justamente por isso. Talvez eu encontre algo que possa nos ajudar."

        f "Fico feliz de ver você corajoso, [mc]. Mas como sua protetora não posso deixar."

        f "Não sabemos o que existe no fundo da caverna. Mas com certeza é algo muito poderoso."

        mc "Mas eu realmente quero fazer algo. Estamos falando da minha cabeça!"

        f "Eu sei. Mas não é fazendo dessa forma que a gente vai conseguir."

        f "Eu sei que é frustrante, mas não podemos ser inconsequentes."

        mc "Ok. Você tem razão."

        f "Você está muito mais maduro, [mc]. Talvez tudo isso tenha seu lado bom também."

        "Ela tá doida! Eu vou esperar ela estar dormindo e entrar nessa caverna."

        "Eu passei pela [p], passar pela [f] vai ser fichinha."

        "Vou fingir que vou acordar e volto aqui amanhã."

        mc "Ai que cansaço... acho que vou acordar, [f]."

        f "Tudo bem. Até a próxima, [mc]."

        mc "Até mais."

        scene black with dissolve

        f "[mc]. Uma última coisa."

        mc "Oi?"

        f "Pense duas vezes antes de querer enganar suas protetoras."

        mc surpreso "!"

        $ pixel_evento += 1

        return

    elif pixel_evento == 2:

        "Tenho que fazer silêncio..."

        "A [f] não pode saber que eu tô aqui."

        "..."

        "Parece que a barra tá limpa. Ela deve tá no lugar de sempre. Preciso passar longe de lá."

        "Contanto que ela não saiba que eu tô aqui, vai ser impossível ela me ver no meio dessa escuridão."

        "..."

        scene black with Dissolve(1.0)

        "Estou quase passando pelo lugar de sempre."

        "Só mais um pouco."

        "..."

        "Não estou enxergando quase na-"

        play sound "audio/som_22_splash.mp3"

        scene caverna caminho1 with vpunch

        "{i}KAPLASH{/i}"

        mc "Argh!"

        "Que merda... caí com tudo... e tá tudo molhado aqui ainda por cima."

        "Droga... deve ter feito um barulhão..."

        "Preciso ficar quieto ou a [f] vai me achar."

        scene caverna caminho1 with Dissolve(2.0)

        play sound "audio/som_18_gotas.mp3"

        "..."

        "..."

        "Não vejo praticamente nada. Também não escuto nada. Só as gotas."

        scene mapa5_pixel_brava with hpunch

        f "[mc]!"

        mc "Caralho!"

        f "O que você está fazendo aqui?!"

        window hide

        pause

        mc "Ai..."

        f "Pode me responder!"

        mc "Você quase me matou do coração..."

        f "Quem dera! Talvez ela fosse menos horrível do que te aguarda no fundo da caverna."

        mc "Desculpa, [f]. Eu não queria te desobedecer, mas eu precisava saber o que tem na-"

        f "Xiu..."

        scene mapa5_pixel_mc with Dissolve(2.0)

        pause

        f "..."

        f "Tem algo... vindo dali."

        f "Algo chamando..."

        f "Um canto... um sentimento..."

        mc "Você tá legal?"

        f "Nós temos que investigar esta caverna, [mc]."

        mc "Mas é isso que eu..."

        mc "Bah! Deixa pra lá!"

        f "Agora não é hora de ficar de mesquinharia. Eu permito que você explore a caverna."

        f "E melhor. Eu vou te acompanhar."

        mc "Sério?!"

        f "Sim!"

        f "Você pode ter vontade e coragem, mas te falta muita coisa."

        f "Nós dois juntos talvez possamos decifrar essa energia que se esconde ali dentro."

        mc "Combinado! Eu vou..."

        mc "Ai!"

        mc "Deu uma tontura..."

        f "Cuidado, [mc]. Não precisamos ter pressa."

        f "Vamos progredir devagar. Por hoje está bom. Volte amanhã e continuamos."

        mc "Acho que é melhor mesmo. Desculpa atrasar a gente."

        f "Não tem porque se desculpar. Como sua protetora, não posso deixar nada acontecer com você."

        f "Mesmo quando você é desobediente..."

        "Ela tá começando a ficar brava de novo. Melhor eu picar a mula."

        mc "Ok. Até, [f]."

        f "Até."

        "..."

        $ pixel_evento += 1

        return

    elif pixel_evento == 3:

        mc "[f]?"

        scene mapa4_pixel1 with Dissolve(2.0)

        f "Oi, [mc]. Pronto?"

        mc "Estou mais pronto do que nunca!"

        f "Perfeito!"

        f "Tenho certeza que existe algo muito valioso no fim daquele caminho."

        f "A energia que eu senti ali não era maligna. Isso me deixou bastante otimista."

        mc "Quer dizer que é um aliado?"

        f "Não."

        mc "Mas você disse-"

        f "Eu disse que não é uma energia maligna. Não quer dizer que é benigna."

        mc "Mas..."

        f "Isso quer dizer que só descobriremos quando encontrarmos a fonte desse poder."

        mc "Combinado. Então vamos começar de uma vez."

        f "Deixa que eu vou na frente."

        scene mapa4_area4 with Dissolve(2.0)

        f "Cuidado com o buraco."

        mc "Acabei aprendendo na marra..."

        scene caverna caminho1 with Dissolve(1.0)

        mc "Opa!"

        mc "Eu sinto um frio muito forte aqui. Muito mais do que antes."

        f "Sim."

        scene mapa5_pixel_conversando with Dissolve(2.0)

        pause

        f "O buraco que nós tivemos que descer serve como uma forma de impedir que o frio vá para fora da caverna."

        mc "Você acha que isso é intencional?"

        f "Pode ser. Talvez, seja lá o que tem aqui, não quer que ninguém o encontre."

        mc "Você acha que tem algo VIVO no fim do túnel?"

        f "Vivo, não sei... acredito que se fosse algo vivo eu estaria captando a energia dele."

        mc "Tem razão. Vamos continuar."

        f "Sim."

        scene caverna caminho3 with Dissolve(2.0)

        mc "Estou começando a me cansar..."

        f "Isso é normal."

        f "Vamos sentar um pouco."

        mc "Tá."

        scene mapa5_pixel_sentados1 with Dissolve(2.0)

        pause

        f "Este lugar é uma espécie de labirinto de um só caminho."

        mc "Como assim labirinto de um caminho só?"

        f "Você enxerga a saída e ela se mostra próxima, mas na verdade ela está a quilômetros de distância."

        mc "Isso é sem noção!"

        f "Isso é magia. E da poderosa, [mc]."

        f "Eu espero que o que nos aguarda ao fim deste túnel realmente não seja um inimigo."

        mc "Eu também... {i}puf{/i}"

        f "Acho que devemos parar por aqui hoje. Quanto mais andarmos, mas você vai se cansar."

        f "Mas se formos devagar, você vai se acostumar com essa energia que está se chocando contra a nossa."

        f "Vamos andar mais longe cada vez que você voltar."

        mc "Seria uma boa... Mas eu posso descansar uns minutinhos e continuamos."

        f "Infelizmente não vai adiantar nada. O cansaço que você está sentindo não é do seu corpo, mas da mente."

        f "Apenas após 24 horas de descanso você vai se recuperar."

        mc "Não é estranho pensar que eu vou ter que acordar para descansar? Normalmente é o contrário..."

        f "Pare de ser bobo, [mc]."

        mc "Mas..."

        mc "Não tenho forças nem pra discutir com você."

        f "Até logo. Vou estar te esperando."

        mc "Até, [f]."

        scene black with dissolve

        $ pixel_evento += 1

        return

    elif pixel_evento == 4:

        "A [f] tá me esperando. Que bonitinha."

        scene mapa4_pixel1 with Dissolve(1.0)

        f "Olá! Pronto para continuar?"

        mc "Sim."

        f "Sinto que estamos chegando perto da saída do túnel."

        mc "Então não vamos perder tempo."

        f "Deixa que eu guio."

        mc "Por favor..."

        scene caverna caminho1 with Dissolve(1.0)

        mc "Já não estou me cansando tanto como antes."

        f "Isso é bom. Mas não vamos parar ainda."

        scene caverna caminho3 with Dissolve(1.0)

        mc "Foi aqui que paramos da outra vez. Mas eu estou com energia ainda."

        play sound "audio/som_18_gotas.mp3"

        scene mapa5_pixel_mc with Dissolve(1.0)

        f "Isso é muito bom. Deixa eu dar uma olhada..."

        f "Estamos chegando bem perto. Acho que hoje mesmo vamos chegar àquela gruta."

        f "Hmmm..."

        f "Estou captando um foco de energia muito grande vindo dalí."

        f "Estamos muito muito perto! Só mais um empurrãozinho, [mc]."

        mc "..."

        scene mapa5_pixel_brava with hpunch

        f "[mc]!"

        mc "Ai!"

        f "Você estava dormindo dentro do sonho!"

        mc "Perdão..."

        mc "Eu tô bem cansado, [f]..."

        f "Tudo bem. Você precisa de um descanso."

        mc "Obrigado..."

        scene mapa5_pixel_sentados1 with Dissolve(2.0)

        f "Não sei se a gente devia ter vindo."

        mc "Tá tudo legal. Só preciso de um tempo."

        f "[mc]..."

        mc "Oi."

        f "Você me odeia?"

        mc "Ah? Como assim?"

        f "Você me odeia?"

        mc "Claro que não. Por que eu odiaria você?"

        f "Ok... vou me ajeitar aqui."

        mc "Tá."

        scene mapa5_pixel_sentados2 with Dissolve(2.0)

        pause

        f "Tudo isso que tá acontecendo com você. Isso é culpa minha também."

        f "Mas eu fico muito feliz de você não me odiar."

        mc "Para de ser boba. Você é só uma garotinha."

        f "Como assim garotinha? Eu tenho centenas de anos."

        mc "Quê?!"

        f "O que foi?"

        mc "É que sua aparência, sei lá..."

        f "Haha. Minha aparência é você quem decide na verdade."

        mc "Eu?"

        f "Sim."

        scene mapa5_pixel_sentados3 with Dissolve(2.0)

        pause

        f "Quando a gente se liga ao nosso protegido, nossa aparência muda de acordo com a.. é... mente, espírito, energia, sei lá como você diz... dele."

        f "Se suas protetoras parecem fadas, é porque seu espírito assim nos transformou."

        mc "Hmmm..."

        mc "Isso quer dizer que outras pessoas vão ter protetores que parecem seres diferentes?"

        f "Com certeza."

        scene mapa5_pixel_sentados2 with Dissolve(1.0)

        f "Tudo depende da energia de cada um."

        f "Se você tivesse visto a minha irmã, veria como a gente é bem parecidas."

        mc "Então essa não é sua forma verdadeira?"

        f "Tehee... o que seria uma forma verdadeira?"

        mc "Se sua aparência depende de mim, como é sua aparência de verdade? Sem ter um protegido?"

        f "Ah! ..."

        mc "..."

        f "Eu não sei..."

        mc "Huh?"

        f "Desculpa. Não é que eu não sei. Na verdade eu não lembro."

        f "Depois de tantos anos como protetora, acho que eu esqueci como eu realmente era..."

        mc "Isso não é... ruim? Não se lembrar de como você é?"

        scene mapa5_pixel_sentados3 with Dissolve(1.0)

        f "Tehee... eu não ligo."

        f "Eu só quero poder proteger você. É só isso que eu me preocupo."

        mc "Obrigado. Você é muito fofinha..."

        f "Obrigada, [mc]."

        mc "Acho que tô melhor."

        scene mapa5_pixel_sentados1 with Dissolve(1.0)

        f "Tem certeza?"

        mc "Sim."

        f "Faz assim. Vai levantando devagar e eu vou na frente preparar o caminho para você."

        f "Se eu achar que ainda falta muito continuamos amanhã."

        mc "Tá. Valeu. Mas vai com cuidado."

        f "Pode deixar. Não se esqueça que eu que sou sua protetora e não o contrário."

        mc "Mas eu me preocupo com você também..."

        f "Tehee... bobinho. Tchau."

        play sound "audio/som_23_passos1.mp3"

        scene caverna caminho3 with Dissolve(1.0)

        "..."

        "Vou aproveitar esse tempo pra descansar mais um pouquinho..."

        "..."

        "..."

        "Puxa. Já faz um tempinho."

        mc "[f]?!"

        "..."

        "Será que ela foi tão longe assim?"

        menu:
            "Continuar esperando":


                $ pixel_amizade += 1

                "Tenho que confiar nela."

                "..."

                "..."

                "Já passou tempo demais."
            "Se arriscar e seguir sozinho pela caverna":


                "Não posso deixar ela sozinha assim. Deve ter acontecido alguma coisa."

        "Tenho que ir atrás dela."

        "..."

        "A [f] disse que faltava muito pouco pro fim do túnel."

        mc "Mais uma forcinha, [mc]!"

        scene black with Dissolve(1.0)

        "..."

        mc "Ela disse que faltava pouco..."

        scene black with hpunch

        mc "Mais um pouco..."

        scene black with hpunch

        mc "Só mais um pouco..."

        scene black with hpunch

        mc "Mais um pouco, porra!"

        scene caverna entrada with hpunch

        pause

        "{i}puf{/i}"

        mc "Consegui! {i}puf{/i}"

        mc "Consegui..."

        "..."

        mc "[f]!"

        f "{size=15}[mc]...{/size}"

        mc "[f]?!"

        f "[mc]! Eu estou aqui! Me ajuda!"

        mc "Eu vou aí te salvar!"

        show white with Dissolve (0.3)

        hide white with hpunch

        play sound "audio/som_27_choque.mp3"

        "{i}BZZZK{/i}"

        mc "Ai!"

        mc "Tem alguma coisa me impedindo..."

        label caverna_impedido_loop:

            mc "Droga..."

        menu:
            "Preciso avançar de novo!":


                mc "Vou tentar de novo, [f]!"

                show white with Dissolve (0.3)

                hide white with hpunch

                play sound "audio/som_27_choque.mp3"

                "{i}BZZZK{/i}"

                mc "Argh! Esse treco queima!"

                jump caverna_impedido_loop
            "Não consigo...":


                mc "É impossível passar, [f]... Não consigo..."

                f "Talvez você esteja cansado..."

                f "Tente descansar e voltar. Talvez você consiga..."

        mc "Não! Quero salvar minha protetora."

        f "Você vai ter que passar por esse campo de energia para chegar até aqui..."

        f "Não sei se você vai conseguir. Eu precisei de muito esforço..."

        mc "Não esquente. Dessa fez eu vou conseguir."

        label caverna_campo_menu:

            "Como será que eu consigo passar por essa barreira?"

        menu:
            "Tentar passar rapidamente":


                "Acho que o melhor é passar de uma vez!"

                mc "Vamos lá!"

                show white with Dissolve (0.3)

                hide white with hpunch

                play sound "audio/som_27_choque.mp3"

                "{i}BZZZK{/i}"

                mc "Argh!"

                mc "Droga! Não deu certo!"

                f "Calma, [mc]..."

                jump caverna_campo_menu
            "Tentar passar com cuidado":


                "Vou tentar passar com muito cuidado. Parece que o problema foi o choque gerado pelo meu corpo com esse campo de força."

                mc "Vamos tentar..."

                show white with Dissolve (3.0)

                show white with hpunch

                "Urrgh..."

                show white with vpunch

                "Acho que..."

                show white with hpunch

                "Droga... é duro demais..."

                play sound "audio/som_27_choque.mp3"

                hide white with vpunch

                mc "Ah!"

                "..."

                "Não funcionou... e agora?"

                jump caverna_campo_menu
            "Não tentar passar":


                mc "Não tenho como passar, [f]. E agora?"

                f "Eu entendo, [mc]. Não se preocupe. Vamos pensar em algo."

                mc "Mas como você vai fazer?"

                f "Eu estou bem. Você não pode me ver, mas eu posso ver você. Eu tenho espaço para andar, e tem água para beber."

                f "E eu não tenho que comer muito, por isso não tenho pressa em sair daqui."

                f "Para falar a verdade, é mais agradável do que o canto escuro que eu estava antes."

                mc "Você tem certeza?"

                f "Sim. Não se preocupe comigo."

                mc "Ok..."

                mc "O que a gente precisa agora é descobrir como eu posso fazer para passar."

                f "Eu vou pensar em algo. Enquanto isso, vou estudar este lugar. Se eu encontrar alguma coisa eu te aviso."

                mc "Ok. Vou tentar descobrir alguma coisa também..."

                f "Vamos sair dessa, [mc]. Confie na sua protetora."

                mc "Com certeza. Depois eu volto aqui pra ver como você tá."

                f "Eu vou ficar muito feliz."

                mc "Agora preciso acordar. Essa barreira acabou comigo."

                mc "Até, [f]."

                f "Beijinhos."

        $ pixel_evento += 1

        return

    elif pixel_evento == 6:

        "Ainda não acredito que a [f] tá presa naquela gruta."

        "Eu tô muito puto comigo mesmo por não ter conseguido tirar ela de lá até agora."

        "Mas agora vai ser diferente. Eu tenho algo diferente comigo desta vez."

        "E a [p]? Então ela sabia o tempo todo que eu tava falando com a [f]..."

        "Mas o que isso quer dizer?"

        scene caverna caminho1 with vpunch

        pause

        mc "Opa."

        "Ela não se importa da gente estar fazendo coisa pelas costas dela?"

        "A [f] falou de uma bruxa. Mas isso parece coisa de filme da Disney..."

        "Por um tempo eu pensei que a [p] podia ser a bruxa que expulsou a [f]... Mas se a [p] não liga, então ela não é?"

        "A [f] também falou de uma irmã... Será que a [p] é a irmã dela?"

        "Elas são realmente bem parecidas..."

        "Mas então por que ela não faz nada pra ajudar a [f] a voltar pra Fadolândia?"

        scene caverna caminho3 with dissolve

        pause

        "Será então que a [p] é só uma {b}terceira entidade{/b}? Será que no fim ela não está ligada com nada disso?"

        "Não posso ficar perdendo tempo pensando nisso agora."

        "Preciso dar um jeito de tirar a [f] daquela gruta!"

        "..."

        scene caverna entrada with dissolve

        mc "[f]! Voltei!"

        f "Oi, [mc]! Obrigada por me visitar!"

        mc "Não vim te visitar. Vim tirar você daqui!"

        f "Mas a barreira..."

        mc "Eu sinto que eu posso remover essa barreira agora."

        f "Sério?! Como?!"

        mc "Você vai ver!"

        label caverna_campo_menu_dois:

            "Como eu vou tentar atravessar ela?"

        menu:
            "Tentar passar rapidamente":


                "Não tenho mais paciência pra essa barreira. Agora eu tenho o poder da [p]!"

                mc "Vamos lá!"

                play sound "audio/som_27_choque.mp3"

                show white with Dissolve (0.3)

                hide white with hpunch

                "{i}BZZZK{/i}"

                mc "Argh!"

                show white with Dissolve (0.3)

                hide white with hpunch

                mc "AAAHHHH!!"
            "Tentar passar com cuidado":


                "Vou tentar passar com muito cuidado. Mesmo com o poder tenho que tomar cuidado."

                mc "Vamos tentar..."

                show white with Dissolve (3.0)

                show white with hpunch

                "Urrgh..."

                show white with vpunch

                "Acho que..."

                show white with hpunch

                "Droga... é duro demais..."

                play sound "audio/som_27_choque.mp3"

                hide white with vpunch

                mc "Ah!"

                "..."

                "Não funcionou... Não acredito! Mesmo com o poder da [p]? E agora?!"

                jump caverna_campo_menu_dois

        scene caverna geral_antes with vpunch

        pause

        mc "ARGH!"

        f "[mc]!"

        mc "Consegui!"

        mc "Consegui passar pela barreira!"

        scene mapa5_pixel_falando with Dissolve(2.0)

        pause

        f "[mc]! Você tá legal?!"

        mc "Sim. Tomei um susto, mas tô legal, sim."

        f "Você caiu com tudo! Você tá bem mesmo?"

        mc "Tô, não esquente comigo. E você?"

        f "Não bateu a cabeça? Parece que tem um galo aí na sua testa."

        mc "Eu já falei que tô bem."

        f "Mesmo com o galo, você foi incrível, [mc]. O jeito que você conseguiu transpor esse campo de força."

        f "Você pareceu um herói."

        mc "Acho que não é pra tanto."

        f "Agora com você aqui a gente vai poder investigar esta caverna melhor!"

        f "Estou muito empolgada!"

        "Ai minha cabeça... Parece que atravessar essa barreira realmente drenou minhas energias..."

        mc "Eu estou um pouco cansado, [f]. Não sei..."

        f "Claro! Você fez muito esforço. Você precisa descansar."

        mc "Acho que eu preciso mesmo."

        f "Bom descanso, [mc]. Amanhã vamos descobrir tudo sobre esta gruta!"

        mc "Pode deixar, [f]. Até amanhã."

        f "Beijinho!"

        $ pixel_evento += 1

        return

    elif pixel_evento == 7:

        "Opa. A [f] tá aqui."

        mc "Oi, pirralhinha."

        scene mapa4_pixel_assustada with Dissolve(1.0)

        f "Ei! Quem é pirralha aqui?!"

        f "Eu sou sua protetora!"

        scene mapa4_pixel_mc with Dissolve(1.0)

        mc "Difícil de acreditar. Pra mim você é só uma fadinha de nada."

        f "{i}Grrr...{/i}"

        mc "É brincadeira! Calma!"

        f "Hmmm..."

        mc "Falando nisso, você vem dizendo que é minha protetora. O que é isso, exatamente?"

        f "Não sei se você merece saber..."

        mc "Hehe... Desculpa. Só queria fazer uma brincadeirinha com você."

        mc "Às vezes eu olho pra você e você parece uma irmã mais nova, sei lá."

        f "E-eu?! Sua irmã mais nova?"

        mc "Sim. Não quero desrespeitar você ou nada assim. É que você é tão pequena..."

        f "Hmmm..."

        scene mapa4_pixel_mc2 with Dissolve(1.0)

        f "Gostei."

        mc "Ãh?"

        f "Ok. Então a partir de agora sou sua irmã mais nova."

        mc "[f]..."

        f "Vo-você não quer mais ser meu irmão?"

        mc "Cla-claro que eu quero."

        f "Tá..."

        f "Então está decidido."

        mc "Ok..."

        "Não era bem isso que eu tinha em mente, mas quem pode negar um pedido de uma fadinha dessas?"

        mc "Pronta pra explorar a caverna?"

        f "Com certeza!"

        scene mapa4_area4 with Dissolve(2.0)

        f "Vem, irmão. Finalmente vamos descobrir o que tem lá dentro."

        mc "Claro. Tô logo atrás de você."

        "A [f] realmente levou esse negócio de irmão à sério..."

        "Ela ficou mais empolgada do que eu esperava com isso."

        "Enfim... Vamos lá."

        scene caverna caminho1 with vpunch

        pause

        scene caverna caminho3 with dissolve

        pause

        scene caverna entrada with dissolve

        "Droga, essa barreira de novo..."

        f "Cuidado com a barreira. Vai ser mais fácil do que da vez anterior."

        mc "Tomara..."

        mc "Espera!"

        f "?"

        show mapa5_pixel_conversando with Dissolve(1.0)

        mc "Como você saiu daí?!"

        f "Tehee! Achei que você nunca fosse perguntar."

        f "Depois que você cruzou ela, ela perdeu muito poder e eu consegui atravessar ela de volta."

        f "Você me salvou!"

        mc "Que bom..."

        f "Mas agora confie em mim. Você vai passar tranquilo."

        f "Eu vou na frente."

        hide mapa5_pixel_conversando with Dissolve(1.0)

        f "Vem!"

        "Vamos lá!"

        show white with Dissolve (0.3)

        hide white with hpunch

        "{i}BZZZK{/i}"

        mc "Ugh!"

        scene caverna geral_antes with Dissolve(1.0)

        pause

        mc "Realmente foi mais fácil dessa vez."

        scene mapa5_pixel_falando with Dissolve(2.0)

        f "Você foi muito bem. Parabéns, [mc]."

        f "Não esperava menos do meu protegido."

        f "Quer dizer, do meu irmão."

        mc "Hehe... obrigado."

        mc "Ufa... finalmente tô aqui no interior da gruta. Parecia tão impossível chegar aqui quando começamos a andar pela caverna."

        f "Você foi muito bem. Estou orgulhosa."

        mc "Valeu."

        mc "Ah. Nesse tempo que você ficou aqui sozinha, o que você descobriu?"

        f "Hmmm..."

        scene mapa5_pixel_visao with Dissolve(2.0)

        pause

        f "Não encontrei nada que possa justificar toda a energia que estou sentindo. Isso é o mais estranho."

        mc "Mas se a energia está vindo daqui, como não estamos vendo de onde ela vem?"

        f "Exatamente. Eu continuo sentindo a energia vindo daqui, mas não vejo nada que possa estar originando todo esse poder."

        menu:
            "Será que é algo invisível?":


                mc "E se a origem dessa energia estiver aqui, agora, mas está invisível?"

                f "Pensando bem, até que faz sentido. Pois com o poder que ela tem, provavelmente ela poderia se esconder de mim dessa forma."

                f "Mesmo usando meus poderes para ver o invisível, como ela é mais poderosa do que eu, ela poderia facilmente me enganar."
            "E se a coisa estiver escondida?":


                mc "E se o responsável por esse poder estiver em algum lugar escondido?"

                f "É meio complicado que ele esteja escondido. Eu pesquisei todos os lugares desta gruta."

                f "Se ele realmente está escondido, então deve ser algo realmente pequenininho."

                mc "Tem razão..."

        f "Mas meu tempo aqui não foi inútil!"

        f "Eu pesquisei cada cantinho daqui e encontrei algumas coisas interessantes. Você precisa ver!"

        mc "O que?"

        f "Vou pegar."

        scene caverna geral_antes with Dissolve(1.0)

        "..."

        f "Está aqui. Olha!"

        show vasilha pedras with Dissolve(1.0)

        pause

        mc "Pedras..."

        f "Isso!"

        mc "..."

        f "Essas pedras com certeza têm alguma ligação com essa energia."

        f "Está vendo essa pedra preta aqui?"

        mc "Hmm... parece que ela tem algo engravado nela..."

        f "Exatamente!"

        f "As pedras negras são diferentes de todas as demais. Elas possuem estes símbolos engravados."

        mc "Isso realmente quer dizer alguma coisa, [f]. Parabéns, maninha!"

        f "Tehee! Eu disse que ia encontrar alguma coisa muito importante aqui!"

        "'Maninha?' Parece que até eu tô entrando nessa onda de irmão-irmã..."

        mc "Enfim, o que será que essas pedras querem dizer?"

        f "Esse é o problema. Eu não tenho certeza..."

        mc "Não se preocupe. Nós vamos descobrir isso juntos."

        f "Ok..."

        "Deixa eu olhar melhor para essas pedras."

        mc "Colocando todas as pedras negras juntas, dá pra ver que tem {b}9 pedras engravadas com letras{/b}."

        f "Isso."

        f "As letras engravadas são dois {b}T{/b}, um {b}S{/b}, dois {b}E{/b}, um {b}G{/b}, um {b}Z{/b} e dois {b}I{/b}."

        mc "Bem observado."

        mc "Vendo essas pedras dessa forma... talvez..."

        mc "..."

        menu:
            "Temos que colocar na ordem correta e formar uma palavra.":


                mc "Eu acho que temos que colocar as pedras negras na ordem correta e formar uma palavra!"

                f "Oh! Isso realmente parece uma boa ideia, [mc]."

                f "Ao menos é uma explicação do porquê essas pedras são diferentes e possuem letras engravadas."
            "Precisamos engravar as mesmas letras nas pedras brancas.":


                mc "Nós temos que pegar as pedras negras e usar elas como moldes para engravar nas brancas também."

                f "Mas como a gente faria isso?!"

                mc "Boa pergunta..."

                f "Mesmo sendo verdade, talvez seja melhor a gente começar com algo que seja possível de fazer."

                mc "Tem toda razão."
            "Temos que quebrar as pedras negras.":


                mc "As pedras negras são as únicas diferentes. Então provavelmente a gente precisa quebrar elas!"

                f "Você acha que essa é a resposta?"

                mc "Com certeza! Deixa comigo!"

                mc "Iááá!"

                f "Não aconteceu nada..."

                mc "Melhor pensarmos em outra coisa..."

        scene mapa5_pixel_falando with Dissolve(2.0)

        f "Colocando as pedras em ordem parece ser a melhor alternativa agora."

        f "Existem muitas palavras mágicas e talvez a gente consiga formar uma e libere a energia que está presa aqui na gruta."

        mc "Vamos nessa então!"

        mc "Mas... qual é a ordem?"

        f "Não faço a mínima ideia..."

        mc "Vamos pensar um pouco..."

        "..."

        scene mapa5_pixel_visao with vpunch

        mc "AAAHH! Não faço a mínima ideia!"

        f "Desculpa, [mc]... Também não me vem nada..."

        mc "Não adianta a gente ficar desesperado."

        mc "Vamos pensar com calma e tentar chegar a uma conclusão."

        f "Combinado!"

        mc "Com certeza vamos encontrar o que tudo isso significa."

        f "Obrigada. Você está sendo um excelente parceiro de exploração!"

        mc "Então eu vou acordar e depois eu volto pra gente continuar."

        f "Certo. Eu vou tentar descobrir alguma coisa que possa nos ajudar."

        mc "Valeu, [f]."

        f "Beijinhos, maninho."

        mc "Tchau..."

        scene black with dissolve

        $ pixel_evento += 1

        return

    elif pixel_evento == 8:

        "Da última vez eu e a [f] estávamos pensando em uma forma de encontrar a fonte da energia."

        "Estou começando a me lembrar de tudo."

        "Parece que quando eu volto pra Fadolândia minha mente vai se recuperando."

        "O mais estranho é que quando eu estou aqui, eu me lembro do que acontece no mundo de verdade..."

        "Mas quando estou no mundo de verdade não lembro o que acontece aqui."

        "Eu tenho a sensação de que aqui é onde eu realmente me sinto completo e não na vida real."

        "Será que isso quer dizer que n-"

        scene mapa4_pixel1 with hpunch

        f "Bu!"

        mc "Eita!"

        f "Oi, [mc]. O que foi? Você parecia paralisado..."

        mc "Não foi nada..."

        f "É normal você se sentir estranho aqui. De vez em quando até eu fico um tanto consternada com o fato de você poder vir até aqui."

        f "Isso não é normal, sabia? Na verdade é bem raro um ser humano que possa fazer isso."

        mc "Interessante você falar sobre isso, porque eu ainda não consigo entender o que esse mundo dos sonhos significa."

        f "Eu também acho estranho você chamar de {b}mundo dos sonhos{/b}."

        mc "Por que?"

        f "Certeza que você gastar seu tempo aqui falando sobre isso ao invés de descobrir os segredos da gruta?"

        mc "Na verdade acho que eu prefi-"

        scene mapa4_area4 with vpunch

        f "Vamos logo, mano!"

        "Droga... eu realmente queria saber mais sobre tudo isso..."

        "Mas ela parece tão empolgada. Só vamo."

        "..."

        scene caverna caminho1 with vpunch

        pause

        scene caverna caminho3 with dissolve

        pause

        scene caverna entrada with dissolve

        pause

        show white with Dissolve (0.3)

        hide white with dissolve

        scene caverna geral_antes with Dissolve(1.0)

        mc "Uou. Eu praticamente não senti nada passando pela barreira."

        f "Verdade!"

        scene mapa5_pixel_falando2 with Dissolve(2.0)

        pause

        f "Você está cada vez mais poderoso, [mc]."

        f "Talvez em algum momento você possa viver aqui o tempo que quiser!"

        "Viver em Fadolândia? Como assim?"

        mc "..."

        show mapa5_pixel_triste with Dissolve(1.0)

        pause

        f "[mc]..."

        f "Que foi? Você não gostaria de viver aqui? A gente poderia se ver sempre..."

        menu:
            "Eu gosto de você, mas minha vida não é aqui.":


                mc "Eu fico feliz de você querer me ver sempre e você sabe que eu gosto muito de você."

                mc "Mas minha vida não é aqui, [f]."

                f "Entendo..."
            "Cla-claro que eu gostaria!":


                $ pixel_amizade += 1

                mc "Cla-claro que eu gostaria. Seria incrível!"

                hide mapa5_pixel_triste with Dissolve(1.0)

                f "Eu também acho!"

        "Parece que a [f] está cada vez mais ligada comigo. Essa reação... negócio de irmão..."

        hide mapa5_pixel_triste with Dissolve(1.0)

        f "Mas agora é hora de encontrarmos uma forma de encontrar o foco do poder."

        mc "Sim. A gente tava falando sobre colocar as pedras engravadas na ordem correta."

        mc "Mas não tenho ideia de que ordem correta é essa."

        f "Eu também não, mas eu tenho uma ideia. E provavelmente nós vamos precisar de você pra isso."

        mc "Não sei o que posso fazer... Não sou um mago como você e sinceramente não entendo nada de magia."

        f "Não é nada disso, bobinho."

        f "No tempo que fiquei trancada aqui eu fiquei um tempo considerável analisando essas plantas e minerais brilhantes."

        mc "Realmente esses cristais e essas plantas não tem nada de normais."

        f "Exatamente. Eles estão brilhando por um motivo específico."

        f "Todos eles foram imbuídos com magia. Quero dizer, alguém colocou um feitiço dentro deles."

        mc "Quê?! Quem fez isso?!"

        f "Provavelmente o mesmo responsável por essa energia que eu sinto desde que entrei na caverna."

        mc "Certo... e que magia é essa?"

        f "Infelizmente eu não sei."

        mc "Puxa..."

        f "Na verdade, eu tentei extrair qualquer informação das pedras e das plantas, mas eu não consigo."

        f "Elas não reagem ao meu poder nem ao meu toque. É como se eu não existisse pra eles."

        mc "Isso é bem estranho..."

        f "Então eu pensei... como eu não consegui..."

        f "Talvez você consiga!"

        mc "Eu?!"

        f "Sim! Se eu que sou daqui não consegui, talvez alguém de fora de Fadolândia consiga!"

        f "Vem aqui!"

        mc "Tá..."

        show mapa5_pixel_cristal with Dissolve(2.0)

        pause

        mc "Não sei, [f]. Eu sou só um cara normal."

        f "Não custa nada tentar, concorda?"

        mc "E se eu morrer?"

        f "Não seja dramático, [mc]. Se fosse perigoso eu nunca deixaria você tentar."

        mc "Ok..."

        mc "Vou tentar."

        f "Assim que se fala!"

        mc "Vou tocar neste treco aqui."

        f "Boa sorte."

        "..."

        show white with Dissolve (0.3)

        hide white with dissolve

        mc "Uou!"

        f "O que foi?!"

        mc "Uma imagem... eu vi uma imagem... mas..."

        mc "{i}puf puf{/i}"

        mc "Tô meio cansado. Mas preciso tocar de novo..."

        f "Não!"

        f "É perigoso!"

        mc "Como assim? Eu acabei de tocar e não acont-"

        scene mapa5_pixel_triste with Dissolve(1.0)

        f "Você sintonizou com a energia contida no cristal."

        mc "Como assim sintonizei?"

        f "Sua alma, espírito, mente, sei lá como você chama, ressoou com a magia no interior do cristal."

        f "Isso fez você ter acesso ao que está dentro dele."

        f "Isso é incrível, mas também muito perigoso. Se você usar energia demais fazendo isso, pode causar problemas permanentes."

        mc "Falando assim você me assusta."

        f "Eu não vou deixar nada acontecer com meu protegido. Quero dizer, com meu irmãozão."

        mc "Obrigado..."

        mc "Mas o que a gente vai fazer então?"

        f "Nossa tarefa continua a mesma. A gente precisa {b}colocar as pedras negras na ordem correta{/b}."

        f "Pelas minha deduções, fazendo isso, nós vamos criar uma palavra mágica que vai revelar a fonte do poder da gruta."

        mc "Entendi. E você acredita que os cristais e as plantas brilhantes possuem as dicas que precisamos pra descobrir a ordem correta."

        f "Isso mesmo. Eu tenho certeza absoluta disso!"

        mc "Ok."

        mc "Então eu vou descansar por um dia e amanhã eu retorno pra podermos começar nossa pesquisa."

        f "Perfeito. Vou estar te esperando, [mc]."

        mc "Até mais, mana."

        f "Tehee... Beijinhos."

        show black with dissolve

        $ pixel_evento += 1

        return

    elif pixel_evento == 9:

        "Hoje eu e a [f] vamos continuar tentando encontrar a fonte do poder que vem daquela gruta."

        "Ela já deve estar lá. Tenho que ir rapidão."

        "..."

        scene caverna caminho1 with vpunch

        pause

        scene caverna caminho3 with dissolve

        pause

        scene caverna entrada with dissolve

        pause

        show white with Dissolve (0.3)

        hide white with dissolve

        jump cave_minigame_inicio

    elif pixel_evento == 10 or pixel_evento == 11:

        "Quero falar com a [f] antes de me encontrar com aquele... Protetor?"

        "Protetor? Onde que eu ouvi isso antes? Pera, a pró-"

        scene mapa4_pixel1 with Dissolve(1.0)

        f "Irmãozão! Oi! Que saudades!"

        mc "Oi! Tudo bem?"

        mc "Aquela coisa não fez nada ruim com você?"

        f "Não. Depois que você saiu eu só me despedi e vim para cá. Não quis ficar sozinha perto dele."

        mc "Eu entendo perfeitamente."

        mc "Mas... o que a gente vai fazer agora? Ele disse que vai responder nossas perguntas..."

        f "Acho que a gente devia aproveitar essa oportunidade e tentar descobrir o máximo que a gente puder."

        mc "Mas você confia nele?"

        f "Como eu te disse, a energia dele é neutra... nem maligna e nem benigna."

        f "Apesar que eu estava pensando sobre isso, e talvez eu esteja errada."

        mc "Em que sentido?"

        f "Talvez ele não tenha uma energia neutra. Na verdade, provavelmente eu que não consigo ler a energia dele e ela aparenta neutralidade."

        mc "Quer dizer que você não consegue entender a energia dele?"

        f "Mais ou menos. Quer dizer que como ele é muito mais poderoso do que eu, talvez eu não tenha capacidade de alcançar a energia dele."

        mc "Entendi... então tem uma possibilidade dele ser uma criatura maligna..."

        f "Sim..."

        menu:
            "Ele me pareceu ser uma criatura bem razoável.":


                mc "Pra falar a verdade, quando escutei ele falando, me pareceu que ele é bem de boa."

                f "Tem razão..."

                f "Será então que ele realmente é do bem?"

                mc "Parece que sim..."
            "Eu não confio nem um pouco nele.":


                mc "Mesmo com a aquele jeito da paz dele, eu não confio nele nem um pouco."

                f "Sério, maninho?"

                mc "Sim. Eu não consigo acreditar nesse jeito dele."

                f "É... acho que você tem razão..."

        mc "Mas, de qualquer jeito, a gente precisa falar com ele. É nossa única chance."

        f "Sim! A gente tem que falar!"

        mc "Então não tem jeito. Bora lá."

        f "Tá!"

        scene caverna caminho1 with vpunch

        pause

        scene caverna caminho3 with dissolve

        pause

        scene caverna entrada with dissolve

        pause

        show white with Dissolve (0.3)

        hide white with dissolve

        mc "Estamos de volta."

        scene mapa5_enki with Dissolve(1.0)

        en "Sejam bem vindos ao meu domínio."

        mc "O-olá..."

        en "Não há o que temer, criança. Vocês invocaram o poder de seus ancestrais. Eu devo lhes oferecer conhecimento. Agora diga..."

        mc "T-tá..."

        scene mapa5_pixel_falando with Dissolve(1.0)

        mc "O que a gente pergunta, [f]?"

        f "Não sei... E se a gente perguntar sobre ele?"

        mc "Bom ideia. Vou começar com essa."

        scene mapa5_caverna with Dissolve(2.0)

        pause

        mc "Você poderia me falar um pouco mais sobre você?"

        en "Se é o que deseja..."

        $ en_nome = "Enki"

        en "Um de meus primeiros nomes foi [en]. Eu sou o Deus da Água. Eu nasci do desejo dos sumérios em ter conhecimento."

        en "Há milhares de anos, eu sou o protetor dos {b}mes{/b}, as {b}Jóias da Civilização{/b}."

        en "De meu poder os sumérios encontraram a prosperidade e se tornaram a monumental civilização pela qual são lembrados."

        mc "E o que você faz aqui?"

        en "O poder de um deus é o poder que ele recebe de seus fiéis. O fim da civilização suméria foi o fim de seus deuses."

        f "{size=15}[mc]!{/size}"

        mc "Ah? Um segundo..."

        scene mapa5_pixel_visao with Dissolve(1.0)

        f "Não sei se a gente deve acreditar nessa criatura..."

        f "E se a gente sair daqui?"

        mc "Como? Você mesma disse pra gente confiar no que ele fala."

        f "Eu sei, mas..."

        mc "Só mais um pouco, [f]. E daí acabo com isso."

        f "Tá..."

        scene mapa5_caverna with Dissolve(1.0)

        mc "Senhor [en]... Se eles tinham seu poder, porque a os sumérios desapareceram?"

        en "Ah, jovem... essa é uma história que não posso contar com palavras. Faz-se mister ver para entender."

        en "Eu lhe proponho..."

        en "Uma viagem ao passado pelas minhas lembranças, para ver como tudo isso se iniciou."

        en "Será a maior viagem que você já fez em sua vida. Isso eu lhe garanto..."

        f "[mc]!"

        scene mapa5_pixel_falando2 with Dissolve(1.0)

        f "Isso é perigoso, [mc]..."

        mc "[f]! Nós temos que saber tudo. É o único jeito de salvar eu, você e sua irmã da bruxa!"

        f "Te entendo... mas por favor tome cuidado."

        mc "Pode deixar."

        scene mapa5_caverna with Dissolve(1.0)

        en "Pronto para visitar o passado?"

        mc "Sim. Tô pronto."

        en "Pois então, venha comigo, venha ser eu..."

        scene white with Dissolve(3.0)

        scene inanna_hall with Dissolve(2.0)

        pause

        "O Templo de Abzu... eu olhava para minha morada com orgulho."

        "Do templo, eu protegia os mes e garantia que os sumérios seguissem sempre o caminho correto."

        "Muitos deuses me visitavam e se deslumbravam com a mejestade de Abzu."

        "Eis que um dia ela se encontrava na entrada do templo."

        "..."

        scene inanna_leao with Dissolve(2.0)

        pause

        ina "Pai!"

        en "Olá, filha."

        ina "Como foi a caminhada?"

        en "Enriquecedora."

        ina "Fico feliz por você."

        $ ina_nome = "Inanna"

        en "[ina]... quantas vezes eu já lhe falei para não usar esse tipo de roupa?"

        ina "Mas eles gostam de mim assim, pai."

        ina "O senhor tem que parar de pensar com sua cabeça. O senhor é velho."

        en "[ina]..."

        en "Você é uma deusa. Você deve se trajar com os mantos reais."

        ina "Eu sou a deusa mais adorada, pai... até mesmo mais que o senhor."

        en "Adoração não é tudo..."

        ina "..."

        ina "Pai. Eu sou a mais adorada. Mas-"

        en "De novo isso?"

        scene inanna_brava with hpunch

        ina "Qual vai ser sua desculpa desta vez?!"

        en "A mesma de sempre, filha."

        ina "Você não vê?! Eu sou a mais querida! Os sumérios me amam! Me desejam!"

        ina "Por que você me trata como ralé?!"

        en "[ina]... eu não te trato como ralé."

        ina "Eu quero mais responsabilidades!"

        en "Você já disse isso. Várias vezes."

        ina "E o senhor nega todas elas!"

        en "E continuarei negando..."

        ina "O senhor é um idiota!"

        scene black with dissolve

        "..."

        "..."

        scene inanna_hall with Dissolve(2.0)

        pause

        "Entre todos os deuses, [ina] sem dúvidas é a mais imprevisível. Quando ela coloca algo na cabeça, é impossível tirar."

        "Aqui está ela novamente..."

        scene inanna_leao with Dissolve(1.0)

        ina "Como vai, amado pai?"

        en "Vou bem, filha. E você?"

        ina "Estou bem. O senhor pensou sobre o que eu pedi?"

        en "Eu expliquei para você..."

        scene inanna_brava with hpunch

        ina "Pai!"

        ina "O povo de Uruk clama por meu nome! Meu poder cresce com o passar dos anos!"

        en "E seu temperamento continua o mesmo..."

        ina "{i}Grrrr{/i}"

        ina "Você não vai poder me coibir para sempre! Entendeu?!"

        en "O que você deseja está longe de lhe ser garantido. Tem paciência e sua hora chegará."

        ina "Não! Chega de esperar! Milhares de pessoas me veneram! Eanna cresce a cada dia e eles clamam por minha intervenção!"

        en "Eles hão de esperar."

        ina "PAI!"

        en "Sua influência vai crescer de acordo com sua sabedoria. Observe e aprenda com seu pai."

        ina "Maldito!"

        scene black with dissolve

        "..."

        scene mapa5_pixel_falando2 with Dissolve(1.0)

        "..."

        mc "O-o que foi isso?"

        f "Você tá bem, [mc]?"

        mc "Eu tô legal... só um pouco zonzo."

        f "Toma cuidado. Você não pode se esforçar demais."

        mc "Pode deixar."

        mc "[en]... o que isso significa?"

        scene mapa5_caverna with Dissolve(1.0)

        en "Essa é uma das minhas últimas lembranças."

        en "Minha conversa com [ina] levou ao fim da civilização suméria."

        "[mc] e [f]" "QUÊ?!"

        en "Mas então algo ocorreu. Eu perdi acesso ao meu passado."

        en "Essas são as últimas lembranças que me restaram. E tudo converge para que tenham sido determinantes."

        f "Então essas visões que o [mc] viu fazem parte do acontecimento que levou os sumérios ao fim?"

        en "Exatamente, pequena. Apesar de que eu ainda não saiba exatamente como isso ocorreu."

        f "Entendo..."

        mc "Eu agradeço pela sua ajuda, [en]. Voltarei em breve e conversamos."

        en "A magia das runas negras perdurará por muito tempo, não há motivo para ansiedade."

        mc "Vem, [f]."

        f "Tá."

        "..."

        scene mapa5_pixel_conversando with Dissolve(1.0)

        mc "Sabe, [f]... acho que eu tenho uma dica sobre o que aconteceu..."

        f "Como assim?"

        mc "Quando eu tava procurando algo pra você comer, eu achei um carinha chamado [fado] que tava com aquela maçã."

        mc "Pra ele me dar a maçã, ele pediu em troca um cristal que tava perto de uma gruta."

        f "Hmm..."

        mc "Então... quando eu toquei no cristal, uma imagem apareceu... e eu tô achando que eu vi exatamente a mesma cena na lembrança do [en]."

        f "Isso é sério, maninho... Ter muito contato com lembranças e imagens de outros seres pode causar problemas para você."

        mc "Eu sei... mas, talvez, o cristal tenha alguma coisa a ver com que o [en] me mostrou."

        f "Pode ser que tenha. Você vai tentar pegar ele de volta?"

        mc "Sim. Acho que vou fazer isso. Tenho que falar com o [fado]."

        scene mapa5_pixel_brava with Dissolve(1.0)

        f "Maninho! Por favor prometa que você vai tomar cuidado."

        f "Eu sou sua protetora! E se envolver com criaturas daqui pode ser muito ruim para você!"

        mc "Ok. Eu prometo que vou ter cuidado."

        f "Então promete três vezes."

        menu:
            "Não precisa se preocupar. Eu vou ficar bem.":


                mc "Não precisar ficar assim. Vai dar tudo certo."

                f "Irmão, idiota... podia só ter prometido!"

                mc "Hehe..."
            "Prometo prometo prometo.":


                $ pixel_amizade += 1

                "Cada uma..."

                mc "..."

                f "Vai!"

                mc "Prometo prometo prometo."

                f "Acho bom!"

        mc "Volto assim que tiver o cristal."

        f "Cuidado!"

        mc "Pode deixar."

        scene black with dissolve















































        $ pixel_evento = 12

        return

    elif pixel_evento == 12:

        if not fadolandia_cristal and not fadolandia_cristal_n:

            "Antes de voltar aqui, preciso conseguir o cristal do [fado]."

            "Só espero que ele queira algo razoável em troca."

            jump fadolandia_m4a2
        else:


            if fadolandia_cristal_n:

                mc "[f]. Tá aí?"

                f "Oi, maninho."

                scene mapa4_pixel1 with Dissolve(1.0)

                f "Tudo bem?"

                mc "Infelizmente não consegui encontrar o cristal."

                "Pra falar a verdade eu sei onde tá, mas não quero que ela ache que sou um covarde, sei lá."

                f "Não tem problema. Nós vamos dar um jeito nisso, tá bom?"

                mc "Ok. Vamos, sim."

                "Que droga. Por que será que o [fado] queria minha consciência?"

                "Acho que eu tomei a decisão certa. Agora só tenho que encontrar outra forma de descobrir sobre o [en]."

                mc "Vou pensar em alguma coisa e depois eu volto, tá legal?"

                f "Tudo bem. Eu também vou pensar. Vou sentir saudades."

                mc "Eu também. Mas logo eu volto."

                f "Tá."

                mc "Até."

                f "Beijinhos."

                $ pixel_evento += 1

                jump fadolandia_m4a2

            elif fadolandia_cristal:

                mc "[f]! Voltei!"

                scene mapa4_pixel1 with Dissolve(1.0)

                f "Oi!"

                mc "Consegui o cristal!"

                f "Legal! Esse é meu irmãozão!"

                mc "Hehe."

                f "Tenho muito orgulho de você."

                mc "Valeu. Agora vamos ver o que o [en] pode nos falar sobre esse cristal. Tô ansioso."

                f "Eu também. Vamos lá."

                scene caverna caminho1 with vpunch

                "Opa."

                scene caverna caminho3 with dissolve

                pause

                scene caverna entrada with dissolve

                pause

                show white with Dissolve (0.3)

                hide white with dissolve

                mc "[en]! Voltamos."

                scene mapa5_enki with Dissolve(1.0)

                en "Sinto uma energia familiar em suas mãos, jovem."

                mc "Sim. Quando eu toquei neste cristal, eu vi uma imagem, que é a mesma imagem da lembrança que você me mostrou."

                en "Não pode ser... Então é isso."

                mc "Ah?"

                f "Também não entendi, senhor [en]."

                en "Só existe uma explicação para você ter visto uma imagem da minha lembrança ao tocar nesse objeto."

                en "A explicação também deixa claro o porquê de eu ter reconhecido a energia dentro desse cristal."

                mc "E qual é a explicação?"

                en "Novamente, vamos viajar para o passado."

                scene mapa5_pixel_triste with Dissolve(1.0)

                f "Mas você disse que perdeu suas lembranças..."

                f "Como o [mc] vai poder rever o passado assim?"

                en "Tenha calma, pequena. Tudo será explicado no seu devido tempo."

                en "Está pronto, jovem?"

                mc "Sim."

                f "Tome cuidado, maninho."

                mc "Eu vou ficar bem."

                scene white with Dissolve(3.0)

                pause

                scene inanna_brava with Dissolve(1.0)

                ina "Maldito!"

                "Esse velho continua atrapalhando tudo o que eu planejei!"

                ina "Tchau, velho!"

                scene inanna_hall with Dissolve(1.0)

                "Droga... eu preciso de mais influência entre os deuses."

                "Por que o velho não pode só aceitar que eu sou a deusa mais amada e me dar um papel à altura?"

                "Existem deuses ridículos que possuem mais tarefas do que eu... a deusa mais venerada da Suméria!"

                "Vou acabar com esse velho se for preciso. Mas vou ter MEU DEVIDO LUGAR nesse círculo."

                scene black with dissolve

                "..."

                scene inanna_vault with Dissolve(2.0)

                "Finalmente!"

                "Então é aqui que ele guarda..."

                "Estou muito perto. Já consigo sentir em minhas mãos."

                "Depois dessa ele não vai ter outra escolha senão me escutar."

                "..."

                "Aqui! Encontrei!"

                play sound "audio/som_26_roar.mp3"

                scene inanna_vault_tesouro with hpunch

                pause

                ina "Por todos os infernos!"

                "Ele protegeu tudo muito bem..."

                "Não adianta eu tentar violar... vou precisar descobrir a senha."

                "Eu te substimei, pai. Só que eu ainda não desisti."

                "Você ainda vai me ver."

                scene black with dissolve

                "..."

                scene inanna_porta with Dissolve(2.0)

                pause

                ina "Nã-nã-não..."

                en "Sai da frente, [ina]. Eu bebi demais, preciso..."

                ina "O senhor tá perdendo o jeito, velho."

                en "Calada..."

                ina "Tá. Só me responde uma coisa..."

                en "Pergunta logo."

                ina "O que é a coisa mais importante para você no mundo?"

                en "Que raios de pergunta é essa?!"

                ina "Estou falando sério."

                en "..."

                ina "Não vai responder?"

                en "Não."

                ina "Hmmm"

                ina "Não creio."

                en "Sai pra lá agora."

                ina "..."

                ina "Tá certo. Pode mijar bastante."

                en "Não... fale assim..."

                ina "Hahaha!"

                scene black with dissolve

                "..."

                scene inanna_vault with Dissolve(1.0)

                "Será que é realmente isso?"

                "Talvez eu não devesse ter deixado o velho passar tão rápido..."

                scene inanna_vault_andando with Dissolve(2.0)

                pause

                "Não posso errar. Eu só tenho uma única chance. O que eu estou fazendo pode me mandar para o ostracismo eterno."

                "Calma, [ina]. Não é hora de ter medo."

                "Você vai dar seu jeito."

                "Eu não quero nada que não me seja de direito. Eu cheguei aqui. Eles me amam. Eu mereço um lugar ao sol."

                "Do jeito que o velho é caduco ele deve ter deixado no mesmo lugar."

                "..."

                "Dito e feito."

                scene inanna_vault_tesouro with Dissolve(2.0)

                ina "Olá, amiguinho. Vim te visitar de novo."

                play sound "audio/som_26_roar.mp3"

                "Quem diria que meu pai seria tão previsível..."

                "Ou será que ele só quer me enganar?"

                "Se eu errar a chave, provavelmente eu estou perdida para sempre."

                "Mas eu vou dizer a chave correta. Não posso ter medo agora."

                "Infinitas palavras... mas apenas uma abre o tesouro. As {b}Jóias da Civilização{/b}. Tão perto... mas tão longe."

                ina "Força, [ina]!"

                ina "..."

                ina "Tesouro escondido / Tesouro guardado / Para abrir eu preciso / Do termo sagrado."

                ina "I N A N N A"

                "..."

                scene black with hpunch

                "{i}GATCHINK{/i}"

                scene inanna_vault_mes with Dissolve(2.0)

                pause

                "PERFEITO!"

                "O {b}me{/b} é meu!"

                "O poder divino! A Jóia da Civilização!"

                "Você foi esperto, [en]! Mas o amor pela filha te traiu!"

                "Eu venci!"

                "Hahahahaha!"

                scene black with Dissolve(1.0)

                pause

                scene mapa5_caverna with Dissolve(1.0)

                en "Então foi isso que aconteceu..."

                mc "Então a [ina] roubou os mes de você?"

                en "É o que a lembrança nos diz."

                mc "Sim..."

                en "Isso também explica como ela se tornou tão poderosa, a ponto de reformular tudo."

                en "Eu falhei... como protetor das joias e também como protetor dos sumérios."

                mc "Não, [en]. Você foi engando pela pessoa mais importante pra você. Não tem o que lamentar!"

                en "..."

                mc "[f]? Pode me ajudar?"

                mc "[f]? [f]!"

                mc "Meu Deus!"

                scene mapa5_pixel_apagada with hpunch

                pause

                mc "[f]!!"

                mc "Acorda! Ei!"

                en "Ela está vazia."

                mc "Vazia?! Como assim?!"

                en "Como se alguém tivesse tirado o espírito dela de dentro do seu invólucro material."

                en "O que ela era, não está mais aí, mas sim em outro lugar."

                mc "Em outro lugar? Quem poderia tirar da minha cabeça e-"

                mc "[fado]!"

                mc "[en]! Por favor! Cuide dela pra mim!"

                en "Ela estará protegida até seu retorno."

                mc "Obrigado. Vou procurar o responsável por isso e pensar em um plano."

                mc "Por favor, não deixe nada acontecer com ela enquanto eu estou fora."

                en "Dou minhha palavra, jovem."

                mc "Obrigado. Vou sair daqui urgente e encontrar uma forma de trazer ela de volta."

                $ pixel_evento += 1

                jump fadolandia_m4a2

    elif pixel_evento == 13:

        "Não adianta eu ir pra caverna agora."

        "Antes preciso pensar em um plano."

        "Provavelmente vou ter que {b}esperar um tempo{/b} até poder continuar."

        jump fadolandia_m4a2

    "Deixa eu sair daqui."

    "..."

    jump fadolandia_m4a2

label fadolandia_m4a3:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m4a3"

    hide screen fadolandia_tela

    scene mapa4_area3 with Dissolve(2.0)

    pause

    if not fado_m4a3:

        $ fado_m4a3 = True

        play sound "audio/som_18_gotas.mp3"

        "Tá começando a não dar pra ver nada..."

        "A luz mal chega aqui. Provavelmente mais pra frente é um breu só."

        "E eu consigo escutar uns barulhos vindo de lá. Certeza que tem alguma coisa lá dentro."

        "Será que realmente vale a pena arriscar?"

        "Talvez tenha outro caminho..."

    menu:
        "Seguir para o interior da caverna":


            jump fadolandia_m4caverna
        "Voltar para a luz":


            "Deixa eu sair daqui. Não tenho porque entrar nesse breu agora."

            jump fadolandia_m4a2

label fadolandia_m4a2:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m4a2"

    hide screen fadolandia_tela

    scene mapa4_area2 with Dissolve(2.0)

    pause

    if not fado_m4a2:

        $ fado_m4a2 = True

        play sound "audio/som_18_gotas.mp3"

        "Aqui tá mais frio que na floresta. Tem um vento gelado saindo desse lugar..."

        "Dá pra escutar o som das gotas batendo nas pedras."

        "..."

        "E... tem outra coisa... parece que eu escutei algo se mexendo ali na frente..."

        "Desde que eu comecei a ter esse sonho só tem acontecido coisas estranhas."

        "Tenho que pensar muito bem onde eu vou me meter."

    show screen fadolandia_tela

    pause

label fadolandia_m4a1:

    play sound "audio/som_25_passos3.mp3"

    if not fado_m4a1:

        "..."

        "Tá cheio de mato nesta região. Nem sei direito pra onde tô indo."

        "..."

        "Ai... ai... maldito matagal!"

        "Por que eu sinto dor mesmo no sonho?"

        "Epa... tem uma luz ali..."

        "Acho que to vendo a saída!"

    $ fadolandia_mapa = "m4a1"

    hide screen fadolandia_tela

    scene mapa4_area1 with Dissolve(2.0)

    pause

    if not fado_m4a1:

        $ fado_m4a1 = True

        "Uou... Olha pro tamanho disso aqui!"

        "Caraca... uma caverna..."

        "Não quero nem imaginar que tipo de desgraça que me espera ali dentro."

        "Essa caverna me dá calafrios, mas não adianta eu ficar com medo."

        "Se eu quiser ver onde tudo isso acaba, eu preciso continuar."

        "Seja o que Deus quiser..."

    show screen fadolandia_tela

    pause

label fadolandia_m3a7:

    play sound "audio/som_22_splash.mp3"

    $ fadolandia_mapa = "m3a7"

    hide screen fadolandia_tela

    scene mapa3_area7 with Dissolve(2.0)

    pause

    if not fado_m3a7:

        "Consegui! Cheguei deste lado."

        "Até que foi tranquilo."

        "Eu consigo ver o lugar daqui. Ele tá bem lá na frente."

        "Tô muito ansioso pra saber o que é aquilo."

        "Só torço pra eu não me arrepender de tá indo lá."
    else:


        "Ufa. Cheguei."

    play sound "audio/som_25_passos3.mp3"

    if not fado_m3a7:

        scene mapa3_fonte with Dissolve(2.0)

        pause

        $ fado_m3a7 = True

        "Uma fonte..."

        "E ainda tá funcionando..."

        "O que isso tá fazendo aqui no meio do nada?"

        "Uma coisa dessas tem que ter sido feita por alguém, certo?"

        mc "Quem será que fez isso aqui?"

        "Hmmm..."

        "Não tô vendo nada de estranho aqui."

        "Pera!"

        "Será uma fonte dos desejos?!"

        "Bem que ela podia realizar pelo menos um desejo."

        mc "Não custa nada tentar."

        menu:
            "Desejo ser rico e não precisar mais trabalhar pro chefe.":


                "..."
            "Desejo pegar todas as garotas e nenhuma descobrir.":


                "..."
            "Desejo que as atualizações demorem menos que duas semanas.":


                "..."

        "Pronto. Será que vai funcionar?"

        mc "Bem que podia funcionar. Quando eu acordar vamos ver."

        fado "Sério mesmo?"

        mc "Hãh?!"

        fado "Sério mesmo?"

        mc "Quem disse isso?!"

        fado "Aqui."

        scene black with hpunch

        mc "Ai!"

        scene mapa3_fado_maca with hpunch

        pause

        fado "Oi."

        menu:
            "Quem é você?!":


                mc "Qu-quem é você?!"

                fado "Por que você tá gritando?"
            "Você bateu na minha cara! Qual é a sua?!":


                mc "Tá louco?! Você me acertou!"

                fado "Calma, calma... não doeu tanto assim."

        $ fado_nome = "Fado"

        fado "Meu nome é [fado]."

        mc "[fado]?"

        fado "Que que tem?"

        mc "[fado] tipo o marido da fada?"

        fado "..."

        fado "E quem é você?"

        mc "Ah. Meu nome é [mc]."

        fado "..."

        mc "Que foi?"

        fado "[mc] tipo o marido do Mário?"

        mc "Que Mário?"

        fado "Deixa pra lá..."

        fado "O que esperar de alguém que acredita em Fonte dos Desejos?"

        mc "Ei! Era só uma tentativa!"

        mc "Mas, fala aí... funciona ou não?"

        fado "Quem sabe..."

        mc "..."

        fado "Que foi?"

        mc "Você é a primeira criatura que realmente conversa comigo aqui, tirando a [f]."

        fado "Você ainda deve ser novo por aqui."

        fado "Existe uma série de seres estranhos andando por estas bandas."

        mc "Eu sei que é esquisito perguntar isso no próprio sonho. Mas você sabe por que eu sonho tanto a mesma coisa?"

        fado "Sonhar?"

        mc "É. Por que?"

        fado "Whatever... não sei, maninho."

        fado "Faz tempo a última vez que eu vi alguém que ainda pode falar e pensar. A maioria meio que ficou... retraída... com o passar dos séculos."

        mc "Séculos?!"

        fado "Por que tudo você tem que gritar como se fosse algo incrível?"

        mc "Sei lá..."

        fado "Você tá me cansando..."
    else:


        if not fado_maca:

            scene mapa3_fado_maca with Dissolve(2.0)

        elif fadolandia_cristal and pixel_evento > 12:

            scene mapa3_fonte with Dissolve(2.0)

            pause

            mc "[fado]."

            mc "..."

            mc "[fado]!"

            mc "Cadê esse merdinha?!"

            "Puta que pariu... o que ele fez com a [f]?!"

            "Ele não tá aqui... Deixa eu sair daqui."

            jump fadolandia_m3voltar
        else:


            scene mapa3_fado with Dissolve(2.0)

        pause

        fado "Fala, maninho!"

        mc "E aí."

        fado "Bom ver que você ainda pode falar."

    label mapa3_fado:

        fado "O que você quer?"

    menu:

        "Será que você pode me emprestar o cristal?" if pixel_evento == 12 and ( not fadolandia_cristal and not fadolandia_cristal_n ):

            mc "Sei que pode parecer meio contraditório, mas você poderia me devolver o cristal?"

            fado "Você só pode tá brincando, maninho. Você acabou de me dar isso..."

            mc "Eu sei... mas as circunstâncias mudaram..."

            fado "Você é um sarro..."

            mc "..."

            mc "E então?"

            fado "Hmmm..."

            fado "Ok."

            mc "Sério?!"

            fado "Sim."

            mc "Obri-"

            fado "Com uma condição."

            "Claro..."

            mc "Qual condição?"

            fado "Eu quero metade da sua consciência."

            mc "Como é?!"

            fado "Você não vai sentir diferença alguma."

            label fado_cristal:

                "Hmmm..."

            menu:
                "Eu aceito.":


                    $ fadolandia_cristal = True

                    mc "Ok. Eu aceito."

                    fado "Escolheu certo, amigo."

                    fado "Aqui tá seu cristal."

                    mc "Valeu."

                    mc "E a minha consciência? Já pegou metade?"

                    fado "Não não. Não tenho pressa, maninho. Quando acontecer, você vai saber."

                    mc "Tá. Valeu."

                    mc "Vou nessa então."

                    fado "Vai na fé."

                    jump fadolandia_m3voltar
                "Pensar sobre a escolha.":


                    "O que será que ele quer dizer com 'metade da consciência'?"

                    "Será que isso vai influenciar o quê?"

                    "Isso me deixa meio cabreiro, mas se eu não aceitar, não tenho como pegar o cristal."

                    "Parece complicado, mas vou ter que resolver isso."

                    jump fado_cristal
                "Eu não aceito.":


                    "Se eu não aceitar, não vou poder saber mais sobre a relação do [en] com a [ina]."

                    "Essa provavelmente é uma decisão bem importante."

                    "Certeza que não vou aceitar?"

                    menu:
                        "Certeza. Não vou aceitar a proposta.":


                            $ fadolandia_cristal_n = True

                            "Certeza. Não posso aceitar algo como perder metade da minha consciência."

                            "Isso é um absurdo."

                            mc "Valeu, [fado], mas não vou querer."

                            fado "Certeza, maninho?"

                            mc "Sim."

                            fado "É uma pena, mas tamo aí."

                            mc "Beleza. Vou dar meus pulos aqui."

                            jump fadolandia_m3voltar
                        "Preciso pensar melhor...":


                            "Espera."

                            jump fado_cristal

        "Eu encontrei o que você quer." if not fado_maca and fado_faloumaca and fado_m2cristal:

            mc "Eu encontrei o que você me pediu."

            mc "É este cristal aqui?"

            jump fadolandia_m3cristal

        "Eu preciso dessa maçã." if fado_precisa_maca and not fado_faloumaca:

            $ fado_faloumaca = True

            "Essa maçã que ele tá segurando..."

            "Se eu conseguir levar isso pra fada da caverna, talvez ela fale comigo!"

            mc "Eu preciso dessa maçã que você tem aí."

            fado "Hm? Por que?"

            mc "Não interessa. Se você não for comer, posso ficar com ela?"

            fado "Hmmm... você realmente parece interessado nisso aqui."

            "Por que eu preciso negociar com uma criatura no MEU sonho? Ela não pode só fazer o que eu quero?"

            mc "Vai logo, cara..."

            fado "Sem dúvida, você é a criatura mais impaciente que eu já vi por aqui."

            mc "..."

            fado "Bom... pensando bem, talvez a gente possa barganhar."

            mc "Certo..."

            fado "Tem algo que eu preciso. É um... uma espécie de escultura de vidro."

            fado "Você vai encontrar isso lá perto da gruta da criatura cheia de cabeças. Sei lá o nome daquilo."

            if fado_m2cristal:

                "Calma! Eu tenho isso! Ele tá aqui comigo."

                mc "Você tá falando desse cristal?"

                label fadolandia_m3cristal:

                    python:
                        if renpy.android:
                            renpy.block_rollback()

                    $ fado_maca = True

                    fado "Oh! Isso mesmo! Você encontrou!"

                    mc "O que que é isso aqui?"

                    mc "Parece que eu vi uma imagem quando eu peguei ele. O que era?"

                    fado "Esqueça isso. Você quer ou não a maçã?"

                    "Parece que o cristal é mais valioso do que parece. Eu-"

                    fado "Dou-lhe uma! O cristal pela maçã!"

                    mc "Espera! Eu-"

                    fado "Dou-lhe duas!"

                    mc "Ok! Ok! O cristal é seu!"

                    fado "Perfeito! Obrigado! Pega aqui sua maçã!"

                    scene fadolandia maca with hpunch

                    pause

                    "Droga. Ele me forçou a trocar."

                    "Pelo menos eu consegui a maçã. Espero que seja suficiente pra fada da caverna falar comigo."

                    "O jeito que ela é parecida com a [p]. Tenho certeza que ela vai poder me ajudar."

                    "Tenho que levar pra ela o mais rápido possível."

                    jump fadolandia_m3voltar

            "Uma espécie de escultura de vidro..."

            "Pelo que ele disse, deve ser então na área da gruta. Aquela que fica antes de eu chegar no lago."

            "Vou ter que dar uma fuçada por lá até encontrar essa tal coisa que ele quer."

            mc "Combinado. Eu vou atrás do seu treco aí."

            fado "Perfeito. Não demore."

            mc "Tu é folgado..."

            jump fadolandia_m3voltar
        "Nada por enquanto.":


            "Se eu não tenho nada a mais pra falar com ele, vou voltar pro outro lado do lago."

            menu:
                "Voltar para o outro lado":


                    label fadolandia_m3voltar:

                        "..."

                        python:
                            if renpy.android:
                                renpy.block_rollback()

                    if not fadolandia_cristal:

                        mc "Falou, [fado]."

                        fado "Mantenha a mente afiada, [mc]. Até logo."

                        "..."

                    play sound "audio/som_22_splash.mp3"

                    scene mapa3_area7 with Dissolve(2.0)

                    pause

                    "Deixa eu voltar."

                    "..."

                    python:
                        if renpy.android:
                            renpy.block_rollback()

                    jump fadolandia_m3a2
                "Permanecer na fonte":


                    "Só mais uma coisinha."

                    jump mapa3_fado

label fadolandia_m3pedra:

    hide screen fadolandia_tela

    scene mapa3_pedra with Dissolve(2.0)

    pause

    if not fado_m3pedra:

        $ fado_m3pedra = True

        "Hmmm..."

        "Então realmente não dá pra passar por aqui."

        "Essa pedra não parecia tão grande de longe."

        "E tem alguma coisa estranha com ela."

        "Tipo uma energia, sei lá. Minha vista fica um pouco embaçada quando tô aqui olhando pra ela."

        "E parece que minha mão tá formigando também."

        "Pior que dá pra ver aquele lance construído daqui. Só preciso passar pela pedra."

        "Só que esse treco energizado. Quase certeza absoluta que eu vou me foder muito se eu encostar nessa pedra."

    "Eu consigo sentir uma energia emanando da pedra."

    "E agora?"

    menu:
        "Tentar escalar a pedra e chegar ao outro lado":


            "É o melhor jeito de chegar do outro lado. Tenho que tentar."

            python:
                if renpy.android:
                    renpy.block_rollback()

            "Pegar apoio e f-"

            play sound "audio/som_27_choque.mp3"

            show white with Dissolve(0.2)

            show white with hpunch

            mc "AAAARRRGH!"

            play sound "audio/som_22_splash.mp3"

            "..."

            scene mapa3_afogado with Dissolve(2.0)

            pause

            "..."

            "..."

            if mapa3_energizado:

                "Que estranho... Eu acho que já sonhei com isso uma vez..."

                "Por que de novo a mesma coisa?"

            scene black with Dissolve(2.0)

            $ mapa3_energizado = True

            "{b}[mc] se sente energizado{/b}"

            jump fadex_errou
        "Se afastar da pedra":


            "Essa energia que eu tô sentindo é perigosa demais."

            "Deixa eu sair daqui."

            if fadolandia_mapa == "m3a4":

                jump fadolandia_m3a4
            else:


                jump fadolandia_m3a3

label fadolandia_m3lago:

    hide screen fadolandia_tela

    "O jeito mais rápido de chegar até a outra margem do lago é nadando."

    "E além de tudo a água tá bem limpa. Eu consigo ver até o fundo do lago e não tem nada perigoso."

    menu:
        "Entrar no lago e nadar até o outro lado":


            "Bora dar um tchibum até a outra margem."

            python:
                if renpy.android:
                    renpy.block_rollback()

            play sound "audio/som_22_splash.mp3"

            scene mapa3_nadando with Dissolve(2.0)

            pause

            "A água tá uma delícia. Na temperatura ambiente."

            "Caraca... fazia tempo que eu não nadava."

            "..."

            if not mapa3_energizado:

                python:
                    if renpy.android:
                        renpy.block_rollback()

                scene mapa3_monstro with Dissolve(2.0)

                pause

                "..."

                "Huh? Parece que tem alguma coisa atrás de mim."

                scene black

                pause

                play sound "audio/som_28_bolhas.mp3"

                mc "Brrrrrrrrglgrrrlglgrrrr"

                "..."

                scene mapa3_afogado with Dissolve(2.0)

                pause

                "..."

                "..."

                jump fadex_errou
            else:


                show white with Dissolve(0.3)

                hide white with Dissolve(0.3)

                "{b}Descargas de energia são liberadas{/b}"

                $ mapa3_energizado = False

                "..."

                "Estou quase do outro lado."

                "..."

                jump fadolandia_m3a7
        "Desistir e ficar onde está":


            "Talvez depois eu dê um tchibum."

            show screen fadolandia_tela

            pause

label fadolandia_m3nota:

    play sound "audio/som_25_passos3.mp3"

    hide screen fadolandia_tela

    scene mapa3_nota with Dissolve(2.0)

    pause

    if not fado_m3nota:

        $ fado_m3nota = True

        "O que isso aqui no meio do mato?"

        "Parece um papel..."

        if fado_m1nota or fado_m2nota:

            "É uma nota igual aquela outra que eu achei."

            "Será que é a mesma pessoa que escreveu?"

        "Tá meio apagada..."

        "Deixa eu tentar ler."

        "{i}{b}Nota do C... VI{/b}{/i}"

        "{i}A paisagem muda, o ambiente clareia e se embeleza. A água, o sol são outros.{/i}"

        "{i}Mas eu mudei? Não vejo diferenças... Então por que?{/i}"

        "{i}Minha mente não é mais minha? Não vejo mais com meus próprios olhos?{/i}"

        "{i}Ou será que estou fora da minha mente? Será que não vejo mais a minha mente, mas outras mentes?{/i}"

        "{i}Sinto que algo me puxa, me faz viajar pelas fortalezas.{/i}"

        "{i}Descobrir onde estou é imprescindível. O que é tudo isso? E por que estou sozinho?{/i}"

        "{i}Leio notas deixadas por outro, e deixo também as minhas próprias.{/i}"

        "{i}Se alguém as encontrar, saiba que ainda há como escapar.{/i}"

        "..."

        mc "Que estranho..."

        "Alguém deixou esse recado aqui. E pelo que eu entendi ele também leu a nota de outra pessoa antes dele."

        "É como se eu tivesse fazendo a mesma coisa que ele fez..."

        "Que merda de sonho é esse?"

        "Enfim... não dá pra continuar porque tá cheio de mato. Deixa eu sair daqui."

        jump fadolandia_m3a5
    else:


        "Foi aqui que eu encontrei aquele papel velho..."

        menu:
            "Reler a nota":


                "Acho que eu tenho a nota comigo aqui ainda."

                "{i}{b}Nota do C... VI{/b}{/i}"

                "{i}A paisagem muda, o ambiente clareia e se embeleza. A água, o sol são outros.{/i}"

                "{i}Mas eu mudei? Não vejo diferenças... Então por que?{/i}"

                "{i}Minha mente não é mais minha? Não vejo mais com meus próprios olhos?{/i}"

                "{i}Ou será que estou fora da minha mente? Será que não vejo mais a minha mente, mas outras mentes?{/i}"

                "{i}Sinto que algo me puxa, me faz viajar pelas fortalezas.{/i}"

                "{i}Descobrir onde estou é imprescindível. O que é tudo isso? E por que estou sozinho?{/i}"

                "{i}Leio notas deixadas por outro, e deixo também as minhas próprias.{/i}"

                "{i}Se alguém as encontrar, saiba que ainda há como escapar.{/i}"

                "..."

                "É como se eu tivesse fazendo a mesma coisa que ele fez..."

                "Que merda de sonho é esse?"

                "Enfim... não dá pra continuar porque tá cheio de mato. Deixa eu sair daqui."

                jump fadolandia_m3a5
            "Voltar para a área anterior":


                "Não tem como dar a volta no lago por aqui. Deixa eu voltar."

                jump fadolandia_m3a5

    pause

label fadolandia_m3a5:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m3a5"

    hide screen fadolandia_tela

    scene mapa3_area5 with Dissolve(2.0)

    pause

    if not fado_m3a5:

        $ fado_m3a5 = True

        "Este caminho parece mais escuro que o do outro lado."

        "Este lago é muito estranho. As árvores contornando como se estivessem protegendo tudo aqui."

        "É tipo como se alguém tivesse feito a natureza desse jeito. Ou algum agricultor tivesse arborizado tudo dessa forma."

        "Tomara que tenha alguma pista sobre tudo isso mais pra frente."

        "Pra mim, só resta continuar explorando."

    show screen fadolandia_tela

    pause

label fadolandia_m3a4:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m3a4"

    hide screen fadolandia_tela

    scene mapa3_area4 with Dissolve(2.0)

    pause

    if not fado_m3a4:

        $ fado_m3a4 = True

        "Aqui pra esquerda fica a gruta..."

        "Pra frente é impossível continuar. É árvore demais."

        "A faixa de terra é bem estreita. O lago ocupa quase todo o espaço daqui."

        "Pra chegar ali vou ter que ir contornando bem de leve e seguindo o caminho."

        "Posso tentar dar uma volta completa por aqui e ver o que eu encontro."

    show screen fadolandia_tela

    pause

label fadolandia_m3a3:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m3a3"

    hide screen fadolandia_tela

    scene mapa3_area3 with Dissolve(2.0)

    pause

    if not fado_m3a3:

        $ fado_m3a3 = True

        "Opa. Dá pra ver quase tudo daqui."

        "O lago não é tão grande, e a água realmente tá limpa. Bem diferente daquele primeiro lugar que eu vi."

        "Tem uma baita pedra ali na frente. Parece que ela tá tapando o caminho pro outro lado do lago."

        "Espera..."

        "Ali no fundo tem alguma coisa. Parece que é uma coisa construída, de cimento ou pedra, sei lá."

        "É a primeira coisa 'construída' que eu vi no sonho. Tenho que dar um jeito de chegar ali."

        "Talvez a forma mais fácil seja só nadar até lá. A outra margem não fica assim tão longe."

        "Posso dar a volta também. Só tenho que ver se dá pra cruzar aquela pedra."

        "É mais fácil andar do que ficar pensando. Vamos lá."

    show screen fadolandia_tela

    pause

label fadolandia_m3a2:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m3a2"

    hide screen fadolandia_tela

    scene mapa3_area2 with Dissolve(2.0)

    pause

    if not fado_m3a2:

        $ fado_m3a2 = True

        "Puxa. Que lugar agradável."

        "A água parece bem limpa e acho que consigo até ver o sol batendo lá na frente."

        "É uma área bem diferente do que eu já vi aqui no sonho."

        "Finalmente tô começando a me sentir melhor."

        "Acho que tô chegando em uma paz de espírito nessa merda de sonho que eu tenho quase TODA SANTA NOITE!"

        "Talvez eu consiga chegar no outro lado do lago nadando..."

        "Ou posso contornar o lago também, mas a água tá realmente bem cristalina."

        mc "Cristalina? Quem usa essa palavra?"

        "..."

    show screen fadolandia_tela

    pause

label fadolandia_m3a1:

    play sound "audio/som_25_passos3.mp3"

    $ fadolandia_mapa = "m3a1"

    hide screen fadolandia_tela

    scene mapa3_area1 with Dissolve(2.0)

    pause

    if not fado_m3a1:

        $ fado_m3a1 = True

        "Então era daqui que tava vindo o barulho da água."

        mc "É um lago."

        "Tudo em volta é árvore e elas são bem altas. É como se aqui fosse um lugar protegido."

        "O que será que eu vou encontrar aqui?"

        "Não adianta ficar pensando, bora explorar."

    show screen fadolandia_tela

    pause

label fadolandia_m2a6:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a6"

    hide screen fadolandia_tela

    scene mapa2_area6 with Dissolve(2.0)

    pause

    if not fado_m2a6:

        "Tá vindo daqui. O som de água tá vindo depois desse matagal aqui."

        "Talvez seja um rio, ou um lago ou talvez até o mar!"

        "O problema vai ser passar por aqui. Provavelmente eu vou ter que abrir uma trilha pelo mato."

        "Pior é imaginar o que pode ter no meio desse mato. Que saco..."

        menu:
            "Criar uma trilha pelo matagal e avançar":


                $ fado_m2a6 = True

                "Vai demorar, mas é o jeito."

                "O mais incrível é que tô me cansando mais dormindo que acordado."

                "Será que isso faz algum sentido?"

                "..."

                python:
                    if renpy.android:
                        renpy.block_rollback()

                scene black with Dissolve(1.0)

                play sound "extra/carta.mp3"

                "{b}[mc] gasta o resto do sonho criando uma trilha pelo matagal.{/b}"

                "{b}A partir de agora, ele poderá acessar o local sem usar toda sua energia.{/b}"

                return
            "Voltar para a área anterior":


                "Talvez depois."

                jump fadolandia_m2a4

    show screen fadolandia_tela

    pause

label fadolandia_m2cristal:





    hide screen fadolandia_tela

    "Huh? O que é isso aqui?"

    scene mapa2_cristal with Dissolve(2.0)

    pause

    "U-um negócio de vidro? Um cristal?"

    if fado_faloumaca:

        "Será que isso que o [fado] falou que precisa?"

        "E por que ele mesmo não vem aqui e pega?"

    "Eu tô com um mal pressentimento sobre isso."

    "Será que é seguro eu só pegar assim? Nem sei de quem é..."

    menu:
        "Pegar o cristal":


            python:
                if renpy.android:
                    renpy.block_rollback()

            $ fado_m2cristal = True

            "Como diria meu avô, achado não é roubado, quem perdeu foi relaxado."

            "Mas o que eu vou fazer isso aqui?"

            "Bom, agora é meu. Deixa eu pegar el-"

            scene white with dissolve

            scene inanna_leao with Dissolve(0.3)

            scene white with Dissolve(0.2)

            python:
                if renpy.android:
                    renpy.block_rollback()

            "Uou!"

            return
        "Deixar o cristal e voltar":


            "É melhor não ficar mexendo nas coisas."

            "Tenho um mal pressentimento sobre isso aqui."

            jump fadolandia_m2a4

label fadolandia_m2a5:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a5"

    hide screen fadolandia_tela

    scene mapa2_area5 with Dissolve(2.0)

    pause

    "Nem daqui eu consigo ver o que tem na gr-"

    play sound "audio/som_26_roar.mp3"

    "!"

    mc "Que porra foi essa?!"

    if mapa2_morte:

        "Pera... eu me lembro."

        "Foi outra vez que eu sonhei com isso."

        "Eu cheguei perto da gruta e um monstro de várias cabeças me atacou..."

        "Quantas vezes será que eu já sonhei com este lugar?"

    show screen fadolandia_tela

    pause

label fadolandia_m2a4:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a4"

    hide screen fadolandia_tela

    scene mapa2_area4 with Dissolve(2.0)

    pause

    if not fado_m2a4:

        $ fado_m2a4 = True

        "Acho que tô ouvindo o som de água vindo deste lado."

        "Só que tem uma porra de um matagal que não me deixa ver nada."

        "Vou ter que continuar se eu quiser saber o que tem depois desse mato todo."

    show screen fadolandia_tela

    pause

label fadolandia_m2gruta:

    play sound "audio/som_22_splash.mp3"



    hide screen fadolandia_tela

    scene mapa2_gruta with Dissolve(2.0)

    pause

    "{i}Brrr{/i}"

    "A água tá super gelada."

    "Tô começando a pensar duas vezes antes de entrar nesse lugar..."

    menu:
        "Entrar na gruta":


            "Não posso ter medo agora. Parece que alguém precisa de ajuda."

            label mapa2_morte:

                python:
                    if renpy.android:
                        renpy.block_rollback()

                play sound "audio/som_26_roar.mp3"

            scene mapa2_monstro with vpunch

            pause

            mc "AAAAAAAAAARRRRRRGGGHHHH!!"

            mc "E-eu-"

            play sound "audio/som_26_roar.mp3"

            scene mapa2_comido with vpunch

            mc "AAAAAAAAAARRRRRRGGGHHHH!!"

            if mapa2_morte:

                "E-eu já passei por isso! Eu lembro!"

            $ mapa2_morte = True

            jump fadex_errou
        "Sair da água e voltar":


            if mapa2_morte:

                jump mapa2_morte

            "Não tô gostando nem um pouco deste lugar. Deixa eu sair daqui..."

            "Desculpa, mas não tenho como te ajudar."

            jump fadolandia_m2a2



    pause

label fadolandia_m2nota:

    play sound "audio/som_24_passos2.mp3"



    hide screen fadolandia_tela

    scene mapa2_nota with Dissolve(2.0)

    pause

    if not fado_m2nota:

        $ fado_m2nota = True
        $ mapa1_precisa_ponte = True

        "O que é isso aqui?"

        if fado_m1nota:

            "Outro papel? É bem parecido com aquele outro que encontrei perto do rio."

        "{i}{b}Nota do ... VII{/b}{/i}"

        "Uma nota? Tá meio apagado. Mas acho que ainda consigo ler."

        "Hmmm..."

        "{i}{b}Nota do ... VII{/b}{/i}"

        "{i}O caminho leva para vistas infindáveis. Quão longa é a jornada que devo andar?{/i}"

        "{i}Por quantas fortalezas passei? Quantas vistas avistei?{/i}"

        "{i}Impossível contar. Impossível enumerar.{/i}"

        "{i}A viagem é demasiado cansativa, mas não me canso e nem me cansarei.{/i}"

        "{i}Algo me empurra. Algo me fortalece. Algo me leva a fazer o que tenho de fazer.{/i}"

        "{i}De onde vem esse sentimento? Essa vontade de ver?{/i}"

        "{i}O que me aguarda no fim? Uma verdade só para mim.{/i}"

        "..."

        "Acho que quem escreveu isso aqui tava começando a perder a cabeça."

        "Isso não tem nada a ver comigo. Eu tenho que continuar e descobrir algo sobre esse sonho que eu volto quase toda a noite."

        "Tô achando que a revista tá me deixando muito ansioso, sei lá."

        "..."

        "Epa! Tem outra mensagem aqui logo embaixo dessa."

        "Caralho. Essa aqui tá ainda mais difícil de ler."

        "Deixa eu ver..."

        "{i}{b}Sobre os ri... ...gos e mar...{/b}{/i}"

        mc "Quê?"

        "{i}Não ...sso esque... dos per... das ág... daqui.{/i}"

        "{i}N... encos... ... águas.{/i}"

        "{i}Exis... um tipo ... dem... ...tando as pr...ezas.{/i}"

        "Opa. A última frase dá pra ler melhor."

        "{i}Use galhos entrelaçados por fibras para formar uma ponte sobre as águas.{/i}"

        "Galhos e fibra? Interessante..."

        if fado_m1a6:

            scene mapa2_nota with vpunch

            "AAHHH!"

            "É assim que eu cruzo o rio da outra área!"

            "Aquele lugar tá cheio de árvore seca e eu já vi fibra por lá também no chão."

            "Só preciso encontrar agora um lugar que tenha bastante árvores que dê um bocado suficiente pra cruzar todo o rio."

            "Vai dar um trabalho do cão, mas vai valer à pena."

        "Acho que não tem mais nada seguindo esse caminho aqui. Melhor eu voltar."

        jump fadolandia_m2a3
    else:



        "Aquela nota estava bem por aqui..."

        menu:
            "Reler a nota":


                "Ué? Ela tá aqui comigo... mas onde que eu guardei?"

                "Hmmm..."

                "{i}{b}Nota do ... VII{/b}{/i}"

                "{i}O caminho leva para vistas infindáveis. Quão longa é a jornada que devo andar?{/i}"

                "{i}Por quantas fortalezas passei? Quantas vistas avistei?{/i}"

                "{i}Impossível contar. Impossível enumerar.{/i}"

                "{i}A viagem é demasiado cansativa, mas não me canso e nem me cansarei.{/i}"

                "{i}Algo me empurra. Algo me fortalece. Algo me leva a fazer o que tenho de fazer.{/i}"

                "{i}De onde vem esse sentimento? Essa vontade de ver?{/i}"

                "{i}O que me aguarda no fim? Uma verdade só para mim.{/i}"

                "..."

                "Continuo achando a mesma coisa... doidera..."

                jump fadolandia_m2a3
            "Voltar para a área anterior":


                "..."

                jump fadolandia_m2a3

label fadolandia_m2a3:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a3"

    hide screen fadolandia_tela

    scene mapa2_area3 with Dissolve(2.0)

    pause

    if not fado_m2a3:

        $ fado_m2a3 = True

        "Dá pra ouvir alguma coisa lá longe."

        "Talvez seja algum tipo de pássaro."

        "A vegetação tá começando a crescer. Como se eu tivesse chegando perto de uma floresta."

        "Não sei se eu devo continuar andando pra cá."

        "Tudo parece mais escuro e mais denso por aqui. Tô meio com medo do que tem pra frente..."

        "[mc] seu cagão..."

    show screen fadolandia_tela

    pause

label fadolandia_m2a2:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a2"

    hide screen fadolandia_tela

    scene mapa2_area2 with Dissolve(2.0)

    pause

    if not fado_m2a2:

        $ fado_m2a2 = True

        "Hmmm..."

        "Então realmente é uma gruta."

        play sound "audio/som_18_gotas.mp3"

        "Dá pra escutar o som da água pingando no fundo."

        "Uma pena que eu não consiga ver direito o que tem lá dentro. O lugar é super escuro."

        "Estranho... Parece que tem algo me chamando lá dentro. Como se alguém tivesse precisando de ajuda."

        "Mas será que é seguro entrar num lugar assim?"

        "Droga..."

    show screen fadolandia_tela

    pause

label fadolandia_m2a1:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m2a1"

    hide screen fadolandia_tela

    scene mapa2_area1 with Dissolve(2.0)

    pause

    if not fado_m2a1:

        $ fado_m2a1 = True

        "Ufa... Que caminhada."

        "Hmmm..."

        "O entorno deu uma boa mudada. Parece bem mais... vivo..."

        "As flores, o mato. Até as árvores aqui tem folhas."

        "O que será que aconteceu com aquela outra região?"

        "A floresta perto da casa da [p] era mais parecida com este lugar aqui."

        "Enfim... pra onde eu vou agora?"

    show screen fadolandia_tela

    pause

label fadolandia_m1a6:

    play sound "audio/som_24_passos2.mp3"

    $ fadolandia_mapa = "m1a6"

    hide screen fadolandia_tela

    if not fadolandia_m1ponte:

        scene mapa1_area6 with Dissolve(2.0)
    else:


        scene mapa1_ponte with Dissolve(2.0)

    pause

    if not fado_m1a6:

        $ fado_m1a6 = True

        if mapa1_morte:

            "Engraçado... eu sinto que eu já sonhei com este lugar antes."

            "Eu tentei atravessar esse rio, mas ali mais pra cima."

            "Uma coisa saiu e me puxou... caraca...."

            mc "Deu até um arrepio agora."

        "Acho que o melhor é tentar chegar do outro lado por aqui. Mesmo o rio sendo mais largo..."

        "Só que não dá pra ir nadando. Vai saber o que tem no meio dessa água."

        "Preciso pensar em uma forma de atravessar aqui sem entrar na água. Tipo uma ponte..."

        "Onde que raios eu vou achar uma ponte?"

        "Calma! Isso aqui é meu sonho! É só eu pensar e ela vai aparecer."

        show black with dissolve

        "Olhos fechados..."

        "Agora é só pensar em uma ponte..."

        "Quando eu abrir os olhos vai ter uma ponte de madeira que vai permitir que eu atravesse o rio."

        "AGORA!"

        hide black with dissolve

        "..."

        "É. Pelo jeito não vai funcionar."

        "Mano! Nem pra sonhar direito! Eu sou um inútil!"

        "{i}Cof cof{/i}"

        "Vou ter que encontrar outra forma de cruzar o rio."

    elif not mapa1_precisa_ponte:

        "Tenho que dar um jeito de chegar até o outro lado do rio, mas sinto que é perigoso demais ir nadando."

        "Preciso encontrar uma forma de atravessar..."

    if mapa1_precisa_ponte and not fadolandia_m1ponte:

        "Segundo aquela nota que eu encontrei, é possível improvisar uma ponte usando galhos..."

        if not fadolandia_galhos:

            "Agora preciso encontrar um lugar que eu possa pegar galhos suficientes."

            "Tá cheio de árvore seca por aqui. Provavelmente se eu procurar bem por aqui eu acho."
        else:


            "Consegui galhos e um tanto de fibra pra amarrar tudo."

            "Tô pronto pra atravessar essa merda de rio."

    menu:

        "Cruzar a ponte e ir para a caverna" if fadolandia_m1ponte:

            jump fadolandia_m4a1

        "Improvisar uma ponte até o outro lado do rio" if fadolandia_galhos and not fadolandia_m1ponte:

            python:
                if renpy.android:
                    renpy.block_rollback()

            $ fadolandia_m1ponte = True

            "Consegui galhos e fibra suficientes. Agora tenho que mandar ver."

            "..."

            "..."

            scene black with Dissolve(1.0)

            "Agora prendo bem forte..."

            "..."

            "Pronto!"

            "Agora é só empurrar até o outro lado."

            "E..."

            scene mapa1_ponte with Dissolve(2.0)

            pause

            mc "Ahaaa! Ficou perfeito!"

            "Pelo menos olhando daqui parece perfeito..."

            "E a coragem pra passar por essa ponte agora?"

            "Pensando bem... é só um sonho. O que pode acontecer?"

            scene black with dissolve

            "Opa."

            "..."

            "..."

            python:
                if renpy.android:
                    renpy.block_rollback()

            jump fadolandia_m4a1
        "Se afastar do rio":


            "Depois eu volto."

            jump fadolandia_m1a5

    show screen fadolandia_tela

    pause

label fadolandia_m1nota:

    play sound "audio/som_23_passos1.mp3"



    hide screen fadolandia_tela

    scene mapa1_nota with Dissolve(2.0)

    pause

    if not fado_m1nota:

        $ fado_m1nota = True

        "Epa. Tem um papel aqui."

        "Deixa eu ver..."

        "Tá meio apagado, mas eu consigo entender. Interessante que eu não sei exatamente que idioma tá escrito, mas eu consigo entender..."

        "Tem coisa que só faz sentido em sonho mesmo."

        "{i}{b}Nota do ... V{/b}{/i}"

        "{i}Longe da minha fortaleza, me vejo despido das seguranças. A zona de conforto ficou há muito para trás.{/i}"

        "{i}Ando, navego, voando, viajo...{/i}"

        "{i}Uma terra arrasada, deixada por quem? De quem seria esta fortaleza?{/i}"

        "{i}Quanto mais viajo, mais difícil é retornar. Mais tempo viajo, menos tempo vivo.{/i}"

        "{i}Outros teriam percorrido o mesmo caminho? Retornaram? Desapareceram?{/i}"

        "{i}Agora é tarde. Não importa. Este é meu caminho. Eu sou um Viajor.{/i}"

        "..."

        mc "Quê?"

        "Nota... uma nota deixada por alguém."

        "Quer dizer que alguém passou por aqui antes de mim... deve fazer um bom tempo já. O papel tá bem velho."

        "Tô sem saco pra pensar nessa besteira agora. Deu até vontade de acordar. Será que falta muito pra acabar isso aqui?"

        "..."

        jump fadolandia_m1a5
    else:


        "Foi aqui que eu encontrei aquele papel velho..."

        menu:
            "Reler a nota":


                "Acho que eu tenho a nota comigo aqui ainda."

                "{i}{b}Nota do C... V{/b}{/i}"

                "{i}Longe da minha fortaleza, me vejo despido das seguranças. A zona de conforto ficou há muito para trás.{/i}"

                "{i}Ando, navego, voando, viajo...{/i}"

                "{i}Uma terra arrasada, deixada por quem? De quem seria esta fortaleza?{/i}"

                "{i}Quanto mais viajo, mais difícil é retornar. Mais tempo viajo, menos tempo vivo.{/i}"

                "{i}Outros teriam percorrido o mesmo caminho? Retornaram? Desapareceram?{/i}"

                "{i}Agora é tarde. Não importa. Este é meu caminho. Eu sou um Viajor.{/i}"

                "Viajor... o cara tava viajado mesmo quando escreveu essa viagem toda."

                "Não adianta quebrar a cabeça por isso. Não lembro se eu bebi muito ontem..."

                "..."

                jump fadolandia_m1a5
            "Voltar para a área anterior":


                "Não tem nada de interessante aqui. Deixa eu voltar."

                jump fadolandia_m1a5

    pause

label fadolandia_m1a5:

    play sound "audio/som_23_passos1.mp3"

    $ fadolandia_mapa = "m1a5"

    hide screen fadolandia_tela

    scene mapa1_area5 with Dissolve(2.0)

    pause

    if not fado_m1a5:

        $ fado_m1a5 = True

        "A casa da [p] fica depois daquelas árvores."

        "Tenho que aproveitar o tempo que ela não vai me receber pra descobrir mais sobre tudo isto."

        "A [p] inclusive parecia incomodada com o fato de eu visitar este lugar."

        "Será que tem algo que ela não quer que eu encontre?"

    show screen fadolandia_tela

    pause

label fadolandia_m1a4:

    play sound "audio/som_23_passos1.mp3"

    $ fadolandia_mapa = "m1a4"

    hide screen fadolandia_tela

    scene mapa1_area4 with Dissolve(2.0)

    pause

    if not fado_m1a4:

        "Tem alguma coisa depois desse morro."

        "Parece uma montanha... não... tem uma abertura. Talvez uma gruta..."

        "Eu tenho a impressão que o rio tá vindo dalí."

        "O caminho até lá parece bem complicado. Não vai ser fácil."

        "Mas talvez eu acabe encontrando alguma coisa lá que me ajude a entender melhor tudo isso aqui."

        "Se a água realmente tá vindo de lá, certeza que tem caroço nesse angu."

        menu:
            "Ir até a gruta":


                $ fado_m1a4 = True

                "Vai demorar, mas é o jeito."

                "O mais incrível é que tô me cansando mais dormindo que acordado."

                "Será que isso faz algum sentido?"

                "..."

                python:
                    if renpy.android:
                        renpy.block_rollback()

                scene black with Dissolve(1.0)

                play sound "extra/carta.mp3"

                "{b}[mc] gasta o resto do sonho e encontra o melhor caminho até a gruta.{/b}"

                "{b}A partir de agora, ele poderá acessar o local sem usar toda sua energia.{/b}"

                return
            "Voltar para a área anterior":


                "Talvez depois."

                jump fadolandia_m1a3

    show screen fadolandia_tela

    pause

label fadolandia_m1galho:

    hide screen fadolandia_tela

    scene mapa1_mc_galho with Dissolve(2.0)

    pause

    if mapa1_precisa_ponte:

        "Hmmm... acho que eu tava certo. Provavelmente dá pra fazer tipo uma ponte se eu conseguir galhos o suficiente."

        "Vai demorar um tempo, mas é a única forma de atravessar o rio sem entrar na água."

    elif fadolandia_galhos:

        "Eu já peguei todos os galhos que eu precisava."

        "Espero nunca mais ter que voltar aqui de novo pegar essa MERDA."
    else:


        "Tem uma porrada de galhos aqui."

        "Mas eu não preciso deles pra nada."

        "E por que alguém ia precisar de galhos na vida dela? Que sonho doido..."

    menu:

        "Coletar galhos" if mapa1_precisa_ponte and not fadolandia_galhos:

            "Eu vou precisar de uma porrada de galhos..."

            "Não tem jeito. Bora trabalhar."

            "..."

            python:
                if renpy.android:
                    renpy.block_rollback()

            $ fadolandia_galhos = True

            "{b}[mc] gasta o resto do sonho coletando galhos.{/b}"

            scene black with dissolve

            play sound "extra/carta.mp3"

            show fadolandia_galho with dissolve

            pause

            "{b}[mc] conseguiu uma porrada de galhos.{/b}"

            "{b}A quantidade é suficiente para ser usada em uma ponte improvisada.{/b}"

            return
        "Voltar para a área anterior":


            "Não tenho porque ficar aqui. Deixa eu voltar."

            jump fadolandia_m1a3

label fadolandia_m1a3:

    play sound "audio/som_23_passos1.mp3"

    $ fadolandia_mapa = "m1a3"

    hide screen fadolandia_tela

    scene mapa1_area3 with Dissolve(2.0)

    pause

    if not fado_m1a3:

        $ fado_m1a3 = True

        "Aqui o rio é bem mais largo."

        "É meio estranho como a água aqui tem uma cor diferente."

        "Eu lembro que a água naquele rio que passava perto da casa da [p] não tinha essa cor."

        "E o ar também. Tudo aqui parece diferente, como se fosse uma áura totalmente diferente."

        "É como se eu me sentisse em casa lá e aqui é como se eu saísse pelado em um lugar desconhecido."

        "Pensando bem... eu tô quase pelado em um lugar estranho."

        mc "Meu sentimento é mais literal do que eu imaginava..."

    show screen fadolandia_tela

    pause

label fadolandia_m1rio:

    play sound "audio/som_24_passos2.mp3"



    hide screen fadolandia_tela

    scene mapa1_mc_rio with Dissolve(2.0)

    pause

    "Neste ponto a água é rasa."

    "Eu posso cruzar o rio por aqui sem problemas. Assim dá pra chegar até a floresta do outro lado."

    "A água também parece comum. Não tem cheiro nenhum. Só tá bem gelada."

    menu:
        "Cruzar o rio andando":


            python:
                if renpy.android:
                    renpy.block_rollback()

            "Tenho que investigar este lugar ao máximo. Aquela floresta é minha melhor chance."

            "Deix-"

            label mapa1_morte:

                play sound "audio/som_22_splash.mp3"

            scene mapa1_monstro with vpunch

            pause

            mc "O-o que é isso?!"

            "???" "..."

            mc "P-por-"

            play sound "audio/som_22_splash.mp3"

            scene mapa1_afogado with vpunch

            mc "O qu-"

            "Não!"

            if mapa1_morte:

                "E-eu já passei por isso! Eu lembro!"

            $ mapa1_morte = True

            jump fadex_errou
        "Voltar para a área anterior":


            if mapa1_morte:

                jump mapa1_morte

            "Quem sabe depois..."

            jump fadolandia_m1a2



    pause

label fadolandia_m1a2:

    play sound "audio/som_23_passos1.mp3"

    $ fadolandia_mapa = "m1a2"

    hide screen fadolandia_tela

    scene mapa1_area2 with Dissolve(2.0)

    pause

    if not fado_m1a2:

        $ fado_m1a2 = True

        "Opa. Um rio. Não dava pra ver isso lá de trás."

        "E lá pra frente parece que tem uma floresta, mas tá com bastante neblina."

        "Eu acho que pra lá deve ser mais parecido com o lugar onde a [p] vive."

        "Tenho que dar um jeito de sair deste lugar o mais rápido possível."

        "Quanto mais tempo eu fico aqui, mais parece que eu vou encontrar alguma coisa que eu não quero."

        "É... realmente uma sensação muito estranha."

    show screen fadolandia_tela

    pause

label fadolandia_m1a1:

    play sound "audio/som_23_passos1.mp3"

    $ fadolandia_mapa = "m1a1"

    hide screen fadolandia_tela

    scene mapa1_area1 with Dissolve(2.0)

    pause

    if not fado_m1a1:

        $ fado_m1a1 = True

        "..."

        "Este lugar é bem diferente de onde fica a casa da [p]."

        "Parece super desolado e eu tô sentindo umas vibes estranhas vindo daqui."

        "Parece... que eu não tô sozinho."

        "{i}Brrrrr{/i}"

        "Que arrepio."

        "Droga. Além de tudo o lugar ainda parece imenso."

        "Esse sonho tá quase virando um pesadelo... literalmente..."

        window hide

    show screen fadolandia_tela

    pause

label fadolandia_acordar:

    hide screen fadolandia_tela

    "Por algum motivo que eu não entendo, eu posso acordar do sonho na hora que eu quero."

    menu:
        "Acordar":


            python:
                if renpy.android:
                    renpy.block_rollback()

            "Tá bom por agora. Vou acordar."

            "Outra hora eu continuo esse sonho doido. Não posso desistir até eu chegar ao final disso tudo."

            scene black with dissolve

            return
        "Continuar sonhando":


            "Ainda tenho o que fazer aqui. Não vou acordar agora."

            show screen fadolandia_tela

            pause

screen fadolandia_tela():
    tag fadolandia

    predict False
    zorder 100
    modal True

    imagebutton auto "extra/botao_acordar_%s.png":
        xalign 0.955
        yalign 0.99
        xanchor 0.5
        action Jump("fadolandia_acordar")

    if fadolandia_mapa == "m1a1":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate315
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a3")

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.5
            yalign 0.60
            xanchor 0.5
            action Jump("fadolandia_m1a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a5")

    if fadolandia_mapa == "m1a2":

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.5
            yalign 0.55
            xanchor 0.5
            action Jump("fadolandia_m1rio")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m1a1")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a3")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a6")

    if fadolandia_mapa == "m1a3":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m1galho")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a4")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate135
            xalign 0.95
            yalign 0.85
            xanchor 0.5
            action Jump("fadolandia_m1a1")

    if fadolandia_mapa == "m1a4":

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.54
            yalign 0.29
            xanchor 0.5
            action Jump("fadolandia_m2a1")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m1a3")

    if fadolandia_mapa == "m1a5":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m1a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m1a6")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate315
            xalign 0.20
            yalign 0.28
            xanchor 0.5
            action Jump("fadolandia_m1nota")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate135
            xalign 0.95
            yalign 0.85
            xanchor 0.5
            action Jump("fadolandia_m1a1")

    if fadolandia_mapa == "m2a1":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a3")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.35
            yalign 0.35
            xanchor 0.5
            action Jump("fadolandia_m2a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a4")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m1a4")

    if fadolandia_mapa == "m2a2":

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.45
            yalign 0.6
            xanchor 0.5
            action Jump("fadolandia_m2gruta")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a5")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m2a1")

    if fadolandia_mapa == "m2a3":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.45
            yalign 0.35
            xanchor 0.5
            action Jump("fadolandia_m2nota")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m2a1")

    if fadolandia_mapa == "m2a4":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a5")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate315
            xalign 0.30
            yalign 0.17
            xanchor 0.5
            action Jump("fadolandia_m2a6")

        if not fado_m2cristal:

            imagebutton auto "extra/botao_seta_%s.png":
                at rotate90
                xalign 0.95
                yalign 0.5
                xanchor 0.5
                action Jump("fadolandia_m2cristal")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m2a1")

    if fadolandia_mapa == "m2a5":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m2a4")

    if fadolandia_mapa == "m2a6":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.45
            yalign 0.40
            xanchor 0.5
            action Jump("fadolandia_m3a1")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m2a4")

    if fadolandia_mapa == "m3a1":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m3a4")

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.5
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m3a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m3a5")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m2a6")

    if fadolandia_mapa == "m3a2":

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.5
            yalign 0.55
            xanchor 0.5
            action Jump("fadolandia_m3lago")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.55
            xanchor 0.5
            action Jump("fadolandia_m3a3")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate135
            xalign 0.95
            yalign 0.7
            xanchor 0.5
            action Jump("fadolandia_m3a5")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m3a1")

    if fadolandia_mapa == "m3a3":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.20
            yalign 0.55
            xanchor 0.5
            action Jump("fadolandia_m3pedra")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.7
            xanchor 0.5
            action Jump("fadolandia_m3a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.95
            yalign 0.3
            xanchor 0.5
            action Jump("fadolandia_m3lago")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate225
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m3a4")

    if fadolandia_mapa == "m3a4":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m3a3")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate45
            xalign 0.95
            yalign 0.1
            xanchor 0.5
            action Jump("fadolandia_m3pedra")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate180
            xalign 0.5
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m3a1")

    if fadolandia_mapa == "m3a5":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate135
            xalign 0.95
            yalign 0.8
            xanchor 0.5
            action Jump("fadolandia_m3a1")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate315
            xalign 0.17
            yalign 0.26
            xanchor 0.5
            action Jump("fadolandia_m3nota")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate225
            xalign 0.3
            yalign 0.95
            xanchor 0.5
            action Jump("fadolandia_m3a2")

    if fadolandia_mapa == "m4a1":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.25
            yalign 0.9
            xanchor 0.5
            action Jump("fadolandia_m4a2")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate135
            xalign 0.8
            yalign 0.7
            xanchor 0.5
            action Jump("fadolandia_m1a6")

    if fadolandia_mapa == "m4a2":

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate270
            xalign 0.05
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m4sangue")

        imagebutton auto "extra/botao_seta_%s.png":
            xalign 0.53
            yalign 0.58
            xanchor 0.5
            action Jump("fadolandia_m4a3")

        imagebutton auto "extra/botao_seta_%s.png":
            at rotate90
            xalign 0.95
            yalign 0.5
            xanchor 0.5
            action Jump("fadolandia_m4a1")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
