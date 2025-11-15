label sofia_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("so1_save", extra_info="so1_save")

    $ sofia_e1 = "iniciado"

    "Tô me sentindo cansado ultimamente."

    "Já entreguei algumas pautas pro chefe. Nem acredito que ainda não fui despedido."

    "Tô conseguindo fazer bem meu trabalho como paparazzo. A pena é ter que entregar segredos das pessoas que eu conheço."

    "Algumas das coisas que eu descubro, eu só fico sabendo porque elas confiaram em mim a ponto de revelar."

    "E entregar isso pro chefe, só pra poder ganhar essa grana que paga meu aluguel e a pizza."

    "Sei lá. Parece que eu sou tipo Judas, vendendo meus amigos por umas moedas de ouro."

    "Será que se eu continuar assim eu vou acabar igual a [j]?"

    w "{size=17}Não, pai! Tá tudo errado!{/size}"

    w "{size=17}Se as coisas continuarem assim, o que vai ser da revista?{/size}"

    b "{size=17}De que merda você tá falando?! Tá tudo certo com a revista, menina!{/size}"

    w "{size=17}Você chama isso de certo?{/size}"

    mc "Ah?"

    "Que merda que tá acontecendo? Parece que o chefe tá brigando com alguém na cozinha."

    "Será que a [j] sabe alguma coisa?"

    menu:
        "Se aproximar da cozinha":


            "Deixa a [j] pra lá. Deixa eu mesmo ver o que tá rolando."

            "..."

            scene trabalho angulo with Dissolve(1.0)

            "Eles ainda tão brigando."

            b "{size=17}Eu tô fazendo o que eu posso. A revista cresceu muito em circulação, mesmo com a constante queda da mídia impressa.{/size}"

            b "{size=17}Até mesmo a [cc] veio reclamar da revista. Estamos chamando a atenção.{/size}"

            w "{size=17}Isso é um feito, pai. Meus parabéns. Mas os fins não justificam os meios.{/size}"
        "Perguntar pra [j]":


            "Deixa eu ir ver com ela. Provavelmente a [j] sabe mais do que eu. Porque a merda tá tensa."

            "..."

            scene trabalho cassia with Dissolve(1.0)

            mc normal "[j]. Beleza?"

            j "Oi, pombinho."

            mc desconfiado "Que que tá acontecendo?"

            j "Ah. É a chefinha."

            mc "Chefinha?"

            j "A filha do careca."

            mc surpreso "A filha do chefe tá brigando com ele?!"

            j "Fica quieto, bebê."

            mc envergonhado "Ops, malz."

            j "Ela estava estudando fora, mas pelo jeito acabou de voltar. Eu não sei mais que isso."

            j "Só que mesmo antes de acabar a faculdade, ela já botava uma banca aqui."

            mc desconfiado "Falar com o chefe desse jeito. Essa menina tem coragem."

            j "Não concordo. Pra mim, ela é só uma garota mimada."

            j "Se eu fosse você ficava longe deles. Você não vai querer se envolver nessa história."

            mc desconfiado "Hmm..."

            "Deixa eu ver o que tá rolando agora."

    scene sofia brigando_chefe with Dissolve(2.0)

    pause

    w "As coisas estão todas erradas aqui na revista! Não é possível que você aceite as coisas dessa forma!"

    b "Olha como você fala comigo, fedelha!"

    w "Tô mentindo?! Olha pra isso aqui!"

    w "Olha aqui. Essa tal de [jc]!"

    if v4_fim and not cassia_aceitou:

        w "Ela escreveu que a modelo [cc] tá de caso com um jornalista da nossa revista!"

        w "Ela não tem prova nenhuma. Só uma foto dos dois juntos!"

        w "Não tem uma resposta, uma entrevista. Só uma foto que não prova nada!"

    if v9_fim:

        w "Publicou que o [nc] está ilegalmente no país. Você acha que tá certo fazer isso com esse sensacionalismo?!"

    w "Tudo o que essa mulher publica é questionável!"

    b "A [j] é uma das nossas principais peças. Tudo o que ela escreve ganha mídia. E ela é uma jornalista investigativa de alto gabarito!"

    w "Você só pode tá maluco, pai! Investigativo?! Você esqueceu o que aprendeu na faculdade?!"

    b "Que faculdade, pirralha?! Quando eu comecei no jornalismo ainda não existia faculdade disso."

    b "Você pode ficar com suas teorias e seu pseudo conhecimento, mas aqui MANDO EU!"

    scene trabalho chefe_porta with hpunch

    mc surpreso "!"

    "Maluco! Ele tá puto mesmo."

    show sofia meudeus with dissolve

    w "Velho cabeça dura."

    w "As coisas não vão ser mais como ele tá achando."

    hide sofia with dissolve

    "Opa. Ela tá vindo pra cá."

    menu:
        "Voltar pra mesa":


            $ sofia_amizade += 1

            "Melhor eu sair daqui."

            "Não quero que meu primeiro contato com ela seja assim."
        "Ficar parado e esperar ela passar":


            "Tô louco pra falar com essa garota. Melhor já fazer amizade com a maior rival do chefe."

            scene trabalho angulo with Dissolve(1.0)

            "Aí vem ela."

            show sofia seria with dissolve

            w "Com licença."

            mc normal "Boa tarde."

            w "Desculpa meus modos. Mas eu preciso trabalhar."

            hide sofia with dissolve

            mc envergonhado "Tudo certo..."

            "Bem... não é o primeiro contato que eu esperava, mas pelo menos ela me viu."
    "..."

    scene trabalho mesa with Dissolve(1.0)

    "Essa garota... ela parece nova, mas se ela terminou a faculdade de jornalismo então ela tem pelo menos uns 21 anos."

    "E a forma que ela falou com o chefe. Só ele mesmo pra não ceder. O velho é casca grossa igual a filha."

    "Então quer dizer que agora ela vai trabalhar aqui na redação também. Isso com certeza vai deixar as coisas mais interessantes."

    mc "Só espero que não seja outra [j] pra foder minha vida."

    "Eu queria poder falar com ela... Só que cadê a coragem?"

    "Não, [mc]. Você conheceu várias pessoas. Você não tem mais medo de mulher igual antigamente."

    "Ela não vai fazer nada com você. Só levante e vá falar com ela."

    mc "Certo."

    scene trabalho angulo with Dissolve(1.0)

    "A mesa dela fica bem na frente da minha."

    "..."

    scene trabalho sofia with Dissolve(2.0)

    pause

    mc normal "Oi."

    w "Oi. Você precisa de algo?"

    "Tá na cara, literalmente, que eu tô incomodando ela. Droga, eu não pensei o que eu ia falar."

    menu:
        "Desde que eu vi você, não parei de olhar. Você é linda.":


            mc charmoso "Desculpa por ser direto, mas eu aprendi que não adianta a gente ficar enrolando pra falar as coisas."

            w "?"

            mc "Desde que eu vi você, não consegui parar de olhar. Você é realmente muito linda."

            w "Quê?"

            mc "Só queria que você soubesse isso."

            w "Você sabia que falar isso pra mim dessa forma é considerado assédio?"

            mc preocupado "Não. Não foi minha intenção te assediar."

            w "Ai ai..."
        "Tem muita coisa errada na redação.":


            $ sofia_amizade += 1

            mc desculpa "Só queria que você soubesse que eu concordo com você. Tem muita coisa errada aqui na redação."

            w "Como?"

            mc envergonhado "Ah. Perdão. Eu acabei ouvindo você brigando com o chefe. Daí-"

            w "Ah, sim. Então você concorda?"

            mc desculpa "É uma pena, mas concordo."
        "Você não quer fazer uma pausa e tomar algo?":


            mc normal "Tava pensando aqui... Quer fazer uma pausa e tomar alguma coisa?"

            w "Obrigada. Eu tenho tudo o que eu preciso. Meu café."

    w "Vejo que eu vou ter muito trabalho aqui na revista."

    w "Olha, eu realmente não tenho tempo pra jogar conversa fora. Eu acabei de chegar e preciso arrumar tudo."

    w "Eu não quero ser grossa com você, mas a gente não vai se falar muito. Só o que for estritamente relacionado ao trabalho."

    w "Posso contar com sua ajuda nisso?"

    "Acho que ela quer dizer que não é pra eu encher o saco dela de uma forma sutil e educada..."

    menu:
        "Pode contar comigo.":


            mc normal "Pode deixar."

            w "Obrigada."
        "Relaxa. Eu entendo quando alguém me dá o fora.":


            $ sofia_amizade += 1

            mc envergonhado "Relaxa. Eu consigo ver quando alguém tá me dando o fora. Pode deixar que não vou incomodar mais."

            w "Não. Não é uma indireta. Perdão."

            w "Um bom relacionamento entre os profissionais de uma equipe é essencial para o desenvolvimento de um bom trabalho."

            mc desconfiado "?"

            w "Pode falar comigo quando achar necessário. Mas tente falar apenas o estritamente necessário."

            mc "Combinado."

    w "..."

    mc envergonhado "Qualquer coisa tô aqui na mesa."

    w "Ok."

    scene trabalho angulo with Dissolve(1.0)

    "Que primeira impressão horrível. Ela deve me achar um idiota."

    w "Ei."

    mc desconfiado "?"

    show sofia falando with dissolve

    w "Olha. Manter um bom clima no local de trablho é imperativo para um bom resultado em equipe."

    mc "..."

    w "Eu queria... é..."

    $ w_nome = "Sofia"

    show sofia ironica with dissolve

    w "Meu nome é [w]. Muito prazer."

    mc normal "Eu sou o [mcc]. Mas pode me chamar de [mc]."

    w "Ok, [mc]. E desculpa qualquer coisa."

    mc "De boa, [w]."

    menu:
        "Agora vamos voltar ao trabalho.":


            $ sofia_amizade += 1

            mc normal "Bom, hora de voltar ao tabalho."

            show sofia falando with dissolve

            w "Isso aí."

            hide sofia with dissolve
        "E o que você acha de tomar algo agora?":


            mc charmoso "E o que você acha da gente tomar alguma coisa agora, então? Melhorar nossa convivência no trabalho."

            show sofia meudeus with dissolve

            w "Você... deixa pra lá."

            hide sofia with dissolve

            mc envergonhado "Bom... não custava tentar..."

    scene trabalho mesa with Dissolve(1.0)

    "Essa [w] é bem gata. Mas ela parece impenetrável. Como eu vou conseguir quebrar esse gelo entre a gente?"

    "Ela é a filha do chefe... Imagina o rolo se eu ficasse com ela."

    mc tarado "Ia ser demais."

    "Não adianta ficar viajando. Não tenho mais ideias pra hoje. Melhor dar o fora."

    $ dia_sofia = dia + 1
    $ tempo += 1

    jump call_cidade

label sofia_evento2:

    $ sofia_dia = dia + 1

    w "Perfeito."

    w "Eu tenho uma série de afazeres aqui pra você. Você já pode começar agora."

    mc zerado "{size=17}Por que eu aceitei isso?{/size}"

    scene trabalho angulo with Dissolve(1.0)

    show sofia invocada with dissolve

    w "O que você disse?"

    mc envergonhado "Eu?"

    menu:
        "Nada, não!":


            $ sofia_amizade += 1

            mc envergonhado "Não disse nada, não!"

            w "Hmm..."

            w "Se você realmente quiser me ajudar, preciso que você leve isso a sério."

            w "Eu realmente quero mudar as coisas aqui."

            mc "Entendo entendo. Pode deixar."
        "Tô pensando se eu realmente quero mais trabalho.":


            mc desconfiado "Tô pensando aqui se eu realmente preciso trabalhar mais ainda..."

            show sofia ironica with dissolve

            w "Não me estranharia se você não aguentasse..."

            mc serio "Ei!"

            w "Que foi?"

            mc "Eu não disse que vou desistir. Mas você é muito mandona."

            w "Mandona ou eficiente?"

            mc "Mandona mesmo."

    show sofia falando with dissolve

    w "A gente se conhece a pouco tempo, mas pelo que eu ouvi você tá é muito mal acostumado."

    mc desconfiado "Hm?"

    w "Eu sei que você tem se dado muito bem com as celebridades. Outros repórteres dizem que você consegue pautas se vendendo."

    mc "Me vendendo? Como assim? Quem disse isso?"

    w "Não quero ser dedo duro, mas você tem trazido pautas realmente incríveis ultimamente. E claro que isso desperta certa... inveja."

    w "Eu não gosto de fofoca, por isso estou tentando falar da forma mais profissional possível."

    w "Dizem que você deita com celebridades, que se vende pra elas em troca de pautas."

    menu:
        "Isso é só inveja. Obviamente é mentira.":


            $ sofia_amizade += 1

            mc envergonhado "Como você mesmo disse, isso é só inveja."

            mc "Eu nunca fiz essas coisas com nenhuma celebridade pra pegar pautas."

            w "Sério mesmo?"

            mc "Claro."

            w "Tá."
        "Você tá louca?! Eu nunca faria isso!":


            $ sofia_amizade += 2

            mc bravo "Você tá louca?! Acha que eu faria coisas assim só pra se manter no emprego!?"

            w "!"

            mc "..."

            show sofia rindo with dissolve

            w "É isso que eu espero de você."

            w "Esse tipo de asco contra o que é errado."

            w "É com esse espírito que a gente vai mudar tudo aqui e transformar a redação em um lugar muito melhor."

            mc concentrando "Ok, mas não precisa me acusar assim."

            w "Desculpa..."
        "Quem sabe?":


            mc safado "Quem sabe? Isso não diz respeito a vocês..."

            mc "Meu trabalho é trazer pautas, não importa como eu consigo."

            show sofia seria with dissolve

            w "Isso é muito sério. Você sabe que eu estou tentando mudar como as coisas funcionam por aqui."

            w "Se eu não puder confiar nem em você como uma pessoa que quer algo melhor também, não sei como vai ficar."

            mc desculpa "..."

    w "Bom, acho que eu fugi um pouco do assunto."

    show sofia explicando with dissolve

    w "Nosso trabalho vai ser de conferir TODAS as informações antes de serem publicadas."

    mc surpreso "Todas as matérias da revista?!"

    w "Não. Todas as matérias da revista E do site também."

    mc "!!!"

    mc "Como isso vai ser possível?!"

    w "Por isso que eu preciso de ajuda."

    mc zerado "Mas só nós dois-"

    show sofia seria with dissolve

    w "Você quer desistir antes de começar?"

    mc preocupado "Não é isso. Mas você não tá sendo razoável..."

    w "E daí que dezenas de matérias são publicadas todos os dias? Vamos passar o dia todo lendo se for preciso."

    mc triste "Isso é loucura..."

    w "Você vai querer participar ou não?"

    menu:
        "É... Ok...":


            $ sofia_amizade += 1

            mc concentrando "Ma-mas... ok... vou participar."

            mc normal "Pode contar comigo."

            w "Era o mínimo que eu esperava de você."

            w "Temos muito trabalho pra fazer aqui."

            mc "Nós vamos conseguir. Só mantermos o foco."
        "Será que não é melhor ajudarmos de outra forma?":


            mc envergonhado "Será que não seria melhor ajudar de outro jeito?"

            w "Por que outro jeito?"

            mc "É um pouco complicado demais a gente conferir tudo de tudo."

            w "Você já tá desistindo antes de começar? Esperava mais de você."

            mc desculpa "Não é isso. É que..."

            mc concentrando "Deixa pra lá."

            mc normal "Eu disse que ia ajudar, então vou ajudar."

            w "Obrigada."
        "Claro! O que você quiser, chefinha!":


            mc envergonhado "Com certeza! O que você achar melhor, tô dentro, chefinha!"

            w "Você tá me zoando?"

            mc "Cl-claro que não! Eu nunca faria isso!"

            w "Estou de olho em você..."

            mc "Só quero que você saiba que eu confio no seu julgamento."

            w "Tá..."

    show sofia meudeus with dissolve

    w "Ufa. Que bom que a gente se entendeu nisso."

    w "Eu estava achando que ia sobrar tudo pra mim. Estava tão nervosa com is-"

    show sofia falando with dissolve

    w "Quero dizer... o que eu sinto não importa. Aqui é trabalho."

    mc desculpa "Eu sei, mas você pode confiar em mim, tá? Não acho que você tem que ser um robô também."

    if sofia_e1_massageou:

        w "Olha, eu sei que na outra noite você... ma-massageou meu pé, mas não quero que isso signifique mais do que significou."

        w "Digo... não quero que você fique pensando coisas."

        mc envergonhado "Eu não tô pensando nada. Aquela noite eu só queria te ajudar."

        w "E você me ajudou, mas agora tudo continua como antes."

        mc "Ok... entendi..."

        w "..."

    elif sofia_confiou:

        w "Olha, eu sei que na outra noite você foi legal comigo e tudo, mas não quero que isso signifique mais do que significou."

        w "Digo... não quero que você fique pensando coisas."

        mc envergonhado "Eu não tô pensando nada. Aquela noite eu só queria te ajudar."

        w "E você me ajudou, mas agora tudo continua como antes."

        mc "Ok... entendi..."

        w "..."

    w "Então a partir de amanhã, quero que você venha no primeiro horário do dia. Eu vou estar na minha cadeira te esperando."

    w "Vamos começar logo o trabalho de faxina na redação."

    mc normal "Ok. Amanhã, primeiro horário."

    show sofia rindo with dissolve

    w "Muito obrigada."

    w "E ah! Vou pedir para a contabilidade um adicional no seu salário."

    mc surpreso "!"

    w "Não é justo você trabalhar mais e não ganhar mais por isso. Eu quero fazer as coisas certas."

    mc normal "Que beleza! Valeu, [w]!"

    w "Nã-não foi nada. Acho que estamos encerrados por hoje."

    mc "Ok. Até amanhã, [w]."

    w "A-até."

    hide sofia with dissolve

    "Então a partir de amanhã, logo cedo começo a ajudar a [w]."

    "Ela é meio mandona, mas eu acho que ela quer fazer a coisa certa aqui na redação."

    "Talvez... só talvez... se ela mudar as coisas aqui na redação eu possa me livrar do chefe e das pautas."

    mc tarado "Isso seria incrível..."

    "Espero que dê tudo certo."

    $ tempo += 1

    jump call_cidade

label sofia_evento4:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("so4_save", extra_info="so4_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ so4_recepcionista = False
    $ so4_contou = False

    $ sofia_e4 = "evento"

    scene black with Dissolve(1.0)



    scene cidade tarde with dissolve

    w "De novo fazendo hora extra! Pelo menos o novo guarda não enrola igual o outro."

    w "Eu tô doida pra chegar em casa e maratonar minha série comendo bolo! Hmmm!"

    w "Vou arrumar tudo e dar o for- AAAHH!!!"

    scene sofia4_new1 with hpunch

    pause

    "Não acredito! De novo essas duas?!"

    "Desde que essa nova recepcionista entrou, é todo dia assim agora?"



    "Garota" "D-dona Cássia! Hmm! N-não!"

    "De novo assediando a pobre garota. Se ela abre um processo, a revista vai ter que pagar milhões. E com razão!"

    "Eu devia ter contato tudo pro meu pai desde a primeira vez. Mas eu tinha outras prioridades..."

    "Agora eu sou obrigada a ficar vendo esse tipo de coisa... que absurdo..."

    label so4_premium1:

        pass

    menu:
        "Eu tenho que ver e juntar mais provas":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_29

                jump so4_premium1

            "Eu não tenho escolha, eu tenho que ficar aqui vendo elas. Como eu vou denunciar sem os detalhes?"

            "Isso aí. Vou observar muito bem o que rola aqui entre essas d-duas..."

            j "Você é tão deliciosa, garota."

            "Garota" "Ahnn... P-por favor!"

            j "A gente tá tirando a roupa, mas tudo não passa de beijo. E você disse que eu podia."

            "Garota" "Hm-hmm... v-você tá me lambendo e apertanodo... aahn... inteira... i-isso não é beijo."

            j "É beijo também. Além de que você tá adorando, não tá?"

            "Garota" "E-eu?! Nng... E-eu disse que não gosto de garotas..."

            j "Mesmo assim, você não para de gemer gostoso..."

            "Garota" "!!!"

            "Garota" "E-eu nãuunnn... consigo controlar... hmm..."

            j "É a prova que você quer mais e mais. No fundo, você sabe que você adora sentir eu abusando de você."

            "Garota" "C-claro que nãaAAUMMM! AAHMM!"

            j "Vamos ver então."

            scene black with dissolve

            scene sofia4_premium1 with Dissolve(1.0)

            pause

            "Garota" "A-ah!"

            j "Eu vou estimular tanto seu corpo. Te dar tanto prazer, que você vai implorar pra eu não parar."

            "Garota" "N-não... s-só me beije igual você prometeu!"

            j "O beijo foi só o começo. Agora você já tá pronta pra mais. Pra sentir mais gostoso ainda."

            "Garota" "N-não... GMM!!"

            "Garota" "E-eu aceito os beijos... m-mas isso é demais!"

            j "No começo você não queria nada, agora aceita só os beijos. Você consegue se ouvir? Você quer mais e mais!"

            "Garota" "N-nãooo..."

            j "Ainda não admite? Deixa comigo. Eu vou mostrar pra você."

            j "Vou abaixar sua saia e fazer você entender qual é sua verdadeira natureza. Uma mulher com um fogo incontrolável."

            scene black with dissolve

            scene sofia4_premium2 with Dissolve(1.0)

            pause

            "Garota" "A-AIIN! N-não!!!"

            j "A gente não precisa dessa saia atrapalhando meu caminho."

            "Garota" "Aahnn... nãoo..."

            j "Seu corpo já tá tremendo, pombinha. Será que ele tá pedindo pra eu chegar mais perto do seu potinho de mel?"

            "Garota" "D-dona Cássia! Por favor! Ai não!"

            "Garota" "Eu não quero transar com outra mulher!"

            j "Não quer? Tem certeza? Porque você tá cada vez mais ofegante."

            "Garota" "A-ah... c-certeza... aahhn..."

            j "Você não quer sentir minha mão acariciando sua parte mais íntima? Esfregando e te dando todo aquele prazer?"

            "Garota" "Aah... n-nãaann..."

            j "Imagina meus dedos... pra cima e pra baixo... ah... esfregando sua buceta ensopada... hm?"

            j "Enquanto eu amasso seu seio carnudo com minha outra mão. E lambo seu pescoço. Tudo de uma vez até o clímax..."

            "Garota" "Aaa-aahn... e-eu..."

            scene black with dissolve

            scene sofia4_premium3 with Dissolve(1.0)

            pause

            w "Não é possível que uma pessoa não consiga resistir a uma coisa barata dessas!"

            "Desde quando nós viramos animais que não conseguem controlar sua luxúria?"

            "Só por causa de uma mão na m-minha... e no meu seio... e-eu conseguiria suportar com certeza!"

            menu:
                "Eu posso t-testar agora mesmo.":


                    "Eu vou provar que é muito simples... m-mesmo que eu pegue em mim..."

                    "Eu nunca deixaria isso tomar conta da minha razão!"

                    "Agora vamos ver você, garota... se você é forte igual a mim."

                    "Aposto que você quer se entregar a esse... p-prazer... aposto que você não resite!"

                    "A Cássia é s-sedutora demais... e você quer que ela f-faça o que quiser com você. Pode falar a verdade..."

                    "Garota" "A-aah!! Aí n-não!!!"

                    w "Huh!?"

                    scene black with dissolve

                    scene sofia4_premium4 with Dissolve(1.0)

                    pause

                    "Garota" "P-por favor! Aah!"

                    j "Você pode falar o que quiser, mas você tá pingando, safada..."

                    "Garota" "N-não... aah... aaiih..."

                    j "Meu dedo escorrega pra dentro de você."

                    "Garota" "Aaah.... aaaiin... hmmm!"

                    j "É gostoso, não é? Sinta meu dedo fincado na sua carne, e meu dedo deslizando pra dentro do seu buraquinho."

                    "Garota" "Hmm! Ahnn! Aahh!!"

                    j "Isso mesmo! Pode gemer. Você vai gemer muito sendo minha putinha."

                    "Garota" "Aaahnn! Nngnhhh! AAHH!"

                    j "Tá quase lá, né?!"

                    j "E se eu parar agora?"

                    "Garota" "!!??"

                    j "Por hoje tá bom... você pode ir..."

                    "Garota" "Aah... n-não..."

                    j "Eu já parei. Não precisa pedir mais."

                    "Garota" "N-não... n-não para..."

                    j "Não ouvi direito..."

                    "Garota" "P-por favor... C-cássia..."

                    j "Dona Cássia."

                    "Garota" "P-por favor, Dona Cássia!"

                    j "Quer sentir na buceta, é?!"

                    "Garota" "Sim..."

                    j "Então toma!"

                    "Garota" "AAHH!!!"

                    scene sofia4_premium5 with Dissolve(1.0)

                    pause

                    "Garota" "E-eu tô quase, D-dona Cássia! NNNGHH!!!"

                    j "Pode gozar, vadia."

                    "Garota" "Isso!! HMM!! E-eu nunca senti assim!!! AAHNNN!! T-tão forte!!!"

                    j "Você quer gozar? Mas você não gosta de mulher."

                    "Garota" "S-sim! AAHNN!! FODA-SE!! É BOM DEMAIS!! NNGHHHHHHHHHHHHH!!"

                    j "Você é igual qualquer outra que eu encontrei... quanto menos falar que quer... é porque mais quer..."

                    "Garota" "MAIS FORTE! AAHH!! MAIISSS!!!"

                    "Garota" "NNGHH!! MMMMGMGMG!!! FAZ EU GOZAR POR FAVORRR!!!"

                    j "Pedindo desse jeito, quem te negaria alguma coisa."

                    "Garota" "ISSOO!! MMH!!! NGGHHHH!!! VAIIII!!! ME FODEEE!!!!"

                    scene sofia4_premium5 with vpunch

                    "Garota" "AAAAHHHHHH!!!!"

                    j "E no fim... foi mais fácil do que eu imaginava..."

                    "Garota" "AAaahhh... minha... aah...."

                    j "Esse é só o começo, pombinha."

                    scene black with Dissolve(2.0)

                    pause

                    scene sofia4_premium6 with Dissolve(1.0)

                    pause

                    w "Aah..."

                    w "E-ela queria no fundo... q-que vadia... hmm..."

                    w "Eu nunca... n-nunca vou cair numa d-dessas... aah..."

                    w "Cabeça... sempre na frente..."

                    "D-deixa eu sair antes que... m-mas... p-parar agora?"

                    "Sai logo, [w]! Elas tão vindo!"

                    w "M-merda!"

                    scene black with hpunch
                "Eu não preciso de nada disso! Adeus!":


                    "Eu não preciso provar nada pra ninguém!"

                    "Eu vou contar pro meu pai assim que der."

                    "Mas, agora, eu vou parar isso."

                    scene black with vpunch

                    j "!"

                    "Garota" "Caiu a luz?!"

                    j "Não... alguém apagou de propósito... a gente continua outro dia."

                    "Garota" "T-tá... ufa..."

                    w "Assim é melhor. E agora bora pro meu bolo."
        "Eu vou parar essa baixaria":


            "Quer saber? Eu não preciso ver mais nada. Eu vou contar pro meu pai assim que der."

            "Mas, agora, eu vou parar isso."

            scene black with vpunch

            j "!"

            "Garota" "Caiu a luz?!"

            j "Não... alguém apagou de propósito... a gente continua outro dia."

            "Garota" "T-tá... ufa..."

            w "Assim é melhor. E agora bora pro meu bolo."

    scene black with Dissolve(1.0)

    scene cidade noite with Dissolve(3.0)

    scene black with Dissolve(1.0)

    scene cidade dia with Dissolve(1.0)

    "Desde aquela nossa ida pra Faux News, a [w] tá pegando mais pesado com a gente ainda."

    "Se antes ela já era maluca, agora tipo endoidou de vez. Ela praticamente dobrou nosso trabalho... galera tá vindo até de fim de semana."

    "???" "Ei."

    scene so4_recepecionista1 with Dissolve(2.0)

    pause

    mc desconfiado "Hm?"

    re "Oi. Eu sou a [re]. Sou a nova recepcionista da revista."

    mc "Caraca. Nem sabia que a gente tinha alguém na recepção."

    menu:
        "Bacana. Bem-vinda à empresa.":


            mc normal "Legal. Então seja bem-vinda à revista. Espero que você curta trabalhar aqui."

            re "Valeu. O trabalho parece bem tranquilo. Acho que eu vou gostar sim."

            mc "É. Não sei se vai ser fácil desse jeito que você tá pensando, mas você aguenta."

            re "Haha... obrigada mesmo pelo voto de confiança."
        "Qualquer coisa que precisar fala comigo.":


            mc charmoso "Opa. Qualquer coisa que você precisar pode falar comigo."

            re "Obrigada. Acho que no começo eu posso precisar de uma ajuda mesmo."

            mc "Eu não sou nenhum especialista, mas pelo menos eu tenho um tempo de casa. Posso falar quem é de boa e quem dá trabalho... tipo o chefe."

            re "Haha... anotado."

    scene so4_recepecionista2 with Dissolve(1.0)

    pause

    re "Você faz o que aqui?"

    mc envergonhado "Eu faço de tudo um pouco. Principalmente depois que a nova coordenadora de produção chegou."

    re "Nova coordenadora? O que é isso?"

    mc normal "A coordenadora de produção coordena a produção. Entendeu?"

    re "Aaahhh... agora entendi. Obrigada, hein?"

    mc "Tem tipo dois chefes aqui. Um é o editor chefe. Ele é mais responsável pelo conteúdo da revista. O que entra e o que não entra."

    mc zerado "Esse é o zé mané que dá dor de cabeça em todo mundo."

    re "Certo..."

    mc normal "A coordenadora de produção não foca no conteúdo, mas em organizar a equipe. Ela que divide o trabalho entre os funcionários."

    mc "Ela precisa garantir que todo o trabalho seja feito e as pessoas estejam trabalhando direitinho."

    re "Ah! Agora, sim. Obrigada."

    re "Então pode ser que acabe sobrando pra mim também..."

    mc normal "Olha, ela foca mais na equipe de jornalismo, mas não garanto que você tá salva. Precisa ficar esperta."

    re "Perfeito... e eu achando que só ia atender o telefone e passar pros outros."

    mc envergonhado "Sinto que vai ser um pouco mais corrido que isso aí."

    re "Já posso começar a comemorar?"

    mc "Haha... você vai aguentar. Tenho certeza."

    re "Sei não. Eu gosto de ficar de boa no trabalho."

    menu:
        "Eu também prefiro ficar de boa.":


            mc charmoso "Se tem jeito, eu também prefiro ficar de boa. Fazer aquele mínimo pra ganhar a grana e aproveitar."

            re "Né?! Eu sou muito assim, cara. Faço o que precisa só. Não sou de trabalhar muito, não haha..."

            mc charmoso "Olha aí. Uma coisa em comum já. Tirando que nós dois somos, assim, muito gatos, né?"

            re "Haha... né?! Concordo..."
        "Você tem que ralar pra justificar o pagamento, né?":


            mc envergonhado "Ralar faz parte, né? Tipo, a gente precisa justificar a grana que a gente recebe."

            re "Mas, tipo, pensa. Os caras ganham uma nota e pagam uma mixaria pra gente. Eles não merecem, não."

            mc "Aí talvez você tenha razão. Mas eu ainda prefiro dar o meu melhor e ficar com a consciência tranquila."

            re "Sei... eu acho isso coisa de trouxa... com todo o respeito, claro. Não tô falando de você."

            mc "Entendi, relaxa. É. Cada uma com a sua cabeça."

            re "Isso aí."

    scene so4_recepecionista3 with Dissolve(1.0)

    pause

    re "Mas, assim, eu ouvi falarem que você é o queridinho da chefinha. Nem sei quem é essa pra falar a verdade. Só me falaram."

    mc zerado "Então é isso que tão falando..."

    re "Contaram que você tá sempre com ela. Sai com ela, faz tudo o que ela manda. Tipo um cachorrinho..."

    menu:
        "Não é bem assim...":


            mc envergonhado "Não é bem assim, né? Eu ajudo ela e acho que sou um dos que mais entraram no jogo dela desde que ela chegou."

            re "Então..."

            mc "Mas eu faço porque eu gosto. Não sou cachorrinho de ninguém. Só quero fazer um bom trabalho e quem sabe me aproximar dela."

            re "Segundas intenções... entendi..."

            if sofia_namorar:

                mc safado "Opa... quem sabe..."

                re "Já tô vendo tudo."
            else:


                mc charmoso "Nem é isso. Ela é legal e tudo, mas não quero nada com ela assim."

                re "Hmm... será que o coração já é de outra pessoa?"

                mc "Quem sabe um dia você descobre."
        "Tô me fodendo pro que falam.":


            mc zerado "Tô pouco me fodendo pro que o pessoal fala de mim. O que eu faço não tem a ver com ninguém."

            re "Certo... só tô comentando..."

            mc desculpa "Se você quer se dar bem em uma empresa de jornalismo, é bom você aprender a filtrar o que é verdade e o que é fake news."

            re "Lição anotada."

    mc normal "E o que mais você tem ouvido por aí?"

    re "Eu acabei de chegar, então não é muita coisa. Só uns rolos aqui e ali."

    mc charmoso "Parece que vai ser bem útil conversar com você..."

    re "Ei... minhas informações não são assim de graça também. Aqui leva quem der o maior lance. Mas eu prometo que vou ouvir de tudo."

    "Essa moça... ela me lembra um pouco a [j]. Tomara que elas não façam muita amizade."

    "Mas ela é linda, jovem e parece bem descolada... será que usam essa palavra ainda? Tenho que tomar cuidado pra não dar fora."

    mc normal "Bom. Se a [w] souber que eu tô aqui batendo papo com você ao invés de pegar as tarefas do dia ela me mata."

    re "Puxa... mais já?"

    scene so4_recepecionista4 with Dissolve(1.0)

    pause

    re "Fica mais um pouco. Eu tô curiosa pra saber mais sobre você e o trabalho aqui. Parece tão interessante..."

    "Opa. Isso pareceu... um convite bem sugestivo. Eu nem conheço essa mina direito. Por que ela tá sendo direta desse jeito?"

    mc envergonhado "Não sei o que tem de tão interessante nesse trabalho."

    re "Eu gosto de saber tudo o que acontece onde eu trabalho. E é legal ter companhia. Você não gostou de falar comigo? Pode ser sincero."

    mc surpreso "N-não! Não é isso!"

    re "Ufa... achei que eu tivesse te enchendo."

    mc envergonhado "Que nada. Você é bem... interessante."

    "E o que EU tô falando agora?! Parece que eu tô dando em cima dela!"

    re "Rsrs... Obrigada. Então. Pode ficar mais um pouquinho comigo?"

    "Caralho... se a [w] me pegar aqui eu tô perdido. Mas perder a chance de falar com essa loira também..."

    menu:
        "Tudo bem. Eu vou ficar.":


            $ so4_recepcionista = True

            mc charmoso "De boa. O trabalho pode esperar."

            re "Ai, que bom. Chega aí."

            mc "Opa."

            scene so4_recepecionista5 with Dissolve(1.0)

            pause

            re "Ah. Deixa eu perguntar uma coisa?"

            mc "Claro."

            re "Você é tipo famoso, né?"

            mc "Eu? Por que?"

            re "Ah... você escreve as matérias, seu nome sai na revista e tudo. As pessoas te conhecem."

            menu:
                "Não é bem assim. Eu consigo pautas.":


                    mc "Não, não. Falta muito pra eu virar alguma coisa assim. Eu só descubro segredos e passo pro chefe."

                    mc "São outras pessoas que apuram, pegam entrevistas e transoforma isso em uma matéria de verdade."

                    re "Então ninguém sabe quem você é?"

                    mc "Praticamente ninguém. Meu nome vai na revista, mas sem destaque. Então só quem tá ligado mesmo pra saber isso."

                    re "Entendi... é tipo um super herói. Salvando o mundo sem que ninguém saiba."

                    mc "Haha! Quem sabe..."
                "Sim. Eu sou tipo uma celebridade.":


                    mc "É. Pensando por esse lado, eu sou tipo uma celebridade mesmo. Mas não fico pensando muito nisso."

                    re "Caralho, que legal. Opa, desculpa..."

                    mc "Relaxa. Mas eu prefiro me manter anônimo, sabe? Eu só dou autógrafo se pedem ou uma self, não fico chamando atenção."

                    re "Deve ser algo bem legal. Deu até um nervoso agora."

                    mc "Sério? Por que?"

                    re "Ah! De falar assim com uma pessoa que reconhecem na rua."

                    mc "Que isso. Não fica pensando besteira. Gostei muito de conversar com você."

                    mc "Além de que você é linda. Tá pra nascer um cara que não curte falar com uma mina gata."

                    re "Ai, bobo... vai me deixar com vergonha assim."

            mc "Se você quiser um autógr-"

            w "[mc]!"

            mc "?!"

            scene so4_recepecionista6 with hpunch

            pause

            "Ih! Fodeu!"

            mc "O-oi, [w]."

            w "Eu achei mesmo que tava ouvindo sua voz. Quando você chega, vem falar comigo a primeira coisa. A gente tá cheio de coisa pra fazer."

            mc "Calma... tá tudo leg-"

            w "Vem logo!"

            re "..."

            mc "Até mais, [re]."

            re "Até..."
        "Outra hora. Agora tenho que trabalhar.":


            $ sofia_amizade += 2

            mc "Outra hora com certeza. Mas se eu não começar o trabalho cedo eu fico preso aqui pra sempre."

            re "Aww... ok."

            mc "Mas a gente vai se falar, [re]. Vai ser legal ter você aqui."

            re "Obrigada. Até mais."

            mc "Até."

    scene trabalho angulo with Dissolve(2.0)

    "A [w] tá cada vez mais doida. E se ela continuar com isso, a redação só vai se dividir mais e mais."

    "Pelo que a [re] falou, as pessoas já criaram até um 'clubinho da chefinha'. Ela precisa ver isso."

    "O que me pega é que a [w] faz um trabalho muito sério. Ela é boa nisso, caralho. Por que as pessoas não se esforçam mais?"

    "A culpa não é dela se ela quer fazer a melhor revista que ela pode. Quem pode culpar ela por ser boa no que faz?"

    w "[mc]?"

    mc surpreso "O-oi!"

    scene so4_sofia_redacao1 with Dissolve(1.0)

    pause

    if so4_recepcionista:

        w "Que conversinha era aquela com a nova funcionária? Já passou do seu horário de chegada."

        mc envergonhado "Eu sei. Desculpa..."

        w "Espero que essa amizade de vocês não te atrapalhe no trabalho."

        mc "Com certeza não."

        "Mentiroso."

        w "{i}hmpf{/i}"
    else:


        w "Eu escutei sua voz lá na frente. Conhecendo a nova funcionária."

        mc normal "Sim. Primeira vez que eu vejo ela."

        w "Espero que isso não atrapalhe seu trabalho aqui."

        mc "Pode ficar tranquila."

        w "Muito bom."

    w "Bom... agora que você tá aqui. Deixa eu te passar o que eu preciso que você faça."

    mc desculpa "É... [w]... antes disso. Posso conversar um negócio com você?"

    w "É muito importante?"

    mc "Eu acredito que sim."

    w "Então tá. O que é?"

    scene so4_sofia_redacao2 with Dissolve(1.0)

    mc "É..."

    "A [w] precisa saber que as pessoas tão chamando a gente de 'cachorrinho'. As pessoas tão vendo ela como uma inimiga."

    "Certeza que é esse jeito dela. Ela tem que saber isso."

    "Mas como eu falo isso pra ela sem que complique pro meu lado? Eu tenho que tomar cuidado pra isso não sobrar pra mim."

    "Será que no fundo é melhor eu só não falar nada? Sei lá se isso tem a ver comigo..."

    menu:
        "Quer saber? Deixa pra lá. Outra hora eu falo.":


            mc "Ah... deixa pra lá. Não era nada muito importante. Dá pra falar depois."

            w "Tem certeza? Não tá escondendo nada de mim, né?"

            mc "N-não! Claro que não."

            w "Ok..."

            mc "Fica tranquila que era um negócio, mas é melhor eu falar outra hora."

            w "Tudo bem."
        "Seu jeito tá dividindo a redação.":


            $ sofia_amizade += 2

            $ so4_contou = True

            mc "É que seu jeito tá dividindo a redação."

            w "Dividindo? Como assim dividindo?"

            mc "Tipo... eu tava falando com a [re] e ela contou que falaram pra ela que eu era seu 'cachorrinho', que eu fazia tudo o que você mandava."

            w "[re]... sei..."

            mc "Me deu a impressão que tão se formando dois grupinhos aqui. Os que tão do seu lado e os que não tão."

            mc "Daí eu queria te falar isso, porque acho que seria legal você saber. Acredito que ninguém vai te falar isso na cara."

            w "Sei... E o que você acha?"

            mc "Eu?!"

            w "É. Você concorda com isso? Que a gente tá parecendo dois grupos?"

            mc "Bah... sei lá, mano."

            w "'Bah sei lá', essa é sua resposta? Sério?"

            mc "Tá bom, calma... Eu já falei isso pra você. Você leva as coisas meio sério demais. Nem todo mundo é assim."

            mc "Quando você puxa muito, uma parte da galera, que é mais tranquila-"

            w "Folgada você quer dizer."

            mc "Tô tentando ser político aqui. Então... uma parte deve se sentir meio alienada. Tipo, meio fora do 'seu grupo'."

            scene so4_sofia_redacao3 with Dissolve(1.0)

            w "Entendi... você acha então que eu devo ser relaxada igual a eles? É assim que a gente tem que levar nossa profissão?"

            w "Você quer que eu faça o mínimo porque tem um bando de folgados que acham que a revista é brincadeira?"

            w "Trabalhar de forma medíocre pros folgados se sentirem em casa? Esse é o certo?!"

            mc "C-calma! O pessoal vai ouvir."

            w "E daí?! Tô pouco me lixando, [mc]! Esse bando de... de... medíocres que vivem sob a lei do mínimo esforço!"

            "Quando a [w] se empolga é duro discutir com ela... ela perde a atenção de tudo."

            "Aliás... ela não tá percebendo que gesticulando desse jeito os peitos dela..."

            menu:
                "Dar uma olhada discreta no...":


                    "Do jeito que ela tá, ela não vai perceber..."

                    scene so4_sofia_redacao4 with Dissolve(1.0)

                    pause

                    "Hehe... eu sou a escória do universo mesmo."

                    w "[mc]! Pra onde tu tá olhando!"

                    scene so4_sofia_redacao3 with vpunch

                    mc "É... E-eu..."
                "Claro que não!":


                    "O que eu tô pensando? Claro que não."

            mc "Então, [w]. Desculpa te cortar."

            mc "Eu só tô falando o que eu acho. Você que perguntou!"

            w "Eu não tô nem aí. Eles fazendo o que eu preciso que eles façam, eles podem me odiar."

            mc "Certeza que esse é o melhor caminho? Você é a chefe de todo mundo aqui."

            w "Eu não aguento viver no meio de gente relaxada, [mc]. Gente que faz só o mínimo só pra não ser despedido."

            w "As pessoas precisam colocar o coração no que elas fazem. Fazer o que é certo! E eu não vou me rebaixar ao nível deles..."

            mc "Tudo bem. Eu entendi."

            w "E não é com você que eu tô brava! É com a situação!"

            mc "Tá legal..."

    "A [w] tem o jeito de pensar dela e eu acho que ela não vai mudar tão cedo. Fazer o quê? A mina gosta de gente esforçada."

    "O máximo que eu posso fazer é avisar ela, mas não adianta querer mudar o que ela pensa."

    "Só torço pra que as coisas não acabem de alguma forma terrível. Tipo... eles crucificando ela e tacando fogo igual uma bruxa."

    "Acho que não chega a tanto... eu acho."

    scene so4_sofia_redacao5 with Dissolve(1.0)

    w "Ah. Meu pai quer falar comigo sobre um negócio. Eu queria que você viesse junto."

    mc surpreso "Eu?!"

    w "É, ué."

    menu:
        "Eu não quero falar com ele.":


            mc zerado "Eu não quero falar com o velho!"

            w "Eu sei que ele é um babaca e dá medo... mas não tem nada a ver com você. Pode ficar tranquilo."

            mc envergonhado "Não tem nada a ver comigo? Então por que..."

            w "Bom... você tá fazendo um trabalho legal e eu queria que você participasse mais das coisas."

            mc "Puxa... valeu. Se é assim então acho que eu posso ir."

            w "Obrigada."
        "Tudo bem. Eu vou junto.":


            $ sofia_amizade += 1

            mc normal "Ok. Se você quer que eu participe, bora. Mas eu e o seu velho só briga."

            w "Eu sei. Ele briga com todo mundo, [mc]. Aquele babaca perdeu o coração em algum ponto da vida dele."

            mc desconfiado "Você sabe como ele ficou tão amargo assim?"

            w "Não interessa. Isso é coisa particular dele. Não tem nada a ver com nosso trabalho."

            mc zerado "Fato."

    w "Acho que é melhor falar com ele agora de uma vez então. Assim não atrapalha quando a gente tiver trabalhando."

    mc normal "Hoje vai ser um dia puxado pelo jeito."

    w "Até a gente ajeitar tudo, o trabalho vai ser puxado. Mas depois... eu acho que melhora..."

    mc zerado "Você acha?"

    w "E não adianta reclamar, [mc]. Vem."

    scene trabalho angulo with Dissolve(1.0)

    if sofia_beijo:

        "A [w] não falou nada do nosso beijo até agora..."

        "Será que eu acabei com todas as chances que eu tinha com ela? Acho que eu não devia ter forçado as coisas."

        "O pior é que eu nem tenho coragem de falar"

    w "Você tá aí ainda?"

    mc surpreso "T-tô indo!"

    scene trabalho chefe_porta with Dissolve(2.0)

    "Falar com esse velho... dá até um calafrio..."

    w "Vamos entrar."

    mc envergonhado "Sim..."

    scene black with Dissolve(1.0)

    scene trabalho chefe with Dissolve(2.0)

    w "Oi, pai. Estou aqui."

    b "Então, filha-"

    b "Huh? Por que ele tá junto?"

    mc envergonhado "..."

    scene so4_chefe1 with Dissolve(2.0)

    pause

    w "O [mc] tá me ajudando bastante no meu trabalho com a equipe. Queria que ele participasse."

    b "Isso é coisa séria, [w]."

    w "Tudo bem. Eu confio nele."

    b "Garoto..."

    menu:
        "Se vocês quiserem, eu posso sair.":


            mc "Então... se vocês preferirem, eu posso esperar lá fora."

            b "Seria bom."

            w "Não! Eu quero que você participe, [mc]. Eu quero que você veja como são nossas reuniões."

            mc "Tudo bem..."

            b "Se você quer assim, [w]..."
        "Pode confiar em mim, chefe.":


            $ sofia_amizade += 1

            mc "Pode confiar, chefe. A [w] disse que é importante e eu só quero melhorar meu trabalho aqui na revista."

            b "Hmm... ok. Se ela diz."

            w "Sim. Eu que chamei ele. Eu quero que ele entenda melhor como funciona nossas reuniões."

    b "Eu te chamei aqui porque talvez as coisas mudem muito na revista daqui um tempo."

    "Ele fala como se a [w] já não tivesse mudando tudo..."

    scene so4_chefe2 with Dissolve(1.0)

    pause

    b "O conselho veio falar comigo novamente sobre uma proposta de compra da revista."

    w "De novo?!"

    b "Sim. Parece que esses energúmenos da Faux News não vão desistir."

    w "Pai! Você não pode deixar eles aceitarem!"

    b "[w]... filha... eu fiz tudo o que eu podia, caralho!"

    b "Eles confiam em mim, mas o que importa pra eles é dinheiro."

    menu:
        "Continuar quieto.":


            "Melhor eu não me intrometer."

            w "Eu não entendo. Nossa revista dá dinheiro!"

            b "Mas não o suficiente, filha. Eles não querem só dinheiro, eles querem TODO o dinheiro."

            w "..."

            w "Eu não sei o que responder... acho isso ridículo."

            b "Você acha ridículo porque você não sabe nada de negócios."

            w "Claro! Não foi isso que eu estudei, droga."

            b "Pois é. Então não se intrometa onde não é chamada."
        "Mas a revista não dá dinheiro?":


            $ sofia_amizade += 1

            mc "Mas, chefe, a revista não dá dinheiro?"

            b "Não seja burro, moleque. Claro que a revista dá dinheiro-"

            w "Não chame ele de burro. A pergunta dele faz todo o sentido."

            b "Só na cabecinha de merda de vocês. Vocês não entendem como funcionam as empresas."

    b "O dono da revista precisa agradar os acionistas que colocam dinheiro aqui. A revista precisa dar dinheiro suficiente pra eles ficarem felizes."

    b "Até hoje, eu sempre mantive a revista em ordem, lucrativa. Esse é meu objetivo aqui. É por isso que até hoje eu segurei as pontas."

    b "Só que a proposta da Faux é maior do que anos do nosso trabalho. É dinheiro fácil demais pro bolso dos burgueses safados."

    "O [lu] não tava brincando quando disse que eles iam vir com tudo pra cima da revista."

    scene so4_chefe3 with Dissolve(1.0)

    w "Mas isso é um absurdo! Com o passar do tempo nossa revista vai dar mais dinheiro do que isso!"

    b "Pode ser que sim, pode ser que não, garota. Mas, pra eles, quanto mais rápido o dinheiro, melhor. Eles vão investir em outra coisa."

    mc "..."

    w "Então é isso? A gente vai dar tudo pra aquele [lu] idiota e esses estúpidos da Faux News? A gente vai virar mais um brinquedinho deles?"

    b "Você não precisa se preocupar. Provavelmente eles vão manter os empregos. No máximo vão te jogar pra repórter."

    b "Será que você não sabe mais como trabalhar com reportagem, filha? É esse seu medo?"

    w "Afe! Não é isso, pai! Eles não tão nem aí com a notícia! Aquele [lu] é um mentiroso salafrário! Eu não quero trabalhar pra ele!"

    b "Talvez seja o único jeito..."

    w "[mc]... você não tem nada pra falar?"

    mc "E-eu?!"

    "Enquanto eles tavam falando eu só conseguia pensar no que o [lu] me falou. Que eu posso aceitar a proposta deles ou não."

    "Se eu aceitar eu vou ficar de boa quando eles comprarem a revista... o que seria incrível, ainda mais agora sabendo de tudo isso."

    "Essa é uma boa hora pra eu já começar a ajudar eles a conseguir a compra. Eu só tenho a ganhar com isso."

    "Só que... por outro lado... a [w] vai me odiar. E se eles não comprarem eu vou ter escolhido o lado errado..."

    "Provavelmente o que eu decidir aqui também vai mudar o que eu tenho com a [j]. Ela com certeza quer que a Faux compre."

    b "Vai falar alguma coisa, garoto? Ou vai ficar com essa cara de cu até amanhã?"

    mc "É..."

    "E agora?"

    menu:
        "O chefe tá certo. Não tem nada que dá pra fazer.":


            $ venda_revista += 1

            "Espero que eu esteja fazendo o melhor pra mim..."

            scene so4_chefe4 with Dissolve(1.0)

            mc "Eu... eu entendo a frustração da [w]. Mas eu concordo com o chefe. Não tem o que ser feito agora."

            mc "Se quem manda aqui são os acionistas e eles querem ganhar essa bolada agora, o que a gente pode fazer?"

            w "[mc]! Não acredito que tô ouvindo isso de você! Bem de você!"

            w "Eu pensei que você tivesse amor pelo Jornalismo igual eu! Agora fala essas coisas?! Que decepção!"

            mc "Eu entendo, [w]... mas isso tá longe demais da gente. O que seu pai pode fazer é limitado."

            b "Ei, calma... o moleque tem razão, filha.. Eu não posso decidir por eles. Mas não é assim também."

            b "Eles sempre me ouviram... então talvez eu possa segurar mais um pouco..."

            w "Isso é pouco. Não dá pra gente trabalhar com essa emeaça em cima da gente."

            mc "Calma, [w]. Ele tá fazendo o que dá. Não adianta a gente culpar ele também."

            w "Parece que você também desistiu, [mc]."

            mc "Não é isso. Ele já falou que vai falar com eles. É tudo o que ele pode fazer."

            w "Merda..."

            b "Eu falei pra você se acalmar. Eu vou continuar fazendo o que eu sempre fiz."

            scene so4_chefe6 with Dissolve(1.0)

            w "Mas se esforce, pai! Não se dê por vencido!"
        "A [w] tá certa. A gente tem que impedir a compra!":


            $ sofia_amizade += 3

            scene so4_chefe5 with Dissolve(1.0)

            mc "Pra mim, o que a [w] disse tá certo. A gente NÃO pode só esperar eles fazerem o que eles quiserem."

            mc "Aquele [lu] falou pra mim e pra [w] quando a gente foi lá. Ele não tá nem aí pra verdade. Os anunciantes em primeiro lugar!"

            mc "Se esses caras assumirem a revista já era. Eles vão transformar isso aqui numa farra."

            w "Isso aí, [mc]! Tá vendo, pai?!"

            b "Vocês vivem no mundo da lua, não é possível. Vocês tão ouvindo o que eu tô falando?! Mas será o benedito?!"

            mc "Chefe... pense em todo o trabalho que você teve pra criar tudo isso aqui. É coisa pra caramba."

            mc "Eles vão jogar tudo o que presta no lixo e ficar só com o que eles quiserem, que é o que dá dinheiro, claro. Jornalismo nem pensar."

            b "Que saco... vocês parecem duas gralhas {i}qua qua qua, qua qua qua{/i}."

            w "Mas não é verdade o que o [mc] tá falando? O próprio [lu] falou na nossa cara que o que importa é agradar os anunciantes."

            w "O cara nem tem vergonha, pai! Você vai entregar tudo o que você criou aqui pra esse sujeito e os amiguinhos dele?"

            b "Tá bom! Tá bom! Vocês já me encheram o saco demais por um dia! Eu vou conversar com eles e ver o que dá pra fazer!"

            scene so4_chefe6 with Dissolve(1.0)

            w "Muito obrigada, pai! E valeu, [mc]! Você foi incrível!"

    b "Tá, tá... mas pode ter certeza que eles não vão me ouvir pra sempre. Eu já tô segurando isso há anos!"

    w "Eu sei! Eu prometo que eu vou dar o meu melhor aqui também, você vai ver!"

    w "Com o meu trabalho e do resto da equipe a revista só vai melhorar e a gente vai trazer todo o dinheiro do mundo pra esses porcos capitalistas."

    b "Porcos capitalistas que pagam toda sua brincadeira aqui."

    w "Mentira! Nosso trabalho que paga isso aqui. Eu vou me esforçar mais. Você vai ver, pai! Isso aqui vai ficar incrível!"

    "A [w] e o chefe parece que tão falando línguas diferentes. Ela não entende que o objetivo dos donos é dinheiro e o velho parece que desistiu..."

    "O que será que é melhor pra mim? Eu preciso pensar nisso porque eu vou ter que decidir e isso com certeza vai mudar minha relação com todos aqui."

    "O [lu] disse que a [w] é carta fora do baralho. Ela é legal e super esforçada. Até demais... mas não sei se ela merece ir pra rua."

    if sofia_namorar:

        "Ainda mais que eu decidi que eu quero namorar ela. Certeza que tudo vai pro buraco se ela for pra rua."

    scene so4_chefe7 with Dissolve(1.0)

    pause

    w "Puxa, [mc]... agora que a gente tava indo bem aqui na redação. As matérias tão melhorando, o pessoal tá entrando na linha."

    mc "Menos a [j] lógico..."

    w "Ela vai se enquadrar também. A gente só precisa ter paciência. Mas se esse idiota do [lu] vier pra cá, eles vão jogar tudo no buraco."

    w "Só de pensar nisso eu fico muito... que bosta..."

    b "..."

    "Eu fico triste por ela, mas eu tenho que pensar nos meus planos. Se eu quiser que a Faux News compre aqui, eu tenho que fazer a cabeça deles."

    "Será que eu tô sendo egoísta demais? Pensar só em mim realmente é o melhor? Não é a [j] que fala assim? Afe, que caralho, viu..."

    menu:
        "Pode contar comigo pra manter a revista!":


            $ sofia_amizade += 3

            mc "Eu sei que eu sou só um paparazzo, um caçador de pautas e minha opinião não vale muito..."

            scene so4_chefe8 with Dissolve(1.0)

            mc "Mas eu quero que vocês saibam que eu vou dar tudo de mim pra revista não ser vendida."

            w "[mc]!"

            mc "Eu sei o quanto isso aqui vale pra você, [w]. E eu sei que o chefe também se esforçou pra caramba durante todos esses anos."

            mc "A gente não pode aceitar que um povo qualquer, só porque tem dinheiro, venha aqui e tome tudo isso de vocês."

            w "I-isso! Isso que eu tô falando!"

            mc "Se o que os donos precisam pra manter a revista é que ela dê muita grana, só depende da gente."

            mc "E do chefe também que vai ter que segurar a barra por um tempo..."

            b "Vocês parecem duas crianças. É quase trabalho infantil isso aqui. Vocês vivem nesse mundinho da lua de vocês."
        "A gente precisa aceitar a derrota.":


            $ venda_revista += 1

            scene so4_chefe9 with Dissolve(1.0)

            mc "Eu sei que é foda, mas a gente precisa saber reconhecer quando a gente tá em desvantagem. Ficar dando soco em ponta de faca não dá."

            w "..."

            mc "Se a Faux tem cacife pra fazer a cabeça dos donos, o que a gente pode fazer?"

            w "Só desistir? É isso?"

            b "Ele tem razão, [w]. A gente faz o que dá. Não adianta chorar pelo leite derramado. Isso é coisa de mulher mimada."

            w "Como você é machista... e vocês dois são uns cansados!"

            mc "Você pode brigar comigo o quanto você quiser. Isso não muda o fato que a Faux vai comprar a revista."

            mc "Eu vou continuar fazendo meu trabalho com você. Não vai mudar nada pra mim. Mas a realidade tá aí batendo na porta."

            w "O que adianta falar com essas palavras bonitas se você já tá se entregando? Eu NÃO vou aceitar isso."

            mc "É sua escolha..."

    scene so4_chefe2 with Dissolve(1.0)

    b "Bom... eu vou fazer o que eu posso. E não quero encheção de saco se tudo der merda. Por isso que te chamei aqui. Pra avisar."

    w "Tá bom... obrigada..."

    mc "Não fica assim não, [w]. Vai tudo ficar bem."

    w "Não tô afim de conversar agora, [mc]. Valeu."

    mc "Se você precisar falar com alguém, pode confiar em mim, beleza?"

    w "Tá bom. Agora a gente tem que ver as tarefas do dia. O deadline da próxima edição tá chegando e vai ter uma matéria da [j]."

    mc "Já entendi..."

    w "Vai ter um bocado de coisa pra você checar. E não dá pra pedir ajuda pro Ronaldo porque ele já tem outra coisa."

    mc "Ok..."

    b "Vocês tão achando que minha sala é pra ficar decidindo esse tipo de coisa?!"

    mc "Mas é sobre a rev-"

    b "Saiam daqui!"

    w "Vamos..."

    scene black with Dissolve(1.0)

    scene trabalho chefe_porta with Dissolve(2.0)

    w "Ixi. Olha a hora. A gente tá super atrasado. Vou precisar da sua dedicação total hoje."

    mc zerado "..."

    scene black with Dissolve(2.0)

    "..."

    scene trabalho angulo with Dissolve(1.0)

    mc concentrando "Caralho... que dia..."

    "O negócio com o chefe deve ter mexido com a [w] mesmo. Ela parecia mais focada que o normal. Pelo menos ela parece animada e não derrotada."

    "Desde o começo eu sabia que essa mina era o leão, bicho. É duro derrubar essa aí."

    "Só não sei como ela ainda não teve um ataque cardíaco de tanto trabalhar. Afe, se fosse eu já tinha pirado."

    "Bom... agora só quero ir pra casa e tirar aquele cochilo até am-"

    mc desconfiado "?"

    scene so4_sofia_cansada1 with Dissolve(2.0)

    pause

    mc desconfiado "[w]?"

    w "Hm?"

    mc "Cadê a galera?"

    w "Todo mundo já foi embora faz duas... horas..."

    mc "Ah. Ei... Você tá bem?"

    w "S-sim... claro. Por que?"

    mc envergonhado "Sei lá. Você parece meio abatida aí."

    w "Não sei por que... Eu tô... super legal..."

    mc desconfiado "..."

    scene so4_sofia_cansada2 with Dissolve(1.0)

    pause

    "'Super legal'? Não sei onde..."

    menu:
        "Você parece tudo, menos super legal...":


            $ sofia_amizade += 1

            mc zerado "Não é por nada, mas você parece tudo, menos super legal."

            w "Você tá exagerando..."

            mc envergonhado "Olha pra sua cara, [w]. Você parece que foi atropelada por uma carroça."

            w "Era pra eu saber o que isso significa?"

            mc preocupado "Você não tá trabalhando demais, não?"

            w "Você não é meu pai, [mc]. Não precisa ficar se preocupando comigo."

            mc desculpa "..."
        "O que você vai fazer agora?":


            mc normal "O que você tá pensando em fazer agora?"

            w "Por que?"

            mc envergonhado "Nada. Só pra saber."

            w "Acho que vou pra casa. Deu pra terminar tudo aqui. Foi um dia bem produtivo apesar de tudo."

            mc "Entendi... vai ser bom você dar uma descansada."

            w "Descansar? Eu vou é preparar a escala de amanhã. Tô super atrasada."

            mc zerado "Mais trabalho..."

    w "..."

    mc desculpa "Olha, [w]. Não quero me intrometer, mas talvez você precise de uma pausa, sabe?"

    w "Obrigada pela sua opinião técnica super valiosa..."

    mc preocupado "Tô falando sério. Não preciso ser psicólogo pra ver que você tá mal pra caralho."

    w "..."

    mc charmoso "Já sei. A gente vai beber uma."

    scene so4_sofia_cansada3 with Dissolve(1.0)

    w "Tá brincando comigo..."

    mc zerado "[w]... sua cara tá me dando medo."

    w "Você tá me deixando mais ansiosa... só pare de falar por favor."

    mc normal "Eu tô falando sério. Seria uma boa a gente tirar a cabeça daqui."

    if sofia_beijo:

        w "Você vai me agarrar de novo..."

        mc surpreso "N-não! Não é isso!"

        w "Sei... você só quer ficar sozinho comigo longe do trabalho."

        mc envergonhado "Já falei que não é isso. Eu... prometo que não vou fazer nada assim."

        w "Você tá falando isso só pra me convencer?"

        mc zerado "Claro que não."
    else:


        w "Isso é viagem demais pra mim, [mc]..."

        w "Eu gosto de ficar em casa-"

        mc zerado "Trabalhando?"

        w "..."

        w "E... se você só quiser me pegar?"

        mc surpreso "C-como assim?! C-claro que não!"

        if sofia_namorar:

            "É... eu realmente queria ficar com ela..."

            mc envergonhado "Não tô falando que eu não gostaria de ficar contigo... mas não é esse meu objetivo agora."
        else:


            mc normal "Eu não tenho nenhum objetivo assim. Você é só uma grande amiga. Só isso."

            w "Tá..."

    w "Desculpa. Você nunca me deu razão pra não acreditar em você. Mas beber no bar? Eu não sou igual essa galera que curte happy hour."

    mc envergonhado "E você acha que eu não sei isso?"

    mc charmoso "Mas você tá precisando. Casos urgentes pedem medidas extremas."

    w "Você tá exagerando de novo..."

    mc "Eu fui falar com o chefe hoje. Agora é sua vez. Vem logo."

    w "[mc]..."

    mc "Veem!"

    scene black with Dissolve(1.0)

    "..."

    scene pub_especial with Dissolve(2.0)

    pause

    "Uou... o bar parece diferente. Acho que ele não abriu completamente ainda."

    "Nem acredito que ela me seguiu até aqui. Sorte que o bar fica do ladinho da redação."

    mc normal "Bem-vinda. Senta aqui."

    w "..."

    scene so4_bar1 with Dissolve(1.0)

    pause

    mc "Não se preocupe que o ar aqui não é venenoso."

    w "Haha..."

    menu:
        "Então? Você já tinha vindo aqui?":


            mc "Pela sua risada, então você já conhecia aqui?"

            w "Não... mas não precisa tirar sarro também."

            mc "Parece zuera sua, mas não tem problema. A gente sempre tem uma primeira vez pra tudo."

            w "Que comentário vergonha alheia."
        "Você já saiu com alguém da redação?":


            mc "Mas fala aí. Você já saiu com alguém da redação?"

            w "Quê?!"

            mc "É. Não tô falando de ficar. Só de sair, conversar e algo assim."

            w "O que isso tem a ver com você, [mc]? Eu tô... nem sei o que falar."

            mc "Só responder."

            w "Até parece..."
        "O que você faz além de trabalhar?":


            mc "Acho que eu vou aproveitar pra te fazer a pergunta que eu sempre quis."

            w "Hm?"

            mc "O que você faz além de trabalhar? Existe alguma coisa?"

            w "..."

            mc "Nada?!"

            w "Claro que sim, idiota! Mas eu não vou te responder. Isso é algo muito pessoal."

            mc "Perguntar o que você faz fora do trabalho é pessoal demais pra você?"

            w "E se for? Isso não tem nada com você."

    mc "Ei... calma..."

    mc "Isso aqui é normal, [w]. É igual como se a gente tivesse no trabalho conversando. Não precisa ficar tão na defensiva asssim."

    w "Não tem nada a ver com o trabalho, [mc]. Lá a gente tem um motivo pra conversar. Aqui a gente só tá, sei lá... se relacionando."

    mc "Como é? Explica isso aí."

    w "Você é meio enxerido, não acha?"

    mc "Só tô tentando puxar conversa. Você que é fechada demais."

    w "Questão de perspectiva."

    mc "Você pode só me explicar isso então? Qual a diferença de conversar comigo aqui ou no trabalho?"

    w "Isso é óbvio. No trabalho a gente fala sobre trabalho. Eu preciso falar com você pra desenvolver meu trabalho."

    w "Agora, aqui, a gente não tem motivo nenhum pra conversar. Qual o objetivo dessa conversa? Não tem porque falar nessas horas."

    mc "O objetivo é a gente se conhecer e se divertir. E nem tudo precisa ter um motivo na vida também."

    mc "Sabe, acho que você é uma pessoa muito racional. Você não consegue viver só por viver. Por isso pensa desse jeito."

    w "Que bom, né? Ficar se emocionando só atrapalha nosso julgamento. Quem toma decisão no 'calor do momento' só entra em problema."

    mc "Talvez..."

    w "Como assim talvez?"

    mc "Não sei se ser racional é tão melhor assim. E se no fundo você é assim porque você não sabe lidar com seus sentimentos?"

    mc "Você esconde eles nessa pilha de razões e porquês pra não precisar olhar pra eles."

    w "Nossa, mas você tá muito terapeuta hoje, né? Insuportável."

    mc "Tá bom. Parei."

    w "..."

    gar "Boa noite, querido amigo e inestimável amiga."

    scene so4_bar3 with Dissolve(1.0)

    pause

    mc "Fala aí, [gar]."

    w "Boa noite."

    gar "É um prazer imensurável ter com figura de tamanha hierarquia e pompa em meu humilde antro de prazeres banais."

    w "Está falando comigo?"

    gar "Com quem mais seria, nobre companheira de ferrenho trabalho?"

    mc "Ei. Não pode ser eu a figura de hierarquia e pompa?"

    gar "Não seja tomado pelo terrível pecado capital da inveja, senhor [mc]. O mundo não gira em torno de nós."

    mc "Touché."

    gar "Não pude deixar de notar que esta incrível personificação da árdua atuação em prol do bem coletivo parece um tanto quanto abatida."

    w "Por que você fala desse jeito?"

    gar "Ora, destemida... não permita que o formato prejudique o conteúdo de minha mensagem. Sou apenas um mero servo de ilustres presenças."

    w "Ele tá fazendo isso de propósito?"

    menu:
        "Não sei. Ele é sempre assim.":


            mc "Não faço ideia. Ele fala assim desde a primeira vez que eu vi ele aqui no bar."

            w "Que coisa, hein?"

            gar "Oh! Sinto-me lisongeado com tamanha atenção dedicada ao meu falar, queridos."
        "Eu já desisti de entender esse cara.":


            mc "Só ignora. Pelo menos é o que eu faço. Faz tempo que eu desisti de entender por que ele fala desse jeito."

            w "Parece que ele é de outro tempo..."

            gar "Não gastem demasiado tempo de vossas vidas terrenas com banalidades, como meus singelos trejeitos."

    mc "Tá vendo?"

    scene so4_bar4 with Dissolve(1.0)

    gar "O que merece a atenção de meus amados convidados, esta noite, é face desolada desta musa inspiradora."

    w "Você também vai encher meu saco agora?"

    gar "Muitas vezes, senhorita, levantamos paredes que cercam nosso ser. Nos acomodamos na segurança trazida por essa fortaleza e ficamos assim, inertes."

    gar "Esses muros escuros e maciços encarceram nossa própria individualidade. O que se vê, é um casulo seco. Lá dentro, a larva espera."

    gar "Entretanto, como a larva, não podemos ajudar. Se forças externas quebram o casulo, a larva morre. Ela própria deve fazer isso, de dentro para fora."

    gar "Somente a borboleta que quebrou a matéria inerte pode voar. Esse processo, doloroso e lindo, acontece com a triste raça humana também."

    w "Grande parábola. O que você quer me dizer com tudo isso?"

    gar "Oh! Não não não, senhorita. Eu não teria tamanha audácia de sugerir algo perante tamanha sabedoria."

    w "Mas então..."

    gar "A humilde metáfora é para nosso amigo, nosso senhor [mc]."

    mc "E-eu?! O que eu tenho a ver com casulos e tudo isso?!"

    gar "Ora, use esse trambolho sobre seus ombros para algo, senhor. Estarei aqui caso precisem de mim."

    scene so4_bar16 with Dissolve(1.0)

    pause

    mc desconfiado "Q-que loucura foi essa?"

    w "Por um instante achei que ele ia me passar uma lição de moral sobre ser fechada ou alguma coisa assim. Sorte que ele foi embora."

    "O que será que o [gar] quis dizer com tudo isso?"

    "Espera... ele começou falando que a atenção deveria ser na cara triste da nossa 'musa inspiradora'. Ele não falaria isso sobre mim."

    "A [w] realmente tá com uma cara péssima. Foi por isso mesmo que eu trouxe ela aqui."

    "Será que o que o [gar] quis dizer é que ela precisa se soltar? Eu concordo. Foi por isso que eu vim com ela."

    "Pior que nossa conversa começou super mal. Se o [gar] não tivesse aparecido, a gente já ia tá brigando."

    "Tá faltando alguma coisa."

    w "[mc]. Eu quero ir embora. Isso aqui não tá funcionando."

    mc surpreso "N-não. Espera!"

    w "Obrigada por me trazer, por tentar me ajudar, mas essa não sou eu. Eu não me sinto bem aqui. Essa não é minha... coisa."

    "O clima aqui tá indo de mal a pior. Não sei o que eu tinha na cabeça quando resolvi chamar ela."

    "Será que é melhor a gente só acabar tudo? Talvez ela se sinta mais confortável indo pra casa e só dormindo."

    "Mas eu queria tanto que ela se divertisse... se soltasse um pouco. Se eu desistir agora, vai saber quando vou conseguir isso de novo."

    "Merda... eu continuo ou não?"

    menu:
        "Tudo bem. Vamos embora pra casa.":


            $ sofia_e4 = "desistiu"

            mc concentrando "Tá. Se você realmente não tá curtindo, então eu jogo a toalha."

            w "Ufa..."

            mc "Desculpa por ser cabeça dura. Eu só queria que você tirasse um pouco a cabeça disso tudo."

            w "Tudo bem. Eu te entendendo. Pra falar a verdade, até eu queria tentar alguma coisa diferente... senão não teria aceitado vir."

            mc normal "Mas a gente vai encontrar alguma coisa que você vai gostar de fazer."

            w "Tá me ameaçando?"

            mc "Você que tá exagerando agora haha..."

            w "O futuro a gente vê depois. Vamos?"

            jump sofia_e4_fracasso
        "Não. Você ainda nem deu uma chance.":


            mc serio "De jeito nenhum. Você ainda nem deu uma chance pra nossa noite. Tá só com essa cara cu aí."

            w "Afe, [mc]... não me deixa desesperada fazendo parecer que a gente vai ficar mais meia hora aqui."

            mc charmoso "Tá brincando, né? Claro que vai ficar mais de meia hora."

            w "Por favor, alguém atire um dardo no meu pescoço..."

            mc "..."

            "Bom... mesmo com esse jeito agressivo, parece que ela tá se animando um pouco."

            "Eu não posso desistir da noite assim. Força, [mc]."

    scene so4_bar5 with Dissolve(1.0)

    mc "Sair com amigos é bem diferente de sair sozinha. Agora eu tô aqui com você, você vai se sentir melhor. Só precisa relaxar um pouco."

    w "Não é só isso, [mc]. Você não entende? As pessoas são diferentes. Você nasceu pra isso, eu não."

    mc "Eu acho que você fala muito assim. Como se você já tivesse certeza que não vai gostar."

    w "Porque eu me conheço."

    mc "Tá, pode até ser. Mas você nunca veio aqui. Aposto que nem vai em outros bares. Como você pode ter certeza?"

    w "Porque... porque eu sei o que acontece nesses lugares."

    mc "Tá vendo? Você acha as coisas e daí criou tipo uma barreira que não deixa você aproveitar."

    w "Você não sabe nada sobre... sobre o que rola comigo. E se eu era baladeira?"

    mc "Você? Baladeira? Tu acha que eu sou uma anta?"

    w "..."

    mc "Olha... e se você começar só tentando tirar essas coisas da sua cabeça? Dá uma chance. Sem preconceitos."

    w "..."

    w "Talvez você até tenha uma certa razão. Mas eu não consigo. Não é fácil assim."

    menu:
        "Eu sei. Só tenha calma.":


            $ sofia_amizade += 1

            mc "Claro. Nada novo é simples. É igual aprender a andar. Primeiro levanta."

            w "Afe, para de ser condescendente."

            mc "Nem sei o que isso significa."

            w "Então vai pesquisar no dicionário..."

            mc "[w]. Eu tô tentando aqui. Você também podia ajudar."

            w "..."
        "Para de graça. É só um bar, pô.":


            mc "Pra que toda essa tempestade em copo de água? É só um bar, caramba."

            w "Pra mim não é só um bar! Você não entende?!"

            mc "Tá bom, tá bom. Eu sei, desculpa."

            w "Se você não tem paciência, por que tá aqui comigo? Só vamos embora."

            mc "Eu entendi... calma."

    mc "Não é fácil pra você. Mas não é impossível também. Só vamos começar do zero. Esquece e só conversa comigo, só isso."

    w "Você já falou isso umas três vezes. Não muda nada."

    "Cara. Por que nada do que eu falo funciona com a [w]? Eu já falei com celebridades, garotas muito mais famosas e tudo o mais..."

    "Mas com ela simplesmente não consigo. Não consigo fazer ela confiar em mim. Não consigo fazer ela se sentir à vontade."

    "Acho que... é um caso perdido..."

    w "[mc]... acho que agora eu quero ir em-"

    scene so4_bar2 with Dissolve(1.0)

    gar "Com licença, minha senhoria."

    w "..."

    mc "O que foi, [gar]?"

    gar "Gostaria de saber se vocês pretendem consumir alguma coisa deste humilde estabelecimento."

    w "Verdade... a gente tá aqui e nem pediu nada. Mas eu já tô sain-"

    mc "Não. Pera. Eu vou pedir algo pra gente."

    w "Mas-"

    mc "Sem 'mas'. Eu prometo que depois da bebida você pode ir. Pelo menos um drink."

    w "... tá bom. Só que depois eu quero ir. Combinado?"

    mc "C-combinado."

    w "E eu vou querer um suco natural."

    mc "[w]... a gente tá em um bar..."

    w "Por acaso não tem suco aqui?"

    scene so4_bar6 with Dissolve(1.0)

    pause

    gar "Se me permite, senhor [mc], gostaria de sugerir uma bebida de nossa especialidade. Uma receita passada de geração em geração neste antro."

    w "É alcoólico?"

    mc "[gar]... você tá falando sério? Aquela bebida?"

    gar "Apenas uma dose para a senhorita entender a intrínsica diferença entre um bar de raízes e uma lanchonete familiar."

    w "Eu não quero álcool."

    mc "Eu sei que você não tá acostumada, mas é um bar, [w]. Você precisa pelo menos experimentar."

    w "Nem adianta você tentar. Não perca seu tempo."

    mc "Olha... eu sei que você tá querendo algo diferente. Você nunca aceitou sair comigo. Nem tomar um café."

    mc "Agora, hoje você veio até o bar comigo. Eu já achei impossível só por isso."

    w "E daí?"

    mc "Quer dizer que você tá procurando alguma coisa diferente, você não acha? Talvez no fundo você queira mudar alguma coisa."

    w "..."

    scene so4_bar9 with Dissolve(1.0)

    mc "Talvez essa seja sua chance. Você tá com um amigo de trabalho, em um bar do lado do trabalho, tomando só uma dose. É um passo de nada."

    w "Mas... o que isso vai mudar?"

    mc "Parece pouco, mas pode ser um começo de algo maior. Tipo, de uma mudança pra melhor."

    w "V-você... prometeu que não vai tentar nada estranho comigo hoje, c-certo?"

    mc "Ainda tem isso. Você tá praticamente com uma mulher do seu lado. Eu falei que não vou fazer nada. Pode confiar em mim."

    w "Mesmo assim... e se eu ficar bê-bêbada?"

    mc "Mesmo que você fique..."

    "E com certeza ela vai ficar depois de beber essa bebida mágica do [gar]."

    mc "Se ficar bêbada, logo passa. Eu vou ficar com você o tempo todo. A cabeça só fica um pouco mais avoada. Não tem nada de mais."

    gar "Eu garanto que a senhorita se sentirá nas alturas. Uma sensação inesquecível e deveras positiva."

    w "Eu não sei se eu confio em você, [mc]... vo-você é um homem apesar de tudo."

    mc "Apesar de tudo o quê? Quer dizer... pensa em tudo o que eu fiz por você na redação. Será que eu não mereço um voto de confiança?"

    $ renpy.notify("Sofia está lembrando das suas ações passadas")

    w "Espera... deixa eu pensar..."

    scene so4_bar6 with Dissolve(1.0)

    gar "Senhores."

    gar "Aqui está. Senhorita... até já servi vossa excelência. Basta aceitar."

    w "E-espera!"

    w "Eu..."

    if sofia_amizade >= 21:

        $ sofia_e4 = "sucesso"

        scene so4_bar10 with Dissolve(1.0)

        w "Tá! Tá bom! Mas só um drink! E depois a gente vai embora."

        mc "Boa! Isso aí, [w]! Esse é o espírito."
    else:


        $ sofia_e4 = "fracasso"

        w "D-desculpa! Mas não!"

        scene so4_bar9 with Dissolve(1.0)

        mc "[w]..."

        w "Eu disse que não queria, [mc]. Talvez um outro dia, mas hoje não. Eu não tô pronta e nem sei se eu quero isso."

        mc "Tudo bem. Tá tudo legal."

        w "Eu sei. Só vamos embora."

        jump sofia_e4_fracasso

    mc "Começa devagar. Só toma um gole."

    w "Tá bom."

    w "{i}gulp{/i}"

    w "..."

    mc desconfiado "[w]?"

    scene so4_bar7 with Dissolve(2.0)

    pause

    mc surpreso "S-sofia?!"

    w "[mc]... eu tô sentindo um calor... I-isso é normal?"

    mc "S-s-sim..."

    w "Minha cabeça tá rodando... eu tô... me sentindo... muito... ai... muito bem..."

    mc zerado "[gar]... você realmente acha isso uma boa ideia?"

    gar "Boa sorte, senhor [mc]."

    mc "Ei..."

    w "Parece que... não tem ar suficiente pra mim... eu tô zonza... mas quente... e minha cabeça tá... vazia..."

    w "Eu quero rir e falar... e eu preciso de atenção... você tá olhando pra mim?"

    window hide

    pause

    mc envergonhado "T-tô sim..."

    scene so4_bar12 with Dissolve(1.0)

    w "Calma... eu tô melhorando um pouco... aah... que sensação diferente... eu quero levantar... minha perna tá se mexendo sozinha..."

    mc preocupado "C-calma, [w]. Fica sentada."

    w "N-não! Eu não c-consigo..."

    mc envergonhado "Fala comigo. Presta atenção no que eu tô falando."

    w "Você tá falando?"

    mc preocupado "Isso não dura tanto. Só relaxa... fala pra mim o que você tá pensando."

    w "Tô pensando... tô pensando que tudo é muito louco... nunca vi o mundo desse jeito."

    "Nossa... a [w] deve ser aquelas bêbadas chatas. Será que foi uma boa ideia?"

    w "Eu queria só poder ficar assim, [mc]..."

    mc envergonhado "Assim como?"

    w "Só assim..."

    mc zerado "Assim?"

    w "Com a cabeça vazia... ficar assim só por uns minutos... sem lembrar dos problemas. Sem sentir todo mundo me cobrando."

    mc desconfiado "Todo mundo te olhando?"

    w "É. Todo mundo me olhando e me obrigando ser perfeita. Me obrigando a manter tudo em ordem. É por isso que elas gostam de mim."

    w "Mas ficar assim o tempo todo é cansativo... as pessoas... as pessoas podiam gostar de mim mesmo fazendo coisa errada."

    w "Seria mais... legal... se eu só pudesse viver normal e as pessoas ainda me ouvissem..."

    mc desculpa "Seria mesmo..."

    scene so4_bar8 with Dissolve(1.0)

    w "Esse povo maldito podia só desaparecer! Só viver a gente, [mc]! E o [gar], claro... mas meu pai podia morrer também. Seria legal..."

    menu:
        "Seria legal mesmo. Com certeza.":


            mc "Seria legal mesmo. Imagina?"

            w "Claro que eu imagino! Esse povo idiota e incompetente! Que fica achando que eu sou idiota e incompetente..."

            mc "Vai tudo pro fogo."

            w "Hihihi... tudo pro fogo, [mc]..."
        "Não sei... parece exagerado...":


            mc "Eu não sei, [w]... parece um pouco exagerado."

            w "Para de ser medroso, [mc]! Eu sei que você odeia meu pai! Pode falar!"

            mc "Se eu odeio ou não, isso não importa. Querer sumir com as pessoas é um pouco demais."

            w "Acho que você precisa de um drink também... só isso..."

            mc "Haha... passo. Alguém precisa ficar de olho em você."

    w "[mc]... você é a única pessoa que eu confio. Por isso eu falo tudo pra você assim. Ninguém mais viu que eu tava acabada."

    w "Nem meu pai vê que eu tô cansada... cheia de tudo isso. Ele nem liga pra mim. Nunca ligou."

    mc "Vocês não se davam bem?"

    w "Sei lá... ele só tinha tempo pro trabalho. A revista era tudo pra ele. Ele se separou da minha mãe por causa disso."

    w "Acho que ela nunca perdoou ele por isso... a-acho que eu também não... mas não vou fugir igual ela fugiu..."

    mc desculpa "Isso é uma merda, [w]..."

    w "É... mas... e você? Você confia em mim, [mc]?"

    mc "Claro que eu confio."

    w "Que bom... isso é muito bom... legal mesmo..."

    mc "Acho que você tá meio alta demais..."

    scene so4_bar11 with Dissolve(1.0)

    w "Claaaro que não! Hihihi... só aconteceu o que você falou... minha cabeça tá de vento... alguma coisa assim..."

    w "Aliás, [mc]... às vezes eu fico pensando que eu queria ser mais sexy eu acho..."

    mc envergonhado "Certo..."

    w "V-você me acha s-sexy? N-não, né?"

    mc "Que pergunta, hein, [w]?"

    w "Vai logo. Só responde."

    menu:
        "Você é bonita, mas sexy... complicado...":


            mc "Não me leve a mal, mas quero ser sincero com você."

            w "Já entendi. Pode parar..."

            mc "Calma. Eu acho que você é uma garota linda. De verdade. Você não tempo pra se arrumar, e mesmo assim dá pra ver que você é bonita."

            mc "Eu acho que nenhum homem iria negar você pela sua aparência. Tô falando sério. Não precisa se preocupar com isso."

            w "Você tá falando sério? Mesmo eu usando sempre a mesma roupa e não me maquiaando e nem penteando o cabelo?"

            mc "Sim. Pelo menos pra mim... eu acho você bonita."

            w "O-obrigada, [mc]... agora acho que fiquei com vergonha..."

            mc "Haha... a bebida te deixou meio sincera."
        "Sim. Eu acho você sexy.":


            mc "S-sim... eu acho você sexy. Claro que é de um jeito seu, só que, sei lá, a forma que você tem controle da situação e tudo..."

            mc "E ainda mais agora depois que você bebeu... sei lá... você tá bem sexy."

            w "E-eu não esperava essa resposta... achei que você ia mentir... mas do jeito que você falou pareceu de verdade."

            w "Obrigada... eu... nem sei o que falar. Eu nunca pensei que alguém me achava s-sexy..."

            w "Eu não me cuido e nem nada..."

    w "[mc]... eu f-fiquei com vontade de ser sexy agora..."

    mc surpreso "C-como?!"

    w "Não tem ninguém no bar agora... e até o garçom sumiu..."

    mc zerado "Sumiu mas deve tá ouvindo tudo de algum lugar..."

    w "E-eu não me importo. Eu quero... eu vou subir aqui..."

    scene black with Dissolve(1.0)

    mc "S-sofia! V-você-"

    w "Xiu..."

    scene so4_bar13 with Dissolve(2.0)

    pause

    w "Eu tô sexy agora?"

    mc charmoso "Com certeza."

    w "Hihi... faz muito tempo que eu não faço algo assim..."

    w "Quem sabe... já que minha blusa tá quase saindo... eu podia tirar ela completamente..."

    mc surpreso "C-como?!"

    w "Só uma gracinha, [mc]. Não precisa ficar todo eriçado desse jeito."

    mc envergonhado "[w]... acho que você tá indo longe demais..."

    w "Para de ser chato. Vou tirar."

    mc surpreso "T-tá louca?!"

    "Ver a [w] sem roupa ia ser demais, mas não dá pra deixar ela fazer isso. Ela tá completamente fora do juízo."

    w "3... 2..."

    mc "!!!"

    mc "Vem aqui!"

    scene so4_bar14 with Dissolve(1.0)

    pause

    mc "Não vai tirar nada."

    w "Ei! Quem é você pra me impedir?!"

    mc "Você não tá em condições de decidir sozinha esse tipo de coisa."

    w "Hihi..."

    mc "Que foi?"

    w "Acho que você é o primeiro cara que fica nervoso comigo assim... É legal..."

    mc "Só se for pra você. Imagina se o [gar] volta ou alguém entra e você tá sem roupa deitada no balcão?"

    w "Seria incrível mesmo."

    mc "N-não foi isso que eu disse!"

    w "Ai... eu tô nos braços do meu herói..."

    mc "Vamo pra casa..."

    w "[mc]..."

    mc "Oi."

    scene so4_bar15 with Dissolve(1.0)

    pause

    w "Desde que eu voltei pro país depois de me formar... eu não deitei com ninguém ainda..."

    mc "Que que tem?"

    w "Ora... você foi um cavalheiro hoje... e eu já tô no seu colo... o que você acha de me levar até seu apartamento..."

    mc "Q-quê?!"

    w "Você não quer que eu seja mais direta do que isso, né?"

    mc "M-mas você fez eu prometer que não ia tentar fazer nada com você hoje."

    w "Eu... tô dando permissão... tipo... estou revogando nosso acordo anterior... o que você acha?"

    "Levar a [w] pro apartamento agora? Assim? Do nada?"

    if sofia_namorar:

        "Claro que eu quero! Eu decidi na Faux que eu quero ter algo com ela."

        if sofia_beijo:

            "Rolou até aquele beijo..."

        "Eu tenho bem claro o que eu quero com ela. E agora ela se oferece assim, de bandeja?"

        "Só que... e a promessa? Eu disse que não ia fazer nada..."

        "Mesmo que agora ela diga que não vale mais, eu fiz essa promessa pra [w] que ainda tinha alguma coisa na cabeça."

        "Essa bebida faz alguma coisa com as pessoas... não dá pra levar a [w] de agora completamente a sério."

        w "E aí? Sua casa é aqui perto, né? Aproveite enquanto a bebida ainda tá aqui na cabeça."

        mc "Então..."

        menu:
            "Eu não posso. Eu prometi que não faria.":


                pass
    else:


        "Eu decidi lá na Faux que não quero nada assim com ela. Então não dá pra rolar."

        "Como eu falo isso sem ferir os sentimentos dela? Talvez..."

    mc "Olha..."

    mc "A verdade é que eu ia querer levar você pra casa, óbvio. Mas não vai dar."

    w "Sério? Por que?"

    mc "Eu prometi que não ia fazer nada."

    w "Mas eu tô falando que você pode, [mc]..."

    mc "Eu sei. Mas você não tá no seu juízo perfeito. Praticamente nem é a mesma pessoa."

    w "Você vai se arrepender se me negar hoje. É uma chance única."

    mc "Quem sabe... mas as coisas podem mudar. E, como você disse, eu sou um cavalheiro."

    w "Se você prefere assim, então tá, né? Mas eu tô facinho..."

    mc "Quem diria que um dia eu ouviria você falando assim e seria eu recusando..."

    w "A vida da voltas... igual o telhado desse bar."

    mc "Você precisa de açúcar urgente... Ah! Vou acompanhar você em casa."

    w "Que nada. Não precisa disso. Só me colocar no chão e eu dou meu jeito."

    mc "Sério mesmo? Mas você-"

    w "Xiu. Eu sei me cuidar. UBERRR!!!!"

    jump sofia_e4_final

    label sofia_e4_fracasso:

        mc "Beleza. Vou chamar um Uber pra você. É o mínimo, já que eu que te chamei."

        w "Tá bom. Eu aceito."

        w "[mc]... mesmo a noite não sendo perfeita, eu gostei de sair com você."

        mc "Eu também. Quem sabe um dia a gente não repita e tente algo mais sua cara?"

        w "Acho difícil, mas quem sabe... e a gente se vê amanhã no trabalho pelo menos."

        mc "Uhuuull..."

        w "E para de fingir. Eu sei que você ama."

        mc "Claro... até mais, [w]. E já tá pago no cartão."

        w "Tá bom. Até, [mc]."

        mc "Tchau tchau."

        "..."

    label sofia_e4_final:

        scene black with Dissolve(1.0)

        scene mc bar_celular with Dissolve(1.0)

    "Bom... a gente não ficou, mas foi uma primeira tentativa até que bem interessante."

    "Mesmo ela falando daquele jeito, eu sei que a gente pode sair mais vezes."

    "A [w] tá cheia dos problemas e isso tem a ver com pai dela... vai ser difícil fazer ela se abrir comigo... se ela não tiver bêbada..."

    "Mas ela com certeza é interessante e eu tô louco pra sair com ela outra vez."

    "Agora... o lance da redação... aquilo realmente tá complicado. Será que vai ser impossível impedir a Faux?"

    "Eu não vou ser só um espectador também. O [lu] tá contando comigo. Eu preciso decidir o que fazer."

    "De uma forma ou de outra, eu tenho que ver o que é melhor pra mim... tentando salvar o máximo de pessoas que eu puder."

    "Não vejo a hora de ver o próximo capítulo dessa novela. É o que tá parecendo minha vida ultimamente. Que doideira."

    menu:
        "Espero que a Sofia fique bem...":




            scene black with dissolve

            scene cidade tarde with Dissolve(1.0)

            w "Eu tô que tô hoje..."

            "Motorista" "Hm? Falou comigo, moça?"

            w "Essa hora... logo antes do guarda chegar... motorista..."

            "Motorista" "Não entendi. Desculpa."

            w "Eu vou pra outro lugar. Acabei de atualizar aqui o trajeto. Você pode ir comigo?"

            "Motorista" "Ok. Sem problemas. Ué... é aqui do lado."

            w "Pois é..."

            w "É a hora certa..."

            "Motorista" "Você que manda."

            scene black with dissolve

            pause 1.0

            scene trabalho angulo with Dissolve(1.0)

            w "..."

            "???" "Hmmm!"

            w "Exatamente o que eu pensei... agora é todo dia assim praticamente."

            label so4_premium2:

                pass

            menu:
                "Chegar perto da sala da Cássia":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_30

                        jump so4_premium2

                    "Eu preciso ter certeza..."

                    scene black with dissolve

                    j "Isso mesmo..."

                    w "Sabia..."

                    scene sofia4_premium7 with Dissolve(1.0)

                    pause

                    j "Lambe com vontade!"

                    re "S-sim, dona Cássia!"

                    j "Se você quer que eu faça você gozar, você tem que merecer."

                    re "Eu vou ser uma boa... hmmm... garota..."

                    j "Não adianta só falar. Aliás, é melhor que você pare de falar e use logo sua boca pra outra coisa."

                    re "S-sim! {i}slhup{/i}"

                    j "Não é você que não gostava de mulheres? Que não queria nem me beijar?"

                    j "Dá pra imaginar que você ia estar agora chupando uma buceta, hm?"

                    re "Eu preciso... hmm... eu preciso sentir aquilo de novo..."

                    j "Você 'precisa', né?"

                    re "S-sim! Eu fico molhada o dia todo esperando... me masturbar não é mais o suficiente."

                    j "Você é ainda mais safada do que eu tinha antecipado."

                    re "Ah..."

                    j "E sabe muito bem como comer uma buceta. Esse lábio carnudo e essa língua... hmm..."

                    j "Vem! Esfrega mais!"

                    re "!"

                    scene sofia4_premium8 with Dissolve(1.0)

                    pause

                    j "Eu só vou te dar o que você quer se você me comer de verdade!"

                    re "Sim, dona Cássia!"

                    re "Hmmmm!"

                    j "Isso, delícia. Mostra que você adora quando eu uso você igual um vibrador."

                    re "Ah..."

                    j "Você adora, né? Quando eu te trato igual uma puta que é o que você é."

                    re "Hmmm!"

                    j "Isso mesmo, vadia. Você adora chupar minha buceta com essa boca suja! AHH!"

                    re "AAHNN!"

                    re "Por favor! Eu preciso!"

                    j "Sua bucetinha não aguenta mais?"

                    re "Não! Por favor, acaba com ela!"

                    j "Então me lambe, caralho!"

                    re "HMM!"

                    scene black with dissolve

                    scene sofia4_premium6 with Dissolve(1.0)

                    w "Não acredito que as coisas chegaram nesse ponto. Essa [re] não tem amor próprio?"

                    w "Como alguém pode cair tão fundo?"

                    "Mesmo sentindo aqui em baixo... e no meu seio... aah... eu nunca vou virar uma escrava."

                    w "Ai..."

                    "Por que ver isso mexe tanto comigo?"

                    "Uma idiota dominadora igual a Cássia! Ver ela abusando dessa profissional me deixa tão agitada!"

                    w "Eu nunca ia fazer isso... nem ia querer que fizessem comigo... ah..."

                    j "Muito bem, puta. Você me deixou excitada o suficiente. Você vai ter o que você quer!"

                    w "Finalmente... N-não... eu tenho que sair daqui agora... hmmm..."

                    "Se eu continuar aqui... pode ser que a Cássia me veja... ia ser o fim da linha pra mim."

                    "Eu vou embora agora."

                    menu:
                        "Ir embora pra casa":


                            "O que eu tô pensando? O que eu tô fazendo?!"

                            "Eu nunca vou ser igual essas duas. Eu tenho valores dentro de mim."

                            "Nem sempre é fácil resistir. Mas é um esforço de cada dia. E hoje eu vou fazer o que eu acho certo."

                            "Eu vou pra casa comer bolo e me resolver sozinha... muito mais saudável."
                        "Continuar assistindo as duas":


                            "Eu preciso ver até onde elas vão..."

                            j "Agora se ajeita que eu vou usar sua buceta."

                            re "ISSO!"

                            scene black with dissolve

                            scene sofia4_premium9 with Dissolve(1.0)

                            pause

                            re "ALELUIA!!! Eu tô sentindo na minha buceta! Aaann!!"

                            j "Sim, meu amor.. hmm... agora eu vou comer você com a minha."

                            re "Ahnn! Aah!! Era disso que eu precisava! Hmm!"

                            j "Sem dúvida você é a mais tarada que eu abusei. Até eu me assusto com o nível de tesão que você chega."

                            j "Melhor pra mim... essa buceta esfregando em mim igual uma louca é uma delícia! Hmmmm!"

                            re "Ahhn! É porque ela pega fogo! AAHnNN!"

                            j "Então deixa eu fazer você gozar logo!"

                            re "AHNN! ISSOO!!!"

                            scene sofia4_premium10 with vpunch

                            pause

                            re "Tá vindo, dona! Continua! AAHMM!! ASSIM MESMO!!!"

                            re "Essa sensação que meus buracos vão explodir! Esse calor na barriga! AAHMMMM!!!"

                            j "Eu tmabém vou gozar, meu amor! Sua buceta é uma delícia!"

                            re "AHMM!! ASSIM! VAIII!!! POR FAVOR!!!"

                            j "Esfrega sua buceta na buceta da sua dona, vai!"

                            re "S-sim, dona! Esfrega na buceta da sua putinha! AAHNN!!"

                            j "Isso! Hmm! Eu adoro ver você no seu lugar!"

                            re "ISSO! MEU LUGAR É GOZANDO IGUAL UMA PUTAAA!!! AAHHHHHH!!!"

                            j "Tô gozando, sua vaca!!! AAHNN!!!"

                            scene sofia4_premium10 with vpunch

                            re "NNNNNGHHH!!!!"

                            scene black with dissolve

                            scene sofia4_premium11 with Dissolve(1.0)

                            pause

                            re "Aah... aaah..."

                            j "Você tá destruída..."

                            re "N-não... eu quero mais... aah... eu aguento..."

                            j "Aguenta o caralho. Você é só uma viciada..."

                            re "Mais... esfrega mais... aah... haha..."

                            j "Eu tenho nojo de você. Completamente maluca."

                            re "Ssiim... aah..."

                            "{i}tdump{/i}"

                            j "Que barulho é esse?"

                            scene black with dissolve

                            scene sofia4_premium12 with Dissolve(1.0)

                            pause

                            w "Ah... hmm..."

                            w "N-não... só mais um pouco... eu vou terminar e tô saindo..."

                            w "Aah..."

                            "T-tão perto! Eu vou terminar e dar o fora daquí! Não me atrapalhe, Cássia!"

                            w "Nnghh..."

                            "N-não vai dar tempo! Eu preciso de mais tempo!"

                            "Ela vai me achar!"

                            menu:
                                "Parar tudo e fugir":


                                    "Ela não pode me ver assim!"

                                    scene black with hpunch

                                    w "D-droga..."

                                    scene sofia4_premium16 with Dissolve(1.0)

                                    j "Hmm..."

                                    j "Estou certa que tinha ouvido alguma coisa..."
                                "Continuar até o clímax e daí correr":


                                    "Não tenho como parar agora! Só mais 30 segundos!"

                                    "Não venha! Não venha!"

                                    w "NNGHH!! NGGGHHH!!!!"

                                    "Mais um pouco!"

                                    j "Olha, só..."

                                    "NÃÃOOOO!!!!"

                                    j "Parece que alguém está aproveitando minha sala como se fosse um filme pornô..."

                                    j "Eu diria que eu estou surpresa, mas no fundo eu não estou... tudo faz sentido agora."

                                    "O que eu fiz?! Fui pega num momento te tanta vulnerabilidade! E ainda mais por minha maior rival!"

                                    "E o pior! O que eu mais odeio! É que eu não consigo parar de sentir tesão!!!"

                                    j "Parece que você realmente precisa desse orgasmo, não é?"

                                    w "!?"

                                    scene sofia4_premium13 with hpunch

                                    pause

                                    w "AAHNN!!"

                                    j "Não tá conseguindo sozinha? Eu te ajudo..."

                                    w "Nnghhhh!"

                                    j "Xi... não precisa lutar... só aproveita e goza..."

                                    w "Ngnh... mmmngnnn..."

                                    j "Você quer esse alívio... você PRECISA desse alívio..."

                                    j "Sinta minha coxa roçando sua intimidade... você adora como ela é macia, mas é firme ao mesmo tempo."

                                    w "Aah..."

                                    j "Você tá sob meu comando... e eu mando você gozar agora."

                                    w "NNGH!!"

                                    j "Mais um pouco, né?!"

                                    j "Vamos tirar isso aqui que tá atrapalhando você."

                                    w "!!!"

                                    "Eu não consigo falar 'não' pra ela."

                                    "Tudo isso é bom DEMAIS!"

                                    scene sofia4_premium14 with hpunch

                                    pause

                                    j "Agora, sim! Sua boca é minha, seu mamilo é meu, sua buceta é minha!"

                                    w "Nnghhh! MMNGHH!!!"

                                    j "Isso! Você quer algo intenso, [w]! Você procura por isso há muito tempo!"

                                    j "Ninguém entende você! Mas eu te entendendo! Você só quer que alguém te coloque no seu lugar!"

                                    w "NNNGHH!!!"

                                    j "Toda essa pose! Todos com medo de você! No fundo você é só uma garotinha querendo uma figura que te domine!"

                                    w "NNGHH!! NNGHHHH!!!"

                                    j "Você não pode nada contra mim! Você só me obedece! E você ama isso!"

                                    w "NNGHHH!!! AAAHHH!!!"

                                    j "..."

                                    w "!?"

                                    j "Chega..."

                                    w "NNH!!!"

                                    j "Agora você vai me prometer que não vai ficar no meu caminho quando eu for comprar a revista."

                                    w "NGH!?"

                                    j "Se você me der sua palavra que vai ficar quieta e deixar eu me entender com o velho, eu te garanto a melhor gozada da sua vida."

                                    j "Se você não aceitar, eu paro aqui... e você NUNCA vai sentir esse clímax que você demorou tanto pra construir."

                                    j "E agora?"

                                    "Eu preciso! Eu preciso!"

                                    "Mas jogar fora tudo o que eu lutei só pra sentir esse prazer tão rápido?!"

                                    "Essa é uma decisão sem volta... e eu sinto que tem muito em jogo aqui! Muito mais que minha própria sanidade!"

                                    menu:
                                        "Aceitar e gozar!":


                                            "Não importa! Nada mais importa agora! Eu preciso sentir isso!!!"

                                            w "XXIMMM!!!"

                                            j "Boa garota..."

                                            scene sofia4_premium14 with vpunch

                                            w "aAAAAAGGGGHHH!!!!!"

                                            scene sofia4_premium14 with vpunch

                                            w "AAAAAAAHHHH!!!"

                                            scene sofia4_premium14 with vpunch

                                            w "NNNGGHHHAAAA!!!"

                                            w "Aah... aah..."

                                            j "Uau... nem nas minhas mais de três mil transas... eu vi um orgasmo igual a esse... parabéns..."

                                            j "E não se esqueça da sua promessa."

                                            w "!"

                                            "Eu tenho que sair daquí!"

                                            scene black with hpunch

                                            scene sofia4_premium16 with Dissolve(1.0)

                                            j "Você é honesta demais para o seu próprio bem, [w]..."

                                            j "A chance era pequena... mas eu sabia que cedo ou tarde você iria encontrar a gente neste horário..."

                                            j "O caminho está aberto pra mim agora."
                                        "Recusar e enfrentar a Cássia!":


                                            "Eu não posso! FORÇA, SOFIAAAA!!!!"

                                            w "UUAAAAAARRGHHH!!!"

                                            j "!??!??"

                                            scene sofia4_premium15 with hpunch

                                            w "NEM A PAU, VÍBORA!!!"

                                            w "Eu posso não ter controle total sobre meu corpo, mas nunca que você vai me usar pra conseguir o que você quer!"

                                            w "Essa redação é resultado do trabalho de dezenas, centenas de pessoas no passar dos anos!"

                                            w "E você não vai colocar essas mãos sujas nela, nem que eu tenha que virar uma freira!"

                                            w "Não confunda meu prazer pessoal com o trabalho de uma vida!"

                                            w "Usar a fraqueza das pessoas contra elas é coisa de filha da puta! E você é uma GRANDE FILHA DA PUTA!"

                                            j "..."

                                            w "Obrigada pelas suas puterias, mas nunca mais tente algo assim contra mim! PUTAAA!"

                                            scene black with dissolve

                                            j "Nossa..."

                                            scene sofia4_premium16 with Dissolve(1.0)

                                            j "Parece que o tesão virou raiva bem rápido..."

                                            j "Você pode fugir, 'chefinha'... mas agora eu sei seu segredo. Você é uma ser humana, como todas nós..."

                                            j "Pode ser que leve tempo... mas eu consigo dobrar você... igual eu dobrei TODOS que cruzaram meu caminho."
                "Desistir e ir pra casa":


                    "O que eu tô pensando? O que eu tô fazendo?!"

                    "Eu nunca vou ser igual essas duas. Eu tenho valores dentro de mim."

                    "Nem sempre é fácil resistir. Mas é um esforço de cada dia. E hoje eu vou fazer o que eu acho certo."

                    "Eu vou pra casa comer bolo e me resolver sozinha... muito mais saudável."
        "Não me interessa o que acontece com ela":


            pass



    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v36_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v36_fim","final","local")

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    call checa_final from _call_checa_final_5

    jump call_cidade

label sofia_evento5:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("so5_save", extra_info="so5_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ sofia_e5 = "evento"

    scene cidade rua_trabalho1 with Dissolve(2.0)

    pause

    "As coisas na redação parecem ter ficado mais suaves esses dias."

    "Tô achando que é por causa da [w]... ela parece menos irritada... ou será que é o contrário?"

    "Será que a chatice dela não tá me afetando tanto mais? Talvez a mesma coisa aconteceu com todos."

    "Talvez... a [w] realmente tenha conquistado o respeito de todo mundo."

    mc envergonhado "Ou eu tô viajando demais e nem tô percebendo mais o povo brigando."

    "Bom... mais um dia de trabalho, querendo ou não... provavelmente a [w] vai pedir pra eu anal-"

    "???" "U-hum! Okay, chefe!"

    mc desconfiado "Hm?"

    scene so5_img1 with Dissolve(1.0)

    pause

    "Hmm... o que a [j] tá falando com a garota da recepção? O nome dela era..."

    menu:
        "Carla":


            mc envergonhado "Acho que eu tô confundindo ela com outra garota..."
        "Rebeca":


            mc desconfiado "Será que era isso mesmo? Parecia outra coisa..."
        "[re]":


            "Isso! [re]!"
        "Hinata":


            mc zerado "Certeza que não era isso."

    "Certeza que era [re]."

    j "Ei, anjinha, se eu descobrir que você não tá contando tudo, você tá fora daqui sem pensar duas vezes."

    "Uou... a coisa parece quente aqui."

    re "E-eu nunca esconderia nada de você, senhora. Você sabe."

    "Parece que a [re] tá com a [j]. E elas não me viram ainda, o que é excelente."

    j "As engrenagens estão em movimento, bebê. Tome cuidado para não cair no meio delas e ser esmagada."

    re "C-claro."

    j "Minha porta não tem uma placa de chefe pendurada nela, mas sou eu quem manda em você, entende?"

    re "Sim, senhora..."

    "Certeza que falar assim com um colega de trabalho é crime... essa [j] é foda."

    mc normal "Ei. Bom dia."

    j "Pombinho, resolveu fazer algo de útil?"

    mc zerado "Como é? Eu sempre chego essa hora. Você que nunca vem trabalhar."

    j "Estar no trabalho e trabalhar são coisas totalmente diferentes, bebê. Eu trabalho conseguindo informações relevantes."

    scene so5_img2 with Dissolve(1.0)

    pause

    j "Atuar como jornalista não é obedecer as ordens de uma criança, igual você e alguns outros fazem aqui."

    j "Jornalistas de verdade estão onde a notícia está. Nós conseguimos furos e entrevistas incríveis para informar e entreter o público."

    menu:
        "Você até parece séria falando assim.":


            mc zerado "Quem vê pensa que você tá muito interessada no público falando desse jeito."

            j "Óbvio que eu me importo com os leitores. No fim, nós escrevemos pra eles."
        "E você se importa com isso?":


            mc desconfiado "E desde quando você se importa com esse tipo de coisa?"

            j "Eu sou uma jornalista acima de tudo, pombinho."

    mc desconfiado "Eu sempre pensei que você tivesse sua agenda."

    j "Minha agenda passa pelo crivo do público. Sem eles não existe revista, e portanto eles são essenciais."

    mc normal "Até interessante você falar isso."

    j "Muitas pessoas pensam mais em seu negócio ou em seus ganhos do que naqueles que eles atendem."

    j "Não importa se você tem uma revista, uma padaria ou instala ar condicionado. O mais importante é o seu cliente estar satisfeito."

    j "O segredo é conseguir o que você quer ao mesmo tempo."

    mc zerado "Ou seja... enganar todo mundo."

    j "Chame como quiser."

    mc "Eu sabia que você tava se saindo ética demais nesse papo."

    mc desconfiado "Mudando de assunto, eu escutei você causando com a [re]. Já tá bulinando outro funcionário?"

    j "Você nunca esqueceu aquela brincadeirinha que eu fiz com você e com a rainha das baixinhas, né?"

    menu:
        "Aquilo não foi brincadeira.":


            mc serio "Aquilo não foi brincadeira. Você ameaçou a carreira da [c] pra poder me manipular."

            j "Foi o que eu disse. Só uma brincadeirinha pra introduzir você a como as coisas funcionam por aqui."

            mc zerado "Como você consegue fazer isso parecer uma coisa boa é incrível..."
        "Nem lembrava mais disso.":


            mc charmoso "Que nada. Nem lembrava mais disso. Eu e a [c] superamos de boa sua maquinação de quinta."

            j "Que bom. Não quero que meu bebê fique de carinha virada pra mim."

            mc zerado "..."

    j "A [re] é uma garota que pegou a coisa rápido."

    mc desconfiado "Quer dizer que ela tá na sua já?"

    scene so5_img3 with Dissolve(1.0)

    pause

    re "A senhora [j] é a pessoa que me acolheu aqui na revista, [mc]."

    mc preocupado "[re]... isso não é 'acolher', tá mais pra 'cooptar'. Você realmente vai acreditar nessa mulher?"

    re "C-como você tem coragem de falar assim da senhora [j]?"

    mc zerado "Todas as desgraças que ela podia fazer comigo ela já fez. Manipulação, ameaça, sedução..."

    mc envergonhado "Não tem muito mais o que eu temer da [j]. Só falta ela mandar alguém me dar um tiro."

    scene so5_img4 with Dissolve(1.0)

    j "Você tá muito saidinho pro meu gosto, pombinho. Será que eu preciso reforçar alguns pontos pra você?"

    menu:
        "Depende de quais pontos...":


            mc safado "Quais pontos você vai querer reforçar? Dependendo do que for, eu topo..."

            j "Óbvio que você topa, pombinho. Homens sempre pensam com a cabeça errada."

            mc "É que é melhor assim..."

            j "Eu também acho melhor. Muito melhor..."
        "Não quero nenhum reforço seu.":


            mc envergonhado "Pode deixar seus reforços pra lá. Não faço questão, não. Normalmente eu me ferro."

            j "Isso depende mais de você, bebê. Se você se comportar, eu prometo que você vai gostar muito."

            mc "Sei não..."

    j "As coisas vão acontecer mais cedo do que você imagina, [mc]. Não vai esquecer das suas opções."

    mc desconfiado "Você tá falando daquele lance?"

    j "Eu tô falando das mudanças que vão acontecer aqui na revista. Você também tem um papel, esqueceu?"

    mc "Eu sei do que você tá falando."

    if venda_revista > 0:

        mc "Eu mandei uma ideia no chefe e na chefinha outro dia aí."

        j "Sério? Não creio..."

        mc "Eu falei das vantagens de vender a revista numa conversa que a gente tava na sala dele."

        j "Isso é perfeito. Continue assim e você vai cair no cercadinho certo."

        mc "Cercadinho?"
    else:


        mc "Eu não falei nada pra eles sobre a venda da revista. Eu tive chance, mas eu não quis."

        mc "Eu não sei se é a melhor coisa pra revista a Faux comprar tudo."

        j "Olha, pombinho... não sei de onde veio essa vontade de desafiar quem vai vencer, mas eu pensaria de novo."

        j "Você não tem mais muito tempo. A coisa vai acontecer logo logo. Se você ficar do lado deles, não vai ser bom."

        mc "Vamos ver..."

    j "O próximo passo já foi decidido e vai acontecer mais cedo do que você imagina."

    j "Falta pouco. Dê os passos certos e você vai ganhar muitas recompensas."

    scene so5_img3 with Dissolve(1.0)

    re "Eu já fiz minha escolha, [j]. Eu tô com você e não abro."

    j "Muito bem, bebê. Mas é senhora [j] pra você."

    re "D-desculpa."

    mc zerado "Você não precisa falar com ela desse jeito."

    j "É bom a gente colocar as pessoas nos lugares certos. Eu vou colocar você também."

    mc envergonhado "E qual é meu lugar?"

    scene so5_img5 with Dissolve(1.0)

    pause

    mc "C-cássia?!"

    j "Se você pudesse escolher um lugar... qual seria?"

    "O que a [j] tá fazendo no meio da redação?!"

    if not nathan_namoro:

        "Ela é maravilhosa... ela é gata, sensual... cheirosa..."

        "Mulherão da porra, sabe?"

        "E ela ainda tem essa aura de perigosa, de alguém que tá no controle da situação e pode te esmagar."

        "Não sei se isso dá medo ou tesão."

    mc "A g-gente tá no meio da redação."

    j "Que que tem, pombinho? Você tem medo de alguém aqui?"

    mc "E-eu?"

    j "Talvez de uma certa novinha magricela que gosta de mandar em todo mundo."

    mc "Você pega muito no pé da [w], sabia?"

    j "Ela acha que pode chegar e mandar em todo mundo?"

    menu:
        "Não é exatamente o que você faz?":


            mc "Só que... Isso não é exatamente o que você faz?"

            j "De forma alguma. São coisas bem diferentes, bebê. Eu trabalhei muito pra chegar onde eu estou."

            j "Eu conquistei esse espaço. Muito diferente do que a coisinha faz. O poder dela vem da posição. Eu conquistei sozinha."

            mc "Hmm... faz sentido até... mas-"

            j "Você falou o que importa. Não precisa continuar."

            mc "..."
        "Ela tá fazendo o trabalho dela.":


            $ sofia_amizade += 2

            mc "A [w] tá só fazendo o trabalho dela, [j]. A função dela é organizar as pessoas e falar o que elas devem fazer."

            mc "É bem diferente de só mandar nas pessoas igual você faz."

            j "Você realmente lambe o pé daquela guria. Eu e a [w] realmente somos diferentes. Mas não por isso."

            j "Eu conquistei o que eu tenho, mas a filhinha do papai só chega aqui com tudo na mão."

            mc "Eu não sei se isso é só uma questão de poder, [j]. Você olha muito as coisas por esse ângulo."

    j "A verdade é que eu prefiro você quietinho e seguindo o que eu falo."

    mc "Eu tenho minha cabeça também, né?"

    j "Aliás... Você ainda não me respondeu... qual cabeça você quer usar?"

    mc "N-nós ainda tamo aqui na redação! Para de falar assim!"

    j "Eu quero uma resposta sua agora, pombinho. Qual delas?"

    "Não acredito que a [j] realmente tá falando pra eu escolher isso agora."

    j "Minha sala tá vazia agora..."

    "Será que a [w] já chegou? Ia ser horrível se ela visse eu indo pra sala da [j] com ela..."

    "Mas a [j] falando desse jeito... se eu quero alguma coisa com ela, é melhor eu aceitar."

    "Ai, caralho... o que eu respondo?"

    j "Então? Qual cabeça você quer usar agora?"

    menu:
        "A cabeça de cima.":


            $ sofia_amizade += 3

            mc "Valeu, mas eu vou usar a cabeça de cima mesmo. É mais seguro. Você tá doida."

            j "É uma pena, [mc]. Eu tava louca pra gente fazer alguma coisa deliciosa juntos lá na minha sala..."

            j "Talvez tirar a roupa um do outro... você senta na minha cadeira... eu coloco a calcinha pro lado e você enfi-"

            mc "[j]! Tá bom!"

            j "Desde quando você ficou fraco e idiota desse jeito?"

            mc "Ei..."

            j "A vida é pra gente se divertir, [mc]."

            "???" "É bom saber que você mantém o mínimo de respeito próprio."
        "A cabeça de baixo.":


            $ renpy.block_rollback()

            mc "Óbvio que eu vou querer usar a de baixo. Não sou idiota."

            j "Era isso que eu queria ouvir, [mc]. Adoro ver você babando pra me comer. Eu já fico molhada só de pensar."

            mc "Então bora pra sua sala?"

            j "Vamos. Eu vou cuidar bem da minha cabecinha preferida. Eu tenho um lugar quentinho pra ela se divertir bastante."

            j "Será que você consegue fazer eu gozar gostoso?"

            mc "Com certeza."

            j "Então vem me comer, seu- {nw}"

            "???" "Consegue o quê, [j]?"

    mc "Hm?!"

    scene so5_img6 with Dissolve(1.0)

    pause

    w "Posso saber que pornografia é essa que tá acontencendo aqui?"

    mc "S-sofia?!"

    j "Veja quem tá causando, pra variar."

    w "Eu? Olha pra vocês! Onde vocês acham que tão?!"

    mc "E-eu posso explicar, [w]!"

    w "Você acha que isso aqui é um filme, idiota?! Que você fala desse jeito?!"

    mc "Foi tudo culpa da [j]!"

    j "Você podia ter pelo menos um pouco mais de bolas e assumir que você também queria."

    mc "E-eu?!"

    menu:
        "É só um abraço. Nada de mais.":


            mc "Calma aí, [w]. É só um abraço... nada de mais. Pelo menos por enquanto..."

            j "Haha... você é terrível. E eu gostei."

            w "Vocês tão fora de controle! Eu vou suspender vocês se continuar assim!"

            mc "C-calma! Eu não posso ganhar menos! Todo o salário que eu ganho aqui eu uso pra pagar as contas!"

            w "Azar o seu, idiota! Quem mandou fazer graça aqui no trabalho!"

            mc "D-desculpa..."
        "Foi tudo ela. É sério.":


            $ sofia_amizade += 2

            mc "Não quero saber disso, não. Foi tudo a [j]. Eu não queria nada disso, [w]."

            j "Agora você fala isso, né, descarado?"

            mc "Eu nunca quis nada disso, caralho!"

    w "Muito bonito vocês..."

    mc "É verdade, [w]!"

    w "E o que você ainda tá fazendo abraçado com ela até agora?"

    j "Eu sou cheirosa, gostosa e sexy, diferente de você, garota mimada."

    j "Os homens gostam de mulheres. E de mulheres que gostam do que eles gostam. Que é transar."

    j "Nenhum homem vai querer ficar perto de uma mulher que mais parece um garoto de cabelo comprido."

    w "Isso é um absurdo!"

    mc "M-melhor eu-"

    j "Cala a boca, pombinho. Deixa eu falar com ela."

    mc "E-ei!"

    scene so5_img7 with Dissolve(1.0)

    pause

    w "[j]! Você é o pior tipo de pessoa que existe! Você passa essa mão cheia de dedos no meio de tudo."

    j "O que isso tem a ver com você? Você é intrometida demais, não acha?"

    w "Enquanto eu for a gerente de produção da revista, é minha tarefa garantir que tá tudo bem com os funcionários."

    j "É isso que você diz pra você pra justificar sua síndrome de controladora?"

    w "Esse é seu problema. Você acha que todo mundo vive pelos parâmetros distorcidos."

    w "Você é egoísta, orgulhosa e manipuladora e acha que todo mundo é assim igual você. Mas as pessoas não são assim."

    w "Eu não tô aqui pra mandar nos outros. Eu quero ter a melhor redação do mundo e a melhor revista do mundo. Só isso."

    j "Você fala bonito, mas será que a gente é tão diferente assim?"

    j "Você já parou pra pensar do porquê você querer isso? De onde vem essa motivação?"

    w "E precisa de uma motivação pra querer ser a melhor?"

    j "Tá falando igual um personagem de desenho japonês. Você não passa de uma fedelha que não sabe nada do mundo."

    w "Q-quê?!"

    j "Além de ser complexada na relação com pai. Eu tenho certeza disso. Impossível ser criada por aquele velho e sair normal."

    w "Ele é seu chefe! C-como você pode falar isso?!"

    j "Por enquanto, fedelha..."

    w "..."

    j "Não importa o que você e o velho acham, quem decide o futuro da revista são os donos e eles não vão recusar."

    w "Meu pai pode ser um babaca quando fala com as pessoas, preconceituoso e várias coisas no mínimo questionáveis..."

    j "Finalmente algo em que a gente concorda."

    w "Mesmo assim, ele sabe o que é Jornalismo de verdade. Ele tá comprometido com a revista, do jeitão dele, mas tá."

    w "Ele não pensa só no bem dele igual você. E por isso os investidores escutam o que ele fala."

    w "E ele nunca vai concordar com o que você quer fazer aqui."

    scene so5_img8 with Dissolve(1.0)

    pause

    j "Será que... vocês realmente sabem o que é melhor pra revista? O que será que o [mc] acha?"

    mc surpreso "E-eu?!"

    j "Você é um profissional e funcionário da revista também. O que você acha melhor?"

    w "Não precisa colocar ele no rolo, [j]."

    j "Você não quer saber a opinião dele também?"

    mc envergonhado "Minha opinião sobre o que mesmo?"

    j "Não seria bom pra revista se uma empresa maior comprasse e melhorasse ela toda? Qual a vantagem de manter ela desse jeito?"

    w "A vantagem é que nós temos nossa liberdade! Aliás, nem acredito que você tá conspirando contra a revista abertamente desse jeito!"

    w "Pensei que fosse algo por baixo dos panos! Agora você falando assim, na frente dos funcionários?!"

    w "Meu pai pode despedir você por justa causa!"

    j "Acho que poderia, sim... mas será que ele realmente ia querer? Será que seu pai é tão contra essa ideia igual você?"

    w "Claro que ele é... E-eu tenho certeza."

    j "Essa incerteza na sua voz diz o contrário, pombinha. Você sabe que ele ainda não decidiu o que é melhor."

    "Por isso que a [j] quer minha ajuda pra fazer a cabeça dele..."

    "Se a compra da revista pela Faux desse certo e eu ajudar ela, eu vou ganhar um cargo melhor na nova revista."

    "Mas com certeza a [w] seria despedida."

    "Eu queria um emprego melhor... mas eu acho a [w] uma garota tão bacana."

    if sofia_namorar:

        "Eu tô super ligadão nela. Queria que rolasse alguma coisa entre a gente."
    else:


        "Mesmo não querendo namorar com ela, eu não sei se ela merece perder a revista que ela ama tanto."

    j "Responde, [mc]. Você acharia tão ruim assim a compra da revista por uma empresa maior?"

    w "[mc]..."

    "E agora? O que eu respondo?"

    menu:
        "Vender não seria tão ruim.":


            $ venda_revista += 1

            mc charmoso "Eu não acho que vender seria tão horrível assim, [w]."

            w "Q-quê?!"

            mc "Nós teríamos mais verba, além de mais experiência na casa com uma rede tão conhecida por trás."

            j "Está vendo, chefinha? Ele não acha tão ruim assim. Será que não é só você que é cabeça dura?"

            w "Vocês estão loucos..."
        "Vender é uma péssima ideia.":


            $ sofia_amizade += 3

            mc charmoso "Eu concordo com a [w]. Vender não é a melhor coisa. A gente precisa manter nossa linha editorial."

            mc "Se a gente aceitar vender, eles vão impor o que eles enxergam e isso provavelmente vai mudar a revista completamente."

            w "É isso que eu tô falando, pô!"

    w "A Faux transformaria a revista em mais um canal de manipulação."

    j "Teorias da conspiração agora?"

    w "Eu não tenho que falar isso pra você também. Não tô nem aí pra sua opinião, [j]."

    j "Não esquece que eu também sou uma funcionária da revista, tá?"

    w "Pra mim você não é mais nada. É uma verdadeira inimiga da revista!"

    j "Haha... pode esbravejar o quanto quiser. O inevitável é inevitável."

    w "Bah!"

    scene black with dissolve

    mc angustiado "S-sofia!"

    scene so5_img2 with Dissolve(1.0)

    pause

    mc serio "Você precisa fazer isso com ela?"

    j "Mexer com a guria é um excelente esporte pra mim."

    j "Acho melhor você ir atrás dela antes que ela resolva fazer alguma coisa ruim."

    if venda_revista >= 3:

        j "Você foi muito bem, [mc]. Depois eu vou te dar sua recompensa."

        scene so5_img5 with Dissolve(1.0)

        mc "Eu tava pensando em ganhar ela agora... se não fosse problema pra você."

        mc "Eu fui ou não fui um bom garoto?"

        j "Eu gosto de homens com iniciativa. Mas só até certo ponto."

        j "A gente transa quando eu quero, entende? Quem manda sou eu. Agora me solta e vai fazer seu trabalho com ela."

        j "Convença a garota que vender é o melhor pra revista. Nada pode acontecer comigo antes da hora."

        mc "Você é terrível..."

        j "E você adora. Agora vai, totó."
    else:


        mc desculpa "Isso é demais... quero ver quando der ruim pra você."

        j "NUNCA é a resposta."

        mc zerado "..."

    scene black with dissolve

    mc preocupado "[w]!"

    w "Que foi?!"

    scene so5_img9 with Dissolve(1.0)

    pause

    mc desculpa "Você tá legal?"

    w "O que você acha? Claro que não."

    mc envergonhado "A [j] é terrível, né?"

    w "Essa mulher é impossível. A cara de pau dela é impressionante."

    w "Ela fala na cara dura que tá organizando um golpe contra o meu pai. E o pior é que ele ainda mantém ela aqui."

    menu:
        "Não ligue demais pra ela.":


            mc envergonhado "Não dê tanta bola pra [j] também. Ela gosta de pegar no nervo das pessoas."

            w "Talvez você tenha razão, mas mesmo assim ainda é difícil pra mim."

            mc "Eu sei... mas a [j] é assim mesmo. Ela é esperta e entra na nossa cabeça."

            w "Você parece bem impressionado com ela."

            mc "Não se esqueça daquela frase famosa. Conheça seus amigos, e ainda mais seus inimigos."

            w "Nunca ouvi isso."

            mc "Hehe... talvez não seja exatamente assim..."

            w "..."
        "Eu posso ajudar com alguma coisa?":


            $ sofia_amizade += 1

            mc desculpa "Eu sei. Ela é horrível mesmo. Tem alguma coisa que eu posso ajudar?"

            w "Obrigada, mas isso é mais entre mim, meu pai e a [j]. Mesmo que isso influencie a vida de todos aqui."

            w "Eu preciso saber controlar melhor as conversas. Eu me deixo levar por ela e me perco..."

            mc envergonhado "Você tá no caminho certo pelo menos. Com um pouco mais de prática você nem vai ligar mais pras bobagens dela."

            w "A gente querendo ou não, não dá pra negar que a [j] é inteligente e sabe dominar uma discussão."

    w "Mas ela nem é o problema. É mais o que ela representa, sabe?"

    w "A [j] e a Faux não vão desistir até que eles comprem a revista e dominem todos os maiores veículos de comunicação da capital."

    w "Eles já dominam o telejornal, a internet, a maior rádio... as bancas todos os dias. Se eles pegarem a revista também, vão dominar o público."

    mc desculpa "Se só uma pessoa controlar todas as fontes de informação, é muito fácil pra ele convencer as pessoas, né?"

    w "Esse é o problema. A gente precisa de ideias divergentes. Ler só uma ideia fecha nossa cabeça pro mundo."

    w "A gente precisa saber o que quem não concorda com a gente pensa também. E por isso que o jornalismo de verdade é importante."

    w "Na faculdade a gente aprende que tem que ouvir sempre os dois lados e tentar ao máximo ser objetivo nas matérias."

    w "Isso é uma coisa que blogueiros, influenciadores e essas personalidades da internet que existem hoje não conseguem fazer."

    w "Eles não têm técnicas e nem a ética jornalística. Por isso uma revista séria e sem agenda por trás é importante pras pessoas."

    mc "Você acha que a Faux não faz isso?"

    w "Claro que não. Tem coisa demais sobre eles. Nada provado, só que onde tem fumaça tem fogo."

    mc "Ouvi falar que eles tão de rabo preso com os Donatello."

    w "Isso é o principal. Mas não é só isso. Tem muitas outras coisas que ninguém explica, tipo empresas fantasmas, evasão de divisas..."

    mc zerado "Caralho, que buraco sem fundo, hein?"

    scene so5_img10 with Dissolve(1.0)

    pause

    w "É... só que a gente tem que pensar de forma prática, sabe? O que eu quero é que a Faux não engula a gente só isso."

    w "Pelo que eu tô lembrando aqui daquela nossa conversa com o meu pai e o que você falou hoje..."

    if venda_revista >= 2:

        w "Parece que você é à favor da venda da nossa revista. Eu pensei que você não ia querer..."

        mc "Eu tô pensando no bem da revista. Eu entendo tudo isso que você falou. Mas quem sabe a Faux não seja tão ruim assim?"

        w "Não sei, [mc]... você é um cara com a cabeça no lugar, mas é meio ingênuo eu acho..."

        w "Eu não quero ser cabeça dura também, mas realmente não parece uma boa ideia pra mim."

        mc "Vamos esperar um pouco mais e acompanhar. Não vamos tomar nenhuma decisão por enquanto."
    else:


        w "Dá pra ver que você concorda comigo. Vender a revista não é a melhor opção pra gente. Eu fiquei feliz com isso."

        mc "Sim. Eu concordo de verdade com isso. A Faux tá doida pra colocar as mãos na revista e acho que não é um bom negócio."

        mc "Eu vou ficar do seu lado, [w]. Você é minha chefinha e eu acredito em você como profissional."

        mc "Você já deu várias provas pra mim que você sabe o que tá fazendo. Então se você não topa, eu também."

        w "O-obrigada pela confiança."

        mc "A gente tem que dar nosso melhor pra fazer a cabeça do velho."

    w "Você tem razão. Além de que nem somos nós que vamos decidir. Tudo depende do meu pai e do conselho."

    w "A gente pode influenciar um pouco, talvez, mas ele tem aquele jeitão dele. Você sabe como ele é, né?"

    mc "Eu sei muito bem... o desgraçado é um pé no saco."

    w "Mesmo sendo meu pai, eu não tenho como falar que você tá errado. Eu já falei que ele é truculento demais, mas ele nem liga."

    w "Por isso que mesmo eu sendo a gerente eu não tenho muita influência. Ele nunca me ouviu, não ia ser depois de velho que ele ia começar."

    mc "Tem certeza? Na nossa conversa aquele dia ele parecia tá prestando bastante atenção no que você tava falando."

    w "V-você acha? I-impossível, [mc]..."

    mc "É sério. Seu pai é cabeça dura, mas eu sinto que ele é diferente com você. Mais educado do que comigo ele é com certeza."

    w "Não sei... mas se você tá falando..."

    mc "É sério. Eu realmente acho isso."

    w "Se isso é verdade..."

    mc "Hm?"

    scene so5_img11 with Dissolve(1.0)

    pause

    w "Valeu por compatilhar isso comigo."

    mc envergonhado "Só tô falando o que eu acho."

    w "Meu pai nunca foi de ouvir. E ele sempre foi fechadão. Eu sempre senti que tava falando com uma porta."

    w "Mas se você acha que ele escuta... então talvez a gente tenha uma chance, certo?"

    mc normal "Com certeza."

    w "Só que antes a gente precisa afinar nosso discurso. E antes disso ainda... a gente precisa ter certeza do que a gente quer."

    w "Você... toparia tirar o dia hoje pra gente conversar sobre isso?"

    "Opa... a [w] parece interessada na minha opinião. Acho que trabalhar direitinho fez eu ganhar uns pontos com ela."

    menu:
        "Só nós dois? É um convite?":


            mc charmoso "Só nós dois? Será que é o que eu tô pensando que é?"

            w "Com certeza não. Não é pra você começar a ter ideias estranhas."

            mc "Mas-"

            w "Nada de 'mas'. É só pra gente conversar."
        "Claro. A gente precisa discutir isso.":


            $ sofia_amizade += 1

            mc "Pode contar comigo, claro. A gente precisa acertar isso pra depois não ter problema."

            w "Isso. Tendo certeza do que a gente quer, vai ficar mais fácil de passar para os outros da redação e até pro meu pai."

    w "Só que conversar aqui vai ser complicado. A gente não sabe onde a [j] tem ouvidos aqui."

    mc desculpa "Verdade. Dá pra ver que a [re] também tá passando coisa pra ela."

    w "A gente vai se sentir mais à vontade fora daqui. Onde você acha que seria uma boa ideia?"

    "Uou... sair em algum lugar com a [w]?"

    "Mesmo que seja pra um lance sério, dependendo do lugar que a gente for as coisas podem evoluírem pra algo mais casual... uma happy hour talvez..."

    w "O que você acha de ir pra minha casa?"

    mc surpreso "Q-quê!?"

    w "Não precisa fazer essa cara. É só porque é um lugar que eu tenho certeza que ninguém vai ouvir a gente."

    mc envergonhado "M-mas sua casa?"

    if sofia_namorar:

        "Por que eu tô questionando essa sugestão?! É minha chance de passar um tempo sozinho e na casa dela ainda!"

        if sofia_beijo:

            "Talvez seja minha chance de falar sobre aquele beijo que rolou na Faux."

        "Se eu conduzir bem a coisa pode evoluir pra... {i}gulp{/i} algo muito... bacana..."

        "A gente vai tá os dois na casa dela, de boassa... daí o papo sério termina, a gente pede alguma coisa pra comer, bebe um pouco..."

        "Perfeito!"

    w "Tudo bem pra você?"

    mc envergonhado "Se você não liga, pra mim tá perfeito."

    w "Então vai pegar suas coisas que eu vou passar o que fazer pro [ron]. Me encontra lá na entrada."

    mc desconfiado "E a revista vai ficar bem com ele?"

    w "O [ron] é confiável. Você sabe. Ele tem feito um excelente trabalho."

    "Contando com o fato que ele tá transando com a Cássia... sei não..."

    mc normal "Então tá. Te encontro em cinco."

    scene black with dissolve

    "..."

    scene onibus parado with Dissolve(1.0)

    pause

    mc "E aí, senhor? Tudo bem hoje?"

    "Motorista" "Tudo em ci- epa epa. Quem é essa? Tá acompanhado hoje, jovem?"

    mc "Ela é uma am-"

    w "Colega de trabalho. Estamos indo trabalhar."

    "Motorista" "Vish... desse mato não sai coelho, meu amigo."

    mc "É o que parece, senhor..."

    if sofia_namorar:

        mc "Mas tamo aí na luta, né?"

        "Motorista" "Isso mesmo, jovem. Aproveite a vida enquanto é jovem. Com moderação, claro."

        mc "Opa. Pode deixar."

    w "Posso saber o que tá acontecendo aqui?"

    mc "Nada não."

    scene black with dissolve

    "..."

    scene so5_casa with Dissolve(1.0)

    pause

    mc normal "Então é aqui que você mora."

    w "É um lugar pequeno, mas como eu quase não passo tempo aqui, tá de bom tamanho."

    "Eu tô mesmo na casa da [w]... nem acredito, mano... casa da [w]? Espera..."

    "Calma lá! Se a [w] é filha do chefe e a [w] mora aqui então!"

    mc angustiado "!!!"

    w "Que foi? Não gostou?"

    mc preocupado "S-sofia... e-essa é a casa do chefe?"

    w "Do meu pai?"

    mc "S-sim..."

    w "Claro que não, [mc]."

    mc desconfiado "Não?"

    scene so5_img12 with Dissolve(1.0)

    pause

    w "Meu pai tem a casa dele, que é lá na ilha mesmo. Pelo que eu conheço do velho, ele não sai daquela cobertura de jeito nenhum."

    mc charmoso "Então o chefe é cheio da bufunfa assim?"

    w "Já são muitos anos como editor chefe da revista, né? Se esse cargo não pagasse bem também, não sei o que seria da gente."

    mc envergonhado "Verdade."

    mc desconfiado "Nossa... mas ele não deixou você morar com ele? Não ia ser melhor pra você?"

    w "Ah, [mc]... nós nem falamos sobre isso pra ser sincera. Eu nem perguntei pra ele."

    w "Eu sei que ele gosta da vida dele. Eu não queria incomodar. Além de que eu também não quero viver às custas dele."

    w "Só faltava isso pro pessoal me chamar mais ainda de 'filhinha do papai' na redação."

    mc normal "Você é muito foda, [w]. Nem todo mundo ia pegar busão todo dia tendo um pai cheio da grana morando do lado do trabalho."

    w "Isso não é nada... você também mora sozinho, né? Não é tão diferente."

    mc envergonhado "É. Mas minha mãe que conseguiu o trabalho pra mim."

    w "Não sabia. Como foi isso?"

    mc desconfiado "Pensando agora, eu não sei exatamente... mas provavelmente minha mãe conhece seu pai. Quase certeza que foi com ele que ela falou."

    w "Isso é interessante, né? Meu pai não é do tipo que faz favor pras pessoas."

    mc "Agora que você falou, ele com certeza não tem cara mesmo. Como minha mãe conseguiu isso?"

    w "Você devia perguntar pra ela um dia. Até eu fiquei interessada agora."

    mc envergonhado "Faz tempo que a gente não se fala, mas quando pintar a oportunidade vou perguntar, sim."

    w "Eu vou tirar essa calça jeans que tá apertando e já volto, tá? Fica à vontade. A geladeira é ali. Pode pegar uma água. Tem suco também."

    mc normal "Valeu."

    w "Já venho."

    scene so5_casa with Dissolve(1.0)

    "Esse papo sobre minha mãe e o chefe ficou na minha cabeça agora. Que merda isso quer dizer?"

    "Foda-se isso agora. Eu tô aqui com a [w]. Eu preciso aproveitar essa chance rara de falar com ela fora do trabalho."

    if sofia_namorar:

        "Eu decidi que eu quero algo mais com ela e não vai ter uma chance melhor do que essa."

    if venda_revista >= 2:

        "Eu já tentei convencer eles de vender a revista pelo menos duas vezes, isso com certeza vai ajudar a [j] a vender a revista."

        "Se eu quiser continuar por esse caminho, hoje é minha chance de fazer a cabeça da [w] e ganhar pontos com a [j] e a Faux."

        "Mas com certeza ficar do lado dela vai acabar com minhas chances de ficar com a [w]."

        "Tenho que pensar bem no que eu vou fazer."

    "Essa conversa com ela agora vai ser muito importante."

    w "Voltei. Desculpa fazer você esperar."

    mc surpreso "F-foi rápido! T-tudo bem."

    scene so5_img13 with Dissolve(1.0)

    pause

    w "Que foi? Por que essa cara? Fica à vontade, [mc]. Senta aí."

    menu:
        "Você parece bem à vontade.":


            mc envergonhado "Opa, vou sentar. Mas é você que parece bem à vontade, hein?"

            w "Que foi? Tô em casa e aquela calça aperta demais. Você fica desconfortável?"

            mc surpreso "C-claro que não."

            "Será que a [w] não sente nada por ficar assim na minha frente? Será que ela só me vê igual um amigo gay?"
        "Não é nada. Deixa eu sentar.":


            $ sofia_amizade += 1

            mc envergonhado "N-nada não. Só vou sentar aqui."

            w "Você com certeza deu um gritinho quando eu sentei."

            mc zerado "Já falei que não é nada, xiu."

            w "Ok..."

    mc envergonhado "Bom..."

    mc envergonhado "Só tava pensando aqui em como as coisas mudaram entre a gente, sabe?"

    w "Mudou? Como assim?"

    mc "Quando você chegou na redação, nos primeiros dias, você só me cortava na cara dura."

    mc "Ai de mim se eu chamasse você pra tomar um café... já ia tomar uma na fuça."

    mc normal "Agora você parece bem mais à vontade comigo."

    w "Agora que você falou isso, talvez eu tenha ficado mais tranquila quando aos homens mesmo."

    mc desconfiado "Como assim?"

    w "No começo eu sentia muito medo de dar qualquer brexa e algum engraçadinho já ver com outros olhos."

    w "A maioria dos homens é ansiosa demais. Qualquer coisa é motivo pra eles acharem que a mulher tá dando em cima."

    w "Isso é super cansativo, sabe? Então acho que eu só não queria que acontecesse isso. Ainda mais no trabalho."

    mc desculpa "Entendi... acho que a gente pode ser um pouco assim mesmo."

    scene so5_img14 with Dissolve(1.0)

    pause

    w "Mas você foi bem diferente comigo, [mc]. Por isso que eu acho que eu me sinto melhor."

    mc desconfiado "Sério? Eu? O que eu fiz?"

    w "Aquele dia no bar você foi um verdadeiro cavalheiro comigo. Acho que aquilo mudou tudo pra mim."

    mc "Hmm..."

    w "Aquele dia eu tava tão cansada, tava chateada com o negócio da venda da revista... minha cabeça parecia que ia explodir."

    mc envergonhado "Sua cara quando eu te vi lá na recepção tava horrível mesmo."

    w "Você foi super legal de me chamar pra tomar alguma coisa. E eu tinha certeza que você ia se aproveitar que eu tava daquele jeito, sabe?"

    mc "Sei..."

    if sofia_e4 == "sucesso":

        w "Não sei até agora direito o que aconteceu depois que eu bebi aquela bebida. Eu tenho só umas imagens aqui e ali."

        w "Uma delas eu lembro quando você tava me carregando..."

        mc envergonhado "Haha... aquela foi boa mesmo..."

        w "E eu tenho certeza que naquele momento você podia ter feito o que você queria comigo. Mas você foi um homem de verdade."

        w "Você me colocou no carro e acertou tudo com o motorista. Daí quando eu cheguei aqui eu já tava melhor e dormi até o outro dia."
    else:


        w "Eu não tive coragem de tomar aquela bebida lá no bar, mas isso não muda como eu me senti segura com você lá."

        "Verdade... eu não passei segurança suficiente pra ela beber..."

    w "Naquela noite eu percebi que você era um cara que tinha valores. Que você colocava o respeito acima do que você queria."

    w "Eu tava super abalada... qualquer 'homem de verdade', como eles se acham, teriam se aproveitado de mim."

    w "E eu ainda não acredito como eu deixei as coisas chegarem naquele ponto, sabe?"

    w "Eu devia ter pensado em tudo isso... mas eu tava tão cansada... tão... frustrada eu acho... que talvez eu tivesse procurando algo assim."

    mc desculpa "[w]..."

    w "E mesmo assim você cuidou de mim, [mc]."

    if sofia_beijo:

        scene so5_img15 with Dissolve(1.0)

        pause

        w "Inclusive... eu até perdoei você por aquele b-beijo roubado na Faux."

        w "Eu fiquei muito confusa naquele dia. Parecia que você tivesse tirando vantagem da minha confusão pelo que a [j] tinha me falado."

        w "Como se eu tivesse perdido a pessoa que eu mais confiava... Aquilo mexeu comigo..."

        mc "Não era isso que eu queria... eu queria que você entendesse o que eu sentia por você."

        w "E depois de como você me tratou no bar eu reavaliei aquilo tudo. Você nunca faria isso comigo."

    w "Minha conclusão é que você é um cara legal e eu posso confiar em você. Que você não vai me prejudicar se eu me abrir com você."

    w "Aliás, nem acredito que eu tô falando tudo isso. Que vergonha..."

    menu:
        "Pode falar tudo pra mim.":


            $ sofia_amizade += 1

            mc normal "Você sabe que pode falar tudo pra mim, né?"

            w "Acho que eu posso mesmo... esse é todo o ponto que eu tô tentando fazer aqui."

            mc "Então não tem porque ficar envergonhada."

            w "Eu sei... mas eu fico, fazer o quê."

            mc "Haha..."
        "Você fica fofa envergonhada.":


            mc charmoso "Você fica fofa envergonhada."

            w "Afe, como assim?"

            mc "Normalmente você é tão séria e fechadona. Quando você fica vulnerável assim é bonitinha."

            w "E você sabe que falar essas coisas não ajuda em nada, né?"

    if praia_sofia_local:

        w "Se bem que depois daquele nosso dia na praia, não tem muito mais o que eu esconder de você, né?"

        w "Aquele biquíni... meu Deus do céu..."

        mc charmoso "Foi um bom dia."

        w "Foi, né? Sei..."

    scene so5_img17 with Dissolve(1.0)

    pause

    mc "Olha... Não tem por que você ficar tão agradecida. Eu só fiz o que eu achei que eu tinha que fazer."

    mc "Eu também tenho as coisas que eu faço de errado. Eu sou um cara bem estragado também, sabe?"

    mc "Aliás, eu tô muito longe de ser tão, sei lá, ético igual você. Você deve ser a pessoa mais 'certinha' que eu já vi."

    mc "O mundo é estragado demais pra você, [w]. Ainda mais essa capital. Todo mundo aqui tem seus planos e não tão nem aí pros outros."

    w "Eu sou assim também."

    mc "Só que é diferente. Você faz o que você acha certo de verdade. A maioria de nós aqui faz coisa errada mesmo sabendo que tá errada."

    w "Eu não vejo você assim, [mc]..."

    mc "Mas pode acreditar. Eu já fiz muita cagada. E eu sei que eu ainda vou fazer muita cagada depois de hoje."

    mc "Mesmo assim eu não quero machucar ninguém. Eu queria ter uma vida bacana, mas sem que as pessoas sofressem. Não sei se dá."

    mc "É que às vezes as coisas acontecem e a gente não sabe como agir..."

    w "..."

    mc "Por isso que eu acho que é incrível as pessoas que fazem o certo. Igual você faz."

    w "Mas e se a [j] tiver certa? E se eu for uma controladora? E teve o que ela falou da outra vez, sobre o certo e o errado..."

    w "Não sei se é tão fácil assim..."

    menu:
        "A [j] só quer entrar na sua cabeça.":


            mc "Não pense demais nisso, [w]. A [j] quer entrar na sua cabeça pelos próprios motivos dela."

            w "Mas e se ele tiver razão? Eu sinto que o que ela fala pode ser verdade."

            mc "Se eu fosse você, não levava isso à sério. A [j] é manipuladora e não é nenhum modelo de certo e errado."

            w "Não sei..."
        "Isso é uma coisa que você tem que pensar.":


            $ sofia_amizade += 1

            mc "A gente sabe como a [j] é, né? Mas esse é o tipo de coisa que só você pode falar."

            w "Tem razão. Eu preciso pensar com calma e encontrar o que é a verdade pra mim."

            w "Obrigada, [mc]. Você sempre pensa de um jeito calmo."

    scene so5_img16 with Dissolve(1.0)

    pause

    w "Eu sinto que eu ainda tenho que descobrir muito sobre mim, sabe?"

    w "Por que eu quero tanto que a revista dê certo? Qual motivo de eu querer tanto isso?"

    w "A [j] pode ser uma víbora, mas ela é bem astuta e experiente. Só não vai falar isso pra ela."

    mc "Haha... pode deixar."

    w "Acho que, no fundo, eu tenho um pouco de inveja desse jeito dela."

    mc "Sério?"

    w "É. Ela tem essa força pra fazer o que ela quer fazer. Regras não são nada pra ela. Ela é a pessoa mais obstinada que eu conheço."

    w "Ela lembra um pouco meu pai. Ele sempre fez o que tinha que fazer pra revista continuar viva e atraindo leitores."

    menu:
        "Sim. A gente faz o que tem que fazer.":


            mc "É. Acho que você tem razão. Às vezes a gente tem que fazer coisas que parecem erradas, mas que são necessárias."

            w "Então você realmente pensa isso também..."

            mc "Cada um sabe sua verdade. E o que é certo pra um é errado pra outro."

            w "Hmm..."
        "Pra mim existe certo e errado.":


            $ sofia_amizade += 1

            mc desculpa "Eu não consigo concordar com isso assim. Pra mim existe o que é certo e o que é errado."

            mc "Não importa seu objetivo. Se você faz algo errado, é errado e pronto."

            mc "A [j] não pensa duas vezes antes de enganar as pessoas pra conseguir matérias. Seu pai também aceita tudo o que ela faz."

            w "É. É uma área bem controversa, pra falar o mínimo. Mas eu tento pensar assim também."

    w "Eu gosto que você sempre tem o que falar sobre as coisas, [mc]. Pessoas que têm opinião sobre as coisas são, sei lá, charmosas."

    "Opa! Esse comentário foi massa pra mim. A [w] me chamando de charmoso?"

    if sofia_namorar:

        "Era esse momento que eu tava esperando. A gente tá falando de coisas super pessoais."

        "Se eu não der o bote agora, a conversa pode mudar de rumo e eu vou perder a chance."

        "Força, [mc]. Fala pra ela que você quer uma coisa séria com ela!"
    else:


        "Talvez a [w] goste de mim... Não sei se é só como amigo, mas e se não for?"

        "Lá na Faux eu cheguei a conclusão que não queria nada com ela... mas será que eu ainda não quero?"

        call namorando from _call_namorando_1

        if namorando:

            "Eu já tô enrolado em um relacionamento sério, mas a [w] é uma garota e tanto. Será que eu aguento não ter nada com ela?"

        "O que eu faço?"

        menu:
            "Eu quero namorar a [w].":


                $ sofia_namorar = True

                "Pensando bem... a [w] é incrível demais pra eu deixar ela escapar assim."

                "Eu vou tentar namorar com ela."

                "Era esse momento que eu tava esperando. A gente tá falando de coisas super pessoais."

                "Se eu não der o bote agora, a conversa pode mudar de rumo e eu vou perder a chance."

                "Força, [mc]. Fala pra ela que você quer uma coisa séria com ela!"
            "A gente é só amigo mesmo.":


                "A gente é só amigo."

                "Não quero nada mais com ela. A [w] é bacana, mas eu não vejo ela assim."

    if sofia_namorar:

        scene so5_img18 with Dissolve(1.0)

        pause

        mc "[w]... já que você tá sendo sincera e aberta comigo hoje, eu queria fazer a mesma coisa."

        w "..."

        mc "Tem uma coisa que eu quero falar pra você. É muito importante pra mim."

        w "[mc]... E-eu não sei se-"

        mc "Calma. Me escuta."

        if sofia_beijo:

            mc "Lembra o que eu falei lá na Faux? Eu te vejo como uma parceira. Não só uma colega de trabalho, mas muito mais que isso."

        mc "Eu não quero ser só um colega de trabalho pra você. E nem só um amigo. Eu quero mais."

        mc "Eu olho pra você e só penso que eu queria mais do que só conversar. Eu quero poder te abraçar e te beijar e passar o dia todo aqui."

        w "!"

        mc "Já faz tempo que eu quero isso, [w]. E eu prometo que é sério. Não é só uma noitada. Eu quero ficar com você de verdade, como minha garota."

        w "..."

        w "Era pra gente tá falando sobre o que fazer com a revista... e a gente falou de tudo, menos isso."

        w "E agora você se declara pra mim assim. Na cara dura?"

        mc "É sério."

        w "Eu não sei o que responder sobre isso, [mc]..."

        scene so5_img19 with Dissolve(1.0)

        pause

        mc "Seja sincera comigo também. Só fala a verdade. Só isso que eu quero."

        mc "Não precisa ficar comigo se você não sente nada por mim. Mas, se você sentir, fala pra mim que você me quer também."

        w "[mc]..."

        "Esse é o momento da verdade. Tudo o que eu vivi com a [w] era pra esse momento."

        "O que ela vai responder? Meu coração tá quase saindo pela boca!"

        w "Olha, [mc]..."

        if sofia_amizade >= 31:

            w "Nunca pensei que fosse falar isso, mas se tivesse alguém com quem eu gostaria de ter algo assim, seria você, [mc]."

            "Sim! Não acredito! Eu sou o cara certo pra [w]!"

            mc "Isso quer dizer qu-"

            w "Mas eu não consigo me ver em um relacionamento com alguém."

            mc "C-como assim?"

            w "Eu sei que encontrar alguém especial é o desejo de muitas pessoas, só que nunca foi o meu."

            w "Você é um cara legal, foi super romântico comigo hoje, e merece uma garota que te dê isso que você tá buscando."

            w "E com certeza essa mulher não sou eu."

            mc "Por que você não seria? Eu escolhi você, [w]."

            w "M-mas, [mc]. Eu não quero pensar em jantares, passeios, beijo e muito menos sexo agora."

            w "Meu foco tá todo na revista, no meu trabalho. Você acha que é isso que você realmente quer numa relação?"

            mc "Sem beijinho? Sem encontros?"

            w "N-nada disso... pelo menos até eu resolver tudo isso que tá acontecendo na revista."

            "Que porra de namoro é esse?! Eu tô me matando pra catar ela depois de ver ela vestida assim e a gente não vai poder fazer NADA?!"

            w "[mc]... o que você quer fazer?"

            "Eu queria te jogar em cima dessa mesa agora..."

            "E agora? O que eu faço?"

            menu:
                "Eu quero você mesmo assim.":


                    $ sofia_namoro = True

                    mc "[w]... eu quero você mesmo assim."

                    scene so5_img20 with Dissolve(1.0)

                    pause

                    w "Verdade?!"

                    mc "Sim. Mesmo que eu tenha que esperar tudo isso se resolver pra ter uma relação 'normal', você é a mulher que eu escolhi."

                    mc "Eu vou ter paciência pra esperar você vir até mim. Eu quero que você aproveite nossa relação tanto quanto eu."

                    w "E-eu não esperava que você fosse aceitar. O q-que eu faço?"

                    mc "Talvez... você devesse ficar só quietinha um pouco e deixar eu te bei-"

                    scene so5_img20 with hpunch
                "Isso não é namoro pra mim.":


                    mc "Eu te entendo, [w]... mas isso não é namoro pra mim."

                    mc "Você tem razão. Você não é a mulher certa pra mim agora."

                    scene so5_img21 with Dissolve(1.0)

                    pause

                    w "Eu fico feliz, [mc]... eu não quero estragar sua vida sendo uma pessoa que você não precisa agora. Eu quero fazer o certo com você."

                    jump sofia5_amizade
        else:


            w "Você é um homem incrível. Eu falei muito bem de você hoje, você sabe."

            w "Mas eu não quero ter um romance agora. Nem de uma noite e nem um relacionamento sério."

            mc "..."

            w "C-com licença."

            scene so5_img21 with Dissolve(1.0)

            pause

            w "Eu tô concentrada completamente no trabalho, ainda mais com tudo isso que tá acontecendo..."

            w "Por isso, eu não quero que você fique me esperando. Eu não vou namorar com você. Nem hoje e nem mais pra frente."

            w "Talvez você não seja o cara certo pra mim... ou talvez eu só não consiga pensar nisso mesmo."

            w "Pode ser que se as coisas tivessem sido diferentes entre a gente... mas mesmo assim eu não sei..."

            label sofia5_amizade:

                $ sofia_e5 = "amizade"

            mc "Tudo bem... era só isso que eu queria saber. Se você não sente essa vontade, não tem o que a gente possa fazer."

            w "Desculpa..."

            mc "Tomar um fora nunca é bom... mas eu vou sobreviver. Não precisa pedir desculpas por isso aí."

            w "Mas eu queria continuar sendo sua amiga. Não só na revista, mas igual hoje, assim... Não sei se você vai querer..."

            mc "Agora é um pouco cedo pra gente falar sobre isso, minha bunda ainda tá doendo..."

            mc "Mas eu vou tá normal na redação. Que é o que mais importa pra gente."

            w "Tá..."

            mc "Daqui uns dias já vai tá tudo normal."

            w "Ok..."

            mc "A gente acabou não falando nada do que tinha que falar, mas eu vou indo nessa."

            w "Tá. A gente conversa melhor outro dia."
    else:


        scene so5_img22 with Dissolve(1.0)

        pause

        mc "A gente acabou não falando nada do que tinha que falar até agora."

        w "Verdade."

        w "Essa tentativa de golpe da Faux usando a [j] como espiã infiltrada é golpe baixo demais. Isso já mostra que não são flor que se cheire."

        menu:
            "Realmente, não dá pra aceitar isso.":


                $ sofia_amizade += 3

                mc "Sem dúvida. Os caras são completamente antiéticos."

                w "Você concorda, né?"

                mc "Claro. Eu tô nessa com você. A gente não pode deixar eles engambelarem a gente."

                w "Eu gosto que você também sempre tá atento, [mc]. Isso é importante pra um jornalista."
            "Mas, na prática, é ruim pra revista?":


                $ venda_revista += 1

                mc "Mas, pensa comigo, deixando de lado essa questão política, na prática do dia a dia da redação, não seria melhor?"

                w "Por que seria melhor?"

                mc "Mais dinheiro, ter a ajuda de todos os veículos dele, mais pessoal, uma estrutura muito melhor pra trabalhar."

                w "É duro admitir, mas por esse lado talvez fosse melhor. A qualidade técnica da revista provavelmente melhoraria."

                mc "Eu acho que a gente tem que levar isso em consideração também."

                w "É... talvez..."

        w "Agora o que a gente precisa fazer é- {nw}"

        scene so5_img22 with hpunch

    "{i}trr trr{/i}"

    w "O interfone?!"

    mc "Quem será que é?"

    "{i}trr trr{/i}"

    w "Vou atender. Só um segundo."

    scene black with dissolve

    scene so5_casa with Dissolve(1.0)

    w "Alô? {w}Pai? {w} O que você tá fazendo aqui?"

    mc desconfiado "Pai?"

    mc angustiado "P-p-pai?! O chefe?!"

    w "O que o senhor tá fazendo aqui?"

    w "..."

    w "Preocupado? Eu nunca saio do trabalho antes da hora?"

    w "Desde quando o senhor se preocupa se eu tô bem?"

    w "..."

    w "Desnaturada?"

    mc angustiado "S-sofia?!"

    w "Ele disse que quer subir pra ver se eu tô bem."

    mc "[w] se ele me ver aqui eu tô fodido!"

    w "Claro que não, [mc]. Somos dois adultos. Qual o prob-"

    mc "Você tá louca?! Ele vai me pendurar pelo pé como exemplo no meio da redação!"

    w "Para de ser bobo."



    if sofia_namoro:

        w "Além de que..."

        mc "Hm?"

        scene black with dissolve

        scene sofia5_new1 with Dissolve(1.0)

        pause

        w "Se você for agora... a gente não vai comemorar... as novidades..."

        mc "T-tá falando sério? Foi você quem disse que não tinha cabeça pr-"

        w "[mc]... a gente pode conversar... mas você não prefere usar esse tempinho comigo de outro jeito?"

        "Claro que eu quero! Mas e o velho?!"

        "Pelo que eu entendi, essa vai ser minha única chance de ter alguma coisa com ela até tudo tá resolvido na redação."

        "É agora ou nunca."

        "Só que se o chefe me pega aqui... com certeza é o fim da minha carreira na revista! Ou seja! O que eu faço?!"

        w "Pera aí..."

        mc "Hm?"

        scene black with dissolve

        scene so5_casa with Dissolve(1.0)

        w "Pai... eu vou me arrumar aqui. Me dá uns 10 minutos e toca aqui de novo."

        w "..."

        w "Não! Não vou esconder nenhuma droga! Eu não uso nada disso, pai! Só me dá um tempo!"

        scene black with dissolve

        scene sofia5_new2 with Dissolve(1.0)

        w "Pronto... agora a gente tem uns minutos..."

        mc "[w]..."

        w "Faz tanto que eu não vivo um negócio assim, [mc]... meu coração tá quase parando."

        w "A última vez que eu tive com alguém, eu ainda nem tinha ido pro exterior estudar."

        w "Minha vontade era só sair correndo... mas depois de como você me tratou hoje... eu quero muito ficar com você."

        mc "Eu também quero... mas assim? A gente só tem alguns minutos!"

        w "Não é perfeito... eu sei... mas assim que você sair por essa porta, eu sinto que tudo vai voltar a ser igual sempre."

        w "Eu vou voltar a só pensar no trabalho. Eu só quero aproveitar o que eu tô sentindo agora."

        "Se ela soubesse o quanto eu quero ela também! Mas eu também quero meu emprego! O que eu faço?!"

        label so5_premium2:

            "Eu fico com ela agora e corro o risco de ser demitido, ou espero a gente resolver tudo?"

        menu:
            "Não posso arriscar tudo assim! Tchau!":


                mc "Desculpa, [w], mas a gente vai ter tempo pra isso no futuro!"

                w "Tudo bem... eu vou te esperar... se você me esperar também..."
            "Eu vou ficar com ela, mesmo que eu acabe na rua":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_31

                    jump so5_premium2

                mc "Eu não vou perder essa chance por causa do seu pai, [w]."

                w "Ah... que bom..."

                mc "Você sabe o quanto eu quero você. E se você tá afim, vamos aproveitar bem esses minutinhos que a gente ganhou."

                w "Vem, [mc]..."

                scene black with dissolve

                scene sofia5_premium17 with Dissolve(1.0)

                pause

                w "Hmm..."

                mc "Você não faz ideia de quanto eu esperei pra sentir você assim."

                w "Seu beijo é melhor do que eu pensei."

                mc "Que bom. Porque eu vou continuar te beijando."

                w "Ah... é gostoso de verdade..."

                "A [w] parece que tá gostando mesmo de ficar comigo. Que legal..."

                "Imagina se depois de tudo isso a gente não tivesse química?"

                w "Eu quero que você continue me beijando."

                mc "Não precisa pedir, linda. Eu tô aqui pra você."

                "Ela fala assim, mas ela tá toda desajeitada... ela nem encosta em mim..."

                w "Ahn... eu tô sentindo sua mão aqui atrás."

                mc "A gente tem pouco tempo. Eu quero aproveitar você ao máximo."

                mc "M-mas se isso for demais... eu posso parar."

                w "N-não... pode continuar... eu tô gostando... hmm..."

                "Eu não achei que ela ia concordar assim."

                w "Eu tô achando muito bom, [mc]. Quero sentir mais você."

                mc "Hm? Ok..."

                scene sofia5_premium18 with Dissolve(1.0)

                pause

                mc "U-uau..."

                "A [w] realmente tá curtindo."

                "A gente tá se beijando tão forte agora. Ela tá me abraçando e tudo."

                w "Ah... hmm..."

                "As coisas tão esquentando mais que eu pensei."

                w "Assim... você tá fazendo eu me sentir tão bem. Deixa eu sentir mais sua língua."

                mc "Claro, amor."

                w "Isso... brinca com a minha... hmm... me aperta mais."

                mc "O que você quiser."

                w "Ai... que gostoso, [mc]. A gent devia ter feito isso antes."

                mc "Eu sempre quis pegar você. Você que fugia de mim."

                w "Eu fui uma idiota... quantas chances eu perdi de sentir você gostoso assim."

                "A Sofia realmente tá entrando no clima. Se as coisas continuarem assim..."

                w "Que delícia... pega em mim, vai..."

                w "Ai... eu nem sei mais o que eu tô falando... eu só quero te beijar."

                mc "[w]..."

                w "Ah... me beija mais, [mc]... beija gostoso... eu adoro..."

                mc "Você quer assim, quer?"

                w "Quero! Quero mais! Eu preci-"

                scene sofia5_premium19 with hpunch

                pause

                w "C-calma!"

                mc "Que foi? Aconteceu alguma coisa?"

                w "T-tá ficando intenso demais, [mc]... e-eu sinto minha cabeça apagando a cada beijo seu..."

                mc "E isso não é bom?"

                w "É... mas... se as coisas continuarem assim... eu não sei se eu vou conseguir parar..."

                mc "Eu também não sei. E essa é a melhor parte."

                w "N-não... é perigoso... acho que foi comemoração demais pra um dia."

                w "E tem meu pai também, né?"

                w "A gente... a gente vai ter tempo, certo?"

                "Ela fala isso, mas eu sinto ela se esfregando em mim aqui embaixo... a [w] tá que tá..."

                "Mas ela tá pedindo... e tme o chefe... mas eu nunca vi ela assim antes."

                "A gente ter começado a namorar deve ter mexido com ela de verdade. Vai saber quando eu vou ter outra oportunidade dessas."

                "Eu vou com calma e respeito ela ou eu dou uma forçada e vejo a reação como vai ser?"

                menu:
                    "Você tá certa. Deixa eu picar a mula!":


                        mc "Tem razão! A gente vai ter tempo!"

                        w "S-sério? Você vai mesmo?"

                        mc "Claro. Você entendeu que o chefe tá chegando aí, né?"

                        w "M-mas... agora que a gente-"
                    "Eu sei que você quer mais. Seja sincera.":


                        mc "Você tá com medo, mas eu tô vendo na sua cara que você quer mais."

                        w "Ai... claro que eu quero... sua língua é boa demais, [mc]."

                        mc "Então para de falar e me beija."

                        w "Ai... se você quer... então por você... e-eu faço..."

                        scene black with dissolve

                        scene sofia5_premium20 with Dissolve(1.0)

                        pause

                        w "Ah... que bom que você não foi..."

                        mc "Que bom, né?"

                        w "Hmm... eu preciso da sua língua esfregando na minha. Quero dizer, eu vou fazer o que você pedir."

                        mc "Eu quero que você continue se esfregando em mim desse jeito."

                        w "Aah... tá bom... então me pega no colo... deixa eu chegar mais perto..."

                        w "Depois que você decidiu ficar comigo, [mc], hoje eu faço o que você quiser."

                        mc "Só hoje?"

                        w "Só. Amanhã é dia de trabalhar. A gente não pode ficar se esfregando... hmm... todo dia assim..."

                        mc "Certeza?"

                        w "Ai... não me provoca... imagina todo dia você me pegando assim? Ah..."

                        scene sofia5_premium21 with Dissolve(1.0)

                        pause

                        mc "O-opa!"

                        w "Cola mais em mim! Nngh... Pra você aproveitar mais."

                        mc "Com certeza."

                        w "E não para de chupar minha língua... eu fico... aahn... sem ar quando você faz assim..."

                        mc "Você gosta?"

                        w "Adoro... adoro quando eu fico zonza... m-mas eu só quero que você se sinta bem comigo."

                        w "Eu não sou o tipo de mulher que fica doida por qualquer coisa safada."

                        mc "Eu sei."

                        w "Que bom. Eu só quero que você aproveite o máximo hoje, pra você não esquecer."

                        "Ela tá se esfregando tanto que a roupa dela tá saindo toda."

                        w "Ai... isso... lambe minha boca... eu adoro na boca e no pescoço. É minha fraqueza."

                        mc "Bom saber..."

                        w "Ai! Você vai me obrigar a gemer assim logo no nosso primeiro beijo."

                        mc "Pode gemer, gostosa."

                        w "Não... ahn... é safado demais, [mc]... ain..."

                        w "Imagina se alguém na redação me visse assim? Nnghh! Que vergonha!"

                        mc "Tamo só nós aqui. Não tem problema nenhum."

                        w "Tem razão... ah... e e-eu já tô quase sem roupa... Mnmm... Tira o resto?"

                        mc "C-com certeza."

                        scene black with dissolve

                        scene sofia5_premium22 with Dissolve(1.0)

                        pause

                        w "Isso... agora eu sinto você muito melhor, [mc]! Nnnghh!"

                        mc "Eu nunca imaginei que você fosse fogoza desse jeito, hein?"

                        w "Não fala assim... aah... é... culpa sua... você que... nnghh me forçou..."

                        mc "Tem razão. Mas não tem nenhum problema. Eu tô amando te beijar assim."

                        w "Eu também! Mmnnh! Não consigo parar de me esfregar em você! Eu preciso de mais!"

                        mc "[w]... mais que isso a gente vai acabar transando..."

                        w "Nãoo... t-transar é demais... e se meu pai sobe?"

                        menu:
                            "Tem razão. A gente não tem mais tempo.":


                                mc "T-tá certa! Só de pensar no velho eu tenho um treco!"

                                w "S-sério? Você vai mesmo?"

                                mc "Claro. Você entendeu que o chefe tá chegando aí, né?"

                                w "M-mas... agora que a gente-"
                            "A gente vai dar uma rapidinha.":


                                mc "Dá tempo de uma rapidinha gostosa! Você não vai me recusar, né?"

                                w "Ahn! S-se você tá me obrigando... nngh... então tira sua calça."

                                mc "T-tô tirando."

                                scene sofia5_premium23 with Dissolve(1.0)

                                pause

                                w "Ai! Assim! Só não para de me beijar!"

                                mc "Uhum!"

                                w "Isso, [mc]! É bom demais! Aaii!"

                                "A Sofia nem sabe mais o que tá rolando aqui. Eu só tenho que garantir que ela vai gozar agora."

                                "Quem ia imaginar que ela curtia tanto uma safadeza?"

                                w "Eu preciso de mais! Mmnn! Sentir mais você em mim!"

                                mc "Você tá perto, é?!"

                                w "Tô! Vai!!!"

                                scene sofia5_premium24 with hpunch

                                pause

                                w "Ai! Isso!"

                                mc "Pode gozar! Goza com meu pau roçando na sua buceta!"

                                w "Aiin! Você vai fazer eu gozar! Assim mesmo! Nnnnghhh!"

                                w "Nnghhh!"

                                mc "Goza logo, sua safada!"

                                w "Mmmgghh! Eu não sou! Aiinn!"

                                mc "Vai logo!"

                                w "Tira minha calcinha! Eu quero sentir mais! Vai! Por favor!"

                                scene sofia5_premium26 with vpunch

                                pause

                                w "Agora sim! Seu pau tá esfregando em mim! Aaahh!"

                                "{i}TRRRR TRRR{/i}"

                                mc "Não! É o seu pai!"

                                w "Não! Aiin! Ignora ele! Não para agora!"

                                mc "Goza logo, Sofia! Se ele subir eu tô morto!"

                                w "Eu preciso de mais! Deixa eu olhar seu pau!"

                                "{i}TRRRR TRRR{/i}"

                                mc "Q-quê?!"

                                w "Eu preciso ver ele! Vaiinn!"

                                scene sofia5_premium27 with vpunch

                                pause

                                w "Que delícia! Tanto tempo que eu não via um pau!"

                                mc "O interfone parou..."

                                w "Ai! Tanto tempo que eu não sentia prazer assim! Nnngh! Tudo você, [mc]! Meu homem!"

                                mc "Você também é uma delícia, mas a gente não tem mais tempo. E se ele tá subindo?!"

                                mc "Eu quero que seja inesquecível pra você, então goza de uma vez pra você nunca mais esquecer."

                                w "Naaumm! Eu queria sentir muito mais!"

                                mc "É perigoso, Sofia!"

                                w "T-tá! Me beija então! Faz eu gozar com sua língua! Eu preciso da sua língua na minha boca!"

                                mc "Vem aqui!"

                                scene sofia5_premium25 with hpunch

                                pause

                                w "Nnnnbggh! Aahhhn!"

                                "Ela tá tremendo! Ela tá quase lá! Vai ser a maior gozada da vida dela!"

                                scene sofia5_premium25 with hpunch

                                "{i}TOC TOC TOC{/i}"

                                "Chefe" "Filha! Você tá bem!?"

                                w "Ai! Agora nauumm!"

                                mc "!!!!!"

                                mc "Sofia, sai de cima!"

                                w "Naumm! Se a gente parar agora eu nunca vou te perdoar!"

                                mc "Você quer que eu morra?!"

                                w "Eu vou gozar! Eu preciso! Só isso que interessa!"

                                mc "Sofia! Por favor!"

                                w "Eu preciso! NNNGHHH!!!"

                                "{i}TOC TOC TOC{/i}"

                                "Chefe" "Filha! Eu vou entrar!"

                                w "ESPERAA!!!"

                                w "Vai! Mais um pouco!"

                                menu:
                                    "Continuar roçando nela":


                                        $ renpy.block_rollback()

                                        mc "Eu nunca vou decepcionar você, amor!"

                                        w "ISSO!!!"

                                        w "VAIII!!!! AAAHHHH!!!!"

                                        scene sofia5_premium28 with hpunch

                                        w "AAAANNNNGHHHHHHHHHHHHHHH!!!!"

                                        "{i}BLANGGGH{/i}"



                                        "Chefe" "Filha, o que aconteceu?! Você tá bem?!"

                                        "Chefe" "QUÊÊÊÊÊ???!!!"

                                        mc "Chefe! Eu posso explicar!"

                                        w "Aaahhh! Aaaah!"

                                        "Chefe" "O que vocês!? Vocês querem MORRER?!!!"

                                        mc "Não era pra você subir!"

                                        "Chefe" "CALA A BOCA, MALDITO! CORROMPENDO MINHA FILHA!"

                                        w "Aah...."

                                        "Chefe" "N-não é possível! Meu coração!"

                                        mc "Chefe! Você tá bem?!"

                                        "Chefe" "Agh! Uma dor forte!"

                                        scene so5_casa with vpunch

                                        mc "Sofia! Seu pai!"

                                        w "P-pai?! Você tá aí?!"

                                        "Chefe" "Que pai o quê?!"

                                        "Chefe" "Vocês d-dois! D-deserdados!"

                                        mc "O senhor tá tendo um ataque! Não sabe o que tá falando!"

                                        w "PAAIIII!!!"

                                        scene black with Dissolve(3.0)

                                        scene cidade noite with Dissolve(1.0)

                                        "Aquilo foi demais pro chefe..."

                                        "Ele realmente me despediu... claro... depois do que ele viu..."

                                        "Eu pensei que ele fosse ter um ataque, mas o coração do velho era mais forte do que eu imaginava."

                                        "Ele deserdou a Sofia, tirou ela da redação e eu também... eu nunca mais vi ela."

                                        "Eu não tenho outra forma de ganhar dinheiro suficiente pra pagar condomínio, luz, comida etc."

                                        "Vou ter que voltar para a casa dos meus pais..."

                                        "Justo agora que eu comecei a conhecer pessoas tão interessantes na capital..."

                                        "Adeus capital! Adeus minhas queridas cebridades! Adeus chance de ter minha própria vida!"

                                        "{i}Final X{/i}"

                                        scene black with Dissolve(3.0)

                                        show pixie impaciente with dissolve

                                        p "Vou te falar... até eu fiquei surpresa com essa..."

                                        $ renpy.full_restart()
                                    "Jogar a Sofia no chão e se esconder":


                                        $ renpy.block_rollback()

                                        mc "Desculpa, Sofia! Mas eu não posso!"

                                        scene so5_casa with vpunch

                                        w "AII! Você me soltou!"

                                        "Espero que ele não me veja aqui!"

                                        "{i}BLANGGGH{/i}"



                                        "Chefe" "Filha, o que aconteceu?! Você tá bem?!"

                                        "Chefe" "QUÊÊÊÊÊ???!!!"

                                        mc "!!!"

                                        "Chefe" "O que você tá fazendo nua no chão, garota?!"

                                        "Chefe" "Pelo amor de Deus! Vai se trocar logo! É por isso que eu não venho te visitar! Jovens!"

                                        w "M-me espera lá no térreo! Quem mandou o senhor subir!?"

                                        "Chefe" "Cada uma..."

                                        w "[mc]..."

    label sofia5_depois_premium:

        pass

    mc "Falous! Tô descendo pela escada! E você não fala que eu tava aqui! Por favor!"

    w "[mc]! Espera seu -- {nw}"

    scene black with hpunch

    mc angustiado "Cristinho de todos os céus!"

    scene black with dissolve

    "..."

    scene mc onibus_noite with Dissolve(2.0)

    pause

    "Acho que eu escapei..."

    "O cara apareceu pra ver a filha só porque ela saiu do trabalho um pouco antes do normal. Imagina se esse velho me pega lá?"

    "Ele ia começar a pedir uma pauta por dia. Isso se ele não me demitisse no ato."

    if sofia_namoro:

        "Mas eu consegui falar pra [w] que eu quero namorar ela... e ela aceitou."

        "Então a gente tá namorando..."

        if premium:

            "E que loucura foi aquela que aconteceu no apê?!"

            "Nunca imaginei que a Sofia ia perder a cabeça daquele jeito... parecia outra pessoa completamente!"

            "Será que é verdade que o povo fala? Quanto mais a pessoa foge... é porque mais medo tem de gostar?"

            "Bom... acho que a gente não vai ter problemas na cama hehe..."

            "O duro... é quando vai ser isso?"
        else:


            "Ou não?"

            "Tamo, sim. Eu disse que queria ficar com ela e respeitar o tempo dela."

            "Mas a gente nem se beijou ainda."

            "Quando que eu vou ter outra chance de passar um tempo sozinho com ela de novo agora?!"

        "Ela só vai aceitar realmente sair comigo quando a gente resolver o lance da compra da Faux! Quando vai ser isso?!"

        "Melhor eu parar de pensar nisso ou eu vou acabar chorando aqui."

    elif sofia_e5 == "amizade":

        "Mesmo eu querendo algo mais com a [w] a gente acabou ficando na amizade."

        "Ela realmente não queria namorar agora. E eu também não quero ficar com uma garota que não tá nem aí pra isso."

        "Tem tantas garotas lindas e gostosas nessa cidade. Seria um desperdício me amarrar com alguém que nem quer beijar."

        "Quero ver o que vai rolar com o resto do pessoal. Essa cidade tá cheia de possibilidades pra mim."
    else:


        "Não consegui falar muito sobre a venda da revista com ela."

        if venda_revista >= 2:

            "Se eu convencer a [w] a vender a revista, ela pode fazer a cabeça do velho e eu ganho pontos com a [j] e o grupo dela."

            "Isso não seria nada ruim."

            "Eu tenho que pensar no meu crescimento nesta ilha. Não quero ser pobre e fraco pra sempre."

            "Eu ainda vou chegar no topo."
        else:


            "Acho que o melhor é a gente não vender mesmo."

            "Mesmo perdendo pontos com a [j] e o grupo dela, eu vou ficar do lado da [w] e do pessoal que quer acabar com essa máfia."

            "Parece um caminho mais perigoso, mas mais promissor também."

    "Seja como for, eu tô ansioso pro que vai vir no futuro."

    "Eu só preciso me manter ligado. Ainda vem muita coisa por aí!"







    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v47_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v47_fim","final","local")

    scene black with Dissolve(3.0)

    call checa_final from _call_checa_final_6

    jump call_cidade

label sofia_18_1:

    $ estou_na_cidade = False
    $ sofia_premium = 1



    scene black with Dissolve(1.0)

    pause 1.0

    scene trabalho angulo with Dissolve(1.0)

    w "O horário já terminou e eu sou a última a sair outra vez..."

    "Estranho... eu não vi meu pai saindo. Normalmente ele sai antes de terminar o expediente."

    "Aquela idiota da [j] também... eu não vi ela saindo."

    "Não é que eu sou xereta... Eu tenho que ficar de olho em tudo aqui ou ninguém faz o trabalho direito..."

    "Se ele tá aqui mesmo, bem que ele podia me dar uma carona."

    scene black with dissolve

    scene trabalho chefe_porta with Dissolve(1.0)

    "???" "Huhuhu..."

    w "Hm?"

    "Tem gente na sala dele. E é uma mulher. Só falta ser a cadela..."

    "Não é possível que depois da [re] ela pega meu pai também! Até meu pai, [j]?!"

    menu:
        "Tenho que confirmar o que tá acontecendo":


            "Não tem problema se é por um motivo justo..."

            scene black with dissolve

            scene sofia5_new3 with Dissolve(1.0)

            pause

            w "HUH?!"

            "Não acredito! É exatamente o que eu pensei! Que decepção, pai! Que decepção!"

            j "Eu vejo que a idade não acabou com seu charme, velho..."



            "Chefe" "..."

            j "O que foi? Você não gosta mais de pegar em mim?"

            "Chefe" "[j]... vá trabalhar, ok? A [w] tem enchido muito meu saco dizendo que eu mimo você demais."

            j "A bonequinha só tá com ciúmes. Eu imagino a situação fodida que vocês dois têm."

            "Chefe" "Não é do seu interesse. O que você quer?"

            "Parece que meu pai tem tudo sob controle. Foi bom eu ter alertado ele sobre os abusos da Cássia."

            "Ou será que é melhor eu me certificar? Eu não quero ver a Cássia pelada... mas talvez seja por uma boa causa."

            menu:
                "Eu não preciso. Ele vai fazer o certo.":


                    "Quem quer ver a Cássia sem roupa? Deixa o pai resolver essa aí."

                    jump so5_final_premium
                "É melhor eu ficar e confirmar...":


                    "Infelizmente eu vou ter que ver ela pelada, mas... é melhor que deixar ela montar no meu pai."

            j "Olha aqui..."

            scene black with dissolve

            scene sofia5_new4 with Dissolve(1.0)

            pause

            j "Eu só vim relembrar os velhos tempos..."

            "Chefe" "Hmpf... eram outros tempos. Eu mudei, você mudou, o mundo mudou."

            j "Quer dizer que eu não te excito mais? Eu até me depilei pra você..."

            "Chefe" "..."

            j "Não consegue negar? Eu sabia... você sempre gostou de me comer... não ia mudar agora."

            "Chefe" "[j]... eu mandei você voltar ao trabalho! Eu perdi minha esposa por sua causa!"

            w "!?"

            j "Minha? Quer dizer que é minha culpa quando você me chamava na sua sala?"

            "Chefe" "Puta que pariu! Eu sei que a culpa foi minha! E eu paguei caro por... você sabe..."

            j "E por que você ia me recusar agora? Será que você não dá mais no coro?"

            "Chefe" "Nada disso... eu ainda aguento uma mulher igual sempre aguentei."

            scene black with dissolve

            scene sofia5_new5 with Dissolve(1.0)

            pause

            j "Então... será que eu posso... me servir?"

            "Chefe" "A questão é que esse tipo de relação não é mais aceitável hoje em dia."

            j "Hahaha... conta outra, velho. Isso nunca te impediu antes. Quantas estagiárias você promoveu assim?"

            "Chefe" "Hm... você você foi a única. Eu aprendi logo na primeira a dor de cabeça!"

            j "Eu não sabia... que eu tinha sido sua única."

            "Chefe" "Não é como se nós fôssemos amigos, não é mesmo?"

            j "Tem razão. Você continua afiado. Acho que foi isso que eu vi em você naquela época."

            "Chefe" "Nem vem... eu conheço o sabor doce do seu veneno. Nada que vem de você é grátis, [j]."

            "Chefe" "O que você quer? Por que tá me agradando desse jeito?"

            j "Eu posso ter ficado um pouco nostálgica... lembrando do passado..."

            "Chefe" "Você devia procurar outros dos seus ex-ficantes. Eu sei que tem uma boa lista pra você procurar."

            j "Não imaginei que você me trataria com essa frieza... eu sempre dei o que você quis... prazer e dinheiro..."

            "Chefe" "Com certeza... seu corpo continua gostoso como sempre, e suas matérias também... mas eu parei."

            "Chefe" "Agora eu só procuro sexo com mulheres que eu posso pagar. A relação é mais simples."

            j "Você virou um velho triste e amargurado..."

            "Chefe" "Com certeza. E você virou uma arrogante e mesquinha que se vende pra quem dá mais."

            scene black with dissolve

            scene sofia5_new6 with Dissolve(1.0)

            pause

            j "Huh... você acabou com o clima."

            "Pai... você realmente resistiu? Eu não acredito..."

            "Até eu... e-eu... d-digo..."

            j "Eu só queria fazer você se sentir bem uma última vez..."

            "Chefe" "Então é isso? Você queria me afagar com a buceta enquanto me apunhala pelas costas?"

            j "Você prefere apenas sentir a facada?"

            "Chefe" "Heh... não ache que eu vou cair sem lutar. Eu sei com quem você se aliou. A banda podre da capital."

            j "Eu pensei que todos nós fôssemos podres..."

            "Chefe" "Eles são um pouco mais. Não são essas pessoas que roubaram n... sua filha?"

            w "!!?"

            j "..."

            j "Você sabe que eu odeio quando você fala dela."

            "Chefe" "Eu sei como o arrependimento dói. E, pode ter certeza, você merece."

            j "Seu velho nojento... traidor... antiquado... você é um péssimo pai, não tem amor, só tem esta porra de revista!"

            j "E por pouco tempo! Essa revista é a única coisa no nosso caminho agora!"

            "Chefe" "'Nosso'? Você realmente acha que entrou pro grupo deles? Você é peixe pequeno demais pra se sentir naquele aquário, idiota."

            j "Não adianta tentar fazer minha cabeça! Você vai perder a única coisa que te restou! E eu vou rir muito quando você sair por aquela porta!"

            j "A gente tá no século XXI! Ninguém mais lê revista! Você devia aceitar o dinheiro e viver bem o resto da vida!"

            "Chefe" "Você quer que eu me venda? Igual você fez?"

            scene black with dissolve

            scene sofia5_new7 with Dissolve(1.0)

            pause

            j "Acorda, seu velho idiota! Eles vão te dar um bônus! Pra eles é mais fácil! E você sai ganhando! Não seja cabeça dura!"

            "Chefe" "[j]! Eu achei que você me conhecesse depois de todos esses anos! Você sabe que eu não vou deixar isso acontecer!"

            "Chefe" "E é por causa da minha cabeça dura e do quanto eu me importo com essa porra de revista que os diretores fazem o que eu digo!"

            j "Por enquanto... nós vamos dar o golpe em breve. E quando os acionistas virem a quantidade de zeros no cheque... não tem lealdade que impeça."

            "Chefe" "Eu sei que hoje nenhum jovem compra jornal e revista em banca! Que a tiragem fica cada vez menor a cada ano!"

            "Chefe" "Eu sei que essa merda de redes sociais vieram pra ficar! Que as pessoas agora se informam no tal do FIDI!"

            j "É no 'FEED', velho."

            "Chefe" "Não me interessa! Eu nunca vou deixar um robô dizer o que eu vou ler! Pro inferno esse algoritmo!"

            "Chefe" "'Conteúdo relevante'! 'Relacionados'! Como as pessoas podem deixar um computador decidir o que elas vão ver!?"

            "Chefe" "Nesta merda de revista tem um ser humano com algum compromisso dizendo o que vai pra capa! Alguém que tem um coração!"

            "Chefe" "Eu faço isso há décadas! Tentar entender o que é importante e relevante pras pessoas! E eu tenho minha ética!"

            j "Mas... pelas vendas... parece que as pessoas preferem o tal do robô."

            "Chefe" "São todos idiotas! Nem fazem ideia do buraco que tão entrando!"

            "Chefe" "Você acha que o robô se importa se é mentira?! Você acha que ele se importa se a notícia vai fazer bem ou não pras pessoas?!"

            "Chefe" "As pessoas acham que eram manipuladas pelos jornais, e agora são manipuladas por esses engenheiros terríveis que criam essas... redes do caralho!"

            j "Sinceramente... eu cansei do seu sermão. Eu não tenho nenhum carinho por você, mas eu sempre respeitei o quanto você ama isso aqui."

            j "Eu tentei te trazer pro lado vencedor, eu tentei arranjar uma boa saída pra você, até tentei te dar um último momento de prazer."

            j "Você negou tudo. E agora fica me tratando como se eu fosse uma dessas crianças que não sabem nada. Você me treinou! Eu sei tudo isso!"

            j "Eu espero que você apodreça amargurado quando a revista passar pra gente. Mas saiba que eu vou fazer de tudo pra ela continuar existindo."

            "Chefe" "Idiota... quem vende a filha por poder jamais vai ter a ética necessária pra fazer qualquer obra que preste."

            j "Velho nojento... nunca mais fale da minha filha!"

            "Chefe" "Eu tenho pouco tempo, mas minha filha tá de volta. A gente vai impedir a compra e ela vai seguir meus passos."

            "Chefe" "E tem o garoto também. Aquele garoto é verde, inocente, quase um completo idiota, mas ele tem coração. Um coração que você infelizmente nunca teve."

            j "Hah! Se você soubesse o que aquele lá já fez... e sua filha não tá longe, não."

            scene black with dissolve

            scene sofia5_new9 with Dissolve(1.0)

            pause

            "Chefe" "Eu confio naqueles dois. Você nunca vai corromper eles. Assim como você e seus chefes nunca vão me corromper e nem minha revista!"

            "Chefe" "Boa sorte, [j]! Quando você olhar pra trás e ver que tudo o que você fez foi por nada, a dor no seu estômago vai ser igual a que eu sinto todos os dias."

            j "Veremos..."

            "Chefe" "Não esqueça de desligar a luz antes de sair. Como você sabe, a grana não tá tão boa quanto antes. Temos que economizar na energia."

            w "N-nossa! Ele tá vindo!"

            scene trabalho chefe_porta with hpunch

            pause 1.0

            "Ufa... deu pra se esconder..."

            "Eu não sabia que meu pai tnha tinha uma história dessas com a [j]... então ele treinou ela desde cedo aqui..."

            "E agora ela vai dar um golpe e tirar a revista dele... que maldição..."

            "Hm? Parece que ela não saiu ainda..."

            scene black with dissolve

            scene sofia5_new8 with Dissolve(1.0)

            pause

            "Parece que o que meu pai falou realmente mexeu com ela... mas ela mereceu."

            "Inclusive! A-acho que eu devia falar umas verdades na cara dela! E-ela não pode tratar meu pai assim!"

            label so5_premium1:

                "O que eu tô fazendo?! E-eu devia só sair daqui! M-mas..."

            menu:
                "Deixa eu sair daqui.":


                    "D-de jeito nenhum! Eu só tô achando uma desculpa pra... m-melhor eu ir."
                "Eu só vou xingar ela! Mostrar quem manda!":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_32

                        jump so5_premium1

                    $ sofia_premium = 1

                    "Desde aquele dia... eu não consigo parar de pensar na [j]. Ela parece uma mulher tão complexa. Confiante, mas errada... que coisa..."

                    "Eu sei que eu não devia... mas... é só pra xingar ela, certo?"

                    scene black with dissolve

                    scene sofia5_premium1 with Dissolve(1.0)

                    pause

                    w "[j]!"

                    w "Parece que seu charme não funcionou com o meu pai, né?!"

                    j "Veja só... bisbilhotando... será que você não é tão certinha igual a gente pensa?"

                    w "E-eu só não posso deixar você solta por aí! Meu pai é muito conivente com seu jeito! Sobra pra mim me preocupar com você!"

                    j "Será que é isso mesmo... ou você fica ansiosa pra ver a próxima sacanagem que eu vou fazer?"

                    w "Como é?!"

                    j "Você fica excitada vendo a putaria acontecendo na redação, não fica? Faz bastante sentido... pelo jeito que você é."

                    w "Para de falar coisas assim sobre mim!"

                    j "Quando você me pegou com a loirinha... você gostou bastante, não gostou?"

                    w "Aquilo! F-foi um erro, um descuido. Eu tava tensa demais. E foi tudo sua culpa. Você me forçou."

                    j "Hmm... então é isso?"

                    w "Isso o quê?! Eu não gosto do tom da sua voz!"

                    j "Você tá procurando alguém que force você a fazer coisas erradas..."

                    w "Que absurdo!"

                    j "Deixa eu te mostrar uma coisa."

                    w "O quê?"

                    scene black with dissolve

                    j "Olha..."

                    scene sofia5_premium2 with hpunch

                    pause

                    w "Que é isso?!"

                    j "Só estou dando o que você quer."

                    w "Você acha que me entende?! Você só tá procurando justificativa pro seu comportamento abusivo!"

                    j "O que você veio fazer aqui então?"

                    w "Eu vim te falar umas verdades!"

                    j "Então diga... fale de uma vez o que você veio me falar."

                    w "Q-que você nunca... n-nunca vai conseguir entregar nossa revista! Meu pai tá vacinado contra você!"

                    j "É o que parece..."

                    w "Você pode achar que consegue o que quer com sua sensualidade, com o prazer, mas ele não vai cair nessa!"

                    j "Uhum..."

                    w "Meu pai nunca vai acertar algo assim só pra sentir você... pra se esfregar em voce... entendeu!?"

                    j "Muito bem... entendi seu ponto de vista..."

                    w "Excelente! Agora me solta!"

                    j "A única coisa que não ficou claro pra mim..."

                    scene sofia5_premium3 with Dissolve(1.0)

                    j "É quanto a você..."

                    w "C-como é?!"

                    j "Você foi bem enfática dizendo que eu não vou dobrar seu pai com a minha buceta... agora... e você?"

                    j "Eu não escutei nenhuma vez você dizendo que não iria aceitar também."

                    j "Pelo contrário... senti você narrando o que aconteceria entre eu e seu pai até de uma forma bem... luxuriosa..."

                    w "Que absurdo! Eu tô vacinada também!"

                    j "O fato de você ter vindo aqui... sem razão alguma... mostra que você tá longe disso, bonequinha."

                    j "Você pode ser toda severa na frente de todo mundo, mas, no fundo, você sente prazer como qualquer outra pessoa."

                    w "Não fala besteira... eu não suporto pessoas que vivem só pra ter prazer."

                    j "E mesmo assim... você é uma delas."

                    w "P-para de falar essas coisas de mim!"

                    j "Todo mundo que fica irritado demais com uma coisa... é porque lá no fundo também quer... sabia?"

                    w "Você fala... qualquer coisa pra justificar sua postura inescrupulosa, só isso..."

                    w "E t-tira essa coxa do meio... hmm... das m-minhas pernas..."

                    j "Só agora que você notou? Ou você tava gostando até agora?"

                    w "C-cala a boca! Eu nunca vou me dobrar a você! Por mais gostoso que você faça eu me sentir!"

                    scene sofia5_premium4 with Dissolve(1.0)

                    pause

                    j "Hmmm... então eu realmente faço você se sentir bem... finalmente você foi sincera..."

                    w "N-não! Não foi isso que eu quis dizer! E não chega perto assim! E para de se esfregar em m-mim!"

                    j "Sua boca fala uma coisa... mas seu corpo que é outra totalmente diferente..."

                    j "Você quer sentir prazer... aqui e agora... com a pessoa mais sexy e quente que você conhece..."

                    w "N-nunca!"

                    j "Você quer se entregar a esse prazer e esquecer todas as preocupações..."

                    j "Um momento de pura luxúria... de puro prazer..."

                    w "Ah... cala a boca... sua boca... tá perto de mais..."

                    j "É sua última chance. Ou você sai correndo agora... ou eu vou fazer o que eu quiser com você."

                    j "Você vai sentir tanto prazer... que nunca mais vai esquecer... vai ser impossível voltar a ser quem você é."

                    w "Q-quê!? C-como você pode falar isso... isso..."

                    j "Não acredita? Eu já fiz isso com dezenas de bonequinhas e bonequinhos iguais a você... que nunca mais conseguiram viver como antes."

                    w "Ah... n-não..."

                    "Minha cabeça tá começando a ficar embaçada... se eu continuar aqui... eu não sei se..."

                    "Vir aqui fui um erro! Eu sabia desde o começo! E mesmo assim..."

                    "Eu não acredito que eu tava procurando isso... essa não sou eu... não..."

                    menu:
                        "Pode vir. Eu nunca vou me corromper.":


                            "Não é possível que eu sou fraca desse jeito. A Cássia nunca vai entrar na minha cabeça."

                            w "Eu não sou uma das suas bonequinhas... eu tenho controle sobre o que eu faço!"

                            j "Você fala, fala... mas continua aqui."

                            w "Eu não tenho medo de você..."

                            scene sofia5_premium5 with hpunch

                            pause

                            j "Vai ser tão prazeroso ver você se contorcendo de prazer nas minhas mãos, pombinha!"

                            w "E-ei!"

                            j "Quando que quebrar essa sua máscara e ver você implorando pra eu fazer você gozar igual uma cadela!"

                            w "NGGH!!!"

                            j "Não consegue se soltar, é? Você é magrinha... você tá nas minhas mãos..."

                            "Ela é mais forte do que eu! E-eu não posso me soltar..."

                            "Calma, [w]... Eu só tenho que manter minha cabeça no lugar. Não vai entrar no jogo dela."

                            j "Você ficou tão excitada vendo eu e a loirinha se pegando, não foi? Ela era igualzinha você antes..."

                            w "E-eu..."

                            j "Será que ver eu seduzindo seu pai também te deixou toda excitada?"

                            w "C-claro que não... eu nunca... nunca... vou me dobrar a você."

                            j "A gente tá só começando, gatinha... você vai se sentir muito bem hoje..."

                            scene sofia5_premium6 with Dissolve(1.0)

                            pause

                            w "A-ah!"

                            j "A loirinha da recepção tinha uma fraqueza aqui no pescoço... lembra?"

                            w "O que você tá fazeeennndooh..."

                            j "O pescoço é uma zona erógena muito grande pra maioria das mulheres... a gente adora ser pega por trás e sentir gostoso no pescoço."

                            w "Ahnn... p-pare com isso agora!"

                            j "E se eu não parar? O que vai acontecer?"

                            "Minha cabeça... tá tudo rodando... por que sentir ela no meu pescoço mexe tanto comigo?"

                            "A língua dela em mim... essas mãos fortes nos meus seios... a coxa dela apertando minha bunda..."

                            "É coisa demais... em todos os lugares..."

                            w "Aah! N-não!"

                            j "Foi um gemido que eu escutei agora? Você realmente tá adorando isso aqui, não tá?"

                            w "Não! Nnngh! P-para por favor!"

                            scene sofia5_premium7 with Dissolve(1.0)

                            pause

                            w "Aaggnh! N-não pega aí!"

                            j "Mesmo de calça jeans... você sente eu apertando sua bucetinha?"

                            w "Paraaa... [j]... p-por favor..."

                            j "Você tá tentando afastar minha língua do seu pescoço ou tá me abraçando?"

                            w "Ahn?!"

                            j "Você nem sabe mais o que seu corpo tá fazendo... você só quer continuar sentindo gostoso..."

                            "Como? Ela tá certa... eu tô cada vez mais perdida... o que eu vim fazer aqui?"

                            "Eu queria que ela me usasse? Impossível..."

                            w "Você... hmm... tá indo rápido demais... e-eu..."

                            j "Só isso é demais pra você, gatinha? Eu achei que você ia dar um pouco mais de trabalho."

                            j "Talvez no fim você realmente era só uma putinha mesmo esperando alguém com fibra o suficiente pra te colocar no seu lugar."

                            w "Ah... Não seja vulgar..."

                            "Ela fala essas coisas de mim... mas por que isso não me deixa brava?"

                            j "Você não precisa mais disso aqui, certo?"

                            w "Não... não tira minha... aah... roupa... por favor..."

                            scene sofia5_premium8 with Dissolve(1.0)

                            pause

                            j "Você não manda nada agora. Você só obedece. É isso que você sempre quis, sua puta."

                            w "Aah..."

                            "Eu sinto meu coração batendo mais forte quando ela me trata assim."

                            "Eu não tenho mais força pra discutir... eu só quero que ela termine de uma vez..."

                            j "Não vai falar nada? Finalmente você resolveu ser sincera."

                            w "Termina logo... nnghh... faz o que você tem que fazer e me deixa!"

                            "Vir aqui foi um erro! E agora eu tenho que pagar por essa decisão!"

                            "Eu vou deixar a [j] me usar como ela quiser, e nunca mais eu vou querer nada com ela!"

                            w "Ai... ah... ai..."

                            j "Isso... vai curtindo, bonequinha... eu só vou parar quando você tiver implorando pra eu continuar."

                            w "Naumm... ahh... minha calça naaummm..."

                            j "Não é mais gostoso sentir direto na sua buceta?"

                            w "Aaiin... naaumm!"

                            scene sofia5_premium9 with Dissolve(1.0)

                            pause

                            j "Que delícia... agora sim!"

                            "Eu não consigo negar... eu não consigo empurrar ela... eu não nem pensar mais..."

                            "Eu tô virando um objeto pra Cássia brincar... e o pior é que quanto mais ela me provoca, mais gostoso fica!"

                            "[mc]... se as coisas continuarem assim... eu..."

                            "[mc]..."

                            j "Hm? Que foi? Seu corpo parece diferente."

                            w "[j]... eu tenho que parar aqui!"

                            j "Por que sua voz tá assim? Você sabe que não adianta lutar."

                            w "Eu gosto de alguém... e eu não posso trair essa pessoa assim!"

                            j "Você tá falando do pombinho?! Que fofos! Mas isso é ridículo!"

                            w "Por quê?!"

                            j "Você vai perder toda essa sensação incrível... por alguém que nunca teve coragem de fazer nada com você?"

                            w "!"

                            j "Vai deixar de sentir minha língua no seu pescoço... minha mão acariciando seu botãozinho... minha coxa na sua bunda..."

                            w "Ah..."

                            j "Pra ficar com alguém que nunca teve coragem de te beijar? É isso mesmo?"

                            w "M-mas..."

                            j "O que você prefere? Perder tudo isso agora? Continuar insatisfeita pra sempre?"

                            j "Se entregue ao prazer... ele nunca vai saber mesmo..."

                            w "Mas eu vou..."

                            j "Aproveite... se entregue... você sabe que é tudo culpa minha..."

                            w "Tudo usa... hmm..."

                            menu:
                                "É tudo culpa dela. Não tenho o que fazer.":


                                    "É tudo culpa dela, [mc]..."

                                    w "Tem razão... aiin... você tá me obrigando... aaah..."

                                    j "Isso mesmo... agora tira isso aqui. Olha o que você ia perder."

                                    scene sofia5_premium10 with Dissolve(1.0)

                                    pause

                                    w "Ai, [j]... cuidado..."

                                    j "Cala a boca. Você acabou de trair o rapaz que você gosta. Você não merece nada."

                                    w "Quê?! Ahn! Mas foi você!"

                                    j "Não se faça de idiota! Você sabe muito bem que você tá pouco se fodendo pra ele! Você só quer gozar!"

                                    w "Aii! Nauuumm! Não faz forte assim! NGHH!!"

                                    j "Ver uma vadia hipócrita me irrita!"

                                    "Ela tem razão! Eu sou só uma vadia que quer gozar!"

                                    "Não! É isso que ela quer que eu pense!"

                                    w "Ai, [j]! Você tá esfregannndo demais! Aahhnn!"

                                    j "Vai chegar lá, vadia?"

                                    w "S-se você con- hnnnmm!!!"

                                    j "A vadia quer gozar, é?!"

                                    w "Aainn! E-eu!"

                                    scene sofia5_premium11 with Dissolve(1.0)

                                    pause

                                    j "Você tá pingando! Pensar no seu amor te deixou mais excitada ainda?!"

                                    w "Ahh!"

                                    j "Ou será que foi trair ele que te deixou assim, hm!?"

                                    w "Não fala assimmm! Nnnghh!"

                                    j "Vai gozar?!"

                                    w "S-sim! Aaahh! E-eu vou gozar!! C-continua assim!"

                                    j "Na-na-não..."

                                    scene sofia5_premium11 with hpunch

                                    w "Não para! Por favor, continua!"

                                    j "Não adianta se debater... eu ainda não permito que você goze."

                                    w "Por quê?!"

                                    j "Você vai ter que me mostrar que você merece... que você é uma boa garota... e daí eu te dou uma gozada de recompensa."

                                    "Eu nem sei mais o que ela quer dizer... eu só preciso gozar... eu já fui humilhada, denegrida... só faz eu gozar!"

                                    w "Tá..."

                                    j "Deita aqui..."

                                    w "Tá... vem..."

                                    j "Eu tô indo, bebezinha..."

                                    scene black with dissolve

                                    scene sofia5_premium12 with Dissolve(1.0)

                                    pause

                                    w "Ah... sua coxa..."

                                    j "Você gosta?"

                                    w "Sim... ai... você sabe que eu adoro... hmm..."

                                    j "Você perdeu toda a vergonha..."

                                    w "Não importa... só faz eu gozarr.... vaaiiin!"

                                    j "Chegou a hora do seu teste então..."

                                    w "Por favor..."

                                    j "Se você realmente sabe seu lugar... se você aprendeu que você é uma puta que precisa sentir prazer pra ser feliz... faz uma coisa."

                                    j "Colooca sua língua pra fora... pra eu ter certeza que você não tem mais honra nenhuma."

                                    "Ela continua me denegrindo... essa sádica sente prazer vendo eu ser a cadelinha dela..."

                                    "Mas..."

                                    "Quando ela me trata assim, eu fico mais e mais excitada... ser a cadelinha dela vai fazer eu gozar... e eu preciso gozar..."

                                    w "Ah... eu vou ser sua putinha..."

                                    j "Então vai... lambe minha língua, cadelinha..."

                                    menu:
                                        "Lutar contra essa vontade":


                                            "Eu preciso..."

                                            "Pfff... quem eu tô enganando? Eu não tenho mais nada..."
                                        "Desistir de sua honra e se submeter à Cássia":


                                            pass

                                    "Eu não tenho mais um pingo de respeito próprio."

                                    "Eu só quero que ela me use... como a putinha dela..."

                                    scene sofia5_premium13 with Dissolve(1.0)

                                    pause

                                    w "Aaaah...."

                                    j "Assim mesmo, meu amor."

                                    w "Hmm... isso..."

                                    j "Você mereceu... fica com a língua assim agora... até eu acabar com você."

                                    w "S-sim, senhora..."

                                    j "Senhora... gostei..."

                                    w "Hmm... ah..."

                                    j "Sente minha coxa gostosa esgregando sua buceta suja."

                                    w "Aain... ai... assim..."

                                    j "Quanto mais eles falam não no começo... mais safados eles são no final... incrível..."

                                    j "Homens... mulheres... são todos iguais. Todos querem se sentir bem. E não tem coisa mais gostosa que sexo bem feito."

                                    w "Ssiiimmm... aaahhh..."

                                    j "Isso... mantém a língua pra fora..."

                                    w "Ahaamm.... hmm... só não para..."

                                    scene black with dissolve

                                    scene sofia5_premium14 with Dissolve(1.0)

                                    pause

                                    j "Isso, meu amor... você mereceu..."

                                    j "Goza pra sua dona."

                                    w "Sim! Assim mesmo! NNGH!!!"

                                    j "Falta pouco agora! Logo logo você vai tá livre!"

                                    w "Isso! AAHH!! Me deixa livre!!! NNNGHHHHAAAA!!!"

                                    w "FINALMENTE! EU VOU GOZAR! NNNGHHHAAA!!!"

                                    scene sofia5_premium15 with hpunch

                                    pause

                                    w "AAAAAAGHHH!!!"

                                    scene sofia5_premium15 with hpunch

                                    w "AAIII!!! AAANHNNN!!!"

                                    scene sofia5_premium15 with hpunch

                                    w "Aaahn..."

                                    w "Puta que pariu..."

                                    j "É bom, né?"

                                    w "Ainda tô tremendo..."

                                    j "Muito bem... meu trabalho aqui terminou."

                                    scene black with dissolve

                                    scene sofia5_premium16 with Dissolve(1.0)

                                    pause

                                    w "Ah... o que aconteceu aqui?"

                                    j "Eu garanti meu sucesso... isso que aconteceu..."

                                    w "Hm? Já vai?"

                                    j "Claro. Eu posso não ter o velho... mas se eu tiver você, o velho vai cair de qualquer jeito."

                                    w "Eu já te falei... eu posso não ter o melhor controle sobre meus impulsos sexuais..."

                                    w "... mas eu nunca vou deixar isso corromper meu trabalho..."

                                    j "Isso é o que você fala agora, pombinha... mas quando você tiver dentro do buraco... de verdade... você não vai ter outra escolha."

                                    w "Uma pessoa como você, que vê tudo dessa forma, nunca vai entender o que é ter valores."

                                    j "Valores valem tanto quanto a promessa de uma boa gozada. Quando chegar a hora, você vai entender."

                                    w "Vamos ver..."

                                    j "Adeus, gatinha. Não esqueça de apagar a luz. Você ouviu seu pai."

                                    w "..."

                                    "Eu nunca vou deixar o prazer corromper meus valores..."

                                    "Nunca."
                                "De jeito nenhum! Adeus!":


                                    w "Não! O que importa é o que eu sei! E eu sou uma pessoa certa! ADEUS!"

                                    scene black with hpunch

                                    j "Droga, pombinho! Como você consegue me ferrar desse jeito?!"

                                    j "Eu tava tão perto!!!"
                        "Não posso arriscar! Deixa eu correr!":


                            "Não dá pra arriscar! Eu não quero ficar aqui pra ver se a Cássia tá certa ou não!"

                            w "Não me interessa o que você acha! Eu não quero ter nada a ver com você!"

                            j "Você fala, fala... mas continua aqui."

                            w "!!!"

                            w "A-adeus!"

                            scene black with hpunch

                            j "Droga... a fedelha é mais cabeça dura do que eu imaginava..."
        "Eu não tenho nada com isso.":


            w "Eu não tenho a mínima vontade de saber o que esses dois tão fazendo aí. Dá pra imaginar."

            "Que decepção, pai... eu achando que pelo menos nisso você tinha carater."



    label so5_final_premium:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 3

    scene black with Dissolve(3.0)

    jump call_cidade

label sofia_18_2:

    $ estou_na_cidade = False



    scene black with Dissolve(1.0)

    pause 1.0

    scene trabalho angulo with Dissolve(1.0)

    $ sofia_premium = 2

    pause

    mc "Sofia?"

    mc "Alguém viu a Sofia? Tem uma matéria aqui sobre o fim da água no planeta. Isso é sério?!"

    mc "Cadê essa mulher?"

    mc "Renata... você viu a... ué? Cadê ela?"

    "Só falta a Cássia tá aqui e a Sofia não. Seria o fim do mundo."

    scene black with dissolve

    scene cassia sentada_rindo with Dissolve(1.0)

    mc "Cássia... você tá aqui mesmo... como pode?"

    j "Pombinho! Você vindo aqui. O que você precisa?"

    mc "Por que você acha que eu preciso de alguma coisa?"

    j "Ah... você só me procura quando precisa de alguma coisa. Inclusive, você já me chamou de interesseira, mas a gente é bem parecido."

    mc "Sei não... vou pensar sobre isso."

    j "Pense... você vai ver... e o que você precisa hoje?"

    mc "É... eu preciso de uma coisa mesmo. Você viu a Sofia?"

    j "Não vi... e espero não continuar vendo."

    mc "Vocês não se entendem, né? Hehe..."

    j "Agora que você falou, pombinho... sendo sincera... a gente até se entendeu em algumas coisas."

    mc "Sério?"

    j "A gente encontrou um... como eu posso dizer... um ponto em comum. Uma coisa que nós duas conseguimos concordar."

    mc "Puxa... não imaginei essa."

    j "No fundo todos nós somos humanos, não é verdade, pombinho? Assim como você... a gente tem nossas coisas em comum também, não concorda?"

    menu:
        "Bom... sim...":


            mc "É... a gente tem, né? E é uma delícia..."

            j "Mediano, mas viu só?"
        "Nem vem.":


            mc "Nem vem. Eu não tenho nada contigo, não."

            j "Você pode continuar repetindo isso o quanto você quiser... não muda o que aconteceu..."

    mc "Ok... mas se você não viu a Sofia... nem a Renata eu tô achando."

    j "Ah... essas duas tão de conversinha ultimamente. Será que elas encontraram algo em comum também?"

    mc "Não acho... a Sofia nunca foi de falar com ninguém..."

    j "A chefinha pode tá mudando. Descobrindo coisas que ela não sabia que gostava..."

    mc "As coisas parecem muito estranhas, isso sim..."

    j "Estranhas pra você, bobinho. As pessoas são assim. Elas escondem segredos. Quem sabe as duas têm algo que acabaram descobrindo juntas?"

    mc "Eu só queria perguntar pra ela sobre uma matéria... ela nunca desapareceu assim."

    j "Parece que as coisas realmente tão mudando... talvez todo esse apego pelo trabalho era só falta de algo. Agora que ela achou..."

    mc "Eu não tô gostando do rumo dessa conversa. Eu sinto que tem um lance... é... obceno no que você tá falando."

    j "Claro que não. A pombinha não é ligada nessas coisas, né?"

    if sofia_namoro and premium:

        "Depois daquele lance no apê dela... eu não tenho mais certeza de nada..."
    else:


        "Claro! A Sofia nunca ia se envolver assim..."

    mc "Aqui na redação? Impossível..."

    j "Tem razão... impossível..."

    mc "Bom... eu vou nessa. Amanhã eu falo com ela."

    j "Vai lá, pombinho... Eu tenho que me preparar. Eu vou terminar de ferrar alguém. Aliás, vai se acostumando..."

    j "A chefinha é só a primeira... logo logo a redação vai ter uma outra cara. Não se esquece que você pode ficar de um lado ou de outro."

    mc "Hum..."

    scene black with Dissolve(1.0)

    "A [j] parece feliz demais... Não sei se eu gosto disso..."

    "Cadê você, Sofia?"

    pause 1.0

    scene trabalho lounge with Dissolve(1.0)

    pause

    w "Eu tenho que te pedir desculpas. Nunca imaginei que seria tão fácil falar com você."

    scene black with dissolve

    scene sofia18_new1 with Dissolve(1.0)

    pause

    re "Eu aceito. Você sempre foi meio esnobe. Não ia com a tua cara."

    w "É... e parece que agora a gente tá conversando tão bem... estranho, né?"

    re "Não acho estranho, não. Pra mim, você mudou esses últimos tempos."

    w "Quê?"

    re "É sério. Você só sabia falar de trabalho, trabalho, trabalho... mas a gente quase não conversa sobre isso."

    w "Agora que você falou... é verdade... nunca tinha reparado."

    re "Hehe... eu te conto dos meus ex-namorados... e você parece bem interessada nas coisas que eu passei com eles."

    w "A-ah! N-nem tanto assim... eu acho um tanto frívolo, mas... sei lá... acho que eu gosto mesmo..."

    re "Não tem problema gostar. Às vezes a gente acaba descobrindo coisas que a gente achava que não gostava, mas gosta."

    w "Isso até que foi bem profundo, [re]... você tem razão."

    re "Eu nunca pensei que eu fosse chegada em mulheres... mas depois que eu experimentei... hmmm..."

    w "S-sério?"

    re "Só de pensar... eu vou ficando excitada, sabe?"

    w "Ah... entendi... eu nunca pensei nisso... acho que eu nunca me importei se era homem ou mulher."

    re "Que interessante, [w]. Isso aí tem um nome. Mas eu não sei qual é. Contanto que seja bom, é o que importa, né?"

    w "N-não sei se é bem assim... mas... agora que você falou... esses tempos tem acontecido umas coisas comigo que eu fico meio..."

    re "Pode falar pra mim... eu sou sua amiga agora, né?"

    w "D-desculpa. Eu tenho vergonha. São coisas bem pessoais. Tem a ver com relacionamentos, sabe?"

    re "É o tipo de coisa que eu adoro conversar..."

    scene sofia18_new2 with Dissolve(1.0)

    re "Escuta, [w]... só de conversar sobre essas coisas minhas pernas já começam a roçar uma na outra, acredita?"

    w "Q-quê?! [re].... por favor..."

    re "Que foi? Eu não tenho vergonha de falar isso na sua frente."

    w "Mas isso não tá certo... você me deixa sem jeito."

    re "Nós duas somos mulheres! Para de ser boba! A gente tem liberdade pra falar de tudo. Agora conta!"

    w "Nossa senhora... tá... é que recentemente tem acontecido umas coisas que me mostraram um outro lado das coisas."

    re "Entendi foi nada!"

    w "Que saco... é... você mesma falou! Antes eu só falava de trabalho... mas eu... comecei a reparar em outras c-coisas ultimamente."

    re "Isso é bom! Você tá se abrindo! E tá uma pessoa muito mais interessante agora!"

    w "Obrigada... mas eu tenho medo... parece que quanto mais eu experimento... mais difícil é voltar ao que eu era..."

    re "E qual o problema?! Se você tá melhorando, por que você quer voltar?!"

    w "Não é tão simples assim... eu não sei se eu quero mudar... e eu tenho medo até onde eu posso chegar se as coisas continuarem assim."

    re "Hmm... você tá falando de sacanagem, né?"

    w "Q-quê?! Ah... então... droga... s-sim..."

    re "Sabia! Não é à toa que só o jeito de você falar já tá mexendo comigo!"

    w "Ai, [re]... você é sincera demais! Se controla, garota!"

    re "Não!"

    scene black with hpunch

    w "AAHNN?!"

    scene sofia18_new3 with hpunch

    pause

    w "O que você tá fazendo?!"

    re "Você me deixou excitada com esse papo! Você, toda certinha, indo pro mal caminho! Só de pensar me deixa assim!"

    w "Que absurdo! M-me solta!"

    re "Eu também era igual você, [w]! Eu me segurava! Vivia frustrada! Mas eu aprendi que se soltar é tudo de bom!"

    w "N-nem começa! Você tá parecendo outra pessoa! Tá igual outra pessoa aqui da redação!"

    re "Eu sempre achei que você fosse uma moça cheia de vontade, sabia?!"

    w "Eu?! Eu nunca fiz nada!"

    re "Olha pra sua blusinha! Uma garota que vem trabalhar assim! E sem sutiã, só pode tá pedindo!"

    w "Você perdeu a cabeça, tonta! A roupa que eu uso é problema meu! E eu só me sinto mais à vontade assim! Nada a ver!"

    w "E para de passar a mão em mim desse jeito! Eu não deixei você fazer isso! Solta agora!"

    label so18_premium1:

        "O que eu tô fazendo?! E-eu devia só sair daqui! M-mas..."

    menu:
        "Empurrar ela e sair da sala":


            w "ME SOLTA!!!"

            scene black with hpunch

            re "Ai! Me machucou!"

            w "Você mereceu! E nunca mais faça isso, ou não falo mais com você!"

            re "Tá..."

            w "A gente precisa respeitar as pessoas. Quando alguém fala 'não', não é 'meio sim', nem 'talvez'. É NÃO!"

            re "D-desculpa..."

            w "Ok... agora de volta ao trabalho."

            re "Ahh..."
        "Continuar pedindo pra ela soltar":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_33

                jump so18_premium1

            w "Já falei pra soltar!!!"

            re "Você pode falar o que você quiser, mulher! Você continua aqui se esfregando em mim!"

            w "Claro que não! Só não quero te machucar!"

            re "Será que é isso mesmo ou você quer..."

            w "RENATA?!"

            scene sofia18_premium4 with hpunch

            pause

            w "A-ai! O que você tá fazendo?!"

            re "Toda mulher adora sentir no pescoço, [w]... aposto que você também fica excitada, não fica?"

            w "Ah... você tá me forçando a fazer uma coisa que eu não quero! Isso é crime!"

            re "Então me prende."

            w "Hmm... não acredito que você continua com isso..."

            re "Você me disse que tava descobrindo uma coisa nova..."

            w "Mas... ah... não é assim..."

            re "O problema sou eu então?"

            if sofia_namoro:

                w "E-eu aceitei namorar com alguém..."

                re "Eu também tô namorando. Não tem problema."

                w "Não é assim que funciona..."
            else:


                w "N-não... eu não tô namorando... mas..."

                re "Então qual o problema?"

            re "Eu juro que você vai gostar."

            w "N-não... ai... não é isso... é que..."

            scene sofia18_premium5 with Dissolve(1.0)

            pause

            re "Certeza que você não quer?"

            w "Q-que que é isso?"

            re "Não quer sentir minha língua dentro da sua boca, hm?"

            w "Ai..."

            "Como ela sabe que eu gosto no pescoço? E que eu t-tenho essa coisa com o beijo..."

            re "Não quer lamber e chupar ela?"

            w "[re]... para..."

            re "Sua língua tá quase saindo da sua boca, safada..."

            w "N-não... a gente não pode..."

            "Só de pensar na gente se beijando... minha cabeça começa a ficar vazia..."

            "Parece que eu tô perdendo o controle cada vez mais fácil..."

            re "Não pode? Então querer você quer..."

            w "E-eu..."

            menu:
                "Eu não posso e não quero! Sai!":


                    w "Eu disse que não quero!"

                    w "ME SOLTA!!!"

                    scene black with hpunch

                    re "Ai! Me machucou!"

                    w "Você mereceu! E nunca mais faça isso, ou não falo mais com você!"

                    re "Tá..."

                    w "A gente precisa respeitar as pessoas. Quando alguém fala 'não', não é 'meio sim', nem 'talvez'. É NÃO!"

                    re "D-desculpa..."

                    w "Ok... agora de volta ao trabalho."

                    re "Ahh..."
                "Q-querer eu...":


                    w "Q-querer eu... digo... não é isso..."

                    re "Entendi tudo. Vira e coloca e linguinha pra fora, vai..."

                    w "Não..."

                    re "Sente minha boca... esfrega sua língua na minha... eu sei que você adora..."

                    w "C-como... você..."

                    re "Vai... aaaah...."

                    scene sofia18_premium6 with Dissolve(1.0)

                    w "Aahh..."

                    re "Isso... assim mesmo, linda..."

                    w "Isso é tão errado, [re]... mas você é impossível..."

                    re "Hmmm..."

                    w "Aahh..."

                    re "Que linda..."

                    w "Para de me deixar assim... você vai me beijar ou não vai?"

                    re "Claro que eu vou... eu também tô igual você."

                    scene sofia18_premium7 with Dissolve(1.0)

                    pause

                    w "MMNN!"

                    re "Nnngh..."

                    w "Finalmente! Essa língua na minha boca!"

                    re "Eu adorei seu gosto, [w]. E você beija bem pra caralho."

                    w "Eu sempre gostei de beijar, mas depois da faculdade... hmm..."

                    re "A gente se fala mais depois, né?"

                    w "É... agora você usa sua boca pra chupar minha língua."

                    re "Hmm..."

                    w "Aahhn... assim..."

                    w "Você já tirou a blusa?"

                    re "Eu quero que você pegue em mim..."

                    w "Eu pego... só não tira sua língua da minha boca."

                    scene sofia18_premium8 with Dissolve(1.0)

                    pause

                    re "Ain... assim mesmo..."

                    w "Uhumm..."

                    w "Desse jeito eu vou... aah... acabar... você sabe... nnnghh..."

                    re "Assim... rápido desse jeito?"

                    w "Hmmnnn... tá bom demais... ai..."

                    re "Eu também gozava rapidinho assim... hoje eu preciso de muito mais..."

                    w "Ah... e-eu te ajudo... hmm..."

                    re "Vem aqui então. Tira essa roupa."

                    w "Não... aqui na redação não dá..."

                    re "Ninguém vai vir aqui agora..."

                    w "Minha nossa, [re]..."

                    re "Deita logo, linda."

                    scene black with dissolve

                    scene sofia18_premium9 with Dissolve(1.0)

                    pause

                    w "Ai... tô tão nervosa..."

                    re "Xii... só me beija..."

                    w "Nngh... você sabe meu ponto fraco... aah..."

                    re "Claro... a Cássia me falou..."

                    w "NNGH!"

                    w "Então foi ela... hmmm... v-vocês me enganaram... nnnghh..."

                    re "Isso importa agora? Não tá bom?"

                    w "Tá... eu só quero beijar agora... mmmnnn..."

                    re "Cada vez mais as coisas vão ter menos importância, gata..."

                    re "Você vai querer beijar e tirar a roupa... sentir esse prazer... mais e mais..."

                    w "Uhuumm... p-parece boommm... aah..."

                    re "É uma delícia... você vai aproveitar muito mais, [w]..."

                    w "Tá... nnnghh... agora faz eu gozar... por favor..."

                    re "Então vem... abre a boca e me chupa mais..."

                    scene sofia18_premium10 with Dissolve(1.0)

                    pause

                    w "Ai... isso, gostosa... hmm..."

                    re "Você tá cada vez mais louca, garota."

                    w "Sim... é tudo você... aah... eu não queria... mmmnnn..."

                    re "Não queria, né?"

                    w "Naaaumm... aaainn... assim... roça sua coxa em mim... nnngg..."

                    re "Ela me contou que você gosta assim também."

                    w "Eu sabia... ngnhh... fazer isso com aa... aaahn... Cássia... nunca ia dar certo... nnnghh!"

                    re "Você só tá se sentindo bem assim graças a ela, ingrata!"

                    w "!!!"

                    re "Nós duas. A gente deve muito a senhora Cássia."

                    w "[re]... mmnnngg... ela também... aahnn..."

                    re "Sim. Ela que me ensinou..."

                    w "Agora... hmmm... faz sentido... agora vai... eu tô quase!"

                    re "Me lambe que eu esfrego sua buceta até você gozar!"

                    scene sofia18_premium10 with hpunch

                    w "T-taaaiin! Tá! Ainn! Isso! Vaiin!!"

                    re "Assim?!"

                    w "É!! Por favorr!! Aaahh!"

                    w "Tá vindo! Que delícia! Vaiiiin!!!!"

                    scene sofia18_premium11 with hpunch

                    w "AAAAAGGHHHH!!!!"

                    re "Xiii! Vão te ouvir, louca!"

                    w "Aaahhnn! É demais! Nnnghh!"

                    w "Aaah... uhh..."

                    re "Foi bom assim, é?"

                    w "Ainda não acredito... que eu fiz isso aqui..."

                    re "Você vai ficar defendo uma pra mim..."

                    w "D-desculpa... eu..."

                    re "Você me paga outro dia, né? E não esquece a senhora Cássia."

                    w "Minha nossa... eu não quero ter mais nada com ela..."

                    re "Mas é bom, né? A gente acaba voltando... mesmo sem querer..."

                    w "É... mas eu vou tentar resistir..."

                    re "Ok..."

                    scene black with Dissolve(2.0)

                    "..."

                    scene trabalho geral with Dissolve(1.0)

                    pause 2.0

                    mc "Sofia? Sofia?!"

                    mc "De novo isso..."

                    "Essas últimas semanas eu não vejo mais a Sofia por aqui. Será que ela tá bem?"

                    if sofia_namoro:

                        "Será que ela tá me evitando por causa do nosso namoro?"

                    scene black with dissolve

                    w "Ah... ai..."

                    j "Huhu..."

                    scene sofia18_premium12 with Dissolve(1.0)

                    pause

                    w "Chega! AAHN! Por favor! NNGHH! Eu não aguento mais!"

                    j "A gente sempre pode superar seu limite e fazer um trabalho melhor! Você ensinou a gente isso!"

                    w "Não quero mais gozar! AAAGHHH!!!"

                    re "Já não tá bom, dona Cássia?"

                    j "De jeito nenhum... essa aí a gente precisa garantir que nunca mais vai conseguir viver sem a gente..."

                    w "N-não... aah..."

                    j "Quem você quer beijar agora?"

                    w "Eu não quero..."

                    w "Mas eu preciso... qualquer uma! Me beija!"

                    j "Huhuhu..."



    label s18_2_final:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 3

    jump call_cidade

label sofia_e1_conversa:

    if sofia_e1_confiou == 0:

        "Voz" "{i}Hic! Huumm...{/i}"

        mc desconfiado "Hm?"

        mc preocupado "Que porra é essa?"

        scene trabalho angulo with Dissolve(1.0)

        "Não era pra ter ninguém aqui essa hora além do segurança lá na frente."

        "Já tá dando aquele cagaço."

        "Voz" "{i}Huh-uh... hic....{/i}"

        "Tá vindo daqui do lounge."

        "..."

        scene sofia sofa_chorando with Dissolve(2.0)

        pause

        "É a [w]!"

        "Ela tá chorando?"

        "Merda! Que merda! O que eu faço?"

    elif sofia_e1_confiou == 1:

        w "{i}Hic! Huumm...{/i}"

        mc desconfiado "De novo esse choro?"

        "Será que é a [w] de novo?"

        scene sofia sofa_chorando with Dissolve(2.0)

        pause

        mc preocupado "..."

        "Droga. Ela tá chorando de novo. O que será que tá rolando?"

        "A [j] disse que ela não ia aguentar. Acho que ela tinha razão."

        "Mas a guria continua vindo trabalhar todo dia. Será que ela desistiu mesmo?"

    elif sofia_e1_confiou == 2:

        $ sofia_confiou = True

        "..."

        mc desconfiado "..."

        "..."

        "Não tô ouvindo nada..."

        scene trabalho lounge with Dissolve(1.0)

        pause

        "Ufa. Acho que a [w] não tá aqui hoje. Mas então... será que ela..."

        show sofia rindo with moveinbottom

        w "[mc]."

        mc surpreso "S-Sofia?!"

        w "Que foi? Parece que viu um fantasma."

        mc envergonhado "Não é nada. Só não achei que ia ver você aqui."

        w "Será que isso é verdade?"

        mc "Como assim? Claro que é haha..."

        show sofia falando with dissolve

        w "Eu sei que você esteve aqui outras noites e me viu ali sentada..."

        mc "Ah! Isso... bem... é que..."

        show sofia rindo with dissolve

        w "Não precisa ficar tão nervoso, bocó."

        mc desconfiado "Como?"

        w "Desculpa, falei sem querer."

        w "Eu... não vim aqui hoje pra chorar. Eu vim pra agradecer você."

        mc "Eu?"

        w "Obrigada por ter deixado eu sozinha. Eu vi que você queria vir falar comigo. Me ajudar."

        w "Mas você acreditou em mim. Não sei por que, mas você sabia que eu ia aguentar e não disse nada."

        w "E não foi uma. Eu vi você pelo menos duas vezes."

        mc envergonhado "Não ache que eu sou um perseguidor..."

        w "Haha. Não. Eu sei que você estava preocupado comigo. Obrigada mesmo."

        "Você tava errada [j]. A garota tem fibra."

        mc charmoso "Relaxa. Só queria ter certeza que você tava bem."

        show sofia seria with dissolve

        w "É... será que você podia sentar um pouco comigo aqui? Coisa rápida."

        mc normal "Claro."

        jump sofia_e1_climax

    menu:
        "Ela precisa de ajuda. Vou chamar ela":


            jump sofia_e1_climax
        "Ela pode resolver isso sozinha. Vou dar o fora":


            $ sofia_e1_confiou += 1
            $ dia_sofia = dia + 1

            "Não tenho que me meter nas coisas dela. Ela é adulta e eu não acredito na [j]. Eu não acho que ela desistiu."

            "Tô confiando na sua força, [w]. Você vai conseguir."

            jump call_cidade

label sofia_e1_climax:

    if not sofia_confiou:

        "Não posso deixar ela sozinha nessa situação. Isso não é certo."

        "Eu tava confiando que ela ia se virar, mas obviamente ela tá despedaçada a coitada."

        w "..."

        "E agora? O que eu falo pra ela?"

        mc preocupado "[w]..."

        w "Ah?"

        scene trabalho lounge with vpunch

        w "É..."

        show sofia chorando with dissolve

        pause

        w "É você, né, [mc]?"

        mc desculpa "Sim. Tá tudo legal?"

        w "{i}hic{/i}"

        w "Claro. Só me dá um segundo."

        w "Eu vou usar o banheiro aqui só um segundo."

        mc "Tá..."

        hide sofia with dissolve

        "Caraca, que barra, mano."

        "Ela tava chorando muito..."

        "..."

        show sofia falando with dissolve

        w "Pronto. Vamos?"

        mc desculpa "Vamos? Como assim 'vamos'?"

        show sofia seria with dissolve

        w "Quê?"

        mc "Você não tá legal, [w]. Você precisa conversar."

        w "Cala a boca, [mc]. Quem você acha que é?"

        mc serio "Quanto tempo você pretende fingir que tá tudo sob controle?! Você tava se acabando de chorar até agora!"

        w "Você! O que você!!"

        "Será que eu exagerei?"

        w "..."

        show sofia chorando with dissolve

        w "Droga, [mc]... Deixa eu... eu consigo..."

        mc "[w]... Senta aqui. Me fala..."

        w "..."

        hide sofia with dissolve

    mc preocupado "Vou acender a luz."

    w "Tá."

    scene sofia mc_conversando with Dissolve(3.0)

    pause

    w "..."

    mc "..."

    w "Desculpa... eu não sei o que falar."

    mc "Tudo bem."

    w "Tipo..."

    w "Por que você tá fazendo isso? A gente nem se conhece."

    mc "Não tô fazendo nada."

    w "Você tá se importando. O que eu tenho a ver com você?"

    mc "Você é minha companheira de trabalho."

    w "E daí?"

    mc "Sei lá. Não sei por que, tá bom? Eu só... vi você se complicando na redação e queria fazer alguma coisa."

    w "Isso não existe, [mc]. Ninguém faz nada pelos outros assim. Fala a verdade."

    mc "Tô falando. O que eu ia querer?"

    w "Sei lá. Quer ganhar mais dinheiro, quer... transar comigo..."

    menu:
        "Não é nada disso.":


            $ sofia_amizade += 1

            mc "Não é nada disso, [w]. Eu juro pra você que nada disso passou pela minha cabeça."

            mc "Sei lá. Você é bonita, e vai ser a nova chefe... Não posso ter certeza do que eu pensei."

            mc "Mas eu juro que se eu pensei algo assim, não foi consciente. Eu não tô aqui por isso agora."

            w "..."

            w "Eu acredito em você. Isso que é o pior."

            mc "Obrigado."
        "Transar com você com certeza seria uma boa. Você é linda.":


            mc "Eu não tô aqui por isso agora. Mas você é uma mulher linda. Transar com você não seria ruim, não."

            w "Você... você é tão 'normal', [mc]. Mas mesmo assim..."

            w "Ai ai..."

    w "Não sei o que fazer..."

    mc "Olha. Não precisa confiar em mim cem porcento. A gente nem se conhece. Só que escuta uma dica."

    mc "Você tá indo longe demais. Você tá querendo empurrar uma pedra quadrada."

    w "Como assim?"

    mc "Pensa. A redação é de um jeito há anos. Você quer mover tudo isso sozinha de uma hora pra outra."

    mc "As pessoas são cabeça dura. Ainda mais gente igual o chefe e a [j]. Não adianta querer mover eles assim."

    w "Agora entendi. Você tá falando que eu tenho que transformar a pedra quadrada numa roda antes de empurrar."

    mc "Isso!"

    w "Ha! Haha!"

    mc "Ei! É sério!"

    w "Desculpa... foi, tão espontâneo..."

    mc "Me deixa..."

    w "Obrigada pela dica. Acho você meio mole, mas talvez você tenha um pouco de razão. Mas só um pouco..."

    mc "Claro que eu tenho."

    if premium:

        p rindo "Você tem que ter 1 ponto de massagem aqui pelo menos. Avance na história da Karli para ver cenas extras com a Sofia."

    if mc_massagem >= 1:

        mc "E eu posso fazer algo mais por você ainda."

        mc "Uma massagem. Acho que você tá precisando disso. Dar uma suavizada no seu corpo."

        $ renpy.notify("Sofia está avaliando sua proposta...")

        w "Uma massagem? E você sabe fazer massagens?"

        mc "Sim. Eu tô fazendo um curso."

        w "Hmmm..."

        if premium:

            p rindo "Conseguir fazer massagem na Sofia exige que você tenha acertado praticamente todas as respostas. É bem difícil."

            p rindo "Mas jogadores PREMIUM podem pular essa necessidade. É uma colher de chá para nossos incríveis apoiadores!"

            p "Se você vai usar minha ajudinha ou não, é escolha sua."

            menu:
                "Usar ajuda da Pixie pra massagear":


                    $ sofia_amizade = 7

                    show white with dissolve

                    hide white with dissolve

                    p "Prontinho! Pode curtir agora, garotão!"
                "Deixar as coisas acontecerem naturalmente.":


                    p "Não precisa da minha ajuda? Já consigo ver você voltando em 2 segundos."

        if sofia_amizade >= 7:

            $ sofia_e1_massageou = True

            w "Deixa eu pensar..."

            $ renpy.notify("Sofia confia em você o suficiente")

            w "Ok... mas sem gracinha, ouviu? E só no pé. E pé é pé! No máximo canela!"

            w "Se você-"

            mc "Ok, ok... Tô fazendo isso pra você relaxar, e não ficar mais nervosa. Pode deitar e se ajeitar."

            w "Tá."

            mc "Agora tira o sapato e..."

            scene sofia mc_massagem with Dissolve(2.0)

            pause

            w "Hmmm..."

            mc "Tá vendo? Um pouco de pressão nos lugares certos e você vai se sentir muito bem."

            w "Tá gostoso mesmo."

            w "Ai!"

            mc "Que foi? Machuquei você?"

            w "Não. Foi só um negócio estranho que subiu."

            mc "Ok..."

            w "Tá gostoso. Pode continuar."

            mc "A senhorita que manda."



            w "Hmm..."

            scene sofia1_new1 with Dissolve(1.0)

            pause

            "Olha eu massageando a 'chefinha'... Dá pra acreditar que ela ia aceitar uma coisa dessas?"

            "E parece que ela tá curtindo mesmo..."

            "!"

            "Ela tá tão focada na massagem que nem percebeu a blusa dela..."

            "E-eu consigo ver... minha nossa..."

            "Eu devia avisar ela. Sim, com certeza eu devia. Seria o certo. Todo mundo sabe disso."

            "Mas... t-talvez fosse minha chance de tentar uma sacanagem com ela..."

            label so1_premium1:

                "O q-que eu tô pensando?! Agora que eu tive minha chance vou jogar tudo pela janela só pra dar uma olhadinha nela sem roupa?!"

            menu:
                "Claro que não!":


                    "D-de jeito nenhum!"

                    "Vou focar na massagem... que eu já vi o suficiente pra hoje."

                    "São nesses momentos que a gente mostra nosso caráter. E eu sou um homem de caráter."
                "Eu não consigo resistir! Me perdoa!":








                    "Eu acho que se eu mexer um pouco na calça dela... e puxar um pouquinho..."

                    "Ela nem vai perceber... e daí..."

                    "... daí..."

                    scene black with dissolve

                    scene sofia1_premium1 with Dissolve(1.0)

                    pause

                    "Funcionou! E ela nem percebeu!"

                    "Que peitinho mais gostoso que ela tem. É tão redondinho e bem durinho."

                    "Como eu queria poder apertar eles agora... e chupar esse biquinho..."

                    "Hmm... Tô ficando duro só de pensar..."

                    "E ela nem aí. Se ela soubesse que tem um tarado pervertido pegando nela..."

                    "Se ela descobrisse... eu nunca mais ia poder encostar nela."

                    w "Hmm... tudo bem se eu relaxar demais e..."

                    mc "T-tudo bem. É normal."

                    w "Que bom... eu tô tão cansada esses tempos..."

                    "Perfeito! Se ela dormir... eu termino aqui e saio de fininho e ela nunca vai descobrir..."
                    scene sonew_ani02 with Dissolve(1.0)
                    "Só tenho que ficar quieto... e aproveitar a vista..."

                    "Hmm... se eu conseguisse abaixar um pouco mais a calça dela..."

                    "Eu daria tudo pra ver o meio das pernas dela... deve ser tão bonitinha.. ah..."

                    w "Ahnn..."

                    "Ela parece bem relaxada... talvez..."

                    menu:
                        "Puxar mais a calça dela":


                            "Por que o ser humano nunca se contenta com o que tem?"

                            "Mas quando eu vou ter outra chance igual essa? Eu tenho que aproveitar."

                            "Só vou puxar um pouquinho..."

                            "Puxar um pouquinho..."

                            w "Hm? O que é isso que eu tô sentindo pux-{nw}"

                            scene sofia1_premium2 with vpunch

                            w "QUÊ??!!!"

                            mc "Q-que foi?!"

                            w "Minha roupa!!!"

                            mc "Minha nossa! E-eu tava olhando pro seu pé e-"

                            w "Então para de olhar agora!"

                            mc "C-claro!"

                            w "Que vergonha!"

                            scene black with vpunch

                            "Agora fodeu!"

                            mc "D-desculpa! Eu prome-"

                            w "Não precisa se desculpar... a culpa não foi sua..."

                            "Se ela soubesse..."

                            w "Pode abrir os olhos..."

                            mc "Opa..."
                        "Desistir da ideia e arrumar a roupa":


                            "Nah... eu vou só continuar assim..."

                            "..."

                            w "{i}zzzzz{/i}"

                            "Parece que ela capotou mesmo. Vou aproveitar pra ajeitar aqui."

                            scene black with dissolve

                            mc "Pronto."

                    scene sofia1_new2 with Dissolve(1.0)

                    w "Eu acabei dormindo, né?"

                    w "Esses dias não tão sendo fáceis... eu praticamente não tô dormindo nada."

                    mc "Tá bem puxado pra você mesmo aqui a redação."

                    w "Tomara que seja só o começo. Eu acho que as coisas devem se resolver com o tempo..."

                    mc "Tomara..."

                    w "É tanto cansaço que quando eu fico um pouco deitada eu capoto... e daí pra eu acordar..."

                    mc "Sério?"

                    w "Pode cair o mundo que eu não levanto. Parece que eu tomei remédio pra dormir, sabe?"

                    mc "Nossa..."

                    "Essa é uma boa informação pra eu saber... talvez eu possa usar isso ao meu favor..."

                    w "Além de que eu tô com tanta coisa na cabeça que eu fico avoada. Nem percebo as coisas."

                    w "Eu nem percebi que... né..."

                    mc "Haha..."

                    w "Só ficar deitada assim... hmmm..."

            window hide

            pause

            mc "Sofia?"
        else:


            w "Bem..."

            w "Você já fez muito por mim. Obrigada pelo convite. Talvez outro dia."

            mc "Você quem sabe."

            w "Agora..."
    else:


        "Se eu soubesse fazer massagens, talvez eu pudesse ofecer pra ela agora..."

    if premium and not sofia_confiou:

        p rindo "A próxima cena depende de ter feito algo específico antes. E você não fez, infelizmente."

        p "Como você é premium, eu posso liberar para você."

        menu:
            "Sim. Por favor.":


                p "Opa."

                show white with dissolve

                hide white with dissolve

                p "Prontinho. Bom jogo!"
            "Não. Eu não mereço.":


                p "Pare de ser bobo. Mas que seja."

    if sofia_confiou:

        w "Ah? Acho que eu preciso só ficar um pouco deitada."

        mc "Relaxa."

        w "Você... eu confio em você, [mc]..."

        w "Seria pedir demais, se você ficasse de olho, só um pouco?"

        mc "Tudo bem."

        w "Obriga... da..."

        scene black with dissolve

        scene sofia redacao_dormindo with Dissolve(1.0)

        pause

        w "{size=17}Só ficar de olho...{/size}"

        w "{size=17}Vou só fechar os olhos... um pouco...{/size}"

        w "{size=17}{i}zzzzz{/i}{/size}"

        mc "Dormiu..."

        w "{size=17}Você...{/size}"

        w "{size=17}você é meu melhor amigo, [mc]...{/size}"

        mc normal "..."

        "Melhor amigo... Bom... não tenho certeza se eu quero ser só um amigo."

        "Mas acho que {b}melhor{/b} amigo é um bom começo."



        w "Mmm..."

        "E aquela história que ela não acorda de jeito nenhum?"

        menu:
            "Vou testar. (+18)":


                mc "Sofia..."

                w "{size=17}{i}zzzzz{/i}{/size}"

                mc "SOFIA!!!"

                scene sofia redacao_dormindo with vpunch

                pause 1.0

                w "{size=17}{i}zZzZz{/i}{/size}"

                mc "Ela falou a verdade... não acorda de jeito nenhum..."

                label so1_premium2:

                    "Eu tô protegendo o sono dela dos outros... mas... quem vai proteger ela de MIM?"

                    "Não... eu não caí baixo desse jeito, caí? Fazer isso com alguém é até crime..."

                menu:
                    "Eu não vou abusar de uma mulher dormindo!":


                        "Eu nunca vou fazer isso! Isso é até crime!"

                        "Só de isso ter passado pela minha cabeça eu devia ter vergonha..."
                    "Só uma olhadinha...":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_34

                            jump so1_premium2

                        "Como eu queria ter força de vontade pra aguentar isso, [w]..."

                        "Arriscar meu trabalho aqui e minha vida só pra poder ver esse seu corpinho maravilhoso..."

                        "Bom... eu já me certifiquei que nem gritando tudo acorda. Deve ser seguro..."

                        "Vamos começar colocando isso aqui um pouquinho pro lado..."

                        scene black with dissolve

                        scene sofia1_premium4 with Dissolve(1.0)

                        pause

                        "Que beleza."

                        "Esse peito arrebitadinho... isso é bem raro, Sofia... você tem um corpo incrível."

                        "E você ainda fica vindo sem sutiã pro trabalho... você tá provocando, né?"

                        "Como se ninguém fosse fazer nada com você porque você é pedreira."

                        "Mas dormindo... eu posso fazer o que eu quiser..."

                        mc "Agora, licença que eu só vou dar uma olhadinha desse lado aqui também..."

                        scene sofia1_premium5 with Dissolve(1.0)

                        pause

                        mc "Hmm..."

                        "Sua pele é incrível... e você cheira tão bem..."

                        "Quem dera eu conseguisse impressionar você a gente ficar junto."
                        scene sonew_ani01 with Dissolve(1.0)
                        "Mas você só fala de trabalho, trabalho..."

                        "Será que você não tem outras vontades, não?"

                        "Eu tenho coragem de pegar em você assim, mas se a gente namorar... hmm..."

                        "Deixa eu ver você melhor."

                        scene sofia1_premium6 with Dissolve(1.0)

                        pause

                        mc "Uau..."

                        "Olha daquí eles parecem ainda mais gigantes..."

                        "Eu nunca vou esquecer como você é gostosa."

                        "Tem gente que realmente é abençoada. Essa cinturinha e um peitão. Aposto que qualquer cara ia adorar ficar contigo."
                        scene sonew_ani03 with Dissolve(1.0)
                        "E o pior é que você não deve ficar com ninguém."

                        "O mundo é uma grande ironia mesmo."

                        "Ok... chega de babar pros seus peitos. Deixa eu ver o resto..."

                        scene black with dissolve

                        scene sofia1_premium7 with Dissolve(1.0)

                        pause

                        mc "Isso que é corpo."

                        "Agora... falta um lugar..."

                        "Acho que é demais... é perigoso ela acordar e eu foder com tudo por causa de taradisse!"

                        "Melhor eu arrumar a camiseta dela e parar enquanto eu tô por cima."

                        "Mas..."

                        menu:
                            "Tirar a calcinha dela":


                                "Só mais uma olhadinha, Sofia... o lugar mais interessante..."

                                "Eu tenho que ter muito cuidado agora... é um lugar muito delicado."

                                mc "Opa..."

                                scene black with dissolve

                                scene sofia1_premium8 with Dissolve(1.0)

                                pause

                                w "Shria shrumm..."

                                mc "!!!"

                                w "{size=17}{i}zzzzz{/i}{/size}"

                                mc "Ufa..."

                                "Quer me matar do coração?!"

                                "Tá quase lá, [mc]... só mais um tantinho..."

                                scene sofia1_premium9 with Dissolve(1.0)

                                pause

                                mc "A-ah..."

                                "Que delícia..."

                                "Como eu queria poder te dar muito prazer."

                                "Será que eu vou ser o primeiro? A Sofia não tem jeito que fica saindo por aí."

                                "Imagina ser o primeiro a visitar esse lugar tão especial?"

                                "Eu tô babando só de pensar entrar aí. Eu faço o que você quiser, Sofia."

                                "Só deixa mexer na sua bucetinha..."

                                w "Shuria shrummam...{nw}"

                                scene sofia1_premium10 with vpunch

                                pause

                                mc "AAARGFHGHH!!"

                                mc "S-S-S-SOFIA!!!"

                                mc "E-eu! P-por favor! E-eu---"

                                w "Shuria shrummam..."

                                mc "...?"

                                w "{size=17}{i}zzzzz{/i}{/size}"

                                "Você continua dormindo?!"

                                "Quase eu infartei agora... ela realmente tá dormindo de olho aberto?"

                                scene sofia1_premium9 with Dissolve(1.0)

                                "Nem consigo mais prestar atenção nessa belezinha... caralho... quase morri..."

                                "M-melhor eu parar aqui antes que dê uma mega merda."

                                "Só deixa eu dar uma última olhada no material. Você merece o risco."

                                scene black with dissolve

                                scene sofia1_premium11 with Dissolve(1.0)

                                pause

                                mc "Olha só pra isso..."

                                "Se eu for um cara decente e parar de fazer essas coisas, talvez um dia eu possa curtir você de verdade."

                                "Esse negócio de massagem pode dar muito certo..."

                                "A Sofia é um pitel de verdade. Além de ser uma garota centrada e eficiente."
                                scene sonew_ani06 with Dissolve(1.0)
                                "Namorar com alguém com você ia ser um sonho."

                                "Hmm..."

                                "Eu não vejo a hora de fazer taradisses de verdade com você. E a gente vai se divertir muito..."

                                "M-melhor eu arrumar ela agora."
                            "Arrumar ela e sair":


                                mc "M-melhor eu parar por aqui."

                                "Eu não quero nem ver a merda que vai dar se ela me pegar."

                                "Ser demitido vai ser o menor dos meus problemas."
            "Deixa a coitada dormir.":


                "Eu não vou tirar sarro da coitada."

        scene black with Dissolve(1.0)

        "Pode dormir tranquila, [w]. Eu tô aqui."

        "..."

        $ dia += 1
        $ tempo = 1

        play sound "audio/som_4_fadolandia.mp3"

        scene sofia1_new2 with Dissolve(1.0)

        w "Uaahhh...."

        w "Ah? Onde eu tô?!"

        scene black with dissolve

        scene trabalho lounge with Dissolve(1.0)

        show sofia rindo with dissolve

        mc concentrando "{i}zzzz{/i}"

        w "Não acredito que ele ficou comigo esse tempo todo..."

        w "Será que realmente existem pessoas assim? Que fazem as coisas pelos outros sem querer nada em troca?"

        w "Incrível..."

        hide sofia with dissolve

        w "[mc]... [mc]... Oi..."

        mc normal "Ha?"

        mc desconfiado "Eu dormi?"

        show sofia rindo with dissolve

        w "Só um pouco. Obrigada por ter ficado comigo. Vamos pra casa?"

        mc concentrando "Vamos... tô precisando..."

        w "Eu te ajudo."

        mc "Valeu..."

        $ sofia_e1 = "true"
    else:


        w "Obrigada por tudo. Nem acredito que eu falei tudo isso pra você."

        mc "Relaxa. Nada mudou. As coisas vão continuar do mesmo jeito entre a gente."

        w "Isso é bom."

        w "Tô cansada. Vamos pra casa?"

        mc normal "Claro."

        $ sofia_e1 = "normal"
        $ tempo += 1

    scene black with Dissolve(1.0)

    "..."

    "A [w] é uma pessoa boa. Eu tenho certeza disso agora."

    "Uma pessoa que coloca os valores acima de tudo. Uma pessoa como poucas existem aqui na cidade."

    "E até por causa disso ela acaba sentindo todo o peso. O peso de quem não escolheu o caminho fácil."

    "Tomara que eu possa ajudar ela a transformar a revista e quem sabe até mais que isso."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v15_fim","sofia","personagem")

    $ sofia_e1_count = 3
    $ v15_fim = True

    jump call_cidade

label sofia_e1_evento:

    if sofia_e1_count == 0:

        $ sofia_evento_manha = True

        scene trabalho geral with Dissolve(1.0)

        "Vou dar uma lida no que o resto do pessoal tá escrevendo. Talvez um pouco de inspiração me ajude a conseguir mais pautas."

        w "Não! Eu entendo que você tem tempo de casa. Mas isso não justifica nada."

        j "Meu bem, você não manda nada aqui."

        mc desconfiado "Hm? Que tá rolando?"

        scene trabalho angulo with Dissolve(1.0)

        show sofia seria with dissolve

        w "Primeiro que você escreve poucas matérias. Só nisso dá pra ver que a coisa tá errada."

        show sofia seria at esquerda with move

        show cassia provocando with dissolve

        j "Olha minha cara de quem liga pra sua opinião sobre meu trabalho."

        show cassia provocando at direita with move

        w "Você se acha toda poderosa, mas você é uma funcionária como todos os outros. As regras valem para todos."

        j "Regras? Quais regras? Só existe uma regra aqui, querida: {b}vender exemplares{/b}."

        j "Enquanto minhas matérias fizerem a revista vender, eu tô fazendo meu trabalho. E agora dá licença que eu tenho mais o que fazer."

        hide cassia with moveoutleft

        w "Ai!"

        w "Cretina..."

        hide sofia with dissolve

        "Ixi. Essa [w] chegou mexendo com tudo que é tubarão aqui na redação."

        "Mas ela é durona também. Se tem alguém que vai conseguir mexer nesse vespeiro é alguém igual ela."

        "..."

    elif sofia_e1_count == 1:

        $ sofia_evento_manha = True

        scene trabalho geral with Dissolve(1.0)

        "Mais um dia de trabalho."

        w "Não! Você tá sendo conivente com tudo isso!"

        mc zerado "Parece que todo dia agora é essa mina gritando..."

        "..."

        scene sofia brigando_chefe with Dissolve(2.0)

        w "Você me chamou aqui pra executar uma tarefa. Mas eu preciso de autoridade pra fazer!"

        b "Isso foi um erro. Você não tá pronta ainda."

        w "Como assim? Eu estudei e fiz estágio em uma das principais redações do mundo! Como pode falar isso?!"

        b "Você pode saber tudo sobre redação, mas você não sabe nada da vida, fedelha."

        b "E não me irrite mais. Faça qualquer coisa que quiser."

        w "Pai!"

        scene trabalho chefe_porta with Dissolve(1.0)

        "Deixou ela falando sozinha."

        show sofia invocada with dissolve

        w "Velho insuportável. Você não vai me ajudar? Foda-se."

        "Acho que ela nunca ficou tão-"

        scene trabalho angulo with hpunch

        mc angustiado "Ai!"

        show sofia seria with dissolve

        w "E você? Tá fazendo o que aqui?"

        mc envergonhado "Só tava indo na cozinha tomar algo."

        w "Ok. Licença."

        hide sofia with dissolve

        mc "Toda..."

        "..."

    elif sofia_e1_count == 2:

        $ sofia_evento_manha = True

        scene trabalho geral with Dissolve(1.0)

        "Qual quer vai ser a confusão hoje?"

        w "Não! Eu mandei você cuidar da pauta da cantora!"

        w "Você! Você é burro?!"

        "Como que ela consegue brigar com todo mundo?"

        scene trabalho angulo with Dissolve(1.0)

        show sofia explicando with dissolve

        w "Eu já falei isso três vezes pra você! Ei! Olha aqui!"

        w "Gente, é muito simples. Só sigam o diagrama que eu mandei pelo e-mail corporativo."

        w "Gente?! Vocês tão me ouvindo?!"

        menu:
            "...":


                "..."

                w "..."

                w "Desisto..."
            "Eu tô ouvindo.":


                $ sofia_amizade += 1

                mc normal "Eu tô te ouvindo."

                w "..."

                show sofia meudeus with dissolve

                w "Ai ai..."

        w "Tudo bem. Estão todos liberados."

        hide sofia with dissolve

        "Realmente, eu sinto que essa mina tá se afundando a cada dia."

        "Se eu pudesse fazer alguma coisa pra ajudar ela. Mas ela nem me ouve."

        mc desculpa "Droga..."

    return

label trabalho_sofia:

    "Falar com ela sempre me dá calafrios."

    scene trabalho sofia with Dissolve(1.0)

    if tempo == 1:

        mc normal "Bom dia."

    elif tempo == 2:

        mc normal "Boa tarde."

    if sofia_e1_count == 0:

        w "Você. Ai ai... O que foi?"

        "Ixi, dá pra ver que ela tá com a macaca... A briga com a [j] deve ter deixado ela invocada."

        "E o pior é que ela vai redirecionar tudo isso pra mim. Vou ter que ser esperto se eu quiser sair por cima dessa."

        menu:
            "Não liga pra [j].":


                mc desculpa "Não liga pra [j]. Ela é assim mesmo."

                w "Como não vou ligar? Ela é uma peça importante pra revista, mas isso não dá direito dela..."

                w "Quer saber? Deixa pra lá."
            "O que acha de comer algo pra dar um tempo?":


                mc normal "E se a gente comer alguma coisa pra dar uma acalmada?"

                w "De novo esse papo? Vai você se acalmar. Eu preciso trabalhar."

                mc desculpa "Ok, malz."
            "A [j] já me ferrou também.":


                $ sofia_amizade += 1

                mc serio "A [j] já me ferrou também."

                w "Sério?"

                mc "Sim. Ela me chantageou com uma matéria sobre eu e a [c]."

                w "Essa mulher é terrível..."

        w "Mas o que você quer? Não tem coisa pra fazer?"

        mc desculpa "Só queria saber se você tava legal mesmo depois da discussão. Você ainda é nova aqui..."

        w "..."

        w "Olha, [mc]. É [mc], né?"

        mc "Isso."

        w "Dá uma licença."

        mc envergonhado "Opa."

        scene trabalho angulo with Dissolve(1.0)

        show sofia falando with dissolve

        w "Não precisa se preocupar comigo. Eu treinei bastante antes de vir pra cá. Eu tenho condições de gerenciar essa redação."

        "Gerenciar? Caraca..."

        w "Eu voltei a pedido do meu pai pra virar {b}Coordenadora de Produção{/b} da revista."

        w "Até agora meu pai tem feito o trabalho de gerência sozinho, como {b}Editor Chefe{/b}, mas ele precisa de alguém que acompanhe o dia a dia."

        w "Eu tenho capacidade pra isso. Ou você acha que eu não tenho? Talvez por que eu seja mulher ou por que eu sou nova. Hã?"

        "Calma, mina. Ela tá putassa."

        menu:
            "Claro que você tem. Dá pra ver na sua cara.":


                mc envergonhado "Claro que você tem. Dá pra ver pelo seu jeito."

                w "Ai ai... ok."

                w "Obrigada, mas... Bom. Com licença. Tenho que correr com um negócio aqui."

                mc "Até."
            "...":


                mc desculpa "..."

                show sofia seria with dissolve

                w "Tá certo..."

                w "Agora dá licença que eu tenho o que fazer."
            "Não é isso. Só acho que você tá pegando pesado demais.":


                $ sofia_amizade += 1

                mc desculpa "Não tem nada a ver com capacidade. Só acho que você tá pegando pesado demais logo no começo."

                show sofia seria with dissolve

                w "Sério mesmo que você vai querer..."

                w "Quer saber? Tenho mais o que fazer."

        hide sofia with dissolve

        "..."

        "Não tem como..."

        scene trabalho mesa with Dissolve(1.0)

        "Parece que nada o que eu falo dá certo. Essa mina é geniosa pra caramba."

        "Melhor eu não forçar a barra por enquanto."

        $ sofia_e1_count = 1
        $ sofia_evento_manha = False
        $ dia_sofia = dia + 1
        $ tempo += 1

        jump call_cidade

    elif sofia_e1_count == 1:

        mc envergonhado "Sou eu de novo."

        w "O que é dessa vez? Não está vendo que eu estou ocupada?"

        menu:
            "Você precisa relaxar um pouco.":


                $ sofia_amizade += 1

                mc desculpa "Calma. Você tá muito pilhada. Precisa relaxar um pouco. Pegar mais leve com as coisas."

                w "Não acredito que você tá falando isso pra mim."

                w "Eu sei o que eu tô fazendo! Agora sai daqui!"
            "Queria saber se você tá precisando de algo.":


                mc normal "Só queria saber se você tá precisando de alguma coisa. Posso te ajudar com algo?"

                w "O que isso quer dizer?"

                mc envergonhado "Nada de mais. É que você chegou agora e..."

                w "O que isso importa?! Eu não preciso de nada! Agora cai fora!"
            "Hoje acho que você tem que beber algo comigo.":


                mc charmoso "Você tá estressada demais. O que acha de beber alguma coisa hoje?"

                w "{i}Grrrr{/i}"

                w "Todo dia a mesma coisa?! Não vou beber com você! Sai daqui!"

        scene trabalho angulo with vpunch

        "Eita!"

        "Agora eu ferrei tudo."

        j "Ei! [mc]! Vem aqui."

        mc zerado "[j]..."

        "Deixa eu ver o que ela quer."

        scene cassia sentada_rindo with Dissolve(1.0)

        j "Tá apanhando também?"

        mc envergonhado "Pois é..."

        j "Você também não pode ver um par de peitos que quer se meter no meio."

        mc "Não é nada disso..."

        j "Não te culpo. A garota tem umas olheiras, mas é bem ajeitada. Além de ser novinha."

        mc zerado "[j]..."

        scene cassia sentada_explicando with dissolve

        j "Mas a chefinha tá com os dias contados."

        mc desconfiado "Como assim?"

        j "Ela não vai aguentar o tranco. Vai por mim."

        mc desculpa "Ela parece ser bem resiliente."

        j "Por fora bela viola..."

        mc "Sei lá..."

        j "Não deixe sua paixonite te cegar, pombinho. Essa garota não tem o que é preciso. Pode acreditar em mim."

        mc "Vamos ver..."

        if cassia_seducao:

            scene cassia sentada_provocando with dissolve

            j "E não vai esquecer de mim."

            mc safado "Claro que não."

            j "Vem me encontrar um dia de noite aqui. O que acha?"

            mc "Pode deixar. Dou uma passada."

            j "Combinado."

        "Não sei se eu concordo com a [j]. A [w] parece durona. Encarar o chefe não é pra qualquer um."

        "Se pá ela só tá com inveja da menina."

        $ sofia_e1_count = 2
        $ sofia_evento_manha = False
        $ dia_sofia = dia + 1
        $ tempo += 1

        jump call_cidade

    elif sofia_e1_count == 2:

        mc envergonhado "E aí?"

        w "[mc], eu tô realmente ocupada hoje, tá? Por favor."

        mc "Ok... Mas qualquer coisa me fala, tá?"

        w "Tá."

        "Parece que ela se fechou de verdade agora. Tô realmente preocupado."

        "Ela costuma trabalhar até de noite. Quem sabe eu não devesse dar uma olhada nela depois."

        jump cenario_trabalho

    elif sofia_e1_count == 3:

        w "O que foi, [mc]?"

        "Achei que depois da outra noite ela ia me tratar melhor. Mas tá com a mesma cara de cú..."

        w "Estou terminando o cronograma da próxima edição. Continue trazendo boas pautas, ok?"

        mc envergonhado "Pode deixar. Estou correndo atrás delas."

        w "Assim que se fala. Aliás, eu tava pensando numa coisa."

        w "O que você acha de trabalhar como meu assistente?"

        mc desconfiado "Como assim?"

        w "A carga de trabalho tá bem intensa e eu poderia contar com uma ajuda."

        w "Depois daquela noite percebi que posso contar com você. O que me diz?"

        mc envergonhado "Bom, acho que pode ser."

        $ sofia_e1_count += 1

        jump sofia_evento2















        jump cenario_trabalho

    elif sofia_e1_count == 4:

        if tempo < 2 and dia >= sofia_dia and sofia_xp < 35:

            jump sofia_minigame

        elif sofia_xp >= 35:

            w "As coisas estão melhorando na redação, [mc]."

            w "Todo nosso trabalho essas semanas tá surtindo efeito."

            w "As pessoas estão melhorando a redação e as matérias estão bem menos sensacionalistas."

            w "Vou dar um tempo agora na correção e ver se elas conseguem fazer por elas mesmas."

            w "Não vou mais precisar do seu trabalho por um tempo. Eu agradeço de verdade tudo o que você fez."

            w "Vou pensar aqui o que podemos fazer em seguida. O próximo passo é conseguir mais leitores."

            w "Assim que eu definir o que eu vou fazer eu te aviso tá?"

            mc "Beleza. Boa sorte, [w]. Qualquer coisa tô sempre por aqui."

            w "Pode deixar. Obrigada, parceiro."

            $ dia_sofia = dia + 1

            jump cenario_trabalho
        else:


            w "Agora já é tarde demais. Comecei a fazer tudo sozinha."

            w "Venha amanhã cedo se quiser ajudar de verdade."

            mc "Ok..."

            jump cenario_trabalho

label sofia_trabalho_evento1:

    w "Ah! Antes disso."

    scene sofia_mc_conversando1 with Dissolve(1.0)

    w "Eu- é..."

    w "Só queria te agradecer pelo trabalho que você vem fazendo."

    mc "Não foi nada. Foram apenas alguns dias."

    w "Não. Você tá fazendo um excelente trabalho. Com muita competência."

    mc "Ah. Valeu."

    menu:
        "Eu mereço que você tome um café comigo então.":


            mc "Então, já que eu tô fazendo meu trabalho direito, você poderia tomar um café comigo."

            w "E-e-eu... Eu sei. Mas é que- que..."

            mc "Calma. Tá tudo legal. A gente não precisa tomar café agora. Vamos continuar o trabalho."

            w "T-tá."
        "Eu tô fazendo isso porque eu quero a redação melhor.":


            $ sofia_amizade += 1

            mc "Eu também quero ver a revista cada vez melhor. Por isso que eu quero te ajudar."

            mc "Pra mim, você é a pessoa certa pra levar nossa revista pra um novo nível."

            w "Ah!"

    w "O-obrigada... é... [mc]..."

    mc "Por que parece que é difícil você falar meu nome?"

    w "Ah! Não! É só que..."

    mc "Hm?"

    w "Não é nada. A gente tem que trabalhar!"

    mc "Você não vai responder direito?"

    w "Pe-pensando melhor a gente devia tirar o dia de descanso! Muito obrigada por tudo!"

    w "Tchau!"

    scene trabalho angulo with vpunch

    "Eita..."

    "Bom. Pelo menos vou ter meu dia de folga."

    "Desde que ela chegou na redação, a [w] está tentando fazer as coisas diferentes."

    "O começo foi bem complicado, mas acho que agora tanto ela como os repórteres não estão mais causando tanto."

    "Mesmo perdendo o dia todo aqui, tá sendo legal conhecer todas essas matérias que as pessoas escrevem."

    "E quem sabe ganhando a confiança da [w], não pode até rolar algo entre a gente?"

    "O que eu tô pensando?! O negócio aqui é trabalho!"

    show black with dissolve

    p rindo "Parabéns! Agora a [w] confia mais em você! Continue ajudando na redação para desenvolver ainda mais sua relação com ela."

    p lecionando "Aliás... Fazendo tudo isso só por uma garota?"

    p rindo "Você já ouviu a expressão {b}Gado D+{/b}?"

    $ dia_sofia = dia + 1

    jump call_cidade

label sofia_trabalho_evento2:

    w "Hoje eu q-"

    "???" "Pombinhos. Têm um segundo?"

    mc desconfiado "Pombinhos?!"

    scene trabalho angulo with Dissolve(1.0)

    show cassia provocando with dissolve

    j "Calma, querido. Sou eu."

    j "Eu vim falar com a chefinha."

    show cassia at esquerda with move

    show sofia seria with dissolve

    w "[j]."

    show sofia at direita with move

    w "Eu já pedi pra não me chamar assim."

    j "Me pedem muitas coisas, e nem sempre eu faço."

    w "..."

    w "O que você quer?"

    j "Eu vi que você mexeu em uma matéria que eu escrevi."

    "Puta que pariu! Eu sabia que isso não ia dar certo!"

    if sofia2_cassia:

        "A [j] vai me comer vivo."
    else:


        "Sorte que eu não me meti nessa."

    show sofia falando with dissolve

    w "Estou fazendo isso com todos os repórteres."

    j "Eu não sou só uma 'repórter', querida. Eu sou A REPÓRTER. Ninguém edita minhas matérias."

    w "Isso não acontecia até agora. Mas agora vai começar a ser editada como todas as outras."

    j "A é? Você..."

    menu:

        "Fui eu quem editou sua matéria." if sofia2_cassia:

            $ sofia_amizade += 1

            mc desculpa "Na verdade, fui eu quem editou sua matéria, [j]."

            j "Você, pombinho?"

            mc "Eu sabia que você não ia gostar, mas a gente tava fazendo isso com todos."

            j "..."

            j "Depois passa na minha sala que eu vou ter uma conversinha com você."

            w "Ca-"

            mc "Tudo bem. Eu vou passar lá."

            j "Até mais."

            hide cassia with dissolve

            hide sofia with dissolve

            show sofia chorando with dissolve

            w "Você não precisava ter se intrometido."

            mc serio "Mas foi eu quem editou a matéria mesmo."

            w "Eu sei, mas sob minhas ordens."

            mc normal "Eu sou seu ajudante. Não posso te deixar na mão assim."

            w "... Obrigada."
        "...":


            j "Quer saber?"

            j "Eu não vou perder minha paciência com você, pombinha."

            j "Mas se isso voltar a acontecer, seu trabalho aqui na revista vai acabar muito antes do que você pensa."

            w "Eu não me intimido com essas suas ameaças."

            j "Vamos ver."

            hide cassia with dissolve

            show sofia meudeus with dissolve

            w "Ufa..."

            mc "..."

    scene sofia_mc_conversando1 with Dissolve(1.0)

    mc "A [j] é terrível."

    w "Mas ela é só uma profissional, como todos os outros aqui."

    mc "Não sei se é tão simples assim."

    w "Como assim?"

    mc "Depois de muitos anos trabalhando, se esforçando, as pessoas meio que conquistam um lugar, sabe?"

    mc "Eu sei que o que a [j] faz não tá certo. Ela me ferrou muito também."

    mc "Mas a gente não pode negar que ela tem muito tempo de casa. Ela conquistou isso com o trabalho dela também."

    w "E daí chega uma pessoa do nada e..."

    mc "..."

    w "Você acha que eu estou agindo errado?"

    menu:
        "Claro que não. Você tá certa.":


            mc "Cl-claro que não. Você só quer tratar todo mundo igual."

            w "Hmm..."

            w "É isso mesmo. Não quero fazer diferença entre todos que trabalham aqui."

            mc "E você tá certa nisso."
        "Acho que você tá sendo dura demais.":


            $ sofia_amizade += 1

            mc "Tô falando minha opinião aqui, tá?"

            w "Claro..."

            mc "Não acho errado que você tá fazendo, só que talvez você esteja pegando um pouco pesado demais."

            mc "Assim, com pessoas tipo a [j] que são prata da casa. Não tem porque mexer nesse vespeiro."

            "Por que eu tô defendendo a [j]? Eu vou me foder com a [w] por causa dela?"

    w "Sabe..."

    w "As coisas não estão fáceis pra mim. Fazer a coisa certa nem sempre é fácil."

    scene sofia_mc_conversando2 with Dissolve(1.0)

    w "Mas de todos aqui na redação, você é o único que consegue falar comigo."

    mc "Como assim consegue?"

    w "Não sei. A maioria das pessoas só troca uma ou duas palavras comigo."

    w "Os outros jornalistas nem olham nos meus olhos direito."

    w "Mas quando você fala comigo eu não sinto essa distância."

    w "Eu acho que você não me vê só como a 'chefinha' ou a chata que tá tornando a vida de todo mundo um inferno."

    mc "Claro que não... você só é... exigente. Mas não tem nada de errado nisso."

    w "Você acha que não tem?"

    mc "Claro que não."

    mc "Assim... eu acho que não tem tanto a ver com você essa reação das pessoas."

    mc "Elas não te odeiam."

    scene sofia_mc_conversando3 with Dissolve(1.0)

    pause

    w "Não?"

    mc "Não."

    w "Mas ent-"

    mc "Deixa eu ver se eu consigo explicar."

    mc "Muitas pessoas não gostam do trabalho. Tipo, muitas só trabalham pelo dinheiro e não por amor."

    mc "Elas queriam estar fazendo outras coisas da vida e acabaram nesse emprego por necessidade."

    mc "Só delas estarem aqui todos os dias, acordando cedo e vindo aqui cumprir as tarefas delas meio que elas já são tipo heróis."

    w "Eu amo trabalhar como jornalista. Seria horrível vir aqui se eu não gostasse..."

    mc "Isso mesmo."

    mc "E daí quando uma pessa aparece e começa a mudar o que elas aprenderam a aguentar, é óbvio que elas não vão curtir."

    mc "Elas só querem continuar fazendo o que elas se acostumaram pra ganhar o salário e poderem continuar com a vida delas."

    mc "Porque o coração delas não tá aqui na redação, mas em outros projetos, ou na família ou sei lá onde."

    w "Entendo..."

    mc "Então eu acho que elas não têm algo contra você, mas contra isso que você tá representando."

    mc "Que tá tornando o lugar que elas aprenderam a suportar em algo novo e pior, pois você quer que elas levem as coisas mais à sério."

    w "Eu acho que faz sentido..."

    w "Então o que eu faço?"

    mc "Eu acho que você poderia dar um tempo pra elas se acostumarem. E também mostrar pra elas que você não é só a nova chefe. Você é uma pessoa."

    w "Eu nunca tinha pensado por esse ângulo, [mc]..."

    mc "Às vezes é complicado a gente se colocar no lugar dos outros. Ainda mais você que é tão focada nas suas coisas."

    scene sofia_mc_conversando2 with Dissolve(1.0)

    w "Obrigada por ter paciência comigo."

    mc "Eu vou continuar te ajudando e vamos tornar a redação melhor. E sempre que precisar pode falar comigo, ok?"

    w "Tá..."

    w "Acho que hoje a gente podia tirar o dia de folga. Acho que eu preciso pensar nisso tudo."

    w "Querer fazer um bom trabalho e ter que lidar com as pessoas me estressa demais..."



    "Hmm... essa pode ser uma boa chance de eu tentar alguma coisa com a Sofia."

    "Acabei de dar uma dentro e ela tá meio vulnerável... será que vale arriscar?"

    menu:
        "O que você acha de uma massagem?":


            "Quem não chora não mama."

            mc "Dá pra ver mesmo que as coisas tão pesadas pra você."

            w "Dá, não dá?"

            mc "Você sabe que eu tenho a solução pra isso aí. Uma massagem rápida e resolve."

            w "Hmm..."

            w "Você lembra da outra vez o que aconteceu? Que vergonha..."

            mc "Relaxa. Eu nem vi nada. Mas o importante é que você relaxou de verdade aquela noite."

            w "É... isso você tem razão."

            mc "E aí? Vamo aproveitar que acabou o expediente e o vigia da noite ainda não chegou?"

            w "..."

            w "Tá bom. Mas coisa rápida! Eu não quero dormir aqui de novo. Você sabe como eu fico quando tô dormindo."

            mc "Eu sei muito bem... d-digo, vamos tomar cuidado pra não cair no sono."

            scene black with dissolve

            scene trabalho lounge with Dissolve(1.0)

            mc "Pode deitar e tirar o sapato."

            w "Ok."

            scene black with dissolve

            scene sofia1_new1 with Dissolve(1.0)

            pause

            w "Ah... é gostoso mesmo."

            mc "Agora fecha os olhos e curte... qualquer coisa eu te acordo."

            w "Você sabe que é impossível me acordar... eu tô com umas 1.423.567 horas de sono atrasadas."

            mc "Mas você sabe que eu te protejo."

            w "Ah... eu sei... acho que vou relaxar um pouco então... mas sem dormir."

            mc "Faça como você achar melhor. Só feche os olhos e sinta..."

            w "Hmm..."

            label so2_premium1:

                pass

            "Ela já fechou o olho... mais 1 minutinho assim e ela dorme com certeza."

            "Se eu der uma puxadinha nela... aposto que dá pra bagunçar toda a roupa dela... e como ela nunca tá de sutiã..."

            "Agora... a questão é... eu vou me comportar ou vou tirar proveito dessa situação?"

            "Se ela descobre, eu nunca mais vou ter chance com ela. É fim da linha. E provavelmente eu tô no olho da rua também."

            "E agora?"

            menu:
                "Bora ver essa belezinha":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_35

                        jump so2_premium1

                    "Nem a pau que eu perco a chance de ver esse corpinho perfeito peladinho de novo..."

                    "É só mexer um pouco..."

                    scene sofia2_premium1 with Dissolve(1.0)

                    pause

                    "Olha lá... a roupa caindo tudo..."

                    "Esses peitinhos durinhos da Sofia são uma delícia."

                    "Da outra vez ela percebeu que tinha dado merda... mas se eu der sorte, hoje ela dorme antes de perceber."

                    "Tudo depende da minha técnica aqui."

                    w "Ahnn... assim..."

                    "Ela já tá gemendo. Com certeza tá dando certo."

                    "Só mais um pouquinho..."

                    w "Hmm... hmm... ..."

                    "Acho que foi... agora dá pra mexer um pouco na calça também."

                    "Arrastar um pouquinho ela assim..."

                    "Força, [mc]. Hoje ela vai ser inteirinha sua... e você vai poder pegar em tudo e não só olhar."

                    "Vou 'massagear' ela inteirinha... enquanto ela 'relaxa'."

                    w "Ah..."

                    "Perfeito. Agora é hora de aumentar o nível. E tirar o que falta..."

                    scene sofia1_premium2 with vpunch

                    w "Meu Deus!"

                    mc "H-HM!?"
                    scene sonew_ani04 with Dissolve(1.0)
                    w "De novo?!"

                    mc "P-puxa! Tô com os olhos fechados!"

                    scene black with vpunch

                    w "Que droga... de novo passando essa vergonha! Tudo porque eu odeio sutiã! Ele me aperta... é horrível!"

                    mc "T-tudo bem... eu prometo que não vi nada de novo. Vamos parar?"

                    w "Da outra vez eu perdi sua massagem por causa disso... dessa vez eu não quero."

                    mc "S-sério?!"

                    "Eu vou poder massagear ela com os peitos de fora?! Não acredito!"

                    w "Pode abrir os olhos, [mc]."

                    "Não acredito..."

                    mc "Ok..."

                    scene sofia2_premium2 with Dissolve(1.0)

                    pause

                    "PUTZ! Era bom demais pra ser verdade!"

                    w "Se eu ficar assim, não tem perigo de acontecer de novo..."

                    w "Eu sei que eu não devia deixar isso, mas vou te falar que eu já tô meio grogue... nem sei direito o que tá acontecendo."

                    mc "Haha... você tá cansa demais, [w]. Cinco minutinhos relaxando e você capota."

                    w "É... então continua só mais um pouco... tá funcionando tão bem..."

                    mc "Claro!"

                    "Ela não percebeu que a calça dela 'escorregou' assim?"

                    "Claro que foi culpa minha... mas pensei que ela ia sentir... mas apagada desse jeito acho que ela tá nem aí."

                    "Ou ela sabe e nem liga? Não faz a cara dela, mas... não dá pra ter certeza. Talvez ela tá curtindo um lance quente. Seria incrível!"

                    "Deixa eu voltar pra massagem."

                    w "Ahnn... isso... mais um pouco assim..."

                    mc "Que bom que você gosta."

                    w "Adoro... hmmm..."

                    scene sofia2_premium3 with Dissolve(1.0)

                    pause

                    "Eu tô massageando, só que não consigo tirar o olho da bunda dela."

                    "N-não consigo me concentrar direito..."

                    "Eu vou acabar fazendo cagada assim. Eu preciso... focar nos pés... e não no rabão dela."

                    w "nhh... ..."

                    "Parece que tá funcionando... ela deve tá quase do outro lado agora."

                    "E se ela dormir pra valer... daí, meu filho... nada levanta essa aí. Eu posso massagear o que eu quiser."

                    mc "Sofia? Tá bom?"

                    w "..."

                    mc "Sofia??!!"

                    w "..."

                    "Não dá pra ter certeza que ela tá dormindo... mas se ela tivesse acordada ela ia responder, né?"

                    "Não tem como esperar mais. Se eu quiser fazer alguma coisa, tem que ser agora antes do guarda chegar."

                    "Se ela tiver acordada... fodeu."

                    menu:
                        "Tirar a calça dela com cuidado":


                            mc "Sem chance de eu parar aqui. É agora ou nunca."

                            "Com cuidado... mantendo a massagem..."

                            scene black with dissolve

                            scene sofia2_premium4 with Dissolve(1.0)

                            pause

                            mc "Uau!"

                            "Agora sim... é disso que eu tô falando."

                            "E dessa vez eu vou pegar em você inteira... não vou só olhar não."

                            mc "Assim mesmo..."

                            "Pegar nas pernas... nessa bundinha arrebitada..."

                            "Acho que dá pra eu tirar a blusa dela aos poucos também."

                            "Só ir com bastante cuidado..."

                            "Ir empurrando enquanto eu faço massagem nas costas. Acho que dá..."

                            "De pouco em pouco..."

                            scene sofia2_premium5 with Dissolve(1.0)

                            pause

                            "Isso aí. O pior já passou. Agora é só tirar aqui..."

                            "E deixar ela peladinha..."

                            "Ir empurrando e pegando nela... você é inteira minha, Sofia."

                            "A gente trabalhou bastante juntos..."

                            "Tá até rolando um lance entre a gente. Eu sei que a gente vai acabar fazendo isso cedo ou tarde."

                            "Eu só tô antecipando um pouquinho, certo?"

                            "Só sendo um cara de pau completo pra tentar justificar um lance desses aqui."

                            "Pelo menos tenha bolas pra admitir que você é um escroto, [mc]."

                            "Ok... falta pouco pra camisa e eu vou soltar esses peitos deliciosos. Deixar tudo livre, [w]."

                            "Devagar..."

                            scene black with dissolve

                            scene sofia2_premium6 with Dissolve(1.0)

                            pause

                            mc "Isso aí!"

                            "Olha pra essa delícia..."

                            "Mas eu prometi que dessa vez eu não ia só ficar vendo, [w]... eu quero mais."

                            "Eu quero sentir você... e eu já peguei no seu corpo todo praticamente."

                            "Falta esses peitos e sua... hmm..."

                            "Pegar nos peitos é tentador, mas eu acho que o maior prêmio é aqui em baixo."

                            "Eu vou roçar sua bucetinha até você ficar molhada... e daí eu vou fazer você se sentir muito bem."

                            "Será que eu consigo fazer você gozar dormindo?"

                            "Impossível. Aposto que daí você vai acordar."

                            "Mas... alguma coisa dentro de mim diz que se eu conseguir... talvez eu possa mudar alguma coisa dentro de você."

                            "Imagina se você fica menos seca e começa a aproveitar um pouco mais os prazeres da vida?"

                            "Eu vou mexer no seu subconsciente... você vai sentir um prazer que nunca sentiu e vai querer sentir de novo."

                            "Se isso funcionar mesmo... eu vou ter transformado você numa mulher de verdade."

                            "Ou eu só vou me ferrar completamente mesmo."

                            "E agora?"

                            menu:
                                "Isso é loucura. Parar aqui.":


                                    "Eu tô muito drogado mesmo. Só pode."

                                    "Melhor eu parar aqui e não arriscar. Vou ajeitar a roupa dela... e tacar ela pra fora do sofá ver se acorda."

                                    scene black with dissolve

                                    scene sofia1_new2 with Dissolve(1.0)

                                    mc "Sofia, você dormiu de novo."

                                    w "Ah... obrigada..."

                                    mc "Melhor a gente encerrar por aqui."

                                    w "Hm? Ah... tem razão... tava tão gostoso..."

                                    mc "Sei... Amanhã tamo aí pro batente igual sempre."
                                "Masturbar ela dormindo":


                                    mc "Se tudo der certo... você vai me agradecer depois."

                                    "Não esquenta que eu não vou te machucar."

                                    "Eu vou começar bem devagar... nas suas costas..."

                                    scene black with dissolve

                                    scene sofia2_premium7 with Dissolve(1.0)

                                    pause

                                    mc "Isso... é gostoso, né?"

                                    w "..."

                                    "Pela carinha dela, ela tá curtindo bastante."

                                    "Agora é começar a esfregar a preciosa... bem no clítoris."

                                    "Bem devagar... pra ela começar a sentir gostoso."

                                    "Passa aqui fora... mais pra dentro... hmmm..."

                                    "Eu tô sentindo você molhada, [w]. Você tá gostando, né?"

                                    w "Hmm..."

                                    mc "Já tá gemendo, é?"

                                    "Eu nem comecei ainda. Agora você vai ver."

                                    w "Ahnn..."

                                    "Agora!"

                                    scene black with dissolve

                                    w "Ahnn!"

                                    mc "Isso!"

                                    scene sofia2_premium8 with vpunch

                                    pause

                                    w "NNNGH!! NNNNGGHHH!!!"

                                    "Ela tá gemendo muito alto!"

                                    mc "Você tá quase lá, [w]! Só mais um pouco!"
                                    scene sonew_ani05 with Dissolve(1.0)
                                    w "HMMNNN!!! NMM??!"

                                    w "HMM?!!"

                                    "Ela tá acordando!!!"

                                    w "Q-que tá acontecendo aqui?!!!"

                                    scene black with hpunch

                                    w "Minha nossa!!!!"

                                    w "[mc]!!!!!"

                                    scene sofia2_premium9 with vpunch

                                    w "AAAHHH!!!"

                                    w "Eu tô nua! Cadê você, [mc]?!!!"

                                    w "O que aconteceu?!"

                                    w "E-eu não lembro de nada! Eu deitei... e massagem! E... e..."

                                    w "Que merda aconteceu aqui?!!!!!"

                                    w "Eu vou encontrar o criminoso que fez isso e acabar com sua vida!!!"

                                    scene black with dissolve

                                    $ dia_sofia = dia + 1

                                    jump call_cidade
                        "Para tudo agora e arrumar ela":


                            "Melhor eu parar aqui e não arriscar. Vou ajeitar ela e acordar ela... tacando ela pra fora do sofá."

                            scene black with dissolve

                            scene sofia1_new2 with Dissolve(1.0)

                            mc "Sofia, você dormiu de novo."

                            w "Ah... obrigada..."

                            mc "Melhor a gente encerrar por aqui."

                            w "Hm? Ah... tem razão... tava tão gostoso..."

                            mc "Sei... Amanhã tamo aí pro batente igual sempre."
                "Eu sou um cara decente":


                    mc "Cuidado que você já tá quase dormindo. Melhor a gente encerrar por aqui."

                    w "Hm? Ah... tem razão... tava tão gostoso..."

                    mc "Sei... Amanhã tamo aí pro batente igual sempre."
        "Não vale a pena":


            mc "Ok. Amanhã tamo aí."

    w "Com certeza. Tchau."

    mc "A gente se fala."

    scene black with dissolve

    $ dia_sofia = dia + 1

    jump call_cidade

label sofia_trabalho_evento3:

    scene trabalho geral with Dissolve(1.0)

    "Caraca. Não tem ninguém aqui ainda."

    "Tô ajudando tanto a [w] que tô me acostumando em vir aqui cedo. Quem diria..."

    mc desconfiado "Âh?"

    scene sofia redacao_dormindo with Dissolve(1.0)

    pause

    mc desconfiado "A [w] tá capotada ali no lounge."

    "Sorte que não tem ninguém aqui ainda."

    "Provavelmente a doida passou a noite aqui. De novo..."

    w "AH?!"

    mc envergonhado "Bom dia."

    w "!"

    scene sofia_sentada1 with Dissolve(1.0)

    w "Bo-bom dia..."

    w "{i}Uaaahh...{/i}"

    mc zerado "[w], você nem tá conseguindo abrir o olho."

    w "..."

    mc "[w]!"

    w "Ah! Tá tudo bem. A matéria tá pronta."

    mc "..."

    w "É... acho que eu acabei dormindo aqui ontem."

    mc envergonhado "Tô vendo."

    w "Que vergonha..."

    if sofia_confiou:

        mc charmoso "Não é a primeira vez que eu vejo você dormindo aqui."

        w "Verdade..."
    else:


        mc "Não seja boba."

    mc desconfiado "Você precisa acordar."

    w "Eu tô acordada..."

    mc "Mais ou menos..."

    w "..."

    mc charmoso "O que você acha da gente tomar aquele café pra dar energia?"

    w "Eu acho que você já me chamou várias vezes pra tomar café."

    mc envergonhado "Quase certeza que não..."

    w "Mas acho que é uma boa. Eu realmente podia tomar alguma coisa."

    mc normal "Vem."

    play sound "audio/som_35_passos.mp3"

    scene trabalho chefe_porta with Dissolve(1.0)

    mc normal "Isso. Deixa eu preparar pra você."

    w "Bastante açúcar por favor."

    mc "Tá."

    w "Bastante mesmo."

    mc "Pode deixar."

    "..."

    scene sofia_cafe1 with Dissolve(1.0)

    mc "E aí? Ficou do agrado?"

    w "Hmm..."

    w "Podia ser um pouco mais doce, mas tá bom. Obrigada."

    mc "Não pensei que você tomasse café tão doce assim."

    w "..."

    w "É que na verdade eu não gosto de café."

    mc "Sério? Mas você toma café todo dia que eu te vejo aqui."

    w "É que..."

    mc "?"

    w "Promete que não vai rir de mim?"

    mc "Claro. O que foi?"

    w "É que eu acho que as pessoas vão me levar mais à sério se eu tomar café..."

    mc "{i}pff{/i}"

    w "Ei..."

    mc "Desculpa. Não aguentei."

    w "Eu sei que é idiotice..."

    mc "Ei. Eu não falei isso."

    w "Mas eu sei..."

    mc "Eu só achei engraçado porque você normalmente é tão séria. Daí você fala uma coisa tão infantil dessas, sei lá. Foi meio chocante."

    w "Hmm..."

    scene sofia_cafe2 with Dissolve(1.0)

    pause

    mc preocupado "Que foi?"

    w "Nada."

    mc "Pode me falar."

    w "É que eu fiquei com vergonha de você me ver dormindo assim aqui no trabalho. Não é o exemplo que eu quero passar."

    mc triste "Você tá se esforçando demais. Precisa de um tempo, [w]."

    w "E-eu sei..."

    w "É que... desde que eu cheguei na redação minha vida virou um inferno."

    w "Não tô conseguindo dormir direito. Fico ansiosa por tudo. Às vezes eu queria ser atropelada só pra não vir trabalhar."

    mc "Tá doida? Não fale uma coisa dessas."

    w "Todo o trabalho que a gente tá tendo. Eu até consigo ver o resultado, mas cada dia é uma luta. Meu pai, a [j], os outros..."

    w "Eu não sei se eu vou aguentar isso por muito mais tempo."

    mc charmoso "Eu sei que você vai."

    mc charmoso "Você é uma garota forte."

    w "Vo-você acha mesmo?"

    mc "Claro. Você tá enfrentando pessoas que eu nunca pensei em desafiar."

    w "..."

    mc "Você confia ou não em mim?"

    w "Depois dessas últimas semanas, eu aprendi a confiar em você, [mc]."

    w "Mas... é que..."

    w "Não sei se eu posso falar sobre algo particular assim no serviço."

    mc preocupado "Claro que pode. Eu não quero ser só um colega de trabalho. Eu quero ser seu amigo também."

    if sofia_amizade >= 9:

        $ sofia_e2_good = True

        $ renpy.notify("Sofia sente que pode se abrir com você")

        w "Amigo?!"

        mc desculpa "Esses dias que a gente passou trabalhando juntos o dia todo. A gente viu tanta coisa, passou por um bocado."

        mc envergonhado "Foi complicado, mas a parte boa é que eu pelo menos pude conhecer melhor você."

        mc charmoso "E eu realmente acho que por dentro dessa chefinha manda-chuva, tem uma mulher incrível e muito bacana."

        w "!"

        w "[mc]..."

        scene sofia_cafe3 with Dissolve(1.0)

        w "Você fala umas coisas às vezes..."

        mc "C-como assim?"

        w "Você desarma a gente. É meio bobo, meio careta..."

        mc "Ei."

        w "Mas você é tão sincero e eu nem sei por que, mas você parece tão interessado em mim. Digo! Que eu esteja bem, sabe?"

        mc "E qual é o problema?"

        w "É estranho... as pessoas hoje não se preocupam muito com as outras."

        w "Eu mesmo sou extremamente egoísta. Só penso em como deixar a revista melhor e em como colocar minhas ideias aqui."

        w "Nunca pensei como você, a [j], o Ronaldo, meu pai ou qualquer outra pessoa da revista estavam se sentindo."

        w "E mesmo você também sendo tão profissional comigo na redação. Nunca deu em cima de mim de forma desrespeitosa..."

        w "Também nunca veio com graça e sempre colocou o trabalho em primeiro lugar. Uma conduta que eu sempre achei incrível."

        w "Só que mesmo assim você consegue olhar pra mim e ver o que eu tô passando e tem interesse de verdade em me ajudar."

        w "É muito mais incrível do que eu."

        mc "Você tá exagerando. Eu não fiz nada disso."

        w "Fez, sim. E eu acho você... incrível de verdade, [mc]."

        mc "Ah! É..."
    else:


        $ renpy.notify("Sofia não se sente confortável se abrindo com você")

        w "Quer saber? É só algo bobo. Não se preocupe isso."

        scene sofia_cafe1 with Dissolve(1.0)

        w "Nós estamos fazendo um bom trabalho juntos e é isso que a gente tem que continuar fazendo, certo?"

        mc desculpa "Sim, mas sua saúde também é importante. Não-"

        w "Pare de ser bobo, [mc]."

    w "A revista tá mudando. E mesmo que meu pai não entenda isso agora, um dia ele vai perceber."

    w "Meu pai vai reconhecer nosso trabalho. E acho que até a [j] pode um dia ver que nós melhoramos as coisas."

    w "A redação já tá mudando. Os textos estão bem melhores, você não acha?"

    mc "Sim. Eu percebi isso também."

    w "Vamos continuar nosso trabalho."

    mc "Ok. Com certeza."

    w "Obrigada por tudo."

    w "Ah! Acho que eu preciso de um descanso. Vou pra casa e tirar o dia de folga."

    label so2_premium2:

        pass



    menu:
        "Você sabe que eu posso te ajudar, né?":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_36

                jump so2_premium2

            mc "Você sabe que eu sou bom em fazer você relaxar. Se você tiver afim."

            scene sofia_cafe2 with Dissolve(1.0)

            w "Sei..."

            mc "Que foi? Aconteceu alguma coisa?"

            w "O que aconteceu da outra vez que você fez massagem em mim? Você acredita que eu acordei sem roupa?"

            "Tem razão! Eu tinha até esquecido!"

            "Ela acordou na hora que eu tava masturbando ela dormindo. Daí eu saí correndo e deixei ela pelada lá. Puta mancada..."

            mc "Eu saí e q-quando eu voltei você não tava mais lá."

            w "Claro! Eu peguei minhas coisas e saí correndo! Mas não imaginei que você ia me deixar sozinha!"

            mc "D-desculpa... eu tava fazendo massagem nos seus pés... daí você dormiu e eu fui no bar. Quando eu voltei, você não tava mais aqui."

            w "A culpa não foi sua. Meu pai já demitiu o vigia. Eu não queria fazer isso, mas só pode ser ele."

            mc "A-ah! Nossa... e-ele mereceu então. Mas e se for a Cássia. Você sabe que ela tem coisa contra você..."

            w "É uma possibilidade... mas ela não tava aqui. E tava quase na hora do vigia chegar."

            w "Tem as câmeras de segurança..."

            mc "C-câmeras?!"

            w "É."

            mc "V-você viu as fitas?"

            w "Então... é aí que a coisa ficaria interessante..."

            w "Mas infelizmente é o próprio vigia que liga elas quando ele chega. Então não tinha nada daquele dia ainda."

            mc "Caraca! Que sort- digo- que c-coisa, hein?!"

            w "..."

            w "Você nunca faria algo assim comigo, não é mesmo, [mc]?"

            "Ai! Que dor no coração... meu estômago tá tão embrulhado que eu tô quase vomitando aqui."

            "Ela deve tá vendo eu suando frio... tô gaguejando... chacoalhando a perna... será que ela já entendeu tudo?!"

            "Será que eu falo a verdade? Não! Se ela não tem a fita, é impossível provar! O que eu faço?!"

            menu:
                "A verdade é que fui eu.":


                    $ renpy.block_rollback()

                    mc "Eu tenho que ser sincero com você."

                    w "N-não!"

                    mc "Desculpa... mas fui eu..."

                    mc "Eu achei que você ia gostar... que poderia te ajudar... além de que foi tentação demais."

                    mc "Eu sei que isso não é certo. Eu me sinto um canalha, mas eu queria que você soubesse a verdade."

                    w "..."

                    w "Então foi isso, [mc]..."

                    mc "Sim... me perdoa..."

                    w "Falando assim, parece que você pelo menos tem coragem... isso é muito importante."

                    mc "Valeu..."

                    w "Se foi com a intenção de me ajudar, então tudo bem, né? Só não fazer de novo, certo?"

                    mc "C-certo."

                    $ renpy.vibrate(1)

                    play sound som_17_tiro

                    scene red with vpunch

                    w "Você acha mesmo que isso é o suficiente?!!!!"

                    w "Que você pode fazer isso com uma mulher inconsciente e achar que pedir desculpas resolve tudo?! Você é IDIOTA?!"

                    w "Você é um CRETINO SEM BOLAS! UM HOMENZINHO SEM MORAL!!!"

                    w "E VOCÊ VAI COMEÇAR INDO PRO OLHO DA RUA!!!!"

                    mc "S-sofia! Nãoooooo!!!"

                    scene black with dissolve

                    scene cidade noite with Dissolve(2.0)

                    "Eu estraguei tudo! Não disse uma palavra sequer depois daquilo..."

                    "Mesmo com meus pedidos de desculpa, o chefe me colocou pra fora."

                    "Dois quarteirões longe e eu ainda conseguia ouvir ele me amaldiçoando."

                    "Tive que voltar a morar com minha família. Eles me empregaram na empresa que eles tinham."

                    "Até que a polícia veio e o processo começou."

                    "O chefe e a Sofia não pararam até me verem atrás das grades."

                    "No fim, as câmeras de filmagem tinham pego tudo e eu não tive como defender minha inocência."

                    "Foi demais pra mim. Eu fiquei doente e acabei morrendo de desgosto."

                    "{i}Final Z: Faz o que quer, morre como não quer{/i}"

                    scene black with Dissolve(2.0)

                    $ renpy.full_restart()
                "Claro que não. Eu sou um homem decente.":


                    mc "Que pergunta é essa? Claro que não! Eu sou um homem decente, [w]."

                    w "Eu sei. Desculpa. É que você pareceu nervoso e você tinha sumido... eu tinha que perguntar."

                    mc "Não duvide mais da minha idoneidade desse jeito!"

                    w "Desculpa de novo. Não vou tocar mais no assunto."

            w "Mas já que você tá oferecendo e o pervertido foi demitido... eu vou aceitar mais uma massagme."

            mc "P-perfeito! Bora!"

            scene black with dissolve

            scene sofia mc_massagem with Dissolve(1.0)

            w "Ah... essa tá sendo a nova vantagem de trabalhar até tarde..."

            mc "Haha..."

            w "Poder ficar sozinha e receber uma massagem dessas... hmm..."

            w "E agora sem se preocupar com o vigia... só a gente fechar aqui quando acabar."

            mc "Pode deixar. Então... só relaxe..."

            w "Sim... hmmm..."

            "Da última vez eu tive que te abandonar na metade... mas dessa vez eu vou até o fim."

            "Eu vou garantir que você vai gozar gostoso, Sofia. E você vai virar outra pessoa."

            "Eu só preciso ir com tudo. Não vou esperar muito, não."

            w "Nngh..."

            "Ela já tá entrando no clima."

            "Pegar nela tá sendo uma das melhores coisas que já aconteceu na redação aqui."

            "Eu fico duro muito rápido pegando nela assim. E a Sofia é tão gata. Minha nossa..."

            w "..."

            mc "Sofia?"

            w "Mnnzz..."

            mc "Parece que é o suficiente."

            "Eu não aguento mais esperar. Eu preciso enfiar meus dedos nela e fazer ela gozar."

            mc "Com licença, [w]."

            w "Nannzz..."

            scene black with dissolve

            scene sofia2_premium10 with Dissolve(1.0)

            pause

            mc "Uhum... vamos preparar você pro que tá vindo."

            w "Nngh..."

            mc "Essa pele lisinha... tão cheirosa... como você consegue trabalhar tanto e mesmo assim ser tão gostosa de pegar?"

            mc "Aposto que você também tem suas necessidades."

            mc "Ninguém tem coragem de chegar em você, mas você quer, não quer?"

            mc "Quer que alguém te dê muito prazer..."

            if sofia_namoro:

                mc "Mesmo a gente NAMORANDO, eu nunca tive a chance de fazer nada."

                mc "Olha o que eu tenho que fazer pra sentir minha namorada!"

            mc "Mas hoje eu vou fazer você se sentir bem. E eu vou sentir bem também."

            mc "Eu vou usar você pra chegar lá também. Mas como eu sou um cavalheiro, primeiro você, madame."

            mc "Deixa eu tirar isso aqui. Com licença."

            scene black with dissolve

            scene sofia2_premium11 with Dissolve(1.0)

            pause

            mc "Que delícia..."

            w "Nhhh..."

            mc "Você tá sentindo também, né? A gente tá quase lá, linda."

            mc "Mesmo dormindo você continua sentindo vontade... e eu vou te dar o que você tá querendo."

            mc "Abre esses buraquinhos pra mim."
            scene sonew_ani08 with Dissolve(1.0)
            mc "Aposto que você vai gostar MUITO!"

            "E-espera... da outra vez ela acordou justamente assim."

            "Eu tô indo mais rápido hoje, mas nada garante que ela não vai acordar outra vez."

            "E agora só tem eu pra incriminar. Eu sinto que pode dar muita merda isso."

            if sofia_namoro:

                "E a gente é namorados. É só eu ter paciência que as coisas vão correr naturalmente."

                "M-mas eu aguento esperar? AAHH!"

            "O que eu faço?"

            menu:
                "Parar enquanto há tempo":


                    mc "Eu tô parando aqui. É demais."

                    "Eu não quero acabar na cadeia por causa disso."

                    mc "Sofia? SOFIAAAAAA!!!!!"

                    "O-opa! Deixa eu arrumar ela antes!"

                    scene black with dissolve

                    scene sofia1_new2 with Dissolve(1.0)

                    w "H-hm?"

                    mc "Você dormiu durante a massagem de novo."

                    w "Puxa... mas que coisa, hein?"

                    mc "Melhor a gente fechar tudo aqui e dar o fora."

                    w "Tá. Pode deixar que eu cuido disso. Você merece um descanso depois do que você fez."

                    mc "D-depois do que eu fiz?"

                    w "Da massagem, bobo."

                    mc "Ah! Claro! Haha..."

                    w "Até amanhã, [mc]."

                    mc "Até."

                    scene black with dissolve

                    $ dia_sofia = dia + 1

                    $ tempo = 2

                    $ v21_fim = True

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("v21_fim","sofia","personagem")

                    jump call_cidade
                "Enfiar os dedos dela e ir até o fim":


                    "Sem chance de eu parar aqui. Se prepara pra sentir gostoso."

                    scene black with dissolve

                    w "Hn-hnnn!"

                    scene sofia2_premium12 with Dissolve(1.0)

                    pause

                    mc "Hmm... que buraquinho gostoso. Você é tão apertadinha..."

                    w "Aahnn..."

                    mc "Gostou?"

                    w "Hmhmmm!"

                    mc "!"

                    mc "Sofia?"

                    w "Aahnn... aah..."

                    "Que susto... claro que ela tá dormindo."

                    mc "Hoje eu paro só com você gozando!"

                    scene sofia2_premium12 with vpunch

                    w "AAHNN!!"

                    mc "Isso mesmo! Goza pra mim, gostosa!"
                    scene sonew_ani07 with Dissolve(1.0)
                    w "Ahnn! Aanhnnnfg!"

                    mc "Eu quero ver você tremendo na minha mão! Você é minha agora!"

                    w "Aagnnh! Aahnnn!"

                    mc "Tá quase lá!"

                    scene sofia2_premium15 with vpunch

                    pause

                    w "AAGNNH!!!"

                    mc "Goza, gata! Goza pra mim!"

                    w "Aanngh! AAAINNGG!!"

                    scene sofia2_premium15 with vpunch

                    w "AAAAAAGHHHHHH!!!"

                    mc "Isso!"

                    w "Aaghh... ahhnn...."

                    mc "Uau!"

                    mc "Você esguichou um monte... fazia tempo, né?"

                    w "Aahnn..."

                    mc "Sofia?"

                    w "Hmmm?!"

                    scene black with hpunch

                    w "Hmm... [mc]?"

                    "!!!"

                    w "[mc]? Eu dormi de novo?"

                    scene sofia2_premium13 with Dissolve(1.0)

                    pause

                    w "HUH!?"

                    w "D-de novo?! Por que eu tô pelada?!"

                    w "Eu tô toda suada... como?"

                    w "MAs o vigia foi demitido!"

                    w "Droga... sem ele também não vai ter câmeras..."
                    scene sonew_ani09 with Dissolve(1.0)
                    w "Então... [mc]... por que você não tá aqui de novo?"

                    w "..."

                    w "E o que é isso que eu tô sentindo? Eu..."

                    w "Hmm..."

                    scene sofia2_premium14 with Dissolve(1.0)

                    pause

                    w "Meu corpo tá leve... como se eu tivesse tirado 10 quilos de peso das minhas costas..."

                    w "E aqui embaixo... tão sensível... eu sinto até o ar tocando minha pele..."

                    w "Ah... é uma sensação... tão..."

                    w "Tão boa..."

                    w "Eu tinha até esquecido como era..."

                    w "A última vez que eu me dei uma atenção assim foi antes da minha viagem."

                    w "Eu preciso... ah... eu preciso arrumar um tempo pra mim."

                    w "E quanto a essas massagens... eu vou descobrir a verdade sobre isso..."

                    w "Só de ser isso... mas eu não quero acreditar... por favor..."

                    window hide

                    pause

                    scene black with dissolve

                    $ dia_sofia = dia + 1

                    $ tempo = 2

                    $ v21_fim = True

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("v21_fim","sofia","personagem")

                    jump call_cidade
        "Boa ideia.":


            mc "É uma excelente ideia."

    w "Até amanhã, [mc]."

    mc "Até."

    play sound "audio/som_35_passos.mp3"

    scene trabalho chefe_porta with Dissolve(1.0)

    "..."

    "Não sei nem o que pensar sobre a [w]."

    "Ser chefe parece sempre uma coisa foda demais, mas ter que carregar esse peso, parece tão desgastante."

    "Acho que essa é a diferença entre ter um bom chefe, que realmente se importa e um que só quer mandar."

    "Espero que ela aguente o tranco."

    "Acho que vai ser bom tanto pra mim, quanto pra revista, como pra todas as pessoas que usam nossas matérias pra se informar."

    "E ela com certeza é uma graça. Quem sabe..."

    mc tarado "Hehehe..."

    mc zerado "Tô parecendo um tarado."

    $ dia_sofia = dia + 1

    $ tempo = 2

    $ v21_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v21_fim","sofia","personagem")

    jump call_cidade

label sofia_trabalho_evento:

    if sofia_xp <= 35:

        $ sofia_xp += 1

    if sofia_xp >= sofia_next:

        if sofia_lvl == 0:

            $ sofia_lvl = 1
            $ sofia_next = 15
            $ sofia_imagem = "extra/sofia_lvl1.png"

            jump sofia_trabalho_evento1

        elif sofia_lvl == 1:

            $ sofia_lvl = 2
            $ sofia_next = 35
            $ sofia_imagem = "extra/sofia_lvl2.png"

            jump sofia_trabalho_evento2







    scene sofia_trabalhando with Dissolve(1.0)

    $ rand = renpy.random.randint(1,10)

    if sofia_xp == 1:

        w "Hoje eu quero que você reveja esta matéria sobre a construção do aeroporto."

        mc "Uou... quem descobriu isso?"

        w "O Ronaldo. Ele teve acesso a uns documentos vazados da prefeitura."

        w "Mas a gente precisa ver se as datas checam e se não é algo forjado."

        mc "Ok. Pode deixar que vou ver aqui."

    elif sofia_xp == 2:

        w "Eu tenho uma matéria aqui sobre a Cidade Chinesa."

        w "É sobre uma tal de garota imortal. Pra mim isso aqui é balela."

        if bao_evento >= 3:

            "É a tal da [xu]."

            "Será que eles vão descobrir a verdade sobre ela?"

        mc "O-ok. Vou conferir aqui."

        w "Obrigada."

    elif sofia_xp == 4:

        w "Parece que um dos secretários do prefeito foi pego na porta de um clube de BDSM no Distrito."

        w "Só que não temos nenhuma foto."

        mc "Complicado, hein? E como sabemos disso?"

        w "Não sei. Precisamos ver com o repórter."

        w "Só que eles iam publicar a matéria assim. Sem nenhuma prova contundente."

        w "Isso não é Jornalismo. A gente precisa ter um compromisso real com a verdade."

        mc "Você tá certa."

    elif sofia_xp == 6:

        w "Deixa eu te mostrar um negócio aqui."

        mc "S-sofia?"

        w "Que foi?"

        mc "Nada não!"

        "E-ela tá tão perto de mim! Eu consigo até sentir o calor do corpo dela..."

        "Que merda eu tô pensando?!"

        w "Entendeu?"

        mc "Eu?"

        w "Como assim?!"

        mc "Entendi! Entendi!"

        "Que merda será que ela disse?"

    elif sofia_xp == 8:

        w "Tenho uma informação quente aqui hoje."

        w "Parece que aquela Quincy Jones visita a capital de tempos em tempos."

        w "Essa mulher é um mistério e poucas pessoas sabem o paradeiro dela."

        w "Só que a matéria que esse cara escreveu tá tudo errada. Dá uma olhada por favor."

        mc "Certo."

        if fabricio_atencao > 0:

            mc "Na verdade eu já passei a pauta pro chefe sobre a [qui]."

            mc "Acho que não saiu ainda, mas eu descobri que ela vai no bar em dia de lua cheia."

            w "Sério isso?! E por que meu pai não publicou ainda?"

            mc "Não sei."

            w "Vou ver com ele..."

        elif fabricio_p1:

            "Eita... eu tenho a pauta da [qui] que o [gar] me deu, mas ainda não passei pro chefe."

            "Será que eu devia entrar pra ele?"
        else:


            mc "Acho que eu nunca ouvi falar dessa mulher. Quem é ela?"

            w "É uma mágica que se apresenta raramente e faz alguns truques que ninguém sabe explicar."

            mc "Caraca..."

    elif sofia_xp == 10:

        w "Preciso que você cheque uma informação importante aqui sobre a antiga estação."

        mc "Antiga estação?"

        w "Sim. A estação de trem que ligava a ilha ao continente. Só que não é mais usada."

        mc "Ah! Tô sabendo..."

        "Eu lembro daquela vez que a [c] fugiu..."

        mc "O que tem a estação?"

        w "Parece que tem pessoas usando o lugar pra fazer negócios longe dos olhos da sociedade."

        mc "T-tipo uma gangue? Tráfico de drogas?"

        w "Isso não sabemos. Mas foram vistas marcas de pneu frescas no lugar. O que quer dizer que foi usado recentemente."

        w "Vamos dar uma olhada melhor nas informações da pauta."

        mc "Ok."

    elif sofia_xp == 12:

        w "Conseguimos um follow up sobre o aeroporto. Parece que ele já tá em construção em uma área próxima à ilha."

        mc "Sério?!"

        w "Sim. O Ronaldo conseguiu outro documento. Bem interessante as informações que estavam lá."

        w "Vai ser um mega empreendimento. Algo do nível do cassino do Barão."

        mc "A capital tá com tudo mesmo, hein."

        w "Não é à toa que tem essa quantidade de celebridades e pessoas importantes vivendo por aqui."

        w "E com certeza esse aeroporto só vai elevar ainda mais o status da ilha."

        mc "Interessante mesmo isso..."

        w "Mas a gente precisa verificar se a informação é verdadeira. Tem várias datas no documento."

        w "Queria que você visse comparasse com a agenda pública dos secretários pra ver se tudo bate."

        mc "Pode deixar."

        "Mano... que trabalheira..."

    elif sofia_xp == 14:

        w "Quero que você reveja esta matéria da [j]."

        mc "QUÊ?!"

        w "Que foi?"

        mc "Você quer editar uma matéria da [j]?"

        w "Estamos fazendo isso com todo mundo não estamos?"

        mc "Mas a [j]?"

        w "Todos aqui na redação são iguais."

        mc "Entendi..."

        menu:
            "Acho que eu prefiro não me meter com a [j].":


                mc "Olha, [w]. Eu quero te ajudar, mas não quero me meter com ela."

                w "Tudo bem. Pode deixar que eu faço isso."

                mc "Muito obrigado."

                "Não tem porque comprar briga com a [j] por coisa boba. Não sou idiota."
            "Tudo bem. Eu faço.":


                $ sofia_amizade += 1

                $ sofia2_cassia = True

                mc "Tudo bem, vou fazer."

                w "Obrigada."

                "Óbvio que isso vai dar merda. E eu vou tá no rolo também."

    elif sofia_xp == 17:

        w "Chegou uma pauta bem estranha aqui."

        mc "O que ela diz?"

        w "Uma garota loira foi vista em cima de um poste no centro da cidade."

        mc "Loira em cima de um poste?"

        w "Isso..."

        if xeena_encontro:

            mc "QUÊ?!"

            "Só pode ser aquela mina que tava no condomínio da [j] aquela vez."

            "Então ela ainda tá por aí?"

            w "Que foi?"

            mc "Nada não..."

        mc "Que doideira, né?"

        w "Nem sei o que fazer com isto..."

        mc "Vou dar uma pesquisada ver se encontro outras referências."

        w "Obrigada."

    elif sofia_xp == 20:

        w "Tem uma matéria aqui sobre o filme da [cc]."

        mc "Que que tem? Novidades dela?"

        w "Na verdade é sobre o orc do filme."

        mc "Que que tem ele?"

        w "A matéria diz que a fantasia que ele usa, a maquiagem etc, são tão reais que ele nem parece um ator."

        mc "Que tipo de matéria é essa? O que isso quer dizer?"

        w "A conclusão é que talvez ele seja um orc de verdade..."

        mc "COMO ASSIM?!"

        w "Será que devemos só jogar a matéria fora?"

        mc "Sem comentários..."

    elif sofia_xp == 23:

        w "Preciso que você entre em contato com a empresa responsável pelo transporte público da cidade."

        mc "O que aconteceu?"

        w "Chegou uma pauta sobre um misterioso motorista de ônibus que não usa o uniforme padrão."

        w "Diz aqui que ele sempre vai trabalhar de camisa social, extremamente bem trajado."

        mc "Esse cara... eu já vi ele algumas vezes."

        w "Sério? E aí?"

        mc "Ele realmente tava de camisa social..."

        w "Vou pedir pra alguém investigar."

        mc "É uma boa."

    elif sofia_xp == 26:

        w "..."

        mc "Que foi? Tá meio quieta hoje."

        w "Hmm..."

        mc "Fala!"

        w "Calma..."

        w "Acho que as pautas estão ficando cada vez mais estranhas ultimamente."

        mc "O que é dessa vez?"

        w "Parece que algumas pessoas estão tendo o mesmo sonho ultimamente."

        mc "O que isso tem de incrível?"

        w "Calma."

        w "Chegaram vários relatos semelhantes. Assim, as pessoas têm o mesmo sonho todos os dias."

        w "Elas estão andando por um local isolado, desertos, vulcões ou nadando no meio do mar."

        w "E então uma criatura aparece e começa a falar com elas."

        w "Elas dizem que no começo não se lembravam do sonho, mas foi ficando cada vez mais vívido e vívido."

        w "Elas estão começando a ficar realmente assustadas. Alguns passam mais tempo dormindo do que acordados."

        mc "Caralho. Que porra é essa? Filme de terror?"

        w "Vamos ler essas transcrições aí de várias pessoas que ligaram pra redação."

        mc "Tá."

    elif sofia_xp == 29:

        w "Você já foi no bar que tem aqui perto?"

        mc "O bar do [gar]? Que fica ali depois da praça?"

        w "Esse mesmo!"

        mc "Que que tem?"

        w "Algumas pessoas que trabalham aqui fazem happy hour lá de vez em quando."

        mc "Eu sei. Nunca me chamaram..."

        w "Nunca me chamaram tambem. Isso não importa."

        w "O que acontece é que eles estão achando o garçom de lá muito estranho."

        mc "É... não tenho como discordar."

        w "E parece que ele organiza festas lá durante a madrugada depois que o bar fecha."

        mc "Tô sabendo..."

        "Eu tenho que ficar limpando lá igual idiota."

        w "Mas ninguém sabe o que acontece nesses encontros."

        w "Eu tenho aqui umas gravações de câmeras da região. Vamos checar todas as fitas e ver o que encontramos."

        mc "Não sei se eu quero descobrir..."

    elif sofia_xp == 32:

        w "Essa matéria aqui tá bem escrita, não acha?"

        mc "Verdade. O Ronaldo mudou bastante o jeito de escrever nessas semanas."

        w "Nem acredito... parece que nosso trabalho está surtindo efeito..."

        mc "Tudo bem?"

        w "Âh?"

        mc "Você parece meio cansada, sei lá."

        w "Tudo bem. Meu cansaço não importa. Temos que passar o olho em 10 matérias hoje."

        mc "Ieei..."
    else:


        w "Hoje vamos apenas corrigir textos."

        w "Tá tudo muito sensacionalista."

        mc "Eu odeio isso..."

        w "Não importa."

        mc "..."

    $ renpy.block_rollback()



    scene black with dissolve

    $ tempo += 1

    scene sofia_trabalhando with Dissolve(1.0)

    mc "Já não tá bom?"

    w "Ainda tem trabalho."

    mc "..."

    scene black with dissolve

    $ tempo += 1

    scene sofia_trabalhando with Dissolve(1.0)

    w "Ufa. Por hoje tá bom."

    mc "Aleluia!"

    w "Até amanhã."

    mc "Até."

    "Eu ainda vou morrer."

    scene black with dissolve

    $ proibido_salvar = False
    $ show_quick_menu = True

    jump call_cidade

screen sofia_trabalho():
    tag sofia

    modal True

    add "extra/confianca_texto.png":
        xpos 165
        ypos 25

    bar:
        xpos 150
        ypos 100
        yanchor 0.5
        xsize 251
        ysize 40
        value sofia_xp
        range sofia_next

    add sofia_imagem:
        ypos 100
        xpos 130
        xanchor 0.5
        yanchor 0.5

    imagebutton auto "extra/trabalhar_%s.png" xpos 140 ypos 180 action Jump("sofia_trab")

    imagebutton auto "extra/sair_%s.png" xpos 140 ypos 250 action Jump("sofia_sair")

label sofia_sair:

    hide screen sofia_trabalho

    mc envergonhado "Ah. Eu volto outra hora pra te ajudar."

    w "Ok..."

    jump cenario_trabalho

label sofia_minigame:

    $ renpy.choice_for_skipping()

    mc "Oi, [w]. Tudo bem?"

    w "Tudo..."

    show screen sofia_trabalho
    with dissolve

    pause

label sofia_trab:

    hide screen sofia_trabalho

    call checa_logado from _call_checa_logado_1

    mc "Oi, [w]. Estou pronto pra ajudar."

    call anuncio from _call_anuncio_2

    w "Oi. Ok. Deixa eu ver aqui as tarefas de hoje..."

    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    "..."

    python:
        if renpy.android:
            sofia_db = PythonSDLActivity.pegaSofia()

    if sofia_vez < sofia_db:

        "{b}Você já esperou para trabalhar com a [w] [sofia_db] vezes. Mas neste gameplay você trabalhou [sofia_vez] vezes.{/b}"

        "{b}Como não é preciso esperar duas vezes pelo mesmo evento, você pode continuar a história sem esperar novamente.{/b}"

        $ sofia_vez += 1

        python:
            if renpy.android:
                renpy.block_rollback()

        jump sofia_trabalho_evento

    call checa_tempo from _call_checa_tempo_2

    python:
        if renpy.android:
            stempo = PythonSDLActivity.checkStempoNext()

    if not stempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        w "Acho que hoje eu consigo dar conta sozinha. Aproveite pra descansar um pouco, ok?"

        mc normal "Beleza. Depois eu venho te ajudar."

        w "Isso. Obrigada."

        show black with Dissolve(1.0)

        p rindo "O [mc] pode ajudar a [w] uma vez a cada 3 horas do mundo real."

        label libera_sofia_coins:

            p "Use o app Relógio no celular do [mc] para ver quando o próximo trabalho estará disponível."

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        p "Ou você pode liberar o próximo trabalho agora mesmo usando Celebrity Coins."

        if persistent.coins >= 500:

            p "Liberar o próximo trabalho usará 500 Celebrity Coins"

            menu:
                "Liberar trabalho":


                    $ proibido_salvar = True
                    $ show_quick_menu = False

                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaSTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    "{b}Você usou 500 Celebrity Coins para liberar o próximo trabalho{/b}"

                    $ renpy.block_rollback()

                    hide black with dissolve

                    w "Pensando bem, acho que tem algo que você pode me ajudar."

                    mc "Beleza."

                    jump sofia_trabalho_continua
                "Agora não. Vou esperar o tempo.":


                    "{b}Você escolheu não liberar o próximo trabalho{/b}"

                    jump cenario_trabalho
        else:


            p lecionando "Você precisa de ao menos 500 Celebrity Coins para liberar o próximo trabalho."

            p "Você pode comprar Celebrity Coins com dinheiro do {b}seu{/b} mundo."

            p "Assim você pode continuar a história agora mesmo e ainda colabora com o desenvolvimento de CH."

            menu:
                "Ok. Quero comprar.":


                    p rindo "Legal!"

                    call comprar_coins from _call_comprar_coins_2

                    p "Se você comprou, agora pode avançar o tempo usando Celebrity Coins."

                    hide black with dissolve

                    jump libera_sofia_coins
                "A vida é dura. Tô sem grana pra isso agora.":


                    p rindo "Não tem problema."

                    p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais."

                    jump cenario_trabalho

    label sofia_trabalho_continua:

        python:
            if renpy.android:
                renpy.block_rollback()

    w "Certo. Vamos pra sua mesa e eu vou te passar o que eu preciso."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("trabalho_sofia","pixie","personagem")

    python:
        if renpy.android:
            PythonSDLActivity.setStempoNext()
            sofia_vez += 1
            snext = PythonSDLActivity.pegaSNext()
            renpy.block_rollback()

    if sofia_db <= 35:

        "{b}[mc] recebeu um adicional de C$ 5 no salário este mês{/b}"

        "Ufa... finalmente vai sobrar alguma coisinha do salário este mês. Tô cansado de só pagar conta."

    jump sofia_trabalho_evento

label sofia_evento3_pre:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("so3_save", extra_info="so3_save")

    $ iconchefe += 1

    $ estou_na_cidade = False
    $ sofia_e3 = "pre"

    "Mais um dia..."

    "..."

    mc desconfiado "..."

    "..."

    "Parece que a [w] não tá brigando com ninguém hoje."

    "Ronaldo" "Bom dia, [mc]!"

    scene trabalho angulo with Dissolve(1.0)

    mc "Fala ae, Ronaldo."

    show ronaldo_andando with dissolve

    "Ronaldo" "Tudo de boa esses dias?"

    mc envergonhado "Tudo, sim. Por que tá perguntando?"

    "Ronaldo" "É que... tu não vai me foder com ela, né?"

    mc desconfiado "Do que você tá falando?"

    "Ronaldo" "Tô vendo você direto com a chefinha... ela não é mole, né?"

    mc envergonhado "Haha... chefinha?"

    "Ronaldo" "É, pô!"

    menu:
        "Essa aí todo dia acorda com a macaca.":


            mc zerado "Essa aí não tem jeito mesmo. Tá todo dia com a macaca."

            "Ronaldo" "Hahaha! Dá pra ver. Meus pêsames, cara."

            mc normal "Mas de boa, não vou reclamar."

            "Ronaldo" "Quem sabe até num rola um lancinho, hein?"

            mc tarado "Hmmm..."

            "Ronaldo" "Quem a gente quer enganar? Dalí não sai nada, amigo."

            mc zerado "O triste é que você tem razão..."
        "Até que é de boa. A gente se acostuma.":


            mc envergonhado "Ela é meio casca grossa, mas depois a gente acaba acostumando."

            "Ronaldo" "Você tem sangue frio, cara. Não sei se eu ia aguentar isso, não."

            mc "Tem que aguentar, né?"

            "Ronaldo" "Ah, sei lá..."

            mc normal "Eu aposto que ainda vou entrar naquela cabecinha dela."

            "Ronaldo" "Opa. Pode entrar em outros lugares também, né?"

            mc envergonhado "Não sei do que você tá falando..."

            "Ronaldo" "A-ham! Sei..."
        "Não chama ela assim, mano.":


            mc serio "Não precisa chamar ela assim, mano."

            mc "A [w] tem aquele jeito, mas falar assim só piora as coisas."

            "Ronaldo" "Ei, ei. Calma ae, cara. Só tava brincando."

            mc "Tô ligado, mas não curto isso."

            "Ronaldo" "Beleza, não tá mais aqui quem abriu o bico."

            mc envergonhado "Valeu. Só não quero que ela se sinta pior, sabe."

            "Ronaldo" "Relaxa. O povo zoa um pouco ela, mas eu acho que tá todo mundo respeitando mais ela."

            "Ronaldo" "Ninguém quer admitir, mas ela vem fazendo um bom trabalho."

            mc normal "Que bom. Eu também acho isso, cara."

    "Ronaldo" "Bom. Vou indo nessa. Boa sorte com a chefinha."

    mc zerado "..."



    "Ronaldo" "Ah! Você ouviu sobre o aeroporto?"

    mc desconfiado "Pior que eu ouvi... mas o que tem?"

    "Ronaldo" "Parece que tá quase pronto. Isso vai ser grande, cara."

    mc normal "Pelo jeito vai ser mesmo."

    "Ronaldo" "Tem um rolo acontecendo aí dizendo que ele só não saiu ainda porque teve um ataque hacker durante a configuração do sistema deles."

    mc surpreso "Ataque hacker?!"

    "Ronaldo" "É. É só um boato. Não consegui confirmar nada, mas parece que um hacker teve acesso aos controles de voo."

    "Ronaldo" "Eles tão tentando descobrir a brecha que permitiu isso, mas até agora nada."

    "Ronaldo" "Se o que me falaram é verdade, até agora ninguém sabe como os hackers fizeram isso e eles não têm coragem de abrir assim."

    mc "Uou... se for verdade, quem será que fez isso?"

    "Ronaldo" "Sei lá, mas deve ser aquele tal de Anonymous que tanta gente fala."

    mc desconfiado "Cara... isso é velho pra caramba. Ainda existe esse negócio?"

    "Ronaldo" "Aí você já tá querendo saber demais. Eu falei que era só um boato. Eu não vou perder tempo com isso. Já tem coisa demais pra checar."

    mc envergonhado "Tem razão. Vamo focar no que importa."

    "Ronaldo" "Isso aí. Mas se você ouvir qualquer coisa sobre isso, me fala, tá? Daria uma boa matéria..."

    mc normal "Pode deixar. Bom trabalho."

    "Ronaldo" "Falou."

    hide ronaldo_andando with dissolve

    "Eu sinto que a redação tá mudando de uns tempos pra cá. As pessoas tão se falando mais, o ambiente melhorou."

    "Será que isso é culpa da [w]?"

    "Se for, ela tá fazendo um trabalho incrível."

    "..."

    j "Ei! Pombinho!"

    mc zerado "[j]..."

    j "Vem aqui."

    scene trabalho cassia with Dissolve(1.0)

    mc zerado "[j]... Você precisa mesmo ficar sentada como se tivesse na sua casa?"

    j "Que que tem?"

    mc desconfiado "Se a [w] te pegar, assim, ela vai ficar 10 minutos falando sobre a conduta correta no local de trabalho."

    j "Nem me fala dessa biscate."

    mc envergonhado "Ei. Calma ae."

    if sofia2_cassia:

        j "Ah! E eu sei que você tá de namorico com a pirainha."

        mc surpreso "E-eu?!"

        j "Vocês editaram minha matéria. Foi a primeira vez que isso aconteceu comigo."

        mc envergonhado "N-não foi nada pessoal, [j]. Todo mundo é igual aqui na re-"

        j "Você tá doido, pombinho?"

        mc "Oi?"

        j "As pessoas não são iguais no trabalho, não. A doida tá te contaminando."

        j "A gente sofre e sobe na empresa justamente pra ter poder e influencia. Não existe isso de todo mundo igual, não."

        j "Quem tá em cima manda em quem tá embaixo e isso é em todo lugar."

        j "Se você editar uma matéria minha outra vez, eu A C A B O com você. Entendeu?"

        menu:
            "S-sim, senhora...":


                mc "T-tá."

                j "Tá, o que?"

                mc preocupado "S-sim... senhora?"

                j "Melhorou."

        "Eu sabia que eu ia me ferrar quando eu decidi editar aquela merda de matéria..."

    j "Calma. Não te chamei aqui pra isso."

    mc envergonhado "O que foi então?"

    j "Eu tenho uma proposta."

    mc surpreso "P-proposta?"

    j "Sim. Não precisa ficar com medo. Você é um bundão, mesmo."

    mc zerado "Sei lá... vindo de você... vai saber."

    j "Vindo de mim o quê, pombinho? Só vem coisa boa de mim. Você sabe disso..."

    if cassia_e1 == "seducao":

        j "Aquele dia no meu apartamento você curtiu, não curtiu?"

        mc envergonhado "No seu apartamento..."

        j "Nem vem... você gostou de tudo. Até do que veio depois, né?"

        mc "Eu não lembro direito do que aconteceu..."

        j "Vai por mim, você achou incrível."

        mc "..."

    mc envergonhado "Vou acreditar em você..."

    j "Eu tenho uns amigos na Faux News e eles me chamaram para ir até lá como uma representante da revista."

    j "Eles querem mostrar a estrutura deles e quem sabe até propor uma parceria."

    j "Eu falei com o chefe, e ele não deu muita bola."

    mc desconfiado "Por que será? Parece algo legal..."

    j "Ele disse que a revista tá indo bem, e em time que tá ganhando não se mexe."

    j "Enfim... ele disse que se eu quisesse ir, ele não ia se opor, mas que ele não iria de forma alguma."

    mc zerado "Velho folgado..."

    j "O que você acha de ir até lá em nome da revista?"

    mc surpreso "Eu?!"

    j "Por que você precisa ficar surpreso com tudo? Você comeu merda?"

    mc zerado "Ei..."

    j "Então, vai querer ou não?"

    "???" "Sim! Ele vai!"

    j "Chegou a piranha que não foi chamada."

    w "[j]... o que eu te disse sobre sua postura aqui na redação?"

    j "Olha minha postura..."

    w "Dá licença, [mc]."

    mc surpreso "T-toda..."

    scene sofia_cassia_redacao with Dissolve(1.0)

    pause

    w "Você leu o memorando sobre roupas que são adequadas para trabalhar aqui?"

    j "Devo ter deixado passar, chefinha..."

    w "Você deixa passar TODOS! E não me chame de chefinha. Meu cargo é Coordenadora de Produção."

    w "A forma como você se veste... isso não é adequado. Você não vê que fica todo mundo olhando pra você?"

    j "E qual é o problema?"

    w "Como assim 'qual é o problema'?! Você quer ficar mostrando seus p... seus-"

    j "Meus peitos deliciosos para todos os homens que quiserem olhar? Bom... eu diria que sim."

    w "[j]! Por favor! Isso não é brincadeira!"

    j "Chefinha... você não entende, né? Isso seria bom pra você também, inclusive."

    w "Como?"

    j "Espera, deixa eu te explicar um negócio."

    j "Sensualidade é uma arma de manipulação muito poderosa, sabia? Ela é igual autoridade, por exemplo."

    j "O flerte é uma forma muito fácil de deixar qualquer homem submisso. Não precisa ser de verdade."

    j "Apenas deixe eles pensarem que você quer algo com eles. Fale manso, use roupas que mostrem um pouco de pele."

    j "Finja que você é uma bobinha e não percebe que eles tão te comendo com os olhos. Os homens adoram isso."

    j "Eles acham que tão tirando proveito da situação, e não percebem que são eles que são o gado e você a pastora."

    j "Quando eles estiverem vulneráveis, basta fazer o que quiser com eles. Entendido? Se quiser, posso escrever um memorando sobre isso."

    w "T-tá louca?!"

    "Essa [j] é um absurdo... Epa... será que ela usa isso comigo também?"

    mc desconfiado "..."

    w "Olha... eu entendo, [j]. O mundo não é fácil. Nem sempre as coisas são justas no trabalho. Eu sei que você tem suas razões..."

    w "Só que você não pode abandonar sua moral, sua ética, pra chegar onde você quer. Não importa o que você consiga, sempre vai ter um buraco dentro de você."

    j "Que fofinha... Não se preocupe comigo, chefinha. Eu não tenho nenhum buraco em mim, não. Pelo menos nenhum buraco que eu não queira ter."

    j "Ética... moral... compaixão... isso é desculpa de pessoas que têm medo de fazer o que precisam pra atingir seus objetivos."

    j "Homens são a maior escória do mundo. Mesmo quando estão com alguém, não aguentam não olhar, não desejar. São animais. Eles não têm moral."

    w "Então você vai fazer igual eles? Vai se rebaixar igual quem você tá criticando?!"

    j "Você não tá entendendo, benhê. Eu tô pouco me fodendo pros homens. Tenho dó das mulheres que acreditam que sua 'cara metade' não tá olhando pra outras."

    j "E parte disso nem é culpa deles. Eles são seres inferiores que não conseguem controlar seu instinto animal. Eu não tô nem aí pra isso."

    j "E por isso mesmo eu usarei todos que puder. Eu não preciso de homem, não preciso de 'companheiro'. Eu só preciso de idiotas que façam o que eu mando."

    w "Isso é nojento..."

    j "Veja, chefinha. Você pode falar o que quiser. Mas você não é muito diferente de mim."

    w "Eu não sou NADA como você!"

    menu:
        "Ixi... melhor tentar parar as duas.":


            mc normal "Ei, pessoal. Vocês sabem de uma coisa, né?"

            w "O quê?!"

            mc zerado "Eu sou homem... e vocês tão completamente me ignorando."

            j "Era só o que me faltava... ele ficou sentido..."

            w "Ai ai... Ele tá certo, [j]. Desculpa, [mc]."

            j "Você é MUITO tonta mesmo..."

            w "{i}Hmpf{/i}"
        "Vou ficar na minha...":


            $ sofia_e3_chocada = True

            "Melhor eu não falar nada... Isso é coisa delas."

            scene sofia_cassia_redacao2 with Dissolve(1.0)

            pause

            w "Ridículo você falar isso!"

            j "Você quer mandar em tudo, controlar tudo. Mas você se sente intitulada a isso pela sua posição. Você usa sua autoridade pra ter o que quer."

            j "Já eu, mesmo tendo poder aqui, nunca fiz isso. Eu consigo o que quero das minhas formas e você das suas."

            w "..."

            w "Querer colocar nós duas no mesmo pacote é muito baixo, [j]. Se você não liga de ser um monstro, pelo menos não se compare comigo e com os outros."

            w "Eu tô aqui pra fazer o certo! Eu faço tudo pelo bem da redação! Pra que a gente tenha orgulho do que faz aqui."

            w "Não é nada pessoal. Não é nenhum desajuste ou ambição particular. Totalmente diferente de você!"

            j "Será mesmo que você é tão benevolente assim? Será que não tem uma ponta do seu desejo nisso?"

            j "Será que você não sente um gostinho bom de ver todo mundo dançando a sua música?"

            w "Ridícula..."

            j "Talvez eu esteja certa? Por isso que você até perdeu a pose?"

            w "..."

            "Eita... acho que a [j] foi longe demais..."

    j "Bom... tudo isso começou com a intrometida da [w] que chegou sem ser convidada. Eu tava falando sobre a proposta da Faux News."

    w "Ah! E eu vim justamente porque você estava falando dessa proposta aí."

    j "É uma proposta para o [mc], não pra você."

    w "Eu sei, mas eu queria que o [mc] fosse e se ele não se incomodasse, gostaria de ir também."

    j "Não tem nada na Faux News pra você."

    w "Como não? Eles são a maior rede de notícias do país. Tem muito que a gente pode ver e aprender com eles."

    j "..."

    j "Eu não tenho nada com isso. Se o [mc] quiser ir e levar você com ele, a decisão é dele."

    j "Eles disseram que estarão esperando qualquer dia na parte da tarde."

    mc "Entendi... ir até a {b}Faux News, lá no centro, na parte da tarde{/b}."

    j "Isso mesmo."

    "Mas eu nem sei se eu quero ir..."

    w "Posso trocar uma palavrinha com você agora, [mc]?"

    mc normal "Ok."

    w "Estou lá fora."

    if cassia_seducao:

        scene cassia sentada_rindo with Dissolve(1.0)

        j "[mc]. Espera. Eu dei um belo presente pra vocês. Eu vou querer algo em troca."

        mc envergonhado "Presente? Eu nem sei se quero ir nessa visita..."

        j "Não importa. Toda essa conversa com a [w] me deixou excitada."

        mc surpreso "Como é?!"

        scene cassia sentada_provocando with Dissolve(1.0)

        j "Por que você não fecha a porta e vem aqui dar um jeito em mim?"

        mc envergonhado "Sério mesmo que você quer transar agora?"

        j "Você quer me comer ou não?"

        "Mas a [w]... caralho, e agora?"

        menu:
            "Foda-se. Vem aqui logo.":


                $ sofia_e3_transou = True

                mc safado "Que se foda, vem aqui logo."

                j "Assim que se fala, pombinho."

                mc "Opa, só deixa eu fechar a porta."

                j "Não quer que a coisinha veja você se divertindo?"

                mc "Melhor que ninguém veja."

                j "Tá. Agora vem."

                scene cassia_sala_mc_beijo with Dissolve(2.0)

                pause

                j "Hmmm... que gostoso."

                mc "Você é muito safada, [j]."

                j "Algum problema?"

                mc "Claro que não."

                j "Então cala a boca e aproveita."

                window hide

                pause

                j "Isso! Assim!"

                j "Tira logo minha roupa. Eu já tô pingando."

                scene black with Dissolve(1.0)

                j "Ai!"

                j "Isso, me lambe."

                "..."

                j "Tá bom, [mc]! Agora vem."

                scene cassia_sala_mc_sexo with Dissolve(2.0)

                pause

                mc "{i}Hmng{/i}"

                j "Isso!"

                j "Vem com força! Ai!"

                scene n3_premium26 with hpunch

                j "Faz gostoso!"

                mc "{i}Ah!{/i}"

                j "Pode gozar, pombinho!"

                scene n3_premium27 with hpunch

                mc "Aaahh!!!"

                mc "{i}puf puf{/i}"

                "..."

                mc tarado "Gostou?"

                j "..."

                scene black with Dissolve(1.0)

                scene n3_premium30 with Dissolve(1.0)



                j "Pode ir. Agora tenho que trabalhar."

                mc preocupado "Mas-"

                j "Tá tá. Você é incrível. Me deixou sem ar. Isso que você quer que eu fale? Tchau."

                mc zerado "..."

                "Por que eu sempre me sinto um objeto quando tô com ela?"

                "Merda! Tomara que a [w] não tenha ficado me esperando."

                "..."
            "Melhor eu ver o que a [w] quer.":


                $ sofia_amizade += 5

                mc envergonhado "Haha... melhor agora não, [j]. Vou ver o que a [w] quer."

                j "Faça o que quiser."

                mc angustiado "..."

                "Eu odeio quando eu não sei o que ela tá pensando... Ela vai me ferrar por isso."

                "Mas agora não adianta ficar pensando nisso."

                "Transar com a [j] aqui no trabalho, ainda mais com a [w] e os outros aqui, ia acabar com minha moral."

                "Eu preciso falar com a [w]."

                "..."
    else:


        $ sofia_amizade += 5

        scene cassia sentada_rindo with Dissolve(1.0)

        j "Vai lá com a chefinha, pode ir."

        mc desconfiado "?"

        j "Toda essa briga me deixou excitada, mas não quero nada com você. Tchau."

        mc surpreso "Ei!"

        scene trabalho angulo with hpunch

        "Ai! A [j] é doida."

        "Preciso falar com a [w] sobre essa visita."

    scene trabalho angulo with Dissolve(1.0)

    mc normal "[w]?"

    if sofia_e3_transou:

        show sofia seria with dissolve

        w "Nossa, [mc]... que demora..."

        mc envergonhado "Você ficou me esperando?"

        w "Claro. Eu queria falar sobre a tal proposta. O que tanto demorou lá?"

        mc "Ah, desculpa. Não foi nada..."

        w "A [j] é perigosa e mentirosa, [mc]. Não confie nela."

        mc "Pode deixar..."

        show sofia explicando with dissolve
    else:


        show sofia explicando with dissolve

        w "Oi. Queria falar com você sobre a proposta da [j]."

        mc normal "Certo."

    w "Então, eu não queria me intrometer nas coisas dela igual a [j] disse. Não era isso."

    w "Eu só queria aproveitar essa oportunidade de conhecer a Faux News. Acho que isso podia ser bom pra gente."

    menu:
        "Não liga pra [j]. Ela só quer te deixar nervosa.":


            mc normal "Não liga pro que ela fala. A [j] só quer te deixar puta e mexer com você."

            w "Não é tão simples assim, [mc]."

            mc desconfiado "Hm?"

            w "A [j] é uma mulher com uma visão muito definida da vida. Ela não é uma menina tonta que quer fazer birra."

            mc "Não?"

            w "Claro que não. Ela sabe muito bem o que quer. Mas isso não significa que a visão dela tá certa."

            mc envergonhado "E-entendi..."
        "Isso não importa. Eu não ligo pra o que os outros falam.":


            mc charmoso "Isso não importa. Eu não ligo pro que os outros pensam."

            w "Como não importa? Você não vive sozinho no mundo. Como seus companheiros de trabalho olham pra você importa, sim."

            w "Claro que você não vai viver em função deles, mas ignorar os outros é coisa de criança birrenta."

            mc envergonhado "Bom... se você acha isso. Mas não consigo me preocupar."

            w "Você é cabeça fresca demais, isso sim."

            mc "Talvez..."
        "Por que é uma boa ideia?":


            $ sofia_amizade += 1

            mc desconfiado "Entendi. Mas por que você acha isso tão importante?"

            w "Porque é uma chance de a gente ver uma empresa grande, uma das maiores se não a maior do país, por dentro."

            w "Entender como eles trabalham pode otimizar bastante nossa redação e aumentar nossa eficiência."

            mc zerado "Trabalho de novo, né?"

            w "Claro. O que mais seria?"

            mc "Realmente, pra você ficar empolgada desse jeito, tinha que ser alguma coisa assim..."

            w "Ei..."

    mc normal "Mas então a Faux News é grande desse jeito?"

    w "Com certeza. Seria uma chance de ouro pra gente."

    w "Você acha que eu posso ir com você? Se você quiser, claro."

    "Eu e a [w] saindo juntos? Parece uma boa oportunidade da gente se conhecer melhor."

    "Vai ser a primeira vez que a gente vai se falar fora da redação."

    "Se eu quero alguma coisa com ela, essa é uma chance que não dá pra perder."

    mc charmoso "Claro que pode vir."

    w "Que bom. Obrigada, [mc]. Vai ser muito importante, você vai ver."

    menu:
        "Vai ser legal sair com você.":


            mc charmoso "Vai ser bacana a gente sair juntos. Se ver fora da redação."

            w "Ei. Você entende que isso é estritamente profissional, né? É uma pesquisa de campo, nada mais."

            mc "Claro. Só tô comentando que vai ser legal fazermos isso juntos."

            w "Ok..."
        "Espero aprender bastante com isso.":


            $ sofia_amizade += 1

            mc normal "Tava meio em dúvida, mas acho que vai ser legal. Tô torcendo pra gente aprender algo bacana."

            w "Eu também. Mas aposto que alguma coisa a gente vai usar, porque eles não são os primeiros à toa."

            mc "Verdade. Pra chegar lá, com certeza várias coisas certas eles fazem."

    w "Então eu te encontro na entrada, tá? Lá na {b}Faux News, na parte da tarde{/b}."

    mc normal "Beleza. Eu pego o busão no ponto da ilha e vou pro centro. De lá dá pra ir andando."

    w "Tudo bem. Eu também ando de ônibus."

    mc "Então a gente se vê lá na parte da tarde."

    w "Tá bom. Até lá, [mc]."

    mc "Até."

    hide sofia with dissolve

    "Eu já assisti muito os noticiários da Faux News, e agora poder ver isso por dentro. Acho que vai ser algo massa."

    "Eles vão apresentar tudo pra gente. E tem aquele lance de proposta que a [j] falou... o que será que eles querem?"

    "Aliás, já passou do almoço. Se pá dá pra ir lá agora mesmo. Tenho que ver o melhor dia pra mim."

    $ tempo = 2

    jump call_cidade

label sofia_evento3:

    $ sofia_e3 = "evento"

    "..."

    "Deu a hora que eu e a [w] combinamos. Agora só esperar ela..."

    w "Finalmente você chegou."

    mc surpreso "S-sofia!"

    show sofia t_falando with Dissolve(1.0)

    w "Que foi? Por que você tá gritando?"

    mc envergonhado "Eu? É..."

    menu:
        "Por que você tá vestida assim?":


            $ sofia_amizade += 1

            mc desconfiado "Por que você se vestiu assim?"

            w "Como assim? A Faux News é uma empresa de grande renome, [mc]. Você não pode chegar de qualquer jeito."

            mc envergonhado "Eu tô com a roupa de sempre..."

            w "Tudo bem. Essa roupa é adequada, contanto que você esteja lavando ela sempre que necessário."

            mc zerado "Que comentário foi esse?"

            w "Hehe... Falo com todo o respeito, claro."

            mc "..."
        "Você ficou muito bem nessa roupa.":


            mc charmoso "Você ficou muito bem com essa roupa."

            w "O-obrigada, mas isso é meio inapropriado, [mc]. Não se esqueça que isso aqui não é um encontro."

            mc "Eu sei. Mas só tô falando o que eu achei. Isso não é crime, né?"

            w "Acho que não..."

    w "Então vamos? Quanto mais tempo tivermos lá, melhor."

    mc normal "Você realmente parece empolgada, hein?"

    w "..."

    mc "Ok, ok. Então, bora."

    hide sofia with dissolve

    "Mesmo com tudo o que a gente trabalhou juntos a [w] continua desse jeito."

    "Será que algum dia ela vai dar uma abertura?"

    mc envergonhado "Espero que sim... Mas por enquanto acho que tenho que ser o mais sério possível."

    mc zerado "E aguentar esse 'passeio escolar' da forma mais adulta possível."

    w "Vem logo, [mc]!"

    scene black with Dissolve(1.0)

    "..."

    "Recepcionista" "Ah! Vocês são da revista... sei. Vou levar vocês até a seção de jornalismo."

    w "Obrigada."

    "Recepcionista" "O senhor Luca Alighieri vai apresentar tudo para vocês."

    "Recepcionista" "Venham comigo por favor."

    "..."

    scene faux_redacao with Dissolve(1.0)

    pause

    "Recepcionista" "Aqui é o setor de jornalismo. Durante à tarde o pessoal está participando de reuniões ou na sala de edição."

    mc normal "Por isso que é melhor visitar essa hora?"

    "Recepcionista" "Isso. Vou falar com o senhor Luca para ele vir atender vocês. Só um segundo."

    w "Obrigada."

    mc normal "E aí? O que achou?"

    show sofia t_pensando with Dissolve(1.0)

    w "Interessante como eles fazem reuniões de pauta todos os dias. Isso é muito comum em lugares que trabalham com hard news."

    mc desconfiado "Hard news?"

    w "[mc]... certeza que você fez faculdade?"

    mc zerado "Claro que fiz."

    w "Então o que são hard news?"

    mc envergonhado "Hmmm..."

    menu:
        "Notícias grandes e de muita importância.":


            $ renpy.block_rollback()

            mc normal "São notícias bem grandes e que falam de coisas muito importantes, como guerras etc."

            w "..."

            show sofia t_brava with dissolve

            w "Quase... mas não é isso."

            mc envergonhado "Não é?"

            w "Claro que não!"

            w "Hard news não tem nada a ver com o tamanho e nem sempre precisa ser de 'muita' importância, como guerras."
        "Notícias diárias que aparecem com bastante frequência.":


            $ renpy.block_rollback()

            $ sofia_amizade += 1

            mc normal "Hard news são notícias do dia a dia com grande relevância, normalmente de política, crime etc."

            mc charmoso "O contrário de soft news, que falam mais de comportamento, arte e outras editorias especiais."

            show sofia t_sorrindo with dissolve

            w "Eu sabia que você ia acertar essa, [mc]."

            mc "Claro."
        "Matérias especiais que demoram bastante tempo para fazer.":


            $ renpy.block_rollback()

            mc normal "São matérias especiais, que a pessoa viaja e faz trabalho de campo e talz."

            show sofia t_brava with dissolve

            w "É totalmente o contrario, [mc]! Você tá brincando comigo?"

            mc envergonhado "Não tô, não..."

    w "Hard news são as notícias que fazem a maioria dos noticiários diários. São notícias de primeira necessidade."

    w "Editorias de política, polícia e grandes assuntos internacionais que você não pode deixar de noticiar."

    w "Elas são normalmente feitas na correria do dia a dia da redação e é bem diferente do que acontece na nossa redação."

    mc normal "Verdade."

    w "A gente trabalha com matérias mais rápidas no site, mas a maioria das pautas que você e os outros trazem levam bastante tempo."

    w "Como a gente não é publicado todo dia, dá pra apurar melhor as coisas e fazer matérias mais completas. Jornal de todo dia não tem essa liberdade."

    mc zerado "Mas o que adianta se a maioria do que a gente publica é coisa irrelevante sobre famosos?"

    show sofia t_pensando with dissolve

    w "É. Isso você tem razão..."

    w "É complicado isso, mas não adianta remar contra a maré. Se é isso que nosso público quer, é isso que a gente tem que oferecer."

    menu:
        "Você até parece um pouco a [j] falando assim...":


            $ sofia_amizade += 1

            mc envergonhado "Não sei... Você até parece um pouco a [j] falando desse jeito..."

            w "Quê?!"

            show sofia t_brava with dissolve

            w "Como assim?!"

            mc normal "A [j] sempre me disse que é importante a gente fazer o que é necessário pra conseguir o que a gente quer."

            mc "Não é um pouco parecido com o que você disse?"

            w "..."

            show sofia t_pensando with dissolve

            w "N-não sei..."

            w "Eu não vejo assim..."

            w "E-eu-"
        "Verdade. Esse é o nosso trabalho.":


            mc charmoso "É isso que a gente tem que pensar. Realizar nosso trabalho."

            w "A-acho que sim..."

            mc desconfiado "O que foi?"

            w "Não, nada... só tava pensando que esse jeito de pensar..."

            w "Por que a gen-"

    "???" "Perdão pela demora."

    mc desconfiado "Hm?"

    show sofia t_sorrindo with dissolve

    w "Boa tarde, Senhor Luca."

    show sofia t_sorrindo at esquerda with move

    mc surpreso "!"

    show luca ola with dissolve

    lu "Muito prazer, meu nome é [lu] Alighieri. Eu sou apresentador da Faux News."

    mc "Vo-você!"

    "O homem que apresenta o noticiário! É ele mesmo!"

    show luca ola at direita with move

    w "Obrigada por receber a gente. Eu sei que não é fácil."

    lu "Não precisa agradecer. É sempre um prazer ter jovens profissionais aqui."

    w "Haha... obrigada. O senhor é muito gentil."

    lu "E você é muito educada. É um comportamento raro nos jovens de hoje."

    w "Parece que as novas gerações perderam um pouco a noção. Mas, sendo sincera, eu me sinto mais da sua geração do que a dos jovens."

    lu "Isso é muito bom, senhorita. Vejo que vamos nos dar muito bem."

    "Ei. Parece que tá rolando um clima aqui..."

    menu:
        "Enfim! Viemos conhecer o trabalho de vocês.":


            mc bravo "A-rrãm! Então! A gente veio conhecer o trabalho da Faux News. A [j] disse que vocês tinham aberto essa oportunidade pra gente."

            lu "Ah? Ah, sim! Claro!"
        "Não vou me intrometer":


            $ sofia_amizade += 1

            "Deixa eles conversarem... a [w] parece tão empolgada."

            w "Eu conheço seu trabalho há muitos anos. Desculpa falar assim, mas o senhor foi uma inspiração pra mim."

            lu "A senhorita está me bajulando demais... vai me deixar sem jeito."

            w "O senhor deve ouvir isso toda hora."

            lu "Mas é diferente vindo de uma companheira de profissão."

            w "Hehe... ok..."

            lu "Muito bem. Não tenho muito tempo. Vocês vieram a pedido da [j], certo?"

            mc normal "Isso."

    show sofia t_falando with dissolve

    w "Isso é verdade..."

    w "Você e a [j] se conhecem?"

    lu "Sim. A [j] é uma conhecida do ramo. Nós nunca trabalhamos juntos, mas acabamos nos conhecendo com o passar dos anos."

    lu "A capital parece grande, mas certos círculos acabam ficando restritos."

    mc desconfiado "Certos círculos..."

    w "Entendo..."

    lu "Vamos conhecer tudo então?"

    mc normal "S-"

    w "Com certeza."

    lu "Pois então venham comigo."

    scene faux_computadores with Dissolve(1.0)

    pause

    lu "Aqui está vazio agora pois a equipe está discutindo os assuntos do jornal da noite. Mas normalmente aqui é uma loucura."

    lu "Pessoas correndo, gritando, principalmente quando temos que parar a programação habitual para algum assunto urgente."

    mc normal "Como vocês ficam sabendo das coisas primeiro?"

    lu "Como?"

    w "{size=17}[mc]...{/size}"

    show luca falando with dissolve

    lu "Verdade. Perdão. Eu esqueço que vocês trabalham em uma revista e não com noticiários diários."

    lu "As notícias chegam de várias fontes. Polícia, correspondentes, fontes primárias e outros."

    lu "Ter fontes é imprescindível para se tornar um bom jornalista."

    mc normal "E como você faz para encontrar pessoas que tenham algo a dizer e fazer elas confiarem e contarem coisas pra você?"

    lu "Bom... na faculdade você deve ouvir que é importante proteger as fontes, ser honrado etc... mas isso é quase 100%% balela."

    mc desconfiado "Como assim?"

    lu "Quase todas as fontes te passam informações por benefício próprio. Ou por dinheiro ou porque elas ganharão algo com a notícia indiretamente."

    lu "Ninguém tá nem aí com a verdade ou com o interesse público. E nós também."

    w "?"

    lu "Não importa se alguma notícia é realmente importante. Se nós acharmos que ela fará as pessoas trocarem de canal, ela não entra."

    w "M-mas, senhor [lu]. E se for algo realmente importante pra elas? Não é nossa obrigação informar?"

    lu "Veja, jovem. Nossa primeira obrigação é com os investidores da Faux News. Eles colocaram e ainda colocam dinheiro pra criar e manter tudo isto."

    lu "A gente precisa garantir que eles recebam um retorno também. E pra fazer isso é preciso agradar anunciantes, que é o que traz o dinheiro."

    lu "Por isso, as notícias precisam ser muito bem pensadas, pra garantir o maior número de telespectadores possível."

    w "..."

    mc normal "Entendi. E se acontecer de alguém que anuncia aqui fazer algo de errado. Como vocês lidam com isso?"

    lu "Abafamos, obviamente. A regra número um é não mexer com quem coloca a comida na mesa, entende? Estamos todos no mesmo time."

    mc envergonhado "C-certo..."

    "Como ele fala uma coisa dessas de forma tão natural?"

    w "..."

    lu "Eu sei que pode ser um pouco chocante pra quem tá saindo agora da univerdade, mas minha proposta é apresentar a realidade pra vocês."

    mc normal "Claro. Eu agradeço pela honestidade."

    lu "Agora venham."

    hide luca with dissolve

    "..."

    scene faux_bancada with Dissolve(1.0)

    pause

    lu "Aqui é onde a magia acontece."

    lu "Olhando assim, como um todo e longe da TV, parece bem menos imponente, não parece?"

    mc normal "Pra falar a verdade, parece até mais."

    show luca falando with dissolve

    lu "Interessante. E você, jovem?"

    w "Ah? Eu?"

    lu "Está conseguindo acompanhar?"

    w "Ah! Claro. Desculpe. Estava pensando no que o senhor tá explicando."

    lu "É bastante coisa pra assimilar, relaxe."

    w "Sim. Obrigada."

    lu "Eu sou o apresentador, mas também o editor chefe de jornalismo. Ou seja, eu tenho palavra final em todas as notícias."

    lu "É minha responsabilidade garantir que o melhor jornalismo seja feito na Faux News."

    mc normal "Caraca. Não é coisa demais, não?"

    lu "Com certeza. Mas depois de anos, a gente acostuma. Claro que isso acaba se tornando sua vida. Entretanto, tem seus pontos positivos também."

    lu "Agora venham."

    hide luca with dissolve

    "..."

    scene faux_telao with Dissolve(1.0)

    pause

    lu "Aqui é onde acontece a previsão do tempo e outras editorias, tipo esportes. O apresentador fica de pé, é mais dinâmico e normalmente mais voltado pros jovens."

    mc desconfiado "Por que jovens?"

    lu "Cada público tem suas características. Os jovens de hoje são muito mais dinâmicos e têm menos capacidade de concentração."

    lu "A forma que os programas eram feitos no passado, não funciona mais. A maioria dos jovens preferem programas mais dinâmicos e menos formais."

    lu "Obviamente fazemos pesquisas para descobrir o que as pessoas querem ver e então criamos os formatos com base nessas informações."

    mc envergonhado "Nunca ninguém me fez pergunta nenhuma..."

    lu "Haha... não é como você está pensando."

    mc desconfiado "Não?"

    lu "Nós obtemos informações por meio de aplicativos ou sites. Sabe aqueles termos que você tem que aceitar sempre antes de usar um app?"

    mc zerado "Sei..."

    lu "Nós coletamos dados de milhares de pessoas e então usamos aquilo para melhorar nossos programas e repassar para os anunciantes."

    mc desconfiado "Então vocês tão passando minhas informações pra anunciantes?"

    lu "Claro. É dessa forma que sites, aplicativos e programas conseguem apresentar anúncios relevantes para as pessoas."

    w "Senhor [lu]. E a privacidade das pessoas? Nem todo mundo sabe que os dados deles estão sendo usados pelas empresas..."

    lu "Você acha que as pessoas ligam pra isso? Ninguém lê os termos mesmo. E mesmo que eles olhassem, vai deixar de usar por causa disso? Claro que não."

    lu "Isso é excelente pra nós. Não é à toa que Google, Facebook e outras empresas que trabalham com dados são as mais ricas hoje em dia."

    lu "Informações sobre hábitos, gostos e o que move o público é de extremo valor para empresas e partidos políticos."

    w "Puxa..."

    lu "Vocês vão ver que no mundo adulto as coisas são diferentes do que nos filmes de fantasia. O bem e o mal se confundem. Nada é tão claro."

    lu "Agora quero mostrar um último lugar. Aqui do lado."

    "..."

    scene faux_poltronas with Dissolve(1.0)

    pause

    lu "Aqui."

    show luca ola with dissolve

    lu "A última parte do estúdio é este confortável local onde apresentamos alguns programas matutinos e de entrevistas."

    lu "Normalmente o apresentador e entrevistados ficam sentados lado a lado, em um clima mais informal e aconchegante."

    lu "Mas não adianta eu falar muito agora. O negócio é vocês sentarem e sentirem como é."

    mc surpreso "A gente pode?!"

    lu "Claro. Fiquem à vontade."

    lu "Inclusive, ainda faltam uns 30 minutos para terminar a reunião, eu vou deixar vocês aqui sozinhos tranquilos."

    lu "Podem andar pelo lugar, conhecer as coisas. Vocês são nossos convidados."

    lu "Assim que a reunião acabar eu volto e conversamos sobre uma proposta que a [j] deve ter mencionado."

    mc normal "Sim."

    lu "Então fiquem à vontade. Volto logo."

    mc "Até."

    w "..."

    hide luca with dissolve

    "..."

    mc desconfiado "Você tá legal, [w]?"

    show sofia t_pensando with dissolve

    w "Hm?"

    mc desculpa "Você ficou quieta durante a visita. Você não gostou?"

    w "Não é isso... eu só... Deixa pra lá."

    menu:
        "Ok. E o que você quer fazer agora?":


            $ sofia_amizade += 1

            mc normal "Beleza. E o que você quer fazer agora?"

            w "A gente tem que esperar ele, né?"

            mc "Sim."
        "Calma. Fala pra mim. O que foi?":


            mc preocupado "[w]... o que aconteceu? Fala pra mim."

            w "É coisa minha, [mc]. Me deixa, poxa."

            mc "Calma aí. Só tô preocupado contigo. O que foi?"

            w "Não é nada da sua conta..."

    w "..."

    "Certeza que tem alguma coisa muito estranha com a [w]."

    "Acho que ela não tava pronta pra saber de todas as maracutaias que esses caras fazem..."

    w "Esse cara..."

    mc desconfiado "Oi?"

    show sofia t_brava with dissolve

    w "Esse cara é um nojento!"

    mc surpreso "Quem?!"

    w "Esse [lu] Alighieri, quem mais?!"

    w "Falando essas coisas como se fossem normais! Isso é ridículo!"

    mc envergonhado "Sabia..."

    w "E você?! Como pôde ficar quieto e aceitar tudo?!"

    w "Você concorda com ele, [mc]?!"

    mc preocupado "Eu?!"

    "Ixi... é melhor eu tomar cuidado com o que eu vou falar agora. Tá fácil dela jogar toda essa merda pra cima de mim."

    menu:
        "Óbvio que tá errado! Isso estraga nossa profissão.":


            $ sofia_amizade += 1

            mc bravo "Claro que tá errado. Colocar o dinheiro na frente de tudo o que a gente aprende como bom jornalismo."

            mc concentrando "Ainda mais sendo uma empresa gigante como esta..."

            show sofia t_pensando with dissolve

            w "É mesmo, não é?"

            mc normal "Claro. Primeiro lugar é fazer a coisa certa."

            w "T-também acho..."
        "Não sei se é uma questão simples assim...":


            mc envergonhado "Bom... eu sei que é errado, mas não acho que dá pra simplificar isso só em certo ou errado."

            w "Como assim?!"

            mc desculpa "Pensa... eles empregam dezenas, talvez centenas de pessoas. Se eles acabassem, o que aconteceria com essas pessoas?"

            mc "E querendo ou não, eles também fazem bom jornalismo na maior parte do tempo. O que aconteceria se eles sumissem?"

            show sofia t_pensando with dissolve

            w "Você não tá pensando direito..."

            mc "Talvez, mas nada é tão simples."

            w "..."

    "Não deve ser só o lance da Faux News. Tem alguma outra coisa acontecendo. O que será?"

    w "Eu não quero mais ficar aqui. Podemos ir, [mc]?"

    mc desconfiado "Mas e a proposta? Ele falou que ia voltar em meia hora."

    w "Eu sei... mas eu queria ir... posso?"

    mc preocupado "Ei. Eu nem tava afim de vir, eu vim mais por você. Sacanagem você ir agora."

    w "Eu sei. Desculpa... mas eu realmente não estou me sentindo bem."

    w "Tô me sentindo até um pouco zonza."

    mc "Isso é perigoso, [w]. Senta aqui."

    w "T-tá."

    hide sofia with dissolve

    mc "Vem."

    scene sofia_faux_sentada with Dissolve(1.0)

    w "Obrigada. Minha cabeça tá pesada e eu não tô respirando direito."

    mc preocupado "Nossa. Isso parece sério, [w]. Quer que eu chame ajuda?"

    w "Não! Não precisa. Sentar foi uma boa ideia."

    "..."

    "Ela não tá legal..."

    mc desculpa "Tá melhor?"

    w "Acho que sim..."

    mc normal "Ele ainda vai demorar uns minutos. Por que você não tira o sapato? Talvez ajude."

    w "Quê?! Que tipo de sugestão é essa, seu bocó?"

    mc zerado "Bocó? Bom... se você não quer melhorar..."

    w "..."

    w "Tá bom."

    mc surpreso "Como?! Você realmente aceitou uma sugestão?!"

    w "..."

    scene sofia_faux_mc1 with Dissolve(1.0)

    w "Pronto."

    mc "E aí? Melhorou?"

    w "Pra ser sincera... melhorou."

    mc "Hah! Eu sou um gênio."

    w "Você é um bocó, isso sim."

    mc "Mas o que aconteceu?"

    w "Não sei exatamente também. Acho que foi o que o Sr. [lu] falou."

    mc "Ele foi bem sincero..."

    w "Acho que no fundo eu que tava errada. Eu esperei demais desse lugar."

    w "Uma vez eu li que somos nós que causamos nossa própria frustração, não tem nada a ver com os outros."

    mc "Por que?"

    w "Porque frustração é quando a gente coloca esperança demais em uma coisa, e quando vemos a realidade, não é como a gente tinha imaginado."

    w "Quando isso acontece, toda a diferença entre o que a gente esperava e o que realmente é vira frustração."

    mc "Você tá querendo dizer que se eu espero ser uma pessoa rica, linda e bem sucedida no futuro, quando finalmente chegar a realidade..."

    mc "Você já tá me deixando frustrado só de pensar!"

    scene sofia_faux_mc2 with Dissolve(1.0)

    w "Você acha que pessoas que tentam fazer o certo estão erradas?"

    w "Seja sincero, por favor. Você acha que o mundo é dos espertos? Que a gente tem que fazer o que for preciso pra se dar bem?"

    mc "Não é um assunto simples, né?"

    w "Eu sei. Mas só me responde... O que você acha que vem na frente? Se dar bem ou fazer o certo?"

    menu:
        "Desculpa, mas eu não quero responder isso.":


            mc "Desculpa, só que eu não vou responder isso agora, assim."

            w "Mas-"

            mc "[w]."

            w "Ok..."

            w "Eu esperava uma posição de você, [mc]."

            mc "Talvez um dia, com mais tempo, em outro lugar a gente pode falar sobre isso."

            w "Ok..."
        "Eu acho que a gente precisa pensar na gente primeiro.":


            $ sofia_amizade += 1

            mc "Vou ser honesto com você. Eu acho que o mundo não é fácil. Tipo a lei da selva, 'a sobrevivência do mais forte'."

            mc "A gente precisa pensar em nós mesmos, porque no mundo tá cheio de gente pensando a mesma coisa. Querendo se dar bem."

            mc "Se você não aproveitar as oportunidades, mesmo que às vezes não seja o certo 'certo', eu ainda acho que tá valendo."

            w "..."

            w "Obrigada por ser sincero comigo, [mc]."

            w "Eu não concordo com você. Eu acho que conseguir as coisas deixando de lado o que você acredita só vai complicar sua cabeça pro futuro."

            mc "Tipo ter que se acertar com Deus, algo assim?"

            w "Não. Não tô falando disso. Tô falando que a gente se sente pior quando olha pra trás e começa a perceber que a gente fez merda."

            w "Quanto mais a gente faz coisa errada, mais a gente vai fazendo e a vida parece que fica complicada."

            mc "Talvez..."

            w "Mas eu não quero ficar julgando. E obrigada de novo por falar a verdade, mesmo sabendo que eu não pensava igual você."

            mc "Relaxa."
        "Eu acho que fazer 'o certo' é o certo.":


            $ sofia_amizade += 1

            mc "Pra mim, não tem desculpa. Fazer o certo é o certo e pronto."

            mc "Não adianta ficar procurando desculpa. Se você fez algo errado, assuma e pronto."

            w "Você acha isso mesmo?"

            mc "Claro. Nem sempre a gente consegue fazer o certo, a gente é humano, certo? Mas a gente tem que pelo menos assumir nossos erros e tentar melhorar."

            mc "Procurar ser mais éticos a cada dia. Não se aproveitar das pessoas, ser honesto, verdadeiro. Não é fácil, mas é o certo."

            w "É assim que eu penso também, [mc]. Foi o que eu sempre quis fazer."

            mc "Eu sei. Até um pouco demais rs..."

            w "..."

    mc "Tudo isso... tem a ver com o que a [j] falou hoje?"

    w "Não! Digo..."

    w "Talvez..."

    if sofia_e3_chocada:

        mc "Eu devia ter parado vocês, né?"

        w "Não. De jeito nenhum. Eu não preciso que você 'me proteja' das coisas. Eu sou sua chefe, inclusive."

        mc "Ok..."

        w "Só que..."

    w "O que ela disse, que eu sou parecida com ela... Isso é impossível..."

    scene sofia_faux_mc3 with Dissolve(1.0)

    pause

    w "Você é a pessoa que eu mais tenho conversado na redação, [mc]."

    w "E como minha vida é praticamente trabalho, você é a pessoa que eu mais converso, ponto."

    mc "E isso é bom ou ruim?"

    w "Hmm..."

    if sofia_amizade >= 16:

        $ sofia_e3_good = True

        w "Isso é algo que eu nunca pretendi admitir pra você, mas como a gente não tá no trabalho, eu vou falar."

        w "Eu acho sua personalidade incrível."

        mc "Sério?"

        w "Sim. Você é um homem que eu aprendi a admirar."

        w "Seu profissionalismo e sua compostura. Você não faltar com respeito e não ficar de gracinha."

        if sofia_e2_good:

            w "Não foi à toa que eu te chamei de amigo aquela vez..."

            mc "Você ainda lembra disso?"

            w "Claro! Não seja bocó... eu não falei aquilo da boca pra fora."

            mc "Haha... ok."

            mc "Depois de todos aqueles dias trabalhando juntos também..."

        if sofia_e1_massageou:

            w "E não é só isso. Eu ainda deixei você me massagear aquela noite."

            w "Eu nunca nem sequer tinha pensado em deixar alguém fazer algo assim, ainda mais no trabalho."

            w "Isso mostra o quanto eu confio em você."

            w "E desde aquele dia você nunca me decepcionou."

        if sofia_amizade >= 29:

            w "Eu não entendo como isso acontece, mas você é perfeito..."

            mc "Perfeito?"

            w "Não teve uma vez que você fez algo que eu não aprovasse. É até estranho... como se você pudesse... deixa pra lá, é loucura."

            mc "Fala."

            w "É como se você pudesse saber como eu ia reagir e escolhesse a melhor alternativa."

            mc "Que doideira..."

            w "Eu falei. Mas enfim..."

            w "[mc], você é mais do que eu podia esperar de um companheiro. Você é um verdadeiro parceiro, [mc]. O cara que eu sempre sonhei que existisse."
        else:


            w "Você não é perfeito, ninguém é, mas é mais do que eu podia esperar de um companheiro. Você é um verdadeiro parceiro, [mc]."

        mc "Obrigado, [w]. Eu fico feliz de saber que você confia em mim."

        mc "Eu gosto da sua companhia e acho você uma mulher incrível."

        mc "O jeito que você encarou a redação de cabeça erguida e mesmo com todo mundo indo contra você no começo, você não desistiu."

        mc "E agora tá aqui. Sempre pensando em fazer o melhor, fazer o certo."

        mc "Você é, de verdade, uma inspiração pra qualquer profissional."

        w "!"

        w "Muito obrigada, [mc]... não quero ficar emotiva, mas... isso significa muito pra mim."

        "A [w] é uma garota incrível. E ela é determinada e confiável. Além de tudo ainda é bonita."

        "Ela seria um partidão, com certeza."

        "E do jeito que ela falou... parceiros... será que ela tá na minha mesmo?"

        "Ela disse que eu sou a pessoa que ela mais conversa... e tipo... ela é uma pessoa como todo mundo. Talvez... talvez eu tenha uma chance."

        "A gente tá tão perto agora... Eu não vou ter outra chance com ela tão cedo. Será que eu devia arriscar um beijo agora?"

        "Será mesmo? Se isso não der certo... eu posso jogar tudo o que eu conquistei com ela fora..."

        "O que eu faço?!"

        menu:
            "Beijar ela":


                $ sofia_beijo = True
                $ sofia_namorar = True

                "Não adianta ficar pensando demais. Nessas horas o que vale é a iniciativa."

                mc "[w]... você falou em parceiro. E eu vejo você assim também. Uma parceira."

                w "Que bom."

                mc "Então... Posso fazer uma coisa?"

                w "Hm? Com-"

                scene sofia_faux_beijo with Dissolve(2.0)

                pause

                w "!"

                w "[mc]!"

                mc "É só um bei-"

                scene faux_poltronas with vpunch

                mc "[w]! Calma!"

                show sofia t_incerta with dissolve

                w "P-por que você fez isso?"

                mc angustiado "E-eu pensei que-"

                if sofia_amizade >= 29:

                    w "E-eu não sei o que pensar, [mc]."

                    w "Você sempre foi incrível comigo... agora isso..."

                    mc preocupado "[w]..."

                    w "Eu gostei... quero dizer! Meu Deus, o que eu tô falando?!"

                    w "Eu preciso pensar, por favor dá licença."
                else:


                    w "Pensou o quê?! Só porque eu vejo você como um bom companheiro, quer dizer que você pode me beijar?"

                    mc desculpa "Desculpa, só achei que fosse o melhor momento..."

                    w "Por que eu estou vulnerável? Por isso?"

                    w "Você não tem respeito pelas pessoas, [mc]?"

                    w "Se aproveitar de uma mulher que tá confusa pra dar em cima? É isso?!"

                    mc angustiado "Não! Claro que não!"

                    mc desculpa "Não é nada disso, [w]. Eu só achei que nossa conversa tava ficando mais pessoal e eu pensei que talvez você também quisesse."

                    w "..."

                    w "Talvez eu quisesse mesmo... mas não assim..."

                    w "Nem pense em mencionar isso na redação. Eu vou tratar você normal, como se isso nunca tivesse acontecido."

                    w "Mas a gente vai conversar sobre isso depois. Não ache que tá tudo bem!"

                    mc "Tudo bem. Desculpa mesmo."

                    w "[mc]..."

                    w "Eu acho que vou embora. Desculpa..."

                hide sofia with dissolve

                mc surpreso "[w]!"

                "Ela saiu..."

                "O que eu fiz?! Será que eu estraguei tudo?"

                if sofia_amizade >= 29:

                    "Ela disse que gostou... mas então por que?"
                else:


                    "Ela disse que talvez também quisesse... mas depois dessa... e agora?"

                "Calma, [mc]... você fez o que achou que era certo. Não adianta chorar agora."

                "É verdade. Eu tenho que assumir o que eu fiz e seguir adiante."

                "Pelo que ela disse... talvez ela também sinta algo por mim..."

                "Eu tenho que d-"

                lu "Olá."

                mc surpreso "!!"
            "Não beijar":


                "Melhor não... as coisas tão indo bem com ela."

                "E além disso eu ainda não sei o que eu quero com a [w]. Será que eu realmente quero algo a mais?"

                jump sofia_e3_continua
    else:


        w "Eu vou falar uma coisa que eu nunca falaria, mas é porque a gente tá fora do ambiente de trabalho."

        mc "Ok."

        w "Você tem sido um cara bacana e atencioso, mas é meio sem noção às vezes."

        mc "Sério? Haha..."

        w "Mas você sempre foi muito educado e nunca cruzou a linha. Eu me sinto à vontade com você, não tanto, mas me sinto."

        mc "Hmm... parece bom."

        w "Você poderia ser um pouco mais maduro e profissional."

        w "Mas olha, não quero que veja isso como dicas de coach ou algo assim. Só estou sendo sincera com você."

        mc "Relaxa."

        "Eu esperava um pouco mais. Talvez se eu tivesse agido diferente com ela em alguns pontos hoje..."

        if sofia_e3_transou:

            "Com certeza ter transado com a [j] lá na redação deve ter feito eu perder alguns pontos..."

        "Se eu pudesse voltar no tempo... talvez eu tivesse uma chance de passar mais confiança pra [w]."

        "Quem sabe até não podia rolar alguma coisa..."

        "Mas enfim. Pelo menos ela disse que se sente à vontade e eu não fui tão sem noção assim."

        "Eu também tenho que decidir o que eu quero com ela. Eu nunca pensei nisso..."

        label sofia_e3_continua:

            "Essa é uma escolha muito importante que vai influenciar como nossa relação vai se desenvolver a partir daqui."

        "Será que eu quero namorar a [w]?"

        menu:
            "Sim. Eu quero namorar com ela":


                $ sofia_namorar = True

                "Sim. Eu quero ir mais à fundo com ela."

                if priscila_namoro or sayuri_namoro or julia_namoro or maria_namoro or nathan_namoro:

                    "Droga... eu já tô em um relacionamento e mesmo assim quero namorar a [w] também..."

                    "Por que tem tantas pessoas irresistíveis na minha vida?"
                else:


                    "Eu ainda não tô namorando ninguém. Seria legal ter alguém como ela do meu lado."
            "Não. Eu prefiro apenas amizade":


                "Nah. Eu não vejo ela assim. Ela é só uma grande amiga e companheira de trabalho que eu quero conhecer melhor, mas não com segundas intenções."

                if priscila_namoro or sayuri_namoro or julia_namoro or maria_namoro or nathan_namoro:

                    "Inclusive, eu já tô namorando, então é melhor eu me comportar hehe..."
                else:


                    "O duro é que eu ainda não namoro ninguém. Tomara que eu consiga me relacionar com a pessoa certa..."

        mc "O [lu] tá demorando..."

        w "Sim..."

        w "Mas foi legal poder conversar com você, [mc]."

        mc "Eu também gostei."

        w "Eu acho que não dá pra gente decidir esse negócio de certo ou errado assim, de uma hora pra outra."

        w "E eu não posso mudar quem eu sou em um dia. Principalmente por causa do que as outras pessoas falam."

        mc "Concordo."

        scene faux_poltronas with Dissolve(1.0)

        w "Upa."

        show sofia t_sorrindo with dissolve

        w "Eu vou continuar sendo a mulher certinha que vocês conhecem. A chefinha rs..."

        mc zerado "Que bom..."

        w "Mas eu preciso descobrir o porquê de eu ser assim. Eu preciso ter certeza do que eu sinto."

        w "Ser 'certinho' só por ser ou porquê alguém falou que é assim que tem que ser não é o suficiente. Eu quero descobrir mais sobre mim."

        w "E a não ser que eu descubra o contrário... acho bom vocês dançarem conforme a música na redação."

        mc angustiado "Pode deixar!"

        w "{i}Rsrs{/i}"

        w "A gente vai deixar aquela redação no esquema, [mc]. Eu conto com sua ajuda."

        mc charmoso "Pode deixar."

        show sofia t_falando with dissolve

        w "E eu cansei dessa Faux News. Eles que vão pro inferno."

        w "Se você quiser ficar aí, pode ficar, mas eu vou embora. Se eles não gostarem, tô pouco me lixando."

        w "Você vai ficar pra ouvir a proposta deles ou vem comigo?"

        "Agora que eu já tô aqui, eu não ligaria de ouvir a proposta deles..."

        mc normal "Eu vou ficar. Vou quebrar essa pra gente."

        w "Eu estou brava com eles agora, mas acho que é o melhor mesmo."

        show sofia t_sorrindo with dissolve

        w "Obrigada, [mc]. Depois a gente marca algo fora do horário de trabalho e você me conta em detalhes."

        mc charmoso "Ok, pode deixar."

        w "Até mais."

        mc "Até."

        hide sofia with dissolve

        "..."

        "Mesmo com toda a pompa, a [w] é uma pessoa bacana."

        "Bem que o apresentador podia chegar em 3... 2... 1..."

        mc charmoso "Agora!"

        mc zerado "Claro que não ia funcionar..."

        lu "Funcionar o quê?"

        mc surpreso "!"

    show luca ola with dissolve

    lu "Desculpe a demora."

    mc normal "De boa."

    lu "E a sua amiga?"

    "Você foi com a cara dela, né? Safado..."

    mc charmoso "Ela tinha muito trabalho na redação, daí eu falei pra ela ir que eu ficaria aqui pra discutir a proposta."

    lu "Uma pena... mas tudo bem. Vamos falar de negócios. Sente aqui."

    mc "Tá."

    scene luca_faux_mc with Dissolve(1.0)

    lu "Você que é do ramo sabe que a Faux News é a maior empresa jornalística do país. Nosso canal é apenas uma das extensões da nossa companhia."

    lu "Nosso portal na internet, emissoras de rádio e outras plataformas são, juntas, a maior fonte de notícias do país."

    mc "Isso é incrível."

    lu "Sim. Nós controlamos boa parte do que a capital e o país como um todo pensa. Esse é um poder e também uma grande responsabilidade."

    lu "Entretanto, existe uma área que nós ainda não conseguimos penetrar. Já tentamos por anos, mas sem sucesso."

    lu "Que é a das revistas semanais de variedade. Nossos concorrentes nessa área nos pisoteiam sempre que tentamos."

    mc "Entendo..."

    lu "Já perdemos muito dinheiro nessa brincadeira e os investidores não querem tentar novamente. Mas eu não estou pronto pra desistir."

    mc "O que o senhor pretende fazer?"

    lu "Bom... é aí que você entra."

    mc "Eu?!"

    lu "Eu e a [j] já discutimos isso algumas vezes, e estamos preparando terreno para o próximo passo."

    lu "Ela tem certa confiança em você e disse que quer trazer você para a roda."

    mc "Não sei se eu entendi..."

    lu "Seu nome é [mc], certo?"

    mc "Isso..."

    lu "Veja, [mc]... a Faux News quer adquirir a sua revista."

    mc "Sério!?"

    lu "Mas o editor chefe atual não quer fazer negócio e os donos da revista fazem o que ele manda."

    lu "Eu já tentei falar com ele, a [j] também, mas ele é irredutível."

    "Então o chefe não quer que vendam a revista..."

    lu "Fizemos inclusive uma proposta muito maior do que o razoável, e mesmo assim ele recusou."

    mc "Velho teimoso..."

    lu "Exatamente. Então, talvez, você possa nos ajudar a facilitar essa transação."

    mc "Não sei, não... Não acho que eu tenha qualquer influência com o velho."

    lu "Talvez não você... mas quem sabe a-"

    mc "[w]?!"

    lu "Você é inteligente afinal de contas."

    lu "A garota parece confiar bastante em você."

    mc "Como você sabe isso?"

    lu "Não é óbvio? Você fez a garota tirar os sapatos..."

    if sofia_beijo:

        lu "E aquele beijo..."

    mc "C-c-como?!"

    lu "As câmeras estavam ligadas, [mc]. Eu vi tudo."

    menu:
        "Essa foi boa...":


            mc "Hah! Quem diria... você não brinca em serviço..."

            lu "Eu precisava ter certeza da sua influência com ela antes de conversar contigo."
        "Isso é um absurdo!":


            mc "Você tá louco?! Isso é um absurdo!"

            lu "Tenha calma. É tudo por um objetivo maior."

            "Esse cara..."
        "...":


            mc "..."

            lu "Não precisa ficar assim."

    lu "Tudo foi por um bem maior."

    lu "[mc]... existe uma sombra nesta cidade. Uma sombra que vem de cima e cobre toda a ilha, toda a parte continental da capital."

    mc "Sombra?"

    lu "Ela está no topo dos edifícios e nas vielas do Distrito. E mesmo assim ninguém vê o que a projeta."

    mc "?"

    lu "Só quem está acima do nível da cidade pode ver de onde vem a sombra. E, pode acreditar em mim, são poucos que estão lá."

    lu "Não precisa me responder nada agora. Pense e preste atenção. Você verá a sombra em vários lugares."

    lu "Na próxima vez que conversarmos, quero que você preste atenção no que eu vou lhe oferecer."

    lu "Aquela revista vai trocar de mãos, isso já está certo. Você só precisa decidir se você quer se aliar ou não aos novos donos."

    lu "Quem ficar do lado certo da história terá inúmeras vantagens obviamente. Vai acontecer uma mudança na chefia."

    lu "Talvez a gente precise de um novo 'chefinho'. O que você acha?"

    mc "!"

    mc "E o que vai acontecer com a-"

    lu "Não pense nela. A velha guarda vai dar lugar para a nova guarda. Pense de que lado você estará quando o momento chegar."

    scene faux_poltronas with Dissolve(1.0)

    show luca falando with dissolve

    lu "Pense nisso com calma. E aguarde a [j] entrar em contato."

    lu "Obrigado pela atenção e nos vemos em breve."

    hide luca with dissolve

    "Caraca... o que foi tudo isso?"

    "Tem coisa demais na minha cabeça..."

    "O lance com a [w] e agora essa proposta maluca."

    "Talvez minha vida esteja pra mudar completamente nos próximos dias..."

    "[w]... Chefe... [j]..."

    "O que vai acontecer comigo e com eles?"



    scene black with Dissolve(1.0)

    "{i}glup{/i}"



    scene trabalho geral with Dissolve(1.0)

    "No fim, eu acho que vai ser um verdadeiro duelo entre a Sofia e a Cássia."

    "E eu vou ter que pensar do lado de quem eu vou querer ficar."

    "Falando nisso... hoje as duas discutiram bastante. Como será que as coisas ficaram entre elas?"

    menu:
        "Eu queria ser uma mosquinha pra ver (+18)":


            w "Tô cansada de ser a última a sair e ter que ficar esperando o guarda da noite chegar."

            "Só eu faço hora extra todo dia? Por isso que as coisas não vão pra frente."

            "Até hoje que eu tive trabalho fora, eu tive que voltar. E mesmo sem mim não tem ning-"

            "???" "... n-não..."

            w "Hm? Na sala da Cássia? Impossível que ela esteja trabalhando essa hora. Ela NUNCA trabalha."

            w "Eu preciso ver isso com meus próprios olhos."

            scene black with dissolve

            scene sofia3_new1 with Dissolve(1.0)

            pause



            "Garota" "S-senhora Cássia..."

            j "Que foi, pombinha? Você acabou de entrar na empresa. Eu só vou te ensinar como as coisas funcionam."

            w "!"

            "Garota" "E-eu entendi que a senhora-"

            j "NUNCA! Nunca me chame de senhora. É Cássia. Essa é a primeira coisa."

            "Garota" "D-desculpa."

            j "A segunda coisa é que se você quer crescer nesta revista, você precisa fazer o que eu mando."

            "Garota" "C-com certeza."

            j "Você vai ser meus olhos e meus ouvidos. E se você fizer um bom trabalho, eu garanto que você vai ser recompensada."

            j "Agora, se você não jurar lealdade a mim, então eu não vejo porque manter você no seu trabalho."

            "Garota" "A-ah..."

            j "Você vai ser uma boa garota?"

            "Garota" "S-sim..."

            j "Excelente. Então vamos selar nosso acordo na prática."

            "Garota" "C-cássia... e-eu concordo de ser sua espiã, m-mas eu... se eu puder... não quero nada desse tipo."

            j "Não quer?"

            "Garota" "P-por favor... eu sou sua aliada... só não me sinto bem com esse... contato físico."

            j "Você quer me dizer que você não pode superar um pouco de desconforto pra conseguir um lugar na mesa?"

            "Garota" "M-mas-"

            j "Eu só quero um beijo. Não é nada de mais, é?"

            "Garota" "U-um beijo?"

            j "Sim. Pra confirmar que você vai ser leal a mim."

            "Garota" "O-ok... um beijo..."

            scene black with dissolve

            scene sofia3_new2 with hpunch

            pause

            w "Que pouca vergonha é essa?!"

            "Como a gente pode ter uma funcionária que faz isso com nossos novos profissionais?!"

            "E a-ainda faz ela ir pra pouca vergonha?!!!"

            "Meu pai precisa saber disso o mais rápido possível!"

            label so3_premium1:

                pass

            "Eu não vou ficar aqui e participar dessa barbaridade!"

            "Ou será que é melhor eu ver bem o que elas tão fazendo pra ter mais provas depois?"

            "Hmm... talvez ver até onde elas vão pode ser importante... p-pra ter provas."

            menu:
                "Melhor eu coletar todas as provas.":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_37

                        jump so3_premium1

                    w "Mesmo não querendo, é melhor eu garantir que essa garota vai ficar bem! E ver até onde a Cássia pode ir!"

                    scene black with dissolve

                    scene sofia3_premium1 with Dissolve(1.0)

                    pause

                    "Garota" "D-dona Cássia... hmm..."

                    j "'Dona Cássia'... gostei... eu sou sua dona. Agora coloca sua língua pra fora."

                    "Garota" "V-você dis... ahnn..."

                    j "Só um beijo. É o que estamos fazendo."

                    j "Agora vem com seu corpo mais perto do meu."

                    j "Deixa eu sentir seus peitos amassando os meus enquanto eu engulo sua boca."

                    "Garota" "Hmmn!"

                    j "Se você se comportar, vai ser muito mais fácil pra você."

                    j "Aproveite... hmm... aproveite que você vai fazer isso... e curta também..."

                    "Garota" "N-não... e-eu... eu não gosto de mulh-"

                    scene sofia3_premium1 with vpunch

                    "Garota" "Hmmm!!!"

                    j "Cala a boca e me beija."

                    "Garota" "Nnngh..."

                    j "Não me interessa o que você acha... só faz o que eu mando e você vai ficar bem."

                    j "Agora continua chupando a boca da sua dona."

                    "Garota" "Nnnhnnn..."

                    j "Você tá indo muito bem."

                    "Garota" "O-obri- HHM!"

                    j "Continua assim... agora falta pouco."

                    "Garota" "Hnnnhn!"

                    scene black with dissolve

                    w "O que ela tá fazendo?!"

                    scene sofia3_premium2 with Dissolve(1.0)

                    pause

                    "Garota" "Aainn!"

                    j "Como você é deliciosa!"

                    "Garota" "Aahnn! D-dona C-cássia?!"

                    j "Só um beijo no pescoço, pombinha! Você não sente um arrepio?!"

                    "Garota" "S-sim!"

                    j "Tá vendo?! HMN! Eu vou sentir você todinha, meu amor."

                    "Garota" "M-mas eu n-não g-gosto! HMMN!"

                    j "Eu não perguntei. Só continua me apertando e deixa eu saborear você, igual a putinha que você é."

                    "Garota" "HMMN!!!"

                    j "Logo logo você vai tá pedindo pra sentir mais e mais... todas vocês são assim!"

                    "Garota" "N-não! Não me lambe assim por favor, dona Cássia!"

                    j "Huhuhu... tá sentindo, né?"

                    "Garota" "Ahn! Ahhhn!"

                    "Garota" "C-com licença!"

                    scene black with vpunch

                    j "Não fuja, minha pombinha!"

                    w "Ela tá vindo pra cá! Deixa eu sair!"
                "Eu já tenho mais que o suficiente!":


                    "Eu não vou ficar aqui participando dessa sem-vergonhice!"

            w "Deixa eu sair daqui."
        "Eu não ligo pra elas.":


            "Bora voltar pra casa."

    scene black with dissolve

    $ tempo = 3

    $ v28_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v28_fim","final","local")

    call checa_final from _call_checa_final_7

    jump call_cidade

label sofia_evento6:

    python:

        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("so6_save", extra_info="so6_save")

    $ iconchefe += 1

    $ estou_na_cidade = False

    $ sofia_evento6 = 2

    scene black with dissolve

    scene sofiaf1 with dissolve

    pause 2.0

    if nathan_final == 2:

        mc "As coisas tão tensas... Depois que o Nathan revelou ser da Interpol e a gente devolveu o dinheiro pra Zaza, ela ficou do nosso lado."

        if roxane_distrito:

            mc "A Roxane voltou pro Distrito, e com a ajuda do Black Cash ela tá se readaptando à vida lá. Ela disse que vai voltar pra sua família."
        else:


            mc pensando "A Roxane decidiu ficar com a Zaza e continuar seu sonho de ser modelo. Elas parecem felizes juntas."

        mc "O Nathan e a Natasha... Interpol... que doidera... e eu tô ajudando a investigar o Grupo, mas eles são poderosos. A gente precisa ser esperto."

        mc "A Cássia... ela não sabe de nada sobre o Nathan e a Interpol. E a Sofia... ela confia em mim. Preciso tomar cuidado pra não decepcionar ela."

        mc "A revista... ela é o próximo alvo. A Faux News quer comprar ela, e a Sofia tá desesperada pra impedir isso."

        mc "O chefe parece cansado, sem paciência. Deve tá na hora dele se aposentar. Ele não quer vender a revista, mas quem decide são os acionistas."

    elif nathan_final == 3:

        mc "Depois que eu convenci o Nathan a ficar com a Blergh! e me juntei ao Grupo, as coisas mudaram."

        mc "O Grupo me promete poder e influência... e a Cássia... ela me prometeu... outras coisas."

        mc "A Zaza tá usando o Nathan e a Roxane para fortalecer a Blergh! e se tornar um membro importante do Grupo. A revista é o próximo alvo deles."

        mc "A Sofia não faz ideia de que eu estou do lado deles. Ela confia em mim. Preciso manter essa fachada e garantir meu lugar no Grupo."

        mc "O chefe tá cansado, pensando em se aposentar. Ele não queria vender a revista, mas não vê outra saída. Essa é minha chance de me dar bem."

    w "{size=18}NÃO! Você não entende! A Faux News vai destruir tudo o que meu pai construiu!{/size}"

    j "{size=18}Você fala como se seu pai fosse um santo, querida. Acorda! Ele só se importa com o dinheiro dele!{/size}"

    mc "Hm? De novo essas duas..."

    menu:
        "Vou fingir que vou pegar um café e ouvir o que elas tão falando...":


            pass

    scene black with dissolve

    scene sofiaf2 with dissolve

    j "Ele tá desesperado pra vender essa revista e se aposentar! Ele já me ofereceu ela se eu conseguisse convencer os acionistas!"

    w "Mentira! Meu pai jamais faria isso!"

    j "Não se faça de sonsa, Sofia. Você sabe que ele não se importa com você! Nem com essa revista!"

    w "CALE A BOCA!"

    "A Sofia tá possessa..."

    j "Você sempre quis ser a princesinha dele, mas sabe o que ele fez contigo? Te mandou pra fora do país! HAHAHAHA!"

    scene sofiaf3 with hpunch

    w "A-ah!"

    j "Ele te odeia, talvez ainda mais que essa merda de revista. Você sabe que ele só se importa com as putas dele!"

    w "Você não passa de uma víbora interesseira!"

    j "Eu aprendi com o melhor. Ou você esqueceu quem foi meu mentor todos esses anos?"

    w "Você se aproveitou dele! Usou a fraqueza dele pra se dar bem!"

    j "E o que você fez a vida toda, hein, princesinha? Nasceu com tudo na mão e ainda se acha a última bolacha do pacote?"

    w "EU..."

    "Essa discussão tá ficando feia..."

    j "Você acha que é melhor que eu? Que você é ética, honesta, íntegra? Mas você não passa de uma mimada que nunca ralou na vida!"

    w "Eu... eu..."

    j "Perdeu as palavras, senhora sabe-tudo?!"

    w "GHHH!"

    play sound som_tapa

    scene sofiaf4 with hpunch

    j "!!!"

    mc "!!!"

    w "Nunca mais fale assim comigo!"

    j "Você é louca!"

    j "... Mimada! Você nunca ralou na vida! Não sabe o que é ter que lutar pra conseguir o que quer!"

    w "E você acha que se dar bem passando por cima dos outros é o certo?! Usando as pessoas?!"

    j "Eu faço o que for preciso pra chegar no topo! Não vou deixar ninguém me impedir!"

    w "Você é doente!"

    j "Sua..."

    b "QUE PORRA É ESSA AQUI?!"

    scene sofiaf5 with hpunch

    mc "!!!"

    w "Pai! Foi ela! Ela começou!"

    j "Eu?! Sua princesinha mimada que me atacou do nada! Ela precisa ser afastada!"

    b "CALEM A BOCA AS DUAS!"

    w "Mas, pai! Ela tava falando um monte de mentira! Que você queria vender a revista e me demitir! E que... e que..."

    j "Eu só falei a verdade! Você se acha a dona da verdade, mas não passa de uma criança mimada que não sabe como o mundo funciona!"

    b "CHEGA!"

    b "Eu tô cansado disso! Vocês duas enchendo meu saco todo santo dia! Parecem duas gralhas!"

    b "Quer saber? Eu vou é torcer pra esses fdp da Faux comprarem essa merda logo! Só pra me livrar de vocês!"

    w "Pai! Você não pode falar assim!"

    j "Parece que alguém aqui tá começando a enxergar a realidade."

    scene sofiaf6 with hpunch

    b "E você, [mc]! Que cara de enterro é essa?! Tá fazendo o quê aqui parado?!"

    mc "E-eu?!"

    "Caralho... o que eu falo? Me pegaram aqui xeretando!"

    "Eu preciso me colocar no lugar certo agora. Se a Faux comprar tudo..."

    "A Cássia... ela me prometeu que se eu ajudasse ela, ela ia me dar um cargo na nova revista. Não precisaria se preocupar com pautas!"

    "Mas a Sofia... ela é uma garota tão íntegra e verdadeira... ela continuaria publicando a verdade."

    if sofia_namoro:

        "Além de que a gente tá namorando. Daquele jeito... mas tá."

    "Será que eu posso ferrar ela desse jeito?"

    "Do lado de quem eu fico?"

    menu:
        "A Sofia começou. Ela deu um tapa na Cássia.":


            $ venda_revista += 1

            mc "Ela deu um tapa na Cássia na frente de todo mundo."

            w "Ela tava me provocando! Falando coisas horríveis!"

            j "Eu só falei a verdade, querida. Você não aguenta."

            b "Sofia... que tipo de coordenadora de produção resolve as coisas no tapa? Você é louca?"
        "Foi a Cássia. Ela tava enchendo o saco da Sofia.":


            mc "A Cássia que começou. Ela tava enchendo o saco da Sofia, falando da venda da revista e que o senhor ia demitir ela."

            j "Eu só falei a verdade! Ela precisa encarar a realidade, e não viver nesse mundinho de conto de fadas!"

            w "Obrigada, [mc]. Você viu, né? Ela é insuportável!"

            b "Cássia, eu já cansei dos seus chiliques. Você é uma das maiores razões pra minha vida ser TÃO miserável!"

            j "Velho caduco..."
        "Elas tavam discutindo sobre a venda da revista. As duas têm culpa.":


            mc "As duas estavam discutindo sobre a venda da revista. A Sofia não quer que vendam, e a Cássia tá do lado da Faux News."

            w "Eu só quero proteger a revista, pai! Não quero que ela caia nas mãos deles!"

            j "Não seja hipócrita, Sofia! A verdade é que a revista não tem mais futuro! Aceita que dói menos."

            b "Eu já disse e repito: eu não me importo com o que vocês acham! A decisão é da mesa de diretores e minha."

    b "[mc]! Entra aqui. AGORA!"

    j "..."

    w "..."

    "Sobrou..."

    scene black with dissolve

    pause

    scene sofiaf7 with dissolve

    b "Senta aí, [mc]."

    mc "..."

    "O chefe tá diferente. Trocou até de roupa. Eu não sabia que ele era fortinho assim..."

    b "Que cara é essa? Nunca entrou na minha sala?"

    mc "J-já entrei sim, senhor. Só tô... surpreso. De você querer falar comigo assim."

    b "Você achou que eu ia te demitir? Que eu ia te colocar pra fora daqui a dois quarteirões de distância com os gritos te acompanhando? É isso?"

    mc "N-nunca se sabe, né..."

    b "Eu não sou um monstro, garoto. Apesar de que às vezes eu me pergunto se não devia ter sido mais duro com vocês."

    "Mais? Velho rabugento do caralho."

    b "Eu não sou um monstro... mas eu tô cansado. Cansado dessa revista, dessa cidade... de tudo."

    mc "O senhor... tá pensando em se aposentar?"

    b "Aposentar? Não é bem isso... mas... talvez..."

    b "Eu trabalho nesta revista desde adolescente, garoto. Meu antigo editor-chefe tornou ela nessa potência que é hoje."

    mc "Seu... tutor?"

    scene black with dissolve

    scene sofiaf8 with dissolve

    b "Sim. Ele me ensinou tudo o que eu sei. E eu segui o legado dele, construindo essa revista com minhas próprias mãos. Dediquei minha vida a esse trabalho."

    b "Abri mão de tudo. Da minha família, dos meus amigos, da minha saúde... por essa merda."

    mc "..."

    b "E agora... olho pra trás e me pergunto... valeu a pena?"

    "Ixi... valeu?"

    menu:
        "Sim, chefe. A revista é importante. É a única mídia na capital que tem algum compromisso com a verdade.":


            mc "A Faux News, o jornal, a rádio... eles só se importam com o dinheiro. Com o poder. Com a manipulação."

            b "Você... você entendeu. Entendeu o que eu tentei construir aqui. O legado do velho Mauro... a importância de um jornalismo honesto... corajoso..."

            "Mauro?"
        "Não, chefe. Vamos ser sinceros. Falar de famosos é bem leviano. A revista nunca mudou a vida de ninguém.":


            mc "É só entretenimento. Fofoca. Não tem impacto real na sociedade."

            b "Você é um cínico, garoto! Um derrotista! Você não entende nada de jornalismo! Nada de vida!"

            mc "É o que eu acho."

            b "Mas... talvez você tenha razão... Talvez eu tenha dedicado minha vida a uma causa perdida... a um sonho vazio..."

            $ venda_revista += 1

    mc "Chefe..."

    b "Eu não queria vender a revista, [mc]. Você entende isso, né? Entregar tudo o que eu mantive por tantos anos pra aqueles abutres da Faux News..."

    b "Deixar de lado o que o meu editor construiu pra eles foderem?! ENTENDE?!"

    mc "S-sim, senhor. Eu entendo."

    b "Eu preciso de uma pessoa que assuma no meu lugar. Que tenha a energia que eu não tenho mais."

    "Alguém pra assumir a revista?"

    menu:
        "Não foi pra isso que o senhor trouxe a Sofia?":


            pass

    scene black with dissolve

    scene sofiaf9 with dissolve

    b "Sim... mas a Sofia... ela não tá pronta. Ela é inteligente, esforçada, tem tudo pra ser uma grande jornalista..."

    b "Mas ela não tem jogo de cintura. Ela é dura demais. Ela vai acabar com a revista se eu deixar ela assumir."

    mc "Mas... ela tem convicções. E ela é parecida com o senhor em ser dura demais."

    b "Você não entende nada, idiota!"

    mc "Olha aí..."

    b "Ser o editor chefe é manter um caldeirão borbulhante de explodir. Um bando de egocêntricos que se acham importantes."

    b "Cada um com sua opinião. Fazer eles se tolerarem e trabalharem juntos."

    mc "Falando assim parece difícil..."

    b "O que adianta bater o pé no chão e gritar suas convicções se não tiver ninguém pra ouvir? Se você afastar todo mundo?"

    scene black with dissolve

    scene sofiaf10 with dissolve

    mc "Realmente não sei..."

    b "Esses corruptos... eles querem a revista pra controlar a narrativa. Pra manipular a opinião pública. Pra se manter no poder."

    b "Se a Faux comprar a revista... eles vão ter o controle total da mídia. Vão poder fazer o que quiserem."

    b "Mas se eu me afastar e deixar na mão da Sofia, a revista acabaria em alguns anos e os investidores perderiam todo seu dinheiro."

    b "Eu não sei o que fazer, [mc]... Não sei qual é a MERDA de escolha dessa vez!"

    mc "..."

    mc "Eu... eu tenho me metido em muita encrenca ultimamente, chefe. Acabei descobrindo muita coisa sobre essa cidade..."

    b "É o que acontece quando se é um bom paparazzo. Você fuça, xereta, se mete onde não é chamado... e acaba descobrindo a verdade."

    b "O poder do paparazzo não é o calibre da sua arma ou o tamanho do seu braço, mas os segredos que descobre de quem tem muito a esconder."

    mc "E os segredos que eu descobri..."

    menu:
        "O senhor sabe quem tá por trás da Faux News, não sabe?":


            b "..."

            b "Como não saberia, [mc]? E você deveria saber, se é jornalista. Ou se diz."

            mc "E-ei..."

            "O chefe tá tão mal... eu... ele tá precisando de um amigo."

            "Nunca imaginei que eu fosse fazer isso, mas..."

            scene black with dissolve

            scene sofiaf11 with dissolve

            b "Garoto... eu..."

            b "Eu comecei a trabalhar com 14 anos. Entregando café, limpando banheiro, fazendo bico de office boy... e fui crescendo."

            b "Meu chefe, o velho Seu Mauro, me ensinou tudo o que eu sei. Ele me ensinou sobre jornalismo... sobre a vida... sobre essa cidade maldita."

            b "O velho Mauro já ralava aqui nessa revista quando o avô do Basílio Donatello ainda era vereador. E já brigava com ele!"

            mc "Então o senhor sabe do Grupo..."

            b "Desde aquela época, esses Donatello já davam dor de cabeça. Sempre querendo controlar tudo, manipulando os outros, se achando os donos da porra toda."

            b "O Seu Mauro me ensinou que o jornalismo é a única arma que a gente tem contra esses filhos da puta."

            b "É a única forma de colocar eles em cheque. De mostrar a verdade pras pessoas."

            mc "Tá vendo? Sabe o que significa se eles assumirem a revista!"

            b "Ele dizia que a gente precisa ser o contraponto. A voz que incomoda. A pedra no sapato desses poderosos."

            b "Porque se a gente se calar, se a gente aceitar tudo o que eles mandam... quem vai defender a verdade? Quem vai lutar pela justiça?"

            b "Totalmente baboseira na minha opinião."

            mc "Senhor..."

            scene black with dissolve

            scene sofiaf12 with dissolve

            b "Mas eu não posso ir contra ele. Não no que era mais importante pro velho fdp."

            b "A Faux News... eles são o braço direito do Donatello. Eles controlam a narrativa. Manipulam as informações. Fazem a cabeça das pessoas."

            b "Se eles comprarem a revista... vai ser o fim do jornalismo nessa cidade. Vai ser o fim da verdade."

            b "O Mauro ia se revirar no túmulo."
        "Eu... melhor eu ficar quieto...":


            mc "Eu... melhor eu não falar nada..."

            b "Não tem nada nessa sua cabecinha oca que preste, né?"

            mc "..."

            b "Você é um merda de jornalista, [mc]. Um zero à esquerda. Mas sabe de uma coisa?"

            mc "O quê?"

            b "Às vezes, até um zero à esquerda pode fazer a diferença. Pode ser a peça que faltava no quebra-cabeça. A gota d'água que transborda o copo."

            b "Você se meteu em muita coisa, garoto. Viu coisas que não devia. Ouviu coisas que não devia. E isso... isso pode ser útil."

            b "É o que o Seu Mauro diria pelo menos."

    "Espera... Mauro... eu lembro desse nome!"

    mc "O senhor... o senhor tá falando do Mauro... Ribeiro?"

    b "Esse mesmo. Você conhece o velho?"

    mc "Minha mãe me contou algumas histórias sobre ele. Ela falava dele com muito respeito."

    b "Sua mãe..."

    mc "..."

    b "Ela sempre foi uma mulher... à frente do seu tempo. Inteligente, corajosa... e teimosa pra caralho."

    "Eu sabia! Minha mãe e o chefe se conheceram!"

    "Como ela teria conseguido esse emprego pra mim?!"

    mc "Chefe... qual era a relação do senhor com ela? Por que o senhor me deu esse trabalho aqui na revista?"

    b "Que porra de pergunta é essa, garoto?!"

    scene sofiaf13 with hpunch

    mc "Eu mereço saber!"

    b "Não interessa! O passado é passado! O que importa é o agora! E o agora... é essa merda de revista sendo vendida pra aqueles abutres!"

    menu:
        "Pode contar comigo. Eu vou dar um jeito de ajudar.":


            mc "Chefe... me escuta... Eu posso ajudar. Eu posso encontrar uma saída pra essa situação."

    b "Você? Ajudar? Você não consegue nem entregar uma pauta decente no prazo!"

    mc "Mas eu posso. Eu conheço gente. Eu tenho informações. Podemos montar uma defesa para os investidores."

    b "Convencer os acionistas? Eles acreditam em mim... mas... não resolve o problema da sucessão."

    menu:
        "Você pode confiar na Sofia. Eu vou ajudar ela.":


            mc "Me ensine. Ensine pra gente como o velho Mauro te ensinou!"

            b "Hah... sua confiança tem a cara dos jovens malucos."

            mc "O senhor começou com 14 anos. Aposto que era pior que a gente."
        "Se o senhor vender, eu estarei aqui para ser o contraponto.":


            $ venda_revista += 1

            b "Você?"

            mc "Me ensine. E eu prometo que vou ser a voz contrária na redação da Faux... na medida do possível."

            mc "E vou convencer eles a deixarem a Sofia. Sua filha vai continuar seu legado."

            b "Hah... sua confiança tem a cara dos jovens malucos."

            mc "O senhor começou com 14 anos. Aposto que era pior que eu."

    scene black with dissolve

    scene sofiaf14 with dissolve

    b "Haha... não sei o que aconteceu com você nessa cidade, menino, mas você não é o mesmo."

    b "Cadê aquele garotinho que falava comigo gaguejando?"

    mc "E-ei!"

    b "Quem sabe... obrigado pela proposta."

    menu:
        "Mas eu quero algo em troca.":


            pass

    b "Em troca? Que tipo de troca?"

    mc "Eu quero a verdade. Eu quero saber a história completa do senhor e da minha mãe. Quero saber por que o senhor me deu esse emprego."

    b "Você tá me chantageando, garoto?!"

    mc "Não, chefe. Eu tô fazendo uma proposta. Uma troca justa. Eu ajudo o senhor na revista... e o senhor me conta a verdade."

    b "..."

    mc "Eu conheço a Sofia. E a Cássia também. Eu posso dar um jeito nisso. Posso até fazer elas se entenderem."

    b "Você tá louco, garoto?! Elas se odeiam! São água e óleo! Impossível juntar essas duas!"

    mc "Nada é impossível, chefe. Confia em mim."

    b "Confiar? Em você? Você acha que eu sou idiota? Você é só um..."

    b "Ha... deixa pra lá."

    scene black with dissolve

    scene sofiaf15 with dissolve

    b "Você se meteu em cada uma nesses meses, trouxe cada coisa, que eu até esqueci que você é só um iniciante."

    b "Essas duas... elas são o oposto uma da outra. Sofia, toda certinha, ética, idealista... e a Cássia, uma manipuladora implacável, sem escrúpulos..."

    b "Elas duas juntas... são responsáveis por metade das minhas dores de cabeça. Os outros 40%% são culpa da minha ex-mulher..."

    b "E os 10%% que sobram são essas malditas dores nas costas."

    mc "Eita..."

    b "Elas brigam tanto... que às vezes eu acho que elas parecem até... marido e mulher... hahaha!"

    mc "Como é?"

    b "Enfim... se você acha que consegue controlar essas duas feras, vá em frente. Mas não espere milagre."

    mc "Eu vou conversar com elas. E vou trazer uma solução. Pode apostar."

    b "E depois... você vai querer saber sobre o seu passado... sobre mim e sua mãe..."

    mc "Sim, senhor."

    b "Eu não espero muito de você, [mc]. Mas... quem sabe. Às vezes, até um cego acha uma moeda no chão."

    b "Mas te digo uma coisa... o passado... às vezes, o passado é melhor ficar guardado. Enterrado. Esquecido."

    b "Às vezes... mexer nele... só traz dor. Arrependimento. Sofrimento."

    mc "..."

    "O que ele fez no passado?"

    b "Agora sai da minha sala!"

    mc "O-ok!"

    scene black with dissolve

    "Parece que o chefe tá confiando mais em mim do que na própria filha e na Cássia, que é velha da casa."

    "Será que eu tenho super poderes e nem faço ideia?"

    scene black with dissolve

    scene sofiaf16 with dissolve

    j "Oi, pombinho. Parece que o chefe tá começando a gostar de você, hein?"

    mc "C-Cássia... você sempre..."

    j "Xiu... você sempre gostou da nossa relação assim, pombinho. Não vamos mudar agora. E então? O chefe tá gostando de você?"

    mc "Gostar? Talvez... ele me falou do velho Mauro."

    j "Sei... mas ele te chamou pra sala dele, conversou com você... isso não é normal, bebê."

    mc "É... eu vi que ele tava diferente. Me xingou de idiota, mas foi diferente."

    j "Talvez ele veja em você o reflexo dele mesmo, quando era mais novo... a inocência que ainda não foi corrompida pelo mundo."

    mc "Eu já vi muita coisa..."

    j "Ah, eu sei... mas o chefe, quando começou, tinha ideais. Queria fazer jornalismo de verdade. Eu lembro."

    mc "E o que aconteceu?"

    j "Aconteceu a vida, querido. O tempo. A realidade. Eles corrompem tudo. E todos."

    mc "..."

    j "Talvez ele queira te transformar no pupilo dele. Te ensinar tudo o que ele aprendeu. Te passar o bastão."

    mc "O bastão?"

    j "É. Te preparar para ser o próximo editor-chefe. O novo Mauro Ribeiro."

    mc "Mauro Ribeiro..."

    j "Só que tem uma diferença... crucial... entre o velho Mauro e o chefe..."

    mc "Qual?"

    scene black with dissolve

    scene sofiaf17 with dissolve

    j "O velho Mauro não era um filho da puta que trepava com as repórteres da revista dele e depois as descartava como lixo."

    mc "C-como é? Isso parece específico demais, Cássia."

    j "Entenda o que quiser entender, pombinho."

    mc "Você... você e o chefe...?"

    j "Vamos com calma... ainda não é hora."

    mc "Hm? Que todo segredo é isso?"

    j "Você tá do lado do Grupo, [mc]? Ou você é um desses idealistas que acham que podem mudar o mundo?"

    if grupo_nathan == 1 or grupo_nathan == 3 or nathan_final == 3:

        mc "Eu tô com o Grupo. Você sabe. E vou fazer o que for preciso pra garantir que eles tenham o que querem. Inclusive a revista."

        j "Sabia que você era esperto, pombinho. Você sabe onde o poder está. E sabe como jogar o jogo."
    else:


        mc "Eu não acho certo dar ao Grupo todo o controle da mídia da Capital. A verdade precisa ser dita, mesmo que fira o Donatello."

        j "Você é um idiota, [mc]. Você vai se arrepender amargamente dessa escolha. O Grupo não perdoa traidores."

        j "Você ainda tem tempo, mas a hora tá chegando. E você vai ter que decidir."

    j "Agora sobre a venda da revista..."

    if venda_revista >= 2:

        j "Parece que você tá se saindo bem, pombinho. Eu ouvi por aí que o chefe tá quase caindo na nossa."

        mc "Eu tô fazendo minha parte. Tô convencendo ele. Agora é só esperar o momento certo."

        j "E quando esse momento chegar... você vai ter sua recompensa. Pode apostar."
    else:


        j "Se continuar nesse ritmo, o velho não vai cair. Você precisa se esforçar mais, pombinho. Ou vai perder tudo."

        mc "..."

        j "Você não quer perder essa chance, quer? De ter uma vida boa, sem ter que ralar pra conseguir pautas?"

    j "Se as coisas acontecerem como eu planejei... você nunca mais vai precisar se preocupar com pautas, com deadlines, com aquele velho filho da puta te enchendo o saco."

    j "Você vai entrar como editor. No meu lugar. Vamos comandar a revista juntos. Você e eu."

    mc "Editor... sem ter que caçar pautas... sem o chefe me enchendo... com a Cássia..."

    j "Mas... se você for contra... se a revista não for vendida..."

    j "..."

    scene black with dissolve

    scene sofiaf18 with dissolve

    j "Eu vou ter que... usar o plano B."

    mc "Plano B?"

    j "É... algo que eu guardei por muito tempo... uma carta na manga... um último recurso..."

    mc "..."

    menu:
        "Que plano é esse?":


            mc "Que plano é esse, Cássia? Você tá me assustando..."

            j "É algo que você não precisa se preocupar... por enquanto. Contanto que as coisas aconteçam como devem acontecer."

            mc "Caralho, hein?"
        "Eu não quero saber. Nada vai funcionar.":


            j "Conte com isso, meu amor."

    j "Faltam poucos dias agora, [mc]. O momento chegou. A Faux News vai fazer a proposta pra comprar a revista."

    j "A Sofia vai lutar com unhas e dentes para impedir a venda. Ela vai tentar te convencer a ficar do lado dela."

    j "Mas você precisa ser esperto, [mc]. Você precisa pensar em você. No seu futuro. Na sua carreira."

    j "Você tem a chance de ter tudo o que sempre sonhou, pombinho. Poder, influência, dinheiro... uma vida de luxo e glamour..."

    j "Ou você pode continuar sendo um simples paparazzo, correndo atrás de migalhas, sendo explorado por aquele velho gagá..."

    j "A escolha é sua, [mc]. Mas decida logo. O tempo pra pensar acabou."

    mc "Ok... você vai descobrir minha escolha em breve."

    j "..."

    "Vamos ver como tá a Sofia agora. Ela deve tá..."

    scene black with dissolve

    w "Desonesta! Víbora! Sem vergonha! Ela acha que pode usar o corpo pra conseguir tudo o que quer! Safada!"

    scene black with dissolve

    scene sofiaf19 with vpunch

    mc "Bu!"

    if sofia_namoro:

        mc "Ei, ei, ei... calma aí, minha bravinha... Tá falando do corpo da Cássia? Que eu saiba, quem usa o corpo aqui sou eu... em você."

        w "Idiota! Não fala essas coisas aqui! E eu não tô 'bravinha'! Só acho ela uma..."

        w "...desgraçada... Que fica se esfregando nos outros... oferecida..."

        mc "Falando assim, até eu fico com ciúmes. Mas pode ficar tranquila, você é a única dona do meu coração... e de outras partes do meu corpo também."

        w "Para de graça, [mc]! A gente precisa se concentrar!"

        mc "Eu sei, eu sei... Mas você sabe que eu adoro te provocar, né?"

        w "Sei... e no fundo... d-deixa pra lá."
    else:


        mc "Sofia... você tá bem? Parece nervosa..."

        w "Nervosa? Eu tô furiosa! Essa Cássia... ela é inacreditável!"

        mc "O que ela fez dessa vez?"

        w "Ela acha que pode manipular todo mundo com aquele charme barato dela! Que pode usar o corpo pra conseguir o que quer! É revoltante!"

    mc "..."

    if venda_revista >= 2:

        w "E você, [mc]? Parece que tá do lado dela... da Cássia... Você também acha que eu sou uma mimada? Que eu não sei como o mundo funciona?"

        mc "Por que tá falando isso?"

        w "Sinto que meu pai vai acabar comprando a revista se continuar assim."

        mc "Hmm..."

    elif venda_revista < 2:

        w "Ainda bem que você tá do meu lado, [mc]. A gente não pode deixar eles destruírem a revista. A Cássia... ela só se importa com ela mesma, com o prazer dela..."

        mc "Que bom que você tá otimista."

        w "Ouvi por aí que ele tá pendendo a não vender. E você tá sendo importante nisso. Só continuar!"

        mc "Pode deixar."

    mc "Agora, escuta aqui. A Cássia... ela tem uma carta na manga. Ela chamou de 'Plano B'."

    w "Plano B? Que plano é esse?"

    mc "Não sei. Ela não quis me contar. Mas parecia algo... sério. Algo que pode mudar tudo."

    w "Mudar tudo? Como assim?"

    mc "Não sei, Sofia. Mas... você precisa se preparar. Pra qualquer coisa."

    mc "Eu sei o quanto essa revista é importante pra você. Você não pode deixar eles ganharem."

    scene black with dissolve

    scene sofiaf20 with dissolve

    w "..."

    w "Essa revista... ela é mais do que um trabalho pra mim, [mc]. É... é o legado do meu pai."

    w "Meu pai dedicou a vida dele a esse lugar. Ele abriu mão de tudo pela revista. Dos amigos, da saúde, da família, de mim..."

    w "Eu... eu sempre achei ele um idiota. Um workaholic que queria se livrar de mim."

    w "Mas... depois que eu comecei a trabalhar aqui... eu entendi. Eu entendi a paixão dele. O amor dele pelo jornalismo."

    w "Eu vi como ele se esforçava pra trazer a verdade pras pessoas. Eu sei que as matérias são fofoca, mas também tem a verdade."

    w "E eu... eu quero continuar esse trabalho. Quero fazer a revista ser ainda melhor. Quero honrar o legado dele."

    menu:
        "Essa é a sua razão então...":


            pass

    w "E, claro, não suporto a Cássia, [mc]. Ela é tudo o que eu abomino em um jornalista. Desonesta, manipuladora, sem escrúpulos..."

    w "Ela acha que pode usar o corpo, o charme, pra conseguir o que quer. Ela acha que todo mundo vai cair pra aquele corpo perfeito dela, siliconado."

    w "Mas eu não vou deixar. Eu vou expor a verdade. Vou mostrar pras pessoas quem ela é de verdade. E vou tirar ela da revista. E todo mundo que for contra mim. Pra sempre."

    scene black with dissolve

    scene sofiaf21 with dissolve

    w "A Faux News... aquele Luca Alighieri... me dá nojo só de lembrar do jeito que ele falou sobre jornalismo."

    w "Como se a verdade fosse um produto. Uma mercadoria que pode ser comprada e vendida."

    w "Eu não vou deixar eles destruírem a revista, [mc]. Eu não vou deixar eles calarem a minha voz."

    w "Eu preciso da sua ajuda. A gente precisa impedir a venda. Custe o que custar."

    menu:
        "Eu tô com você, Sofia. A gente vai conseguir.":


            mc "Não vamos deixar eles vencerem."

            w "Obrigada, [mc]. Eu sabia que podia contar com você."
        "Sofia, eu sei que a revista é importante, mas não pode ser tudo na sua vida. Você tem...":


            if sofia_namoro:

                mc "...a mim. E eu não vou deixar você se afundar nisso. A gente vai dar um jeito, juntos."

                w "[mc]..."
            else:


                mc "...seus amigos, sua família... você não pode deixar isso te consumir."

                w "Você tem razão... talvez eu esteja levando isso a sério demais..."

    w "Agora é esperar pra ver o que meu pai decide. Se ele resolver vender..."

    w "Se eu souber de qualquer coisa, eu te ligo, tá?"

    mc "Combinado."

    if sofia_namoro:

        menu:
            "Provocar ela agora no meio da redação":


                mc "Mas antes de eu ir..."

                scene black with dissolve

                scene sofiaf22 with dissolve

                mc "E quando você for a diretora-chefe e eu o editor... vou levar uma 'notícia' na sua sala todo dia, hein?"

                w "Que 'notícia', [mc]? Você tá ficando maluco? Você não vai ser editor! Precisa ralar pra isso."

                mc "Bom... vou levar uma notícia do tipo que deixa você toda molhadinha... só esperando meu pau entrar."

                w "Para com isso, [mc]! Aqui não!"

                mc "Imagina só... você sentada na sua cadeira, toda poderosa, de pernas cruzadas... e eu entro na sua sala, fecho a porta..."

                w "E-ei..."

                mc "...e me enfio em baixo... bem devagar... até chegar na sua mesa..."

                w "P-para..."

                mc "Você tenta se controlar, mas não consegue. Suas pernas começam a tremer... você sente um calorzinho... bem lá..."

                w "N-não..."

                mc "Eu chego mais perto... e começo a te lamber... bem de leve... sentindo seu gosto... seu cheiro..."

                w "Aahh..."

                mc "Você geme baixinho, tentando se controlar... mas eu sei que você tá gostando... tá adorando..."

                w "Nnn..."

                mc "Eu continuo... cada vez mais rápido... mais fundo... até você..."

                w "[mc]... e-eu..."

                mc "Você explode de prazer... ali mesmo... na sua sala... na sua mesa... enquanto eu..."

                scene sofiaf24 with hpunch

                w "CHEGA! Para com isso agora, [mc]! Você tá me deixando... louca!"

                mc "Haha... Parece que alguém gostou da 'notícia'..."

                w "Idiota..."
            "Deixar pra outra hora":


                pass

    mc "Agora eu vou indo nessa."

    w "Tá... a gente se fala. Que eu tenho que dar umas 2 broncas hoje ainda."

    mc "Haha... credo. Falous."

    scene black with dissolve

    "Deixa eu dar o fora daqui antes que sobre pra m-"

    re "Ei, gato. Vai aonde com tanta pressa?"

    scene sofiaf23 with dissolve

    mc "Renata..."

    menu:
        "Oi, Renata. Tá sexy.":


            mc "Você é a secretária mais sexy que eu já vi."

            re "Ai, que fofo. Você também, [mc]."

            re "Você é um dos únicos aqui na redação que não me come com os olhos."

            mc "Vou mudar isso a partir de hoje."

            re "Bobo..."
        "Que que foi, Renata?":


            "Ela tá com a Cássia. Tenho que tomar cuidado."

            re "Nossa, que grosseria. Não posso mais nem admirar um gato que passa por aqui?"

            mc "Hum... qual sua intenção?"

    re "Eu tô contente."

    mc "A é? E por quê?"

    re "A Cássia... ela me prometeu uma nova posição quando a revista for vendida."

    mc "Prometeu? Mas isso ainda não tá certo. A Sofia não vai deixar."

    re "Eu adoraria que ela não tivesse errada, sabe? Seria ótimo pra mim..."

    mc "Seria, né? Quanto ótimo?"

    re "Hmmm... bastante... O quanto você quiser, gato..."

    "A Renata... ela tá dando fazendo o que eu tô achando que ela tá?"

    "Será que eu entro nessa? Pode ser arriscado, mas..."

    menu:
        "Tem uma sala vazia ali. Vamos conversar melhor lá?":


            mc "Quero saber o quão feliz você pode ficar se a revista for vendida..."

            re "Você tá falando sério?!"

            mc "Você é gostosa... e parece que precisa de uma ajuda... e eu adoro ajudar."

            re "Hmmm... mas é sério mesmo, gato?"

            mc "Vem. Me mostra o quanto você quer que essa revista seja vendida."

            re "Hmmm..."

            play sound som_roupas

            scene black with dissolve

            scene sofiaf25 with dissolve

            mc "Uau..."

            re "E então, safadinho... gostou?"

            mc "Você é ainda mais linda do que eu imaginava..."

            re "Eu sei. E agora... eu sou toda sua."

            mc "Vem cá..."

            re "Espera... primeiro você tem que me prometer que a revista vai ser vendida."

            mc "Eu não tenho esse poder."

            re "Tá... tá bom... mas você vai fazer tudo o que puder pra ela ser vendida."

            menu:
                "Tá bom. Agora vem aqui.":


                    $ renata_prometeu = True

                    "Espero que pensar com o pau não acabe me fodendo depois. Mas essa mina é um tesão."

                    mc "Eu prometo. Agora me beija, gostosa."

                    re "Eu gosto assim, com vontade."

                    scene black with dissolve

                    scene sofiaf26 with dissolve

                    re "Hmmm..."

                    mc "Que boca gostosa... você é muito gata, sabia? E sabe beijar."

                    re "Eu sei... nunca ninguém reclamou."

                    mc "Safada... você fica muito por aí?"

                    re "Só com quem merece e me pega de jeito."

                    mc "Entendi a sua. Você gosta de ser mandada, né? De obedecer..."

                    re "Hmmm... adoro... adoro quando me dizem o que fazer... adoro ser uma boa garota."

                    mc "Eu adoro mulheres assim... submissas... que fazem tudo o que eu quero."

                    re "Eu faço... ahnn... eu juro..."

                    re "E você tá me lembrando a Cássia..."

                    mc "A Cássia, é?"

                    re "O jeito dela. O jeito que ela manda, que ela domina... é excitante, sabe?"

                    mc "Pra uma putinha igual você deve ser uma delícia, mesmo."

                    re "Hmmm..."

                    mc "Agora senta aqui... vou sentir se sua buceta é gostosa."

                    scene black with dissolve

                    scene sofiaf27 with dissolve

                    re "Hmmm... adoro esse seu jeito mandão... me deixa tão molhada."

                    re "Hmmm... [mc]... mais... mais forte... aí... sua língua... na minha buceta... aahh..."

                    "Que xotinha gostosa. Ela é docinha, molhada, rosinha..."

                    mc "Você é deliciosa, [re]."

                    re "Aiii... [mc]... isso... aahh... você chupa com tanta vontade."

                    mc "Tô te preparando pro que vai vir."

                    re "Aahnnn..."

                    mc "Você é tão gostosa, Renata... tão apertada... tão molhada..."

                    re "Isso... ahnnn... não sabia que você... ahh... que delícia! Isso, me fode mais com essa língua!"

                    mc "Caralho, Renata... você é..."

                    re "Sua... sou toda sua..."

                    re "Hmmm... [mc]..."

                    mc "Agora você tá pronta pro meu caralho."

                    scene black with dissolve

                    scene sofiaf28 with dissolve

                    re "Que pau gostoso... dá pra sentir daqui... vou adorar pegar nele."

                    mc "Vai sentir ele agora, vai?"

                    re "Claro que eu vou... minha bucetinha tá chorando pra você socar nela."

                    mc "Deita aí no sofá agora."

                    re "Ai... eu nunca te vi assim... tão mandão... pegando o que quer..."

                    mc "Talvez a cidade tenha mudado a gente, Renata. A ilha... as celebridades... o poder... o dinheiro..."

                    re "Sim... e eu gosto assim..."

                    re "Mas eu só vou deixar você saboerear ela se você cumprir sua palavra."

                    mc "Como é?"

                    re "Você prometeu que vai vender a revista. Se você vender... eu te dou ela todinha."

                    mc "Vai me provocar assim, é?"

                    re "Vou... ah... que tesão..."

                    mc "Caralho, garota... tá bom. Vem cá."

                    re "Hehe... Eu vou."

                    scene black with dissolve

                    scene sofiaf29 with dissolve
                "Não posso. Você é linda, mas não posso prometer isso.":


                    re "Então nem vem. Você não quer me ajudar."

                    mc "Não é isso... é que tem outras coisas em jogo aqui."

                    re "Não me interessa. O que me interessa é minha vida."

                    mc "Faz sentido... mas falando nisso..."

            mc "Como você entrou nessa? Com a Cássia, com a revista..."

            mc "Quem... quem é você, Renata? De verdade?"

            re "Eu? Você quer saber mesmo?"

            menu:
                "Quero. Me fala.":


                    re "Eu... eu vim pra cá cheia de sonhos, [mc]. Queria ser atriz..."

                    mc "É o que acontece com várias garotas aqui da ilha."

                    re "Sim! Vim pra ilha pra fazer o teste pro novo filme do diretor Gustav Aldebaran... um filme de fantasia..."

                    mc "Não me diga..."

                    re "Mas... eu não consegui o papel. A produção disse que eu não tinha... experiência suficiente."

                    re "Eu fiquei tão decepcionada... tão... perdida... Não sabia o que fazer..."

                    mc "Poxa..."

                    re "Não queria voltar pra casa sem dinheiro... sem perspectivas... sem esperança..."

                    re "Foi aí que a Cássia me encontrou. Ela me ofereceu o emprego na recepção da revista... disse que era um lugar pra eu recomeçar..."

                    mc "Uau... a Cássia te ajudou?"

                    re "Demais! Ela... queria alguém do lado dela, pra ajudar em um plano envolvendo o editor."

                    mc "É... isso sim faz a cara dela."

                    re "O editor é um safadinho."

                    mc "Safadinho?"

                    re "Mas foi assim que eu consegui o emprego."

                    re "O salário é uma merda... mas pelo menos paga o aluguel e a comida... e me mantém perto do sonho..."

                    re "Eu sei que não sou atriz... nem modelo... nem cantora... nem nada..."

                    re "Mas... eu ainda sonho que um dia eu vou conseguir ser atriz."

                    if renata_prometeu:

                        scene black with dissolve

                        scene sofiaf30 with dissolve

                    menu:
                        "Por isso a Faux ajudaria você...":


                            re "Muito!"

                            re "Se a Faux News comprar a revista, ela vai ter muito mais dinheiro, posições pra crescer."

                            re "A Faux News também faz parte do Grupo Faux, sabia? A produtora do Gustav também faz parte."

                            re "Eles são donos de emissoras de TV, rádio, jornais... e a produtora dele."

                            mc "É... eles estão todos envolvidos no mesmo grupo... faz sentido."

                            re "Se eu conseguisse um contato lá... seria incrível pro meu sonho! Uma chance de ouro!"

                            menu:
                                "Você sabe quem são eles, Renata? O que eles fazem?":


                                    pass

                            re "Eu... eu escuto boatos... que eles são meio... maus... que fazem coisas erradas pra conseguir o que querem..."

                            mc "Mesmo assim você ainda quer se envolver com essas pessoas?"

                            re "Pensa, [mc]... criar um império desse tamanho não deve ser fácil. Eles precisam ser fortes... determinados..."

                            re "Eu... eu adoro pessoas fortes... que fazem o que têm que fazer... igual você fez hoje..."

                            mc "..."

                            "Igual eu fiz hoje... ela tá falando... de como eu tratei ela? De como eu mandei nela?"

                            "Ela gostou... gostou de ser usada... de ser dominada..."
                        "Entendi. Vou indo nessa.":


                            pass

                    "A Renata... ela é mais complicada do que eu imaginava..."

                    re "Se a revista for vendida... você vai poder ter tudo de mim. Tudo o que você quiser. Lembra disso, por favor!"

                    mc "Pode deixar. Eu... vou pensar em você também."

                    re "Obrigada! Hehe."
                "Pensando bem, a gente fala disso outra hora.":


                    re "O-ok..."
        "A revista não será vendida. E você devia tomar cuidado com a Cássia. Ela não é flor que se cheire.":


            mc "A revista não será vendida, Renata. E você devia tomar cuidado com a Cássia. Ela não é flor que se cheire. Ela promete mundos e fundos, mas no fim..."

            re "Então... eu não tenho mais chance..."

            mc "Você pode continuar trabalhando aqui!"

            re "N-não é suficiente, não entende?! Tudo o que eu queria era..."

            re "Deixa pra lá..."

            mc "..."

    mc "Até mais, Renata."

    re "Até..."

    scene black with dissolve

    scene sofiaf31 with dissolve

    "Caralho... tanta gente envolvida nessa decisão da revista."

    "São dezenas de pessoas trabalhando. Todas elas poderiam ter uma vida melhor se a Faux investisse na revista."

    "Eles são os picas da galáxia da mídia. Eu e os outros repórteres e funcionários..."

    "Será que seguir a Sofia é a coisa certa?"

    "Eu preciso de uma luz. Eu preciso saber o que é melhor, o que é certo. Eu... preciso de respostas."

    "Evitei isso pelo máximo tempo que deu. Mas eu preciso de alguém que saiba sobre tudo isso."

    "Tá na hora de falar com ela."

    menu:
        "Vou ligar pra minha mãe":


            $ so6_mae_ligou = 2

            mc "Faz tempo que a gente não se fala. Ela vai tá uma arara."

            "{i}Tu tu tu...{/i}"

            mae "Alô?"

            scene black with dissolve

            scene sofiaf32 with dissolve

            mc "Oi, mãe. Tudo bem?"

            mae "[mc]?! É você mesmo? Faz tempo que a gente não se fala... NÉ?!"

            mc "Pois é... bastante tempo..."

            mae "Lembrou que tem mãe?"

            mc "Eu nunca esqueci. Você podia ter me ligado também."

            mae "Não. Claro que não! Desnaturado! É obrigação dos filhos ligar pros pais. Não o contrário."

            mc "Sei..."

            mae "E por que você resolveu dar sinal de vida agora? Aconteceu alguma coisa?"

            mc "Mãe... por que você conseguiu esse emprego pra mim? Por que na revista?"

            mae "Que pergunta é essa?"

            mae "Você está me cobrando por isso agora? Depois de tanto tempo?"

            mc "Não, mãe. Eu só... eu só quero entender."

            mae "Entender o quê? Que eu me sacrifiquei pra te dar uma vida melhor? Que eu abri mão dos meus sonhos pra te criar?"

            mc "Não, mãe. Não é isso..."

            mae "Então o quê? Fala logo, [mc]! Eu sou sua mãe, não esconda as coisas de mim!"

            mc "Eu me meti em muita coisa aqui, mãe. E eu preciso saber... se você tem alguma coisa a ver com isso."

            mae "Você está se metendo com gente perigosa, [mc]?"

            mc "Eu... eu não sei, mãe. Mas eu preciso saber. Por que a revista? Por que o chefe?"

            mae "..."

            scene black with dissolve

            scene sofiaf33 with dissolve

            mc "Quem... quem era o Mauro Ribeiro pra você?"

            mae "Bom..."

            mae "Eu trabalhei com o Mauro há muito tempo. A gente... se ajudava. Ele ficou me devendo uma."

            mae "E o Escobar acabou pagando no lugar dele."

            mc "Escobar?"

            mae "Seu chefe! Vai me dizer que você nunca perguntou o nome dele?!"

            mc "..."

            "Eu nunca soube o nome do meu chefe... caralho... o nome dele é Escobar então!"

            mc "O que... o que você fez, mãe? Por que o chefe pagou uma dívida do Mauro Ribeiro? Do ex-chefe dele?"

            mae "Você está me julgando? É isso? Depois de tudo que eu fiz por você, você se acha no direito de me questionar?"

            mc "Não, mãe! Eu só... eu só preciso saber!"

            mae "Saber pra quê?! Pra se meter em mais encrenca?! Pra se afundar ainda mais nesse buraco que você cavou?!"

            mc "Mãe, eu preciso entender! Saber qual a melhor decisão! E eu preciso saber se você tem algo a ver com isso!"

            mae "Decisão?! Filho, se afaste disso! Não se meta com essa gente! Eles vão te destruir!"

            mae "Eu não quero que você se machuque... Você quer deixar sua mãe nervosa?!"

            mc "Eu tô falando de mim, mãe... não da senhora."

            mae "Eu só queria te proteger... te dar uma vida melhor... longe dessa cidade... dessas pessoas..."

            mae "Não se envolva demais no passado, [mc]. Certas coisas... certas coisas foram feitas pra serem esquecidas. Enterradas. Pra nunca mais verem a luz do dia."

            mc "..."

            mc "O chefe... ele disse algo parecido... 'o passado é melhor ficar guardado...' O que vocês tão escondendo?"

            mae "[mc]... se afaste disso. Por favor. Volta pro interior... vem morar comigo... a loja da família tá precisando de ajuda..."

            scene black with dissolve

            scene sofiaf34 with dissolve

            mc "Não, mãe. Eu não vou voltar. Eu não vou abandonar tudo o que eu construí aqui."

            mae "Mas é perigoso! Você não sabe com quem está se metendo!"

            mc "Eu sei me cuidar, mãe. E o chefe... ele tá de olho em mim."

            mc "Se a revista não for vendida pra Faux News, talvez eu acabe crescendo aqui. Virando editor... quem sabe..."

            mae "Vender? Vende logo essa revista maldita! Ela já deu o que tinha que dar! Tanto pro Escobar quanto pra mim!"

            mc "Como assim?"

            mae "E outra coisa, filho... liga mais vezes pra sua mãe! Não só quando for pertinente pra você!"

            mc "Mãe..."

            mae "Você não sabe o que eu passei pra te criar! Eu me sacrifiquei! Abri mão de tudo! Da minha carreira, dos meus sonhos, da minha vida! Tudo por você!"

            mae "E você me trata assim?! Me liga só quando precisa de alguma coisa?! Cadê o respeito, [mc]?! Cadê a consideração?!"

            "Por isso que eu não queria ligar pra ela!"

            mae "Jesus fala que a gente precisa honrar pai e mãe! É um dos dez mandamentos, não é!? Você não aprendeu nada na igreja?!"

            mae "Eu te levei todo domingo na missa! E você me trata assim?! Que tipo de filho você é?!"

            mc "M-mãe... eu..."

            mae "Você não sabe o quanto eu sofri! As noites que eu passei em claro cuidando de você! As vezes que eu abri mão de comer pra te alimentar!"

            mae "Eu te dei tudo, [mc]! Tudo! E você me retribui com essa ingratidão?! Com essa indiferença?!"

            menu:
                "Mãe, eu preciso ir! Te amo! Tchau!":


                    pass

            mae "Fil-"

            "{i}Tu tu tu...{/i}"

            mc "Ufa..."

            "Não adianta tentar tirar algo dela. Ela sempre foi assim."

            "Vou ter que fazer o chefe me contar. E decidir o que é melhor por mim mesmo."
        "Não... eu não quero falar com ela. Ela vai vir com sermão.":


            $ so6_mae_ligou = 1

            "Eu vou decidir por mim mesmo."

    "Agora é esperar a proposta da Faux. Ela tá vindo."

    "E vai ser a hora de decidir TUDO!"

    scene black with dissolve

    p lecionando "O final da Sofia continua na próxima atualização."

    call ajuda_itchio

    $ tempo += 1

    jump call_cidade

label sofia_evento6_parte2:

    $ estou_na_cidade = False

    $ sofia_evento6 = 4

    scene black with dissolve

    scene so6_img0 with dissolve

    "O clima na redação não tá mais o mesmo."

    "Parece que todo mundo já tá sabendo que pode rolar a venda."

    mc "Eu sinto que cada passo que eu der agora vai ditar o futuro da revista e de todos aqui."

    if sofia_namoro:

        "Parece que namorar a Sofia me colocou em um lugar privilegiado nessa história."
    else:


        "Parece que ter virado amigo da Sofia me colocou em um lugar privilegiado nessa história."

    "Ela confia em mim."

    if venda_revista >= 2:

        "Mas o azar é dela."

        "Eu preciso fazer o chefe vender a revista pra Faux News. É o melhor pra mim e eu vou conseguir o que eu quero."

        "Eu vou ficar do lado da Cássia e garantir minha vida."
    else:


        mc "Eu preciso impedir que a revista seja vendida. Não posso deixar que a Sofia perca o controle dela. E eu vou proteger ela do que for preciso."

    menu:
        "Ela falou pra eu esperar, mas eu sou ansioso demais!":


            pass

    mc "Tem que ter alguma coisa que eu possa fazer! Influenciar de alguma forma!"

    "Ronaldo" "Tá falando sozinho, [mc]?"

    scene black with dissolve

    scene no2_ronaldo1 with dissolve

    mc "N-não! HAHA!"

    "Ronaldo" "Eu, hein... calma que vai dar tudo certo."

    mc "C-claro... hahaha..."

    "Vexame. Eu preciso descobrir quem são os donos da revista, os investidores. Virar a balança eu mesmo!"

    "Se eu puder fazer a cabeça deles, talvez eu consiga..."

    mc "Vou dar uma olhada no site da revista."

    scene black with dissolve

    scene sofiaf31 with dissolve

    mc "Deixa eu ver... Quem Somos... Aqui tem os nomes da diretoria. E aqui... Conselho de Administração..."

    "Também chamado de mesa de diretores, o Conselho é responsável por representar os investidores e avaliar o CEO da empresa, que no caso é o Editor Chefe."

    "Balela... deixa eu ver quem são esses fdps."

    mc "..."

    mc "Mauro Ribeiro?! Esse nome..."

    if so6_mae_ligou != 1:

        scene black with dissolve

        scene sofiaf33 with dissolve



        mae "Eu trabalhei com o Mauro há muito tempo. A gente... se ajudava. Ele ficou me devendo uma."

        mae "E o Escobar acabou pagando no lugar dele."

        scene black with dissolve

        scene black with dissolve

        scene so6_img0 with dissolve

        "Mauro Ribeiro... o antigo editor-chefe... ele conhecia minha mãe!"

    "E ele é um dos donos da revista! Eu posso começar por ele... sim... se eu fizer a cabeça dele eu posso garantir o que eu quero!"

    "Eu preciso falar com ele. Agora!"

    "Vou ligar pra revista e tentar marcar uma reunião."

    "..."

    scene black with dissolve

    scene mc bar_celular with dissolve

    "Telefone" "{i}Tu... tu... tu...{/i}"

    mc "Alô? É do escritório do Sr. Ribeiro? Eu gostaria de marcar uma reunião com o senhor Mauro."

    "..."

    mc "Isso! Sim, um dos membros do conselho."

    "Secretário" "Sinto muito, senhor, mas o senhor Ribeiro não está recebendo ninguém no momento."

    mc "Mas é importante. É sobre a revista e o futuro dela! Ele vai querer!"

    "Secretário" "Compreendo, mas as ordens são claras. Sem reuniões."

    mc "..."

    mc "Merda... e agora?"

    "Secretário" "Como é?"

    mc "N-nada, não! Hahaha..."

    "De novo eu tô fazendo isso? Tô mais tapado que o normal."

    "E agora? O que eu faço? Ele conhecia minha mãe. Será que..."

    menu:
        "Desistir de falar com ele":


            t "Isso vai pular boa parte do Encontro. Se não ter certeza, volte e escolha a outra opção."

            jump so6_mauro_depois
        "Usar a cartada da sua mãe":


            pass

    mc "Diga a ele que é o filho da Helena [mcsnome]."

    "Secretário" "Eu não entendi, senhor. Pode repetir?"

    mc "Helena [mcsnome]. Diga que o filho dela quer falar com ele. É urgente."

    "Secretário" "Senhor, eu já disse que o senhor Ribeiro..."

    menu:
        "Desistir e falar pra ele esquecer":


            t "Isso vai pular boa parte do Encontro. Se não ter certeza, volte e escolha a outra opção."

            jump so6_mauro_depois
        "Forçar ela a falar pro Mauro da sua mãe":


            pass

    mc "Por favor! É importante! Diga que é o filho da Helena! Ele vai entender!"

    "Secretário" "..."

    mc "Vai! Ou ele vai ficar bravo contigo!"

    "Secretário" "Um momento, por favor."

    scene black with dissolve

    scene n8_img13 with dissolve

    "..."

    "..."

    "..."

    "Será que vai funcionar?"

    "Caramba... eu tô mó nervoso..."

    "..."

    "Secretário" "Senhor?"

    mc "S-sim?"

    "Secretário" "O senhor Ribeiro vai recebê-lo. Hoje à tarde, às 15h. No escritório dele."

    mc "Sério?! Consegui! Valeu!"

    "Secretário" "Ele... ele pediu para avisar que a conversa será estritamente profissional."

    mc "Claro... claro... não se preocupe. É sobre a revista mesmo."

    "Secretário" "Certo. Até mais, senhor."

    mc "Até."

    scene black with dissolve

    scene n8_img38 with dissolve

    mc "Funcionou! Ele vai me receber!"

    mc "Ainda bem que eu lembrei da minha mãe. Agora eu tenho uma chance!"

    gar "Ao que me indicam os ventos vindos do vosso lado, vosmecê conjectura grande tramóia."

    menu:
        "Vou ter a chance de falar com o cara mais velho da revista! O lendário Mauro Ribeiro!":


            pass

    mc "Ele foi o mentor do chefe e ainda conhece minha mãe. A ponto de querer falar comigo!"

    gar "Meus pêsames..."

    mc "P-por que 'pêsames'? Era o que eu queria!"

    gar "Ora, ora... meus pêsames."

    mc "Sai pra lá! Deixa eu me preparar."

    mc "Tenho que descobrir tudo o que puder sobre ele, sobre a revista e até... sobre a minha mãe."

    if venda_revista >= 2:

        mc "Se a revista for mesmo ser vendida, é bom eu me aproximar de quem realmente manda nela."
    else:


        mc "Ele é a minha única chance de impedir a venda. É agora ou nunca."

    gar "Rogo que a deusa acompanhe vossos passos."

    menu:
        "Bora falar com esse Mauro! Que te carca atrás do armauro!":


            pass

    gar "..."

    mc "Não resisti!"

    scene black with dissolve

    scene so6_img3 with dissolve

    mc "..."

    mc "Aqui estou, esperando pelo lendário Mauro Ribeiro."

    mc "Será que ele é do Grupo? Acho que não. Ele parece íntegro pelo que o chefe e a minha mãe disseram... mas vai saber."

    mc "E se ele for como o Barão? Ou pior? Ugh... é difícil lidar com essas pessoas de ego."

    mc "Preciso manter a calma. Ele é a chave para entender o que está acontecendo com a revista."

    mc "E com a Sofia..."

    "..."



    mr "[mcc]?"

    mc "Opa!"

    scene black with dissolve

    scene so6_img4 with dissolve

    mc "Senhor Ribeiro?"

    mr "Impressionante... Você tem os olhos da sua mãe."

    mc "S-sério? O senhor conheceu minha mãe?"

    mr "Helena [mcsnome]... Uma grande mulher. Uma jornalista excepcional."

    mc "Caramba..."

    mr "Você parece surpreso. Sente-se, [mcc]. Temos muito o que conversar."

    mc "Tá."

    "Ele me analisa com um olhar atento. Como se pudesse ver até minha alma. Esse cara... tenho que tomar cuidado com ele."

    "Será que ele sabe? Sobre a Cássia... sobre a Sofia... sobre tudo?"

    menu:
        "O senhor é um dos investidores da revista, né?":


            mr "Sim. Eu e um grupo de acionistas. Investimos na revista há muitos anos. Acreditamos no poder do jornalismo."

            mc "Mas agora... querem vender."

            mr "As coisas mudam, [mcc]. O mundo muda. A mídia impressa está morrendo. A internet é o futuro."

            mr "E... a Faux News... eles têm os recursos, a influência... eles podem levar a revista para outro patamar."

            mc "E te dar muita grana."

            mr "E cobrir tudo o que investimos, garantindo uma aposentadoria farta para mim, para o Escobar e os outros investidores."

            mc "Às custas da verdade?"

            mr "Moralismo barato não vale tanto quanto você pensa no mundo adulto."

            mr "A verdade é uma faca de dois gumes, [mcc]. Pode ser usada para o bem... ou para o mal."
        "Não quero saber disso":


            pass

    mc "A Sofia, é... a nova Coordenadora de Produção... ela não quer vender! Ela acredita na revista. No legado do pai dela."

    scene black with dissolve

    scene so6_img5 with dissolve

    mr "Sofia... que saudades..."

    mc "Hm?"

    mr "Eu a vi nascer, [mcc]. Eu sou o padrinho dela, inclusive. Você deve saber da minha história com o Escobar."

    mc "A-ah... O senhor é?"

    mr "Sim. Eu e o Escobar... temos uma grande história juntos... me perdoe, falar sobre isso está me deixando um pouco nostálgico."

    mc "Sem problemas. O que aconteceu?"

    mr "..."

    menu:
        "Vocês parecem ter sido bons amigos.":


            mr "Ainda somos. Não como antigamente, mas o carinho e a amizade permanecem."

            mc "O velho é meio chato... difícil de acreditar que ele manteve uma amizade por tanto tempo."

            mr "Hahahaha! Eu entendo perfeitamente."
        "O senhor não parece muito com o Escobar.":


            mc "O senhor parece... mais leve."

            mr "É o que estar aposentado faz com a gente, [mcc]. Hahaha..."

            mr "Mas eu o treinei. E ele sabe o que fazer. Eu confio nele."

    mr "Ser editor faz isso com a gente. Pode acreditar em mim."

    mr "É cansativo, desgastante. Tudo cai nos seus ombros. Você não entende como minha vida mudou para melhor quando deixei isso pra trás."

    scene black with dissolve

    scene so6_img6 with dissolve

    mc "Mas a Sofia..."

    mr "Sofia é uma idealista. Ela quer justiça, mesmo que tenha que mudar tudo pra conseguir. Ela sempre foi assim, desde pequena."

    mr "Extremamente mi... bem... digamos que ela quer as coisas do jeito dela."

    menu:
        "Nunca é ruim lutar pela justiça.":


            mr "Mas o mundo não é assim, [mcc]."
        "Você tá falando que ela é meio 'chefinha'?":


            mr "Haha... você conhece a peça. Ela pode ser meio mandona."

            mc "Com certeza."

    mr "O mundo é dos fortes. Dos que têm coragem de fazer o que é preciso. E a Sofia é forte."

    mc "Mas os objetivos dela parecem justos."

    mr "Não vou entrar nesse mérito. Existem muitas pessoas assim, capazes de fazer de tudo. E eu acho isso incrível."

    mc "Mesmo que isso signifique passar por cima dos outros?"

    mr "Às vezes... é necessário."

    mc "Você... me lembra certas pessoas."

    "Ele fala como a Cássia... Mauro, você também é do Grupo? Seremos amigos ou rivais?"

    mr "Bem... meu tempo é curto. Mas foi incrível reviver um momento tão incrível da minha vida. O passado realmente sempre vem conosco. Eu agradeço."

    "Não! Você não pode ir assim! Eu..."

    menu:
        "E a revista? O que acontece com ela?":


            pass

    scene black with dissolve

    scene so6_img7 with dissolve

    mr "Eu investi todo o meu dinheiro nessa revista, [mcc]. E eu preciso que ela dê lucro."

    mr "Eu confio no Escobar. Ele é o editor-chefe. Ele sabe o que é melhor para a revista."

    mc "E se ele decidir vender?"

    mr "Então a revista será vendida. É simples assim."

    mc "Mas e a Sofia? E os funcionários? E a verdade?"

    mr "A verdade é uma ilusão, [mcc]. Uma história que contamos para nos sentirmos melhor."

    mr "O que importa é o resultado. O lucro. O poder."

    mc "..."

    mr "Eu entendo sua preocupação, [mcc]. Mas você precisa entender... o mundo não é um conto de fadas."

    mc "Eu sei..."

    mr "Você tem potencial, [mcc]. Eu vejo isso em você. Você me lembra sua mãe."

    mc "Minha mãe? A gente não se fala muito, sabe?"

    "Por que eu tô falando isso pra ele?"

    mr "Hmm... Você quer saber sobre ela, tá me parecendo."

    mc "Sim."

    "Ele vai me revelar? Assim? O que ela nunca me contou?"

    mr "Helena era uma grande jornalista. Corajosa, determinada, apaixonada pelo que fazia."

    mr "Ela acreditava na verdade, na justiça... como você."

    mr "E ela pagou o preço por isso."

    mc "Q-quê?! O que aconteceu?"

    mr "Ela descobriu algo... algo que não devia. E eles a silenciaram."

    mc "Eles?! O Grupo?!"

    mr "O Grupo, [mcc]. Eles estão em todos os lugares. Eles controlam tudo."

    mr "Eles não vão deixar ninguém se intrometer em seus planos."

    mc "..."

    mr "Acho que eu falei demais. Aposto que Helena não ia qu-"

    menu:
        "POR FAVOR! EU PRECISO SABER!":


            mr "..."

            mc "Eu tenho direito. Saber de onde eu vim."

            scene black with dissolve

            scene so6_img8 with dissolve

            mr "Não é justo com Helena [mcsnome] que a história dela seja enterrada porque ela é uma cabeça dura."

            mc "V-você vai contar?"

            mr "Se você prometer guardar segredo. Um acordo entre dois homens honestos."

            mc "Feito."

            mr "Sua mãe... ela era jovem e idealista. Tinha acabado de se formar na UFC. Ela acreditava que o jornalismo podia mudar o mundo."

            mc "UFC, a Federal da Capital. Foi lá que eu me formei também."

            mr "Eu também, o Escobar também. Veja só como são as coisas."

            mc "Desculpe, continue."

            mr "Sua mãe se dedicou ao jornalismo de corpo e alma. Ela investigava, denunciava, expunha a verdade."

            mr "Eu vi o potencial dela e a trouxe pra revista que eu tinha acabdo de fundar."

            mr "Meu feeling tava correto. Ela virou uma pedra no sapato dos Donatello. Eles a odiavam."

            mc "E o que aconteceu?"

            mr "Ela descobriu algo sobre um deles. Não lembro se era sobre Vittorino ou o Patriarca. Algo que poderia destruí-lo."

            mc "Vittorino... ele é pai do Basílio? Do atual prefeito?"

            mr "Sim... digamos que ele tinha um segredo. Um segredo que ele faria qualquer coisa para proteger."

            mc "E a minha mãe..."

            mr "Ela ia expor esse segredo. Ela ia publicar uma matéria que ia acabar com ele. Talvez com todos eles."

            mc "E por que el-"

            mr "Eles a impediram."

            mc "Como?"

            mr "Eles te ameaçaram. Disseram que se ela publicasse a matéria, eles iriam atrás de... bem, de você."

            scene black with dissolve

            scene so6_img9 with dissolve

            mc "!!!"

            mr "Ela teve que fazer uma escolha, [mcc]. E ela escolheu você."

            mr "Ela abandonou a matéria. E saiu da cidade. Para proteger você."

            mc "Eu não sabia..."

            mr "Ela te amava mais que tudo, [mcc]. Você era a vida dela."

            mc "..."

            mr "E agora... a história se repete. Você está no meio de tudo isso. De novo."

            "Isso... é por isso que ela nunca me disse?"

            "Ela não queria... que eu... mãe..."

            mc "O senhor realmente gostava dela, Sr. Ribeiro."

            mr "Helena... que jornalista você seria..."

            mr "Enfim, aposto que ela poderia ter se tornado a editora, mas com a saída dela... Escobar assumiu o comando anos depois quando eu deixei o cargo."

            mr "Foi bem conveniente para ele. Mas tudo acabou dando certo. Ele se tornou um editor eficiente."

            mc "Mas ele... ele não é como a Sofia ou minha mãe."

            mr "Não. Escobar nunca se dobrou às forças que comandam a cidade, mas também nunca foi atrás dela, como sua mãe tentou fazer."

            mr "Ele é pragmático. Ou devia alguma coisa, não é mesmo? Hahaha... brincadeira."

            "O jeito que ele fala..."

            "Eu... tenho que pensar sobre tudo isso. É coisa demais. Mas antes, eu tenho que fazer o que eu vim fazer."
        "Não, eu não quero saber. Deixe o passado em paz.":


            mc "Não, senhor Ribeiro. Deixe o passado em paz. Eu não quero me envolver nisso."

            mr "Você tem medo, [mcc]? Medo da verdade?"

            mc "Não é medo. É... prudência. Eu não quero acabar como ela."

            mr "Entendo."

    mc "E agora? O que vai acontecer com a revista?"

    scene black with dissolve

    scene so6_img10 with dissolve

    mr "Eu sou o investidor com mais ações, [mcc]. Mas a decisão não é só minha."

    mr "O conselho... eles vão votar. E eles confiam no Escobar. Esse é o ponto crucial."

    mr "Eles apostam na integridade, na frieza e eficiência dele. Escobar foi treinado por mim, e tem feito um bom trabalho."

    mc "Realmente, não dá pra negar que ele manteve a revista em pé."

    mr "Ele sabe o que faz. E ele vai fazer o que for preciso para manter a revista viva."

    mr "Mesmo que isso signifique... vendê-la."

    mc "Então isso tá..."

    mr "A única coisa que poderia mudar isso... seria se descobríssemos algo sobre o Escobar."

    mr "Algo que abalasse a confiança dos acionistas nele. Algo que provasse que ele não é digno de confiança."

    mr "Negar a grana da Faux News requer a confiança de que a revista vai continuar lucrando por muitos anos."

    mc "Entendi... se eles não venderem, eles vão querer que a revista dê mais dinheiro do que a venda daria."

    mr "Exatamente. Tudo vai depender dele passar essa confiança para o Conselho. Provar que pode manter a revista lucrando por mais 20 anos."

    mc "E você acha que ele dá conta?"

    mr "Eu o treinei bem. Ele não comete erros."

    "O chefe... ele não me parece uma pessoa ruim. Ele é mala, mas ele me parece decente. Mas..."

    mc "E se ele fez algo no passado? Algo que ele escondeu? Algo... que o Grupo saiba."

    mr "O passado... às vezes ele volta para nos assombrar, [mcc]."

    scene black with dissolve

    scene so6_img11 with dissolve

    mr "Mas eu duvido que o Escobar tenha feito algo tão grave que pudesse manchar sua reputação."

    mr "E se ele tivesse feito, com certeza já teria aparecido. A Faux deve ter cavado toda a vida dele."

    mr "A não ser que alguém que saiba esteja tentando lucrar com isso. Mas teria que ser alguém próximo dele. Não... impossível."

    mc "Faz sentido..."

    mr "Agora, se me der licença, eu preciso ir. Tenho uma reunião com os outros investidores."

    mr "A resposta para todas essas dúvidas tá mais perto do que você imagina."

    mc "E-eita..."

    "O momento da verdade. Ele tá chegando."

    mc "Senhor Ribeiro... uma última coisa."

    mr "Sim?"

    mc "De qual lado o senhor tá? Pessoalmente? O senhor quer a grana rápida ou quer manter a revista?"

    mr "Eu vou fazer o que é melhor para a revista, [mcc]."

    scene black with dissolve

    scene so6_img12 with dissolve

    mr "Agora... por outro lado. E você? O que VOCÊ vai fazer?"

    mc "E-eu?"

    "Se ele tá perguntando pra mim, talvez minha resposta influencie ele de alguma forma!"

    "Vender ou não a revista. Tenho que me manter firme no meu objetivo."

    menu:
        "Eu vou apoiar a venda. É o melhor para o futuro da revista.":


            $ venda_revista += 4

            mc "Eu vou apoiar a venda, senhor Ribeiro. É o melhor para o futuro da revista."

            mr "Você é um rapaz inteligente, [mcc]. Sabe reconhecer uma boa oportunidade quando a vê."

            mr "A Faux News vai investir na revista. Vai torná-la mais forte, mais influente."

            mc "E eu quero fazer parte disso."

            mr "Eu sei. E é por isso que eu confio em você."
        "Eu vou impedir a venda. Eu vou proteger a revista. Custe o que custar.":


            $ venda_revista -= 4

            mc "Eu vou impedir a venda, senhor Ribeiro. Custe o que custar."

            mr "Você é um idealista, [mcc]. Como sua mãe. Mas o mundo não é lugar para idealistas."

            mc "Eu não me importo. Eu vou proteger a revista. E a Sofia."

            mr "Você está se colocando em perigo, [mcc]. O Grupo não vai tolerar interferência."

            mc "Eu não tenho medo deles."

            mr "Você deveria. Eles são mais poderosos do que você imagina."

            mr "Mas... se você está decidido... eu não vou te impedir."

            mr "Só tome cuidado, [mcc]. E não diga que eu não avisei."

            "Isso é um aviso? Ou uma ameaça?"

            mc "Certo..."
        "Eu ainda não sei. Preciso pensar.":


            mc "Eu ainda não sei, senhor Ribeiro. Preciso pensar."

            mr "Não demore muito, [mcc]. O tempo está se esgotando."

            mc "Eu sei..."

    mr "Boa sorte, [mcc]."

    mc "Obrigado, senhor Ribeiro."

    scene black with dissolve

    pause

    scene black with dissolve

    scene so6_img13 with dissolve

    "Eu saio da sala, sozinho com meus pensamentos."

    "E agora? O que eu faço?"

    "Eu sabia que essa conversa ia ser reveladora, mas... nem tanto haha..."

    "Loucura. Eu realmente acabei entrando em um lago profundo. Como eu acabei no meio disso tudo?"

    menu:
        "Deixa eu voltar...":


            pass

    mc "..."

    "Preciso de um tempo para pensar em tudo isso. Mauro, minha mãe, a revista, a Sofia, a Cássia... o Grupo..."

    "Tantas coisas acontecendo ao mesmo tempo... e eu no meio de tudo."

    scene so6_img14 with hpunch

    mc "Agh! D-desculpa."

    lu "..."

    mc "!!!"

    mc "Senhor Luca?!"

    lu "Hm? Quem é você?"

    mc "[mcc]... eu e a Sofia conversamos com o senhor na Faux!"

    lu "Ah, você é o rapaz da revista... junto da garota inocente."

    mc "Sim... e o senhor é Luca Alighieri, não é?"

    lu "Isso mesmo. O que faz aqui, paparazzo? Veio se juntar ao Mauro? Ele está prestes a tomar uma decisão muito importante."

    "Melhor não revelar tudo pra ele agora. Esse cara... ele me dá calafrios."

    mc "Eu... tô avaliando minhas opções, senhor Alighieri."

    lu "Hmm... esperto. Sempre bom manter as opções abertas."

    lu "Você me lembra alguém, [mcc]... Alguém que eu conheci há muito tempo..."

    mc "Minha mãe, Helena, talvez? Ela trabalhou na revista com o Mauro."

    lu "Ah, sim... Helena... Uma jornalista talentosa. Pena que se envolveu com as pessoas erradas."

    "Os olhos dele... é como se ele tivesse olhando pro passado. Ele também fez parte daquele rolo que tirou minha mãe daqui?"

    mc "Ela só queria fazer a coisa certa."

    lu "Certo e errado... conceitos tão subjetivos, não acha?"

    mc "..."

    scene black with dissolve

    scene so6_img15 with dissolve

    lu "Deixe-me dizer uma coisa, [mcc]. Esta cidade... ela é o que é graças a um delicado equilíbrio de poder."

    lu "Um equilíbrio que mantemos há gerações. Nós... o Grupo... garantimos que as coisas funcionem como devem."

    lu "E a revista... a revista é uma peça importante nesse quebra-cabeça. Sempre foi."

    mc "Ela... ela é o outro lado da balança."

    lu "Você já deve ter percebido que eu sou um homem que consegue o que quer, [mcc]."

    lu "E eu quero a revista. Cedo ou tarde, ela será nossa."

    mc "A-ah..."

    "Caralho. A forma como ele falou isso. É como... se eu tivesse tomado um soco no estômago."

    lu "Veja bem... eu sei sobre você também."

    mc "Q-quê?"

    if sayuri_final3:

        lu "Você fez um bom trabalho na Cidade Chinesa, [mcc]. Ajudou a Mestra a manter a ordem. O Grupo aprecia isso."

    elif sayuri_final2:

        lu "Você causou uma confusão desnecessária na Cidade Chinesa, [mcc]. Agora ela está sem liderança."

    if julia_final3:

        lu "Interessante sua aproximação com a Júlia. Ela permanece esperando o momento certo de cumprir sua parte em tudo isso."

    elif julia_final2:

        lu "A Júlia foi um erro. Uma peça defeituosa. Ela deveria estar aqui para cumprir a parte dela em tudo, mas desapareceu."

        "Eles ainda não acharam a Ju? Será que ela... não... não pode ser!"

        lu "Uma pena o que aconteceu com o Gevanni. Sua posição no banco era essencial. Bem, agora ele é passado."

    if diana_final3:

        lu "A Diana... uma cantora talentosa. Ela está no lugar dela, esperando o momento. Isso é perfeito."

    elif diana_final2:

        lu "A Diana... ela vai se arrepender de ter desafiado o Barão. E você também, por ter ajudado ela."

        mc "E-eu..."

        lu "Mas tudo ocorre bem. Antonio está no comando agora. Não é o ideal que o lixeiro cuide disso, mas... enfim."

    if nathan_final3:

        lu "Ajudar o Nathan a ficar com a Blergh! foi um movimento inteligente, [mcc]. A Zaza está satisfeita."

        lu "Investimos muito dinheiro na Blergh! e o retorno tem que vir, antes da próxima eleição, que está MUITO perto."

        lu "Você tem talento."

    elif nathan_final2:

        lu "Ajudar o Nathan a ficar com a Blergh! foi um movimento inteligente, [mcc]. A Zaza está satisfeita."

        lu "Investimos muito dinheiro na Blergh! e o retorno tem que vir, antes da próxima eleição, que está MUITO perto."

        lu "Você tem talento."

        "Ele não imagina que o Nathan tá infiltrado. Isso vai ser incrível."

    scene so6_img16 with hpunch

    "Ele... ele sabe de tudo! Caralho!"

    lu "Você se esquece de uma coisa, [mcc]. Ninguém engana o Grupo. Ninguém."

    lu "Nós sabemos de tudo. Vemos tudo. Controlamos tudo."

    lu "Nesta cidade, [mcc], nada acontece sem o nosso consentimento. Nada."

    lu "E você... você não quer se tornar uma pedra no nosso sapato."

    lu "Uma pedra que precisa ser removida."

    "De novo essa metáfora?"

    mc "E o Tony? O sobrenome dele também é Alighieri. Mas eu ouvi dizerem que ele é... o 'lixeiro'."

    mc "Hm?"

    "Por um segundo... um vislumbre de desgosto cruza seu rosto, como uma sombra rápida."

    scene black with dissolve

    scene so6_img17 with dissolve

    lu "Antonio... Ele carrega o sobrenome, sim. Mas isso não significa nada."

    lu "Não se engane, [mcc]. Neste mundo, nesta cidade, o nome é tudo. As pessoas morrem, o dinheiro acaba, o poder se esvai, mas o nome..."

    lu "O nome fica. Ele ecoa através das gerações. É um legado. Uma responsabilidade."

    lu "E não é qualquer um que merece carregar o nome Alighieri."

    "Ele fala com um desdém quase palpável, como se o próprio nome fosse uma relíquia... que foi profanada pelas mãos sujas do Tony."

    lu "Minha filha, ela era uma Alighieri. De sangue. Mas ainda assim, uma mulher."

    mc "Uma mulher..."

    lu "Emocionada. Fraca. Deixou-se levar por um... um... Ela desonrou o nome, me desobedeceu... e trouxe Antonio para o nosso ninho."

    lu "Ele é útil, sim. Sabe fazer o trabalho sujo. Mas ele nunca vai sentar à mesa. Nunca será um dos nossos de verdade."

    mc "Então o Tony nã-"

    lu "Ele não tem visão, [mcc]. Não tem a... grandeza necessária para entender o que realmente está em jogo."

    "Ele me olha profundamente, como se quisesse me ensinar alguma coisa realmente muito importante pra ele."

    scene so6_img18 with vpunch

    lu "Você entende, [mcc]? Entende a importância do nome? Do legado?"

    menu:
        "Sim. O nome, a família, elas sobrevivem. São sagrados.":


            lu "Muito bem."

            "Ele tá satisfeito com a minha resposta. Ufa."
        "Não. Nome, sobrenome, são só palavras. O valor tá nos atos.":


            lu "..."

            "Vejo a decepção nos seus olhos, mas ele não fala nada. Até que..."

            lu "Você é novo... ainda vai chegar sua hora."

    lu "Eu reconheço o seu... potencial."

    lu "Você tem talento, paparazzo. Você tem coragem. E você tem ambição. Qualidades que nós valorizamos."

    "O que ele tá fazendo?"

    lu "Então, eu vou te dar uma chance, [mcc]. Uma chance que poucos têm."

    lu "Uma chance de ser útil. De se juntar a nós."

    "Q-que pergunta é essa? Assim, na lata? Ele tá me testando?"

    lu "Pense bem, [mcc]. Pense no seu futuro. Pense no poder que você pode ter. Na influência. No dinheiro."

    lu "Pense na vida que você sempre sonhou."

    lu "E pense no que você vai perder se fizer a escolha errada."

    lu "A escolha é sua, [mcc]. Mas escolha com sabedoria."

    "E agora? O que eu faço?"

    menu:
        "Eu não tenho medo de vocês. A verdade tá escrita. E se eu morrer, todos saberão.":


            scene black with dissolve

            scene so6_img19 with dissolve

            mc "Eu não tenho nada pra proteger, como a minha mãe tinha a mim. Se vocês quiserem vir atrás de mim, que venham."

            mc "Mas a verdade tá escrita. E se eu morrer, todos saberão."

            "Luca me encara, mas eu não vejo raiva, desaprovação. Apenas... pena?"

            scene black with dissolve

            scene so6_img20 with dissolve

            lu "Você é jovem, [mcc]. Idealista. Acha que pode mudar o mundo com palavras, com jornalismo. Mas o mundo não se importa com palavras. Ele só se importa com poder."

            lu "Outros já tentaram nos derrubar, [mcc]. Outros mais fortes, mais influentes, mais ricos."

            lu "Adversários políticos, ativistas de direitos humanos, e agora até mesmo a Interpol... todos falharam."

            lu "Eles subestimaram nossa força, nossa determinação, nossa influência. Eles acharam que podiam nos expor, nos destruir, nos levar à justiça."

            lu "Mas eles estavam errados. Estamos aqui há séculos, [mcc]. E continuaremos aqui por muitos mais."

            lu "Eu só fico triste pelo seu futuro, [mcc]. Um futuro vazio. Infeliz. Porque você escolheu o lado errado da história."

            mc "E-eu-"

            lu "E a verdade só será publicada enquanto a revista for independente. Se ela for nossa, sua última segurança deixa de existir. Pense nisso."

            scene so6_img20 with dissolve

            lu "Segurança. Tire este garoto daqui."

            "Segurança" "Hm? O senhor é o que do nosso edifício?"

            lu "Agora, homem!"

            "Segurança" "S-sim, senhor!"

            scene black with dissolve

            "Segurança" "Vamos, garoto! Pra fora!"

            mc "E-ei! Quem é ele pra ordenar isso?! Isto é um prédio comercial!"

            "Segurança" "Cale a boca e dê o fora!"

            "Maldito Luca!"
        "Eu quero ficar do lado de vocês. Eu vou fazer o que for preciso para 'sentar à mesa'.":


            scene black with dissolve

            scene so6_img19 with dissolve

            mc "Pode confiar em mim, senhor Luca."

            scene black with dissolve

            scene so6_img20 with dissolve

            lu "Interessante... Vejo que você finalmente entendeu como as coisas funcionam, [mcc]."

            lu "O poder não se conquista com ideais vazios, mas com ações concretas. Com lealdade. Com determinação."

            lu "Você terá oportunidades de provar seu valor. De mostrar que é digno de se juntar a nós."

            lu "A primeira delas... é a revista. Garanta que a venda aconteça, [mcc]. E você terá dado um passo importante para se tornar um de nós."

    "Ele se afasta, me dando um último olhar de advertência. Um olhar que me faz tremer até a alma."

    scene black with dissolve

    scene so6_img22 with dissolve

    mc "Uau... que presença."

    "Então esse é o patriarca da família Alighieri... será que ele é o chefe do Grupo?"

    "O Tony sempre me pareceu tão forte, mas pro Luca ele não passa de 'lixo', um 'erro'."

    "Será que Luca é o homem que eu tenho que derrubar se eu quiser acabar com o Grupo?"

    "Ou o homem que eu tenho que convencer a me aceitar na mesa."

    "Eu sei o que eu quero com relação ao Grupo... mas eu sinto que tudo ainda pode mudar."

    menu:
        "Manter a mente aberta e ver o que acontece.":


            pass

    mc "Aliás... pera..."

    "O que o Luca Alighieri tava fazendo no mesmo prédio do escritório do Mauro Ribeiro?"

    mc "Será que eles... não... não pode ser..."

    mc "Será que o Mauro já se entregou?! Não é pos-"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "{i}Trr trrr{/i}"

    if carro:

        scene black with dissolve

        scene carro_mc_cidade2 with dissolve
    else:


        scene black with dissolve

        scene cidade centro13 with dissolve

    label so6_mauro_depois:

        pass

    mc "Alô?! Sofia?!"

    w "[mc]! Pelo amor de Deus! Onde você tá?! A reunião vai começar!"

    mc "Sofia?! Calma! O que tá acontecendo?"

    w "Os investidores! Eles tão prontos! Todos eles! Vai ter uma videoconferência com eles agora!"

    w "O Mauro Ribeiro também! Ele é o representante do Conselho, [mc]!"

    mc "Mas... e a venda? Foi decidida?!"

    w "Eu não sei! Acho que eles vão decidir agora! Você precisa vir pra cá! Correndo!"

    mc "Mas eu tô no centro da cidade! Não tô na ilha!"

    w "Eu não me importo! Dá um jeito! Voa! Faz qualquer coisa! Mas vem pra cá agora!"

    w "A reunião tá começando! AGORA!"

    "{i}Tu tu tu...{/i}"

    mc "Tô indo! Sofia?!"

    mc "Merda! Merda! Merda!"

    mc "Eu não acredito! Justo agora! Eu preciso chegar na redação! Rápido!"

    scene cidade centro10 with hpunch

    "Corro pelas ruas da capital, o coração disparado, a respiração ofegante. Cada segundo é crucial."

    "Sofia precisa de mim. A revista precisa de mim."

    "E eu... eu preciso saber o que tá acontecendo."

    scene cidade tarde with hpunch

    "Finalmente chego na ilha. Corro para o prédio da revista. Tentando ignorar as pessoas me olhando me achando um doido."

    scene trabalho geral with hpunch

    "A redação tá... vazia? Procuro pela Sofia, mas não a vejo em lugar algum."



    scene so6_img21 with hpunch

    re "Ei, gato. Vai aonde com tanta pressa?"

    mc "R-renata?!"

    re "Você tá todo suado... Aconteceu alguma coisa?"

    mc "A Sofia... a reunião... cadê ela?"

    re "Ela tá lá dentro. Com o chefe. Entraram faz uns minutos."

    mc "Eu tô atrasado... O que você tá fazendo aqui? Você não vai pra reunião?"

    re "Eu? Não... A Cássia me mandou ficar aqui. Disse que eu não era necessária lá."

    mc "A Sofia me chamou... disse que a reunião ia começar..."

    re "Que mané, reunião, gato... Vem cá... deixa eu te mostrar uma coisa..."

    mc "Agora? Mas a Sofia..."

    re "Ninguém sabe que você chegou. Vai ser rapidinho... do jeito que você gosta..."

    mc "C-como é?"

    "Ela... tá querendo dar uma rapidinha? Eu entendi certo?"

    re "Eu sei que você quer, [mc]... a gente sempre teve... hmm... essa ligação."

    "A Renata... ela tá se oferecendo pra mim..."

    "Mas a Sofia... a reunião... a revista..."

    "Eu não posso me distrair agora. Não posso colocar tudo a perder."

    "Mas... e se essa for a minha única chance com a Renata? Vou recusar trepar com uma das loiras mais lindas que eu já vi?"

    "Droga... eu preciso decidir. E rápido."

    menu:
        "Vem cá, Renata. Vamos aproveitar que a redação tá vazia. Bem rápido!":


            $ venda_revista += 2

            $ renata_seduziu = True

            mc safado "Você me convenceu, Renata. Vamos aproveitar que a redação tá vazia."

            re "Eu sabia que você não ia resistir, gatinho..."

            re "Vem comigo... eu sei um lugar onde ninguém vai nos incomodar..."

            scene black with dissolve

            scene trabalho lounge with dissolve

            "A gente volta pro lounge dos funcionários, que ninguém vai. O cheiro é de papel velho e tinta de impressora, com o banheiro ali do lado."

            scene black with dissolve

            scene so6_img31 with dissolve

            re "Aqui é perfeito... ninguém vem aqui..."

            mc "Você... você já trouxe outros caras aqui?"

            re "Talvez... mas isso não importa agora. O que importa é que eu tô aqui... com você..."

            re "E eu quero você, [mc]. Agora."

            mc "..."

            scene black with dissolve

            scene sofiaf26 with dissolve

            "Ela se aproxima, seu corpo colado ao meu. Sinto o calor de sua pele, seu perfume doce e inebriante."

            re "Me beija, [mc]. Me beija como se não houvesse amanhã."

            mc "Renata..."

            re "Shiii... sem conversinha. Só me beija."

            "Seus lábios se encontram em um beijo urgente, cheio de desejo. As mãos de Renata exploram meu corpo, me puxando para mais perto, me despindo..."

            mc "Ahh... Renata..."

            re "Você gosta, né? Gosta de sentir meu corpo no seu?"

            mc "Muito... você é tão... quente... tão gostosa..."

            re "E você é tão duro... Tão forte... Me fode, [mc]! Me fode logo!"

            "Ela me puxa para um canto escuro da sala, onde as sombras nos escondem de olhares indiscretos."

            re "Me come, [mc]... me come como se eu fosse sua..."

            mc "Você é minha, Renata... toda minha... vou te foder todinha."

            "Eu a pressiono contra a parede, sentindo seu corpo tremer sob o meu toque. Minhas mãos exploram suas curvas, seu calor, sua maciez."

            re "Aahnn... [mc]... isso... aahnn..."

            mc "Você gosta, né? Gosta que eu te toque assim?"

            re "Muito... aahnn... mais... mais forte..."

            "Eu beijo seu pescoço, sentindo seu perfume, seu gosto... Ela geme baixinho, seu corpo se contorcendo contra o meu."

            mc "Você é tão gostosa, Renata... esse seu peitinho... essa sua bucetinha molhada..."

            re "Hmmm... você também, [mcc]... você me deixa louca..."

            "Sinto sua respiração acelerada, seu coração batendo forte contra o meu. Nossos corpos... unidos em um só ritmo..."

            mc "Eu quero você, Renata... agora..."

            re "Eu também te quero, [mcc]... eu te quero..."

            mc "Então, me mostra o quanto você quer que essa revista seja vendida!"

            re "Eu quero muito, [mc]... muito..."

            scene black with dissolve

            scene so6_img32 with dissolve

            "Ela se exibe todinha, revelando a buceta molhada pra mim."

            re "E então, safadinho... gostou do que viu?"

            mc "Você é linda, Renata... provocante... uma verdadeira tentação."

            re "Eu sei. E agora... eu sou toda sua. Faça o que quiser comigo."

            "Ela se encosta na estante de arquivos, as pernas levemente afastadas, os olhos brilhando de desejo."

            mc "Você gosta de ser mandada, né? De obedecer..."

            re "Hmmm... adoro... me diz o que fazer..."

            mc "Então deita nesse sofá e abre as pernas pra mim. Agora."

            re "S-sim... mestre..."

            scene black with dissolve

            scene so6_img33 with dissolve

            "Ela obedece prontamente, deitando-se no sofá e abrindo as pernas, se oferecendo completamente a mim."

            mc "Eu adoro mulheres assim... submissas... que fazem tudo o que eu quero..."

            re "Eu faço... eu juro..."

            re "Você tá me lembrando a Cássia... do jeito que ela manda... que ela domina..."

            mc "A Cássia, é? Então você gosta de uma mulher no comando também?"

            re "Ela sabe ser dura quando precisa."

            mc "Eu sei ser bem mais duro que ela. Quer ver?"

            re "Hmmm... tô louca pra saber. Eu quero."

            mc "Isso... bem vadiazinha... do jeito que eu gosto."

            re "Abre você... tô doida pra sentir ele dentro de mim..."

            mc "Vou rasgar essa buceta no meio, sua puta..."

            re "Arromba, [mcc]... arromba essa buceta... aahnn..."

            mc "Agora olha pra mim e chupa meu pau. Bem gostoso."

            re "Tudo o que você quiser, [mcc]."

            scene black with dissolve

            pause 1.0

            scene so6_img34 with dissolve

            "Ela se ajoelha na minha frente, seus olhos fixos nos meus. Ela pega meu pau com as mãos, acariciando e brincando, e então leva até a boca."

            "Ela chupa com vontade, com força e paixão. Eu sinto sua língua quente, seus lábios apertando e sugando."

            re "Hmmm... que delícia, [mcc]... seu pau é tão grosso... tão duro..."

            mc "Você gosta, né, sua puta? Gosta de chupar uma rola bem grossa?"

            re "Aahnn... s-sim... eu adoro... chupo todinho... até você gozar..."

            mc "Então continua, vadia... me chupa até eu não aguentar mais..."

            "Ela continua, com ainda mais intensidade. Eu sinto meu corpo todo formigar, o prazer crescendo a cada segundo."

            mc "Aahnn... Renata... assim eu vou..."

            re "Aahnn... [mcc]... isso... aahhh... que delícia de pau..."

            mc "Chupa gostoso, vadia... chupa que eu vou gozar..."

            re "Hmmm... eu vou engolir tudo... todinho..."

            mc "Aaaahhh... isso... goza pra mim... na minha boca..."

            re "Hmmm... que delícia... você adora, né?"

            re "Goza, [mcc]... goza pra mim... quero sentir seu gozo..."

            mc "Eu vou gozar, sua safada... vou gozar na sua boquinha..."

            "Eu não aguento mais. Meu corpo explode em uma onda de prazer indescritível."

            scene so6_img35 with hpunch

            mc "AAAHHHH!!!"

            "Ela engole tudo, sem hesitar, sem reclamar. E continua me chupando, mesmo depois que eu gozo, como se quisesse mais."

            re "Hmmm... que delícia, [mc]... você tem um gosto ótimo..."

            mc "..."

            re "Agora é minha vez. Deixa eu te mostrar o que eu sei fazer."

            "Ela me puxa para cima do sofá, me fazendo deitar. Ela sobe em cima de mim, roçando sua buceta na minha barriga."

            re "Você vai se apaixonar por mim, [mc]. Eu vou te dar o melhor sexo da sua vida."

            mc "Eu não duvido, Renata..."



            re "Eu vou te levar ao céu... e você nunca mais vai querer voltar."

            scene black with dissolve

            pause 1.0

            scene so6_img36 with hpunch

            "Eu me ajeito em cima dela, e ela vai rebolando, guiando meu pau pra dentro dela. A sensação é incrível... Apertada, quente, molhada!"

            re "Aahnn... [mc]... isso... aahnn..."

            mc "Caralho, Renata... você é... aahhnn..."

            re "Sua... eu sou sua, [mcc]... faz o que você quiser comigo... aahnn..."

            "Ela se move em cima de mim, com um ritmo selvagem e apaixonado. Eu sinto meu pau latejando dentro dela, o prazer crescendo a cada investida."

            mc "Aahnn... mais rápido, Renata... mais forte..."

            re "Aahnn... [mcc]... isso... aahhh... que pauzão... me fode... me fode forte... aahh..."

            mc "Caralho, Renata... você é uma puta deliciosa..."

            re "Sua... eu sou sua, [mcc]... faz o que você quiser comigo... aahhh..."



            menu:
                "Dominar ela por completo":


                    $ venda_revista += 2

                    re "Aahnn... [mc]... isso... aahhh... que pauzão... me fode... me fode forte... aahh..."

                    mc "Caralho, Renata... você é uma puta deliciosa..."

                    re "Sua... eu sou sua, [mcc]... faz o que você quiser comigo... aahhh..."

                    mc "Aaaahhh... vou gozar de novo..."

                    re "Goza, [mc]... aproveita que você ainda tá duro! Goza pra mim... me enche de porra... aahhh..."

                    mc "Vou foder essa sua bucetinha gostosa até você viciar nela."

                    re "É assim que eu gosto, meu macho... me fode com força! Me fode como se eu fosse uma cadela no cio..."

                    mc "Você é minha putinha, Renata... minha cadelinha..."

                    re "Aahnn... sou... sua putinha... sua cadelinha... aahnn..."

                    mc "E as putinhas obedecem ao dono, não é?"

                    re "Sim, mestre... as putinhas fazem tudo o que o dono mandar..."

                    mc "Então geme pra mim, vadia... geme bem alto..."

                    scene so6_img37 with hpunch

                    re "Aaaahhhhnnn... [mcc]... mais forte... mais rápido..."

                    mc "Eu vou te arrombar todinha, sua puta... vou te deixar toda fodida..."

                    re "Faz isso, mestre... me arromba... me fode... aahnn..."

                    "Puxo seus cabelos com força, expondo seu pescoço, seu rosto contorcido em uma mistura de dor e prazer."

                    mc "Você gosta, né, sua safada? Gosta de ser tratada como uma vadia?"

                    re "Aahnn... s-sim... eu adoro, [mcc]... aahnn..."

                    "Ela geme, as unhas cravando em minhas costas, me puxando para mais perto, mais fundo."

                    mc "Eu vou te foder até você implorar pra parar, sua puta..."

                    re "Eu imploro, [mcc]... aaahhhnnn... eu imploro... mas não para... aahnnn..."

                    "Dou um tapa forte em seu rosto, o som estalando na sala vazia. Ela geme, surpresa e excitada."

                    mc "Você é minha, Renata... minha puta particular... eu vou te usar até te deixar toda marcada..."

                    re "Aahnn... faz isso, [mcc]... me marca... me deixa toda roxa... aahnn..."

                    "Outro tapa, mais forte, e ela se contorce sob mim, gemendo ainda mais alto."

                    mc "Você gosta, né, sua vadia? Gosta de apanhar enquanto é fodida?"

                    re "A-ahnn... s-sim, [mcc]... e-eu adoro... aahnn..."

                    mc "Então aguenta, sua puta... porque eu vou te foder até você gozar..."

                    "Aperto suas coxas com força, sentindo o calor de sua pele, a umidade entre suas pernas."

                    mc "Goza pra mim, Renata... goza..."

                    scene so6_img38 with vpunch

                    re "Aaaahhhhhnnn!"

                    "Seu corpo convulsiona sob o meu, seus gemidos ecoando pela sala."

                    mc "Isso... goza, vadia... goza pra mim..."

                    re "Aahnn... aahhhnnn..."

                    mc "Goza pra mim, Renata... goza pro seu dono..."

                    re "Eu vou gozar.. eu vou... aaahhhnnn!"

                    scene so6_img38 with vpunch

                    re "Aaaahhhhhnnn!"

                    "Ela se desfaz em meus braços, exausta, mas com um sorriso perverso no rosto."

                    mc "Caralho, Renata... você é..."

                    re "Sua... eu sou sua, [mc]... faça o que quiser comigo..."

                    mc "Aaaahhh... vou gozar..."

                    re "Goza, [cc]! Goza pra mim... me enche de porra... aahhh..."

                    re "AAAHHHH!!!"

                    "Ela se contorce em cima de mim, seu corpo tremendo em espasmos de prazer. Eu a seguro firme, sentindo cada contração, cada gemido, cada gota de suor."

                    scene black with dissolve

                    scene so6_img39 with dissolve

                    re "Ufa... isso foi... intenso."

                    mc "Você é... incrível, Renata..."

                    re "Você também, [mcc]... você também..."

                    "Ela se deita ao meu lado, ofegante, exausta, mas com um sorriso satisfeito no rosto."

                    re "Agora você entende por que eu quero tanto que a revista seja vendida?"

                    mc "Entendo... você quer uma vida melhor."

                    re "E você? Vai me ajudar?"

                    mc "..."

                    "O que eu faço agora? Eu prometi a Sofia que ia impedir a venda... mas a Renata... e a Cássia..."

                    "E o Grupo... eu não posso me esquecer deles."

                    re "[mc]?"
                "Deixar ela e correr para a reunião.":


                    pass

            mc "Eu... eu preciso ir."

            re "Já? Mas a gente nem..."

            mc "Eu tenho que ir, Renata. A reunião... a Sofia... eu preciso..."

            re "..."

            re "Tudo bem. Eu entendo."

            mc "Desculpa..."

            re "Não se preocupa. Eu sei que você vai fazer a coisa certa."

            mc "..."

            scene black with dissolve

            scene trabalho lounge with dissolve

            "Eu me levanto, me vestindo rapidamente. Olho para Renata uma última vez, e saio da sala."
        "Eu não posso agora, Renata. Sem chance.":


            mc "Eu não confio em você, Renata. O que você quer de verdade?"

            re "Eu já disse! Eu quero que a revista seja vendida! Eu quero uma chance de crescer!"

            mc "E por que você tá me contando isso? Por que tá tentando me seduzir?"

            re "Porque... porque eu preciso de você, [mc]. Você tem influência com a Sofia, com o chefe... você pode fazer isso acontecer."

            re "E eu... eu pensei que você quisesse isso também... o poder... o dinheiro..."

            mc "..."

            re "Eu posso te ajudar, [mc]. Eu posso te dar informações, contatos... eu posso te apresentar às pessoas certas..."

            re "E eu posso te dar prazer! Um prazer que você nunca experimentou antes..."

            mc "..."

            re "Pensa nisso, [mc]. Pensa no que podemos ser juntos. Ajuda a vender a revista!"

            mc "Tá bom! Agora sai!"













    scene black with hpunch

    "A reunião!"



    scene so6_img23 with hpunch

    mc "D-desculpa!"

    w "[mc]! Finalmente! Que demora!"

    mc "Desculpa, Sofia! Eu..."

    if renata_seduziu:

        "Meu Deus! Eu devo ter perdido a reunião inteira por causa da Renata!"

        "A Sofia vai me matar!"

    b "Chega de conversa! Estamos no meio de uma reunião!"

    mc "A-ah... perdão."

    w "..."

    "A sala tá em silêncio. Todos os olhares tão voltados pra mim."

    "O chefe, com uma expressão cansada e derrotada. Sofia, com os olhos vermelhos e inchados, segurando as lágrimas."

    "E, na tela, Mauro Ribeiro, com uma expressão séria e compenetrada. Ao lado dele, na mesma tela, Luca Alighieri. Então eles tão juntos?!"

    "A vídeo chamada... consigo ver vários rostos desconhecidos. Devem ser os outros investidores."

    scene black with dissolve

    scene so6_img24 with dissolve

    mr "Como eu estava dizendo... a proposta da Faux News é de 10 milhões de dólares pela compra total da revista Capital."

    "Investidor" "Dez milhões?! Isso é um valor exorbitante! Parece irreal!"

    lu "Isso mostra o comprometimento que a Faux Corporation tem com o trabalho que foi empenhando na revista até hoje."

    lu "Nós acreditamos no potencial da Capital. E queremos investir no seu futuro."

    mr "O valor está no papel, senhores. E é real."

    "..."

    "Tá todo mundo quieto e a sala fica pesada. Sofia parece prestes a desabar. Cássia exibe um sorriso de satisfação quase imperceptível."

    "O chefe... ele olha pra mim, com uma mistura de resignação e... esperança?"

    "Dez milhões... é muito dinheiro... Será que a revista vale tudo isso?"

    "Ou será que a Faux News está desesperada pra colocar as mãos nela? Dinheiro não faz diferença pra eles."

    "E agora? O que eu faço?"

    menu:
        "Falar alguma coisa, qualquer coisa!":


            mc "E-{nw}"
        "Ficar em silêncio":


            pass

    mr "Eu entendo que o valor é alto. Mas todos aqui devem recordar. A Revista Capital lucrou muito mais do que isso em todos esses anos."

    mr "Além de ser uma marca sólida, com um público fiel e uma reputação impecável."

    "Investidor 2" "É verdade. Sob a direção de Mauro e do Escobar, a revista foi extremamente lucrativa nas últimas décadas."

    "Investidor 3" "Concordo. Se o senhor Escobar nos prometer que a revista continuará dando lucro, mesmo com o avanço da internet e das redes sociais, o valor, embora alto, ainda é menor do que o potencial da revista."

    scene black with dissolve

    scene so6_img25 with dissolve

    j "Escobar está cansado. Ele não é mais o homem que costumava ser. Isso eu garanto. Sou sua principal editora."

    b "Cássia?!"

    w "Isso é mentira! Meu pai é um grande jornalista e um ótimo administrador! Você é uma víbora, Cássia! Uma aproveitadora!"

    b "S-sofia? O que você tá fazendo, garota?!"

    mr "Escobar, você está treinando ela para ser a próxima a carregar nosso legado, não está?"

    b "Sim, mas..."

    mr "Queremos conhecer ela."

    b "Que seja... fale, garota."

    w "M-muito bem."

    w "Eu me preparei, pai, Conselho. Eu estudei fora, me atualizei. Estou pronta para seguir seus passos e os do senhor Ribeiro. Eu sei como conduzir a revista nessa nova era da internet."

    mr "Então nos di-"

    scene so6_img25 with hpunch

    w "Já estou investindo nas redes sociais, criando conteúdo exclusivo para o site, implementando um sistema de {i}memberships{/i} para os leitores mais fiéis..."

    w "Nosso número de seguidores cresceu 20%% no último mês! E nossa receita online vem crescendo 5%% por mês nos últimos 6 meses, sem sinal de queda."

    w "Eu posso garantir que a revista continuará lucrativa, e ainda manter a ética e a responsabilidade que sempre foram a marca registrada da Capital, desde a época do senhor Ribeiro."

    "Ela fala com paixão, com convicção. Mas será que isso é suficiente?"

    "Os investidores se entreolham, em silêncio. Mauro Ribeiro observa Sofia atentamente. Não consigo ver na expressão dele o que ele tá pensando. Saco."

    "Então Sofia olha pra mim, buscando apoio... É a minha vez. Eu preciso falar."

    if renata_prometeu:

        "Eu também prometi pra Renata que ia ajudar a vender a revista. Eu... quem eu vou decepcionar?"

    menu:
        "Sofia, eu vi seu trabalho. O chefe, digo, Escobar e depois você vão continuar dando lucro pra todos!":


            $ sofia_amizade += 3

            $ venda_revista -= 2

            scene black with dissolve

            scene so6_img27 with dissolve

            mc "Eu acredito na Sofia. Eu vi o trabalho dela de perto. Ela tem a garra, a inteligência e a integridade necessárias para conduzir a revista."

            mc "Ela entende do novo jornalismo, das novas mídias. Ela sabe como se comunicar com os milenials e a geração Z."

            mc "E a equipe... bom... mem todos 'gostam' dela... mas todos respeitam ela."

            mc "Eu não tenho dúvidas de que, sob a liderança da Sofia, a revista vai continuar prosperando."

            w "Obrigada, [mc]..."

            j "Que piada... você acha mesmo que essa garotinha mimada tem capacidade para liderar alguma coisa?"

            j "Ela nunca sujou as mãos na vida! Nunca teve que lutar por nada!"

            w "Isso não é verdade! Eu..."

            b "Chega! De novo vocês?!"
        "A revista precisa ser vendida. A Sofia não tem a experiência necessária. Peguem o dinheiro e curtam a aposentadoria.":


            $ venda_revista += 2

            mc "Eu entendo a sua paixão, Sofia. Mas eu concordo com a Cássia."

            w "[mc]! Como você pode?!"

            scene black with dissolve

            scene so6_img27 with dissolve

            mc "A revista precisa de uma mudança radical pra sobreviver a nova era da informação. E, com todo o respeito, você não tem a experiência necessária para isso."

            mc "A Faux News tem os recursos, a tecnologia, a influência... eles podem levar a revista a um novo patamar."

            j "Finalmente alguém sensato por aqui."

            mc "E eu... eu quero fazer parte disso. Eu quero essa oportunidade."

            w "Você é um traidor, [mc]! Um vendido! Você não se importa com a verdade, com a justiça, com nada!"

            b "Sofia! Já chega!"

            "Sofia me olha com desprezo, com decepção. Um olhar que me corta a alma."

            if sofia_namoro:

                w "E eu achando que você era diferente, [mc]... que você me amava..."

                mc "..."
            else:


                w "E eu achando que você era meu amigo, [mc]... que você me entendia..."

                mc "..."

    "Luca Alighieri permanece em silêncio, observando tudo com um olhar frio, sem se mover."

    "O desgramado sabe que não precisa dizer nada. Os números falam por si."

    "A oferta da Faux News é tentadora, irresistível para alguns. Uma tábua de salvação para uma revista que luta para sobreviver na era digital."

    "Mas a que custo?"

    scene black with dissolve

    scene so6_img28 with dissolve

    mr "Agradeço as palavras de vocês. Mas quem queremos ouvir agora é o homem que manteve essa revista lucrativa por todos esses anos."

    mr "Escobar, o que você nos diz? A revista vai continuar vendendo, seja impressa ou digitalmente?"

    mr "O futuro de vocês, ou melhor, de todos nós aqui, depende de você."

    mc "..."

    scene black with dissolve

    scene so6_img29 with dissolve

    "Todo mundo olha pro chefe. Mas ele não parece intimidado... ele já deve ter feito isso dezenas de vezes."

    "Ele me parece mais... cansado, exausto. Um homem que carregou um fardo pesado por tempo demais."

    "Tudo que ele queria era se aposentar, pegar a parte dele da compra da Faux e viver feliz a aposentadora. Acho que o Mauro também."

    "Mas... e agora?"

    "Esse é o momento da verdade. Tudo o que eu fiz até aqui... tudo o que eu disse... tudo o que eu escolhi... é pra este instante."

    "Se o chefe vender a revista... a Sofia perde tudo. O legado do pai dela... seu trabalho... tudo o que ela acredita..."

    "E a Cássia... o que ela vai fazer se o plano dela falhar? Plano B... qual será o plano B que ela falou?"

    "O que ela vai fazer comigo?"

    "E o Grupo? Eles não vão aceitar uma derrota assim. Eles vão revidar."

    "Eu lembro das palavras do chefe... 'o passado é melhor ficar guardado'..."

    "E as palavras do Mauro... 'às vezes precisamos fazer sacrifícios'... Será que esse é o momento do sacrifício?"

    "E as palavras de Luca... 'o poder não se conquista com ideais vazios, mas com ações concretas'..."

    "E a minha mãe... o que ela diria se tivesse aqui?"

    "Tantas vozes... tantas escolhas... tanto em jogo..."

    b "Bem... eu vou falar."

    mc "!!!"

    "O chefe... ele vai falar. E tudo será decidido."

    scene black with dissolve

    scene so6_img30 with dissolve

    if venda_revista >= 2:

        b "Eu... eu tomei uma decisão. E foi o [mc] que me ajudou a ver isso."

        b "Depois de muita reflexão, de muitas noites sem dormir, eu decidi..."

        b "Eu decidi que o melhor para a revista..."

        b "... é aceitar a proposta da Faux News."

        scene so6_img30 with hpunch

        w "O QUÊ?!"

        b "Eles têm os recursos... e outras marcas melhor posicionadas para os jogvens. Eles podem levar a revista a um novo patamar."

        b "Eu não posso mais fazer isso sozinho. A Sofia... ela não tá pronta."

        b "E eu estou cansado. Cansado de lutar, cansado de me preocupar."

        b "Eu quero paz. Quero me aposentar. Quero viver o resto dos meus dias sem essa pressão."

        b "Vou garantir que todos aqui lucrem o máximo com esse investimento e possamos ter uma boa vida a partir de agora."

        "Ele parece aliviado. Ele tá feliz."

        j "Você tomou a decisão certa, velho. Você não vai se arrepender."

        b "Eu espero que não, Cássia. Espero que não."

    elif venda_revista < 2:

        b "Eu... eu tomei uma decisão."

        b "Depois de muita reflexão, de muitas noites sem dormir, eu decidi..."

        b "Eu decidi que a revista não será vendida."

        scene so6_img30 with hpunch

        j "O QUÊ?!"

        b "Nós vamos continuar independentes. Vamos continuar lutando. Vamos continuar a fazer o que fazemos de melhor: jornalismo de verdade."

        b "Eu acredito na Sofia. Eu acredito que ela pode liderar a revista. E eu vou treiná-la, como o Mauro me treinou."

        b "E, nos próximos 30 anos, posso afirmar que essa revista vai continuar lucrando, e muito!"

        b "Mais do que esses 10 milhões que estão oferecendo! Esse valor não é nada perto do que a revista vale e vai valer!"

        b "E vou passar tudo que o velho Mauro me passou para que ela e o [mc] possam continuar seu legado e o meu."

        w "Pai..."

        mc "Chefe..."

        b "E eu espero que você, [mcc], esteja do nosso lado. Que você nos ajude a construir o futuro da revista."

        b "E você, Cássia... sem reclamação. Você também tem que continuar dando dinheiro."

        j "Velho desgraçado..."

    b "Mauro, conto com você."

    mr "Sempre, Escobar. Sempre."

    label sofia6_parte2_final:

        pass

    menu:
        "E agora?":


            if venda_revista >= 2:

                "Tutorial" "A atualização acaba aqui. A história da Sofia continua na próxima atualização."

                call ajuda_itchio

                jump sofia6_parte2_final
            else:


                pass

    scene so6_img40 with hpunch

    w "A gente conseguiu, [mc]! A revista... ela é nossa!"

    mc "Nossa! A gente conseguiu, Sofia! Você foi incrível!"

    w "Você também, [mc]! Sem sua ajuda, eu... eu não teria conseguido!"

    b "Eu vou sair daqui..."

    mc "Você foi demais lá na frente! Enfrentando a Cássia, o Luca... e ainda convenceu teu pai e o Mauro!"

    w "O velho tá cansado... mas ele é forte, [mc]! Ele vai aguentar até me passar o bastão!"

    w "Vou aprender tudo com ele e me preparar! Só quero ver o que a Cássia e a Faux vão aprontar."

    mc "Deixa eles. Agora o que importa é a gente. E a revista!"

    w "A revista... ela é tudo o que importa..."

    mc "Não, Sofia. Você também importa. Você é incrível. Você é..."

    if sofia_namoro:

        menu:
            "Beijar a Sofia para comemorar":


                mc "Vem cá!"

                scene so6_img41 with hpunch

                mc "!!!"

                w "!!!"

                w "[mc]... a gente tá namorando, mas..."

                mc "Desculpa... eu... não consegui me controlar. Você tava tão linda..."

                w "Eu... eu também... a gente conseguiu."

                mc "S-sim..."
    else:


        "Eu e a Sofia salvamos a revista. A gente tem os mesmos objetivos na vida."

        "Essa... talvez essa seja minha última chance de se declarar pra ela."

        "Será que ela aceitaria?!"

        menu:
            "Sofia... eu quero namorar contigo.":


                $ sofia_namoro = True

                w "Q-quê?!"

                mc "É sério. A gente vai cuidar da revista a partir de agora."

                scene so6_img41 with hpunch

                mc "S-sofia?!"

                w "[mc]... eu tô tão contente! Ok! Eu aceito! Eu quero você do meu lado agora!"

                mc "Eu vou tá do seu lado aqui na revista! Confia em mim!"
            "Não. Eu só quero amizade com ela.":




                "Não é ela que eu quero."

                "Podemos fazer muito como amigos."

    mc "A gente passou por tanta coisa... tantos desafios..."

    w "Lembra quando a gente se conheceu? Eu te tratei tão mal..."

    mc "E agora a gente tá aqui. Juntos. Vencedores."

    w "Você sempre acreditou em mim, [mc]. Mesmo quando eu duvidava de mim mesma, você tava lá, me apoiando."

    mc "E você sempre lutou pelo que você acreditava, Sofia. Mesmo quando tudo parecia perdido, você nunca desistiu."

    scene black with dissolve

    scene so6_img42 with dissolve

    w "A gente vai fazer a revista Capital ser o orgulho do jornalismo de novo! Pode apostar!"

    mc "Eu sei que vai. Com você no comando, a revista vai ser a melhor do país!"

    w "E quando eu assumir o comando..."

    mc "Hm?"

    w "A gente vai mudar tudo. Vamos acabar com as fofocas, com as matérias sensacionalistas..."

    menu:
        "Com certeza!":


            mc "Vamos focar em reportagens investigativas, em denúncias, em histórias que realmente importam..."
        "Mas será que é isso que eles querem?":


            mc "A revista tem que continuar vendendo."

            w "Deixa comigo, [mc]. Eu sei o que eles querem. Eu estudei."

            mc "Então tá."

    w "Vamos dar voz aos sem voz. Vamos mostrar a verdade, mesmo que ela doa. Mesmo que ela incomode os poderosos e o status quo."

    mc "Vamos fazer jornalismo de verdade, Sofia. Jornalismo que muda o mundo. Jornalismo como o do velho Mauro."

    w "E você vai estar lá, comigo, não vai, [mc]?"

    menu:
        "Claro que eu vou. Sempre.":


            mc "Sempre, Sofia. Eu tô com você até o fim."

            w "[mc]..."

            if sofia_namoro:

                w "Me beija... eu quero sua boca agora."

                mc "Sofia... vem..."

                scene ani22 with Dissolve(1.0)

            w "Eu... eu não sei o que dizer... você... você é..."

            mc "Eu sou o quê? Fala..."

            w "Você é... o parceiro que eu sempre quis ter. O homem que eu sempre sonhei."

            w "E a gente vai fazer história juntos, [mc]. Pode apostar."

            mc "Eu sei que a gente vai. A gente sempre dá um jeito."
        "Você esqueceu o que a Cássia disse? Eles são poderosos demais. Se a gente cutucar eles, a gente se ferra.":


            mc "Sofia... eu tô feliz da gente ter conseguido. Mas..."

            w "Mas...?"

            mc "A Cássia... lembra o que ela disse? Se a gente for contra o prefeito, o Tony, o Barão..."

            w "Eles vão se vingar."

            mc "Eles são poderosos demais, Sofia. A gente não pode simplesmente ignorar isso."

            w "Você tem razão. Eu... eu tava tão empolgada que acabei esquecendo disso."

            w "Mas a gente não pode ter medo deles, [mc]. A gente precisa lutar. Pela verdade. Pela justiça. Pelos nossos ideais."

            mc "..."

            w "Não podemos nos curvar ao poder deles, [mc]. A gente precisa..."

    j "{i}Cof cof{/i}"

    mc "!!!"

    w "!!!"

    scene so6_img43 with hpunch

    mc "Cássia... v-você ainda tava aqui?"

    w "Eu... eu tinha esquecido completamente..."

    j "Não queria atrapalhar a comemoração entusiasmada dos dois..."

    mc "Parece que alguém não gostou muito do resultado da reunião, né?"

    w "Você tentou manipular todo mundo, Cássia. Mas não deu certo. A revista... ela é nossa."

    j "Não cantem vitória antes da hora, pombinhos. A guerra ainda não acabou."

    menu:
        "A guerra pela revista acabou. A gente venceu. Você perdeu.":


            pass

    j "Vocês são uns idiotas. Vocês não fazem ideia do poder que..."

    w "Poder? Que poder? O poder do dinheiro? Da influência? Da manipulação?"

    w "A gente não precisa disso, Cássia. A gente tem o que importa. A verdade."

    mc "E a ética. A gente não precisa pisar nos outros pra chegar onde a gente quer."

    j "Ética? Vocês acham que ética vai pagar as contas? Vai garantir o futuro de vocês?"

    mc "Ética garante que a gente possa se olhar no espelho e ter orgulho de quem a gente é. Isso não tem preço."

    w "E a gente vai continuar lutando por isso, Cássia. A gente vai continuar fazendo jornalismo de verdade. Não as suas fofocas."

    j "Vocês são tão ingênuos... tão patéticos..."

    scene black with dissolve

    scene so6_img45 with dissolve

    j "Eu dou o que as pessoas querem. E elas querem fofocas. Elas não querem a verdade."

    mc "Patéticos? A gente? Olha quem está falando, a rainha da manipulação que acabou de perder tudo o que ela queria."

    w "Você subestimou a gente, Cássia. Você achou que podia nos controlar com seus joguinhos e suas mentiras."

    w "Mas a gente é mais forte do que você pensa. A gente tem valores. E a gente não vai se vender por nada."

    j "Essas frases de efeito me dão vontade de vomitar..."

    menu:
        "E agora, Cássia? Qual é o seu próximo passo?":


            pass

    j "Meu próximo passo... é fazer vocês se arrependerem de terem cruzado meu caminho."

    mc "A gente não tem medo de você, Cássia."

    w "Você pode ter o Grupo do seu lado. Você pode ter o dinheiro e o poder."

    w "Mas a gente tem a revista agora. Não importa o que a Faux faça, nós podemos contra-atacar."

    j "Idiotas... ingênuos..."

    mc "Hm?"

    scene so6_img46 with hpunch

    j "O que vocês estão comemorando, idiotas?! Vocês não venceram nada!"

    mc "?!"

    w "?!"

    mc "Como 'não vencemos nada'? A revista não foi vendida! A gente..."

    mc "Espera... Plano B?"

    w "Você perdeu, Cássia. Acabou. Você foi demitida. Não tem mais nada pra você aqui."

    w "A revista vai continuar. E vai ser melhor do que nunca. Sem você e suas mentiras, sem suas manipulações, sem seu..."

    mc "Alguma coisa não parece certo..."

    j "..."

    j "Ver vocês fingindo que são os virtuosos me dá NOJO! Vocês não sabem NADA!"

    mc "Como é? Sofia, espera."

    w "O quê? Ela merece! Ela tentou destruir a revista, destruir a minha vida! Ela é minha inimiga, [mc]! E vai ter o que merece!"

    j "Destruir? Eu? Quem destruiu minha vida foi ele! Aquele filho da puta!"

    w "Do que você tá falando, sua patética?!"

    scene ani23 with Dissolve(1.0)

    j "Seu pai! O Escobar! Aquele filho da puta! Ele é um monstro! Um canalha!"

    j "Merda... Ele nunca deveria ter assumido o lugar do Mauro! Ele não é digno! Ele não tem..."

    w "Meu pai?! Do que você tá falando, Cássia?! Para com essa palhaçada! Meu pai não é perfeito, mas ele é ético!"

    j "Palhaçada?! Ético?! Você acha que isso é palhaçada, garotinha?! Tá na hora de você sair do seu castelo nas nuvens e vir pra terra!"

    w "Eu não quero saber a porra que você vai inventar agora, sua desgraçada! Sai daqui!"

    menu:
        "Deixa ela falar, Sofia. Eu sinto que ela tem algo sério pra dizer.":


            w "Mas, [mc]... essa mulher é uma mentirosa! Uma víbora! Falsa!"
        "A Sofia tem razão! Cala sua boca e sai daqui, Cássia!":


            j "Calem a boca!"

    j "Eu era tão jovem... tão ingênua. Tinha acabado de me formar na Capital e consegui o estágio dos sonhos, aqui na revista."

    j "Eu queria ser jornalista. Eu sempre gostei de escrever, de contar histórias... igual vocês! E o Mauro percebeu meu talento!"

    j "Eu consegui um estágio na revista... o Mauro sempre foi tão educado. Mas ele... ele..."

    mc "O chefe?"

    scene black with dissolve

    scene so6_img44 with dissolve

    j "Ele era tão charmoso... tão inteligente... tão... poderoso... sempre ao lado do Mauro, sempre decidindo tudo."

    j "Eu o admirava. Via ele como um mentor... como um herói..."

    j "E ele... ele se aproveitou disso. Da minha ingenuidade. Da minha admiração..."

    w "Não... não vem com história, Cássia! O que meu pai fez?! Fala!"

    j "Foi só uma vez... uma noite que tava só a gente aqui... um erro..."

    w "!!!"

    j "Droga... Um erro que mudou minha vida pra sempre..."

    j "Eu engravidei."

    "[mc] e Sofia" "QUÊ?!"

    scene ani25 with Dissolve(1.0)

    j "Eu tava desesperada... com medo... não sabia o que fazer..."

    j "Meus pais... eles me deserdariam se soubessem. Eu estava sozinha na Capital... sem ninguém pra me ajudar..."

    j "Eu contei pra ele... pro Escobar... achando que ele... que ele faria a coisa certa."

    w "..."

    j "Mas ele... ele..."

    mc "Ele tem abandonou?"

    j "Ele me mandou abortar."

    w "Meu Deus! Não!"

    "A Sofia grita, desesperada, tremendo. Um som involuntário saindo da sua boca."

    mc "Abortar?"

    scene ani24 with Dissolve(1.0)

    j "O canalha disse que seria ruim pra imagem dele... pra revista."

    j "Que o Mauro nunca perdoaria ele se descobrisse que ele tinha engravidado uma estagiária..."

    w "Não... não pode ser..."

    j "Ele não se importou comigo... com o meu bebê... com nada..."

    j "O cretino só quis saber da sua posição na revista... com o poder... com a porra imagem dele!"

    j "Abortar! Vocês entendem isso?! Abortar! Minha filha!"

    menu:
        "Mas... isso nem é legal no nosso país...":


            pass

    j "E daí?! Ele queria que eu fizesse isso de forma clandestina! O filho da puta não tava nem aí! Ele só queria se livrar do problema."

    scene black with dissolve

    scene so6_img47 with dissolve

    j "Como eu ia fazer isso?! Matar minha própria filhinha?!"

    w "Chega... chega de inventar histórias!"

    j "Eu não sabia o que fazer... tava desesperada... sozinha..."

    menu:
        "E aí? Conta a história inteira, Cássia!":




            j "Foi a Zaza... ela me ajudou. Ela me apresentou ao Grupo. Disse que eles me protegeriam... protegeriam meu filho..."

            j "Eu me afastei da revista... tive meu filho longe dele... uma menina... uma bebê linda..."

            j "Ai..."
        "Chegar de mentiras! Você tá inventando tudo isso!":


            pass

    mc "Então... ela nasceu mesmo... e o Escobar?"

    j "Jamais ele poderia saber dela. Vai saber o que o louco ia fazer pra apagar a merda que ele fez."

    j "Eu a vendi pro Grupo. Eles sumiram com ela..."

    w "N-não..."

    j "Eu não sei onde ela tá... fazia parte da porra do contrato. Eu perdi uma parte de mim..."

    j "Mas pelo menos ela estava viva. Viva e... segura. Eles prometeram que iam cuidar dela. Que ela seria uma 'Sacerdotisa'. Que porra é essa?!"

    mc "Sacerdotisa..."

    j "Até hoje eu lembro... aquela bebê linda de cabelos como fogo... a pele clara... sardas desde pequena... perfeita..."

    j "Eu a entreguei pro Tony. Chorando. Sentindo o calor dela deixando meus braços. Pra sempre."

    j "E ele... com aquela expressão sem qualquer sentimento, como se tivesse segurando um quilo de cocaína."

    w "Não... Cássia... a gente não vai acre-"

    j "E o Escobar? O filho da puta ficou aliviado! Aliviado por se livrar de mim... da minha bebê... do problema que ele criou!"

    j "..."

    menu:
        "Foi assim que você voltou aqui?":


            pass

    scene black with dissolve

    scene so6_img48 with dissolve

    j "Pois é... o mundo dá voltas."

    j "Eu voltei pra revista... e ele, pra me calar, me deu o trabalho. Me deu poder. Influência. Me fez uma das principais jornalistas da Capital!"

    w "Eu não acredito... não dá pra acreditar! Meu pai não é esse monstro! NUNCA!"

    j "E vocês acham que esse... esse monstro... merece seguir os passos do Mauro?! Merece comandar a revista?!"

    w "Mentirosa..."

    mc "Sofia..."

    "Será mesmo que é mentira?"

    mc "E se... e se for verdade? Se o Escobar realmente fez isso?"

    mc "Meu Deus... a filha dela... uma bebê vendida pro Grupo."

    mc "O que a gente faz com essa informação, Sofia?"

    w "..."

    j "Vocês acham que o Mauro vai ficar parado quando souber disso? E os investidores? Qual vai ser o futuro da revista?!"

    j "O Escobar... ele destruiu tudo! A minha vida! A vida da minha filha! O futuro da revista!"

    j "Ele precisa pagar por isso. Ele precisa..."

    j "E eu vou garantir que ele descubra! Adeus pra vocês, ratos! Acobertadores de assassinos!"

    scene black with hpunch

    mc "Cássia!"

    scene so6_img49 with dissolve

    w "[mc]... não é possível..."

    w "É mentira! É tudo mentira! Ela não tem provas! Ela..."

    mc "..."

    mc "Sofia..."

    w "Não! Não pode ser... Meu pai... ele nunca..."

    mc "Sofia, escuta..."

    w "Não! Eu não quero ouvir! Eu não acredito nela! Ela tá mentindo! Ela..."

    mc "Pensa comigo, Sofia. A Cássia era tão jovem... tinha acabado de chegar na Capital."

    mc "E o teu pai era o braço direito do editor-chefe... poderoso, o chefe dela."

    mc "Ela admirava seu pai... via ele como um mentor. E a Cássia sempre curtiu transar. Tá na cara."

    mc "É fácil de imaginar qu-"

    w "Não... não é possível... para de falar."

    menu:
        "Tudo isso faz sentido, Sofia.":


            mc "E a forma como a Cássia entrou no Grupo... a Zaza a ajudou... a protegeu..."

            mc "Ela teve o bebê longe dele... em segredo... e depois o vendeu para o Grupo..."

            mc "Tudo isso... faz sentido, Sofia."
        "Ok... chega.":


            pass

    w "..."

    w "{i}Snif{/i}"

    mc "Sofia?"

    scene so6_img51 with hpunch

    w "Como!? Como eu vou aguentar isso, [mc]?!"

    w "Meu pai... ele sempre foi tão distante... tão frio!"

    w "Ele nunca ligou pra mim, nunca se importou! Me mandou pro exterior pra se livrar de mim!"

    "Ela fala com tristeza misturada com recentimento. Sua voz, falhando, mas forte, com uma raiva antiga, guardada no coração por tanto tempo."

    w "Mesmo com tudo isso, eu sempre me inspirei nele... no trabalho dele... no jornalismo."

    w "Esse trabalho é a única coisa que a gente tinha! Que a gente compartilha! A única ligação que eu criei com ele!"

    "Sua voz cada vez mais desesperada, perdida, triste e desolada."

    mc "Sofia..."

    w "Era a única coisa... que me fazia... amar ele..."

    w "E agora... agora eu descubro que ele fez isso... com uma garota... ainda mais jovem na época do que eu sou agora."

    w "Com outra mulher! Que só queria trabalhar na revista e admirava ele!"

    w "Se ela realmente falou a verdade... Como... c-como eu posso defender meu pai, [mc]?"

    w "A Cássia... ela é manipuladora! Mentirosa! Ela armou tudo isso! Ela..."

    mc "..."

    menu:
        "Vamos avaliar a situação... pensar com a cabeça e não o coração.":


            scene black with dissolve

            scene so6_img50 with dissolve

            mc "Se o Mauro descobrir isso, a revista tá acabada. Ele vende ela na hora pra Faux News."

            mc "Ele disse que só algo que destruísse a reputação do Escobar poderia mudar o resultado. E isso, Sofia, é justamente o que ele quis dizer."

            "Fico pensando se o Mauro sabia disso... se ele... talvez ele tivesse me alertando!"

            "E se a Cássia já falou com ele? E se ele sabia que na hora certa ela usaria esse Plano B?!"

            mc "A Cássia, ela sempre quis se vingar do teu pai. Ela odeia ele, te odeia, odeia todos que ficam entre ela e o poder."

            mc "Ela é capaz de qualquer coisa pra destruir tudo o que impede ela de conseguir o que quer. Ela é forte, manipuladora e fria."

            mc "Nada garante que esse não seja outro jogo dela. E se ela inventou isso pra justamente jogar a gente contra a parede. Por que ela revelaria isso?"

            w "Tem razão... por que ela contaria pra gente?"

            mc "Mas, e se for verdade? Se a gente acobertar isso, não estaremos sendo cúmplices?"

            mc "Como a gente pode falar de ética, de justiça, de verdade, se a gente esconder algo tão terrível, tão monstruoso?"

            mc "O que é mais importante? A revista? O jornalismo? Ou a verdade? A justiça?"

            w "Eu não sei! Eu não sei mais!"

            mc "Meu Deus... a filha dela... vendida pro Grupo..."
        "Precisamos tomar uma decisão no calor do momento!":


            pass

    mc "Seu pai... se for verdade... ele merece sair impune dessa?"

    w "!!!"

    scene black with dissolve

    scene so6_img52 with dissolve

    w "Eu... eu não sei o que fazer, [mc]. Me ajuda..."

    w "Eu devo acreditar na minha maior inimiga? Uma mulher que sempre me odiou, que sempre quis me destruir? Uma manipuladora sem escrúpulos?"

    w "Ou eu devo proteger meu pai? O homem que, apesar de tudo, eu amo? O homem que eu sempre corri atrás..."

    "Será que o chefe realmente nunca se importou com a filha? Será que isso tem a ver..."

    w "Se a revista for vendida, a Faux News vai controlar tudo! Vão manipular a informação, vão censurar a verdade, vão impor a narrativa dos Donatellos, do Grupo."

    w "A gente não pode deixar isso acontecer! A gente precisa proteger a revista! Proteger o jornalismo!"

    w "Mas, se a gente acobertar a verdade sobre o meu pai, como a gente pode se olhar no espelho?"

    w "O que eu faço, [mc]? Qual é o caminho certo?"

    menu:
        "É aqui... a decisão que vai mudar tudo.":


            pass

    scene ani26 with Dissolve(1.0)

    "O que eu faço agora?"

    "Se eu não acreditar na Cássia... eu posso convencer o Mauro que ela tá mentindo. Que tudo isso é uma armação pra destruir a revista."

    "A Cássia se emocionou demais. Ela acabou entregando o Plano B dela antes da hora."

    "Eu posso abafar essa história... esconder a verdade... e a revista continuaria sendo nossa."

    "A Sofia, ela seria feliz... e a gente... a gente... salvaria o chefe e garantiria que a revista continuasse com a verdade."

    "A gente poderia finalmente realizar nosso sonho. Juntos. Ela como editora-chefe. E eu... ao lado dela. Como sempre quis."

    "Seria o final feliz... pra mim, pra ela... pra revista."

    menu:
        "Mas e se a Cássia tiver falando a verdade?":


            "Se o Escobar realmente fez tudo aquilo?"

            "Se a gente acobertar isso... estaremos sendo cúmplices de um crime. De um ato monstruoso."

            mc "A gente sempre falou de ética... de justiça... de verdade... como a gente pode trair nossos próprios princípios?"

            "A gente vai conseguir viver com essa culpa? Como vai ser nossa relação?"

            "Algo em mim diz que a gente precisa descobrir a verdade. Como jornalistas."

            "A gente precisa encontrar a filha da Cássia. Descobrir o que aconteceu com ela. Se a história é verdadeira..."

            "E se for... será o fim do Escobar. O fim da revista como a gente conhece. Provavelmente a Faux News vai comprar tudo e..."
        "Eu não quero pensar nessa possibilidade":


            pass

    label sofia6_parte3_final:

        pass

    mc "Não existe meio termo. Não existe uma solução fácil. Eu preciso escolher um lado. E essa escolha... ela vai mudar tudo."

    menu:
        "Acreditar na Cássia, denunciar o chefe e perder a revista":


            $ sofia_final2_pre = True

            jump sofia_final2_pre
        "Negar a Cássia, proteger Escobar e ficar com a revista":


            mc "Sofia, eu não acredito na Cássia. Ela tá mentindo. Ela quer destruir a gente."

            w "Você... você acha mesmo, [mc]?"

            mc "Tenho certeza. Ela é manipuladora. A gente não pode cair no jogo dela."

            w "Mas... e se ela tiver falando a verdade?"

            mc "Ela não tem provas. A gente pode simplesmente negar tudo. E a Cássia não vai ter como provar nada."

            w "É... você tem razão. A gente precisa proteger a revista. Proteger meu pai. Proteger a gente."

            mc "Isso. A gente vai esquecer tudo o que ela disse e vamos seguir em frente. Juntos."

            jump sofia_final1

label sofia_final1:

    w "Você tem certeza?"

    scene black with dissolve

    scene ani27 with Dissolve(1.0)

    mc "Sim. Sofia, olha pra mim. A gente não pode fazer isso. Não podemos acreditar na Cássia."

    w "Mas, [mc]... e se for verdade? E se ele realmente fez aquilo com ela?"

    mc "Eu não acredito que o Escobar seria capaz de uma coisa dessas. Ele pode ser duro, insensível às vezes, mas..."

    w "Ele me mandou pra longe! Ele nunca se importou comigo! E se ele fez isso com a Cássia, ele é capaz de qualquer coisa!"

    mc "A Cássia é uma manipuladora, Sofia. Ela odeia o teu pai, ela te odeia. Ela quer destruir a revista. Ela quer se vingar."

    mc "Ela se sente injustiçada, desprezada. Ela acha que o teu pai arruinou a vida dela. Que ele a usou e depois a descartou. Ela quer que ele pague por isso."

    w "Mas... e a garota? E se ela realmente existir? E se ela estiver viva?"

    mc "A gente não tem provas, Sofia. A Cássia não apresentou nenhuma prova. Só a palavra dela. Contra a do teu pai. De quem você vai acreditar?"

    w "Eu... eu não sei..."

    mc "E se a gente destruir a vida dele por causa de uma mentira? E se a Cássia tiver inventado tudo isso? A gente não pode se arriscar."

    w "Mas..."

    mc "A gente vai proteger a revista, Sofia. A gente vai proteger o teu pai e também a verdade."

    menu:
        "A gente precisa pensar no bem maior.":


            pass

    scene black with dissolve

    scene so6_img53 with dissolve

    w "O bem maior... você tem razão, [mc]. A revista é mais importante do que qualquer coisa."

    w "Ela é o legado do meu pai. O trabalho de uma vida inteira. Eu não posso deixar isso ser destruído."

    mc "E tem os funcionários da revista, Sofia. Se a revista for vendida, eles perderão seus empregos. A gente precisa pensar neles também."

    w "Você tem razão. A gente não pode ser egoísta. A gente precisa fazer o que é melhor para todos."

    w "Mesmo que isso signifique... acobertar a verdade."

    mc "A verdade... ela pode ser uma arma perigosa, Sofia. Às vezes, é melhor deixar o passado no passado. Esquecer. Seguir em frente."

    "Foi isso que o Mauro e o Escobar me disseram. Deixar o passado pra trás."

    w "Esquecer... seguir em frente... você tem razão, [mc]. A gente vai esquecer tudo isso. A gente vai seguir em frente. Juntos."

    mc "Juntos, Sofia. Sempre."

    scene ani28 with Dissolve(1.0)

    mc "..."

    mc "Sofia... você tá bem?"

    w "Eu... eu não sei, [mc]. É muita coisa..."

    mc "Eu sei. Pra mim também. Mas a gente vai fazer o que acha certo. A gente..."

    mc "A gente decidiu se proteger. Proteger a revista. Proteger o teu pai."

    w "Mas... a que custo?"

    mc "A gente vai ficar bem. Eu prometo. A gente vai..."

    mc "A gente vai superar isso juntos."

    if sofia_namoro:

        w "..."

        w "[mc]..."

        mc "Sofia..."

        scene black with dissolve

        scene so6_img54 with dissolve

        w "Eu... eu preciso de você, [mc]..."

        mc "Eu também preciso de você..."

        w "A gente... a gente não devia..."

        mc "Eu sei... mas..."

        w "Mas..."

        mc "Eu quero você, Sofia. Agora."

        w "Eu também te quero, [mc]..."

        menu:
            "Você tem certeza?":


                mc "Você tem certeza, Sofia?"

                w "Tenho. Eu preciso disso... preciso de você..."
            "Eu não vou conseguir parar se você continuar me olhando assim.":


                w "E você quer parar?"

                mc "Não..."

        scene black with dissolve

        scene so6_img55 with dissolve

        w "Hmmm..."

        mc "Beijar você é uma delícia."

        w "Então beija, poxa... eu preciso de você."

        mc "Vou te beijar! Eu tô aqui pra você."

        w "Isso! Você precisa me agarrar, me beijar, me chupar. Igual um homem de verdade."

        mc "S-sofia... você tá tão sexy."

        w "Não! Você não viu nada ainda, gostoso. Eu... eu adoro sua boca. Eu gosto forte, entendeu?"

        "Ela tá me dando tanto tesão. Foi igual na casa dela... quando ela fica com tesão..."

        mc "Hmmm..."

        w "Eu sinto uma ligação com você, delícia. Algo que não consigo explicar. Como se a gente... tivesse ligado desde sempre."

        mc "É? Desde sempre?"

        w "Sim... agora me pega."

        scene ani29 with Dissolve(1.0)

        mc "Toma..."

        w "Aahh... isso... tô com tanto tesão, [mc]. Faz alguma coisa agora."

        mc "Faço, gostosa. Eu aperto esses peitos, mordo essa boca. Você vai ter tudo que você gosta."

        w "Ah... isso... eu gosto, eu quero assim... me obedece!"

        mc "Obedeço, amor.... gostosa..."

        w "Hmmnnggg..."

        menu:
            "Sofia. Eu quero te foder agora.":








                w "[mc]! Chega!"

                mc "O-oi?!"

                w "Não podemos fazer isso aqui! Aqui é o trabalho!"
            "A gente não devia fazer isso aqui. Não assim.":


                w "Eu sei! Eu sei!"

        mc "S-sofia..."

        w "D-desculpa. Eu quero ficar com você. Mas não aqui, né?"

        mc "Sim..."

        w "Mas... te beijar... me acalmou, sabia? Você... você é o melhor pra minha vida, [mc]."

        w "Você sabe o que fazer pra me deixar bem."

        mc "A gente precisava disso. E eu vou tá sempre do seu lado."

        w "Precisávamos. Pra... esquecer. Pra... recomeçar."

        mc "Recomeçar... juntos."

    w "Juntos."

    "Nossa escolha foi delicada... a Sofia é uma pessoa correta e ela vai precisar de um tempo pra digerir isso."

    "Espero que ela entenda que nós tomamos a decisão correta, pelo bem da revista e da Capital."

    "Não quero que ela se cobre, não quero que ela perca essa luta pela justiça. Não quero que ela mude."

    menu:
        "E eu preciso falar com o Mauro Ribeiro. Parar a Cássia.":


            pass

    mc "Eu vou indo nessa, Sofia. Preciso resolver isso logo."

    w "O que você vai fazer?"

    mc "Garantir que o bem vença. Vou falar com o Mauro e alertar ele sobre a mentira."

    w "A mentira da Cássia..."

    mc "Sim. Vai tudo certo. Você vai ver."

    w "Boa sorte... tomara que o Mauro veja a verdade. Conto com você, [mc]."

    mc "Deixa comigo."

    scene black with dissolve

    scene sofiaf31 with dissolve

    "É agora ou nunca. Se eu quero proteger a Sofia, proteger a revista, eu preciso fazer isso dar certo."

    b "Deu tudo certo, Renata. Você e sua chefe, a víbora, não conseguiram."

    mc "Hm?"

    scene ani30 with Dissolve(1.0)

    re "Que pena, senhor... parece que eu vou ter que me juntar ao mais poderoso..."

    b "Hmmm... eu aceitaria uma novinha do meu lado."

    re "Ai, senhor... o senhor é muito charmoso, sabia?"

    b "Charmoso? Haha... você é que é uma novinha deliciosa, Renata."

    mc "?!"

    "Aquilo é... o chefe e a Renata? E ela tá dando em cima dele? Que que tá acontecendo?"

    re "Ai, senhor... você é o chefe, você pode falar isso?"

    b "Eu sou o chefe, eu posso qualquer coisa, você sabe disso."

    re "Hihihi..."

    b "E essa sua roupa hoje... tá marcando tudo... hmm..."

    re "Senhor..."

    b "Você sabe que eu gosto de mulheres com carinha de bebê, Renata..."

    re "Gosta, é?"

    b "Tem uma novinha lá no bar que eu bebo, você consegue ser ainda mais gostosa que ela. E ela adora meus dedos."

    re "Ai, senhor... o que você faz com esses dedos, hein?"

    b "Quer que eu te mostre?"

    scene black with dissolve

    scene sofiaf32 with dissolve

    mc "..."

    "Você tomou sua decisão, [mc]! Não é hora de ter dúvidas!"

    "Tenho que marcar uma reunião com o Mauro Ribeiro!"

    mc "Senhor Ribeiro? É o [mc]."

    mr "Sim, [mc]. O que você quer?"

    mc "Eu preciso falar com o senhor. É urgente. É sobre a revista... sobre o Escobar."

    mr "O Escobar? O que aconteceu?"

    mc "É... uma coisa complicada, senhor. Eu preciso te contar pessoalmente. Pode ser agora?"

    mr "Agora? Mas já é tarde... O que é tão urgente assim?"

    mc "É sobre a Cássia, senhor. E... e uma acusação muito séria contra o Escobar. O senhor precisa saber."

    mr "..."

    mr "Tudo bem, [mc]. Venha até o meu escritório. Estou te esperando."

    "Eu tenho que fazer ele ver a verdade."

    scene black with dissolve

    scene so6_img56 with dissolve

    mc "Senho-"

    scene so6_img56 with hpunch

    mc "Luca!?"

    lu "[mc]..."

    menu:
        "Tá de saída?":


            lu "Sim. Tenho trabalho a fazer na Faux agora. Mais do que nunca."

            mc "..."

            mr "Boa sorte. E vamos conversar."
        "Parece que as coisas não aconteceram como você esperava.":


            lu "Ribeiro tomou a decisão que ele julgou a melhor."

            lu "Mas, se algo acontecer e ele mudar de ideia, nossa proposta ainda está de pé."

            mr "Manterei isso em mente, Luca. Obrigado por entender."

            lu "..."

            mc "Nada vai acontecer. A revista está em boas mãos, com Escobar."

    lu "Até mais, Ribeiro."

    mr "Até, senhor Alighieri."

    "O Luca não gostou nada do que aconteceu. Se fodeu, velho mafioso."

    "Eu venci. Só preciso completar minha missão agora."

    scene black with dissolve

    scene so6_img57 with dissolve

    "Sorte que esse idiota foi embora."

    mr "Pois então... o que houve?"

    mc "Senhor Ribeiro, eu preciso te contar uma coisa. E eu não sei como..."

    mr "O que foi, [mc]? A decisão já foi tomada. Tudo deu certo no final. Escobar vai continuar comandando, não é o que você queria?"

    mc "Sim, sim. Nós vencemos."

    mr "E então?"

    mc "É sobre a Cássia, senhor. Ela... ela fez uma acusação muito séria contra o chefe. Ela disse que..."

    mr "O passado..."

    mc "Sim. Ela disse que teve um caso com ele há alguns anos. Quando ela era estagiária na revista."

    mr "Com o Escobar... Mas isso é..."

    mc "E ela disse que engravidou, senhor. E que ele obrigou ela abortar. Disse que seria ruim pra imagem dele, pra revista... pro senhor."

    mr "..."

    mc "Ela disse que a Zaza a ajudou... que a apresentou ao Grupo... que eles protegeriam ela e o bebê..."

    mc "Ela teve a criança... uma menina... longe de tdos. E depois... vendeu a menina pro Grupo. Pra garantir que ela ficaria segura."

    mc "Ela voltou pra revista... e o Escobar... pra garantir que ela ficasse quieta... ele deu o cargo pra ela."

    mr "E por que você tá me contando tudo isso?"

    menu:
        "Porque é mentira. Tem que ser.":


            pass

    scene black with dissolve

    scene so6_img58 with dissolve

    mc "A Cássia... ela tá se vingando, senhor. Ela e perdeu e foi demitida. Ela quer destruir o Escobar. Destruir a revista. Destruir tudo."

    mr "Será que é tudo tão simples assim?"

    mc "O senhor saberia se alg-"

    mr "E você, [mc]? Você acredita nela?"

    mc "E-eu?"

    mr "Isso não vai mudar o que vai acontecer. Eu só quero que seja sincero comigo."

    menu:
        "Sim, eu acredito na Cássia. Mas temos que proteger a revista.":


            mc "Eu... eu não tenho certeza, senhor. Mas... eu acho que ela tá falando a verdade."

            mr "Se nem você tem certeza do que está dizendo, [mc], então eu vou ter que ouvir a Cássia e decidir por mim mesmo."

            mc "M-mas!"

            mr "Isso é sério, garoto. São vidas de pessoas reais. Crimes que podem ter sido cometidos. Acusações sérias."
        "Não, eu não acredito na Cássia.":


            mc "Não, senhor. Eu não acredito nela. Ela tá mentindo. Ela..."

            mr "Você tem certeza disso, [mc]?"

            mc "..."

            menu:
                "Tenho.":


                    mc "Tenho certeza, senhor. Ela tá inventando tudo isso pra se vingar."

                    mr "Muito bem, [mc]. Eu confio em você. Eu sei que você não me decepcionaria."

                    mr "Eu vou dar um jeito na Cássia. Ela não vai causar mais problemas."
                "Não tenho.":


                    mc "Eu... eu não tenho certeza, senhor. Mas... eu acho que é melhor o senhor ouvir os dois lados da história."

                    mr "Se nem você tem certeza do que está dizendo, [mc], então eu vou ter que ouvir a Cássia e decidir por mim mesmo."

                    mc "M-mas!"

                    mr "Isso é sério, garoto. São vidas de pessoas reais. Crimes que podem ter sido cometidos. Acusações sérias."

    mc "O Escobar, ele foi treinado pelo senhor. Ele sabe o que é certo, o que é ético. Ele não faria uma coisa dessas."

    mc "A gente não pode deixar que a Cássia e o Grupo destruam tudo o que o senhor construiu. A gente precisa proteger a revista."

    mr "Se formos por esse caminho, então temos que evitar qualquer problema. Escobar terá que deixar a revista."

    mc "S-sério? Mas..."

    mr "Você acha que ela tá pronta?"

    "A Sofia... ela tá pronta pra liderar a revista assim, tão cedo? E agora?"

    menu:
        "A Sofia tá pronta. Tenho certeza. Você viu na reunião.":


            pass
        "Eu não sei... talvez seja cedo pra ela.":


            pass

    scene black with dissolve

    scene so6_img59 with dissolve

    mr "Muito bem... obrigado por trazer essa informação para mim. Agora, tenho que tomar uma decisão importante."

    mr "O fato de você estar aqui e não Escobar ou Sofia, me mostra que você pode ser nosso trunfo na revista."

    mc "E-eu?"

    mr "Você tem o sangue da sua mãe. Eu conheço ela... talvez mais do que eu devesse."

    "Quê?! O que ele quer dizer com isso?! Ele e minha mãe..."

    mr "E eu te digo isso, para que você saiba que eu confio no seu potencial. Você herdou isso dela."

    mr "E eu posso te deixar um ensinamento. Todas nossas decisões vêm com consequências."

    mr "Se você decidir calar a Cássia, esquecer o passado, isso terá consequências para você, para a Sofia... para a cidade. Todos nós."

    mr "Você está aqui. Agora me diga, está pronto para as consequências?"

    "Eu entendo o que ele quer dizer... e agora é a hora de eu assumir minha decisão."

    "Qual será meu final, se eu escolher acabar com o Plano B da Cássia e negar o passado?"

    mc "Eu..."

    label sofia_final_final2_escolha1:

        pass

    menu:
        "Estou pronto. Nós vamos manter a revista.":


            mr "Excelente."
        "Eu não quero carregar esse peso. Escute ela e tome sua decisão.":


            call final_bloqueado

            jump sofia_final_final2_escolha1

    mc "O senhor está tomando uma decisão muito importante, senhor Ribeiro."

    mr "Eu sei, [mc]. E você também."

    mc "Pode ficar tranquilo. É por um bem maior. A Cássia... ela tá na mão do Grupo, senhor. Eles tão usando ela pra destruir a revista."

    mc "Eu e a Sofia, a gente vai cuidar da revista, senhor Ribeiro. Pode confiar na gente. A gente vai garantir que a Faux News não coloque as mãos sujas aqui."

    mc "Vamos manter o legado do senhor e do Escobar."

    mc "Vamos fazer jornalismo de verdade. Jornalismo ético. Jornalismo que faz a diferença."

    scene black with dissolve

    scene so6_img60 with dissolve

    mr "Eu confio em você, [mc]. Algo em você... me lembra de mim mesmo, mais jovem. E me lembra da sua mãe também. Sempre pensando no que é correto, no que é justo."

    mc "A Sofia... ela vai ser uma grande editora-chefe, senhor. Ela tem a força, a determinação, os valores..."

    mr "Eu sei que ela vai, [mc]. Eu confio nela. E em você. Torço pelo melhor, para a revista e para a Capital."

    mr "Seus milhões de habitantes merecem a verdade. Merecem uma voz ética no jornalismo."

    mc "Pode contar com a gente, senhor Ribeiro. A gente não vai decepcionar o senhor."

    mr "Suas intenções são boas. Suas e as da Sofia, mas nem sempre intenções são o suficiente, [mc]."

    mc "Mas..."

    scene black with dissolve

    scene so6_img61 with dissolve

    mr "Vocês são jovens. Pessoas como o Escobar, eu e até mesmo a Cássia, nós vimos nas prática o que as pessoas querem."

    mr "Dar o que as pessoas querem, muitas vezes, exige ir contra nós mesmos. Nos sacrificar pelos outros."

    mr "Você vir aqui hoje... me mostra que talvez você tenha a coragem de fazer o que precisa."

    mr "Mas e a Sofia? Será que ela vai ter? Ela será a editora-chefe."

    menu:
        "Eu vou tá do lado dela. Eu vou garantir que essa revista não vá à falência.":


            pass

    mr "A decisão foi tomada. Agora, só posso torcer pelo sucesso."

    mr "Não ache que sua verdade é a única, [mc]. Achar que sabe de algo é a pior fraqueza de um jornalista."

    mr "É preciso estar aberto para ouvir, pronto para agradar. Se você não conseguir se livrar da sua carga, não pode carregar a carga dos outros."

    mc "Obrigado, senhor. Vou me lembrar disso."

    mr "Boa sorte, meu garoto."

    scene black with dissolve

    pause

    scene capital_final with Dissolve(3.0)

    pause

    mc "A Sofia... ela vai precisar de mim agora. Mais do que nunca. E eu vou estar lá, com ela. A gente vai fazer isso juntos."

    scene black with dissolve

    pause

    scene so6_img63 with dissolve

    mc "Já se passaram algumas semanas desde a reunião com o Mauro. E as coisas mudaram... bastante."

    mc "O chefe se aposentou e desapareceu."

    mc "A transição foi rápida, como se o Mauro quisesse sumir com ele. Sumir com o passado."

    mc "Escobar foi aproveitar a aposentadoria, eu acho... com uma garota que ele conheceu. Não sei quem é. Mas nunca mais ele se meteu na revista."

    mc "Junto com ele, a Cássia também sumiu. Ela parecia derrotada, vazia... ela nem mesmo pegou as coisas dela da sala."

    mc "Parece que minha reunião com o Mauro funcionou. Ele não deu ouvidos a ela."

    mc "A Renata tentou se aproximar da Sofia, mas não deu certo. E ela acabou indo embora no mesmo dia da Cássia."

    mc "A Sofia assumiu de vez a revista. E ela não tá pra brincadeira."

    mc "O clima na redação é outro. Todo mundo trabalhando sério, focado. Eu nunca tinha visto esse clima tenso aqui."

    mc "Nossa nova linha editorial está à todo vapor. Sem sensacionalismo, agora com um jornalismo de verdade, combativo e investigativo."

    mc "E minha vida... bem... minha vida mudou também. Muito. Agora eu sou um chefe também, ao lado da Sofia."

    mc "Eu cresci... e minha história chegou ao fim, da melhor forma possível."

    scene black with Dissolve(3.0)

    pause

    mc "Até que..."

    scene black with dissolve

    scene so6_img62 with dissolve

    mc "Sofia, precisamos conversar."

    w "Não tá vendo que eu estou ocupada, [mc]?"

    mc "É sobre os números da revista. Eles não tão bons."

    w "Eu sei. Não preciso que você me lembre disso toda hora."

    mc "A tiragem da revista impressa caiu pela metade. O número de assinantes do site também. As pessoas não tão entendendo nosso 'jornalismo de verdade'."

    w "Elas precisam entender, [mc]. As pessoas precisam ser informadas, não entretidas. Elas precisam saber a verdade, mesmo que ela doa."

    menu:
        "Tem razão. Vamos seguir no caminho certo.":


            w "Excelente."
        "Tem certeza? Sem leitores a revista pode acabar!":


            w "Jamais. O certo sempre vence no fim."

            mc "Mas, Sofia, talvez a gente precise ir devagar. Repensar a estratégia. Seu pai e o Mauro... eles me deixaram aqui pra te ajudar. Pra..."

    w "Meu pai... ele não entende mais nada. Ele estava preso ao passado. Ao jornalismo ultrapassado. Eu preciso fazer as coisas do meu jeito."

    w "Você pode me ajudar, sim, [mc]. Mas a palavra final é minha. E eu não vou comprometer meus valores. Eu sei que isso é o que o Mauro queria. Ele me disse."

    mc "..."

    "Eu tô vendo as coisas pegando fogo, e não posso fazer nada. A Sofia, ela não escuta ninguém. Ela é teimosa, idealista..."

    "Ela acha que pode mudar o mundo sozinha. Mas ela vai se quebrar. Jogar todos nós no buraco. E eu... eu não sei como ajudar."

    w "Você está aí ainda, [mc]? Tenho trabalho a fazer. Se você não tem nada de útil para me dizer..."

    mc "Eu... eu só queria ajudar, Sofia."

    w "Então me ajude trazendo boas pautas. Pautas que mostrem a verdade. Pautas que façam a diferença. Pautas que..."

    mc "..."

    menu:
        "Acalmar ela com uma massagem":


            $ sofia_trepou = 1

            if mc_massagem > 4:

                "As massagens que eu aprendi com a Karli podem ajudar agora."

            pass

            scene black with dissolve

            scene so6_img65 with dissolve

            "Eu me aproximo dela, sem falar nada... minhas mãos pegando nos ombros tensos dela, de quem parece tá carregando o mundo."

            mc "Sofia, você tá tensa demais. Precisa relaxar. Deixa eu te ajudar..."

            w "Agora não, [mc]. Eu preciso..."

            mc "Você precisa, sim. Mas não desse tipo de ajuda. Você precisa... de mim, bem aqui, cuidando de você como uma mulher."

            "Eu sussurro no ouvido dela, com uma voz rouca, sentindo o perfume gostoso que ela tem."

            w "[mc]!"

            mc "Você sabe que quer, Sofia. A gente se deseja. Desde aquela noite na sala do seu pai, eu não consigo tirar você da cabeça."

            mc "Seu corpo... sua pele... seu cheiro... a gente quase não tem passado tempo junto. Você precisa de mim."

            w "Eu... eu não consigo pensar nisso agora... a revista..."

            mc "Esquece a revista por alguns minutos. Deixa eu cuidar de você..."

            scene black with dissolve

            scene so6_img64 with dissolve

            "Eu beijo o pescoço dela, meu toque descendo lentamente até a base de sua coluna, sentindo o tecido da roupa arrepiar com meu toque."

            w "Ah... [mc]... n-não..."

            mc "Você geme tão gostoso quando eu te toco assim... essa sua pele macia, esse seu cheiro... me deixa louco."

            w "Eu... eu não posso... não aqui..."

            mc "Ninguém vai entrar aqui, Sofia. A gente tá sozinho... e eu quero muito foder você."

            w "Mas..."

            mc "Me deixa te fazer sentir bem, Sofia. Me deixa te mostrar como eu te quero..."

            "Vou massageando, tocando, apertando, apalpando... eu sinto a respiração dela ficando mais rápida, antecipando o que eu vou fazer."

            mc "Essa sua calça atrapalhando... deixa eu tirar ela pra você..."

            w "N-não... [mc]... a gente não pode..."

            mc "A gente pode, sim. Você é a chafe, não é? Você pode o que quiser. E a gente vai. Eu quero foder você, Sofia. Aqui e agora."

            mc "Você quer, não quer? Eu sei que quer..."

            w "Eu não sei do que... aahhnn... você tá falando..."

            menu:
                "Abre as pernas pra mim, Sofia. Deixa eu cuidar de você.":


                    $ sofia_trepou = 2

                    w "Hmm... [mc]..."

                    scene black with dissolve

                    scene so6_img66 with dissolve

                    mc "Olha como você tá linda... toda molhadinha pra mim... essa sua bucetinha pulsando..."

                    w "Eu tô louca por você... doida pra sentir sua língua... me chupa, [mc]..."

                    mc "Vou chupar, amor. Vou te chupar todinha..."

                    mc "Hmmm... que delícia... você é tão gostosa, Sofia..."

                    w "Aahnn... isso... aaiinn... mais... mais forte..."

                    mc "Você gosta assim, é? Gosta que eu chupe com força? Que eu morda de leve?"

                    w "S-sim... aahnn... assim mesmo... não para... amor..."

                    mc "Eu vou te deixar louca, Sofia. Vou fazer você gozar só com a minha língua..."

                    w "Eu quero, [mc]... eu quero..."

                    "Ela já tá tremendo."

                    w "Ai, meu Deus! Eu já v-vou-"

                    mc "Goza, goza na minha boca! Me enche de mel!"

                    scene so6_img68 with vpunch

                    w "AAAAHHHHNNN!!!"

                    mc "Isso... goza pra mim, gostosa... goza..."

                    w "Aahnn... aahhhnnn... eu tô gozando... aahhh..."

                    "Sofia goza, seu corpo tremendo, se contraindo em espasmos de prazer."

                    mc "Que delícia, Sofia... você é perfeita..."
                "Encerrar a massagem":


                    mc "Tem razão, tá bom por enquanto."

                    w "S-sim... suas mãos... são muito boas."

                    mc "Gostou? Tá mais calma?"

            w "Aahnn... [mc]... eu... eu acho que eu realmente precisava disso..."

            w "Hmmm... você é tão gostoso, [mc]... tão..."

            w "Hmmm... que delícia... você é incrível, [mc]..."

            mc "Ah... aah... você... você me deixou louco, Sofia..."

            w "Eu sei. E eu vou deixar ainda mais."

            mc "Caralho, Sofia... isso foi..."

            w "Incrível... intenso... eu nunca..."

            mc "Nem eu..."

            w "A gente precisava disso, [mc]. A gente merecia."

            mc "Merecia..."

            w "Agora... agora eu me sinto... mais forte. Mais preparada."

            mc "Eu também, Sofia. Eu também."
        "Sair da sala e descobrir como salvar a revista":


            $ sofia_trepou = 0

            "Eu não posso abaixar minha cabeça pra Sofia. Eu tenho que encontrar uma forma de salvar a revista."

            "Tem que ter jeito."

    scene black with Dissolve(3.0)

    scene cidade tarde with dissolve

    pause

    scene black with dissolve

    scene trabalho geral with dissolve

    mc "Bom dia, redação..."

    "..."

    "A gente tá cada vez com menos pessoas trabalhando aqui. Tamo só com metade da equipe."

    "Mas ainda tenho fé. Sei que as pessoas vão entender uma hora."

    if sofia_trepou > 0:

        "Será que alguém aqui imagina o que aconteceu ontem?"

    "Acho que nem se eu contasse alguém acreditaria... a minha história nesta revista."

    "Agora eu sou o Coordenador de Produção... eu que mando o que todos vão fazer, organizo as equipes. Sou o pica das galáxias."

    "E eu tô adorando aproveitar meu novo cargo."

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "{i}Trr trrr{/i}"

    mc "Hm?"

    mc "Sofia?"

    w "Oi, [mc]. Tá ocupado?"

    mc "Não, não... pode falar."

    w "Vem até minha sala... preciso de uma coisa."

    mc "Já tô indo."

    w "E é algo pessoal."

    mc "Entendi."

    if sofia_trepou > 0:

        "Ela me quer de novo? Assim? No meio do trabalho?"

    "A Sofia tá realmente mudando."

    scene trabalho chefe_porta with dissolve

    "Será que ela tá querendo que eu faça aquilo de novo? Aqui?"

    "Que loucura! Mas eu não vou recusar. De jeito nenhum."

    "Bora ver o que a chefinha quer."

    play sound som_35_passos

    scene black with dissolve

    scene so6_img69 with dissolve

    mc "Oi. O que você precisa, Sofia?"

    w "Fecha a porta."

    mc "..."

    play sound som_porta

    w "Eu tô com um problema, [mc]."

    mc "Que problema?"

    w "Um problema que só você pode resolver."

    mc "Eu?"

    w "Sim... você."

    if sofia_trepou > 0:

        w "Lembra do que a gente fez ontem?"

        mc "Lembro..."

        w "Eu não consigo parar de pensar naquilo e eu quero mais."

        mc "Aqui? Agora?"

        w "Sim. Aqui e agora. Eu quero que você me lamba, [mc]. De novo."

        mc "M-mas, Sofia... a gente tá no trabalho..."
    else:


        w "Ontem eu precisava do seu toque e você me negou."

        w "Hoje você vai dar tudo o que sua chefe precisa."

        mc "M-mas..."

    w "Eu sou a chefe. Eu decido o que a gente faz aqui."

    w "Vem cá. Ajoelha em baixo da minha mesa. E me chupa enquanto eu reviso estas matérias."

    menu:
        "Sim, senhora... chefe...":


            $ sofia_trepou += 1

            mc "O-ok... tudo o que você quiser, chefinha."

            scene black with dissolve

            scene so6_img70 with dissolve

            w "Isso... bem devagar... e chefinha, não, chefe."

            mc "Assim, chefe?"

            w "Aham... agora mete essa língua igual o bom garoto que você é."

            mc "Sofia..."

            w "Vai logo, [mc]. Eu quero sentir sua língua em mim."

            mc "..."

            w "Eu tô mandando, [mc]. Obedece."

            mc "S-sim, senhora."

            "Ela tá diferente. Mais mandona. Mais... dominadora. E eu... eu não sei como eu me sinto quanto a isso."

            w "Isso... agora olha pra mim. Olha pro que você vai lamber."

            mc "..."

            w "Você quer, não quer?"

            mc "Q-quero..."

            w "Então vem. Vem e pega o que é seu."

            mc "..."

            scene black with dissolve

            scene so6_img71 with dissolve

            mc "Aahnn..."

            w "Isso... me lambe, [mc]... me lambe todinha..."

            mc "Você... você é tão gostosa, Sofia..."

            w "Eu sei que eu sou. Agora cala a boca e me chupa."

            mc "Hmmm..."

            "Eu chupo a bucetinha dela, sentindo seu gosto, seu cheiro, sua umidade."

            w "Aahnn... mais... mais forte, [mc]..."

            mc "Assim?"

            w "Isso... assim mesmo... não para... aahnn..."

            "Sofia se contorce na mesa, seu corpo tremendo de prazer."

            w "Eu vou gozar, [mc]... eu vou..."

            mc "Goza... goza pra mim, Sofia..."

            w "Aahnn... eu tô quase... mais um pouco..."

            mc "Isso... goza..."

            scene so6_img72 with vpunch

            w "AAAAHHHH!!!"

            "Ela goza, entregue, seu corpo se contorcendo em espasmos de prazer."

            mc "Que delícia de mel... sempre docinho na minha boca."

            w "De novo, [mc]... eu quero de novo..."

            mc "Agora?"

            w "Agora. Eu quero sentir você de novo. Me fode, [mc]."

            mc "Você quer?"

            w "Eu tô mandando."

            mc "Então tá bom."

            mc "Hnnngghh!"

            w "Isso... isso... me fode, [mc]... me fode com essa boca..."

            menu:
                "Tudo o que você quiser, amor.":


                    pass
                "Eu também quero te foder, linda.":


                    mc "Sofia... eu também que-"

                    w "Xiii... continua..."

            mc "Aahnn... você... você é tão gostosa, Sofia..."

            w "Eu sou sua, [mc]... faz o que você quiser comigo..."

            mc "Eu vou te foder até você não aguentar mais..."

            w "É assim que eu gosto... aahnn..."

            w "Eu vou gozar, safado... eu vou..."

            mc "Goza... goza em mim, chefe... goza..."

            scene so6_img73 with vpunch

            w "AAAAHHHH!!!"

            "Ela goza, seu corpo tremendo, o prazer explodindo dela pra minha boca."

            w "Aahhhnnn..."

            mc "..."

            w "De novo, [mc]... eu quero de novo..."

            mc "Sofia... eu... eu não sei se consigo..."

            w "Você vai fazer o que eu tô mandando. Agora."

            mc "S-sim, senhora..."

            scene black with dissolve

            "Eu... eu não sei o que tá acontecendo. Mas eu tô... gostando."

            "A Sofia... ela tá diferente. Mais dominante... mais mandona..."

            "E eu... eu tô gostando de obedecer ela. De fazer o que ela quer."

            "Será que... será que é isso que eu sempre quis?"

            "Ser dominado... ser usado... ser... o brinquedinho dela?"

    scene cidade noite with dissolve

    pause

    scene so6_img74 with dissolve

    "O tempo tá passando... e a situação da revista não melhora."

    "Estamos só com 25%% do pessoal que a gente tinha. Os investidores tão perdendo a paciência."

    "O jornalismo de verdade não tá dando certo como a Sofia tinha imaginado. Mas ela não arreda o pé, ela não para."

    "E os 'chamados' à sala dela... eles estão cada vez mais frequentes. Às vezes, duas vezes por dia."

    "E cada vez mais... intensos."

    "Eu não sei o que ela tá pensando. Não sei se ela tá só... se aproveitando de mim."

    "E eu... eu tô deixando. Eu não consigo dizer não pra ela. E, pra falar a verdade... eu nem sei se eu quero."

    w "Fecha a porta, [mc]."

    mc "..."

    play sound som_porta

    w "O que você tá fazendo parado aí?"

    mc "Eu tô pen..."

    w "Você demorou."

    mc "Eu tô tentando encontrar uma forma d-"

    w "Não me interessa. Vem aqui."

    mc "..."

    menu:
        "Você sabe que eu sempre tô aqui pra você.":




            w "Tira logo minha saia."

            mc "Sofia..."

            w "Você sabe que eu não gosto de esperar. Tira logo essa merda."

            mc "..."

            w "E vem chupar o que é seu."

            mc "..."

            w "Isso... vem, cachorrinho... vem pegar o que a dona tem pra você..."

            mc "Aahnn..."

            w "Ajoelha. Isso. Agora olha pra mim."

            "Ela abre as pernas, exibindo sua buceta molhada pra mim. Ela já tá morrendo de vontade."

            scene black with dissolve

            scene so6_img75 with dissolve

            w "Olha bem, [mc]. Olha o que eu tenho pra você. Eu fico com tesão quando você bota a cara nela assim."

            mc "Fica, é?"

            "Eu tô hipnotizado pela visão... pelo cheiro, pelo poder que emana dela."

            w "Você quer, não quer? Você quer chupar a buceta da sua dona?"

            mc "Quero... eu quero, Sofia..."

            w "Então vem. Morde ela cachorrinho."

            w "Aahnn... isso... isso... me chupa, [mc]..."

            mc "Hmmm..."

            w "Chupa essa buceta... aahnn... chupa ela todinha..."

            mc "Tô chupando, Sofia... tô chupando..."

            "Minha boca na Sofia, minha língua explorando cada dobra, cada reentrância, sugando, lambendo, mordiscando."

            w "Aahnn... mais... mais forte, [mc]... eu quero sentir sua língua em mim..."

            mc "Eu vou te deixar louca, Sofia... vou te fazer gozar..."

            w "Isso! Faz eu gozar, [mc]... mostra que você não é um inútil igual os outros... aahhnnn..."

            w "Eu tô quase, [mc]... eu tô... aahnn... adoro quando você me obedece assim. Eu sou a chefe!"

            mc "Sim, você é. Goza, Sofia... goza pra mim..."

            w "AAAHHHNNN!!!"

            scene so6_img75 with vpunch

            "Sofia goza, seu corpo incontrolável, o gozo se espalhando por ela como uma onda de calor."

            mc "Agora você pode trabalhar melhor."

            w "De novo, [mc]... eu quero de novo..."

            mc "Você não cansa?"

            w "Eu nunca vou me cansar de você, [mc]. Eu quero você sempre. Aqui. Em mim."

            mc "Sofia..."

            w "Agora fode essa porra, [mc]. Me fode forte."

            "Ela tá cada vez mais agressiva, mais exigente."

            "Como se ela quisesse me usar, me possuir, me controlar."

            "E, merda, eu tô gostando disso."





























            "Eu perdi a conta de quantas vezes a gente fez isso. E ela quer mais."

            "Eu não sei mais quem é essa mulher. Mas eu sei que eu tô... viciado."

            "Viciado no corpo dela... no prazer que ela me dá... e no poder que ela tem sobre mim."
        "Não! Chega disso! Nós temos que salvar a revista! Adeus!":


            w "Volte aqui e obedeça sua chefe!"

            mc "Não assim! Tá tudo indo pro buraco!"

            w "Você disse que ia ficar junto, pra sempre! Que ia me obedecer!"

            mc "Não! Eu quero fazer o que é melhor pra revista! Adeus!"

            w "[mc]!"

    scene black with dissolve

    scene ilha_vista_noite with dissolve

    pause

    scene black with dissolve

    scene so6_img76 with dissolve

    mc "Sofia, a gente precisa conversar. De novo."

    w "Não tá vendo que eu tô ocupada, [mc]?"

    mc "Os números, Sofia. Eles estão despencando. A revista... a revista tá quase no buraco."

    w "Você acha que eu não sei disso?! Acha que eu passo o dia inteiro brincando de ser editora-chefe?!"

    mc "Não, mas... as pessoas não estão entendendo o que a gente quer fazer. Esse jornalismo 'de verdade'... elas não querem isso."

    w "Elas vão aprender a querer. Eu não vou voltar atrás, [mc]. A gente se comprometeu com isso. Com o jornalismo justo, ético, verdadeiro."

    mc "Eu sei, mas..."

    w "Não foi pra isso que a gente fez tudo o que fez?! Quer desistir agora, seu fraco?!"

    "Ela tá na defensiva. Ela parece machucada... o que aconteceu com a Sofia?"

    w "Idiota..."

    "Será que ela... não pode ser... o que a gente fez com a Cássia? Foi isso que deixou ela assim? Ela tá se arrependendo de ter acobertado o pai?"

    "Será que ela tá começando a ver que o que a Cássia falou... talvez... talvez fosse verdade?"

    "Eu tenho que descobrir. Eu sou a única chance de salvar a revista."

    menu:
        "Sofia, e se a Cássia não estivesse mentindo? E se a gente tivesse errado?":


            pass

    scene so6_img76 with hpunch

    w "CHEGA!"

    w "Eu não quero falar sobre isso. A gente fez o que tinha que ser feito. E agora a gente vai até o fim."

    w "Mesmo que a Cássia morra de fome por nossa causa! Mesmo que ela nunca veja a filha dela! E nunca tenha justiça!"

    mc "Mas..."

    w "Agora volta pro trabalho e para de encher meu saco, [mc]."

    if sofia_trepou > 0:

        w "Melhor. Vem aqui e me chupa que é a melhor coisa que você faz."

        mc "O-o quê?!"

        w "Você ouviu. Vem aqui e chupa. Agora."

        mc "Sofia..."

        w "Eu sou a chefe. E eu tô mandando."

        mc "..."

        w "Que foi? Tá com medo?"

        mc "Não é medo..."
    else:


        w "Na verdade... você tem me recusado, dito não pra sua chefe."

        w "Acho bom você vir agora e fazer aquele carinho gostoso que eu quero. Ser um bom funcionário."

        mc "[w]... você tá descontando a frustração da revista em mim?"

        w "E se eu tiver? Eu não sou a chefe?"

        mc "Chefes não são pra agir assim..."

        w "Você quer que eu seja feliz ou não?"

        "Parece até outra mulher... ela tá tão machucada... pelo que a gente fez com a Cássia?"

        mc "Eu quero... quero que você seja feliz."

    w "Então vem. Vem cá e me satisfaz, [mc]."

    mc "..."

    menu:
        "Obedecer e chupar ela":


            w "Eu sei que você quer. Você sempre quer."

            mc "S-sim..."

            w "Então vem e pega o que é seu."

            mc "Hmmm..."

            scene black with dissolve

            scene so6_img78 with dissolve

            w "Isso... assim mesmo, [mc]... beija... me beija toda..."

            mc "Você... você gosta de mandar, né, Sofia?"

            w "Eu... adoro, [mc]... eu sou a única... hmmm... que tem capacidade."

            mc "Você quer... quer chamar a Cássia de volta? Esfregar seu poder na cara dela?"

            w "C-como?"

            mc "Pensa, Sofia... pensa no que ela pode fazer pela revista... por você."

            w "M-mas ela... hmmm..."

            mc "Ela errou, sim. Mas ela pode se redimir. E você... você pode ser magnânima, perfeita."

            mc "Você pode mostrar pra ela quem é que manda. Quem tem o poder."

            w "Eu... nnnghh... mostrar pra ela, né?"

            mc "Visualiza... pensa direitinho. Imagina ela aqui... agora... de joelhos... pedindo perdão..."

            w "Hmmm..."

            mc "Implorando pra voltar pra revista... dizendo que vai fazer tudo o que você mandar..."

            w "Ela... ela faria isso? Aquela víbora? Ahnn..."

            mc "Eu garanto que sim. E você sabe que eu tenho razão. Você sabe que, no fundo, ela te admira, Sofia."

            scene black with dissolve

            scene so6_img77 with dissolve

            w "Ela?"

            mc "Ela só não sabe perder. Mas agora... agora ela perdeu."

            w "É verdade... ela perdeu..."

            mc "E você venceu. Você mostrou pra ela que o bem sempre vence."

            w "Eu venci..."

            mc "Você é a editora-chefe agora, Sofia. Você tem o poder. É a chefe da porra toda."

            w "Eu tenho o poder..."

            mc "E você pode usar esse poder... pro que você quiser. Você pode perdoar uma fraca derrotada e salvar ela desse fim horrível."

            mc "Pensa nisso, Sofia. Pensa na Cássia e na Renata, as duas, implorando pelo seu perdão..."

            mc "Implorando para serem suas... servas."

            w "..."

            w "Imagina que é a Cássia aqui... que você tá humilhando ela... fazendo ela implorar por perdão..."

            mc "A Cássia... Você queria que ela tivesse aqui, não queria? No meu lugar?"

            w "E-eu..."

            scene ani31 with Dissolve(1.0)

            mc "Você queria esfregar na cara dela que você venceu. Que você e seu namoradinho a colocaram no lugar dela."

            w "A-ahnn... [mc]..."

            w "Tira minha calcinha, [mc]. Tira e me chupa como ela vai chupar."

            mc "Claro..."

            w "Aahnn... isso... assim mesmo..."

            mc "Hmmm..."

            w "Agora enfia essa sua língua no meio das minhas pernas, [mc]. Me chupa como a Cássia vagabunda vai fazer."

            mc "S-Sofia..."

            w "Faz o que eu tô mandando, porra! Chupa essa buceta!"

            mc "S-sim, senhora..."

            mc "Aahnn... você... você é tão molhadinha, Sofia..."

            w "Hmmm... eu tô excitada, [mc]... muito excitada..."

            w "Imagina a Cássia aqui... de joelhos... implorando pra eu não demitir ela..."

            mc "Ela... ela não tem chance contra você, Sofia..."

            w "Eu sei que não. Eu vou acabar com ela. Assim como eu tô acabando com você."

            mc "Nnghh..."

            w "Chupa mais forte, [mc]... me deixa sentir sua língua..."

            mc "Hmmm..."

            "A cada investida da minha língua eu sinto a Sofia se contorcer e gemer mais alto."

            w "Isso... isso... aahnn... mais... mais fundo..."

            mc "Você gosta, né, Sofia? Gosta de ser chupada assim?"

            scene ani32 with Dissolve(1.0)

            w "Aahnn... eu adoro, [mc]... adoro..."

            w "Imagina a Cássia aqui... no seu lugar... fazendo tudo o que eu mandar..."

            mc "Tenho certeza que ela faria. Ela precisa desse trabalho. Ela é um lixo agora."

            w "Faria sim. Se eu mandasse, ela faria. Ela faria qualquer coisa pra manter o emprego. Qualquer coisa pra sobreviver."

            w "Uhum..."

            "Eu tô conseguindo... o Mauro confiou em mim. E eu vou fazer tudo pra revista não morrer."

            w "Eu ia fazer ela lamber meu cu, [mc]. Ela ia fazer qualquer merda que eu mandasse. Porque eu venci! AHNNN!"

            mc "Aahnn..."

            "Essa maluca por poder tá me dando cada vez mais tesão."

            "Eu intensifico os movimentos, minha língua trabalhando com mais força, mais precisão, fazendo a Sofia gemer e se contorcer na mesa."

            w "Isso... isso... aahnn... mais... mais forte, [mc]..."

            w "Eu quero gozar, [mc]... quero que você me faça gozar..."

            mc "Eu vou, Sofia... eu vou..."

            w "E depois... depois eu ia mandar ela chupar minha buceta... bem aqui... na sua frente..."

            mc "Sofia..."

            w "E você... você ia ficar olhando... duro... sem poder fazer nada..."

            mc "Aahnn..."

            w "A não ser que eu mandasse você fazer alguma coisa. Você ia ter que obedecer, [mc]."

            mc "Eu sempre obedeço."

            w "Você ia ter que fazer tudo o que eu quisesse."

            mc "Hmmm..."

            scene black with dissolve

            scene so6_img79 with dissolve

            w "Você faria isso por mim, [mc]? Você faria a Cássia se humilhar desse jeito?"

            mc "Eu... eu faria, Sofia. Eu faço qualquer coisa por você."

            w "Qualquer coisa, [mc]?"

            mc "Qualquer coisa."

            w "Então... então faz ela vir aqui, [mc]. Faz ela implorar pelo emprego dela."

            w "Faz ela se ajoelhar na minha frente... e pedir desculpas... por tudo o que ela fez..."

            mc "Sofia..."

            w "Você disse que faria qualquer coisa, [mc]. Eu quero isso. Eu quero ver a Cássia humilhada. Destruída."

            w "Você vai fazer isso por mim, [mc]? Você vai me dar esse gostinho?"

            mc "Seu desejo é uma ordem."

            w "Isso! Isso... isso... me fode, [mc]... me fode com força..."

            mc "Eu vou te arrombar, Sofia... vou te foder até você não aguentar mais..."

            w "Aahnn... é assim que eu gosto, [mc]... assim que eu quero..."

            w "Eu quero que você me foda como se eu fosse a Cássia... como se eu fosse aquela vadia..."

            w "Quero... aahnn... eu quero que você me puna... que você me castigue..."

            mc "Eu vou te castigar, sua putinha... vou te foder bem forte..."

            w "Imagina ela aqui, [mc]... de joelhos... implorando pra voltar pra revista..."

            w "Eu vou fazer ela limpar o chão com a língua... vou fazer ela engraxar meus sapatos..."

            mc "Ela vai lamber suas botas... vai implorar pra você deixar ela ser sua escrava..."

            w "E-eu vou fazer ela me servir... vai trazer meu café... vai me massagear..."

            mc "Ela vai fazer tudo o que você mandar, Sofia... tudo..."

            scene ani33 with Dissolve(1.0)

            w "Tudo o que eu mandar, [mc]... tudo o que eu quiser..."

            w "E a Renata... aquela vadiazinha... eu vou acabar com ela também..."

            mc "Ela vai rastejar pra você, Sofia... vai implorar pelo seu perdão..."

            w "Eu vou fazer ela se vestir de empregada... e limpar meu banheiro... de joelhos..."

            mc "Ela vai limpar seu vaso com a língua, Sofia... e você vai rir da cara dela..."

            w "Aahnn... isso, [mc]... isso... eu vou humilhar ela... vou fazer ela pagar por ter ficado do lado da Cássia..."

            mc "Você vai, Sofia... você vai... Eu vou fazer você gozar pensando nela! NNGHHH!"

            w "Aahnn... eu vou, [mc]... eu vou..."

            mc "Então goza, porra!"

            scene ani33 with hpunch

            w "AAAAGHHH!!!"

            "Eu tô usando o ódio dela pela Cássia e pela Renata pra levar ela ao limite... pra fazer ela gozar como nunca..."

            w "AAAAHHHHNNN!!!"

            "Ela atinge o clímax, seu corpo convulsionando em espasmos de prazer, se agarrando em mim."

            w "AAAIIIIIHHHNNN!!!"

            "E ao mesmo tempo... eu tô plantando a semente na cabeça dela... a semente da reconciliação..."

            "A Cássia pode ser a chave pra salvar a revista... e eu vou fazer a Sofia perceber isso..."

            mc "Imagina, Sofia... a Cássia e a Renata... as duas... juntas... servindo você..."

            w "Aahnn... [mc]..."

            mc "Você manda nelas, Sofia... você controla elas... você faz o que quiser..."

            w "Sim... sim... eu quero... eu quero..."

            w "Caramba... isso foi demais..."

            mc "Você é sempre deliciosa..."

            w "Você também... falando esses absurdos..."

            mc "Hehe... absurdo, né?"

            w "..."
        "Negar a Sofia e tentar salvar a revista":


            mc "Sofia. A revista tá quase no buraco!"

            w "Eu sei! O que eu posso fazer?!"

            mc "Nós ainda temos uma chance. Mas você não vai gostar."

            w "Como? Eu faço qualquer coisa pra fazer a revista sobreviver."

            menu:
                "A Cásia...":


                    pass

            w "Não!"

            mc "Ela sabia o que fazer. Como atrair o público. Mas agora vai ser diferente."

            mc "Ela vai tá sob seu comando. Ela vai voltar como um cachorrinho com o rabo entre as pernas."

            w "Ela... aceitaria? Depois do que a gente fez?"

            mc "Claro. É aqui que ela pode fazer o que faz de melhor. Ela nunca vai recusar."

            w "Eu..."

            mc "E a gente ainda vai tá dando trabalho pra ela. Salvando ela."

            w "Salvar ela... depois de... sim... talvez..."

    "Eu vejo nos olhos dela... a semente foi plantada."

    "A ideia de ter a Cássia e a Renata sob seu controle... de poder humilhar as duas, dominar elas... isso a excita."

    "E ao mesmo tempo... a ideia de perdoar... de ser magnânima... isso também a atrai."

    "A Sofia tá dividida. Mas eu sei que, no fundo, ela vai fazer a escolha certa."

    "Ela vai trazer a Cássia de volta. E a revista... a revista vai sobreviver."











    scene black with dissolve

    scene so6_img80 with dissolve

    w "[mc]..."

    mc "Oi?"

    w "Desculpa por tudo."

    mc "Hm?"

    w "Eu sei que eu tô ferrando tudo. Mas é desse jeito que eu sei viver. Você me perdoa?"

    menu:
        "Claro, Sofia. Você tá lutando pelo que é certo.":


            w "Sim... mas não sei se consigo."
        "Você não tava pronta para ser editora-chefe.":


            pass

    mc "Foi pra isso que o seu pai e o Mauro me colocaram aqui. Pra garantir que, juntos, a gente consiga."

    w "Você acha que a gente consegue? As coisas... as coisas estão terríveis. Eu acabei com a revista."

    mc "Fazer o certo nunca é fácil. Mas ainda temos uma chance. É nossa última chance."

    w "A Cássia..."

    mc "Tinha uma razão pro seu pai manter ela aqui, mesmo ela tentando esfaquear ele pelas costas."

    w "..."

    scene black with dissolve

    scene so6_img73 with dissolve

    w "Então... é sério? A gente vai fazer isso? Trazer a Cássia de volta?"

    mc "Eu sei que é difícil, Sofia. Ela representa tudo o que você odeia. A mentira, a manipulação, o sensacionalismo barato..."

    w "Ela inventou aquela história pra acabar com o meu pai! Ela queria destruir a revista! E agora eu vou simplesmente..."

    mc "Eu sei, eu sei. Mas pensa bem, Sofia. Olha os números. A revista tá indo de mal a pior."

    mc "A gente precisa de algo que chame a atenção do público. E a Cássia... bem, ela sabe como fazer isso."

    w "Mas a que custo, [mc]? A gente vai se vender? Vai jogar no lixo tudo o que a gente construiu até agora?"

    mc "Não, Sofia. A gente vai continuar com o nosso jornalismo sério, investigativo."

    mc "Mas a gente também precisa ser realista. A gente precisa de leitores. A gente precisa de dinheiro."

    mc "E a Cássia... ela pode ajudar a gente com isso. Lembra da história do Nathan? Ela descobriu tudo!"

    mc "E aquela matéria sobre a Priscila, quando ela ainda estava no começo da carreira? Foi um sucesso absoluto!"

    "Mesmo complicando minha vida, a Cássia sempre foi eficiente."

    mc "Ela tem contatos, ela tem faro pra notícia... ela sabe o que vende. E tem a Zaza e a Blergh!."

    w "Eu não sei, [mc]... Eu não confio nela. Ela é perigosa."

    mc "Eu sei que é, Sofia. Mas a gente pode controlar ela. A gente pode usar o talento dela a nosso favor."

    w "Eu não queria ter que fazer isso, [mc]. Eu não queria ter que ceder."

    w "Mas... mas eu tô vendo a revista afundar... e eu não sei mais o que fazer..."

    mc "Eu sei, Sofia. Eu sei. Mas a gente vai superar isso. Juntos."

    w "Tá bom, [mc]. Eu... eu aceito. Traga a Cássia de volta. Mas com uma condição."

    mc "Qual?"

    scene ani34 with Dissolve(1.0)

    w "Eu não quero ter contato nenhum com ela. Nenhum. Você vai ser o responsável por lidar com a Cássia."

    w "Você vai receber as pautas dela, vai repassar pra mim, e depois vai entregar as minhas ordens pra ela."

    w "Eu não quero ver ela, não quero falar com ela, não quero nem respirar o mesmo ar que ela. Você cuida disso."

    mc "Tudo bem, Sofia. Eu cuido disso."

    w "E se ela tentar alguma coisa... qualquer coisa... eu quero que você me avise imediatamente."

    mc "Pode deixar."

    w "Ótimo."

    w "Então... acho que é isso."

    mc "É. Acho que sim."

    w "Vai ser estranho... ter ela de volta na revista..."

    mc "A gente se acostuma. O importante é que a revista sobreviva."

    w "Sim... o importante é que a revista sobreviva..."

    mc "..."

    w "..."

    mc "Eu... eu vou indo, então. Tenho que... ligar pra alguém."

    w "Vai lá, [mc]. E... obrigada. Por tudo."

    mc "Não precisa agradecer, Sofia. A gente tá junto nessa."

    w "Eu sei. Juntos."

    scene black with dissolve

    "Eu saio da sala dela, o coração batendo forte."

    "Passo em casa e me arrumo para falar com a Cássia. Tiro o bigode, a barba, e coloco a roupa que ela já conhece."

    scene so6_img81 with dissolve

    mc "Eu consegui. Eu convenci a Sofia."

    "E a Cássia... o que será que ela vai fazer quando souber? Será que ela vai aceitar a humilhação? Será que ela vai se submeter à Sofia?"

    "Uma coisa é certa. As coisas na revista nunca mais serão as mesmas."

    "E eu... eu estarei lá para ver tudo acontecer."

    scene black with dissolve

    pause

    scene ani35 with Dissolve(1.0)

    mc "A volta da Cássia para a revista foi... um terremoto, pra dizer o mínimo. A redação inteira ficou louca."

    mc "Alguns dos poucos jornalistas que ainda tão aqui comemoraram. Outros torceram o nariz. Ninguém ficou indiferente ao retorno dela."

    mc "E as matérias dela... ah, as matérias... Voltaram com força total. Escândalos, fofocas, revelações bombásticas... tudo o que o público adora."

    mc "E, como era de se esperar, as vendas da revista impressa voltaram a subir. As assinaturas do site também."

    mc "Sofia, no começo, ficou apreensiva. Ela odiou a ideia de ter que voltar atrás, de ter que ceder."

    mc "Mas, aos poucos, até ela teve que admitir que a Cássia, goste ou não, sabia como fazer o trabalho."

    scene black with dissolve

    scene so6_img83 with dissolve

    mc "A Cássia trouxe a Renata com ela, pra surpresa de ninguém. As duas voltaram a ser unha e carne, inseparáveis."

    mc "A Renata, agora, é tipo uma assistente da Cássia, correndo pra lá e pra cá, sempre com aquele sorriso puxa-saco no rosto. Ela também é uma sobrevivente."

    mc "Mas a Cássia... ela parece diferente. Mais cansada, mais... domada, eu diria. Como se tivesse perdido as garras."

    mc "Ela ainda faz questão de tratar todos com aquele jeito arrogante, aquele ar de superioridade, mas não é a mesma coisa."

    mc "Ela me contou, num daqueles raros momentos em que ela se abre, que foi rejeitada pelo Grupo."

    mc "Eles a culparam pelo fracasso da venda da revista. Que eles a descartaram, como se ela fosse um objeto quebrado, sem valor."

    mc "Ela disse que eu e a Sofia arruinamos a vida dela, assim como o Escobar tinha arruinado anos atrás."

    mc "E, por incrível que pareça, eu senti um pingo de compaixão por ela. Só um pingo, claro."

    mc "Mas ela precisa trabalhar, ela disse. Precisa sobreviver. E, no fundo, ela sabe que a revista é o único lugar onde ela pode fazer o que faz de melhor."

    mc "É provável que as garras dela voltem. Mas eu vou ficar de olho pra proteger a revista e a Sofia dela."

    scene black with dissolve

    scene so6_img82 with dissolve

    mc "Falando da Sofia, ela, a Cássia e a Renata nunca se encontram. Pelo menos que eu saiba. Eu sou o único que transita entre os dois mundos."

    mc "O mundo da Sofia, da verdade, da ética, do jornalismo idealista. E o mundo da Cássia, do sensacionalismo, da manipulação, do vale-tudo pela audiência."

    mc "E eu... eu tô no meio. Tentando equilibrar as coisas. Tentando fazer o que é certo... ou o que eu acho que é certo."

    mc "Eu ainda falo com o Mauro Ribeiro de vez em quando, ele me dá dicas, me ensina sobre jornalismo, e sobre como comandar pessoas."

    mc "Tem algo que me faz querer conversar mais com ele. E parece que ele também gosta de me ensinar. Talvez um dia eu me torne tão inteligente como ele."

    mc "E a revista? Bom, a revista parece estar finalmente no caminho certo. A gente não faliu, e estamos crescendo a cada mês. Quase como a gente era antes."

    scene ani36 with Dissolve(1.0)

    mc "A Sofia tá conseguindo, aos poucos, impor sua visão. Um jornalismo mais sério, mais investigativo, mas sem perder a popularidade."

    mc "O Donatello que se prepare. A gente vai chegar nele. Parece que tem algo envolvendo o aeroporto. E a gente vai descobrir."

    if sofia_namoro:

        mc "E as visitas à sala dela... hehe... elas continuam. Ainda mais frequentes, eu diria. Mas ela... ela parece diferente. Menos mandona, menos estressada."

        mc "Ela ainda é a Sofia, claro. Forte, determinada, exigente. Mas agora... agora tem um brilho diferente nos olhos dela. Ela achou uma luz."

        mc "Começou a falar até em casamento, acredita? Casamento! Eu nunca imaginei que ela fosse do tipo que pensa nessas coisas."

        mc "Ela fala em querer tirar umas férias, cuidar do casório, e me deixar no comando por uns meses. Ela precisa de um ar. Vai fazer bem pra ela."

    mc "Quem diria que a Cássia era o que a gente precisava? Parece que ignorar o passado é algo perigoso."

    mc "Não é o final que eu esperava, com certeza. É confuso, é imperfeito, é cheio de dificuldades e contradições."

    mc "Mas, como o Mauro me ensinou, o caminho certo nunca é fácil."

    mc "Mesmo assim, tão complicado, eu vejo que é um final que pode ser feliz. Com certeza. Se a gente continuar lutando pelo que acredita."

    scene black with Dissolve(3.0)

    $ persistent.sofia_final1 = True

    "{i}FIM{/i}"

    pause

    p rindo "Esse final foi feliz pra quem? Pra mim que não foi! Foi pra você?! Qual é a desse cara, hein?!"

    p "Mas esse final sem graça é apenas um dos possíveis para a história da Sofia! Se você voltar e fizer outras escolhas..."

    p "O que será que acontece se o [mc] decidir acabar com o velho Escobar? Que verdade o passado ainda guarda?!"

    p "E a Faux? O que acontece se a revista for vendida?! Cada final tem um pedaço da história que você pode descobrir."

    p lecionando "Junte todas as peças do quebra-cabeça! Descubra os outros finais! E se prepare para surpresas de outro mundo!"

    p "Você também pode ver todos os finais que você já conquistou no menu Personagens! Só clicar na fotinho dela e você terá acesso aos seus incríveis feitos!"

    p "Até a próxima, jogador! ;)"

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Parabéns! Você conquistou o Final 1 da Sofia! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    scene white with dissolve

    $ renpy.full_restart()

label sofia_final2_pre:

    scene black with dissolve

    scene so6_img49 with dissolve

    $ sofia_final2_pre = True

    w "Caramba... não acredito que é isso que eu quero. A verdade, foi o que eu sempre lutei."

    mc "Exato. A gente escolheu a verdade, mesmo que ela vá foder com tudo."

    mc "Não tem mais volta. A gente vai desmascarar seu pai, mesmo que isso signifique entregar a revista pra Faux News."

    w "A verdade... [mc]... Que merda de verdade é essa que destrói tudo?"

    w "Meu pai... vai ser o fim dele. A carreira, a reputação... tudo pro esgoto."

    w "E a Capital... nas mãos do Luca Alighieri... ele vai transformar nosso trabalho numa piada, numa ferramenta pro Grupo!"

    w "Todo o esforço, o legado do Mauro... vai virar putaria e manipulação!"

    "Ela tá no limite, a idealista vendo o mundo cuzão como ele é."

    w "Mas... a Cássia... aquela filha perdida... Se for verdade, a gente não pode só ignorar. Não pode."

    w "A gente sempre falou em fazer o certo... não dá pra amarelar agora, né?"

    scene black with dissolve

    scene sofiaf20 with dissolve

    mc "Nunca, Sofia. A gente é melhor que isso. Mesmo que o 'certo' seja um caminho cheio de merda e caco de vidro."

    "O perigo iminente, a decisão irreversível... isso tá deixando o ar pesado, carregado."

    w "Mas eu... eu tô apavorada, [mc]. Perdida. Eu não sei nem por onde começar a procurar essa verdade."

    w "Como a gente vai conseguir uma prova? A palavra da Cássia não vale NADA pra mim!"

    mc "Ei, calma."

    scene black with dissolve

    scene sofiaf22 with dissolve



    mc "Eu tô aqui contigo. Eu vou investigar, cavar essa história. Nem que eu tenha que achar essa filha dela!"

    w "E-eu... eu não sei se eu consigo..."

    "Ela me olha, os olhos grandes, assustados, vulneráveis. E é nesse momento que a máscara dela cai de vez."

    w "[mc]... eu não sei se aguento esperar. Eu tô... eu tô surtando."

    w "Eu preciso... preciso de alguma coisa agora. Antes que eu desmorone."

    mc "Sofia... o que eu posso fazer?"

    w "Preciso sentir... sentir você."

    "O pedido dela me pega de surpresa, mas a necessidade crua na voz dela mexe comigo."

    "O medo dela, o meu medo, a adrenalina... tá tudo virando um tesão bruto, desesperado."

    mc "Sofia..."

    w "Você sabe o que eu quero, o que eu preciso."

    scene black with dissolve

    scene so6_img42 with dissolve

    menu:
        "Tentar confortar o desespero da Sofia transando":


            $ sofia_final_sexo = True

            mc "Eu sei... e eu sou a pessoa certa pra te dar. Eu vou te ajudar, meu amor."

            w "Me fode, [mc]. Por favor. Me fode aqui e agora. Faz eu esquecer essa merda toda, nem que seja por um minuto."

            w "Eu tô com tanto medo! Me faz sentir alguma coisa que não seja esse pânico do caralho."

            "Meu pau já tá duro como pedra só de ouvir ela implorando assim, quebrada na minha frente."

            "Foda-se a lógica, foda-se o perigo. Ela precisa disso. E eu também... eu posso perder meu trabalho, minha razão na capital."

            "Ela precisa? NÓS precisamos disso."

            mc "Vem cá, minha lutadora..."

            scene black with dissolve

            scene so6_img41 with dissolve



            "Eu pego ela num abraço e o beijo... não é gentil, é uma colisão de bocas, línguas se procurando com fome, desespero."

            mc "Sofia... eu sempre quis ficar com você... sempre."

            w "[mc]... me pega mais, pega."

            "Ela fica ofegante, me olhando com uma mistura selvagem de medo e desejo nos olhos. A saia dela já subiu, revelando a calcinha branca e simples. Tão... Sofia."

            mc "Você pediu pra ser fodida, Sofia. Agora aguenta."

            "Subo em cima dela, minhas mãos rasgando os botões da blusa dela, expondo o sutiã rendado que eu nem sabia que ela usava. Que se foda a delicadeza."

            "Primeira vez que vamos transar... e tem que ser nessa situação de merda total."

            "E daí? Ela precisa de mim. E que tesão que isso tá me dando... foder ela sabendo que a gente tá arriscando tudo..."



            scene black with dissolve

            scene so7_img1 with dissolve

            "Arranco o sutiã dela, jogando longe. Os seios dela são perfeitos, firmes, os mamilos rosados já duros."

            "Abocanho um, chupo com força, mordo o bico de leve."

            w "AAAHNN! [mc]! Caralho... assim... que saudades de trepar!"

            play sound gemido5

            "Ela geme, vem mais perto, oferecendo mais. Minha outra mão já tá na calcinha dela, sentindo o tecido encharcado."

            "Essa ela gosta, ela precisa, essa safada. Um lado da Sofia que eu não conheço e eu quero explorar, quero ver."

            scene black with dissolve

            scene ani39 with Dissolve(1.0)

            scene so7_img2 with dissolve

            mc "Molhadinha pra mim, né, sua certinha do caralho?"

            "Enfio dois dedos por baixo do elástico, direto na buceta dela. Ela tá pulsando, quente, escorregadia. Apertada pra cacete."

            w "É culpa sua... você me deixa louca... me fode logo, porra!"

            "Tão apertada... será que ela nunca foi fodida? Ou faz muito tempo? Minha rola grossa vai caber aqui?"

            scene black with dissolve

            scene so7_img3 with dissolve



            "Tiro a calcinha dela também. A visão daquela bucetinha vermelha, inchada, brilhando de tão molhada... Puta que pariu."

            mc "Que xota linda da porra, Sofia..."

            "Afundo meu rosto ali, a língua buscando o clitóris durinho dela, tá maior, e tá pulsando. O gosto dela é intenso, a prova do desespero e do tesão."

            w "[mc]! PUTA MERDA! ASSIM! NÃO PARA! AAAIIINNN!"

            play sound gemido5

            "Chupo ela gostoso, com força, bruto, sem carinho. Uso os dedos pra abrir mais os lábios dela, minha língua fazendo círculos, subindo e descendo."

            w "Awewhnnn! Assimmmm! Devota minha buceta, amor! Eu tô tão assustada!"

            "Ela se debate no sofá, arranhando o estofado, os gemidos ficando mais altos, mais agudos."

            mc "Goza na minha boca, Sofia! Deixa eu provar seu desespero!"

            w "EU VOU! TÔ INDO! NNGHH... AAAAAHHHHHH!!!"

            scene black with dissolve

            scene so7_img4 with dissolve



            "O corpo dela treme louco, toda suada! E eu sinto o jato quente do gozo dela explodindo na minha boca."

            mc "Hmmnn... caralho."

            "Ela tem um gosto viciante... doce, salgado. O melzinho dela escorrendo pelas coxas hmmm..."

            "Mas não acabou, pô. Tá brincando?"

            "O rosto dela tá todo vermelho, suado, os olhos olhando pro nada, morta de prazer."

            "Mas a minha rola tá latejando, dura como um maldito tronco de árvore, a cabeça roxa começando a pingar porra."

            w "Ahnn... [mc]... nem sei o que tá acontecendo... hahaha..."

            play sound gemido5

            mc "Não sabe, né? Eu tenho um lance aqui pra você."

            mc "Olha pra ele, Sofia. Olha a r-ola que vai te arrombar agora."

            "Ela olha, os olhos se arregalando só de pensar... Uma arma pronta pra batalha."

            w "É... g-grande... [mc]... vai doer?"

            mc "Vai ser gostoso pra caralho. Abre as pernas."

            scene black with dissolve

            scene so7_img5 with dissolve



            "Ela obedece, afastando as coxas. Me posiciono, a cabeça do meu membro roçando na entrada dela, já lubrificada pela porra gostosa dessa delícia."

            mc "Pronta pra ter essa buceta rasgada?"

            w "Não sei se eu aguento... mas eu quero. Me fode... me fode agora, [mc]..."

            "Com uma força bruta, empurro meu pau pra dentro dela. Ela grita, um som que mistura dor aguda e prazer intenso."

            "Sinto a xota dela se esticando pra me receber, apertada pra caralho, quente, me sugando."

            mc "PUTA MERDA, SOFIA! QUE APERTADA!"

            w "Aahnn... vai devagar... tá doendo..."

            menu:
                "Devagar, é? Tá louca. Aguenta, gostosa.":


                    pass
                "Claro, meu amor. Do jeito que você gosta.":


                    pass

            w "Aahnnn... [mc]..."

            w "T-tá... gostoso..."

            scene black with dissolve

            scene ani37 with Dissolve(1.0)

            scene so7_img6 with dissolve

            "Começo a me mover, estocadas lentas e profundas, sentindo meu pau grosso grosso arrombando aquela xota apertadinha."

            "Essa filha da puta é uma delícia. Me dá tanto tesão."

            mc "Essa buceta, porra... tão gostoso te foder."

            "A cada movimento, ela geme, se acostumando com o tamanho, começando a pedir mais."

            w "Isso... aahnn... tá gostoso... o jeito que você me fode, [mc]!"

            scene black with dissolve

            scene ani38 with dissolve

            scene so7_img7 with dissolve

            mc "Quer mais, Sofia? Quer que eu te foda com mais força?"

            w "Quero! Fode essa buceta, [mc]! Soca com força!"

            "Ela que pediu. Eu meto com mais força, rápido, forte, porradas brutais naquela xoxotinha."

            "O som dos nossos corpos suados se batendo, uma foda desesperada. O sofá rangendo sob nosso peso."

            mc "Geme pra mim, porra! Geme alto!"

            scene black with dissolve

            scene so7_img8 with dissolve

            w "AAHHNN! MAIS RÁPIDO! ASSIM! RASGA MINHA XOTA!"

            play sound gemido5

            "Ela tá enlouquecendo... e esse desespero tá me dando cada vez mais vontade de marretar essa desgraçada."

            "Seguro os quadris dela, a carne macia nos meus dedos, suada, se batendo, arrombando cada vez mais fundo."

            "Ela arranha minhas costas, rebola contra meu pau, completamente entregue."

            mc "Tô quase lá, Sofia... vou gozar..."

            w "DENTRO! GOZA DENTRO, [mc]! ME ENCHE COM A SUA P-ORRA!"

            menu:
                "Foder e gozar dentro dela, mesmo com o risco de gravidez":


                    $ sofia_goza_dentro = True

                    "O pedido dela me deixa louco, leva ao limite! Tenho que gozar!"

                    "As últimas estocadas são selvagens, puro instinto. Sinto o orgasmo subindo, uma explosão quente e poderosa."

                    mc "SOFIAAA! VOU GOZAAAAR! AAAAHHHHH! CARALHOOOO!!!"

                    play sound gemido5

                    scene so7_img9 with vpunch

                    "Jorro minha porra quente dentro dela, sentindo a buceta dela se contraindo e sugando todo meu leite. Levando tudo pro útero dela."
                "Não. É perigoso demais.":


                    scene black with dissolve

                    scene so7_img10 with dissolve

                    $ sofia_goza_dentro = False

                    "Eu tiro a rola pra fora e gozo igual um louco!"

                    mc "SOFIAAA! VOU GOZAAAAR! AAAAHHHHH! CARALHOOOO!!!"

                    play sound gemido5



            mc "Aahh... caralho..."

            "Porra... é uma mistura de prazer, e de não ter nada na cabeça."

            "E eu sobre ela, esgotado, o cheiro de sexo e suor no ar."

            w "[mc]... foi incrível... aah..."

            "Ficamos ali, abraçados, ofegantes."

            mc "Esse silêncio pós-foda é diferente..."

            "A tensão foi liberada, a gente tá junto... uma aliança nascida do desespero e do prazer."
        "Resistir ao impulso. Não é hora de fraquejar":


            scene black with dissolve

            scene so6_img42 with dissolve

            $ sofia_final_sexo = False

            mc "Não agora, Sofia. A gente precisa ser forte. Mas depois... depois eu vou cuidar de você."

            w "Promete?"

            mc "Prometo. Agora, eu vou atrás da Cássia."

    scene black with dissolve

    scene so6_img53 with dissolve

    mc "Agora... a gente tá pronto."

    w "Sim... Agora eu tô. Mas... eu não sei o que fazer..."

    mc "Eu vou atrás da verdade. Descobrir o que a Cássia não contou e ver que provas que ela tem."

    w "Cássia?! Toma cuidado, [mc]. Ela é uma cobra. Ela não vai abaixar a cabeça, pelo contrário!"

    mc "Eu sei. Mas agora... eu tenho um motivo ainda maior pra não deixar ela foder com a gente."

    "A imagem da Sofia ali, vulnerável, mas com um novo fogo no olhar, fica gravada na minha mente."

    mc "Me espera. Eu volto com respostas."

    w "Eu vou esperar... conto com você."

    mc "Pode contar."

    if sofia_final_sexo:

        "Saindo da sala e o gosto dela ainda na minha boca, o cheiro dela na minha pele."

        "Nossa foda foi um pacto. Agora começa a guerra pela verdade. E eu tô pronto pra caralho."

    if banho_evento >= 20:

        jump sofia_final2_cassia
    else:


        "Eu tenho que {b}descobrir sobre a filha da Cássia{/b}."

        "Ela existe mesmo? Onde ela pode estar?"

        play sound notificacao

        scene black with dissolve

        p rindo "Fala, meu lindo!"

        p "Quer uma dica? Não? Ahh! Quanto orgulho, hein?!"

        p "Vou te dar uma dica mesmo assim porque eu que mando nessa porra!"

        p "Você vai ter que na {b}Cidade Chinesa{/b} e tomar banhos de Saúde e Beleza com a chinesa doidinha lá!"

        p "Para fazer este final, SERÁ necessário descobrir a verdade. E a verdade está lá."

        p "Só depois de finalizar tudo lá no banho, volte e {b}fale com a Cássia na redação{/b}."

        menu:
            "Terminar os banhos na Cidade Chinesa e falar com a Cássia depois, ok.":


                pass
            "Eu faço o que eu quero, maldita.":


                pass

        p "Hehe! Boa sorte!"

    jump call_cidade



label sofia_final2_cassia:



    scene black with dissolve

    scene so6_img81 with dissolve

    if sofia_final_sexo:

        "Puta que pariu... A foda com a Sofia foi... intensa pra caralho. Necessária. Mas preciso colocar a cabeça no lugar."

    "A história da Cássia... uma filha entregue pro Grupo... vendida."

    "Isso realmente é verdade? O chefe obrigou ela a fazer isso pra evitar o aborto?"

    "Como diabos eu vou confirmar uma merda dessas? O Escobar vai negar, a Cássia pode até ter inventado pra foder com ele..."

    "Preciso de algo concreto. Uma testemunha, um documento... alguma coisa que..."

    "Espera..."



    "Aquela garota do banho da Liling... a história dela sempre foi estranha pra cacete."

    show black with dissolve

    scene so7_img49 with dissolve

    ka "{i}A verdade é que eu não sou filha da Liling. Acho que dá pra perceber, né?{/i}"

    ka "{i}Eu sempre estive aqui, mas era bem diferente dela...{/i}"

    ka "{i}... ela nunca me explicou como que eu cheguei até aqui.{/i}"

    "Ela não é chinesa. Não tem traços. E vive naquele muquifo desde criança, sem saber de onde veio..."

    "E tinha aquela outra coisa que ela falou..."

    ka "{i}Daí um dia eu escutei uma conversa dela com alguém que eu não sabia quem era.{/i}"

    ka "{i}Era uma mulher ruiva. Ela brigou com a Liling por um tempão. Ela queria alguma coisa daqui.{/i}"

    ka "{i}Ela disse que queria trocar alguma coisa de volta.{/i}"

    ka "{i}EU era a coisa que a mulher ruiva queria de volta.{/i}"

    "A Kaira!!!"

    scene black with dissolve

    scene so7_img16 with dissolve

    "Uma mulher RUIVA... tentando pegar a Kaira de volta..."

    "Cássia. A Cássia é ruiva. Puta merda, não pode ser coincidência!"

    "E a Kaira disse que..."

    ka "{i}Eu fui vendida... certeza que a Liling me comprou de algum jeito.{/i}"

    "Vendida... Comprada... E a Liling? O que ela me disse mesmo sobre ter conseguido o banho?"

    li "{i}Liling segue leis de bairro. Liling ganhou banho e Kaira e faz que quer com garota!{/i}"

    mc "{i}G-ganhou?{/i}"

    li "{i}Esse é caminho que Liling escolheu lá atrás. Troquei duas coisas importantes por tudo isso aqui.{/i}"

    mc "{i}O que você trocou?{/i}"

    li "{i}Que perdi foi mais que dinheiro... Primeira delas se foi... outra seguiu caminho sem volta.{/i}"

    "Ela trocou DUAS coisas importantes... e ganhou o Banho e a Kaira."

    "Uma coisa 'se foi'... a outra 'seguiu caminho sem volta'."



    "E como a Liling ficou quando eu pressionei ela sobre essas coisas?"

    li "{i}Sério?! Que aconteceu?!{/i}"

    li "{i}Tudo isso parece errado. Eu tenho que ver que tá acontecendo. Por favor, saia de banho, vou fechar.{/i}"

    "Ela surtou! Ficou desesperada!"

    "Puta que pariu!"

    "A-HA! CARALHO!"

    menu:
        "Kaira É a filha da Cássia! A ruiva! O Grupo levou ela e deu pra Liling!":


            pass

    "A Kaira é uma sacerdotisa! O Grupo pegou ela da Cássia e deu pra Liling cuidar! É a porra do contrato!"





    "É uma teia de merda gigantesca! Tudo conectado! O Grupo, os Escolhidos, a Liling, a Kaira, a Cássia, o Escobar!"

    "Não tem prova maior que essa! Eu posso encontrar a porra da filha vendida!"

    "Isso... isso muda TUDO!"

    "Eu tenho a faca e o queijo na mão. Ou melhor, a katana e a buceta."

    "Preciso falar com a Cássia. Agora. Eu só preciso que ela confirme."

    "Melhor que confirmar! Se realmente for a filha dela, talvez eu consiga cancelar o Plano B da Cássia."

    "Se a Cássia não contar pro Mauro ou pra Faux ou não jogar a merda no ventilador, talvez tenha uma forma de NÃO vender a revista!"

    "Só que pra isso... eu vou ter que fazer a Cássia desistir do plano dela. Da vingança contra o chefe."

    "Como eu faço isso?"

    menu:
        "Vou falar com ela. Vamos ver o que ela vai falar quando eu cuspir a verdade na cara dela.":


            pass

    mc "Talvez ela muda completamente quando ver que eu descobri. Bora!"

    scene black with dissolve



    scene black with dissolve

    scene trabalho angulo with dissolve

    "É aqui. Respiro fundo. Minha cabeça tá a mil com as conexões que eu fiz."

    "Kaira... Liling... Cássia... Escobar... Tudo se encaixa de um jeito doentio."

    mc "Cássia? Sou eu, [mc]. Posso entrar?"

    "..."

    j "Entra logo, pombinho. Não me faça esperar."

    "Engulo seco e giro a maçaneta."

    scene black with dissolve

    scene so7_img11 with dissolve

    "Essa cara fechada, ainda tá puta com o resultado da reunião. O ar tá pesado."

    j "O que você quer, idiota? Me jogou aos lobos e agora veio assistir? Você é nojento."

    mc "Não é nada disos, Cássia. Eu... eu acho que descobri."

    j "Descobriu o quê, idiota? Que a vida é uma merda e os certos sempre se fodem?"

    mc "Não... Quer dizer, também. Mas sobre... sobre a sua filha."

    j "Do que caralhos você tá falando, moleque?"

    mc "Eu juntei as peças, Cássia! A Kaira, lá no banho da Liling!"

    mc "Ela não é chinesa, não sabe como foi parar lá! Uma mulher ruiva tentou pegar ela de volta anos atrás!"

    mc "E a Liling! Ela 'ganhou' o banho e a Kaira! Ela trocou duas coisas importantes! Uma 'se foi', a outra 'seguiu caminho sem volta'!"

    mc "A Kaira... a Kaira é a sua filha, Cássia! A que você deu pro Grupo pra não abortar!"

    "Caralho, eu tô sentindo a porra da adrenalina no meu corpo. Como ela vai reajir?! Ela precisa mudar!"



    scene black with dissolve

    scene so7_img12 with dissolve

    j "Hahahaha! Puta que pariu, [mc]! Você realmente superou todas as minhas expectativas de idiotice!"

    mc "Q-quê?! Como assim?!"

    j "Que porra de novela mexicana você inventou agora? Andou cheirando cola de sapateiro?"

    mc "Mas... faz sentido! Tudo se encaixa!"

    j "Faz sentido na sua cabecinha oca, pombinho! Uma mulher ruiva? Sério? A cidade tá cheia de vadias tingidas!"



    j "Você tá misturando fofoca de bairro com seus delírios! Acorda pra vida, seu merda!"

    "Porra... que balde de água fria. Ela tá negando. Rindo da minha cara."

    menu:
        "Será que eu viajei mesmo?":


            pass
        "Não... não pode ser. A conexão era muito forte.":


            pass

    j "Se não tem mais nada a dizer, então pode se retirar. Eu tenho um plano pra executar."

    scene black with dissolve

    scene so7_img14 with dissolve

    mc "Não! Cássia!"

    j "Sim, meu querido. Quando a merda explodir, a Faux vai comprar a revista, acabar com o puto do Escobar."

    j "Eu terei minha vingança e ainda sentarei na mesa dos adultos. TUDO PERFEITO! EU VENCI!"

    "Droga! Fui com muita sede ao pote. A Cássia nunca ia se rebaixar. Eu devia ter pensado."

    "Ela é orgulhosa, narcisista, e controladora demais pra admitir."

    "Tenho que mudar a tática. Não... tenho que esquecer a tática."

    mc "..."

    j "?"

    "A Cássia foi ferida por um homem. Ela... ela aprendeu a se defender pra nunca mais sofrer."

    "Tenho que fazer o contrário."

    "Vou ser verdadeiro. Honesto. Vulnerável."

    menu:
        "Eu... tenho que ser o OPOSTO do chefe.":


            pass

    mc "Ok, Cássia. Ok. Talvez eu tenha viajado. Desculpa."

    scene black with dissolve

    scene so7_img16 with dissolve

    j "Hm? Finalmente um pingo de bom senso."

    mc "Mas uma coisa não muda. O Escobar. O que ele fez com você... aquilo que você contou... aquilo eu acredito."

    "O olhar dela se estreita. Ela tá desconfiada, mas tá me ouvindo."

    j "E daí?"

    mc "E daí que ele é um filho da puta. E ele merece se foder bonito."

    mc "Eu não sei se minha teoria sobre a Kaira tá certa, talvez eu só seja um idiota mesmo. Mas isso não importa agora."



    mc "O que importa é que eu tô do seu lado nessa, Cássia. De verdade."

    mc "Eu vi o que o poder fez com ele, o que ele fez com você, o que essa merda toda tá fazendo com a Sofia. Eu cansei de ser só um peão."

    mc "Me fala a verdade. A história toda. Sem filtros. E eu vou ser seu soldado nessa guerra."

    j "Minha história?"

    mc "Me transforma no seu assistente, sua arma, o que você precisar pra finalmente fazer ele quitar a dívida contigo."

    j "Me diga o que você quer de verdade."

    mc "O que eu tô falando é... Eu te ajudo a ter sua vingança, se sua história realmente for verdadeira."

    j "Hmmm..."

    "Ela tá me analisando... avaliando. A oferta é tentadora. Ter um 'soldado' leal, ainda mais um que tem acesso à Sofia."

    scene black with dissolve

    scene so7_img17 with dissolve

    j "Você tá falando sério, pombinho? Trocando a princesinha idealista por mim, a vadia má?"

    j "O que te faz pensar que pode confiar em mim? Ou que eu confiaria em você?"

    mc "Porque nós dois queremos a mesma coisa agora. Acertar as contas. E porque você sabe que eu posso ser útil. Eu já provei isso."

    j "É... você tem seus... talentos. Mas lealdade, [mc]... lealdade exige sacrifícios."

    j "Se você quer mesmo estar do meu lado... se quer mesmo que eu te conte tudo e te use pra minha vingança... você vai ter que provar."

    mc "Provar? Como? Como eu te provo que tô do seu lado?"

    j "A Sofia."

    mc "Que que tem ela? Se vingar dela? Isso não! Ela não fez nada!"

    j "Cale a boca. Não é isso, imbecil."

    j "Ela não pode saber de nada disso. Nada sobre nosso acordo, nada sobre o que vamos fazer contra o Escobar."

    scene black with dissolve

    scene so7_img18 with dissolve

    j "Nem nada sobre... a verdade que você acha que descobriu."

    mc "Não posso contar nada pra ela? Mas... eu e ela somos uma dupla."

    j "Ela fica no escuro total. Alienada. Até eu decidir o contrário."

    j "Você vai mentir pra ela, vai esconder as coisas dela, vai ser meu espião do lado dela."

    j "Lealdade total e irrestrita a mim, pombinho. Ou nada feito."

    mc "Porra, Cássia..."

    "Aí está. O teste final. Trair a confiança da Sofia, uma mulher justa e honesta que tá disposta a ir contra o próprio pai pela verdade."

    "Que eu gosto. Prometemos enfrentar o mundo junto..."

    "Mas e se esse for realmente o único caminho pra verdade? Pra saber se o chefe foi ou não esse monstro? De evitar o Plano B e a Faux?"

    "Puta que pariu. Que escolha de merda. Mas talvez eu tenha que jogar o jogo sujo da Cássia."

    j "E então, [mc]? Vai ser meu cachorrinho fiel? Ou vai voltar correndo pra saia da Sofia?"

    "A decisão é minha. O futuro meu, da Cássia, da Sofia, da revista, do chefe e talvez de toda a Capital... depende disso."

    menu:
        "Aceito, Cássia. A Sofia não saberá de nada. Eu sou seu agora.":


            $ cassia_lealdade = True

            scene black with dissolve

            scene so7_img19 with dissolve
        "Não posso fazer isso com a Sofia. Sinto muito, Cássia.":




            $ cassia_lealdade = False

            mc "Não, Cássia. Eu não posso fazer isso com a Sofia."

            mc "Ela confia em mim. A gente tá junto nessa. Não vou mentir pra ela por você."

            scene black with dissolve

            scene so7_img16 with dissolve

            "Falei. Agora aguenta."

            scene so6_img46 with vpunch

            j "Você... o quê?! Tá me dizendo NÃO?!"

            j "Depois de tudo?! Você escolhe a princesinha chorona?!"

            j "Você é mais BURRO do que eu imaginava, pombinho! Um completo idiota!"

            mc "Pensa o que quiser, Cássia. Essa é minha decisão."

            j "Decisão errada, seu merda."

            j "Você jogou fora sua única chance. Você e sua querida Sofia."

            j "Eu vou usar meu Plano B. Vou jogar toda a sujeira do Escobar no ventilador! Vou garantir que ele e essa revista queimem no inferno!"

            "Plano B... ela vai mesmo expor tudo... eu tenho que me preparar com a Sofia."

            scene black with dissolve

            scene so7_img65 with dissolve

            j "Agora SAIA da minha frente! Some daqui antes que eu te mate!"





            play sound som_porta 

            scene black with dissolve

            show sofiaf1 with dissolve

            "Puta que pariu! Ela vai fazer! Ela vai destruir o Escobar publicamente!"

            "Se ela fizer isso, a Faux compra a revista por um centavo! Fim de jogo!"

            "A única chance... a ÚNICA... é impedir que a história vaze ou que acreditem nela!"

            "Preciso falar com a Sofia. AGORA! Convencer ela!"



            scene black with dissolve

            scene sofiaf20 with dissolve

            mc "Sofia! Rápido! Preciso falar com você!"

            w "Falar o quê, [mc]? Que você finalmente se cansou da sua nova dona e voltou rastejando?"

            "Ela tá fodidamente magoada. Droga."

            mc "Não! Eu mandei a Cássia pra puta que pariu! Disse que não ia te trair!"

            w "O quê?! Você... você fez isso mesmo?"



            mc "Fiz! Mas agora ela tá puta pra caralho! Ela disse que vai usar o 'Plano B'! Vai expor seu pai de qualquer jeito, com mentira ou não, só pra se vingar e destruir tudo!"

            w "Meu Deus! Ela vai fazer isso?! Mas então a gente tem que... contar a verdade primeiro? Tentar..."

            mc "NÃO, SOFIA! Exatamente o contrário!"

            mc "Se essa história vaza, não importa se é verdade ou mentira distorcida pela Cássia, a revista JÁ ERA! A Faux compra na hora! Seu pai é destruído!"

            "Preciso ser convincente... é a única saída..."

            mc "Pensa comigo! A Cássia não tem prova nenhuma! É só a palavra dela! Ela tá agindo por vingança!"

            mc "A gente TEM que ficar do lado do seu pai! Temos que negar tudo! Dizer que ela tá inventando, que tá louca!"

            mc "É o único jeito de proteger a revista! De impedir a Faux! De proteger o legado do seu pai... e o seu!"



            scene black with dissolve

            scene sofiaf19 with dissolve

            w "Mas, [mc]... acobertar? Negar tudo? E se... e se ela não estiver mentindo completamente?"

            w "A gente vai mesmo... fazer isso?"

            w "Você tem certeza?"





            jump sofia_final1

    scene black with dissolve

    scene so7_img19 with dissolve

    j "Excelente, pombinho. Sabia que você não era tão idiota quanto parece."

    j "Gosto de homens que sabem a hora de abaixar a cabeça... e talvez outras coisas."

    "Essa mulher... ela saboreia o controle."

    mc "O que você quer que eu faça primeiro? Como vamos derrubar o Escobar?"

    j "Paciência, meu cachorrinho fiel. Tudo a seu tempo."

    scene black with dissolve

    scene so7_img18 with dissolve

    j "Antes da vingança... vem a sobremesa."

    j "Sua primeira tarefa como meu leal servo... é um pequeno teste. Uma prova de que você realmente deixou a princesinha pra trás."

    mc "Porra... Que teste?"

    j "Simples. Além de manter essa sua boquinha fechada sobre o que a gente conversou... você vai fazer melhor."

    j "Você vai trazer a Sofia aqui."

    mc "Q-quê?! Trazer a Sofia? Pra quê?"

    j "Pra quê? Pra eu me divertir um pouco, oras."

    j "Quero olhar bem na cara dela enquanto ela admite. Quero que ela diga, na minha frente, que o papai perfeito dela é um FDP criminoso, um monstro que destrói vidas."

    j "Quero ver a máscara de santinha dela rachar. Quero ver ela engolir a própria merda de idealismo."

    mc "Cássia, isso é... cruel pra caralho. Ela já tá destruída!"

    j "Exatamente! E eu quero o golpe final. Quero ter certeza que ela sabe quem manda agora."

    j "E quero que você a traga. O amiguinho leal, o 'parceiro'. Vai ser delicioso ver a cara dela quando perceber que foi você quem a serviu pra mim numa bandeja."

    "Meu estômago... essa mulher não tem limites? Manipular a Sofia, levar ela pra ser humilhada assim... Isso é baixo até pros meus padrões recentes."

    scene black with dissolve

    scene so7_img16 with dissolve





    "Mas a verdade... a filha... a vingança contra o Escobar... Talvez seja o único jeito."

    "Ninguém mais vai me contar. O Grupo me esmagaria, Tony, Luca, obviamente nenhum deles abriria a boca sobre uma Sacerdotisa."

    mc "E... e se ela não vier? Ela me odeia cada vez mais agora. Por sua causa!"

    j "Aí é que tá a graça, pombinho. Você vai ter que usar seu 'charme'. Vai ter que manipular ela. Mentir. Fazer o que for preciso."

    j "Essa é sua prova de lealdade. Ou você faz a Sofia vir até aqui, ou nosso acordo acaba antes de começar."

    j "E você volta a ser só um paparazzo de m-erda esperando pra ser demitido."

    "A escolha tá na minha cara. O caminho 'fácil' e sujo com a Cássia, ou o caminho 'certo' e provavelmente suicida com a Sofia."

    "Eu já escolhi acreditar na Cássia... agora tenho que ir até o fim. Ou não?"

    menu:
        "Eu faço. Vou trazer a Sofia até aqui.":


            $ mc_manipula_sofia = True

            mc "Ok, Cássia. Eu... eu faço. Vou trazer a Sofia."

            j "Bom garoto. Sabia que podia contar com sua... falta de escrúpulos."

            j "Agora vai. E não demore. Estou ansiosa pelo show."
        "Não. Eu não vou fazer isso com ela. Nosso acordo acaba aqui.":


            $ mc_manipula_sofia = False

            mc "Não, Cássia. Eu não posso. Existe um limite pra mim. Humilhar a Sofia desse jeito... isso eu não faço."

            "Falei. Que se foda. Não vou ser o capacho sádico dela nesse nível."



            scene black with dissolve

            scene so7_img11 with dissolve

            j "Que pena, pombinho. Achei que você tinha mais estômago pra fazer o que é preciso."

            j "Achei que você queria poder de verdade."

            mc "Eu quero, mas não assim. Não passando por cima de tudo e de todos dessa forma."

            "Talvez eu seja um idiota mesmo... mas não consigo."

            j "Então nosso acordo está desfeito, obviamente."

            j "Você fez sua escolha. Preferiu a moralidade barata à oportunidade."

            j "Saia da minha sala agora. Sua presença me irrita."

            j "E pode rezar, [mc]. Reza pra eu não te destruir junto com o Escobar e a sua amada princesinha quando eu soltar minha bomba."

            "A bomba... o Plano B... ela vai usar de qualquer jeito agora. Fodeu."



            mc "..."



            play sound som_porta

            scene black with dissolve

            scene sofiaf1 with dissolve

            "Caralho! Quebrei o acordo! Ela vai me foder!"

            "E pior: ela vai expor o Escobar de qualquer maneira! O Plano B vem aí!"

            "Se ela fizer isso, adeus revista, adeus Escobar, adeus Sofia... adeus meu emprego!"

            "Não tem mais jeito de usar a verdade a nosso favor... não sem a Cássia pra controlar a narrativa."

            "A única saída... a única MÍSERA chance... é negar. Abafar. Proteger o velho."

            "Tenho que falar com a Sofia IMEDIATAMENTE. Convencer ela que a gente precisa mentir, acobertar tudo. É a única forma de talvez... talvez... sobreviver a isso."



            scene black with dissolve

            scene sofiaf24 with dissolve

            mc "Sofia! Urgente! Preciso falar com você!"

            w "O que foi agora, [mc]? Conseguiu 'resolver' seu assunto com a Cássia?"



            mc "Resolvi até demais! Eu rompi com ela! Mandei ela enfiar o acordo no..."

            mc "Enfim! O problema é que agora ela ficou puta e vai usar o Plano B de qualquer jeito! Vai expor seu pai pra mídia!"

            w "O QUÊ?! Mas... então a gente tem que agir! Contar nossa versão antes!"

            mc "NÃO, SOFIA! Esse é o ponto! Se essa história explodir, não importa a versão, a Faux News ganha! A revista acaba!"

            mc "A única chance que a gente tem é negar! Fingir que a Cássia tá louca, que tá inventando tudo por vingança!"

            mc "A gente precisa proteger seu pai! Proteger a revista! É o único jeito!"

            "Convence ela, [mc]... convence ela..."



            scene black with dissolve

            scene so5_img10 with dissolve

            w "Proteger meu pai? Acobertar tudo? Mas, [mc]... e se a Cássia..."

            w "A gente vai mesmo fazer isso? Você tem certeza?"





            jump sofia_final1

    mc "Calma... Me dá um tempo, caralho."

    "Agora vem a parte mais fodida... encontrar Sofia e mentir na cara dura dela."

    "..."

    scene black with dissolve

    show so7_img75 with dissolve

    mc "Sofia?"

    w "[mc]! Você... falou com ela? Terminou sua reuniãozinha?"

    mc "Falei."

    w "E aí? O que ela disse? Ela tem provas? O que toda essa lealdade descobriu?"

    "Puta que pariu, como eu vou fazer isso?"

    mc "Sofia, é complicado. Ela... ela tá disposta a conversar. A contar o que sabe."

    w "Sério?! Isso é ótimo! Quando? Onde?"

    mc "Aqui. Agora. Na sala dela."

    w "Na sala dela? Com ela? [mc], eu não posso... Depois de tudo o que ela disse, tudo o que ela fez..."

    mc "Eu sei, Sofia, eu sei que é difícil pra caralho. Mas pensa comigo. A Cássia tá acuada agora. A gente venceu a batalha da venda, ela sabe que o Escobar tá na merda."

    mc "Talvez... talvez ela esteja disposta a cooperar agora pra se salvar, pra conseguir algum acordo."

    mc "Digo, é a nossa chance de arrancar a verdade dela antes que ela mude de ideia e a Faux descubra tudo."

    scene black with dissolve

    scene so5_img10 with dissolve

    w "Mas... ir até lá? Sozinha com ela?"

    mc "Não sozinha. Eu vou com você. Do seu lado, o tempo todo."

    mc "A gente precisa mostrar pra ela que não temos medo. Que estamos juntos nisso. Que queremos a verdade tanto quanto ela quer vingança."

    w "Não sei, [mc]... Não tenho medo dela, mas não sei se quero ver ela agora. O jeito que ela olha, o que ela fala..."

    mc "Eu sei. Mas a gente precisa ser forte agora, Sofia. Pela verdade. Pelo jornalismo que a gente acredita. Pelo... pelo fim dessa merda toda."

    mc "Vamos só ouvir o que ela tem a dizer. Se for mentira, a gente sai de lá e foda-se. Mas se ela tiver algo... a gente precisa saber."

    "A confiança dela em mim tá lutando contra o medo e a repulsa que ela sente pela Cássia."

    w "Você... você vai ficar comigo o tempo todo? Não vai me deixar sozinha com ela?"

    mc "Eu juro, Sofia. Do seu lado. O tempo todo."

    w "..."

    w "Tá bom, [mc]. Tá bom. Eu... eu vou. Mas se ela tentar qualquer gracinha..."

    mc "Eu cuido disso. Vamos."

    scene black with dissolve

    mc "Cássia? Trouxe ela."

    scene black with dissolve

    scene so7_img22 with dissolve

    "Cássia tá com um sorriso que faria o diabo sentir inveja."

    j "Ora, ora... a princesinha resolveu honrar minha humilde sala com sua presença."

    w "Cássia... O [mc] disse que você... que você quer conversar. Contar a verdade."

    j "Verdade? Que palavra engraçada na sua boca, Sofia. Mas sim, podemos conversar. Senta aí."

    "Quero ser um apoio pra ela, mas tô me sentindo o maior Judas da história."

    j "Então... você quer saber sobre seu papai herói, não é? O grande Editor-Chefe Escobar?"

    w "Eu quero... eu quero saber o que aconteceu. O que ele fez... com você."

    j "O que ele fez comigo? Ele me usou, querida. Me usou e me jogou fora como um pedaço de lixo. Achou que podia me calar com um cargo e um salário gordo."

    j "Achou que eu ia esquecer o que ele me obrigou a fazer. O que ele me tirou."

    w "A... a filha... é verdade?"

    j "Você acredita, Sofia? Você acredita que seu paizinho perfeito, o pilar da ética jornalística?"

    j "Que esse babaca é, na verdade, um monstro FDP que engravidou uma estagiária e mandou ela se livrar do 'problema'?"

    "Sofia não responde. Apenas abaixa a cabeça, os ombros tremendo levemente."

    j "Eu quero ouvir, Sofia! Admite! Admite que seu pai é um canalha! Admite que toda essa sua pose de certinha é uma farsa construída em cima da merda que ele fez!"

    w "..."

    j "FALA, PORRA!"

    scene black with dissolve

    scene so7_img23 with dissolve

    w "E-ele... ele... ele pode ter... errado..."

    j "ERRADO?! ERRADO É ROUBAR UM DOCE NA PADARIA, SUA MIMADA DO CARALHO! O QUE ELE FEZ FOI CRIME! FOI MONSTRUOSO!"

    "Sofia se encolhe na cadeira. Tento dar um passo à frente, mas o olhar da Cássia me congela no lugar."

    j "Fica quieto, cachorrinho. O show é dela."

    j "Então, Sofia? Vai continuar defendendo ele? Vai continuar se escondendo atrás da imagem falsa que você criou?"

    w "Não... Não vou defender... o que não tem defesa."

    w "Se... se o que você diz é verdade... então... meu pai é..."

    "Ela não consegue terminar a frase. A admissão, mesmo que incompleta tá aí, pesada, dolorosa."

    "Ela não brigou. Ela não gritou. Ela... aceitou? Que p-orra tá acontecendo com a Sofia?"

    "Esse olhar... não é só tristeza. Tem algo mais... uma quebra? Uma... curiosidade?"

    w "Você queria me humilhar, Cássia? É isso? Ok, você me humilhou."

    j "Finalmente. Demorou, mas a princesinha caiu do cavalo."

    w "Hmm..."

    j "Agora sim... agora podemos começar a conversar de verdade."

    scene black with dissolve

    scene so7_img24 with dissolve

    w "Eu não quero conversar..."

    j "Você vai fazer o que eu mandar."

    w "..."

    w "Tá bom... o que você quiser, Cássia."

    "Q-quê?!"

    j "Hahaha! Não pensei que eu fosse gostar TANTO de ver a chefinha toda submissa!"

    w "..."

    mc "Sofia... você tá bem?"

    "Ela se vira pra mim, e eu não consigo dizer o que ela tá pensando, mas tá tremendo a garota."

    w "Me deixa em paz, [mc]. Posso ir pra minha mesa, Cássia?"

    w "Eu preciso... ficar sozinha."

    mc "Mas, Sofia-"

    w "Quieto!"

    scene black with dissolve

    scene so7_img25 with dissolve

    j "Ouviu a patroa, pombinho. Deixa a princesinha lamber as feridas. Pode ir, minha bonequinha."

    w "O-obrigada... até mais."

    "Eu não quero deixar ela assim. Mas o olhar dela... ela sai, fechando a porta atrás de mim, deixando Sofia sozinha com seus demônios."

    "Puta merda... O que eu fiz?"

    "A humilhação funcionou. Sofia admitiu... quase. E Cássia conseguiu o que queria."

    "Mas o olhar da Sofia... Aquilo não foi normal. O que tá passando na cabeça dela agora?"

    "E agora... eu sou oficialmente o cachorrinho da Cássia."



    scene black with dissolve

    scene so7_img13 with dissolve

    j "Parece que a princesinha finalmente entendeu quem manda na porra toda."

    j "E você, pombinho... você fez um bom trabalho. Trouxe o cordeirinho pro abate direitinho."

    mc "Eu... eu fiz o que você mandou, Cássia."

    "Ainda sinto o gosto amargo da traição, só que ver ela assim, vitoriosa, dona da situação..."

    j "Fez sim."

    "Não sei porque, mas ver a Cássia vendendo desperta algo sombrio em mim. Uma admiração torta."

    j "Ver você assim... dividido... obediente... me dá um tesão do caralho, sabia?"

    mc "C-como é?"

    "Ela passa os dedos lentamente pelo meu peito, descendo até minha virilha."

    "Meu corpo reage, meu pau começando a dar sinal de vida dentro da calça."

    j "Parece que você finalmente encontrou o seu lugar, [mc]. De joelhos... metafórica e talvez literalmente."

    mc "N-não sei do que você tá falando."

    j "E sabe o que mais? Isso me deixa... molhada."

    scene black with dissolve

    scene so7_img26 with dissolve

    "O olhar dela é predatório. Ela não tá brincando. Ela me quer. Agora."

    "Mas é como um troféu. Como uma forma de selar minha submissão."

    mc "Cássia... a gente... a gente tá no trabalho. Qualquer um pode ver."

    j "E quem se importa, porra? Eu sou a chefe agora, esqueceu? Eu fodo quem eu quiser, onde eu quiser."

    "A mão dela aperta meu caralho, que já tá grosso. A mão dela, mesmo sendo mulher, é forte e tem um aperto possessivo."

    j "E eu quero foder você. Quero sentir essa sua rola grossa me rasgando, enquanto eu te lembro quem manda."

    "Meu sangue ferve. A humilhação da Sofia, a tensão, o poder cru da Cássia... é uma mistura de medo e desejo."

    j "E então, meu cachorrinho? Vai me dar o que eu quero? Ou vai tentar latir um 'não'?"

    menu:
        "Eu também tô com um tesão do c-aralho por você, Cássia. Me usa.":


            $ mc_transa_cassia_pos_humilhacao = True

            mc "Como eu poderia recusar... chefe?"

            mc "Tô duro pra caralho só de pensar em você mandando em mim."

            scene black with dissolve

            scene so7_img18 with dissolve

            j "Bom garoto. Tira a roupa. Devagar. Quero ver cada pedaço seu."

            "Obedeço, minhas mãos tremendo um pouco enquanto desabotoo a camisa, a calça. A cada peça que cai, o olhar dela me devora."

            j "Nada mal, pombinho. Podia ser maior, mais grosso, meio curvado pra cima, do jeito que eu gosto pra sentir lá no fundo. Igual do Ronaldo."

            scene black with dissolve

            scene so7_img27 with dissolve

            mc "Você vai mesmo falar isso?"

            j "Eu falo o que eu quero. O que importa é se ele é meu."

            mc "Ele é todo seu, Cássia."

            j "Eu sei. Agora... deita na minha mesa."

            mc "Na... na mesa?"

            j "Algum problema? Ou prefere o chão, como eu vou botar sua amiguinha Sofia?"

            mc "N-não... a mesa tá ótima."

            "Deito na mesa fria, completamente nu, exposto sob o olhar dela."

            scene black with dissolve

            scene so7_img28 with dissolve

            "Ela se aproxima, também se despindo, revelando o corpo escultural. Seus seios perfeitos, obviamente silicone, mas quem se importa?"

            "E a cintura fina, uma buceta toda esculpida na cirurgia. É quase uma bimbo."

            j "Olha bem pra essa perfeição, [mc]. Dinheiro compra muita coisa... inclusive a melhor foda da sua vida."

            "Ela monta em cima de mim, sentando no meu quadril, roçando a buceta quente e úmida no meu abdômen antes de se posicionar na minha piroca dura."

            j "Agora... sente como é ser possuído pela chefe."

            "Ela desce devagar, engolindo minha rola grossa inteira. É apertada, firme, mas molhada pra caralho."

            scene black with dissolve

            scene so7_img29 with dissolve

            mc "Puta merda, Cássia... você é... aahnn..."

            j "Eu sei. Agora cala a boca e sente. Sente minha buceta perfeita e apertadinha, toda cheia de suco."

            mc "Aahnn... é mesmo, que xota perfeita!"

            "Ela começa a cavalgar, devagar no início, depois aumentando o ritmo. O controle dela é absoluto."

            "Ela dita a velocidade, a profundidade, o ângulo. Eu sou só a pica que ela tá usando pra se satisfazer."

            scene black with dissolve

            scene ani41 with Dissolve(1.0)

            scene so7_img32 with dissolve

            j "Assim... hmmm... mais fundo... sente minha xota apertando sua rola grossa, seu merda!"

            play sound gemido5

            "Ela joga a cabeça pra trás, os seios balançando. A visão é hipnotizante. Eu agarro a cintura dela, tentando acompanhar o ritmo frenético."

            mc "Você vai me fazer gozar rápido assim, porra..."

            j "Não antes de mim, cachorrinho."

            "A buceta dela aperta meu pau, com fome. As paredes dela, esfregando, pra cima e pra baixo, apertando, apertando, apertando, me sugando!"

            mc "PORRA!!!"

            j "Gosta de ser minha cadeira de pica, [mc]? Gosta de sentir minha xota te engolindo enquanto você nem pode fazer nada?"

            "Ela me provoca, enquanto acelera, as estocadas ficando mais fortes, mais brutais. A mesa treme."

            "Não sei se sou eu que tô comendo... não... é ela que tá me comendo com a buceta faminta dela."

            mc "Caralho..."

            j "Vai, pombinho! Soca! Ah, não! Eu que soco minha xota nesse pau minúsculo! Ahhnn!"

            play sound gemido5

            scene black with dissolve

            scene ani40 with Dissolve(1.0)

            scene so7_img30 with dissolve

            "Ela reclama, mas ela geme. Essa vadia."

            j "Fode sua dona, seu cachorro! Seu puto! Vadio! Aahnnn!"

            j "Eu tô quase lá... sente como eu aperto sua rola grossa? Tá sentindo minha xotinha te espremendo?"

            "O cheiro de sexo, de suor, a mesa rangendo, ela me fodendo com força, e minha rola crescendo, mais dura."

            mc "S-sim... Cássia... tá... bom pra c-caralho..."

            j "Eu sei que tá! Agora geme pra mim! Geme como a putinha que você é!"

            "As estocadas dela são impiedosas agora. Ela tá perto."

            j "VOU GOZAR EM VOCÊ, SEU MERDA! AAHHHNN!"

            play sound gemido5

            scene black with dissolve

            scene so7_img31 with dissolve

            "O corpo dela se contrai sobre o meu, sinto o espasmo do orgasmo dela, a b-uceta apertando meu pau violentamente."

            "Ela grita, um som primitivo de puro prazer e poder."

            j "Eu tô quase... AAHNN... que delícia de pau... me fode, [mc]! Me fode!"

            "Ela tá perdendo o controle, e o barulho. Todo mundo deve tá ouvindo. Sofia? Não... tomara que não!"

            j "VOU GOZAR! NNGHH!"

            "A buceta operada dela me espremendo, me devorando, com força. A porra desse corpo tremendo."

            j "AAAHHNNNGGHHH!!!"

            play sound gemido5

            mc "Isso... goza... me dá todo esse mel..."

            j "Ah... puta que pariu... cala boca, idiota..."

            mc "Cássia... eu... eu também tô..."

            scene black with dissolve

            scene so7_img36 with dissolve

            j "Eu sei. Mas ainda não. Vira."

            mc "Virar?"

            j "De quatro, cachorrinho. Na mesa. Agora."

            menu:
                "Ficar de quatro e obedecer o que ela mandar":


                    "Dá aquele medo, mas o comando na voz dela é irrecusável. Viro, ficando de quatro sobre a mesa dela, meu rabo empinado."

                    j "Isso... bem submisso... Hora de você aprender uma lição sobre quem realmente manda aqui."

                    scene black with dissolve

                    scene so7_img33 with dissolve

                    mc "C-Cássia... o que você vai...?"

                    j "Shhh... relaxa e aproveita. Ou não. Ou talvez você goste de ser meu brinquedinho anal?"

                    mc "N-não... Cássia... aí não..."

                    j "Medinho, putinha? Você não disse que era meu? Que faria tudo? Relaxa... ou não. Talvez você goste da dorzinha."

                    "O dedo dela entra, uma invasão chocante, desconhecida."

                    mc "Aahgnnn..."

                    j "Xxiii... me dá sua rola também."

                    "O dedo dela no meu rabo, mas a mão dela no meu pau... Rápido, forte, apertando a cabeça, deslizando pelo corpo grosso sem dó."

                    "A sensação é uma loucura. A delícia da punheta dela na minha rola, e o dedo dela no meu toba."

                    mc "P-porra!"

                    scene black with dissolve

                    scene so7_img34 with dissolve

                    j "Gostando da massagem dupla, [mc]? Sentindo seu rabinho ser cuidado enquanto eu espremo a porra pra fora dessa rola?"

                    "A voz dela é baixa, rouca, cheia de malícia."

                    mc "P-para... não... continua! Aahhh! C-caralho!"

                    "Eu tô perdido. Não sei o que eu quero. Só sei que tô prestes a explodir."

                    j "Geme pra mim, desgraçado! Implora pra gozar no meu dedo!"

                    "Ela aumenta a pressão no dedo, girando levemente, enquanto a punheta fica mais forte, ela vai arrancar minha rola, filha da puta!"

                    mc "VOU GOZAR! CÁSSIA! POR FAVOR! AAAHH!"

                    j "Goza, porra! Goza pro meu dedo no seu cu!"

                    "Não aguento mais. O mundo explode em branco. Goz-o com uma força absurda, jorrando minha p-orra quente por toda a mesa dela, sujando os papéis, o tampo de vidro."

                    "Meu corpo inteiro convulsiona, a sensação no cu ainda ecoando."

                    mc "AAAAARRRGGGHHHH!!!"

                    "Caio na mesa, tremendo, ofegante, humilhado, esvaziado... e estranhamente... satisfeito de um jeito doentio."
                "Cássia... t-tá bom... eu tô satisfeito.":


                    j "Se você quer assim, foda-se. Eu já gozei mesmo."

            j "Bom garoto. Fez uma bela sujeira na minha mesa. Limpa."

            "Ela não tá nem aí pra mim."

            j "Se veste. A brincadeira acabou. Por agora."

            show black with dissolve

            "Ainda ofegante, limpo a bagunça na mesa dela sob seu olhar divertido e superior."

            "Visto minhas roupas, sentindo cada músculo doer. Aquilo foi... intenso pra caralho."

            "Ela me usou, me dominou, e uma parte doentia de mim adorou."
        "Não, Cássia. Não agora. Primeiro as respostas.":


            $ mc_transa_cassia_pos_humilhacao = False

            mc "Não. Eu não sou seu brinquedinho, Cássia. Eu aceitei ser seu aliado pra derrubar o Escobar, pra descobrir a verdade. Não pra ser seu objeto sexual."

            "Cássia me encara, surpresa pela recusa. Um brilho perigoso surge em seus olhos."

            scene black with dissolve

            scene so7_img12 with dissolve

            j "Ousado, pombinho. Muito ousado."

            j "Recusando sua dona? Depois de tudo o que eu te ofereci?"

            mc "Eu quero a verdade, Cássia. E a vingança. O sexo... fica pra depois. Ou talvez nunca."

            j "..."

            j "Tudo bem, [mc]. Se é assim que você quer. Você fez sua escolha. Lealdade, mas sem os... benefícios."

            j "Vamos direto aos negócios então. Mas não pense que eu esqueci essa sua... insubordinação."

    mc "E agora, Cássia? A verdade. Você prometeu."

    scene black with dissolve

    scene so7_img12 with dissolve


    j "Sim, sim... a verdade."

    mc "E aí?"

    j "Você acertou na mosca."

    mc "Acertei?!"

    j "Sua teoria... sobre a Kaira ser minha filha... e sobre ela estar no banho daquela chinesa."

    j "É tudo verdade."

    mc "Puta que pariu... Kaira é sua filha... então era tudo verdade."

    j "Desde o início. O Grupo me tirou ela quando nasceu. Foi a 'garantia' deles, a coleira que o Escobar ajudou a colocar em mim depois de me chutar grávida."

    j "Eles me prometeram uma 'vida especial' pra ela... e a jogaram naquele banho chinês de m-erda com a Liling, sabe-se lá em troca do quê!"

    "A raiva na voz dela é genuína, fria, direcionada ao Grupo e ao Escobar."

    mc "A Liling... ela recebeu a Kaira deles?"

    j "Pelo que eu descobri fuçando onde não devia, sim. O Grupo tem seus tentáculos naquela espelunca também."

    j "A Liling deve ter feito um pacto com o diabo pra conseguir aquele banho e ficar de boca fechada."

    mc "Caralho, Cássia... Que história fodida."

    j "Bem-vindo ao clube, pombinho. Agora você entende por que o Escobar tem que queimar no inferno?"

    mc "Sim."

    menu:
        "Sim, mas nós vamos recuperar a Kaira. E não só se vingar.":


            pass

    j "Como é?"

    mc "Confia em mim. Vamos pra Cidade Chinesa."

    j "Pombinho..."









    "Chegamos ao Banho de Saúde e Beleza. Porra... que nervoso, mano."

    j "Qual seu plano, idiota? Acha que ela vai desistir da escrava assim? Acha que eu não tentei?"

    "Cássia tá do meu lado, não dá pra saber o que ela tá pensando, mas sinto a tensão emanando dela."

    "Ela tá prestes a confrontar a mulher que criou, que manteve cativa... sua filha por anos."

    mc "Deixa comigo."

    "Pode parecer que eu tenho tudo sob controle, mas não sei ainda como tirar a Kaira daqui."

    scene black with dissolve

    scene so7_img37 with dissolve



    li "Senhor [mc]? Veio para banho? Liling não esperava..."

    "Liling aparece na entrada, o sorriso profissional quase congelando ao ver Cássia."

    li "Você? Que mulher ruiva faz aqui em banho de Liling?!"

    j "Vim buscar o que é meu, velha."

    "A voz da Cássia é puro gelo cortante."

    mc "C-calma..."

    li "Aqui não tem nada seu! Liling não deve nada pra gente como você! Xô! Xô!"

    "Ela faz um gesto para nos expulsar, tipo espantando maus espíritos."

    mc "Liling, calma. A gente sabe de tudo."

    mc "Sabemos da Kaira. Sabemos que ela é filha da Cássia. E que você ganhou ela do Grupo."

    li "Mentira! Mentira de homem branco! Kaira é de Liling! Liling cuida dela!"

    j "Cuidar? Ou usar, como usaram minha filha e como usam você?"

    li "Não sabe de nada! Sai daqui!"

    mc "A gente sabe do acordo, Liling. O acordo com os Escolhidos, com o Grupo. Sabemos que você 'ganhou' a Kaira."

    mc "Mas a gente precisa saber o que você deu em troca."

    li "Q-quê? Senhor [mc] não sabe que diz."

    menu:
        "Eu sei Liling. Não precisa mais esconder.":


            pass
        "Então me fala. Me explica.":


            pass

    mc "Eu tô do seu lado, Liling. Seu, da Kaira... e do que você perdeu."

    li "!!!"



    mc "Fale, Liling... O que você sacrificou pra ter isso aqui?"

    li "Sacrifício? Liling sacrificou TUDO! TUDO!!!"

    li "Você pergunta o que Liling perdeu?"

    scene black with dissolve

    scene so7_img38 with dissolve

    li "Liling perdeu MARIDO! Liling perdeu FILHA!"

    mc "Filha?! Você... você tinha uma filha?"

    li "Minha única f-ilha... meu sangue... Pequena flor de lótus..."

    "Flor-de-Lótus? Espera. Onde eu ouvi isso antes?"

    li "Marido não aceitou acordo... Escolhidos... silenciaram ele."

    li "Eles precisavam de menina... menina especial... para ser He Xiangu."

    mc "He Xiangu?! Eu sabia! Flor-de-Lótus! A He Xiangu é tua filha?!"

    li "Minha filha... Eles levaram minha filha... fizeram ela acreditar que era imortal... que era deusa..."

    j "Cretinos..."

    li "Trocaram minha filha... por banho... e por... por Kaira."

    mc "Puta que pariu... Você... você deixou eles levarem sua filha?! Pra virar aquela... aquela farsa?!"

    "Como ela pôde aceitar isso?! Ela fez isso pore scolha?!"

    mc "Como você teve coragem, Liling?! Trocar sua própria filha por... por um negócio?!"

    scene black with dissolve

    scene so7_img43 with dissolve

    li "Coragem?! Homem branco não entende! Cidade Chinesa tem regras! Escolhidos mandam! Grupo manda!"

    li "Se Liling não obedece... Liling morre! Família de Liling na China morre! Minha filha ia morrer de qualquer jeito!"

    mc "Mas você sabe o que aconteceu com a He Xiangu?! Ela virou uma, sei lá, uma fanática!"

    li "Pelo menos assim... ela vive... mesmo que... mesmo que não seja mais minha filha..."



    mc "Ma-"

    j "Chega, [mc]."

    mc "Cássia! Você não que-"

    j "Você não entende a porra do buraco em que essa gente vive. Você é só um pombinho que não sabe PORRA alguma!"

    li "Mulher ruiva sabe. Filha dela..."

    j "Eles tiram tudo de você, não é, Liling? Esses filhos da puta. Nos forçam a fazer escolhas impossíveis. E depois nos deixam com as migalhas e a culpa."

    scene black with dissolve

    scene so7_img39 with dissolve

    li "Mulher ruiva... entende..."

    j "Eu entendo pra caralho. Agora escuta aqui, velha. Você quer sua filha de volta? A sua de verdade?"

    li "Minha... minha flor de lótus?"

    j "Nós vamos quebrar essa farsa. E o pombinho aqui vai dar um jeito, não vai, pombinho?"

    mc "Q-quê?! Bom... eu conheço a He Xiangu, e ela tá... bom... pronta pra saber a verdade."

    mc "Talvez eu possa falar tudo pra ela."

    j "Vamos desfazer o acordo que fizeram com NOSSAS FILHAS sem nem que pudéssemos falar algo."

    j "Eu quero retomar a porra da minha vida, e da minha filha. Mesmo que eu tenha que matar alguns poderosos."

    li "..."

    mc "Você precisa libertar a Kaira, Liling. Deixar ela ir. Deixar ela conhecer a mãe dela. Viver onde é a casa dela."

    li "Libertar Kaira... se minha filha voltar?"

    li "Se acordo quebrar... se flor de lótus voltar... Kaira livre? Desfazemos acordo de Sacerdotisas."

    scene black with dissolve

    scene so7_img40 with dissolve

    j "É a única condição. Sua filha pela minha. O acordo original, desfeito."

    li "..."

    "Caralho... ela vai aceitar?"

    li "Liling... Liling aceita."

    li "Traz minha filha de volta. Traz minha flor de lótus. E Kaira é sua."

    j "Você ouviu, pombinho. Você me trouxe até aqui, e eu fiz o principal. Coloquei a velha na roda."

    j "Agora vai e traz a filha de volta. Mostra que você realmente tem alguma utilidade."

    "Falar com a He Xiangu... e explicar tudo isso pra ela."

    "Talvez eu consiga... se ela não me cortar em dois."

    if xiangu_namoro:

        "Ela deve tá lá em casa... me esperando."

        scene black with dissolve

        scene xiang_casa1 with Dissolve(1.0)

        mc "Xiangu!"

        i "[mc]?"

        mc "Ela não tá hoje?"

        i "Ela deve tá no templo. Ela vai pra lá às vezes, né?"

        mc "Verdade... nem sempre ela tá aqui."

        i "É difícil esquecer o passado às vezes."

        mc "É... vou lá falar com ela."

        i "Cuidado pra ela não cortar sua cabeça. Vai que o passado volta com tudo."

        mc "Que isso, Xiang, vira essa boca pra lá."

        scene black with dissolve

        mc "{i}Gulp{/i}"

        jump sofia_final2_xiangu
    else:


        "Ela deve tá lá no portal."

        scene black with dissolve

        "Espero que ela não corte minha cabeça."

        mc "{i}Gulp{/i}"

        jump sofia_final2_xiangu







label sofia_final2_xiangu:

    scene black with dissolve

    scene c_chinesa ofuro_entrada with dissolve

    pause

    scene black with dissolve

    scene sayuri9_xiangu5 with dissolve

    mc "He Xiangu... ou melhor... eu não sei como te chamar agora."

    xu "Pode continuar me chamando como sempre. A [xu] ainda existe aqui. Eu ainda sou a deusa."

    mc "Sei..."

    xu "O que o [mc] deseja? Veio trazer notícias da Cidade Chinesa?"

    mc "Não. Eu vim falar sobre... você. Sobre a sua verdadeira história."

    xu "Minha história é conhecida por todos. A [xu] é uma dos Oito Imortais..."

    mc "Não. Essa não é a sua história. Essa é a história que te contaram. Que te forçaram a acreditar."

    mc "Você mesma admitiu que tinha dúvidas..."

    xu "Dúvidas são naturais... mesmo para... para alguém como eu. Uma deusa. Estamos sempre evoluindo."

    "Ela ainda tá lutando contra a verdade... mas ela vai entender a verdade quando ver de quem ela nasceu."

    scene black with dissolve

    scene xiangu_mc_sentados with dissolve

    mc "Eu conversei com a Liling. A dona do banho. Você conhece ela?"

    xu "A senhora Liling? Sim. O que ela tem a ver com isso?"

    xu "Ela é uma devota. Sempre respeitou a [xu]."

    mc "Ela respeita a lenda, sim. Mas ela... ela sabe a verdade. E ela me contou."

    xu "Que verdade o [mc] insiste em trazer? Sobre que é essa tal verdade?"



    mc "A verdade sobre sua mãe."

    xu "Minha mãe? A [xu] não tem mãe há milhares de anos. Sou nascida da essência divina, tocada pelos deuses..."

    mc "Não. Você teve uma mãe e ela tá viva. Uma mulher de carne e osso. Que te carregou na barriga, que te deu à luz."

    mc "Uma mãe que foi forçada a te entregar. Que sofreu muito com isso. E que ainda tem saudades da sua flor de lótus."

    xu "Do que você está falando?! Isso é blasfêmia!"



    mc "Sua mãe... é ela... a Liling!"



    scene black with dissolve

    scene sayuri9_xiangu4 with dissolve

    xu "Liling?! Minha... mãe?! Impossível! Ela... ela sempre me tratou com reverência... como uma serva!"

    mc "Porque foi isso que mandaram ela fazer! Os Escolhidos! O Grupo!"

    mc "Eles te tiraram dela quando você era bebê! Te colocaram aqui, nesse papel de He Xiangu, pra manter a farsa deles funcionando, pra controlar o bairro!"

    xu "Não... não pode ser... Liling... ela nunca..."

    mc "Eles a obrigaram, He Xiangu! Ameaçaram a família dela na China! Ela perdeu o marido por causa disso, seu pai! E perdeu você!"

    mc "E sabe o que eles deram pra ela em troca? Em troca de tirarem a única filha dela?"

    xu "..."

    scene black with dissolve

    scene sayuri9_xiangu6 with dissolve

    "Ela tá absorvendo o choque... a mente dela deve tá a milhão."

    mc "Deram o banho. E deram outra criança pra ela criar. Uma moeda de troca viva. A Kaira."

    xu "Kaira... a garota do banho... então ela..."

    xu "Liling... trocou... a mim?"

    "A voz dela falha. A realização começa a doer."

    mc "Ela foi forçada. Ela não queria. Ela sofre até hoje. A Mestra, que você tanto defendeu, é a culpada."

    mc "Sabe como ela te chama quando pensa em você? Quando fala de você?"

    xu "..."

    mc "'Minha Flor de Lótus'. Foi assim que ela te chamou."



    scene black with dissolve

    scene sayuri9_xiangu2 with dissolve

    xu "Flor... de Lótus?"

    "Ela faz uma cara de tristeza, como se sentisse uma dor física. As lágrimas começam a aparecer."

    xu "Como pode? Então... tudo... minha vida inteira foi... uma mentira? Isso dói, [mc]."

    mc "Uma mentira criada por eles. Pelos Escolhidos. Você é tão vítima quanto a Liling, quanto a Kaira."

    "Caralho... ver a ficha dela caindo assim... é foda..."

    xu "Eu não... eu não sou He Xiangu... a imortal."

    xu "Eu sou... só... a f-ilha da Liling?"

    mc "Você pode ser a He Xiangu. Ser quem você escolher ser a partir de agora. Mas você não precisa mais carregar o peso dessa farsa."

    xu "Mas... meu dever... o portal... a Cidade Chinesa..."



    mc "A Cidade Chinesa vai encontrar um novo camanho. Um caminho sem mentiras. E você pode ajudar, se quiser."

    mc "E você... você pode finalmente ser livre. Conhecer sua mãe de verdade. Descobrir quem você é."

    scene black with dissolve

    scene sayuri9_xiangu4 with dissolve

    xu "Livre... conhecer minha mãe..."



    mc "Liling quer você de volta. Ela só precisa que você vá até ela."

    mc "E ela prometeu... se você voltar, ela liberta a Kaira."

    xu "Libertar... "

    xu "Então... minha volta... pode salvar outra pessoa?"

    mc "Exatamente. Pode quebrar o ciclo. Desfazer o acordo que o Grupo fez para essas duas mães e para duas filhas."

    xu "..."

    "Ela olha para as próprias mãos, talvez para a espada, como se visse tudo com novos olhos."

    scene black with dissolve

    scene so7_img55 with dissolve

    xu "Eu preciso... Isso é... demais."

    mc "Eu sei. Mas a verdade tá aí. E sua mãe tá esperando."

    xu "Você tem razão... eu não posso mais viver essa mentira."

    mc "Sério?"

    xu "Sim. Eu sabia que tinha algo estranho. Desde sempre. Desde que eu vi a Xiang."

    xu "Eu senti algo por ela... por você. Coisas que não são... divinas."

    mc "Hehe..."

    mc "Então vamos ver sua mãe?"

    xu "Sim. Vamos acabar com isso. Me leve até ela, [mc]. Me leve até... minha mãe."

    scene black with dissolve

    "He Xiangu... você PRECISA perdoar sua mãe. Ou a Kaira nunca vai voltar e a revista e eu... tô fodido."



    scene black with dissolve

    scene c_chinesa ofuro_entrada with dissolve

    pause





    li "..."

    li "Chegaram."





    scene black with dissolve

    scene so7_img56 with dissolve

    xu "..."

    mc "Liling..."



    li "Minha flor... Minha flor de lótus..."

    li "Você... voltou..."

    "A voz dela tá tão fraca, nem parece aquela Liling..."

    xu "Voltei? Ou me trouxeram?"

    xu "Você me entregou, Liling. Você me trocou... por este lugar! Pela Kaira!"

    "Droga! Droga! Não era isso que era pra acontecer!"



    li "Não! Não foi assim!"

    li "Liling não queria! Nunca quis!"

    xu "Então por quê?! Por que me deixou viver essa mentira?! Por que me abandonou?!"

    li "Eles obrigaram, minha flor! Os Escolhidos! A Mestra Jidao!"

    xu "A Mestra? Vai dizer que a culpa é dela agora? Pelas SUAS ações?!"

    mc "Xiangu!"



    scene black with dissolve

    scene so7_img57 with dissolve

    li "Seu pai... ele não aceitou... eles... eles mataram ele!"

    xu "!!!"

    li "Ameaçaram nossa família... todos que Liling amava..."

    li "Eles precisavam... precisavam de uma He Xiangu pra manter controle... pra manter poder..."

    xu "A Mestra? Ela... matou meu pai?"

    li "Ela me tirou você! Me forçou a entregar você pra farsa deles! Pra virar deusa falsa!"

    li "Eles deram Kaira... deram banho... mas levaram você! Levaram minha vida!"

    li "Liling não teve escolha, minha flor! Perdoa Liling! Perdoa!"



    "Caralho, que peso... ouvir a história assim, da boca dela... Jidao... sua vaca."



    xu "Então... não foi você..."

    xu "Foi ela... a Mestra Jidao... ela fez isso tudo?"

    xu "Ela matou meu pai? Ela me transformou... nisso?"

    menu:
        "Foi ela, sim.":


            pass

    mc "Ela e o sistema podre dos Escolhidos, criado pelos Oito Imortais. Vocês duas foram vítimas dela."

    scene black with dissolve

    scene so7_img58 with dissolve



    xu "Mãe..."

    "A palavra sai quase como um sussurro."

    xu "Me perdoa... por ter... te culpado e por ter desaparecido por tanto tempo."



    li "Liling que pede perdão, minha flor... por não ter sido forte... por não ter protegido você..."





    scene black with dissolve

    scene so7_img59 with dissolve

    pause 2.0





    xu "Então eu não sou mesmo He Xiangu... a deusa imortal. Eu sou uma garota, como qualquer uma."

    mc "Como qualquer uma aí já é demais. O jeito que você usa essa espada aí, credo."

    xu "Verdade. Isso não significa que eu não possa fazer a diferença."

    li "Minha filha..."

    xu "A Cidade Chinesa precisa se libertar dessa mentira. Precisa encontrar um caminho novo, sem a Mestra, sem os Escolhidos manipulando tudo."

    xu "Eu não tenho poderes divinos... mas eu tenho força. Eu aprendi a lutar. Eu posso ajudar."

    xu "Posso ajudar como... como humana."

    mc "É isso aí! Esse é o espírito, ou melhor, essa é a garota!"

    scene black with dissolve

    scene so7_img60 with dissolve

    li "Minha filha... tão forte... mesmo depois de tudo..."



    xu "Obrigada, [mc]. Por me mostrar a verdade. Por me trazer de volta."

    mc "Não foi nada. Eu também tinha meus interesses. Agora vocês duas têm muito o que conversar."

    mc "E, Liling... acho que você tem outra promessa pra cumprir, né?"

    li "Sim... Kaira..."

    li "Liling vai falar com ela. Vai... tentar explicar."

    li "Obrigada, senhor [mc]. Obrigada por trazer minha flor de volta."

    scene black with dissolve

    scene so7_img55 with dissolve



    xu "Senhor [mc]."

    mc "Sim?"



    xu "Antes de você ir... posso falar algo?"

    mc "Claro. O que foi?"

    xu "Sobre a Xiang."

    xu "Aquela garota... ela é diferente, [mc]."

    mc "Diferente como? Ela é forte pra caralho, isso eu sei."

    xu "Mais que isso. O jeito dela... os olhos... a força que vem de dentro..."

    xu "Eu vivi uma mentira por anos, fingindo ser algo que não era. Mas a Xiang... tem algo nela que não parece deste mundo."

    mc "Você acha que... a lenda... talvez a Xiang seja? De verdade?!"



    scene black with dissolve

    scene so7_img61 with dissolve

    xu "Eu não sei. Talvez não uma deusa imortal como a lenda diz. Mas especial? Sim. Muito especial."

    xu "Ela passou por coisas que ninguém imagina... naquela sala branca que ela falou."

    xu "E mesmo assim... ela tem essa luz. Essa força."

    mc "Eu também sinto isso nela. É como se tudo fosse... uma brincadeira?"

    xu "Então cuide dela, [mc]. Por favor. Ela parece confiar muito em você."

    xu "O mundo lá fora... pode ser cruel com alguém como ela. Proteja essa luz."

    mc "Pode deixar, Xiangu. Eu prometo. Vou cuidar dela."



    scene black with dissolve

    scene so7_img45 with dissolve

    xu "Obrigada."

    "Ela me olha de um jeito diferente agora. Um olhar mais direto, mais... humano."

    xu "E obrigada por... por tudo. Você sabe..."

    mc "N-não foi nada. Eu curti muito. E fico feliz que você esteja livre agora."

    xu "Livre..."

    "Um pequeno sorriso surge nos lábios dela."

    xu "Sim. Livre pra fazer... isso."





    scene so7_img62 with hpunch

    pause

    scene black with dissolve

    scene so7_img64 with dissolve


    mc "O-o quê?! Xiangu! O que foi isso?"

    xu "Isso?"

    "Ela ri, um som leve e genuíno que eu nunca tinha ouvido antes."

    xu "Isso é o que garotas normais fazem quando querem, [mc]."



    xu "Agora que eu não sou mais uma 'deusa'... acho que posso ter desejos, não posso?"

    xu "E posso roubar um beijo se eu quiser."

    mc "Mas..."

    xu "Zaijian, [mc]."

    "Ela pisca pra mim e se vira, caminhando com leveza em direção ao interior do Banho, talvez para encontrar Liling."

    scene black with dissolve

    scene so7_img63 with dissolve

    mc "..."



    "Ha... garota normal... ela aprendeu rápido como ser uma safadinha."

    "Ver ela assim, livre, se permitindo... caralho, dá um orgulho fodido."

    "E pensar que eu tive uma parte nisso... nada mal pra um paparazzo de merda."

    scene black with dissolve

    scene so7_img45 with dissolve

    "Será que eu ainda vou ver ela um dia? Agora que ela não é mais... uma deusa?"

    ka "Que isso?!"

    mc "HM?!"



    li "Pronto, senhor [mc]. Aqui está Kaira."

    mc "O-opa. Liling, o que você tá fazendo?!"

    scene black with dissolve

    scene so7_img47 with dissolve

    li "Parte de Liling no acordo tá feita. Leva garota logo pra mãe dela."

    ka "Assim? Do nada? Só me joga pra fora como se eu fosse lixo?"

    "Opa, parece que a 'escrava' criou afeto pela 'dona'? Ou só tá puta mesmo?"

    li "Lixo não! Garota forte! Vai logo pra sua mãe! Xô! Xô!"

    "Caramba, até o 'xô xô' tradicional voltou com tudo"

    li "Liling tem muito trabalho agora. Precisa limpar banho. Vai, vai!"



    mc "..."

    ka "..."

    "Que silêncio constrangedor... no nível de encontrar a sogra na fila do sex shop."

    mc "E aí, Kaira? Pronta pra conhecer a famosa 'mulher ruiva'?"



    ka "Pronta? [mc], você tá maluco?"



    scene black with dissolve

    scene so7_img48 with dissolve

    ka "Eu passei a vida inteira sem saber quem era minha mãe! Achei que tinha morrido, que tinha me abandonado de propósito!"

    ka "Agora, do nada, você aparece, fala que ela tá viva, que ela me quer, e eu tenho que ir lá conhecer ela? Assim?!"

    mc "Bom... resumindo bem, é mais ou menos isso."

    "Diplomacia nunca foi meu forte."

    ka "E se ela me odiar? E se ela me achar horrível? E se ela se arrependeu de ter me procurado?"

    ka "E se ela for... sei lá... um monstro?"



    "Monstro? Filha, se você soubesse QUEM é sua mãe... Cássia Roitman faz o Godzilla parecer um poodle assustado."

    mc "Relaxa, garota. Pior que a Liling gritando 'Vai trabalhar, Kaira!' no seu ouvido não deve ser."

    mc "E pensa bem, você aguentou cliente tarado, aguentou a Liling, aguentou essa vida de m-erda aqui. Você é forte pra caralho. Vai tirar isso de letra."

    ka "Ser forte pra mandar um velho babão se foder é uma coisa, [mc]. Encarar a mãe biológica que aparentemente me vendeu é... um pouquinho diferente."

    "Justo. Ponto pra ruivinha. Lidar com tarado parece ser mesmo mais fácil que lidar com seu interior."

    mc "Olha, Kaira... não vou mentir pra você. Sua mãe... ela não é flor que se cheire. Ela é... intensa. Complicada pra caralho."

    mc "Mas ela revirou céus e terra pra te achar. Ela enfrentou a Liling, tá disposta a peitar o Grupo... ela te quer de volta. Isso eu senti que é verdade."

    "Pelo menos a parte de querer a Kaira de volta... a parte de ser boazinha, já é outra história."

    ka "Intensa... complicada..."

    menu:
        "E você tem uma irmã te esperando também.":


            pass

    ka "S-sério?"

    mc "Acabei de pensar nisso. Se a história for verdade, então a Sofia é sua meia-irmã."

    ka "Perfeito... cada segundo que passa fica mais fácil."

    scene black with dissolve

    scene so7_img50 with dissolve

    mc "Hahaha... a decisão é sua. Sua mãe e talvez sua irmã estão te esperando."

    "Vamos, Kaira... vamos salvar sua mãe da desgraça que ela virou."

    ka "Não. Eu vou seguir meu caminho sozinha. Sem minha mãe ou qualquer outra família."

    "PORRA!!!"

    mc "T-tá falando sério?!"



    ka "Não. Foda-se. Eu vou ver minha mãe."

    mc "Ufa... Não me mata do coração, FDP."

    ka "Preciso saber por quê. Preciso olhar na cara dela. Preciso entender essa merda toda."

    "Aí sim! Essa é a Kaira! Direto ao ponto, sem frescura."

    mc "É assim que se fala! Bora encarar a fera."

    mc "Eu vou estar lá contigo. Qualquer coisa, eu te protejo."

    mc "Ou, sei lá, uso você de escudo humano e saio correndo. A gente improvisa."

    ka "Idiota."

    ka "Vamos logo com isso, antes que eu perca a coragem."

    mc "Bora. Próxima parada... Reuniões Anônimas de Mães Complicadas."

    "Ou só a sala da Cássia mesmo."

    ka "[mc]... idiota... olha pra mim."

    mc "Ops. Vamos comprar uma roupa pra você antes."

    ka "Paspalho."

    "Tal mãe, tal filha."








    scene black with dissolve

    scene trabalho geral with dissolve

    mc "Chegamos."

    scene black with dissolve

    scene so7_img51 with dissolve

    ka "N-não! Não quero ver ela!"

    mc "Vem, Kaira! Tá tão perto!"

    ka "Quero voltar!"

    mc "Mas a gente chegou! O covil da fera é logo ali."

    ka "Não ajuda muito falar assim, sabia? Tipo, chamar minha mãe de fera."

    mc "Foi mal. Força do hábito. Agora veeemmm!"

    ka "Caramba... ela deve ser terrível."

    mc "Hahaha... é só brincadeira, calma. Não precisa correr!"

    "Ela tá tensa pra caralho. Também... de todas as mamães, justo a Cássia? Não é pra qualquer um."

    "E o pai ainda é o chefe... dá pra acreditar? Essa garota tá perdida. Ela vai voltar pra Liling..."



    scene black with dissolve

    scene so7_img52 with dissolve

    w "[mc]? Onde você estava? E... quem é essa?"



    "Essa? É sua irmã. Nada de mais. Imagina?"



    mc "Sofia! Oi! É... agora não dá pra falar. Eu tô com pressa."

    "Merda, merda, merda! Justo agora?"

    w "Pressa pra quê? Aconteceu alguma coisa? E por que você tá com essa garota?"

    ka "..."

    mc "É um assunto... particular. Com a Cássia."

    "Queria tanto contar pra Sofia! Mostrar que eu consegui achar a filha da Cássia! Que elas são irmãs!"

    "Mas não posso... ordem da 'dona'... Que merda de papel eu fui me meter!"

    w "Com a Cássia?! Desde quando você tem assuntos particulares e urgentes com a Cássia? E quem é ela?"

    "Pronto. Acionei o modo 'Ciúmes & Controle' da chefinha. Ótimo."

    ka "..."

    mc "É complicado, Sofia. Longa história. Depois eu te explico tudo, prometo. Agora eu realmente preciso ir."

    w "..."

    "Ela claramente não gostou de ser deixada de fora."

    "Vai dar merda depois. Anotado."



    scene black with dissolve

    scene so7_img53 with dissolve

    mc "É aqui. Respira fundo, Kaira. V-vamos entrar."

    ka "Como se fosse fácil..."

    w "..."

    "{i}TOC TOC{/i}"

    mc "Cássia. Trouxe alguém."

    j "!!!"

    j "Ela?"

    mc "É."

    j "Entra!"

    mc "Boa sorte..."

    ka "Vou precisar."

    scene black with dissolve

    scene so7_img66 with dissolve

    "Puta que pariu, são parecidas mesmo. O cabelo vermelho fogo... os olhos... Cássia versão pocket e menos psicopata."

    "Imagina as duas juntas daqui uns anos? Ou numa briga? Ou... não, foco, [mc], foco!"

    j "Então... você veio."

    ka "Você... é a mulher ruiva."

    ka "Você é... minha mãe?"

    "A palavra 'mãe' sai engasgada, cheia de dúvida e dor."

    j "Eu sou Cássia Roitman."



    j "E você... é a Kaira."

    ka "Por quê?"

    "Eita, porra. Ela foi direta pro que importa."



    scene black with dissolve

    scene so7_img67 with dissolve

    j "As coisas... não são simples, garota. A vida me obrigou a fazer escolhas difíceis."

    ka "Escolhas? Ou você só se livrou de mim?"

    "Porra! Vai dar merda!"

    j "..."

    "Cássia parece sentir o golpe, mas só isso não vai derrubar essa mulher."

    j "Acho que temos muito o que conversar."

    j "A sós."



    mc "A-ah, claro. Eu... vou deixar vocês."

    "Fui dispensado. Hora do cachorrinho sair de fininho."

    j "Saia, [mc]. E feche a porta."

    mc "T-tá legal. Kaira..."

    ka "Pode deixar."

    mc "Ok."

    "Não tem como. Ela é filha da Cássia e ponto. Sem tirar nem por. E elas vão se matar, escreve o que eu tô dizendo."



    play sound som_porta 

    scene trabalho geral with dissolve

    "E agora? Vão se matar lá dentro? Ou vão chorar e se abraçar?"

    "Com a Cássia envolvida, a chance de sangue é maior que a de lágrimas, eu acho."

    "Bom, minha parte tá feita. Trouxe a cria de volta pra mamãe diaba. Agora é esperar o resultado... e torcer pra não sobrar pra mim."

    "A Cássia reencontrou a filha. Talvez ela consiga colocar isso acima da vingança."

    "Talvez ela mude e esqueça o Grupo. Ela é ambiciosa, isso nunca vai mudar, mas talvez ela siga uma ambição diferente, longe de quem pegou a filha dela."



    scene black with dissolve

    scene so7_img53 with dissolve

    "Que porra será que tá rolando lá dentro? Não dá pra ouvir nada com essa porta maldita!"

    "Vão se matar? Vão fazer as pazes? Vão começar uma seita bizarra de ruivas?"

    "Preciso chegar mais perto... só uma espiadinha... ou uma ouvidinha..."



    mc "Só um pouquinho... eu tô quase ouvindo."

    "O que é isso? A Kaira tá chorando? Ou a Cássia tá ameaçando ela? Mais um pouco... mais..."



    scene trabalho geral with hpunch

    scene black with dissolve

    scene so7_img54 with dissolve

    w "[mc]! O que você pensa que está fazendo com a orelha colada na porta da Cássia?!"

    "FODEU! Pego no flagra! Merda, merda, merda!"

    mc "S-Sofia! Que susto, caralho! Eu... eu não tava ouvindo nada! Eu só tava..."

    mc "...admirando a madeira da porta? Vendo se precisava de verniz?"

    "Isso não é hora de fazer piada, idiota! Ainda mais com uma desculpa nível político pego com dinheiro na cueca."

    w "Admirando a porta? Você acha que eu nasci ontem, [mc]? Eu vi você! Tava aí bisbilhotando!"

    w "Primeiro some com aquela garota ruiva estranha, depois diz que tem 'assunto urgente' com a Cássia, e agora tá espionando?! O que tá acontecendo?!"

    mc "Não é nada disso que você tá pensando, Sofia! É complicado!"

    "Queria tanto poder contar pra ela... falar 'Olha, achei a filha perdida da Cássia, aquela que teu pai FDP fez ela vender pro Grupo!'"

    "'Aliás, ela é sua irmã também, filha do chefe. Legal, né?'"

    "Mas não posso!"

    scene black with dissolve

    scene so7_img73 with dissolve

    w "Complicado?! Complica pra mim, [mc]! Você some, esconde as coisas, fica de segredinho com a mulher que mais odeio e quer destruir nossa revista!"

    w "Como você quer que eu confie em você desse jeito?!"

    w "Eu pensei que... a gente tinha decidido fazer isso JUNTOS."

    "Ai... Ela tá magoada pra cacete... e isso dói pra caralho."

    mc "S-sofia..."

    w "QUÊ?!"

    "Ela também fica gata pra porra quando tá brava assim... o que eu falo pra gente não virar inimigos pra sempre?!"

    mc "Sofia, eu juro que não tô te traindo! Eu tô tentando... resolver as coisas. Coisas importantes pra revista!"

    "Mentira... Ou talvez não? Afinal, se a Cássia conseguir a vingança dela sem explodir tudo, pode ser bom pra revista? Ah, foda-se, nem eu sei mais."

    w "Resolver coisas com a CÁSSIA?! A troco de quê?! O que ela te prometeu?! Um cargo melhor quando a Faux News comprar tudo?! É isso?!"

    if sofia_namoro:

        w "Ou ela te prometeu... outra coisa? Você tá me traindo com ela, [mc]? É isso?!"

        mc "N-não! Você é minha namorada! Não é nada disso!"

        w "Será que você gosta das que mandam em você, [mc]? É isso? Gosta de ser dominado?"

        mc "N-não, senhora."

        "Espera..."

    scene black with dissolve

    scene so7_img74 with dissolve

    mc "Não! Claro que não, Sofia! Para de paranoia! Eu nunca faria isso com você!"

    w "Então me conta! Me conta o que tá acontecendo! Me diz quem era aquela garota! Me diz por que você tá agindo assim!"



    mc "Eu... eu não posso, Sofia. Ainda não."

    "Droga, droga, droga! Odeio ser o cachorrinho dela!"



    j "[mc]!!! VOLTA AQUI!"

    mc "Q-quê?!"

    w "..."



    w "Ela te chamou. Sua dona."

    w "E agora, [mc]? Vai ficar aqui e me explicar essa m-erda toda como um homem..."

    w "Ou vai correr pra lamber as botas dela como o cachorrinho que você virou?"



    menu:
        "Eu preciso ir, Sofia. Desculpa. A gente conversa depois.":


            pass

    mc "Sofia... me perdoa... eu preciso ir agora. É... é importante pra redação. Eu te explico depois, eu juro!"

    "A maior mentira da minha vida. E a mais dolorosa. Adeus, confiança da Sofia..."

    scene so7_img54 with vpunch

    w "Mentiroso! Traidor!"



    w "Não precisa explicar mais nada, [mc]. Eu já entendi tudo."





    scene black with dissolve

    scene so7_img68 with dissolve

    mc "Cássia... eu..."

    "Fechei a porta na cara dela... literalmente. Acabou. Fodi com tudo. Sou um merda."

    j "Finalmente, a bela adormecida resolveu aparecer."

    "Essa vadia ainda tira sarro..."

    mc "O que você quer, Cássia?"

    j "Então, o cachorrinho voltou pra dona. Fez um bom trabalho lá fora afastando a mosca morta."

    "Ela tá saboreando cada segundo da minha humilhação..."

    mc "Eu fiz o que você mandou, Cássia."

    j "Eu sei que fez. Mas agora me diga, pombinho... por quê?"

    j "Por que tanto esforço? Enfrentou a Liling, me trouxe a... garota... largou a Sofia aos prantos lá fora."

    j "O que você realmente quer com tudo isso, [mc]? O que você espera ganhar?"

    mc "Eu..."

    "Hora da performance... convencer a diaba que eu sou um FDP ambicioso igual ela."

    scene black with dissolve

    scene so7_img70 with dissolve

    mc "Eu quero o que todo mundo quer nessa cidade de merda, Cássia... poder. Um lugar melhor."

    mc "Cansei de ser o paparazzo fudido que corre atrás de migalha. Eu vi o Escobar, vi você, vi como as coisas funcionam."

    mc "E eu vi a verdade no que você disse sobre ele. O cara é um monstro por baixo daquela pose de chefe durão. Ele merece pagar pelo que fez com você."

    j "Hmmm... interessante. Continua."

    "Ela tá comprando... ou fingindo que tá?"

    mc "E quando você falou da sua filha... eu vi a dor ali. Ninguém merece ter um filho arrancado desse jeito. Isso mexeu comigo."

    "Ok, essa parte foi quase verdade. A história é fodida mesmo."

    ka "..."

    j "Ambição e um pingo de... compaixão distorcida? Uma mistura perigosa, pombinho. Mas que me agrada."

    j "Fico feliz que você tenha finalmente escolhido um lado. O lado vencedor."

    j "Porque agora... agora o Escobar vai pro inferno."

    mc "Como assim?"

    "Aí vem..."

    j "Meu Plano B, querido. A cartada final."

    j "Vou pegar toda a merda do passado dele, a história da nossa... filha... o jeito que ele me tratou, tudo!"

    j "E vou jogar na cara da mídia! Dos acionistas! Do Mauro Ribeiro!"

    j "A reputação dele vai virar pó! A Faux News vai comprar essa revista por um saco de laranjas podres depois do escândalo!"

    j "E eu vou assistir de camarote ele ser destruído!"



    scene black with dissolve

    scene so7_img69 with dissolve

    mc "Cássia, não! Pensa direito! Isso é loucura!"

    j "Loucura?! Loucura foi o que ele fez comigo! Isso é justiça!"

    "Não... ela não mudou nada. O Plano B continua. Tudo o que eu fiz não serviu pra PORRA alguma!"

    "Eu vou acabar sem a revista, sem a Cássia, sem a Sofia! MERDA!"

    j "E eu ainda serei aceita no Grupo! Acabar com quem acabou comigo e ainda me tornar a nova dona da porra toda!"

    "Não dá pra desistir agora. Eu preciso falar algo... descobrir como mudar ela de ideia! Mas se nem a filha..."

    "Calma... a Cássia é ambiciosa. É aí que eu tenho que pegar."

    "E eu consigo ver um furo no plano dela."

    mc "Tá louca, Cássia?! Você vai entregar a revista inteira pro Luca Alighieri de bandeja?! Pra ele te usar e te chutar depois, igual fizeram com a Zaza?!"

    mc "Você acha que o Grupo vai te dar o comando? Eles vão te dar um pé na bunda assim que você não for mais útil! Você não vai ter poder NENHUM!"

    j "Eles não fariam isso..."

    "A dúvida no olhar dela... consegui atingir um nervo."

    scene black with dissolve

    scene so7_img68 with dissolve

    mc "Ah, não fariam? Você acha que não fariam? Acha que pessoas como o Donatello, o Luca, o Tony! Que eles vão te dar o que você quer?"

    mc "Eles não são coitados como eu, Cássia. Eles vão te chutar!"

    j "Ugh... você não sabe o que tá falando."

    "Não funcionou?! Hora de apelar pro coração!"

    mc "E a Kaira?! Pensa nela!"

    mc "Você quer que a história dela, a dor dela, vire manchete de jornal sensacionalista?!"

    mc "Que a vida dela seja exposta pra todo mundo só pra sua vingança pessoal?!"



    ka "Mãe..."



    ka "Eu... eu não quero mais... confusão. Não quero minha vida... exposta."

    j "Kaira..."

    "Funcionou? A Kaira falando... isso pode mudar tudo..."

    mc "Tá vendo, Cássia? Tem outro jeito! Uma vingança muito mais... elegante. Mais definitiva."

    j "Que jeito? Você tá me enrolando, seu filho da puta."

    mc "Não! Me escuta! Toma o lugar dele. Vira a Editora-Chefe. Assume a porra toda!"

    j "Quê?"

    scene black with dissolve

    scene so7_img71 with dissolve

    mc "A Faux ainda não sabe nada. Você pode negociar com o Mauro e os acionistas diretamente. Pensando no SEU sucesso."

    j "Continue... quero ver se faz sentido."

    mc "Faz o chefe assistir, dia após dia, você sentada na cadeira dele, mandando e desmandando, controlando o legado que ele achava que era intocável!"

    mc "Humilha ele por dentro, Cássia! Destrói ele aos poucos, vendo você ter sucesso onde ele falhou! Isso não é mil vezes melhor do que só explodir tudo?"

    j "Tomar o lugar dele..."

    "Os olhos dela brilham com uma nova luz... a luz da ambição pura."

    mc "E eu te ajudo a conseguir isso! Eu conversei com o Mauro Ribeiro! Ele me ouviu, Cássia!"

    j "Por que alguém poderoso como o Mauro ouviria você?"

    mc "Não sei, mas tem algo com minha mãe."

    j "Não me diga que... hmm... que coisa. Você não faz ideia, faz?"

    mc "Eu? O quê?"

    j "Nada, pombinho. Continue. Me convença."

    mc "Se a gente for até ele e mostrar que a única forma de impedir a venda pra Faux é colocando VOCÊ no comando ele pode apoiar!"

    mc "Com você garantindo lucro, estabilidade, e abafando o escândalo do Escobar. Por que ele não aceitaria?"

    mc "A escolha pra ele vai ser simples... Cássia Roitman no poder, ou Luca Alighieri engolindo a revista. O que você acha que ele vai escolher?"

    j "Mauro... ele deve me odiar também. Mas, realmente, os investidores querem o lucro da revista e isso eu posos dar."

    mc "Suas matérias são as que têm mais cliques, mais comentários. Você sabe como a coisa roda."

    scene black with dissolve

    scene so7_img72 with dissolve

    j "Ter a revista... sem a Faux... ser a dona de tudo..."

    "Ela tá considerando... c-caralho, acho que vai dar certo!"

    j "E o Escobar... vendo ele rastejar... implorar..."

    j "Hmmm..."

    j "Você pode ser só um pombinho irritante, [mc], mas às vezes... às vezes você até qube usa a cabeça."

    mc "Então? Qual vai ser, Cássia? Destruição total e entregar tudo pro Grupo? Ou a vingança perfeita, com você no topo, no controle de tudo?"


    j "Ok, pombinho. Você me convenceu."

    j "O Plano B... está cancelado. Vamos pro Plano C... de Cássia no Comando."

    mc "BOAA!!!"

    "Eu consegui! Eu evitei! A Faux não vai comprar tudo! Porra, [mc]! Tudo é FODA!"

    j "Agora... me diga exatamente o que você falou com o velho Mauro."

    "UFA! Caralho, funcionou! Eu realmete consegui..."

    "Agora é 'só' convencer o Mauro... torcer pra ele concordar comigo. E e rezar pra Cássia não foder TUDO!"



    j "Plano C... Cássia no Comando. Gostei da sonoridade."

    mc "Ficou bom mesmo."

    scene black with dissolve

    scene so7_img71 with dissolve

    j "Então o próximo passo é falar com o velho Mauro Ribeiro. Convencer ele que eu sou a única salvação pra essa espelunca."

    "Única salvação... ou a nova praga. Depende do ponto de vista."

    mc "Exato. E eu acho que sei como aumentar nossas chances com ele."

    j "Ah, é? O pombinho virou estrategista agora? Desembucha."

    mc "A Kaira."



    j "A Kaira? O que ela tem a ver com o Mauro?"

    mc "O Mauro... ele me pareceu ter um lado mais... humano, digamos. Ele falou da minha mãe com um carinho que eu não esperava. Ele é padrinho da Sofia."

    mc "Se ele ver a Kaira... se ele ver você como mãe... talvez ele não te veja só como a Cássia Roitman, a jornalista FDP."

    j "Ei. Bom... eu sou a editora FDP mesmo."

    "Talvez ele veja a mulher por trás da máscara. Ou talvez ele só me mande tomar no cu por sugerir isso."

    j "Espera. Não! Você quer usar minha filha pra manipular o Mauro?! De jeito nenhum, [mc]!"

    j "Eu acabei de encontrar ela! Não vou jogar ela no meio dessa merda toda! Ela fica fora disso!"

    mc "Calma aí, é impressão minha ou você tá colocando o instinto maternal na ferente da ambição? Quem diria."

    j "CAL-"

    ka "Eu quero ir."



    j "Kaira? Você ouviu? Isso não é lugar pra criança!"

    scene black with dissolve

    scene so7_img69 with dissolve

    ka "Eu não sou criança. E eu quero ir."

    ka "Quero conhecer esse Mauro Ribeiro. Ele é amigo do meu... pai, não é?"

    "Pai... essa palavra na boca dela... que nó na garganta. O homem que queria que a Cássia abortasse."

    ka "Se ele conhece meu pai, talvez ele possa me contar... como ele é. Antes... antes de tudo."

    j "Kaira, não acho uma boa ideia..."

    ka "Mãe. Eu preciso saber. Eu preciso entender. E eu quero estar lá. Por favor."

    "Ela chamou de 'mãe'... que foda... deu até uma coisa. Mas eu não vou chorar."

    j "Tá bom. Você vai. Mas vai ficar quieta. Só observar. Entendeu?"

    ka "Entendi."

    j "E você, [mc]... se alguma coisa acontecer com ela por causa dessa sua ideia brilhante..."



    mc "Não vai acontecer nada, Cássia. Relaxa. Vai ser bom pra todo mundo."

    "Espero..."

    j "Que seja. Então vamos logo acabar com isso. Peguem suas coisas."

    scene black with dissolve

    scene so7_img46 with dissolve

    label sofia_final2_end:

        pass

    menu:
        "O final do chefe, da Sofia, meu, Cássia... É hora de decidir como tudo isso vai acabar.":


            pass

    mc "Vamos falar com o Mauro!"

    mc "Tenho certeza que ele vai me ouvir."

    j "Você é o novo discípulo dele? É a cara desses velhos machistas te escolher."

    mc "Tenho certeza que ele vai entender que você é a escolha natural depois do Escobar."

    ka "Eu sei lá, [mc]... pelo que eu vejo dos velhos da Cidade Chinesa... eles não gosta de mulher no poder."

    ka "A Liling teve que lutar muito."

    mc "Mas a Mestra é a chefe."

    ka "Você sabe como ela é... as poucas vezes que eu vi ela, ela teve que ser implacável pra conseguir o lugar dela."

    mc "Não tem ninguém mais implacável que sua mãe."

    j "Então chega de enrolar! Vamos fazer aquele velho me engolir."

    mc "Bora..."

    scene black with dissolve

    w "[mc]?"

    scene ani42 with dissolve

    mc "S-sofia!"

    "Aquele olhar... P-uta que pariu... Gelo puro. Ódio. Decepção."

    "Se olhar matasse, eu já tava virando presunto fatiado na mesa do açougueiro. E a Sofia seria a açougueira, com um sorriso sádico no rosto."

    "Cada segundo que eu passo do lado dessas duas, Cássia e Kaira, a ponte com a Sofia tá queimando mais rápido."

    "Se eu não resolver essa porra logo... já era. Adeus, Sofia."

    if sofia_namoro:

        "Adeus, noites de sono pensando naquela bucetinha que talvez eu nunca mais veja..."

        "Minha namorada perfeita... ela precisa me perdoar!"

    "Mas que se foda agora! Preciso focar no Mauro. Uma coisa de cada vez. Apagar um incêndio e depois pensar se ainda sobrou casa pra morar."

    scene black with dissolve

    pause

    scene 9201 with dissolve

    mc "Ok, deixa eu ligar pro escritório dele. Não dá pra chegar de surpresa."

    "Pelo menos não com a Cássia e a 'prova viva' do lado. Imagina o Mauro tomando um susto e tendo um infarto? Aí sim a revista ia pra vala de vez."

    j "Faça o que tem que fazer. Você disse que ia garantir que desse certo."

    mc "Eu disse?"

    j "Disse."

    "O que ele vai pensar quando descobrir que o Escobar, o protegido dele, teve essa filha e mandou a Cássia abortar? Mano..."

    scene black with dissolve

    scene 9202 with dissolve

    play sound "audio/som_3_celular.mp3"

    "{i}Discando... Tu... tu... tu...{/i}"

    "Secretário" "Escritório Mauro Ribeiro, bom dia."

    mc "Bom dia. Aqui é [mcc], da Revista Capital."

    mc "Por favor, avise imediatamente o Senhor Mauro Ribeiro que eu e a senhora Cássia Roitman estamos a caminho para uma reunião urgente sobre o futuro da revista."

    "Secretário" "Um momento, senhor... O senhor Ribeiro não agendou nenhuma reunião e a agenda dele está..."

    mc "Não interessa a agenda! Diga a ele que é URGENTE e que estamos chegando. Câmbio, desligo."

    "Que se f-oda a educação. Precisamos entrar. Depois eu mando um bombom de desculpas."

    j "Gostei de ver, pombinho. Às vezes você até parece ter culhões."

    scene black with dissolve

    scene ani43 with dissolve

    mc "É aqui. Prontas?"

    ka "..."

    "Kaira parece que vai vomitar a qualquer momento. Coitada."

    j "Eu nasci pronta, querido."

    "Claro que nasceu..."

    j "E você sabe que eu sempre consigo o que eu quero. Então, trate de conseguir pra mim."

    mc "Provavelmente já saiu do útero da mãe dando ordens e planejando aquisições hostis."

    j "Como é?"

    mc "Deixa pra lá..."

    play sound som_porta

    scene black with dissolve

    scene 9203 with dissolve

    "Secretário" "Senhor [mcc], senhora Roitman... e... senhorita? O senhor Ribeiro os aguarda. Por aqui, por favor."

    "Finalmente, a porta do chefão. O futuro da revista depende dessa conversa."

    scene black with dissolve

    scene 9204 with dissolve

    mr "Entrem. Fechem a porta."

    "A voz dele é calma, mas tem um peso... Esse velho não é qualquer um."

    mc "Senhor Ribeiro. Obrigado por nos receber assim, do nada."

    mr "A urgência, o futuro da revista... [mc], me deixou... intrigado. E a presença da senhora Roitman, mais ainda."

    mr "Sentem-se. Vocês sabem mesmo como criar expectativa."

    j "Mauro. Quanto tempo. Continua o mesmo de sempre, pelo visto."

    mr "Cássia. Sempre direta. Algumas coisas nunca mudam."

    mr "E a jovem?"

    "A Kaira parece que vai desmaiar."

    scene black with dissolve

    scene 9205 with dissolve

    mc "Senhor Ribeiro, esta é Kaira. Ela... ela é a razão principal disso tudo."

    mr "Kaira... Um nome incomum... neste local da ilha. E por que uma jovem como você estaria envolvida no 'futuro da revista'?"

    "Hora do show, caralho!"

    mc "M-"

    j "Mauro, vamos cortar a frescura. Você sabe que a revista tá na merda."

    mr "Como assim?"

    scene black with dissolve

    scene 9206 with dissolve

    j "A Faux News tá com a faca e o queijo na mão pra comprar essa espelunca por uma ninharia."

    mr "Não entendo. Nós acabamos de decidir ficar com a revista."

    j "Eu tenho uma proposta. Uma forma de salvar a sua amada revista da desgraça total."

    j "E de quebra, te dar um retorno financeiro muito mais interessante do que a esmola que o Luca Alighieri vai te oferecer depois que o escândalo do Escobar vier à tona."

    mr "Escândalo? Que escândalo, Cássia? O Escobar é um homem de reputação. Ele conseguiu convencer a mesa de diretores, com a ajuda do senhor [mcc] inclusive."

    menu:
        "Bem... talvez eu tenha ficado do lado errado.":


            mr "..."
        "Novos... desenvolvimentos aconteceram. Do tipo que mudam tudo.":


            mr "C-como é?"

    scene black with dissolve

    scene 9207 with dissolve

    j "Ah, Mauro, não pensei que você fosse assim... de varrer a sujeira pra debaixo do tapete."

    mr "Cássia! Eu não estou entendendo! Pare de charadas!"

    "O que a Cássia tá fazendo?! Por que ela tá criando todo esse teatro?!"

    j "Essa sujeira... ela tem nome e sobrenome. E está bem aqui."

    ka "Ei! Eu sou a sujeira?!"

    "O velho Mauro finalmente olha com mais atenção pra Kaira."

    ka "..."

    mr "Do que você tá falando, Cássia? Seja clara."

    j "Clareza? Tudo bem. Kaira é minha filha, Mauro. Filha do seu protegido, Escobar."

    "Ai caralho!"

    mr "!!!"

    j "Aquela que ele me obrigou a dar um fim."

    mr "Meu Deus..."

    scene black with dissolve

    scene 9208 with dissolve

    j "Eu tive que fazer um acordo com seu amigo, bem... com os amigos do seu amigo Luca."

    j "Consegui manter viva. Em segredo. Até agora."

    "BOMBA! Ela jogou a merda toda no ventilador de uma vez! Caralho!"

    mr "..."

    mr "Isso é... uma acusação muito séria, Cássia. Você tem provas disso? Ou é só mais uma das suas tentativas de causar o caos?"

    j "Provas? A prova está bem aqui, olhando pra você!"

    menu:
        "Olha pra ela, Mauro! Ela não te lembra ninguém?":


            mc "Esses cabelos de fogo, a teimosia..."

            ka "Ei..."

            mr "Heh..."

            "O Mauro encara a Kaira. E eu juro que vi... por um segundo... uma sombra de dor, de arrependimento, sei lá, passando pelos olhos dele."

            "Ele conhecia a história? Ele sabia do Escobar e da Cássia?"
        "Não é mentira.":


            pass

    scene black with dissolve

    scene 9209 with dissolve

    mc "Senhor Ribeiro... a Cássia não tá mentindo. Eu mesmo ajudei a descobrir... a ligar os pontos."

    mc "A Kaira foi criada na Cidade Chinesa, pela Liling, do Banho de Saúde e Beleza. Ela foi entregue ao Grupo... como parte de um acordo."

    mr "Essa história..."

    mr "O Grupo... Liling... Cidade Chinesa..."

    mr "Vocês estão me dizendo que o Escobar... meu sucessor... o homem que eu treinei... fez algo baixo assim?"

    j "Não diga 'fez' como se fosse uma vez. Ele sempre foi assim."

    menu:
        "Olhar bem por debaixo da saia dela":


            scene black with dissolve

            scene ani46 with dissolve

            pause
        "Prestar atenção na conversa":


            "Para de pensar besteira."

    j "As estagiárias... Um lobo em pele de cordeiro. E você foi cego demais pra ver."

    mr "Cego... ou talvez... eu tenha escolhido não ver."

    j "Não importa mais o que você viu ou deixou de ver, Mauro."

    j "O fato é que o segredo do Escobar está prestes a explodir. E quando explodir, a revista vai junto."

    j "A não ser... que a gente faça um acordo. Um novo acordo."

    mr "Agora tudo faz sentido."

    mc "Senhor Mauro..."

    mr "Eu entendi, [mc]. Que tipo de acordo, Cássia? O que você quer?"

    scene black with dissolve

    scene 9210 with dissolve

    j "Eu quero a revista."

    "Direta. Fria. Essa é a Cássia."

    j "Eu assumo como Editora-Chefe. Eu coloco a casa em ordem, garanto o lucro que vocês tanto querem."

    j "E o escândalo do Escobar morre aqui. Ninguém de fora precisa saber."

    j "A Faux News fica a ver navios. O Grupo não leva a revista por um centavo, que é quanto ela vai custar quando eu revelar a verdade."

    mr "Você quer que eu entregue a revista pra você... em troca do seu silêncio sobre o Escobar?"

    mr "E isso é o suficiente pela dor do que ele te fez passar? Você e sua garota? Eu sei que você é vingantiva."

    j "Ah... pombinho.... O Escobar... bom, o Escobar vai ter a punição que merece."

    j "Ele vai ver a jornalista que ele mais odeia sentada na cadeira dele."

    j "O velho sabia que eu era a próxima, eu era a pessoa certa. Mas ele nunca, nunca me daria o gosto."

    j "Ele colocou a puta da filha dele lá. Aquela nojentinha."

    mr "Ele é minha afilhada."

    scene black with dissolve

    scene 9211 with dissolve

    j "Foda-se! Foda-se você e o Escobar! Vocês não mandam mais porra alguma! E não vão ter o que querem!"

    j "É minha vez! Minha vez de ter o que eu quero!"

    "Caralho..."

    mr "E sua filha? A prova vida?"

    ka "É! E eu?!"

    j "Minha filha... a Kaira... ela fica comigo. Segura. Longe dessa sujeira toda."

    mr "Hmm..."

    menu:
        "Ele não parece convencido...":


            "Será que o Mauro vai aceitar? Dar a revista pra ela?"

            "Ou ele vai dar pro Luca e pro Grupo?!"

    j "É um bom negócio, Mauro. O melhor que você vai conseguir nessa situação de merda."

    j "Pense bem. Seu legado, seus investimentos... ou ver tudo virar cinzas por causa de um segredo sujo."

    j "Você apostou suas fichas no cavalo errado. Ele foi bem a corrida toda, mas colocou tudo a perder no final."

    "E agora? Ele vai aceitar a chantagem da Cássia? Ou vai deixar a bomba explodir e f-oder com tudo?"



    scene black with dissolve

    scene 9212 with dissolve

    mr "Cássia..."

    mr "Sua audácia nunca teve limites. Mas sua proposta... ela fede a desespero. O seu, não o meu."

    j "Desespero? Eu estou te oferecendo uma saída limpa, seu velho gagá!"

    mr "Uma saída limpa onde você senta no trono e dita as regras? Onde a 'verdade' se torna o que Cássia Roitman decide que é?"

    mr "Escobar pode ter sido um idiota, um canalha em muitos aspectos. Mas ele, ao menos, entendia que a revista servia a algo maior que o próprio umbigo."

    "Porra... tá dando merda!"

    mr "Você, Cássia? Você só serve a si mesma. Ao seu poder. À sua vingança."

    scene black with dissolve

    scene 9213 with dissolve

    j "Como você ousa?! Eu sou a única com culhões pra salvar essa porra de revista!"

    menu:
        "Tentar segurar a Cássia":


            pass

    mc "C-cássia! Calma!"

    mr "Salvar? Ou transformá-la no seu panfleto pessoal? Na sua arma de destruição em massa?"

    mr "Agora eu entendo perfeitamente porque Escobar nunca te considerou para o comando."

    j "Como é?!"

    mr "Você não tem ética, Cássia. Não tem responsabilidade. Você só tem ambição cega."

    "Puta que pariu, o Mauro tá jantando a Cássia com farofa!"

    scene black with dissolve

    scene 9214 with dissolve

    j "Você vai se arrepender dessas palavras, seu velho decrépito!"

    mc "Cássia! Não estrague tudo!"

    ka "[mc]! Eu te ajudo!"

    mr "E você realmente achou que trazer essa jovem... essa garota... Você achou que usar a dor dela, a história dela, ia amolecer meu coração?"

    ka "S-senhor..."

    mr "Tudo foi por água abaixo no momento em que você, na sua arrogância sem fim, se referiu à sua própria filha como 'sujeira'."

    ka "!!!"

    "Caralho... o Mauro pegou no ponto fraco. Chamar a filha de sujeira nunca é uma boa."

    scene black with dissolve

    scene 9215 with dissolve

    j "Eu... eu não! Você não entende! Era... era força de expressão!"

    mr "Força de expressão, Cássia? Ou a mais pura verdade sobre como você vê as pessoas? Peças no seu jogo doentio?"

    j "Pelo amor de Deus!"

    mr "Não. O acordo está desfeito. Ou melhor, nunca existiu. A revista não será sua."

    mc "!!!"

    j "O QUÊ?! VOCÊ NÃO PODE FAZER ISSO! SEU FILHO DA PUTA! EU VOU ACABAR COM VOCÊ!"

    j "EU VOU EXPOR O ESCOBAR! VOU JOGAR TODA A MERDA NO VENTILADOR! A FAUX NEWS VAI COMER VOCÊS VIVOS!"

    j "VOCÊ VAI VIVER POBRE!"

    "Aí fodeu! Cássia perdeu a linha de vez."

    scene black with dissolve

    scene 9216 with dissolve

    ka "Mãe! Para! Por favor!"

    j "CALA A BOCA, GAROTA! VOCÊ NÃO ENTENDE NADA! ELE ARRUINOU TUDO! TUDO!"

    "Plano C? Mais pra Plano Cabou Tudo. Que desastre!"

    menu:
        "Meter a cara e a mão na bunda dela":


            scene black with dissolve

            scene ani47 with dissolve

            pause

            "Ela tá tão nervosa que nem vai perceber..."

            "Hmm... o cheiro da buceta da Cássia... que delícia."

            "Ela puta e eu pegando gostoso nela. Eu sou um safado do caralho."

            ka "[mc]... você é um safadinho..."

            mc "E-eu..."

            ka "Ela é gostosa mesmo, né?"
        "Tá louco?!":


            "Ela acaba comigo!"

    mr "Senhora Roitman, e você, jovem Kaira, por favor, retirem-se. Minha decisão está tomada."

    j "RETIRAR?! EU NÃO VOU A LUGAR NENHUM! VOCÊ VAI ME OUVIR, SEU MERDA!"

    mr "Quer que eu chame os seguranças?"

    "Fodeu, fodeu, fodeu! Seguranças. Isso nunca acaba bem."

    menu:
        "Kaira! Tira sua mãe daqui! Eu te ajud-":


            pass

    scene 9217 with hpunch

    ka "Deixa comigo!"

    mc "K-Kaira?! Porra tu é forte!"

    j "NÃO ENCOSTEM EM MIM! EU VOU DESTRUIR VOCÊS! TODOS VOCÊS!"

    ka "Mãe, por favor! Vamos embora! Já chega!"

    j "ME SOLTA, GAROTA! EU AINDA NÃO TERMINEI!"

    scene 9218 with vpunch

    ka "Mãe! Não é assim que você vai mostrar pra ele!"

    ka "A Liling me ensinou como dominar as coisas! E nem sempre é com força bruta!"

    ka "E aqui não adianta! Aprende a jogar com suas cartas!"

    j "Garota..."

    j "Você é melhor que sua mãe..."

    ka "Hm?!"

    j "PORQUE EU NUNCA VOU ACEITAR QUE ESSE IDIOTA ME DIGA O QUE FAZER!!!"

    mc "Kaira! Tira ela!"

    ka "Tá certo!"

    play sound som_porta

    scene 9203 with hpunch

    "{i}BLAAAMMM{/i}"

    scene black with dissolve

    scene 9219 with dissolve

    "Ufa. Que show de horrores. E eu aqui, de camarote."

    "Tudo foi por água abaixo... a Cássia vai denunciar o Escobar e a moral dele vai cair em desgraça..."

    "Os investidores vão querer tirar o controle dele... e dar pra Faux."

    menu:
        "O Grupo ganhou! Merda!!! O que eu podia ter feito diferente?!":


            pass

    mc "Senhor Ribeiro... o senhor... o senhor tem certeza do que tá fazendo?"

    mr "Certeza, [mcc]? Nesse nosso ramo, a única certeza é a incerteza."

    mr "Mas eu fiquei entre a cruz e a espada."

    mr "A revista nas mãos de uma víbora descontrolada como a Cássia, que usaria a verdade como arma de vingança pessoal."

    mr "Ou permitir que a Faux News, com todos os seus defeitos e sua agenda questionável, assuma o controle..."

    menu:
        "O senhor acha que a Faux News vai ser... melhor?":


            pass

    "Melhor que a Cássia surtada? Talvez. Mas e a 'verdade'? E a Sofia? E o meu emprego, caralho?"

    scene black with dissolve

    scene 9220 with dissolve

    mr "Melhor? Não sei. Diferente, certamente. A Faux News tem uma estrutura, um alcance."

    mr "Eles podem manter meu legado. Mas a Cássia..."

    mr "A Cássia apenas aniquilaria tudo."

    mr "A Cássia, no poder, seria um câncer. Corroendo tudo por dentro até não sobrar nada além do ego inflado dela."

    "Pior que o velho tem um ponto. Dar a chave do galinheiro pra raposa Cássia não parecia a melhor das ideias, pensando bem."

    "Talvez o Plano C fosse uma roubada desde o começo."

    mr "Às vezes, [mcc], entre dois males, escolhemos o que nos parece... menos destrutivo a longo prazo."

    mr "Ou o que nos dá uma chance, por menor que seja, de manter algum tipo de controle indireto."

    "Ou seja, ele tá apostando que consegue manipular a Faux News de alguma forma? Ou só tá escolhendo o veneno que mata mais devagar?"

    mc "Eu... eu não sei o que dizer, senhor Ribeiro."

    "Minha cabeça tá um nó. Cássia ia explodir tudo. Faux News vai engolir tudo. Sofia vai se f-oder de qualquer jeito."

    "E eu? Bom, eu provavelmente vou ter que atualizar meu currículo."



    scene black with dissolve

    scene 9222 with dissolve

    mr "Não há muito o que dizer, [mc]. A situação é... deplorável. Mas decisões precisam ser tomadas."

    "Decisões... ele fala como se fosse fácil."

    "O que EU QUERO? Vou entregar a revista pra FAUX mesmo?"

    "Agora que Cássia tem a Kaira não adianta querer tirar ela. Ela tem a prova viva, o DNA, esse caminho de ignorar o passado já foi."

    label so_final2_final3_ponte:

        pass

    "Essa escolha MUDA TUDO. O que eu faço?"

    menu:
        "Entrego a revista para a Faux News e o Luca, o Tony e o Grupo ganha.":


            call final_bloqueado

            jump so_final2_final3_ponte
        "Eu vou insistir no Plano C. A Cássia é a ÚNICA forma de ferrar o Grupo.":


            pass

    "Puta merda! A Faux News! Se eles compram a revista, os Alighieri e os Donatello basicamente viram o dono da porra toda da informação na Capital!"

    "Adeus 'verdade', adeus qualquer chance de expor os podres deles! A revista vira o porta-voz oficial dos mafiosos, igual a Faux!"

    "E eu? Eu que já tô na lista negra deles por causa de tudo... eu não convenci o Escobar a vender.."

    "Eles me chutam pra rua no primeiro dia. Ou pior, me 'desaparecem'."

    scene black with dissolve

    scene 9223 with dissolve

    "Não. Não posso deixar isso acontecer. O Plano C... por mais fodido que seja ter a Cássia no comando... ainda é MELHOR que entregar tudo pro Grupo."

    "Não tem saída. É o Grupo, ou a Cássia. E foda-se o Mauro, eu VOU fazer a cabeça dele!"

    mc "Senhor Ribeiro... com todo respeito, mas acho que o senhor tá se precipitando."

    mr "Precipitando, [mcc]? Depois daquele espetáculo lamentável da senhora Roitman?"

    mc "Eu sei, ela perdeu a cabeça. Mas pense nas consequências REAIS se a Faux News comprar a revista."

    mc "Quando a merda do Escobar explodir... e vai explodir, a Cássia não vai deixar barato, o senhor sabe... o valor da revista vai pro esgoto."

    mc "Vocês vão ter que vender por uma merreca pro Luca Alighieri. Ele vai rir da cara de vocês."

    "É jogar baixo, mas preciso fazer ele ver a lógica fria da grana."

    mc "E não é só o dinheiro. Você vai acabar com a vida do Escobar, do seu pupilo!"

    mr "O mal menor, lembra? Ele... ele vai ter que dar um jeito de arcar com o que fez."

    "Eita velho frio."

    scene black with dissolve

    scene 9221 with dissolve

    mc "Vai acabar com a vida do Escobar publicamente, sim, mas vai respingar na Sofia também. A filha do monstro."

    mc "A carreira dela, da sua afilhada, a pessoa mais ética dessa cidade provavelmente, a vida dela... tudo no lixo. Eles vão ser massacrados."

    mr "..."

    "Acho que acertei um nervo."

    mc "E a verdade, senhor Ribeiro? A Faux News vai transformar a revista num panfleto do prefeito, do Grupo."

    mc "Adeus jornalismo investigativo, adeus qualquer pingo de independência editorial."

    mc "A Cássia... ela é uma filha da puta egoísta, sim. Mas ela é uma jornalista da porra. O senhor sabe!"

    mc "As matérias dela, por mais sensacionalistas que sejam, VENDEM. Elas trazem leitores, trazem dinheiro."

    menu:
        "Ela manteve essa revista relevante por anos, quer o senhor admita ou não.":


            pass

    mr "Você está me dizendo que eu deveria confiar a revista... o meu legado... nas mãos de Cássia Roitman?"

    mr "Ainda mais depois do que ela demonstrou aqui?"

    mc "Eu não confio nela pra passear com meu cachorro, senhor Ribeiro!"

    scene black with dissolve

    scene 9224 with dissolve

    mc "Mas ela é uma APOSTA! Uma aposta arriscada, mas ainda uma aposta!"

    mc "Com a Faux News, é derrota CERTA pra qualquer um que não seja do Grupo!"

    mc "A Faux vai ficar do lado do prefeito, dos Donatello, dos poderosos. Isso é óbvio!"

    mr "E qual o problema disso, [mcc]? O poder precisa de estabilidade. A ordem, mesmo que imposta, é melhor que o caos."

    menu:
        "Como é?! O Mauro é do Grupo!":


            "Que papo é esse? 'Ordem imposta'? Esse velho tá mais pra lá do que pra cá..."

            "Puta merda... 'qual o problema disso?'... O jeito que ele falou... Ele não é só um 'investidor preocupado'."

            "Merda, merda, merda. Ele pode ser um deles. Um peixe grande do Grupo que eu nem desconfiava."
        "Impossível. Ele ajudou a vender a revista. Ele não é do Grupo.":


            "Calma, [mc]... você tá indo longe demais. É a polícita do mal menor."

            "Pra ele o Grupo é menos pior que a Cássia. Só isso."

    "Foco... Preciso de uma cartada forte. Uma que toque nele de verdade. Minha mãe..."

    menu:
        "Senhor Ribeiro... minha mãe, Helena [mcsnome]. O senhor disse que conheceu ela. Que ela era uma grande jornalista.":


            pass

    mr "Sim. Uma das melhores que já vi. Corajosa. Apaixonada."

    "Dá pra ver um brilho diferente do olho dele. Ele... será que é saudades?"

    mc "Ela lutou contra essa gente, senhor Ribeiro. Contra o Grupo. Ela perdeu tudo por causa disso. Teve que fugir pra me proteger."

    mr "..."

    scene black with dissolve

    scene 9225 with dissolve

    mc "Ela acreditava na verdade, na justiça. O senhor... o senhor vai mesmo deixar o legado dela... digo..."

    mc "O legado do jornalismo que o senhor mesmo ajudou a construir, ser engolido por essa gente sem escrúpulos?"

    mr "Você está usando a memória da sua mãe para me manipular, [mcc]?"

    menu:
        "Eu tô te lembrando da VERDADE, senhor Ribeiro! A verdade que o senhor parece ter esquecido!":


            pass

    mr "Você... você tá indo em um terreno perigoso."

    "Me fodi! Fui longe demais!"

    mr "A Cássia... ela pode destruir tudo. Ela é incontrolável."

    scene black with dissolve

    scene 9226 with dissolve

    mc "E-eu vou tá lá, senhor Ribeiro. Eu vou estar na revista. Eu e a Sofia. A gente segura as pontas."

    mc "A gente garante que ela não passe dos limites. Deixe ela ter o gostinho do poder, a vingança dela contra o Escobar..."

    mc "Até que a Sofia esteja pronta pra assumir de verdade. E eu vou estar do lado dela."

    "Que promessa fudida eu tô fazendo... Segurar a Cássia? É mais fácil segurar um furacão com um guardanapo de papel."

    mr "Você, [mc]? Você acha que está pronto para ir contra o Grupo? Contra pessoas como Cássia Roitman? Contra o próprio Escobar, se ele se voltar contra vocês?"

    mc "Eu... eu tô com medo pra caralho, senhor Ribeiro. Mas eu tô. Eu tenho que estar."

    mr "..."

    "Desde quando eu fiquei tão confiante assim? Será que é ter quase morrido mil vezes?!"

    mr "Você me lembra tanto ela... sua mãe."

    mc "S-sério?"

    mr "A mesma teimosia, a mesma... chama. Talvez ela tivesse que correr, [mcc]. Fugir para sobreviver. Você pode ter que fazer o mesmo."

    scene black with dissolve

    scene 9227 with dissolve

    mc "Eu posso parecer ela, Mauro. Mas eu não sou ela."

    mc "Eu não vou fugir, senhor Ribeiro. Eu vou ficar. Eu vou lutar. Pode confiar em mim."

    mr "Confiar..."

    mr "Eu lembro quando comecei esta revista. Não era nada. Um folhetim de fofocas, rodado numa gráfica de quinta categoria."

    mr "Eu era um paparazzo, [mc]. Igual você. Correndo atrás de migalhas, de closes de celebridades decadentes..."

    mr "De podres do avô do Donatello, o pai do Vittorino. Aquilo sim era jornalismo de risco."

    "Vô do Basílio? Pai do Vittorino? Será ele o Donatello-Mor?"

    mr "O Escobar... ele era o único em quem eu realmente confiava. Um moleque esperto, ambicioso. Eu o treinei. Dei tudo a ele. E agora..."

    "Ele parece genuinamente quebrado. A traição do Escobar fodeu tudo."

    mr "Eu não sei se consigo entregar o que sobrou disso tudo nas mãos de alguém que não seja ele... ou alguém que eu realmente possa... guiar."

    "Já era. Ele não vai confiar na Cássia. O Plano C afundou antes mesmo de zarpar. A Faux News vai levar tudo. Fudeu."

    scene black with dissolve

    scene 9228 with dissolve

    mr "Você não sabe, [mcc], mas... eu e sua mãe... nós tivemos um caso."

    "QUÊ?! QUE PORRA É ESSA?!"

    "O velho tá me zoando? Um caso? Minha mãe e ele?!"

    mc "C-como assim, senhor Ribeiro?! Um... um caso?"

    mr "Sim. Logo antes dela... dela ter que sair da revista. Da cidade. Foi... um adeus. Intenso. Inesquecível."

    "Minha cabeça tá girando. Minha mãe? E o Mauro? Isso explica tanta coisa... ou não explica porra nenhuma."

    mr "Eu nunca confiaria na Cássia, [mcc]. Mas em você... há algo em você. Um instinto. Uma... decência teimosa que me lembra... eu mesmo."

    mc "!"

    mr "E, por mais cru que você seja, sinto que você pode vir a ser um bom jornalista."

    "Ele... ele tá falando sério? Confia em MIM?"

    menu:
        "Eu sou... o Mauro é meu pai?!":


            "Puta merda... será que... não... não pode ser... eu sou... f-filho... DELE?!"

            "A semelhança, a forma como ele fala da minha mãe, a 'confiança' repentina em mim... caralho!"

            "Foda-se. Se ele confia em mim, mesmo que seja por um motivo bizarro desses, eu tenho que usar isso AGORA!"
        "Não inventa, [mc]! Ele tá vulnerável, é agora ou nunca!":


            pass

    scene black with dissolve

    scene 9229 with dissolve

    mc "Senhor Ribeiro... se o senhor acredita em mim... se o senhor realmente vê algo da minha mãe, e de você, em mim..."

    menu:
        "Então acredite na Cássia.":


            pass

    mr "!!!"

    "Que se foda. Ou vai ou racha."

    mr "..."

    "Um silêncio mortal toma conta da sala... ele parece com a maior dor de cabeça do mundo."

    mr "Você... [mcc]... você me convenceu."

    "ESPERA AÍ! QUÊ?! Ele... ele aceitou?! Puta que pariu, funcionou! A cartada mais desesperada da minha vida e o velho caiu?!"

    scene black with dissolve

    scene 9230 with dissolve

    mr "Nunca, em todos os meus anos, imaginei que eu trocaria de opinião sobre Cássia Roitman."

    mr "Mas você... você está me levando por este caminho incerto. Um caminho que cheira a pólvora e problemas."

    mc "Eu sei do que o senhor tá falando. Aquela mulher é terrível."

    mr "A responsabilidade, no entanto, será sua. Sua e da Sofia. Vocês dois terão que manter Cássia Roitman sob controle."

    mr "Garantir que ela não transforme a revista no seu playground particular de vinganças e escândalos baratos."

    mc "P-pode deixar, senhor Ribeiro! A gente... a gente dá um jeito! Com certeza!"

    "Com certeza o caralho! Manter a Cássia na linha? É mais fácil ensinar um porco a cantar ópera!"

    mr "Talvez o Escobar possa desaparecer sem causar. Que decepção..."

    menu:
        "Ele fodeu tudo. E sempre foi chato.":


            mr "Se envolver com uma secretária... mandar ela abortar ainda. Onde ele tava com a cabeça?"

            mc "Pensando com a porra do cacete. Ele sempre foi babaca. Ainda ignorou a filha."

            mr "Caralho..."
        "O velho fez o que podia. Eram outros tempos.":


            mr "Eu sei, as coisas não eram as mesmas... mas fazer isso..."

            mc "Ele vai pagar pelo que ele fez."

            mr "..."

    scene black with dissolve

    scene 9231 with dissolve

    mc "Não tinha como você saber, Mauro. Ele sempre foi um bom jornalista, pelo que você fala."

    mr "Sim. Eu ensinei ele a farejar o que as pessoas querem ler."

    mc "Mas ele tinha um problema. Ele gostava de novinhas. E poder quando sobe na cabeça..."

    mr "[mc]... você é diferente."

    mc "Eu também tenho minhas coisas. As coisas erradas que eu fiz."

    mr "Você... você pode se tornar o próximo. Ser melhor que o Escobar, e até que eu."

    menu:
        "Valeu, Mauro. Eu não vou decepcionar você. Eu vou fazer a revista ir pra frente.":


            mr "Conto com você."
        "Eu tô nessa pela grana e as garotas. Perdão.":


            mr "Bem... quem sabe um dia você não sente esse chamado."

            mc "Acho que não, mas quem sabe."

    mr "Então estamos acertados."

    "CONSEGUI! PUTA MERDA, EU CONSEGUI! A revista não vai pra Faux News! O Grupo não leva!"

    "A Cássia vai ter o poder dela, mas... sob nosso 'controle'. E eu... eu tô no comando dessa porra toda, de um jeito ou de outro!"

    scene black with dissolve

    scene 9232 with dissolve

    mr "Não se engane, [mcc]. A luta contra o Grupo precisa continuar."

    mr "A Revista Capital é um dos poucos contrapesos que ainda restam contra o poder absoluto dos italianos e seus associados nesta ilha."

    mc "O senhor... o senhor e minha mãe... vocês também lutavam contra o Grupo dessa forma?"

    mc "Porque o Escobar... ele sempre pareceu passar um pano pra eles, deixar as coisas correrem mais soltas."

    mr "Eu ensinei ao Escobar o que eu sabia. O que eu aprendi na marra e que passei pra ele e pra sua mãe."

    mr "A luta contra eles precisa ser... cirúrgica. Cautelosa. Um passo em falso, e eles te devoram vivo."

    mr "É frustrante, parece que estamos do lado dele,s mas você não pode perder mais do que conquista, ou a guerra já está perdida antes de começar."

    menu:
        "Entendi.":


            "Então ele não era do Grupo. Ele só... luta do jeito dele."
        "Não concordo com isso!":


            mc "Cautela, senhor Ribeiro? Com o que eles FAZEM?! Eles são monstros!"

            mc "Eles es-cravizam garotas pra fazerem um ritual maluco! Usam elas como se fossem... objetos!"

    if sacerdotisas >= 1:

        "Aquele contrato da Júlia... as três de quimono... a Diana falando das 'sacerdotisas' do Barão... O [us] também tocou nesse assunto..."

    mr "Você...? Você sabe sobre as Sacerdotisas?"

    mc "S-sim, senhor. Eu... eu tropecei em algumas coisas. Informações. Fotos."

    scene black with dissolve

    scene 9233 with dissolve

    mr "Então... então você também tem uma parte das informações."

    mc "Eu tenho? Como assim? O que o senhor quer dizer?"

    mr "Parece... parece destino, [mcc]. Que justamente você, o f-ilho de Helena, esteja desenterrando essa sujeira toda."

    menu:
        "Destino? Por quê? O que a minha mãe tem a ver com as Sacerdotisas?":


            $ sacerdotisas = 3

            play sound notificacao

            $ renpy.notify("Você descobriu outra pista sobre o mistério das Sacerdotisas")

            "Que porra tá acontecendo? O que a velha aprontou?"

            mr "Foi essa matéria, garoto. Foi essa reportagem sobre as Sacerdotisas... foi ela que obrigou sua mãe a deixar a Capital. A fugir para te proteger."

            mc "!!!"

            "Puta merda. Meu sangue gela. Minha mãe... ela descobriu sobre as Sacerdotisas? E por isso teve que fugir?"

            "Por isso ela sempre ficou puta quando eu perguntava do passado, querendo que eu ficasse longe da Capital?"

            "Eu tive que dá um surto pra ele me deixar estudar aqui... e ela conseguiu o emprego pra mim na revista..."

            "Talvez... paparazzo... talvez ela quisesse me manter longe disso tudo. Mas o destino..."

            mr "Se você quiser, [mcc]... como um ato de... honestidade, de ética jornalística que sua mãe tanto prezava... eu posso te entregar a matéria original dela."

            mr "Eu guardei. Todos esses anos. Como uma... uma lembrança. Um amuleto de Helena. Da coragem dela."

            "A matéria da minha mãe... a que quase custou a vida dela. E a minha."

            "Eu preciso ler isso. Preciso saber o que ela descobriu. O que fez o Grupo querer apagar ela do mapa."

            mc "Eu... eu aceito, senhor Ribeiro. Eu quero ler."
        "Eu não quero saber disso. Quanto menos eu souber, menor risco eu sofro.":


            mr "Esperto. Mas sua mãe trabalhou duro por isso. Aposto que ela ia querer que você visse."

            mc "Ok..."

    scene black with dissolve

    scene 9234 with dissolve

    mr "Aqui está. Mas um aviso, [mcc]. Espero que isso não acabe te matando."

    mc "Caralho, viu... mais uma."

    mr "Mas antes de você se afogar no passado da sua mãe... vá."

    mc "Hm?"

    mr "Vá avisar a cobra da Cássia Roitman que ela é a nova Editora-Chefe."

    mc "A Cássia!"

    mr "Antes que aquela mulher, no seu descontrole, realmente exploda a porra toda e coloque o próprio plano dela a perder."

    "Meu Deus! A Cássia! Ela deve tá espumando de raiva, pronta pra ligar pra Faux News e vender a alma por um prato de vingança fria!"

    mc "P-pode deixar, senhor Ribeiro! Eu vou correndo!"

    mr "E [mcc]..."

    mc "Sim, senhor Ribeiro?"

    mr "Nunca se esqueça... o caminho de quem vai contra o Grupo é um caminho de dor. De perdas."

    mr "Prepare-se para perder tudo. Porque é isso que eles fazem. Eles tiram tudo de você."

    "Um arrepio percorre minha espinha. Perder tudo... igual minha mãe."

    "Mas eu não sou ela. Eu não vou fugir."

    mc "Eu tô pronto, senhor Ribeiro. Deixa eles virem."





    scene black with dissolve

    scene ani44 with dissolve

    "E assim, do nada, o mundo virou de cabeça pra baixo."

    "Escobar... ah, o velho chefe... saiu da redação não como ele imaginava... nas como um rato escorraçado."

    "Cássia fez questão de esfregar na cara dele cada podridão, cada sujeira, cada ano de humilhação que ela guardou."

    "Foi um espetáculo grotesco. A mulher soube como se vingar... deu até dó do velho."

    scene black with dissolve

    scene 9235 with dissolve

    "Cássia Roitman. Nova Editora-Chefe da Revista Capital. Parece até piada, mas é a porra da realidade."

    "E quem ajudou a colocar a coroa na cabeça da diaba? Eu mesmo, o trouxa aqui."

    "Renata, a loirinha esperta, não perdeu tempo. Subiu que nem foguete."

    "Agora é a nova Coordenadora de Produção, o cargo que era da Sofia."

    "Como que a secretária vai fazer esse trabalho? Não sei..."

    "Ronaldo, o cachorrinho oficial dela, também se deu bem. Virou editor. Quem diria que ter um pau amigo abriria tantas portas? Anotado."

    "E a Kaira... até a novinha da Kaira. Tá aqui na redação, fazendo uns trabalhos simples."

    "Será que ela quer seguir os passos tortos dos pais? Ou passar mais tempo com a mamãe?"

    "Jornalismo, vingança... sei lá que porra ela tá pensando. Mas ela tá aqui. Sob as asas da mamãe Cássia."

    scene black with dissolve

    scene 9236 with dissolve

    j "...e que fique bem claro! A Revista Capital vai continuar fazendo o que sempre fez de melhor..."

    j "Dar ao público EXATAMENTE o que ele quer!"

    j "E isso significa fofoca da boa, escândalos suculentos, a vida íntima dos seus ídolos exposta pra quem quiser ver!"

    j "Esse papinho de 'jornalismo ético', 'verdade acima de tudo'... isso é conversa pra boi dormir!"

    j "Uma revista é INÚTIL se não ressoa com as pessoas, se não vende, se não causa burburinho!"

    scene black with dissolve

    scene 9237 with dissolve

    j "Nosso objetivo é dar a elas o que elas querem! E mais! Vamos dar a elas o que elas NEM SABIAM que queriam!"

    j "Vamos cavar fundo na sujeira, porque é na sujeira que o ouro brilha mais forte!"

    j "A minha nova equipe de direção está pronta! Renata, Kaira, Ronaldo, coloquem todos na linha!"

    "Renata, Kaira, Ronaldo" "Sim, senhora!"

    j "Agora vão! Se enterrem na lama e me tragam esse ouro, imbecis!"

    scene black with dissolve

    scene 9238 with dissolve

    "Jornalistas" "Sim, senhora!"

    w "..."

    "Um pragmatismo nojento, mas que, infelizmente, faz um certo sentido nesse mundo."

    "Ela tá cuspindo na cova da 'ética' da Sofia e ainda tá rindo."

    w "Essa vaca..."

    mc "Sofia."

    w "Que foi?!"

    mc "N-nada..."

    w "Acho bom."

    "Sofia... ela não aguentou. Foi demais pra ela."

    menu:
        "Ir atrás da Sofia... é ela que eu quero.":


            "Eu não vou desistir da Sofia. Ela vai entender o porque disso tudo."

            scene black with dissolve

            scene 9239 with dissolve

            mc "Sofia? Você... você tá bem? O que você tá fazendo aqui?"

            "Que pergunta idiota, [mc]. Claro que ela não tá bem, seu animal."

            w "Bem? Você tá vendo onde eu tô, [mc]?! Ela me colocou como recepcionista, acredita?!"

            mc "!!!"

            w "Deu meu lugar pra puta da Renata e me colocou aqui!"

            "Merda! Aquela filha da puta! Eu devia ter imaginado..."

            w "Meu pai... o homem que eu, apesar de tudo, admirava... é um monstro, [mc]. E ele desapareceu em desgraça!"

            w "O cargo que eu estudei a vida inteira pra ter, a chance de seguir os passos do meu pai, de fazer a diferença... foi pra vala."

            w "A Cássia me odeia. Ela nunca vai me deixar chegar perto de nada importante aqui. Eu virei uma ninguém. Uma recepcionista!"

            mc "Sofia..."

            scene black with dissolve

            scene 9240 with dissolve

            w "E a revista... o 'jornalismo'... virou essa palhaçada sensacionalista que a Cássia tá vomitando."

            w "Eu perdi tudo, [mc]. Tudo!"

            "Ela tá destruída. E eu... eu culpa nisso. Uma parcela bem grande, pra ser honesto."

            if sofia_namoro:

                mc "Sofia... você não perdeu tudo. Você... você ainda tem a mim. A gente é namorado, eu vou te ajudar!"

                "Que frase clichê do caralho. Mas saiu. Fazer o quê."

                w "Você? [mc], você arquitetou essa merda com a Cássia! Você sabia o que ia acontecer!"

                mc "Ai..."

                w "Por isso você tava todo estranho! Você deve ter ganhado a porra de um cargo excelente, né?! Tá no meu lugar?!"

                mc "Não... não é nada disso."

                w "Você acha mesmo que eu quero do meu lado o cara que ajudou a construir o meu pior pesadelo?!"

                "Direto no meu estômago. E ela tem razão. Que merda."

            scene black with dissolve

            scene 9241 with dissolve

            menu:
                "Era o único jeito! Era isso ou a Faux!":


                    mc "Sofia, era a única chance! Era isso ou o Grupo engolia tudo! A culpa não é minha!"

                    mc "A culpa é do SEU PAI! Foi a merda que ELE fez que começou essa bola de neve!"

                    "Joguei baixo. Botei a culpa no velho. Mas ela precisava ouvir. Ou eu precisava dizer pra me sentir menos culpado."

                    w "..."
                "Tem razão. Não tem desculpa.":


                    w "Foda-se!"

            w "Acabou, [mc]. Tudo acabou."

            "Ela parece tão... vazia. Derrotada. E eu, que ajudei a colocar ela nesse buraco, me sinto um lixo."

            "O Mauro disse... 'prepare-se para perder tudo'. Será que já começou? Será que a Sofia é a primeira coisa que eu perco?"

            "Não! Eu não vou deixar as coisas assim!"

            "Tá na hora de usar meu poder! A lábia suprema!"

            menu:
                "Não acabou, Sofia.":


                    scene black with dissolve

                    scene 9242 with dissolve

                    mc "O Mauro... ele ainda confia na gente. Em nós dois. Ele disse que conta com a gente pra manter a Cássia na linha."

            mc "Ele ainda é o líder da mesa de diretores. Ele pode tirar a Cássia do poder se ela foder demais com as coisas."

            w "O Mauro? Você... você acha que... que eu devia ficar?"

            mc "Sim, Sofia! Fica! Luta! A gente vai ter um trabalho fudido pra manter essa revista nos trilhos!"

            mc "Pra impedir que vire só um panfleto que se você espremer escorre sangue e porra!"

            mc "Mas a gente pode tentar! Juntos!"

            $ sofia_ficou = True

            w "Ficar... e aguentar a Cássia? Ela... ela vai me tratar como um capacho. Ela vai me humilhar."

            w "Ela vai me fazer engolir cada palavra que eu já disse sobre ética. Vai me forçar a assistir ela transformar tudo o que eu acredito em... em piada."

            mc "Provavelmente... mas, assim... ser secretária é um trabalho honesto."

            scene black with dissolve

            scene 9243 with dissolve

            w "Vai ser como... como ser uma submissa da minha pior inimiga."

            w "Ter que obedecer cada ordem nojenta, sentir o po-der dela sobre mim... cada toque, cada olhar de des-prezo..."

            mc "C-como é?"

            w "Ela provavelmente vai querer que todos os funcionários an-dem de quatro pela redação, que a gente la-mba o chão que ela pisa..."

            w "Que a gente tre-pe com quem ela mandar, só pra mostrar quem tem o con-trole da bu-ceta e do ca-ralho de todo mundo aqui!"

            mc "O Ronaldo que o diga... mas-"

            w "E eu vou ter que... que aceitar... que talvez até... encontrar algum tipo de... prazer per-verso nisso tudo?"

            mc "Como é? Repete essa parte."

            w "[mc]... essa mulher é uma puta sádica. E ela tem todo o poder agora. Você entende? Nós somos putas dela agora."

            mc "Eu não dir-"

            w "Ela é a figura de autoridade. Ela é o novo papai... e... eu tenho que obedecer. Eu sempre fui uma boa garota, não é?"

            "Ela tá com um olhar vidrado, quase maníaco. Que porra tá acontecendo com ela?"

            mc "Sofia... você?"

            scene black with dissolve

            scene 9244 with dissolve

            w "Com aquele jeito mandão dela... pervertido, inescrupuloso, com aquelas roupas, fodendo a Renata, o Ronaldo, meu pai."

            mc "Você sabia disso tudo?"

            w "Ela sempre foi assim, e eu sempre lutei... mas agora ela tem todo o poder. Sou só uma garota perto da dona da porra toda."

            w "Aah..."

            mc "S-sofia?"

            w "Eu... e-eu vou testar. Você tem razão. Digo... vou ver se é possível aguentar. Pela... revista. Pelo... pelo que sobrou."

            w "Aguentar ser a putinha da Cássia... só quero ver o que ela vai mandar eu fazer... hmm..."

            menu:
                "E a gente? Como fica?":


                    scene black with dissolve

                    scene ani45 with dissolve

                    mc "Sofia... e a gente? Depois de tudo isso... você... você ainda consegue... me perdoar? A gente ainda tem uma chance?"

                    "Preciso saber. Mesmo que a resposta me destrua."

                    w "..."

                    w "Bom... [mc]..."

                    w "Vamos ver o que acontece nesta revista, não é?"

                    $ renpy.notify("Você ainda tem uma chance com a Sofia")

                    "Que porra de resposta é essa?! Sim? Não? Talvez? Ela tá me deixando na corda bamba, a desgraçada!"

                    "Mas... é uma esperança. Uma minúscula, fudida e talvez doentia esperança. E nesse momento, é tudo o que eu tenho."
                "Não... a gente não vai ficar juntos.":


                    pass

            mc "Sofia, eu-"

            scene 9245 with hpunch

            j "{i}POOOMBINHOOO! VEM CÁÁÁ, SEU CACHORRO! AGORA!{/i}"

            "A Cássia. Gritando como se fosse a dona do canil e eu o vira-lata sarnento."

            w "Vai lá... obedece nossa dona..."

            "Melhor obedecer antes que ela solte os verdadeiros cachorros em cima de mim."
        "Esquece a Sofia. Agora eu quero a Cássia.":


            "Vou falar com a Cássia. Muito melhor. A Sofia era a chefinha, mas agora a Cássia é a porra da CHEFE."

    scene black with dissolve

    scene trabalho chefe_porta with dissolve

    "A sala do chefe. Do Escobar... agora é a sala dela."

    play sound som_porta

    scene black with dissolve

    scene 9246 with dissolve

    "CARALHO! Mas que porra é essa?!"

    "Renata tá sentada no co-lo da Cássia, a Cássia tá com as duas mãos firmes na bunda dela, apertando aquela carne gorda e macia."

    re "Aihh... Cássia... assim... a gente conseguiu, chefa... agora a gente que manda nessa porra toda!"

    j "Isso mesmo, minha putinha ambiciosa. A mamãe Cássia tá no comando agora."

    "A mão da Cássia tá afundada na bu-ceta da Renata... é uma puta mesmo."

    "Dá pra ver os dedos da Cássia fodendo aquela vadia."

    j "E eu vou foder você todo dia nessa mesa, sua vadiazinha loira. Só pra te lembrar quem é que te colocou no poder."

    re "S-sim, senhora Cássia... me fode... me usa... aahnn..."

    ka "Mãe, você não precisa falar assim com ela... ela é tão linda."

    "Kaira?! Ela também tá aqui?!"

    scene black with dissolve

    scene 9247 with dissolve

    j "Fica quieta, Kaira. Aprenda como se trata uma safada submissa."

    ka "Mãe..."

    re "Aainnn!"

    "A Cássia puxa a Renata pelo cabelo, e mete o dente no pescoço dela."

    re "ISSO... AAHH... CHEFA... Me morde... me machuca... aqui... na frente deles!"

    ka "Ela é uma puta mesmo..."

    j "Quando eu mandar, puta. E onde eu mandar."

    scene black with dissolve

    scene 9248 with dissolve

    re "Hmmmm... essa sua voz... mandando em mim... me dando ordens..."

    re "Você me ensinou a ficar com a minha pepeca querendo uma rola bem grossa pra me arrombar..."

    ka "É sempre assim com essas putas, [mc]? Ficam todas molhadinhas só de ouvir uma ordem da minha mãe?"

    mc "K-Kaira! V-você... o que você tá fazendo aqui?"

    ka "A mesma coisa que você. Olhando. Mas e aí?"

    mc "Eu... eu não tenho muita experiência com... reuniões assim, Kaira. Mas parece que sim."

    "Na verdade, a única puta que eu vi na mão da Cássia fui eu mesmo... Mas isso ela não precisa saber."

    j "Não é ele, filha. É o Ronaldo."

    re "Ahnn... o Ronaldo... hmmnnng..."

    scene black with dissolve

    scene 9249 with dissolve

    ka "Quem é esse?"

    j "O Ronaldo vai adorar saber que tem duas bucetas novas e famintas esperando pela piroca dele todo dia."

    ka "Mãe! Eu não quero saber desse Ronaldo!"

    re "Aahhn... é que você ainda não viu o... cacetão gigante... aahnn.. dele."

    ka "Eu tenho mais vontade de conhecer o [mc]..."

    mc "Q-quê?!"

    j "Quê?! Mas ele tem uma minhoquinha, filha. Ele não é homem pra você."

    scene black with dissolve

    scene 9250 with dissolve

    ka "E daí? E se eu gostar de minhoquinhas?"

    menu:
        "Você gosta mesmo de pau pequeno?":


            ka "Sim... é fofo... pequeno e bonitinho. Eu fico toda excitada."

            mc "N-nossa..."
        "Eu não tenho pau pequeno!":


            ka "Uma pena..."

    j "HAHAHA! Essa minha filha!"

    scene black with dissolve

    scene 9251 with dissolve

    re "Fica.. hmmm... mais pra mim."

    j "Você e a Sofia... ah, a Sofia vai ser a próxima. Aquela lá tá louca pra levar uma chi-cotada no ra-bo."

    mc "A Sofia?! Você tá louca, Cássia! Ela nunca participaria disso!"

    "A imagem da Sofia 'certinha' pedindo pra apanhar... querendo a rola do Ronaldo. Impossível."

    re "Sabe nada! Ahnn! Esse aí!"

    j "Eu vi nos olhos dela, pombinho. Aquela garota quer rola, quer apanhar, quer ser abusada até não aguentar mais."

    j "Ela só não sabe como pedir. Mas a mamãe aqui vai ensinar."

    mc "Você... você é louca, Cássia."

    j "Louca por poder, [mc]. E por um bom par de tetas pra apertar."

    re "Ahhnn! Aperta a minha, minha dona! Minhas tetas são suas!"

    j "Cala boca. Você não veio aqui só pra assistir, veio?"

    scene black with dissolve

    scene 9252 with dissolve

    mc "C-Cássia... vim porque você me chamou..."

    ka "Eu tô feliz que você veio, [mc]. Essas duas não param de se comer, fiquei de fora."

    mc "Haha... tá bom."

    "Desde que eu trouxe a Kaira, parece que ela tá me curtindo."

    "Será que seria coisa de outro mundo ficar com ela? Tipo... ela é novinha, tem o corpo gostoso... e esses peitinhos."

    j "Chamei, sim. Lembra do que eu te disse? Sobre os amigos de Cássia Roitman?"

    mc "O-opa..."

    "Melhor focar na mãe agora."

    menu:
        "Que só coisas boas acontecem com seus amigos?":


            pass

    j "Exato. E você, meu ladino safado, que convenceu o idiota do Mauro, merece uma recompensa."

    mc "Uma promoção? Vou finalmente poder mandar em alguém além do estagiário do café?"

    j "Promoção? Hahaha! Você é tão ingênuo, [mc]. Não, sua recompensa é outra."

    scene black with dissolve

    scene 9253 with dissolve

    mc "Cássia! O Ronaldo virou editor! Eu mereço mais que ele!"

    re "Aah... Cássia... eu vou... gozar... aahnn..."

    j "Aguenta firme, minha cadela. A chefe ainda não mandou."

    j "Não, pombinho. Eu prefiro você ralando, no chão, igual um cachorrinho."

    mc "Não é possível... você tá me punindo por causa da Sofia, né?"

    j "E se eu tiver?"

    mc "Vaca... você se diverte me fazendo de lixo, né?"

    re "Ahhnn... ela ama..."

    j "Mas não vou te deixar sem nada. Os amigos de Cássia Roitman sempre se dão bem."

    j "A sua recompensa, [mc], é a seguinte... eu sei o acordo que você tinha com o filho da puta do Escobar."

    mc "As pautas... quase sendo demitido toda porra de semana!"

    j "Pois bem. Eu não preciso mais das suas pautas de merda."

    scene black with dissolve

    scene 9254 with dissolve

    "QUÊ?! EU OUVI DIREITO?! SEM PAUTAS?!"

    mc "C-como é, Cássia?! Tá falando sério?!"

    j "Tudo o que você tem que fazer é continuar sendo meu cachorrinho. Você é muito mais útil assim."

    mc "Claro que tinha algo..."

    j "Você escolhe. Prefere dar as pautas ou ser meu bebê obediente, hein?"

    menu:
        "Ok... Me livra das pautas e eu viro seu cachorrinho.":


            $ pautas_liberado = True

            scene black with dissolve

            scene 9255 with dissolve

            j "Hmmm... é assim que eu gosto, pombinho."

            "Eu... eu não acredito! É o fim da tirania das pautas! Eu tô... livre?!"

            mc "Eu... eu aceito, Cássia. Contanto que eu não precise mais caçar pautas..."

            "Ser o boneco da Cássia ou voltar pra miséria das pautas? A escolha é óbvia pra caralho."

            j "Pode comemorar, cachorrinho. Você merece um ossinho."
        "Nada disso. Eu me viro com as pautas.":


            $ pautas_liberado = False

            j "Você fica tão sem graça quando tenta ser macho."

            "Vou ter que continuar entregando pautas... pra Cássia agora, mas pelo menos mantenho a dignidade."

            j "Mas comigo vai ser diferente. Vai ter que dar o dobro de pautas."

            mc "Quê?!"

            j "Essa é sua promoção."

            mc "Cadela."

            j "Hahaha! Fica bravinho, fica!"

    ka "Para de pegar no pé dele, mãe."

    re "Chefa... por favor... eu não aguento mais... me deixa gozar..."

    j "Hmm... tá bom, minha putinha. Mas só porque você foi uma boa menina hoje."

    "A Cássia enfia os dedos com mais força ainda, e a Renata dá um grito abafado."

    "O corpo todo tremendo enquanto ela tem um orga-smo ali mesmo, no colo da chefe, na frente de todo mundo."

    scene black with dissolve

    scene 9256 with dissolve

    re "Aahnnnnnn!"

    j "Isso, minha puta, goza pra sua chefe, goza..."

    ka "Mãe... você é terrível..."

    "Meu pau tá duro pra caralho. A Renata gozando, a Cássia dominando, a Kaira assistindo... essa redação virou um puteiro de luxo."

    j "Viu só, [mc]? O poder que eu tenho? Eu dou prazer, eu tiro o fardo das suas costas..."

    if pautas_liberado:

        mc "Eu... eu não sei como agradecer, Cássia..."

        j "Ah, eu sei como você pode agradecer. Você vai continuar sendo meu brinquedinho particular, claro. Meu cachorrinho que vem quando eu chamo."
    else:


        mc "Ô... fala pro dobro de pautas que vou ter que entregar."

        j "A escolha foi sua."

    j "Muito bem. Estamos prontos para iniciar uma nova era nesta revista."

    j "Vamos conseguir essa grana, essa tiragem, esse público. E mostrar pro Mauro que eu sou muito melhor que o velho careca."

    scene black with dissolve

    scene 9257 with dissolve

    ka "Não esquenta que eu vou fazer ela te agradar também a partir de agora, [mc]."

    mc "A é, Kaira? Ok."

    ka "E se ela não te agradar, eu te agrado."

    mc "Eita..."

    "Como vai ser voltar pra cá agora com a Cássia no poder?"

    "A redação vai ser toda diferente."

    "E a Sofia? Será que ela vai continuar aqui? Será que a gente tem alguma chance de mudar isso?"

    "E a Kaira, hein? Carai... talvez eu acabe me dando bem hehe..."

    menu:
        "E o mais importante... eu VENCI o Grupo!":


            pass

    "Pelo menos eu venci o Luca. Ele ainda vai ter a gente no pé dele. O Grupo NÃO vai dominar TODA a informação."

    "Toma cuidado comigo, Donatello, Alighieri... Tony."

    "E a matéria da minha mãe sobre as Sacerdotisas?"

    "Parece que tudo tá culminando no grande momento! E ele tá MUITO perto!"

    play sound notificacao

    scene black with dissolve

    $ renpy.notify("Você conquistou um novo final")

    $ persistent.sofia_final2 = True

    $ sofia_final2 = True

    "{b}Parabéns! Você conquistou o Final 2 da Sofia! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    scene white with dissolve

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
