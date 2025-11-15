label cassino_entrada:

    if diana_e7 == "pauta":

        python:
            if renpy.android:
                roupa_blacktie = PythonSDLActivity.pegaBlacktie()

        "Tá na hora da verdade."

        "Resolver tudo com o Barão, com a Diana, e minha moral com a Sofia e com o chefe."

        "É o maior evento que eu já cobri como jornalista desde o começo. Nada foi igual isso."

        "Eu tenho que tá no estilo com o {b}Black Tie{/b} e tá certo do que eu vou decidir."

        "Vamos lá?"

        label diana7_comeca:

            pass

        menu:
            "Esperar o grande show da Diana começar":


                if not roupa_blacktie:

                    "Eu não tenho um Black Tie... e o chefe mandou eu tá no esquema pra esse evento."

                    "Vou comprar uma roupa de grife na boutique da cidade antes. A mais cara. É o único jeito de continuar."

                    "Esse evento vai valer à pena. Só quando eu passar por isso que posso continuar finalizando as outras coisas."

                    "Fazer bico no bar do Fabrício, no lámen, sei lá, dá um jeito! Mas eu não vou desistir agora!"

                    p "Se você não tem dinheiro, você pode comprar no menu ou ganhar trabalhando no bar e no lámen."

                    jump diana7_comeca

                jump diana_evento7
            "Ainda não. Preciso de mais tempo":


                "Ainda não tô pronto. Tudo precisa tá perfeito pra um evento desse tamanho."

                "Quando eu tiver pronto, é só eu voltar aqui no Cassino."



    if tempo < 3:

        "Eu só posso usar a parte de apostas do cassino durante a noite."

        "Tenho que dar um tempo e depois volto."

        jump call_cidade

    if not silver_card:

        "Aqui é o cassino. É o lugar mais top de toda a ilha."

        "Deixa eu passar lá na frente."

        scene cassino fachada with Dissolve(1.0)

        "Escutei o chefe falando uma vez. O lugar é chamado de Cassino do Barão."

        mc envergonhado "O dono parece mesmo gostar de aviões."

        "Deixa eu chegar mais perto."

        scene cassino portas with Dissolve(1.0)

        "Caralho. O lance é de outro mundo. Parece que é tudo feito de ouro."

        mc charmoso "Vou entrar."

        "Segurança" "Com licença, senhor."

        mc normal "Boa noite."

        "Será que tem que pagar pra entrar?"

        "Segurança" "Boa noite. Nunca vi o senhor antes. Com licença, mas posso ver seu cartão de jogador?"

        mc preocupado "Desculpa, mas não tenho isso."

        "Segurança" "Você precisa de um cartão de jogador pra curtir uma noitada no cassino. No mínimo um {b}Bronze Card{/b}."

        mc desculpa "Entendi. Não posso só dar uma olhada?"

        "Segurança" "Senhor, com todo o respeito... Dá o fora que você tá atrapalhando os clientes de verdade!"

        mc zerado "Cuzão..."

        scene cassino fachada with Dissolve(1.0)

        "Parece que eu só posso vir neste lugar se eu tiver no mínimo um {b}Bronze Card{/b}."

        mc desconfiado "Onde eu vou encontrar isso?"

        "..."

        jump call_cidade

    "Visitar o Cassino do Barão vai usar um período do meu dia. Será que eu quero ir agora?"

    menu:
        "Entrar no cassino":


            mc charmoso "Uma noitada no cassino é sempre muito bom."

            $ estou_na_cidade = False
        "Agora não":


            "Vou deixar para outra hora."

            jump call_cidade

    python:
        if renpy.android:
            roupa_blacktie = PythonSDLActivity.pegaBlacktie()
            roupa_blazer = PythonSDLActivity.pegaBlazer()

    "Com qual traje eu vou no cassino hoje?"

    menu:

        "Black Tie" if roupa_blacktie:

            $ cassino_roupa = "blacktie"

            mc charmoso "Hoje eu vou matar a pau."

            "..."

        "Blazer" if roupa_blazer:

            $ cassino_roupa = "blazer"

            mc normal "Com meu blazer não passo vergonha."

            "..."
        "Roupa de sempre":


            $ cassino_roupa = "normal"

            mc preocupado "Não acredito que tenho que ir no lugar mais chique da cidade vestido assim."

            mc angustiado "Maldito [gar] muquirana!"

            "..."

    scene cassino portas with Dissolve(1.0)

    $ randc = 0

    $ randc = renpy.random.randint(4,5)

    $ randc = renpy.random.randint(1,3)

    $ renpy.block_rollback()

    if not cassino_2vez:

        "Esse lugar ainda me assusta um pouco."

        "O jeito que esse povo tá bem vestido e têm esse jeito de rico. Tá louco."

        if not cassino_roupa == "normal":

            "Sorte que eu não tô com a minha camiseta de sempre. Assim não chamo atenção da forma errada."

            "Vai saber quem eu vou encontrar aí dentro."
        else:


            "Tô com esta roupa aqui, mas foda-se. Depois que eu deixar o Barão pobre vou poder comprar a roupa que eu quiser."

        "Vem gente do país inteiro jogar aqui. A ilha existe basicamente como uma extensão do Cassino do Barão."

        "Tudo gira em volta deste lugar."

        "Pensar o dinheiro que deve correr aqui todo dia. Imagina se alguém tentasse roubar essa fortuna?"

        "Falar a verdade eu nem devia tá aqui. Desde quando assalariado tem dinheiro pra perder em cassino?"

        "Mas já que eu moro em uma ilha paradisíaca tenho que aproveitar."

        "Hoje eu não sou qualquer um. Eu sou [mcc] o cassineiro."

        mc zerado "Certeza que essa palavra nem existe."

        mc charmoso "Enfim. Bora lá!"
    else:


        if randc == 1:

            "Hoje eu vou ganhar muito dinheiro."

        elif randc == 2:

            "É hoje que eu vou ficar rico!"

        elif randc == 3:

            "Hoje eu tô sentindo a sorte do meu lado. Vou quebrar a banca!"

    stop sound

    scene cassino hall with Dissolve(1.0)

    pause

    if not cassino_1vez:

        call atendente_cena from _call_atendente_cena

    elif not cassino_2vez:

        $ cassino_2vez = True

        "Opa! Aquela moça tá aqui de novo."

        show atendente cassino_bemvindo with Dissolve(1.0)

        ate "Boa noite, senhor."

        mc charmoso "Boa noite."

        ate "Muito bom ver o senhor novamente aqui no Cassino do Barão."

        mc "Minha primeira visita foi incrível. Estou ansioso pra continuar curtindo."

        ate "É pra isso que estamos aqui, senhor. Você pode se divertir e mudar sua vida em uma noite."

        mc envergonhado "Tem gente que realmente acredita nessas coisas? De ficar rico de um dia pro outro?"

        show atendente cassino_timida with dissolve

        ate "Hihi... a maioria, sim."

        mc "Imagino..."

        ate "O senhor parece ser mais inteligente que isso..."

        mc "Bom... se você ver o chefe que eu tenho que aguentar e as coisas que eu tenho que fazer, talvez sua opinião mude um pouco."

        ate "Cada um faz o que precisa pra viver. A gente aqui não é diferente."

        mc desconfiado "Como assim?"

        show atendente cassino_contrariada with dissolve

        ate "Nã-não é nada. Desculpa..."

        "O que deu nela?"

        mc charmoso "Bom. Vou entrar e ver se pelo menos um pouquinho eu ganho."

        show atendente cassino_timida with dissolve

        ate "Tomara que seja seu dia de sorte."

        mc envergonhado "Tomara mesmo."

        ate "Estarei sempre aqui na entrada para recebê-lo... se precisar de algo."

        mc charmoso "Obrigado. Boa noite."

        ate "Tenha uma excelente noite no Cassino do Barão."
    else:


        show atendente cassino_bemvindo with Dissolve(1.0)

        if not gold_card:

            ate "Boa noite, senhor."

            mc normal "Boa noite."
        else:


            ate "Boa noite, senhor [mc]."

            if not patricia_conheceu:

                $ patricia_conheceu = True

                mc desconfiado "Hm? Primeira vez que você fala meu nome."

                ate "Ah, sim. Agora você é um jogador Gold, não é mais um cliente comum."

                ate "Nós conhecemos pessoalmente e de forma diferenciada os portadores do Gold Card."

                mc envergonhado "Assim fica parecendo algo realmente exclusivo mesmo."

                ate "E é."

                mc charmoso "Bom, já que você sabe meu nome eu também quero saber o seu, porque até agora pra mim você é só [ate]."

                show atendente cassino_timida with dissolve

                ate "Meu nome?!"

                mc "Sim. Qual o problema?"

                ate "É... acho que nunca ninguém me pergunou antes."

                mc normal "Pessoas sem educação. E então?"

                $ at_nome = "Patrícia"

                ate "Então tá... meu nome é [ate]."

                mc charmoso "Muito prazer, [ate]."

                mc normal "Espero que a gente possa se conhecer melhor um dia desses."

                ate "Ok..."

                mc "Agora vou jogar."

                ate "Tá..."
            else:


                mc charmoso "Boa noite, [ate]. Já sou Gold, mas dinheiro nunca é demais. Continua torcendo por mim."

                ate "Pode deixar, senhor [mc]."

                ate "Uma excelente noite de jogos para você."

                mc normal "Obrigado."

        if natasha_e2 == "diana":

            $ natasha_e2 = "patricia"

            mc normal "Ah! Será que eu posso te fazer uma pergunta?"

            ate "Com certeza, senhor. Estou aqui para servir."

            mc "O que você sabe sobre o Barão?"

            ate "O Barão é o criador deste universo paralelo, onde você pode viver uma nova vida de diversão."

            ate "Ele é apenas quem idealizou este sonho, porque aqui, é você quem cria sua história. Você é dono do show."

            mc envergonhado "..."

            mc "Esse texto que você decorou aí... será que você poderia me falar algo diferente?"

            show atendente cassino_contrariada with dissolve

            ate "Ahn?"

            ate "Não entendi, senhor..."

            mc charmoso "Eu gostaria de saber algo diferente sobre ele. Algo mais... pessoal."

            ate "Eu... gostaria de ajudar o senhor... só que eu não posso..."

            mc desconfiado "Você não sabe nada? A [d] disse que algumas garotas tem um 'contato mais direto' com ele."

            ate "!"

            ate "E-eu não sei... agora vou atender outros convidados. Com licença, senhor."

            hide atendente with dissolve

            "Hmmm... tem caroço nesse angu."

            "Se ela não quer falar comigo... quem será que falaria?"

            "E se nenhuma garota que trabalha aqui quiser abrir o bico? E se elas tiverem um contrato..."

            "A [d] deve ter mais liberdade do que elas. Ela é cantora, é importante. Talvez as outras não possam falar nada."

            "Mas se for isso mesmo... e agora? Eu ainda não tenho o suficiente pra ajudar a [na]..."

            "Talvez alguém fora do Cassino saiba... Mas quem?"

            "..."

            show atendente cassino_bemvindo with Dissolve(1.0)

            ate "Olá, senhor."

            mc desconfiado "Hm?"

            ate "Estou aqui para qualquer coisa que precisar de mim. O Cassino do Barão existe para você."

            "Por que ela tá falando assim como se a gente não tivesse se falado?"

            mc envergonhado "Obrigado."

            ate "Estou torcendo pelo senhor!"

            "Melhor eu só fingir que nada aconteceu..."

        if randc == 1:

            ate "Que a Lady Luck sorria pra você esta noite."

            menu:
                "Muito obrigado.":


                    mc envergonhado "Muito obrigado. Preciso mesmo de toda a ajuda pra conseguir uns créditos."

                    ate "Você vai conseguir esta noite. Estou sentindo."

                    mc normal "Obrigado."
                "Prefiro o seu sorriso":


                    mc charmoso "Prefiro quando você sorri pra mim."

                    show atendente cassino_timida with dissolve

                    ate "Charmoso como sempre."

                    mc "Tá vendo? Bem melhor. Até outra hora."

                    ate "Estarei aqui se precisar."

        elif randc == 2:

            ate "Estou vendo que hoje o senhor vai ter muito sucesso na máquina de slots."

            mc "Ela é minha preferida. Vou apostar alto hoje então."

            ate "Sucesso!"

            mc "Obrigado. Até outra hora."

        elif randc == 3:

            ate "Se você precisar de alguma coisa lá no salão de apostas, não esquece de chamar a [ana]."

            mc normal "Valeu. Eu falo com ela."

            ate "Ela pode pegar drinks e fazer outras coisas se o senhor precisar."

            mc "Ok."

    ate "Até."

    hide atendente with dissolve

    if randc == 1:

        "Hoje eu vou ganhar muito dinheiro."

        play music "audio/musica_3_cassino.mp3" loop

    elif randc == 2:

        "É hoje que eu vou ficar rico!"

        play music "audio/musica_4_cassino2.mp3" loop

    elif randc == 3:

        "Hoje eu tô sentindo a sorte do meu lado. Vou quebrar a banca!"

        play music "audio/musica_3_cassino.mp3" loop

    $ renpy.block_rollback()

    jump cassino_geral

label cassino_geral:

    $ cassino_regiao = "apostas"
    $ cassino_area = "geral"

    hide screen cassino_tela

    scene cassino geral with Dissolve(1.0)

    if not cassino_1vez:

        $ cassino_1vez = True

        call cassino_ana_cena from _call_cassino_ana_cena

    elif v19_fim and natasha_e1 == "nada":

        $ slots_evento30_viu = False
        $ slots_ana_aviso = False
        $ cassino_drink = False
        $ show_diana = False
        $ randc = 2

        $ cassino_regiao = "complexo"
        $ cassino_area = "jazz"

        jump natasha_evento1

    show screen cassino_tela

    pause

label cassino_ponte:

    hide screen cassino_tela

    if cassino_regiao == "apostas":

        "Subindo estas escadas eu saio do salão de apostas. Dá pra ir pra outras áreas do cassino."

    $ cassino_regiao = "complexo"
    $ cassino_area = "ponte"

    if cassino_roupa == "normal" and randc != 2 and evento_c_ponte == 0:

        $ evento_c_ponte = 1

        scene cassino_ponte with Dissolve(1.0)

        "Ali acho que é en-"

        "???" "Ei! Rapaz!"

        mc desconfiado "Hm? Tá falando comigo?"

        show pessoas_ponte with dissolve

        "Homem de Negócios" "Esqueci meu blazer no quarto, mas tô mega atrasado. Tem como você pegar pra mim e eu te dou uma caixinha?"

        mc zerado "Eu não trabalho aqui..."

        "Homem de Negócios" "Me encontra lá no carro, tá?"

        mc bravo "Eu não trabalho aqui, caralho."

        "Homem de Negócios" "Sério? É... que essa roupa..."

        mc "..."

        "Homem de Negócios" "Desculpa."

        hide pessoas_ponte with dissolve

        "..."

        mc zerado "Era só o que me faltava..."

    elif randc == 1:

        scene cassino_ponte with Dissolve(1.0)

        "Eu tenho a impressão que esse casal tá sempre brigando."

    elif randc == 2:

        scene cassino_ponte2 with Dissolve(1.0)

        "Acho que ali pra cima fica a entrada do hotel."

        "Se você não tiver o Platinum Card, o preço da diária é um absurdo."

        if evento_c_ponte == 1:

            mc zerado "Aquele cara..."

    elif randc == 3:

        scene cassino_ponte3 with Dissolve(1.0)

        "Tá bem vazio aqui hoje..."

    show screen cassino_tela

    pause

label cassino_slots:

    $ cassino_area = "slots"

    hide screen cassino_tela

    scene cassino_slots with Dissolve(1.0)

    if randc == 1:

        show pessoas_slots1 with dissolve

    elif randc == 2:

        show pessoas_slots2 with dissolve

    elif randc == 3:

        show pessoas_slots3 with dissolve

    show screen cassino_tela

    pause

label cassino_roleta:

    $ cassino_area = "roleta"

    hide screen cassino_tela

    scene cassino_roleta with Dissolve(1.0)

    if randc == 1:

        show pessoas_roleta1 with dissolve

    elif randc == 2:

        show pessoas_roleta2 with dissolve

    elif randc == 3:

        show pessoas_roleta3 with dissolve

    show screen cassino_tela

    pause

label cassino_blackjack:

    $ cassino_area = "blackjack"

    hide screen cassino_tela

    scene cassino_blackjack with Dissolve(1.0)

    show screen cassino_tela

    pause

label slots_minigame_pre:

    python:
        if renpy.android:
            credito = PythonSDLActivity.pegaCredito()
            credito_total = PythonSDLActivity.pegaCreditoTotal()

    $ credito_atual = credito_total

    hide screen cassino_tela

    scene cassino_slot_jogando with Dissolve(1.0)

    menu:
        "Iniciar nova partida":


            "Agora vai!"

            $ randvezes = 1

            jump slots_minigame
        "Deixar para outra hora":


            "Agora não. Não tô sentindo a Lady Luck aqui do meu lado."

            jump cassino_slots
        "Como funciona a máquina de slots?":


            mc desconfiado "Ah. Tem as explicações aqui."

            "{i}A Máquina de Slots ou Caça Níqueis oferece a oportunidade de ganhar muitos créditos no Cassino do Barão!{/i}"

            "{i}A aposta mínima é de C$ 3 a máxima de C$ 100. Você ganha o prêmio de acordo com o valor apostado.{/i}"

            "{i}Após fazer sua aposta, três roletas vão girar e você deverá pará-las no momento apropriado.{/i}"

            "{i}O objetivo é que as três roletas tenham a mesma figura. Existem três figuras: cereja; barras e o Sete.{/i}"

            "{i}Se você conseguir uma combinação de três cerejas, você receberá o mesmo valor investido.{/i}"

            "{i}Três barras lhe dará como prêmio o valor da aposta DOBRADO.{/i}"

            "{i}E se você conseguir três Setes, você receberá o valor da aposta QUINTUPLICADO. Ou seja, cinco vezes o valor da aposta.{/i}"

            "{i}Que a Lady Luck esteja ao seu lado. Muito entretenimento e riqueza lhe esperam nas Máquinas de Slot do Cassino do Barão!{/i}"

            mc tarado "A riqueza me espera!"

            jump slots_minigame_pre

label slots_minigame:

    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    scene cassino_slot_jogando with Dissolve(1.0)



    python:
        if renpy.android:
            credito = PythonSDLActivity.pegaCredito()
            credito_total = PythonSDLActivity.pegaCreditoTotal()

    $ credito_ganho = credito_total - credito_atual
    $ credito_falta = credito_gold - credito_total
    $ renpy.block_rollback()

    if credito_total >= 10000 and not gold_card:

        jump ganha_gold

    if credito_ganho >= 30 and not slots_evento30_viu:

        $ slots_evento30_viu = True

        scene cassino_slots_mc with Dissolve(1.0)

        $ rand = renpy.random.randint(1,3)

        if rand == 1:

            "Boa. Já ganhei uns créditos a mais pro meu cartão."

            show slots_pessoa1 with dissolve

            "Homem" "Com licença, senhor. Como tá a sorte hoje?"

            mc "Mais ou menos. Mas já deu pra ganhar uns créditos."

            "Homem" "Boa. Quer ouvir uma dica sobre como se dar bem aqui no Cassino do Barão?"

            menu:
                "Claro!":


                    mc "Com certeza. Dicas nunca são de mais."

                    "Homem" "Nunca é uma boa ideia sair apostando muito logo de cara."

                    "Homem" "Comece apostando pouco e sinta o clima. Veja se a sorte está do seu lado."

                    "Homem" "Muitos dizem que isso é tudo fantasia, mas sorte realmente existe."

                    "Homem" "Tem a ver com sentir o momento, o espírito da aposta. Alguns chamam isso de Lady Luck, um tipo de personificação."

                    "Homem" "O segredo é começar devagar e então ir com tudo!"

                    "Homem" "BANG!"

                    "Homem" "Espero que você tenha entendido."

                    mc "Acho que sim."

                    "Homem" "Isso vai ser muito importante pra você."

                    mc "Ok..."
                "Agora não. Talvez outro dia.":


                    mc "Quem sabe uma outra oportunidade."

                    "Homem" "Sem problemas."

            "Homem" "Continue assim. Até outra hora."

            mc "Boa noite."

            hide slots_pessoa1 with dissolve

            "Acho que eu já vi esse senhor aqui outras vezes."

            "Espero que ele também teja ganhando alguma coisa."

        elif rand == 2:

            "Opa! Os ganhos da noite já superaram os 30 créditos."

            mc "Espero que as coisas continuem boas."

            show slots_pessoa2 with dissolve

            "Mulher" "O senhor parece que tá com sorte hoje."

            mc "Haha! Acho que sim."

            "Mulher" "Eu já vi o senhor aqui outras vezes."

            mc "Estou sempre aqui nesta máquina."

            "Mulher" "Também gosto de jogar por aqui."

            "Mulher" "Você quer uma dica valiosa sobre Cassinos?"

            menu:
                "Por favor.":


                    "Mulher" "Eu sou uma matemática e estudei bastante sobre cassinos."

                    mc "Uou."

                    "Mulher" "Sério. Agora deixa eu te explicar algo interessante."

                    "Mulher" "O Cassino do Barão e todos os outros trabalham com porcentagens específicas de ganho e perdas."

                    mc "O que isso quer dizer?"

                    "Mulher" "Quer dizer que o que chamam de 'sorte' não passa de um resultado aleatório de um programa de computador."

                    "Mulher" "Essa máquina de slot, por exemplo, possui um sistema que vai fazer você ganhar ou perder em uma taxa específica."

                    "Mulher" "Ela faz de uma forma que você ganhe de vez em quando e perca de vez em quando, pra manter você querendo jogar."

                    mc "Isso quer dizer que é tudo mentira? Já tá programado o resultado?"

                    "Mulher" "Não. A máquina possui uma probabilidade de gerar um resultado. Mas se estivesse programado todos teriam o mesmo resultado."

                    "Mulher" "Isso quer dizer que se muitas pessoas jogarem, e tirarmos uma média de ganhos e perdas, você vai ter o número definido."

                    "Mulher" "Esse é o número que o dono do cassino programou para as máquinas."

                    mc "Então quer dizer que uma pessoa específica pode ganhar bastante e outra perder bastante."

                    "Mulher" "Exatamente."

                    mc "Só que na média elas vão ficar dentro da programação da máquina."

                    "Mulher" "Exatamente."

                    mc "Então você pode ser tanto o que ganha muito ou o que perde muito."

                    "Mulher" "Exatamente."

                    mc "Então existe sorte."

                    "Mulher" "Exat-"

                    "Mulher" "Hmmm..."
                "Talvez depois.":


                    mc "Talvez numa próxima."

                    "Mulher" "Claro."

            "Mulher" "Bom resto de jogo. A gente se vê."

            mc "Boa noite. Até."

            hide slots_pessoa2 with dissolve

            "Parece que ganhar chama a atenção das pessoas hehe..."

        elif rand == 3:

            "Não vejo a hora de pegar meu próximo card."

            show slots_pessoa3 with dissolve

            "Jovem" "Já conseguiu os 30 de crédito de hoje?"

            mc "Opa. Consegui sim."

            "Jovem" "Posso te contar algo interessante sobre cassinos e psicologia?"

            menu:
                "Com certeza.":


                    mc "Com certeza. Informação é sempre importante."

                    "Jovem" "Também acho. Veja bem..."

                    "Jovem" "Muitas pessoas usam apostas para terem uma certa esperança em suas vidas."

                    "Jovem" "É uma forma de termos esperança que algo pode melhorar."

                    "Jovem" "A questão é que em todos os jogos a chance de perder é muito maior do que ganhar."

                    "Jovem" "As pessoas que criam apostas não são boazinhas. Elas não querem doar dinheiro pras pessoas."

                    "Jovem" "Por isso, mesmo que um sortudo realmente fique milionário, o dinheiro arrecadado pela empresa foi maior."

                    "Jovem" "E todos que não ganharam nada só jogaram seu dinheiro fora."

                    "Jovem" "Mas essa esperança de ter algo melhor na vida continua fazendo a gente jogar mesmo sabendo das chances."

                    "Jovem" "A gente pensa: 'e se eu parar agora e na próxima eu ganhar? Seria um desperdício de tudo o que eu já gastei'."

                    mc "Daí a gente continua jogando e perdendo..."

                    "Jovem" "E assim as empresas ficam ricas."

                    mc "Melhor parar de jogar então?"

                    "Jovem" "Pra mim apostas são uma forma de diversão. Eu sei que não vou ficar rica."

                    "Jovem" "Assim, nunca gasto mais do que eu planejei. Contanto que você fique de olho e não seja enganado, dá pra curtir."

                    mc "Essa é realmente uma excelente dica."

                    "Jovem" "E isso não vale só pra este cassino. Vale pra todos os jogos de azar da vida, até pra Mega da Virada."

                    mc "Entendi..."

                    "Jovem" "Era isso. Desculpa falar um monte."

                    mc "Que nada. Foi bacana."

                    "Jovem" "Bom jogo e tome cuidado não gastar mais do que deve."
                "Um outro dia.":


                    mc "Tô concentrado no jogo aqui. Talvez depois."

                    "Jovem" "Entendo. A gente ainda vai se ver."

            mc "Ah, ok. Estou sempre por aqui. Bom jogo."

            "Jovem" "Você também. Até outro dia."

            mc "Até."

            hide slots_pessoa3 with dissolve

            "Esse pessoal parece que sempre aparece quando tô ganhando."

    if credito_ganho >= 50 and not slots_ana_aviso:

        $ slots_ana_aviso = True

        "Opa. Consegui mais de 50 créditos no meu cartão."

        "Eu tenho direito a pegar um drink gratuito com a [ana]. Eu não peguei o de hoje ainda."

        "Ela deve tá perto das roletas. Depois passo lá."

    if credito <= 0:

        "Epa. Não tenho créditos no meu [card]."

        "Tenho que passar no guichê e recarregar."

        jump cassino_slots
    else:


        "Eu tenho [credito] de crédito no meu cartão para jogar."

    python:
        if renpy.android:
            PythonSDLActivity.setaSalvado()

    menu:

        "Apostar C$ 3" if credito >= 1:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassino_aposta_3","cassino","local")

            $ aposta = 3

        "Apostar C$ 10" if credito >= 10:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassino_aposta_10","cassino","local")

            $ aposta = 10

        "Apostar C$ 25" if credito >= 25:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassino_aposta_25","cassino","local")

            $ aposta = 25

        "Apostar C$ 100" if credito >= 100:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassino_aposta_100","cassino","local")

            $ aposta = 100
        "Parar de jogar":


            $ proibido_salvar = False
            $ show_quick_menu = True
            $ renpy.block_rollback()

            "Tá bom por hora."

            if credito_total < credito_gold:

                if credito_total > credito_atual:

                    "Ganhei mais alguns créditos pro meu cartão."

                    "Deixa eu ver... foram mais [credito_ganho] pontos."

                    "Falta mais [credito_falta] de crédito para eu conseguir o {b}Gold Card{/b} e virar um cliente premium do cassino."

                    "Tenho que continuar jogando e ganhando mais créditos."

            jump cassino_slots

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("cassino_joga_slots","cassino","local")

    $ parar_vez = 0
    $ slot1 = ""
    $ slot2 = ""
    $ slot3 = ""
    $ slot_result1 = ""
    $ slot_result2 = ""
    $ slot_result3 = ""
    $ slots_ganhou = False
    $ ganhos = 0
    $ slotvezes = 0

    $ renpy.block_rollback()

    python:
        if renpy.android:
            PythonSDLActivity.salvaJogo()

    play sound "audio/som_29_slot1.mp3"

    $ renpy.pause(delay=4, hard=True)

    python:
        if renpy.android:
            salvado = PythonSDLActivity.pegaSalvado()

    if not salvado:

        p rindo "Para jogar nos slots, você precisa de uma conexão estável com a internet."

        p "Verifique sua rede e volte mais tarde."

        jump cassino_sair

    call slots_conta from _call_slots_conta

    scene slots_minigame_tela with Dissolve(1.0)

    play sound "audio/som_31_slot3.mp3"

    $ renpy.pause(delay=2, hard=True)

    show screen slot_tela

    play sound "audio/som_30_slot2.mp3" loop

    pause

screen slot_tela():
    tag cassino

    predict False
    zorder 100
    modal True

    if slot1 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.295
            yalign 0.36
            yanchor 0.5
            xanchor 0.5
    else:

        if slot1 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot1 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot1 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

    if slot2 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.509
            yalign 0.36
            yanchor 0.5
            xanchor 0.5

    else:

        if slot2 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot2 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot2 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

    if slot3 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.718
            yalign 0.36
            yanchor 0.5
            xanchor 0.5

    else:

        if slot3 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot3 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot3 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

    imagebutton auto "images/cassino/botao_%s.png":
        xalign 0.955
        yalign 0.99
        xanchor 0.5
        action Jump("slots_parar")

screen slot_resultado():
    tag cassino

    predict False
    zorder 100
    modal False

    if slot1 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.295
            yalign 0.36
            yanchor 0.5
            xanchor 0.5
    else:

        if slot1 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot1 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot1 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.295
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

    if slot2 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.509
            yalign 0.36
            yanchor 0.5
            xanchor 0.5

    else:

        if slot2 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot2 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot2 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.509
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

    if slot3 == "":

        add "images/cassino/img.png" at slot_img:
            xalign 0.718
            yalign 0.36
            yanchor 0.5
            xanchor 0.5

    else:

        if slot3 == "cereja":

            add "images/cassino/img_cereja.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot3 == "bar":

            add "images/cassino/img_bar.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

        elif slot3 == "sete":

            add "images/cassino/img_sete.png":
                xalign 0.718
                yalign 0.36
                yanchor 0.5
                xanchor 0.5

label slots_parar:

    $ renpy.block_rollback()

    if parar_vez == 0:

        $ slot1 = slot_result1

    elif parar_vez == 1:

        $ slot2 = slot_result2

    elif parar_vez == 2:

        $ slot3 = slot_result3

        play sound "audio/som_32_slot4.mp3"

        hide screen slot_tela

        show screen slot_resultado

        $ renpy.pause(delay=4.3, hard=True)

        hide screen slot_resultado

        jump slots_resultado

    $ parar_vez += 1

    pause

label slots_resultado:

    stop sound

    if slots_ganhou:

        if randslotw <= 70:

            "Ufa. Ganhei [ganhos] de crédito. Dá pra continuar jogando."

        elif randslotw > 70 and randslotw <= 90:

            "Boa! Ganhei [ganhos]! Dobrei minha aposta!"

            "A sorte tá chegando!"

        elif randslotw > 90 and randslotw <= 100:

            mc surpreso "UOU! Cinco vezes! Ganhei de [ganhos] créditos no total!"

            mc tarado "Um beijo pra você, Lady Luck!"
    else:


        "Merda. Essa não deu."

        if credito <= 0:

            "Ixi. Meus créditos acabaram."

    jump slots_minigame

label slots_conta:

    $ randslot = 0

    if persistent.slot_controle > 5:

        $ persistent.slot_controle = 0

    if persistent.slot_controle == 0:

        $ randslot0 = random.randint(1,100)

        $ randslot = randslot0

    elif persistent.slot_controle == 1:

        $ randslot1 = random.randint(1,100)

        $ randslot = randslot1

    elif persistent.slot_controle == 2:

        $ randslot2 = random.randint(1,100)

        $ randslot = randslot2

    elif persistent.slot_controle == 3:

        $ randslot3 = random.randint(1,100)

        $ randslot = randslot3

    elif persistent.slot_controle == 4:

        $ randslot4 = random.randint(1,100)

        $ randslot = randslot4

    elif persistent.slot_controle == 5:

        $ randslot5 = random.randint(1,100)

        $ randslot = randslot5

    $ persistent.slot_controle += 1

    if randslot > 0 and randslot <= 50:



        $ randslotw = 0

        $ randslotw = random.randint(1,100)

        if randslotw <= 70:



            $ ganhos = aposta

            $ slot_result1 = "cereja"
            $ slot_result2 = "cereja"
            $ slot_result3 = "cereja"

        elif randslotw > 70 and randslotw <= 90:



            $ ganhos = aposta * 2

            $ slot_result1 = "bar"
            $ slot_result2 = "bar"
            $ slot_result3 = "bar"

        elif randslotw > 90 and randslotw <= 100:



            $ ganhos = aposta * 5

            $ slot_result1 = "sete"
            $ slot_result2 = "sete"
            $ slot_result3 = "sete"

        $ slots_ganhou = True

        if ganhos > 0:

            python:
                if renpy.android:
                    PythonSDLActivity.addCredito(ganhos, aposta)

                else:
                    credito += ganhos
                    credito -= aposta
                    credito_total += ganhos

    elif randslot > 50 and randslot <= 100:



        $ randslotl = 0

        $ randslotl = random.randint(1,100)

        if randslotl <= 10:



            $ slot_result1 = "cereja"
            $ slot_result2 = "cereja"
            $ slot_result3 = "sete"

        elif randslotl > 10 and randslotl <= 20:



            $ slot_result1 = "cereja"
            $ slot_result2 = "bar"
            $ slot_result3 = "sete"

        elif randslotl > 20 and randslotl <= 30:



            $ slot_result1 = "sete"
            $ slot_result2 = "sete"
            $ slot_result3 = "cereja"

        elif randslotl > 30 and randslotl <= 40:



            $ slot_result1 = "sete"
            $ slot_result2 = "cereja"
            $ slot_result3 = "bar"

        elif randslotl > 40 and randslotl <= 50:



            $ slot_result1 = "sete"
            $ slot_result2 = "sete"
            $ slot_result3 = "bar"

        elif randslotl > 50 and randslotl <= 60:



            $ slot_result1 = "bar"
            $ slot_result2 = "bar"
            $ slot_result3 = "cereja"

        elif randslotl > 60 and randslotl <= 70:



            $ slot_result1 = "bar"
            $ slot_result2 = "cereja"
            $ slot_result3 = "bar"

        elif randslotl > 70 and randslotl <= 80:



            $ slot_result1 = "cereja"
            $ slot_result2 = "sete"
            $ slot_result3 = "cereja"

        elif randslotl > 80 and randslotl <= 90:



            $ slot_result1 = "bar"
            $ slot_result2 = "sete"
            $ slot_result3 = "bar"

        elif randslotl > 90 and randslotl <= 100:



            $ slot_result1 = "bar"
            $ slot_result2 = "bar"
            $ slot_result3 = "sete"
        else:


            $ slot_result1 = ""
            $ slot_result2 = ""
            $ slot_result3 = ""



        $ ganhos = 0

        python:
            if renpy.android:
                PythonSDLActivity.addCredito(ganhos, aposta)

            else:
                credito -= aposta

    return

label cassino_casher:

    hide screen cassino_tela

    scene cassino_guiche1 with Dissolve(1.0)

    "Atendente" "Boa noite, senhor."

    mc normal "Boa noite."

    if not casher_1vez:

        $ casher_1vez = True

        mc desconfiado "Oi. Aqui é o guichê? O que você faz aqui?"

        "Atendente" "Esta seção do cassino é onde você pode recarregar seu cartão com créditos para usar nossas atrações."

        "Atendente" "Você também pode fazer o contrário. Ou seja, trocar os créditos que você ganhou por C$."

        mc normal "Entendi."

        "Atendente" "Se divertir no cassino, como por exemplo, usar a Máquina de Slots, usa créditos do seu cartão de jogador."

        "Atendente" "Antes de usar ela, você precisa vir aqui e carregar seu cartão. Daí é só ir e aproveitar."

        "Atendente" "Qualquer dúvida, é só me perguntar."

        mc "Obrigado."
    else:


        "Atendente" "Como posso ajudar hoje?"

    label casher_menu:

        $ proibido_salvar = True
        $ show_quick_menu = False

        python:
            if renpy.android:
                credito_total = PythonSDLActivity.pegaCreditoTotal()
                credito = PythonSDLActivity.pegaCredito()
                cash = PythonSDLActivity.pegaCash()

        $ renpy.block_rollback()

    menu:
        "Recarregar cartão com créditos":


            mc normal "Eu gostaria de recarregar meu cartão."

            "Atendente" "Perfeito. Quanto o senhor gostaria de adicionar?"

            menu:

                "C$ 10" if cash >= 10:

                    $ ganhos = 10

                "C$ 50" if cash >= 50:

                    $ ganhos = 50

                "C$ 250" if cash >= 250:

                    $ ganhos = 250

                "Tudo o que eu tiver" if cash > 0:

                    $ ganhos = cash
                "Mudei de ideia. Não vou comprar créditos":


                    "Atendente" "Sempre às ordens. Posso te ajudar com algo mais?"

                    jump casher_menu

            python:
                if renpy.android:
                    PythonSDLActivity.compraCredito(ganhos)
                else:
                    credito += ganhos
                    cash -= ganhos

            $ renpy.block_rollback()

            "Atendente" "Pronto! Seu [card] foi recarregado com [ganhos]."

            "Atendente" "Que a Lady Luck sorria para você esta noite no Cassino do Barão."

            jump casher_menu
        "Trocar créditos por Celebrity Reais":


            mc normal "Eu quero descarregar meu cartão e trocar por Celebrity Reais."

            "Atendente" "Muito bem, quanto o senhor gostaria de retirar?"

            menu:

                "Trocar 10 créditos por C$ 10" if credito >= 10:

                    $ ganhos = 10

                "Trocar 50 créditos por C$ 50" if credito >= 50:

                    $ ganhos = 50

                "Trocar 250 créditos por C$ 250" if credito >= 250:

                    $ ganhos = 250

                "Tudo o que eu tiver" if credito > 0:

                    $ ganhos = credito
                "Mudei de ideia. Não vou retirar nada agora.":


                    "Atendente" "Sempre às ordens. Posso te ajudar com algo mais?"

                    jump casher_menu

            python:
                if renpy.android:
                    PythonSDLActivity.trocaCredito(ganhos)
                else:
                    credito -= ganhos
                    cash += ganhos

            $ renpy.block_rollback()

            "Atendente" "Pronto! Aqui estão seus C$ [ganhos]."

            "Atendente" "Se precisar de créditos novamente, não deixe de falar comigo."

            "Atendente" "Esperamos você se tornando o próximo milionário aqui no Cassino do Barão."

            jump casher_menu
        "Comprar Celebrity Reais":


            show black with dissolve

            p rindo "Oi. Você pode comprar {b}Celebrity Reais{/b} para o [mc] com dinheiro do seu mundo."

            p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

            menu:
                "Sim. Tô com uma graninha sobrando aqui.":


                    p rindo "Que bom!"

                    call comprar_cash from _call_comprar_cash_3

                    p "Agora é só falar novamente com o rapaz do guichê. Boa sorte!"

                    hide black with dissolve

                    "Atendente" "Senhor? Tudo bem?"

                    mc surpreso "Ah! Sim! Dei uma viajada."

                    jump casher_menu
                "Não. Tô pobre igual a ele...":


                    p rindo "Não esquente."

                    p "Trabalhe sempre que possível no bar e vá juntando seu dinheirinho."

                    p " Logo logo você já vai estar com grana suficiente pra aproveitar tudo. Vale a pena!"

                    hide black with dissolve

                    "Atendente" "Senhor? Tudo bem?"

                    mc surpreso "Ah! Sim! Dei uma viajada."

                    jump casher_menu

        "Você pode me tirar umas dúvidas?" if not gold_card:

            mc normal "Você pode me ajudar com algumas informações?"

            "Atendente" "Claro. O que o senhor precisa?"

            label cassino_casher_perguntas:

                pass

            menu:
                "Como funciona esse sistema de créditos?":


                    mc normal "Como funcionam os créditos pra eu poder me divertir aqui no cassino?"

                    "Atendente" "O Cassino do Barão emprega um sistema de créditos para que você possa aproveitar nossas atrações."

                    "Atendente" "É algo muito simples. Basta você vir falar comigo e comprar créditos sempre que quiser jogar."

                    "Atendente" "Eu vou trocar seus C$ por crédito no seu cartão em uma razão de 1 para 1. Para cada C$ 1, você recebe 1 de crédito."

                    "Atendente" "Esses créditos são adicionados ao seu cartão. Com eles você pode jogar na máquina de slots por exemplo."

                    "Atendente" "Se seus créditos acabarem, é preciso voltar aqui e recarregar."

                    mc tarado "Mas e se eu ficar rico?"

                    "Atendente" "Isso seria incrível, senhor. Com certeza é uma possibilidade aqui. Nesse caso, você pode fazer o contrário."

                    "Atendente" "Você pode converter seus créditos em C$ na mesma razão de 1 para 1. "

                    "Atendente" "Ou seja, se você ganhar 500 créditos jogando, pode trocar comigo por C$ 500."

                    mc "Perfeito."

                    "Atendente" "Você tem alguma outra dúvida?"

                    jump cassino_casher_perguntas
                "O que é Silver, Gold e Platinum Cards?":


                    python:
                        if renpy.android:
                            credito_total = PythonSDLActivity.pegaCreditoTotal()

                    mc desconfiado "E essa história de Silver, Gold e Platinum Cards?"

                    "Atendente" "Por favor, me passe seu cartão, senhor."

                    mc normal "Aqui está."

                    "Atendente" "Hmm..."

                    "Atendente" "O seu é um Silver Card. Este é o segundo tier de cards aqui no Cassino do Barão. O primeiro é o Bronze Card."

                    "Atendente" "Esses cartões são um tipo de classificação para diferenciar os clientes do cassino."

                    "Atendente" "Depois do Silver Card, temos o {b}Gold Card{/b} e o {b}Platinum Card{/b}."

                    "Atendente" "Quanto maior a categoria do seu cartão, mais benefícios você recebe."

                    "Atendente" "Você pode ganhar drinks gratuitos, acesso a salas VIPs do cassino, e até uma suíte em nosso hotel gratuitamente."

                    mc surpreso "Uou! Incrível!"

                    "Atendente" "Com certeza."

                    mc tarado "E como eu consigo passar de um Silver para Gold Card."

                    "Atendente" "Deixe-me ver...."

                    $ credito_falta = credito_gold - credito_total
                    $ credito_acumulado = 490000 + credito_total

                    "Atendente" "Você já tem [credito_acumulado] de crédito em seu Silver Card..."

                    mc surpreso "Quê?!"

                    "Atendente" "Algum problema?"

                    mc envergonhado "Não, não..."

                    "Caraca! A [d] me deu um cartão com todo esse valor..."

                    "Atendente" "Faltam apenas [credito_falta] de crédito para você ser promovido para portador do Gold Card."

                    "Atendente" "Continue jogando no cassino como o senhor sempre fez e em breve vai conseguir."

                    mc charmoso "Pode deixar. Em breve chegarei lá."

                    "Atendente" "Com certeza."

                    "Atendente" "Você tem alguma outra dúvida?"

                    jump cassino_casher_perguntas
                "Era isso que eu ia perguntar.":


                    mc normal "Valeu. Era isso que eu ia perguntar."

                    "Atendente" "Sempre às ordens. Posso te ajudar com algo mais?"

                    jump casher_menu
        "É só isso. Até outra hora.":


            $ proibido_salvar = False
            $ show_quick_menu = True

            $ renpy.block_rollback()

            mc normal "Só isso por enquanto. Até depois."

            "Atendente" "Até a próxima, senhor."

            jump cassino_geral

label cassino_voltar:

    "Deseja voltar para a cidade?"

    menu:
        "Sim.":


            label cassino_sair:

                $ slots_evento30_viu = False
            $ slots_ana_aviso = False
            $ cassino_drink = False
            $ show_diana = False
            $ natasha_falou = False

            $ tempo += 1

            stop music

            $ renpy.block_rollback()

            jump call_cidade
        "Não.":


            jump cassino_geral

label cassino_ana:

    hide screen cassino_tela

    if randc == 1:

        "Ah! Olha a [ana] ali. Deixa eu chamar ela."

        hide pessoas_roleta1 with dissolve

    elif randc == 2:

        "Cadê a [ana]? Normalmente ela fica perto das roletas."

    elif randc == 3:

        "Vou chamar a [ana]. Ela tá sempre aqui no salão de apostas."

    show mc c_ana_mc with Dissolve(1.0)

    mc "Boa noite, [ana]."

    show ana drink1 with Dissolve(1.0)

    ana "Boa noite, senhor."

    if cassino_roupa == "normal":

        ana "O senhor ainda não conseguiu uma roupa mais adequada ao cassino?"

        mc "Não precisa me lembrar toda vez."

        ana "{i}Rsrs{/i}"

    elif cassino_roupa == "blazer":

        ana "Eu já disse que esse blazer cai muito bem no senhor?"

        mc "Toda vez que eu venho com ele."

        ana "Ah. Mas é verdade..."

    elif cassino_roupa == "blacktie":

        ana "Uou! Você não tem dó das pessoas comuns? Desfilar com um black tie desses?"

        mc "As pessoas já acostumaram."

        ana "Eu não. Sempre que vejo você com ele tenho que dar uma boa conferida."

    if ana_evento == 0:

        $ ana_evento += 1

        mc "Então você fica andando aqui pelo salão ajudando os jogadores?"

        ana "Mais ou menos isso, senhor."

        ana "Além de tirar dúvidas, eu sirvo drinks e também posso ver quantos créditos você tem no seu cartão e quantos pontos você acumulou no total."

        show ana drink2 with dissolve

        ana "Eu também posso oferecer companhia caso o senhor precise."

        mc "Co-companhia?"

        ana "Sim. Toda vez que os clientes acumulam 250 pontos em seus cartões, eu posso te oferecer um serviço especial."

        ana "Nós podemos passar um tempo juntos... conversar... eu serei sua companheira para o que precisar."

        "Companheira? Companhia? Será que ela tá falando o que eu tô pensando?"

        ana "Aliás, nossos melhores clientes às vezes precisam conversar algo mais pessoal comigo. Temos uma sala reservada especial para isso."

        mc "Entendi..."

        menu:
            "Estou ansioso pelos seus serviços especiais.":


                mc "Pode ter certeza que estou ansioso pelos seus serviços."

                ana "Eu imagino que sim. O senhor vai adorar..."
            "Você é obrigada a fazer companhia pros jogadores?":


                mc "Desculpa perguntar assim... mas você é obrigada a fazer companhia pros jogadores?"

                ana "Ah?! É..."

                ana "Faz parte do meu serviço..."

                mc "Entendo..."

                ana "Mas não pense nisso como uma coisa negativa. Todas as atendentes do cassino devem tratar bem os melhores jogadores."

                ana "Não é nada de mais também. Falando assim parece que somos escravas. Não é nada disso."

                mc "Certo."

        ana "Por isso, continue aproveitando sua noite no Cassino do Barão e venha me ver sempre que precisar."

        ana "Ah! Sempre que você conseguir 50 pontos em uma mesma seção na Máquina de Slots, você pode pegar um drink comigo."

        ana "Esse é um benefício exclusivo para os portadores do {b}Silver Card{/b}."

        ana "Caso o senhor se torne um jogador VIP com o {b}Gold Card{/b} você terá direito a um drink gratuito todos os dias, mesmo sem jogar."

        mc "Saquei. Então quanto maior o 'nível' do meu cartão, mais benefícios eu recebo."

        ana "Exatamente. Caso tenha alguma dúvida sobre isso, o atendente do guichê tem mais informações."

        mc "Certo."

        ana "O rapaz do guichê também vai adicionar créditos no seu cartão para que você possa jogar. Ou resgatar seus créditos em C$."

        if casher_1vez:

            mc "Na verdade eu já falei com ele. Ele me explicou umas coisas."

            ana "Que bom."
        else:


            mc "Vou falar com ele então."

            ana "É só ir até a área geral do cassino e ir na direção dos guichês."

        show ana drink3 with dissolve

        ana "Então lhe desejo uma excelente noite no Cassino do Barão e qualquer coisa que precisar estou sempre às ordens."

        mc "Obrigado. A gente se vê."

        ana "É o que eu espero, senhor."

        hide ana drink3 with dissolve

        "Interessante isso... parece que o cassino dá vários benefícios quanto mais você joga."

        "Um drink gratuito por noite se conseguir 50 pontos por seção nos slots..."

        "E a cada 250 pontos no meu Silver Card eu tenho direito a pedir uma espécie de serviço especial da [ana]..."

        "Eles querem me fazer gastar todo o meu dinheiro aqui..."

        "Preciso tomar cuidado pra não deixar o Barão mais rico do que ele já é."

        "Mas me divertir um pouco não tem nada de errado. A noite tá começando!"

        jump cassino_geral

    label cassino_ana_menu:

        ana "E como posso ser útil para o senhor?"

    mc "É..."

    menu:

        "O que você pode me falar sobre o Barão?" if natasha_e2 == "fabricio":

            $ natasha_e2 = "ana"

            mc "Eu tô fazendo uma matéria sobre o cassino e queria saber um pouco sobre o Barão. Você pode me falar sobre ele?"

            ana "Posso falar com certeza. Estou aqui para servir o senhor, [mc]."

            ana "O Barão é o criador deste universo paralelo, onde você pode viver uma nova vida de diversão."

            ana "Ele é apenas quem idealizou este sonho, porque aqui, é você quem cria sua história. Você é dono do show."

            mc "..."

            ana "Esqueça sua vida e seja quem você quer ser no Cassino do Barão. Aqui você e suas escolhas importam."

            "Acho que ela disse exatamente a mesma coisa que a outra..."

            mc "Valeu, [ana]... mas eu tava pensando, tipo, em algo mais específico sobre ele."

            ana "Específico?"

            mc "Sim. Algo mais, assim... sobre ele como pessoa. A rotina dele e talz."

            ana "Hmm..."

            scene ana mesa1 with Dissolve(1.0)

            ana "O Barão é um homem muito reservado. Ele não gosta que a gente fale sobre as coisas dele."

            mc charmoso "Então você realmente conhece ele."

            ana "Eu conheço ele um pouco mais do que as outras garotas..."

            mc "E você pode me falar?"

            ana "Eu acho que você merece..."

            mc "Obrigado."

            ana "O que você quer saber exatamente?"

            "Acho que vou aproveitar e perguntar exatamente o que eu preciso."

            mc "Eu gostaria de saber sobre os assuntos que ele tem fora do cassino."

            mc "Me falaram que ele, quando vem, tem assuntos fora da ilha, lá no continente."

            ana "Sim. É verdade."

            mc "Legal... e você sabe onde exatamente?"

            ana "Talvez..."

            mc desconfiado "Não pode me falar?"

            ana "Não é bem isso. É que ele nunca me falou nada sobre esse lugar. Mas eu sei que ele vai."

            mc "Ok..."

            ana "Teve uma vez que a gente estava... conversando... e alguém ligou pra ele."

            mc "Quem?"

            ana "Não sei. Mas ele disse alguma coisa assim, tipo... 'É uma boa, que tô com fome mesmo'."

            mc "Hmm... com fome."

            ana "E daí ele saiu logo em seguida sem falar nada. Eu acho que ele foi em algum lugar comer."

            ana "Mas é só isso que eu posso falar, [mc]. Desculpa."

            mc normal "Que desculpa, o quê. Acho que você foi a pessoa que mais me ajudou até agora."

            ana "Que bom..."

            mc charmoso "Vou dar uma pensada em tudo agora e daí vou tentar descobrir mais sobre ele."

            ana "Ok, investigador. Boa sorte."

            mc envergonhado "Hehe..."

            ana "[mc]..."

            mc normal "Oi?"

            ana "Às vezes eu fico pensando se a gente é realmente tudo igual."

            mc desconfiado "Como assim?"

            ana "As pessoas dizem que somos todos iguais, sei lá, pensando na lei, nas coisas... mas não sei."

            ana "Conversando com o Barão, eu senti que ele não era igual a mim. Ele tava em um lugar diferente."

            ana "Ele olhava pra mim como se olha pra alguém que está embaixo. Não é bem um olhar de superioridade..."

            ana "É como se ele nem me visse. A opinião que eu tenho sobre ele ou qualquer coisa assim não importa."

            mc "..."

            ana "Desculpa ficar falando sobre essas coisas, mas é que eu lembrei disso quando tava te falando."

            ana "Talvez as pessoas queiram que a gente se ache igual... mas na verdade talvez o mundo não seja tão justo assim."

            mc desculpa "Eu não acho legal que algumas pessoas se sintam tão acima dos outros que nem consigam 'ver' elas."

            mc "E também não acho que você tá errada. Eu acho que tem gente assim mesmo."

            mc "Quando eu entrei na revista, eu via meu chefe meio assim..."

            mc envergonhado "Mas ele briga tanto comigo que é impossível dizer que ele não liga pra mim..."

            ana "É. É diferente. Eu sinto que o Barão não tem olhos pra gente. Como se ele... nem fosse desse mundo."

            ana "Mas agora eu falei demais, desculpa de novo."

            mc normal "Relaxa, gostei de saber disso."

            ana "Sempre que precisar, pode vir falar comigo, tá?"

            mc charmoso "Pode deixar. Tchau."

            ana "Beijo."

            scene cassino_roleta with Dissolve(1.0)

            if randc == 1:

                show pessoas_roleta1 with dissolve

            elif randc == 2:

                show pessoas_roleta2 with dissolve

            elif randc == 3:

                show pessoas_roleta3 with dissolve

            "Então o Barão falou algo sobre comer..."

            "Ele é um cara chique. Ele não vai comer em qualquer lugar, com certeza."

            "Algum conhecido dele chamou ele e provavelmente eles se encontraram em algum lugar que tem comida e que é chique."

            "É um lugar também que provavelmente fica na parte continental da cidade, então não pode ser o Tadaima."

            "O Barão também é um cara reservado... acho que ele não foi em algum lugar grande. Ele deve ter ido em um lugar mais reservado."

            "Talvez o restaurante de um conhecido... algo que ele tem confiança... talvez um local familiar e bem tradicional..."

            "Tem um lugar... que se encaixa perfeitamente nessa descrição. Eu tenho que ir lá!"

            "Mas não adianta ir qualquer hora. Se eu quiser confirmar realmente... precisa ser na hora em que o Barão pode estar lá."

            "Tenho que pensar direito em tudo o que eu descobri..."

            jump cassino_geral
        "Requisitar serviços especiais":


            python:
                if renpy.android:
                    credito = PythonSDLActivity.pegaCredito()
                    credito_total = PythonSDLActivity.pegaCreditoTotal()

            $ credito_ganho = credito_total - credito_atual
            $ credito_falta = credito_gold - credito_total
            $ credito_acumulado = 490000 + credito_total
            $ credito_ana = 250 * ana_evento
            $ renpy.block_rollback()

            mc "[ana]... tô precisando de uma companhia."

            ana "Seu cartão por favor."

            "..."

            if credito_total < credito_ana:

                ana "Clientes do cassino podem requerer serviços especiais toda vez que forem adicionados 250 créditos ao cartão como prêmio por apostas."

                ana "Seu [card] está com [credito_total] pontos. Você pode requisitar um novo serviço quando atingir [credito_ana]."

                mc "Entendi. Vou continuar jogando e ganhando créditos então."

                ana "Boa sorte, senhor."

                "Por que ela fala desse jeito? Como se fosse uma máquina, sei lá... tão formal..."

                jump cassino_ana_menu

            stop music fadeout 3.0

            ana "Aqui. Seu [card] de volta."

            mc "Obrigado."

            ana "Deixa eu colocar essas bebidas de lado e me ajeitar aqui rapidinho."

            ana "Upa."

            play music "audio/musica_7_sensual.mp3" loop

            scene ana mesa1 with Dissolve(2.0)

            pause

            if ana_evento == 1:

                $ ana_evento += 1

                mc envergonhado "..."

                ana "É a primeira vez que a gente conversa desde que você começou a jogar, né?"

                mc normal "Sim."

                ana "O que o senhor tá achando do Cassino do Barão?"

                mc "Eu-"

                ana "Opa. Espero não estar atrapalhando, meninos..."

                "Funcionário" "Não, não, [ana]. Fique à vontade."

                "Apostador" "Claro que não, [ana]."

                ana "Obrigada."

                ana "Desculpa, senhor. Você dizia..."

                mc "Não é nada. Tô gostando..."

                mc desconfiado "Se bem que eu tô perdendo mais do que ganhando eu acho..."

                ana "Não tem como perder aqui no nosso cassino. Em que outro lugar você pode olhar pra algo assim?"

                window hide

                pause

                mc desconfiado "Algo assim? Al-"

                mc surpreso "!"

                menu:
                    "(ficar com vergonha)":


                        mc envergonhado "..."

                        ana "Que fofo..."
                    "Tem razão. Vale bastante à pena.":


                        mc safado "Você tá certa. Vale muito à pena."

                        ana "Eu sei..."

                ana "É bem raro alguém reclamar da companhia das atendentes do cassino."

                ana "A gente sabe como cuidar dos nossos queridos clientes."

                mc envergonhado "Entendo..."

                ana "Eu não tenho tanto tempo disponível pra gente ficar conversando, senhor. Mas garanto que sempre vou ter algo novo pra você."

                ana "Se você quiser, é claro..."

                ana "Você entende o que eu quero dizer, né?"

                "Ela tá flertando comigo na cara dura e na frente de todo mundo. Será que isso é normal aqui no cassino?"

                ana "Seu jeito é muito fofo, sabia?"

                mc "Sei lá..."

                ana "Não sei como são as coisas no seu dia a dia, mas aqui no Cassino do Barão, seus maiores desejos se tornam realidade."

                ana "A oportunidade de ficar rico, garotas lindas ao seu dispor, bebida e comida com o máximo de refino."

                ana "O resto do mundo não interessa quando você tá aqui com a gente."

                menu:
                    "Você tem razão. É hora de curtir.":


                        mc tarado "Você tem toda razão."

                        mc "Nada como uma noite rodeado de lindas garotas, bebida até não aguentar mais e muito dinheiro!"

                        ana "O senhor realmente entende como curtir a vida."

                        mc safado "Eu quero curtir com você também, com certeza."

                        ana "Eu vou adorar cutir com o senhor."

                        mc "..."

                        ana "A gente vai ter outras oportunidades, confie em mim."
                    "Realmente... é fácil se iludir aqui.":


                        mc desculpa "Você tem razão. Olhando assim, realmente é bem fácil se perder nessa ilusão."

                        ana "Ilusão? O que o senhor quer dizer?"

                        mc "A gente vem pra cá, pro cassino, e essas luzes, os drinks, os jogos..."

                        mc "É fácil esquecer tudo o que tem lá fora, como se aqui fosse a realidade."

                        mc "Mas é claro que o Barão não é nenhum santo. Em troca, ele fica com uma parte do nosso dinheiro."

                        ana "..."

                        mc "Mas quando a noite acaba, ou o dinheiro... a gente precisa voltar lá pra fora e se lembrar que tudo continua igual quando a gente entrou."

                        mc "Talvez um pouco pior, porque agora a gente tá mais pobre do que antes..."

                        ana "Puxa..."

                        mc surpreso "Ah!"

                        mc envergonhado "Desculpa. Não queria acabar com o clima."

                        ana "Acho que o senhor tem razão em algumas coisas..."

                ana "Meu tempo acabou. Sua companhia foi incrível, senhor."

                ana "Quando tiver mais pontos, venha falar comigo. Vamos continuar de onde paramos."

                ana "Tenho muita coisa interessante pra mostrar pro senhor."

                mc normal "Boa noite, [ana]."

                ana "Boa noite."

                scene cassino geral with Dissolve(1.0)

                "Ficou meio tarde. Melhor eu voltar pra casa."

                "..."

                jump cassino_sair

            elif ana_evento == 2:

                $ ana_evento += 1

                ana "Sorte que o pessoal já tá acostumado com esse meu jeito."

                mc envergonhado "Um dia você ainda vai derrubar as fichas..."

                ana "Daí eu peço desculpas com jeitinho..."

                mc "..."

                ana "Eu não via a hora de poder passar um tempo com o senhor. Nossa última conversa foi MUITO interessante."

                mc charmoso "Eu também queria falar mais contigo."

                ana "Fico feliz."

                ana "Conversar é legal, mas eu tava pensando em uma coisa mais rápida e interessante..."

                ana "Sei lá... queria te mostrar algo diferente... talvez em um lugar mais reservado?"

                ana "O senhor gostaria de me acompanhar?"

                "O que será que ela tá querendo? Será que..."

                "E agora?"

                menu:
                    "Com certeza. Estou logo atrás de você.":


                        call ana_sexy from _call_ana_sexy
                    "Na verdade, eu quero só conversar.":


                        call ana_conversa from _call_ana_conversa

            elif ana_evento >= 3:

                $ ana_evento += 1

                ana "Eu ADORO passar um tempo a sós com o senhor."

                label ana_escolhe_evento:

                    ana "O que você vai querer fazer hoje?"

                menu:
                    "Eu quero que você me mostre algo interessante...":


                        call ana_sexy from _call_ana_sexy_1
                    "Eu quero só trocar uma ideia.":


                        call ana_conversa from _call_ana_conversa_1
                    "Pensando bem, não quero nada hoje.":


                        ana "Certeza? Você vai perder sua chance de passar um tempo comigo."

                        mc normal "Eu sei. Mas pode deixar que vou ganhar mais pontos e voltar."

                        ana "Um homem determinado? Incrível."

                        mc "Haha. Para de me zoar..."

                        ana "Estarei sempre no seu aguardo senhor."

                        mc "Valeu."

                        play music "audio/musica_3_cassino.mp3"

                        jump cassino_geral

            scene black with Dissolve(1.0)

            "{b}[mc] e [ana] passam mais de uma hora falando sobre variados assuntos{/b}"

            ana "Ai ai... tenho que voltar pro salão."

            mc "Já? Que pensa. Então eu vou pra casa. Baguncei demais por hoje."

            ana "Bom descanso."

            mc "E bom trabalho pra você."

            "..."

            jump cassino_sair

        "Vou querer meu drink da noite." if ( slots_ana_aviso or gold_card ) and not cassino_drink:

            $ cassino_drink = True

            if not gold_card:

                mc "Consegui juntar os 50 prontos e vou pegar o meu drink."

                ana "Parabéns, senhor. O que o senhor vai querer hoje?"
            else:


                ana "Veio pegar o drink da noite, senhor [mc]?"

                mc "Sim."

                ana "Qual deles você deseja?"

            mc "Hmmm..."

            menu:
                "Champagne":


                    mc "Me vê um champagne por favor."

                    ana "Aqui está."

                    show mc c_mc_drink with Dissolve(1.0)

                    mc "Obrigado."

                    ana "O champagne tem tudo a ver com cassino."

                    ana "Um espumante para comemorar após ganhar aquela bolada é o toque diferencial."

                    mc "Tem razão. Tá uma delícia."

                    ana "Só não vai querer pegar a garrafa e comemorar igual fazem na Fórmula 1."

                    mc "É proibido?"

                    ana "Não, mas eu teria que limpar..."

                    mc "Haha! Relaxa. Não vou fazer isso contigo."

                    ana "Obrigada."
                "Slippery Nipple":


                    mc "Slip... nipple? É isso mesmo?"

                    ana "Isso mesmo."

                    mc "Nipple não é mamilo? E sli-"

                    ana "Não precisa tentar traduzir ao pé da letra, senhor."

                    mc "Haha... ok..."

                    ana "Tá na mão."

                    show mc c_mc_drink with Dissolve(1.0)

                    mc "Valeu. Caraca. Esse drink tem duas camadas."

                    ana "Esse drink, quando feito da forma correta, exibe essas duas camadas bem distintas no copo."

                    ana "Ele é feito misturando dois outros drinks chamados Baileys Irish Cream e Sambuca."

                    mc "Muito interessante. Você realmente sabe sobre esses drinks."

                    ana "A gente aprende."
                "Bloody Mary":


                    mc "Vou querer o Bloody Mary."

                    ana "Perfeito. Bom drink."

                    show mc c_mc_drink with Dissolve(1.0)

                    mc "Esse aqui é gostoso, mas é bem diferente. Você sabe do que é feito?"

                    ana "O Bloody Mary é um drink feito com uma série de ingredientes que se eu falar talvez você ache estranho."

                    mc "Pode falar."

                    ana "Ele é preparado com vodka, suco de tomate, suco de limão, molho Worcester, que aqui a gente conhece como molho inglês e Tabasco."

                    mc "Quê?! Tem tudo isso aqui?!"

                    ana "Haha... sim, senhor."

                    mc "Caraca. Ouvindo assim parece uma loucura... Mas não é ruim, não."
                "Long Island Iced Tea":


                    mc "E esse chá gelado da ilha?"

                    ana "Esse drink é bem forte."

                    mc "Não tem problema. Pode mandar."

                    ana "Bom drink."

                    show mc c_mc_drink with Dissolve(1.0)

                    mc "{i}puaah{/i}"

                    mc "Forte mesmo."

                    ana "Esse é o drink mais forte que temos no Cassino do Barão."

                    ana "Ele é uma mistura de tequila, vodka, rum branco, triple sec, gin, suco de limão, um xarope feito com goma arábica e coca com gelo."

                    mc "Uou. O que é triple sec?"

                    ana "Triple sec é um licor francês com gosto de laranja. Ele não tem cor e adiciono um leve toque cítrico ao drink."

                    mc "Muitos detalhes..."

                    ana "Sim. Qualquer coisa errada e o drink já não é o mesmo."
                "Rusty Nail":


                    mc "Hoje vou querer o Rusty Nail."

                    ana "Saindo."

                    show mc c_mc_drink with Dissolve(1.0)

                    mc "Hmmm... muito bom."

                    mc "Rusty nail quer dizer prego enferrujado, né?"

                    ana "Haha. Sim. Inclusive, alguns bares oferecem o Rusty Nail com um prego enferrujado no copo."

                    mc "Sério?!"

                    ana "Sim. É um costume. Mas o drink em si não tem nada com prego."

                    ana "É uma mistura do whiskey Scotch e Drambuie."

                    mc "Drambuie?"

                    ana "Drambuie é uma marca de licor escocesa. Além do whiskey, ele tem mel e especiarias."

                    mc "Massa."

            show mc c_ana_mc with Dissolve(1.0)

            mc "Tava muito bom, [ana]. Valeu."

            show ana drink3 with Dissolve(1.0)

            ana "Não tem o que agradecer, senhor. Fico feliz que tenha gostado."

            ana "Tudo o que precisar, basta me chamar. Estou às suas ordens."

            mc "Ok."

            jump cassino_geral
        "Como tá o desempenho do meu [card]?":


            mc "Você pode ver no meu cartão como tá meu desempenho no cassino?"

            ana "Claro. Eu tenho meu aparelho aqui. Só um segundo."

            "..."

            python:
                if renpy.android:
                    credito = PythonSDLActivity.pegaCredito()
                    credito_total = PythonSDLActivity.pegaCreditoTotal()

            $ credito_ganho = credito_total - credito_atual
            $ credito_falta = credito_gold - credito_total
            $ credito_acumulado = 490000 + credito_total
            $ renpy.block_rollback()

            if not gold_card:

                ana "O senhor tem [credito] de crédito no seu Silver Card."
            else:


                ana "Uou. O senhor tem [credito] de crédito no seu Gold Card."

            ana "No total, seu cartão já tem [credito_acumulado] pontos. Isso é incrível!"

            if not gold_card:

                ana "Falta apenas mais [credito_falta] para você fazer o upgrade para o Gold Card."

                mc "Se comparado com tudo o que precisa, falta pouco mesmo."

                ana "Com certeza! Boa sorte nos próximos jogos!"

                mc "Valeu."
            else:


                ana "Você já tem o Gold Card. Meus parabéns. Você é um cliente vip do Cassino."

                ana "Continue jogando e um dia você pode entrar no nosso seleto grupo Platinum."

                mc "E como eu faço isso?"

                ana "Infelizmente, não é possível para o senhor no momento. Não se preocupe que quando for a hora você saberá."

                mc "Mistério..."

                ana "Haha! São só os procedimentos do Barão."

                mc "Entendo."

            jump cassino_ana_menu
        "Era isso. Obrigado.":


            mc "Valeu, [ana]. Era isso."

            ana "Boa diversão e muita sorte no Cassino do Barão."

            jump cassino_geral

label ana_sexy:

    if ana_sexy == 0:

        mc safado "Eu quero ver tudo. Estou logo atrás de você."

        ana "Só não vem tão coladinho..."

        mc "..."

        ana "Vamos até as mesas de Black Jack. Não tem ninguém jogando ali."

        mc "Ok."

        "..."

        scene cassino_blackjack with Dissolve(1.0)

        ana "Aqui tá bom. Não tô vendo ninguém perto agora."

        ana "..."

        mc surpreso "!"

        scene ana mesa2 with Dissolve(2.0)

        pause

        mc surpreso "..."

        ana "O que foi, senhor?"

        mc "É... é..."

        ana "Eu disse que eu ia te mostrar algo interessante... {i}rsrs{/i}"

        mc envergonhado "Bota interessante nisso..."

        ana "Pode olhar bem."

        window hide

        pause

        ana "Gostou?"

        mc safado "Como não gostar?"

        ana "Fico feliz."

        ana "É pra isso que nós estamos aqui. Pra vocês aproveitarem a noite."

        mc "..."

        ana "Tá bom?"

        mc "Não posso levar um quadro?"

        ana "{i}Rsrs{/i}"

        ana "Quando quiser ver, é só vir falar comigo."

        mc "Ok..."

        mc charmoso "Ok. Acho que já vou indo pra casa depois dessa."

        ana "Sei... Tenha uma boa noite, senhor."

        mc "Você também, [ana]."

        scene cassino geral with Dissolve(1.0)

        "Que loucura é essa? Posando pra mim desse jeito..."

        mc tarado "Bom... Eu não vou reclamar, é claro."

        scene black with Dissolve(1.0)

    elif ana_sexy == 1:

        ana "Então você gostou do que eu te mostrei da outra vez, né?"

        mc safado "Adorei."

        ana "Hoje eu vou te levar para um lugar diferente. Um lugar ainda mais reservado..."

        mc tarado "Claro. Onde você quiser."

        ana "Vem..."

        scene black with Dissolve(1.0)

        scene cassino_ponte3 with Dissolve(1.0)

        ana "Não tem ninguém aqui hoje. Melhor pra gente."

        ana "Entra aqui."

        mc charmoso "Tá."

        scene cassino_poker with Dissolve(2.0)

        mc surpreso "Uou..."

        ana "Essa aqui é uma sala especial."

        show ana c_ola with dissolve

        ana "Só nossos clientes Gold podem vir aqui."

        if gold_card:

            mc charmoso "Eu já tenho meu Gold Card."

            ana "Incrível. Agora então é só esperar e eles vão entrar em contato com você quando novas vagas forem abertas."

            mc "Estou ansioso."
        else:


            ana "Mas hoje você pode sentir um pouco do que te aguarda."

        ana "Hoje você ainda por cima tá acompanhado por uma atendente só sua."

        show ana c_provocando with dissolve

        ana "E eu vou subir nessa mesa e fazer uma graça para o senhor."

        mc safado "Tô louco pra ver..."

        ana "Então com sua licença."

        hide ana with dissolve

        "..."

        mc surpreso "!"

        scene ana mesa3 with Dissolve(2.0)

        pause

        ana "O que você acha?"

        mc tarado "Perfeita."

        ana "Fico feliz que o senhor tenha gostado."

        ana "Estamos aqui pra isso."

        window hide

        pause

        ana "Tenho mais algumas poses para o senhor."

        mc "Claro."

        scene black with Dissolve(1.0)

        "{b}[ana] passa os próximos minutos fazendo outras poses{/b}"

        ana "Ai ai... tenho que voltar pro salão."

        scene cassino_poker with Dissolve(2.0)

        show ana c_ola with dissolve

        mc desculpa "Já? Que pena. Então eu vou pra casa. Baguncei demais por hoje."

        ana "Da próxima vez, vou pensar uma pose nova para o senhor."

        mc safado "Vou ficar ansioso."

        ana "Bom descanso."

        mc "E bom trabalho pra você."

        hide ana with dissolve

        "..."

        scene black with Dissolve(1.0)

    elif ana_sexy == 2:

        ana "O que você acha da gente ir lá na nossa salinha especial?"

        "Apostador" "Que sala é essa?"

        ana "Continue jogando e você vai chegar lá, senhor."

        "Apostador" "{i}Hmpf{/i}"

        ana "Vamos?"

        mc tarado "Claro."

        scene black with Dissolve(1.0)

        scene cassino_ponte2 with Dissolve(1.0)

        ana "O pessoal saindo do hotel."

        ana "Quando o senhor se tornar um jogador Platinum, poderá usar todas nossas instalações gratuitamente."

        mc charmoso "Não vejo a hora."

        "..."

        scene cassino_poker with Dissolve(1.0)

        pause

        show ana c_ola with dissolve

        ana "O que o senhor quer que eu faça hoje?"

        mc safado "Pode subir na mesa quando quiser..."

        ana "O senhor não cansa?"

        mc "Nunca."

        scene ana mesa3 with Dissolve(2.0)

        pause

        ana "Assim?"

        mc "Sim."

        ana "Tenho outra para o senhor. Só deixa eu tirar os sapatos..."

        mc surpreso "!"

        scene ana mesa4 with Dissolve(2.0)

        pause

        ana "E assim? Você gosta?"

        mc envergonhado "Você tá é acabando comigo."

        ana "{i}Rsrs{/i}"

        ana "Fico feliz, senhor. Estou aqui pra lhe servir."

        mc safado "..."

        window hide

        pause

        ana "Tá bom?"

        mc tarado "Claro que não."

        ana "..."

        scene black with Dissolve(1.0)

        "{b}[ana] passa os próximos minutos fazendo outras poses{/b}"

        ana "Ai ai... tenho que voltar pro salão."

        scene cassino_poker with Dissolve(2.0)

        show ana c_ola with dissolve

        mc desculpa "Já? Que pena. Então eu vou pra casa. Baguncei demais por hoje."

        ana "Da próxima vez, vou pensar uma pose nova para o senhor."

        mc safado "Vou ficar ansioso."

        ana "Bom descanso."

        mc "E bom trabalho pra você."

        hide ana with dissolve

        "..."

        scene black with Dissolve(1.0)

    elif ana_sexy == 3:

        ana "Pronto?"

        mc charmoso "Sempre. Você vai na frente."

        ana "O senhor gosta da vista?"

        mc tarado "Como não?"

        scene black with Dissolve(1.0)

        scene cassino_ponte with Dissolve(1.0)

        ana "Eu acho que já vi esse casal brigando nesse mesmo lugar..."

        mc desconfiado "Sabia que eu acho que eu também?"

        "..."

        scene cassino_poker with Dissolve(1.0)

        pause

        show ana c_ola with dissolve

        ana "Nem precisa falar..."

        mc safado "Já aprendeu."

        ana "..."

        scene ana mesa3 with Dissolve(2.0)

        pause

        scene ana mesa4 with Dissolve(2.0)

        pause

        ana "E agora uma pose especial pro meu jogador PREFERIDO de todo o cassino..."

        mc surpreso "!"

        scene ana mesa5 with Dissolve(2.0)

        pause

        ana "Nessa pose... até eu fico sem jeito..."

        ana "Essa é a PRIMEIRA vez que eu faço isso..."

        mc tarado "Você tá linda."

        ana "Obrigada. Fico feliz que o senhor gostou."

        ana "Mesmo com vergonha, pode ver..."

        window hide

        pause

        ana "Posso parar?"

        mc safado "Só mais um pouquinho..."

        ana "{i}Hmpf{/i}"

        scene black with Dissolve(1.0)

        "{b}[ana] passa os próximos minutos fazendo outras poses{/b}"

        ana "Ai ai... tenho que voltar pro salão."

        scene cassino_poker with Dissolve(2.0)

        show ana c_ola with dissolve

        mc desculpa "Já? Que pena. Então eu vou pra casa. Baguncei demais por hoje."

        ana "Sempre que quiser me ver posar para o senhor, basta vir falar comigo."

        mc safado "Ok. Pode me esperar."

        ana "Vou estar ANSIOSA."

        ana "Bom descanso."

        mc "E bom trabalho pra você."

        hide ana with dissolve

        "..."

        scene black with Dissolve(1.0)

    elif ana_sexy >= 4:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("ana_sexy_final","ana","personagem")

        ana "O senhor vai querer o tour de sempre?"

        mc tarado "É o meu tour preferido."

        ana "Então pode vir comigo. Como se o senhor não soubesse o caminho..."

        mc "Hehe..."

        scene cassino_blackjack with Dissolve(1.0)

        ana "Vamos fazer uma parada aqui na mesa de Black Jack."

        ana "Aproveitar que não tem ninguém."

        mc tarado "Claro."

        scene ana mesa2 with Dissolve(2.0)

        pause

        ana "Podemos continuar com o tour?"

        mc safado "Podemos..."

        scene black with Dissolve(1.0)

        scene cassino_ponte with Dissolve(1.0)

        ana "Por aqui..."

        "..."

        scene cassino_poker with Dissolve(1.0)

        pause

        show ana c_ola with dissolve

        ana "Agora é hora do especial da casa."

        mc safado "Pode começar."

        ana "..."

        scene ana mesa3 with Dissolve(2.0)

        pause

        scene ana mesa4 with Dissolve(2.0)

        pause

        ana "E agora uma pose especial pro meu jogador PREFERIDO de todo o cassino..."

        scene ana mesa5 with Dissolve(2.0)

        pause

        ana "Gostou?"

        mc safado "Como sempre..."

        ana "Que bom. É isso que IMPORTA pra mim..."

        mc "Mas ainda falta um pouco..."

        ana "..."

        scene black with Dissolve(1.0)

        "{b}[ana] passa os próximos minutos fazendo outras poses{/b}"

        ana "Vou voltar pro salão."

        scene cassino_poker with Dissolve(2.0)

        show ana c_ola with dissolve

        mc desculpa "Ok. Então eu vou pra casa."

        ana "Sempre que quiser me ver posar para o senhor, basta vir falar comigo."

        mc safado "Ok. Pode me esperar."

        ana "Vou estar ANSIOSA."

        ana "Bom descanso."

        mc "E bom trabalho pra você."

        hide ana with dissolve

        "..."

        scene black with Dissolve(1.0)

    $ ana_sexy += 1

    jump cassino_sair

label ana_conversa:

    if ana_conversa == 0:

        ana "Conversar? {i}Rsrs{/i}"

        ana "Tem certeza?"

        mc normal "Sim."

        if ana_sexy > 1:

            ana "Não prefere fazer nosso tour por coisas interessantes pelo cassino?"

            mc envergonhado "Agora não..."
        else:


            ana "Mas você entendeu o que eu quis dizer?"

            mc envergonhado "Entendi..."

        if ana_sexy < 3:

            ana "O senhor é realmente um homem diferente..."

            mc zerado "Acho que eu já ouvi isso demais..."

            ana "Mas é mesmo! {i}Rsrs{/i}"

            mc "..."

        ana "Então... sobre o que o senhor quer conversar?"

        mc normal "Como é trabalhar no cassino? Você gosta?"

        ana "Eu?!"

        mc desconfiado "É. O que foi?"

        ana "Nada... é que não costumam perguntar o que eu acho das coisas..."

        mc normal "Deve ser meu espírito jornalístico."

        ana "Provavelmente..."

        ana "É..."

        ana "É BACANA trabalhar aqui..."

        mc desconfiado "Por que parece que você não tá sendo sincera?"

        ana "Eu? CLARO que é legal. Por que eu não gostaria?"

        mc desculpa "Sei..."

        "Tenho a impressão que ela não tá falando a verdade."

        ana "Acho que tá bom de conversa por hoje, não acha?"

        mc normal "Haha. Se você acha."

        if ana_sexy < 3:

            ana "Eu?"

            ana "..."

            ana "Você realmente é esquisito..."

            mc zerado "..."

        ana "Boa noite."

        mc "Boa noite, [ana]."

        scene cassino geral with Dissolve(1.0)

        "A [ana] é um pouco misteriosa, não sei. Tenho a impressão que ela nunca fala o que ela realmente pensa."

        "Talvez se eu continuar conversando com ela eu descubra alguma coisa não só sobre ela, mas também algo do Cassino do Barão."

        "Imagina se ela sabe algum segredo sujo sobre tudo aqui? Talvez pudesse virar até uma pauta."

        mc tarado "Isso seria incrível."

        "Só que perdi a vontade de jogar. Agora o negócio é ir pra casa."

    elif ana_conversa == 1:

        ana "Vai me dizer que quer conversar de novo comigo..."

        mc normal "Exatamente."

        ana "Não sei que tanto de interessante eu posso ter pra falar."

        mc charmoso "A gente só vai saber depois de conversar."

        ana "Será mesmo?"

        ana "Hmmm..."

        if ana_sexy < 3:

            scene cassino_roleta with Dissolve(1.0)

            ana "Olha..."

            show ana c_preocupada with dissolve

            ana "Mesmo com eu te oferecendo um serviço ESPECIAL... você continua só querendo falar comigo..."

            mc desconfiado "Que que tem?"

            ana "Eu... É a primeira vez que eu tô vendo isso..."

            ana "Não sei direito o que você tá querendo com isso."

            mc preocupado "Intenções? Como assim?"

            ana "Sei lá..."

            mc concentrando "Ai ai..."

            mc normal "Você tá achando que eu quero algo estranho com você?"

            ana "..."

            mc normal "Para de ser boba, [ana]."

            mc envergonhado "Bom... você é uma garota linda, engraçada, claro que talvez um pouquinho..."

            show ana c_ola with dissolve

            ana "{i}Rsrs{/i}"

            ana "Entendi entendi... acho que você tem razão."

            mc desconfiado "Tenho?"

            ana "Você não é um creepy. Só é estranho mesmo."

            mc zerado "Essa é toda a conclusão?"

            ana "Sim."

            mc "..."

            ana "Eu vou ter que voltar pro trabalho agora... mas talvez um dia a gente possa conversar melhor..."

            ana "Quem sabe você poderia passar aqui de manhã? Quando eu tiver saindo?"

            ana "A gente poderia fazer alguma coisa."

            mc normal "Parece uma excelente ideia."

            ana "Sério?"

            mc "Sim, ué."

            ana "Tá."

            ana "Então assim que eu tiver um tempo, vou te avisar e você vem me pegar?"

            mc envergonhado "Pegar?"

            ana "Me esperar na saída do trabalho, bobo..."

            mc surpreso "Ah!"

            mc envergonhado "Ok. Vou ficar esperando."

            ana "Obrigada. É..."

            show ana c_preocupada with dissolve

            ana "Mas... já que você quer fazer amizade comigo... e talvez um pouquinho mais..."

            ana "Não quero que você me chame pra fazer outras coisas mais... privadas aqui no cassino, tudo bem?"

            mc envergonhado "Acho que eu entendo..."

            ana "Claro que se você me chamar, eu vou ter que aceitar por conta do meu trabalho. E nem vou falar nada mais sobre isso pra você."

            ana "Mas... se eu pudesse escolher... eu escolheria que a gente se conhecesse de outra forma..."

            mc charmoso "Combinado. Vou manter isso em mente."

            show ana c_provocando with dissolve

            ana "Vai valer a pena me esperar, [mc]."

            ana "Boa noite."

            mc normal "Até."

            scene cassino geral with Dissolve(1.0)

            "A [ana] parece uma garota super sensual por fora, mas... algo dentro dela diz que ela não é assim."

            "Não sei. Pode ser só viagem minha... mas meu senso jornalístico está me dizendo que ela pode ser uma incrível companheira."

            "Tenho que me controlar."

            "Agora bora pra casa."
        else:


            ana "Fala a verdade... o senhor já viu muito mais que minha alma..."

            mc tarado "Vi mesmo..."

            ana "Acho que é muito melhor a gente fazer outra coisa, né?"

            mc "Também tô começando a achar..."

            ana "Quando quiser fazer algo um pouco mais... privado... junte os pontos e me avise, senhor."

            mc safado "Tá."

            ana "Agora vou trabalhar. Boa diversão."

            mc "A gente se fala."

            scene cassino geral with Dissolve(1.0)

            "Cansei. Acho que vou pra casa."

            "..."

    elif ana_conversa == 2:

        if ana_sexy >= 3:

            "A [ana] não quer conversar comigo..."

            "Depois de todos os shows privados que ela fez pra mim, agora nosso negócio é só físico."

            "Se eu quiser algo mais sério com ela... só se eu pudesse voltar no tempo e não tivesse chamado ela pros nossos 'tours'."

            "Pena que a vida real não permite voltar no tempo... Seria bem útil."
        else:


            "Eu tô esperando a [ana] me chamar pra eu pegar ela na saída..."

            "Essa frase ficou com duplo sentido. Mas deu pra entender."

            "Pera... por que eu tô falando comigo mesmo?"

            "Essas celebridades tão me deixando louco..."

        jump ana_escolhe_evento

    scene black with Dissolve(1.0)

    $ ana_conversa += 1

    jump cassino_sair

label cassino_jazz:

    $ cassino_area = "jazz"

    if fabricio_atencao == 1 and quincy_evento == 0 and show_diana:

        call quincy_evento1 from _call_quincy_evento1

    hide screen cassino_tela

    scene jazz geral with Dissolve(1.0)

    if v13_fim and diana_e3 == "nada":

        $ slots_evento30_viu = False
        $ slots_ana_aviso = False
        $ cassino_drink = False
        $ show_diana = False

        jump diana_evento3

    if randc == 1 and not show_diana:

        "Opa. Acho que hoje tem show da [d]."

        "Será que eu fico aqui pra ver?"

        if diana_namoro:

            "Agora que a gente tá namorando eu quero ver ela mais vezes, mas ela me pediu pra eu não fazer nada de diferente."

            "Ela não quer que ninguém saiba que a gente tá junto. Isso é uma bela merda..."

    elif randc != 1 and natasha_evento == 9:

        "Eu nunca mais vi a [na] aqui..."

        "O que será que aconteceu?"

        if natasha_e2 == "positivo":

            "Será que eu não devia ter falado pra ela sobre o Barão?"
        else:


            "Será que eu devia ter falado pra ela sobre o Barão?"










    show screen cassino_tela

    pause

label cassino_jazz_diana:

    hide screen cassino_tela

    "Vou ficar e assistir o show da [d]?"

    menu:
        "Sim":


            $ show_diana = True

            "Eu acho incrível ver a [d] cantando. Vou ver ela com certeza."

            "..."

            scene jazz corner with Dissolve(1.0)

            pause

            if cassino_roupa == "normal":

                show mc jazz_corner_normal with dissolve

            elif cassino_roupa == "blazer":

                show mc jazz_corner_blazer with dissolve

            elif cassino_roupa == "blacktie":

                show mc jazz_corner_blacktie with dissolve

            pause

            "Vai começar daqui a pouco..."

            if not gold_card:

                "Sorte que ela me deu o Silver Card. Parece que os bronzes não podem ver o show dela gratuitamente."
            else:


                "Agora que eu tenho meu Gold Card. Estou perto de conseguir o status máximo no cassino."

            "..."

            "Opa. Ai vem ela."

            show diana show1 with dissolve

            d "Boa noite, [mc]."

            mc "Boa noite."

            show pessoas_jazz with dissolve

            "A galera já tá juntando."

            "Tem uma moça animada demais ali..."

            pause

            d "Boa noite a todos."

            d "Peço o seu silêncio e a sua atenção, pois só assim o jazz pode invadir seu coração."

            show diana jazz_corner_cantando with dissolve

            $ renpy.choice_for_skipping()

            $ proibido_salvar = True
            $ show_quick_menu = False

            "..."

            play music "audio/musica_6_diana.mp3"

            $ renpy.pause(delay=5, hard=True)

            scene diana cantando1 at diana_esquerda with Dissolve(3.0)

            $ renpy.pause(delay=5, hard=True)

            scene diana cantando2 with Dissolve(3.0)

            scene diana cantando2 at diana_direita with Dissolve(3.0)

            $ renpy.pause(delay=5, hard=True)

            scene diana cantando3 with Dissolve(3.0)

            scene diana cantando3 at diana_esquerda with Dissolve(3.0)

            $ renpy.pause(delay=5, hard=True)

            scene diana cantando4 with Dissolve(3.0)

            scene diana cantando4 at diana_direita with Dissolve(3.0)

            $ renpy.pause(delay=5, hard=True)

            stop music fadeout 3.0

            scene black with Dissolve(2.0)

            scene jazz corner

            if cassino_roupa == "normal":

                show mc jazz_corner_normal

            elif cassino_roupa == "blazer":

                show mc jazz_corner_blazer

            elif cassino_roupa == "blacktie":

                show mc jazz_corner_blacktie

            show diana show1

            show pessoas_jazz

            show black

            hide black with Dissolve(1.0)

            $ proibido_salvar = False
            $ show_quick_menu = True

            play music "audio/musica_5_cassino3.mp3" loop

            "Garota Animada" "UHULLL! INCRÍVEL! DIANA VOCÊ É TUDOOOO!"

            "Homem Pomposo" "Excelente experiência."

            "Jovem Bêbado" "Quê? Acabou?"

            d "Agradeço a presença de todos."

            if diana_namoro:

                d "..."

                "Opa? Acho que ela mandou um beijo pra mim."

            hide diana with dissolve

            "Garota Animada" "DEUSAAAAAAAA! LACROU!"

            "Homem Pomposo" "Vamos nessa."

            "Jovem Bêbado" "Â?"

            hide pessoas_jazz with dissolve

            pause

            if natasha_e2 == "chefe":

                $ natasha_e2 = "diana"

                "Esses malucos..."

                "Opa! Não posso esquecer de falar com a [d] sobre o Barão."

                if diana_e3 != "horrivel":

                    "Não tenho certeza se é uma boa depois do que aconteceu aquele dia no quarto dela."

                    "Com certeza a relação dela com o Barão não é das melhores... mas isso só me deixa com mais vontade de falar com ela."

                "Se tem alguém que deve saber algo sobre o Barão é a [d]."

                "Espero que ela não fique chateada comigo..."

                mc "[d]!"

                scene jazz geral with Dissolve(1.0)

                mc normal "Ei, [d]..."

                d "[mc]?"

                show diana ola with dissolve

                d "Boa noite, [mc]. Eu vi você na plateia hoje."

                mc charmoso "Ah, sim. Seu show foi incrível, como sempre."

                d "Obrigada, sua visita significa muito pra mim."

                mc desculpa "[d]... posso te perguntar uma coisa?"

                d "Claro, fique à vontade."

                mc "O que você pode me falar sobre o Barão?"

                d "Como?"

                mc serio "Sobre o Barão..."

                show diana exibida with dissolve

                d "Por que você tá me perguntando sobre isso?"

                if diana_e3 != "horrivel":

                    d "Espero que não seja por conta daquela noite... no quarto..."

                    "E agora? O que eu falo?"

                    mc envergonhado "Não... é... pra revista..."
                else:


                    "Ixi..."

                    mc envergonhado "É coisa da revista..."

                d "Entendo... O que você quer saber?"

                mc desculpa "Qualquer coisa que você puder me falar sobre ele ajuda."

                d "Eu gostaria de poder falar um podre bem grande desse homem..."

                mc envergonhado "A é? Então..."

                d "Mas infelizmente eu não sei nada sobre ele."

                mc desconfiado "Nada?"

                d "Ele é meu... empregador. A vida que eu tenho é por ele..."

                d "... mas isso pode dar uma impressão errada. A gente não se conhece tão bem assim."

                d "Eu falo mais com advogados e produtores do que com ele mesmo."

                mc serio "Entendo..."

                d "Ele quase não vem pra cá. E quando vem ele só dá uma passada pelo cassino. Ele tem assuntos pra resolver no continente."

                "No continente..."

                d "Mas não me pergunte. Não tenho ideia do que ele vai fazer lá."

                mc desconfiado "Será que outra pessoa no cassino sabe?"

                show diana provocando with dissolve

                d "Quem sabe..."

                d "Ouvi dizer que algumas das mulheres que trabalham aqui fazem um tipo de {b}passeio especial{/b} com ele."

                d "Talvez uma delas possa te falar pra onde ele vai."

                "Passeio 'especial'? Isso parece algo mais terrível do que especial..."

                mc normal "Obrigado, [d]. Vou ver se consigo mais informações."

                d "Boa sorte com sua matéria. Venha ver meu show mais vezes."

                mc charmoso "Pode deixar."

                d "Bye bye."

                hide diana with dissolve

                "Hmm..."

                "Então o Barão tem coisas na parte continental da capital... que estranho..."

                "Por que o dono da maior atração da ilha, um cassino desse tamanho, teria negócios fora daqui?"

                "Provavelmente tudo o que ele precisa, tipo administração, contabilidade etc... caberia aqui no próprio cassino."

                "Mas por algum motivo ele vai pra parte continental..."

                "Talvez eu possa descobrir algo com mais alguém aqui no cassino... mas quem?"

                "..."
            else:


                if diana_namoro:

                    "Essa minha gata é incrível mesmo. Dá nem pra acreditar que a gente tá juntos."

                    "Parece que agora a música dela tá ainda mais emocional pra mim. Parece que eu sinto melhor o que ela quer passar."

                    "Não vejo a hora de ver ela de novo fora daqui pra gente poder namorar."
                else:


                    "Hoje foi incrível como sempre. A [d] realmente tem muita classe."

                    "A música dela traz um sentimento diferente. Tem um tom, sei lá... emocional. Como se ela cantasse com o coração."

                    "Agora eu só tô parecendo um idiota. Deixa eu sair daqui."

                hide mc with dissolve

                "..."

            jump cassino_jazz
        "Não":


            "Talvez outra hora."

            jump cassino_jazz

label quincy_morte_evento:

    stop music

    play sound "extra/start.mp3"



    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.block_rollback()





    qui "OooOoOooOOooi, amigo."

    qui "Eu sei que você tá aí. Eu sei que noooOOOoOoooOo fundo é você quem controla o [persistent.mc]."

    qui "Você. Segurando esse celular."

    qui "Eu voOoOOoooOOu descobrir seu nome. E quando isso acontecer a gente vai se encontrar de noOooOoooOOOooOvo."

    qui "Aproveite o joOoOOOOOOoooOooogo até lá."

    $ persistent.quincy_especial = True

    $ renpy.full_restart()

label quincy_evento1:

    $ persistent.mc = mcpnome

    $ quincy_evento = 1

    $ renpy.choice_for_skipping()

    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.block_rollback()

    stop music

    show black with Dissolve(0.2)

    show quincy_terror1 with Dissolve(0.3)

    hide quincy_terror1

    hide black with Dissolve(0.2)

    "Opa. A luz piscou."

    "Caraca. Não tem ninguém aqui."

    show black with Dissolve(0.2)

    show quincy_terror1 with Dissolve(0.3)

    hide quincy_terror1

    hide black with Dissolve(0.2)

    "De novo. Deixa eu sair daqui."

    scene jazz geral with Dissolve(1.0)

    "Talvez eu devesse avisar algué-"

    scene black

    show quincy_terror1 with Dissolve(0.3)

    hide quincy_terror1 with Dissolve(0.3)

    "Hâh? O que é isso?!"

    scene quincy_chao with vpunch

    pause

    mc angustiado "AARGH!"

    $ qui_nome = "???"

    qui "Huhuhu..."

    "Que merda é essa saindo do chão?!"

    mc "Qu-quem é você?!"

    qui "Assustou, [mc]?"

    mc "Co-co-como você sabe meu nome?!"

    qui "Eu sei de voooOooOOocê, tanto quanto você sabe de mim..."

    mc "Eu n-não sei na-nada d-disso!"

    qui "Ahhh... será?"

    scene black with dissolve

    mc "Ei! Não se aproxime."

    scene quincy cassino_falando with Dissolve(1.0)

    pause

    $ qui_nome = "Quincy"

    qui "Meu nooOoOoome é Quincy Jones."

    mc "Qui-qui!"

    "A mina que o [gar] me deu a pauta! Ele disse que ela podia..."

    "O filha da puta me dedurou!"

    qui "Não. OoooOooOOOooo [gar] não me disse nada. Mas, veja bem... você é um tanto quanto... famoooOooOOoOoso..."

    menu:
        "Eu só tava fazendo meu trabalho...":


            mc desculpa "Me perdoe, mas eu só tava fazendo meu trabalho..."

            qui "Parece tão fácil pedir desculpas agoooOoOOOooOoOOora, né?"

            mc "..."
        "Vai se foder!":


            mc irritado "Para de brincadeira, sua louca! Vai se foder!"

            qui "Garoto mal educado."

            mc angustiado "Âh?!"

            if not persistent.quincy_especial:

                $ renpy.block_rollback()

                scene black with vpunch

                qui "Huhuhu"

                play sound "audio/som_33_quincy.mp3"

                $ persistent.quincy_morte = True

                $ renpy.pause(delay=5, hard=True)

                $ renpy.full_restart()
            else:


                qui "De novo isso? Você não aprende?"

                mc desconfiado "Quê?"

                qui "Não importa..."
        "Desculpa! Por favor!":


            mc angustiado "Desculpa! Eu não que-queria isso!"

            qui "Huhuhu..."

            mc "!"

    qui "?"

    mc preocupado "?"

    qui "Que estranho..."

    qui "Você. Você tem uma energia diferente."

    mc "Energia?"

    qui "É como se você não fosse você."

    mc desconfiado "Como assim?"

    qui "É como se você tivesse alguém comandando suas ações. ComooOoOOOooOoOoOoo se você não tivesse vontade própria."

    mc desculpa "Bom... eu tenho meu chefe. Mas não diria que ele coman-"

    qui "Não! Você não entendeu! Não é nada disso."

    qui "Vou continuar te oOoOOoOoOooolhando."

    qui "Você acabou com minha privacidade noOoOOoOoOoo bar. Agora eu terei que beber aqui no Cassino do Barão."

    qui "Talvez... a gente se fale de nOoOooOooovo... quem sabe."

    scene black with dissolve

    scene jazz geral with Dissolve(1.0)

    "Ah?"

    "Que me-merda foi essa?"

    "Então essa é a maga Quincy Jones..."

    "Onde eu me meti?"

    play music "audio/musica_5_cassino3.mp3" loop

    $ proibido_salvar = False
    $ show_quick_menu = True

    $ renpy.block_rollback()

    return

screen cassino_tela():
    tag cassino

    predict False
    zorder 100
    modal True

    if cassino_regiao == "apostas":

        if not cassino_area == "geral":

            imagebutton auto "images/cassino/cassino_%s.png":
                xalign 0.05
                yalign 0.95
                action Jump("cassino_geral")

        else:

            imagebutton auto "images/mapa/ilha_%s.png":
                xalign 0.05
                yalign 0.95
                action [ Hide("cassino_tela"), Jump("cassino_voltar") ]

            imagebutton auto "images/cassino/casher_%s.png":
                xalign 0.05
                yalign 0.75
                action Jump("cassino_casher")

        if not cassino_area == "slots":

            imagebutton auto "images/cassino/slots_%s.png":
                xalign 0.15
                yalign 0.95
                action Jump("cassino_slots")

        else:

            add "images/cassino/slots_hover.png":
                xalign 0.15
                yalign 0.95

            imagebutton auto "images/cassino/mc_slots_%s.png":
                xalign 0.05
                yalign 0.75
                action Jump("slots_minigame_pre")

        if not cassino_area == "roleta":

            imagebutton auto "images/cassino/roleta_%s.png":
                xalign 0.25
                yalign 0.95
                action Jump("cassino_roleta")

        else:

            add "images/cassino/roleta_hover.png":
                xalign 0.25
                yalign 0.95

            imagebutton auto "images/cassino/ana_%s.png":
                xalign 0.05
                yalign 0.75
                action Jump("cassino_ana")

        if not cassino_area == "blackjack":

            imagebutton auto "images/cassino/ponte_%s.png":
                xalign 0.35
                yalign 0.95
                action Jump("cassino_ponte")

    if cassino_regiao == "complexo":

        if not cassino_area == "ponte":

            imagebutton auto "images/cassino/ponte_%s.png":
                xalign 0.05
                yalign 0.95
                action Jump("cassino_ponte")

        else:

            imagebutton auto "images/cassino/cassino_%s.png":
                xalign 0.05
                yalign 0.95
                action Jump("cassino_geral")

        if not cassino_area == "jazz":

            imagebutton auto "images/cassino/jazz_%s.png":
                xalign 0.15
                yalign 0.95
                action Jump("cassino_jazz")

        else:

            add "images/cassino/jazz_hover.png":
                xalign 0.15
                yalign 0.95

            if randc == 1 and not show_diana:

                imagebutton auto "images/cassino/diana_%s.png":
                    xalign 0.05
                    yalign 0.75
                    action Jump("cassino_jazz_diana")

            elif not randc == 1 and natasha_e1 != "nada" and not natasha_falou and natasha_evento < 9:

                imagebutton auto "images/cassino/natasha_%s.png":
                    xalign 0.05
                    yalign 0.75
                    action Jump("natasha_evento")

label ganha_gold:

    $ gold_card = True
    $ card = "Gold Card"

    "Opa! Acho que eu consegui os pontos que eu precisava pra pegar o Gold Card!"

    "Talvez eu tenha me perdido na conta, mas acho que não."

    "Vou passar no guichê e confirmar."

    "..."

    scene cassino_guiche1 with Dissolve(1.0)

    "Atendente" "Boa noite, senhor."

    mc normal "Boa noite."

    mc "É... eu acho que eu consegui os pontos necessários para pegar meu Gold Card."

    scene cassino_guiche2 with dissolve

    "Atendente" "Sério mesmo?!"

    mc desconfiado "Ué? Qual o problema?"

    "Atendente" "Você precisa ganhar mais de C$ 500 mil jogando no cassino para obter o Gold Card."

    mc envergonhado "Então... acho que eu eu consegui."

    "Atendente" "Hmmm... deixa eu conferir seu cartão."

    mc serio "Tá aqui."

    "Atendente" "..."

    "Atendente" "E não é que você está certo?"

    mc surpreso "Eu realmente consegui?!"

    "Atendente" "Sim... você está com [credito_total]. Isso te tá direito ao Gold Card e todas as vantagens."

    scene cassino_guiche1 with dissolve

    "Atendente" "Aliás, peço desculpas. Não achei que você ia conseguir isso."

    "Atendente" "Mas você merece. Aqui está seu Gold Card."

    play sound "extra/carta.mp3"

    "{b}[mc] recebeu Gold Card{/b}"

    mc charmoso "Valeu."

    "Atendente" "Com esse cartão você tem direito a drinks gratuitos todos os dias no cassino."

    "Atendente" "Você também é considerado um de nossos jogadores VIPs, com muitos outros benefícios."

    "Atendente" "Nos próximos dias você pode falar com nossas atendentes e elas vão te passando todas as vantagens."

    mc normal "Obrigado."

    "Atendente" "Esperamos que você continue aproveitando todo o entretenimento do Cassino do Barão."

    mc "Com certeza."

    "Atendente" "E qualquer coisa que precisar, me procure. Estou sempre às ordens, senhor [mc]."

    mc "Até."

    jump cassino_geral

label atendente_cena:

    "Ops, parece que tem uma moça vindo na minha direção."

    mc desconfiado "E que roupa é essa?"

    show atendente cassino_bemvindo with Dissolve(1.0)

    ate "Bem vindo ao Cassino do Barão, senhor. Estou ao seu dispor."

    mc surpreso "Você! A garota da loja!"

    ate "Tenha calma, senhor. Sou eu mesmo."

    mc desconfiado "Você faz bico aqui?"

    ate "Não devíamos falar sobre isso agora. Esta noite é para o senhor se divertir e fazer o que desejar."

    ate "Esqueça o que existe lá fora. O Cassino do Barão é onde você pode ser quem quiser."

    menu:
        "Assim que eu gosto. Vamos focar no Cassino.":


            mc tarado "Isso aí. Melhor a gente esquecer as complicações e focar na diversão."

            mc "Tô sentindo que a noite vai ser incrível."

            ate "Com certeza, senhor. Você terá uma noite inesquecível."
        "Entendo, mas eu queria saber mais sobre você.":


            $ atendente_seducao += 1

            mc charmoso "Entendo, mas mesmo assim queria saber mais sobre você. Pode me falar?"

            show atendente cassino_timida with Dissolve(1.0)

            ate "É..."

            mc "O que foi?"

            ate "É que ninguém nunca tinha perguntado isso dessa forma..."

            mc "Dessa forma?"

            ate "Normalmente os visitantes só se interessam por mim quando estão dando em cima."

            ate "Acho que é a primeira vez que alguém perguntou sobre mim parecendo estar interessado de verdade."

            ate "Foi... diferente."

            mc desculpa "A gente se viu outras vezes, só achei que seria educado."

            ate "Você parece ser um rapaz muito bacana."

            ate "Re-respondendo sua pergunta, na verdade eu faço bico na loja de roupas."

            mc desconfiado "Sério? Mas você não trabalha de manhã e à tarde lá?"

            ate "Sim. Mas mesmo trabalhando menos, o Cassino me paga muito mais."

            mc charmoso "Você deve ser uma boa funcionária."

            ate "Haha... não. Todas as garotas ganham muito bem aqui. A gente..."

            show atendente cassino_contrariada with dissolve

            ate "Deixa pra lá. Não é nada importante..."

            ate "..."

            mc preocupado "..."

            "Melhor eu mudar de assunto."

            mc charmoso "Entendi. Mas estou pronto pra uma noite muito foda."

            ate "Ah!"

            show atendente cassino_bemvindo with dissolve

            ate "Tenho certeza que o senhor vai viver uma experiência única aqui."
        "Esse tipo de apelo não funciona comigo.":


            mc zerado "Esse tipo de apelo é um pouco exagerado demais."

            show atendente cassino_contrariada with Dissolve(1.0)

            ate "Me desculpe, senhor. Não era minha intenção desagradar..."

            mc envergonhado "Ah, não é pra tanto."

            mc "Você só tá fazendo seu trabalho."

            show atendente cassino_bemvindo with dissolve

            ate "Isso! Obrigada por entender, senhor."

    ate "Para que eu possa te atender melhor, o senhor pode me dizer se você possui algum de nossos {b}cartões de jogador{/b}?"

    mc desconfiado "Cartão de jogador?"

    ate "Nós temos vários cartões que são distribuídos de acordo com a {b}quantidade de dinheiro que o senhor joga no Cassino{/b}."

    ate "Existe o Bronze, Silver, Gold e Platinum. Cada cartão te dá vantagens maiores no Cassino, como acesso a áreas VIPs e serviços exclusivos."

    mc normal "Entendi. Eu tenho o {b}Silver Card{/b}."

    ate "Então o senhor já é um veterano aqui."

    show atendente cassino_contrariada with dissolve

    ate "Estranho... eu não lembro de ter visto o senhor aqui antes."

    ate "Normalmente eu guardo o rosto de todos os clientes. Eu sou realmente boa em reconhecer as pessoas."

    mc envergonhado "Na verdade eu ganhei este cartão de uma amiga. Esta é a primeira vez que eu venho ao Cassino."

    show atendente cassino_bemvindo with dissolve

    ate "Isso explica tudo. Então, novamente, seja muito bem vindo e aproveite sua noite."

    mc normal "Obrigado."

    if d2_blacktie or cassino_roupa == "blacktie":

        ate "Pelo traje do senhor, não tenho dúvidas que você veio pronto para deixar sua marca por aqui."

        mc charmoso "Com certeza. Um lugar VIP como este merece um traje à altura."

        ate "Como eu disse ao senhor lá na boutique, com todo o respeito, ele te deixa sexy."

        mc charmoso "Muito obrigado."

    elif d2_blazer or cassino_roupa == "blazer":

        ate "Vejo que o senhor está usando o blazer que você comprou na boutique."

        mc normal "Sim."

        ate "Ele caiu realmente muito bem no senhor. Ficou lindo."

        mc "Obrigado."
    else:


        show atendente cassino_contrariada with dissolve

        ate "Só gostaria que o senhor soubesse que mesmo seu traje não combinando com o restante dos outros visitantes, não é isso que importa, ok?"

        mc envergonhado "Sei que meu traje não é o mais adequado, mas sabe como é a vida..."

        ate "Eu entendo perfeitamente. Fique à vontade."

        mc normal "Obrigado."

        show atendente cassino_bemvindo with dissolve

    ate "Então vou deixar o senhor conhecer nossas instalações, conversar com as outras garotas e aproveitar ao máximo sua noite."

    menu:
        "Obrigado. Boa noite e bom trabalho.":


            mc normal "Obrigado pela atenção. Tenha uma boa noite."

            ate "Boa noite, senhor."
        "Outras garotas?!":


            mc tarado "Como assim outras garotas?"

            ate "O Cassino oferece uma vasta gama de garotas para deixar sua noite ainda mais especial."

            ate "Elas estão espalhadas pelo complexo para lhe atender da forma que o senhor precisar."

            "Me atender?! Essa frase dela pode significar tantas coisas..."

            mc "Ok, muito bom saber. Boa noite."

            ate "Boa noite, senhor."
        "Espero poder ver você novamente ainda hoje.":


            $ atendente_seducao += 1

            mc charmoso "Agradeço toda sua atenção e não vejo a hora de poder ver você novamente pelo Cassino."

            show atendente cassino_timida with dissolve

            ate "Seria uma honra."

            mc "A honra seria minha. Mesmo a gente falando pouco, adorei sua companhia. E além de tudo você é linda."

            ate "Obrigada, senhor. O senhor também é um rapaz diferenciado."

            mc "Obrigado. Até mais, então."

            ate "Até. Beijos..."

    hide atendente with dissolve

    "Certo. Que coisa encontrar ela aqui no Cassino."

    "Deve ser um inferno trabalhar nos três períodos do dia. Não é fácil essa vida..."

    "Bom! Agora é hora de se divertir. Bora ver o que esse Cassino tem a oferecer!"

    "..."

    return

label cassino_ana_cena:

    mc surpreso "Uou!"

    mc envergonhado "Quer dizer..."

    "Para de passar vergonha, [mc]..."

    if d2_blacktie or cassino_roupa == "blacktie":

        show mc blacktie with dissolve

    elif d2_blazer or cassino_roupa == "blazer":

        show mc blazer with dissolve

    "Olha só pra isso! A música, as pessoas jogando, as pessoas bebendo, as pessoas..."

    "Acho que tô até um pouco tonto."

    "Espera... essa placa aqui diz..."

    "{i}Salão Principal{/i}"

    "E tem indicações para outros lugares. Deixa eu ver."

    "{i}Hotel{/i}"

    "{i}Shopping{/i}"

    "{i}Área de Entretenimento{/i}"

    "{i}Jazz Corner{/i}"



    "{i}Heliporto{/i}"

    mc "Caralho!"

    "Tem até um heliporto! Olha só pra tudo isso, mano!"

    "{i}Área Platinum{/i}"

    "Hmm... Área Platinum? O que será isso?"

    "Deve ter algo a ver com o {b}Platinum Card{/b} que a moça me falou na entrada."

    hide mc with dissolve

    "..."

    "Tudo isso... em um único prédio... É de deixar qual-"

    show ana c_ola with moveinbottom

    "Garota" "Boa noite, senhor."

    if nathan_e1 != "nada":

        mc surpreso "Você!"

        mc desconfiado "Você... [ana], não é?"

        ana "Isso mesmo, senhor. Não acredito que lembrou."

        mc charmoso "Não tenho como esquecer."

        ana "Desculpa não lembrar o seu..."

        mc "Não esquente com isso. Meu nome é [mcc]."

        ana "Verdade."
    else:


        mc normal "Boa noite."

        "Ixi, esqueci de perguntar o nome da outra garota. Vou falar de uma vez."

        mc "Desculpa, como é seu nome?"

        ana "Sou a [ana]."

        mc charmoso "Muito prazer."

        ana "O prazer é meu, senhor."

    if nge == "Ana":

        mc envergonhado "Aquele lance no bar..."

        ana "Não precisa ficar envergonhado. Eu gostei bastante."

        mc "Eu também..."

        "..."

        mc "É..."

    if karli_p_tadaima:

        mc desconfiado "Você não tá trabalhando no Tadaima no lugar da [m]?"

        ana "Sim, senhor."

        ana "O Cassino paga muito bem pra gente deixar um bico desses passar batido."

        ana "E a gente nem precisa fazer nada tão..."

        ana "Bom, esquece."

    mc normal "Então você tá aqui no Cassino. Não imaginei."

    ana "Sim. O dinheiro realmente é bom."

    mc charmoso "Entendo. Que bom que tá valendo à pena."

    ana "Eu acho que você ainda vai encontrar outras garotas que você conhece por aqui."

    mc desconfiado "Como assim?"

    ana "O Cassino é o maior empregador de garotas bonitas da ilha."

    menu:
        "Entendo.":


            mc normal "Entendo. Então devem ter outras garotas aqui."

            ana "Sim. E como a ilha é pequena, provavelmente todo mundo que mora aqui acaba se conhecendo alguma hora."

            mc "Isso é verdade."

            ana "Toma cuidado se você não tá acabando seus relacionamentos da melhor forma."

            mc envergonhado "..."
        "É por isso que você trabalha aqui, né?":


            mc charmoso "As garotas mais bonitas? Por isso você trabalha aqui. Agora entendi."

            show ana c_provocando with dissolve

            ana "Você já pegou quantas garotas com essas cantadas baratas?"

            mc "Só tô fazendo uma constatação."

            ana "A é?"

            mc "Você sabe que você é linda. Além de ser sexy também."

            ana "..."
        "Por que você diz isso?":


            mc desconfiado "Por que você diz isso?"

            ana "Quase todas as garotas que querem uma grana boa e não se importam muito com alguns detalhes vêm trabalhar aqui."

            mc "As condições de trabalho são tão boas assim?"

            show ana c_preocupada with dissolve

            ana "Não é bem isso..."

            mc "..."

            ana "A grana é boa. Isso que importa."

            mc "Entendi..."

            mc "E que detalhes são esses que você disse?"

            ana "Não é nada de mais. Pode esquecer que eu falei isso, senhor."

            ana "..."

            "O que será que ela tá querendo esconder de mim?"

    show ana c_ola with dissolve

    ana "Todas nós estaremos aqui para atender você. Qualquer coisa que precisar, QUALQUER coisa pode me chamar, ok?"

    mc normal "Ok. Obrigado."

    if d2_blacktie or cassino_roupa == "blacktie":

        show ana c_provocando with dissolve

        ana "E só pela sua roupa dá pra ver que você tem o que precisa pra curtir muito a noite."

        mc charmoso "Você acha?"

        ana "Com certeza. Não é qualquer um que usa um smoking desses. Mesmo aqui no Cassino."

        mc "Entendo..."

    elif d2_blazer or cassino_roupa == "blazer":

        ana "E tô vendo que você veio muito bem vestido. Pontos a mais pra você."

        mc charmoso "Você achou?"

        ana "Com certeza. Esse blazer caiu muito bem em você."

        mc "Obrigado."
    else:


        ana "Se bem que... quer uma dica?"

        mc normal "Claro."

        ana "Normalmente o pessoal dá mais bola pra quem tá melhor vestido."

        ana "Se eu fosse você, juntava uma graninha e pegava um blazer ou até um black tie pra ficar gato."

        mc envergonhado "Valeu a dica, mas sabe como é, né? A grana tá apertada..."

        ana "E eu não sei, disso? Mas não esquente. É só um toque mesmo."

    show ana c_provocando with dissolve

    ana "Bom... desculpa roubar seu tempo. Se o senhor precisar de alguma coisa, me chama, tá?"

    mc normal "Valeu, [ana]."

    hide ana with dissolve

    "Hmmm..."

    if d2_blacktie or cassino_roupa == "blacktie":

        show mc blacktie with dissolve

    elif d2_blazer or cassino_roupa == "blazer":

        show mc blazer with dissolve

    "Então além da [ana] e daquela garota da boutique, outras jovens trabalham aqui."

    "Essa cassino parece que tem alguma coisa que atrai todas essas garotas."

    "Quem mais será que eu vou encontrar?"

    hide mc with dissolve

    return

label cassino_evento:

    $ cassino_evento = "finalizado"
    $ silver_card = True

    "Nem acredito que a [d] realmente me deu um cartão para poder jogar no Cassino do Barão!"

    "E ela ainda me deu um {b}Silver Card{/b}! Pra pegar um destes a pessoa tem que ganhar centenas de milhares de C$ jogando."

    "Então a partir de agora eu vou poder visitar o cassino quando eu quiser."

    "O salão de apostas abre durante a noite e eu posso curtir até não aguentar mais."

    mc normal "Caralho, tô muito ansioso pra ver o que vai rolar lá."

    "Finalmente vou começar a sentir o que é viver em uma ilha paradisíaca."

    mc zerado "Porque até agora só tá sendo chumbo no lombo..."

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
