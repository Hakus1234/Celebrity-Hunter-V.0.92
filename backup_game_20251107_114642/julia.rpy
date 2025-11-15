label julia_cel_msg1_resposta:

    $ julia_cel_msg1_resposta_check = False

    mc surpreso "A [g] me mandou uma foto da [s]!"

    mc zerado "Essa menina não tem jeito mesmo... Que perigo ter ela como irmã."

    "Que bonitinha a [s] treinando no celular. Tomara que ela me mande uma mensagem logo."

    "E o que eu vou responder sobre essa foto?"

    menu:
        "Valeu! Pode mandar mais fotos.":


            $ julia_cel_msg1_r = "sim"

            mc tarado "A [g] vai acabar sendo muito útil pra mim."

            mc "Imagina quantas fotos interessantes ela vai tirar morando com a [s]..."
        "Não quero que mande fotos da [s].":


            $ julia_cel_msg1_r = "nao"

            mc serio "Não quero constranger a [s]. A [g] precisa parar com isso."

    "Certo. E sobre me encontrar com ela?"

    "Será que tá certo eu ver ela mesmo saindo com a irmã?"

    "Ela trabalha no Tadaima. Fica perto da minha casa. Se eu tiver afim, posso dar uma passada lá."

    "Não é porque vou ver ela que precisa significar alguma coisa, certo?"

    "Opa. Ela já respondeu."

    show screen celular_julia

    "..."

    "Essa menina é uma peça."

    "Só não sei se eu devo me envolver com ela..."

    "Pensando bem, se eu me aproximar da [g] posso ganhar pontos com a [s] também."

    "Tenho certeza que ela ia gostar mais de mim se eu me desse bem com a irmã estranha dela."

    mc normal "Preciso fazer a [g] parar de me jogar contra a irmã."

    mc serio "E tenho que tomar muito cuidado em como vou lidar com ela."

    scene black with Dissolve(1.0)

    p rindo "Oi!"

    p rindo "O [mc] está certo em uma coisa. Essa [g] é perigosa."

    p "Diferente de outras personagens onde você deve conquistá-las, com a [g] é o contrário."

    p lecionando "Quero dizer, ela que que vai tentar te seduzir. Se você aceitar todas as provocações dela, você vai cair na mão dela."

    if julia_seducao >= 10:

        p "Inclusive, você deu um belo amasso com ela no restaurante, e isso já aumentou e muito sua chance de ser seduzido."

    p rindo "Tomar cuidado e ter o controle da relação ou se deixar levar e ser dominado por ela, é sua escolha."

    p rindo "Não se esqueça que você pode sempre voltar e tentar caminhos diferentes caso você não goste do resultado das suas escolhas."

    p rindo "E não se esqueça de me visitar quando dormir! Xau xau!"

    if tempo < 3:

        if tempo == 1:

            scene mapa cidade with dissolve

        if tempo == 2:

            scene mapa cidade_tarde with dissolve
    else:


        scene mapa cidade_noite with dissolve

    "Então ela trabalha no período da tarde. Preciso ir no restaurante no turno dela pra gente conversar melhor."

    "Será que é uma boa eu ir lá agora?"

    menu:
        "Ir até o Tadaima falar com a [g]":


            "Acho que é uma boa falar com ela de uma vez."

            "Ela é a irmã da [s] e se eu me aproximar dela vai ser melhor."

            if julia_seducao >= 4:

                mc safado "E depois do que a gente fez lá no restaurante..."

                "Quem sabe não pode rolar mais safadezas com ela?"

            "Vou esperar até ficar de tarde e dou um pulo lá."

            scene black with Dissolve(1.0)

            $ tempo = 2

            jump cenario_tadaima
        "Deixar para outra hora":


            mc zerado "Nah... melhor eu falar com ela outra hora."

            "Tenho coisas mais importantes para resolver agora."

    if estou_na_cidade:

        jump call_cidade
    else:


        return

label julia_cel_msg3_evento:

    "Então a [s] mostrou a roupa pra [g]. Elas são realmente bem próximas."

    if sayuri_e3 == "beijo":

        "E o beijo realmente mexeu com a [s]. Que bonitinha."

        "Não posso negar que mexeu comigo também."

        "A [s] é tão fechada que até uma coisinha tão simples vira um grande evento."

    "Só que..."

    mc surpreso "Ela tá me chamando pra ir na casa delas!"

    "Será que essa é uma boa ideia?"

    "Eu ficaria sozinho com a [g]... Com certeza seria uma excelente chance de acontecer alguma coisa."

    "Mas e a [s]? Isso seria certo?"

    "Vou pensar um pouco nisso tudo e respondo ela depois..."

    jump call_cidade



label julia_evento1:

    g "Que legal!"

    g "Vou alugar você por um tempinho, tudo bem?"

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você não pode ser completamente seduzido pela Júlia. Ou seja, não precisa escolher SÓ SACANAGEM!"

        p "Se você tiver a cabeça no lugar, no momento certo, CONVERSE com ela. Entendeu a dica? Mas... você vai resistir?"

        p rindo "E aí? Você vai preferir a pauta ou viver mais sacanagem? Aqui, você decide! Boa sorte!"

    menu:
        "Tudo bem.":


            $ tempo += 1

            mc normal "Claro. Eu vim aqui pra passar um tempo contigo."

            show garconete bemvindo with dissolve

            python:
                renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
                renpy.save("j1_save", extra_info="j1_save")

            $ iconchefe += 1
            $ estou_na_cidade = False

            g "Toda garota gosta de receber atenção. Ponto pra você."

            mc normal "Sério?"

            mc charmoso "E quantos pontos eu tenho até agora?"

            if julia_seducao >= 6:

                g "Você tem bastante..."

                mc charmoso "E eu posso trocar meus pontos?"

                g "Claro que pode. Você quer um pedaço de mim?"

                mc safado "Quero tudo."

                g "Hmm..."
            else:


                g "Alguns... Mas ainda é pouco."

                mc charmoso "Vou tentar ganhar mais então."

                g "Não precisa de muitos. Você sabe que eu tô facinho..."
        "Agora não posso. Volto outro dia.":


            mc normal "Desculpa, [g]. Eu tô correndo hoje. Pode ser outro dia?"

            show garconete perguntando with dissolve

            g "Ahh... Que droga! Mas tudo bem."

            g "Quando der vem me ver."

            mc "Ok. Até depois."

            jump cenario_tadaima

    g "Espera só um instantinho que meu turno tá acabando."

    mc normal "Ok..."

    scene black with Dissolve(2.0)

    "{b}Meia hora depois{/b}"

    mc zerado "Esse 'instantinho' dela..."

    "{b}Mais meia hora depois{/b}"

    scene tadaima restaurante with dissolve

    show garconete provocando with dissolve

    g "Ufa! Mais um dia de trabalho..."

    g "Eu acho que estudantes não deviam ter que trabalhar. Ainda mais as gatas que nem eu..."

    mc zerado "Seu 'instantinho', hein..."

    show garconete perguntando with dissolve

    g "Para de ser cuckeira, [mc]!"

    mc zerado "Cuckera?"

    g "Deixa pra lá. Você vai ter que esperar mais um pouquinho... Vou tomar um banho e me trocar."

    mc triste "Quê?!"

    mc bravo "..."

    menu:
        "Não quero mais esperar. Quero ir com você.":


            $ julia_seducao += 1

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e1_trocada","amizade","julia")

            mc charmoso "Não vou mais esperar. Vou com você lá."

            show garconete charmosa with dissolve

            g "Quê?"

            mc charmoso "Você ouviu."

            g "Hmmm..."

            g "Ok. Mas só se você prometer não me olhar enquanto eu tô me trocando."

            mc safado "Eu prometo."

            show garconete provocando with dissolve

            g "Essa sua cara não tá me passando confiança..."

            mc tarado "..."

            g "Piorou..."

            mc envergonhado "..."

            g "Tudo bem... Vamos lá numa sala vip vazia."

            mc safado "Vamos."
        "Tudo bem. Vou te esperar aqui.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e1_esperar","amizade","julia")

            if julia_seducao > 0:

                $ julia_seducao -= 1

            $ renpy.notify("Você resistiu à sedução de Júlia...")

            mc normal "Tudo bem. Eu prometi que ia passar um tempo com você. Vou esperar."

            show garconete charmosa with dissolve

            g "Ounnn... Você é muito bacana, [mc]."

            g "Você não vai se arrepender."

            g "Eu te prometo!"

            hide garconete with dissolve

            "..."

            "Essa [g] é uma garota sem rodeios. Ela vai direto no ponto."

            "Ela parece bem resolvida com a forma que ela lida com a sexualidade."

            "Por um lado, ela parece pronta pra transar comigo quando eu quiser. Só que parece que ela sempre tá planejando alguma coisa."

            "Preciso tomar muito cuidado em como vou lidar com ela."

            "..."

            scene black with Dissolve(2.0)

            "..."

            "{b}Mais 15 minutos depois...{/b}"

            "..."

            scene tadaima restaurante with Dissolve(1.0)

            g "Olá! Estou de volta!"

            show garconete e_provocando with dissolve

            mc surpreso "Uou!"

            g "Gostou? Tô muito gata, não tô?"

            mc normal "Você tá linda."

            g "Só linda?"

            menu:
                "Tá maravilhosa.":


                    mc normal "Você tá maravilhosa."

                    g "Hmm... Acho que isso vai servir."

                    mc desconfiado "Como assim?"

                    g "Ser bonita não é suficiente. Eu quero ser sexy, gostosa."

                    mc normal "Você é tudo isso também."

                    g "Agora você só tá querendo que eu me sinta bem."

                    mc "Claro que não. Você é realmente sexy."

                    g "Tá. Ok..."
                "Tá muito gostosa.":


                    $ julia_seducao += 1

                    mc tarado "Tá muito gostosa, isso sim."

                    g "Agora sim."

                    g "Linda não é o suficiente pra mim. Eu quero que você queira me morder."

                    mc safado "E eu quero..."

                    g "Quem sabe mais tarde?"

                    mc "Vou estar esperando."

            jump julia_e1_continuar

    scene tadaima porta with dissolve

    show garconete perguntando with dissolve

    g "Pode entrar e me esperar lá dentro."

    mc normal "Certo. Não vai demorar tanto."

    g "Uma garota precisa do tempo que for necessário pra ficar linda. Desencana."

    mc serio "..."

    g "Já volto."

    hide garconete with dissolve

    "Bom... Agora que eu aceitei passar um tempo com ela não adianta reclamar."





    scene tadaima local with dissolve

    "A sala que eu saí com a [s] era igualzinha essa. Parece que eles têm várias salas para os clientes VIPs..."

    "Esse lugar é realmente pra gente de dinheiro. Sorte minha que a gente acabou não comendo nada aquele dia."

    "Se bem que a [g] é irmã dela... Talvez a gente fosse comer de graça!"

    mc zerado "Eu devia ter me esbaldado..."

    "..."

    "..."

    "E agora ela tá tomando banho."

    if julia_seducao >= 6:

        "Com certeza ela vai voltar toda cheirosa..."

        "O que eu não daria pra..."

        mc serio "Calma, [mc]!"

        "Não posso perder a cabeça."

        mc tarado "Ou será que eu posso?"

    "Espero que ela volte logo."

    "..."

    "..."

    "{i}TUMP TUMP{/i}"

    mc desconfiado "Tem alguém correndo..."



    scene j1_new1 with hpunch

    mc surpreso "!"

    g "Ufa! Acho que ninguém me viu..."

    "Ela tá de toalha!"

    g "Toda vez é isso..."

    mc desconfiado "Pera... Você anda de toalha no lugar em que você trabalha todo dia?"

    g "Sim. Eu tenho que tomar banho e me trocar aqui antes de sair..."

    mc concentrando "Estou tentando imaginar isso..."

    g "Tarado..."

    mc surpreso "Não! Não nesse sentido!"

    mc zerado "Como você ainda não foi despedida?"

    g "Você se preocupa demais com as coisas..."

    "..."

    g "Não acredito que deixei você ficar aqui enquanto eu me troco."

    menu:
        "Não se preocupe. Eu vou ficar de costas.":


            mc normal "Não se preocupe. Eu não vou olhar. Vou ficar de costas, ok?"

            g "Ok..."
        "Eu sei que te excita eu tá aqui.":


            $ julia_seducao += 1

            mc tarado "Eu sei que no fundo você fica excitada de saber que eu tô aqui e você pelada."

            g "Tá bom. Não vou mentir. Eu fico mesmo."

    g "Então pode ir pra porta e olha pra lá."

    mc "Certo."

    scene tadaima salinha with Dissolve(1.0)

    g "Não tá olhando?"

    mc "Pronto. Não tô vendo nada."

    g "Vou tirar minha toalha..."

    "..."

    g "Tô tirando agora..."

    "..."

    g "Já tô peladinha..."

    "Ela tá me provocando de propósito!"

    g "..."

    "..."

    "E agora?"

    if julia_seducao < 15:

        "Eu cumpro minha promessa?"

        menu:
            "Quero que ela confie em mim. Tenho que cumprir.":


                if julia_seducao > 0:

                    $ julia_seducao -= 1

                $ renpy.notify("Você resistiu à sedução de Júlia...")

                "Não posso parecer um babaca. Preciso me controlar."

                jump julia_e1_trocada
            "Só uma olhadinha. Ela nem vai notar...":


                "Só uma olhadinha... Ela nem vai saber..."
            "Ela vai gostar se eu olhar.":


                $ julia_seducao += 1

                "Quem eu quero enganar? Ela vai adorar se eu olhar ela."
    else:


        "Eu não consigo resistir. Eu preciso ver ela pelada. Não consigo me controlar!"

    "Vamos lá..."





    scene j1_new2 with Dissolve(1.0)

    pause

    mc surpreso "!"

    "Meu Deus! Olha pra essa bunda!"

    "Essa mina é muito gostosa!"

    "..."

    if julia_seducao < 15:

        menu:
            "Só mais um pouquinho...":


                $ julia_viutrocando = True

                "Não posso parar agora. Não consigo tirar os olhos dela."
            "Já vi demais. Melhor parar...":


                "Já me aproveitei demais dela."

                "Melhor voltar..."

                scene tadaima salinha with slideright

                jump julia_e1_trocada
    else:


        $ julia_viutrocando = True

        "Não consigo parar de olhar. Preciso continuar olhando..."

    "..."





    scene j1_new3 with Dissolve(1.0)

    pause

    g "E aí?"

    g "Gostou do show?"

    mc tarado "Claro..."

    g "Tô aprovada?"

    menu:
        "Aprovada com louvor.":


            mc safado "Aprovada com louvor."

            g "Eu sabia que você ia gostar. Principalmente do material aqui em baixo."

            mc "Você pensou certinho..."

            g "Tenho certeza que você daria tudo pra poder apertar minha bunda agora..."

            mc "..."

            g "Quem sabe outro dia. Agora pode virando que o show acabou."

            mc "..."
        "Preciso ver melhor pra ter certeza.":


            $ julia_seducao += 1

            mc safado "Não tenho certeza. Preciso ver melhor..."

            g "Você é insaciável?"

            mc "Vai mostrar ou não?"

            g "Tá bom. Só pra você."



            scene j1_new4 with Dissolve(1.0)

            pause

            g "E agora?"

            mc tarado "Você é perfeita..."

            g "Quer sentir também?"

            mc "Com certeza."

            g "Quem sabe outro dia. Agora pode virando que o show acabou."

            mc "..."

    scene tadaima salinha with slideright

    label julia_e1_trocada:

        "..."

        "..."

        g "Pronto?"

        mc desconfiado "Pra quê?"

        g "Pra ver a universitária mais deliciosa que existe!"

        mc charmoso "..."

        mc "Será que é mesmo?"

        g "Pode ter certeza que sim."

        mc "Ok. Tô virando."

        scene tadaima vip with slideleft

        show garconete e_provocando with Dissolve(1.0)

        g "Sou ou não sou?"

        mc charmoso "Com certeza."

        g "Eu sabia que você ia babar pra mim."

        mc charmoso "..."

        g "Vamos lá pra frente."

        mc normal "Ok."

        "..."

        scene tadaima restaurante with Dissolve(1.0)

        "..."

    label julia_e1_continuar:

        mc normal "E agora?"

        show garconete e_provocando with dissolve

        g "Podemos ir."

        mc desconfiado "Onde a gente vai?"

        g "Olha pra minha roupa. A gente vai pra faculdade."

        mc triste "Por que eu iria pra lá? Eu já acabei a faculdade ano passado..."

        g "Você vai me acompanhar! E se quiser pode fingir que é meu peguete."

        mc zerado "..."

        mc "Certeza que é isso que quer fazer? Ir pra faculdade não parece o melhor dos encontros."

        g "Primeira coisa. Você acha que ter um corpo como esse é fácil?"

        if julia_viutrocando:

            g "Você deu uma boa olhada nele. Você sabe que eu sou uma delícia."

        g "Segundamente. Eu trabalho de tarde e estudo de noite."

        g "Não tenho tempo pra nada, rapaz."

        mc desculpa "Não deve ser fácil..."

        g "Não quero saber de compaixão. Só quero que você vá comigo."

        mc normal "Ok. Você venceu."

        g "Agora sim você falou igual um homem."

        g "Vamos lá?"

        mc normal "Vamos."

        "..."

        $ tempo += 1
        $ julia_e1 = "amizade"





    show mapa cidade_noite with Dissolve(2.0)

    "Eu não sei o que pensar sobre a [g]."

    "Ela é uma garota bem direta. Deu em cima de mim aquele dia e não perde uma chance de tentar me seduzir."

    "As intenções dela parecem bem claras. Mas e se ela só estiver tentando me colocar contra a [s] de novo?"

    "O que eu devo fazer?"

    menu:
        "Não tenho certeza do que eu quero ainda...":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e1_naosei","amizade","julia")

            if julia_seducao > 0:

                $ julia_seducao -= 1

            "Não tenho certeza ainda se eu devo ir até o fim com ela."

            "Tem a [s] e eu não sei se ela tá armando alguma pra cima de mim."

            "Essa menina é perigosa demais pra ser levada na brincadeira."
        "Eu quero ir até o fim com ela. Tenho certeza.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e1_ateofim","seducao","julia")

            $ julia_seducao += 1

            "Não importa se ela tá tramando alguma coisa. Eu quero chegar até o fim com ela."

            mc safado "Ela é gata e esse jeito peralta dela..."

            "Só quero poder experimentar essa menina..."

    scene cidade angulo_1_noite with Dissolve(2.0)

    mc normal "A cidade é muito bacana durante a noite."

    g normal "Desde quando você virou romântico?"

    mc envergonhado "Só tô puxando assunto..."

    g emburrada "Você não precisa falar nada se não tiver nada pra falar."

    mc "Tudo bem..."

    "..."

    mc desculpa "Você tá atrasada pra faculdade?"

    g normal "Hm? Não. A gente tem uns 45 minutos até minha aula começar."

    mc normal "Beleza. Então ainda dá pra gente enrolar um pouco."

    g "Sim. Por quê?"

    mc normal "O que acha da gente sentar no parque um pouco?"

    g "Você realmente tá estranho..."

    mc zerado "Para de me encher."

    scene parque banco_noite with Dissolve(2.0)

    mc normal "Aqui tá legal."



    g "Você tá ficando velho e precisa descansar as pernas?"

    mc zerado "..."

    mc normal "Só queria trocar uma ideia."

    g "Já falei que a gente não precisa disso, [mc]. Nossa relação é puramente física."

    mc "Certo. Mas eu queria saber um pouco sobre você."



    scene j1_new5 with Dissolve(1.0)

    g "Sinceramente, não sei se quero conversar."

    mc "Você normalmente fala pouco e é bem direta. Quero saber mais sobre você."

    g "Quer a real? Você tá perdendo todo o charme assim."

    menu:
        "Ok. Você venceu. Sem conversa então. Vamos continuar.":


            $ julia_seducao += 1

            mc zerado "Ok, chorona. Sem conversa então."



            g "Agora eu gostei. Menos papo e mais ação."

            g "Inclusive..."
        "Não me importo. Quero conhecer você melhor.":


            if julia_seducao > 0:

                $ julia_seducao -= 1

            mc charmoso "Não tô nem aí. Vamos conversar."

            g "Seu chato..."

            g "Hmm..."

            g "Pensando bem..."

    g "Vem aqui no banco comigo rapidinho..."

    mc desconfiado "...? Pensei que você não quise..."



    scene j1_new6 with hpunch

    mc "U-uou!"

    g "O que você acha de em vez da gente falar a gente se beijar?"

    g "Muito melhor, hein?"

    "..."

    "Essa garota realmente sabe o que quer..."

    "E é uma proposta bem tentadora..."

    if julia_seducao < 15:

        menu:
            "Muito melhor mesmo. Vem aqui.":


                $ julia_seducao += 1

                mc "Muito melhor mesmo."

                jump julia_e1_beijo
            "Quem sabe depois? Agora eu só quero conversar.":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("julia_e1_conversou","conversou","julia")

                $ julia_conversou = True

                mc "Você é incrível. Você sabe disso. Mas agora eu só quero conversar."

                g "Você realmente não vai mudar de ideia, né?"

                mc "Não."





                g "Ok... O que você quer saber?"

                mc normal "Nada de mais. Me fala um pouco sobre você. Quantos anos você tem? Onde você mora? O que você quiser."

                g "Hmmm... Isso parece conversa de um tarado querendo me assassinar."

                mc envergonhado "Que exageiro..."

                g "Tudo bem. Se você realmente quer saber essas coisas."

                g "Eu acabei de fazer 18 anos. Tô no primeiro ano da faculdade e moro lá na cidade."

                mc normal "Puxa. Em cinco segundos eu descobri mais coisa sobre você do que todo o resto das nossas conversas."

                g "Mas o que você prefere? Saber esse tipo de coisa ou me beijar? Ou ver minha bunda?"

                mc "Cada coisa na sua hora."

                g "Tá. Agora me fala alguma coisa de você."

                mc charmoso "Então você também quer saber sobre mim."



                scene black with dissolve

                scene j1_new5 with Dissolve(1.0)

                g "Cala a boca..."

                mc normal "Tudo bem. Meu nome é [mcc]..."

                g "Isso eu sei."

                mc normal "Eu me formei na mesma faculdade que você. Foi no ano passado."

                g "Uhum..."

                mc "Não vou falar minha idade. E eu moro naquele prédio logo ali."

                g "Por que não vai falar a idade?"

                mc "Talvez um dia eu fale."

                g "..."

                g "Então você mora ali?"

                mc "Sim. No nono andar."

                g "Dá pra ver a ilha toda de lá?"

                mc "Mais ou menos. Eu consigo ver o parque, e até um pouco do bar. Mas esses prédios ficam bem no meio da minha vista da praia."

                g "Que saco."

                mc "Pois é."

                mc desculpa "..."

                mc serio "Você parece gostar muito da [s]..."



                g "Com certeza! A [s] é a melhor pessoa do mundo. Eu amo ela."

                if sayuri_e2 == "amizade":

                    g "Você se deu bem naquele encontrinho de vocês. Mas eu não vou deixar você roubar ela de mim."

                    mc charmoso "Eu não quero roubar ela de você. É só dividir."

                    g "Hmmmm..."

                    mc zerado "E como assim roubar ela de você?"

                    g "..."
                else:


                    g "Por isso que eu não deixei você se dar bem com ela naquele encontrinho."

                    mc zerado "Então era realmente tudo um plano seu?"

                    g "Assim, começou como um plano. Mas eu realmente gostei do seu beijo."

                    mc envergonhado "..."

                g "Ela foi muito importante pra mim..."



                g "É que as pessoas estavam me tratando muito mal. Meus pais não gostam muito de mim."

                mc triste "..."

                g "E ela sempre conversou comigo. Ela me entende. Ela sabe que eu não sou uma idiota."

                mc desculpa "Você não parece uma idiota."

                g "Você só fala isso porque quer me comer..."

                mc zerado "Você que queria me beijar e eu neguei, lembra?"



                g "Verdade... Isso é estranho. Então por que tá sendo legal comigo?"

                mc desculpa "Eu preciso ter uma razão pra ser legal com você?"

                g "Claro. Por que você faria isso se não fosse por algum motivo?"

                mc envergonhado "Talvez porque eu queira ou porque eu ache que você mereça... Sei lá."

                g "[mc], você é engraçado."

                mc desconfiado "Huh? Por quê?"

                g "Sei lá também! Só sei que você é."

                mc zerado "..."

                "..."

                scene j1_new6 with vpunch

                g "Hmm... Agora que a gente conversou. O que acha daquele beijo?"

                mc "Hmm..."

                menu:
                    "Agora acho que você merece.":


                        mc "Agora sim. Podemos ir pro beijo."

                        g "Finalmente a hora que eu tava esperando..."

                        jump julia_e1_beijo
                    "Você vai se atrasar pra faculdade.":


                        if julia_seducao >= 0:

                            $ julia_seducao -= 1

                        mc desculpa "Você vai se atrasar pra faculdade."

                        jump julia_e1_beijo_depois
    else:


        label pixie_julia_15pontos:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_15pontos","seduzido","julia")

            "Não consigo negar ela. Não consigo me controlar. Essa garota mexe comigo demais."

            "Preciso dessa boca agora."

            scene black with Dissolve(1.0)

            p rindo "Oi! Desculpe acabar com o clima, mas eu queria te dar um aviso importante."

            p lecionando "Nesse ponto o [mc] já não consegue mais se controlar. Tudo que a [g] quiser ele vai fazer. Em outras palavras, ele foi seduzido."

            p "Você não verá mais escolhas e sempre vai só fazer o que ela te mandar, mesmo que isso vá prejudicar a vida do [mc]."

            p "Se você não liga pra isso, não tem problema nenhum."

            p "Mas se você quiser estar no controle da situação, você precisa negar as investidas dela no futuro ou voltar o encontro e pegar mais leve."

            p "Inclusive, ela está te conquistando desde quando você saiu com a [s] no outro dia. Talvez você queira pegar leve lá também."

            p "A cada investida sexual dela que você aceita, mais difícil vai ser para você se controlar no futuro. Tome cuidado!"

            p "Agora pode continuar! Xau xau!"

        scene j1_new6 with Dissolve(1.0)

        "A [g] é gostosa demais! Eu quero beijar ela e comer ela de qualquer jeito."

        mc "Você mexe comigo demais."

        g "Eu sei..."

        jump julia_e1_beijo

    label julia_e1_beijo:

        mc "Você realmente sabe como conseguir o que quer, hein?"

        g "É muito fácil quando se é uma delícia que nem eu..."

        mc "Mas deixa comigo agora..."

        "Ela vai ver quem está no controle."

        g "Quê?!"

        scene j1_new7 with Dissolve(1.0)

        pause

        g "Ai... Desde quando você é assim, hein? Todo mandão?"

        mc "Agora vem aqui."

        g "Hmmm..."

        mc "Não era isso que você queria, danada?"

        g "Era..."

        g "E você tá fazendo direitinho... com essa boca, essa língua... ah..."

        if julia_seducao >= 9:

            g "Só continua. Você tá me deixando molhada."

            mc charmoso "Quê?"

            g "Eu quero mais. Quero seu corpo, sua perna..."

            g "Quero sentir aqui, no meio das minhas pernas."

            mc surpreso "..."

            mc envergonhado "Aqui? No meio do parque? E se alguém..."

            g "Cala a boca e pega em mim. Tá no parque só me dá mais tesão."

            g "Certeza que aquele cara tá olhando pra gente e querendo tá no seu lugar."

            mc "Exibicionista..."

            if julia_seducao < 15:

                menu:
                    "Esse beijo já foi o suficiente por hoje.":


                        if julia_seducao >= 0:

                            $ julia_seducao -= 1

                        mc normal "Eu adorei nosso beijo. É mais do que suficiente pro nosso primeiro encontro."

                        g "Você vai mesmo me obrigar a dar pra alguém da faculdade?"

                        mc envergonhado "Vai ser o jeito."

                        g "Você é mais difícil do que eu esperava, sabia?"

                        mc charmoso "Que bom que você acha isso. Fica um pouco do mistério."

                        g "Hmph.."

                        jump julia_e1_beijo_depois
                    "Com certeza.":


                        $ julia_seducao += 1

                        mc tarado "Como eu vou negar algo pra uma delícia dessas?"
            else:


                "Se eu não tivesse com tanto tesão..."

                "Mas não tenho como negar um pedido desses. Só quero pegar ela AGORA."

            $ julia_e1 = "seducao"

            $ julia_seducao_evento += 1

            mc safado "Claro que eu pego..."

            g "Isso... Só faz o que eu falo..."

            scene j1_new8 with Dissolve(1.0)

            g "Assim..."

            g "Isso. Um pouco pro lado..."

            "{i}shruk shruk{/i}"

            mc safado "O que você tá fazendo?"

            g "Hmm... tirando a calcinha..."

            "Caralho... o tesão dessa menina é impossível."

            "Não acredito que essa novinha delícia vai esfregar a bucetinha tarada dela em mim..."

            g "Assim... isso... consegui..."

            scene j1_global1 with Dissolve(1.0)

            pause

            g "Olha aqui."

            mc "Caralho... você tirou mesmo..."

            g "Sim... agora coloca na boca pra você sentir como eu tava molhada..."

            menu:
                "Põe aqui.":


                    mc "Hmmm... que melzinho mais gostoso..."

                    g "Docinho direto da minha xerequinha perfeita."
                "Cala a boca e se esfrega.":


                    g "Mandão..."

            g "{i}puf puf{/i}"

            g "Ai... assim... queria esfregar no seu pau..."

            mc "Eu ainda vou meter gostoso em você."
            scene jnew_ani10 with Dissolve(1.0)
            g "Assim... isso... fala besteira que eu tô cada vez mais excitada."

            g "{i}puf puf{/i}"

            g "Ain... Bem aí!"

            mc "Esfrega, safada. Toma o que você quer."

            g "Ahh! Isso!"

            g "Nnghhhh...."

            g "Porra..."

            mc "Meu pau tá até doendo no jeans. Olha como você deixou ele."

            g "Aahh... é o que eu... aahnn... faço de melhor... hmmmnnn..."





            scene black with dissolve

            scene j1_new6 with Dissolve(1.0)

            g "Hmm... Que gostoso..."



            mc surpreso "Opa!"

            g "Agora eu tô por cima de novo..."

            mc envergonhado "..."

            g "Eu tô ensopada. Não esperava menos de você."

            mc safado "Que bom que você gostou. Mas e eu? Olha como você me deixou."

            g "Você? Ixi... Não tenho tempo agora. Você vai ter que se virar sozinho."

            mc tarado "Ei! Isso não é justo."

            g "Mas vai ser o jeito."

            g "Prometo te recompensar outro dia."

            mc envergonhado "Safada... você me paga."
        else:


            "Eu sinto que se eu tivesse aceitado mais as provocações dela, dava pra pegar mais fogo ainda..."

            "Se bem que é até demais pra primeira vez que a gente se fala..."

    label julia_e1_beijo_depois:

        scene parque banco_noite with Dissolve(1.0)

    "..."

    g "Olha a hora. Precisamos correr pra faculdade. Se pá até perdemos o busão já."

    if carro:

        mc "Não esquenta que te dou uma carona."

        g "UAU! Tu é o fodão, hein?"

        mc "Bonito, gostoso e fodão."

        play sound som_carro

        scene black with dissolve

        pause
    else:


        mc serio "Vamos correr então!"

        scene black with Dissolve(1.0)

        "..."

        scene cidade onibus_noite with Dissolve(1.0)

        mc concentrando "Ufa... acho que conseguimos."

        g "Ufa..."

        mc surpreso "Não! Pera! Olha o busão ali!"

        g emburrada "Ei! Para aí!"

        mc bravo "Motorista! Olha a gente!"

        g emburrada "Ei seu puto! Para!"

        "..."

        scene black with Dissolve(1.0)

        play sound "audio/som_14_onibus.mp3"

        $ renpy.pause(delay=5, hard=True)

        "..."

        g normal "Conseguimos..."

        mc normal "Obrigado por parar."

        "Motorista" "Só sentem logo."

        mc triste "Ok..."

        g emburrada "Para de ser idiotão."

        "Motorista" "..."

        "..."

    g normal "Chegamos!"

    stop sound

    scene universidade fachada with Dissolve(2.0)

    mc zerado "Eu sei. Estudei aqui também..."

    g "Hehe!"

    show garconete e_provocando with dissolve

    g "Valeu por ter vindo comigo."

    mc normal "De boa. Eu queria passar um tempo com você."

    if julia_conversou:

        mc "Gostei de saber um pouco sobre você."

        g "Hmmm... Sei lá."

        mc "Não gosta de falar sobre você, né?"

        g "Não muito."

        mc desculpa "É porque sempre que você falou de você as pessoas te viram como idiota, né?"

        show garconete e_emburrada with dissolve

        g "Pode parar de me analisar..."

        mc desculpa "Desculpa..."

        g "Tô te zuando."

        show garconete e_resignada with dissolve

        g "Acho que você tem razão."

        g "Não sou aquele tipo de mulher que fica chorando. Mas minha vida não foi a mais fácil."

        mc normal "Espero que um dia eu possa saber mais sobre você."

        g "Quem sabe... Se você continuar sendo estranho desse jeito."

        mc zerado "..."

        show garconete e_provocando with dissolve

        g "Mas espero que você queira um pouquinho de ação também."

        mc charmoso "Quem sabe..."

        "..."

        g "Hmm..."

        g "Tenho um presente pra você. E dessa vez não é uma foto da [s]."

        g "É um segredo sobre a [s]."

        mc desconfiado "Quê?!"

        g "Pois é. Eu sei que seu trabalho é publicar sobre as celebridades."

        g "E... Depois de hoje... Eu não quero que você seja despedido. Então quero te passar um segredo sobre a [s]."



        "Uma pauta?! Não acredito! Eu não vou ser demitido!"

        "Só que... eu vou invadir a privacidade da Sayuri assim mesmo? E agora? E se for uma armadilha da [g]?"

        menu:
            "Ok! Manda. Preciso dessa pauta.":


                $ pautas += 1
                $ sayuri_p2 = True

                mc desconfiado "Ok... espero não me arrepender."

                g "Eu sei que sua revista gosta de coisa envolvendo sexo, relacionamento e etc."

                g "A [s] é uma pessoa, assim, muito escondida. Ela não fala dela mesma. Ninguém sabe nada sobre ela."

                g "Você pode não acreditar, mas a [s] é virgem. E ela nunca teve um namorado. Ela é BV na verdade."

                mc surpreso "Você tem certeza disso?!"

                show garconete e_emburrada with dissolve

                g "Claro... Ela me conta tudo. Não duvide do nosso amor, seu idiota."

                mc envergonhado "Entendi entendi. Desculpa."

                g "O que você vai fazer com isso depende de você."

                mc zerado "Pera... Sua intenção me falando isso é pra que eu me ferre com ela, né?"

                show garconete e_resignada with dissolve

                g "Nãããooo... Imagina, [mc]. Eu nunca faria isso."

                mc "Você nem tá se esforçando pra esconder sua ironia."

                g "Êta desconfiança! E pior. Nem me agradeceu ainda."

                mc desculpa "Ok. Independente dos seus objetivos por trás, obrigado pela pauta."

                g "Pelo quê?"

                mc normal "Pela pauta. Pauta é como a gente chama um assunto que pode virar notícia. Tipo algo super interessante."

                g "Chaaato.... Não sei porque eu perguntei..."
            "Eu agradeço a intenção, mas não posso fazer isso com a [s].":


                $ sayuri_amizade += 3

                "Espero que em algum momento isso me ajude com a Sayuri. Porque tô desistindo de algo muito importante..."

                mc preocupado "Obrigado [g], mas eu não posso aceitar."

                mc "Não quero invadir a privacidade da Sayuri assim. Não é ético e seria mancada com ela."

                if sayuri_e5 == "nada":

                    if sayuri_amizade > 9:

                        mc feliz "Ainda mais agora que parece que nosso encontro no Tadaima foi legal."
                    else:


                        mc desculpa "Ainda mais que parece que nosso encontro lá no Tadaima não foi dos melhores."

                mc desculpa "Eu sei que {b}vou estar correndo risco de perder meu emprego caso não tenha nenhuma outra pauta para o chefe{/b}."

                mc bravo "Mas eu prefiro perder meu emprego do que ferir os sentimentos da Sayuri."

                if sayuri_atencao > 0:

                    show garconete e_emburrada with d

                    g "Outra vez?"

                    mc desculpa "É, dessa vez eu quero fazer diferente!"

                show garconete e_sexy with d

                g "Hmmm... Você até parece um homem de verdade falando desse jeito."

                mc zerado "Fã ou hater?"

                g "Haha... bobo."



    mc normal "Mas eu gostei muito da nossa noite."

    if julia_viutrocando:

        g "Tenho certeza que você adorou o showzinho que eu fiz pra você lá no Tadaima."

        mc safado "Com certeza."

    if julia_e1 == "seducao":

        show garconete e_provocando with dissolve

        g "E o servicinho que você prestou pra mim na praça."

        g "Hmmmm... Que delícia."

        mc tarado "Que bom que você gostou."

        g "Eu vou te recompensar mais tarde, ok? Fica de olho no celular."

        mc "Com certeza."

    g "Eu gostei de tudo. Vamos fazer isso de novo, ok?"

    mc normal "Vamos sim."

    g "Agora vou lá. Beijo no pinto!"

    mc zerado "..."

    hide garconete with dissolve

    "Essa menina..."

    "Só de sair com ela eu me sinto mais jovem."

    mc triste "Agora vou ter que pegar o busão até a ilha."

    "..."





    scene black with Dissolve(1.0)

    "..."

    scene cidade angulo_1_noite with Dissolve(1.0)

    "Hoje foi um dia corrido. A [g] é uma garota estranha, mas muito divertida."

    "Com certeza ela teve problemas que deixaram ela assim. Parece que ela tem medo de falar sobre ela e de se conectar com as pessoas."

    if julia_conversou:

        "Ela procura relações fáceis e superficiais. Eu sinto que é por causa de um medo do que os outros vão pensar dela."

        "Se for verdade, até os pais... Isso deve ser horrível pra qualquer criança."
    else:


        "Mas eu podia ter descoberto mais coisas sobre ela se naquela hora do parque eu tivesse insistido pra sentar e conversar."

        "Foi uma chance perdida."

    if julia_viutrocando:

        "Aquele lance no Tadaima foi demais. Ela é muito sexy e ainda acabou se exibindo pra mim."

        "Como eu queria poder pegar nela inteira naquela hora."
    else:


        "Eu podia ter visto ela se trocando no Tadaima. Mas eu resolvi não forçar a barra."

        mc incomodado "Será que eu tô arrependido?"

    if julia_e1 == "seducao":

        "Minha sorte foi que no parque eu fui com tudo pra cima dela."

        "Aquele beijo, e depois que eu pude pegar nela. Ela tava louca de tesão."

        mc safado "E eu também."

        "Espero que ela me pague por essa de alguma forma incrível."
    else:


        "Eu não fui até o fim com ela no parque. As coisas poderiam ter ficado ainda mais loucas."

        "Mas será que eu deveria? Acho que eu segui o caminho que eu queria."

    if julia_seducao >= 15:

        "O problema é que agora eu não consigo negar nada que ela me fala."

        "É como se ela tivesse me enfeitiçado."

        "Isso pode ser terrível pra mim dependendo do que ela me pedir. Preciso tentar retomar o controle da situação."
    else:


        "Estou conseguindo manter as coisas sob controle."

        "Não é como se eu fosse fazer qualquer coisa que ela me pede em troca de sexo."

        "Eu preciso tomar cuidado pra não ser seduzido por ela e virar um escravo."

    $ julia_cel_msg2 = True

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    mc normal "Opa."

    mc "A [g] mandou alguma coisa."

    mc zerado "Ela não devia tá na aula agora?"

    show screen celular_julia

    "..."

    if julia_e1 == "seducao":

        mc safado "Caraca... Essa mina não tem jeito mesmo."

        "Não vejo a hora de pegar ela de jeito."

    if julia_conversou:

        "E essa selfie vendo a palestra?"

        "Ela sabe ser fofa quando quer também."

    "Eu podia fazer uma visita pra ela no Tadaima de vez em quando. Ela trabalha durante a tarde."

    "Mas acho que agora vou direto pra cama."

    $ v5_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v5_fim","v5","terminou")



    scene black with dissolve

    scene universidade fachada with Dissolve(1.0)

    label j1_premium1:

        pass

    menu:
        "O que a [g] faz na faculdade?":








            "O que será que essa doida faz quente desse jeito durante a aula? Dá nem pra imaginar..."

            "???" "Ei, putinha! Tô aqui!"

            g "Ei! Fala, putão!"

            scene black with dissolve

            scene j1_new9 with Dissolve(1.0)



            "???" "Achei que você não ia vir."

            g "Tava preocupado que eu ia reprovar... de novo?"

            "???" "Até parece... eu achei que ia ficar sem minha boneca. Eu tô meio tarado hoje."

            g "Eu também..."

            "???" "Você tá sempre tarada. Não é à toa que seu apelido é putinha."

            g "Só você me chama assim."

            "???" "É que nem todo mundo passou a mão em você ainda. Mas espera mais um pouquinho."

            g "Cala a boca."

            "???" "E por que você atrasou?"

            g "Tava de rolo com um cara aí."

            "???" "Haha! Não duvido. Mas você lembra que a gente tá namorando, né?"

            g "Tô brincando. Eu sei. A gente combinou que ia tentar não se trair dessa vez."

            "???" "Quero ver se você consegue."

            g "Claro que eu consigo."

            "???" "Haha... tá bom... com essa buceta flamejante aí?"

            g "Se você der conta de mim, não preciso procurar em outro lugar."

            "???" "Acho que nem uns 3 paus duros 24 horas por dia dá conta de você."

            g "A culpa não é minha se eu adoro..."

            "???" "Então tá. Essa conversa me deixou duro. E aí? Rola?"

            g "No meio da aula?"

            "???" "Só tira sua saia. Só pra eu dar uma olhadinha na perigosa."

            g "Hmm... mas e se alguém olhar?"

            "???" "E você não prefere assim?"

            g "Afe... verdade..."

            "???" "Vai logo. Arranca logo isso."

            menu:
                "Tá bom. Só a saia.":


                    g "Tá bom... só uma olhadinha."

                    scene black with dissolve

                    scene j1_new10 with Dissolve(1.0)

                    pause

                    "???" "Eu vou olhar quanto eu quiser. Ela é minha mesmo."

                    g "Safado..."

                    g "Era isso que você queria?"

                    "???" "Tô vendo nada."

                    g "Ela é transparente, idiota. Dá pra ver tudo."

                    "???" "Não tem graça assim. Quero ver melhor."

                    g "Quer que eu arranque tudo? Vai todo mundo ver sua namorada pelada."

                    "???" "Você acha que eu ligo? Eles podem olhar, mas só eu te como."

                    g "Que seja... o que eu faço agora então? Tiro a calcinha?"

                    "???" "Não. Espera. Eu quero que você comece tirando a parte de cima."

                    g "Tá louco?! O professor vai ver!"

                    "???" "Só você abaixar aqui, tonta."

                    g "Afe... você é muito tarado."

                    "???" "Vai logo. Você é minha namorada. Você serve pra isso."

                    g "Tá bom..."

                    "???" "Vem aqui. Aqui no chão ninguém vai ver."

                    scene black with dissolve

                    "???" "Isso... coloca aqui em baixo."

                    scene j1_new11 with Dissolve(1.0)

                    pause

                    g "Assim?"

                    "???" "Que delícia."

                    g "Você gosta?"

                    "???" "Quando tá assim até que dá pro gasto."

                    g "Você nunca reclamou."

                    "???" "Se você faz seu trabalho eu não reclamo mesmo."

                    g "Meu trabalho é tirar a roupa?"

                    "???" "Seu trabalho é fazer eu gozar. Tirar a roupa é uma parte."

                    g "Hmm..."

                    "???" "Mas vamos combinar, você nasceu pra isso, Ju."

                    g "Nasci?"

                    "???" "Você fica muito melhor igual uma puta sem roupa. Todo mundo prefere você assim."

                    g "Sei..."

                    "???" "Você gosta de chamar atenção. E obedecendo a gente é fácil. Só você continuar assim."

                    g "Você quer que eu seja uma boa garota. É isso?"

                    "???" "Você é uma péssima garota. E a gente gosta de você assim, uma garota suja."

                    g "Haha... seu puto..."

                    "???" "Agora ajoelha."

                    g "Tá louco? Eles vão me ver."

                    "???" "Eu quero ver você de quatro. É minha posição preferida."

                    g "Só qu-"

                    "???" "Cala a boca. Só abaixa a cabeça, porra."

                    g "Hm."

                    scene j1_new12 with Dissolve(1.0)

                    "???" "Agora sim. É assim que eu gosto de ver você."

                    g "Eu não sou sua cadela."

                    "???" "É sim. Late."

                    g "Au au"

                    "???" "Que cadela gostosa. Você já tá no cio, não tá?"

                    g "Eu já tô pegando fogo."

                    "???" "Sabia."

                    "Professor" "Ei. O que a Júlia tá fazendo aí?"

                    g "!"

                    "???" "Ela tá procurando uma coisa."

                    "Professor" "Por favor... vocês já estão reprovados. Tentem não atrapalhar a recuperação."

                    "???" "Nunca, fessôr."

                    g "Procurando uma coisa, é?"

                    "???" "É. Meu pau."

                    g "E cadê ele?"

                    scene j1_new13 with Dissolve(1.0)

                    "???" "Tá aqui."

                    g "Hmm... achei..."

                    "???" "É sua recompensa por ser uma cadelinha obediente."

                    g "Arf arf..."

                    "???" "Essa cachorra não aguenta vê um pau que já quer colocar na boca."

                    g "Eu quero."

                    "???" "Você gosta tanto assim de caralho?"

                    g "Gosto. Eu amo. Eu sei como deixar meu namorado feliz."
                    scene jnew_ani11 with Dissolve(1.0)
                    "???" "Você vai deixar seu namorado muito feliz assim mesmo."

                    "???" "Você é meio burra, lerdinha, sem graça... mas com um caralho na boca você é a melhor."

                    g "Eu sei. Eu vou cuidar de você."

                    "???" "Se você não aguenta mais, pode engolir ele."

                    "???" "Quero ver se você chupa melhor que a Mari."

                    g "Quê?! Você ficou com ela?"

                    "???" "Haha... é brincadeira, Ju."

                    g "Não gostei."

                    "???" "Você não vai deixar seu namorado na mão agora, né? Olha como eu tô duro por sua causa."

                    g "Eu devia..."

                    "???" "Você é a melhor com pau. Agora vai logo e me chupa."

                    "Esse filho da puta deve ter ficado com a Mari mesmo com a gente prometendo que não ia transar com outros."

                    "Eu devia deixar ele na mão... só que... eu sou a melhor nisso... não posso deixar ele achar que eu piorei."

                    menu:
                        "Chupar ele":


                            g "Só porque eu sou sua namorada. Porque você não merece."

                            "???" "Tá bom, tá bom. Agora usa sua boca pra uma coisa útil. Mama logo."

                            scene j1_new14 with Dissolve(1.0)

                            pause

                            "???" "Ah... que boca molhadinha... sua boca foi feita pra chupar pau."

                            g "Hmm..."

                            "???" "Isso aí, chupa rola. Chupa a rola do seu macho."

                            g "Ah... que rola boa."

                            "???" "Não fala. Só mama. Você fica linda, chupando."

                            g "Filho d-"

                            "???" "Já mandei calar a boca."

                            "???" "Ah... e faz com mais vontade. Parece que tá morrendo."

                            g "Hm!"

                            "???" "Não não... ainda é pouco."

                            "???" "Tira a mão do meu pau. Só com a boca. Bora ver se melhora."

                            g "Hm?!"

                            scene j1_new15 with vpunch

                            pause

                            "???" "Hmm! Assim!"

                            g "HHMMMG!"

                            "???" "Isso! Coloca a língua pra fora e suga! Deixa eu sentir sua garganta!"

                            "Professor" "Tudo bem aí, C-"

                            "???" "Tudo perfeito, senhor!"

                            g "!"

                            "???" "Vô goza, puta. Engole tudo!"

                            g "HMMM!"

                            "???" "Toma, cadela!!!"
                            scene jnew_ani12 with Dissolve(1.0)
                            "Professor" "Agora chega! O que foi isso?!"

                            "???" "Fica de boa professor... acabou... a [g] achou o que tava procurando."

                            "Professor" "Olha, jovem..."

                            "???" "Qualquer coisa fala com a Júlia, professor. Ela que tá aqui embaixo fazendo o que não devia."

                            "???" "E meu pai é o maior doador da faculdade. É como se vocês trabalhassem pra mim, então não enche."

                            "Professor" "Fedelho..."

                            "???" "Agora chega, Ju. Eu já gozei. Se arruma aí."

                            g "Mas e eu?"

                            "???" "Quando chegar em casa você enfia alguma coisa aí dentro haha..."

                            g "Desgraçado..."

                            scene black with dissolve
                        "Deixar ele na mão":


                            g "A gente tinha um combinado. Agora você vai ficar na mão."

                            "???" "Você tá louca?! Chupa logo, sua puta! Você é minha namorada! É sua obrigação!"

                            g "Você é um coitado. Vai passar a noite se masturbando."

                            scene black with dissolve

                            g "Falou."

                            "???" "Você não manda nada, vagabunda!"

                            "???" "Tá cheia de mina querendo meu pau!"

                            g "Corno..."

                            "???" "Filha da puta!"
                "Cansei da aula. Tô saindo.":


                    g "Quer saber? Cansei disso aqui. Tô saindo fora."

                    "???" "Quê?! Você vai aguentar isso comigo, folgada."

                    g "Foda-se você e essa faculdade."

                    "???" "É uma vagabunda mesmo."

                    g "Cala a boca, otário."

                    scene black with Dissolve(1.0)
        "Eu não quero saber.":


            "Deixa pra lá."

    scene black with dissolve

    call call_cidade from _call_call_cidade

label julia_evento2:

    "Tenho que ver o que fazer com o convite da [g]..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j2_save", extra_info="j2_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "O que a [s] iria pensar se eu fosse na casa dela? Eu vou estar sozinho com a [g]."

    if sayuri_e3 == "beijo":

        "Ainda mais depois que eu e a [s] nos beijamos."

    if sayuri_intencao == "namoro" and not sayuri_e3 == "beijo":

        "Mesmo a gente não tendo se beijado, eu decidi que iria tentar ter ela como minha namorada."

        "Talvez eu perca pontos com ela se ela descobrir."

        "Droga... E agora?"

    if sayuri_intencao == "namoro":

        "Ela não parece ser o tipo de garota que iria aceitar uma relação aberta."

        "Ainda mais dividindo o namorado com a irmã..."

        mc triste "Isso não parece nada bom..."

        "Se bem que eu não sei se ela vai descobrir. Acho que depende mais de como eu vou lidar com isso."

        if julia_seducao >= 15:

            "Além do mais eu não consigo dizer não pra [g]. Todo esse pensamento não serve pra nada."

        elif julia_conversou:

            "Eu e a [g] conversamos um bocado lá no parque aquela vez que eu levei ela pra faculdade."

            "Eu acho que ela tem algo dentro dela que ninguém teve acesso ainda. E eu quero desvendar esse mistério."

        elif julia_e1 == "seducao":

            mc safado "E depois daquele nosso lance no parque eu quero muito poder ver ela de novo."

            mc "Só de pensar que a gente vai estar sozinhos..."

    if sayuri_intencao == "amizade":

        "Bom... Não é como se a gente tivesse comprometidos ou algo assim também."

        "Eu decidi que quero ela como uma amiga."

        "Então não tem porque ela ficar triste comigo ou se sentir traída."

        "Eu posso ter um lance com a [g] e mesmo assim estar lá pra ela quando ela precisar."

        "Não tem nada que me impeça nesse sentido."

        "Ufa... Já estou me sentindo melhor."

    "..."

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    "Deixa eu avisar a [g] que eu quero ver a premiação com ela."

    "Smartphone" "Tuu... Tuuu..."

    g "[mc]?"

    show mc telefone with dissolve

    mc "Isso!"

    g "Você é tão velho assim?"

    mc "Quê?"

    g "Ninguém mais usa celular pra ligar hoje em dia. Você tem zap pra quê?"

    mc "Me deixa..."

    mc "Só queria te avisar que eu tô afim de ver a premiação da [s] com você hoje à noite."

    g "Sério?!"

    mc "Sim."

    menu:
        "Estou louco pra ficar sozinho com você.":


            if julia_seducao < 15:
                $ julia_seducao += 1
                if julia_seducao >= 15:
                    $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
            else:
                $ julia_seducao += 1

            mc "Estou louco pra gente ficar sozinho."

            g "Você quer me pegar de qualquer jeito, né?"

            mc "Não vejo a hora..."

            g "Vai pensando no que você vai fazer comigo hoje à noite."

            mc "..."
        "Acho que vai ser uma boa oportunidade da gente se conhecer melhor.":


            if julia_seducao >= 15:
                $ julia_seducao -= 1
                if julia_seducao < 15:
                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
            else:
                $ julia_seducao -= 1

            mc "Essa pode ser uma boa oportunidade da gente conversar e se conhecer."

            g "[mc]... você sabe que eu não gosto de conversar..."

            mc "Não perguntei."

            g "Mas vai ter outras coisas também, né?"

            mc "Se você se comportar, vamos ver..."

            g "Agora você tá me provocando."

        "Mas é só pra assistir a premiação da [s]." if julia_seducao < 15:

            if julia_seducao >= 15:
                $ julia_seducao -= 2
                if julia_seducao < 15:
                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
            else:
                $ julia_seducao -= 2

            mc "Eu topo, mas é pra gente assistir o evento da [s] e só."

            mc "Não quero que fique achando que vão ter outras coisas."

            g "Vamos ver quando você chegar aqui."

            mc "[g]..."

            g "Ok ok... Calma..."

    mc "Então hoje a noite eu passo aí, ok? Você pode me passar o endereço?"

    g "Certo. É Alameda Shigure, número 313."

    mc "Ok. Combinado. Até lá."

    g "Tchau, gostoso."

    "..."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)





    "Não tenho nada urgente pra hoje. Vou enrolar um pouco até dar a hora."

    "..."

    "Ainda não consegui desencanar da [s]."

    "Será que a [g] contou pra ela?"

    "Talvez eu devesse ligar pra ela... Deixa eu pensar um pouco."

    "Nessa altura do campeonato eu tenho certeza que a [g] quer me afastar da [s]."

    "Por outro lado, parece que ela se interessou em mim. Se puder, com certeza vai unir o útil ao agradável."

    mc zerado "Eu tenho certeza que a [g] não tá nem aí pros meus sentimentos."

    "Esse convite dela é uma armação pra eu perder pontos com a [s]? Ou será que ela realmente só quer companhia pra assistir o evento?"

    "Sei lá... Impossível prever o que aquela menina pensa."

    "..."

    "E de minha parte? Será que eu devo avisar a [s]? Seria o mais honesto a fazer?"

    "Ou será que o melhor pra nossa relação é tentar fazer isso sem ela descobrir?"

    "Parece bobeira, mas eu sinto que essa escolha vai influenciar se a [s] vai confiar mais ou menos em mim."

    "E agora?"

    menu:
        "Avisar a [s] que eu vou ver o evento com a [g]":


            $ j2_sayuri_avisou = True

            "Melhor eu avisar ela. É mais honesto."

            if casa:

                scene ap sala with Dissolve(1.0)
            else:


                scene apartamento geral with Dissolve(1.0)

            show mc telefone with dissolve

            "Smartphone" "Tuuu... Tuuu..."

            s "Alô?"

            mc "Oi, [s]! Tudo bem?"

            if sayuri_e3 == "beijo":

                s "Be-be-be... quer dizer! [mc]!"

                mc "Tudo legal?"

                s "S-s-s-sim!"

            s "Tá tudo legal, sim."

            mc "Que bom."

            mc "Tudo pronto para o evento hoje?"

            s "Si-sim."

            if not sayuri_e3 == "horrivel":

                s "Muito obrigada pela ajuda no outro dia..."

                mc "Com a roupa você diz?"

                s "Isso. Se não fosse por você não teria conseguido."

                mc "Não esquente. Foi bacana aquele dia."

            s "Ainda estou um pouco nervosa com tudo isso. Mas acho que vou conseguir."

            mc "Fico muito feliz."

            mc "Olha... A [g] me chamou pra ir na sua casa hoje à noite assistir o evento."

            s "Sério?!"

            mc "Daí queria te avisar..."

            s "[mc]..."

            s "Eu..."

            if sayuri_intencao == "namoro":

                s "Por favor, tome muito cuidado com a [g]."

                s "Eu amo ela... ela é muito querida. Mas ela é meio doidinha."

                s "Depois que a gente... {size=10}não consigo falar...{/size} eu queria que você tomasse mais cuidado."

                "A [s] parece conhecer a irmã muito bem..."

                "Ela deve estar com um pouco de ciúmes depois que eu disse pra ela que não queria ser só um amigo."

                if sayuri_e3 == "beijo":

                    "Ainda mais depois que a gente se beijou..."

                "Minha próxima resposta vai ser muito importante."

                menu:
                    "...":


                        mc "..."

                        s "Tudo bem?"

                        mc "Eu tô legal. Só queria te avisar mesmo, ok?"

                        s "Ok..."
                    "É apenas pra assistir seu evento. Não quero nada com ela.":


                        $ sayuri_amizade += 3

                        mc "Não se preocupe. A gente vai só assistir você recebendo o prêmio."

                        mc "Eu sei como a [g] é. Só quero me aproximar mais dela porque ela é sua irmã."

                        mc "Não tenho nenhuma outra intenção."

                        s "Nã-não é o que você tá pensando!"

                        mc "Tem certeza?"

                        s "E-eu... Aii, [mc]..."

                        mc "Não precisa morrer de vergonha!"

                        s "O-ok..."
            else:


                $ sayuri_amizade += 3

                mc "Eu quero ser seu amigo. E por isso conhecer sua irmã faz parte!"

                s "Ah! O-obrigada por fazer isso. Eu sei que a [g] não é fácil, e você está fazendo isso por mim."

                s "Muito obrigada."

                if julia_e1 == "seducao":

                    "Se ela soubesse que a gente já se pegou e eu tô muito afim de pegar ela de novo hoje..."

                    "Tadinha da [s]. Mas não posso revelar isso pra ela ainda."

                    mc "Cla-claro! Conhecer ela ao máximo! É o mínimo que eu posso fazer."
                else:


                    "Claro. É o mínimo que eu posso fazer."

            s "Então está certo. Eu vou demorar lá no evento, você provavelmente não vai estar mais em casa."

            mc "Verdade..."

            s "Então tá. Não pegaria bem você dormir lá sozinho com ela... I-isso... papa-pareceria..."

            mc "Haha! Não esquente!"

            mc "Então boa preparação e uma ótima premiação! Você merece!"

            s "Obrigada de novo por tudo. Tchau."

            mc "Até."

            hide mc with dissolve
        "Não avisar ela dos planos desta noite":


            "Acredito que o melhor é não fazer uma tempestade em copo d'água. Não tenho porque causar."

            "Vou ir lá, assistir o evento e sair de fininho antes da [s] chegar."

            "Daí é só torcer pra [g] não causar comigo e ficar quieta. Vou ter que confiar nela..."

            if sayuri_intencao == "namoro":

                "Se a [s] chegar e me encontrar lá sozinho na casa dela com a irmã vai ser terrível."

                mc triste "Tenho que me preparar para o pior."

                "Preciso ter isso em mente e fazer tudo certo."

                "Ainda mais depois que eu disse pra ela que {b}queria ser mais do que só um amigo{/b}."

                "Pelo que eu conheço a peça, a [s] deve estar muito nervosa com isso que eu disse. Não posso ser um cuzão agora."
            else:


                "Se bem que eu disse pra [s] que queria ser apenas um amigo."

                "Não deveria importar muito se eu tiver uma relação com a irmã dela."

                mc desconfiado "Certo?"

                "Mas e se ela se sentir traída por eu me envolver com a [g]? Ela já foi traída várias vezes antes pelo que eu entendi."

                "Eu não quero ser outro a machucar o coração dela."

                mc safado "Mas a [g] é tão..."

    "Bom. Com isso resolvido agora é só assistir alguma coisa."

    "{b}Algum tempo depois{/b}"

    $ tempo = 3

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    "Acho que deu a hora. Melhor pegar o busão e ir pro centro da cidade. De lá ainda tenho que pegar um Uber."

    scene black with Dissolve(1.0)

    play sound "audio/som_14_onibus.mp3"

    $ renpy.pause(delay=5, hard=True)

    "..."

    mc "Opa. Tô indo pra Alameda Shigure. O número... é 313."

    "Motorista" "Beleza. Tá aqui no app."

    mc "Valeu."

    "..."





    mc normal "O número tá certo. Tem que ser aqui."

    play sound "audio/som_15_campainha.mp3"

    "{i}Ding Dong{/i}"

    "..."

    g "Oi, [mc]! Entra!"

    mc "Opa. Licença."

    $ julia_e2 = "iniciou"

    scene sayuri_casa geral with Dissolve(3.0)

    mc "Muito bonita."

    show garconete e_provocando with dissolve

    g "Obrigada."

    mc zerado "Eu tava falando da casa."

    menu:
        "Sua casa é maravilhosa.":


            if julia_seducao >= 15:
                $ julia_seducao -= 1
                if julia_seducao < 15:
                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
            else:
                $ julia_seducao -= 1

            mc surpreso "Sua casa é realmente incrível!"

            mc normal "Esse tom oriental é muito massa."

            show garconete e_emburrada with dissolve

            g "Obrigada... eu acho."

            mc "Que foi?"

            g "Nada..."
        "Você não é bonita, você é uma delícia.":


            if julia_seducao < 15:
                $ julia_seducao += 1
                if julia_seducao >= 15:
                    $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
            else:
                $ julia_seducao += 1

            mc tarado "Você não é bonita. Você é uma delícia."

            g "Eu sei."

            g "Mas eu gosto de ouvir mesmo assim."

            mc safado "..."
        "Você é linda também.":


            mc charmoso "Mas você é linda também."

            g "Só linda?"

            mc "E divertida."

            g "Me pegou..."

    g "Eu acabei de chegar da facul."

    g "Vou colocar uma roupa de ficar em casa e já volto. Sinta-se em casa."

    hide garconete with dissolve

    mc "A gente tá sozinhos?"

    g "{size=15}Sim. A [s] já foi pro evento e meus pais estão viajando, eu acho...{/size}"

    "Eu acho? Ela nem tem certeza onde os pais estão?"

    "Essa casa tem a cara da [s]. Esses detalhes e pinturas orientais."

    play sound "audio/som_16_chuveiro.mp3"

    "{i}sssshhhhh....{/i}"

    "Que barulho é esse?"

    "Parece o som do chuveiro..."

    mc surpreso "A [g] tá tomando banho!"

    "Opa. Que mania que eu tenho de ficar gritando."

    "Será que eu tento dar uma espiada nela?"



    "Mas, também, invadir a casa dela assim... não é coisa que um cara decente faria."

    "Se eu quero que a [g] me veja como algo mais que um pedaço de carne, tenho que pensar bem..."

    menu:
        "Espiar ela no banho.":


            if julia_seducao < 15:
                $ julia_seducao += 1
                if julia_seducao >= 15:
                    $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
            else:
                $ julia_seducao += 1

                "Eu não consigo resistir à sedução dela. Eu preciso tentar ver ela nua de qualquer jeito."

            "Ok... Talvez eu consiga ver alguma coisa se eu tomar cuidado."

            "..."

            scene sayuri_casa banheiro_porta with Dissolve(3.0)

            play sound "audio/som_16_chuveiro.mp3"

            "Ela deixou a porta um tanto aberta..."

            "Por isso que consegui ouvir o chuveiro lá da sala."

            "Chegou a hora da verdade. E agora?"

            menu:
                "Não tem mais volta. Vou olhar.":


                    $ j2_espiou = True

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("j2_tomando_banho","julia","personagem")

                    "Não posso voltar atrás agora. Preciso dar só uma espiadinha..."

                    "..."



                    scene black with dissolve

                    scene j2_new1 with Dissolve(1.0)

                    pause

                    "Uou!"





                    mc safado "..."

                    "Ela tá logo ali... nunca que ela ia pensar que eu ia vir aqui..."

                    "O problema é que não dá pra ver nada! Mas... se eu..."

                    "É... se eu conseguisse chegar um pouquinho mais perto..."










                    "É muito arriscado. Se ela me pegar aqui eu tô ferrado."

                    menu:
                        "Melhor sair enquanto ainda posso":


                            if julia_seducao >= 15:
                                $ julia_seducao -= 1
                                if julia_seducao < 15:
                                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                            else:
                                $ julia_seducao -= 1

                            "Não. Já vi tudo o que queria ver. Preciso sair daqui antes que ela me veja."

                            scene black with dissolve

                            scene sayuri_casa banheiro_porta with Dissolve(1.0)

                            "Não quero que ela ache que eu tô necessitado desse jeito."

                            "..."

                            jump j2_banho_depois
                        "Abrir a porta com a mão e se aproximar andando devagar":


                            "Vou tentar ir bem devagar, sem fazer movimentos bruscos..."

                            jump j2_banho_perto
                        "Agachar e se aproximar empurrando a porta com a cabeça":


                            "Melhor eu ir agachado. É meio estranho, mas acho que vai chamar menos atenção..."

                            label j2_banho_perto:

                                "Entrar devagar e tomar cuidado com o piso que pode tá molhado{nw}"

                                $ renpy.vibrate(1)

                                scene j2_new2 with vpunch

                                pause

                                "AIEE!"





                                g "[mc]!!"

                                mc surpreso "UARGH!!"







                                g "Não acredito... O que você tá fazendo aí no chão?"

                                mc "N-n-n-não... é..."

                                g "Tudo isso é vontade de me ver peladinha?"

                                mc "..."

                                g "Você sabe que eu sou facinho. Não precisa dessas coisas... Olha aqui."







                                scene j2_new3 with Dissolve(1.0)

                                pause

                                mc surpreso "A-ah!"

                                g "Que foi? Nunca viu uma mina pelada antes?"

                                g "Espera... você já me viu pelada."

                                mc envergonhado "E-eu?"

                                g "Achei que era você... talvez não seja mesmo..."

                                g "Mas agora você viu o que você queria ver. E nem precisava ter se esborrachado no chão."
                                scene jnew_ani26 with Dissolve(1.0)
                                mc "Desculpa..."

                                g "Tudo bem. No fundo todos os homens têm tipo 15 anos quando se trata de sacanagem."

                                mc desculpa "Não quero que pense que sou um tarado."

                                g "Impossível não pensar depois dessa, né?"

                                mc "..."

                                g "A não ser que você queira ver melhor..."

                                menu:
                                    "E-eu vi o suficiente.":


                                        mc "S-sim. Q-quero dizer. E-eu vi o suficiente!"

                                        g "Foi o que eu pensei."
                                    "Hmm...":


                                        mc "Bom..."

                                        scene j2_new4 with Dissolve(1.0)

                                        "Se ela tá oferecendo... poder olhar pra essa belezura..."

                                        g "Cuidado secar demais."

                                        mc "Você quem deixou... agora deixa eu ver."
                                        scene jnew_ani14 with Dissolve(1.0)
                                        g "Como é mimado... mas tá bom... quando terminar me avisa."

                                        "Caralho... essa mina é impossível..."

                                        mc "Acho que tá bom."

                                        g "Sempre que você quiser é só pedir. Meu corpo tá aqui pra você."

                                        mc "Gostosa..."

                                        scene j2_new3 with Dissolve(1.0)

                                g "Agora vai lá pra sala e me espera quietinho que eu vou secar o cabelo e colocar uma roupa."

                                mc "Ok. T-tô indo."

                                scene black with dissolve

                                scene sayuri_casa banheiro_porta with Dissolve(1.0)

                                g "{size=15}Ei! Eu sabia que você ia vir. Bobinho.{/size}"

                                "Droga. Parece que ela me tem na mão dela. Eu sou muito idiota mesmo."

                                "Tenho que parar de pensar com o pinto de vez em quando."

                                jump j2_banho_depois
                "Preciso ser forte e resistir!":


                    if julia_seducao >= 15:
                        $ julia_seducao -= 2
                        if julia_seducao < 15:
                            $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                    else:
                        $ julia_seducao -= 2

                    "Preciso me controlar! Não é isso que eu quero com ela. Não sou um cachorro no cio."

                    "Mas... mas... Ela peladinha..."

                    "Chega de pensar nisso!"

                    "..."

                    "Consegui..."

                    jump j2_banho_depois

        "Ficar na sala e esperar ela voltar." if julia_seducao < 15:

            if julia_seducao >= 15:
                $ julia_seducao -= 2
                if julia_seducao < 15:
                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
            else:
                $ julia_seducao -= 2

                "Ufa... Isso vai me ajudar a não cair no controle dela..."

            "Não! Não posso ceder às tentações."

            "Não é assim que eu quero que ela se lembre de mim."

            "E ainda tem a [s]. Eu preciso ser forte e me controlar."

            "A [g] não perde uma chance de me seduzir. Ela não dá ponto sem nó. Eu preciso tomar muito cuidado com as minhas escolhas."

            jump j2_banho_depois

    label j2_banho_depois:

        scene sayuri_casa geral with Dissolve(1.0)

        "..."

        "Ela já deve tá terminando."

        "..."

        mc zerado "Por que ela demora tanto pra se arrumar?"

        "..."

        show julia provocando with dissolve

        g "Heya!"

        mc surpreso "..."

        g "Que foi? Nunca viu uma mina tão gata na sua frente?"

        menu:
            "Você é a mina mais gostosa que eu conheço.":


                mc safado "Sem dúvidas você é a mina mais gostosa que eu conheço."

                if julia_seducao < 15:
                    $ julia_seducao += 1
                    if julia_seducao >= 15:
                        $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                else:
                    $ julia_seducao += 1

                g "Você sabe como deixar uma garota com vontade de dar."

                mc "..."
            "Certeza que você vai usar essa roupa comigo aqui?":


                if julia_seducao >= 15:
                    $ julia_seducao -= 1
                    if julia_seducao < 15:
                        $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                else:
                    $ julia_seducao -= 1

                mc desconfiado "Certeza que você vai ficar de boa com essa roupa eu estando aqui?"

                g "Claro. O que você vai fazer? Ficar olhando? Grande coisa..."

                mc normal "Você é fogo mesmo..."
            "Tá se achando demais, não tá?":


                mc feliz "Tá se achando muito pro seu tamanho."

                show julia brava with dissolve

                g "Ei! Não era isso que era pra você responder!"

                mc normal "Eu sei... Por isso respondi..."

                g "Grrr..."

                g "Falando assim parece que você nem quer me pegar."

        show julia peralta with dissolve

        if julia_seducao >= 9:

            g "Você sabe que eu sempre tô facinho pra você."

            if julia_conversou:

                mc charmoso "Eu sei. Mas será que isso é tudo?"

                g "Como assim?"

                mc "Lembra da nossa conversa na praça? Você falou de você pela primeira vez lá."

                g "Nem me lembre daquilo..."

                mc "Por quê?"

                g "Não gosto de falar sobre essas coisas..."

                mc normal "Ok. Por hora você tá livre."
            else:


                mc safado "Eu sei. E eu adoro isso."

        g "O que você tá pensando em fazer comigo hoje?"

        menu:

            "Comer você, é claro." if julia_seducao >= 9:

                mc tarado "Comer você, obviamente."

                if julia_seducao < 15:
                    $ julia_seducao += 1
                    if julia_seducao >= 15:
                        $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                else:
                    $ julia_seducao += 1

                g "Você tá sendo direto demais."

                mc "Algum problema com isso?"

                g "Nenhum..."
            "Assistir a premiação da [s] e trocar uma ideia.":


                if julia_seducao >= 15:
                    $ julia_seducao -= 1
                    if julia_seducao < 15:
                        $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                else:
                    $ julia_seducao -= 1

                mc normal "Assistir a [s] e a gente podia conversar um pouco também."

                show julia brava with dissolve

                g "Conversar?"

                mc charmoso "Sim."

                g "Mas só isso?"

                mc "Por hora, só."

                g "Você acha que é pra isso que eu te chamei aqui, [mc]?"

                mc "Foi o que você me disse."

                g "Não se faça de tonto!"

                mc "..."
            "Eu consigo pensar em um monte de coisas.":


                mc charmoso "Eu consigo pensar em um bocado de coisas."

                g "Eu também consigo..."

                g "E todas elas são muito divertidas."

                mc "Vamos ver se a gente tá pensando na mesma coisa..."

        g "Daqui a pouco vai começar a apresentação. Vamos se ajeitar."

        mc normal "Bora."

        scene sayuri_casa tv with Dissolve(3.0)

        g "Vai passar na TV aberta, acredita?"

        mc surpreso "Sério?!"

        show julia radical with dissolve

        g "A mana é importante! Tá brincando?"

        mc normal "Você gosta do fato dela ser famosa?"

        g "Claro que sim!"

        g "A mana é simplesmente incrível. Ela é a principal esportista do país e mesmo assim não tem o nariz empinado."

        mc "Isso é verdade. A [s] continua sendo muito humilde."

        g "Sim! E ela sempre dá autógrafos e nunca fica brava quando criticam se ela não ganha alguma coisa."

        g "A minha irmã é a pessoa mais incrível que eu conheço!"

        mc "... Mas..."

        g "{i}Ssshh!{/i} Agora vai começar! Cala a boca!"

        hide julia with dissolve

        "Apresentador" "A Décima Segunda Premiação do Esportistas do Ano está para começar!"

        "Apresentador" "E quem fará a abertura do nosso evento é nada mais, nada menos que nossa principal atleta!"

        "Apresentador" "[sc]!"

        mc surpreso "É a [s]!"

        g "{i}Ssshh!{/i} Eu falei que ela é a melhor!"

        mc desconfiado "Precisa fazer..."

        g "{i}Sssshhh!{/i}"

        mc zerado "..."

        s "Boa noite."

        g "Ela tá falando!"

        s "O esporte quebra a barreira da competição e do entretenimento. O esporte é o motor da mudança física, social e espiritual."

        s "O esporte é saúde, é mudança de vida, é o desejo de se tornar uma pessoa melhor e atingir a distância."

        s "Investir no esporte não é investir em medalhas, mas sim em um povo aguerrido e com maior esperança."

        "{b}Alguns minutos depois{/b}"

        s "E que o esporte seja nossa única arma na busca por uma vida melhor!"

        s "Obrigada."

        "{i}Clap clap clap clap{/i}"

        g "Como ela é linda..."

        mc normal "Você realmente tem muita admiração por ela."

        show julia brava with dissolve

        g "Claro. Quem não teria?"

        mc charmoso "Chega a ser uma fascinação."

        g "O que você quer dizer com isso?"

        mc normal "Não é nada. Eu só queria entender melhor isso."

        g "Lá vem você de novo querendo conversar..."

        if julia_conversou:

            g "Já não bastou todo aquele papo na praça?"

            mc charmoso "Claro que não. Aquilo foi só o começo."

        g "Grrr..."

        mc charmoso "Eu sei que você não gosta de falar sobre sua vida, mas eu realmente quero saber mais sobre você."

        g "Então vou avisar agora! Se você continuar com esse papo não vou deixar você me beijar hoje!"

        mc charmoso "Ei!"

        g "É sério!"

        menu:

            "Eu não quero nada desse tipo com você." if julia_seducao < 9:

                if julia_seducao > 3:

                    $ julia_seducao -= 1

                $ sayuri_amizade += 2

                mc charmoso "Pode me ameaçar. Eu não quero nada desse tipo de coisa com você."

                g "Ei! Mas eu quero!"

                mc charmoso "..."

                g "Não me olhe desse jeito! Se eu quiser te beijar você tem que querer também!"

                mc "Você não tem nenhum controle sobre mim. Pode chorar o quanto quiser."

                g "Grrr..."
            "Eu sei que você não vai negar um amasso.":


                "Será que ela negaria um amasso? Pelo que eu conheço a [g] ela não iria negar uma farrinha."

                mc charmoso "Eu sei que você não consegue negar um amasso."

                g "Grrr..."

                g "Se eu tiver que fazer isso, eu consigo, sim!"

                g "{size=10}Eu acho...{/size}"

                mc "O que você disse aí?"

                g "Não interessa!"
            "Calma. Não precisa me ameaçar!":


                if julia_seducao < 15:
                    $ julia_seducao += 1
                    if julia_seducao >= 15:
                        $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                else:
                    $ renpy.notify("Você continua seduzido pela Júlia e não pode ver algumas escolhas")
                    $ julia_seducao += 1

                mc incomodado "Calma. Não precisa ameaçar."

                mc charmoso "Você sabe que eu tô aqui pra isso."

                g "Acho bom!"

        g "Agora deixa eu assistir mais um pouquinho..."

        hide julia with dissolve

        "Eu não sei se eu quero ser só mais um objeto sexual na coleção da [g]."

        if julia_seducao >= 15:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e2_dominado","julia","personagem")

            "Só que eu estou completamente dominado por ela."

            "Eu entrei demais no jogo dela e agora não consigo negar se tiver algo sexual envolvido."

            "É como se ela me tivesse na mão dela sempre que me oferece qualquer recompensa sexual."

            "Talvez eu deva só parar de me preocupar e ir com tudo. Foda-se se for só sexo."

            "Só que..."
        else:


            "Graças a Deus eu ainda tenho o controle da situação. Eu estou resistindo à sedução dela."

            if julia_seducao < 9:

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("julia_e2_gelado","julia","personagem")

                "Inclusive as coisas nem estão tão quentes entre a gente."

                "Se continuar assim eu acho que não vai rolar nada esta noite."

                "Se eu quiser algo com ela, preciso ser mais sedutor e aceitar mais as provocações dela."
            else:


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("julia_e2_perfeito","julia","personagem")

                "Mesmo assim o clima entre a gente tá quente."

                "Esse é o ponto ideal pra nossa relação. As coisas estão quentes, mas eu não fui dominado."

                "Se eu conseguir manter as coisas assim eu sinto que posso ir longe com ela."

        "Se nossa relação for apenas sexo, será que ela não vai enjoar de mim?"

        "Todos os namoradinhos dela devem estar comendo na mão dela. Se eu for só mais um, talvez ela só desista da gente."

        if sayuri_intencao == "namoro":

            "Também não posso esquecer que eu falei pra [s] que quero ser algo mais que amigo."

            "Não posso brincar com os sentimentos dela."

            "Mas se ela não descobrir..."

        "Minha próxima escolha vai ser {b}MUITO importante{/b} para definir como minha relação com a [g] vai continuar."

        "E agora?"

        mc serio "[g]..."

        g "Que foi?"

        menu:
            "Não posso obrigar você a falar se você não quer, mas...":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("j2_mesmacoisa_5pontos","julia","personagem")

                mc charmoso "Eu não posso te forçar a falar sobre você."

                g "Obrigada."

                mc "Mas eu realmente gostaria muito que você falasse."

                show julia brava with dissolve

                g "[mc]! Não é assim!"

                g "É pra você dizer que não quer! Senão vai parecer que sou eu que não quero falar."

                mc "Você não tá falando coisa com coisa."

                g "Grrr..."
            "Vamos esquecer a conversa e ficar só na ação mesmo.":




                mc tarado "Você tem toda razão. Vamos esquecer a conversa e focar no prazer."

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("j2_aumentou_5pontos","julia","personagem")

                if julia_seducao < 15:
                    $ julia_seducao += 5
                    if julia_seducao >= 15:
                        $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                else:
                    $ renpy.notify("Você está ainda mais dominado pela Júlia")
                    $ julia_seducao += 5

                g "Agora sim você falou minha língua, mano! E você vai adorar minha língua..."

                mc safado "..."

                g "..."

                g "Não quero que você ache que eu tenho algo terrível pra esconder de você."

                mc desconfiado "Como assim?"
            "Não quero só pegação. Quero saber mais sobre você.":


                mc serio "Eu entendo que você não gosta, mas eu não quero só pegação. Eu quero conhecer você melhor."

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("j2_diminuiu_5pontos","julia","personagem")

                if julia_seducao >= 15:
                    $ julia_seducao -= 5
                    if julia_seducao < 15:
                        $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                    else:
                        $ renpy.notify("Você reduziu o poder dela sobre você, mas continua dominado por ela")
                else:
                    if julia_seducao >= 9:
                        $ julia_seducao -= 5
                        if julia_seducao < 9:
                            $ renpy.notify("As coisas esfriaram. Se continuar assim não rolará nada físico")
                    else:
                        if julia_seducao >= 8:
                            $ julia_seducao -= 5

                show julia brava with dissolve

                g "Quê?!"

                g "Você vai mesmo querer ir por esse caminho?"

                mc charmoso "Não precisa ficar triste. Eu só quero te conhecer."

                g "Hmmm..."



    label julia_e2_conversa_pre:

        scene julia confessando_solo with Dissolve(3.0)

        pause

        g "Sabe, [mc]."

        g "Não sei por quê, mas eu fico um pouco feliz de você querer conversar comigo."

        if julia_conversou:

            g "Quando eu falei sobre mim no parque... eu até me senti bem depois."

            g "Como se tivesse mais leve."

            g "Foi um sentimento estranho ter alguém pra poder contar as coisas."

        g "Só que tudo isso é muito complicado e triste."

        g "A minha vida e da [s] não é uma história bonita, nem vai inspirar ninguém."

        g "Só vai te deixar triste e talvez afastar você da gente."

        mc preocupado "..."

        g "Eu... não quero que você se afaste da [s]. Ela tá tão mais feliz esses tempos."

        if julia_e1 == "seducao":

            g "E não posso negar que eu gostei muito da sua companhia também."

            g "Principalmente a nossa brincadeirinha no parque."

        $ renpy.notify("Júlia está exercendo a dominação dela sobre você...")

        g "Por isso, por favor, não estrague tudo querendo entrar nesse ninho de vespas."

        mc "[g]..."

        "Ela está preocupada de verdade com tudo isso."

        "E tá se controlando pra não atrapalhar minha relação com a [s]."

        "A [g] é uma garota muito especial."

        "Como eu devo lidar com isso?"

        if julia_seducao >= 15:

            $ renpy.notify("Júlia tem você sob controle. Você não pode ir contra o desejo dela")
        else:


            $ renpy.notify("Você não está dominado pela Júlia. Você tem o poder de escolher o que quer")

        "..."

        menu:

            "Eu entendo, mas não vou me afastar de você." if julia_seducao < 15:

                mc preocupado "Eu entendo sua preocupação, mas você precisa confiar em mim."

                mc "Se eu estou falando pra você me contar seu passado, é porque eu tô pronto pra ouvir."

                mc charmoso "Eu não vou me afastar nem da [s] e nem de você, [g]."

                g "[mc]..."

            "Eu quero saber mais sobre você e a [s]. Confie em mim." if julia_seducao < 15:

                mc charmoso "É minha escolha, ok? E eu escolho saber tudo sobre vocês."

                mc "Se eu estou falando pra você me contar seu passado, é porque eu tô pronto pra ouvir."

                mc charmoso "Eu não vou me afastar nem da [s] e nem de você, [g]."

                g "[mc]..."
            "Ok. Não vamos conversar sobre isso.":


                mc tarado "Você venceu. "

                jump julia_e2_game_pre

    label julia_e2_conversa:

        $ julia_e2_conversou = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("julia_e2_conversou","julia","personagem")

        scene julia confessando with Dissolve(3.0)

        g "Eu nem sei por onde eu começo..."

        mc "Por onde você quiser."

        g "Pra você entender sobre a gente, vou precisar revelar coisas sobre a [s] também. Tudo bem?"

        mc "Eu entendo."

        g "Promete que não vai usar isso pra me afastar dela?"

        mc "Claro que não, idiota. Você não confia em mim?"

        g "Entendi, calma... Confio..."

        g "Então... A [s] me contou que vocês se encontraram pela primeira vez no templo."

        mc "Isso."

        g "Não sei o que ela te disse, mas aquele templo é de uma grande organização."

        mc "Organização?"

        g "Sim. Eles são um grande grupo chefiado por um velho chinês que eu não sei o nome."

        g "Isso são tudo coisas que a [s] me contou durante os anos. Eu não sei tudo também."

        g "Mas eles têm algum rolo com o governo. E o que eles fazem é ajudar chineses que estão espalhados pelo mundo."

        g "Eles garantem que os chineses que têm algum talento especial possam contar com ajuda pra orgulhar a China."

        mc "E a [s] recebe ajuda dessas pessoas?"

        g "Sim. Mas não é fácil fazer parte desse grupo. Eles exigem várias coisas em troca."

        mc "Que coisas?"

        g "..."

        mc "..."

        g "Várias coisas. É parecido com as faculdades dos Estados Unidos que dão bolsas pros melhores alunos."

        g "Eles analisam não apenas se a pessoa é boa naquilo, mas se a família tem condições, é bem estruturada essas coisas."

        mc "Não sei se tô entendendo completamente."

        g "Quero dizer que você precisa ser top pra eles te escolherem."

        mc "Isso entendi. Não sou burro."

        g "Certeza?"

        mc "..."

        g "Bom... o que acontece é que a [s] foi reprovada."

        mc "Sério?! Mas ela é incrível."

        g "Sim. Mas a culpa não foi dela. Os chineses disseram que a família dela não era boa o suficiente."

        g "E pra provar que eles eram caridosos e esforçados, eles adotaram uma garota."

        g "Eles trataram ela perfeitamente, como uma verdadeira filha. E isso convenceu os chineses."

        g "Só que..."

        g "Depois que a [s] foi aprovada, eles não precisavam mais da garota adotada."

        mc "..."

        g "Ela foi jogada de lado e ignorada por muitos anos."

        g "Mesmo que ela tentasse de tudo pra ser a filha perfeita... nada adiantava."

        g "Não importava se ela tirava notas perfeitas, se comportasse e nunca desse problema pra ninguém."

        g "Mesmo assim os pais dela nunca deram atenção. É como se ela fosse um pedaço de lixo que não tinha mais serventia."

        g "E essa menina viveu isolada, sozinha. Ela era invisível."

        mc "[g]..."

        g "Mas um dia a [s] voltou do treino dela. Ela já tinha ganhado a primeira medalha de ouro olímpica."

        g "Ela chegou e viu a irmã adotada no quarto, sentada sozinha..."

        g "A [s] sentou do lado dela e disse que tava com saudades. Mas a irmã não respondeu."

        g "Só que [s] continuou voltando todos os dias. Até que um dia a irmã respondeu ela."

        g "E a [s] brigou com os pais porque eles não queriam que ela perdesse tempo com a adotada."

        g "Mas ela continuou dando atenção pra irmã."

        g "..."

        mc "[g]... Acho que tá bom..."

        g "Ai, [mc]... não quero chorar..."

        mc "Tudo bem. Tudo bem..."

        mc "Desculpa eu fazer você passar por tudo isso de novo."

        g "Não."

        g "..."

        scene julia confessando_solo2 with Dissolve(3.0)

        g "Eu... acho que eu gostei..."

        g "Meu peito tá apertado, mas eu sinto que tá passando..."

        mc preocupado "Que bom, [g]. Eu fico feliz."

        g "Obrigada, [mc]."

        g "Você é a primeira pessoa além da [s] que sabe sobre essas coisas."

        g "Você acha que vai continuar vendo a gente?"

        mc normal "Claro que eu vou, tonta."

        g "Legal..."

        g "Eu nunca imaginei que alguém além da [s], ainda mais um homem, teria saco pra aguentar uma história fodida dessas."

        mc preocupado "Tudo isso é muito pesado. Não consigo imaginar como você se sentiu com tudo isso."

        mc normal "Mas eu estou aqui pra você se sentir melhor. E vou estar enquanto você não se cansar de mim."

        g "Tenho que confessar que eu perco o interesse na maioria dos garotos depois de um tempo."

        g "Mas tem alguma coisa em você que é diferente."

        g "Você é meio estranho."

        mc zerado "Você já disse isso..."

        g "Hehe! Obrigada por ser estranho, [mc]."

        mc "Não sei se isso é um elogio ou o quê."

        g "Sei lá também. Só me deu vontade de falar isso."

        "..."

        g "Parece que acabou o evento. Sorte que a gente viu toda a parte da mana."

    label julia_e2_game_pre:





        scene sayuri_casa tv with Dissolve(1.0)

        g "Ah!"

        show julia radical with dissolve

        g "Tive uma super ideia!"

        g "Faz muito tempo que eu não jogo, porque meus dias estão super corridos. Mas acho que ainda sou boa."

        mc desconfiado "Do que você tá falando?"

        g "Eu te desafio para um duelo de Plantas x Zumbis!"

        mc "Plantas versus Zumbis?"

        g "Isso!"

        menu:
            "Nunca ouvi falar. O que é isso?":


                mc desconfiado "Nunca ouvi falar isso. Do que se trata?"

                g "É um jogo para PS3 que a gente pode jogar um contra o outro."

                g "Um de nós vai ser as plantas e o outro vai ser os zumbis."

                g "O objetivo dos zumbis é passar pelas plantas e comer o cérebro do dono das plantas."

                g "E as plantas precisam proteger seu dono."

                g "É isso."

                mc normal "Até que parece interessante."

                g "É muito foda!"

                g "Tem até o dois agora, só que é pra celular. Eu odeio jogo de celular."

                mc normal "Quanta ironia..."

                g "Por que ironia?"

                mc envergonhado "Nada não..."
            "Tô ligado! Sei tudo sobre esse jogo!":


                mc feliz "Tô ligado! Acho muito massa esse jogo."

                g "Que legal que você conhece. Não imaginei que você era um cara de videogame."

                mc normal "Às vezes a gente joga uma coisa ou outra."

                g "Então você sabe como o jogo funciona. Não preciso explicar."

                mc "Não."

                g "Beleza."

        g "Só que a gente vai deixar nossa partida mais interessante!"

        mc desconfiado "Mais interessante?"

        show julia peralta with dissolve

        g "Claro, né, [mc]?"

        g "Você sabe o quanto eu gosto de uma baguncinha."

        mc safado "..."

        g "Vamos fazer assim. Cada round que um de nós perdermos a gente vai ter que tirar uma peça de roupa."

        mc surpreso "Quê?!"

        g "Mas não vem com essa história de meia, brinco e coisas de criança."

        g "Perdeu o primeiro round tira a peça de cima. Perdeu o segundo tira a calça e se perder o terceiro precisa subir na mesa."

        g "E ainda vai ter que fazer a pose que o outro pedir. Pra ficar bem ridículo."

        g "Fechado?"

        mc preocupado "Espera. Deixa eu pensar."

        if julia_seducao >= 15:

            "Quem eu quero enganar? Não tem o que pensar."

            "Só de imaginar ela tirando a roupa já fico excitado."
        else:


            "Ela parece muito boa no jogo então vai ser complicado para eu ganhar."

            "E se a gente começar a tirar a roupa as coisas vão começar a esquentar."

            "Tenho que pensar bem nas consequências. Será que vale a pena entrar nessa?"

        menu:
            "Ok. Bora jogar!":


                label j2_aceitou_jogar:

                    mc charmoso "Eu aceito seu desafio. Bora jogar!"

                    g "Assim que se fala!"

            "Se recusar a jogar com ela" if julia_seducao < 15:

                "Se eu recusar jogar com ela provavelmente eu já vou pra casa e o encontro vai acabar."

                "Certeza que eu já quero finalizar a noite e voltar pra casa?"

                menu:
                    "Tenho certeza, sim. Encerrar o encontro.":


                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("j2_naoquis_jogar","julia","personagem")

                        "Melhor não correr o risco de desagradar a [s]. Vai saber onde essa noite daria."

                        "Além do mais eu conversei um bocado com a [g]. Tenho certeza que ela vai se lembrar disso."

                        "Eu posso me aproximar dela apenas como amigo."

                        mc normal "Acho que vou deixar pra próxima, [g]."

                        show julia brava with dissolve

                        g "Quêêêê?!"

                        mc "Esse negócio de tirar a roupa... Não tô muito pra isso hoje."

                        show julia peralta with dissolve

                        g "Ok... Eu entendo."

                        g "Obrigada de novo por me ouvir. Eu realmente me senti bem."

                        mc "Não esquente. Vamos conversar mais no futuro."

                        g "Combinado... Mas não só conversar, né?"

                        mc envergonhado "Veremos..."

                        scene sayuri_casa geral with Dissolve(1.0)

                        jump julia_e2_final
                    "Melhor jogar e ver onde isso vai dar.":






                        "Ainda não tô pronto pra voltar pra casa. Mesmo meio com medo de como isso vai acabar."

                        jump j2_aceitou_jogar

    scene sayuri_casa geral with Dissolve(1.0)

    g "Espera só um instantinho que vou pegar lá no quarto e instalar aqui pra gente."

    mc normal "Beleza."

    "{b}Alguns minutos depois{/b}"

    show julia provocando with dissolve

    g "Está tudo certo. Pronto pra perder e ficar peladão?"

    mc charmoso "Vamos ver quem vai perder."

    g "Você sabe como o jogo funciona, mas acho que você não tem chances de ganhar de primeira."

    g "Então se você perder, eu vou deixar você tentar quantas vezes você quiser."

    g "Se você cansar, que é o que eu acho que vai acontecer, você pode só desistir."

    mc charmoso "Acho que você tá se achando demais, isso sim."

    g "Vamos ver."

    g "Agora eu vou me concentrar. Não fala comigo enquanto eu tô jogando que eu fico puta!"

    mc triste "O-ok..."

    "..."

    scene julia jogando_concentrada with Dissolve(2.0)

    pause

    "Caraca. Ela parece bem concentrada."

    "Será que eu fiz o certo de desafiar essa guria?"

    g "Preparado?"

    g "Como você não é tão bom quanto eu, vou deixar você jogar com as Plantas, que é mais fácil."

    g "Eu vou começar atacando e daí você precisa proteger sua casa plantando o tipo de planta correta."

    g "Você vai ter que escolher como vencer minha estratégia."

    g "Velocidade e técnica é tudo nesse jogo. Não fique palermando."

    mc zerado "Palermando?"

    "Certo. Então preciso escolher qual estratégia eu vou usar de acordo com o que ela escolher."

    "Caso eu perca, só preciso ir tentando coisas diferentes. Uma hora eu consigo."

    "Isso SE eu perder. O que não vai acontecer."

    label julia_e2_game:

        $ timeout_label = "julia_e2_demorou"
        $ timeout = 5.0
        $ j2_jvenceu = 0
        $ j2_mcvenceu = 0

        scene julia jogando_concentrada with Dissolve(1.0)

        mc tarado "Se prepare pra ir tirando tudo."

        g "Desculpa acabar com a sua graça, mas é impossível você ganhar três rodadas."

        mc "Não tenha tanta certeza."

        g "Vai começar!"

        label j2_novoround:

            g "Pronto?"

            mc "Pode apostar que sim."

            $ j1dom = renpy.random.randint(1,4)

            if j1dom == 1:

                g "Vamos ver o que eu vou fazer desta vez..."

                g "Vou ir devagar com um exército de zumbis comuns!"

                "Ela está vindo com muitos {b}zumbis fracos{/b}... Como vou combater isso?"

            elif j1dom == 2:

                g "Neste round eu tenho algo especial pra você."

                g "Espero que você goste destes senhorzinhos..."

                "Ela escolheu vários {b}zumbis jornaleiros{/b}. E agora? Como eu respondo isso?"

            elif j1dom == 3:

                g "Uma nova rodada, uma nova história."

                g "Prepare-se para o maior inferno que existe neste jogo!"

                "Meu Deus! Ela tá me atacando com uma {b}avalanche de galinhas zumbis{/b}! São muitas! O que eu faço??"

            elif j1dom == 4:

                g "Neste round eu vou esquentar um pouco as coisas."

                g "Pegue ele zumbi fortão!"

                "Esse zumbi parece mais forte que os outros. Ele tá sozinho e usa equipamento de {b}futebol americano{/b}. E agora?"

            jump j2_resposta

        label j2_resposta:

            menu:
                "Plantar {b}girassóis{/b} para comprar plantas melhores depois":


                    "Já sei. Vou plantar poucas defesas e priorizar os girassóis."

                    "Vou aproveitar que eles são fracos e me defendendo planejando para o futuro."

                    if j1dom == 1:

                        "{b}Sua fraca defesa é suficiente e os girassóis te deixam mais poderoso no fim para vencer a rodada{/b}"

                        mc "Boa! Venci!"

                        g "Hmm..."

                        $ j2_juliavenceu = False
                        $ j2_mcvenceu += 1

                    elif j1dom == 2:

                        "{b}Sua fraca defesa inicial não é suficiente e os zumbis comem o cérebro do dono da casa{/b}"

                        g "Que idiota! Os jornaleiros acabaram com você!"

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 3:

                        "{b}Sua fraca defesa inicial não é suficiente e os zumbis comem o cérebro do dono da casa{/b}"

                        g "Você achou mesmo que essas plantas comuns iam te defender das galinhas? Muito burro!"

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 4:

                        "{b}Sua fraca defesa inicial não é suficiente e o zumbi come o cérebro do dono da casa{/b}"

                        g "Haha! Só com isso você nunca vai parar o jogador de futebol americano! Ele é foda!"

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    jump j2_resultado
                "Plantar uma {b}Batatamina{/b}":


                    "O melhor aqui é plantar uma batata para que ela exploda."

                    "Tenho certeza que isso vai funcionar nesta rodada."

                    if j1dom == 1:

                        "{b}Sua Batatamina explode e derrota o primeiro zumbi, mas os outros comem o cérebro do dono da casa{/b}"

                        "Haha! A mina não é pra usar nesse caso. Você não sabe nada desse jogo. Que vergonha."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 2:

                        "{b}Sua Batatamina explode e derrota o primeiro zumbi, mas os outros comem o cérebro do dono da casa{/b}"

                        "São muitos jornaleiros pra derrotar. A mina não é suficiente nesse caso. Aprenda com a mestra."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 3:

                        "{b}Sua Batatamina explode e derrota o primeiro zumbi, mas os outros comem o cérebro do dono da casa{/b}"

                        "São galinhas demais! Mesmo que você exploda uma ou duas, as outras acabam com você! Buhahahaha!"

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 4:

                        "{b}Sua Batatamina explode o poderoso zumbi e [g] fica sem poder invocar outros zumbis. Você venceu!{/b}"

                        mc "Toma essa, pirralha! A batatinha acabou com ele!"

                        g "Você me paga, [mc]..."

                        $ j2_juliavenceu = False
                        $ j2_mcvenceu += 1

                    jump j2_resultado
                "Plantar uma fileira de {b}Repolhopultas{/b}":


                    "Estas plantas atacam por cima. Elas são perfeitas contra este tipo de zumbi!"

                    "Não tem como elas não darem conta do recado."

                    if j1dom == 1:

                        "{b}As Repolhopultas derrotam os primeiros zumbis, mas sem recursos você acaba perdendo no final{/b}"

                        g "Isso que dá não investir em girassóis no começo. Você perde o gás no fim. Muito ruim!"

                        mc "Grrrr..."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 2:

                        "{b}Suas plantas atacam por cima e derrotam os zumbis jornaleiros com facilidade. A rodada é sua!{/b}"

                        mc "Muito bom, Repolhopultas! Mostramos pra ela quem que manda aqui!"

                        g "Não acredito que você ganhou fácil desse jeito..."

                        mc "Hah! Toma essa, pirralha!"

                        $ j2_juliavenceu = False
                        $ j2_mcvenceu += 1

                    elif j1dom == 3:

                        "{b}As Repolhopultas não atacam rápido suficiente para matar todas as galinhas e você perde a rodada{/b}"

                        g "Você pensou que elas iam vencer o ataque infernal das galinhas?"

                        g "Você precisa de muito treino ainda..."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 4:

                        "{b}A Repolhopulta não é forte o suficiente para vencer o zumbi jogador de futebol americano e você é derrotado{/b}"

                        g "Tadinha da Repolhopulta! Ela precisa sofrer porque o dono dela é um babaca hahaha!"

                        mc "Grrr..."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    jump j2_resultado
                "Plantar alguns {b}Junco-relâmpagos{/b}":


                    "Estas plantas são elétricas e bem diferentes. Elas são fracas, mas atacam muitos zumbis de uma vez."

                    "Tenho certeza que é o ideal para esta rodada!"

                    if j1dom == 1:

                        "{b}Os relâmpagos derrotam o ataque inicial, mas sem girassóis você é derrotado no final da rodada.{/b}"

                        g "{i}Pfff{/i}... Sem comentários."

                        mc "..."
                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 2:

                        "{b}Os ataques elétricos não são forte o suficiente para evitar que o cérebro do dono da casa seja comido{/b}"

                        g "Depois que os jornais são queimados eles ficam ainda mais fortes!"

                        "Parece que eu tenho que atacar estes aqui por cima..."

                        g "Burro!"

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    elif j1dom == 3:

                        "{b}Os ataques fracos, mas constantes, são o suficiente para matar as galinhas e garantem sua vitória!{/b}"

                        mc "Isso aí! Eu sabia que esses choquinhos iam acabar dando certo."

                        g "Você conseguiu vencer as galinhas... Impossível..."

                        mc "Enfia as galinhas no..."

                        g "Ei!"

                        $ j2_juliavenceu = False
                        $ j2_mcvenceu += 1

                    elif j1dom == 4:

                        "{b}Os ataques elétricos não são forte o suficiente para evitar que o cérebro do dono da casa seja comido{/b}"

                        g "O grandão é forte demais pra esses choquinhos de nada. Você ainda não entendeu?"

                        mc "Só fica quieta que eu vou ganhar de você ainda..."

                        g "Ah, vai. Claro..."

                        $ j2_juliavenceu = True
                        $ j2_jvenceu += 1

                    jump j2_resultado

        label julia_e2_demorou:

            g "Você demorou demais, palermão!"

            "Droga... Não posso demorar tanto pra tomar uma decisão."

            $ jandom = renpy.random.randint(1,4)

            if jandom == 1:

                g "Essa eu ganhei fácil!"

                mc "Não vai comemorando antes da hora."

            elif jandom == 2:

                g "Mas já perdeu?!"

                mc "Droga..."

            elif jandom == 3:

                g "Hahahaha!"

                "Merda... Por que eu demorei tanto?"

            elif jandom == 4:

                g "Já tá dando dó."

                mc "Se concentra aí..."

            $ j2_juliavenceu = True
            $ j2_jvenceu += 1

            jump j2_resultado

        label j2_resultado:

            if j2_juliavenceu:

                if j2_jvenceu == 1 and j2_mcvenceu == 0:

                    scene julia jogando_mc with Dissolve(1.0)

                    g "Você fica gato sem camisa. Tá me deixando excitada."

                    mc "É tudo o que você vai ver nessa partida."

                    g "Eu acho que eu vou ver muito mais."

                    mc "..."

                    jump j2_novoround

                elif j2_jvenceu == 1 and j2_mcvenceu > 0:



                    g "Agora sim! Foi só sorte de principiante."

                    mc "Vai nessa. Eu vou acabar com você!"

                    g "Sonha mais."

                    jump j2_novoround

                elif j2_jvenceu == 2:

                    scene julia mc_perdendo with Dissolve(1.0)

                    mc "Droga! Dessa vez eu pego você!"

                    g "Tá nervosinho?"

                    mc "Cala a boca. Só deixa eu me concentrar."

                    "Ela vai ver só..."

                    jump j2_novoround

                elif j2_jvenceu == 3:

                    $ timeout_label = None

                    g "Ganhei as três! Eu sou demais!"

                    mc "Merda..."

                    g "Você já tá sem roupa. Então agora é só subir na mesa."

                    mc "Vai me fazer subir mesmo?"

                    g "Claro. E ainda vai ter que fazer uma pose assim de homem das cavernas."

                    mc "Droga..."

                    scene julia mc_perdeu with Dissolve(2.0)

                    mc "..."

                    g "Hahaha!"

                    mc "Feliz?"

                    g "Muito!"

                    g "E agora? Essa derrota foi o suficiente pra você ou vai querer uma revanche?"

                    mc "Hmmm..."

                    menu:
                        "Jogar mais uma vez e tentar ganhar dela":


                            $ j2_mc_perdeu = True

                            "Não posso desistir agora. Quero ver ela tirando toda a roupa."

                            "E meu orgulho como gamer? Como fica?"

                            mc "Vou querer uma revanche. Vai se preparando."

                            g "Vai perder de novo!"

                            jump julia_e2_game
                        "Desistir e sair derrotado":


                            $ julia_e2_game = "derrota"

                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("j2_desistiu_jogo","julia","personagem")

                            "Não aguento mais. Não tenho como derrotar ela nesse jogo."

                            mc "Desisto. Tenho que admitir minha derrota."

                            g "Muito bem!"

                            g "É importante saber o seu lugar."

                            mc "Pirralha..."

                            jump julia_e2_game_depois
            else:


                if j2_mcvenceu == 1:

                    mc "Haha! Cadê toda sua pompa agora?"

                    g "Ah! Cala a boca! Tem muito jogo ainda."

                    scene julia perdeu_uma with Dissolve(1.0)

                    pause

                    g "Eu estou só começando com você."

                    mc "Se prepara pra perder a próxima também."

                    jump j2_novoround

                elif j2_mcvenceu == 2:

                    mc "Estou chegando muito perto."

                    g "Grrr... Mas ainda falta mais uma pra você."

                    "..."

                    scene julia jogando_final with Dissolve(1.0)

                    pause

                    g "Vou começar a jogar pra valer agora."

                    mc "Tá ficando com medinho, né?"

                    g "Cala a boca e joga!"

                    jump j2_novoround

                elif j2_mcvenceu == 3:

                    $ timeout_label = None

                    mc "Pera... Consegui! Este era o terceiro roundo! Eu venci!"

                    scene sayuri_casa tv with Dissolve(1.0)

                    g "..."

                    mc "E aí? Cadê a provocadora agora?"

                    g "Ainda não acredito..."

                    mc "Agora tá caladinha, né?"

                    g "..."

                    "Muito bom! Consegui vencer ela!"

                    "Será que eu cobro que ela suba na mesa e faça uma pose?"

                    menu:
                        "Com certeza. Essa é uma boa chance de esquentar as coisas.":


                            if julia_seducao < 15:
                                $ julia_seducao += 1
                                if julia_seducao >= 15:
                                    $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                            else:
                                $ julia_seducao += 1

                            "Tudo o que eu quero agora é poder pegar ela. E fazer ela pagar esse castigo vai me ajudar nessa."

                            jump j2_pagar_castigo
                        "Isso é demais. Não vou fazer ela pagar o castigo.":


                            $ sayuri_amizade += 3

                            if julia_seducao >= 15:
                                $ julia_seducao -= 2
                                if julia_seducao < 15:
                                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                            else:
                                $ julia_seducao -= 2

                            "Ah... Acho que ela não precisa fazer isso. Minha vitória foi o suficiente."

                            mc "Não se preocupe. Pode se vestir. Não precisa subir na mesa."

                            g "Sério?"

                            mc "Sim."

                            "..."

                            show julia provocando with dissolve

                            g "Obrigada, [mc]. Você até que é um cavalheiro."

                            mc charmoso "Se eu quiser tirar sua roupa, tenho outras formas de fazer isso."

                            g "E você tem mesmo, você sabe disso."

                            mc safado "..."

                            jump julia_e2_game_depois
                        "Ela perdeu. Ela precisa arcar com o castigo.":


                            label j2_pagar_castigo:

                                "Não existe piedade agora."

                            mc "Chegou a hora que eu tava esperando. Pode subindo na mesa."

                            g "Ok..."

                            mc "Quero que você faça uma pose bem sexy."

                            g "Hmm... Agora eu até gostei."

                            "..."

                            scene julia mc_venceu with Dissolve(3.0)

                            pause

                            mc "..."

                            g "Gostou da sua recompensa?"

                            mc "Com certeza. Você é uma delícia."

                            if julia_seducao >= 9:

                                if j2_mc_perdeu or j2_jvenceu > 0:

                                    g "Sabia que vendo você tirando a roupa e me olhando desse jeito me deixou toda molhada?"

                                    mc "Você também me deixou excitado."

                                    g "Só tem um jeito da gente resolver isso, não acha?"

                                    mc "Sim."

                                    scene sayuri_casa tv with Dissolve(1.0)

                                    mc "Vem aqui no sofá comigo."

                                    g "Eu vou..."

                                    mc "Sobe aqui."

                                    g "Ai..."

                                    menu:
                                        "Beijar ela":


                                            "Eu esperei muito tempo por isso."

                                        "Melhor parar por aqui. Isso está indo longe demais" if julia_seducao < 15:

                                            mc "Não!"

                                            mc "Desculpa, [g]. Mas é melhor a gente parar."

                                            g "Como assim?! Agora que a gente tá chegando no que eu esperei a noite toda."

                                            mc "Mas..."

                                            menu:
                                                "Ceder e beijar ela":


                                                    "Não tenho como parar agora. Eu tô muito excitado."
                                                "Preciso me controlar e parar por aqui.":


                                                    $ sayuri_amizade += 3
                                                    $ j2_recusou = "sim"

                                                    "Não é isso que eu quero com ela. E ainda tem a [s]. Eu preciso me controlar"

                                                    mc desculpa "Me desculpa. Mas eu realmente não posso fazer isso."

                                                    "..."

                                                    show julia brava with dissolve

                                                    g "Não tô acreditando em você, [mc]!"

                                                    g "A gente tava indo tão bem! Eu tô muito excitada. Você também!"

                                                    g "O que aconteceu?!"

                                                    mc desculpa "Não é nada... Só que eu tô pensando e acho que a gente parar é o melhor."

                                                    g "Não tô entendendo!"

                                                    mc normal "Você vai ter que aceitar, só isso."

                                                    g "Hmm... Não posso te obrigar a me beijar, mas isso ainda vai ter volta. Você vai ver!"

                                                    mc desculpa "Desculpa de novo por ter cortado o clima."

                                                    g "Tudo bem..."

                                                    jump julia_e2_game_depois

                                    scene julia beijo_close with Dissolve(3.0)

                                    pause

                                    $ j2_recusou = "não"

                                    $ julia_e2 = "seducao"

                                    python:
                                        if renpy.android:
                                            PythonSDLActivity.registraEvento("julia_e2_seducao","julia","personagem")

                                    g "Isso, [mc]. Me beija."

                                    g "Eu tô sentindo você aqui embaixo. Você tá muito duro."

                                    mc "Não consigo me controlar."

                                    g "Então me beija aqui. Isso."

                                    g "Ai..."

                                    menu:
                                        "Tirar o sutiã dela.":


                                            mc "Deixa eu te ajudar. A gente não precisa disso aqui."

                                            g "Ai, seu safado. Vai me deixar peladinha?"

                                            mc "..."

                                            scene julia beijo_casa with Dissolve(3.0)

                                            g "Ai, [mc]. Tá tão gostoso me esfregar em você."

                                            g "Hmmm..."

                                            mc "Isso. Quero que você se sinta bem."

                                            g "Sim! Só continua me beijando."

                                            g "Hmmm! Ai!"

                                            g "Assim!"

                                            g "Aaaaiii!"

                                            g "{i}puf... puf...{/i}"

                                            g "Que delícia..."

                                            g "Agora é sua vez."

                                            if julia_e1 == "seducao":

                                                mc "E você ainda tem que me pagar pelo parque também."

                                                g "Claro."

                                                g "Vou começar com a boca..."

                                            g "Hmmm..."



                                            scene j2_new5 with Dissolve(1.0)

                                            pause

                                            g "Era isso que você tava esperando pra hoje?"

                                            menu:
                                                "Eu quero mais.":


                                                    mc "A gente não precisa parar agora. Eu quero mais ainda."
                                                "Não. Foi uma surpresa.":


                                                    mc "Não... eu vim assistir a premiação... foi uma surpresa e tanto."

                                            g "Eu falei que eu ia te compensar, então a gente vai até onde você quiser."

                                            mc "A gente nem se conhece direito."

                                            g "E daí? A gente só tá se pegando, bobo."

                                            mc "E tá tudo bem pra você?"
                                            scene jnew_ani13 with Dissolve(1.0)
                                            g "Claro. Eu adoro brincar com desconhecidos."

                                            mc "Você faz bastante isso?"

                                            g "Só com quem me deixa quente."

                                            mc "E eu te deixei..."

                                            g "Com certeza. Tirar a roupa pra você por causa do jogo foi bem quente."

                                            mc "Eu gostei bastante."

                                            g "Agora falta gozar bastante. Vem aqui."

                                            scene j2_new6 with Dissolve(1.0)

                                            g "Hmm..."

                                            mc "Você é boa de beijo."

                                            g "Eu sei. Eu treino bastante."

                                            "Essa garota..."

                                            g "Eu adoro sentir uma língua dentro da minha boca."

                                            mc "Você tem bastante fogo, hein?"

                                            g "O tempo inteiro. Será que você consegue apagar ele?"

                                            mc "A [s] deve tá chegando logo logo. Se ela pega a gente..."

                                            g "E daí? Você vai perder isso aqui por causa dela?"

                                            "As coisas com a [s] podem complicar se eu continuar aqui com a [g] desse jeito..."

                                            menu:
                                                "Eu vou apagar seu fogo.":


                                                    mc "Eu sei exatamente como apagar o fogo dessa sua bucetinha."

                                                    g "Hmm... eu gosto quando falam grosso assim."

                                                    mc "Vira aqui que você vai sentir."

                                                    scene j2_new7 with Dissolve(1.0)

                                                    pause

                                                    g "Hmmm!"

                                                    mc "Arrepiou?"

                                                    g "Arrepiei. Você apertou gostoso agora."

                                                    g "Eu tô sentindo seu caralho bem na boquinha."
                                                    scene jnew_ani27 with Dissolve(1.0)
                                                    mc "É bom?"

                                                    g "Para de me provocar!"

                                                    mc "Quer sentir ele, é?"

                                                    g "Quero! Vai!"

                                                    menu:
                                                        "Continuar provocando":


                                                            "Eu tô gostando de ver ela assim."

                                                            scene j2_new8 with Dissolve(1.0)

                                                            g "Ah... vai..."

                                                            mc "Não tô conseguindo..."

                                                            g "Deixa que eu enfio."

                                                            "Se eu não ajudar, ela não consegue."

                                                            g "Nnng... você tá fazendo de propósito?!"

                                                            mc "O quê?"

                                                            g "Para de esfregar e enfia logo!"

                                                            g "Eu tô toda molhada, é só você... nnng... vai... ahnn..."

                                                            "Até meu pau tá ficando molhado com o suco da [g]."

                                                            "Acho que tá bom. Eu também não vejo a hora de comer ela."
                                                        "Enfiar nela":


                                                            pass

                                                    mc "Se você não aguenta mais..."

                                                    g "Não aguento!"

                                                    "Chega de brincadeira!"

                                                    scene j2_new9 with vpunch

                                                    g "AANNNG!"

                                                    g "Assim!"

                                                    g "Agora você vai meter com toda sua força, seu filha da{nw}"
                                                "É melhor parar aqui.":


                                                    mc "Você é muito gostosa, mas não quero que a [s] pegue a gente com a mão na massa."

                                                    g "Ain... eu não sou gostosa o suficiente pra você fazer uma coisinha errada?"

                                                    mc "[g]... você é uma delícia, mas voc-"

                                            play sound "audio/som_15_campainha.mp3"

                                            "{i}Ding Dong{/i}"

                                            g "{size=15}Meu Deus! É a [s]!{/size}"

                                            s "{size=15}[g]. Cheguei.{/size}"

                                            scene sayuri_casa tv with vpunch

                                            g "{size=15}Sai de cima de mim!{/size}"

                                            mc "Ei!"

                                            g "Já tô indo, mana!"

                                            g "{size=15}Coloca a roupa!{/size}"

                                            "..."

                                            "Meu Deus! A [s] vai me ver aqui. O que eu falo pra ela?"

                                            if j2_sayuri_avisou:

                                                "Eu disse pra ela que eu estaria aqui, mas também disse que voltaria cedo."

                                                "Droga... Como será que ela vai reagir?"
                                            else:


                                                "Eu resolvi não avisar ela! E agora? Não dá pra sair escondido."

                                                "Tô ferrado!"

                                                mc triste "..."

                                            scene sayuri_casa geral with Dissolve(1.0)

                                            show julia provocando with dissolve

                                            g "Oi, mana! Voltou rápido."

                                            show julia provocando at direita with move

                                            show sayuri e_sem_jeito with dissolve

                                            s "Eu não fiquei até o fim. Mas eu juro que fiquei o máximo que aguentei."

                                            show sayuri e_sem_jeito at esquerda with move

                                            g "Não precisa ficar triste! Você foi muito bem!"

                                            mc envergonhado "Oi, [s]."

                                            show sayuri e_desesperada with hpunch

                                            s "[mc]!"

                                            mc "O-olá."

                                            g "Aé! O [mc] tá aqui. Ele veio ver a sua premiação. Eu que chamei ele."

                                            if j2_sayuri_avisou:

                                                show sayuri e_sem_jeito with dissolve

                                                s "Ah... Eu sei... Ele me avisou."

                                                g "Sério?"

                                                s "Sim."

                                                if sayuri_intencao == "namoro":

                                                    if sayuri_e3 == "beijo":

                                                        s "Ele deve ter achado importante me avisar depois que a gente se be-be-be..."
                                                    else:


                                                        s "Ele deve ter achado importante me avisar depois que ele falou que não quer ser só um..."

                                                    show sayuri e_desesperada with hpunch

                                                    s "Me-meu Deus! O que eu estou falando!?"

                                                    s "Bo-bo-bo-boa noite!"

                                                    hide sayuri with moveoutleft

                                                    show julia brava with dissolve

                                                    show julia brava at centro with move

                                                    g "Ei. Que porra foi essa?"

                                                    g "Tá rolando alguma coisa que eu não tô sabendo?"

                                                    mc envergonhado "Sei lá..."

                                                    g "Bah! Não gosto de ficar no escuro desse jeito! Pode abrindo a boca."

                                                    mc normal "Pergunte pra sua mana."

                                                    g "Seu maldito. Ela vai me contar!"

                                                    mc tarado "Ok, então."

                                                    g "Você tá me zuando! Pode parando aí!"

                                                    g "Droga... Ok."

                                                    jump julia_e2_final

                                                elif sayuri_intencao == "amizade":

                                                    s "Eu fiquei feliz dele ter me contado. Isso é coisa que amigos fazem."

                                                    s "Eu queria muito conversar, mas eu tô tão cansada."

                                                    g "Não esquente, mana. O [mc] já tava saindo na verdade."

                                                    mc envergonhado "Isso mesmo. O importante era só ver seu momento."

                                                    s "O-obrigada."

                                                    s "Eu vou tomar um banho, então. Boa noite, [mc]."

                                                    mc normal "Boa noite, [s]. Até a próxima."

                                                    s "Até."

                                                    g "Falou, mana."

                                                    hide sayuri with moveoutleft

                                                    show julia provocando with dissolve

                                                    show julia provocando at centro with move

                                                    g "Amigos, hein?"

                                                    mc envergonhado "Pois é..."

                                                    jump julia_e2_final
                                            else:


                                                $ sayuri_amizade -= 3
                                                $ j2_sayuri_traida = True

                                                python:
                                                    if renpy.android:
                                                        PythonSDLActivity.registraEvento("j2_sayuri_traida","julia","personagem")

                                                s "Ma-mas... Por que vocês não me contaram nada?"

                                                g "É... é..."

                                                mc preocupado "É que foi de última hora. Desculpa não ter te contado, [s]."

                                                if sayuri_intencao == "namoro":

                                                    if sayuri_e3 == "beijo":

                                                        s "Ainda mais depois que a gente se be.... be-be..."
                                                    else:


                                                        s "Ainda mais depois que você falou que não quer ser só um am..."

                                                    s "Me-meu Deus! O que eu ia falar?!"

                                                    s "E-e-e-eu..."

                                                elif sayuri_intencao == "amizade":

                                                    s "Isso não é coisa que um amigo... faça..."

                                                    s "Você disse que queria ser... meu..."

                                                s "E-e-eu... eu não tô me sentindo bem."

                                                s "Com licença, pessoal."

                                                hide sayuri with dissolve

                                                show julia brava with dissolve

                                                show julia brava at centro with move

                                                g "Droga... Não deu nada certo..."

                                                g "Você devia ter avisado ela!"

                                                g "Agora ela tá triste e é tudo culpa sua!"

                                                mc serio "Culpa minha?! Você quem causou tudo isso!"

                                                g "Grrrr...."

                                                mc concentrando "..."

                                                menu:
                                                    "Não me chame nunca mais pra fazer nada!":


                                                        $ julia_e2 = "brigados"

                                                        python:
                                                            if renpy.android:
                                                                PythonSDLActivity.registraEvento("julia_e2_brigados","julia","personagem")

                                                        mc bravo "Você só ferra meu lance com a [s]! Não me chame nunca mais pra fazer nada!"

                                                        g "Com todo o prazer, idiota!"

                                                        hide julia with dissolve

                                                        mc "Adeus!"

                                                        scene black with Dissolve(1.0)

                                                        "Que merda..."

                                                        "Consegui deixar a [s] triste e ainda briguei com a [g]. Essa noite foi horrível!"

                                                        "Espero que as coisas melhorem no futuro..."

                                                        $ tempo += 1

                                                        $ v8_fim = True

                                                        jump call_cidade
                                                    "Ok. A culpa foi minha também... Desculpa.":


                                                        mc desculpa "Não adianta eu brigar com você agora. A culpa foi minha também de não ter avisado."

                                                        g "A culpa foi só sua!"

                                                        mc zerado "..."

                                                        g "Droga... Tomara que ela não fique chateada pra sempre, agora."

                                                        mc envergonhado "'Pra sempre' parece um pouco exagerado."

                                                        g "Você não sabe de nada."

                                                        mc desculpa "..."

                                                        show julia peralta with dissolve

                                                        g "Mas não se preocupe. Acho que eu consigo arrumar ela."

                                                        mc zerado "Não é como se ela tivesse quebrada."

                                                        g "Eu vou conversar com ela e explicar tudo."

                                                        g "Eu gostei da nossa noite. Quero poder fazer mais vezes."

                                                        mc desculpa "Não sei se a gente devia..."
                                        "A gente foi longe demais.":




                                            $ j2_recusou = "sim"
                                            $ sayuri_amizade += 3

                                            "Não é isso que eu quero com ela. E ainda tem a [s]. Eu preciso me controlar"

                                            mc desculpa "Me desculpa. Mas eu realmente não posso fazer isso."

                                            "..."

                                            show julia brava with dissolve

                                            g "Não tô acreditando em você, [mc]!"

                                            g "A gente tava indo tão bem! Eu tô muito excitada. Você também!"

                                            g "O que aconteceu?!"

                                            mc desculpa "Não é nada... Só que eu tô pensando e acho que a gente parar é o melhor."

                                            g "Não tô entendendo!"

                                            mc normal "Você vai ter que aceitar, só isso."

                                            g "Hmm... Não posso te obrigar a me beijar, mas isso ainda vai ter volta. Você vai ver!"

                                            mc desculpa "Desculpa de novo por ter cortado o clima."

                                            g "Tudo bem..."

                                            jump julia_e2_final

    label julia_e2_game_depois:

        scene julia confessando with Dissolve(1.0)

        g "Cansei..."

        mc concentrando "Eu também."

        g "Essa noite foi muito bacana, [mc]."

        mc normal "Você achou?"

        g "Sim. Normalmente eu não faço muita coisa com os garotos. A gente normalmente só se pega."

        mc safado "Entendo..."

        scene julia confessando_solo with Dissolve(1.0)

        g "Mas com você eu sinto que eu converso e faço outras coisas. Você é como se fosse uma [s] XY."

        mc desconfiado "XY?"

        g "Faz tempo que você prestou vestibular, hein?"

        mc zerado "Tá me zoando..."

        g "Hehe. Você é estranho."

        mc "Você vive me falando isso."

        g "Mas eu gosto de você, [mc]. Obrigada por ter passado a noite comigo."

        mc envergonhado "Eu gosto de você também. Não foi nada. Eu me diverti."

        scene sayuri_casa geral with Dissolve(1.0)

    label julia_e2_final:





        g "Bom..."

        g "O show acabou. Pode indo pra casa."

        mc triste "Mas a gente ainda..."

        show julia peralta with dissolve

        g "A gente ainda vai se ver. Você ainda vai ter sua chance de me comer."

        mc surpreso "Mas... mas..."

        g "Que foi?"

        mc envergonhado "Nada. Só que não sei se isso é certo..."

        g "Já falei pra você parar de ser cagão."

        mc zerado "A questão não é..."

        g "Falous, [mc]. Logo eu te escrevo."

        mc zerado "Falous..."

        hide julia with dissolve

        scene black with Dissolve(1.0)

        "Bora voltar pra ilha."

        play sound "audio/som_14_onibus.mp3"

        scene cidade noite with Dissolve(1.0)

        $ renpy.pause(delay=5, hard=True)

        "..."

        "Todas as vezes que eu me envolvo com a [g] é uma loucura."

        if julia_e2 == "seducao":

            "As coisas esquentaram esta noite."

            "Eu tava tão perto de finalmente transar com ela. A [s] tinha que chegar bem naquela hora..."

            "A [g] é tão sexy. Será que vale a pena tentar uma coisa mais séria com ela?"

            "Tenho que tomar cuidado com o jeito dela também. A [g] parece tratar todos os homens como brinquedos."

            "Como se a gente fosse apenas um vibrador. Se eu for só mais um objeto pra ela talvez ela enjoe."

            "E seria uma perda terrível não poder mais dar uns amassos com ela."

            if j2_sayuri_traida:

                "O problema é que a [s] ficou muito chateada com tudo isso."

                "Ainda mais porque eu disse que queria algo mais com ela."

                "Depois tenho que ver como as coisas vão ficar entre a gente."

        if julia_e2_conversou:

            "Por outro lado, aquela história que ela contou sobre ela e a [s] foi muito grave."

            "Será que é possível pais tratarem uma criança desse jeito?"

            "Talvez isso explique muita coisa sobre a forma como ela vive."

            mc preocupado "Será que eu posso fazer alguma coisa pra ajudar?"

            "Se eu tiver a chance, eu gostaria de dizer umas verdades pra esses canalhas."

            "Pelo menos eu sou uma pessoa que ela pode se abrir. Se eu continuar vendo ela, quem sabe."

            "Talvez um dia surja a oportunidade de fazer algo mais por ela."

            "..."

            "Esse negócio de {b}organização chinesa{/b} também é muito estranho."

            "Parece coisa de filme..."

            "Dá até um calafrio. Mas se eu quiser ter algo sério com uma delas, provavelmente vou ter que entrar nessa."

        "Essas garotas dão uma dor de cabeça, mas minha vida nunca foi tão divertida."

        "Eu fico pensando como minha relação com elas vai acabar."

        "E quantas novas celebridades e pessoas eu ainda vou encontrar."

        "Preciso estar pronto para o que futuro me reserva!"

        $ tempo += 1

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v8_fim","julia","personagem")

        $ v8_fim = True

        jump call_cidade

label julia_evento3:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j3_save", extra_info="j3_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "A [s] disse que a [g] não tá muito bacana esses dias. O que será que aconteceu com ela?"

    if tempo < 3:

        scene mc parque_sentado with Dissolve(2.0)
    else:


        scene mc parque_sentado_noite with Dissolve(2.0)

    if julia_e2 == "brigados":

        "A gente discutiu feio lá na casa dela por causa da [s]..."

    if sayuri_e4 == "badending":

        "Teve todo aquele rolo na outra noite. Ela acabou comigo na frente da [s]."

        mc bravo "A [g] não podia ter feito aquilo."

    elif s4_julia_good:

        "Naquela outra noite, no ponto de ônibus, a [g] não tava nada legal."

        "Ela gritou e fez tudo aquilo. Tentou me queimar com a [s], mas no fundo ela só tava muito triste."

    "De uma forma ou de outra ela me deu a dica de chamar a [s] pra sair."

    "Eu queria poder fazer alguma coisa por ela."

    if julia_e2_conversou:

        "Ela me contou aquela vez na casa dela todo aquele lance com os pais da [s]."

        "Aquilo me deixou tão puto. Como pode os pais fazerem isso com uma filha?"

    "No fundo eu sinto que a [g] é só uma garota muito machucada. Mas não tenho como ter certeza."

    "O tanto que ela é sexy e peralta ela também é misteriosa. Ela fala pouco sobre ela. E não tem como saber o que ela tá pensando."

    if julia_seducao >= 15:

        "Eu só sei que eu tô muito na dela. Ela tem me provocado muito e eu tô aceitando."

        "O problema disso é que eu não consigo dizer não pra ela. É como se ela tivesse controle sobre mim."

        "Isso é muito perigoso. Além do mais, a [g] já enjoou de outros namoradinhos."

    elif julia_seducao >= 9 and julia_seducao < 15:

        "Até o momento eu estou conseguindo manter nossa relação no ponto ideal."

        "Não estou dominado por ela. Ou seja, não sou um brinquedinho, mas também nossa relação não esfriou."

        "Se eu conseguir manter as coisas assim, posso ter uma relação duradoura com ela eu acho."
    else:


        "Nossa relação tá bem fria. Eu não aceito as provocações dela e a gente tá nessa."

        "Não vejo a [g] com segundas intenções. Acho que podemos ser bons amigos."

        "Ou talvez nem isso se ela me encher muito."

    "Mesmo tendo passado um tempo com ela, ainda acho ela uma incógnita. Só que eu quero desvendar esse mistério."

    "Talvez eu consiga entender melhor a relação da [g] e da [s] se eu descobrir mais sobre essa doidinha."

    "..."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    "Mas dessa vez eu vou tentar algo diferente. Ao invés de eu perguntar pra ela, eu vou investigar."

    "Eu sei que ela vive na capital... que trabalha no Tadaima e tá na faculdade..."

    "Eu nem sei qual é o curso dela..."

    if julia_e1 == "seducao" or julia_e2 == "seducao":

        mc "Que cavalheiro que eu sou..."

        "Já quase transei com a mina, e nem sei o curso que ela estuda na faculdade..."

    "Eu vou mudar isso dessa vez. Vou tentar descobrir o máximo que eu puder sobre ela."

    "Talvez o melhor lugar seja investigar ela na faculdade. Talvez eu consiga pegar ela falando com alguma amiga ou amigo."

    "Quem sabe ela não se abre mais falando com um conhecido? Isso seria perfeito pra eu entender ela melhor."

    "Se eu fizer um bom trabalho de investigação, tenho certeza que posso descobrir tudo sobre ela."

    if julia_seducao >= 9:

        mc "E quem sabe até pegar ela se trocando quem sabe..."

        "O que eu tô pensando!?"

    "Mas acho melhor que ela não saiba. Do jeito que ela é retraída, no momento que eu for descoberto, ela vai ficar esperta."

    "Tenho que ser o mais sorrateiro possível."

    mc "Estou realmente animado. Estou me sentindo um agente do FBI."

    "Agente [mcc]. Até que ficou bom."

    "Chega de viajar!"

    if tempo < 3:

        "Ainda tem um tempo até começar a aula dela. Vou dar uma enrolada antes de sair."

        "Vou tomar um banho tranquilo e daí eu saio."
    else:


        "Olha a hora. Daqui a pouco começa a aula dela. Melhor eu sair o quanto antes."

        "Vou tomar uma ducha rápida e dar o fora."

    scene black with Dissolve(1.0)

    p rindo "Oi! Esta é uma parte bem interessante do game. Por isso queria te dar umas dicas."

    menu:
        "Por favor me ajude!":


            p "O [mc] vai tentar descobrir o máximo que ele puder sobre a [g] sem ser descoberto."

            p "O tamanho deste encontro depende do quanto você conseguirá descobrir sobre ela sem ser pego."

            p lecionando "Pra não ser pego, você vai ter que saber ser um bom investigador."

            p "Isso quer dizer que você precisa escolher a hora certa de se aproximar, e a hora certa de dar o fora."

            p "Outro ponto importante é sua sorte. Toda vez que você tentar xeretar, você pode ser descoberto ou não."

            p rindo "Ah! Quanto mais você fuçar a vida da [g], mais ela vai ficar de olho."

            p "E por isso é tão importante saber os melhores momentos pra xeretar."

            p "E caso você seja azarado e seja descoberto, não adianta usar o botão {b}Voltar{/b}. O resultado será sempre o mesmo."

            p "Por isso eu recomendo que você sempre pense bem antes de arriscar."

            p "Boa sorte, bebê!"
        "Não preciso. Sou conhecido como 007 na minha rua!":


            p "Ok, sabe-tudo! Boa sorte!"

    play sound "audio/som_16_chuveiro.mp3"

    if casa:

        scene ap mc_chuveiro with Dissolve(1.0)
    else:


        scene mc banho with Dissolve(1.0)

    "Digamos que eu vou fazer um jornalismo investigativo. Isso mesmo..."

    "Ou será que eu só tô tentando justificar minhas ações e no fundo só sou um perseguidor sem escrúpulos?"

    "..."

    "Pelo menos minha intenção é boa! Talvez..."

    menu:
        "Eu quero ajudar a [g] de verdade":


            "Eu realmente quero ajudar ela. Tanto pela própria [g] como pela [s]."

            "Ainda não entendo direito, mas tudo começou porque eu precisava de pautas para o chefe."

            "Mas agora parece que essas garotas realmente se transformaram em algo especial pra mim."
        "Eu quero ter a chance de ver ela se trocando...":


            "Talvez minhas intenções não sejam tão boas assim..."

            "Droga, eu devia ter vergonha de mim mesmo. Parece que cada vez mais eu tô virando um cachorro no cio."

            "Você é melhor que isso, [mc]!"

    "Visitar a casa da [g] seria um tanto perigoso. Eu ia parecer um ladrão."

    "Talvez o melhor é eu tentar investigar ela na faculdade. Talvez eu consiga ver ela no habitat natural de estudante."

    "Por que eu tô falando como se ela fosse um animal de um documentário da Discovery?"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene mc ap_pronto with Dissolve(1.0)

    "Estou pronto. Vou ser o melhor detetive que a cidade já viu."

    "Bora lá pegar o busão pra variar."

    "..."

    $ tempo = 4

    if carro:

        play sound som_carro

        scene black with dissolve

        scene carro_mc_cidade1 with Dissolve(1.0)

        pause

        "O problema de investigar a universidade é que eu acabei de me formar lá... E se alguém me reconhecer?"

        scene black with dissolve
    else:


        scene cidade onibus_noite with Dissolve(2.0)

        mc surpreso "Eita! O ônibus tá chegando! Primeira vez que eu dô sorte assim."

        call cena_onibus from _call_cena_onibus_3

        "O problema de investigar a universidade é que eu acabei de me formar lá... E se alguém me reconhecer?"

        "..."

        "Opa. É o próximo ponto."

        "..."

    scene universidade fachada with Dissolve(2.0)

    "Que saudades desse lugar."

    "Pensar que eu vim aqui toda noite por quatro anos..."

    scene uni_hall geral with Dissolve(3.0)

    "..."

    "Certo. Tem outros estudantes aqui e eu ainda me lembro muito bem onde fica cada lugar. Como que eu encontro a [g]?"

    label julia_e3_procurar:

        "Onde eu vou procurar por ela?"

        menu:
            "Biblioteca":


                "Talvez ela esteja na biblioteca."

                "Até parece. A [g] não tem cara de que fica na biblioteca."

                "Bom, não custa nada tentar."

                "..."

                scene uni_hall corredores with Dissolve(1.0)

                "Pelo que eu me lembro a biblioteca é esta sala."

                "Droga... eu praticamente nunca vim aqui em quatro anos estudando."

                "Tenho que tomar muito cuidado pra ela não me ver."

                "Vou dar uma olhada como quem não quer nada pelo vidro da porta..."

                scene uni_biblioteca geral with Dissolve(3.0)

                mc surpreso "Jackpot!"

                "Não acredito... o que ela tá fazendo aí?"

                "Preciso encontrar um lugar pra ouvir ela e que eu não chame atenção nem dela e nem dos outros alunos."

                call j3_calculo from _call_j3_calculo

                "Aqui ficou excelente. Deixa eu prestar atenção."

                show garconete e_emburrada with Dissolve(1.0)

                g "Não acredito que você vai me fazer ler..."

                show garconete e_emburrada at esquerda with move

                g "Você sabe que eu não tenho paciência pra ficar sentada."

                show 4olhos nervosa with Dissolve(1.0)

                o "Desculpa, Ju. É que... eu preciso mesmo estar pronta pra prova."

                show 4olhos nervosa at direita with move

                o "Eu só li esse material duas vezes. Nem terminei de fazer todos os exercícios..."

                show garconete e_resignada with dissolve

                $ o_nome = "Carol"

                g "Sem comentários pra você, [o]."

                o "Quê? Como assim?"

                g "Nada não..."

                g "Ah! E se a gente aproveitar que o professor liberou a gente e treinar e depois estudar?"

                g "A gente tem um monte de exercícios pra praticar!"

                o "Mas e a prova?"

                g "Você já tá mais do que pronta pra prova! Para de ser assim!"

                show 4olhos assustada with vpunch

                o "Pronta?!"

                o "Tô muito longe de pronta!"

                g "Para de ser besta."

                o "Só que-"

                g "Eu vou me trocar e te encontro na quadra!"

                o "..."

                o "Ok..."

                hide garconete e_emburrada with dissolve

                o "Ai ai, Ju..."

                hide 4olhos with dissolve

                "Epa. Deixa eu sair daqui."

                jump julia_e3_parte2
            "Vestiário":


                mc envergonhado "Talvez ela esteja no vestiário...."

                mc tarado "Tomara que ela esteja..."

                "Se controle, [mc]!"

                "..."

                scene uni_hall corredores with Dissolve(1.0)

                "Ok... preciso tomar muito muito cuidado pra ninguém me pegar xeretando o vestiário das mulheres."

                "Com muito cuidado..."

                scene uni_vestiario geral with Dissolve(2.0)

                "Talvez..."

                "Não tem nada aqu-"

                scene uni_vestiario geral with vpunch

                "Garota" "AAAHHHHHHHHHHHHHH!"

                mc surpreso "!!!!"

                scene uni_hall geral with vpunch

                "Ufa.... acho que não deu tempo dela ver minha cara."

                "Que perigo..."

                "Bom, a [g] não tava lá. E agora?"

                jump julia_e3_procurar
            "Quadra de esportes":


                "Eu nem sei qual é o curso que ela participa. Deixa eu dar uma olhada na quadra."

                "..."

                scene uni_hall corredores with Dissolve(2.0)

                "Agora tenho que pegar este outro caminho pra cá."

                "..."

                scene uni_quadra geral with Dissolve(2.0)

                "A quadra tá vazia..."

                "Nem sinal da [g]..."

                "..."

                scene uni_hall geral with Dissolve(2.0)

                "Que merda, nem sinal da [g]. E agora?"

                jump julia_e3_procurar


    label julia_e3_parte2:

        scene uni_hall geral with Dissolve(2.0)

        "Hmmm... quem é essa agora?"

        show mc pensando with dissolve

        "Então a [g] tem uma amiga além da [s]..."

        "Isso já é novidade pra mim. Minha investigação parece ter começado muito bem."

        "A questão agora é saber o quanto próximas elas são."

        "Em um primeiro momento, a garota parecia meio assustada com o jeito da [g]."

        "Hmmm..."

        "Opa! Acho que tô vendo elas."

        hide mc with dissolve

        "..."

        scene uni_hall corredores with Dissolve(1.0)

        "Preciso encontrar um lugar que elas não me notem, mas que eu possa ver e ouvir elas falando."

        "Será que eu devo arriscar ou melhor só ir pro ginásio e esperar elas lá?"

        menu:
            "Tentar xeretar a conversa sem ser visto":


                $ j3_ouviu_p1 = True

                "Eu tenho que saber sobre o que elas tão falando."

                "Tenho certeza que vai ser uma informação importante pra investigação."

                "..."

                call j3_calculo from _call_j3_calculo_1

                "Deu certo! Daqui eu vou poder ouvir tudo."

                show julia hall_falando with dissolve

                g "[o]! O que você tá fazendo sem a roupa ainda?!"

                show 4olhos hall_explicando with dissolve

                o "Desculpa, [g]. Eu só quis dar uma lidinha..."

                g "Você só pode tá brincando comigo!"

                g "Essa merda de prova de {b}Biologia Marítima{/b} não vale coisa nenhuma!"

                g "É uma disciplina de merda!"

                "{b}Biologia Marítima{/b}... Essa informação parece importante. Melhor eu me lembrar disso."

                o "Mas, [g]-"

                g "Nada de nada! Você só pensa em estudar!"

                o "E-eu... eu..."

                show 4olhos hall_chorando with dissolve

                o "{i}snif{/i}... você tem razão... {i}snif{/i}"

                g "Ca-carol... Você tá chorando?"

                o "{i}snif{/i}..."

                show julia hall_desculpa with dissolve

                g "Ai... e agora? De-desculpa, [o]. É... não queria te deixar triste."

                o "Não é culpa sua... Eu que sou tonta..."

                g "Nã-não! Eu que fui grossa com você."

                o "Não sei porque eu estudo tanto... e decepciono minha única amiga..."

                g "Tá, tá tudo legal, viu?"

                show 4olhos hall_explicando with dissolve

                o "Obrigada, Ju."

                g "Ufa..."

                show julia hall_falando with dissolve

                g "Que bom que você parou. Não me assusta assim, menina."

                o "Eu vou me trocar."

                g "Tá. Te espero lá na quadra."

                o "Tá. Tchau."

                hide julia with dissolve

                o "A [g] é tão legal..."

                hide 4olhos with dissolve

                "????"

                "Essa menina tá meio perdida com a [g]"

                o "Deixa eu..."

                mc surpreso "Opa!"

                o "Ai!"

                show 4olhos hall_mc with dissolve

                o "Ops. Desculpa, moço."

                menu:
                    "Relaxa. Você é linda, sabia?":


                        $ carol_reconheceu = True

                        mc charmoso "Não esquente. Trombar em uma garota linda como você nunca foi um problema."

                        o "Ah! É..."

                        mc "Como é seu nome?"

                        o "É [o]..."

                        mc "Um nome lin-"

                        o "Licença. Tenho que ir. Desculpa."

                        hide 4olhos with dissolve

                        "{b}Agora [o] marcou seu rosto e ficará mais esperta se você tentar investigá-la no futuro{/b}"

                        $ j3_xereta += 1
                    "Não foi nada. Com licença.":


                        "Melhor que ela não veja meu rosto."

                        mc concentrando "Não foi nada. Com licença."

                        o "..."

                        hide 4olhos with dissolve

                        "Ufa. Essa foi por pouco."

                        "É melhor que ela não me reconheça pra não prejudicar minha investigação."

                        jump julia_e3_ginasio
            "Deixar as duas e ir na frente":


                "Não quero arriscar que elas me vejam aqui. Vou direto pro ginásio e tento bisbilhotar elas por lá."

                "Provavelmente elas não vão falar nada importante no meio do corredor."

                jump julia_e3_ginasio


    label julia_e3_ginasio:

        "Certo. Melhor eu já ir pro ginásio e encontrar um lugar onde eu possa investigar elas."

        "Tenho que tomar cuidado pra não trombar com elas no caminho."

        "Se a [g] me ver aqui, vai ser o fim de tudo."

        "..."

        scene uni_quadra geral with Dissolve(2.0)

        mc feliz "Ufa. Cheguei antes delas."

        "{i}Inheeeeek{/i}"

        mc surpreso "!"

        "Tem alguém chegando aí. Deve ser a [g]."

        "O problema da quadra é que é um lugar aberto demais. Vai ser muito fácil elas me verem..."

        "E agora?"

        menu:
            "Fugir da quadra e esperar ela do lado de fora.":


                "Droga! Este lugar é arriscado demais!"

                "Mesmo perdendo o treino dela, não posso arriscar ser visto aqui!"

                "Só que elas vão treinar por um tempo. Vou perder muitas conversas... talvez tenha algo importante."

                "Será que eu realmente devo desistir de investigar ela aqui?"

                menu:
                    "Preciso desistir. É arriscado demais.":


                        "Não adianta eu exagerar. Melhor investigar ela em um lugar melhor."

                        jump julia_e3_vestiario
                    "Tenho que arriscar. Melhor investigar.":


                        "Não seja bundão, [mc]!"

                        jump j3_investigar_quadra
            "Se esconder e investigar.":


                label j3_investigar_quadra:

                    "Não quero perder as conversas dela durante todo o treino."

                    g "Tomara que a [o] chegue logo. Menina lerda!"

                    mc surpreso "É ela!"

                    "Xiu!! Tenho que me esconder rápido."

                    "Opa! Bem ali."

    scene uni_quadra visao1 with hpunch

    "Acho que aqui ela não vai me ver."

    "..."

    "Daqui dá pra ver uma parte da quadra. Espero que ela fique perto daquela porta."

    o "Oi, Ju! Desculpa a demora."

    "A outra chegou também."

    g "Aleluia, [o]! Pelo menos você veio."

    g "Vamos ficar ali no canto pra ninguém ficar secando a gente."

    o "Não acho que os garotos vão fazer isso."

    g "{i}Pff{/i}"

    "Elas tão indo bem pra aquela porta! O problema é que de lá elas vão poder me ver."

    "Tenho que me ajeitar o mais apertadinho aqui possível."

    "Agora é a hora da verdade."

    call j3_calculo from _call_j3_calculo_2

    mc concentrando "Que beleza. Parece que elas não me viram..."

    $ j3_ouviu_p2 = True

    scene uni_quadra close1 with Dissolve(2.0)

    show julia quadra_close1_provocando with dissolve

    g "Você é muito tontinha, [o]."

    o "Quê?"

    g "Os homens só conseguem pensar na gente. Parece que eles não têm outro objetivo na vida que não seja mulher."

    o "Não sei se isso é ver-"

    g "Olha só pra você. Você tem um par de peitões que qualquer homem iria dar a vida pra enfiar a cara no meio."

    scene uni_quadra close2 with Dissolve(1.0)

    show 4olhos quadra_close1_chateada with dissolve

    o "Ju!"

    g "É verdade!"

    o "Não acredito... eu não sou gostosa igual você..."

    g "Os homens que vão decidir isso. Mas que você tem um par de melões de outro mundo você tem."

    o "Eles são grandes demais."

    g "Tá doida? Pra eles quanto maior, melhor."

    o "Não sei..."

    scene uni_quadra close1 with dissolve

    show julia quadra_close1_provocando with dissolve

    g "O que eu tava querendo dizer é assim. Uma garota que não tem medo de usar seus dotes vai longe com os homens."

    o "Mas isso não é tipo se prostituir?"

    g "Claro que não! Eu tô falando de uma brincadeirinha. Dá uma olhada meio assim pra eles, pega no braço deles."

    g "Não precisa transar com os idiotas. Se bem que se você transar, você pode conseguir ainda mais coisa!"

    o "Ju!"

    g "Que foi?"

    scene uni_quadra close2 with dissolve

    show 4olhos quadra_close1_chateada with dissolve

    o "Seu jeito de falar. Você dá muito pouco valor pro seu corpo."

    g "Pelo contrário. Eu sei o valor do meu corpo e uso ele pra pisar neles."

    g "Ninguém mandou eles só pensarem nisso. Parecem um bando de animais."

    show 4olhos quadra_close1_falando with dissolve

    o "Do jeito que você fala, é como se você tivesse ódio dos rapazes."

    o "Parece que você tem uma obsessão por eles. Só que ao contrário, não sei."

    scene uni_quadra close1 with dissolve

    show julia quadra_close1_provocando with dissolve

    g "Você não sabe do que tá falando."

    o "É só você se ouvir."

    show julia quadra_close1_invocada with dissolve

    g "Para de falar besteira! Não tenho nada contra cara nenhum!"

    o "Desculpa... Não quis ofender ou alguma coisa assim."

    g "..."

    scene uni_quadra close2 with dissolve

    show 4olhos quadra_close1_falando with dissolve

    o "Mas eu acho que você podia pensar nisso direito. Talvez você devesse ver um psicólogo."

    g "Quê?! Tá me chamando de louca?!"

    show 4olhos quadra_close1_chateada with dissolve

    o "Não! A gente não tá mais em 1950, Ju! Hoje é muito normal a gente ver um profissional se não tá se sentindo bem."

    o "Pelo menos é o que eu acho..."

    scene uni_quadra close1 with dissolve

    show julia quadra_close1_invocada with dissolve

    g "Eu acho que você tá se intrometendo demais nas minhas coisas."

    o "Desculpa..."

    g "Tudo bem, vai..."

    show julia quadra_close1_provocando with dissolve

    g "O que eu quero é me tornar logo {b}bióloga{/b} e sair pelo mundo estudando as coisas!"

    o "É estranho ouvir você falando em estudar."

    g "Ei!"

    "{b}Bióloga{/b}? Então é isso que a [g] estuda... Ela deve tá cursando Biologia. Essa é uma informação que preciso guardar."

    g "..."

    o "..."

    g "Quer saber? Cansei desse exercício. O que acha da gente fazer aquela última sequência ali no meio da quadra e dar o fora daqui?"

    scene uni_quadra close2 with dissolve

    show 4olhos quadra_close1_falando with dissolve

    o "Sim. Eu queria mesmo poder dar mais uma lid-"

    g "[o]!"

    show 4olhos quadra_close1_chateada with dissolve

    o "Mas você prometeu que ia estudar comigo..."

    g "Tá!!"

    g "Vamos fazer o exercício e daí a gente toma uma ducha e estuda. Tá bom pra você?"

    o "Tá!"

    scene uni_quadra visao1 with Dissolve(1.0)

    "Parece que elas vão vir pro meio da quadra. Elas vão virar pra cá e podem me ver."

    "Será que eu arrisco ou melhor dar o fora daqui?"

    menu:
        "Vou arriscar. Tenho que tentar ver.":


            "Preciso ver isso. Não adianta ficar com medo. Preciso arriscar."

            "Elas estão vindo..."

            "Com muito cuidado..."

            call j3_calculo from _call_j3_calculo_3

            "Parece que deu tudo certo. Que cagaço, mano..."

            "Deixa eu ver o que vai rolar."

            scene julia quadra_4olhos with Dissolve(3.0)

            pause

            o "Ju..."

            g "Oi."

            o "Você tá fazendo o exercício certo ou só tá zoando?"

            g "..."

            o "Tá só zoando!"

            o "Ah! No fundo você só não quer estudar!"

            g "..."

            o "Vou sair daqui."

            g "[o]! Espera!"

            o "Mas você só tá de brincadeira."

            g "..."

            o "Você só brinca comigo, Ju..."

            g "Ok, tá bom. Desculpa. Vamos tomar um banho?"

            o "Tá."

            "Opa. Melhor dar o fora daqui."
        "Melhor não abusar da sorte.":


            "Melhor não abusar da sorte por agora."

            "Vou esperar elas irem para o vestiário."

            jump julia_e3_vestiario

    label julia_e3_vestiario:

        scene uni_hall corredores with Dissolve(1.0)

        show mc pensando with dissolve

        "Esse negócio de detetive tá me deixando nervoso de verdade."

        if j3_ouviu_p2:

            "Aquela conversa das duas foi bem interessante."

            "A forma que a [g] olha pros homens é realmente problemática."

            if v4_fim:

                "Ela me lembra até um pouco a [j]..."

                "Esse negócio de usar tudo e todos pra conseguir seus objetivos."

                "Mas de alguma forma não é a mesma coisa. A [g] não parece tão obstinada como a [j]."

                "Parece que é mais como se ela quisesse estar no controle..."

            "Minha investigação está indo muito bem por enquanto. Preciso continuar nessa pega."
        else:


            "Eu acabei não ouvindo o que elas conversaram na quadra, mas tudo bem."

            "Melhor ir devagar."

            "Vou esperar elas saírem e daí vejo qual é o próximo passo."

            "..."

            "..."

            "Elas tão saindo!"

            hide mc with dissolve

            "..."

            show julia hall_falando with dissolve

            g "Eu adoro tomar uma ducha depois do treino!"

            g "Vem!"

            hide julia with dissolve

            "Elas tão indo pro vestiário!"

            show mc pensando with dissolve

        "Bisbilhotar as duas no vestiário..."

        "Será que eu realmente deveria fazer isso? Se a [g] me pegar lá vai ser terrível."

        "E agora?"

        menu:
            "O vestiário é demais. Melhor não!":


                hide mc with dissolve

                mc envergonhado "Acho que olhar elas no vestiário seria demais..."

                "Não sei se quero me rebaixar desse jeito."

                "Mas o tanto de coisa que eu poderia descobrir..."

                if julia_seducao >= 9:

                    "E talvez até dê pra ver elas peladinhas..."

                    mc tarado "..."

                "Só que e se a [g] ou a amiga dela me verem lá?! Seria o fim pra mim!"

                "Preciso pensar muito bem o que eu faço! AAAHHH!"

                menu:
                    "De forma alguma. Não quero investigar ela lá.":


                        "Não consigo. É demais. Vai que elas me pegam. Seria vergonha demais."

                        "Além de que não é coisa que um cavalheiro faria."

                        "Não vou me rebaixar desse jeito."

                        "Vou esperar elas saírem."

                        scene uni_hall geral with Dissolve(1.0)

                        "..."

                        "..."

                        "..."

                        mc zerado "Acho que eu devia ter ido ver ela lá. Que demora..."

                        "..."

                        "Opa! Tô vendo a [g] ali!"

                        "Ixi. Ela me viu também. Ela não tá com uma cara muito boa..."

                        jump julia_e3_pre_final
                    "Mesmo não sendo o melhor, vale a pena.":


                        "Eu sei que não é educado fazer algo assim, mas eu estou aqui pra saber sobre ela."

                        "Tudo isso vai valer à pena se eu conseguir a [g] depois."

                        "Força, [mc]!"
            "Quem não arrisca não petisca.":


                "Eu sei que não é educado fazer algo assim, mas eu estou aqui pra saber sobre ela."

                "Tudo isso vai valer à pena se eu conseguir a [g] depois."

                "Ou pelo menos é o que eu tô tentando me convencer..."

                "Será que realmente tá certo isso?"

                "Agora não é hora de ficar viajando!"

                "Força, [mc]!"

                hide mc with dissolve

    "Certo. Agora tá decidido. Preciso tomar muito muito cuidado."

    "Elas já devem estar lá."

    "Deixa eu dar uma olhada ver se não tem ninguém vindo."

    "..."

    "Beleza! Agora é a hora! Rápido!"

    scene uni_vestiario geral with hpunch

    pause

    "Tô dentro. E parece que ninguém me viu. Eu sou muito bom!"

    "Mas o pior começa ago-"

    g "{size=13}... vergonha de mim, [o]? Eu não vou te morder.{/size}"

    o "{size=13}Ai, Ju... tá...{/size}"

    mc surpreso "!"

    "O que elas tão falando lá?"

    "Merda... será que eu tento me aproximar?"

    "Agora que eu tô aqui não adianta pensar. Se é pra investigar, vou até o fim."

    "Vou tentar me escorar em um dos armários..."

    "Sem fazer barulho..."

    call j3_calculo from _call_j3_calculo_4

    "Aqui eu tô muito bem. E elas não conseguem me ver. Pelo menos eu espero..."

    $ j3_ouviu_p3 = True

    "Vamos dar uma olhada..."

    scene julia vestiario_4olhos with Dissolve(2.0)

    pause

    mc surpreso "!"

    "Elas tão tirando a roupa... o que eu tô fazendo aqui?!"

    g "Seu corpo é muito gostoso, [o]. É a primeira vez que consigo ver ele assim."

    o "Ai, não fala assim..."

    o "E eu não acredito nisso..."

    g "Eu tô falando sério! Seus peitos são lindos. E você é magrinha. E até tem bunda."

    g "Tá dando até raiva agora! Como uma pessoa pode ter gordura só nos lugares certos?"

    o "Você tá exagerando, [g]. Você também é muito... {size=10}gostosa{/size}."

    g "Você me chamou de gostosa?!"

    o "..."

    g "Valeu, [o]!"

    g "Pra ficar 10, agora você só precisava tirar os óculos, passar uma maquiagem, soltar o cabelo, usar uns cremes e talvez academia."

    o "..."

    g "Não precisa fazer essa cara!"

    o "Você acabou de me criticar um monte, sabia? Me chamou de 4 olhos, flácida, cabelo de bruxa..."

    g "E desde quando é fácil ser gostosa?"

    o "Pra você falar é fácil, que é assim... toda..."

    g "Eu sei que sou gata. Mas não é fácil. Eu me esforço bastante, sabia?"

    o "Imagino... Desculpa..."

    g "Não queria fazer pouco de você também. É que tá tão fácil pra você."

    o "..."

    g "Mas, olha, [o]. Ser bonita e bem cuidada não é tudo."

    g "Os homens vão continuar sendo babacas com você. E até as garotas começam a te olhar torto."

    o "Parece que você tá reclamando de problemas do primeiro mundo..."

    g "Não é isso! Só queria que você soubesse que... você é linda do jeito que você é."

    o "O-obrigada..."

    g "Esse negócio de sofrer pra ser gostosa e bonita, sei lá, não é pra todo mundo."

    g "Eu acho que só quem realmente gosta disso que deveria fazer."

    g "Se matar de se cuidar por causa dos outros é trabalhoso demais e não sei se vale a pena."

    o "O problema é que na maioria das vezes só nós que somos garotas que sofremos com isso."

    o "A maioria dos garotos adora uma garota bonita e cheirosa mas não fazem nada..."

    g "Homens são os piores. Eu falo pra você..."

    o "..."

    o "Ju... eu tava pensando aqui... Você não tá falando tudo isso por causa daquele [mc], né?"

    g "Quê?! Claro que não! Afe!"

    o "Sei..."

    o "Você parecia bem interessada nesse rapaz uns tempos atrás. E de repente você tá assim."

    o "Começou a falar comigo {b}recentemente{/b}..."

    g "Para de viajar, [o]!"

    "Então quer dizer que a [g] começou a falar com essa amiga {b}recentemente{/b}..."

    "E parece que ela tava falando de um [mc]... Será que sou eu?"

    g "Chega de papo! Vamos pro banho!"

    o "Tá..."

    scene uni_vestiario geral with hpunch

    "Elas tão vindo nessa direção. E agora?!"

    menu:
        "Escapar pra fora do vestiário":


            "O melhor é eu sair daqui."

            "Pera! Tem um lugar fora de vista ali."

            "Opa!"

            scene uni_vestiario escondido with dissolve

            g "..."

            o "..."

            "Ufa... daqui não consigo escutar elas conversando, mas pelo menos não vou ser pego."

            "Acho que é a melhor decisão."

            jump julia_e3_vestiario_fim
        "Tentar encontrar um lugar pra se esconder":


            "Preciso agir rápido, não dá tempo de sair."

            "E agora?!"

            "Pra onde eu vou?!"

            mc angustiado "..."

            "Já sei!"

            scene uni_vestiario armario with vpunch

            pause

            "{i}puf puf{/i}"

            "Acho que tô bem aqui..."

            g "Você escutou alguma coisa?"

            mc "..."

            o "Escutei. Parece que bateram no armário."

            "Tô fodido!"

            o "Que medo..."

            g "Calma que eu vou dar uma olhada."

            call j3_calculo from _call_j3_calculo_5

            g "Acho que não é nada. Deve ter sido o vento."

            "Não acredito... Consegui... Dessa vez eu achei que tinha ido pro saco."

            play sound "audio/som_16_chuveiro.mp3"

            "Elas vão tomar banho..."

            scene uni_vestiario armario_banho with Dissolve(2.0)

            pause

            mc surpreso "!"

            o "Agora fiquei pensando aqui... E se tiver um tarado olhando a gente?"

            g "Por que tá falando isso?"

            o "Por causa do barulho."

            g "Se tiver um tarado, deixa ele olhar. Será que ele tá gostando da vista?"

            o "Ju! Que absurdo!"

            g "Que foi? É sério... eu não ligo nem um pouco."

            o "Eu ligo! Eu nunca respeitaria um rapaz que se esconde pra ficar xeretando mulheres peladas."

            o "Isso é nojento!"

            mc triste "..."

            g "Você leva isso tudo à sério demais..."

            g "Deixa eu te mostrar que não tem problema nenhum. Vou pegar no seu peito."

            o "Sai pra lá!"

            g "Vem aqui!"

            scene uni_vestiario armario with dissolve

            mc zerado "Essa [g]..."

            "Elas tão correndo pelo lugar! É minha chance de dar o fora!"

            "Rápido!"

            scene uni_vestiario escondido with hpunch

            $ renpy.vibrate(1)

            "{i}Blammm{/i}"

            "Droga! Que barulhão!"

            "Júlia e Carol" "Ai!"

            o "O que foi isso?!"

            g "Quem tá aí?!"

            mc preocupado "..."

            "Merda merda merda..."

            g "Fala logo!"

            g "{size=10}Vou dar uma olhada... xiu...{/size}"

            "Tenho que ficar quieto... Calma... calma..."

            call j3_calculo from _call_j3_calculo_6

            g "{size=10}Não vi nada...{/size}"

            o "Ufa. Acho que não tem nada então."

            g "É. Eu falei. Deve ter sido só um vento forte."

            "Mano, essa foi por pouco."

            o "Você viu o que a Maria fez ontem?"

            g "Nossa, que rídicula! Hahaha!"

            o "Eu não tava falando no sentido de zoeira..."

            "Elas parecem bem animadas. Talvez eu consiga me aproximar."

            "Merda, [mc]... você tá falando sério?"

            "Eu tô tão nervoso que tô falando comigo mesmo. Minhas mãos tão suando."

            menu:
                "Ficar escondido e esperar elas terminarem":


                    "Não vou arriscar tudo o que eu consegui e ser pego xeretando duas garotas no banho. Vou ficar de boa aqui."

                    jump julia_e3_vestiario_fim
                "Tentar se aproximar dos chuveiros":


                    "Foda-se os riscos! Quem não cola não sai da escola. Preciso ter coragem se eu quiser saber mais sobre ela."

                    "Ou ver ela no banho..."

                    mc tarado "..."

                    "Ok... Com muita calma..."

                    "Bem devagar..."

                    "..."

                    play sound "audio/som_16_chuveiro.mp3"

                    scene uni_vestiario escondido2 with Dissolve(2.0)

                    "Meu Deus, eu tô muito perto delas..."

                    "Um passo em falso aqui e já era tudo. Por que eu resolvi vir aqui?"

                    o "Ju, eu ainda tô meio nervosa com o tarado."

                    g "Quer que eu dê uma olhada de novo?"

                    o "Se não for-"

                    g "Não se preocupe. Deixa que eu te salvo."

                    o "Minha heróina!"

                    "Bosta! Isso ainda vai acabar sobrando pra mim. Dessa vez eu fui longe demais."

                    "Espero que ela não esteja vindo pra cá. Preciso me esconder o máximo que eu puder."

                    "..."

                    call j3_calculo from _call_j3_calculo_7

                    g "É. Não tem nada mesmo."

                    $ j3_ouviu_p4 = True

                    o "Que estranho. Eu continuo sentindo como se tivesse alguém por aqui."

                    g "Pior é que eu também tô."

                    "Elas não são adversárias à altura das minhas habilidades. Eu sou um ninja. Ninguém pode me ver..."

                    mc zerado "..."

                    "Acho que eu tô fazendo papel de ridículo agora."

                    o "E o que você planeja fazer sobre o idiota do {b}Caio{/b}?"

                    g "Que que tem ele?"

                    o "Eu vi que ele não larga do seu pé."

                    g "Pois é. Eu dei umas vezes pra ele, mas agora acabou. Só que ele não entende isso."

                    o "Não sei como você aguenta, ele se jogando em cima de você. Que cara sem noção."

                    g "Vou falar o quê? Eu também não gosto quando ele fica pegando em mim, mas é da natureza deles."

                    "Então a [g] tá sendo assediada por esse idiota chamado {b}Caio{/b}. Acho que essa é outra informação importante."

                    o "Lá vem você com essa história de que os homens são a escória."

                    g "Mas não são?"

                    o "Eu acho que eu nunca vou entender a forma que você vê os rapazes. A gente é tão diferente nisso."

                    g "Eu acho normal. As coisas que eu e você passamos são bem diferentes."

                    o "Você tem razão. Acho que são as coisas que a gente passa que fazem a gente gostar ou não de alguma coisa."

                    g "Aí já filosofou demais."

                    o "Idiota..."

                    g "Quer que eu pegue nos seus peitões de novo? Me provoca!"

                    o "Sai [g]!"

                    "Elas tão entretidas de novo. É minha chance de ver..."

                    "Será que..."

                    mc tarado "Será?"

                    menu:
                        "Sim.":


                            $ j3_banho = True

                            "Eu já vim até aqui. Não vou perder a chance de ver as duas tomando banho."

                            "A questão vai ser fazer isso sem ser visto."

                            "..."

                            call j3_calculo from _call_j3_calculo_8

                            scene julia vestiario_banho with Dissolve(2.0)

                            pause

                            "Já posso morrer feliz..."

                            o "É a primeira vez que eu tomo banho com outra pessoa..."

                            g "Sério?"

                            o "Você já tomou?"

                            g "Algumas vezes eu tomo com a minha irm-"

                            g "Eu tomo com o pessoal que eu fico. Alguns deles são limpinhos, né."

                            o "Bom pra você..."

                            g "Mas acho que esta é a vez mais legal."

                            o "Por que?"

                            g "Porque eu gosto de você."

                            o "!"

                            o "Xavequeira..."

                            g "..."

                            window hide

                            pause



                            label j3_premium1:

                                pass

                            "Se eu continuar aqui com certeza elas vão me pegar..."

                            "Só que... quando eu vou ter outra chance dessa pra ver elas peladinhas desse jeito?"

                            "Se me pegarem fodeu... mas se eu conseguir..."

                            menu:
                                "Continuar olhando":








                                    "Não dá pra ir embora assim. Eu quero ver mais um pouquinho..."

                                    "Se eu conseguisse me aproximar..."

                                    scene black with dissolve

                                    "Atrás desse chuveiro aqui..."

                                    scene j3_new1 with Dissolve(1.0)

                                    pause

                                    "Não acredito! Que visão dos deuses! Camarote vip!"

                                    o "[g]..."

                                    g "Oi, linda."

                                    "Elas ainda tão conversando..."

                                    o "Quando você disse que gostava de mim... você tava brincando, né?"

                                    g "Claro que não. Você sabe que eu realmente gosto de você, bebê."

                                    o "E-eu também gosto de você."

                                    "Q-quê?!"

                                    g "Mas não do jeito que eu gosto de você."

                                    o "V-você... v-você tá falando s-sério?"

                                    g "É."

                                    o "Mas e o Caio? E-ele não é seu namorado?"

                                    g "Você sabe como é... eu e o Caio às vezes tá, às vezes não tá."

                                    g "Mas eu não tenho problema em namorar vocês dois."

                                    o "Q-que absurdo! Tá vendo?!"

                                    g "Vai me dizer que... hmm..."

                                    o "P-pare de pensar besteira."

                                    g "Você tava cogitando a gente ficar juntas mesmo? Que fofa!"

                                    o "Claro que não!"

                                    g "Você merece um abraço! Vem aqui!"

                                    scene j3_new2 with hpunch

                                    mc surpreso "!"

                                    o "!!!"

                                    g "Você merece todo um carinho meu."

                                    o "J-júlia! Me solta!"

                                    g "Como assim?! Eu sei que você quer! Você disse!"

                                    o "P-pode ter alguém aqui!"

                                    g "Só tem a gente, boba."

                                    o "M-mesmo assim! Eu não quero i-isso!"

                                    g "Eu vou saber cuidar de você, bobinha!"

                                    o "Hm!?"

                                    g "Olha pra essas tetas gigantes! Elas precisam de uma pegada forte."

                                    o "A-ai!"

                                    g "Elas são bem molinhas e cheias de carne. Você parece uma vaca."

                                    o "AAH! Q-que que eu tô ouvindo?!"

                                    g "Tô mentindo? Olha pra esse peitão de vaca. Você deve sentir muito gostoso quando eu pego assim."

                                    "A [g] tá praticamente obrigando a amiga dela a fazer isso. Será que eu deixo isso continuar?"

                                    "Eu posso fazer um barulho e salvar a garota..."

                                    menu:
                                        "Tentar interromper as duas":


                                            "É minha obrigação salvar a moça. A [g] pega pesado demais."

                                            scene black with dissolve

                                            scene uni_vestiario geral with dissolve

                                            "Com cuidado... agora a porta..."

                                            "{i}inheeeec{/i}"

                                            "Agora!"

                                            "{i}BLAM!!!{/i}"

                                            "Carol e Júlia" "HUH!"

                                            "Carol e Júlia" "T-tem alguém! Para para!"

                                            g "Que merda..."

                                            "Deu certo. Agora chega."
                                        "Continuar assistindo":


                                            "E-eu que não vou me meter nessa... bora ver onde vai dar."

                                            o "Ahn..."

                                            g "Agora que você tá entrando no clima, bora preparar a perigosa."

                                            o "P-perigosa?"

                                            scene j3_new3 with hpunch

                                            g "Bem aqui!"

                                            o "A-ahnn!"

                                            o "Onde você tá passando a mão?!"

                                            g "No seu lugarzinho mais gostoso, ué."

                                            o "J-júlia... você tá brincando demais! Chega!"
                                            scene jnew_ani15 with Dissolve(1.0)
                                            g "Você fala isso, mas eu sei que tá gostando. Eu tô sentindo."

                                            o "Não é assim que eu quero! Você tá me invadindo!"

                                            g "Só fecha os olhos e foca no prazer. Logo logo você não vai querer mais parar."

                                            o "Não fala desse... jeito... ahn..."

                                            g "Tá vendo? Não é bom?"

                                            o "N-nãounn... ahnn..."

                                            scene j3_new4 with Dissolve(1.0)

                                            g "Eu sabia que você ia gostar."

                                            o "N-nannn... ahnn... su-sua mão... agnn!"

                                            g "Isso! Você tá quase lá, gatinha. Você vai gozar gostoso!"
                                            scene jnew_ani17 with Dissolve(1.0)
                                            o "Minha nossa! Aahnn! Aahnng!"

                                            g "Goza pra mim, docinha! Mela meus dedos!"

                                            o "O que é isso?! AHN! Tá vindo! J-júlia!"

                                            g "Vem! Pode vir!"

                                            o "Ahng! Ahnn! AAHNNN!"

                                            scene j3_new4 with vpunch

                                            o "AAAHNHNN!"

                                            g "Que delícia! Como goza gostoso!"

                                            o "Ahnn... ah..."

                                            g "Gostou?"

                                            o "S-sua..."

                                            scene black with dissolve

                                            scene j3_new5 with Dissolve(1.0)

                                            o "Que m-merda foi essa, [g]!? Eu mandei você parar!"

                                            g "Sua boca falou uma coisa... mas seu quadril queria outra coisa... se mexendo daquele jeito."

                                            o "Absurdo! Nunca mais faça uma coisa dessas!"

                                            g "Só se voc-"

                                            o "[g]! Isso que você fez é crime! Isso é assédio sexual!"

                                            g "Calma lá... eu só queria te agradar."

                                            o "Me agradar?! Se eu mandar você parar você tem que parar!"

                                            g "Só qu-"

                                            o "Não importa o que você acha que eu quero! Isso que é o pior!"
                                            scene jnew_ani16 with Dissolve(1.0)
                                            o "Se uma pessoa fala que não quer, você tem que parar NA HORA!"

                                            g "Mas e se ela qu-"

                                            o "Eu não quero ouvir mais nenhum um 'A' sobre o que você acha!"

                                            g "Ok, bravinha..."

                                            o "E não faça graça!"

                                            g "Tá... tá... bora sair daqui de uma vez..."

                                            "Opa..."
                                "Nah. Perigoso demais.":


                                    "Deixa quieto."

                            "Já curti mais do que eu devia. Melhor eu dar o fora daqui."

                            "Vou voltar pro meu esconderijo e esperar elas acabarem."

                            scene uni_vestiario escondido with Dissolve(1.0)

                            jump julia_e3_vestiario_fim
                        "Melhor não.":


                            "Não tenho porque fazer isso. Já consegui ouvir tudo o que eu precisava."

                            "Vou voltar pro meu esconderijo e esperar elas acabarem."

                            scene uni_vestiario escondido with Dissolve(1.0)

                            jump julia_e3_vestiario_fim

    label julia_e3_vestiario_fim:

        $ j3_cena = True

        "..."

        "..."

        "Minha investigação tá indo muito bem por enquanto."

        "Eu descobri muito sobre a [g] hoje. Mas depois eu penso sobre isso."

        "Agora eu preciso me concentrar. Parece que elas terminaram o banho."

        o "Ju, eu tenho que falar com o Otávio sobre aqueles exercícios. Você me espera na biblioteca?"

        g "Droga..."

        o "Você prometeu!"

        g "Tá bom... Eu vou só porque foi muito bom ver você peladinha assim."

        o "[g]..."

        g "Que foi? Já falei que você é linda."

        o "Tá, mas assim parece que você tá dando em cima de mim de novo..."

        g "E se eu estiver?"

        o "O que eu te disse lá atrás?! Não exagera!"

        g "Hmmm... lá atrás..."

        o "N-não me deixa sem jeito. Vou lá e te encontro na biblioteca. Se não tiver lá, nem fala mais comigo."

        g "Tá bom, chefe..."

        o "Beijos."

        g "Beijo, gata."

        "Opa, a [g] tá se aproximando."

        g "Ver a [o] pelada e depois pegar nos peitos dela me deixou toda excitada."

        g "Queria fazer uma safadeza hoje."

        "Parece que ela tá aqui do lado."

        g "Vamos ver se alguém quer fazer uma baguncinha comigo..."

        scene julia vestiario_deitada with Dissolve(2.0)

        pause

        if julia_seducao >= 9:

            "Como essa garota mexe comigo..."

            "Ela realmente é muito gata. Isso ninguém pode negar."

        "Tadinha da outra menina. Certeza que a [g] não vai estudar com ela. Como ela planeja se formar desse jeito?"

        "Quem será que ela vai chamar? A [g] deve ter uma porr-"

        play sound "audio/som_3_celular.mp3"

        $ renpy.vibrate(1)

        "Smartphone" "Trrrr... trrrr..."

        mc surpreso "Eita!"

        g "Ah?!"

        scene uni_vestiario escondido with hpunch

        g "Tarado?! É você?!"

        "Merda!"

        g "Eu escutei! Quem tá aí?!"

        "Droga droga droga droga droga droga droga!"

        "Agora não tem como eu negar. O que eu faço?!"

        g "Não adianta se esconder! Eu ouvi o celular!"

        "Merda! Ela tá vindo. Vou ter que sair correndo e rezar pra ela não ver!"

        jump julia_e3_descoberto

    label julia_e3_final:

        if j3_ouviu_p1 or j3_ouviu_p2 or j3_ouviu_p3 or j3_ouviu_p4:

            $ j3_uma_pergunta = True

        "Que merda..."

        "Não tinha como eu continuar lá. Agora tenho que rezar pra que ela não tenha visto minha cara."

        if j3_cena:

            "Então de todas as pessoas que ela sai, ela resolveu ligar bem pra mim..."

            "Nunca passou pela minha cabeça que a [g] estava tão ligada assim em mim."

            "Isso me deixa feliz por um lado."

            "Se bem que é possível que ela só me veja como um objeto pra satisfazer as vontades dela."

        "Não acredito! Ela tá vindo pra cá!"

        "Ela tá olhando direto na minha direção. Agora eu marquei, não tenho como sair da faculdade. Ela já deve ter sacado tudo."

        label julia_e3_pre_final:

            "..."

        show garconete e_emburrada with vpunch

        g "{i}hmph{/i}"

        mc envergonhado "Oi, [g]."

        g "Que oi o quê?"

        g "O que você tá fazendo aqui?"

        menu:
            "Eu vim procurar você.":


                mc charmoso "Eu vim procurar você. Ver como você tava."

                show garconete e_sexy with dissolve

                g "Tava com saudades de mim, é? Saudades desse corpinho aqui?"

                mc envergonhado "..."
            "Vim resolver um negócio do diploma do meu curso.":


                mc envergonhado "Na verdade eu vim resolver um problema com meu diploma. A faculdade que me chamou."

                g "Hmm... E conseguiu resolver?"

                mc normal "Consegui."

                g "Que bom."
            "Não te interessa.":


                mc desculpa "Não te interessa."

                g "Como assim não me interessa? Você aparece aqui na minha faculdade e sai correndo?"

                g "O que tá pegando?"

                mc "Não tem nada a ver com você. É assunto meu e da faculdade."

                g "Você tá cheio de misteriosinho..."

        mc envergonhado "Mas eu fico feliz em ver você. Tá tudo legal?"

        show garconete e_provocando with dissolve

        g "..."

        mc desconfiado "Que foi?"

        g "Por acaso você não tava me seguindo pela faculdade, né?"

        "Não tenho coragem pra revelar isso pra ela. É vergonhoso demais."

        mc surpreso "Eu?! Como assim?!"

        g "Parece que eu vi alguém me seguindo, e vendo você aqui agora..."

        mc envergonhado "De forma alguma. Eu não faria isso..."

        g "Hoje eu não tive aula. Eu tava indo pra biblioteca esperar uma amiga. O que acha de sentar comigo?"

        mc normal "Claro. Vamos lá."

        g "Me segue."

        mc zerado "Eu sei onde fica."

        g "Me segue mesmo assim."

        mc "..."

        hide garconete with dissolve

        "..."

        scene uni_biblioteca geral with Dissolve(1.0)

        show garconete e_provocando with dissolve

        g "Agora que só tá a gente aqui, pode falar a verdade."

        mc envergonhado "Como assim a verdade?"

        g "Você tava seguindo eu e a minha amiga."

        mc "Tá com isso na cabeça ainda?"

        g "Senta aqui."

        scene julia biblioteca_cena1 with Dissolve(2.0)

        pause

        g "Eu acharia bem sexy se você tivesse me seguindo."

        mc desconfiado "Sexy? Por que?"

        g "Mostra que você tá interessado em mim. E um homem atencioso sempre ganha pontos."

        "E agora? Será que ela tá falando sério ou só quer me pegar no flagra?"

        mc envergonhado "Eu-"

        if not j3_uma_pergunta:

            g "Tudo bem vai..."

            mc desconfiado "Que foi?"

            g "Eu sei que você não ia fazer uma coisa dessas."

            "Tá certo que eu vim aqui com a intenção de investigar ela, mas eu não ouvi nenhuma informação importante."

            "Então posso dizer que eu realmente não xeretei nada."

            jump julia_e3_amizade
        else:


            g "Espera. O que você acha da gente fazer um jogo?"

        g "Eu tenho a impressão de que eu te vi em alguns lugares durante a noite..."

        "Impossível! Será que ela me viu e me deixou seguindo ela de propósito?!"

        mc "Não sei do que você tá falando."

        g "Vamos aproveitar que não tem ninguém aqui na biblioteca e apimentar as coisas."

        g "O jogo é assim. Como eu acho que você tava me xeretando, eu vou fazer perguntas sobre o que eu conversei com a [o] hoje."

        g "Você pode fingir que não sabe a resposta, é um direito seu. Só que pra cada resposta certa eu vou te mostrar uma parte do meu corpo."

        g "Quem sabe até tirar umas peças de roupa. O que me diz?"

        menu:
            "Ok. Combinado.":


                jump julia_e3_jogo

            "Não quero jogar isso." if julia_seducao < 15:

                mc charmoso "Não tenho porque jogar esse jogo. Eu não bisbilhotei, então não tenho como responder nada."

                g "Você entendeu como funciona, né? Vai realmente perder a chance de me ver sem roupa?"

                "Falando desse jeito ela tá me fazendo pensar duas vezes..."

                menu:
                    "Não quero!":


                        "Não adianta ela me provocar, não quero."

                        mc charmoso "Não quero mesmo, [g]. Você sabe que você é linda, mas realmente não tenho como responder."

                        jump julia_e3_amizade
                    "Tudo bem! Eu vou jogar.":


                        "Melhor entrar na brincadeira dela. Aparentemente eu não tenho nada a perder."

                        jump julia_e3_jogo

    label julia_e3_jogo:

        $ j3_jogo = True

        mc charmoso "Certo. Eu vou jogar com você."

        g "Eba!"

        g "Eu tô bem excitada, [mc]. Espero que você saiba tudo o que eu perguntar."

        mc envergonhado "Vamos ver..."

        g "Vou começar pelo começo."

        g "Quando eu e a minha amiga [o], que eu acho que você já conhece... a gente tava no corredor. E eu falei pra ela de uma prova."

        g "Você consegue se lembrar da matéria que era essa prova? Se você ouviu, você vai saber."

        if j3_ouviu_p1:

            "Elas estavam conversando no corredor, logo depois que saíram da biblioteca."

            "Foi a primeira coisa que eu ouvi."

            mc charmoso "Você vai ter uma prova sobre Biologia Marítima. Tenho certeza."

            $ j3_investigou += 1

            call j3_avaliacao from _call_j3_avaliacao
        else:


            "Ixi, não sei sei. Acho que eu não tava escutando quando ela comentou desse assunto."

            mc envergonhado "Não sei do que você tá falando. Eu disse que eu não tava xeretando..."

            g "A é?"

        g "Certo. A segunda pergunta é sobre meu curso. Na quadra, eu conversei com a [o] e disse pra ela o que eu estudo."

        g "Se você tava prestando atenção, tenho certeza que você vai saber qual é meu curso."

        if j3_ouviu_p2:

            "Hmmm... eu lembro que ela disse que o sonho dela era se tornar bióloga."

            "Lá durante o exercício na quadra ela disse sobre o sonho dela e sobre Biologia. Tem que ser isso."

            mc charmoso "Você cursa Biologia. Inclusive, seu sonho é ser bióloga e estudar animais pelo mundo."

            $ j3_investigou += 1

            call j3_avaliacao from _call_j3_avaliacao_1
        else:


            "Não tô lembrando disso. Acho que eu não tava escutando quando ela comentou desse assunto."

            mc envergonhado "Não sei do que você tá falando. Eu disse que eu não tava xeretando..."

            g "Sei..."

        g "Agora a terceira pergunta. Lá no vestiário..."

        g "Espera... Será que você seguiu a gente até o vestiário, safado?"

        mc envergonhado "Claro que não..."

        g "Tá. Se por um acaso você seguiu, você sabe há quanto tempo eu falo com a [o]."

        g "Pode responder essa?"

        if j3_ouviu_p3:

            "Eu lembro. Elas tavam se trocando antes de tomar banho."

            mc charmoso "A [o] disse que vocês começaram a conversar recentemente."

            g "E fala assim na cara dura. Não tem nem vergonha de ficar olhando duas garotas nuas no vestiário?"

            mc envergonhado "Não sei do que você tá falando..."

            $ j3_investigou += 1

            call j3_avaliacao from _call_j3_avaliacao_2
        else:


            "Sei lá do que ela tá falando... Acho que eu não tava escutando quando ela comentou desse assunto."

            mc envergonhado "Não sei do que você tá falando. Eu disse que eu não tava xeretando..."

            g "Então não tava mesmo..."

        g "E, por último, essa aqui é só pros tarados de verdade."

        "Certeza que ela vai perguntar algo de quando elas estavam tomando banho."

        mc envergonhado "..."

        g "Quando a gente tava tomando banho..."

        "Sabia..."

        g "Eu falei o nome de um idiota que tá me perseguindo ultimamente. Você sabe o nome dele?"

        if j3_ouviu_p4:

            "E o pior é que eu lembro..."

            mc desculpa "O nome dele é Caio..."

            g "Você realmente xeretou a gente até no banho!"

            call j3_avaliacao from _call_j3_avaliacao_3
        else:


            "Não faço a mínima ideia. Acho que eu não escutando quando ela comentou desse assunto."

            mc envergonhado "Como posso saber isso? Eu disse que eu não tava xeretando..."

            g "Que estranho... será que você tá me enganando?"

        label julia_e3_amizade:

            $ julia_e3 = "amizade"

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("julia_e3_amizade","julia","personagem")

        g "Bom. Parece que você realmente falou a verdade e não tava me xeretando."

        mc normal "Eu falei. Eu não faria uma coisa dessas."

        g "Por um lado eu fico triste... só que isso mostra que você realmente é um cavalheiro."

        if sayuri_e4 == "namoro":

            g "Eu sei que as coisas entre você e a mana tão ficando cada vez mais sérias."

            g "Ela me falou do beijo de vocês na Cidade Chinesa."

            g "Depois eu queria falar com você sobre tudo isso."

            mc normal "Claro. Não vou passar por cima de você."

        g "Eu também quero um pedaço desse cavalheiro, eu acho... mas..."

        g "Epa. Parece que a [o] tá chegando aí. Ela é uma amiga minha."

        g "Eu já falei de você pra ela. Só não seja um babaca."

        mc zerado "Mas quando que eu... esquece..."

        jump julia_e3_fim

    label j3_avaliacao:

        if j3_investigou == 1:

            scene julia sentada_parte1 with Dissolve(2.0)

            pause

            g "Sei... então você realmente ficou me ouvindo..."

            mc charmoso "Não sei do que você tá falando..."

            g "Tô com um calor aqui embaixo. Tá vendo?"

            mc "..."

            g "Preciso deixar ela bem ventilada."

            mc "Sei..."

        elif j3_investigou == 2:

            g "Acho que só abrir as pernas não vai ser suficiente, sabe?"

            mc charmoso "Não?"

            g "Não... vou ter que tirar isso aqui de uma vez."

            scene julia sentada_parte2 with Dissolve(2.0)

            pause

            g "Bem melhor..."

            mc envergonhado "Que bom..."

            g "Tô pensando em você lá quietinho, só de olho em mim, com medo de ser pego."

            g "Tão fofo..."

            g "Tá me deixando mais quente ainda. Deixa eu ficar mais à vontade."

            g "Tô te incomodando?"

            mc charmoso "Claro que não."

            g "Ai, que bom. Porque tá gostoso ficar assim."

            mc "..."

        elif j3_investigou == 3:

            g "Ainda não acredito que você ficou todo esse tempo seguindo a gente pela universidade..."

            g "Acho que nunca um rapaz fez uma coisa tão extrema por mim, assim."

            g "Entrar no vestiário só pra poder me xeretar."

            "Acho que nesse ponto não adianta mais eu querer negar. Já tá na cara que eu persegui durante toda a noite."

            "E minha sorte é que estranhamente ela parece tá gostando."

            mc charmoso "Eu queria saber mais sobre você."

            g "Você é muito fofo. E tá me deixando muito excitada."

            g "..."

            scene julia sentada_parte3 with Dissolve(2.0)

            pause

            g "Agora sim... Assim ficou bom, não acha?"

            mc safado "Eu acho que ficou excelente."

            "Essa [g] é doida. Imagina se alguém entra agora?"

            g "Eu tranquei a porta por dentro, bobinho..."

            mc envergonhado "Como você sabe que eu..."

            g "Eu consigo ler você como uma história em quadrinhos. Mais fácil que ler um livro."

            mc "..."

            g "Tá gostando de me ver assim?"

            mc safado "Com certeza."

            g "Acho que já tá bom. Não preciso perguntar mais nada. Você passou no teste."

            mc "Passei, é?"

            g "Sim. Vou te dar uma recompensa e tanto."

            g "Senta direito que eu vou lhe usar."

            "A [g] vai querer transar aqui bem no meio da biblioteca. E agora?"

            g "Deixa que eu cuido de tudo. Só-"

            jump julia_e3_jogo_after

        return

    label julia_e3_jogo_after:

        $ julia_e3 = "seducao"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("julia_e3_seducao","julia","personagem")

        "{i}TUDUMP{/i}"

        mc surpreso "Tem alguém!"

        "{i}TOC TOC{/i}"

        g "Só pode ser a [o]! Ela é a única que usa a biblioteca."

        o "Ei! Abre a porta agora ou vou chamar o inspetor!"

        scene uni_biblioteca geral with vpunch

        g "Vai lá e enrola ela pra eu colocar a roupa!"

        g "Ela não pode chamar ninguém!"

        mc surpreso "O-ok!"

        "Deixa eu tentar parar ela no corredor."

        "{i}GA-TCHAK{/i}"

        scene uni_hall corredores with Dissolve(1.0)

        mc normal "Oi, jovem."

        show 4olhos nervosa with dissolve

        o "Oi... é... eu só queria usar a biblio-"

        mc normal "Não se preocupe que logo ela vai ser libera-"

        o "Com licença!"

        hide 4olhos with moveoutright

        mc surpreso "Não!"

        scene uni_biblioteca geral with vpunch

        "Droga, ela entrou! Deu merda."

        show 4olhos nervosa with dissolve

        o "Você que fechou a biblioteca?"

        mc desculpa "É... sim! Eu tava sentado bem aqui ó."

        scene 4olhos mc_sentado with Dissolve(1.0)

        mc "Tava aqui, lendo um livro."

        o "E por um acaso você não viu-"

        o "Epa. As coisas da [g] estão aqui na mesa. Eu conheço esse celular."

        mc envergonhado "Você tá falando de uma garota, com o mesmo uniforme seu... cabelo meio loiro, meio ruivo. Ah! Ela tava aqui."

        o "E pra onde ela foi?"

        mc "Hmmm..."

        scene julia mesa_vazia with dissolve

        mc desconfiado "Ela tava..."

        "Pra onde que a [g] foi? Ela simplesmente desaparece-"



        scene j3_new6 with vpunch

        mc surpreso "Quê?!"

        g "{size=13}xiu...{/size}"
        scene jnew_ani18 with Dissolve(1.0)
        "Que que essa doida ainda tá fazendo aí?"

        o "Moço..."

        mc "Opa!"

        scene 4olhos mc_sentado with Dissolve(1.0)

        mc preocupado "É..."

        mc envergonhado "Onde será que ela pode ter ido, né? Hehe..."

        o "Mas a porta não tava trancada?"

        mc "Sim, ela ta-"

        mc surpreso "Ack!"

        o "Que foi, moço?"

        "A [g] tá mexendo no meio das minhas-"



        scene j3_new7 with vpunch

        g "{size=13}Continua falando com ela que eu tenho uma surpresa...{/size}"



        mc "Q-quê? E-eu..."

        g "{size=13}Só tenta ser normal uma vez na vida!{/size}"

        mc desculpa "Então..."

        mc surpreso "É!! É QUE!!"

        o "Você tá legal? Será que você dormiu e não vi-"

        mc "POIS É!!"

        label j3_premium2:

            pass

        "A [g] tirou minha calça!"

        "Se eu continuar assim a garota aqui vai descobrir."

        "Mas perder um oral assim... merda... o que eu faço?"

        menu:
            "Deixar ela continuar":








                "Se ela quer devorar meu pau, não sou eu que vou reclamar."

                mc "Pode se deliciar..."

                o "C-como é?"

                mc "N-nada... desculpa..."

                scene j3_new8 with Dissolve(1.0)

                pause

                g "Eu vou sentir o sabor do seu caralho..."

                "Minha nossa... que boquinha quente..."

                g "Até que xeu pau é goxtoso..."

                "Foda-se se a garota ouvir ela... escutar a [g] falando com meu pau na boca é bom demais."

                o "Estranho que ela não apareceu ainda..."

                mc "V-verdade... o que será que ela tá fazendo? Hmm..."

                g "Eu tô prestes a mamar seu caralho, safado..."

                o "Estranho..."

                mc "N-não foi nada."

                scene j3_new9 with Dissolve(1.0)

                pause

                mc "A-ah!"

                o "Que foi?"

                g "{i}slhuuuuupp{/i}"

                "Ah! Que chupada deliciosa! Vai arrancar a cabeça do meu caralho assim..."

                g "Paun goxtoxoo! NNNHG!"

                mc "S-se ela co... digo, se ela continuar d-desaparecida... hmm..."

                mc "V-você devi... aahn... procurar ela."
                scene jnew_ani19 with Dissolve(1.0)
                o "É... depois do que aconteceu... a [g] deve tá com alguém."

                mc "V-você acha?"

                g "Eu txô bem axi xom voxê... gmm..."

                "S-se ela continuar assim..."

                mc "E-eu tô quase!"

                o "Quase?"

                mc "É... tô pensando aqui... onde ela pode tá... tô quase... lembrando de alguma coisa..."

                g "Fode minha garganta então!"

                scene j3_new10 with Dissolve(1.0)

                pause

                "Puta que pariu! Como ela faz isso?!"

                mc "A-anhg!"

                mc "Uh-uhhh!"

                o "Você tá zombando de mim?!"

                mc "Cla-claro que... naauunngg!"
                scene jnew_ani20 with Dissolve(1.0)
                o "Que gemido é esse?!"

                mc "AAAHHH! AAaahh..."

                o "Seu ridículo!"

                mc "Não espera!"

                mc "AHH! Foda-se! Eu vou gozar na sua garganta!"

                g "Podxe goxxar!"

                mc "NNNNGH!!"

                scene j3_new10 with vpunch

                mc "AAAHH!"

                g "NNNGN!! Quanta porra..."

                mc "Que delícia..."

                g "Agora espera... eu preciso também..."

                mc "Hm?"

                g "Deixa eu chegar lá também enquanto eu limpo seu caralho..."

                "Uou... ela merece depois de uma mamada dessas..."

                "Ou... eu deixo ela com vontade?"

                menu:
                    "Tá bom por hoje.":


                        mc "Nah... a gente já fez o suficiente."

                        g "Quê?!"

                        mc "Tô levantando."

                        g "Nem pense nisso, seu puto!"

                        mc "Você mamou demais pra um dia."

                        scene black with dissolve

                        g "Você me paga, filho duma égua!"

                        mc "Quem sabe depois... mas obrigado por me fazer gozar. Você foi uma boa garota."

                        g "Que seja... se você aproveitou, tá bom..."
                    "Pode gozar.":


                        mc "Pode gozar. Eu deixo."

                        scene j3_new11 with Dissolve(1.0)

                        pause

                        g "Hnn... é o mínimo... você deixar eu usar sua porra pra me fazer gozar."

                        g "Esse pau imundo... hmm... que delícia de porra..."

                        mc "J-júlia..."

                        g "Você tá crescendo de novo? Que lindo..."
                        scene jnew_ani22 with Dissolve(1.0)
                        g "Mas agora sou eu... nnng... eu adoro enfiar o dedo no buraquinho..."

                        mc "Como você é safada."

                        g "Eu... nng... eu sou só uma garota querendo diversão... aahnng."

                        g "Mas um pouco, deixa o pau aí.... vou lamber ele... nnnhgh..."

                        g "Annhh... annng!"

                        scene j3_new11 with vpunch

                        g "NNNG!"

                        mc "Gostou?"

                        g "Gozei... obrigado, pau... você não é grande coisa, mas ajudou..."

                        mc "Ei!"

                scene black with dissolve

                scene uni_biblioteca geral with Dissolve(1.0)

                g "Ufa..."
            "Chutar a [g]":


                "Não dá! Ela tem que acelerar!"

                "{i}TUDUMP{/i}"

                g "{size=13}Ai! Filha da puta!{/size}"

                mc "{size=13}Ela vai pegar a gente! Sai!{/size}"

                g "{size=13}Eu não vou parar agora!{/size}"

                "Se eu brigar com ela, daí que vai dar na cara. Agora eu vou curtir e torcer pra ela terminar rápido!"

                mc "{size=13}E-então vai logo!{/size}"

                mc "OOOHH!"

                o "O que foi, moço?! Você tá me assustando!"

                scene 4olhos mc_sentado with vpunch

                mc preocupado "Não foi nada..."

                scene julia mesa_mc with hpunch

                mc "Uh-uhhh!"

                o "Você tá zombando de mim?!"

                scene 4olhos mc_sentado with vpunch

                mc angustiado "Cla-claro que..."

                scene julia mesa_mc with hpunch

                mc "AAAHHH! AAaahh..."

                scene 4olhos mc_sentado with vpunch

                o "Seu ridículo!"

                scene uni_biblioteca geral with hpunch

                mc concentrando "Ah... aah..."

                mc "Não... por favor..."

                "Ela saiu correndo..."

        show garconete e_provocando with moveinbottom

        g "E aí? Gostou?"

        mc envergonhado "Muito..."

        g "Você fica me devendo uma. Agora deixa eu correr atrás dela."

        hide garconete with dissolve

        "Nem acredito que a [g] fez isso..."

        "Que menina louca... Mas... foi muito bom..."

        "Acho que elas tão voltando."

    label julia_e3_fim:

        scene uni_biblioteca geral with dissolve

        show 4olhos nervosa with dissolve

        o "Oi..."

        mc envergonhado "Olá."

        show 4olhos nervosa at direita with move

        o "A [g] me explicou tudo sobre você."

        show garconete e_resignada with dissolve

        g "Eu falei que você tem problema na cabeça."

        mc desconfiado "Ei..."

        show garconete e_resignada at esquerda with move

        g "Esta aqui é minha amiga [o]. A gente tem se falado bastante nos últimos tempos."

        mc normal "Como você aguenta a [g]? Mala pra caramba..."

        show garconete e_emburrada with dissolve

        g "Ou! Fica na sua!"

        o "Rsrs..."

        show 4olhos ola with dissolve

        o "Mesmo meio doidinha, a [g] é muito bacana."

        mc desconfiado "Se você diz..."

        g "Já tá bom de me zoar!"

        mc normal "Bom, garotas. Eu só vim dar um alô pra [g] mesmo. Foi legal te conhecer, [o]."

        g "Já vai?"

        mc "Já tá tarde. Tenho que voltar pra ilha."

        g "Ah. É verdade."

        o "Foi um prazer conhecer você, [mc]."

        mc normal "Igualmente."

        mc "Até, garotas."

        "Júlia e Carol" "Até."

        scene uni_hall corredores with Dissolve(1.0)

        o "{size=10}Ele é um pouquinho mais velho, mas é bem gatinho, Ju...{/size}"

        mc surpreso "!"

        "Deixa eu sair daqui."

        scene universidade fachada with Dissolve(1.0)

        pause

        if carro:

            play sound som_carro

            scene black with dissolve

            scene carro_mc_cidade2 with Dissolve(1.0)
        else:


            "Ufa. Agora pegar o busão de volta."

            "..."

            scene mc onibus_noite with Dissolve(2.0)

            "..."

        "É incrível... toda vez que eu me envolvo com a [g] é a mesma coisa. É sempre uma doidera."

        "Esse negócio de investigação realmente foi sem noção da minha parte."

        "Ninguém tem o direito de ficar seguindo outra pessoa sem ela permitir. Isso é uma total invasão de privacidade."

        "Ainda mais quando no fundo a gente tá pensando mais na gente que na outra pessoa."

        "Mas que bom que ela não ficou puta com isso. Acho que no fundo ela até gostou. Ela é bem estranha..."

        "Talvez ela tenha gostado de saber que tem alguém que passou tudo isso por ela."

        "A [g] com certeza tem problemas..."

        if julia_e3 == "seducao":

            mc "Mas hmm... aquela hora na biblioteca, embaixo da mesa..."

            mc "Essa menina sabe como conquistar um homem..."
        else:


            "Eu não consegui investigar ela em todos os momentos."

            "Parece que no fundo ela queria que eu tivesse xeretado ainda mais a vida dela."

            if not j3_jogo:

                "Talvez eu devia ter aceitado jogar aquela brincadeira que ela queria."

            "Bom, se desse pra eu voltar no tempo e tentar outras coisas, minha vida seria bem mais fácil."

            "Que viagem, haha!"

        "A [s] disse que ela não tava legal. Mas parece que essa [o] tá sendo uma boa companhia pra ela."

        "Talvez o que a [g] precisa agora é de distância dos rapazes. Uma amiga talvez seja o melhor pra ela."

        "E ela também pode contar comigo. Já tô ansioso pro que vai acontecer quando a gente se ver de novo..."

        "E essa [o]... ela disse que me achou gatinho... quem sabe..."

        scene black with Dissolve(1.0)

        mc feliz "Ainda tem muita coisa pra acontecer! Estou empolgadasso!"

        "Motorista" "Que foi aí, rapaz?"

        mc surpreso "Nada não!"





        scene universidade fachada with Dissolve(1.0)

        label j3_premium3:

            pass

        menu:
            "O que a [g] faz na faculdade?":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_18

                    jump j3_premium3

                "Depois de tudo isso que rolou com a [g]... eu fico pensando o que ela vai fazer na aula agora..."

                scene black with dissolve

                scene j3_new12 with Dissolve(1.0)

                pause

                g "Finalmente você me achou. Não tá feliz?"

                o "Eu fiquei um tempão de procurando!"

                g "Eu tava aqui, ué."

                o "Mas uma hora eu vim... você não tava!"

                g "O que importa é que a gente tá juntas agora."

                o "A aula vai começar daqui a pouco. Melhor a gente ir pro-"

                g "Calma... eu queria falar sobre sua dívida."

                o "Dívida? Que dívida? Você nunca me emprestou nada, [g]."

                g "Tô falando de hoje à tarde."

                o "A-ah! E-eu não quero falar sobre aquilo! Eu ainda tô brava com você!"

                g "Como brava?! Eu te dei prazer!"

                o "Você abusou de mim!"

                g "Vem aqui... eu tenho uma coisa séria pra falar..."

                o "Sei..."

                g "Vem!"

                scene black with dissolve

                scene j3_new13 with Dissolve(1.0)

                pause

                o "Q-que você quer agora?"

                g "Você é a única aqui na facul que fala comigo mesmo sabendo das minhas coisas."

                o "E daí?"

                g "Você sabe que as meninas da sala me odeiam porque eu fico com... todo mundo."

                o "Você também, né?"

                g "E mesmo sabendo desse meu jeito... você quis ser minha amiga."

                g "Depois da minha mana você é a pessoa que eu mais gosto."

                o "J-júlia... e-eu... valeu..."

                g "É sério. Vocês duas... e você nem é minha parente. Parece mais especial ainda."

                g "Por isso que eu quero fazer você se sentir bem. É assim que eu mostro pra você..."

                o "N-não precisa fazer eu me sentir bem... eu entendi."

                g "Você fala isso, mas no fundo você sabe que eu sou boa nisso."

                o "Não é essa a questão!"

                g "Você fala que tudo bem, mas se eu fizer você gozar, você vai querer ficar mais comigo."

                o "Não é-"

                scene black with vpunch

                o "J-júlia?!"

                g "Fica quietinha!"

                o "Minha roupa!"

                scene j3_new14 with vpunch

                pause

                g "É igual no banho! Só fica quietinha que eu cuido de você..."

                o "[g]... não..."

                g "Você não gosta quando eu beijo seus peitos, hm?"

                o "N-não é isso... mas..."

                g "Fica quieta então..."

                o "Quando você faz assim... eu fico sem ar..."

                g "É assim mesmo. Você tá excitada."

                o "Ahnn... não..."

                g "Você não precisa desse sutiã gigante. Pode soltar suas tetas de vaca."

                o "Não!"

                scene j3_new15 with Dissolve(1.0)

                g "Deixa eu mamar você."

                o "AAHNN!"

                g "É aqui que você gosta, né? No biquinho..."

                o "Ai, [g]... não... minha... ahn..."

                g "É tão gostoso assim? Eu vou morder então."

                scene j3_new15 with vpunch

                g "AAAANNG!"

                g "Cho-choque!"

                g "Uau... você é muito sensível... quem diria... num peitão desse tamanho..."
                scene jnew_ani21 with Dissolve(1.0)
                g "Você é a vaca perfeita. Só falta o leite agora."

                o "Ahn... {i}puf puf{/i}"

                g "Você nem aguenta mais, né?"

                o "Minhan... cabeça..."

                g "Xii... deixa comigo. Deita aqui e abre a boca."

                g "aah... [g]..."

                scene j3_new16 with Dissolve(1.0)

                pause

                g "Isso. Fica com a boca aberta. Deixa eu lamber sua boca."

                g "Você tem um gosto delicioso. Você é docinha..."

                o "Ah..."

                g "Eu sabia desde o começo... que se eu forçasse você não ia aguentar..."

                g "Agora você vai fazer o que eu mandar... e vai ser muito bom, sua safada."

                o "Ahn..."
                scene jnew_ani23 with Dissolve(1.0)
                g "Isso, coloca a língua pra fora, deixa eu te lamber, putinha."

                g "Me lambe também. Ou eu paro de apertar seu peito. Eu sei que você quer mais."

                g "Essa tetona é grande demais, ela precisa de muito carinho. Muita força, né?"

                g "Quanto mais forte eu aperto..."

                o "ANG!"

                g "Melhor é, né? Que teta delícia!"

                g "Agora tira essa saia... você não precisa dela."

                scene j3_new17 with Dissolve(1.0)

                pause

                o "[g]... chega..."

                g "Agora?"

                o "Eu... ahn... hmm..."

                g "Você não vai conseguir falar com minha língua na sua boca."

                o "Mnnng!"

                g "Eu mandei você ficar quieta e sentir prazer. Você vai me obedecer e gozar."

                o "Ahn..."

                g "Assim é melhor. Só geme, que eu fico ainda mais molhada ouvindo sua vozinha assim."

                g "Agora abre a perna que chegou a hora de você sentir lá."

                o "!"

                g "Lá mesmo. Mas não se preocupa, que eu vou continuar mamando em você."

                g "Eu sei que é aí que você gosta."

                o "Ah..."

                g "Vem aqui."

                scene black with dissolve

                scene j3_new18 with Dissolve(1.0)

                pause

                o "[g]! AAHN! NÃO!"

                g "Cala a boca! Eu sei que você gosta!"

                o "Não! Ahn!"

                g "Continua apertando seu peito!"

                o "[g]! É demais!"

                g "É assim mesmo! Aperta mais sua teta, vagabunda! Você adora!"
                scene jnew_ani25 with Dissolve(1.0)
                o "Ahn!"

                g "Fala que você ama no seu peito! Fala!"

                o "ANG!"

                g "Eu sei que você gosta do meu dedo na sua buceta faminta!"

                o "N-não!"

                g "Fala logo!"

                o "E-eu... tá bom! Tá muito bom!"

                g "Isso!"

                o "AHN! Mama em mim, [g]!"

                g "Agora goza, minha putinha!"

                o "Vou gozar! Isso é gozar! Tô gozando!"

                scene j3_new18 with vpunch

                o "AAAIIINNGH!"

                g "Assim mesmo! Agora eu tenho que gozar também!"

                o "T-tá! O que eu faço?!"

                scene j3_new19 with vpunch

                pause

                g "Coloca sua língua pra fora! Deixa eu te lamber!"

                o "Ah! T-tá!"

                g "Deixa eu te lamber inteira, sua safada! Gozou gostoso!"

                g "Eu adoro ver você tremendo! Eu vou fazer você gozar muito!"

                o "V-você também."

                g "Eu também! Eu vou gozar na sua boca, no seu peito! Ahn!"
                scene jnew_ani29 with Dissolve(1.0)
                g "Aperta meu pescoço!"

                o "Ahn!?"

                g "Aperta logo! Me obedece, vadia!"

                o "A-ah-"

                g "Isso! Ang! Tá vindo! Você vai fazer eu gozar!"

                g "Tá muito bom! Tá bom demais! Você é gostosa demais!"

                g "Tá vindo! AAH! AANG! Minha n-"

                scene j3_new19 with vpunch

                g "AAAAAHHH!"

                o "{i}puf puf{/i}"

                g "Ahn... caralho... essa foi demais..."

                scene black with Dissolve(2.0)

                g "Foi a melhor gozada que eu tive esses tempos..."

                o "Ai, [g]... o que eu tô fazendo?"

                g "Se divertindo..."

                o "Se eu continuar assim eu vou... n-não posso..."

                pause
            "Eu não quero saber.":


                "Deixa pra lá."

        scene black with dissolve

    $ v12_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v12_fim","julia","personagem")

    jump call_cidade

label j3_calculo:

    $ j3_dificuldade = 10 * j3_xereta

    $ j3_chance = 100 - j3_dificuldade

    if j3_xereta == 0:

        "{b}Você ainda não investigou a [g] nenhuma vez.{/b}"

        "{b}Sua chance de conseguir xeretar ela agora sem ser descoberto é de [j3_chance] por cento.{/b}"

    elif j3_xereta == 1:

        "{b}Você investigou a [g] uma vez.{/b}"

        "{b}Sua chance de conseguir xeretar ela agora sem ser descoberto é de [j3_chance] por cento.{/b}"
    else:


        "{b}Você investigou a [g] [j3_xereta] vezes.{/b}"

        "{b}Sua chance de conseguir xeretar ela agora sem ser descoberto é de [j3_chance] por cento.{/b}"

    mc desculpa "{size=15}Preciso fazer isso com muito calma. Ela não pode me ver, ou minha investigação acaba.{/size}"

    "{size=15}Com muita calma agora...{/size}"

    $ randj3 = renpy.random.randint(1,100)

    if randj3 <= j3_chance:

        $ j3_xereta += 1

        play sound "extra/carta.mp3"

        "{size=15}Ufa! Estou seguro. Ela não me viu...{/size}"

        return
    else:


        label julia_e3_descoberto:

            mc angustiado "!!!"

            "DROGA! Acho que ela me viu!"

            "Tenho que sair daqui!"

        scene uni_hall corredores with hpunch

        scene uni_hall geral with hpunch

        mc preocupado "{i}puf puf{/i}"

        "Merda! Estraguei tudo!"

        jump julia_e3_final

label julia_evento4:

    $ julia_e4 = "evento"

    scene ape_tv with Dissolve(1.0)

    pause

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j4_save", extra_info="j4_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você vai ter que se aliar com o inimigo! Ou seja, aceitar uma proposta terrível."

        p "Essa escolha também vai impedir que você namore com a Júlia. Por isso, pense muito bem."

        p rindo "E aí? Você vai preferir a pauta ou ficar com ela? Aqui, você decide! Boa sorte!"

    "A [s] realmente parecia preocupada com a [g]."

    if j3_ouviu_p4:

        "Eu lembro de escutar a [g] falando de um tal de Caio lá na faculdade..."

        "Nem acredito que eu segui ela até o vestiário..."

        "Eu não tenho salvação mesmo."

        mc tarado "Mas ver aquilo..."

        "Enfim!"

    if sayuri_contou_caio:

        "Nessa última vez que a gente foi na Cidade Chinesa, a [s] me falou desse Caio."

        "Esse sujeito não parece ser um cara bacana, não."

    "Ela deve tá passando por um momento muito delicado na vida dela."

    "Eu tenho que decidir qual vai ser minha intenção. Tipo, não posso confundir ela mais ainda."

    "Eu já conheço a [g] há um tempinho..."

    if julia_e1 == "seducao":

        "Lá na praça a gente se pegou."

        mc tarado "Foi bem incrível."

    if julia_e2 == "seducao":

        $ julia_seducao_evento += 1

        "Depois teve nossa brincadeira na casa dela."

        "A gente jogou aquele game e as coisas esquentaram."

        "No fim a [s] chegou e não terminamos, mas mesmo assim foi muito bom."

    if julia_e3 == "seducao":

        $ julia_seducao_evento += 1

        "Quando eu investiguei ela na faculdade também."

        "Ela fez aquelas perguntas, e eu que sou o 007 da rua sabia de tudo."

        "Ela acabou... fazendo aquele agrado embaixo da mesa..."

        "Já tô ficando duro só de pensar."

    if julia_seducao_evento > 0:

        "Não tenho dúvidas que nossa relação esquentou no passado."

        if julia_seducao_evento >= 2:

            "E não só uma vez. A gente já trocou umas boas carícias."

    "Mesmo com os problemas dela, a [g] sempre me passou a vibe de uma garota bem resolvida."

    "Hmm..."

    if julia_conversou:

        $ julia_amizade_evento += 1

        "Aquela vez no parque ela me falou um pouco sobre ela."

        "Deu pra ver que a [g] tem alguns demônios internos também."

        "Ela não gosta de falar sobre ela mesma. Por que isso?"

    if julia_e2_conversou:

        $ julia_amizade_evento += 1

        "E aquela conversa na casa dela."

        "Ela foi adotada... e deixa de lado pela família."

        "A [g] parecia tão triste falando sobre aquelas coisas."

    if julia_amizade_evento > 0 and julia_seducao_evento > 0:

        "Eu já compartilhei mais com ela do que só pegação."

        "Às vezes ela é sexy e até meio agressiva... às vezes ela parece uma pessoa tão machucada."

        "Talvez nem eu saiba direito o que eu queira com ela..."

    elif julia_amizade_evento > 0 and julia_seducao_evento == 0:

        "Eu fui um ombro amigo pra ela nos outros encontros."

        "Eu acho que eu posso ajudar ela novamente."

    elif julia_amizade_evento == 0 and julia_seducao_evento > 0:

        "A gente tá numa baita de uma pegação."

        "A [g] é uma garota sapeca e tô curtindo muito esse jeito dela."

        "Não quero me envolver com esses problemas dela. Acho que o melhor é só aproveitar nosso lance físico mesmo."

    if julia_seducao >= 15:

        "Ainda por cima a [g] me tem na mão. Eu simplesmente não consigo negar o que ela me pede."

        "Só de pensar em entrar no meio daquelas pernas eu fico louco."
    else:


        "Pensando bem, por enquanto eu tô conseguindo manter nossa relação sob controle."

        "Negando algumas investidas dela, eu mostro pra ela que eu tô no controle."

        if julia_seducao < 9:

            "Inclusive não quero nada físico com ela."

            "Nossa relação tá bem fria e não corro risco dela entender errado o que eu sinto."

    "..."

    "Se meter com essa mina realmente tá sendo uma aventura."

    "Pensar nela assim até deu uma saudades agora..."

    "Vou mandar uma mensagem pra ela."

    menu:

        "Como vai a minha sapeca?" if julia_seducao >= 9:

            $ julia_cel_msg5 = "safado"

            if julia_seducao < 15:
                $ julia_seducao += 1
                if julia_seducao >= 15:
                    $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
            else:
                $ julia_seducao += 1

            "Vou já mexer com ela."

            "..."

            show screen celular_julia

            pause

            "Pelo que eu conheço essa mina, ela vai adorar."

            "..."

            "Opa. Resposta."

            $ julia_cel_msg5_r = True

            show screen celular_julia

            pause
        "Tudo legal com você, [g]?":


            if julia_seducao >= 15:
                $ julia_seducao -= 2
                if julia_seducao < 15:
                    $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
            else:
                $ julia_seducao -= 2

            $ julia_cel_msg5 = "amigo"

            "Deixa eu mandar."

            show screen celular_julia

            pause

            "Tomara que ela teja bem..."

            "..."

            "Ela respondeu."

            $ julia_cel_msg5_r = True

            show screen celular_julia

            pause

    "Como é? A [o] tá respondendo o celular da [g]?"

    "Eu sei que elas são amigas, mas deixar alguém responder coisas pessoais..."

    "Será que elas são tão próximas? A [g] nunca tinha nem comentado sobre a [o] até um tempo atrás."

    "E se elas... não não..."

    "Acho que eu devia dar um pulo na faculdade e ver o que tá acontecendo."

    if carro:

        play sound som_carro

        scene black with dissolve

        scene carro_mc_cidade1 with Dissolve(1.0)

        pause

        scene black with dissolve
    else:


        "..."

        scene cidade onibus with Dissolve(1.0)

        "Lá vamos nós pegar o busão. Será que isso nunca vai mudar?"

        "..."

        call cena_onibus from _call_cena_onibus_4

    scene universidade fachada with Dissolve(1.0)

    "E lembrar que da última vez eu vim aqui 'investigar' a [g]."

    "O que eu tinha na cabeça?"

    "E pensar que tudo ainda acabou bem..."

    "Se a [g] fosse um pouco menos cuca fresca ela podia até ter chamado a polícia."

    "Espero nunca mais fazer uma coisa assim."

    "Se bem que..."

    "Não, [mc]!"

    "..."

    scene uni_hall geral with Dissolve(1.0)

    "Cheguei."

    "Onde será que a [g] ou a [o] tão?"

    "Da última vez eu vi elas ali na entrada do auditório. Deixa eu passar ali."

    scene uni_hall corredores with Dissolve(1.0)

    "..."

    "Nada por aqui. E agora?"

    menu:
        "Biblioteca":


            mc zerado "Será que é possível?"
        "Vestiário":


            mc tarado "Tomara que eu esteja certo."
        "Quadra de esportes":


            mc normal "É possível."

    "Deix-"

    "Garota brava" "{size=12}[caio]! O que eu falei pra você, seu corno!?{/size}"

    mc desconfiado "Hân?"

    "Parece a voz da [g]."

    "..."

    scene caio uni_julia with Dissolve(2.0)

    pause

    caio "Calma, amor..."

    g "Eu não falei que era pra você parar de ver outras garotas?!"

    caio "Eu sei... mas eu fiz isso."

    g "Não fez! A [o] me falou que viu você com a [ma] esses dias!"

    caio "Vish..."

    g "Seu idiota, cretino..."

    g "Eu tava me esforçando..."

    caio "Calma, linda. Você sabe que eu te amo. É você que eu amo de verdade."

    g "Você é só um cuzão..."

    g "Você tinha prometido que ia se controlar. Como eu vou confiar em você assim?"

    caio "Eu sei... mas você vai me perdoar, não vai? Hein?"

    g "Não vou."

    caio "Vai, sim..."

    g "Cala a boca..."

    caio "Vou fazer um carinho em você. Vem aqui."

    g "Droga..."

    scene uni_hall geral with Dissolve(1.0)

    "Então esse é o tal do [caio]..."

    "Será que a [g] tá tendo um lance sério com ele?"

    if julia_seducao_evento > 0:

        "Mas e toda nossa pegação?"

        "Isso nem foi há tanto tempo assim..."

    menu:
        "Não posso deixar eles sozinhos.":


            $ j4_juliacaio = True

            "Não tem como deixar esses dois sozinhos, assim."

            "Eles foram ali pelo corredor."

            "É hora do 007 voltar à ativa."

            mc zerado "Isso aconteceu mais cedo do que eu esperava..."

            "..."

            scene uni_hall corredores with Dissolve(1.0)

            "Eles vieram por aqui."

            "E devem ter virado por aqui e da-"

            mc surpreso "!"

            scene julia_beijando_caio with Dissolve(1.0)

            pause

            g "Sai... eu não quero isso agora..."

            caio "Eu sei que você quer."

            g "Vai beijar a [ma], vai."

            caio "Para de ciúmes. Você gosta quando eu te pego assim."

            g "Não! Me solta..."

            "..."

            if julia_seducao > 15:

                "Foda-se se a [g] tá ficando com outro. Eu só quero pegar ela mesmo."
            else:


                "Sei lá... ver a [g] assim, me dá um tipo aperto no coração. Sei lá..."

            menu:
                "Deixar a [g] resolver":


                    "A [g] disse que não quer nada com ele agora. Ela vai..."

                    scene julia caio2 with Dissolve(2.0)

                    pause

                    g "Hmm..."

                    caio "Tá vendo como é bom."

                    g "Você sabe que eu adoro, mas não é essa a ques-"

                    caio "Xii... só deixa..."

                    g "Hmmm..."

                    jump j4_carol_chega
                "Procurar a [o]":


                    "A [o] que me chamou. Acho que é melhor eu procurar por ela."

                    jump j4_procura_carol

                "Gritar para que eles parem" if julia_seducao < 15:

                    $ j4_interrompeu = True

                    "Não consigo ficar vendo isso."

                    mc irritado "Ei, vocês!"

                    "E agora? O que eu falo?"

                    "É..."

                    mc "Mãos pra cima! Os dois! Aqui não é lugar disso!"

                    scene julia_caio_surpresos with vpunch

                    "Júlia e Caio" "Desculpa!"

                    g "[mc]?!"

                    caio "Que foi, velho? Quem é você?"

                    mc serio "Eu sou... É..."

                    menu:
                        "Sou o guarda-costas da [g].":


                            $ j4_guardacosta = True

                            mc serio "Sou o novo guarda-costas da [g]."

                            g "???!!!"

                            caio "Guarda-costas?"

                            mc "É."

                            caio "..."

                            g "..."

                            caio "Ok."
                        "Não interessa!":


                            mc irritado "Não interessa! Circulando!"

                            caio "Calma, cara..."

                            caio "..."

                    caio "[g], depois a gente se tromba lá na festa."

                    g "Tá."

                    scene uni_hall corredores with Dissolve(1.0)

                    show garconete e_emburrada with dissolve

                    g "..."

                    mc desculpa "..."

                    g "O que você tá fazendo aqui?"

                    mc "Eu..."

                    o "[g]! Tô aqui!"

                    o "Você tava com o [caio]?!"

                    hide garconete with dissolve

                    jump j4_conversa_julia
        "Deixa eles. Vou procurar a [o].":


            "Não tenho nada com o que eles fazem. Deixa eu procurar a [o]."

            label j4_procura_carol:

                scene uni_hall corredores with Dissolve(1.0)

                "..."

                "Por que será que ela me chamou pra vir aqui?"

                "Ela com certeza tá na biblioteca. Deixa eu ir pra lá."

                "..."

                scene uni_biblioteca geral with Dissolve(1.0)

                "Sabia! Ela tá bem ali."

                mc normal "Fala, [o]."

                show 4olhos ola with dissolve

                o "[mc]? Boa noite. Você veio."

                mc normal "Claro. O que aconteceu?"

                show 4olhos nervosa with dissolve

                o "A gente não pode conversar aqui. Vamos no corredor."

                mc zerado "Mas não tem ninguém..."

                o "Não importa. A bilbioteca é um lugar sagrado que a gente precisa respeitar."

                mc envergonhado "Sagrado, é? Tudo bem..."

                "Essa deve ser meio piradinha também..."

                "..."

                scene carol_mc_corredor with Dissolve(2.0)

                pause

                o "Desculpa falar pra você vir. Não queria incomodar."

                menu:
                    "Por que você me chamou?":


                        mc "O que aconteceu? Por que você me chamou?"

                        o "É... a [g] tá passando por um problemão e ela me falou bastante de você."

                        mc "Sério?"

                        o "Sim."
                    "Sem problemas.":


                        mc "Não tem problema. Eu quero ajudar como puder"

                        o "Valeu. A [g] tá precisando de alguém que ajude ela."

                        mc "Entendo..."
                    "A [g] deixou o celular dela com você?":


                        mc "Relaxa. Mas por que você tá com o celular da [g]?"

                        o "Ah! Perdão o susto... é que ela estava precisando da minha ajuda."

                        mc "Não entendi..."

                        o "Eu vou te explicar."

                o "Então... a [g] tá enrolada com esse sujeito, o [caio]."

                mc "Sei..."

                o "Só que na minha opinião ele faz muito mal pra ela. Eu queria que ela deixasse ele."

                o "Mas, sei lá... ela gosta de ficar com ele, não sei. Ela aceita muita coisa."

                o "Eu senti que você é um grande amigo dela, e daí você podia me ajudar nessa."

                mc "Entendo..."

                menu:
                    "Pode contar comigo. Quero ajudar a [g].":


                        mc "Pode contar comigo, [o]."

                        mc "Quero ajudar a [g] no que for possível. E pelo que entendi esse cara não é legal pra ela."

                        o "Obrigada, [mc]. Sabia que você ia entender."
                    "Eu não tenho nada a ver com ela.":


                        mc "Pra falar a verdade, eu não tenho nada com a vida da [g]."

                        mc "Se ela quiser ficar com esse cara, azar o dela."

                        o "Entendo..."

                        mc "Mas também não quero te atrapalhar."

                        o "Obrigada."
                    "Não curto nem um pouco o lance dela com esse [caio].":


                        mc "Não tô curtindo nem um pouco a história da [g] com esse [caio]."

                        mc "Quero fazer o possível pra que eles parem com isso."

                        o "Então estamos juntos nessa."

                mc "Ah! Eu vi os dois hoje na entrada."

                scene uni_hall corredores

                show 4olhos assustada with hpunch

                o "Sério?!"

                o "Não posso deixar eles se pegarem de jeito nenhum!"

                mc "Mas a [g] disse que não quer-"

                o "Ela fala isso dez vezes por dia, mas isso não muda nada!"

                o "Vem!"

                hide 4olhos with moveoutright

                "Ixi..."

                "..."

                jump j4_carol_chega

    label j4_carol_chega:

        o "[g]!"

        g "Hm?"

        o "Parem os dois!"

        scene julia caio_carol with Dissolve(2.0)

        pause

        g "Foi tudo culpa dele, [o]! Eu disse que não queria!"

        caio "..."

        o "[caio]?"

        caio "Ela fala da boca pra fora. Eu sei que no fundo ela quer."

        caio "Além disso, bocuda, quem mandou você contar pra ela da Maria?"

        o "Eu... a [g] é minha amiga. Eu tinha qu-"

        caio "Você é só uma bocuda, isso sim."

        g "Não fala assim da [o]! Se não fosse por ela, eu nem ia saber da sua cuzãozisse!"

        caio "Por isso que tô falando..."

        caio "Bom... eu vou dar o fora."

        g "Não vai não! Você ainda tem que me explicar da Maria!"

        caio "Explicar o que? Ela deu em cima de mim, eu comi ela. Só isso."

        caio "Você acha mesmo que eu ia deixar passar? Não sou viado."

        g "Cretino!"

        o "[caio]... você tá ouvindo o que você tá falando?"

        o "Vocês não combinaram que ia ser algo sério?"

        caio "Sim, só que... O que você tem a ver com isso, quatro olhos bocuda?"

        o "Eu-"

        g "Já mandei você parar de falar com ela assim!"

        o "Fodam-se, eu vou sair fora."

        g "Ei!"

        scene uni_hall corredores with Dissolve(1.0)

        g "..."

        "Parece que ele foi embora. Acho que agora é uma bora hora pra aparecer."

        jump j4_mc_chega

    label j4_mc_chega:

        mc normal "Boa noite. Fala aí, [g]."

        g "[mc]?!"

    label j4_conversa_julia:

        scene julia_carol_uni with Dissolve(2.0)

        pause

        o "Ele tá aqui porque eu chamei ele."

        g "Hmm..."

        g "Não sei se essa foi a melhor ideia..."

        o "Por que? Ele não é seu amigo também?"

        g "Não queria que ele soubesse de mim e do [caio]."

        o "Por que?"

        if julia_seducao_evento > 0:

            g "Eu e o [mc] já demos nossos pegas..."

            mc tarado "E que pegas..."

            o "..."

            g "Falando nisso, acho que eu tô com vontade de dar uns pegas agora."

            scene julia_carol_mc with Dissolve(2.0)

            pause

            g "Eu tô muito excitada. O que você acha, [mc]?"

            g "Quer dar uns pegas em alguma sala vazia agora?"

            "Como que a [g] entra no clima do nada assim? Essa mina tá sempre pegando fogo?"

            mc "É..."

            menu:
                "Na hora que você quiser.":


                    if julia_seducao < 15:
                        $ julia_seducao += 1
                        if julia_seducao >= 15:
                            $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
                    else:
                        $ julia_seducao += 1

                    mc "Na hora que você quiser, linda."

                    g "Assim que eu gosto."

                    g "Vamos na sala-"

                    o "Não! Se controlem! Nada de pegação ou de sarrada ou de brincadeirinha ou de tcha-"

                    g "Entendi... entendi..."

                    g "Não precisa ser estraga prazer desse jeito, [o]."

                    o "..."

                "Nem vem, [g]." if julia_seducao < 9:

                    if julia_seducao >= 15:
                        $ julia_seducao -= 1
                        if julia_seducao < 15:
                            $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
                    else:
                        $ julia_seducao -= 1

                    mc "Nem vem com essa."

                    o "Isso mesmo, [mc]."

                    g "Você tá ficando chato igual essa daí. Pelo amor de Deus, hein..."

                    g "Que saco."

                "Você sabe que eu quero, mas não agora." if julia_seducao < 15:

                    mc "Você sabe que eu gosto de uma brincadeira, mas não agora."

                    o "Isso. Se controlem, por favor."

                    g "Que merda... os dois..."

            scene julia_carol_uni with Dissolve(1.0)

        o "Enfim. [g], a gente precisa conversar sobre o [caio]."

        g "De novo?"

        o "Claro!"

        g "Ele é só meu ficante, só isso."

        o "Ele não faz bem pra você, [g]."

        g "Eu sei! Mas... eu gosto de ficar com ele."

        o "Você que me pediu pra não deixar você ficar com ele."

        g "Eu sei..."

        "Parece que a [g] tá só me ignorando aqui."

        if julia_seducao_evento > 0:

            "Ela não se importa com o que a gente passou?"

            "Será que tudo foi só físico pra ela?"

            if julia_amizade_evento > 0:

                "Mas e o que a gente trocou ideia também? As coisas que ela me contou?"

                "Eu pensei que ela tava se abrindo... no sentido figurado, claro..."

        o "Você precisa dessa força. Por isso que eu chamei o [mc]."

        mc desculpa "..."

        g "O [mc] entende, né?"

        menu:

            "Claro que eu entendo. Eu só quero farrear com ela." if julia_seducao >= 9 and julia_seducao_evento == 0:

                mc tarado "Claro que eu entendo. Eu só quero curtir com a [g]."

                jump j4_farra

            "Claro que eu entendo. A gente só farreia juntos." if julia_seducao >= 9 and julia_seducao_evento > 0:

                mc tarado "Claro que eu entendo. Eu e a [g] só tamo curtindo."

                label j4_farra:

                    scene julia_carol_mc with Dissolve(1.0)

                g "Vi-viu, só? O [mc] entende o que eu quero."

                mc "A [g] é uma delícia que eu não tenho como resistir."

                g "Sempre que eu precisar de uma curtição, eu chamo ele."

                g "E depois do que eu [caio] fez, acho que o que eu tô precisando é isso mesmo."

                o "Não, Ju! Não é assim que você vai resolver isso!"

                mc "Por que não? Não atrapalha a gente."

                o "Você também?"

                o "Eu vou chamar algum inspetor se vocês continuarem com isso!"

                mc "Que merda, hein?"

                g "Merdona. Mas fica pra próxima."

                mc "Demorou."

                g "Gostei de você vir aqui só por mim. Tava com saudades, né?"

                mc "Tô com saudades você sabe do quê."

                g "Safado. Mas você merece. Vamos marcar alguma coisa."

                mc "Vou te esperar."

                g "Tá. Vou indo nessa. Vamos [o]?"

                o "Tá."

                mc "Falou, [g]. Até, [o]."

                g "Beijo no pinto."

                o "Até. E obrigada por nada."

                scene uni_hall corredores with Dissolve(1.0)

                "Poxa. A [o] não curtiu muito."

                "Acho que ela me chamou aqui pra tentar convencer a [g] que o [caio] é problema e eu realmente não ajudei em nada."

                "Enfim..."

                jump j4_uni_caio

            "Independente do que eu sinto, quero te ajudar." if julia_seducao < 15 and julia_amizade_evento > 0:

                mc "Não importa o que eu sinto. Você precisa pensar se esse cara é o melhor pra você."

                scene julia_mc_universidade with Dissolve(2.0)

                pause

                g "[mc]?"

                jump j4_mc_julia_conversa

            "Não entendo. Não falo contigo só por pegação." if julia_seducao < 15 and julia_amizade_evento > 0 and julia_seducao_evento > 0:

                $ j4_intencao = True

                mc desculpa "Na verdade eu não entendo, [g]."

                mc "Ver você ficando com um cara que te faz mal assim... Não consigo concordar com isso."

                scene julia_mc_universidade with Dissolve(2.0)

                pause

                g "[mc]?"

                mc "A gente já ficou, mas você também já me contou sobre suas coisas."

                mc "Pensei que você entendesse que eu não quero só transar com você."

                label j4_mc_julia_conversa:

                    $ j4_conversa = True

                    mc "Não achei que você ia só concluir que eu aceitaria bem esse lance, sem nem pelo menos me perguntar antes."

                g "Eu não... desculpa..."

                jump j4_uni_conversa

            "Eu sou seu amigo. Quero te ajudar." if julia_seducao < 9:

                mc "Você tentou me seduzir antes, mas você sabe que eu neguei suas tentativas."

                g "Pois é... idiota..."

                mc "É porque eu vi que você tava só se escondendo nessa máscara de mulher sedutora."

                scene julia_mc_universidade with Dissolve(2.0)

                pause

                g "Hã?"

                jump j4_uni_conversa

    label j4_uni_conversa:

        mc "Olha..."

        mc "Eu não sei o que tá rolando com você. Já deu pra ver que você não gosta de falar da sua vida."

        mc "Mas a [o] tem razão. Não é assim que você vai resolver qualquer coisa."

        g "Você acha que eu não sei?"

        mc "Então! Porque você continua fazendo isso?!"

        g "Eu..."

        mc "Você é uma garota incrível, [g]. Mas você precisa pensar melhor no que você tá fazendo."

        mc "E se esse [caio] realmente não tá sendo bom pra você, igual a [o] disse, então você tem que sair fora dessa."

        mc "Um cara que só ignora seu pedido de ter algo sério e fica com outra. Esse cara realmente merece você?"

        g "Mas ele tá tentando..."

        mc "Tentando? Você viu o jeito que ele falou? Ele não tá nem aí, [g]."

        g "..."

        mc "Eu sei que às vezes pode parecer que ele é o único cara certo pra você. Que é ele que você ama."

        mc "Mas não dá pra ficar com alguém que não te respeita."

        g "Mas e se eu conseguir fazer ele mudar?"

        menu:
            "Você realmente acha que esse cara vai mudar?":


                mc "Olha pra esse [caio]. Você realmente acha que ele vai mudar?"

                g "..."
            "As pessoas não mudam assim.":


                mc "As pessoas não mudam assim de uma hora pra outra."

                g "Mas e se ele realmente gosta de mim?"

                mc "Mesmo assim. Mudar é difícil."

        mc "E dá pra ver que o problema dele é do pior tipo. Ele não te respeita."

        mc "Uma pessoa que faz o que ele fez e ainda fala desse jeito, sem nem se desculpar."

        mc "Esse cara é furada, [g]."

        g "..."

        o "Ele tem razão, [g]. Pense direito."

        g "..."

        scene julia_carol_uni2 with Dissolve(2.0)

        pause

        g "Quer saber? Tem razão."

        o "Verdade?"

        g "Esse cara é um babaca e ele não me merece."

        g "Mesmo que ele seja o último cara do mundo, ele foi um CUZÃO!"

        g "Ele ficou com a Maria mesmo eu falando pra ele se esforçar."

        g "Eu tô me matando esses últimos tempos pra não transar com ninguém e ele tá galinhando."

        g "Que raiva!"

        o "Olha aí."

        g "E sobre essa festa dele aí. Pode esquecer. Não vou de jeito nenhum."

        o "Boa, garota."

        g "Agora eu tô puta. Vou pra casa. Falou pra vocês."

        mc envergonhado "Tchau."

        o "Boa noite, Ju."

        scene carol_mc_corredor with Dissolve(1.0)

        o "Obrigada por toda a ajuda. Você foi demais."

        mc "Não é nada. Só queria que ela racionalizasse se esse cara realmente é coisa boa pra ela."

        o "Não é. Ela sabe disso. Mas a [g]... é duro de entender."

        mc "Vamos ver se ela acorda dessa vez."

        o "Só de ela não ir nessa festa amanhã, já tá excelente. Fico pensando que loucura que ela faria lá."

        o "Desculpa mais uma vez por ter te chamado."

        mc "Relaxa."

        o "Até uma outra oportunidade."

        mc "Boa noite."

        jump j4_uni_caio

    label j4_uni_caio:

        "..."

        scene uni_hall geral with Dissolve(1.0)

        "Acho que minha missão aqui tá finalizada."

        "Tomara que a [g] f-"

        "???" "Oi."

        mc desconfiado "Ân?"

        scene caio_universidade with Dissolve(2.0)

        pause

        "[caio]?!"

        if j4_juliacaio:

            "Eu vi esse idiota beijando a [g]. Vontade de morder a cabeça desse babaca."

        caio "Opa. Não queria chegar do nada."

        if j4_interrompeu:

            caio "Aquela hora você me assustou, mas tá de boa. Eu não te reconheci, mas agora tô ligado."

        menu:
            "Como é?":


                mc desconfiado "Como é?"

                caio "Vi você andando agora e te reconheci."
            "...":


                mc bravo "..."

                caio "É... não queria começar com o pé esquerdo."

        caio "Você trabalha na revista da ilha, certo?"

        "Como ele sabe disso?"

        mc "Sim. E daí?"

        caio "Nada. Só queria dizer que acompanho seu trabalho e acho bem massa. Parabéns."

        menu:
            "...":


                mc serio "..."

                caio "Era só isso."
            "Valeu.":


                mc desculpa "Valeu."

                caio "Nada. Suas matérias foram bem massa."

        caio "Ah! Amanhã eu vou dar uma festa na minha casa. Se v-"

        mc desculpa "Tô de boa. Tenho compromisso amanhã."

        caio "Bom. A [g] vai tá lá. Você é amigo dela, certo?"

        mc "Sim, mas-"

        caio "Olha. Eu anotei meu endereço aqui. Aparece lá. O esquenta vai ser lá pela meia noite."

        caio "Vai ter muita mina lá. Tudo de boa pra você pegar."

        "Pegar? O cara acha que mulher é o quê? E ele nem sabe se eu sou hétero e vai falando assim."

        mc serio "Beleza. Qualquer coisa apareço lá."

        caio "Valeu, mano. Até amanhã."

        scene uni_hall geral with Dissolve(1.0)

        "A [g] disse que não ia mais na festa. Então nem tem porque eu ir."

        "Deixa eu voltar pra casa."

        scene black with Dissolve(1.0)

        "..."

        scene ape_cama with Dissolve(1.0)

        "Conversei pouco com a [g] hoje. Queria ter passado mais tempo com ela."

        "Se ela fosse na festa amanhã, quem sabe dava pra gente se falar mais."

        if julia_seducao_evento > 0:

            "E quem sabe até se pegar de novo..."

            "Eu acho que não recusava, não."

        "Eu..."

        scene black with Dissolve(1.0)

        mc "{i}zzzz{/i}"

        $ dia += 1
        $ tempo = 1

        scene ape_geral with Dissolve(1.0)

        show mc acordando with dissolve

        mc "Uaaahh..."

        mc "Um novo dia, uma nov-"

        play sound "audio/som_3_celular.mp3"

        $ renpy.vibrate(1)

        scene ape_geral with hpunch

        "Smartphone" "Trrrr… trrrr…"

        "Opa. De quem é esse número?"

        show mc cueca_telefone with dissolve

        mc "Alô? Quem é?"

        "???" "Bom dia."

        mc "Bom dia."

        "É a voz de uma garota."

        o "Aqui é a [o]."

        mc "Aah! Oi, [o]. Tudo bem?"

        o "Tudo sim."

        mc "Aconteceu alguma coisa?"

        o "Pois é. Não aconteceu nada. Mas eu acho que vai acontecer."

        mc "Como assim?"

        o "A [g] não tá respondendo minhas mensagens..."

        mc "Se pá ela não acordou ainda."

        o "Não! Já é mó tarde."

        "Verdade... já passou do meio dia. Eu dormi pra caralho."

        mc "Entendi. Mas o que isso tem a ver? E se ela tá, sei lá, fazendo alguma coisa sem o celular."

        o "Eu sei. Pode ser. Só que normalmente a [g] não me atende quando ela tá fazendo alguma coisa errada."

        o "Sempre que eu tento falar com ela e ela não me responde é porque ela tá aprontando."

        mc "Será que el-"

        o "Eu tenho certeza que ela vai na festa do [caio] hoje!"

        if j4_conversa:

            mc "Não, [o]. Ontem a [g] disse que não queria mais nada com ele. Ela tava putassa."

            o "Não seja ingênuo, [mc]. A [g] fala as coisas, mas depois..."
        else:


            mc "Sei não..."

        o "Olha. Eu vou continuar tentando. Se eu conseguir falar com ela eu te aviso."

        o "Mas... se eu não conseguir... você poderia ir na festa do [caio] hoje a noite?"

        mc "Eu?!"

        o "É. Você vai ter que ir de bicão, mas é pela [g]."

        mc "Na verdade ontem o [caio] me convidou."

        o "Sério?! Por que?!"

        mc "Não faço ideia."

        o "Mas isso é perfeito! Por favor, [mc]!"

        menu:
            "Só que não quero ir na festa.":


                mc "[o], eu não quero ir na festa desse cara. Por que você não vai?"

                o "Nã-não! Eu não fui convidada e eu odeio festa! Não tem como!"

                mc "Nem pela [g]?"

                o "Po-po-po-por favor, [mc]!"

                mc "Hmmm..."
            "Tudo bem. Eu vou.":


                "Esse [caio] pode ser um xarope, mas não vou jogar fora a chance de ir numa festa dessas."

                "Ainda mais que eu vou poder ver a [g]."

                "Acho que eu não tenho nada a perder. Eu acho..."

        mc "Ok. Eu vou."

        o "Sério?! Muito obrigada!"

        mc "Mas continua tentando falar com ela. Se ela responder a gente aborta a missão."

        o "Perfeito! Muito obrigada mesmo. Qualquer coisa eu te falo. Tchau."

        mc "Tchau."

        hide mc with dissolve

        "Onde que eu me meti..."

        "Bom... se eu realmente vou nessa festa, talvez seja uma boa hora pra impressionar a [g]."

        "Talvez usar uma roupa mais caprichada."

        "Deixa eu ver o que eu tenho."

        python:
            if renpy.android:
                roupa_blacktie = PythonSDLActivity.pegaBlacktie()
                roupa_blazer = PythonSDLActivity.pegaBlazer()

        if roupa_blacktie:

            "Eu tenho meu Black Tie, mas acho que seria muito exagerado pra uma festinha de universitário."

            "Esse traje é pra acabar com a falera no cassino."

        if roupa_blazer:

            "Meu blazer! Ele é perfeito. É chique, mas não é exagerado."

            jump j4_pos_roupa
        else:


            $ j4_roupa = True

            "Foda. Não tenho nada bacana pra usar na festa."

            "Acho que vou dar um pulo lá na boutique."

            "Se for menos de {b}C$ 300{/b} eu acho que vale à pena comprar."

            "O [caio] falou que o esquenta começa meia noite. Tenho tempo de sobra."

            "Bora."

            scene black with dissolve

            "..."

            jump boutique

    label j4_pos_roupa:

        $ j4_roupa = False

        "..."

        scene ape_geral with Dissolve(1.0)

        python:
            if renpy.android:
                roupa_blazer = PythonSDLActivity.pegaBlazer()

        "Beleza."

        if roupa_blazer:

            "Então eu tenho meu blazer."
        else:


            "Vou ter que ir com essa roupa de sempre mesmo. Mas foda-se."

            "Porra. Preciso fazer mais bicos. Se eu for contar só com o salário da revista não vai dar."

            "Tudo o que eu ganho na revista eu gasto com moradia, internet e pizza. O salário até que é bom, mas viver numa ilha dessas é caro demais."

            "Tenho que trabalhar sempre que der no bar do [gar]. Se eu trabalhar direitinho, dá pra tirar tranquilo C$ 50 por dia."

            "Em alguns dias já consigo comprar uma roupa massa."

            "Enfim..."

        "Com qual roupa eu vou na festa?"

        menu:

            "Blazer" if roupa_blazer:

                $ j4_blazer = True

                "Claro que eu vou com meu blazer top."

                mc charmoso "A galera vai pagar muito pau."
            "Roupa de sempre":


                "Vai ter que ser essa roupa de sempre."

                "Mas e daí? Quem vê cara não vê coração. É o que minha vó dizia."

                mc zerado "..."

        "Ainda tenho tempo até a festa."

        scene ape_tv with Dissolve(1.0)

        "..."

        "Mano! Que merda é essa?!"

        "O cara chega e pergunta como que faz pra dividir a alma."

        "Depois ele começa a matar outros magos e talz. Dá pra ver que vai dar uma merda monstra."

        "E os caras têm um treco que volta no tempo! Por que não usa?!"

        "Volta até o dia em que esse menino apareceu e mete uma varinhada no crânio dele. Problema resolvido."

        "Esses bruxos são tudo burro..."

        $ tempo = 3

        scene ape_geral with Dissolve(1.0)

        "Já tá dando a hora. E nem sinal da [o]. Provavelmente a [g] vai aprontar mesmo."

        "Vou ter que me aprontar também."

        play sound "audio/som_16_chuveiro.mp3"

        scene ape_chuveiro with Dissolve(1.0)

        pause

        "Se a [g] realmente tiver lá na festa, vou ter que ver como fazer."

        "Minha relação com a [g] não é uma coisa clara."

        if julia_seducao < 9:

            "Eu não aceitei as investidas dela e nossa relação tá meio fria."

            "Acho que é assim que eu prefiro. Provavelmente não vou querer nada quente com ela."

        elif julia_seducao >= 9 and julia_seducao < 15:

            "Nossa relação tá quente, mas eu tô me controlando."

            "Se eu manter as coisas assim, posso escolher o que eu quiser. É o melhor."

            "Tenho que decidir se quero algo só físico, uma relação séria ou só ser um amigo mesmo."
        else:


            "Eu me deixei ser dominado por ela. Ela mexe demais com minha cabeça."

            "Eu só quero saber de comer ela e tô pouco me fodendo se ela vai dar pros outros também."

            "Contanto que eu possa pegar um pedacinho também, tá valendo."

            "Mas vai ser impossível ter uma relação séria com ela assim. E nem quero."

        "Pronto."

        stop sound

        scene ape_geral with Dissolve(1.0)

        if j4_blazer:

            show mc blazer with dissolve

            "Tô no esquema."

            "Quero ver a [g] e todo mundo lá pagando um pau."
        else:


            show mc pensando with dissolve

            "Tô pronto."

        "Espero que eu consiga fazer a [g] pelo menos ter algum juízo."

        "Eu sei onde que fica esse lugar da festa. É um bairro bem foda da capital."

        "Era só o que faltava. Esse [caio] ser rico."

        if carro:

            play sound som_carro

            scene black with dissolve

            scene carro_mc_cidade1 with Dissolve(1.0)

            pause

            scene black with dissolve
        else:


            hide mc with dissolve

            mc zerado "E eu andando de busão."

            "..."

            call cena_onibus from _call_cena_onibus_5

            "É aqui o ponto."

            "..."

        scene cidade centro10 with Dissolve(2.0)

        pause

        "Pior que eu tava certo. Esse desgramado mora no {b}Carlton Courts{/b}. Deve ser o prédio mais chique da capital."

        "Só de ver aqui os policiais fazendo a proteção de um prédio privado... dá pra entender o tipo de gente que mora aqui."

        if j4_blazer:

            "Sorte que eu vim usando uma roupa decente."
        else:


            "E eu vestindo essa roupa aqui... merda."

        "Deixa eu tocar o interfone."

        "{i}Bling bloom{/i}"

        "..."

        caio "Opa."

        mc "[caio]? Aqui é o [mc]."

        caio "Caralho! Você veio! Sobe aqui. É na cobertura."

        "Cobertura?!"

        mc "O-ok."

        caio "Não dá pra chegar de elevador aqui. Precisa de uma chave. Então desce no último andar e pega a escada até aqui."

        mc "Beleza."

        caio "Vou deixar aberto pra você. Valeu!"

        "{i}tchk{/i}"

        "Mano... olha só pra isso..."

        "O elevador deve ir até a casa dele direto. Tipo coisa de filme. Afe."

        "Agora bora, né."

        scene black with dissolve

        "..."

        "Opa. Ele deixou a porta aberta."

        scene caio_varanda_cenario with Dissolve(2.0)

        pause

        mc surpreso "!"

        "Uou. Olha só pra esta cobertura!"

        "Piscina, vista de toda a capital. Acho que dá até pra ver a ilha daqui."

        caio "Fala ae."

        mc surpreso "Opa."

        scene caio_varanda_entrada with Dissolve(2.0)

        pause

        caio "E aí? O que achou?"

        mc serio "Fala aí. Massa."

        caio "É só uma casa. Isso não importa muito. É só legal trazer a galera aqui."

        caio "Eu gosto de chamar as garotas pra cá. É mais fácil de comer elas quando elas tão impressionadas."

        caio "Você vai virar meu parceiro. Quero ver você aproveitando também, certo?"

        menu:
            "Opa. Mulher é sempre bom.":


                mc tarado "E quando que mulher é ruim?"

                caio "Falo o mesmo."

                caio "Tô achando que você vai curtir muito a noite."

                mc "Tô pronto pra isso."

                caio "Demorou."
            "Tô de boa.":


                mc desculpa "Tô de boa."

                caio "Bom... vamos ver conforme a noite for passando. Tem várias garotas gatas aqui."

                mc "Entendo..."

                caio "É..."

        caio "Vem aqui rapidão."

        scene caio_varanda_cenario with Dissolve(1.0)

        caio "Quero explanar um negócio contigo."

        show caio_varanda tranquilo with dissolve

        caio "Assim... não sei o que falaram de mim pra você."

        caio "Tipo a [g] e aquela quatro olhos da [o]. Mas tudo tem dois lados, certo?"

        menu:
            "Vou mandar a real. Você tá enrolando a [g].":


                label j4_explica_caio:

                    mc bravo "Vou ser sincero contigo."

                mc bravo "Elas foram bem claras em dizer que você tá enrolando a [g]. E isso não é bacana, cara."

                caio "Eu imaginei que elas iam falar algo assim."

                caio "Olha..."

                caio "Você tem todo o direito de ficar puto. Não sei qual é sua relação com a [g]. Talvez você seja até irmão dela, sei lá."

                caio "Mas você sabe como ela é, certo?"

                mc bravo "Como assim? Como 'ela é'?"

                show caio_varanda confiante with dissolve

                caio "Ah, mano. A [g]... ela gosta de curtir com a galera, certo?"

                caio "Não nego que eu fui cuzão com ela. Ela disse que queria algo sério, e eu aceitei, mas acabei ficando com outras minas."

                mc "..."

                caio "Mas, calma! A [g] fez a mesma coisa, cara!"

                caio "Ela fica com uma pá de gente da nossa sala. A mina curte uma farra! O que ela pode falar de mim?!"

                caio "Mano, ela dá pros meus amigos! Gente que eu converso quase todo o dia! Eu sei disso! Eles me falam!"

                "Será que isso é verdade?"

                if julia_seducao_evento > 0:

                    "Bom... eu e a [g] já demos nossos pegas. E se ela já tivesse em um lance sério com o [caio] naquela época?"

                caio "Não sou eu que tô errado, só. É uma via de mão dupla."

                caio "Não tá certo eu ser o cara errado da história, sendo que a gente tá fazendo a mesma coisa."

                mc serio "Mas ela disse que tá se esforçando."

                show caio_varanda tranquilo with dissolve

                caio "{i}pfff{/i}"

                caio "E você acreditou nisso?"

                caio "O que a [g] fala a gente não escreve."

                caio "Olha. Não me leve a mal. A [g] é uma garota sensacional. Ela é divertida, ela é sexy, ela é gostosa pra caralho."

                caio "Mas tem coisas que ela não é. E ser fiel é uma delas."

                mc serio "..."

                caio "Só que eu não vou ficar só falando. Vocês jornalistas precisam de fatos, certo?"

                caio "Vou te mostrar uma coisa."
            "Elas não falaram nada.":


                mc desculpa "Ninguém falou nada."

                caio "Ah, mano! Olha tua cara! É óbvio que aconteceu alguma coisa."

                caio "Mas como eu vou me explicar se você não me falar o que tá rolando?"

                caio "Você é jornalista! Tem que ouvir os dois lados, não tem?!"

                menu:
                    "Não importa o que elas falaram.":


                        mc serio "Não importa o que elas falaram. Você sabe o que você fez."

                        caio "Beleza. Não vai falar, tudo bem."

                        caio "Mas deixa eu te mostrar uma coisa."
                    "Então vou mandar a real. Você tá enrolando a [g] e isso é foda!":


                        jump j4_explica_caio

        show caio_varanda confiante with dissolve

        caio "Quero que você veja com seus próprios olhos."

        caio "Ela tá aqui na festa. Você sabia, né?"

        if j4_conversa:

            mc serio "Ela disse que não ia vir."

            caio "Haha! Parece que você não conhece ela muito bem."

            caio "A [g] perder uma chance de transar?"

            caio "Ela gosta dessa vida, mano. Ela gosta de sentir o luxo e de tá no meio de um monte de homem."

            mc bravo "..."

            "Não vou acreditar em tudo o que esse cara fala."
        else:


            mc serio "Não sabia."

            caio "Você vai ver."

        caio "Vem aqui comigo. Ela já chegou e tá lá dentro."

        caio "Mas fica de boa pra ela não te ver. Quero que você veja ela agindo como ela sempre faz com a gente."

        "..."

        scene festa_caio_cozinha with Dissolve(2.0)

        pause

        caio "Vamos entrar aqui pela cozinha pra ela não te ver."

        caio "Espera só um segundo. Já te chamo."

        "Por que eu tô fazendo isso?"

        "Será que eu também não confio na [g]? Será que ela fala as coisas, mas no fundo só quer saber de safadeza?"

        "Se eu pensar um pouco... ela deu em cima do encontro da irmã. Certinha ela não é."

        "Mas será que ela é tudo isso que o [caio] tá falando?"

        caio "Ei! [mc]. Vem aqui."

        "O que será que ela tá fazendo? Tenho até medo de ver."

        "..."

        scene julia_sinuca_teo with Dissolve(2.0)

        pause

        caio "Olha ela ali com meu amigo Téo."

        caio "Ele tá 'ensinando ela jogar sinuca' haha!"

        teo "Deixa eu segurar sua mão aqui na mesa."

        g "Tá."

        teo "Segura direito o taco."

        g "Tô tentando."

        teo "Você já bebeu umas, né?"

        g "Só umas..."

        teo "Não esquenta que eu te ajudo."

        g "Tá. Já tá na hora de eu aprender a jogar isso."

        teo "Você vai aprender."

        window hide

        pause

        caio "Tá vendo o que eu disse?"

        caio "Você acredita em mim agora?"

        "É estranho, mas só isso não quer dizer nada."

        "Vai que ela realmente acha que ele tá ajudando..."

        "Mas... será que eu tô pensando isso só pra defender ela? E agora?"

        menu:
            "Isso não prova nada.":


                mc serio "Concordo que é estranho, mas isso não prova nada."

                mc "Isso é muito diferente de você transar com outra pessoa."

                caio "Tem razão. Mas vamos continuar vendo."

                window hide

                pause

                teo "Você precisa acertar sua postura."

                g "Como assim?"

                teo "Calma que eu te ajudo."

                scene julia_sinuca_teo2 with Dissolve(2.0)

                pause

                g "[teo]? Posso saber o que você tá fazendo pegando no meu peito?"

                teo "Tô só ajudando você a acertar a postura."

                g "A é, é?"

                teo "Claro. Eu sei que você tá num lance mais sério com o [caio]."

                g "Que bom que você sabe. A gente não vai poder mais ficar."

                teo "Certeza, [g]? Eu gostava tanto."

                g "Você sabe que eu sempre gostei, mas, né?"

                teo "Tá bom... vou ter que me contentar só de pegar nesse peitão gostoso."

                g "Safado..."

                window hide

                pause

                caio "Haha! Tá vendo?!"

                caio "Ela nem percebeu que o vestido dela tá mostrando o peitão dela. E o [teo] claro não é bobo."

                mc desculpa "..."

                caio "Ela fala que não pode, mas deixa ele fazer o que quiser."

                caio "Daqui a pouco ela tá na cama com ele."

                label julia4_premium1:

                    pass

                menu:
                    "Quero ver onde vai dar...":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_19

                            jump julia4_premium1

                        mc "..."

                        scene j4_new1 with Dissolve(1.0)

                        pause

                        g "Você não tá indo longe demais?"

                        teo "Eu? Não."

                        g "Você tá apalpando, caralho."

                        teo "E daí? Eu faço isso quase todo dia na faculdade."

                        g "Mas é a casa dele..."

                        teo "Você sabe que ele nunca ligou. Você é nossa."

                        g "Mas agora..."

                        teo "Cala a boca, Ju. Deixa eu sentir seu peito, porra."

                        g "Grosso..."

                        teo "Você vive falando que adora quando a gente pega você de jeito."

                        g "E daí? Eu gosto de um pouco de força mesmo."

                        teo "Então fica quieta que você tá me deixando duro."

                        g "Afe..."

                        teo "Deixa eu sentir aqui também."

                        scene j4_new2 with Dissolve(1.0)

                        pause

                        g "Ei!"

                        teo "Para de reclamar de tudo. A culpa é sua que é gostosa demais."

                        g "Você tá abusando, tá todo mundo vendo!"

                        teo "Todo mundo sabe que você é nossa putinha."

                        g "E você tá passando tempo demais com o Caio!"

                        teo "E se ele que aprendeu comigo?"

                        g "Você é bem saidinho mesmo."

                        teo "Eu prometo que eu vou te recompensar."

                        g "Até imagino..."

                        teo "Vem aqui."

                        scene j4_new3 with Dissolve(1.0)

                        pause

                        g "A-ah, Téo!"

                        teo "Eu vou fazer você se sentir bem também."

                        g "A-ah! M-meu pescoço!"

                        teo "Você não falou que tava começando a gostar de ficar sem ar?"

                        g "Ah-aahgnn..."

                        teo "Tá vendo? Você não aguenta quando a gente mexe na sua buceta."

                        g "É.. q-que é gostoss... akh..."

                        teo "Vai gozar assim, é?"
                        scene jnew_ani24 with Dissolve(1.0)
                        g "Vô! Esfrega ela com força, filha da puta!"

                        teo "Hmm... e o que eu ganho?"

                        g "Esfrega, caralho! Depois eu mamo!"

                        teo "Sua puta!"

                        g "HMMN!"

                        teo "Mas não deixo você gozar."

                        g "N-não!"

                        teo "Você vai ficar assim a festa inteira."

                        g "Desgraçado! Eu vou trepar com outro!"

                        teo "Tô nem aí... só sai pra lá."

                        g "Filha da puta..."
                    "...":


                        pass

                if julia_seducao < 15:

                    "Que merda! O que a [g] tá fazendo?!"

                    "Ela vai realmente deixar esse babaca pegar nela?"

                    "Mas ela tá bêbada..."

                    "Droga. Não sei o que pensar."

                    menu:
                        "Eu vou falar com ela.":


                            $ j4_bronca = True

                            mc bravo "Eu vou falar com ela. Ela não pode fazer isso."

                            caio "Relaxa, cara. Ela é assim."

                            mc "Não tem essa."

                            mc bravo "[g]!"

                            g "[mc]?! É você mesmo?!"

                            teo "Ixi. Deixa eu vazar. Falous, Ju."

                            scene festa_caio_sinuca with Dissolve(1.0)

                            mc bravo "Sou eu mesmo, [g]."

                            show julia v_ola with dissolve

                            g "O que você tá fazendo aqui? Parece coisa da minha cabeça hihi..."

                            mc serio "O que parece coisa da minha cabeça era ver você deixando aquele idiota pegar em você."

                            g "O [teo]? Ele só tava me ajudando a jogar esse treco aí. Sinuca, né?"

                            mc zerado "Ele tava com a mão no seus peitos."

                            g "Oops..."

                            mc bravo "[g]! Se você não quer nada sério com o [caio], você precisa terminar de vez com ele. Você já fez isso?"

                            g "Não... não sei se quero chutar ele."

                            if j4_conversa:

                                mc zerado "Ontem você disse que ele não te merecia..."

                                g "Só que hoje é um novo dia, [mc]! As coisas mudam!"
                            else:


                                mc desculpa "Entendo..."

                                mc serio "A [o] disse que ele não te faz bem."

                                g "Ele faz bem gostoso na verdade..."

                            mc desculpa "Você tá alta demais, já..."

                            g "Nada! Só tomei algumas."

                            caio "[mc]?"

                            g "Você tá aí, [caio]? Amor!"

                            caio "Oi, linda. Vai jogar lá sinuca com o [teo], vai. Eu preciso conversar com o [mc] rapidinho."

                            g "Tá. Cuida dele pra mim. Vou beber mais um pouco que minha boca tá seca."

                            caio "Isso."

                            g "Tchau, gatos."

                            mc zerado "..."

                            hide julia with dissolve

                            caio "Deixa ela um pouco. Vem aqui fora comigo."

                            "Que merda tá acontecendo? Parece que eu não tenho controle nenhum sobre o que acontece aqui..."

                            "A [g] tá completamente fora de controle."

                            jump j4_varanda_caio
                        "Eu entendi. Vamos lá pra fora.":


                            mc desculpa "Eu entendi. Vamos conversar lá fora."

                            caio "Demorou. Vem."

                            jump j4_varanda_caio
                else:


                    "Só de ver a [g] assim já tô ficando duro. Quero pegar nela também."

                    "Não consigo resistir."

                    "Se eu continuar aqui vou atacar ela. Preciso de um ar."

                    mc desculpa "Eu já vi o que tinha que ver. Deixa eu sair daqui."

                    caio "Claro. Vamo lá pra fora."

                    jump j4_varanda_caio
            "Eu já vi o suficiente. Deixa eu sair daqui.":


                mc desculpa "Eu já vi o que tinha que ver. Deixa eu sair daqui."

                caio "Claro. Vamo lá pra fora."

                jump j4_varanda_caio

    label j4_varanda_caio:

        "..."

        scene caio_varanda_cenario_festa with Dissolve(2.0)

        pause

        caio "O pessoal já tá alto pra caralho haha!"

        show caio_varanda tranquilo with dissolve

        caio "E aí?"

        caio "Você viu como ela é, né?"

        if j4_bronca:

            caio "Você até conversou com ela. A mina só te ignorou e foi beber mais."

        mc desculpa "..."

        caio "Não precisa ficar assim, mano. Eu entendo você. A [g] tem uma carinha de anjo, qualquer um cai nesse conto."

        caio "Mas depois de conhecer ela de verdade, você perde as esperanças."

        show caio_varanda confiante with dissolve

        caio "Eu vou mandar a true da true pra você."

        caio "Fica com ela. Curte a [g]. Aproveita o que ela tem pra te oferecer. Mas não fica procurando pelo em ovo."

        caio "Não adianta você querer ter algo sério com ela. Ou ser amigo pra proteger ela."

        caio "Ela tem 18 aninhos. Ela é nova. Você também é novo. Eu também. Vamo só curtir haha!"

        if julia_seducao >= 15:

            "Ele tá certo. Eu não tô nem aí pra ela. Só quero poder comer ela quando eu quiser."

            "Se ela vai dar pra festa toda, eu não tô nem aí."

            mc tarado "Acho que tô entendendo o lance."

            caio "Agora sim!"

        elif julia_seducao < 15:

            mc desculpa "..."

            caio "Você ainda parece meio desconfiado. Acho que esse senso cético é tipo o poder do jornalista."

        caio "Eu não tô pedindo nada de outro mundo. Só quero que você deixe eu e a [g] em paz."

        caio "A gente tem nosso lance. E se você quer continuar aproveitando ela também, eu não ligo."

        caio "Pode comer ela quando quiser. Só deixa eu comer ela também e não embaça nosso esquema."

        caio "Se a quatro olhos vier encher o saco, só corta ela. E deixa a [g] ser feliz."

        show caio_varanda tranquilo with dissolve

        caio "Não parece uma coisa de outro mundo, certo?"

        if julia_seducao >= 15:

            mc tarado "Me parece uma excelente proposta."

            caio "Haha! Isso aí."

            caio "E eu tenho uma surpresa pra você."
        else:


            mc desculpa "Não sei, [caio]... Não dá pra ter certeza de uma coisa assim."

            caio "Eu entendo. Claro. Mas espera."

        caio "Eu sei que pra você informação privilegiada é muito importante."

        caio "E eu tô ligado de um lance que você pode publicar na sua revista e vai te garantir um bom bônus com seu chefe."

        "Será que ele tem uma pauta?!"

        caio "Se você aceitar o que eu tô propondo, vou te passar uma informação valiosa."

        show caio_varanda confiante with dissolve

        caio "Ah! E eu percebi que você não é um cara fácil. E pra provar que eu tô falando sério..."

        caio "Espera outro segundo. Tenho mais uma coisa."

        hide caio_varanda with dissolve

        "O que acontece com esse cara? Por que parece que agora ele tá me subornando?"

        "Eu não sou nada da [g]. Eu não tenho direito de escolher alguma coisa por ela."

        "Por que raios ele quer tanto que eu concorde com isso?"

        caio "Voltei. Olha aqui."

        show caio_varanda mari with dissolve

        caio "Tcharãã!"

        caio "[mari]. [mc]. [mc]. [mari]."

        mari "Oi."

        mc envergonhado "Olá."

        caio "A [mari] e eu tamo ficando, mas a gente tem uma relação aberta. E ela disse que quer passar um tempo contigo."

        mc surpreso "Como?!"

        mari "Haha! Que fofinho."

        mc envergonhado "E-eu..."

        caio "Eu vou deixar vocês sozinhos pra se conhecerem melhor."

        mari "Isso, amor."

        caio "Só quero ter certeza que você aceita minha proposta."

        "Então tudo o que o [caio] quer é que eu deixe ele tranquilo com a [g]."

        "Ele não tá nem aí se eu vou vou ficar com ela também. Ele só não quer que eu atrapalhe o lance dele com ela."

        "Eu não vou poder mais me intrometer na relação deles. Mesmo que a [o] peça ajuda igual ontem."

        "Em troca, além de eu poder continuar saindo com a [g], ele vai me revelar uma pauta e também posso conhecer a [mari]."

        if julia_seducao >= 15:

            "No fundo, eu só quero saber de pegar ela, então como eu vou poder continuar saindo com ela, não tem porque não aceitar."

            "A não ser que eu queira ela SÓ pra mim. Mas tô pouco me fodendo pra isso eu acho."
        else:


            if julia_seducao < 9:

                "Minha relação com a [g] tá meio que mais de amizade agora."

                "Eu não dou muita bola pras provocações dela."
            else:


                "Eu não sei pra onde eu quero levar nossa relação."

                "Eu aceitei algumas provocações dela..."

                "Mas é só físico ou quero algo a mais?"

                "Será que é possível ter uma relação séria com a [g]? Ou ela só vai me tratar igual ao [caio]?"

            "E eu sei que esse [caio] não é flor que se cheire. Se eu tirar ele da vida da [g], provavelmente eu estaria fazendo a coisa certa."

            "Mas eu tenho que pensar em mim também."

            "Esta com certeza é uma decisão que vai {b}mudar completamente{/b} minha relação com a [g]."

        caio "E então? Vai deixar a gente de boa?"

        label j4_escolha_caio:

            "Tem tanta coisa na minha cabeça. Eu queria ter mais tempo, mas eu preciso escolher uma coisa agora."

        menu:
            "Eu aceito. Pode fazer o que quiser com ela.":


                "Se eu permitir que ele continue fazendo isso, não dá pra prever o que vai acontecer com a [g]."

                "Ela tava meio abalada esses tempos. A própria [s] me disse."

                "Deixar ela com esse cara..."

                "É realmente isso que eu quero?"

                menu:
                    "Sim. Vou aceitar a proposta do [caio]":


                        "Sim. É isso que eu quero. Não me importo com o que ele vai fazer com a [g]."

                        mc tarado "Eu aceito, [caio]. A [g] é sua."

                        caio "Minha, não, nossa."

                        mc "Hehe. Você que tá falando."

                        scene caio_varanda_entrada with Dissolve(1.0)

                        caio "Vou deixar vocês conversando. Vou lá pra dentro ver como tá a [g]."

                        caio "Até depois."

                        mc tarado "Falous."

                        jump j4_conversa_mari
                    "Não. Preciso pensar melhor":


                        "Espera... deixa eu pensar um pouco."

                        jump j4_escolha_caio
            "Não aceito. Eu me importo com a [g].":


                "Se eu não aceitar o acordo dele, vou perder uma possível pauta e provavelmente uma chance de conversar com a [mari]."

                "Além de que com certeza ele vai ficar puto."

                "Por outro lado, eu vou ajudar a [g] a se livrar desse idiota que não tá nem aí pra ela."

                "É realmente isso que eu quero?"

                menu:
                    "Não aceitar a proposta do [caio].":


                        $ caio_negou = True

                        "Meu foco é a [g]. E esse cara não vai fazer o que quiser com ela."

                        "Essa menina já tem problemas demais sem ele, e com esse otário na vida dela só consigo ver a coisa piorar."

                        mc serio "Sem chance. Não posso deixar você com a [g]."

                        caio "Como?"

                        mc bravo "O que você não entendeu? Não aceito a merda da sua proposta."

                        show caio_varanda puto with hpunch

                        caio "Sai pra lá!"

                        mari "Ai!"

                        caio "Você é burro, cara?!"

                        caio "Não tá entendendo o que eu tô te oferecendo?!"

                        caio "Vai negar tudo isso por causa daquela putinha?!"

                        mc bravo "Não fala assim dela."

                        caio "Ela é minha e eu falo como eu quiser, seu puto!"

                        mc irritado "Cala a boca, [caio]! Você pode ter sua casa, suas putas, mas não vai ter a [g]!"

                        mc "Você acha que dá pra me comprar oferecendo uma mina como se fosse sua propriedade?!"

                        mc "Você não passa de um cuzão mimado!"

                        caio "!"

                        caio "Foda-se."

                        hide caio_varanda with dissolve

                        mc concentrando "{i}puf puf{/i}"

                        mari "Puxa."

                        show mari sexy with dissolve

                        mari "A [g] é sortuda."

                        mc "Hm?"

                        mari "Também queria ter um cara que me protegesse igual você protegeu ela assim."

                        mc "..."

                        mari "E obrigada por me defender também."

                        mc "Só falei a verdade."

                        mari "Sei... olha... eu sei que você quer ir atrás da [g], mas será que você pode sentar comigo só um segundo?"

                        mc desconfiado "Por que?"

                        mari "Só queria te falar um negócio."

                        menu:
                            "Ok. Mas rápido.":


                                mc desculpa "Tudo bem. Mas seja rápida por favor."

                                mari "Tá."

                                jump j4_confissao_mari
                            "Não tenho tempo. Quero ver a [g].":


                                mc desculpa "Desculpa, mas não posso agora. Preciso ver se a [g] tá bem."

                                mari "Tá bom. E obrigada de novo."

                                mc normal "Relaxa. Até outro dia."

                                mari "Beijo."

                                jump j4_retorno_festa
                    "Não. Preciso pensar melhor":


                        "Espera... deixa eu pensar um pouco."

                        jump j4_escolha_caio

        label j4_conversa_mari:

            scene caio_varanda_cenario with Dissolve(1.0)

            mc charmoso "E aí? Tudo legal?"

            show mari sexy with dissolve

            mari "Tudo, sim, gato."

            mari "Eu tava de olho em você. O [caio] parece que realmente foi com sua cara. Isso mostra que você tem valor."

            mari "Vem aqui comigo."

            if j4_blazer:

                mari "Você tem bom gosto pra roupa. Esse blazer tá demais."

                mari "Tira o sapato e senta aqui."

            mc surpreso "Opa!"

            scene j4_mari_flertando with Dissolve(2.0)

            mari "O [caio] é incrível, mas você tem alguma coisa que chama a atenção."

            mari "Não sei o que é, mas só de olhar pra você tá me deixando excitada."

            "Sinto que essa mina tá prestes a pular em mim."

            mc "É... e como funciona esse lance de relacionamento aberto?"

            mari "Normal, ué. A gente namora, mas a gente pode ficar com outras pessoas."

            mari "Ele fica com a [g] e eu fico com você... por exemplo..."

            mari "Não é a melhor coisa que já inventaram?"

            mc "Não sei se a me-"

            mari "Tipo... E se a gente pular as preliminares e ir direto pra pegação? Você se importa?"

            mc "E-eu?"

            menu:
                "Claro que não. É pra isso que tô aqui.":


                    mc "Tá louca? Claro que não. Tamo aqui pra isso."

                    mari "Boa. Deixa eu tirar sua roupa e você tira a minha."

                    mc "Assim!? Aqui?!"

                    mari "Relaxa, fofo. Tá todo mundo lá dentro."

                    mari "Deixa que eu vou cuidar muito bem de você."

                    mc "Ok."

                    scene black with dissolve

                    mari "Assim. Tira. Pode me beijar enquanto isso."

                    mari "Hmmm..."

                    mari "Você é cheiroso."

                    mc "Obrigado. Você também."

                    mari "Tá. Agora me morde também."

                    mari "Ai. Isso."

                    mari "Pronto."

                    scene mari_pegacao with Dissolve(2.0)

                    pause

                    mari "Pode passar a mão em mim. Não precisa ter medo."

                    mari "Isso. Me aperta com força."

                    mari "Pode me beijar, me chupar, me morder. Só não vou deixar você meter porque eu não dou no primeiro encontro."

                    mari "De resto tá tudo liberado."

                    mc "Perfeito."





                    label julia4_premium2:

                        mari "O que você vai querer?"

                    menu:
                        "Quero aproveitar TUDO.":


                            if not premium:

                                call mensagem_premium from _call_mensagem_premium_20

                                jump julia4_premium2

                            scene j4_new4 with Dissolve(1.0)

                            pause

                            mc "Calma aí, gata. Uma mulher igual você eu quero aproveitar bem."

                            mari "Hmm... tá..."

                            mc "Seus amigos não gostam de curtir você?"

                            mari "Eles são meio... afobados..."

                            mc "Sei... agora você tá com um homem de verdade. Que gosta de mulher e não só de gozar."

                            mari "Ai..."
                            scene jnew_ani28 with Dissolve(1.0)
                            mc "Seu corpo é perfeito. Seus peitos... sua bunda... olha pra essa coxa... a barriguinha definida."

                            mari "Você gostou mesmo?"

                            mc "Demais. Quem falar outra coisa é muito burro. Ou cego."

                            mari "Para..."

                            mc "Agora vem aqui. Deixa eu experimentar você, hm."

                            mari "Ah... claro... eu tô aqui pra você, gato."

                            scene j4_new5 with Dissolve(1.0)

                            pause

                            mari "Hmmm... que vontade..."

                            mc "Você é deliciosa, Mari."

                            mari "Obrigada... eu gosto de ser perfeita pra.. hmn!"

                            mc "Arrepiou?"

                            mari "É..."

                            mc "Você gosta de ser usada assim?"

                            mari "Gosto. Eu quero você fazer se sentir bem."

                            mc "Que boa garota... é bom ficar com uma mulher assim."

                            mari "Que bom... eu quero que você me queira."

                            mc "Eu quero você. Muito."

                            mari "M-mas eu não posso dar pra você hoje..."

                            mc "Tem certeza?"

                            mari "S-sim..."

                            mc "Acho que eu vou ter que aproveitar você melhor então. Posso?"

                            mari "P-por favor! Pode me usar!"

                            menu:
                                "Morder o peito dela":


                                    scene j4_new6 with Dissolve(1.0)

                                    pause

                                    mari "Annngh!"

                                    mc "É ruim?"

                                    mari "Não! Eu gosto..."
                                    scene jnew_ani33 with Dissolve(1.0)
                                    mc "Nhg!"

                                    mari "Aainngh! Ahnn... anh..."

                                    mc "Você realmente gosta disso, hein?"

                                    mari "I-isso tem problema?"

                                    mc "Claro que não. Muita gente gosta de sentir dor assim."

                                    mari "Se tá tudo bem, me morde!"

                                    scene j4_new6 with vpunch

                                    mari "NNNGH!"

                                    mc "Quanto mais forte, mais gostoso?"

                                    mari "Eu tô ficando molhada..."
                                    scene jnew_ani33 with Dissolve(1.0)
                                    mc "Só com isso?"

                                    mari "É muito bom!"

                                    "Parece que ela tá quase pronta... pode ser a hora..."
                                "Se esfregar nela":


                                    "Eu tô louco pra sentir ela no meu caralho."

                            scene j4_new7 with Dissolve(1.0)

                            pause

                            mari "Mnn... o que você tá fazendo, safado?"

                            mc "Parece que você tá pronta pra mim..."

                            mari "E-eu tô, só que... eu disse que não posso..."

                            mc "Certeza?"

                            mari "Sim..."
                            scene jnew_ani32 with Dissolve(1.0)
                            mc "Eu vou deixar você escolher... enquanto eu mamo em você."

                            mari "Nnnghh..."

                            mc "E aí?"

                            mari "Não... não assim..."

                            mc "Você realmente leva a sério esse negócio de primeiro encontro..."

                            mari "Sim."

                            mc "Então se a gente se ver de novo..."

                            mari "Daí você pode me comer."

                            mc "No segundo não tem problema?"

                            mari "Não. Daí pode fazer o que quiser comigo."

                            mc "Se essas são as regras... eu tenho outra ideia então."

                            mari "Anal também não pode..."

                            mc "Calma. Eu vou te mostrar."

                            scene black with dissolve

                            mari "A-ah! Q-que você t-tá?!"

                            scene j4_new8 with Dissolve(1.0)

                            pause

                            mc "Uau... meu dedo escorregou pra dentro tão fácil... você tá molhada mesmo."

                            mari "N-não fala assim!"

                            mari "Era pra eu tá te dando prazer..."

                            mc "Você foi uma boa garota. Você merece um agrado."
                            scene jnew_ani30 with Dissolve(1.0)
                            mari "N-não..."

                            mc "Você não gosta do meu dado no seu buraquinho?"

                            mari "C-claro que eu gosto... mas..."

                            mc "É o Caio?"

                            mari "É... ele... ele não vai gostar de saber..."

                            mc "Hmm..."

                            scene j4_new8 with vpunch

                            mari "Ahnngg!"

                            mari "S-se você continuar ass-"

                            mc "Saber que ele não vai gostar me dá mais vontade ainda de ver você gozando."

                            mari "M-mas! Ahnnn! [mc]!"

                            mc "O pessoal lá dentro vai te ouvir assim."

                            mari "F-foda-se! Eu tô quase! Nnng!"

                            mari "Faz eu gozar, por favor!"

                            mc "Então goza, Mari!"

                            mari "NNG! NNNNHG!"

                            scene j4_new9 with vpunch

                            mari "AAAHNNNN!!!"

                            window hide

                            pause

                            mari "Tô gozando, [mc]!"

                            mc "Isso!"

                            mari "Que d-delícia!"

                            scene j4_new9 with vpunch

                            mari "AAIIINH!!"

                            mari "Ah... aghhh...."

                            mc "Uou... foi forte, hm?"
                            scene jnew_ani31 with Dissolve(1.0)
                            mari "Muito..."

                            mc "E foi... bem rápido... achei que você tivesse mais acostumada..."

                            mari "Ahnng... {i}puf{/i}"

                            mari "Anng... ainda tô... nnnh...."

                            mari "Não tô acostumada... com um homem colocando eu em primeiro lugar assim..."

                            mc "Entendi..."

                            mari "E o que eu faço por você agora?"

                            mc "Tá bom por hoje. No segundo encontro a gente se entende..."

                            scene black with dissolve

                            mari "Combinado..."
                        "Só faz eu gozar.":


                            mc "Só vamo logo pros finalmentes."

                            mari "Garoto precipitado... mas pelo menos você sabe o que quer."

                            scene black with dissolve

                            "..."

                            mari "Ai! Isso!"

                            mari "Eu vou gozar!"

                            mc "Eu também!"

                            mari "Aaah!"

                            mc "Ugh!"

                            scene mari_pegacao with Dissolve(1.0)

                            pause

                            mari "Foi bom. Você fez direitinho."

                            mc "Que bom que você gostou. Eu adorei."

                    mari "Quero ver você de novo, ok?"

                    mc "Pode deixar."

                    scene caio_varanda_cenario with Dissolve(1.0)

                    mc "Vou dar um pulo lá dentro."

                    mari "Pode ir. Eu vou fumar alguma coisa e ficar um tempinho aqui."

                    mari "Até mais, gostoso."

                    mc safado "Até."

                    jump j4_retorno_festa
                "Na verdade não quero ficar com você.":


                    mc "Olha. Não me leva a mal, mas não quero ficar contigo."

                    mari "Que?! Por que? O que eu fiz de errado?"

                    mc "Calma. Não fez nada de errado. Você é linda, gata e tudo o mais."

                    mc "Mas eu não gostei do jeito que o [caio] te ofereceu como um objeto."

                    mc "Não vou me sentir bem ficando com você assim. Mas em outra circunstância, com certeza eu aceitaria."

                    mc "Vou lá pra dentro agora. Valeu pelo papo, [mari]."

                    mari "Sei... olha... eu sei que você quer ir atrás da [g], mas será que você pode ficar aqui só mais um segundo?"

                    mc "Por que?"

                    mari "Só queria te falar um negócio."

                    menu:
                        "Ok. Mas rápido.":


                            mc "Tudo bem. Mas seja rápida por favor."

                            mari "Tá."

                            jump j4_confissao_mari
                        "Não tenho tempo. Quero ver a [g].":


                            mc "Desculpa, mas não posso agora. Preciso ver se a [g] tá bem."

                            mari "Tá bom. E obrigada de novo."

                            mc "Relaxa. Até outro dia."

                            mari "Beijo."

                            jump j4_retorno_festa

        label j4_confissao_mari:

            scene mc_mari falando with Dissolve(2.0)

            pause

            mari "Você é um cara estranho."

            mc "Isso que você queria falar? Me chamar de estranho?"

            mari "Não! Desculpa!"

            mari "É só que... eu nunca vi alguém fazer o que você fez."

            if caio_negou:

                mari "O jeito que você encarou o [caio]. Eu nunca vi alguém fazendo isso."

                mc "Não sei qual é a dele. Tentar comprar as pessoas desse jeito."

                mari "Isso que eu tô falando. O [caio] sempre consegue o que ele quer. Essa foi a primeira vez que eu vi isso."
            else:


                mari "Você é o primeiro cara que nega ficar comigo assim."

            mari "Olha. O [caio] não faz bem pra [g]. Ele não faz bem pra ninguém."

            mari "Ele domina a gente. A gente fica do lado dele porque ele tipo dá uma segurança."

            mari "Ele tem dinheiro, conhece as pessoas. Não sei explicar. Ele é tipo o 'chefe'."

            mc "Entendo..."

            mari "Mas vendo você encarar ele desse jeito... meio que eu vi que ele não é tudo isso."

            mc "Se o [caio] realmente não faz bem pra vocês. Vocês precisam se desfazer disso."

            mc "Ninguém precisa de um cara desses pra se dar bem."

            mari "..."

            mari "Entendi. Valeu."

            mc "Agora vou lá ver se tá tudo bem com a [g]."

            mari "A [g] não é uma garota fácil. Ela nem gosta de mim. Ela me chama de Maria porque ela sabe que eu odeio."

            mari "Mas no fundo acho que ela é legal."

            mc "Você também parece muito legal, [mari]. Tomara que um dia a gente se veja de novo."

            mari "!"

            mari "Tomara mesmo... Beijo."

            mc "Até."

            jump j4_retorno_festa

    label j4_retorno_festa:

        "..."

        scene festa_chegada with Dissolve(2.0)

        "Vozes" "Vai! Vai! Vai!"

        mc desconfiado "Que tá acontecendo?"

        g "Tudo bem. Já que vocês querem tanto."

        "Galera" "Aeeee!"

        scene julia_sinuca1 with Dissolve(2.0)

        pause

        g "Pronto! Abri as pernas!"

        teo "Uhul! Gostosa!"

        caio "Que menina safada, hein?!"

        g "Safados são vocês que ficam olhando pra mim de perna aberta!"

        "Rapaz" "Você é uma delícia, [g]!"

        g "Que bom que você gostou!"

        "O que a [g] tá fazendo?"

        teo "Faz outra pose!"

        g "Vocês são insaciáveis, hein?"

        caio "Vai logo!"

        g "Calma! Tenho que me preparar."

        "Rapaz" "Deita na mesa!"

        g "Boa ideia, Japa!"

        scene julia_sinuca2 with Dissolve(2.0)

        pause

        "Galera" "Uoooou!"

        teo "Que delícia!"

        g "Obrigada! Já pode parar de olhar!"

        "Rapaz" "Nem que me pagassem eu paro!"

        caio "E como é ter todo mundo duro olhando pra você, [g]?!"

        g "Vocês são tudo safados, só isso! Mas não posso fazer nada."

        teo "Agora faz uma pose sexy! Bem sensual!"

        g "Ai! Tá bom já."

        caio "Não tá, não. Bora! Atende seus fãs. Senão a gente não vai te pagar depois."

        g "Tá me chamando de puta, é?"

        caio "{size=15}Puta pelo menos recebe pelo trabalho...{/size}"

        teo "Hahaha!"

        g "Que você disse?!"

        caio "Nada! Deita na mesa! Deita! Deita!"

        g "Ai, assim vocês vão me convencer."

        "Galera" "Deita! Deita! Deita!"

        g "Tá bom!"

        "Galera" "Aeeee!"

        "A [g] tá exagerando. Ela tá bebassa e tá se deixando levar por esses tarados."

        "Ela tá fazendo papel de palhaça pra esses marmanjos."

        label j4_sinuca_decisao:

            "Será que eu devo parar com tudo isso e salvar ela dessa situação?"

            "Tenho certeza que essa escolha vai ser {b}muito importante{/b} pra minha relação com ela."

        menu:
            "Sim. Tirar a [g] de cima da mesa de sinuca":


                if not caio_negou:

                    "Eu prometi pro [caio] que não ia me intrometer nas coisas da [g]."

                    "É um saco. Mas eu vou ter que deixar as coisas rolarem."

                    jump j4_sinuca_decisao

                elif julia_seducao >= 15:

                    "Tá doido?! Eu até me sinto mal por ela, mas não consigo resistir."

                    "Tenho que ver ela tirando a roupa toda em cima dessa mesa!"

                    "Talvez se eu não tivesse feito tanta sacanagem com ela... eu conseguiria resistir... mas agora é tarde. Eu quero ver!"

                    jump j4_sinuca_decisao

                "Isso é um absurdo. Não quero ver ela virando motivo de piada pra esses idiotas!"

                jump j4_salva_julia
            "Não. Deixar ela continuar.":


                $ julia_e4 = "caio"

                "Foda-se se tão fazendo ela de boba. Ela tá curtindo a atenção."

                g "Prontos?"

                caio "Opa. Deixa eu chegar mais perto pra ver isso."

                caio "Chega aí, [mc]."

                mc safado "Tô de boa. Vai lá."

                teo "Eu que-"

                caio "Você cala a boca e apaga uma luz pra ficar um clima mais sexy."

                teo "Tá..."

                g "Prontos agora?"

                caio "Manda ver."

                scene julia_sinuca3 with Dissolve(2.0)

                pause

                g "Assim?"

                caio "Tá demais assim, [g]. Tá muito gata."

                teo "Tá todo mundo babando em você."

                g "Ai. Vocês tão me deixando excitada falando assim."

                caio "Tá todo mundo te comendo com os olhos."

                g "Parem, safados... minha cabeça tá girando."

                caio "O que você quer?"

                g "Eu quero..."

                caio "Pode falar."

                g "Eu quero transar muito."

                caio "Seu pedido é uma ordem, princesa."

                scene julia_sinuca_caio with Dissolve(2.0)

                pause

                g "Ai! Me beija, [caio]!"

                g "Me pega bem forte."

                teo "Pena que só ele pode aproveitar... Nosso show acabou. Falous ae."

                g "Isso, [caio]!"

                caio "Vamo pro quarto?"

                g "Sim! Agora! Me leva!"

                caio "Claro. Vem que eu vou dar um jeito em você."

                "..."

                scene festa_caio_sinuca with Dissolve(1.0)

                "A [g] saiu com o [caio]."

                mc "{i}tsc{/i}"

                "Acho que não tem mais nada pra mim aqui."

                "Deixa eu voltar pra casa."

                "..."

                scene cidade centro10 with Dissolve(1.0)

                "Eu acabei vendendo a [g] pro [caio]."

                "Depois de ver como aqueles idiotas trataram ela... sei lá. Não sei se a [g] merece isso."

                "Se a [s] soubesse disso ela ficaria tão triste."

                mc desculpa "Agora não adianta chorar pelo leite derramado."

                play sound "audio/som_3_celular.mp3"

                $ renpy.vibrate(1)

                "Smartphone" "Trrrr… trrrr…"

                mc desconfiado "Ligação..."

                mc "Alô?"

                caio "Fala aí, [mc]. Tô na cama aqui com nossa amiga."

                mc serio "..."

                caio "Mas não queria que você achasse que eu te enrolei, então quer-"

                g "{size=17}Vem logo! Já tô peladinha!{/size}"

                caio "Já vou, caralho!"

                caio "Desculpa, [mc]. Quero só te passar a pauta que eu prometi e assim ficamos numa boa."

                caio "Escuta direito. Estou te mandando um dossiê em anexo com um relato de outro mundo."

                caio "A Madame Nora, uma das cabeças do Distrito, está envolvida em tráfico de pessoas."

                caio "Isso é algo terrível. Inclusive, como pessoas de bem, precisamos denunciar algo assim."

                caio "Espero que você faça a coisa certa."

                caio "Agora estamos quites. Deixa eu dar um trato nela aqui. Boa noite!"

                "{i}Tu tu tu...{/i}"

                $ pautas += 1
                $ caio_p1 = True

                "Isso parece realmente sério. Por que ele me passaria uma informação dessas?"

                "Não tô com cabeça pra pensar nisso agora."

                "O que eu preciso é ver direitinho antes de entregar essa pauta pro chefe."

                "Agora deixa eu voltar."

                "..."

                "Espero que a [g] fique bem nas mãos desse cara."

                scene black with Dissolve(3.0)

                show tela continua with Dissolve(1.0)

                pause

                $ tempo = 4
                $ v18_fim = True

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("v18_fim","julia","personagem")

                "..."

                jump call_cidade

    label j4_salva_julia:

        $ j4_salvou = True

        mc bravo "Dá licença."

        scene julia_sinuca2 with hpunch

        mc bravo "[g]! Para com isso!"

        g "[mc]?! Você tava aí?!"

        mc bravo "Sai daí de cima e vem comigo."

        caio "Só pode tá brincando com a gente!"

        teo "Sai você daí, cuzão!"

        mc irritado "Calem a boca! A [g] não é uma puta pra vocês fazerem isso com ela!"

        "..."

        g "Você tá putasso, hein?"

        mc bravo "Vem logo aqui."

        g "Tá bom, pai."

        scene j4_carregando with Dissolve(2.0)

        pause

        g "Você veio me salvar ou me levar pra cama?"

        mc "Para de ser boba."

        g "Ah! Esqueci que você é estranho."

        mc "Estranho, é?"

        if julia_amizade_evento > 0:

            g "Você é o único que fica perguntando sobre mim ao invés de só me pegar."

            mc "E daí? Não tem nada de estranho nisso."

            g "Tem sim... mas eu acho fofo."

            mc "..."

        if j4_blazer:

            g "Agora que eu vi. Até que você se vestiu bem. Foi pra mim?"

            mc "Não."

            g "Você negou muito rápido. Deve ter sido."

            mc "Cala a boca..."

        mc "Vou deixar você no sofá."

        g "Tá."

        scene j4_sofa with Dissolve(2.0)

        pause

        g "Ai ai ai..."

        mc "Que foi?"

        g "Minha cabeça tá latejando..."

        mc "Tá passando o efeito da bebida?"

        g "Merda. Preciso beber mais."

        mc "Nem vem. Tá doida?"

        g "..."

        g "Ainda não acredito que você tá aqui."

        mc "Por que?"

        g "Parece que você é tipo do Disco 2 da minha vida. Não devia tá no Disco 1."

        mc "Como?"

        g "Gamer nutella..."

        mc "Você tá bêbada ainda?"

        g "Só um pouco."

        mc "..."

        g "É..."

        mc "Que foi?"

        g "Não vai me dar bronca?"

        mc "Por que bronca?"

        g "Passei um pouco do ponto..."

        mc "Tudo bem. O que importa é que você tá bem agora."

        g "[mc]..."

        mc "Oi."

        g "Não queria que você tivesse visto essas coisas. Desculpa. Eu nã-"

        mc "Relaxa. Só descansa um pouco."

        g "Tá... mas tô falando sério. Não queria que você me visse assim."

        mc "Todo mundo faz coisa que se arrepende depois. Faz parte da vida."

        g "Você parece o Dumbledore falando."

        mc "Nem sei quem é esse. Não. Pera. É o cara do filme que vi hoje."

        g "Ah! Eu vi Harry Potter hoje também... Isso faz da gente almas gêmeas?"

        mc "Acho que não é pra tanto."

        g "Tem raz-"

        g "{i}Cof cof{/i}"

        mc "Tá um cheiro forte aqui mesmo."

        g "Deve ser quatro e vinte."

        mc "Não. Ainda falta um tanto pras quatro."

        g "Deixa pra lá... vamo lá fora?"

        mc "Tá. Quer ajuda?"

        g "Sim."

        "..."

        scene caio_varanda_cenario with Dissolve(1.0)

        g "A noite tá bonita."

        mc "Sim."

        g "Tô passando tempo demais com você. Já tô falando essas baboseiras."

        mc zerado "..."

        g "..."

        "A [g] tá realmente bem estranha hoje. Tô começando a concordar com a [s]."

        mc desculpa "[g]. Por que você se envolveu com o [caio]?"

        g "Ah... deixa pra lá, [mc]."

        mc desculpa "[g]. Olha aqui."

        g "Opa."

        scene j4_varanda with Dissolve(2.0)

        pause

        mc "Me fala, por favor. Pode confiar em mim. Não tô falando pra te julgar."

        g "Não é assim tão fácil, [mc]..."

        if julia_amizade_evento > 0:

            mc "Você já se abriu comigo antes. Não precisa ter medo."

            g "Eu sei, só qu-"

            mc "Sem 'mas'. Só fala."

            g "Afe, [mc]..."

            g "..."

            mc "..."

            g "Tá bom. É que eu tava com inveja."

            mc "Inveja?"

            g "É! Inveja de você e da [s]."

            if sayuri_intencao == "namoro":

                mc "Eu realmente quero namorar a [s], mas o que isso tem a ver?"
            else:


                mc "Como assim? Eu só quero ser amigo da [s]."

                g "Você fala isso agora, mas..."

            g "Você chegou na mana e foi tão legal com ela."

            g "A mana nunca teve alguém igual você. Alguém que olhasse pra ela e entendesse ela. Que ajudasse ela de verdade."

            g "Toda vez que ela me contava o que você fazia..."

            g "Eu também queria ter alguém assim!"

            g "E, eu sei que você vai me chamar de idiota, mas o [caio] foi o mais perto que eu achei disso."

            g "Mesmo sendo um babaca, ele me ouviu. Não sei porque, mas ele passou uma segurança que eu nunca senti com ninguém."

            g "Eu queria que ele me tratasse igual você trata a mana. Só que ele nunca vai fazer isso, vai?"

            mc "..."

            g "Eu só tô me enganando..."

            g "Acho que eu nunca vou encontrar alguém assim. Eu nem mereço alguém assim pra começo de conversa."

            "A [g] tá tão triste. Eu consigo ver nos olhos dela como ela tá desesperada."

            "Parece que ela realmente quer alguém do lado dela. Alguém que ame ela de verdade."

            "Eu acho que a gente tem uma química bacana, só que..."

            if priscila_namoro:

                "Eu já tô comprometido com a [c]."

            if sayuri_namoro:

                "Eu assumi um compromisso sério com a [s]."

            if maria_namoro:

                "Eu aceitei namorar com a [ma]."

            "Será que eu quero ter algo sério com a [g]? Acho que ela tá cansada desse papo de só pegação."

            "Não é justo eu querer só ficar de pegação com ela em um momento que ela tá tão fragilizada."

            "Eu preciso tomar uma decisão sobre isso agora."

            "Se eu quiser ter uma relação com a [g], vai ter que ser só como amigo ou como um verdadeiro namorado."

            "Se ela aceitar namorar comigo, claro..."

            g "Que foi? Quebrou? Ou dormiu?"

            mc "Não... só tava pensando aqui."

            g "Pensando no que?"

            "É agora ou nunca."

            menu:
                "Eu quero namorar com você.":


                    mc "Sabe, [g]. O [caio] não é o cara certo pra você. Sabe por que?"

                    g "Por que?"

                    mc "Porque eu sou o cara certo pra você."

                    mc "Esquece esse idiota e fica comigo. Me escolhe, [g]."

                    g "!"

                    g "[mc]?!"

                    mc "Tô falando sério."

                    g "As coisas não são assim, [mc]! Você é louco?!"

                    if julia_seducao_evento > 0:

                        $ julia_namoro = True

                        $ julia_e4 = "seducao"

                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("julia_e4_seducao","julia","personagem")

                        mc "A gente já se pegou. A gente tem química. E você conseguiu se abrir comigo."

                        mc "Eu não sou igual esses babacas, [g]. Eu gosto de você de verdade. Não quero só te comer."

                        g "[mc]... e-eu..."

                        mc "Não precisa ficar nervosa. Não precisa falar nada complicado. Só fala 'sim'."

                        g "Ai..."

                        g "Si-sim. Eu te escolho."

                        "Beleza!"

                        mc "Sabia que mesmo a gente se pegando, tem uma coisa que a gente nunca fez?"

                        g "A-a-âh?"

                        mc "A gente nunca se beijou."

                        g "Então me beija logo."

                        scene j4_beijo with Dissolve(2.0)

                        pause

                        "A [g] beija tão bem."

                        "Dessa vez não é nenhuma loucura."

                        "Um beijo de verdade. Não é só tesão, é paixão."

                        "Eu quero ficar com ela. Proteger ela."

                        "E mostrar pra ela que existem homens que não são babacas. Que não querem só um pedaço dela."

                        g "Você tem razão. A gente realmente tem química."

                        mc "Eu te falei."

                        if j4_blazer:

                            g "E você até se vestiu todo especial só pra me impressionar."

                            g "Você merece um bônus."

                            mc "!"

                            scene julia_e4_beijo2 with Dissolve(2.0)

                            pause

                            g "Hmmm..."

                            g "É bom? Pegar em mim?"

                            mc "Muito bom. A melhor sensação do mundo."

                            g "Eu sou só sua, [mc]."

                            mc "E eu sou seu."







                        g "[mc]... e se a gente não parar por aqui?"

                        mc "Tô ouvindo..."

                        g "Tá afim de uma baguncinha?"

                        mc "Aqui no meio da festa?"

                        g "Eu conheço um lugar que ninguém vai se intrometer... a gente ficar peladinhos e tudo..."

                        mc "{i}gulp{/i}"

                        "Ficar com a Ju aqui... na casa do Caio? Depois do rolo?"

                        "A gente acabou de começar um lance... um namoro... será que é uma boa?"

                        label julia4_premium3:

                            g "E aí? Vai apagar meu fogo ou não?"

                        menu:
                            "Eu não tô aguentando também.":


                                if not premium:

                                    call mensagem_premium from _call_mensagem_premium_21

                                    jump julia4_premium3

                                mc "Você acha que é só você? Eu tô louco pra transar contigo."

                                g "Uhul! Era isso que eu tava esperando! Vem aqui!"

                                scene black with Dissolve(1.0)

                                g "Agora tira tudo."

                                mc "N-não sei se eu tenho coragem..."

                                g "Olha aqui."

                                scene j4_new10 with Dissolve(1.0)

                                pause

                                g "Se você tirar... você pode ter tudo isso aqui."

                                mc "Uau..."

                                g "E aí? Só a camisa não adianta. Eu quero tudo de fora, pau de fora também óbvio."

                                mc "Mas aqui... na casa d-"

                                g "Agora que a gente tá junto, a gente pode fazer tudo o que a gente quiser um com o outro. Não é?"

                                "Ai, caraca..."

                                "Acho que é melhor a gente deixar isso pra depois. Aqui é perigoso demais."

                                g "Vai logo. Ou eu vou ter que comemorar com outro cara."

                                "Brincadeira essa aí..."

                                mc "Comemorar com outro cara nosso namoro?"

                                g "Se você não dá no coro..."

                                mc "Vamo ver, então. Vem aqui."

                                g "Sim, senhor."

                                scene black with dissolve

                                scene j4_new11 with Dissolve(1.0)

                                pause

                                g "Hmmmm... até o beijo fica diferente quando a gente tá sem roupa."

                                mc "Você é uma safada, isso sim."

                                g "E daí? Não é isso que você gosta?"

                                mc "Hm..."

                                g "Ou você prefere outra santinha igual minha mana?"
                                scene jnew_ani02 with Dissolve(1.0)
                                mc "Você é especial do seu jeito."

                                g "É isso que eu tô falando. Você adora que eu seja uma putinha. Todo mundo gosta."

                                mc "[g]..."

                                g "Não esquenta, [mc]. Eu sei que você não é igual os outros, mas é verdade."

                                mc "Eu acho que você não pode ficar fal-"

                                g "Xi... eu cansei da sua língua, enfia a boca no meu peito agora."

                                mc "Hm?!"

                                scene j4_new12 with Dissolve(1.0)

                                pause

                                g "Assim. Eu prefiro quando os homens ficam quietos me dando prazer."

                                mc "E-"

                                g "Nãnã! Você só abre a boca pra lamber minha teta ou chupar meu biquinho."

                                mc "{i}shluup{/i}"

                                g "Ain... assim mesmo. Eu tô começando a ficar excitada."

                                g "Eu tô o dia todo assim... sempre pingando... sempre pronta pra dar..."

                                mc "E-"

                                g "Xiu! Só trabalha meus peitos agora."

                                g "Eu preciso ficar no limite... o tempo todo..."

                                g "Eu preciso de mais. Você tá cansando já?"

                                mc "Não."

                                g "Então me chupa direito. Morde meu peito, meu filho!"

                                scene j4_new13 with vpunch

                                g "Ainn!"

                                window hide

                                pause

                                g "Assim! Não precisa ter medo de me machucar. Eu gosto quando machuca."

                                g "Ahnn... agora sssim... tá apertando com vontadeee... issooo... morde com forçaainn..."

                                g "Você tem que parar de ser bonzinho e me tratar igual uma coisa!"

                                g "É assim que eu gosto... quando eu sinto que eu tô sendo útil."
                                scene jnew_ani03 with Dissolve(1.0)
                                g "Me deixa cheia de tesão quando eu tô sendo usada assim!"

                                g "Eu tô quase lá, [mc]!"

                                mc "Então goza!"

                                g "Não! Ainda não! Eu gosto de ficar no limite, seu tonto..."

                                g "Vem aqui, deixa eu cuidar de você enquanto eu tô pingando."

                                mc "De mim?"

                                scene black with dissolve

                                scene j4_new14 with Dissolve(1.0)

                                pause

                                mc "Ah..."

                                g "Entendeu agora, né, bonitão?"

                                mc "Você já tá acostumada com ele..."

                                g "Eu já cuidei dele algumas vezes... mas ainda é pouco. Eu nem lembro do gosto."

                                mc "A-ah!"

                                g "Agora eu lembro..."

                                mc "Certeza que você não quer chegar lá antes d-"

                                g "Eu já falei pra você... primeiro que eu adoro ficar o dia todo com vontade de gozar."

                                mc "Mas isso deve ser horrível..."

                                g "No começo era um pouco... mas agora eu não consigo viver sem tá excitada."

                                g "Eu gosto de tá toda hora melada, pensando em besteira, pronta pra qualquer pau que aparecer."

                                mc "Ei... mas agora..."

                                g "É... agora você vai ter que manter eu assim sempre..."

                                mc "[g]... eu não sei como as coisas vão funcionar entre a gente se você cont-{nw}"

                                scene j4_new15 with hpunch

                                pause

                                mc "AAGH!"

                                g "É goxtoxa minha boxinha mollhazda?"

                                mc "Muito gostoza..."

                                g "Entxão xala a boxa e dexa eu chupxa voxê..."

                                menu:
                                    "Não. A gente tem que conversar.":


                                        mc "Espera. Eu-"

                                        scene j4_new15 with hpunch

                                        mc "A-ah!"
                                    "Você quem manda.":


                                        pass

                                mc "Ok... você venceu... pode chupar... hmmm..."

                                g "Hnnn.... {i}shlluuupp{/i}"
                                scene jnew_ani01 with Dissolve(1.0)
                                mc "Você é incrível... sua língua brincando com a cabecinha é demais."

                                mc "Eu nunca vi uma mulher cuidar de um pau igual você, [g]."

                                mc "Aahn... você nasceu pra mamar uma rola, sua safada."

                                mc "Você tá me deixando louco... se continuar assim..."

                                g "Expera!"

                                scene j4_new16 with Dissolve(1.0)

                                pause

                                g "Na gharghantzxaa... kkh!"

                                mc "Ah! Meter na sua garganta é demais!"
                                scene jnew_ani04 with Dissolve(1.0)
                                mc "Vai sair, [g]! Eu vou gozar tudo na sua garganta!"

                                g "Vhaii!"

                                mc "AAh!"

                                mc "AAAHN!"

                                mc "TOMA! AAAGGH!"

                                scene j4_new16 with vpunch

                                pause

                                g "{i}gulp GULP{/i}"

                                mc "Tá engolindo toda minha porra..."

                                g "Aah... atxhé qhue é boahh... o goxthoo..."
                                scene jnew_ani04 with Dissolve(1.0)
                                mc "Minha nossa... você é demais..."

                                mc "E agora?"

                                scene black with dissolve

                                scene j4_new17 with Dissolve(1.0)

                                pause

                                g "Agora você vem aqui. É sua vez de meter a língua em mim."

                                g "Chupar seu pau me deixou com mais vontade."

                                mc "Você vai querer gozar dessa vez pelo menos?"

                                g "Enfia sua linguinha em mim e a gente vê."
                                scene jnew_ani05 with Dissolve(1.0)
                                g "Mas enfia com força. Pode meter bem fundo de onde você quiser."

                                mc "Qualquer lugar?"

                                g "Todos meus buraquinhos só servem pra dar prazer."

                                mc "Você sabe como deixar qualquer um louco..."

                                g "Esse é meu ponte forte na vida... aproveita..."

                                mc "Tô caindo de boca e tudo."

                                scene j4_new18 with Dissolve(1.0)

                                pause

                                g "Hmm... Isso mesmo, gato."

                                mc "Assim que você gosta?"

                                g "É... você gosta do meu gosto?"

                                mc "Você é deliciosa. Dá pra ver que você tá louca."

                                g "Eu tô... faz tanto tempo..."
                                scene jnew_ani07 with Dissolve(1.0)
                                mc "Eu vou fazer você gozar então."

                                g "..."

                                mc "Você cuidou de mim tão bem, agora é sua vez."

                                g "Você tá indo bem... só continua assim... ah..."

                                mc "Hmm! Você ser toda cheia de fogo deixa tudo mais interessante."

                                g "Eu sei... é bom, né?"

                                mc "Mas você também merece sentir aquela paz depois do clímax."

                                g "Então vai... me lambe..."

                                "Eu sinto que isso ainda é pouco pra ela."

                                "Eu vou ter que pegar mais firme pra fazer a [g] realmente chegar lá!"

                                scene j4_new19 with Dissolve(1.0)

                                pause

                                g "Aaiiin! Você tá com fome mesmo..."

                                mc "Eu sei que você gosta assim, bem forte!"

                                g "Eu gosto mesmo, pode fazer com a força que você quiser!"

                                mc "{i}SLLUUPP{/i}"

                                g "Hmmm..."

                                mc "Ainda não é essa reação que eu quero de você!"
                                scene jnew_ani09 with Dissolve(1.0)
                                g "Ahgn!"

                                "Parece que sexo oral não vai resolver as coisas."

                                "Acho que tá na hora de eu finalmente transar com ela. Aqui na casa do idiota."

                                "Eu não vou deixar a [g] sair com o trabalho na metade."

                                g "Que foi? Cansou?"

                                mc "Não. Só vou mudar de tática."

                                g "Oba..."

                                scene black with dissolve

                                scene j4_new20 with Dissolve(1.0)

                                pause

                                mc "Tá na hora de você me sentir de verdade."

                                g "Sério? Aqui? Sem proteção nem nada?"

                                mc "Eu não vou deixar você sair daqui assim."

                                g "Para de ser bobo, você foi muito gostoso."
                                scene jnew_ani08 with Dissolve(1.0)
                                mc "Eu não vou parar enquanto você não gozar."

                                g "Homens..."

                                g "Vamos ver onde você chega."

                                mc "Nossa primeira vez tem que ser incrível."

                                g "E você vai querer fazer aqui?"

                                mc "Você não quer? Não achei que você fosse romântica."

                                g "Cala a boca... claro que eu não ligo. Só mete logo."

                                scene j4_new21 with Dissolve(1.0)

                                pause

                                mc "Calma... deixa eu brincar um pouco."

                                g "Para de me provocar, desgraçado..."

                                mc "Essa [g] que eu gosto de ver..."

                                g "Só de pensar no seu rolo entrando em mim... hmm..."

                                mc "Já tá arrepiada."

                                g "Vai... come logo! Come sua namoradinha!"

                                mc "Eu v-"

                                "???" "Ei! É a [g] alí?!"

                                g "Afe! É o maldito do japonês!"

                                mc "Ele tá olhando pra gente e chamando todo mundo!"
                                scene jnew_ani06 with Dissolve(1.0)
                                g "Foda-se! Só me come! Vai ser mais excitante dar na frente de todo mundo!"

                                mc "Tá louca?!"

                                g "Vai logo! Eu preciso disso! Eu preciso gozar, [mc]!"

                                mc "[g]... eles tão vindo! As coisas não podem ser assim!"

                                g "Afe! Só porque tem umas 15 pessoas assistindo você transar?"

                                mc "Exatamente!"

                                g "Ok..."

                                mc "Eu sei que é ruim, mas eu também tava louco."

                                g "Espero que você me recompense na próxima."

                                mc "Com certeza."

                                scene black with dissolve

                                mc "Agora bora se trocar e sair daqui."

                                g "Tá..."

                                "..."

                                g "Hehe..."

                                mc "Que foi?"

                                g "Até que foi divertido. Tô ansiosa pra nossa próxima vez."

                                mc tarado "Eu também..."
                            "A gente vai ter tempo.":


                                mc "Eu sei como você é... você adora uma brincadeira, mas a gente vai ter tempo."

                                g "Hah... eu sabia que você ia falar isso..."

                                mc "Decepcionada?"

                                g "Eu sei como você é. E é por isso que eu quero namorar você e não só transar."

                                mc "Poxa... parece que você pode ser legal também."

                                g "Cuzão..."

                        jump j4_deixar_festa
                    else:


                        g "Você é um cara especial. Você é o cara mais incrível que eu conheço."

                        g "Mas a gente precisa ter química. A gente nunca se pegou."

                        g "Não tem como você namorar com alguém que você não sente tesão."

                        "Merda... Se em algum encontro passado eu tivesse sido mais intenso com ela..."

                        mc "Huh... Eu entendo... já me sinto melhor de ter te falado a verdade."

                        g "Com certeza você é corajoso. Nunca ninguém chegou em mim assim..."

                        jump j4_amizade
                "Eu quero ser seu melhor amigo e te ajudar.":


                    label j4_amizade:

                        $ julia_e4 = "amizade"

                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("julia_e4_amizade","julia","personagem")

                        mc "Mesmo não sendo essa pessoa que você procura, eu quero ser seu amigo. Eu quero te ajudar a superar isso."

                        mc "Namorar não é tudo. E talvez um namorado nem é o que você precisa agora."

                        mc "Você precisa de alguém que goste de você e queira ver você se dando bem na vida."

                        mc "Pessoas como a [o], a [s] e eu também. Pode contar com a gente, [g]. A gente vai ser o apoio que você precisa."

                        g "Essas palavras não fazem sentido na minha cabeça."

                        g "Não acredito que exista um cara que não queira trepar comigo."

                        mc "Pode ser novidade pra você, mas é a verdade haha! Você vai ter que se acostumar."

                        g "Você realmente é estranho, [mc]."

                        mc "As pessoas adoram falar isso pra mim."

                        g "É bom que você vai acostumando."

                        mc "..."

                        g "Eu sei que às vezes pode parecer que eu não ligo, mas valeu mesmo por se importar comigo."

                        mc "Não esquenta. Só quero o melhor pra minha amiga."

                        g "Valeu... amigo."

                        mc "Viu só? Nem doeu."

                        g "Doeu sim! {i}KHH!!!{/i} Tô ficando sem ar!"

                        mc "Engraçadinha..."

                        g "Bobo..."

                        jump j4_deixar_festa
        else:


            mc "Não pensa muito. Só me fala."

            g "Eu..."

            g "Desculpa... mas e não consigo."

            mc "Relaxa. Você tem seu tempo."

            "Se nos encontros anteriores eu tivesse ouvido mais ela, talvez as coisas tivessem sido diferentes."

            "Eu não posso só pensar em sacanagem com ela."

            mc "Não pense demais nisso. Acho que já tivemos progresso hoje."

            g "Nem fala... você me salvou de uma que vou te falar..."

            mc "Não pense mais nisso."

            jump j4_deixar_festa

    label j4_deixar_festa:

        scene caio_varanda_cenario with Dissolve(2.0)

        show julia v_ola with dissolve

        g "Acho que eu quero dar o fora daqui."

        mc normal "Claro. Foi aventura demais pra uma noite."

        scene cidade centro10 with Dissolve(1.0)

        mc normal "Quer que eu te acompanhe até em casa?"

        show julia v_ola with dissolve

        g "Não seja bobo. Essa não é minha primeira festa, [mc]."

        mc zerado "Sei... só tava sendo educado."

        g "Tchau, tonto."

        if julia_namoro:

            mc desconfiado "Nem um beijinho no seu namorado?"

            g "Já beijamo demais por hoje."

        hide julia with dissolve

        mc "Até, [g]."

        "Fico pensando se eu fiz a coisa certa."

        "Mas não tinha como ser de outro jeito. Eu não ia deixar ela ficar nas mãos do [caio] e dos outros babacas."

        "A [g] é uma garota especial."

        if julia_namoro:

            "Agora a gente tá namorando. Quem diria?"

            "Ela é uma garota complicada. Tenho que me preparar para o pior."

            "Só torço para que ela se esforce. Eu também. Não posso ser um idiota."

            "Se eu quero que ela seja minha, eu tenho que ser dela também."

        "Quero que ela seja feliz."

        "E tem o [caio]. Ele pistolou comigo. Sinto que isso vai dar problema."

        "Tenho que me preparar pra isso também."

        "Mas agora eu quero só voltar pra casa."

        scene black with Dissolve(3.0)

        show tela continua with Dissolve(1.0)

        pause

        $ tempo = 4
        $ v18_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v18_fim","julia","personagem")

        "..."

        jump call_cidade

    label j_mais:

        if julia_seducao < 15:
            $ julia_seducao += 1
            if julia_seducao >= 15:
                $ renpy.notify("Você foi completamente seduzido e não poderá mais negar os pedidos da Júlia")
        else:
            if julia_seducao <= 19:
                $ julia_seducao += 1

        return

    label j_menos:

        if julia_seducao >= 15:
            $ julia_seducao -= 1
            if julia_seducao < 15:
                $ renpy.notify("Você conseguiu se livrar do domínio sedutor da Júlia e tem o controle novamente")
        else:
            if julia_seducao > 0:
                $ julia_seducao -= 1

        return

label julia_evento5:

    $ julia_e5 = "evento"





    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j5_save", extra_info="j5_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "Por que ela tá falando assim? Parece sério demais pra ser a [g]... Será que é a Carol?"

    "Só falta ter acontecido alguma coisa com ela."

    "Deixa eu responder."

    "..."

    $ julia_cel_msg6_r = True

    "Beleza."

    scene mc bar_celular with Dissolve(1.0)

    "..."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "{i}Trrrrrrr{/i}"

    mc "É ela."

    g "O-oi."

    if not j4_salvou:

        g "É... queria falar sobre aquele lance na festa no outro dia."

        g "Eu acabei bebendo pra caralho e nem lembro direito como você foi."

        mc "Relaxa. Desculpa qualquer coisa também."

        "Por que eu tô pedindo desculpa pra ela?"
    else:


        g "É... tipo... não sei como falar haha..."

        mc "Que foi?"

        g "Queria agradecer por tudo o que você fez na festa. Acho que eu fiquei meio louca com a bebida."

        g "Se não fosse você nem sei o que ia rolar com aqueles doidos."

        mc "Tudo bem..."

        if julia_namoro:

            mc "Bom... agora você sabe por que eu quis te tirar de lá, né?"

            g "Safado... você me queria só pra você, né?"

            mc "Claro."

            g "Bobo..."

            mc "Ei!"

    g "É... você não quer dar uma passada aqui na faculdade? Tô eu e a [o] aqui."

    mc "Tá. Dou um pulo aí."

    g "Ok! A gente tá te esperando."

    mc "Beleza. Já tô saindo."

    if julia_namoro:

        mc "Beijos."

        g "Beijão, gostoso!"

    "..."

    if julia_namoro:

        "Caraca... ainda não acredito que eu falei pra [g] que queria namorar com ela. E o pior é que ela aceitou!"

        "Como será que vai ficar isso aí? Tá louco?"

        "A [g] sempre foi doida... mas eu sei que lá dentro daquele corpo gostoso tem algo a mais."

        "Ela já me demonstrou outras vezes e é isso que me conquistou. E a safadeza, claro."

    if not j4_salvou:

        "Naquela noite a [g] tava trêbada. Não quero nem pensar no que o [caio] e aqueles outros caras fizeram com ela."

        "Será que eu devia ter tirado ela de lá?"

        if not caio_negou:

            "A proposta do [caio] foi muito boa."

            "A [g] já é adulta. Ela não precisa de mim pra decidir a vida dela. Não tenho que me sentir responsável pelos outros."

            "Ela é do jeito que ela é e isso é só culpa dela. Não vou me sentir mal por isso. Ela só tá colhendo o que plantou."

            mc "..."

            mc "Eu sei que eu tô certo... Mas por que então eu tô sentindo essa coisa no peito?"

            "Merda..."

    "Deixa eu ir pra facul dela."

    scene black with Dissolve(1.0)

    call locomocao from _call_locomocao_8

    scene universidade fachada with Dissolve(1.0)

    "Parece que eu tô vindo mais aqui do que quando eu tava fazendo o curso de jornalismo..."

    mc zerado "..."

    scene uni_hall corredores with Dissolve(1.0)

    mc desconfiado "Onde será que elas tão?"

    mc "Hm?"

    show 4olhos hall_explicando with dissolve

    "Que beleza. A [o] ali."

    mc normal "[o]!"

    o "Ah?"

    hide 4olhos with dissolve

    show 4olhos hall_mc with dissolve

    o "[mc]!"

    mc "Boa noite. Tudo legal?"

    if not j4_salvou:

        o "Legal? Como assim legal?"

        mc desconfiado "Quê? Que foi?"

        o "..."

        o "Já esqueceu, cabeça de vento?!"

        mc envergonhado "Desculpa, mas não tô entendendo."

        o "Não lembra da outra noite?! A gente combinou que você ia na festa ajudar a [g]!"

        mc "Ah, sim. Que que tem?"

        o "Como que que tem?!"

        o "A Mari me contou que a [g] causou um monte! Não era nem pra ele ter visto o [caio]!"

        o "Ela disse que ela tava na mesa de bilhar e... olha, nem vou falar nada."

        mc desculpa "Eu... queria ter ajudado mais, mas a [g] é grande. Ela tem as coisas delas."

        o "É assim que você tá tentando se desculpar? Se não pela [g], você devia ter feito por mim."

        o "Bah... esquece."
    else:


        o "Oi, [mc]. Tudo legal, sim."

        o "A Mari me contou que você não deixou a [g] na mão daqueles moleques ridículos."

        o "Muito obrigada."

        mc envergonhado "Não foi nada."

        mc charmoso "Era o mínimo que eu podia fazer por ela e também depois de você ter me pedido ajuda."

        show 4olhos ola with dissolve

        o "Você cumpriu sua parte do acordo. Fico te devendo uma."

        mc "Vou cobrar."

        o "O-ok..."

        o "Só que nosso trabalho com a [g] ainda tá longe de acabar..."

        mc desconfiado "Como assim?"

    scene carol_mc_corredor with Dissolve(1.0)

    o "A [g] não é uma pessoa fácil, [mc]. Ela tem problemas sérios."

    o "E a amizade dela com esses moleques só tá despertando o que ela tem de pior."

    menu:
        "O que você quer dizer com isso?":


            mc "Como assim o que ela tem de pior?"

            o "Isso não é óbvio pra você?"

            mc "Não tem nada óbvio pra mim."

            o "Então você precisa prestar mais atenção nas pessoas."

            o "Você acha que a vida é igual esses jogos de celular que vai te explicando tudo do começo e nem deixa você apertar outros botões?"

            o "A vida não tem tutorial, [mc]!"

            o "Abre o olho!"

            mc "Haha... tá, ok. Não precisa ficar brava."

            o "..."
        "Você tem a mesma idade dela, mas parece uma velha falando assim.":


            mc "[o]..."

            mc "Você parece uma velha falando assim, toda sabida e preocupada."

            o "Sério mesmo, [mc]? Você não vê o que tá em jogo aqui?"

            mc "Você parece realmente preocupada."

            o "E-eu tô! Isso não é brincadeira!"

            mc "Ok..."

    o "Olha... a [g] claramente tem problemas de aceitação. Eu não sei nada sobre a infância dela, mas obviamente ela procura aceitação."

    mc "Aceitação desses caras você diz?"

    o "Também..."

    o "Ela busca aceitação de todo mundo. E ela vai fazer o que for preciso pra conseguir isso."

    mc "Isso parece sério mesmo..."

    o "Sim! E tem muita gente por aí. E o pior é quem se aproveita disso pra conseguir o que quer."

    o "Pro [caio] e outros tarados ter a [g] nas mãos deles é excelente."

    "Pensando agora... talvez até eu tenha me aproveitado do jeito da [g]..."

    mc "Tá. Mas o que isso tem a ver com a gente?"

    scene carol_mc_corredor with hpunch

    g "Ei!"

    o "Xiu!"

    scene julia_carol_uni2 with Dissolve(1.0)

    g "O que vocês tão falando aí?"

    menu:
        "A [o] tá preocupada com você.":


            $ j5_carol_contou = True

            mc desculpa "Na verdade a [o] tá preocupada com você depois da festa do [caio]."

            o "[mc]!"

            g "Eu já não falei pra você me deixar minha vida em paz, [o]?"

            o "Eu sou sua amiga, [g]. Nunca vou deixar de me preocupar com você."

            g "Só que você se preocupa demais e com tudo. Isso vai deixar você com cara de velha."

            mc envergonhado "..."

            o "[g]..."

            g "Tô mentindo?"

            o "Não importa isso..."

            g "Eu não sei você, mas não tenho dinheiro pra plástica, então se eu ficasse com cara de velha eu só ia me matar."

            mc angustiado "!"

            o "Não fale isso nem de brincadeira."

            g "Que seja..."

            mc zerado "Essas duas..."
        "Nada não.":


            mc envergonhado "Não foi nada..."

            o "O [mc] só veio falar comigo. Não foi nada."

            g "Vocês tão de duplinha escondendo as coisas de mim?"

            mc surpreso "Tá doida?! Claro que não!"

            g "Sei..."

            o "..."

        "Eu tava chamando a [o] pra dar uns pegas." if not julia_namoro:

            mc safado "Eu tava vendo se a [o] não queria dar uns pegas."

            g "A é?! Fala de mim, mas já tá dando em cima dele, né, Carolzinha..."

            o "E você acredita nesse idiota?"

            g "Hmmm..."

            mc envergonhado "..."

            g "Não gosto quando fazem dupla contra mim."

            o "Eu não tô fazendo nada. Ele que tá te zuando."

            g "[mc]!"

            mc "Era só brincadeira."

            g "{i}grrrr{/i}"

    if j4_salvou:

        scene julia_carol_mc with hpunch

        g "O [mc] me carregou lá na festa do idiota."

        g "Eu tava meio bêbada."

        mc "Meio?"

        g "Me deixa!"

        g "Daí ele me pegou e me carregou. Parecia tipo um super homem."

        mc "Só existe um super homem. Você quer dizer que parecia um super herói."

        g "Você quer apanhar?"

        if julia_namoro:

            mc "Você contou pra ela que agora a gente tá namorando?"

            o "Quê?!"

            g "Ah. Tem essa também."

            o "Como assim?!"

        o "E chega vocês dois! Separar!"

    scene julia_carol_uni with Dissolve(1.0)

    g "Chata..."

    o "Você que chamou o [mc] hoje?"

    g "Sim."

    if not j4_salvou:

        g "Eu tinha um negócio pra falar com ele... Mas agora perdi a coragem."

        o "É bom você se desculpar pelo que faz de errado."

        g "Como você sabe que eu fiz alguma coisa?"

        o "E eu não te conheço, [g]?"

        g "Tá falando igual uma mãe."

        o "..."

        o "Então eu vou sair fora e deixar vocês conversando."

        g "[o]! Não me deixa!"

        o "Tchau pros dois."

        mc desculpa "Tchau."

        g "Chata!"

        scene julia_mc_universidade with Dissolve(1.0)

        g "O-oi."

        mc "Oi."

        g "É... Valeu por ter vindo."

        mc "De boa. É sobre a festa?"

        g "É..."

        "Que merda. Só dela falar isso eu já sinto uma ansiedade."

        g "Eu fiquei feliz de você ter ido lá."

        mc "Que bom..."

        g "Só queria ter certeza que você não ficou chateado com... tipo, o que você viu lá."

        g "E se, tipo, a gente continua de boa."

        mc "Sei..."

        g "Você sabe que esse é meu jeito. Eu curto uma farra."

        if julia_e1 == "seducao" or julia_e2 == "seducao" or julia_e3 == "seducao":

            g "A gente já teve nossas farras também, né?"

            mc "... Sim..."

        g "Não sei porque eu tô falando isso pra você. A gente não tem nada um com o outro."

        g "Mas sei lá, só queria sabe se tá tudo legal."

        menu:
            "Tá tudo de boa.":


                mc "Tá tudo de boa."

                g "Certeza?"

                mc "Sim."

                scene uni_hall corredores with dissolve

                show garconete e_emburrada with dissolve

                g "Não vai me dar bronca?"

                mc envergonhado "Claro que não."

                g "Hmm..."

                mc desculpa "Não tô falando que eu concordo com tudo, mas quem sou eu pra falar o que você tem que fazer?"

                mc charmoso "Quando você quiser conversar comigo, eu vou tá aqui."

                g "Valeu, [mc]."

                g "Você pareceu com a [s] agora."

                mc desconfiado "Sério?"

                g "Sim. Ela é a única que me aceita. Que me entende."

                g "E agora você... valeu, mesmo."

                mc normal "Relaxa. Mas você promete que se quiser conversar sobre alguma coisa fala comigo?"

                g "..."

                mc "Nem sempre guardar tudo pra você é o melhor."

                g "T-tá..."

                mc charmoso "Agora você pareceu a [s]."

                show garconete e_resignada with dissolve

                g "Ei..."

                jump j5_chama_cinema
            "Não tá. Se você não se respeitar, ninguém vai te respeitar.":


                $ j5_brigou_uni = True

                mc "Olha, [g]... Não quero que você me leve à mal, mas tem algo errado acontecendo aqui."

                mc "O que aconteceu lá na festa não foi certo."

                mc "Você bêbada, se expondo daquela forma, desesperada procurando atenção daqueles idiotas."

                g "!"

                g "Ma-"

                mc "Espera. Escuta."

                mc "Você não precisa disso. Você pode encontrar amigos de outra forma. Pessoas que não abusam da sua fraqueza."

                mc "Eu quero seu bem e por isso que tô falando isso."

                if julia_seducao_evento > 0:

                    g "?!"

                    g "[mc]..."

                    scene uni_hall corredores with hpunch

                    show julia e_putassa with hpunch

                    g "Que merda você tá falando?!"

                    g "Chamar atenção?! Amigos?! Você fumou crack!?"

                    mc preocupado "[g], calma."

                    g "O que eu faço com meu corpo só diz respeito a mim!"

                    g "Bem que você abusou da 'minha fraqueza' quando você teve vontade, né?!"

                    if julia_e1 == "seducao":

                        g "Quando você meteu a mão no meio das minhas pernas lá no parque!"

                    if julia_e2 == "seducao":

                        g "Tava certo quando você me fez tirar a roupa lá em casa quando a [s] tava recebendo o prêmio!"

                    if julia_e3 == "seducao":

                        g "Quando eu paguei um boquete pra você aqui do lado na biblioteca!"

                    g "Aposto que lá não teve problema!"

                    g "A [o] pelo menos tem moral pra cobrar qualquer coisa de mim!"

                    g "Você não passa de um hipócrita! Agora SAI DAQUI!"

                    mc desculpa "[g]-"

                    show julia e_putassa with hpunch

                    g "SAAAAAIIIII!!!!"

                    mc angustiado "T-tá. Tô saindo."

                    g "IDIOTA!"
                else:


                    g "..."

                    g "V-você não sabe nada, [mc]."

                    g "Você parece a [o]. Vocês só me criticam."

                    g "É fácil olhar pros outros e apontar o dedo. Você não sabe o que tá acontecendo comigo."

                    g "Ficam me julgando!"

                    mc "[g]..."

                    g "Só sai daqui. Por favor."

                    g "Eu não quero ver você agora."

                    mc "Po-"

                    g "Sai!"

                    mc "Tá..."

                jump j5_uni_ruim
    else:


        g "Eu tava meio cansada de ouvir você me xingar por causa da festa do [caio]."

        o "Sério mesmo que você tá usando o coitado pra desviar do assunto?"

        mc zerado "..."

        g "Era o único jeito."

        o "[g]..."

        o "E o pior é que você conseguiu. Vou nessa."

        g "Não creio! Funcionou mesmo! Valeu, [mc]!"

        scene uni_hall corredores with hpunch

        g "E não é que ela foi mesmo?"

        mc envergonhado "Verdade..."

        show garconete e_resignada with dissolve

        g "Valeu por ter vindo."

        mc normal "De boa."

        if julia_namoro:

            mc charmoso "Agora a gente tá sério, né? Então é massa poder falar com você."

            g "'Tá sério'... olha só pra você falando, que fofo."

            mc "Eu sei que você tá zoando porque tá com vergonha."

            g "Já tá se achando muito, rapaz."
        else:


            mc normal "Eu sempre tenho tempo pras minhas amigas."

            g "Falando assim até parece que você tem muitas."

            mc zerado "Ei..."

        g "Falar a verdade, nem eu tenho certeza direito por que eu te chamei hehe..."

        mc zerado "..."

        show garconete e_emburrada with dissolve

        g "Acho que... eu só queria agradecer pela outra noite."

        g "Você foi super legal comigo. A Mari até me contou que você foi contra o [caio]."

        mc desconfiado "Tá chamando ela de Mari agora?"

        g "Me deixa. Acho que ela não tem culpa de nada."

        mc charmoso "Alguém tá amadurecendo?"

        g "Nossa. Você tá insuportável, [mc]."

        mc feliz "Haha. Que exageiro."

        label j5_chama_cinema:

            g "Ah... amanhã o pessoal da sala vai sair no cinema."

        if julia_namoro:

            g "Agora... agora que a gente tá junto... você quer ir como... sabe, namorados?"
        else:


            g "Depois de tudo o que você fez, acho que eu queria que você fosse comigo. Quer ir?"

        mc desconfiado "Pessoal da sala? Como assim? A [o]?"

        g "Não... a [o] não gosta de sair."

        mc serio "Não vai me falar que você tá falando do pessoal da festa."

        g "Sim."

        mc surpreso "!"

        mc desconfiado "Sério isso ou tá me zuando?"

        g "Como assim?"

        "Isso é sério? Ela ainda quer sair com esse povo?"

        if julia_namoro:

            mc "Mesmo com a gente namorando? Não tô acreditando nisso."

        "Mano..."

        menu:
            "Sério que você ainda vai sair com essas pessoas?":


                $ j5_brigou_uni = True

                mc bravo "Sério mesmo que você ainda quer sair com esses caras?"

                g "Como assim? Eles são meus amigos."

                mc irritado "Que amigo, [g]?! Os caras só tão se aproveitando de você!"

                mc bravo "Não tô acreditando que tô ouvindo você falar desse povo ainda!"

                g "Você tá parecendo um idiota agora."

                mc "Eu um idiota?! Certeza que sou eu?!"

                hide garconete with dissolve

                show julia e_putassa with dissolve

                g "Para de enrolar e fala logo o que você quer falar!"

                g "O que você quer dizer?!"

                mc "Depois daquela festa não era pra você querer nem chegar perto dessas pessoas!"

                g "Como assim?! Que festa?! Não aconteceu nada demais lá! Eu só bebi um pouco!"

                mc "Um pouco?! Você tava quase tirando a roupa naquela mesa!"

                g "..."

                g "Não quero mais falar com você, seu babaca! Sai daqui!"

                mc "..."

                mc "Garota mimada!"

                g "Seu- seu- molengão!"

                mc "..."

                jump j5_uni_ruim
            "Tudo bem. Eu topo.":


                $ j5_cinema = True

                mc envergonhado "Beleza, se você realmente quer sair com essa galera..."

                g "S-sério mesmo?"

                g "Você não liga de sair com eles?"

                mc desculpa "Óbvio que eu ligo. Se eu pudesse escolher, eu gostaria que você nunca mais se envolvesse com essa turma."

                mc envergonhado "Mas eles são seus amigos. Provavelmente você conhece eles mais do que me conhece."

                if julia_namoro:

                    mc "Além de que eu não quero ser aqueles namorados que chega pra mudar a vida da mina."

                show garconete e_provocando with dissolve

                g "Caraca, [mc]."

                mc desconfiado "Que foi?"

                g "Você parece tão confiante no seu taco falando assim."

                if julia_namoro:

                    g "Fiquei até excitada agora."

                mc envergonhado "Haha..."

                g "Valeu por entender. Vai ser bacana."

                mc "Vamos ver..."

                g "Então é amanhã, tá? Eu vou chegar umas quatro. Vai ser aqui nesse cinema do centro."

                mc normal "Ah. Eu sei onde é."

                g "Ok."

                g "Então... até amanhã."

                mc "Até."

                hide garconete with dissolve

                "Que despedida foi essa? Será que tá tudo legal?"

                "Agora pegar busão de novo pra voltar."

                "Amanhã, sair com esse pessoal..."

                mc zerado "Não vai ser fácil."

                jump j5_continua

    label j5_uni_ruim:

        scene universidade fachada with Dissolve(1.0)

        "..."

        "Caralho, ela surtou."

        "Tudo foi tão rápido que eu nem sei como a gente chegou nessa briga."

        if j4_salvou:

            "Não tinha como eu aceitar esse negócio dela querer sair com esses caras de novo. Isso não vai fazer bem pra ela."
        else:


            "Eu só queria que ela entendesse a gravidade da situação. Não queria parecer um inimigo pra ela... que saco..."

        "???" "Ei. Você."

        mc desconfiado "Hm?"

        if caio_negou:

            show caio_varanda puto with dissolve

            caio "Veja só se não é o cavaleiro protetor da piriguete."

            mc bravo "[caio]..."
        else:


            show caio_varanda confiante with dissolve

            caio "Fala aí, [mc]. Beleza?"

            mc envergonhado "E aí?"

            caio "Curtiu a pauta que eu te passei?"

            mc charmoso "Curti, sim."

            if distrito_atencao > 0:

                mc "Até já passei pra revista."

                caio "Perfeito."

            caio "Tem muito mais de onde saiu essa, viu?"

            mc "Bom saber."

        show caio_varanda tranquilo with dissolve

        caio "Amanhã eu vou sair com a [g], tá sabendo?"

        mc desculpa "E daí? Vai querer causar com ela de novo?"

        caio "Calma, cara."

        if not caio_negou:

            caio "Não é nada que você não tenha aceitado aquela noite lá no meu apê."

        caio "Só coisa de boa."

        caio "Se você quiser, pode aparecer por lá amanhã à tarde. Eu vou chegar com o [teo] umas quatro."

        caio "Vai ser aqui no cinema do centro."

        mc desconfiado "Por que você tá me falando isso?"

        if not caio_negou:

            caio "Ué. Aquela noite você foi brother. Eu só quero retribuir."

            caio "Não esqueça que a gente vai dividir a [g] igual. Ela é de todo mundo."

            mc desculpa "..."

            caio "Só relaxa. Vai ficar tudo bem."
        else:


            caio "Por que eu quero que você veja a [g] no seu habitat natural."

            mc bravo "..."

            caio "Ver como ela fica alegrinha com a gente. É uma putinha mesmo."

            mc "Cala a boca."

            caio "Haha! Vai ser massa, cara."

        caio "Aparece lá, beleza? Falous."

        hide caio_varanda with dissolve

        "Esse cara..."

        "O jeito confiante que o [caio] fala... Parece que ele sempre tem tudo sobre controle e sempre quer ver o circo pegando fogo."

        "Que se foda também isso. Deixa eu voltar logo pra casa e capotar."

        jump j5_continua

    label j5_continua:

        scene black with dissolve

        "..."

        $ dia += 1

        $ tempo = 2

        "{b}No outro dia, durante a tarde{/b}"

        if carro:

            scene carro_mc_cidade1 with Dissolve(1.0)
        else:


            scene mc onibus with Dissolve(1.0)

        "Vou chegar depois das quatro. Acabei dormindo demais."

        "Só que... ainda não consigo entender porque a [g] quer sair com essas pessoas."

        "Será que ela não vê que eles são todos babacas?"

        if j4_salvou:

            "Depois que eu tirei ela da mesa naquela noite, eu achei que ela ia perceber o que ela tá passando."

            "Eu pensei que... depois que ela visse que eu era um amigo dela, ela pensaria melhor nessas coisas."
        else:


            "E o pior é que eu deixei ela lá na festa do [caio]."

            "A merda é que eu só reforcei esse comportamento. Será que se eu tivesse ajudado ela, ela agiria diferente agora?"

            "Se eu pudesse voltar no tempo..."

            "Que merda eu tô pensando? Haha..."

    "Opa. Tô chegando. Deixa eu descer."

    scene cidade centro12 with Dissolve(2.0)

    pause

    "Aqui é o cinema que a [g] comentou."

    "Esse é o que fica mais perto da universidade, então provavelmente é esse aqui. E eles falaram do centro e esse é conhecido como 'cinema do centro'."

    "Não acredito que tô nervoso de ir no cinema igual um adolescente."

    mc zerado "A que ponto chegamos..."

    "Bora."

    scene black with dissolve

    "..."

    scene cinema geral with Dissolve(2.0)

    pause

    "Caraca. Faz muito tempo que eu não venho aqui."

    "O lugar é até bacana, mas antes de virar paparazzo eu não tinha ninguém pra trazer pro cinema."

    "Sem namorada, sem amigos. Mano, tô até ficando depressivo agora. Se e-"

    "???" "HAHAHA!"

    "Garota" "Paaara!"

    mc desconfiado "Essa voz?"

    scene julia_cinema_galera with Dissolve(1.0)

    pause

    mc surpreso "!"

    caio "O que seria da gente sem a Julinha e a Mari?"

    teo "Seria uma bosta."

    g "Não ia ter nenhuma bunda pra vocês ficarem olhando."

    caio "A bunda do [teo] até que não é de se jogar fora."

    g "Aiii, [caio]. Mas é verdade, [teo]."

    teo "Cala a boca, [g]! Hahaha!"

    mari "..."

    caio "A [mari] também não fala porra nenhuma. Sorte que é gostosa."

    teo "Eu já te falei que você é muito gata, [mari]?"

    mari "Já..."

    g "Concordo. É gata bagarai."

    mari "Haha... até você, [g]."

    caio "É legal ver vocês se dando bem."

    "Pera! Para!"

    "O-oque a [g] tá fazendo com esses caras?!"

    if julia_namoro:

        "Mesmo com a gente namorando... como ela pode..."

        "Calma, [mc]."

        "Mano, não consigo! Tô muito puto de ver ela assim!"

    "Acho que eu não acreditava que ela realmente ia tá com eles aqui. Acho que eu tava em negação."

    "Tenho que chamar ela."

    mc desconfiado "[g]?"

    g "Ent- Ah! [mc]!"

    if julia_namoro and j5_cinema:

        $ j5_beijo = True

        g "Finalmente você chegou!"

        g "Vem aqui, seu gostoso!"

        mc surpreso "!"

        scene julia_cinema_beijo with hpunch

        pause

        g "Hmmm!"

        g "Que bom ver você. Aqui eu posso te beijar tranquila."

        "Que susto..."

        mc "Hmmm..."

        mc "Também quero te beijar."

        g "Hmmm..."

        "..."

        mc "Acho q-que tá bom. Tá todo mundo olhando."

        g "Tá."

    scene cinema geral with Dissolve(1.0)

    g "E aí?"

    if not j5_cinema:

        show julia_cine incomodada with dissolve

        g "É... O que você tá fazendo aqui?"

        mc desculpa "O [caio] me disse que vocês iam tá aqui umas quatro."

        g "Que babaca..."

        mc desculpa "Eu sei que a gente discutiu ontem, mas muito mancada você não ter falado nada."

        g "Por que? Ontem você me irritou, não queria te ver."

        mc serio "Mas a gente pode conversar e acertar as coisas, pô."

        g "Não tenho paciência pra isso, [mc]."

        if julia_namoro:

            mc desculpa "Nem agora que a gente tá namorando você acha que vale à pena?"

            g "!"

            show julia_cine triste with dissolve

            g "..."

            mc "..."

        g "É..."

    elif j5_cinema and not j5_beijo:

        show julia_cine feliz with dissolve

        g "Que legal que você veio. Achei que você não ia vir."

        mc "Eu me atrasei um pouco, mas não ia furar com você."

        g "Acho bom mesmo."

    g "Olha aqui!"

    g "O que você achou?"

    mc desconfiado "Achei do que?"

    g "Como o que? Disso aqui, idiota."

    show julia_cine provocando with dissolve

    pause

    mc surpreso "!"

    g "Tô ou não tô gata?"

    "Por as conversas sempre acabam assim quando tô falando com ela?"

    menu:

        "Eu achei essa roupa meio curta..." if julia_seducao <= 15:

            $ j5_roupa = True

            mc desconfiado "Essa roupa não tá mostrando muito?"

            g "Sério, [mc]? É isso que você vai falar?"

            mc envergonhado "Ué. Só dando minha opinião."

            mc "Não gosto que olhem pra você e foquem só no seu corpo. Esse tipo de roupa passa uma imagem."

            show julia_cine incomodada with dissolve

            g "..."

            mc "Que foi?"

            g "Você fica pegando no meu pé!"

            g "Você gosta ou não de andar com uma garota deliciosa?"

            mc "[g]..."

            if julia_namoro:

                mc charmoso "Agora que a gente tá juntos, eu me preocupo mais com essas coisas. Não é normal?"

                g "Sei lá se é normal, mas eu só quero que você e todo mundo olhem pra mim e deixem uma babinha escorrer pela boca hehe..."

                mc zerado "[g]..."

                g "Namorar uma delícia é melhor que uma freira, concorda?"

                mc envergonhado "Não é esse o ponto."

                g "Que seja."
        "Óbvio que tá gata! Delícia!":


            mc safado "Você sabe que você tá uma delícia. Gata é pouco. Vontade de morder."

            g "Assim que eu gosto de ver você. Doidinho."
        "Você sempre tá bonita. Não importa a roupa.":


            mc charmoso "Você não tá gata, você É linda. Não é por causa da roupa. É você."

            g "Como é charmoso esse [mc]."

            g "Mas tô gostosa também, né?"

            mc envergonhado "Tá, sim, [g]..."

            g "Ah bom."

    if not j5_roupa:

        g "É ou não é muito melhor a gente falar de como eu fico gostosa do que ficar discutindo coisa séria?"

        mc charmoso "Com certeza é mais agradável."

        mc "Mas mesmo não sendo 'melhor', às vezes a gente pre-"

        g "Xiu! Só olha pra minha bunda."

        mc envergonhado "Haha..."

    g "Ixi. O povo tá tudo olhando pra cá. Vamos lá. Vou te apresentar eles direito."

    mc desconfiado "Ok..."

    hide julia_cine with dissolve

    g "Vem."

    "..."

    scene julia_cinema_galera_perto with Dissolve(1.0)

    pause

    g "[mc], essa é minha turma."

    g "Turma, esse é o [mc]."

    caio "Sua turma, é?"

    mc normal "Prazer."

    mari "Oi, [mc]."

    mc envergonhado "Oi, [mari]."

    teo "Fala ae, cara. Eu te vi lá na festa do [caio]."

    mc normal "Verdade."

    "Eu tive o desprazer de ver você pegando na [g]..."

    caio "..."

    if caio_negou:

        caio "Eu conheço esse cara."

        g "Que foi, [caio]?"

        caio "Nada..."

        g "Ixi."

        "Eu neguei a proposta do [caio] na festa. Por isso que ele deve tá puto desse jeito."

        "Não vou com a cara desse moleque. Se acha muito e pelo que a [mari] falou, ele ainda tem esse tipo de controle sobre os outros."

        "Em mim essa porra não funciona."
    else:


        caio "Opa! O [mc] já é parça nosso."

        g "Sério? Vocês se conheciam?"

        caio "Ué, a gente se falou um monte lá na festa. Ele fez a boa pra gente."

        g "Ah. Eu não lembro muito bem do que aconteceu hehe..."

        caio "Também, bebeu igual um camelo."

        g "Para!"

        teo "Não dá pra negar, né, Julinha? Você tava pegando fogo."

        g "Ai! Chega de falar disso!"

        "Aquele dia o [caio] me passou uma pauta. Bem que ele podia me passar outra. Sempre ajuda."

    g "Ah. A gente precisa comprar."

    mari "Já compramos. Só você e o [mc] que precisam."

    g "Ah então tá. Vamos, [mc]?"

    mc normal "Claro."

    scene cinema geral with Dissolve(1.0)

    mc normal "Ei."

    if not j5_cinema:

        mc desculpa "A gente acabou discutindo ontem e talz..."

        show julia_cine incomodada with dissolve

        g "De novo isso? Que que tem?"

        mc envergonhado "Deixa eu me desculpar com você. Vou pagar tudo hoje."

        g "Sério mesmo que você acha que vai me comprar com dinheiro? Igual uma puta?"

        mc preocupado "Não. Não era iss-"

        show julia_cine provocando with dissolve

        g "Ok. Eu aceito."

        mc desconfiado "Hm?"

        g "É o mínimo. Um bom agrado."

        mc envergonhado "Ahaha... que bom..."
    else:


        mc normal "Pode deixar que eu pago pra você."

        g "Sério?"

        show julia_cine provocando with dissolve

        g "Alguém tá querendo algo comigo hoje. Eu aceito."

        mc charmoso "Pode ficar à vontade."

        g "Valeu, [mc]."

    g "Então vamos logo!"

    hide julia_cine with moveoutright

    mc surpreso "Calma! Não vamos perder o controle!"

    "..."

    scene julia_cinema_comprando with Dissolve(1.0)

    pause

    g "Moça, a gente quer duas entradas e uma pipoca do maior tamanho, e uma bebida do maior tamanho. E isso aqui?"

    "Vendedora" "Isso é um chocolate espec-"

    g "Chocolate! Tô dentro. Pega dois."

    mc envergonhado "[g]. Eu não quero, obrigado."

    g "Isso que tô pegando é só pra mim. O seu depois você vê."

    mc zerado "O-ok."

    g "E pra depois, uma balinha desta aqui."

    "Vendedora" "Certo."

    g "Agora acho que tá bom."

    g "E você, [mc]?"

    mc surpreso "Ah!"

    mc envergonhado "Não tô com fome..."

    g "Mas isso não é pra matar fome. É só pra divertir."

    mc "Entendi..."

    "Vendedora" "Ficou C$ 109,96."

    mc surpreso "Ce-cento!?"

    mc envergonhado "Passa no crédito, por favor."

    "Vendedora" "Ok. Prontinho."

    mc "Valeu..."

    g "Boa. Agora tô pronta."

    g "Só que eu tenho que esvaziar pra encher. O banheiro é aqui do lado, né?"

    "Vendedora" "Isso. Esta porta na lateral."

    g "Já venho."

    mc normal "Tá."

    scene cinema geral with Dissolve(1.0)

    "Bom..."

    mari "Ei."

    mc normal "[mari]?"

    mari "Vem aqui."

    scene cinema entrada with Dissolve(1.0)

    mc normal "Oi, [mari]."

    show mari n_feliz with dissolve

    mari "Oi."

    mari "Que bom que você veio também."

    mc envergonhado "Por que?"

    mari "Sei lá. Eu só fui com sua cara eu acho."

    mc charmoso "Talvez você tenha gostado do que aconteceu na festa."

    if caio_negou:

        mari "Sim. Eu te falei aquele dia. O jeito que você foi contra o [caio] foi, tipo... bem inspirador."

        mc envergonhado "Não sei se é pra tanto assim."

        mari "Foi sim. Eu pelo menos achei bem especial."
    else:


        mari "Talvez..."

        mari "Você aceitou a proposta do [caio], agora você é um de nós."

        mc desconfiado "Não sei se é tão simples assim..."

        mari "Todos nós começamos com um favorzinho aqui, um outro ali. E de uma hora pra outra a gente já tava fazendo tudo o que ele falava."

        mc desculpa "Sei..."

        "Eu nunca vou deixar isso acontecer comigo..."

    mc desconfiado "Falando em [caio], cadê ele?"

    mari "Ele e o [teo] foram no banheiro."

    mc surpreso "!"

    "Merda... a [g] foi no banheiro também."

    "Mas eles não vão tentar nenhuma graça com ela aqui, né?"

    mc envergonhado "Talvez eu devesse dar uma olhada lá no banheiro também."

    mari "Preocupado com a [g]?"

    mc "Haha... talvez um pouco."

    mari "Vocês tão juntos?"

    if julia_namoro:

        mc normal "Sim. Desde a festa."

        show mari n_triste with dissolve

        mari "Sei..."

        mc desconfiado "?"

        mari "[mc]... você parece um cara muito bacana."

        mari "Eu vi o jeito que você tirou a [g] lá da mesa na festa. Eu comentei com tanta gente..."

        mari "Parecia tipo uma cena de filme."

        mc zerado "Ela só tava exagerando e não quis que eles se aproveitassem dela naquelas condições."

        mari "Sei... é que assim, não sei se você vai conseguir namorar a [g]."

        mc serio "Por que?"

        mari "Eu só acho que o jeito de vocês não combinam. Ela é desinibida e gosta de uma farra."

        mari "Não parece um jeito que vai combinar com você."

        mc desconfiado "Como você pode saber uma coisa dessas?"

        mari "Não sei. Só olhando na sua cara."

    elif j4_salvou:

        mc envergonhado "N-não... Somos só amigos."

        mari "Entendi."

        mari "Eu vi o jeito que você tirou a [g] lá da mesa na festa. Eu comentei com tanta gente..."

        mari "Parecia tipo uma cena de filme."

        mc zerado "Ela só tava exagerando e não quis que eles se aproveitassem dela naquelas condições."

        show mari n_triste with dissolve

        mari "Sei..."

        mc desconfiado "Que foi?"

        mari "Assim..."

        mari "É que eu não sei se a [g] merece isso."

        mc preocupado "Como assim? Por que?"

        mari "Ela é desinibida e gosta de uma farra. Eu sinto que talvez ela te faça mal."

        mc desconfiado "Como você pode saber uma coisa dessas?"

        mari "Não sei. Olhando na sua cara. Eu sinto que você não vai ser feliz querendo proteger ela de tudo isso."
    else:


        mc normal "Não. A gente só se fala."

        mari "Verdade. Aquele dia na mesa, você acabou deixando ela lá com os garotos."

        mc safado "Ela tava bem sexy."

        mari "Tava mesmo."

        mari "E vai saber o que fizeram com ela lá, né? Mas é o jeito dela, o que a gente pode fazer?"

        mc envergonhado "Sim..."

        "Será que realmente não tinha nada?"

    mc desculpa "..."

    mari "Ei."

    scene mari_cinema_abraco with Dissolve(1.0)

    pause

    mari "Esquece a [g] e fica comigo."

    mari "Eu vou saber cuidar de você muito melhor do que ela."

    mari "Eu prometo que eu vou ser só sua e eu largo esses panacas agora mesmo."

    "Q-que ela tá falando? Como assim?"

    "A [mari] com certeza é uma mina sexy e linda. E ela parece ser bem cabeça, mesmo andando com esses caras."

    "Eu sinto que ela não curte tanto essa turma e talvez queira conhecer outras pessoas."

    if julia_namoro:

        "Será que ela tá falando sério? Ela quer que eu largue a [g] por ela?"

        "Mas... assim... sem mais nem menos?"

        "Isso tá até me lembrando aquela vez no Tadaima, quando eu conheci a própria [g]..."
    else:


        "Mas o que ela quer dizer com 'esquece a [g] e me escolhe'?"

        "Será que ela acha que eu tenho alguma queda pela [g] e na verdade..."

    mari "Eu tô vendo sua cara de nervoso. Calma."

    mari "Só fica aqui comigo e deixa a [g] com os moleques lá."

    "A [g] tá no banheiro com os idiotas! Tinha até esquecido."

    "E agora?"

    menu:
        "Ficar e esperar a [g] com a [mari]":


            "Eu não vou me meter no que a [g] tá fazendo. Eu vou ficar com a [mari] aqui."

            "Ela já é grande e não precisa de mim pra saber que não tem que fazer nada com esses caras."

            "É isso aí. Melhor dar uma atenção pra [mari] e confiar na [g]."

            mc normal "Tudo bem."

            mari "Que bom que eu coloquei um pouco de juízo nessa cabecinha."

            mari "Aliás... e se a gente aproveitasse nosso tempo junto?"

            mc "A-aproveitar?"

            mari "Você sabe..."

            if julia_namoro:

                "Eu e a [g] tamo juntos agora... não ia ser certo eu ficar com a Mari assim..."

                "Ou será que..."

            label julia5_premium2:

                "Que perigo... o que eu faço agora? Será que eu consigo negar?"

            menu:
                "Bora se divertir.":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_22

                        jump julia5_premium2

                    mc "Uma curtidinha você diz... o que você tá pensando?"

                    mari "Hmm..."

                    scene black with dissolve

                    scene j5_new9 with Dissolve(1.0)

                    pause

                    mari "Eu tava pensando em um agradinho aqui..."

                    mc "M-mari!"

                    mari "Que foi?"

                    mc "Alguém pode ver..."

                    mari "Você fica bonitinho com vergonha. Mas você vai negar uma pegada gostosa aqui?"

                    mc "E-eu... você... você é bem corajosa..."

                    mari "Quem dera..."

                    mc "Olha o que você tá fazendo."

                    mari "Você acha que isso que é ser corajosa? Fazer sacanagem em público?"

                    mc "P-pra mim é..."

                    mari "Depois das coisas que eu tive que fazer... isso não é nada, bobo."

                    mari "Eu queria... ter coragem de não fazer isso."

                    mc "P-por favor, eu nã-"

                    mari "Não tô falando com você, [mc]. Eu tô fazendo isso porque eu quero."

                    mc "Você... tá falando do Caio?"

                    scene j5_new10 with Dissolve(1.0)

                    mari "É... mas não sou só eu. A [g]..."

                    mc "Por que vocês fazem isso? Vocês podiam só parar de atender esse cara!"

                    mari "Quem dera..."

                    mc "Por que é tão difícil?"

                    mari "Imagina se você fosse sozinho no mundo? Isso seria triste demais..."

                    mari "Querendo ou não o Caio protege a gente... ele tá do nosso lado..."

                    mc "Mari... mas a contrapartida que ele exige é... demais, não é?"

                    mari "O que é aguentar os caprichos do Caio se isso significa tá num grupo que aceita você?"

                    mc "Hmm... cada pessoa é de um jeito, né? Eu não ligo tanto de ficar sozinho."

                    mari "Você não acha horrível?"

                    mc "É legal estar com as pessoas, dividir as coisas, mas se eu tiver que ficar sozinho, eu fico na boa."

                    mc "Com certeza é melhor do que ficar com pessoas que me fazem mal."

                    mari "[mc]..."

                    scene j5_new9 with Dissolve(1.0)

                    mc "E-ei!"

                    mari "O que você falou foi tão bonito... merece um prêmio."

                    mari "Vem aqui agora!"

                    mc "Uou!"

                    scene black with dissolve

                    scene j5_new11 with Dissolve(1.0)

                    pause

                    mc "M-mari!"

                    mari "Me beija, [mc]!"

                    mc "Hmm... q-que aconteceu?"

                    mari "Eu quero ficar com você."

                    mari "Eu quero que você grude o máximo em mim!"

                    mc "A-ah..."

                    mari "Eu quero que você fique comigo. Eu quero ser sua."

                    mc "Mari... eu... eu não posso... assim..."

                    mari "Você precisa aceitar ficar comigo. Mesmo que você tenha outras!"

                    mc "C-calma..."

                    mari "Beijar não é o suficiente? Pega em mim então!"

                    scene j5_new12 with Dissolve(1.0)

                    pause

                    mari "Isso, aqui na minha coxa, na minha bunda."

                    mc "Hm... você é muito gostosa."

                    mari "Tá gostando de pegar aqui? Eu adoro minha coxa e minha bunda."

                    mc "São quentes mesmo."

                    mari "Pode aproveitar. Eu tô sentindo que você tá ficando duro."

                    mari "Eu quero que você aproveite, [mc]."

                    mc "Eu vou aproveitar bastante."

                    mari "Então aperta! Assim!"

                    mc "Hmmnn... você sabe provocar, Mari."

                    mari "Eu sei fazer tudo. Se você ficar comigo eu faço você gozar todo dia."

                    mc "Eu..."

                    mari "Me pega, [mc]. Vai!"

                    mc "O-opa!"

                    scene j5_new13 with Dissolve(1.0)

                    pause

                    mari "Se aproveita de mim! E fica comigo!"

                    mc "Mari... a gente nem se conhece direito..."

                    mari "Me beija!"

                    mc "Hnng..."

                    "A Mari tá doida... ela parece tão excitada agora."

                    mari "Você promete que vai pensar?"

                    mc "No quê?"

                    mari "Em ficar comigo de verdade? Ser sua escolhida?"

                    mc "E-eu prometo."

                    mari "Na próxima vez que a gente sair... você pode experimentar tudo, ok?"

                    mc "T-tudo?"

                    mari "Você vai ver como eu sou boa, [mc]..."

                    mari "Imagina se você pudesse ficar comigo e com a [g]?"

                    mc "As duas?!"

                    mari "Aposto que eu e ela não íamos ligar... talvez até fosse bom..."

                    mc "Você toparia algo assim?"

                    mari "Com certeza... você é um cara que merece."

                    mc "Falando nela, ela deve tá voltando... mas eu prometo que eu vou pensar."

                    mari "Tá, gostoso... pode me soltar agora."

                    mc "O-opa..."

                    scene black with dissolve

                    mc "Você e a [g]..."
                "Melhor a gente parar por aqui.":


                    mc "M-melhor a gente não exagerar."

                    mari "Só uma esfregadinha... certeza?"

                    mc "C-certeza. Você é incrível, mas eu quero tomar cuidado."

                    mari "Tá..."

                    scene black with dissolve

            scene cinema entrada with Dissolve(1.0)

            mari "Isso."

            show mari n_feliz with dissolve

            mari "A [g] é grande."

            mari "E se você realmente quer algo com ela, você precisa deixar ela voar."

            mc envergonhado "Não sei..."

            mari "Vai por mim. Eu sou garota igual ela e tenho a mesma idade. Um ano a mais, mas tô mais perto que você mesmo assim."

            mc zerado "Ei..."



            "..."
        "Ir até o banheiro e ver o que tá acontecendo":


            $ j5_banheiro = True

            mc envergonhado "É-é melhor eu dar uma olhada nela."

            mari "Se você acha..."

            mc "C-com licença."

            scene cinema geral with Dissolve(1.0)

            "Ufa."

            "Senti que tava começando a rolar mó clima entre eu e a [mari]."

            "Mas tô mais preocupado com a [g]. O que será que ela tá fazendo no banheiro até agora com aqueles dois?"

            "Acho que é uma boa chance de ver se realmente a [g] tá tomando jeito."

            "Depois do que rolou na festa, seria bom ela ter um pouco mais de consciência que esse povo não faz bem pra ela."

            "Acho que eu consigo ouvir o que tá rolando se eu ficar escondido..."

            scene cinema_olhando_banheiro with Dissolve(1.0)

            "Assim..."

            "Se eu deixar só um pouco aberto, acho que dá pra ouv-"

            g "{size=17}Aaiiii! Para!{/size}"

            menu:
                "Abrir a porta e ver":


                    "Eu tenho que ver o que ela tá fazendo."

                    g "Só você tá aqui?"

                    teo "O Caio também."

                    g "E cadê el-"

                    scene j5_new1 with hpunch

                    pause

                    caio "Bú!"

                    g "Q-que você tá fazendo, doido?!"

                    caio "O que você acha de uma baguncinha no banheiro?"

                    g "Pirou de vez!"

                    caio "Eu sei que você gosta quando os outros tão olhando pra você."

                    g "Não!"

                    if julia_namoro:

                        g "Agora eu tô namorando o [mc]! Não posso mais fazer essas coisas!"

                        caio "Ah! Cala a boca! Você nunca foi fiel quando tava comigo. Vai ser agora com esse palerma?"

                        g "Você nunca mereceu!"

                        caio "E ele merece?"

                        g "Merece... ele é um cara decente!"
                    else:


                        g "A gente tá tentando ter uma coisa oficial e você quer me dividir com o Téo?!"

                    g "E v-você tá me deixando sem ar..."

                    caio "Só me escuta uma coisa e daí eu deixo você ir. Hm?"

                    label julia5_premium1:

                        g "Lá vem você com historinha... eu sei exatamente onde isso vai acabar."

                    menu:
                        "Escutar o que ele vai falar":


                            if not premium:

                                call mensagem_premium from _call_mensagem_premium_23

                                jump julia5_premium1

                            g "Tá bom... que que é?"

                            scene j5_new3 with vpunch

                            g "AKH!"

                            g "Tá me apertando! O que é?!"

                            window hide

                            pause

                            caio "A Mari me contou que você tá com um fogo esses tempos."

                            g "A Mari é uma bocuda! E daí?!"

                            caio "Ficar sem gozar deve ser um inferno, ainda mais pra você."

                            g "Cala a boca!"

                            caio "Se você gosta de ser uma cadela no cio, eu não vou brigar com você."

                            g "Hmm..."

                            caio "Mas se você quiser um alívio, a gente pode tentar uma coisa diferente aqui."

                            caio "Uma coisa bem apimentada... aposto que você vai curtir bastante."

                            g "Com os dois?! Ao mesmo tempo?!"

                            caio "Um em cada buraquinho... imagina?"

                            g "Ah..."

                            caio "Você gemeu só de pensar, né?"

                            g "..."

                            caio "Eu conheço você. Você adora ser tratada igual lixo. É sua natureza."

                            caio "Esse tipo de homem que trata de você com cuidado... você não consegue ter prazer assim."

                            caio "Você quer que te dominem e tratem você igual uma puta barata. Fala a verdade!"

                            menu:
                                "...":


                                    g "Nnng... ah..."

                                    caio "Tá vendo? Você não consegue negar quem você é."

                                    g "Aah... o que vocês vão fazer comigo?"

                                    caio "Assim que eu gosto."

                                    caio "Vem aqui, Téo. Me ajuda com essa aqui."

                                    scene black with dissolve

                                    scene j5_new4 with Dissolve(1.0)

                                    pause

                                    g "Ahng!"

                                    teo "Você tá ok com isso, Ju?"

                                    caio "Cala a boca e abusa dela. Não estraga tudo, idiota."

                                    teo "Tá... caralho... deixa eu mexer nela aqui."

                                    caio "Isso aí. Pode fazer o que quiser com essa aí."

                                    g "Ai, Téo... quem deixou você mexer aí?"

                                    caio "Cala a boca, vagabunda."

                                    g "Ai, grosso..."

                                    caio "Chupa meu dedo enquanto o Téo prepara você."

                                    g "Eu já tô molhadaann..."

                                    caio "Você tá com tanta vontade assim?"

                                    g "Eu não... vocês tão me forçando."

                                    caio "Essa é a história, então? A gente tá forçando?"

                                    g "Claro. Eu não quero nada disso."

                                    caio "Olha que puta mentirosa."

                                    g "Ah..."

                                    teo "Ela tá ficando cada vez mais molhada."

                                    caio "Tá na hora. Eu fico na frente."

                                    scene j5_new5 with Dissolve(1.0)

                                    pause

                                    g "Não acredito que vocês vão querer fazer ao mesmo tempo..."

                                    caio "Pra saciar uma arrombada tem que ser assim."

                                    g "Ah..."

                                    teo "Não é fácil meter aqui..."

                                    caio "Vai que você consegue."

                                    g "Tenham calma, garotos. Não precisa-"

                                    caio "Xi! Deixa que a gente tá acostumado comer você. A gente sabe."

                                    g "Tá... só não vão me rasgar... muito..."

                                    caio "Haha! Parece que alguém entrou no clima!"

                                    g "Eu nem sei mais direito o que tá acontecendo... HM!"

                                    caio "Entrei!"

                                    teo "Calma... eu vou..."

                                    g "AANNG!"

                                    teo "Delícia!"

                                    caio "Boa! E aí, gata?!"

                                    g "Me arrombando na frente e atrás! Vocês são loucos! AHNN!"

                                    caio "É bom, né?!"

                                    g "É! É bom! Vai!"

                                    caio "Ela quer mais, Téo! Força!"

                                    g "AHNN!"

                                    scene j5_new6 with vpunch

                                    g "ASSIM!"

                                    g "É muito bom! Vai! Pode ir mais forte!"

                                    window hide

                                    pause

                                    g "ANH! AANNGH!"

                                    caio "Ah!"

                                    g "Vai seus desgraçados, comam! VAI!! AANG!"

                                    teo "Uau... eu nunca vi a [g] animada desse jeito!"

                                    caio "Eu sabia que ela ia curtir uma dupla!"

                                    g "Eu tô sentindo! Vai! Não para!"

                                    caio "Vai gozar?!"

                                    g "Ainda não! Continua!"

                                    teo "Eu não sei quanto tempo eu vou aguentar teu cuzinho me apertando!"

                                    g "Não para! Não! Por favor!"

                                    caio "Essa buceta é um buraco negro!"

                                    g "Vai, caralho! Fode! FODE!"

                                    g "HNNG!"

                                    caio "Vai gozar?!"

                                    g "Não! Eu preciso de mais!"

                                    caio "Impossível!"

                                    teo "Ela ficou super molhada quando eu peguei ela pelo pescoço na mesa de sinuca."

                                    g "Isso! Aperta meu pescoço!"

                                    caio "Deixa com a gente!"

                                    scene j5_new7 with vpunch

                                    pause

                                    g "Isso! Não deixa eu respirar!"

                                    teo "Caralho, [g]!"

                                    caio "Essa puta é maníaca!"

                                    g "Axxxim! Vaainnnxx!"

                                    g "UUUHH!!"

                                    g "UUGHH!"

                                    teo "Ela vai morrer, Caio!"

                                    caio "Continua!"

                                    g "NNNNNGGHH! UUKH!"

                                    g "AAIINN!!"

                                    g "GOZAAZ!!!"

                                    scene j5_new8 with vpunch

                                    g "AAAAAANNHH!"

                                    caio "Tá gozando?!"

                                    g "Tô! Tô gozando! Tô gozando!! AAAHIHI!!"

                                    g "AAIINHN!!"

                                    caio "Uau... essa foi boa..."

                                    g "Nossa... aah..."

                                    caio "Isso aí, gata. Quando você quiser se divertir de verdade... você sabe quem pode te ajudar..."

                                    g "Caralho..."

                                    scene black with dissolve

                                    caio "Bora vazar que com esse grito que ela deu..."

                                    g "Saiam logo..."

                                    "..."
                                "Não! Sai fora!":


                                    g "Chega de falar tudo o que vem na sua cabeça, seu merda! Você nem me conhece!"

                                    caio "O que você disse?"

                                    g "Eu falei que NÃO!"

                                    caio "E desde quando você fala 'não' pra mim?"

                                    g "Desde agora... me solta, Caio."

                                    caio "Ei... calma... você sempre foi minha gatinha, então... só faz o que eu tô falando, tá?"

                                    g "Me solta!"

                                    caio "Eu não vou te soltar, sua puta!{nw}"

                                    scene j5_new2 with vpunch

                                    pause

                                    g "Eu mandei você me soltar, seu filho da puta!"

                                    caio "AAAGGH! MEU SACOO!"

                                    g "Tá aí! Acabei de acabar contigo e com todos seus descendentes!"

                                    g "Pelo menos não vão ter outros imundos por aí igual você!"

                                    caio "Sua vaca!"

                                    scene black with dissolve

                                    g "Falous!"
                        "Chutar ele e vazar do banheiro":


                            g "Eu disse que não..."

                            caio "E desde quando você fala 'não' pra mim?"

                            g "Desde agora... me solta, Caio."

                            caio "Ei... calma... você sempre foi minha gatinha, então... só faz o que eu tô falando, tá?"

                            g "Me solta!"

                            caio "Eu não vou te soltar, sua puta!{nw}"

                            scene j5_new2 with vpunch

                            pause

                            g "Eu mandei você me soltar, seu filho da puta!"

                            caio "AAAGGH! MEU SACOO!"

                            g "Tá aí! Acabei de acabar contigo e com todos seus descendentes!"

                            g "Pelo menos não vão ter outros imundos por aí igual você!"

                            caio "Sua vaca!"

                            scene black with dissolve

                            g "Falous!"
                "Ficar apenas ouvindo":


                    "É melhor eu não correr o risco."

                    teo "{size=17}Não tô fazendo nada, louca!{/size}"

                    g "{size=17}Hahaha! Safado!{/size}"

                    caio "{size=17}A gente só tá matando a saudades de você.{/size}"

                    g "{size=17}Imagina se alguém entra agora e vê uma moça sozinha com dois caras no banheiro?{/size}"

                    teo "{size=17}Que que tem?{/size}"

                    g "{size=17}Não ia pegar bem pra mim!{/size}"

                    caio "{size=17}Olha... não ia ser sua primeira vez.{/size}"

                    g "{size=17}Afe, [caio]! Hahaha!{/size}"

            "[g]..."

            "Deixa eu sair daqui."

            scene cinema geral with Dissolve(1.0)

            "Não é possível isso..."

            if julia_namoro:

                "Mesmo ela assumindo o namoro comigo..."

                "Ela continua... nem sei nem o que pensar agora."

            "..."

            scene cinema entrada with Dissolve(1.0)

            mari "Voltou?"

            mc desculpa "Sim."

            mari "O qu-"

    g "Olá!"

    mari "Olha eles aí."

    scene julia_cinema_galera_perto with Dissolve(1.0)

    g "Voltei, [mc]."

    mc desculpa "Oi."

    caio "Vamos? Já deu a hora."

    g "Vamos."

    g "[mc], você pegou as coisas que eu comprei?"

    mc desculpa "Não. Nem peguei."

    g "Vou lá. Vão na frente."

    caio "Vamo logo."

    scene black with dissolve

    "..."

    scene cinema sala_corredor with Dissolve(1.0)

    caio "Vão achar um lugar pra gente. Eu vou trocar uma palavrinha com o [mc]."

    mc desconfiado "?"

    "Téo e Mari" "Tá."

    show caio confiante with dissolve

    caio "E aí?"

    if caio_negou:

        mc bravo "Que foi, [caio]?"

        caio "Calma, cara."

        mc "Eu tô calmo. O que você quer falar?"

        caio "Eu sei que a gente não fechou aquele dia na festa, mas pra mim isso já são águas passadas, belê?"

        mc desconfiado "..."
    else:


        mc normal "E aí?"

        caio "Tudo de boa. Valeu por ter deixado a gente curtir a [g] na festa aquele dia."

        mc charmoso "De boa. Foi massa ver ela lá."

        caio "Né?"

        mc normal "O que você quer falar?"

    caio "Então. A [g] tem falado bastante de você."

    caio "Tipo, é a primeira vez que eu vejo ela preocupada com a opinião de alguém igual agora."

    mc desconfiado "E daí?"

    caio "Então... Eu e o [teo] tamo pensando em dar uma brincada com ela hoje no cinema."

    mc zerado "..."

    caio "Daí eu queria poder contar com você."

    mc "Contar comigo?"

    caio "Mesma coisa que eu te pedi na festa. Só ficar de boa e deixar a gente."

    caio "Finja que não tá vendo nada, belê?"

    mc "..."

    show caio tranquilo with dissolve

    caio "Se você quebrar essa, a gente deixa a [mari] do teu lado e você pode tipo mandar seus papos nela."

    caio "E talvez eu tenha informações que sejam importantes pra você e pra sua revista."

    g "O que tão fazendo aí, meninos?"

    caio "Nada. Já tô subindo. Não se atrasem."

    hide caio with dissolve

    g "Vamos, [mc]?"

    mc "Opa..."

    scene cinema sala_bancos with Dissolve(1.0)

    mc desconfiado "Eu nem sei que filme que a gente vai assistir..."

    show julia_cine feliz with dissolve

    g "E o que importa? Quem vem pro cinema assistir filme?"

    mc zerado "Todo mundo?"

    g "Todo mundo que não tem ninguém pra se pegar. Tudo forever alone."

    mc envergonhado "[g]... não é bem assim."

    show julia_cine feliz at esquerda with move

    show caio confiante with dissolve

    caio "Vão ficar namorando aí? Senta logo."

    show caio confiante at direita with move

    g "A gente já tava indo."

    caio "Eu e o [teo] guardamos um lugar pra você aqui."

    show julia_cine incomodada with dissolve

    g "Guardou? O cinema tá vazio..."

    caio "Foda-se. Eu quero que você sente aqui com a gente."

    if julia_namoro:

        "!"

        "Esse cara só pode tá brincando. Ela é minha namorada."

        "A [g] não vai..."

    show julia_cine triste with dissolve

    g "M-mas, [caio]... Eu queria ficar a-"

    show caio irritado with dissolve

    caio "Vem logo, [g]."

    g "!"

    g "T-tá. Calma."

    g "Desculpa, [mc]. Mas é só durante o filme, tá?"

    "..."

    if julia_namoro:

        "Quê?!"

        "Como ela pode fazer isso?! A gente tá... a gente tá..."

    if not j4_salvou:

        "Eu vou deixar a [g] na mão de novo?"

        "E além disso, eles vão se divertir com ela no meu lugar?"

    caio "A [mari] faz companhia pro [mc]. Não esquenta."

    g "Mas-"

    caio "Vem!"

    "Eu vou ficar quieto e deixar ele fazer o que quiser?"

    "Mas será que eu realmente me importo assim com a [g]? Será que a [mari] não tá certa?"

    "Talvez o jeito da [g] e o meu nunca combinem. Ela acabou de aceitar sentar com ele..."

    "Minha cabeça tá à milhão. O que eu faço?"

    menu:
        "Falar pra eles que a [g] ficará do seu lado.":


            mc bravo "Espera!"

            "Caio e Júlia" "Ahn?!"

            mc "Cala a boca, [caio]. Você não percebeu que a [g] quer sentar em outro lugar?"

            g "[mc]! Eu! Eu..."

            caio "Fica quieto, imbecil..."

            caio "Eu sei o que é melhor pra [g]. Eu conheço ela muito mais tempo do que você."

            caio "Quando ela tava sozinha, fui eu que ficou do lado dela."

            caio "Você não passa de um amiguinho que ela fez aí esses dias."

            g "[caio]..."

            caio "A [g] provavelmente já estaria morta se não fosse por mim. Eu que fiz ela sair da depressão, não você."

            caio "Então agora cala sua boca. Vamos, [g]."

            g "E-eu..."

            if j4_salvou:

                g "[caio]... calma."

                g "E-eu quero sentar com o [mc]. D-desculpa."

                caio "Quê?! Voc-"

                mc irritado "Você ouviu ela, [caio]. Dá o fora!"

                if julia_namoro:

                    g "A gente tá namorando e eu quero curtir o filme com ele, só isso, tá?"

                caio "..."

                hide caio with dissolve

                jump j5_cinema_good
            else:


                g "..."

                show julia_cine incomodada with dissolve

                mc desconfiado "Hm?"

                g "Relaxa, [mc]. Não precisa fazer uma tempestade."

                g "É só um lugar no cinema. A gente se fala depois."

                mc preocupado "Mas, [g]. Não é só isso. É você poder fazer o qu-"

                g "Xiu. Bom filme."

                "..."

                caio "Senta ali do lado do [teo]."

                g "T-tá."

                g "Até depois, [mc]."

                jump j5_cinema_bad
        "Não falar nada.":


            "..."

            caio "Senta ali do lado do [teo]."

            g "T-tá."

            g "Até depois, [mc]."

            jump j5_cinema_bad

    label j5_cinema_good:

        $ j5_good = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("j5_good","julia","personagem")

        g "[mc]..."

        mc charmoso "Tá tudo bem. Não precisa ficar preocupada."

        g "T-tá..."

        g "É a primeira vez... primeira vez que eu falo assim com o [caio]."

        mc "Ele vai entender. É só um lugar no cinema, certo?"

        g "A-acho que sim..."

        mc "Vem. Vamos sentar."

        scene cinema_sala_julia with Dissolve(1.0)

        pause

        g "Você ficou bem puto ali."

        mc desculpa "Não quero que abusem de você."

        if julia_namoro:

            g "Que namorado ciumento..."

            mc desconfiado "Acho que aquilo passava um pouco de ciúme, né?"

            g "Ele só queria que eu sentasse com ele. Não é nada de mais."

            mc zerado "Sei..."

        g "Mas eu gostei..."

        mc desconfiado "Do quê?"

        g "Do jeito que você me defendeu."

        g "Me deixou bem excitada, sabia?"

        "Essa mina não tem todos os parafusos. Certeza."

        mc envergonhado "A é?"

        scene cinema_sala_julia_avanca with Dissolve(1.0)

        pause

        g "O que você acha de uma recompensa?"

        mc "N-não sei..."

        g "Você mereceu..."

        if julia_namoro:

            "Mesmo namorando com ela, esse jeito ainda me pega desprevinido."
        else:


            mc "M-mas a gente é só amigo, lembra?"

            g "Amizade colorida, bobinho."

        "E agora?"

        menu:
            "Se entregar aos avanços da [g]":


                $ j5_beijo2 = True

                mc "Impossível recusar você, sua delícia."

                g "Assim que eu gosto."

                g "Deixa eu sentar em você."

                mc "U-uou!"

                scene cinema_sala_julia_beijo with Dissolve(1.0)

                pause

                g "Assim mesmo. Aproveita bem meus peitos. São pra você."

                mc "Hmmm..."

                g "Pode me beijar inteira, [mc]."

                g "Deixa eu me esfregar no seu colo."

                g "Ai."

                g "Eu tô sentindo você todinho aqui embaixo."

                g "Assim!"

                g "Beija mais, safado!"

                g "ANG!"

                label julia5_premium3:

                    pass

                menu:
                    "Segurar e continuar":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_24

                            jump julia5_premium3

                        g "Nem pensar! Segura aí!"

                        mc "J-júlia?! E-eu!"

                        g "Eu quero mais... vem aqui..."

                        mc "[g]... a gente já foi longe demais! O cinema tá vazio, mas tem gente pra lá..."

                        g "Não quero saber. A gente tá junto, tá na hora da gente consumar nosso lance."

                        mc "Mas aqui?"

                        g "Aqui é muito mais excitante... você sabia que eu era assim. E eu preciso que você faça eu gozar..."

                        "Ela tem razão... eu sempre soube que a Júlia tinha várias taras... transar em público deve ser uma..."

                        mc "Que seja, vem aqui."

                        scene black with dissolve

                        g "Hmmm..."

                        show white with dissolve

                        g "As luzes!"

                        mc "N-não!"

                        scene j5_new14 with vpunch

                        pause

                        g "Acenderam..."

                        mc "E agora?!"

                        g "Agora continua! Você tá dentro de mim!"

                        mc "Xxiiiuu!"

                        mc "Sorte que a Mari e os outros dois saíram..."

                        g "Para de pensar neles quando você tá metendo numa mulher!"

                        mc "E você para de gritar! Quer ser presa?!"

                        g "Presa transando?! Parece muito bom..."

                        mc "Merda!"

                        scene j5_new14 with hpunch

                        g "AIN!"

                        mc "Fica quieta que eu te como!"

                        g "Agoraan gosteii..."

                        mc "Agh..."

                        g "Isso, continua assim... seu pau é gostoso..."

                        mc "Hmm... você que é gostosa... e-eu não sei quanto tempo eu aguento assim..."

                        g "Você vai aguentar até eu mandar você gozar..."

                        g "Agora vai... mais forte..."

                        mc "Nngh!"

                        scene j5_new15 with Dissolve(1.0)

                        mc "Assim!?"

                        window hide

                        pause

                        g "Isso... assim... tá bom..."

                        mc "Aah... você é demais, Ju."

                        g "Eu sei... agora continua..."

                        "Se eu quiser que ela aproveite também, eu vou ter que segurar a barra."

                        "Mas como?! Ela é gostosa demais!"

                        mc "Você é gostosa demais..."

                        g "Você também..."

                        mc "Você gostou... do meu..."

                        g "Sim... vocês homens pensam demais em tamanho... isso não importa tanto."

                        g "Ritmo e resistência são muito mais importantes... ahn..."

                        g "Tipo... você tem que tá no ritmo da sua mulher, caralho... se ela tá no começo, não adianta querer furar ela com seu pau."

                        g "Esse seu jeito tranquilo... tá muito bom... mas você vai ter que acelerar... logo logo..."

                        mc "S-se eu acelerar... você vai fazer eu gozar, porra."

                        g "Azar o seu! Agora vai!"

                        scene j5_new15 with vpunch

                        mc "Nnngh!"

                        g "Issoo! Ahnnn!"

                        mc "[g]!"

                        g "Continua!"

                        mc "A-ah!"

                        g "Mais forte!"

                        "Eu não vou aguentar!"

                        menu:
                            "Gozar nela":


                                mc "Não aguento! Toma tudo!"

                                mc "aAAGH!"

                                g "Nnnnngg!"

                                g "Você me encheu de porra..."

                                mc "Eu tentei... mas você é boa demais..."

                                g "O que eu posso fazer... eu vou ter que continuar te treinando."

                                mc "Uau..."

                                g "Eu sei... é o tipo de treinamento que qualquer homem ia querer..."

                                mc "Haha... agora bora sair daquí..."
                            "Tentar resistir":


                                mc "UUGH!"

                                g "Ah... você tá segurando bem... ang..."

                                mc "Tá perto?"

                                g "Deixa eu sentar em você. Se eu controlar... eu consigo."

                                mc "Onde?! Aqui eu tô de costas pelo menos!"

                                g "Deita ali atrás das cadeiras."

                                mc "A gente ainda vai se ferrar..."

                                scene black with dissolve

                                scene j5_new16 with Dissolve(1.0)

                                pause

                                g "Agora, sim!"

                                g "Eu posso fazer ele entrar e sair do meu jeito! Ahn!"

                                mc "A-aghh! Eu vou explodir, [g]!"

                                g "Mais! Eu preciso de mais!"

                                g "Assim mesmo!"

                                mc "Nnnngg!"

                                g "Assim tá bom! Isso! Continua enfiando!"

                                mc "Ah!"

                                "Eu nunca cheguei nesse ponto! Parece que meu pau vai estourar!"

                                g "Segura! Você tá ficando mais duro!"

                                mc "Agh! Jú!! AAHG!"

                                g "Mais um pouco!"

                                menu:
                                    "Não aguento mais! AAH!!":


                                        mc "É o meu limite!"

                                        g "Então vai! Pode gozar!"

                                        scene j5_new16 with vpunch

                                        mc "AAAAGGH!"

                                        mc "Aagh...."

                                        g "Caralho... você gozou muito."

                                        mc "Minha nossa... acho que eu nunca senti isso..."

                                        g "Você foi melhor do que eu esperava..."

                                        mc "Eu tentei... mas você é boa demais..."

                                        g "O que eu posso fazer... eu vou ter que continuar te treinando."

                                        mc "Uau..."

                                        g "Eu sei... é o tipo de treinamento que qualquer homem ia querer..."

                                        mc "Haha... agora bora sair daquí..."
                                    "Continuar prendendo":


                                        mc "E-eu vou... morrer..."

                                        g "Para de escândalo! E continua duro desse jeito!"

                                        g "Eu vou acelerar!"

                                        mc "T-tá louca?!"

                                        scene j5_new17 with vpunch

                                        pause

                                        g "Assim! Desse jeito!"

                                        mc "..."

                                        g "Eu tô sentindo! Vai! Vai pau! Me come! AAGNH!"

                                        mc "E-eu!"

                                        "Agh! Tá doendo! Eu preciso!"

                                        g "Não para! Não goza! Deixa eu sentir mais! Eu preciso!"

                                        g "Fode! Me fode! Assim! Duro! Grosso!"

                                        g "Angg! AaaGH!!"

                                        mc "[g]! Chega! Não consigo!"

                                        g "Não! Ainda não! Fode mais!"

                                        scene j5_new17 with vpunch

                                        mc "AAAGH!"

                                        g "Annh... ahn..."

                                        mc "Minha nossa..."

                                        g "Não vou parar!"

                                        scene j5_new17 with vpunch

                                        mc "Para, louca! Tá doendo!"

                                        g "Foda-se!"

                                        scene j5_new17 with vpunch

                                        mc "AKH!"

                                        caio "Então por isso que vocês tão aqui até agora..."

                                        mc "C-caio?!"

                                        g "Sai pra lá, Caio! Eu tô quase gozando!"

                                        caio "Não parece que ele vai aguentar muito... olha a cara de dor do coitado, Ju."

                                        g "Azar o dele! Eu preciso!"

                                        caio "Bom... se vocês tiverem afim... eu e o Téo podemo ajudar."

                                        g "Hmm..."

                                        mc "Ajudar?!"

                                        caio "É... podemos dar uma mão... ou outro membro..."

                                        mc "Eu e a [g] tam-"

                                        g "O que você acha, [mc]?"

                                        mc "Tá falando sério?!"

                                        g "Se você topar..."

                                        caio "Essa mulher é insaciável, [mc]... não precisa se sentir péssimo por precisar de ajuda."

                                        teo "Ele tá certo. Nenhum de nós consegue..."

                                        "Não acredito que eu tô aqui ouvindo isso!"

                                        "Isso é completa loucura!"

                                        "Ou será que eu tô sendo cabeça dura?"

                                        "Eu tô pensando só em mim e esquecendo o prazer da minha namorada?"

                                        "O que eu faço?"

                                        menu:
                                            "De jeito nenhum!":


                                                mc "De jeito nenhum! Saiam agora daqui!"

                                                caio "Tá bom... que cara sem graça..."

                                                teo "Falous."

                                                g "..."

                                                scene black with dissolve

                                                "..."

                                                scene cinema sala_bancos with Dissolve(1.0)

                                                mc "[g]... é assim que você quer fazer as coisas?"

                                                scene cinema_sala_julia_sozinha with Dissolve(1.0)

                                                g "Era só uma ideia... não precisa ficar assim."

                                                mc "Eu quero que você tenha prazer... mas eu não consigo dividir você com os outros assim."

                                                g "Por enquanto..."

                                                mc "Nada de 'por enquanto'!"

                                                g "Ok..."

                                                mc "Eu prometo que eu vou te fazer se sentir muito bem."

                                                g "Você é um fofo... eu sei que você vai."

                                                mc "Tá... e desculpa qualquer coisa."

                                                g "Desculpa eu também."

                                                g "O que eu posso fazer... eu vou ter que continuar te treinando."

                                                mc "Uau..."

                                                g "Eu sei... é o tipo de treinamento que qualquer homem ia querer..."

                                                mc "Haha..."

                                                g "Mas chega de falar disso... eu tenho outra coisa importante pra falar."

                                                mc "Hm?"

                                                jump continua_julia5_premium3
                                            "Ok...":


                                                mc "Se é pra dar prazer pra ela... eu aceito."

                                                caio "uou... Tu é durão, cara."

                                                g "Incrível! Obrigada, [mc]!"
                                            "A [g] escolhe.":


                                                mc "Eu... a [g] escolhe."

                                                g "Sério?"

                                                mc "Eu não me sinto à vontade, mas é seu prazer... então..."

                                                g "Então eu quero!"

                                                mc "Ah..."

                                                "Claro que quer..."

                                                g "Obrigada, [mc]! Você é demais!"

                                        g "Venham, garotos! Venham cuidar da sua amiga insaciável!"

                                        mc "E eu?"

                                        g "Você usa sua lingua. Até ficar pronto de novo."

                                        mc "T-tá."

                                        scene black with dissolve

                                        scene j5_new18 with Dissolve(1.0)

                                        pause

                                        g "Assim... três... de uma vez... aah..."

                                        caio "Esse é um recorde até pra você, hein, safada?"

                                        g "É... tão excitante! Eu tô ficando loca!"

                                        teo "Olha pra cara de maluca da menina. Ela tá que não se aguenta."

                                        g "Claro, tem um cara me lambendo enquanto eu tenho dois caralhos na mão."

                                        caio "Eu sabia que você ia acabar voltando pra pedir nosso pau."

                                        g "Eu preciso gozar... só isso... vocês são dois consolos, só isso."

                                        g "Eu quero só o [mc] de verdade..."

                                        caio "Ah tá... entendi... aha."

                                        g "É sério! Só ele pode me foder na buceta."

                                        caio "Essa é a regra?"

                                        g "Claro. Eu sou uma boa garota."

                                        caio "Então é bom ele molhar sua bunda também, porque eu não saio sem sentir um buraquinho seu."

                                        g "Tá... é justo... [mc]... me lambe atrás."

                                        mc "Ju... eu..."

                                        g "Vem..."

                                        scene j5_new19 with Dissolve(1.0)

                                        g "Assim... hmmm... eu tô tão quente, [mc]."

                                        teo "Eu também."

                                        g "Eu tô vendo, o pau de vocês tá crescendo."

                                        caio "Tá na hora. Então vamo dividir direitinho."

                                        caio "Eu fico com a bunda, o [teo] com a boca e o namorado com a frente. De acordo?"

                                        g "Eu a-"

                                        caio "Não falei com você, falei com eles."

                                        g "Ah tá... haha..."

                                        teo "Eu queria-"

                                        caio "Você não quer nada."

                                        mc "O que a [g] quiser."

                                        g "Eu quero só você na buceta, [mc]. Você é meu namorado."

                                        caio "Tá ouvindo? Você tem vantagens por namorar ela."

                                        g "Tá. Ele lambeu o suficiente. Pode enfiar, Caio. Meu buraquinho tá chamando seu pau."

                                        caio "Com todo o prazer."

                                        g "E você vem, [mc]. Eu quero os dois ao mesmo tempo."

                                        mc "Ainda não sei s-"

                                        scene j5_new20 with Dissolve(1.0)

                                        pause

                                        g "AAGH!"

                                        caio "Ah! Como sua bunda é apertada!"

                                        g "NNGGH!"

                                        mc "Você tá muito molhada, [g]!"

                                        teo "Tomando nos três buracos ao mesmo tempo!"

                                        caio "Só assim pra essa vaca conseguir gozar!"

                                        g "Nngh!"

                                        caio "Mama nela, [mc]! Ela precisa de toda ajuda possível!"

                                        caio "A gente vai ter que acelerar, pessoal!"

                                        scene j5_new21 with hpunch

                                        g "Anh! AANNH! {i}cof{/i}"

                                        teo "Tá conseguindo respirar agora?"

                                        g "Ahh! Três caralhos! Três! ISSO!"

                                        caio "Ela nem sabe mais o que tá acontecendo."

                                        g "AH! FODE! AAHN! ARROMBA SUA VAGABUNDA!"

                                        mc "Ah, [g]! É isso que você queria!"

                                        g "ISSO! TUDO DE UMA VEZ!!!"

                                        g "Eu sou a putinha da galera! Podem me comer!"

                                        caio "A gente sabe! Toma!"

                                        "Isso é tão errado! Mas por que é tão excitante ao mesmo tempo!"

                                        g "Você tá cada vez mais forte, [mc]!"

                                        scene j5_new22 with vpunch

                                        caio "O parceiro aqui tá excitado mesmo!"

                                        mc "UGH!"

                                        g "ISSO! FODE!!"

                                        caio "Eu tô sentindo, ela tá quase!"

                                        g "TÔ LÁ! NÃO PAREM AGORA, FILHOS DA PUTA!!"

                                        g "METAM EM TUDO! METE NA GARGANTA, NO CU, NA BUCETA!"

                                        teo "Então toma!"

                                        g "NNNHNNG!!"

                                        mc "Ela tá ficando apertada!"

                                        g "NNGH! NNNGH!!!"

                                        caio "Goza, caralho!"

                                        scene j5_new23 with vpunch

                                        pause

                                        g "TÔ GOZANDO! GOZANDO!! FINALMENTEEE!!!"

                                        g "aaHAHAHAAAA!"

                                        mc "Eu também!! AAAGH!"

                                        scene j5_new23 with vpunch

                                        pause

                                        caio "Agora tem nós!"

                                        g "Claro! Pode gozar em mim! Me enche de porra!"

                                        g "Eu adoro porra! Me alimenta de porra! Todas as porras!"

                                        scene j5_new23 with vpunch

                                        "Caio e Téo" "AAAANNHH!"

                                        g "MARCAA SUA CADELAA!"

                                        scene black with Dissolve(3.0)

                                        teo "Falous..."

                                        caio "A gente se vê logo, casalzinho... "

                                        "..."

                                        scene j5_new24 with Dissolve(1.0)

                                        pause

                                        g "Ei..."

                                        mc "Opa..."

                                        g "Eu..."

                                        mc "..."

                                        g "Não queria que ficasse estranho entre a gente."

                                        mc "O que aconteceu aqui foi uma loucura."

                                        g "Eu sei... eu..."

                                        g "Essa sou eu, [mc]. Você não disse que não, então..."

                                        mc "Eu sei."

                                        g "Sabe? O quê? Me perdi..."

                                        mc "Desde o começo eu sei que você é uma doideira. Eu tinha uma ideia que as coisas iam ser assim."

                                        g "É... são assim..."

                                        mc "Eu aceitei você desse jeito. E não adianta eu reclamar agora."

                                        mc "Não sei quanto tempo eu vou tá ok com uma coisa dessas. Mas por hoje, pode ficar tranquila. Não vai ficar estranho."

                                        mc "Pra falar a verdade... eu acabei gostando também. É estranho, mas eu cheguei lá com você..."

                                        g "Eu senti... é... legal..."

                                        mc "[g]... eu acho que essa não é você. Que tem alguma coisa que você tá ignorando."

                                        g "É..."

                                        mc "Hm? Você concorda?"

                                        jump continua_julia5_premium3

                        scene black with dissolve

                        scene cinema sala_bancos with Dissolve(1.0)

                        scene cinema_sala_julia_sozinha with Dissolve(1.0)

                        jump continua_julia5_premium3
                    "Chegar no clímax":


                        mc "Eu não consigo!"

                        mc "Eu vou gozar!"

                        g "Isso! Pode soltar tudo!"

                        g "Aaahh!"

                        mc "Agh!"

                        mc "{i}puf puf{/i}"

                        scene cinema_sala_julia with Dissolve(1.0)

                        g "Foi rápido..."

                        mc safado "Alguém tava com muita vontade..."

                        g "É. Você."

                        mc "Talvez..."
            "Recusar a investida":


                mc "Você é linda e uma tentação, mas acho melhor a gente não partir pra esse lado aqui no cinema."

                g "Que chatão, [mc]..."

                g "Eu tô com muita vontade. É mancada deixar uma mina assim."

                mc "Haha. Usa sua energia sexual pra outra coisa."

                g "Sacanagem..."

                scene cinema_sala_julia with Dissolve(1.0)

                g "Como você aguenta?"

                mc envergonhado "Aguento o que?"

                g "Resistir. Se fosse o contrário eu já tava de quatro..."

                mc "Que exageiro..."

                g "Quem dera."

                mc charmoso "Bom. É óbvio que não e fácil. Eu também tenho vontade de transar."

                mc "Mas às vezes tem outras coisas mais importantes."

                mc desculpa "Assim, se a gente sempre ceder aos impulsos, qual vai ser nossa diferença pros animais?"

                g "Agora apelou."

                mc envergonhado "Malz. Mas é o que eu acho de verdade."

                g "Por um lado até que faz sentido."

                g "Por isso você é um cara tão diferentão, né, [mc]?"

                mc zerado "De novo..."

                g "É impossível não pensar isso. Você é a pessoa mais diferente das outras que eu já vi na vida."

                g "Você até me lembra um pouco a [o]... talvez eu devesse dar em cima dela..."

                mc "Ei..."

        caio "Cansei desse filme. Bora."

        teo "Já?"

        scene cinema sala_bancos with Dissolve(1.0)

        caio "Bora logo."

        g "Vocês já vão?"

        caio "Você não vai comigo?"

        g "Não. Vou ficar mais um pouco."

        caio "..."

        mari "Tchau, gente."

        mc normal "Tchau, [mari]."

        g "Falou, galera."

        "..."

        scene cinema_sala_julia_sozinha with Dissolve(1.0)

        pause

        mc charmoso "Parece que o [caio] não curtiu muito."

        g "Ele vai sobreviver..."

        mc "Também acho."

        label continua_julia5_premium3:

            pass

        g "[mc]. Quando você me salvou lá na festa e agora aqui, eu fiquei pensando numas coisas."

        mc normal "Tipo?"

        g "Assim, que talvez o que eu tô vivendo agora não é tudo o que eu tenho."

        g "Eu gosto dos meninos."

        mc zerado "Não sei como..."

        g "Eles são divertidos, e eles despertam uma coisa em mim. E eu gosto da [mari] também. Não quero abandonar eles."

        if julia_namoro:

            g "Mas minha promessa tá de pé. Eu não vou fazer nada com eles, tá? É tudo brincadeira."

            g "Nosso namoro tá firme."

            mc desculpa "É o que eu espero."

            g "Bom... contanto que você também não faça com ninguém."

            mc "Claro."

        g "Mas, então... por outro lado..."

        g "Você me mostrou que existe vida fora disso. Que eu não tô presa nesse lugar que me colocaram."

        g "E talvez largar tudo. Sair da faculdade, sair da casa da [s] e ir pra longe. Recomeçar."

        mc envergonhado "Isso não é um pouco drástico demais?"

        g "Eu sinto que pra mim vai ter que ser assim. Vai ser o único jeito."

        g "Só que eu não vou conseguir fazer isso assim. Eu acho... que eu quero saber mais sobre mim."

        g "Eu quero saber mais sobre meu passado. Sobre meus pais e como eu fui parar na casa da [s]."

        mc charmoso "Isso parece bem interessante, [g]."

        g "Você acha?"

        mc "Claro. Eu acho que isso vai te dar uma nova visão sobre as coisas. Muito legal mesmo."

        g "Talvez... acho que você tem razão. Não é uma ideia tão ruim, né?"

        mc "De jeito nenhum. E pode contar comigo, claro."

        g "Valeu... você é a coisa mais estranha e mais importante que aconteceu pra mim desde a [s], [mc]."

        g "Valeu por acreditar em mim."

        mc "Não se preocupe. Eu vou tá sempre com você."

        g "Galã."

        mc envergonhado "Haha..."

        scene cinema sala_bancos with Dissolve(1.0)

        g "Agora deixa eu ver o que sobrou do filme..."

        mc zerado "Pior que eu nem sei que filme é."

        g "Eu te disse..."

        scene black with Dissolve(1.0)

        "..."

        scene cinema geral with Dissolve(1.0)

        g "{i}smack{/i}"

        g "A gente se fala, lindo."

        mc normal "Tchau."

        "..."

        "A [g] é doidinha... mas é uma graça."

        "Esse [caio] é um filho da puta. Certeza que ele não vai desistir dela."

        "Ele acha que tem o mundo nas mãos. Hah! Otário..."

        jump j5_finaliza

    label j5_cinema_bad:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("j5_bad","julia","personagem")

        hide caio with dissolve

        hide julia with dissolve

        "..."

        "Deixa eu sentar com a [mari]."

        mc envergonhado "Olá."

        mari "Senta aqui."

        scene cinema_sala_mari with Dissolve(1.0)

        pause

        mari "Que bom que a gente vai poder conversar."

        mc envergonhado "É."

        mc "Aliás, eu queria te perguntar um negócio."

        mari "Pode perguntar. Eu deixo."

        mc "Você não parece eles três. Eu sei que vocês tem a idade parecida, mas não sei explicar, você parece meio um peixe fora da água."

        mari "Peixe fora da água? Quantos anos você tem?"

        mc zerado "Ei..."

        g "{size=17}Tá louco?! Não, [caio]...{/size}"

        mari "Eu entendi o que você quis dizer. Só tô zuando mesmo."

        mari "Não sei explicar também. Eu gosto deles. Eles são divertidos, mas eu meio que cansei."

        mc desculpa "Então por que só não encontra outras pessoas?"

        mari "Sei lá. Não é tão fácil assim."

        g "{size=17}Mas aqui?!{/size}"

        mari "Eu conheço eles há muito tempo. E eu não sei se eu ia me dar bem com os outros."

        mari "O [caio], o [teo], o Japa, a [g]... eles podem ser meio doidos, mas pelo menos eles tão aí comigo."

        mc desculpa "Sei..."

        g "{size=17}Tá bom! Vocês são impossíveis!{/size}"

        mc desconfiado "Que tanto a [g] grita?"

        mari "Não sei se você vai querer ver isso..."

        mc desconfiado "Ahn?"

        scene cinema_mari_julia_bad with Dissolve(1.0)

        pause

        "Q-que que a [g] tá fazendo ali?!"

        mari "Faz tempo que o [caio] queria transar com ela no cinema."

        mari "Parece que eles têm uma lista de lugares que eles querem cumprir..."

        mc preocupado "U-uma lista?"

        mari "Acho que é culpa dos hormônios. Eles queriam fazer comigo também, mas tá louco."

        mc "E a [g] aceitou isso?"

        mari "Ela sempre curtiu, bom pelo menos eu acho... A gente nunca se falou tanto. Só que de uns tempos pra cá ela meio que tava pulando fora."

        mari "Só que o [caio] tá sempre insistindo."

        mari "Ei!"

        scene cinema_sala_mari with Dissolve(1.0)

        mc desculpa "Que foi?"

        mari "Não fica pensando nisso, bobinho."

        mari "Conversa comigo."

        mc "[mari]... isso tá certo? Você acha isso certo?"

        mari "..."

        mari "Como assim certo?"

        g "{size=17}Ai!{/size}"

        mc "Não sei. Você acha que isso faz bem pra ela? Ou até pra eles?"

        mari "Como eu vou saber? Se eles tão curtindo... acho que faz."

        g "{size=17}Ai! Assim!{/size}"

        teo "{size=17}Ei. Deixa um pouco pra mim.{/size}"

        mc preocupado "..."

        mari "Tenta não pensar nisso."

        g "{size=17}AAH!{/size}"

        mari "O [caio] tem esse jeito... poderoso. Ele é confiante, ele passa uma energia que é difícil a gente aguentar."

        mari "Mas eu quero sair dessa, [mc]. E você parece que não me odeia, né?"

        mc envergonhado "Claro que não. Você é uma garota cabeça."

        mari "Então fica comigo?"

        mc surpreso "E-eu!"

        mari "Esquece a [g] com eles. Ela não te merece."

        "Eu não posso esquecer a [g]. Isso não tá certo. Nada disso faz sentido pra mim."

        mari "Acho que eles acabaram. Agora a gente pode ver o filme tranquilos."

        "O que eles tão fazendo? Eu tenho que olhar."

        scene cinema_julia_caio with Dissolve(1.0)

        pause

        g "{size=17}Não acredito que a gente fez isso aqui.{/size}"

        caio "{size=17}Por que? Você gostou, não gostou?{/size}"

        g "{size=17}S-sim...{/size}"

        caio "{size=17}Então foda-se. Eu disse que eu sei o que é melhor pra você.{/size}"

        g "{size=17}Mas não é isso, [caio]. Não é só gostar. E todas as outras coisas?{/size}"

        caio "{size=17}Que outras coisas? Eu cuido de você.{/size}"

        g "{size=17}Você me trai.{/size}"

        caio "{size=17}Você também.{/size}"

        g "{size=17}Esse é o problema. Eu não quero mais isso.{/size}"

        caio "{size=17}Claro que quer. Você nasceu assim. Você nasceu com esse fogo na buceta.{/size}"

        g "{size=17}...{/size}"

        g "{size=17}Não sei...{/size}"

        caio "{size=17}Eu sei. Só confia em mim.{/size}"

        if julia_namoro:

            g "{size=17}Além de que eu disse que ia namorar com o [mc].{/size}"

            g "{size=17}Eu não quero mais transar com você.{/size}"

            caio "{size=17}O idiota tá olhando ali e nem falou nada.{/size}"

            caio "{size=17}Às vezes ele até gosta...{/size}"

            g "{size=17}Ai. Fica quieto...{/size}"

        g "{size=17}...{/size}"

        "Eu não consigo mais olhar pra isso."

        "Não tô me sentindo legal. Melhor eu sair daqui."

        scene cinema_sala_mari with Dissolve(1.0)

        mc desculpa "[mari], valeu a conversa, mas eu vou embora."

        mari "Quê? Mas já?"

        mc "Acho que é melhor eu ir embora."

        mc charmoso "Mas eu gostei muito de falar com você."

        mari "Pensa no que eu falei. Eu quero te ver de novo."

        mc "Pode deixar. Até."

        mari "Tá. Tchau tchau."

        scene cinema sala_corredor with Dissolve(1.0)

        "Não quero fazer mais parte disso."

        "E eu vou tirar a [mari] dessa também. Se a [g] quiser, ela que fique com esses pau no cu."

        caio "Ei!"

        mc bravo "Hm?"

        show caio tranquilo with dissolve

        caio "Ufa. Quase não te alcancei."



        mc desculpa "Terminou o que tava fazendo?"

        caio "Só dei uma pausa. Valeu por tudo."

        mc "Não precisa me agradecer."



        caio "Mas desta vez eu não tenho nada pra você."



        mc "Não importa. Não quero nada."

        show caio confiante with dissolve

        caio "Não tô te entendendo. Ficou bravinho por que comi a [g] e você não?"

        mc "Não é isso... Só não sei se você é o melhor pra essas garotas."

        caio "O que é isso? Deu um ataque de santinho agora? O que importa se é bom pra elas? Se a gente tiver se aproveitando, tá bom, né não?"

        mc serio "Não sei... não sei se é certo ignorar pessoas assim. Mesmo que a gente saia ganhando."

        caio "[mc]... esse mundo é dos espertos. Eu achei que a gente fosse parecidos, mas já entendi que você é 'certinho' demais."

        caio "Você foi feito pra ser gado. Pra amaciar a carne pra gente como eu comer."

        mc desculpa "Eu realmente não sei o que é certo ou errado nessas situações. Com certeza não tenho essa certeza que você tem."

        mc "Pode rir à vontade. Mas eu acho que a [g] ainda vai ver o babaca que você é. E saiba que a [mari] já viu e vai pular fora logo."

        caio "Sério, mesmo? Como você é ingênuo, [mc]. Certeza que você é jornalista?"

        mc serio "O que você quer dizer?"

        caio "A [mari] só tava falando o que você queria ouvir pra você aceitar melhor nosso lance."

        caio "Mas parece que não adiantou. Então foda-se. A [mari] tá pouco se lixando pra você."

        caio "Elas são minhas. As duas. E você não pode fazer nada."

        caio "Eu faço com elas o que eu quiser. Elas me chupam e dão pra mim sempre que eu quiser."

        caio "E pra você nada, entendeu?"

        mc irritado "Foda-se, otário. Garoto mimado."

        scene black with dissolve

        caio "Hahahaha!"

        scene cinema entrada with Dissolve(1.0)

        "Que bosta..."

        "..."

        jump j5_finaliza

    label j5_finaliza:

        pass

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(1.0)

    pause

    $ tempo = 3
    $ v25_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v25_fim","julia","personagem")

    jump call_cidade

label julia_evento6_pre:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j6_save", extra_info="j6_save")

    $ julia_e6 = "pre"

    $ estou_na_cidade = False

    "Pensando bem... acho que hoje vou ficar um pouco mais na cama..."

    scene ape_cama with Dissolve(1.0)

    pause

    "Tava lembrando aqui daquele dia no cinema com a [g]..."

    if j5_good:

        "Foi muito bom ver o [caio] todo bravinho porque ela sentou comigo. Ele tinha certeza que ia dobrar a [g]."

        "Mas, pensando agora, é incrível como ele tem poder sobre ela. Por um instante, eu achei que a [g] fosse mesmo recusar sentar comigo."

        "O jeito que ele se sentiu contrariado só mostra que ele sente que tem ela na palma da mão dele. A questão é... como a coisa chegou nisso?"
    else:


        "Eu ainda não acredito o que ela faz no cinema com aqueles caras. Só de lembrar me dá um lance muito ruim."

        "Será que a [g] não percebe o que tá rolando? Que eles tão usando ela?"

        if not julia_namoro:

            "A gente é só amigos, eu não tenho direito nenhum a ficar cobrando ela..."

        "Mas eu sei que ela é uma garota que precisa de uma ajuda nisso. Só ver como a [o] fica preocupada com ela."

    "Por que a [g] continua indo atrás do [caio] mesmo depois de tudo isso?"

    "Ela tentou namorar ele e não deu certo. Ele ficou com a [mari] e sabe lá com quantas outras. Não dá pra levar ele à sério."

    "Mas então por que a [g] só não pula fora? Será que ela não consegue ver que esses 'amigos' não fazem bem pra ela?"

    "Eu tenho certeza que tem coisa aí. Não é só amizade de faculdade. Principalmente no rolo da [g] com o [caio]."

    if julia_namoro:

        "Agora que eu tô namorando ela, eu não quero mais isso. Ela disse que ia se esforçar pra gente ser exclusivos."

        "Mas não consigo sentir essa firmeza... Não quero duvidar dela e nem ficar de ciúme bobo, mas quero pelo menos entender."

    "Se eu entender o que tá rolando aí, eu tenho certeza que vou olhar pra [g] com outros olhos."

    "Mas provavelmente eu não vou ter mais essa liberdade com o [caio]. O rolo do cinema deve ter acabado com nossa 'amizade'."

    "Isso é outra coisa que me deixa intrigado. A [mari] disse que ele tem um 'poder' sobre os outros. O que ela quis dizer com isso?"

    "Por mais mala que ele seja, o [caio] com certeza é um cara confiante. Ele se sente o dono da padoca, o rei da cocada preta."

    "Da onde vem isso? Ele deve ser rico... no mínimo. Mas não acho que é só isso. Eu quer-"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "{i}Trr trrr{/i}"

    scene ape_celular_falando with Dissolve(1.0)

    mc "Alô?"

    g "Oie, gatinho!"

    mc "E aí, [g]? Tudo bem?"

    "Bem ela me ligando agora. Parece até filme..."

    if julia_namoro:

        g "Como vai o namorado mais gostoso e pintudo do mundo?"

        mc "Haha... vou bem."

        g "Eu também!"
    else:


        g "Eu tô legal, e você, lindo?"

        mc "Tô de boa."

    g "Te acordei?"

    mc "Nada... ia dar uma saída, mas resolvi voltar pra cama."

    g "Então tá deitado sem roupa? Hmmm..."

    mc "Da onde você tirou o sem roupa? Haha..."

    g "Aí! Não tá impressionado que eu tô acordada essa hora?"

    mc "Verdade... é bem cedo, né? Não é sua cara mesmo."

    g "E você não vai acreditar onde eu tô. Se você acertar, eu te dou uma recompensa bem safada depois."

    mc "J-júlia..."

    g "Vai logo, adivinha!"

    "Onde a [g] ia estar essa hora da manhã..."

    menu:
        "Faculdade":


            python:
                if renpy.android:
                    renpy.block_rollback()

            mc "Na... faculdade?"

            g "Errou!"

            mc "Óbvio que eu errei... até parece que você ia estar na faculdade. Sei lá porque falei isso."

            g "Ei! ... é verdade..."

            mc "Haha..."
        "Cinema":


            python:
                if renpy.android:
                    renpy.block_rollback()

            mc "Cinema?"

            g "Cinema nem deve tá aberto essa hora, mongol."

            mc "Verdade."

            g "Você nem tentou!"

            mc "..."
        "Aqui na ilha":


            python:
                if renpy.android:
                    renpy.block_rollback()

            mc "Aqui na ilha!"

            g "Talvez..."

            mc "Sério?!"

            g "Não."

            mc "..."

    g "Eu tô na biblioteca!"

    mc "Biblioteca? O que você tá fazendo aí?"

    g "O que uma pessoa vem fazer na biblioteca?"

    mc "Uma pessoa normal vai ler, você eu já não sei."

    g "Tá me trollando, né, vagal?"

    mc "Imagina... mas fala aí. Sério mesmo que tá na biblioteca?"

    g "Sérião."

    mc "E foi pra ler mesmo?"

    g "Isso aí."

    mc "..."

    g "Que foi? Por que tá quieto?"

    mc "Tô achando isso muito estranho."

    g "Nossa, que desconfiança..."

    menu:
        "Ok. Desculpa...":


            mc "Tá bom, você venceu. Tô surpreso que você tá lendo na biblioteca. Desculpa pela desconfiança."

            g "Acho bom. Mordeu a lingua."
        "Tô desconfiado mesmo.":


            mc "Ainda não comprei essa sua, não."

            g "Nossa! Você é um cuzão mesmo, [mc]."

            mc "Calma..."

    g "Mas é sério. Eu vim aqui estudar com a [o]. Ela disse que aqui tinha livros melhores pro que a gente tá vendo na facul."

    mc "Entendi. Bom pra você, [g]. Não tava botando fé, mas acho que você tá séria nesse lance de estudar."

    g "Sim..."

    mc "E por que ligou?"

    if julia_namoro:

        g "Não posso querer falar com meu gato?"
    else:


        g "Não posso querer falar com meu amigo?"

    mc "Pode, claro. Fiquei feliz de você ligar."

    g "Por que você não vem aqui? A gente vai ficar a manhã toda estudando, você podia vir junto."

    o "{size=17}[g]! Não era isso que a gente combinou!{/size}"

    g "{size=17}Relaxa! Eu sei que eu tô fazendo.{/size}"

    mc "Que que foi?"

    g "Foi nada. Você sabe onde é, né? A {b}biblioteca fica no museu aqui no centro{/b}."

    mc "Tô ligado. É uma porta que tem dentro do museu. Eu já passei por lá."

    g "Então tá. Tô te esperando!"

    mc "Mas eu n-"

    "{i}Tuu... tuu...{/i}"

    scene ape_celular with Dissolve(1.0)

    "Nem quis saber..."

    "Se eu quiser falar com elas, preciso ir até a {b}o museu agora de manhã e depois entrar na biblioteca{/b}."

    "É só {b}pegar o busão até o centro e entrar no museu{/b}. A biblioteca fica {b}dentro do museu{/b}."

    "Acho que vale a pena passar um tempo com a [g]."

    if julia_namoro:

        "A gente tá namorando, mas quase nem fizemos nada juntos direito até agora. Aqueles amiguinhos dela sempre tão no meio."

        "Essa pode ser uma boa oportunidade. Quem sabe até a gente pode passear pelo centro depois."

    "A [g] estudando é um caso à parte. Acho que dar um apoio pra ela pode ser bem positivo."

    "Bora lá."

    jump call_cidade

label julia_evento6:

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ julia_e6 = "evento"

    "???" "{size=17}Hahaha!{/size}"

    mc desconfiado "Hm? Normalmente aqui tá tão silencioso."

    "???" "{size=17}Shhhh!{/size}"

    mc envergonhado "Alguém já se incomodou com o barulho."

    "Deixa eu subir e ver o que tá rolando."

    scene biblioteca 2andar with Dissolve(1.0)

    "A [g] disse que ela e a [o] estavam aqui."

    mc surpreso "Ah! Tô vendo ela ali."

    "A [g] é realmente muito gata, tá doido."

    mc charmoso "Oi, Ju-"

    o "O-oi, [mc]. Bom dia."

    mc desconfiado "Hm?"

    scene carol_biblioteca_incomodada with Dissolve(1.0)

    pause

    mc normal "Oi, [o]. Tava indo dar um alô pra [g]."

    o "Eu sei, mas será que você pode esperar um pouco?"

    mc desconfiado "Hm? Por que?"

    o "A [g] me pediu pra vir com ela aqui pra ela estudar. Você deve imaginar como eu fiquei surpresa..."

    menu:
        "Você tá fazendo pouco dela...":


            mc envergonhado "Você tá fazendo pouco dela. Vai que a menina encontrou o caminho."

            o "S-será? Acho difícil, [mc]... mas quem sabe. Se for isso, vai ser realmente bom pra ela. A [g] precisa muito de algo pra ocupar a cabeça."

            mc "Concordo..."
        "Com certeza. Eu também fiquei.":


            mc envergonhado "Impossível não ficar, né? Isso não é a cara da [g] de jeito nenhum."

            o "Acho que se ela chegou até aqui na faculdade, foi mais por mim do que por ela."

            mc "Haha..."

            o "Então imagina a minha surpresa quando ela me disse isso."

            mc "Entendo completamente..."

    o "Ela disse que tá na hora dela levar mais à sério as coisas da faculdade e parar de pensar só em amigos e peguetes. Palavras dela, claro..."

    mc envergonhado "Haha..."

    if julia_namoro:

        "Agora que eu tô namorando ela, não sei se isso é uma boa."

        "Bom... não posso pensar só no que eu quero. A [g] realmente precisa de um pouco de sossego."

    mc normal "E daí vocês vieram pra cá."

    o "Isso..."

    mc desconfiado "Mas você não parece muito alegre"

    o "Ah..."

    scene carol_biblioteca_incomodada_close with Dissolve(1.0)

    pause

    o "Eu falei pra [g] que viria com ela, mas só se ela fosse estudar de verdade. Se fosse só pra passear, que ela saísse com a turminha dela."

    o "Só que daí não fez nem meia hora, ela queria chamar alguém pra vir 'estudar junto'."

    mc envergonhado "Estudar... sei..."

    o "Ela insistiu tanto e eu queria que ela não desistisse, então falei que ela podia ligar pra você. Só pra você."

    mc "Pra mim?"

    if j4_salvou:

        o "Você salvou ela daquela festa, lembra? Eu sei que você se preocupa com ela."

        if julia_namoro:

            o "Apesar que eu estou sabendo que vocês estão namorando."

            mc "Hehe..."

        o "Eu sinto que eu posso confiar em você."
    else:


        o "É... você foi sem noção aquela vez deixando ela ficar sozinha na festa com aqueles estrupícios, mas fazer o que..."

        o "Ainda é melhor que os outros. Eu quero confiar em você pelo menos."

    mc charmoso "Com certeza. Eu quero que você confie em mim mesmo."

    mc desculpa "Inclusive hoje eu tava pensando na [g]. Eu queria entender melhor o que rola entre ela e essa turminha aí."

    o "Hmm... olha, eu não sei exatamente. Eu conheci a [g] depois deles, mas e-"

    g "Oieee!"

    mc surpreso "J-júlia!"

    scene julia_carol_biblioteca1 with Dissolve(1.0)

    pause

    g "Cheguei, gatos e gatas!"

    o "Oi, [g]. Terminou aquela lista?"

    g "Aaaahhh.... no."

    o "[g]...."

    g "Mas eu escutei vozes. Eu queria ver quem era. E acertei em cheio!"

    if julia_namoro:

        g "Meu gato veio me ver! Tava com saudades!"

        o "E-ei! Calma aí! Nada de namoro aqui."

        g "Mas a gente quase nem namorou ainda!"

        o "Não é não."
    else:


        g "[mc]! Meu amigo com benefícios!"

        mc envergonhado "Benefícios?"

        o "Calma lá os dois. A gente tá aqui pra estudar."

        g "Não seja chata, [o]."

        o "Sou sim. Se controle, [g]."

    menu:
        "Você tá muito séria, [o]. Relaxa...":


            mc charmoso "Calma, [o]. Você tá muito nervosa..."

            o "Você também, [mc]?"

            g "Tá vendo, chatonilda? O [mc] entende que um pouco de bagunça faz parte também."

            mc envergonhado "Haha... um pouquinho não faz mal, certo?"

            o "Nada de um pouquinho... a gente veio aqui pra ler e fazer exercícios. Se vocês começarem de graça eu vou embora."

            g "Calma, calma. Era só brincadeira, não precisa ficar assim."

            mc "..."

            scene julia_carol_biblioteca2 with Dissolve(1.0)
        "A [o] tem razão. Não quero atrapalhar seus estudos.":


            mc normal "A [o] tá certa. Não vim aqui pra atrapalhar vocês."

            o "Isso mesmo. Obrigada, [mc]."

            scene julia_carol_biblioteca2 with Dissolve(1.0)

            g "Nãããoooo... Uma [o] XY não!"

            mc envergonhado "Não exagere..."

            o "Exatamente. A gente só tá fazendo o que a gente veio fazer aqui."

            g "Dois chatos..."

    o "Já está na hora de você começar a pensar no seu futuro, [g]. Você vai bombar em quase todas as matérias já no seu primeiro ano?"

    g "E daí? O que isso tem a ver com você?"

    o "Eu sou sua amiga, [g]. Eu quero ver você indo pra frente."

    g "Sei..."

    mc desconfiado "Que foi, [g]? Por que você tá falando assim com a [o]?"

    g "Não é da sua conta também."

    mc "Ei... não pre-"

    g "E se eu nem quiser terminar o curso? Hoje em dia fazer faculdade nem quer dizer nada. Tá todo mundo sem emprego."

    o "Então porque a situação não tá fácil você vai se complicar ainda mais?"

    mc preocupado "Ela tem razão, [g]. Será que você não tá só arranjando uma desculpa?"

    g "E se eu tiver?"

    scene julia_carol_biblioteca3 with Dissolve(1.0)

    o "Então tem que parar. Você não é mais criança. Precisa entender logo que tem uma vida que não é fácil. Se você não se importar, só vai se afundar mais."

    g "A vida não é só isso, [o]. Não tem só um jeito certo da gente ter sucesso. Não é só estudando."

    o "Tá. E qual é o outro jeito então?"

    g "Arranjando um marido rico... talvez..."

    if julia_namoro:

        mc zerado "Se você realmente pretende continuar comigo, esse não é um bom plano."

        g "..."

    o "Que absurdo é esse, [g]? Você tá ouvindo o que você tá dizendo? Depender de um homem pra ter suas coisas? A gente já passou dessa época."

    g "E se eu ainda quiser viver assim?"

    o "Impossível. Isso é simplesmente ridículo, [g]."

    "Eita... a [o] realmente tá ficando meio brava com isso."

    "Parece que ela tá começando a atacar a [g]. Será que eu me intrometo nessa história?"

    menu:
        "[o]... calma...":


            mc envergonhado "Calma, [o]. E se el-"

            o "Que calma? A [g] tá com um parafuso solto, só pode. Olha o que ela tá falando, [mc]."

            mc "Eu sei, mas e se ela quer viver assim mesmo? Não é ela que precisa decidir?"

            scene julia_carol_biblioteca4 with Dissolve(1.0)

            pause

            g "Tá vendo, Carolzinha? O [mc] tá concordando comigo, mesmo não sendo rico."

            mc zerado "Ei... Tô começando a repensar meu comentário."

            o "Vocês só podem estar brincando..."
        "Melhor não falar nada":


            "Vou só ficar na minha."

            o "Parece que são as próprias mulheres que são as maiores machistas da história quando você fala assim, [g]."

            o "A gente não pode ficar achando que é tarefa do homem conseguir emprego e você só precisa ser bonita e 'boa mulher'."

            g "Sei lá... não vejo problemas nisso."

            o "Que absurdo!"

    o "[g]... você é muito infantil se você acha que as coisas são fáceis assim."

    scene julia_carol_biblioteca2 with Dissolve(1.0)

    o "Não sei o que seria de você sem mim..."

    g "Provavelmente já taria curtindo a mansão de algum ricão."

    if julia_namoro:

        mc zerado "..."

        o "Você sabe que seu namorado tá aqui, né?"

        g "Ele sabe que é tudo brincadeirinha."

        mc "..."

    mc zerado "Que absurdo..."

    g "Aliás... falando nisso..."

    scene julia_carol_biblioteca4 with Dissolve(1.0)

    g "Acho que eu vou pra casa de passeio do [caio] hoje. Quer ir?"

    o "Quê?! Como assim?!"

    mc surpreso "Na casa daquele idiota?!"

    g "Calma, gente... não é nada de mais... vai todo mundo."

    mc zerado "Como você fala algo totalmente nada a ver assim de uma hora pra outra?"

    g "Claro que você vai comigo, né, [mc]? Você não vai me deixar sozinha com eles..."

    "Essa mina tem problema. Só pode."

    o "[g]... eu nem sei o que falar pra você sobre isso. É tão fora da realidade... fico até cansada. A gente não ia estudar?"

    g "Eu sei... mas ele me chamou. A [mari] e o [teo] também vão. Daí pensei que seria uma boa... tá um dia bonito hoje."

    o "Que dia bonito que nada, [g]! Escuta o que você tá falando!"

    g "Ai, [o]... às vezes você parece o [mc]. Ele que tem esse costume de falar gritando às vezes."

    mc zerado "Óbvio... olha o que você faz..."

    "Não acredito que a [g] simplesmente decide um negócio assim do nada. Justo com aquele povo?"

    o "Obviamente você sabe minha opinião. E claro que eu não vou junto. Não suporto essas pessoas."

    scene julia_carol_biblioteca1 with Dissolve(1.0)

    if julia_namoro:

        g "E você, gato?"
    else:


        g "E você, [mc]?"

    g "Não vai perder a chance de me ver de biquini, né?"

    mc desculpa "Meu Deus..."

    "Só de pensar no [caio] já tenho vontade de mandar a [g] tomar no cú, essa que é a verdade."

    "Por outro lado a [mari] sempre foi legal comigo. E o [teo] tirando aquela vez que ele tava abusando da [g] no bilhar nunca fez nada contra mim."

    "Será que se eu não for, a [g] vai perder a vibe ou será que ela só vai sem mim? É meio óbvio a merda que vai dar se eu deixar ela sozinha com eles."

    "A [o] também tá contando comigo. Certeza que eu ganho uns pontos com ela se eu não apoiar a [g] nisso."

    "Mas também... tem outra coisa. Eu posso ir com a [g] e curtir com ela."

    if julia_namoro:

        "A gente tá namorando e eu posso muito bem sair com minha namorada na casa de um amigo dela. Isso é super normal."
    else:


        "A gente é só amigos, mas isso nunca parou a [g] antes. Pode rolar muita coisa lá."

    "E agora?"

    menu:
        "Eu vou com você, claro.":


            $ julia_e6 = "passeio"

            "Não vou perder essa chance de sair com a [g]. Ver ela de biquini então? Foda-se [caio] e companhia. Eu dou um jeito neles lá."

            mc charmoso "Pode contar comigo, claro."

            if julia_namoro:

                mc "Não vou deixar minha mina sozinha no covil do lobo. Eu sei cuidar do que é meu."

                g "Falou tudo!"
            else:


                mc envergonhado "Pelo menos um amigo com juízo precisa ir com você..."

                g "Sei, você só quer ver minha bunda."

                mc "..."

            scene julia_carol_biblioteca1 with Dissolve(1.0)

            o "Mas, [g]..."

            g "Não esquente, [o]. A gente estuda aí um dia desses."

            o "..."

            g "Eu vou pra casa e daí te ligo pra marcar tudo certinho, tá, [mc]?"

            mc "Beleza. Vou pra casa e te espero."

            g "Legal! Tchau, lindos!"

            scene biblioteca 2andar with Dissolve(1.0)

            mc envergonhado "Caraca... ela saiu correndo..."

            scene carol_biblioteca_incomodada_close with Dissolve(1.0)

            o "E você também, hein?"

            mc desculpa "Foi mal, mas ela não ia desistir só porque a gente não ia com ela. Você conhece a [g]."

            mc envergonhado "Se eu não fosse com ela, ela ia ficar sozinha com aquela galera. Isso ia ser terrível."

            o "Talvez você tenha razão..."

            o "Pelo menos então fica de olho nela. Não deixa ela chegar perto do [caio]. Só se for pra dar uma bolacha nele."

            mc "Haha... pode deixar."

            scene carol_biblioteca_incomodada with Dissolve(1.0)

            o "E toma cuidado também. Se você provocar ele demais, vai saber o que ele pode fazer com você."

            o "O [caio] é um bully de marca maior na faculdade e dá pra ver que ele tem problema de aceitar qualquer pessoa que vai contra ele."

            mc charmoso "Eu já lidei com muita complicação nessa cidade. Pode deixar."

            o "De qualquer jeito, fique de olho, tá? Toma cuidado. Você vai estar na casa dele. Longe de tudo e de todos. Vai saber..."

            mc normal "Ok, vou ficar esperto. Valeu, [o]. Até outro dia."

            o "Até, [mc]."
        "Melhor nenhum de nós irmos nesse passeio.":


            $ julia_e6 = "biblioteca"

            mc desculpa "Não quero ferrar seus planos, mas eu acho melhor nenhum de nós irmos nesse passeio aí."

            scene julia_carol_biblioteca5 with Dissolve(1.0)

            g "Como assim, [mc]?!"

            mc charmoso "Você que decidiu vir estudar aqui hoje não foi?"

            g "Que que tem?"

            mc "Se você programou isso é porque você tava afim de fazer alguma coisa diferente. Você até chamou a [o] pra dar uma força, né?"

            g "..."

            mc "Você não pode perder a força agora."

            if j5_good:

                mc "Eu lembro aquele dia no cinema que você disse que queria saber mais sobre você. Lembra disso?"

                mc "Eu vi no jeito que você falou aquela vez que você tava mudando um pouco seu jeito de ver as coisas."

            mc normal "Eu sei que você começou a ter um pouco mais de esperança no que pode acontecer com você."

            g "..."

            mc envergonhado "Eu sei que às vezes a gente sente um medo e é difícil. A gente quer deixar tudo e voltar ao que a gente tá acostumado."

            mc charmoso "Mas eu sei que você insistir um pouco, talvez você acabe encontrando um novo tipo de prazer que você nem sabia que existia."

            g "Bah... você só quer falar bonito."

            g "Tá bom... você me convenceu, tontão... não vou nem responder o [caio]."

            g "Mas acho bom eu aprender alguma coisa com tudo isso e que me ajude de algum jeito um dia!!!"

            o "Vai sim, Ju. Confia na gente."

            g "Tá. Eu vou lá então ler."

            o "Isso. Logo estou lá."

            if julia_namoro:

                g "Queria te dar um beijo, gato, mas você ouviu a tontona aqui. Então fica pra próxima."

                mc envergonhado "Tudo bem, eu espero."

                g "Você é um fofo. Tô aqui."
            else:


                g "Tchau, [mc]. Não vou agradecer porque ainda não sei se me convencer a estudar foi uma boa."

                mc charmoso "Haha... de boa."

                g "Tô por aqui."

                mc "Tá."

            scene carol_biblioteca_sorrindo with Dissolve(1.0)

            pause

            o "Ufa... nem acredito que a gente conseguiu convencer ela. Obrigada pela ajuda."

            mc normal "Não foi nada. Eu também acho que a [g] podia acalmar um pouco e focar em outras coisas."

            o "É bom contar com um aliado nessa tarefa de tutora da [g]."

            mc envergonhado "Haha... Dá pra ver o quanto você se preocupa com ela."

            mc desculpa "Eu acho que a [g] sempre foi meio deixada de lado, sabe. Antes da gente, por tudo o que aconteceu na vida dela..."

            o "Concordo. Aliás, acho que você falou uma coisa bem certa."

            scene carol_biblioteca_incomodada with Dissolve(1.0)

            o "A [g] sempre me pareceu uma pessoa deixada de lado. Esse jeito dela, eu tenho quase certeza que é pra chamar a atenção."

            o "Quando ninguém olha pra você, vem essa vontade de gritar, de aparecer... justamente pra ser vista."

            mc desculpa "E como você acha que essa turminha dela, com o [caio], entra nisso?"

            scene carol_biblioteca_incomodada_close with Dissolve(1.0)

            o "Não sou psicóloga e nem sou a pessoa que conhece ela a mais tempo, mas eu acho que ela acabou se apegando a quem apareceu."

            o "Eu sei que ela conhece o [caio] desde antes da faculdade. Eu acho que eles se conheceram em uma época muito difícil pra ela."

            o "O [caio] acabou dando atenção pra ela. Eu acho que foi alguma coisa assim."

            mc serio "Entendi... talvez seja isso mesmo."

            o "Eu também não vou com a cara desse [caio]. Ele é espertalhão demais pra mim. Sempre rindo, cara de debochado."

            mc "Ele é meio babaca mesmo."

            scene carol_biblioteca_sorrindo with Dissolve(1.0)

            o "Mas eu fico feliz de ver que você tá do lado da [g] agora também. Hoje você me mostrou que tem a cabeça no lugar."

            mc envergonhado "Que bom..."

            "A [o] é muito fofa também... seria legal conversar mais com ela. Na amizade só... claro... talvez..."

            if julia_namoro:

                "O que eu tô pensando?! Eu tô namorando a [g], a amiga dela. A [o] nunca aceitaria isso..."
            else:


                "Eu não tenho nada com a [g]. Nada me impede que eu e a [o] tenha um rolinho nesse sentido."

                "Pelo menos olhando pelo lado da [g]..."

            "Será que eu chego nela ou seria atirado demais?"

            "Se eu falar a coisa certa... acho que até dá pra rolar algo quente com ela... ela é bem influenciável..."

            menu:
                "Dá pra ver que você é uma garota especial.":


                    $ j6_carol_beijinho = True

                    mc charmoso "Quanto mais eu vejo você se preocupando com a [g], mais dá pra ver como você é uma garota especial."

                    scene carol_biblioteca_vergonha with Dissolve(1.0)

                    o "Ah... não é nada... eu só gosto dela... só isso."

                    mc "Você ficou com vergonha, hein..."

                    o "Para de falar sobre isso... só piora minha situação."

                    mc "É que você ficou fofa assim."

                    o "[mc]!"

                    mc "Que foi? É verdade..."

                    o "Parece que você tá flertando comigo..."

                    mc "E se for? Algum problema?"

                    if julia_namoro:

                        o "Mas você tá namorando a [g]... isso não é certo."

                        mc "Você é uma garota bem diferente da [g]. Às vezes a gente acaba mudando de ideia..."
                    else:


                        o "Não sei... a gente quase não se conhece."

                        mc "Não vejo nenhum problema. Eu sou um cara tranquilo. A gente pode sair e conversar um dia desses. O que você acha?"

                    o "!"

                    o "N-não quero falar sobre isso agora..."

                    mc "Tudo bem. Não tenho pressa."

                    mc "Só queria te agradecer por ajudar a [g]."

                    scene carol_biblioteca_beijo with Dissolve(1.0)

                    pause

                    o "[mc]!"



                    mc "É só um obrigado."

                    o "T-tá!"

                    menu:
                        "Melhor parar aqui":


                            mc "Valeu por ajudar."
                        "Vou forçar ela um pouco":


                            mc "Você gosta de carinho, não gosta?"

                            o "A-ah... que p-pergunta é essa?"

                            mc "Você é uma moça jovem, bonita... você também quer encontrar alguém, né?"

                            o "E-eu não penso nessas coisas!"

                            scene j6_new1 with Dissolve(1.0)

                            mc "Certeza?"

                            o "[mc]!"

                            mc "Xi... se você gritar a [g] vai ouvir a gente."

                            o "A g-gente não devia tá fazendo isso."

                            mc "Eu quero que você saiba que eu tô de olho em você."

                            o "A-ai..."

                            mc "Ou será que você já tem dono? Ou talvez dona?"

                            o "N-não!"

                            mc "Você e a [g] são bem próximas... nunca rolou nada?"

                            o "E-e-e-eu..."

                            mc "Acho que isso responde."

                            o "Ah..."

                            "A [o] é super influenciável... se eu pressionar ela um pouquinho ela vai ceder na hora."

                            "Eu sinto que ela não me odeia... será que eu vou por esse caminho?"

                            "Tipo... se eu ficar pensando muito nunca vai acontecer nada. Ela é devagar demais. Eu tenho que assumir."

                            label j6_premium1:

                                pass

                            "O que eu faço?"

                            menu:
                                "Atacar ela":


                                    if not premium:

                                        call mensagem_premium from _call_mensagem_premium_25

                                        jump j6_premium1

                                    "Bora ver até onde eu consigo chegar."

                                    scene j6_new2 with Dissolve(1.0)

                                    pause

                                    "Aposto que a [g] tira várias casquinhas dela... eu também posso, certo?"

                                    mc "[o]... você é bonita... e muito gostosa. Olha pra isso aqui."

                                    o "[mc]... a-ah..."

                                    mc "Tudo bem... eu quero dar uma olhadinha. Não é nada demais."

                                    o "A gente não pode..."

                                    mc "Rapidinho, [o]. Você não vai deixar?"

                                    o "N-não é isso... e-eu..."

                                    "Eu sabia. Ela não consegue falar não."

                                    mc "Eu posso dar uma olhada, não posso? Bem rápido."

                                    o "Olhadinha? Como assim?"

                                    scene j6_new3 with Dissolve(1.0)

                                    pause

                                    mc "Assim ó."

                                    o "AAH!"

                                    mc "Xii... você quer que ela escute?"

                                    o "O que você tá fazendo, d-doido?!"

                                    mc "Por que você tá sem sutiã?"

                                    o "Q-que isso te importa?!"

                                    mc "Deve ser difícil achar um sutiã pra um peitão desse tamanho."

                                    o "Ah... chega, por favor."

                                    mc "Deve machucar bastante. É por isso?"

                                    o "S-sim... eu me sinto melhor assim."

                                    mc "Eu prefiro assim. Poder olhar pra eles assim desse jeito."

                                    o "N-não... você tá parecendo a [g]!"

                                    "Claro que a [g] se aproveita dela. Eu sabia! E agora? Eu vou também?"

                                    "Se eu quiser, aposto que ela vai continuar aceitando. Mas tá certo isso?"

                                    menu:
                                        "Parar aqui":


                                            mc "Tem razão. Eu não quero forçar você, [o]..."

                                            o "E-então posso me arrumar?"

                                            mc "Claro."

                                            scene black with dissolve

                                            o "Obrigada..."

                                            jump j6_premium_continua
                                        "Continuar pressionando":


                                            mc "Eu sabia que a [g] se aproveitava de você. Deixa eu tirar uma casquinha também."

                                            o "C-casq-"

                                            scene j6_new4 with hpunch

                                            pause

                                            o "Ahn!"

                                            mc "Muito bom, [o]."

                                            o "Não, [mc]! A g-gente não pode!"

                                            mc "Não? Você vai fazer eu parar?"

                                            o "E-eu! Por favor!"

                                            mc "Você quer que ela escute?"

                                            o "Ahn... o que você tá fazendo?"

                                            mc "Eu falei que você é gostosa, Carol. Eu só quero aproveitar você um pouco."

                                            o "N- Hmm!"

                                            mc "Você deve se sentir tão sozinha. Eu vou te dar um carinho, tá?"

                                            o "Nn... nnnhh..."

                                            mc "Me abraça."

                                            o "N-n-"

                                            mc "Vem. Curte o momento."

                                            scene j6_new5 with Dissolve(1.0)

                                            pause

                                            o "[mc]..."

                                            mc "Eu sabia que você ia gostar."

                                            o "Não..."

                                            mc "Fala que você gosta."

                                            o "..."

                                            mc "Fala que você gosta quando eu chupo seu pescoço."

                                            o "Ahn... e-eu... g-"

                                            o "Ahnn!"

                                            mc "Você vai chegar lá só com isso?"

                                            o "N-não... ah... aahnn..."

                                            mc "Você vai fazer eu parar?"

                                            o "N-nã- AHN!"

                                            mc "Não vai? Então eu vou fazer o que eu quiser."

                                            o "Ah..."

                                            "Ela tá quase lá. Mas as coisas tão saindo do controle."

                                            "Acho que é melhor parar aqui."

                                            menu:
                                                "Parar aqui":


                                                    mc "Tá bom por aqui, né?"

                                                    o "A-ah... v-você..."

                                                    mc "Eu que decido? Então vamos parar..."

                                                    o "O-obrigada..."

                                                    scene black with dissolve

                                                    o "Obrigada... obrigada, [mc]..."

                                                    mc "Se arruma."

                                                    o "Ufa..."
                                                "Ir até o fim":


                                                    mc "Eu vou fazer você gozar, [o]."

                                                    o "Nnnnnhgg!"

                                                    mc "Vem aqui."

                                                    scene j6_new6 with vpunch

                                                    pause

                                                    o "Agh!"

                                                    mc "Se você mandar eu parar eu paro."

                                                    o "Nnngaa!"

                                                    mc "Você tá tremendo. Você gosta quando te pegam forte assim?"

                                                    o "Mhmmm!"

                                                    mc "Fala que você gosta!"

                                                    o "E-eu go- mnmmmh!"

                                                    g "Tem alguém aí?"

                                                    mc "A [g]! Fodeu!"

                                                    mc "Se arruma!"

                                                    mc "Eu vou sair daquí, fala pra ela que eu tive que vazar!"

                                                    mc "Mas a gente continua outro dia, entendeu?!"

                                                    o "Ah.."

                                                    mc "Entendeu?!"

                                                    o "S-sim!"

                                                    scene black with vpunch

                                                    mc "Boa sorte com ela. Tchau."

                                                    o "T-tchau."

                                    scene biblioteca geral with Dissolve(1.0)

                                    g "[o]?"

                                    o "O-oi!"

                                    scene julia_carol_biblioteca4 with Dissolve(1.0)

                                    g "O que aconteceu?"

                                    o "N-nada..."

                                    g "E o [mc]?"

                                    o "Ah... e-eu tenho que resolver uma coisa... logo a gente estuda."

                                    g "Que foi? Você tá suando."

                                    o "J-já te... hmm... encontro. É c-coisa da biblioteca, hm?"

                                    g "Tá... você... tá meio sexy agora, sabia?"

                                    o "Ahn... t-tchau!"

                                    g "Que doida..."

                                    scene biblioteca geral with Dissolve(1.0)

                                    "..."

                                    o "Ah..."

                                    o "O que deu no [mc]? Hmmm..."

                                    scene j6_new7 with Dissolve(1.0)

                                    pause

                                    o "Me tratando daquele jeito!"

                                    o "Ele fez o que queria comigo só por que eu não consigo falar 'não' pras pessoas!"

                                    "Agora ele vai achar que eu sou uma puta que adora ser dominada."

                                    "Não acredito!"

                                    "E agora eu fiquei com essa vontade! Nem pra ele terminar!"

                                    "Tudo culpa da desgraça da [g] que apareceu bem na hora que ele tava no meu pescoço!"

                                    "Foi tão bom! Ele me pegando forte daquele jeito! Nnng!"

                                    "Calma, [o]! Se você continuar assim, alguém pode te ver!"

                                    menu:
                                        "Foda-se! Eu preciso!":


                                            "Ahn! Eu preciso me aliviar! Hm!"

                                            "Não acredito que eu tô fazendo isso na biblioteca! E se alguém ver?!"

                                            "Só tá me deixando mais quente! Preciso de mais!"

                                            scene j6_new8 with Dissolve(1.0)

                                            pause

                                            o "Isso! NNG!"

                                            "Ele me tratou igual um lixo! Seu puto!"

                                            "Me deixando molhada desse jeito, cheia de tesão!"

                                            "E agora me deixando sozinha! Você não presta, [mc]!"

                                            "E se eu não conseguir gozar agora?!"

                                            "A [g] vai vir me procurar e me encontrar aqui desse jeito... toda molhada. E aí?!"

                                            "Ela vai me atacar no sofá, arrancar minha roupa e me usar igual um consolo!"

                                            "Ahnng!"

                                            "Isso! Vai fazer o que quiser comigo! E eu não posso falar nada!"

                                            "Ahn! Aahnn!"

                                            "Tenho que deitar!"

                                            scene black with dissolve

                                            scene j6_new9 with Dissolve(1.0)

                                            pause

                                            "Não, [g]! Não me obrigue!"

                                            "A gente não pode fazer igual na faculdade! Não! Não enfia aí!"

                                            o "Nnngh!"

                                            "Claro que eu não gosto! Aí, não! Atrás não!"

                                            o "Ahn! AAHN!"
                                            scene nnew_ani04 with Dissolve(1.0)
                                            "Eu não sou seu brinquedo! Para de fazer o que você quiser comigo!"

                                            o "E-eu tô quase lá, [g]! Não para!"

                                            "E-eu falei isso?! Que perigo!"

                                            "Mas eu preciso... eu tenho que tirar isso de mim!"

                                            "Eu tô ficando louca!"

                                            o "Ah! Aahhg!"

                                            "Mais! Mais que a [g]!"

                                            scene j6_new10 with Dissolve(1.0)

                                            pause

                                            o "Os dois!"

                                            "[g]! [mc]! Vocês dois?! Eu não sou escrava de vocês!"

                                            o "Isso!"

                                            "Não puxem meu cabelo! Dói! Dói e é gostoso!"

                                            "Mete em mim! Em qualquer lugar que vocês quiserem! Os dois!"
                                            scene nnew_ani02 with Dissolve(1.0)
                                            o "AAGH! AAAHNG!"

                                            o "Isso! Façam o que quiserem! Eu sou a puta de vocês! AAGNH!"

                                            "Cala a boca, [o]!"

                                            "Mas eu vou gozar! Tanto tempo! Quase!"

                                            o "Aagh! Eu vou! Aghh!!"

                                            o "FODE!!!"

                                            "Me enforca! Me bate! Façam o que quiserem!"

                                            scene j6_new11 with vpunch

                                            pause

                                            o "NNNNNNNGGGGHAA!!!"

                                            scene j6_new11 with vpunch

                                            "M-minha nossa! É m-muito forte!"

                                            o "Aah... aah..."

                                            "O que eu tô fazendo... ah..."

                                            "E-eu tenho que me trocar..."
                                        "Tenho que me controlar...":


                                            "É p-perigoso demais... e eu... não posso deixar essas pessoas me afetarem assim."

                                            "Eu tenho que me cuidar..."

                                    "Será que eu encontrei outra [g]?"

                                    "[o]... você precisa sair dessa. Chega de relacionamentos tóxicos. Supera isso, garota."

                                    "S-sim... eu não posso entrar nessa."

                                    scene black with dissolve

                                    "Por mais que isso mexa com meu corpo, eu não posso virar cachorrinha dele também..."

                                    "..."

                                    jump j6_premium_continua
                                "Tá bom por enquanto":


                                    "Eu não vou forçar demais. Não ia ser bacana."

                                    scene black with dissolve

                    scene carol_biblioteca_vergonha with Dissolve(1.0)

                    mc charmoso "Obrigado e até outra hora, [o]. Fala pra [g] que eu não quis atrapalhar, e já piquei a mula."

                    o "Tá bom... Até mais..."

                    mc "Até."

                    o "..."
                "Obrigado por ficar de olho na [g].":


                    mc normal "Valeu por sempre ficar de olho na [g]."

                    o "Eu fico porque eu gosto dela. Eu sei que a [g] é uma garota boa de coração, ela só é meio doidinha."

                    o "Se ela tiver pessoas que deem uma força pra ela, eu tenho certeza que ela vai longe."

                    mc "Verdade. A [g] é super carismática e parece que ela tem um feeling muito forte."

                    o "Também acho. A personalidade dela é super forte e ela tem esse sexto sentido pras coisas. Ela consegue ver dentro da gente."

                    o "Ela sabe ver se alguém tá mal ou triste, ou se a pessoa precisa de alguma ajuda. Isso é muito forte nela."

                    if julia_namoro:

                        o "Eu acho que namorar não é o melhor pra ela, mas até fiquei feliz de saber que era você."

                        mc envergonhado "Sério?"

                        o "É. Você parece um cara de boa, e dá pra ver que você também se preocupa com ela."

                        mc charmoso "Valeu."
                    else:


                        o "Dá pra ver que você também é um grande amigo e se preocupa com ela. Isso me deixou bastante feliz."

                        mc normal "Eu tento, né?"

                        o "Como eu falei, seu apoio vai ser muito importante pra ela, sabe? Não esquece disso."

                        mc "Pode deixar."

                    o "Se a gente ficar de olho na [g], tenho certeza que ela vai acabar se desfazendo das más influências."

                    mc envergonhado "Tomara..."

                    o "O que você acha de fazer companhia pra ela agora? Mas você tem que prometer que não vai atrapalhar."

                    mc normal "Vai ser massa. Pode ficar tranquila, que é pra estudar."

                    o "Então combinado. Pode ir com ela lá. Só vou comprar alguma coisa pra beber."

                    mc "Tá. Até depois."

                    o "Até."

                    scene biblioteca 2andar with Dissolve(1.0)

                    "Deixa eu ver se a [g] tá realmente estudando."

                    "..."

                    mc normal "Opa. Oi, [g]."

                    scene julia_biblioteca_sentada with Dissolve(1.0)

                    pause

                    g "Ah. [mc]. Que foi? A [o] mandou você pra me vigiar?"

                    mc normal "Nada disso boba. Só vim ver você."

                    g "Hmmm... muito suspeito."

                    mc "Que livro é esse que você tava lendo."

                    g "Tô lendo um texto sobre 'Biologia Celular, Molecular e Evolução', que é uma matéria agora do segundo semestre."

                    mc "Caraca, que massa. Não faço ideia do que é isso."

                    g "Nem eu... por isso mesmo eu precisava de uma ajuda dela."

                    g "Mas pra falar a verdade, até que lendo hoje eu peguei um pouco da matéria que acho que vai cair na próxima prova."

                    g "Talvez se eu for legal na P2, eu até consiga não bombar."

                    mc charmoso "Isso é muito bom. Parabéns."

                    g "Valeu. Talvez se eu for bem na prova e não precisar fazer essa matéria tudo de novo semestre que vem, vai ter valido à pena."

                    mc "Com certeza. Se você pegar firme agora, você vai dar conta. Certeza."

                    g "É. Tomara..."

                    mc "Por que você não resume pra mim o que você leu?"

                    g "Sério que você vai querer ouvir sobre isso?"

                    if julia_namoro:

                        mc "Ué, eu tenho que ajudar minha mina."

                        g "Se você acha que sendo bonzinho vai conseguir me levar pra cama... você acertou... vai mesmo."

                        mc "Haha... vai, começa logo."
                    else:


                        mc "Não basta ser amigo. Tem que participar."

                        g "Se você quer, então bora."

                    g "A gente tá no começo, então começamos a ver sobre células. O texto de apoio é do Professor Doutor S-"

                    mc concentrando "zzzzz"

                    g "Ou!"

                    mc envergonhado "Haha.. brincadeira. Pode falar..."

                    g "Tontão..."

    label j6_premium_continua:

        pass

    scene biblioteca geral with Dissolve(1.0)

    "Pronto. Consegui. Ver a [g] parece sempre uma aventura. Mesmo na biblioteca..."

    if julia_e6 == "passeio":

        "Tenho que voltar pra ilha e me preparar. A [g] vai me ligar pra gente viajar."

        "Por um lado isso parece muito foda, mas tinha que ser na casa do [caio]? Até a [o] falou pra eu ficar de olho aberto..."

        "E pelo que eu entendi é uma casa no interior, sem nada em volta. Parece até um cenário de filme de terror pensando assim."

        "Foda-se. Eu vou aproveitar a [g]. Isso que me importa. E provavelmente a [mari] vai tá lá também. Ela é uma mina legal."

        "Ai... espero que dê tudo certo."

        scene black with Dissolve(1.0)







        "..."

        scene mapa cidade with Dissolve(1.0)

        jump julia_e6_passeio
    else:




        "Fiquei feliz de conseguir tirar a [g] dessa viagem. Meter ela no meio desse pessoal de novo ia ser ruim pra ela."

        "A [o] concorda com isso também. Quanto mais a gente tirar a [g] dessa turma, mais ela vai ter chance de ter uma vida mais saudável."

        "Sei lá... pensando assim... eu tô parecendo um professor, sei lá, o pai dela. Será que tá certo eu me intrometer tanto na vida dela?"

        if julia_namoro:

            "Eu sou o namorado dela... eu quero o melhor pra ela. Mas mesmo assim..."

        "Será que querer que uma pessoa faça o que a gente acha certo, realmente é ajudar? Mesmo quando parece que nosso caminho é melhor?"

        "Aahh... não posso ficar duvidando de mim agora. Eu já vi que esses caras fazem mal pra [g]. Eu preciso tirar ela desse buraco."

        "Interessante o que a [o] disse também sobre o [caio]. Parece que a [g] já conhecia ele bem de antes."

        "Talvez isso explique essa ligação que ela tem com ele. Uma pessoa que tava super machucada encontrou segurança no primeiro que apareceu."

        "Mas será que é só isso? A [g] não vê o [caio] só como amigo. Ela até tentou namorar ele. Eu acho que tem mais coisa nisso."

        if julia_namoro:

            "Se eu realmente quero continuar com ela, eu preciso descobrir tudo isso. Faz parte."

        "Não vejo a hora de ver ela de novo."

        jump julia_e6_final

    label julia_e6_passeio:

        $ julia_e6 = "j6_continua"

        "Um passeio com a [g]... o foda é aquele pessoal. Será que isso vai dar bom?"

        "Não tinha como eu deixar ela sozinha. E certeza que ela ia de qualquer jeito. A não ser que eu e a [o] colocasse um segurança em cima dela."

        "Melhor eu ir, pelo menos eu vou tá lá."

        mc zerado "'Melhor eu ir, pelo menos vou tá lá'. Agora filosofei."

        "{i}Trrr... trrr...{/i}"

        "Opa. Deve ser a [g]."

        mc normal "Oi."

        g "Oi. Já tá tudo certo pra gente ir."

        mc envergonhado "Então você vai mesmo? Desistiu do estudo..."

        g "Isso a gente pode fazer todo dia. Agora passar o dia todo de biquini tomando sol e bebendo, daí, né?"

        mc "Pior é que eu acho que você tem razão nisso."

        g "Então para de enrolar e vem logo."

        if julia_namoro:

            g "Eu prometo que vai rolar uma recompensa pro meu namorado gato."
        else:


            g "Eu prometo que vai rolar uma recomensa pro meu amigo de todas as horas."

        mc envergonhado "Recompensa, é?"

        g "E não vai poder negar."

        if julia_seducao <= 9:

            mc zerado "Você sabe que eu tô de boa dessas suas 'recompensas', né? Desde sempre..."

            g "Você é um chato, só isso."
        else:


            mc safado "Se for o que eu tô pensando, não vou negar, não."

            g "Assim que eu gosto, gato."

        g "Então pega o busão na ilha. Você tá na ilha, né?"

        mc normal "Sim. Eu voltei pra cá."

        g "Beleza. Pega o 69 e desce no terceiro ponto. Vai parecer que é o meio do nada, mas tá certo."

        g "Qualquer coisa, o [caio] falou pra você falar pro motorista que você tá indo na casa de passeio, ele vai saber onde é."

        mc zerado "O motorista sabe onde é a casa dele?"

        g "Haha. Você vai entende quando chegar lá. Ele é dono de um lago."

        mc "Agora tu tá zuando..."

        g "Tô nada! Você vai ver."

        menu:
            "Beleza. Vou me arrumar e tô saindo.":


                mc normal "Ok. Vou me arrumar aqui e tô saindo. Uma e hora por aí eu chego lá."

                g "Tá bom. Eu vou tá te esperando, lindo. Beijo!"

                mc "Beijo."
            "E você? Como vai pra lá?":


                mc desconfiado "E você? Como vai pra lá?"

                g "Ah. Eu vou com o pessoal de carro. Eu ia falar pra você vir, mas não cabe todo mundo no carro. Malz."

                if julia_namoro:

                    mc zerado "Sério que tu vai deixar seu namorado ir de busão e sozinho?"

                    g "Para de chororô, [mc]. Você é um rapaz crescido já."

                    mc "Foda-se você. Vou encontrar uma mina gostosa no busão, tu vai ver."

                    g "Ei! Haha... safado."

                g "Mas não vai deixar de ir. Vou ficar te esperando, lindo. Beijão!"

                mc "Beijo..."

                "Como não cabe todo mundo no carro? Se forem os quatro de sempre, ainda sobra uma vaga..."

        "Bom... deixa eu me arrumar."

    scene ape_geral with Dissolve(1.0)

    "Se tem um lago e ela falou de usar biquini, então vou levar um shorts de praia."

    if carro:

        "Não vou sujar meu carro no meio da lama. Vou de busão."

    "Bora."

    scene black with Dissolve(1.0)

    scene cidade onibus with Dissolve(1.0)

    "Será que a [g] realmente só quer farra?"

    if julia_conversou or julia_e2_conversou:

        "Eu acho que não. Eu já conversei sério com ela."

        "Já teve vezes que a [g] apareceu de verdade. Uma pessoa com seus problemas. Eu tenho certeza que ela usa uma máscara."

        "Ela esconde o que realmente tá sentindo nessa fachada de pessoa alegre que só quer curtir."

        "Eu que consegui ver esse outro lado dela preciso confiar mais nela. Eu preciso ajudar ela a não cruzar essa linha."

    "Esse negócio de estudar hoje. Eu tenho certeza que é uma tentativa de dar uma acertada no futuro."

    "Falando assim, eu sinto que conheço ela há tanto tempo já. Lembro da primeira vez que a gente se viu lá no Tadaima. Faz tanto tempo..."

    mc surpreso "Opa! O ônibus! Para!!!"

    scene black with Dissolve(1.0)

    "..."

    scene j6_onibus with Dissolve(1.0)

    "Motorista" "Então você tá indo pra casa do lago?"

    mc "Isso. Como você sabe?"

    "Motorista" "Ninguém pega esse ônibus. Ou é pra ir pra lá ou pra assassinar alguém lá no meio do mato."

    mc "..."

    mc "Mas você já ouviu falar dessa casa mesmo?"

    "Motorista" "Opa. É a casa de um figurão aí."

    mc "Figurão? Você sabe quem é?"

    "Motorista" "Sei não, rapaz. Mas me falaram que é um ricaço aí. Ele trabalha em alguma coisa grande na ilha. Coisa grande mesmo."

    mc "Beleza..."

    "Motorista" "Olha... ouvi falarem que o cara é perigoso inclusive. Tá enrolado em coisa errada."

    mc "Tava querendo saber mais sobre isso..."

    "Motorista" "Você é da polícia?"

    mc "Haha... sou nada. Mas eu trabalho em uma revista e a gente tá sempre querendo saber mais sobre esse tipo."

    "Motorista" "Opa. Eu tenho umas histórias boas aí. Se pá um dia a gente coloca o papo em dia."

    mc "Seria massa."

    "Motorista" "Aliás, tá chegando. É logo ali sua parada."

    mc "Mas não tem nada aqui..."

    "Motorista" "É assim mesmo. É no meio dessa floresta aí. Acho que tem uma trilha, algo assim."

    mc "Valeu..."

    "Só a [g] pra me colocar nuns lances desse."

    scene black with Dissolve(1.0)

    "Acho que é por aqui..."

    scene j6_matagal with Dissolve(1.0)

    pause

    "Que bosta de matagal... acho que eu me perdi. Não tá com cara que tem uma mansão pra esse lado..."

    "A [g] também é foda. Nem pra ela vir comigo. "

    "Acho..."

    "Acho que eu tô ouvindo alguma coisa por ali."

    scene black with Dissolve(1.0)

    mc surpreso "!"

    "Não creio..."

    scene casa_caio geral with Dissolve(1.0)

    pause

    "Olha só pra isso aqui... Sério que aquele moleque é dono de tudo isso?"

    "Claro que deve ser tudo do pai, né? Aquele pirralho não deve nem ganhar dinheiro. Um dia ele ainda vai saber o que é trabalhar pra viver."

    "Ou não..."

    "Agora eu só tenho que."

    mc angustiado "Uargh!"

    scene j6_matagal with vpunch

    pause

    mc "{i}glob glub{/i}"

    mc "Aaahhhh!"

    "Merda..."

    scene j6_mc_agua with Dissolve(1.0)

    "Afe, mano! O lago começou do nada. Eu nem vi!"

    "Por que tá dando tudo errado? Tô começando a achar que eu não devia ter vindo pra cá."

    "Acho que é mais negócio eu ir nadando até lá do que querer dar a volta todo molhado."

    "A galera já vai me zuar... que bosta..."

    "..."

    scene j6_julia_curtindo with Dissolve(1.0)

    pause

    g "Que delícia.... e a [o] queria que eu ficasse estudando... que idiota..."

    "Opa. A [g]! Parece que ela não me viu."

    g "Nem acredito que o [caio] tem uma casa dessas... como o mundo é injusto."

    g "Pelo menos eu sou amiga dele hehe... benefícios indiretos..."

    g "Sinto que hoje vai ser um grande dia!"

    "A mina só curtindo enquanto eu tô aqui me fodendo o dia todo. Isso sim é injusto."

    "Quando ela me chamou aqui eu achei que ela queria companhia e talz... mas parece que ela não tá nem aí."

    "É nessas horas que eu acho que a [g] não tem salvação, mano."

    if julia_namoro:

        "A gente tá namorando, caralho..."
    else:


        "Não foi ela que disse que eu sou um grande amigo?"

    "Isso não importa também. Agora já tô aqui. Deixa eu subir."

    scene black with dissolve

    g "[mc]?! O que você tá fazendo aí?!"

    mc envergonhado "E aí..."

    scene j6_julia_preocupada with Dissolve(1.0)

    g "O que você tá fazendo todo molhado desse jeito, doido?"

    menu:
        "Tu me deixou sozinho pra vir aqui...":


            mc zerado "O que você acha? Tu deixou eu vir aqui sozinho. Eu acabei me perdendo e caí no lago ainda por cima."

            g "D-desculpa... {i}pffff{/i}"

            mc desculpa "Eu sei que você nem liga."

            scene j6_julia_coracao with Dissolve(1.0)

            g "Tá bom, malz. Eu não queria que você se ferrasse vindo aqui. Só achei que não ia dar nenhum problema."

            mc concentrando "Não é culpa sua mesmo. Sei lá..."

            g "Que foi?"

            mc desculpa "Só achei que você ia se importar com o lance de eu vir."

            scene j6_julia_preocupada with Dissolve(1.0)

            g "..."

            mc "..."

            mc "Agora isso não interessa."

            g "[mc]... eu me importo com você."

            mc desconfiado "Não precisa falar isso só porque eu falei. É até pior."

            g "Calma... eu tô falando sério. É que eu sou meio sem noção, mas eu realmente queria que você viesse."

            mc envergonhado "Que você é sem noção todo mundo sabe."

            g "Ei..."
        "Deixa pra lá.":


            mc zerado "Deixa pra lá. Você é zé ruela, só isso."

            g "Você e essas gírias... mas tira a roupa pra você ficar mais de boa."

            mc normal "Beleza. Já vou tirar. E você como tá?"

            g "Tudo legal... cheguei faz uma meia hora. Daí me troquei e já vim pra cá."

            mc "O dia tá bonito."

            g "Falei que ia ser uma boa vir pra cá."

    scene j6_julia_curtindo_close with Dissolve(1.0)

    pause

    g "Eu tô louca pra curtir um dia assim... só de curtir mesmo."

    mc envergonhado "Sei..."

    g "Esses dias eu tô pensando muito na vida. Tá na hora de dar uma parada e só curtir mesmo."

    mc desconfiado "Pensando muito na vida? Desde quando você faz isso?"

    if j5_good or julia_conversou or julia_e2_conversou:

        g "Haha... engraçadinho."

        mc charmoso "Tô falando sério. Não sabia dessa. Pensando no que exatamente?"

        g "Eu esqueço que você gosta de falar dessas coisas..."

        if julia_namoro:

            mc "Não foi isso que conquistou você?"

            g "Acho que você tá é se achando demais."

        mc "Pois é... vai falar ou não."

        g "Tá..."

        scene j6_julia_pensando with Dissolve(1.0)

        g "Acho que foi naquele dia do cinema..."

        if j5_good:

            mc charmoso "Certo... não foi um dia ruim."

            g "Ah, sim... não é isso. Não é que foi ruim."
        else:


            "Aquele dia que ela ficou zoando com os dois lá... me dá raiva só de pensar."

            mc bravo "Que que tem esse dia?"

        g "Depois que a gente saiu do cinema, eu fiquei pensando nuns negócios. Tipo, sobre o que eu quero fazer."

        mc zerado "Entendi tudo..."

        g "Calma! Não tô sabendo como falar."

        mc "Dá pra ver."

        g "Assim... eu achei que depois que eu entrasse na faculdade as coisas meio que iam se encaminhar pra mim."

        g "Só que nada mudou. Quase nada pelo menos. Eu não sinto nada seguindo pra frente. Minha vida não tá caminhando, entende?"

        g "Eu ainda moro com meus pais, eu vou bombar em um monte de matérias..."

        if julia_namoro:

            g "Pelo menos a gente tá com alguma coisa mais séria, né?"

            mc charmoso "Com certeza."

            g "Pelo menos acho que isso caminhou um pouco... mas não é o suficiente. Olha..."

        scene j6_julia_triste with Dissolve(1.0)

        g "Quando a [s] era criança ela já tava treinando. Na minha idade ela já era campeã olímpica. Você acredita nisso?"

        g "E às vezes ela fala dessa menina com nome chinês que eu sempre esqueço que é super novinha e já tá treinando também."

        mc envergonhado "Sei, a [fen]."

        g "Essa aí mesmo. E olha eu. Isso não tá certo. Isso tá me deixando super preocupada. Não quero viver assim pra sempre."

        mc concentrando "[g]... eu entendo... mas acho que você tá exagerando um pouco."

        g "Exagerando? Você fala isso porque não é você."

        mc envergonhado "Acho que nossa história é um pouco mais parecida do que você imagina."

        mc "Quando eu saí da faculdade eu não tinha merda nenhuma. Eu não morava com meus pais, mas eu não queria voltar lá de jeito nenhum."

        mc "E mesmo tentando fugir dos meus pais, foi minha mãe que arranjou meu trabalho. Olha a ironia."

        mc "E agora eu tô aqui... sei lá o que eu faço da minha vida. Eu ganho o suficiente pra viver e só. Tenho que fazer bico pra juntar grana."

        mc charmoso "Eu acho bacana você tá preocupada com seu futuro, mas não é pra tanto assim. Não precisa ficar tão nervosa."

        mc "Contanto que você não faça nada estúpido demais, dê tempo pra você. Você não é a [s], não precisa ganhar uma medalha olímpica."

        scene j6_julia_confiante with Dissolve(1.0)

        g "Você realmente acha isso ou tá falando só pra eu me sentir melhor?"

        mc "Tô falando sério, boba. Só de você tentar estudar hoje já foi um grande avanço."

        mc "Comece devagar. Tente se salvar em algumas matérias, estudar um pouco mais semestre que vem e vai ficar tudo bem."

        g "Sabia que eu acho que você pode até tá certo?"

        mc charmoso "Claro que eu tô certo."

        g "Ufa... nossa... valeu, [mc]. Acho que eu tô um pouco menos nervosa. De verdade."

        mc "Que bom."

        g "Às vezes eu fico toda tonta como você fala as coisas certas pra mim. Não foi a primeira vez."

        "Pra [g] tá falando desse jeito ao invés de zoar... ela devia tá preocupada com isso mesmo."

        mc "Relaxa. Tá tudo certo."

        scene j6_julia_curtindo_close with Dissolve(1.0)
    else:


        g "Haha... engraçadinho."

        mc charmoso "Tô falando sério. Não sabia dessa. Pensando no que exatamente?"

        g "..."

        g "Esquece. Você não vai querer ouvir sobre isso."

        mc desconfiado "?"

        "Acho que a [g] não tem confiança em mim o suficiente. Mas foda-se, eu só quero pegar ela mesmo. Melhor ficar só com a parte boa."

        mc charmoso "De boa. A gente não precisa ficar perdendo tempo com isso."

        g "Falou tudo."

    g "Agora eu quero curtir isso aqui. O vento e o quentinho do sol. Quem sabe pegar mais uma corzinha..."

    mc charmoso "Essa parte é com você, né?"

    g "Opa! Se é pra curtir, pode chamar."

    mc envergonhado "Haha..."

    mari "E aí, dois? Tudo bem?"

    g "[mari]! Você chegou!"

    mc normal "Fala aí, [mari]."

    g "Vem aqui que eu quero falar um negócio."

    scene j6_julia_mari1 with Dissolve(1.0)

    pause

    g "Queria te falar um negócio sobre o [teo]."

    mari "Hmm... alguma coisa que eu não sei?"

    g "É mega confidencial. Tipo-"

    mc normal "..."

    g "Para de ser xereto, [mc]. É um negócio à sós. Vai conhecer a casa e a gente já se fala."

    mari "Coitado dele, [g]... Ele não veio aqui por sua causa?"

    g "É só um negócio, ele não vai morrer."

    mc zerado "..."

    mc "Falous."

    mari "Desculpa, [mc]."

    mc envergonhado "Relaxa. Conversem aí de boa. Vou tirar essa roupa molhada e dar uma olhada lá em cima. Nem conheci a casa ainda."

    mari "Até depois."

    g "Vai logo!"

    "Nem acredito que eu tô aqui com essas duas gatas. A [g] é muito gostosa, mas a [mari] também é super caprichada."

    "Ver essas duas garotas lindas de biquini assim... não deve ser todo cara que tem essa sorte também."

    "Eu tô parecendo um tarado, mas só olhar não tem problema, tem?"

    scene casa_caio geral with Dissolve(1.0)

    "Enfim, deixa eu andar por aqui e deixar elas conversarem."

    "Primeiro deixa eu ficar só de shorts. Vou deixar minhas coisas aqui. Não posso esquecer depois..."

    "Essa casa é realmente gigante. Eu nem entrei ainda e já dá pra ver como ela é incrível. Isso que dá não ter onde colocar o dinheiro."

    "O pior é saber que tudo isso aqui é do-"

    mc serio "Você..."

    scene j6_caio_teo1 with Dissolve(1.0)

    pause

    teo "Fala aí, [mc]. Bom ver você, cara."

    mc serio "E ae, [teo]? Tudo de boa."

    caio "Então você veio mesmo..."

    mc bravo "Vim porque a [g] veio e me chamou."

    caio "Você é cara de pau mesmo, velho. Depois do que rolou no cinema você achou certo vir na minha casa."

    teo "Ei! O que é isso, manos? Para com isso, [caio]."

    if not j4_salvou:

        teo "Você não lembra que ele deixou a [g] pra gente lá no seu apartamento aquele dia? O cara é dos nossos."

        caio "Mas daí ele surtou no cinema. Isso não é coisa de brother."

        teo "Tu surtou mesmo, [mc]."

        "Claro que eu surtei. Os caras tavam fazendo a [g] de um brinquedo sexual na festa e no cinema também."

        "Mas se eu quiser ficar do lado deles, eu vou precisar me desculpar por aquele surto."

        menu:
            "Tô ligado. Eu não devia ter explodido daquele jeito.":


                $ j6_caio_perdoa = True

                mc desculpa "Eu sei. Eu não devia ter ficado pistola daquele jeito. Malz."

                teo "Tá vendo, [caio]? O [mc] é super de boa."

                mc "É que a [g] ainda mexe comigo. Daí vendo vocês com ela lá, eu fiquei puto."

                scene j6_caio_teo_felizes with Dissolve(1.0)

                teo "O coração é assim mesmo, cara. O [caio] entende isso também, não entende?"

                caio "Sei lá, [teo]. Mas talvez realmente o cara não conseguiu segurar."

                teo "Tô falando! Ele é de boa. Vamo parar com essa treta aí e curtir de boassa."

                caio "É. Você tá certo. Não adianta ficar causando demais."
            "Olha o que vocês tão fazendo com a [g] também!":


                mc bravo "Mas fala sério! Olha o que vocês tavam fazendo com a [g] no cinema!"

                mc "Vocês tratam a mina como um animal. Isso não tá certo."

                scene j6_caio_teo_bravos with Dissolve(1.0)

                caio "Tá vendo, [teo]? O cara é um vacilão!"

                teo "Pô, [mc]. A gente só tava brincando. A [g] concordou também. Ninguém obrigou ela a fazer nada."

                mc bravo "Não é porque vocês não obrigaram que tá certo."

                caio "Tá vendo o que esse idiota pensa da gente?"

                teo "Olha, [mc]... eu acho que você criou uma [g] na sua cabeça e você queria que ela fosse desse jeito."

                teo "Só que ela não é. Você não pode culpar a gente por isso. Ela sempre foi assim, sempre curtiu brincar com a gente."

                mc desculpa "Afe, mano... não é assim que vocês deviam tratar as minas tá ligado."

                caio "Você que é otário demais. Mulher gosta dessas coisas, cara. Mulher só parece que gosta de gado. No fundo elas ficam com homem que manda."

                mc bravo "..."

                teo "Calma, [caio]. Não é assim também preto no branco. Tem mulheres e mulheres. Isso que o [mc] tem que ver."

                caio "Você também fica de conversinha, [teo]."

                teo "Não, cara. É que eu entendo o que o [mc] tá falando. Só que não concordo que a gente é o lado mau da história. Isso que ele tem que ver."

                "Será que ele tem razão? Eles e a [g] são farinha do mesmo saco? Eu que tô querendo ver ela de outro jeito?"

                teo "Eu acho que se ele colocar na cabeça que a gente não é mau, ele vai ser um dos manos também."

                caio "Tá. Mas esse idiota é gadão. Ele não vai entender isso nunca."

                teo "E aí, [mc]? Não dá pra você pelo menos dar uma chance pra gente ao invés de só sair julgando?"

                "E agora? Será que eu vou ficar do lado desses caras?"

                "Tipo... eles não são boas companhias pra [g]. Dá pra ver isso. Mas será que realmente é culpa deles ou dela?"

                "Porque se eles só tiverem curtindo com ela, quem tá fodendo tudo sou eu e não eles."

                mc "Então..."

                menu:
                    "Eu vou ficar do lado de vocês dois.":


                        $ j6_caio_perdoa = True

                        mc concentrando "Acho que você tá certo, [teo]. Não dá pra culpar vocês por tudo também."

                        mc envergonhado "Não é novidade que a [g] tem esse jeitão dela. Se ela tá entrando na brincadeira, não é como se vocês fossem os grandes culpados."

                        scene j6_caio_teo_felizes with Dissolve(1.0)

                        teo "Tá vendo! Tô falando que o [mc] é o cara!"

                        caio "Agora você me pegou. Não achei que ele ia aceitar assim."

                        mc normal "Eu tento não ser cabeça dura. Eu tô pensando bem sobre isso."

                        teo "Isso aí."
                    "Não posso aceitar isso. Vocês também têm culpa.":


                        $ j6_caio_perdoa = False

                        mc bravo "Eu entendo, [teo], mas eu não consigo concordar com o que vocês fazem."

                        mc desculpa "Não sei se eu tô 100%% certo nisso, mas não dá. Mesmo com a [g] sendo desse jeito e aceitando as coisas, não tá certo."

                        mc "Eu acho que cada um tem sua parte na responsabilidade. Ela tem a dela também, mas por que eu nunca fiz algo assim com ela?"

                        mc "A [g] já deu muito em cima de mim também. E a gente até já se pegou, mas nunca desse jeito."

                        mc "Eu nunca falei dela do jeito que vocês fazem. Com essa falta de respeito aí."

                        teo "Touché. Nem discordo de você, [mc]..."

                        caio "Tu é maluco, [teo]? O cara tá falando mó besteira aí."

                        caio "Fodam-se vocês. Falou."

                        scene casa_caio geral with Dissolve(1.0)

                        teo "Vish... pistolou."

                        mc desculpa "Pois é."
    else:


        teo "Eu sei que o [mc] não aceitou a brincadeira lá na festa, mas não é por isso que ele é um cuzão também."

        caio "Eu acho que ele é, sim. Ou ele tá com a gente ou tá contra a gente. É simples assim."

        mc serio "Não faço questão nenhuma de tá do seu lado, [caio]. O [teo] é de boa, mas você se acha muito, cara."

        scene j6_caio_teo_bravos with Dissolve(1.0)

        caio "Sério que você vai vir na minha casa e vai falar assim comigo, mano?"

        teo "Pega leve, [mc]. Não precisa disso tudo, não..."

        mc desculpa "Não quero ficar causando... só quero ficar de boa com a [g]. Eu tô aqui por causa dela."

        mc "Se você não arrumar encrenca comigo eu também não vou causar."

        caio "Mano, você é muito chato. Ninguém quer saber de você, não. Eu vou dar o fora desse mané."

        scene casa_caio geral with Dissolve(1.0)

        teo "Vish... pistolou."

        mc desculpa "Pois é."

    if j6_caio_perdoa:

        caio "Eu também não quero ficar brigando por causa dessas minas. Elas não valem toda essa dor de cabeça."

        teo "Haha..."

        caio "Agora a gente falou tanto delas que eu vou dar uma olhada nelas lá. Vê se dão um tempo pra mim."

        teo "Pode deixar. Vai lá."

        scene casa_caio geral with Dissolve(1.0)

        teo "Que bom que vocês se entenderam."

        mc concentrando "Por enquanto pelo menos..."
    else:


        teo "Vai ser duro vocês se entenderem... mas mesmo sendo amigo dele, eu sei que tu não é um mané, [mc]."

        mc "Você também é um cara de boa."

    scene j6_mc_teo with Dissolve(1.0)

    mc normal "E valeu por não se juntar com ele contra mim."

    teo "Você nunca fez nada pra mim, mano. Eu não sou possessivo com a [g] igual o [caio]. Eu prefiro ficar de boa."

    teo "Eu gosto de brincar com elas também, mas nem tanto assim. E eu acho que eu fui com sua cara haha..."

    menu:
        "Valeu. Qual é a do [caio] com a [g]?":


            mc "Haha... massa. Mas o que você sabe do lance do [caio] e da [g]?"

            jump j6_teo_julia
        "Opa. Eu também fui com a sua cara.":


            mc "Pra falar a verdade, acho que eu fui com sua cara também."

            teo "Eu gostei bastante da sua vibe. Você parece ser um cara de boa e cabeça. Eu gosto disso."

            "Gostou da minha vibe? Será que ele tá tentando flertar?"

            menu:
                "Elogiar ele também":


                    $ j6_teo = True

                    mc "Prestou atenção em mim mesmo, hein?"

                    teo "Ah! Isso é fácil de ver..."

                    mc "Tô zuando. Eu também vi que você não é cabecinha igual o [caio] só do jeito que você falou com ele hoje."

                    mc "Eu acho foda caras assim que conseguem se manter de boa. Passa um lance bom."

                    teo "De boa é comigo mesmo. Eu gosto de curtir, mas não no ritmo do [caio] e da [g]. Eles têm energia demais."

                    teo "Eu sou mais de boa. Eu curto, mas um lance mais de boa, uma conversa, uma música com os amigos."

                    teo "Assim, tipo, eu sou o cara que vai no barzinho e não na balada, entende?"

                    mc "Com certeza. Até porque pensando assim eu sou desse jeito também. Balada não é muito minha praia."

                    teo "Olha aí. E se a gente fosse em um bar aí um dia? Só a galera de boa."

                    mc "Beber um pouco, conversar. Eu topo com certeza."

                    if nathan_e4_beijo:

                        "Sério que eu tô beijando o [n] e tô marcando de ir no bar sozinho com esse cara?"

                        "Mas foi tão rápido..."

                    teo "Então fechou. Depois eu pego seu telefone com a [g] e te ligo. Fechou?"

                    mc "Fechado. Vou ficar esperando."

                    teo "Demorou, [mc]. E agora?"

                    mc "Vou descer lá ver se a [g] parou de falar com a [mari]."

                    teo "Beleza. Eu vou dar uma andada por aí."

                    mc "Até, cara."

                    teo "Abração."
                "Cortar a conversa":


                    mc "Haha... massa. Mas o que você sabe do lance do [caio] e da [g]?"

                    label j6_teo_julia:

                        teo "Esses dois? Sei lá."

                    mc "Você falou que ele tem uma fixação por ela e talz..."

                    teo "Ah. Então, o [caio] ele tem alguma coisa pela [g]. Posso até tá meio doido, mas eu acho que é um tipo de amor, sei lá."

                    mc "Amor? Mas-"

                    teo "Eu sei que é estranho pensar assim, mas ele fala dela várias vezes. Às vezes ele tá puto com ela, às vezes ele tá de boa."

                    teo "Mas eu nunca vi ele falando assim de outra garota."

                    mc "Nem da [mari]?"

                    teo "Quem dera... ele nem liga pra ela direito. O negócio dele é a [g]. E é isso que eu não entendo."

                    mc "Por que?"

                    teo "Porque assim, o [caio] é mó bem de vida. E ele não é feio, ele fala bem. Ele pode ser meio infantil, mas eu já vi várias minas dando em cima dele."

                    teo "Ele podia ficar com muita gente aí. E vou falar pra você... muito melhores que a [g]."

                    if julia_namoro:

                        "Vou matar esse cara se ele falar da minha namorada assim de novo."

                    mc "Sei..."

                    teo "Mas ele fica em cima dela. Só que ao mesmo tempo ele não fica só com ela. Ela tentou namorar ele e ele chifrou ela pra caramba."

                    teo "É uma relação complicada a deles parece..."

                    mc "Era sobre isso que eu queria saber..."

                    teo "O que eu posso falar é que eles se conhecem desde antes da faculdade. Quando eu conheci o [caio] eles já eram amigos."

                    mc "Entendi. Valeu, [teo]."

                    teo "Relaxa. E se você tá de olho na [g] também, fica esperto porque o [caio] não é de desistir."

                    teo "Eu já vi esse cara puto, mas se colocar a obsessão dele no meio, não consigo nem falar como ele vai ficar."

                    mc "Beleza haha... vou lembrar disso."

                    teo "Falou, rapá."

                    mc "A gente se vê aí."

    scene casa_caio geral with Dissolve(1.0)

    "Caraca, fiquei um tempão falando com eles. Daqui a pouco a gente vai embora e nem curti com a [g] ainda."

    "..."

    mc zerado "Não creio..."

    scene j6_julia_mari2 with Dissolve(1.0)

    pause

    mc zerado "Ainda tão conversando?"

    g "Onde você tava? Sumiu."

    mari "[g]... você que falou pra ele dar espaço pra gente."

    g "É... mas ele ficou um tempão."

    g "Aliás, o [caio] falou pra eu encontrar ele lá dentro, né?"

    mari "Acho que sim. Antes dele falar, você disse pra ele sair de perto."

    g "Porque esses caras querem ficar ouvindo nossa conversa?"

    mari "Acho que você é irresistível demais."

    g "Aí você falou uma verdade, [mari]."

    g "Eu vou ver o que ele quer e já volto. Só um segundinho, [mc]."

    mc zerado "Mas..."

    g "Tchau!"

    scene j6_mc_mari with Dissolve(1.0)

    pause

    mari "Parece que só sobrou eu..."

    menu:
        "Vai entender essa [g]...":


            mc "Tem como entender essa [g]?"

            mari "Doidinha... mas o que aconteceu? Você parece meio pra baixo."

            mc "Sei lá. Ela que me chamou pra vir aqui e até agora nem consegui falar com ela."

            mari "Hmmm... você acha que ela tá te evitando?"

            mc "Não sei se chega nisso, mas que ela não tá sendo atenciosa, com certeza."

            mc "Tipo, nada muito grande, mas se você convida alguém pra um lugar novo pra ela, no mínimo você tem que fazer uma sala, né?"

            mari "Concordo. E nem dá pra falar que a [g] é desatenta, porque ela tem um feeling bem grande."

            mc "Pior que é. Mas deixa pra lá."

            mc "E você? Como que tá?"
        "Sobra? Nunca.":


            mc "Você? Sobra? De jeito nenhum. Acho que eu prefiro conversar com você do que com ela."

            mari "Será mesmo? Ou você só tá querendo pagar de cavalheiro?"

            mc "De um jeito ou de outro eu tô tentando te impressionar. Não ganho uns pontos?"

            mari "Não."

            mc "Não? Que frieza..."

            mari "Você já tem pontos demais comigo. Não tem como acumular mais."

            mc "Opa..."

            mari "Muito direta? Assustado?"

            mc "Talvez um pouco..."

            mari "Bobo... mas toma cuidado."

            mc "Tô vendo. Mas fala aí... como você tá?"

    mari "Na mesma de sempre."

    scene j6_mari_mc with Dissolve(1.0)

    pause

    mc "E qual é a de sempre?"

    mari "Procurando um rapaz decente pra ficar."

    mc "Haha... e o [caio]?"

    mari "O [caio] é muita coisa, menos decente."

    mc "Hahaha... E o [teo]?"

    mari "O [teo] é legal, mas ele não liga pra mim. E eu também não curto muito ele."

    mc "E esses são seus únicos amigos?"

    scene j6_mari_incomodada with Dissolve(1.0)

    pause

    mari "..."

    mc desculpa "Desculpa. Falei alguma merda?"

    mari "Não. É que eu percebi que eu só tenho esses amigos mesmo..."

    mc envergonhado "Sei. Mas isso não é ruim. A gente normalmente tem poucos amigos de verdade mesmo."

    mari "Não é a quantidade que eu tô falando. É o tipo de amigo."

    mc desconfiado "Como assim?"

    mari "Seria legal se eu tivesse um amigo ou amiga que eu realmente confiasse, sabe? Eu sinto que eu não posso confiar nesses aqui."

    mc desculpa "..."

    mari "Acho que eu fiquei um pouco desesperada, só isso."

    mc envergonhado "Olha... vocês lá na festa e no cinema, dá pra ver que vocês são bem próximos."

    mari "Sim. A gente faz sempre as coisas junto. Mas é diferente."

    mari "Eu tô falando de pessoas que você pode contar tudo, que você pode ser você de verdade e não se preocupar se eles vão gostar."

    mari "O [caio] é engraçado, confiante, mas eu sinto que se as coisas não são do jeito dele, ele já fica puto."

    mari "O [teo] é o contrário. Eu sinto que ele não tá nem aí pra mim. Eu posso falar o que quiser ele não tá nem aí."

    mari "E a [g] tá tão ferrada na cabeça dela, que nem sei se dá pra falar alguma coisa de verdade. A gente só fala de bobeira."

    mc desculpa "Não é fácil encontrar uma pessoa assim, né? Uma pessoa que a gente realmente confia e que se preocupa com a gente."

    mari "É. É isso que eu tô falando."

    mc envergonhado "Não sei se vale de alguma coisa, mas se algum dia você quiser falar alguma coisa, eu posso ouvir, tá?"

    mc charmoso "A gente nem se conhece direito, eu sei que não dá pra você confiar em mim... mas se precisar, eu vou ouvir."

    mari "Hmm..."

    scene j6_mari_mc_abracados with Dissolve(1.0)

    pause

    mc "M-mari?! Q-que foi?"

    mari "Não sei... só me deu vontade de abraçar você..."

    mc "Será que é uma boa ideia? Alguém pode tá vendo."

    mari "Você fala isso, mas eu tô sentindo sua mão na minha bunda, tá?"

    mc "Ops... acho que foi meio automático."

    mari "Essa é sua desculpa? Foi 'automático'? Horrível..."

    mc "Foi mesmo hehe..."

    mari "Olha... e se a gente esquecesse eles?"

    mc "Esquecer como?"

    mari "E se você me beijasse agora e a gente passasse a tarde juntos? A gente podia ir até o outro lado do lago."

    mc "Só deixar eles aqui?"

    mari "O que você acha?"

    "Eita... e agora?"

    if julia_namoro:

        mc "Olha... eu tô namorando a [g]. Você sabe, né?"

        mari "Sei... mas eu não ligo. E o coração muda, sabia? E se você acabar gostando mais de mim?"

    "Maluco... não posso dizer que eu tô 100%% surpreso. A [mari] sempre deu em cima de mim."

    "Mas eu vim aqui pela [g]... se bem que ela nem ligou pra mim o dia todo."

    "Eu podia só ficar com a [mari]. Ia ser uma boa vingança pelo que ela fez."

    "Não... eu sou realmente esse tipo de cara? Que faz isso?"

    if julia_namoro or priscila_namoro or sayuri_namoro or maria_namoro:

        "Eu já tô namorando... eu vou só ficar com ela também?"

        "Desde quando eu virei esse cusão traidor?"

    "Eu preciso pensar com a cabeça de cima."

    mari "-Eii... eu tô aqui. E aí?"

    mc "Desculpa. Então..."

    menu:
        "Eu aceito. Bora.":


            $ j6_final_mari = True

            mc "Quer saber?"

            mari "Que foi?"

            scene j6_mari_mc_beijo with Dissolve(1.0)

            pause

            mari "!"

            mc "Foda-se esse pessoal. Vou te beijar muito hoje."

            mari "Ai que delícia, [mc]... você tá me apertando muito gostoso."

            mc "Você é tão cheirosa, [mari]. E seu corpo é uma delícia."

            mari "Hoje você vai pegar em tudo mesmo?"

            mc "Tudo tudo. Quero experimentar tudo também..."

            mari "Pode fazer o que você quiser comigo."

            mc "Eu vou. Agora bora sair daqui. Vamo encontrar um lugar mais de boa."



            mari "Nanana... eu quero que você me pegue aqui."

            mc "Aqui? Mas..."

            mari "Que foi? Não quer que saibam que a gente tá ficando?"

            mc "No meio da festa do Caio... no cinema... você quer mesmo que peguem a gente, né?"

            mari "Não sei do que você tá falando. Se quiser... vai ter que ser aqui."

            if julia_namoro:

                "Eu e a [g] tamo namorando... ficar com a Mari aqui vai dar merda... certeza."
            else:


                "Eu e a [g] não tamo namorando... não deve dar nada se pegarem a gente."

            "O que eu faço?"

            menu:
                "Eu fico contigo em qualquer lugar.":


                    mc "Foda-se os outros. Eu fico contigo no lugar que você quiser."

                    mari "Isso. Eu vou te recompensar pra valer."

                    mari "Pode fazer o que você quiser."

                    scene j6_new12 with Dissolve(1.0)

                    pause

                    mc "Então eu vou aproveitar seu corpo inteiro."

                    mari "Ah... quanta animação..."

                    mari "Qualquer mulher se sente bem quando um homem mostra vontade de ficar com ela."

                    mc "Então pode se sentir muito bem, porque eu tô com muita vontade de te pegar."

                    mari "Eu tô vendo. A gente vai se divertir bastante hoje."

                    scene j6_new13 with Dissolve(1.0)

                    pause

                    mari "Ai... você vai tirar toda minha roupa aqui mesmo?"

                    mc "Você que quis ficar aqui."

                    mari "Ahnn... Não achei que você ia aceitar assim."

                    mc "Não se preocupa que eu vou arrancar a roupa também."

                    mari "Louco..."

                    mc "Seu corpo é incrível, [mari]. Tudo em você é muito bom."

                    mari "E você não liga dos outros olhando?"

                    mc "Hmm..."

                    mari "Não é como se eles nunca tivessem visto, mas..."

                    mc "Você prefere ir pra lá? Eu só quero poder aproveitar você."

                    mari "Prefiro... passar a tarde a noite inteira com você."

                    mc "Então bora."

                    scene black with Dissolve(1.0)

                    scene casa_caio geral with Dissolve(1.0)

                    "Não adianta ficar dando bola pra quem não liga pra gente."

                    "A [mari] é incrível e tá na minha. Se a [g] quer dar pra esses idiotas, eu não sou pai dela nem nada."

                    "Ficar correndo atrás é coisa de gado. Eu vou ficar com a [mari] que se preocupou comigo de verdade."

                    if julia_namoro:

                        "O foda é nosso namoro, né? Acho que assim que as relações começam a dar merda..."

                        "Espero que eu não me arrependa disso mais tarde."

                    label j6_premium2:

                        pass

                    menu:
                        "Ir devagar e aproveitar tudo":


                            if not premium:

                                call mensagem_premium from _call_mensagem_premium_26

                                jump j6_premium2

                            mari "Vem, [mc]!"

                            mc "Tô indo!"

                            mari "Aqui nessa árvore acho que ninguém vai ver."

                            mc "E agora?"

                            mari "Agora encosta e deixa comigo."

                            scene black with dissolve

                            scene j6_new14 with Dissolve(1.0)

                            pause

                            mc "!"

                            mc "M-mari... ah..."

                            mari "Eu vou mostrar pra você porque o Caio e o Téo gostam tanto de mim."

                            mari "Eu sou a melhor com um pau na mão que você vai conhecer na sua vida."

                            mc "S-sua mão é incrível..."

                            mari "Tenta segurar o máximo que você puder..."

                            scene j6_new15 with Dissolve(1.0)

                            pause

                            mc "N-não sei quanto tempo eu aguento assim."

                            mari "Aguenta quanto conseguir."

                            mari "Seu pau tá igual uma pedra."

                            mari "Ele é bem gostoso de pegar, sabia?"

                            mc "S-se você continuar falando assim, daí que eu não aguento!"

                            mari "Hihi..."

                            mari "Melhor eu ir logo pro principal, se não você vai chegar lá na metade do show."

                            mc "P-principal?"

                            scene j6_new16 with vpunch

                            pause

                            mc "AANNGH!"

                            mc "M-mari! Sua mão é uma delícia, mas sua boca é perfeita!"

                            mari "Obrrigadxa! SHLUP!"

                            mc "E-eu!"

                            scene j6_new16 with vpunch

                            mari "NNGH!"

                            mc "AAAHHG!"

                            mc "Gozando na sua boca!"

                            mari "Soltxa!"

                            scene j6_new16 with vpunch

                            mari "Hmmm..."

                            mc "Ah... ahh..."

                            mari "Sua porra é deliciosa..."

                            mc "Haha... o-obrigado..."

                            mari "Você quer sentir ela também?"

                            mc "Q-quê?"

                            mari "Eu fico muito excitada de beijar depois de uma chupada."

                            menu:
                                "Melhor a gente parar por aqui":


                                    mc "M-melhor a gente parar... eu não aguento mais, Mari."

                                    mari "Que pena... achei que a gente só tivesse começando."

                                    mc "Você foi incrível, mas tá bom... ufa..."

                                    mari "Então tá..."
                                "Vem aqui então":


                                    mc "Vem aqui."

                                    mari "Uau!"

                                    scene j6_new17 with Dissolve(1.0)

                                    pause

                                    mc "Hmm!"

                                    mari "Você ainda tá animado, hm?!"

                                    mc "Eu só preciso de um tempinho pra me recuperar."

                                    mari "Você não quer perder o prato principal?"

                                    mc "Eu não saio daquí sme comer você, Mari."

                                    mari "Era o que eu queria ouvir."

                                    mari "Vem! Mete a língua na minha garganta, [mc]!"

                                    scene j6_new18 with Dissolve(1.0)

                                    pause

                                    mari "Hmmm... adoro..."

                                    mc "Você beija bem, Mari."

                                    mari "É a experiência. Eu sou treinada pra te dar prazer, [mc]."

                                    mc "Haha..."

                                    mari "E como tão as coisas aí em baixo?"

                                    mc "A-ainda não."

                                    mari "Então continua. Mete a língua como se tivesse me comendo, gostoso."

                                    mc "Mari... você é maravilhosa."

                                    mari "Nnhha..."

                                    mc "Hmm!"

                                    scene j6_new19 with Dissolve(1.0)

                                    pause

                                    mari "Opa... o que é isso que eu senti aí?"

                                    mc "Hehe... tô quase pronto pra você, linda."

                                    mari "Eu tava duvidando, mas você vai dar conta mesmo..."

                                    mc "Você vai sar daqui muito satisfeita. Você vai ver."

                                    mari "Então vem. Pode me sentir onde eu sei que você quer sentir."

                                    menu:
                                        "Fazer oral nela antes":


                                            mc "A gente vai chegar lá, mas eu vou preparar você antes."

                                            mari "Sério?"

                                            mc "Você merece depois do trato que você deu em mim."

                                            mari "Ser acarinhada é nova pra mim..."

                                            scene j6_new20 with Dissolve(1.0)

                                            pause

                                            mc "Comigo você vai ter muito disso."

                                            mari "Aah..."

                                            mc "Tudo bem?"

                                            mari "Faz tempo que eu não ganho um oral assim."

                                            mc "Faz?"

                                            mari "A-acho que eu... ahn... nunca eu ganhei de um homem..."

                                            mc "Mentira. Não sabem o que tão perdendo."

                                            mari "A maioria... ng... só querem saber de m-meter... ah..."

                                            mc "Não vai me dizer que foi a-"

                                            mari "Eu prefiro nnn... não falar..."

                                            mc "Tá bom. Mas se você falar, eu acelero aqui."

                                            mari "Como é?"

                                            scene j6_new21 with Dissolve(1.0)

                                            pause

                                            mari "A-ahnn!"

                                            mc "E aí, vai falar?"

                                            mari "Isso é sacan... ngh... -nagem!"

                                            mc "Vai falar ou não vai?!"

                                            mari "Assim! Nnnngg! Continua!"

                                            mc "Vai falar?"

                                            mari "Só lambe! AHNG! Me chupa, [mc]!"

                                            mc "Tá bom, chega."

                                            scene j6_new22 with Dissolve(1.0)

                                            pause

                                            mari "Ah... ahn... que maldade..."

                                            mari "Só por que eu não quis falar quem foi?"

                                            mc "Não. Foi brincadeira."
                                        "Ir direto para a penetração":


                                            mc "Eu não consigo esperar pra meter em você, Mari."

                                            mari "Foi o que eu pensei, gato."

                                    mc "Tá na hora da verdade. De eu sentir essa sua bucetinha."

                                    mari "Vem aqui."

                                    mc "Sua bunda é tão gostosa, posso te pegar por trás?"

                                    mari "Claro, querido. Ela é toda sua."

                                    scene black with dissolve

                                    scene j6_new23 with Dissolve(1.0)

                                    pause

                                    mc "Agh... entrei, Mari!"

                                    mari "Hmm... eu tô sentindo, bem."

                                    mari "Tá gostando?"

                                    mc "Ah... muito... sua bunda tá me apertando inteiro."

                                    mari "Que bom que você gostou."

                                    mc "E-eu vou acelerar."

                                    mari "É sua segunda hoje... vai com calma."

                                    mc "Não consigo! Eu preciso te fuder direito."

                                    mari "Ahnn... eu tô pronta pra gozar também. Pode ir fundo, amor."

                                    mc "Então toma, Mari! Toma!"

                                    mari "NNHG!"

                                    scene j6_new24 with Dissolve(1.0)

                                    pause

                                    mari "Hmm! Tá bom, [mc]. Tá pegando o ritmo! Nngg!"

                                    mc "Eu vou gozar em você de novo!"

                                    mari "Vai me engravidar, é?"

                                    mc "Isso só me dá mais tesão, Mari!"

                                    mari "Então me aperta! Eu quero gozar também!"

                                    mc "Então goza!"

                                    mari "Vem comigo! Vai, [mc]!"

                                    mc "Tá vindo!"

                                    mari "Vai! Agora!"

                                    scene j6_new25 with vpunch

                                    pause

                                    mc "AAAAARGH!"

                                    mari "Aaaii!"

                                    mc "Ah... tô t-tremendo..."

                                    mari "Você chegou lá mesmo... ufa..."

                                    mc "E você?"

                                    mari "Nunca... um homem me deu prazer desse jeito..."

                                    mc "Sério?"

                                    mari "Você fez direitinho, [mc]..."

                                    mc "Só mais um segundo... ainda tô... uff..."

                                    mari "Sem pressa, gato... curte o momento..."

                                    mc "A gente tem que repetir essa, Mari... você... foi incrível."

                                    mari "Quem sabe... mas agora eu queria falar com você."

                                    mc "Papo depois do sexo?"

                                    mari "Não seja cuzão."

                                    mc "Brincadeira... claro..."

                                    mari "Que bom... hehe..."

                                    mc "Depois dessa, você pode pedir o que quiser de mim... eu sou seu."

                                    mari "Vou cobrar, hein? Agora vem."
                        "Transar o mais rápido possível":


                            "Eu quero voltar o mais rápido possível pra casa."

                            "Vou dar uma trepada rápida com ela e voltar."





                            "..."

                            mari "Assim mesmo, [mc]!"

                            mc "Vou gozar, [mari]!"

                            mari "AAH!"

                    scene black with Dissolve(1.0)

                    mari "Vem aqui comigo."

                    mc "Opa."

                    scene j6_new26 with Dissolve(1.0)

                    mari "Então gostou mesmo..."

                    mc "Demais."

                    mari "Que bom. Eu também adorei."

                    mc "Você é demais, Mari. Por que você perde tempo com o Caio e esse pessoal?"

                    mari "Você acha eles tão ruins assim?"

                    menu:
                        "Com certeza.":


                            mc "Claro. Principalmente o Caio. Baita cuzão."

                            mari "Haha... se você diz..."
                        "Sei lá...":


                            mc "Sei lá, não conheço eles tão bem, mas pelo que eu vi, pelo menos o Caio é no mínimo um babaca."

                            mari "É... acho que muita gente ia concordar..."

                    mari "Não precisa se preocupar comigo. E se a gente falar da gente?"

                    mc "Da gente?"

                    mari "Eu queria saber se... foi só um lance ou se você tá pensando em ficar comigo pra valer."

                    mc "A gente não se viu muito, né, Mari?"

                    mari "Se viu o suficiente pra você me comer."

                    mc "Touché... bom... você tá sentindo alguma coisa por mim?"

                    mari "Eu falei pra você antes... eu quero que você me tire daqui."

                    mari "Você tá preocupado que eu ando com eles? Por que você não me leva daqui?"

                    mc "Mari... esse é um grande compromisso... eu não sei se a gente tá nesse momento ainda."

                    scene j6_new27 with Dissolve(1.0)

                    mari "Por que você só não fala a verdade e diz que eu sou uma mulher só pra ter caso, hm?"

                    mc "Porque não é isso..."

                    mari "Mentiroso. Você só tá comigo porque eu sou gostosa e sou boa no sexo."

                    if julia_namoro:

                        mari "Eu sei que você e a Júlia tão juntos, mas se você gosta de mim de verdade... a gente pode... e aí?"

                    "A Mari não tá legal... ela até me lembrou um pouco da Júlia..."

                    "Como se todo mundo só gostasse dela por causa do sexo."

                    "O que eu falo pra ela?"

                    menu:
                        "Desculpa, você é só um caso.":


                            mc "Mari, desculpa se você tava esperando uma coisa diferente, mas eu nunca pensei na gente como algo sério."

                            mc "Você é divertida, linda, é boa no sexo mesmo. Mas eu achei que a gente tava se curtindo."

                            mari "C-claro que você achou..."

                            mari "Tudo bem. Não me importo. Eu vou ficar com eles pra sempre, eu já sabia."

                            mc "Você... não precisa ficar com eles."

                            mari "E com quem eu vou ficar?! Sozinha?! Sozinha é triste demais..."

                            mc "Mari..."
                        "Eu quero algo sério com você.":


                            $ j6_mari_serio = True

                            mc "Eu não quero brincar. Eu quero um lance de verdade mesmo."

                            mari "Sei..."

                            mc "Tô falando sério. Você é a garota que eu quero do meu lado pra valer."

                            mari "Namoro? Duvido."

                            mc "Namoro. Se você topar... eu quero."

                            mari "!"

                            mc "E aí?"

                            mari "Eu acho que você tá tirando com a minha cara."

                            mc "É sério, pô! Se não quer, fala logo!"

                            mari "Você tá falando isso só pra me comer de novo, né? Tá bom, pode vir aqui."

                            mc "Não, Mari! Para com isso!"

                            mc "Nem tudo é sexo, poxa."

                    mari "E-eu tenho que voltar lá pra dentro."

                    mari "Eles devem tá se aproveitando da [g] lá... se eu fosse você eu dava uma olhada."

                    mc "Ei. Sobre a gente... a gente pode falar depois?"

                    mari "Hm... Eu vou pensar no seu caso."

                    scene black with dissolve

                    "Puxa... a Mari, a Júlia... o que aconteceu com elas pra ficar desse jeito?"

                    jump julia_e6_final_passeio
                "Melhor a gente parar aqui então.":


                    jump j6_mari_recusou

            mari "Alguma coisa aqui atrás tá ansioso."

            mc "Muito. Vamo vamo vamo."

            mari "Vem por aqui."

            scene black with Dissolve(1.0)



            "..."

            jump julia_e6_final_passeio
        "Você é incrível, mas não rola.":


            label j6_mari_recusou:

                pass

            mc "Malz, [mari], mas não vai rolar."

            mari "Aww... sério? Eu tava tão confiante..."

            mc "E tava confiante com razão. Você é muito gata, decidida, linda, tem um papo muito bom também."

            mc "Não vou ficar falando muito porque vai ficar parecendo aquele negócio do 'não é você, sou eu', e a gente já é adulto."

            mari "Mas pegar na minha bunda tá bom, né?"

            mc "Opa!"

            scene j6_mari_incomodada with Dissolve(1.0)

            mc envergonhado "Desculpa..."

            mari "Tô brincando..."

            mc normal "Você realmente é uma garota bacana."

            mari "Você fala isso, mas não quer ficar comigo."

            if julia_namoro:

                mc envergonhado "Eu tô com a [g]. Não ia ser certo com ela."

                mari "É só por isso mesmo?"

                mc "Basicamente..."

                mari "Então quem sabe um dia eu não conquisto você?"

            elif priscila_namoro or sayuri_namoro or maria_namoro:

                mc envergonhado "Eu e a [g] não tamo namorando, mas eu já tô de rolo."

                mari "Sério? Mas é só por isso mesmo?"

                mc "Basicamente..."

                mari "Então quem sabe um dia eu não conquisto você?"
            else:


                mc envergonhado "Eu não tô com a [g], mas eu vim por causa dela. Se eu deixar ela sozinha por aí, vai saber o que acontece."

                mari "Você é bonzinho demais, [mc]. Se fosse outro, já taria chamando a [g] de puta e deixado ela pra trás."

                mc desculpa "Talvez... mas é que ela realmente precisa de um apoio."

                mari "É verdade. Eu também acho isso. Talvez se ela tiver alguém com cabeça do lado dela..."

                mc normal "É o que eu penso também."

                mari "Mas então quem sabe outro dia eu consiga te conquistar..."

            mc envergonhado "..."

            mari "Não precisa fazer essa cara. Eu não vou ficar te esperando, [mc]."

            mari "Eu vou achar um cara bacana igual você um dia. Você que enrole muito que vai me perder."

            mc charmoso "Vou lembrar disso."

            mc normal "Agora vou dar uma olhada na [g]. Vai saber o que o [caio] queria falar com ela."

            mari "Boa sorte."

    scene casa_caio geral with Dissolve(1.0)

    "O que será que o [caio] quer falar com a [g]?"

    "Será que ele não entende que ele faz mal pra ela? Eles tentaram ficar juntos, mas não deu certo. Agora bora pra próxima."

    "Só que a [g] continua dando trela... ela devia era sumir da vista desse povo."

    g "Já ouvi, [caio]. Tchau."

    mc desconfiado "Hm?"

    caio "Espera!"

    mc angustiado "!"

    scene j6_julia_caio with Dissolve(1.0)

    pause

    "Que merda tá acontecendo aqui?!"

    caio "Só queria falar mais um negócio."

    g "Sai, [caio]..."

    caio "Só mais um negocinho."

    g "Tá... fala logo..."

    caio "É..."

    g "Se alguém ver a gente assim vão pensar besteira..."

    caio "E isso ia ser tão ruim assim?"

    g "..."

    "A [g] tá dando bola pra esse cara?! É sério isso?!"

    if julia_namoro:

        "Mesmo com a gente namorando... eu não tô acreditando no que eu tô vendo."

    "O [caio] nem tem mais nada pra falar. Ele só quer ficar a sós com ela. Certeza que ele quer beijar ela."

    "E aposto que a [g] já viu isso. Ela não é burra! Então por que ela só não sai andando?!"

    "Calma, [mc]... respira... e se ela não for fazer nada?"

    if julia_namoro:

        "Se eu realmente vou namorar ela, não dá pra ficar nessa constante desconfiança. Eu preciso confiar nela."
    else:


        "Eu sei que a gente não é namorado nem nada. Mas tá na cara que esse [caio] só empaca a vida da [g]!"

        "Até a [o] já falou isso. Mas e se a [g] não ficar por conta dela mesmo?"

    "Talvez seja melhor eu só deixar e ver o que acontece."

    "Mas e se eles ficarem? A culpa não vai ser minha também?! Eu vou ficar só olhando? Isso é um absurdo!"

    "Afe... por que eu tô passando por isso? O que eu faço?!"

    menu:
        "Se intrometer e acabar com a palhaçada":


            $ julia_e6 = "ruim"

            mc bravo "Ei! Que que tá rolando aqui?! Vamo parar com a palhaçada!"

            "Caio e Júlia" "Hm?!"

            mc "Sério mesmo que você vai ficar com esse cara de novo, [g]?!"

            scene j6_julia_caio_brava_mc with Dissolve(1.0)

            g "Ei! Quem disse que eu vou ficar com ele?!"

            caio "..."

            mc bravo "Você não tá vendo que esse cara faz mal pra você?! E fica de brincadeira com ele ainda por cima?!"

            if julia_namoro:

                mc "E isso nem é o importante! A gente tá namorando, caralho! Agora você fica coladinha com esse sujeito!"

                mc "O que você acha que eu vou pensar de ver vocês assim?! Você não tem vergonha?!"

            g "Você nem sabe o que tava acontecendo, seu idiota!"

            mc "Sou idiota mesmo pra achar que você quer sair dessa vida. Que você tá procurando coisa melhor pra você."

            g "!"

            mc desculpa "Eu realmente achei que você queria uma coisa diferente pra você. Mas parece que você não consegue!"

            g "Não acredito que eu tô ouvindo isso."

            caio "Tenham calma vocês dois. Tá tudo bem."

            mc irritado "Cala a boca!"

            caio "..."

            g "Você... você tá só vomitando merda, seu ridículo! Tem tanta coisa na cabeça, que já tá vendo o que quer!"

            mc bravo "O que eu quero? Quer que eu tire uma foto de como vocês tavam?!"

            g "... Eu não quero mais falar com você hoje!"

            "O que eu tô fazendo? O [caio] tá até parecendo o cara sensato da história."

            mc concentrando "..."

            mc desculpa "Olha aqui... eu não quero perder a cabeça, [g]. Desculpa por ter gritado."

            g "Idiota..."

            mc "Talvez eu realmente tenha exagerado um pouco. Mas você sabe que eu quero o melhor pra você."

            g "..."

            scene j6_caio_feliz with Dissolve(1.0)

            caio "Eu não vou atrapalhar vocês. Depois a gente se fala [g]. A gente vai voltar só de noite."

            caio "Você tá indo bem, campeão. Boa sorte!"

            mc bravo "..."

            scene j6_julia_mc_chateada with Dissolve(1.0)

            g "Ai, [mc]... não queria falar com você agora..."

            mc "Eu sei. Mas só me escuta rapidinho."

            mc "Eu não quero duvidar de você. Eu não quero falar também o que você deve ou não pode fazer. Eu não sou o seu pai."

            if julia_namoro:

                mc "Ainda mais porque a gente tá namorando. Eu quero confiar 100%% em você."

            mc "Só que... não é fácil. Você entende o que eu tô falando, né?"

            g "O que eu tô entendendo é que você tá falando que eu não consigo deixar minha piriquita quieta. É isso?"

            mc "Nã-não! Claro que não!"

            mc "Você e o [caio] tem um histórico. E eu nunca soube o que rola entre vocês. Nem sei como vocês se conheceram."

            mc "O que eu sei é o que eu vi lá na festa, no cinema e na faculdade."

            g "Olha, [mc]... você é um cara legal, de verdade."

            if julia_namoro:

                g "Eu sabia que não ia ser fácil, mas a gente começou a namorar. Nem namoramo direito pra falar a verdade, né?"

                mc "Pois é..."

            g "Sei lá... Eu tava esperando que você confiasse mais em mim. Eu não quero que você seja outra [o] na minha vida."

            g "Eu e o [caio] nem tava fazendo nada. Eu até tava deixando ele pra trás. Eu não ia ficar com ele."

            g "Se você tivesse ficado quieto e visse, talvez você entendesse que eu realmente não caio mais na dele."

            g "Mas agora parece que você que é o vilão. Você que não confiou em mim."

            g "O [caio] pode ter uma personalidade horrível, mas ele sempre acreditou em mim. Ele nunca veio falar o que eu tenho que fazer."

            g "Ele me aceita do jeito que eu sou. Era isso que eu queria de você."

            if julia_namoro:

                g "E se você não acredita na sua namorada, então, sei lá. Depois a gente vê..."
            else:


                g "E se você não acredita que eu posso mudar, então, sei lá... não sei se eu preciso da sua amizade agora..."

            g "Tchau."

            mc "Espera. [g]!"

            g "..."

            scene casa_caio geral with Dissolve(1.0)

            mc preocupado "[g]!"

            "..."

            "Merda! Não é possível que ela colocou a culpa em mim!"

            "Os dois tavam quase abraçados. Daí depois ia dar merda e eu ia ficar só olhando?! Que saco..."

            "Não quero mais saber dela também. Se ela quiser sumir, azar o dela."

            "Que droga..."

            "..."

            jump julia_e6_final
        "Ficar onde está e deixar as coisas rolarem":


            $ julia_e6 = "bom"

            "Merda. Pode me chamar de gado, mas eu quero acreditar em você, [g]. Vamos ver se sua cabecinha vai aprontar..."

            if julia_namoro:

                "A gente tá namorando agora. Eu sei que ela não vai colocar isso a perder assim. Eu sei..."
            else:


                "Ela disse que queria algo diferente. Ela não quer mais o [caio]. Eu acredito que ela vai escolher o certo."

            g "Fala logo, [caio]!"

            "Opa."

            caio "Tá! Calma! Eu vou falar... É que... eu não queria que a gente acabasse o que a gente tem."

            g "Como assim? Tá louco? A gente não tem mais nada."

            caio "[g]... você sabe que isso é mentira. Você pode falar isso quantas vezes você quiser. Ainda rola alguma coisa entre a gente."

            g "Não..."

            caio "Eu sei que você gosta de ficar comigo."

            g "..."

            caio "Mais uma vez só. Pelos velhos tempos..."

            g "Você já... falou isso antes..."

            caio "Só tá nós dois aqui. Vai..."

            g "[caio]... eu..."

            caio "Vem aqui."

            if not julia_namoro:

                scene j6_julia_caio_beijo with Dissolve(1.0)

                pause

                g "Ai... eu sabia que ía acabar nisso..."

                caio "Hmm... como você é gostosa..."

                g "Me beija..."

                g "Ai..."

                caio "Você não pode ficar sem isso, gata. Eu sei que você gosta."

                g "Não importa... não era... chega..."

                caio "Só mais um pouco."

                g "Hmm..."

                g "Tá bom, tá bom."

                caio "Cala a bo-"

                scene j6_julia_caio_brigando with hpunch
            else:


                scene j6_julia_caio_brigando with hpunch

                g "Não!"

            g "Eu falei sai! Que saco, [caio]!"

            caio "Que porra você tá fazendo, [g]?!"

            mc surpreso "!"

            g "Eu falei que eu não quero nada com você, caralho! Você não escuta?!"

            caio "Você sempre falou não e mes-"

            g "Cala a boca, nojento! Você sempre fez o que você quis comigo. Agora chega."

            caio "A gente sempre ficou, [g]! Isso nunca deu nada de ruim!"

            if julia_namoro:

                g "Só que agora eu tô namorando! Eu já falei isso!"

                caio "Com aquele gado idiota?! Aquilo não é homem pra você! Ele deve ser um gayzinho!"

                g "Primeiro que ser gay não é uma ofensa, babaca... você nem sabe o que tá falando! E segundo que... que..."

            g "Foda-se! Eu não quero mais e pronto!"

            caio "Sua vaca... você não vai sumir assim!"

            scene j6_julia_caio_brigando2 with Dissolve(1.0)

            g "Não vou?! Você acha que você manda alguma coisa na minha vida?!"

            caio "[g]! Você nem ia ter vida se não fosse eu! Você lembra disso?!"

            g "Sai de perto de mim..."

            caio "De jeito nenhum! Você... você vai ficar comigo! Até eu falar que você pode sair!"

            g "Você é um monstro! Por causa desse seu jeito que eu nunca consegui me sentir bem com você!"

            g "Se você só... normal, sei lá! A gente podia tá junto, idiota!"

            caio "Normal?! Você tá falando que eu não sou normal?! Você que não é normal, sua puta!"

            caio "Quem que muda de cabeça assim do nada?! Dando pra mim sempre e agora não me toca!"

            g "Sai [caio]! Sai fora!"

            caio "Para de gritar!"

            g "Se você não sair vai todo mundo ouvir!"

            caio "Nem ligo... mas tá bom... O [teo] e a [mari] não são igual você. Eles têm lealdade. Mas seu amiguinho..."

            caio "Isso não acabou, [g]."

            g "Sai..."

            scene casa_caio geral with Dissolve(1.0)

            "Caraca... A coisa saiu do controle rápido."

            "Será que eu falo com a [g] agora?"

            g "[mc]? Você tava aí?"

            "Caralho ela me viu!"

            scene j6_julia_irritada with Dissolve(1.0)

            mc envergonhado "E aí?"

            g "Ouviu?"

            mc "Sim, ouvi. Acho que todo mundo ouviu."

            g "É até bom... aquele filho de uma puta..."

            "Ela parece tão abalada. Até o rosto dela tá diferente..."

            mc desculpa "Eu não vou encher seu saco. Quer voltar pra casa?"

            g "A gente nem fez nada ainda..."

            mc envergonhado "Esse passeio foi uma merda mesmo."

            g "Desculpa..."

            mc "Ei. Não precisa pedir desculpa. Pelo menos eu vi você de biquini."

            g "Que comentário de tonto..."

            mc "..."

            scene j6_julia_mc_chateada with Dissolve(1.0)

            g "E a [mari] também, né, safado?"

            if julia_namoro:

                mc charmoso "Eu só tenho olhos pra você."

                g "Não precisa mentir... mas obrigada mesmo assim. Não tem problema olhar, eu sei que ela é gostosa."

            mc envergonhado "Haha..."

            g "Eu perdi a linha ali atrás, né?"

            mc preocupado "Você falou o que tinha que falar. Eu tô orgulhoso de você."

            g "Eu não queria ter explodido, mas o [caio] sempre me deixa muito irritada."

            mc desculpa "Sei... Olha, [g]... desculpa se não for a hora, mas de onde vem essa sua históra com ele?"

            g "Com o [caio]?"

            mc "É. Eu sei que vocês se conhecem desde antes da faculdade. E não dá pra negar que vocês tem uma ligação."

            g "Tá com ciúmes?"

            mc envergonhado "Talvez um pouco. Mas não é isso."

            g "Sei..."

            scene j6_julia_mc_contando with Dissolve(1.0)

            g "Certeza que você vai ter saco pra essa história agora?"

            "Será que é uma boa aceitar? Ou melhor só deixar as coisas assim e levar ela de volta?"

            menu:
                "Escutar a história dela":


                    $ j6_historia = True

                    mc charmoso "Claro que eu vou ter saco. Eu que perguntei, ué."

                    g "Acho que vai ser bom pra mim eu falar sobre isso. Eu... preciso encerrar isso de uma vez por todas, [mc]."

                    mc "Isso."

                    g "Mas não é uma história com final feliz."

                    mc "Não importa."

                    g "Tá... eu... vou tentar falar rápido. Mas é que acho que ninguém sabe disso."

                    g "Tipo... quando eu entrei no colegial, a [s] tinha voltado de algumas competições já e ela me ajudou bastante."

                    g "Eu era uma menina quietinha, e daí eu fui ganhando confiança e comecei a chamar atenção na sala."

                    g "Era uma escola chique. Os pais da [s] sempre pagaram tudo pra mim. E o pessoal começou a olhar pra mim."

                    g "Só que logo esse meu jeito começou a afastar as meninas. Elas não foram muito com esse jeito meio brincalhão meu."

                    mc desculpa "Sei..."

                    g "Só que teve um pessoal que gostou... Os meninos... logo eu entrei pro grupinho deles."

                    g "Eles eram legais e não demorou muito pra um querer alguma coisa comigo. Eu não tinha muita experiência, mas eu lembro que até fiquei feliz."

                    g "Eu tava nervosa, mas aceitei. A gente se beijou. Ele foi legal comigo. Acho que eu até comecei a gostar dele mesmo..."

                    scene j6_julia_irritada with Dissolve(1.0)

                    g "Só que um dia eles vieram rindo... outro amigo disse que esse menino tinha deixado ele ficar comigo."

                    mc desconfiado "Como assim?"

                    g "Eu não entendi direito também. Mas é como se ele tivesse dividindo eu com o amigo dele."

                    g "Eu disse que não, mas ele falou que era assim no grupo deles. Se eu quisesse continuar falando com eles, eu tinha que ficar com ele."

                    g "O pior é que depois de falar com o menino que eu gostava, ele realmente deixou. E eu acabei ficando com o amigo. Não era nada de mais também."

                    g "E daí fiquei com o outro e com o outro. Eu não entendi direito, mas eles eram legais comigo. Nunca me forçaram nada fisicamente assim."

                    mc desculpa "..."

                    g "Até aí... era estranho, mas eu não ligava. A gente era tudo amigo mesmo."

                    g "E então um dia eu ia sentar na minha carteira, e alguém tinha escrito 'puta' lá. Eu apaguei e fiquei muito nervosa."

                    g "Depois de alguns dias tava escrito de novo. Só que dessa vez tinham raspado na mesa. Não dava pra tirar."

                    mc preocupado "Que merda, [g]..."

                    scene j6_julia_mc_contando with Dissolve(1.0)

                    g "Foi passando o tempo e foram escrevendo mais e mais coisas. Escreveram no banheiro."

                    g "Meus amigos falavam pra eu não ligar, mas ninguém me falava quem era. Aquilo foi ficando muito ruim."

                    g "Claro que eu não ia falar pros pais da [s]. E sorte minha que ninguém na escola tinha visto."

                    g "Eu falei pros meus amigos que não ia mais ficar com ninguém nunca mais. E daí eles pararam de falar comigo."

                    mc "Não acredito."

                    g "Acho que eles queriam ver se eu ia mudar de ideia, mas eu tava decidida. E daí ninguém mais falou comigo."

                    g "Continuavam a escrever coisas sobre mim e eu fui me isolando. Tentei trocar de carteira, mas colocaram a carteira antiga onde eu tava."

                    g "Aquilo me deixou muito triste... a ponto de eu... de eu... só querer acabar tudo, sabe?"

                    g "Eu queria que tudo sumisse. As risadas, as frases no banheiro, a maldita carteira..."

                    g "Daí um dia chegou um garoto novo na escola. Ele veio pra nossa sala e o único lugar vago era do meu lado."

                    g "Parece que ele tinha sido expulso da escola que ele tava e veio pra nossa, que também era boa."

                    g "Ele sentou do meu lado e eu lembro até hoje a primeira coisa que ele me falou: 'Calma. Eu não vou morder. Não precisa fazer essa cara'."

                    g "Era a primeira vez que alguém falava comigo e eu não consegui nem responder direito."

                    g "Ele sacou na hora olhando pra carteira que tinha alguma coisa errada. Daí no intervalo ele sentou comigo."

                    g "Ele tentou puxar conversa, mas eu só respondia seco. Eu tava muito feliz, mas eu sabia que não ia durar muito."

                    g "E dito e feito. Uma menina veio chamar ele pra sentar com ela e as amigas. E ele foi na hora claro. Ele era boa pinta e tal."

                    g "Eu tava cada vez com mais vontade de deixar a escola. Não ia aguentar aquilo nem mais um mês."

                    g "Mas no outro dia, esse aluno novo sentou comigo outra vez. Ele falou que não gostou das meninas, elas falavam demais."

                    g "Eu sorri e ele falou alguma coisa, mas daí eu comecei a chorar, sei lá por que... e ele ficou todo tonto sem saber o que fazia."

                    g "No outro dia eu cheguei e não achei minha carteira. Tinha outra no lugar. No intervalo ele disse que quebrou ela de propósito."

                    g "Bom... acho que eu acabei falando muito... acho que deu pra sacar, né?"

                    mc preocupado "[g]..."

                    scene j6_julia_mc_abracados with Dissolve(1.0)

                    pause

                    g "Q-que foi? Eu disse que não era feliz."

                    mc "Muito obrigado por contar isso pra mim. Eu sei que não é fácil."

                    g "É... mas e agora?"

                    mc "Sabe... você falou que essa história não tinha um final feliz. Mas a verdade é que essa história ainda não acabou."

                    mc "Você ainda tem 18 anos, moça. Você ainda vai viver quatro vezes isso."

                    g "Credo, [mc]. Eu não quero viver 90 anos."

                    mc "Quatro vezes dezoito não é 90, mas não se preocupe. Você vai viver muito ainda."

                    mc "Dá tempo de ter um final incrível pra essa história. E vai ser a história mais bonita que as pessoas já viram."

                    mc "Coisa de cinema mesmo."

                    g "..."

                    g "Vamos ver, né? Porque não tá fácil esse final bom aí..."

                    mc "Tá sim. Pelo que eu vi hoje, o pior já passou. Agora é a parte que tudo dá certo, você vai ver."

                    g "Nos filmes as coisas só dão certo no final, idiota..."

                    mc "Vai ser outro tipo de filme então!"

                    g "Para que a metáfora não deu certo. Você já cagou nela."

                    mc "Tá bom. Só que pode escrever o que eu tô falando. Eu vou tá com você pra ver esse final aí. E vai ser massa pra CARALHO."

                    g "..."

                    g "Valeu, [mc]. Só você pra aguentar esse enredo cansado..."

                    mc "Esse roteiro aí é tudo, menos cansado."

                    g "Haha... tá..."



                    g "Ah... eu sei que depois do meu filme o clima não é dos melhores, mas queria te recompensar..."

                    mc "?"

                    scene black with dissolve

                    scene j6_new28 with Dissolve(1.0)

                    pause

                    mc "Uau..."

                    g "Sabia que você ia curtir dar uma olhada no material."

                    mc "Eu sempre vou gostar, mas, olha, eu tava pensando numa coisa."

                    g "Eu sei exatamente no que você tava pensando..."

                    mc "Haha... não... escuta."

                    mc "Eu acho que tem uma coisa que você entendeu errado."

                    mc "Sexo não é a única coisa que você pode oferecer pras pessoas."

                    g "Aham... agora olha aqui."

                    scene j6_new29 with Dissolve(1.0)

                    mc "J-júlia! Escuta."

                    mc "Você é bacana, você é divertida, sabe conversar."

                    g "Você fala isso enquanto olha pra mim pelada..."

                    mc "Você que tá arrancando a roupa enquanto eu falo!"

                    g "Eu sei o que você tá tentando falar, valeu. Mas eu sei que é mentira."

                    mc "N-não é!"

                    g "Quer saber... tô cansada."

                    mc "Ok... mas eu queria explicar isso pra você uma hora..."

                    g "Uma hora... mas agora, não."

                    mc "Fechou. Então agora..."
                "Se negar a ouvir e falar pra voltarem logo":


                    mc "Vamos deixar essa história pra outro dia. Não quero que você se preocupe com isso agora."

                    g "... tá."

                    mc "Diferente desse merda aí, pode contar comigo pra sempre, Ju. Eu tô aqui pra você."

                    g "Valeu."

                    mc "E agora?"

            mc "Bora? Ou animou pra ficar aqui?"

            g "De jeito nenhum. Bora pra casa."

            mc "Eu vou deixar você lá."

            g "Que cavalheiro."

            scene black with Dissolve(1.0)

            "Ufa... que dia..."

            jump julia_e6_final

    label julia_e6_final_passeio:

        scene casa_caio noite with Dissolve(3.0)

        "A gente curtiu muito o resto do dia juntos. Foi até escurecer."

        "Eles iam voltar juntos de carro. Dessa vez eles me levaram até o ponto e eu consegui pegar o busão de boa."

        if j6_final_mari:

            "Acho que ninguém se ligou no que rolou comigo e com a [mari]. A [g] nem perguntou também. Pelo menos pra mim."

            "Não dá pra saber se vai tudo continuar de boa com a gente."

        "Agora é só torcer pra que dê tudo certo."

    label julia_e6_final:

        pass



    scene black with Dissolve(3.0)

    $ tempo = 3

    $ v33_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v33_fim","final","local")

    scene black with Dissolve(3.0)

    call checa_final

    jump call_cidade

label julia_evento7:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j7_save", extra_info="j7_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ julia_e7 = "evento"

    $ j7_carol = False
    $ j7_carol_beijo = False
    $ carol_amizade = 0
    $ j7_lesbica = False

    "Hmmmm.... Acho que hoje eu vou dormir até um pouco mais tarde."

    scene black with dissolve

    "A cama parece que tá mais fofinha que o normal hoje... tá até cantando uma musiquinha."

    "Vem...{w} Te quero do meu lado... {w}"

    "..."

    scene sayuri tadaima_julia

    $ renpy.pause(delay=0.2, hard=True)

    scene julia sentada_parte1

    $ renpy.pause(delay=0.2, hard=True)

    scene jp_julia3

    $ renpy.pause(delay=0.2, hard=True)

    scene julia_carol_biblioteca1

    $ renpy.pause(delay=0.2, hard=True)

    scene cinema_sala_julia_sozinha

    $ renpy.pause(delay=0.2, hard=True)

    scene ape_cama with hpunch

    mc "U-uou!"

    "Sonhei com a [g]...{w} Essa mina me atormenta até quando eu tô dormindo?"

    "Isso que dá dormir fora de hora."

    scene ape_pensando with Dissolve(1.0)

    "Agora fiquei preocupado... será que ela tá legal?"

    "As coisas com ela nunca são fáceis. É só pedreira atrás de pedreira."

    "Tanto que esses tempos a gente nem conseguiu fazer nada divertido."

    if j5_good:

        "A última vez foi lá no cinema."
    else:


        "Lá no cinema ela ficou com aqueles porra louca."

    "Depois disso nem rolou mais nada. Nem provocação direito..."

    "Quando eu conheci a [g] ela era super sapeca. Cada coisa que ela queria comigo..."

    "Só que de uns tempos pra cá eu sinto que ela não tá me dando muita bola."

    if julia_e6 == "biblioteca":

        "Da outra vez que a gente se viu ela ficou estudando com a [o] lá na biblioteca."

        "Até que foi bacana ver a [g] pensando em outra coisa que não seja beijo na boca, mas a gente não fez nada juntos..."
    else:


        "Quando a gente foi na casa de passeio do [caio] lá a gente quase nem fez nada divertido juntos."

        if j6_final_mari:

            "O fato de eu e a Mari ter saído pra se pegar não deve ter ajudado muito..."

            "Talvez eu devesse ter negado ela. Mas a Mari é tão deliciosa. Quem ia conseguir?"

        elif julia_e6 == "ruim":

            "Ainda ver ela com o [caio] lá. A [g] não tem salvação mesmo. Por que ela ficou com o idiota de novo?"
        else:


            "A gente até conversou e tudo... mas ela tava super pra baixo."

            "Eu fico feliz de ter sido um ombro amigo... ela tava precisando, tadinha..."

    "Mas e a nossa diversão juntos? Acho que eu vou ch-"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trr... trrr..."

    scene ape_geral with Dissolve(1.0)

    mc zerado "Só pensar em querer fazer bagunça e parece que ela consegue ler nossa cabeça."

    mc normal "Oi?"

    g "E aí, gostosoooo!"

    if julia_namoro:

        mc charmoso "Fala, gata. Como tá?"
    else:


        mc envergonhado "E aí, [g]. Tudo bem?"

    g "Tô excitada, [mc]."

    mc surpreso "T-tá o quê?"

    g "Eu ganhei um presente hoje!"

    menu:
        "Fala de novo. Tá o quê?":


            mc envergonhado "Você pode voltar um pouco? Você falou que tá o quê?"

            g "Hm? Que eu tô feliz. Eu tô empolgada com meu presente!"

            mc "Aahh! Tinha entendido outra coisa. Disfarça."
        "Que presente?":


            mc desconfiado "Que presente que você ganhou?"

            g "Vai abrir um novo resort aqui na capital. E um amigo meu me chamou pra ir lá."

            mc "Resort? Aqui na ilha?"

            g "Não. É aqui no continente. Nem tudo que é bom é aí na ilha. Não precisa se achar tanto."

            mc charmoso "Você sabe que aqui é o point, né?"

            g "Tá passando vergonha."

    g "Presta atenção. Meu amigo me deu um ingresso vip. O legal é que eu posso levar duas pessoas comigo."

    if julia_namoro:

        mc charmoso "Que bom que você lembrou do seu namorado."

        g "Fazer o quê, né? É o que a sociedade espera."

        mc zerado "Como é?"

        g "Tô zoando, [mc]. Zuerinha!"
    else:


        mc normal "E você me escolheu?"

        g "Claro! Você é meu melhor amigo!"

    mc desconfiado "E a outra pessoa? Quem você vai levar?"

    g "É uma pessoa que eu tô querendo ficar aí?"

    mc zerado "Que que foi?"

    g "Haha... brincadeira. É a [o]. Lembra dela?"

    menu:
        "Certeza que ela é uma boa?":


            mc "Você acha que é uma boa chamar a [o]?"

            g "Por quê?"

            mc "Sei lá, ela não curte muito farra, né?"

            g "Ah... isso é verdade, só que ela vai ter que dar um jeito de ir."
        "Que bacana! A [o] é uma boa escolha.":


            $ carol_amizade += 1

            mc normal "Que legal! A [o] vai ser uma boa. Ela é tranquila, e ela gosta de você, [g]."

            g "Ela é sem graça, mas eu gosto dela, fazer o quê."

    mc "E como é que você vai fazer ela ir? Não sei se ela vai topar só porque você tá querendo."

    g "É aí que você entra."

    mc zerado "Eu?"

    g "É."

    scene ape_celular_falando with Dissolve(1.0)

    mc "Hah! O que eu tenho a ver com isso?"

    g "Se eu for lá e falar com ela, ela vai só negar e mandar eu ler alguma coisa ainda por cima."

    mc "É... parece uma coisa que a [o] falaria mesmo."

    g "Ela é muito ewwwww entendeu? Toda certinha. Só que ela vai escutar você se você inventar alguma coisa."

    mc "Inventar? Você que tá inventando [g]."

    g "Não! Tipo, falar pra ela que é importante pra mim, pra eu não me misturar com o pessoal errado e talz..."

    mc "[g]..."

    g "Por favor, [mc]!"

    if julia_namoro:

        g "Você é meu namorado ou não é?"
    else:


        g "Você é meu melhor amigo ou não é?"

    mc "... {w}Tá bom. Eu falo com ela."

    g "Legal! Já pega ela e já vai pra lá de busão. Vou mandar o endereço certinho pra vocês depois."

    g "A gente se vê lá! Beijo, gatoso!"

    mc "Bei-{w=0.5}"

    "{i}Tuuuuu-{/i}"

    "Desligou."

    scene black with dissolve

    "A [g] sempre foi mimada desse jeito? Pior é que eu acho que sim..."

    call locomocao from _call_locomocao_9

    scene museu2 with Dissolve(1.0)

    "Um dia em um resort novinho com a [g]... e a [o] ainda por cima?"

    if not nathan_namoro:

        "Quando eu ia imaginar que eu ia sair num lugar de rico desses com duas gatas?"

        "Só um idiota ia reclamar dessa situação."

        "Eu tenho que convencer a [o] de qualquer jeito... imagina as duas brigando pela minha atenção?"

        "Hihihi"

        mc zerado "Agora eu tô parecendo um tarado."
    else:


        "Quem dera fosse o [n] comigo nessa situação..."

    "A [o] gosta bastante da [g]. Se ela fosse fazer alguma coisa assim, ia ser pra proteger ela."

    "Com certeza eu posso usar isso pra convencer ela, mas não ia ser mancada?"

    scene biblioteca 2andar with Dissolve(1.0)

    "Cheguei."

    mc normal "Oi, [o]. Tudo bem?"

    o "[mc]! V-você!"

    scene carol_biblioteca_incomodada with Dissolve(1.0)

    pause

    mc normal "Oi, [o]. Tudo bem com você?"

    o "T-tudo... o que você tá fazendo aqui?"

    menu:
        "Tava procurando um livro...":


            $ carol_amizade += 1

            mc normal "Eu vim aqui porque eu tô procurando um livro."

            o "Sério? Que livro?"

            mc envergonhado "Um livro... é... sobre jornalismo. Quero melhorar minhas habilidades de paparazzo."

            o "E como é o nome do livro?"

            mc "O nome? É... não tem nome. Qualquer livro sobre isso aí."

            o "Qualquer livro sobre jornalismo? A gente tem alguns aqui. N-não sei se vai ajudar você."

            mc "Opa. Valeu."
        "Vim procurar você.":


            $ carol_amizade += 2

            mc charmoso "Eu vim procurar você."

            o "E-eu?"

            mc "É. Eu sabia que você ia tá aqui. E depois que a gente conversou aquele dia, fiquei com vontade de ver você de novo."

            o "S-sério?"

            mc "Tô incomodando?"

            o "N-não. Eu só vim aqui terminar de arrumar umas coisas que não deu tempo ontem. Mas já terminei."

            mc "Ah, legal."
        "A [g] que me pediu pra vir aqui.":


            mc envergonhado "A [g] que me pediu pra vir. Ela disse que você ia tá aqui."

            o "Ah... o que a [g] quer agora?"

            mc "Você conhece bem ela, né?"

            o "Se ela falou pra você vir aqui é porque tá com medo de falar comigo..."

            mc "Haha..."

    mc normal "É... você realmente gosta da biblioteca, né? Mesmo em dia de folga você vem pra cá."

    o "Ah... acho que eu gosto desse ambiente aqui. Eu sou meio que o contrário da [g] nesse sentido."

    o "Ela adora sair e fazer as coisas com os outros. Por isso que ela tá sempre se metendo nessas farras dela aí."

    mc "E você? Não gosta de sair?"

    o "Eu gosto de ficar mais sozinha. Não é que eu gosto de ficar em casa. Eu não ligo de sair."

    o "Mas eu me sinto melhor quando eu tô sozinha. Quando eu tô com os outros eu me sinto meio cansada..."

    o "D-desculpa por ficar falando dessas coisas."

    mc normal "Que nada. Eu gostei de ouvir sobre você."

    menu:
        "Mas você não fica triste quando tá sozinha?":


            mc desculpa "Mas você não fica triste quando tá sozinha? Não bate aquela solidão? Aquela vontade de ver alguém..."

            o "Eu não sei se eu sou estranha... mas eu não sinto isso. A [g] já me falou que sente uma coisa assim."

            o "Ela fica meio desesperada quando fica muito tempo sozinha. Não sei se a maioria das pessoas são assim."

            scene carol_biblioteca_vergonha with Dissolve(1.0)

            o "Só que eu não me sinto assim. Eu me sinto bem quando eu tô aqui na biblioteca e não tem ninguém."

            o "E quando eu volto pra casa também e eu tô no meu quarto, e eu gosto de ler e ouvir música... eu me sinto bem..."

            mc normal "Caraca... isso é legal, [o]. Eu não sei se eu me sinto assim quando eu tô sozinho."

            mc "Acho que eu sou mais parecido com a [g] nisso."

            o "Tudo bem... acho que não tem jeito certo. Cada um é uma pessoa."

            o "Só ver nos livros como tem muito tipo de personagem diferente. Imagina se todo mundo fosse igual?"

            mc envergonhado "É verdade... você falou tudo agora."
        "Eu também prefiro ficar sozinho.":


            $ carol_amizade += 1

            mc envergonhado "Se você quer saber, acho que eu também prefiro ficar sozinho."

            scene carol_biblioteca_vergonha with Dissolve(1.0)

            o "Sério? Então você sabe como é."

            mc normal "É. Acho que isso é porque a gente é mais introspectivo. A gente se diverte mais na nossa cabeça que fora."

            o "Acho que é isso mesmo, [mc]... por isso que eu gosto tanto de livro, de música... eu sinto que tá na minha cabeça."

            o "Só que as pessoas falam que eu tô triste, que eu sou antissocial. Não é isso..."

            mc envergonhado "Tem gente que não entende, né? Acha que pra tá feliz a gente tem que tá por aí causando."

            mc charmoso "Às vezes a gente quer só curtir a gente mesmo."

            o "Assino em baixo.{w} Olha, mas eu não imaginava que você fosse assim, [mc]. Ainda mais sendo um jornalista."

            mc envergonhado "É... parece um pouco estranho mesmo."

            o "S-só que eu entendo, viu?! Não tá errado nem nada assim."

            mc "Haha... eu entendi. Eu vou levando as coisas do meu jeito."

            o "Tá certinho."

    mc "Mudando de assunto, você tem falado com a [g]?"

    o "Sim. Na faculdade."

    mc "Ela tá legal?"

    o "Tá sim."

    if julia_e6 == "biblioteca":

        o "Ela não ter ido naquele passeio com o [caio] e ter ficado estudando aqui ajudou bastante ela."

        o "Eu senti que ela tá mais tranquila."

        mc normal "Que beleza."
    else:


        o "Aquele passeio de vocês na casa do [caio]... eu sinto que ela voltou diferente de lá."

        mc desconfiado "Diferente como?"

        o "Não sei explicar, mas diferente..."

        mc "Hmmm..."

    mc envergonhado "Então... não quero que você fique brava comigo, mas ela quer que a gente vá num lugar com ela."

    scene carol_biblioteca_incomodada_close with Dissolve(1.0)

    o "O que que ela tá aprontando dessa vez?"

    mc normal "Eu não sei se é uma 'aprontada' mesmo ou se realmente é uma coisa boa."

    mc envergonhado "Ela quer que a gente vá com ela em um resort."

    o "Resort? Que resort?"

    mc "Ela disse que ganhou um convite vip e pode levar duas pessoas."

    o "E ela chamou a gente?"

    mc "Pois é..."

    o "Olha... acho que isso é um bom sinal. Só de ela não ter pensado no babaca já é uma vitória eu acho."

    mc normal "Você acha? Então tu acha que é uma boa a gente ir?"

    o "Hmmm..."

    o "Se você prometer que vai me ajudar a manter ela na linha, eu acho que pode ser bom."

    mc desconfiado "E o que é manter ela na linha?"

    o "Sem muita bagunça, ora. Não querer transar com ela na piscina no meio de todo mundo é um exemplo."

    mc "Nem uma baguncinha?"

    o "Não..."

    menu:
        "A gente vai pra curtir. Não seja séria demais.":


            mc charmoso "A gente vai pra curtir, [o]... não precisa ficar assim tão séria. Tudo vai ficar bem."

            o "[mc]... você não tá me passando nenhuma confiança."

            mc "Eu prometo que a gente não vai estrapolar demais."

            o "Estrapolar demais é redundância. Não é nem pra estrapolar..."

            mc "Ok..."
        "Combinado. Eu vou ajudar manter ela na linha.":


            $ carol_amizade += 2

            mc envergonhado "Tá legal... pode contar comigo pra manter a [g] em ordem."

            scene carol_biblioteca_sorrindo with Dissolve(1.0)

            o "Legal! Eu vou cobrar você depois, hein?"

            mc normal "Pode deixar."

            o "Se a [g] tiver um tempo sem coisa envolvendo pegação, sem aflorar os hormônios dela, talvez ela veja que tem mais coisa na vida."

            mc envergonhado "Talvez ela esteja precisando disso mesmo..."

            o "Com certeza ela tá precisando, [mc]. Aquela mulher é o fogo em pessoa."

            mc "..."

    mc "Ela disse pra gente ir direto daqui."

    o "Ah... isso explica o endereço que ela me mandou aqui por mensagem sem nem falar o que era."

    mc "Tá explicado. Então vamos?"

    o "Eu vou pegar minhas coisas e fechar tudo aqui daí a gente já vai."

    scene biblioteca 2andar with Dissolve(1.0)

    "Até que ela aceitou fácil... a [g] tem uma amiga e tanto. Eu sinto que a [o] faria muita coisa pra ajudar ela."

    "A [g] precisa perceber isso logo e dar mais atenção pra [o] menos pro [caio] e aquela turma."

    o "Tô pronta."

    mc "Então bora."

    scene black with dissolve

    "..."

    scene resort_geral with Dissolve(2.0)

    pause

    mc surpreso "Uou! O lugar é demais!"

    o "Será que a gente pode usar isso aqui mesmo de graça?"

    mc normal "Acho que sim. Você não viu o que a moça da recepção disse? Eles tavam até esperando a gente."

    o "Verdade..."

    g "Oie! Cheguei!"

    o "J-ju..."

    scene j7_imagem1 with Dissolve(1.0)

    pause

    g "Nossa... olha só pra isso aqui... é do caralho mesmo, hein?"

    o "Não precisa falar palavrão desse jeito..."

    g "Vocês têm muita sorte de ter uma amiga que consegue isso de graça pra vocês."

    mc "E como você conseguiu isso?"

    g "Eu tenho meus contatos."

    mc desconfiado "..."

    o "Aposto que tem alguma coisa a ver co-"

    g "Para de ser chata, [o]. Não vai causar no nosso dia. A gente veio pra curtir isso aqui."

    o "Só tô falando que eu não quero que isso venha cobrar seu preço depois."

    g "Você tá falando como se fosse um filme da Disney. 'Uuuhh... vai cobrar seu preço...'"

    menu:
        "Um dia de curtição não tem problema.":


            mc "Relaxa, [o]. É só um favor que fizeram pra [g]. Ninguém vai cobrar nada por causa disso."

            g "Exatamente! Tá tudo em casa."

            o "Vocês são inocentes demais. Ninguém paga um resort desses por nada."

            o "E por que você não quer falar como conseguiu isso, hein, [g]?"

            g "Porque... porque você é xereta demais."

            mc charmoso "Tá tudo certo. Bora esquecer isso aí."

            g "Tá vendo? É só você que é estraga prazer, [o]!"
        "Eu tô meio com o pé atrás também...":


            $ carol_amizade += 2

            mc desconfiado "Isso tá estranho mesmo, [g]. Que presente foi esse que você ganhou aí?"

            g "Não interessa... vocês são muito mimados. Ganham um negócio desses e ainda reclamam."

            mc envergonhado "Todo mundo sabe que você é meio doidinha, só isso."

            o "O [mc] entende o que eu tô falando, [g]. Você não pensa muito nas consequências."

            g "Vocês dois tão muito amiguinhos."

            g "E eu sei que o [mc] só tá falando isso por causa da [o]. Você que tá fazendo a cabeça dele."

    o "Eu? E-eu não fiz nad-"

    g "Você vai pagar por isso."

    o "!"

    scene j7_imagem2 with Dissolve(1.0)

    pause

    o "J-jul-"

    g "Você vai pagar por colocar os outros contra mim!"

    mc "[g]!!!"

    o "E-eu não tô me sentindo segura aqui, [g]..."

    g "Você é meio pesada mesmo, [o]... você tá comendo muito ultimamente?"

    o "Como assim!? N-não tem nada a ver com isso!"

    g "Esse negócio de só ficar lendo na biblioteca... isso sim tá cobrando seu preço."

    o "Para de me chamar de gorda!"

    g "Se bem que no seu caso..."

    o "[g]! Me coloca no chão ou eu vou começar a me debater!"

    g "A gente tá bem do lado da piscina. Se você se mexer muito a gente pode cair!"

    o "Você que não tem força pra me segurar. E ainda fica colocando a culpa em mim..."

    g "Tadinha dela... ela não quer ficar gorda... que fofinha..."

    o "[g]... tá bom."

    mc envergonhado "[g]... você tá pegando no pé dela mesmo..."

    g "Não. Vocês que não deixaram eu terminar. Eu ia falar que não é ruim a [o] engordar."

    o "Como assim não é ruim?!"

    scene j7_imagem3 with Dissolve(1.0)

    pause

    g "Você tem a vantagem de acumular gordura nos lugares certos..."

    o "Q-quê?!"

    g "Você tem uma cinturinha... mas olha pra esse bundão... que delícia de raba que você tem."

    o "[g]! Para de falar assim!"

    g "Seu peito é tão grande que eu quase nunca reparo que você tem um bundão delicioso desses..."

    o "Chega! Eu vou desc-"

    g "Aposto que o [mc] concorda comigo."

    mc surpreso "E-eu?!"

    g "Você não acha que o corpo da [o] é perfeito? Ela tem cinturinha, e um peitão e um bundão que dá vontade de morder."

    o "[mc]! Não!"

    menu:
        "Ela não tá gostando disso [g]. Chega.":


            $ carol_amizade += 2

            mc serio "Calma aí, [g]. Você não tá vendo que ela não tá curtindo?"

            g "Ela tá sim. Só não quer admitir."

            o "Para de besteira!"

            mc "Você tá ouvindo, [g]?! Respeita sua amiga!"
        "Vocês duas são muito bonitas.":


            mc charmoso "Vocês duas deram sorte. O corpo das duas é maravilhoso."

            o "[mc]... não entre na dela... eu não tô nem aí pro meu corpo."

            g "Mentirosa. Ela gostou, [mc]. Eu tô vendo que ela deu uma risadinha!"

            o "Não! Para, [g]!"
        "Ela tem um corpão mesmo.":


            $ carol_amizade += 1

            mc safado "Com certeza. A [o] tem um corpo maravilhoso."

            o "[mc]! Não entra nada dela por favor!"

            mc "Mas é sério. Eu falo com todo o respeito, viu, [o]. Você é gata mesmo."

            g "Tá vendo? Pena que ele não pode pegar em você igual eu tô fazendo, né?"

            mc envergonhado "..."

            g "Não vejo a hora de você colocar o biquíni pra eu dar uma lambida nessa bunda gorda."

            o "[g]! Você tá passando dos limites!"

    g "Tá... vou colocar você no chão..."

    o "Acho bom. Eu já tava escorregando."

    g "Eu nunca ia deixar minha princesa se machucar."

    o "[g]... eu tô escorregando."

    g "Tudo bem. {w} Eu já tô colocan-"

    o "[g]! Cuidado!"

    g "C-car-"

    mc surpreso "Cuidado vocês du-"

    scene j7_imagem4 with vpunch

    pause

    o "[g]!"

    g "S-socorro!"

    mc angustiado "Cuidado!"

    g "Eu disse que você era gorda dem-"

    scene black with vpunch

    "{i}SPLAAASH{/i}"

    mc "Vocês tão bem?!"

    o "[g]! Minha roupa tá toda transparente!"

    g "E por que você tá sem sutiã?!"

    mc surpreso "!"

    o "S-sai daqui, [mc]!"

    mc angustiado "T-tô saindo!"

    g "HAHAHA!"

    scene resort_geral with Dissolve(1.0)

    "Essas duas..."

    "Se eu ficar atrás delas eu não vou curtir nada."

    "Tem uns lugares pra deitar ali. É pra lá que eu vou."

    scene j7_imagem5 with Dissolve(1.0)

    pause

    mc "Aahh... agora sim..."

    "Desde que eu comecei essa vida de paparazzo eu quase não tive tempo pra curtir..."

    "É problema atrás de problemas... no trabalho, com os amigos, no amor..."

    "Acho que a [o] vai manter a [g] ocupada por um tempo... e eu posso só curtir um dia sem fazer nada."

    "Pensando bem... a [g] parece que tá fissurada na [o]. Ela nem falou nada comigo..."

    if julia_namoro:

        "Nem parece que a gente tá namorando..."

        "Quem que ignora o namorado assim pra ficar pegando na amiga? Que doideira..."

    "Será que a [g]... enjoou de mim? Eu sinto que a gente era bem mais próximo antes..."

    "Quer saber, não vou pensar nisso demais."

    "O céu tá lindo, o sol não tá tão forte... eu vou pedir uma bebida do caralho e só curtir..."

    "Eu ralei muito esses tempos. Eu mereço um descanso."

    mc "Aahhh... isso que é aproveitar a vi-"

    "???" "Oi."

    "Brincadeira..."

    scene j7_imagem6 with Dissolve(1.0)

    pause

    o "Tava dormindo? Desculpa incomodar..."

    menu:
        "Eu tava curtindo um pouco só.":


            mc "Nada. Eu só tava curtindo um pouco aqui. O sol tá bom e eu tô precisando de um dia de folga."

            o "O lugar é bonito mesmo... mas eu te entendo. Eu te falei que gosto de ficar sozinha, né?"

            mc "Verdade..."

            o "Pode ficar curtindo aí."

            mc "Não precisa ir. Fica à vontade aí."

            o "Verdade? Não queria estragar seu momento."

            mc "Relaxa."
        "Nunca. Eu gosto de conversar contigo.":


            $ carol_amizade += 1

            mc "Não tá incomodando. Eu gosto de conversar com você. Você é bacana, [o]."

            o "Haha... que bom... eu vou ficar quietinha aqui e tentar curtir o sol um pouco também."

            mc "Não é sempre que a gente consegue vir em um lugar desses, ainda mais com umas garotas bonitas."

            mc "Qualquer homem ia querer me bater se soubesse que uma garota igual você quis sentar do meu lado e eu mandei ir embora."

            o "Hmm..."

    o "Então com licença..."

    scene j7_imagem7 with Dissolve(1.0)

    pause

    o "..."

    "A [o] parece meio sem jeito... mas também... olha pra esse biquíni. Por que ela tá usando isso?"

    menu:
        "Dar uma 'boa olhada' no biquíni da [o]":


            "Acho que só uma olhadinha de nada ela não vai ligar."

            scene j7_imagem8 with Dissolve(1.0)

            pause

            "U-u-uou... olha pra isso... a [o] sem dúvida tem um peitão enorme."

            "Eu tenho que concordar com a [g] que ela é gostosa demais. Acho que deve ser o maior peito que eu já vi."

            "E esse biquíni tá mostrando tudo praticamente!"

            "Só mais uma olhadinha de nada..."

            window hide

            pause

            o "...gal?"

            mc desconfiado "Hm?"

            o "[mc]..."

            scene j7_imagem7 with hpunch
        "É melhor não ficar reparando igual um tarado":


            $ carol_amizade += 1

            "Não vou ficar olhando igual um tarado."

            "Se eu reparar daí que ela vai se sentir mais desconfortável ainda. É só eu agir normal... sem olhar... força, [mc]!"

    o "Tudo bem, [mc]?"

    mc surpreso "S-sim!"

    o "Eu tô me sentindo meio exposta nisso aqui."

    mc envergonhado "É... mas tá bonito."

    "Eu não imaginei que a [o] ia usar uma coisa assim."

    o "A [g] trouxe pra mim... e eu nunca ia usar, mas eu molhei a roupa... então..."

    "Ah... agora faz mais sentido."

    mc "Molhou não, né? Ensopou tudo."

    o "A [g] é impossível... você viu o que ela fez? E ainda ficou passando a mão na minha..."

    mc "Bunda?"

    scene j7_imagem9 with Dissolve(1.0)

    o "Pois é! E o jeito que ela tava falando... nossa, me tirou do sério."

    mc envergonhado "A [g] é assim, né? E parece que ela gosta bastante de você."

    o "Sei lá o que tá acontecendo. A [g] sempre foi meio ligada em mim, mas ultimamente tá demais."

    o "Ela fica falando como eu tô bonita, como eu sou... nem acredito que eu vou falar isso... 'gostosa'."

    mc "..."

    o "Ela fica pegando em mim, me apertando. Até na faculdade ela me joga na parede às vezes e fica passando a mão em mim."

    "N-não acredito que [g] faz isso... {w}Bom, acho que eu acredito, sim."

    o "Eu queria saber o que aconteceu com ela pra ela ficar desse jeito."

    if not julia_e6 == "biblioteca":

        o "O que aconteceu com vocês naquele passeio, hein?"

        mc desconfiado "No passeio? Aquele dia na casa do idiota..."

        if j6_final_mari:

            "O pior é que eu nem sei porque eu tava com a [mari]..."

        elif julia_e6 == "bom":

            "Naquele dia o [caio] deu em cima dela e ela não deu bola pra ele. Será que foi isso?"

            "O [caio] ficou putasso com aquilo. Ele não devia tá acostumado com a [g] negando ele daquele jeito."

            mc desculpa "Eu não tenho certeza, [o]... mas eu acho que a [g] tá se emendando."

            o "Você acha?"
    else:


        $ carol_amizade += 5

        o "Aquele dia a gente estudou... ela até deixou de ir naquela farra na casa do babaca, né?"

        mc normal "Pois é..."

        mc desculpa "Eu não tenho certeza, [o]... mas eu acho que a [g] tá se emendando."

        o "Você acha?"

    mc normal "Eu acho que a [g] tá meio que criando coragem pra ser ela de verdade."

    o "Hmmm..."

    mc "Querendo ou não aquela turma foi o porto seguro dela por um bom tempo."

    o "Aquelas pessoas são terríveis, [mc]. Elas fazem muito mal pra Ju."

    mc "Eu sei, mas elas foram amigos dela por um tempão."

    if j6_historia:

        mc desculpa "A [g] me contou a história dela com o [caio]. Ele foi muito importante pra ela."

        o "É duro ouvir isso... aquele escroto..."

    mc "A gente precisa dar um tempo pra ela, sabe?"

    scene j7_imagem10 with Dissolve(1.0)

    pause

    o "Se é o que você acha... talvez seja melhor mesmo eu ter paciência com a [g]."

    o "Esse negócio dela ficar pegando em mim... me chavecando... me deixa um pouco com vergonha, mas acho que eu aguento."

    mc zerado "Sem comentários essa mina..."

    o "Mas eu tô impressionada com seu jeito. Não achei que você ia levar isso de boa assim."

    if julia_namoro:

        o "Vocês tão namorando, né? A [g] me falou. Daí fiquei com medo de falar disso com você."

        mc charmoso "Sim. A gente tá. Mas a [g] é assim, né? Eu sei que no fundo não é sério."
    else:


        o "Eu pensei que você gostasse dela. Ela tá sempre falando de você e vocês tão sempre juntos agora."

        mc normal "A gente não tem nada sério. É só amizade mesmo."

        mc envergonhado "Se bem que a [g] já se atirou bastante pra cima de mim..."

        o "Ah. Isso eu imaginei."

    mc zerado "Além de que ter ciúmes da [g] é pedir pra sofrer..."

    o "Você é um homem maduro, [mc]. É muito positivo trocar ideia com pessoas assim."

    o "A maioria das pessoas que eu conheço fica no mesmo papo de sempre. A mesma ladainha, sabe?"

    o "Agora, quando a gente passa um tempo com alguém que fala de sentimentos, que entende melhor as pessoas... dá até uma alegria."

    menu:
        "A maioria das pessoas são rasas demais.":


            mc desculpa "O que acontece é que a maioria das pessoas é fútil. Elas não têm tempo pra pensar nas coisas."

            mc "E se a pessoa não pensa, ela não tem sobre o que falar. Ela vai falar o de sempre. Que é aquela coisa básica."

            o "É... a maioria é assim infelizmente. Mas eu não sinto assim quando eu tô falando com você."

            mc "Valeu, [o]."
        "Eu também tô adorando falar com você.":


            $ carol_amizade += 1

            mc charmoso "Eu tô adorando falar com você também. Eu acho que... sei lá... é até meio natural quando eu converso com você."

            o "Você acha?"

            mc "É. Não é cansativo. Eu só falo o que eu penso e parece que você vai entender, sabe?"

            o "Que bom... eu sinto a mesma coisa com você, [mc]. E nem sei a última vez que eu me senti bem assim com alguém."

    mc normal "Por que você não deita um pouco igual eu e relaxa também?"

    o "Acho que eu fiquei tempo demais no sol... tô com medo, porque eu sou meio branca demais..."

    mc "Quer que eu passe protetor em você? Têm vários espalhados pelas mesas aí."

    o "Hmm... n-não tem problema?"

    mc charmoso "Claro que não. Deita aí que eu passo."

    o "Tá. Obrigada."

    scene j7_imagem11 with Dissolve(1.0)

    pause

    o "E desculpa por esse biquíni... nem sei onde a [g] conseguiu isso. A alça é grande de propósito, só pra ficar caindo..."

    mc "Tá tudo certo."

    o "Até nisso ela quer se aproveitar de mim..."

    mc "Falando nisso, cadê ela?"

    o "Ela disse que ia pegar um biquíni novo pra ela aqui no resort. Tava incluso no presente dela um novo."

    mc "Caraca, que presentão..."

    o "A gente tem que aproveitar que a gente tá sozinhos pra aproveitar um pouquinho."

    o "Q-quero dizer! Isso pareceu meio te chamando pra alguma coisa mais íntima! N-não era isso!"

    menu:
        "Se você quiser algo mais íntimo eu topo.":


            $ carol_amizade += 1

            mc charmoso "Se você tiver afim de uma coisa mais íntima eu topo."

            o "[mc]... {w}Você t-tá passando tempo demais com a [g]..."

            mc "Sem compromisso. Só me colocando a disposição aqui."

            o "Se você continuar falando assim eu vou acreditar."

            if julia_namoro:

                o "E eu vou falar pra [g] que o namorado dela tá dando em cima de mim?"

                mc "Brincadeira, né, [o]?"

                o "Ah tá."
            else:


                mc "Igual eu falei. Sem compromisso. Deixa a ideia no ar."

                o "Hmm..."
        "Eu entendi. Tá tudo certo.":


            mc "Eu entendi... não precisa ficar tão preocupada."

            o "Ufa... obrigada."

    if mc_massagem > 2:

        "Eu tô fazendo aulas de massagem com a [m]. Eu podia ofecer pra [o]... ou será que é demais? A gente nem se conhece tanto..."

        menu:
            "Vou oferecer. Quem não chora não mama":


                $ carol_amizade += 2

                mc "Ah, eu tô fazendo aulas de massagem. Tudo bem pra você se eu passar enquanto faço uma massagem?"

                o "Massagem... nossa... agora eu fiquei impressionada. Por mim tudo bem, se for de graça, né?"

                mc "Posso fazer de graça pra você, sim. Se você gostar, a próxima é o dobro do preço."

                o "Vamos ver..."

                scene j7_imagem12 with Dissolve(1.0)

                pause

                o "Não achei que esse passeio fosse acabar sendo tão bom..."

                mc "Tava com medo da [g]?"

                o "Tirando que ela me tacou na água e eu ainda não sei se ela vai aprontar... mas tá bom, pelo menos agora..."

                mc "..."

                o "Hmmm... você realmente tá fazendo um bom trabalho aí atrás."

                mc "Que bom. Eu não sou um mestre, mas as aulas tão fazendo efeito."

                mc "E você tá um pouco tensa aqui nos ombros."

                o "Devem ser as provas... eu não sei se eu fui tão bem."

                mc "Mas sua pele é muito boa. Ela é lisinha e é gostosa de pegar, super macia."

                o "O-obrigada."
            "Melhor agora não. Talvez uma próxima":


                "Deixa quieto."

                mc "Vou passar então. Licença."

                scene j7_imagem12 with Dissolve(1.0)

                pause

                o "Não achei que esse passeio fosse acabar sendo tão bom..."

                mc "Tava com medo da [g]?"

                o "Tirando que ela me tacou na água e eu ainda não sei se ela vai aprontar... mas tá bom, pelo menos agora..."

                mc "Que bom."
    else:


        "Se eu soubesse fazer massagem... talvez desse pra eu oferecer pra ela..."

        mc "Vou passar então. Licença."

        scene j7_imagem12 with Dissolve(1.0)

        pause

        o "Não achei que esse passeio fosse acabar sendo tão bom..."

        mc "Tava com medo da [g]?"

        o "Tirando que ela me tacou na água e eu ainda não sei se ela vai aprontar... mas tá bom, pelo menos agora..."

        mc "Que bom."

    window hide

    pause

    mc "No que você quer trabalhar, [o]?"

    o "Hoje eu tô trabalhando na biblioteca. É só um estágio, daí eles pagam pouquinho, mas eu gosto."

    mc "Sei... mas e depois que você se formar?"

    o "Ah... eu quero continuar estudando. Eu quero fazer pós-graduação, depois mestrado e doutorado."

    mc "Orra."

    o "Eu pretendo trabalhar no ensino superior. Quero ser professora e pesquisadora de alguma universidade."

    mc "Muito bacana. Boa sorte."

    o "Isso não é sorte não..."

    scene j7_imagem13 with Dissolve(1.0)

    pause

    o "... a gente precisa estudar muito. Conhecer a linha de pesquisa dos professores, ler muito, escrever muito..."

    g "{size=25}Xiiii....{/size}"

    mc "{size=25}O que você quer?{/size}"

    g "{size=25}Só continua...{/size}"

    if julia_namoro:

        "Que que a [g] tá querendo aqui agora? Só falta ela tá com ciúmes de mim e da [o]."
    else:


        "Que que a [g] tá querendo aqui agora. A [o] tá relaxando... eu tô passando creme nela há um tempão e ela tá curtindo..."

    "Certeza que ela vai aprontar alguma coisa. Será que é melhor eu avisar a [o]?"

    "Ou será que é melhor ver o que a [g] quer aprontar? Dá pra imaginar o que ela quer fazer..."

    menu:
        "Vou ficar quieto":


            "Tomara que a [o] não fique brava comigo... pelo menos não muito."

            mc "Passei em tudo [o]."

            o "Foi muito bom, [mc]. Obrigada de verdade. Agora acho que eu vou tirar um cochilo..."

            o "Hmmm... aproveitar antes que a [g] venha... e comece a baderna..."

            o "..."

            g "{size=25}Agora deixa comigo.{/size}"

            mc "{size=25}Não apronte demais com ela.{/size}"

            scene j7_imagem14 with Dissolve(1.0)

            pause

            g "{size=25}Certeza que ela vai adorar...{/size}"

            g "{size=25}A [o] fica de frescura, mas eu sei que ela gosta quando eu faço essas coisas com ela.{/size}"

            mc "{size=25}Tem certeza? Você já derrubou ela na água hoje.{/size}"

            g "{size=25}Eu sei, mas foi sem querer. E valeu a pena. Ela gostou, vai por mim.{/size}"

            mc "{size=25}Eu acho que é você que gosta disso, não ela.{/size}"

            g "{size=25}A [o] é muito frígida, entende?{/size}"

            mc "{size=25}Que merda isso quer dizer?{/size}"

            g "{size=25}Ela é sozinha. Ninguém dá em cima dela, ela não dá em cima de ninguém. Ela vai ficar pra tia assim.{/size}"

            mc "{size=25}E daí? E se ela tá feliz desse jeito?{/size}"

            g "{size=25}Ela é virgem. Ninguém na faculdade é virgem. Isso é um absurdo.{/size}"

            mc "{size=25}Você tá exagerando, [g]. É só o jeito dela. Não tem nada de mais nisso.{/size}"

            g "{size=25}Você vai ver o que eu tô falando...{/size}"

            g "Oi, minha linda..."

            o "Hm?"

            g "Oiee!"

            scene j7_imagem15 with hpunch

            pause

            o "[g]! O q-que você tá fazendo?!"

            g "Tava dormindo tão linda."

            o "[g]! Sai de cima! O-onde você tá com essa mão?!"

            g "Por que o [mc] pode pegar em você e eu não!?"

            o "Ele tava só passando protetor nas minhas costas!"

            g "Sei! Ficou cinco minutos passando, né?!"

            o "Sei lá! E ele não tava pegando na minha bunda e no meu peito!"

            g "Ele que é bobo. Não sabe o que tá perdendo."

            o "Dá licença. Eu vou sentar."

            scene j7_imagem16 with Dissolve(1.0)

            pause

            o "Posso saber o que você tá fazendo aí ainda?"

            g "Não quer que eu passe protetor na parte da frente?"

            o "Não. Obrigada."

            "Mano... a [g] é muito carente com a [o]. Normalmente ela é tão 'foda-se' com as pessoas. Nem parece ela grudenta desse jeito."

            g "Quer que eu chame o [mc] pra passar no seus peitos também?"

            mc envergonhado "[g]..."

            o "O [mc] só fez um favor pra mim."

            if julia_namoro:

                o "Eu sei que ele é seu namorado."

                g "Não é esse o problema, Carolzinha."

            g "Não tem nada a ver com ele. Eu só quero que você admita que você gosta quando eu dou em cima de você."

            o "..."

            g "Não vai falar nada?"

            scene j7_imagem17 with Dissolve(1.0)

            pause

            o "O que é isso agora, [g]?"

            g "..."

            o "Você tá passando a mão nos meus..."

            g "..."

            o "Tira a mão daí..."

            g "Não..."

            o "[g]..."

            g "Seus peitos são tão gostosos, [o]... eles são grandes... macios... é tão bom pegar neles."

            o "..."

            g "E é tão gostoso seu cheiro... eu adoro tanto..."

            scene j7_imagem18 with Dissolve(1.0)

            pause

            o "Ah... p-para..."

            "O q-que tá acontecendo aqui?"

            g "..."

            o "Você tá apertando, Ju! Ai..."

            g "Fala logo que você adora quando eu pego em você assim..."

            o "Não! Ai!"

            g "Que delícia apertar esse peitão! Sua gostosa."

            o "Ah! Sua resp-piração."

            g "[o]..."

            o "N-não! Sai!"

            scene black with hpunch

            mc surpreso "!"

            scene j7_imagem19 with Dissolve(1.0)

            o "Que porra foi essa, [g]?! O que você tava pensando?!"

            g "Foi ou não foi bom?"

            o "Cala a boca!"
        "Melhor eu avisar a [o]":


            $ carol_amizade += 3

            "Não vou deixar a [g] causar com a [o], coitada."

            mc "{size=25}Não. Ela tá descansando agora. Deixa ela!{/size}"

            g "{size=25}Para de ser puxa-saco, [mc]! Rapidinho!{/size}"

            mc "[o]..."

            o "Hm? Hmm!? Que que aconteceu?"

            mc "Nada. Você tava quase dormindo e a [g] tá aqui do lado querendo causar contigo."

            o "[g]? Você tá aí? O que que foi dessa fez?"

            g "Nada..."

            o "Pode vir sentar aqui. Valeu, [mc]."

            mc "Opa..."

            g "Seu ridículo."

            o "E você vem aqui. Deixa eu te falar um negócio que eu já tô cansada."

            scene j7_imagem19 with Dissolve(1.0)

    g "Calma... era só uma brincadeira."

    o "Eu tô cansada das suas brincadeiras, [g]! Eu tava falando isso com o [mc]! Agora chega!"

    o "Eu não sei que merda você tá passando, mas chega de ficar em cima de mim desse jeito! Eu não quero!"

    g "Você continua falando isso? Você não vê que você quer?! Eu sei que você quer!"

    o "Isso é um absurdo, [g]. Da onde você tirou isso? Me fala uma vez que eu falei pra você que eu gostava disso?"

    g "Você nunca falou, mas eu sei que você quer. Eu vejo no seu jeito."

    o "Óbvio que não! Você fica toda hora grudada em mim, me alisando, me apertando. Eu já falei que eu não quero isso."

    o "Quando uma pessoa fala não, quer dizer NÃO. E, poxa, eu esperava que você fosse ser legal comigo."

    scene j7_imagem20 with Dissolve(1.0)

    pause

    g "Eu só faço isso porque eu gosto de você, [o]."

    o "Se você gostasse de mim de verdade, você ia me respeitar. Respeitar meu espaço."

    g "M-mas... e se eu tiver perdendo a oportunidade porque eu tô sendo bundona? A gente tem que ter pulso na hora da conquista."

    o "Eu não sei de conquista, mas eu sei que eu não quero você fazendo mais isso. Me respeita."

    scene j7_imagem21 with Dissolve(1.0)

    pause

    mc "O que aconteceu com você, [g]? Quem te viu, quem te vê, hein? Sofrendo de amor por alguém assim."

    g "Que que você sabe de qualquer coisa?!"

    menu:
        "A [o] tá certa. Você tem que respeitar ela.":


            $ carol_amizade += 2

            mc "A [o] tem toda razão, Ju. Não importa o que VOCÊ acha. Se ela não quer, você não pode fazer isso."

            mc "Isso é assédio ou bullying ou no mínimo você sendo uma baita inconveniente. Ela é sua amiga, caralho."

            g "Não é porque você é bundão que eu vou ser também."

            o "O [mc] não é bundão. Ele é muito gente boa."

            g "Esse é só outro jeito de falar bundão."

            o "Não! S-se eu fosse namorar com alguém... e-eu namoraria com ele e não com você!"

            scene j7_imagem20 with Dissolve(1.0)

            g "Quê?!"

            o "N-não com ele! Mas com alguém do jeito dele ao invés de alguém com o seu jeito! Isso que eu quis dizer."

            g "Não acredito que eu tô ouvindo isso!"

            mc "Ela que falou, não fui eu."
        "Por que todo esse interesse nela? E eu?":


            mc "O que aconteceu que você tá em cima dela desse jeito?"

            if julia_namoro:

                mc "Eu sou seu namorado e você fica fazendo graça desse jeito na minha frente?"
            else:


                mc "Eu pensei que eu fosse seu melhor amigo e você fica de papelão com ela aí?"

            g "Eu sei... mas..."

            o "Ele tem razão, [g]. Eu não vi você falando nada com o [mc] ainda desde que a gente chegou aqui."

            o "Você fez graça comigo, me jogou na piscina, foi comprar suas coisas e agora fica em cima de mim de novo."

            o "Por que você chamou ele então?"

            g "..."

    scene j7_imagem22 with Dissolve(1.0)

    pause

    o "Agora eu vou dar uma volta e eu não quero que você venha atrás de mim."

    g "N-nã-"

    o "Eu vim aqui pra me divertir. Aliás, eu só vim aqui porque o [mc] me chamou e disse que ia ser importante pra você."

    o "Só que você me irritou e agora eu quero um tempo sozinha. Quero aproveitar pelo menos um pouco disso aqui."

    g "M-mas, [o], eu só quis vir aqui por sua causa!"

    o "Azar o seu. Aproveita pra pensar um pouco na sua vida, [g]."

    o "Não esquece que não é só o que você quer. As pessoas têm as vontades delas também. Acho bom você entender isso."

    mc "E eu vou tomar um sol também. Aproveita bem, [o]."

    o "Obrigad[o]. E toma cuidado com essa aí."

    g "Vocês dois tão de duplinha. Que merda... Não vou falar mais com você hoje também!"

    scene black with Dissolve(1.0)

    mc "[g]..."

    scene j7_imagem5 with Dissolve(1.0)

    "Caralho... a [g] saiu putassa. A [o] também tá mó irritada. As coisas deram errado bem rápido."

    "Sinceramente, não sei o que deu na [g]. Ela parece uma doida atrás da [o]. Parece que tem 12 anos."

    if not julia_seducao < 9:

        "Se ela tá com esse fogo, ela podia vir atrás de mim. Eu apagava esse fogo dela na hora."

    "Mas não sei se eu posso ajudar com isso... eu acabei falando aquelas coisas legais dela, mas sei lá."

    "E a [o] tá certa, mano. A [g] não poder fazer o que bem entender."

    "Ver as duas de biquíni não é o pior dos mundos, mas esse passeio podia ter sido melhor..."

    scene black with Dissolve(1.0)

    "..."

    scene j7_imagem23 with Dissolve(1.0)

    pause

    "Caraca, acho que eu cochilei... o sol já tá quase indo embora."

    mc desconfiado "Hm? A [g] tá sozinha ali na ponte."

    "Quem sabe não é nossa chance de conversar um pouquinho antes de ir embora?"

    scene black with dissolve

    scene j7_imagem24 with Dissolve(1.0)

    pause

    mc "E aí? Tá pensando na vida?"

    g "Sei lá..."

    mc "As coisas não saíram como você planejava, né?"

    g "Ah... cala a boca..."

    menu:
        "Você que causou isso.":


            mc "Você não pode reclamar muito. Você que causou isso sendo grudenta demais."

            g "Cara, se for pra me dar lição de moral, pode ir curtir em outro lugar."

            mc "Não adianta descontar em mim. Eu fiz o que você pediu. Ela tá aqui porque eu falei com ela."

            mc "Quem fodeu tudo foi você mesmo."

            g "..."
        "Tomou um fora da [o]. Faz parte.":


            mc "É duro tomar um fora, né? Faz parte da vida."

            g "Que que você sabe disso?"

            if julia_namoro:

                mc "Eu sei que eu vim pra um resort com a minha mina e ela nem deu bola pra mim. É tipo tomar um fora."
            else:


                mc "Eu corro muito aqui nessa cidade. Já passei por coisa muito pior que isso aí."

            g "..."

    mc "Não vai retrucar?"

    g "Me deixa..."

    mc "Que foi? Por que você tá assim, hein? Não confia mais em mim agora?"

    g "Por que eu ia te falar? Você tá contra mim."

    mc "Que 'contra', [g]? Eu sempre quis te ajudar."

    if j4_salvou:

        mc "Você não lembra quando eu te tirei daquela mesa de bilhar na festa?"

        mc "Os caras iam fazer o que queriam com você lá."
    else:


        mc "Eu sei que eu deixei você naquela mesa de bilhar na festa aquela vez, mas eu não consegui."

        mc "Não é por isso que eu quero ver você se ferrando. Eu briquei com o [caio] por sua causa."

    g "Eu sei... no fundo eu sei que você, a [o] e a mana querem que eu seja feliz..."

    mc "Claro."

    g "Às vezes o [caio], a [mari] e o [teo] são filhos da puta, mas parece que é mais fácil viver com eles."

    mc "Então é isso? Você prefere eles do que a gente? É por isso que você tá assim?"

    scene j7_imagem25 with Dissolve(1.0)

    pause

    g "Para de ser idiota, [mc]... não é nada disso."

    mc "Então o que tá acontecendo? Por que parece que você tá afastando eu e a [o]?"

    g "Como assim?"

    if not julia_e6 == "biblioteca":

        mc "Naquele passeio na casa do [caio], você ficou o tempo todo longe de mim praticamente."

        mc "Você podia ter estudado comigo e a [o] na biblioteca, mas você quis sair com eles."

        mc "E eu que fui lá com você, quase nem te vi."

    mc "Hoje você podia ter passado um tempo comigo e com a [o] e você fodeu tudo."

    mc "Nem deu bola pra mim. E a [o] que veio aqui por sua causa ficou putassa, e com razão, depois da sua palhaçada."

    if julia_namoro:

        mc "Eu pensei que você quisesse namorar comigo. Mas a gente nem parece que tá namorando."

    g "Eu não queria... não era isso que eu queria, [mc]."

    g "Tem muita coisa ruim na minha cabeça agora. É que... Eu acho que eu tô com medo do que vai acontecer."

    mc "Eu acho que você é uma das garotas que eu conheço que mais entende seus sentimentos."

    mc "Uma pessoa que olha pra você pode achar que você é infantil, mas eu acho que você tem noção do que tá rolando."

    mc "Você faz o que você quer. Você gosta de pagar pra ver. Mas você não é boba."

    g "Você... pode me segurar?"

    mc "Hm? Se eu posso ser seu amigo agora? Você tá falando de aguentar seus sentimentos?"

    g "Upa."

    scene j7_imagem26 with Dissolve(1.0)

    pause

    mc "Ah... você tava falando no sentido literal..."

    g "Olha... eu sou meio fodida, [mc]."

    mc "C-como?"

    g "Toda vez que uma coisa boa acontece comigo, eu acabo ferrando ela."

    g "Eu estraguei o que eu tinha com meus amigos de antes, com meus pais. Eu tô toda hora testando a paciência da mana..."

    g "Uma hora ela vai enjoar desse meu jeito. Eu tenho certeza."

    g "E você, a [o], logo logo vocês vão se cansar de mim também. Por isso que não adianta isso, sabe?"

    g "Aquela turma é a única que me aguentou. Porquele eles também são fodidos igual eu."

    g "E agora eu vou parar de falar com eles... e daí uma hora vocês vão me deixar e eu vou ficar sozinha de novo."

    g "Acho que é por isso que eu tô tão ansiosa esses dias. É por isso que eu tô meio longe de você. Eu não quero que você enjoe de mim."

    menu:
        "Ninguém vai abandonar você.":


            mc "[g], ninguém vai abandonar você ou enjoar de você."

            mc "Você é uma garota divertida, é cheia de energia. Você é muito cativante e é bem verdadeira."
        "Se você continuar assim, daí que você vai perder a gente.":


            mc "O que vai acontecer é que esse jeito que você tá usando pra resolver a situação vai ser a causa da desgraça."

            mc "Se você continuar assim, daí sim que você vai ficar sozinha."

    mc "Você tem suas coisas coisas que não são legais? Qualquer pessoa tem. Não quer dizer que vão abandonar a gente por causa disso."

    mc "Brigar de vez em quando faz parte. A gente se cansar um pouco do outro também, mas depois volta. Isso tudo acontece."

    mc "O que não dá é você ficar forçando uma coisa igual você fez com a [o] hoje. Ou se afastar de mim com medo de eu enjoar de você."

    mc "Você tá deixando seus medos comandarem. E isso vai acabar causando o que você tem tanto medo."

    g "E você tá se achando o psicólogo."

    mc "E-eu não... só tô falando o que eu acho..."

    scene j7_imagem27 with Dissolve(1.0)

    pause

    g "Então me fala uma coisa..."

    mc "Q-q-quê?"

    g "Se você não vai me abandonar mesmo... eu quero uma prova."

    mc "Q-que prova?"

    g "Eu e a [o] somos completamente diferentes. Eu quero que você olhe nos meus olhos e fale quem você prefere."

    mc "Eu?"

    g "Você, [mc]. Fala se você prefere eu ou a [o]. Mas eu quero que você fale a verdade."

    if julia_namoro:

        g "Esquece que a gente tá namorando."

    g "Faz de conta que nós duas queremos ficar com você. Fala com quem você ia querer ficar."

    g "Se você for sincero comigo, eu não vou ficar chateada com você."

    mc "[g]..."

    "Que tipo de pergunta é essa."

    if julia_namoro:

        "Ela é minha namorada. Como eu posso falar que prefiro outra garota?"
    else:


        "A gente é só amigos, mas mesmo assim... se bem que... talvez essa seja minha chance de ficar com ela."

    "O que eu responder aqui provavelmente vai mudar completamente o final desse passeio."

    menu:
        "Eu prefiro você.":


            $ julia_e8 = "julia"

            mc "Claro que eu prefiro você."

            g "De verdade?"

            mc "Óbvio. Você é a garota mais sexy, mais linda, mais divertida e interessante que eu conheci na minha vida."

            mc "Nunca perderia a chance de ficar com voc-"

            label julia_e7_beijo:

                pass

            scene j7_imagem28 with hpunch

            pause

            "Uou!"

            "A [g] beija muito bem. Essa língua maluca dela é uma delícia."

            g "Só me beija muito, [mc]."

            g "Vem, me aperta. Deixa eu sentir você coladinho no meio das minhas pernas."

            g "Se você me beijar gostoso, eu prometo que eu deixo você me comer quanto tempo você quiser depois."

            if praia_julia_local:

                mc "Igual no nosso passeio da praia?"

                g "Melhor ainda."

            mc "Então vem aqui."

            window hide

            pause

            scene black with dissolve

            scene j7_imagem29 with Dissolve(2.0)

            pause

            "Então a [g] tava preocupada com isso... que boba..."

            "Eu acho que a solidão faz esse tipo de coisa com as pessoas."

            "Eu quero que a [g] saiba o quanto eu gosto dela. E que eu não vou sair do lado dela nunca."

            "Mesmo nessa vida maluca de paparazzo, eu tenho que agradecer por ter pessoas incríveis do meu lado."

            "Depois eu vou mandar uma mensagem pra todas as pessoas incríveis que eu conheci nesses meses."

            "E tomara que aquelas pessoas que estejam sozinhas, saibam que um dia elas vão encontrar alguém especial também."

            "Igual eu encontrei a [g]."

            scene black with Dissolve(3.0)

            o "O que os dois tão fazendo aí? Vocês podem desgrudar um pouco a boca pra gente ir?"

            g "Só mais um segundinho, encalhada!"

            o "Absurdo..."

            jump julia_e7_final
        "Eu prefiro a [o].":


            $ julia_e8 = "carol"

            if julia_namoro:

                mc "Você tá falando pra eu esquecer que a gente é namorado, hein? Porque isso muda tudo."

                g "..."
            else:


                mc "A gente é só amigos, então não importa quem eu escolher. Não muda que a gente é amigos."

            mc "Eu prefiro uma garota igual a [o]."

            g "Sabia."

            mc "Mas isso não muda nada. E eu nem conheço ela direito. Eu tô falando por cima, comparando as diferenças entre vocês."

            g "Não precisa tentar explicar. É óbvio."

            g "Qualquer pessoa vai preferir uma garota meiga, inocente, gente fina e ainda com um corpão daqueles igual o da [o]."

            mc "As pessoas são diferentes. Eu tenho certeza que muita gente ia preferir seu jeito divertido e cheio de energia."

            mc "Além de que você é super sexy e é super gata."

            if julia_namoro:

                mc "Eu escolhi você como minha namorada, não ela. E não é porque eu não conhecia ela. Eu já conhecia."

                mc "Mas você sempre foi incrível pra mim. Eu não trocaria você pela [o] de jeito nenhum."

                g "Se você diz... mas eu não ligo, de verdade. {w}Só que eu tenho uma proposta pra você."

                mc "Proposta? Que tipo?"

                g "Eu quero que você faça a minha com a [o]. Eu quero que você fale pra ela que ela devia ficar comigo."

                mc "Como é?!"

                g "Se você fizer essa pra mim, eu deixo você ficar com ela também. Se ela quiser, claro."

                mc "Nós dois vamos ficar com ela?"

                g "É. Se você não se importar, claro."

                menu:
                    "Melhor não. Eu quero você só pra mim.":


                        mc "Melhor não, Ju. Você é minha e eu não quero dividir você, nem com a [o]."

                        g "Mesmo se você comer ela também?"

                        mc "Mesmo assim."

                        g "Não acredito como você é romântico. Vem logo aqui."

                        jump julia_e7_beijo
                    "Tô dentro. Eu vou falar de você pra ela.":


                        $ j7_carol = True

                        mc "Se você topa, é um pouco estranho pra mim, mas tô dentro."

                        g "Uou... não achei que você fosse topar."

                        jump julia_e7_explica
            else:


                $ j7_carol = True

                g "Você é legal demais pra só admitir que ficaria com ela ao invés de mim."

                mc "Tô sendo sincerão, de verdade."

                g "Tá bom..."

                mc "Mas se eu puder só falar uma coisa."

                g "Que foi?"

                mc "Por mais doidinha e estranha que você seja, eu vou tá sempre aqui com você. Por isso, não vai me excluir das coisas."

                g "Afe... tá bom."

                mc "Agora eu vou dar uma andada por aí, tá?"

                g "Vai lá."

                scene black with dissolve

                jump julia_e7_carol

        "Eu não prefiro nem uma nem outra." if not julia_namoro:

            $ julia_e8 = "nenhuma"

            mc "Minha praia não é nem você e nem ela pra falar a verdade."

            g "Afe, [mc]... você realmente é um cara único. São duas gatas pra escolher e você não quer nenhuma?"

            mc "É, ué. Já que é pra escolher, eu recuso as duas haha..."

            g "Se você tiver se fazendo de difícil eu te dou um tapa."

            mc "Nada disso. É sério."

            g "Caralho... essa eu não esperava mesmo. Mas você me deu uma ideia."

            mc "Hm? Que foi?"

            g "Eu quero que você faça a minha com a [o]. Eu quero que você fale pra ela que ela devia ficar comigo."

            mc "Sério? Você quer ficar com ela?"

            g "Quero. Será que você pode fazer essa pra mim?"

            "A [g] e a [o] se pegando?"

            label julia_e7_explica:

                pass

            mc "Se você realmente quer, então bora. Vou tentar, mas não dá pra garantir."

            g "Combinado. Eu vi ela indo pra praia."

            mc "Beleza. Eu vou pra lá."

            scene black with dissolve

    label julia_e7_carol:

        "..."

    "Ah. Ela tá ali."

    mc normal "Oi, [o]."

    scene j7_imagem30 with Dissolve(1.0)

    pause

    o "[mc]... cansei... já estamos indo?"

    mc "Acho que daqui a pouco. O que você tava fazendo?"

    o "Tava aproveitando um pouco pra espairecer. A [g] me irritou."

    mc "Tô ligado. Às vezes ela exagera, né?"

    o "Pois é... eu sei que é o jeito dela, mas cada coisa que ela faz. Eu cansei."

    mc "Foda..."

    o "Eu sei que a gente tinha acabado de conversar sobre ter paciência com ela, mas eu não aguentei."

    mc "Relaxa. Ela não é criança. Ela vai ficar legal. Eu já conversei com ela também."

    o "Que bom... mesmo irritada eu ainda gosto da Ju, sabe? Ela é uma pessoa boa."

    mc "Verdade. Eu tenho certeza que vocês vão se aceitar."

    o "Você tem sido muito legal comigo, [mc]. Obrigada."

    mc "Que nada. A gente só tá conversando."

    o "Vou ser sincera com você. Faz tempo que eu não falava... com um rapaz... tanto tempo assim."

    if j7_carol:

        mc "Verdade? E como eu me saí?"

        "Dependendo do que ela responder agora, é a hora de dar o bote."

        mc "Eu seria o cara certo pra você?"

        scene j7_imagem31 with Dissolve(1.0)

        if carol_amizade >= 12:

            $ j7_carol_beijo = True

            o "Ai, [mc]... Que tipo de pergunta é essa?"

            mc "Eu queria saber se eu faço seu tipo."

            o "Não sei... eu não sou muito ligada nisso. Eu sinto que se eu falo dessas coisas pode parecer outra coisa..."

            mc "Pode parecer o quê? Que você tá dando em cima de mim?"

            o "S-sim... não queria que parecesse esse tipo de coisa..."

            mc "Por que ia parecer isso? Porque você realmente acha que a gente daria certo? É isso que você ia responder?"

            o "Ai... acho que... [mc]... não sei... acho que sim... mas não pense coisa errada de mim, por favor."

            mc "Claro que não... eu também fico muito nervoso com esse tipo de coisa."

            o "Fica?"

            mc "Claro... quem não fica? {w}Mas será que eu posso chegar mais perto?"

            o "Hm?"

            "Ela disse tudo o que eu tinha que saber. É sua chance, [mc]. Não faz cagada agora. O clima tá perfeito."

            mc "Opa."

            scene j7_imagem33 with Dissolve(1.0)

            pause

            o "Que você tá fazendo?"

            mc "Eu... queria falar que... você é meu tipo de garota, [o]."

            o "!"

            mc "Seu jeitinho meigo, mas sério, preocupada com a [g]... e muito inocente nesses assuntos... eu achei super charmoso."

            o "[mc]... por que você tá falando isso?"

            if julia_namoro:

                o "Você namora a [g]... a gente não pode..."

                mc "A [g] não liga pra isso. Ela já disse."

                o "Mas e eu?"

            mc "Dá uma chance pra gente. E depois a gente vê o que faz."

            o "D-dar uma chance? O que você quer dizer?"

            mc "Fica comigo. Deixa eu te beijar."

            o "M-mas assim?"

            mc "Assim. Só fecha os olhos."

            o "Ai..."

            mc "Deixa que eu tomo conta de você agora."

            o "N-nã..."

            menu:
                "Beijar ela":


                    mc "Eu vou tomar as rédeas. Com licença."

                    scene black with dissolve

                    scene j7_new1 with Dissolve(1.0)

                    pause

                    o "Ah... hmm..."

                    "Sabia que ela não ia recusar se eu só beijasse ela."

                    "A Carol com certeza tem problema pra falar 'não'."

                    "Eu sou um otário por abusar disso pra ficar com ela?"

                    mc "Gostou?"

                    o "E-eu..."

                    mc "Não acabou ainda."

                    o "!"

                    scene j7_new2 with Dissolve(1.0)

                    pause

                    o "Nnmmm..."

                    "Parece que ela tá entrando no clima..."

                    "Nem acredito que eu tô pegando a Carol. Aquela mocinha toda recatada..."

                    "Com certeza que impressionei ela hoje."

                    "Até onde será que eu consigo ir com ela?"

                    o "Ah... hmmm..."

                    window hide

                    pause

                    scene j7_new3 with Dissolve(1.0)

                    mc "Gostou, né?"

                    o "Você podia... ter me dado mais tempo."

                    menu:
                        "Você é muito mole.":


                            mc "Você é muito mole, Carol."

                            o "Ah... d-desculpa... m-mas se é uma relação de dois, você precisa me ouvir."

                            mc "Que seja."
                        "Desculpa, não aguentei.":


                            mc "Foi mal, mas você mexe demais comigo. Não aguentei."

                            o "I-isso não justifica nada!"

                    mc "O importante é que você gostou. Eu tô vendo na sua carinha."

                    o "Ah..."

                    "Ela tá até agora com a perna me apertando... tá muito na minha."

                    "Será que eu... posso aproveitar um pouco mais?"

                    "Por ela eu acho que a gente pararia aqui, mas se eu tiver no controle..."

                    label j7_premium1:

                        pass

                    menu:
                        "Forçar ela ir além":


                            if not premium:

                                call mensagem_premium from _call_mensagem_premium_27

                                jump j7_premium1

                            mc "Mas eu não tô afim de parar aqui, tá?"

                            scene j7_new4 with Dissolve(1.0)

                            o "N-não?"

                            mc "Eu não queria ter que fazer a mesma coisa lá da biblioteca, sabe?"

                            o "A-aah!?"

                            mc "Mas você funciona melhor desse jeito, né?"

                            o "[mc]... lá na b-biblioteca... i-isso-"

                            mc "Shh... fica quetinha. Eu só vou te beijar mais um pouquinho aqui."

                            o "P-por fav-"

                            scene j7_new5 with Dissolve(1.0)

                            pause

                            mc "Eu sei que você gosta no pescoço."

                            o "Nggh..."

                            mc "Você é deliciosa, [o]. Você é macia, seu corpo é muito gostoso de apertar."

                            o "Ahn."

                            mc "Eu vou me aproveitar bastante dele hoje, tá?"

                            o "N-não, [mc]. A [g]..."

                            mc "Ela tá dando um tempo pra gente. Relaxa."

                            o "Mas e s-"

                            mc "Você vai aceitar o que eu mandar, não vai?"

                            o "Nnmm..."

                            mc "Boa garota. Deixa eu sentir você aqui atrás também."

                            scene j7_new6 with Dissolve(1.0)

                            pause

                            mc "Hm... não é só um peitão, você tem uma bunda enorme, Carol."

                            o "P-para..."

                            mc "Você tem o corpo perfeito pra quem gosta de carne, sabie?"

                            mc "É um desperdício você ficar se escondendo. Qualquer um ia querer usar você assim."

                            o "I-isso é um absurdo!"

                            mc "Absurdo? Você não ia gostar?"

                            o "C-claro que não!"

                            mc "Mas eu vou te usar. Alguma coisa contra?"

                            o "V-você... n-não... hmm... ai!"

                            scene j7_new7 with vpunch

                            pause

                            o "Ai! M-meu biquíni!"

                            mc "Você não precisa mais disso, Carol. Só tá atrapalhando."

                            o "[mc]... você tá indo longe demais..."

                            mc "Eu faço o que eu quiser com você. Eu sei que você gosta."

                            o "Ahnn... n-não..."

                            mc "Só falar um pouco mais firme com você e você fica assim, né?"

                            o "Agnn..."

                            mc "Fala logo que você adora quando eu te aperto assim!"

                            o "Aai!"

                            mc "Fala!"

                            o "E-eu..."

                            "O que eu tô fazendo?"

                            "Eu vou mesmo me aproveitar dela desse jeito?"

                            "Se eu continuar assim, não vai ter mais volta. Eu posso fazer o que eu quiser com ela."

                            "Mas é essa relação que eu quero com a Carol?"

                            "O que eu faço?"

                            menu:
                                "Eu aproveitei o suficiente":


                                    mc "Então você quer que eu pare? É só mandar eu parar e eu paro."

                                    o "N-não... e-eu n-não..."

                                    mc "Não consegue mandar eu parar?"

                                    o "N-não..."

                                    mc "Não precisa. Eu sei que no fundo você quer ir devagar."

                                    mc "Desculpa, eu acabei exagerando. Pode se vestir."

                                    o "[mc]... não faça mais esse tipo de coisa."

                                    mc "Tá. Eu não vou fazer mais, ok?{w=0.5}"
                                "A gente vai até o fim":


                                    "Não consigo parar agora. Ela tá prontinha pra eu ir até o fim."

                                    mc "Como você não fala nada, eu vou continuar mandando."

                                    o "A-ah..."

                                    mc "Você adora quando a gente trata você assim. Aposto que a [g] deita e rola com você."

                                    o "S-sim..."

                                    mc "Sabia. Do jeito dela, você faz o que ela manda toda vez, né?"

                                    o "É... hmm..."

                                    mc "Então você vai fazer o que eu mandar também."

                                    o "!?"

                                    mc "Ajoelha alí na rede."

                                    o "A-aqui?"

                                    mc "Vai!"

                                    scene j7_new8 with vpunch

                                    pause

                                    o "Aiin!"

                                    mc "Eu vou ser seu primeiro, Carol! E vai ser hoje!"

                                    o "M-minha nossa!"

                                    mc "Ou alguém já mandou você fazer isso antes?"

                                    o "N-não!"

                                    mc "Então eu vou ser o felizardo. Que delícia..."

                                    o "Ai, [mc]... n-não..."

                                    mc "Não posso? Você tá me mandando parar?"

                                    o "N-não..."

                                    mc "Então o que que é?"

                                    o "A gente não pode... ainda mais aqui!"

                                    mc "Você não quer que eu enfie então?"

                                    o "N-não... fala assim... é vulgar..."

                                    mc "Eu tenho uma ideia..."

                                    o "Hm?!"

                                    scene j7_new9 with Dissolve(1.0)

                                    pause

                                    mc "Eu vou roçar na sua buceta até você admitir que quer meu pau."

                                    o "Aahh! T-tá pegando nela!"

                                    mc "Isso aí!"

                                    o "Anngh!"

                                    mc "Você quer meu caralho ou não quer?!"

                                    o "Aannh! N-não pode! É i-imoral, [mc]!"

                                    mc "Você gosta de imoral, não gosta?!"

                                    o "Aiinn! N-nn!"

                                    mc "Você vai fazer tudo o que eu mandar! Vai ficar aí de quatro!"

                                    o "T-tá!"

                                    mc "Assim que eu gosto! Agora pede meu pau!"

                                    o "Nnnnghh!"

                                    mc "Vai!"

                                    scene j7_new10 with vpunch

                                    pause

                                    o "A-absurdo!"

                                    mc "Absurdo?!"

                                    o "Ainn! Aannngh!"

                                    mc "E se eu mandar você pedir?!"

                                    o "N-não!"

                                    mc "Daí você vai ter que pedir!?"

                                    o "Aaiinnngh! E-eu vou!"

                                    mc "Mas não é imoral?"

                                    o "É i-imoral!"

                                    mc "Mas você gosta?"

                                    o "N-não! M-mas eu tenho!"

                                    mc "Vou mandar você pedir ele então!"

                                    o "Isso! N-não! Não mande!"

                                    mc "Eu vou gozar só de me esfregar em você... aah..."

                                    o "V-vai gozar em mim?!"

                                    mc "Vou te engravidar! Com esse tetão você vai ser perfeita, Carol!"

                                    o "Minha n-nossa! Não!"

                                    mc "Eu tô sentindo você toda melada. Voce tá aproveitando tanto quanto eu! Não minta!"

                                    o "N-nnngg!"

                                    mc "Vem aqui!"

                                    scene j7_new11 with vpunch

                                    pause

                                    o "Vai gozar?!"

                                    mc "Vou enfiar e gozar dentro de você!"

                                    o "Annngh! Vai gozar! Eu vou fazer você gozar!"

                                    mc "Vai, [o]!"

                                    o "Isso é tão errado! Minha nossa!"

                                    mc "Eu tô mandando você fazer eu gozar, Carol!"

                                    o "S-sim! Gozar! Goza!"

                                    mc "Quase!"

                                    o "Aaiinn!"

                                    g "Eeiiiii! Tõ chegaaando!"

                                    mc "A [g]!"

                                    scene black with vpunch

                                    mc "Coloca a roupa!"

                                    o "T-tá!"
                        "Tá bom por hoje":


                            "Nah. Não vamo abusar da fraqueza dela. Tá excelente por hoje."

                            mc "Eu vou querer outro desses logo logo, ouviu? Se prepara."

                            o "[mc]! M-mas então a gente vai mesmo agir como namorados?{w=0.1}"
                "Esperar ela aceitar":


                    mc "Você ainda não tá pronta?"

                    o "E-eu... n-não..."

                    mc "Tudo bem... se você não quiser ainda, eu te espero, [o]."

                    o "[mc]... você é tão incr-"







            scene j7_imagem34 with hpunch

            g "Que que tá rolando aqui?!"

            o "J-júlia?! N-não tá rolando nada!"
        else:


            o "Você é um cara legal, muito gente boa. Mas acho que você faz mais o tipo da [g] mesmo."

            if julia_namoro:

                o "Vocês tão certos de serem namorados."

            mc "Você acha?"

            "Putz, que merda. Acho que eu não consegui impressionar ela hoje. Afe, o que será que eu podia ter feito de diferente?"

            "Se eu tivesse feito outras escolhas... acho que podia ter dado outra coisa..."

            o "Eu gostei bastante das nossas conversas hoje."

            mc "A gente tá juntos na mesma causa pelo menos. Salvar a [g]."

            o "É verdade. Vai ser difícil, mas acho que a gente dá conta."

            mc "Espero que si-"

            scene j7_imagem34 with hpunch

            g "Que que tá rolando aqui?!"

            mc "Hm?"

            o "Oi, Ju."

            g "Toma cuidado! Ele tá fazendo aquilo de novo!"

            o "Hm?"
    else:


        mc "Você é muito gente fina, [o]. Eu acho que a gente pode ser bons amigos."

        mc "A gente tá juntos na mesma causa pelo menos. Salvar a [g]."

        o "É verdade. Vai ser difícil, mas acho que a gente dá conta."

        mc "Espero que si-"

        scene j7_imagem34 with hpunch

        g "Que que tá rolando aqui?!"

        mc "Hm?"

        o "Oi, Ju."

        g "Toma cuidado! Ele tá fazendo aquilo de novo!"

        o "Hm?"

    g "Eu sei muito bem o que tá pegando aqui. Mas não se preocupa, Carolzinha, eu sei que a culpa é dele, viu?"

    mc "Epa epa. Pera aí."

    g "Esse cafajeste faz isso com todas. Chega com essa fala mansa e CRAU!"

    o "V-verdade?"

    mc "Claro que não!"

    if julia_namoro:

        g "Veja que até eu caí nessa ladainha! E eu pensei que ele fosse diferente!"
    else:


        g "Ele tentou comigo também, mas eu resisti!"

    mc "Isso é calúnia!"

    g "É o que todos dizem!"

    mc "Brincadeira..."

    g "Vem aqui, [o]... eu te protejo."

    o "[g]... mas não aconteceu nada..."

    g "Mas nunca se sabe quando ele vai querer atacar. Vem aqui..."

    scene j7_imagem35 with Dissolve(1.0)

    pause

    g "Pronto. Agora eu vou te proteger. Pode dar o fora, [mc]. Não tem nada pra você aqui."

    "A [g] tá falando mal de mim e ainda quer sair como heroína. Que cara de pau."

    "Será que eu deixo ela dar em cima da [o] assim?"

    "Ela deu a chance pra mim... e eu cheguei na Carol... agora é a vez dela... mas..."

    menu:
        "Vou deixar ela continuar":


            $ j7_lesbica = True

            mc "Eu não vou ficar aqui ouvindo essas inverdades sobre minha pessoa! Falou pra vocês."

            o "[mc]..."

            mc "Relaxa, [o]. Eu vou dar uma andada. Qualquer coisa vocês me chamam."

            "Vou dar uma andada nada. Vou é parar logo ali e ver o que a [g] tá aprontando."

            o "Você fez ele ir embora, [g]..."

            g "Eu sei. Mas ele foi bem pago pra isso. Agora você é só minha, [o]."

            o "Ah, não, [g]!"

            g "Eu sei que você tava me negando por causa dele. Não precisa mais ficar com vergonha."

            o "O [mc] foi muito legal comigo... e até com você. Ele disse pra eu ter paciência."

            g "Isso... tenha paciência..."

            o "Ai... Para de falar no meu ouvido assim..."

            g "Sua pele é tão gostosa, [o]... e eu sei que você é super sensível. Eu vejo quando eu pego em você que você até perde o ar."

            o "Então para..."

            g "Ele tava dando em cima de você, é?"

            o "Mhmmm..."

            g "Você ficou toda derretida por ele, né? Você queria que ele te pegasse?"

            o "Ai... n-não..."

            g "Eu sei que seu ponto fraco são os peitos."

            scene j7_imagem36 with Dissolve(1.0)

            g "Você é tão sensível aqui. Ninguém nunca deve pegar nessas duas delícias... você deve ficar só na vontade, né?"

            o "A-ah! V-você pega!"

            g "Será que só eu mesmo?"

            g "E esse pescoço cheiroso... essa pele lisinha... eu não aguento, [o]. Desculpa, mas você é deliciosa demais."

            o "N-não! Ah! Não me aperta assim!"

            g "Eu aperto!"

            o "A-ah! Aah!"







            o "Ai, [g]... v-você sabe do meu problema..."

            g "Não conseguir negar, né?"

            o "Você não pode se aproveitar de mim... i-gual todas aquelas vezes na facul!"

            g "Hehe... será que eu deixo você escapar ou não?"

            label j7_premium2:

                pass

            menu:
                "Se aproveitar da Carol":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_28

                        jump j7_premium2

                    g "Nem fodendo que eu vou deixar você escapar assim."

                    o "A-ah..."

                    g "Por que você... espera... por que você tá toda melada aqui em baixo, hein?"

                    g "Vocês tavam fazendo alguma coisa ali na rede? Eu achei mesmo que voce parecia..."

                    o "J-jú... n-não..."

                    g "Que ódio de vocês! Agora você vai ver, sua puta! Eu vou te castigar!"

                    o "Ain.. t-tá... d-desculpa..."

                    g "Pula logo nessa rede!"

                    scene black with dissolve

                    scene j7_new12 with Dissolve(1.0)

                    pause

                    g "Você gostou do pau dele, né? Não é muito grande, deve ter sido perfeito pra sua xotinha."

                    o "Q-que você tá fazendo?!"

                    g "Eu não tenho pau, mas eu te conheço inteirinha. Vou fazer você gozar igual uma, sei lá! Tô muito brava!"

                    o "Ain... [g]..."

                    g "Só uma mulher pra conhecer outra desse jeito."

                    o "V-você tá me assustando!"

                    g "Não é a primeira vez que eu vou forçar você a dar pra mim, né?"

                    o "Onde você tá mexendo!?"

                    g "Você vai gostar. Olha aqui."

                    scene j7_new13 with Dissolve(1.0)

                    pause

                    o "M-minha nossa! Ah!"

                    g "Relaxa e curte minha língua... mhmm..."

                    o "Aahnn... é d-demais pra mim..."

                    g "Hoje eu vou fazer você ser minha. Vou te deixar viciada em mim."

                    o "E-eu já s- AGHHN!"

                    g "Fica quieta e geme. Ouviu?!"

                    o "S-sim... hmm..."

                    g "Esse seu gemidinho me deixa louca."

                    o "Hmmm..."

                    g "Ainda não acredito como você tava molhada por causa daquele cara."

                    g "Eu só vou parar quando você tiver seca."

                    o "J-júlia... mi-minha... aahnn..."

                    g "Bora gozar logo."

                    scene black with dissolve

                    scene j7_new14 with Dissolve(1.0)

                    pause

                    o "Ahnn..."

                    g "No peito que você gosta, né?"

                    o "N-não..."

                    g "Fala a verdade, safada!"

                    o "S-sim... no peito..."

                    g "Então goza enquanto eu mamo seu peitão."

                    o "A-ahnn..."

                    window hide

                    pause

                    g "Que demora é essa?"

                    o "E-eu..."

                    scene j7_new15 with Dissolve(1.0)

                    pause

                    o "Hmm!"

                    o "Annh... nngh..."

                    window hide

                    pause

                    g "Goza logo, Carol! Tá tão ruim assim?!"

                    o "N-não... é que... [g]..."

                    g "Não é possível que você não consegue chegar lá igual uma pessoa normal!"

                    o "E-eu..."

                    g "Você é uma puta esquisita mesmo, hein?!"

                    scene j7_new15 with vpunch

                    o "A-ah!"

                    g "Você tremeu?! Você é uma louca mesmo. Que tipo de amiga estranha eu fui arrumar."

                    o "Hmhmmm!"

                    g "Entendi tudo."

                    scene j7_new16 with vpunch

                    g "Você quer que eu te trate igual uma vida, é isso?!"

                    o "AGH!"

                    g "É disso que você gosta! Sua viciada! Puta viciada!"

                    o "UUGHGN!"

                    g "Chupa meus dedos! Coloca essa língua pra fora!"

                    g "Você vai fazer tudo o que eu mandar, sua escrava de merda!"

                    o "HMMMNN!"

                    g "Vai gozar?! Goza logo que eu tô mandando!"

                    o "Isso! Isso! HMMN! Vou gozaaaAARR!!!"

                    scene j7_new17 with vpunch

                    pause

                    o "NNNNNNGHH!!"

                    g "Ufa... quem diria, Carol... o que a gente fez com sua cabeça, hein?"

                    o "Aah... aah..."

                    g "Você era só uma garota tímida... agora você precisa ser humilhada pra gozar..."

                    o "Aah..."

                    g "Essa história me deixou bem quente também."

                    o "Hm?"

                    g "É sua vez agora."

                    o "..."

                    scene black with dissolve

                    scene j7_new18 with Dissolve(1.0)

                    pause

                    o "[g]... e se alguém pegar a gente aqui?"

                    g "Não tem ninguém aqui hoje. É meio de semana. Hmm..."

                    g "Além de que você quer me fazer gozar, não quer?"

                    o "E-eu..."

                    g "Você quer ser uma boa putinha, né? Você gosta quando eu me sinto bem."

                    o "Hmmm..."

                    scene j7_new19 with Dissolve(1.0)

                    pause

                    g "Assim mesmo..."

                    o "Aah..."

                    g "Você é tão delicada. Eu vou ter que te dar uma ajudinha, tá?"

                    o "N-não tá bom?"

                    g "Você é perfeita... mas eu preciso de mais, sabe?"

                    g "Você tem o lance que você precisa pro clímax... eu tenho o meu."

                    o "N-não quero falar sobre isso."

                    scene j7_new20 with Dissolve(1.0)

                    pause

                    g "Se não quer falar, então lambe direito."

                    o "O-ogh..."

                    g "Aposto que qualquer daria o que fosse pra ficar com você."

                    g "Olha pra você... não acredito que você não tem dono ainda."

                    o "V-você sabe que eu nunca liguei pra isso."

                    g "Até eu forçar você a gostar, né?"

                    o "..."

                    g "Você tá cada vez mais tarada..."

                    o "N-não fala isso..."

                    g "Mas é legal, né? Viver esse outro lado."

                    o "C-com moderação... mas você não tem moderação..."

                    scene j7_new21 with Dissolve(1.0)

                    g "Como não? Ok... eu sei... talvez eu não fosse a melhor pessoa pra te colocar nesse mundo."

                    o "Hmmm..."

                    g "Que foi? Você acha que eu fui?"

                    o "Não vou falar nada... se eu falar algo posso piorar tudo mais ainda."

                    g "Será que eu vi você pelo que você era?"

                    o "Cala a boca..."

                    g "No fundo você era uma puta que se fingia de inocente?"

                    o "Eu v-vou morder você."

                    g "Hmm... vai... morde..."

                    o "Afe..."

                    g "Ai! Você mordeu mesmo..."

                    o "Você mandou..."

                    g "Então vai, vamo terminar com isso. Para de falar e chupa."

                    scene j7_new22 with Dissolve(1.0)

                    g "Assim mesmo... ghnnn..."

                    o "..."

                    g "Eu tô muito quente, Carol. Mas só sua língua não vai dá."

                    o "N-não?"

                    g "Você vai ter que encher meus buraquinhos."

                    o "Ai, [g]..."

                    g "Você quer fazer eu gozar ou não? Não vai parar no meio..."

                    o "N-não quero parar... m-mas é perigoso... e eu não sou boa nisso..."

                    g "Eu vou ensinar você. Pega seus dedinhos e enfia aqui..."

                    menu:
                        "Melhor eu parar aqui":


                            o "J-júlia... isso é demais. Eu quero parar..."

                            g "Sério mesmo?"

                            o "P-por favor?"

                            g "Ok... você foi bem... na próxima você faz direito, ok?"

                            o "Tá... obrigada..."

                            g "Obrigada, senhora."

                            o "S-senhora..."
                        "Eu tenho que obedecer a [g]":


                            "Eu não consigo falar não... eu tenho que obedecer ela..."

                            scene j7_new23 with Dissolve(1.0)

                            g "Assim... aaann..."

                            o "Não machuca?"

                            g "Um pouco... mas é gostoso."

                            g "Só continua assim... enfia... vai enfiando com força... e lambe também, não para."

                            o "Aah..."

                            g "Ficando excitada de novo?"

                            o "Ai... fica quieta."

                            g "Vai metendo. Você mete gostoso, Carol."

                            g "Você tá pegando o jeito. Tá perdendo o medo."

                            o "E-eu vou fazer você gozar, Jú!"

                            g "Você parece animada! AAHN!"

                            o "Vem aqui!"

                            scene black with vpunch

                            g "Uau!"

                            scene j7_new24 with vpunch

                            pause

                            g "Annh! Q-quantos dedos?! Ahn!"

                            o "Goza, Jú!"

                            g "Você tá... Aannhn... Doida?!"

                            o "E-eu tô quente! Eu quero que você goze!"

                            g "Então tá! Continua assim! Hmm!"

                            o "Ahnn.. hmmnng..."

                            g "Se você gemer assim... hmm... a-ajuda... annnhg.."

                            o "Enfia sua mão na minha boca."

                            g "Você gostou?"

                            o "Eu gostei... eu gostei muito... vai... ahnn..."

                            scene j7_new25 with Dissolve(1.0)

                            pause

                            g "Tá muito bom, Carol!"

                            o "Mhmmmmm!"

                            g "Ahnn! Vai! Com as duas mãos! nnnghh!"

                            g "Eu vou gozar de verdade! Ah! Não acredito! Ahnn!"

                            o "Ahnng! Gozxxaa! Aannghh!!"

                            g "Minha nossa! Vai! Hnnngg! Não paraaann!!"

                            o "Ahnng! Aaahh!"

                            g "VaiiiiiIINN!"

                            scene j7_new26 with vpunch

                            pause

                            g "AaaaaaAAAAAHH!"

                            o "V-vou t-também!"

                            scene j7_new26 with vpunch

                            o "J-júliaaannhh!"

                            scene j7_new26 with vpunch

                            pause

                            g "Aah..."

                            o "Uhh..."

                            scene black with Dissolve(2.0)

                            pause

                            scene j7_new27 with Dissolve(1.0)

                            o "Então toda vez que a gente... vai ser assim agora?"

                            g "Não seria muito bom?"

                            o "A-acho demais pra mim, [g]..."

                            g "Hoje você foi muito bem. Uma boa garota."

                            o "O-obrigada... mas eu tô falando sério..."

                            g "A gente pode ver... hoje eu tava irritada porque o [mc] te deixou molhada."

                            o "Ah... e sobre ele?"

                            g "Se você não se importar, ele pode brincar com a gente também..."

                            o "I-isso é demais..."

                            g "Ele foi legal comigo... acho que ele merece um agrado. Duas gostosas pra ele se divertir."

                            o "E-eu ainda sou virgem... e minha primeira vez vai ser um grupal? Nem sei como chama isso..."

                            g "Três pessoas não é bem grupal, mas eu entendi... então hoje ele não te comeu?"

                            o "E-eu pedi pra ele... e ele... mas quase..."

                            g "Que legal! Então a gente vai te deflorar juntos, ok?"

                            o "T-tá louca?"

                            scene j7_new28 with Dissolve(1.0)

                            g "Hmmm... e se eu mandar você dar pra ele, hm?"

                            o "Ahh... o que você tá fazendo?"

                            g "Fala a verdade, Carol... você não consegue mais sair dessa, consegue?"

                            o "C-como assim?"

                            g "Esse prazer... essa sensação... é viciante..."

                            o "Aahnn..."

                            g "Sentir isso o dia todo... todos os dias... ser escravo dela... não parece bom?"

                            o "Aainn... n-não me lambe... eu vou... você sabe..."

                            g "Tá vendo? E então? Você vai dar pra ele? Vai deixar ele te arrompar?"

                            o "M-minha nossa... aahnn..."

                            "O que tá acontecendo comigo? A [g] tá me transformando numa ninfomaníaca."

                            "Eu preciso... parar... mas... aah..."

                            menu:
                                "Eu não posso fazer isso":


                                    o "Eu preciso..."

                                    scene j7_new27 with Dissolve(1.0)

                                    o "E-eu preciso de um tempo pra mim, Ju... pensar em tudo isso."

                                    g "Parece que você ainda tem volta, né?"

                                    o "G-graças aos céus..."

                                    g "Vamos ver por quanto tempo..."
                                "Eu só obedeço você, Ju":


                                    "Eu não consigo mais parar!"

                                    o "Você sabe, Jú..."

                                    scene j7_new29 with Dissolve(1.0)

                                    o "Eu tô pronta pra fazer o que você mandar... eu sou assim..."

                                    g "Excelente... então agora você é minha putinha de verdade."

                                    o "Sua putinha... eu sou..."

                                    g "Finalmente eu quebrei você, Carol..."

                                    o "Hehe... então vamos procurar o [mc]?"

                                    g "Calma lá, garota... tá bom por hoje."

                                    o "Mas eu preciso..."

                                    g "Ficar com vontade o dia todo também faz parte... você vai se acostumar."

                                    o "Hmmm..."
                "Deixar ela escapar":


                    g "Ok... vou deixar você escapar hoje..."

                    o "O-obrigada..."

                    mc "Mas vai ter aula, viu? Te encontro na biblioteca..."

                    o "M-minha nossa..."

            scene black with Dissolve(1.0)



            scene j7_imagem23 with Dissolve(1.0)

            "Uou... o que foi isso?"

            "Essa [g] é louca... e a [o]... f-foi bem interessante..."

            "Se as coisas continuarem assim, não vejo a hora de sair com elas de novo e ver o que elas vão aprontar comigo..."
        "Vou parar essa palhaçada":


            mc serio "Ela só tá inventando pra dar em cima de você, [o]. Aparentemente ela não aprendeu nada."

            o "Afe, [g]!"

            g "Você vai acreditar nele e não em mim?"

            o "Óbvio! Você já tá passando a mão em mim!"

            g "N-não é isso!"

            o "Vamos embora agora!"

            g "[o]!"

            scene j7_imagem23 with Dissolve(1.0)

            mc "Haha... seu plano quase deu certo."

            g "Você ainda vai me pagar por essa, cuzão."

            mc "Quero ver..."

            o "Venham logo!"

            scene black with dissolve

            "Vou ficar de olho nessa aí. E a [o]..."

    label julia_e7_final:

        pass



    scene black with Dissolve(3.0)

    $ tempo = 3

    $ v42_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v42_fim","final","local")

    scene black with Dissolve(3.0)

    pause

    call checa_final from _call_checa_final_4

    jump call_cidade

label julia_evento8:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("j8_save", extra_info="j8_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ julia_v8 = "evento"

    "O que foi aquele meu dia com a Júlia no resort?"

    scene black with dissolve

    scene ape_pensando with Dissolve(1.0)

    "Aquele medo que ela tem de que as pessoas enjoem dela..."

    "Com certeza a Júlia passou por umas barras pesadas. Essa carência dela, esse jeito... tem que ter uma razão por trás disso."

    "E do jeito que ela tá ficando cada vez mais doida atrás da [o], da [s], deve faltar pouco pra tudo isso explodir."

    "Agora... onde que eu quero tá onde tudo isso acontecer?"

    if julia_namoro:

        "Ela é minha namorada, então eu quero ajudar ela o máximo que eu puder."
    else:


        "A gente é só amigos... mas eu devo ser o melhor amigo dela... talvez o único amigo de verdade."

    "Mas ao mesmo tempo, esse jeito dela também cansa um pouco. Será que a Júlia ainda tem salvação?"

    "Talvez o caso dela seja coisa pra psicólogo, só com muita terapia mesmo pra resolver."

    "Ou tem algo que eu possa fazer? E mesmo que tenha... por que EU tenho que fazer alguma coisa?"

    mc "Droga, [g]... por que você não pode só ser uma gatinha meio safadinha?"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "{i}Trr trrr{/i}"

    "Hm? De quem é esse número?"

    scene black with dissolve

    scene ape_celular_falando with Dissolve(1.0)

    mc "Oi?"

    o "Oi, [mc]. Desculpa te incomodar. Ah! É a [o]."

    mc "Oi! Como você tá?"

    if j7_carol_beijo:

        o "E-eu..."

        mc "Ainda não esqueceu do que a gente fez lá no resort?"

        o "Ah... isso não tá certo. Eu não devia..."

        mc "Tá tudo bem, [o]. Não precisa pensar demais nisso."

        o "Mas... tudo bem... tem razão... a gente não é mais criança."
    else:


        "Imagina se eu tivesse ficado com ela lá no resort?"

    "A Carol com certeza é um amor... tô feliz que ela me ligou. Será que a gente podia..."

    o "É... eu tô preocupada com uma coisa. Queria saber só se você tá com a Jú."

    mc "Não. A gente não se viu desde aquele dia."

    o "Hmm... isso não é bom."

    mc "O que aconteceu? Por que você tá nervosa?"

    o "Eu acho que ela tá com aqueles idiotas de novo. Não acredito! Que raiva da [g]!"

    mc "[o]... a gente precisa pensar se é nossa responsabilidade corr-"

    o "Agora não! Ela tá desaparecida! Posso contar com você? Você vai procurar ela?"

    mc "Bom..."

    menu:
        "Não posso deixar ela sozinha agora.":


            mc "Eu não ia me sentir bem deixando ela sozinha."

            o "No fundo você gosta dela, né?"



            if julia_namoro:

                mc "Claro que eu curto ela... a gente tá namorando, durr."

                o "Não precisa ser grosso também."
            else:


                mc "A gente não tá juntos, mas somos amigos."
        "Só porque você tá pedindo.":


            mc "Eu vou por você, não por ela. A Júlia já é grande."

            o "T-tudo bem, então... você indo..."

            mc "E eu vou ganhar alguma coisa em troca depois?"

            o "N-nada de coisa em troca!"

            mc "Vamos ver..."

            o "[mc]!"

            mc "Tá bom..."

    o "Tá. Eu vou na casa dela. Vou começar por lá. Provavelmente ela não tá, mas só pra garantir."

    o "Você vai na faculdade ou no cinema, tá? Se eu encontrar ela eu te aviso."

    mc "Beleza. Se eu achar eu te falo também."

    o "Obrigada mesmo, [mc]... você é o único que eu posso contar agora."

    o "A Júlia pode ter aquele jeito dela, mas no fundo ela só precisa da nossa amizade."

    o "Agora vamos lá! Júliaaaa!"

    "Desligou..."

    scene black with dissolve

    scene ape_geral with Dissolve(1.0)

    "Eu tenho que começar pegando o busão."

    call locomocao

    "Se ela tiver em um dos dois lugares, eu tenho 50 por cento de chance de acertar."

    "Qual vai ser meu chute?"

    jump j8_escolhe_lugar



    label j8_escolhe_lugar:

        menu:
            "Faculdade":


                if j8_faculdade:

                    "Eu já fui na faculdade... quase certeza que ela não tá lá."

                    jump j8_escolhe_lugar

                $ j8_faculdade = True

                jump j8_faculdade
            "Cinema":


                if j8_cinema:

                    "Eu já fui no cinema... quase certeza que ela não tá lá."

                    jump j8_escolhe_lugar

                $ j8_cinema = True

                jump j8_cinema

            "Tadaima" if j8_faculdade and j8_cinema:

                $ j8_tadaima = True

                jump j8_tadaima



        jump j8_continua

    label j8_faculdade:

        scene black with dissolve

        scene uni_hall geral with Dissolve(1.0)

        pause

        "Eu lembro da outra vez que eu vim procurar a Júlia aqui..."

        "Investigando ela igual o James Bond... cada coisa que eu já fiz por causa dela."

        "Aquele dia eu vi como ela e a Carol são amigas... ou mais que amigas..."

        "Não consigo tirar isso da cabeça."

        if julia_e3 == "seducao":

            "E depois... a Júlia... embaixo da mesa... ah... foi a coisa mais quente que eu fiz aqui."

        "A Júlia é super novinha, né? Ela acabou de entrar na faculdade. Tá no primeiro ano."

        "Eu também era bem porra louca no meu primeiro ano. Será que eu tô pegando pesado demais com ela?"

        "Uma mocinha que acabou de fazer 18... que ainda por cima foi adotada... talvez querer que ela seja boa da cabeça seja pedir muito."

        "Sei lá... Bora dar uma olhada se ela tá aqui."

        show black with dissolve

        play sound som_35_passos

        pause 2.0

        hide black with dissolve

        "Nada... Ela não tá aqui."

        "E agora?"

        jump j8_escolhe_lugar

    label j8_cinema:

        scene black with dissolve

        scene cinema geral with Dissolve(1.0)

        pause

        "Cinema... outro lugar que teve loucura com a Júlia."

        "Eu ainda não tenho certeza do que ela foi fazer no banheiro... aquela hora que a Mari me chamou."

        "Não adianta eu ficar pensando em besteira."

        if j5_good:

            "A gente ficou aqui. Foi incrível. E eu ainda tirei ela na mão daqueles otários."

            "Com certeza o Caio ficou puto da vida quando a gente se pegou."

            "Naquele dia eu percebi que a Júlia podia ser diferente. Ela podia trocar a baguncinha por alguém que ela gosta."
        else:


            "Ela ainda ficou com o Caio e o Teo no meio do cinema..."

            "Só de pensar já me dá meio raiva da Júlia."

            "A Mari que me fez companhia aquela noite."

            "Será que se a gente tivesse namorando as coisas seriam diferentes?"

        "Eu vim aqui... mas como eu vou saber se ela entrou em algum filme?"

        "Vou dar uma olhada e falar com a vendedora ali."

        show black with dissolve

        play sound som_35_passos

        pause 2.0

        hide black with dissolve

        "Pelo menos ela não viu nenhuma jovem igual a Júlia ou o Caio. Não tinha ninguém no banheiro também."

        "Afirmativo que eles não tão aqui."

        "Pra onde eu vou agora?"

        jump j8_escolhe_lugar

    label j8_tadaima:

        "Espera... tem um lugar que ela não falou. A Júlia pode muito bem tá lá!"

        scene black with dissolve

        scene tadaima restaurante with Dissolve(1.0)

        "O Tadaima... a Carol não pediu pra eu olhar aqui. Mas eu não podia deixar de vir."

        "Foi aqui que a gente se conheceu. E ela ainda trabalha aqui, não trabalha?"

        "A diabinha tentou me afastar da Sayuri. Sorte que eu não caí na tramoia da bandida."

        "Depois eu voltei aqui e a gente começou a sair juntos. A pegação na praça, levar ela pra facul..."

        "Parece que fazem anos que isso aconteceu. E lembrar disso agora... nossa... que nostalgia."

        "Eu fico pensando se realmente eu posso ajudar a Júlia a mudar."

        "Tirar ela da garra desses cuzões e tentar fazer ela ver que ela tem amigos de verdade."

        "Mas ela precisa parar de encher o saco da Sayuri, da Carol, o meu saco..."



        "Hmm... a Júlia é tão bacana. Se ela não tivesse esse jeito. Talvez ela fosse a namorada perf-"

        scene tadaima restaurante with hpunch

        "???" "Como que não tá?!"

        "E-essa voz!"

        play sound som_35_passos

        scene black with dissolve

        scene j8_new1 with Dissolve(1.0)

        mc "Carol... você tá gritando com a garconete?"

        o "Ela tá escondendo a Júlia!"

        mc "Pode ir. Eu vou falar com ela e já tamo saindo."

        "Garçom" "Obrigado. Mas vai rápido. Vocês não podem ficar aqui sem consumir nada."

        mc "Valeu. Pode deixar."

        mc "O que aconteceu contigo, Carol? Nem parece você. Nada da Júlia, né?"

        o "Nnghh... não... dessa vez eu tô preocupada pra valer. Você não tá?!"

        menu:
            "Sim. A gente precisa encontrar ela!":


                mc "Saco... Se a gente deixar ela sozinha, certeza que vai dar merda."

                o "Claro... ela não tem condições de ficar 5 minutos sozinha com eles!"
            "Vamos esquecer a Júlia. Quer fazer algo?":


                mc "A Júlia é grandinha, Carol. Deixa ela. Vamo aproveitar que tamo aqui e fazer algo nós dois?"

                if julia_namoro:

                    o "Você não é namorado dela? Você devia tá mais preocupado com isso!"
                else:


                    o "Mesmo vocês sendo só amigos..."

                o "Agora não é hora de ficar passeando! Ela precisa da gente!"

                mc "Por que você não só deixa ela fazer as coisas dela? Talvez fosse melhor pras duas."

                o "C-claro que não! Desde quando você é frio assim, hein?"

                mc "Tudo bem, tudo bem... o que você quer de mim?"

        o "A gente tem que encontrar eles! E parar os dois antes que eles façam uma merda juntos!"

        mc "Você acha que ela saiu pra ficar com o Caio? É isso?"

        o "Claro! O que mais pode ser?"

        menu:
            "E se ela foi dar adeus pra ele pra sempre?":


                mc "E se ela aprendeu e resolveu... dar adeus pro Caio pra sempre? Tipo... fechar esse ciclo."

                mc "Você lembra como ela tava diferente lá no resort, né?"

                o "Você acredita mesmo nisso? É mais fácil chover canivete que a Júlia ter resolvido os problemas psicológicos dela!"

                mc "Você tem que ter mais fé nela, [o]."

                o "Minha fé na Júlia é negativa, [mc]!"
            "Tem razão. Só pode ser safadeza.":


                mc "Tá na cara que é sacanagem, né?"

                o "Só se você for muito ingênuo mesmo você ia achar outra coisa."

        scene j8_new2 with Dissolve(1.0)

        o "Eu tenho que cuidar dela, ou ela já teria ido pro buraco!"

        mc "Você realmente gosta dela, né?"

        o "Q-quê?! N-não é isso! Ela só não tem juízo! E eu não quero que ela jogue a vida dela fora."

        o "Eu não tenho nada com a [g]! Por favor não fique criando fanfics sem sentido."

        mc "Ok, desculpa. Mas a gente já foi em todo lugar que a gente conhecia. Você não achou nada, achou?"

        o "Não... fui na casa dela, no resort, na biblioteca..."

        o "Até liguei pra casa de passeio do idiota do Caio. A mulher que cuida da casa falou que não tem ninguém lá."

        mc "Sério?"

        o "A menina sumiu!"

        mc "Será que aconteceu alguma coisa com ela mesmo?"

        o "Quer saber? Já deu."

        mc "Vai desistir?"

        o "O que a gente pode fazer? Fizemos o que dava. Se ela quer sumir do mapa, a gente não é onisciente igual Deus."

        o "Obrigada pela ajuda, [mc]... e desculpa colocar você nessa. Se ela te procurar, por favor me fala."

        mc "Não fica nervosa, tá? A Júlia sabe se cuidar."

        o "Obrigada... tomara que sim."

        o "Se a gente terminou aqui... eu acho que eu vou indo nessa."

        o "Quem sabe se a Júlia não fosse tão criança a gente podia ter clima pra fazer alguma coisa nós três."

        "Alguma coisa nós três? Que coisas ela tá pensando?"

        o "Mas, né? É nossa cruz ter que aguentar essa... você sabe... maluquinha. Até, [mc]."

        mc "[o]..."

        scene black with dissolve

        scene tadaima vip with Dissolve(1.0)

        "A Carol é tão bacana. Ela sim é uma mulher decente."

        "Será que... ela aceitaria... ficar comigo?"

        if julia_namoro:

            "Eu podia terminar com a Jú."
        else:


            "Eu e a Júlia somos só amigos mesmo."

        "Eu podia esquecer a Júlia pra sempre. Toda aquela bagunça. E ficar com uma garota normal, inteligente, bacana."

        "Além que a Carol é linda, com um corpo delicioso demais!"

        "Claro que se eu ficar com a Carol, já era minha chance com a Júlia. Então eu preciso pensar bem. Mas ela é tão fofa."

        "Ou eu tô maluco? Eu devo tá maluco! Droga! O que eu faço? Ela tá indo embora!"

        menu:
            "Carol! Eu não gosto da Júlia! Eu gosto de você!":


                $ carol_declarou = True

                "Eu não vou perder essa chance de falar pra ela o que eu sinto de verdade."

                scene j8_new3 with hpunch

                mc "[o]!"

                o "Ai! Que foi?!"

                mc "Eu quero mandar a real. Eu acho que eu devia ter falado isso antes até."

                o "P-por que você tá falando sério assim?"

                mc "Porque o que eu vou falar é muito sério. Não quero que você veja como brincadeira."

                o "[mc]... T-tá..."

                mc "Eu quero namorar com você, não com a Júlia. É de você que eu gosto, [o]!"

                o "A-ah!!!"

                mc "Eu tô pronto pra desistir de qualquer coisa com a Jú pra ficar contigo."

                mc "Você... aceita? Aceita namorar comigo pra valer?"

                o "M-mas assim?"

                mc "Você cansou da Júlia e pode ser que a gente não se veja mais. Eu não quero perder a chance de falar a verdade."

                o "Não... eu..."

                mc "Você não quer?"

                o "N-não é isso! E-eu! Eu preciso de ar!"

                mc "Calma, Carol. Só responde sim ou não."

                o "Tudo o que a gente passou... eu... [mc]..."

                mc "..."

                o "Ai..."

                o "Tá bom."

                mc "!!!"

                o "Eu falo. Você merece uma resposta."

                o "Calma... eu..."

                o "Eu não quero."

                mc "Quê? Não quer?"

                o "Não. Eu não tô pronta pra namorar."

                mc "Não tem isso de tá pronta. A gente pode aprender juntos!"

                o "Não é isso... eu... eu tenho um problema."

                o "Eu tenho uma dificuldade de falar 'não'. Eu fico nervosa quando mandam em mim."

                o "E é por isso mesmo que eu tô parando de ser amiga da Júlia. Ela sabe que eu tenho isso e usa contra mim."

                o "Eu sei que ela precisa de alguém do lado dela, e eu gosto muito dela... só que..."

                o "Eu tenho que resolver meus problemas antes de ser amiga da Júlia de verdade."

                mc "Mas eu não sou a Júlia! Eu não vou fazer mal pra você!"

                o "Mesmo assim... é a mesma coisa. Eu só posso compartilhar algo com alguém depois que eu resolver isso."

                o "Se eu fosse namorar com alguém... é... com certeza... s-seria alguém igual você."

                o "Mas eu não posso. Desculpa."

                "Droga... a Carol tá me dando o toco."

                "Mas eu sei como ela é. Eu posso fazer ela ficar comigo se eu quiser."

                "Talvez um empurrãozinho seja o que ela precisa... isso... forçar ela um pouquinho não tem problema, certo?"

                menu:
                    "Vou roubar um beijo dela!":


                        mc "Você só tá com medo."

                        o "Hm?!"

                        scene j8_new4 with hpunch

                        pause

                        o "Nnnghhh!"

                        mc "Eu sei que no fundo você quer ficar comigo! Você só tá com medo!"

                        o "N-não!"

                        mc "Me beija!"

                        o "N-não fala assim... nnghh..."

                        mc "Você gosta de mim. Você vai me beijar."

                        o "Ah... não manda em mim assim... nnghh..."

                        mc "Eu sabia. Você quer me beijar!"

                        o "Não... aah... não faz igual a Júlia, [mc]... por favor..."

                        mc "Você tem certeza que não gosta de mim?"

                        o "Hmmm... n-não é isso... eu só não posso... agora..."

                        mc "Droga, [o]... eu queria tanto ficar com você!"

                        o "Aahh... me escuta..."

                        menu:
                            "Tirar a roupa dela e continuar":


                                mc "Vem aqui."

                                scene black with dissolve

                                scene j8_new5 with hpunch

                                o "Ai! N-não..."

                                mc "Você é tão linda. Você precisa aprender o lado bom da vida, Carol."

                                o "Aahh... por que...?"

                                mc "Você vai ficar comigo."

                                o "Aahnn... vou?"

                                mc "Claro que vai. Eu sei que você quer."

                                o "Ahhn..."

                                mc "Você é tão gostosa."

                                o "Nnnnhh... nããoo..."

                                mc "Xii..."

                                o "POR FAVORR!!!"

                                mc "!!!"
                            "O que eu tô fazendo?! Isso não tá certo!":


                                mc "D-desculpa... eu... eu só queria..."

                                o "Sai!"

                        scene j8_new6 with hpunch

                        "O que eu fiz?!"

                        mc "[o]..."

                        o "Você... aaahnn... você é igualzinho a Júlia..."

                        mc "Eu pensei que você tivesse..."

                        o "Eu te falei! E mesmo assim! Você veio pra cima de mim!"

                        o "O que v-vocês têm na cabeça?! Vocês n-não pensam nos outros?!"

                        mc "Eu gosto tanto de você, [o]... você não entende?"

                        o "Eu entendi! Mas isso não muda! Eu disse que não tô pronta pra isso! Por que você não me ouve?!"

                        o "Adeus!"

                        mc "[o]!"

                        scene black with dissolve

                        scene j8_new7 with Dissolve(1.0)

                        "Por que eu fiz isso?"

                        "Ela parecia tão... suculenta... eu tinha que ter me segurado! Eu não sou um animal!"

                        "Droga... eu preciso esquecer isso... a Júlia ainda tá desaparecida."

                        pause 2.0

                        "Agora... pensando na [o] e a [g]..."
                    "Não... o que eu tô pensando?":


                        "Nunca... eu não sou esse tipo de homem. Se ela disse 'não', é não."

                        mc "É triste tomar um fora... mas claro que eu vou te respeitar, né?"

                        o "N-não é um fora..."

                        mc "Não precisa ficar triste, Carolzinha. Eu sou grandinho. Eu aguento um 'não', ok?"

                        o "D-desculpa..."

                        mc "Não precisa se desculpar também. Quem sabe no futuro, certo?"

                        o "S-sim... digo... nnghh..."

                        mc "Hahaha... se não for comigo, espero que outro cara, ou garota, te faça feliz."

                        o "O-obrigada... a-até mais, [mc]."

                        mc "Até."

                        o "Eu... eu fico muito feliz... de saber que você gosta de mim..."

                        mc "Verdade?"

                        o "Você é o primeiro rapaz... que fala uma coisa dessas pra mim assim..."

                        o "Um dia... eu quero tá pronta pra uma relacionamento..."

                        o "E eu torço... pra que você se dê bem com a Jú! ADEUS!"

                        mc "Carol!"

                        scene black with dissolve

                        scene j8_new7 with Dissolve(1.0)
            "Até depois. A gente se fala.":


                mc "Qualquer novidade eu te falo. Até mais."

                o "Até..."

                scene black with dissolve

                scene j8_new7 with Dissolve(1.0)

        "Com certeza a [o] gosta de verdade da Júlia."

        "Será que elas são só melhores amigas... ou rola uma coisa a mais?"

        "Esse jeito todo preocupado da Carol... será que tem mais que amizade nisso?"

        if julia_namoro:

            "Espero que no final a Júlia não me troque por ela... era só o que faltava..."

        "Mas eu acho que ela também gosta de mim... e ela não tem experiência nenhuma nessa área."

        "Bom... a Carol tá fora do meu alcance infelizmente... bola pra frente."

        jump j8_continua



    label j8_continua:

        pass



    "Ai, [g]... O que você tá aprontando dessa vez?"

    "Hmm... espera... tem um lugar que a gente não foi ainda!"

    "Com certeza é um lugar que eu não ia querer voltar... nem por um milhão de C$."

    "A casa do Caio. Onde a gente foi na festa aquela vez."

    "Bosta... merda... eu vou ter que ir falar com aquele riquinho mauricinho de novo?"

    "Além de se achar, o desgraçado trata a Mari e a Júlia super mal. Ele só fica de conversinha com o tal do Téo."

    if julia_e4 == "caio":

        "Aquela vez ele me deu uma pauta e ainda me ajeitou a Mari... tipo... até que a gente se entendeu aquela noite."

        "Mas isso não muda que ele se acha o reizinho da turma. Alguém precisa abaixar a bola desse maldito."
    else:


        "Ele nunca fez nada por mim. Ainda tentou me comprar lá na festa."

    "Não tem jeito."

    "Se eu quero deitar com a cabeça tranquila no travesseiro essa noite eu tenho que fazer tudo o que eu posso."

    "Bora pra casa dele."

    scene black with dissolve

    $ tempo = 2

    scene cidade centro10 with Dissolve(1.0)

    mc "É aqui."

    play sound som_15_campainha

    pause 1.0

    "Interruptor" "Quem fala?"

    mc "Oi..."

    menu:
        "É um amigo do Caio.":


            mc "Eu sou um amigo do Caio. Ele tá?"

            "Interruptor" "O senhor Caio? Sim, está."
        "Tem uma mocinha ruiva aí?":


            mc "Eu tô procurando uma amiga minha. Uma ruivinha, com dois coques."

            "Interruptor" "A senhorita Júlia?"

            mc "Essa mesmo!"

    "Interruptor" "Hm?"

    "Interruptor" "Espera um segundo..."

    "Interruptor" "..."

    "Interruptor" "Pode subir, por favor."

    mc "S-subir? Eu só queria saber se-"

    "Interruptor" "Eu abri o portão. Por favor, use o elevador principal."

    mc "Ok..."

    "Eu nem queria vir... e agora eu tô subindo? Que que tá acontecendo?"

    play sound som_35_passos

    scene black with dissolve

    scene caio_varanda_cenario with Dissolve(1.0)

    "De novo eu tô aqui... eu lembro aquela vez que rolou a festa. A Júlia tava loucassa"

    if julia_e4 != "caio":

        "Mas eu consegui tirar ela da mesa e evitar coisa pior."
    else:


        "Eu ainda fiquei vendo ela em cima da mesa, com o Caio e todo mundo se aproveitando dela."

    "Não que fosse fazer qualquer diferença eu acho... a Júlia já deve ter feito de tudo..."

    play sound som_35_passos

    scene black with dissolve

    scene j8_new8 with Dissolve(1.0)

    pause

    caio "Fala, mano!"

    mari "Oi, [mc]."

    mc "Você que falou pra eu subir?"

    caio "É. Queria trocar uma ideia contigo. Já que você veio atrás de mim, então bora."

    menu:
        "Eu vim procurar a Júlia.":


            mc "Eu vim atrás da Júlia."

            caio "Cara, esquece a Júlia."
        "O que você quer conversar?":


            mc "Que ideia você quer trocar?"

            caio "Nada especial, meu mano."

    caio "Eu sinto que você tem potencial, sabe?"

    mc "Potencial?"

    mari "..."

    caio "Eu conheci muitos betas iguais você por aí. Mas a maioria tá perdido, saca?"

    mc "Beta?"

    caio "Você nem sabe o que é isso, cara? Vou te mandar a real. Eu tenho a red pill aqui pra você."

    mc "Não sei se eu tô entendendo o que você tá falando."

    caio "É uma parada que vai mudar tua vida."

    mari "Caio..."

    caio "Quieta. Que agora os homens tão falando coisa séria."

    mari "Tá..."

    caio "Senta aqui."

    mc "Hmm..."

    scene black with dissolve

    scene j8_new9 with Dissolve(1.0)

    pause

    caio "Assim, [mc]. Você tem que entender que tem muita mentira no mundo. Uma camada de fumaça esconde a verdade."

    mc "Certo... e a verdade tá por trás disso?"

    caio "Isso aí! Mas você precisa tomar a red pill pra enxergar, entende? Igual no Matrix."

    menu:
        "Ok. Manda a real aí então.":


            mc "Se você diz... qual a real então?"

            caio "Eu sabia que você ia tomar a red pill, cara! Tu é igual o Téo, você tem cabeça, mano!"

            caio "A real é que a mídia criou essa farsa do feminismo. Mas a verdade é que os homens tão se ferrando!"

            caio "As mulheres têm tudo de mão beijada e nós que pagamos as contas, a gente que tem que conquistar!"

            caio "Esse lance de igualdade é tudo mentira! Elas querem dominar a gente, e não vamos deixar."

            mc "Hmm..."

            scene j8_new11 with Dissolve(1.0)

            pause

            caio "Homens e mulheres nasceram diferentes e têm que ter funções diferentes na sociedade. Igualdade meu ovo!"
        "Não quero saber dessa merda.":


            mc "Sinceramente, eu não vim aqui pra isso. Sem querer ser chato, mas valeu."

            mari "Rsrs..."

            scene j8_new10 with hpunch

            pause

            caio "A-ah! Cara! Eu tô mandando a real pra ti! Você vai continuar sendo um beta pra sempre?!"

            caio "Deixa eu resumir então!"

            mc "Ok..."

            caio "A moral da história dá pra resumir em uma frase. Presta atenção."

    caio "Mulheres são cadeados, e homens são chaves. Se uma chave abre vários cadeados, é uma chave mestra..."

    caio "... mas se um cadeado é aberto por várias chaves, ele é um cadeado defeituoso. Simples, né?"

    caio "Homens foram feitos pra ficar com várias mulheres, agora as mulheres que querem o mesmo tão se desgastando."

    caio "Os homens são divididos em alfas e betas. Eu sou um alfa, e você é um beta, por enquanto."

    caio "As mulheres querem alfas. Homens másculos, com dinheiro, poder, shape e personalidade."

    caio "E os betas ficam com o que sobra. São esses homens que não entendem como o jogo do sexo funciona."

    caio "Olha pra Júlia e a Mari. Por mais que elas digam o contrário, elas sempre voltam pra mim."

    caio "E eu nem ligo de dividir elas com betas como você, porque eu sei que no fundo elas vão voltar pro pai."

    mari "..."

    scene j8_new12 with Dissolve(1.0)

    pause

    caio "Eu tô tentando ensinar isso pro Téo. Ele tá aprendendo. E você tem potencial também."

    caio "Se vocês seguirem na red pill levando à sério, vocês vão ser homens que vão tá cheio de mulher no seu pé."

    caio "Mas se ficar de amizadinha com mulher, xi... vai ser sempre o amiguinho. O ombro amigo, mas que não fode ninguém."

    caio "Eu tô pouco me fodendo pra elas, mas fodo todas! Tá vendo como é?! Hahahaha!"

    menu:
        "Eu acho que você pode ter razão nisso.":


            mc "Pensando aqui... pode ser que você tenha razão. Faz sentido..."

            caio "Tá vendo?! Você tá pronto pra tomar a pílula da verdade, cara!"
        "Você tá falando muita merda. Só acho.":


            mc "Sinceramente, só parece que você tem ódio das mulheres e tá vomitando merda."

            caio "Não, mano! Para de ser imbecil! Você não entendeu nada?!"

            mc "Eu entendi o suficiente."

    caio "A gente vai sair juntos muito mais! Daí tu vai ver!"

    "???" "Sair com quem? Espero que seja com garotas, filho."

    caio "P-pai!"

    mc "!!!"

    scene black with dissolve

    scene j8_new13 with Dissolve(1.0)

    pause

    gi "Olha só! É o [mc]. É isso, né?"

    "Meu Deus! É o diretor lá do NBC! Que eu conheci com a Nona!"

    mc "Sim, senhor."

    gi "Espero que meu filho não esteja dando trabalho pra você."

    caio "C-claro que não, pai. Tô mandando a red pill pra ele."

    "P-PAI?! O GEVANNI É PAI DO CAIO?!"

    gi "De novo isso? Esses jovens de hoje parece que dão nome pra tudo."

    gi "Mas é bom ver que você tá com a Mari. Isso sim é companhia boa, não é, Mari?"

    mari "Oi, senhor, [gi]. É sim."

    gi "Eu vejo mais meu filho com aquele tal de Téo. Eu prefiro mil vezes ele como uma garota linda como você."

    mari "Obrigada."

    caio "O Téo é meu amigo, pai! Eu tô ajudando ele!"

    scene j8_new14 with Dissolve(1.0)

    pause

    gi "O que mais ele seria? Era só o que me faltava. Meu filho ser gay. Me dá desgosto só de pensar."

    caio "Que gay!? C-claro que não, idiota!"

    gi "Assim que se fala. Quando você me pediu pra colocar o Téo na pizzaria eu achei meio estranho."

    caio "M-mas eu pedi pra tu conseguir o emprego da Mari também, né?! Lá no Cassino!"

    gi "Isso é..."

    caio "E você sabe que eu tenho a Júlia também. Se a Mari pisar na bola, eu troco na hora."

    mari "..."

    gi "Que Júlia, garoto?! Eu já disse pra você não se envolver com aquela garota!"

    caio "Só q-"

    gi "Cala a boca! Me respeite, ouviu? Quer ficar com todas? Não ligo. Mas aquela Júlia eu já disse que não."

    menu:
        "Licença, mas por que a Júlia não?":


            mc "Que que tem a Júlia? Por que ela não?"

            caio "Cala a boca você também, hein?!"

            gi "Vai tratar seu convidado assim, moleque!?"

            scene j8_new15 with hpunch

            pause

            gi "Idiota!"

            caio "Ai! Que tapão!"
        "Melhor eu ficar na minha":


            caio "Tudo bem..."

            gi "Acho bom."

    gi "Eu vou ali no quarto pegar uma coisa e já vou voltar pro banco."

    scene j8_new16 with vpunch

    pause

    caio "N-não! Eu pego pro senhor!"

    gi "Finalmente aprendeu a respeitar os mais velhos, né? Tá bom. Pega lá. Vou tá lá no carro. Você leva pra mim."

    caio "Pode deixar."

    gi "Aproveita e leva um pano e uma sacolinha. Tá precisando dar uma limpada lá."

    caio "Sim. Já tô indo."

    gi "Até mais, [mari], linda. Até mais, [mc]. Quando der faz uma visita novamente no NBC."

    "Ir lá? Depois do que aconteceu com a Nona e o roubo do cofre?"

    menu:
        "Com certeza. Vou passar lá então.":


            mc "Fechado. Uma hora dessas eu passo lá então."

            gi "Então tá combinado."
        "Tá meio corrido esses dias.":


            mc "Quer saber... tá meio corrido pra mim esses tempos haha..."

            gi "Acho bom você encontrar tempo então."

            mc "Mas temos alguma coisa pra resolver. Tipo..."

    gi "Temos um assunto muito sério pra conversar. Melhor que você esteja lá."

    mc "O-ok..."

    gi "Fiquem bem."

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    scene j8_new17 with Dissolve(1.0)

    pause

    mari "Oi, [mc]."

    mc "Oi... tudo bem?"

    mari "Tô feliz de te ver."

    mc "A é?"

    mari "Não vai deixar as baboseiras do Caio te contaminar."

    menu:
        "Eu sei. Aquele monte de merda do esgoto da internet.":


            mc "Eu não sei da onde aqueles caras tiram essas coisas."

            mari "É tempo demais pensando em besteira."

            mc "É... só que mesmo sendo um babaca, o Caio sempre consegue o que quer."
        "Baboseira? O que você tá fazendo aqui então?":


            mc "Você realmente acha que são baboseiras? O que você tá fazendo aqui com ele então?"

            mari "[mc]... é complicado."

            mc "Talvez o que o Caio disse tenha fundamento."

            mari "Claro que não. Isso é pensamento de pessoas doidas."

    mc "Tem a Júlia também. Ela também fica atrás dele."

    scene black with dissolve

    scene j8_new18 with Dissolve(1.0)

    pause

    mari "A Júlia... A Júlia é outra coisa. Também não é uma coisa simples."

    mc "Simples ou complexo, o que acontece tá aí na cara de todo mundo. Ela se envolve com o Caio e o amigo dele."

    mari "Eu sei, mas não julgue ela assim. A Júlia é uma boa pessoa. Me escuta."

    "Essa pose dela... eu consigo ver quase tudo..."

    menu:
        "Focar no meio das pernas delas":


            "Não tem como eu perder essa chance..."

            scene j8_new19 with Dissolve(1.0)

            pause

            mc "Aah..."
        "Vou só prestar atenção e ser um homme decente":


            mc "Uhum... pode falar..."

    mari "Já teve vez que o Caio tava irritado comigo, ele ia até me bater, e a Júlia me ajudou. Tirou a atenção dele."

    mari "Ela não é uma garota ruim, [mc]. Mas ela tem algo dentro do coração que faz ela ficar assim."

    mari "É uma coisa que eu acho que a gente não pode entender. Que só ela sabe o que ela tá sentindo."

    mc "Mesmo que a Júlia tenha algo no coração dela, na cabeça dela, sei lá, ela tá afastando todo mundo que gosta dela."

    mc "A Carol disse que a Júlia abusa dela e ela não quer mais ser amiga. E a Carol era a única amiga de verdade dela."

    mari "..."

    mc "Tirando essa turminha de vocês, agora a Júlia só tem eu e a Sayuri, a irmã dela. E eu tô ficando cansado disso."

    mari "Mas você gosta de verdade dela, não gosta?"

    scene j8_new20 with vpunch

    mc "E-eu?!"

    "O que eu sinto pela Júlia?"

    if julia_namoro:

        "A gente tá namorando. Mas será que eu amo ela de verdade? Ou é só o tesão falando mais alto?"
    else:


        "Nós somos só amigos... mas não dá pra negar que eu sinto uma coisa a mais por ela. Mas isso é gostar de verdade?"

    menu:
        "A gente acabou virando amigos.":


            if julia_namoro:

                "Ela não precisa saber que a gente namora..."

            mc "Depois do que a gente passou, a gente acabou virando amigos. Só isso."

            mc "Não acho que isso vai atrapalhar..."

            mari "Para de tentar ser legal comigo."

            mc "Não é 'tentar ser legal'!"

            mari "Eu tô falando sério. Você tá aqui por causa dela. Não negue."
        "Eu acho que eu gosto dela de verdade.":


            mc "Eu não sei exatamente o porquê, mas acho que eu gosto dela de verdade."

            mari "Hehe... eu sabia. Eu consigo ver nos seus olhos quando você fala dela."

            mari "Até quando você critica a Jú, você fala com carinho."

    mari "Eu queria tanto que alguém me amasse assim um dia também..."

    mc "Mari..."

    mari "Tudo bem, [mc]. Eu sabia que não ia dar pra rolar nada entre a gente."

    mc "Ei... espera..."

    scene black with dissolve

    scene j8_new21 with Dissolve(1.0)

    pause

    menu:
        "Quem disse?!":


            mc "Mas... quem disse?"

            mari "Você continua falando qualquer coisa..."

            mc "Não. Você não tá me entendendo. É sério."
        "A gente ainda pode ser amigos, certo?":


            mc "Mas a gente pode curtir uma amizade. Eu sempre gostei de conversar contigo."

            mari "É..."

    mc "Mas e o Caio? Vocês..."

    mari "O Caio é um babaca. Quanto mais tempo eu passo com ele, mais eu vejo isso."

    mari "Eu achei que um dia talvez ele mudasse, mas a verdade é que eu tava me enganando."

    mari "Ele vai tratar as mulheres como objetos pro resto da vida. A visão de mundo dele é torta demais."

    mari "É incrível como ele maltrata eu e a Júlia. Ele tem prazer nisso."

    mari "Só que com o Téo ele é todo diferente. Daí eles são amigos."

    mari "É como se fosse uma guerra entre homens contra mulheres. Como se ele tivesse um ódio da gente..."

    mc "Toma cuidado com ele então, tá? Tenta dá um jeito de sair fora dessa. Antes que seja tarde."

    mari "Obrigada... você sempre me tratou tão bem. Sempre foi um cavalheiro. E isso é uma coisa que o Caio nunca vai entender."

    mari "Eu torço pra que você seja sempre assim. E se não for comigo, que seja com a Júlia então."

    mc "Eu não sei se a Júlia me valoriza igual você... essa é a questão."

    scene black with dissolve

    scene j8_new22 with Dissolve(1.0)

    pause

    mari "A Carol gostava da Júlia, mas ela queria mudar a Júlia. Aposto que a irmã dela também."

    mari "Eu acho que a Jú não precisa de alguém que queira mudar ela. Ela precisa mudar sozinha."

    mari "O que ela precisa é de alguém que tenha paciência. Que dê força pra que ela resolva esse problemão no coração."

    menu:
        "Não tá certo engolir o quanto ela é tóxica.":


            mc "E enquanto isso a gente só aguenta ela abusando da gente? Isso não tá certo."

            mari "Eu sei que não é fácil. Mas se você gosta dela de verdade, tem que ser assim."
        "Eu entendo. Forçar ela é errado também.":


            mc "É uma violência querer que ela mude no nosso ritmo. É isso?"

            mc "A gente tem que respeitar ela, mesmo que a gente ache que ela tá indo pro buraco..."

            mari "Isso! Você entendeu o que eu tô tentando falar."

            mari "Mesmo que a gente ache uma coisa, é a pessoa que precisa entender. Ou não vai ser de verdade."

    mc "Hmm... mas não é fácil, Mari..."

    mari "Eu vou ajudar vocês. Pode ter certeza. Tá vendo aquele corredor ali atrás?"

    mc "Sei. Ali que ele foi pegar o negócio pro pai dele, né?"

    mari "Sim. O Caio tá escondendo uma coisa lá. Vai lá."

    mc "Invadir a casa dele assim?"

    "Eita... será que isso é uma boa?"

    menu:
        "Acho melhor eu não me arriscar.":


            mc "Mari, acho melhor eu não comprar briga com ele e o pai dele."

            mari "Não esquenta. Eu seguro ele pra você."

            mc "Mesmo assim..."

            mari "É importante, [mc]. Vai por mim."

            mc "Tá bom... vou confiar."
        "Tá bom. Mas você me cobre?":


            mc "Você vai me ajudar? Tipo... ficar de vigia?"

            mari "Claro."

    mari "Quando você terminar, pode só sair. Eu vou deixar a barra limpa pra você."

    mc "Até depois então."

    mari "[mc]..."

    scene black with dissolve

    scene j8_new23 with Dissolve(1.0)

    pause

    mc "O-oi..."

    mari "Eu tava pensando que... se tudo der certo... a gente podia ser amigos."

    "A Mari é tão gente boa... ela parece tão mais adulta que a Júlia... até que a Carol."

    "E não é só a cabeça que é boa, não... ela é sexy... gostosa pra caralho também."

    "Será que ela aceitaria ficar comigo de verdade? Se eu escolhesse namorar ela?"

    menu:
        "Com certeza. A gente já é inclusive.":


            mc "Você sabe que a gente já é amigos."

            mari "Que bom... eu vou tá torcendo por você."

            mc "A gente ainda vai se ver, né? Depois que tudo isso acabar."

            mari "Tomara que sim. Mas agora você tem que ir!"
        "Eu acho que a gente pode ser mais que amigos.":


            mc "Do que você tá falando?"

            mari "A-acha impossível? Desculpa... eu..."

            mc "Eu acho que a gente pode ser mais que amigos..."

            mari "Hah... para de me dar falsas esperanças, bobo. Seu coração já é dela."

            if j6_final_mari:

                mc "Como assim? Você não lembra do que eu disse lá na casa de férias? A gente ficou lá."

                mari "Você lembra daquilo?"

                mc "Eu disse que queria algo sério com você, não disse?"

                mari "Eu não pensei que..."

                mc "Chega mais perto..."

                mari "Hmm..."

                scene black with dissolve

                scene j8_new24 with Dissolve(1.0)

                pause

                mari "Assim?"

                mc "É... você gostou do que a gente fez lá?"

                mari "Muito... eu gozei de verdade aquele dia... você fez com força... e com jeitinho..."

                mc "Eu senti que rolou uma química de verdade entre a gente."

                mari "[mc]... mas você tem a Júlia..."

                mc "Mas e se eu escolher você? E se, de verdade, eu preferir ficar contigo do que com ela?"

                mari "Já falei pra você parar de brincar comigo..."

                mc "Para você de falar que é brincadeira. Eu tô falando sério, [mari]."

                mari "..."

                mari "Eu... você realmente gosta de mim assim? Falando sério, [mc]."

                mari "Sem brincadeira. Você... ficaria comigo ao invés da Carol ou da Júlia?"

                mc "Mari..."

                "Eita... ela chamou na responsa agora. Sem brincadeira... eu tenho que falar a verdade."

                "É com ela que eu quero ficar de verdade?"

                menu:
                    "Sim. Eu quero só você.":


                        $ mari_final = True

                        mc "Sim. Eu tô falando sério. Eu quero você. Troco todas elas por você, Mari."

                        mari "!!!"

                        mc "Que foi? Não achou que eu ia te escolher?"

                        mari "N-não... eu... pensei que você tava me deixando em segundo plano... nunca..."

                        mc "Você não é minha segunda opção, ok? Você é com quem eu quero ficar... de verdade."

                        mari "Ah..."

                        scene black with dissolve

                        scene j8_new25 with Dissolve(1.0)

                        pause

                        mc "Agora você tá me provocando... me dá essa boquinha logo..."

                        mari "Rsrs... você quer, é?"

                        mc "Claro!"

                        mari "Vou te falar um segredo... meu sonho sempre foi ser escolhida de verdade por um homem."

                        mari "Eu sinto que sempre fui segundo lugar..."

                        mari "Você é o primeiro homem que fala, de verdade, que eu sou a primeira escolha."

                        mc "Os homens são idiotas então. Porque você é perfeita."

                        mari "Hmm..."

                        mari "Eu tenho outro segredo."

                        mc "Mais um?"

                        mari "Eu amo o Caio."

                        mc "!!!"

                        mari "Mesmo ele não me amando... eu gosto dele."

                        mc "Mas ele é um babaca! Você falou!"

                        mari "Eu sei... mas é complicado..."

                        mari "Se você realmente gosta de mim... fica com a Jú."

                        mc "Com a Jú?"

                        mari "É... ela e o Caio têm uma coisa estranha. Mas não é amor."

                        mari "Ela não gosta dele de verdade. E ele não gosta dela de verdade. Eu tenho certeza."

                        mari "Eles têm um problema... E só vão ser feliz se eles conseguirem quebrar essa corrente."

                        mc "Você quer o Caio livre?"

                        mari "Sim..."

                        mc "Mari... você me deu o fora e ainda pede um favor?"

                        mari "Desculpa... é sua culpa."

                        mc "Minha?"

                        mari "Você é o primeiro homem que me coloca em primeiro. Você... provou pra mim que eu tenho meu valor."

                        mari "Se eu consegui conquistar um homem incrível como você, o Caio, tontão, não tem chance."

                        mc "Mari... não sei se eu dou risada ou eu choro."

                        scene black with dissolve

                        scene j8_new26 with Dissolve(1.0)

                        pause

                        mari "Fica com a Jú. Ela é a mulher mais interessante que eu vi na vida."

                        mari "Se ela conseguir se livrar do Caio... ela vai ficar só com as coisas boas."

                        mc "Merda... não era isso que eu queria ouvir."

                        mari "Se você gosta mesmo de mim, acredita em mim. Vocês vão ser felizes."

                        mc "..."
                    "Não... eu gosto de você, mas eu prefiro outra.":


                        mc "Desculpa, Mari... mas eu não posso escolher você. Não seria honesto."

                        mari "Tá vendo? Eu sabia..."

                        mc "Eu gosto de você... isso não muda. E acho que a gente se divertiu bastante. Mas meu coração..."

                        mari "Eu sei. E eu não fico triste, tá? E vou te falar... não ligo de ser a segunda."

                        mc "S-segunda?"

                        mari "Fico feliz que você goste de mim... mesmo gostando mais de outra."

                        mari "Quem sabe um dia... a gente possa se divertir de novo, né?"

                        mc "Com certeza..."

                        scene black with dissolve

                        scene j8_new26 with Dissolve(1.0)

                        pause
            else:


                "Talvez... se eu tivesse ficado com ela lá na casa de férias do Caio eu pudesse falar alguma coisa..."

                mc "A gente nunca sabe o futuro, certo?"

                mari "Certo..."

                scene black with dissolve

                scene j8_new26 with Dissolve(1.0)

                pause

    mari "Boa sorte, [mc]. E se você e a Júlia resolverem ficar juntos... toma cuidado com o Caio."

    mari "Ele parece sempre tá por cima... mas quando ele não consegue o que ele quer, ele fica maluco."

    mc "Mas então eu não devia invadir a casa dele, né?"

    mari "Para de medo! Vai logo! Eu vou lá segurar ele! Tchau!"

    mc "T-tchau."

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    scene j8_new27 with Dissolve(1.0)

    "Nem acredito que eu tô invadindo a casa do idiota... se ele me pegar tô fodido."

    "O que será que a Mari quer que eu veja que é tão importante?"

    "O que o Caio guarda aqui que pode me ajudar?"

    "Hmm... a porta tá meio aberta. É o quarto dele? Será que ele veio correndo pra pegar o lance pro pai dele?"

    "Ele tava tão nervoso com o Gevanni que nem deve ter fechado a porta..."

    "Hmm... só uma olhadinha..."

    pause 2.0

    "!!!"

    "N-não é possível!"

    "Não acredito! Eu tenho que entrar!"

    scene j8_new28 with vpunch

    pause

    mc "O que a Júlia tá fazendo aqui?!"

    g "Hm? Aah..."

    g "[mc]? Pera... o que tá acontecendo?"

    mc "Júlia! O que você tá fazendo nessa cama só de calcinha e sutiã?!"

    g "Eu tô com sono ainda... Deixa eu dormir mais um pouco..."

    mc "Não acredito! Levanta agora!"

    g "Tá bom... calma..."

    scene black with dissolve

    scene j8_new29 with Dissolve(1.0)

    pause

    g "[mc]? É você mesmo? O que você tá fazendo aqui? Aqui é a casa do Caio, né?"

    mc "Não acredito... eu e a Carol procurando você pela cidade... e você trepando com esse idiota?!"

    g "Não! Eu não fiz nada disso!"

    menu:
        "Não mesmo?":


            mc "Nada? Você tá falando sério?"

            g "Sim... é verdade..."
        "Você acha que eu sou idiota?!":


            mc "Só pode ser brincadeira... você acha que eu sou idiota?!"

            g "Não! É verdade!"

    g "Por favor... me escuta..."

    mc "Júlia... não tem escuta. Você desapareceu! Não atendeu seu telefone... a Carol tava doida atrás de você."

    g "Aquela lá se preocupa com tudo, [mc]. Não entra na dela."

    mc "Ela gosta de você, Júlia! Ou melhor... gostava... eu acho que ela chegou no máximo que dava."

    g "HUH!!!"

    scene black with dissolve

    scene j8_new30 with Dissolve(1.0)

    pause

    g "Huh... Eu sabia... uma hora ela ia se cansar de mim... todo mundo cansa..."

    mc "Você tá falando como se fosse culpa da Carol? Você não ajuda!"

    g "Ela é só mais uma! Todo mundo me abandona uma hora ou outra! Ninguém me aguenta!"

    mc "A Carol era sua amiga de verdade... e você perdeu ela. Ela disse que você abusou da fraqueza dela."

    g "Mentirosa... ela sempre quis ficar comigo... ela só não tem coragem de admitir..."

    mc "Se você continuar pensando assim... você vai perder a Sayuri também."

    g "Gghh... eu... eu já perdi."

    mc "Como assim? A Sayuri sempre te amou. Ela disse alguma coisa?"

    g "Sim... ela disse que eu tava confundindo as coisas..."

    mc "Até com sua irmã, [g]? Você não tem limites?"

    g "Cala a boca..."

    "A Júlia perdeu a Sayuri também... a Sayuri que tinha tanto carinho por ela."

    "Primeiro a Carol... e sem a Sayuri... agora a Júlia só tem eu. Sem mim, ela tá sozinha no mundo."

    g "Eu sei o que você tá pensando... que eu fiquei sozinha. Você também vai me abandonar."

    menu:
        "Exatamente. Só se você tiver uma boa explicação.":


            mc "Eu tô por aqui com você. Acho bom você ter uma excelente explicação."
        "Eu ainda não decidi. Depende de agora.":


            mc "Vai depender de agora. Porque eu também tô por aqui com esse seu jeito."

    g "Então vai logo! Todos vocês me amam no começo! Mas depois se cansam de mim! Sai fora!"

    mc "Não fale como se fosse nossa culpa! Seu jeito tóxico expulsa as pessoas da sua vida!"

    scene black with dissolve

    scene j8_new31 with Dissolve(1.0)

    pause

    g "EU SEI!!!"

    g "Eu sei! É tudo culpa minha! Por isso que eles me abandonaram! Porque eu sou imprestável!"

    g "Eu não sirvo pra nada! O único que me aguenta é o merda do Caio! Porque ele também é um cretino!"

    g "Droga... vai logo embora..."

    mc "É isso que você quer?"

    g "Isso é o que VOCÊ quer."

    g "Merda... {i}nnghh{/i}"

    "[g]... o que adianta chorar agora?"

    "Eu vou abandonar ela também? Depois de tudo o que a gente viveu juntos?"

    menu:

        "Ela é minha namorada. Eu vou proteger ela." if julia_namoro:

            "Eu não posso deixar minha namorada nessas condições."

            "Eu não sei se a gente vai continuar junto depois dessa, mas pelo menos por enquanto, não posso abandonar ela."
        "Sim. Ela merece.":


            "Ela ferra tudo e ainda se faz de vítima... como se a gente quisesse abandonar ela."

            "É uma desgraçada... que merece sofrer pra aprender como tratar os outros."

            "Uma mimada que merece viver sofrendo na mão de outro mimado."

            "O melhor é se livrar desse tipo de relação tóxica logo de cara. Não ser arrastado pra esse drama."

            "Essa é a decisão mais sensata. Com certeza."

            "Mesmo assim..."

            "Como eu posso abandonar ela nessas condições?"

            "Ela só tem eu."
        "Não. Não posso deixar ela assim.":


            "Que tipo de homem deixa uma mulher assim?"

            "Nada disso... que tipo de pessoa deixaria a outra no seu pior momento sozinha?"

    "Droga... por que eu tenho a mania de carregar o sofrimento dos outros nas costas?"

    "Às vezes eu queria ter um coração de pedra."

    mc "Chega pra lá."

    g "Q-quê?"

    scene black with dissolve

    scene j8_new32 with Dissolve(1.0)

    pause

    mc "Como você consegue ser tão problemática, hein?"

    g "O que você tá fazendo aqui ainda?"

    mc "Para de se fazer de difícil. Pelo menos reconheça que você é uma pé no saco."

    g "Cala a boca... pé no saco é você."

    mc "Você é tão cheia de energia, tão carismática, divertida. Tem tudo pra ser uma mulher incrível."

    mc "Mas você afasta as pessoas. Você ignora o sentimento dos outros. Como se tivéssemos obrigação de aguentar tudo."

    mc "Você não percebe? Ninguém te deixou. Você afastou eles de você. Abusando deles, sendo tóxica, não respeitando a amizade."

    g "Eu só ajudei todo mundo... acelerando as coisas. Uma hora todos vão enjoar e me abandonar."

    g "Todo mundo só me quer por causa do sexo. E quando eles enjoam... ele me largam."

    g "Sexo é muito bom no começo. Mas uma hora fica sem graça. E é aí que eles me abandonam."

    mc "Eu não acho que a Sayuri ou a Carol estavam com você por causa de sexo."

    g "Por que mais elas iam tá? É que elas não tinham coragem de admitir... hipócritas..."

    mc "Haha... você tem uma cabeça bem torta. Chega a ser engraçado."

    g "Hm?"

    g "Que droga, [mc]... por que você é assim?"

    mc "Assim?"

    g "É! Idiota desse jeito!"

    mc "Ei..."

    g "Qualquer outro já teria me deixado! Até minha irmã me deixou!"

    if julia_namoro:

        g "E você é o contrário! Ainda quis namorar comigo!"

        mc "Sim... querer namorar você foi loucura mesmo."

    g "Daí me encontra de calcinha na casa de um ex e ainda tá aqui!?"

    g "Como você pode ser tão palerma?"

    mc "Você tem razão... talvez eu seja um beta, igual o Caio falou."

    mc "Eu fico com a amizade, com a bomba, e ele que transa contigo."

    g "O Caio é um babaca. Ele se acha a última bolacha do pacote. Mas é só um filhinho de papai."

    mc "Vou falar a mesma coisa que disse pra Mari: você fala isso, mas tá aqui."

    g "Nada a ver. Eu trocaria 10 Caios por 1 [mc]. Qualquer hora."

    mc "Tá bom. Não precisa começar com essa agora."

    scene black with dissolve

    scene j8_new33 with Dissolve(1.0)

    pause

    g "É sério! Eu sinto uma coisa diferente quando tô com você! Não é a mesma coisa de sempre!"

    g "Eu sempre... eu sinto um vazio. O tempo todo. Uma coisa que tá faltando."

    g "E eu acho que esqueço dele quando eu tô trepando, ou brigando..."

    menu:
        "Mas eu cansei. Não quero mais nada com isso.":


            g "Eu sei! Calma! Escuta o que eu tô falando!"

            mc "Hm..."

            g "Com você não é assim!"
        "Certo... continua...":


            mc "E daí?"

            g "E daí que com você eu sinto uma coisa diferente!"

    if j4_salvou:

        g "Você lembra aquele dia que você me tirou da mesa de bilhar?"

        mc "Como eu vou esquecer... ia deixar você lá pro Caio, o Téo e os outros fazerem o que quisessem?"

        g "Tá vendo? Você é diferente... todos os homens lá queriam só me ver sem roupa, sendo uma safada. Igual uma puta."

        g "Você não..."
    else:


        g "Mesmo você me deixando lá na mesa de bilhar..."

        mc "Eu não aguentei... eu tinha que ver você... você mexeu demais comigo."

        g "Safado..."

    if j5_good:

        g "No cinema... você quis ficar comigo... ao invés de querer me ver zoando com eles..."

        mc "Claro! Mas lá você aceitou ficar comigo... eu não achei que você ia aceitar."

        g "Eu também não... mas... lá eu já comecei a sentir uma coisa diferente..."

        g "Eu tinha uma necessidade de fazer o que o Caio queria, mas querer ficar com você foi mais forte."

        mc "Hmm..."
    else:


        g "Mesmo com o que aconteceu lá no cinema..."

        mc "Você ficando com os dois lá no meio! Você é louca!"

        g "Mesmo assim... você continuou comigo..."

    if j6_historia:

        g "Eu até te contei minha história..."

        mc "Aquela que aconteceu com você e o Caio, né?"

        g "Sim... você é a única pessoa que eu contei isso... nem a mana sabe os detalhes."

        mc "Hmm..."
    else:


        g "Quando a gente vai naquela casa de passeio do Caio eu não consegui te contar uma coisa importante..."

        mc "Aquele dia..."

        g "Mas mesmo assim..."

    g "O principal... foi no resort. A gente teve um dia tão diferente lá. E nós nem transamos."

    mc "É. Mas teve discussão aquele dia... você tava mais focada na Carol que em mim."

    g "Eu sei! Mas escuta! Eu achei que ia ser igual sempre! Mas só de saber que você tava lá... mesmo me deixando de lado um pouco."

    g "Saber que você tava lá... me deixou feliz. Eu senti que só de tá com você, eu não precisava de mais nada."

    g "Nem precisava da Carol pra brigar! Ou fazer sacanagem! A gente devia ter ido sozinhos!"

    menu:
        "Era o que eu queria. Sair com você.":


            mc "Era o que eu queria... passar um tempo com você."

            g "Fui tudo idiotice minha! Mas como eu ia saber antes de saber?!"

    g "Foi naquele dia que eu percebi que eu podia preencher aquele vazio com outra coisa."

    g "O carinho da Sayuri nunca tinha feito isso por mim. Nem a preocupação da Carol."

    g "Foi seu jeito... quando fez todas aquelas coisas por mim, que fez eu perceber essas coisas!"

    mc "Escutar você falando assim... será que finalmente você começou a criar juízo?"

    scene black with dissolve

    scene j8_new34 with Dissolve(1.0)

    pause

    g "Sei lá... mas eu prometo que eu tô falando a verdade pra você, gato!"

    "Será que a Júlia tá entendendo as coisas de verdade?"

    "Ser um panaca que corria atrás dela acabou mostrando algo que até hoje ela não tinha?"

    "A Júlia tem várias coisas bacanas. Tá com ela é sempre quente, divertido, excitante!"

    "Se ela realmente começar a valorizar nossa relação, eu acho que a gente podia ter um tempo bom."

    g "Que foi? Acabou a bateria?"

    mc "Tô pensando no que você disse..."

    g "A-apaixonou, foi? Se a gente se entender... a g-gente podia fazer até uma baguncinha pra comemorar."

    menu:
        "Baguncinha? Gostei...":


            mc "Hmmm..."

            g "Parece que alguém gostou... t-tá com saudades da minha boquinha no seu pau, é?"
        "De novo essa história?":


            mc "Já voltamos pra baguncinha?"

            g "P-para de ser chato..."



    g "Eu sempre precisei da bagunça pra me tirar da desgraça que eu vivia. Mas acho que eu encontrei outra coisa pra fazer isso."

    if julia_namoro:

        mc "Eu? Digo... nosso namoro?"

        g "Sim! A gente sempre teve uma puta química. Tanto que a gente resolveu ficar!"

        g "Eu caguei às vezes... mas chega!"

        g "E eu descubri agora! Eu descobri que eu quero tentar ser sua! De verdade!"

        g "Só me dá mais uma chance! Eu sei que você também gosta de mim, [mc]!"

        menu:
            "Bom... se você realmente mudou...":


                mc "Acho que... se você realmente tá entendendo o que a gente pode ter... e quer..."

                mc "Pode ser que dê pra gente se entender..."

                g "Isso, caralho!"
            "Não sei. Não acho que seja isso...":


                mc "Não sei, Júlia... não sei se eu continuo sentindo a mesma coisa por você..."

                g "Eu sou o melhor sexo que você teve na sua vida! E você não viu nada ainda!"
    else:


        mc "Eu? Tipo... nossa amizade?"

        g "É, né, DURR!"

        g "Mas não é a amizade. Eu acho que a gente sempre teve química. Essa parte não dá pra negar."

        g "Faltava só a gente querer!"

        g "E eu descubri isso agora! Eu descobri que eu quero tentar ser sua! De verdade!"

        g "Você não tá afim de tentar?! Eu sei que você também gosta de mim, [mc]!"

        menu:
            "Bom... se você realmente mudou...":


                mc "Acho que... se você realmente tá entendendo o que a gente pode ter... e quer..."

                mc "Pode ser que dê pra gente se entender..."

                g "Isso, caralho!"
            "Não sei. Não acho que seja isso...":


                mc "Não sei, Júlia... não sei se é isso que eu sinto por você..."

                g "Eu sou o melhor sexo que você teve na sua vida! E você não viu nada ainda!"

    g "E se d-der errado, a gente vai cada um pra um lado! Mas imagina deixar passar essa chance?!"

    g "E se eu for a mulher da sua vida?! E você meu homem certo?!"

    mc "Você acredita em destino agora?"

    g "F-foda-se se eu pareço uma idiota! Eu tô gostando de você de verdade! Pode rir!"

    mc "Haha... eu tô rindo, mas não é de você, boba."

    g "Sei... por isso que eu nunca me declarei pra ninguém... a gente parece uma palhaça..."

    mc "A Júlia com vergonha? Não é possível... você foi abduzida?"

    g "Vai... continua batendo!"

    mc "Tá bom... eu vou parar de tirar sarro... se você tá sendo sincera... não é justo contigo."

    g "Fala de mim, mas você também é bem engraçadinho... claro que eu tô falando a verdade, porra."

    scene black with dissolve

    scene j8_new35 with Dissolve(1.0)

    pause

    "Será que é possível? Que a Mari tinha razão? Que a Júlia precisava de tempo?"

    "Será que ela entendeu finalmente? Que aquela vida que ela levava não era exatamente o que ela queria?"

    "Eu não acho que a Júlia vai mudar completamente de uma hora pra outra... mas se ela tá sendo sincera agora..."

    "Talvez eu posssa ficar do lado de uma garota divertida, engraçada e que cresceu demais nesses meses."

    g "Não vai falar nada?"

    if julia_namoro:

        g "A gente vai continuar com o namoro? Vamos ser namorados pra valer ou não?"
    else:


        g "A gente vai continuar brincando de amiguinho ou a gente vai ser namorados pra valer?"

    g "Eu... eu não vou ter coragem de perguntar de novo."

    "Essa é a escolha que pode mudar tudo na minha vida."

    "Eu tenho que... calma... huh?"

    "HUH?!"

    "Calma, [mc]! Não... seja idiota!"

    "Tudo o que a Júlia disse é lindo, mas ela tá quase pelada na casa do Caio!"

    "Eu quase esqueci disso!"

    "Se ela tinha entendido o valor do que a gente tinha, por que raios ela veio transar com ele?!"

    "Ela só tá me engabelando! Igual sempre! Essa..."

    mc "[g]... eu... quase caí na sua."

    g "Hm?"

    mc "Se tudo o que você tá falando é verdade..."

    scene j8_new36 with hpunch

    pause

    mc "QUE MERDA VOCÊ TÁ FAZENDO AQUI?!"

    g "E-eu?! Como assim?!"

    mc "Você tá na porra da casa do Caio sem roupa! Como você pode vir com essa de que quer um lance sério agora?!"

    mc "Como eu vou ter uma relação de verdade com uma companheira que na primeira chance vai pra casa do ex?!"

    mc "Você só pode ter problema nessa cabeça oca!"

    g "Não! Eu não transei com ele!"

    g "E eu não quero mais nada com o Caio! Eu prometo!"

    mc "Cara... de novo isso? Você acha que eu sou trouxa? Tu tá na cama dele sem roupa!"

    g "Eu sei! Mas não é o que parece!"

    g "Depois que a Sayuri me deixou eu fiquei com medo de incomodar você e a Carol!"

    mc "E veio trepar e ser maltratada pelo idiota?"

    g "Sim..."

    mc "Até que enfim você tá sendo honesta."

    g "Não! Eu juro que eu saí com ele, mas não fiz nada! Nem um beijo, nem nada!"

    g "Eu, ele, o Téo e a Mari saímos, mas não rolou nada! Tanto que eu fiquei nesse quarto aqui separada!"

    g "Eu acho que a Mari nem ficou até o fim também. O Téo e o Caio foram fazer sei lá o que sozinhos!"

    g "Devem ter contratado umas putas, sei lá..."

    g "Mas eu juro que não fiz nada! Eu nunca menti pra você, [mc]!"

    if julia_namoro:

        mc "A gente tá namorando! Você acha que tá certo isso, caralho?!"

        g "Eu sei... mas meu coração é assim... não tem explicação matemática..."

        g "Mas eu juro... eu não transei com o Caio, nem ninguém! Eu continuo sendo sua namorada!"

    g "Eu posso até ser uma puta! Mas eu não sou mentirosa! Você sabe que eu sempre fui sincera!"

    mc "..."

    "Eu vou acreditar nessa história?"

    "Se ela tiver falando a verdade, é a prova de que ela mudou pra valer."

    "A Júlia de antes nunca negaria uma baguncinha dessas. Ainda mais com a tristeza depois de perder a Sayuri."

    "Mas..."

    "Se ela tá mentindo... quer dizer que ela não mudou nada. Em qualquer momento de tristeza ela vai apelar pra isso."

    "A Júlia sem dúvida é uma das garotas mais incríveis que eu já conheci."

    "A energia, o humor, a espontaneidade, o sexo, o prazer... ela deve ser uma das pessoas que eu mais me emocionei na capital."

    "Só de imaginar a gente saindo no cinema, na praia, o sexo maluco... eu começo a rir sozinho."

    if julia_namoro:

        "Não é à toa que eu decidi namorar com ela."
    else:


        "Mas a gente sempre foi só amigos... apesar de quê... a gente já se envolveu em cada uma."

        "Não temos nada sério... pelo menos até hoje..."

    "E agora... se ela tá deixando pra trás esse lance de sair com todos... ela pode ser a parceira perfeita."

    "Eu posso finalmente ter uma namorada real. Uma garota normal, que não tá envolvida com a máfia, que não tem problemas imensos."

    "Só viver um amor delicioso, mas cotidiano, com uma pessoa que me curte e tá se esforçando pra ficar comigo."

    mc "[g]..."

    g "Você é o único que aguentou ficar do meu lado até o fim, [mc]..."

    g "Por favor... fala que você quer ficar comigo."

    "Eu tenho que dar uma resposta pra ela."

    "Se as coisas derem certo entre a gente... ela pode ser a garota que eu vou viver pro resto da vida."

    "E se der errado... a gente pode se separar também. Não precisamos ficar juntos pra sempre."

    "Ela parece super afim... e eu nunca vi ela tão séria e vulnerável assim."

    label j8_decisao_namoro:

        pass

    "Será que vale a pena acreditar que ela mudou?"

    menu:

        "Eu acredito em você. E quero que você seja minha namorada." if not julia_namoro:

            "Mesmo com ela sem roupa no quarto do Caio... eu vou acreditar na Júlia e tentar ter uma relação séria com ela?"

            "A chance disso dar errado é gigante. Eu sei como ela é... e pode ser que tenha uma grande decepção me esperando..."

            "Eu vou mesmo namorar sério com ela? Pelo menos tentar?"

            menu:
                "Eu tenho certeza. É isso que eu quero.":


                    $ julia_namoro = True

                    "Eu confio na Júlia. E eu quero ela."
                "Eu preciso pensar melhor":


                    "Essa não é uma decisão fácil. Eu preciso pensar melhor."

                    jump j8_decisao_namoro

        "Eu acredito em você. E vou continuar sendo seu namorado." if julia_namoro:

            "Mesmo com ela sem roupa no quarto do Caio... eu vou acreditar na Júlia e tentar ter uma relação séria com ela?"

            "A chance disso dar errado é gigante. Eu sei como ela é... e pode ser que tenha uma grande decepção me esperando..."

            "Eu vou mesmo namorar sério com ela? Pelo menos tentar?"

            menu:
                "Eu tenho certeza. É isso que eu quero.":


                    $ julia_namoro = True

                    "Eu confio na Júlia. E eu quero ela."
                "Eu preciso pensar melhor":


                    "Essa não é uma decisão fácil. Eu preciso pensar melhor."

                    jump j8_decisao_namoro

        "Eu acredito. E eu vou te ajudar, mas como amigo." if not julia_namoro:

            "Mesmo com ela sem roupa no quarto do Caio... eu vou acreditar na Júlia? Continuar sendo o amigo que ela precisa?"

            "A chance de eu acabar fodido igual a Carol e a Sayuri é imensa... além de que eu vou comprar briga com o Caio."

            "E o Caio não é só o Caio... agora eu sei que ele faz parte daquela maldito grupo..."

            "É esse caminho mesmo que eu vou seguir?"

            menu:
                "Eu tenho certeza. É isso que eu quero.":


                    "Sim. Eu confio nela e quero que ela seja feliz. Eu sou o último amigo que ela tem."
                "Eu preciso pensar melhor":


                    "Essa não é uma decisão fácil. Eu preciso pensar melhor."

                    jump j8_decisao_namoro
        "Quem acreditaria em você nessas condições? Você tá sozinha no mundo.":














            scene black with dissolve

            scene j8_new37 with Dissolve(1.0)

            pause

            $ j8_negou = True
            $ julia_namoro = False

            mc "Não dá, Jú."

            mc "Olha pra você... sem roupa na cama do cara que abusa de você."

            mc "Por mais complicada que seja sua cabeça, eu tenho que pensar em mim também. Na minha saúde."

            g "A-ah..."

            mc "Olha como a Carol e a Sayuri desistiram de você. E é isso que eu vou fazer também."

            mc "Eu não acho que tu tá errada. Eu acho que você vive a vida do jeito que você quer."

            mc "Quem sou eu pra falar com quem você deve ou não andar? Ou fazer ou não fazer?"

            mc "Eu entrego segredos de amigos pra ganhar dinheiro..."

            mc "A única coisa que você precisa é tá com pessoas que pensam como você."

            g "E você..."

            mc "Não... eu não penso como você. Eu quero uma vida bacana, mas sem essa loucura. Sem pessoas tóxicas."

            g "Entendi... obrigada por ser legal comigo até o fim."

            mc "Eu sempre vou ser legal com você. E eu vou torcer pra você encontrar seu caminho."

            mc "Olha pra sua irmã. A Sayuri vivia com medo de falar com as pessoas. Praticamente paralizada, mesmo tendo tanto sucesso."

            mc "Ela superou aquela necessidade da aprovação da Mestra e seguiu seu próprio caminho. Mesmo eu não concordando totalmente."

            g "É verdade... ela encontrou o caminho dela."

            g "Vendo como você, a mana e a Carol tomarem o rumo que vocês querem... eu também vou juntar força pra seguir o meu."

            mc "Quem sabe no futuro a gente não possa se 'conhecer' de novo?"

            g "Isso seria incrível..."

            g "Eu vou começar me afastando das pessoas que me fazem mal."

            mc "O Caio?"

            g "Todos aqui. Mesmo sendo bacana, eu não consigo entender a Mari. Eu tenho um pouco de medo dela."

            mc "Sério? Haha..."

            g "As coisas que ela me fala às vezes... não sei se ela ama ou odeia o Caio."

            mc "Não é igual você?"

            g "Não. Eu odeio o Caio do fundo do meu coração, mas às vezes eu quero trepar com ele. É igual um vício."

            g "Agora, a Mari... eu sinto que é mais pensado. Às vezes eu sinto que ela tá planejando alguma coisa..."

            g "Igual, às vezes ela fala pra eu dar uma chance pro Caio. Que ele não é tão ruim. Mas depois... sei lá..."

            mc "Hm? Estranho... Falando assim... dá um pouco de medo mesmo haha..."

            g "Por isso eu vou me afastar de todas essas pessoas. E quem sabe um dia a gente não se encontra de novo?"

            mc "Quem sabe?"

            g "E faz uma baguncinha?"

            mc "Haha... só você, Júlia... você tá indo? Eu tô vazando."

            g "Não... eu vou resolver minha vida... só que depois."

            scene black with dissolve

            scene j8_new37 with Dissolve(1.0)

            g "Agora acho que eu vou dormir mais um pouco."

            mc "Tá bom... boa sorte, garota!"

            g "Falou, mano!"

            scene black with dissolve

            scene j8_new27 with Dissolve(1.0)

            "Agora deixa eu sair daqui antes que o Caio me pegue e eu me foda."

            scene black with dissolve

            pause 1.0

            "Agora é só sair pela sala."

            scene j8_new42 with vpunch

            caio "EI!"

            caio "Que merda é essa?!"

            "Fodeu!"

            caio "Por isso que você tava me enrolando, né, Mari?!"

            mari "E-eu!"

            menu:
                "Eu só fui no banheiro.":


                    mc "Não precisa criar uma tempestade em copo d'água. Eu só tava mijando."

                    caio "Como assim, cara?!"
                "A Mari não tem nada com isso!":


                    mc "A Mari não fez nada!"

                    caio "Eu vou falar com essa vaca depois."

            caio "Eu quero saber que MERDA TÁ ACONTECENDO AQUI?!"

            mc "Nada. Eu fui mijar, encontrei a Júlia e falei pra ela que nossa amizade acabou."

            scene black with dissolve

            scene j8_new48 with Dissolve(1.0)

            caio "Tá falando sério, cara?!"

            mc "Tô."

            caio "Eu sabia que você tinha potencial!"

            mc "Calma que eu não tô redpilado, não, viu? Eu só tô cansado do jeito dela mesmo."

            caio "Você não tá ainda! Mas já começou bem colocando ela no lugarzinho dela!"

            caio "A gente precisa comemorar!"

            "Não gosto de ver o Caio feliz desse jeito... não é porque eu larguei da Júlia que eu curto esse filhinho de papai."

            "Mas é bom ter ele do meu lado. A última coisa que eu preciso é de um mafioso na praça do polvo me esperando passar..."

            mc "Eu tô vazando. E vocês ficam bem aí."

            mari "[mc]... mas a Jú..."

            mc "Desculpa, Mari. Eu cansei. Espero que você saiba o que você tá fazendo."

            mari "Eu... tudo bem... até outra vez."

            mc "Acho que a gente não vai se falar de novo. Boa vida pra vocês dois."

            mari "Vamos ver..."

            caio "Ele tá meio pra baixo, Mari! Mas amanhã ele tá aí! Tenho certeza!"

            "Por que o jeito que ele fala me deixa tão puto?"

            mc "Falou."

            scene black with Dissolve(3.0)

            pause 2.0

            $ tempo = 1

            jump call_cidade



    mc "Pode me chamar de beta... de ingênuo... de tonto... de palerma..."

    g "Hm?"

    mc "Mas eu acredito. Eu acredito que as pessoas podem mudar."





    scene black with dissolve

    scene j8_new37 with Dissolve(1.0)

    pause

    mc "Quando eu cheguei aqui nessa cidade pra estudar jornalismo na facul que você tá agora, eu tava cheio de sonhos."

    mc "Eu pensava que jornalismo era descobrir a verdade e fazer algo de bom pras pessoas."

    mc "Olha agora. Acabei virando um paparazzo que ganha pra descobrir fofoca de famosos."

    mc "Eu sinto que tudo o que eu vi e vivi mudou muito o que eu era, o que eu pensava sobre a cidade."

    g "Mas continua sendo o boboca de sempre."

    mc "Olha pra sua irmã. A Sayuri vivia com medo de falar com as pessoas. Praticamente paralizada, mesmo tendo tanto sucesso."

    mc "E agora... nos últimos eventos que a gente viveu na Cidade Chinesa, ela é praticamente outra pessoa."

    mc "Ela superou aquela necessidade da aprovação da Mestra e seguiu seu próprio caminho. Mesmo eu não concordando totalmente."

    g "A mana mudou muito mesmo. Ela parece bem mais decidida... e parece mais feliz também, sabia?"

    g "A mana de antes nunca ia me dar um chute no pé igual ela me deu ontem..."

    mc "Se eu e a Sayuri podemos mudar... por que você não pode também?"

    g "Tá falando sério?! Você acredita em mim mesmo?!"

    mc "Por quê? Não devia acreditar?"

    g "C-claro que devia! É que... sabe..."

    scene j8_new38 with vpunch

    g "Acho que... nnghh... essa é a primeira vez... que alguém acredita em mim... nnngh..."

    mc "Você tem que parar de se fazer de vítima e mudar. Não coloque a culpa nos outros."

    g "Eu sei... idiota... eu tô chorando de feliz... nnghh..."

    mc "Alguma coisa me diz que eu vou me arrepender, mas... você tem razão no que você disse ali."

    if julia_namoro:

        mc "E se você for a minha escolhida? E eu tô deixando você ir embora sem nem tentar?"

        g "Claro que eu sou... nnghh..."

    mc "Então bora ver onde isso vai dá. Eu tô acreditando em você. Não jogue minha confiança no lixo... de novo."

    g "Nnghhh!"

    g "Você falando assim... nnghh... me deixa... huhh..."

    mc "Feliz?"

    scene j8_new39 with hpunch

    g "Excitada..."

    if julia_namoro:

        mc "Ju-Júlia... eu também tô afim de trepar com você, mas olha onde a gente tá."
    else:


        mc "Júlia! Eu disse que sou seu amigo!"

        g "E amigos não podem trepar?!"

        mc "E ainda por cima... olha onde a gente tá."

    g "Foda-se... o Caio merece... que o troféuzinho dele dê pra outro homem na casa dele."

    g "Vai ser uma vitória e tanto pra você também, não vai? Me comer embaixo do teto dele."

    mc "É... com certeza tem um saborzinho..."

    g "Então cala a boca e me beija, delícia!"

    menu:
        "Vem aqui, safada!":


            mc "Como que eu vou falar 'não' pra melhor foda que existe?"

            g "Sabia, gato! Você é adora trepar comigo!"

            g "Vamo aproveitar que a gente tá na casa do idiota do Caio e ter o melhor sexo até hoje."

            mc "É perigoso, Ju. Melhor uma rapidinha."

            g "Se você não quer aproveitar TUDO o que eu quero te dar..."

            label ju8_premium1:

                pass

            menu:
                "Tá bom. Vamos transar como a gente merece.":


                    if not premium:

                        call mensagem_premium

                        jump ju8_premium1

                    g "Assim que eu gosto. Tira essa roupa."



                    scene black with dissolve

                    scene j8_premium8 with Dissolve(1.0)

                    pause

                    g "Quero começar te deixando bem duro só com minha boquinha tarada."

                    mc "Sua boquinha adora mamar, não adora?"

                    g "Todo mundo sabe que ela adora enfiar um pau na boca e chupar tudinho."

                    g "Gosto de caralho gostoso, igual o seu, [mc]."

                    mc "Vou fingir que eu acredito que meu pau é teu preferido."

                    if julia_namoro:

                        g "Pau de namorado tem um sabor diferente. Acho que é o amor."

                        mc "Haha... sei..."

                    mc "A-ah..."

                    g "Assustou, é? Eu não perco tempo quando colocam uma pica boa dessas na minha frente."

                    scene black with dissolve

                    scene j8_premium9 with Dissolve(1.0)

                    pause

                    g "Hmmm..."

                    g "Meu cu já tá piscando só de te lamber desse jeito."

                    mc "Hhmmm... eu disse que... ah... podia ir devagar, mas... nngh... não precisa judiar também?"

                    g "Deixa eu fazer o que eu quiser com esse caralhão."

                    g "Olha como meu buraquinho fica todo animado... hmmm... enquanto eu chupo..."

                    mc "Tô v-vendo... ah... esse bundão pra cima e pra baixo."

                    g "Ele tá só imaginando em você arrombando ele hoje."

                    mc "Vai querer no cuzinho?"

                    g "Talvez... nnghhh..."

                    menu:
                        "Para de enrolar e deixa eu te comer.":


                            mc "Cansei dessa boquinha, tô ansioso pra mais."
                        "Continua mamando assim...":


                            mc "Tá bom assim... ah... tô gostando..."

                            g "Tudo pra você, amor..."

                            scene black with dissolve

                            scene j8_premium10 with Dissolve(1.0)

                            pause

                            g "Ngghh... alguém tá gostando mesmo, hein?"

                            mc "Claro... ah... você tem a melhor mamada que eu já vi."

                            g "É a prática, gato... tem coisa que só a experiência resolve."

                            mc "Haha... você não tem jeito..."

                            if julia_namoro:

                                g "Mas agora eu só vou usar com você. Acabou se dando bem, fala aí."

                            mc "Nnnghhhh... é m-muito bom tá na boca de alguém que sabe o que tá fazendo."

                            g "Uhum..."

                            scene black with dissolve

                            scene j8_premium11 with Dissolve(1.0)

                            pause

                            mc "Ahhh... tá me engolindo inteiro, safada!"

                            g "Você não viu nada... hmm... tudo do melhor pra você, gostoso."

                            g "Quero você com o pau bem deslizando pra poder me comer."

                            mc "Se você quer sentir ele te comendo, m-melhor você parar ou eu não aguento."

                            g "Hmmm... tá gostoso desse jeito mesmo?"

                            mc "M-muito!"

                    g "Tá bom, tu vai meter. Nas eu vou querer atrás."

                    mc "Eu sabia. Desde que você começou a falar do rabinho eu sabia que você queria."

                    g "Quero fazer uma coisa bem safada aqui nessa cama."

                    mc "Então vai. Vou te dar o que você quer."

                    g "C-calma! Primeiro eu quero ficar bem molhadinha."

                    g "Deita aqui que eu vou te guiar."

                    menu:
                        "Pode deixar. Vou deixar minha mina pronta pra mim.":


                            mc "Quero você bem cremosinha pra mim."

                            g "Ain... assim que é bom... Vem cá."

                            scene black with dissolve

                            scene j8_premium12 with Dissolve(1.0)

                            pause

                            g "Eu adoro quando lambem minha buceta assim comigo por cima."

                            mc "Você é uma safadam isso sim."

                            g "Sou mesmo! Eu adoro ser chupada desse jeito! Hnnn e você faz tão gostoso!"

                            g "Usa essa língua que tá indo bom demais!"

                            mc "{i}Slhup! Slhep!{/i}"

                            g "Desse jeito! Eu amo quando fazem assim! Nnghhhh!"

                            g "Com vontade, caralho! Hmmm!"

                            scene black with dissolve

                            scene j8_premium13 with Dissolve(1.0)

                            pause

                            g "Assim mesmo!!! Com vontade!!!"

                            g "Aahnnn! AAHHHNNN!"

                            g "Assim mesmo! Igual homem, [mc]!!"

                            mc "TOMA!"

                            g "AAiinnnn! Tá dentro de mim essa língua fodida!"

                            g "Vai tomar todo meu melzinho!"

                            mc "Tomo tudo, gostosa."

                            g "Nnghhh! Fico tão excitada de você se lambuzar todo comigo!"

                            g "Agora no cu! Lambe meu rabinho!"

                            menu:
                                "Prefiro enfiar meu pau nele.":


                                    mc "Vai tomar é meu pau agora!"

                                    g "Mas assim?! Molha ele!"

                                    mc "Eu sei que tu aguenta só com a saliva do meu pau!"

                                    scene black with hpunch

                                    g "Ai!"

                                    scene j8_premium14 with vpunch

                                    pause
                                "Senta aqui. Deixa eu preparar esse cuzinho.":


                                    mc "Vem."

                                    g "Assim que eu gosto de ouvir. Por isso é tão bom transar com você, filho da puta."

                                    scene black with dissolve

                                    scene j8_premium15 with Dissolve(1.0)

                                    pause

                                    g "Hmmm! Assim mesmo! Passa do grelinho e vai até o cuzinho! Ai ai!"

                                    g "Como você lambe gostoso! Nnghhh!"

                                    mc "Vou deixar ele protinho pra me receber."

                                    g "Sim... esse cuzinho adora receber carinho... ele aprendeu como retribuir."

                                    g "Toda vez que lambem ele assim ele não aguenta, ele precisa agradecer o pau de quem lambeu."

                                    mc "A é? Que rabinho mais agradecido."

                                    g "Simm.... ai... tá muito bom, [mc]!"

                                    scene black with dissolve

                                    scene j8_premium16 with Dissolve(1.0)

                                    pause

                                    g "Se continuar assim eu vou acabar gozando de verdade, safado!"

                                    mc "Vai gozar só com meu oral, cachorra?"

                                    g "Essa cadelinha gosta muito de uma chupada! Ela gosta muito mesmo!"

                                    mc "Tô vendo!"

                                    g "Assim, gato! Puta que pariu!"

                                    if julia_namoro:

                                        g "Se nosso namoro vai ser assim, eu tô feita!"
                                    else:


                                        g "Se nossa amizade vai ser assim, eu tô feita!"

                                    g "É tudo o que eu quero!"

                                    g "Aaiinnnnnn!"

                                    g "Vem! Eu não aguento mais! Eu quero seu caralho agora!"

                                    mc "Não via a hora de foder esse cuzinho."

                                    g "Ele tá pronto pra você, desgraçado. Arromba ele!"

                                    scene black with dissolve

                                    scene j8_premium14 with Dissolve(1.0)

                                    pause

                                    g "Hmmmm!"

                                    mc "Tá entrando gostoso!"

                                    g "Tá! Agora mete!"

                                    scene black with hpunch

                                    g "Ai!"

                                    scene j8_premium14 with vpunch

                                    pause
                        "Vai guiar nada. Cai logo nessa cama que eu vou te pegar, danada!":


                            mc "Eu sei que tu aguenta só com a saliva do meu pau!"

                            scene black with hpunch

                            g "Ai!"

                            scene j8_premium14 with vpunch

                            pause

                            g "Vai me arrombar desse jeito mesmo, é?!"

                            mc "As coisas vão ser assim hoje. Eu mando!"

                            g "Ai! Quem é esse [mc]?! Só toma cuidado."

                    mc "Toma!"

                    g "Ngnhhhh!"

                    g "Toma cuidado com o rabinho da sua mina, caralho."

                    mc "Vou fazer bem gostosinho pra você. Do jeito que você gosta, delícia."

                    scene black with dissolve

                    scene j8_premium17 with Dissolve(1.0)

                    pause

                    g "Nnnghh... uhummhhggg! Tá fazendo! Assim mesmo!"

                    mc "Mexendo gostoso pra minha gatinha gemer."

                    g "Eu gemo! Nngh! Gemo pra você, safado! Agnnnn!"

                    g "Faz eu gozar só com a sua pica no meu rabo!"

                    g "Vai fodendo sua piranha!"

                    mc "Hmmm! Como! Com gosto!"

                    g "Assim mesmo! Arromba ele, arromba! Arromba como ele nunca foi arrombado!"

                    scene black with dissolve

                    scene j8_premium18 with Dissolve(1.0)

                    pause

                    mc "Ai! Caralho! Teu fogo não acaba!"

                    g "Não! Ainn! Ele é infinito! Preciso de muita pica mesmo! Nnghhhh!"

                    mc "Vou apagar esse fogo todo agora! Nnnghh!"

                    g "Hnmnnnnggg! Assim! Com ódio!"

                    g "É com você que eu quero gozar, [mc]!"

                    g "Tudo que a gente viveu! Tudo o que você fez! Nngh! É pra você que eu mais gosto de dar!"

                    mc "Você vai ser minha, porra!"

                    g "Vou!"

                    if julia_namoro:

                        g "Agora eu vou ser sua! Só sua!"

                        g "A gente tá fazendo amor! Não é só sexo! É amor, né?!"

                        menu:
                            "É amor!":


                                pass

                        mc "É amor! Isso é amor de verdade!"

                        g "Simmmm!"

                    scene black with dissolve

                    scene j8_premium19 with Dissolve(1.0)

                    pause

                    g "Caralho! Você vai me fazer gozar mesmo!"

                    g "Nnnghhhhh! Eu gosto de você, [mc]! Agnnn! Eu gosto!"

                    mc "Vou gozar em você! Na tua bunda!"

                    g "Me enche de porra, caralho! Nnghhhh!"

                    g "Gozaaaa em miimmmmmm!"

                    g "NNGHHHHHH!"

                    mc "AAAAHHHHH DELÍCIAAA!!!"

                    scene j8_premium20 with vpunch

                    pause

                    mc "Aahh... ah... enchi tua bunda..."

                    g "Hmmmm... tô sentindo..."

                    g "Porra... muita porra... vazando..."
                "Dar uma trepada rápida e correr da casa":


                    mc "A gente não tem tempo."

                    scene black with dissolve

                    pause 2.0

                    g "Nnghh! Aahhh!"

                    mc "Eu esqueci como você mexe gostoso! Você é a melhor trepando, Jú!"

                    g "Nnghh! Se aquele filho da puta soubesse que você tá me comendo aqui! Aahh!"

                    mc "Então vai! Vamo fazer esse desgraçado ouvir!"

                    if julia_namoro:

                        g "Aahh! Assim! Mete gostoso na sua namorada! Aaaiin!"
                    else:


                        g "Aahh! Assim! Mete gostoso na sua amiga! Aaaiin!"

                    g "A bucetinha dela é sua, gostoso! Aahhhnnn!"

                    mc "Aahhhhh!"

                    g "Nnghhhhh!"

            mc "C-caralho... o que a gente fez?"

            mc "A Mari tá segurando o Caio, mas... acho que a gente exagerou..."

            g "Nem demorou tanto assim, vai.... hmmm... não valeu a pena?"

            mc "Depende. O sexo foi incrível, mas se o Caio atirar em nós."

            g "Para de ter medo... ele é um bundão."

            mc "Bora se arrumar e vamo."
        "A gente comemora em casa.":


            mc "A gente não precisa disso. A gente vai trepar muito lá em casa."

            scene j8_new40 with Dissolve(1.0)

            pause

            g "Sem graça. Eu queria tanto sentir esse pauzão na minha bucetinha molhada..."

            mc "Não fala assim, safada..."

    g "Vamo logo pra casa então..."

    scene black with dissolve

    scene j8_new41 with Dissolve(1.0)

    pause

    if julia_namoro:

        g "Por que essa pressa? Agora que a gente tá junto de verdade?!"
    else:


        g "Por que essa pressa?"

    mc "O Caio vai fazer um furdúncio se ele ver eu tirando você dele."

    g "Quer dizer que você quer salvar a princesa sem lutar com o bandido?"

    mc "Exatamente!"

    g "Que romântico..."

    mc "Isso aqui é vida real, Júlia. Acorda. A Mari disse que não sabe o que ele pode fazer."

    g "Isso é... ele pode ser bem... extremo... às vezes..."

    mc "Vem. Antes que ele apareça e tente alguma doideira{nw}"

    scene j8_new42 with hpunch

    caio "Que merda é essa?!"

    "Fodeu!"

    caio "Por isso que você tava me enrolando, né, Mari?!"

    mari "E-eu!"

    menu:
        "Sem confusão. Tamo de saída!":


            mc "A gente tá vazando, Caio. Não precisa criar uma tempestade em copo d'água!"

            caio "Você não decide nada aqui, não, imbecil!"
        "A Mari não tem nada com isso!":


            mc "A Mari não fez nada!"

            caio "Eu vou falar com essa vaca depois."

    caio "Eu quero saber que MERDA TÁ ACONTECENDO AQUI?!"

    mari "C-calma, Caio... não vai ficar louco por causa disso!"

    caio "Eu pensei que você fosse tomar a red pill, caralho?! E agora roubando minha mina assim?!"

    mc "!"

    g "Quem disse que eu sou sua mina, babaca?!"

    caio "E você cala a boca também, vadia! Trocando de homem igual troca de calcinha!"

    mc "Não fala dela assim. A Júlia decidiu que acabou. Respeita ela!"

    if julia_namoro:

        mc "E eu não tô roubando nada. Nós somos só amigos. Mas você faz mal pra ela."

        mc "Só deixa ela em paz, caralho!"

    caio "'Respeita ela'... Você acha que uma puta dessas merece respeito?! Você é gayzinho, é?!"

    caio "Mulheres devassas igual essa aí não merecem porra nenhuma!"

    mc "E homens que ficam com várias, igual você? Merecem o quê? Porra nenhuma então também!"

    caio "É diferente! Homens e mulheres são diferentes! A sociedade aceita que o homem faça isso!"

    mc "A sociedade é uma bosta, cara! Essa teoria idiota que tu criou pra justificar essas merdas que não merece porra nenhuma!"

    caio "Velho! Você só caiu na dela! Eu sei que no fundo você não quer brigar comigo!"

    caio "Você sabe quem eu sou! Você sabe quem meu pai é! Eu posso te ajudar!"

    caio "Não jogue fora tudo o que você pode conseguir com a ajuda do {b}Grupo{/b}!"

    mc "Eu sei o que você tá me oferecendo..."

    g "[mc]..."

    mari "..."

    caio "E então? O que vai ser?! De que lado você vai ficar, hein?!"

    "Ele tá me oferecendo o poder do grupo que controla a ilha..."

    "As pessoas que conseguiram trabalho pro Téo, pra Mari, que garantem que o Caio faça o que quer."

    "Eles comandam o Novo Banco Central com o Gevanni... e têm coisa até com o prefeito..."

    label j8_decisao2:

        pass

    "Eu vou querer brigar com eles pra poder ficar com a Júlia? Ou vou sair fora?"

    "Deixar ela com ele... pra sempre... é isso que eu vou fazer?"

    menu:
        "Desculpa, Júlia. Mas eu não quero briga com essas pessoas.":














            $ j8_negou = True
            $ julia_namoro = False

            "O Caio tem razão... é complicado demais enfrentar essas pessoas."

            if julia_namoro:

                "Se eu tiver que desistir do meu namoro com a Júlia pra gente não morrer... não tem muito o que eu decidir."

                "A gente não vai namorar, mas pelo menos eu sei que ela vai tá bem."

            mc "Desculpa, Júlia... mas você se meteu num buraco fundo demais pra eu te tirar."

            scene black with dissolve

            scene j8_new43 with Dissolve(1.0)

            g "Q-quê? Você tá com medo desse idiota?!"

            caio "Não é medo! Você só não vale o esforço, entendeu?!"

            mc "Você sabe que eu fiz de tudo pra você, mas essas pessoas não são brincadeira, Júlia. Só dá o fora."

            g "Tá falando sério?! Esse idiota não vale nada, [mc]!"

            mc "Júlia! Você não sabe o que eu sei! Só dá o fora!"

            g "IDIOTA!"

            play sound som_35_passos

            scene black with dissolve

            scene j8_new48 with Dissolve(1.0)

            mc "Pronto. Feliz? Só deixa eu e ela em paz, caralho."

            caio "Tá falando sério, cara?!"

            mc "Tô."

            caio "Eu sabia que você tinha potencial!"

            mc "Nada de potencial. Eu só quero que você deixe ela em paz."

            mc "Eu não tô redpilado porra nenhuma. Eu só quero ficar longe disso."

            caio "Você não tá ainda! Mas já começou bem colocando ela no lugarzinho dela!"

            caio "A gente precisa comemorar!"

            "Não gosto de ver o Caio feliz desse jeito... não é porque eu larguei da Júlia que eu curto esse filhinho de papai."

            "Mas é bom ter ele do meu lado. A última coisa que eu preciso é de um mafioso na praça do polvo me esperando passar..."

            mc "Eu tô vazando. E vocês ficam bem aí."

            mari "[mc]... mas a Jú..."

            mc "Desculpa, Mari. Eu cansei. Espero que você saiba o que você tá fazendo."

            mari "Eu... tudo bem... até outra vez."

            mc "Acho que a gente não vai se falar de novo. Boa vida pra vocês dois."

            mari "Vamos ver..."

            caio "Ele tá meio pra baixo, Mari! Mas amanhã ele tá aí! Tenho certeza!"

            "Por que o jeito que ele fala me deixa tão puto?"

            mc "Falou."

            scene black with Dissolve(3.0)

            pause 2.0

            $ tempo = 1

            jump call_cidade
        "Eu não tenho medo de vocês, idiota!":


            "Eu vou mesmo comprar briga com essas pessoas? Eu posso muito bem acabar morto!"

            menu:
                "Sim. Eu não tenho medo deles.":


                    "Eles que vão pra puta que os pariu!"
                "Calma... pensa com calma.":


                    "Essa não é uma decisão fácil. Eu preciso pensar com calma."

                    jump j8_decisao2

    mc "Eu não quero saber do seu grupo... eu vim aqui pela Júlia. Mas é ela que tem que decidir."

    scene black with dissolve

    scene j8_new43 with Dissolve(1.0)

    pause

    mc "Júlia... se você tiver pronta pra deixar esse palerma pra sempre... eu tô pronto pra te ajudar."

    g "Pra sempre..."

    caio "Pra sempre, Júlia... nunca mais..."

    g "Nnghh..."

    "Júlia! Essa é sua chance de escapar dessa vida pra sempre! Força!"

    mari "Jú..."

    g "Caio... você... no fundo... a gente sempre esteve juntos..."

    g "... mas a gente só fez mal um pro outro! A gente se odeia! E eu não quero mais isso!"

    g "Você nunca mais vai me ver! Vem, [mc]!"

    caio "Onde que você pensa que tá indo, puta?!"

    g "Acabou, Caio! Eu não preciso mais dessa merda tóxica que a gente tinha!"

    caio "HAHAHAHA!"

    caio "Quantas vezes você saiu assim toda mandona, hein?!"

    caio "Isso até você perceber que eu sou o único que te aguenta, sua fodida!"

    g "Você... que é o fodido..."

    mc "Não escuta ele, Júlia. Você não precisa mais disso."

    caio "HAHAHA! Esse beta idiota acreditou em você mesmo?! Essa fachada aí?!"

    caio "E eu achando que você tinha potencial, babaca!"

    caio "Você nasceu pra ser trouxa de mulher, seu idiota!"

    mc "Fale o que quiser, Caio. Eu não tenho a cabeça fraca como esses idiotas que você convive."

    caio "Filho da puta! Ela vai voltar! Você vai ver! Na primeira briguinha de vocês!"

    caio "Você sabe disso, sua puta! Você precisa de mim!"

    g "Ghhh... c-cala a boca."

    mc "Vem, Jú. Falou, Caio."

    caio "Você só sai quando eu mando! Você ainda vai ser minha, sua safada! Eu sei que vai!"

    g "..."

    scene black with dissolve

    caio "Nem que eu tenha que matar TODOS OS OUTROS HOMENS!!!"

    window hide

    pause 2.0

    scene j8_new44 with Dissolve(1.0)

    pause

    "Eu sei que não vai ser fácil pra ela."

    "Terminar desse jeito algo que começou há tantos anos... é igual tirar um bandeide puxando rápido."

    "Vai doer... mas se a ferida tá curada, logo logo fica bem. E eu vou tá aqui pra ajudar nessa recuperação."

    mc "Vamos esquecer o que ficou pra trás e construir nossa história agora."

    g "Sim... nngh..."

    g "Eu quero... quero deixar isso pra trás."

    mc "Isso. É hora de ir adiante."

    g "Só que eu não posso só esquecer o que eu fiz ainda... eu tenho que resolver umas coisas, [mc]."

    mc "Tá falando sério? A gente pode só deixar isso. Esquecer!"

    g "Não... eu preciso resolver isso de vez."

    mc "[g]... você acha que essas pessoas merecem? Voltar nisso é perigoso."

    g "É uma coisa que eu tenho que fazer! Eu só preciso de uns dias!"

    menu:
        "Pode ir. Eu confio em você.":


            pass

    mc "Se você acha que precisa... eu tô contigo."

    g "Obrigada. É uma coisa que eu tenho que fazer sozinha. Depois que eu te ligo, tá?"

    mc "Tá..."

    scene black with dissolve

    "O que a Júlia vai fazer agora?"

    scene black with dissolve

    pause 2.0

    scene ape_pensando with Dissolve(1.0)

    pause

    "O que a Júlia pode querer fazer agora?"

    "Eu decidi acreditar nela... eu preciso confiar na Jú. Quando ela tiver pronta. Ela vai ligar."

    scene black with Dissolve(3.0)

    pause 2.0

    scene ape_pensando with Dissolve(1.0)

    "Quantos dias já passaram? E nada dela ligar..."

    "O que será que aconteceu? Será que eu não devia ter deixado ela voltar?"

    "Júlia..."

    window hide

    pause 2.0

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trr... trrr..."

    "Hm?"

    scene black with dissolve

    scene ape_celular_falando with Dissolve(1.0)

    g "Oi, gato!"

    mc "Júlia!"

    g "Bora pro cinema?!"

    mc "Claro!"

    scene black with dissolve

    scene j8_new45 with Dissolve(1.0)

    pause

    if not julia_namoro:

        mc "Não precisa ficar assim..."

        g "Eu só preciso de um carinho... de amigos... prometo."

        mc "Tá bom..."

    mc "Terminou o que tinha que fazer?"

    g "Com certeza! Mas não adianta perguntar! Não vou contar!"

    mc "Não faço questão de saber..."

    g "Eiiii!"

    "É mentira, claro... eu quero saber... mas melhor deixar ela contar quando quiser."

    g "Agora bora se pegar lá dentro!"

    if not julia_namoro:

        mc "Júlia... amizade, lembra?"

        g "Eu sei!!!"

        "E nossa amizade continuou assim. De vez em quando a gente saía."

        "Ia no cinema, na praia... e claro que sempre que dava ela tentava vir pra cima de mim."
    else:


        "E assim nossos dias têm sido divertidos pra caramba!"

        "A gente vai no cinema, na praia, igual eu tinha imaginado..."

    g "E se a gente sair daqui e for transar lá no vestiário da faculdade?"

    mc "Por que lá?"

    g "Por que você quer saber?! Porque eu tô com vontade, caramba!"

    mc "Hahaha!"

    menu:
        "Claro. Bora transar lá.":


            if julia_namoro:

                mc "Se minha princesa tá afim de dar lá na faculdade, eu só posso aceitar."
            else:


                mc "Amizade colorida, né? O que eu posso falar?"

            g "Assim, sim! Eu já tô toda meladinha, [mc]..."

            mc "Então vamo logo antes que eu tenha que andar até lá duro!"

            g "Hmm..."

            scene black with dissolve

            scene j8_new46 with Dissolve(1.0)

            pause

            g "Ai! Que delícia!"

            mc "Aahh!"

            g "Transar com você é diferente! Aahh!"

            mc "Certeza que não é o medo de ser pega!?"

            g "Aahhn! Eu queria ser pega! Nnghh!"

            mc "Você é impossível! Nnggh! Sua sorte é que tu é uma delícia!"

            g "AAHHH!!!"
        "Hoje a gente assiste o filme.":


            mc "Hoje não. Hoje a gente vai ver o filme."

            g "Tudo bem... você pode me comer lá dentro também."

            mc "Júlia..."

    if julia_namoro:

        "E, obviamente, tamo transando pra caralho. O tesão infinito da Júlia é quase impossível de saciar."

        "Eu tô me esforçando. Só espero dar conta dela... se minhas bolas não secarem antes."

    scene black with Dissolve(3.0)

    pause

    scene j8_new47 with Dissolve(1.0)

    pause

    if julia_namoro:

        "Com o tempo a gente foi ficando cada vez mais juntos..."

        "Parece que ela se tornou minha vida e eu me tornei a vida dela. A gente maratona muita séria, transa, sai juntos."

        "O trabalho ficou em segundo plano... e aqueles rolos todos que eu tinha me metido... eu fui deixando de lado."

        "Minha vida foi ficando normal... de uma forma que ela nunca tinha sido desde que eu tinha mudado pra ilha."

        "Máfia... prefeito... escravidão... polícia mundial... escândalos... conspirações..."

        "Não sei como... mas parecia que mais nada disso me encontrava."

        "Fico até pensando agora... se não era eu que procurava esse monte de desgraça."

        "Eu parei de procurar aquele pessoal doido, e a Júlia até hoje nunca aprontou. Pelo menos eu não vi nada."

        "Até hoje eu não sei se ela transou ou não com o Caio quando encontrei ela na cama de lingerie."

        "E nem o que ela foi fazer aqueles dias... até hoje ela não me contou."

        "Mas, independente disso, os meses passaram... e... simples assim... a gente foi sendo feliz."

        "Até quando isso vai durar? Sei lá... eu nem sei mais se a gente tá 'tentando' ou se as coisas só deram certo."

        "Só que... se isso durar por mais um tempo... eu não ia reclamar de viver assim."

        "Uma vida feliz do lado de uma pessoa que me faz bem. Não tinha mais nada que eu podia pedir."
    else:


        "A gente tinha nossa amizade... e a Júlia parecia mais feliz do que nunca."

        "Eu tô orgulhoso dela ter superado aquela fase. Pelo menos é o que ela me fala. E eu acredito nela."

        "Não foi fácil, mas ela conseguiu."

    "O único problema é o Caio..."

    "Ele tá desaparecido... mas por quanto tempo?"

    "O filho da puta não tem jeito de que só vai desaparecer e desistir do brinquedinho dele."

    "Alguma coisa me diz que que tirar a Júlia dele não foi uma boa ideia..."

    scene black with Dissolve(3.0)

    pause 2.0

    $ tempo = 1

    jump call_cidade

label julia_evento8_parte2:

    $ estou_na_cidade = False

    $ julia_v8 = "parte2"

    if julia_namoro and not j8_negou:

        "Meu namoro com a Júlia tá dando tudo de bom!"

        "Eu sabia que ia ser uma doideira, mas a gente se pega TODO DIA!"

        "Não tô conseguindo fazer mais nada... nem sei a última vez que eu peguei uma pauta."

        "Quer saber? Foda-se. Não quero pensar em trabalho nem nada! Deixa eu lugar pra ela!"

        play sound "audio/som_3_celular.mp3"

        "..."

        "Estranho... normalmente ela me atende."

        scene black with dissolve

        scene ape_celular_falando with Dissolve(1.0)

        play sound "audio/som_3_celular.mp3"

        "Smartphone" "{i}Trr trrr{/i}"

        "Ah! Olha ela aí."

        "Não? Não é o número dela."
    else:


        play sound "audio/som_3_celular.mp3"

        "Smartphone" "{i}Trr trrr{/i}"

    "Hmm... telefone desconhecido... Quem que é dessa vez?"

    scene black with dissolve

    scene ape_celular_falando with Dissolve(1.0)

    mc "Oi? É o [mc]."

    mari "Oi, [mc]! Aqui é a Mari."

    mc "Mari... como você tá? Faz tempo que a gente não se fala."

    mari "É..."

    mc "Que que foi? Sua voz tá diferente."

    mari "É o Caio."

    mc "Ele fez alguma coisa contigo? Pode falar!"

    mari "Ele tá meio estranho."

    if julia_namoro and not j8_negou:

        mari "Desde que você saiu com a Júlia, ele tá pior do que nunca."

        mc "Ele ficou irritadinho, é?"
    else:


        mc "Eu não tenho nada com a Júlia... e nem contigo. Então, foda-se. Eu tô fora."

    mc "Inclusive, você devia sair dessa também, Mari. Não importa o que você sente pelo Caio, ele não é um cara legal."

    mc "Você merece coisa melhor, garota. Sai dessa."

    mari "Eu tenho medo que ele faça alguma coisa com a Jú."

    if julia_namoro and not j8_negou:

        mc "Com a Júlia?! Como assim?!"
    else:


        mc "Eu não tenho mais nada com ela. Os dois são adultos."

        mari "Eu sei... e eu não quero te colocar num rolo sem motivo."

    mari "Eu liguei pra ele e ele não atendeu. E a Júlia também não me responde. Eu acho que os dois podem..."

    menu:

        "Não acredito que a Júlia! Não!" if julia_namoro and not j8_negou:

            "Por isso que ela não me..."

            mc "Só pode ser brincadeira! Você tá de tiração comigo, né?!"

            mari "E-eu..."

        "Eu não tenho nada com ela. Deixa ela se acabar." if j8_negou:

            mc "Haha... a Júlia tá foda."
        "Não acho que ela faria isso.":


            mc "Não, Mari. Impossível a Júlia fazer uma coisa dessas depois daquele dia na casa do Caio."

            mc "Eu sei que ela mudou. Ela me disse."

            mari "Mas... você tem certeza?"

    mari "Nem o Téo me respondeu quando eu liguei... Tenho medo que os dois acabem fazendo alguma coisa com ela."

    "Não seria a primeira vez... que saco... Júlia..."

    if julia_namoro and not j8_negou:

        mari "Vocês tão namorando... então pensei que..."

        mc "Entendi... tem razão. Valeu por me falar. E você tem alguma dica?"
    else:


        mc "E por que você tá me falando isso?"

        mari "Eu queria pedir sua ajuda..."

        mc "Com o quê exatamente?"

    mari "Você lembra do que eu te falei aquela noite no apê do Caio?"

    mc "Você disse alguma coisa sobre a pizzaria."

    mari "Será que você podia passar lá pra mim agora?"

    "O que a Mari tá tentando falar?"

    "Por um lado ela gosta do Caio, mas por outro ela parece tá sempre um pé atrás com ele."

    menu:

        "Claro que eu vou! Não posso deixar a Júlia!" if julia_namoro and not j8_negou:

            mc "Tá brincando? Mesmo que você não falasse nada, eu não vou deixar a Júlia lá!"

            mc "Eu preciso ter certeza que minha namorada não voltou a ser o que ela era antes!"

            mari "Entendo... mesmo você fazendo isso por vocês dois, eu tenho que agradecer."

            "E se ela voltou a se pegar com ele? O que eu faço?"
        "Tudo bem. Eu faço esse último favor pra você.":


            mc "Eu vou fazer a boa uma última vez pra você."
        "Não tem nada que eu possa dizer pra tu pular fora?":


            mc "Você parece sempre quase saindo de vez desse grupo. Será que não consigo dar esse empurrãozinho?"

            mari "Provavelmente tem... mas você não saberia o que é. Nem eu sei."

            mc "Mari..."

            mc "Se não tem como... "

    mari "Obrigada, [mc]... esse seu jeito fofo sempre me deu um calorzinho no peito."

    mari "Foi isso que me conquistou. E por isso que eu sempre fiquei na dúvida entre continuar aqui ou mudar de vida contigo."

    mari "Mas o que eu sinto por ele... não é racional."

    mari "Ao mesmo tempo que eu quero sair desse mar de lama, eu quero me afogar nele cada vez mais."

    mc "Nem falo mais nada. Como você diria, Mari... é complicado..."

    mari "Hehe... exatamente. É complicado."

    mc "Tudo bem. Eu não consigo saber exatamente qual é sua motivação aqui, mas eu vou dar uma olhada."

    mari "Boa sorte. E cuidado com ele."

    if julia_namoro and not j8_negou:

        mari "Do jeito que você levou a Jú aquela vez... ele vai tá puto contigo."

        mc "Se a Júlia mentiu pra mim... eu tô pouco me fodendo pro Caio."

        mari "Você já me provou que é grandinho. Toma cuidado, hein?"
    else:


        mari "Agora que você deixou a Júlia ele tá mais tranquilo. Mas o Caio é de lua."

    mc "Pode deixar que eu vou ficar bem. Só vou dar uma olhada se ele tá lá."

    mc "Daí te mando uma mensagem e você vê o que você faz. Não vou nem falar com ele."

    mari "Pra mim tá bom. Vou ficar esperando, tá?"

    mc "Tá bom. Já já te aviso."

    if julia_namoro and not j8_negou:

        if casa:

            scene ap sala with Dissolve(1.0)
        else:


            scene apartamento geral with Dissolve(1.0)

        "Eu tenho que ligar pra Júlia! Não pode ser verdade!"

        "..."

        if casa:

            scene ap sala with hpunch
        else:


            scene apartamento geral with hpunch

        mc "DROGA!!!"

        "Por que ela não tá atendendo?!"

    "Eu vou ter que ir pra aquela pizzaria."

    call locomocao

    scene cidade pizzaria with Dissolve(1.0)

    if julia_e4 == "caio":

        "Eu e o Caio conseguimos nos entender aquela vez que ele me deu a pauta e eu deixei a Jú pra eles."

        "Mas não dá pra negar que ele é um mimado."
    else:


        "O Caio é um insuportável."

        "E a Júlia sabe que esse cara só faz ela sofrer. Não é possível que ela tá aqui."

        "Se eu tivesse um jeito de tirar o Caio da jogada completamente."

        "Mas ele também tá de rolo com os italianos."

    "Hmm... pensando em tudo..."

    menu:
        "Sim, o Caio é um babaca mimado e merece sofrer":


            mc "O Caio é um desgraçado. Se eu tiver a chance, eu vou acabar com a vida dele. Completamente."
        "Não... no fundo, o Caio só é um cara que sabe o que quer":


            "Sendo sincero... acho que o Caio é determinado. E pessoas assim acabam parecendo babacas."

            "Mas ficar do lado dele pode ser melhor pra mim."
        "Mesmo sendo idiota, até que o Caio é meio gatinho":


            "Nada a ver pensar isso agora, mas... né... aquele jeito do Caio..."

            "Bem que podia... o que você tá pensando, [mc]?"

    "Bora ver se ele tá aqui mesmo."

    play sound som_35_passos

    scene black with dissolve

    scene pizzaria_out_noite with Dissolve(1.0)

    "Nada aqui... essa pizzaria parece sempre fazia... como que o Tony paga as contas, hein?"

    "Deve ser lavagem de dinheiro essa merda, isso sim."

    play sound som_35_passos

    scene black with dissolve

    scene pizzaria_interior with Dissolve(1.0)

    pause 2.0

    "Hmm... nada aqui também."

    "Garçom" "Boa noite! Desculpa a demora! Posso separar uma mesa para o senhor?"

    if julia_namoro and not j8_negou:

        mc "Você viu uma garota com dois coques?! Ruiva?!"

        "Garçom" "Desculpa, senhor... mas eu não tava atendendo. Era outro rapaz que devia..."

        mc "O Téo? Ele tá aqui?"
    else:


        mc "Ah! Obrigado... na verdade... você conhece um rapaz chamado Téo? Ele trabalha aqui."

    "Garçom" "Era pra ele ter vindo atender o senhor. Peço desculpas em nome dele e da Pizzaria Alighieri."

    mc "Ah. Então ele tá na hora de trabalho dele."

    "Garçom" "Sim. Era para ele estar atendendo... você conhece ele?"

    mc "Só um pouco. Mas... tinha que falar um negócio com ele."

    "Garçom" "Se quiser pode deixar um recado comigo. Ou jantar aqui. Logo logo ele deve estar aí."

    mc "Tô de boa. Deixa eu perguntar outra coisa. Você não viu outro rapaz. Da idade do Caio aqui?"

    mc "Cabelo curto, castanho claro, meio loiro, meio fortinho."

    "Garçom" "Agora que você falou, acho que eu conheço esse rapaz, sim. Eu já vi ele aqui outras vezes."

    menu:
        "Valeu. Era isso que eu queria saber.":


            mc "Beleza. Obrigado. Era só isso mesmo. Acho que vou nessa agora."
        "E o que normalmente ele faz aqui?":


            mc "E você já reparou o que ele faz? Ele come normal e tudo?"

            "Garçom" "Desculpa, mas nunca reparei. Ele nunca fica muito aqui, não."

            "Garçom" "Agora que você falou, eu acho que ele sempre pede pra ser atendido pelo Téo. Devem ser amigos."

            mc "Devem mesmo..."

    mc "Bom trabalho pra você."

    "Garçom" "E se quiser alguma coisa, pode me falar."

    mc "Pode deixar."

    play sound som_35_passos

    "Então o Caio vem... a suspeita da Mari tava certa. Realmente tem algum lance acontecendo aqui."

    if julia_namoro and not j8_negou:

        "Agora é saber se a Júlia veio pra cá também. E se o Téo foi com eles! Por isso ele não tá aqui!"

        "Merda..."

        "Tá me dando até um calafrio agora..."

        "E se tiver realmente alguma coisa a ver com a Júlia?"

        menu:
            "Eu não vou perdoar ela desta vez":


                "Eu tô decidido. Não vou dar outra chance pra ela."

                "Se ela quer bagunçar, se ela prefere trocar nossa relação por sexo, eu tô fora."
            "Ela tá tentando... ela merece outra chance":


                "Mesmo que ela esteja com eles... a Júlia não vai mudar de uma hora pra outra."

                "Eu tenho que entender ela. Contanto que ela demonstre que quer mudar de verdade."

        "Mas primeiro eu tenho que ver com meus próprios olhos. Não posso ficar com essa dúvida pra sempre."

    "Se eu tô lembrando certo, foi o Caio que arranjou o trampo pro Téo aqui. Por que ele faria isso? Ele não faz o tipo 'bonzinho'."

    "Deve ser pra ter o Téo na mão dele. Pra calar a boca. O Caio deve comprar as pessoas, igual o lance da pauta que ele me ofereceu."

    "É assim que ele mantém poder sobre o Téo, a Mari e vai saber quem mais. Com esses 'favores'."

    "Enfim, os dois não tão agora. Onde merda eles foram?"

    menu:
        "Vou dar uma olhada pela pizzaria antes de ir":


            "Melhor eu olhar bem em cada canto antes de desistir."

            play sound som_35_passos

            scene black with dissolve

            scene pizzaria_interior2 with Dissolve(1.0)

            pause 2.0

            "Hmm... parece que não tem nada aqui também."

            "O último lugar que falta é o banheiro... que seria o lugar ideal pra uma sadadeza..."

            "Era só o que me faltava..."
        "Só deixa eu ver o banheiro antes":


            "Deixa eu sair logo daqui e falar pra Mari que ele não tava."

            "Só vou dar uma olhada no banheiro..."

            play sound som_35_passos

            scene black with dissolve

            scene pizzaria_interior2 with Dissolve(1.0)

            pause 2.0

    "Hm? Parece que tô ouvindo uma coisa..."

    "???" "Xiiiuuu..."

    "???" "Não... você disse que a gente só ia convernsar..."



    "Eles tão falando baixo demais! Não dá pra saber quem é!"

    "Não é possível... E agora?!"

    menu:
        "Entrar no banheiro":


            "Meu coração tá quase saindo pela boca. Não aguento mais."

            "Não tem o que escutar! Eu preciso entrar!"
        "Continuar escutando":


            "Deixa eu ver se eu escuto a Júlia..."

            "???" "Ai, Caio... você sabe que eu não posso..."

            "???" "Você não pode, mas você quer... você sempre quis..."

            "Caio... não... não acredito..."

            menu:
                "Entrar no banheiro":


                    "Meu coração tá quase saindo pela boca. Não aguento mais."
                "Dar meia volta e ir embora":


                    "Como que eu posso fazer isso?!"

                    "Eu tenho que ver com meus próprios olhos!"

            "Bora encerrar essa merda!"

    play sound som_porta

    scene black with dissolve

    pause 2.0

    scene j8_caio_teo1 with Dissolve(1.0)

    pause

    teo "Já falei que eu não posso... a gente tá no meu trabalho!"

    caio "Você sabe que meu pai que paga o Tony, né? Ele não pode demitir você. Para de ser mocinha."

    teo "Olha quem tá falando..."

    caio "Safado..."

    mc "!!!"

    caio "HM?!"

    mc "V-vocês!?"

    scene j8_caio_teo2 with hpunch

    pause

    caio "Você!!! Que porra tu tá fazendo aqui, idiota?!"

    teo "[mc]! C-calma! Entra e fecha a porta por favor!"

    menu:
        "Não. Vocês vão se foder agora.":


            mc "Eu não tô nem aí pro que vocês querem, Téo. A culpa é toda do teu parceiro aí!"

            teo "M-mas..."
        "Beleza. Vamos com calma.":


            mc "Tudo bem... tá tudo ok. Vou fechar."

            play sound som_porta

            pause 2.0

            mc "Pronto. Agora podemos conversar."

    caio "Que tu tá fazendo aqui bem agora, animal?!"

    mc "Eu tomaria cuidado com o jeito que você fala com quem sabe seu segredo..."

    teo "Ele tem razão, Caio. Ele descobriu. Se ele tacar a merda no vertilador já era pra tu."

    caio "Eu não vou abaixar a cabeça pra esse merda!"

    mc "Então no fundo esse era seu segredo..."

    caio "Cala a boca!"

    "Depois do que eu vi na casa do Caio... dá pra entender por que ele precisa esconder..."

    menu:
        "Papai não ia gostar, né?":


            mc "Papai não ia gostar de te ver ficando com homens, né?"

            teo "[mc]..."

            caio "Eu mandei tu calar a boca!"
        "...":


            mc "Tudo bem... eu não tenho nenhum problema com isso."

            caio "..."

    teo "Ninguém sabe do nosso rolo. Por favor, não vai contar pros outros, [mc]!"

    caio "A gente não tem rolo nenhum!"

    mc "Cala a boca, Caio. Eu não sou seu pai. Tô pouco me fodendo se tu curte homem ou mulher."

    if nathan_namoro:

        mc "Além do mais, eu namoro com um cara também. E ele é muito mais gostoso que vocês dois."

        teo "Haha..."

    mc "Agora... o velho... se ele souber que você curte o Téo... ele vai ficar puto."

    teo "Por isso que eu tô pedindo, [mc]... ele não pode saber! Pede pra ele também, Caio, caralho!"

    caio "Eu não vou pedir porra nenhuma! Se tu foder minha vida, eu fodo a tua também!"

    caio "Eu mato você, seu filho de uma puta! Tá me ouvindo?!"

    "Ver o Caio com o Téo assim explica tanta coisa..."

    "Agora ele tá na minha mão. O pai dele é um machista homofóbico escroto. Se o [gi] descobrir que o filho dele é xonadão no Téo..."

    "... o cara vai deserdar o Caio na lata."

    teo "[mc]... você vai ficar de boa?"

    "O Gevanni me chamou pra ir lá no NBC quando desse. É o convite perfeito pra eu ir lá como quem não quer nada e contar do Caio."

    "Isso ia foder ele completamente. O Téo também... e até a Mari ia acabar triste. Mas a vida do Caio ia tá acabada."

    "Ou eu posso ter o Caio na minha mão. Guardar o segredo dele pode me valer de moeda de troca."

    if julia_namoro and not j8_negou:

        "O Caio disse que não ia deixar barato meu namoro com a Jú."

        "Ter o segredo dele na mão vai deixar ele pianinho... e se eu quero uma vida com ela, essa seria a melhor escolha."

        "Pelo menos eu acho..."

    "Agora, se ele for deserdado, ele perde tudo: o dinheiro, a influência, o poder. Ele ia ser como um gatinho sem garras."

    "Mesmo assim... eu quero ferrar mesmo com ele?"

    if not j8_negou:

        "O que é melhor pra eu poder ajudar a Júlia no futuro dela? Tá na hora de eu provar minha amizade."

    elif julia_namoro and not j8_negou:

        "O que será que é melhor pro meu futuro com a Júlia?"

    caio "Fala alguma coisa logo, seu maldito."

    mc "..."

    teo "Por favor, [mc]!"

    "Essa próxima decisão pode ser mais importante do que tá parecendo..."

    "Acabar com o Caio é mais do que ensinar uma lição pra ele... pode mudar minha vida com a Júlia pra sempre."

    "Eu teria um motivo pra falar com o Gevanni no NBC. E vai saber o que eu posso descobrir falando com ele."

    label j8_decisao3:

        pass

    "Tenho que ter certeza do que eu vou decidir."

    menu:
        "Se fodeu, Caio. Seu pai vai adorar saber a verdade.":














            $ caio_prometeu = 0

            "Se eu contar pro Gevanni sobre o Caio, eu acabo com a vida desse mauricinho."

            "O homofóbico machista do pai dele nunca vai aceitar um filho que fica com outros caras."

            "A Mari já me alertou que o Caio é perigoso. Eu vou mesmo comprar briga com ele?"

            menu:
                "Óbvio! Eu tenho que acabar com a vida desse cara!":


                    "Ele merece! Se tem alguém que merece enfrentar a realidade é o Caio."
                "Melhor eu pensar nisso direito":


                    "Calma aí... talvez bater de frente não seja o mais inteligente."

                    jump j8_decisao3

            mc "Eu disse que não tenho nada contra sua preferência. Por mim, tu tem é que seguir seu coração mesmo."

            "Téo" "Então você vai!"

            mc "Só que o Caio fodeu a Júlia, a Mari, e é um mimado desgraçado!"

            mc "Azar o dele que o pai dele é um babaca homofóbico!"

            scene j8_caio_teo3 with hpunch

            caio "Cuzão! Eu sabia que você é um idiota! Eu confiei em você, seu traíra!"

            mc "FODA-SE! Você se acha o reizinho da porra toda! Bora ver agora se tu é rei mesmo!"

            caio "Eu tô falando, cara! Eu vou tirar tudo que é mais sagrado pra você! Pensa bem!"

            menu:
                "Eu já pensei. E tu vai se foder!":


                    pass

            mc "Eu já pensei bastante! E eu não tenho medo das suas ameaças, não."

            mc "Uma vez na vida você vai aprender que você é igual todo mundo! Vai ter que encarar as consequências!"

            teo "[mc]! Por favor! O pai dele-"

            mc "Desculpa, Téo, mas é uma escolha minha. E não tenho nada contra você. Tu é só mais uma vítima aqui."

            teo "Eu não sou, não! Não acaba com o Caio, por favor!"

            "Eu vou fazer isso pelo Téo? Porque eu sei que o Caio não merece."

            menu:
                "Tudo bem. Por você, Téo.":


                    mc "Tá bom. Vcê é um cara bacaa, Téo. E se você quer proteger esse babaca de verdade, então beleza."

                    teo "Tá falando sério?! Valeu, [mc], porra! Ouviu, Caio?!"

                    caio "Esse babaca..."

                    teo "Não fala assim dele!"

                    mc "Escuta aqui. Não vai ser tão fácil assim."

                    jump julia8_final3_continua
                "De jeito nenhum. Ele vai se foder.":


                    mc "Desculpa, Téo. Mas não dá. Chegou a hora dele experimentar a realidade."

            mc "Se ferrou, Caio! Vai ter que ligar com sua situação igual todos nós precisamos todos os dias!"

            mc "A vida também vale pra você, amigo! Eu quero só ver sua cara quando teu pai tirar tudo!"

            caio "Você vai pagar por essa, maldito!"

            mc "Vamos ver. Enquanto isso, eu tenho uma visita ao NBC pra fazer. Valeu!"

            scene black with Dissolve(1.0)

            caio "IDIOOOOTAAAAA!"

            jump julia_final2
        "Não vou contar. Não quero briga com você. Mas tenho condições.":


            $ caio_prometeu = 1



            if julia_namoro and not j8_negou:

                "O melhor pra mim e a Júlia é ter esse cara fora da nossa vida."

                "Segurar o segredo dele é a forma perfeita de ter ele na coleira."

            label julia8_final3_continua:

                pass

            mc "Eu quero propor algo pra vocês."

            scene black with dissolve

            scene j8_caio_teo4 with Dissolve(1.0)

            pause

            caio "Fala logo! Não começa de conversinha!"

            teo "Escuta ele, Caio! Que merda!"

            mc "Eu deixo seu segredo quieto, Caio, mas com um condição..."

            menu:
                "Você deixa a Júlia em paz.":


                    mc "Você vai deixar a Júlia em paz. Não vai aparecer nem pintado na vida dela."

                    caio "Quê?!"

                    mc "Isso aí. Você causou demais na vida dela. Tá na hora de cada um seguir seu caminho."
                "Você deixa a Júlia e a Mari em paz.":


                    $ j8_mari = True

                    mc "Eu não falo nada e daí você deixa a Júlia em paz. A Mari também."

                    caio "Quê?!"

                    mc "Isso aí. Você causou demais na vida das duas. Tá na hora de todos vocês seguirem seus caminhos."

            if julia_namoro and not j8_negou:

                mc "Agora eu e a Júlia tamo junto pra valer. Então acho bom tu não causar."

                caio "Tu é muito idiota mesmo. A Júlia não nasceu pra ser de um homem só."

                caio "Se não for comigo, vai ser com outro que aparecer por aí. Toda vez que ela se sentir rejeitada."

                caio "Eu pensei que você tinha saída, mas você é só um trouxa mesmo."

                mc "Não me interessa sua opinião sobre minha relação com ela. Deixe suas merda de red pill pro Téo."
            else:


                caio "O que você tem a ver com...?! Você nem namora com... por quê?!"

            mc "Temos um acordo ou não?"

            teo "Claro que a gente tem, né, Caio?!"

            caio "E eu vou deixar esse beta mandar em mim?!"

            teo "Você prefere perder tudo, é?!"

            caio "Filho da puta!"

            mc "Pode gritar, fazer careta... temos ou não?"

            caio "Temos, caralho!"

            teo "Boa! Ele prometeu, [mc]!"

            mc "Então estamos combinados. Se eu descobrir que você apareceu... vou direto pro NBC e falo pro teu pai."

            caio "Que merda, hein?! Já falei que tudo bem!"

            mc "Perfeito. Podem relaxar e continuar aproveitando."
        "Pensando bem... eu gostaria de brincar com vocês também.":


            $ caio_prometeu = 2



            mc "Olhando pra vocês sem roupa assim... o que passa na minha cabeça mesmo é que eu quero curtir um pouco também."

            scene black with dissolve

            scene j8_caio_teo4 with Dissolve(1.0)

            pause

            caio "!!!"

            teo "T-tá falando sério?"

            mc "Ué? Não posso curtir uns machos novinhos gostosos também?"

            teo "E a-agora?"

            caio "Se esse puto quer brincar... eu não ligo... é mais um pra me satisfazer. E você?"

            teo "Por mim... fiquei até excitado agora."

            scene black with dissolve

            scene j8_caio_teo5 with Dissolve(1.0)

            pause

            mc "Só que... se vocês querem que eu guarde esse segredo, vocês vão ter que fazer valer."

            teo "Lá ele... tá bom... eu sei pagar um oral que vai te convencer na hora. Abaixa essa calça."

            caio "Você é muito puta, Téo... não pode aparecer um caralho que tu já quer mamar."

            teo "Eu faço isso pelo nosso lance."

            caio "Cala a boca! Ninguém acredita nisso."

            mc "Vem, Téo... fala menos e trabalha mais."

            teo "Sim, senhor."

            label ju8_premium2:

                pass

            menu:
                "Eu vou querer o serviço completo.":


                    if not premium:

                        call mensagem_premium

                        jump ju8_premium2

                    scene black with dissolve

                    scene j8_premium1 with Dissolve(1.0)

                    pause

                    mc "Bota essa boca que eu vou querer o serviço completo."

                    teo "Uhumm..."

                    teo "Até que seu pau é gostoso, [mc]. Vou acabar ficando de pau duro de mamar."

                    caio "Você é uma puta mesmo, Téo."

                    teo "Eu? Depois que você chupar tu vai querer também."

                    caio "Cala a boca."

                    mc "Hoje você tá na minha mão, Caio. Acho bom você se comportar igual ao Téo."

                    caio "Viado..."

                    mc "Todos nós somos."

                    teo "Não dá pra negar, gato."

                    caio "Filhos da puta mesmo..."

                    mc "Tu já se fodeu, Caio. Então para de reclamar e usa sua boca aqui."

                    caio "Hmpf..."

                    scene black with dissolve

                    scene j8_premium2 with Dissolve(1.0)

                    pause

                    mc "Hmmm..."

                    mc "Tá vendo? Não é muito melhor assim?"

                    caio "Eu nunca ia te beijar se não fosse essa situação."

                    teo "Mentirooooso..."

                    mc "Você precisa ser mais honesto, Caio. Não tem problema nenhum tu ficar com tesão por homens."

                    caio "Eu sei! Hmmm..."

                    teo "Logo logo ele se entrega, [mc]."

                    mc "E você não para aí em baixo, hein?"

                    teo "Com certeza."

                    scene black with dissolve

                    scene j8_premium3 with Dissolve(1.0)

                    pause

                    mc "Aahh... quem diria que eu ia me dar bem desse jeito aqui?"

                    teo "E a gente também..."

                    caio "Ah... fale por você..."

                    mc "Será mesmo?"

                    teo "Mentiroso safado, [mc]. Ele goza rapidinho tomando por trás."

                    mc "Hmmm... sério?"

                    caio "Cala a boca, Téo! Claro que não! Eu sou macho!"

                    teo "Sei..."

                    mc "Vamos fazer o teste então."

                    caio "C-como é?! Nunca!"

                    mc "Você não escolhe nada aqui hoje, Caio. Tu vai seguir o que eu quiser."

                    caio "Se é o único jeito... desgraçado..."

                    teo "Tá vendo como ele já cedeu?"

                    caio "CALA A B- Hmm...."

                    mc "Usa sua língua comigo."

                    menu:
                        "Vamos dar o que o Caio quer.":


                            mc "Se ele gosta tanto assim, coloca a mão na parede, Caio."

                            caio "Tá falando sério?"

                            mc "Agora!"

                            scene black with dissolve

                            scene j8_premium4 with Dissolve(1.0)

                            pause

                            caio "Hmmnn... cuidado."

                            mc "Agora você quer cuidado, né?"

                            teo "Deixa que eu vou garantir que teu pau vai tá o mais duro possível."

                            mc "Aahh... Téo... assim é bom..."

                            caio "Vai com cuid-"

                            mc "Toma!"

                            scene j8_premium5 with hpunch

                            pause

                            caio "Nnghhh!"

                            mc "Assim que você gosta, né?!"

                            caio "Cala a boca! Nnghh! Só faz o que você tem que fazer!"

                            mc "V-vou fazer! Aghh! Isso tá me deixando com tanto tesão, caralho!"

                            teo "Come a bunda dele gostoso!"

                            mc "Toma, safado!"

                            caio "Aghhh!"

                            mc "Que bunda gostosa! Nnghhh!"

                            scene black with dissolve

                            scene j8_premium6 with Dissolve(1.0)

                            pause

                            teo "Olha como ele tá duro!"

                            caio "Nghhh!"

                            teo "[mc]! Ele vai gozar rapidinho assim!"

                            mc "Pior que eu também!"

                            teo "Então vai! Quero os dois gozando!"

                            caio "Filho da puta! Aaghhhh!"

                            mc "Caralho, seu gostosoooo! NNGHHH!"

                            caio "GOZA, PORRA!!!"

                            mc "AAAAGHHHH!!!"

                            scene j8_premium7 with vpunch

                            pause

                            mc "CARALHOOOO!"

                            caio "AAAAHHHNNN!!"

                            teo "Os dois gozando! Que delícia!"

                            mc "Aah... aaah... puta que pariu..."

                            caio "Filho... da puta.... aah..."

                            mc "Que comida mais gostosa..."

                            caio "Cala a boca..."

                            teo "Vocês têm química..."

                            mc "Também tô achando..."

                            caio "..."
                        "Já tô satisfeito por hoje.":


                            mc "Vou ter que deixar o agrado do Caio pra outro dia. Tô satisfeito."

                            mc "Só continua me mandando, Téo."

                            teo "S-sim! Vai gozar pra mim, é?!"

                            mc "V-vou! NNGHHH!!!"

                            scene j8_premium3 with vpunch
                "Só uma babada básica é o suficiente.":


                    scene black with dissolve

                    pause 2.0

            mc "Ahh..."

            teo "Hmm..."

            caio "Safado..."

            scene black with dissolve

            scene j8_caio_teo6 with Dissolve(1.0)

            pause

            mc "Adorei."

            teo "Hmm..."

            teo "Isso significa que você não vai caguetar a gente?"

            mc "De mim, o pai dele não vai saber."

            caio "Acho bom mesmo. O velho é cabeça dura..."

            mc "Só acho que você devia falar com a Mari. Ela gosta de você de verdade."

            caio "E é bom assim."

            mc "Não seja terrível, Caio. Assume logo seu namoro com o Téo e libera a Mari."

            mc "Você sabe que enquanto você não assumir a verdade, você vai continuar sofrendo, bravo com o mundo."

            caio "Você não sabe nada de mim, idiota. Vai dar liçãozinha de moral pro algum idiota amigo teu."

            mc "Enfim..."

            if not j8_negou and julia_namoro:

                mc "Agora eu e a Júlia tamo junto pra valer. Então acho bom tu não causar."

                caio "Tu é muito idiota mesmo. A Júlia não nasceu pra ser de um homem só."

                caio "Se não for comigo, vai ser com outro que aparecer por aí. Toda vez que ela se sentir rejeitada."

                caio "Eu pensei que você tinha saída, mas você é só um trouxa mesmo."

            mc "Quem sabe a gente não se encontra de novo..."

            caio "Vai sonhando..."

            teo "Eu não ia reclamar, não."

            mc "Fiquem bem, garotos."

            if not j8_negou and julia_namoro:

                "Não acredito que eu tive toda aquela conversa com a Júlia... e eu que acabei traindo ela na primeira chance..."

                "Eu não tenho salvação..."

    if caio_prometeu > 0 and julia_namoro and not j8_negou:

        jump julia_final1

    elif caio_prometeu == 0:

        jump julia_final2

    label julia_final3_continua:

        pass

    scene black with Dissolve(3.0)

    scene capital_final with Dissolve(1.0)

    "Não que o Caio não mereça sofrer por tudo de ruim que ele fez... mas eu me coloquei em primeiro."

    "Eu não quero briga direta com ele... melhor pensar que ele vai ficar pianinho."

    "Assim eu não preciso me preocupar com os amigos do pai dele. Só de pensar na voadora do Marco meu estômago embrulha."

    "Espero que assim a Júlia consiga seguir o caminho dela."

    if j8_negou:

        "Eu abandonei ela lá na casa do Caio. Ela vai ter que seguir o caminho dela sozinha agora."

        "Será que algum dia a gente vai se reencontrar?"
    else:


        "Eu vou continuar do seu lado como seu anjo da guarda. Eu vou proteger ela desse babaca até o fim."

        "E com esse segredo na minha mão... ela nem vai entender por que o Caio não vai mais causar com ela."

        "Não se preocupa, Jú. O Caio nunca mais vai ser um problema pra você."

    "Enquanto ela procura o caminho dela, eu também tenho que encontrar o meu."

    "E a Ilha das Celebridades, ou melhor, a capital como um todo, tem muita coisa pra eu conquistar. Possiblidades infinitas."

    "Conquistar o amor verdadeiro, o sucesso profissional, fama, riqueza, poder... qual desses será que eu quero mais?"

    "Eu também quero tá certo do que eu quero pra minha vida."

    if not j8_negou:

        "Porque... se eu encontrar a Júlia de novo um dia, eu quero poder responder ela que eu também achei meu caminho."

        "{b}Se eu continuar vivendo meus dias (7 dias), talvez eu encontre ela de novo{/b}"
    else:


        "E meu caminho não passa mais pela Júlia. Eu abandonei ela na casa do Caio, então agora é olhar pra frente."

        "A Júlia não merecia minha atenção. Aquilo era tóxico demais. E eu espero nunca mais ver ela na minha vida."

        "Adeus."

        p "Então este foi o final que você escolheu na sua história com aquela doidinha. Hmm..."

    $ julia_final3_dia = dia + 5

    scene black with Dissolve(3.0)

    $ tempo = 3

    jump call_cidade

label julia_final1:

    $ julia_final1 = True

    scene black with dissolve

    scene cidade noite with Dissolve(1.0)

    if not caio_gi_contou:

        "Não que o Caio não mereça sofrer por tudo de ruim que ele fez... mas eu me coloquei em primeiro."

        "Ele vai poder continuar vivendo essa vida escondida que ele escolheu... sem coragem de encarar o pai."

        "Querendo ou não, ele vai ter que deixar eu e a Júlia tranquilos. Ou a vida dele acaba."

        "Pelo menos eu espero que ele pare. E que a Júlia finalmente pare de procurar esse babaca."

        if j8_mari:

            "Eu ainda fiz ele desistir da Mari... acho bom ele parar de pegar no pé dela."

            "Não sei se a Mari ia querer isso... mas eu quero tirar ela das garras dele."

            "Eu sinto que é meu dever fazer isso por ela. Ela que encontre outro cara pra fazer ela sofrer."

        "Mas eu não tenho nada a ver com isso agora."

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "{i}Trr trrr{/i}"

    g "Oi, gatoooo!"

    scene black with dissolve

    scene mc bar_celular with Dissolve(1.0)

    mc "Fala, minha bagunceirinha."

    g "Eu vi que você me ligou! Eu tava na facul, né?!"

    mc "Aahh!"

    g "Eu sempre dou um jeito de fugir pra falar contigo, mas hoje a gente tava fazendo um lance prático."

    g "Daí não deu pra eu falar com meu gato gostoso delicioso fogoso!"

    mc "Haha... como você vai me recompensar?"

    g "Bora amanhã na praia?!"

    mc "Fechou! Te espero lá!"

    g "Bons sonhos molhados comigo!"

    mc "Sempre!"

    scene black with Dissolve(3.0)

    pause 2.0

    "E foi assim que tudo acabou."

    pause 2.0

    scene j8_julia_praia2 with Dissolve(2.0)

    pause

    "Com o segredo dele na mão, o Caio não tinha mais como estragar as coisas entre a gente."

    "Eu e a Júlia podemos finalmente aproveitar nossa vida normal como namorados agora que o último empecilho tá resolvido."

    "Naquele dia na praia eu perguntei pra Júlia o que ela teve que fazer quando ela desapareceu por uns dias depois de eu tirar ela da casa do babaca."

    "Ela me contou que tentou fazer as pazes com as duas pessoas que ela mais gostava."

    "Depois de mim, claro."

    scene black with dissolve

    scene j8_julia_sayuri with Dissolve(1.0)

    pause

    g "Mana!"

    s "J-júlia?! Por que você tá assim?!"

    g "Eu tentei namorar com um cara, mas eu descobri que no fundo eu quero ficar com você!"

    g "Por favor! Casa comigo!"

    s "Q-QUÊ??!!!"

    g "Brincadeira..."

    s "E-então o quê?"

    g "Desculpa..."

    g "Me desculpa, mana... você sempre me deu amor e carinho... e eu usei isso contra você!"

    g "Eu confundi o carinho que você tava me mostrando como um convite pra te bulinar!"

    g "Minha mente doida não conseguia dividir uma coisa da outra! Me perdoa por ter feito você sofrer!"

    s "Jú... eu... eu nunca pensei que você ia perceber essas coisas..."

    g "Acho que eu nunca conseguiria sozinha... mas você... a Carol... e meu namorado... vocês me mostraram."

    g "Vocês tiveram mais paciência comigo do que eu merecia!"

    s "Seu namorado... é o [mc], né?"

    g "S-sim... tem... algum problema?"

    s "N-não... só ele mesmo pra te ajudar. Aquele jeito..."

    g "Você é igual ele, mana. Vocês dois têm um coração maior do que o de um cavalo!"

    s "Claro que eu te desculpo. Eu sempre gostei da sua energia. Sempre foi um prazer ser sua irmã."

    s "Você sempre foi a doidinha. Só precisa controlar melhor seus impulsos e será uma pessoa incrível."

    s "Eu sempre vou tá torcendo por você."

    g "Valeu, mana. E você também... eu tô sempre do teu lado! E sem pegar no seu bundão gostoso!"

    s "Júlia..."

    g "Hehe..."

    s "Continue sempre assim. Desafiando o que as pessoas acham ser o certo."

    s "Eu sei que com essa energia toda você vai conquistar o mundo!"

    g "Valeu!"

    scene black with Dissolve(3.0)

    pause 2.0

    scene j8_julia_carol with Dissolve(1.0)

    pause

    o "Então isso é sério? Vocês tão juntos de verdade?"

    g "Sim... mesmo com esse meu jeito, o [mc] resolveu ficar comigo. Ele deve ser doido."

    g "Eu disse que faltava eu resolver umas coisas... então eu queria falar com você."

    o "Hm. Que que é?"

    g "Desculpa..."

    o "Desculpa? Tá falando sério? O [mc] que te mandou pedir desculpa? Desculpa pelo quê?"

    g "Ele não falou nada... eu só queria pedir desculpas por ser uma amiga terrível."

    g "Você tentou ser legal comigo e, tipo, eu te ataquei várias vezes. Isso não tá certo."

    g "Você tava certinha de se afastar. Eu sou tóxica demais. Mas eu não vou ser mais. Eu decidi."

    o "Tô achando isso muito estranho..."

    g "Não duvida de mim, idiota! É... você não é idiota. Você é bem mais inteligente que eu."

    o "Hahaha... tô gostando dessa nova Júlia toda cuidadosa."

    g "Ah... vai se foder..."

    o "Agora, sim. Essa é a amiga que eu conheço."

    o "Você não precisa mudar seu jeito. Eu acho seu jeito desbocado muito divertido."

    o "Só não abusa, tá? Respeita os outros. E a gente vai poder ser amigas de novo."

    g "Valeu, quatro olhos!"

    o "E não me chama assim, tonta!"

    g "Tá bom!!!"

    o "Agora você vai me ajudar a arrumar os livros da biblioteca por um mês inteiro como pedido de desculpas!"

    g "Nãããooooo!"

    o "Se reclamar, vai arrumar aqui, e na biblioteca do centro da cidade também!"

    g "Buuuahhhhh!"

    scene black with Dissolve(3.0)

    pause 2.0

    scene j8_mc_jogando with Dissolve(3.0)

    pause

    "Pelo que ela contou... eu não sei se funcionou."

    "Depois de tanta cagada, não acho que as duas vão perdoar ela num piscar de olhos assim."

    "Não é só questão de palavras. Ela vai ter que mostrar que é uma irmã e amiga que vale à pena tá perto."

    "E costurar as feridas abertas do passado não é tão fácil quanto abrir elas."

    "Mas a Júlia é outra pessoa agora. Não é mais aquela que trocaria amor por uma noite quente. Foi uma transformação e tanto."

    "Às vezes eu fico pensando se tudo isso realmente é verdade. Se ela mudou mesmo. Uma ansiedade bate no peito."

    "Só que eu não posso cair nessa espiral negativa. Eu decidi acreditar nessa doidinha."

    "A Júlia é diferenciada. Tá com ela é sempre divertido, engraçado, uma verdadeira aventura."

    "Ela tem tudo pra reconquistar o coração das duas... e conquistar muito mais no futuro."

    "Agora ela tem a mim, pra dar aquela força. Apesar que não adianta eu falar qualquer coisa..."

    if julia_segredo:

        "Até agora eu não revelei pra ela o que eu descobri naquele contrato."

        "Então a Jú não foi adotada. Teve aquela história de 'ritual'. O que será que é aquilo?"

        "Mas eu não quis mudar a vida dela desse jeito. Não acho que é o melhor pra ela agora."

        "Vamos curtir e deixar o passado no passado. Vamos ser feliz!"

    mc "Não importa quanto você treine! Eu sempre vou ganhar!"

    g "Como que você consegue ganhar usando os zumbis e com as plantas também?!"

    mc "HAHAHA! Ser um nerdão tá se pagando agora! Se prepara pra ficar peladinha!"

    g "Eu não vou perder dessa vez!"

    mc "Tarde demais! Agora só falta eu..."

    scene j8_mc_jogando2 with vpunch

    mc "Ei! Que merda é essa?!"

    g "Se você deixar eu ganhar eu transo com você!"

    mc "Você vai transar comigo de qualquer jeito!"

    g "Não vale!!!"

    g "Quero só ver você ganhar comigo aqui!"

    mc "EEIIII!!!"

    "A Júlia sempre teve a personalidade forte e, graças a Deus, ela nunca perdeu essa força de vontade, essa vontade de viver."

    "As coisas vão acontecer no tempo dela. E eu não consigo imaginar uma flor melhor do que essa pra ver desabrochar."

    "O que eu não sabia... é que a Júlia vai herdar da família uma bufunfa imensa."

    "E ela já disse que a grana é minha também. Contanto que eu não traia ela..."

    "Mesmo que o velho babaca resolva me demitir por falta de pautas eu não tô mais na sarjeta."

    "Dá pra acreditar? De todas as garotas que eu encontrei, foi a Júlia que me salvou daquela revista maluca."

    "Chega de chefe, Cássia, pressão pra entregar os segredos das minhas amigas."

    "Eu vou de boa, seguindo minha vida normal, e se ele me demitir, minha namorada resolve pra mim."

    "Uma vida garantida e tranquila no trabalho e cheia de aventura no amor com a mulher mais fogosa do planeta."

    "O que mais um homem pode querer?"

    "Aquele garoto que chegou na cidade grande e não fazia ideia do que tava fazendo... sendo chutado por todo lado."

    "Quem diria que a história de [mcc] ia acabar bem desse jeito?"

    scene black with Dissolve(3.0)

    pause

    $ persistent.julia_final1 = True

    "{i}FIM{/i}"

    pause

    p rindo "Parabéns por chegar ao final... mas que finalzinho... hein?"

    p lecionando "Uma vida normal? Ao lado de uma única garota? Eu sei que ela é fogo, mas uma só mesmo?"

    p "A vida é cheia de possibilidades. Por que você se colocaria em uma gaiola como essa?"

    p "Pensa em todas as mulheres e homens que você pode conhecer, todas as intensas emoções que te esperam."

    p "Quais outras dezenas de finais diferentes existem no seu futuro?"

    p rindo "Eu permito que você volte e tente outros destinos. Destinos que serão muito interessantes para você."

    p "Mas principalmente para mim."

    p "Aqui mesmo na sua relação com a Júlia... existem tantas possibilidades. Não aceite qualquer uma!"

    if julia_segredo:

        p "O que foi aquilo que você leu na sala do machistinha homofóbico, hein?"

    p "Vou continuar de olho em você, gato!"

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 1 da Júlia! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    scene white with dissolve

    $ renpy.full_restart()

label julia_final2:




    "Tá na hora de fazer uma visitinha lá no NBC."

    "Bora contar pro Gevanni o que o filho dele anda fazendo."

    scene black with dissolve

    scene banco_geral with Dissolve(1.0)

    pause

    "Ele é um diretor fodão aqui. Além de fazer parte do grupinho dos cabeças da cidade."

    "Esses caras ainda tão tentando me recrutar pro lado deles. Principalmente pra ajudar com a revista."

    "Só que agora não é hora de pensar nisso. Eu tô aqui pra ferrar o Caio e quem sabe ajudar a Júlia."

    "Tirando esse folgado da jogada, aposto que ela e a Mari vão poder seguir com a vida delas."

    "Melhor eu falar com o carinha ali das informações."

    mc "Com licença. Eu queria falar com o senhor Gevanni."

    "Atendente" "Desculpa, mas se você tiver algum problema, pode falar comigo, senhor."

    mc "Não. Eu sou um... amigo dele. Ele me convidou pra vir pra cá."

    mc "Dá pra você falar pra ele que [mcc] tá aqui?"

    "Atendente" "Vou falar com meu superior. E daí ele vê."

    mc "Boa. Vou ficar aqui esperando."

    show black with dissolve

    hide black with dissolve

    "Atendente" "Senhor. O senhor Gevanni vai te receber no segundo andar."

    mc "Valeu."

    "Hora da verdade."

    play sound som_35_passos

    scene black with dissolve

    scene julia_final2_img1 with Dissolve(1.0)

    mari "O-oi, [mc]."

    mc "MARI?!"

    mari "Eu vim deixar uma coisa aqui pro Caio. Mas não quero atrapalhar a conversa com vocês."

    menu:
        "Eu vou salvar você do Caio.":


            mc "Eu vim salvar você do Caio."

            mari "Me salvar? Eu já não te expliquei isso, bobo?"

            mc "Vamos ver como as coisas vão ser depois de hoje."

            mari "[mc]... se você se preocupa comigo de verdade, não vai fazer nenhuma loucura."

            mari "As coisas tão dando certo pra mim."

            mc "Vamos ver."
        "Não é estranho você tá aqui?":


            mc "Mari... não é meio estranho você tá aqui?"

            mari "Por que? O pai do meu namorado trabalha aqui."

            mc "Eu sei... bom... talvez eu que esteja pensando demais."

            mari "Com certeza, [mc]. Não pense besteira."

            mc "Ok. Desculpa."

    mari "Tudo bem. Vou deixar vocês conversarem. Até mais."

    mc "Até, Mari."

    "Velho... deixar coisa pro Caio? No escritório do Gevanni?"

    "O que que a Mari tá fazendo?"

    scene black with dissolve

    scene julia_final2_img2 with Dissolve(1.0)

    gi "[mc]! Aleluia você tá aqui!"

    mc "Haha... não sabia que você queria tanto assim minha visita."

    gi "Olha, meu amigo. Você sabe que nós queremos você do nosso lado."

    gi "E quando digo 'do nosso lado', você sabe que lado é esse, né?"

    menu:
        "Não tem como não saber quem são vocês.":


            mc "Nessa altura do campeonato, claro que eu sei."

            gi "Excelente."
        "Quem EXATAMENTE são vocês?":


            mc "Eu tô interessado em saber."

            gi "Eu estou certo que você já se encontrou com vários de nossos integrantes."

            gi "Nós somos o Mestre dos Bonecos. Mas, obviamente, tudo isso é extra oficial."

            mc "Falando assim, parece um negócio que controla tudo."

            gi "E não é? Nosso alicerce está na base desta cidade. Para nos derrubar, você teria que derrubar a capital."

            gi "Isso é algo que começou com a fundação, e veio passando de geração a geração."

    gi "Você consegue imaginar como seria sua vida se você for aceito no clube?"

    gi "Seu trabalho como repórter não seria mais que brincadeira para você nesse ponto."

    mc "É por isso que você queria tanto que eu viesse?"

    gi "Eu vejo potencial em você. É novo, acabou de chegar na cidade, e já tá se metendo nos buracos."

    gi "Pessoas menos sofisticadas já teriam se livrado de você, principalmente quando você se meteu com o Gustav."

    menu:
        "O velho merece o pior. Ele é um abusador.":


            mc "Com todo o respeito, aquele velho nojento não merece estar entre vocês. Ele não é nada 'sofisticado'."

            gi "Eu sei muito bem do que você está falando."

            gi "Alguns de nosso grupo podem ter certos hábitos questionáveis. Mas você precisa entender uma coisa."

            gi "Quando se tem todo o poder em suas mãos, fica cada vez mais difícil de satisfazer seus desejos."

            gi "Você deseja cada vez mais. É como se todo vinho que você tomasse tivesse gosto de água."

            mc "Mas isso justifica o que ele faz?"

            gi "Com certeza, não. Mas eu quero que você tente entender a cabeça atrasada dele."
        "E-eu não pretendo arranjar problema pra vocês.":


            mc "E-eu-"

            gi "Não se preocupe. Como eu disse, somos pessoas sofisticadas."

    gi "Pra nós, o mais importante é que nosso grupo continue satisfeito e sempre com novos cabeças talentosas."

    gi "Não posso garantir que você seria aceito, mas o primeiro passo é você demonstrar interesse."

    gi "Identifique oportunidades para ficar do nosso lado. E eu tenho certeza que você ganhará pontos."

    gi "Você é esperto. Tenho certeza que você vai identificar essas oportunidades."

    gi "Indo por esse caminho, na hora certa você receberá um aviso. E sua vida vai mudar completamente. Pra melhor."

    gi "Você vê a Cássia. Ele não era nada, mas seria interessante pra gente ter alguém na revista."

    gi "Agora compara com a Carla. Aquela puta me enganou. Tentou dar um golpe na gente."

    gi "Mas a gente resolveu o esquema. Ela nunca mais vai ser um problema."

    if nona_e3 == "viva":

        "Eles não sabem que ela tá viva."

        "Eu sou um herói ou não sou? Sem mim, aposto que ela já tinha ido dessa pra melhor."
    else:


        "Eu queria ter salvado a Nona aquele dia."

        "Com certeza tinha um jeito de salvar ela... mas como?"

        "Será que se eu ficasse quieto e deixasse ela apanhar... uma hora o Tony ia desistir?"

    gi "Então estar do nosso lado é crucial."

    gi "E uma vez dentro, não é só você. Seus filhos, netos, bisnetos. Todos terão a vida garantida."

    menu:
        "E o Caio? Você tá preparando ele?":


            pass

    mc "Ele deve seguir seus passos, né?"

    scene black with dissolve

    scene julia_final2_img3 with Dissolve(1.0)

    gi "Infelizmente o Caio não é o melhor material para esse tipo de coisa. Parece uma fruta podre."

    gi "Minha vontade é dar um murro naquele garoto mimado. Eu tento de tudo, eu juro, mas ele não entende as responsabilidades dele."

    gi "Em breve ele vai tomar meu lugar cuidando de todo o recurso financeiro do grupo."

    gi "Agora como posso colocar ele numa tarefa desses se ele só pensa em farrear com aquele povinho?"

    gi "Eu tô por aqui com ele. Mais uma e vai ser a gota d'água. Eu deserdo ele para sempre. E corro ter outro filho."

    mc "Mais uma e vai ser a gota d'água... entendi..."

    gi "Quem dera você fosse meu filho. Com certeza eu estaria muito mais tranquilo agora."

    mc "Haha... você fala isso por causa daquela amiga dele? A Júlia?"

    gi "Nem tava pensando nisso, mas agora que você falou, outra coisa pra cabeça."

    "O que ele quer dizer com isso? Por que ele odeia a Júlia?"

    "Será que tem uma pauta nisso pra mim ainda? Eu preciso saber."

    menu:
        "Qual o problema com a Júlia? Você conhece ela?":


            mc "Tem alguma coisa especial com essa Júlia? Ou você só não vai com a cara dela?"

            gi "Eu ouvi que ela é uma devassa. Esse é o tipo de mulher que você só quer se divertir. Não ter alguma coisa séria."

            "Esse sujeito... Além de homofóbico é machista."

            mc "Entendi. Faz sentido..."

            gi "Mas o passado dessa garota é pior que o fogo dela."

            gi "Inclusive eu tava dando uma olhada nisso bem na hora que você chegou."

            gi "O melhor é eu acabar com isso."

            mc "Sério?"

            menu:
                "Qual que é a merda?":


                    mc "O que aconteceu com ela antes?"

                    gi "É o tipo de coisa que a gente não fala. Principalmente pra alguém que tem o poder da mídia igual você."

                    mc "Eu não pretendo publicar. Eu só-"

                    gi "Você vai ter que descobrir isso por você mesmo, [mc]. Sem comentários. Você entende."

                    mc "Tudo bem..."
                "É melhor não chamar atenção pra Júlia":


                    "Ficar quieto é o melhor aqui. Não atrair mais coisa pra cima da Jú."

    "O [gi] sabe de muita coisa, parece. Ele deve ser um dos cabeças. É bacana conhecer ele se eu quiser entrar pro grupo."

    "Pensando agora, talvez... se eu não entregar o Caio, seja melhor para o Gevanni."

    "E para o grupo dele de forma geral. Não mexer nesse vespeiro seria melhor."

    "Agora jogar ele contra o filho... não vai dar pra saber o que pode acontecer."

    "Eu decidi entregar o Caio, mas eu não disse ainda. Eu posso voltar atrás."

    "O que eu faço?"

    menu:
        "Eu tenho que te falar uma coisa sobre o Caio.":


            pass
        "Foi bom ter falado com você. Já tô indo.":


            "Eu decidi não contar sobre o Caio. É mais seguro assim."

            "Desse jeito eu não irrito o Gevanni e as coisas continuam como tão pra eles."

            "Infelizmente o Caio vai continuar firme e forte, atormentando a Mari e talvez até a Júlia."

            "Mas é melhor assim. Não mexer com essas pessoas. Tentar viver minha vida."

            if julia_namoro:

                "E, do lado da Jú agora, a gente pode continuar sendo felizes juntos!"

            mc "Então é isso, Gevanni. Eu vou indo nessa."

            gi "Você vai pensar nisso que eu te disse?"

            mc "Com certeza."

            gi "Fica do lado certo, [mc]. E toma cuidado. Essa cidade não é pra principiantes."

            mc "P-pode deixar. Falous."

            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua



    mc "Eu tenho que te contar uma coisa e não acho que você vai curtir muito."

    gi "Hm? Você não vai entrar pro nosso grupo? Pensei que você fosse esperto."

    mc "Não é isso. É algo mais pessoal pra você."

    gi "Ok... fala de uma vez então."

    mc "Eu vi o jeito que você falou com o Caio quando eu tava no seu apartamento aquele dia."

    gi "Aquele menino é só decepção. Só faltava ele ser comunista ou gayzinho pra acabar com tudo."

    mc "Então... comunista eu não sei, ma-"

    scene black with dissolve

    scene julia_final2_img4 with hpunch

    gi "Calma aí, garoto! Eu espero que você tenha certeza do que tu tá falando!"

    gi "Eu te chamei aqui no respeito e na amizade! Se você for falar da minha família, acho bom você tomar cuidado!"

    "Talvez ele não esteja pronto pra ouvir a verdade..."

    "E se acabar sobrando pra mim? Eu não tinha pensado nisso."

    "E se ao invés de ferrar o Caio ele vier pra cima de mim, pois eu sei a vardade? Tipo queima de arquivo?"

    "Eu vou continuar e contar pra ele ou é melhor parar aqui?"

    menu:
        "V-você entendeu errado... eu não tava falando do Caio.":


            mc "Q-que isso! Não era do Caio que eu tava falando. Só acho que aquele Téo lá, hein..."

            scene black with dissolve

            scene julia_final2_img5 with Dissolve(1.0)

            gi "Ah! Isso com certeza! Eu vou acabar com essa amizade entre eles! Pode deixar."

            mc "Haha... Era só isso."

            "Eu decidi não contar sobre o Caio. É mais seguro assim."

            "Desse jeito eu não irrito o Gevanni e as coisas continuam como tão pra eles."

            "Infelizmente o Caio vai continuar firme e forte, atormentando a Mari e talvez até a Júlia."

            "Mas é melhor assim. Não mexer com essas pessoas. Tentar viver minha vida."

            if julia_namoro:

                "E, do lado da Jú agora, a gente pode continuar sendo felizes juntos!"

            mc "Então é isso, Gevanni. Eu vou indo nessa."

            gi "Você vai pensar nisso que eu te disse?"

            mc "Com certeza."

            gi "Fica do lado certo, [mc]. E toma cuidado. Essa cidade não é pra principiantes."

            mc "P-pode deixar. Falous."

            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua
        "Eu sei do que eu tô falando. Me escuta.":


            pass

    mc "Eu sei que não é fácil, [gi]. Mas não é melhor encarar a verdade de frente?"

    gi "Caralho... fala de uma vez, porra!"

    mc "Seu filho é gay."

    gi "Não é possível! Cala tua boca, miserável!"

    mc "T-tô falando sério!"

    gi "Eu não vou deixar ninguém falar dele assim! Esse tipo de mentira desvairada!"

    "Me fodi! Eu devia ter pensado nisso melhor!"

    gi "Você acha que eu não ia saber uma coisa dessas?!"

    menu:
        "Calma, amigo! É brincadeira! Relaxa!":


            mc "Q-que isso! Era só uma brincadeira! Pra que isso, parceiro!?"

            scene black with dissolve

            scene julia_final2_img5 with Dissolve(1.0)

            gi "Ah! Que isso, [mc]! Não me assusta assim, cara!"

            mc "Agora aquele Téo, hein?"

            gi "Isso com certeza! Eu vou acabar com essa amizade entre eles! Pode deixar."

            mc "Haha... Era só isso."

            "Eu decidi não contar sobre o Caio. É mais seguro assim."

            "Desse jeito eu não irrito o Gevanni e as coisas continuam como tão pra eles."

            "Infelizmente o Caio vai continuar firme e forte, atormentando a Mari e talvez até a Júlia."

            "Mas é melhor assim. Não mexer com essas pessoas. Tentar viver minha vida."

            if julia_namoro:

                "E, do lado da Jú agora, a gente pode continuar sendo felizes juntos!"

            mc "Então é isso, Gevanni. Eu vou indo nessa."

            gi "Você vai pensar nisso que eu te disse?"

            mc "Com certeza."

            gi "Fica do lado certo, [mc]. E toma cuidado. Essa cidade não é pra principiantes."

            mc "P-pode deixar. Falous."

            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua
        "Pode ficar puto! A verdade é essa!":


            pass

    $ caio_gi_contou = True

    mc "Não sei o que te falar, [gi]! Eu vi! Não dá pra mentir, cara!"

    gi "Viu?! Tu tá falando sério?!"

    mc "Na pizzaria do Tony! No banheiro! Ele e o Téo! Eu vi os dois!"

    gi "..."

    scene black with dissolve

    scene julia_final2_img5 with Dissolve(1.0)

    gi "Não é possível..."

    gi "Você tá falando sério, [mc]?"

    mc "Eu não ia brincar com uma coisa dessas. Por pior que seja, eu achei que você ia preferir saber."

    gi "Eu... não sei o que pensar..."

    mc "Só não desconte no mensageiro por favor."

    gi "Não... você tem razão. Eu perdi a cabeça. Você ainda tá tentando me ajudar."

    gi "Então é verdade..."

    menu:
        "Você já suspeitava?":


            mc "Você já..."

            gi "Sim..."
        "...":


            "Melhor eu calar minha boquita agora."

    gi "Tava na cara. Eu quero fechei os olhos."

    gi "Aquele apego que ele tinha com o Téo. E o jeito que ele trata a Mari."

    gi "A Mari é uma garota sensacional. Linda, inteligente, sexy, boa de... completa."

    gi "Aquele ódio todo..."

    gi "Como que um filho meu pôde virar algo assim? Não pode ser culpa minha."

    gi "O erro tá em mim, [mc]?"

    menu:
        "Ser gay não é um erro. Tanto faz se você gosta de homem ou mulher.":


            mc "Gevanni, ser gay não é um erro. Que que importa se um homem gosta de outro homem ou de mulher?"

            gi "Do que você tá falando?!"

            mc "Pra mim, o que importa é a pessoa tá feliz, satisfeita. O que interessa se é por homem ou mulher?"

            gi "Você só pode tá brincando, [mc]... vocês jovens hoje tão totalmente fora de controle."

            gi "Se eu... falasse uma coisa assim pro meu pai... e-ele ia me dar um tapão na boca."

            mc "Seu pai..."

            gi "Antigamente não era assim. A gente não podia namorar um... digo... fazer o que a gente queria."

            mc "Entendo..."

            gi "Enfim..."
        "De jeito nenhum. A culpa é toda dele.":


            mc "Claro que a culpa é dele! Ele que tá indo contra a moral e os bons costumes!"

            gi "Você tá certo! Provavelmente só pra me desafiar, o infeliz!"

    gi "Eu não posso ter um filho assim. O que os outros vão dizer?"

    gi "Ele vai ter que parar com essa graça ou eu vou deserdar ele. Vai pra rua aprender a ser homem."

    mc "..."

    gi "Eu... preciso de um ar. Fique à vontade, [mc]."

    gi "Talvez eu vá direto pra casa. Talvez possamos conversar novamente no futuro."

    mc "Tudo bem. E desculpa qualquer coisa."

    gi "Você tá certo. Eu que pisei na bola. E agora vou resolver meu erro."

    gi "..."

    play sound som_35_passos

    scene black with dissolve

    scene sala_gevanni with Dissolve(1.0)

    mc "Consegui... falei pra ele..."

    "Teve uma hora lá que eu gelei. Achei que ele ia me matar. Mas tudo deu certo."

    "Agora é só esperar o Caio se ferrar. Ele teve o que merecia."

    "Acho bom eu ficar de olho agora. Vai saber o que aquele mimado vai fazer pra se vingar."

    "Nah... todo o poder que ele tinha vinha do pai dele. Sem o pai, o Caio é um zé ninguém."

    mc "É isso que acontece quando você só usa o dos outros e não constrói nada por você mesmo, idiota."

    mc "Deixa eu dar o fora."

    menu:
        "Espera... eu tô sozinho na sala dele.":


            pass

    "Hmm... agora que eu tô aqui... e sozinho... bem que eu podia... dar uma xeretada..."

    "Dá pra ver que ele tá cheio das informações. Se eu tivesse acesso à isso, eu poderia mudar meu destino."

    "Tem o risco dele voltar ou outra pessoa entrar e me ver xeretando."

    "Poderia ser ruim se eu quiser me juntar ao grupo dele. Mas se eu quiser ferrar eles, ter essas informações seria interessante."

    "O que eu faço?"

    menu:
        "Eu vou correr o risco e xeretar.":


            "Vale à pena. Ele sabe algo do passado da Júlia. Eu quero ver isso também."
        "Melhor eu não desafiar os poderosos e ir embora.":


            "Tô saindo fora. Meu negócio é com a Jú."

            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua

    $ julia_segredo = True



    scene black with dissolve

    scene julia_final2_img6 with Dissolve(1.0)

    mc "Ele disse que tava justamente mexendo nas coisas sobre a Júlia."

    "Por que agora? Será que ele viu a Júlia lá no apê deles?"

    "Se ele tava olhando isso agora, deve ter alguma gaveta ou arquivo aberto por aqui."



    mc "Tem vários papéis, mas quase todos são só contas."

    mc "Hm? Uma pasta aberta."

    "Quê?! Quem é essa criança aqui na foto?!"

    scene black with dissolve

    scene julia_final2_img7 with Dissolve(1.0)

    pause

    mc "Essa garotinha... Esse cabelo..."

    mc "É a J-Júlia!?"

    mc "Que merda é essa?! Por quê o Gevanni tem uma foto da Júlia tão pequena?!"

    "Calma... tem coisa escrita aqui."

    "!"

    "Júlia *REMOVIDO*, foi entregue à família Ai no processo do ritual *REMOVIDO*."

    "{i}Todos os dados foram removidos de ambientes digitais. Apenas duas versões impressas do contrato ficaram disponíveis.{/i}"

    "{i}Uma para cada parte do acordo.{/i}"

    "{i}As partes se comprometem a manter sigilo absoluto quanto à transação, sob pena de sanções em caso de vazamento.{/i}"

    "{i}As partes reconhecem que este contrato não tem e não pode ter qualquer respaldo legal devido à natureza da transação.{/i}"

    "{i}O passado da garota também foi apagado para evitar que a mesma tenha qualquer chance de vazar o ocorrido.{/i}"

    "O passado da Júlia... apagado?"

    "Então... parece que ela não foi adotada pelos pais da Sayuri!"

    "Se eu contar isso pra ela, isso pode mudar a vida dela pra sempre!"

    menu:
        "Eu descobri o que eu queria. Deixa eu dar o fora.":


            "O que eu peguei tá bom. É informação demais até. Bora dar o fora antes que me peguem e mandem o Marco atrás de mim!"

            jump julia_final2_continua
        "O risco vale à pena. Pode ter mais coisa!":


            "Eu sei que é problemático isso que eu tô fazendo, mas não dá pra parar agora!"

    "Tem outra foto aqui."



    scene black with dissolve

    scene julia_final2_img8 with Dissolve(1.0)

    pause

    "{i}A família Ai ficará responsável por fazer a proteção da sacerdotiza.{/i}"

    "{i}O acordo firmado entre o Distrito e a Cidade Chinesa estabelece que ambas as partes deverão receber uma promessa de fidelidade.{/i}"

    "{i}Dessa forma, o Grupo funcionará como mediador da transação.{/i}"

    "{i}A família *REMOVIDO* já entregou sua parte para os cuidados do mediador, que repassará assim que receber a contrapartida.{/i}"

    "{i}No caso da família *REMOVIDO*, suas dívidas para com o Grupo foram totalmente apagadas como contrapartida.{/i}"

    "{i}Parte do acordo estabelece que a família deverá deixar a capital e ir para local não descriminado.{/i}"

    "{i}A família também renega qualquer direito de contato com a parte a partir da assinatura deste instrumento.{/i}"

    "A família da Júlia tá por aí! Mas eles não podem falar com ela!"

    "Que merda de contrato é esse?! Eu conheço a Cidade Chinesa e o Distrito, mas quem é o 'Grupo'?!"

    menu:
        "É mais seguro eu parar aqui.":


            "O que eu peguei tá bom. É informação demais até. Bora dar o fora antes que me peguem e mandem o Marco atrás de mim!"

            jump julia_final2_continua
        "Só mais um pouco!":


            "Não vou parar agora."

    $ sacerdotisas = 1

    "Opa. Mais uma foto."

    scene black with dissolve

    scene julia_final2_img9 with Dissolve(1.0)

    pause

    "{i}A parte do Grupo do contrato ficará protegida em no cofre de um banco de segurança máxima.{/i}"

    "{i}Uma pessoa de confiança será designado para fazer a segurança pessoal e deverá responder caso o documento seja perdido.{/i}"

    "{i}Por fim, a família Ai deverá fazer relatórios periódicos do desenvolvimento da sacerdotiza.{/i}"

    "{i}Ela deve apresentar plena saúde e desenvolvimento físico, mental e psicológico.{/i}"

    "{i}Falha em atender qualquer um dos parâmetros acordados acarretará em sanções extra judiciais.{/i}"

    "{i}E, por estarem assim justos e contratados, firmam o presente contrato em duas vias de igual teor e forma.{/i}"

    "{i}E na presença das testemunhas, que subscrevem, obrigam-se, por si e seus sucessores, a cumprir o aqui disposto.{/i}"

    mc "Acaba aqui."





    scene julia_final2_img10 with hpunch

    pause

    mc "Q-quê é isso?!"

    "Essa foto... são só três garotas normais... mas... eu sinto uma coisa tão estranha olhando pra ela."

    "Eu fico pensando se tem alguma coisa a ver com tudo o que eu li."

    "Quer saber? E se eu levar ela comigo e pedir ajuda pra alguém? Alguém que saiba o que isso significa."

    "Ok. Vou levar ela."

    "Agora deixa eu sair daqui que eu já tô correndo risco demais."



    scene sala_gevanni with hpunch

    "Atendente" "Ei! O senhor tá aqui ainda?!"

    mc "Ah!"

    "Atendente" "O senhor Gevanni não está mais no prédio. Por que você ainda tá aqui?"

    mc "B-bem..."

    "Atendente" "Eu vou ter que contar pra ele que você ficou sozinho aqui na sala até agora."

    "Merda! Ele não pode saber! Se ele tiver uma dúvida que eu li essas merdas eu tô fodido!"

    mc "Calma aí, amigo!"

    "Atendente" "Nada de calma aí. Vamos. E amanhã eu conto pra ele."

    menu:
        "Eu sou um paparazzo. Vou fazer sua vida um inferno.":


            mc "Sabe quem eu sou? Não sabe, né?"

            "Atendente" "Q-quê?"

            mc "Meu nome é [mcc] e eu sou o principal paparazzo da revista maior revista da Capital."

            "Atendente" "E daí?!"

            mc "Meu trabalho é encontrar podre das pessoas e foder com a vida delas."

            mc "Aposto que meu chefe ia adorar saber tudo o que tu faz de errado."

            mc "Imagina eu em cima de você todos os dias, de um lugar que você não pode me ver."

            "Atendente" "Ei! Para com isso, tá?!"

            mc "Você que me diz."

            "Atendente" "Tá bom! Chega! Só dá o fora e fica tudo como tá."

            mc "Eu vou confiar em você. Mas se o Gevanni falar um 'a' pra mim, eu volto."

            "Atendente" "T-tá! Só cai fora!"
        "Eu te pago pra você me deixar ir.":


            mc "Ei. A gente não precisa disso. Eu tenho uma coisa aqui pra você."

            "Atendente" "Do que você tá falando?"

            mc "Meu salário não é muito, mas dá pra regar tua mão. E o Gevanni não precisa saber."

            "Atendente" "Tu não pegou nada, né?"

            menu:
                "Claro que não.":


                    pass

            mc "Nadinha."

            "Atendente" "Então tá. Mas não é merreca, né?"

            mc "Bom..."

            "Atendente" "Passa logo isso aí e dá o fora!"

    label julia_final2_continua:

        pass

    scene black with Dissolve(2.0)

    scene mc parque_sentado with Dissolve(1.0)

    "Ufa... acho que deu certo."



    "Ainda não acredito naquele contrato... tudo o que tava falando da Júlia..."

    "Sorte que eu peguei uma das fotos dela pra provar. Se não é duro de acreditar nessa história."

    "Ela precisa saber de tudo isso."

    "..."

    "Ou não?"

    "Se ela descobrir que ela não foi adotada, mas foi peça de barganha em uma coisa muito mais podre e estranha."

    "A cabeça dela pode pifar de vez. Eu posso ferrar com ela mais do que ajudar. E eu não quero estragar a vida da Jú."

    if julia_namoro:

        "Ainda mais agora que a gente tá junto pra valer."

    "Mas eu tenho o direito de esconder essa informação dela?"

    "Talvez seja melhor eu conversar com alguém. Não carregar uma decisão dessas sozinho. Pelo menos ter outra opinião."



    "Sem a Sayuri, a única que sobrou foi a Carol. Mas ela não quer saber da Júlia também."

    "Não tem jeito. Eu tenho que tentar."

    if sacerdotisas == 1:

        "E eu ainda tenho aquela foto com as três garotas de quimono."

        "A Carol é uma enciclopédia humana. Ela pode me dar alguma luz sobre isso."

    mc "Bora lá."

    scene black with dissolve

    scene biblioteca 2andar with Dissolve(1.0)

    mc "Carol!"

    o "[mc]?"

    mc "Ufa! Sorte que você tá aqui hoje."

    o "E-eu sempre tô aqui."

    scene black with dissolve

    scene carol_biblioteca_incomodada_close with Dissolve(1.0)

    o "O que você veio..."

    menu:
        "Eu vim falar sobre a Júlia.":


            pass

        "E o nosso lance, hein?" if j7_carol_beijo or carol_declarou:

            mc "Eu tô com saudades de você. Você ainda não tá pronta pro nosso lance?"

            scene black with dissolve

            scene carol_biblioteca_vergonha with Dissolve(1.0)

            o "E-eu!"

            o "Eu... não. Não passou tanto tempo assim, né?"

            mc "Toda vez que eu te ver, eu vou ter que te perguntar isso."

            o "T-tudo bem... hehe..."

            mc "Agora que eu já te deixei vermelha, tem outro assunto."

    mc "Eu descobri uma coisa sobre a Júlia. E não tenho certeza de como lidar isso."

    mc "Tava pensando se você podia me ajudar? Pelo menos dar sua opinião."

    scene carol_biblioteca_incomodada_close with Dissolve(1.0)

    o "A Júlia... você lembra que eu não tenho mais nada com ela, né?"

    if j8_negou:

        mc "Eu também não tenho. Eu já falei pra ela que cada um segue seu caminho."

        o "Poxa... verdade? Então agora ela tá sozinha de verdade..."

        mc "Ela sempre vai ter aqueles idiotas."

        o "É..."

    mc "Mesmo assim, isso é algo grande, Carol. Pode mudar tudo de verdade!"

    o "Se você precisa... eu posso fazer isso por você, não por ela."

    mc "Valeu."

    show black with Dissolve(1.0)

    scene carol_biblioteca_incomodada with Dissolve(1.0)

    o "Minha nossa..."

    o "E a foto... com certeza é a Júlia nela. Ela era tão fofinha... não que ela não seja agora, d-digo!"

    mc "E o que você acha? Eu conto ou não?"

    o "Não é uma coisa fácil. E eu não vou ser irresponsável e dizer que eu sei o que eu tô te falando."

    o "E nem acho certo você ter que passar por isso. É uma situação bem complicada que você tá."

    o "Poder mudar a vida de uma pessoa assim... é um peso muito alto pra carregar."

    o "Mesmo com essas ressalvas, eu acho que você devia contar, [mc]."

    o "A Júlia tem o direito de saber sobre a vida dela. E ela é grandinha. Faça sua parte."

    mc "Talvez você tenha razão..."

    o "Agora, esteja preparado. Eu conheço a Júlia. Ela às vezes é bem adulta. Mais do que a gente dá crédito pra ela."

    o "Mas ela é muito emocional também. Quando ela sente algo que ela não sabe controlar, ela fica doida."

    o "E eu tenho praticamente certeza total que descobrir que seus pais te venderam... é algo que ela não vai saber lidar."

    mc "Entendi..."

    mc "Muito obrigado, Carol. Foi pra isso que eu vim aqui."

    show black with dissolve

    scene carol_biblioteca_sorrindo with Dissolve(1.0)

    o "Tudo bem. Eu continuo sendo sua amiga, tá?"

    mc "E eu continuo sendo seu amigo também."

    o "[mc]..."

    mc "Oi?"

    o "D-deixa pra lá. Tomara que dê tudo certo com você e a [g]."

    o "Quero que vocês dois fiquem bem."

    if not julia_namoro:

        mc "A gente é só amigo também. Mas tomara que a gente fique bem mesmo assim."

        o "Ah, entendi haha..."
    else:


        mc "É. A gente tá namorando firme agora. Tomara que dê tudo certo."

        o "V-vai dar."

    if sacerdotisas == 1:

        $ sacerdotisas = 2

        mc "Ah. Eu tenho outro favor pra te pedir."

        o "Hm? Claro."

        mc "Eu queria saber se você conhece essa foto aqui."



        scene julia_final2_img10 with dissolve

        mc "Eu não faço ideia do que que é. Mas como você manja dos livros."

        o "Ai, [mc]. Essa foto me dá uma coisa estranha."

        mc "Por quê? São só três garotas orientais."

        o "Não são elas exatamente. É que me lembra de alguns livros que eu já li."

        o "Falava de um ritual que acontecia há muito tempo na Ásia, que envolvia três sacerdotisas."

        mc "Deve ser isso, Carol!"

        o "Eu vou te mostrar onde fica o livro."

        play sound som_35_passos

        scene black with dissolve

        "{b}Você liberou um novo livro secreto na biblioteca{/b}"

        scene carol_biblioteca_sorrindo with Dissolve(1.0)

    mc "Valeu por tudo, [o]. Você sempre foi uma garota super legal, diferente do que tem por aí."

    o "Uma nerdona você quer dizer, né?"

    mc "E isso é um grande charme. Você é séria e confiável, só que é amável e meiga ao mesmo tempo."

    mc "Eu torço pra gente continuar se vendo em outras oportunidades."

    o "O-obrigada, [mc]. Você é o rapaz mais bacana que eu já conheci. Eu também torço pra gente se ver..."

    mc "Fica bem."

    o "Você também!"

    scene black with Dissolve(1.0)

    pause 1.0

    scene ape_chuveiro with Dissolve(1.0)

    "A Carol acha que eu devo contar tudo pra [g]."

    "Mas no final a decisão é minha."

    "Eu vou falar a verdade e virar a vida dela de ponta cabeça?"

    "Ou guardo esse segredo pra mim, um segredo que eu nem deveria ter encontrado, e mantenho a vida dela nos trilhos?"

    if julia_namoro:

        "O que é melhor pra nossa relação também?"

        "As coisas tão boas entre a gente agora. Será que eu vou querer mexer nisso com uma revelação bombástica dessas?"

    "O que vai ser, [mc]?"

    menu:
        "Contar o segredo para a Júlia":


            mc "Eu não posso esconder isso dela. Ela precisa saber verdade, não importa quão impactante ela seja."
        "Não revelar a verdade para ela":


            "Eu não vou contar."

            "Não quero mudar completamente a vida dela com algo que eu nem deveria ter descoberto."

            "Eu nem devia ter esse peso nas costas se eu não fosse tão xereta."

            "Vou continuar como se eu nunca tivesse visto isso e ver onde as coisas levam."

            "Minha história com a Júlia vai continuar. E isso vai ficar perdido pra sempre."

            "Espero que essa seja a melhor escolha pra você também, Jú."

            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua

    scene black with Dissolve(1.0)

    pause 1.0

    scene ape_celular_falando with Dissolve(1.0)

    "Vou ligar pra ela."

    "tu tu tu"

    "Não tá atendendo... que estranho."

    "Será que ela tá na aula? Não. Nem é hora da faculdade ainda."

    "tu tu tu"

    "Nada..."

    "Ela não pode desaparecer assim bem agora que eu decidi contar o maior segredo da vida dela!"

    "O que eu posso fazer? Amanhã eu tento falar com ela de novo."

    scene black with Dissolve(1.0)

    pause

    scene ape_cama with Dissolve(1.0)

    "Uaahh..."

    "Eu tava precisando de um sono."

    scene black with dissolve

    scene ape_celular with Dissolve(1.0)

    mc "Nenhuma mensagem da Jú. Que que tá acontecendo?"

    "Tu tu tu"

    "Merda! Isso nunca aconteceu antes!"

    "Júlia, que que tu tá aprontando numa hora dessas?"

    mc "Vou ter que ir atrás dela. E dessa vez eu tô sozinho."

    "Mas eu não vou perder tempo igual da outra vez. Eu vou no pior lugar de cara."

    "Da outra vez ela tava lá..."

    call locomocao

    scene cidade centro10 with Dissolve(1.0)

    pause 2.0

    mc "Atende logo!"

    "???" "Oi?"

    mc "Sou eu! A Júlia tá aí?!"

    "???" "J-Júlia? Ela não t-"

    mc "Abre aqui!!! Eu vou subir!!!"

    "???" "S-sim, senhor."

    scene black with dissolve

    scene caio_varanda_cenario with hpunch

    mc "Júlia!?"

    mc "Você tá aqui de novo?!"

    "???" "Ei! O que é isso?!"

    scene black with dissolve

    scene julia_final2_img11 with Dissolve(1.0)

    gi "[mc]? Por que você tá aqui?!"

    mc "G-gevanni! Eu! Cadê a Júlia?!"

    gi "Por que essa garota estaria aqui?! Eu já disse pro Caio que não quero mais ver ela! E isso nem interessa mais."

    mc "Desculpa... eu não queria entrar assim, mas eu pensei que ela tivesse vindo pra cá."

    gi "Atrás do Caio, né?"

    mc "É. Os dois têm uma história."

    gi "Não se preocupe mais com aquele filho da puta. Aquele merdinha é passado!"

    mc "Como assim? Você tá falando do seu filho?"

    scene black with dissolve

    scene julia_final2_img12 with Dissolve(1.0)

    gi "Ele não é mais meu filho! Ele não vive mais aqui! Ele não faz mais parte da minha vida!"

    gi "A mãe dele que perdoe. Ela era uma santa. Mas ele perdeu tudo! Chutei ele pra fora!"

    mc "Então ele realmente..."

    gi "Foi graças a você, [mc]. Você abriu meus olhos."

    gi "Então esquece o Caio. Ele perdeu tudo. Vai viver igual um indingente pelas ruas."

    gi "Não acredito que meu filho era a porra de um viadinho!"

    mc "..."

    gi "O bom é que a Mari vai parar de sofrer na mão dele. Ela tá livre daquele babaca."

    gi "Ela é mulher demais pra aquele... você sabe. Ela merece coisa melhor."

    menu:
        "Então a Júlia não tá aqui...":


            pass

    mc "Se a Júlia não tá aqui..."

    gi "Cuidado com aquela garota, [mc]. Escuta um homem com experiência. Procura uma garota séria e linda igual a Mari."

    gi "Deixa essa tal de Júlia pra lá."

    mc "Ok. Beleza. Eu vou indo nessa então."

    gi "Tá. A gente se vê lá no NBC."

    scene black with dissolve

    "Júlia, o que aconteceu com você?!"

    "Não me diz que você foi socorrer ele!"

    jump call_cidade

label julia_final2_final:

    $ julia_v8 = "completo_final2"

    "Então o Caio se ferrou mesmo. Eu acabei com a vida dele."

    "Vamos ver se ele vai manter aquela pompa toda sem as coisas que o pai dele conquistou."

    "A única coisa é que a Júlia sumiu também. Não é possível que ela foi atrás dele."

    "Eu sei que os dois têm uma história, mas..."

    "Mas cadê a Júlia então?!"

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "{i}Trr trrr{/i}"

    mc "Hm?"

    scene black with dissolve

    scene ape_celular_falando with Dissolve(1.0)

    mc "Mari?"

    mc "Oi?"



    "Mari" "[mc]! A Júlia tá na casa de férias com o Caio! Rápido e você pega eles!"

    mc "Mari!"

    "Tuu... tuu..."

    mc "Casa de férias?! Não é possível!"

    if carro:

        "Melhor eu ir de ônibus lá. Não vou levar meu carro pra aquele buraco."

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    play sound "audio/som_14_onibus.mp3"

    if tempo >= 3:

        scene onibus parado_noite with Dissolve(3.0)
    else:


        scene onibus parado with Dissolve(3.0)

    pause 2.0

    scene black with dissolve

    scene j6_onibus with Dissolve(1.0)



    "Motorista" "E aí, maninho? Acho que eu lembro de tu!"

    mc "Você que me levou lá da outra vez!"

    "Motorista" "Ainda se metendo com essa gente?"

    mc "Essa gente que tá se metendo comigo. Eu acho pelo menos..."

    "Motorista" "Eu te falei aquela vez e falo de novo. Não vai comprar briga com essa galera."

    "Motorista" "A gente percisa focar no nosso."

    menu:
        "Eu preciso confirmar uma coisa com meus olhos.":


            mc "Eu tenho que ver uma coisa!"

            "Motorista" "Xi... tem jeito de pessoa apaixonada isso."
        "Talvez eu devesse voltar mesmo... e esquecer isso.":


            mc "Talvez eu esteja se metendo em coisa que eu não devia."

            "Motorista" "Eu acho que tá."

            mc "Mas não dá pra parar assim."

    if julia_namoro:

        mc "Eu preciso ter certeza se minha namorada é quem eu acho que ela é."
    else:


        mc "É só uma amiga, mas... ela só tem a mim agora."

    "Motorista" "Boa sorte, meu truta. E depois que eles limparem o chão contigo, não vai dizer que eu não avisei."

    scene black with dissolve

    "Motorista" "Chegamos. Boa sorte, maninho."

    mc "Valeu."

    play sound som_23_passos1

    scene black with dissolve

    scene j6_matagal with Dissolve(1.0)

    pause

    "Se eu conseguir chegar lá sem ninguém me ver vai ser muito melhor."

    "Agora... como eu faço isso..."

    if julia_e6 != "biblioteca":

        "Aquela merda que aconteceu a primeira vez que eu vim aqui vai acabar ajudando."

        "Bora pra água!"
    else:


        "Eu vou tentar passar pelo meio do mato aqui. Tentar chegar por trás."

        "Vamos lá, [mc]!"

        mc "E-ei!"

    play sound som_22_splash

    scene black with dissolve

    scene julia_final2_final1 with dissolve

    pause 2.0

    mc "Não acredito... quanto mais eu fico aqui, mas eu me sinto um idiota!"

    "Mas agora que eu me fudi, eu vou ter certeza do que tá acontecendo."

    "Que bosta a Júlia tá fazendo aqui?!"

    if julia_namoro:

        "A gente tá namorando! Por que merda ela não me avisou?!"

        menu:
            "Eu nunca ia deixar ela vir aqui!":


                "Quem que eu quero enganar? Nunca eu ia deixar ela vir aqui."

                "Não que eu seja o dono dela também, mas eu ia ser super contra!"
            "Conversando, talvez não tivesse problema.":


                "Se ela tivesse uma razão de verdade... eu não posso querer mandar nela."

                "Eu ia aceitar se é o que ela quisesse. Eu tenho que confiar nela, né?"
    else:


        "E por que eu tô aqui? Merda! Bendita hora que eu disse que ia ser amigo dela!"

        "Acho bom ela me dar um troféu de melhor amigo se eu tiver que tirar ela de rolo de novo!"

    "Ela com o Caio... como eu vou reagir se eu encontrar os dois juntos?"

    "Depois eu penso nisso!"

    "Agora... como que eu chego lá sem ninguém me ver?"

    "AH!"

    play sound som_22_splash

    scene black with dissolve

    scene julia_final2_final2 with dissolve

    pause 2.0

    "Ok... não tem ninguém aqui"

    scene julia_final2_final2 with hpunch

    "???" "Parem de ser cuzões medrosos!"

    mc "!!!"

    mc "A voz de um homem. Acho que eu já ouvi essa voz antes."

    "???" "Vocês sempre me obedeceram! Não vão dar uma idiotas agora!"

    "Hm? Briga? Tem gente brigando."

    "Se eu chegar mais perto acho que eu consigo ouvir melhor."

    "Mas a chance de me pegarem aumenta bastante."

    menu:
        "Chegar mais perto para escutar":


            "Acho que eu vou lá."

            "Só tomar cuidado com o barulho..."

            play sound som_23_passos1

            scene black with dissolve

            scene julia_final2_final3 with Dissolve(1.0)

            "Ok... acho que daquí eu consigo ouvir tudo."
        "Continuar tentando ouvir de longe":


            "Melhor eu ficar aqui mesmo."

    "???" "Vai dar tudo certo! Só fazerem o que eu tô mandando!"

    "???" "Velho! Uma arma! Você tá indo longe demais, cara!"

    "Outra voz de homem."

    "???" "Cala a boca! Eu que sei o que eu tô fazendo!"

    "???" "Caio, você precisa voltar e conversar com seu pai. Ele é um homem razoável. Só tava irritado."

    "Caio" "Ele me deserdou, porra!"

    "É o Caio! E uma voz feminina."

    menu:
        "É a Júlia?!":


            mc "Por que a Júlia taria falando do pai do Caio?"

            "Não acho que seja ela."
        "Só pode ser a Mari!":


            pass

    "Tem que ser a Mari! Ela que tem contato com o pai do Caio!"

    "Então a outra voz masculina deve ser o Téo."

    "Caio" "Façam o que eu digo e eu vou fazer meu pai me aceitar de volta!"

    "Caio" "E se eu voltar, vocês vão voltar também! Não esqueçam disso!"

    "Mari" "Tudo bem... mas eu preciso de um ar."

    "Téo" "Eu ainda acho isso loucura."

    "Caio" "Ah! Cala a boca."

    "Calma! Precisa de um ar?! Ela vai-"

    play sound som_porta

    scene black with dissolve

    scene j8_final4 with hpunch

    mari "!!!"

    mc "M-merda!"

    menu:
        "Mari! Por favor! Não grita!":


            mc "Mari! Eu tô aqu-"

    mari "Xii!"

    mari "Não abre a boca!"

    mc "Por que você me chamou?"

    mari "A Júlia tá aqui."

    mc "O que ela tá fazendo aqui?! O que VOCÊS tão fazendo aqui?!"

    mari "O Caio chamou a gente! Mas não dá tempo de eu te explicar!"

    mari "Você vai naquele cômodo lá no fundo! A Júlia tá lá!"

    scene j8_final4 with hpunch

    caio "MARIII!"

    mari "Que droga! Toma a chave!"

    mc "Essa é a chave daquele cômodo?!"

    mari "É! Vai logo!"

    menu:
        "Tô indo!":


            mc "Tô indo!"

            mari "Boa sorte!"
        "Mari? Por que você tá me ajudando?":


            mc "Por que você tá fazendo isso?"

            mari "Eu tô arrumando a cagada que você fez!"

            mc "O Caio merecia se ferrar!"

            mari "E eu? Você pensou no que eu queria?"

            mc "Eu..."

            menu:
                "Não. Não pensei.":


                    mc "Não..."

                    mari "Obrigada, [mc]."
                "Eu queria te salvar dele.":


                    mc "Você merece mais que ele!"

                    mari "NA SUA OPINIÃO!"

                    caio "Mari?!"

            mari "Você sabia que tava tudo legal assim pra mim."

            mari "As coisas tavam quase se ajeitando com a Júlia saindo da vida dele."

            mari "Mas você tinha que causar, né? Tinha que fazer o que VOCÊ queria!"

            mc "Mari, eu..."

            mari "Vai logo tirar ela daqui. Antes que o Caio suspeite."

            mc "T-tô indo!"

            mari "Boa sorte."

    scene black with dissolve

    mc "Aqui!"

    play sound som_porta

    scene black with dissolve

    scene j8_final5 with dissolve

    mc "Júlia!"

    g "[mc]!"

    if julia_namoro:

        g "Gato! Eu juro que eu não vim pra cá! Eu não te traí!"

    g "O Caio me raptou! Eu tô presa aqui desde ontem!"

    menu:
        "Estranho como você tá na casa dele de novo!":


            mc "Outra vez você com ele, né?"

            g "Eu tô falando sério! Se a gente perder tempo demais ele vai pegar a gente!"

            mc "Eu preciso confirmar isso, Jú! Eu preciso ter certeza que eu posso confiar em você!"

            mc "Toda vez acontece isso! Eu tô cansado!"

            if julia_namoro:

                mc "Eu quero ser seu namorado, mas eu não quero ser um babaca!"

            g "A-agora não dá tempo. A gente pode ver isso depois! Por favor!"

            mc "T-tudo bem. Vamos sair daqui."
        "Então foi isso! Cara louco!":


            mc "Desde ontem?! Então foi por isso! Esse cara é doente!"

            mc "A gente tem que sair daqui voando, Jú! Antes que ele pegue a gente!"

    g "e como que você abr-?!"

    mc "A Mari tá ajudando a gente! Bora sair daqui!"

    g "Tá! Por favor vai na frente!"

    mc "Me dá sua mão e me segue!"

    scene black with dissolve

    scene j8_final6 with vpunch

    mc "Vem! Vamos pela água!"

    g "Tá louco?!"

    mc "Eu sei por onde a gente pode sair!"

    g "Sério esse negócio da água?!"

    mc "Só faz o que eu tô falando, porra!"

    g "Tá bom! T-tô te seguindo!{nw}"

    play sound som_17_tiro

    scene j8_final7 with vpunch

    pause

    caio "FILHO DA PUTA!!!"

    caio "Você de novo!"

    g "Caio! Você tá com merda na cabeça! Que porra é essa?!"

    "Ele tá armado! Um passo em falso aqui e eu tô morto!"

    menu:
        "Calma, Jú!":


            pass
        "Vai à merda você, seu cuzão! Já era pra você, otário!":


            $ renpy.block_rollback()

            scene j8_final8 with hpunch

            mc "Tô cansado desse seu jeito Caio! Você já se fodeu!"

            caio "FILHO DA PUTA!!!"

            play sound som_17_tiro

            scene red with hpunch

            g "[mc]!!!!!! NÃÃOOOO!!!"

            "E-eu... vou morrer assim?!"

            scene black with Dissolve(2.0)

            $ renpy.full_restart()

    mc "Calma, [g]!"

    caio "Agora você tá calminho, né?"

    caio "Tá vendo isso aqui na minha mão, né, otário?!"

    caio "Mas e quando tu acabou com a minha vida contando aquilo pro meu pai?!"

    menu:
        "Você é um cuzão que mereceu!":


            scene j8_final21 with hpunch



            mc "A culpa não é minha se seu pai é um homofóbico do caralho."

            mc "E você fez a Júlia, a Mari, até o Téo sofrer! Agora você vai pro lixo, cara!"

            caio "Só porque você quer!"
        "Não tem nada perdido aqui. Eu posso te ajudar com seu pai.":


            scene black with dissolve

            scene j8_final21 with dissolve

            mc "Você ainda tem chance!"

            caio "Eu não preciso você falar isso pra mim!"

    caio "Eu sei como eu vou recuperar meu lugar!"

    menu:
        "Hmm...":


            pass

    caio "Hah! Você se acha o grande amor da Júlia, mas não sabe nada sobre ela."

    caio "Essa rapariga aí vale mais do que esse jeito puta dela entrega!"

    "Ele tá falando do contrato?"

    menu:
        "Não fala assim dela!":


            mc "Não fala assim dela, seu escroto!"

            caio "Vai me dizer que você também não odeia esse jeito dela?"

            mc "Claro que não odeio! A Júlia é livre pra fazer o que ela quiser. Não é isso que diz se uma pessoa tem valor ou não."

            g "!"

            mc "Além de que um mimado como você não tem direito de falar de ninguém!"

            caio "Eu vou meter uma bala na cabeça desse otário!"

            g "Para, Caio!"
        "O que você sabe, Caio?":


            mc "Do que você tá falando, Caio?"

            caio "Vocês querem saber mesmo?"

    caio "Você quer ouvir, não quer, bebê?"

    g "Eu?"

    "Então ele sabe do lance do contrato mesmo. E vai acabar contando tudo pra ela!"









    "Eu decidi que ia contar pra ela. Mas não é assim que a Júla tem que ouvir algo daquele tamanho."

    "Saber sobre a infância dela vai mudar a vida dela pra sempre. E se ela descobrir desse jeito..."

    "Uma arma! Um segredo! Várias vidas!"

    "Isso pode mudar o destino da Júlia, do Caio, da Mari, do Téo e principalmente o meu!"

    "O que eu decidir aqui pode alterar toda a nossa trajetória!"

    "O que eu vou fazer?!"

    menu:
        "Avançar no Caio e tentar tirar a arma da mão dele":


            "Eu não sei como que eu vou chegar lá e tirar da mão dele sem tomar um tiro."

            "Minha vida tá por um fio!"

            "Mas se eu não fizer nada, ele pode arruinar a vida da Júlia."

            menu:
                "É o único jeito! AAAHHHH!!":


                    pass
                "Melhor eu não me arriscar e tentar conversar.":


                    jump j8_decisao_caio

            $ renpy.block_rollback()

            scene j8_final8 with hpunch

            pause

            mc "Tô cansado desse seu jeito Caio! Você não manda em tudo!"

            caio "FILHO DA PUTA!!!"

            mari "NÃÃOOOO!!!"
        "Deixar a conversa correr e encontrar uma saída":


            $ renpy.block_rollback()

            label j8_decisao_caio:

                pass

            $ j8_julia_ouviu = True

            "Isso aqui não é filme e eu não sou herói. Sou só um jornalista."

            "Falar é meu forte. Não adianta eu querer dar uma de mocinho aqui. Do jeito que o Caio tá, só ia dar merda."

            mc "Caio... eu... sei do que você tá falando."

            caio "V-você sabe? Como?"

            g "Sabe? Do que VOCÊS DOIS tão falando?!"

            mc "Eu sou um repórter. Esse é meu trabalho. Descobrir a verdade."

            scene black with dissolve

            scene j8_final14 with dissolve

            caio "Pfft... tentando dar uma de alfa numa situação dessas, otário? EU tenho o poder aqui!"

            mc "Presta atenção, cara."

            mc "Você sabe que se alguma coisa acontecer com a Júlia a cabeça de muita gente vai rolar."

            g "Hm?"

            caio "Então você sabe mesmo... não sei como você descobriu isso, mas então agora você entende."

            caio "Eu tenho algo que meu pai precisa."

            mc "Você vai usar ela como moeda de troca pra ter tua vida de volta?"

            caio "Claro que não! Eu quero ter a MINHA vida! Meu pai vai ter que me pagar por ela!"

            caio "E nós dois sabemos que ele tem dinheiro e ela vale MUITO."

            mc "Então esse foi seu plano..."

            scene j8_final15 with vpunch

            caio "Não é um plano, babaca! As coisas tão acontecendo, quer ver, é?! A coisa tá acontecendo!"

            mc "!!!"

            mari "Calma, Caio! Se você atirar em alguém você vai arruinar sua vida! E não só a sua!"

            caio "Tá com medo, é?! Você tá comigo por mim ou pelo meu dinheiro, hein, vadia?!"

            mari "Você sabe que eu te amo!"

            caio "Isso que você fala! Mas eu sempre senti que você faz as coisas pelas minhas costas!"

            mari "Tira essas merdas da cabeça!"

            caio "A verdade é que nenhum de vocês gosta mesmo de mim! Vocês são todos interesseiros!"

            caio "Meu pai me odeia, meus amigos me odeiam, eu tô cheio de lambe-botas do meu lado por causa da grana do meu pai!"

            caio "Mas isso acaba hoje! De um jeito ou de outro!"

            mari "Você tá delirando, amor!"

            caio "Agora eu sou amor, né, sua víbora?!"

            "Ele tá perdendo a cabeça! Se as coisas continuarem assim alguém vai acabar tomando uma bala."

            scene black with dissolve

            scene j8_final16 with dissolve

            g "Claro que você tá sozinho! Você não passa de um babaca!"

            "J-Júlia?!"

            menu:
                "Para, Jú! Agora não!":


                    mc "Jú!"

                    g "Não! Ele precisa ouvir a verdade! É o único jeito!"
                "Eu vou ficar calado":


                    pass

            caio "Isso! Fala logo de uma vez! Pelo menos alguém aqui tem coragem!"

            g "Você é um insuportável que nunca conseguiu nada por si mesmo! Você dependeu do seu pai a vida inteira!"

            g "Comprando os outros com favores e o dinheiro dele. E agora reclama que não tem nada?! Você é um porra de um mimado!"

            g "Se você não gosta disso, você precisa mudar! Conseguir as coisas pelas suas próprias mãos!"



            g "Gente fodida como a gente precisa chegar no fundo do poço pra poder subir! E não tem buraco maior do que você tá agora!"

            caio "TSC!"

            g "Eu também perdi tudo! Todas as pessoas que gostavam de mim! Mas agora eu tô pronta pra reconquistar tudo!"

            caio "Não me compara a você, sua puta!"

            "A Júlia tem razão? O Caio tem salvação?"

            "Eu quero que ele se salve? Ele merece se salvar?"

            menu:
                "Ela tem razão, Caio. Você pode sair dessa.":


                    mc "Não desista!"

                    caio "Eu não quero ouvir palavras bonitas suas, idiota!"
                "Você vai se foder porque nunca vai mudar.":


                    mc "Quem dera esse babaca tivesse coragem pra mudar. Ele não é igual você, Júlia."

                    g "M-mas!"

                    caio "Eu vou meter uma bala nesse cretino!"

            g "Eu que tô falando com você agora!"

            caio "Foda-se o que você acha, cadela! Você nem sabe o quão fodida você é!"

            caio "Você foi vendida pelos seus pais! Você não passa de um objeto pra eles, entendeu?!"

            g "Do que você tá falando, babaca?!"

            caio "Cala a boca! Todo mundo! Eu preciso pensar!"

            g "Ei! Do que você tá falando?!"

            caio "Mandei calar a boca!"

            caio "Minha vida tava tudo certa até esse babaca aparecer e foder com tudo!"

            caio "Você é a causa de tudo que tá acontecendo de errado comigo! E agora a Júlia e meu pai vão pagar!"

            menu:
                "Sua vida sempre foi merda.":


                    mc "Sua vida já tava bem merda antes de mim, cara. Tu não pode me culpar."
                "Eu não me arrependo. Tu mereceu.":


                    mc "Você mereceu! Eu não me arrependo de só falar a verdade."

            scene black with dissolve

            scene j8_final17 with dissolve

            caio "CHEGAAA!!! Parem de me desafiar!!!"

            mari "Caio... por favor... chega... só vamos parar com tudo isso."

            teo "Ela tá certa, cara. Deixa disso. Bora viver nossa vida."

            caio "Eu..."

            menu:
                "Eles têm razão, Caio. Não jogue fora o pouco que você ainda tem.":


                    mc "Só tenha calma!"
                "Parem de enganar ele. Vocês sabem que tudo acabou.":


                    mc "Quem vocês querem enganar? Acabou."

            g "Isso só acaba quando esse merda falar o que ele sabe de mim!"

            caio "Todo mundo falando no meu ouvido! Vocês não falam! Vocês só me escutam!"

            $ renpy.notify("Caio está pensando em tudo o que aconteceu...")

            caio "Merda! O que... eu..."

            menu:
                "Ele tá desconcentrado. É a hora de tirar essa merda da mão dele!":


                    $ renpy.block_rollback()

                    scene j8_final8 with hpunch

                    pause

                    mc "Tô cansado desse seu jeito Caio! Você não manda em tudo!"

                    caio "FILHO DA PUTA!!!"

                    mari "NÃÃOOOO!!!"
                "Eu não tenho coragem. Melhor esperar e ver.":


                    $ renpy.block_rollback()

                    "Acho que a gente tá conseguindo. Ele tá em dúvida."

            caio "AAAHH!!! Eu não sei o que eu faço, caralho!"

            g "Para de ser egoísta! Eu quero saber de mim!"

            caio "AAHHGHH! Tudo tava indo bem até vocês ficarem de amizade!"

            caio "Tudo tá acontecendo por causa desse desgraçado do [mc]! Você colocou minha vida de ponta cabeça!"

            g "Você não vai atirar nele, cretino!"

            if julia_namoro:

                g "Você não vai matar meu namorado!"

            caio "Não quer?! Então eu vou matar você antes, cadela!"

            g "!!!"

            "Não deu nada certo! Ele vai atirar em mim ou na Júlia?!"

            "Eu tenho um segundo!"

            menu:
                "Vou desviar e tentar me salvar":


                    pass
                "Vou pular na frente da Júlia":


                    pass

    play sound som_17_tiro

    scene red with hpunch

    g "[mc]!!!!!! NÃÃOOOO!!!"

    scene j8_final9 with hpunch

    mc "AARGHHH!!!"

    "E-eu... vou morrer assim?!"

    mc "Júlia! Você tá bem?!"

    g "E-eu! E-eu não sei! E você?! Você que é o problema, [mc]!"

    mc "Eu..."

    scene black with dissolve

    scene j8_final10 with dissolve

    pause

    mc "Eu... eu tô vivo..."

    mc "Não pegou em mim. E-eu acho que não pegou em mim!"

    mc "Júlia!!!!!!"

    g "Em mim também não!"

    mc "Mas então! Ele errou?!"

    caio "AAAHH???!!!"

    scene j8_final11 with vpunch

    pause

    mc "MARIII!!!"

    mari "Aaaghh..."

    caio "M-mari... p-por quê?!"

    mari "E-eu... n-não queria... que você... j-jogasse sua vida fora..."

    caio "H-hufhhh!"

    mc "Mari! A gente precisa de uma ambulância! Caio! Faça alguma coisa!"

    scene j8_final12 with vpunch

    caio "E-eu matei ela! Eu realmente matei alguém!"

    caio "Mari! Nãoooo!"

    mc "Para de ser idiota, Caio! Liga pra ajuda! Emergência! 192! 190! Vai logo!"

    caio "E-eu..."

    scene black with dissolve

    scene j8_final13 with dissolve

    pause

    mari "T-tudo que eu queria... era... fazer parte... Ser alguém..."

    mari "S-será que... era demais pra mim?"

    mc "Não gasta energia, Mari! Você vai sair dessa!"

    mc "TÉO!!! LIGA PRA EMERGÊNCIA!!!"

    teo "Eu tô aqui dentro! Tá!!!"

    mari "Eu queria tá com eles... eu... tô cansada..."

    g "Mari! Não!"

    caio "Acabou... acabou tudo..."

    scene black with Dissolve(2.0)

    play sound policia

    pause 2.0

    scene casa_caio geral with Dissolve(2.0)

    pause

    scene black with dissolve

    scene j8_final18 with Dissolve(1.0)

    mc "O que foi aquilo... A Mari não merecia..."

    mc "Vamos rezar pra que eles consigam salvar ela. E ainda sobrou pra gente ter que ir na delegacia prestar depoimento."

    "Logo logo o Tony e o grupo vai saber o que aconteceu aqui. Eu acho que eles têm a polícia na mão."

    g "Você escutou o que ela disse no fim?"

    mc "O-oi? A Mari? Que ela queria 'fazer parte'?"

    g "O que ela queria dizer?"

    menu:
        "Eu não sei também. Alguma ideia?":


            mc "Nada. E você?"

            g "Parece uma coisa muito misteriosa. Mas ela nunca tinha falado disso antes."

            g "Acho que nem o Caio sabia disso. Que a Mari tinha algum objetivo assim."

            mc "Talvez você tenha razão..."
        "O grupo...":


            mc "Eu acho que ela tava falando do grupo que o pai do Caio faz parte."

            g "Grupo?"

            mc "São coisas complicadas, Júlia... não sei se agora é a melhor hora."

            g "Tudo bem... e o Caio?"

            mc "Eu acho que o Caio não faz parte."

            g "Hm..."

    g "Ele sempre foi um lunático, mas nunca pensei que ele tinha coragem pra fazer uma coisa assim."

    mc "É... agora que ele tava com as costas contra a parede que ele partiu pro tudo ou nada."

    g "[mc]... você veio me salvar, né?"

    if julia_namoro:

        mc "Eu nunca ia deixar minha mina em perigo."
    else:


        mc "Não podia deixar minha amiga desse jeito."

    g "Você é um mistério."

    mc "Mistério?"

    g "Quem te vê nunca vai pensar que você vai fazer esse tipo de coisa."

    mc "Tá falando que eu tenho cara de bundão, é?"

    g "Não só a cara... haha..."

    mc "EI!"

    g "Mas é nas horas que precisa que a gente vê o [mc] de verdade."

    g "Todas as vezes que eu precisei, você tava lá pra mim. E dessa vez foi a mesma coisa."

    g "Por isso que eu não entendo. Talvez um dia eu descubra que você é um herói, sei lá."

    menu:
        "Talvez eu seja mesmo. Só escondo muito bem.":


            mc "Quem sabe? Às vezes por baixo da camiseta eu tenho meu uniforme de tanguinha por cima da calça."

            g "Hahaha... só você..."
        "Eu não sou o Peter Parker, relaxa. Fotógrafo e super-herói.":


            mc "Tirar fotos é parte de ser paparazzo, mas é minha única semelhança."

            g "Tá vendo? Esse é um dos problemas. Acho que você pensa pouco de você."

            mc "Sei lá, Júlia. Eu não fico pensando nisso."

            g "Haha... esse é você."

    g "Agora..."

    scene black with dissolve

    scene j8_final19 with Dissolve(1.0)

    pause 2.0

    if j8_julia_ouviu:

        g "Desculpa quebrar o clima, mas... e aquela história, hein?"

        g "Por que o Caio disse tudo aquilo? Que eu fui vendida pelos meus pais? Que eu era um objeto?"

        g "Ele só queria me deixar louca, né?"
    else:


        g "Então é isso? Vamos pra casa? Acho que já tá bom, né?"

        mc "Sim... a polícia deve tá esperando a gente."

        g "Então tá..."

        "E o que eu descobri com o Gevanni?"

    mc "[g]..."

    "Eu decidi contar tudo pra ela. Chegou a hora de falar."

    "Mas olhando pro rosto dela agora... será que vale à pena jogar essa bomba no colo dela mesmo?"

    "Tô começando a ter dúvida do que eu escolhi..."

    "O que eu falar aqui vai mudar a vida da Júlia pra sempre. O que eu faço?"

    menu:
        "Vamos deixar tudo isso pra trás. Amanhã vai ser um dia melhor.":


            mc "Quer saber?"

            if j8_julia_ouviu:

                mc "O Caio só queria te deixar doida mesmo. Eu entrei na conversa, mas claro que não tem nada disso."

                g "Eu sabia! Aquele maldito..."

            mc "Vamos focar no que a gente vai construir a partir de hoje."

            mc "Deixar isso pra trás."

            g "Acho que é o melhor mesmo..."

            g "Sabe? Eu sempre achei que o Caio soubesse algo de mim. Não quero contar tudo agora, tô cansada."

            g "Mas talvez um dia eu te fale."

            g "E quando ele disse aquilo, eu achei que eu finalmente ia descobrir essa verdade."

            g "Mas no fundo eu acho que eu só tava sonhando que tinha algo a mais nisso tudo."

            g "Meus pais só me colocaram pra adoção mesmo. E eu não posso usar isso de desculpa pra não ser feliz."

            if julia_namoro:

                g "Eu quero construir uma nova vida do seu lado, [mc]."

            mc "Assim que se fala! E você sabe que eu sempre vou tá aqui!"

            g "Obrigada. Agora vamos?"

            mc "Vem. Me dá a mão."

            g "Hehe..."



            if julia_namoro and not j8_negou:

                jump julia_final1
            else:


                jump julia_final3_continua
        "Presta bem atenção no que eu vou te contar.":


            mc "Presta atenção em mim."

    g "Hm?"

    mc "Eu achei um lance na sala do Gevanni. E isso vai mudar sua vida pra sempre."

    g "T-tá falando sério?"

    mc "Seus pais assinaram um contrato com a máfia da Capital. Eles te venderam pra pagar uma dívida."

    g "!!!"

    g "Você... você não tá me zoando, né?"

    mc "Não. Eu tirei foto. Você pode ler com calma depois. Olha pra mim agora."

    mc "Tem alguma coisa muito estranha acontecendo. Você não é uma garota normal pra eles."

    mc "Eles querem te proteger. Pro contrato funcionar, a família da Sayuri tinha que te dar abrigo e garantir sua saúde."

    mc "Eu não sei porque a família dela foi escolhida, e também não sei o que eles querem fazer com você."

    mc "Mas eu tenho certeza que tem algo grande em jogo aqui. Alguma coisa doente que saiu da cabeça desses poderosos."

    scene black with dissolve

    scene j8_final20 with Dissolve(1.0)

    pause 2.0

    g "Eu não... eu não sei se eu tô conseguindo te entender."

    mc "É muita coisa pra digerir agora, Jú."

    if julia_namoro:

        mc "Mas eu sou seu namorado. Eu vou tá com você, tá? A gente vai passar isso juntos."

        g "Você... eu só tenho você agora, gato."

    g "Se eles precisam de mim... enquanto eu tiver aqui, eu não vou tá livre, certo?"

    mc "Sim. Você tá segura até que chegue a hora deles fazerem o que querem fazer. Só que... você vai tá sempre sob os olhos deles."

    g "E o Caio e o pai dele sabiam de tudo isso. E os meus pais também. Tanto meus adotivos como meus pais biológicos que me venderam."

    g "O filho da puta tinha razão. Eu não passo de um objeto pra todos eles."

    mc "Tá tudo acontecendo agora, [g]. Você precisa de um tempo pra respirar."

    g "Não..."

    g "Eu não posso deixar eles respirarem. Se eu realmente for fazer isso... precisa ser agora."

    mc "Fazer o quê?"

    g "Você vai saber amanhã. Mas esse Gevanni vai pagar por tudo o que ele fez."

    mc "J-júlia?"

    g "Quando a gente foi no cinema... lembra? Eu tava com uma ideia na cabeça lá."

    g "Não lembro se eu cheguei a contar pra você. Mas agora parece que tudo ficou pronto pra isso."

    menu:
        "Calma. Acho que você tá de cabeça quente.":


            mc "Pera aí..."
        "O que você tá pensando? Me fala!":


            mc "Você não vai me contar?"

    if julia_namoro:

        g "Eu adorei que a gente ficou juntos. Eu tô adorando ser sua namorada."

    g "E adorei que você veio aqui me salvar e se arriscou lá com o FDP pai pra descobrir sobre mim."

    g "Você é o cara mais legal que eu conheci. E até acho que você não merece tá no meio desse rolo todo."

    g "Mas o que eu vou fazer também vai te ajudar eu acho. Por mais que você ache que não no começo."

    mc "Hm? Júlia... não tô gostando desse papo!"

    g "Vai ser melhor pra todo mundo. Até pra mim."

    g "Esse... é o único jeito deles não terem o que eles querem."

    menu:
        "Promete que não vai fazer nada que você não possa voltar atrás!":


            pass

    mc "Júlia! Promete! Não vai fazer uma loucura!"

    g "Calma! Eu sei o que eu tô fazendo. Confia em mim."

    if julia_namoro:

        g "Confia na sua namorada."

    g "Fica bem, tá?"

    mc "Não sei se você sabe o que tá fazendo... mas você é grande. Precisa de ajuda pra voltar pra casa?"

    g "Não. Eu tô bem, sério. O idiota me assustou um pouco, mas ele não fez nada."

    mc "Beleza. Que bom que pelo menos a gente tá são e salvo."

    mc "Eu sinto que as coisas podiam ter dado muito pior hoje."

    if julia_namoro:

        g "Um beijo no pipi, gostoso."

    mc "Até mais, gata."

    g "..."

    scene black with Dissolve(2.0)

    $ dia += 1

    $ tempo = 1

    pause

    "{b}No outro dia{/b}"

    scene cidade dia with dissolve

    pause

    "A Júlia não foi comigo pra delegacia. Nem sei se eles colheram o depoimento dela sobre o Caio."

    "{i}Tuu... tuu...{/i}"

    "E agora ela não tá me atendendo."

    "Será que a Júlia tá bem?"

    "Talvez eu não devesse ter deixado ela sozinha ontem. Ainda mais depois daquela conversa."

    "Qual é o plano dela?"

    scene black with Dissolve(1.0)

    $ dia += 7

    $ tempo = 1

    pause

    scene cidade tarde with dissolve

    pause

    "Uma semana passou e nada da Júlia..."

    "Nenhuma mensagem. A Carol não sabe nada dela também."

    play sound "audio/som_3_celular.mp3"

    scene cidade tarde with hpunch

    "AHH!"

    "Que susto... que número é esse?"

    mc "Alô."

    gi "[mc]! Oi! É o [gi]!"

    menu:
        "Oi! Que que foi? Aconteceu alguma coisa?":


            pass

    gi "As coisas não tão fáceis. Mas não quero incomodar você com isso. Só quero te perguntar uma coisa mesmo."

    gi "Você é amigo daquela garota... Júlia, né?"

    "Como se você não soubesse o nome dela..."

    mc "Sim."

    if julia_namoro:

        mc "Na verdade a gente tá namorando."

    gi "Ah! Então... você... poderia me falar onde que ela tá p-por favor?"

    menu:
        "Eu não sei. Ela não tá me respondendo também.":


            mc "Também tô sem resposta..."

            gi "Sério? A garota desapareceu... e agora que o Caio... enfim..."

            gi "Nenhum dos amigos dela sabe o que aconteceu com a guria."
        "Por que você quer saber? Você tem algo com ela?":


            mc "Vocês têm algo? Pensei que você achasse ela problema."

            gi "Não é nada... é uma coisa pro Caio. Não precisa se preocupar com isso."

            gi "Você sabe?"

            mc "Não. Não falei com ela também."

    gi "Caramba, [mc]... as coisas tão indo de mal a pior!"

    gi "Primeiro o lance com o Caio. O degraçado tá detido! agora essa garota desaparece! Isso vai acabar caindo no meu colo!"

    mc "Meus pêsames sobre o Caio... mas e a Júlia? Por que ela é importante pra você desse jeito?"

    gi "Você não tá entendendo! Quando essa história vazar eles vão vir pra cima de mim!"

    gi "O NBC tá no país todo! Se eu perder a confiança da mesa de diretores eles me tiram daquí!"

    gi "Sabe o que vai acontecer se eu não tiver acesso ao banco?! Você não faz ideia!"

    gi "O banco é o principal alicerce, [mc]! Se você tem interesse em fazer parte, você precisa me ajudar!"

    gi "Nem a porra dos pais dela conseguiram me falar qualquer merda! Ela pode ter se matado numa hora dessas!"

    mc "Se matado?!"

    gi "Ninguém encontra ela, entendeu?! Se pá tá no fundo de um rio!"

    gi "A garota TEM que aparecer! E o Caio não pode continuar na cadeia! Isso me fode! E fode os outros!"

    gi "E pior ainda parece que alguém xeretou minha sala! Tá tudo desabando!"

    gi "A sorte sempre esteve do nosso lado! E agora parece que de uma hora pra outra tudo tá indo pro buraco!"

    if not sayuri_final3:

        gi "E eu acabei de descobrir que quebraram nosso elo na Cidade Chinesa também!"

        gi "Você tá entendendo?! Parece que tem alguém tentando destruir o que a gente construiu!"

        mc "S-sei... poxa..."

    gi "Enfim! Qualquer coisa que você descobrir, por favor me diga! Tô contando com você!"

    gi "E quando eu encontrar quem mexeu na minha sala! Adeus!"

    mc "Uau..."

    "O [gi] ficou fodido."

    "Será que foi a Júlia que passou na sala dele? Será que ele tá falando de mim?"

    "Ele parecia bem consternado... com certeza tem alguma coisa com o contrato."

    "Parece que sem o [gi] no NBC a coisa pode começar a azedar para o tal grupo."

    "É nesse grupo que você queria entrar Mari? Será que se eles acabarem, você vai se sentir vingada?"

    "Por que sem a Júlia, alguma coisa não vai dar certo."

    "Sem a Júlia... no fundo de um rio... o que aconteceu com você, gatinha?"

    if julia_namoro:

        "Eu sou seu namorado... por que você não me chamou? Por que não falou comigo?"

        "Saco!"

    "Espero que você esteja bem..."

    $ julia_completo = True

    "E que você apareça logo! Só pra eu saber que você tá viva."

    scene black with Dissolve(2.0)

    $ julia_completo = True
    $ julia_final2 = True
    $ persistent.julia_final2 = True

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 2 da Júlia! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    pause 2.0

    if not premium:

        call final_free

    jump call_cidade



label julia_final3:

    scene black with dissolve

    scene hub_bar_fundo cenario with Dissolve(2.0)

    "Ufa... finalmente um tempinho de descanso."

    play sound som_36_cadeira

    show hub_bar mc with dissolve

    "Assalariado também merece gastar um pouco no bar."

    "A situação não tá fácil."

    show hub_bar fabricio with dissolve

    gar "Que feição ausente de vitalidade apresentas, meu nobre companheiro de jornada terrena."

    mc "Opa, [gar]. Eu tava pensando numa coisa..."

    gar "Há vezes em que pensar perde seu propósito e é deveras interessante deixar de fazê-lo."

    mc "E se eu não pensar, o que eu faço?"

    play sound som_porta

    gar "Sua resposta chega de capa e espada para lhe salvar neste momento de infortúnio."

    mc "Minha respos-"

    mc "!!!"

    "???" "Oiii!"

    scene julia_final3_img1 with hpunch

    g "Que saudades!"

    mc "O-oi!"

    g "E aí, gatinho!? Que 'oi' foi esse?"

    mc "Tu quase me matou do coração!"

    g "Não é esse tipo de oi que eu quero que você dê! Eu prefiro mais um 'oi' tipo gemido, mais 'aaiii!'."

    mc "Você tá bem?!"

    g "Por que você tem essa mania chata de ficar se preocupando com a gente, hein?"

    mc "Cala a boca. Desde quando se preocupar com os outros é ruim?"

    g "Foda-se. Não vou brigar com você por causa disso, mané."

    mc "Mas você que come... deixa pra lá. Você realmente é a Júlia."

    g "Exatamente! Eu sempre vou ser essa aqui!"

    menu:
        "Eu acho que você mudou, sim.":


            mc "Pra mim você mudou bastante. Eu vi lá na casa do Caio."

            g "Q-quê?! Eu só tava depressiva!"
        "Talvez você não tenha mudado mesmo.":


            mc "Talvez não mesmo. Mas e lá na casa do Caio?"

            g "Não lembro do que você tá falando."

            mc "[g]!"

    g "Às vezes a gente tá pra baixo. Não quer dizer nada."

    mc "Então me responde uma coisa."

    g "Se eu tô com a calcinha ensopada?"

    menu:
        "Isso. Você tá?":


            g "Eu sempre tô! Ainda mais quando eu tô me esfregando num gostoso."

            mc "A é? Quem sabe a gente não pode resolver isso?"

            g "Você quer ter certeza? Pode sentir, com língua? Daí você aproveita e 'resolve'."

            mc "Você tá parecendo a Júlia que eu conheço mesmo."

            g "Viu só?"

            mc "Então quer dizer que você continua vendo o Caio e o pessoal lá."
        "Não. Eu quero saber do Caio.":


            mc "Sem brincadeira. Eu quero saber se você ainda tá vendo o Caio."

            mc "Mesmo depois do que acontece lá no apê dele."

    g "Sim. Aquele zé roela é um idiota, o Téo também, e a Mari é estranha, mas eles são meus amigos."

    menu:
        "Eles são tudo, menos seus amigos.":


            mc "Amigos o caralho."

            g "Você entendeu. Eles são esse povo que tão comigo."
        "Eu nem falo mais nada.":


            mc "Vou nem falar mais nada."

            g "Melhor mesmo."

    scene black with dissolve

    scene julia_final3_img2 with Dissolve(1.0)

    mc "Só não entendo por quê. Você só sofre nessa situação."

    g "Eu sinto que tem alguma coisa no Caio que é muito mal explicada."

    menu:
        "Talvez o fato dele ser bissexual?":


            mc "Talvez a peça que tá faltando pra você é saber que ele é bissexual."

            g "O Caio? O Caio não é bissexual!"

            mc "Ele é. Tô falando."

            g "O Caio é gay mesmo! Ele só fica com mulher pra esconder."

            mc "Você... sabia?"

            g "Acho que é bem fácil de perceber, né? Todo aquele ódio que ele tem por mulheres e por tudo no geral."

            g "A necessidade de tá por cima, de sentir que tá controlando tudo. Isso aí é coisa de enrustido."

            mc "Agora tô chocado. Eu tinha esquecido como seu Quoficiente Emocional é alto..."

            g "Eu tô melhor da cabeça que todos vocês juntos."

            mc "Haha... quem sabe. Talvez no fundo eu que não saiba nada."
        "Melhor não falar nada":


            "..."

    g "Você que vai ficar depressivo agora? Quer um boquete?"

    mc "[g]..."

    g "Que foi?! É uma delícia!"

    mc "Ouvir você falando assim... parece que nada mudou mesmo."

    g "E por que ia mudar? As coisas tão boas assim."

    menu:
        "Certeza?":


            mc "Você tem certeza?"
        "Claro que não tão. Você quase teve um treco.":


            mc "Eu lembro do ataque que tu teve lá no apê."

            g "Para de ser tão dramático, [mc]. Esquece isso!"

    g "Às vezes eu tenho umas recaídas, tenho. Mas e daí? Quem que não tem?"

    g "Todo mundo é problemático. Todo mundo é fodido. Não quer dizer que todo mundo precisa mudar."

    mc "Provavelmente precisa, sim."

    g "Ah, para! A gente vai cambaleando, mas vai pra frente!"

    menu:
        "E o lance com a Carol e a Sayuri?":


            pass

    g "Ah... você quer mesmo fazer drama, né?"

    mc "Tô falando sério. O que você vai fazer com relação a isso?"

    g "O que eu posso fazer? Nada. Se as duas querem distância, as duas que sumam."

    mc "E daí você volta pra vida normal. Atrás de Caio, Mari e o Téo."

    g "É. Sempre foi assim."

    mc "Júlia... eu andei tanto com você nesse tempo. Foram poucas e boas... e agora ver você acabar do jeito que começou?"

    g "E que que tem? Da minha vida cuido eu. A gente sempre foi um casinho mesmo. Só um contatinho."

    mc "..."

    g "Que foi?"

    mc "Acho que bateu uma deprê."

    g "Eu sabia que tu ia acabar ficando depressivo. Tava na cara."

    mc "Eu achei que essa história toda ia acabar diferente, sabe?"

    g "A vida não é um filme. As pessoas não mudam."

    g "Desde o começo eu tenho meu caminho. E eu vou continuar com ele, porque mesmo caindo às vezes, eu me divirto."

    g "Não tem como a gente resolver nossa vida. A gente só dá nosso melhor a cada dia."

    mc "Então esse vai ser seu caminho mesmo."

    g "Acho que foi esse caminho que me encontrou, gato. Eu não procuro nada. Eu só sigo o que me dá na telha."

    g "Talvez você devesse parar de tentar controlar tudo e só curtir. Pensar demais atrapalha."

    menu:
        "Nossa história foi um grande nada.":


            pass

    scene black with dissolve

    scene julia_final3_img3 with Dissolve(1.0)

    mc "É... Mas e nossa história? Eu sinto que tudo foi um grande nada agora."

    mc "A gente não ficou juntos, e eu também não consegui te ajudar a sair da relação tóxica com o Caio."

    mc "O Caio também não teve o que mereceu. Vai continuar sofrendo com o pai, e ferrando você e a Mari."

    if sayuri_final3:

        mc "Foi assim com a Sayuri também."

        g "Com a mana?"

        mc "Eu não fiquei com ela, não virei um Imortal e também não acabei com a Jidao."

        g "Qual o problema? Você não é um super herói. Tu não tem que fazer nada."

    mc "Então pra que serviu tudo isso?"

    g "E por que as coisas precisam servir pra algo? Para de pensar demais, bobo. É tudo sobre a viagem."

    mc "Parece que eu tô sempre escolhendo o caminho do meio. Será que eu sou um bundão?"

    g "Hahaha... você tá depressivo mesmo."

    g "Posso tirar essas coisas da sua cabeça com uma bela chupada. Mas você não quer."

    mc "Eu tô falando sério!"

    g "Eu também. Mas tá certo. Se quiser, eu posso ser sua psicóloga hoje."

    menu:
        "Você? Só pode ser brincadeira.":


            mc "Ouvir lição de moral da Júlia é o fundo do poço."

            g "Ei! Eu sou sabida, viu?!"

            mc "Pfff!"
        "Tá bom. Manda aí.":


            mc "Qual a dica da psicóloga Júlia, então?"

            g "Escuta só."

    g "Naquele dia na casa do Caio eu te falei todas as coisas boas que você fez pra mim."

    mc "Você só tava depressiva querendo me manipular."

    g "Hahaha! Calma aí! Tá parecendo adolescente agora. Acorda, homem!"

    g "Eu tô falando sério. Você sabe o que você fez por mim."

    g "Nem minha irmã e nem minha melhor amiga aceitam falar comigo. E você tá aqui."

    g "O cara que eu conheci tentando dar um golpe pra afastar da minha mana. Você podia ter só me batido, processado, sei lá."

    g "Só que você viveu tudo isso comigo. Foram meses de aventuras e muita safadeza!"

    g "Só porque as coisas não terminaram como você esperava, não quer dizer que deram errado."

    menu:
        "Até que eu curti aqueles momentos.":


            mc "Lembrando agora... até que nossos momentos foram divertidos."

            g "Né?! Eu também acho!"
        "Minha história com você foi sofrível.":


            mc "Não sei do que você tá falando. Tudo que a gente viveu foi sofrível."

            g "Isso que tu acha agora que tá nesse climão."

    scene black with dissolve

    scene julia_final3_img4 with Dissolve(1.0)

    g "Nós dois vamos seguir assim. Meio que cambaleando, caindo de vez em quando, mas a gente vai chegar longe."

    g "E não precisa pensar demais. Razões, o que é certo, que é errado. Só vamo em frente, cara!"

    mc "É. Talvez a gente não tenha uma grande missão pra realizar no mundo mesmo. Só tamo vivendo."

    g "E não é melhor assim? Por que a gente quer tanto aparecer? Por que ficar buscando uma coisa especial?"

    g "Isso é cansativo. E tudo fantasia também. Uma vida normal é muito melhor."

    g "Tira esse peso das costas. E vai viver a vida do seu jeito. Deixa os outros serem os heróis e heroínas."

    mc "Olha... falando assim, pode ser que você tenha razão mesmo. Esse lance de peso. Você não é a primeira."

    g "Tô falando, delícia! As pessoas tão toda hora procurando uma razão pra se sentir especial!"

    g "Eu não quero saber disso! Eu vou fazer minhas coisas! Chorar meu choro e sorrir meu sorriso!"

    menu:
        "Pode ser que seja o melhor mesmo.":


            mc "Talvez seja o melhor. Seguir meu caminho e parar de ficar querendo fazer a diferença."
        "Não concordo. Acho que você só tá fugindo.":


            mc "De jeito nenhum. Pra mim, você só quer fugir da responsabilidade."

            g "Blergh!"

    g "Eu conheço seu jeito, [mc]. Eu tenho certeza que você ainda vai mudar a vida de muita gente."

    mc "Você não é uma delas."

    if sayuri_final3:

        mc "E nem a Sayuri."

        g "Nem vem com essa. Você sabe como a mana mudou por sua causa."

        g "Ela era um bicho do mato e agora até tem coragem de me chutar."

    g "Eu sou um caso diferente. Eu nunca quis mudar. Minha vida nunca me incomodou. Tá, as vezes sim, mas no geral não."

    mc "Hah... faz sentido. Acho que eu criei uma realidade na minha cabeça. Que eu ia te tirar de tudo isso."

    g "Isso que eu tô falando. Essa é nossa mania de querer ser herói."

    g "Deixa as pessoas seguirem o caminho delas. Se elas não te pedirem ajuda, só dexa elas irem."

    mc "É... tanto faz o que eu penso. A vida é delas, não minha."

    g "Falou tudo agora. Eu acho que muita gente não entende isso. Fica julgando os outros."

    g "Foca nas suas coisas. Na sua vida. E vai viver tua história, mano. Oxi!"

    menu:
        "Como você disse, eu ainda vou ajudar outras pessoas.":


            mc "Seu discurso não me comprou, não. Eu ainda vou ajudar as pessoas."

            g "É sua cara! Eu sei que tu vai, gato!"

            mc "Mas se não é seu caso, eu só posso te dar o boa sorte."
        "Você tá mais acertada que eu.":


            mc "É. Parece que você tá mais certa do que vai fazer do que eu. Tenho que encontrar meu caminho."

            g "Já falei que não tem caminho. Só vai viver, homem."

    mc "Vô torcer pra dar tudo certo pra você nessa vida normal aí."

    g "Valeu, gato. E eu tô torcendo pra você parar de ser bobo e querer ficar carregando a mulherada nas costas."

    g "E se você precisar de um chacoalhão, pode me chamar. Eu vou te mandar umas bem na tua cara."

    g "Ou também, né... se tiver precisando esvaziar o tanque... a gente pode ver isso também."

    menu:
        "Eu que não vou recusar uma baguncinha.":


            mc "Bom... falando assim... com aquela história de molhada."

            g "Eu sempre vou querer sua língua bem aqui no meinho."

            mc "Safada."

            g "Sempre que você quiser."
        "Só um papo tá de bom tamanho.":


            mc "Pode ser que eu queira outra sessão."

            g "Você tem meu telefone."

    mc "Valeu pela injeção de ânimo. Você até que é uma boa psicóloga."

    g "Eu estudo biologia... talvez eu devesse mudar de curso."

    mc "Já seria uma mudança."

    g "Nah... deixa pra lá."

    mc "Haha..."

    mc "Fica bem, Jú."

    g "Você também, gostoso. Não esquece que você vai tá sempre comigo."

    g "Principalmente quando eu tiver sozinha no quarto. Eu vou lembrar de você."

    mc "Pode lembrar. E eu vou dar uma olhadinhas em umas fotos que você me mandou."

    g "Se pá te mando outras de vez em quando, pra dar aquele tesão gostoso."

    mc "Adeus, Jú."

    g "Adeus, meu mano. Beijo no piupiu."

    scene black with dissolve

    scene parque noite with Dissolve(1.0)

    "Acho que vai ser a última vez que eu vejo a [g]."

    "Agora eu só posso torcer pra que ela seja feliz no caminho que ela escolheu."

    "Eu também vou encontrar meu caminho, [g]. Continue torcendo por mim. E seja feliz pra sempre."

    scene black with Dissolve(2.0)

    $ julia_final3 = True
    $ persistent.julia_final3 = True

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 3 da Júlia! Você pode acessar o menu Personagens e apertar no botão dela para ver sua conquista!{/b}"

    pause 2.0

    if not premium:

        call final_free

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
