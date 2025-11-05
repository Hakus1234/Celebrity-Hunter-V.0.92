label quincy_evento2:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("quincy_evento2","a","a")

    $ quincy_e1 = True

    "Onde será que eu saio hoje?"

    "Tem umas baladas bem massa lá no centro."

    mc tarado "Talvez eu pegue uma novinha e dê uma sarr-"

    q "Ei!"

    mc desconfiado "Hm?"

    q "Você aí!"

    mc angustiado "Quem tá falando?!"

    q "Aqui em cima, idiota!"

    mc "Quê?!"

    scene quincy_ponto_acenando with Dissolve(1.0)

    pause

    q "Tudo bem aí embaixo?"

    mc desconfiado "Que merda você tá fazendo aí?"

    q "Daqui eu posso ver a lua melhor."

    mc zerado "Eu tenho quase certeza que não faz diferença nenhuma olhar a lua daqui ou daí."

    q "É o que você pensa. Alguns metros mais perto ou mais longe da lua e tudo muda."

    mc "Não me diga..."

    q "Você sabe algo sobre a lenda da lua cheia?"

    mc zerado "Não é mais fácil você descer se tá afim de conversar?"

    q "Será que você morreu e esqueceram de enterrar?"

    mc "Ei..."

    q "Upa!"

    scene cidade onibus_noite with hpunch

    mc surpreso "Uou!"

    show quincy seria with moveinbottom

    q "Eu perguntei se esqueceram de te enterrar."

    mc zerado "Eu escutei da primeira vez."

    mc desconfiado "Tá falando que eu tô morto só porque eu não acredito no poder das fases da lua?"

    q "Sua descrença ainda será o motivo da sua ruína."

    menu:
        "A é? Fala mais aí sobre minha ruína.":


            mc charmoso "Sério? Fala aí então sobre a minha ruína."

            q "Você é mesmo muito engraçadinho."

            q "Você não tá levando à sério coisas que são muito importantes."

            mc "Tipo?"

            q "Calma. Deixa eu explicar."
        "Foi legal te conhecer, mas tchau.":


            mc envergonhado "Bom. Foi legal conversar com você, mas acho que já vou indo. Adeus."

            "Que mina doida."

            q "Ei!"

            mc desconfiado "Hm?"

            show quincy provocando with dissolve

            q "Eu tô me sentindo tão sozinha... será que você não podia me fazer companhia até o ônibus chegar pelo menos?"

            mc surpreso "!"

            mc envergonhado "Talvez... uma pequena companhia."

            q "Muito obrigada, moço."

    q "Eu vi que você não acredita muito em coisas paranormais."

    mc charmoso "Olha. Não quero ser grosso e talz, mas eu acho isso meio balela."

    show quincy invocada with dissolve

    q "Você sabia que existem vários fenômenos que o homem não consegue explicar, né?"

    q "Não é de hoje que as pessoas falam sobre aparecimento de espíritos."

    mc preocupado "Eu não sei se quero falar sobre isso."

    q "Pensa. É só você procurar na internet. Procura sobre fenômenos espirituais e você vai achar um monte de casos."

    mc desconfiado "Mas nada disso foi comprovado pela ciência."

    q "Aí é que tá. A ciência não tem capacidade de entender essas coisas ainda."

    q "Até uns anos atrás os cientistas achavam que o átomo era a menor partícula que existe. E hoje já viram que ele é feito de outras coisas menores."

    mc envergonhado "Você tá querendo dizer que a ciência não tem capacidade de provar, sei lá, espíritos, fantasmas e coisas assim?"

    show quincy costas with dissolve

    q "Existem muitas coisas inexplicáveis pra ciência, [mc]."

    q "Não é porque eles não conseguem entender que elas não existem. Existem coisas que estão ao seu lado e você nem vê."

    q "Nesse momento mesmo. Enquanto você mexe no celular. Atrás de você."

    mc desconfiado "Eu nem tô mexendo no celular, sua louca."

    q "Huhuhu..."

    "Cara, que mina doente..."

    mc desconfiado "Aliás, eu não sei seu nome."

    q "Meu nome?"

    q "..."

    show quincy alegre with dissolve

    $ q_nome = "Selena"

    q "Pode me chamar de [q]."

    menu:
        "É um nome bonito.":


            mc charmoso "É um nome diferente, muito bonito."

            q "Eu sou bem criativa."

            mc desconfiado "Como?"
        "Nunca ouvi esse nome na minha vida.":


            mc envergonhado "É um nome bem incomum. Nunca tinha ouvido."

            q "É em homenagem ao nosso encontro."

            "Por que parece que nada que essa mina fala faz sentido?"

            mc "A é? Que legal..."

    q "Eu gostei bastante de conversar com você."

    mc envergonhado "Que bom..."

    q "Agora eu vou indo nessa. Boa noite."

    hide quincy with dissolve

    mc zerado "..."

    q "Ei!"

    scene quincy_ponto_acenando with Dissolve(1.0)

    q "A lua tá me dizendo que a gente vai se encontrar de novo. Bacana, né?"

    mc zerado "Como você já tá aí?"

    q "Você dorme no ponto, [mc]."

    mc zerado "Trocadilho horrível..."

    mc normal "Tchau!"

    scene cidade onibus_noite with Dissolve(1.0)

    "Essa ilha realmente tá cheia de gente estranha."

    "..."

    $ tempo += 1

    jump call_cidade

label quincy_evento3:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("quincy_evento3","a","a")

    scene praia_gazebo_especial with Dissolve(1.0)

    pause

    if not quincy_e2_comecou:

        "Caraca. A noite parece diferente hoje."

        "Essa lua... tá realmente certo esse tamanho?"

        if xeena_encontro:

            "Isso tá me lembrando aquela vez que eu encontrei aquela moça no condomínio da [j]."

            "Eu nunca vou lembrar o nome dela. Mas ela tava encima de um poste."

            "Que coisa maluca foi aquela?"

        "Eu tenho certeza que não é normal isso. É como... se ela tivesse mais perto."

        "Mas isso é impossível. Dizem que se a lua estivesse um pouco mais perto da terra o nível do mar subiria."

        "E se ela tivesse mais longe também. De qualquer jeito, todo mundo só morreria."
    else:


        "A lua tá assim de novo hoje..."

    "{cps=18}{size=17}{i}grrrraaaaaauuuuuuuuuullll{/i}{/size}{/cps}"

    if quincy_e2_comecou:

        mc angustiado "De novo esse barulho?!"
    else:


        mc desconfiado "Hm?"

        "{cps=12}{size=17}{i}grrrraaaaaauuuuuuuuuullll{/i}{/size}{/cps}"

        mc preocupado "Que porra de barulho é esse?"

    "Parece que tá vindo dali da frente."

    $ quincy_e2_comecou = True

    menu:
        "Eu tenho que ver o que é isso":


            $ quincy_e2 = True

            "Não dá pra ignorar uma coisa dessas."

            mc zerado "Interessante que é exatamente o que o povo pensa antes de morrer nos filmes de terror."

            "Mas eu não sou cagão. {size=15}Eu acho.{/size} Tenho que ver o que é isso."

            "{cps=12}{size=17}{i}grrrraaaaaauuuuuuuuuullll{/i}{/size}{/cps}"

            "Calma! Calma! Já tô indo!"
        "Melhor eu cair fora daqui":


            "E eu lá quero me meter com isso e acabar morto?"

            "Deixa eu sair daqui e voltar pra ilha."

            scene black with Dissolve(1.0)

            $ tempo = 4

            jump call_cidade

    scene black with dissolve

    "..."

    $ fundo_especial = True

    scene ilha praia_gazebo_perto with Dissolve(1.0)

    pause

    "E agora?"

    "{cps=12}{i}grrrraaaaaauuuuuuuuuullll{/i}{/cps}"

    mc angustiado "!!"

    scene ilha quincy_gazebo with vpunch

    "???" "{cps=18}{i}grrrraaaaaauuuuuuuuuullll{/i}{/cps}"

    "Que merda é essa ali em cima?!"

    "???" "Huhuhuhu... meu ritual lhe atraiu?"

    mc desconfiado "Hm?"

    "Parece que eu já ouvi essa voz antes."

    mc preocupado "Quem é você?!"

    "???" "Eu sou a deusa Diana! Feche seus olhos, me adore e talvez eu te leve até a lua!"

    mc desconfiado "Me levar pra lua?"

    "Eu tenho certeza que já ouvi essa voz antes..."

    menu:
        "Vou fechar os olhos e ver o que acontece":


            $ quincy_amizade += 2

            show black with dissolve

            mc concentrando "Pronto. Estão fechados."

            "???" "Agora repita. 'Deusa Diana, carregadora da luz, leve-me até a lua'!"

            "Que doideira... por que eu aceitei isso?"

            "???" "Vamos! Repita!"

            mc "Deusa Diana, carregadora da luz, leve-me até a lua!"

            "???" "Muito bem!"

            hide black with dissolve

            "???" "Leve-me até a lua! Deixe-me brincar entre as estrelas. Deixe-me ver como é a primavera na imensidão do nada!"

            "???" "Segure minha mão, querida, beije-me!"

            "O jeito que ela fala... com esse ritmo... Será que isso realmente é um ritual?"
        "É você, não é, [q]?!":


            mc charmoso "Eu lembro da sua voz! É você, não é, [q]?!"

            q "Não sei quem é essa [q]! Eu sou a deusa Diana!"

            mc zerado "..."

            mc charmoso "Caraca. Quem diria, que só daquele dia que conversamos, eu iria gravar sua voz?"

            mc "Você é realmente marcante."

            q "Não vou cair nessa sua fala mansa, humano!"

            mc envergonhado "Eu me sinto mais louco falando com você gritando. Por que você não desce aqui?!"

    scene black with dissolve

    mc surpreso "Uou!"

    scene ilha praia_gazebo_perto with dissolve

    show quincy_b mascara with dissolve

    q "Sinta-se agraciado pela minha presença."

    mc zerado "Eu sabia que eu te conhecia. Pode parar com isso, [q]."

    q "Eu tenho várias identidades. Onde você vê uma, existem muitas, como as diferentes fases da mesma lua."

    q "Eu sou Diana, uma das fases."

    mc envergonhado "..."

    menu:
        "Por que você não tira essa máscara?":


            mc "E se você tirasse essa máscara pra gente poder conversar melhor?"

            q "Essa máscara está presa por magia negra."

            mc "E não dá pra tirar?"

            q "É preciso um sacrifício para liberar minha face desta máscara. Você se voluntaria?"

            mc zerado "De jeito nenhum."

            q "Hmmm... o sacrifício pode ser feito depois também."

            mc envergonhado "Isso seria uma boa."
        "Entendi. Então agora você é uma deusa?":


            $ quincy_amizade += 1

            mc envergonhado "Acho que entendi. Então agora você é a tal da deusa Diana?"

            q "Exatamente. Meu ritual estava quase completo, mas você estragou tudo."

            mc "Desculpa. Eu escutei um barulho e quis ver o que era."

            q "Que bom que você reconhece seu erro. Mas vocês humanos são assim mesmo, falhos."

            mc zerado "..."

    q "Eu não preciso mais disto."

    show quincy_b feliz with dissolve

    mc normal "Bem melhor."

    q "Olá, [mc]. Agora eu sou apenas... [q]."

    menu:
        "Você é muito mais bonita como [q].":


            mc charmoso "Você é mais bonita assim, sendo 'apenas' [q]."

            show quincy_b discorda with dissolve

            q "Obrigada. Mas como [q] eu não tenho nenhum poder."

            mc envergonhado "E pra que você precisa de poderes?"

            q "Como pra quê? Pra realizar minha missão."

            mc desconfiado "Que seria?"

            q "Não interessa..."

            mc zerado "Mal educada..."

            show quincy_b feliz with dissolve
        "Eu prefiro você como a deusa Diana.":


            $ quincy_amizade += 1

            mc desculpa "Que pena. Eu preferia você como a poderosa deusa Diana."

            q "Eu sei. Quem não preferiria? Mas não posso abusar dos poderes dela."

            "Será que ela realmente acha que eu tô falando sério?"

            mc envergonhado "Ah entendi..."

    q "Mas foi bom ver você aqui, [mc]."

    mc normal "A é? Por que?"

    q "Quanto mais pessoas reunidas em nome dos deuses, mais poder passamos para eles."

    q "O poder dos deuses vem de seus adoradores. Sem adoração, eles desaparecem. E agora Diana tem sua adoração também."

    mc zerado "Sei não..."

    mc "Mas mudando de assunto, o que você tá fazendo com essa roupa?"

    window hide

    pause

    q "Como assim? Estamos na praia, não estamos?"

    mc desconfiado "E o que isso tem a ver?"

    q "Estou usando um biquini como qualquer outra garota."

    mc zerado "Esse é seu biquini? Com essas cordas e essa imagem... sei lá o que é isso."

    q "É tipo um maiô. Uma roupa de banho de uma peça só."

    mc envergonhado "Tem uma grande diferença entre um maiô e isso aí. Quer saber? Por que eu tô me preocupando com isso?"

    q "Pergunto o mesmo. Existem coisas muito mais urgentes."

    mc concentrando "Agora você falou uma verdade."

    show quincy_b discorda with dissolve

    q "[mc]... você sabe que existem coisas estranhas nesta ilha, não sabe?"

    mc desconfiado "Hm?"

    q "Esta ilha, cheia de garotas lindas e usando pouca roupa. Você sabe que existe um sentido nisso tudo, não sabe?"

    menu:
        "O sentido é se dar bem.":


            mc tarado "O sentido é aproveitar e se dar bem. Por isso não posso ser despedido."

            q "Não seja tonto, [mc]."

            mc zerado "Ei."

            q "Mas não adianta falar sobre isso agora. Você ainda não tá pronto."

            mc "..."
        "Como assim um sentido nisso?":


            $ quincy_amizade += 1

            mc desconfiado "O que você quer dizer com isso?"

            q "Existem pessoas, milhares de pessoas, que se aproveitam desse cenário em que você está."

            q "Elas se divertem às suas custas e você nem faz ideia."

            mc envergonhado "Mas não é pra isso mesmo que existem os paparazzi? Eu sei que não é o mais sério dos empregos, mas meu objetivo é manter elas entretidas."

            q "Eu acho que você tá levando essa sua profissão a sério demais."

            mc zerado "Mas eu nem-"

            mc concentrando "Você me deixa cansado..."

    show quincy_b feliz with dissolve

    q "Mas agora preciso ir."

    mc desconfiado "Onde você vai?"

    q "Vou enfrentar a escuridão onde nada existe e as luzes parecem perto, mas navegam por milhares de anos até chegar em mim."

    mc zerado "..."

    q "Boa noite, [mc]."

    hide quincy_b with dissolve

    mc normal "Boa noite, [q]."

    show quincy_b mascara with dissolve

    q "Quem é [q]? Eu sou Diana, a deusa da lua."

    mc zerado "De novo, não. Tchau."

    scene praia_gazebo_especial with Dissolve(1.0)

    "Essa doida é doida de verdade."

    mc normal "Mas não posso negar que ela me diverte até."

    mc "Por que gente tonta é tão divertida?"

    return

label quincy_evento4:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("quincy_evento3","a","a")

    $ quincy_e3 = True

    "Não sei exatamente por que eu sinto isso, mas tem alguma coisa legal em voltar aqui onde eu estudei..."

    mc desconfiado "A entrada parece meio vazia..."

    mc "Onde foi todo mundo?"

    "???" "AAAAHHHHHHHHHHHH!"

    mc surpreso "!"

    mc "Tem uma pessoa a-"

    scene quincy_escorregando with hpunch

    q "AAAAAYYYYYEEEEEE!!!!"

    mc surpreso "[q]!"

    q "[mc]?!"

    q "Socorrroooo!"

    mc surpreso "CALMA! EU TE AJ-"

    scene quincy_sentada_mc with vpunch

    pause

    q "Ufa... essa foi por pouco."

    mc "Ai..."

    q "Meu herói."

    mc "P-posso saber o que tá rolando?"

    q "Nada, ué."

    mc "Nada?"

    menu:
        "Por que você tava escorregando pelo corrimão?":


            $ renpy.block_rollback()

            mc "Como você foi parar em cima do corrimão?"

            q "É que eu queria chegar mais perto da lua, e daí queria escalar o corrimão pra ver ela pela janela, mas escorreguei..."

            mc "Sério mesmo?"

            q "Sim, ué."

            mc "E por que você foi fazer isso?"

            q "Pra chegar mais perto da l-"

            mc "Eu sei! Você já respondeu! Mas por que a lua? Por que você queria chegar mais perto?"

            q "Pra poder ver ela melhor."

            mc "..."

            q "Você faz cada pergunta, [mc]. Tem gente que vai falar que você é doido."

            mc "Eu, né?"
        "Cadê todo mundo?":


            $ renpy.block_rollback()

            mc "Você sabe onde tá todo mundo?"

            q "Como assim? Você viu que horas são, [mc]? Já passou da meia-noite."

            mc "Sério?! Caraca... nem percebi..."

            mc "Então por que a universidade tá aberta essa hora?"

            q "Eu abri."

            mc "Você?! Como?!"

            q "Eu queria ver a lua mais de perto, então eu pensei em entrar nesse prédio que é o lugar mais alto por aqui."

            mc "Isso não explica nada..."

            q "[mc]... quando você quer muito uma coisa, você consegue."

            mc "Tipo, você quis tanto entrar aqui que a porta só abriu?"

            q "Não exatamente..."

            mc "Por que eu ainda tento entender você?"

            q "Hehe..."
        "Você estuda aqui?":


            $ renpy.block_rollback()

            mc "Vou tentar me esforçar ao máximo pra fazer uma pergunta normal. Você estuda aqui?"

            q "Não."

            mc "Alguma coisa dentro de mim sabia que você ia respoder isso..."

            q "Você acha que eu não tenho cara de quem faz faculdade?"

            mc "Olha... pelo seu rosto, você tem idade, mas, sei lá, seu jeito..."

            q "Você consegue olhar pra dentro do meu corpo, [mc]?"

            mc "Como assim?!"

            q "Consegue ver meu espírito?"

            mc "Ah? Hmm... Acho que não..."

            q "Quem sabe..."

    "Eita... agora que eu vi que ela tá sentada bem no meu..."

    mc "É... Agora que você tá bem... posso levantar?"

    q "Claro."

    scene uni_hall geral with Dissolve(1.0)

    q "Upa."

    show quincy provocando with dissolve

    q "Sorte que você tava passando aqui bem agora."

    mc envergonhado "Verdade..."

    q "Você também tava querendo ver a lua mais de perto?"

    mc "Haha... não. Só tava andando pela cidade mesmo."

    q "Talvez a lua tenha trazido você até aqui."

    mc "Quem sabe..."

    show quincy seria with dissolve

    q "[mc]... a lua atua na gente de formas muito marcantes. Você entende isso?"

    mc "Então você acredita nessas coisas?"

    q "Como assim essas coisas? Isso é ensinamento muito antigo. Muito mais velho do que eu e você."

    mc normal "Haha... claro, né? Mas e a ciência?"

    q "Você acredita cegamente na ciência?"

    mc desconfiado "Cegamente... na ciência?"

    q "Só porque algumas pessoas fizeram uns testes com muitas pessoas e seguiram um formato específico, isso é a verdade?"

    q "Você acha que isso anula tudo o que as pessoas diziam milhares de anos atrás?"

    mc envergonhado "Eu sinto que você tá falando de forma contrária..."

    show quincy costas with dissolve

    q "Sabe, [mc]... Teve uma época em que ciência e a fé não eram coisas tão diferentes igual hoje."

    mc desconfiado "Como assim?"

    q "Muitos anos antes da gente nascer, antes mesmo de Jesus nascer, milhares de anos antes dele..."

    q "Teve um povo na Terra que criou quase tudo o que a gente conhece hoje."

    q "Eles foram os primeiros a criar uma cidade... eles foram os primeiros a escrever com palavras."

    mc normal "Uou... eu não tô ligado muito dessas coisas de história..."

    q "Esse povo juntava ciência e magia. Eles sabiam como usar a matéria do mundo, mas eles também olhavam para os céus."

    q "Eles viam as estrelas e a lua e sabiam que existiam coisas que a gente não podia ver."

    q "Coisas que o próprio mundo não podia explicar."

    mc desconfiado "O próprio mundo não podia explicar? O que você quer dizer?"

    q "O mundo, a matéria... eram coisas que não estavam no que a gente pode ver e pegar, mesmo com microscópios..."

    mc "..."

    show quincy invocada with dissolve

    q "Então não ache que só porque uma coisa não tá escrita em um livro, ela não existe."

    q "Não ache que o mundo é só o que você consegue entender. Existem coisas que a gente não entende, mas estão lá!"

    mc envergonhado "O-ok..."

    show quincy alegre with dissolve

    q "Pelo menos é isso que eu acho!"

    mc zerado "Você fala tudo isso pra terminar com um 'acho'?"

    q "Eu não sou uma estudiosa, [mc]. Não tô nem aí se as pessoas falam que existe ou não."

    q "Pra mim, se eu sinto, então existe. Não importa se um velho careca numa roupa branca fala que não existe."

    q "Essa sou eu."

    "Doida. Essa é doida."

    mc normal "Você tem uma boa autoestima, isso eu posso falar."

    show quincy costas with dissolve

    q "Pare de rotular as coisas, [mc]. Essa sou eu e pronto."

    mc envergonhado "Ok... desculpa."

    q "Agora eu vou subir no telhado e ver a lua. Quer ir junto?"

    menu:
        "Não. Tô indo nessa.":


            mc envergonhado "Valeu, mas tenho que ir nessa."

    show quincy provocando with dissolve

    q "Que pena... mas foi legal ver você."

    q "Que Nanna olhe seus passos e te banhe de luz."

    mc zerado "Quê?"

    q "Tchau, [mc]."

    hide quincy with dissolve

    mc "..."

    "O que aconteceu aqui?"

    scene black with dissolve

    "Deixa eu voltar pra casa..."

    jump call_cidade

label quincy_evento5:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("quincy_evento4","a","a")

    $ quincy_e4 = True

    "Hmm... o céu parece diferente hoje."

    "Eu tô sentindo um arrepio aqui atrás. Eu não gosto muito dessa sensação. Eu já senti ela outra vez... e era de noite..."

    if xeena_encontro:

        "Nossa. Agora eu lembrei daquela mina que tava em cima de um poste quando eu tava no condomínio da [j]."

    "Só falta a lua tá gigante igual..."

    scene selena_f1 with Dissolve(1.0)

    pause

    mc zerado "Óbvio que ela ia tá lá..."

    mc desconfiado "Essa lua... eu nunca vi ninguém na redação falando sobre ela."

    mc "Nem notícia nenhuma sobre essa lua. Não é possível que isso seja normal. Olha o tamanho dessa giribonga."

    mc "Hm? {w}Pera... {w}O que é aquela coisa lá em cima?"

    mc "..."

    mc surpreso "!!!"

    mc "T-tem alguém lá em cima!"

    mc angustiado "Ei! Socorro! Tem alguém lá em cima! Acho que ela vai pular!"

    menu:
        "Subir até lá ajudar":


            $ renpy.block_rollback()

            mc serio "Não dá tempo de procurar ajuda. Eu tenho que subir lá."

            mc desconfiado "Mas... como que eu vou chegar até lá em cima? Não dá pra eu só entrar nesse prédio aí{nw}"

            scene black with Dissolve(0.2)

            scene quincy_terror1 with Dissolve(0.2)

            scene predio_cima with Dissolve(0.2)

            pause

            mc angustiado "Hm?!"

            mc "O que eu tô fazendo aqui?!"

            "Eu decidi que ia subir... E de repente eu tava aqui em cima. Que porra foi essa?"

            "Nem sabia como eu ia subir... Como eu vim parar aqui?"
        "Correr procurar por ajuda":


            $ renpy.block_rollback()

            "Melhor eu procurar ajuda. Eu não tenho o que fazer lá."

            scene cidade centro1 with Dissolve(1.0)

            mc angustiado "Socorro! Alguém!"

            scene cidade centro1 with hpunch

            mc angustiado "Preciso de ajuda!"

            scene black with Dissolve(0.2)

            scene quincy_terror1 with Dissolve(0.2)

            scene predio_cima with Dissolve(0.2)

            pause

            mc angustiado "Hm?!"

            mc "O que eu tô fazendo aqui?!"

            "Eu fui procurar ajuda... né? E de repente eu tava aqui em cima. Que porra foi essa?"

            "Eu cheguei a chamar alguém? E como eu vim parar aqui?"

    "Merda. Que porra foi essa?"

    "Foda-se. Cadê aquela pessoa que ía pular?! Será que não deu tempo?!"

    "???" "Oh! Lua maravilhosa! Lua cheia de energia! Controladora das marés do mundo exterior e interior!"

    mc desconfiado "Hm?"

    "Tá vindo dalí..."

    scene black with dissolve

    "..."

    scene selena_f2 with Dissolve(1.0)

    pause

    "???" "Você! Prisão impenetrável! Motivo da minha angústia e esperança! Se aproxime de mim! Venha até minhas mãos!"

    mc surpreso "Essa garota!"

    if xeena_encontro:

        "Esse cabelo... essa roupa azul colorida..."

        "É aquela garota que eu encontrei em cima do poste! Lá na casa da [j]!"

        "Como era o nome dela mesmo?"

        "Acho que eu nunca vou lembrar... Mas esse cabelo é irreconhecível."

    "???" "[mc]... nem acredito que é você..."

    mc desconfiado "Essa voz... acho que eu sei quem é você."

    q "Sou eu. A [q], seu bobo. Já se esqueceu de mim?"

    mc "[q]? Mas... o que você tá fazendo com esse cabelo e essa roupa?"

    q "Que cabelo? Que roupa?"

    mc zerado "Enlouqueceu de vez? Eu sabia que você ainda ia surtar..."

    q "Você vê como a lua tá perto das minhas mãos?"

    mc envergonhado "Nem me fala... tá bem perto mesmo..."

    q "Você consegue sentir também, não consegue?"

    mc desconfiado "Hm?"

    q "Você não sente a energia da lua? É ela te chamando, [mc]."

    if xeena_encontro:

        "Então é a [q]... não é aquela garota..."

        "Pensando agora... a [q] também sempre apareceu em cima das coisas e a lua também sempre tá assim. Igual aquela estranha do poste..."

        "Será que as duas..."

        q "[mc]?"

        mc surpreso "Ah! Desculpa..."

    mc envergonhado "Acho que eu não sinto nada, [q]... só acho estranho ninguém falar nada de uma lua desse tamanho."

    q "Quem dera todo mundo tivesse os olhos abertos como você, [mc]. Quem dera..."

    q "Agora vamos chamar ela! Vamos chamar a lua pra gente!"

    scene selena_f3 with Dissolve(1.0)

    pause

    q "Lua! Você que nos observa aí de cima! Venha até nós! Para que possamos sentir seu poder e sua influência!"

    mc "P-por que você tá gritando assim, [q]?!"

    q "Ela precisa me ouvir! Ela precisa saber que eu estou aqui pensando nela! E toda vez que ela vem até mim, eu a tocarei!"

    mc "Você vai cair, isso sim!"

    q "Eu não posso morrer, [mc]! Não enquanto você tiver do meu lado!"

    menu:
        "Eu posso tentar te proteger...":


            $ renpy.block_rollback()

            mc "Eu p-posso fazer o possível, mas... se você cair, o que eu faço?!"
        "Tá achando que eu sou o homem-aranha?!":


            $ renpy.block_rollback()

            mc "C-como que eu vou te salvar se você cair do prédio?! Não sou o homem-aranha, não!"

    q "Pare de ser bobo! Ela nunca me traíria, [mc]! Você se preocupa dem-"

    scene selena_f3 with hpunch

    pause

    q "Ops! Quase escorreguei!"

    mc "[q]! Me escuta por favor! Sai logo daí!"

    q "Ela nunca esteve tão perto da gente, [mc]. Essa é a nossa chance de chegar até ela."

    q "Eu vou voar até lá! E você pode ir comigo!"

    q "Eu vou pular!"

    q "E chegar!"

    q "Até lá!"

    mc "[q]!!!"

    scene black with vpunch

    pause

    scene selena_f4 with vpunch

    pause

    q "Meu herói..."

    mc "Nada de seu herói... isso foi perigoso, [q]. Se você tivesse escorregado pra lá, você ia cair pra fora..."

    q "Teehee... você é meu salvador, [mc]. Igual daquela outra vez, né?"

    mc "Então você lembra?"

    q "Como eu ia esquecer? Aquilo foi tão marcante pra você."

    mc "E-ei... não coloque palavras na minha boca."

    q "Eu lembro como você ficou quando eu caí sentada bem no seu..."

    mc "Tá bom! Entendi!"

    q "Eu acho que a gente faz uma boa dupla, sabe? A gente se completa de alguma forma."

    mc "Em que sentido?"

    q "Você é mais pé no chão e eu sou completamente no mundo da lua."

    q "Não tem um ditado que vocês falam... tipo... opostos se atraem?"

    mc "Tem..."

    q "O que você acha?"

    mc "Eu?"

    q "Quem mais? Tem mais alguém me segurando no colo aqui?"

    "Será que a [q] tá se declarando pra mim? Só que... desse jeito estranho dela?"

    "Eu preciso pensar muito bem no que eu vou responder pra ela."

    call namorando from _call_namorando_4

    if namorando:

        "Eu já tô numa relação séria... será que eu devia me comprometer com mais alguém assim?"
    else:


        "Eu não tô namorando com ninguém agora... eu tô livre pra ficar com ela se eu quiser..."

    "E agora? O que eu respondo? Essa é uma escolha sem volta..."

    menu:
        "Eu acho que a gente forma uma boa dupla.":


            $ renpy.block_rollback()

            mc "Eu concordo."

            scene selena_f5 with Dissolve(1.0)

            pause

            mc "Eu acho que a gente forma uma bela dupla mesmo. Em vários sentidos."

            q "Será que eu tô entendendo certo?"

            mc "Acho que você tá, sim."

            mc "Eu te acho muito linda, [q]. E esse seu jeito sapeca me deixa louco. Você é a doidinha que eu precisava."

            q "Hmmm..."

            mc "O que você me diz?"

            q "Será que você consegue me acompanhar, [mc]?"

            mc "Olha, dependendo da viagem eu consigo. Só não pode exagerar."

            q "Eu não gosto de meio termo. Minha cabeça tá lá em cima e não é fácil vir atrás de mim. Você quer mesmo assim?"

            mc "Vale a pena por você."

            q "Que homem... então eu aceito. A gente pode ficar juntos a partir de hoje."

            mc "Posso te beijar então?"

            q "Pode."

            mc "Então, com licença."

            q "Calma!"
        "A gente é diferente demais pra ser uma dupla.":


            $ renpy.block_rollback()

            scene selena_f5 with Dissolve(1.0)

            pause

            mc "Não tem como a gente ser uma dupla, [q]. A gente é tipo água e óleo, não se mistura de jeito nenhum."

            q "Awwwwnnn... tem certeza? Eu acho que você se surpreenderia em como a gente tá ligado."

            mc "Você é cuca fresca demais pra mim. Eu sou mais racional. Ia ficar de cabelo branco em uma semana do seu lado."

            q "Aí você disse uma verdade. Eu sou meio louquinha mesmo, [mc]."

            q "Talvez você não queira ver o que eu tenho então."

            mc "Hm? Calma lá. Do que você tá falando?"

            q "Eu vou te mostrar."

    scene black with hpunch

    pause

    mc "E-ei! Q-que foi isso?"

    scene selena_f6 with Dissolve(1.0)

    pause

    q "Eu vou pegar uma coisinha aqui antes."

    mc desconfiado "O que tem aí atrás?"

    q "Você vai ver... eu não subi até aqui à toa, né, [mc]?"

    mc zerado "Não subiu? Toda vez que eu te vi você tava em cima de alguma coisa sem muita razão..."

    q "Impossível que você ache que eu ia perder meu tempo trepando nas coisas sem motivo."

    q "Logo logo você vai entender tudo, [mc]."

    q "Sabe, [mc]... Não sei se você lembra, mas da outra vez eu falei que tem coisa nesse mundo que a gente não entende."

    q "Pera aí. Só um segundo."

    scene black with dissolve

    "{i}tchak tchak{/i}"

    mc surpreso "!!!"

    scene selena_f7 with Dissolve(1.0)

    pause

    q "Então. Tem gente que chama de Deus, tem gente que fala que é o diabo, que é sorte, destino, outros acreditam em espíritos, almas..."

    q "Seja lá o nome que você dá pro que as pessoas não conseguem explicar com a razão, elas estão lá."

    mc preocupado "[q]... sem querer cortar teu barato, mas que porra de roupa é essa?!"

    q "Calma. Ainda não acabou."

    q "Agora presta atenção. Porque é muito importante."

    mc envergonhado "Tá, mas não sei se eu tô entendo onde você que chegar."

    q "Só escuta."

    mc "Ok..."

    q "Nossa vida tá cheia de coisas que a gente não consegue entender. E às vezes a gente precisa só acreditar."

    q "Não tem explicação. É só aceitar que aquilo aconteceu e abraçar a vida como ela é. Com todos seus mistérios."

    q "A maioria das pessoas tenta ignorar o que não entende. Por isso vive na bolha só do que gosta e conhece."

    q "Mas você é diferente, não é? Você aceita o que a vida te traz e vai atrás das oportunidades."

    mc envergonhado "Sei lá..."

    q "E essa oportunidade vai aparecer pra você essa noite, [mc]."

    q "Se você quiser vir comigo, essa é sua chance."

    mc desconfiado "O que você quer dizer? O que eu tenho que fazer?"

    q "É fácil."

    scene black with dissolve

    "{i}tchak tchak{/i}"

    scene selena_f8 with Dissolve(1.0)

    pause

    q "Você só precisa vir comigo."

    mc surpreso "Q-que que é isso, [q]?!"

    q "Como você acha que a gente vai chegar na lua?"

    mc zerado "Repete..."

    q "Lembra o que eu disse. Você só precisa acreditar em mim e vir comigo."

    mc preocupado "[q]... você tá querendo me dizer que... você vai voar com isso?"

    q "Não só eu. Você também, [mc]."

    mc "N-não sei, não, [q]... tá tudo muito estranho."

    q "Eu vou te mostrar. É só ter coragem e vir comigo!"

    mc angustiado "[q]! Não!"

    scene selena_f9 with Dissolve(1.0)

    pause

    q "Viu?"

    mc angustiado "V-você é louca?! Volta logo pra cá!"

    q "Eu sou louca, [mc]! Mas quem não é?!"

    q "Você não tá vendo como é possível?! Tem coisas que a razão não explica! Você só tem que acreditar!"

    "Que porra tá acontecendo aqui? Como que ela tá voando desse jeito?"

    q "Vem. Pula e eu te pego. A gente pode ficar juntos depois disso."

    mc preocupado "P-pular?!"

    q "Pode confiar em mim. Eu tô aqui pra te segurar!"

    mc preocupado "[q]... não sei..."

    show selena_f10 with Dissolve(1.0)

    pause

    mc "Parece bem alto..."

    q "Mas eu tô aqui. Você me salvou de cair antes. Eu vou fazer o mesmo por você."

    q "Você só precisa acreditar, [mc]!"

    "Como que isso pode tá acontecendo?"

    "Mas a [q]... como que ela tá voando desse jeito? Essa roupa dela... de onde veio isso?"

    "E onde será que ela vai me levar?"

    hide selena_f10 with Dissolve(1.0)

    mc preocupado "Isso é demais pra mim, [q]..."

    q "Eu pensei que você fosse diferente dos outros. Que você ia ter coragem pra aceitar o que a vida te mostra."

    q "O medo é a única coisa que nos separa! Se entregue ao seu impulso e venha! Pensar é a desgraça da humanidade!"

    mc angustiado "Eu não sei!"

    q "Essa é sua chance. Se você não vier agora, nós nunca mais vamos nos ver."

    q "Você topa ou posso ir sozinha?"

    "A [q] realmenet tá voando... e ela poderia me salvar... será que eu devo só fechar os olhos e acreditar nela?"

    "Que tipo de coisa uma pessoa igual ela pode me mostrar? Coisas que ninguém acreditaria..."

    "Mas isso não é loucura demais?!"

    "Coragem... burrice... o que eu faço?!"

    "Esse é o tipo de coisa que não dá pra se arrepender. O que eu escolher aqui vai ser pra sempre!"

    "É agora! O que eu escolho?!"

    menu:
        "Eu aceito. Eu vou com você.":


            $ renpy.block_rollback()

            $ renpy.save("None-continue", extra_info="None-continue")

            mc charmoso "Ok. Eu não vou deixar o medo tirar o melhor de mim. Eu vou fazer o que eu quero."

            q "Isso!"

            mc "Eu confio em você, [q]. E eu quero tá com você agora. Seja lá pra onde a gente vai."

            q "Então vem!"

            mc "Tá. Ufa... que nervoso..."

            scene black with dissolve

            mc concentrando "{i}puuuff{/i}"

            mc "Você tá aí?"

            q "Claro! Agora vem!"

            mc "Iáááá!"

            scene black with vpunch

            mc "[q]!"

            q "Agora vai ser rápido, [mc]."

            scene selena_f11 with vpunch

            pause

            mc "[q]!"

            mc "Cadê você?!"

            mc "[q]!!!"

            mc "Aaaaahhhh!!!"

            scene red with vpunch

            pause

            mc "..."

            scene black with Dissolve(5.0)

            pause

            p lecionando "É. Parece que foi demais para ele."

            p "Eu pensei que o [mc] iria aguentar o tranco, mas foi demais para ele..."

            p "Parece que eu vou ter que encontrar outro... um que dessa vez aguente a pressão."

            p rindo "Não é fácil ter toda essa energia incrível dentro da cabeça, sabe? Não precisa dar risada dele."

            p lecionando "Aliás, se todos eles aguentassem, eu já teria terminado há muitos anos. Uma pena que eles sejam tão frágeis."

            p rindo "Isso vale para você também. Não fique com essa cara. Não se esqueça do que você me prometeu no começo."

            p "Agora acho bom você fazer alguma coisa."

            $ persistent.selena_morreu = True

            $ renpy.block_rollback()

            "..."

            $ renpy.full_restart()
        "De jeito nenhum eu pulo aí.":


            $ renpy.block_rollback()

            $ renpy.save("None-continue", extra_info="None-continue")

            "Não tem como. Eu não vou fazer isso."

            if persistent.selena_morreu:

                show black with dissolve

                "???" "Teehee... aprendeu a lição, né?"

                hide black with dissolve

            mc desculpa "Malz, [q]... mas não dá. Esse é o tipo de viagem que é demais pra mim."

            mc "Eu entendo que às vezes o mundo pode ser meio estranho, mas não é tudo que é aceitável também."

            mc envergonhado "Se você consegue viajar com essa roupa louca aí, boa sorte. Eu prefiro o chão mesmo."

            q "É uma pena, [mc]..."

            q "Você vai perder coisas incríveis. Mas assim talvez acabe sendo melhor, sabe?"

            mc desconfiado "Hm?"

            q "Às vezes o medo é uma forma de coragem. Coragem de não desistir de tudo e continuar, entende?"

            mc "Meio contraditório o que você tá falando."

            q "Às vezes a gente tá de saco cheio e só quer acabar. Parece que é coragem ser porra louca."

            q "Mas a coragem está, de verdade, em continuar, mesmo quando as coisas parecem terríveis."

            q "Manter os pés no chão e se apegar à vida, essa é sua coragem. E é diferente da minha, mas é bonita também."

            q "As coisas vão ficar cada vez mais difíceis quanto mais você caminhar em direção ao fim."

            q "Mas eu confio que você vai chegar lá. Mantenha os pés no chão e boa vida."

            scene black with dissolve

            "{i}vuooooosh{/i}"

            scene predio_cima with Dissolve(1.0)

            mc zerado "Lá vai ela voando... que doideira..."

            "Não acredito nessa noite... essa sem dúvida foi a experiência mais louca que eu já tive."

            "???" "Senhor! O senhor está bem?!"

            mc desconfiado "Eu?"

            scene selena_f12 with Dissolve(1.0)

            "Policial" "Sim. O senhor foi visto na beirada desse edifício. Graças a Deus o senhor não tomou nenhuma medida impensada."

            mc "Eu? E a mulher voando? Ninguém se preocupou com isso?"

            "Policial" "Mulher voando? O senhor pode me entregar sua identidade por favor?"

            mc "Sim... mas eu tô falando sério."

            "Policial" "O senhor usou ou tomou qualquer tipo de bebida ou substância esta noite, senhor?"

            mc "Eu tô bem. É sério. Não é possível que ninguém viu a mulher que tava aqui."

            "Policial" "Nenhuma mulher foi vista, senhor. Apenas você estava na beirada."

            "Policial" "Por sorte uma senhora ouviu a porta sendo arrombada e me chamou. Acredito que o senhor foi o responsável."

            "Policial" "Eu vou precisar fazer alguns testes com o senhor."

            mc "Tudo bem... Putz! Caralho! Eu vou ter que pagar pela porta?!"

            "Policial" "Haha... se essa é sua preocupação, então talvez o senhor esteja melhor do que eu imaginava."

            mc "Eu devo tá muito estressado ultimamente, seu guarda."

            "Policial" "Todos nós temos que liberar um pouco de pressão às vezes."

            "Policial" "Olha, se você vier comigo, eu prometo que não faço um Boletim de Ocorrência e o senhor não precisará pagar."

            mc "Fico te devendo essa, cara. Valeu mesmo."

            "Policial" "Ok. Mas então vamos descer."

            mc "Agora."

            scene black with dissolve

            "Eu ainda não tô acreditando nessa merda..."

            "[q]... será que eu ainda vou ver você um dia?"

            pause

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
