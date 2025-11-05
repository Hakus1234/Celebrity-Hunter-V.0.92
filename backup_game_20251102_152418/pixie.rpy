label pixie_evento3:

    $ pixie_e3 = True

    "..."

    mc normal "Voltei, [p]."

    "..."

    mc desconfiado "Hm? De novo ela não tá aqui?"

    "Melhor eu procurar."

    scene fadolandia geral_bot with Dissolve(1.0)

    "Não tá aqui na base na árvore também. Que estranho..."

    "Vou ver lá em cima."

    scene fadolandia casa with Dissolve(1.0)

    mc desconfiado "[p]! Tá aí!?"

    "..."

    "O jeito é entrar... se bem que daquela vez ela não curtiu muito que eu tava andando pelas coisas dela sem avisar."

    "Mas é culpa dela também. O que eu faço?"

    menu:
        "Entrar na casa.":


            $ renpy.block_rollback()

            "Se pá ela tá dormindo ainda... talvez..."

            "Quem sabe ela dorme sem roupa? Ela vive sozinha aqui mesmo..."

            "P-pera! O que eu tô pensando?!"

            scene fadolandia interior with Dissolve(1.0)

            pause

            mc preocupado "[p]?"

            "..."

            mc concentrando "Nada aqui também... ela deve tá em outro lugar."

            scene fadolandia casa with Dissolve(1.0)
        "Descer e procurar em outro lugar.":


            $ renpy.block_rollback()

            "Então eu vou descer."

    "Vou procurar ela lá perto daquela ponte. É o último lugar que falta."

    scene pi3_fado1 with hpunch

    pause

    p "Oi, [mc]. Visitando?"

    mc surpreso "P-pixie?!"

    p "Eu adooooro quando você fica com saudades de mim, sabia?"

    mc envergonhado "Onde você tava?"

    p "Por aí."

    mc "Só por aí?"

    if f1_biquini:

        p "Desde que você me viu com minha nova roupa, eu estou bem mais animada."

        if f1_poder:

            p "Ainda mais depois de ver você ficando excitado com ela."

            p "Tudo aquilo que você me disse me deu nova vida."

            mc safado "Que bom..."

    p "Estou pensando em levar você para um lugar."

    mc desconfiado "Onde?"

    p "Você está cada vez mais perto, [mc]. Se você continuar caçando e vindo aqui, em breve você vai estar pronto."

    mc desculpa "Não tô entendendo. Pronto pra quê?"

    p "Para conhecer o que tem além da Fadolândia."

    mc desconfiado "O que tem além daqui..."

    if fadex_1vez:

        "Eu encontrei um lugar além daqui... uma terra diferente..."

        if pixel_evento > 5:

            "Eu achei a [f]... e até teve aquele lance com a [p] quando aqui tava de noite."

        "Dá pra ver que esse sonho aqui tá cheio de coisas que eu não consigo entender ainda..."

        if pixel_evento > 5:

            "Tem até monstro aqui... duendes... sei lá o que era aquela coisinha."

        "Mas eu não fico confortável em falar isso pra [p] agora. Eu lembro que ela não gostava disso."

    mc "E o que tem aqui pra mim?"

    p "Tem tudo. Tudo o que você pode querer pra sua vida mundana. Eu quero... colocar fogo nisso tudo."

    mc envergonhado "Colocar fogo, é?"

    scene pi3_fado2 with Dissolve(1.0)

    p "O que você acha da gente fazer um passeio agora?"

    mc preocupado "P-passeio?"

    p "Sim... só nós dois..."

    if not f1_biquini:

        p "Você não viu meu traje novo ainda. Vai ser uma boa chance."
    else:


        p "Eu vou até usar aquele biquíni de fada que você adorou..."

    mc envergonhado "Haha..."

    p "Que foi? Parece que você não está muito afim... você sabe que eu não gosto de enrolação, [mc]. Ou caga ou sai da moita."

    "Um passeio com a [p]... só nós dois... s-será que é o que eu tô pensando?"

    p "Eu prometo que você não vai se arrepender..."

    mc safado "Não, né? Imagino..."

    p "Está vendo? Eu sei que você vai querer ver tudo o que eu tenho para mostrar."

    "C-calma! Eu não tô pensando direito! Preciso pensar com a cabeça certa!"

    "Eu sei que tem alguma coisa muito estranha nesse sonho. Os sinais estão em todo lugar!"

    "Se eu só aceitar e ir na onda da [p] eu vou virar um alvo fácil."

    p "Você está me cansando, [mc]. Vai embora. Quando você finalmente tiver coragem, volta aqui e fala comigo."

    mc preocupado "Eu ainda nã-"

    p "Acho melhor você acordar. Bom dia!"

    mc "E-espera!"

    return

label pixie_evento2:

    $ pixie_e2 = "iniciou"

    scene fadolandia noite_chegada with Dissolve(2.0)

    pause

    mc desconfiado "Ãh?"

    "Uou..."

    mc desconfiado "Que estranho."

    "Acho que é a primeira vez que eu vejo aqui sem sol. Fadolândia nunca tinha ficado escura dessa forma."

    "Como se tivesse ficado de noite dentro do meu sonho..."

    mc serio "[p]?!"

    mc desculpa "Estranho... ela não tá aqui? Será que tá dormindo?"

    "Isso tudo parece tão suspeito..."

    menu:
        "É melhor eu tomar cuidado.":


            mc serio "É melhor eu redobrar minha atenção até eu descobrir o que tá havendo."
        "Não tenho porque me preocupar.":


            mc normal "Tudo isso aqui é só um sonho mesmo. Não tenho porque ficar cabreiro."

    "..."

    "Não adianta eu querer explorar nada agora. Desse jeito aquela floresta que já é um breu vai ficar impossível de ver qualquer coisa."

    "Sem a luz do sol, não vai dar pra chegar na caverna também."

    "Talvez eu deva procurar a [p] e perguntar pra ela o que tá acontecendo.."

    "É o jeito... subir até a casa eu vou..."

    "..."

    scene fadolandia noite_escada with Dissolve(2.0)

    "Esse lugar nunca pareceu tão longe. E nem consigo ver o caminho pelo que tô passando."

    "De uns tempos pra cá eu tenho pensado que a [p]-"

    scene fadolandia noite_escada with hpunch



    "Opa!"

    "Quase caí no buraco aqui. Sorte que ali perto da casa tá mais claro."

    "..."

    "Ufa. Acho que..."

    p "{size=15}Hm...{/size}"

    "Epa, parece a [p]."

    menu:
        "Tentar ouvir o que ela tá falando sem ser visto":


            scene pixie fado_noite_sentada with Dissolve(2.0)

            pause

            "Ela tá sentada ali..."

            p "{size=15}Tô conseguindo levar as coisas... mas até quando vou ter que viver assim?{/size}"

            p "{size=15}Estou cansada disso. Dessa insignificância.{/size}"

            p "{size=15}Preciso de mais... preciso de ajuda...{/size}"

            p "..."

            p "{size=15}[mc]? Você tá aí?{/size}"
        "Se apresentar pra ela":


            mc normal "Oi, [p]."

    scene pixie fado_noite_sentada with Dissolve(1.0)

    p "[mc]?"

    mc surpreso "Tô-tô aqui!"

    mc envergonhado "Tudo bem com você?"

    p "..."

    p "Tudo legal..."

    "O que aconteceu com ela? Ela parece outra pessoa... se é que eu posso chamar ela de pessoa."

    mc desculpa "Você não parece legal. O que foi?"

    p "..."

    p "Eu estou um pouco para baixo. Eu me sinto um pouco triste, só isso."

    mc preocupado "Aconteceu alguma coisa que te deixou assim?"

    p "Nada. Só as coisas de sempre mesmo."

    p "Desculpa por não te receber como sempre."

    mc desculpa "Não se preocupe. Quer conversar?"

    p "Você quer fazer companhia para mim? Mesmo eu não dando em cima de você?"

    mc envergonhado "Você acha o quê? Que eu só penso nisso?"

    p "Sim..."

    mc zerado "[p]..."

    p "Eu sempre vejo você duro quando a gente tá conversando."

    mc envergonhado "Quê?! Como você poderia saber uma coisa dessas?"

    p "[mc]. Eu posso ver seu corpo."

    mc surpreso "Você pode ver pela minha roupa?!"

    p "Que roupa? Você está nu, [mc]."

    mc desconfiado "Como?"

    show mc pelado_assustado with vpunch

    pause

    mc "QUÊÊÊÊ?!"

    mc "Ma-mas! Eu sempre apareci aqui pelado?!"

    p "..."

    "Não é possível! Eu sempre estive pelado?"

    "Como eu nunca reparei nisso?"

    if notas_do_confinado2:

        "Espera... eu tô me lembrando de uma coisa."

        "O velho na ponte... onde eu li aquela mensagem estranha."

        "Ele tava pelado..."

        "Será que isso quer dizer que todo mundo que vem pra cá fica pelado?"

        "Ou será que..."

    "Impossível eu não ter reparado que eu sempre estive sem roupa aqui na Fadolândia-"

    p "O que foi?"

    "Quer saber? Foda-se. Só tem a [p] aqui mesmo."

    hide mc with dissolve

    mc envergonhado "Não é nada..."

    p "[mc]..."

    mc "Oi?"

    "Estou me sentindo tão estranho... vulnerável. Nesse escuro com a [p], pelado..."

    p "Você pode vir aqui mais perto de mim?"

    p "Pode sentar comigo nesta cadeira?"

    mc surpreso "Eu?!"

    p "Você disse que faria companhia para mim..."

    mc envergonhado "Mas, [p]. Parece que só tem um lugar nessa-"

    p "Eu sento no seu colo."

    mc "Acho que vou sentar nesta outr-"

    p "Por favor. Deixa eu sentar no seu colo."

    menu:
        "Deixar ela sentar no seu colo":


            "!"
        "Deixar ela sentar no seu colo":


            "?"

    show black with Dissolve(0.1)

    hide black with Dissolve(0.1)

    "Acho que não tem problema se eu deixar ela sentar no meu colo."

    mc envergonhado "Tudo bem."

    p "Obrigada. Vem aqui."

    "..."

    scene pixie noite_sentada_mc with Dissolve(2.0)

    pause

    mc "Não tá ruim assim?"

    p "Está muito bom, [mc]. Você tem um cheiro gostoso."

    mc "Valeu..."

    "..."

    mc "É..."

    p "Não precisa falar nada."

    mc "Ok..."

    if f1_poder:

        p "No outro dia você me ajudou muito..."

        mc "Ajudei? Como?"

        p "Eu mostrei minha nova roupa para você. Você ficou todo excitado com ela."

        mc "Ah, é verdade..."

        p "Eu... eu já não sou tão poderosa quanto era no passado."

        p "Obrigada a viver dessa forma..."

        p "Mendigando o desejo de humanos desse jeito... e pensar que tantos me amaram... Onde eu cheguei, [mc]?"

        mc "..."

        p "Eu sei que tudo isso parece estranho para você. Mas não é como se você fosse ter tempo para entender."

    "..."

    p "Fado... como é mesmo?"

    mc "Fadolândia?"

    p "Isso."

    p "Fadolândia é um lugar agradável, mas viver aqui sozinha pode ser um pouco triste, ainda mais quando você estava acostumada a viver rodeada de pessoas."

    "..."

    mc "Não sei se estou acompanhando o que você quer dizer..."

    p "Presta atenção, [mc]."

    scene fadolandia noite_geral with Dissolve(2.0)

    p "Olhe só pra este lugar. O que você vê?"

    mc "Não sei..."

    p "Estamos sozinhos aqui. Não importa o que aconteça, nunca ninguém saberia..."

    "Não sei por que, mas ela me deu um arrepio agora."

    "O que será que ela tá querendo dizer?"

    p "É tudo tão silencioso, afastado, vazio. Apenas nós dois, esperando alguma coisa acontecer."

    mc "Verdade..."

    p "Essa solidão, esse marasmo. Por que isso?"

    scene pixie noite_sentada_mc with Dissolve(1.0)



    p "..."

    mc "Você realmente tá bem estranha hoje, [p]."

    p "Eu... sei que você tem vindo aqui enquanto eu durmo."

    mc "Qu-quê!?"

    p "E eu não gosto nada disso, [mc]."

    "Ela mudou o tom de voz. Será que ela realmente tá brava?"

    p "Eu te disse para não xeretar pela minha propriedade."

    mc "E-eu..."

    p "E parece que agora você chegou no fim da linha. Não tem mais pra onde ir."

    mc "Como?"

    p "Eu vou ter que fazer algo. Espero que você não fique triste comigo."

    mc "Como assim fazer algo? Ficar triste por que? Não tô gostando des-"

    p "Você fala muito, [mc]."

    mc "Pi-pixie nã-"

    scene black with dissolve

    mc "!"

    scene pixie noite_beijo_mc with Dissolve(2.0)

    pause

    "Be-beijo?!"

    "Os lábios dela são tão pequenos, só que muito macios..."

    "E tem gosto de fruta... de coisa fresca."

    "É uma sensação que eu nunca senti antes. Eu tô me sentindo meio zonzo, meio..."

    "..."

    window hide

    pause

    scene pixie noite_prebeijo with Dissolve(2.0)

    pause

    mc "..."

    p "Gostou?"

    mc "..."

    p "Não precisa falar. Eu sei que você gostou."

    mc "É..."

    mc "[p]... desculpa se estou invadindo seu espaço falando isso... mas é a primeira vez que eu te vejo assim... tão..."

    p "Vulnerável?"

    mc "É... não sei... parece que não tem tudo sob controle, como sempre."

    p "Acho que até uma su... digo, uma fada pode se sentir nostálgica de vez em quando."

    mc "..."

    p "Mas eu tô me sentindo melhor agora."

    p "Obrigada, [mc]."

    mc "Eu não fiz nada..."

    p "Você fez mais do que imagina."

    mc "Estranho. Eu tô me sentindo diferente. Sei lá..."

    p "Eu dividi meu poder com você."

    mc "O que você quer dizer? Você me deu seu poder?"

    p "Exatamente. Eu te passei um pouco do meu poder com um beijo."

    p "Agora você vai poder {b}cruzar a barreira{/b} no interior da gruta."

    mc "Quê?! Como você sabe?!"

    p "Não seja bobo, [mc]. Você realmente pensou que estava fazendo isso escondido de mim?"

    p "Eu inclusive te ajudei a chegar na caverna, bobinho."

    mc "Co-como..."

    p "Mesmo assim, só vou deixar você ir bater perna de manhã. Nos outros horários você é só meu."

    mc "Mas..."

    p "Vou me levantar. Dá uma licencinha."

    p "Opa!"

    scene pixie noite_feliz with Dissolve(1.0)

    p "Eu gosto muito de você, [mc]. De todos que eu possuí, você realmente está sendo o mais especial."

    p "Eu..."

    p "Eu torço para que de alguma forma as coisas não acabem como elas devem."

    p "Que de alguma forma você consiga evitar o que está por vir."

    mc preocupado "Agora você tá me assustando..."

    p "Não pense muito nisso. Melhor você acordar."

    mc preocupado "Só que eu ain-"

    p "Xau xau, [mc]!"

    scene black with Dissolve(1.0)

    p "Nós vamos estar sempre com você."

    $ pixie_e2 = "fim"

    $ pixel_evento = 6

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("pixie_e2_fim","pixie","personagem")

    $ renpy.block_rollback()

    return

label pixie_evento1:

    $ pixie_e1 = "iniciou"

    "Que estranho... a [p] não aparecer pra me receber."

    "Onde será que ela tá?"

    "Melhor eu procurar ela. Eu já andei por aqui antes, eu sei o caminho."

    "..."

    scene fadolandia ponte with Dissolve(1.0)

    "Caraca, eu vi esse lugar aqui da outra vez."

    if notas_do_confinado2:

        "Foi aqui que eu encontrei a nota do confinado. Estava embaixo de um corpo melequento."

        "Parece que o corpo não tá mais aqui."

        "A mensagem daquele... será que eu posso chamar de... recado? Enfim, aquela mensagem me deu mó arrepio."

        "Eu não lembro exatamente o que era, mas parecia que o cara tinha tido um final terrível."

    "Não sei se eu devo continuar andando por aqui. Eu queria muito saber o que tem por trás daquelas árvores."

    "Só que a [p] me dá um pouco de medo. Ela pode me trazer aqui quando quiser. É como se ela tivesse controle sobre meus sonhos."

    "E o mais estranho é que eu nunca lembro quando eu acordo. Será que isso é só um sonho mesmo?"

    "Será que é outra dimensão?"

    mc envergonhado "Acho que eu devia ficar quieto e parar de pensar besteiras."

    scene fadolandia ponte with hpunch

    p "Oi, bonitinho."

    mc angustiado "ÂEEIIN!!"

    show pixie bonitinha with dissolve

    p "Te assustei?"

    mc preocupado "Pra caralho..."

    p "Teehee!"

    mc concentrando "Que susto, [p]..."

    p "Isso é pra você aprender a não sair por aí xeretando na casa dos outros."

    mc desconfiado "Xeretando?"

    menu:
        "Desculpa. Não queria desrespeitar você.":


            mc desculpa "Malz. Não era minha intenção desrespeitar você."

            p "Não se preocupe com isso, bobinho."

            p "Só não se esqueça de sempre vir me ver direto quando vier pra cá."

            mc normal "Ok. Combinado."
        "Qual é o problema? Tá escondendo alguma coisa?":


            $ f1_atencao += 1

            mc desconfiado "Parece que você ficou incomodada... Tem alguma coisa que eu não posso ver por aqui?"

            show pixie desconfiada with dissolve

            p "Como assim?"

            mc "Qual é o problema de eu andar por aqui?"

            p "Você é tonto? Você vai na casa de alguém e fica andando pelo quintal sem falar com ela?"

            mc zerado "..."

            mc normal "Então se eu te chamar podemos sair por aí?"

            p "Não."

    p "E agora chega de papo e vamos pra..."

    show black with dissolve

    "Garota" "{size=10}Socorro...{/size}"

    hide black with dissolve

    mc preocupado "O-o que foi isso?"

    show pixie desconfiada with dissolve

    p "O que foi agora?"

    mc "Eu..."

    show black with dissolve

    "Garota" "{size=10}No meio da floresta...{/size}"

    hide black with dissolve

    mc "..."

    p "Ei, [mc]. Tudo bem?"

    menu:
        "Eu escutei uma voz...":


            $ f1_atencao += 1

            mc "Eu... minha vista escureceu e..."

            mc "Eu escutei uma voz. Parece que tava dentro da minha cabeça."

            p "E o que ela disse?"

            mc "Era alguém pedindo ajuda."

            p "Sei..."
        "Não foi nada. Só me deu uma tontura.":


            mc desculpa "Não foi nada. Foi só uma tontura do nada..."

            p "Tontura?"

            p "..."

    show pixie explanando with dissolve

    p "Este lugar pode mexer um pouco com a cabeça dos humanos."

    p "Lembra que eu te disse isso quando você veio pra cá pela primeira vez?"

    mc desculpa "Acho que eu me lembro, sim."

    p "Pois é."

    show pixie sorrindo with dissolve

    p "Não precisa ficar pensando nisso, ok?"

    p "Logo logo você vai se sentir melhor. Tá tudo certo."

    mc envergonhado "Ok."

    show pixie provocando with dissolve

    p "Ah! Eu consegui uma roupa nova. Quer ver como fica em mim?"

    p "É daquelas que eu tenho certeza que você vai adorar."

    menu:
        "Com certeza. Vamos lá ver.":


            mc tarado "Com certeza. Não perderia isso por nada."

            p "Foi o que eu pensei."

            jump pixie1_continua
        "Hoje não. Não tô me sentindo legal.":


            mc desculpa "Foi mal, mas hoje não tô bacana. Acho que vou acordar."

            show pixie desconfiada with dissolve

            p "Quê?! Vai perder a chance de me ver em uma roupa mega sexy?"

            mc "É..."

            menu:
                "Sim. Quero acordar.":


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("pixie1_fugiu","pixie","personagem")

                    mc "Desculpa, mas desta vez eu vou. Realmente não tô legal."

                    p "Que droga, [mc]... Mas tudo bem. Eu entendo."

                    p "Você que vai perder."

                    jump pixie1_final
                "Pensando melhor, acho que vou ver.":


                    mc normal "Ok, ok. Não precisa ficar assim. Eu vou com você."

                    show pixie provocando with dissolve

                    p "Agora, sim!"

                    p "Tenho certeza que você não vai se arrepender."

                    mc envergonhado "..."

                    jump pixie1_continua

label pixie1_continua:

    $ f1_biquini = True

    p "Então vamos lá para casa que eu vou me trocar."

    mc normal "Ok. Tô logo atrás."

    hide pixie with dissolve

    "Que merda foi essa que aconteceu comigo?"

    "Uma garota me pedindo socorro..."

    "Será que isso é sério? Será que é só uma invenção da minha cabeça?"

    "..."

    scene fadolandia casa with Dissolve(1.0)

    show pixie provocando with dissolve

    p "Você pode me esperar aqui enquanto eu me troco?"

    if p1_pixie_espiar:

        p "Ou você vai querer me espiar igual aquela outra vez, hein?"

        mc tarado "..."

        p "Ainda não esqueci que você tava me olhando."

        mc desconfiado "Aliás, daquela vez eu tive a sensação que você tinha virado por meio segundo e me olhado nos olhos."

        mc "Isso aconteceu mesmo?"

        p "Querido, eu posso fazer coisas que você nem imagina..."

        mc safado "Por que parece que você tá me provocando?"

        p "Porque eu estou."

        mc "..."

    p "Já já te chamo. Vai ser bem rapidinho."

    mc normal "Ok."

    hide pixie with dissolve

    "A [p] vai se trocar bem na minha frente. E ela sempre deixa a janela aberta."

    "Será que eu devo dar uma olhadinha nela peladinha?"

    "Se bem que talvez essa fosse uma boa oportunidade de dar uma xeretada por aqui. O que será que eu posso encontrar?"

    menu:
        "Vou esperar ela aqui. Não quero mais encrenca.":


            "Acho que eu já causei demais com ela por hoje."

            mc concentrando "Vou só esperar ela aqui."

            "{b}Alguns minutos depois{/b}"

            "..."

            jump pixie1_roupa
        "Vou dar uma espiada pela janela...":


            $ renpy.block_rollback()

            mc tarado "Eu vou é dar uma olhada nessa belezinha pelada."

            "..."

            scene fadolandia casa_janela with Dissolve(1.0)

            "Tenho que tomar cuidado com a cabeça. A [p] parece bem relax pra essas coisas, mas vai saber o que ela vai fazer se me pegar aqui."

            "Agora não tem mais volta. Vamos lá."

            "..."

            mc surpreso "!"

            scene pixie pelada1 with Dissolve(3.0)

            pause

            mc "{i}gulp{/i}"

            "A [p] pode não ser humana, mas ela continua sendo gostosa pra caramba."

            "Esse corpo petit dela parece que tem carne nos lugares certos."

            "Melhor eu dar o fora daqui antes que ela perceba."

            "Se é que ela já não percebeu."

            jump pixie1_roupa
        "Vou procurar algo no entorno da casa.":


            $ renpy.block_rollback()

            "Essa pode ser uma boa oportunidade pra dar uma fuçada sem chamar a atenção dela."

            "Se ela tá escondendo algo de mim, talvez eu possa encontrar alguma coisa por aqui."

            "..."

            scene fadolandia varanda with Dissolve(3.0)

            "Aquele apagão... a voz... esse lance que aconteceu comigo hoj..."

            show black with dissolve

            "Garota" "{size=10}Por favor... eu preciso de você...{/size}"

            hide black with dissolve

            mc angustiado "..."

            "De novo isso..."

            "Parece que alguém está precisando de ajuda."

            "Mas isso não é um sonho? Como alguém pode estar pedindo ajuda dentro do meu sonho?"

            "Quanto mais eu penso, menos tudo isso parece um sonho."

            "Mas então... o que é tudo isso?"

            "..."

            mc desconfiado "Epa! O que é isso aqui?"

            show mc lendo_nota with dissolve

            "{i}Notas do Confinado III{/i}"

            if notas_do_confinado1 or notas_do_confinado2:

                "É um papel parecido com aquela outra nota que eu li."
            else:


                "O número desta nota é três. Será que tiveram outras duas antes?"

            "{i}Sua alegria era contagiante, sua pele era brilhante, seu corpo era voluptuoso.{/i}"

            "{i}Minha grande amiga em horas, minha grande paixão em outras.{/i}"

            "{i}Minha excitação crescia a cada visita. Eu estava tão perto de conseguir o que queria.{/i}"

            "{i}E então aconteceu. Tudo o que eu buscava.{/i}"

            "{i}E sua pele era seca, seu olhar era profundo, sua face era demoníaca.{/i}"

            "{i}O que eu fiz? Era tarde demais. Será para você também?{/i}"

            "..."

            "Quer merda foi essa?"

            "Quem será que escreveu isso aqui?"

            "Merda. Não tenho tempo pra pensar nisso agora."

            "Deixa eu sair daqui antes que ela venha me procurar."

            hide mc with dissolve

label pixie1_roupa:

    "..."

    scene fadolandia casa with Dissolve(1.0)

    "..."

    p "Estou pronta, [mc]!"

    mc zerado "Aleluia..."

    p "Pronto para ficar duro?"

    mc safado "Com certeza."

    p "Então pode entrar."

    mc "Claro..."

    scene fadolandia casa with vpunch

    mc angustiado "!"

    "Que calafrio foi esse?"

    "Alguma coisa não tá me cheirando bem."

    menu:
        "Entrar na casa":


            "Foda-se. O que tem me esperando lá dentro é mais importante que um calafrio idiota."

            mc safado "..."
        "Inventar uma desculpa e acordar":


            "Não tô gostando nada do que tá acontecendo no meu sonho hoje."

            "Acho que é melhor eu dar o fora daqui e voltar outra hora."

            p "Algum problema, bonitinho?"

            mc preocupado "Desculpa, [p]. Mas hoje eu realmente não tô me sentindo bem."

            mc "Acho que eu quero acordar. Estou quase desmaiando."

            p "Sério, bebê?!"

            p "Tô indo aí."

            "..."

            label pixie1_parar:

                show pixie b_preocupada with dissolve

                p "Tá tudo legal?"

                "Uou. Perto de mim, e vestida desse jeito... Será que eu devia ter entrado na brincadeira?"

                mc "Eu tô muito zonzo e sinto que eu posso desmaiar."

                p "Que estranho, eu nunca ouvi falar nada disso aqui no Zei... quero dizer, aqui na Fadolândia."

                mc "Não sei como explicar. Tudo começou antes da gente vir pra cá."

                p "Tudo bem. Não se preocupe. É melhor você acordar."

                jump pixie1_final

    scene fadolandia interior with Dissolve(1.0)

    p "E aí?"

    mc surpreso "..."

    show pixie b1 with dissolve

    pause

    p "Sou ou não sou a fada mais sexy do mundo."

    menu:
        "Com certeza. Você é muito gostosa.":


            p "{i}Hmmm...{/i}"

            p "Adoro quando você paga pau pra mim."

            mc safado "..."

            p "Acho que você merece um showzinho."

            mc "Também acho."

            show pixie b2 with dissolve

            pause

            p "E assim? O que você acha da minha bunda?"

            menu:
                "A mais gostosa que eu já vi.":


                    p "{i}Hmmm...{/i}"

                    p "Isso. Continua falando."

                    mc "Eu tenho muita vontade de pegar nela."

                    p "Você quer?"

                    mc "Claro."

                    p "Quem sabe daqui a pouco."

                    p "Tenho mais pra você."

                    mc "Quero ver..."

                    show pixie b3 with dissolve

                    pause

                    menu:
                        "Como você é deliciosa...":


                            $ f1_poder = True

                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("pixie1_poder","pixie","personagem")

                            $ renpy.block_rollback()

                            p "Aaaiii... Como eu gosto quando você fala assim. Eu tô pegando fogo, [mc]."

                            mc safado "Você sabe que eu também tô."

                            p "Eu adoro quando você fica cheio de tesão. Eu vejo nos seus olhos a vontade de me pegar."

                            p "Você quer rasgar minha roupa e me comer agora mesmo."

                            mc "Sim!"

                            mc "O que acha da gente fazer o que a gente quer de uma vez?"

                            p "..."

                            p "Nós vamos."

                            p "Mas não hoje."

                            mc triste "Quê?! Por que não?"

                            show pixie b_provocando with dissolve

                            p "Muito obrigada. Ver você se deliciando comigo é tudo o que eu precisava."

                            mc serio "Mas e eu?"

                            mc "Como que eu fico?"

                            p "Você vai lá no seu mundo e se satisfaz sozinho ou vai atrás de uma das suas peguetes."

                            mc bravo "Isso não é justo, [p]. Você só me provoca."

                            p "Tenha calma, bebê. Sua hora vai chegar."

                            mc desculpa "Que droga..."

                            p "Você ainda vai poder aproveitar tudo isto aqui. Só ter paciência."

                            p "Eu ainda tenho muito o que sentir vindo de você antes do fim."

                            mc serio "E agora? Acho que quero acordar."

                            jump pixie1_final
                        "Acho melhor inventar uma desculpa e parar por aqui":


                            mc desculpa "Desculpa, [p]. Você sabe que eu adoro ver você assim, mas eu acho que preciso parar."

                            mc "Eu não tô me sentindo nada bem. Tô preocupado."

                            jump pixie1_parar
                "Já vi melhores lá no meu mundo.":


                    mc tarado "Já vi umas bundas mais gostosas lá no meu mundo."

                    p "Quê?!"

                    hide pixie with dissolve

                    p "Você fodeu o clima, [mc]."

                    mc envergonhado "..."

                    mc desculpa "Desculpa... Não sei porque disse isso. Eu não tô me sentindo legal hoje."

                    jump pixie1_parar
                "Acho melhor inventar uma desculpa e parar por aqui":


                    mc desculpa "Desculpa, [p]. Você sabe que eu adoro ver você assim, mas eu acho que preciso parar."

                    mc "Eu não tô me sentindo nada bem. Tô preocupado."

                    jump pixie1_parar
        "Nunca vi outras pra poder falar.":


            mc desconfiado "Pra falar a verdade eu nunca vi outras fadas pra poder falar que você é a mais sexy."

            mc "Tem mais fadas por aqui? Onde elas estão?"

            hide pixie with dissolve

            p "Você tá matando o clima, [mc]. Não era essa a resposta certa."

            mc desculpa "Desculpa... Não sei porque disse isso. Eu não tô me sentindo legal hoje."

            jump pixie1_parar

label pixie1_final:

    p "Vamos lá para a entrada então."

    "..."

    scene fadolandia geral with Dissolve(1.0)

    if not f1_poder:

        $ f1_atencao += 1

        mc preocupado "Desculpa qualquer coisa... Estou me sentindo um pouco melhor."

        mc normal "Valeu pela ajuda."

        if f1_biquini:

            show pixie b_provocando with dissolve
        else:


            show pixie bonitinha with dissolve

        p "Isso é bom, [mc]. Quero que você só sinta coisas boas vindo para cá."
    else:


        show pixie b_provocando with dissolve

        p "Espero que você tenha gostado do meu show pra você. Eu com certeza adorei."

        mc serio "Poderia ter algo mais físico, mas que seja..."

        p "Não fique triste, bebê. Vou estar aguardando você voltar, como sempre."

    mc normal "Falando nisso, toda vez que eu venho aqui você vem me receber. Você não dorme, não?"

    p "Que pergunta é essa?"

    mc "Sei lá. Sempre que eu vim aqui você tava acordada."

    p "Hmmm..."

    if f1_atencao < 2:

        p "Na verdade eu tenho que dormir, sim. Mas normalmente eu {b}durmo de manhã{/b}."

        mc normal "Entendi. Interessante saber isso sobre você."

        p "Você me deixa excitada querendo saber mais sobre mim..."

        mc zerado "[p]..."
    else:


        p "Eu não preciso dormir. Eu estou sempre acordada porque as fadas são uma raça mágica."

        mc normal "Entendi. Bom pra você, hein?"

        p "Pois é..."

    p "Não deixe de vir me visitar, ok?"

    mc charmoso "Com certeza. Sempre que der eu passo aqui."

    p "Combinado. Até mais, [mc]."

    mc normal "Até, [p]."

    scene black with Dissolve(1.0)

    return

label fadolandia_pixie:

    $ fado_type = "pixie"

    call checa_fadolandia from _call_checa_fadolandia

    return

    return

    jump call_cidade

    label pixie_historia:

        if pixie_historia > 0:

            p "Pronto para continuarmos?"

            mc charmoso "Sim."

            p "Então vamos."

            scene black with Dissolve(1.0)

            "..."

            if pixie_historia == 5 and pixel_evento < 1:

                "Garota" "{size=10}Socorro...{/size}"

                "Hm?! Isso de novo?!"

                "Garota" "{size=10}Por favor! Não esqueça de mim!{/size}"

                "Eu já tinha ouvido isso antes... tem alguém aqui nesse lugar além de mim e da [p]..."

                "Eu preciso encontrar ela. Talvez ela me explique melhor quem é a [p] e o que tá acontecendo comigo."

                "Eu sinto que a [p] não me conta a história toda. Talvez... essa garota gritando me ajude."

                "Tenho que vir quando a [p] estiver dormindo e encontrar essa garota escondida e conversar com ela!"

                "Talvez seja melhor eu {b}descobrir quem é ela antes de voltar a andar com a [p]{/b}."

                p "Vem logo, [mc]!"

                mc surpreso "O-opa! Tô indo!"

                "..."

        if pixie_historia == 0:

            $ pixie_historia = 1

            scene pi3_fado2 with Dissolve(1.0)

            p "Que bom que você aceitou, [mc]! Estou ansiosa para ir com você!"

            p "Tem tanta coisa que eu quero que você veja, que você saiba. E principalmente... eu quero que você me veja."

            mc envergonhado "T-te veja? Como assim?"

            p "Eu serei sua nesses passeios. E promero que eu deixarei você fazer o que quiser comigo quando chegarmos ao final."

            mc surpreso "T-tudo!?"

            scene pi3_fado1 with Dissolve(1.0)

            p "Tudo mesmo. O objetivo dos nossos passeios vai ser como vocês humanos se aproximam. Como encontros..."

            p "No fim desses encontros, eu permitirei que você me tenha, da forma que você quiser."

            menu:
                "Então vamos logo. Eu quero você.":


                    $ renpy.block_rollback()

                    mc safado "Então bora começar isso logo. Não vejo a hora de te pegar, [p]."

                    p "Não se afobe, homem. Sua hora vai chegar. Tenha paciência."

                    mc "..."
                "E se eu não quiser nada contigo?":


                    $ renpy.block_rollback()

                    mc envergonhado "E se... por acaso... eu não quiser nada com você?"

                    p "Haha... que fofo... claro que você vai querer, bobinho."

                    mc "Mas e se-"

                    p "É impossível, [mc]. Quando você ver de perto tudo o que eu tenho para você, é impossível que você me negue."

                    mc "Ok..."

            p "Eu quero que você me espere perto da ponte. Eu vou me preparar e te encontro lá."

            mc normal "Ok. Tô indo pra lá."

            scene fadolandia ponte with Dissolve(1.0)

            "Pra onde será que a [p] quer me levar? Essa ponte..."

            if fadex_1vez:

                "Eu passei por aqui depois que ouvi uma voz... nem lembro quanto tempo faz que isso aconteceu."

                "Existe praticamente um mundo diferente depois desta floresta."
            else:


                "Eu nunca passei por ela..."

                "O que será que existe depois desta floresta?"

            "A [p] deve conhecer isso aqui muito melhor do que eu... eu fico imaginando pra onde ela vai me levar."

            p "[mc]?"

            mc normal "Oi."

            show pixie b_provocando with dissolve

            p "Estou aqui. Pronto?"

            mc normal "Sim."

            p "Veja, [mc]... O caminho que nós vamos seguir não será simples. É provável que você vá desistir várias vezes antes de chegarmos."

            mc preocupado "Por que desistir? Tem algum perigo nisso, [p]?"

            p "Atingir locais desconhecidos é desgastante. Você vai entender logo."

            mc zerado "Você me passa confiança zero falando assim."

            hide pixie with dissolve

            p "Pare de autopiedade e vamos."

            mc "..."

            scene black with Dissolve(1.0)

            "..."

            mc preocupado "P-pixie... esse lugar não parece legal..."

            scene pi3_floresta1 with Dissolve(2.0)

            pause

            p "Qual o problema?"

            mc "Essa floresta... não dá pra ver nada... e tudo parece meio gigante..."

            p "Não coloque a culpa em mim. Não sou eu quem cria essas imagens..."

            mc "Não é essa a questão. Eu quero saber que lugar é esse aqui."

            p "Aqui é-"

            scene black with vpunch

            mc angustiado "Argh!"

            mc "O que aconteceu!? Eu caí! Não vejo nada!"

            p "Calma, paspalho! Sua energia acabou... só isso. Não vai dar pra continuarmos nessas condições..."

            mc concentrando "É isso que você quis dizer quando falou que eu ia desistir?"

            p "Exatamente."

            mc angustiado "Mas eu nem comecei!"

            p "É assim mesmo. Você precisa acordar e recuperar suas energias. Volte aqui depois e prosseguimos."

            p "Quando estiver pronto, só falar comigo e me avisar."

            mc concentrando "T-tá legal. Vou tentar acordar."

            p "..."

            return

            return

            jump call_cidade

        elif pixie_historia == 1:

            $ pixie_historia = 2

            scene pi3_floresta1 with Dissolve(2.0)

            mc "Foi aqui que a gente parou da outra vez."

            p "Sim. Isso vai acontecer bastante. Então é importante você guardar os sentimentos que você vai sentir."

            mc "Como assim sentimentos?"

            p "Para o que a gente vai fazer, razão não importa muito, [mc]. Eu preciso que você deixe o sentimento fluir e tomar conta."

            p "Eu quero que você sinta sem amarras, sem as barreiras da consciência ou da sociedade. Eu quero você como um animal."

            menu:
                "Eu gosto assim também.":


                    $ renpy.block_rollback()

                    mc "Eu quero isso também."

                    p "Assim que se fala, garoto! Pode deixar que eu vou te ajudar. Vou te treinar direitinho."
                "Será que isso é certo?":


                    $ renpy.block_rollback()

                    mc "S-será que isso é certo?"

                    p "Certo... errado... Por que vocês sempre pensam nesses termos?"

                    mc "Sei lá... educação talvez?"

            p "Vocês perdem muita energia para se colocar dentro de uma caixinha, tentando viver igual aos outros. Fazer parte do clubinho."

            mc "[p]... É assim que as pessoas conseguem viver juntas..."

            p "Isso me cansa, [mc]!"

            scene pi3_floresta2 with Dissolve(1.0)

            pause

            p "Eu quero ver você e os outros ficando loucos! Quero ver a sensação e os desejos tomando conta!"

            p "Libertos de todas essas coisas que a civilização criou para nos enclausurar!"

            p "Ah... [mc]... se eu pudesse, eu pegava tudo isso de novo e sumia com tudo!"

            mc "Acho que você tá meio doidona..."

            p "Eu? Eu estou mais sã do que nunca. E muito graças à você."

            mc "E-eu?"

            p "Sim."

            mc "E o que eu fiz?"

            p "Não importa. Só continue fazendo o que você faz e ouvindo meus conselhos. Juntos a gente vai longe."

            mc "Ok. Mas eu n-"

        elif pixie_historia == 2:

            $ pixie_historia += 1

            scene pi3_floresta2 with Dissolve(2.0)

            mc "Essa floresta não tá legal, [p]... eu nem sei porque eu tô vindo aqui com você."

            p "Não é óbvio? Você me ama."

            mc "Não sei da onde você tira toda essa autoestima..."

            p "Uma mulher poderosa consegue o que quer, [mc]. Isso é que que todas deveriam entender."

            mc "Isso não vale pros homens também?"

            p "Os homens são diferentes. Eles são animais, criaturas mais simplórias. Vocês procuram satisfação."

            mc "E as mulheres?"

            p "As mulheres procuram a essência das coisas. Nós procuramos a beleza, a segurança, a plenitude. São coisas diferentes."

            mc "Mas já faz tempo que as mulheres lutam pela igualdade. Será que todas as pessoas no fundo não querem a mesma coisa?"

            p "Esse tipo de luta é superficial e de curto prazo. O que acontece é que elas olham para os homens e querem o que eles têm."

            p "Isso não é de hoje, [mc]. A busca por um lugar na mesa existe em qualquer relação e em qualquer tempo e local."

            mc "E não tá certo querer um lugar na mesa?"

            scene pi3_imagem1 with Dissolve(1.0)

            pause

            p "Isso é ridículo. É como ser um cavalo e só poder ver o caminho que vai em frente, e ignorar as rotas laterais."

            mc "Não sei se eu tô entendendo..."

            p "Se eu fosse uma mulher nessas condições, eu não ia querer ser como um homem. Longe de mim."

            p "Eu o dominaria, teria tudo o que é dele, e do irmão dele e do pai dele também. Eu não me contento com a igualdade."

            p "Quando uma mulher poderosa se livra do cabresto, ela percebe que as lutas da maiora são fúteis."

            p "O que vale é o que está no fim do arco-íris. É estranho como isso é tão simples de entender, mas vocês não conseguem."

            menu:
                "Haha... é fácil mesmo...":


                    $ renpy.block_rollback()

                    mc "É fácil... concordo com você... tsc tsc... esse pessoal burro, viu?"

                    p "Ai, [mc]... você é o homem perfeito pra qualquer mulher esperta."

                    mc "Hm? O-obrigado."

                    p "Não precisa agradecer."
                "Não sei se é tão simples assim...":


                    $ renpy.block_rollback()

                    mc "Acho que você acha isso simples... mas é bem difícil de entender esse raciocínio."

                    p "Talvez pra vocês que vivem tão pouco."

                    p "Mas o que esperar de um homem, certo?"

                    mc "Ei..."

            p "Estamos bem perto do fim da floresta."

            mc "Ufa... eu tô meio cansado."

            p "Segura mais um pouco, [mc]. Estamos quase lá."

            mc "Pode deixar. Eu sei que eu consig-"

        elif pixie_historia == 3:

            $ pixie_historia += 1

            scene pi3_imagem1 with Dissolve(1.0)

            pause

            mc "Então a gente tá chegando no fim?"

            p "Isso. Quem diria que você seria uma pessoa confusa assim, hein?"

            mc "Como assim? O que uma coisa tem a ver com a outra?"

            p "Não é óbvio? Essa floresta é sua cabeça, [mc]."

            mc "Bom... eu achei que tudo fosse da minha cabeça, já que é um sonho meu..."

            p "Você não está errado. Mas não é tão simples quanto você está pensando. Este não é apenas um sonho."

            mc "Hmm... se você é parte do sonho... então o sonho não é sonho pra você... certo?"

            p "Hahaha! Não! Você está vendo tudo isso de forma errada. Sua cabeça não cria o que você está vendo, mas molda o resultado."

            mc "Molda e não cria? Qual é a diferença?"

            p "Toda. Moldar algo que existe é diferente de criar algo que não existia antes."

            menu:
                "Não entendi...":


                    $ renpy.block_rollback()

                    mc "Não entendi ainda... qual seria a diferença."

                    p "Imagine que você esteja em uma completa escuridão. E então você coloca um óculos que lhe permite ver no escuro."

                    p "O óculos muda a percepção do espaço, revela o que estava oculto, mas não cria nada do que já existia ali."

                    p "Sua mente é como o óculos. Não cria, mas molda o que existe de forma que você possa perceber."

                    mc "Caralho... isso é bem complexo."
                "Isso é demais pra mim. Só vamos sair daqui.":


                    $ renpy.block_rollback()

                    mc "Quer saber? Isso é demais. E se a gente só sair daqui?"

                    p "Essa foi a coisa mais inteligente que você disse nos últimos tempos."

                    mc "..."

            p "Veja. Tamo bem perto do fim."

            scene black with dissolve

            mc surpreso "Mano! Como assim?!"

            scene eanna1 with Dissolve(2.0)

            pause

            mc surpreso "A gente saiu de uma floresta pro meio de um deserto?!"

            p "Sim. Isso é algo básico."

            mc zerado "Isso pode ser qualquer coisa, menos bas-"

        elif pixie_historia == 4:

            $ pixie_historia += 1

            scene eanna1 with Dissolve(1.0)

            pause

            mc concentrando "Conseguimos voltar aqui..."

            p "Da outra vez você apagou igual um fraco."

            mc zerado "Ei, da outra vez eu senti tipo um soco na barriga quando a gente entrou aqui."

            p "Isso é normal. Nós estamos mudando de vibração. Esse choque acontece com qualquer criatura consciente."

            mc "Não vou nem tentar mais entender o que você tá falando. Agora... que lugar é esse?"

            p "Aqui é o nosso objetivo. Foi para te trazer aqui que eu apareci na sua vida."

            mc surpreso "S-sério?"

            p "Venha."

            mc "O-ok."

            scene pi3_imagem2 with Dissolve(1.0)

            pause

            mc "O que a gente vai fazer nesse lugar?"

            p "Algo que só você pode fazer. É a sua missão neste mundo."

            mc "Missão? Tipo um escolhido?"

            p "Se você se sente melhor pensando assim... claro."

            mc "E o que só eu posso fazer? Eu sou só um cara normal... né?"

            p "Ah, sim. Você é só um sujeito como outro qualquer. Até mais normal que a maioria eu diria."

            mc "E isso é bom... digo, é bom pro que você quer que eu faça?"

            p "Você é bom o suficiente. Mas devido à conjuntura, você é o único capaz de realizar o que eu preciso."

            mc "Como que um cara 'manos normal que a maioria' pode ser o único que pode fazer uma coisa?"

            p "Por que tantas perguntas? Você precisa melhorar essa autoestima urgente."

            menu:
                "Não é nada...":


                    $ renpy.block_rollback()

                    mc "Não é nada. Esquece."

                    p "Isso. Vamos falar menos e agir mais, ok?"

                    mc "..."
                "Eu não confio em você completamente...":


                    $ renpy.block_rollback()

                    mc "A verdade é que eu não confio completamente em você, [p]... sei lá... eu sinto que tem algo de errado."

                    p "Seguir sua intuição é importante. A maioria dos humanos pensa demais antes de agir."

                    p "Se vocês abandonassem essas correntes da consciência e fossem mais animais, vocês iriam longe."

                    mc "Você quer dizer que... e-eu tô certo de desconfiar de você?"

                    p "Se eu te der qualquer confirmação, você não estará mais seguindo sua intuição. Por isso, não posso responder."

            mc "Sem dúvidas esse é o sonho mais estranho que eu já tive..."

            p "E provavelmente será o mais estranho que você terá em toda sua vida."

            mc "É o que p-parec-"

        elif pixie_historia == 5:

            $ pixie_historia += 1

            scene pi3_imagem2 with Dissolve(1.0)

            pause

            p "Não se preocupe que vamos chegar logo. Aproveite esse passeio para poder me admirar o máximo que puder."

            mc "Olha... esse seu biquíni realmente mostra bastante coisa pra admirar..."

            p "É o que tem, né? Infelizmente o que eu uso diz mais sobre você do que sobre mim."

            mc "E-eu não quero que você fique seminua desse jeito. Nem vem."

            p "Tem certeza? Porque eu acho que você quer, sim."

            mc "Q-quando eu te conheci você tava com outra roupa! E-eu tenho certeza!"

            p "Quando eu te conheci você não era tão tarado quanto agora. Sua cabeça mudou muito nos últimos tempos."

            mc "Hmm... talvez você tenha razão..."

            p "Mas isso é normal, viu? Todo ser humano é assim. É muito difícil encontrar alguém que se contente com o que tem."

            scene pi3_imagem3 with Dissolve(1.0)

            pause

            mc "Você tá falando que eu sou ganancioso? Alguma coisa assim?"

            p "Também. Mas acho que ambicioso seria a melhor palavra nesse caso. O homem sempre procura por mais. Nunca está bom."

            p "Esse desejo inesgotável é o que move a humanidade, seja para cima ou para o fundo do precipício."

            mc "Mas é normal a gente sempre querer uma vida melhor. Você tem que concordar comigo nessa."

            p "Só que mais é sempre melhor? Será que não existem pessoas que estão felizes, mas mesmo assim querem mais?"

            p "Veja... eu não acho isso ruim. Esse desejo da humanidade é o que faz ela incrível. É por isso que eu amo vocês."

            p "Esse é o desejo que eu coloquei no coração de cada um. No seu também. É um presente pro meu queridinho."

            mc "Presente pra mim? Valeu..."

            p "Eu fiz muita coisa para você, [mc]. Mais do que você imagina. E ainda vou fazer mais."

            mc "Só por que você me ama?"

            p "Claro. Eu só vou querer uma coisinha em troca. Mas é uma coisa rápida."

            mc "O quê?"

            p "Não se preocupa com isso agora. Logo logo eu te falo. Mas eu garanto que você vai adorar e não vai levar muito tempo."

            mc "Se você diz... é pra esse lugar que a gente tá indo? Onde eu vou fazer esse favor pra você?"

            p "Sim! Garoto esperto. Logo logo a gente chega lá se você não apagar que nem um idio-"

        elif pixie_historia == 6:

            $ pixie_historia += 1

            scene pi3_imagem3 with Dissolve(1.0)

            pause

            mc "[p]... posso te perguntar uma coisa?"

            p "Claro."

            if pixel_evento > 5:

                mc "O que... o que aconteceu com a gente naquele dia que a Fadolândia tava de noite?"

                mc "Tipo... eu nunca tinha visto ela daquele jeito..."

                p "Ah... não sei se eu quero falar sobre isso, [mc]."

                mc "Como assim? Por quê?"

                p "Eu não estava bem naquele dia... um tanto nostálgica. Pensando em tempos antigos, entende?"

                mc "Acho que sim..."
            else:


                mc "Tem mais alguém aqui em Fadolândia além da gente?"

                p "Por que quer saber isso?"

                mc "Eu tava pensando nisso esses dias..."

                p "O lugar nós estamos é grande, [mc]. Provavelmente existam outras criaturas. Mas eu não recomendo você procurar."

                mc "Hmm... e mais uma coisa..."

                p "Hm?"

            mc "Você... quem é você, [p]?"

            p "Que pergunta é essa? Eu sou isto que você está vendo. O que mais seria?"

            mc "Você disse que meu sonho é como um óculos que muda o que tá acontecendo... será que eu mudei você também?"

            p "Então você está prestando atenção no que eu estou falando? Não creio..."

            mc "Eu sei que você acha que eu sou idiota, mas eu sou muito esperto."

            scene pi3_imagem4 with Dissolve(1.0)

            p "Bom... talvez você tenha razão. Você é o primeiro que me pergunta uma coisa assim."

            mc "Primeiro? Então você já esteve nos sonhos de outras pessoas?"

            p "Muitas, [mc]... fica até difícil de contar. Mas, pelos deuses... acredito que esta será a última vez."

            mc "Hmm... mas, então. Quem é você?"

            p "Você não desiste mesmo, né? Você não sabe como tratar uma dama."

            menu:
                "Fala logo.":


                    $ renpy.block_rollback()

                    mc "Responde logo. Além de que de 'dama' você não tem muito."

                    p "Que absurdo... não acredito que tenho que ouvir isso."

                    mc "Você tá desviando do assunto de novo."

                    p "Como eu posso explicar de uma forma que você entenda?"

                    p "Eu sou mais de uma coisa. Eu sou um amálgama de vontades. Eu sou o resultado de uma liga de identidades."

                    p "Essa seria a resposta simples."

                    mc "Essa é a simples?!"

                    p "Sim..."

                    mc "Isso não explica nada."

                    p "Será? Você tem realmente prestado atenção no que eu digo? No que acontece aqui?"

                    p "Você não esperava que seria algo como 'eu sou sua mãe', né?"

                    mc "Acho que eu tava torcendo pra ser alguma coisa que eu pudesse entender... só isso..."

                    p "Não pense demais nisso. Sua tarefa não é pensar."
                "Ok, não quero forçar também.":


                    $ renpy.block_rollback()

                    mc "Tá bom. Se você não quer falar, foda-se."

                    p "Agora sim você falou igual homem. A gente sabe que o que você quer de mim não é o nome."

                    mc "E eu vou ter o que eu quero?"

                    p "Se você continuar me agradando assim, vai sim."

                    mc "Tô esperando então..."

            mc "Eu não sei o quanto eu posso confiar em v-"

        elif pixie_historia == 7:

            $ pixie_historia += 1

            scene pi3_imagem4 with Dissolve(1.0)

            pause

            mc "Ufa... acho que agora a gente chega até aquela construção lá na frente."

            p "Se você não perdesse energia questionando besteiras, teríamos conseguido da outra vez."

            mc "Não é besteira, [p]. A gente tá falando da minha cabeça. E você não me conta tudo."

            p "[mc]... nós dois sabemos o que realmente importa aqui. Você me quer, não é?"

            p "Você quer que eu arranque tudo o que eu estou usando e sente em você. Quer que eu pule no seu pau duro até você não aguentar mais."

            p "Você entende que sexo, tesão e atração pouco têm a ver com o que é dito. O que importa é o que é sentido."

            p "Cheiro, aparência, o tom da sua voz, a pose do seu corpo. Conquista tem a ver com partes das sua cabeça que você não tem acesso."

            mc "Você quer dizer que a gente não tem controle sobre isso?"

            p "Praticamente nenhum controle. Você pode se preparar antes, pode tentar montar um cenário que favoreça, mas o momento é irracional."

            p "O momento em que alguém decide ficar ou não com você, em um primeiro momento, é basicamente uma decisão animal baseada no instinto."

            p "Por isso, se alguém não quiser ficar com você, tem menos a ver com você e mais com ela, assim como o contrário também, na grande maioria dos casos."

            mc "No nosso caso também? Não é por causa do meu charme irresistível que você ficar comigo?"

            p "Você é fofo, [mc]... mas, não, infelizmente nós vamos trepar, mas isso tem pouco a ver com você."

            mc "M-mas-"

            p "Chega de falar! Olha!"

            scene black with dissolve

            mc surpreso "!"

            scene pi3_imagem5 with Dissolve(2.0)

            pause

            p "Finalmente chegamos! Que saudades deste lugar!"

            mc "Você já veio aqui antes?"

            p "Ai, [mc]... se você soubesse... eu fico molhada só de pensar em tudo o que aconteceu neste banho..."

            menu:
                "O que aconteceu aqui?":


                    $ renpy.block_rollback()

                    mc "E o que aconteceu nesse lugar? Por que... você ficou, assim..."

                    p "Excitada que nem um animal no cio?"

                    mc "N-não é bem isso que eu ia dizer..."

                    p "Aqui aconteceram bacanais infindáveis. Mulheres transando com mulheres, homens com homens, mulheres com homens... animais..."

                    p "Orgias sem fim... quem duravam dias... você não conseguia distinguir mais quem estava te comendo... tempos incríveis, [mc]."

                    mc "É... acho que isso é um pouco pesado demais pra mim..."

                    p "Apenas no começo. Quando você experimentar o doce do mel, sempre vai querer mais. E fica cada vez mais difícil de se saciar."
                "A gente podia aproveitar que você tá molhada...":


                    $ renpy.block_rollback()

                    mc "E se a gente aproveitasse que você ficou excitada pra acabar logo com isso?"

                    p "Com certeza eu daria para você agora sem pensar duas vezes. Este lugar realmente me faz ficar louca."

                    mc "Então! Eu topo com certeza."

                    p "Dói muito ter que negar uma trepada deliciosa, mas essa vontade só vai aumentar o sabor quando realmente acontecer."

                    mc "E quando vai ser isso?!"

                    p "Logo... estamos quase lá, [mc]."

                    mc "Que saco..."

            p "Mesmo que nós ainda não possamos nos divertir juntos, eu preciso ter certeza que você vai poder continuar o caminho."

            mc "O que eu preciso fazer?"

            p "Você precisa de mulheres, homens, quanto mais, melhor. Preciso que você domine todos no seu entorno."

            mc "No mundo real você diz?"

            p "O que será real? Esse é um conceito muito complexo. Mas, para não perdermos tempo, sim, é no seu 'mundo real'."

            p "Você se lembra do nosso primeiro encontro? Eu quero que você seja um caçador, que corra atrás de suas presas."

            p "Só depois de conquistá-las, você estará pronto para o próximo passo."

            mc "Mas e se eu não conseguir? Ou se eu não quiser ficar com todo mundo?"

            p "Então você terá sido um inútil e terá feito eu perder um tempo precioso da minha existência."

            mc "[p]... você precisa me falar a verdade. Por que tudo isso?"

            p "Se você quer tanto assim saber... então faça o que eu lhe ordeno. E depois você saberá tudo."

            mc "Não! Eu quero saber antes!"

            p "Acho bom você não se exaltar demais."

            mc "Por quê?! Eu preciso saber o que tá ro-"

            mc "Ai... deu uma fraqueza..."

            p "Está vendo? É por isso... usar energia demais vai dar em-"

        elif pixie_historia == 500:

            $ pixie_historia += 1

            scene pi3_imagem1 with Dissolve(1.0)

            pause

            menu:
                "":


                    $ renpy.block_rollback()

                    ""
                "":


                    $ renpy.block_rollback()

                    ""

            "..."

        scene black with vpunch

        mc preocupado "Agh!"

        p "Cansado de novo? É hora de acordar. Vamos continuar na próxima vez que você vier."

        mc concentrando "Ok... depois eu volto..."

        return

        return

        jump call_cidade

label fadolandia_exploracao:

    $ fado_type = "pixel"

    if not fadex_1vez:

        "De novo esse sonho..."

        "Puta que pariu... Eu sempre acordo cansado quando eu sonho com isso aqui."

        "..."

        mc desconfiado "Ué? Cadê a fada?"

        show black with dissolve

        "Garota" "{size=10}No meio da floresta...{/size}"

        hide black with dissolve

        mc angustiado "..."

        "Isso de novo?"

        "Essa voz... Será que eu devia escutar ela e dar uma olhada por aí?"

        "Quer saber, foda-se. A [p] não tá aqui agora. É a hora perfeita."

        "Preciso descobrir quem é essa garota que tá me chamando. E ainda por cima desvendar que porra de sonho é esse."

        "..."

        scene fadolandia ponte with Dissolve(1.0)

        "Eu nunca foi além desta ponte. Da outra vez a [p] apareceu e me impediu. Só que agora ela não tá aqui."

        mc concentrando "Força, [mc]."

        "..."

        scene black with Dissolve(1.0)

        "Vou cruzar a ponte, passar por entre as árvores e..."

        mc surpreso "!"





        mc "Uou! Olha o tamanho desse lugar!"

        mc "Será que meu sonho é desse tamanho?!"

        mc concentrando "Maluco, bateu até uma ansiedade agora."

        "Não faço a mínima ideia por onde começar a procurar. Será que eu realmente devo me enfiar no meio disso tudo?"

        "Da outra vez a [p] não gostou de eu andar por aí..."

        mc preocupado "Não quero nem saber o que ela vai fazer comigo se ela descobrir."

        $ fadex_1vez = True



    $ renpy.choice_for_skipping()

    call checa_logado from _call_checa_logado

    "Parece que a [p] não está acordada agora. É a hora perfeita pra eu saber mais sobre este lugar."

    call anuncio from _call_anuncio_1

    "Este sonho parece um labirinto. Preciso encontrar o caminho correto."

    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    label checa_fadolandia:

        "..."

    python:
        if renpy.android:
            fadolandia_db = PythonSDLActivity.pegaFadolandia()
            fadolandia_soma = fadolandia + 1

    if fadolandia_soma < fadolandia_db:

        "{b}Você já esperou para explorar Fadolândia [fadolandia_db] vezes. Mas neste gameplay você explorou [fadolandia] vezes.{/b}"

        "{b}Como não é preciso esperar duas vezes pelo mesmo evento, você pode continuar a história sem esperar novamente.{/b}"

        $ fadolandia += 1

        python:
            if renpy.android:
                renpy.block_rollback()

        if fado_type == "pixel":

            jump fadolandia_m1a1
        else:


            jump pixie_historia

    call checa_tempo from _call_checa_tempo_1

    python:
        if renpy.android:
            ftempo = PythonSDLActivity.checkFtempoNext()
        else:
            ftempo = True

    if not ftempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        mc concentrando "O problema é que eu ainda tô muito cansado."

        "Preciso descansar mais minha mente antes de continuar me aventurando pelo meu sonho."

        mc desculpa "Melhor eu acordar e voltar depois."

        scene black with Dissolve(1.0)

        "{b}[mc] pode explorar Fadolândia uma vez a cada 3 horas do mundo real{/b}"

        "{b}Use o app Relógio no celular do [mc] para ver quando a próxima exploração estará disponível{/b}"

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        "{b}Ou você pode liberar a próxima exploração agora mesmo usando Celebrity Coins{/b}"

        if persistent.coins >= 200:

            "{b}Liberar a próxima exploração usará 200 Celebrity Coins{/b}"

            menu:
                "Liberar exploração":


                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaFTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    "{b}Você usou 200 Celebrity Coins para liberar a próxima exploração{/b}"

                    "{b}[mc] será levado ao começo do sonho e você poderá continuar sua exploração de Fadolândia{/b}"

                    $ renpy.block_rollback()

                    scene fadolandia geral with Dissolve(1.0)

                    jump checa_fadolandia
                "Agora não. Vou esperar o tempo.":


                    "{b}Você escolheu não liberar a próxima exploração{/b}"

                    return
        else:


            "{b}Você precisa de ao menos 200 Celebrity Coins para liberar a exploração{/b}"

            "{b}Você pode comprar Celebrity Coins com dinheiro do {b}seu{/b} mundo.{/b}"

            "{b}Assim você pode continuar a história agora mesmo e ainda colabora com o desenvolvimento de CH.{/b}"

            menu:
                "Ok. Quero comprar.":


                    "..."

                    call comprar_coins from _call_comprar_coins_1

                    "{b}O [mc] será mandado de volta no tempo para que você possa continuar jogando.{/b}"

                    hide black with dissolve

                    scene fadolandia geral with Dissolve(1.0)

                    jump checa_fadolandia
                "A vida é dura. Tô sem grana pra isso agora.":


                    "Não tem problema."

                    "{b}Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais.{/b}"

                    return

    python:
        if renpy.android:
            renpy.block_rollback()

    "Não posso desistir. Tenho que descobrir tudo sobre este sonho."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("pixie_exploracao","pixie","personagem")

    python:
        if renpy.android:
            PythonSDLActivity.setFtempoNext()
            fadolandia += 1
            renpy.block_rollback()

    if fado_type == "pixel":

        jump fadolandia_m1a1
    else:


        jump pixie_historia

label fadex_menu:

    menu:

        "Visitar a {b}caverna{/b}" if fadex_caverna:

            scene black with Dissolve(1.0)

            "..."















        "Visitar a {b}fonte{/b}" if fadex_fonte:

            scene black with Dissolve(1.0)

            "..."
        "Encontrar novos caminhos na floresta":




            pass
        "Acordar":




            "Não tô com saco pra me aventurar no meio desse mato agora."

            mc zerado "Outra hora eu volto."

            scene black with Dissolve(1.0)

            return

label fadex_caminho:

    menu:
        "Seguir o caminho da esquerda":


            pass



        "Seguir o caminho do meio" if not fadex_c1:

            $ fadex_c1 = True

            jump fadex_errou
        "Seguir o caminho da direita":


            pass




label fadex_errou:

    $ renpy.vibrate(1)

    scene black with Dissolve(0.2)

    show pixie barreira at animacao_pixie

    python:
        if renpy.android:
            renpy.block_rollback()

    "QUE MERDA FOI ESSA?!"

    "Que susto..."

    "O que foi isso? Um pesadelo?"

    "{b}Você pode andar pelo labirinto dos sonhos uma vez a cada 3 horas{/b}"

    "{b}O que será que o [mc] encontrará lá?{/b}"

    python:
        if renpy.android:
            renpy.block_rollback()

    return

label cave_minigame_inicio:

    scene caverna geral_antes with Dissolve(1.0)

    mc "Estou de volta, [f]."

    scene mapa5_pixel_feliz with Dissolve(1.0)

    pause

    f "Oi, [mc]. Pronto para descobrir o segredo da gruta?"

    mc "Com certeza. Pode contar comigo."

    f "Assim que se fala. Vou deixar você tomar a dianteira e qualquer coisa me fala, tá?"

    mc "Pode deixar."

    jump cave_minigame

label cave_minigame:

    scene caverna geral_antes with Dissolve(1.0)

    "Preciso colocar as pedras negras na ordem correta. É a única forma de descobrirmos de onde está vindo todo o poder."

    menu:
        "Tentar colocar as pedras na ordem correta":


            "As letras engravadas são dois {b}T{/b}, um {b}S{/b}, dois {b}E{/b}, um {b}G{/b}, um {b}Z{/b} e dois {b}I{/b}."

            "{b}Escreva a palavra de 9 letras formada quando as pedras são colocadas na ordem correta.{/b}"

            call screen zeit_screen






            if cave_resposta == "zeitgeist":

                jump cave_minigame_final
            else:


                "..."

                "..."

                "..."

                mc "Não aconteceu nada..."

                scene mapa5_pixel_triste with Dissolve(1.0)

                f "Parece que não era a ordem certa..."

                mc "Não se preocupe. Vamos encontrar a resposta."

                scene mapa5_pixel_feliz with Dissolve(1.0)

                f "Confio em você, [mc]!"

                jump cave_minigame
        "Investigar a gruta":


            "Para descobrir a ordem correta, tenho que prestar muita atenção nas mensagens reveladas pelos artefatos naturais espalhados pela gruta."

            "..."

            jump cave_mini_area1
        "Falar com a [f]":


            mc "[f]."

            scene mapa5_pixel_feliz with Dissolve(1.0)

            f "O que foi, [mc]?"

            mc "Você pode me explicar novamente o que a gente precisa fazer?"

            f "Claro."

            f "Existe uma força muito poderosa nesta gruta. E a gente precisa descobrir de onde esse poder está vindo."

            f "Eu acho que para revelarmos a identidade do foco de energia, a gente precisa colocar as pedras negras na ordem correta."

            f "São 9 pedras que quando colocadas na ordem certa devem formar uma palavra mágica que vai revelar o segredo."

            f "Os artefatos naturais que estão espalhados pela gruta devem ter algo a ver com tudo isso."

            f "Ah! Artefatos naturais são essas pedras e plantas que estão brilhando pois foram imbuídos com magia."

            f "Você tem o poder de sintonizar sua energia com os artefatos. Algo que nem eu posso fazer."

            mc "Quando eu sintonizo com os artefatos, uma imagem específica vem na minha cabeça."

            f "Exatamete! E esses pedaços de informação devem ser a chave para decifrarmos esse enigma."

            mc "Ok. Entendi. Tenho certeza que vamos conseguir."

            f "Se precisar que eu te explique novamente, só falar comigo."

            mc "Valeu."

            jump cave_minigame
        "Acordar":


            label cave_minigame_esgotado:

                mc "[f]. Não estou conseguindo resolver isso agora."

                mc "Vou acordar e depois podemos continuar."

                scene mapa5_pixel_feliz with Dissolve(1.0)

                f "Eu sinto que estamos cada vez mais perto de resolver esse enigma."

                f "Vou ficar te esperando, irmãozão."

                mc "Logo eu volto."

                f "Beijinho."

                $ cave_mini_energia = 0

                return

label cave_mini_area1:

    scene cave um with Dissolve(1.0)

    pause

    "Este é o ponto inicial. Posso continuar andando ou sintonizar com o artefato desta área."

    menu:
        "Sintonizar com o artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    f "O que é?!"

                    mc "Eu vejo uma imagem... lugares... monumentos..."

                    mc "As {b}sete maravilhas do mundo{/b} formam um c{b}í{/b}rculo e sobrevoam m{b}i{/b}nha cabeça. Sobre m{b}i{/b}m, elas rodop{b}i{/b}am em sua majestade."

                    f "Como?"

                    mc "Não sei o que isso significa."

                    f "As sete maravilhas do mundo?"

                    mc "Tinha uma pirâmide, uma construção que parecia da Grécia, um jardim alagado..."

                    f "Interessante... temos que entender como isso nos ajuda com as pedras, pois com certeza existe algo aí para nós."

                    mc "Verdade... Eu sei que {b}uma letra específica{/b} aparecia em destaque. E nessa frase tinha um número também."

                    f "O que isso quer dizer?"

                    mc "Não sei... ainda é muito cedo."

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area1
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintoniar agora."

                    jump cave_mini_area1
        "Ir para a próxima área":


            "..."

            jump cave_mini_area2
        "Ir para a área anterior":


            "..."

            jump cave_mini_area6
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_area2:

    scene cave dois with Dissolve(1.0)

    pause

    "Aqui fica a segunda área. Aqui existem dois artefatos naturais que eu posso sintonizar."

    menu:
        "Sintonizar com o {b}primeiro{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    f "O que esse artefato diz?"

                    mc "Os {b}cinco rios do submundo{/b} são o caminho que minha alma cruza para che{b}g{/b}ar ao seu destino final."

                    mc "Eu vejo a morada de Hades, o Deus da Morte. E lá está ele a {b}g{/b}ar{b}g{/b}alhar enquanto as almas {b}g{/b}ritam aflitas."

                    f "Uou... isso parece terrível, maninho..."

                    mc "A visão com certeza me deu um baita calafrio."

                    mc "O que isso pode ter a ver com a ordem das pedras?"

                    f "Não sei... mas precisamos analisar os detalhes. Eu tenho certeza que essas visões são a resposta."

                    mc "Uma das letras estava destacada."

                    f "Qual letra era?"

                    mc "Não lembro agora, mas da próxima vez tenho que prestar muita atenção para ver qual letra {b}aparece em destaque{/b}"

                    mc "E também apareceu um número."

                    f "Então sempre aparece uma letra em destaque e um número..."

                    mc "Isso."

                    mc "Certo! Vamos conseguir."

                    f "Com certeza!"

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area2
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area2
        "Sintonizar com o {b}segundo{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    "Tenho que prestar atenção no número e na letra que aparece em destaque."

                    f "O que o artefato está te falando?"

                    mc "Um dragão... terrível, imenso..."

                    mc "O {b}primeiro dragão{/b} ja{b}z{/b} imóvel e cerra os dentes quando me manda procurar a maga Muriel."

                    f "M-maga Muriel?!"

                    mc "Isso quer te dizer alguma coisa?"

                    f "Não..."

                    mc "..."

                    mc "Essa visão não quer me dizer nada..."

                    f "Temos que pensar com calma. Eu estou certa que essas visões são a resposta para resolver o enigma das pedras negras."

                    "Qual foi o número que apareceu e qual a letra que tava em destaque mesmo? Se eu pudesse anotar..."

                    mc "Ok. Vamos chegar lá."

                    f "Sim!"

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area2
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area2
        "Ir para a próxima área":


            "..."

            jump cave_mini_area3
        "Ir para a área anterior":


            "..."

            jump cave_mini_area1
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_area3:

    scene cave tres with Dissolve(1.0)

    pause

    "Chegamos na terceira área da gruta. Aqui também tem dois artefatos naturais."

    menu:
        "Sintonizar com o {b}primeiro{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    f "O artefato tá brilhando enquanto você se concentra..."

                    mc "A imagem tá aparecendo..."

                    f "Não esquece de ver o número e a letra que aparecem em destaque."

                    mc "Ok."

                    mc "Os {b}oito sub-príncipes do inferno{/b} e{b}s{/b}tão reunido{b}s{/b}. Ele{b}s{/b} comandam dezena{b}s{/b} de legiõe{b}s{/b} de demônio{b}s{/b} que obedecem cegamente {b}s{/b}ua{b}s{/b} orden{b}s{/b}."

                    f "Sub-pri... do inferno...?"

                    mc "Não olhe com essa cara pra mim. Só estou falando a mensagem da visão."

                    f "Credo..."

                    mc "..."

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area3
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area3
        "Sintonizar com o {b}segundo{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    f "Tudo bem, [mc]? O que você está vendo?"

                    mc "Construções altas... uma ao lado da outra, subindo até as nuvens..."

                    mc "As {b}duas torres{/b} {b}e{/b}ram o símbolo d{b}e{/b} sua supr{b}e{/b}macia. A {b}e{/b}ntrada para o reino n{b}e{/b}gro {b}e{/b} as par{b}e{/b}d{b}e{/b}s d{b}e{/b} mármor{b}e{/b} branco."

                    f "Hmm... torres... que construções são essas? Do que o artefato está falando?"

                    mc "Não faço a mínima ideia. Não consigo lembrar de nenhuma torre de mármore..."

                    f "Tudo isso é muito estranho, [mc]..."

                    mc "Sim. Vamos pensar com calma."

                    mc "A letra destacada nessa era bem fácil de ver. Ela apareceu várias vezes."

                    f "E o número era DOIS, né?"

                    mc "Sim, eram DUAS TORRES, então o número é dois."

                    f "Talvez queira dizer que a letra em destaque é a SEGUNDA na ordem!"

                    mc "Pode ser! Muito bem, [f]!"

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area3
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area3
        "Ir para a próxima área":


            "..."

            jump cave_mini_area4
        "Ir para a área anterior":


            "..."

            jump cave_mini_area2
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_area4:

    scene cave quatro with Dissolve(1.0)

    pause

    "A quarta região da gruta... Estamos quase no final do caminho. E aqui tem mais um artefato natural."

    menu:
        "Sintonizar com o artefato":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena está se formando na minha cabeça..."

                    "Tenho que anotar a letra que aparecer destaque e o número que aparece na mensagem."

                    "A [f] acha que o número que eu ver é justamente a ordem em que a letra em destaque aparece."

                    f "O artefato está mostrando alguma coisa?"

                    mc "Leste, oeste, norte e sul..."

                    f "Ah?"

                    mc "Os {b}quatro ventos{/b} sopram para {b}t{/b}odas as direções. Dirigidos por Éolo, a paz e a des{b}t{/b}ruição eles carregam pelo mundo."

                    f "Quatro ventos... o que é isso, [mc]?"

                    mc "Pelo que eu vi, são quatro... pessoas... talvez?"

                    f "Pessoas?"

                    mc "Não sei se podemos chamar de pessoas. Mas eram como pessoas."

                    f "Muito interessante..."

                    mc "Espero que a gente consiga usar essa informação de alguma forma."

                    f "Com certeza. Então o número aqui era QUATRO. E a letra em destaque era?"

                    mc "Não lembro..."

                    f "Se concentre [mc]!"

                    mc "Desculpa! Vou prestar atenção na próxima."

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area4
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area4
        "Ir para a próxima área":


            "..."

            jump cave_mini_area5
        "Ir para a área anterior":


            "..."

            jump cave_mini_area3
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_area5:

    scene cave cinco with Dissolve(1.0)

    pause

    "O penúltimo lugar. Tem mais um artefato aqui. Espero que as informações sejam revelantes."

    menu:
        "Sintonizar com o artefato":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena tá se formando na minha cabeça..."

                    f "O que será desta vez... Estou ansiosa..."

                    mc "As {b}três bruxas{/b} observam a l{b}i{/b}nha com o dest{b}i{/b}no do re{b}i{/b}. Ao seu tr{b}i{/b}ste f{b}i{/b}m elas o levam. Para elas, não passa de ma{b}i{/b}s um."

                    f "Bruxas! Três?!"

                    mc "Será que ele tá falando da bruxa que você mencionou?!"

                    f "Só pode ser! E são três!"

                    mc "Como isso?"

                    f "Não sei, [mc]... mas eu acho que isso é realmente importante."

                    mc "Eu também. Vou pensar sobre isso com calma."

                    mc "Olha... desta vez eu lembro. A letra em destaque era {b}i{/b}."

                    f "'i' de índio?"

                    mc "Isso mesmo."

                    f "E o número era o TRÊS."

                    mc "Certo."

                    f "Então a terceira letra que temos que formar na palavra é a letra 'i'."

                    mc "Eu também acho isso."

                    f "Então agora é só a gente fazer o mesmo processo com todas."

                    mc "Pode deixar."

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area4
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area4
        "Ir para a próxima área":


            "..."

            jump cave_mini_area6
        "Ir para a área anterior":


            "..."

            jump cave_mini_area4
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_area6:

    scene cave seis with Dissolve(1.0)

    pause

    "Esta é a última área. Aqui acaba a gruta e existem dois artefatos naturais que eu posso sintonizar."

    menu:
        "Sintonizar com o {b}primeiro{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena tá se formando na minha cabeça..."

                    f "Tomara que seja algo simples de entender..."

                    mc "É toda uma terra... uma grande região."

                    mc "Os {b}nove reinos{/b}, cada um com sua {b}t{/b}erra, cada um com seu povo. {b}T{/b}odos esperam o momen{b}t{/b}o da grande guerra."

                    mc "Só isso..."

                    f "Nove reinos? Provavelmente ele não tá falando de Fadolândia. Aqui não tem nove reinos. Eu acho..."

                    mc "A Terra tem muito mais do que nove reinos."

                    f "De onde ele tá falando então?"

                    mc "Não faço a mínima ideia..."

                    f "Vamos tentar pensar um pouco e vamos entender."

                    mc "Sim!"

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area6
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area6
        "Sintonizar com o {b}segundo{/b} artefato.":


            "Eu gasto energia toda vez que eu sintonizo com um artefato natural. Após sintonizar com 3 artefatos, preciso acordar."

            menu:
                "Sintonizar":


                    $ renpy.block_rollback()

                    show white with Dissolve (0.3)

                    scene mapa5_pixel_cristal

                    show white

                    hide white with dissolve

                    "A cena tá se formando na minha cabeça..."

                    f "Força, irmãozão!"

                    mc "Uma estrela!"

                    f "Estrela?"

                    mc "As {b}seis pontas{/b} da {b}e{/b}str{b}e{/b}la r{b}e{/b}pr{b}e{/b}s{b}e{/b}ntam a luta do b{b}e{/b}m contra o mal, do físico contra o {b}e{/b}spiritual."

                    f "Uma estrela de seis pontas..."

                    mc "Exatamente isso. O que será isso?"

                    f "Não faço a mínima ideia."

                    mc "..."

                    f "Mas vamos pensar um pouco e juntar todas as informações que temos até agora."

                    mc "Isso. E qualquer coisa posso sintonizar novamente com os artefatos que a gente achar importante."

                    f "Isso ajudaria bastante, [mc]."

                    mc "Vamos nessa."

                    $ cave_mini_energia += 1

                    if cave_mini_energia >= 3:

                        jump cave_mini_cansado
                    else:


                        "Ufa... mesmo após ter sintonizado com este artefato, ainda tenho energia para continuar por aqui."

                        "Tenho que aproveitar e descobrir o máximo que eu puder."

                        jump cave_mini_area6
                "Melhor não gastar minha energia.":


                    "Vou poupar minha energia. Não vou sintonizar agora."

                    jump cave_mini_area6
        "Voltar para a primeira área":


            "..."

            jump cave_mini_area1
        "Ir para a área anterior":


            "..."

            jump cave_mini_area5
        "Voltar para o centro da gruta":


            "Deixa eu parar um pouco e pensar."

            jump cave_minigame

label cave_mini_cansado:

    scene caverna geral_antes with Dissolve(1.0)

    mc "Puxa, [f]... depois desse último artefato eu realmente tô cansado..."

    scene mapa5_pixel_feliz with Dissolve(1.0)

    f "Não esquente, [mc]. Você fez um excelente trabalho hoje."

    f "Descanse e volte o quanto antes pra gente continuar."

    mc "Pode ter certeza que eu vou voltar."

    f "Vou estar te esperando, irmãozão."

    mc "Até depois, maninha."

    f "Beijinho."

    $ cave_mini_energia = 0

    return

label cave_minigame_final:

    scene black at cena_chacoalhando with Dissolve(3.0)

    "{i}Drrrrrrrrrrrrr{/i}"

    mc "O que tá acontecendo?!"

    f "Eu não sei!"

    f "Fizemos alguma coisa terrível, [mc]!"

    mc "Mas... mas-"

    f "Alí!"

    mc "!!!"

    scene mapa5_enki at cena_chacoalhando with Dissolve(5.0)

    mc "AAAHHHH!"

    f "Está tudo tremendo!"

    mc "Que porra gigante é essa?!"

    f "O foco! Esse é o foco do poder!"

    mc "Não me diga!"

    mc "E agora?!"

    f "..."

    mc "[f]!"

    f "Eu não sei!"

    mc "Tamo fodido! Já morremo já morremo! Deus!!"

    "Som Gutural" "Uuoooooo...."

    mc "E agora que merda é essa?!"

    f "Está vindo da coisa!"

    mc "Eu sei [f]!"

    mc "O que isso quer dizer?!"

    f "Eu estou ficando zonza!"

    mc "Por favor não nos mate! Somos da paz!"

    "Som Gutural" "UUOOOOHHH!"

    mc "Nããããoooo!!!"

    scene black at cena_chacoalhando with Dissolve(3.0)

    scene black with Dissolve(2.0)

    scene mapa5_enki with Dissolve(2.0)

    "..."

    "{i}Tsssss{/i}"

    mc "Acabou? Aqui é o céu?"

    f "Recomponha-se, [mc]! Não aconteceu nada."

    mc "Como nada?"

    "Som Gutural" "Criaturas..."

    f "Senhor! Eu sinto sua energia e não quero lhe causar mal."

    mc "Eu também isso que ela disse!"

    "Som Gutural" "Eu ouço suas vozes. Eu vejo suas almas..."

    "Som Gutural" "Vocês não são bons, ou justos, ou confiáveis..."

    mc "..."

    f "..."

    "Som Gutural" "E não são o mal também."

    "Som Gutural" "Vocês podem não ver, mas eu lhes vejo o âmago, o íntimo, a verdade escondida pelo medo e pelo desejo."

    f "..."

    mc "Isso quer dizer que você vai nos matar?"

    "Som Gutural" "Não há o que temer, jovem... Ninguém há de morrer aqui hoje."

    mc "..."

    "Som Gutural" "Vocês conjuraram magia ancestral ao ordenar de forma adequada as {b}runas negras{/b}."

    "Som Gutural" "O poder dos sumérios tornou-se vosso poder hoje e a minha presença é requisitada."

    "Som Gutural" "Ei de fazer-lhes acompanhantes de minha presença e minha sabedoria."

    "Som Gutural" "..."

    "..."

    "Acho que agora eu tenho que falar alguma coisa..."

    mc "{size=15}O que eu falo, [f]?{/size}"

    f "{size=15}Não tenho ideia...{/size}"

    "Som Gutural" "..."

    mc "É..."

    menu:
        "Você vai responder nossas perguntas? É isso?":


            mc "Você disse algo sobre sabedoria. Você vai responder nossas perguntas?"

            "Som Gutural" "A depender das perguntas..."

            mc "..."
        "Desculpe, mas não quero te incomodar.":


            mc "Não sei o que falar senhor. A verdade é que eu tô com medo de desagradar você."

            "Som Gutural" "Não há o que temer, filhos."

    mc "Ce-certo... você poderia falar quem é você?"

    "Som Gutural" "Não QUEM, porém O QUÊ, seria o mais adequado."

    "Som Gutural" "Eu sou um {b}Protetor dos Sumérios{/b}, batizado por centenas de nomes no decorrer dos séculos."

    "Som Gutural" "Talvez vocês me conheçam como {b}AYA{/b} ou {b}EA{/b}. Mas os sumérios tinham outro nome para mim."

    mc "Eu... {i}ARGH{/i}"

    f "O que foi, [mc]?!"

    mc "Nada... só tô meio tonto..."

    "Som Gutural" "Não há razão para impaciência. Estarei aqui quando voltarem."

    f "Acho que é melhor você ir, irmãozão..."

    mc "Mas..."

    f "Você ouviu. Não precisa se apressar."

    mc "Ok. Até depois, [f]."

    mc "Logo eu volto..."

    show black with dissolve

    $ pixel_evento += 1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
