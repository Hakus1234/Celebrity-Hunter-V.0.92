

label priscila_evento2:

    $ tempo += 1

    scene ilha parque with Dissolve(2.0)









    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial pra você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você precisa esquecer a sedução um pouco e ser amigo da [c]."

        p rindo "E aí? Você vai preferir a pauta ou ver mais sacanagem? Aqui, você decide! Boa sorte!"

    "O parque fica bem perto da minha casa e do meu trabalho."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p2_save", extra_info="p2_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "Na verdade, nós estamos em uma ilha separada do centro da capital."

    "Nossa ilha é muito usada como local turístico. É como um grande parque de diversões com bares, um grande hotel, um cassino..."

    "E é por isso que diversos famosos acabam vindo para cá."

    "Ufa..."

    if priscila_cel_msg2_r == "zoado":

        scene pri2_img1 with dissolve

        pause

        "Ela tá ali sentada..."

        "Ainda mais bonita que no bar."

        mc triste "Espero que eu não tenha demorado demais..."

        "..."

        mc normal "Olá!"

        scene black with dissolve

        scene ani09 with Dissolve(1.0)

        pause

        "U-uou!"

        "Olha só pra aqueles melões balançando!"

        "E ela ainda não usa sutiã... vão pular pra fora daqui a pouco!"

        "Essa Priscila com certeza é bem ousada no visual."

        "Fico imaginando como é ser desejada por milhões de pessoas no país inteiro..."

        c "Oi!"

        scene black with dissolve

        scene pri2_img2 with dissolve

        pause
    else:


        mc feliz "Ela parece não ter chegado ainda."

        "Isso é bom. Eu queria chegar antes dela."

        "Ser um cavalheiro é muito importante para impressionar uma garota."

        mc zerado "Pelo menos é o que parece nos filmes..."

        c "[mc]?!"

        mc "Ah! Ela tá no outro banco!"

        scene black with dissolve

        scene ani09 with Dissolve(1.0)

        pause

        "U-uou!"

        "Olha só pra aqueles melões balançando!"

        "E ela ainda não usa sutiã... vão pular pra fora daqui a pouco!"

        "Essa Priscila com certeza é bem ousada no visual."

        "Fico imaginando como é ser desejada por milhões de pessoas no país inteiro..."

        c "Oi!"

        c "Escutei você falando de filmes! Que filmes? O meu?"

        mc surpreso "Nã-não! Nada não..."

        c "Vamo sentar?"

        mc "Claro."

        scene black with dissolve

        scene pri2_img2 with dissolve

        pause

        c "Você é engraçado."

        mc envergonhado "Haha..."

    c "Obrigada por ter vindo. Te atrapalhei?"

    menu:
        "Claro que não.":


            $ priscila_amizade += 1

            mc normal "Claro que não. Eu gostei bastante da nossa noite."

            c "Eu também gostei de conversar com você."
        "Mais ou menos...":


            mc desculpa "Eu tinha algumas coisas pra resolver, mas tudo bem."

            c "Desculpa... É que..."

            mc normal "Não precisa se desculpar. Não é pra tanto assim."

            c "Eu tava meio ansiosa pra falar com você."

            mc desconfiado "Por que?"
        "Eu tava louco pra te ver de novo.":


            $ priscila_seducao += 1

            mc charmoso "Depois da nossa noite, eu tava louco pra te ver de novo."

            c "A é?"

            mc charmoso "Sim. Depois do que aconteceu no bar, quero te conhecer melhor."

            c "..."

    c "Olha..."

    c "Eu queria falar sobre a outra noite, no bar..."

    menu:
        "Espero que você tenha gostado tanto quanto eu.":


            $ priscila_seducao += 1

            mc charmoso "Espero que você tenha gostado do nosso encontro tanto quanto eu."

            c "..."

            c "Eu gostei..."

            c "Mas eu sinto que as coisas não aconteceram como deveriam."
        "Sinceramente, não quero falar sobre isso.":


            mc desculpa "Não quero ser grosso, mas, sinceramente, não quero falar sobre isso."

            c "Eu também não queria falar, mas se..."

            c "Se a gente for continuar se vendo, quero deixar as coisas claras."
        "Não precisamos falar sobre isso se não quiser.":


            $ priscila_amizade += 1

            mc triste "Não precisamos falar sobre isso se não quiser."

            c "Obrigada pela gentileza, mas nós precisamos conversar."

    scene pri2_img4 with dissolve

    pause

    c "Eu pensei muito sobre o que aconteceu e eu não estava normal."

    c "Uma coisa tinha acontecido e eu estava meio... fragilizada..."

    c "Eu precisava muito conversar com alguém... e você estava lá."

    if priscila_amizade_evento > 0:

        c "Eu sei que pareceu estranho... Mas eu precisava mesmo daquilo."

        c "Você foi um verdadeiro amigo. Me ouviu e não me julgou."

        c "Normalmente eu não consigo me abrir com outras pessoas, só que no bar com você eu consegui."

        c "Eu sei que parece bobeira... mas foi muito especial pra mim..."

    elif priscila_seducao_evento > 0:

        c "Eu sei que as coisas avançaram muito rápido..."

        c "Eu não sei como explicar, mas você mexeu comigo dessa forma..."

        c "..."

        c "... Eu tô muito envergonhada, mas queria deixar claro que eu nunca tinha feito algo assim..."

        c "E... mesmo... muito envergonhada..."

        c "Eu não achei ruim..."

    menu:
        "Focar no decote":


            mc tarado "..."

            scene pri2_img3 with dissolve

            pause

            "A roupa dela tem um decote gigante..."

            "Ela é realmente ousada."

            mc tarado "..."

            "O jeito que ela está levantando o braço está aumentando ainda mais o espaço..."

            "Daqui dá até pra ver..."

            "..."

            scene pri2_img5 with hpunch

            c "Ei!"

            c "Você tá me ouvindo?"

            c "O que você tá olhando!?"

            mc surpreso "Eu... eu..."

            mc desculpa "Eu achei que tivesse caído algo em você e me distraí..."

            c "..."

            mc desculpa "Eu não te ouvi direito... Perdão..."

            $ renpy.notify("Priscila está avaliando suas ações no encontro...")

            c "Tudo bem. Mas isso é algo importante pra mim!"

            mc desculpa "Eu sei... E eu acho que eu entendi."

            mc desculpa "Não quero que você fique pensando besteira por causa do bar."

            mc normal "Eu quero que você seja você mesma do meu lado."

            c "É verdade?"

            mc normal "Claro! É justamente seu lado verdadeiro que eu gostei em você."
        "Eu quero ser um amigo que você pode confiar.":


            $ priscila_amizade += 2

            mc normal "Olha... Eu sei que você se abriu comigo e agora tá se sentindo vulnerável."

            mc "Mas pode confiar em mim."

            mc "Eu sei que parece estranho porque eu trabalho em uma revista de fofoca... Mas não quero arrancar segredos de você."

            mc "Eu quero que você possa falar comigo o que você quiser, na hora que você quiser."

            scene pri2_img2 with dissolve

            mc feliz "E se no bar você precisava desabafar, eu me sinto muito feliz de poder te ajudar."

            $ renpy.notify("Priscila está avaliando suas ações no encontro...")

            mc normal "Eu achei você alegre, divertida e principalmente verdadeira."

            mc "E é por isso que eu quero ser seu amigo."

            mc normal "..."
        "Eu quero você completamente, do jeito que você é.":


            $ priscila_seducao += 2

            mc charmoso "Não me importa esse tipo de coisa."

            mc "No momento em que eu vi você no bar, eu soube que eu ia querer saber tudo sobre você."

            mc "Essa insegurança não combina com você."

            mc "Você é uma mulher linda, ousada, e que sabe o que quer."

            mc "No bar você me respondeu com confiança, e se deixou levar pelo momento, aproveitando ao máximo nosso encontro."

            mc "E é isso que me conquistou."

            if priscila_seducao >= 7:

                window hide

                scene pri2_img6 with dissolve

                pause

                c "Con-conquistei?"

                mc "Sim."

            mc "Você mexe comigo."

            mc "Eu só consigo pensar em você. Eu só consigo pensar em estar com você."

            $ renpy.notify("Priscila está avaliando suas ações no encontro...")

            if priscila_seducao >= 7:

                c "Você... mexe comigo também..."

                mc "Eu sei. E é isso que eu quero."

                c "Ah..."

                c "Você é confiante. E fala de uma forma que ninguém falou comigo."

            mc "Os homens têm medo de você. Mas eu não tenho."

            mc "Eu quero você do jeito que você é. Por isso, não se preocupe com o bar."

            c "..."

    if priscila_seducao >= 7:

        label priscila_e2_finalseducao:

            $ persistent.priscila_cena3 = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e2_seducao","seducao","resultado")

        $ priscila_e2 = "seducao"

        mc charmoso "Você entendeu o que eu quero?"

        $ renpy.notify("Priscila achou você sexy e charmoso...")

        c "Sim..."

        "Ela parece paralisada, mas não vou parar agora. Eu sei o que fazer."

        "Vou me aproximar e mostrar pra ela na prática o que eu quero."

        scene pri2_img7 with dissolve

        pause

        mc "Eu quero ser mais do que um amigo."

        c "Ah..."

        "Ela está tremendo..."

        "Meu coração vai sair pela boca... mas não posso mostrar pra ela."

        "Vou pressionar ela na parede e conduzir."

        "O braço dela... consigo sentir ele nas minhas costas. Ela está aceitando."

        mc "Você me quer também?"

        c "Eu... Ah..."

        $ renpy.end_replay()

        mc "Eu sei que..."

    elif priscila_amizade >= 6:

        label priscila_e2_finalamizade:

            $ persistent.priscila_cena4 = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e2_amizade","amizade","resultado")

        $ priscila_e2 = "amizade"

        $ renpy.notify("Priscila achou você confiável e um verdadeiro amigo...")

        c "Você... [mc]..."

        c "Parece que você sempre sabe o que dizer."

        c "Quando eu tô do seu lado parece que eu posso..."

        c "..."

        mc "..."

        scene pri2_img8 with dissolve

        pause

        c "..."

        "Não sei o que fazer..."

        "Ela veio e me abraçou do nada."

        mc "..."

        "Acho que ela está chorando..."

        c "..."

        mc "..."

        c "Eu..."

        mc "Não precisa falar nada."

        mc "Estou aqui pra você."

        c "Obrigada... Muito obrigada, [mc]."

        mc "Às vezes as coisas parecem que vão nos esmagar."

        mc "Eu mesmo... Se não fosse por você eu teria perdido meu emprego."

        c "..."

        mc "Você me salvou."

        mc "E agora eu quero fazer o mesmo. Pode confiar em mim. Você está segura aqui."

        c "..."

        c "..."

        c "As coisas não estão fáceis pra mim."

        c "Eu consegui algo incrível. Vou estrelar o novo filme de [diretor]..."

        c "Vai ser o filme mais caro... já produzido no país."

        c "Mas..."

        c "Mas o que..."

        c "O que eu tive que fazer pra conseguir o papel é repugnante."

        c "Tenho vontade... de vomitar só de pensar nisso..."

        menu:
            "Você já falou o suficiente.":


                $ priscila_amizade += 1

                mc "Calma... Você já falou o suficiente sobre isso. Precisa tirar isso da sua cabeça."

                c "Obrigada..."
            "O que você teve que fazer?":


                mc "O que você precisou fazer que era tão horrível?"

                c "Não... não posso falar."

                c "Não tenho coragem..."
            "...":


                c "Você me odeia?"

                mc "Claro que não. E você não devia pensar mais nisso. Não te faz bem."

        c "Um dia, talvez, eu te explique tudo..."

        $ renpy.end_replay()

        mc "Não se preocupe. Eu vou sempre estar..."
    else:


        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e2_fracasso","nada","resultado")

        $ priscila_e2 = "fracasso"

        c "Mas eu não quero que você se preocupe demais."

        c "Estamos apenas nos conhecendo e não quero que isso estrague o que a gente ainda pode criar."

        mc normal "Com certeza não vai estragar nada."

        mc "Eu quero que a gente se conheça melhor."

        c "Eu também."

    scene pri2_img9 with hpunch

    "Menina Histérica" "OLHA A PRISCILA!"

    "Menina Histérica" "É VOCÊ MESMO!!"

    c "!?"

    c "Eu... eu..."

    "Menina" "NÃO TÔ ACREDITANDO!"

    c "Calma... calma..."

    c "Está tudo bem. Como é seu nome?"

    "Jasmine" "Jasmine. Eu te amo, [c]!"

    c "Dá só um minutinho, [mc]."

    mc "Claro... ser famosa é assim, né?"

    c "É difícil ter criança aqui na ilha... mas parece que uma é suficiente pra me conhecer..."

    mc "Haha..."

    scene black with dissolve

    scene pri2_img10 with dissolve

    c "Muito obrigada, Jasmine. Eu amo você também."

    "Jasmine" "He he..."

    "..."

    "Jasmine" "O que vocês tavam fazendo?"

    c "A gente?!"

    if not priscila_e2 == "fracasso":

        "Jasmine" "É! Quando eu cheguei vocês estavam acho que se abraçando..."

    "Jasmine" "Vocês são namorados?"

    c "Que?! Namorados?!"

    c "É..."

    menu:
        "Somos namorados, sim.":


            $ e1_priscila_namorado = "namorado"

            mc charmoso "Sim. Nós estamos namorando. Meu nome é [mc]. Muito prazer."

            c "Que?!"

            mc "Não precisa ficar com vergonha, amor."

            "Jasmine" "Oohh..."

            c "Eu... eu..."

            mc "Você fica linda quando tá com vergonha..."

            c "Eu..."

            c "..."

            c "{size=15}Você quase me matou de vergonha...{/size}"
        "Não. Somos apenas conhecidos.":


            $ e1_priscila_namorado = "nada"

            mc normal "Somos apenas conhecidos. Não é namoro."

            c "Isso!"

            "Jasmine" "Ah tah..."

            mc normal "A gente se conheceu esses dias."

            c "Ele... estava só me ajudando a limpar minha roupa."

            mc normal "Exatamente."

            mc feliz "Tinha caído uma centopéia em cima da [c]!"

            "Jasmine" "Eca!"

            c "Hehe... {size=15}Obrigada...{/size}"
        "...":


            $ e1_priscila_namorado = "silencio"

            c "É... É..."

            c "Não!"

            c "Ele é apenas um amigo..."

            c "Isso..."

            if not priscila_e2 == "fracasso":

                "Jasmine" "Ah tah... É que vocês estavam se abraçando, não estavam?"

            c "É..."

            if not priscila_e2 == "fracasso":

                c "Mais ou menos... Eu só caí... Isso... Eu caí e ele me ajudou."

            mc feliz "Ha ha... Tá engraçado ver você se explicar."

            c "..."

            c "{size=15}Você fica só rindo aí... Você vai pagar por isso...{/size}"

    "Jasmine" "..."

    "Jasmine" "Você é tão linda, [c]... Igual nas revistas..."

    c "Você é linda também, sua fofa! Deixa eu te dar um abraço!"

    "Jasmine" "He he..."

    c "Pronto!"

    "Jasmine" "Não tô acreditando que eu tô te vendo ainda..."

    "Hmm... eu tô com uma sensação estranha..."

    "Parece que tem alguém ali..."

    scene pri2_img11 with dissolve

    pause

    $ cassia_evento = True
    $ cassia_evento1 = True

    "!"

    "O que é aquilo?"

    "Parece que ela tá olhando na nossa direção..."

    "..."

    "Espera..."

    "O pior é que eu acho que eu conheço aquela mulher... Não acredito..."

    "Mulher" "Jasmine!"

    "Agora tem uma outra mulher gritando dali..."

    scene pri2_img10 with dissolve

    "Jasmine" "Ah não! Minha mãe!"

    c "É melhor você ir, senão ela não vai mais deixar você ser minha fã."

    "Jasmine" "Tá bom..."

    "A mulher com a câmera foi embora... Deve ter percebido que eu vi ela..."

    "A desgraçada deve ter ido pra redação... Tenho que ir o mais rápido possível falar com {b}ela{/b}."

    "Antes eu tenho que terminar meu lance com a Pri."

    c "Mas antes de ir, um beijo!"

    "Jasmine" "He he..."

    "Jasmine" "Tchau!"

    c "Tchau, linda!"

    "Mãe da Jasmine" "Jasmine, venha logo!"

    scene black with dissolve

    c "Ufa..."

    scene pri2_img2 with dissolve

    menu:
        "Aleluia ela foi embora, hein?":


            mc angustiado "Aleluia ela foi embora, hein?"

            scene pri2_img12 with dissolve

            c "Eu sei que elas às vezes podem atrapalhar um pouco..."

            c "Mas eu realmente gosto deles."

            c "Essa ilha ainda é muito boa para descansar da rotina, porque aqui não tem muita criança."

            c "Você tem que ver no resto da cidade como é..."
        "Incrível como você tem jeito com as crianças!":


            mc feliz "Incrível como você tem jeito com as crianças!"

            $ priscila_amizade += 1

            c "Eu realmente gosto dos meus fãs."

            c "A maioria deles são crianças e adolescentes. Eles são sinceros e não têm vergonha de demonstrar carinho."

            mc normal "Essa menina de agora realmente admirava você."

            c "Eu acho que é algo que você precisa se acostumar, quando se é conhecido..."

            c "Eu espero ser um bom exemplo pra ela..."

        "O timing dela não podia ter sido melhor..." if priscila_e2 == "seducao":

            mc envergonhado "O timing dela não podia ter sido melhor..."

            $ priscila_seducao += 1

            scene pri2_img6 with dissolve

            c "Eu sei..."

            mc charmoso "Não precisa se preocupar."

            mc "Eu espero que a gente tenha outras oportunidades como esta."

    if priscila_e2 == "seducao":

        scene pri2_img6 with dissolve

        c "..."

        c "Você foi incrível... antes dela chegar..."

        c "Eu..."

        c "Eu não sei o que falar..."

        mc charmoso "Eu quero que você saiba como eu me sinto."

        c "Você me deixa sem jeito..."

        mc normal "Vamos deixar aqui por hoje. Eu acho que nosso encontro foi perfeito."

        c "Me desculpe qualquer coisa..."

        c "Eu não sei direito como reagir..."

        mc charmoso "Não se preocupe. Você é linda do jeito que você é."

        c "..."

    elif priscila_e2 == "amizade":

        scene pri2_img2 with dissolve

        c "Obrigada de novo... Por me ajudar."

        c "Antes dela chegar você foi um verdadeiro amigo."

        c "Eu me senti realmente bem ao seu lado."

        mc normal "Eu fico feliz de poder conhecer você melhor."

        mc "Espero que a gente continue se conhecendo. Você é uma excelente companhia."

        c "Eu concordo..."

        c "Sou uma excelente companhia."

        mc feliz "Haha..."

        c "Brincadeira."

        mc "Mas você é! Não precisa ficar sem jeito..."

        c "..."
    else:


        scene pri2_img12 with dissolve

        c "O que você estava dizendo antes dela chegar?"

        mc concentrando "Hmm..."

        mc "Ah! Que você não precisa se preocupar que o que aconteceu no bar não vai estragar o que eu acho de você."

        mc "Por isso não se preocupe."

        scene pri2_img2 with dissolve

        c "Obrigada, [mc]."

        "..."

    mc normal "Eu gostei muito de passar esse tempo com você."

    scene pri2_img2 with dissolve

    c "Eu também!"

    c "E pra mostrar como eu gostei do seu papo, tenho um presente pra você."

    mc desconfiado "Presente?"

    c "Não precisa me olhar assim! É sério!"

    mc desconfiado "Ok..."

    c "Este cartão te dá direito a um curso de massagem gratuito!"

    c "Eu tenho uma amiga aqui e ela me deu, mas logo vou deixar a ilha."

    c "E como hoje você foi um cavalheiro, resolvi dar de presente."

    c "Pode se sentir agradecido!"

    menu:
        "Muito obrigado. Com certeza vou fazer.":


            mc feliz "Que legal! Com certeza vou querer fazer."

            scene pri2_img12 with dissolve

            c "Você não é obrigado, ok? Não quero que se sinta obrigado."

            mc triste "Não, não! Eu entendi..."

            c "Mas fico feliz que você tenha gostado."

            mc normal "Sim..."
        "Só se eu puder praticar massageando você.":


            mc tarado "Só se eu puder praticar massageando você..."

            $ priscila_seducao += 1

            scene pri2_img6 with dissolve

            c "Haha! Vamos ver."

            c "Não seja apressado."

            c "Quem sabe depois que você fizer algumas aulas..."

            mc charmoso "Vou cobrar, hein?"

            c "Ok..."
        "Obrigado! Só tenho que ver se vou conseguir fazer.":


            $ priscila_amizade += 1

            c "É um presente, bobinho..."

            c "Você não é obrigado, ok?"

            mc normal "Eu gostei do presente! Mas é que tem tanta coisa acontecendo ultimamente..."

            c "Isso que eu tô falando. Prefiro que você faça só se tiver vontade."

            c "Não quero que faça só porque eu dei, senão seria um castigo e não um presente."

            mc feliz "Verdade."

    c "..."

    mc triste "Droga... Vou ter que ir agora."

    scene pri2_img1 with dissolve

    c "Verdade?"

    mc "Sim... Tenho que passar na redação ainda para resolver uma coisa. E infelizmente não vai dar pra esperar."

    c "Você parece realmente preocupado com isso..."

    mc "Sim... Infelizmente é algo bem sério."

    c "Hmmm..."

    hide priscila with dissolve

    if priscila_amizade > 5 or priscila_seducao > 5:

        scene black with dissolve

        scene pri2_img13 with dissolve

        pause

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e2_beijinho","fim","local")

        c "Eu sei uma coisa que vai te fazer se sentir melhor."

        mc "..."

        "{i}smack{/i}"

        mc "Eu..."

        if priscila_seducao >= 7:

            c "Eu sei que você queria um beijo em outro lugar, mas hoje vai ser aqui."

        elif priscila_amizade >= 6:

            c "Quero que saiba que vou estar do seu lado, igual você está do meu."

        c "Tenho certeza que agora você vai se sentir muito melhor."

        mc "Eu..."

        c "Não se preocupe. Tudo vai ficar bem, tá?"

        c "Eu confio em você."

        c "E não precisa ficar assim. É só um beijo de boa sorte."

        mc normal "Você me pegou de surpresa."

        scene black with dissolve

        scene pri2_img1 with dissolve

        c "Era a intenção, bobinho."

    mc normal "Obrigado por tudo, [c]."

    mc "Você disse que vai sair da ilha. Você volta logo?"

    c "Não sei. Depende da minha agenda. Mas podemos conversar pelo celular qualquer coisa, né?"

    mc "Com certeza."

    c "Ok! Tenho mais uma surpresa pra você, então. Mas você vai ter que esperar."

    mc "Pode deixar."

    c "Então vou indo."

    mc "Ok. Eu também. Até a proxima."

    c "Beijo!"

    scene black with dissolve

    scene mc_ilha_polvo2 with dissolve

    mc "..."

    "Uou!"

    "Tudo isso é tão estranho pra mim. Eu nunca conversei assim com uma garota antes."

    "Eu nunca tive jeito com as mulheres. Mas parece que eu estou indo tão bem agora."

    "A gente realmente se aproximou desta vez."

    "E não foi aquela loucura do bar! Foi tipo uma conversa de dois conhecidos normais."

    "Se eu continuar assim, com certeza eu vou poder me aproximar cada vez mais dela."

    "O encontro de hoje..."

    $ resultado_encontro = "priscila"
    $ priscila_amizade_total = 16
    $ priscila_seducao_total = 13

    show screen menu_pontos
    with dissolve

    if priscila_e2 == "seducao":

        $ priscila_seducao_evento += 1

        "Foi incrível!"

        if priscila_amizade_evento > 0:

            "Nossa relação evoluiu de amizade para algo, como posso dizer, mais carnal..."

            "Consegui sair da zona da amizade e aprofundar nossa relação para o lado físico."

            "Só tenho que tomar cuidado para as coisas não ficarem confusas."
        else:


            "No primeiro encontro eu já consegui mexer com ela. E agora novamente."

            "Conseguir excitar uma garota como essa, e ainda duas vezes, é... simplesmente incrível."

            "E, mantendo esse clima, ela vai saber que não quero amizade e sim algo físico."

        "Sinto a tensão sexual crescendo."

        "Ela parece querer a mesma coisa, mas ainda não tem certeza. Ainda é muito cedo."

        "Mas se eu continuar assim logo vou poder fazer o movimento e consumar nossa relação."

        "Quero pegar ela e levar ela pra cama. O quanto antes."

    elif priscila_e2 == "amizade":

        $ priscila_amizade_evento += 1

        $ pautas += 1
        $ priscila_p2 = True

        "Foi muito especial."

        if priscila_seducao_evento > 0:

            "Nossa relação passou de uma coisa mais carnal para algo mais profundo."

            "Tenho que decidir o que quero com ela, para as coisas não ficarem confusas."
        else:


            "Nossa amizade está crescendo. Consegui ser o amigo que ela precisava novamente."

            "É a segunda vez que ela precisava de um ombro amigo e eu estava lá."

        "Estou começando a gostar cada vez mais dela. E não tenho segundas intenções."

        "Não sei se isso vai mudar no futuro, mas por enquanto quero ela como amiga."

        "Quero estar perto dela e conhecer ela."

        "O que será que ela teve que concordar para estrelar o filme?"

        "Isso me lembra das coisas que li no celular dela no bar..."

        "Espero que eu só esteja viajando, mas a forma como ela falou parecia algo realmente sério."

        "E eu ainda descobri que esse filme é do diretor [diretor]... E é o filme mais caro da história do país!"

        "Tenho certeza que posso transformar isso em uma pauta para a revista."

    elif priscila_e2 == "fracasso":

        "Não sei o que pensar deste encontro."

        "Por um lado tudo parece ter terminado bem, mas eu acho que eu poderia ter me saído melhor."

        "Se comparado com o bar, a gente não avançou quase nada..."

        "Ela me deu um presente, e disse que tem outra surpresa, mas mesmo assim, eu acho que poderia ter conseguido algo a mais..."

        mc desculpa "..."

        "Eu acho que eu vou ter um melhor resultado se eu mantiver meu objetivo bem definido com ela."

        if priscila_e1 == "amizade":

            "Eu fui um amigo para ela no bar..."

            "Eu tinha mais chance de ser um amigo desta vez também."

            "Pra isso, eu não posso avançar demais. E manter as coisas num clima amistoso."

        elif priscila_e1 == "seducao":

            "Lá no bar eu seduzi ela de uma forma que ela nunca tinha vivido antes..."

            "Eu devia continuar avançando nela novamente..."

            "Eu devia ter continuado confiante e tomado cuidado para não extrapolar."

        "Mas eu não preciso continuar sendo a mesma coisa pra ela pra sempre."

        "Se eu quiser mudar a forma como ela me vê, o melhor seria voltar no tempo e trocar minha {b}Abordagem{/b} no primeiro encontro também."

        "Mas nem sei porque tô pensando nisso! Isso é impossível!"

        mc desconfiado "Pelo menos eu espero que seja..."

    hide screen menu_pontos with Dissolve(0.5)

    "E agora? O que vou fazer?"

    "Preciso ir o mais rápido possível para a redação e descobrir o que {b}ela{/b} estava fazendo nos olhando na praça."

    mc preocupado "Com certeza não vai ser coisa boa pra mim."

    "Pelo lado bom, pelo menos ganhei um curso de massagem! Isso pode acabar sendo muito útil."

    "Eu tô vendo o endereço da massagista e fica no mesmo prédio que meu apartamento!"

    "Eu podia dar uma passada lá agora..."

    "E também não posso esquecer da [sc]. Ela deve estar no {b}templo da Cidade Chinesa{/b}."



    "O problema é que a {b}cada 5 encontros eu preciso entregar uma pauta para o chefe{/b}."





    "Sem esse emprego não vou conseguir me manter na cidade e vou perder tudo o que eu acabei de conquistar."





    mc serio "Certo! Força, [mc]! Para onde eu vou agora?"

    menu:
        "Procurar a jornalista da câmera na redação da revista":


            "Certo. O mais importante agora é descobrir o que aquela mulher da câmera quer com a [c]."

            "Tenho que ir pra lá agora."

            scene black with Dissolve(1.0)

            "..."

            scene trabalho geral with Dissolve(2.0)

            jump cassia_evento1

        "Procurar a [sc] no templo" if sayuri_evento1_check:

            "Bom... depois eu passo na {b}redação da revista{/b} para resolver esse problema."

            "Agora eu vou procurar a tal da [s]."

            scene black with Dissolve(1.0)

            "..."

            $ tempo += 1

            jump cenario_chinatown
        "Ir para o centro da ilha":


            "Vou andar por aí..."

            scene black with dissolve

            jump call_cidade



label priscila_evento3:

    "Nossa... Eu tô cansadão esses dias."

    "Vou dar um pulo lá em casa. Quem sabe tirar um cochilo."

    "..."

    if casa:

        scene ap quarto with Dissolve(1.0)
    else:


        scene apartamento cama with Dissolve(2.0)

    show mc acordando with dissolve

    "Caraca. Vou dormir muito gostoso agora."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    $ priscila_e3_check = "evento"

    hide mc with dissolve

    "Smartphone" "Trr... trr..."

    mc bravo "Que merda! Ligação bem agora..."

    mc "Só falta ser o puto do che..."

    "É a [c]! Meu Deus!"

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p3_save", extra_info="p3_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "Quanto tempo que eu não falo com ela!"

    show mc cueca_telefone with dissolve

    mc "Alô?"

    c "[mc]?"

    mc "Sou eu, [c]! Tudo bem?"

    c "Oi!"

    mc "Oi... Tudo legal?"

    if cassia_priscila_avisou:

        mc "Eu achei que você não fosse mais falar comigo depois da matéria da [j]..."

        c "Então. Minha agente disse que não era pra eu falar com você."

        c "Ela disse que você não é de confiança..."

        mc "Me desculpa, [c]. Eu juro que não tenho nada a ver com isso."

        c "Eu acredito em você, [mc]. Eu realmente acredito."

        c "Desde que a gente se viu pela primeira vez eu senti que você tem algo de especial."

        c "Só que ela diz que se a gente se falar de novo vai ser muito ruim pra minha carreira..."

        mc "..."

        c "Só que eu queria muito falar com você."

        c "Eu não sei o que eu faço..."

        mc "[c]..."

        menu:
            "Eu acho que é melhor a gente não se ver.":


                mc "..."

                mc "Eu sei que não é o que você quer ouvir. E também não é o que eu quero, mas acho melhor a gente não se falar."

                c "!"

                c "Não! Eu não quero isso, [mc]! Eu não ligo pros que os outros vão dizer!"

                mc "..."

                menu:
                    "Eu não vou te ver. É pro seu bem, [c].":


                        mc "Me desculpe, [c]. Mas eu tô fazendo isso pro seu bem."

                        mc "Vamos ficar pelo menos um tempo sem se falar..."

                        c "..."

                        c "Eu..."

                        c "{i}sob{/i}"

                        "Acho que ela tá chorando..."

                        mc "Eu gosto muito de você. E vai ser difícil pra mim também."

                        c "Tá..."

                        c "Adeus, [mc]..."

                        c "Me desculpa..."

                        mc "Não é um ad..."

                        "Smartphone" "Tu tu tu..."

                        mc "Ela desligou..."

                        hide mc with dissolve

                        "Eu fiz o que tinha que fazer. Eu não posso deixar ela acabar com a carreira dela por minha causa."

                        "Eu trouxe essa situação pra vida dela. Eu não aceitei levar o acordo da [j] até o fim."

                        "E agora eu tenho que corrigir isso. Não posso deixar que ela se prejudique pelas minhas decisões."

                        "Não vai ser fácil perder ela... Mas vai ser o melhor pra nós dois..."

                        $ priscila_e3 = "fim"

                        jump call_cidade
                    "Você tem certeza que é isso que você quer?":


                        mc "Você tem certeza, [c]? A última coisa que eu quero é te prejudicar."
            "Não podemos deixar a opinião dos outros decidir nossa vida.":


                mc "Eu acho que a gente não pode deixar que a opinião desse povo atrapalhe o que a gente quer fazer."

                c "Eu concordo... Minha carreira é importante, mas não quero esquecer você."

                mc "Essa é uma escolha difícil. Você tem certeza?"
            "Eu quero te ver, não importa as consequências.":


                mc "Eu sei que essa situação não é fácil pra você. Mas eu quero tanto ver você."

                c "Eu também!"

                mc "Você tem certeza disso?"

        $ priscila_cassia_ignorou = True

        c "Eu tenho, [mc]! Eu quero falar com você! Quero te ver! Não me importo com os outros."

        mc "Mas e sua carreira?"

        c "Não é uma matéria que vai acabar com a minha carreira. Você tá achando que eu sou uma ninguém?"

        mc "Não é isso..."

        c "Eu me decidi. Só o pensamento de não te ver de novo já me deixa muito nervosa."

        mc "Tudo bem... Não quero fazer pouco do seu trabalho."

        c "..."

        c "Tudo bem... Eu tô me sentindo muito melhor depois dessa conversa."

        mc "Verdade?"

        c "Sim! Eu tô quase rindo aqui."

        mc "Eu também tô muito feliz. Tô feliz de saber que essa matéria não ferrou tudo entre a gente."

        c "É verdade. Eu tava com muito medo disso."

        c "Mas agora passou. Como se tivessem tirado um peso "

        mc "Mas acho que a gente tomou a decisão certa. Não sei o que vai aceontecer, mas eu quero ver isso junto com você."

        c "..."

        mc "Tudo legal?"

    c "Sim. Desculpa. É que eu tô um pouco nervosa."

    c "Parece que hoje em dia não é mais normal ligar pras pessoas."

    menu:
        "É verdade. Hoje em dia é tudo zap do zap.":


            mc "Hoje em dia a galera só quer saber de zap, né?"

            c "Sim... Não tô te atrapalhando, tô?"

            mc "Claro que não. Pare de pensar besteira."
        "Eu adoro ouvir sua voz.":


            $ priscila_seducao += 1

            mc "Você sabe que eu adoro falar com você. Ouvir sua voz."

            c "Ai, [mc]... Não me deixa mais nervosa..."

            mc "Não precisa ficar nervosa comigo."

            c "Eu sei. É que eu sou boba. Desculpa."
        "Você sabe que não precisa ter isso comigo.":


            $ priscila_amizade += 1

            mc "Tsc! Você sabe que não precisa se preocupar com isso, né?"

            mc "Pode sempre contar comigo."

            c "Eu sei. Eu que fico pensando besteira."

            c "É que... sabe... acho que eu nunca tive alguém assim."

            mc "Assim como?"

    c "Sei lá. É que eu nunca tive alguém que eu me preocupasse tanto com o que acha de mim."

    mc "Eu fico feliz de saber que você me considera assim. Eu também sinto o mesmo."

    c "..."

    c "Agora eu fiquei vermelha..."

    mc "[c]... para de ser boba."

    mc "Tô falando sério. Fiquei feliz de você ter ligado."

    c "Olha aí! Acabei até esquecendo porque eu liguei."

    c "Ah! Eu ía te escrever, mas fiquei tão feliz que resolvi te ligar."

    c "É que eu tô indo pra capital! Vou ficar hospedada na ilha!"

    mc "Que bacana!"

    c "Sim!"

    c "Vo-você gostaria de fazer alguma coisa comigo amanhã?"

    menu:
        "Claro. Onde você quer ir?":


            $ priscila_amizade += 1

            mc "Com certeza. Eu adoraria."

            c "Que bom!"

            c "Você não ia recusar a companhia de uma celebridade, né?"

            mc "A rainha dos adolescentes? Claro que não."

            c "{i}Rsrs{/i}"

            c "Eu gosto de conversar com você, [mc]. Sei lá. Eu só me sinto bem."

            mc "Você é uma excelente companhia. Eu também adoro falar contigo."
        "Tá louquinha pra me ver?":


            mc "Parece que você tá doidinha pra me ver. Acertei?"

            c "Ah! Eu... eu..."

            mc "Ficou sem palavras?"

            c "Eu não sei..."

            mc "Não sabe?"

            c "Não me força, por favor. Eu... fico muito nervosa."

            mc "Ok..."
        "Só se você deixar eu cuidar de tudo.":


            $ priscila_seducao += 1

            mc "Só se você deixar eu cuidar de tudo."

            mc "Você aceita sair em um encontro comigo?"

            c "Claro! Eu esperei muitos dias pra te ver de novo."

            c "Quer dizer! Droga... Fiquei parecendo uma grudenta?"

            mc "Eu acho você linda quando fica com vergonha."

            c "..."

            c "Não me deixa sem jeito."

    if priscila_e1 == "seducao" or priscila_e2 == "seducao":

        c "Sabe, antes de te ligar hoje..."

    if priscila_e1 == "seducao":

        c "Eu lembrei do bar..."

    if priscila_e2 == "seducao":

        c "Lembrei da praça..."

    if priscila_e1 == "seducao" or priscila_e2 == "seducao":

        c "De como você foi romântico e sexy..."

        c "Eu fico sem ar... só de lembrar..."

        mc "Você também mexeu muito comigo."

        mc "Quando eu lembro dessas coisas eu tenho muita vontade de te ver."

        mc "Eu quero mais daquilo, [c]. E quero ir além."

        c "..."

        c "Eu fico muito nervosa, [mc]..."

        mc "Deixa que eu vou cuidar de você."

        c "Tá..."

        "..."

    c "Mas.. então assim que eu estiver aí eu te aviso, tá?"

    mc "Claro. Me liga e daí a gente sai."

    c "Combinado. Beijos."

    mc "Beijo."

    hide mc with dissolve

    "..."

    "Nem acredito que a [c] vai voltar pra ilha amanhã."

    "Ela foi a primeira garota que deu bola pra mim."

    mc zerado "Acho que na minha vida toda..."

    "Preciso pensar em algo bem legal pra gente fazer amanhã."

    "Lembrando dos meus primeiros encontros com ela..."

    if priscila_e1 == "seducao":

        "No bar eu seduzi ela completamente. Ela ficou realmente excitada e no fim eu tenho quase certeza que ela teve um orgasmo."
    else:


        "No bar eu fui o grande amigo que ela precisava. Ela tava extremamente fragilizada e eu ajudei ela a se recompor."

    if priscila_e2 == "seducao":

        "No segundo encontro, no parque, eu seduzi ela e a gente quase se beijou."

        "Se não fosse aquela pirralha..."

    elif priscila_e2 == "amizade":

        "No segundo encontro, no parque, eu disse pra ela que queria ser um amigo que ela pudesse contar."

        "E assim eu consegui conquistar a confiança dela. Ela até revelou sobre o filme..."
    else:


        "Logo no dia seguinte, na praça, eu senti que nosso encontro não foi dos melhores..."

        "Isso com certeza não é um bom sinal."

        "Se eu quiser ter uma relação duradoura com ela, eu preciso aliar sedução com amizade."

    if priscila_seducao_evento >= 2:

        "Eu seduzi ela nos dois encontros... Eu nunca tive uma chance de realmente conversar com ela algo profundo."

        "Será que uma relação só física é tudo o que eu quero com ela?"

        "Será que é isso que ela tá buscando?"

        "Talvez agora seja hora de mudar o rumo e conhecer ela por outro lado."

        mc tarado "Falar é fácil. Quero ver eu negar aquela delícia de mulher."

    if priscila_amizade_evento >= 2:

        "Eu fui um grande amigo nos dois primeiros encontros que a gente teve."

        "Ela é uma excelente amiga e talvez eu queira que as coisas continuem assim."

        "Mas se eu quiser ir além. Não sei... talvez até namorar com ela..."

        "Eu vou precisar que ela me veja com outros olhos. Preciso que ela me veja como um homem."

        "No nosso próximo encontro eu preciso ser charmoso e sexy."

    "Eu tenho a impressão que os próximos dias vão ser determinantes pra minha relação com ela."

    "Tô sentindo um tipo de calafrio. Como se tivesse alguém muito ansioso com tudo isso além de mim."

    "Que loucura..."

    "Certo. Amanhã ela chega. O que eu vou fazer até amanhã?"

    mc tarado "Pensando bem, eu posso só dormir o resto do dia inteiro..."

    "Essa é uma excelente ideia. Vou estar cheio de energia pra sair com a [c] amanhã."

    show mc acordando with dissolve

    "Finalmente a hora chegou..."

    "Cama... não existe mais nada entre nós."

    "Agora eu..."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    hide mc with dissolve

    "Smartphone" "Trr... trr..."

    mc "..."

    mc "Será que ela esqueceu de falar alguma coisa?"

    show mc cueca_telefone with dissolve

    mc "[c]?"

    "Voz desfigurada" "Para de falar com ela agora."

    mc "Quê? Alô?"

    "Voz desfigurada" "Eu sei de você. Eu não quero mais saber de você perto dela."

    "Voz desfigurada" "Você me entendeu?"

    "Número desconhecido..."

    mc "Quem tá falando?!"

    "Voz desfigurada" "Você entendeu, [mc]? Não quero mais você perto da [c]."

    "Smartphone" "Tu tu tu..."

    hide mc with dissolve

    mc bravo "Caralho! Que susto!"

    "Mas que porra foi essa?!"

    "Que voz estranha... Pareceu... uma ameaça."

    if cassia_priscila_avisou:

        "Será que foi alguém que leu a matéria que saiu da gente?"

        "Será que eu devia ter dado mais atenção às ameaças da [j]?"

    "Meu coração tá muito acelerado."

    "Que porra..."

    menu:
        "Deve ter sido só um trote.":


            "Deve ter sido apenas trote de algum fã da [c] que viu a gente juntos."

            "Não tenho porque me preocupar com isso ainda."
        "Será que era um fã da [c]?":


            "Será que era algum fã tipo obsessivo? A pessoa parecia realmente incomodada."

            "Não deve ser nada muito sério. Andar com celebridades tem seu preço."
        "Isso parece algo muito sério.":


            "Sei lá. Tô assustado, mano. Parece ser algo muito sério."

            "Essa voz modificada. Não é qualquer um que consegue modalizar a voz desse jeito."

    "Não tenho certeza do que pensar. Preciso ficar ligado. Só tomara que não aconteça de novo."

    "A última coisa que eu quero é que aconteça alguma coisa comigo no melhor momento da minha vida."

    "..."

    "O sono bateu."

    scene black with Dissolve(2.0)

    "..."

    $ tempo = 3

    "..."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    $ priscila_cel_msg4 = True

    "..."

    if casa:

        scene ap quarto with Dissolve(1.0)
    else:


        scene apartamento cama with Dissolve(2.0)

    "Tocando de novo."

    "..."

    if not casa:

        scene apartamento cama_celular with dissolve

    "É uma mensagem da [c]. Ufa..."

    show screen celular_priscila

    "..."

    "Caraca, isso é um avião ou uma piscina?"

    "Gente rica é outra coisa."

    if priscila_seducao_evento > 0:

        "Essa mina é muito linda..."

        "Como eu quero pegar ela logo."

    "Deixa eu responder..."

    menu:
        "Quero que você chegue logo!":


            $ priscila_cel_msg4_r = "amizade"
            $ priscila_amizade += 1

            "Tô muito ansioso pra ver ela."
        "Consigo ver quase seu peito inteiro.":


            $ priscila_cel_msg4_r = "cuzao"

            "Essa roupa tá me deixando duro."
        "Você mexe muito comigo.":


            $ priscila_cel_msg4_r = "seducao"
            $ priscila_seducao += 1

            "Essa mina mexe comigo demais, meu Deus!"

    "Pronto."

    "..."

    "Ela visualizou..."

    show screen celular_priscila

    "..."

    "Tudo tá tão legal entre a gente. Aquela ligação parece só um sonho agora."

    "..."

    "Não adianta eu ficar pensando muito nisso. Deixa eu dormir mais um pouco."

    "Eita. Já são onze da noite. Eu vou é dormir até amanhã."





    scene black with Dissolve(2.0)

    "..."

    scene fadolandia geral with Dissolve(2.0)

    "Esse lugar? Fazia tempo que eu não vinha aqui..."

    show pixie bonitinha with dissolve

    p "Olázinho."

    mc surpreso "[p]!"

    p "Eu mesma. Tudo bem?"

    mc serio "Não sei... Você que tem que me falar."

    mc serio "Foi você quem disse que não ia mais me chamar aqui."

    show pixie desconfiada with dissolve

    p "Eu sei, [mc]. Mas eu tive que te trazer."

    mc desconfiado "?"

    p "Eu tô me sentindo culpada."

    mc "Culpada pelo quê?"

    p "Calma, eu vou te explicar tudo. Bom, não tudo, mas o necessário."

    mc zerado "Você e seus enigmas..."

    show pixie explanando with dissolve

    p "É tudo muito simples. Eu disse algo pra você, mas eu estava errada."

    mc serio "..."

    p "Eu queria que você fosse com tudo pra cima daquela garota [c]."

    if priscila_e1 == "seducao":

        p "Até te elogiei quando você pegou ela de jeito no bar."

        p "E na época era realmente o que eu queria."

    p "Mas agora eu não quero mais."

    mc desconfiado "Não quer mais? Se converteu a Jesus?"

    p "Nada disso. Eu não tenho nada com o Deus do seu mundo e nem o filho dele."

    p "Minha questão é prática. Eu acho que você devia deixar essa [c] e perseguir outras mulheres."

    p "Mulher é o que não falta no mundo."

    mc zerado "Não tô acreditando no que eu tô ouvindo."

    p "Eu não vou tentar te convencer. Não tenho paciência pra isso."

    p "Estou falando como alguém que depende de você pra sentir... sentir coisas."

    p "Eu quero você firme e forte. E se você insistir com essa menina, talvez sua história termine antes do esperado."

    p "Literalmente."

    mc preocupado "Você está me deixando preocupado."

    p "Lembra que eu disse que suas ações iriam realmente alterar seu futuro?"

    p "Nessa altura do campeonato você já percebeu isso. Ou você é mais burro do que o esperado."

    p "Se você escolher insistir com a [c], pode ser que você chegue ao fim da sua história."

    p "E você será o único culpado."

    mc "..."

    menu:
        "Eu quero continuar vendo a [c].":


            $ priscila_amizade += 1

            mc serio "Eu agradeço sua preocupação, mas vou continuar vendo a [c] independente disso."

            mc "Se você estiver certa e algo acontecer comigo, a gente se fodeu."

            show pixie desconfiada with dissolve

            p "Você tem certeza?"

            mc "Sim."

            p "Ok. Então vou te dar uma dica."
        "Ok. Vou seguir sua orientação e esquecer ela.":


            mc preocupado "Você parece saber do que tá falando."

            mc "Acho que vou seguir seu conselho e esquecer ela."

            p "Ufa. Fico mais tranquila. Isso é realmente sério, [mc]. Entendeu?"

            p "Quando acordar, espero que você cumpra isso."

            mc "Vou tentar."

            p "Mas, se caso você mudar de opinião, vou te falar algo importante."
        "Eu não posso decidir isso agora.":


            mc desculpa "Eu entendo, mas eu tô desenvolvendo sentimentos por ela."

            mc "Não sei o que fazer agora."

            show pixie desconfiada with dissolve

            p "Escute sua fada particular. Você acha que todo mundo tem essa chance? De ter uma conselheira?"

            mc envergonhado "Eu sei, mas não consigo prometer isso pra você agora."

            p "Você é foda, [mc]."

            p "Mas se você realmente decidir continuar com isso, eu vou te falar uma coisa."

    if priscila_amizade_evento == 0:

        p "Você não conseguiu conquistar a amizade dela em nenhum dos dois primeiros encontros."

        p "Como você espera que ela abra o coração pra você se a única coisa que você quer abrir é as pernas dela?"

        p "Acorda, [mc]! Se você não tiver as informações que você precisa, você vai comer laranja no próximo café da manhã."

        p "Você só tem mais uma chance. Se ela não puder confiar em você após o próximo encontro, tá acabado."
    else:


        p "Você conseguiu mostrar pra ela que você é um amigo pelo menos uma vez."

        p "Ela vai poder se abrir com você e vai te explicar coisas que você precisa saber para não acabar na vala."

        p "Preste atenção no que você vai fazer nos próximos dias!"

        if priscila_seducao_evento == 0:

            p "Só que você não seduziu ela nenhuma vez também."

            p "Se você quiser só ser amiguinho tudo bem, mas se você tem alguma pretensão a mais, é sua última chance."

            p "Se você não seduzir ela dessa vez, vai cair na friendzone pra sempre."

    p "Acorda, [mc]!"

    mc incomodado "Calma... Entendi o que você tá querendo dizer..."

    p "Estou falando literalmente. Acorda!"

    $ tempo = 1
    $ dia += 1

    scene black with Dissolve(1.0)

    "..."

    if casa:

        scene ap quarto with Dissolve(1.0)
    else:


        scene apartamento cama with Dissolve(1.0)

    "..."

    show mc acordando with dissolve

    "Tá doido. Dormi pra caramba."

    "Mas por algum motivo meu ouvido tá doendo..."



    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with dissolve

    "A [c] já deve estar na ilha essa hora."

    "Eu acabei nem pensando no que eu quero fazer com ela."

    "A [c] é uma garota muito especial. Não posso pensar pequeno se eu quiser impressionar ela."

    "Nessas horas que eu odeio ser pobre..."

    "O que adianta ganhar uma graninha boa no trabalho se quase tudo vai pra pagar aluguel e as contas?"

    "Talvez fosse hora de eu começar a fazer algumas coisas ilegais pra ganhar aquela grana bacana."

    "..."

    "Isso provavelmente traria mais dificuldades do que soluções."

    "Enfim... Não posso perder tempo. Ela deve me ligar a qualquer hora."

    "Eu acho que o mais legal seria se eu resolvesse tudo sozinho e só surpreendesse ela."

    "Ou será que seria melhor perguntar a opinião dela?"

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trr... trrr..."

    "Opa! Deve ser ela! Depois eu resolvo o que fazer."

    show mc cueca_telefone with dissolve

    mc "Alô?"

    "..."

    "Voz no fundo" "{size=15}Como foi a viagem?{/size}"

    "Voz feminina" "{size=15}Tudo bem...{/size}"

    "Voz masculina" "{size=15}Eu fico feliz que a primeira coisa que você fez tenha sido vir me ver.{/size}"

    "..."

    "Voz masculina" "{size=15}O que foi? Não está feliz em me ver?{/size}"

    "O que é isso? Parece que são duas pessoas conversando no fundo."

    menu:
        "Continuar ouvindo":


            $ priscila_e3_ouviu = True

            "Voz feminina" "{size=15}Eu...{/size}"

            "Voz masculina" "{size=15}Diga.{/size}"

            "Voz feminina" "{size=15}Eu tô.{/size}"

            "Voz masculina" "{size=15}Eu queria muito ver você. Sentir você.{/size}"

            "..."

            "Voz masculina" "{size=15}Você não queria me sentir também?{/size}"

            "..."

            "Voz masculina" "{size=15}RESPONDA, MULHER!{/size}"

            "Voz feminina" "{size=15}Si-sim...{/size}"

            "Voz masculina" "{size=15}Assim é melhor.{/size}"

            "Voz masculina" "{size=15}Agora vem aqui que o papai tava com saudades...{/size}"

            "..."

            "{i}TCHAK{/i}"

            "Smartphone" "Tu... tu... tu..."
        "Desligar o telefone":


            hide mc with dissolve

            "Eu não quero ouvir essa merda!"

            "..."

            "Eu tô tremendo..."

    hide mc with dissolve

    "Que porra foi essa?"

    "Parece a ligação de ontem. Por que essas coisas esquisitas estão acontecendo?"

    "Essas vozes. Eu tenho a impressão que eu conheço elas. Principalmente a da mulher."

    "Mas eu ouvi muito pouco. Impossível ter certeza."

    "Alguém tá querendo ferrar com a minha cabeça. E o pior é que tá conseguindo."

    "..."

    mc serio "Não!"

    mc "Não posso deixar uma coisa dessas estragar meus planos com a [c]."

    "Eu vou fazer algo muito especial hoje."

    "Só que eu tô ficando assustado. E se a ligação de ontem for séria?"

    "Por que alguém não quer que eu veja ela?"

    "..."

    "Acho que eu preciso de um banho."

    scene black with Dissolve(1.0)

    "{b}Alguns minutos depois{/b}"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    mc normal "Hmmm..."

    "Tô me sentindo melhor."

    "Se eu ficar assustado daí que eu não vou me dar bem com a [c] mesmo. Tenho que agir como se tudo tivesse normal."

    "No fundo pode ser só um trote mesmo. Algum fã querendo me ferrar."

    "O que eu podia fazer com ela hoje?"

    "O dia tá bem bonito. Talvez..."

    "Talvez eu pudesse levar ela na praia!"

    "Eu nunca fui lá, mesmo sendo tão perto. Talvez ela não tenha ido também. Ela nem mora aqui."

    "Eu sei que tem um restaurante muito bacana lá. Uma parte dele fica sobre a água."

    "Deixa eu dar uma pesquisada."

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento cama_celular with dissolve

    "O nome é Chez Robinson. Preciso ver os preços..."

    "Eles nem colocam aqui... Deve custar os olhos da cara."

    "Não importa. Vale a pena. Depois de um jantar ao por do sol na praia ela nunca vai se esquecer de mim."

    mc "Pelo menos é o que eu espero."

    "Bom, melhor já reservar."

    "..."

    scene black with Dissolve(1.0)

    "{b}Alguns minutos depois{/b}"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    mc normal "Reservado."

    mc preocupado "R$ 200 por pessoa... Lá se vai o salário do mês."

    "Ok. Agora é só esperar ela me ligar. Achei que ela já teria me ligado essa hora."

    mc normal "Deixa eu ver o que tem na Netflix..."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    "..."

    "Tá difícil começar uma série. Não tenho vontade de ver nada. Vou assistir essa aqui da drag queen..."

    "{b}Uma hora depois{/b}"

    "Ai, cara... Sashay Away... Esse povo é engraçado."

    "Será que a [c] esqueceu de mim? Será que eu devo mandar uma mensagem pra ela?"

    menu:
        "Escrever uma mensagem.":


            "Será que eu não vou parecer grudento demais?"

            "Não vou ficar pensando nisso. Só vou mandar logo."

            "O que eu escrevo?"

            menu:
                "Bom dia, [c]! Chegou bem de viagem?":


                    $ priscila_seducao += 1
                    $ priscila_amizade += 1
                    $ priscila_cel_msg4_rA = "deboa"

                    "..."

                    "Pronto."

                    "Pra não parecer muito desesperado."
                "Cadê você??????":


                    $ priscila_amizade += 2
                    $ priscila_cel_msg4_rA = "desesperado"

                    "Ela ficou de me avisar assim que chegasse. Por que não me escreveu ainda?"

                    "E se ela tá com algum problema?"

                    "..."

                    "Pronto."
        "Continuar esperando.":


            $ priscila_seducao += 1


            "Não vou ser grudento. Ela deve tá fazendo as coisas dela."

    "Vamos continuar vendo as drags aqui..."

    "{b}Mais uma hora depois{/b}"

    "Hmmm..."

    "Caraca, cadê ela?"

    if not priscila_cel_msg4_rA == "nada":

        show screen celular_priscila

        "..."

        "Ela ainda não respondeu a mensagem. Ela nem visualizou."

    "Talvez ela esteja dormindo até tarde. Ainda não é nem meio-dia."

    "Vou fazer mais uma horinha e se ela não ligar tenho que ver o que...."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trrr... trrr..."

    "Caralho... Espero que não seja merda de novo."

    "Graças a Deus! É a [c]. Que bom!"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    show mc telefone with dissolve

    mc "Oi, [c]! Tudo bem?"

    c "O-oi..."

    menu:
        "Você demorou...":


            mc "Você demorou..."

            c "Verdade..."
        "Sonhei com você hoje.":


            $ priscila_seducao += 1

            mc "Dormi muito bem. Sonhei com você."

            mc "Eu sonhei que a gente passava um dia incrível e tinha um jantar romântico na praia."

            c "Sério? Seria um dia perfeito..."

            mc "Sim. E você? Dormiu bem?"

            c "Acho que sim..."
        "Tá tudo legal com você?":


            $ priscila_amizade += 1

            mc "Você tá legal? Achei que fosse ligar mais cedo."

            c "Eu tô mais ou menos..."

            c "Não acordei tão bem. Tô meio com dor de cabeça..."

            c "Mas, então..."

    c "Eu queria ter te ligado mais cedo, mas tive que resolver um negócio hoje de manhã."

    mc "Não tem problema. Eu só tava ansioso pra ver você."

    c "Eu também. Só de falar com você eu fico mais alegre. Obrigada."

    menu:
        "Tá agradecendo por quê?":


            mc "Por que tá me agradecendo?"

            c "Não sei... Eu só quis."

            mc "Você sabe que não precisa."

            c "Ok..."
        "Pode sempre contar comigo.":


            $ priscila_amizade += 1

            mc "Você pode sempre contar comigo, tá?"

            mc "Eu quero que você fique bem."

            c "Obrigada, [mc]. Eu sinto que posso confiar em você."

            mc "E você pode."
        "Eu vou proteger você de tudo, [c].":


            $ priscila_seducao += 1

            mc "Eu quero proteger você. Quero que nada de ruim aconteça com você."

            mc "E não precisa me agradecer. Eu faço isso porque eu quero."

            c "Tá... Eu confio em você."

    c "É que tem tanta coisa acontecendo comigo."

    if priscila_amizade_evento > 0:

        c "Eu pude realmente confiar em você aquele dia. Você me ouviu e foi muito muito importante pra mim."

        c "Mas eu não quero estragar nossa relação com isso."

        mc "Você nunca vai estragar nada. Seus problemas são importantes pra mim também. Porque eu me importo com você."

        c "..."

        c "Obrigada, de verdade. Eu quero acreditar nisso."

        mc "Vamos deixar isso pra depois, tá? Quando a gente se ver você me conta mais."

        c "Co-combinado."

        mc "Vai dar pra gente sair hoje, né?"
    else:


        c "Mas não quero estragar nosso lance com isso."

        mc "Você pode confiar em mim. Você sabe o quanto eu quero você."

        c "Eu sei. E eu gosto da nossa relação assim. Você faz eu ficar sem ar..."

        mc "Você sabe o quanto você mexe comigo também. Você sabe o que eu quero."

        c "Eu sei. E eu também quero. Você sabe, né?"

        mc "Vamos só viver isso então."

        c "É o que eu mais preciso agora."

        mc "..."

        mc "Então vai dar pra gente sair hoje?"

    c "Sim! Agora eu tô com o dia livre."

    mc "Que bom! Porque eu tenho planos pra gente."

    c "Sério?"

    mc "Sim. Mas não vou falar ainda. Você já tá pronta pra sair?"

    c "Eu tô chegando agora no hotel. Vou tomar um banho e daí já tô pronta."

    mc "Legal."

    c "Onde a gente se encontra?"

    mc "O que você acha de eu passar aí te pegar no hotel? É perto daqui."

    c "Seria incrível!"

    mc "Então tá combinado. Saio daqui em uns 30 minutos. Fica bom pra você?"

    c "Combinado! Até daqui a pouquinho!"

    mc "Até!"

    hide mc with dissolve

    "Parece que ela tá legal."

    "Falando com ela eu até esqueço das coisas estranhas que aconteceram. A [c] é realmente uma garota especial."

    "Preciso fazer tudo certo hoje."

    "Tá legal. O que eu faço agora?"

    menu:
        "Ver um pouco de TV.":


            if casa:

                scene ap mc_assistindo with Dissolve(1.0)
            else:


                scene apartamento tv with Dissolve(1.0)

            "Ainda tenho tempo."

            "Vou ver mais um pouco das drags aqui."

            "..."

            "Agora deu. Bora se trocar e sair."

            "..."

            scene ilha parque with Dissolve(1.0)

            "O hotel fica logo passando a praça."

            "..."

            "Cheguei."
        "Tomar outro banho.":


            "Eu acabei de tomar banho, mas ficar cheiroso nunca é demais."

            scene black with Dissolve(1.0)

            "Lava lava laaava... uma orelha, outra orelha..."

            "..."

            mc "Ok. Estou pronto."

            "..."

            scene ilha parque with Dissolve(1.0)

            "O hotel fica logo passando a praça."

            "..."

            "Cheguei."
        "Se trocar e chegar mais cedo.":


            $ marco_conheceu = True

            "Não quero correr nenhum risco."

            "Vou só me trocar e sair rapidinho. Eu acabei de tomar banho mesmo."

            "..."

            "Tô pronto. Vamos lá."

            scene ilha parque with Dissolve(1.0)

            "..."

            "Hoje o dia tá massa pra ir na praia. Espero que continue..."

            "Homem" "Bom dia, jovem."

            mc surpreso "Ou!"

            show pri3_img1 with dissolve

            pause

            "Homem" "Perdão. Não queria te assustar."

            mc desculpa "Tudo bem. Acho que eu tô um pouco assustado."

            "Homem" "Você tá indo pro hotel?"

            mc serio "Sim. Por que?"

            "Homem" "Nada. Só queria puxar assunto."

            mc "Ah tá. E você o que tá fazendo aqui?"

            "Homem" "Só fazendo hora."

            mc "Ok..."

            mc normal "Valeu."

            "Homem" "Falou."

            hide pri3_img1 with dissolve

            "Que foi isso?"

            "Bom. Acho que eu vou esperar lá na recepção. Se eu ficar no sol vou chegar parecendo que corri a maratona."

    "..."





    scene black with dissolve

    scene hotel recepcao with Dissolve(2.0)

    "Uou. Que diferença pra entrada do meu prédio."

    "Ela deve tá chegando logo. Tô muito ansioso pra ver ela..."

    "{b}Alguns minutos depois{/b}"

    c "Oi!"

    mc normal "Oi!"

    scene pri3_img2 with dissolve

    pause

    c "Nem acredito que você realmente veio aqui me esperar."

    mc normal "Claro."

    menu:
        "Sou um cavalheiro.":


            $ priscila_amizade += 1

            mc charmoso "Sou um cavalheiro. E os cavalheiros esperam as damas."

            c "Muito agradecida, Sir [mc]."

            mc normal "Ao seu dispor, senhorita."
        "Eu tava tranquilo hoje.":


            mc normal "Relaxa. Eu tava tranquilo hoje."

            c "Que bom. Então deu certo da gente se encontrar."

            mc "Sim."
        "E deixar essa gata sozinha?":


            $ priscila_seducao += 1

            mc charmoso "E deixar uma gata dessas esperando? Só se eu fosse muito idiota mesmo."

            c "Gata?"

            c "..."

            c "Você tá falando dessa garta aqui?"

            mc safado "Exatamente..."

            c "Às vezes eu acho que eu devia ter mais cuidado com você."

            mc "Talvez..."

    c "Nossa. Você não sabe como eu tô cansada..."

    scene pri3_img3 with dissolve

    c "Eu cheguei mó tarde ontem e hoje ainda tive que acordar cedo pra... pra resolver uns negócios."

    c "Minha agenda tá tão lotada... Várias fotos e eventos. Você não sabe..."

    mc surpreso "!"

    "Essa roupa é realmente decotada, mas se eu ficar olhando muito pode dar bandeira..."

    menu:
        "Focar no decote":


            "Não consigo não dar uma olhadinha..."

            scene pri3_img4 with dissolve

            pause

            "Caraca..."

            c "Ei!"

            if priscila_seducao_evento > 0:

                $ priscila_seducao += 1



                c "Você tava olhando pros meus peitos, não tava?"

                mc envergonhado "E-eu..."

                c "Não consegue negar, né?"

                c "Quer que eu abaixe assim pra você ver melhor, taradão?"

                mc "Vou tentar me controlar..."

                scene pri3_img3 with dissolve

                c "Acho bom, porque se continuar me secando assim eu vou sumir logo logo."

                mc "..."

                "Mesmo passando vergonha, acho que a reação dela foi melhor do que eu imaginava."

                "Depois de ter seduzido ela no outro dia, acho que ela deve estar mais aberta a coisas sacanas comigo."

                "Isso é um excelente sinal."
            else:


                scene pri3_img5 with dissolve

                c "Eu vi você com o olhão no meu decote."

                mc desculpa "Ops. Perdão."

                c "Eu me sinto segura do seu lado, [mc]. Se você ficar com esse olhão aí..."

                mc "..."

                c "Mas eu sei que mesmo sendo meu amigo você não deixa de ser homem, né?"

                c "É que eu não consigo te ver assim..."

                mc normal "Relaxa. Mas que bom que você entende que eu não consigo me controlar sempre."

                c "Tá tudo bem... Não queria ficar tão brava."

                "A gente nunca partiu pro lado da sedução nos encontros anteriores."

                "Por isso é dificil pra ela aceitar que eu sou homem também."

                "Se eu quiser que ela me veja assim, preciso ser mais direto nos meus sentimentos e conquistar ela assim."
        "Manter o contato visual":


            $ priscila_amizade += 1

            "Não quero que ela ache que eu sou um tarado."

            mc preocupado "Você tá correndo demais. Tem certeza que isso é bom pra sua saúde?"

            c "Pior é que não sei, viu. Eu vivo tão cansada."

            c "Não é que eu não goste da minha rotina. Mas é que é meio puxado."

            mc normal "Que bom que você arranjou um tempinho pra gente se ver."

            c "Eu tô enchendo minha agente faz dias pra gente vir pra cá."

            c "Daí acabou casando com um outro compromisso aqui na capital e eu consegui vir."

            mc "Que bom."

    scene pri3_img6 with dissolve

    pause

    c "Mas não se preocupe que eu tô cheia de energia pro nosso encontro!"

    c "Pode mandar que eu aceito qualquer coisa."

    mc normal "Que bom. Porque você vai precisar de energia mesmo."

    mc "Tá pronta pra sair?"

    c "Vamos."

    mc "Pode seguir o mestre."

    c "Sim, senhor!"

    mc "Vamos passar pelo parque e seguir por alí."

    c "Que sensação legal sair e nem saber pra onde tô indo. Dá um frio na barriga."

    scene black with dissolve

    scene ilha parque with Dissolve(1.0)

    if marco_conheceu:

        mc "Que bom que você con..."

        show pri3_img1 with dissolve

        "Aquele cara tá lá até agora."

        c "[mc]?"

        mc normal "Ah."

        hide pri3_img1 with dissolve

        c "Você tava dizendo uma coisa."

        mc "Eu disse que é bom que você confia em mim."
    else:


        mc normal "Que bom que você confia em mim."

    scene black with dissolve

    scene pri3_img7 with dissolve

    pause

    c "Você foi muito bacana comigo das outras vezes. Não tenho porque duvidar."

    mc "Certo. Agora a gente vai andar uns 15 minutos pra lá."

    c "Ok. Sabia que eu nem sei o que tem pra lá?"

    mc "Não?"

    c "Normalmente eu fico só bem no centro da ilha, né? Vou no bar, brigar com seu chefe {i}rsrs{/i}..."

    mc "Verdade."

    scene pri3_img8 with dissolve

    c "Não era bem do jeito que eu queria que você tivesse me conhecido..."

    mc "Que nada."

    menu:
        "Você foi a primeira garota que me chamou de gato.":


            $ priscila_amizade += 1

            mc envergonhado "Sinceridade. Você foi a primeira garota que me deu bola daquele jeito na minha vida."

            c "Mentira."

            mc "Tô falando sério."

            c "Mas, com todo o respeito, tá, eu te acho mó bonito."

            mc "Haha! Sei lá. Nunca ninguém tinha falado isso pra mim."

            "Pensando bem... Realmente nunca tinham me achado bonito..."

            "Mas agora parece que várias mulheres estão reparando em mim."

            "Como se de um dia pro outro tivesse acontecido alguma coisa mágica."

            "Que loucura..."
        "Ali eu vi que você era uma garota especial.":


            $ priscila_seducao += 1

            mc charmoso "Ver você brigando com o chefe foi incrível."

            mc "Eu soube ali que você era uma garota especial."

            c "Não achou que eu fosse uma louca?"

            mc "Claro que não. Você tava lutando pelo seu direito."

            mc "Não sou daqueles caras que acha que mulher tem que ficar quieta e cuidar da casa."

            mc "Eu acho incrível mulheres que lutam e brigam pelo que acham certo."

            c "..."

            c "Você também é especial, [mc]. Você às vezes fala cada coisa incrível."

            mc normal "Que nada. Só tô sendo sincero."

    mc normal "Vamos então que temos um caminho aí."

    c "Bora, chefe!"

    scene black with dissolve

    "..."

    "Ufa... Era mais longe do que eu tinha calculado. Mas agora tamo chegando."

    play sound "audio/som_12_gaivota.mp3"

    scene pri3_img9 with dissolve

    pause

    c "Uou! Pera! A gente tá indo na praia?!"

    mc normal "Isso mesmo."

    c "Aiii! Que legal!"

    c "Eu nem sabia que dava pra vir passear aqui!"

    mc "Ela não é tão usada. Mas é turística como tudo aqui na ilha. Coisa fina."

    c "A vista daqui já é linda, [mc]! Imagina quando a gente chegar mais perto."

    mc feliz "Que bom que você ficou animada."

    mc envergonhado "Fiquei preocupado de você achar simples demais."

    c "Não seja bobo."

    c "Você sabe que eu fico feliz de andar com você. Mesmo que a gente fosse no lixão."

    c "Mas por favor não me leve no lixão..."

    mc normal "Pode deixar. Nada de lixão por enquanto."

    c "Isso. Deixa o lixão pra daqui uns cinco encontros."

    mc "Combinado."

    mc "Vamos descer por ali."

    c "Tá."

    c "Eu vou colocar o pé na areia primeiro!"

    scene black with dissolve

    play sound "audio/som_13_praia.mp3"

    scene pri3_img10 with dissolve

    pause

    c "Iá! Ganhei!"

    c "Hehe!"

    mc feliz "Gosta tanto assim da praia?"

    c "Sei lá. Acho que sim."

    c "Eu me sinto tão livre aqui. Como se não tivesse ninguém querendo mandar em mim."

    c "Tipo viver sem agendas e pessoas dizendo o que você tem que fazer."

    c "Tô até com vontade de rolar na areia!"

    mc normal "Calma. Vai ficar cheia de areia."

    c "Verdade."

    menu:
        "Você pode tirar a roupa antes de rolar.":


            $ priscila_seducao += 1

            mc charmoso "Você pode tirar a roupa e daí não tem perigo de sujar ela."

            if priscila_seducao_evento > 0:

                c "E você ia adorar a vista de eu rolando na areia pelada, né?"

                mc safado "Não brinca com minha imaginação."

                c "..."

                c "Quanto mais você fala essas coisas, mais eu tenho vontade de fazer de verdade."

                c "Se você continuar assim..."

                mc charmoso "Calma que o dia tá começando. Vai acontecer muita coisa ainda hoje."

                mc "E eu tenho certeza que você vai se sentir muito bem."

                c "..."
            else:


                c "Claro. Ficar peladona aqui no meio da praia, né?"

                mc envergonhado "Eu não ia me importar."

                c "Tô vendo que hoje você tirou o dia pra me cantar..."

                mc charmoso "Você sabe o quanto eu te acho linda."

                c "..."

                c "Quem sabe se você se comportar direitinho não tem algo pra você?"

                mc "Hoje eu vou mostrar pra você como um homem deve tratar uma mulher."

                c "Tá..."
        "Quer que eu compre um biquíni?":


            $ priscila_amizade += 1

            mc normal "Quer que eu compre um biquíni pra você?"

            c "Não precisa. Eu sei que a gente vai vir aqui outras vezes."

            c "Posso rolar na areia nas outras vezes."

            mc "Então tá combinado. Vou te trazer aqui de novo. É uma promessa."

            c "Você sabe que eu ia adorar."

    mc "A gente vai ter bastante tempo pra descansar."

    mc "Vamo pegar umas cadeiras e sentar pra lá? O pessoal do restaurante ali empresta."

    c "Ok. Mas onde que você vai pegar cadeira?"









    scene pri3_img11 with dissolve

    c "Você realmente sabe como impressionar uma garota."

    if priscila_seducao_evento > 0:

        mc charmoso "Você sabe o quanto eu quero você, [c]."

        mc "Você é especial pra mim."

        c "Sou?"

        menu:
            "Você sabe o quanto você mexe comigo.":


                $ priscila_seducao += 2

                mc "Você sabe que eu quero ir além com você."

                mc "E eu falo de verdade."

            "Você me deixa louco, mas eu quero conhecer você também." if priscila_amizade_evento <= 0:

                $ priscila_amizade += 2

                mc "Você sabe minhas intenções."

                mc "Mas eu também quero conhecer você melhor. Conhecer seu coração e sua cabeça."

        c "[mc]..."

        c "Você fala de um jeito..."

        c "Você também é especial pra mim."

        mc "Quero aproveitar esse tempo só entre a gente."

        mc "Quero que seja um dia especial."

        c "Eu também."
    else:


        mc normal "Você é muito especial pra mim, [c]."

        menu:
            "Eu quero ser mais que um amigo.":


                $ priscila_seducao += 2

                mc desculpa "Você é uma grande amiga, mas não sei se quero parar nisso."

                mc charmoso "Eu te vejo com outros olhos. Como uma mulher."

                c "Eu não sei, [mc]..."

                c "Falando assim você mexe comigo de um jeito que eu não entendo."

                c "Nos outros encontros eu não te vi assim, mas eu também não sei..."

                mc charmoso "Nosso dia tá começando. Eu vou fazer você entender meus sentimentos."

                c "Tá... Eu também quero entender o que eu sinto."
            "Você é minha melhor amiga.":


                $ priscila_amizade += 2

                mc normal "Você é a amiga mais importante que eu tenho."

                c "Eu sinto a mesma coisa, [mc]. Você é meu melhor amigo."

                c "Eu já desabafei coisas muito sérias com você. E você ficou do meu lado."

                c "Eu sei que posso confiar em você."

                mc "Pode mesmo. Eu estou aqui pra você."

    mc "Vou preparar um lugar pra gente sentar, ok?"

    c "Tá. Valeu."

    scene black with dissolve

    "..."

    mc "Pronto. As cadeiras tão aqui. O sol tá bacana. Parece um..."





    scene priscila praia_cadeira with Dissolve(1.0)

    pause

    c "Aaahh...."

    c "Que delícia! Esse lugar é perfeito!"

    mc envergonhado "..."

    c "Faz tanto tempo que eu não me sinto tão bem, [mc]!"

    mc normal "Fico feliz que você esteja gostando."

    c "O sol... o vento..."

    c "Só deixa eu aqui um pouco..."

    window hide

    pause

    "A [c] é tão linda e divertida. Quando eu tô com ela eu me esqueço de tudo."

    "Ela é uma modelo super conhecida no país. Ela é rica, famosa, amada por milhões de pessoas."

    "E ela ainda dá bola pra mim desse jeito. Conversa comigo..."

    "E às vezes quando a gente tá conversando, sinto que ela sofre com alguma coisa."

    "Nunca tive a chance de conversar coisas mais sérias com ela..."

    mc desculpa "[c]."

    c "Oi?"

    mc "Tá tudo bem com você?"

    c "Quê? Melhor impossível."

    mc "Não digo agora 'agora'. Digo, na sua vida no geral."





    c "..."

    c "Por que você tá perguntando isso?"

    mc desculpa "Sei lá. Só quero ter certeza que tá tudo bem. Você sabe que pode me contar qualquer coisa."

    if priscila_amizade_evento > 0:

        c "Minha carreira tá indo muito bem, e como eu disse eu tô bem cansada."

        mc "Mas é só isso?"

        if priscila_e2 == "amizade":

            c "Lembra no parque? Eu te contei da outra vez que o filme..."

            c "Mas... Isso é uma coisa complicada demais, [mc]."

            c "Eu não quero estragar nosso dia com isso."

            mc "Tudo bem se não quiser falar sobre isso agora."

            c "Obrigada. Quem sabe depois..."

            c "Eu fico muito feliz de poder falar isso pra alguém. Só que não agora."

            mc normal "Eu entendo. Vamos falar disso depois."

            c "Co-combinado..."
        else:


            c "É só isso..."

            mc "Então tá. Você sabe que qualquer coisa pode falar comigo, né?"

            c "Eu sei. Pode deixar."

            "Eu tenho a impressão que ela não me disse tudo."

            "Quem sabe depois eu posso voltar nesse assunto."
    else:


        c "Está tudo bem, sim."

        mc desculpa "Certeza?"

        c "Sim. Não quero que você fique pensando nisso. Quero que você pense em outras coisas quando olhar pra mim."

        c "O que você pensa quando me vê assim?"

        mc safado "Eu penso que esse corpo é o mais bem-feito da Terra."

        c "Isso. Você mexe tanto comigo. Quero que você sinta isso também."

        mc charmoso "Você sabe que eu sinto."

        c "Então não pense besteira."

        mc desculpa "Tá certo..."

        "Ela não quer me falar."

        "É como se ela não confiasse em mim pra isso."

        "Eu acho que ela sente uma grande atração por mim... Só que ela não tem coragem de me contar essas coisas."

        "Sei lá se isso é problema meu também. Mas algo dentro de mim parece que me deixa ansioso."

        "Aquelas ligações devem ter me deixado cabreiro. Preciso esfriar a cabeça."

    mc feliz "Ah!"

    c "Que foi?"

    mc "Tenho uma surpresa pra você."

    c "O quê?"

    mc "Eu vi lá no restaurante quando a gente foi pegar as cadeiras. Pera aí que vou pegar pra você."

    c "Ok. Tô esperando."

    scene praia dia with Dissolve(1.0)

    "..."

    mc feliz "[c]!"

    mc "Pega!"

    c "Quê?! Eii!"

    play sound "audio/som_13_praia.mp3"

    scene priscila praia_bola with Dissolve(1.0)

    pause

    c "!"

    c "Uma bolona!"

    mc feliz "Sim!"

    c "..."

    c "É pra mim?"

    mc normal "Presente."

    c "..."

    mc "Tá em choque?"

    c "Ela é tão colorida. Eu nunca tive uma bola."

    mc zerado "Tá me zuando."

    c "É sério!"

    mc envergonhado "Não é nada de mais, [c]..."

    c "..."

    mc normal "Nunca vi uma pessoa ficar paralisada por causa de uma bola."

    c "Para de tirar sarro de mim e da minha bolona!"

    mc "..."

    c "Então pega!"

    scene praia dia with Dissolve(1.0)

    mc "Ei! Não vale atacar na minha cara!"

    c "Hahaha! Toma essa senhor não ligo pra bolas!"

    mc "..."

    "..."

    "A gente passou o resto do dia na praia. Aproveitando que teve sol o dia todo."

    "Até que finalmente começou a escurecer."

    scene black with dissolve

    play sound "audio/som_13_praia2.mp3"

    $ tempo += 1

    scene pri3_img12 with dissolve

    c "Cansei..."

    c "Nem sabia que dava pra se cansar de se divertir."

    mc charmoso "Que bom que você se divertiu. Pelo menos você não tomou uma bolada na cara e nem jogaram água na sua roupa."

    c "Pelo menos você pode tirar a camisa."

    mc "Ninguém tá te impedindo."

    c "Engraçadinho..."

    c "Bateu aquela fome agora."

    mc "Que bom. Porque a segunda parte da programação vai resolver seu problema."

    c "Verdade? Tem comida envolvida?"

    mc normal "Exatamente."

    mc "Vem comigo."

    scene black with dissolve

    scene praia restaurante with Dissolve(2.0)

    mc "O que achou?"

    c "A gente vai comer aqui?"

    mc "Sim."

    c "Nossa, [mc]. Parece um lugar tão especial."

    menu:
        "Queria fechar o encontro com chave de ouro.":


            $ priscila_amizade += 1

            mc charmoso "Queria fechar nosso encontro da melhor forma possível. A gente merece."

            c "Você tá me mimando demais hoje."

            mc normal "Não é grande coisa."

            c "Claro que é. Olha pra esse lugar. Nunca comi num lugar assim."

            mc "Eu também não pra falar a verdade. Vamos ver se é tão bom quanto parece."

            c "Opa! Com certeza."
        "Comigo é só coisa do bom e do melhor.":


            $ priscila_seducao += 1

            mc charmoso "Comigo não tem coisa meia boca."

            mc "Só o melhor para a garota mais linda que eu já vi na vida."

            c "Ai, [mc]..."

            c "Assim você vai acabar me conquistando..."

            mc "É a intenção."

            c "..."

            mc "Vamos entrar. Espero que seja tão bom quanto parece."

            c "Com certeza vai ser."

    play sound "audio/som_6_bar.mp3"

    scene black with dissolve

    scene pri3_img13 with dissolve

    pause

    mc normal "Vamos sentar aqui."

    c "Tá legal."

    mc "A gente nunca conversou sobre o seu trabalho, né?"

    mc "Como é ser adorada por tanta gente?"

    c "A gente não precisa falar sobre isso. É chato."

    menu:
        "Ok. Não vamos falar disso então.":


            mc normal "Beleza. Se você prefere não falar dessas coisas."

            c "Vamos aproveitar o por do sol e a comida."

            c "O dia tá tão legal."

            mc "Combinado."

            "..."
        "Não é chato. Eu quero saber mais sobre você.":


            $ priscila_amizade += 1

            mc normal "Eu não acho chato. Tenho bastante curiosidade na verdade."

            c "Certeza?"

            mc "Ahã."

            c "Então tá."

            c "Ser modelo tem seu lado bom e seu lado ruim como todas as profissões eu acho."

            mc charmoso "Modelo super-famosa. Não esqueça disso."

            c "É uma correria danada. Eu passo a maior parte do tempo viajando de um lugar pra outro pra participar de eventos."

            c "Ou trancafiada nos estúdios de fotografia, posando pras capas e matérias."

            mc normal "Problemas do primeiro mundo?"

            c "Pode ser..."

            mc desculpa "Tô brincando. Parece bem cansativo e, desculpa falar, mas até um pouco chato."

            c "Pois é. Você precisa gostar. Porque os eventos até são mais divertidos, mas tirar fotos é realmente bem técnico."

            c "A gente precisa fazer várias caretas..."

            c "Seja sexy! Seja encantadora! Seja inspiradora!"

            c "E eu assim, assim, assim, tem que ir mudando as caras e os jeitos pra cada produto."

            mc "Caraca! E como você consegue contratos fazendo essas caras?"

            c "Como é?"

            mc normal "Tô só te enchendo."

            if priscila_seducao_evento > 0:

                c "Hmmm..."

                scene pri3_img14 with dissolve

                c "Assim que você gosta, né?"

                mc surpreso "!"

                c "Tô contratada, senhor presidente?"

                mc "A... a...."

                c "Ficou sem palavras?"

                c "Tadinho do engraçadinho..."

                c "Será que ele tá pensando como é isso aqui sem roupa? Que droga esses panos atrapalhando, né?"

                mc "Si-sim..."

                c "Ele nem sabe mais o que tá falando..."

                c "Tá bom. Já pode voltar."

                mc charmoso "..."

                mc "Fazer isso é sacanagem."

                c "Não gostou?"

                mc safado "Você sabe que eu adorei."

                c "..."

            "Garçonete" "{i}Cof cof...{/i}"

            "Priscila e [mc]" "?"

            "Garçonete" "Desculpa incomodar."

    "Garçonete" "O que o casal vai querer?"

    scene pri3_img14 with dissolve

    c "Casal?"

    menu:
        "O que você vai querer, amor?":


            mc charmoso "Pode pedir, amor. Eu vou acompanhar você."

            c "E-eu..."

            c "Eu vou querer então esta sopa de camarão."

            c "E você, querido?"

            mc envergonhado "Não vale querer me deixar sem jeito também..."

            c "..."
        "Somos apenas amigos.":


            $ priscila_amizade += 1

            mc normal "Somos apenas amigos passando a tarde juntos."

            c "Isso. Esse cara é incrível. Tá me dando um dia de rainha."

            "Garçonete" "..."

            mc normal "Que bom que você tá curtindo, mas não é pra tanto assim."

            c "É sim. Ele que é modesto."

            "Garçonete" "..."

            c "Melhor eu pedir..."

            c "Eu vou querer então esta sopa de camarão."

            c "E você?"
        "A gente é amigo, por enquanto...":


            $ priscila_seducao += 1

            mc charmoso "A gente não é um casal... ainda."

            mc "Depende dela."

            "Garçonete" "A é? E como ele tá indo?"

            if priscila_seducao_evento > 0 and priscila_amizade_evento > 0:

                c "Ele tá indo muito bem..."

                c "Ele se importa comigo, e também é muito charmoso e sexy."

                c "O [mc] mexe muito comigo..."
            else:


                if priscila_seducao_evento > 0:

                    c "Ele é muito sexy e muito charmoso."

                    c "Ele sabe como mexer comigo."

                    c "Só temos que ver se ele é pra casar, né?"

                elif priscila_amizade_evento > 0:

                    c "Ele é um grande amigo. Alguém que me entende de verdade e em quem eu confio."

                    c "Mas eu não consigo ver ele como um namorado..."

                    c "Eu não tô com ele por segundas intenções. Ele é realmente um cara legal."

            "Garçonete" "..."

            "Garçonete" "Eu tava mais brincando, mas tudo bem..."

            c "Ah! Desculpa..."

            mc feliz "Haha..."

            c "Melhor eu pedir..."

            c "Eu vou querer então esta sopa de camarão."

            c "E você?"

    "Garçonete" "?"

    mc normal "Eu vou querer..."

    menu:
        "Peixe":


            mc normal "Filé de Pescada Branca."

            c "Peixe é muito bom e é leve também."
        "Camarão":


            mc "Camarão frito no alho."

            c "Eu adoro camarão!"
        "Carne vermelha":


            mc "Medalhão de filé mignon."

            c "Certeza que você vai comer carne de vaca aqui?"
        "Salada":


            mc "Salada de alface e palmito."

            c "Que cara mais light."

    "Garçonete" "Tá anotado. Eu já trago."

    mc normal "Obrigado."

    c "Hmmm..."

    c "Essa conversa com ela me lembrou da gente no parque, lembra? Com aquela mocinha?"

    if e1_priscila_namorado == "namorado":

        c "Você falou pra ela que a gente era namorados..."

        mc feliz "Eu lembro, sim. Você ficou mó sem jeito."

        c "Foi sacanagem aquilo lá."

        c "Se bem que pensando agora... Essa ideia não é assim tão esquisita..."

        mc charmoso "..."

    elif e1_priscila_namorado == "silencio":

        c "Você ficou quieto e ainda riu de mim!"

        mc feliz "Eu lembro, sim. Você ficou mó sem jeito. Desculpa! Mas tava fofa demais."

        c "..."
    else:


        c "Você me ajudou e explicou pra ela. Obrigada por me tirar daquela enrascada."

        mc envergonhado "Tudo bem. Foi minha culpa também."

        c "..."

    show black with dissolve

    "..."

    hide black with dissolve

    c "Opa! Acho que nossa comida tá chegando."

    mc charmoso "Bon apetit"

    c "Valeu!"

    show black with dissolve

    c "Hmm... Tá bom isso aqui..."

    hide black with dissolve

    mc normal "Nossa, a janta passou voando."

    c "Tava uma delícia! Eu adorei o camarão. E o caldo tava tão gostoso também."

    mc "Que bom. O meu também foi excelente."

    "Smartphone" "{i}Talá... lalalá... lalalá...{/i}"

    scene pri3_img14 with dissolve

    c "Opa. É o meu celular. Só um segundo."

    c "Vou ali fora e já volto, tá?"

    mc "Claro."

    scene praia r_interior with dissolve

    "Parece algo sério..."

    "Por que será que ela não quis atender aqui?"

    menu:
        "Escutar a conversa escondido":


            "Tô curioso demais só pra esperar ela aqui."

            "Se eu só chegar perto e tomar cuidado ela não vai me ver."

            "..."

            scene black with dissolve

            "Vou ficar aqui. Acho que dá pra ouvir."

            scene pri3_img16 with dissolve

            pause

            c "{size=15}Sim. Tô com ele. E daí?{/size}"

            c "{size=15}Eu tô bem, [a].{/size}"

            c "{size=15}...{/size}"

            c "{size=15}Quê?! Mas eu já vi ele hoje. Não! De jeito nenhum!{/size}"

            c "{size=15}...{/size}"

            c "{size=15}Só conversar? Muito estranho...{/size}"

            c "{size=15}Eu não sei, [a]. Você sabe que eu tô arrependida de tudo isso.{/size}"

            c "{size=15}...{/size}"

            c "{size=15}Eu sei. Tá bom. Eu vou ser forte.{/size}"

            c "{size=15}Tá legal. Mas eu quero mais um tempo.{/size}"

            c "{size=15}Não! Já falei que não agora.{/size}"

            c "{size=15}Tchau!{/size}"

            c "{size=15}Que saco...{/size}"

            "..."

            "Ela tá voltando!"

            "..."
        "Esperar ela voltar":


            "Tenho que dar privacidade pra ela. Não adianta eu querer me meter."

            "..."

            "..."

    scene black with dissolve

    scene pri3_img15 with dissolve

    c "Oi..."

    mc preocupado "Oi. Aconteceu alguma coisa?"

    c "Não. Tá tudo legal."

    mc "Você não parece nada legal."

    c "..."

    mc normal "Quer saber? Tá ficando meio tarde."

    c "Quê?"

    mc feliz "O que você acha da gente dar uma última andada na praia antes de voltar?"

    c "..."

    c "Eu ia gostar muito."

    mc charmoso "Então vamos. Depois da senhorita."

    c "Obrigada."

    scene black with dissolve

    play sound "audio/som_13_praia.mp3"

    scene praia tarde with Dissolve(1.0)



    "..."

    mc normal "E daí o [gar] me ofereceu aquela bebida louca..."

    c "..."

    mc desculpa "Alô? Tem alguém aí?"

    scene pri3_img17 with dissolve

    c "Desculpa, [mc]. Não sei o que aconteceu comigo. Acho que tô meio cansada."

    mc preocupado "..."

    "O dia tá acabando... Se eu não fizer nada agora vai ser outra oportunidade perdida."

    "Essa é minha última chance."

    "Todas as escolhas que eu tomei desde que eu conheci a [c] foi pensando nesse momento."

    "Eu preciso decidir o que eu quero com ela."

    "O que você quer com ela, [mc]?"

    menu:
        "Eu quero ser o melhor amigo dela.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pe3_escolheu_amizade","escolheu","priscila")

            $ priscila_amizade += 3
            $ p3_escolha = "amigo"

            "Eu quero ser o melhor amigo dela."

            "Alguém que ela possa confiar e que possa estar lá para ela em todos os momentos."
        "Eu quero levar ela pra cama.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pe3_escolheu_sexo","escolheu","priscila")

            $ priscila_seducao += 3
            $ p3_escolha = "sexo"

            "Ela me deixa com muito tesão e eu só quero poder levar ela pra cama."

            "Não vejo a hora de poder transar com ela."
        "Eu quero uma relação séria.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("pe3_escolheu_namoro","escolheu","priscila")

            $ priscila_amizade += 2
            $ priscila_seducao += 2
            $ p3_escolha = "namorado"

            "Ela mexe comigo, mas eu quero ir além. Não quero ficar só na amizade e nem só comer ela."

            "Quero que ela seja minha parceira pra todas as coisas."

    mc concentrando "..."

    mc normal "Hoje foi um dia cansativo mesmo."

    mc charmoso "Eu gostei de todos os momentos."

    mc "Quando eu tô com você eu esqueço de todas as coisas. Eu só consigo olhar pra você."

    c "[mc]..."

    c "Você sabe como eu gosto de você também. Eu gosto tanto que nem eu entendo meus sentimentos às vezes."

    mc "O que acha da gente sentar aqui e ver o por do sol juntos?"

    c "Você é muito romântico."

    mc "Eu só quero passar um momento bacana com você."

    c "Eu me sinto tão bem com você."

    mc "Senta aqui."

    c "Tá."

    play sound "audio/som_13_praia2.mp3"

    scene priscila praia_sentados with Dissolve(2.0)

    pause

    c "O sol tá tão bonito agora, [mc]."

    if p3_escolha == "amigo":

        mc "Eu também acho. E é incrível poder ver isso com você."

        mc "Você é minha melhor amiga, [c]."

        mc "Você me salvou de ser despedido e de voltar a morar com meus pais. Que era a coisa que eu menos queria."

        mc "E me deu bola, sentou e conversou comigo no bar. E no parque..."

        mc "Eu não sei como agradecer você. E nem sei o que eu fiz pra merecer sua atenção assim."

        c "[mc]..."

        c "Não pegue tão pesado com você. Você é um cara incrível, sabia?"

        c "Você fala como se você nunca tivesse sorte com as garotas, mas elas que foram tontas."

        c "Eu te acho bonito, e até charmoso às vezes. E isso é o de menos. Você é um cara muito bacana."

        c "Eu que tive sorte de te conhecer."
    else:


        mc "Mas eu só consigo olhar pra você, mesmo com esse por do sol."

        mc "E não falo isso como uma cantada barata, [c]."

        mc "Você é a garota mais incrível com a qual eu tive a chance de conversar."

        mc "Eu me sinto enfeitiçado por você. Como se eu nunca conseguisse parar de te olhar."

        c "[mc]..."

        c "Você é tão confiante. Você fala essas coisas... Me deixa sem jeito toda vez..."

        c "Eu queria poder falar coisas bonitas também. Mas sou só uma modelo tonta..."

        mc "Nunca mais fale isso."

        mc "Você não é só linda. Você é determinada, você é confiante também."

        mc "Você é bem-sucedida, mas não é mesquinha. Não só seu corpo, mas sua personalidade também me deixa louco."

        c "Ai, [mc]..."

    $ renpy.notify("Priscila está avaliando suas ações no encontro...")

    if priscila_amizade >= 16:

        $ priscila_amizade_evento += 1

    if priscila_seducao >= 16:

        $ priscila_seducao_evento += 1

    if priscila_amizade_evento > 0:

        c "Desculpa se eu sou uma garota complicada..."

        c "Eu queria que as coisas fossem mais simples, [mc]."

        c "Mas é tudo tão complicado. Eu tenho tanta vontade de chorar."

        mc "Você pode chorar, [c]. Pode falar o que tá sentindo."

        c "Não sei se eu posso..."

        if priscila_seducao_evento > 0:

            $ renpy.notify("Priscila achou você sexy e charmoso...")

            c "..."

            c "Você é tão sexy e charmoso. Eu fico sem ar, meu peito fica quente."

            c "Eu tenho vontade de te beijar."

            mc "Eu sinto a mesma coisa."

            c "Mas tenho medo de estragar isso com meus problemas."

            if p3_escolha == "sexo":

                menu:
                    "Vamos esquecer tudo isso e pensar no prazer.":


                        jump priscila_e3_sexo
                    "Eu quero seu corpo, mas quero estar do seu lado.":


                        mc "Você sabe o quanto tesão eu sinto, mas não é só seu corpo que eu quero."

                        mc "Eu quero mais que isso."

                        c "Tem certeza que não vou estragar tudo?"

            mc "Não vai estragar nada. Eu quero te conhecer. Não é só físico o que eu sinto."

        label priscila_e3_finalamizade:

            $ persistent.priscila_cena5 = True

            scene priscila praia_sentados

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e3_confissão","escolheu","priscila")

        $ p3_confissao = True

        c "..."

        mc "Por favor confia em mim. Eu tô aqui pra você."

        $ renpy.notify("Priscila achou você confiável e um verdadeiro amigo...")

        c "Você..."

        c "Você vai ter nojo de mim, [mc]."

        mc "Nunca."

        c "..."

        if priscila_e2 == "amizade":

            c "Lembra do filme que eu disse pra você no parque eu ia estrelar?"

            mc "Sim."

            c "Então..."
        else:


            c "Eu vou estrelar um filme muito importante. É o filme mais caro da história do cinema no país."

            c "E eu vou ser a atriz principal."

            mc "Isso parece incrível..."

        c "Só que... o que eu tive que fazer pra... conseguir o papel..."

        c "Não consigo falar, [mc]. Eu vou vomitar..."

        mc "Você consegue, [c]. Você precisa disso."

        c "..."

        c "Eu... {size=15}tive que transar com o diretor do filme.{/size}"

        c "{i}Ugh{/i}"

        c "E não só uma vez..."

        c "Eu me vendi por esse papel, [mc]!"

        c "{i}Ughhh{/i}"

        c "E-eu não mereço nada!"

        mc "..."

        c "Por favor! Não olhe pra mim!"

        mc "..."

        mc "[c]..."

        c "... {i}Uegh{/i}..."

        c "Eu... sou uma puta... que se vende pra um velho corno e desgraçado..."

        mc "..."

        c "O que eu faço agora, [mc]?"

        c "Eu não consigo dormir direito..."

        c "Eu tô desesperada!"

        mc "[c]..."

        mc "[c]... Eu não consigo imaginar... como é ter isso dentro de você e não poder falar pra ninguém."

        c "..."

        mc "Eu fico muito feliz... de você ter me contado. De você ter confiado dessa forma em mim."

        mc "Eu prometo que eu vou te ajudar. Da forma que você precisar."

        c "Você não tem nojo de mim? {size=15}Eu sou suja, [mc]...{/size}"

        mc "Claro que eu não tenho nojo de você. E você não é suja. Esse mundo é sujo, [c]."

        mc "Você é a pessoa mais importante pra mim agora e eu vou fazer tudo o que eu puder pra estar ao seu lado."

        mc "Pode contar comigo pro que precisar. Continua confiando em mim por favor."

        c "[mc]... Você..."

        $ renpy.end_replay()

        if priscila_seducao_evento > 0 and not p3_escolha == "amigo":

            label priscila_e3_finalbeijo:

                $ persistent.priscila_cena6 = True

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("priscila_e3_beijo","escolheu","priscila")

            $ priscila_e3_beijo = True

            c "Por favor... me abraça. Me beija, por favor."

            mc "[c]."

            c "Eu preciso de você."

            mc "..."

            scene black with dissolve

            scene priscila praia_beijo with Dissolve(1.0)

            pause

            c "..."

            mc "..."

            c "Me abraça bem forte."

            mc "..."

            c "Fica comigo por favor."

            mc "Eu tô do seu lado."

            window hide

            pause

            scene priscila praia_beijo2 with Dissolve(1.0)

            pause

            "Eu não sei há quanto tempo a gente tá assim."

            "Ela tremeu, chorou, me apertou..."

            "Eu também tô tremendo. Eu não sei o que vai acontecer quando eu soltar ela."

            "..."

            "..."

            window hide

            pause

            $ renpy.end_replay()

        scene praia tarde with Dissolve(1.0)

        c "..."

        scene pri3_img18 with dissolve

        c "..."

        c "Minha cabeça tá girando..."

        c "Eu tô sem ar..."

        mc preocupado "Você precisa descansar."

        c "Sim..."

        c "[mc]..."

        mc "Que foi?"

        c "Ainda não acredito que você tá aqui comigo."

        mc "Claro que eu tô..."

        c "..."

        c "Você é a pessoa mais especial que eu tenho, [mc]."

        c "Obrigada por não ter nojo de mim."

        mc "Eu nunca teria nojo de você. Eu disse que você é incrível. E nada disso vai mudar o que eu sinto."

        c "..."

        c "Eu acho... que eu tô melhor..."

        c "..."

        c "Desculpa. Desculpa por jogar isso em você."

        mc desculpa "Não precisa disso. Eu fiquei feliz de você ter falado essas coisas pra mim por pior que tenha sido pra você."

        c "..."

        c "Você é realmente um cara especial..."

        c "..."

        c "Eu ainda não tô legal."

        jump priscila_e3_final
    else:


        jump priscila_e3_sexo

    label priscila_e3_sexo:

        $ persistent.priscila_cena7 = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e3_sexo","escolheu","priscila")

        $ priscila_e3_sexo = True

        mc "Eu acho que a gente tem que aproveitar o tesão que a gente sente um pelo outro e esquecer os problemas."

        mc "Eu quero te dar muito prazer, [c]."

        $ renpy.notify("Priscila só consegue pensar em transar com você...")

        c "Por favor. Me faz esquecer de tudo isso, [mc]."

        c "Me beija! Me aperta! Me dá prazer de verdade!"

        mc "Eu vou fazer você gozar até esquecer seu nome."

        scene black with dissolve

        scene pri3_img19 with dissolve

        pause

        mc "Traz essa boca aqui."

        c "Isso, [mc]... Ai... Me beija mais forte. Você tá me deixando louca."

        c "Hmmm..."

        mc "Vem aqui. Deixa eu tirar sua calça."

        c "Ai, [mc]. Eu tô toda molhada."

        mc "Vem aqui. Agora que vou te deixar louca de verdade."

        c "..."

        scene priscila praia_sexo with Dissolve(2.0)

        pause

        c "Ai! [mc]! Assim!"

        mc "..."

        c "Aiii... que gostoso..."

        c "Ai, [mc]!"

        menu:
            "Devorar a buceta dela com gosto":


                scene black with dissolve

                scene ani06 with Dissolve(1.0)

                pause

                mc "Eu vou provar todo esse suquinho gostoso."

                c "A-ah... [mc]..."

                c "Nunca ninguém me chupou... aaahh... é tão g-gostoso..."

                mc "Depois dessa você vai viciar."

                c "Awnn... aaah..."

                mc "Que delícia de buceta que você tem. Docinha."

                c "Ahhn... é g-gostosa, é?"

                mc "Muito!"

                c "Então vai, safado... ahnn... devora ela, vai..."

                menu:
                    "Judiar dela indo devagar":


                        mc "Eu vou... mas bem devagar..."

                        scene black with dissolve

                        scene ani07 with Dissolve(1.0)

                        pause

                        c "Awwnnn... n-não..."

                        mc "Não vai gozar, não, safada."

                        c "Meu Deus... aaanhnn..."

                        mc "Uma xotinha dessas a gente tem que aproveitar o máximo."

                        c "Ai... awnn... delícia... deixa eu gozar, deixa..."

                        mc "Vai me dar tudo, vai?"

                        c "V-vou... ah..."
                    "Quer gozar, é?! Então toma, vadia!":


                        pass

                c "P-por favor! Me faz gozar igual uma louca! Eu PRECISO!"
            "Finalizar rápido":


                pass

        mc "Quer gozar, é?! Então toma!"

        c "{i}puf{/i}"

        c "Isso! Assim!"

        c "Eu já vou gozar!"

        c "{i}puf{/i}"

        c "Aaaiiii!"

        scene pri3_img20 with vpunch

        c "aAAAAIHHHH!"

        c "{i}puf{/i}"

        c "Eu tô... tô tremendo..."

        c "Deixa eu colocar a roupa... Tá tudo molhada..."

        c "..."

        c "..."

        mc safado "..."
        scene pnew_ani05 with Dissolve(1.0)
        c "Eu nunca senti uma coisa tão gostosa assim, [mc]."

        mc safado "Gostou?"

        c "Eu nem sei onde eu tô...."

        mc charmoso "Que bom."

        c "Mas e você?"

        mc "Não se preocupe comigo hoje. Você tava precisando disso."

        c "Você é incrível, [mc]. Eu prometo que vou te recompensar."

        mc charmoso "Nós vamos ter outras oportunidades."

        c "Ai... Com certeza..."

        $ renpy.end_replay()

        "..."

        scene black with dissolve

        scene pri3_img18 with dissolve

        c "Hoje foi um dia e tanto."

        c "Tô me sentindo melhor. Como se tivesse drogada."

        c "Obrigada."

        mc safado "O prazer foi meu."

        c "..."

    label priscila_e3_final:

        c "Eu acho que eu quero voltar pro hotel."

        mc normal "Você quer que..."

        "???" "É uma excelente ideia, [c]. Você está tempo demais aqui."

        c "Vo-você!"

        scene pri3_img21 with hpunch

        "Senhor" "Oi, querida."

        c "O que você tá fazendo aqui, [gus]?!"

        gus "Vim apenas ver minha atriz preferida."

        if p3_confissao:

            "Então esse é o velho desgraçado que tá causando tudo isso na vida da [c]."

            "Se eu pudesse eu socava esse velho na fuça agora."

        c "Como você sabia que eu tava aqui?!"

        gus "Isso não importa, querida."

        c "..."

        gus "A gente tem uma reunião agora."

        c "Que reunião?!"

        scene pri3_img23 with dissolve

        gus "Você quer falar sobre isso na frente desse desconhecido? Ele é um paparazzo."

        c "E daí?! Pode falar o que quiser na frente do [mc]. Eu confio nele."

        gus "Só venha comigo, [c]."

        menu:
            "Entrar na frente dela e brigar com o velho":


                mc bravo "Espera!"

                c "[mc]..."

                mc "Ela não parece querer ir com você, velho. Por que você não dá o fora daqui?"

                gus "Não estou falando com você. Meu assunto não é com jornalista de quinta."

                mc "Eu estou falando com você. Pode dando o fora antes que eu te coloque pra fora dessa praia."

                gus "..."

                gus "[mar]."

                scene pri3_img22 with dissolve

                gus "Não deixe esse paparazzo chegar perto de mim."

                mar "Sim, senhor diretor."

                if marco_conheceu:

                    "Esse cara! Eu vi ele na frente do hotel da [c]!"

                    "É como se eles tivessem vigiando ela."

                    "Provavelmente o velho tarado sabe tudo sobre o que aconteceu com a gente hoje."

                mar "Oi, [mc]."

                "Ele sabe meu nome..."

                "Parece que eu vi esse cara antes, muito antes de hoje... Não lembro onde..."

                "Era um dia de noite..."

                "Espera! No bar!"

                "No dia que eu conheci a [c]!"

                window hide

                show tela p3_1 with Dissolve(1.5)

                pause

                "Os seguranças... Um deles era esse homem..."

                "Espera... Naquela noite... quando coloquei a [c] no carro..."

                window hide

                show tela p3_2 with Dissolve(1.5)

                pause

                if p3_confissao:

                    "Tudo tá fazendo sentido agora."

                    "Desde aquele dia..."

                    "Não acredito..."
                else:


                    "O que isso quer dizer?"

                    "Eles estavam atrás dela desde aquele dia?"

                    "Mas por quê?"

                hide tela with dissolve

                "..."

                mar "Não se intrometa que isso é coisa deles."

                mc bravo "..."

                "Não tenho chances contra esse cara... Que merda!"

                scene pri3_img17 with dissolve

                c "[mc] por favor não faça uma loucura. Eu não quero isso."

                mc serio "Tudo bem. Desculpa."
            "Deixar ela resolver a situação":


                "Não adianta eu me meter nas coisas dela. Só vou atrapalhar mais do que ajudar."

        c "..."

        c "Ok. Eu vou pra tal 'reunião'. Mas eu vou me despedir do [mc]. Vai na frente e já vou pro carro."

        scene pri3_img23 with dissolve

        gus "..."

        gus "Como queira..."

        mc preocupado "Isso não tá certo, [c]."

        scene pri3_img17 with dissolve

        c "Não se preocupe comigo, [mc]."

        c "Eu sei me cuidar."

        mc desculpa "..."

        c "Acho que hoje foi o dia mais feliz da minha vida."

        mc preocupado "..."

        c "Você fez eu me sentir tão especial. A garota mais importante do mundo."

        mc desculpa "É o mínimo que você merece."

        c "Não fica com essa cara. Eu ainda vou ficar alguns dias na capital."

        c "A gente vai se ver de novo, tá?"

        mc "Ok. Por favor, toma cuidado com ele."

        c "Pode deixar."

        c "Vou te escrever. E vou morrer de saudades."

        c "Até outra hora, [mc]."

        mc preocupado "Até, [c]. Se cuida."

        scene black with dissolve

        scene pri3_img24 with dissolve

        pause

        "Eu vou mesmo deixar ela ir com aquele velho?"

        if p3_confissao:

            "Mesmo depois de tudo o que ela me contou?"

            "Será que não tem nada que eu possa fazer pra mudar isso?"
        else:


            "Parece que ele deixou ela muito perturbada."

            "Será que eu fiz a escolha certa?"

        "Eu nunca me senti tão impotente quanto agora..."

        $ v6_fim = True
        $ dia_priscila = dia + 1
        $ dia_priscila_evento = dia + 1

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v6_fim","v6","terminou")

        mc irritado "Que droga!"

        scene black with Dissolve(2.0)

    jump call_cidade



label priscila_evento4:

    scene black with Dissolve(1.0)

    "..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p4_save", extra_info="p4_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "{b}4 dias depois{/b}"

    $ dia += 4

    "Aquele dia na praia com a [c] foi uma loucura..."

    "Eu preciso de um tempo pra pensar em tudo o que aconteceu."

    "Melhor eu dar uma parada em casa."

    "..."

    if casa:

        scene ap cozinha with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    "Quando a gente saiu lá na praia..."

    if casa:

        scene ap mc_cozinhando1 with Dissolve(1.0)
    else:


        scene mc ap_pensando with Dissolve(2.0)

    if p3_confissao:

        "Todas as coisas que ela me contou sobre o filme... sobre o diretor..."

        "Ela parecia tão desesperada sobre tudo aquilo. E eu não pude fazer nada..."

        "E o idiota ainda teve a cara de pau de aparecer lá como se tudo estivesse normal."

        "Aquele era o [gus], o tal diretor de cinema."

        "Maldito..."

        mc "O que eu posso fazer pra ajudar a [c]?"

        "O que eu não entendo é por que ela aceitou fazer isso. Ela parecia tão arrependida de ter se envolvido com essa gente."

        "Será que ficar do lado dela é realmente a única coisa que eu posso fazer?"
    else:


        "A [c] parecia tão desesperada com algo. Mas parece que ela não teve coragem de me falar."

        "Aquele velho tinha algo a ver com tudo aquilo."

        "Mas eu não tenho informações suficientes pra entender o que tá rolando."

        "Seja como for, eu quero ficar do lado dela e ajudar no que eu puder."

    "Smartphone" "Trrr... Trrr..."

    if casa:

        scene ap mc_cel with Dissolve(1.0)
    else:


        scene mc ap_celular with Dissolve(1.0)

    $ priscila_cel_msg5 = True

    mc "Falando nela..."

    show screen celular_priscila

    pause

    mc "!"

    mc "Q-que que é isso?!"

    "Como assim adeus?!"

    "Ela tá saindo fora da ilha? Mas por que ela falaria desse jeito?"

    "Será que ela ficou triste comigo por alguma coisa?"

    "Droga... Preciso escrever alguma coisa pra ela."

    "..."

    $ priscila_cel_msg5_r = True

    show screen celular_priscila

    pause

    "Tomara que ela me responda..."

    "..."

    "..."

    mc "Droga."

    mc "Vou tentar ligar."

    "..."

    "Smartphone" "Tuu... Tuuu...."

    "..."

    mc "Merda."

    "O que será que ela tá pensando? O que eu faço?"









    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene mc ap_pensando with Dissolve(1.0)

    "Não posso perder a cabeça. Eu queria sair atrás dela, mas nem sei onde ela pode estar agora."

    "Eu sempre senti que havia algo de errado com a [c]. Desde nosso primeiro encontro."

    "Aquela noite no bar não foi normal. Ela estava se esforçando pra parecer normal, mas eu senti que havia algo de errado."

    "Os seguranças indo buscar ela. Ela nunca teve segurança em nenhum de nossos encontros."

    "E a forma como tudo aconteceu. Ela parecia alegre, mas no fundo era óbvio que ela tava abalada com algo."

    "E depois as coisas que eu li no celular dela. Aquele e-mail... Não lembro exatamente agora, mas era tudo tão estranho."

    if p3_confissao:

        "E ainda depois que ela me explicou o que teve que fazer pra conseguir o papel no filme... tudo fez sentido."

        "Aquele maldito diretor..."

        "Eu tenho que fazer alguma coisa sobre isso..."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trrr... Trrr..."

    "Algum número desconhecido me ligando..."

    if casa:

        scene ap mc_cel with Dissolve(1.0)
    else:


        scene mc ap_celular with Dissolve(1.0)

    stop sound

    mc "Alô? Quem fala?"

    "Voz Feminina" "[mc]?"

    mc "Sim. Quem é?"

    a "Meu nome é [a] e eu sou a agente da [cc]. Você tem falado com ela nos últimos tempos, não tem?"

    mc "Sim, tenho. Mas..."

    a "Será que você poderia me encontrar no bar próximo da sua casa?"

    menu:
        "Certo. Estou saindo.":


            mc "Tudo bem. Vou sair agora."

            a "Perfeito. Já estou aqui te esperando."

            jump priscila_e4_agente
        "Por que você quer falar comigo?":


            mc "Por que você quer falar comigo? Aconteceu alguma coisa com a [c]?"

            a "Sim. Ela está desaparecida. Achei que talvez ela estivesse com você."

            mc "Não. Não está. Como assim desaparecida?"

            a "Esse assunto é delicado demais para falarmos por telefone. Você pode me encontrar no bar?"

            menu:
                "Não posso. Vou procurar a [c].":


                    mc "Você tá louca?! A gente precisa procurar a [c]!"

                    a "Não seja idiota. Onde você vai procurar ela?"

                    mc "Eu..."

                    a "Temos que tentar descobrir pra onde ela foi antes."

                    mc "..."

                    menu:
                        "Não importa. Eu vou procurar ela em todos lugares.":


                            mc "Não importa! Eu preciso encontrar ela!"

                            a "Você é teimoso mesmo, hein?"

                            mc "..."

                            a "Boa sorte."

                            mc "Adeus."

                            jump priscila_e4_procurar
                        "Você tem razão. Estou indo para o bar.":


                            mc "Acho que você está certa."

                            a "Você vem então?"

                            mc "Sim. Já estou saindo."

                            a "Perfeito."

                            jump priscila_e4_agente
                "Ok. Te encontro no bar em alguns minutos.":


                    mc "Tudo bem. Daí você me explica melhor o que tá havendo."

                    a "Estou te esperando."

                    mc "Até."

                    jump priscila_e4_agente

    label priscila_e4_procurar:

        if casa:

            scene ap sala with Dissolve(1.0)
        else:


            scene apartamento geral with Dissolve(1.0)

        "Não sei como ela consegue ficar tão calma em uma situação dessas."

        "Preciso me apressar. A mensagem da [c] me deixou muito preocupado."

        mc serio "Não se preocupe, Pri. Eu vou salvar você."

        label p4_procura_menu:

            "Preciso pensar com calma. Onde vou procurar a [c] agora?"

            menu:
                "Procurar perto do bar":


                    $ p4_tempo += 1

                    "Ela foi pro bar quando tava triste àquela vez. Quem sabe..."

                    "..."

                    scene pub geral with Dissolve(1.0)

                    "Não estou vendo ela por aqui. E agora?"

                    menu:
                        "Andar pelo bar":


                            $ p4_tempo += 1

                            scene pub dois with Dissolve(1.0)

                            "..."

                            "Parece que ela não está aqui também."

                            if p4_miranda_bar:

                                jump p4_procura_menu
                            else:


                                $ p4_miranda_bar = True

                            "Mulher" "[mc]?"

                            mc desconfiado "Hã?"

                            scene pri4_img1 with dissolve

                            pause

                            a "Eu sou a assessora da [c]. Nós conversamos mais cedo."

                            mc desconfiado "O que tá fazendo aqui?"

                            a "Lembra que eu chamei você pra conversar? Eu estava aqui no bar."

                            a "Pelo que eu vejo, não teve sorte ainda procurando pela [c]."

                            mc desculpa "Pois é..."

                            a "O que acha de sentar comigo e a gente conversa enquanto a gente espera uma informação sobre ela?"

                            menu:
                                "Ok. Coisa rápida.":


                                    mc desculpa "Combinado, mas coisa rápida. Só enquanto a gente espera algo sobre a [c]."

                                    a "É só o que eu quero."

                                    a "Senta aqui do meu lado."

                                    mc normal "Ok."



                                    jump p4_miranda
                                "Não posso. Tenho que continuar procurando.":


                                    mc desculpa "Desculpa, mas tenho que continuar procurando."

                                    a "Fique à vontade. Se eu descobrir algo eu te aviso."

                                    mc normal "Ok. Obrigado."

                                    scene pub dois with Dissolve(1.0)

                                    jump p4_procura_menu
                        "Procurar em outro lugar":


                            jump p4_procura_menu
                "Procurar perto da praça":


                    $ p4_tempo += 1

                    "A praça é um lugar que fica vazio. Talvez ela esteja lá."

                    "..."

                    scene parque banco_noite with Dissolve(1.0)

                    "Que merda. Não estou vendo ela por aqui. E agora?"

                    menu:
                        "Andar pela praça":


                            $ p4_tempo += 1

                            "..."

                            scene parque noite with Dissolve(1.0)

                            "Que droga. Parece que ela não tá aqui também."

                            jump p4_procura_menu
                        "Procurar em outro lugar":


                            jump p4_procura_menu
                "Procurar perto do hotel":


                    $ p4_tempo += 1

                    "Talvez ela esteja só perto do hotel. Quem sabe ela não foi longe..."

                    "..."

                    scene cidade angulo_1_noite with Dissolve(1.0)

                    "Que merda. Não estou vendo ela por aqui. E agora?"

                    menu:
                        "Entrar no hotel":


                            $ p4_tempo += 1

                            "..."

                            scene hotel recepcao with Dissolve(1.0)

                            "Que droga. Parece que ela não tá aqui também."

                            jump p4_procura_menu
                        "Procurar em outro lugar":


                            jump p4_procura_menu
                "Procurar perto do Tadaima":


                    $ p4_tempo += 1

                    "A região do Tadaima é meio escura, porque o restaurante fica fechado essa hora. Quem sabe..."

                    "..."

                    scene cidade vista with Dissolve(1.0)

                    "Parece que ela não tá por aqui também..."

                    menu:
                        "Entrar no Tadaima":


                            $ p4_tempo += 1

                            "O Tadaima tá fechado essa hora, mas... Epa."

                            "Smartphone" "Trr... trr..."

                            $ renpy.vibrate(1)

                            mc desconfiado "Opa. Tem alguém me ligando."

                            mc "Alô?"

                            a "[mc]. Aqui é a [a]."

                            mc "Oi. Estou procuran..."

                            a "Eu sei. Queria te avisar que viram a [c] seguindo a rua que passa ao lado do restaurante japonês."

                            mc surpreso "Sério?! Eu tô aqui do lado!"

                            a "Perfeito. Vou deixar isso para você então. Boa sorte encontrando ela."

                            mc normal "Obrigado. Pode deixar comigo."

                            "..."

                            mc serio "Pode confiar em mim, [c]. Eu vou encontrar você."

                            jump priscila_e4_procura_final
                        "Procurar em outro lugar":


                            jump p4_procura_menu



















    label priscila_e4_agente:

        $ p4_tempo += 2

        "..."

        scene parque noite with Dissolve(1.0)

        "Toda essa situação tá muito estranha. Como que perderam ela de vista assim?"

        "Eu queria fazer alguma coisa, mas não adianta eu forçar a barra. Nem sei por onde começar a procurar."

        "Talvez essa [a] possa me ajudar de alguma forma. Porra. Ela é a agente da [c]. Ela tem que saber algo."

        "Não sei se essa mulher merece minha confiança. A [c] já falou algumas vezes dela, mas nunca senti que elas fossem amigas."

        "Talvez seja uma relação estritamente profissional."

        if p3_confissao:

            "Não consigo tirar uma coisa da cabeça..."

            "Aquele e-mail que eu li no bar a primeira vez que eu saí com ela."

            "Era um e-mail da [a] falando sobre um tal de acordo, ou eles fechariam com outra. Alguma coisa assim."

            "Depois de escutar a confissão da Pri eu não consigo parar de pensar que esse tal de acordo é justamente a relação dela com o [gus]."

            "Naquele e-mail, a [a] parecia achar tudo normal... mas se ela realmente tava falando disso que eu tô pensando..."

            mc preocupado "Como alguém pode achar isso normal?"

        "..."

        "Caraca, já cheguei no bar. Eu tô muito tenso."

        scene pub geral with Dissolve(1.0)

        "Pelo que eu entendi ela já está aqui..."

        "Mulher" "[mc]. Estou aqui. Senta aqui do meu lado."

        mc surpreso "!"

        scene pri4_img2 with dissolve

        pause

        a "O que foi?"

        menu:
            "Nada não...":


                mc envergonhado "Não é nada."

                a "Hum."

                "Que mulher linda. Não sei porque, mas achei que ela fosse uma velha feia."

                a "Eu não tenho paciência para pessoas que não são diretas."

                a "Se tem algo para falar, por favor diga."

                mc desculpa "Já disse que não é nada."

                a "Então..."
            "Não imaginei que você fosse bonita assim.":


                $ miranda_seducao += 1

                mc charmoso "Pra falar a verdade, espero que você não me leve a mal, mas eu não imaginei que você fosse bonita desse jeito."

                a "Obrigada. Você não é o primeiro a achar que a agente da modelo linda é a amiga feia."

                mc "De feia você não tem nada."

                a "E pelo que estou vendo, você não gosta de perder tempo."

                mc charmoso "..."

                a "Enfim..."
            "Eu esperava uma velha feia.":


                mc normal "Eu fiquei um pouco surpreso, só isso."

                a "Surpreso com o quê?"

                mc "Não sei por que, mas pensei que você fosse uma velha feia."

                a "Isso acontece com frequência. Não me incomoda."

                a "As pessoas acham que a agente da modelo é sempre velha e feia."

                a "Bom..."

        a "Desculpa chamar você assim de última hora. Mas a situação exige. Por favor, se sente."

        mc desculpa "Ok."

        scene pri4_img1 with dissolve

        pause

        label p4_miranda:

            mc preocupado "Fiquei muito preocupado com o que você me disse."

        a "Estamos todos preocupados. Ela desapareceu hoje mais cedo. Não responde minhas chamadas."

        mc desculpa "Talvez ela só precise de um tempo pra ela."

        a "O problema é que ela nunca fez isso. Mesmo com todo o stress, ela nunca deixou de responder uma mensagem minha."

        a "Eu cuido da [c] desde o início da carreira dela. Ela confia em mim, e nunca fez algo assim antes."

        a "Não tenho dúvidas de que estamos enfrentando uma situação como nunca antes aconteceu."

        mc "..."

        "A situação realmente parece séria. Será que eu devo avisar que a [c] me mandou uma mensagem?"

        "Eu não sei se essa mulher merece minha confiança..."

        menu:
            "Entendo... realmente é uma situação grave.":


                mc desculpa "Eu entendo... é uma situação terrível pelo que você tá me falando."

                a "Sim. Eu imaginei que talvez ela tivesse entrado em contato com você."

                mc "Infelizmente não."

                a "Entendo."
            "...":


                mc desculpa "..."

                a "Eu sei que a situação é complicada, mas faremos alguma coisa."

                a "Por um acaso ela não te escreveu ou te ligou..."

                mc preocupado "Não..."

                a "Certo."
            "Eu recebi uma mensagem da [c] hoje à tarde.":


                $ miranda_seducao += 1

                mc serio "Na verdade, talvez eu possa ajudar de alguma forma."

                a "Como?"

                mc serio "Ela me mandou esta mensagem hoje à tarde... dizendo adeus..."

                a "Posso ver?"

                mc "Claro."

                a "..."

                a "Entendo. Imaginei mesmo que ela pudesse te escrever. Obrigada por me mostrar."

                a "A mensagem não nos dá nenhuma dica de onde ela possa ter ido, mas obrigada mesmo assim."

        scene pri4_img3 with dissolve

        pause

        a "..."

        a "[mc]. Você tem visto a [c] com frequência, não é verdade?"

        mc normal "Sim. A gente tem se visto algumas vezes."

        a "Ela tem me falado bastante sobre você."

        if priscila_seducao_evento > 0:

            a "E não apenas como amigo. Eu sinto que o que ela sente por você é maior do que isso."

            a "Ela vê você como um homem."

        a "É inegável que os sentimentos que ela sente por você são bem fortes."

        a "Eu gostaria de saber se o sentimento é mútuo. Quais são seus planos com relação a ela?"

        mc desconfiado "Meus planos?"

        menu:
            "Eu quero um romance sério com ela.":


                mc serio "A [c] não é apenas uma amiga. E também não é só uma peguete."

                mc charmoso "Eu quero algo sério com ela. Quero que nossa relação vá além. Ela... ela é especial pra mim."

                a "Entendo..."

                if priscila_e3_beijo:

                    a "Eu não sei se tenho o direito de dizer isso, mas eu sinto que ela te vê da mesma forma."

                    a "Desde aquele encontro na praia, ela está diferente."
            "Ela é uma grande amiga.":


                mc normal "A [c] é uma grande amiga. Talvez minha melhor amiga."

                mc "Eu quero que ela seja feliz e quero passar bons momentos ao lado dela."

                a "Isso parece algo muito especial."

                mc desconfiado "Como assim, parece? Você não sente o mesmo sendo amiga dela?"

                a "Não dessa forma. Eu quero que a [c] se dê bem na vida profissional. Quero que ela realize todos os sonhos dela."

                a "É pra isso que eu sirvo. Eu sou aquela que vai transformar a [c] naquilo que ela nasceu para ser."

                a "Nada que impeça ela de se tornar a estrela que ela merece terá qualquer chance contra mim."

                mc normal "Você gosta muito dela também, do seu jeito."

                a "Acredito que sim."
            "Ela é só mais um caso. Nada sério.":


                $ miranda_pri_caso = True
                $ miranda_seducao += 2

                mc tarado "Ela é só mais um caso. A [c] é linda e mexe muito comigo, como mulher. Eu adoro ficar com ela."

                a "Entendo. Então é apenas um caso."

                mc charmoso "Sim. Como a gente poderia ter também."

                a "Você realmente não perde tempo."

                mc "Quando uma mulher incrível está falando com você, não existe meio termo."

                a "Você... é um homem confiante. Isso eu tenho que dizer."

                mc "Obrigado."

        a "Você me parece um rapaz honesto."

        if priscila_atencao > 0:

            if priscila_atencao == 1:

                a "Se bem que você entregou uma pauta sobre a [c] para seu chefe, não é mesmo?"

                a "Você revelou para ele sobre o filme. "

            elif priscila_atencao >= 2:

                a "Se bem que você entregou duas pautas sobre a [c] para seu chefe, não é mesmo?"

                a "Não bastou falar para ele sobre o filme, ainda tinha que descobrir que se trata do filme mais caro do país."

            mc surpreso "Mas! Como!?"

            a "Gostaria de saber como você descobriu... Melhor! Deixa eu advinhar, você fuçou no celular dela não é mesmo?"

            mc surpreso "..."

            a "Não precisa fazer essa cara. Você só fez seu trabalho de paparazzo. Não vou te criticar por fazer seu trabalho."

            mc desculpa "Mas como você sabe..."

            a "A matéria ainda não foi publicada, mas eu tenho fontes dentro da sua revista."

            a "Na verdade, eu tenho uma amiga que trabalha lá."
        else:


            $ miranda_seducao += 2

            a "O incrível é que você não entregou nenhuma pauta sobre ela para seu chefe."

            a "Eu imaginei que você não resistiria."

            mc serio "Só farei isso em último caso. Não quero prejudicar a vida dela dessa forma."

            a "Isso... é admirável. Colocar o bem dela acima do seu, é realmente admirável."

            mc envergonhado "..."

        a "Enfim. Agora não é hora de falarmos sobre isso."

        mc serio "Tem razão. Precisamos procurar a [c]."

        a "Sim. Mas não ainda. Eu tenho pessoas procurando por ela. Quando eles encontrarem alguma pista você também vai saber."

        mc desculpa "Ok. Mas eu estou preocupado com ela..."

        a "Ainda preciso te falar sobre algo muito importante."

        mc desconfiado "..."

        scene pri4_img4 with dissolve

        pause

        a "Na verdade, este é o motivo pelo qual eu te chamei aqui."

        if p3_confissao:

            a "Na praia... a [c] te contou uma coisa muito séria, não contou?"

            mc desculpa "Não... ela não..."

            a "Não precisa tentar negar. Era uma pergunta retórica. Eu sei que ela te contou."

            a "Eu não sei como você reagiu a tudo isso, mas pelo que me parece você não vai desistir dela por causa disso."

            mc serio "Claro que não."

            a "Esse é o problema."

            mc desconfiado "Como?"

            a "É melhor que você desista dela. O [gus] sabe sobre vocês dois. Ainda mais depois do showzinho na praia."

            a "Esse homem não está para brincadeira, [mc]. Ele consegue o que quer, de uma forma ou de outra."

            mc "Mas... por que você envolveu a [c] nisso?!"

            mc bravo "Se você sabe o que esse homem é, por que você insistiu para que a [c] aceitasse esse contrato absurdo!?"

            a "Essa não é a questão."

            menu:
                "Essa é a questão, sim! Olhe o que você fez com ela!":


                    mc bravo "Claro que essa é a questão! Essa é toda a questão!"

                    mc serio "A [c] está sofrendo muito por causa dessa situação. E foi você que convenceu ela! Você fez isso tudo parecer normal!"

                    a "Eu entendo que você esteja bravo comigo, [mc]. Mas você não sabe nada sobre mim e a [c]."

                    a "O que eu fiz foi o que qualquer agente interessada no sucesso de sua estrela faria."

                    a "A [c] não é a primeira a fazer parte desse jogo sujo. E pode ter certeza que não será a última."

                    a "E não ache você que isso está restrito ao mundo das modelos. Milhares de mulheres precisam se sujeitar no trabalho e até em casa."

                    a "Elas passam por todos os tipos de violência, na maioria das vezes em silêncio."

                    mc bravo "Isso não tá certo."

                    a "Saia desse mundo de conto de fadas e aprenda como a realidade funciona."

                    mc irritado "Eu não vou aceitar isso!"

                    a "Você é mais cabeça dura do que eu imaginava."
                "Tem razão. Não adianta chorar pelo que passou.":


                    $ miranda_seducao += 2

                    mc concentrando "Não quero falar sobre isso. Você tem razão. Temos que focar no que fazer a partir de agora."

                    a "Essa é a postura de um homem que sabe como a vida real funciona."

                    mc serio "Eu não acho isso normal. Eu não acho certo o que tá acontecendo. Nunca vou achar."

                    mc "Só não quero perder tempo chorando pelo leite derramado. Quero ajudar a [c] a partir de agora."

                    a "Entendo."

            a "Só que o [gus] é um adversário fora da sua liga. Você não vai ter chance em um embate direto contra ele."

            mc serio "Eu vou apostar tudo o que eu tenho. Vale a pena comprar essa briga."

            a "Não, [mc]. Você não está entendo sua situação. Ele sabe de vocês, e ele pode impedir o que vocês têm a hora que ele quiser."

            mc bravo "Ele não pode parar o que eu sinto pela [c]."

            a "Ele pode. E ele vai."

            "Essa forma que ela fala... Fico pensando se foi ele que me ligou aquele dia antes de eu levar a [c] na praia."

            "Talvez ele estivesse tentando me intimidar."

            mc concentrando "Olha, [a]. Eu agradeço sua preocupação. Mas, como disse, eu vou arriscar."

            mc normal "A [c] vale o esforço."

            a "Eu sei reconhecer um homem decidido. Só espero que tudo acabe bem para você."

            mc "Obrigado. Eu vou tomar cuidado."
        else:


            a "Na praia... a [c] te contou uma coisa muito séria, não contou?"

            mc desconfiado "Como?"

            a "Ela te disse sobre..."

            mc "Sobre o quê?"

            a "Você... realmente está sendo sincero?"

            mc desculpa "Eu sei que a [c] tá passando por alguma barra. Ela tava estranha na praia."

            mc "Mas eu não sei o que tá rolando. Ela disse que não queria estragar nossa relação com isso."

            a "Isso... isso é terrível, [mc]."

            mc preocupado "Como assim terrível?"

            a "Você... não sabe nada do que está acontecendo. Saber isso era sua única chance..."

            mc "Você tá começando a me assustar. O que eu preciso saber?"

            a "Eu não posso te falar, me desculpe. Mas ele deve saber que você não tem todas as peças."

            a "Ele não tem porque poupar você, [mc]. Eu não tenho nada com sua vida, mas, pela [c], eu vou fazer isso."

            mc triste "..."

            a "Você precisa esquecer a possibilidade de ter um romance com a [c]."

            a "Veja ela como uma irmã, sem nenhuma segunda intenção, e você TALVEZ ainda tenha uma chance."

            mc bravo "Não quero fechar uma porta com a [c] de forma alguma. Não depois do que a gente fez na praia."

            a "Não importa o que você quer ou o que ela quer. Não importa o que vocês fizeram."

            a "Só deixe pra lá. Você precisa me prometer que não vai tentar nada além de amizade com ela."

            mc preocupado "..."

            a "Vamos! Prometa!"

            "Como assim? Como que eu não sei o que está acontecendo? Que tipo de informação eu deveria ter?"

            "Essa mulher não parece estar brincando..."

            "Mas se eu aceitar eu vou ter que esquecer uma relação íntima com a [c] pra sempre?"

            menu:
                "{b}Eu prometo.{/b}":


                    $ p_amigo = True
                    $ miranda_seducao += 2

                    "Eu não tô gostando do tom dessa mulher. Mesmo sacrificando minha relação com a [c], tenho que fazer isso."

                    mc concentrando "Ok. Eu prometo."

                    a "Isso vai ser bom pra vocês."
                "{b}Não! Eu verei a [c] da forma que eu quiser.{/b}":








                    mc bravo "De forma alguma! Eu vou continuar vendo a [c] da jeito que eu quiser."

                    a "Não vou tentar mudar sua cabeça. Boa sorte."

                    mc "..."

        "Smartphone" "Pó póróró... Pó póróró póó..."

        a "Perdão, preciso atender."

        scene pub geral with Dissolve(1.0)

        "..."

        a "Certo..."

        a "Ok."

        a "Obrigada."

        scene pri4_img1 with dissolve

        a "Alguém viu a [c] andando perto do restaurante japonês Tadaima hoje mais cedo."

        mc serio "Era tudo que eu precisava saber, [a]. Vou atrás dela!"

        a "Perfeito. Vou deixar isso nas suas mãos."

        mc serio "Pode contar comigo. Eu vou revirar toda aquela região e só volto depois de encontrar ela."

        a "Tenho certeza que você vai conseguir. E obrigada por ter falado comigo esta noite."

        mc "Foi bom conhecer você. Eu sei que você é importante pra [c]."

        mc "Só que agora eu vou lá. Até."

        if miranda_seducao >= 4:

            scene pri4_img5 with dissolve

            a "[mc]."

            mc normal "Que foi?"

            a "Você é um homem interessante."

            a "Eu entendo o que a [c] viu em você."

            a "Espero que a gente possa se ver novamente, em uma oportunidade diferente."

            menu:
                "Eu adoraria.":


                    $ miranda_sexo = True

                    mc charmoso "Eu adoraria, [a]. Você é um tipo raro de mulher nesta cidade."

                    a "Vou levar isso como um elogio."

                    a "Não esqueça de me chamar para sair."

                    mc charmoso "Não vou de forma alguma."
                "Eu acho que não seria apropriado.":


                    mc desculpa "Me desculpe, mas eu acho que não seria apropriado."

                    a "Eu respeito um homem de convicções."

                    mc normal "Obrigado. Mas foi um prazer falar com você."

                    a "Igualmente."

            a "Agora vai. Boa sorte com a [c]."

            mc charmoso "Obrigado."

        $ miranda_conversou = True
        $ p4_tempo += 4

        jump priscila_e4_procura_final

    label priscila_e4_procura_final:

        scene black with dissolve

        "..."

        "Tenho que seguir por esta rua... agora vou reto..."

        "..."

        "Primeira vez que eu venho pra esta região."

        scene viaduto pichacao with Dissolve(3.0)

        "Essa parte da ilha é bem diferente do centro. Parece que a prefeitura não liga muito pra esta região..."

        "As paredes todas pichadas. Parece que falta luz... e ainda mais durante a noite..."

        mc preocupado "Tá me dando um cagaço..."

        "Só que eu não posso desistir agora. Preciso encontrar a [c] de qualquer jeito."

        "Então ela foi vista por aqui. Só que tem vários caminhos. Preciso decidir por onde eu começo procurando."

        label p4_menu_viaduto:

            "Tem um viaduto seguindo reto ou eu posso dobrar pra direita aqui... Parece que tem uma grande construção lá pra frente."

            menu:
                "Procurar perto do viaduto":


                    $ p4_tempo += 1

                    "Vou seguir pelo viaduto, não acho que ela iria por aquele outro caminho medonho..."

                    "..."

                    scene viaduto esquerda with Dissolve(2.0)

                    "Nada por aqui."

                    mc serio "Priscila!"

                    mc triste "Droga..."

                    menu:
                        "Continuar procurando o viaduto":


                            $ p4_tempo += 1

                            "..."

                            scene viaduto central with Dissolve(2.0)

                            "Não vejo ela por aqui também. Onde será que ela pode ter ido?"

                            "Será que vale a pena continuar insistindo neste caminho?"

                            menu:
                                "Olhar embaixo do viaduto":


                                    $ p4_tempo += 1

                                    "Agora que estou aqui não adianta voltar atrás."

                                    "Vou continuar por aqui."

                                    label p4_menu_viaduto_sob:

                                        "..."

                                    scene viaduto embaixo with Dissolve(2.0)

                                    mc serio "Priiiiii! É o [mc]!"

                                    "..."

                                    mc preocupado "Nada ainda..."

                                    "E agora?"

                                    menu:
                                        "Cruzar o viaduto e continuar o caminho.":


                                            $ p4_tempo += 1

                                            "Alguma coisa me diz que estou seguindo o caminho correto."

                                            mc zerado "Eu acho..."

                                            label p4_menu_lixao:

                                                "..."

                                            scene lixao conteiners with Dissolve(2.0)

                                            mc angustiado "Eca! O cheiro daqui é ainda pior."

                                            "Com certeza é algum tipo de lixão..."

                                            "Acho muito difícil ela ter se enfiado aqui. E agora?"

                                            menu:
                                                "Procurar pelo lugar":


                                                    $ p4_tempo += 1

                                                    "Vou dar uma andada rápida por aqui."

                                                    "..."

                                                    scene lixao entrada with Dissolve(2.0)

                                                    "Nunca imaginei que eu viria em um lugar como estes a esta hora da noite..."

                                                    "Tô começando a torcer pra ela não ter vindo parar aqui."

                                                    "..."

                                                    scene lixao esquerda_parede with Dissolve(2.0)

                                                    "Nada aqui também."

                                                    "E se ela não estiver mais viva?"

                                                    mc serio "Não!"

                                                    "Pare de pensar besteiras, [mc]..."

                                                    "???" "{i}suup... ick...{/i}"

                                                    mc angustiado "!"

                                                    "Que barulho foi esse?!"

                                                    "???" "{i}uuuhh... ick...{/i}"

                                                    "Acho que tem alguém chorando. Será que..."

                                                    mc surpreso "!"

                                                    jump priscila_e4_encontro
                                                "Voltar tudo e escolher outro caminho":


                                                    "Acho que não adianta continuar procurando por aqui."

                                                    "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                                    jump p4_menu_viaduto
                                        "Voltar tudo e escolher outro caminho":


                                            "Acho que não adianta continuar procurando por aqui."

                                            "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                            jump p4_menu_viaduto
                                "Procurar sobre o viaduto":


                                    $ p4_tempo += 1

                                    "Talvez ela esteja lá em cima. Dá menos medo que aqui embaixo pelo menos."

                                    "..."

                                    scene viaduto noite with Dissolve(2.0)

                                    mc serio "[c]!"

                                    "..."

                                    "Merda! Parece que ela não tá aqui também."

                                    menu:
                                        "Continuar andando sobre o viaduto":


                                            $ p4_tempo += 1

                                            "Já que eu tô aqui, melhor continuar por este caminho mesmo."

                                            "..."

                                            scene lixao gadget with Dissolve(2.0)

                                            if not gadgetbeta or not persistent.gadgetbeta:

                                                "Opa!"

                                                mc desconfiado "Parece que tem um negócio brilhando aqui..."

                                                $ persistent.gadgetbeta = True
                                                $ gadgetbeta = True

                                                play sound "extra/carta.mp3"

                                                show gadget_beta with dissolve

                                                "{b}[mc] encontrou Gadget Beta{/b}"

                                                "{b}Gadget Beta é um Item Especial. Itens especiais ficam com você mesmo que você reinicie o jogo.{/b}"

                                                "{b}Você só perde um Item Especial se você desinstalar o aplicativo e não salvar seu jogo na nuvem.{/b}"

                                                "{i}zzzzkkkk{/i}"

                                                "{i}tccchhhkkkk{/i}"

                                                mc desconfiado "Que que é isso?! Tá fazendo um barulho estranho..."

                                                if (persistent.gadgetbeta or gadgetbeta) and (persistent.gadgetalfa or gadgetalfa) and not gadget2cena:

                                                    call gadget2cena from _call_gadget2cena
                                                else:


                                                    "{i}Trying to connect to HQ...{/i}"

                                                    "{i}Missing TWO components{/i}"

                                                    "{i}Please locate Gadget Alfa and Gadget Gama before trying to connect.{/i}"

                                                    "{i}tccchhhkkkk{/i}"

                                                    mc surpreso "Uou! Esse negócio falou alguma coisa!"

                                                    mc desconfiado "Parece que eu preciso encontrar outros dois trecos antes de fazer alguma coisa..."

                                                    mc "Ele falou em outra língua... O que será que significa isso?"

                                                    mc concentrando "Melhor continuar..."

                                            if not gadgetbeta and persistent.gadgetbeta:

                                                $ gadgetbeta = True

                                                "{b}Você já encontrou o Gadget Beta jogando anteriormente.{/b}"

                                                "{b}Itens especiais ficam salvos mesmo que você reinicie o game, por isso não é preciso pegá-los novamente.{/b}"

                                            "..."

                                            "Vou continuar andando por este caminho..."

                                            mc serio "[c]!"

                                            "..."

                                            scene lixao acima with Dissolve(2.0)

                                            mc angustiado "Eca! O cheiro aqui é horrível!"

                                            "Sera que ela realmente viria pra cá? Esse lugar é um nojo."

                                            "Bom... Não tem mais nada aqui em cima. Ou eu desço aqui ou volto tudo. E agora?"

                                            menu:
                                                "Descer e procurar no lixão":


                                                    $ p4_tempo += 1

                                                    "Agora que eu tô aqui não adianta voltar tudo. Só volto com a [c]."

                                                    jump p4_menu_lixao
                                                "Voltar tudo e escolher outro caminho":


                                                    "Acho que não adianta continuar procurando por aqui."

                                                    "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                                    jump p4_menu_viaduto
                                        "Descer e olhar embaixo do viaduto":


                                            $ p4_tempo += 1

                                            "Melhor descer e olhar aqui embaixo também."

                                            "Se bem que acho que ela ouviria eu gritando..."

                                            jump p4_menu_viaduto_sob
                                        "Voltar tudo e escolher outro caminho":


                                            "Acho que não adianta continuar procurando por aqui."

                                            "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                            jump p4_menu_viaduto
                                "Voltar tudo e escolher outro caminho":



                                    "Acho que não adianta continuar procurando por aqui."

                                    "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                    jump p4_menu_viaduto
                        "Voltar tudo e escolher outro caminho":


                            "Acho que não adianta continuar procurando por aqui."

                            "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                            jump p4_menu_viaduto
                "Seguir o caminho da direita até a construção abandonada":


                    $ p4_tempo += 1

                    "Acho melhor eu seguir por este caminho da direita até aquela construção tenebrosa."

                    mc zerado "Essa não parece a melhor opção..."

                    "..."

                    scene black with Dissolve(1.0)

                    "Essa região é ainda pior que a de antes. Parece tudo abandonado..."

                    "Mas o que é estranho é que tem marcas de pneu... como se alguém tivesse passado por aqui de carro recentemente."

                    "..."

                    scene v_estacao entrada with Dissolve(3.0)

                    mc surpreso "Uou..."

                    "Olha pro tamanho deste lugar."

                    "Parece que é a antiga estação ferroviária."

                    "Pelo que eu sei, ela foi desativada vários anos atrás. Agora quem usa são tipo moradores de rua ou quem quer fugir da sociedade."

                    mc zerado "Por que eu tô falando igual um guia turístico?"

                    "Espero que a [c] não tenha se metido por aqui..."

                    "Tenho que decidir se vou continuar andando por aqui ou se é melhor voltar e pegar o caminho do viaduto."

                    menu:
                        "Subir as escadas da estação abandonada":


                            $ p4_tempo += 1

                            "Agora que eu tô aqui... Só espero que eu não acabe no meio de uma rodinha de traficantes."

                            "..."

                            scene v_estacao catraca with Dissolve(3.0)

                            "Olha só pra este lugar... O aço está todo corroído. Tá tudo caindo aos pedaços."

                            "Quem diria que uma ilha paradisíaca como essa ia ter um lugar como este."

                            "E agora?"

                            menu:
                                "Entrar na estação abandonada":


                                    $ p4_tempo += 1

                                    "Tudo pela [c]!"

                                    mc triste "Ai, carai..."

                                    "..."

                                    scene v_estacao area with Dissolve(3.0)

                                    play sound "audio/som_18_gotas.mp3"

                                    "A estação é bem grande. Mas realmente tá abandonada."

                                    "O som das gotas caindo. Esse teto tudo cheio de buraco, e tudo corroído."

                                    "É o cenário ideal pra filmar uma obra de terror."

                                    mc triste "Melhor parar de pensar isso que tô ficando com medo de verdade."

                                    "Que merda. A [c] não tá aqui também."

                                    label p4_estacao_menu:

                                        scene v_estacao area with Dissolve(1.0)

                                        "Existem vários caminhos possíveis a partir daqui. Pra onde eu vou?"

                                    menu:
                                        "Procurar na plataforma 11":


                                            $ p4_tempo += 1

                                            "Vou checar esta primeira plataforma."

                                            mc serio "[c]! Você tá aqui?!"

                                            "..."

                                            scene v_estacao plataforma11 with Dissolve(3.0)

                                            mc "[c]!"

                                            "Parece que ela não tá aqui também."

                                            "A ilha é governada pelo mesmo grupo de políticos há muitos anos. É como se fosse uma dinastia."

                                            "Eu já ouvi falarem que o prefeito só tem olhos pra região central da ilha, e agora olhando pra estes lugares..."

                                            "Parece que os críticos realmente têm razão. Por qual motivo eles abandonariam esta estação e construiríam outra?"

                                            "Bom... Ela não tá aqui. Melhor eu voltar."

                                            jump p4_estacao_menu
                                        "Procurar entre a plataforma 9 e 10":


                                            $ p4_tempo += 1

                                            "Tem outras duas plataformas mais pra lá. Quem sabe..."

                                            "..."

                                            scene v_estacao plataforma910 with Dissolve(3.0)

                                            "Nada aqui também... Onde a [c] se meteu?"

                                            "Eu posso continuar procurando pelas plataformas ou posso voltar."

                                            "E agora?"

                                            menu:
                                                "Procurar pelas plataformas 9 e 10":


                                                    "Não posso perder a paciência. Tenho que procurar em todos os lugares possíveis."

                                                    "..."

                                                    if not gadgetalfa or not persistent.gadgetalfa:

                                                        "Epa! O que é isso aqui no chão?"

                                                        scene v_estacao gadget with Dissolve(3.0)

                                                        mc desconfiado "Tem uma coisa brilhando aqui. Deixa ver."

                                                        "..."

                                                        $ persistent.gadgetalfa = True
                                                        $ gadgetalfa = True

                                                        play sound "extra/carta.mp3"

                                                        show gadget_alfa with dissolve

                                                        "{b}[mc] encontrou Gadget Alfa{/b}"

                                                        "{b}Gadget Alfa é um Item Especial. Itens especiais ficam com você mesmo que você reinicie o jogo.{/b}"

                                                        "{b}Você só perde um Item Especial se você desinstalar o aplicativo e não salvar seu jogo na nuvem.{/b}"

                                                        "{i}zzzzkkkk{/i}"

                                                        "{i}tccchhhkkkk{/i}"

                                                        mc desconfiado "Que barulho é esse?! Que coisa estranha..."

                                                        if (persistent.gadgetbeta or gadgetbeta) and (persistent.gadgetalfa or gadgetalfa) and not gadget2cena:

                                                            call gadget2cena from _call_gadget2cena_1
                                                        else:


                                                            "{i}Trying to connect to HQ...{/i}"

                                                            "{i}Missing TWO components{/i}"

                                                            "{i}Please locate Gadget Beta and Gadget Gama before trying to connect.{/i}"

                                                            "{i}tccchhhkkkk{/i}"

                                                            mc surpreso "Uou! Esse negócio falou alguma coisa!"

                                                            mc desconfiado "Parece que eu preciso encontrar outros dois trecos antes de fazer alguma coisa..."

                                                            mc "Ele falou em outra língua... O que será que significa isso?"

                                                            mc concentrando "Melhor continuar..."

                                                    if not gadgetalfa and persistent.gadgetalfa:

                                                        $ gadgetalfa = True

                                                        "{b}Você já encontrou o Gadget Alfa jogando anteriormente.{/b}"

                                                        "{b}Itens especiais ficam salvos mesmo que você reinicie o game, por isso não é preciso pegá-los novamente.{/b}"

                                                    "..."

                                                    "Não posso perder o foco. Eu tenho que encontrar a [c] de qualquer jeito."

                                                    "Certo. Não tem mais caminho pra cá. Vou ter que voltar pra área principal e seguir adiante."

                                                    jump p4_estacao_menu
                                                "Voltar para o centro da estação":


                                                    "Já perdi tempo demais nestas plataformas."

                                                    "Melhor continuar adiante."

                                                    jump p4_estacao_menu
                                        "Continuar adiante":


                                            $ p4_tempo += 1

                                            "Certo. Vou olhar ali pro outro lado agora."

                                            "..."

                                            scene v_estacao locomotivas with Dissolve(3.0)

                                            "Caraca. Olha pra essas locomotivas. O tempo corroeu tudo."

                                            "Estranho pensar como deixaram isso aqui cair aos pedaços dessa forma."

                                            "O que será que aconteceu? Talvez um dia eu devesse pesquisar mais sobre isso aqui."

                                            "..."

                                            scene v_estacao plataforma with Dissolve(3.0)

                                            "Canseira... cheguei na última plataforma. E nenhum sinal da [c] até agora."

                                            mc preocupado "Estou começando a ficar realmente preocupado com ela."

                                            "A estação chegou ao fim... mas eu consigo ver que os trilhos seguem até um viaduto beeeem lá na frente."

                                            "Eu posso voltar tudo até aquele outro viaduto, ou posso seguir os trilhos. Os caminhos são opostos."

                                            menu:
                                                "Seguir os trilhos pra fora da estação":


                                                    $ p4_tempo += 1

                                                    "Sempre pra frente que atrás vem gente. Não adianta voltar agora."

                                                    "..."

                                                    scene black with Dissolve(1.0)

                                                    "..."

                                                    "Mano... que caminhada..."

                                                    "Finalmente tô chegando."

                                                    scene lixao trilho with Dissolve(3.0)

                                                    "O trilho acaba aqui. Eita, que cheiro ruim. Tem uns conteiners ali, deixa eu dar uma olhada."

                                                    jump p4_menu_lixao
                                                "Voltar até o primeiro viaduto e recomeçar":


                                                    "Acho que não adianta continuar procurando por aqui."

                                                    "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                                    jump p4_menu_viaduto
                                        "Voltar tudo e escolher outro caminho":


                                            "Acho que não adianta continuar procurando por aqui."

                                            "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                            jump p4_menu_viaduto
                                "Voltar tudo e escolher outro caminho":


                                    "Acho que não adianta continuar procurando por aqui."

                                    "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                                    jump p4_menu_viaduto
                        "Voltar tudo e escolher outro caminho":


                            "Acho que não adianta continuar procurando por aqui."

                            "Talvez eu deva dar uma olhada naquele outro caminho que vai até a construção abandonada."

                            jump p4_menu_viaduto

    label priscila_e4_encontro:

        scene black with dissolve

        scene pri4_img6 with dissolve

        pause

        "Não consigo enxergar direito..."

        "Pera!"

        "É a [c]!"

        "O que eu faço agora?"

        menu:
            "Se aproximar dela o mais rápido possível":


                "Agora não é hora de ficar pensando. Tenho que ajudar ela o mais rápido possível."
            "Esperar e analisar a situação":


                $ p4_tempo += 1

                "Calma, [mc]!"

                "Essa situação é mais delicada do que você imagina. Ela tá num momento de muita dor pra ter acabado aqui desse jeito."

                "Eu preciso pensar muito bem como eu vou abordar as coisas com ela."

                if p3_confissao:

                    "Isso com certeza tem a ver com o que ela me confessou na praia. Ela pode estar arrependida de tudo."

                    "Eu preciso, antes de mais nada, mostrar que estou do lado dela. Que ela pode confiar em mim."
                else:


                    "Se eu soubesse melhor pelo que ela tá passando... Talvez eu pudesse falar alguma coisa."

                    "Mas lá na praia a gente acabou se pegando e eu fiquei sem saber o que tava rolando com ela."

                "O objetivo precisa ser tirar ela daqui. Nesse lugar não vai dar pra gente conversar direito."

                "Ok! Vamos lá."

        mc serio "[c]! É o [mc]!"

        c "[mc]..."

        c "É você mesmo?"

        mc preocupado "Sim. Sou eu... O que você tá fazendo aqui? Levanta."

        c "Não consigo, [mc]. Tô fraca demais."

        if p4_tempo <= 15:

            mc charmoso "Pode deixar que eu vou te ajudar."

            c "Ei!"

            mc "Opa!"

            scene pri4_img7 with dissolve

            pause

            mc "Pronto."

            mc "Lembra quando eu te carreguei no bar?"

            if p3_confissao:

                mc "Agora eu sei quem eram aquelas pessoas."

                mc "Eu peço desculpas por ter feito aquilo àquela noite."

                mc "Só que..."

            mc "Sempre que você precisar, eu vou carregar você. Às vezes a gente precisa da ajuda de alguém."

            c "É..."

            if p3_confissao:

                c "Na praia você disse a mesma coisa..."

                mc "Porque é o que eu penso de verdade. Eu quero que você confie em mim."

            c "Você sempre é tão incrível, [mc]. Às vezes eu acho que é tudo uma mentira..."

            c "Você chegou tão rápido. Eu... ninguém veio me procurar aqui ainda. Minha agente, os seguranças..."

            c "Você apareceu como um príncipe encantado."

            if not p3_escolha == "amigo":

                mc "Você merece, porque você é minha princesa."

                c "Ai, [mc]..."
            else:


                mc "Você é minha melhor amiga, [c]."

                mc "Eu sempre vou estar aqui pra você."

            c "Tudo bem... Pode me colocar no chão. Acho que nós podemos conversar, se for aqui."

            mc "Não tem problema, pode ser aqui mesmo."

            c "Tá..."
        else:


            scene lixao geral with Dissolve(1.0)

            mc preocupado "Eu sei que é complicado, Pri. Mas você precisa conseguir forças."

            c "Eu tô tão cansada, [mc]..."

            mc "Eu sei que você cansou, que você não quer mais pensar em nada."

            c "Isso..."

            mc "Mas não precisa pensar. Não precisa fazer nada. Só fala comigo."

            c "..."

            mc "Só vamos conversar. Pode ser aqui mesmo."

            c "Não precisamos sair daqui?"

            mc triste "Não. Vamos ficar aqui se você quiser."

            c "Tá... Eu vou levantar."

        scene black with dissolve

        scene pri4_img8 with dissolve

        c "Oi..."

        mc "Oi..."

        c "Desculpa fazer você vir até aqui."

        menu:
            "Não precisa pedir desculpas. Eu tô sempre do seu lado.":


                mc "Você nunca vai precisar pedir desculpas por uma coisa assim."

                mc "Eu sempre vou estar do seu lado."
            "Eu quero proteger você de tudo.":


                mc "Não fale isso, [c]. Eu quero proteger você de tudo. Você é minha companheira."

        if not p3_escolha == "amigo":

            mc "Depois do que aconteceu entre a gente na praia, nunca que eu poderia deixar você sumir assim da minha vida."

            mc "Você sabe o que eu sinto por você, não sabe?"
        else:


            mc "Eu te disse na praia que quero ser seu melhor amigo, não disse?"

        c "[mc]..."

        c "Eu..."

        c "Minha cabeça mudou completamente..."

        mc "Como assim?"

        c "Antes de eu conhecer você, eu tinha certeza do que eu queria."

        c "Mas depois que a gente começou a se ver e se aproximar, tudo começou a virar um inferno na minha cabeça."

        scene pri4_img9 with dissolve

        pause

        c "Eu tenho muita vergonha do que eu fiz, [mc]! Eu não consigo olhar pra você!"

        c "Minha cabeça dói todos os dias! E não consigo mais entender porque eu aceitei fazer o que eu fiz!"

        c "A [a] tenta me ajudar, mas nada do que ela diz faz sentido mais! Antes não era assim!"

        c "Por que isso tá acontecendo comigo, [mc]!?"

        c "É difícil demais! O remorso! O nojo! Eu só quero que isso tudo acabe! Quero que minha cabeça pare de pensar!"

        c "Não quero ter mais que lembrar! Quero que tudo fique escuro! Que tudo pare!"

        mc preocupado "[c]..."

        menu:
            "A saída não é acabar com tudo.":


                mc "Acabar com tudo não é a saída, [c]."

                mc "Mesmo quando tudo parece impossível, quando a gente sente que não tem mais nada pra fazer..."

                mc "Mesmo nessas horas a saída existe. É que a gente está tão envolvido em nossos problemas que a gente não consegue ver."

                mc "Não é porque você não consegue ver uma luz, que ela não existe. Ela tá lá!"
            "Se tudo ficar escuro, você não vai mais me ver.":


                mc "Se tudo acabar pra sempre, nunca mais você vai poder me ver. E nunca mais eu vou ver você, [c]."

                mc "Isso seria algo muito triste pra mim. Algo que eu não tô pronto pra ver acontecer."

                mc "Você é a pessoa mais importante que eu tenho agora e eu quero que você me escolha."

                mc "Entre o fim de tudo e eu, me escolha [c], por favor."

        c "Mas eu não consigo, [mc]... Todo dia eu sofro. Todo dia meu coração aperta mais."

        c "Eu sinto que de uma forma ou de outra eu vou morrer."

        mc preocupado "..."

        mc "Seu coração e sua cabeça são mais fortes do que você imagina."

        mc "Mesmo parecendo que tudo vai acabar, sempre é possível recomeçar. Sempre é possível reconstruir a nossa vida."

        c "Eu não sei, [mc]... Eu acho que eu não consigo."

        mc "Você consegue. Olhe pras pessoas do seu lado. Olhe pra mim, pra [a]. Nós gostamos de você, porque você é uma pessoa incrível."

        c "Mas eu só causo problemas pra você e pra [a]. Eu não mereço vocês..."

        mc "Deixe que a gente decida isso. Você não pode decidir pela gente se a gente vai te amar ou não."

        mc "Eu quero ficar com você agora. E não é você que tem que falar se é verdade ou não. Você entende?"

        c "Não sei... acho que você só tem dó de mim."

        mc "Nada disso. Eu gosto de você desde o dia que a gente se conheceu no bar, e desde aquele dia eu sabia que você não era perfeita."

        mc "Ninguém é perfeito, [c]. Todos nós erramos. E se a gente não tá bem, é nessas horas que a gente precisa de ajuda."

        mc "E eu quero ajudar você. E não faço isso por dó. Mas porque eu decidi que eu quero viver do seu lado."

        scene black with dissolve

        scene pri4_img10 with dissolve

        c "O que você tá falando me deixa feliz, [mc]... mas, mesmo assim... dói tanto..."

        mc "Isso não vai parar de uma hora pra outra. Por favor, confie em mim. A gente vai superar isso juntos."

        mc "Só dá mais uma chance. Uma chance pra gente resolver tudo."

        c "..."

        c "Quando você fala assim, você me dá tanta força, [mc]..."

        c "Eu não sei o que seria de mim se não fosse você."

        mc "É pra isso que eu tô aqui. E não se esqueça, mesmo sem mim, você é mais forte do que pensa."

        c "Hehe... Ok..."

        "Ufa. Que bom que ela sorriu. Acho que agora é a hora."

        mc "O que você acha da gente sair daqui? Tem um lugar que eu vi que vai ser excelente pra gente esquecer de tudo."

        c "Não sei se eu vou ser uma boa companhia agora..."

        menu:
            "Só de poder tá do seu lado é o suficiente pra mim.":


                mc "Só de tá do seu lado, é tudo o que eu preciso."

                c "Ai, [mc]..."

                c "Só você pra me deixar sem jeito até nessas horas..."

                mc "É que eu gosto da carinha que você faz quando tá com vergonha..."

                c "Tonto..."
            "Você sempre é uma excelente companhia!":


                mc "Impossível! Você é sempre uma companhia incrível!"

                c "Você me mima muito! Isso sim."

                mc "E não é bacana?"

                c "É sim... hehe..."

        mc "Vamos sair daqui então?"

        c "Tá..."

        scene black with dissolve

        scene pri4_img11 with dissolve

        c "[mc]..."

        mc normal "Oi?"

        c "Lembra que eu falei pra você não me trazer pra um encontro no lixão?"

        c "Eu que acabei te trazendo pra cá."

        mc desconfiado "Verdade..."

        mc zerado "Você podia ter esperado pelo menos até o quinto encontro, como a gente tinha combinado."

        c "Verdade... errei por pouco..."

        mc normal "Você vai querer voltar aqui então no próximo?"

        c "Me-melhor não!"

        mc feliz "Combinado!"

        c "Bobo..."

        scene black with dissolve

        "..."

        scene viaduto central with Dissolve(1.0)

        c "Eu passei por aqui..."

        mc "Eu pensei que sim. Mas ainda falta um pouquinho. Vem. Sobe aqui."

        c "Tá."

        scene viaduto noite with Dissolve(1.0)

        mc normal "Chegamos."

        c "Puxa! O céu tá tão bonito..."

        mc "Acho que vai amanhecer logo..."

        c "{i}Vrrrruuummmmm!{/i}"

        "?"

        scene black with dissolve

        scene pri4_img12 with dissolve

        mc envergonhado "Pri...?"

        c "Tá tão bonito, [mc]. Só você mesmo..."

        menu:
            "Você precisa de uma vista dessas depois do que aconteceu hoje.":


                mc normal "Nada como uma vista dessas pra reanimar o espírito!"

                c "Verdade!"
            "Você sabe que eu quero conquistar você.":


                mc charmoso "Você sabe que eu vou fazer de tudo pra conquistar você."

                if p3_escolha == "amigo":

                    c "Mas você disse que queria ser meu amigo na praiaa..."

                    mc charmoso "Estou repensando minha decisão..."

                    c "Ai, [mc]... Não faz isso com meu coração."
                else:


                    c "Você sabe como fazer eu me sentir especial."

                    mc "É porque você realmente é especial pra mim."

                    c "..."

        c "Esse lugar... sem nada sobre a nossa cabeça. Apenas o céu e as estrelas lá longe!"

        c "Parece que a gente pode voar!"

        c "{i}Vrrrruuummmmm!{/i}"

        mc envergonhado "De novo isso? O que tá rolando?"

        c "Não tá vendo?! Eu tô voando! {i}Vrrrruuummmmm!{/i}"

        mc "..."

        c "Aqui no céu nada pode chegar até mim! Eu vou pra onde eu quiser!"

        c "{i}Vrrrruuummmmm!{/i}"

        mc "Se você continuar correndo desse jeito vai desmaiar..."

        c "{i}puf{/i} Para de ser chato! {i}puf puf{/i}"

        mc normal "Olha aí. Já tá ofegante."

        c "Senhor Sabe-tudo..."

        c "Ufa! Deixa eu sentar. Vem aqui comigo."

        scene black with dissolve

        scene pri4_img14 with dissolve

        pause

        c "Opa."

        mc envergonhado "Ai... é bom sentar um pouco depois de tudo isso."

        c "Verdade. Mas eu nem sinto, sabe? Quando a gente tá junto, eu me sinto tão bem, [mc]."

        c "Mas depois a gente se separa e tudo volta a ficar horrível de novo."

        mc normal "Não pense nisso agora. Agora a gente tá juntos."

        if p3_confissao:

            c "Você tem razão. Mas é que eu quero aproveitar que eu tô com você pra poder tomar uma decisão."

            mc "Pode contar comigo."

            c "Você lembra o que eu te contei na praia, né?"

            mc preocupado "Sim..."

            c "É isso que tá me deixando desse jeito. Se eu quiser sair desse buraco, eu vou precisar fazer alguma coisa."

            c "Eu não quero mais ver o [gus] daquele jeito. Nunca mais."

            c "Mas se eu desistir agora, tudo o que eu passei vai ter sido pra nada. E isso eu não vou aguentar também."

            c "Todo o esforço da [a] também. Tudo o que ela fez pra conseguir esse contrato..."
        else:


            c "Mas é que eu quero aproveitar que eu tô com você pra poder tomar uma decisão."

            c "Desculpa se eu não tenho coragem de te contar tudo. Mas é que..."

            c "Eu achei que eu sabia o que eu queria pra minha vida e pra minha carreira."

        c "Só que desde que eu conheci você, eu não tô entendendo meus sentimentos."

        if priscila_e3_beijo:

            c "Depois do nosso beijo na praia..."

            c "E você disse que me vê assim... mais do que uma amiga..."

        elif priscila_e3_sexo:

            c "Depois do que a gente fez na praia..."

            c "Aquilo foi muito além de amizade."
        else:


            c "Você disse que eu era a pessoa mais importante pra você..."

            c "E eu te vi como um grande amigo. Talvez o único que eu tenho..."

        c "Eu fiquei tão feliz com isso. Mas, ao mesmo tempo, tudo o que eu fiz voltou à minha cabeça."

        mc preocupado "[c]..."

        c "Eu... preciso ter certeza... do que você... sente..."

        c "Desculpa... eu tô tão nervosa..."

        c "Se o que a gente... tá fazendo..."

        menu:
            "Deixar ela continuar falando":


                mc normal "..."

                c "Eu preciso saber... o que você planeja comigo... é o que eu acho que é."

                c "Ufa... fala alguma coisa que eu tô muito nervosa!"

                mc charmoso "Já falei que você fica muito linda nervosa, né?"

                c "Babaca..."

                mc "Olha..."
            "Abraçar ela":


                mc "Vem aqui..."

                c "Opa!"

                scene black with dissolve

                scene priscila viaduto_declaracao with dissolve

                pause

                c "A-a-a... [mc]..."

                mc "Olha. Eu entendi o que você quer saber."

                mc "Você quer saber os meus verdadeiros sentimentos pra com você, não é?"

                c "Sim..."

        mc "Eu não tenho medo de falar pra você o que eu sinto, [c]."

        mc "Tenho certeza dos meus sentimentos."

        c "..."

        "É aqui que eu vou definir tudo. Preciso pensar muito bem antes de dar esta resposta."

        "O que eu falar agora para a [c] vai moldar tudo a partir de hoje. Não só com ela, mas com outras garotas também."

        if priscila_e3_beijo:

            "Na praia eu beijei ela. Eu disse aquele dia que sentia algo mais do que amizade."

            "Mas será que eu continuo vendo ela como uma companheira real mesmo depois de tudo?"

            "Pelo que eu entendi, ela vai continuar vendo o [gus]. Que tipo de relação será essa?"

            "O que eu sinto por ela vai superar isso?"

        elif priscila_e3_sexo:

            "Na praia a gente foi muito além da amizade. A gente se pegou de verdade e eu realmente dei prazer a ela."

            "Mas eu sei que tem alguma coisa acontecendo, só não sei exatamente o que."

            "Será que eu quero entrar nesse rolo todo?"
        else:


            "Eu decidi na praia que eu queria apenas amizade com ela."

            "Mas será que eu continuo achando a mesma coisa? Assim como ela, não tenho certeza do que eu sinto."

        if sayuri_e3 == "beijo":

            "Eu beijei a [s]... O que será que ela vai pensar se eu ficar com a [c]?"

        if p_amigo:

            "Eu também prometi pra [a] que não iria me envolver de outra forma com ela."

            "Será que eu quebro minha promessa?"

        "Seja como for, preciso ser decisivo na minha escolha. Eu preciso ser firme pela [c]. É o mínimo que eu posso fazer."

        c "..."

        "Ok. É hora de decidir."

        mc "Não quero que você continue nessa incerteza."

        label priscila_e4_escolha:

            mc "O que eu quero..."

        menu:
            "Eu quero namorar você.":


                "Esta é uma decisão que eu nunca poderei voltar atrás sem prejudicar minha relação com a [c]."

                "Eu estou certo disso?"

                menu:
                    "Sim. Quero namorar com ela.":


                        jump priscila_e4_namoro
                    "Não. Preciso pensar melhor.":


                        "Melhor eu pensar mais um pouco..."

                        jump priscila_e4_escolha
            "Eu gosto de você, mas como amiga.":


                "Se eu escolher não namorar com ela, provavelmente eu nunca mais vou poder mudar isso."

                "Eu estou certo disso?"

                menu:
                    "Sim. Quero apenas amizade com ela.":


                        jump priscila_e4_amizade
                    "Não. Preciso pensar melhor.":


                        "Melhor eu pensar mais um pouco..."

                        jump priscila_e4_escolha

    label priscila_e4_amizade:

        $ persistent.priscila_cena8 = True

        scene priscila viaduto_declaracao with Dissolve(2.0)

        mc "Eu pensei muito sobre a gente, e cheguei a conclusão que você é uma pessoa especial pra mim, mas não como uma namorada."

        mc "Eu quero que você seja feliz, eu quero te ver sempre pra cima, e que você tenha sucesso em tudo o que você tentar."

        mc "E quero estar do seu lado pra te ajudar e colher os frutos com você."

        if priscila_seducao_evento > 0:

            mc "Em alguns encontros passados até rolou uma coisa outra entre a gente."

        if priscila_e3_beijo:

            mc "E rolou o beijo na praia. Foi incrível."

            mc "Aquilo me deixou muito confuso. Eu comecei a duvidar do que eu realmente sentia."

            mc "Mas hoje eu vejo melhor as coisas..."

        elif priscila_e3_sexo:

            mc "Teve nosso lance na praia. Foi algo incrível. Super excitante. Eu gostei muito."

            mc "Aquilo me deixou muito confuso. Eu comecei a duvidar do que eu realmente sentia."

            mc "Mas hoje eu vejo melhor as coisas..."

        mc "Eu quero ser seu amigo. É isso que eu sinto."

        c "[mc]..."

        c "Você... me segurando assim e falando desse jeito, eu me sinto tão segura."

        c "Como se fosse meu irmão mais velho. Que vai me proteger de tudo."

        mc "Eu quero te proteger de tudo mesmo."

        c "Obrigada, por tudo o que você fez por mim."

        c "Você foi me procurar no lixão, e não saiu de lá enquanto eu não saí com você."

        c "Eu acho que você é o cara mais legal que eu já vi na vida."

        c "Nunca eu imaginei que você estaria ao meu lado até agora."

        mc "Claro que eu estou."

        c "É que eu sou uma garota tão complicada. E todo esse lance do cinema..."

        c "Senta comigo?"

        mc "Claro."

        scene black with dissolve

        scene pri4_img13 with dissolve

        c "Às vezes eu fico pensando porque eu decidi participar desse filme. Eu já sou famosa."

        c "Mas é que nem sempre a gente tem controle sobre tudo. Às vezes as coisas vão aparecendo na nossa frente."

        c "E ainda por cima tem outras pessoas falando o que você deve e não deve fazer."

        c "É tudo tão sufocante. Eu me sinto presa."

        c "Mas quando a gente sai juntos, parece que a gaiola abre e eu consigo olhar tudo em volta."

        c "Eu penso com mais clareza, e parece que a carreira nem é tão importante assim porque existem outras coisas."

        mc normal "..."

        c "Tem hora que a gente fica bitolado nas coisas e não enxerga o que tem em volta."

        mc normal "Isso é verdade."

        c "E eu fico feliz, agora depois do que você disse, de finalmente a gente ter acertado nossa relação."

        mc preocupado "No fundo eu não sei se você sente o mesmo..."

        c "Eu não tenho tanta certeza sobre os meus sentimentos igual você."

        c "Mas pensando agora, talvez o que eu precise no momento não é um namorado, e sim alguém que esteja ao meu lado."

        c "Não romanticamente, mas que me ajude a tomar as melhores decisões porque realmente me quer ver feliz."

        c "Eu sinto que tem tudo pra gente continuar se vendo e passando um tempo legal juntos."

        mc normal "Eu acho a mesma coisa. Tem muita coisa pra gente passar juntos ainda."

        $ renpy.end_replay()

        c "Inclusive, a gente podia..."

        jump priscila_e4_final

    label priscila_e4_namoro:

        $ persistent.priscila_cena9 = True

        $ priscila_namoro = True

        if priscila_e3_beijo or priscila_e3_sexo:

            mc "Eu acho que desde nosso encontro na praia ficou bem claro o que eu quero."

            mc "Eu não menti quando eu disse que você mexeu comigo de uma forma diferente."

            mc "Eu não pretendo voltar atrás por conta do que aconteceu com você."
        else:


            mc "Eu sei que eu disse que te via como amiga, mas meu coração mudou."

            mc "Você ocupa um espaço diferente agora."

        mc "Eu quero que você seja minha, [c]."

        mc "Só minha."

        c "..."

        c "[mc]..."

        c "Eu quero ser sua também. Só sua."

        c "Por favor, me beija."

        scene priscila viaduto_beijo with Dissolve(3.0)

        pause

        "..."

        c "Hmm..."

        "Quando eu beijo a [c] meu coração bate tão rápido. Eu tenho certeza que fiz a escolha certa."

        "É com ela que eu quero ficar. Eu vou proteger ela de tudo, não importa o que aconteça."

        "..."

        scene priscila viaduto_declaracao with Dissolve(1.0)

        c "Ai, [mc]... Tudo o que eu queria era beijar você."

        c "Quando a gente tá junto eu esqueço de tudo. Eu fico tão nervosa, que minha cabeça fica branca."

        mc "Eu sinto a mesma coisa."

        c "É?!"

        mc "Sim."

        c "Isso me deixa muito feliz."

        c "Eu quero que a gente possa continuar se vendo."

        mc "Com certeza a gente vai. Eu vou fazer de tudo pra te ajudar, [c]."

        c "Obrigada, de verdade."

        c "Aliás..."

        c "Acho que eu não quero só parar no beijo hoje..."

        mc "Uou..."

        c "Você não quer?"

        menu:
            "Acho que por hoje está bom.":


                mc "Acho que esse beijo foi muito mais do que eu aguentava por hoje."

                c "Eu beijo tão bem assim?"

                c "Não achei que você fosse recusar, mas eu entendo."
            "Claro que eu quero. Estou louco pra ter você.":


                mc "Tá louca? O que eu mais quero é poder ter você."

                c "Então hoje você vai realizar seu sonho."

                c "Vem! Me pega!"

                scene pri4_img15 with dissolve

                pause

                c "Hmm... era isso que eu queria, [mc]."

                c "Eu quero sentir você cada vez mais em mim!"

                label pri4_priscila_premium:

                    pass

                "Como a Pri é gostosa. Será que eu paro aqui?"

                menu:
                    "Tirar a alça":


























                        "Claro que não. Eu quero ir até o fim hoje."

                        scene black with dissolve

                        scene pri4_img16 with dissolve

                        pause

                        c "[mc]... hmm..."

                        c "O que você tá fazendo?"

                        mc "Deixa que eu comando."

                        c "Ah... tá..."

                        menu:
                            "Massagear os peitos dela":


                                "Ela tá no clima. Ela vai gostar."

                                scene black with dissolve

                                scene pri4_img17 with dissolve

                                pause

                                c "Ahhnnn... você gosta deles?"

                                mc "Eles são maravilhosos. Eles são gigantes e incríveis."

                                c "Que bom que você gosta... sua mão também é macia. É gostoso..."

                                c "E você me beijando assim... eu tô pegando fogo, [mc]."

                                "Ela tá na minha. E agora?"

                                menu:
                                    "Apertar eles com força":


                                        "Ela vai curtir um pouco de força."

                                        scene pri4_img18 with dissolve

                                        pause

                                        c "Ai, [mc]! Você tá com tanta vontade assim?"

                                        mc "É culpa sua, por ser deliciosa desse jeito."

                                        c "Ai... seu grosso..."

                                        "Eu sabia. Ela tá louca de tesão agora. Ela vai aceitar o que eu quiser."

                                        window hide

                                        pause

                                        "Agora é hora de eu mostrar o lugar dela."

                                        menu:
                                            "Dar um apertão com tudo":


                                                "Agora toma essa!"

                                                $ renpy.block_rollback()

                                                scene pri4_img19 with vpunch

                                                pause

                                                mc "Hmm!"

                                                c "Aii! [mc]! Para! Você tá me machucando!"

                                                mc "D-desculpa!"

                                                "Acho que eu entrei nessa demais... exagerei..."

                                                c "Eu sei que eu sou gostosa, mas cuidado, eles são sensíveis."

                                                mc "Foi mal..."

                                                c "Faça sempre com carinho e eles vão se apaixonar por você."

                                                mc "Hmm..."

                                                mc "Toma o carinho aqui."
                                            "Sem exagerar...":




                                                "Não tem porque exagerar."

                                                c "Hmmm... você é bom com as mãos..."

                                                window hide

                                                pause

                                                c "Agora e-"

                                                c "E se agora você deixar eu massagear uma coisa sua..."

                                                mc "Eu acho que seria justo..."

                                                c "Mas eu não quero uma coisa macia... eu quero ele bem duro pra mim..."

                                                mc "Ele já tá pronto pra você..."

                                        mc "Sente ele gostoso."

                                        scene black with dissolve

                                        scene ani13 with Dissolve(1.0)

                                        pause

                                        c "Awnn... [mc]..."

                                        c "Ele tá tão duro apertando minha bunda."

                                        mc "Tá sentindo minha rola roçando aí trás, tá?"

                                        c "T-tô... adoro te ver com tesão por mim assim."

                                        mc "Você é uma delícia, Pri!"

                                        c "Sou, né?! Você gosta dessa delícia?! Gostar de roçar nela?"

                                        mc "Adoro! Adoro passar meu pau nela!"

                                        c "Annnn... então passa! Faz o que quiser com a bunda da sua princisa, safado."

                                        mc "Nghhh!"

                                        "Por que essa garota é tão gostosa?!"

                                        "Acho que eu me mataria pra comer essa puta!"

                                        c "Ahhn! Chega! Vamos tirar! Eu quero mais hoje! Quero trepar de verdade pela primeira vez!"

                                        menu:
                                            "Quer? Eu também! Vou deflorar você por completo!":


                                                pass

                                        c "Isso!"

                                        c "Deixa eu abaixar sua cal-"
                                    "Isso não vai dar certo":


                                        "Não tem porque exagerar."

                                        window hide

                                        pause

                                        c "Hmm... adorei..."

                                        mc "Que bom."

                                        c "Agora e-"
                            "Parar por aqui":


                                "As coisas tão boas assim. Ela tá curtindo, não tenho porque forçar as coisas."

                                window hide

                                pause

                                c "Agora e-"
                    "Continuar beijando":


                        "As coisas tão boas assim. Ela tá curtindo, não tenho porque forçar as coisas."

                        window hide

                        pause

                        c "Agora e-"



        $ renpy.end_replay()

        jump priscila_e4_final

    label priscila_e4_final:

        "Smartphone" "{i}Talá... lalalá... lalalá...{/i}"

        c "Ops..."

        scene viaduto noite with Dissolve(1.0)

        c "É a [a]... O que eu faço?"

        mc desculpa "Não adianta fugir pra sempre, né?"

        c "Acho que você tem razão. Vou falar com ela."

        scene black with dissolve

        scene pri4_img20 with dissolve

        pause

        c "Alô? [a]?"

        c "..."

        c "Eu sei, eu sei... Desculpa..."

        c "..."

        c "Eu tô bem. Não precisa ficar preocupada."

        c "..."

        c "Sim. Tô com ele."

        c "Quê?"

        c "Por que ele?"

        c "..."

        c "Ok... Estamos no viaduto da..."

        c "Ah... então tá."

        c "Tchau."

        c "Estão vindo me buscar."

        mc preocupado "... Eu sei que você tá meio assim, mas acho que é o melhor."

        scene pri4_img13 with dissolve

        c "Tudo bem. Eu não tô nem aí pra isso."

        mc desconfiado "Como é?"

        c "Você... fez esse ser o melhor dia da minha vida, [mc]."

        if priscila_namoro:

            c "Eu nem acredito que a gente..."

            mc charmoso "Tá namorando?"

            mc "Agora a gente tá juntos. E pode contar comigo pra tudo."

            c "Você vai me proteger?"

            mc "Com certeza."

            c "Obrigada..."
        else:


            c "Agora você é oficialmente meu melhor amigo."

            c "E com meus sentimentos definidos, eu sinto que eu sei o que eu tenho que fazer a partir de agora."

            c "Você renovou minhas certezas."

            mc normal "Eu fico muito feliz e pode sempre contar comigo."

            c "Eu vou contar."

        mc "Vamos descer?"

        c "Vamos."

        scene black with dissolve

        scene viaduto embaixo with Dissolve(1.0)

        c "Ele deve tá chegando."

        mc "Quem vem te pegar?"

        c "O [mar]..."

        mc serio "Por que ele?"

        scene pri4_img21 with dissolve

        c "Não sei. A [a] que combinou tudo..."

        menu:
            "Tome cuidado com eles, [c].":


                mc preocupado "Tome cuidado com essas pessoas, [c]. Elas não te fazem bem."

                c "..."
            "Não gosto nem um pouco desse cara.":


                mc serio "Não vou com a cara dele. Esse idiota pau mandado do [gus]."

                c "..."

        c "Eu sei. Eu já te falei... não quero mais continuar com isso. Eu vou dar um jeito de resolver tudo."

        if priscila_namoro:

            mc charmoso "Agora a gente tá juntos. Pode contar comigo pra tudo. Eu vou ser seu parceiro."

            c "Tá... Tudo isso ainda é tão novo pra mim."

            c "Você... é meu..."

        "{i}vruvruvrummm{/i}"

        scene black with dissolve

        scene viaduto carro with dissolve

        pause

        c "Acho que é ele..."

        mc "Eu não sei se eu gosto desse cara, [c]."

        c "Eu não sei qual é a dele... mas ele nunca fez nada errado comigo."

        mc "Sei..."

        scene black with dissolve

        scene pri4_img22 with dissolve

        mar "Olá."

        c "Oi, [mar]. O [gus] te mandou?"

        mar "Na verdade foi a [a]. O Sr. [gus] não tá sabendo de nada ainda."

        mar "Mas não vamos conversar aqui. Entre no carro e feche a porta. Eu vou trocar uma palavra com o nosso amigo."

        c "Como assim?! O que você tem pra falar com ele?"

        mar "Não interessa. Não é assunto que lhe diz respeito. Entre no carro. E feche a porta."

        scene black with dissolve

        scene pri4_img23 with dissolve

        pause

        c "Droga, [mar]..."

        mar "Não quero ouvir reclamações. Você sabe disso."

        c "Ok... Até depois, [mc]. Beijo."

        mc preocupado "Até, [c]."

        "O que esse cara quer comigo? Não tô gostando nada disso."

        scene pri4_img22 with dissolve

        mar "É impossível ver ou ouvir algo de dentro do carro. Não se preocupe que ela não vai saber de nada."

        mc serio "Saber do quê?"

        mar "Por favor, não me leve à mal, [mc]. Nós fomos bem claros com você."

        mar "Nós te avisamos que a coisa não acabaria bem se você continuasse vendo a [c]."

        if not p3_confissao:

            mar "Até a [a] tentou te alertar disso."

        mar "Mas você não quis ouvir."

        scene pri4_img24 with hpunch

        pause

        mar "Isso acaba aqui."

        mc surpreso "Quê?!"

        mc angustiado "Você tá doido?! Me assassinar por causa disso?!"

        mar "Eu só estou cumprindo ordens."

        mc "Não! Isso não é possível! Eu vou gritar!"

        mar "Pode fazer o que quiser. Ninguém pode te ouvir aqui. Você e a [c] deixaram tudo mais fácil pra mim."

        mc irritado "Filho da puta!"

        mar "Já disse que não é pessoal. Peço desculpas, mas são ordens."

        mc bravo "Maldito..."

        "Eu preciso fazer alguma coisa ou ele vai me matar aqui e agora."

        "Tenho que pensar em tudo o que eu sei. Tem que ter uma forma de impedir que ele me mate..."

        menu:

            "Se você me matar, todos saberão que o [gus] estupra a [c]." if p3_confissao:

                label priscila_e4_finalvence:

                    $ persistent.priscila_cena11 = True

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("p4_fim_namoro","priscila","personagem")

                $ gustav_derrotado = True

                mc serio "Se você apertar esse gatilho, a carreira do seu chefe vai pro saco, [mar]."

                mc "Eu sei o que ele faz com a [c]. E eu deixei uma matéria sobre isso escrita na redação, pronta pra publicarem."

                mar "Como é?"

                mc charmoso "Vocês acharam que eu seria um alvo fácil, mas suas ameaças me deram dicas demais. Eu pude me defender."

                mar "Então a [c] realmente contou tudo pra você?"

                mc "Sim. No dia da praia, ela revelou tudo pelo que tava passando. Foi fácil ligar os pontos. As ligações..."

                mc "Vocês inclusive me deram a chance de gravar uma conversa entre eles."

                mc tarado "Meu chefe vai adorar acabar com a carreira do [gus] publicando a matéria sobre ele, ainda mais agora com esse filme."

                scene pri4_img22 with dissolve

                mar "Eu acho que você está blefando, mas não sou eu que tenho que tomar esse tipo de decisão."

                mar "Você vai viver mais um dia, [mc]."

                mar "Mas enquanto você estiver com os olhos na [c], o [gus] não vai te deixar em paz."

                mc bravo "Eu sei."

                mar "Essa garota vale tudo isso?"

                mc "Vale. E você não tá em condições de me ameaçar. Eu tenho o [gus] nas minhas mãos agora. Eu posso foder a vida dele."

                mar "O que você quer dizer com isso?"

                mc charmoso "Eu quero que você diga pra ele me ligar amanhã. Nós sabemos que ele tem meu número."

                mc "Tenho algo muito sério pra tratar com ele. E ele não vai gostar nem um pouco."

                mar "Você tem certeza que você vai cutucar a onça com a vara curta, [mc]?"

                mar "O [gus] é só uma das peça de uma máquina muito maior."

                mar "Você não sabe nada, [mcc]."

                mc serio "Não interessa. Tô pouco me lixando pra essa 'máquina'. Podem ir todos pro inferno junto com o [gus]."

                mar "Você tem fibra, [mc]. Talvez a gente possa usar isso em algum momento."

                $ renpy.end_replay()

                mar "Mas agora eu tenho que sair, antes que a [c] desconfie de alguma coisa."

                scene black with dissolve

            "Você não precisa me matar. Eu resolvi não ter algo com ela." if not priscila_namoro:

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("p4_fim_amizade","priscila","personagem")

                mc desculpa "Não tem porque continuar com tudo isso..."

                mar "Como?"

                mc "Eu resolvi não ter nada com a [c]. Seu chefe não precisa mais ter ciúmes de mim. Pode continuar a vida tosca dele."

                mar "Você está falando sério?"

                mc serio "Sim. Eu falei pra ela que seremos no máximo amigos. Não tá contente?"

                scene pri4_img22 with dissolve

                mar "Você tomou uma ótima decisão."

                mar "[mc], agora que você não é mais um inimigo do [gus], talvez possa se tornar nosso aliado."

                menu:
                    "Não quero nada com vocês.":


                        mc bravo "Tá louco? Não quero nada com vocês. Aliado é o caralho."

                        mar "Não precisa tomar uma decisão sobre isso agora."

                        mc "Já falei que não quero nada com vocês."
                    "Aliado? Como assim?":


                        mc desconfiado "Aliado?"

                        mar "Sim. Sempre precisamos de novas pessoas, e você se mostrou um cara astuto e agora não é mais um inimigo."

                        mc desculpa "Não sei, não quero falar sobre isso agora."

                        mar "Não apresse as coisas. Vamos falar sobre isso no futuro."

                mar "Mas agora eu tenho que sair, antes que a [c] desconfie de alguma coisa."

                scene black with dissolve
            "Não consigo pensar em nada. Tenho que revidar!":


                label priscila_e4_finalmorte:

                    $ persistent.priscila_cena10 = True

                mc irritado "Eu não vou deixar você me levar fácil desse jeito!"

                mar "Não adianta resistir, [mc]."

                $ renpy.block_rollback()

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("priscila_e4_morreu","priscila","personagem")

                $ persistent.mc_morreu = True

                mc "Isso que a gente vai ver seu filho de um-"

                play sound "audio/som_17_tiro.mp3"

                scene black

                "{i}BANG{/i}"

                "..."

                c "Que barulho foi esse..."

                c "Nã-"

                c "NÃÃÃÃÃÃÃOOOOOOOOOOOO!"

                c "O QUE VOCÊ FEZ, SEU MONSTRO?!"

                mar "Entra logo no carro."

                c "ME SOLTA! NÃO! SEU ANIMAL! SEU CORNO!"

                c "VOCÊ MATOU ELE! NÃÃããooo..."

                scene mc morto with Dissolve(3.0)

                $ renpy.pause(delay=5, hard=True)

                scene black with Dissolve(5.0)

                show pixie b_preocupada with Dissolve(1.0)

                p "Parece que a história do [mc] chegou ao fim."

                p "É uma pena. Eu tinha muitas expectativas para o futuro dele. Tantas coisas para sentir e fazer."

                p "Mas parece que as decisões que {b}você{/b} tomou levaram a esse fim prematuro."

                p "Sim. Você é o único culpado pelo [mc] ter acabado dessa forma. Lembra que você concordou que é o único responsável pelas suas escolhas?"

                p "Sem o [mc], eu tenho um lugar a menos para eu me alojar. Terei que encontrar outro hospedeiro agora."

                p "Mas o espírito do tempo liga todas as mentes. Não é difícil encontrar outro que possa fazer o que ele não conseguiu."

                show pixie b_provocando with dissolve

                p "..."

                p "Ainda está aqui?"

                p "Não tem nada mais que você possa fazer."

                $ renpy.block_rollback()

                p "Não. Você não pode usar o botão {b}Voltar{/b}."

                p "Mas eu sempre vou deixar você carregar o seu jogo. Se você tentar novamente, é trabalho a menos para mim."

                p "Eu realmente gosto do [mc]. Não queria que ele acabasse assim."

                p "Mas aí é com você."

                p "O que eu posso te dizer pra te ajudar? Na verdade eu tenho uma dica, sim."

                p "Volte no encontro da praia com a [c] e não pense só em sexo. Escute o que ela tem a te dizer."

                p "Ela vai te contar um segredo que vai salvar a vida do [mc]."

                p "Eu sou ou não sou a fada mais foda, do mundo?"

                $ renpy.end_replay()

                p "Adeus."

                hide pixie with Dissolve(1.0)

                $ renpy.full_restart()

        "Minhas pernas... Eu vou desmaiar..."

        "..."



        scene pri4_img23 with dissolve

        c "Eu só quero dar um tchau pra ele..."

        c "Tchau, [mc]. Quero te ver de novo logo."

        mc preocupado "Eu vou te ligar! Pode deixar."

        c "Tá. Beijo."

        mc "Beijos..."

        "Ela parece tão triste... Eu espero que nada de ruim aconteça com ela agora..."

        scene viaduto noite with Dissolve(1.0)

        "{i}vruvruvrummm{/i}"

        "O desgraçado do [mar] levou ela."

        "..."

        "A [c] tá em pedaços. Mas parece que eu consegui melhorar um pouco como ela se sente."

        if priscila_namoro:

            "Agora a gente tá namorando."

            mc feliz "Estou tão feliz."

            "Como isso vai influenciar em tudo o que tá acontecendo comigo nos últimos tempos?"

            "Ela tá confiando demais em mim. Não sei o que vai acontecer se eu quebrar a confiança dela."

            mc preocupado "Não quero nem pensar nisso..."

            "Por outro lado, eu tô muito animado pra saber como tudo entre a gente vai ser a partir de hoje."

            "Eu sei que tem o idiota do [gus], mas a gente vai poder sair juntos e tudo o mais."

            mc feliz "Tô muito ansioso pro que vai acontecer agora!"

        "Ufa..."

        scene black with dissolve

        "Eu tô exausto."

        $ v10_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v10_fim","priscila","personagem")

        $ tempo = 4

        jump call_cidade



label priscila_evento5:

    $ priscila_cel_msg6_r = "iniciado"

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p5_save", extra_info="p5_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "A [c] é tão fofa."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    if priscila_namoro:

        "Nem acredito que eu realmente tô namorando com ela."

        "Parece um lance muito impossível."
    else:


        "A gente realmente se aproximou depois do que aconteceu."

    "Só de lembrar do [mar] apontando aquela arma pra mim, já fico com a perna bamba."

    "Ela pediu pra eu ligar a TV rapidão. Provavelmente é pra eu ver o noticiário."

    scene tv apresentador with Dissolve(1.0)

    "Apresentador" "... filme será uma das maiores produções mundiais."

    mc desconfiado "Quê? Será que tão falando do filme dela?"

    "Apresentador" "O novo filme será estrelado por, nada mais nada menos, que [cc], sensação teen do ano."

    if not priscila_p1:

        $ p1_descobriu = True

        "Apresentador" "A informação veio à tona após publicação de uma revista de grande circulação na capital."

        "Apresentador" "A matéria cita que [c] fechou o contrato recentemente após visita à capital."
    else:


        $ priscila_p1 = False
        $ pautas -= 1

        "Apresentador" "Obtivemos com exclusividade a informação de que [c] fechou o contrato após uma visita à capital."

        mc angustiado "Quê?! Droga! Eu tinha essa informação, mas não entreguei pro chefe e agora descobriram!"

        "Merda... uma pauta a menos pra entregar pro chefe."

    scene priscila filme_close with Dissolve(1.0)

    pause

    mc surpreso "Uou!"

    "Apresentador" "O que você vê agora em sua tela é uma cena exclusiva do filme vazada esta manhã na internet."

    "Apresentador" "A cena mostra [c] trajada como uma guerreira medieval."

    "Apresentador" "Ao que tudo indica, a história será do gênero fantasia, mas não temos informações sobre isso."

    if priscila_atencao == 2:

        "Apresentador" "Outra informação divulgada recentemente pela mesma revista que descobriu o protagonismo de [cc]..."

        "Apresentador" "É que o diretor do longa será o renomado [diretor]. Ele não quis comentar o caso."

        "Apresentador" "[diretor] é conhecido por usar jovens modelos como protagonistas em seus filmes. O fato se tornou uma das marcas do diretor."

        "Apresentador" "Em entrevista recente, [gus] explicou a curiosidade, afirmando que gosta de transformar garotas em mulheres por meio de seu trabalho."

    scene tv apresentador with Dissolve(1.0)

    "Apresentador" "Por meio de sua assessoria, [cc] não desmentiu a informação, afirmando que irá se pronunciar no momento correto."

    "Apresentador" "Pela imagem vazada esta manhã, podemos acreditar que o filme se encontra na etapa de filmagem."

    "Apresentador" "A carreira meteórica de [c] tem tudo para subir um novo degrau, fazendo fãs de todas as idades por meio da telona."

    "Apresentador" "Fique ligado na Faux News para todas as informações sobre o filme. Voltamos já."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    "Vinheta" "{b}Faux News: Nós somos a Verdade{/b}"

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    "Acho que era isso que ela queria que eu visse."

    if casa:

        scene ap mc_cel with Dissolve(1.0)
    else:


        scene mc ap_celular with Dissolve(1.0)

    if p1_descobriu:

        "E o pior é que agora ela vai saber que eu entreguei a pauta dela pro chefe."

        "Óbvio que ela vai ligar os pontos."
    else:


        "Pelo menos eu não entreguei a pauta pro chefe, ou ela ia descobrir agora."

        "Acho que eu me safei de uma pesada, agora."

    "Deixa eu avisar ela que eu vi."

    "..."

    "Já respondeu. Acho que ela tava vendo também."

    $ priscila_cel_msg6_r = "viu"

    show screen celular_priscila

    "..."

    "Que boba. Claro que pode lig-"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    mc "Já tá ligando... Pra que pergunta então?"

    mc "Alô?"

    c "Oiê! Ah! Não quero falar no telefone... Você não pode vir aqui?"

    mc "Como é? Não entendi nada."

    c "Hehe. Desculpa. Eu ia te falar um negócio, mas eu tô no hotel na frente da sua casa. Você não quer vir aqui?"

    mc "Claro. Cinco minutos tô aí."

    c "Tá! Tô te esperando!"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    "Ela parece bem animada. Será que tem alguma coisa com o filme?"

    "Deixa eu ir lá."

    scene ilha parque with Dissolve(1.0)

    pause

    "Só cruzar a praça e tô no hotel."

    scene hotel recepcao with Dissolve(1.0)

    "Ela ficou me esperando. Que bonitinha."

    "Essa é a primeira vez que eu vejo ela depois do lance no viaduto."

    if priscila_namoro:

        "A gente oficializou o namoro, mas nem tivemos tempo pra curtir isso ainda."

        "Será que vai ficar estranho se eu chegar beijando ela? Tô nervoso..."

    menu:
        "Apenas comprimentar":


            "Melhor não arriscar nada agora. Vou só falar com ela normal. Com o tempo a gente vai pegando no tranco."

            mc normal "Oi."

            scene pri3_img2 with dissolve

            c "Oii!"
        "Abraçar ela":


            if priscila_namoro:

                "Acho que um abraço não vai longe demais e também não fica parecendo que nada aconteceu."

            scene black with dissolve

            scene pri6_img1 with dissolve

            pause

            c "Hmmm... que gostoso."

            c "Tava com saudades de você."

            mc "Eu também."

            scene pri3_img2 with dissolve

        "Abraçar e dar um beijo" if priscila_namoro:

            "Um bom abraço e um beijinho é o suficiente pra não forçar a barra."

            scene black with dissolve

            scene pri6_img1 with dissolve

            pause

            c "Hmmm... que delícia ganhar um beijo do meu namorado."

            mc "Você tá muito cheirosa."

            c "Obrigada."

            scene pri3_img2 with dissolve

    c "Tá tudo bem com você?"

    mc "Eu tô bem. E você?"

    if priscila_namoro:

        c "É..."

        c "Tô meio com vergonha... mas tô muito feliz."

        mc "Eu também."

        mc charmoso "Mas não precisa disso, ok? A gente só vai continuar se vendo igual sempre..."

        menu:
            "Mas você vai deixar eu pegar na sua bunda.":


                $ priscila_idiota += 1

                mc tarado "Só que você vai deixar eu pegar na sua bunda. Única diferença."

                c "Ei! Que isso..."

                c "..."

                mc envergonhado "Era só brincadeira."

                c "Sei..."

                "Acho que ela não gostou muito."
            "Só que com uns beijos a mais...":


                mc charmoso "Mas com uns beijos aqui e ali. O que você acha?"

                c "Ai... adorei. Principalmente a parte do beijo."
            "Nada vai mudar.":


                mc normal "Na vai mudar, por isso não precisa ficar envergonhada."

                c "Nada nadinha?"

                mc desconfiado "Ah?"

                c "Nada. Deixa..."
    else:


        c "Sabe... tô bem mais feliz esses dias. E é tudo graças a você, [mc]."

        mc desculpa "Não vai desaparecer de novo, hein?"

        c "Eu sei... desculpa..."

        mc "Não precisa se desculpar. Só não quero perder minha amiga de novo."

        c "Seu fofo..."

    c "Ah! Eu te liguei pra te contar uma coisa muito especial!"

    mc normal "O que?"

    c "Eu acho muito legal pelo menos... não sei se você vai gostar..."

    mc envergonhado "Vai falar ou não?"

    c "Calma! Agora eu tô me sentindo pressionada. Não devia ter falado que era muuuuito especial."

    mc zerado "..."

    c "Tá! Eu falo! É o seguinte..."

    c "Eu vou viajar para regravar algumas cenas do filme..."

    mc desconfiado "Eee..."

    c "Eeee você quer viajar para o set de gravação comigo?!"

    mc surpreso "Quê?!"

    c "Sim! Você quer ver as filmagens comigo amanhã?!"

    "Viajar com ela até o set de filmagem... Parece algo incrível..."

    if p3_confissao:

        "Só que... será que o [gus] vai tá lá?"

        mc desculpa "[c]... o [gus] também vai tá lá?"

        scene pri3_img5 with dissolve

        c "Ugh!"

        c "..."

        c "Sim..."
    else:


        "Não tenho por que não aceitar!"

        mc feliz "Claro que eu vou!"

    if p3_confissao:

        "Merda..."

        "Será que ela continua 'vendo' ele? Só de pensar nisso eu tenho vontade de socar alguma coisa!"

        "A vontade que eu tenho de esmurrar esse velho..."

        mc bravo "..."

        mc "..."

        c "[mc]?"

        "Ver o velho idiota vai acabar com a viagem, mas perder esse tempo com a [c] por causa dele vai ser muita burrice."

        "E o [mar] também vai estar lá... Como a [c] consegue continuar nesse círculo mesmo depois de tudo?"

        label priscila_e5_viagem:

            "Não dá pra ficar pensando nisso agora. O que eu faço? Viajo com ela?"

        menu:
            "Claro que eu vou! Vai ser incrível!":


                mc feliz "Não perderia isso por nada!"

                scene pri3_img6 with dissolve

                c "Sério?!"

                mc "Claro! Vou deixar de ver a minha atriz preferida gravando?"
            "Desculpa, mas não posso.":


                "Se eu recusar, vou perder toda a viagem com ela. Será que é o melhor?"

                menu:
                    "Sim. Não vou viajar":


                        $ p5_naoviajou = True
                        $ priscila_idiota += 2

                        mc desculpa "Desculpa, mas eu tô correndo com uma matéria da revista, não vou conseguir ir..."

                        c "Sério?! Puxa..."

                        c "..."

                        "Ela ficou bastante triste..."

                        c "Então tá..."

                        mc normal "Mas assim que você voltar a gente se vê. E não deixe de me mandar fotos."

                        c "Ok. Se cuida, [mc]."

                        mc envergonhado "Boa viagem e até daqui a pouquinho."

                        if priscila_namoro:

                            c "Não vejo a hora de voltar e a gente poder namorar."

                            mc charmoso "Eu também."

                        c "Tchau."

                        scene black with dissolve

                        "Tomara que fique tudo bem entre a gente..."

                        jump priscila_e5_finalzinho
                    "Melhor eu pensar um pouco mais":


                        "Perder todo esse tempo com a [c] não vai ser legal também. Deixa eu pensar..."

                        jump priscila_e5_viagem

    scene pri3_img6 with dissolve

    c "Vai ser incrível, [mc]! Você vai ver!"

    mc normal "Tenho certeza que vai."

    c "Então amanhã logo cedo eu passo te pegar no seu prédio, tá?"

    c "A gente vai de carro até o aeroporto e de lá a gente vai ter um jatinho particular esperando a gente."

    mc envergonhado "Caraca. Isso que é luxo."

    c "É uma mega produção. Tá tudo pago pra gente."

    mc "Legal..."

    c "Então amanhã a gente se vê. Agora tenho que arrumar tudo pra viagem."

    mc normal "Ok. Vou ficar ansioso."

    c "Eu tambéééémmmm!"

    if priscila_namoro:

        c "Tô louca pra gente namorar muito."

        mc "Não fala assim que você já me deixa doido."

        c "A gente vai ter tempo, homi!"

        c "Beijos, lindo."
    else:


        c "Tchau, [mc]."

    mc "Até amanhã."

    scene black with dissolve

    "O clima tá bem legal entre a gente..."

    "Opa. Deixa eu sair daqui antes que o porteiro me coloque pra fora."

    "..."

    if casa:

        scene ap mc_dormindo3 with Dissolve(1.0)
    else:


        scene mc dormindo_dois with Dissolve(1.0)

    "Uma viagem com a [c]... direto onde o [gus] trabalha. Será que realmente foi uma boa decisão?"

    if priscila_namoro:

        "Outra coisa é que agora que a gente tá namorando, eu preciso pensar nisso também."

        "Se eu for um idiota com ela, provavelmente {b}ela pode me deixar{/b}."

        "Ser chutado pela [c] depois de tudo o que a gente viveu por uma coisa idiota vai ser horrível."

    "Tenho que pensar... direitinho..."

    show black with dissolve

    hide black with dissolve

    "Se ela me deixar..."

    show black with dissolve

    $ renpy.pause(delay=1, hard=True)

    hide black with dissolve

    "Não posso deixar as coisas acabarem assim..."

    show black with dissolve

    "..."

    $ tempo = 1
    $ dia += 1

    "..."

    hide black with vpunch

    "Ah!"

    "Acho que eu dormi."

    "Quê?! Já amanheceu..."

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento dia with Dissolve(1.0)

    "Tenho que arrumar as coisas. A [c] vai passar aqui logo."

    "..."

    "Agora um banho, que eu tô fedendo."

    play sound "audio/som_16_chuveiro.mp3"

    if casa:

        scene ap mc_chuveiro with Dissolve(1.0)
    else:


        scene mc banho with Dissolve(1.0)

    "Vou levar só o essencial. Vai ser apenas um dia também. Se pá dá pra ir só com a roupa do corpo."

    "Viajar de jato..."

    mc "Espero que eles me tragam tamb-"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    "Opa. Acho que tô ouvindo o cel."

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento dia with Dissolve(1.0)

    show mc cueca_telefone with dissolve

    mc "Oi?"

    c "Bom dia! Dá pra passar aí em 10 minutos?"

    mc "Sim. Vou por uma roupa e tô pronto."

    c "Legal! Já tô indo então. Beijo!"

    mc "Beijo."

    hide mc with dissolve

    "Deixa eu acelerar tudo aqui."

    "..."

    play sound "audio/som_15_campainha.mp3"

    "{i}Ding Dong{/i}"

    mc surpreso "É ela!"

    mc envergonhado "Caraca, que nervoso que deu agora."

    "Mas bora lá."

    scene black with dissolve

    "..."

    scene carro cidade with Dissolve(2.0)

    pause

    c "Tô tão feliz que você tá indo comigo, [mc]."

    mc "Não é nada..."

    c "Pra mim é tudo!"

    mc "Hehe..."

    c "..."

    mc "Duro é a gente ter que dirigir uma hora de carro só pra chegar no aeroporto."

    mc "Bom, é o motorista que tá dirigindo, mas você entendeu..."

    c "Verdade. Aliás, eu escutei um negócio dizendo que o prefeito desistiu do metrô e vai fazer um aeroporto na ilha."

    mc "Quê?! Quem disse isso?"

    c "Alguém lá do filme. Parece que vão lançar daqui a pouco tempo inclusive."

    mc "E como ninguém sabe disso?"

    c "Eles tão fingindo que a obra é pra outra coisa, por isso não tá na mídia ainda."

    mc "Que loucura... esconder uma obra desse tamanho... só nessa cidade mesmo."

    c "Tem muita coisa que acontece aqui e a gente nem fica sabendo."

    mc "Verdade..."

    "..."

    "Motorista" "Senhorita [c]. Estamos chegando."

    c "Ok! Obrigada!"

    scene black with dissolve

    "..."

    c "Pronto?"

    mc preocupado "Si-sim..."

    scene jato exterior with Dissolve(1.0)

    pause

    mc surpreso "Caralho! Que massa!"

    c "Né? Agora vem aqui."

    mc "O-opa!"

    scene black with dissolve

    scene pri5_img1 with dissolve

    pause

    c "E é só pra gente, sabia?"

    mc "Co-como?!"

    c "Bobinho..."

    mc envergonhado "Ei... mas é sério que é só pra gente?"

    c "Sim. Iremos somente nós e o pessoal que faz esse treco voar."

    mc "Incrível..."

    c "Ah... não quero que você fique me achando uma metida... só achei divertido ver sua reação."

    mc charmoso "Para de ser boba. Tá tudo legal."

    mc envergonhado "Apesar que eu tenho que revelar que eu nunca andei de avião antes..."

    c "Sé-sério?!"

    c "Vai ser sua primeira viagem de avião?"

    mc envergonhado "Sério... mas não é pra tirar sarro."

    c "Ai! Que legal, [mc]! Vai ser tão especial..."

    mc normal "É o que eu espero também."

    "E que eu não morra."

    c "Mas se-"

    "Homem" "Senhorita, [c]! Estamos prontos pra decolar!"

    c "Ah! Já vamos sair."

    mc preocupado "Ok..."

    if priscila_namoro:

        scene pri5_img2 with dissolve

        c "É... eu queria te pedir um negócio antes da gente sair."

        mc desconfiado "Certo..."

        c "Você sabe que eu adoro ser sua namorada, né?"

        mc envergonhado "Bom saber..."

        c "Claro que eu gosto!"

        mc "Ok ok!"

        c "Então. Mas é que eu não quero que as pessoas saibam disso ainda."

        c "Eu tô com muita vergonha de falar isso pra você... mas, você entende, né?"

        "Não sei se eu entendo... Por que as pessoas não podem saber da gente?"

        "Eu sei que ela é famosa, e nosso namoro pode causar um rebuliço, mas tipo... como eu fico?"

        "E agora? Como eu vou reagir a isso?"

        menu:
            "Eu não aceito. Eu sou seu namorado.":


                $ priscila_idiota += 1

                mc serio "Eu não quero que a gente namore desse jeito. Eu sou seu namorado ou não sou?"

                c "Ah? É... claro que é!"

                mc "Então. Quero que as pessoas saibam disso também."

                c "Por favor, [mc]. Você trabalha como paparazzo. Você sabe como as revistas são."

                c "Não quero que isso atrapalhe nosso relacionamento e nem minha carreira."

                mc "..."

                mc concentrando "Ok. Não quero te prejudicar. Mas não concordo com isso."

                c "Valeu..."
            "Tudo bem. Eu entendo.":


                mc normal "Eu entendo. Claro que eu queria poder beijar qualquer hora, mas sei como as coisas são."

                c "Obrigada, [mc]... eu sei que isso é sacan-"

                mc charmoso "Não precisa se preocupar, de verdade. O importante é que eu tô com você. Ninguém precisa saber disso."

                c "Ai..."

                c "Às vezes eu esqueço que você fala as coisas desse jeito..."

                mc charmoso "..."
            "Mesmo não concordando, eu aceito.":


                mc desculpa "Mesmo não achando certo a gente esconder as coisas, eu concordo que é melhor por enquanto."

                c "Obrigada... eu sei que é sacanagem pedir isso pra você, mas assumir um namoro agora só complicaria tudo."

                mc normal "Eu sei. Pode contar comigo."

                c "Valeu."

        c "É..."

        c "Eu queria pedir um último favor pra você."

        mc charmoso "Não precisa falar assim com medo. O que é?"

        c "Já que a gente vai ter que tomar cuidado lá no set de filmagem, será que você podia me dar pelo menos um abraço agora?"

        mc envergonhado "Mas o pessoal do avião tá de olho aqui."

        c "Ah! Eu sei, mas... eu queria muito... e é só um abraço. Tipo de amigo..."

        "Ounn... que fofinha... mas e se os pilotos verem a gente? E agora?"

        menu:
            "Dar um abraço como ela pediu":


                "Ela pediu de forma tão bonitinha..."

                scene black with dissolve

                scene jato exterior with dissolve

                c "Obrigada... eu gosto tanto de sentir você."

                mc "Eu também gosto de você, bobinha."

                c "Só mais um pouquinho..."
            "Dar um beijo":


                $ priscila_idiota += 1

                "Vou é dar um beijão nela. Foda-se o pessoal do avião."

                mc tarado "Vem aqui."

                scene pri5_img2 with hpunch

                c "Ei!"

                c "O que você tá fazendo?!"

                mc "Só um beijo..."

                c "Era um abraço! Eles tão olhando!"

                mc serio "Calma, não precisa fazer tudo isso..."

                c "Isso é importante pra mim, [mc]."

                mc "..."

                c "Por favor, não faça mais essas coisas..."

                mc preocupado "Ok..."
            "Não dar nenhum dos dois":


                mc envergonhado "Na verdade acho que é melhor a gente não dar chance pro azar."

                mc normal "Quero muito ficar com você, mas não quero nem pensar em virar boato."

                c "Você tem razão..."

                c "Obrigada por se preocupar com a gente."

    c "Então vamos pra lá?"

    mc "Vamos."

    scene black with dissolve

    scene pri5_img3 with dissolve

    pause

    "..."

    scene black with dissolve

    scene ilha jato_geral with Dissolve(1.0)

    mc surpreso "Sério que tudo isso aqui é pra gente?"

    c "Sim... eu também acho que é meio coisa de mais às vezes..."

    if priscila_namoro:

        "Caraca... o que eu tô fazendo namorando com essa mina?"

        "A [c] normalmente é tão de boa que eu me esqueço que ela é uma estrela nacional."

        "Certeza que ela podia ter o cara que quisesse. O que será que ela viu em mim?"
    else:


        "A [c] normalmente é tão de boa que eu me esqueço que ela é uma estrela nacional."

        "Por que ela perde tempo comigo?"

    mc desculpa "..."

    c "Que foi? Não gostou?"

    mc envergonhado "Não é nada. Só tô pensando em umas coisas..."

    c "No quê?"

    mc "Nada, não..."

    c "Huh..."

    "Autofalante" "Bom dia, senhorita passageira e senhor passageiro. Estamos decolando em 5 minutos."

    "Autofalante" "Peço que se acomodem e coloquem os cintos, por favor."

    c "Pode sentar em qualquer lugar, ok?"

    mc normal "Pode deixar."

    c "Com medo?"

    mc envergonhado "Até parece..."

    scene ilha jato_geral at treme_vertical

    mc surpreso "!"

    mc angustiado "Que porra é essa?!"

    c "Calma, [mc]. Quando liga o motor, como é uma nave menor, a gente sente um pouco. Logo passa."

    mc envergonhado "Eu sei. Só tava brincando."

    c "Bobo..."

    "Sorte que ela acreditou."

    "..."

    "Autofalante" "Aviso final. Por favor, apertem os cintos e se preparem para tomar altitude."

    "..."

    "É agora ou nunca!"

    "..."

    mc incomodado "..."

    "..."

    mc angustiado "..."

    scene white with Dissolve(3.0)

    pause

    "..."

    "Autofalante" "A decolagem foi um sucesso. Podem soltar os cintos."

    "Autofalante" "Tempo estimado de viagem... uma hora e doze minutos."

    scene black with dissolve

    scene priscila jato_mc with dissolve

    pause

    "Ufa... Tá dando tudo certo... Até colocaram as coisas pra gente comer e beber."

    c "Tá mais calmo?"

    mc "Eu nem fiquei nervoso..."

    c "Nem um pouquinho?"

    mc "{size=10}Talvez um pouquinho{/size}"

    c "Você é muito fofinho às vezes, [mc]."

    if priscila_namoro:

        c "Eu tenho muita sorte de ter pescado esse peixe pra mim."

        mc "Hehe..."

        menu:
            "Por que você quis namorar comigo?":


                mc "Sabe, [c]. Sei que a gente ainda tá só começando, mas por que você quis namorar comigo?"

                c "Que tipo de pergunta é essa, [mc]?"

                mc "Tipo... eu tava pensando aqui... você é linda, inteligente, fofa, engraçada, gostosa, rica, famosa..."

                c "Tá vendo o por quê? Quando um rapaz fala isso de você de forma tão sincera, é o cara certo."

                mc "Haha... tô falando de verdade."

                c "..."

                c "Essa falta de confiança não combina com você."

                mc "..."

                "É que você não consegue ler meus pensamentos..."

                c "Se você realmente precisa saber is-"

                mc "Quer saber? Foi uma pergunta idiota. Acho que foi todo esse luxo que me deixou meio deslocado."

                c "Tudo bem, gato... você vai sobreviver."

                mc "Valeu..."
            "...":


                mc "..."

                "Não tenho que ficar pensando em besteira."

        "O que eu tô fazendo? Ficar me sentindo inferior só vai complicar ainda mais as coisas."

        "Se ela resolveu namorar comigo é porque ela quer. Ninguém obrigou ela. E se ela quer, é porque alguma coisa eu tenho."

        "Se eu ficar me sentindo inferior, só vou piorar tudo. Força, [mc]!"

        c "É..."

        mc "Hm?"

        c "A gente tá longe, né?"

        mc "Verdade... Na hora de decolar, nem vi onde tava sentando..."

        c "É..."

        "Acho que ela tá querendo falar alguma coisa com isso."

        "Mas e se ela ficar chateada? Ela pediu pra gente não dar bandeira durante a viagem..."

        menu:
            "Vem aqui sentar do meu lado.":


                mc "Vem aqui sentar comigo."

                c "Mas... é melhor a gente não exagerar. Pode deixar o pessoal do avião ligados demais."

                menu:
                    "Tem razão. Vamos tomar cuidado.":


                        mc "Você tá certa. Vamos tomar cuidado. Vamos ter tempo."

                        c "Sim..."
                    "Que nada. Vem aqui.":


                        label priscila_e5_cenaaviao:

                            scene priscila jato_mc

                            $ persistent.priscila_cena12 = True

                        mc "Não quero saber. Pode vindo aqui."

                        c "Mas-"

                        mc "Veeeemmm..."

                        c "Tá..."

                        mc "Deita aqui."

                        "..."

                        scene priscila jato_mc_deitada with Dissolve(2.0)

                        pause

                        c "Ai, [mc]..."

                        mc "Que foi?"

                        c "Eu me sinto tão bem quando tô com você."

                        mc "Aproveita, então..."

                        c "Metido..."

                        window hide

                        pause

                        $ renpy.end_replay()
            "A gente vai ter muito tempo juntos depois.":


                mc "Vamos tomar cuidado. Vamos ter bastante tempo ainda, né?"

                c "Sim..."
    else:


        c "Nessas horas eu fico pensando um negócio..."

        mc "O que?"

        c "Eu sei que a gente resolveu as coisas... desculpa por falar sobre isso de novo..."

        c "Mas às vezes ainda tenho vontade de ser mais... que uma amiga..."

        mc "Eu sei como é."

        mc "Pra falar a verdade, você é uma garota incrível. O sonho de qualquer rapaz."

        c "Mas não o seu sonho..."

        mc "..."

        c "Desculpa por acabar com o clima."

        mc "Não acabou com nada."

    mc "E como tão as coisas com o filme?"

    c "Ah..."

    c "Tá indo tudo bem. Criaram uma cidade enorme pra gente gravar e alguma coisa já tá pronta."

    mc "É cansativo?"

    c "Bastante. Eu passo quase 12 horas por dia gravando."

    mc "Sério?!"

    c "Sim. Como tudo é alugado, inclusive toda a área, a gente precisa gravar o mais rápido possível. Não dá pra ficar enrolando."

    mc "Mas 12 horas..."

    c "Eu sou forte. Eu aguento."

    mc "Hehe... Você é mesmo..."

    if p3_confissao:

        "Não tenho coragem de perguntar pra ela sobre o [gus]..."

        "Provavelmente ela nem sabe que o [mar] me ameaçou aquela noite no viaduto."

    c "Mas assim que as gravações terminarem meu trabalho vai tá pronto. Daí é com eles."

    mc "Que bom."

    c "Uaaahh..."

    mc "Fecha os olhos um pouco até a gente chegar."

    c "Quem sabe..."

    scene black with dissolve

    c "{i}zzzz{/i}"

    mc zerado "Pra quem tava em dúvida, até que dormiu bem rápido."

    mc desculpa "Ela deve tá super cansada."

    "..."

    "Autofalante" "Atenção. Por favor coloquem seus cintos novamente. Pousaremos em breve."

    mc desculpa "Pri. A gente já vai pousar."

    c "Ah! Acho que eu dormi... deixa eu voltar pra minha cadeira."

    scene priscila jato_mc with Dissolve(1.0)

    c "Acabei deixando você sozinho, né?"

    mc "Foi só um pouquinho."

    scene priscila jato_mc at treme_vertical

    mc "Opa!"

    c "Aperta aí. Já vamos descer."

    scene white with Dissolve(2.0)

    "..."

    c "Obrigada pela viagem!"

    "Piloto" "É sempre um prazer, senhorita [c]."

    c "Vamos, [mc]?"

    mc "Claro."

    scene priscila mc_andando_set with Dissolve(2.0)

    pause

    mc "Maluco, quanto verde..."

    c "É um lugar imenso. Você vai ver ainda."

    mc "Não dá nem pra ver o final."

    c "Tem até um rio e uma gruta. Ah! E um castelo e uma vila mágica..."

    mc "Sério isso?"

    c "A-hã. Você vai ver tudo hoje."

    mc "Uou..."

    mc "E agora? Pra onde tamo indo?"

    c "Pro meu camarim. Eu vou me trocar, maquiar... o horário tá meio em cima. Menos de uma hora pra começar a filmar."

    mc "E nesse tempo eu fico onde?"

    c "Você vai ficar o tempo todo comigo. Quero que você veja tudo. Se você quiser, claro..."

    mc "Vou ver, sim. Não vou perder uma cena."

    c "Tenho certeza que você vai gostar da minha roupa."

    if priscila_namoro:

        c "Seria melhor guardar pra nossa lua de mel, mas, né?"

        mc "Eita. A roupa é assim mesmo?"

        c "Mais ainda. Você vai ver logo..."

    c "É logo ali."

    scene black with dissolve

    scene camarim geral with Dissolve(1.0)

    pause

    c "Tcharããã~!"

    mc desconfiado "O que é essa minicasa?"

    c "Rsrs... não seja bobo. É meu camarim."

    mc "Como é? Aí que você se arruma?"

    c "Sim. Na verdade, é praticamente minha casa enquanto eu tô gravando."

    c "Eu me arrumo aqui, mas também posso tomar banho, tem cama, internet. Quando não tô gravando, passo um tempão aqui."

    mc normal "Que legal."

    c "Vem ver dentro."

    mc "Claro."

    scene black with dissolve

    scene camarim interior with Dissolve(1.0)

    pause

    c "Lar doce lar!"

    c "O que você achou?"

    mc normal "Hmmm...."

    mc charmoso "Muito bacana."

    mc "Tô vendo suas coisas de maquiagem aqui. Ali é o banheiro, né?"

    c "Isso."

    mc "E lá em cima fica sua cama. É... parece bem aconchegante."

    c "Não é nada de mais... só é meu lugarzinho."

    mc charmoso "Que nada. Eu achei muito muito legal. Que bom que eles te dão essa privacidade."

    c "Sim. Isso é importante. Ninguém vem mexer comigo aqui."

    mc "Isso é muito bom."

    c "Com certeza."

    if priscila_namoro:

        mc "Mas e eu? Posso mexer com você aqui?"

        c "No que você quer mexer?"

        mc "Talvez na boca... talvez nesse seu corpo incrível."

        c "Sei..."

        c "Falando em corpo..."

    c "Aliás, eu tenho uma surpresa pra você."

    mc normal "A é?"

    c "Mas você vai ter que ficar de olho fechado até eu falar que você pode abrir, hein?"

    mc concentrando "Ok."

    c "Promete?"

    mc "Prometo."

    c "Olha, hein!"

    mc envergonhado "Prometo..."

    c "Ok. Pode fechar então."

    show black with dissolve

    mc concentrando "Pronto."

    c "Quantos números tem aqui na minha mão?"

    mc "Como vou saber? Tô de olho fechado..."

    c "Então tá."

    "..."

    menu:
        "Continuar de olhos fechados":


            "Não vou ferrar com minha surpresa. Vou é ficar quietinho aqui."

            mc concentrando "..."

            "..."

            "..."

            "Caraca, o que ela tá fazendo?"

            "..."

            "..."

            "..."

            "Não tô aguentando mais..."

            menu:
                "Continuar de olhos fechados":


                    "Só mais um pouco. Tenho que aguentar..."

                    mc concentrando "..."

                    "..."

                    "..."

                    "..."

                    "..."

                    "..."

                    jump priscila_e5_roupa
                "Abrir e fechar os olhos rapidamente":


                    "Vou abrir bem rápido... nem vai dar pra ver..."

                    scene priscila camarim_maquiando

                    show black

                    hide black with dissolve

                    show black with dissolve

                    "O que era aquilo?! Ela tava de calcinha e sutiã?!"

                    "Acho que ela não viu eu abrindo os olhos. Fechei rapidão."

                    "E agora? Será que eu tento a sorte? Será que eu abro um pouco os olhos?"

                    menu:
                        "Não abrir os olhos novamente":


                            "Não posso foder tudo. Ela deve tá acabando, certeza..."

                            mc concentrando "..."

                            "..."

                            "..."

                            "..."

                            "..."

                            "..."

                            jump priscila_e5_roupa
                        "Abrir só um pouco os olhos":


                            "Se eu abrir só um pouquinho vai ser impossível dela perceber..."

                            show black with Dissolve(1.0):
                                alpha 0.95

                            pause

                            "Uou... a [c] é MUITO gata. Olha só pra esse material. Coisa de primeira linha."

                            "Eu queria poder ver melhor... mas acho que já fui longe demais."

                            "Ou será que não?"

                            menu:
                                "Fechar os olhos e esperar":


                                    "Já fui longe demais. Não quero estragar tudo."

                                    show black with dissolve:
                                        alpha 1.0

                                    mc concentrando "..."

                                    "..."

                                    "..."

                                    "..."

                                    "..."

                                    "..."

                                    jump priscila_e5_roupa
                                "Abrir os olhos completamente":


                                    "Não aguento! É perigoso, mas eu não consigo! Preciso ver essa bunda!"

                                    hide black with Dissolve(1.0)

                                    pause

                                    "Uoooou!"

                                    "A garota perfeita!"

                                    if priscila_namoro:

                                        "Eu tô namorando a garota perfeita!"
                                    else:


                                        "Por que eu disse que não queria namorar ela?!"

                                        "Ver ela assim faz eu questionar toda minha existência!"

                                    c "Ah?"

                                    "Merda!"

                                    c "Ei! Você tá de olho aberto, safado!"

                                    mc angustiado "Não! Desculpa!"

                                    c "[mc]! Seu cuzão!"

                                    jump priscila_e5_fracasso
        "Abrir os olhos":


            $ priscila_idiota += 1

            "Não consigo esperar. Preciso dar uma olhadinha."

            hide black with Dissolve(1.0)

            "Ah?"

            scene pri5_img3 with vpunch

            c "Aha!"

            c "Peguei você!"

            mc surpreso "Eita!"

            c "Safado!"

            mc preocupado "Não..."

            c "Agora não tem mais graça. Vou no banheiro me trocar e já venho."

            scene black with dissolve

            "Que merda... estraguei tudo."

            jump priscila_e5_fracasso

label priscila_e5_roupa:

    c "Ufa... terminei."

    "Maluco, deve ter passado mais de uma hora..."

    c "Pronto?"

    mc concentrando "Tô."

    c "Pode abrir."

    scene pri5_img5 with Dissolve(1.0)

    pause

    c "E aí? Tô gata ou não?"

    menu:
        "Tá muito linda.":


            mc normal "Você tá incrível. Tá linda demais."

            c "Obrigada, [mc]."

            if priscila_namoro:

                c "Como é namorar uma garota linda demais?"

                mc charmoso "Não sei nem o que falar. Mas acho que é a melhor sensação do mundo."

                c "Hmmm..."

        "Gostosa pra caralho." if priscila_namoro:

            mc charmoso "Tu tá gostosa pra caralho!"

            c "Nossa. Tudo isso?"

            mc safado "Mais do que você imagina."

            c "Hmm..."

            mc safado "Agora você tá me provocando de propósito."

            c "E se eu tiver?"

            mc "Você tem que tomar cuidado pra eu não te atacar..."

            c "Eu tô tão desprotegida..."

            "Ela tá me deixando louco."
        "E eu tenho que falar?":


            mc normal "E eu tenho que falar?"

            c "Seria bom..."

            mc "Você sabe que você tá linda."

            c "Mas é melhor quando a gente escuta."

    jump priscila_e5_roupa_depois

label priscila_e5_fracasso:

    $ priscila_idiota += 1

    c "Eu falei pra você não olhar..."

    mc preocupado "Desculpa... mas fiquei muito ansioso."

    c "Seu chatão."

    "Que droga... se eu tivesse me segurado."

label priscila_e5_roupa_depois:

    mc desconfiado "Mas agora que eu tô pensando... que roupa é essa?"

    c "Haha! É minha roupa de batalha, ué?"

    mc normal "Ah! Eu vi você com essa roupa no noticiário. Então era isso!"

    c "Espera."

    scene camarim interior with Dissolve(1.0)

    mc "E o que é agora?"

    c "Pera. Tá aqui."

    show priscila a_brava with dissolve

    pause

    c "Eu não deixarei você sair com vida depois do que você fez na Cidade Mágica!"

    c "Minha lâmina tingida de vermelho vai vingar a morte de todos aqueles que encontraram o fim pela ponta da sua lança."

    c "Seu filho da puta!"

    mc desconfiado "Filho da puta? Sério? É uma das falas?"

    show priscila a_surpresa with dissolve

    c "Nã-não. Só tô tentando entrar no personagem, sabe?"

    mc zerado "Acho que isso é um pouco demais pro público do filme..."

    c "Hehe... acho que você tem razão."

    if priscila_namoro:

        mc safado "Mas o que você acha de deixar essa espada de lado e vir aqui comigo rapidinho."

        c "O que você tá planejando?"

        mc "Você vai ver."

        hide priscila with dissolve

        c "Opa!"

        mc tarado "Você não vai precisar disso aqui agora."

        c "Ei, [mc]!"

        scene priscila camarim_mc with Dissolve(2.0)

        pause

        c "Ai..."

        mc "Essa roupa tá me deixando louco."

        mc "Seu jeito tá me deixando louco."

        c "Eu gosto de te deixar louco, mas lembra o que eu disse? Vai que alguém vê a gente?"

        mc "Não tem ninguém aqui perto. Pode ficar tranquila."

        c "Hmmm..."

        c "Será que ninguém vai vir mesmo? Ai, [mc]..."

        label pri5_priscila_premium:

            pass

        "Ela disse pra eu maneirar aqui nas gravações... mas se eu forçar um pouco acho que ela aceita."

        "O que eu faço?"

        menu:
            "Deixa disso. Vem aqui.":


                if not premium:

                    show black with dissolve

                    p rindo "Ops! A próxima cena é exclusiva para a versão premium do game."

                    p "Você precisa baixar a versão exclusiva para apoiadores no site www.apoia.se/geiko para poder jogar ela."

                    p "Você pode saber mais sobre a versão premium abrindo o MENU."

                    p lecionando "Quê?! Você tá falando que o desenvolvedor é um salafrário que só pensa em dinheiro e tudo devia ser grátis?"

                    p "Bom... talvez ele seja mesmo. Eu não vou discutir com você por causa disso. Eu não estou nem aí."

                    p "Mas talvez ele precise da grana para continuar fazendo os jogos. Vocês humanos precisam de comida, não precisam?"

                    p "Se cada jogador ajudar com um pouco, melhor para os games continuarem crescendo e melhorando!"

                    hide black with dissolve

                    jump pri5_priscila_premium

                mc "Claro que não... eu só vou pegar um pouco em você..."

                c "A-ai!"
            "Tem razão. É perigoso.":


                jump pri5_pulou_premium

        c "Essa roupa te deixou tão louco assim?"

        mc "Demais..."

        c "Então tá... vem aqui."

        scene black with dissolve

        scene pri5_img6 with dissolve

        pause

        c "É só isso que você queria, né? Pegar nos meus peitos."

        mc "Eu quero pegar em você toda... só vou começar por eles."

        c "Parece que você tem uma fixação por eles, isso sim... tipo uma tara por peitões gostosos."
        scene pnew_ani04 with Dissolve(1.0)
        mc "Eu não posso negar."

        c "Então vai... aproveita mais um pouco."

        scene black with dissolve

        scene pri5_img7 with dissolve

        pause

        c "Ah... quando você me aperta com vontade assim..."

        mc "Que que tem?"
        scene pnew_ani06 with Dissolve(1.0)
        c "Vai me dando um tesão..."

        menu:
            "Pega nele aqui, pega... sente como eu tô.":


                c "Ai... a gente tá no meio do meu trabalho..."

                scene black with dissolve

                scene ani11 with Dissolve(1.0)

                pause

                mc "A-agh..."

                c "Mas você falando assim... hmmm..."

                c "Esse pau duro... gostoso..."

                mc "Tudo por causa desses peitão que você tem... esse rabão... seu cheiro..."

                c "Ai... adoro quando eu te deixo duro assim!"

                mc "Ah..."

                mc "Que punheta gostosa, delícia. Sentir sua mão assim na minha piroca é muito bom."

                c "Eu bato gostoso pro meu homem?"

                mc "Bate direitinho."

                c "Awnn... eu amo deixar você desse jeito... me deixa molhada."

                mc "Deixa, é? Saber que você deixa um homem com o pau assim?"

                c "Muito..."

                menu:
                    "Todos homens ficam duros pra você, Pri. Você é uma modelo.":


                        c "E-eles ficam?"

                        mc "Você sabe que ficam... ficam te olhando e batendo pra você."

                        c "Aahh..."

                        scene black with dissolve

                        scene ani12 with Dissolve(1.0)

                        pause

                        mc "Ngghh..."

                        c "Ai... eles nunca vão ter coragem de falar pra mim..."

                        mc "Mas você sabe que é isso que acontece. Eles te olham no Instagram, nos sites de famoso."

                        mc "E se matam pro teu corpo gostoso."

                        c "Ai, [mc]..."

                        mc "Isso te deixa louca, né?"

                        c "Muito... t-tudo bem?"

                        menu:
                            "Fico com ciúmes assim.":


                                c "M-mas eu sou só sua..."

                                mc "Então tá."
                            "Claro. É só fantasia, gostosa. Pra te deixar no grau.":


                                c "Ahnn... s-sim..."

                                c "Eu fico muito excitada, [mc]... q-quando todo mundo me deseja..."

                                mc "Uhum..."
                    "Vai! Bate mais forte, delícia.":


                        c "Uhum..."

                c "Eu não tô aguentando mais, [mc]..."
            "Vamos trepar, Pri. Foda-se o trabalho.":


                c "S-sério? Aqui?!"

                mc "Você tá com tesão..."

        mc "Eu também. A gente não precisa parar aqui. Você sabe, né?"

        c "Se a gente não tivesse no meio de todo o pessoal que eu trabalho..."

        mc "Bora... não fica assim..."

        c "Não. Por favor, [mc]. Não quero agora."

        menu:
            "Não seja boba. Você vai gostar.":


                $ priscila_idiota += 1

                mc "Já falei que não tem ninguém. Não seja boba. Tenho certeza que você vai gostar."

                c "[mc]!"

                mc "..."

                scene camarim interior with vpunch

                c "Falei que não!"

                mc "A-ai..."

                scene pri5_img4 with dissolve

                c "Desculpa, mas não quero namorar agora."

                menu:
                    "Mas foi você que me provocou!":


                        $ priscila_idiota += 2

                        mc serio "Foi você que me provocou e agora quer tirar o corpo fora?"

                        c "Eu sei. Mas achei que você ia entender. Eu te expliquei sobre isso antes."

                        mc "Droga..."
                    "Tá legal, eu entendi.":


                        mc serio "..."

                mc concentrando "Ok..."

                mc envergonhado "Acho que eu exagerei um pouco."

                c "Tudo bem."
            "Tudo bem. Vamos ter tempo.":


                mc "Hmm..."

                label pri5_pulou_premium:

                    pass

                mc "Ok... a gente vai ter muito tempo ainda."

                c "Obrigada."

                c "Você sempre pensa em mim."

                scene black with dissolve

                scene pri5_img8 with dissolve

                pause

                c "Você foi a melhor coisa que já aconteceu pra mim."

                c "Ainda não acredito que consegui conquistar você."

                mc envergonhado "Tá louca? Sou eu que tinha que falar isso."

                c "Claro que não. Em todos nossos encontros, você sempre me colocou na frente."

                c "Eu sou só a donzela em perigo. Tipo uma idiota que tá em um game só pra ser bonitinha e ser salva pelo herói."

                c "Eu queria ser mais que isso..."

                c "Queria ter meus objetivos e também queria poder ajudar você com suas dificuldades."

                mc preocupado "Mas você ajuda."

                c "Não..."

                mc desculpa "Pensa, [c]. Sem você, eu teria perdido meu emprego. Estaria morando com meus pais."

                mc "Talvez até já tivesse morrido de desgosto."

                mc charmoso "Você me salvou."

                c "Não vale falar as coisas só pra me deixar feliz, hein?"

                mc "Combinado. Tô falando a verdade."

                c "Ok."
    else:


        scene black with dissolve

        scene pri5_img8 with dissolve

    c "Caraca. A gente precisa sair. Demorei pra caramba me arrumando. Eles já devem ter começado a filmar."

    c "E a maquiadora vai retocar tudo ainda."

    c "Tudo bem a gente ir pra lá?"

    mc normal "Claro. Tô super ansioso pra ver os cenários e tudo o mais."

    c "Você vai achar incrível! A primeira vez que eu vi eu quase desmaiei."

    c "É como se você tivesse dentro de um filme tipo O Senhor dos Anéis."

    mc "Então bora, mulher."

    c "Vamos."

    scene black with Dissolve(1.0)

    c "Já estamos quase lá. Continua com os olhos fechados."

    mc concentrando "Eu vou acabar caindo."

    c "Calma, eu tô segurando você."

    mc "Se você fizer eu passar vergonha na frente do povo..."

    c "Pode deixar."

    "..."

    c "Oi, pessoal!"

    "Várias vozes" "Boa tarde, [c]."

    c "Trouxe um amigo comigo hoje pra dar uma olhadinha. Vocês já tão em posição pra gravar?"

    if priscila_namoro:

        "Amigo?"

    "Mulher" "Sim."

    c "Eu queria que ele visse como se fosse a cena do filme mesmo."

    "Não acredito que ela tá fazendo esse auê todo. Que vergonha..."

    c "Isso. Tá ficando muito legal."

    c "Pode abrir os olhos."

    mc "E-eu?"

    c "Sim. Pode ver!"

    mc "Ok."

    scene rua magica with Dissolve(1.0)

    pause

    mc feliz "Que massa!"

    c "Eu disse."

    mc normal "A galera toda vestida. E essa rua. Parece um lugar de verdade."

    scene black with dissolve

    scene pri5_img9 with dissolve

    pause

    c "Mas é de verdade rsrs..."

    mc envergonhado "Digo, parece que não é um cenário. Que a gente realmente tá nesse lugar."

    c "Brincadeira. Eu entendi. Bem legal, né?"

    mc normal "Muito."

    c "Esse pessoal aí são figurantes. Eles ficam vários minutos parados ou andando pra lá e pra cá enquanto gravamos as cenas."

    c "Não é um trabalho fácil."

    mc normal "Imagino. Mas tá realmente incrível."

    ag "E quem é esse?"

    c "Ah!"

    scene black with dissolve

    scene pri5_img10 with dissolve

    pause

    ag "Bom dia."

    $ ag_nome = "Ágata"

    c "Bom dia, [ag]. Tudo bem?"

    ag "Estou sim. E quem é esse rapaz?"

    if priscila_namoro:

        c "Ah! É só um amigo meu que queria ver a cidade cenográfica."

        "Amigo, é? De novo isso?"
    else:


        c "É um amigo meu que mora na ilha."

    ag "Hmmm... amigo, né?"

    mc desconfiado "?"

    ag "Então tá. Vou lá me preparar. Foi bom ver você, [c]."

    c "Até mais, [ag]."

    ag "E você? Como é seu nome?"

    mc normal "[mc]."

    ag "Foi um prazer."

    menu:
        "Até.":


            mc normal "Até mais."
        "O prazer é todo meu.":


            mc charmoso "O prazer é todo meu."

            ag "..."

    mc desconfiado "Ela é coadjuvante?"

    scene black with dissolve

    scene pri5_img9 with dissolve

    c "Assim, ela não é coadjuvante, mas também não é uma protagonista."

    c "Nem todo mundo pode ter o papel principal."

    mc charmoso "Como se acha..."

    c "Hehe."

    "Homem" "Bom dia, [c]. Pronta pra começar?"

    c "[gus]. Bom dia..."

    scene black with dissolve

    scene pri5_img11 with dissolve

    pause

    gus "Oh. Vejo que você trouxe seu amigo."

    c "Si-sim."

    gus "Bom dia, [mc]. É [mc], né?"

    menu:
        "Bom dia.":


            mc serio "Bom dia."

            c "..."
        "...":


            mc serio "..."

            c "[mc]..."

    gus "Já faz um tempo que vocês se viram na praia aquela vez."

    c "Verdade..."

    "Praia? Será que ele não sabe sobre o que aconteceu no viaduto?"

    gus "Estão todos esperando você para iniciarmos. Você está uns minutos atrasada."

    c "Desculpa, [gus]."

    gus "Não tem problema. Só vamos começar o quanto antes."

    c "Ok."

    gus "Hoje quero refazer algumas cenas pontuais que não ficaram tão legais na edição."

    c "Foi algo que eu fiz?"

    gus "Não. Nada disso. Pode ficar tranquila. Só estamos buscando o melhor resultado possível, não é mesmo?"

    c "Sim. Quero dar o meu melhor."

    gus "Assim que se fala. Pode ter certeza que o filme será um sucesso."

    gus "Vou deixar vocês se despedirem e preparar tudo para você começar a gravar."

    gus "Não esqueça de falar com a figurinista e ajeitar o look. Reveja suas falas com o suporte e vamos aquecer um pouco antes."

    c "Ok. Pode deixar, [gus]. Obrigada."

    gus "Com licença."

    if p3_confissao:

        "Como é possível isso? Como ela pode agir de forma tão... casual... na frente desse monstro?!"

        "Ele fala como se fosse um amigo preocupado com o desempenho dela."

        "Esse maldito estuprador!"

        mc bravo "..."

        scene black with dissolve

        scene pri5_img12 with dissolve

        c "[mc]..."

        mc "..."

        c "[mc]! Ei!"

        mc desculpa "Oi... desculpa..."

        menu:
            "Eu vou matar esse velho.":


                mc bravo "Eu vou matar esse velho, [c]. Se eu ficar cinco minutinhos sozinho com ele. Eu mato ele..."

                c "Por favor, não fale isso! Por favor, [mc]!"

                mc angustiado "Mas [c]?!"

                c "Isso é coisa minha. Eu... nem sei o que falar pra você. Se uma coisa dessas acontecer, minha carreira pode acabar."

                mc desculpa "[c], isso é mais sério do que tudo isso. Eu tô falando da sua segurança!"

                c "Por favor, chega. Depois a gente vai falar mais sobre isso."

                mc "Droga..."

                c "E obrigada por entender."

                "Entender o quê? Eu não entendo porra nenhuma!"
            "Tá tudo legal.":


                mc desculpa "Tá tudo legal."

                mc "Não consigo ver esse cara e ficar de boa, [c]. Não depois daquele dia."

                c "Eu sei. Mas... não sei o que dizer. Só, por favor, não vai fazer nenhuma loucura."

                mc "Tá..."
            "...":


                mc serio "..."

                c "..."
    else:


        scene rua magica with Dissolve(1.0)

        "Depois da ameaça daquele [mar] no viaduto, eu fico pensando qual é a desse diretor."

        "O que será que tá rolando?"

    c "Eu vou lá gravar a cena, ok? Fique à vontade pra me ver ou, se tiver chato, pode ir conhecer os outros lugares ou até ir pro camarim."

    mc desculpa "Ok."

    scene rua magica with Dissolve(1.0)

    "Esse velho acabou com o clima."

    "..."

    if p3_confissao:

        "Pelo jeito da [c], ela ainda deve tá transando com esse paspalho."

        "Sei lá, mano. Que caralho. Nem sei o que pensar sobre isso."

        "Ela parecia tão mal na praia, e principalmente lá no lixão. Tive medo que ela fizesse o pior naquela noite."

        if priscila_namoro:

            "Mas parece que nosso namoro deu uma nova energia pra ela."
        else:


            "Mas parece que nossa amizade deu uma nova energia pra ela."

        "Esse é um assunto muito delicado. E {b}minhas ações podem mudar pra sempre nossa relação{/b}."

        "E o pior é que se eu ficar pensando demais nisso, só vai acabar com esse dia incrível que eu tô passando com ela."

        "Tenho que manter a cabeça no lugar, ou só vou piorar tudo."

    "Opa!"

    "Parece que ela tá pronta pra gravar."

    scene priscila rua_magica with Dissolve(2.0)

    pause

    "Que bacana isso tudo! Nem acredito que dá pra eu acompanhar a gravação do filme desse jeito."

    "O que será que vai rolar?"

    gus "[c]! Vamos refazer igual da outra vez, ok?"

    c "Ok!"

    gus "Você chega na cidade pedindo informações sobre o orc e o sentinela te dá as coordenadas, te mandando para o Vale dos Orcs."

    gus "É uma cena simples, mas precisamos fazer de forma que a cidade pareça viva."

    gus "Coadjuvantes em posição, por favor!"

    gus "Espera! Você de verde. Você tá interessada na conversa delas. Tente mostrar isso por meio do olhar."

    gus "Vamos fazer três vezes!"

    scene black with dissolve

    "{b}Meia hora depois{/b}"

    scene rua magica2 with Dissolve(1.0)

    pause

    "Bem complicada a gravação. Eles olham cada pequeno detalhe."

    "Opa, a [c] tá vindo pra cá."

    scene black with dissolve

    scene pri5_img12 with dissolve

    c "Oi."

    mc normal "Olá. O que foi?"

    c "Tá muito chato?"

    mc "Que nada. Eu gostei bastante de ver."

    mc charmoso "Ainda mais porque era você lá."

    scene pri5_img9 with dissolve

    c "Haha! Seu Casanova."

    mc desconfiado "Casanova?"

    c "Deixa pra lá."

    c "Eu ainda vou refazer mais uma ou duas vezes essa cena. Por que você não dá uma volta pelo set? Tem bastante coisa pra ver."

    mc normal "Mas deixar você?"

    c "Eu vou ficar mais tranquila se você estiver passeando de boa."

    mc "Se você não liga, então vou dar uma andada por aí. Aproveitar meu tempo aqui."

    c "Isso!"

    if priscila_namoro:

        c "{size=12}Beijos, namorado.{/size}"

        mc charmoso "Beijo."
    else:


        c "Até daqui a pouquinho."

        mc normal "Até."

    scene black with dissolve

    scene rua magica2 with Dissolve(1.0)

    "Certo. Deixa eu dar uma olhada por aqui e ver pra onde eu vou."

    "Tem três lugares que eu posso visitar. Dar uma olhada melhor na {b}Cidade Mágica{/b}, ou ir pro {b}Vale dos Orcs{/b} ou a {b}Ponte de Dehor{/b}."



    "Pelo tempo que ela levou pra fazer as duas cenas, e agora ela vai fazer mais duas... eu calculo que dá pra eu visitar {b}dois lugares{/b}."

    label priscila_e5_visita_menu:

        if p5_visita == 0:

            "Então eu tenho tempo pra visitar dois pontos da cidade cinematográfica."

            "Preciso escolher bem."

        elif p5_visita == 1:

            "Posso visitar só mais um lugar."
        else:




            "Ixi. Acabou meu tempo. A [c] já deve ter gravado as cenas e eu quero chegar antes dela. Tenho que ir pro camarim."

            jump priscila_e5_surpresa

        $ p5_visita += 1

        "Pra onde que eu vou agora?"

        menu:

            "Continuar na cidade {b}Cidade Mágica{/b}" if not p5_cidade:

                $ p5_cidade = True

                "A cidade mágica é impressionante. Quero dar uma olhada melhor nisso tudo."

                jump priscila_e5_cidade

            "Visitar o {b}Vale dos Orcs{/b}" if not p5_vale:

                $ p5_vale = True

                "Vou dar uma olhada nesse Vale dos Orcs. Tomara que não tenha uma criatura assassina de verdade lá."

                mc angustiado "..."

                scene black with dissolve

                "..."

                jump priscila_e5_vale

            "Visitar a {b}Ponte de Dehor{/b}" if not p5_ponte:

                $ p5_ponte = True

                "Fiquei interessado nessa tal de Ponte de... Dehor. O que será que é 'Dehor'?"

                "Bora lá."

                "..."

                jump priscila_e5_ponte







label priscila_e5_ponte:

    scene ponte dehor with Dissolve(2.0)

    pause

    "Que lugar bacana! É tipo a entrada para uma cidade cercada por um muro gigante."

    "Ainda não acredito que eles criam tudo isso pro filme..."

    "A quantidade de dinheiro que eles investem nessas coisas é demais pra gente normal entender."

    show hero ola with dissolve

    he "Oi. Você é da produção?"

    mc normal "Opa. Não. Sou só um convidado. Estou conhecendo os sets de filmagem."

    he "Ah, ok. Estou precisando de uma ajuda pra polir minha espada."

    he "O pessoal da produção ficou de ver isso pra mim para as cenas que eu vou regravar hoje."

    mc normal "Entendi. Caraca, que massa. Uma espada..."

    he "Pra você que é só um visitante deve parecer coisa de outro mundo."

    mc envergonhado "Pior que você tem razão."

    he "Relaxa que você vai se acostumar logo. Você é convidado de quem?"

    mc normal "Da [cc]."

    he "Da hora. A [c] é uma garota incrível. Ela é linda, engraçada e tem um ar super inocente."

    if priscila_namoro:

        "Não tô gostando do jeito que esse cara fala dela."
    else:


        "Se eu fosse namorado dela, já dava um sopapo nesse sujeito."

    he "Nós vamos gravar uma cena juntos em breve. Mas ainda estão preparando tudo. Vai ser uma das últimas cenas do filme."

    he "Estamos só esperando o diretor resolver tudo."

    mc "Entendi. Você conhece bem o diretor [gus]?"

    he "Já fiz alguns trabalhos com ele. Mas este é o primeiro que serei um personagem importante."

    he "O diretor é alguém extremamente talentoso, além de ter me ajudado bastante a começar a carreira."

    mc desconfiado "Você sabe por que ele sempre escolhe garotas jovens pra serem as protagonistas dos filmes?"

    he "É... pior que nem sei."

    he "Bom. Vou ir lá resolver o problema da espada."

    mc normal "Ok. Foi um prazer."

    he "Falou."

    hide hero with dissolve

    if p3_confissao:

        "Todos falam bem do [gus]. Será que ninguém sabe o que ele fez com a [c]?"

        "Não é possível que todos eles tenham sido comprados por esse idiota."

    "Bom, deu pra dar uma boa olhada. Melhor eu continuar."

    jump priscila_e5_visita_menu

label priscila_e5_cidade:

    "..."

    scene rua magica3 with Dissolve(2.0)

    pause

    "Uou. Tem outros coadjuvantes aqui. Parece que eles vão gravar alguma coisa aqui depois."

    "Aquelas duas que tavam lendo o livro vieram pra cá agora."

    "E tem uma orc andando ali."

    "Mano, e tem dois elfos passeando pela cidade e um anão descendo as escadas."

    "Tipo... é como se eu tivesse em um cenário de Dungeons & Dragons."

    "Talvez aquele elfo arqueiro seja o Silverleaf Halfmoon..."

    "De vez em quando eu sou mesmo muito nerd."

    scene pri5_img14 with Dissolve(1.0)

    ag "Veja se não é o amiguinho da [c]."

    mc envergonhado "Haha... você me assustou."

    ag "O que tá fazendo sozinho aqui?"

    mc normal "Tô só conhecendo melhor a cidade cenográfica."

    ag "Sei..."

    mc normal "E você... é... já fez muitos filmes?"

    ag "Sério que você não me conhece?"

    menu:
        "Tentar lembrar quem é ela":


            "Quem será que é essa aí?"

            "Não faço ideia... nem adianta tentar eu acho..."

            "Hmm..."
        "Secar o corpo dela":


            "Hmm..."

            show pri5_img15 with dissolve

            pause

            "Acho que eu lembraria dessa barriguinha..."

            "É meio tábua, mas é linda assim..."

            "Será que tem alguma chance de rolar alguma coisa?"

            if priscila_namoro:

                "O que eu tô pensando? Eu tô namorando a Pri."

            ag "Hm... o que tanto você tá procurando aí?"

            hide pri5_img15 with dissolve

            mc envergonhado "Opa..."

    mc desconfiado "Agora que você falou... eu acho que já te vi."

    ag "Eu fui a estrela do último filme do diretor [diretor]!"

    ag "Claro que eu tava diferente, mas achei que..."

    mc surpreso "Nã-não! É que eu não vejo muito filme! E mesmo assim reconheci!"

    ag "..."

    "Ela ficou triste de verdade..."

    ag "Agora ele só tem olhos pra [c]..."

    mc desculpa "Sei..."

    if p3_confissao:

        mc desculpa "É... quantos anos você tem?"

        ag "Ah?"

        ag "Tenho 20. Por que?"

        "Hmmm... perto da idade da [c]. E ela foi a protagonista do filme anterior. Será que..."

        mc charmoso "É que você é muito bonita. Com todo o respeito."

        ag "Valeu. Haha! Vou conta pra [c] que você tá me cantando."

        mc envergonhado "Ei..."

        ag "Brincadeira. Obrigada pelo elogio."

    scene black with dissolve

    scene pri5_img16 with dissolve

    pause

    ag "Bom, vou lá me preparar que logo vou refazer algumas cenas."

    mc normal "Ok. Foi uma honra conhecer uma estrela."

    ag "Sei..."

    ag "Estarei aqui nos próximos meses gravando. Se quiser conversar mais algum dia, com mais tempo."

    menu:
        "Claro.":


            mc charmoso "Claro. Vamos sim."

            ag "Ok. Tchau."
        "Vou indo nessa também.":


            mc normal "Vou indo nessa também. Boa filmagem."

            ag "Até."

    scene rua magica3 with Dissolve(1.0)

    "Muito massa poder conversar com essas pessoas famosas. A [c] realmente faz parte de um círculo bem diferenciado."

    "Bom, e agora?"

    jump priscila_e5_visita_menu

label priscila_e5_vale:

    scene ilha vale with Dissolve(1.0)

    pause

    "Caraca. Isso aqui é de verdade, né? Não é possível que seja só um cenário..."

    mc desconfiado "Parece que eu tô ouvindo um barulho."

    scene pri5_img13 with vpunch

    pause

    orc "Boa tarde."

    mc angustiado "ÃÃÃHHN?!"

    orc "Perdão. Te assustei?"

    mc envergonhado "Claro, pô. O que é você?"

    orc "Como assim? Estou só aqui treinando pra cena que vamos gravar durante a tarde."

    mc desconfiado "Acho que entendi."

    orc "Se eu conseguir ir bem nesse papel, tenho certeza que muitas portas vão se abrir pra mim."

    orc "O [gus] é um grande diretor. E ele sabe ver o talento nas pessoas de verdade."

    if p3_confissao:

        "Como é? Esse cara tá falando sério?"

        mc desconfiado "Verdade?"

        orc "Sim. Este é o primeiro filme que eu faço com ele, mas é fácil ver o quanto ele é profissional."

        mc desconfiado "Mas por que todos os filmes dele é uma jovem que faz o papel principal?"

        mc "Você é um rapaz, né? Não se sente um pouco excluído trabalhando com ele?"

        orc "Ah... com certeza existe uma razão pra isso..."

        orc "Deve ser uma questão de história que nós... não entendemos."

        "Nem ele acredita no que tá falando."

    orc "Bom, vou indo nessa. Tenho que treinar um pouco mais."

    mc normal "Ok. Foi muito legal ver um personagem assim, vestido de uma forma tão real."

    orc "Vestido?"

    mc desconfiado "É... bom, deixa pra lá."

    orc "Até."

    scene black with dissolve

    scene ilha vale with Dissolve(1.0)

    "Cara estranho."

    "Bom, deixa eu dar uma olhadinha por aqui e depois dar o fora."

    "..."

    mc desconfiado "Ah?"

    scene cenario gadget_gama with Dissolve(2.0)

    if not gadgetgama or not persistent.gadgetgama:

        "Opa!"

        mc desconfiado "Que merda é essa brilhando?"

        $ persistent.gadgetgama = True
        $ gadgetgama = True

        play sound "extra/carta.mp3"

        show gadget_gama with dissolve

        "{b}[mc] encontrou Gadget Gama{/b}"

        "{b}Gadget Gama é um Item Especial. Itens especiais ficam com você mesmo que você reinicie o jogo.{/b}"

        "{b}Você só perde um Item Especial se você desinstalar o aplicativo e não salvar seu jogo na nuvem.{/b}"

        "{i}zzzzkkkk{/i}"

        "{i}tccchhhkkkk{/i}"

    if not gadgetgama and persistent.gadgetgama:

        $ gadgetgama = True

        "{b}Você já encontrou o Gadget Gama jogando anteriormente.{/b}"

        "{b}Itens especiais ficam salvos mesmo que você reinicie o game, por isso não é preciso pegá-los novamente.{/b}"

    if (persistent.gadgetbeta or gadgetbeta) and (persistent.gadgetalfa or gadgetalfa):



        "Eu consegui três pessas parecidas..."

        "Elas tão brilhando. Assim que eu voltar pra ilha eu preciso ver o que isso significa."
    else:


        "{i}Trying to connect to HQ...{/i}"

        "{i}Missing components{/i}"

        "{i}Please locate all Gadgets before trying to connect.{/i}"

        "{i}tccchhhkkkk{/i}"

        mc surpreso "Uou! Esse negócio falou alguma coisa!"

        if (persistent.gadgetbeta or gadgetbeta) or (persistent.gadgetalfa or gadgetalfa):

            mc desconfiado "Ele disse que eu preciso encontrar todos os {b}gadgets{/b} antes de tentar conectar alguma coisa."

            "Esse treco parece com o outro que eu encontrei aquele dia à noite procurando a [c]."
        else:


            mc desconfiado "Parece que eu preciso encontrar outros dois trecos antes de fazer alguma coisa..."

        "{b}Existe uma história secreta caso você encontre três gadgets. Caso queira ver, viva novamente encontros da [c] e procure as outras peças{/b}"

    scene ilha vale with Dissolve(1.0)

    "Caraca. Acho que gastei tempo demais aqui."

    "Tenho que continuar antes que fique tarde demais."

    jump priscila_e5_visita_menu

label priscila_e5_surpresa:

    scene black with dissolve

    "..."

    "Quero chegar antes dela no camarim e surpreender ela."

    "Ela deve tá cansada depois de gravar. Posso até fazer uma massagem nela."

    scene camarim geral with Dissolve(1.0)

    "Sorte que eu encontrei o caminho. Era muito fácil eu me perder a acabar no camarim de outra pessoa."

    mc envergonhado "Eu ia parar na Consigo..."

    mc zerado "Ou talvez até a [j] que publicasse..."

    "Deixa eu entrar."

    scene camarim interior with Dissolve(1.0)

    mc normal "Boa! Ela não tá aqui ainda."

    "Caralho! Toda essa andada e o nervosismo tão me deixando com vontade de cagar. Será que é uma boa fazer isso aqui?"

    "Mano do céu... e se o bagulho ficar fedendo?"

    mc angustiado "Não consigo segurar!"

    scene black with dissolve

    scene mc camarim_banheiro with Dissolve(1.0)

    mc "Uuh... Me desculpa [c]..."

    "..."

    "Vou dar um tempo aqui, assim sai pela janela e não vai pro resto do camarim."

    "..."

    "{i}grrraakkk{/i}"

    mc "!"

    "Acho que alguém abriu a porta!"

    gus "O idiota não está aqui."

    c "Não chama ele assim."

    gus "Ver vocês juntos me deixou muito irritado, mocinha."

    c "..."

    label pri5_gustav_premium:

        pass

    "Meu Deus... é o idiota do diretor... o que eu faço?"

    menu:
        "Espiar eles conversando":


            if not premium:

                call mensagem_premium from _call_mensagem_premium



















                jump pri5_gustav_premium

            "Eu não aguento. Eu tenho que dar uma olhada."

            scene black with dissolve

            scene pri5_img17 with dissolve

            pause

            gus "Você vai ter que me compensar por isso agora mesmo."

            c "Sai..."

            gus "Não comece, [c]. Eu não vou aceitar esse seu 'tempo' por muito mais, não."

            c "..."

            gus "Você vai cumprir sua parte do acordo ou a [ag] vai muito bem tomar seu lugar."

            c "Não..."

            gus "Então só fica quieta."

            "Meu coração... vai sair pela boca..."

            "O que eu faço?! O que eu faço porra?!"

            scene black with dissolve

            scene pri5_img18 with dissolve

            pause

            c "Eu disse sai..."

            "..."

            c "Eu tenho que ir no Vale dos Orcs gravar agora..."

            gus "Você não manda nada aqui. Quer que eu chame o [mar]?"
            scene pnew_ani07 with Dissolve(1.0)
            c "Não!"

            gus "Acho bom."

            "..."

            gus "Isso..."

            "Minhas pernas tão tremendo..."

            scene pri5_img19 with dissolve

            pause

            gus "Assim mesmo... igual sempre... minha princesa guerreira..."

            c "[gus]... hm..."

            gus "Eu sei que você vai gostar..."

            c "Não..."

            gus "Claro que vai... é só um pouco... e tudo vai dar certo..."
            scene pnew_ani08 with Dissolve(1.0)
            c "P-por favor..."

            gus "Você é minha..."

            "Não! Eu tô com cagaço..."

            "Só que... eu não posso ficar aqui ouvindo isso!"

            "Eu tenho que ajudar a Pri! Ninguém pode ver uma coisa dessas e não fazer nada!"

            "Eu vou-"

            c "NÃÃOOO!"

            scene mc camarim_banheiro with hpunch

            "{i}TUDUMP{/i}"

            gus "Ai!"

            c "Agora não!"

            "{i}grrraakkk{/i}"

            gus "Volta aqui, sua PUTA!"

            gus "Ai..."

            gus "Sua puta desgraçada... você acha que vai fugir de mim?"

            gus "..."
        "Só escutar sentado":


            gus "Você vai ter que me compensar por isso agora mesmo."

            c "Sai..."

            gus "Não comece, [c]. Eu não vou aceitar esse seu 'tempo' por muito mais, não."

            c "..."

            gus "Você vai cumprir sua parte do acordo ou a [ag] vai muito bem tomar seu lugar."

            c "Não..."

            gus "Então só fica quieta."

            "Meu coração... vai sair pela boca..."

            "O que eu faço?! O que eu faço porra?!"

            c "Eu disse sai..."

            "..."

            c "Eu tenho que ir no Vale dos Orcs gravar agora..."

            gus "Você não manda nada aqui. Quer que eu chame o [mar]?"

            c "Não!"

            gus "Acho bom."

            "..."

            gus "Isso..."

            "Minhas pernas tão tremendo..."

            "Só que... não posso ficar aqui ouvindo isso!"

            "Eu vou-"

            c "NÃÃOOO!"

            scene mc camarim_banheiro with hpunch

            "{i}TUDUMP{/i}"

            gus "Ai!"

            c "Agora não!"

            "{i}grrraakkk{/i}"

            gus "Volta aqui, sua PUTA!"

            gus "Ai..."

            gus "Sua puta desgraçada... você acha que vai fugir de mim?"

            gus "..."

    $ priscila_segredo = True

    if p3_confissao:

        "Esse velho... desde que a [c] me contou aquilo na praia."

        "Depois do que o [mar] fez no viaduto..."

        "Como pode?! Eu vou matar esse velho!"
    else:


        "Que porra é essa?!"

        "Esse velho tá assediando a [c]?! Como eu nunca..."

        "Espera... lá na praia..."

        scene priscila praia_sentados

        show black

        show black with Dissolve(1.0):
            alpha 0.5

        c "Desculpa se eu sou uma garota complicada..."

        c "Eu queria que as coisas fossem mais simples, [mc]."

        c "Mas é tudo tão complicado. Eu tenho tanta vontade de chorar."

        mc "Você pode chorar, [c]. Pode falar o que tá sentindo."

        c "Não sei se eu posso..."

        c "Você é tão sexy e charmoso. Eu fico sem ar, meu peito fica quente."

        mc "Eu sinto a mesma coisa."

        c "Mas tenho medo de estragar isso com meus problemas."

        scene mc camarim_banheiro with Dissolve(1.0)

        "Depois disso... quando ele foi procurar ela na praia..."

        "E tudo o que aconteceu aquela noite no lixão!"

        "Como... eu nunca percebi?!"

        "Eu sou um idiota!"

        "E esse velho FILHO DE UMA PUTA é o culpado de tudo isso!"

    "Eu tô tremendo... o que eu faço?"

    menu:
        "Não posso me intrometer. Tenho que confiar na [c].":


            "Não! Eu tenho que confiar na [c]! Se eu me intrometer posso acabar com tudo o que ela conquistou."

            "Não posso ferrar com as coisas dela só porque eu acho que é o certo."

            "Mas eu vou deixar esse cretino continuar fazendo isso?! Ameaçando ela desse jeito?!"

            "Que merda..."

            gus "Ela vai ver..."

            gus "Você não pode fugir de mim pra sempre, [c]."

            "..."

            "Acho que ele saiu fora."

            "Será que eu fiz a escolha certa? Talvez a [c] esteja precisando de ajuda."

            "Mas se eu ferrar a vida dela agindo de forma impensada, posso atrapalhar mais do que ajudar."

            "..."

            jump priscila_e5_continua
        "Não aguento ficar aqui. Ele vai se ver comigo.":


            $ conversou_gustav = True

            mc "Não vou só ficar aqui ouvindo esse cretino."

            scene black with Dissolve(1.0)

            "Tudo que eu queria era cinco minutos com ele. Só pode ser um presente dos céus."

            jump priscila_e5_gustav

label priscila_e5_gustav:

    "{i}grrraakkk{/i}"

    scene camarim interior2 with Dissolve(1.0)

    mc bravo "[gus]..."

    gus "?"

    show gustav malicioso with dissolve

    gus "Então você estava aqui?"

    mc irritado "Eu sei de tudo, seu verme!"

    gus "Eu sei que a [c] pode ter te contado, mas e daí?"

    mc bravo "Como assim e daí? Eu posso acabar com sua vida!"

    gus "Haha... que frase curiosa..."

    gus "[mc]... Você pode tentar acabar com minha vida de forma figurada. Já eu posso acabar com sua vida de forma bem literal."

    show gustav explicando with dissolve

    gus "Eu não suporto você, seu... sua criatura inútil."

    gus "Não suporto que a [c] sinta alguma coisa por você. Você só profana ela. Você não merece que ela sinta algo por você."

    gus "Você não passa de um qualquer. Você não faz parte do mundo dela, ou do meu. Você é um ninguém que trabalha para comer."

    gus "Ninguém te convidou para este mundo. Ninguém quer você aqui."

    menu:
        "Tô cagando e andando pro que você acha de mim.":


            mc tarado "Sabe o que vale sua opinião pra mim? Merda nenhuma, seu velho nojento."

            mc serio "Pode falar o que quiser. É de mim que a [c] gosta."
        "...":


            mc bravo "..."

            gus "..."
        "E você é um velho estuprador.":


            mc irritado "Você não passa de um velho estuprador! O que pode falar de mim?!"

            mc "Fale pelos cotovelos enquanto pode, seu puto!"

    mc bravo "O que você faz com a [c] é nojento, é pervertido, é simplesmente imperdoável. Você é um coitado que precisa disso."

    gus "Não passa de um tolo. Eu tenho dó de você."

    mc serio "..."

    show gustav malicioso with dissolve

    gus "Você acha que alguém obrigou a [c] fazer isso? Acha que o [mar] apontou uma arma na cabeça dela e forçou ela a aceitar?"

    gus "Ela aceitou porque quis. Porque ela sabe como as coisas funcionam. A [c] sempre soube do que é preciso pra crescer."

    gus "Sempre foi uma boa garota, mas ela mudou... depois que viu você..."

    gus "Você colocou coisas na cabeça dela e ela desviou do caminho."

    gus "Mas isso não vai durar. Logo ela vai esquecer você e voltar pra mim."

    gus "Eu sei que no fundo ela gosta disso. Isso excita ela."

    "Olha as merdas que esse velho tá falando!"

    gus "Ela gosta de bancar a certinha, mas no fundo ela gosta de dar pra mim."

    mc concentrando "Cala a boca."

    gus "Ela geme enquanto eu pego ela, aqui mesmo onde a gente está agora."

    mc irritado "Eu mandei calar a boca!"

    menu:
        "Socar a cara do [gus]":


            label priscila_e5_cenasocou:

                $ persistent.priscila_cena13 = True

            $ priscila_idiota += 3

            $ socou_gustav = True

            mc irritado "Seu filho da puta!"

            scene mc soco_gustav with vpunch

            pause

            gus "Argh!"

            "Toma essa, seu corno!"

            "Espero que você caia e quebre o pescoço. Ninguém vai sentir saudades de você!"

            scene camarim interior2 with vpunch

            gus "Maldito..."

            gus "Tá se achando..."

            show gustav gritando with hpunch

            gus "Você é louco?!"

            mc irritado "O louco aqui é você. Nunca mais abra sua boca suja pra falar da [c] na minha frente."

            gus "..."

            show gustav explicando with dissolve

            gus "..."

            gus "Isso não vai ficar assim."

            gus "..."

            gus "Adeus, [mc]."

            hide gustav with dissolve

            "{i}grrraakkk{/i}"

            "Não acredito. Consegui. Eu soquei a fuça desse velho. E ainda saiu barato pra ele."

            "Espero que ele pense duas vezes antes de mexer com a [c]."

            "Eu tô tremendo até agora... meu sangue tá quente. E agora?"

            "Eu tenho que encontrar a Pri. Isso! Boa ideia... Ela... ela disse que ia pra Vila dos Orcs."

            "Preciso ter certeza que o [gus] não vai descontar nel-"

            "{i}grrraakkk{/i}"

            mc desconfiado "?!"

            show marco chegando with dissolve

            mar "Boa tarde, [mc]."

            mc angustiado "Ma-Marco?!"

            mar "Você fez um belo trabalho no [gus]. O velho tá puto."

            mc bravo "..."

            mc "Tá fazendo o que aqui?"

            show marco explicando with dissolve

            mar "Vim fazer o trabalho sujo."

            mc irritado "Se você me matar, já sabe! Eu tenho as informações do velho com alguém na redação!"

            mar "Eu sei dessa possibilidade. E é só por isso que você vai continuar vivo."

            mc preocupado "Então deixa eu sair."

            mar "Foram essas ordens que eu recebi. Mas eu acho que você tá só blefando."

            mc irritado "Não brinque comigo, [mar]! Deixa eu sair!"

            mar "Isso não vai ser possível, [mc]. Você não devia ter socado o [gus]."

            $ renpy.end_replay()

            mc serio "Adeu-"

            jump priscila_e5_soco
        "Não perder a cabeça":


            "Merda! Porra! Caralho!"

            "Não posso deixar ele entrar na minha cabeça! Eu sei que ele só tá me provocando!"

            mc bravo "Você fala isso da boca pra fora. Nem você acredita nisso."

            mc "Você acha que conhece a [c], mas ela nunca foi verdadeira com você. O que você acha dela é uma mentira que você criou nessa cabeça doentia."

            mc irritado "Não importa o que você fale. Ela NUNCA vai sentir qualquer coisa por você. Só NOJO e ÓDIO!"

            gus "..."

            gus "Idiota..."

            hide gustav with dissolve

            "Não acredito que eu consegui... Consegui não bater nele."

            "[c]... espero que eu esteja fazendo a coisa certa."

            jump priscila_e5_continua

label priscila_e5_continua:

    "Eu ainda tô num encontro com ela. Ela não tem noção do que aconteceu."

    "Tenho que agir normalmente. Não posso deixar essas coisas acabarem com meu tempo com ela. O [gus] não vai ganhar."

    "Ela disse que tava indo pro Vale dos Orcs."

    if p5_vale:

        "Eu fui lá mais cedo. Sei como chegar."
    else:


        "Eu acabei não visitando lá, mas acho que sei o caminho."

    "Não vejo a hora de ver a [c]."

    $ tempo += 1

    scene black with dissolve

    "..."

    scene ilha vale with Dissolve(1.0)

    pause

    "Tem uma galera aqui."

    if p5_vale:

        "Aquele orc estranho tá aqui também. Mano... fico doido como ele parece de verdade."

    mc normal "Tô vendo ela!"

    mc "Priiii!"

    "..."

    show priscila a_feliz with dissolve

    c "Oi, [mc]!"

    c "Nossa, parece que faz tanto tempo que a gente não se vê. Mas faz uma horinha só."

    mc "Verdade. E como foi lá na cidade mágica?"

    show priscila a_exibida with dissolve

    c "Deu tudo certo. Eu sou eu, né?"

    if priscila_namoro:

        mc charmoso "Essa é minha namorada perfeita."

        c "Hehe."
    else:


        mc normal "Essa é minha garota."

        c "Hehe."

    show priscila a_feliz with dissolve

    c "Falta mais uma cena hoje e estamos prontos pra voltar, ok?"

    mc normal "Ok. Eu tô gostando bastante do passeio."

    "Tirando a parte que um velho maluco e nojento dá em cima de você."

    c "Tava com medo que você achasse tudo muito chato. Nem consigo dar atenção pra você."

    mc charmoso "Tá louca? Tá sendo incrível."

    c "Então, tá."

    gus "[c]. Estamos prontos."

    "Não acredito que esse idiota tá aqui também."

    show priscila a_exibida with dissolve

    c "Vou lá. Não tem cena sem a protagonista, né?"

    mc "Com certeza. Bom trabalho."

    c "Até daqui a pouquinho."

    hide priscila with dissolve

    gus "Orc, vem aqui. Vamos regravar a cena que ela encontra você depois de ter saído da cidade mágica."

    orc "Perfeito, diretor."

    gus "Vocês repassaram as falas com o suporte, né?"

    c "Sim. Estou pronta."

    gus "Perfeito. Todos em posição."

    gus "Câmera."

    "Câmera man" "Pronto."

    gus "Luz."

    "Rapaz" "Pronto."

    gus "Cena 21, Tomada 8, Fim dos Tempos. Rodando!"

    scene priscila vale_orc with Dissolve(2.0)

    pause

    c "Finalmente encontrei você, besta!"

    orc "{i}Shhhh Shhhh{/i}"

    c "Você vai pagar pelo que fez com a [ag] e todos os outros da cidade mágica!"

    orc "Fedelha inocente... você não sabe nada do que acontece no reino."

    c "Suas palavras são sujas como sua alma!"

    orc "Eles são os sujos. E você faz o serviço sujo deles, sem entender o que está fazendo."

    c "Não me venha com sua ladainha! Ela pode funcionar nos orcs idiotas, mas não comigo!"

    orc "Olhe a sua volta, guerreira. Enquanto os elfos dominam a riqueza e o conhecimento, o que sobra para os orcs e os humanos?"

    orc "Você não passa de uma ferramenta para eles. Você deveria estar do meu lado se não tivesse sido corrompida."

    c "Suas palavras podem soar bonitas, mas seus atos são repugnantes! Eu vou parar você aqui!"

    orc "Não tenho medo da morte. Mas ainda não é minha hora. Sua espada vai perfurar meu coração, mas não hoje."

    orc "Adeus, guerreira."

    gus "CORTA!"

    scene ilha vale with Dissolve(1.0)

    gus "Gostei bastante. Parabéns."

    gus "Agora vamos para quando ele te domina, [c]."

    c "Essa cena? Agora?"

    gus "Essa mesma."

    c "S-sim... senhor..."

    orc "Vem aqui."

    scene black with dissolve

    scene pri5_img20 with dissolve

    pause

    c "O-opa."

    gus "Você foi pega por ele e precisa tentar escapar, [c]. Você lembra como foi, certo? Só estamos fazendo novos takes."

    c "S-sim, senhor..."

    c "Você tá me apertando forte, senhor orc..."

    orc "Hm..."

    c "O-ok..."

    gus "Ação!"

    c "ME SOLTE!"

    orc "HUHUHU!"

    c "N-não! Não me esmague!"

    orc "Eu não vou te matar, garota! Eu vou fazer outra coisa com você..."

    c "NÃO!!!"

    scene pri5_img21 with vpunch

    pause

    c "A-ah!!!"

    orc "Certeza que você tá tentando escapar?"

    c "C-claro! Hmf!"

    orc "Você nunca vai se soltar de mim..."

    c "Eu vou s-"

    scene pri5_img22 with vpunch

    pause

    orc "HAHAHA!"

    c "Hm-hmg! A-ah!"

    orc "Você vai servir pra muita coisa em nossa floresta..."

    c "M-meus amigos vão me ajudar..."

    orc "VAMOS VER!"

    c "Ah... ah..."

    orc "Eu não vou parar aqui! Você vai ser minha, guerreira!"

    c "S-sua?!"

    orc "Você é linda demais! A humana mais bela que eu já vi!"

    orc "Você vai ser minha e dos meus irmãos! Ukh!"

    c "N-não!"

    orc "Vou te mostrar o que um orc pode fazer!"

    "Mentira! Eles vão fazer uma cena dessas aqui?!"

    menu:
        "Tentar chutar a câmera sem ninguém ver":


            play sound derrubou

            scene ilha vale with vpunch

            "Câmera" "EIII!"

            mc "O-ops!"

            gus "O que aconteceu?!"

            "Câmera" "D-desculpa, senhor... eu derrubei aqui."

            gus "Idiota!"

            mc "Hehe..."

            "O idiota tava tão focado que nem percebeu que fui eu... espero que ninguém tenha notado."
        "Não vou causar. Vamos ver a gravação":


            orc "Venha, mulher!"

            scene black with dissolve

            scene ani10 with Dissolve(1.0)

            pause

            c "A-aahh! Seu grosso! O que você tá fazendo?!"

            orc "Você vai ser minha!"

            c "A-ahnnn! N-nunca! Um... u-um bruto grosseiro igual você! Awnnn!"

            orc "Tem coisas que só um orc pode fazer com você, fêmea!"

            c "Aahn... não me chama... d-de fêmea! Eu... aah... não sou sua fêmea!"

            orc "Você vai ser quando eu te mostrar!"

            c "V-vai me mostrar?! O que..."

            menu:
                "CHUTAR a câmera de qualquer jeito!":


                    play sound derrubou

                    scene ilha vale with vpunch

                    "Câmera" "EIII!"

                    mc "O-ops!"

                    gus "O que aconteceu?!"

                    "Câmera" "D-desculpa, senhor... eu derrubei aqui."

                    gus "Idiota!"

                    mc "Hehe..."

                    "O idiota tava tão focado que nem percebeu que fui eu... espero que ninguém tenha notado."
                "Eu quero ver o que esse orc faz com ela...":


                    orc "Toma, princesa!"

                    scene ani21 with vpunch

                    pause

                    c "Awwnnnhghh!"

                    orc "Tá sentindo o poder dele, minha fêmea!"

                    c "A-ahnnn! Seu monstro! C-com esse negócio aí!"

                    c "Nenhum homem jamais! Aaahhnnn!"

                    orc "Eu disse que só orcs podem fazer! HAHAHA!"

                    c "A-ahhn! Grosseirão! Ahnnn! Me pegando forte assim!"

                    "Uau..."

                    "Imagina o que um orc de verdade faria com a Priscila?"

                    "Eu... jamais ia conseguir competir com uma coisa dessas..."

                    c "Aainn! AINNN! Monstro! Vaiii!"

                    gus "Eeee.... CORTA!"

                    scene black with dissolve

                    scene ilha vale with Dissolve(1.0)

    gus "Cinco minutos e faremos novamente."

    "Mano... que porra de filme é esse?"

    "Uma pessoa com a mente poluída já ia pensar besteira de tudo isso aí..."

    c "[mc]! Vem aqui!"

    mc normal "Opa."

    "..."

    scene priscila vale_mc with Dissolve(2.0)

    pause

    mc "Você foi incrível."

    c "Sério? Gostou mesmo?"

    mc "Tipo, parecia que você tava falando de verdade. E ainda mais com esse orc super real..."

    c "Eu me esforço bastante pra entrar na personagem. Eu sou uma guerreira humana contratada pelos elfos pra matar os orcs."

    c "Tenho que entrar na personagem."

    mc "E você conseguiu. Falando nisso, achei bem interessante a história. Tem como eu saber mais sobre isso?"

    c "Verdade? Gostou?"

    mc "Sim. Não sou aquele fissuraaaaado, mas até que eu gosto de coisa de fantasia."

    c "Eu também gosto um pouco. Mas não muito rs"

    mc "Você prefere uma comédia romântica, né?"

    c "Você ainda lembra..."

    mc "Claro."

    if ep_pontos > 1:

        mc "Eu acertei ou não aquelas [ep_pontos] perguntas sobre você?"

        c "Acertou mesmo. Nem acredito..."

        mc "Pra você saber o quanto você é importante pra mim."

        c "Seu fofo..."

    c "Sabe, [mc]? Quando eu era mais nova, eu sempre achei que ia encontrar um príncipe."

    c "Um cara especial que fosse me tratar igual uma princesa, que ia ser bonito, charmoso, rico..."

    scene priscila vale_mc_confissao with Dissolve(2.0)

    pause

    c "Só que eu cresci e comecei a ver que as coisas não eram assim..."

    c "Eu não era uma princesa e os homens que eu convivia não eram príncipes."

    c "E foi daí pra pior. Aquele dia no bar eu tava ruim, mas daí na praia eu me senti bem de novo. Foi um dia especial."

    c "Só que do mesmo jeito que você me mostrou que existia, sim, um príncipe, você me mostrou que eu não tinha direito..."

    c "Eu... não tinha direito de ser princesa. Não depois de tudo o que eu fiz."

    c "Por isso eu fugi. Por isso você teve que ir me buscar no lixão, igual uma... sei lá... uma barata."

    c "Desculpa falar tudo isso... nem sei se eles tão ouvindo..."

    c "Mas só queria te pedir desculpas. Desculpa por não ser uma princesa."

    mc "[c]..."

    mc "Sabe... acho que você continua sendo aquela garota de antes."

    c "Como assim?"

    mc "Vindo pra capital eu entendi que não existe príncipe também. E eu tô muito longe disso."

    mc "Eu... eu vendi meus amigos pra revista."

    if priscila_atencao > 0:

        $ priscila_idiota += 1

        mc "Inclusive, você viu a matéria lá no noticiário, né?"

        mc "Eu descobri sobre seu filme xeretando seu celular aquele dia no bar."

        mc "Você tava dormindo no meu colo e eu só pensando em me manter no emprego."

        c "Isso realmente não foi legal."

    if cassia_aceitou:

        mc "Eu ainda me aliei à pior jornalista que eu já vi na minha vida."

        mc "Corrompi minha ética só pensando no meu benefício."

    mc "Eu tô muito longe de ser o príncipe que você acha que eu sou."

    c "..."

    mc "E qual é o problema? Qual o problema se a gente não é perfeito? Se às vezes a gente erra?"

    mc "Eu não ligo se você fez alguma coisa que se arrepende. Isso não muda o quão especial você é pra mim."

    c "Tá. Eu também não ligo se você fez alguma coisa de errado. Você ainda é um príncipe."

    if priscila_namoro:

        c "Você é meu príncipe."

        "O clima tá muito bom. Até esqueci que a gente tá no set de filmagem."

        "Agora pode ser a hora que eu esperei o dia todo. E ainda na frente do [gus]."

        "O que será que a [c] vai achar? Será que eu faço isso?"

        menu:
            "Beijar a [c]":


                label priscila_e5_replaybeijo:

                    scene priscila vale_mc_confissao

                    $ persistent.priscila_cena14 = True

                $ priscila_e5 = "namoro"

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("priscila_e5_namoro","priscila","personagem")

                $ p5_beijo = True

                mc "Eu não aguento, [c]..."

                c "Como?"

                c "Opa!"

                scene priscila vale_mc_beijo with Dissolve(2.0)

                pause

                c "Hmmm..."

                c "[mc]..."

                c "A gente... não..."

                mc "..."

                window hide

                pause

                $ renpy.end_replay()

                if priscila_idiota <= 0:

                    label priscila_e5_replaybeijoextra:

                        scene priscila vale_mc_beijo

                        $ persistent.priscila_cena15 = True

                    c "Me beija mais."

                    scene priscila vale_mc_beijo2 with Dissolve(2.0)

                    pause

                    c "Hmmm..."

                    c "Eu adoro te beijar, [mc]."

                    c "Foda-se gravação, foda-se o [gus]. Só me beija."

                    mc "Sim."

                    window hide

                    pause

                    $ renpy.end_replay()
            "Não beijar a [c]":


                "É perigoso demais beijar ela aqui na gravação. Na frente de todas essas pessoas."

                "Ela mesmo disse que seria ruim pra controlar as notícias depois."

                "Não posso me aproveitar da fraqueza dela."

                jump priscila_e5_amizade
    else:


        label priscila_e5_amizade:

            $ priscila_e5 = "amizade"

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("priscila_e5_amizade","priscila","personagem")

            c "Deixa eu pegar minha espada."

            scene priscila vale_mc with Dissolve(2.0)

            c "Eu tô me sentindo muito melhor, [mc]."

            mc "Que bom. Eu fico feliz de você conseguir compartilhar isso comigo."

            mc "Eu realmente gosto de você, [c]."

            c "Hehe... você fala umas coisas tão... sei lá, incomuns... com tanta naturalidade."

            c "Sem dúvidas, você é o cara mais legal que eu já vi na vida."

            mc "Que exagero..."

            c "Não tô brincando, não."

            mc "Hehe..."

            c "[mc]... Falando sério agora. Por favor, nunca me deixe, tá?"

            mc "Claro, boba. Vou te encher muito o saco ainda."

            c "Tá..."

    scene ilha vale with Dissolve(1.0)

    gus "[c]."

    show gustav explicando with dissolve

    gus "Estamos prontos para refazer."

    show gustav explicando at direita with move

    show priscila a_surpresa with dissolve

    c "Ah! [gus]!"

    show priscila a_surpresa at esquerda with move

    c "Desculpa..."

    gus "Tudo bem. Só precisamos fazer agora. Estão todos esperando."

    show priscila a_seria with dissolve

    c "Sim. Pode deixar."

    c "[mc], eu volto logo, ok?"

    show gustav malicioso with dissolve

    gus "Na verdade, eu pedi para todos que não forem trabalhar no filme que deixem o local."

    c "Mas-"

    mc desculpa "Não se preocupe. Eu tava pensando em ir esperar no camarim. Tô meio cansado."

    c "T-tá. Eu já tô indo pra lá."

    mc normal "Bom trabalho pra vocês."

    c "Obrigada..."

    scene black with dissolve

    "..."

    scene camarim interior2 with Dissolve(1.0)

    "Maluco. Esse dia parece que não acaba."

    "Vou esperar a [c] e espero que a gente volte pra ilha logo."

    "..."

    show black with dissolve

    hide black with dissolve

    "Que sono..."

    show black with dissolve

    hide black with dissolve

    "Talvez eu acabe tirando uma pestana."

    show black with dissolve

    if p5_beijo:

        "..."

        "{i}grrraakkkk{/i}"

        scene camarim interior2 with vpunch

        "Quê?!"

        show marco chegando with dissolve

        mc surpreso "Ma-Marco?!"

        mar "Olá, [mc]. Desculpa, mas não tenho muito tempo."

        mc preocupado "Como assim?"

        mar "Você não devia ter beijado a [c] na frente do [gus]."

        mc angustiado "Calma, [mar]. Eu não-"

        jump priscila_e5_soco

    "..."

    c "[mc]..."

    scene camarim interior with Dissolve(1.0)

    mc concentrando "Acho que eu capotei..."

    show priscila feliz with dissolve

    c "Pronto pra voltarmos?"

    mc normal "Sim."

    c "O carro tá esperando a gente."

    mc "Então vamos."

    scene black with dissolve

    "..."

    scene priscila jato_mc with Dissolve(1.0)

    mc "Hoje foi um dia incrível. Obrigado, [c]."

    c "Eu que agradeço. Foi tão bacana ter você aqui."

    c "Queria poder te trazer mais vezes..."

    mc "Se der, me avise."

    c "Pode deixar."

    scene black with dissolve

    scene ilha vale with Dissolve(1.0)

    mc desconfiado "Ainda tá com sol. Como isso? Parece que eu passei dois dias fora..."

    show priscila incerta with dissolve

    c "É um pouco cansativo, né?"

    mc "Não sei como você aguenta essa rotina."

    c "Eu não tô velha igual você."

    mc envergonhado "Ei..."

    jump priscila_e5_final

label priscila_e5_soco:

    $ persistent.priscila_cena16 = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("priscila_e5_soco","priscila","personagem")

    scene mc soco_marco with hpunch

    pause

    mc "OOF!"

    mc "KHA!"

    mc "{i}cof cof{/i}"

    mc "Não... cons... respi..."

    mc "{i}cof cof{/i}"

    if socou_gustav:

        mar "Você pode ser forte o suficiente pra bater em velhinhos. Mas eu não sou o [gus]."

    mc "Não... resp..."

    mar "Calma que você não vai morrer só com isso."

    mar "Esse foi só o aperitivo. Tem muito mais pra você."

    mc "[mar]... calm-"

    scene black with hpunch

    mc "ARGH!"

    mar "Pro chão!"

    scene mc socado with vpunch

    pause

    "{i}TUDUMP{/i}"

    mc "Ai..."

    "Por favor... não me mate..."

    mar "Não se preocupe que a adrenalina não vai deixar você sentir muita dor... por hora..."

    scene black with hpunch

    "{i}DEISH{/i}"

    scene black with vpunch

    "{i}BOUSH{/i}"

    scene black with hpunch

    mc "..."

    mar "Adeus, [mc]."

    "..."

    "..."

    "{i}grrraakkk{/i}"

    "O que aconteceu?"

    "Não sinto nada... tá tudo zumbindo..."

    scene camarim interior2 with Dissolve(3.0)

    c "AAAAAAHHHHHHHH!"

    scene mc socado_sangrando with vpunch

    c "[mc]! MEU DEUS!"

    c "Socorro!! Alguém! Por favor!"

    "A voz da [c]..."

    mc "Pri..."

    c "[mc]?! O que foi?!"

    mc "Des... {i}cof{/i}... desculpa..."

    show black with dissolve

    hide black with dissolve

    c "Não fala isso, [mc]. Por favor."

    show black with dissolve

    hide black with dissolve

    "Ela parece tão preocupada. Será que eu vou morrer?"

    show black with dissolve

    $ renpy.pause(delay=1, hard=True)

    hide black with dissolve

    c "Calma, eu vou buscar ajuda..."

    show black with dissolve

    $ renpy.pause(delay=5, hard=True)

    hide black with dissolve

    c "{size=15}[mc]...{/size}"

    scene black with Dissolve(3.0)

    pause

    show pixie b_provocando with dissolve

    p "Sério que {b}você{/b} deixou o [mc] morrer?"

    if persistent.mc_morreu:

        p "E pela segunda vez ainda?"

        p "Tomar um tiro não foi o suficiente pra você aprender que essas pessoas são perigosas?"

    p "Agora você vai que voltar e faz-"

    c "{size=12}[mc]!{/size}"

    show pixie b_preocupada with dissolve

    p "Hm?"

    p "Que estranho..."

    show pixie b_provocando with dissolve

    p "..."

    p "Talvez eu esteja enganada... Esse rapaz tem mais força do que eu imaginei."

    p "Fiz ou não fiz o certo escolhendo ele?"

    p "Quem sabe eu finalmente possa trazer de volta aquele tempo..."

    p "Continue fazendo o que está fazendo e talvez você acabe me ajudando mais do que imagina."

    hide pixie with dissolve

    $ dia += 3
    $ tempo = 1

    pause

    scene mc uti_deitado with Dissolve(5.0)

    pause

    "Ah? Onde eu tô?"

    "Não tô lembrando..."

    "A [c]! Eu tava com a [c] no set de filmagem!"

    scene mc soco_marco with dissolve

    scene mc uti_deitado with dissolve

    "..."

    "O soco na boca do estômago..."

    "Tá tudo voltando agora..."

    if socou_gustav:

        "Eu soquei o [gus]..."

        "E ele mandou o puto do [mar] fazer o que ele mesmo não conseguia."

        "Velho maldito."
    else:


        "O [mar] apareceu no camarim e me deu uma surra."

        "Eu nem entendi o que aconteceu. Aque filho da puta..."

    "Meu corpo tá doendo muito, mas não quero ficar aqui. Cadê a [c]? Será que tem alguém aqui comigo?"

    "{i}gatchak{/i}"

    mc "?"

    scene hospital uti with Dissolve(1.0)

    mc surpreso "[c]?!"

    show priscila d_surpresa with dissolve

    c "[mc]! Você acordou!"

    mc envergonhado "Sim..."

    c "Você não pode ficar em pé. Vai pra cama."

    mc "Eu tô me sentindo bem. Não esquente."

    show priscila d_chateada with dissolve

    c "Que bom, [mc]... fiquei tão preocupada..."

    c "Os médicos disseram que você tava com uma hemorragia interna na cabeça... você podia ter morrido de verdade."

    $ renpy.end_replay()

    menu:
        "Foi tudo culpa do [gus].":


            $ priscila_idiota += 1

            mc bravo "Foi tudo culpa do maldito do [gus]..."

            c "[mc]..."

            show priscila d_preocupada with dissolve

            c "Você... precisa entender... se não..."

            mc "[c], esse idiota é a causa de tudo de ruim."

            c "Mas... eu preciso dele, [mc]..."

            mc irritado "Como assim?!"

            c "Não grite comigo..."

            mc desculpa "Desculpa... Mas [c]... esse cara..."

            show priscila d_chateada with dissolve

            c "Eu sei, [mc]. Eu sei de tudo isso. Você acha que eu não sei?"

            c "Você acha que você é o único que não tá gostando disso?"

            c "E eu?! Não acha que eu também odeio tudo isso?!"

            c "Você acha que eu não tenho nojo, ódio e repulsa de mim mesma?!"

            mc preocupado "Mas você..."

            c "Não! Eu sou culpada também!"

            show priscila d_preocupada with dissolve

            c "Só que..."

            c "Por favor... vamos conversar sobre isso outra hora. Você não tá bem."

            mc desculpa "[c]..."

            c "O importante agora é sua melhora."

            mc "Ok."
        "Que bom que eu não morri então.":


            mc envergonhado "Que bom que eu não morri, então..."

            show priscila d_feliz with dissolve

            if priscila_namoro:

                c "Imagina se eu perco meu namorado?"

                c "Bem no primeiro encontro depois que a gente oficializou?"
            else:


                c "E o que eu faria sem meu melhor amigo, hein?"

            mc "Seria trágico..."

            c "Sim!"

    mc desculpa "E, afinal, como eu vim parar aqui?"

    show priscila d_feliz with dissolve

    c "Não se preocupe com nada. Eu deixei tudo acertado com o hospital."

    c "A equipe da Dra. Lisandra é a melhor do país. Se não fosse por eles, provavelmente você..."

    mc desculpa "... teria morrido?"

    show priscila d_preocupada with dissolve

    c "Desculpa..."

    mc normal "Não esquente."

    c "Mas agora volte pra cama por favor. Eu vou falar com eles. Ela me pediu pra avisar quando você acordasse."

    mc desconfiado "Quanto tempo eu tô aqui?"

    c "Dois dias e um tantinho."

    mc surpreso "Quê?!"

    c "Foi complicado, [mc]..."

    mc desculpa "Meu Deus... eu nem tinha percebido..."

    show priscila d_feliz with dissolve

    c "Mas o importante é que você tá bem agora. Vou avisar ela. Enquanto isso, deite e descanse."

    mc concentrando "Ok, chefe."

    c "Hehe."

    hide priscila with dissolve

    "Será que a [c] ficou esse tempo todo comigo aqui? Mas e as gravações dela?"

    "Bom, deixa eu deitar..."

    scene black with Dissolve(1.0)

    "{b}24 horas depois{/b}"

    $ dia += 1
    $ tempo = 1

    scene hospital espera with Dissolve(1.0)

    c "Que bom que você vai poder sair!"

    mc envergonhado "Nem fala."

    mc "Desculpa ter causado tanto problema."

    show priscila preocupada with dissolve

    c "Tá doido? Problema nenhum, bobo..."

    mc "Valeu."

    c "Você ouviu o que ela disse. Sem muito esforço nos próximos dias."

    mc normal "Ok, doutora."

    show priscila hehe with dissolve

    c "Hehe..."

    jump priscila_e5_final

label priscila_e5_final:

    show priscila incerta with dissolve

    c "Aconteceram tantas coisas..."

    mc envergonhado "Sim. Com certeza."

    if priscila_namoro and priscila_idiota >= 5:

        label priscila_e5_replaychutado:

            $ persistent.priscila_cena17 = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("priscila_e5_chutado","priscila","personagem")

        $ priscila_namoro = False
        $ priscila_chutado = True

        show priscila chateada with dissolve

        c "[mc]... eu não sei como falar isso, mas eu sei que você gosta muito de mim, então você vai entender."

        mc desconfiado "Ah?"

        c "Eu quero terminar nosso namoro."

        mc angustiado "Quê?!"

        c "Eu... tinha medo que isso acabasse acontecendo. Acho que eu coloquei muita esperança na gente, mas não vai dar certo."

        if socou_gustav:

            c "Todos no filme já sabem que você bateu no [gus]. Eu realmente não esperava isso de você."

            c "Mas não foi só isso..."

        c "A forma como você se comportou. Você podia ter agido de forma diferente..."

        mc preocupado "Ainda é muito cedo. Esse foi só nosso pr-"

        show priscila chorando with dissolve

        c "Por favor, [mc]! Não fale nada! Se você gosta de mim, por favor só aceita!"

        c "Já é difícil demais pra mim falar isso!"

        mc angustiado "Mas, [c]..."

        c "Por favor..."

        "Como posso entender uma coisa dessas? Esse foi nosso primeiro encontro namorando."

        "Mas o que eu posso fazer? Não posso descontar nela..."

        mc concentrando "Ok..."

        mc desculpa "Eu entendo... Nós tentamos e não deu certo."

        show priscila chateada with dissolve

        c "Você entende?"

        mc concentrando "Claro que eu tô frustrado. Mas eu entendo."

        c "Obrigada. Mas eu não quero desaparecer. Eu gosto muito de você. Só não acho que vamos poder continuar dessa forma."

        mc desculpa "..."

        c "Tá um climão agora..."

        show priscila preocupada with dissolve

        c "Eu pedi pra eles te levarem pra ilha."

        mc desculpa "Não precisa. Eu vou de busão mesmo."

        c "Não, [mc]! Por favor!"

        mc "[c]. Eu disse que entendo. Agora, por favor, deixa eu fazer do meu jeito."

        c "Tá..."

        mc "Até mais."

        c "Até."

        hide priscila with dissolve

        "Não acredito..."

        $ tempo += 1

        if carro:

            scene carro_mc_cidade1 with Dissolve(1.0)
        else:


            scene mc onibus_noite with Dissolve(1.0)

        "Por que as coisas tinham que acontecer assim?"

        "Eu realmente forcei a barra algumas vezes hoje. Não devia ter feito isso."

        "A [c] é uma garota apaixonada, mas muito sensível. Eu tinha que ter tido mais cuidado em como agir com ela."

        if socou_gustav:

            "Principalmente no lance do soco no velho. Eu tinha que ter me segurado..."

        "Vamos ver como as coisas vão acontecer entre a gente agora."

        menu:
            "Foda-se a [c]. Tem muitas garotas na ilha.":


                "Por mim, se ela quiser ser minha amiga, eu topo. Mas tem garotas demais aqui."

                "Não vou ficar correndo atrás."
            "Eu quero reconquistar ela.":


                $ priscila_reconquista = True

                "Não quero deixar de ver ela."

                "Eu quero {b}reconquistar ela{/b} de qualquer forma! E eu vou conseguir."

                mc "Força, [mc]. Você conquistou ela uma vez. Pode fazer isso de novo."

        $ renpy.end_replay()
    else:


        show priscila cansada with dissolve

        c "Até eu tô ficando cansada agora."

        c "Vamos pra ilha?"

        mc concentrando "Tô louco pra chegar e tomar um banho também."

        c "Deixa eu chamar o motorista."

        scene black with dissolve

        "..."

        scene carro cidade with Dissolve(1.0)

        c "Aaaaaahhhhh!"

        mc "Que foi?!"

        c "Quero tomar banho!"

        scene black with dissolve

        mc zerado "..."

        scene hotel recepcao with Dissolve(1.0)

        mc normal "Chegamos enfim."

        show priscila feliz with dissolve

        c "Não acredito que você ainda me trouxe até aqui."

        if priscila_namoro:

            c "Você é o melhor namorado do mundo."

            mc "Sou só um cavalheiro."

            c "Se eu não tivesse tão suada, eu te chamava pra subir agora..."

            mc charmoso "Vem aqui."

            show priscila abracando_mc with dissolve

            mc "Então quer dizer que eu tenho um cupom que vale uma farrinha?"

            c "Sim, safado..."

            mc "Foi tudo incrível, [c]. Não vejo a hora da gente fazer algo juntos de novo."

            c "Tá. Vou morrer de saudades."

            mc "Tchau, linda."

            c "Beijos."
        else:


            c "Você é o cara mais legal do mundo!"

            mc charmoso "Com certeza."

            c "Agora tá se achando."

            mc desconfiado "Ei. Eu que falo isso."

            c "Haha!"

            mc "Vou indo nessa. A gente se fala."

            c "Beijos, [mc]."

            mc "Beijo."

        hide priscila with dissolve

        "Ufa... que encontro gigante..."

        "Deixa eu sentar um pouco no parque."

        "..."

    label priscila_e5_finalzinho:

        scene mc parque_sentado_noite with Dissolve(1.0)

    "Tanta coisa aconteceu comigo nos últimos tempos."

    "Mas isso não é nada."

    "Ainda tem muita água pra passar por debaixo dessa ponte."

    "Minha vida de paparazzo tá só começando."

    if not p5_naoviajou:

        "E independente da [c], depois de hoje eu quero acabar com a vida desse [gus]. Virou um lance pessoal agora."

        "Aqueles artistas... a [ag]... Todos eles pareciam saber alguma coisa sobre o [gus]."

        "Eu tenho certeza que de alguma forma ou de outra eu posso colocar esse velho na cadeia."

        "E eu vou livrar a [c] das garras dele de uma vez por todas."

    "Como será que tudo isso vai acabar?"

    $ v16_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v16_fim","priscila","personagem")

    scene black with Dissolve(1.0)





    jump call_cidade



label priscila_evento6:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p6_save", extra_info="p6_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ priscila_cel_msg7_r = True

    "Então a [c] quer que eu acompanhe na filmagem..."

    if p5_naoviajou:

        "Da outra vez eu não acompenhei ela. Eu imaginei que ia dar cagada."

        "Não quero recusar ela de novo. Ia ficar muito chato. Dessa vez eu vou com certeza."

    if priscila_chutado:

        "Sério que ela tá me chamando?"

        "Mesmo depois de ter me chutado no outro dia, ela me manda uma mensagem dessas como se nada tivesse acontecido?"

        if priscila_reconquista:

            "Bom... aquele dia eu decidi que ia querer reconquistar ela."

            "A [c] é muito importante pra mim e eu realmente quero ficar com ela."

            "Não é fugindo dela que eu vou me reaproximar. Vou ter que voltar nas gravações."
        else:


            "Eu resolvi no outro dia que não vou correr atrás dela. Vamos ser só amigos mesmo."

            "Ainda tô meio puto com ela por ter acabado nosso lance, mas ela tem pautas e pelo menos nisso ela pode ser muito útil."

            "Além de que tem muitas garotas aqui na ilha. Não vou ficar de picuinha com ela por causa disso."

            "A fila anda."

    if priscila_namoro and not p5_naoviajou:

        "A gente tá num lance sério. Não vou dar mancada faltando no bagulho que é tão importante pra ela."

        "Mesmo que eu tenha que ver o idiota do [gus] de novo."

        "Como eu odeio esse velho filho de uma puta."

    "Então se eu vou viajar com ela, eu tenho que me preparar. Psicologicamente, claro..."

    scene mc parque_sentado with Dissolve(1.0)

    "Cara, todo o lance da [c] com o [gus]. Isso é tão terrível que eu nem sei como encarar."

    "Eu queria poder fazer mais por ela. Como é possível que ninguém faça nada?"

    "E aquela agente dela? Até esqueci o nome agora."

    "E a [c] também. Ela não vai tornar isso público? Tudo isso é por um papel no filme?"

    "Eu mesmo podia botar a boca no mundo e revelar isso pro chefe. O que será que ele falaria?"

    "Mas daí eu taria passando por cima da [c]. Eu preciso confiar nela e ajudar no que eu puder."

    "Só que essa situação me deixa puto demais, mano. Que saco..."

    "Agora é esperar e ir com ela. E rezar pra que nada de terrível aconteça."

    scene ilha parque2 with Dissolve(1.0)

    mc zerado "Por que eu tenho a impressão que toda vez que eu me encontro com ela algo terrível acontece?"

    play sound "audio/som_35_passos.mp3"

    scene hotel recepcao with Dissolve(1.0)

    "E aqui tô eu. Como um bom cachorrinho."

    "Merda... por que eu fico pensando assim? Acho que toda essa situação tá mexendo comigo."

    c "[mc]!"

    scene pri6_img1 with Dissolve(1.0)

    pause

    c "Muito obrigada por vir."

    mc "Não foi nada."

    if not p5_naoviajou:



        c "Eu sei que da outra vez não foi o melhor dos passeios, né?"

        mc desculpa "Foi legal assim."

        c "Eu sei que não foi. Não precisa mentir."

        if priscila_chutado:

            scene pri3_img5 with dissolve

            mc desculpa "O pior foi o que aconteceu com a gente."

            c "[mc]... É que-"

            if priscila_reconquista:

                mc preocupado "Eu sei que eu não me comportei como eu devia."

                if socou_gustav:

                    mc "Eu não devia ter batido no [gus]. Mas, [c]! Você precisa entender!"

                mc "Eu não queria te desrespeitar. Eu só queria passar um tempo bacana com você igual dois namorados."

                c "Eu sei, [mc]... e eu sei que eu tô pedindo muito de você. Mas eu tinha pedido de verdade..."

                c "Eu disse que não era pra gente fazer nada que revelasse nossa relação. Você tinha concordado!"

                mc "Eu sei... Por favor, desculpa..."

                c "Você sabe o quanto eu gosto de você. Mas gostar não é tudo na vida. Existem coisas maiores."

                c "Se você não pode ser meu namorado assim, então nossa relação nunca vai dar certo."

                c "Não é só uma decisão minha. É sua também."

                c "Eu quero muito muito muito ficar com você. Mas eu preciso que você aceite o que eu te pedi. Pelo menos por enquanto. Não é pra sempre."

                "Então ela gosta mesmo de mim, só que ela não consegue colocar nossa relação em primeiro lugar."

                "A [c] tem as coisas dela. E se eu quiser ficar com ela eu vou ter que aceitar as coisas assim sabe-se lá até quando."

                "A decisão é minha também. O que eu quero pra gente e principalmente o que eu quero pra mim?"

                menu:
                    "Eu vou tentar namorar com ela nessas condições":


                        $ priscila_namoro = True
                        $ priscila_reatou = True

                        mc desculpa "Você tem razão. Eu preciso entender seu trabalho também."

                        mc concentrando "Eu peço desculpas, de verdade."

                        mc charmoso "E eu prometo que vou me esforçar ao máximo pra respeitar seu trabalho. Por favor, me dê mais uma chance."

                        scene pri6_img1 with Dissolve(1.0)

                        c "Ai, [mc]! Você é tão incrível! Eu sabia que você também gostava de mim!"

                        mc "Claro que eu gosto, boba!"

                        c "Eu tô tão tão feliz!"

                        mc "Eu também."

                        c "Hmm..."

                        "Ela parece tão aliviada."
                    "Acho melhor a gente só ser amigos":


                        jump priscila_e6_amigos
            else:


                label priscila_e6_amigos:

                    $ priscila_friendzone = True

                    mc desculpa "Olha... eu entendo. Eu pensei bastante sobre isso e acho que é melhor sermos só amigos mesmo."

                c "V-você tem certeza?"

                mc "Sim. Você tá focada no seu trabalho e eu tô no meu."

                mc "Você sabe que eu gosto de você, de verdade. Mas com essas coisas acontecendo, eu realmente acho que a gente devia dar um tempo em algo sério."

                scene pri3_img3 with Dissolve(1.0)

                c "Eu... eu acho que eu concordo."

                mc normal "Que bom. Acho que a gente pode se dar super bem como amigos."

                c "V-verdade."

                c "Você tem razão. Vamos deixar o romance pra quem pode, né?"

                mc charmoso "Concordo."

            c "Eu fico feliz que a gente tenha resolvido as coisas. Eu tava tão mal que a gente tinha ficado assim."

            mc normal "Eu também. Tô mais tranquilo agora."



        show black with Dissolve(0.1)

        hide black with Dissolve(0.1)

        if priscila_namoro:

            c "Sabe, [mc]... a gente tá namorando, né? A gente tá bem agora... e mesmo depois de tudo você tá do meu lado."
        else:


            c "Sabe, [mc]... a gente é só amigos... e mesmo assim você tá do meu lado desde sempre."

        mc envergonhado "S-sim."

        c "Eu acho que você merece uma recompensa..."

        mc "R-r-recompensa?"

        c "É... uma recompensa do jeitinho que você tá pensando... e aí? Você quer?"

        label pri6_priscila_premium:

            pass

        "Recompensa? Bom... eu realmente fui legal com ela, mas será que eu vou cobrar ela por isso?"

        menu:
            "Eu aceito.":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_1



















                    jump pri6_priscila_premium

                mc "Claro que eu aceito. Você pode começar vindo aqui."

                c "A-ai!"

                scene pri6_img2 with Dissolve(1.0)

                pause

                mc "Faz tempo que eu queria pegar você assim."

                c "Toma cuidado. A gente tá no hall do hotel."

                mc "Eu nunca vi ninguém aqui."

                c "O pessoal usa outra entrada pros carros, mas de vez em quando vem alguém..."
                scene pnew_ani09 with Dissolve(1.0)
                mc "Foi você quem ofereceu."

                c "Eu só tô falando pra você me usar o mais rápido possível."

                mc "T-tá..."

                c "Pega aqui em baixo."

                scene pri6_img3 with Dissolve(1.0)

                pause

                mc "E essa mania de não usar calcinha?"

                c "Eu odeio ela me apertando. Eu gosto de sentir bem livre aqui em baixo..."

                mc "Você tá querendo me deixar louco, é?"

                c "Eu quero que você me aperte... que você me bata."

                mc "Hmm..."

                c "Aperta forte."

                scene pri6_img4 with Dissolve(1.0)

                pause

                c "Ai! Assim! Me belisca!"

                mc "Você gosta?"

                c "Eu adoro quando doi."

                mc "S-sério?"

                c "Sim. A dor me deixa quente. Quanto mais, melhor."

                mc "Então tá."

                scene pri6_img4 with vpunch

                c "AI!"

                mc "Assim que você quer?"

                c "Ééé... faz mais..."

                c "Você tá me deixando louca. Eu quero mais na minha bunda."

                scene pri6_img5 with Dissolve(1.0)

                pause

                c "Vem. Bate em mim, [mc]."

                mc "[c]..."
                scene pnew_ani14 with Dissolve(1.0)
                c "Cala a boca e me bate."

                "Ela tá muito excitada. Eu tô até me sentindo estranho. Será que eu entro nessa?"

                menu:
                    "Claro. Toma aqui.":


                        mc "Não precisa falar duas vezes, gostosa."

                        c "Isso... vem..."

                        play sound tapa

                        scene pri6_img6 with hpunch

                        pause

                        c "AAH!"

                        mc "Quer mais?"

                        c "Bate!"

                        play sound tapa

                        scene pri6_img6 with hpunch

                        c "AI! ISSO!"

                        play sound tapa

                        scene pri6_img6 with hpunch

                        c "Assim! Eu tô ficando molhada!"

                        mc "Tá é? Então grita!"

                        play sound tapa

                        scene pri6_img6 with hpunch

                        c "AAH! ISSO!"

                        mc "Gostou?"

                        c "Você vai ver..."

                        mc "Opa..."

                        scene black with dissolve

                        scene pri6_img7 with Dissolve(1.0)

                        pause

                        c "Olha aqui como você me deixou, seu gostoso... com esse mãozão..."

                        mc "Hmm..."
                        scene pnew_ani10 with Dissolve(1.0)
                        c "Agora vem e me devora."

                        mc "Agora você que tá me deixando louco."

                        c "Isso... lambe sua putinha, vai..."

                        scene pri6_img8

                        "Priscila?" "É isso que eu quero."

                        mc "Q-QUÊ?!"

                        "Que merda tá acontecendo?!"

                        c "Vemm..."

                        menu:
                            "Foda-se. Vou cair de boca nessa delícia molhada.":


                                c "Isso!"

                                scene black with dissolve

                                scene ani16 with Dissolve(1.0)

                                pause

                                c "Assim, gostoso! Você tem a melhor língua!"

                                mc "Você gosta assim, é?!"

                                c "Adoro! Tô com tanto tesão por você, gostoso! Awnn!"

                                mc "Adoro esse seu gemidinho, sua delícia."

                                c "Isso! Eu gemo assim pra todo mundo saber que minha xotinha tá sendo devorada! Aahh!"

                                mc "Quer que todo mundo saiba, é?!"

                                c "Ainn! S-sim! Vai todo mundo bater pra puta deles! Awwnn!"

                                mc "Fica cheia de tesão pensando nisso, né?"

                                c "Aaiii! Simmmm!"

                                menu:
                                    "Nada disso. Só eu que aproveito essa delícia.":


                                        c "A-ah... ok..."

                                        mc "Agora teu dono aqui acaba contigo."

                                        c "I-isso!"
                                    "Eles podem gozar pra você também. Eu deixo.":


                                        c "Todo mundo que quiser poder gozar pra sua princesa, é!?"

                                        scene black with dissolve

                                        scene ani17 with Dissolve(1.0)

                                        pause

                                        mc "Ninguém mandou eu namorar uma famosa que todo mundo deseja."

                                        c "T-todo mundo deseja sua namorada, amor! Aahnnn!"

                                        c "Todos eles batem pras minhas fotos no IG! Safados! Awwnn! Só porque eu sou gostosa!"

                                        mc "E fica se exibindo pra todo mundo!"

                                        c "Aii! Eu fico! Awnnnn! Quero todo mundo batendo pra mim! Ainnn!"

                                        c "Todos safados! Annn! Todo mundo sabe! Ainn!"

                                        mc "A puta da galera!"

                                        c "Aaannnn! Não fala assim! Eu vou gozar!"

                                        mc "Goza, safada! Grita pra todo mundo saber!"

                                        scene ani17_final with vpunch

                                        pause

                                c "Aaiinnnnnn!"

                                c "Delíciaaaaa!"

                                mc "U-uau! Você até jorrou, gata..."

                                c "Ahh... ahh..."

                                scene pri6_img8

                                "Priscila?" "Adorei..."

                                mc "Hm?!"
                            "Não tô gostando disso. Vamos parar.":


                                pass

                        scene pri3_img3
                    "Melhor a gente parar aqui.":


                        mc "Pri, eu sei que você tá no clima, mas é melhor a gente parar aqui."

                        c "Tá brincando?! Vem logo!"

                        mc "Eu queria que a gente fosse com calma..."

                        c "Você só pode tá de brincadeira... é sério?"

                        mc "É... nem tá parecendo você."

                        c "Eu tô excitada, [mc]! Você não entende que mulheres também têm vontades?!"

                        mc "Eu sei, mas..."

                        c "Tem certeza? Você tá perdendo uma chance de se dar bem..."

                        mc "T-tudo bem... q-quem sabe um dia..."

                        scene pri3_img3 with dissolve

                        c "Você é difícil, moleque... mas eu ainda vou pegar você. Pode ter certeza."

                        mc "C-como?"
            "Não precisa.":


                mc "Não tem necessidade disso, [c]. Eu não fui legal com você pra depois você ter que me pagar."

                mc "Eu só fiz o que eu achei que eu tinha que fazer. E você não deve nada pra mim por causa disso, tá?"

                c "Tem certeza? Você tá perdendo uma chance de se dar bem..."

                mc "T-tudo bem... q-quem sabe um dia..."

                c "Você é difícil, moleque... mas eu ainda vou pegar você. Pode ter certeza."

                mc "C-como?"

        show black with Dissolve(0.1)

        hide black with Dissolve(0.1)

        c "Que foi?"

        mc desconfiado "Hm?"

        c "Você ficou quieto e depois começou a sussurrar umas coisas. Você tá legal?"

        "Que merda foi essa?"

        mc envergonhado "T-tá tudo legal."

        mc "É..."
    else:




        c "Que bom que dessa vez você vai poder ir comigo."

        mc envergonhado "Sim. Desculpa não ter ido da outra vez."

        c "Tudo bem. Mas vou te encher o saco o dobro agora também."

        mc feliz "Haha. Combinado."

    mc "E o que vai rolar lá nas gravações dessa vez?"

    scene pri3_img6 with Dissolve(1.0)

    c "Ah. O de sempre. Vou ter que te deixar um tempinho sozinho, mas vou tentar terminar o mais rápido que der."

    c "E daí a gente passa um tempo lá no meu camarim. Não é nada incrível."

    mc "Beleza. Vai ser legal passar esse tempo com você."

    c "Hehe. Foi o que eu pensei também. Só queria passar mais tempo com você. Tomara que eu não esteja sendo mimada."

    mc normal "Que nada. Eu vou adorar."

    c "Você é tão bacana, [mc]. Eu nem acredito que eu te achei no meio de todas essas pessoas que existem."

    mc desconfiado "Que comentário é esse?"

    scene pri3_img2 with Dissolve(1.0)

    c "Ei! Me deixa! Agora você me fez ficar com vergonha."

    mc "Você é só boba, isso sim."

    c "Ei ei! Ago-"

    "{i}trriim trriim{/i}"

    c "Ah. Acho que nossa carona tá aí."

    mc "Opa. Então bora."

    c "Vamos."

    "Seja o que Deus quiser."

    scene black with Dissolve(1.0)

    scene carro cidade with Dissolve(1.0)

    $ renpy.pause(delay=2, hard=True)

    scene jato exterior with Dissolve(1.0)

    c "Ufa."

    scene pri5_img2 with Dissolve(1.0)

    mc desconfiado "Você tem que fazer isso diretão?"

    c "Sim. Não é todo dia porque alguns dias eu durmo lá no meu camarim mesmo. Mas sempre que eu volto pra cá eu preciso fazer isso."

    mc desculpa "Que trabalho, hein, [c]?"

    c "Nem fala."

    c "Mas hoje vai ser diferente. Só de você tá comigo já muda tudo, [mc]."

    mc envergonhado "Que bom."

    c "Vamos subir?"

    mc normal "Claro."

    scene ilha jato_geral with Dissolve(1.0)

    if not p5_naoviajou:

        c "E aí? Vai morrer de medo outra vez?"

        mc zerado "Me deixa."

        c "Hihi."
    else:


        mc surpreso "Uou! É gigante! Tudo isso aqui é seu?"

        c "Esqueci que você não veio da outra vez. É pra mim, sim."

        c "Mas não é meu. É da produção do filme."

        mc normal "Entendi. Muito massa."

    scene priscila jato_mc with Dissolve(1.0)

    c "Hm-hm-hmmmm..."

    "A [c] parece feliz mesmo. A gente tá numa boa."

    if priscila_namoro:

        "A gente tá namorando, mas ninguém ia falar. Eu queria poder pegar ela aqui no avião mesmo."

        "Não vejo a hora que o ensaio acabe e a gente volte pra ilha."

        "Acho que tá na hora da gente consumar nossa relação."

    "Eu conheço a [c] há um bom tempo já."

    "Se você pensar, desde aquele dia na redação que ela foi brigar com o chefe. Já faz mó cota."

    "E eu sinto que a gente já passou tanta coisa."

    if priscila_namoro:

        "O máximo que a gente fez foi ter dado uns beijos. Mas eu quero mais que isso."

        "A gente já é adultos. E só um beijinho não resolve nada."

        c "[mc]?"

        mc tarado "..."

        c "[mc]?!"

        mc surpreso "Ah! Oi!"

        c "Você estava com uma cara estranha..."

        mc envergonhado "Não foi nada..."

        "Eu tô pensando tanto nisso que tá até na cara."

    c "Sabe, [mc]..."

    mc "Oi?"

    c "Eu posso deitar com você aí?"

    mc "C-claro."

    "Eita!"

    scene priscila jato_mc_deitada with Dissolve(1.0)

    mc "Aconteceu alguma coisa?"

    c "É... o que você acha do seu emprego?"

    mc "Meu?"

    c "Sim. O que você acha de ser paparazzo?"

    "Tenho vontade de matar meu chefe... mas acho que é melhor não responder isso."

    menu:
        "Não é fácil, mas no fundo eu gosto.":


            mc "Não quero ficar me fazendo de vítima, mas não é fácil. Principalmente ter que entregar segredos de quem eu conheço e gosto..."

            c "Entendi..."

            mc "Mas eu gosto de ser jornalista, descobrir e investigar as coisas. E é graças ao meu trabalho que eu conheci tanta gente bacana."

            c "É verdade. Se você não trabalhasse na revista a gente nem ia se conhecer."

            mc "Verdade."
        "Eu só faço porque eu preciso. É horrível.":


            mc "O que me importa é o dinheiro pra poder continuar morando na ilha e não voltar pra casa dos meus pais."

            c "Você odeia tanto assim?"

            mc "Sim. Odeio de verdade."

            c "Mas se você não trabalhasse lá a gente não teria se conhecido..."

            mc "É. Isso é verdade. Mas eu preferia ter te conhecido sem precisar trabalhar lá."

            c "Entendo..."

    if priscila_namoro:

        c "Eu não teria encontrado o melhor namorado do mundo!"

        mc "Você que é a melhor namorada do mundo."

        c "Não sei se a melhor, mas a mais linda, a mais engraçada, a mais interessante, a mais inteligente, a mais-"

        mc "Ok, eu entendi!"

        c "Hehehe..."
    else:


        c "Eu não teria meu melhor amigo do meu lado."

        mc "Isso seria um desperdício mesmo, porque eu sou muito bacana."

        c "Ai! Como se acha! E quem fala 'bacana' hoje em dia?"

        mc "Me deixa!"

    mc "..."

    c "..."

    mc "Por que você me perguntou do trabalho?"

    c "Ah... por nada..."

    menu:
        "Ficar quieto":


            "Melhor não insistir no assunto se ela não quer falar."

            mc "Ok..."

            c "..."
        "Insistir em saber o que está acontecendo":


            mc "Tem alguma coisa aí. O que foi?"

            c "Não é nada!"

            mc "Faaaala..."

            c "É que... ah, merda! Por que eu fui te perguntar. Não queria falar sobre isso."

            mc "Por que? Você não confia em mim?"

            c "Não é isso, [mc]. É só que eu não queria falar disso pra você."

            mc "Ok. Tudo bem."

            c "Obrigada..."

    "O que será que tá rolando?"

    scene priscila_jato_deitada1 with Dissolve(1.0)

    pause

    c "Tá tudo legal, viu? Não precisa ficar preocupado comigo."

    "Por que ela tá falando isso?"

    c "As filmagens estão quase no fim. E eu acho que tudo vai valer à pena quando acabar."

    mc "Pri..."

    c "..."

    if p3_confissao:

        mc "Eu não esqueci o que você me contou na praia. Eu quero continuar do seu lado."
    else:


        mc "E-eu descobri o que aconteceu entre você e o [gus]."

        mc "Na praia aquela vez você queria ter me contado isso, né?"

        mc "Olha. Eu só quero que você saiba que eu vou estar sempre do seu lado."

        c "[mc]... Eu não s-sei o que te falar... por favor me de-"

        mc "Não fala isso. Não tô aqui pra julgar você. Eu só quero ser alguém que você possa se apoiar."

        c "O-obriga.. obrigada..."

    mc "E eu não quero desrespeitar você, mas eu quero fazer mais coisas. Eu não quero só ser seu apoio."

    c "Você já tá fazendo muito mais do que eu posso pedir, [mc]."

    c "Se as pessoas soubessem disso, todas iam ficar contra mim. Iam ter nojo e... me chamar de puta."

    mc "Eu nunca vou fazer isso, [c]. Não fique pensando nessas coisas. Não vai fazer bem pra você."

    scene priscila_jato_deitada2 with Dissolve(1.0)

    pause

    c "E-eu... eu quero que você seja sincero comigo. O que você sente, de verdade?"

    mc "Eu?!"

    c "Sim. Eu sei que você é um cara incrível, que não quer me magoar. Mas eu quero saber sua opinião de verdade."

    c "O que você sentiu quando você descobriu o que eu... eu tive que fazer pra poder fazer o filme?"

    c "Eu quero muito que você seja sincero. Fale de verdade e não o que eu quero ouvir."

    mc "[c]..."

    c "[mc]! Por favor."

    "Caralho, que pergunta..."

    menu:
        "Eu acho que você escolheu se vender pra ter mais fama.":


            $ p6_julgamento = "culpada"

            mc "Você sabe que eu tô do seu lado, né?"

            c "Sim. Eu sei."

            mc "Tá. Olha..."

            mc "Quando eu penso sobre isso, eu não consigo não julgar você."

            mc "Você já era a modelo teen mais famosa do país. Todo mundo te conhecia. Você não precisava desse filme."

            mc "Mas mesmo assim você escolheu passar por isso pra poder ter mais fama, mais dinheiro, sei lá."

            mc "Olha. Eu não quero ficar te julgando. Eu só-"

            c "Não precisa se explicar, [mc]. Foi eu que pedi pra você me falar a verdade."

            c "Obrigada por ter coragem de falar isso na minha cara. Isso só prova que você realmente é um cara especial."

            mc "Só queria falar o seguinte."

            c "Hm?"

            mc "Não importa o que eu acho, ou o que eu fico pensando sobre isso."

            mc "Eu vou ficar com você e não vou gostar menos de você por nada dessas coisas, ok?"

            c "M-muito obrigada, [mc]... de verdade..."

            "Nem acredito que eu tive coragem de falar isso na cara dela."

            "Eu ainda não consigo acreditar que uma garota igual ela aceitou tudo isso."
        "Eu acho que as pessoas te levaram a fazer isso.":


            $ p6_julgamento = "vítima"

            mc "Certo. Olha. Você disse pra eu falar a verdade, mas você tem que acreditar em mim então."

            c "Claro. Eu vou acreditar."

            mc "Tá. Então..."

            mc "Quando eu fico pensando sobre isso, e depois de conhecer as pessoas que estavam ao seu redor, eu não consigo culpar você."

            mc "Eu só consigo pensar que foi por causa dessas pessoas ao seu redor. Esse sistema podre que transforma coisas terríveis em normais."

            c "[mc]..."

            mc "Eu sei que parece que eu tô inventando só pra te deixar feliz, mas é o que eu sinto."

            mc "Você é uma garota, tipo assim, tão doce. Tão bacana. Não consigo aceitar que você sozinha aceitou passar por isso."

            mc "Pra mim foram essas pessoas que fizeram sua cabeça e quando você percebeu o que tava acontecendo já era tarde demais."

            mc "Você tava tão dentro disso tudo que era impossível sair. E até agora isso acontece."

            c "..."

            mc "Eu tô falando sério."

            c "Você!"

            scene priscila_aviao_beijo with hpunch

            pause

            "!"

            if priscila_namoro:

                "O que deu nela?"

                "Um beijo assim, agora..."
            else:


                "O-o que é isso?! A gente não combinou só ser amigos?!"

                c "Desculpa. Eu..."

                "..."

            window hide

            pause
        "Eu realmente não quero falar sobre isso.":


            $ p6_julgamento = "negou"

            mc "Pri, não é por nada. Mas eu realmente não quero ficar falando sobre isso."

            mc "Eu sei que você me pediu, mas isso são coisas que você decidiu e não sou eu que tenho que falar aqui o que eu acho."

            mc "Eu confio em você e vou tá aqui sempre do seu lado. Eu acho que é isso que eu tenho que fazer."

            c "Mas eu preciso saber disso! E se no fundo você tem nojo de mim..."

            mc "Claro que não! Você tem que acreditar em mim."

            mc "Eu disse que eu quero ficar do seu lado enquanto você quiser."

            c "Eu quero pra sempre."

            mc "Então pra sempre."

            c "[mc]... se você não tem nojo de mim, então me beija..."

            if priscila_namoro:

                mc "Agora? Com essas outras pessoas aqui?"

                c "Sim. Não importa."

                mc "Vem aqui. Levanta."

                scene priscila_aviao_beijo with hpunch

                pause

                c "Hmm..."

                c "O-obrigada, [mc]... eu precisava tanto disso."
            else:


                mc "Mas a gente é só amigos, [c]."

                c "Não importa. Por favor, me beija."

                menu:
                    "Beijar ela":


                        mc "Vem aqui. Levanta."

                        scene priscila_aviao_beijo with hpunch

                        pause

                        c "Hmm..."

                        c "O-obrigada, [mc]... eu precisava tanto disso."
                    "Não beijar ela":


                        mc "Desculpa, [c]. Mas eu não posso fazer isso agora."

                        c "Mas então-"

                        mc "Não tem nada a ver com nojo, com asco. Eu só não quero fazer algo assim desse jeito."

                        c "T-tá..."

                        mc "..."

                        c "..."

    scene priscila_jato_deitada1 with Dissolve(1.0)

    c "Sabe... assim... às vezes a gente tem pessoas na nossa vida que parecem nossos melhores amigos, gente que a gente confia de verdade."

    c "E de uma hora pra outra essas pessoas parecem que não estão mais lá pra gente."

    c "A gente colocava tanta coisa pra elas. E elas só se afastam. Desaparecem."

    c "Às vezes a gente tá sozinha. A gente precisa de alguém pra se sentir melhor. A gente precisa confiar em alguém."

    c "Sentir que tem alguém perto da gente, que gosta da gente. E a gente acaba pegando as piores pessoas."

    mc "..."

    c "Por favor, [mc]. Por favor, nunca saia de perto de mim."

    mc "T-tá."

    c "Você promete?"

    mc "Prometo."

    c "Obrigada..."

    "..."

    "{i}Atenção senhoras e senhores passageiros, estamos nos aproximando do destino{/i}"

    c "Eu v-vou sentar."

    mc "Tá."

    scene black with Dissolve(1.0)

    mc "Ufa. Chegamos."

    c "Sim. Vamos pro meu camarim?"

    mc "Claro."

    play sound "audio/som_24_passos2.mp3"

    scene camarim geral with Dissolve(1.0)

    mc "Pode ir se trocar. Eu vou esperar você aqui. Assim você fica mais tranquila."



    if not p5_naoviajou:

        c "Da outra vez foi demais pra você?"

        mc "Não sei se eu vou aguentar."

        c "Tá. Já saio."
    else:


        c "Tá legal. Já termino. Não vai olhar, hein?"

        mc "Vai tranquila."



    "Dar um pouco de privacidade pra ela."

    mc desconfiado "Hm?"

    scene marco_andando with Dissolve(1.0)

    pause

    mc surpreso "!"

    "É a porra do [mar]! A merda do segurança do [gus]. O que ele tá fazendo andando por aqui?"

    "Sorte que ele não me viu."

    "Todas as vezes que eu encontrei esse cara as coisas não acabaram bem pra mim."

    "Só que meu comichão jornalístico tá dizendo que eu devia seguir ele."

    mc zerado "E acabar com um tiro na cabeça."

    "Será que eu vou?"

    menu:
        "Ignorar ele e continuar esperando a [c]":


            "Não tenho porque me meter com ele. Com certeza seria encrenca."

            "Vou continuar só acompanhando a [c] que eu ganho muito mais."

            "Eu não quero nada com esses caras e não posso deixar que eles entrem na minha cabeça."

            "Eu tô aqui por ela e não por esse bando de cuzão."

            scene black with dissolve

            "..."

            jump priscila_e6_after_marco
        "Seguir o [mar]":


            "Não dá pra deixar esse cara sozinho andando por aí. Não consigo."

            "Foda-se se é perigoso. Minha vó já me falava que quem não chora não mama."

            "Vamos ver qual é a desse cara."

            play sound "audio/som_24_passos2.mp3"

            "..."

            scene mc_mato_escondido with Dissolve(1.0)

            "Aqui eu tô numa distância seg-"

            mc surpreso "!"

            "Por que alguma coisa dentro de mim sabia que isso ia acontecer?"

            scene marco_gustav_camarim with hpunch

            pause

            mc irritado "[gus]..."

            "O cão raivoso do velho então tava voltando pro dono."

            "Será que o [mar] sabe do que o velho faz com a [c]? Eles parecem próximos, mas eu não revelaria algo assim pra um segurança."

            "O que será que eles vão fazer agora? E eu?"

            menu:
                "Tenho que ficar e ouvir o que eles estão falando":


                    $ marco_gustav = True

                    "Se eu conseguir escutar eles falando alguma coisa, eu posso até usar contra eles."

                    mc surpreso "!"

                    "Eu posso tentar gravar o que eles tão falando. Meu Deus... Deixa eu ouvir primeiro..."

                    "..."

                    gus "{size=17}... que isso me irrita, [mar].{/size}"

                    mar "{size=17}Eu sei.{/size}"

                    gus "{size=17}E o idiota tá aqui de novo. Ela trouxe ele pras gravações!{/size}"

                    mar "{size=17}Eu sei. Eu vi eles saindo do avião e indo até o camarim dela.{/size}"

                    gus "{size=17}Minha paciência acabou. Eu quero que você passe esse idiota de uma vez por todas.{/size}"

                    mc surpreso "!"

                    "E-ele tá falando de mim! Só pode! 'Eu quero que você passe...' - isso só pode significar que ele tá falando pro [mar] me matar!"







                    scene marco_gustav_camarim with Dissolve(1.0)

                    mar "{size=17}Como? Por que?{/size}"

                    gus "{size=17}Você não escutou o que eu acabei de falar? Eu não quero ver mais esse paparazzo idiota perto da [c].{/size}"

                    gus "{size=17}É óbvio que ela tá trazendo ele aqui pra zombar da minha cara.{/size}"

                    mar "{size=17}...{/size}"

                    mar "{size=17}Você tá perdendo o controle, [gus].{/size}"

                    gus "{size=17}Como é?{/size}"

                    mar "{size=17}Você já corre risco demais transando com todas suas protagonistas. A Flávia, a Ágata, a [c].{/size}"

                    mar "{size=17}E sabe-se lá quantas antes delas.{/size}"

                    gus "{size=17}Cala a boca! Por que você tá falando isso em voz alta?{/size}"

                    mar "{size=17}Pra você entender a gravidade da sua situação.{/size}"

                    mar "{size=17}Não bastasse seu desejo de comer todas essas garotas, agora você tá querendo assassinar alguém por ciúme.{/size}"

                    gus "{size=17}...{/size}"

                    mar "{size=17}O garoto é importante pra gente, sabia?{/size}"

                    gus "{size=17}Não acredito que tô ouvindo isso.{/size}"

                    mar "{size=17}A [a] comentou que a [c] quase teve um ataque um tempo atrás aí.{/size}"

                    mar "{size=17}A menina surtou, [gus]. Ela ia se matar.{/size}"

                    gus "{size=17}Não exagere. Elas só parecem estar sofrendo, mas no fundo gostam.{/size}"

                    mar "{size=17}Você realmente acredita nisso, né? Você é nojento.{/size}"

                    gus "{size=17}[mar]! Cala essa sua boca. Parece que você não sabe o lugar de cada um aqui. Você é o segurança e obedece.{/size}"

                    mar "{size=17}D-desculpa, senhor.{/size}"

                    gus "{size=17}Assim é melhor.{/size}"

                    mar "{size=17}Se me permite, senhor. Eu contei ao senhor a história do viaduto. A menina tava no lixão. Foi o moleque que tirou ela de lá.{/size}"

                    gus "{size=17}Foda-se. Foda-se! Não quero mais saber desse idiota!{/size}"

                    gus "{size=17}Se você não passar ele, eu vou encontrar outro segurança que faça. E se eu encontrar, você está no olho da rua!{/size}"

                    mar "{size=17}Ok. Sim, senhor.{/size}"

                    scene mc_mato_escondido with Dissolve(1.0)

                    "Caralho! O [mar] aceitou me matar. Eu preciso sair daqui voando."

                    "Se esse cara me pegar eu tô fodido."

                    play sound "audio/som_24_passos2.mp3"

                    scene black with dissolve

                    "..."

                    scene camarim geral with Dissolve(1.0)

                    mc envergonhado "Voltei."

                    scene pri6_img9 with Dissolve(1.0)

                    c "Onde você tava?"

                    mc surpreso "Eu?!"

                    c "Não, a vó..."

                    mc envergonhado "Ah. Eu queria te deixar em paz, daí dei uma andada por aí."

                    c "Eu tô te esperando um tempão. Que andada, hein."

                    mc desculpa "Desculpa."

                    c "Enfim..."

                    jump priscila_e6_after_marco2
                "Melhor voltar para o camarim da [c]":


                    "Não tem mais ninguém aqui. Se eu for pego eu tô perdido."

                    "Melhor eu voltar."

                    play sound "audio/som_24_passos2.mp3"

                    scene black with dissolve

                    "..."

                    jump priscila_e6_after_marco

    label priscila_e6_after_marco:

        scene camarim geral with Dissolve(1.0)

        mc concentrando "Ufa. Cheguei antes dela sair."

        c "[mc]?"

        mc normal "Oi. Tô aqui."

        c "Já tô acabando. Só um segundinho."

        mc "Ok."

        "Então o [mar] tá aqui. Isso não é nada bom pra mim."

        "Só de pensar o que ele e aquele maldito velho podem tá tramando, já dá um cagaço."

        c "Olha eu."

        scene pri6_img10 with Dissolve(1.0)

        c "E aí? Gostou?"

        if not p5_naoviajou:

            c "Ou será que já enjoou?"

            mc safado "Claro que não. Como enjoar de uma vista dessas?"

        mc "Gostei muito. Você tá linda."

        c "Obrigada."

        c "Eu acho ela um pouco curta demais. Mal cobre meu busto e minha bunda."

        mc envergonhado "Isso é verdade..."

        c "Mas parece que é algo importante pra atrair a atenção de adolescentes e jovens adultos, eles me disseram."

        mc desconfiado "Entendi..."

        c "O produtor me contou que é muito fácil fazer esse público gostar de um filme. É só colocar uma mulher bonita com uma roupa curta."

        c "E um cara sem camisa, claro. Se der, até mostrar a bundinha do cara e uma cena da mulher tomando banho meio escondido assim."

        mc envergonhado "Você tá querendo dizer que esse pessoal é fácil de serem manipulados."

        c "Acho que é isso. Tipo, eles não tão nem aí pra diálogos bem escritos ou um bom enredo, muitos só querem ver putaria mesmo."

        mc "Imagino que tenha um monte por aí."

        mc desculpa "Mas você não se sente mal de ter pessoa que vai ver o filme só pra poder ver você assim?"



        c "Assim... eu não penso muito nisso. Só que eu sou modelo há alguns anos, e eu meio que acostumei nas pessoas quererem me ver."

        c "Às vezes eu fico pensando se não é ruim as pessoas só se interessarem em mim por conta do meu corpo ou do meu jeitinho meigo."

        c "Eu acho que eu tenho outras coisas, sabe. Coisas pra falar, opiniões sobre as coisas."

        c "Só que eu vejo muita gente falando na internet que eu sou burra. Mas ninguém me pergunta!"

        mc "Sei... Parece que eles já sabem o que querem de você."

        scene pri6_img9 with Dissolve(1.0)

        c "Isso mesmo! Essa é a parte que cansa, sabe..."

        c "Não é porque algumas modelos não têm nada na cabeça, que todas vão ser assim."

        mc normal "Falou tudo."

        c "Eu espero que o filme mude isso, sabe."

        mc desconfiado "O filme?"

        c "É. Eu vou ter uma chance de mostrar que eu não sei só colocar uma roupa bonita e ser fotogênica."

        c "Eu vou atuar, e passar sentimentos. As pessoas vão me ver com outros olhos. Vão ver que eu tenho outros talentos."

        mc normal "Entendi. É uma grande oportunidade pra você."

        scene pri6_img11 with Dissolve(1.0)

        c "Sim!"

        mc "E o que você acha das falas? Estão legais?"

        c "Hmm... é um filme de fantasia, né? Não tem muito drama e talz. É mais luta e umas frases feitas."

        c "Não sei se é o melhor filme pra eu mostrar meus talentos... mas é um começo, certo?"

        mc desculpa "Sim... claro..."

        "A [c] parece que não consegue ver as coisas... deu até dó dela agora..."

        mc normal "Eu tenho certeza que com o tempo você vai conseguir outros papéis."

        c "Obrigada, [mc]. Eu fico feliz de saber que você tá torcendo por mim."

        mc charmoso "Claro. Eu vou sempre torcer por você."

        c "Hihi..."

        c "Caraca. A gente falou um monte."

    label priscila_e6_after_marco2:

        c "As gravações vão continuar. Vamos comigo pro set?"

        mc normal "Claro."

        c "Hoje a gente vai gravar a cena da batalha final entre minha personagem e aquele orc verde."

        mc "Que bacana. Espero que você acabe com ele."

        scene pri6_img10 with Dissolve(1.0)

        c "Vai ser uma batalha e tanto. Ele vai me agarrar, e eu vou me debater, mas ele é muito mais forte do que eu."

        c "Então eu-"

        mc tarado "..."

        c "[mc]?"

        mc surpreso "Ah! Tô ouvindo!"

        c "Você tá fazendo uma cara estranha."

        mc envergonhado "Não foi nada hehe... vamos lá?"

        c "Vamos."

        "Esse filme..."

        play sound "audio/som_24_passos2.mp3"

        scene black with Dissolve(1.0)

        "..."

        scene vila_magica_entrada with Dissolve(1.0)

        pause

        mc "Essa parte do set é muito real. Parece até a entrada de um centro comercial de um jogo de fantasia."

        c "Nossa, que específico, hein."

        mc "Sei lá porque eu disse isso haha..."

        scene rua magica2 with Dissolve(1.0)

        c "Chegamos."

        scene pri5_img9 with Dissolve(1.0)

        c "O pessoal já tá se preparando pra gravar."

        mc normal "Pode ir lá se preparar. Eu vou ficar aqui e dar uma olhada."

        c "Ah, é chato. Vai ser melhor se você der uma uma volta. O set é imenso. Tem muita coisa pra você ver."

        mc desconfiado "Mas eu vim por sua causa. Não-"

        c "Eu que estou falando pra você ir."

        mc "Mas-"

        c "Nada de 'mas'. Vai dar um passeio. Eu vou me sentir melhor."

        c "A gente se encontra lá no meu camarim em umas três horas, tudo bem?"

        mc "Combinado. Bom trabalho."

        if priscila_namoro:

            c "Até daqui a pouco, lindo."

            mc "Eu sei que não é fácil namorar uma estrela do cinema."

            c "Você tá indo bem. Beijo."

            mc "Beijo."

        scene rua magica2 with Dissolve(1.0)

        "Nossa, parece que a [c] não quer que eu fique aqui vendo. Por que será?"

        "Bom..."

        "E agora?"

        "..."

        scene priscila rua_magica with Dissolve(1.0)

        "A [c] vai passar as próximas horas gravando. Acho melhor eu seguir o conselho dela e dar o fora daqui."

        "..."

        scene vila_magica_entrada with Dissolve(1.0)

        if not p5_naoviajou:

            "Da outra vez eu visitei dois lugares. Acho que hoje eu vou pra outro lado."

        "Tem toda uma floresta por aqui. Acho que eu vou dar uma andada aqui por perto."

        scene set_floresta1 with Dissolve(1.0)

        "..."

        "Cara. Olha só pra isso aqui. Essa floresta é imensa."

        "Eu já tô andando tipo meia hora."

        "Pior é que eu nem tenho mais certeza da onde eu vim."

        mc desconfiado "Hm? Tem um lago ali."

        play sound "audio/som_24_passos2.mp3"

        "..."

        "Acho que eu vou sentar um pouco."

        scene mc_sentado_floresta with Dissolve(1.0)

        pause

        "Não é possível que fizeram tudo isso aqui pra fazer um filme. Quem constrói uma floresta? Acho que nem é possível."

        "O dinheiro que esses caras têm não é brincadeira."

        "A [c] disse que esse filme é a produção mais cara da história do país. Com certeza é algo gigante."

        "E colocar tudo isso nas mãos de um velho tarado que abusa de-"

        "???" "Você?"

        mc "Hm? Quem-"

        scene agata_mc_sentados1 with Dissolve(1.0)

        pause

        ag "Opa."

        if not p5_naoviajou:

            mc "Ah! A atriz. Eu lembro de você."

            ag "Boa tarde, moço."

            mc "Boa tarde."
        else:


            mc "Q-quem é você?"

            $ ag_nome = "Ágata"

            ag "Meu nome é [ag] e eu sou uma das atrizes do filme."

            mc "Puxa, que bacana."

        ag "O que você tá fazendo aqui sozinho?"

        mc "Eu queria dar alguma razão mais inteligente, mas é que eu acabei andando sem rumo e cansei."

        ag "Haha... você não tem medo de passar vergonha, né?"

        mc "Ei..."

        ag "Você veio com a [c], né?"

        mc "Sim."

        ag "Hmm..."

        mc "Que foi?"

        ag "Estou só dando uma boa olhada em você."

        mc "Ok..."

        "..."

        ag "Como tá sua relação com a [c] agora?"

        ag "Continua namorando ela?"

        mc surpreso "Co-como assim continuo?!"

        mc envergonhado "Eu não sei do que você tá falando..."

        ag "Não me vem com essa."

        scene agata_mc_sentados2 with Dissolve(1.0)

        pause

        ag "Vai, fala."

        mc "Falar o que?"

        ag "Para de se fazer de idiota. Vocês tão ou não namorando."

        menu:

            "Falar a verdade e dizer que estão namorando" if priscila_namoro:

                $ agata_priscila = True

                "Será que é uma boa falar que a gente tá namorando pra uma desconhecida? Bom, foda-se."

                mc "A gente tá namorando, sim. E daí?"

            "Mentir e falar que estão namorando" if not priscila_namoro:

                "Como será que ela vai reagir se eu falar que a gente namora?"

                $ agata_priscila = True

                mc "A gente tá namorando, sim. E daí?"

            "Falar a verdade e dizer que são amigos" if not priscila_namoro:

                "Não tenho porque mentir sobre isso."

                mc "A gente é só amigo. De verdade."

            "Mentir e falar que são apenas amigos" if priscila_namoro:

                "Melhor não revelar pra ela que a gente tá namorando."

                mc "A gente é só amigo."

        if agata_priscila:

            ag "Eu sabia! Vocês tão tentando esconder, né?"

            mc "Sim. Não vai abrir a boca."

            ag "Pode deixar..."

            ag "Hmm..."

            mc "Que foi agora?"

            ag "Tô tentando descobrir o que ela viu em você."

            mc "A é? E aí?"

            ag "Assim, você não é bonito."

            mc "Ei..."

            ag "Mas tem alguma coisa em você... não sei se é seu cheiro... alguma coisa que me atrai."

            ag "Você com certeza tem alguma coisa, uma confiança, não sei..."

            ag "Eu tenho quase vontade de dar pra você aqui mesmo."

            mc "Ou! Ou! Calma aí!"
        else:


            ag "Será mesmo?"

            ag "..."

            ag "Que merda..."

            mc "Que foi?"

            ag "Eu acredito em você."

            mc "E que que tem? Qual o problema?"

            ag "Seria mais legal se você fosse namorado dela."

            mc "Legal como?"

            ag "Você pergunta demais. Deixa eu fazer uma pergunta agora."

        ag "Posso chegar mais perto de você?"

        mc "Opa! Como assim?! Perto como?"

        ag "Posso? Não tem ninguém aqui."

        "O que ela quer dizer com isso?! Essa mina é louca?"

        menu:
            "Deixar ela se aproximar":


                mc "Tudo bem. Mas não entendi o que-"

                scene agata_mc_abracados1 with Dissolve(1.0)

                pause

                mc "Uou!"

                ag "..."

                mc "[ag]. O que é voc-"

                ag "Xiu..."

                ag "Só deixa eu aqui..."

                "Essa mina tem algum problema."

                "Se bem que ela é bem cheirosa. E ela tá encostando a bunda bem no meu..."

                ag "Tá gostando?"

                mc "E-eu?"

                ag "Eu sou cheirosa, né?"

                mc "E-e-eu acho..."

                if agata_priscila:

                    ag "Me abraça?"

                    mc "C-como?"

                    ag "Me abraça."

                    "Que que tá acontecendo aqui? Como a gente chegou nisso?"

                    menu:
                        "Melhor não.":


                            mc "Melhor não, [ag]. Eu já nem devia ficar com você assim. E se um paparazzo vê a gente?"

                            ag "Mas tem um paparazzo me vendo."

                            mc "Quê?!"

                            ag "Você, bobo."

                            mc "Idiota..."

                            ag "Idiota é a mãe!"

                            mc "Desculpa..."

                            jump priscila_e6_agata_conversa
                        "Claro.":


                            $ agata_beijo = True

                            mc "Claro."

                            scene agata_mc_abracados2 with Dissolve(1.0)

                            ag "Hmm... assim. Assim eu posso sentir você melhor."

                            "Não tô conseguindo mais aguentar. Essa mina tá me deixando louco."

                            "Só a gente aqui no meio dessa floresta. Ela praticamente sem roupa."

                            ag "Eu tô sentindo o amigo crescendo. Ele tá gostando de sentir minha bunda?"

                            mc "Ele tá..."

                            ag "Eu sabia que ele ia gostar. Deixa eu me ajeitar melhor aqui."

                            "Meu Deus! Essa mina é muito abusada! Ela tá se roçando em mim."

                            ag "Melhorou agora?"

                            mc "Acho que você precisa se ajeitar melhor."

                            ag "Também acho."

                            "..."

                            mc "Não vou aguentar assim."

                            ag "Não precisa aguentar. Pode fazer o que precisa fazer."

                            ag "Hmm..."

                            ag "Agora vem aqui."

                            mc "Mas-"

                            ag "Vem aqui agora."

                            mc "..."

                            scene agata_mc_beijo with Dissolve(1.0)

                            pause

                            ag "Isso. Me beija."

                            mc "..."

                            ag "Fala que eu beijo melhor que a [c]."

                            mc "Por que?"

                            ag "Fala logo."

                            menu:
                                "Você beija melhor que a [c].":


                                    jump priscila_e6_agata_beijo
                                "...":


                                    mc "..."

                                    ag "Não vai falar?"

                                    ag "Então chega."

                                    menu:
                                        "Ok, ok. Você beija melhor que a [c].":


                                            label priscila_e6_agata_beijo:

                                                mc "Você b-beija melhor que a [c]."

                                            ag "Eu sei. Eu sou muito mais mulher que ela. Você tá vendo?"

                                            mc "Eu tô."

                                            ag "Sempre que você quiser, pode se satisfazer comigo."

                                            ag "Eu tô aqui pra você, tá?"



                                            "Ela disse que eu posso me satisfazer quando eu quiser... será que não pode ser agora?"

                                            label pri6_agata_premium:

                                                pass

                                            "Será que pode dar problema com a Pri? Eu demorar muito pra voltar? E agora?"

                                            menu:
                                                "Melhor não falar nada":


                                                    mc "Tá. Agora eu que-"
                                                "Eu quero me satisfazer agora.":


                                                    if not premium:

                                                        call mensagem_premium from _call_mensagem_premium_2

                                                        jump pri6_agata_premium

                                                    mc "Se você vai me satisfazer quando eu quiser, a gente podia começar agora. O que você acha?"

                                                    ag "Agora? Hmm... eu adorei quando você disse que eu sou mais mulher que a Pri. Acho que você merece."

                                                    mc "Obaa..."

                                                    scene black with dissolve

                                                    scene pri6_img13 with Dissolve(1.0)

                                                    pause

                                                    ag "O que você acha? É material de uma protagonista?"

                                                    mc "Com certeza."

                                                    ag "Incrível alguém não querer uma coisa assim, né?"

                                                    mc "Impossível. Eu quero muito isso."

                                                    ag "Você quer?"

                                                    mc "Agora."

                                                    ag "Acho que eu vou deixar você aproveitar... um pouquinho disso aqui."

                                                    mc "Isso..."

                                                    scene pri6_img12 with Dissolve(1.0)

                                                    pause

                                                    ag "Então fica quietinho que eu vou cuidar de você. Eu sou muito boa em deixar os homens satisfeitos."

                                                    mc "Sério?"

                                                    ag "Você vai ver..."

                                                    mc "Você é linda, [ag]."

                                                    ag "Eu sei."

                                                    ag "Meu rosto é lindo, meu corpo é magro, mas meus seios são grandes... e minha bunda é durinha."

                                                    mc "Parece... {i}gulp{/i}... s-saboroso..."

                                                    ag "Você vai poder provar um pouquinho agora."

                                                    ag "Tira essa calça..."

                                                    mc "Na hora."

                                                    scene pri6_img14 with Dissolve(1.0)

                                                    pause

                                                    ag "O que é isso que eu tô sentindo apertando minha bunda, huh?"

                                                    mc "O que você acha?"

                                                    ag "Parece que você já tá pronto."

                                                    mc "Eu tô. Olhar pra você deixou ele assim. E você?"

                                                    ag "Eu nasci pronta, querido."
                                                    scene pnew_ani01 with Dissolve(1.0)
                                                    mc "Você é muito macia, [ag]..."

                                                    ag "Eu sei como é. Meu corpo deixa qualquer um assim... pode aproveitar ele pra chegar lá."

                                                    menu:
                                                        "Ok...":


                                                            mc "Eu quero aproveitar."
                                                        "Posso enfiar?":


                                                            mc "Eu posso enfiar?"

                                                            ag "Você quer tanto assim?"

                                                            mc "Muito..."

                                                            ag "Hoje não."

                                                            ag "Mas eu aposto que eu consigo fazer você gozar assim."

                                                    ag "Pode esfregar na minha bunda, na minha buceta, nas minhas coxas... é tudo seu."

                                                    mc "A-ah..."

                                                    scene pri6_img14 with vpunch

                                                    mc "HMM!"

                                                    ag "Você parece animado, [mc]."

                                                    ag "Continua assim... que eu tô adorando."
                                                    scene pnew_ani01 with Dissolve(1.0)
                                                    mc "Tá gostando, né!"

                                                    ag "Tô!"

                                                    "Eu tô ficando doido sentindo meu caralho roçando nela."

                                                    mc "Eu vou enfiar!"

                                                    ag "Nãão... eu falei que, não, ouviu?!"

                                                    menu:
                                                        "Enfiar nela mesmo assim.":


                                                            scene pri6_img15 with vpunch

                                                            pause

                                                            mc "Epa!"

                                                            ag "Ainnn! Filha da puta, tu meteu!"
                                                            scene pnew_ani02 with Dissolve(1.0)
                                                            mc "Não aguentei, você é gostosa demais, Ágata!"

                                                            ag "Mais gostosa que a Priscila?"

                                                            mc "Muito mais!"

                                                            ag "Ai, caralho, então mete, vai! Fode gostoso!"

                                                            scene black with dissolve

                                                            scene ani18 with Dissolve(1.0)

                                                            pause

                                                            mc "Ahh! Isso, sim!"

                                                            ag "Ahnnn! Ainnn!"

                                                            ag "Tô fodendo o namorado da Pri! Que delícia!"

                                                            mc "Tô traindo ela contigo, safada! Você é a outra!"

                                                            ag "Eu sou! Porque eu sou mais gostosa! Por isso que tu prefere me foder!"

                                                            ag "Eu sou melhor em tudo! Aaahnn! Por isso você é um traidor fdp!"

                                                            mc "E cavalga gostoso pra caralho!"

                                                            ag "T-tudo! Aahh! Eu faço tudo gostoso! Tudo mundo acha!"

                                                            menu:
                                                                "Até o Gustav?":


                                                                    ag "Quê?! O velho tarado?!"

                                                                    mc "Eu sei o que ele faz."

                                                                    ag "Ele não faz nada... o filho da puta..."

                                                                    mc "Não faz nada mesmo? Você não é a preferida dele?"

                                                                    ag "Eu sou a preferida... aah... mas ele não faz nada com aquele pau mole dele."

                                                                    mc "Sei... e o Marco?"

                                                                    ag "Aah... aaah!"

                                                                    ag "Ele é grande! Mas não quer saber disso!"

                                                                    mc "Então eu que te fodo pra valer, é?!"

                                                                    ag "É! Você! Aahnn!"
                                                                "Eu vou gozar, delícia!":


                                                                    ag "Gozaa!"
                                                        "Continuar roçando":


                                                            pass

                                                    mc "Eu tô chegando lá, [ag]!"

                                                    ag "Isso! Goza pra mim, gostoso!"

                                                    ag "Joga toda sua porra na minha bunda!"

                                                    mc "Eu vou!!!"

                                                    scene pri6_img15 with vpunch

                                                    mc "AAAHHH!"
                                                    scene pnew_ani02 with Dissolve(1.0)
                                                    ag "Ai! Quanta porra!"

                                                    mc "{i}puf puf{/i}"

                                                    scene black with dissolve

                                                    scene pri6_img16 with Dissolve(1.0)

                                                    pause

                                                    ag "Gozou gostoso?"

                                                    mc "Muito..."

                                                    ag "Acho bom. Se quiser de novo, só me falar."

                                                    mc "T-tá..."

                                                    ag "Agora eu vou sair."

                                                    mc "Mas já? E-"

                                                    ag "Venha mais vezes aqui pro estúdio, [mc]."

                                                    ag "A gente tem muito o que conversar."

                                                    jump priscila_e6_agata_after
                                        "Tá certo.":


                                            mc "Ok. Vamos parar."

                                            ag "{i}Hmpf{/i}"

                            scene agata_mc_abracados2 with Dissolve(1.0)

                            ag "Agora eu vou sair."

                            mc "Mas já? E-"

                            ag "Venha mais vezes aqui pro estúdio, [mc]."

                            ag "A gente tem muito o que conversar."

                            jump priscila_e6_agata_after
                else:


                    ag "Eu sinto que você gosta muito da [c]."

                    mc "Sente é?"

                    ag "Você sente alguma coisa quando me vê?"

                    mc "Não entendi. A gente nem se conhece..."

                    scene agata_mc_sentados1 with Dissolve(1.0)

                    jump priscila_e6_agata_conversa
            "Falar pra ela ficar onde está":


                mc "Melhor você ficar aí. Eu tô conseguindo te ouvir. Tá bem silencioso."

                ag "Você é um homem difícil."

                mc "Não é isso..."

                scene agata_mc_sentados1 with Dissolve(1.0)

        label priscila_e6_agata_conversa:

            ag "Aqui... você me acha feia?"

            mc "N-Não é isso, [ag]."

            mc "Eu te achei linda. E você parece uma garota muito divertida, legal."

            mc "Mas é melhor a gente não abusar. Vai saber o que vão pensar se pegarem a gente juntos aqui."

            ag "Você é covarde, só isso."

            mc "Pode falar o que quiser..."

            ag "Essa sua confiança tá me irritando. Você se acha muito superior."

            mc "..."

            ag "Vai! Fala alguma coisa!"

            mc "Por que você precisa ficar brigando assim? Você tá sendo mimada."

            ag "De novo. Tá sendo todo superior..."

            mc "Desculpa."

            ag "Não pede desculpas! Você só parece melhor ainda!"

            mc "Haha... não sei o que falar então."

            ag "..."

            mc "Você não tá legal, né?"

            ag "Não interessa."

            play sound "audio/som_37_arbusto.mp3"

            "!"

            mc "Hm? Você ouviu alguma coisa?"

            ag "Não!"

            mc "Tá... Olha..."

            mc "Seja lá o que tá rolando, se você precisar de alguém, pode falar comigo, tá legal?"

            mc "Anota meu número."

            ag "..."

            scene agata_mc_sentados2 with Dissolve(1.0)

            ag "Você tá achando mesmo que eu preciso de algum zé ninguém igual você pra conversar?"

            ag "Eu sou uma atriz, idiota. Eu posso não ser a estrela, mas esta é a maior produção que o país já viu!"

            mc "Eu sei, mas-"

            ag "Haha! Não me faça rir. Você é muito baka mesmo!"

            mc "Baka?"

            ag "Não importa."

            ag "Agora eu vou fazer algo útil com a minha folga que não seja ficar ouvindo um palerma."

            mc "Ok..."

            ag "Tchau!"

            scene set_floresta1 with hpunch

            "..."

            "Ixi..."

    label priscila_e6_agata_after:

        scene mc_sentado_floresta with Dissolve(1.0)

        "Essa [ag]..."

        "Ainda não entendi qual é a dela."

        if marco_gustav:

            "O pior é que quando o [mar] tava falando com [gus] hoje mais cedo, eles falaram de uma [ag]."

            "Certeza que é ela."

            "Então depois de usar ela, o [gus] trocou ela pela [c]."

            "E provavelmente ele fez o mesmo com outras e vai fazer com a [c] também."

            "Alguém precisa parar esse canalha."

        play sound "audio/som_37_arbusto.mp3"

        "Hm?"

        if not agata_beijo:

            "De novo esse barulho?"
        else:


            "Que barulho foi esse?"

        "Deixa eu levantar."

        scene set_floresta1 with dissolve

        "Parece que veio dalí."

        "Tô começando a ficar meio assustado sozinho aqui."

        "Melhor eu vo-"

        scene marco_floresta_bu with hpunch

        mar "Bú!"

        mc angustiado "AH!"

        mar "Desculpa, [mc]. Foi um pedido do [gus]."

        mc "[mar]! Não!"

        scene marco_floresta_chute with hpunch

        pause

        mc "{i}AKKH!{/i}"

        mar "Bons sonhos."

        scene black with hpunch

        "Filho da puta..."

        "Ai..."

        pause

        scene set_floresta1 with dissolve

        scene black with dissolve

        "Onde eu tô?"

        mar "[gus]?"

        mar "..."

        mar "Eu sei. Perdão, senhor. É coisa rápida."

        mar "Eu peguei ele."

        mar "..."

        mar "Na sua sala? Por que?"

        mar "..."

        mar "Senhor, isso é arriscado demais. Por que se envolv-"

        mar "..."

        mar "Ok. Sim, senhor."

        mar "..."

        mar "Sim, senhor. Entendi."

        mar "Era isso."

        mar "..."

        mar "Ok."

        "..."

        "Merda..."

        "..."

        pause

        scene marco_mc_carregando with Dissolve(1.0)

        mc "Ai."

        mar "Acordou?"

        mc "O que vo- ai!"

        mar "É. O chute vai começar a doer agora."

        mc "Seu... desgraçado..."

        mar "Desculpa, maninho. Só seguindo ordens."

        if marco_gustav:

            mc "O [gus] mandou, agora você vai me 'passar'..."

            mar "Eu suspeitei mesmo que tinha alguém ouvindo a gente aquela hora."

        mc "E agora? O que vai acontecer?"

        mar "Minhas ordens eram matar você, mas mudaram e me mandaram te deixar aqui."

        mc "Como você consegue falar isso com essa naturalidade?"

        mc "Você tá falando em matar alguém. Tirar uma vida. Você não percebe isso? Ai!"

        mar "Calma. Deita aqui."

        "..."

        scene marco_mc_sala1 with Dissolve(1.0)

        mc "Caralho... tá doendo muito."

        mar "..."

        mc "Então. {i}cof{/i}..."

        mc "Não entra na minha cabeça como você consegue... falar em matar desse jeito."

        mar "Veja, [mc]. Existem várias realidades. Cada pessoa tem uma história. O que é difícil pra você pode não ser pra mim."

        mc "Sério mesmo que você tá filosofando antes de me dar um tiro?"

        mar "..."

        mc "Tudo isso por que eu me meti com a [c]?"

        mar "Basicamente."

        mc "Por que você é o cachorrinho de um velho nojento? Você não tem ética? É só pelo dinheiro?"

        mar "Eu sei que as coisas podem parecer assim pra você, mas é um pouco mais complexo do que isso."

        mc "Pra mim parece bem óbvio."

        mar "Veja... o [gus] pode pensar o que ele quiser, mas eu não trabalho pra ele."

        mc "Quê? Como assim?"

        mar "Eu trabalho pra um... aliado do [gus]. É do interesse dele que o [gus] esteja satisfeito."

        mc "E você tá falando isso pra mim por que? Tipo um vilão revelando o plano antes da morte do herói?"

        mar "Haha! Acho que você tá se achando demais, [mc]. Você é só mais um coitado que mexeu com as pessoas erradas por azar."

        mc "Desgraçado..."

        mar "Você tem um grande poder em suas mãos. Se você soubesse como usar ele..."

        menu:
            "Poder? Tipo magia?":


                mc "Poder? Tipo magia?"

                mar "Hahaha! O medo tá te fazendo perder o juízo, [mc]. Não seja ridículo."

                mc "Então o que?"
            "Poder sobre a [c]?":


                mc "Você diz que eu tenho influencia sobre a [c]?"

                mar "Parece que ela realmente te escuta. E é isso que irrita o velho."

                mar "Mas não tô falando disso."

        mar "Bom... deixa pra lá."

        mc "Já que você tá disposto a falar comigo..."

        scene marco_mc_sala2 with Dissolve(1.0)

        mc "Ai."

        mar "Cuidado."

        mc "Pode me responder mais uma coisa?"

        mar "Diga."

        mc "Por que o [gus] é tão importante pra você?"

        mar "Pra mim não. Pro meu chefe."

        mc "Que seja..."

        mar "É bem simples e óbvio. Os filmes do [gus] dão dinheiro."

        mar "Ele é um velho... excêntrico... mas o poder de atingir números ridículos nas bilheterias é inegável."

        mc "E seu chefe tem participação nisso tudo?"

        mar "Com certeza."

        mc "E por que você fica atrás do [gus] o tempo todo?"

        mar "Acho que você já perguntou demais, [mc]."

        mc "..."

        mar "Eu vou ver com ele o que tá acontecendo."

        mc "..."

        mar "Só uma coisa. Fique claro que eu e meu chefe não concordamos com tudo o que o [gus] faz."

        mar "Mas sem o [gus] perderíamos uma das nossas fontes de renda. Por isso ele vai continuar comendo todas as garotas que ele quiser, entendeu?"

        mar "Eu não me importo com a [cc] ou se você acha isso nojento. A vida não é fácil e muito menos simples, [mc]."

        mar "Nós fazemos o que precisamos pra chegar onde queremos. Ética, moral, isso é coisa que pessoas como meu chefe inventaram pra manter vocês no lugar."

        mc "!"

        mc "Esse seu jeito... Você me lembra uma outra pessoa que eu conheço."

        mar "Deve ser uma pessoa inteligente. Agora com licença."

        scene sala_gustav with Dissolve(1.0)

        "..."

        "Isso parece tão surreal que eu nem sei o que pensar."

        "Pode ser que eu morra daqui alguns minutos e eu tô convesando com o idiota que vai me matar. Parece tão ridículo que dá vontade de rir."

        "Mulher" "{size=17}Tomara que ele ainda esteja aqui.{/size}"

        mc desconfiado "?"

        "{i}Gatchak{/i}"

        mc surpreso "Você!"

        a "[mc]... É a [a]. Lembra de mim?"

        mc "[a]! Isso!"

        scene miranda_mc_sofa1 with Dissolve(1.0)

        pause

        a "O que aconteceu com você? Você tá branco, menino."

        mc "..."

        a "Fala alguma coisa!"

        mc "Não sei mais o que falar..."

        a "Calma. Respira, [mc]. Você tá bem."

        mc "O [mar] ia me matar a pedido do [gus] e daí ele me deixou aqui falando que mudaram as ordens dele. E agora você aparece."

        mc "Tudo isso é tão absurdo, que deu até preguiça."

        a "Claro que isso é um absurdo, [mc]. Ninguém vai te matar. Pare de pensar besteiras."

        mc "Mas o [mar] disse..."

        a "Não escute aquele idiota. Ele só tá querendo te assustar."

        mc "Mas ele me bateu! Ele me chutou!"

        mc "Que porra tá acontecendo, [a]?!"

        a "Isso eu acredito. Eu falei pra você, não falei? Que não era pra você se meter nisso?"

        if priscila_namoro:

            mc "Tudo isso por que eu tô namorando a [c]?"

            a "Óbvio! O que eu te falei?!"
        else:


            mc "Mas a gente é só amigos!"

            a "Não importa mais pra ele."

        a "O [gus] tá puto com você. E com a [c] também. Ele tá vendo essa sua vinda pro estúdio como uma afronta direta."

        a "Você precisa sair daqui o mais rápido possível e não voltar mais. E de preferência não fale mais com a [c]."

        mc "Não... falar..."

        show black with dissolve

        hide black with dissolve

        mc "Ai. Eu não tô conseguindo respirar, [a]."

        a "Calma. Você vai ter um treco assim. Deita aqui."

        scene miranda_mc_sofa2 with Dissolve(1.0)

        pause

        a "Isso. Eu vou cuidar de você."

        mc "..."

        mc "Eu sou só um jornalista, [a]. Eu queria as pautas... depois eu só queria ajudar a [c]..."

        a "Eu sei... calma..."

        mc "O [mar] me falou do chefe dele... como se tivesse contando um plano maligno antes de me fuzilar."

        a "[mc]... Você tá levando tudo isso de forma muito fantasiosa."

        a "É muito mais simples do que você tá pensando."

        a "Tem um homem poderoso com ciúmes de você. E, infelizmente, ele tem um segurança que mais parece um gorila."

        a "Ele vai te surrar e te jogar em uma sarjeta se você continuar vendo a [c]."

        mc "Mas-"

        scene miranda_mc_sofa3 with Dissolve(1.0)

        pause

        a "Não tem mais nada."

        a "Eu preparei um avião particular pra te levar de volta pra ilha. Você vai subir nele, voltar e esquecer tudo isso."

        mc "E a [c]?"

        a "Não se preocupe. Eu vou falar pra ela que você passou mal e teve que voltar."

        mc "Eu não posso mais falar com ela?"

        a "Poder você pode. Ninguém vai te amarrar na cama. Mas eu não recomendo você ligar pra ela por um tempo."

        a "Pra mim, o melhor seria você só esquecer ela, mas você é muito importante pra [c]."

        a "Ela tava muito fragilizada e se não fosse por você nem sei o que teria acontecido com a garota."

        mc "Você diz do viaduto?"

        a "Não só isso. Aconteceram algumas coisas com a [c] e tudo isso-"

        mc "Não precisa falar assim. Eu sei que ela precisa transar com o [gus] por causa do papel no filme."

        a "Sim..."

        mc "Isso que me irrita, [a]. Você sabe disso e não faz nada!"

        a "..."

        mc "Fale alguma coisa, mulher!"

        a "Você tem todo o direito de me odiar, mas não é tão simples como você pensa, [mc]."

        a "Tem muito mais coisa em jogo aqui. Tudo o que aconteceu com a [c] é só uma pequena mancha no currículo dessas pessoas."

        mc "Como assim 'dessas pessoas'? De quem você tá falando?"

        mc "O [mar] me falou que ele não trabalha pro [gus], mas pra outro chefe."

        a "..."

        a "Isso é coisa demais pra você. Levanta. Vamos sair daqui."

        mc "Ei."

        scene sala_gustav with Dissolve(1.0)

        a "Vem. O avião deve estar pronto."

        mc bravo "[a]!"

        a "Você quer apanhar de novo? Então vem logo."

        mc bravo "Merda..."

        scene black with dissolve

        "..."

        a "Aqui."

        mc "T-tá."

        scene miranda_mc_aviao1 with Dissolve(1.0)

        pause

        a "Boa viagem. Não se preocupe que a [c] não vai saber de nada."

        mc "Eu não posso nem escolher se eu vou ou fico aqui?"

        a "Não. Porque se você escolhesse ficar com certeza seria game over pra você. Agora vai."

        mc "Mas você diss-"

        a "Eu disse vai."

        mc "Calma. Tá."

        a "Certeza que a [c] vai te chamar pra conversar. Veja bem o que você vai fazer."

        menu:
            "Eu vou falar com ela. Foda-se essa gente.":


                mc "Claro que eu falar com ela."

                mc "Eu não tô nem aí pra essas pessoas. Depois de hoje, sei lá o que pensar disso tudo. Nem consigo ter medo mais."
            "Não quero causar. Vou pensar bem.":


                mc "Eu não quero mais problema. Pode deixar que eu vou pensar bem."

        a "Eu sei que foi um pouco pesado pra você. Só que você vai se recuperar. Toma cuidado, tá?"

        a "Você é um cara bacana, [mc]."

        mc "..."

        mc "[a]... eu não acho que as coisas estão acontecendo sejam boas, sabe."

        a "Eu sei, eu sei. Pode deixar que eu vou ajudar você resolver tudo isso."

        mc "Sério?"

        a "Claro. Não vai esquecer quem te tirou da sala do [gus]."

        mc "Sala do-"

        a "Eu tô do seu lado, [mc]. Você acredita em mim?"

        menu:
            "Acredito.":


                mc "Acredito."

                mc "Muito obrigado por tudo o que você tá fazendo, [a]."

                a "Eu só quero ver você e a [c] bem, tá?"

                mc "Tá."
            "Não consigo decidir isso agora.":


                mc "Não sei. Não consigo pensar nisso agora."

                a "Tudo bem. Olha, eu só quero ver você e a [c] felizes."

                a "Eu sei que tem muita coisa que você não entende. Mas não adianta acelerar as coisas."

                a "Às vezes nossa cabeça viaja e a gente acha que tem mais coisa do que realmente tem."

                mc "Sei..."

        if not priscila_namoro:

            a "Você é um homem e tanto. E eu queria muito que a gente tomasse alguma coisa juntos um dia."

            a "A gente pode aproveitar que você e a [c] são só amigos, não acha?"

            mc "A-acho que sim."
        else:


            a "Eu sei que você e a [c] estão juntos..."

            mc "Hm?"



        a "Mas tem alguma coisa que eu possa fazer pra você aceitar o que eu tô falando?"

        mc "Como assim?"

        scene pri6_img17 with Dissolve(1.0)

        pause

        mc "O-oi?"

        a "Agora você entende?"

        mc "É-é..."

        a "A gente não tem muito tempo, mas eu sei ser bastante persuasiva... eu... sei como convencer um homem."

        "Será que ela tá falando do que eu tô pensando?"

        a "Acho que agora você entendeu."

        label pri6_miranda_premium:

            pass

        "É certo eu me aproveitar dela assim? A [a] com certeza é gata pra caramba, só que... e agora?"

        menu:
            "Me convença.":








                $ miranda_aviao = True

                mc "Eu não sabia que você tava tão interessada assim na minha ajuda."

                a "Você e a [c] são um time. Entende?"

                mc "N-não sei... mas eu tô gostando de onde isso tá indo."

                a "Era só o que eu precisava ouvir."

                a "Por que você não tira essa roupa e deixa que eu te convença?"

                mc "C-combinado."

                scene black with dissolve

                scene pri6_img18 with Dissolve(1.0)

                pause

                a "O que você acha de mim, hein?"

                mc "V-você é incrível."

                a "Você tá olhando bastante... deve ter gostado."

                mc "Eu adorei."

                a "Eu não mostro eles pra todo mundo. Você é um dos únicos que já me viram assim, sabia?"

                mc "A é?"

                a "Por que você não olha mais de perto?"

                mc "P-posso?"

                a "Claro, querido. Eles tão aqui pra você."

                scene pri6_img19 with Dissolve(1.0)

                pause

                a "Melhor assim, né?"

                mc "Perfeito."

                mc "Você cheira bem, [a]."

                a "Eu sou vaidosa. Eu gosto de cheirar bem, me vestir bem, estar bem."

                mc "Dá pra ver..."

                a "Parece que alguém aqui embaixo também gostou de mim."

                mc "Muito."

                a "Que bom que eu consegui agradar vocês dois."

                a "E então? Você tá do meu lado? Você vai tomar cuidado quando for falar com a Pri?"

                mc "É..."

                "Ela fez a parte dela. Será que eu paro aqui?"

                menu:
                    "Sim. Você foi convicente.":


                        mc "Vocês foram bem convincentes. Eu tô do seu lado."

                        a "É bom saber que a gente conseguiu convencer você. Nosso charme continua."
                    "Não foi o suficiente.":


                        mc "Acho que você fez uma boa introdução..."

                        a "Introdução, hm?"

                        mc "É... meu pau tá pronto... mas se você parar agora... não vai dar..."

                        a "Vocês, garotos de hoje em dia, são mimados demais."

                        mc "Me mima um pouquinho..."

                        a "Você sabe negociar... combinado."

                        a "Então tira a calça. Deixa eu garantir que o bonitão aqui vai sossegar."

                        mc "Boa..."

                        scene black with dissolve

                        scene pri6_img20 with Dissolve(1.0)

                        pause

                        a "Deixa eu molhar ele um pouquinho..."

                        mc "T-tá!"

                        "Nossa! Ela realmente vai fazer um oral em mim?"

                        a "Você tá até tremendo... que bonitinho..."
                        scene pnew_ani19 with Dissolve(1.0)
                        mc "H-haha..."

                        a "Tudo isso é antecipação? Você não tá tendo muita sorte com as garotas?"

                        mc "E-eu..."

                        a "Deu até vontade de enfiar você inteiro na boca agora!"

                        scene pri6_img21 with vpunch

                        pause

                        mc "A-ah!"

                        "E-eu quase gozei só com isso!"

                        a "Hmmm..."

                        "Incrível..."
                        scene pnew_ani17 with Dissolve(1.0)
                        a "Você... hmm... seu pau é gostoso..."

                        mc "[a]... você que tá fazendo gostoso..."

                        a "Que bom que você tá gostando, querido..."

                        mc "Se você continuar assim..."

                        a "Hmg! Eu sei!"

                        window hide

                        pause

                        scene pri6_img22 with vpunch

                        pause

                        mc "[a]!"

                        a "Isso, bebê! Goza pra mamãe!"

                        mc "Eu tô quase! Não para!"

                        a "Dá tudo pra mim! Toda sua porra!"

                        mc "Isso! Fala!"

                        a "Assim! Me dá! Joga na minha boca!"

                        mc "A-assim! Me mama!"

                        a "Hmmm!"

                        scene pri6_img22 with vpunch

                        mc "Aaahhh!!"

                        a "Ah! Gostoso..."

                        mc "{i}puf puf{/i}"

                        a "Deixa eu limpar isso aqui..."

                        a "A gente não tem muito tempo. Espero que tenha sido o suficiente."

                        mc "F-foi sim... mais que suficiente... Eu sou seu agora. Quer dizer, tô do seu lado."

                        a "Excelente..."

                a "Se você continuar do nosso lado, outros momentos como este aqui podem acontecer. Não esquece, tá?"

                mc "N-não vou..."
            "Chega disso. Eu vou pensar.":


                mc "Eu não quero nada de você agora. Eu vou pensar direitinho."

                a "Se você prefere assim, eu agradeço se você puder escolher meu lado."

        a "Vamos conversar mais no futuro. Agora vai."

        a "Até outro dia, [mc]."

        mc "Até."

        scene black with dissolve

        "Deixa eu me arrumar..."

        scene mc_aviao_voltando with Dissolve(1.0)

        "..."

        "Minha cabeça não para de pensar! Que bosta!"



        "Desde aquele dia na praia, quando o [gus] apareceu com o [mar], eu sabia que tinha caroço nesse angu."

        "Mas nunca imaginei o tamanho do buraco que eu tava me metendo."

        "Agora a [a] quer que eu não fale com a [c]. Como eu vou fazer isso?"

        "Tudo começou quando o chefe me mandou pegar pautas pra revista e eu fui me envolvendo cada vez mais com a [c]."

        if priscila_namoro:

            "Agora a gente tá namorando, mas ela continua lá, sozinha, com o velho..."
        else:


            "Ela disse que eu era o melhor amigo dela, mas eu deixa ela sozinha com o nojento..."

        "QUE RAIVA!"

        "Eu não posso fazer nada, DE NOVO!"

        "Agora eu tenho que voltar pra minha vida normal sabendo de tudo isso?"

        "Não. Eu preciso de mais. Eu preciso conhecer mais pessoas, eu preciso aumentar minha influência na revista."

        "Eu posso fazer alguma coisa, sim. Não agora. Mas eu sou um jornalista e eu posso colocar esse velho na cadeia de uma forma que ninguém mais pode."

        "Eu vou acabar com ele. Eu só preciso me esforçar mais."

        "Existem mais celebridades, mais gente importante que pode me ajudar. Eu preciso encontrar essas pessoas e acabar com o [gus]."

        "Eu posso fazer isso!"

        "Eu acho..."



    $ v23_fim = True
    $ tempo = 3

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v23_fim","priscila","personagem")

    scene black with Dissolve(3.0)

    jump call_cidade



label priscila_evento7:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p7_save", extra_info="p7_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ priscila_e7 = "evento"

    scene black with Dissolve(1.0)

    "{i}{cps=1}zZzzZzZz{/cps}{/i}"

    mc "Uaaahhh..."

    scene ape_cama with Dissolve(1.0)

    "Caraca... que sonho estranho... eu sonhei que a [c] tava em uma praça escura e eu chegava pra falar com ela, mas alguém atacava a gente."

    "Mas o que a gente faria em uma praça escura sozinhos? E nem parecia na ilha."

    "Eu devo tá preocupado com alguma coisa..."

    "Aquela ligação da Pri..."

    if p6_denuncia:

        "Será que eu fiz o certo falando pra ela a verdade sobre o que aconteceu lá no set?"

        "Ela é uma garota sensível, tenho medo que isso acabe deixando ela preocupada."

        "Mas eu tinha que falar a verdade. Não dava pra deixar ela fora dessa."
    else:


        "Eu preferi não falar pra ela sobre a verdade aquele dia no set de gravação."

        "Como ela é sensível, não queria deixar ela preocupada."

        "Mas mesmo assim eu tenho que pensar direito o que isso significa pra mim."

    "A verdade é que eu tô cansado de deixar as coisas desse jeito."

    "Esse povo do [gus] é perigoso. Aquele merda do [mar] também. O que ele tem contra mim?"

    "Tipo, o [mar] nem parece ter algum problema comigo. Eu sinto que ele só tá seguindo as ordens do [gus] filho da puta."

    "Só que esse velho cretino faz com a [c]... e fico pensando que deve ter feito com muitas outras."

    "Esse velho nojen-"

    "Acho que eu vou assistir alguma coisa. Mudar de clima."

    scene ape_tv with Dissolve(1.0)

    "Hmm..."

    "Vai começar o boletim da Faux News."

    "Vinheta" "{b}Faux News: Nós somos a Verdade{/b}"

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    scene tv apresentador with Dissolve(1.0)

    "Apresentador" "Bom dia. Agora são 9h15 e você está assistindo ao Boletim das 9 na Faux News."

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    "Apresentador" "Abrimos o noticiário com uma imagem que acaba de ganhar 300 mil curtidas nas redes sociais."

    "Apresentador" "O diretor [diretor] publicou em seu perfil pessoal uma foto com duas de suas protagonistas."

    scene gustav_priscila_agata with Dissolve(1.0)

    pause

    "Apresentador" "Os números mostram o nível de entusiasmo do público com o filme."

    "Apresentador" "Segundo analistas de métricas de redes sociais, nunca um filme gerou tamanha antecipação."

    "Apresentador" "O diretor escreveu na postagem que as gravações estão indo muito bem e devem acabar antes do planejado."

    "Apresentador" "'Estas duas são profissionais completas, e sabem como fazer seu trabalho, tanto em foco como fora das câmeras'"

    "Apresentador" "[diretor] tem uma carreira de muito prestígio e um filme desse tamanho vem apenas sacramentar o que o diretor conquistou."

    "Apresentador" "Entrevist-"

    "{i}Trrr trrr{/i}"

    scene ape_tv with Dissolve(1.0)

    mc "Hm?"

    "Número desconhecido."

    scene ape_celular_falando with Dissolve(1.0)

    mc "Alô?"

    "???" "{i}Está assistindo a Faux News agora? A [c] fica linda nessa roupa, não acha?{/i}"

    "???" "{i}Eu sei que você fugiu graças à [a]. Ela me contou.{/i}"

    "???" "{i}Mas saiba que a [c] continua aqui comigo. A gente se vê todos os dias.{/i}"

    "Não acredito! É a porra do [gus]!"

    "A voz tá distorcida, mas claro que é ele!"

    menu:
        "Continuar ouvindo":


            "???" "{i}Acho bom você se afastar da vida dela antes que você acabe perdendo a sua.{/i}"

            "???" "{i}Se você voltar aqui, eu vou acabar com você. E dessa vez você não vai ter ajuda de ninguém.{/i}"

            mc "Ei!"

            "???" "{i}...{/i}"

            mc "Você ainda vai pagar pelo que tá fazendo!"

            "???" "{i}...{/i}"

            mc "Me escuta seu velho escroto de uma merda. Você não passa de lixo!"

            "???" "{i}Você é um nada. Um zé ninguém. Você pode falar o que quiser, mas quem vê a [c] sou eu.{/i}"

            "???" "{i}Sou eu quem adiciona algo na vida dela. Que pode fazer ela ser alguma coisa. Você não traz pra ela, só suga.{/i}"

            "???" "{i}Chore à vontade, criança. Você não passa de um párea. Ninguém sabe de você ou se preocupa com você. Você é nada.{/i}"

            mc "Você que n-"

            "{i}Tu tu tu{/i}"

            mc "Velho filho de uma..."

            mc "Então ele sabe de tudo."

            "Eu tive sorte de ter dado o fora aquele dia. A [a] realmente me ajudou."
        "Desligar a chamada":


            "Desgraçado. Vai falar com seus idiotas. Que raiva desse velho, mano!"

            "Eu não quero nada com ele."

    scene ape_celular with Dissolve(1.0)

    "Então ele continua vendo a Pri..."

    if priscila_namoro:

        "Mesmo com a gente namorando... ela continua... mas eu sei que ela não quer. Aquele dia na praia ela chorou, quase gorfou pensando nisso."
    else:


        "Eu sei que a gente é só amigos, mas não dá pra achar que tá tudo bem isso. Aquele dia na praia ela chorou, quase gorfou pensando nisso."

    "Ela não tá de boa com essa situação. Mas então... por que ela continua? Será que... será que ela não consegue parar com isso sozinha?"

    "A [a] sabe o que tá acontecendo. Por que ela deixa isso acontecer?"

    "Eu lembro daquele email que eu li lá no nosso primeiro encontro no bar."

    show pub booth with dissolve

    show mc celular with dissolve

    "Sem tela de bloqueio? Que descuidada."

    "..."

    "E-mails talvez?"

    "'Parabéns! A negociação foi um sucesso!'"

    "'Olá, querida. A negociação foi um sucesso. Nossa viagem para a capital foi providencial para fecharmos o contrato.'"

    "'Você foi maravilhosa como sempre. E me desculpe por aquele negócio lá. Tivemos que aceitar, senão ele fecharia com outra.'"

    "'Não fique chateada por causa disso. Isso é normal, ok? Você vai ficar bem.'"

    "'PS.: Quem vai ser a nova estrela de cinema nacional?'"

    if casa:

        scene ap mc_cozinhando1 with Dissolve(1.0)
    else:


        scene mc ap_pensando with Dissolve(1.0)

    "Claro que esse email foi da [a] pra ela. Engraçado que ela mandou um email... mesmo elas sendo tão próximas."

    "Outra coisa é que a [c] quase nem fala dela. Será que elas são tão amigas assim?"

    "Será que a [a] é tão fria desse jeito? Tudo o que ela quer é ver a [c] mais famosa, mesmo que isso custe a integridade dela?"

    "E se... ela estiver certa e eu que tô errado?"

    "E se o melhor pra vida da [c] realmente for superar isso e depois curtir uma vida muito melhor? Será que eu tô sendo mesquinho?"

    menu:
        "Eu tô certo. Vender a [c] desse jeito é errado.":


            mc "Não é possível. É claro que eu tô certo. Existe um limite pras coisas. O trabalho é importante, claro que é, mas fazer qualquer coisa não dá."

            "Se eu achar que ela tá certa, então o que sobrou dentro de mim? Eu vou ter perdido minha ética, minhas máximas."

            "Claro que é mais difícil viver com valores, mas é isso que significa ser um grande homem ou uma grande mulher."

            "O [gus] pode ter dinheiro, influência, fama. Mas ele perdeu algo mais importante, que são as convicções dele..."

            "Tem que ser assim... Tem que ser..."
        "Talvez a [a] esteja certa... o que vale é o resultado.":


            "Talvez... será que sou eu que tô errado? Pensando agora... e se a situação da [c] é algo pequeno pelo que ela tá ganhando em troca?"

            "Ser a principal atriz da maior produção cinematográfica do país? Isso deve ser uma coisa que vai mudar a vida dela pra sempre."

            "E tudo o que ela tem que fazer é aguentar o velho por um tempo. Se você pensar... não é tão ruim assim."

            "Não... mas será? Impossível..."

    if casa:

        scene ap mc_cozinhando2 with Dissolve(1.0)

    "Merda... no fundo, o que eu acho não importa. O que importa é o que a [c] acha. Ela que tá passando por isso."

    "E toda vez que ela falou comigo sobre isso, ela não parecia tá gostando nada disso."

    "É nisso que eu tenho que focar. Quem sou eu pra julgar a situação dela?"

    if priscila_namoro:

        "Eu sei, a gente tá namorando. Mas eu posso só deixar ela se eu não concordar."

    "Tudo isso na verdade tem a ver com ela e não comigo. Eu preciso focar nela, no que ela tá sentindo."

    "E ela já deixou claro que não tá gostando disso. Na praia, lá no set de filmagem aquela vez..."

    "Eu preciso focar nisso e fazer alguma coisa. Não dá pra só ficar esperando ela ser abusada."

    "Eu tenho minhas armas também... eu sou um jornalista. Eu tenho a revista. Talvez seja hora de eu usar meu poder de paparazzo pra algo realmente importante."

    "Tá na hora de colocar a boca no mundo e falar que o [gus] é um cretino!"

    "Eu vou pensar um pouco... e na hora certa eu vou {b}falar com o chefe e entrego a pauta pra ele{/b}."

    "Pensa bem, [mc]... Pensa bem..."

    "..."

    "Certo... eu tenho que pelo menos {b}ir na redação e falar da pauta para o chefe para continuar{/b}."

    $ priscila_p3 = True
    $ pautas += 1

    jump call_cidade

label priscila_evento7_parte2:

    mc desculpa "Eu tenho uma pauta muito complicada... é assunto bem sério envolvendo uma celebridade famosa, senhor."

    b "Fala logo, moleque!"

    mc "Bom... o diretor de cinema [diretor], que tá fazendo o filme de maior budget da história do país, abusa da atriz protagonista, a [cc]."

    b "..."

    mc "..."

    b "..."

    mc "Senhor?"

    show chefe surpreso with vpunch

    b "COMO É?!"

    mc "O senhor me ouviu?"

    b "Claro que eu ouvi, fedelho. Espera... deixa eu sentar..."

    scene chefe_sentado_close with Dissolve(1.0)

    b "Cristo..."

    mc desconfiado "Tudo bem, chefe?"

    b "Calma... deixa eu pegar um ar."

    b "..."

    b "Você sabe o que isso que você disse quer dizer?"

    mc bravo "Claro. Mas é a verdade, senhor. Eu não mentiria algo assim."

    b "Eu preciso de provas. Onde estão as provas?"

    if marco_gustav:

        mc serio "Eu gravei uma conversa do [gus] falando com o segurança dele, um tal de [mar]."

        mc "Gravei pelo celular mesmo, e tava meio longe, mas ainda dá pra ouvir."

        mc "O [mar] inclusive cita nomes de pessoas que o [gus] teria feito a mesma coisa."

        b "Deus..."

        b "Garoto, isso é pouco."

        mc "Eu sei... a gravação não ficou legal, mas eu pensei que poderia ser algo."

        b "Ajuda... mas é pouco."
    else:


        mc desculpa "Infelizmente eu não tenho nenhuma gravação ou documento, mas eu tenho a palavra dela."

        b "Só?"

    b "Se você conseguir fazer a [c] falar e outras garotas que passaram por isso também, porque se é verdade, provavelmente devem ter outras."

    b "O testemunho de duas fontes, mas sem anonimato, dando a cara e falando. Isso é suficiente pra mim."

    mc desculpa "Duas?"

    b "Só a [cc], como vítima, vai parecer fraco demais. Precisamos de material pesado pra isso aqui."

    b "Veja [mc]..."

    scene chefe_sentado_pensando with Dissolve(1.0)

    b "Esse [diretor] não é qualquer merda. Ele está acima das merdas dessa merda de indústria. A gente sabe que tudo é uma merda mesmo, mas não é fácil."

    b "Tem muita sujeira nesse lixão, mas esse lixão gera muito dinheiro. Cinema, televisão, streaming, música, games, tudo isso gera dinheiro pra CARALHO."

    b "Foder um diretor igual esse, é declarar guerra contra gente grande. Eles vão vir pra cima da revista. E eu tenho meus interesses aqui."

    b "Inclusive meus interesses são seus interesses também, porque sem revista tu morre de fome, entendeu?!"

    mc zerado "Sim... Eu sei."

    b "Então presta atenção no que você tá fazendo. Pensa mesmo se você quer correr com isso aqui. Pensa direitinho e depois me traz depoimentos ou provas."

    b "Me traz alguma coisa concreta que faça a gente vencer uma causa contra esse povo que vai cair matando. Ou esquece isso e não me fala mais nada."

    b "Quanto menos eu souber, melhor pra mim."

    mc serio "Eu vou pensar, chefe."

    scene chefe_sentado_bravo with Dissolve(1.0)

    b "Deus não te deu essa cabeça só pra carregar chifre. Usa ela, [mc]! Usa! E agora tchau!"

    mc zerado "Ok..."

    scene black with Dissolve(1.0)

    scene trabalho mc_ouvindo with Dissolve(1.0)

    mc "Hmmm..."

    "Parece que o chefe não quer muito publicar a pauta. Mas foi o que eu decidi. Eu quero ajudar a [c]."

    "Mas ele disse uma coisa séria. Que com certeza muita gente se benificia do dinheiro do [gus]."

    "Se eu for atrás dele, os poderosos vão se ferrar, só que também atores, produtores, milhares de pessoas vão sofrer de algum jeito."

    "E com certeza eles vão vir atrás da revista e de mim. Eu posso perder meu emprego... ou até coisa pior."

    "Não seria a primeira vez que eu quase iria pra vala por causa disso. Aquela vez no viaduto... depois no set..."

    "Será que eu tô pronto pra tudo isso?"

    scene trabalho chefe_porta with Dissolve(1.0)

    "Deixa eu tomar alguma coisa."

    j "Ei! Pombinho!"

    mc zerado "Essa voz..."

    scene trabalho cassia with Dissolve(1.0)

    mc zerado "Que foi, [j]?"

    j "Qual a razão da sua conversinha com o chefe?"

    "Hmm..."

    menu:
        "Contar pra ela sobre a conversa":


            $ p7_cassia = True

            mc serio "Eu contei pra ele que eu tenho um podre de uma celebridade aí."

            j "Sei... e o velho ficou louco? Dava pra escutar ele gritando."

            mc envergonhado "Tipo isso..."

            j "Eu não tenho nada com você, mas eu tenho uma dica e é bom você prestar atenção."

            mc "Ok..."

            j "Existem dois tipos de pessoas nesta cidade. Os que importam e os que não importam."

            j "Se você quer ter algum sucesso aqui, acho bom você ficar do lado dos que importam."

            mc concentrando "Não sei se eu entendi o que você quer dizer..."

            j "Mexer com as pessoas erradas pode dar ruim pra você, [mc]. Nunca se esqueça disso."

            mc "Ok..."
        "Desviar o assunto":


            mc desconfiado "Você nunca quis saber das minhas conversas com o chefe."

            j "Mas agora eu quis."

            mc "Por que?"

            j "Não quer falar, não fale. Eu não preciso de você pra saber o que acontece naquela sala."

            mc zerado "Vai ficar de conversinha com o chefe?"

            j "Eu odeio aquele velho careca. Se acha o pica das galáxias, mas não passa de um velho que perdeu o tempo."

            mc desconfiado "Não sabia que você não curtia ele desse jeito."

            j "Por que é um idiota."

            mc zerado "Mas não foi ele que te deu todas essa liberdade na redação?"

            j "Não. O que eu tenho aqui eu conquistei com meu trabalho."

            j "Apenas as pessoas que têm algo para dar, podem dar algo, [mc]. E o chefe não é uma delas."

            mc concentrando "Bom... pense como quiser."

    j "Agora pode dar o fora. Pense direitinho no que eu falei."

    mc zerado "Grossa."

    j "..."

    scene trabalho mesa with Dissolve(1.0)

    "A [j] parecia interessada demais em mim dessa vez. Difícil ela me chamar pra conversar aqui."

    "E aquelas 'dicas' dela..."

    "Eu não caio mais na conversinha da [j]. Já ficou mais que provado que essa mulher só pensa nela."

    "Capaz dela ainda tá envolvida em tudo isso de algum jeito. Imagina prender a [j] junto do [gus]?"

    "Será que é demais pra um sonho só?"

    if sofia_e1 != "nada":

        w "[mc]! O que você tá fazendo parado aí?!"

        w "Tem uma matéria pra você checar aqui!"

        mc "Droga..."

        w "Parece que tem alguma coisa a ver com aquele polvo estranho no meio da praça!"

        mc "Buaaaa...."
    else:


        "Acho que hoje vou tirar o dia de folga e descansar."

        "Esse é o lado bom de ser paparazzo."

    scene black with Dissolve(1.0)

    $ dia += 1
    $ tempo = 1

    "{b}Um dia depois{/b}"

    show ape_cama with dissolve

    hide ape_cama with dissolve

    "{i}Trrrr... trrr...{/i}"

    show ape_cama with dissolve

    hide ape_cama with dissolve

    "{i}Trrrr... trrr...{/i}"

    mc "Hm?"

    scene ape_cama with Dissolve(1.0)

    mc "O celular..."

    "Nem sei se eu devo atender isso... E se for o idiota de novo só querendo me atazanar?"

    menu:
        "Atender o telefone":


            "Foda-se. Vou atender."
        "Ignorar a chamada e voltar a dormir":


            "Bah! Vou dormir que eu ganho mais."

            show black with dissolve

            "..."

            "{i}Trrrr... trrr...{/i}"

            hide black with dissolve

            show black with dissolve

            "Hm?"

            "{i}Trrrr... trrr...{/i}"

            hide black with dissolve

            "De novo?"

    "Espera... tem número a ligação. O DDD não é da capital. Que estranho."

    scene ape_celular_falando with Dissolve(1.0)

    mc "Quem fala?"

    a "Bom dia, [mc]. É a [a], agente da [c]."

    mc "[a]! Caraca... que hora pra você me ligar."

    a "Sério? O que aconteceu?"

    mc "É que eu tava pensando numas coisas aqui ontem... mas depois você vai acabar sabendo."

    a "Entendi..."

    mc "Aliás, valeu pela sua ajuda lá no set aquele dia. Se não fosse você, não sei o que ia acontecer comigo naquela sala."

    a "... Não precisa agradecer, [mc]."

    if marco_gustav:

        mc "Como não? Eu tinha escutado o [mar] e o [gus] conversando sobre me 'passar'. Esse é um jeito diferente de falar 'matar', [a]."
    else:


        mc "O [mar] já tinha me dado uma voadora e vai saber o que ele tava pensando em fazer ainda..."

    a "Eu sei, [mc]... de vez em quando as coisas podem sair um pouco do controle nesse mundo."

    mc "Sair um pouco do controle? É isso que você diz?"

    a "..."

    a "Olha... será que a gente pode se encontrar?"

    mc "A gente?"

    a "É... preciso falar um negócio sério com você."

    "Algo sério? O que será que ela quer?"

    menu:
        "Você tá armando uma armadilha pra mim?":


            mc "Como assim? Você tá armando pra cima de mim, [a]?"

            a "N-não é nada disso, [mc]. É que quero tratar de um assunto sério e pelo telefone é problemático."

            mc "..."

            a "Vai ser em um lugar aberto, pode ser agora de dia mesmo se você se sente melhor."

            mc "..."

            a "Eu sei que você tá um pouco assustado com tudo, mas eu tô do seu lado. Pode confiar em mim."

            "Tipo... ela me ajudou lá no set. Isso é óbvio. Ela não quer que eu morra... acho que isso dá pra concluir."

            "Mas será que eu realmente posso confiar nela? A [a] é uma das pessoas que colocou a [c] nessa situação."

            "E agora?"

            menu:
                "Não posso falar com você agora.":


                    mc "Eu tô ligado que você não tá contra mim, [a]. Só que agora eu tô em um momento muito crítico. Não dá pra falar com você."

                    a "Por favor, [mc]. É rápido."

                    mc "Desculpa, mas não."

                    a "... Ok..."

                    a "Se é assim que você prefere... então deixa eu te falar uma coisa."

                    a "Eu tenho um recado pra você. Pra você vir na Pizzaria Alighieri hoje meio dia."

                    mc "Pizzaria? Uma famosa que tem no centro?"

                    a "Essa mesmo. Se você puder pelo menos fazer isso por mim, eu agradeceria muito."

                    mc "O que eu faço chegando lá?"

                    a "Não se preocupe que vão te reconhecer na entrada e vão te chamar. Fique tranquilo."

                    mc "Ok... Vou pensar..."

                    a "Faça isso por favor. Eu te peço."

                    a "Bom dia."

                    mc "Até, [a]."

                    "..."

                    menu:
                        "Ir até a pizzaria":


                            "Se ela acha isso tão importante, acho que vale a pena dar uma passada lá."

                            "O que será que vai rolar lá?"

                            "Deixa eu ir pro continente."

                            scene black with Dissolve(1.0)

                            call locomocao from _call_locomocao

                            scene cidade centro1 with Dissolve(1.0)

                            "Daqui dá pra ir andando."

                            "..."

                            scene cidade centro4 with Dissolve(1.0)

                            "Aqui é perto da Cidade Chinesa. É a região mais antiga da cidade."

                            "Agora é só andar mais um pouco."

                            "..."

                            scene cidade pizzaria with Dissolve(1.0)

                            "Ufa. Deve ser aqui."

                            "..."

                            jump priscila_e7_tony
                        "Recusar o convite e ficar em casa":


                            "Não faz sentido eu conversar com mais ninguém nesse ponto."

                            "Eu já sei o que eu quero fazer."

                            jump priscila_e7_continua
                "Certo. Onde você quer conversar?":


                    mc "Tudo bem. Eu vou conversar com você."
        "Ok. Onde você quer se encontrar?":


            mc "Ok. Tá certo. A gente pode se falar."

    $ p7_miranda = True

    a "Que bom. Isso é muito importante."

    mc "Onde você quer se encontrar?"

    a "Você já ouviu falar da Pizzaria Alighieri?"

    mc "Uma famosa que tem no centro?"

    a "Isso, uma bem tradicional."

    if v26_fim:

        "Ah... eu fui com a [d] aquela vez."

    if v27_fim:

        "Eu e o [n] já se encontrou lá também. Mas a gente acabou nem comendo nada."

    mc "Tudo bem. Entendi."

    a "Então a gente se encontra lá em... uma hora mais ou menos?"

    mc "Tá. Dá tempo de tomar um banho e chegar lá."

    a "Obrigada, [mc]. Vou ficar te devendo uma."

    mc "Relaxa. Até mais."

    scene ape_chuveiro with Dissolve(1.0)

    "Que estranho. Por que a [a] quer tanto falar comigo? E bem agora?"

    "Será que ela tem um sexto sentido pra saber que tá acontecendo alguma coisa que envolve a [c]?"

    "Que viagem..."

    if praia_priscila_local:

        "Aquele dia que eu e a Pri curtirmos a praia ela contou um pouco sobre a história dela e da [a]."

        "Parece que elas são próximas desde muito cedo. A [a] sempre esteve presente e praticamente construiu a carreira dela."

        "Essa é uma ligação muito forte."
    else:


        "O que me deixa encucado é qual a relação das duas. A [c] parece confiar bastante na [a]. Elas devem se conhecer há um tempão."

        "E como ela é nova, se pá a [a] deve ser a primeira agente dela."

    if miranda_conversou:

        "O que a [a] falou com certeza aquela vez no bar é que ela vai fazer tudo pela [c]. Ela quer ver ela famosa."

        "Só que será que é isso que a própria [c] quer?"

    "E se a Pri tiver só indo na onda dessas pessoas e no fundo tá cansada disso?"

    "Bom... não adianta eu ficar pensando demais nisso agora. Tenho que falar com a [a] e daí ver o que ela vai dizer."

    "Deixa eu ir pro continente."

    scene black with Dissolve(1.0)

    call locomocao from _call_locomocao_1

    scene cidade centro1 with Dissolve(1.0)

    "Daqui dá pra ir andando."

    "..."

    scene cidade centro4 with Dissolve(1.0)

    "Aqui é perto da Cidade Chinesa. É a região mais antiga da cidade."

    "Agora é só andar mais um pouco."

    "..."

    scene cidade pizzaria with Dissolve(1.0)

    "Ufa. Deve ser aqui."

    a "[mc]!"

    mc normal "Ah. A [a] tá ali."

    "..."

    scene miranda_pizzaria1 with Dissolve(1.0)

    pause

    a "Oi, [mc]. Obrigada por vir."

    menu:
        "Parecia algo importante. Por isso eu vim.":


            mc "Parecia ser algo sério mesmo. Achei melhor ver o que você queria."

            a "Sim, é um assunto sério."
        "É um prazer ver você.":


            $ miranda_seducao += 1

            mc charmoso "Não precisa agradecer. É sempre um prazer ver você."

            if miranda_seducao >= 5:

                scene miranda_pizzaria_rindo with Dissolve(1.0)

                a "Ah... tinha esquecido que você tem esse jeito encantador."

                a "Eu lembro quando a gente conversou no bar, na primeira vez que a gente se viu."

                mc charmoso "Eu gostei muito de falar com você naquele dia."

                a "Eu também. Você tem um jeito especial, [mc]."

                scene miranda_pizzaria1 with Dissolve(1.0)
            else:


                a "Digo o mesmo."

            a "Mas hoje eu não quero falar da gente..."

    a "Eu preciso falar com você sobre a [c]."

    mc desconfiado "O que tem ela?"

    a "Eu vou precisar que você tenha um pouco de paciência, porque eu vou precisar contar pra você toda a história."

    mc "Tudo bem. Pode falar."

    a "Muita coisa aconteceu com a Priscila nesses últimos dois anos e meio. Muito mais do que acontece com 99%% das pessoas."

    a "Ela deixou a casa dela no interior, veio pra capital, ganhou dinheiro, fãs no país, foi pra fora..."

    a "A menina correu que nem louca. Ela nem tinha tempo pra dormir. Foto, vídeo, foto, vídeo, maquiagem, mais foto."

    menu:
        "Espera. E a [c]? Ela tava curtindo isso?":


            mc serio "Calma, [a]. Espera. E a [c]? Ela tava gostando dessa vida?"

            a "Como assim? Ela tava virando uma estrela. Claro que ela tava gostando."

            mc desculpa "Você, chegou a conversar com ela sobre isso?"

            a "... Que pergunta, [mc]... ela saiu do nada e virou uma famosa, cheia da grana, reconhecida em todo lugar."

            mc "..."

            a "Então. Por favor, continua ouvindo."
        "Continuar ouvindo":


            "Melhor eu só continuar ouvindo."

    mc "Certo. E daí?"

    scene miranda_pizzaria_falando with Dissolve(1.0)

    a "Sabe, [mc]... às vezes eu fico pensando se ela realmente sabia o que estava acontecendo. Eu trazia as coisas pra ela, ela só ria e fazia."

    a "Tão criança... o que ela sabia do mundo?"

    a "E mesmo assim, ela acreditou, ela passou por muita coisa e agora ela chegou no topo. Acima disso não dá pra ir. O mundo todo vai ver ela."

    a "O mundo todo vai ver a cara dela, vai ver ela interpretando, sabe? Ela chegou onde ela merece. Foi rápido, só que não foi fácil."

    mc desculpa "Por que você tá me falando isso?"

    a "Porque... porque a [c] precisa do [gus]."

    mc bravo "Como?!"

    a "Se alguma coisa acontecer com ele, o filme é cancelado e tudo o que ela passou foi por nada. Você entende isso?"

    mc "[a]... o que esse velho fez ela passar não pode ficar impune. Não quero nem pensar nisso."

    a "Eu sei, você tem razão, [mc]."

    mc "Então?! Por que você tá falando tudo isso?"

    a "O [gus] é um lixo. Ele não merece respirar o mesmo ar que a [c]. E com certeza ele vai pagar por tudo o que ele fez."

    mc "En-"

    a "Só que ele é a passagem da [c] pra chegar no topo. Pra ela chegar onde toda garota quis."

    a "O [gus] ainda vai ter o dele. Eu tenho certeza que isso ainda vai estourar. Mas não agora. Não enquanto a [c] ainda precisa dele de pé."

    mc desculpa "[a]..."

    a "Pensa. Ela mesma aceitou isso. Ela sabia o que ía acontecer. Mesmo assim ela quis ir adiante e fazer o filme."

    a "Eu não quero dizer que o [gus] tá certo. Deus me livre. Mas o que eu quero dizer é que a [c] sabia das dificuldades e aceitou."

    a "Se você causar alguma coisa com o [gus], você vai passar por cima do que ela queria. E vai jogar toda a luta dela no lixo."

    a "Isso não é egoísmo demais? Colocar o que você quer acima dela própria? A vida é dela!"

    mc "..."

    a "Você é um rapaz esperto."

    if priscila_namoro:

        a "Eu sei que vocês tão juntos. Ela me falou do namoro de vocês. E eu não sou contra."
    else:


        a "Você é o melhor amigo dela. Ela me disse. Tudo o que você falar e fazer é importante pra gente."

    a "Eu sei que você vai entender o que eu tô dizendo."

    "Será que eu entendo?"

    "O jeito que ela fala... parece que eu sou o culpado aqui. Eu que vou tá passando por cima da [c]..."

    "Se for realmente assim... o que eu faço?"

    mc desculpa "Não sei, [a]... tudo isso é muito estranho."

    a "Só pensa no que eu falei. E coloca a [c] em primeiro lugar."

    mc concentrando "Ok..."

    scene miranda_pizzaria_rindo with Dissolve(1.0)

    a "Você ainda é novo, [mc]. Tem muito o que viver, o que curtir, pessoas pra conhecer."

    if miranda_seducao >= 5:

        a "Nunca se sabe quando você vai conhecer uma pessoa especial que vai roubar seu coração."

        a "Eu sei que agora essa pessoa pode ser a [c]..."

        scene miranda_pizzaria_mc with Dissolve(2.0)

        pause

        a "Mas sentimentos mudam... nunca se sabe o dia de amanhã."

        mc "M-miranda?!"

        a "Eu sei que parece um pouco forçado, mas eu queria deixar claro que pode rolar alguma coisa entre a gente."

        a "Você é um rapaz sofisticado. E eu me considero uma mulher sofisticada e posso te dar uma coisa que nenhuma dessas garotinhas pode."

        if priscila_namoro:

            a "Claro que você vai ter que encerrar essa brincadeira que você tem com a [c] antes."

        mc "E-eu..."

        a "Pense bem, tá? O mundo tá cheio de oportunidades pra quem é esperto."

        mc "O-ok."



        "Oportunidades? Ela tá querendo me trazer pro lado dela. Certeza."

        "Eu e a [a] tamo nessa tensão sexual faz um tempo já."

        if miranda_aviao:

            "E depois do que rolou com a gente no avião lá nas gravações... eu sei que ela tá pronta pra fazer de tudo."

        "Se ela realmente quer contar comigo, eu posso fazer ela lutar um pouco por isso..."

        "Pedir pra ela um certo tipo de favor, sabe?"

        label pri7_miranda_premium:

            pass

        "M-merda! O que eu tô pensando?! Eu vou pedir uma coisa dessas pra ela mesmo?!"

        menu:
            "Eu tenho uma oportunidade pra você.":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_3

                    jump pri7_miranda_premium

                mc "Já que você falou sobre isso... EU tenho uma oportunidade pra você."

                a "A é? Eu adoro oportunidades... estou ouvindo."

                mc "Tem uma ruela aqui do lado... o que você acha de vir comigo?"

                a "Como é? Você tá falando sério?"

                if miranda_aviao:

                    mc "Tô. Lembra do avião? Eu gostei bastante do jeito que você me convenceu..."

                    a "Nossa senhora... que monstro que eu tô criando?"

                    mc "Você tá me deixando mimado... agora eu quero de novo..."
                else:


                    mc "Eu tô. Eu sei que você quer que eu dance a música, mas eu vou precisar de um incentivo..."

                    a "Eu tenho certeza do tipo de incentivo que o senhor tá querendo agora..."

                    mc "Exatamente..."

                mc "E aí?"

                a "Concordo. Mas a gente não tem muito tempo."

                scene black with dissolve

                scene pri7_img14 with Dissolve(1.0)

                pause

                a "É nesse tipo de lugar que você traz as mulheres que você quer se divertir?"

                mc "C-claro que não. Mas é o que tem pra hoje."

                a "Eu esperava mais de você, [mc]."

                mc "Ok... eu tô ansioso. Vem aqui."

                scene pri7_img15 with Dissolve(1.0)

                pause

                a "Ai... eu vou te falar... eu não achei que você fosse esse tipo de homem."

                mc "Pra falar a verdade, nem eu."

                a "Sua sinceridade é... um charme."

                mc "Acho que você que tá mexendo comigo."

                a "Será que esse negócio de vender seu apoio por prazer mexeu com você?"

                mc "Pode ser... agora tira isso."

                scene pri7_img16 with Dissolve(1.0)

                pause

                a "Ai. Você tá animado demais, [mc]."

                mc "É tudo culpa sua."

                a "Ainda não é o suficiente?"

                mc "Tá brincando?"

                if miranda_aviao:

                    mc "Você lembra como foi no avião?"

                    a "Você vai querer outro round?"
                else:


                    a "Sabe no avião? Eu tava pronta pra fazer uma coisa por você. Você quer receber agora?"

                mc "Com certeza."

                mc "Tira a roupa e ajoelha."

                a "Que mandão..."

                scene pri7_img17 with Dissolve(1.0)

                pause

                mc "Assim... sua boca é incrível."

                a "Hmm..."

                mc "Eu quero que você enfie ele inteiro na boca."

                a "C-asdaj... hm..."
                scene pnew_ani18 with Dissolve(1.0)
                mc "Não entendi nada. Só me chupa, [a]. Sua boca é demais!"

                "Tá muito bom isso aqui. Mas acho que eu quero mais."

                "Será que eu vou com tudo na garganta dela? Acho que é violento demais isso aí..."

                menu:
                    "Forçar na garganta dela":


                        "Eu não consigo me segurar! Eu quero chegar no limite!"

                        mc "Toma, sua puta!"

                        scene pri7_img18 with vpunch

                        pause

                        a "HHM! GHH!"

                        a "{i}GLUOF COF{/i}"

                        mc "Isso é muito bom!!"

                        a "HHMMM!"

                        mc "Para de se mexer e toma!"

                        a "{i}COF COF{/i}"

                        a "PARA! HM!"

                        "Parar? Agora?!"

                        menu:
                            "Jogar ela na parede":


                                mc "Se isso é demais, então vem aqui!"

                                a "A-ah!"

                                scene pri7_img19 with Dissolve(1.0)

                                pause

                                a "[mc]... o que você tá fazendo?"

                                mc "Se você não vai deixar eu usar sua garganta pra gozar, eu vou usar outra coisa."

                                a "Você... você tá violento demais..."

                                mc "Você que começou tudo isso com aquela história de oportunidades. Nem vem."

                                a "Eu... não pensei que você..."

                                mc "Você é tão linda, [a]... eu não consigo me segurar..."

                                a "Vai logo então... faz o que você precisa fazer."

                                mc "Aleluia!"

                                a "Mas eu não quero que você enfie em mim assim."

                                mc "M-mas!"

                                a "Sem proteção, não."

                                mc "Droga. Tá bom."

                                scene black with dissolve

                                scene pri7_img20 with Dissolve(1.0)

                                pause

                                mc "Mas você vai ter que deixar eu me esfregar até gozar."

                                a "Claro. Eu sou sua."

                                mc "Então fala assim que eu fico excitado!"

                                a "A-ah! Vai! Pode gozar!"

                                mc "HM!"

                                a "Eu sei que eu sou gostosa! Aproveita!"

                                mc "Eu vou! Vou gozar em você, [a]!"

                                a "Dá tudo pra mim!"

                                scene pri7_img20 with vpunch

                                mc "A-AAH!!"

                                a "ISSO!"

                                mc "{i}puf puf{/i}"

                                a "Satisfeito?"

                                mc "A-ah..."
                            "Melhor parar. Tá indo longe demais":


                                mc "D-desculpa..."

                                scene pri7_img17 with Dissolve(1.0)

                                a "Não precisava... hm... de tudo aquilo."

                                mc "Você tá certa... assim tá bom..."

                                a "Então... {i}shlup{/i}... goza pra mim, goza..."

                                mc "T-tá!"

                                a "Isso... você tá crescendo!"

                                mc "Continua assim, [a]! Eu tô vindo!"

                                a "H-hmmm... na min... boc..."

                                mc "C-claro! Vou gozar na sua boca, sua gostosa!"

                                scene pri7_img17 with vpunch

                                mc "Aaahh!!"

                                a "HMM!"
                    "Melhor parar por aqui":


                        "Eu vou conseguir gozar só fazendo assim. Eu não tenho que exagerar."

                        mc "Continua assim, [a]! Eu tô vindo!"

                        a "H-hmmm... na min... boc..."

                        mc "Acho que eu entendi! Vou gozar na sua boca, sua gostosa!"

                        scene pri7_img17 with vpunch

                        mc "Aaahh!!"

                        a "HMM!"

                scene black with dissolve

                scene pri7_img21 with Dissolve(1.0)

                pause

                a "Nossa... você... você me pegou de jeito. Tô impressionada."

                mc tarado "Eu não consegui me segurar. Desculpa qualquer coisa."

                a "Não adianta falar isso agora, safado..."

                mc envergonhado "..."

                "O que eu fiz com a Miranda aqui... querendo o corpo dela por uma coisa em troca..."

                "Tudo isso... Não é a mesma coisa que..."

                "O que aconteceu comigo?"

                a "Ei."

                jump pri7_miranda_premium_depois
            "Não vou falar nada":


                "Deixa quieto. Eu não sou esse tipo de pessoa. Que se aproveita da vulnerabilidade das outras."

                mc "Então é isso?"

    scene miranda_pizzaria_rindo with Dissolve(1.0)

    a "Não deixe que os outros tirem o que você tem de bom no coração. A alegria de viver e de ver sua vida dar certo."

    scene miranda_pizzaria_seria with Dissolve(1.0)

    label pri7_miranda_premium_depois:

        pass

    a "Agora... eu tenho uma última coisa pra te pedir."

    mc desconfiado "Hm?"

    a "Tem uma pessoa que quer falar com você."

    mc "Quem?"

    a "Essa pessoa tá aqui na pizzaria e ela vai te pedir pra reconsiderar algumas coisas que você vêm pensando."

    a "[mc]... me escuta... esse homem... ele tem uma energia diferente. Ele não é assim, igual você e eu."

    mc desconfiado "Ele não é igual a gente? Ele é tipo um alien?"

    a "Isso é sério, [mc]. Presta atenção. Esse homem, eu só falei com ele uma vez. Mas ele deixou uma impressão de outro mundo."

    a "Eu não sei explicar direito. Você vai ver quando falar com ele. Mas toma cuidado, tá?"

    mc preocupado "Tomar cuidado com o que?"

    a "Só presta atenção. Fica atento e faz o que ele falar."

    a "Agora vai lá. Já faz um tempo que a gente tá se falando. Ele já deve tá te esperando."

    mc serio "Certo. Aqui na pizzaria, né?"

    a "Isso."

    a "Boa sorte. E fica tranquilo que eu vou proteger a [c] e você também."

    mc concentrando "Até outro dia."

    a "..."

    scene black with dissolve

    scene cidade pizzaria with Dissolve(1.0)

    "..."

    "Não sei ainda se o que a [a] disse faz sentido. Preciso pensar nisso tudo com calma."

    "E agora essa... falar com esse homem que eu nem sei quem é."

    "Ainda por cima ela fala que é um cara perigoso. Por que eu falaria com ele?"

    "Só falta ela me colocar numa mesa com o [gus]. Eu não vou tolerar isso. Eu vou socar esse velho."

    if socou_gustav:

        "De novo... hihihi..."

        "Foi muito bom bater nesse velho daquela vez. Ser estourado e quase morrer não foi legal, mas valeu à pena. Ah, se valeu!"

    "Agora... será que eu realmente entro nessa pizzaria?"

    menu:
        "Entrar na pizzaria":


            "Não tenho porque me esconder. Não tenho medo de ninguém."

            mc preocupado "{i}gulp{/i}"
        "Voltar para casa":


            "Esse cara que fique me esperando. Não tô nem aí pra eles."

            "Passar risco à toa. Não sou idiota, não. Espera sentado aí, coitado."

            jump priscila_e7_continua

    label priscila_e7_tony:

        $ p7_tony = True

        "Vamo nessa e seja o que Deus quiser."

        scene black with Dissolve(1.0)

        "Será que é aqui mesmo?"

        "???" "Oi, [mc]."

        mc surpreso "!"

        scene chefao_pizzaria_marco_pe with Dissolve(1.0)

        pause

        mc "M-Ma-ma-marco?!"

        mar "Boa tarde."

        menu:
            "O que você tá fazendo aqui?!":


                mc bravo "[mar]?! O que você tá fazendo aqui?!"

                mar "Calma. Eu não pretendo te bater hoje."

                mc "Era só o que me faltava..."

                mar "[mc]... Eu nunca tive nada contra você. Você é um cara bacana, gente boa. Eu já acompanhei muito você por aí."
            "B-boa tarde...":


                mc bravo "Boa tarde... O que isso aqui quer dizer?"

                mar "Meu chefe te chamou pra uma conversa e ele me pediu pra participar."

                mc "Uma conversa?"

        mar "Eu sei que você não tem nenhum motivo pra gostar de mim. Mas saiba que você não tem porque se preocupar hoje."

        if marco_gustav:

            mc "Não é você que ia me 'passar'? Eu gravei sua conversa com o [gus] no set."

            mar "Eu sei. Eu sabia que você tava lá."

            mc irritado "Sabia?!"

            mar "Eu imaginei que você chegaria mais perto... a gravação não ficou tão boa, imagino."

            mc "..."

            mar "Eu não vou matar você."

            mc bravo "Por que eu acreditaria nisso?"

        mar "Eu não quero que você se ferre. Quer uma prova?"

        mar "Aquele dia no set, fui eu que chamei a [a]."

        mc surpreso "Você?!"

        mar "Agora... será que a gente pode conversar?"

        "Será que ele tá falando sério? Por que ele me salvaria?"

        "Não vou ficar perguntando tudo pra ele. Isso é algo que eu vou ter que entender sozinho."

        to "Obrigado, [mar], pela introdução. Ninguém aqui tem pressa. Sente-se, tome uma taça de vinho."

        "Esse cara..."

        if v26_fim:

            "Ele tava aqui àquela noite que eu vim comer pizza com a [d]..."

        if v29_fim:

            "O nome dele é [to]. Ele conversou com o Barão naquela noite."

            "Agora eu entendo o que a [a] quis dizer. Ele não tá brincando."

        mc serio "Com licença."

        to "Toda."

        scene chefao_pizzaria_marco_mc with Dissolve(2.0)

        pause

    to "Eu pedi para a [a] marcar este encontro, mas não vou usar muito do seu tempo."

    mc "..."

    to "Nós sabemos que você tem uma relação com a [cc]. Não me importa se vocês são namorados, amantes, amigos ou o que quer que seja."

    to "Ela confia muito em você. E isso, sem dúvidas, é uma coisa muito poderosa."

    menu:
        "...":


            mc serio "Prossiga..."
        "Poderosa?":


            mc "Poderosa? O que isso quer dizer?"

            scene chefao_pizzaria_close with Dissolve(1.0)

            to "Não é óbvio? Você tem um poder sobre ela que nem mesmo a [a] tem. E ela está aqui justamente por conta isto."

            mc desculpa "Isso não é meio... manipulação? Digo, olhar as coisas desse jeito?"

            to "Eu sou uma pessoa pragmática. Isso é algo que temos que deixar claro logo de pronto. Peço que deixe o certo e o errado do lado de fora."

            to "O que é 'certo', o que é 'ético', o que é 'moral'... isso não quer dizer nada pra mim. Minha verdade é minha família. Ponto."

            mc serio "Acho que eu entendo."

            scene chefao_pizzaria_marco_mc with Dissolve(1.0)

            to "Perfeito. Agora veja..."

    to "Nós investimos muito na senhorita [c]. Trazer uma garota do interior, desconhecida, e transformá-la nesse fenômeno não foi de graça."

    to "Garantir contratos, participações, assessores, profissionais da estética, da moda, coaching, psicólogos, treino e educação..."

    to "Para enumerar apenas alguns dos investimentos necessários. Agora, é hora de colher um alto retorno pelo meu investimento."

    to "Os especialistas chamam esse cálculo de ROI, ou Retorno Over Investment. E a [c] tem tudo para apresentar um grande ROI."

    to "Para ser sincero com você, eu não entendo muito dessa parte. Nós temos uma pessoa cuidando da parte monetária e investimento."

    menu:
        "Não sei se eu entendi o que você quer dizer":


            mc "Eu não sei se eu entendi exatamente. Como se a [c] estivesse devendo pra vocês alguma coisa?"

            scene chefao_pizzaria_close with Dissolve(1.0)

            to "Não é exatamente isso. Tem menos a ver com ela e mais com minhas próprias decisões."

            to "Se ela não der o resultado esperado, então terei apostado no cavalo errado, apenas isso."

            to "Para o cavalo, isso não importa muito, mas para quem apostou alto nele, isso significa muito."

            mc bravo "Não sei se sua comparação é boa..."

            to "Não vamos nos perder aqui. Não é isso que importa, ainda, pois meu cavalo ainda está correndo."

            mc "..."
        "Mas e o talento da própria [c]? Não conta?":


            mc "Mas e o talento da Pri? Você tá ignorando tudo o que ela trouxe pra mesa."

            scene chefao_pizzaria_close with Dissolve(1.0)

            to "O talento vale muito pouco nessa soma. Sem as pessoas certas trazendo o que ela precisava, o talento dela de nada servia."

            to "A [cc] não foi escolhida pelo seu rosto bonito e seu jeito carismático. O que não falta são garotas com esses atributos."

            mc desculpa "Mas então..."

            to "O que nos fez decidir por ela foi o fato dela ter sido vendida como uma garota que faria o que era necessário."

            to "Quando ela foi apresentada, nos prometeram que ela tinha tudo o que era preciso, inclusive a personalidade que queríamos."

            to "E isso tem se mostrado verdade."

    scene chefao_pizzaria_marco_mc with Dissolve(1.0)

    to "Sendo sincero, o mais difícil já foi feito. A estrela foi criada. Mas, não se engane, essa foi a parte fácil."

    to "A parte de maior apreensão foi fazer ela passar pelo [diretor]. O velho é uma fábrica de problemas."

    mc "É justamente esse o problema! Isso é ridículo!"

    to "Concordo plenamente com você. E aposto que o [mar] pensa o mesmo."

    scene chefao_pizzaria_marco with Dissolve(1.0)

    mar "Claro. Eu mesmo disse isso várias vezes pra ele. Mas ele não escuta. O velho é cabeça dura."

    to "Está vendo, [mc]? Nós não discordamos de você quanto ao [gus]. Ele já causou problemas para nós antes."

    to "Por isso mesmo eu tenho o [mar] na cola dele quase o tempo todo. O velho é uma bomba relógio."

    mc preocupado "Mas então por que?!"

    to "Mesmo com seus negativos, o [gus] é um dos diretores mais famosos do mundo. E ele aceitou colocar a [c] no papel."

    to "Dar protagonismo para uma garota que nunca atuou na vida, no filme de maior budget da história. Você entende o que é isso?"

    mc desculpa "..."

    to "Nós sabíamos que ele aceitaria, pelos motivos que você deve estar imaginando."

    to "A reação da senhorita [c], no entanto, era imprevisível. A [a] teria que manter ela no jogo. Fazia parte do acordo."

    "..."

    to "Mas tudo correu bem. Claro, não foi perfeito, mas foi melhor do que o esperado."

    mar "Mas daí você apareceu, [mc]."

    mc surpreso "Eu?!"

    to "Quando o [mar] foi buscar ela no bar na noite em que vocês se falaram pela primeira vez, não imaginamos que você teria tanto peso."

    to "Na verdade, só começamos a sondar você quando vimos a foto de vocês dois na praça."

    mc desconfiado "Foto?"

    to "Espero que não nos leve a mal por tudo isso. Nossa intenção nunca foi lhe causar mal. Estávamos apenas protegendo nossos recursos."

    menu:
        "Acho que eu já ouvi o bastante. O que você quer?":


            mc bravo "Eu tô achando que já ouvi o bastante sobre tudo isso."

            to "Entendo."
        "E aquela noite no viaduto?":


            mc bravo "Mas e a noite no viaduto? Esse idiota ia me matar ali de qualquer forma!"

            mar "[mc]... eu-"

            to "Espere, [mar]. Veja. Naquele ponto, eu fiz um julgamento errado. A culpa foi minha."

            to "Eu não quero me estender demais no assunto, mas eu assumo a responsabilidade."

            to "Naquele momento, eu ainda estava incerto quanto ao lado que você penderia..."

            to "E com as constantes reclamações do [gus]... eu achei melhor tirar você da equação se você continuasse tentando se aproximar demais dela."

            to "Veja, senhor [mc]. Eu não quero sangue nas minhas mãos. Eu não sou um assassino. Eu apenas resolvo problemas e emprego os recursos necessários para tal."

            mc "Inclusive assassinatos..."

            to "Sim, entre outras coisas."

            mc "Isso é um absurdo..."

    to "Você não precisa concordar com meu modus operandi, entretanto, eu acredito que nossos objetivos têm mais pontos de interseção que de colisão."

    mc serio "Certo. Agora o que interessa. O que eu tô fazendo aqui?"

    scene chefao_pizzaria_apontando with Dissolve(1.0)

    to "Serei franco com o senhor novamente. O que eu peço é que o senhor não envenene meu cavalo ou, muito menos, jogue meu investimento no lixo."

    mc "Mas o que eu posso fazer?"

    to "Se alguma coisa acontecer com o [diretor] ou se a [cc] desistir do nosso acerto, eu e meus amigos seremos os maiores perdedores."

    to "Entretanto, se você garantir que tudo aconteça como planejado, vocês poderão ficar juntos, como amigos ou namorados, como você preferir."

    to "A senhorita [c] terá uma carreira de ouro e este filme será apenas o começo. Temos outros planos para ela."

    mc "Então você quer que eu não faça nada quanto ao [gus]..."

    to "O [gus] pode ter seus problemas, mas ele é um excelente aliado por vários motivos. Eu gostaria que tudo só continuasse como está."

    to "Pense. A senhorita [c] já passou pelo pior. Ela está feliz ao seu lado. Desde aquele dia no lixão, ela está mais feliz graças a você."

    scene chefao_pizzaria_marco_mc with Dissolve(1.0)

    "Como ele sabe que eu quero fazer algo contra o [gus] justo agora?"

    menu:
        "Entendo...":


            mc "Entendi..."
        "E se eu quiser ferrar o [gus]?":


            mc "Consegui entender o que você quer. Mas e se eu quiser ferrar o [gus] mesmo assim?"

            to "Bem... eu espero que isso não aconteça, mas, caso você vá adiante com essa ideia, seria muito prejudicial para meus negócios."

            mc "Você teria que 'resolver o problema'?"

            to "Não pense algo assim de mim. Eu não puno pessoas. Eu resolvo problemas. Depois que o estrago foi feito, não há nada que eu possa fazer."

            mc "Você quer dizer que mesmo que eu publique algo sobre o [gus] e o filme seja cancelado, porque provavelmente é o que vai acontecer..."

            mc "Você tá falando que mesmo assim não vai ter nenhum tipo de retaliação contra mim?"

            to "De minha parte, não."

            mc "Vai ser o [mar]? É isso que você quer dizer?"

            scene chefao_pizzaria_marco with Dissolve(1.0)

            to "O [mar] obedece diretamente minhas ordens. Você não precisa se preocupar com nada desse tipo."

    to "Eu sei que você pode vir com uma cabeça do que viu em filmes, mas isso aqui não é O Poderoso Chefão, [mc]."

    to "Eu não estou fazendo uma proposta irrecusável para você. Nem ameaçando sua vida. Estou fazendo um pedido como cavalheiros."

    to "Caso o senhor aceite, sinto que uma parceria entre nós pode nascer. Se não, nada irá mudar."

    scene chefao_pizzaria_marco_mc with Dissolve(1.0)

    mc "Você me dá sua palavra que nada vai acontecer?"

    to "Você tem minha palavra. No entanto, se tudo só continuar como planejado, tanto eu quanto vocês acabaremos felizes com o resultado. O que me diz?"

    mc "Eu preciso responder agora?"

    to "Eu gostaria. Preciso avaliar quais serão meus próximos passos."

    "O que esse cara quer é que eu desista de publicar a matéria sobre o [gus] e deixe ele impune pelo que ele fez com a [c]."

    "Ele quer que eu esqueça tudo o que o [mar] me fez também e simplesmente aceite que as coisas são assim."

    "Em troca ele diz que eu vou poder viver feliz com a [c] e prometeu uma 'parceria'."

    "Por outro lado, se eu negar ele disse que nada de ruim vai acontecer comigo. Em outras palavras, que ele não vai me espancar até a morte."

    "Será que tudo o que esse cara tá me falando é verdade? Por que eu confiaria nele? E se ele simplesmente me matar?"

    "Aliás, por que ele não me mata agora? Resolveria o problema dele comigo de uma vez."

    "Mano, é coisa demais pra pensar de uma hora pra outra. Mas eu preciso dar uma resposta agora."

    "E essa {b}resposta pode mudar minha história na capital para sempre{/b}. O que eu faço?"

    "..."

    "Não consigo decidir!"

    to "[mc]..."

    mc "O-oi..."

    to "Vamos fazer o seguinte. Vá para casa e pense. Esqueça isso."

    mc "Hm?"

    scene chefao_pizzaria_close with Dissolve(1.0)

    to "Se eu quero que você acredite em mim quando digo que eu quero que você seja livre para escolher o que quer, não posso te pressionar dessa forma."

    to "Respire, beba algo em casa. Se for te ajudar, fale com a senhorita [c]. Seja lá o que o senhor acabar escolhendo, eu saberei."

    to "Eu sinto que ainda nos veremos outras vezes. De uma forma ou de outra, eu quero você como um aliado. Não se esqueça disso."

    mc "O-obrigado."

    scene chefao_pizzaria_marco_pe with Dissolve(1.0)

    to "Até mais e tenha um bom dia."

    mar "Até mais, [mc]. Vai com Deus."

    mc "V-valeu..."

    "Que merda tá acontecendo aqui?"

    "Melhor eu dar o fora antes que ele mude de ideia."

    scene cidade pizzaria with Dissolve(1.0)

    "..."

    $ tempo = 2

    scene black with dissolve

    if carro:

        scene carro_mc_cidade2 with Dissolve(1.0)
    else:


        scene mc onibus with Dissolve(1.0)

    "..."

    "Nem sei o que pensar..."

    "..."

    scene ape_geral with Dissolve(2.0)

    "..."

    "Eu devia imaginar que tinha algo por trás do [gus]. Todo esse dinheiro pro filme... Essas pessoas devem tá envolvidas até o rabo nisso."

    "Droga..."

    label priscila_e7_continua:



        if not p7_miranda:

            "Eu não preciso da [a] falando coisa no meu ouvido. Eu sei que ela é culpada também pelo que acontece com a [c]."

            "Quanto mais eu falo com ela, mais eu sei que ela é uma nojenta que deixou isso acontecer com a amiga dela."

            "E... pra falar a verdade... se ela acabar se ferrando junto do [gus], azar o dela."

            "O que eu sei é que o [gus] tá dirigindo o filme de maior budget da história do país. Isso não acontece do nada. Devem ter muitas pessoas envolvidas."



        if not p7_tony:

            "E não sei pra que esse encontro misterioso na pizzaria. Se alguém quiser falar comigo que me ligue. Parece que todo mundo tem meu telefone mesmo."

            "Eu não quero me envolver com mais ninguém nessa história."

    "Se eu publicar a matéria do [gus] eu vou mexer com gente grande. E com certeza vai sobrar pra mim."

    "Mas será que dá pra deixar o filha da puta escapar dessa assim? Tudo o que a [c] passou... ninguém vai saber disso? Eu vou me tornar cúmplice também?"

    "Se eu não fizer nada, mesmo sabendo o que tá rolando, é como se eu fizesse parte... Será que isso tá certo?"

    "Merda... e agora?"

    "{i}Trrr trrr{/i}"

    mc "Afe... bem agora?"

    scene ape_celular_falando with Dissolve(1.0)

    mc desculpa "Alô?"

    c "Oiee! Adivinha quem é!"

    if priscila_namoro:

        mc "A namorada mais linda do mundo?"
    else:


        mc "Oi, Pri!"

    c "Essa mesmo! Haha!"

    c "Acabei de chegar na ilha! Queria muito ver você. O que você acha?"

    mc "Agora?"

    c "Sim... Agora não dá?"

    mc "Claro que dá. Também quero ver você."

    c "Que bom!"

    "Com todas essas coisas que tão rolando, acho que não seria legal a gente se ver nem na ilha e nem no continente..."

    mc "E se a gente fosse em um lugar novo?"

    c "Uuuu! Adoro surpresa! Onde você vai me levar?"

    c "Ah! Tem um parque seguindo a ponte, depois da praia. O que você acha da gente se encontrar lá?"

    mc "Hmm... ok. Acho que eu sei onde é."

    c "A [m] me falou que bastante gente faz caminhada lá."

    mc "Legal."

    c "Você me dá uma horinha? Eu vou me preparar."

    mc "Não precisa se preocupar tanto com isso, tá?"

    c "Claro que eu preciso, idiota! Beijo!"

    scene ape_celular with Dissolve(1.0)

    "..."

    "Eu tinha até esquecido que ela tava voltando das gravações. Bem que a filmagem podia acabar de vez logo."

    "Talvez falar com a Pri me ajude a resolver o que fazer."

    if priscila_namoro:

        "A gente já tá namorando um tempo, mas eu nem consigo sentir isso direito. A gente quase nem passa tempo juntos."
    else:


        "Eu sei que eu sou só um amigo, mas não consigo só deixar isso de lado e fingir que nada aconteceu."

    "Deixa eu tomar outro banho."

    scene ape_chuveiro with Dissolve(1.0)

    "Quando eu lembro o que o [gus] disse aquela vez no camarim... mano... eu fiquei muito puto. Aquilo mexeu comigo."

    "E eu ainda tava no banheiro... que situação ridícula!"

    "Só de pensar o que esse velho cretino fez com ela... eu tenho vontade de socar alguma coisa... até sangrar."

    "Afe, mano!"

    "Respira..."

    "Melhor eu sair tomar um ar e já ir encontrar ela. Não vou deixar ela esperando lá naquele lugar sozinha à noite."

    scene black with Dissolve(1.0)

    "..."

    "Maluco... o que a [c] tava na cabeça quando marcou neste lugar aqui... é longe pra caramba."

    "..."

    $ tempo = 3

    scene track noite with Dissolve(2.0)

    pause

    "Ufa... acho que é aqui."

    if maria_evento >= 3:

        "Esse lugar é onde eu e a [ma] vem pra treinar."

        "Parece tão diferente de noite..."

    "Por que ela quis marcar bem aqui? Não tem luz... não tem ninguém..."

    "Eu também não tô vendo ela..."

    "..."

    "Caralho, tô ficando com mó medão agora. Não faz sentido uma mina marcar um encontro num lugar perigoso igual esse aqui."

    "Será que... esse lugar não foi ideia da [c]?"

    "E se alguém quisesse eu aqui nesse lugar deserto sozinho de noite e só mandou a [c] falar?"

    "Isso aqui não tá certo, mano."

    show black with dissolve

    hide black with dissolve

    mc angustiado "?!"

    "A luz deu uma piscada? Ficou tudo escuro do nada."

    "Merda..."

    menu:
        "Acho que vou ligar pra [c].":


            mc preocupado "Acho que vou ligar pra ela."

            "..."

            mc desconfiado "Hm?"

            "{i}{size=15}Talalá tololó{/size}{/i}"

            "Parece que eu tô escutando alguma coisa tocando. Por aqui..."
        "Melhor eu sair daqui rápido e depois eu ligo pra ela da ilha.":


            mc desculpa "Melhor eu sair daqui. Depois eu ligo pra ela."

            "Bora sair desse inferno."

            scene black with dissolve

            "..."

            mc surpreso "!"

    scene pri7_img1 with Dissolve(2.0)

    pause

    mc normal "Pri!"

    c "Hm? [mc]?"

    mc normal "Tô aqui, boba."

    c "Ufa!"

    scene pri7_img2 with Dissolve(2.0)

    pause

    c "Que bom que você me achou..."

    mc normal "Haha."

    c "Desculpa ter chamado você aqui essa hora."

    menu:
        "Por que você escolheu aqui?":


            mc desconfiado "Por que você escolheu esse parque aqui?"

            c "Não sei... acho que eu sou louca."

            mc envergonhado "Haha..."

            c "Falando sério, eu queria ir em um lugar novo. Tava cansada da ilha, do continente..."

            mc "Daí você quis ir no meio do caminho..."

            c "Isso hehe... desculpa."

            mc normal "Eu gostei. Não esquenta."
        "Relaxa. É um lugar bacana.":


            mc charmoso "Relaxa. O lugar é bacana, é bonito e romântico até."

            c "É! Também tô achando... primeiro achei que era um cenário de filme de terror, mas agora que você chegou, ficou mais romântico."

    if premium:

        menu:
            "Dar uma conferida nela":


                "Olha pra essa roupa... a Pri tá muito gata. Eu preciso dar aquela conferida."

                if priscila_namoro:

                    "E agora que a gente tá namorando não é mais esquisito, certo?"

                show pri7_img4 with Dissolve(1.0)

                pause

                "Uou..."

                c "Que que você tá olhando, hein?"

                mc safado "Só tô conferindo seu... visual."

                c "E aí? O que você achou?"

                pause



                hide pri7_img4 with Dissolve(1.0)
            "Melhor não arriscar":


                "Deixa quieto. Vou só elogiar."

    mc charmoso "Você tá linda."

    c "Eu disse que tinha que me aprontar, né?"

    mc "Você tá sempre linda."

    c "Eu tinha a impressão que você sempre me via com a mesma roupa."

    mc normal "Aquela que é da sua própria linha, né?"

    c "Sim. Eu uso bastante ela... mas enjoou um pouco. E tá meio frio também."

    if priscila_namoro:

        mc charmoso "Bom... eu já aceitei que eu namoro a garota mais linda, gostosa e estilosa do mundo."

        c "E dá pra ver bastante com essa roupa... é pra você aproveitar mesmo."

        mc safado "Pode deixar. Vou aproveitar bastante."

    mc "Ah. E as gravações... tão acabando?"







    c "Então..."

    c "Eu tipo nem cheguei na ilha a [a] já veio falar comigo. Ela parecia meio ansiosa. Você sabe se aconteceu alguma coisa?"

    if p6_denuncia:

        c "Isso tem a ver com o que você me contou no telefone? Sobre o [mar] ter ido pra cima de você?"

        mc desculpa "Não sei... mas pode ser."

        c "Eu ainda não tô acreditando naquilo, [mc]. Essas pessoas... elas tão todas erradas."

        mc normal "Eu falei pra você não pensar demais nisso. Já passou."

        c "Mesmo assim... isso só me faz ficar pensando mais nisso ainda."
    else:


        c "Ela não me disse nada, só que deu pra sentir que ela tava preocupada com alguma coisa."

        "A [a] então tá nervosa..."

        c "Quanto mais o tempo passa, mais eu fico pensando nisso tudo."

    c "Onde eu fui me meter?"

    "Acho que agora é a hora de puxar o assunto."

    mc desculpa "Sobre isso, Pri... você acha que a gente pode conversar um pouquinho sobre isso?"

    c "Hm?"

    mc "Eu sei que esse é um assunto complicado e que te deixa triste, mas eu tinha que te perguntar algumas coisas."

    c "Vamos sentar?"

    mc surpreso "C-claro!"

    scene pri7_img3 with Dissolve(2.0)

    pause

    c "[mc]... Eu odeio pensar nisso..."

    if priscila_namoro:

        c "Só que agora a gente tá juntos. Eu quero ser sincera e aberta com você."
    else:


        c "Você é meu melhor amigo... e eu me sinto segura com você. Eu... eu vou me esforçar, tá?"

    "Eu preciso decidir o que fazer quanto ao [gus] e tudo isso só existe por causa da Pri. O que ela tem pra falar é muito importante."

    "Só que também esse assunto é delicado pra ela, claro. É melhor eu perguntar só o que realmente eu achar essencial saber."

    label p7_perguntas:

        if p7_perguntas == 0:

            "Ok... será que eu pergunto alguma coisa pra ela sobre esse assunto? Ou eu decido isso sozinho?"
        else:


            if p7_perguntas < 2:

                scene pri7_img6 with Dissolve(1.0)

                c "Ufa..."

                mc desculpa "Eu nem imagino como isso pode ser difícil pra você."

                c "T-tudo bem... eu fico feliz de você se preocupar comigo."

                "Certo... eu preciso saber mais alguma coisa sobre isso?"
            else:


                scene pri7_img5 with Dissolve(1.0)

                c "E-era isso?"

                "Ela tá ficando muito triste... Melhor eu parar."

                mc desculpa "Sim. Desculpa falar sobre isso tá?"

                c "Não precisa pedir desculpas. Eu fui bem até, né?"

                mc normal "Com certeza."

    menu:

        "Como tudo isso começou? O lance do filme?" if p7_perguntas == 0:

            mc desculpa "Eu sei que esse é um lance pessoal e ninguém tem que se meter nisso, nem eu. Só queria que você soubesse isso."

            c "Tá..."

            mc serio "Eu só quero entender melhor isso, porque desde que você virou uma pessoa importante na minha vida, isso me deixa muito mal também."

            mc desculpa "Eu me preocupo demais com você, Pri. Eu queria que você fosse feliz e isso me deixa muito irritado com as pessoas."

            c "S-sei..."

            mc concentrando "Você me desculpa por ser intrometido? Só você sabe o que é passar por isso e mesmo assim eu fico... é egoísmo meu."

            c "Não, [mc]... eu te entendendo. E, eu fico muito envergonhada e com o coração apertado por você saber disso, mas eu fico feliz também."

            c "Parece que eu não tô sozinha. Poder contar isso pra alguém legal igual você, que não fica me julgando, me deixa mais leve, mais segura."

            c "Eu sei que você não se sente bem. Claro que isso é normal. Obrigada por ser sincero comigo. Prefiro que você fale do que me abandone."

            mc desculpa "Tá... Só que mesmo assim... eu peço desculpa. E prometo que nunca mais vou falar sobre isso."

            c "Certo... o que você quer saber? Eu prometo que vou contar tudo o que você quiser saber sendo o mais sincera que eu conseguir."

            mc serio "Ok... como tudo isso começou? Como essa proposta chegou pra você e você sabia o que tava envolvido?"

            c "Ai... agora que você perguntou... eu senti uma dor..."

            mc preocupado "Tudo bem. Não prec-"

            c "É difícil, mas eu vou falar tudo. Eu só preciso pensar um pouco..."

            mc "Claro..."

            c "..."

            scene pri7_img7 with Dissolve(2.0)

            c "Pelo que eu lembro... eu tava em algum estado no norte do país fazendo fotos. Eu já tinha começado a posar fazia um ano e pouco."

            c "A [a] apareceu e disse que tinha vindo pra capital e arranjado o melhor trabalho do mundo pra mim."

            c "Ela contou que tinha conseguido convencer um grupo de pessoas de uma distribuidora a me contratar pra fazer o papel em um filme."

            c "E não era só um papel, eu ia ser a protagonista da história."

            c "Eu fiquei tão feliz, [mc]. Eu não me aguentava!"

            mc envergonhado "Eu imagino..."

            c "Depois de uns dias, quando tava chegando o dia da reunião em que eu ia convensar com esses diretores, a [a] me chamou."

            c "Ela falou que tinha uns boatos que o diretor dava em cima das atrizes, mas que eram só boatos."

            c "Eu não acreditei, claro. Um senhor famoso igual ele. Nem passou pela minha cabeça que era verdade. E a [a] até concordou."

            c "No meio da reunião a gente falou do meu papel, eles pediram para eu ler algumas falas, vestir umas roupas..."

            c "Quando eu tava me trocando, o... o..."

            mc bravo "O velhor cretino."

            c "É-é... ele apareceu e eu me assustei. Eu tava quase nua. Ele se aproximou e falou... umas coisas pra mim."

            c "Naquela hora eu quase desmaiei, [mc]. Eu fiquei branca, gelada... tava na cara que era tudo verdade."

            c "Ele ficou lá, me olhando enquanto eu me trocava. E depois disse um negócio tipo assim."

            c "'Se você quiser trabalhar comigo, você vai ter que aceitar TODO o contrato, inclusive as cláusulas que não tão no papel.'"

            c "Até hoje eu lembro disso, [mc]... até hoje..."

            c "Eu não sabia o que fazer. Eu chamei a [a]... tentei falar pra ela que não tava acreditando naquilo. Que eu queria sair dalí."

            c "Mas ela... ela disse que era 'normal'. Que ele ia querer me ver pelada, talvez passar a mão em mim. Que era pouco."

            c "Eu não lembro o que eu pensei na hora. Eu meio que só tava seguindo ela. Eu-"

            c "Não... não posso colocar a culpa na [a]. Eu tinha que ter negado isso. Mas eu nem conseguia pensar... é duro de explicar. Foi rápido demais."

            mc serio "Pri. Olha... não fica pensando nisso de culpa. Só vai te deixar mais confusa."

            mc "Cada pessoa vai ver isso de uma forma. E eu, pessoalmente, acho que a [a] era sua agente, ela era mais velha e ela era mais experiente."

            mc "Ela que tinha que ter cuidado de você. Protegido você disso. Você é muito nova, tomar essa culpa sozinha não tá certo."

            mc desculpa "Mas não pensa nisso. Vamo focar no futuro."

            c "O-obrigada... [mc]... {i}chiuf{/i}... eu tô bem..."

            mc "..."

            $ p7_perguntas += 1

            jump p7_perguntas

        "Como você vê essa situação com o [gus]?" if p7_perguntas == 1:

            mc serio "Eu queria saber sua opinião sobre tudo isso. Eu sei que você se sente muito mal por isso, dá pra ver nos seus olhos."

            mc "Mas você se arrepende? Você, olhando agora, acha que tudo foi um erro?"

            c "N-nunca pensei nisso..."

            mc desculpa "Sério?"

            scene pri7_img7 with Dissolve(2.0)

            c "Acho que... eu nunca quis pensar nisso..."

            c "Eu... isso tudo é muito nebuloso pra mim. Acho que eu mesma me escondi do que aconteceu."

            c "Toda vez que eu penso nisso eu me sinto suja, nojenta, porca... então eu odeio, odeio, odeio pensar em qualquer coisa com isso."

            mc "Sei..."

            c "Mas se você quer saber... talvez eu consiga..."

            mc desculpa "Olha... eu não acho você nada disso. Eu vejo você como uma vítima disso. Nonjento é o velho abusador, não você."

            mc "E eu queria que você pudesse contar comigo."

            c "O-obrigada... o...brigada, [mc]... eu..."

            c "Eu não sei... eu tava quebrada quando a gente se conheceu. Mas depois que eu conheci você, eu mudei, sabe."

            c "Você me deu uma nova energia. É tipo como se eu tivesse em um quarto escuro e você tivesse abrido uma janela."

            c "Toda vez que eu tô lá, no escuro, eu penso na janela e olho pra ela. E depois daquela noite no lixão, eu me transformei."

            c "Foi lá que eu vi que eu podia confiar em você e que você faria qualquer coisa por mim."

            c "Eu me senti meio egoísta por jogar tudo em cima de você. D-desculpa... mas foi tão bom."

            if priscila_namoro:

                c "Ainda mais que você me pediu em namoro... foi acho que o pior e o melhor dia da minha vida..."

            mc charmoso "Que bom. Pode sempre contar comigo mesmo. Eu nunca vou deixar você sozinha, tá?"

            c "T-tá..."

            $ p7_perguntas += 1

            jump p7_perguntas

        "Se você pudesse parar tudo. Você pararia?" if p7_perguntas == 2:

            mc desculpa "E se você pudesse parar tudo agora? Se você pudesse chutar o pau da barraca? Você faria?"

            scene pri7_img4 with Dissolve(2.0)

            c "Eu penso muito nisso... mas eu tenho medo de muita coisa, sabe."

            c "Tenho medo de que tudo tenha sido por nada."

            c "Tenho medo de decepcionar a [a] e deixar meus fãs tristes."

            c "E se eu nunca mais conseguir um trabalho na vida? E se eu jogar tudo fora por causa disso?"

            c "Eu sei que eu não pareço, [mc]... mas eu pelo menos quero ser uma garota forte. Eu quero superar tudo isso."

            mc normal "Você é forte, viu?"

            c "Por isso que eu realmente não sei. Por um lado eu queria jogar tudo pro alto e mandar o [gus] se foder."

            c "Mas também eu penso em tudo o que eu estaria perdendo fazendo isso. Eu não quero ser uma criança."

            c "O mundo não é um mar de rosas, isso a [a] me ensinou..."

            c "E eu sei que eu tô, mesmo considerando tudo, em um lugar que muitas garotas gostariam de estar também."

            scene pri7_img7 with Dissolve(2.0)

            c "E é nisso tudo o que eu penso... e isso só me deixa mais nervosa, porque parece que eu tô me vendendo ainda mais..."

            c "Isso me deixa muito triste... e mais perdida..."

            mc concentrando "Eu queria poder ajudar você com isso, Pri. Mas o melhor seria falar com uma psicóloga sobre isso."

            mc normal "O que eu sei é que você é uma mina incrível e eu tenho orgulho de tudo o que você conquistou."

            mc charmoso "E mesmo que você se sinta muito mal, não esqueça que eu nunca vou me decepcionar com você."

            c "[mc]..."

            $ p7_perguntas += 1

            jump p7_perguntas

        "Eu não preciso incomodar ela com isso. Vou decidir por mim." if p7_perguntas == 0:

            "Pensando bem... eu posso tomar uma decisão sozinho, sem fazer ela passar por isso."

            mc normal "Você tem razão. Não quero gastar o tempo que a gente tem juntos com assuntos assim."

        "Eu perguntei tudo o que eu queria." if p7_perguntas > 0:

            "Chega. Eu não quero que ela sofra mais com isso."

            mc desculpa "Obrigado e desculpa por ficar falando disso."

    mc charmoso "Como eu falei várias vezes pra você, eu confio em você e eu vou tá do seu lado sempre que você precisar."

    scene pri7_img5 with Dissolve(1.0)

    c "[mc]... Eu não sei como eu ia passar por tudo isso sem você."

    mc "Claro que você ia passar."

    c "Não, não ia. Mas obrigada por acreditar em mim. Eu preciso de alguém do meu lado, sabe."

    c "Eu sei que isso é criancisse, que eu sou meio melosa e grudenta, mas eu não consigo viver sozinha no mundo. Eu preciso de alguém."

    c "Quando eu tô sozinha eu me sinto tão triste. Dá tipo uma angústia. Daí logo eu tenho que ligar pra alguém."

    mc desculpa "Cada pessoa tem suas coisas, Pri. Não fica assim. Você vai superar essas coisas, eu tenho certeza."

    c "Tá... mas fica comigo enquanto isso, tá?"

    mc charmoso "Claro."

    if priscila_namoro:

        mc "Perder a chance de ficar do lado da minha namorada deliciosa, cheirosa, gostosa..."

        c "Você tá me provocando, né?"

        mc envergonhado "Eu?"

        if p7_perguntas < 2:

            c "Sorte que nossa conversa não matou o clima. Eu ainda tô com muita vontade de curtir meu namorado hoje..."

            mc "Eu também quero curtir você hoje."



            c "Então pega em mim..."

            scene black with dissolve

            scene pri7_img8 with Dissolve(1.0)

            pause

            mc "O-opa."

            c "E se você fizer uma massagem em mim?"

            mc "Seria um prazer..."

            c "Hmm... sua mão é gostosa. É macia..."

            "Pegar na Pri assim tá me deixando louco. Eu não quero parar aqui..."

            label pri7_priscila_premium:

                pass

            "Será que eu tento puxar ela pra cima de mim?"

            menu:
                "Puxar ela pro seu colo":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_4

















                        jump pri7_priscila_premium

                    mc "Pri, deixa eu massagear mais pra cima..."

                    c "Pra cima?"

                    mc "Você vai gostar..."

                    c "Hmm... você tá pensando em sacanagem, né?"

                    mc "Faz tanto tempo que a gente não se curte de verdade... deixa eu pegar em você..."

                    c "Não sei, [mc]..."

                    mc "Mas eu sei... vem aqui, delícia..."

                    c "Só uma massagem então..."

                    scene black with dissolve

                    mc "Você vai ver a massagem que eu vou fazer..."

                    c "[mc]! O que você tá fazendo?!"

                    scene pri7_img9 with Dissolve(1.0)

                    pause

                    mc "A massagem não é muito melhor assim?"

                    c "M-mas e se alguém pegar a gente?!"

                    mc "Mas isso só não deixa as coisas mais quentes?!"

                    c "[mc]! Você tá doido!"

                    mc "Você tá me deixando doido, Pri! Eu quero que você fique louca também!"

                    c "Nossa..."

                    mc "Eu tô sentindo sua bunda em mim... seu corpo é maravilhoso..."

                    c "Ah... eu quero te agradar, [mc]... só que..."

                    mc "Calma... eu vou fazer você esquecer os problemas."

                    c "Como?"

                    mc "Assim..."

                    c "!"

                    scene pri7_img10 with Dissolve(1.0)

                    pause

                    c "A-ah! N-não!"

                    mc "Não? É ruim?"

                    c "Não... mas e se a-alguém..."

                    mc "É só um carinho. Se aparecer alguém a gente para. Só curte."

                    c "Hmm... tá bom... sua mão tá boa."
                    scene pnew_ani12 with Dissolve(1.0)
                    mc "Eu quero ver você gozar."

                    c "Já tá bom. Foi bom..."

                    "Eu paro agora? Não acho que ela chegou lá ainda..."

                    menu:
                        "Eu não vou parar agora!":


                            mc "De jeito nenhum. Eu quero ver você gozar."

                            scene pri7_img11 with Dissolve(1.0)

                            pause

                            c "[mc]! Ah! Hmm!"

                            mc "Você tá muito molhada. Eu sei que você quer."

                            c "Eu quero... mas... ah! Aí! Assim!"

                            mc "Assim é melhor. Eu quero ver você gemendo."

                            c "Hm-hmm! Hm! Aah!"
                            scene pnew_ani16 with Dissolve(1.0)


                            c "Você quer que eu goze aqui, é?"

                            mc "Vou manter você viciada."

                            c "Então me beija... deixa que eu dou carinho nela."

                            scene black with dissolve

                            scene ani02 with Dissolve(0.1)

                            pause

                            c "Hmm..."

                            "A Pri é tão gostosa, tão cheirosa... minha nossa... ficar com ela me deixa duro na hora."

                            mc "Você é demais, gata. Que lábio..."

                            c "Ah..."

                            mc "Imagina se seus fãs vissem você aqui agora? Nua no meio de uma praça esfregando a buceta?"

                            c "Ai... hmmm..."

                            mc "Aposto que eles já imaginam isso, né?"

                            c "Nnghhh... eles comentam cada coisa nos meus posts... hmmm..."

                            c "O que eles vão fazer comigo... aah..."

                            c "M-mas só você que faz de verdade, [mc]..."

                            menu:
                                "Assim que eu gosto. Eles querem, mas só eu faço.":


                                    c "Só você, meu amor!"

                                    mc "Hmmm..."
                                "Mas você adora ser a puta de todo mundo. Deixa eles aproveitarem.":


                                    c "Awahhh! S-sério?!"

                                    scene black with dissolve

                                    scene ani03 with Dissolve(0.1)

                                    pause

                                    mc "Todos eles já batem pra você, não batem?"

                                    c "Simmmm! Awwnnn!"

                                    mc "Até o orc lá no cinema aproveitou."

                                    c "Q-queinn... aaahn... E-era só a cena..."

                                    mc "Mas e se fosse de verdade? Você não ia querer experimentar um orc daqueles?"

                                    c "Nauaummm... aquele monstrooo... awwnn..."

                                    menu:
                                        "Você fala 'não', mas tá acabando com essa bucetinha.":


                                            c "Awhhh! Eu só aceitaria se você visse!"

                                            mc "Assistir minha namorada ser arrombada por aquele monstro imenso?"

                                            c "S-simmm! Eu vou deixar você e todo mundo cheio de tesaauumm! Hmmnnng!"

                                            c "Gozemm pra sua princesa! Seus tarados safados! Aawnn!"
                                        "Então tá.":


                                            mc "Agora só falta gozar."

                                    c "Eu vou gozaawwnn!"

                            mc "Isso! Goza pra mim, vai!"

                            c "Eu vou gozar! Não para! Mexe em mim!"

                            mc "!"

                            scene pri7_img11 with vpunch

                            pause

                            c "AAH! AAIIHHH!"

                            c "{i}puf puf{/i}"

                            mc "Era isso que eu tava falando..."

                            c "Você é fogo, [mc]..."

                            "Ela gozou, mas eu ainda tô com um fogo do cacete... não queria parar agora."

                            "Mas não sei se ela vai aguentar... e agora?"

                            menu:
                                "Tá bom por hoje":


                                    "Não tem porque exagerar. Eu já fiz ela curtir bastante hoje."

                                    mc "Tá bom. Que bom que você gostou."

                                    c "A gente pode se beijar um pouco?"

                                    mc "Claro. Vem aqui."

                                    show black with Dissolve(2.0)

                                    "..."

                                    scene pri7_img23 with Dissolve(1.0)

                                    c "Aaahh... que delícia..."

                                    mc "E outra coisa? Você tá sentindo?"

                                    c "Tô, safado..."

                                    c "Vou levantar, tá?"

                                    mc "Claro."
                                "Eu vou chupar ela":


                                    "Hoje eu tô com a macaca. Eu não vou parar aqui, não."

                                    mc "Pri, se prepara. Esse foi só o primeiro tempo."

                                    c "Q-quê?!"

                                    scene black with vpunch

                                    mc "Se alguém aparecer me fala!"

                                    c "[mc]!"

                                    scene pri7_img12 with vpunch

                                    pause

                                    c "A-ai! O que você tá fazendo, seu doido?!"

                                    mc "Eu quero que você goze de novo!"

                                    c "Eu ainda tô sensível..."

                                    mc "Por isso que eu só vou usar a língua. Bem devagarzinho..."

                                    c "Ai, [mc]... você é terrível... por que você tá assim hoje?"

                                    mc "Não sei. Eu tô doido por você, [c]."

                                    c "Ai, não fala assim..."

                                    c "Hmm... tá começando a ficar gostoso..."
                                    scene pnew_ani15 with Dissolve(1.0)
                                    mc "Isso..."

                                    c "Lambe gostoso... hmmm..."

                                    c "Tô ficando quente, [mc]. Vai. Continua..."

                                    c "..."

                                    scene pri7_img13 with Dissolve(1.0)

                                    pause

                                    "Ela tá começando a mexer o quadril. Ela tá pegando fogo."

                                    "Acho que eu vou conseguir fazer ela gozar de novo!"

                                    c "Isso! Ain!"
                                    scene pnew_ani13 with Dissolve(1.0)
                                    c "Vai! Vai! Enfia a língua dentro!"

                                    "Ela tá apertando minha cabeça nela! Deve tá quase lá!"

                                    c "Vou gozar de novo! Vai, [mc]!"

                                    c "VAII! AAHN!"

                                    pause

                                    scene pri7_img22 with vpunch

                                    pause

                                    c "Eu tô gozaaando!!!"

                                    scene pri7_img22 with vpunch

                                    pause

                                    c "{i}puf puf{/i}"

                                    c "Aiinnn... {i}puf puf{/i}"
                                    scene pnew_ani11 with Dissolve(1.0)
                                    c "..."

                                    mc "..."

                                    c "Agora me abraça?"

                                    mc "Claro."

                                    scene black with dissolve

                                    scene pri7_img23 with Dissolve(1.0)

                                    pause

                                    c "N-não acredito que você fez isso..."

                                    mc "Agora eu tô satisfeito..."

                                    c "Eu... e-eu ainda tô tremendo..."

                                    mc "Era assim que eu queria."

                                    c "Na próxima eu vou cuidar de você então."

                                    mc "Não esquenta. A gente vai fazer muito isso ainda. Principalmente quando acabar o filme."

                                    c "É-é..."
                        "Vou fazer o que ela disse":


                            "Eu queria agradar ela, mas se ela tá falando que assim tá bom, então tá bom."

                            mc "Gostou?"

                            c "Adorei..."

                            c "Agora vem aqui que eu quero te beijar um pouco..."

                            mc "Com todo o prazer."

                            show black with Dissolve(2.0)

                            "..."

                            scene pri7_img23 with Dissolve(1.0)

                            c "Aaahh... que delícia..."

                            c "Eu nem tô sentindo minha boca mais, [mc]..."

                            mc "E outra coisa? Você tá sentindo?"

                            c "Tô, safado..."

                            c "Vou levantar, tá?"

                            mc "Claro."
                "Não vou exagerar":


                    "Melhor eu não exagerar. Vou só ficar no básico mesmo."

                    mc "E aí? Tá bom?"

                    c "Hmm... e essa mão aí?"

                    mc "Gostou?"

                    c "Adorei... pode continuar..."

                    mc "Barra tá limpa?"

                    c "Tá limpa. Você conquistou esse benefício sendo um namorado companheiro e fiel."

                    mc "Opa."

                    c "Agora vem aqui que eu vou te beijar muito."

                    mc "Com todo o prazer."

                    show black with Dissolve(2.0)

                    "..."

                    scene pri7_img23 with Dissolve(1.0)

                    pause

                    c "Aaahh... que delícia..."

                    c "Eu nem tô sentindo minha boca mais, [mc]..."

                    mc "E outra coisa? Você tá sentindo?"

                    c "Tô, safado..."

                    c "Vou levantar, tá?"

                    mc "Claro."
        else:


            c "Eu queria muito passar a noite namorando, mas essa conversa meio que acabou com o clima. Você me desculpa?"

            "A gente quase nem se vê... eu queria muito passar esse tempo namorando..."

            "Se eu não tivesse perguntado tanta merda..."

            mc desculpa "Tudo bem..."

            c "Você ficou triste..."

            menu:
                "É que a gente quase não se vê...":


                    mc envergonhado "É que a gente quase não se vê. Daí eu queria passar mais tempo com você, sabe? Namorando..."

                    c "Eu sei, fofo... eu também queria."

                    mc normal "Mas eu entendo, viu? Eu sei que isso vai passar."

                    c "O-obrigada..."
                "Eu disse que tá tudo bem.":


                    mc desculpa "Eu disse que tá tudo bem, ok?"

                    c "T-tá..."

        scene black with dissolve

        scene pri7_img2 with Dissolve(1.0)

        c "Às vezes eu fico pensando que quando esse filme finalmente acabar, a gente podia sair daqui, [mc]."

        mc "Sair?"

        c "É. Ir pra algum lugar muito longe. Longe da cidade, das pessoas... só eu e você."

        mc "Sei..."

        c "Você acha isso muita viagem?"

        menu:
            "Assim... a gente tem uma vida aqui, né?":


                mc envergonhado "Pensando assim, do nada, parece um pouco viagem, sim. A gente tem uma vida aqui na capital."

                c "Hehe... verdade. É meio sem noção."

                mc normal "Mas acho que todo mundo pensa nisso às vezes. Digo, essa vontade de ir pra longe, desaparecer."

                c "Acho que sim... eu acharia super bacana."
            "Viagem nada. Ia ser massa.":


                mc surpreso "Viagem nada! Eu e você?! A gente podia sair hoje!"

                c "Haha... bobo. A gente não pode abandonar tudo de uma hora pra outra também."

                mc envergonhado "Que pena..."

                c "Mas eu fico muito feliz de saber que você aceitaria. Você é um fofo."

                mc "Hehe..."
    else:


        c "Tudo isso que tá acontecendo agora, eu só tô conseguindo lidar com toda essa merda porque você tá do meu lado, [mc]."

        c "Eu sei que não faz tanto tempo assim, mas parece que você é meu amigo por anos já."

        mc normal "Eu também sinto isso, sabia?"

        c "Que legal..."

        c "Eu não sei porque, mas o pessoal do filme não tem essa ligação. Eu sinto que não vou falar com ninguém depois que as gravações acabarem."

        mc desconfiado "Por que você acha isso?"

        c "Não sei... a gente só não se fala muito mesmo."

        c "A Ágata até que fala comigo de vez em quando, mas é só ela mesmo."

        mc "E a [a]?"

        c "Ah. Ela não é bem do filme, né?"

        mc envergonhado "Verdade... mas ela conversa com você?"

        c "Não muito. Ela tá sempre correndo aqui na capital ela diz. Vendo contratos e cuidando do dinheiro e de coisa administrativa."

        c "Eu não sei direito qual é o sonho da [a], sabe? Ela não fala direito sobre coisas pessoais."

        c "É só trabalho, trabalho, trabalho... agenda, impostos, contratos, revistas blá blá blá."

        c "Afe, que saco ha..."

        mc "Haha... saco mesmo. Ela precisa de um tempinho pra ela."

        c "Eu queria que ela se abrisse mais comigo. Me falasse dela, da família, se ela tá namorando alguém, sei lá. Nem isso eu sei."

        mc "Ruim assim..."

        "{i}Talalá tololó{/i}"

        c "Opa. Falando nela..."

        c "Ela quer que eu volte já."

        mc "Mas já? A gente nem conversou..."

    c "A [a] me trouxe e vai dormir lá em casa hoje. Sei lá, ela não sai do meu pé desde ontem."

    c "Só que dá pra gente voltar juntos até a ilha. Você quer? A gente pode ir andando..."

    mc charmoso "Claro. Não precisa nem pedir, né?"

    c "Eu acho que no fundo você não entende direito como você é legal, [mc]..."

    mc desconfiado "Hm?"

    c "Nada. Só continue sendo assim pra sempre. Promete?"

    mc envergonhado "P-prometo..."

    "Que que deu nessa mina?"

    scene pri7_img1 with Dissolve(1.0)

    c "Agora vem. A gente pode ir abraçados?"

    if not priscila_namoro:

        c "A-abraço de amigo..."

        mc normal "Haha..."

    mc normal "Claro..."

    mc "[c]... só mais uma coisa."

    c "Oi? Que foi?"

    mc "Se acontecer alguma coisa nos próximos dias, qualquer coisa fala comigo, tá?"

    c "Como assim?"

    mc "Só isso. Se alguma coisa inesperada acontecer assim e você precisar falar com alguém. Pode sempre me escrever."

    c "T-tá bom, ué... você tá bem?"

    mc "Tô haha!"

    c "Hmmm... então vamos?"

    mc "Opa, tô indo."

    scene black with Dissolve(1.0)

    "..."

    if priscila_namoro:

        mc "Boa noite, linda."

        mc "Boa noite, gatinho."
    else:


        mc "Boa noite, Pri."

        mc "Boa noite, [mc]. Obrigada pela companhia."

    "..."

    scene ape_geral with Dissolve(1.0)

    "Ufa..."

    "A [a] tá em cima da Pri."

    if p7_miranda:

        "Certeza que tem a ver com a nossa conversa de hoje."

    "Mas agora não dá pra esperar mais. Eu tenho que escolher o que eu quero."

    "{b}Denunciar ou não o [gus].{/b}"

    "Essa é a escolha mais complicada que eu tô tendo que fazer até hoje desde que comecei a trabalhar na revista."

    "Certeza que minha vida vai mudar muito dependendo do que eu escolher. Se eu for publicar a matéria, vou amanhã mesmo falar com o chefe."

    label p7_decisao:

        "Certo. O que eu faço?"

    menu:
        "Denunciar o [gus] em uma matéria na revista":


            "Se eu publicar a matéria, o [gus] vai se ferrar bonito. Ele vai ter que arcar com o que ele fez."

            "Por outro lado, eu vou mexer com gente grande que colocou muita grana nesse filme."

            "É isso mesmo que eu vou fazer?"

            menu:
                "Sim. Vou denunciar o [gus].":


                    $ p7_denunciou = True
                    $ p7_gustav = True

                    mc serio "Certo. Eu me decidi. {b}Eu vou publicar a matéria sobre o [gus]{/b}."

                    scene ilha_vista_noite with Dissolve(2.0)

                    pause

                    "Esse velho desgraçado vai pagar pelo que ele fez com a [c] e com todas as outras."

                    "Vou jogar o nome dele na lama e ele vai ter que vir à público responder sobre isso."

                    "Certeza que a coisa vai esquentar pro meu lado."

                    "Ele vai vir pra cima de mim e da revista, igual o chefe falou. Vou ter que me preparar bem pra passar por esse inferno."

                    "Eu vou precisar convencer a Pri e pelo menos mais uma pessoa a vir a público e corroborar as informações."

                    "Não consigo nem imaginar a repercussão que isso vai dar no país. Isso é matéria pra virar coisa internacional."

                    "Talvez até minha carreira dê uma melhorada... imagina ganhar um Prêmio Pulitzer?"

                    mc surpreso "Tô ficando empolgado!"

                    "Ou o [mar] vai acabar me mandando pra vala."

                    "Acho que vou dar uma andada pela cidade até o sol raiar. Não vai dar pra dormir essa noite."

                    "[c]... me espera só mais um pouquinho. Eu vou salvar você."
                "Deixa eu pensar um pouco mais...":


                    "Calma. Vou pensar mais um pouco."

                    jump p7_decisao
        "Ignorar a matéria e deixar o [gus] impune":


            "O [gus] faz isso há muito tempo. Se eu não publicar a matéria, provavelmente ele vai sair ileso dessa."

            "O velho nojento vai continuar abusando da Priscila e vai saber quantas garotas depois dela."

            "Mas ficando na minha eu não ferro o filme da Pri e nem mexo com gente poderosa que tá por trás do filme."

            "É isso mesmo que eu vou fazer?"

            menu:
                "Vou ignorar a matéria e não mexer com o [gus].":


                    $ p7_denunciou = True
                    $ p7_gustav = False

                    mc desculpa "Não adianta eu querer fingir que eu sou herói... ficar me enganando. O [gus] e esses caras tão em outro nível."

                    scene ilha_vista_noite with Dissolve(2.0)

                    pause

                    "Se eu me meter nisso, só tem coisa ruim me esperando. Inimigos, desgraça e talvez até morte..."

                    "E eu ainda ia embaçar o esquema da [a] e da [c]. Ela não me pediu nada, ela passou por tudo sozinha."

                    "Eu não tenho o direito de me meter agora e decidir tudo por ela e jogar todo esforço dela no lixo."

                    "As gravações estão no fim e logo ela vai sair desse inferno. E se existir justiça no mundo, o [gus] vai se foder ainda."

                    "Mesmo que não seja eu a ferrar esse velho cretino, espero do fundo do coração que alguém faça."

                    "Eu quero ser parceiro da [c] e dar o apoio que ela precisar. E quero me dar bem aqui na capital, crescer e ser alguém."

                    "É nisso que eu vou focar. E eu tenho certeza que esse é o melhor caminho pra mim."

                    "Agora eu tenho que falar pro chefe que vou desistir da pauta e ver o que acontece."

                    "[c]... eu quero ver você de novo e te dar força. Boa sorte, garota."
                "Deixa eu pensar um pouco mais...":


                    "Calma. Vou pensar mais um pouco."

                    jump p7_decisao



    $ renpy.choice_for_skipping()









    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v31_fim = True
    $ dia_priscila = dia + 3

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v31_fim","final","local")

    scene black with Dissolve(3.0)

    jump call_cidade



label priscila_evento8:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p8_save", extra_info="p8_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ priscila_e8 = "evento"

    $ tata_pontos = 0
    $ tata_convenceu = False
    $ p8_terminou = False

    "Mais um dia nessa cidade cheia de tranqueirada."

    "Ainda não tô acreditando no que uma celebridade tem que passar pra chegar lá. Parece tão surreal..."

    if not p7_denunciou:

        show black with dissolve

        "Eu tava pensando de novo sobre a situação da [c] e do [gus]..."

        label p8_acerto:

            "Será que eu vou denunciar ele mesmo?"

        menu:
            "Denunciar o [gus] em uma matéria na revista":


                "Se eu publicar a matéria, o [gus] vai se ferrar bonito. Ele vai ter que arcar com o que ele fez."

                "Por outro lado, eu vou mexer com gente grande que colocou muita grana nesse filme."

                "É isso mesmo que eu vou fazer?"

                menu:
                    "Sim. Vou denunciar o [gus].":


                        $ p7_denunciou = True
                        $ p7_gustav = True

                        mc serio "Certo. Eu me decidi. {b}Eu vou publicar a matéria sobre o [gus]{/b}."
                    "Deixa eu pensar um pouco mais...":


                        "Calma. Vou pensar mais um pouco."

                        jump p8_acerto
            "Ignorar a matéria e deixar o [gus] impune":


                "O [gus] faz isso há muito tempo. Se eu não publicar a matéria, provavelmente ele vai sair ileso dessa."

                "O velho nojento vai continuar abusando da Priscila e vai saber quantas garotas depois dela."

                "Mas ficando na minha eu não ferro o filme da Pri e nem mexo com gente poderosa que tá por trás do filme."

                "É isso mesmo que eu vou fazer?"

                menu:
                    "Vou ignorar a matéria e não mexer com o [gus].":


                        $ p7_denunciou = True
                        $ p7_gustav = False

                        mc desculpa "Não adianta eu querer fingir que eu sou herói... ficar me enganando. O [gus] e esses caras tão em outro nível."
                    "Deixa eu pensar um pouco mais...":


                        "Calma. Vou pensar mais um pouco."

                        jump p8_acerto

        hide black with dissolve

    "Agora que eu tomei minha decisão sobre a [c], eu preciso falar com o chef-{w=1.0}"

    scene mapa cidade with hpunch

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    "Maluco! Esse telefone sempre me assusta. Que coisa. Bem que podia ter uma função pra tirar essa vibração."

    a "Alô? [mc]?"

    scene ape_celular_falando with Dissolve(1.0)

    mc desconfiado "[a]?"

    a "Isso. Sou eu."

    menu:
        "Bom dia. Precisa de alguma coisa?":


            mc "Bom dia."

            a "Bom dia, [mc]."

            mc "Precisa de alguma coisa?"

            a "Ah. Eu queria falar com você um assunto."

            mc "O que foi?"
        "Que foi?":


            mc "O que você quer?"

            a "Estou atrapalhando?"

            mc "..."

            a "Bom..."

    a "Eu queria te chamar pra uma reunião aqui no centro."

    mc "Reunião?"

    if p7_tony:

        a "Você lembra do senhor que você conversou na pizzaria no outro dia?"

        mc "O chefe do [mar]?"

        a "Isso."
    else:


        a "É. Um homem com quem eu trabalho quer falar com você."

        a "Era pra vocês terem conversado aquele dia, mas você não foi falar com ele, né?"

        mc "Ah... realmente..."

        "E eu lá quero me meter com esse povo?"

    a "Ele quer mesmo que você participe desta reunião."

    menu:
        "Tudo bem. Eu participo.":


            mc "Tá bom. Pode contar comigo."

            a "Sério? Que bom... ele vai gostar bastante de ouvir isso."
        "O que isso tem a ver comigo?":


            mc "E o que isso tem a ver comigo?"

            a "Eu acho que essa conversa vai te interessar bastante. Será uma conversa pra definir o futuro da [c]."

            mc "Da [c]?! Ela vai estar aí?"

            a "Não sei se ela vai participar, mas independente da presença dela, o assunto tem tudo a ver com ela."

            "Se tem a ver com a [c]... é melhor eu participar."

    if priscila_namoro:

        "A Pri é minha namorada e o máximo que eu puder participar das coisas dela melhor."

    "Ela tá envolvida nesse mundo que ainda é muito estranho pra mim, mas aos poucos eu sinto que eu tô entendendo como tudo funciona."

    mc "Sim. Eu vou participar. Pode falar pra ele. E onde que vai ser?"

    a "Vai ser aqui no centro, no escritório da produtora. Eu vou te mandar o endereço por mensagem, pode ser?"

    mc "Pode."

    a "Até daqui a pouco, [mc]."

    mc "Ai ai..."

    scene ape_celular with Dissolve(1.0)

    "De novo eu vou acabar no meio desse povo. Será que eu não aprendo?"

    "{i}Tuli-li{/i}"

    mc "Ela mandou o endereço."

    "Esse lugar... Será que foi o mesmo lugar que a [c] assinou o contrato do filme?"

    "Eu lembro que foi por causa de uma reunião dessas que a gente se conheceu."

    "Ela veio pra capital pra fechar o lance do filme. Ela aproveitou pra vir pra ilha tirar satisfação com o chefe."

    "A gente acabou se vendo aquele dia... foi aquele encontro que mudou minha vida."

    "Se não fosse pela Pri, o chefe teria chutado minha bunda e eu ia voltar pra casa dos meus pais."

    "O mínimo que eu posso fazer é garantir que ela tenha uma oportunidade de ser feliz. Igual ela me deu."

    "E se eu tenho que tá numa reunião com esse pessoal aí, eu aceito."

    "Agora bora lá."

    scene black with dissolve

    call locomocao from _call_locomocao_2

    scene cidade centro10 with Dissolve(1.0)

    "Esse é o bairro mais nobre da capital. Claro que ia ser aqui."

    "FF... {b}Faux Filmes{/b}. Então a produtora do [gus] é da Faux News... aquele canal famosão que eu assisti esses tempos."

    if v28_fim:

        "Eu lembro quando eu fui lá com a [w]... aquele apresentador... falou cada coisa que deixou ela desnorteada."

    "Esse é o tipo de gente que trabalha junta nessas coisas."

    scene black with dissolve

    mc normal "Com licença. Meu nome é [mcc] e eu tenho uma reunião com a senhorita [a] e..."

    "Recepcionista" "Sim, senhor [mc]. No final do corredor."

    mc "Obrigado."

    "..."

    scene p8_reuniao1 with Dissolve(2.0)

    pause

    "Então aqui que vai acontecer a reunião. Eu fui o primeiro a chegar."

    "Dizem que é coisa de rico chegar por último nos compromissos. Pra mim é coisa de gente folgada."

    a "Bom dia, [mc]."

    mc "Hm?"

    scene p8_reuniao2 with Dissolve(1.0)

    pause

    mc "[a]..."

    a "Você chegou cedo."

    menu:
        "Eu só cheguei na hora.":


            mc "Nada de mais. Eu só cheguei na hora."

            a "Tem razão. Acho que a gente que atrasou."
        "Eu tô ansioso pra essa conversa.":


            mc "Eu tô ansioso pra essa conversa. Quero saber qual o objetivo disso aqui."

            a "Não tem necessidade disso. Você vai entender logo logo."

    a "Essa aqui você ainda não conhece. É a [ta]."

    ta "Olá! Muito prazer."

    mc normal "O prazer é meu, [ta]. Meu nome é [mc]."

    mc desconfiado "Ela vai participar da reunião também?"

    a "Com certeza. Bom... a reunião é sobre ela, né? Ela precisa tá aqui."

    mc "Sério?"

    a "Sim. A [ta] vai ser a nossa nova estrela. Ela vai conquistar o país e quem sabe o mundo."

    ta "Não precisa exagerar assim, [a]..."

    a "Não tô exagerando, garota. Aqui nessa sala você vai conversar com gente importante. Eu preciso de você com a cabeça no lugar."

    ta "Tá..."

    mc "Então ela é uma nova estrela... e você é agente dela?"

    a "Isso que a gente vai conversar hoje. A [ta] ainda tá começando a ver tudo. Não vai assustar ela, [mc]."

    mc zerado "Como assim, assustar?"

    scene p8_reuniao3 with Dissolve(1.0)

    ta "Por que assustar, [a]?"

    a "O [mc] é um paparazzo que trabalha para uma revista aqui da capital. É o tipo de gente que publica os podres que encontra sobre você."

    ta "N-nossa..."

    menu:
        "Esse é o meu trabalho, né?":


            mc envergonhado "Esse é só meu trabalho, não é nada pessoal, ok, [ta]?"

            ta "Ok..."

            a "Tá vendo? Ele acha até normal."

            mc "O que eu posso fazer? A gente faz o que precisa pra viver."
        "Não é bem assim. Eu não sou um vilão.":


            mc zerado "Não precisa ficar com medo, [ta]. Não é como se eu fosse seu inimigo."

            ta "Tá..."

            mc "A [a] que tá te colocando mesmo, isso sim."

            a "Ele fala desse jeito agora, mas é só pra entrar na sua cabeça."

    a "Jornalistas são o pior tipo de gente. Eles não tão nem aí pras pessoas. Eles só se preocupam com o que vão escrever."

    a "Pra eles não importa se o que eles tão escrevendo vão acabar com a vida da pessoa ou não. Eles querem leitores, acessos no site."

    ta "Então é assim..."

    a "É assim, garota. Nunca se esqueça disso. Não confie nesse tipo de pessoa."

    mc zerado "Como se você soubesse tudo sobre mim e sobre os jornalistas, né, [a]?"

    a "Não tô falando de você. Eu tô falando da sua profissão. É uma coisa assim, que todos fazem."

    mc serio "Você nem sabe na verdade. Você não trabalha com isso."

    a "Aí que você se engana. Eu sou amiga de uma jornalista muito importante há muitos anos. Eu sei como funciona."

    mc envergonhado "Do jeito que você fala, eu teria medo dessa sua amiga jornalista aí..."

    a "Não diria que você tá errado. É bom ter medo mesmo."

    "Quem será essa amiga dela? Do jeito que ela falou eu até lembrei de alguém... mas será que elas conhecem?"

    ta "Eu não sei se eu tô pronta pra isso, [a]..."

    a "Não seja boba, [ta]. Você tá mais que pronta."

    "???" "[ta]? Então essa é a famosa?"

    mc desconfiado "?!"

    scene black with dissolve

    a "Senhor, [gus]... que honra ver o senhor."

    mc surpreso "!!!"

    gus "Com licença, [a]. Eu quero conhecer nossa nova estrela."

    scene p8_reuniao4 with Dissolve(1.0)

    pause

    gus "Senhorita... com licença."

    ta "A-ah..."

    gus "Com todo o respeito, você é muito mais linda pessoalmente do que nas fotos."

    ta "..."

    a "[ta]?"

    ta "O-obrigada..."

    gus "Não se preocupe. Ela só está nervosa."

    ta "Bastante..."

    gus "Não precisa disso. Você vai ver que aqui você terá tudo o que você precisa para brilhar."

    gus "Contanto que você faça sua parte, fique tranquila que tudo acabará bem."

    ta "Ok..."

    gus "Você parece um pouco tímida..."

    a "Ela normalmente não é ass-"

    gus "Eu gosto de garotas assim."

    gus "Diga, [ta]. O que você acha de homens mais velhos?"

    scene p8_reuniao5 with Dissolve(1.0)

    ta "C-como assim?"

    gus "Homens mais velhos são mais maduros e podem conduzir você por um caminho mais seguro na vida, entende?"

    ta "E-eu não sei o que o senhor quer dizer com isso."

    gus "Tudo vai ficar claro para você daqui a pouco. Mas é importante você saber que não é fácil ser uma estrela."

    gus "Todas que vieram antes de vocês precisaram se esforçar muito. Elas entenderam que esse é um mercado complexo."

    ta "Sei..."

    gus "A vida dos adultos não é como um desenho de criança. Não tem o bonzinho e o vilão."

    gus "E às vezes a gente precisa fazer coisas que a gente não concorda, mas que são necessárias. Você entende isso?"

    ta "N-não sei... acho que sim..."

    ta "O senhor pode soltar, por favor?"

    a "[ta]..."

    gus "Tenha calma, [ta]. Todas são assim no começo. Mas o tempo ajuda."

    ta "C-com licença!"

    gus "Eu já vo-"

    "???" "Estão todos aqui?"

    mc desconfiado "Hm?"

    "Mais um agora?"

    scene p8_reuniao6 with Dissolve(1.0)

    pause

    gus "[to]... você. Eu vou sentar."

    to "Ora, se não é o [mc]. Obrigado por ter aceitado meu convite."

    if p7_tony:

        to "Eu sei que a gente conversou aquele dia, mas hoje estamos aqui pra outro motivo."
    else:


        to "Da outra vez você não apareceu para falar comigo."

        mc envergonhado "Pois é..."

    to "Hoje eu quero que você veja o nascimento de uma nova estrela. Quero que você veja como tudo é feito."

    menu:
        "Eu quero entender melhor vocês.":


            mc normal "Entendi. Eu quero mesmo entender melhor vocês."

            to "Você parece um homem razoável. Eu admiro isso."
        "Não vai mudar muita coisa.":


            mc desculpa "Não sei o que isso pode mudar..."

            to "Eu só quero que você acompanhe nossa conversa com os olhos abertos."

    to "Eu não quero convencer você de nada. Só quero que você preste atenção e veja como tudo é feito."

    mc desculpa "Olha... sendo bem sincero, eu sou um zé ninguém. Por que vocês querem que eu veja isso? Por que essa atenção comigo?"

    to "[mc]... eu sei que pode parecer algo estranho. O [gus] é o diretor mais famoso do país. A [c] é uma super celebridade."

    to "Eu entendo que isso pode parecer outro mundo, mas no fundo são só pessoas como eu e você."

    to "Talvez você pense que você e sua revista são peixes pequenos para um grupo como esse aqui, mas eu não gosto de ignorar problemas."

    to "Dá pra ver que você gosta da [c] e pessoas fazem coisas sobrehumanas quando elas se importam de verdade com alguém."

    mc envergonhado "Por mais que eu goste dela, não sei se eu realmente poderia fazer algo grandioso assim."

    to "Grandioso ou não, um buraco em um navio rapidamente pode se tornar o fim da embarcação. Como disse, não ignoro problemas."

    to "Agora eu vou me sentar. Apenas preste atenção e, por favor, peço que não publique nada sobre o que for dito aqui."

    mc "Nem sou louco."

    to "Muito bem. Fique à vontade."

    scene black with dissolve

    "Esse homem fala de um jeito tão calmo... tão seguro... dá uma impressão muito boa."

    "O que será que ele é nisso tudo?"

    scene p8_reuniao7 with Dissolve(1.0)

    pause

    "AGH! Sentei do lado do maldito do [gus]..."

    to "Agora que estamos todos aqui, gostaria de falar sobre o futuro desta jovem talentosa."

    $ to_nome = "Tony"

    to "Gostaria de me apresentar. Meu nome é [to] e sou um dos procuradores de um dos investidores do grupo Faux."

    gus "Falando nisso, [to]. Por que você está aqui? Eu me sentiria melhor se eu falasse diretamente com ele ao invés de você."

    to "Eu sei, [gus]. Mas ele é um homem ocupado. Ele pediu que eu acompanhasse tudo."

    gus "Se ele não tem tempo pra falar comigo, então tem algo errado na agenda dele. Eu não sou qualquer um, [to]."

    to "E ele sabe disso. Por isso mesmo ele me enviou."

    gus "Você tá com o nariz muito empinado."

    to "Peço desculpas se eu pareci esnobe ou acima do meu lugar."

    gus "Que seja... só avise ele que eu fiquei muito decepcionado com isso."

    to "Eu passarei suas palavras..."

    a "E-eu também queria agradecer por me chamarem para esta reunião."

    to "Você tem feito um bom trabalho, [a]. Seu faro com a [cc] foi incrível. Resolvemos investir em você."

    a "Eu agradeço. É o que eu sempre quis. E não será diferente desta vez."

    to "É o que esperamos."

    gus "A [ta] sem dúvidas é uma garota linda e jovem. Tenho certeza que ela vai ser uma estrela."

    to "Fale um pouco sobre ela, [a]. Quem é a garota?"

    scene p8_reuniao8 with Dissolve(1.0)

    pause

    a "A [ta] vem de uma família humilde do interior. Eu conheci ela da escola da [c] há alguns anos. Depois ela mudou com a família."

    a "Fiquei sempre com ela na cabeça. Eu nunca esqueci o quão linda ela era e essa energia inocente e ao mesmo tempo animada."

    to "E a família?"

    a "Os pais estão sempre fora trabalhando. A [ta] vivia praticamente sozinha em casa cuidando do irmão pequeno."

    a "Ela acabou desenvolvendo essa independência muito cedo."

    to "Isso é bom. Garotas que amadurecem cedo sem a presença dos pais já sabem como tomar decisões por si mesmas."

    to "E você falou pra ela de todas as possibilidades?"

    a "Sim. Eu expliquei que ela terá uma carreira estruturada, contratos, muito dinheiro e um caminho certo para a fama."

    to "Mas, claro, isso depende dela também, certo?"

    a "C-claro."

    scene p8_reuniao9 with Dissolve(1.0)

    pause

    to "Você entende isso, não entende, [ta]?"

    ta "Eu? C-como assim?"

    a "Eu falei com você sobre isso."

    ta "Eu sei... mas eu não sei se eu entendi muito bem."

    gus "Essa inocência dela. Eu adoro isso..."

    to "[gus], por favor."

    scene p8_reuniao10 with Dissolve(1.0)

    gus "[to], você entende que tudo isso só acontece por minha causa? É meu nome que faz esses filmes."

    to "Eu entendo, senhor... e somos todos muito gratos por isso."

    gus "Às vezes eu sinto que você esquece seu lugar. Você é só um garoto de recados dos Donatello. Só isso."

    gus "Ah! Você pode ter herdado a pizzaria, só que você não é um Alighieri de verdade. Não passa de um usurpador."

    gus "Você sabe que o Luca nunca foi à favor do casamento. Olha pro seu nome... você nem deveria estar aqui."

    to "[gus]... peço desculpas se eu exagerei, mas agora não é hora disso."

    gus "Então pare de agir comigo dessa forma."

    to "A [ta] é uma garota nova. É a primeira vez dela na capital, não é, [a]?"

    a "Isso."

    to "Precisamos deixar ela confortável. Obviamente todos nós vamos conseguir o que buscamos dessa parceria. Mas no momento certo."

    gus "Tudo bem... mas eu não preciso de você pra me falar isso."

    to "Obrigado."

    scene p8_reuniao9 with Dissolve(1.0)

    to "Desculpa por isso, [ta]. Às vezes nós adultos também nos comportamos como crianças. Mas é só pra você ver como estamos felizes por ter você aqui."

    ta "T-tá..."

    to "A [a] te falou um pouco, mas eu queria te explicar melhor como tudo vai acontecer."

    to "Nós temos contratos com revistas de moda e marcas de roupas. Você já ouviu falar da Blergh!, não ouviu?"

    ta "S-sim. Daquele modelo... ele é lindo... quer dizer, desculpa!"

    a "[ta]..."

    to "Haha... isso. Nós vamos conseguir contratos pra você com marcas como essa. Vamos conseguir espaço na rede da Faux e criar sua imagem."

    to "Você vai ganhar espaço na mídia. Vai aparecer em programas de entrevista, na capa das revistas, em desfiles e até filmes."

    gus "Exatamente. E não é qualquer filme, linda. É o meu próximo mega sucesso."

    to "Isso. Você vai ganhar tanto dinheiro que nem imaginaria ser possível."

    ta "N-nossa..."

    to "Você vai poder ajudar sua família. Isso não parece legal?"

    ta "Acho que sim..."

    a "Como assim, [ta]? Isso é incrível! Não fale desse jeito!"

    ta "Desculpa..."

    to "Tá tudo legal, [a]. Sua casa é complicada, não é, [ta]?"

    scene p8_reuniao11 with Dissolve(1.0)

    ta "É bastante..."

    to "Ficar sempre sozinha em casa, seus pais estão lutando pra vocês terem o que comer, mas nunca te dão atenção."

    to "Cuidar do seu irmão mais novo sozinha... toda essa responsabilidade. E você nem pode reclamar porque a situação tá difícil."

    to "Não seria justo ficar reclamando porque seus pais também tão dando duro. Eu sei como é isso. Eu passei por isso."

    ta "Verdade?"

    to "Eu nasci muito pobre, [ta]. Demorou muito pra eu chegar onde eu tô hoje."

    to "Por isso eu sei como é. E eu sei que essa é uma excelente oportunidade pra você."

    to "Sair de casa, viver SUA vida. Sem seu irmão e a dificuldade dos seus pais. Ter fãs e pessoas que gostam de você."

    to "Você nunca mais vai se sentir sozinha. Milhares de pessoas que te amam e vão fazer de tudo pra ficar do seu lado."

    ta "Nossa... seria legal..."

    a "E você também vai ter eu, [ta]. Você sabe que eu me importo com você."

    ta "Eu sei..."

    a "Só é importante que você faça sua parte também."

    ta "Mas, [a]..."

    a "Você não ouviu o que ele falou?"

    ta "É que... isso... eu não sei..."

    gus "[a]."

    scene p8_reuniao12 with Dissolve(1.0)

    pause

    a "Senhor [gus]."

    gus "Espero que você entenda que pra mim nada disso faz sentido sem a parte em questão."

    a "..."

    gus "[to], eu não estou nem um pouco feliz com esta conversa."

    to "Eu entendo, senhor [gus]... e eu tenho confiança na [a]. Ela sabe como tudo funciona."

    to "A [ta] é uma garota linda. Tem a personalidade e o background certos para a posição. Ela vai aceitar."

    gus "É o que eu espero."

    to "Eu acho que nós podemos fazer uma pausa. Foi uma longa conversa. Vamos tomar uma água e voltamos em uma hora."

    gus "Eu não gosto de ficar aqui. Isso nunca aconteceu antes."

    gus "Eu esperava mais de você, [a]."

    a "Tudo vai ficar bem, senhor [gus]. Me perdoe."

    a "Vai tomar uma água, [ta]. Eu já encontro você lá fora."

    ta "T-tá..."

    gus "Não se preocupe, [a]. Eu vou mostrar o prédio para a [ta]."

    ta "!"

    a "Vai com ele, garota."

    ta "T-tá..."

    to "Então nos encontramos novamente em uma hora. Até lá."

    scene black with dissolve

    a "[mc]."

    mc "Oi!"

    a "Posso falar com você uma coisinha?"

    mc "S-sim. Diga."

    scene p8_fala1 with Dissolve(1.0)

    pause

    a "E então? O que achou?"

    menu:
        "Tudo isso foi terrível.":


            $ tata_pontos += 1

            mc bravo "O que eu achei? Isso aqui é um circo por acaso? Um bando de animais?"

            mc "Eu sei sobre o que vocês tavam falando com ela. E ela sabia também. Vocês não têm vergonha?"

            scene p8_fala2 with Dissolve(1.0)

            a "Eu não sei por que eu pensei que seria diferente... esse é você, [mc]. Preso nas suas coisas."

            mc serio "Se você quer dizer preso no que é ético e certo, então esse sou eu mesmo."
        "Não sei o que falar...":


            mc desculpa "Sinceramente, nem sei o que falar..."

            a "Essa é uma reunião de gente grande, [mc]. Você pode não estar acostumado, mas nem tudo é preto no branco."

            a "Você precisa entender que aqui são todos adultos trabalhando. Fazendo o que precisam fazer. Só isso."

            mc "Não sei, [a]... isso não tá certo."

    a "Eu quero que você pare um pouco e pense no que isso significa pra você."

    mc desconfiado "Pra mim?"

    a "Sim. Aqui pode ter uma coisa pra você também. Você pode se benificiar disso tanto quanto a gente."

    mc serio "Acho que você tá me confundindo com esses caras."

    mc "Então foi isso que aconteceu com a [c]? É isso que você queria que eu visse?"

    mc "Uma garota humilde e inocente que foi trazida pra um... sei lá... um antro de lobos."

    scene p8_fala3 with Dissolve(1.0)

    pause

    a "Por favor, [mc]. Não comece com essa ladainha."

    a "Tanto a [c] como a [ta] sabem muito bem o que tão fazendo. Elas entendem o que tão apostando. Você que é inocente."

    a "Elas sabem o que as esperam e sabem o que vão ganhar com isso. Ninguém aqui tá apontando a arma pra cabeça dela."

    a "Não tá vendo o rolo que tá dando aqui? Isso se chama 'livre arbítrio'. A oportunidade de se escolher o que quer."

    a "Você, de verdade, acha que se ela aceitar, ela vai ser uma ovelha no meio dos lobos?"

    "Essa questão não é fácil. Eu sei que ela que vai escolher, mas olha pra isso aqui."

    "O [to] disse que a [a] escolheu a garota certa, com o 'background' certo. Isso quer dizer alguma coisa."

    "Será que eu concordo com ela? Que, se ela aceitar, realmente é só uma escolha dela e eles não têm responsabilidade?"

    a "Eu sei o que você tá pensando. Mas vamos ser sinceros aqui. Você acha que ela é só uma ovelha? Ela não pode escolher?"

    menu:
        "Concordo, ela realmente tem escolha...":


            mc desculpa "Acho que você tem razão... no fundo é ela quem vai escolher. Ela pode só falar 'não'."

            scene p8_fala4 with Dissolve(1.0)

            pause

            a "Então você é inteligente... não é uma coisa tão difícil de entender."

            a "Nós apresentamos tudo pra ela e, no fim, ela é a única responsável pela escolha dela."

            mc "Sim. Ela pode falar sim ou não. Mesmo que o 'sim' seja atrativo demais, ela precisa ter força pra negar."

            a "SE ela quiser negar, docinho. Eu aposto que ela não vai querer. É uma vida boa demais e o preço é pequeno."

            a "Foi a mesma coisa que aconteceu com a [c]. Ela sabia o preço, mas aceitou. Agora você vê?"

            mc "..."

            "A [c] podia ter dito não, mas ela quis participar disso tudo. Virar um objeto sexual do [gus]."

            "Mas alguma coisa, no fundo, tá me incomodando. Não parece tão simples assim."
        "Discordo. Vocês armaram pra ela aceitar.":


            $ tata_pontos += 1

            mc bravo "Não. Não é fácil desse jeito. Pode parecer fácil, mas não é."

            mc "O [to] disse que você achou uma garota com o 'background' certo. Eu sei o que isso quer dizer. Uma garota propensa a aceitar."

            mc "O fato dela ser nigligenciada pela família. De não ter ninguém pra olhar por ela... de viver uma realidade difícil com o irmão."

            mc "Eu sei que isso não é coincidência. E agora eu entendo o seu trabalho, [a]."

            scene p8_fala5 with Dissolve(1.0)

            pause

            a "O que você quer dizer com isso?"

            mc bravo "Eu sei que seu trabalho não é encontrar garotas talentosas. Mas é achar garotas que aceitem se escravizar."

            mc desculpa "Mulheres que sejam bonitas, claro, com uma energia de celebridade? Claro... mas não é o mais importante."

            mc "Você procura garotas frágeis, sem amparo, propensas a se vender por uma vida assim."

            mc bravo "Você aprendeu com a [c] e fez a mesma coisa com essa nova garota."

    "Eu sei que em um primeiro momento realmente é escolha dela. Ela é quem fala 'sim' ou 'não'. Isso é simples mesmo."

    "Mas pensa no resto. Uma garota que veio de uma família pobre, que sofre sendo a verdadeira mãe do irmão."

    "Uma jovem esquecida pelos pais, que estão ralando pra que eles tenham o que comer."

    mc desculpa "Falar pra uma garota nessas condições que ela pode ter uma vida diferente... muito melhor..."

    mc "A única contrapartida é aceitar tudo o que for dito. Aceitar um trabalho super puxado, viajando pra cá e pra lá."

    mc "A [c] quase nem tem tempo pra ela. E sem contar ter que aturar esse velho ridículo do [gus]."

    mc "Ela tem, sim, uma ideia de onde ela tá entrando. Mas será que ela, de verdade, entende? Alguém tá do lado dela?"

    mc bravo "Eu não tenho certeza se é uma escolha justa... uma garota pobre contra uma corporação do tamanho de vocês."

    scene p8_fala6 with Dissolve(1.0)

    pause

    a "Você não entende nada, [mc]... você acha que tá pensando nela, achando que sabe o que é certo, o que é justo."

    a "Mas sabe o que não é justo? Viver uma vida esquecida. Não ter chance de subir na vida. Pobreza pra todos os lados."

    a "Nem todo mundo tem chance de vir pra capital estudar e conseguir uma vaga em um emprego decente."

    a "Muita gente só vê buraco pra todos os lados."

    a "Eu era uma ninguém. E agora tenho uma oportunidade de sentar na mesa de pessoas como um diretor de cinema!"

    a "E é graças a mim que a [ta] e a [c] também sentaram! Eu não quero que elas vivam igual eu vivi!"

    a "Ser uma zé ninguém que não tem nem dinheiro pra ter certeza se vai dar pra jantar! Você não sabe o que é ser pobre de verdade!"

    mc desculpa "..."

    a "Claro que o [to] e o [gus] tão se aproveitando das garotas, mas e daí? É um preço pequeno pro que vem depois."

    a "Não ache que você pode julgar a gente que tá batalhando pra ter uma vida melhor. Pense nisso."

    mc preocupado "[a]."



    a "{i}fuuhhh{/i}"

    a "Acho que eu acabei soltando os cachorros, né?"

    mc envergonhado "Normalmente você não é assim... mas eu entendo."

    scene p8_fala4 with Dissolve(1.0)

    a "Não foi dando bronca nos homens que eu cheguei aqui."

    mc "A é?"

    a "Você sabe que eu tenho outras formas de trazer você pro meu lado..."

    a "Eu tenho medo do que eles tenham câmera na sala. Por que você não vem aqui no escurinho do corredor comigo?"

    a "Eu vou te mostrar uma coisa... sem compromisso..."

    label pri8_premium1:

        pass

    "Eu acho que eu sei o que ela tá propondo... e agora?"

    menu:
        "Vamo ver o que você tem aí.":


            mc safado "Falando assim é difícil falar não... acho que eu vou dar uma olhada sem compromisso."

            a "Era o que eu estava esperando ouvir. Vem aqui."

            scene black with dissolve

            scene pri8_img1 with Dissolve(1.0)

            pause

            a "Aqui parece bem mais reservado... pro que eu queria te mostrar..."

            mc "Eu tô vendo..."

            a "Você não quer um pouquinho disso que eu tenho aqui?"

            mc "M-mas aqui? E se alguém voltar antes de uma hora?"

            a "A gente tem tempo suficiente pra você ver, pegar... e mamar um pouquinho também se você quiser..."

            mc "A-ah..."

            a "E então? Posso fazer esse agradinho pro meu bebê?"

            mc "[a]..."

            "E se a [ta] me pegar aqui com ela sem roupa? Ou o [gus] e o [to]... será que eu brinco com a [a] aqui?"

            menu:
                "Eu vou voltar pra sala.":


                    mc "Acho melhor eu voltar pra sala e esperar o pessoal voltar."

                    a "Tem certeza? Você sabe que eu tenho algo aqui que você vai adorar..."

                    mc "M-melhor não."

                    a "Você quem sabe... mas não esquece de tudo o que eu falei."

                    mc "Pode deixar."

                    a "A gente se fala, [mc]."

                    scene black with dissolve
                "Só uma brincadeirinha rápida.":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_5

                        jump pri8_premium1

                    mc "Uma hora é bastante tempo... você pode me agradar se você quiser."

                    a "Olha aqui."

                    scene pri8_img2 with Dissolve(1.0)

                    pause

                    a "Tinha como resistir?"

                    mc "Você sabe que eu não consigo falar não pra me aproveitar de você."

                    a "Você tem me pegado cada vez com mais vontade, [mc]."

                    mc "Você me deixa com vontade. Não é por mal, não."

                    a "Eu sou crescidinha. Pode vir com tudo que eu te aguento, garoto."

                    mc "Acho bom. Que eu quero aproveitar bem nossos minutinhos."

                    a "Mas hoje você pode se divertir com meus peitos. É perigoso mais que isso."

                    mc "Agora que eu comecei eu não sei se eu consigo parar, [a]."

                    a "Não seja um garoto desobediente..."

                    window hide

                    pause

                    mc "Hmm... seus peitos são gostosos demais. Você me deixou duro pra caralho."

                    a "É pra isso que eles servem. Pra você se aproveitar deles."

                    a "Mas agora tá bom. Você já se divertiu muito."

                    "Parar agora? Faz só uns minutinhos que a gente começou."

                    menu:
                        "Lamber ela":


                            mc "A diversão só começou. Eu aprovei seus melões, mas agora eu quero sentir outra coisa."

                            a "E-ei."

                            mc "Vira aqui, deixa eu te ajudar."

                            scene black with vpunch

                            a "A-ah! [mc]!"

                            scene pri8_img3 with vpunch

                            pause

                            mc "Hmm!"

                            a "Q-que você tá fazendo?"

                            mc "Tô saboreando você inteira."

                            a "Ah... e se eles voltarem?"

                            mc "Não acho que esses safados vão se importar de ver você assim? Eles fizeram coisa muito pior!"

                            a "Hm-hmmm!"

                            mc "É bom?"

                            a "Você tá me comendo com vontadnnn!"

                            mc "Eu vou deixar você ensopada."

                            a "Hmm! Mete a língua dentro!"

                            mc "{i}shlep{/i}"

                            window hide

                            pause

                            mc "Agora você tá pronta."

                            a "Ah... pronta pra quê?"

                            mc "Pra mim, ué. Molhadinha assim não tem problema eu abusar mais um pouquinho, né?"

                            a "N-não hoje, [mc]. Você pode me comer outro dia. Outro lugar."

                            "Ela quer que eu pare aqui..."

                            menu:
                                "Ok. Eu como você depois.":


                                    mc "Tá bom... eu como você depois..."

                                    a "B-bom garoto. A gente vai ter tempo mais pra frente."

                                    scene black with dissolve

                                    mc "Verdade... Eu vou voltar pra sala."

                                    a "E eu vou procurar a garota... vai saber o que o [gus] fez com ela."

                                    mc "..."

                                    a "E não esquece de mim quando for falar com a [ta], ok? A gente precisa fechar com ela. Me ajude."

                                    mc "Pode deixar. A gente se fala."
                                "De jeito nenhum. Vamo até o fim.":




                                    $ miranda_sexo1 = True

                                    mc "Nada disso. Se é pra experimentar você, eu quero experimentar tudo. E vai ser agora."

                                    a "Você tá impossível... Se a [ta] ver a agente dela dando assim..."

                                    mc "Vamo falar menos e transar mais."

                                    mc "Agora vai. Deita aqui."

                                    scene black with dissolve

                                    "{i}slap{/i}"

                                    a "Hmm!"

                                    scene pri8_img4 with Dissolve(1.0)

                                    pause

                                    mc "Ah!"

                                    a "Hmmm!"

                                    mc "Valeu a pena molhar você, [a]. Entrou facinho."

                                    a "Tá gostoso me comer, safado?"

                                    mc "Muito. Sua buceta é uma delícia."

                                    a "Então aproveita e goza."

                                    mc "Hmf!"

                                    window hide

                                    pause

                                    scene pri8_img5 with Dissolve(1.0)

                                    mc "Eu tô quase lá, [a]!"

                                    a "Cuidado... só não grita..."

                                    mc "D-desculpa... é que você gostosa demais."

                                    a "Então come, garoto. Pode soltar toda sua porra em mim."

                                    a "Ah... Assim... Seu pau é bom."

                                    mc "Você também! É m-melhor do que eu imaginei."

                                    a "Se lambuza então. E me lambuza também."

                                    mc "N-não tem problema?"

                                    a "Você não prefere me encher de porra?"

                                    menu:
                                        "Gozar dentro dela":


                                            mc "A-ah! Eu vou encher você!"

                                            mc "Toma tudo!"

                                            a "I-isso..."

                                            scene pri8_img6 with vpunch

                                            pause

                                            mc "Aaaahhh!"

                                            a "Hhmmmf!"

                                            a "Ahh... eu tô sentindo dentro de mim..."
                                        "Gozar fora":


                                            mc "N-não vou gozar em você."

                                            a "Você que sabe, meu bem..."

                                            mc "T-tá vindo, [a]!"

                                            a "Joga em mim, amor!"

                                            mc "A-aahh!"

                                            scene pri8_img6 with vpunch

                                            pause

                                            a "Hhmmmf!"

                                            a "Você me sujou inteirinha, [mc]."

                                            mc "D-desculpa..."

                                    mc "{i}puf puf{/i}"

                                    a "A-ah... ainda tô sentindo... você fez de tudo comigo hoje..."

                                    mc "A-ainda tá saindo..."

                                    a "Ahnn... que garotão cheio de energia..."

                                    mc "S-se arruma. Não sei quanto tempo passou."

                                    a "Claro."

                                    scene black with dissolve

                                    a "Vai logo pra sala. Eu vou atrás da [ta]."

                                    mc "T-tá..."
                        "Melhor parar aqui":


                            mc "Você tá certa. É perigoso."

                            a "Bom garoto. A gente vai ter tempo mais pra frente."

                            mc "Verdade... Eu vou voltar pra sala."

                            a "E eu vou procurar a garota... vai saber o que o [gus] fez com ela."

                            mc "..."

                            a "E não esquece de mim quando for falar com a [ta], ok? A gente precisa fechar com ela. Me ajude."

                            mc "Pode deixar. A gente se fala."

                            scene black with dissolve
        "Vou ficar aqui mesmo.":


            mc serio "Acho melhor eu ficar aqui mesmo e esperar o pessoal voltar."

            a "Tem certeza? Você sabe que eu tenho algo aqui que você vai adorar..."

            mc envergonhado "M-melhor não."

            scene p8_fala5 with Dissolve(1.0)

            a "Você quem sabe... mas não esquece de tudo o que eu falei."

            mc normal "Pode deixar."

            a "A gente se fala, [mc]."

            scene black with dissolve



    scene p8_reuniao1 with Dissolve(1.0)

    pause

    if miranda_sexo:

        "Uou... as coisas esquentaram com a [a]..."

        "Eu tô curtindo muito essa nossa relação 'profissional'."

        "Antes dela querer me ganhar pelo sexo ela tava bem diferente..."

    "Parece que a [a] foi bem sincera aquela hora... ela parecia super ressentida..."

    "Eu não sei o que elas passaram... talvez ter que aguentar o [gus] não seja o pior pra elas..."

    "Mas uma coisa não muda a outra. O [gus] e o [to] tão errados de se aproveitar da desgraça delas pra benefício deles."

    "É isso que eu tenho que lembrar. Dar uma vida melhor pra elas não é justifica pra fazer o que eles tão fazendo."

    "Mas sem eles... como elas ficariam? Merda... quanto mais eu penso nisso, menos eu tenho certeza."

    "Acho que eu v-"

    "{i}rrrrrkkk{/i}"

    mc desconfiado "Opa?"

    scene p8_fala7 with Dissolve(1.0)

    pause

    ta "D-desculpa. Eu queria puxar a cadeira, mas travou..."

    mc normal "Tudo bem. Eu que tava pensando e assustei."

    ta "Se quiser eu espero lá fora."

    mc "Não precisa. Eu que tô de intrometido aqui. Você é a grande estrela do show, né?"

    ta "Haha... não sei ainda..."

    menu:
        "Sei...":


            mc envergonhado "Entendi... não é fácil, né?"

            ta "Nada... é bem complicado mesmo."

            mc "Pois é..."
        "O que você achou da reunião?":


            $ tata_pontos += 1

            mc normal "O que você achou do que foi discutido até agora?"

            ta "Não sei... eles me deram esse tempo pra pensar, mas não sei."

            ta "Tem bastante coisa passando pela minha cabeça agora. Tô até meio zonza."

            mc envergonhado "Não é fácil mesmo..."

    ta "E você o que tá fazendo aqui?"

    mc envergonhado "Se eu te falar que eu não sei você acredita?"

    scene p8_fala8 with Dissolve(1.0)

    pause

    ta "Você parece mais perdido do que eu..."

    mc zerado "Com certeza."

    mc normal "A [a] me chamou pra vir aqui, mas não sei exatamente o motivo."

    ta "Sem querer ser má, mas é legal ver alguém mais perdido do que eu aqui."

    mc envergonhado "Haha... eu te entendo. Tem horas que as coisas só vão acontecendo, né?"

    ta "Sim!"

    menu:
        "Você quer me contar o que você tá pensando?":


            $ tata_pontos += 2

            mc normal "Se você quiser conversar sobre isso, talvez eu até sinta que tô fazendo alguma coisa útil aqui."

            ta "Hmm... acho que tudo bem."

            ta "Assim... Quando a [a] me disse que eu ia ser modelo e talvez até atriz, eu achei super bacana, sabe?"

            ta "Ela disse que eu ia poder ajudar minha família. Eles nem iam precisar mais trabalhar."

            ta "Pareceu tão legal, sabe?"

            mc "Imagino."

            ta "Eu topei viajar com ela na hora. Eu tava super empolgada."

            scene p8_fala9 with Dissolve(1.0)

            pause

            ta "Mas durante a viagem ela disse umas coisas... eu achei que não tivesse entendido direito."

            ta "Só que depois da nossa conversa hoje aqui, agora eu acho que eu entendi o que ela queria dizer."

            ta "Eu ainda não tenho certeza se eu entendi. Parece que... parece estranho demais pra ser verdade."

            mc desculpa "..."
        "É assim mesmo.":


            mc desculpa "Não se preocupe. É assim mesmo..."

            scene p8_fala9 with Dissolve(1.0)

            pause

    ta "Agora eu não sei o que eu faço. É tudo estranho demais..."

    mc preocupado "Essa confusão é normal, viu?"

    ta "Eu me sinto meio boba... como se fosse só eu."

    mc desculpa "Não é boba, não. Eu fiquei igualzinho vendo eles falando."

    ta "Mas eu não sei o que eu faço agora. A gente viajou até aqui pra eu assinar o contrato..."

    menu:
        "Você tem que decidir logo então.":


            mc envergonhado "O negócio é decidir logo então."

            ta "Sim... tô ferrada..."
        "Você pode não assinar.":


            $ tata_pontos += 1

            mc envergonhado "E se você não assinar?"

            ta "Não assinar? Isso seria... não sei... a [a] ia ficar brava comigo, né?"

            mc "Mas a gente tá falando da sua vida. É uma decisão importante. Você devia pensar em você mais que na [a]."

            ta "É... mas sei lá... eu não queria decepcionar ela..."

    scene p8_fala10 with Dissolve(1.0)

    pause

    ta "Antes da gente sair da minha cidade, a [a] me perguntou se eu queria vir. Ela me explicou as coisas."

    ta "Ela disse que pra ela isso era muito importante. Que eu tinha que ter certeza."

    ta "E eu disse que eu tinha... que eu queria muito sair de casa... que eu ia fazer tudo o que eu tivesse."

    ta "Mas agora que a hora tá chegando... eu tô tão nervosa..."

    mc normal "Olha... ficar assim na hora de uma decisão importante é normal. Todo mundo é assim."

    mc "A gente tá falando de algo que vai mudar sua vida inteira. Se sentir nervosa é o mínimo. Não se preocupe com isso."

    ta "..."

    mc "Eu acho que o negócio é você pensar no que você vai fazer agora. Esse tempo na reunião é pra isso."

    ta "Verdade... Ah... como é seu nome mesmo?"

    mc "[mc]."

    ta "Isso... [mc]... se você tivesse na minha situação, o que você ia fazer?"

    mc surpreso "Eu?!"

    ta "É. Por favor..."

    "O que eu faria? Se eu vivesse em uma casa super pobre, sem chance de nada na vida... minha família não me dá atenção..."

    "E daí aparece a chance de ser rico, famoso e sair desse buraco. Mas eu teria que transar com alguém que eu odeio..."

    "Eu ia ter que obedecer tudo, desistir dos amigos, do lazer. Comer o que me mandam, fazer o que me mandam..."

    "O que eu faria?"

    mc desculpa "Bom, [ta]..."

    menu:
        "Eu aceitaria.":


            mc envergonhado "Eu acho que aceitaria. Assim, é impossível falar com certeza sem estar no seu lugar."

            mc "Mas pensando aqui agora, acho que eu aceitaria, sim. Essa é uma proposta que melhoraria minha vida pra sempre."

            mc normal "É um dinheiro e uma fama que eu nunca conseguiria de outro jeito."

            scene p8_fala11 with Dissolve(1.0)

            pause

            ta "É verdade... Mas e as... outras coisas?"

            mc desculpa "Eu sei... mesmo assim acho que eu ia escolher aceitar. Não dá pra ter tudo, né?"

            ta "..."
        "Eu não aceitaria.":


            $ tata_pontos += 3

            mc serio "Claro que eu não aceitaria. Nem preciso pensar muito."

            scene p8_fala11 with Dissolve(1.0)

            pause

            ta "Você perderia tudo?"

            mc desculpa "Sim. E não é porque eu sou um riquinho... Eu também tenho que ralar bastante, sabe?"

            mc "E eu até tenho que fazer várias coisas que meu chefe manda. Até entregar coisas que eu não quero..."

            ta "E-então... isso não é a mesma coisa?"

            mc "Falando assim, parece mesmo... mas tem duas grandes diferenças, [ta]."

            mc "A primeira é que o que eu faço não está fora da lei. Contanto que eu não invente e engane os leitores da revista, não tem nada de errado."

            mc envergonhado "Às vezes eu realmente posso expor alguém. Mas isso não é ilegal."

            mc desculpa "Você reparou que ninguém aqui falou realmente o que você tem que fazer? Todo mundo sabe que exigir isso é ilegal."

            ta "É verdade... isso é contra a lei. Tem que ser."

            ta "E qual é a outra coisa?"

            mc "A segunda é uma diferença que não tá no que é feito, mas COMO é feito."

            mc serio "Por mais que eu precise do meu emprego, ninguém nunca foi atrás de mim com uma proposta sedutora igual você."

            mc "O jeito que eles te escolheram... que a [a] te apresentou tudo. Isso é mesquinho demais."

            mc bravo "Eles tão usando a riqueza e o poder deles pra fazer o que quiser com pessoas necessitadas como você."

            ta "..."

            mc desculpa "E é triste como a [a] caiu nessa. Uma pessoa que tá fazendo tudo pra entrar nesse mundo."

    ta "Eu acho que você tem razão, [mc]..."

    ta "Mas e se eu tiver pensando demais? E se nem for assim tão ruim?"

    mc desculpa "Isso é uma coisa que você vai ter que pensar. Pra mim, o lado ruim parece realmente ruim."

    mc "Sabe, [ta]..."

    if priscila_namoro:

        mc "Eu sou namorado da garota que veio antes de você."
    else:


        mc "Eu sou amigo da garota que veio antes de você."

    ta "Da [cc]?"

    mc "Isso. Aliás, foi ela quem salvou meu emprego na revista. Eu sou muito agradecido a ela por isso."

    mc "E ela sofreu muito com isso, sabe? Muito mesmo... então eu acho que você tem que tá pronta pro lado ruim."

    scene p8_fala12 with Dissolve(1.0)

    pause

    ta "Parece bem ruim..."

    mc charmoso "No fundo, se tem uma coisa que a [a] falou certo, é que é você que vai tomar sua decisão. Só você."

    mc "Você precisa pensar direitinho no que VOCÊ quer pra sua vida. Esquece sua família, a [a] e os outros."

    mc "Pensa com o seu coração e com sua cabeça e depois assuma as consequências do que você escolheu."

    ta "Mas e as pessoas?"

    mc "Todo mundo faz tranqueragem na vida. Todo mundo pensa primeiro no próprio umbigo. Ninguém pode reclamar da sua escolha."

    ta "A-acho que sim..."

    mc desculpa "Se você quer aceitar, isso não tem a ver com ninguém. Mas isso é algo que você tem que escolher por você."

    mc charmoso "E se você não quiser, azar o dos outros. Outras coisas vão aparecer na sua vida. Eu tenho certeza."

    mc envergonhado "Provavelmente não vai aparecer nenhuma tão grande desse jeito, mas, né? Essa é rara..."

    ta "Eu não sei se você quer que eu aceite ou não..."

    menu:
        "Eu quero que você recuse.":


            $ tata_pontos += 1

            mc charmoso "Você que tem que escolher... mas se eu tivesse que falar algo agora pra você, eu diria pra você não fazer."

            ta "C-certo..."
        "Eu quero que você aceite.":


            mc desculpa "Não é meu lugar escolher, mas se eu tivesse que falar, eu diria pra você aceitar, superar e viver feliz."

            ta "Então é isso que você acha..."
        "Eu não quero nada. Você quem escolhe.":


            $ tata_pontos += 2

            mc envergonhado "Você escutou o que eu falei? Você tem que fazer essa escolha, [ta]."

            mc charmoso "Tira um tempinho e pensa de verdade. E daí siga com isso. Eu sei que você vai saber."

            ta "Mas eu... tudo bem..."

    ta "Acho que eu preciso de mais um tempo..."

    mc charmoso "Vai ser bom."

    ta "[mc]..."

    scene p8_fala13 with Dissolve(1.0)

    pause

    ta "V-valeu por ter conversado comigo. A gente nem se conhece e você foi super atencioso. Obrigada."

    mc charmoso "Não foi nada. Tô torcendo pra que você seja feliz não importa o que você faça."

    ta "Eu vou pensar agora e daí eu falo com a [a]. Eu tava perdida, mas acho que agora eu consigo pensar."

    ta "Eu queria que ela tivesse feito isso que você fez."

    menu:
        "A [a] vai te ajudar do jeito dela.":


            mc envergonhado "Eu acho que a [a] tá tentando te ajudar do jeito dela. Por mais estranho que pareça."

            ta "Eu vou lembrar disso..."
        "A [a] tem os objetivos dela. Cuidado.":


            $ tata_pontos += 1

            mc envergonhado "Olha, eu acho que a [a] tem os próprios objetivos dela. É uma pena, mas é isso..."

            ta "Vou ficar de olho."

    ta "Agora eu vou indo lá, tá legal? Acho que vou andar um pouquinho."

    mc charmoso "E eu vou indo. Nossa conversa fez eu pensar na [c]. Não deve ter sido fácil pra ela."

    ta "Se ela for meio parecida comigo, então não foi nada fácil."

    mc "Vou ligar e conversar com ela. Se o [gus] tá aqui, então ela deve tá de folga."

    ta "Boa sorte no encontro."

    mc charmoso "Valeu, garota. E boa sorte nas suas coisas também."

    ta "Ah! Só uma coisa. A gente pode trocar números? Se não for te atrapalhar... talvez eu precise conversar de novo..."

    mc "Claro. Tudo bem. Vou ficar feliz se der pra ajudar em alguma coisa."

    ta "Tá! Valeu. O meu número é esse aqui..."

    scene black with Dissolve(2.0)

    "..."

    scene cidade centro10 with Dissolve(1.0)

    pause

    "A [ta] me lembrou da Pri. A gente se viu lá no parque aquele dia à noite, mas depois disso nem saímos mais."

    if priscila_namoro:

        "A gente tá namorando, mas nem conseguimos curtir direito."

        if praia_priscila_local:

            "Tirando aquele dia na praia. Aquele passeio realmente foi bacana. Finalmente a gente se curtiu um pouco."

    "Eu sinto que eu devia passar mais tempo com ela. E se o [gus] tá aqui... talvez ela também tenha vindo."

    "Ou será que é melhor eu voltar pra reunião?"

    "Acho que não... eu vi o que eu tinha que ver. Falei com ela... agora a [ta] tem que decidir."

    "O que será que ela vai resolver? Será que eu influenciei ela de algum jeito?"

    if tata_pontos >= 6:

        $ tata_convenceu = True

        "Eu acho que ela tava mais pra não aceitar... mas é duro ter certeza. Eles podem fazer a cabeça dela fácil."
    else:


        "Eu acho que ela vai aceitar... mas é duro ter certeza. Eu vou acabar sabendo disso cedo ou tarde pela [a] ou até pela Pri."

    "Agora eu só t-"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    mc zerado "Me ligando de novo... deve ser a [a]."

    mc desconfiado "Não é. Que número é esse?"

    mc "Alô?"

    "???" "Oiee!"

    mc surpreso "Pri!?"

    c "Sou eu! Assustei você?!"

    mc envergonhado "Sim. Seu número tá diferente."

    c "Pois é. Eu troquei."

    menu:
        "Fiquei feliz com a surpresa.":


            mc charmoso "Fiquei feliz de saber que era você. Quem dera todas surpresas fossem assim."

            c "E você como sempre charmoso."

            mc "Só com as garotas bonitas."

            c "E cafajeste..."

            mc envergonhado "Ei!"
        "Por que você trocou?":


            mc desconfiado "Por que você trocou de número?"

            c "Achei melhor... agora vou adicionar só as pessoas que eu gosto."

            mc envergonhado "Parece uma boa."

    mc normal "Aliás, eu tava pensando em você agora."

    c "Ownn..."

    if priscila_namoro:

        c "Esse meu namorado é ou não é muito fofo?"

        mc envergonhado "Haha..."

    c "Por quê? O que aconteceu que você lembrou de mim?"

    mc desculpa "Então... foi por causa da reunião de hoje."

    c "Reunião? Ah! Espera... que reunião?"

    mc "Da [a] e da menina nova com a produtora do seu filme."

    c "Nossa... como você sabe disso?"

    mc normal "E se a gente saísse agora?"

    c "Agora?"

    mc desculpa "Pra você não dá?"

    c "Não! Não é que não dá... é que... bom, ok. Você quer ir em um bar aí onde você tá?"

    mc zerado "O preço das coisas por aqui não rola, não. Eu tava pensando na ilha... talvez no bar do [gar]."

    c "Eu adoro o [gar], mas pra mim na ilha não dá. Ah! Eu tenho um lugar."

    mc desconfiado "Você não tá ficando na ilha?"

    c "Não. Dessa vez eu não tô lá."

    mc normal "Tudo bem. Pode me passar onde é que eu vou lá."

    c "Tá. Só me espera que eu vou me arrumar e já tô saindo."

    mc "Ok. Até daqui a pouco."

    c "A gente se vê, gato."

    scene black with dissolve

    "..."

    scene cidade centro2 with Dissolve(1.0)

    pause

    "Nesse bairro aqui já dá pra aguentar..."

    if v34_fim:

        "Eu lembro quando eu fui com a [d] lá naquele bar Aquarium. Sorte que a gente acabou não bebendo nada..."

    "Se bem que eu esqueço que a [c] deve ter uma boa grana. Nem todo mundo tá na pindaíba igual eu."

    "Acho incrível como ela ainda quer sair comigo. Não tenho nem condição de gastar num bar um pouco mais caro..."

    mc "Opa. Aqui é o lugar."

    scene p8_bar1 with Dissolve(2.0)

    pause

    "O lugar é bem bacana..."

    mc normal "Ela deve tá chegando daqui a pouco."

    c "Ainda com essa mania de falar sozinho?"

    mc surpreso "O-oi!?"



    scene pri8_img7 with Dissolve(1.0)

    pause

    c "Rwarrr!"

    mc normal "Haha..."

    c "Oi. Mas eu não tô mentindo, tô? Você adora falar sozinho."

    mc envergonhado "Do que você tá falando?"

    c "Lembra lá na praça? A primeira vez que a gente foi lá. Acho que eu peguei você falando sozinho..."

    menu:
        "É culpa sua que me deixa nervoso.":


            mc envergonhado "A culpa é sua que me deixa nervoso. Daí eu preciso ficar repassando tudo na cabeça."

            c "E ainda vai colocar a culpa em mim? Que tipo de cavalheiro é esse?"

            mc "Do tipo que não gosta de passar vergonha por falar sozinho."

            c "Esse seu jeito sincero sempre foi muito fofo, [mc]."

            mc "Que bom que você acha fofo..."
        "Nem lembro disso...":


            mc envergonhado "Ah... nem lembro disso..."

            c "Você tá tentando sair dessa, mas eu lembro muito bem."

            mc "Nanana..."

            c "Tá bom. Eu não vou te encher..."







































    mc "Faz tempo que você conhece esse lugar?"

    c "Mais ou menos. Eu vou mais no bar do [gar] lá na ilha."

    c "Mas depois que a gente se conheceu eu não tenho saído muito. Acho que eu prefiro quando a gente faz alguma coisa juntos..."

    mc envergonhado "E com as gravações você nem tem tido muito tempo, né?"

    c "Nem fala... mas agora acabou. E foi até por isso que eu liguei pra você!"

    mc surpreso "Sério?! Acabou!?"

    c "Sim! Finalmente a gente passou tudo e regravou o que precisava... meu trabalho acabou, [mc]..."

    mc normal "Que bom. Nem acredito!"

    c "Agora o filme tem outras etapas lá, mas minha parte acabou."

    mc "Bacana. Bora sentar e você me conta certinho."

    c "Tá."



    scene black with dissolve

    scene pri8_img8 with Dissolve(1.0)

    pause

    mc "Então... o que vai acontecer agora?"

    c "Agora o filme tem a parte de pós-produção. Eles vão colocar o som, editar, adicionar os efeitos especiais."

    c "Todas essas partes técnicas eles fazem agora. Até porque a gente grava a mesma cena várias e várias vezes."

    c "Agora o editor vai escolher os melhores ângulos e takes pra fazer o filme. Bastante coisa eles jogam fora também."

    mc "Então nem tudo entra no filme..."

    c "Não. O filme tem que ter um tempo certo lá. Os filmes do [gus] tem uma hora e meia. Eles são meio diretos e mais simples."

    mc "Entendi..."

    menu:
        "E o que você achou do trabalho?":


            mc "E como foi atuar no filme? Era o que você esperava?"

            c "Ah... não sei se era exatamente o que eu tinha imaginado..."

            c "Foi bem difícil. Tinha um bocado de texto que a gente tinha que decorar. Devia ter mais de mil páginas aquilo."

            c "O filme era algo mais pensando na ação, então não teve parte muito dramática."

            c "A maioria das vezes eles queriam que eu ficasse pulando e rolando pra depois editarem e fazerem as cenas de ação."

            c "Mas pensando em tudo, acho que foi bem legal. Eu gostei."

            mc "Que bom."
        "Tenho certeza que vai ser sucesso.":


            mc "Tenho certeza que ele vai fazer sucesso."

            c "Tomara... podia abrir portas pra mim."

            mc "Tenho certeza que vai."

    mc "De qualquer jeito agora essa é uma etapa que acabou, né? O que você tá pensando em fazer agora?"



    scene pri8_img9 with Dissolve(1.0)

    pause

    c "Hmm..."

    c "É que ainda não acabou..."

    mc "Não?"

    c "Eles... eles me chamaram pra fazer outro filme."

    mc "Quê?!"

    c "É... eles gostaram de mim... e querem que eu faça outro."

    c "Dessa vez eu não vou ser a protagonista. Mas eu vou ter um papel secundário."

    mc "Mas... você não disse que queria acabar com isso e viajar? Sair disso tudo?"

    c "Eu sei... eu falei... mas não sei se eu quero desistir ainda."

    c "O pior já passou, sabe? Abandonar tudo na melhor hora... quando eu vou tá famosa pelo primeiro filme... seria um desperdício."

    menu:
        "Entendi. Se é o que você quer...":


            mc "Se é isso que você quer..."

            c "Eu acho que é o que eu quero, sim."

            mc "..."

            scene pri8_img10 with Dissolve(1.0)

            pause

            c "Que foi? Você parece estranho, [mc]..."
        "Não acho que isso é o melhor pra você.":


            mc "Olha, [c]... eu não sei se essa é a melhor opção, sabe?"

            c "Hm? Por quê?"

            mc "Agora você parece ok com isso, mas até um tempo atrás você tava super triste. Você vai querer mais disso?"

            scene pri8_img10 with Dissolve(1.0)

            pause

            c "Eu achei que você fosse me apoiar... até a [a] me apoiou nisso."

            mc "Calma. Eu quero conversar com você sobre isso."

            if priscila_namoro:

                mc "Eu sou seu namorado. Eu quero participar dessas coisas com você."
            else:


                mc "Eu sou seu amigo. Eu quero participar dessas coisas com você."

            c "Tá... o que você quer falar?"

            mc "Eu quero que você me fale. Porque eu sempre pensei que você tava odiando isso tudo e queria só terminar."

            mc "E agora você diz que vai passar por isso de novo? Mais um filme? Vai saber quanto tempo você vai ficar presa."

    mc "Eu não sei se eu concordo com isso, sabe?"

    c "A gente tá falando da minha carreira, [mc]. Isso é muito importante pra mim."

    mc "Eu sei que é importante. Mas eu também já vi você muito triste por causa dela. Não vale à pena pensar melhor?"

    c "Você acha que eu não pensei? Fui EU que passei por tudo."

    mc "Tipo... hoje eu conheci a [ta] na reunião."

    c "A garota que eles vão colocar no meu lugar, né?"

    mc "É assim que funciona? Eles vão te trocar?"

    c "É... parece que as pessoas não conseguem gostar da mesma celebridade por muito tempo."

    c "Eles precisam tá sempre trocando e trocando... pra manter a galera interessada..."

    menu:
        "Infelizmente o mundo é assim.":


            mc desculpa "Infelizmente o mundo é assim, né? As pessoas não têm paciência pras coisas hoje em dia. Não adianta a gente brigar."

            c "Sim... a gente precisa fazer o que dá... mas é triste mesmo assim..."

            mc "Eu sei..."
        "Você concorda com isso?":


            mc desculpa "E você concorda com isso? Acha que tá certo eles fazerem assim com você e as outras?"

            c "As pessoas são assim, [mc]... não é culpa de ninguém."

            mc "Eu sei que as pessoas são assim, mas sei lá, eu não concordo. Devia ter um jeito de fazer diferente..."

            c "Obrigada por querer me proteger... eu me sinto melhor."

            mc desculpa "Mas não é isso..."



    scene pri8_img11 with Dissolve(1.0)

    pause

    mc "Depois de ver a [ta] hoje. Uma garota simples, novinha, que veio de uma família complicada. Ela tem esperança de uma vida melhor."

    mc "Daí a [a] já grudou nela e eles vêm com essa coisa de 'oportunidade'. Eu sei que vai ajudar ela de algum jeito..."

    mc "Mas esse jeito deles me irrita. Parece que eles têm o poder e podem fazer o que quiser com ela."

    mc "Ou ela aceita TUDO e tem uma vida melhor ou recusa e volta pra merda. Por que só tem essas opções?"

    mc "Daí eu lembrei de você, sabe?"

    c "..."

    mc "Você deve ter passado pela mesma coisa. Começou a aparecer, eles viram como você era talentosa, bonita, querendo uma vida melhor."

    mc "E daí deram aquele empurrão na sua carreira e te colocaram no filme pra lucrar com você."

    mc "Mas a condição era que você tinha que aceitar tudo ou não ia ter nada."

    c "Foi... foi bem assim..."

    mc "Aposto que a [a] tava louca pra você aceitar."

    c "Claro... ela disse que era nossa chance de sair dessa vida e ter alguma coisa melhor."

    mc "Depois do que ela me disse hoje, eu acho que a [a] realmente quer seu bem e da [ta] também. Ela quer ver vocês fazendo sucesso."

    mc "O problema é que ela quer fazer isso do jeito dela. Parece que ela não pensa em como isso pode ferir vocês também."

    c "Ela sempre falou que tudo era um preço pequeno pra gente ter uma vida de sucesso."

    mc "Mas será que é mesmo? Será que vale à pena aceitar tudo pra ter dinheiro?"

    c "Eu... eu não sei..."



    c "Puff... eu tô com calor, [mc]. Dá licença..."

    mc "C-claro."



    scene pri8_img12 with Dissolve(1.0)

    pause

    c "Desculpa. Que que você tava falando?"

    mc "A-ah..."

    menu:
        "V-você tá incrível.":


            mc "V-você tá fantástica..."

            c "Obrigada... mas e aí?"

            mc "A-ah! Então..."
        "Eu tenho que me concentrar.":


            "Eu tô falando uma coisa importante, eu não posso perder o controle agora."

    mc "Sabe, Pri... acho que isso é algo que cada pessoa tem que ver. Não adianta pensar na opinião dos outros."

    mc "Não adianta pensar muito em família, religião e outras coisas. Isso é só você que vai saber."

    mc "Como VOCÊ se sente com isso. Qual é o preço pra VOCÊ. Não importa o que a [a] acha. A [a] tem as coisas dela."

    c "[mc]... eu não sei o que eu acho... eu pensei muito... mas eu não sei o que é melhor pra mim."

    c "Eu amo a minha carreira. Eu amo meus fãs, eu amei fazer o filme... mas você tem razão. Eu tô triste."

    c "Você sabe como eu fiquei durante tudo isso. Eu pensei até em me matar, [mc]..."

    c "O lado bom é muito bom... mas o lado ruim é muito ruim..."

    c "Você é a pessoa que eu mais confio hoje em dia. Mais que a [a]. O que você acha que eu faço?"

    mc "Eu não sei se eu d-"

    c "Por favor! Eu preciso que você me fale o que eu tenho que fazer! Por favor, [mc]!"

    "Não... como eu posso decidir uma coisa dessas por ela? Isso vai definir a vida dela pra sempre."

    "E se a vida dela for uma desgraça? Ela vai me culpar pra sempre."

    if priscila_namoro:

        "Mas eu sou o namorado dela. Será que tá certo eu lavar as mãos?"

    "Aaaah! Caralho! Eu tô tão indeciso quanto ela! O que eu falo?!"

    menu:
        "Você tem que parar agora.":


            $ p8_escolha = "desaprova"

            mc "Eu acho que você tem que parar."

            c "Verdade?"

            mc "Eu vi você sofrer muito por isso, [c]. Um sofrimento terrível, sabe?"

            mc "E eu acho que, de verdade, o lado ruim pesou mais. Eu acho que você seria mais feliz parando agora."

            mc "Você já sofreu o que tinha que sofrer. Conquistou algo incrível. E mesmo que acabe agora, sempre vai tá lá."

            mc "Eu acho que só você pode decidir, mas como você pediu minha opinião, eu tô falando o que eu acho."

            c "Sim... eu pedi..."
        "Você tem que continuar com eles.":


            $ p8_escolha = "aprova"

            mc "Eu acho que isso é coisa sua. Não sou eu que tenho que falar... mas você me pediu..."

            mc "Mesmo sendo terrível as consequências, eu acho que é algo que vai durar pouco."

            mc "Você disse que gosta dos seus fãs, e se você tá pronta pra aguentar a parte ruim, eu acho que você devia ir fundo."

            c "Você acha mesmo?"

            mc "Eu falei que é você quem sabe. Mas é isso que eu acho."

            c "Obrigada por ser sincero..."
        "Eu não posso escolher por você.":


            $ p8_escolha = "certo"

            mc "Olha, Pri. Eu sei que você tá precisando de uma luz e você confia em mim, mas eu não posso responder uma coisa dessa."

            c "Por favor, [mc]! Você não tá vendo que eu preciso de ajuda?!"

            mc "Eu sei, mas não é essa ajuda que é melhor. Não é falar pra você se você deve escolher uma coisa ou outra no seu lugar."

            mc "Eu vou tá com você e te apoiar. Vou tá do seu lado pra te ajudar não importa o que você escolha."

            mc "Mas escolher por você, isso não dá. Eu não posso forçar minha opinião assim. Se não eu vou tá fazendo igual eles fizeram com você."

            c "Puxa... mas eu precisava..."

            mc "Desculpa..."

    c "Tipo... eu achei que tivesse escolhido, sabe?"

    c "Só que cada pessoa fala uma coisa!"



    scene pri8_img13 with Dissolve(1.0)

    pause

    c "Minha mãe fala que tá orgulhosa de mim, daí vem você e fala que eu tenho que pensar bem!"

    c "A [a] quer que eu continue porque vou ter uma carreira incrível, mas eu não consigo sentir isso!"

    c "Por que eu não posso só ter um emprego normal?!"

    if priscila_namoro:

        c "A gente começou a namorar e tem que ficar falando de toda essa merda!"

        c "Eu quero ser uma namorada bacana pra você! Nem sei porque você ainda tá comigo!"

    c "Eu só trago problema! Você só quer ter seu trabalho e viver suas coisas e eu continuo te complicando!"

    mc "Eu sei que é frustrante... mas tá tudo bem. Eu gosto de fazer parte das suas coisas. A gente tá junto nessa."

    mc "Não esquece que você salvou meu trabalho. Era pra eu tá muito pior se não fosse por você."

    c "Eu nem penso nisso..."

    mc "Quando a gente quer estar com alguém, não adianta ser só na hora boa. É nos problemas que a gente se sente mais perto."

    c "[mc]..."



    scene pri8_img14 with Dissolve(1.0)

    pause

    c "Você realmente acha isso?"

    mc "Acho. De verdade."

    c "Então..."

    if p8_escolha == "desaprova":

        c "Eu sei que você não queria, e você tem razão."

        c "Eu sei que eu vou sofrer muito... Só que..."

    c "E-eu acho que eu vou querer continuar trabalhando lá."

    if priscila_namoro:

        "Não acredito..."

        c "Eu sei que isso não é certo porque a gente namora e... a gente sabe o que isso tudo significa."

        mc desculpa "Significa que você vai continuar vendo o [gus]?"

        c "..."

        mc "Vai continuar mais fora da cidade do que aqui... que a gente quase não vai se ver... é isso que significa?"

        c "Eu sei que isso não tá certo, [mc]! Mas, eu prometo que esse é o fim! Essa é a última coisa que eu vou fazer!"

        c "Depois eu vou seguir o que eu puder sem eles. Só a gente! É verdade!"

        mc "Pri..."

        "Ela disse que ia parar com tudo isso no parque... e agora isso..."

        "Ela tá falando de novo que vai parar... mas será que ela vai mesmo? Eu vou ter que aguentar isso por quanto tempo?"

        "Eu não sei se esse namoro ainda vai dar certo pra mim... principalmente desse jeito."

        label p8_termina:

            "Eu disse que ia ficar do lado dela. E eu vou. Mas não precisa ser como namorado."

        menu:
            "Terminar o namoro com a [c].":


                "Desde que eu e a [c] começamos a namorar, a gente quase não teve um momento bom."

                "Eu apanhei, fui ameaçado de perder a vida, o emprego, e tirando alguns momentos com ela... foi tudo muito difícil."

                "A [c] é uma garota incrível, mas ela tá presa nessa vida. Ela é super fofa, muito gata, e ela se preocupa comigo."

                "Eu tinha esperança que a gente fosse ficar juntos... mas agora ela vai continuar nessa vida?"

                "Não sei se eu vou aguentar..."

                "Eu não sou um cafajeste de terminar com ela depois. Se eu for terminar, vai ser agora antes dela aceitar."

                "Vou falar na cara dela, ser sincero, e prometer que vou ficar do lado dela como amigo se ela quiser."

                "Encerrar tudo com ela... é isso mesmo que eu quero?"

                menu:
                    "Sim. TERMINAR com a [c].":


                        $ priscila_namoro = False
                        $ p8_terminou = True

                        "Eu vou terminar com ela. É o melhor pra mim agora. Eu não quero me envolver mais nesse rolo todo."

                        "Eu gosto dela de verdade. Eu não tava com ela só pra curtir, tanto que passei várias coisas por ela."

                        "Mas agora tá bom. Eu não quero mais isso pra mim."



                        mc "Pri... eu prometi que ia ficar do seu lado. E eu vou."

                        c "Obrigada..."

                        mc "Mas eu não quero passar isso com você como namorados."

                        c "?!"

                        mc "Eu prometo que eu vou tá do seu lado. Mas eu quero ser só seu amigo."

                        c "[mc]... é verdade?"

                        mc "Eu quero ser o mais sincero possível com você."



                        scene pri8_img15 with Dissolve(1.0)

                        pause

                        c "Eu sabia que isso ia acontecer... eu puxei demais, né?"

                        mc "Você escolheu seu caminho. E eu quero escolher o meu também."

                        c "Isso dói muito, [mc]... meu coração tá ardendo... e eu tô sem ar..."

                        mc "..."

                        c "Você... já tem certeza disso? A gente não tem... nenhuma chance?"

                        mc "Eu juro que eu pensei. Eu gosto muito de você. Mas nossos objetivos não combinam como namorados."

                        mc "Se você quiser, eu posso ser seu amigo. Passar todas as dificuldades com você. Mas como amigo."

                        c "Obrigada... claro que eu quero..."
                    "Preciso pensar melhor.":


                        "Calma... tenho que pensar melhor."

                        jump p8_termina
            "Continuar namorando a [c].":


                "Desde que eu e a [c] começamos a namorar, muita coisa terrível aconteceu."

                "Eu apanhei, fui ameaçado de perder a vida, o emprego... foi tudo muito difícil."

                "A [c] é uma garota incrível, mas ela tá presa nessa vida. Ela é super fofa, muito gata, e ela se preocupa comigo."

                "Eu tinha esperança que a gente fosse ficar juntos... mas agora ela vai continuar nessa vida?"

                "Se eu for continuar com ela, eu preciso me preparar..."

                "Eu não sou um cafajeste de terminar com ela depois. Eu preciso me decidir sobre isso agora."

                "Vou falar na cara dela, ser sincero... a gente vai ficar juntos, mesmo que no fim eu acabe me ferrando."

                "Continuar namorando ela... é isso mesmo que eu quero?"

                menu:
                    "Sim. CONTINUAR com a [c].":


                        $ p8_terminou = False

                        "Eu não tenho dúvidas sobre isso. Eu quero ficar do lado dela. Como namorado."

                        mc "Se o que você decidiu é continuar por esse caminho. Eu vou tá do seu lado. A gente namora ou não?"
                    "Preciso pensar melhor.":


                        "Calma... tenho que pensar melhor."

                        jump p8_termina
    else:


        "Ela tá falando sério?"

        mc "[c]... você tem certeza disso?"

        c "Claro que eu não tenho certeza... mas é o que eu decidi."



        scene pri8_img15 with Dissolve(1.0)

        pause

    if not priscila_namoro:

        mc "Se o que você decidiu é continuar por esse caminho. Eu vou tá do seu lado como seu melhor amigo."

        mc "Eu prometo que eu não vou fugir."

    c "Muito obrigada... eu não sei o que eu ia fazer sem você, [mc]..."

    c "Eu tô tão triste com tudo isso... eu nem sei o que fazer..."

    mc "Eu prometo que a gente vai dar um jeito. Você vai conseguir ser a estrela que você quer."

    if priscila_namoro:

        mc "A gente precisa começar melhorando esse seu astral. Chega de ficar triste. Vem aqui."

        c "[mc]?"

        mc "Vem logo aqui."

        c "Opa."

        scene black with dissolve



        scene pri8_img16 with Dissolve(1.0)

        pause

        c "Que você tá fazendo, louco?"

        mc "Tô preparando você pro beijo."

        c "Vai todo mundo olhar pra cá, bobo."

        mc "Tô pouco me fodendo. Eu só quero olhar bem nos seus olhos."

        c "..."

        "A Pri só tem eu. A [a] só pensa nela. O [to] e o [gus] tão nem aí pra ela. Eles têm os objetivos dela."

        "A família dela parece que não tá nem aí."

        "Só sobrou eu. Só eu posso ajudar a Pri agora. Eu sou o último degrau antes dela cair no buraco."





        mc "Eu queria que você tivesse outras pessoas que se preocupassem com você de verdade..."

        c "Eu só tenho você, [mc]."

        mc "Se eu tivesse te conhecido antes de tudo isso... acho que tudo podia ter acontecido diferente, sabe?"

        c "Sei..."

        mc "Mas não importa. Eu vou ajudar você a realizar seus sonhos."

        c "E eu quero que você realize os seus. Eu vou te ajudar também."

        mc "Obrigado."

        c "Eu que tenho que a-"





        scene pri8_img17 with Dissolve(1.0)

        pause

        c "Hmmm!"

        "Espero que eu não acabe apanhando ou morrendo por causa desse beijo."

        c "Eu precisava disso, [mc]."

        mc "Ainda não acabou, gata."

        window hide

        pause





        "O cheiro da [c] é tão bom."

        "É um cheiro de emoção com desejo. Tudo é tão intenso com ela..."

        "Quando eu tô beijando ela parece que tudo vale à pena."

        "Mas uma coisa aqui dentro ainda diz que tudo vai acabar de forma terrível. Não sei o porquê..."







        c "[mc]... eu quero sentir você mais... me beija mais forte."

        mc "C-claro. Eu vou be-"

        "Homem" "EI! VOCÊS!"

        scene pri8_img18 with vpunch

        mc "A-ah!"

        c "Q-quê?!"

        "Homem" "O que vocês pensam que tão fazendo no meu bar?!"

        mc "D-desculpa, senhor."

        "Homem" "Nada de desculpa! Podem parando com isso aí! Vão pro motel seus descarados!"

        c "A-ai..."

        mc "A-acho melhor a ge-"

        c "C-claro. Eu vou só... é... retocar a maquiagem no banheiro e tamo indo."

        c "[mc].... você precisa ir no banheiro antes de sair também, né?"

        mc "E-eu?"

        c "Claro. Você... mora longe. Vê se passa lá no banheiro pra não... é... fazer xixi na viagem."

        mc "Pri..."

        c "Vai logo no banheiro!"

        mc "O-opa!"

        "Homem" "Façam logo o que têm que fazer e deem o fora!"

        scene black with dissolve

        scene p8_bar1 with dissolve













        "A Pri me chamou pra ir no banheiro... será que ela tá me chamando pra... sei lá..."

        "Será que eu vou atrás dela ou espero aqui? Talvez eu tenha entendido tudo errado. Eu sou meio safado então..."

        menu:
            "Ir atrás dela":


                "Bom... ela deu bem na cara que queria que eu fosse... tô achando que eu vou me dar bem..."

                "Pelo menos é o que eu espero..."

                "Deixa eu ir lá."

                scene black with dissolve

                "Banheiro... banheiro... aqui."

                "E-epa... parece que só tem um banheiro... e o sinal tá falando que tá desocupado... mas ela..."

                "Deixa eu ver..."

                mc desconfiado "O-oi?"

                c "Vem aqui!"

                mc surpreso "!!!"

                scene pri8_img19 with Dissolve(1.0)

                pause

                c "Que bom que você entendeu..."

                mc envergonhado "T-tá tudo bem?"

                c "[mc]... quando você disse que queria ficar comigo mesmo com tudo isso acontecendo... e me beijou..."

                c "Eu quero ficar com você... eu quero sentir que a gente tá mais perto do que nunca..."

                mc "Ok..."

                c "Olha aqui..."

                scene pri8_img20 with Dissolve(1.0)

                pause

                c "Eu quero que você aproveite tudinho disso aqui... tudo o que eu tenho pra você..."

                mc "Pr-Pri..."

                c "Você vai querer?"

                mc "E o dono do bar? Ele vai perceber que a gente tá aqui faz tempo."

                c "Você prefere agradar ele ou ficar comigo? Eu vou deixar você escolher..."

                "Eita... e agora? Eu vou ficar com ela pela primeira vez aqui nesse banheiro?"

                label pri8_premium2:

                    pass

                "Melhor guardar pra outro dia ou aproveitar a chance?"

                menu:
                    "Eu não vou perder essa chance.":


                        if not premium:

                            call mensagem_premium from _call_mensagem_premium_6

                            jump pri8_premium2

                        mc "Perder a chance de pegar a mulher mais linda da capital? Tá louca?"

                        c "Quando você fala assim de mim, eu tenho mais vontade de fazer ainda, [mc]."

                        c "Vem aqui e tira minha calcinha. Olha bem o que eu tenho pra você."

                        mc "Com certeza."

                        scene pri8_img21 with Dissolve(1.0)

                        pause

                        "Delícia..."

                        c "Ela tá te esperando..."

                        mc "Deixa eu aproveitar a vista um pouquinho."

                        c "Vai logo... o que você quer fazer com ela?"

                        c "Ah... sempre que a gente ficou junto, você cuidou de mim... dessa vez eu quero eu fazer você se sentir bem."

                        c "Deixa eu colocar seu pau na minha boca por favor. Eu prometo que eu vou fazer você gozar muito."

                        c "E aí?"

                        "Hmm... sentir a boca da Pri ia ser o sonho... mas eu posso agradar um pouco ela um pouco também. E aí?"

                        menu:
                            "Cuidar dela antes":


                                mc "Foda-se o dono, a gente não precisa correr, Pri."

                                c "Hm?"

                                mc "Já que você tá assim, deixa eu experimentar você um pouquinho."

                                c "Só que da outra vez..."

                                mc "Ninguém tá contando nada... deixa eu fazer você gozar antes, depois você faz comigo."

                                c "Ai, [mc]... eu já tô arrepiada só de pensar você no meio das minhas pernas."

                                mc "Então vem aqui."

                                scene black with dissolve

                                scene pri8_img22 with Dissolve(1.0)

                                pause

                                mc "Deixa eu sentir seu sabor de novo, sua gostosa."

                                c "Gostosa é sua língua na minha buceta... ghmmmm... ah..."

                                mc "Você é deliciosa."

                                c "Ain... assim... bem no fundo..."

                                c "Passa nela inteira... vai com calma... hmm.. ah..."

                                "Ela tá muito molhada, deve tá sendo bom."

                                c "Assim... continua!"

                                mc "Agora que você vai ver!"

                                scene pri8_img23 with vpunch

                                pause

                                c "A-ah!!"

                                mc "Hmm!"

                                c "Ai! Você tá me comendo com a boca, safado!"

                                mc "Geme gostoso!"

                                c "Ahn! Ghmm! Assim! Vai!"

                                c "{i}puf puf{/i}"

                                c "Aainnn! E-eu tô sentindo! M-mais forte!"

                                scene black with dissolve

                                scene ani01 with Dissolve(0.1)

                                pause

                                c "Ai meu Deus, que chupada! Aawwnn!"

                                mc "Minha princesa... hmmm... merece do melhor."

                                c "Se você tivesse... aah... terminado... hmm... você ia ficar sem essa xotinha!"

                                mc "A melhor xotinha do mundo."

                                c "Ela toda sua, meu homem."

                                mc "Só minha?"

                                c "V-você sabe que é só sua! Hnnnnng!"

                                c "A gente brinca... aahn... mas juro que é só sua..."

                                c "E ela tá guardada... pra você... aaah... pra quando você quiser comer."

                                mc "Eu SEMPRE quero comer."

                                c "Awnn... e você vai... aahn... p-prometo..."

                                c "Agora mama sua delícia, vai!"

                                mc "Nnghh!"

                                c "AAIINNN! Que boca! Devora meu suquinho, bebê! Vai, amorrr!"

                                c "Aainnnn!"

                                c "Aaaiinhngghh!"

                                scene pri8_img23 with hpunch

                                c "aAAAHHHH!"

                                "Uou... ela tá tremendo..."

                                c "Aainn... caramba... que delícia..."

                                c "Deixa... eu... pegar meu ar..."

                                scene black with dissolve

                                scene pri8_img21 with dissolve

                                c "Ufa... aah..."

                                c "Agora deixa eu cuidar de você? Tira a calça pra mim?"

                                jump pri8_premium_mc
                            "Tirar a calça e chamar ela":


                                label pri8_premium_mc:

                                    pass

                                mc "Eu vou aceitar seu carinho. Vem aqui."

                                c "Ai... era o que eu tava esperando..."

                                c "Se apoia aqui onde eu tô e deixa que eu cuido do resto, gostoso."

                                c "Finalmente eu vou sentir seu gosto, [mc]."

                                scene black with dissolve

                                scene ani14 with Dissolve(0.1)

                                pause

                                mc "Aagh..."

                                c "Hmnnng... que pau gostoso..."

                                mc "Vida... aah... como você mama... que delícia..."

                                c "Chupo gostoso, gato?"

                                mc "Demais... tá engolindo ele com uma vontade... nnghh..."

                                c "É de tanto... glup... que eu te amo..."

                                mc "Que chupada monstra, Pri... me suga gostoso, safada."

                                c "Sua puta sabe mamar o macho dela, é?"

                                mc "Demais! Qualquer um ia amar essa mamada!"

                                c "Hmmmm... se você diz..."

                                c "Falando assim você me dá mais vontade..."

                                scene black with dissolve

                                scene ani15 with Dissolve(0.1)

                                pause

                                mc "Ai, caralho... que especialista em chupada."

                                c "Eu sou a melhor em tudo... em oral também... hhmmm..."

                                c "Vai me dar todo o leitinho, vai? Leitinho de saco."

                                mc "Você quer?"

                                c "Me dá tudo! Alimenta sua cadela, alimenta!"

                                mc "Caralho, Pri... às vezes você pega fogo, porra."

                                c "Eu pego... eu fico toda molhada, meu amor!"

                                scene black with dissolve

                                scene pri8_img24 with Dissolve(1.0)

                                pause

                                "Caralho... eu tô nas nuvens..."

                                c "Hmm..."

                                c "Eu gostei dele..."

                                mc "A é?"

                                c "Sim... eu posso me divertir bastante aqui..."

                                "Tomara que o maldito do cara do bar não apareça agora."

                                mc "Pode se divertir..."

                                c "Tá gostoso pra você?"

                                mc "Claro... você é incrível, Pri."

                                c "Que bom... agora deixa eu chupar ele... ele tá pedindo..."

                                "Tá tão bom... não acredito que finalmente depois de tudo isso eu tô recebendo uma chupada dela..."

                                "A boca dela é tão gostosa..."

                                "Mas eu queria sentir mais... será que eu..."

                                menu:
                                    "Enfiar mais fundo":


                                        "Eu quero sentir a cabeça dela mais. Até o fim."

                                        mc "Pri... deixa eu enfiar mais..."

                                        c "Hm?"

                                        scene pri8_img25 with Dissolve(1.0)

                                        pause

                                        c "Hm!"

                                        mc "A-assim... ah..."

                                        c "{i}shlup{/i}"

                                        mc "Isso... chupa, gostosa..."

                                        "Eu não vou aguentar muito assim!"

                                        "E-eu quero mais rápido!"

                                        menu:
                                            "Meter na boca dela":


                                                "Eu não aguento, eu preciso mais disso!"

                                                "Eu vou meter na boca dela!"

                                                scene pri8_img26 with vpunch

                                                pause

                                                c "Hmm!"

                                                mc "Pri! Tá muito bom! Continua engolindo meu pau!"

                                                c "{i}cof{/i}"

                                                mc "S-só mais um pouco!"

                                                c "Nhhhg!"

                                                mc "T-tá quase!"

                                                mc "Eu vou gozar na sua boca, sua p-"

                                                scene pri8_img26 with hpunch

                                                "{i}BLANG BLANG{/i}"

                                                "Homem" "Vocês tão aí?! Saiam agora do meu bar antes que eu chame a polícia!"

                                                mc "M-merda!"

                                                c "[mc]! A gente tem que sair!"

                                                scene black with dissolve

                                                c "Eu vou pegar minha jaqueta. Me espera lá fora."

                                                mc preocupado "P-pode deixar."

                                                "Caraca..."

                                                "..."

                                                jump pri8_novidades_final
                                            "Deixar ela conduzir":


                                                "Ela tá incrível, eu não tenho que forçar mais nada."
                                    "Continuar aproveitando":


                                        "Só vou curtir... assim ela curte também..."

                                mc "Continua assim, Pri..."

                                c "Hmmm... você tá gostando mesmo, hein..."

                                mc "Muito... meu pau tá derretendo na sua boca..."

                                c "Deixa eu sentir mais ele."

                                mc "O-opa."

                                scene pri8_img26 with Dissolve(1.0)

                                pause

                                c "Hng!"

                                "Ela tá me pegando inteiro! Que delícia!"

                                c "Tchá buom, nhn?"

                                mc "Muito bom! Continua assim, Pri!"

                                c "{i}shlup{/i}"

                                mc "Ahnn! Nhg!"

                                mc "Assim! Vai!"

                                c "Hm! Anh!"

                                "Ela tá gemendo também!"

                                scene pri8_img27 with Dissolve(1.0)

                                pause

                                c "Hnm! Hmmmm!"

                                mc "M-mais! Hmmg!"

                                c "Hmmmmm!"

                                mc "Eu vou gozar na sua boca!"

                                mc "Aaahh!"

                                scene pri8_img27 with vpunch

                                c "Aahh!!"

                                mc "Q-que-{nw}"

                                "{i}BLANG BLANG{/i}"

                                "Homem" "Vocês tão aí?! Saiam agora do meu bar antes que eu chame a polícia!"

                                mc "M-merda!"

                                c "[mc]! A gente tem que sair!"

                                scene black with dissolve

                                c "Eu vou pegar minha jaqueta. Me espera lá fora."

                                mc preocupado "P-pode deixar."

                                "Caraca... Que delícia..."

                                "Acho que nós dois chegamos lá aquela hora..."

                                "..."

                                jump pri8_novidades_final
                    "Melhor a gente sair.":


                        mc envergonhado "V-você é maravilhosa, Pri... mas é melhor a gente deixar isso pra um momento melhor."

                        c "S-sério? A culpa... é comigo?"

                        mc "Claro que não. Você é perfeita e eu quero muito fazer isso com você, mas não aqui."

                        mc charmoso "Eu prefiro que seja uma coisa especial, em outro lugar."

                        c "Owwn... como você é romântico, [mc]. É por isso que eu te escolhi. Tudo bem..."

                        c "É uma pena que eu vou ficar com esse fogo... mas tá bom... é por uma boa causa..."

                        c "Eu vou lá pegar minha jaqueta e a gente já sai."

                        mc "Beleza."

                        "Espero que eu não me arrependa dessa..."

                        jump pri8_novidades_final
            "Esperar ela no salão":


                "Acho que só vou esperar ela aqui de boa."

                "..."

                c "[mc]! Por que você não foi comigo?!"

                mc envergonhado "N-não sei... eu..."

                c "Eu tava afim, seu zé ruela..."

                mc surpreso "A-ah!"

                c "Agora deixa pra lá... vou pegar minha jaqueta."

                mc envergonhado "O-ok..."

                "Que fora..."

        label pri8_novidades_final:

            pass

        scene black with dissolve

        scene pri8_img7 with Dissolve(1.0)

        c "Peguei minhas coisas. Tô pronta pra ir."

        mc "Beleza. Bora então."

        c "Ah."

        c "Obrigada de verdade por tá sempre comigo, [mc]. Se não fosse você eu não ia aguentar."

        mc "Você é mais forte do que você pensa."

        c "Eu sei! Rawarr!"

        mc normal "Haha... fofinha."

    c "Eu prometo que eu vou me esforçar pra tudo dar certo."

    c "E eu não quero ser egoísta, [mc]. Eu quero que você também seja feliz. E eu vou te ajudar também com qualquer coisa."

    c "Eu prometo que eu vou te ajudar igual você tá me ajudando."

    mc "A gente vai conseguir, Pri. A gente vai conseguir juntos."

    scene black with Dissolve(3.0)

    "..."

    scene mc_povo_noite with Dissolve(3.0)

    "Que dia... eu vou chegar em casa e jogar um pouco."

    "Eu ainda não entendi o que a [a] queria comigo na reunião. Mas agora eu tenho uma ideia muito melhor do que acontece."

    "Eles nunca vão parar. O [gus] nunca vai parar. Eles são gigantes, eles são pragmáticos e com certeza perigosos."

    "Tudo isso fez eu pensar na decisão mais importante da minha vida até aqui."

    if p7_gustav:

        "Eu decidi entregar o [gus] para a revista. Mexer nesse ninho de vespas e acabar com esse sistema que envolve tanta gente."

        "Foder a FAUX, o esquema do [to], ferrar o velho tarado, acabar com o sonho da [a] e de todas as garotas."
    else:


        "Eu tinha decidido não entregar o [gus]... eu não queria mexer com tudo isso e nem estragar o filme da [c]."

        "Mas agora eu sei que ele vai continuar fazendo isso pra sempre. Com a [c], com a [ta] e com quantas outras?"

        "Não entregar ele..."

    "Essa é a decisão que vai mudar minha vida pra sempre."

    label p8_decisao:

        "É isso mesmo que eu quero?"

    menu:
        "Denunciar o [gus] em uma matéria na revista":


            "Denunciar... é isso mesmo que eu vou fazer?"

            menu:
                "Sim. Vou denunciar o [gus].":


                    $ p7_gustav = True

                    mc charmoso "Não vou mudar de ideia. Eu vou explodir a porra toda."
                "Deixa eu pensar um pouco mais...":


                    "Calma. Vou pensar mais um pouco."

                    jump p8_decisao
        "Ignorar a matéria e deixar o [gus] impune":


            "Deixar tudo isso de lado? Ignorar tudo o que tá acontecendo e só ajudar eles com meu silêncio? É isso mesmo?"

            menu:
                "Vou ignorar a matéria e não mexer com o [gus].":


                    $ p7_gustav = False

                    mc desculpa "Não adianta querer comprar briga com quem eu não posso. O melhor é me aliar a eles."
                "Deixa eu pensar um pouco mais...":


                    "Calma. Vou pensar mais um pouco."

                    jump p8_decisao

    if not p7_gustav:

        "Vamos ver como isso vai acabar..."
    else:


        "Eu vou entregar ele. É o único jeito que eu vou conseguir dormir em paz."

        "Eu vou salvar a [ta], a [c] e até a [a]. Eu vou acabar com esse castelo de cartas que eles levantaram."

        scene black with Dissolve(3.0)

        "..."

        $ dia += 1
        $ tempo = 1

        scene trabalho chefe_porta with Dissolve(2.0)

        mc "Chefe. Posso entrar?"

        b "VAI LOGO!"

        scene chefe_sentado_pensando with Dissolve(1.0)

        b "O que foi?"

        mc serio "Eu ouvi seu conselho. Eu pensei muito e resolvi seguir com a matéria sobre o diretor [gus]."

        b "Então você realmente vai querer continuar com isso..."

        mc "Sim. Eu tô certo disso agora."

        b "Você sabe que... a gente nunca fez isso..."

        mc desconfiado "Nunca fez o quê?"

        b "Nossa revista é de fofoca, garoto. A gente fala sobre sexo e fuxico de pessoas famosas."

        mc envergonhado "O [gus] é famoso... e tem a ver com sexo..."

        b "Nem pense em brincar com isso, idiota. Você lembra das minhas condições, certo?"

        mc "Conseguir pelo menos duas testemunhas..."

        b "Exatamente. Você conseguiu?"

        mc "Ainda não, mas eu sei que eu consigo."

        b "Olha, filho. Eu não sei o que você tem dentro dessa cabecinha, mas deixa eu te explicar uma coisa."

        scene chefe_sentado_close with Dissolve(1.0)

        b "Depois que essa matéria for pro ar, o ministério público vai com tudo pra cima do diretor tarado."

        b "Eles vão ter que fazer alguma coisa. E não vai ser a cidade, não. Ele não vai ter a proteção do Donatello."

        mc normal "Isso é bom."

        b "Pode ou não. Se o [gus] se safar, ele vai vir pra cima de nós. Ele vai processar a revista e você vai foder a gente."

        b "'Mas eu tô pouco me fodendo pra revista', você pode tá pensando. Mas não é só isso. Ele vai pra cima de VOCÊ pessoalmente."

        b "E um homem desse tamanho, com a raiva que ele vai estar, só vai querer uma coisa de você. A sua cabeça."

        mc angustiado "..."

        b "Tem um ditado que diz 'Quando você ataca um dragão, tenha certeza de matá-lo, pois seu contraataque é mortal.'"

        b "Entende o que eu quero dizer? Se o [gus] for inocentado, você tá fodido. E se ele não te matar, EU VOU."

        b "Nós vamos publicar sua matéria e seu nome vai estar em destaque. Espero que você tome cuidado."

        b "Agora sai daqui antes que eu me irrite demais."

        mc angustiado "C-com licença."

        scene black with dissolve

        mc angustiado "O que eu fiz?"



    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v40_fim = True
    $ dia_priscila = dia + 3

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v40_fim","final","local")

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    jump call_cidade



label priscila_evento9:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("p9_save", extra_info="p9_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ priscila_e9 = "evento"

    $ p9_miranda_beijo = False
    $ p9_agata = False
    $ p9_juiza = False
    $ julgamento1 = ""
    $ julgamento2 = ""
    $ julgamento3 = ""
    $ p9_escolha = 0
    $ p9_priscila = False

    if p7_gustav:

        scene black with dissolve

        "..."

        mc desculpa "Então é isso."

        scene chefe_sentado_close with Dissolve(1.0)

        b "Então você decidiu continuar com isso. Essa sua cabecinha de vento não entende a merda que você tá fazendo."

        mc desculpa "Eu sei. Mas eu preciso parar isso. Ou pelo menos fazer alguma coisa."

        b "Você sabe que é seu nome que vai aparecer lá. Eles vão te enrabar."

        mc preocupado "A gente não tem certeza disso!"

        b "Eu tenho. Mas se você decidiu, eu vou permitir que a matéria seja publicada."

        mc "O-obrigado..."

        b "Você... garoto... você me lembrou do começo da minha carreira. Eu também queria usar o jornalismo pra fazer algo bom."

        mc normal "Que legal. E o que aconteceu?"

        b "O que você acha?! A realidade é uma bosta, idiota! O jornalismo não pode salvar o mundo! Ninguém pode! O mundo já deu errado!"

        mc desculpa "Parece que alguma coisa bem séria aconteceu..."

        b "Bah! Isso não interessa!"

        b "Você e essa cabecinha de criança ainda acham que podem fazer algo pelas pessoas. E você vai sofrer muito antes de chegar na minha conclusão."

        b "Aliás, espero que você chegue até o dia em que você se dê conta que tudo é inútil. É possível que você morra antes."

        menu:
            "Eu não vou morrer!":


                mc angustiado "E-eu não vou morrer!"

                b "Vamos esperar e ver, moleque... vamos esperar e ver..."

                mc "..."
            "Que seja...":


                mc zerado "Que seja..."

                b "Jovens têm esse jeito mesmo de não ligar pras coisas. A inconsequência é o combustível de quem ainda vai se foder muito."

        mc desconfiado "Mas e a matéria?"

        b "Não se preocupe. Ela já tá pronta."

        mc "Quê?!"

        b "Quando você trouxe a pauta nós já escrevemos uma nota citando o caso da [cc]."

        b "Eu só precisava saber se você ia ou não colocar o seu na reta para ser nomeado na matéria, pois quem escreveu não quis."

        mc preocupado "Entendi... então vai parecer que eu que fiz tudo."

        b "É. Desistiu?"

        menu:
            "Não. Vamos continuar.":


                mc charmoso "Que nada. Bora fazer isso de uma vez por todas."

                b "..."

                b "Certo."
            "Talvez seja melhor...":


                mc envergonhado "Pensando bem... talvez seja melhor e-eu-"

                b "Nem vem. Vê se vira homem, garoto!"

                mc angustiado "Mas-"

                b "Agora é tarde demais!"

                mc "Mas eu... tem razão..."

                mc concentrando "Eu resolvi que ia denunciar ele. Não posso dar pra trás agora."

                b "Hm..."

        b "Pode tirar o dia de folga hoje. Coma uma carne bem cara. Aproveite as luzes da noite e se prepare."

        mc angustiado "Por que você tá falando como se fosse meu último dia?!"

        b "E agora dá o fora daqui que eu vou ter que garantir que essa matéria saia no site com o BANG! que ela precisa."

        b "E não abre o bico pra ninguém, ouviu? Não quero que a [j] saiba nada sobre isso."

        mc desculpa "Ok. Até mais, chefe."

        b "Xô."
    else:


        "Pensando bem... acho que eu vou ficar em casa o dia inteiro hoje. Eu preciso de um descanso também..."

    scene black with dissolve

    $ tempo = 3

    "..."

    if casa:

        scene ap mc_assistindo with Dissolve(1.0)
    else:


        scene apartamento tv with Dissolve(1.0)

    pause

    mc "Cansei de Netflix. Parece que agora eles só colocam coisa original. Esse povo falando em tudo que é língua estranha."

    mc "Gastando milhões pra fazer essas séries bosta e até agora não colocaram Chaves."

    mc "Deixa eu ver o que tá rolando na TV."

    "Vinheta" "{b}Faux News: Nós somos a Verdade{/b}"

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    scene tv apresentador with Dissolve(1.0)

    "Apresentador" "Boa noite. Hoje iniciamos o noticiário com um acontecimento estarrecedor."

    "Acabou de começar o jornal."

    "Apresentador" "O site de uma revista de grande renome na capital diz ter informações sobre um suposto crime cometido por um diretor de cinema."

    "Apresentador" "Segundo a reportagem, o diretor Gustav Aldebaran estaria abusando de atrizes durante a filmagem de suas obras."

    "Apresentador" "O mais recente acontecimento teria ocorrido com a atriz [cc], protagonista do filme que estreará nas próximas semanas."

    "Apresentador" "A reportagem não traz nenhum depoimento ou qualquer prova, mas garante que recebeu a confirmação de pessoas envolvidas."

    "Apresentador" "As fontes para a notícia não quiseram se identificar, e a revista se diz comprometida a respeitar o desejo das fontes."

    if p7_gustav:

        "Então a notícia saiu... e a Faux já repercutindo..."

        "Apresentador" "A matéria foi assainada pelo jornalista, [mcc]."

        "Caralho... agora todo mundo sabe que sou eu..."

        "Apresentador" "Esse nome tem aparecido em outras revelações feitas pela mesma revista nos últimos tempos."

        "Parece que meu trabalho tá dando resultado..."
    else:


        "Quê?! Como assim a revista publicou isso?!"

        "Eu decidi não confirmar com o chefe! Por quê ele faria isso?! C-como ele sabe disso?!"

    "Apresentador" "Nossa equipe contatou o diretor, que negou as acusações. [gus] classificou a matéria como sensacionalismo barato."

    "Apresentador" "O diretor afirmou estar sendo alvo de fake news devido ao lançamento do seu próximo filme."

    "Apresentador" "Nas redes sociais, entretanto, o público parece ter aceitado a denúncia como verdade e a repercussão tem sido imensa."

    "Apresentador" "Juristas entrevistados acreditam que a denúncia, mesmo fraca, pode gerar uma investigação por parte do ministério público."

    "Apresentador" "A denúncia seria motivada, principalmente, por se tratar de figura pública de grande influencia."

    "Apresentador" "Mesmo acreditando não passar de sensacionalismo barato, a Faux News continuará noticiando os desdobramentos."

    "Apresentador" "E agora, uma mensagem de nossos patrocinadores. Voltamos em breve."

    "Vinheta" "{b}Faux News: Nós somos a Verdade{/b}"

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    if casa:

        scene ap mc_cel with Dissolve(1.0)
    else:


        scene mc ap_pensando with Dissolve(1.0)

    "Chance de ir pra Justiça... Pode ser que o [gus] acabe indo pra julgamento."

    "O chefe disse que eu vou precisar de pelo menos duas pessoas que confirmem o que ele fez. Que só a [c] não ia ser suficiente."

    "Da outra vez que a gente se viu, ela disse que ia aceitar fazer outro filme com ele..."

    "Eu fico maluco pensando que ela vai aceitar passar por tudo aquilo de novo... da outra vez ela tava tão triste..."

    menu:
        "Ela não quer jogar tudo fora...":


            mc "Acho que ela só não quer jogar fora tudo o que ela fez até agora."

            "Ela conquistou um espaço no cinema estreando um filme. Vai saber quando ela vai ter outra oportunidade de tá por cima desse jeito."

            "Ela precisa colher o máximo de frutos que ela pode antes que a fama dela desapareça."

            "Eu sei que essas coisas mudam rápido. Um dia um cantor tá com tudo, ano que vem a gente nem escuta mais nada dele."

            "Se ela não aproveitar o momento dela, talvez ela nunca consiga outra chance. Acho que eu entendo isso..."
        "Ela se vendeu pela fama...":


            "Ela já conquistou o topo. Ela fez o filme, virou uma celebridade como nenhuma outra, e mesmo assim não é o suficiente?"

            "Eu acho que ela bebeu dessa água e agora não consegue mais parar. Nada mais vai ser suficiente."

            "A [c] sempre foi uma moça super meiga, talvez uma das pessoas mais amáveis que eu conheci aqui, mas esse lado dela pode dar problema..."

    "Mas, de um jeito ou de outro, eu não posso julgar ela. Ela fez a escolha que ela quis, assim como eu tenho feito as minhas."

    "Cada um vai colher o que plantou e eu espero que ela seja feliz, de um jeito ou de outro."

    if priscila_namoro:

        "A gente tá namorando e eu pretendo continuar firme com ela até o fim."
    else:


        "Eu sou o melhor amigo dela. Ela já falou isso várias vezes."

    "E por isso eu só posso torcer pra que tudo dê certo no fim."

    "Eu não sei o que esse julgamento do [gus] vai fazer com ela, com a carreira e tal... mas eu torço pra que isso acabe sendo bom."

    "Eu queria tanto poder falar com ela agora. Saber o que ela tá sentindo..."

    if priscila_namoro:

        "Eu quero ser o cavaleiro dela. Alguém que vai tirar ela desse buraco e deixar ela a salvo."

    "A [c] me salvou de ser demitido e eu aposto que ela faria a mesma coisa por mim."

    "Eu preciso garantir que o [gus] seja preso. Impedir que esse porco continue fazendo isso que ele fez com tantas garotas inocentes."

    "Ver ele atrás das grades vai ser incrível. Aquela cara de idiota dele chorando com roupa de presidiário."

    "Eu preciso torcer pra que ele realmente seja indiciado. E daí as garotas que foram vítimas dele precisam falar a verdade."

    "A Ágata, a [c] e a até a Tatá, que tava aquele dia na reunião. Eles queriam fazer a mesma coisa com ela. Até ela podia ajudar."

    scene ape_cama with Dissolve(1.0)

    "Olha a hora... minha cabeça tá a milhão. Eu preciso descansar e esperar..."

    "E torcer pra que tudo isso não acabe me fodendo..."

    scene black with dissolve

    "Eu sinto que as coisas tão se movendo... e logo a gente vai chegar no fim disso tudo."

    "Eu só quero que se alguém tiver que se ferrar nisso, que seja o [gus], não eu, nem a Pri e nem ninguém..."

    "..."

    if not v52_fim:

        "{b}Continue jogando CH para habilitar a continuação da história da [c]{/b}"

        "{b}Para liberar o próximo evento, você deve conhecer a Nona e chegar até o final do terceiro evento com ela{/b}"

        "{b}Para conhecer a Nona, você deve encontrar a Sofia e seguir a história com ela até ter o celular hackeado{/b}"

        "{b}Suas decisões nos vários eventos do jogo vão decidir o final de sua jornada. Boa sorte vivendo na ilha das celebridades!{/b}"

        $ tempo = 4

        jump call_cidade
    else:


        $ dia += 7
        $ tempo = 1

        jump priscila_e9_miranda

label priscila_e9_miranda:

    $ priscila_e9 = "miranda"

    "Uaaah... mais um dia!"

    "Falando em mais um dia..."

    "Ainda não saiu nada sobre o [gus]... eu sinto que passou tanto tempo."

    if not p7_gustav:

        "Aliás... se eu não denunciei o velho... quem será que assinou a matéria? Eu deixei a pauta com o chefe, mas ele não ia publicar no nome dele."

        "Quem assumiu esse B.O. tá fodido. Não quero nem pensar o que o [gus] vai fazer quando ele pegar quem denunciou ele."

        "Vou dar um pulo na redação e ver quem que ficou com a bucha..."

        scene black with dissolve

        "..."




        scene trabalho angulo with Dissolve(1.0)

        pause

        "Pensando agora... eu podia só ter lido a matéria no site pra saber quem assinou... que idiota."

        "Mas já eu tô aqui."

        mc normal "Ei. [w]. Tá ocupada?"

        w "[mc]?"

        scene so5_img11 with Dissolve(1.0)

        w "Que foi?"

        mc normal "Ah. Eu vi no jornal de ontem a Faux falando sobre a matéria do diretor Gustav Aldebaran."

        w "Sim. Eu tava na sala do meu pai e eu vi a pauta lá em cima. Parabéns pela informação."

        mc "Valeu. Eu decidi não dar prosseguimento na matéria..."

        w "Foi o que eu pensei mesmo. Ela ficou lá um tempo..."

        mc envergonhado "Pois é. Daí eu queria saber... Quem é que escreveu?"

        w "Eu passei pro Ronaldo. Você e ele são os únicos que eu confio aqui."

        mc desculpa "Então vai sair no nome dele..."

        w "Não. Na verdade vai sair no meu nome."

        mc surpreso "C-como é?!"

        scene so5_img10 with Dissolve(1.0)

        w "Eu achei injusto pedir pra ele assumir o risco. Uma matéria dessa aí pode dar problema na carreira."

        mc "Eu sei... mas por que você?"

        w "Eu tenho uma posição bem confortável aqui, [mc]. Não é como meu pai fosse me demitir por causa disso."

        w "Agora, se o Ronaldo sair daqui e for pra outra empresa, ele pode sofrer retaliação se o diretor resolver ferrar ele."

        mc "Isso é perigoso, [w]..."

        w "Você parece preocupado demais, [mc]."

        menu:
            "Acho que eu tô exagerando mesmo...":


                mc "Acho que eu tô exagerando mesmo... eles não vão fazer nada muito grave..."

                w "Isso aqui não é filme. Não é como se o diretor fosse matar o responsável pela matéria."

                mc "É... acho que você razão... tomara..."
            "Eles podem fazer mais que ferrar uma carreira.":


                mc "Você não tá entendendo, [w]. Eles podem fazer mais que ferrar sua carreira. Eles podem te fazer mal de verdade."

                w "Eu agradeço, mas acho que você tá exagerando. Deve tá assistindo filme demais."

                mc "Eu sei por experiência própria. Eles são loucos, [w]. Ameaçar a vida de alguém não é nada pra eles."

                w "Você tá parecendo meio louco agora. Eu já entendi. Você tem medo deles. Mas eu não. Eles que venham me pegar."

        mc "[w]..."

        "Eu não acredito que ela colocou o nome dela na matéria..."

        if sofia_namoro:

            "E justo agora que a gente tá namorando... se o [gus] se vingar... não quero nem pensar no que ele vai fazer com ela."

        w "Agora dá licença que eu tenho mais coisas pra fazer, [mc]. A gente se fala depois."

        mc "Ok..."

        scene trabalho angulo with Dissolve(1.0)

        "Que saco... a [w] tá correndo risco e nem sabe."

        "Eu preciso garantir que o [gus] seja preso. Ele precisa ir pra cadeia antes de ter chance de fazer alguma coisa com ela."

        "E nem assim dá pra garantir que ele vai perdoar ela... ou será que é melhor que ele se livre? Talvez ele se irrite mesmo."

        "Merda. De um jeito ou de outro a [w] pode se ferrar muito."

        menu:
            "Eu preciso ajudar a [w].":


                "Eu tenho que ajudar ela. Eu não posso deixar nada de ruim acontecer com ela."

                "Eu sei do que o [gus] e o Marco são capazes. Eles me ameaçaram na cara dura no viaduto aquela vez."

                "Se eu deixar a [w] sozinha na mão deles, ela vai acabar... não quero nem pensar nisso."
            "Essa pica não é minha. Ela que se vire.":


                "Eu sei que é triste, mas eu não tenho nada a ver com a [w]. Eu já não entreguei a pauta pra não correr risco."

                "Se eu me meter nessa por ela, eu vou acabar na vala do mesmo jeito. E eu não quero isso."

                "Espero que tudo acabe bem pra ela..."

        "Deixa eu voltar pra casa."

        "..."

    scene black with dissolve

    scene ape_tv with Dissolve(1.0)

    pause

    "Faz mó tempo que a notícia do abuso dele saiu. A Faux falou no dia, mas não saiu mais nada depois."

    "O chefe tinha certeza que o ministério público não ia ignorar isso. E a própria Faux disse que pela fama do [gus] eles podiam fazer algo."

    "E agora nada acontece? Que porra é essa?! O [gus] é um sacana! Ele precisa encarar a Justiça!"

    "Ele precis-{nw}"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr... trrrr..."

    "Uou! Que susto!"

    "Esse telefone... é a [a]."

    scene ape_celular_falando with Dissolve(1.0)

    mc "Alô? [a]?"

    a "Boa noite, [mc]. Parece que você não excluiu meu contato ainda."

    menu:
        "Acho que eu devia ter excluído...":


            mc "Agora que você falou, é verdade. Eu devia ter excluído você mesmo."

            a "Espera... eu sei que você não concorda com as coisas, mas você precisa escutar o meu lado."

            mc "Acho que eu já escutei você demais."

            a "Não escutou."
        "Por que eu faria isso?":


            mc "Por que eu ia querer excluir seu contato? Eu gosto de falar com você."

            a "Você sabe... nosso último encontro na reunião. Não senti que você ficou à vontade com tudo."

            mc "Eu não fiquei mesmo, mas não coloco a culpa em você. Eu sei que você quer ajudar elas."

            a "Obrigada."

    a "Eu preciso falar uma coisa muito importante com você."

    mc "Tem a ver com a matéria sobre o [gus]."

    a "Sim..."

    if p7_gustav:

        mc "Você sabe que fui eu que denunciei ele, né?"

        a "Eu sei. Eu sabia que cedo ou tarde você ia acabar fazendo essa loucura."
    else:


        mc "Mas não fui eu que escrevi a matéria. Você não leu?"

        a "Eu li... mas eu sei que você que tinha as informações."

        mc "Não tem como você ter certeza disso."

        a "Mas eu tenho. Só você conhecia a [c] suficiente pra tirar isso dela."

        mc "Acho que faz sentido..."

    a "Será que a gente pode conversar?"

    "A [a] tá no meio de todo esse rolo com o [gus]. Certeza que ela pode até acabar como cúmplice."

    "Ela levou a [c] pra ele, ela instigou ela a aceitar o papel. Ainda não esqueço daquele primeiro e-mail que eu li no celular da Pri."

    "Aquele e-mail que me deu a primeira pauta da minha vida... era a [a] falando que essas coisas eram 'normais'."

    "E se tivesse um jeito de eu convencer ela a entregar o [gus]? Será que eu tô sonhando demais?"

    "Eu devo falar com ela? E se ela acabar me arrastando pro buraco com ela e o tarado?"

    menu:
        "Tudo bem. A gente pode se encontrar.":


            $ miranda_seducao += 1

            mc "Tá legal. A gente pode se ver. Você quer conversar hoje?"

            a "Que bom! Eu tava com medo que você fosse negar. Obrigada."

            a "O que você acha da gente se encontrar no mesmo bar aí na ilha. O bar que conversamos da primeira vez."

            mc "Ah. O bar do [gar]. Tudo bem."

            a "Perfeito. Nos encontramos lá então em uma hora."

            mc "Sério que você consegue se arrumar e chegar aqui em uma hora?"

            a "Eu não pego ônibus, [mc]. Essa é a diferença."

            mc "Ah... verdade... eu nunca pensei que existia outra possibilidade..."

            a "Conversamos mais no bar. Até logo."
        "O que você quer falar?":


            mc "Pra que você quer conversar? Não pode ser por telefone?"

            a "Não posso. É um assunto sério. Não posso correr o risco de você gravar."

            mc "Só de falar isso você já tá meio que se entregando, né?"

            a "Eu não estou brincando. Eu prometo que vai ser rápido."

            menu:
                "Ok. A gente pode conversar.":


                    mc "Se é assim... tudo bem. Pode contar comigo."

                    a "Que bom! Eu tava com medo que você fosse negar. Obrigada."

                    a "O que você acha da gente se encontrar no mesmo bar aí na ilha. O bar que conversamos da primeira vez."

                    mc "Ah. O bar do [gar]. Tudo bem."

                    a "Perfeito. Nos encontramos lá então em uma hora."

                    mc "Sério que você consegue se arrumar e chegar aqui em uma hora?"

                    a "Eu não pego ônibus, [mc]. Essa é a diferença."

                    mc "Ah... verdade... eu nunca pensei que existia outra possibilidade..."

                    a "Conversamos mais no bar. Até logo."
                "Eu não tenho o que conversar com você.":


                    mc "Desculpa, [a], mas eu não tenho nada pra conversar com você."

                    a "Eu garanto que vai ser uma coisa do seu interesse também."

                    mc "Duvido. Meu interesse é não ter nada a ver com você e com o velho tarado. Espero que vocês dois se ferrem."

                    a "[mc]... você não tá sendo razoável."

                    mc "Você não foi nem um pouco razoável coloca a Pri e agora a Tatá nessa situação. Você é tão porca quanto eles."

                    a "Eu não vou ficar ouvindo você me difamando desse jeito."

                    mc "Falou tudo. Tenha uma boa vida."

                    "{i}Ti{/i}"

                    "Desliguei na cara mesmo. Essa mulher não merece minha atenção."

                    "Eu vou é dormir e esperar uma notícia sobre o [gus] indo pra julgamento. É só o que eu quero agora."

                    scene black with dissolve

                    "..."

                    jump priscila_e9_agata

    "Espero que me encontrar com ela seja a melhor escolha..."

    "Eu queria mesmo era falar com a [c]... Mas sei lá, eu ainda não tive coragem de tocar nesse assunto com ela."

    "Depois eu penso nisso. Melhor eu me preparar e descer."

    scene black with dissolve

    "..."

    scene pub booth with Dissolve(1.0)

    "Eu enrolei um pouco, mas acho que acabei chegando cedo demais..."

    "???" "[mc]! Aqui!"

    mc desconfiado "Hm?"

    scene p9_img1 with Dissolve(1.0)

    pause

    mc charmoso "Você já chegou."

    a "Acho que eu tô um pouco ansiosa. Toda essa situação tá me deixando desse jeito. Queria muito falar com você."

    menu:
        "Calma. Eu quero ajudar você.":


            $ miranda_seducao += 1

            mc charmoso "Não precisa falar desse jeito. Eu vou ajudar você no que eu puder."

            a "Eu preciso mesmo de uma palavra amiga agora... Mas eu não esperava que fosse ouvir de você."

            mc "Eu não posso ver uma mulher bonita com essa cara de preocupada. Deve ser algum instinto."
        "Você? Vulnerável desse jeito?":


            mc envergonhado "Esse jeito vulnerável não combina com você."

            a "Eu não tô brincando. Eu não tô dormindo esses últimos tempos. É sério."

            mc serio "Hm..."

    "Parece que ela tá bem preocupada mesmo. Das outras vezes a [a] sempre parecia mais posuda."

    mc serio "Eu pensei que as coisas fossem ficar complicadas pra você e pra Pri depois da matéria, mas eu não vi nenhuma repercussão."

    a "A Faux deu a notícia no principal jornal deles na mesma noite."

    mc "Eu sei, só que... depois disso não teve mais nada."

    a "São coisas diferentes. Você pode não ter visto, mas as coisas aconteceram."

    mc desconfiado "Verdade? Tipo o quê?"

    a "É sobre isso que eu queria conversar com você. Por isso eu te chamei."

    mc "Certo..."

    a "E se a gente sentasse aqui no fundo hoje? Um pouco mais de privacidade seria bom."

    menu:
        "Só nós dois nesse cantinho mais escuro...":


            $ miranda_seducao += 1

            mc tarado "Só eu você nesse cantinho escuro do bar? Qual é sua intenção, hein, [a]?"

            a "[mc]... nunca perde uma chance de levar a conversa pra esse lado."

            mc charmoso "Não quando eu estou com uma mulher igual você. Só um idiota ia perder, concorda?"

            a "Faria mais sentido flertar se a situação não fosse essa que a gente tá."

            mc "Eu sei, mas um pouquinho ainda é melhor do que nada."

            a "Só não vai ficar triste se seu esforço não der em nada."
        "A gente vai poder conversar melhor.":


            mc normal "Tem razão. Acho que a gente vai conversar melhor aqui."

            a "Sim. É um assunto delicado e é perigoso se os ouvidos errados ouvirem."

    a "Vem. Eu tava sentada nessa mesa aqui."

    mc "Opa."

    scene p9_img2 with Dissolve(1.0)

    pause

    mc "E então? O que era tão importante conversar?"

    if p7_gustav:

        a "A matéria que você publicou acabou mexendo com muita gente. Não só o [gus]."
    else:


        a "A matéria que aquela [w] publicou acabou mexendo com muita gente. Não só o [gus]."

    mc "Eu sei quem essa 'gente' é. Não precisa falar assim. Eu sei que o [to] e o prefeito contam com o velho também."

    a "Você fala isso de um jeito casual demais, [mc]. Você sabe o poder dessas pessoas."

    mc "Eu tô ligado que eles controlam a cidade. Eu não sou mais aquele recém-formado que não sabia nada da cidade grande."

    mc "Mas eu sei também que a situação deles não tá normal."

    a "O que você quer dizer?"

    mc "Tem gente querendo a cabeça deles. Tem gente querendo acabar com essa festa."

    a "Eu não sei do que você tá falando."

    mc "Como não sabe?"

    a "Parece que você sabe mais desse mundo do que eu."

    menu:
        "Acho que você quer me fazer de bobo.":


            mc "Acho que você só tá querendo se fazer de idiota, isso sim."

            a "Quem dera..."

            mc "Eu sempre achei que você tivesse com eles."

            a "Hm..."
        "Você realmente não sabe?":


            $ miranda_seducao += 1

            mc "Você não sabe? De verdade? Não sabe com quem você tá mexendo esse tempo todo?"

            a "Falando assim eu pareço uma idiota... eu sei."

            mc "Não é isso... eu pensei que você fizesse parte disso tudo. Foi o que eu sempre achei pelo menos."

            a "Não é bem assim..."

    a "Não adianta mais ficar de mistério. Você já sabe tudo o que tá acontecendo. Talvez seja melhor eu só falar de uma vez."

    a "Quero dizer... se você quiser ouvir."

    menu:
        "Claro. Eu preciso entender isso.":


            $ miranda_seducao += 2

            mc "Com certeza. Eu quero entender seu papel nisso tudo."

            a "Acho que é até bem simples entender meu 'papel'..."

            a "Eu vou ser sincera. Eu sei que o que eu fiz não foi ético. Qualquer pessoa razoável iria concordar com isso."

            a "Quando eu trouxe a [c] pra cá e ofereceram esse papel pra ela, com a condição que ela se tornaria a bonequinha do [gus]..."

            mc "..."

            a "Eu sei... qualquer pessoa que quisesse fazer o 'certo' teria negado. Eu sei. Mas nem sempre o 'certo' é o certo."

            mc "Eu não sou um padre, [a]. Eu não tô aqui pra você se confessar. Eu quero que você me explique os fatos."

            a "Ok... é que é fácil me ver como um monstro que fez a [c] se vender por fama e dinheiro. Mas só eu entendo as minhas razões."

            mc "Eu prometo que eu não vou te julgar antes da hora. Mas eu não quero que você tente me manipular. Eu sou grandinho, posso escolher por mim mesmo."

            a "Justo."

            a "Quando eu digo que eu não sei o que tá acontecendo com esse grupo do [to], é porque eu realmente não sei. Eu não faço parte."

            a "A verdade é que eu quero entrar no grupo deles, mas até agora ninguém permitiu."

            a "Eles continuam me enrolando, dizendo que eu tenho que provar minha utilidade e lealdade."

            mc "Tipo o caso da [c]? Você trouxe ela pra-"

            a "Mais ou menos. O caso dela foi o meu primeiro. Eu ainda não tinha nenhuma pretensão desse tipo. Eu só queria uma boa vida pra gente."

            a "Quando descobriram ela naquelas audições de modelos, eu vim até a capital pra conversar com o [to]."

            a "Ele só me disse que tinham gostado muito dela. Ela era linda, mas o mais importante é que ela era inocente e carismática."

            a "Eles só precisavam que eu apoiasse ela, porque não ia ser uma vida fácil."

            mc "Então eles conhecem a [c] desde antes daquela reunião que você e ela fecharam com o [gus]?"

            a "Claro. Eles construíram a [c] desde o começo."

            mc "Não acredito..."

            scene p9_img3 with Dissolve(1.0)

            pause

            a "Todos os contratos... a exposição... tudo que a [c] conquistou foi dado por eles."

            mc surpreso "Tudo?!"

            a "Você acha que alguém consegue se tornar mais conhecida que Jesus em pouco mais de um ano?"

            a "Eles investiram milhões na carreira dela. Eles construíram o que a [c] é. Sem o [to], ela estaria, posando pra catálogo de roupa."

            mc desculpa "Então foi assim que ela cresceu..."

            a "Ela não cresceu. Ela explodiu. Foi a carreira mais meteórica da história do país e talvez do mundo."

            a "O filme com o [gus] é só mais um fruto dessa árvore chamada [c]. Eles vão usar ela o máximo que puderem, até ela secar."

            a "Quando ela parar de dar ibope, eles vão jogar ela fora, e eles já estão começando a preparar uma nova pra tomar o lugar."

            mc "A Tatá."

            a "Sim."

            mc "Que você também trouxe."

            a "Se a Tatá virar, ela vai ser meu ingresso para o grupo. Vou me tornar a caça talentos oficial deles. E vou estar garantida pra sempre."

            mc "E a [c]? Como fica?"
        "Acho que não é necessário.":


            mc "Eu acho que não preciso saber disso agora. A gente tem que falar sobre o [gus]."

            scene p9_img3 with Dissolve(1.0)

            pause

            a "Tem razão. Eu não sou a estrela do momento, certo?"

            mc envergonhado "Haha... acho que eu tô um pouco ansioso com tudo isso. Desculpa."

            a "Mesmo quando você corta uma pessoa, você continua sendo fofo."

            mc "Haha..."

            a "Quem importa aqui é a [c]."

            mc normal "Concordo."

    a "Ela não tem quase nenhuma segurança. Se alguma coisa acontecer com o acordo entre ela e os contratantes, ela vai ficar pobre em um ou dois anos."

    mc preocupado "Como assim?! Ela não é rica?!"

    a "Longe disso. A maioria do dinheiro que ela recebe fica com as marcas e com os empregadores dela."

    a "Claro que ela recebe um bom salário e pode ter uma boa vida. Mas é diferente de estar garantida pra vida."

    a "Sem uma nova fonte de renda... logo ela vai estar em necessidade de novo."

    mc "Mas e o filme? Ela é a protagonista de uma mega produção!"

    a "E daí? A vantagem de levantar a carreira de alguém do zero é justamente colher os frutos depois."

    a "Eles não tão pagando nada praticamente pra ela pelo papel. E ela não pode nem recusar... pois tudo está previsto no contrato inicial."

    mc desculpa "Você quer dizer que... desde quando eles contrataram ela, eles já tinham planejado tudo isso."

    a "Claro. Nem todas as garotas dão certo como a [c], então eles fazem isso com várias. A maioria volta pra casa em dois ou três meses."

    mc "E mesmo sabendo de tudo isso, se elas não aceitam, nada acontece..."

    a "Sim. Quem tem o poder dá as cartas. Nesse caso, é o [to]."

    mc "Sei..."

    a "E é por isso tudo que eu preciso de você."

    mc desconfiado "Precisa de mim pra quê?"

    a "Agora que sua revista publicou a matéria, eu preciso que você garanta que nem a [c] e nem outras pessoas denunciem o diretor [gus]."

    mc bravo "Você tá falando sério?"

    a "A [c] não pode acabar sem nada. Ela passou por muita coisa. Mais do que uma garota dela deveria. Ela merece viver feliz, não acha?"

    mc desculpa "[a]..."

    a "Por favor. Pense no futuro dela."

    "Ignorar o que o [gus] fez com ela e ajudar ele a se dar bem? Essa mulher tá louca?"

    "Ou... será que eu tô ignorando a Pri? Eu tô colocando meu ódio e minha vingança na frente dela?"

    if p7_gustav:

        "Eu resolvi entregar o bosta do velho pra acabar com tudo isso."
    else:


        "Eu decidi não entregar ele pro chefe... então será que é tão ruim assim deixar ele escapar pela [c]?"

    "Eu sinto que o que eu responder agora vai mudar muita coisa... tenho que pensar bem..."

    "O que eu falo pra ela?"

    menu:
        "Nós não podemos deixar ele escapar.":


            "De jeito nenhum eu deixo esse picareta escapar. A [a] deve tá louca."

            scene p9_img7 with Dissolve(1.0)

            mc "Sem chances. Nem por você, nem pela [c]. Esse cara vai pagar por ser um tarado abusador."

            mc "Você mesmo me explicou. Era isso ou a Pri ia voltar pro nada. Aceitar o velho ou voltar a ser uma garota sem porra alguma."

            mc "E você também não queria isso. Perder sua chance de ser alguém. Ele estragou tudo. Ele fodeu vocês duas."

            mc "E eu não vou deixar isso, [a]. Se eu tiver uma oportunidade que seja de acabar com esse velho, pode ter certeza que eu vou."

            a "[mc]... Não tem nada que eu diga que pode fazer você mudar de ideia?"

            mc "Impossível. Eu tenho certeza do que eu quero fazer."

            if p7_gustav:

                mc "Eu resolvi publicar a matéria pra isso. Mesmo sabendo dos riscos, eu tô nem aí. Eu quero ver ele pagando."
            else:


                mc "Eu não publiquei a matéria, mas você sabe que fui eu que dei as informações. E foi pra foder ele mesmo."

            mc "E se eu fosse você, eu faria a mesma coisa."

            a "E jogar fora tudo o que eu conquistei nesse tempo? Você tá louco. Eu não ligo pra sua moral ou o que é 'certo' pros outros."

            a "Eu vou fazer o que eu achar que é o melhor pra mim e pras minhas garotas."

            menu:
                "Eu sei. Você faz o seu melhor.":


                    $ p9_miranda = 1

                    mc "Eu sei. Você faz o seu melhor, [a]. Você quer uma vida melhor pra você e pra elas."

                    mc "E parece que você coloca seus próprios valores de lado pra garantir que você consiga."

                    mc "Você sem dúvidas é uma mulher obstinada e corajosa. Nem todo mundo teria a coragem que você tem."

                    a "..."

                    mc "Agora, a questão é que talvez falte pra você conseguir olhar o outro lado."

                    mc "Eu sinto que sua diferença pra outra mulher obstinada que eu conheço da redação é justamente essa."

                    mc "Ela faz tudo pra ter poder pra ela. Já você é uma excelente profissional, querendo uma vida melhor pra você e suas protegidas."

                    mc "Só que tem uma coisa aí... Uma mulher pragmática igual você talvez não entenda que ter uma vida humilde não é o pior."

                    mc "Ter um coração machucado, com medo, sozinho... essa é a pior coisa do mundo. Esse buraco dentro da gente é horrível."

                    mc "E você viu como a Pri tava até um tempo atrás. Ela tava prestes a acabar tudo. E o dinheiro e a fama não iam ajudar ela."

                    a "Eu sei... mas..."

                    mc "Eu quero que você pense. Pense no que você pode fazer por elas. Mostrar pra elas que o [gus] não domina a vida delas."

                    mc "Que ele pode cair. Que ele é só um velho estuprador que marece apodrecer na cadeia. Você vai libertar tantas garotas."

                    mc "Só pensa nisso. E vamos torcer pra que a Justiça faça alguma coisa."

                    a "Você realmente falou tudo o que queria, hein?"

                    mc "Desculpa... acho que eu me empolguei."

                    a "Obrigada por me ouvir hoje. Agora eu tenho que ir."

                    mc "O-ok. Até mais."

                    a "..."
                "Você é igual a eles. Pense nisso.":


                    mc "O que parece pra mim é que você igual a eles. Você só quer dinheiro e fama em troca das outras pessoas."

                    mc "E sei que você pode se enganar dizendo que tá ajudando elas, mas você só quer ajudar você mesma."

                    mc "Dar uma vida melhor pra elas é só uma consequência. E essa é toda a diferença."

                    a "..."

                    mc "Pense bem no que você vai fazer se a casa do [gus] começar a cair. Ela pode soterrar você junto com ele."

                    a "Eu pensei que você fosse entender. Mas você tá até me ameaçando. Você não entende nada também, idiota."

                    mc "Pode falar o que você quiser. Eu sei de que lado eu tô."

                    mc "Tenha uma boa noite."

                    a "..."
        "Ok. Eu vou poupar ele pela [c].":


            $ p9_miranda = 2

            "Talvez ela tenha razão... eu posso tá sendo egoísta aqui. Eu preciso colocar a [c] em primeiro lugar."

            scene p9_img7 with Dissolve(1.0)

            mc "Se você realmente acha que isso é o melhor pra [c], eu vou fazer isso."

            a "Você tá falando sério?"

            mc "Tô. Eu achei que salvando a Pri do [gus] eu ia ajudar ela a ter uma vida melhor. Mas quem sabe eu tô errado?"

            mc "Talvez ela só precise de alguém que apoie elas nas coisas. E ela mesmo disse que quer fazer outro filme."

            a "Nossa, [mc]... você amadureceu bastante desde a primeira vez que a gente conversou."

            mc "Acho que depois de ver tanta coisa nessa cidade, a gente acaba olhando as coisas por outro lado."

            a "Você realmente gosta da [c]. Eu consigo ver nos seus olhos. E eu tenho certeza que ela vai ficar bem com você do lado dela."

            mc "Vamos ver o que o futuro reserva..."

            menu:
                "Mas eu vejo um futuro com você.":


                    mc "Só que... pra falar a verdade, acho que eu prefiro ficar do seu lado e não do dela."

                    a "Hm?"

                    if priscila_namoro:

                        a "Você e ela não tão namorando?"

                        mc "Sim... mas as coisas não tão indo bem."

                        a "Hmm..."
                    else:


                        mc "Eu e a [c] somos só amigos. Não temos nada mais que isso..."

                    mc "E, pra ser sincero, eu sempre tive uma certa atração por você."

                    a "[mc]... isso é meio repentino."

                    mc "Você me convenceu a ter o que você queria. Será que a gente não pode comemorar?"

                    a "Essa sua cara de pau... tem o seu charme."

                    mc "Eu sei... por que a gente só não bebe um drink ou dois? Na minha conta."

                    if miranda_seducao >= 8:

                        a "Ok... um drink ou dois, no máximo."

                        mc "É só o que eu tô pedindo... Eu sei o drink perfeito pra você nesta noite."

                        a "Você conhece de bebida?"

                        mc "Não muito... mas o suficiente pra saber de uma bebida que vai te deixar louca."

                        a "Agora eu fiquei ansiosa..."

                        scene black with dissolve

                        "..."

                        a "Ai, [mc]... o que foi isso que você me deu?"

                        mc "O-opa..."

                        scene p9_img4 with Dissolve(1.0)

                        jump p9_miranda_seducao
                    else:


                        a "Quem sabe em uma próxima?"

                        mc "É sua decisão final? Uma pena..."

                        a "O importante é que a gente se entendeu na questão da [c] e do [gus]."

                        mc "Vamos ver o que vai acontecer..."

                        a "Boa noite, [mc]."

                        mc "Até a próxima."
                "Acho que podemos ir, né?":


                    mc "Acho que conversamos o que tinha pra falar, né? Podemos ir."

                    a "O importante é que a gente se entendeu na questão da [c] e do [gus]."

                    mc "Vamos ver o que vai acontecer..."

                    a "Boa noite, [mc]."

                    mc "Até a próxima."
        "Talvez eu aceite se você me convencer...":


            $ p9_miranda = 3

            mc "Talvez eu deva aceitar essa... se você for convincente."

            a "Hm? Se eu for convincente? Eu achei que você tivesse entendido nossa situação."

            mc "Quero dizer... se você me convencer de outro jeito. Talvez, sem falar nada..."

            a "Então é isso que você quer? Bom... parece que no fim você é só mais um homem, hm?"

            mc "Acho que você entendeu o que eu quis dizer."

            a "Eu entendi... e eu acho que a gente pode se entender..."

            scene p9_img4 with Dissolve(1.0)

            pause

            mc "Opa... acho que você entendeu mesmo."

            a "Vou falar a verdade... eu gosto de manter as coisas simples. Leva menos tempo e são mais fáceis."

            mc "Entendi..."

            a "E eu tenho muito mais sorte que a [c], não acha? Você ainda é bonito, cheiroso, tem um corpo legal."

            mc "Obrigado. Eu também te acho muito gata. Desde sempre eu quis receber um carinho seu, sabe?"

            a "Devia ter falado antes... eu nunca ia recusar dar um carinho pra você."

            mc "Tenho quase certeza que eu deixei bem na cara que eu tava querendo algo assim."

            a "Que falta de atenção a minha..."

            mc "E eu prometo que se você se comportar bem, eu vou fazer um carinho em você também."

            a "Eu ia adorar... mas... será que eu fui convincente agora?"

            mc "Eu diria que você está indo muito bem..."

            a "Que bom."

            mc "A gente não vai parar agora, né?"

            a "O resto eu vou deixar pra depois que tudo acontecer. Se tudo der certo, eu prometo que você vai sair ganhando."

            mc "Eu vou ter o que eu quero de você?"

            a "Mais ainda..."

            menu:
                "Eu não vou aguentar esperar.":


                    mc "Não quero esperar... eu já tô de olho em você tempo demais."

                    a "Tá de olho em mim?"

                    if priscila_namoro:

                        a "Você e a [c] não tão namorando?"

                        mc "Sim... mas as coisas não tão indo bem."

                        a "Hmm..."
                    else:


                        mc "Eu e a [c] somos só amigos. Não temos nada mais que isso..."

                    mc "Faz tempo que eu quero você."

                    mc "Você é uma mulher sexy. Eu adoro mulher que sabe o que tá fazendo."

                    mc "Eu não sei quando a gente vai se encontrar assim de novo... então eu não quero perder essa chance."

                    mc "Eu quero experimentar você agora. Se você tiver afim de esquecer tudo e só curtir comigo."

                    a "[mc]... você..."

                    if miranda_seducao >= 8:

                        a "Quando você fala desse jeito, fica difícil de resistir. Mas só se você prometer cumprir nosso trato."

                        mc "Com certeza. Você tem minha palavra."

                        label p9_miranda_seducao:

                            $ p9_miranda_beijo = True

                            a "Eu tô me sentindo tão bem agora. Eu não achei que você fosse aceitar."

                            mc "E eu não acredito que eu tô com você no meu colo."

                            a "Você mereceu."

                            mc "A gente mereceu. A gente só tem que aproveitar e comemorar."

                            a "Concordo."

                            mc "Você é maravilhosa, [a]. Um mulherão da porra."

                            a "Já tá bom de elogios. Você já conseguiu o que você queria."

                            mc "Então deixa eu pegar meu prêmio."

                            scene p9_img5 with Dissolve(1.0)

                            pause

                            "Eu não sei se ela tava preparada pra isso, mas é minha chance de pegar essa gata."

                            a "Ninguém falou nada sobre beijo..."

                            mc "Bom... agora você sabe."

                            a "{i}Hmmm{/i}"

                            a "Você beija bem, [mc]. Melhor do que eu imaginava."

                            mc "Você não viu nada ainda."

                            "Se ela acha que eu vou ficar só nisso."

                            window hide

                            pause

                            scene p9_img6 with Dissolve(1.0)

                            pause

                            a "Ai, [mc]! Você tá indo longe demais..."

                            mc "Você não gosta?"

                            a "E-eu não disse isso! Hm!"

                            a "A g-gente precisa parar!"

                            mc "E se eu não quiser? Eu achei você uma delícia."

                            a "[mc]!"

                            window hide

                            pause

                            scene p9_img4 with Dissolve(1.0)

                            mc "Calma. Já parei..."

                            a "Você é saidinho demais... precisa ir com calma."

                            mc "Eu não escutei você falando que não gostou. Aliás, meu apê é aqui perto. E se a gente..."

                            a "Não, não... isso fica pra depois que tudo isso passar. Se você fizer a sua parte."

                            mc "Ok... ok..."

                            a "O importante por hoje é que a gente se entendeu na questão da [c] e do [gus]."

                            mc "Vamos ver o que vai acontecer..."

                            a "Faça sua parte e a gente vai se entender, [mc]. Eu prometo que você não vai se arrepender."

                            mc "Eu quero só ver... Até a próxima, [a]."
                    else:


                        a "Eu... realmente não posso agora. Tem muita coisa acontecendo."

                        mc "É sua decisão final? Uma pena..."

                        a "O importante é que a gente se entendeu na questão da [c] e do [gus]."

                        mc "Vamos ver o que vai acontecer..."

                        a "Boa noite, [mc]."

                        mc "Até a próxima."
                "Tudo bem. Eu vou esperar.":


                    mc "Eu vou dar essa moral pra você. Eu vou esperar."

                    a "Vai valer a pena. Eu prometo, bobinho..."

                    a "O importante é que a gente se entendeu na questão da [c] e do [gus]."

                    mc "Vamos ver o que vai acontecer..."

                    a "Você vai saber de mim logo logo, [mc]..."

                    mc "Vou tá te esperando..."

    scene pub booth with Dissolve(1.0)

    "Espero que essa conversa com ela acabe ajudando em alguma coisa... Pelo menos que eu não tenha ferrado tudo mais ainda."

    "Alguma coisa me diz que a [a] ainda vai ser importante nessa história."

    scene black with Dissolve(2.0)

    "..."

    $ dia += 1
    $ tempo = 1

    jump priscila_e9_agata

label priscila_e9_agata:

    $ priscila_e9 = "agata"

    "..."

    scene ape_geral with Dissolve(2.0)

    "Uaaaahhh..."

    "Aquela conversa ontem com a [a]... Por que será que ela tá tão preocupada? Não tem nada acontecendo."

    if p9_miranda_beijo:

        "O bom é que a gente acabou se pegando. E vai ter mais depois disso tudo."

    "O foda é que mais um dia passou e ninguém fala nada sobre isso... parece até que tão abafando o caso."

    "Merd-{nw}"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr... trrrr..."

    mc desconfiado "Hm? De novo?"

    "Eu não sei de quem é esse número."

    scene ape_celular_falando with Dissolve(1.0)

    "???" "Alô? Eu falo com o [mc]?"

    mc "Isso."

    "???" "Lembra de mim?"

    "Eu já escutei essa voz antes... mas não sei se eu lembro..."

    menu:
        "É a Miranda?":


            mc "É a Miranda, né?"

            "???" "Não. Não acredito que você esqueceu minha voz."

            "Que idiota! Eu falei com a [m] ontem! E eu tenho o contato dela! Mula!"

            mc "D-desculpa."

            ag "É a [ag]."
        "É a Ágata?":


            mc "É você, Ágata?"

            ag "Lembrou da minha voz... gostou dela, né?"

            mc "Sabia que era você."
        "É a Tatá?":


            mc "É a Tatá? A gente se viu na reunião lá."

            "???" "Não. Não acredito que você esqueceu minha voz."

            mc "D-desculpa."

            ag "É a [ag]."

    ag "Você lembra que a gente se viu lá nas gravações do filme, né?"

    mc "Ah! [ag]! Claro! Você foi a protagonista do filme do [gus] dantes da [c]."

    ag "É... não precisa ficar me lembrando que eu fui substituída."

    mc "N-não foi minha intenção. Malz."

    ag "Não importa. Eu quero falar com você. Será que a gente pode se encontrar?"

    menu:
        "Aconteceu alguma coisa?":


            mc "Que foi? Aconteceu alguma coisa?"

            ag "Claro. Você não viu as notícias? Caiu a casa do [gus]."

            mc "Ah. Isso eu sei."

            if p7_gustav:

                ag "Claro que você sabe. Foi você quem jogou ele na fogueira."

                mc "Pois é. Alguém precisava fazer isso."
        "Claro. Onde a gente pode se ver?":


            mc "Claro. Quer conversar agora?"

            ag "Se você pudesse... eu acho importante."

    ag "Eu estou aqui no centro. Se você parar no primeiro ponto depois da ponte você vai me ver do lado de uma loja de roupas."

    mc "Ah. Eu sei onde é aí."

    ag "Você pode vir aqui agora então?"

    "Conversar com ela... será que vai pegar bem isso? Ainda mais agora com o [gus] na mira por causa de uma matéria da nossa revista."

    "Mas passou tanto tempo... e eu não ouvi mais nada sobre isso. Será que ele vai se safar fácil desse jeito?"

    "Será que só a palavra da [c] não foi suficiente pra investigarem ele?"

    "Agora a [ag] quer falar comigo... o que eu faço?"

    menu:
        "Ok. Vamos conversar agora.":


            $ p9_agata = True

            mc "Beleza. Eu vou precisar de um tempo pra pegar o busão e chegar aí."

            ag "Ônibus? Eca... plebeus..."

            mc "É o jeito."

            ag "Tá bom. Mas se você demorar muito, nem adianta vir. Eu... não vou gastar minha beleza te esperando sozinha aqui."

            mc "Calma, calma... eu já tô chegando."
        "Melhor a gente não se ver.":


            mc "Acho que não é uma boa a gente se ver, [ag]. Justamente pelas coisas que tão acontecendo. Ia ser estranho."

            mc "Eu trabalho pra revista que tá denunciando ele por abusar das atrizes. Você é... uma potencial vítima, entende?"

            ag "Foda-se. Se você não quer falar comigo, eu não preciso falar com você também. Eu pensei que você fosse diferente."

            mc "[ag]! Calma!"

            "Talvez ela possa ajudar! É melhor eu dar só uma olhadinha!"

            mc "Eu vou dar uma passada aí! Espera!"

            "{i}Tu tu tu{/i}"

            "Tomara que ela tenha me ouvido. Bora!"

            scene black with dissolve

            call locomocao from _call_locomocao_3

            scene cidade centro1 with Dissolve(1.0)

            pause

            "Ela disse que ia tá do lado da loja de roupas... deve ser por aqui... Vou dar uma olhada."

            "..."

            mc desculpa "Merda... Ela não esperou... Será que era melhor eu ter falado com ela? Bom... agora não adianta chorar pelo leite derramado."

            jump priscila_e9_juiza

    "Primeiro a [a] e agora a [ag]... será que tá acontecendo alguma coisa e eu ainda não sei?"

    "Eu não sei se eu devia ligar pra Pri... eu tava achando que ela ia me ligar, mas nada até agora."

    "O duro é não saber se isso é um bom ou mau sinal..."

    "Agora eu preciso ir rápido antes que a [ag] enjoe de me esperar e pique a mula."

    "Quando a gente tava na floresta ela deu em cima de mim na caruda. Eu não sei o o que esperar dessa mina."

    scene black with dissolve

    call locomocao from _call_locomocao_4

    scene cidade centro1 with Dissolve(1.0)

    pause

    "Ela disse que ia me esperar do lado da boutique. Deve ser por aqui."

    mc zerado "Opa... uma mulher toda de preto como se tivesse em um velório de filme. E o cabelo vermelho... só pode ser..."

    mc normal "E aí, [ag]?"

    scene p9_img8 with Dissolve(1.0)

    pause

    ag "Por que você tá gritando?!"

    mc desconfiado "Hm? Eu tô falando normal."

    ag "E não fale meu nome. E não chegue muito perto. Vamos conversar dessa distância."

    mc zerado "Você que me chamou aqui, lembra?"

    ag "A conversa vai ser rápida. Eu só preciso que você saiba uma coisa."

    mc desculpa "Tô ouvindo."

    ag "O [gus] vai ser julgado por causa da matéria da sua revista."

    mc surpreso "Quê?! O ministério público abriu um caso contra ele?!"

    ag "Xiu! Para de gritar!"

    mc preocupado "Desculpa. Você tem certeza disso?"

    ag "Eu não sei nada sobre esse negócio de ministério. Só sei que ele vai pra julgamento."

    mc desconfiado "Como você descobriu isso?"

    ag "Não interessa. Só que a coisa tá acontecendo."

    if p7_gustav:

        ag "Me falaram que foi você que publicou a matéria dele."

        mc serio "Sim. Foi eu."
    else:


        ag "Eu vi que a matéria saiu na sua revista."

    ag "Então eu queria que você soubesse que ele vai atrás de você."

    mc angustiado "Quê?!"

    ag "Ele tá muito irritado. E ele vai querer a cabeça de todo mundo envolvido nisso."

    menu:
        "Isso se ele não for preso.":


            mc serio "Isso se ele não tiver trancado na cadeia. Não é uma acusação leve."

            ag "É nisso que você tá se defendendo? Ele não vai ser preso, tonto."

            mc "Claro que vai."
        "Você precisa me ajudar!":


            mc preocupado "Você tem que dar um jeito de me ajudar!"

            ag "Q-quê?! E-eu não tenho nada a ver com isso!"

            ag "Eu quero é distância de tudo isso! Esse rolo só vai prejudicar minha carreira!"

    ag "[mc]... esse é um julgamento diferente. Eles conseguiram fazer isso de forma secreta."

    mc desconfiado "Secreta?"

    ag "O processo parece que está sob sigilo e ninguém tá sabendo que vai acontecer. Eu não entendo nada disso."

    ag "Eu só sei que tudo vai acontecer rápido e sem ninguém saber quando e como vai ser."

    mc bravo "Mas isso não tá certo."

    scene p9_img9 with Dissolve(1.0)

    pause

    ag "Não venha perto de mim, seu idiota!"

    mc "Você precisa me explicar isso melhor, [ag]!"

    ag "Eu já falei que eu não sei! E para de falar meu nome!"

    ag "O que eu sei é isso! Eles vão fazer um tipo diferente de audiência. Eles vão chamar algumas pessoas pra depor."

    mc desconfiado "Você vai ser chamada?"

    ag "Hmf..."

    ag "Sim."

    mc desculpa "Foi o que eu pensei... então a [c] também vai."

    ag "Com certeza. Ela é pessoa central disso tudo."

    mc "Então eles conseguiram esconder a audiência pra não sair na mídia..."

    ag "É. Mas eu sei quando vai sair..."

    mc surpreso "Claro! Porque você foi chamada!"

    ag "É! Agora cala a boca!"

    mc desculpa "..."

    ag "Eu só queria te avisar pra tomar cuidado... porque tudo isso que tá acontecendo é muito ruim pra minha carreira."

    ag "Então eu vou falar que nada aconteceu."

    mc preocupado "Sério?"

    ag "Eu nem tenho o que falar dele. Todo mundo suspeita da [c], mas não aconteceu nada comigo."

    mc desculpa "Verdade? Ele nunca fez nada contra você?"

    ag "Eu não tenho porque responder isso pra você. E nem pra Justiça. Ninguém precisa saber o que aconteceu."

    mc "[ag]... dá pra ver que tem uma coisa que não tá normal."

    ag "Normal? Claro que não. No mundo das celebridades nada é normal, [mc]. É uma selva. Os mais fortes sobrevivem."

    ag "Um fraco igual você nunca ia ter sucesso nesse mundo."

    mc "Você sabe que meu trabalho é entregar segredos de pessoas que são próximas, né? Amigos... e até mais..."

    ag "É um serviço bem porco realmente."

    mc zerado "Não precisa falar assim... mas você não tá errada."

    ag "Se você entende isso, então entende o que eu tô passando. Eu não posso jogar tudo fora agora."

    "A [ag] tá confusa... dá pra ver que por trás dessa certeza dela, ela ainda tem dúvida do que vai fazer."

    "Ela não precisava ter me chamado aqui. Ela não deve nada pra mim. Se ela me chamou, é porque ela quis."

    "Agora... o que eu falo pra ela? Eu sinto que o que eu falar aqui pode influenciar ela no julgamento."

















    menu:
        "Você precisa entregar o [gus].":


            $ agata_confessa = True

            mc serio "Você precisa falar a verdade, [ag]."

            ag "Q-quê?"

            mc "Você vai estar sob juramento. Se você falar uma mentira, e depois descobrirem, você pode ter que responder por isso."

            ag "..."

            mc desculpa "E isso nem é o principal. O mais importante é que o [gus] não pode continuar fazendo o que ele fez."

            mc "Esse velho usou o poder dele pra se aproveitar de pessoas vulneráveis. Isso não tem desculpa."

            mc bravo "Abusar do seu poder pra conseguir o que quer não é só anti ético. Isso é nojento e quem faz isso é fraco e ridículo."

            mc "Se a gente deixar esse cara continuar fazendo isso, mesmo sabendo de tudo, a gente vai tá do lado dele."

            mc desculpa "Eu sei que isso pode prejudicar você conseguir contratos, mas... pensa... você não quer que ele pague pelo que ele fez?"

            ag "[mc]..."

            ag "Você... lembra quando a gente se viu na floresta do set de filmagem do filme?"

            mc envergonhado "L-lembro."

            if agata_beijo:

                scene p9_img10 with Dissolve(1.0)

                pause

                ag "Naquele dia a gente se beijou. Eu sei que você lembra. Quem esqueceria de um beijo meu?"

                mc envergonhado "Verdade..."

                ag "E isso foi muito ruim, sabe?"

                mc desconfiado "Hm? Por quê? Eu não beijei bem?"

                ag "Nada a ver, idiota..."

                ag "Eu pensei muito naquele dia, sabe? Se tava certo o que eu fiz... e a conclusão que eu cheguei é que você é um cuzão."

                mc surpreso "C-como?!"

                ag "Pensa... quando a gente se beijou, você falou que tava namorando a [c]. Aliás, foi por isso que eu quis te beijar. Roubar algo dela."

                mc zerado "Você fala isso na cara dura?"

                ag "Agora, ou você mentiu que tava namorando ela, o que faz você de um mentiroso. Ou você falou a verdade e traiu sua namorada. O que é pior."

                ag "E ainda quer que eu confie em você pra denunciar o [gus]? Se enxerga."

                mc preocupado "Eu sei que eu fiz cagada, [ag]. Desculpa. Mas isso é sério!"

                ag "Não adianta falar isso agora. Eu não confio em você."



                menu:
                    "Tá certa. Eu só queria te pegar {b}(+18){/b}":


                        mc concentrando "Tem razão... eu só queria pegar com você."

                        ag "Hm? Como é?"

                        mc charmoso "Uma garota gata igual você, famosa... eu tava falando qualquer merda só pra ficar contigo."

                        ag "Você não tem nem vergonha, né? Falar assim na cara dura que só queria me comer."

                        mc safado "Mas era o que eu queria. E você tá me devendo desde aquela vez."

                        ag "Eu sei que eu sou inesquecível, mas... sério mesmo?"

                        mc "Já que você me pegou na mentira, por que não aproveitar o lado bom? Ficar com o namorado da Pri?"

                        ag "Mas você tá namorando ela mesmo então?"

                        mc "Tô. Desde antes daquela época lá."

                        ag "Não acredito..."

                        scene p9_img12 with Dissolve(1.0)

                        mc surpreso "E-ei!"

                        ag "Eu tive uma ideia... vem aqui comigo..."

                        mc desconfiado "Você vai na loja de roupa?"

                        ag "É. Aqui a gente vai ficar de boa. Vem logo."

                        "S-será que vai dar certo mesmo?"

                        mc tarado "T-tô indo."

                        scene black with dissolve

                        scene boutique geral with Dissolve(1.0)

                        "Essa loja..."

                        ag "Vem aqui."

                        "Atendente" "Posso ajudar, senhorita?"

                        ag "Não. Eu só quero mostrar uma roupa pra ele. Eu sei onde tá."

                        "Atendente" "Fiquem à vontade."

                        scene boutique trocador with Dissolve(1.0)

                        mc charmoso "Acho que entendi sua ideia..."

                        ag "Não fala nada... só me segue."

                        ag "Aqui."

                        scene pri9_img1 with Dissolve(1.0)

                        pause

                        ag "Você vai entrar ou não vai?"

                        mc envergonhado "Tem certeza que é uma boa?"

                        ag "Não é você que falou que queria aproveitar? Vai dar pra trás agora?"

                        mc "Mas e atendente?"

                        ag "Eu prometo que eu vou gemer bem baixinho..."

                        mc surpreso "A-ah..."

                        "Assim eu não vou aguentar.."

                        scene pri9_img2 with Dissolve(1.0)

                        pause

                        ag "Parece que alguém comprou a ideia de verdade..."

                        mc "Você tá me provocando demais..."

                        ag "Você tem a Pri com você, a queridinha do Gustav. Por que toda essa vontade de ficar comigo?"

                        mc "Porque você é linda também."

                        ag "'Também'?"

                        mc "Você é muito mais gata que ela."

                        ag "Eu sei. Mas eu adoro ouvir. E você vai até trair ela só pra tirar um pedacinho de mim?"

                        mc "Hmm..."

                        ag "Espera. Não fala ainda. E-eu vou te dar uma amostra grátis. Vem aqui."

                        mc "E-ei!"

                        scene pri9_img3 with vpunch

                        pause

                        mc "Hmm?!"

                        ag "Hmm!"

                        ag "Você lembra lá da floresta no set de filmagem? Eu posso te dar... muito prazer..."

                        mc "Eu sei... você é demais, [ag]..."

                        ag "Você só precisa me escolher no lugar da Pri. Eu quero que você traia ela porque me comer é mais importante pra você agora."

                        mc "a-ah..."

                        ag "E então? Vai querer ou não?"

                        if priscila_namoro:

                            "Eu tô namorando a Pri... será que vale a pena trair ela com a [ag]? E se ela contar?"

                            "Do jeito que ela tá falando... pra ela seria tudo jogar na cara da Pri que ela me fez trair."
                        else:


                            "Eu nem tô namorando a Pri... e se a [ag] for falar com ela?"

                            "A mentira pode cair por terra e eu me ferrar com as duas..."

                        "Isso pode acabar dando muita merda mais pra frente..."

                        label pri9_premium1:

                            pass

                        "O que eu faço?"

                        menu:
                            "Trair a Pri com a [ag]":


                                if not premium:

                                    call mensagem_premium from _call_mensagem_premium_7

                                    jump pri9_premium1

                                mc "Eu escolho você, [ag]."

                                ag "Ai..."

                                ag "Você escolheu certo, [mc]. Eu vou te agradar."

                                ag "Da outra vez você não me comeu, então nessa aqui pode vir direto. Eu sou toda pra você hoje."

                                mc "Era isso que eu queria ouvir. Eu não ia aguentar ficar de novo sem sua bucetinha."

                                mc "Deixa eu te preparar antes."

                                scene black with dissolve

                                scene pri9_img4 with dissolve

                                pause

                                ag "Hm-hmmm! E-eu disse que era pra você aproveitar..."

                                mc "Calma... deixa eu preparar ela antes. Eu não quero te machucar."

                                ag "Q-que... hmm... c-cavalheiro..."

                                "Ela já tá bem molhada."

                                "Só de saber que eu vou trair a Pri, ela já ficou assim... essa garota..."

                                "Eu também não quero saber. Eu vou aproveitar."

                                mc "Agora você tá no ponto."

                                ag "Então vem."

                                mc "Eu quero comer você por trás. Vira aí."

                                scene pri9_img5 with Dissolve(1.0)

                                pause

                                ag "Hm!"

                                mc "Que delícia, [ag]!"

                                ag "Seu pau é grande, [mc]! Cuidado comigo, eu sou pequena!"

                                mc "Shh... você quer que a mulher escute?"

                                ag "T-tá... hng!"

                                mc "Você é deliciosa, garota. Você é apertadinha mesmo!"

                                ag "Aproveita! Eu quero que você aproveite! Eu sou melhor que ela em tudo!"

                                mc "Eu vou acabar com você hoje! Vem aqui!"

                                menu:
                                    "Meter mais forte":


                                        "Tá na hora dela me sentir de verdade!"

                                        scene pri9_img6 with vpunch

                                        pause

                                        ag "A-ah! Q-quanta força..."

                                        mc "Eu não sou aquele velho, não! Eu vou acabar com você, [ag]!"

                                        ag "Nnnhhhg! A-ah!"
                                    "Continuar no ritmo":


                                        "Tá bom assim. Não tenho que forçar ela."

                                        scene pri9_img6 with Dissolve(1.0)

                                        ag "Hmmm..."

                                mc "Tá sentindo ele?"

                                ag "Tô. E você tá? Gostou do meu sabor?"

                                mc "Muito. E-eu não vou aguentar muito assim. Você tá me apertando, [ag]."

                                ag "Então vaiinn. Goza!"

                                mc "P-posso gozar em você?"

                                ag "Pode. Pode jorrar em mim."

                                mc "E-eu já tô chegando lá!"

                                ag "Então fode! Ah! Ahn!"

                                mc "Isso! G-geme pra mim!"

                                ag "Ain! Isso! Mete na sua garota!"

                                mc "T-toma!"

                                scene pri9_img6 with vpunch

                                pause

                                mc "{i}puf puf{/i}"

                                mc "Você foi incrível, [ag]..."

                                ag "Vem aqui..."

                                mc "Hm?"

                                scene pri9_img3 with hpunch

                                ag "Eu quero recomeçar..."

                                mc "N-não sei se eu c-consigo... {i}puf{/i}"

                                ag "Você me deixou com fogo agora... e eu ainda não gozei..."

                                ag "Você não vai me deixar assim, né?"

                                "Já faz muito tempo que a gente tá aqui... e eu já tô satisfeito..."

                                menu:
                                    "Melhor a gente sair daqui.":


                                        mc "Desculpa, [ag], mas é melhor a gente sair daqui antes que a moça da loja venha."

                                        ag "Nhf!"

                                        scene black with dissolve

                                        scene pri9_img9 with Dissolve(1.0)

                                        ag "Não acredito que você vai me deixar assim."

                                        mc envergonhado "Desculpa... mas você foi incrível."

                                        ag "Foda-se. Eu queria gozar."

                                        mc "..."

                                        ag "Agora vai lá. E toma cuidado com o Gustav. Aquele velho é perigoso."

                                        mc "Pode deixar. Valeu."

                                        ag "Vai logo. Deixa que eu me resolvo com a moça da loja."

                                        mc "Agata... eu sei que você tem esse lance com a Pri, mas deixa eu te falar uma coisa."

                                        mc "Você é maravilhosa do seu jeito. Eu tenho certeza que você vai encontrar alguém que veja como você é especial."

                                        mc "E mesmo que você nunca encontre o príncipe encantado, saiba que você é incrível. E vai ser grande ainda."

                                        ag "Para de dar lição de moral depois de me comer. Tá acabando com o clima."

                                        mc charmoso "Haha... tá certa. Até, [ag]."

                                        ag "..."

                                        scene black with dissolve

                                        scene boutique geral with Dissolve(1.0)

                                        "Mano... a [ag] foi incrível. Que mulher..."

                                        "Eu tenho que andar... espairecer..."

                                        "Eu vou aproveitar pra andar até o centro."

                                        "Tenho que focar no que importa. Que o [gus] tá envolvido em alguma coisa... preciso descobrir o que é."

                                        scene black with dissolve

                                        "..."
                                    "Eu vou cuidar de você agora.":


                                        mc "Tá bom. Eu vou cuidar de você agora."

                                        ag "Era isso que eu queria ouvir, gostoso."

                                        mc "Eu preciso de um tempo pra ele..."

                                        ag "Eu adorei a sua lingua em mim. Deita aqui..."

                                        ag "Agora você vai fazer o que eu mandar até eu gozar."

                                        mc "Ok..."

                                        scene black with dissolve

                                        ag "Deixa eu tirar isso aqui... me ajeitar..."

                                        scene pri9_img7 with Dissolve(1.0)

                                        pause

                                        ag "Hmm! Era o que eu queria... isso... enfia sua boca nela."

                                        mc "Hnng!"

                                        ag "Não fala nada... só enfia sua boca e me faz gozar!"

                                        ag "E prepara seu menino enquanto isso... que eu vou querer gozar nele."

                                        "A [ag] tá muito excitada. Ela tá se esfregando loucamente."

                                        ag "Isso! Que delícia!"

                                        ag "Não para de lamber agora! Ahh!"

                                        ag "E aí? Hm! Tá pronto agora? Acho que eu vou precisar dele..."

                                        mc "Tchô... {i}shulp{/i}"

                                        ag "Que boomn... Eu tô ensopadann!"

                                        ag "Agorann me comeen, [mc]!"

                                        mc "Vem aqui!"

                                        scene black with dissolve

                                        scene pri9_img8 with Dissolve(1.0)

                                        pause

                                        ag "Ah! Assim! Tão grosso na minha bucetinha!"

                                        mc "Hm! Você tá mais apertada ainda, [ag]!"

                                        ag "Eu tô quase gozando! Não para agora!"

                                        "Atendente" "s-senhorita!?"

                                        mc "Eita, porra!"

                                        ag "Não para agora!"

                                        mc "Mas ela tá escutando!"

                                        ag "Foda-se! Você aguenta ou não?!"

                                        menu:
                                            "Então toma, tesuda filha da puta!":


                                                scene black with dissolve

                                                scene ani19 with Dissolve(1.0)

                                                pause

                                                mc "Era isso que você queria?!"

                                                ag "Isso! Aahh! Eu quero que você não resista!"

                                                ag "Você não resiste trair sua namorada com sua puta!"

                                                mc "Não resisto! Você é uma puta gostosa demais!"

                                                "Atendente" "G-gente!"

                                                ag "I-isso! Aahnn! Usa sua puta pro que ela serve! Pra ser a perfeita cadela do teu caralho!"

                                                mc "Isso! Você é a melhor cadela, Ágata! Aahh!"

                                                ag "Eu sei! A Ágata é a melhor! Aahhnn!"
                                            "Não dá pra fazer isso agora. Só goza rápido!":


                                                ag "Frouxo!"

                                        ag "Enfia fundo na [ag]! Come!"

                                        mc "a-ah!"

                                        ag "Ai-aiinnnn!"

                                        scene pri9_img8 with vpunch

                                        ag "Aaaiinnnngghhh!!!"

                                        "Atendente" "s-senhorita!?"

                                        ag "A-ah! Aaah..."

                                        mc "T-tá tudo legal. Ela... se prendeu aqui... mas tá bem!"

                                        "Atendente" "O-ok... esses clientes..."

                                        mc "Ela sabe, [ag]..."

                                        ag "Foda-se... e-eu tô tremendo... e-eu... eu nunca senti uma coisa assim..."

                                        ag "{i}puf puf{/i}"

                                        scene black with dissolve

                                        scene pri9_img9 with Dissolve(1.0)

                                        ag "Então isso é gozar... que d-delícia..."

                                        mc charmoso "Que bom que você gostou."

                                        ag "Nem acredito que a Pri tem isso quando ela quer..."

                                        ag "Ela que não abra o olho... eu vou roubar você..."

                                        mc envergonhado "Haha..."

                                        "Se ela soubesse que eu a Pri ainda não transamos de verdade ainda..."

                                        ag "Agora vai lá. E toma cuidado com o Gustav. Aquele velho é perigoso."

                                        mc "Pode deixar. Valeu."

                                        ag "Agora vai logo. Deixa que eu me resolvo com a moça da loja."

                                        mc "Agata... eu sei que você tem esse lance com a Pri, mas deixa eu te falar uma coisa."

                                        mc "Você é maravilhosa do seu jeito. Eu tenho certeza que você vai encontrar alguém que veja como você é especial."

                                        mc "E mesmo que você nunca encontre o príncipe encantado, saiba que você é incrível. E vai ser grande ainda."

                                        ag "Para de dar lição de moral depois de me comer. Tá acabando com o clima."

                                        mc charmoso "Haha... tá certa. Até, [ag]."

                                        ag "..."

                                        scene black with dissolve

                                        scene boutique geral with Dissolve(1.0)

                                        "Mano... a [ag] foi incrível. Que mulher..."

                                        "Eu tenho que andar... espairecer..."

                                        "Eu vou aproveitar pra andar até o centro."

                                        "Tenho que focar no que importa. Que o [gus] tá envolvido em alguma coisa... preciso descobrir o que é."

                                        scene black with dissolve

                                        "..."
                            "Parar por aqui":


                                "Eu não posso fazer isso com a Priscila e nem com a [ag]. Não seria certo, não seria justo."

                                "Elas já sofreram demais na mão de um homem inescrupuloso e eu não sou igual ele. Eu não sou terrível igual o Gustav."

                                "Eu vou fazer a coisa."

                                mc "Desculpa, [ag], mas eu não posso fazer isso com você."

                                mc "É melhor eu sair daqui."

                                scene black with dissolve

                                ag "S-seu idiota! Me solta então! IDIOTA! CORRE PRA AQUELA VADIA QUE SE VENDE!"

                                mc "A-adeus!"

                                scene boutique geral with Dissolve(1.0)

                                "Foi melhor assim..."

                                "Eu tenho que andar... espairecer..."

                                "Eu vou aproveitar pra andar até o centro."

                                "Tenho que focar no que importa. Que o [gus] tá envolvido em alguma coisa... preciso descobrir o que é."

                                scene black with dissolve

                                "..."
                    "E-espera!":


                        ag "Passar bem."

                        scene black with dissolve

                        mc angustiado "[ag]! Volta!"

                        "Saco!"

                jump priscila_e9_juiza
            else:


                scene p9_img10 with Dissolve(1.0)

                pause

                ag "Naquele dia eu queria te beijar, sabe? Pra roubar você da [c]. Eu queria tanto pegar uma coisa dela."

                ag "Eu queria fazer igual ela fez comigo. Ela tirou meu lugar. O lugar que eu penei tanto pra conseguir."

                ag "Com aquele rostinho dela, aquele sorriso... aceitando dar pro diretor como se não fosse nada... aquilo me revirava o estômago."

                ag "Se eu conseguisse tirar você dela... mesmo que fosse só um beijo... eu já ia me sentir melhor. Mas nem isso deu certo pra mim."

                ag "Acho que eu nasci pra ser a segunda mesmo..."

                mc desculpa "Acho que você não tá olhando a situação da melhor forma, sabe?"

                ag "Que outro jeito tem da gente olhar pra isso?"

                mc "A [c] sofreu muito com o que aconteceu com ela. Ela pensou até em se matar uma noite."

                mc "E foi horrível pra você também. Eu sei que foi. E vocês só tiveram que passar por isso por causa de um velho nojento e tarado."

                mc "Quando a Pri tava super mal... eu fiz uma coisa com ela que ajudou. Será que eu posso fazer com você também?"

                ag "Uma 'coisa'? P-pode..."

                scene p9_img11 with hpunch

                pause

                ag "!!!"

                mc "Não esquece que você não tá sozinha. E tudo que é ruim uma hora passa. Por pior que seja, uma hora as coisas mudam."

                mc "Eu sei que não foi fácil pra você e agora você só quer uma coisa boa depois de ter passado por tanta coisa ruim."

                mc "Mas essa coisa não vai vir do [gus] e nem dos outros idiotas que apoiam ele. Árvore podre não pode dar fruto bom."

                mc "Esquece essa galera. Você é linda, espera e muito determinada. Você vai conseguir outra coisa pra fazer."

                mc "E, se você precisar de ajuda, eu prometo que eu vou tá do seu lado, ok? Pode contar comigo."

                ag "S-seu idiota..."

                ag "Falando t-toda essas merdas s-sem saber de nada..."

                ag "{i}snif{/i}"

                mc "Eu sei que eu não sei. Só você que passou por isso sabe. Mas eu posso tá do seu lado mesmo assim."

                ag "Droga... eu odeio quando os outros tão certos..."

                mc "Haha... cabeça dura."
        "Você tá certa. Tem que se proteger.":


            $ agata_confessa = False

            mc charmoso "Você tem razão. Tem que pensar em você primeiro. Deixa o [gus] pra lá."

            ag "Hm?"

            scene p9_img10 with Dissolve(1.0)

            pause

            ag "Você tem certeza?"

            mc charmoso "Eu tenho. Você tem que ser a prioridade e não as outras pessoas."

            mc "Se falar qualquer coisa contra ele vai prejudicar sua carreira, então esqueça isso. Foque em você."

            ag "É! É isso que eu tava pensando mesmo. Eu não tenho n-nada a ver com essas picuinhas dos outros. Tá tudo certo pra mim."

            mc "Então estamos combinados."

            ag "Estamos..."

    ag "Obrigada, [mc]... por ouvir o que eu tinha pra falar."

    mc "Relaxa."

    ag "Eu vim aqui porque eu tava em dúvida do que eu ia fazer, mas você me ajudou a colocar a cabeça no lugar."

    scene p9_img12 with Dissolve(1.0)

    pause

    mc surpreso "E-ei!"

    ag "Agora eu tô muito melhor! Valeu, tontão!"

    mc zerado "Tontão?"

    ag "Espero que dê tudo certo pra gente no final! Boa sorte na audiência, [mc]!"

    mc angustiado "Ei! Calma! Volta!"

    scene black with dissolve

    mc angustiado "V-você não me falou onde vai ser!"

    "Cada uma..."

    jump priscila_e9_juiza

label priscila_e9_juiza:

    scene cidade centro1 with Dissolve(1.0)

    "Agora eu tô aqui no centro... Eu sei que tá rolando alguma coisa com o [gus]... mas eu não tenho informação!"

    "Se eu não descobrir esse rolo, as coisas vão acontecer e eu não vou poder fazer nada!"

    if nona_e3 == "morta":

        "A [h] estava lutando contra o grupo deles... talvez ela pudesse me ajudar de alguma forma agora."

        "Infelizmente ela acabou morrendo naquele lance horrível com o [to] no bar."

        if no3_tony:

            "Eu decidi contar tudo pra ele e ele me deu até uma pauta."

            "Independente do que acontecer com o [gus], provavelmente eu tô de boa. Eu não acho que o [mar] vai aceitar me matar."

            "Eu tô do lado deles agora. Mas talvez seja melhor eu dar um pulo lá na pizzaria e falar com ele."

            "Ter uma garantia que tudo vai acabar bem pra mim é uma boa."

            scene black with dissolve

            "..."

            mc charmoso "E aí, [to]?"

            "Sorte que ele tá aqui."

            to "[mc]... sente-se por favor."

            scene chefao_pizzaria_close with Dissolve(1.0)

            to "Que visita inesperada."

            mc normal "Valeu por me receber."

            to "Não é esforço algum. Achei interessante você ter vindo."

            mc desculpa "Eu queria falar com você sobre a questão do [gus]."

            to "Muito bem..."

            if p7_gustav:

                to "Foi muito imprudente de sua parte ter publicado aquela matéria na revista. Isso prejudicou um de nossos aliados."

                mc preocupado "Desculpa, [to]. Eu ainda não tava com vocês na época que eu decidi isso."

                to "Sim... eu entendo. Não se preocupe."
            else:


                to "Essa matéria que saiu na sua revista prejudicou um de nossos aliados."

                mc desculpa "Sei... desculpa..."

                to "Não se preocupe. Não foi você que quis publicar. Eu sei disso."

            to "Agora o [gus] vai passar por uma espécie de julgamento, e isso é péssimo para quem quer manter as coisas por baixo dos panos."

            to "Usamos nossa influência pra conseguir que fosse um julgamento diferente. Vai ser uma sessão secreta, sem júri e sem mídia."

            mc charmoso "Isso parece conveniente."

            to "Muito. O problema é que a juíza sorteada foi justamente a Elizabeth Richter. Uma das únicas que não temos no bolso."

            to "Isso significa que, pela primeira vez em muito tempo, teremos um julgamento real acontecendo."

            to "Isso é perigoso, [mc]. Nossos parceiros não gostam de incerteza. Eles investem muito pra garantir que tudo ande como deve."

            mc desculpa "Entendo..."

            to "Independente do resultado, eu quero que você fique tranquilo. Nada vai acontecer com você."

            if not p7_gustav:

                mc "Eu também queria pedir pra que nada acontecesse com a [w], que publicou a matéria."

                to "Hmm... tudo bem. Se é um pedido seu, eu posso garantir a segurança dela também."

                to "Mas apenas porque você é nosso aliado agora."

                mc normal "Perfeito. Obrigado, [to]."

            to "Mas o que eu quero de você é que você garanta que o [gus] não entre em cana."

            to "Você tem contato com várias das pessoas que podem ser chamadas pra depor."

            to "Caso você se encontre com elas, eu quero que você as convença a negar a denúncia. O [gus] pode ser um pé no saco, mas ele é importante."

            to "Será que você pode fazer isso pra mim?"

            menu:
                "Com certeza. Eu vou fazer.":


                    mc charmoso "Com certeza. Pode contar comigo."

                    to "Perfeito."
                "Vou tentar...":


                    mc envergonhado "Eu vou tentar..."

                    to "Dê o seu melhor. Agora você é um de nós. Isso também lhe diz respeito."

                    mc "Pode deixar..."

            to "Então é isso. Fique em paz e vamos trabalhar pelo melhor."

            mc charmoso "Ok. Até mais, [to]."

            scene black with dissolve

            jump priscila_e9_final
        else:


            "Acho que eu vou voltar pra casa. Não tem mais nada pra mim aqui."

            scene black with dissolve

            "..."

        jump priscila_e9_final

    $ p9_juiza = True

    $ renpy.vibrate(1)

    mc desconfiado "Mensagem..."

    mc zerado "Um número todo estranho... deve ser a [h] de novo."

    "{i}Estou vendo que você tá no centro.{/i}"

    "Ela precisa parar de me hackear."

    "{i}Vai até o tribunal e procura pela juíza. Ela vai ter uma coisa pra você.{/i}"

    "Só isso... epa! a mensagem apagou."

    "Como ela consegue fazer tudo isso? Eu preciso trocar de aparelho urgente."

    "Ela disse pra eu ir até o tribunal... espero que seja uma coisa que me ajude e não acabe comigo preso."

    scene black with dissolve

    $ tempo = 2

    scene cidade centro9 with Dissolve(1.0)

    pause

    "O tribunal fica dentro da prefeitura. Eu vou ter que entrar por aqui."

    scene black with dissolve

    scene tribunal geral with Dissolve(1.0)

    pause

    mc desconfiado "Tô aqui. E agora?"

    "Funcionário" "Ei. Rapaz."

    mc "Hm? Eu?"

    "Funcionário" "Seu nome é [mc]?"

    mc "Isso."

    "Funcionário" "[mcc]?"

    mc "Isso aí."

    "Funcionário" "Por favor. Segue por aquele vão e entra na primeira porta que a excelentíssima quer falar com você."

    mc "Excelentíssima..."

    mc normal "Beleza. Valeu pelo aviso. Vou subir lá."

    "A juíza... Aquela que me salvou da prisão depois do assalto no banco."

    if v20_fim:

        "Ela também julgou o caso do [n]. Essa mulher é maluca..."

        "Da última vez ela me falou umas coisas que pelo amor..."

    "Eu tenho que tomar cuidado com essa aí."

    scene black with dissolve

    scene sala_juiza poltronas with Dissolve(1.0)

    mc envergonhado "C-com licença."

    eli "Só um segundo."

    mc "Claro."

    menu:
        "Eu recebi uma mensagem pra vir aqui.":


            mc "Alguém me mandou uma mensagem que eu-"

            eli "Eu disse para você esperar."

            mc surpreso "O-ok!"
        "...":


            "Ela mandou eu esperar. Melhor só obedecer essa aí."

    "..."

    "Que demora..."

    eli "Terminei. Muito bem..."

    "Aleluia."

    scene juiza sofa1 with Dissolve(1.0)

    pause

    eli "A [h] me avisou que te mandaria aqui. Ela disse que você poderia ajudar."

    mc desconfiado "Ajudar?"

    eli "Veja, jovem. A Justiça é cega. Assim como ela não vê quem é o julgador e o julgado, eu faço o mesmo."

    eli "Eu não permito que corrupção adentre os sagrados salões desta instituição."

    mc envergonhado "Ok..."

    "O que ela tá querendo falar?"

    eli "No entanto, o mal existe. E é inegável que o mal se espalhou pelas entranhas desta cidade."

    eli "Pessoas que sacrificam muitas para o bem de poucas. Poder e influência sendo usados para descumprir a lei."

    eli "É meu dever garantir a Lei e Ordem. E punir aqueles que traem a maioria em benefício de si próprios."

    eli "Subir usando os outros como degraus é o mesmo que nunca sair do limbo ético e moral."

    mc "Entendo... v-você tá falando de mim?"

    eli "Espero que não, jovem. Sabemos que existe outra pessoa que se enquadra muito mais neste perfil do que você."

    if p7_gustav:

        eli "Você falou sobre ele em sua matéria. Um ato de grande coragem, diga-se de passagem."
    else:


        eli "A matéria que saiu em sua revista. A [h] revelou que as informações vieram de você."

    eli "Essa matéria garantiu que finalmente pudéssemos tomar medidas contra Gustav Aldebaran."

    mc desconfiado "Você tava atrás dele?"

    eli "Ele é um dos pilares do esquema que suja e constrange nossa cidade. Eliminá-lo será benéfico a todos."

    mc envergonhado "M-mas isso não é meio anti ético? Eu estar aqui falando com você sobre isso?"

    scene juiza sofa2 with Dissolve(1.0)

    pause

    eli "De forma alguma. Se fosse o caso, nunca aceitaria falar com você."

    eli "Não é permitido ao juíz ter acesso a advogados de ambas as partes, ou ter seu julgamento alterado por terceiros."

    eli "Neste caso, o que eu quero é sua ajuda com algo pontual."

    mc desconfiado "Minha ajuda?"

    eli "Você conhece esse mundo melhor do que a promotoria. Você esteve com a [cc] no set de filmagem."

    eli "Quem melhor do que você para falar desse caso? Eu preciso de sua ajuda para garantir que o diretor seja condenado."

    menu:
        "Você não é a juíza? Não pode só condenar ele?":


            mc envergonhado "Mas... você é a juíza. Você que vai decidir tudo. Você não pode só condenar ele se você quiser?"

            eli "Posso. Mas qual seria a justiça se fosse esse o caso? Eu não vou pesar minha decisão nem para um lado e nem para o outro."

            mc desconfiado "Nem pra salvar a cidade?"

            eli "Não. Fazer algo errado para condenar alguém que está errado é fazer o mesmo e se colocar no mesmo monte de sujeira."

            eli "Nós teremos um julgamento correto, extremamente justo e imparcial."

            mc concentrando "Entendi..."
        "Ok. Eu posso ajudar.":


            mc charmoso "Se você acha que eu posso ajudar, seria um prazer."

            eli "Ótimo."

    mc desconfiado "Então o [gus] realmente vai pra julgamento?"

    eli "Sim. Mas não em um julgamento comum. É uma outra espécie de conciliação jurídica."

    eli "É um processo que envolve somente coleta de depoimentos e a decisão é de responsabilidade do juíz e não do júri."

    mc "E esse sistema é melhor pro [gus]?"

    eli "Em teoria, não. Mas ele acreditava que poderia comprar o juíz. Porém, o destino me sorteou para o caso. Algp que ele não previu."

    mc charmoso "Então ele tá ferrado."

    eli "Na verdade, se ele conseguir controlar o depoimento das vítimas, será muito mais fácil do que convencer um júri."

    mc preocupado "E ele pode! Ele tem as vítimas nas mãos dele!"

    eli "Esse é o problema. Pra ele, é muito fácil entrar na cabeça delas e obrigar que elas fiquem quietas."

    mc "Talvez ele nem precise falar nada... elas se sentem pressionadas demais por toda a situação. E tem outras pessoas na cabeça delas."

    eli "Eu imaginei. E por isso que eu preciso de você."

    mc serio "Ok. O que você precisa que eu faça?"

    eli "Eu preciso que você me diga quem eu devo chamar pra depor."

    mc surpreso "V-você quer que eu decida uma coisa dessas?!"

    eli "Não seja medroso. Você conhece eles mais do que qualquer um que não é corrupto. Eu preciso de você."

    mc desculpa "Eu não sei... como que eu vou escolher isso?"

    eli "Isso é muito importante. Pense bem. Pense em quem com certeza denunciaria ele e que tenha um caso real contra ele."

    eli "Um depoimento que realmente comprove que ele causou mal. E, principalmente, alguém que tenha coragem e interesse em falar a verdade."

    "Ela quer que eu escolha quem vai depor contra o [gus]..."

    "Isso quer dizer que se vai ser um sucesso ou não depende do que eu vou falar agora."

    "Eu preciso escolher as pessoas certas!"

    eli "Muito bem... Quem eu devo chamar para depor?"

    label priscila_e9_escolha:

        if p9_escolha == 0:

            mc "Eu quero que você chame..."
        else:


            mc "Outra pessoa que eu acho importante é..."

    menu:

        "Priscila" if julgamento1 != "Priscila" and julgamento2 != "Priscila" and julgamento3 != "Priscila":

            if p9_escolha == 0:

                $ julgamento1 = "Priscila"

                mc serio "A primeira pessoa vai ser a [cc]."

            elif p9_escolha == 1:

                $ julgamento2 = "Priscila"

                mc serio "A segunda pessoa vai ser a [cc]."

            elif p9_escolha == 2:

                $ julgamento3 = "Priscila"

                mc serio "A última pessoa tem que ser a [cc]."

            $ p9_escolha += 1

            mc "Ela foi o pivô do caso e é impossível a gente não escutar o que ela tem pra falar."

            eli "Espero que ela tenha coragem para expor esse homem no tribunal."

            mc "Eu aposto que ela vai ter. Ela é uma mulher de fibra."

        "Ágata" if julgamento1 != "Ágata" and julgamento2 != "Ágata" and julgamento3 != "Ágata":

            if p9_escolha == 0:

                $ julgamento1 = "Ágata"

                mc serio "A primeira pessoa eu vou escolher a [ag]."

            elif p9_escolha == 1:

                $ julgamento2 = "Ágata"

                mc serio "A segunda pessoa eu vou escolher a [ag]."

            elif p9_escolha == 2:

                $ julgamento3 = "Ágata"

                mc serio "Minha terceira escolha vai ser a [ag]."

            $ p9_escolha += 1

            mc "Ela sofreu com isso antes da [c]. E eu aposto que ela vai acabar com o velho."

            eli "Se você acha que ela será uma boa testemunha, eu chamarei."

        "Tatá" if julgamento1 != "Tatá" and julgamento2 != "Tatá" and julgamento3 != "Tatá":

            if p9_escolha == 0:

                $ julgamento1 = "Tatá"

                mc serio "A primeira que eu vou querer chamar é a mais nova vítima dele. A Tatá."

            elif p9_escolha == 1:

                $ julgamento2 = "Tatá"

                mc serio "A segunda que eu vou querer chamar é a mais nova vítima dele. A Tatá."

            elif p9_escolha == 2:

                $ julgamento3 = "Tatá"

                mc serio "A última que eu vou querer chamar é a mais nova vítima dele. A Tatá."

            $ p9_escolha += 1

            mc "Ela participou de uma reunião recentemente com o grupo, onde o [gus] tambem participou. Eles já estavam cooptando ela."

            eli "Então não foi nada concretizado ainda?"

            mc "Ainda não. Mas ela entendeu o que aconteceu na reunião. Essa reunião inclusive foi idêntica a da [c]."

            eli "Pode ser uma boa falar com ela então. Eu concordo."

        "Miranda" if julgamento1 != "Miranda" and julgamento2 != "Miranda" and julgamento3 != "Miranda":

            if p9_escolha == 0:

                $ julgamento1 = "Miranda"

                mc serio "A primeira que eu quero que você chame é a [a], agente da [c]."

            elif p9_escolha == 1:

                $ julgamento2 = "Miranda"

                mc serio "A segunda que eu quero que você chame é a [a], agente da [c]."

            elif p9_escolha == 2:

                $ julgamento3 = "Miranda"

                mc serio "A última que eu quero que você chame é a [a], agente da [c]."

            $ p9_escolha += 1

            mc "Ela entrou nesse rolo junto com a [c] e agora trouxe a Tatá também. Ela pode ser até cúmplice do caso se você for pensar..."

            mc "Só que ela também só queria uma vida melhor pra ela e pras modelos. Ela não merece pagar igual ele."

            eli "Se ela aceitar denunciar ele, podemos fazer um acordo e livrar ela de uma pena maior."

            mc "Seria perfeito."

        "Eu" if julgamento1 != "[mc]" and julgamento2 != "[mc]" and julgamento3 != "[mc]":

            if p9_escolha == 0:

                $ julgamento1 = "[mc]"

                mc envergonhado "O primeiro a acabar com o [gus] precisa ser eu. Eu quero que você me chame."

            elif p9_escolha == 1:

                $ julgamento2 = "[mc]"

                mc envergonhado "O segundo a acabar com o [gus] precisa ser eu. Eu quero que você me chame."

            elif p9_escolha == 2:

                $ julgamento3 = "[mc]"

                mc envergonhado "Quem vai selar o caixão desse maldito precisa ser eu. Eu quero que você me chame."

            $ p9_escolha += 1

            mc bravo "Você tem que me chamar. [mcc]. O [gus] precisa ouvir de mim."

            eli "Veja... você pode odiar essa pessoa, mas se você não tiver uma informação nova sobre o caso, não adianta."

            eli "Você tem certeza que pode ajudar no caso?"

            mc "Com certeza. Eu quero tá no meio quando a gente mandar ele pra cadeia. Eu não ia aguentar se eu não tivesse."

            eli "Se você objetivamente acredita que pode ajudar, então eu chamarei você."

    if p9_escolha <= 2:

        eli "Perfeito. Agora eu preciso que você escolha outra pessoa."

        jump priscila_e9_escolha
    else:


        eli "Muito bem... essas serão as pessoas."

    mc serio "Sim. Eu tô certo que elas vão ajudar."

    eli "Era isso que eu precisava. Eu espero que você tenha feito boas escolhas, porque o resultado do julgamento dependerá disso."

    mc envergonhado "Eu dei o meu melhor... vamos esperar o resultado agora."

    eli "A audiência será em breve. Eu vou anotar as informações pra você. Sua presença será de suma importância."

    mc charmoso "Pode deixar. Estarei aqui."

    scene juiza sofa4 with Dissolve(1.0)

    eli "Isso... bom garoto..."

    mc desconfiado "H-hm? Senhora?"

    eli "Você é muito bom em obedecer ordens, sabia? E eu adoro pessoas que sabem o seu lugar."

    if v20_fim:

        "Ah, não... tá acontecendo igual no outro dia..."

        eli "Lembra quando você foi um bom cachorrinho da última vez? Tão obediente..."

        mc envergonhado "..."

    eli "Você quer ganhar um biscoitinho, meu cachorrinho? Você só precisa fazer o que eu falar. Igual tava fazendo até agora."

    mc surpreso "!"

    if v20_fim:

        "Será que eu aceito ser o cachorrinho dela?"

    "Pode ser que isso ajude no caso do [gus], mas eu não sei..."

    "Ou quem sabe eu posso transar com ela depois... se eu for um bom garoto..."

    "Ou eu preciso colocar a cabeça no lugar e sair daqui o quanto antes!"

    menu:
        "{i}Au au{/i}":


            mc charmoso "{i}Au au{/i}"

            eli "Assim mesmo, meu totó."

            scene juiza sofa6 with Dissolve(1.0)

            eli "Como eu gosto de um cachorrinho obediente."

            "Como eu vim parar nessa situação?"

            eli "Agora você vai fazer a mamãe se sentir bem e depois você ganha seu presentinho. Você entendeu? Late pra mim."

            mc charmoso "{i}Au au{/i}"

            "Não sei por que, mas essa brincadeira mexe comigo também..."

            eli "Isso mesmo."

            scene juiza sofa8 with Dissolve(1.0)

            pause

            eli "Sua dona tá pronta."



            eli "Pode me cheirar, totó."

            eli "Cheira sua dona, pra você não esquecer."

            mc "..."

            eli "Isso mesmo. É gostoso, né? Tá com vontade de lamber ele, tá?"

            "Até onde essa mulher vai querer ir..."

            label pri9_premium2:

                pass

            eli "Que foi? Tô esperando uma resposta. Não faça sua dona esperar."

            menu:
                "Lamber o pé dela":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_8

                        jump pri9_premium2

                    mc "S-sim, senhora."

                    scene black with dissolve

                    scene pri9_img10 with dissolve

                    pause

                    eli "Eu quero que você lamba o pé dela direitinho. Bem devagar..."

                    eli "Passa a língua em todos os cantinhos e coloca ele inteirinho na boca. Acho bom você fazer um bom trabalho."

                    mc "S-sim..."

                    eli "Eu quero ouvir direito, animal."

                    mc "Sim!"

                    eli "Você não quer sofrer as consequências de ver sua dona brava, né?"

                    mc "N-não..."

                    eli "Isso... se você fizer direitinho, eu te dou o outro pra brincar também..."

                    window hide

                    pause

                    eli "Isso... enfia na sua boca, cachorrinho!"

                    eli "Você mereceu seu prêmio. Eu vou deixar você brincar com outra coisa agora."

                    eli "Vem aqui lamber a buceta da sua dona, vem. E você só vai parar quando eu mandar."

                    "E depois? Será que eu vou me dar bem também?"

                    mc "S-senhora... depois eu t-"

                    eli "Bah! Eu não quero ouvir nada. Você é só um cachorro e não tem vontade aqui."

                    eli "Agora vem aqui e olha pra ela."

                    menu:
                        "Apenas obedecer":


                            mc "Sim, senhora."

                            scene pri9_img11 with Dissolve(1.0)

                            eli "O que você achou? Ela é linda, né?"

                            mc "S-"

                            eli "Cala a boca. Só late."

                            mc "{i}Au au{/i}"

                            eli "Você tá excitado pra lamber ela, tá? Quer enfiar sua língua dentro dela, doguinho?"

                            eli "Primeiro olha bem. Você vai curtir bem devagarzinho... até a sua dona gozar na sua cara."

                            eli "Não consegue aguentar, né? Você é só um animal. Esse cheiro tá deixando louco?"

                            eli "Então vai. Pode se divertir, garoto. Lambuza a sua senhora."

                            window hide

                            pause

                            scene pri9_img12 with Dissolve(1.0)

                            pause

                            eli "Hmm... assim... com vontade..."

                            eli "Você é um cachorro no cio. Você quer devorar esse buraquinho."

                            eli "Mas você não pode. Você só pode lamber ele com essa língua suja."

                            eli "Se você tentar estuprar sua dona, você vai apanhar muito. Você vai ter que se segurar."

                            mc "{i}slup shluup{/i}"

                            eli "Assim mesmo. Devora ela com essa boca. É pra isso que você serve, seu animal. Pra fazer sua dona gozar."

                            eli "Nhg... ai..."

                            eli "Sua língua não é suficiente, inútil. Eu vou ter que me estimular aqui atrás."

                            eli "Você não serve pra nada mesmo, imprestável."

                            scene pri9_img13 with Dissolve(1.0)

                            pause

                            eli "Assim... continua..."

                            eli "Eu vou enfiar meus dedos aqui atrás e você enfia essa língua na frente. Ahn..."

                            eli "Ai... ah... isso..."

                            eli "Eu tô chegando lá, cachorro. Sua língua é boa. E meu cu tá cheio."

                            eli "Continua... ahnn... continua assim..."

                            eli "Isso! Enfia mais fundo! Mas forte, idiota!"

                            eli "Vai! Assim!"

                            eli "Ahn! Tá vindo!"

                            eli "Agora toma tudo!"

                            scene pri9_img14 with vpunch

                            pause

                            "E-euh! Q-que é isso?!"

                            eli "Toma aqui! Toma tudo da sua dona!"

                            menu:
                                "Ficar parado":


                                    "Eu tenho que aguentar!"

                                    mc "Hmmmff!"

                                    eli "Isso! Toma todo o meu suco!"

                                    eli "Aaahh! Bom garoto!"

                                    eli "Agora vem me limpar, totó. Vem, cachorrinho."

                                    menu:
                                        "Limpar o mijo da buceta dela":


                                            mc "Tudo o que você mandar, senhora. Eu tô aqui pra fazer o que você quiser."

                                            eli "Vem, garoto... obedece direitinho."

                                            scene black with dissolve

                                            scene ani20 with Dissolve(1.0)

                                            pause

                                            mc "Obedeço, senhora. Vou te deixar limpinha. Ser um bom garoto."

                                            eli "Hmmm... esse garoto merece uma boa recompensa... ah..."

                                            eli "Ele sabe se comportar. Merece muito carinho e amor..."

                                            mc "Mereço? Eu só... faço o que a senhora manda."

                                            eli "Exatamente. Não faz mais que a obrigação, cachorro... hmm..."

                                            eli "Mas limpando minha xota desse jeito... ah... com tanta vontade..."

                                            eli "Você aprendeu direitinho... uuhnnn..."

                                            eli "Se continuar devorando minha buceta suja desse jeito eu vou te dar muita porra de presente."

                                            mc "Me dá... nngh..."

                                            eli "Você quer, não quer?"

                                            mc "Quero!"
                                        "Terminar o serviço aqui mesmo":


                                            pass

                                    mc "Só goza, senhora!"

                                    mc "Mela minha boca!"

                                    eli "Nnghhh! NNGHHH!"

                                    eli "Que gozada boa!"

                                    eli "Agora vem aqui e deita. Você mereceu um carinho."

                                    "S-sério?"

                                    scene black with dissolve

                                    eli "Pega as poltronas e arruma elas uma virada pra outra."

                                    mc "Assim?"

                                    eli "Isso... agora deita."

                                    scene pri9_img15 with Dissolve(1.0)

                                    pause

                                    eli "Eu vou te dar a honra de usar o meu pé pra você se satisfazer."

                                    eli "Acho bom você me agradecer, coitado."

                                    mc "V-valeu..."

                                    eli "Só isso? Agradece de verdade, corno."

                                    mc "Obrigado, s-senhora!"

                                    eli "Melhorou um pouco..."

                                    "Eu me sinto um nada perto dessa mulher..."

                                    "Como ela consegue fazer isso? Me dominar desse jeito?"

                                    eli "Tá aproveitando, coisinha? É bom sentir meu pé no seu pintinho de nada?"

                                    mc "É..."

                                    eli "Ele é tão pequeno... não serve pra nada. Isso nunca vai dar prazer pra ninguém."

                                    mc "..."

                                    eli "Ele merece ser pisado! Só isso! Que pinto inútil!"

                                    mc "A-ah!"

                                    eli "Que foi isso? Doeu ou você gemeu? Você gosta mesmo de ser humilhado, hein?"

                                    mc "..."

                                    eli "Eu vou começar a mexer. Acho bom você gozar logo."

                                    scene pri9_img16 with Dissolve(1.0)

                                    pause

                                    "Tá gostoso mesmo ela esfregando o é no meu caralho..."

                                    eli "Você tá gostando. Não é possível. Como um homem pode ser tão fraco? Você não tem bolas?"

                                    mc "S-senhora..."

                                    eli "Cala a boca! Só aproveita esse seu pau minúsculo pra alguma coisa! Goza logo!"

                                    mc "S-sim..."

                                    eli "Eu tô gostando de ver você com essa cara de sofrimento. Agora goza!"

                                    mc "A-ah! Hm!"

                                    eli "Goza em você mesmo, seu inútil!"

                                    eli "Goza enquanto eu piso em você!"

                                    scene pri9_img16 with vpunch

                                    mc "A-aaaah!"

                                    eli "Isso! Que delícia..."

                                    scene pri9_img17 with vpunch

                                    eli "Ufa!"

                                    eli "Você é imprestável mesmo... gozando desse jeito... igual uma garotinha..."

                                    eli "Sua sorte é que eu consegui gozar. Pelo menos pra isso você serviu."

                                    mc desculpa "..."

                                    eli "Você fez o que tinha que fazer. Aposto que você gostou também."

                                    eli "Não tem coisa mais fraca e rídicula que um homem que não admite suas vontades."

                                    eli "Toma vergonha na cara e assume suas taras!"

                                    mc "S-sim..."

                                    eli "Agora se manda! E vê se aprende logo que na mão de um alfa de verdade, você não é nada."

                                    mc preocupado "..."

                                    eli "E quando quiser se humilhar de novo... sabe onde me encontrar."

                                    mc "..."
                                "Se afastar":


                                    mc "N-não!"

                                    scene black with vpunch

                                    mc "{i}cof cof{/i}"

                                    mc "Que nojento! Isso é demais!"

                                    scene pri9_img17 with vpunch

                                    eli "HAHAHA!"

                                    eli "Você é imprestável mesmo... nem pra aguentar uma coisa simples dessas..."

                                    eli "Sua sorte é que eu consegui gozar. Pelo menos pra isso você serviu."

                                    mc serio "Você podia ter avisado... eu não queria chegar nesse ponto."

                                    eli "Você fez o que tinha que fazer. Aposto que você gostou também. Só não quer admitir."

                                    eli "Não tem coisa mais fraca e rídicula que um homem que não admite suas vontades."

                                    eli "Parece aqueles idiotas que ficam o dia todo falando mal de homossexual daí chega em casa e vão se masturbar pra trans."

                                    eli "Toma vergonha na cara e assume suas taras!"

                                    mc irritado "Hnf..."

                                    eli "Agora se manda! E vê se aprende logo que na mão de um alfa de verdade, você não é nada."

                                    mc preocupado "..."
                        "Parar e dar o fora":


                            mc envergonhado "D-desculpa, senhora. Mas isso é demais."

                            eli "Que cahorrinho desobediente. Eu vou lembrar da sua escolha, seu otário desprezível."

                            eli "Se você não vai parar no meio assim, então pode deixar minha sala."

                            mc "P-pode deixar. Valeu por tudo."

                            eli "Até mais, au au..."
                "D-desculpa, não posso":


                    mc envergonhado "D-desculpa, senhora. Mas isso é demais."

                    eli "Que cahorrinho desobediente. Eu vou lembrar da sua escolha, seu otário desprezível."

                    eli "Se você não vai parar no meio assim, então pode deixar minha sala."

                    mc "P-pode deixar. Valeu por tudo."

                    eli "Até mais, au au..."
        "Acho melhor eu ir agora...":


            mc envergonhado "S-senhora... acho melhor eu ir embora..."

            eli "Tem certeza? Vai ficar sem o seu biscoitinho?"

            mc "Acho que sim... m-mas quem sabe outro dia..."

            eli "É uma pena ver um cachorrinho tão obediente indo embora... mas você pode voltar quando quiser. A mamãe vai te receber."

            mc "P-pode deixar. Valeu por tudo."

            eli "Até mais, au au..."

    scene black with dissolve

    "Essa mulher..."

    "Parece que todo mundo nessa cidade tem alguma coisa de anormal..."

    "S-será que eu também..."

    jump priscila_e9_final

label priscila_e9_final:

    "..."

    $ tempo = 3
    $ v53_fim = True

    scene mc parque_sentado_noite with Dissolve(2.0)

    pause

    "Então realmente vai ter um julgamento... e o resultado vai depender de mim também."

    "Eu nunca fiz algo tão grande assim na minha vida."

    "Eu sempre me senti tão fraco nessa cidade. Tem gente gigante, armada, rica, influente. E eu não tenho nada disso."

    "Mas agora eu posso ser o responsável por condenar um figurão conhecido no mundo todo."

    "Até uns meses atrás eu só queria um trabalho e não voltar pra casa da minha família. E agora eu tô ameaçando o status quo."

    if no3_tony:

        "Ou ajudando o status quo já que eu tô do lado do [to]... dá pra acreditar nisso?! Eu tô com a máfia!"

    "Eu tô começando a achar que eu tenho um futuro aqui mesmo."

    "E tem a [c] também... eu não vi e nem falei com ela nenhuma vez. Eu não tive coragem de ligar pra ela..."

    "Ela não me ligou também... o clima tá horrível."

    "Esse julgamento vai mudar tudo. E vai ser daqui 7 dias!"

    "Não só o destino da Pri vai tá em jogo, mas o meu também... o do [gus], da [ag], da Tatá, da [a]..."

    "Eu nunca imaginei que um zé ruela que nem eu ia tá no meio de um furacão desses. Tomara que tudo dê certo..."

    scene black with dissolve

    pause

    "Mas por hoje tá bom. Melhor voltar pra casa e dormir."

    "Eu sinto que essa semana vai demorar pra passar..."

    jump priscila_e9_pre_julgamento



label priscila_e9_pre_julgamento:

    $ dia += 7
    $ tempo = 1

    "..."

    scene ape_geral with Dissolve(2.0)

    "Finalmente o dia! Eu sinto que a semana passou voando!"

    "E mais uma semana sem conseguir falar com a Pri. Eu queria tá perto dela, poder ajudar com isso, mas ela não ligou. Nem eu liguei."

    if priscila_namoro:

        "A gente tá namorando, mas nem parece. Só deu encrenca desde que a gente começou."

        "Tirando um beijo aqui e ali, a gente nem conseguiu curtir ainda."

        if praia_priscila_local:

            "Pelo menos aquele encontro na praia só nós dois foi bacana. Ela posou pra mim e talz, mas só!"
    else:


        "Ela me disse que eu sou o melhor amigo dela. E ela não poder contar com ele agora... Isso é triste."

    "Eu não sei o que eu poderia tá fazendo por ela."

    "Pra mim, se o [gus] for ou não preso, eu quero que ela seja feliz. Que ela fique bem."

    "Mas eu não posso enrolar agora. Hoje é o dia que tudo vai ser decidido."

    if julgamento1 != "[mc]" and julgamento2 != "[mc]" and julgamento3 != "[mc]":

        "Eu não vou depor, mas eu vou tá lá pra ver o que vai dar."
    else:


        "Eu vou depor também... por que raios eu acabei escolhendo eu mesmo? O que será que ela vai me perguntar?"

    if p9_juiza:

        "Quando a [eli] pediu minha ajuda, passou tanta coisa na minha cabeça. Como eu vou saber quem vai ou quem não vai ajudar?"
    else:


        "Eu falei com o [to], ele me garantiu que não importa o resultado a coisa vai ser tranquila pra mim."

        "Esse é o lado bom de tá do lado de quem manda na cidade."

    "Agora... o que vai acontecer com o [gus] é o que mais mexe comigo. Esse velho fez o que queria com a [c], com a [ag]... e sabe lá quantas."

    "Esse cara tem que pagar pelo que ele fez. Independente do meu lado nisso tudo, e do meu próprio interesse na história, uma coisa eu sei."

    "Esse velho tarado tá errado. Usar seu poder pra fazer o que quiser com garotas encurraladas. Isso não pode sair impune."

    if not p9_juiza:

        "Mesmo eu ficando do lado do [to], é impossível falar que esse cara tá certo. Eu nunca vou fazer uma coisa dessas."

    "Caralho! Olha a hora."

    "Tenho que ir."

    scene black with dissolve

    call locomocao from _call_locomocao_5

    scene cidade centro9 with Dissolve(1.0)

    pause

    "Não tem ninguém aqui fora. Eles realmente conseguiram despistar a mídia nessa."

    "Se é que a Faux ia querer cobrir isso. Se eles tão com os poderosos, então eles querem abafar isso o máximo."

    "E no caso da nossa revista, a [w] nunca iria aceitar publicar uma notícia que atrapalharia as autoridades."

    "Desde que ela chegou, as coisas mudaram na revista. Só a [j] continua fazendo o que bem entende."

    scene black with dissolve

    "..."

    scene tribunal_p9 with Dissolve(1.0)

    pause

    "Tem algumas pessoas... Um policial ali... Mas nada da Pri."

    "Falta trinta minutos pro horário e não tem um cristo que eu conheço aqui. Será que eu vim na hora certa?"

    "???" "Vejam só... se não é o caipira. Incrível como parece que ninguém liga para a entrada de ratos no lugar."

    mc desconfiado "Hm? Tá falando comigo?"

    scene p9_img13 with Dissolve(1.0)

    pause

    gus "Com quem mais seria?"

    "[gus]!"

    menu:
        "Com licença. Vou sair daqui.":


            mc desculpa "Eu não tenho que ficar te ouvindo aqui. Vou sentar em outro lugar. Com licença."

            gus "Ei. Espera, garoto. Eu ainda tenho o que falar com você."

            mc "O que foi?"

            gus "Isso. Eu prefiro animais domesticados."

            mc serio "..."
        "Só se for você, velho tarado.":


            mc tarado "Só se for você, velho safado. Se bem que você tá mais pra um cachorro no cio."

            gus "Olha como você fala comigo, verme."

            mc bravo "Olha você."

            to "[gus], por favor. Estamos no tribunal. Esse garoto não tem nada a perder aqui, você tem."

            gus "Isso é o que veremos. Eu acho que tem muita coisa em jogo hoje."

            to "Só tente chamar menos atenção."

            gus "E você pare de achar que tem algum poder sobre mim."

            to "..."

    gus "Eu quero deixar apenas uma coisa clara."

    if p7_gustav:

        gus "Aposto que você se divertiu muito imaginando este dia quando resolveu publicar aquela matéria."

        mc charmoso "Eu só fiz o que qualquer pessoa ética faria."
    else:


        gus "Eu sei que tem dedo seu naquela matéria que saiu na sua revista. Tudo isso aqui é culpa sua também."

        mc serio "Eu não tenho nada a ver com isso. Eu sou só um pauteiro da revista."

        gus "Você pensa que me engana, fedelho?"

    gus "Mas pode tirar o cavalo da chuva. Tudo isso aqui é uma encenação, ouviu?"

    mc serio "..."

    gus "O resultado do 'julgamento' já foi decidido. Não importa o que aconteça aqui, eu vou estar livre no fim do dia."

    gus "A Justiça não é cega, pivete. Ela foi criada para que pessoas como eu possam controlar pessoas como você."

    gus "Mas a criatura não se volta contra o criador. Nem hoje e nem nunca."

    gus "E, lembre-se disso! Eu vou atrás do responsável por aquela matéria. Ah, se eu vou!"

    gus "Alguém vai pagar por tudo isso aqui."

    to "[gus]... por favor."

    gus "Merda, [to]! Da próxima vez eu quero só o [mar] comigo!"

    mar "..."

    gus "Tudo bem. Eu já terminei. Adeus, idiota."

    menu:
        "Aproveite a liberdade enquanto pode.":


            mc tarado "Isso. Fala bastante, velho. Aproveita bem a liberdade enquanto você pode. Amanhã você vai ver o Sol nascer quadrado."

            gus "..."

            gus "Minha vontade é meter um tiro nesse pirralho agora mesmo! [mar]!"

            to "[gus]! Por favor! Venha..."

            gus "Você vai ver... você vai ver..."
        "...":


            "Eu não tenho o que falar pra esse velho ridículo."

            gus "..."

    scene black with dissolve

    scene tribunal_p9 with Dissolve(1.0)

    "Esse velho..."

    "Guarda" "Senhor!"

    mc desconfiado "Hm? Eu?"

    "Guarda" "O senhor pode vir até aqui por favor. O senhor está sendo chamado."

    mc preocupado "Ok..."

    scene black with dissolve

    "Guarda" "Por favor. Passe por esta porta até a área de trás, por favor."

    "..."

    "Será que a [eli] quer falar comigo de novo? Será que é sobre os depoimentos?"

    "???" "Oi."

    mc desconfiado "Quê?"

    mc surpreso "QUÊ?!"

    scene p9_img15 with Dissolve(1.0)

    pause

    c "Oi..."

    mc surpreso "P-p-p-p---- Priscila!"

    c "{i}Rsrs{/i}"

    c "Você continua com esse jeito até hoje, né?"

    menu:
        "Que nada. Eu mudei muito.":


            mc charmoso "Que nada. Eu mudei muito."

            c "É verdade... desculpa."

            mc "Não precisa. Mas que eu mudei eu mudei. Olha onde a gente tá."

            c "Sim..."
        "Sei lá...":


            mc envergonhado "Não sei do que você tá falando."

            c "Você continua tão fofo quando eu te conheci."

    c "Parece que faz um século que a gente se viu, né?"

    mc normal "Sim. Deve fazer menos tempo do que parece. Dá a impressão que foi uma eternidade."

    c "Faz... [dia] dias que eu te conheci."

    mc envergonhado "Haha... acho que foi um dia a mais."

    c "Não tô brincando. Faz esse tempo mesmo. Eu contei."

    mc desconfiado "Sério? Você realmente contou o tempo que a gente se conheceu?"

    c "É estranho demais? Falando assim, parece estranho mesmo..."

    menu:
        "Não é estranho. É fofo.":


            mc charmoso "Não é nada estranho. É fofo e incrível."

            mc "Eu me sinto honrado de nosso encontro ter sido tão marcante pra você, assim."

            c "Obrigada..."
        "É um pouco estranho...":


            mc envergonhado "É... assim... parece que você tá me perseguindo, né?"

            c "D-desculpa... eu não devia ter falado isso."

            mc "Haha..."

    c "O dia que a gente se conheceu foi muito importante pra mim. Aquela noite no bar. Você ainda lembra?"

    mc normal "Claro. Como se fosse ontem."

    if priscila_e1 == "seducao":

        c "Eu ainda não acredito que a gente fez aquilo logo no primeiro encontro..."

        mc "Aquilo já me disse que você era uma garota diferente. Eu fiquei super com vontade de conhecer você."

    c "Aquela noite foi quando eles me falaram qual era... o próximo passo da minha carreira."

    mc desculpa "Sei..."

    scene p9_img14 with Dissolve(1.0)

    pause

    c "Acho que foi o dia que tudo começou a dar problema pra mim."

    mc "Não pensa nisso... Ainda mais hoje."

    c "É... mas... também foi quando eu conheci você. É incrível como aquele dia aconteceram coisas tão diferentes."

    c "Uma tão ruim e uma tão boa. Eu fico pensando bastante nisso."

    if priscila_namoro:

        c "O dia que eu conheci meu namorado e também o dia que eu decidi... fazer o que eu fiz."

        mc desculpa "..."

    mc "A vida parece que não faz sentido às vezes."

    c "É! Eu acho isso também..."

    mc normal "E como você tá? Tipo, com tudo isso que tá acontecendo?"

    c "Foi tudo tão rápido..."

    if p7_gustav:

        c "Eu não imaginei que você ia contar tudo... pra todo mundo desse jeito..."

        mc desculpa "..."
    else:


        c "Foi você que deu tudo pra sua revista publicar, né? Eu sei que não foi você que escreveu, mas foi você que falou, não foi?"

        mc desculpa "Sim..."

    "Ela sabe. Claro que que ela sabe..."

    menu:
        "Eu fiz pra te salvar.":


            mc preocupado "Eu juro que eu fiz isso pra te salvar. Pensando em livrar você dessa vida!"

            c "Mesmo depois que eu disse que ia querer fazer mais um filme?"

            mc "Eu pensei nisso, mas pra mim era o certo!"

            c "Você fez o que era o certo pra você. E o que era o certo pra mim, [mc]?"

            mc desculpa "Eu... eu tinha que seguir a minha cabeça. Eu não acho que eu fiz errado. Foi com a melhor das intenções."

            c "Eu acredito... você não ia querer me prejudicar."
        "Desculpa... eu fui egoísta.":


            mc preocupado "Desculpa. Eu sei que você não queria isso. Você disse que ia querer continuar trabalhando no filme."

            mc "Mesmo assim eu fui lá e joguei sua história na roda. Eu juro que eu fiz pensando em te ajudar, mas eu não tinha direito."

            c "[mc]... se você sabia disso... então por que fez isso?"

            mc "Não sei. Acho que eu só não pensei. Você tava em sofrimento, Pri."

            if priscila_namoro:

                mc angustiado "Você é minha namorada, caralho!"

                c "!"

            mc "Eu só queria que você fosse feliz... só isso!"

            c "..."
        "É... eu fiz.":


            mc charmoso "É... eu fiz o que eu achei que eu tinha que fazer."

            c "Eu fiquei assustada. Eu não achei que você ia fazer isso."

            mc "Eu mudei, né?"

            c "É... mudou mesmo."

    mc desculpa "..."

    mc concentrando "Olha. Será que eu posso falar uma coisa sobre isso?"

    c "Sim. Claro..."

    mc preocupado "Eu sei da sua história. Eu conversei com a [a] mais de uma vez sobre isso."

    mc "Eu sei que vocês vieram do nada. E que você não queria voltar pra lá."

    mc desculpa "Mas eu fico pensando se tudo isso vale a pena, sabe?"

    mc preocupado "Eu sei que essa é uma conclusão que você tinha que chegar sozinha..."

    if p7_gustav:

        mc bravo "Mas eu não consegui deixar esse velho impune. Ele merece apodrecer na prisão, [c]!"

        mc desculpa "Eu sei que eu passei por cima de você. Mas eu tinha que fazer isso. Eu não ia aguentar."

        mc serio "Eu sei que você pode não me perdoar por isso. Mas eu juro que eu pensei em você."

        mc preocupado "Eu vi você sofrendo muito desde que a gente se conheceu. E é tudo culpa dele."

        mc "Eu sei que você tem seus objetivos, mas esse cara vai fazer você sofrer e muitas outras depois de você."

        mc angustiado "Alguém precisa fazer alguma coisa! Se não for agora, talvez seja nunca!"

        c "Você pode tá certo, [mc]. Mas deixa eu te falar uma coisa..."

        mc preocupado "Por favor. Eu quero ouvir tudo."
    else:


        mc "E foi por isso que eu decidi não entregar o [gus]. Eu não queria que isso aqui tivesse acontecido."

        mc "Eu cheguei na conclusão que eu não podia entregar ele e jogar tudo o que você tinha passado no lixo."

        mc "Se você queria continuar, eu tinha que aceitar. E foi isso que eu fiz."

        mc "As informações que usaram realmente foi eu que deixei com o chefe. Mas não era pra terem usado."

        mc "Eu juro pra você que não era minha intenção."

        c "[mc]... e-eu..."

        c "Eu acredito em você. Obrigada. Obrigada por entender isso."

    scene p9_img16 with Dissolve(1.0)

    c "Eu vim de uma cidadezinha. Eu era toda da minha família. Eu vivia pra ajudar meus pais..."

    c "Eu nunca tive uma coisa minha. Eu nunca fui ninguém. Nunca ninguém olhou pra mim e disse 'olha é a [c], o que ela quer?'."

    c "Meus pais nunca perguntaram pra mim o que eu queria. Eu era... um objeto pra eles."

    c "Eu sei que eles me amavam! Eu não quero ser ingrata! Mas eles nunca pensaram no que eu queria."

    c "E daí a [a] veio com essa ideia maluca de virar uma modelo! Pela primeira vez eu tinha uma coisa minha..."

    c "As pessoas me amavam. Eu era a [cc]. Meu nome, [mc]! Todo mundo sabia meu nome! E eles me queriam!"

    c "Eu não posso mais voltar pra aquele lugar. Não posso voltar a ser ninguém."

    mc preocupado "[c]..."

    c "Eles vão tirar tudo de mim e vão me trancafiar naquele lugar de novo. Sem nada meu..."

    c "Eu sei que o [gus] é um cretino. Nunca que eu ia aceitar uma coisa dessas se eles não tivessem minha vida na mão deles."

    c "Eu senti tanto nojo de mim. Mas foi você que me deu força pra fazer o que eu queria. Você me ajudou!"

    c "E foi por isso que eu decidi continuar mais um pouco. Juntar toda a força que eu ainda tenho e passar por esse final."

    c "A [ag] não vai tá no próximo filme. Parece que eles libertaram ela. Comigo vai ser a mesma coisa!"

    c "Mais um filme... mais uns meses aguentando esse cretino! E depois eu vou tá livre!"

    c "Eu vou cunprir meu contrato! Vou receber uma parte de tudo o que eu faturei! Eu vou sair por cima!"

    c "Mas se tudo acabar agora... eu não vou ter nada... E é por isso que... que..."

    c "Eu preciso de você agora."

    mc desculpa "De mim?"

    c "Eu preciso que você me fale, de verdade, o que você acha. Eu preciso de força uma última vez."

    c "Se você me falar que eu tenho que ser forte e aguentar pra viver feliz depois, eu sei que eu consigo."

    if priscila_namoro:

        c "Você aceitou continuar comigo mesmo sabendo de tudo isso. Muito mais do que eu esperava de um namorado."

    c "Nunca uma pessoa ficou do meu lado igual você ficou todos esses [dia] dias. Então... eu preciso de você uma última vez."

    "Eu já falei tanta coisa pra Pri... o que adianta perguntar isso pra mim agora? Ela não faz o que eu falo mesmo..."

    "Só que... ela parece tá precisando... talvez não é bem o que eu falo, mas ela sentir que eu me importo..."

    "Eu queria poder saber o que passa na cabeça das pessoas!"

    c "Por favor, [mc]..."

    "Ok..."

    menu:
        "Faça o que você quiser. Eu cansei.":


            mc desculpa "Sinceramente, Pri, eu acho que a gente já falou muito disso. Tudo o que eu tinha pra falar eu te disse."

            mc preocupado "Eu sei que é uma situação díficl e eu não quero fazer pouco do que você tá passando."

            mc "Mas eu realmente não tenho mais nada pra te falar sobre isso. Só que você deve seguir seu coração."

            mc "A decisão é sua e a consequência das suas ações vai afetar sua vida. Va afetar a de outros também, mas principalmente você."

            mc desculpa "Então eu torço pra que você faça o que você acha certo e boa sorte."

            mc normal "Se você precisar de alguém, eu sempre vou estar aqui pra você."

            if priscila_namoro:

                mc "Eu continuo sendo seu namorado. Por isso, eu quero que você seja feliz, do meu lado."

            mc "Mas fora isso, é com você."

            c "Ai..."

            c "Eu não... não esperava essa resposta vindo de você, [mc]. Mas quem sabe você não tem razão..."
        "Não denuncie. Falta pouco pra acabar.":


            mc desculpa "Eu não acredito que eu vou te falar isso, mas é melhor você só continuar com isso mais um pouco."

            mc "O pior já passou. O [gus] vai ter outra fruta mais fresca pra brincar agora. Vai ser mais fácil pra você."

            c "[mc]... falando assim... tudo parece tão errado..."

            mc bravo "Claro que é errado!"

            c "!"

            mc preocupado "Mas não é você que tá errada. É ele, é tudo isso que tá em volta da gente."

            mc "Aceitar as coisas como são ou perder tudo. Ninguém devia ter que passar uma escolha dessas."

            mc "Mas se é isso que a vida guardou pra você, que você tenha força pra aguentar. Porque uma hora as coisas melhoram."

            c "Você acha isso de verdade?"

            mc desculpa "Não sei se é o melhor... mas depois de tudo, eu comecei a achar que talvez você tenha que só acabar logo com isso."

            c "Então acho que é isso..."

            mc "É isso..."
        "Denuncie ele. Você não vai perder tudo.":


            $ p9_priscila = True

            mc preocupado "Eu não tenho como falar outra coisa pra você, Pri. Você precisa entregar o [gus]."

            mc "Eu sei que você vai perder muito quando o velho tarado cair e eles cancelarem o filme, e podem até acabar com seu contrato."

            c "Eu perderia praticamente tudo... meus contratos... e logo eu ia voltar pra..."

            mc "Eu sei. Mas me escuta. Você não tá mais sozinha. Você tem eu do seu lado."

            mc "Eu prometo que eu vou continuar do seu lado, não importa o que aconteça. Você sabe que eu não ligo pra fama."

            c "Você fala isso agora, mas como a gente pode ter certeza?"

            mc angustiado "Eu prometo! Eu juro! Eu faço o que você quiser. Eu assino um contrato com você!"

            c "Ok, tá! Eu acredito em você... bobo..."

            mc desculpa "Eu acho que depois de toda essa experiência sua vida nunca mais vai ser a mesma, Pri."

            mc "Mesmo sem seus contratos, você não vai voltar pra casa e ser a mesma que você era antes de tudo isso."

            mc "Mesmo que você perca sua fama e as pontes que o [to] construiu pra você, não quer dizer que sua carreira acabou."

            mc normal "Existem novos contratos, novas possibilidades. O mundo é grande e agora você não é mais uma ninguém."

            c "Você acha?"

            mc "Eu tenho certeza!"

            mc desculpa "Eu não posso garantir isso pra você, claro. Mas eu aposto que qualquer marca iria querer ter você."

            c "Mas e o escândalo? Isso vai dificultar tudo, [mc]."

            mc preocupado "Pode ser que sim. Mas pode ser que abra novas portas. Existem celebridades que se recuperaram de coisas assim."

            c "É verdade..."

            mc "Todo mundo sabe que a culpa não foi sua, Pri. O [gus] é o monstro, não você. E muitas empresas vão lembrar disso."

            c "Pode ser... talvez..."

            c "Eu não sei, [mc]. Obrigada pela sua opinião. Eu vou pensar muito."

            mc envergonhado "Desculpa se eu me exaltei. Eu não sei muito desse mundo. Só quero que você seja feliz."

            c "Obrigada... você sempre foi um fofo..."

    scene p9_img17 with Dissolve(1.0)

    c "Eu vou ver o que vai acontecer. Ainda nem sei se eles vão me chamar. Eu vou esperar numa sala aqui atrás."

    mc charmoso "Seja lá o que acontecer, vamos tentar continuar tudo como antes, tá?"

    c "Eu não vejo a hora de poder ter uma vida normal... e a gente pode ir em algum lugar juntos."

    mc "Eu tenho certeza que isso vai acontecer logo logo. Bora passar por isso logo e curtir."

    c "Tomara..."

    mc desculpa "Até daqui a pouco."

    c "Até..."

    if priscila_namoro:

        c "Te amo."

    scene black with dissolve

    mc desculpa "Pri..."

    "..."

    scene tribunal_p9 with Dissolve(1.0)

    pause

    "Falta 5 minutos... nem acredito."

    "Guarda" "Atenção! Por favor, levantam-se para receber a excelentíssima [eli] Richter."

    scene p9_img18 with Dissolve(1.0)

    pause

    eli "Podem se sentar."

    eli "Muito bem. Estamos aqui hoje para audiência requisitada pelo Ministério Público com o intuito de justificar a abertura de ação."

    gus "Juíza, se permite. Esta formalidade é desncessária."

    eli "Senhor [gus], por favor, mantenha-se calado em meu tribunal a não ser que eu diga o contrário."

    gus "Ju-"

    eli "Senhor [gus]! Por favor, eu não quero ter que prender o senhor por desacato."

    gus "..."

    eli "Tenho que lembrar o senhor que não existe ação contra sua pessoa por parte dos promotores. O senhor não está sendo julgado."

    eli "Esta audiência é uma reunião para decidir quanto a uma possível abertura de inquérito e investigação."

    eli "Como não foi apresentada queixa formal contra o senhor, o Ministério Público não deve abrir nada contra o senhor."

    eli "Entretanto. Devido à cobertura midiática que a matéria trouxe para a população, é de praxe realizarmos este ritual."

    eli "Vamos ouvir o depoimento de pessoas que estariam envolvidas e deliberar se existe ou não razão para abrir um processo contra você."

    eli "Como ainda não existe ação contra o senhor, não há necessidade de presença de advogados e nem de promotores."

    eli "Serão apenas o senhor, as possíveis testemunhas e eu, responsável pela decisão de abrir ou não."

    eli "Garanto-lhe que tudo será feito conforme determina a Lei."

    eli "Dito isto, vamos dar início ao processo."

    eli "A matéria publicada em revista de alcance nacional menciona que o senhor poderia estar envolvido em casos de abuso de atrizes."

    eli "A matéria cita nominalmente a profissional [cc], mas diz que outras atrizes sofreram o mesmo tipo ataque, que é uma prática recorrente."

    eli "O que o senhor tem a dizer sobre os fatos relatados na matéria?"

    scene p9_img19 with Dissolve(1.0)

    pause

    gus "Senhora juíza, eu declaro que a matéria foi irresponsável e mentirosa. Nada do relatado na revista aconteceu em nenhum grau."

    gus "Inclusive, tomarei medidas drásticas contra todos os envolvidos."

    scene p9_img18 with Dissolve(1.0)

    eli "Muito bem. Em face da premissa de que todo acusado é inocente antes que se prove o contrário, você será considerado inocente."

    gus "Claro... foi o que eu disse..."

    eli "O próximo passo é chamar outras pessoas que estariam envolvidas de acordo com a mesma matéria."

    eli "Gostaria de chamar para o púlpito o primeiro depoente."

    if not p9_juiza:

        $ julgamento1 = "Priscila"
        $ julgamento2 = "Ágata"
        $ julgamento3 = "Tatá"

label priscila_e9_depoimentos:

    if p9_depoimentos == 0:

        pass

    elif p9_depoimentos == 1:

        eli "Temos que dar prosseguimento. A audiência deve ser rápida."

        eli "Vou convocar agora minha segunda depoente."

    elif p9_depoimentos == 2:

        eli "Eu peço a atenção de todos para que possamos continuar."

        eli "Eu tenho uma última pessoa que desejo ouvir antes de tomar minha decisão."

    elif p9_depoimentos == 3:

        jump priscila_e9_resultado

    $ p9_depoimentos += 1

    if p9_depoimentos == 1:

        if julgamento1 == "Priscila":

            jump p9_depoimento_priscila

        elif julgamento1 == "Ágata":

            jump p9_depoimento_agata

        elif julgamento1 == "Tatá":

            jump p9_depoimento_tata

        elif julgamento1 == "Miranda":

            jump p9_depoimento_miranda

        elif julgamento1 == "[mc]":

            jump p9_depoimento_mc

    elif p9_depoimentos == 2:

        if julgamento2 == "Priscila":

            jump p9_depoimento_priscila

        elif julgamento2 == "Ágata":

            jump p9_depoimento_agata

        elif julgamento2 == "Tatá":

            jump p9_depoimento_tata

        elif julgamento2 == "Miranda":

            jump p9_depoimento_miranda

        elif julgamento2 == "[mc]":

            jump p9_depoimento_mc

    elif p9_depoimentos == 3:

        if julgamento3 == "Priscila":

            jump p9_depoimento_priscila

        elif julgamento3 == "Ágata":

            jump p9_depoimento_agata

        elif julgamento3 == "Tatá":

            jump p9_depoimento_tata

        elif julgamento3 == "Miranda":

            jump p9_depoimento_miranda

        elif julgamento3 == "[mc]":

            jump p9_depoimento_mc

    label p9_depoimento_priscila:

        eli "Pivô dos acontecimentos, seria impossível não chamarmos a modelo e atriz [cc]."

        eli "A matéria cita ela como a atual vítima do senhor [gus] Aldebaran."

        eli "A verdade teria sido confidenciada fora de uma entrevista oficial, mas o nome dela foi citado mesmo assim."

        eli "Oficial. Por favor, traga a senhorita [cc]."

        scene black with dissolve

        "..."

        scene p9_img20 with Dissolve(1.0)

        pause

        eli "Senhorita [c]. Posso chamar a senhorita de [c]?"

        c "T-tudo bem."

        eli "Não precisa ficar assustada, minha querida. Esta nossa reunão não passa de uma formalidade. Não é um julgamento."

        c "N-não é?"

        eli "Não. Não vai ter advogado te fazendo perguntas e nem nada. Esse é apenas um processo inicial."

        eli "Queremos apenas saber se vale ou não abrirmos um processo contra o senhor [gus] Aldebaran."

        c "E-entendi."

        eli "Por isso não precisa se preocupar. Eu serei a única a te fazer perguntas. E será apenas uma."

        eli "É importante que você entenda que neste processo você não precisa falar a verdade."

        c "Como é?"

        eli "Diferente de um julgamento real, onde seria condenável mentir sob juramento, aqui você pode se sentir livre para mentir."

        c "..."

        eli "Entretanto, eu recomendo que você seja sincera. Ninguém aqui tem nada contra sua pessoa."

        eli "A verdade, por mais difícil que seja, sempre é mais limpa e mais ética. É o que eu faria se estivesse em seu lugar."

        c "Certo. Acho que eu entendi."

        eli "Muito bem. O que eu tenho que te perguntar é o seguinte."

        eli "A principal informação contida na matéria que originou este impasse são os abusos que você teria sofrido."

        eli "O perpetuador seria o diretor [gus] Aldebaran e ele o faria durante as gravações do seu filme mais recente."

        eli "Filme esse do qual você é a atriz principal. Você teve acesso a matéria?"

        c "S-sim, meretíssima."

        eli "Pois bem. Deixando de lado outras informações da matéria, que podem ou não ser corretas. Só quanto a esse detalhe principal."

        eli "A informação contida na matéria é verdadeira? Os abusos que você teria sofrido. A matéria é verídica neste ponto específico?"

        c "E-eu..."

        eli "Pense com calma e leve o tempo que precisar. Responda quando estiver pronta."

        c "..."

        scene p9_img21 with Dissolve(1.0)

        pause

        c "Eu vou ser s-sincera com a senhora."

        c "Essa parte da matéria da matéria... é..."

        c "Mentira."

        eli "A senhorita está certa sobre isso?"

        c "S-sim."

        eli "Muito bem. Isso era tudo, senhorita [c]."

        c "S-só isso?"

        eli "Sim. Pode ir voltar para a sala e se preparar para sair."

        c "Ok."

        show black with dissolve

        pause

        c "Ah. Juíza."

        hide black with dissolve

        eli "Sim?"

        if p9_priscila and priscila_namoro:

            $ julgamento_sucesso += 1

            scene p9_img21 with Dissolve(1.0)

            pause

            c "Eu... acho que eu quero falar mais um pouco. Eu posso?"

            eli "Fique à vontade, senhorita [c]."

            c "É... isso não tem muito a ver com o que você perguntou. Mas quem sabe é importante..."

            c "Assim..."

            c "Eu acho que muitas pessoas passam por coisas difíceis durante suas vidas. Não é tudo um mar de rosas."

            c "A gente sabe que pra conseguir uma coisa, a gente precisa dar duro. Superar dificuldades pensando em viver melhor no futuro."

            c "Eu não quero ser uma ingrata pelas oportunidades que a vida me deu pra ser feliz. Eu não quero parecer fraca."

            c "A última coisa que eu quero, é deixar a chance de uma vida melhor ir embora porque eu não aguentei o que eu tinha que aguentar."

            c "Mas... parece que às vezes as coisas são demais, sabe? Faz a gente pensar se tá certo passar por isso..."

            c "Por isso... eu pensei muito e não queria decepcionar todos que apostaram em mim. Jogar no lixo tudo que fizeram pra me ajudar."

            c "Só que... um dia eu conheci alguém que me ajudou também. E essa pessoa nunca me pediu nada em troca."

            c "No começo eu pensei que era um aproveitador, mas ele passou por tanta coisa do meu lado sem precisar. Até ameaçaram ele, acredita?"

            c "E mesmo assim ele sempre ficou do meu lado. Com ele não tinha acerto, negociação... foi alguém que me mostrou o que é ajudar alguém."

            c "Ajudar de verdade. Não dar com uma mão e pegar com a outra. Mas passar por tudo pensando no bem de outra pessoa."

            c "E é por isso que eu resolvi falar tudo. Eu quero fazer a mesma coisa que ele fez. Eu quero ajudar as próximas garotas."

            c "Garotas que terão o sonho de uma vida melhor ao alcance das mãos, mas terão que aceitar tudo o que pedirem a elas!"

            scene p9_img21 with hpunch

            pause

            c "Esse homem! Ele abusou de mim durante toda a gravação do filme!"

            mc "!"

            gus "!!!"

            c "Eu tinha que transar com esse nojento sempre que vinha pra cá! Ou até no camarim durante as gravações!"

            c "Eu tentava segurar ele, mas ele sempre voltava com essas mãos nojentas pra cima de mim!"

            c "Eu não quero que isso aconteça com mais ninguém! Com mais nenhuma garota!"

            c "Por favor, juíza! Acredita no que eu tô falando! Aquela matéria é tudo verdade! E tem mais coisa do que eles falam!"

            c "Esse velho filho de uma puta! Seu nojento!"

            gus "Fala de novo isso, sua vagabunda!"

            eli "Senhor [gus]! Eu mandei o senhor ficar quieto, ou o senhor será escortado para fora!"

            gus "Essa puta é uma mentirosa!"

            eli "Senhorita [c]. Por favor, se acalme. Eu entendi seu posicionamento. Pode ir para trás."

            c "{i}snif{/i}"

            c "T-tá..."

            scene p9_img23 with Dissolve(1.0)

            eli "E o senhor, por favor. Respeite este tribunal."

            "A [c] contou! De verdade! Ela conseguiu! Não acredito!"

            "Isso é muito importante pra gente prender ele! Ela confirmou!"

            "Eu sempre acreditei em você, Pri! Minha gata! Parabéns pela coragem!"

            "Eu sabia que eu podia confiar nessa mulher! Minha namorada é incrível!"
        else:


            c "N-não é nada. D-desculpa."

            gus "Boa garota."

            c "..."

            scene p9_img23 with Dissolve(1.0)

            eli "Senhor [gus]. O que conversamos sobre sua participação? Respeite os trâmites. Não falarei novamente."

            gus "..."

            "Então a [c] não falou a verdade mesmo..."

            "Se ela, que era a principal, falou que era mentira... qual a chance deles irem atrás do velho safado?"

            "Eu não posso desistir, mas tá difícil..."

        jump priscila_e9_depoimentos

    label p9_depoimento_agata:

        eli "Eu quero chamar outra atriz que trabalhou com o senhor [gus] e portanto pode ter sofrido abusos."

        eli "A matéria não explicita ela, mas diz que o fato teria acontecido a outras atrizes."

        eli "Por favor, oficial. Peça para que a senhorita [ag] adentre o recinto."

        scene black with dissolve

        "..."

        scene p9_img24 with Dissolve(1.0)

        pause

        ag "Estou aqui."

        eli "Bom dia, senhorita [ag]. Posso chamá-la assim?"

        ag "Eu preferia ser chamada de maior atriz do cinema nacional, mas senhorita também serve."

        eli "Senhorita [ag], eu peço para que reconsidere sua postura. Este é um assunto de grande seriedade."

        ag "..."

        eli "Eu preciso que responda uma coisa simples. É com relação a matéria que foi publicada acusando o senhor [gus]."

        eli "Você trabalhou com o diretor no penúltimo de seus filmes, há dois anos atrás. Isso é verdade?"

        ag "Eu trabalhei com esse lindo por muito tempo. Esse foi apenas um dos filmes que gravamos juntos."

        ag "Inclusive, eu diria que sou a atriz que nunca deixou a cabeça dele."

        eli "Vou considerar sua resposta como uma afirmativa ao que perguntei."

        eli "A senhorita teve acesso a matéria que deu origem a esta reunião?"

        ag "Eu não me interesso por tablóides de segunda, a não ser que falem sobre mim."

        eli "Pedirei para que seja lida a matéria para você na frente de todos."

        ag "Não há necessidade. Como eu disse, se falam sobre mim, eu leio."

        eli "Mesmo sem ser citada nominalmente, esta matéria falava sobre você? Está certa disto?"

        ag "Obviamente. Sempre que falarem de cinema, do meu velhinho preferido e de qualquer coisa importante, eu estou no meio."

        eli "Senhorita [ag]... por favor..."

        ag "Apenas quero dizer que estou ciente de tudo. Eu não sou só um rostinho bonito, eu sou bem informada."

        eli "Enfim..."

        eli "O que eu vou lhe perguntar precisa de sua total atenção."

        eli "Quero ressaltar que você não está sob juramento. Mas recomendo dizer a verdade, para contribuir com a sociedade."

        ag "Minha sociedade é a high society, diferente da sua sociedade... que deve ser a mesma daquele guardinha ali."

        eli "Eu gostaria de uma resposta sincera e concisa de sua parte. E espero que preste atenção."

        ag "Farei o possível."

        eli "Na matéria em questão, é citado que, não apenas [cc], mas outras atrizes teriam sofrido abusos por parte do diretor."

        eli "O diretor em questão é o senhor Gustav Aldebaran. Este homem a nossa frente."

        eli "A matéria não nomeia quais seriam as outras atrizes, mas diz que eram protagonistas, assim como a senhorita [c]."

        eli "Você foi a protagonista do penúltimo filme do senhor [gus], como a senhorita confirmou."

        eli "O que eu preciso saber da senhorita, é se esse trecho da matéria especificamente, quando cita outras protagonistas..."

        eli "Este trecho ao qual me refiro. Desejo que foque apenas nele."

        eli "Você diria que se esse trecho específico da matéria é verdadeiro de acordo com sua própria experiência?"

        ag "Você está tentando me enganar?"

        eli "Perdão... como senhorita?"

        scene p9_img25 with Dissolve(1.0)

        pause

        ag "Você quer me engambelar? Falando desse jeito eu quero dizer."

        eli "Não, senhorita. Estou apenas tentando ser a mais clara e direta possível. Eu posso reformular."

        ag "Não precisa. Quem olha pro meu rostinho maravilhoso, pro meu corpo gostoso, pode achar que eu sou burra, mas eu não sou."

        ag "Eu também tenho muita inteligência e sei o que você perguntou. Você quer saber se aconteceu comigo também."

        ag "O tal abuso que aconteceu com a [c]. Aquela atriz de quinta que nem devia ter sido chamada em primeiro lugar."

        eli "O que a senhorita tem a dizer sobre isso?"

        ag "Eu poderia ficar falando e falando aqui. Mas humildade também é um dos meus atributos, então serei direta."

        if agata_confessa and not agata_beijo:

            $ julgamento_sucesso += 1

            ag "Esse paspalho de diretor me obrigou a transar com ele, sim."

            mc "!"

            ag "Essa era uma das condições para eu me tornar protagonista do filme. Obviamente eu não ia deixar passar."

            ag "Se eu tivesse a chance, eu nunca teria ficado com esse velho. Olha pra mim, olha pra ele."

            ag "Mas é um preço pequeno. Hoje eu sou uma artista conhecida no mundo todo. Com dezenas de contratos."

            eli "Então, apenas para ficar claro, a senhorita sofreu, sim, abusos por parte do diretor [gus] Aldebaran."

            ag "Sim. E deixa eu falar mais. Eu-"
        else:


            scene p9_img26 with Dissolve(1.0)

            pause

            ag "Só existe uma verdade..."

            eli "..."

            ag "..."

            ag "Meu velhinho nunca fez nada comigo contra minha vontade."

            ag "Não nego e nem afirmo que ocorreram pegações impróprias nos camarins e até nos corredores. Não posso comentar sobre isso."

            ag "Mas nada foi feito contra minha vontade."

            ag "Inclusive, diretor. Estou disponível para o senhor quando quiser. Quero dizer, para estrelar seu próximo filme."

            gus "Veremos, [ag]..."

            eli "Silêncio, por favor."

            eli "Senhorita [ag], apenas para deixar claro, você está afirmando que não sofreu nenhum abuso do diretor [gus]."

            ag "Exatamente. Qualquer relação que pode ou não ter ocorrido, foi concensual."

            ag "Inclusive, pode ou não ter acontecido uma vez em que estáv-"

        eli "Não há necessidade, senhorita [ag]. Agradeço pela sua honestidade. Pode voltar para a sala de espera."

        ag "Mas agora que eu gostaria de interpretar uma cena famosa de minha person-"

        eli "Oficial, por favor leve a senhorita para a sala de espera."

        scene black with dissolve

        ag "Ei! Eu ainda não terminei! Me solta, seu grosso! Animal!"

        scene p9_img23 with Dissolve(1.0)

        eli "{i}cof cof{/i}"

        jump priscila_e9_depoimentos

    label p9_depoimento_tata:

        eli "A depoente não foi atriz sob a direção do senhor [gus] Aldebaran, mas participou de tratativas com o mesmo."

        eli "Segundo informações trazidas pelo ministério público, a depoente será a estrela da próxima produção do diretor."

        eli "Oficial, por favor traga a senhorita."

        scene black with dissolve

        "..."

        scene p9_img27 with Dissolve(1.0)

        pause

        ta "Muito bom dia a todos."

        ta "Podem me chamar de [ta]. Espero poder fazer o melhor pra vocês hoje."

        ta "Eu sei que este é um assunto sério, e eu não pretendo lidar com ele de forma leviana, mesmo eu tendo apenas 18 anos."

        ta "Eu quero fazer o melhor pela nossa sociedade."

        "Essa é a mocinha que tava naquela reunião com o [to], o velho e a [a]."

        "Eu não tive tanta chance de falar com ela, mas deu pra dar trocar uma ideia. Ela tava incerta se ela devia aceitar ou não."

        "Dependendo do que ela escolheu, talvez aconteça uma coisa diferente aqui."

        eli "Senhorita, eu agradeço pelo seu discurso, e eu tenho uma pergunta pra você."

        ta "Por favor. Eu responderei o que você quiser."

        scene p9_img28 with Dissolve(1.0)

        pause

        eli "O que raios você estava pensando quando veio ao tribunal com esse tipo de roupa?"

        ta "A-ah? A-algum problema?"

        eli "É do senso comum que se vem ao tribunal de roupas sociais, ou... ao menos... não tão chamativas."

        ta "D-disseram que era algo importante, então quis colocar meu melhor vestido. E eu achei que esse ficou uma graça em mim."

        ta "A s-senhora juíza não acha?"

        eli "Eu prefiro não comentar sobre o quanto eu gostei ou não do seu vestidinho e sua tiara florida."

        eli "Só quero deixar claro que, se houver uma próxima vez, vista de forma adequada."

        ta "O-ok... me perdoe..."

        eli "Isso é o de menos, senhorita."

        eli "O motivo de estarmos aqui hoje é sobre a matéria que foi publicada recentemente sobre um possível delito."

        eli "Esse delito seria abusos cometidos pelo diretor [gus] Aldebaran durante a gravação de seus filmes."

        eli "A senhorita teve acesso a essa matéria?"

        ta "S-sim... foi uma coisa totalmente horrível..."

        eli "Muito bem. Sua tarefa hoje aqui é muito simples. Só precisamos que você responda com clareza o que eu lhe perguntar."

        ta "Sim. Sendo bem clara, certo?"

        eli "Exatamente. É uma pergunta simples, e você não está sob juramento. Estamos apenas consultando você sobre o assunto."

        eli "No entanto, isso não faz de sua ajuda menos fundamental. Sua honestidade com certeza ajudará a sociedade."

        ta "É o q-que eu quero."

        eli "Então vamos a pergunta."

        eli "Na matéria em questão, é relatado que os abusos seriam constantes entre protagonistas, e não apenas no caso da [cc]."

        eli "A matéria cita inclusive que o trato fazia parte das negociações preliminares com as atrizes."

        eli "Você, segundo contra no dossiê elaborado pelo Ministério Público, teria acabado de passar por uma reunião desse tipo."

        eli "O que eu preciso saber de você é se, por experiência própria, foi lhe requerida participação em algum esquema como este?"

        eli "Digo, durante as tratativas, surgiu algum ponto que deixasse dúbia a total idoneidade dos seus futuros empregadores?"

        ta "Você quer saber se me ofereceram o trabalho em troca de... fazer esse tipo de coisa?"

        eli "Resumindo, sim. Entretanto, não precisa ser algo direto. Você, durante as conversas, sentiu esse tipo de premissa?"

        ta "A-acho que eu entendi... então..."

        scene p9_img29 with Dissolve(1.0)

        pause

        ta "Eu quero ser o mais sincera aqui... e eu..."

        if tata_convenceu:

            $ julgamento_sucesso += 1

            ta "A verdade é que..."

            ta "Sim, juíza... eles queriam que eu aceitasse várias condições pra fechar o contrato com eles."

            ta "Ia ser uma coisa incrível, uma grande oportunidade de trabalho. Mas eu ia ter que aceitar umas coisas também..."

            eli "Quando você diz aceitar 'umas coisas', está incluso nessas 'coisas', abusos de cunho sexual?"

            ta "S-sim..."

            eli "Entendido. Eu agradeço pela sua colaboração."

            ta "Eu só queria falar mais uma coisa, posso?"

            eli "Fique à vontade, senhorita."

            ta "Eu... eu ia aceitar, sabe? Era uma proposta boa demais pra uma garota simples igual eu."

            ta "Era dinheiro demais, além da fama e toda a ajuda que eles iam me dar. Era o emprego perfeito."

            ta "E minha age- m-minha amiga tinha dito que era algo muito bom."

            eli "Então você não aceitou o trabalho."

            ta "É. Não aceitei. Só que isso só foi possível porque naquele dia da reunião, que tudo ia ser assinado, alguém falou comigo."

            ta "Uma pessoa que não tinha nada a ver com o que tava acontecendo me disse que talvez não fosse uma boa ideia."

            ta "Eu fico pensando se as outras garotas também tiveram alguém assim, que mostrasse o outro lado, entende?"

            ta "Porque naquelas condições, sozinha... não tinha como eu ter força sozinha pra tomar a melhor decisão, eu acho..."

            ta "Eu agradeço todos os dias por terem me ajudado naquele momento. Por terem se preocupado comigo."

            ta "E-era isso... me desculpa."

            eli "Não precisa se desculpar. Estou certa de que sua fala será muito útil para o que está por vir."

            ta "O-obrigada..."

            eli "Oficial. Agora leve a senhorita para a sala de espera por favor."

            scene black with dissolve
        else:


            ta "Eu queria dizer que..."

            ta "E-eu não sei nada disso. S-só isso."

            eli "Você não presenciou ou foi oferecida nenhum acordo do tipo."

            ta "S-sim. Eu... aceitei a proposta do senhor [gus] inclusive. Minha agente foi à favor e outras pessoas também."

            ta "E-eu aceitei, sabendo de tudo... quero dizer, entre tudo, não tinha nada disso, e-entendeu?"

            eli "Entendi, senhorita. Agradeço pela sua resposta."

            ta "N-não precisam se preocupar. Está t-tudo de acordo e certinho."

            eli "Oficial, por favor leve a senhorita para a sala de espera."

            ta "T-tá tudo certo. Queria deixar isso claro pras câmeras. Ouviu mãe, pai! T-tá tudo certo!"

            eli "Não existem câmeras, senhorita. Por favor... acompanhe o oficial."

            ta "T-tudo c-certo!"

            scene black with dissolve

        "..."

        scene p9_img23 with Dissolve(1.0)

        "Pronto."

        jump priscila_e9_depoimentos

    label p9_depoimento_miranda:

        eli "Responsável pelo contrato da modelo [cc] com o diretor Gustav Aldebaran, nossa próxima depoente é peça-chave."

        eli "Segundo a matéria na qual baseamos esta seção, ela seria a responsável por negociar os detalhes."

        eli "A senhorita [a] também é responsável pela nova atriz a entrar em negociação com a produção do próximo filme do diretor."

        eli "Oficial, por favor, avise a senhorita [a] que estamos esperando."

        scene black with dissolve

        "..."

        scene p9_img30 with Dissolve(1.0)

        pause

        eli "Senhorita [a]. Agradeço em nome de todos por se juntar a nós durante esta audiência."

        a "Agradeço pelo convite. Espero ser de alguma ajuda."

        eli "Com certeza será. Para começarmos, gostaria que de saber se você está a par da matéria publicada na revista."

        eli "A matéria que originou esta audiência quanto aos abusos que o diretor [gus] Aldebaran teria cometido com atrizes."

        a "Sim. É de meu conhecimento a matéria."

        eli "Perfeito. Então, o que eu irei lhe perguntar é quanto a uma informação contida naquela matéria."

        eli "Assim como outras depoentes, você não está sob juramento, mas pedimos para que responda com honestidade."

        a "Farei isso, senhora."

        eli "O que eu quero saber de você é quanto uma passagem específica do material em questão."

        eli "Na matéria, teria sido revelada sua participação como mediadora da negociação entre [cc] e o diretor."

        eli "Inclusive, você estaria a par da situação, tendo escrito em um e-mail que era 'algo comum', segundo a matéria."

        eli "Me refiro a questão de abusos aos quais sua agenciada seria exposta. Tendo você apoiado a decisão."

        eli "O mesmo estaria para acontecer com a mais nova protagonista. A jovem também teria você como sua agente."

        eli "Em vista do exposto, o que lhe pergunto é muito simples."

        eli "A possibilidade de favores sexuais foi negociada às claras ou inferida de qualquer forma durante as tratativas?"

        eli "Você teve conhecimento da possibilidade favores sexuais como moeda de troca para o trabalho?"

        a "..."

        scene p9_img31 with Dissolve(1.0)

        pause

        a "Senhora... eu..."

        eli "Leve o tempo que precisar para responder."

        a "Deus... eu serei rápida."

        if p9_miranda == 1:

            $ julgamento_sucesso += 1

            a "Eu sou uma profissional que veio do nada. Eu estava cansada da vida no interior, assim como as garotas."

            a "Queríamos ter algo a mais nessa vida. Alguma visibilidade e a chance de sermos alguém de revelância."

            a "Eu tinha certeza absoluta dentro de mim que eu estava fazendo o melhor para essas meninas."

            a "Elas teriam fama, dinheiro, estabilidade e, principalmente, o caminho aberto para uma vida melhor."

            a "Eu não imaginei que o preço seria tão caro para a mente delas. Eu estava preparada para sofrer no lugar delas se fosse possível."

            a "É verdade. Eu não sabia o quanto isso prejudicaria a saúde mental de quem eu prometi ajudar e proteger..."

            a "Mas, se tinha algo que eu sabia, é que elas estavam sendo abusadas. E todos nós sabíamos."

            a "A [c], o diretor [gus], os demais responsáveis pelas negociações. É impossível algum envolvido dizer que não sabia."

            a "Tudo foi revelado de forma clara. Nada foi escrito, obviamente, mas as conversas não deixavam dúvidas."

            a "E isso é tudo o que eu tenho pra dizer."

            a "Eu sei que eu estou jogando minha carreira no lixo, mas um rapaz me ensinou que o certo é fazer o que nós achamos certo."

            a "E pra mim, o certo é falar a verdade agora. Obrigada."

            eli "Senhorita... normalmente eu costumo confirmar o que o depoente quis dizer, mas suas palavras foram claras demais."

            eli "Eu agradeço a cooperação e pode voltar a sala de espera. Eu que agradeço pelo seu tempo."

            eli "Oficial, por favor acompanhe a senhorita."

            scene black with dissolve
        else:


            a "A verdade é que essa matéria é um poço de mentiras."

            a "Sim, eu sou a agente da [cc] e agora da nova modelo que eu prefiro não mencionar no momento."

            a "No entanto, não houve nenhuma trativa com favores sexuais implícitos ou explícitos. Nada foi negociado nesse sentido."

            a "Eu não tive acesso a isso e, de meu conhecimento, nenhuma outra parte também."

            a "Isso é apenas fabricação forçada e mentirosa de um tablóide que precisa de escândalos para sobreviver na era da internet."

            a "Acho isso um absurdo e pretendo, inclusive, tomar medidas legais."

            eli "Eu agradeço seu depoimento, senhorita."

            a "Isso era tudo?"

            eli "Sim."

            eli "Oficial, por favor acompanhe a senhorita."

            scene black with dissolve

        scene p9_img23 with Dissolve(1.0)

        jump priscila_e9_depoimentos

    label p9_depoimento_mc:

        if p7_gustav:

            eli "O depoente que vou chamar agora assina a matéria que foi publicada na revista e iniciou todo este processo."
        else:


            eli "Mesmo não sendo o autor da matéria, o depoente que chamarei agora conseguiu os dados utilizados."

        eli "O senhor [mcc] trabalha na revista em que a matéria foi publicada e teve acesso privilegiado a essas informações."

        eli "Ele é um paparazzo da revista, ficando responsável por descobrir acontecimentos desconhecidos sobre os famosos."

        eli "Oficial, por favor traga o senhor [mcc]."

        scene black with dissolve

        scene p9_img32 with Dissolve(1.0)

        pause

        eli "Senhor, [mc]. Obrigada por participar desta audiência."

        menu:
            "É um prazer contribuir.":


                mc "Vai ser um prazer contribuir para o andamento do processo."

                eli "Eu aposto que sua colaboração será inestimável."
            "T-t-tá!":


                mc "T-t-t-tá! T-tá legal."

                eli "Senhor, por favor se acalme. Será apenas uma pergunta simples."

                mc "C-certo."

        eli "O que eu vou precisar de você, é que responda a uma pergunta sobre a matéria da revista."

        eli "Eu chamarei você de responsável por ela, por ter sido você quem trouxe as informações necessárias, que é o que nos importa."

        mc "C-certo."

        eli "Não faz sentido perguntar se você sabe do conteúdo, já que foi você quem conseguiu eles."

        eli "O que eu preciso de você, é confirmar que foi você que teve acesso ao material."

        if p7_gustav:

            eli "Foi você quem escreveu a matéria, mas as informações usadas foram conseguidas por você? Pode confirmar?"
        else:


            eli "A matéria não saiu em seu nome, mas as informações usadas foram conseguidas por você? Pode confirmar?"

        mc "Sim. Eu que consegui elas."

        eli "Isso implica que você teve contato com a atriz e modelo [cc] ou outras pessoas próximas a ela."

        mc "Sim. Eu tive contato com a [c], com a [a], com o diretor e outras pessoas envolvidas."

        eli "Considerando ser verdade o que foi dito, você teve local privilegiado para descobrir o que você relatou."

        eli "Muito bem. Vou lhe perguntar agora o que eu preciso."

        mc "E-estou pronto."

        eli "A matéria trouxe muitas revelações pessoais e que não podem ser verificadas facilmente."

        eli "Eu não preciso que você me mostre nada material no momento. O que eu quero é apenas saber uma resposta simples."

        eli "Você teria como provar, de alguma forma, a denúncia principal de sua matéria?"

        eli "O fato do diretor Gustav Aldebaran ter abusado da atriz [cc] e de outras atrizes também?"

        mc "Se eu tenho como provar?"

        eli "Isso. Não é preciso provar agora. E você também não está sob juramento. Mas sua sinceridade é essencial para o processo."

        scene p9_img33 with Dissolve(1.0)

        mc "O-ok..."

        "Eu me coloquei nesta situação. Agora eu tenho que decidir o que eu vou fazer."

        "Uma prova... eu não sei se eu tenho uma prova. Esse que é o problema. Tudo o que eu sei foi o que eu vi ou me falaram."

        "Eu não sou policial, investigador, nada disso. Como eu vou ter provas?!"

        "O que eu falo?!"

        menu:
            "Eu tenho provas.":


                mc "Senhora juíza... eu... eu tenho provas."

                eli "Muito bem. Obrigada pela resposta. Neste caso, eu tenho um novo pedido."

                mc "N-novo?"

                eli "Sim. Você pode descrever, mesmo sem detalhes, qual tipo de prova é essa?"

                mc "A-acho que eu entendi... você quer saber que tipo de prova é e não ver ela..."

                eli "Em resumo é isso."

                if marco_gustav:

                    $ julgamento_sucesso += 1

                    mc "Certo... a verdade é que eu vi uma confissão da própria boca do [gus]."

                    mc "Ele e o segurança dele, que também tá aqui, estavam conversando sobre os abusos lá no set de gravação."

                    mc "Eles não sabiam que eu tava lá. Mas eu escutei tudo."

                    mc "O segurança disse que o [gus] tava fazendo a mesma coisa que ele tinha feito com uma tal de Flávia e com a [ag]."

                    mc "Que o diretor tava saindo da linha e pedindo demais. Que ele ia ser pego cedo ou tarde."

                    eli "Obrigada. Era justamente esse tipo de detalhe que eu precisava."
                else:


                    mc "E-eu não sei exatamente que prova é essa. Eu escutei o diretor falando isso, mas tudo o que eu sei eu coloquei na matéria."

                    mc "É... n-não tem nada novo ou que eu possa adicionar aqui. Desculpa."

                    eli "Tudo bem. Se isso é tudo, então sua honestidade é muito importante para o processo."
            "Eu não sou policial...":


                mc "Ei... eu não sou policial ou nada desse tipo. Eu não fico coletando provas. Eu sou um jornalista."

                mc "E-eu não sei exatamente que prova é essa. Eu escutei o diretor falando isso, mas tudo o que eu sei eu coloquei na matéria."

                mc "É... n-não tem nada novo ou que eu possa adicionar aqui. Desculpa."

                eli "Tudo bem. Se isso é tudo, então sua honestidade é muito importante para o processo."

        eli "Agradeço pela sua colaboração e pode se retirar. Oficial, por favor, ajude ele."

        mc "Ok. Até."

        scene black with dissolve

        mc envergonhado "Oficial, eu gostaria de voltar pra plateia ao invés de ir pra sala de espera."

        "Oficial" "Tudo bem. Pode seguir por aqui então."

        scene tribunal_p9 with Dissolve(1.0)

        pause

        "Ufa... será que deu certo?"

        eli "Atenção."

        "Opa! Ela vai falar."

        scene p9_img23 with Dissolve(1.0)

        jump priscila_e9_depoimentos

label priscila_e9_resultado:

    eli "E essa foi nossa terceira entrevista. Eu acredito que isso é o suficiente para que possamos chegar a uma conclusão."

    scene p9_img34 with Dissolve(1.0)

    pause

    eli "Como informei, este não é um julgamento. É apenas uma etapa inicial para determinar se os promotores vão ou não abrir um processo."

    eli "Sabemos que estamos em face de uma situação delicada. A acusação é séria e o senhor [gus] é uma figura proeminente."

    eli "Todo o material coletado hoje será repassado aos promotores do MP e eles vão deliberar sobre a necessidade de um processo."

    eli "Assim que tivermos uma decisão, informaremos o senhor [gus] quanto a isso."

    gus "Eu aposto que vocês tomarão a decisão correta quanto a isso."

    gus "Um processo agora seria muito ruim para a cidade, economicamente e também será um golpe na imagem."

    gus "Muita gente depende dos meus filmes, senhora juíza. Não se esqueça disso."

    eli "A Justiça será levada em conta, senhor [gus]. E a verdade deverá vir à tona, cedo ou tarde."

    eli "Agradeço a colaboração de todos e estão dispensados."

    scene tribunal_p9 with Dissolve(1.0)

    "Então foi isso..."

    "Aconteceu o que tinha que acontecer."

    "O [gus] tentou manter a pose, mas eu sei que ele tá puto. Eu acho que agora ele pode fazer alguma coisa contra a gente."

    "O processo ainda não tá acontecendo e ele sabe quem traiu ele agora."

    "Eu preciso tomar muito cuidado... a [c] também. E todo mundo que teve alguma coisa a ver com isso."

    "Eu não quero que ninguém morra por causa desse velho filho da puta. Ainda mais as pessoas que eu gosto."

    scene black with dissolve

    "Os próximos dias vão ser do cão... eu preciso tomar muito cuidado com o que eu vou escolher agora..."

    mc angustiado "{i}gulp{/i}"

    "Como as coisas chegaram nisso?"

    jump priscila_e9_final_final

label priscila_e9_final_final:



    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v54_fim = True
    $ dia_priscila = dia + 3

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v54_fim","final","local")

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    call checa_final from _call_checa_final

    jump end_priscila

    jump call_cidade



label priscila_e6_ligacao:

    $ priscila_e6_ligacao = True

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    mc desconfiado "Hm?"

    mc surpreso "A [c] tá me ligando!"

    mc normal "Alô, [c]?!"

    c "Oi, [mc]!"

    scene ape_celular with Dissolve(1.0)

    mc "Tudo bem?"

    c "Eu que pergunto! Tá tudo legal com você?!"

    c "A [a] me falou que você passou mal e ela te ajudou a voltar pra casa."

    "Passei mal?"

    c "Você passou no médico?"

    "Então foi isso que ela disse pra [c]... Parece que a [a] quer proteger ela de tudo o que aconteceu."

    "Eu fico puto dela simplesmente ignorar o que aconteceu comigo e inventar uma dessas. Mas será que preocupar a [c] é o melhor?"

    "O que eu respondo?"

    menu:
        "Passei, sim. Já tô bem legal.":


            mc "Ah! D-deu certo, sim. Foi só uma tontura, um lance repentino."

            mc "Desculpa ter saído sem te avisar."

            c "Que desculpa, o quê!"

            c "Desculpa eu por ter deixado você, lá."

            if priscila_namoro:

                c "Que bela namorada..."

            c "Convidei você pra ir lá, ainda te deixei sozinho e não tava lá pra te ajudar."

            c "Desculpa mesmo."

            mc "Não fica pensando nisso."

            c "Tá... mas é que eu me preocupo com você."

            "Você nem imagina o risco de saúde que eu tô correndo..."
        "[c]... na verdade não foi bem isso que aconteceu.":


            $ p6_denuncia = True

            mc "Olha, Pri. Eu não queria ficar te preocupando..."

            if priscila_namoro:

                mc "Mas agora a gente tá namorando e eu não quero esconder nada de você."

            c "O que foi, [mc]? Me fala por favor."

            mc "Calma, eu falo."

            mc "É que, na verdade, eu não passei mal durante as gravações..."

            c "Então o que aconteceu?"

            mc "O Marco me bateu."

            c "Quê?! Como assim?!"

            mc "E-eu tava andando por aquela floresta que fica perto de onde você tava gravando, e ele só voou em mim."

            c "Não acredito, [mc]..."

            mc "Acho que se eu continuasse lá alguma coisa muito grave ia acontecer. Daí a [a] me ajudou a vazar de lá."

            c "..."

            mc "Mas acabou ficando tudo legal, ok?"

            c "Isso... isso é muito sério, [mc]. Isso não tá certo. Não tá nada certo. O que a gente vai fazer?"

            mc "Como assim? A gente não vai fazer nada."

            c "Quê?!"

            mc "Eu disse que vou ficar do seu lado."

            if priscila_namoro:

                mc "Eu quis ser seu namorado sabendo de tudo isso."

            c "Não, [mc]! Isso é muito sério! Te agrediram! E não é a primeira vez!"

            mc "Olha, eu sei que não é fácil. Mas vai ficar tudo bem. Eu confiei em você. Agora eu quero que você confie em mim."

            c "Só que-"

            mc "Por favor. Vamos fingir que nada aconteceu."

    mc "Vai ficar tudo legal, confia em mim, por favor."

    c "Ok..."

    mc "Eu quero que a gente se veja o mais rápido possível."

    c "Eu também. Qualquer coisa pode me chamar, tá?"

    mc "Claro. Eu te ligo."

    if priscila_namoro:

        c "Te gosto, gato!"

        mc "Eu também."
    else:


        c "Até mais, [mc]. Fica bem."

        mc "Você também."

    "Caraca..."

    if p6_denuncia:

        "Será que eu realmente devia ter falado disso pra ela? E se ela fizer alguma merda?"
    else:


        "Será que eu devia ter falado a verdade? Não... só ia deixar ela ainda mais nervosa."

    "Eu quero continuar do lado da [c]. Ajudar ela no que eu puder. Tenho que ter coragem."

    "Esse povo é louco. Preciso andar com muito cuidado."

    "Agora deixa eu respirar um ar que eu tô precisando."

    jump call_cidade

label priscila_out_1:

    "..."

    window hide

    scene black with Dissolve(2.0)

    $ dia += 4

    "{b}Quatro dias depois{/b}"

    "{b}Em outro lugar{/b}"

    scene estudio fotografia with Dissolve (2.0)

    "Produtor" "Muito bem, pessoal! Por hoje é só. Parabéns a todos, as fotos ficaram ótimas."

    c "Eu vou lá atrás me trocar."

    scene black with dissolve

    scene pri_foto1 with dissolve

    pause

    "Produtor" "Parabéns, [c]. Linda e graciosa como sempre. Parabéns."

    c "Muito obrigada. Obrigada a todos. Vocês foram incríveis!"

    "Produtor" "Até a próxima sessão."

    c "Tchau tchau, todo mundo."
    scene pnew_ani03 with Dissolve(1.0)
    "Fotógrafo" "Eu vou ficar mais um tempinho aqui pra arrumar o material."

    "Produtor" "Ok. Até mais pro resto."

    c "Hmm..."

    "Faz vários dias que eu não falo com o [mc]. Será que ele esqueceu de mim?"

    "Acho que essa é a hora perfeita pra minha surpresa."

    scene pri_foto2 with dissolve

    pause

    "Eu tô maquiada e e tá cheio de roupa bacana aqui. Vou mandar uma foto pra ele."

    "Ele foi muito bacana comigo no bar e lá na praça. Acho que não é demais, né?"

    "Todo mundo gosta de presente. É. Vou fazer isso."

    "Eu vou precisar da ajuda do Elias... tomara que ele ainda não tenha guardado a máquina fotográfica."

    c "Ei!"

    "Fotógrafo" "?"

    c "Fábio! Tá aí ainda?"

    "Fábio" "Tô. Tudo bem?"

    c "Sim. Queria pedir uma coisa pra você."

    menu:
        "Chamar ele pra dentro do biombo":


            c "Você pode vir aqui um pouquinho?"

            "Fábio" "Claro."

            scene black with dissolve

            scene pri_foto3 with dissolve

            pause

            "Fábio" "O-opa."

            c "Que foi?"

            "Fábio" "Tudo bem eu ficar aqui mesmo?"

            c "Para de ser bobo. Você já tirou tanta foto minha... e com cada roupa..."

            "Fábio" "Mas assim... sem roupa... é a primeira vez."

            c "Ficou com vergonha?"

            "Fábio" "Fiquei é com outra coisa..."

            c "Haha... bobo..."

            "Fábio" "Depois dessa eu tô te devendo uma. O que você quer."

            c "Bom saber... vou aproveitar."
        "Falar com ele dalí mesmo":


            c "Você tá me ouvindo?"

            "Fábio" "Claro. Pode falar."

    c "Então, você ainda consegue tirar uma foto?"

    "Fábio" "Claro, linda. É um segundo pra preparar a câmera."

    c "Que bom! Você poderia tirar mais uma foto, então? Esta é particular."

    "Fábio" "Sem problemas. Pode se preparar."

    c "Ok."

    "Que tipo de foto eu devo mandar pra ele?"

    menu:
        "Mandar uma foto bonitinha":


            $ priscila_cel_msg3_r = "amizade"
            $ priscila_amizade += 2

            "Vou mandar uma foto gracinha. Ele vai adorar."

            c "Tô indo pra aí."

            scene black with dissolve

            scene estudio fotografia with Dissolve(1.0)

            c "Tô pronta."

            "Fábio" "Aqui vai!"

            scene white with Dissolve (0.2)

            scene pri_foto4 with dissolve

            pause

            "Fábio" "Uou!"

            "Fábio" "Quem é o sortudo que vai receber a foto? Ou seria uma sortuda?"

            c "É um sortudo mesmo. Porque receber uma foto minha assim..."

            c "Pensando bem, você tem várias fotos minhas assim, né?"

            "Fábio" "Ah! Mas no meu caso é diferente. É trabalho. Queria ter uma garota linda que nem você pra me mandar fotos também."

            c "Ounn... Você tá sendo fofo agora."
        "Mandar uma foto sensual":


            $ priscila_cel_msg3_r = "seducao"
            $ priscila_seducao += 2

            "Vou mandar uma foto bem ousada. Tenho certeza que ele vai gostar muito mais."

            "Será que ele vai pensar em sacanagem? Tomara..."

            c "Tô indo pra aí."

            scene black with dissolve

            scene estudio fotografia with Dissolve(1.0)

            "Fábio" "Pronta?"

            c "Ah! Tô pronta."

            "Fábio" "Aqui vai!"

            scene white with Dissolve(0.2)

            scene pri_foto5 with dissolve

            pause

            "Fábio" "Minha nossa. Você tá muito gata."

            c "Valeu. Mas você sempre fala isso."

            "Fábio" "Quem é o sortudo que vai receber a foto? Ou seria uma sortuda?"

            c "É um sortudo mesmo. Porque receber uma foto minha assim..."

            c "Pensando bem, você tem várias fotos minhas assim, né?"

            "Fábio" "Ah! Mas no meu caso é diferente. É trabalho. Queria ter uma garota linda que nem você pra me mandar fotos também."

            c "Ounn... Você tá sendo fofo agora."

            "Fábio" "Falando nisso, e se a gente apimentar mais um pouco isso aí?"

            c "Apimentar como?"

            "Fábio" "Tira a roupa. Manda um nude pra ele."

            c "Não é coisa demais? A gente não se conhece tanto assim."

            "Fábio" "Faz assim... a gente tira a foto e depois você pensa se manda ou não. Pelo menos você fica com ela pra pensar."

            c "Hmm..."

            menu:
                "Hmm... ok...":


                    c "Hmm... ok... vamo aproveitar, então."

                    "Fábio" "Isso!"

                    "Fábio" "Tira tudo então e faz uma pose bem gostosa."

                    c "Pode deixar. Posar e ser sensual é comigo."

                    "Fábio" "Nem fala..."

                    scene black with dissolve

                    scene pri_foto6 with dissolve

                    pause

                    c "E aí?"

                    "Fábio" "Se fosse eu, não aguentava..."

                    c "Perfeito."

                    "Fábio" "E quem é esse que merece tudo isso?"

                    c "É um rapaz que eu conheci. Eu acho que é um cara especial, Fábio."

                    "Fábio" "Eu fico feliz por você. Então bora caprichar no ensaio."

                    "Fábio" "Posso chegar mais perto?"

                    c "Claro."

                    scene pri_foto7 with dissolve

                    pause

                    "Fábio" "Bem melhor daqui."

                    c "Eu já falei que eu não fico com receio de você."

                    "Fábio" "Você fala como se eu não pudesse dar em cima de você."

                    c "Eu sei que você não é gay, mas eu confio em você."

                    "Fábio" "Hmf... Já deu pra ver que eu não tenho chance com você."

                    c "Haha..."

                    "Fábio" "Pelo menos eu posso olhar."

                    c "Ei..."

                    "Fábio" "Eu tô aqui trabalhando de graça..."

                    c "Combinado. Mas eu não quero foto minha nua com você, hein?"

                    "Fábio" "Relaxa. Eu te dou o cartão de memória. Ficar com foto pessoal das pessoas é muita mancada."

                    c "Tá vendo? Por isso eu confio em você."

                    "Fábio" "Isso é o mínimo. Gente que posta foto íntima dos outros é lixo."

                    "Fábio" "Mas agora eu quero tirar uma última foto."

                    c "Mais?"

                    "Fábio" "Essa vai ser especial. Eu quero que você deite no chão, eu vou tirar a foto de cima pra baixo."

                    c "Parece sensual demais..."

                    "Fábio" "Pelo menos tira a foto. Depois você vê se manda."

                    "Hmm..."

                    menu:
                        "Não vou parar agora. Vamo.":


                            c "Agora que a gente tá aqui, vamo lá."

                            "Fábio" "Então deita aqui."

                            scene black with dissolve

                            scene pri_foto8 with dissolve

                            pause

                            c "Ai, Fábio..."

                            "Fábio" "Relaxa... eu tô acostumado com esse tipo de coisa."

                            c "Sério?"

                            "Fábio" "Eu tiro foto de tudo. E posso dizer que mulher que trabalha com ensaio quente adora essa posição."

                            c "Hmm..."

                            c "Parece que você pode fazer o que quiser comigo assim."

                            "Fábio" "E eu posso... você tá nas minhas mãos, Pri."

                            "Parece a coisa tá esquentando entre a gente."

                            menu:
                                "Vou deixar rolar":


                                    c "Sei... e o que você vai fazer?"

                                    "Fábio" "O que eu quero fazer e o que eu vou fazer são diferentes infelizmente..."

                                    c "E o que você quer fazer?"

                                    "Fábio" "Eu queria largar essa câmera agora e segurar você pelo cabelo..."

                                    c "Ai, Fábio... não precisa falar assim também."

                                    "Fábio" "Eu tô me segurando muito, [c]."

                                    c "Eu sei... eu tô sentindo uma coisa aqui na minha barriga."

                                    "Fábio" "Não brinca comigo, mulher..."

                                    c "Hmm... bem que você queria brincar agora, né?"

                                    "Fábio" "Pri!"

                                    c "Tá bom... desculpa... eu gostei de provocar você."

                                    "Fábio" "Eu sou muito idiota mesmo de não te catar agora."

                                    c "Você é um cavalheiro, Fábio. Por isso que eu confio tanto em você."

                                    "Fábio" "Vão me chamar de gado, isso sim..."

                                    "Fábio" "Espero que esse rapaz que você tá afim aproveite melhor."

                                    c "Ele parece um cavalheiro, igual você."

                                    "Fábio" "Outro idiota então..."

                                    c "Ei..."

                                    "Fábio" "Deixa eu tirar logo essa foto."

                                    show white with Dissolve(0.2)

                                    hide white with Dissolve(0.2)

                                    c "Pronto."
                                "Melhor parar com isso":


                                    c "T-tirou a foto?"

                                    "Fábio" "Tô quase lá."

                                    c "..."

                                    show white with Dissolve(0.2)

                                    hide white with Dissolve(0.2)

                                    "Fábio" "Prontinho."
                        "Tá bom assim.":


                            c "Valeu, mas é melhor não. Deixa pra depois."

                            "Fábio" "Você quem sabe, gata."
                "Melhor não...":


                    c "Valeu, mas é melhor não. Deixa pra depois."

                    "Fábio" "Você quem sabe, gata."

    c "Era isso, Fábio. Obrigada."

    scene black with dissolve

    scene estudio fotografia with Dissolve(1.0)

    "Fábio" "Toma aqui o cartão de memória. Não tem cópia. Depois você me devolve, tá?"

    c "Obrigada mesmo."

    "Fábio" "Sem problemas, linda. O que quiser de mim, só pedir."

    menu:
        "Bom saber...":


            $ priscila_neto += 1

            c "Obrigada. Bom saber..."
        "...":


            c "..."

            c "Tchau, Fábio."

    "Agora deixa eu mandar pro [mc]."

    "..."

    "Mandei! Tomara que ele goste..."

    scene black with dissolve

    if tempo < 3:

        scene mapa cidade with dissolve
    else:


        scene mapa cidade_noite with dissolve

    mc incomodado "Se passaram vários dias e eu ainda não dei nada novo pro chefe."

    "Mas ele parece sob controle. Deve ter acontecido algo de bom. Só não posso enrolar demais."

    if tempo < 3:

        scene mapa cidade with hpunch
    else:


        scene mapa cidade_noite with hpunch

    $ priscila_cel_msg3 = True

    "Opa. Uma mensagem da [c]."

    "Só fazem alguns dias, mas parece que faz tanto tempo que a gente não se fala."

    show screen celular_priscila

    "..."

    if priscila_cel_msg3_r == "amizade":

        mc feliz "Que legal! A Pri é incrível mesmo. É linda e muito bonitinha."

        mc normal "Não tem como ficar pra baixo depois de receber uma foto dessas."

    elif priscila_cel_msg3_r == "seducao":

        mc safado "Uou..."

        mc "Ela sabe mesmo como mexer comigo."

        if priscila_seducao_evento == 1:

            mc "Eu consegui seduzir ela uma vez até agora. Eu deixei a desejar nesse sentido no outro encontro. Mas tudo bem."

        elif priscila_seducao_evento == 2:

            mc "Eu seduzi ela duas vezes já. Ela deve ficar molhada só de pensar em mim."
        else:


            mc "Até agora eu não consegui seduzir ela em nenhum dos encontros. Preciso melhorar meu jogo nessa área."

    "Deixa eu responder ela..."

    "..."

    $ priscila_cel_msg3_rA = True

    mc normal "Pronto."

    "..."

    mc "Ela já respondeu."

    show screen celular_priscila

    mc "..."

    mc incomodado "Não vejo a hora de encontrar ela de novo."

    "..."

    if cassia_aceitou:

        mc angustiado "Ixi!"

        "Esqueci completamente da [j]!"

        "Preciso descobrir algo sobre o fulano lá... O [nc]."

        "Senão tudo isso que eu tenho com a [c] vai pro buraco."

        mc angustiado "..."

    $ v3_fim = True

    if not persistent.tutorial_cards:

        call tutorial_cards from _call_tutorial_cards

    return

    jump call_cidade

label namoro_priscila2:

    if premium:

        python:
            if renpy.android:
                a9009 = PythonSDLActivity.pegaBacker()

        if renpy.variant("android") and not a9009:

            jump nao_apoiador

    python:
        a9010 = False
        if renpy.android:
            a9010 = PythonSDLActivity.pegaBanned()

    if a9010:
        $ a9010 = False

    return

label priscila_inicio:

    scene quarto pc with Dissolve(2.0)

    c "Que delícia de banho..."

    scene black with dissolve

    scene ani04 with Dissolve(1.0)

    pause

    c "Essas revistas sempre falam de crush... amor verdadeiro... par perfeito..."

    c "Eu já tô com 19 anos e ainda nem... fiz aquilo..."

    c "Minha agenda tá toda lotada! Como é possível conhecer alguém legal assim?!"

    c "Por favor alguém me..."

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    c "Epa. Tem alguém me ligando..."

    "Eu acabei de sair do banho e ela já tá enchendo..."

    c "Deve ser Deus dizendo pra eu ser menos tarada..."

    c "Deus! Você entendeu tudo errado! É o contrário!"

    c "..."

    scene black with dissolve

    scene priscila_quarto1 with Dissolve(1.0)

    c "Alô?"

    "Agente" "Olá, querida! Tudo bem com você?"

    c "Mais ou menos..."

    "Agente" "O que houve?"

    c "É que eu tava pensando que tô querendo um namorado..."

    "Agente" "Não pense em besteiras, [c]!"

    c "Desde quando querer um namorado é algo errado?!"

    "Agente" "Não temos condições de pensar nisso agora! Você está no topo, querida!"

    c "Mas..."

    "Agente" "Não tem 'mas'! Amanhã estamos indo para a capital. Temos que fechar o contrato."

    scene black with dissolve

    scene priscila_quarto2 with Dissolve(1.0)

    c "Ah! Eu tinha esquecido disso..."

    "Agente" "E você acha que eu não sabia? Por que acha que eu tô te ligando?"

    c "..."

    "Agente" "Olha, linda... Eu não sei o que te dizer. Você é uma celebridade! A celebridade mais famosa entre os adolescentes."

    "Agente" "Eles te amam! Por que você quer um homem na sua vida agora?"

    c "Não sei... Só tô, sei lá, me sentindo sozinha..."

    "Agente" "Quando isso acontecer, pense nos seus fãs! Veja todas mensagens que você recebe deles!"

    c "Eu sei... Mas não é a mesma coisa..."

    scene black with dissolve

    scene ani05 with Dissolve(1.0)

    pause

    c "Será que... depois a gente podia se ver?"

    "Agente" "..."

    "Agente" "Eu adoraria, querida. Você sabe que eu te amo, mas é que tá tudo tão corrido..."

    c "Tudo bem. Eu entendo."

    "Agente" "Por que você não assiste um filme pra parar de pensar baboseira? Vê aquele {b}O Diabo Veste Prada{/b}."

    c "Nunca ouvi falar..."

    "Agente" "Eu imaginei... E outra coisa: uma garota não precisa de um homem pra satisfazer suas necessidades."

    c "Não quero saber disso!"

    "Agente" "Calma... Só tô falando."

    c "Tchau!"

    "Smartphone" "Tu... tu... tu..."

    scene black with dissolve

    scene priscila_quarto3 with Dissolve(1.0)

    c "Cada uma..."

    c "..."

    c "Minha alma gêmea..."

    c "Eu sei que você existe. Onde será que você tá agora?"

    c "Será que você tá indo dormir também?"

    window hide

    pause

    scene black with Dissolve(2.0)

    c "{size=15}Eu só queria saber... se você vai gostar de mim...{/size}"

    c "{size=10}Quando a gente se ver...{/size}"

    c "{size=15}zzzz{/size}"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
