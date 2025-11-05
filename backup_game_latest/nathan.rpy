label nathan_evento1:

    $ nathan_evento = False

    "Pelo horário, se a [j] falou a verdade, ele pode estar por aqui agora."

    "..."

    scene pub dois with dissolve

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você deve ajudar quem não tem coragem de puxar o gatilho. Você não é um medroso, certo?"

        p "O segredo é... o que você vai fazer com a pauta? Entregar ou guardar para você? Tudo vai mudar com sua escolha!"



    "..."

    "???" "Calma, garotas..."

    mc surpreso "!"

    scene pub booth with dissolve

    python:
        renpy.save("n1_save", extra_info="n1_save")
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")

    $ iconchefe += 1

    "Garota 1" "Mas é sério, [n]! Porque nenhum dos caras que me chama pra sair é malhado igual você?"

    n "Quê? Isso é o de menos, não acha?"

    "Garota 2" "Você fala isso porque você tem um corpão..."

    n "..."

    "Garota 1" "Qualquer garota ia querer pegar você, [n]..."

    n "Isso não é verdade. Mas obrigado."

    "Por que eu tenho a impressão que ele não tá aproveitando?"

    "Normalmente um homem nessa situação estaria muito mais animado..."

    "Bom... Eu preciso me aproximar dele. Não quero acabar com o clima e embaçar o esquema, mas realmente parece que ele não está à vontade."

    "Pode ser a chance que eu precisava."

    "Vou me sentar do lado deles e ver o que acontece."




    mc normal "Boa noite, [n], garotas."



    scene black with dissolve

    scene n1_new1 with Dissolve(1.0)

    pause

    "Uou! As garotas estão caindo em cima dele..."

    menu:
        "Será que cabe mais um fã neste banco?":


            mc normal "Será que cabe mais um fã neste banco?"

            "Garotas" "..."

            n "Se for você, cabe sim."
        "Duas? Você nunca ouviu falar em repartir o pão?":


            $ nathan_garotas += 2

            mc tarado "Duas? Você nunca ouviu falar sobre um tal de Jesus? Ele disse algo sobre repartir o pão."

            "Garotas" "..."

            n "..."
        "Parece que você precisa de um ajudante...":


            $ nathan_garotas += 1

            mc desculpa "Parece que você pode usar um ajudante..."

            "Garotas" "..."

            n "E você conhece alguém?"

            mc charmoso "Eu acabei de chegar no bar e eu realmente tô me sentindo autruísta hoje."

            n "Quanta sorte a minha."

    "Garota 2" "E quem é esse, [n]?"

    n "..."

    mc desculpa "Ah. Perdão."

    mc normal "Meu nome é [mc]. Eu sou um jornalista que acompanha o trabalho do [n]."

    n "Ah... A [j] me falou sobre você. Ela disse que você provavelmente apareceria no bar hoje."

    n "Ela te mandou pra ajudar ela com a reportagem? Fazer o que ela não conseguiu?"

    menu:
        "Exatamente.":


            $ nathan_cassia = True

            mc normal "Você acertou, não tenho como negar. Ela achou que talvez eu tivesse mais sorte do que ela."

            n "..."

            mc desculpa "Mas não é como se a gente fosse amiguinhos."

            mc "A [j] está me chantageando. Ela tem informações sobre uma amiga..."

            n "Entendo... Isso é uma merda, amigo."
        "A [j] me tem na mão dela, infelizmente...":


            $ nathan_cassia = True

            mc incomodado "A [j] está me chantageando. Ela tem informações sobre uma amiga e disse que vai publicar na revista, mesmo sendo mentira..."

            n "Eu conversei algumas vezes com ela, e realmente é algo que ela faria."

            mc desculpa "Pois é..."
        "Ela não tem nada a ver com isso. Eu sempre venho aqui.":


            mc bravo "Ela trabalha na mesma revista que eu, mas não tem nada a ver com ela."

            mc desculpa "Eu venho bastante aqui. Inclusive encontrei a [cc] outro dia."

            n "Me desculpe. Não queria te acusar."

            mc normal "Tudo bem. Eu posso entender..."

    "Garota 1" "{i}Cof cof{/i}"

    n "Ah... Essas duas garotas lindas são Ana e Maria."

    n "A gente tava conversando sobre... Alguma coisa..."

    menu:
        "Você são lindas mesmo. Muito prazer...":


            $ nathan_garotas += 2

            mc safado "Lindas mesmo... O prazer é todo meu, garotas."

            "Garotas" "..."
        "Prazer em conhecer vocês.":


            $ nathan_garotas += 1

            mc normal "Legal. Prazer em conhecer vocês."

            "Garotas" "..."
        "Certo...":


            mc incomodado "Ok."

            "Garotas" "..."

    "Garota 2" "[n], a gente vai no banheiro. Pode conversar aí. A gente volta logo."

    n "Tudo bem, meninas. Não demorem tanto."

    "Garota 1" "Pode deixar."

    "..."

    scene black with dissolve

    scene pub banco with dissolve

    mc desconfiado "Parece que elas não foram com a minha cara."




    scene black with dissolve

    scene n1_new2 with Dissolve(1.0)

    pause

    n "Não se preocupe. Não é nada pessoal. Elas só queriam passar um tempo com o [nc] e você está atrapalhando."

    mc desculpa "Eu não queria embaçar seu esquema."

    n "Não esquente. Pra falar a verdade, eu nem tava curtindo tanto assim."

    mc incomodado "É... percebi. Eu achei que você tava meio desanimado..."

    n "Sua percepção é boa. As duas ali parecem não ter notado nada."

    mc normal "Elas pareciam tipo hipnotizadas... Sem ironia, deve ser bom ser você."

    n "Existe a parte boa, claro. Mas também tem o seus problemas..."

    mc "..."







    n "Não vamos acabar com o clima falando de besteira."

    n "Olha. Eu tenho uma proposta pra você."

    mc desconfiado "Proposta?"

    if nathan_garotas > 2:

        n "Sim. Você obviamente se interessou pelas garotas."
    else:


        n "Sim. Sabe as garotas?"

    n "O nome da loira é Ana e a outra é Maria. Eu conheci as duas faz uma meia hora."




    n "Eu tava planejando passar a noite conversando com elas, mas o que acha da gente repartir o pão?"

    mc desconfiado "O que quer dizer com isso?"

    n "Exatamente o que você está pensando. O que acha de escolher uma delas?"

    n "Eu te ajudo te apresentando uma delas. E assim eu posso ficar mais tranquilo com a outra."

    mc safado "Parece uma proposta irrecusável..."

    mc desculpa "Mas não sei se elas aceitariam..."




    n "Não se preocupe com isso. Confie em mim. Só me diga qual delas você gostou mais."

    menu:
        "Gostei mais da loira, Ana.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("nathan_garota_loira","inicio","local")

            $ nge = "Ana"

            mc safado "A Ana com certeza."

            n "Então tá decidido. Só relaxe e deixe comigo."

            jump nathan_garotas
        "Maria, a morena, me chamou mais a atenção.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("nathan_garota_morena","inicio","local")

            $ nge = "Maria"

            mc safado "A morena, Maria, né? Me chamou mais a atenção."

            n "Está decidido. Só relaxe e deixe comigo."

            jump nathan_garotas
        "Nenhuma. Acho que eu prefiro só conversar com você.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("nathan_garotas_negou","inicio","local")

            mc desculpa "Na verdade, acho que não tô no clima pra garotas."

            mc normal "Queria aproveitar que encontrei você aqui e trocar uma ideia contigo."

            if nathan_cassia:

                mc desculpa "Juro que não é só por causa da [j]."

            n "Isso é um pouco inesperado."

            n "Você tem certeza que não quer se dar bem com uma delas?"

            menu:
                "Tenho.":


                    $ nathan_amizade += 3

                    mc normal "Sim. Não é que eu não goste de garotas, é só que não tô afim agora."

                    n "Eu entendo perfeitamente. Eu tô na mesma vibe. Vamos dispensar elas."

                    jump nathan_sem_garotas
                "Pensando bem...":


                    mc tarado "Pensando bem... Acho que seria um pecado deixar passar essa chance."

                    n "Perfeito! E qual delas você escolhe?"

                    menu:
                        "A loira, Ana.":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("nathan_garota_loira","inicio","local")

                            $ nge = "Ana"
                        "Maria, a morena.":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("nathan_garota_morena","inicio","local")

                            $ nge = "Maria"

                    n "Assim que se fala. Pode deixar comigo."

                    jump nathan_garotas

    label nathan_garotas:

        mc desconfiado "Mas por que você tá fazendo isso?"




        n "Como assim? Um brother não pode ajudar o outro?"

        mc "..."

        mc "É..."

        n "Pare de pensar besteira e se ajeite, elas estão voltando."




        mc "..."

        "Primeiro, por que ele faria isso por mim?"

        "E segundo, as garotas me odeiam por estragar o lance delas com um modelo. Por que elas dariam bola pra mim?"

        "Que merda..."

        "..."

        "Maria" "Estamos de volta! Deixa eu sentar do seu lado, [n]."




        "Maria" "Vem aqui, Ana."

        "..."










        scene black with dissolve

        scene n1_new3 with Dissolve(1.0)

        pause

        "Ana" "Ainda estão conversando?"




        n "Mais ou menos. O [mc] estava me falando que conhecer muitos famosos às vezes é complicado."




        "Ana" "Muitos famosos? Como assim?"

        n "Ele é paparazzo. Ele conhece vários famosos, e daí as pessoas ficam pedindo favores pra ele."

        n "E o pior é que ele acaba aceitando e leva o pessoal que quer conhecer, ou autógrafo esse tipo de coisa."

        "Garotas" "Hmmm..."

        n "Não é, [mc]?"

        "Será que a [j] contou meu nome pra ele? De que outro jeito ele saberia?"

        n "[mc]?"

        mc surpreso "Ah! É sim!"

        mc charmoso "Eu conheço MUITOS famosos. São muitos anos de amizade, né? E me pedem favores. Eu sou coração mole."

        "Ana" "Puxa..."

        "Maria" "Muito legal você fazer isso."

        mc desculpa "Não é nada de mais..."

        n "Ele é humilde, isso sim. Mas isso nem é o mais incrível."

        n "Como ele manda e desmanda na revista, o [mc] acaba lançando vários artistas no cenário."

        n "Eu mesmo. Se eu cheguei onde tô hoje, e olha que eu tô começando ainda, foi graças a ele."

        "Garotas e [mc]" "Sério?!"

        n "Como assim, [mc]? Não lembra?"

        mc charmoso "Ah! Claro que eu lembro. Aquela reportagem..."

        n "Sim. Aquela reportagem de capa que você obrigou publicarem. Acho que foi a primeira vez que eu apareci."

        n "Muito obrigado mesmo."

        mc desculpa "Você sabe que não foi nada..."

        n "Inclusive, você me disse que tá procurando uma nova modelo, né? Pra capa da revista da semana..."

        mc desconfiado "Nova modelo?"

        n "Sim! Uma garota pra aparecer na capa da revista da semana! NÃO É?!"

        mc charmoso "Claro! Realmente. Não consegui encontrar até o momento uma garota que se encaixe..."

        n "Era sobre isso que a gente tava conversando antes de vocês chegarem."

        if nge == "Ana":

            n "O [mc] estava me dizendo como você, Ana, se encaixa perfeitamente no perfil que ele está procurando."

            "Ana" "Verdade?!"

            n "..."

            mc charmoso "Exatamente, Ana. O que acha?"

            "Ana" "Nossa... Seria uma grande oportunidade, né?"

            n "Com certeza. Ana, por que você não vai ali e vocês conversar melhor?"

            "Ana" "Claro!"

            "Ana" "Deixa eu chegar mais perto, [mc]."

            mc safado "Isso. Vem aqui."







            scene black with dissolve

            scene pub banco with dissolve

            pause 1.0

            jump nathan_e1_ana

        elif nge == "Maria":

            n "O [mc] estava comentando como a Maria se encaixa perfeitamente no perfil dessa capa."

            ngep "Sério, mesmo?"

            n "..."

            mc charmoso "Verdade, [nge]. Você seria perfeita."

            ngep "Isso é incrível!"

            n "[nge], por que você não senta do lado dele e vocês conversam melhor?"

            ngep "Claro!"







            scene black with dissolve

            scene pub banco with dissolve

            jump nathan_e1_maria

    label nathan_e1_ana:







        scene black with dissolve

        scene n1_new4 with Dissolve(1.0)

        pause

        ngep "Isso é realmente sério?"

        mc charmoso "Claro. Nossa revista tem alcance nacional e encontrar garotas bonitas como você não é fácil."

        ngep "Você realmente me acha linda?"

        menu:
            "Eu gosto dos seus cabelos loiros.":


                mc "Seu cabelo parece tão macio e a cor é incrível."
            "Eu gosto do seu corpo.":


                mc safado "Seu corpo é perfeito e você tem uma aura sexy."
            "Eu gosto do seu estilo.":


                mc "Suas roupas, seu estilo, você realmente sabe se vestir."

        ngep "Não fala assim que você me deixa sem jeito..."

        mc charmoso "É verdade. Eu acompanho muitas garotas e poucas me atraíram igual você."

        ngep "A é?"

        mc "Uma capa com você deixaria qualquer homem excitado."

        ngep "..."

        ngep "Até você?"

        menu:
            "Com certeza.":


                mc safado "Principalmente eu."

                mc "Não tá fácil aguentar sem chegar mais perto de você."

                ngep "Hmm..."
            "Não deixo nada influenciar meu trabalho.":


                mc concentrando "Não posso deixar nada influenciar meu trabalho."

                mc "O que eu acho de uma garota não importa."

                ngep "Entendo..."

        mc charmoso "Mas a escolha da modelo de capa não é apenas aparência."

        mc "Ela precisa ser sexy e precisa saber passar isso na hora do ensaio."

        ngep "Eu posso ser muito sexy. Você quer ver?"

        menu:
            "Me convença...":


                $ nathan_e1_fim_garota = "Ana"

                mc tarado "Quero ver. Me convença..."

                ngep "Com todo o prazer."

                hide ana with dissolve

                "..."
            "Não. Qualquer coisa entro em contato com você.":


                mc normal "O que eu precisava saber de você eu já consegui."

                mc "Foi um prazer, [nge]. Quando tiver uma resposta eu entro em contato com você."

                mc "Pode me passar seu contato?"

                ngep "... Claro. Aqui está."

                mc "Obrigado."

                jump nathan_e1_continua

        "Eu não acredito nisso... Ela está disposta a fazer qualquer coisa."

        ngep "Estou pronta..."



        scene n1_new5 with Dissolve(1.0)

        pause

        ngep "E então? Sou sexy o suficiente pra revista?"

        mc tarado "Deixa eu analisar melhor."

        ngep "O que você acha das minhas pernas?"

        mc safado "Eu acho que você tá mexendo demais comigo. Mas não sei se é o suficiente..."

        ngep "Ver não é o suficiente pra você? Pode pegar."

        mc "..."

        ngep "Isso, passa a mão em mim."

        mc "Sua pele é muito macia."

        ngep "Sim... Pode pegar mais."

        mc "..."

        ngep "Seu teste tá me deixando louca..."

        mc safado "Vem aqui. Deixa eu testar sua boca agora."




        ngep "Tá..."





        scene black with dissolve

        scene n1_new6 with Dissolve(1.0)

        pause

        "..."

        ngep "Hmm... Esse é o melhor teste que já fiz na vida."

        mc "Você está indo muito bem..."

        ngep "Eu sei que eu tô..."

        ngep "Hmmm..."

        ngep "Deu pra me avaliar?"

        menu:
            "Mais um pouco.":


                mc "Ainda não."

                scene n1_new7 with Dissolve(1.0)

                pause

                mc "Eu preciso avaliar mais um pouco..."

                "..."
            "Deu, sim.":


                "..."

                mc "Ok... tá bom."



        scene black with dissolve

        scene n1_new5 with Dissolve(1.0)

        pause

        mc tarado "Eu vou conversar com o pessoal da revista, mas acho que você é perfeita."



        ngep "Que bom..."

        ngep "Eu preciso fazer mais alguma coisa?"

        mc charmoso "Só me passe seu telefone e assim que tudo estiver certo eu falo com você."

        ngep "Obrigada, [mc]. Por essa oportunidade."

        mc "Não esquente."

        ngep "E se você quiser me entrevistar de novo pra alguma outra coisa, eu estou sempre aqui no bar durante a noite."

        ngep "A gente pode testar outras coisas também."

        menu:
            "Pode deixar. Eu estou sempre por aqui.":


                mc charmoso "Eu venho sempre aqui. Vou te procurar com certeza."

                ngep "Vou estar te esperando."
            "Eu estou muito ocupado esses dias...":


                mc desculpa "Eu estou meio ocupado esses dias, então não sei..."

                ngep "Ok..."

        mc normal "Então é isso. Obrigado pela disposição [nge]."

        ngep "Pode sempre contar comigo."

        mc "Ok. Beijos."

        ngep "..."



        scene black with dissolve

        "..."

        jump nathan_e1_continua

    label nathan_e1_maria:







        scene black with dissolve

        scene n1_new8 with Dissolve(1.0)

        pause

        ngep "Eu queria muito poder participar de algo assim."

        ngep "Parece uma grande oportunidade..."

        mc charmoso "Nossa revista tem alcance nacional. É uma excelente oportunidade."

        mc "E você é realmente linda."

        ngep "Tem certeza? Eu me acho tão normal..."

        menu:
            "Você não é normal. Você é fantástica.":


                mc "Não fale besteira. Você é fantástica."

                mc "Desde que eu entrei aqui no bar, eu não consegui parar de olhar pra você."

                ngep "Hmm..."
            "Você tem uma beleza cotidiana. É o que eu estou procurando.":


                mc normal "Você é bonita de uma forma cotidiana."

                mc "É como uma garota do dia-a-dia, só que a mais bonita entre elas."

                ngep "Hmm..."



        ngep "Você tá me deixando envergonhada..."

        mc charmoso "É verdade. Eu acompanho muitas garotas e poucas me atraíram igual você."

        ngep "Você só tá querendo me deixar com vergonha agora..."

        mc "Claro que não. Uma capa sua chamaria a atenção de qualquer homem."

        ngep "..."

        ngep "Essa é sua opinião pessoal?"

        menu:
            "O que eu acho não importa.":


                mc concentrando "Meu gosto pessoal não importa."

                mc "Preciso olhar de uma forma profissional."

                ngep "Entendi..."
            "Com certeza. Você mexeu comigo.":


                mc safado "Com certeza."

                mc "Você tá mexendo muito comigo."

                ngep "Hmm... É bom saber que a gente mexe com alguém."

                mc safado "Você poderia mexer com qualquer homem."

        mc charmoso "Mas isso não resume o trabalho de uma modelo de capa."

        mc "Ela precisa ser sexy e precisa saber passar isso na hora do ensaio."

        ngep "Eu não sei se eu poderia ser sexy..."

        menu:
            "Eu sei que você pode. Eu vou te ajudar.":


                $ nathan_e1_fim_garota = "Maria"

                mc tarado "Claro que você pode. Eu vou te ajudar."

                ngep "Tudo bem... O que eu faço?"



                "..."
            "Eu vou dar mais tempo pra você e voltamos a falar depois...":


                mc desculpa "Infelizmente isso é essencial para o trabalho. Você precisa encontrar sua confiança antes de um ensaio desse tipo."

                ngep "..."

                mc "Foi um prazer, [nge]. Eu vou ver certinho e falar com você depois, tá?"

                mc normal "Pode ser que a coisa ainda aconteça."

                mc "Pode me passar seu contato?"

                ngep "... Tudo bem. Me desculpe..."

                mc incomodado "Não precisa se desculpar. Vamos ver tudo certinho."

                mc "Obrigado."

                jump nathan_e1_continua

        "Essa é minha chance de conseguir o que eu quero... Tenho que fazer diretinho, com confiança."

        mc charmoso "Vou ajeitar você, tudo bem?"

        ngep "Claro..."

        mc "Coloque sua mão aqui. E deite assim no banco com as pernas assim..."

        ngep "Você sabe o que está fazendo..."

        mc "Claro. Cuidar de garotas bonitas iguais a você é meu trabalho."

        ngep "Para..."

        mc "Certo. Só cruza assim... Deixa eu ajeitar seu cabelo também."

        ngep "Hmm..."

        mc "Agora olha pra mim e faz uma expressão assim."

        mc "Pronta?"

        ngep "..."



        scene black with dissolve

        scene n1_new9 with Dissolve(1.0)

        pause

        ngep "E então? Sou sexy o suficiente pra revista?"

        mc safado "Uou... Você está incrível."

        ngep "Sério?"

        mc safado "Sim... Você está me deixando louco..."

        ngep "Você também tá..."

        mc "Deixa eu analisar você melhor."

        ngep "Isso."

        mc "Sua pele é macia..."

        ngep "Hmmm... Sua mão está me deixando arrepiada..."

        mc safado "Você está incrível, mas não sei se é o suficiente..."

        ngep "O que eu faço agora? Faço qualquer coisa pra você..."

        mc "..."

        mc charmoso "Deixa eu ver você mais de perto."

        ngep "Ahh... Tá..."

        mc "Agora vem aqui em cima de mim... Vem aqui..."

        ngep "..."



        mc "..."

        "..."

        scene black with dissolve

        scene n1_new10 with Dissolve(1.0)

        pause





        "..."

        ngep "Hmm... Isso... Faz parte do teste?"

        mc "Você está indo muito bem... Continue assim..."

        ngep "Tá..."

        ngep "Hmmm..."

        "..."



        mc safado "Agora sim... Consegui testar o que eu queria."

        mc tarado "Eu vou conversar com o pessoal da revista, mas acho que você é perfeita."



        scene black with dissolve

        scene n1_new9 with Dissolve(1.0)

        pause

        ngep "Tá... Eu... Eu gostei muito do seu teste..."

        mc safado "Você foi muito bem mesmo."

        ngep "E agora? Eu preciso fazer mais alguma coisa?"

        mc charmoso "Só me passe seu telefone e assim que tudo estiver certo eu falo com você."

        ngep "Ok, [mc]. Obrigada por essa oportunidade."

        mc "Não se preocupe."

        ngep "E se você precisar de mais alguma coisa, eu estou sempre aqui no bar durante a noite."

        menu:
            "Pode deixar. Eu estou sempre por aqui.":


                mc charmoso "Eu venho sempre aqui. Vou te procurar com certeza."

                ngep "Que bom..."
            "Eu estou muito ocupado esses dias...":


                mc desculpa "Eu estou meio ocupado esses dias, então não sei..."

                ngep "Ok..."

        mc normal "Então é isso. Obrigado pela disposição [nge]."

        ngep "Pode sempre contar comigo."

        mc "Ok. Beijos."

        ngep "Beijo."



        scene black with dissolve

        "..."

        jump nathan_e1_continua

    label nathan_e1_continua:





        scene pub booth with dissolve

        mc normal "Pronto, [n]."

        mc normal "Consegui tudo o que eu precisava dela."



        n "Eu vi... Que bom que vocês se acertaram."

        n "Eu terminei aqui também."

        n "Foi uma noite divertida, não foi, garotas?"



        scene black with dissolve

        scene n1_new11 with Dissolve(1.0)

        pause

        if nathan_e1_fim_garota == "Maria":



            ngep "Foi sim. Eu adorei meu teste..."

            ngep "O [mc] me ensinou uma pose sexy e... muito mais..."



            "Ana" "A gente reparou..."

            "Ana" "Eu gostei muito da nossa conversa, [n]. Você é um cavalheiro."

        elif nathan_e1_fim_garota == "Ana":



            ngep "Com certeza! O [mc] foi incrível."



            "Maria" "Deu pra ver tudo, [nge]..."

            "Maria" "O [n] foi um verdadeiro cavalheiro. Adorei nossa conversa."







        n "Ainda vamos nos ver. Boa noite."

        "Garotas" "Até, lindos."

        mc normal "Até!"

        scene black with dissolve

        "..."

        scene n1_new12 with Dissolve(1.0)

        n "Ufa."

        if nathan_e1_fim_garota != "Nada":



            n "Eu vi você com a [nge]."

            n "Não falei que meu plano ia funcionar?"

            mc normal "Realmente... foi incrível. Você realmente fez a cabeça delas."

            n "Mas a parte final foi você. Meus parabéns."

            mc "Valeu."
        else:




            n "Eu vi que no fim acabou não rolando..."

            mc desculpa "Pois é. Valeu pela ajuda, mas eu não tava no clima."

            n "Tudo bem, amigo. Eu entendo. Não tem porque ficar pra baixo."

        jump nathan_e1_final

    label nathan_sem_garotas:

        n "Eu vou dispensar elas e a gente pode conversar melhor."

        mc normal "Legal."

        "..."



        "Garotas" "Voltaaamos!"

        scene black with dissolve

        scene n1_new11 with Dissolve(1.0)

        pause



        n "Maria, Ana. A conversa com vocês estava muito bacana, mas eu tenho um assunto sério pra conversar com o [mc] sobre minha carreira."

        n "Infelizmente não vou poder passar a noite com vocês."







        "Ana" "Que pena, [n]..."



        n "É mesmo. Vocês são garotas incríveis. Mas a gente vai sair de novo. Certeza."

        "Ana" "Ok... Boa noite, [n]."







        "Maria" "Boa noite, [n]. Foi um prazer."



        n "O prazer foi meu, Maria."



        "..."



        scene black with dissolve

        n "Prontinho..."

        scene n1_new12 with Dissolve(1.0)

        mc envergonhado "Elas ficaram realmente tristes de não poderem passar a noite com você."

        n "É o que parece."

        mc normal "Você tem noção de que você poderia ter ficado com as duas muito fácil, né?"

        n "Eu não gosto de pensar nos outros dessa forma."

        mc serio "Como assim?"



        n "Não me importa se elas me olham como um objeto. Um cara bonito, sarado e famoso que faz os hormônios delas ferverem."

        n "Eu não consigo olhar para elas dessa forma."

        n "Eu só fico com pessoas que eu conheço há algum tempo e que me impressionam não apenas sensualmente, fisicamente eu digo, mas por outros atributos."

        mc serio "Não existem muitas pessoas que conseguem segurar as vontades desse jeito."

        n "Talvez eu seja um esquisitão... Só que eu não consigo sentir prazer em relações de uma noite. Me parece barato e..."



        n "Desculpa falar de coisa chata. Ainda fico parecendo um esnobe puritano."

        mc normal "Relaxa. Eu entendo o que você está falando."

        menu:
            "Eu também não gosto de relações de uma noite.":


                $ nathan_amizade += 1

                mc normal "Eu concordo. Eu também acho relações puramente físicas uma coisa barata e meio sem sentido."

                n "Legal saber isso. Somos parecidos nisso então."

                mc normal "Verdade."
            "Às vezes eu preciso de algo rápido e físico.":


                mc normal "Eu entendo o que você diz."

                mc safado "Mas às vezes não tem como evitar. Eu preciso de algo físico."

                mc "Sentir o momento pelo momento."

                n "Eu também consigo entender. E não acho que seja errado ou algo assim. Só não é minha praia."

                mc normal "E eu acho bem legal de sua parte. Acho nobre."

        "..."

    label nathan_e1_final:



        n "Bom, agora somos só nós. O que acha da gente beber alguma coisa?"

        $ garcomname = "Fabrício"

        menu:
            "Claro. Vamos pedir algo.":


                $ n1_bebida = True

                $ nathan_amizade += 1

                mc normal "Seria uma boa."

                n "Ótimo. Vamos até o balcão."



                mc desconfiado "O que será que o [gar] vai inventar hoje?"

                n "Você conhece o figura?"

                mc "Sim."

                if p1_bebida:

                    mc desconfiado "Ele arranjou uma bebida esquisita pra mim da última vez que estive aqui."

                    n "Ah! Eu sei do que você tá falando. Eu já tomei isso..."

                    n "Mano... pensa num treco forte."
            "Pode pedir para você. Eu tô de boa.":


                mc desculpa "Eu não tô no clima pra bebida. Obrigado."

                mc normal "Mas vou acompanhar você."

                n "Aí, sim. Vamos lá no balcão."

                mc "Vamos."

        scene pub dois with dissolve

        "..."



        n "E aí, [gar]! O que manda?"



        gar "Senhor, [n]!"

        scene black with dissolve

        scene n1_new13 with Dissolve(1.0)

        pause





        mc desconfiado "Boa noite, [gar]."

        gar "O senhor [mcc] também está aqui."

        mc "Você lembra meu nome?"

        gar "Obviamente, senhor [mc]. É meu trabalho como garçom."

        mc zerado "Se você diz..."



        if nge == "Garotas":

            gar "Puxa, senhor [n]. Pelo que estou vendo, não deu certo com as duas senhoritas..."

            n "Não sinta pena da gente, [gar]. A gente resolveu ter uma noite de amigos."

            gar "Isso é deveras importante, senhor."

            gar "Amizade é um recurso imensurável e deve ser tratado como tal."
        else:


            gar "Eu vi os dois senhores se dando bem com as senhoritas. Meus parabéns."

            gar "Eram espécimes da mais alta postura."

            "O jeito que esse cara fala sempre me assusta..."

            n "Claro que você não poderia deixar de ficar de olho, né?"

            gar "É de minha responsabilidade manter todos meus visitantes em segurança, senhor. Peço que entenda."

            mc zerado "Você só tá encontrando razões pra continuar bisbilhotando..."

        n "[gar], mudando de assunto. Você pode pegar algo pra gente beber?"

        if not n1_bebida:

            n "Tem certeza que não vai querer beber nada, [mc]?"

            menu:
                "Tenho. Não quero.":


                    mc normal "Tenho, sim, [n]. Obrigado por oferecer."

                    n "Sem problemas."
                "Vou querer beber, sim":


                    $ n1_bebida = True

                    mc normal "Na verdade acho que vou querer, sim. Pode pedir pra mim."

                    n "Você não vai se arrepender."

        if n1_bebida:

            gar "Então o que vai ser, senhores?"

            n "Pode me trazer aquela lá, [gar]."



            gar "Você se refere àquela LÁ, senhor [n]?"

            n "Essa mesmo."

            gar "Aguardem um segundo e voltarei em breve."
        else:


            n "Me traga o de sempre, [gar]."

            gar "Sim, senhor."





        scene black with dissolve

        scene n1_new16 with Dissolve(1.0)

        n "Logo logo ele volta."

        mc normal "Beleza."

        "Esse [n]... Não tenho certeza do que pensar..."

        "Ele me ofereceu uma das garotas..."

        if nathan_cassia:

            "E mesmo sabendo do lance da [j] ele continua agindo normalmente e de boa comigo..."

        "Mas não tenho certeza se fui com a cara dele."

        "Não posso esquecer também do meu acordo com a [j]."

        "Preciso decidir quais serão minhas intenções com ele."

        menu:
            "Ele é só um modelo idiota. Não quero papo com ele.":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("nathan_opiniao_exibido","inicio","local")

                $ n1_avaliacao = "nada"

                "Não adianta eu ficar todo impressionado. Provavelmente ele só tá querendo se exibir."

                "Não quero ter nada a ver com esse babaca."

                "Vou cortar ele na primeira chance que eu tiver."
            "Vou tratar ele como um amigo por enquanto.":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("nathan_opiniao_amizade","inicio","local")

                $ n1_avaliacao = "amigo"

                "Ele tá sendo bem legal comigo. Acho que ele é um cara bacana. Não tenho porque pensar diferente por enquanto."
            "Ele é um partidão. Acho que eu quero algo a mais com ele...":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("nathan_opiniao_seducao","inicio","local")

                $ n1_avaliacao = "seducao"

                "Ele é um gato. E tá sendo bem atencioso comigo. Se eu conseguir, vou tentar ir além com ele sem dúvidas."

        "Seja como for, preciso conseguir alguma informação dele..."

        n "{size=15}[mc]...{/size}"

        "Pelo jeito que as coisas estão no momento, eu ainda tô muito longe. A [j] vai acabar comigo..."

        mc angustiado "..."

        n "[mc]!"

        mc triste "..."

        mc surpreso "Ah! O que foi?!"



        n "Tudo bem? Você parecia meio voando..."

        mc desculpa "Sim. Está tudo bem. Desculpa."

        n "Só queria saber se você tá legal..."

        mc "..."

        menu:
            "Não é nada...":


                $ nathan_amizade += 1

                mc envergonhado "Valeu por se preocupar, mas não é nada."

                n "Tem certeza? Você não parece tão legal..."

                mc normal "Pô. Tamo tendo um tempo massa aqui. Não quero estragar o clima."



                n "Haha... Normalmente eu diria pra gente não se preocupar com isso."

                n "Mas este encontro não é um acaso do destino, certo?"

                mc desconfiado "Como assim?"

                n "Obviamente você tem um motivo pra ter vindo falar comigo."

                n "E existe um motivo do meu lado também, pra ter aceitado conversar com você esta noite."

                mc "Quer dizer que você também tem uma agenda por trás?"

                n "Não sei se é algo tão bem pensado que a gente possa chamar de agenda... Mas, sim, algo do tipo."

                scene n1_new17 with Dissolve(1.0)



                n "Na verdade, eu estou com uma dúvida, e tava pensando que talvez você pudesse me ajudar."

                menu:
                    "Tem algo a ver com a [j]?":


                        mc serio "Isso tem a ver com a [j], não tem?"

                        n "Sim. Acho que não adianta negar isso."

                        if not nathan_cassia:

                            mc envergonhado "Eu não vou mais negar também."

                            mc serio "Eu tô aqui por causa dela. Ela me escreveu e disse que você estaria aqui."

                            n "Isso era óbvio. Só queria saber se você ia admitir."

                            mc serio "..."
                    "Posso ajudar, claro. Pode falar.":


                        $ nathan_amizade += 1

                        mc normal "Já que estamos jogando limpo, eu vou ouvir o que você tem a dizer."

                        if not nathan_cassia:

                            n "Só que antes de continuar, quero que você me fale a verdade."

                            n "Você está aqui por causa da [j], não é?"

                            mc envergonhado "Não adianta negar mais."

                            mc serio "Sim, eu tô aqui por causa dela."

                            n "Isso era óbvio. Só queria saber se você ia admitir."

                            mc serio "..."

                jump n1_verdade

            "Sabe aquele lance que eu te falei da [j]?" if nathan_cassia:

                mc desculpa "Então, sabe aquele lance que te falei da [j]?"

                n "Sei... Que ela tá embaçando sua amiga."

                mc triste "Pois é. Ela disse que eu preciso conseguir alguma coisa sobre você. Alguma coisa que ela possa usar."

                n "Eu tô ligado disso desde o começo."

                if n1_avaliacao != "nada":

                    mc desculpa "Mas você tem sido um cara legal. Não sei o que fazer agora."

                    mc triste "Claro que eu me preocupo com minha amiga. Mas não quero só passar por cima de você."

                    n "..."

                    mc envergonhado "Malz. Não queria estragar a noite falando dessas coisas."



                    n "Relaxa..."

            "Eu queria te falar a verdade sobre a [j]." if not nathan_cassia:

                mc desculpa "É que eu menti pra você antes. Eu falei que não tinha nada com a [j]."

                mc triste "Mas a verdade é que é por isso que eu vim aqui hoje."

                n "..."



                n "Relaxa. Eu saquei isso desde o começo."

                n "E além disso a forma como você negou não foi a mais convincente."

                mc envergonhado "Haha..."

        label n1_verdade:

            n "Olha, [mc]..."

            n "Eu não odeio a [j]. A matéria dela não é terrível pra mim pra falar a verdade."

            n "Eu ainda estou só começando como modelo. Tô muito longe de atingir o topo."

            n "A [j] viu, sei lá, um potencial que eu tenho, e resolveu investir em mim."



            scene n1_new17 with Dissolve(1.0)



            n "Ela quer fazer uma coisa meio louca na minha opinião..."

            mc desconfiado "Meio louca?"

            n "Sim. Ela quer escrever uma matéria completa enquanto ainda não sou famoso, e me tornar famoso com a matéria dela."

            n "E assim ela vai ter sido a primeira a falar do novo modelo top, entende?"

            mc desconfiado "Acho que sim..."

            mc "E por que então você não aceitou passar tudo pra ela?"

            n "Não sei. Alguma coisa nela não me cheira bem. Ela parece... obstinada demais. Não consegui confiar completamente nela."

            mc zerado "Eu entendo perfeitamente..."

            n "Pois é! Aquele jeito dela é terrível..."

            n "Agora eu não sei direito o que fazer..."

            menu:
                "Você precisa fazer o que é melhor pra sua carreira.":


                    jump n1_carreira
                "Não confie na [j] de forma alguma.":


                    $ nathan_amizade += 1

                    mc bravo "Se tem uma coisa que eu aprendi, é que a gente não pode confiar na [j] de forma alguma."

                    mc "Mesmo que seja algo que vai te ajudar na carreira, a gente não sabe o que ela tá tramando contra você."

                    n "Mas..."



                    scene n1_new15 with Dissolve(1.0)

                    n "Não é melhor pra você que eu conte algo pra ela? E sua amiga?"

                    mc desculpa "Não importa. Eu vou dar um jeito nisso de alguma forma depois."

                    mc "Não quero que você coloque tudo à perder por minha causa."

                    n "..."

                    n "Mas e se minha carreira não progredir?"

                    mc concentrando "Hmm..."

                    menu:
                        "Talvez realmente seja melhor você contar com a [j].":


                            jump n1_carreira
                        "Não importa. A [j] é muito perigosa. Confie em mim.":


                            $ nathan_amizade += 1

                            mc desculpa "Não sei como resolver isso. Mas minha opinião é que você não pode confiar nela."

                            mc bravo "Mesmo que ela te ajude, o que ela vai cobrar depois?"

                            mc "Ela é uma mulher que não dá ponto sem nó. Ela está um passo na nossa frente."

                            scene n1_new16 with Dissolve(1.0)

                            n "Obrigado, [mc]. Eu acho que o medo de estagnar não está me deixando pensar direito."

                            mc normal "Não é nada de mais. Eu só não consigo suportar a [j]."

                            n "Ela foi atenciosa comigo. Mas eu sinto que uma hora ou outra ela vai fazer algo que eu não vou gostar."

                            mc triste "Igual ela fez comigo..."

                            n "..."

                            n "Agora você me deu uma ideia."

                            mc desconfiado "Huh?"

                            jump n1_ideia

            label n1_carreira:

                mc envergonhado "Assim..."

                mc "Não que eu seja a pessoa certa pra dar dicas sobre isso."

                mc serio "Mas, pelo que eu tô aprendendo nos últimos tempos, esse meio é tipo uma mão lava a outra."

                mc bravo "Eu sei que isso por um lado é terrível. E pra falar a verdade eu nem queria ser paparazzo."

                mc serio "Só tô nessa porque é a única forma que eu encontrei de continuar morando aqui na capital."

                mc serio "Mas no seu caso, se você acha que isso vai alavancar sua carreira, acho que você deveria aceitar."

                if n1_avaliacao == "seducao":

                    mc safado "E você é boa pinta. Além de ter um corpo sarado."

                    mc "Você tem tudo pra se dar bem."

                mc normal "Eu sei que nem tudo vai ser perfeito. Provavelmente a [j] vai fazer alguma coisa voltar contra você em algum momento."

                mc "Mas nem tudo é perfeito na vida, concorda?"

                mc "..."

                n "..."



                n "Acho que você tem razão, [mc]..."

                n "Pensando bem, não adianta ter medo. Acho que eu preciso dar esse passo."

                mc "..."

                label n1_ideia:



                    n "Só que eu vou precisar de você pra isso."

                    mc desconfiado "Ah? Por que eu?"

                    n "Olha... Eu tenho uma novidade que é exatamente aquilo que a [j] tá querendo."

                    n "Mas eu não vou falar pra ela."

                    mc normal "Certo..."

                    n "Vou revelar pra {b}você{/b}."

                    mc surpreso "Quê?! Por quê?!"

                    n "Porque assim eu não vou me entregar pra ela e ainda por cima posso dar o up que eu preciso na minha carreira."

                    mc triste "..."



                    n "Eu fechei um grande contrato com uma marca de roupas. Mas ela não é tão conhecida."

                    n "Meu contrato está ligado ao quanto minha presença vai agregar para a marca."

                    mc desconfiado "Agregar em qual sentido?"

                    n "Quanto minha presença vai atrair olhares para essa marca. Quero dizer, depende do meu potencial como celebridade."

                    n "Se eu conseguir atrair matérias, reportagens e deixar a marca famosa, eu vou crescer com ela, e vou ganhar uma bolada."

                    n "Mas se eu não atrair olhares, então eles vão só cancelar o contrato e eu volto pra estaca zero."

                    mc serio "É por isso que por um lado você precisa da matéria da [j]."

                    n "Exatamente."

                    n "Mas eu não preciso dela. Eu preciso da sua revista."

                    mc desconfiado "..."

                    n "Então vou deixar nas suas mãos. Se você quiser, você publica a matéria e ganha os pontos com seu chefe e a fama."

                    n "Ou você pode entregar para a [j]. Eu não me importo."



                    n "Eu sei que é mancada, mas vou deixar essa escolha pra você."

                    mc triste "..."

                    n "Aqui estão as informações sobre meu contrato."

                    mc angustiado "..."

                    menu:
                        "Tudo bem. Pode contar comigo.":


                            $ nathan_amizade += 1

                            label n1_ajuda:

                                python:
                                    if renpy.android:
                                        PythonSDLActivity.registraEvento("nathan_ajudar_aceitou","inicio","local")

                                $ n1_ajuda = True

                                mc charmoso "Tudo bem. Pode deixar que eu vou fazer essa pra você."

                                mc "Prometo que vou fazer tudo o que eu puder pra te ajudar, [n]."

                                scene n1_new14 with Dissolve(1.0)

                                n "Muito obrigado, [mc]. Não sei por que, mas eu confio em você."

                                mc envergonhado "Hehe... Também não sei..."

                                n "Agora eu tô sentindo que tirei um baita peso das costas!"

                                n "Espero que sua revista possa realmente me ajudar..."

                                mc serio "Pelo bem ou pelo mal, parece que o que nossa revista publica é verdade. Alguma coisa vai acontecer."

                                n "É o que eu espero. Minha carreira depende disso."

                                jump n1_final
                        "Não posso fazer isso. Não posso escolher por você.":


                            mc desculpa "Me perdoe, [n]. Mas não posso fazer essa escolha por você."



                            scene n1_new18 with Dissolve(1.0)

                            n "Eu sei que é complicado, mas eu realmente preciso da sua ajuda!"

                            n "Por favor, [mc]!"

                            menu:
                                "Me desculpe, mas não posso. Você precisa decidir seu próprio futuro.":


                                    python:
                                        if renpy.android:
                                            PythonSDLActivity.registraEvento("nathan_ajudar_recusou","inicio","local")

                                    mc triste "Eu entendo, mas não posso ficar com essa responsabilidade."

                                    n "..."

                                    mc desculpa "Me desculpe, [n]..."

                                    n "Tudo bem. Acho que só vou entregar essas informações para a [j]..."

                                    mc serio "Espero que você entenda minha posição..."



                                    n "Ah, claro. Eu entendo. É seu direito."

                                    mc normal "Valeu."

                                    mc normal "Espero que a decisão que você tomar leve você para um grande futuro."

                                    if n1_avaliacao != "nada":

                                        mc "E sempre que você precisar de alguém, pode falar comigo."

                                        n "Obrigado, [mc]. Estava meio triste com você, mas acho que você realmente só quer que eu decida por mim mesmo."

                                        mc "Exatamente. Tenho certeza que você vai conseguir."

                                        n "Ok..."

                                    jump n1_final
                                "Ok. Eu vou ajudar você.":


                                    mc normal "Tudo bem. Você venceu. Eu vou ajudar você."

                                    jump n1_ajuda

    label n1_final:

        if n1_ajuda:

            mc serio "Espero que eu possa conseguir te dar a visibilidade que você precisa..."



            n "Eu sei que você vai conseguir."

            mc zerado "Só não sei se vou conseguir isso sem te vender pra [j]..."

            n "Você vai tomar a melhor decisão. Eu confio em você."

            mc serio "..."

            "Esse cara tá colocando o futuro dele nas minhas mãos. Será que isso é certo?"
        else:


            scene n1_new14 with Dissolve(1.0)



        n "Agora vamos esquecer disso e se divertir."

        mc desconfiado "Aliás, cadê o [gar]?"

        n "Nossa, faz tempo que ele..."









        scene black with dissolve

        scene n1_new19 with Dissolve(1.0)

        gar "Aqui estou, senhores..."

        mc zerado "Você estava ouvindo tudo?"

        gar "Como pode pensar algo assim de mim, senhor [mc]?"

        mc "..."

        gar "Aqui está sua bebida, senhor [n]."

        n "Opa! Valeu."

        if n1_bebida:

            gar "E aqui está a sua, senhor [mc]."

            mc serio "Obrigado..."
        else:


            n "É sua última chance. Não vai querer beber mesmo?"

            menu:
                "Não. Tô de boa. É sério.":


                    mc serio "Não. Realmente tô correndo de bebida hoje. Vai ficar pra próxima."



                    n "Beleza..."

                    n "Mas você não sabe o que tá perdendo..."
                "Tudo bem, vai. Depois de tudo, preciso de um gole.":


                    $ n1_bebida = True

                    mc normal "Depois do nosso papo, acho que tô precisando beber algo."

                    n "Você não vai se arrepender."

                    gar "Eu trouxe duas taças, senhores."

                    mc zerado "Como você sabia?"

                    mc "Quer saber, esquece..."

        if n1_avaliacao == "nada":

            "Ele parece ter sido bem sincero comigo. Será que ele realmente é um babaca?"

            menu:
                "Sim. Continuo querendo distância desse cara.":


                    mc serio "..."
                "Não. Vou dar uma chance pra ele.":


                    $ n1_avaliacao = "amigo"

                    mc normal "..."

        if not n1_avaliacao == "nada" and nathan_amizade > 0 and n1_bebida:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("nathan_e1_amizade","inicio","local")

            $ nathan_e1 = "amizade"
            $ nathan_amizade_evento += 1





            scene black with dissolve

            scene n1_new14 with Dissolve(1.0)

            n "[mc]! É aqui que nossa noite começa!"

            mc feliz "A é?"

            n "Claro! Se prepare!"

            mc desconfiado "Pois é... É minha primeira vez tomando essa bebida especial do [gar]..."

            n "Você vai ficar bem! {size=15}Depois de 1 ou 2 dias...{/size}"

            mc zerado "O que você disse aí?!"

            n "Não esquente com isso! Só mandar pra dentro."

            mc feliz "Ok. Aqui vai!"

            mc concentrando "{i}glup glup{/i}"

            mc muitofeliz "Puaahhh... É quente pra caralho!"

            n "Não tô falando?!"

            mc "Tô sentindo uma vontade de gritar, sei lá!"

            n "Hahaha! É assim mesmo, brother! Curte aí!"



            scene black with dissolve

            mc muitofeliz "O que está acontecendo?!"

            "..."

            scene n1_new20 with Dissolve(2.0)

            pause



            n "Você tá fazendo um cara engraçada, brother!"

            "[mcpnome]" "Tá brincando, cara?!"

            "[mcpnome]" "Tá tudo girando!"

            "[mcpnome]" "Tá tudo muito louco!"

            n "Hahaha! Assim que é bom, brother!"

            n "Vamo curtir a parada!"

            "[mcpnome]" "Curtir a parada!"

            "[mcpnome]" "{size=20}Curtir a parada...{/size}"

            "[mcpnome]" "{size=15}Curtir a parada...{/size}"

            "[mcpnome]" "{size=10}Curtir a parada...{/size}"

            "[mcpnome]" "{size=5}Curtir a parada...{/size}"

            "..."

            scene black with Dissolve(5.0)

            "..."

            "[mcpnome]" "{size=10}HAHAHA!{/size}"

            "..."

            "[mcpnome]" "{size=10}OLHA ISSO! OLHA O QUE VÔCE TÁ FAZENDO!{/size}"

            n "{size=10}O que é isso, cara?! HAHAHA!{/size}"

            if n1_avaliacao == "seducao":

                scene n1_new21 with Dissolve(2.0)

                pause

                "[mcpnome]" "{size=10}Você fica mais gato sem camisa...{/size}"

                n "{size=10}Valeu...{/size}"

                n "Você é foda, [mc]. Tira a blusa também!"

                mc "Se você quer ver... eu tiro..."

                n "Alguém tá afim de fazer coisas diferentes hoje!"

                mc "Você que tá mexendo comigo."

                n "Olha, [mc]... você já beijou um cara antes?"

                mc "Eu nem sei onde eu tô... imagina saber o meu passado!"

                n "Essa bebida bate forte mesmo, né?"

                mc "Mas se você quer saber se eu beijaria um cara hoje... hmm..."

                n "Beijaria?"

                menu:
                    "Beijaria.":


                        mc "Beijaria... com certeza."

                        n "Eu sou um cara, sabe?"

                        mc "Acho que eu entendi..."

                        scene black with dissolve

                        scene n1_new22 with Dissolve(1.0)

                        pause

                        mc "Hmm..."

                        n "Será que a gente vai lembrar alguma coisa amanhã?"

                        mc "Tomara que eu nunca esqueça esse beijo..."

                        n "Era isso que eu tava pensando... seria um desperdício..."

                        n "Foda-se também. Vamo aproveitar agora."

                        mc "Falou tudo."

                        window hide

                        pause
                    "Hoje não.":


                        mc "Beijar acho que hoje não... mas a gente pode se divertir!"

                        n "Fechou!"

                n "Bora pra um lugar mais vazio!"

                mc "Tem a praça do outro lado da rua!"

                n "Então bora!"

                scene black with dissolve

            scene parque noite with Dissolve(3.0)

            pause

            scene parque noite with hpunch

            mc surpreso "!"

            mc "Onde eu tô..."

            mc "Ai minha cabeça... O que eu tô fazendo aqui na praça?"

            mc angustiado "Preciso ir pra casa..."

            scene black with Dissolve(3.0)

            $ nathan_numero = True
            $ nathan_cel_msg1 = True

            $ dormir_em_casa = True

            jump dormir
        else:


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("nathan_e1_fracasso","inicio","local")

            $ nathan_e1 = "fracasso"



            scene black with dissolve

            scene n1_new13 with Dissolve(1.0)

            n "Mano! Essa bebida é demais!"

            mc normal "Parece boa mesmo."

            mc "Acho que eu vou indo, [n]. Tenho que pensar em tudo o que conversamos."

            n "Certeza, brother? Não quer curtir um pouco?"

            mc "É sério. Preciso pensar muito bem no que vou fazer."

            n "Beleza, brother. A gente se vê depois."

            mc "Claro! Até a próxima."

            gar "Boa noite, senhor [mc]."

            mc "Boa noite, [gar]."

            "..."

            scene black with dissolve

            scene pub geral with dissolve

            if n1_ajuda:

                $ pautas += 1
                $ nathan_p1 = True

                $ resultado_encontro = "nathan"

                show screen menu_pontos
                with dissolve

                "O [n] me passou todas as informações sobre o contrato dele. Isso com certeza dá uma excelente pauta para o chefe."

                "Mas eu também tenho meu problema com a [j]..."

                mc serio "E agora?"

                "Dependendo do que eu fizer com essa informação, minha vida vai mudar para um lado diferente."

                "Desde que a [c] apareceu na minha vida e eu comecei a conhecer as celebridades, estou precisando tomar decisões difíceis."

                "Não é fácil ter que escolher essas coisas."

                "Por um lado quero continuar vivendo aqui, mas entregar essas informações para meu chefe e agora talvez pra [j] também..."

                mc incomodado "Isso é horrível."

                "Bom... A vida não é fácil. E eu não quero desistir. Muitas coisas legais estão acontecendo também."

                "Preciso pensar muito bem no que eu vou querer fazer com o caso do [n]."

                "Mas vou deixar isso pra amanhã."

                hide screen menu_pontos
                with dissolve
            else:


                "Ele queria que eu ajudasse ele com o lance da [j] e eu recusei."

                "Será que eu devia ter negado isso? Ele parecia tão desesperado."

                "Mas não posso tomar uma decisão dessas por ele. É a carreira dele, mais ainda, a vida dele está em jogo."

                "Você não pode passar essa responsabilidade para alguém dessa forma."

                "Mas agora não tenho informação nenhuma pra dar pra [j]..."

                mc triste "Será que ela vai publicar a matéria sobre mim e a [c]?"

                mc serio "Amanhã tenho que falar com ela de qualquer jeito."

            mc serio "Depois de tudo o que aconteceu eu tô quebrado. Vou direto pra cama."

            "..."

            $ dormir_em_casa = True

            jump dormir

label nathan_evento3:

    $ nathan_e3 = "finalizado"

    mc desculpa "Tava pensando aqui..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n3_save", extra_info="n3_save")

    "O que será que deu aquele rolo com o [n]?"

    scene mc parque_sentado with Dissolve(1.0)

    if cassia_e1 != "nathan":

        "Mesmo tendo ficado do lado da [j] aquele dia, ainda tô preocupado com ele."

    "Acho que eu vou mandar uma mensagem e perguntar..."

    $ nathan_cel_msg2 = True

    show screen celular_nathan

    ""

    "Pronto. Tomara que esteja tudo legal."

    "A Cássia não tinha que se enfiar dessa forma na vida dele. Ela podia muito bem ter escrito a matéria sem mencionar algo como esse problema dele com o país."

    "É estranho pensar que alguém como o [n], que pode virar uma estrela de grande destaque, esteja ilegalmente no país."

    if nathan_e2 == "seducao":

        $ nathan_beijo = True

        "E agora que a gente se beijou... ele ainda disse que não queria que acabasse nisso..."

        "O [n] é tão bonito e charmoso. É incrível que ele tenha se interessado por mim. Além de que ele pode virar muito famoso e cheio da grana também."

        "Eu preciso pensar muito bem se eu vou querer algo sério com ele. Ele não parece ser um cara que curte só farrear."

    elif cassia_e1 == "nathan":

        "Ele está virando cada vez mais um grande amigo."

        "Sem dúvida ele é um cara bacana. O Nathan tem uma vibe relax e ele sabe conversar."

        "Pelo menos quando uma jornalista não expõem seu pior segredo pra todo o país."

        "Além de ser uma boa companhia, como famoso eu posso conseguir pautas com ele ainda."

        "Acho que eu fiz o certo ficando do lado dele e não da [j] aquela noite."
    else:


        "Sem dúvida ele é um cara bacana. O [n] tem uma vibe relax e ele sabe conversar."

        "Pelo menos quando uma jornalista não expõem seu pior segredo pra todo o país."

        "Além de ser uma boa companhia, como famoso eu posso conseguir pautas com ele ainda."

        "Eu sei que eu acabei entrando no jogo da [j] aquela noite. Mas isso não muda o que ele é."

    "Opa, ele respondeu."

    $ nathan_cel_msg2_r = True

    show screen celular_nathan

    ""

    "Ele quer se encontrar comigo."

    if nathan_beijo:

        "Não posso deixar ele na mão. Não depois do que rolou entre a gente."

        "Não tenho nem o que pensar."

        "Deixa eu avisar ele que eu vou pro bar."

        "..."

        "Opa. Ele já respondeu."

        $ nathan_cel_msg2_r2 = "sim"

        show screen celular_nathan

        ""

        "Beleza. Ele deve chegar logo. Melhor eu sair."

        scene black with Dissolve(1.0)

        "..."

        jump nathan_e3_bar
    else:


        "Ele tá vivendo esse rolo todo. Será que eu quero entrar no meio disso?"

        mc "Eu não devia estar sendo pragmático desse jeito, mas tem tanta coisa acontecendo ultimamente..."

        "Não! Não posso ser cuzão. Tenho que..."

        play sound "audio/som_3_celular.mp3"

        $ renpy.vibrate(1)

        "Smartphone" "Trr... Trrr..."

        scene parque dia with Dissolve(1.0)

        "Quem é?"

        mc surpreso "[j]?!"

        mc zerado "..."

        mc desconfiado "Alô?"

        j "Oi, pombinho."

        mc zerado "Odeio quando você fala assim..."

        j "Olha. Eu preciso falar com você hoje."

        if cassia_e1 != "nathan":

            j "Você fez um bom trabalho convencendo o [n] que eu posso ajudar ele. Mas agora a gente precisa continuar com o plano."

            mc desculpa "[j]... eu sei o que eu fiz. Mas não sei se eu quer-"
        else:


            j "Você não fez o que eu te pedi na outra noite."

            mc serio "Eu-"

            j "Só que eu vou te dar outra chance de ser meu amigo."

            mc desculpa "[j]. Não sei se eu-"

        j "Calma. Vem aqui em casa e eu vou te explicar o que eu preciso de você. Estou te esperando."

        mc serio "Espera! Eu não sei se eu quero fazer parte disso. O [n] precisa de ajuda."

        j "Mas é pra isso que eu estou te chamando."

        mc desconfiado "Como é?"

        j "É o que você ouviu, pombinho. Eu quero ajudar o [n]."

        j "Se você vier até aqui falar comigo eu prometo que ele não será deportado do país."

        mc desculpa "Mas ele quer falar comigo agora. Acabou de me chamar."

        j "Tudo bem. Você pode sair com ele depois. Só preciso que você passe aqui antes de falar com ele."

        mc serio "Espera..."

        "Ele não será deportado? Como ela pode garantir isso?"

        "A [j] é famosa na ilha e deve ter várias conexões. Seria uma forma de eu garantir que o [n] vai continuar aqui."

        "E agora? O que eu faço? Acredito ou não na [j]?"

        "Será que eu aceito o convite dela?"

        menu:
            "Aceitar o convite da [j]":


                "Prefiro falar com a [j]. Ela pode ser uma víbora, mas eu ganho muito mais sendo um aliado dela."

                "E talvez isso até acabe ajudando o [n] no fim."

                "Deixa eu avisar o [n] que não vou poder sair agora."

                $ nathan_cel_msg2_r2 = "nao"

                show screen celular_nathan

                ""

                if cassia_e1 != "nathan":

                    "Espero que eu não me arrependa de falar com ela..."

                    mc desculpa "Vou dar uma passada aí então."

                    j "Perfeito, pombinho. Te espero."

                    mc zerado "..."

                jump nathan_e3_cassia_casa
            "Recusar a [j] e se encontrar com o [n]":


                "É claro que eu vou falar com o [n]. O cara tá passando por mó barra."

                "Não tenho nem o que pensar. Me envolver com a [j] só vai dar rolo."

                if cassia_e1 != "nathan":

                    mc serio "[j], eu combinei de falar com o [n] agora. Não vai dar pra passar aí."

                    j "Tudo bem, pombinho. Depois me fala como foram as coisas com ele."

                    j "Até."

                    "..."

                    "A [j] foi estranhamente compreensiva... Só consigo pensar que tem algo pra ela em eu me tornar amigo do [n]."

                    "Tudo o que essa mulher faz é calculado."

                    "Bom..."

                "Deixa eu avisar ele que eu vou pro bar."

                "..."

                "Opa. Ele já respondeu."

                $ nathan_cel_msg2_r2 = "sim"

                show screen celular_nathan

                ""

                "Beleza. Ele deve chegar logo. Melhor eu sair."

                jump nathan_e3_bar

label nathan_e3_cassia_casa:

    $ cassia_e2_cassia = True

    "Me envolver com a [j] é sempre complicado. Ela já causou muito comigo e com a [c]. E agora tá pegando no pé do [n]."

    "Eu nem devia tá aceitando falar com ela desse jeito."

    "Mas ela tem poder dentro da revista. E ela é implacável. É melhor ser amigo do que inimigo da [j]."

    mc concentrando "Enfim... bora pegar o busão."

    scene cidade onibus with Dissolve(1.0)

    "Espero que ele chegue logo."

    "..."

    call cena_onibus from _call_cena_onibus

    "O condomínio da [j] fica pra cá."

    "..."

    scene cassia_ap porta with Dissolve(1.0)

    play sound "audio/som_15_campainha.mp3"

    "..."

    "..."

    "De novo ela vai querer que eu entre..."

    "Tô sem saco. Bora entrar."

    scene cassia_ap geral with Dissolve(1.0)

    "Esse ap dela ainda me deixa louco, mano. Quanto dinheiro essa mulher não tem?"

    mc serio "[j]!"

    j "{size=17}Estou aqui no quarto, pombinho!{/size}"

    mc zerado "..."

    mc "Já vi essa história antes."

    if cassia_e1 == "seducao":

        "Da outra vez que eu vim aqui a gente se pegou. Será que ela vai querer outra vez?"

        "Pensando bem... não tenho muitas lembranças daquela noite."

        "O que será que ela fez comigo? Que estranho..."

    scene cassia cama_levantando with Dissolve(1.0)

    mc surpreso "!"

    mc envergonhado "Opa. Cheguei."

    j "Estou levantando, bebê."

    "..."

    scene cassia_ap quarto with Dissolve(1.0)

    mc "Oi."

    show cassia n_provocando with Dissolve(1.0)

    j "Já aprendeu o caminho até aqui, né?"

    if cassia_e1 == "seducao":

        j "Ficou com saudades da nossa última brincadeira?"

        mc envergonhado "..."

        mc desconfiado "Ah! Falando nisso, eu não consigo lembrar direito daquela noite. O que houve?"

        j "Não fique pensando demais, bebê. A gente só curtiu."

        mc "Ok..."

    j "Eu sei que você veio porque queria olhar pra mim de novo."

    menu:
        "E quem não ia querer?":


            mc tarado "E quem não ia querer ver uma mulher gostosa desse jeito assim?"

            show cassia n_costas with dissolve

            j "Você tá aprendendo como tratar uma mulher, pombinho."

            j "Tô gostando de ver."

            mc safado "..."
        "Estou aqui por causa do [n].":


            mc desculpa "Na verdade, eu quero saber qual é seu objetivo com o [n]. Ele tá passando por uma barra gigante."

            show cassia n_explicando with dissolve

            j "Não estrague a diversão falando sobre ele, pombinho."

            j "Olha bem o que tem na sua frente. Isso não acontece todo dia."

            mc "..."
        "Por que você me chamou?":


            mc serio "O que eu quero saber é por que você me chamou. Qual é seu plano?"

            show cassia n_explicando with dissolve

            j "Não precisa ir com tanta sede ao pote, pombinho."

            j "Olha bem o que tem na sua frente. Isso não acontece todo dia."

            mc serio "Mas eu-"

            j "Bom..."

    show cassia n_proposta with dissolve

    j "Eu te chamei aqui porque está na hora da gente continuar com o plano de cobertura da crise do [n]."

    if cassia_e1 != "nathan":

        j "Você fez muito bem convencendo ele a aceitar minha ajuda. Então agora a gente vai continuar com isso."
    else:


        j "O acordo era você convencer ele a contar com minha ajuda, certo? Só que você não fez."

        mc serio "..."

        j "Mesmo assim, a gente vai poder continuar com o plano. Só que vai ser um pouco mais difícil por sua causa."

    mc preocupado "Mas se o [n] for deportado sua matéria vai pro saco, certo?"

    j "Na verdade seria uma excelente conclusão. Mas não é esse meu objetivo."

    mc desconfiado "Isso quer dizer que-"

    j "Não quero que ele seja deportado. Eu vou salvar ele."

    mc surpreso "Quê?! Mas então-"

    j "Exatamente."

    j "Vamos descer. Tenho que te explicar tudo."

    mc serio "Ok."

    scene cassia_ap terreo with Dissolve(2.0)

    "Salvar ele? Ela que colocou ele em risco em primeiro lugar."

    "Por que tudo isso?"

    show cassia n_pensando with dissolve

    j "Você ainda é muito ingênuo pra entender certas coisas. A maioria das pessoas nem prestam atenção na vida."

    j "Você tem que tomar cuidado pra não acabar como elas."

    j "Segure a vida com suas duas mãos. VOCÊ tem o controle sobre ela, não o contrário."

    menu:
        "Você não passa de uma controladora.":


            mc serio "Você não passa de uma controladora maquiavélica. Não quero ser como você."

            j "Pode falar o que quiser, bebê. Se você quer ver seus sonhos realizados, não adianta ficar de nhé nhé nhé."

            mc "..."

            j "Eu sou maquiavélica no sentido real da palavra. Pra mim, os fins justificam os meios."

            j "Se eu tiver que acabar com o [n] pra subir na vida, eu farei isso sem pensar duas vezes."

            mc preocupado "..."
        "Como assim? O que isso tem a ver?":


            mc desconfiado "O que isso tem a ver com o caso do [n]?"

            show cassia n_proposta with dissolve

            j "Eu vou mesmo ter que explicar tudo pra você?"

            mc "..."

            if cassia_nathan_entregou:

                j "Eu só consegui as informações dele porque você me entregou."

            elif cassia_nathan_naoajudou:

                j "Ele só veio me entregar as informações depois de falar com você no bar."
            else:


                j "Eu nunca consegui a informação do contrato dele com a Blergh! porque nem ele nem você me entregaram."

            j "O [n] acha que não precisa de mim. Ele me recusou."

            j "E agora ele vai ver só. Ele vai sofrer na minha mão. Vai, com certeza."

            mc desculpa "Você resolveu publicar sobre a ilegalidade dele só por causa disso?"

            show cassia n_explicando with dissolve

            j "Isso não é pouco, benzinho. Você não pode deixar as pessoas fazerem o que querem com você."

            j "Se alguém te esnobar, acabe com ela. Se alguém te negar, pise nela. Não pode existir alguém acima de você."

            mc preocupado "..."

    show cassia n_costas with dissolve

    j "Mas não quero te dar sermão hoje, pombinho. Olha aqui pra baixo."

    window hide

    pause

    j "Olhou bem?"

    mc envergonhado "..."

    j "Então. Se você continuar com nosso plano, prometo mais disso pra você hoje. Você aceita?"

    mc serio "Não posso aceitar nada sem que você me explique melhor qual é o próximo passo do seu plano."

    mc "Eu quero te ajudar, mas não quero prejudicar o [n] também."

    show cassia n_proposta with dissolve

    j "Você ainda tem escrúpulos demais, pombinho."

    j "Já tá na hora de você deixar essas coisas de lado e focar em fazer aquilo que você precisa."

    mc "..."

    j "Ok, ok."

    j "O que você vai ter que fazer é gravar o [n] contando tudo pra você. Eu quero material multimídia sobre essa questão toda."

    mc surpreso "Gravar?!"

    j "Sim. Quero ele falando sobre os problemas, sobre os medos dele. Tudo o que você conseguir."

    j "Vamos dar um follow up no fato dele estar irregular no país e faturar em cima disso."

    mc zerado "[j]..."

    j "Me poupe da sua ética. E então? Tá dentro ou não?"

    menu:
        "Eu aceito. Com algumas condições.":


            "Não tenho o que fazer. Vim até aqui. Agora tenho que aceitar."

            "Ela disse que não vai deixar ele ser deportado. Vou confiar nela... por hora."

            mc desculpa "Ok... eu vou fazer isso."

            j "Perfeito."
        "Não quero mais fazer parte disso.":


            mc serio "Eu sei que eu entrei na sua da outra vez, mas agora eu não quero mais saber disso."

            show cassia n_explicando with dissolve

            j "Como?"

            mc "É isso mesmo. Não concordo com o que você tá fazendo com o [n]."

            j "[mc], pombinho... você não sabe o que tá falando. Você já viu o que eu posso fazer com você. Tem certeza que me quer como inimiga?"

            mc desculpa "Não é isso. Mas esse lance do Na-"

            j "Como seu amiguinho [n] vai sair dessa sem minha ajuda? Você tá jogando sua chance de ajudar ele pelo ralo."

            "Falando desse jeito, ela tá me fazendo duvidar de mim mesmo. E agora?"

            menu:
                "Tenho certeza. Não quero participar do plano da [j].":


                    mc serio "Você pode me ameaçar quanto quiser. Eu não quero mais nada com esse plano."

                    j "Você tomou sua decisão, [mc]. Boa sorte pra vocês."

                    j "Pode sair da minha casa."

                    hide cassia with dissolve

                    "Não tenho mais nada pra fazer aqui."

                    scene cassia_ap porta with Dissolve(1.0)

                    "Tenho que voltar pra ilha."

                    "..."

                    scene mc onibus with Dissolve(1.0)

                    "Vou dar uma passada no bar. Talvez o [n] ainda queira conversar."

                    jump nathan_e3_bar
                "Acho melhor eu aceitar o plano dela.":


                    mc desculpa "Pensando bem, se o seu plano vai ajudar o [n], eu aceito."

                    show cassia n_proposta with dissolve

                    j "Você fez a escolha certa, pombinho."

                    j "Os amigos de [jc] só têm coisas boas os esperando."

                    "Espero que tudo acabe bem."

    mc serio "Mas você precisa me prometer que o [n] não vai ser deportado."

    j "..."

    $ cassia_e2_plano = True

    if cassia_seducao:

        show cassia n_costas with dissolve

        j "Eu já te falei que o homem que faz o que eu mando me deixa pegando fogo?"

        mc desconfiado "?"

        mc envergonhado "Que papo é esse?"

        j "Chegou a hora da sua recompensa..."

        mc "Re-recompensa?!"

        hide cassia with dissolve

        j "Agora deixa o resto comigo. Só relaxa e tira a roupa..."

        mc surpreso "Cá-Cássia!?"

        j "Só tira aqui..."

        mc "O que você tá fazendo?!"

        j "Cala a boca e me ajuda."

        mc "Mi-minha roupa!"

        menu:
            "Sair correndo":


                mc surpreso "Te-te-tenho que ir!"

                j "Como?!"

                show cassia_ap porta with hpunch

                mc angustiado "{i}puf puf{/i}"

                "Essa mulher é louca!"

                "Deixa eu voltar pra ilha."

                "..."

                scene mc onibus with Dissolve(1.0)

                "Vou dar uma passada no bar. Talvez o [n] ainda queira conversar."

                jump nathan_e3_bar
            "...":


                mc safado "..."

        j "Agora já pro sofá!"

        scene cassia mc_sofa with Dissolve(3.0)

        $ renpy.pause(delay=2, hard=True)

        pause

        j "Hoje eu acordei muito excitada, [mc]. Você vai ter um agrado e tanto..."

        mc "Ma-mas... eu..."

        j "Só me aperta e deixa o resto comigo."

        mc "E-eu..."

        j "Hmm... assim mesmo..."

        "Essa mulher é maluca. Mas eu simplesmente não consigo falar não pra ela."

        mc "Hmm..."

        j "Agora chega de preliminares. Pronto para o prato principal?"

        mc "S-sim."

        j "Então deixa eu tir-"

        "Telefone" "{i}Ring ring{/i}"

        mc "Ah?"



        j "Eu tô excitada demais pra parar agora."

        mc "É importante?"

        j "Claro. Eu só faço coisas importantes."

        mc "Então não é me-"

        j "Cala a boca. Eu tô mandando você vir aqui e chupar meu peito. Se eu vou atender ou não não importa pra você."

        j "Vem aqui agora."

        label ca3_premium1:

            pass

        menu:
            "Tá bom.":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_9

                    jump ca3_premium1

                mc "Ok... eu quero curtir você também."

                j "E quem não quer a mulher perfeita, hm? Vem, bebê."

                scene black with dissolve

                scene n3_premium9 with Dissolve(1.0)

                pause

                j "Assim mesmo, querido."

                mc "Hmmm..."

                j "Se diverte bastante. Se lambuza no meu peitão."

                j "Não foi barato deixar ele desses jeitos, mas eu vejo todos na redação babando pra eles."

                j "Fico pensando quantos de vocês se masturbaram pra eles lá na redação mesmo... ah..."

                j "É por isso que vocês fazem tudo o que eu mando?"

                mc "Eles são uma delícia mesmo."

                j "É o que todos eles falam."

                mc "Todos? Você sai com outros da redação?"

                j "Você achou que fosse o único, é, pombinho? Você é o do dia. E olha lá."

                j "Se você não arrancar minha roupa e não me mamar direito, vou ter que chamar outro."

                menu:
                    "Eu cuido de você.":


                        mc "Deixa comigo. Eu vou cuidar bem dessa tetona."

                        scene black with dissolve

                        scene n3_premium10 with Dissolve(1.0)

                        pause

                        j "Assim que eu gosto! Com vontade!"

                        j "Eu preciso sentir você morrendo pra me comer."

                        mc "Eu quero muito!"

                        j "Então continua mamando que você chega lá."

                        mc "{i}slhup{/i}"
                        scene nnew_ani14 with Dissolve(1.0)
                        j "Isso... com vontade... hmm..."

                        j "Continua agradando sua chefe. Que paparazzo mais safado que você é."

                        mc "Hmm..."

                        j "Tá bom pra aí. Tenho outro lugar pra você chupar agora."

                        mc "Outro?"

                        j "Deita aí. Vai!"

                        mc "Tá..."

                        scene black with dissolve

                        scene n3_premium11 with Dissolve(1.0)

                        pause

                        mc "NGH!"

                        j "Isso! Coloca a língua pra fora e deixa eu me esfregar na sua cara!"

                        mc "Nnnngh! C-cáxia!"

                        j "Cala a boca e fica quieto! Engola minha buceta perfeita!"

                        j "Eu opero ela todo ano pra deixar ela assim bonitinha! Então aproveita!"

                        mc "A-aghh!"

                        j "Para de chorar! Aannh... delícia..."

                        "Ela tá esfregando mesmo!"

                        j "Eu amo vocês que tão abaixo de mim! Eu faço o que eu quero!"

                        "Essa mulher não tem jeito mesmo."

                        j "Eu uso vocês como eu bem entender! No trabalho, na cama! Vocês são todos meus!"

                        j "Assim! Continua!"

                        scene n3_premium12 with Dissolve(1.0)

                        pause

                        j "Continua assim! No meu clítoris!"

                        j "Ainn! Que delícia!"

                        mc "Aa-ahnn! C-cuidado!"

                        j "Tá quase acabando! Ahnn! Você aguenta!"
                        scene nnew_ani05 with Dissolve(1.0)
                        mc "C-cá-"

                        j "Cala a boca e enfia a língua pra fora!"

                        mc "Nnngh!"

                        "Ela é violenta! Esfregando desse jeito!"

                        j "Você geme assim de dor, mas seu pau tá duro, né?!"

                        j "Eu sei que você gosta de obedecer, pombinho!"

                        j "Agora é sua recompensa! Eu tô pronta!"

                        j "Eu preciso dessa jeba pra gozar gostoso!"

                        scene n3_premium13 with vpunch

                        pause

                        j "AAHHNN!"

                        mc "Aah!"

                        j "Isso! Eu tô encharcada! Deixa eu usar seu pau!"

                        mc "A-ah! C-calma!"
                        scene nnew_ani06 with Dissolve(1.0)
                        j "Deixa eu quebrar seu pau com minha buceta deliciosa! Vai ser inesquecível!"

                        mc "Ah-ahnn!"

                        "Mesmo louca desse jeito ela continua uma delícia! Ela tá me apertando muito!"

                        mc "Você é muito apertada, Cássia!"

                        j "Claro que eu sou, pombinho! Eu garanto que tudo esteja perfeito! Ahnn!"

                        j "Anngh! Mas eu preciso de mais! Me aperta mais, viado!"

                        mc "NNGH!"

                        scene n3_premium14 with vpunch

                        pause

                        j "Ai! Assim mesmo!"

                        mc "Aah... aah..."

                        j "Assim! Ahnn! Forte assim!"

                        mc "S-se você continuar assim eu vou gozar!"

                        j "Nem brinque com uma coisa dessas, idiota! Você só goza depois de mim! Nngh!"

                        j "Eu preciso de muito mais!"

                        mc "E-eu-"

                        j "Aguenta, cretino! Ahnn!"

                        mc "Eu tô quase lá! Não vai dar!"

                        j "Cala a boca e segura!"

                        "Eu vou enlouquecer assim!"

                        j "Aaiinn! Assimmm! AAhnn!"

                        mc "C-cássia!"

                        scene n3_premium15 with vpunch

                        pause

                        mc "AAAAGGH!"

                        j "Nããão!"

                        mc "G-gozando!"

                        scene n3_premium15 with vpunch

                        j "Eu mandei! Não acredito, seu frouxo!"

                        mc "E-eu... não aguentei... você é gostosa demais..."

                        j "E ainda tudo dentro de mim... não é possível... e já tá amolecendo!"
                        scene nnew_ani07 with Dissolve(1.0)
                        mc "Perdão... mas..."

                        j "Não quero saber de desculpa... eu vou ter que chamar aquele outro lá."

                        mc "Outro?"

                        j "O meninão lá da redação. Ele vai dá no coro."

                        j "Se você quiser ficar aqui, eu não ligo. Até prefiro dois caralhos, mas se quiser pode ir."

                        "Ficar aqui e participar com outro cara?"

                        menu:
                            "Eu vou ficar.":


                                mc "Eu fico... até ele chegar eu tô pronto."

                                j "É o mínimo... deixa eu ligar."

                                scene black with dissolve

                                "..."

                                scene cassia_ap terreo with Dissolve(1.0)

                                j "Isso... estamos te esperando... vem logo ou nem venha."

                                j "Pronto... ele chega rápido."

                                "Transar com ela e outro cara junto... onde eu fui entrar?"

                                "Será que eu fiz certo de aceitar isso aí?"

                                show black with dissolve

                                hide black with dissolve

                                j "Ele chegou."

                                "É agora... quem será esse aí? Outro boneco na mão da Cássia..."

                                scene black with dissolve

                                scene n3_premium16 with Dissolve(1.0)

                                pause



                                "Ronaldo" "O-olá... [mc]?!"

                                mc "Ronaldo?!"

                                "Ronaldo" "Então você também..."

                                mc "Pois é..."

                                j "Você também pensou que era o único?"

                                "Ronaldo" "Aquela conversa de se juntar..."

                                j "Cala a boca. Você não tá aqui pra usar a boca. Mas por causa desse pau imenso que você tem."

                                mc "E-"

                                j "Você também. Vocês dois juntos vão fazer sua chefe gozar rapidinho."

                                j "Pombinho, você vem aqui na frente. E você, grandão, me pega por trás."

                                "Ronaldo" "S-sim, senhora."

                                j "Pode entrar direto, que ele já me melou toda."

                                "Ronaldo" "..."

                                scene black with dissolve

                                scene n3_premium17 with Dissolve(1.0)

                                pause

                                j "Ain... isso... esqueci como seu pau é grosso."

                                j "E você, pombinho, encher minha boca."

                                j "Usar vocês dois assim me deixa com muito tesão!"

                                "Ronaldo" "Senhora Cássia... você é uma delícia."

                                j "Então vai, me arromba com esse caralhão monstro!"

                                j "E você... deixa eu me lambuzar..."

                                "Ronaldo" "Nngh!"

                                mc "Ah..."

                                j "Aproveitxem!"

                                mc "Você chupa muito gostoso, Cássia..."

                                scene n3_premium18 with Dissolve(1.0)

                                pause

                                j "Voxê não merrexe, goxou xem eun mandaarr... ahnn..."

                                j "Max eu xupoonnn... hmmmm...."

                                j "Quero tudooaan... como come goxtozzonn!"
                                scene nnew_ani18 with Dissolve(1.0)
                                j "Ahnn..."

                                "Se ela continuar me mamando assim acho que eu vou gozar de novo."

                                "Mas o Ronaldo tá acabando com ela lá trás."

                                "A Cássia deve ter todo mundo da redação na mão dela..."

                                "Ou na buceta dela, né?"

                                scene n3_premium19 with Dissolve(1.0)

                                pause

                                j "Issxo! Ahnn! Nnnghh!"

                                "Ronaldo" "S-senhora Cássia! Eu tô aqui pra fazer você se sentir bem!"

                                j "Isxo! Vaiinn! Nnnnghh!"

                                "Ronaldo" "Eu tô aproveitando também! Me desculpa!"

                                j "Podxe aprovetarr! Annnhhn! Gostoxo! Ainn!"
                                scene nnew_ani08 with Dissolve(1.0)
                                j "Asxim mesmo!"

                                "Ronaldo" "A senhora vai gozar?"

                                j "Ainda não! Eu quero maix!"

                                j "Mudxa de posixão!"

                                mc "Tá legal."

                                "Ronaldo" "Sim, senhora."

                                scene black with dissolve

                                scene n3_premium20 with Dissolve(1.0)

                                pause

                                j "Assim, crianças... hmm..."

                                j "Aprende com ele, pombinho. Olha como ele segura e come gostoso até eu deixar ele gozar."

                                mc "E-eu já to quase gozando de novo..."

                                j "Pode gozar... pode soltar o que sobrou da sua porra em mim... hmmm..."
                                scene nnew_ani09 with Dissolve(1.0)
                                mc "Ah..."

                                "Ronaldo" "Senh-"

                                j "E você fica quieto e come."

                                "Ronaldo" "s-sim..."

                                j "Se vocês não me fizerem gozar agora, eu não sei o que eu faço!"

                                j "Deixa eu me divertir aqui..."

                                scene n3_premium21 with Dissolve(1.0)

                                pause

                                mc "Ah... tá gostoso demais, Cássia."

                                j "Então goza... se masturba logo e goza em mim... eu tô quase chegando lá também."

                                j "Ahnnn... isso... continua com esse caralhão em mim..."

                                "Ronaldo" "Sim, senhora Cássia."

                                j "Agora acelera... aahnn... hmm... vai..."

                                "Ronaldo" "Aagh!"

                                j "Assim... aahnn... AHNN!"

                                mc "C-cássia!"

                                j "Isso! AAHNN! Assim! Mais um pouco!"

                                "Ronaldo" "Eu vou gozar!"

                                j "Isso! Gozem os dois em mim!"

                                mc "Posso gozar?!"

                                j "Ain! SSiimm! Eu também! Seus paus - aahnn! - Vão fazer eu gozar, cretinos!"

                                j "Vain! AAHG!! AAAHNNN! VAIIINN!!!"

                                scene n3_premium22 with vpunch

                                pause

                                j "AAAHHNNNN! GOZANDO!!!"

                                mc "E-eu também!! AAH!"

                                "Ronaldo" "AAAGH!"

                                scene n3_premium22 with hpunch

                                pause

                                j "Aah... aahh... aannnhh...."

                                j "Quanta porra... que delícia..."

                                j "Vocês foram bem... meninos... agora... eu tenho que voltar ao trabalho."
                                scene nnew_ani10 with Dissolve(1.0)
                                j "Volta logo pra redação, grandão. A gente se vê lá."

                                "Ronaldo" "Qualquer coisa me chama..."

                                j "Eu sei.. não precisa falar."

                                scene black with dissolve

                                j "Preciso de um banho. Cadê minha camisola?"
                            "Tô indo nessa.":


                                mc "Pra mim deu... outro cara é demais... se divirta."

                                j "É um frouxo mesmo... pode sair. Eu tenho que ligar pra ele."

                                j "Mas primeiro..."
                    "Então chama. Falou.":


                        mc "Se você vai ficar de graça aí, então tô saindo fora."

                        j "Você tá falando sério, idiota?!"

                        mc "Tô. Vou indo nessa."

                        j "Era só que me faltava... um idiota desses. Me solta!"

                j "Eu vou responder aquela ligação de antes."
            "Melhor você atender.":


                mc "Se é importante é m-melhor você atender."

                j "Tanto faz..."
    else:


        "Telefone" "{i}Ring ring{/i}"

        mc "Ah?"

        j "Licença. Preciso atender."

        "Telefone" "{i}Ring ring{/i}"



    scene black with dissolve

    scene cassia_ap terreo with Dissolve(1.0)

    "O que é isso agora?"

    mc angustiado "..."

    "..."

    show cassia n_explicando with dissolve

    j "Eu vou ter que atender aqui. Você entendeu o que tem que fazer."

    j "Depois de gravar o Nathan, me procure na redação."

    mc envergonhado "Mas-"

    j "Adeus."

    hide cassia with moveoutright

    mc zerado "..."

    "O que eu faço agora? Ela não vai falar comigo."

    "Vou me trocar e dar o fora..."

    show black with Dissolve(1.0)

    "..."

    "Espera!"

    hide black with dissolve

    "Com quem será que a [j] tá falando no telefone?"

    "Do jeito que ela abandonou nossa pegação mesmo dizendo que tava excitada..."

    mc desconfiado "Deve ser algo importante..."

    menu:
        "Dar o fora o quanto antes":


            "Bah! Não vou me meter nessa. Só vou dar o fora."

            "..."

            scene cassia_ap porta with Dissolve(1.0)

            "Tenho que voltar pra ilha."

            "..."

            scene mc onibus with Dissolve(1.0)

            "Vou dar uma passada no bar. Talvez o [n] ainda queira conversar."

            jump nathan_e3_bar
        "Tentar ouvir a conversa":


            mc tarado "Vou tentar ouvir..."

            "Com muita calma..."

            scene cassia_ap cozinha with Dissolve(2.0)

            "..."

            j "{size=17}Sim. Vou estar na redação. Podemos nos falar mais lá.{/size}"

            j "{size=17}Tá tudo sob controle... Não. Espera. Só um segundo.{/size}"

            "Ixi. Ela tá esperta. Deixa eu sair daqui."

    "..."

    scene cassia_ap porta with Dissolve(1.0)

    "Tenho que voltar pra ilha."

    "..."

    scene mc onibus with Dissolve(1.0)

    "Vou dar uma passada no bar. Talvez o [n] ainda queira conversar."

    jump nathan_e3_bar

label nathan_e3_bar:

    if cassia_e2_cassia:

        "Acho que eu vou avisar ele que eu tô indo pra lá."

        if cassia_e2_plano:

            "Eu disse pra [j] que eu ia gravar ele falando sobre os problemas dele. Ela vai querer sensacionalizar com isso."

            "Mas ela disse que ia ajudar ele também a continuar no país. Será que eu fiz a escolha certa?"

        scene mapa cidade with Dissolve(1.0)

        "Smartphone" "Tuuu... Tuuu..."

        n "Alô? [mc]?"

        mc normal "Oi, [n]. Acabei meus rolos aqui. Quer dar um pulo no bar agora?"

        n "Quero, sim, amigo. Tô precisando conversar."

        mc "Tô chegando lá agora."

        n "Beleza. Tô saindo do centro. Vou demorar um pouco."

        mc "Sem problema. Te vejo lá."

        n "Até."

        "Boa! Que bom que ele aceitou falar comigo."

    "..."

    "Cheguei no bar do [gar]."

    $ tempo = 2

    scene hub_bar_fundo cenario with Dissolve(2.0)

    "Parece que tá vazio. Nem o [gar] tá por aqui. O que será que tá rolando?"

    "Deixa eu sentar."

    show hub_bar mc_sul with dissolve

    if nathan_beijo:

        "Eu e o [n] nos beijamos daquela vez. Não consigo tirar isso da cabeça."

    if n1_avaliacao == "seducao":

        "Eu quero ficar com ele..."

        "Só que com a chance dele ser deportado do país, nosso lance pode acabar de uma hora pra outra."

        "Tenho que ajudar ele com todas minhas forças."

        "Além de que ele deve tá super pra baixo com tudo isso acontecendo. Vou tentar dar uma animada nele."

    elif n1_avaliacao == "amigo":

        "Eu e o [n] estamos ficando cada vez amigos."

        "Mesmo com o surto que ele teve na casa da [j], dá pra ver como ele é um cara bacana."

        "Espero que a gente consiga resolver esse problema. Quero ajudar o máximo que eu puder."

    gar "Senhor [mc]. Não tive a honra de ver o senhor adentrando o recinto."

    show hub_bar fabricio with dissolve

    mc "Fala aí, [gar]."

    gar "A que devo a honra de sua resplandecente estadia?"

    mc "Tô esperando o [n]."

    gar "Oh. O senhor [n] está deveras preocupado com os últimos acontecimentos..."

    mc "Como você sabe disso?! Ele te contou?"

    gar "Existem certas coisas que todo homem deve saber, senhor [mc]."

    mc "Quê?! Mas isso não faz... Quer saber? Deixa pra lá."

    gar "Por mais que suas palavras sejam sempre de grande admirabilidade, continuar a parlar com este humilde garçom não seria de grande valia."

    mc "Se eu entendi o que você acabou dizer, você quer parar de falar comigo?"

    gar "Pois, sim."

    mc "Por que? Tô incomodando?"

    gar "Oh, não! Como poderia, senhor [mc]? É que o senhor [n] acaba de chegar."

    mc "Mas cadê ele?"

    gar "Ali."

    mc "Na-Nathan?!"

    n "Fala aí, [mc]."

    n "Deixa eu sentar aí."

    show hub_bar mc_nathan with dissolve

    mc "Como ele sab-"

    n "O que foi?"

    mc "O [gar]..."

    n "Haha! Não tente entender o sujeito. Certas coisas são melhores quando não entendemos."

    mc "Acho que você tem razão..."

    n "E cadê ele?"

    mc "Eita. Sumiu."

    n "É bom que ele nos dê um pouco de privacidade."

    mc "Você realmente acredita que ele só vai deixar a gente conversar sem bisbilhotar?"

    n "Com certeza não. Mas eu confio nele. Pode deixar ele ouvir."

    mc "Se você diz..."

    label nathan_e3_conversa:

        if not n3_carreira:

            n "..."

            "O [n] não tá falando nada. Deixa eu puxar um assunto."

            "Melhor não falar do lance da imigração de primeira. Vou puxar um assunto qualquer antes."
        else:


            "Agora é a hora."

        menu:

            "Como tá indo no trabalho?" if not n3_carreira:

                $ n3_carreira = True

                mc "Como andam as coisas no trabalho?"

                n "Ah... Olha..."

                scene nathan mc_bar_rindo with Dissolve(1.0)

                n "Em vista de tudo, até que tá indo bem, acredita?"

                mc "Sério? Isso é muito bom."

                n "Sim. Eu achei que já teria sido demitido por quebra de contrato a essa hora, mas ninguém falou nada."

                mc "Finalmente uma boa notícia."

                n "Pois é. É estranho que eles não tenham ouvido do caso. Mas não vou ficar questionando haha!"

                mc "Sim. E o que você tem feito pela Blergh? Eles tão curtindo seu trabalho?"

                n "Estão, sim. Está sendo melhor do que eles imaginavam. Vou nos eventos, tiro umas fotos, uso umas roupas deles..."

                mc "Vida difícil, hein?"

                n "Pior que é corrido pra caramba. Inclusive hoje a noite tem evento."

                mc "Assim que é bom, rapaz."

                n "Espero que um dia a gente possa ir juntos em um evento."

                menu:
                    "Com certeza. Vai ser massa.":


                        if nathan_beijo:

                            mc "Eu adoraria ir com você."

                            n "Por que isso parece uma cantada?"

                            mc "Talvez por que seja?"

                            n "[mc]..."
                        else:


                            mc "Opa. E conhecer um monte de gente rica e famosa? Pode contar comigo."

                            n "Haha! Você sabe como são essas festas."

                            n "Quem sabe até umas minas, né? Modelo ainda por cima."

                            mc "Aí você tá falando minha língua."
                    "Esses eventos cheio de glamour não são minha praia.":


                        mc "Pra falar a verdade, acho que eu nem curto muito esses ventos muito cheio de glamour."

                        n "E o pior é que é tudo assim. Tem que gostar."

                        n "Mas tem eventod de todo tipo. Se aparecer um assim mais calmo eu te aviso."

                        mc "Demorou."

                "Eu sinto que essa conversa deu uma animada nele."

                scene hub_bar_fundo cenario with Dissolve(1.0)

                show hub_bar mc_nathan with Dissolve(1.0)

                jump nathan_e3_conversa

            "O lance da sua situação no país..." if not n3_situacao:

                if not n3_carreira:

                    "Não quero entrar direto no assunto... melhor eu perguntar alguma coisa mais tranquila antes."

                    jump nathan_e3_conversa

                $ n3_situacao = True

                mc "Sei que é chato falar disso, mas não consigo não te perguntar... Como tá a situação da imigração?"

                n "Ah!"

                n "Nem sei o que te falar, [mc]..."

                n "Você foi muito legal comigo naquela noite. Não sei se eu ia conseguir me acalmar se não fosse por você."

                n "Obrigado mesmo."

                mc "Que isso, [n]. Claro que eu ia te ajudar. Não precisa agradecer, tá doido?"

                if cassia_e1 == "nathan":

                    n "Mas você ficou do meu lado. Mandou a gente esquecer a [j] e dar nosso jeito."
                else:


                    n "Você me convenceu que mesmo depois de tudo a [j] pode nos ajudar. Foi isso que me acalmou aquela noite"

                n "Você me passou tanta confiança. Não consigo imaginar o que eu teria feito sem você."

                if cassia_e2_plano:

                    scene mc bar_celular with Dissolve(2.0)

                    "A [j] pediu pra eu gravar tudo que o [n] falasse. Essa é a hora perfeita."

                    "Mas agora que eu tô aqui, não sei se isso realmente é o melhor."

                    "Ela disse que ajudaria ele, mas será que realmente vender ele pra [j] vai resolver alguma coisa?"

                    menu:
                        "Gravar sua conversa com o [n].":


                            $ n3_gravou = True

                            "Eu tenho que fazer isso. Por mim e pelo [n] também. Todo mundo vai sair ganhando nessa."

                            "Vou ligar o gravador e nem tem como ele saber."
                        "Não gravar e desobedecer a [j].":


                            "Não consigo. Não quero fazer parte disso. Não seria justo com o [n]."

                            "Foda-se a [j]. Depois eu me entendo com ela."

                    n "[mc]? Tudo bem?"

                    mc "Ah! Sim!"

                scene nathan mc_bar_conversando with Dissolve(1.0)

                mc "Eu queria poder te ajudar mais. Não sei como isso funciona."

                n "Nem eu. E o pior é que não posso contar com ninguém. Não posso falar com meus amigos do trabalho."

                mc "Por que?"

                n "Isso pode se virar contra mim. Se os diretores da Blergh! descobrem isso, meu contrato pode ir pro saco."

                n "Nem sei como ainda não me chamaram depois que a matéria foi publicada no site da revista."

                mc "Entendo..."

                mc "Deve ser como uma bomba relógio pra você."

                n "Exatamente! Eu sinto que a qualquer hora isso vai explodir e acabar com a minha vida."

                n "Preciso resolver isso sozinho. Isso que é o pior. Vou ter que saber mais sobre as leis e como regularizar minha situação."

                menu:
                    "Espero que isso se resolva":


                        mc "Isso é complicado mesmo, [n]. Espero que tudo fique bem."

                        mc "Pode contar comigo."

                        n "Obrigado, [mc]. Desculpa puxar você pro meio desse rolo todo. Eu queria-"

                        mc "Não precisa falar nada. Vamos resolver isso. Eu prometo."

                        n "Ok..."

                        scene nathan mc_bar_rindo with Dissolve(1.0)

                        n "Você é o cara. Um verdadeiro amigo."

                        mc "Não é pra tanto, cara."

                        n "É, sim. Você é um sujeito especial. Não sei explicar. O jeito que você parece aberto pra resolver o problema das pessoas."

                        n "Não sei... é como se você quisesse ajudar os outros sem pedir nada em troca."

                        mc "Deixe pra falar isso quando a gente resolver tudo."

                        n "Haha! Verdade. Mas mesmo que dê tudo errado. Você já é meu parça, [mc]."

                        mc "Valeu, [n]."

                        n "Eu que agradeço."
                    "Segurar a mão do [n] e confortar ele":


                        scene nathan mc_bar_mao with Dissolve(2.0)

                        pause

                        mc "Você sabe que pode contar comigo. Eu tô aqui pra você."

                        n "Obrigado, [mc]. Você é realmente um cara especial."

                        if n1_avaliacao == "seducao":

                            mc "Inclusive... tem uma coisa que eu não consigo tirar da cabeça."

                        if nathan_beijo:

                            mc "Nosso beijo no condomínio da [j]..."

                            n "O que eu disse naquela noite continua valendo."

                            mc "Co-continua?"

                        if n1_avaliacao == "seducao":

                            n "Eu gosto de você, [mc]. Você me protegeu no momento que eu estava mais precisando."

                            n "Eu me sinto bem falando com você. E nosso beijo... eu achei muito especial."

                            mc "Eu também achei..."

                            n "Você... não quer repetir?"

                            menu:
                                "Eu quero.":


                                    $ nathan_e3_beijo = True

                                    mc "Eu quero..."

                                    n "Eu estava torcendo pra você responder isso. Vem aqui comigo."

                                    mc "Tá..."

                                    scene pub booth with Dissolve(1.0)

                                    show nathan seduzido with Dissolve(1.0)

                                    n "Aqui a gente vai ter mais privacidade."

                                    n "Hoje eu não vou deixar você sair só com um beijinho."

                                    mc envergonhado "O-ok..."

                                    hide nathan with dissolve

                                    n "Senta aqui, [mc]."

                                    "Que nervoso. Meu coração vai sair pela boca."

                                    "Ele tá se aproximando."

                                    n "..."

                                    mc concentrando "..."

                                    scene nathan mc_beijo with Dissolve(3.0)

                                    $ renpy.pause(delay=5, hard=True)

                                    pause

                                    mc "Hmmm..."

                                    "O beijo do [n] é diferente de tudo o que eu já senti antes."

                                    "O jeito que ele faz eu me sentir. Acho que ele é o cara certo pra mim."

                                    "..."

                                    "A gente já tá se pegando por um tempo..."

                                    "..."

                                    window hide

                                    pause



                                    n "A gente não precisa parar aqui. Tá afim de fazer mais?"

                                    mc "Aqui? Você sabe que a gente tá no meio do bar, né?"

                                    n "E daí? Tá vazio essa hora."

                                    n "Eu quero mais."

                                    mc "Eu também, mas..."

                                    n "Tira minha camisa e me beija."

                                    "E agora? E se alguém vê a gente aqui?"

                                    label n3_premium1:

                                        pass

                                    menu:
                                        "Tirar a camisa dele":


                                            if not premium:

                                                call mensagem_premium from _call_mensagem_premium_10

                                                jump n3_premium1

                                            "Nem morto que eu paro agora. Eu quero aproveitar esse homem e vai ser agora."

                                            mc "Seu pedido é uma ordem, gostoso."

                                            scene black with dissolve

                                            scene n3_premium1 with Dissolve(1.0)

                                            pause

                                            n "Hmm... era isso mesmo que eu queria. Poder olhar e beijar você assim."

                                            mc "Você sabe que eu também quero você. Quero aproveitar."

                                            n "Então aproveita."

                                            window hide

                                            pause

                                            n "Beija mais."

                                            mc "Hmm..."

                                            scene n3_premium2 with Dissolve(1.0)

                                            pause

                                            n "Eu adoro sua boca."

                                            mc "E eu a sua."

                                            "É uma loucura eu e o Nathan se pegando aqui no bar."

                                            "O Fabrício ou qualquer cliente pode pegar a gente no pulo, se catando sem roupa aqui."

                                            "Que absurdo..."

                                            "Mas isso só deixa tudo mais quente."

                                            "Eu quero mais."

                                            mc "Eu quero mais que sua boca."

                                            n "O que você quer?"

                                            scene n3_premium3 with Dissolve(1.0)

                                            pause

                                            n "A-ah... safado..."

                                            mc "Você gosta?"

                                            n "Tá me deixando louco."
                                            scene nnew_ani29 with Dissolve(1.0)
                                            mc "Quer que eu pare?"

                                            n "Claro que não. Continua assim... eu quero sentir mais disso."

                                            mc "Então me pega com esse bração forte que você tem."

                                            n "Tudo o que você quiser, gato. Só continua me beijando assim."

                                            scene n3_premium4 with Dissolve(1.0)

                                            pause

                                            n "Aah... ahnn..."

                                            mc "Parece que o amigão aqui em baixo tá curtindo também."

                                            n "Eu tô com muito tesão, [mc]."

                                            mc "Aah..."

                                            n "Mas eu não quero tudo pra mim. Você também merece. Ainda mais depois do que você fez pra mim."

                                            mc "Aproveitar você assim é tudo que eu quero agora."

                                            n "Não... eu tenho um presente melhor ainda pra você."

                                            mc "Hm?"

                                            n "Tira a calça... eu quero pegar nele."

                                            mc "S-sério?! I-isso é demais, Nathan..."

                                            n "Vai, tira logo. Eu quero agradecer você."

                                            menu:
                                                "Abaixar as calças":


                                                    mc "T-tá... pega nele..."

                                                    scene black with dissolve

                                                    mc "Pronto..."

                                                    scene n3_premium5 with Dissolve(1.0)

                                                    pause

                                                    n "Assim..."

                                                    mc "Ah..."

                                                    n "Eu vou cuidar muito bem de você."
                                                    scene nnew_ani31 with Dissolve(1.0)
                                                    mc "Tá..."

                                                    "Que delícia a mão dele em mim assim..."

                                                    n "´É bom, né? Eu sabia que você ia gostar quando eu pegasse no seu pau assim."

                                                    n "Mas isso é só o começo, [mc]..."

                                                    mc "Hm?"

                                                    scene n3_premium6 with Dissolve(1.0)

                                                    pause

                                                    n "Se você não gozar, não tem graça... então eu vou acelerar, tá?"

                                                    mc "A-ah!"

                                                    n "Sente minha mão te masturbando."
                                                    scene nnew_ani30 with Dissolve(1.0)
                                                    "S-se ele continuar assim eu vou..."

                                                    n "Quero sentir bem gostoso..."

                                                    mc "N-nathan... e-eu..."

                                                    n "Isso..."

                                                    "Eu vou gozar!"

                                                    scene n3_premium7 with hpunch

                                                    pause

                                                    mc "A-ah!!!"

                                                    n "Assim mesmo, [mc]!"

                                                    mc "M-minha nossa... aah..."

                                                    n "Hmmm..."
                                                    scene nnew_ani33 with Dissolve(1.0)
                                                    mc "Essa foi... a mais intensa... da minha vida..."

                                                    n "Que bom..."

                                                    mc "Ai... você foi incrível."

                                                    n "Dá pra ver... mas agora é bom você se arrumar que eu escutei o Fabrício voltando pro balcão."

                                                    mc "O-opa!"

                                                    scene black with dissolve

                                                    scene n3_premium8 with Dissolve(1.0)

                                                    pause

                                                    n "Então gostou, né? Eu falei."

                                                    mc "Sorte que eu fui na sua... valeu à pena."

                                                    n "Eu tava te devendo uma... agora estamos quites, certo?"

                                                    mc "Eu preciso fazer você dever outra então."

                                                    n "Não me provoca que eu já tô quente pra caralho."

                                                    mc "V-vamo trocar de assunto então."

                                                    n "É melhor haha..."
                                                "Parar pora qui":


                                                    mc "Desculpa, mas não tenho coragem."

                                                    n "Poxa..."

                                                    n "Você provavelmente tá certo... eu que tô animado demais..."

                                                    mc "A gente vai ter nossa chance ainda."
                                        "É arriscado demais":


                                            mc "Você é uma delícia... mas eu não quero que ninguém pegue a gente."

                                            n "Você provavelmente tá certo... eu que tô animado demais..."

                                            mc "A gente vai ter nossa chance ainda."

                                    scene black with dissolve



                                    scene pub booth with Dissolve(1.0)

                                    mc envergonhado "Você me deixou sem ar... literalmente..."

                                    show nathan seduzido with Dissolve(1.0)

                                    n "E aí? Passei no teste?"

                                    mc "Com certeza."

                                    n "Você consegue fazer eu esquecer dos problemas. É como se minha cabeça ficasse toda vazia."

                                    mc charmoso "Que bom, [n]."

                                    "A minha relação com o [n] tá indo tão bem..."

                                    "Eu me sinto bem com ele. E desde o começo eu sinto que rola uma atração intensa entre a gente."

                                    "Eu acho que quero dar o próximo passo. Será que agora não é a hora de oficializar?"

                                    menu:
                                        "Pedir o [n] em namoro":


                                            $ nathan_pediu_namoro = True

                                            mc desculpa "[n]... você é um cara especial pra mim. Eu realmente me sinto bem quando tô contigo."

                                            mc charmoso "Igual você me disse àquela noite, eu também não quero parar nisso."

                                            mc "Você... quer namorar comigo?"

                                            n "[mc]?! Eu..."

                                            show nathan preocupado with dissolve

                                            n "Eu..."

                                            mc preocupado "O que foi?"

                                            n "Eu gosto muito de você. Eu sinto a mesma coisa que você..."

                                            mc "..."

                                            n "Só que... eu não tô pronto pra isso agora."

                                            mc desculpa "Não?"

                                            n "Nos próximos dias minha vida pode mudar completamente..."

                                            n "Não posso me comprometer com você e depois te deixar sozinho! Eu não me perdoaria."

                                            mc preocupado "[n]..."

                                            show nathan discutindo with dissolve

                                            n "Eu... prometo que vou resolver minhas coisas. E eu vou te responder."

                                            n "Por favor, me espere [mc]."

                                            mc charmoso "Claro. Nós vamos resolver esse problema juntos."

                                            mc "Você não tá mais sozinho."

                                            show nathan preocupado with dissolve

                                            n "Obrigado, [mc]. Desculpa puxar você pro meio desse rolo todo. Eu queria-"

                                            mc "Não precisa falar nada. Vamos resolver isso. Eu prometo."

                                            n "Ok..."

                                            show nathan seduzido with dissolve

                                            n "Você é o cara."

                                            mc envergonhado "Não é pra tanto."

                                            n "É, sim. Você é um sujeito especial. Isso não tem nada a ver com o que eu sinto por você. Você realmente é especial."

                                            mc "Deixe pra falar isso quando a gente resolver tudo."

                                            n "Combinado."
                                        "Não quero dar esse passo ainda":


                                            "..."
                                "Melhor hoje não.":


                                    mc "Desculpa, [n]. Mas acho que é melhor hoje, não."

                                    mc "Todo esse problema com você tá me deixando nervoso."

                                    n "Eu entendo, [mc]. Mas... não deixa isso acabar com nosso lance."

                                    mc "T-tá... obrigado."

                                    n "Eu que agradeço por você se preocupar comigo."
                        else:


                            mc "Não é pra tanto, cara."

                            n "É, sim. Você é um sujeito especial. Não sei explicar. O jeito que você parece aberto pra resolver o problema das pessoas."

                            n "Não sei... é como se você quisesse ajudar os outros sem pedir nada em troca."

                            mc "Deixe pra falar isso quando a gente resolver tudo."

                            n "Haha! Verdade. Mas mesmo que dê tudo errado. Você já é meu parça, [mc]."

                            mc "Valeu, [n]."

                            n "Eu que agradeço."
                    "Não falar nada":


                        mc "..."

                        n "..."

                "..."

                n "Bom... já tá ficando tarde. Acho que vou pra casa."

                scene pub geral with Dissolve(1.0)

                mc desculpa "Já?"

                show nathan preocupado with dissolve

                n "Esses dias eu tenho ficado bastante cansado."

                mc "Deve ser o stress. Descanse bastante. Vai fazer bem pra você."

                n "Pode deixar. Vamos nos falar mais depois."

                mc normal "Não se preocupe que vamos dar um jeito nisso. Qualquer coisa pode me ligar."

                n "Valeu. Até, [mc]."

                mc "Até."

                hide nathan with dissolve

                "..."

                show mc pensando with dissolve

                "Hmmm..."

                if cassia_e2_plano and n3_gravou:

                    "Ele saiu. E eu tenho tudo gravado aqui. Deve ser material suficiente pra [j]."

                    "Espero que eu tenha tomado a decisão certa."

                    "Vou entregar pra ela e espero que ela cumpra a parte dela do acordo."

                    "..."

                    jump nathan_e3_redacao

                elif cassia_e2_plano and not n3_gravou:

                    "Eu prometi pra [j] que ia gravar ele, mas na hora não consegui. Ela vai ficar uma fera."

                    "Ou seja, agora ela não vai mais querer ajudar ele. Vou ter que encontrar outra forma de resolver essa parada."

                    "O [n] é um bom cara. Ele não merece ser deportado agora que a vida profissional dele começou a dar certo."
                else:


                    "Agora que ele foi embora, o que eu posso fazer pra ajudar ele?"

                    if nathan_e3_beijo:

                        "Eu não quero que ele vá pra longe de mim de forma alguma."
                    else:


                        "Eu vou fazer alguma coisa pra evitar que ele seja deportado. Com certeza!"

                "Talvez..."

                "Ele disse alguma coisa sobre olhar as leis. Quem sabe eu possa dar uma estudada nisso e encontrar alguma brecha."

                "A Biblioteca Municipal fica no Museu de Arte Moderna. Ainda nem anoiteceu, se pá dá pra eu dar uma lida lá antes de fechar."

                "Não que eu seja advogado, mas pelo menos alguma luz..."

                "Perfeito! Bora lá!"

                jump nathan_e3_biblioteca

label nathan_e3_redacao:

    scene trabalho geral with Dissolve(1.0)

    "Não tem ninguém aqui na redação essa hora."

    "Devem tá tudo correndo atrás dos famosos. Coitados..."

    "Espero que a [j] esteja na sala dela."

    scene trabalho sala_cassia with Dissolve(1.0)

    mc serio "[j]? Ué..."

    "Não tá aqui?"

    "Opa. Parece que tô ouvindo algo."

    j "{size=17}Não se preocupe. Está tudo certo. Eu vou ficar de olho.{/size}"

    gi "{size=17}Isso é sério, [j]. Eu acho que eles conseguiram provas.{/size}"

    "O que será que tá rolando? Tem alguém conversando na cozinha."

    j "{size=17}Fique tranquilo. Eu estou esperta. Se aparecer alguma coisa eu dou meu jeito.{/size}"

    gi "{size=17}Eu confio em você. Só quero que você entenda a gravidade da questão.{/size}"

    j "{size=17}Eu entendo.{/size}"

    "..."

    "Eles pararam de falar. Vou aproveitar e fingir que tô chegando agora."

    scene trabalho geral with Dissolve(1.0)

    mc desconfiado "Alooou! Tem alguém aqui?!"

    j "Pombinho? Estou na cozinha."

    mc envergonhado "Opa. Vou aí."

    scene trabalho chefe_porta with Dissolve(1.0)

    mc "Olá."

    show cassia provocando with dissolve

    j "Boa tarde... mas já é praticamente boa noite."

    mc "Verdade."

    show cassia provocando at direita with move

    show gevanni ola with dissolve

    $ gi_nome = "Homem de terno"

    gi "Boa noite, jovem."

    if celeste_fotos:

        "Este homem... eu já vi ele antes..."

    show gevanni ola at esquerda with move

    $ gi_nome = "Gevanni"

    j "Este é o [gi]. Ele é o diretor financeiro do Banco Central."

    gi "Muito prazer. E você é?"

    if celeste_fotos:

        "É ele! O cara das fotos que a Celeste me entregou!"

    mc desculpa "Meu nome é [mcc]. O prazer é meu."

    gi "Não precisa ficar acanhado, [mc]. Sua fama está chegando até os ouvidos certos."

    mc desconfiado "Como?"

    gi "O pessoal do Banco já leu algumas de suas matérias. E esse é o tipo de amizade que você quer."

    mc envergonhado "Que bom..."

    j "O [gi], como diretor financeiro, possui um cargo diferenciado no banco. É uma boa amizade pra você."

    gi "Imagina o que faz o diretor financeiro dentro de um banco, né? Haha!"

    mc "Hehe..."

    gi "Caso você tenha uma grana sobrando e queira investir no mercado de ações, me procure."

    gi "Nada como aprender com o melhor."

    mc "Obrigado. Vou te procurar, sim."

    gi "Enfim, os assuntos que eu tinha para resolver agora estão resolvidos. Tenho que voltar ao trabalho."

    j "A essa hora?"

    gi "E tem hora pra trabalharmos?"

    j "Touché."

    gi "[j]. [mc]."

    hide gevanni with dissolve

    j "Vem pra minha sala."

    mc serio "Ok."

    scene cassia sentada_explicando with Dissolve(1.0)

    j "E aí? Gravou?"

    mc desculpa "Sim. Vou mandar pra você."

    "..."

    mc "Pronto."

    j "Tá aqui. Depois vou ouvir."

    mc serio "Agora quero saber se você vai cumprir sua parte da promessa."

    scene cassia sentada_rindo with Dissolve(1.0)

    j "Claro que eu vou, pombinho. Se esta gravação realmente contiver material relevante, farei minha parte."

    mc "É o que eu espero."

    j "Não precisa ficar assim. Enquanto você for meu aliado, você será muito bem recompensado."

    mc serio "Com isso resolvido, acho que vou dar o fora. Boa noite, [j]."

    scene trabalho geral with Dissolve(1.0)

    "Acho que hoje vou dormir cedo."

    if cassia_seducao:

        j "Ei. Pombinho."

        mc desconfiado "Oi?"

        scene cassia sentada_provocando with Dissolve(2.0)

        pause

        mc surpreso "!"



        j "Eu fico excitada quando meus garotos fazem as coisas direito. Quer a recompensa?"

        mc safado "Você quer fazer isso agora? Aqui na redação?"

        j "Por que não?"

        mc envergonhado "Mas e se alguém ver a gente?"

        j "E daí? O máximo que alguém vai fazer é bater uma pra gente transando."

        mc safado "..."

        mc "Então bora."

        j "Assim que eu gosto, pombinho. Vem logo."

        scene cassia redacao_mc_beijando with Dissolve(2.0)

        $ renpy.pause(delay=3, hard=True)

        pause

        j "Que tesão, pombinho! Me beija!"

        mc "..."

        j "Hoje a gente vai passar a noite toda aqui."

        mc "Não sei, não, Cássia... e se alguém pegar a gente? Você sabe que tem gente que fica até tarde aqui..."

        j "Isso, me aperta! Com força!"



        mc "Por que tá gritando?!"

        j "Qual o problema? Com medo de alguém saber? Você quer que eu tire minha roupa ou não?"

        mc "Você tá falando sério?"

        j "Claro... o que você quer? Diga 'sim' e eu tiro na hora. Você foi um bom garoto hoje... você merece."

        j "Se você prefere fazer rápido pra ninguém ver..."

        "Comer ela aqui como minha recompensa? Mas e se..."

        label ca3_premium2:

            pass

        menu:
            "Tira a roupa então.":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_11

                    jump ca3_premium2

                mc "Foda-se se pegarem a gente. Tira tudo."

                j "Haha... assim que eu gosto, pombinho. Arriscando tudo só pra provar minha doce bucetinha."

                mc "Eu fiz meu trabalho... agora eu quero minha recompensa."

                j "Toma ela aqui então."

                scene black with dissolve

                scene n3_premium23 with Dissolve(1.0)

                pause

                j "Gostou?"

                mc "Adorei... você tem o corpo perfeito."

                mc "Mas o que eu quero mesmo é poder entrar dentro desse pedaço de carne delicioso."
                scene nnew_ani11 with Dissolve(1.0)
                j "Eu consigo sentir seu tesão... aprecie um pouco."

                mc "Você brinca demais comigo. Eu quero ir pra parte boa logo."

                j "Então vai... tira ele pra fora e vem..."

                scene black with dissolve

                scene n3_premium24 with Dissolve(1.0)

                pause

                mc "Valeu... eu preciso disso."

                j "Ei, ei... calma, pombinho... ninguém deixou você fazer nada ainda."

                mc "Tá brincando?"

                j "Você vai ficar assim com um tempo... eu quero você bem duro antes de entrar..."

                mc "É minha recompensa! Deixa eu fazer logo!"

                j "Não, não... só quando eu mandar."

                "Até assim ela quer brincar comigo?!"

                menu:
                    "Ignorar ela e enfiar!":


                        "Eu quero minha recompensa agora!"

                        mc "Vou esperar o caralho! Toma, vadia!"

                        scene n3_premium26 with hpunch

                        pause

                        j "AAAIII!"

                        j "Vai meter assim na sua mãe, filho da puta!"

                        mc "É minha recompensa! Eu vou meter quando eu quiser!"
                    "Continuar esperando":


                        mc "Aahhhh..."

                        j "Sem vontade suficiente, você não vai me apreciar igual um animal."

                        j "E eu não sou uma transinha qualquer que você tem por aí... eu sou o prato principal, bebê."

                        mc "Cássia..."

                        j "Se ajeita, pombinho... vem mais pertinho..."

                        scene n3_premium25 with Dissolve(1.0)

                        pause

                        mc "Isso é um martírio!"

                        j "Quanto mais fome, mais gostosa a comida... nunca ouviu esse ditado?"

                        mc "Não! Agora deixa eu meter!"

                        j "Você merece... por ser um bom menino..."

                        mc "Aleluia!"

                        j "Só vai com cui-"

                        scene n3_premium26 with hpunch

                        pause

                        mc "AAAHH!"

                        j "AAIN!"

                j "Quanta vontade! Ainn! Eu gosto assim!"

                mc "Eu sei que você gosta!"

                j "Tá vendo como a vontade ajuda? Você parece um animal mesmo!"

                mc "Você que me trata igual um animal!"

                j "Vocês fazem por merecer... ahnnn..."

                mc "Que delícia!"

                j "Que bom que você tá se divertindo... enquanto você estiver sendo útil, é isso que eu tenho pra você."

                mc "Tá! Agora deixa eu me concentrar."

                j "Eu vou te ajudar... gemendo bem gostoso tá? Hmm..."

                mc "Você sabe provocar também, hein!? Ahn... Ser seu brinquedo também tem seus benefícios!"

                j "Ah... claro que tem, pombinho... hmm... muitos... deliciosos benefícios..."

                mc "Acho que eu já vô gozar!"

                j "Pode gozar, bebê! Essa noite é sua!"

                scene n3_premium26 with vpunch

                pause

                mc "Tá vindo!"

                j "Isso! NNGH!! Enche sua chefe de porra!"

                mc "Então geme pra mim!"

                j "HMM!! AAHNNN!!"

                mc "Isso! Tomaaa!!!"

                scene n3_premium26 with vpunch

                pause

                mc "AAGH! Aaahh!"

                mc "Ah..."

                j "Hmmm..."

                mc "Minha nossa... essa foi boa..."

                j "Eu sei que foi... é fácil de ver por essa carinha de anjo..."

                scene black with dissolve

                scene n3_premium30 with Dissolve(1.0)

                pause

                j "Me melou inteira, né?"

                mc "Sim... foi uma recompensa e tanto... obrigado..."

                j "Agora é hora de limpar sua bagunça."

                mc "L-limpar?"

                j "Você fez uma bagunça aqui, não fez? Agora tem que limpar..."

                mc "C-cássia... não sei..."

                j "Vem aqui... limpa minha buceta com sua língua... é sua porra mesmo..."

                "Por que tudo tem que ser assim com essa mulher?"

                j "Aproveita e faz sua chefe gozar..."

                j "Eu não vou aceitar um 'não' como resposta."

                "E agora?"

                menu:
                    "Fazer o que ela mandou":


                        mc "Sim, chefe... eu limpo você."

                        j "Excelente. Vem aqui, pombinho."

                        scene black with dissolve

                        scene n3_premium28 with Dissolve(1.0)

                        pause

                        j "Hmmm... assim mesmo, querido. Mete essa língua."

                        mc "{i}slhip{/i}"

                        j "Deixa ela limpinha! Nnnghh... essa sensação é incrível."

                        mc "..."

                        j "Não fui eu que mandei você gozar tanto... apesar que é minha culpa, né? Por ser gostosa assim."
                        scene nnew_ani12 with Dissolve(1.0)
                        j "Nnnghh.. não importa... só continua assim..."

                        j "Ah... tá mais gostoso do que eu imaginava!"

                        j "Você é bom pra caralho com essa língua, [mc]!"

                        mc "Mhmmm!"

                        j "Isso! Acelera agora!"

                        scene n3_premium29 with Dissolve(1.0)

                        pause

                        j "Assim mesmo! Vai! HMMM!"

                        mc "MMM!!"

                        j "Isso! Assimmm! NNNGH! AIII!"

                        j "Enfia! NNGHH!"

                        j "Mais um pouco! Limpa mais um pouco! AAHH!"

                        j "AAAHHHHH!!!"

                        scene n3_premium29 with vpunch

                        j "Tô gozando, caralho!!!"

                        mc "!"
                        scene nnew_ani15 with Dissolve(1.0)
                        j "Aah... aahh..."

                        mc "Gozou mesmo?"

                        j "Sim... foi rápido... toda essa situação acabou me excitando..."

                        mc "Ok..."

                        j "Excelente... agora pode ir... tenho que voltar logo pra casa."

                        mc "Boa noite."

                        j "..."

                        scene black with Dissolve(3.0)
                    "Sair correndo":


                        mc "Agora não dá! Valeu!"

                        scene black with hpunch

                        j "Ei! Volte aqui, mocinho! Eu não deixei você sair!"

                        mc "Já saí!"

                        j "Criança mimada do cacete!"
            "Vamo terminar isso rápido!":


                mc "Sem enrolação! Só vem aqui!"

                j "Hahaha! Então me come!"

                scene black with Dissolve(1.0)

                j "Assim! AAH!"
            "Não quero recompensa.":


                mc "O que aconteceu aqui já tá bom demais. Eu tenho que ir."

                j "Não quer sua recompensa? Haha! Faça o que quiser, pombinho!"

                scene black with Dissolve(1.0)

        $ tempo = 4

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cassia_e2_seducao","cassia","personagem")

    jump nathan_e3_finalizar

label nathan_e3_biblioteca:

    $ visitou_museu = True

    scene cidade onibus with Dissolve(1.0)

    "Eu fui uma vez só no museu... justamente quando eu precisava de um livro da biblioteca prum lance da faculdade."

    call cena_onibus from _call_cena_onibus_1

    "Opa. Acho que é aqui."

    scene centro museu with Dissolve(3.0)

    pause

    "O museu é incrível. É o maior do país e está cheio de obras famosas de todas as partes do mundo."

    "Com certeza eu preciso trazer alguém especial aqui um dia."

    "Mas hoje não dá tempo. Tenho que ir direto pra biblioteca antes que ela feche."

    "..."

    scene biblioteca geral with Dissolve(2.0)

    "Uou. Tinha esquecido como ela era gigante."

    "Fico pensando quantos milhares de livros cabem em dois andares..."

    "Hmmm... não tô vendo ninguém. Certeza que não vou encontrar um livro específico sem ajuda."

    "Deixa eu ver no segundo andar."

    "..."

    scene biblioteca carol_pegando with Dissolve(2.0)

    pause

    "?"

    mc desconfiado "Hm?"

    "Tem uma garota tentando pegar o livro."

    mc zerado "Deixa eu ajudar..."

    mc normal "Com licença. Qual livro você quer pegar?"

    o "Este de capa amarela."

    mc "Opa."

    mc normal "Tá na mão."

    scene biblioteca 2andar with Dissolve(1.0)

    o "É..."

    show 4olhos nervosa with dissolve

    o "O-obrigada. Desculpa..."

    if v12_fim:

        "Espera... da onde eu conheço essa menina? Quase certeza que eu já vi ela em algum lugar."

        "E esse uniforme... Enfim!"

    mc normal "Não tem o que se desculpar. Olha. Você por acaso trabalha aqui?"

    show 4olhos ola with dissolve

    o "Si-sim. Eu sou responsável pela biblioteca na parte da tarde."

    mc "Legal. Você poderia me ajudar a encontrar um livro?"

    o "Claro. Qual livro?"

    mc desculpa "Na verdade eu não sei hehe... Preciso de algum livro que fale sobre as leis."

    o "É... existem centenas de livros sobre leis. O senhor tem algo mais específico em mente?"

    mc envergonhado "Ah! Um livro sobre as leis de imigração. Não sei se isso existe."

    show 4olhos ola with dissolve

    o "Com certeza. Acho que existem 3 livros especializados em leis migratórias. Eu vou pegar para o senhor."

    o "Sorte que esses ficam na prateleira de baixo."

    mc normal "Hehe..."

    hide 4olhos with dissolve

    "Garota simpática."

    if not nathan_beijo:

        mc tarado "Talvez valha a pena eu começar a ler um pouco mais..."

        show 4olhos ola with dissolve

        o "Como é?"

        mc surpreso "Na-nada não!"
    else:


        show 4olhos ola with dissolve

        o "Voltei."

    o "Aqui está."

    mc normal "Muito obrigado."

    o "Não precisa agradecer. Boa leitura."

    hide 4olhos with dissolve

    "Certo..."

    scene biblioteca mc_lendo with Dissolve(2.0)

    "Caraca... tem uma pá de coisa aqui."

    "..."

    "..."

    "AAAAAAH!"

    "Já cansei..."

    mc zerado "Não vou conseguir ler nada hoje."

    "Acabei vindo aqui à toa. Bom, pelo menos agora eu sei quais são os livros."

    "Vou voltar depois com mais tempo e ler tudo com bastante calma."

    "Eu vou descobrir uma forma de ajudar o [n]. Eu preciso fazer isso."



    "???" "Hmm... ah..."

    "Que barulho é esse?"

    "???" "Aaah..."

    "Parece alguém... gemendo?"

    label n3_premium3:

        pass

    menu:
        "Procurar de onde vem o gemido":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_12

                jump n3_premium3

            "De onde veio isso? Será que alguém precisa de ajuda?"

            "Impossível... mas pode ser... sacanagem..."

            scene black with dissolve

            scene biblioteca 2andar with Dissolve(1.0)

            "Não tem ninguém aqui essa hora... só eu e..."

            "Então será que é ela?!"

            "???" "Ahn!"

            "Tá vindo daquí..."

            mc surpreso "!!!"

            scene black with dissolve

            scene j6_new9 with Dissolve(1.0)

            o "Aahnn... hmm..."

            "É ela mesmo! Não acredito!"

            o "Ah... ela não pode fazer aquilo... que eu fico... hmm..."

            o "Eu preciso de alguém urgente... pra não ficar assim... aaah..."

            o "Hmm..."

            o "Só de pensar... aah... que tem alguém... hmm..."

            o "Aah... alguém aqui... lendo... aah... enquanto eu... me toco..."

            o "Minha nossa... aahnnn..."

            o "Eu preciso... preciso chegar lá... nnnghh!"

            scene j6_new10 with Dissolve(1.0)

            "Não acredito... aqui onde qualquer pessoa pode ver..."

            "Parece que as pessoas precisam ler mais nesse país mesmo... não tem uma alma penada... além de mim, claro..."

            "Hehe... a sede de conhecimento foi recompensada hoje..."

            o "É errado... mas é tão bommm... hmm..."

            o "Mais um pouquinho! Aaiin..."

            o "Só mais um tantinho e eu tô livre dessa sensação! MMNNNHH!!"

            o "Por favor, não ouça! Não me ouça gozando!!!"

            scene j6_new10 with vpunch

            o "aAaAHHH!"

            o "Ah... aah..."

            o "T-tenho que me arrumar u-urgente!"

            "Opa! É minha deixa!"
        "Deixa eu sair daquí":


            "Isso não tem nada comigo..."

    scene black with Dissolve(1.0)

    "Agora bora pra ilha que já tá escurecendo."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("nathan_e3_biblioteca","cassia","personagem")

    $ tempo = 3

    jump nathan_e3_finalizar

label nathan_e3_finalizar:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v14_fim","nathan","personagem")

    $ dia_cassia = dia + 2
    $ v14_fim = True

    jump call_cidade

label nathan_evento4:

    label nathan_cel_msg3_resposta:

        $ nathan_cel_msg3_resposta = True

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n4_save", extra_info="n4_save")

    $ iconchefe += 1

    "Caraca. Já chegou o dia da audiência do [n]. O tempo passou voando."

    scene ape_tv with Dissolve(1.0)

    if n3_gravou:

        "Eu gravei nossa conversa e passei pra [j]. Ela disse que ia ajudar ele com isso."

        "Tá na hora de eu cobrar essa ajuda dela."

        "Será que eu fui idiota acreditando nela? O que ela pode fazer nesse caso?"

        "Se ela só rir da minha cara eu nunca mais vou aceitar nada que ela oferecer. A [j] que vá pro inferno."
    else:


        "Sem a ajuda da [j], vou ter que arranjar um jeito de salvar o [n] sozinho."

        "Aqueles livros que eu encontrei na biblioteca talvez sejam o que eu preciso."

        "Só que é claro que ele tem o advogado dele que vai saber muito mais do que eu, né. Sei lá, mano..."

        "Eu sou um jornalista... não sou advogado. Será que perder tempo lendo livros sobre lei é a melhor forma de ajudar?"

        "Que merda..."

        "Se a [j] não fosse uma DESGRAÇADA talvez ela pudesse ajudar... Mas não dá pra contar com aquela mulher."

    play sound "audio/som_34_news.mp3"

    mc "Ah?!"

    show tv apresentador with dissolve

    "Apresentador" "Estamos de volta e agora uma notícia estarrecedora."

    "Apresentador" "O modelo em ascenção [nc] que tem estampado diversos outdoors pela capital está ilegalmente no país."

    "Apresentador" "A informação foi publicada primeiramente no site de uma revista."

    "Apresentador" "[n] mudou-se muito cedo para o país, e a situação acabou se resolvendo com o tempo."

    "Apresentador" "Entretanto, a matéria trouxe à tona o problema legal do modelo."

    if n3_gravou:

        "Apresentador" "Uma das repórteres da Faux News teve acesso a uma gravação exclusiva onde o modelo fala sobre como está se sentindo."

        "Apresentador" "Vamos ouvir."

        n "... pior é que não posso contar com ninguém. Não posso falar com meus amigos do trabalho."

        n "Isso pode se virar contra mim. Se os diretores- descobrem isso, meu contrato pode ir pro saco."

        n "Nem sei como ainda não me chamaram..."

        n "... eu sinto que a qualquer hora isso vai explodir e acabar com a minha vida."

        n "Preciso resolver isso sozinho. Isso que é o pior. Vou ter que saber mais sobre as leis e como regularizar minha situação."

        "Apresentador" "A situação realmente parece estar mexendo com os nervos do jovem."

    "Apresentador" "Uma audiência foi marcada para o dia de amanhã. Ela será fechada para o público."

    "Apresentador" "A juíza designada para o caso é a meretíssima [eli] Richter."

    show juiza_close2 with dissolve

    "Apresentador" "A juíza é conhecida por sua postura firme e por evitar ao máximo a vida pública."

    "Apresentador" "Ela ficou famosa após a decisão que tornou possível o impeachment do ex-prefeito da capital Stefano Donatello."

    "Apresentador" "Desde então, Richter evita ao máximo conceder entrevistas e aparecer publicamente."

    hide juiza_close2 with dissolve

    "Apresentador" "A Faux News esta pronta para trazer o desenvolvimento da história para nossos telespectadores."

    play sound "audio/som_34_news.mp3"

    "Apresentador" "No próximo bloco: a história do flanelinha que se tornou multimilionário investindo C$ 5 no Cassino do Barão."

    "Vinheta" "{b}Faux News: Nós somos a Notícia de Verdade{/b}"

    "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

    hide tv apresentador with dissolve

    "Aconteceu... finalmente todo mundo sabe da situação do [n]."

    if n3_gravou:

        "E eles ainda conseguiram a gravação que eu fiz do [n]!! Como?!"

        "Só a [j] tinha esse material. Será que ela passou pra eles?"

        "Mas por que?"

        "Que estranho..."

    "Eu tenho que fazer alguma coisa... não posso deixar ele na mão agora."

    if n3_gravou:

        "A [j] vai ter que me ajudar. Ela prometeu."
    else:


        "Mesmo não tendo aceitado os rolos da [j], acho que não custa nada tentar."

        "Talvez pelo menos me dar uma dica."

    "Ela deve tá na redação agora."

    scene black with Dissolve(1.0)

    play sound "audio/som_35_passos.mp3"

    scene trabalho angulo with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene trabalho sala_cassia with Dissolve(1.0)

    mc desconfiado "[j]?"

    show cassia provocando with dissolve

    j "Como vai, pombinho?"

    mc zerado "Ainda me chamando assim?"

    if n3_gravou:

        j "Ouviu sua gravação? Acabou de sair no FNews das-"

        mc serio "Ouvi, sim... Pra isso que você queria a gravação? E por que raios você daria pra eles e não pra revista?"

        scene cassia sentada_rindo with dissolve

        j "Ainda tem muita coisa que você não entende, pombinho..."

        mc "Foda-se."

        j "Talvez, quando você crescer, você seja chamado pra fazer parte do clube."

        menu:
            "Que clube?":


                mc desconfiado "E que clube é esse?"

                j "Clube dos adultos... do qual você ainda não pode fazer parte."

                j "Mas talvez sua hora ainda chegue. Você tá indo bem, de verdade. Está chamando a atenção."

                mc "Eu?"

                j "Mas não se ache muito. Ainda é só o começo pra você."
            "Não quero fazer parte desse clube.":


                mc "Não sei se quero fazer parte disse seu clube."

                j "Ainda é cedo pra você decidir uma coisa dessas. Espere mais um pouco."

                mc "..."

        mc bravo "Você disse que ia ajudar o [n] se eu fizesse a minha parte. Vim cobrar sua ajuda."

        scene cassia sentada_explicando with Dissolve(1.0)

        j "Sim, eu disse. Mas não sei se você merece."

        mc bravo "Como assim?! Eu fiz minha parte!"

        j "Ninguém obrigou você a fazer. Eu coloquei uma arma na sua cabeça? Não."

        mc serio "Eu acreditei em você..."

        j "Porque quis..."

        mc bravo "Desgraçada..."

        scene cassia sentada_rindo with dissolve

        j "Calma, pombinho... eu estou brincando com você."

        j "Eu já disse pra você mais de uma vez... apenas coisas boas esperam os amigos de [jc]."

        mc desconfiado "E então?"

        j "Você sabe que a juíza do caso do bobinho é a tal da [eli]."

        mc serio "Sim, eu vi no noticiário."

        j "Acontece que eu tenho uma foto dela fazendo algo... no mínimo comprometedor."

        mc preocupado "Quê?!"

        mc "Você quer que eu ameaçe a juíza do caso dele?!"

        mc angustiado "Você é louca?!"

        scene cassia sentada_foto with dissolve

        j "Uma imagem vale mais do que mil palavras, benzinho."

        j "Se essa foto vir à público, a vida da m e r e t í s s i m a acabou."

        j "Tome."

        mc preocupado "Opa."

        show juiza_bdsm1 with vpunch

        pause

        mc surpreso "!"

        "É-é-é a mulher que apareceu hoje na TV!"

        if not stifler_conheceu:

            "Que que tá acontecendo aqui?!"

            "Essas roupas, esse lugar! Isso aqui é muito mais do que comprometedor!"

            "Isso pode acabar com a vida de qualquer um!"
        else:


            "Ela tá no Distrito!"

            "E essa ajoelhada é a [ce]!"

            "Essas roupas, esse lugar! Isso aqui é muito mais do que comprometedor!"

            "Isso pode acabar com a vida de qualquer um!"

        mc surpreso "E-essa!"

        mc "Não acredito nisso..."

        j "Esta é uma cartada e tanto. Espero que você se lembre de quem fez isso por você."

        mc "..."

        hide juiza_bdsm1 with dissolve

        mc desculpa "Coagir uma juíza... não sei se eu quero fazer isso..."

        scene cassia sentada_irritada with vpunch

        j "Não seja idiota, [mc]!"

        j "Eu tô te dando a chance de salvar o bonitinho lá. Não vai jogar isso no lixo, ouviu!?"

        j "Você me cansa! Sai fora!"
    else:


        j "Não é esse seu nome?"

        mc bravo "..."

        mc serio "Eu vi no noticiário hoje o caso do [n]."

        j "Tem razão. A Faux News usou minha informação. Agora vai ficar bem mais complicado pro bonitinho."

        mc desculpa "Pois é... olha... eu sei que eu não tô sendo o mais fiel dos aliados, mas você não tem algo que possa ajudar?"

        scene cassia sentada_rindo with dissolve

        j "Interessante..."

        j "Você devia ter pensado melhor antes de ter se aliado ao bonitinho ao invés de fazer o que eu quero."

        mc "Eu sei, ma-"

        j "Eu já te disse que os amigos de [jc] têm tudo. Agora... os inimigos..."

        scene cassia sentada_irritada with vpunch

        j "Não tem PORRA NENHUMA! Agora sai fora!"

    scene trabalho angulo with hpunch

    mc angustiado "Calma!"

    mc envergonhado "Caraca... ela pistolou mesmo."

    mc desconfiado "E agora? O que eu faço?"

    if sofia_e1 != "nada":

        show sofia seria with dissolve

        w "[mc]?"

        mc envergonhado "Oi, [w]."

        w "Brigou com a [j]?"

        mc "Parece que sim..."

        show sofia falando with dissolve

        w "Hmmm..."

        mc desconfiado "?"

        w "É..."

        mc "?!"

        show sofia ironica with dissolve

        w "Tem... alguma coisa que eu possa fazer por você?"

        mc "Você? Xeretando?"

        show sofia falando with hpunch

        w "Não estou xeretando!"

        w "Só quero tentar melhorar o humor da redação, só isso..."

        mc envergonhado "Obrigado..."

        mc "Olha. Você já ouviu falar da juíza [eli]-"

        show sofia explicando with dissolve

        w "Claro. Ela é um exemplo para todas as mulheres."

        mc desconfiado "Exemplo?"

        w "Com certeza! A meretíssima é conhecida pela sua incrível postura profissional. É uma honra ver ela trabalhando."

        if n3_gravou:

            "Uma honra, é? Se ela soubesse o que essa mulher faz nas horas vagas..."

        mc desculpa "Entendo."

        w "Agora ela tá com o caso daquele modelo [nc]. Tenho certeza que ela vai conduzir o caso com maestria."

        mc envergonhado "Espero que sim..."

        show sofia seria with dissolve

        w "Falei demais... Bom trabalho, [mc]."

        mc normal "Até."

        hide sofia with dissolve

        "..."

        "Pra [w] gostar assim de alguém... essa [eli] deve ser incrível mesmo..."

    if n3_gravou:

        "Mas o que pensar então daquela foto?"

        "Será que tá certo eu fazer isso?"

    "Talvez... se eu for até o fórum eu possa falar com ela. Explicar o lance do [n]."

    "Se ela entender a situação, vai ser bem melhor..."

    "Ou ela pode só me prender por querer influenciar na decisão de um juíz."

    mc zerado "O que eu faço?"

    "Acho que eu já me perguntei isso..."

    scene black with Dissolve(1.0)

    play sound "audio/som_35_passos.mp3"

    scene cidade onibus with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    "O fórum fica no mesmo prédio da prefeitura, lá na parte continental."

    "É estranho que o fórum e a prefeitura fiquem no mesmo lugar. Eu acho que isso não é normal... ainda mais pra uma cidade do nosso tamanho."

    "Sei lá."

    call cena_onibus from _call_cena_onibus_2

    scene cidade centro9 with Dissolve(1.0)

    "A prefeitura... o castelo da dinastia Donatello."

    "Parece que nem a prisão do Stefano reduziu o poder da família. Nada acontece na cidade sem a aprovação deles."

    "Tomara que eu encontre a juíza aqui."

    play sound "audio/som_35_passos.mp3"

    $ renpy.pause(delay=1, hard=True)

    scene prefeitura geral with Dissolve(1.0)

    pause

    "É a primeira vez que eu venho na prefeitura. O lugar é bem cuidado, isso eu tenho que admitir."

    "Será que o prefeito anda por aqui normalmente?"

    "Ele deve ter um jatinho prefeitural e muitos seguranças e uma comitiva... de assassinos."

    "Que merda eu tô pensando? Assassinos?"

    "Bom... E agora?"

    scene prefeitura detector with Dissolve(1.0)

    "Opa. Acho que eu tenho que passar pelo detector de metais ali."

    "Às vezes eu penso se essas merdas realmente servem pra alguma coisa ou é só pra dar uma sensação falsa de segurança."

    "Tem um guarda ali."

    scene prefeitura guarda with dissolve

    "Guarda" "Boa tarde, senhor."

    mc normal "Boa."

    "Guarda" "Algum objeto de metal?"

    menu:
        "Sim.":


            mc normal "Sim."

            "Guarda" "Pode colocar aqui então."

            mc desconfiado "..."

            "Guarda" "..."

            mc envergonhado "Na verdade eu não tenho nada."

            "Guarda" "..."
        "Não.":


            mc normal "Não."

            "Guarda" "Tudo bem."

    "Guarda" "Então pode passar."

    "..."

    play sound "audio/som_35_passos.mp3"

    $ renpy.pause(delay=1, hard=True)

    scene prefeitura geral2 with Dissolve(1.0)

    "Sorte que o treco não apitou."

    "Deixa eu ver agora..."

    "Parece que o fórum fica pra esquerda. Bora lá."

    play sound "audio/som_35_passos.mp3"

    $ renpy.pause(delay=1, hard=True)

    scene tribunal geral with Dissolve(1.0)

    "Uou!"

    "Então a audiência vai acontecer aqui amanhã."

    "Tá tão vazio. Tão quieto..."

    "O lugar parece ainda mais assustador quando a gente olha desse jeito."

    "Bem que ela poderia só apa-"

    scene tribunal geral with hpunch

    "???" "Ei!"

    show juiza cel with dissolve

    "???" "..."

    if n3_gravou:

        show juiza_bdsm1 with Dissolve(0.5)
        hide juiza_bdsm1 with Dissolve(0.5)
    else:


        show juiza_close2 with Dissolve(0.5)
        hide juiza_close2 with Dissolve(0.5)

    mc surpreso "[eli] Richter!"

    eli "Quê? Quem é você?!"

    menu:
        "Por favor, me desculpe!":


            mc angustiado "Por favor, perdão! Não queria gritar."

            show juiza excitada with dissolve

            eli "Tenha calma, jovem. Eu não vou te açoitar por isso..."

            mc envergonhado "Obrigado, senhora juíza."

            eli "Hmm..."
        "Ops. Meu nome é [mc].":


            mc charmoso "Ops. Meu nome é [mc]. Muito prazer."

            eli "Com licença."

            mc preocupado "Não, espere!"

            eli "?"

    mc envergonhado "Que bom que eu encontrei a senhora."

    eli "Hm?"

    mc desculpa "Eu queria falar algo muito importante com a senhora. Sobre um amigo meu."

    mc "Na verdade, é um caso que a senhora vai comandar... é comandar que fala? Amanhã..."

    mc preocupado "Desculpa, é que eu fiquei meio nervoso."

    show juiza rindo with dissolve

    eli "..."

    mc desconfiado "..."

    eli "Você tá parecendo uma criança que faz algo de errado e tá com medo de apanhar da mãe."

    eli "Respire fundo e fale de novo."

    mc envergonhado "Haha... ok."

    mc desculpa "É que você será a juíza de um julgamento amanhã e é algo que envolve alguém que eu conheço."

    show juiza incomodada with dissolve

    eli "Jovem, não posso falar sobre casos dessa forma."

    mc triste "Mas é que-"

    eli "É o caso do [nc], certo?"

    mc desculpa "S-sim..."

    eli "..."

    eli "Este não é meu primeiro caso envolvendo um famoso. Eu sei que é complicado para os fãs quando eles descobrem."

    eli "Celebridades são como modelos para pessoas. Eles são verdadeiros influenciadores e portanto têm responsabilidades."

    eli "Em um mundo em que cada vez mais vemos o surgimento de influenciadores de nicho, mais complicado é escolhermos referências."

    mc desculpa "Eu não sou apenas um fã. Eu sou um amigo e só quero que a justiça seja feita."

    eli "..."

    "Eu sinto que a paciência dela tá acabando..."

    if n3_gravou:

        "Não queria usar as fotos, mas será que é o único jeito?"

        "O que ela vai fazer comigo se minha ameaça sair pela culatra?"

        "Talvez eu devesse guardar esse cartucho por enquanto..."

    menu:
        "Por favor! Só me escute. Eu imploro!":


            $ n4_juiza = "implorou"

            mc angustiado "Eu sei que só pareço uma criança, mas por favor!"

            mc preocupado "Não quero atrapalhar a senhora! Só qu-"

            show juiza excitada with dissolve

            eli "Você implora de uma forma tão linda..."

            eli "Posso ver o quanto você realmente se importa com isso."

            eli "Tudo bem."

            mc surpreso "Sério?!"

            eli "Eu permito que você me acompanhe até minha sala. Você terá alguns minutos para me explicar tudo."

            mc feliz "Perfeito! Muito obrigado, senhora juíza!"

            eli "..."
        "Eu sou um jornalista e queria saber mais sobre seu trabalho.":


            $ n4_juiza = "jornalista"

            mc envergonhado "É que na verdade eu sou um jornalista e estou cobrindo esse caso."

            mc normal "Gostaria de saber mais sobre o caso pelos seus olhos. Conhecer você melhor antes do julgamento."

            show juiza cel with dissolve

            eli "Então é isso. Tudo bem."

            eli "Pode me acompanhar até minha sala. Você terá alguns minutos para fazer suas perguntas."

            eli "Mas obviamente não podemos falar sobre o caso de amanhã. E você também não pode gravar ou citar nenhuma de minhas falas."

            eli "Eu não gosto de visibilidade midiática."

            mc charmoso "Perfeito. Como a senhora quiser."

        "Eu tenho uma foto que a senhora gostaria de ver" if n3_gravou:

            $ n4_juiza = "ameaca"

            mc tarado "Eu quero falar algo com a senhora que tenho certeza que é do seu interesse."

            show juiza brava with dissolve

            eli "Hm? Não estou gostando do seu tom! Do que você está falando?"

            mc tarado "É algo que diz respeito à sua vida privada. Acho que a senhora deveria arranjar um tempo pra isso."

            eli "Como assim?!"

            mc tarado "Vamos pra sua sala e eu te explico."

    eli "Venha."

    hide juiza with dissolve

    mc normal "Estou logo atrás."

    play sound "audio/som_35_passos.mp3"

    $ renpy.pause(delay=1, hard=True)

    scene sala_juiza geral with Dissolve(2.0)

    pause

    if n4_juiza == "ameaca":

        show juiza brava with dissolve

        eli "E então? O que você quer me mostrar que é sobre minha vida?"

        mc tarado "Primeiro de tudo, quero que saiba que não tenho nada contra a senhora."

        mc "Só quero garantir que a audiência tenha um resultado positivo pra ele amanhã."

        eli "Abre a boca!"

        mc bravo "Ai!"

        jump nathan_e4_ameaca

    "Que sala incrível."

    "É tipo a sala do chefe, só que decorada com bom gosto."

    show juiza excitada with dissolve

    eli "É aqui onde recebo advogados e decido o futuro de tantas pessoas."

    if n4_juiza == "implorou":

        eli "Ver você implorando pelo seu amigo mexeu comigo."

        eli "Eu costumo prestar bastante atenção nos olhos dos culpados, mas poucos possuem uma energia como a sua."

        mc desculpa "É que eu realmente quero poder ajudar ele."

        eli "Entendo..."
    else:


        eli "Então você está escrevendo uma matéria sobre o caso do modelo [nc] e deseja saber o meu lado também."

        mc normal "Isso."

        eli "Eu posso falar um pouco sobre como é sentenciar esses pobres coitados e coitadas que não cumprem a lei."

        eli "É um trabalho difícil, mas é a vocação da minha vida. Eu faço com muito... gosto."

    eli "Vamos sentar aqui."

    mc envergonhado "Ok."

    scene sala_juiza poltronas with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene juiza sofa1 with Dissolve(1.0)

    eli "Antes de mais nada, deixa eu te explicar uma coisa."

    eli "É importante que você saiba que meu trabalho é garantir que a Justiça seja encontrada em meio a uma miríade de versões."

    mc desconfiado "Não sei se entendi."

    eli "Trocando em miúdos, quando uma acusação chega para mim, existem dois lados. Cada um com sua visão sobre o ocorrido."

    scene juiza sofa2 with dissolve

    eli "Normalmente o público só quer comprovar seus preconceitos. Se eles acham que alguém é culpado, eles só esperam que o juíz corrobore isso."

    eli "No entanto, é minha responsabilidade garantir a lisura do processo. Não adianta dar um 'jeitinho' pra garantir o resultado que você quer."

    eli "O juíz que vai pela vontade das pessoas não passa de um fraco! O respeito à Lei e ao processo é o que garante uma sociedade justa."

    scene juiza sofa1 with dissolve

    eli "Por outro lado, o juíz também não pode se dobrar perante outros poderes. Juíz não pode ter medo de autoridade."

    mc "Nem do prefeito ou presidente, sei lá?"

    eli "Óbvio que não."

    eli "O Poder Judiciário é autônomo e existe como fiscalizador dos outros poderes."

    eli "Juíz não pode ter medo de político. Também não pode escolher partido ou defender um grupo político específico."

    eli "Vou além! Juíz não pode ter amigo ou inimigo quando vai julgar. Todas as decisões devem ser feitas estritamente perante o rigor da Lei."

    "Uou... essa mulher parece incrível mesmo."

    "Ela fala sobre aplicar a lei com muito rigor."

    "Acho que não vai ser possível convencer ela de nada... O que vai ser do [n]?"

    if n3_gravou:

        "Talvez... a única forma seja ameaçar ela com as fotos..."

        "Mas será que ela vai cair nessa? Olha pra essa mulher..."

    scene juiza sofa3 with dissolve

    eli "Na corte, o poder do juíz é supremo."

    eli "Eu sou o poder máximo e todos precisam obedecer o que eu determino..."

    eli "Hmmm..."

    mc desconfiado "?"

    "O que foi isso?"

    mc envergonhado "Tudo bem?"

    eli "Claro."

    eli "Falar sobre a prática da magistratura me deixa... feliz."

    "Tem alguma coisa estranha com essa mulher."

    eli "Como é seu nome mesmo?"

    mc normal "Ah. É [mc], senhora."

    eli "Sei... o que você acha de mim após ouvir sobre a prática?"

    mc surpreso "Ah!"

    mc envergonhado "É..."

    "Acho que eu tô começando a entender essa mulher."

    mc charmoso "É incrível a quantidade de poder que a senhora tem. Você pode decidir o futuro de tantas pessoas."

    scene juiza sofa4 with dissolve

    eli "Siimm..."

    eli "Eu posso decidir o futuro de todos essas pessoas. Elas não têm o que fazer, além de aceitar o que eu mando."

    mc envergonhado "A senhora gosta desse sentimento?"

    eli "Eu adoro. Quando eu olho para as carinhas delas, encurraladas, prontas para verem suas vidas tomarem um rumo drástico."

    eli "Eles ficam... tão... lindos..."

    scene juiza sofa3 with dissolve

    eli "Acho que eu fugi um pouco do tópico. Perdão..."

    "E-essa mulher..."

    "Tem alguma coisa errada com essa mulher. Eu sinto que ela tá mostrando um lado diferente aos poucos."

    if n3_gravou:

        "E deve ter algo a ver com a foto que a [j] me deu."

    "Mas antes tenho que ter certeza do que é."

    mc envergonhado "Eu achei bem... interessante a forma como a senhora falou."

    mc "Você parecia tão poderosa. E é incrível ver uma mulher assim."

    eli "Você realmente gosta disso?"

    scene juiza sofa4 with dissolve

    label n4_juiza_pergunta:

        eli "Se sente... bem... perto de uma mulher poderosa?"

    menu:
        "Sim.":


            mc envergonhado "Sim. Ver uma mulher assim mexe comigo."

        "Não." if n4_juiza_pergunta:

            "Acho que eu saquei a dela. Ela quer realmente fazer isso comigo?"

            "De jeito nenhum. Eu não vou ser um brinquedo dela."

            "Só que..."

            call n4_juiza_recusou from _call_n4_juiza_recusou

        "O que a senhora quer dizer com isso?" if not n4_juiza_pergunta:

            $ n4_juiza_pergunta = True

            mc envergonhado "O que a senhora quer dizer com isso?"

            eli "Você sabe muito bem o que quero dizer, mocinho."

            eli "Eu vejo nos seus olhos envergonhados. No seu olhar desviado."

            eli "Você gosta quando uma mulher assume o controle?"

            mc "..."

            eli "Vou perguntar de novo..."

            jump n4_juiza_pergunta

    eli "Sério?"

    mc "Sim... senhora."

    eli "Hmmmm..."

    eli "Não posso negar que você é um jovem interessante."

    eli "Você parece saber seu lugar. É comportado. É... um bom garoto."

    eli "Você é um bom garoto, [mc]?"

    "Essa mulher realmente tá perguntando isso de verdade? O que ela espera que eu responda?"

    "Parece que ela tá mudando... não sei explicar. Parece que ela tá me testando."

    menu:
        "Não sei se entendi...":


            "Essa mulher é louca? Ela espera que eu responda essa pergunta?"

            call n4_juiza_recusou from _call_n4_juiza_recusou_1

            mc envergonhado "É..."
        "E-eu sou um bom garoto.":


            mc envergonhado "E-eu..."

    mc "Eu sou um bom garoto..."

    eli "Assim que se fala. Você é um garoto muito comportado."

    "..."

    eli "Ops. Acho que eu deixei cair meu sapato. Você pode pegar pra mim?"

    mc desconfiado "Âh?"

    eli "Meu sapato, [mc]. Vem aqui pegar. Você é um bom garoto, não é?"

    "Eu vou realmente fazer isso?"

    menu:
        "Sim, senhora juíza.":


            mc envergonhado "Si-sim, senhora juíza."
        "Não. De jeito nenhum":


            "Eu não vou ser o 'bom menino' dessa mulher!"

            "Mas se eu não fizer o que ela tá falando..."

            call n4_juiza_recusou from _call_n4_juiza_recusou_2

    eli "Muito bem, [mc]. Você está entendo."

    mc desculpa "Tá aqui seu sapato, senhora."

    eli "Hmmmm!"

    eli "Tá ficando quente aqui. Meu paletó tá quente demais."

    mc envergonhado "É?"

    scene juiza sofa5 with Dissolve(1.0)

    pause

    eli "Você tá fazendo sua senhora muito feliz."

    mc desculpa "Tá aqui."

    eli "É assim que se fala?"

    mc "Seu sapato, se-senhora..."

    eli "Agora, sim. Ver você ajoelhado assim tá me deixando louca, [mc]."

    eli "Meu novo bonequinho..."

    eli "Está realmente quente aqui, não está?"

    scene juiza sofa6 with Dissolve(1.0)

    eli "Eu quero brincar muito com você, tolinho."

    eli "Você quer tanto ajudar seu amigo, não quer?"

    mc desculpa "Sim, senhora."

    eli "É por isso que você está aqui? É por isso que você tá ajoelhado pra mim?"

    eli "Ou será que é porque você gosta de ficar no chão?"

    "Ela parece completamente outra pessoa."

    mc desculpa "Eu-"

    eli "Eu prometo que se você for um bom animalzinho pra sua dona, eu ajudo seu amigo."

    eli "O caso dele pode ir para ambos os lados. É algo antigo, e, depende muito da interpretação de cada juíz."

    eli "Sua dona vai deixar você feliz, tudo bem?"

    mc "O-obrigado..."

    eli "MAS! Só se você se comportar e me obedecer direitinho."

    "Já não tá bom o que eu fiz?"

    eli "Você tá me deixando muito excitada. Se você continuar assim, merece seu prêmio."

    mc "Sim, senhora..."

    eli "Mas, por hoje, eu tenho só mais uma tarefa para você."

    "Até que enfim."

    eli "Meu cachorrinho tem que vir aqui e beijar meu pé."

    "!"

    scene juiza sofa7 with Dissolve(1.0)

    pause

    mc surpreso "!"

    eli "Vem, totó. Vem aqui, vem."

    eli "Obedece direitinho sua dona."

    "Isso é verdade? Até onde vai a cabeça dessa mulher?"

    eli "Se você beijar com vontade, você vai deixar sua dona muito satisfeita."

    eli "Hmmm... não me faz esperar."

    menu:
        "Eu não vou fazer isso. Isso já foi longe demais":


            "Ela tá exagerando. Se ela acha que eu sou só um 'cachorrinho'. Ela que vá pro inferno."

            "Mas se eu negar ela, ela vai ficar muito puta. Tipo..."

            call n4_juiza_recusou from _call_n4_juiza_recusou_3

            "Merda... Agora falta pouco. Eu consigo aguentar essa humilhação pelo [n]."

            mc desculpa "Cla-claro, senhora. O que você pedir."
        "Sim, senhora.":


            mc desculpa "Claro, senhora. O que você me pedir."



    eli "Assim que eu gosto de ouvir..."

    scene black with dissolve

    scene pri9_img10 with Dissolve(1.0)

    mc "Hmm..."

    eli "Aaahhh..."

    eli "Assim mesmo..."

    eli "Isso. Com vontade."

    eli "Meu cãozinho que adora lamber os dedos da dona dele... hmm..."

    "Eu preciso continuar atendendo os caprichos dessa aí..."

    eli "Você tá me deixando com vontade de fazer algo mais..."

    mc "M-mais?"

    eli "E aposto que você vai adorar..."

    mc "Vou?"

    eli "Você gostaria de... sentir a preciosa da sua senhora?"

    mc "T-transar de verdade?"

    eli "Você vai ter que continuar obedecendo tudo o que eu mandar direitinho... e daí eu permito."

    "Nunca passou pela minha cabeça fazer isso aqui... com ela..."

    label n4_premium1:

        eli "Agora obedeça e diga 'sim, senhora'."

    menu:
        "Sim, senhora.":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_13

                jump n4_premium1

            mc "S-sim, senhora."

            eli "Aahh... muito bem..."

            eli "Primeiro permita-me preparar seu material... eu quero ele do jeito que eu gosto."

            mc "E como vai ser isso?"

            eli "Venha... se ajeite aqui."

            mc "{i}gulp{/i}"

            scene black with dissolve

            eli "Pronto..."

            scene pri9_img15 with Dissolve(1.0)

            pause

            mc "Aah... c-cuidado..."

            eli "Fica quietinho... eu sei o que eu estou fazendo."

            mc "Sim, senhora..."

            eli "Vamos amassar bem..."

            mc "A-agh!"

            eli "E preparar bem... vê... ele já tá crescendo... ele adora ser pisado..."

            mc "N-não é isso! É que você tá mechendo nele!"

            eli "Você pode mentir quanto você quiser, mas sabemos o quanto ele gosta... olhe aqui."

            scene pri9_img16 with Dissolve(1.0)

            pause

            mc "S-senhora!"

            eli "Forte demais pra você?"

            mc "ARGH!"

            eli "Ele continua duro..."

            mc "M-mas!"

            eli "Muito bem. Você tá pronto. Agora desça!"

            mc "Q-quê?!"

            scene black with vpunch

            mc "AGHH!"

            scene n4_premium1 with Dissolve(1.0)

            pause

            mc "Não precisava me jogar assim..."

            eli "Eu disse que você poderia sentir ela, contanto que você me obedecesse. Então pare de reclamar de tudo."

            mc "..."
            scene nnew_ani22 with Dissolve(1.0)
            eli "Vamos... você quer, não quer?"

            mc "Eu..."

            eli "Pode ser que doa um pouco... mas vai ser melhor do que pior... se você continuar me ouvindo."

            mc "E-eu!"

            menu:
                "Continuar parado":


                    mc "Sim, eu aceito o que a senhora quiser."

                    eli "Perfeito."

                    scene n4_premium2 with Dissolve(1.0)

                    pause

                    eli "Você vai ficar parado e deixar eu fazer o que eu quiser com seu membro. Entendido?"

                    mc "Sim, senhora..."

                    "Aah... essa ansiedade tá me matando."

                    eli "Não importa o que eu faça, apenas continue duro. Eu vou usar você como eu quiser, entendeu?"

                    mc "Sim, senhora."

                    eli "Agora você é só um vibrador de carne quentinho. Só serve pra meu prazer."

                    eli "Eu vou começar estimulando meu clítoris... porque eu adoro e me excita."

                    eli "Fique duro enquanto eu uso você."

                    mc "Si-"

                    eli "Cala a boca, vibrador. Você não fala."

                    scene black with dissolve

                    scene n4_premium3 with Dissolve(1.0)

                    pause

                    eli "Ah... assim..."

                    eli "Eu adoro me esfregar em um vibrador duro e quentinho..."

                    eli "Me deixa molhada pra depois poder enfiar em mim."

                    mc "A-a-"

                    eli "O único problema é que ele é barulhento demais!"

                    mc "!"

                    eli "Parece que melhorou... hmm..."
                    scene nnew_ani19 with Dissolve(1.0)
                    eli "Assim mesmo..."

                    eli "Se eu continuar assim, logo logo eu vou tá molhada o suficiente pra enfiar na minha vagina."

                    eli "Assim... hmm..."

                    eli "Desse jeito... aahnn... que delícia..."

                    mc "Ah..."

                    eli "Tá na hora... eu quero sentir tudo agora!"

                    scene n4_premium4 with vpunch

                    pause

                    eli "AAIH!"

                    eli "Entrou direitinho!"

                    mc "Ah..."

                    eli "Agora meu consolo vai ficar aí até eu atingir o clímax! Esse consolo de merda que nem me preenche inteira!"

                    menu:
                        "Ei!":


                            mc "Como as-"

                            eli "CALA A BOCA SEU CONSOLO INÚTIL!"
                        "...":


                            mc "..."

                            eli "Isso mesmo... quietinho enquanto eu te uso!"

                    eli "Seu vibrador imundo na minha buceta perfeita! Que degradação!"
                    scene nnew_ani24 with Dissolve(1.0)
                    eli "Como essa sujeira é permitida?!"

                    eli "Assim! É uma desgraça!"

                    eli "AAHNN!"

                    eli "Isso! Fode minha vagina virgem!"

                    eli "Esse objeto imundo no meu corpo limpo! Que falta de escrúpulo! NNNGHH!"

                    scene n4_premium5 with vpunch

                    pause

                    eli "Mais forte! AAIIN!"

                    eli "Eu preciso de mais! Esse pedacinho de carne é pouco demais pra mim!"

                    eli "Você não tem vergonha de transar assim?!"

                    eli "Não serve nem pra satisfazer sua senhora?! Você não é um homem! Nunca vai ser!"

                    eli "ANNGH! ISSO! HMMMM!!!"

                    scene n4_premium5 with vpunch

                    pause

                    mc "!"
                    scene nnew_ani25 with Dissolve(1.0)
                    eli "Não faça essa cara! Você aguenta, inútil!"

                    "Essa mulher maluca vai quebrar meu caralho desse jeito!"

                    eli "Cansei desse pau na minha buceta! Vou usar ele no meu rabo agora!"

                    eli "Vem, entra aqui!"

                    scene n4_premium6 with vpunch

                    pause

                    eli "Isso!"

                    eli "Eu sou uma filha da puta por enfiar esse treco imundo no meu anus! Aahhnn!"

                    eli "Mas você é mais coitado ainda! NNGH! Fazendo tudo o que uma mulher suja manda! Ahnn! Que coitado!"

                    mc "..."

                    eli "Nem consegue falar nada! AHH! Que falta de vergonha nessa cara! HMMM!"
                    scene nnew_ani23 with Dissolve(1.0)
                    eli "Se você continuar assim! HNNNG! Entrando e saindo! NNNGH!"

                    eli "Minha nossa!"

                    mc "AGH!"

                    eli "Tá doendo, é?! HMMM!"

                    eli "Só porque eu tô entortando esse vibrador velho?!"

                    "Mais um pouco! Só mais um pouco!"

                    eli "Assim! Eu tô! Quase! NNGHH!! LÁÁÁ!!!"

                    scene n4_premium7 with vpunch

                    pause

                    eli "AAAAANNGHHHH!"

                    scene n4_premium7 with vpunch

                    eli "Aahnn... aaahnn... hmmm..."

                    eli "Não acredito... que você me fez gozar assim!"
                    scene nnew_ani20 with Dissolve(1.0)
                    mc "Que bom que-"

                    eli "Seu objeto fez sua função. Não tem nada de mais nisso... Mesmo assim..."
                "Parar com tudo!":




                    mc "N-não! T-tá bom pra mim!"

                    eli "Tem certeza? Então se desculpe."

                    mc "Perdão..."

                    eli "É uma pena, mas se você não está preparado..."

            scene black with dissolve
        "Melhor parar aqui.":


            mc "S-senhora, eu acho melhor parar aqui."

            eli "Tem certeza? Então se desculpe."

            mc "Perdão..."

    eli "Muito bem, garoto. Você foi muito bem hoje, meus parabéns."

    eli "Pode levantar."

    scene sala_juiza poltronas with Dissolve(1.0)

    eli "Só um segundo."

    "..."

    eli "Pronto."

    show juiza excitada with dissolve

    eli "Quem diria..."

    mc envergonhado "..."

    eli "Depois da sua ajuda, vou precisar da sala só pra mim por um momento."

    eli "Quem sabe, em outra oportunidade, eu deixe VOCÊ ir até o fim."

    eli "Mas não hoje. Pode se retirar."

    mc preocupado "Mas e o-"

    eli "Já disse que não posso falar sobre o caso amanhã."

    hide juiza with dissolve

    mc bravo "Mas entã-"

    eli "Eu não prometi nada a você. Você fez um bom trabalho, como um verdadeiro cachorrinho. Mas isso não muda nada."

    mc irritado "!"

    show juiza incomodada with dissolve

    eli "Não se engane. Eu NUNCA vou deixar que algo interfira em minhas decisões."

    eli "O que fazemos em nossa vida privada diz respeito somente a nós mesmos."

    eli "Mas não podemos deixar que isso atrapalhe em outras áreas da nossa vida."

    eli "Inclusive, eu poderia dar flagrante em você agora mesmo por tentar corromper um funcionário da Lei."

    mc angustiado "Não! Por favor! Eu-"

    show juiza excitada with dissolve

    eli "Essa sua expressão angustiada.. hmm..."

    eli "Esse seu jeito de coitado já conseguiu coisas demais de mim."

    eli "Venha para a audiência amanhã, eu vou gostar de te ver."

    eli "Até uma próxima, [mc]."

    hide juiza with dissolve

    mc envergonhado "Ai..."

    "Essa [eli] Richter é uma peça. Nem sei o que achar dessa mulher."

    "Acho que todos nós temos nossos segredos..."

    scene black with dissolve

    "Droga! Não consegui nada pra ajudar o [n]!"

    if n3_gravou:

        "E eu tinha as fotos e não ameacei ela! Não consegui achar uma brecha nesse final!"

    "Merda merda merda!"

    $ juiza_sucesso = True

    jump nathan_e4_incerto



    label n4_juiza_recusou:

        "Sinto que se eu responder isso ela não vai gostar nem um pouco."

        if n3_gravou:

            "Eu ainda tenho as fotos, então provavelmente vou ter que usar elas."

            "Mas eu não sei como ela pode reagir à chantagem."
        else:


            "Se eu não conseguir convencer ela a dar o caso ganho para o [n], provavelmente ele vai ser deportado."

            "É isso que eu vou fazer?"

        menu:
            "Eu {b}não{/b} vou continuar com o jogo dela":


                "Não quero isso!"

                jump nathan_e4_recusou
            "Preciso aguentar isso pelo [n] e continuar":


                "O [n] precisa da minha ajuda. Tenho que continuar aceitando o jogo dessa doida."

                return

    label nathan_e4_recusou:

        scene sala_juiza poltronas with dissolve

        mc serio "[eli], eu entendi o que tá acontecendo."

        mc "Eu não quero participar disso."

        show juiza incomodada with dissolve

        eli "Tem certeza?"

        mc desculpa "Não me leve a mal, mas isso-"

        eli "Não precisa falar nada. Por favor, só se retire."

        mc preocupado "Mas e-"

        eli "Não posso falar nada sobre julgamentos. Espero que seu amigo fique bem."

        mc "Mas-"

        show juiza brava with dissolve

        eli "Eu vou precisar chamar o segurança?"

        mc "Não! Por favor!"

        eli "Então acho bom você deixar minha sala agora mesmo."

        if n3_gravou:

            "Merda... não consegui convencer ela."

            "É agora ou nunca. Se eu não ameaçar ela agora, o [n] pode ser deportado."

            "Mas o que vai acontecer COMIGO se eu tentar coagir uma juíza desse calibre?"

            "O que eu faço?!"

        menu:

            "Eu tenho uma foto aqui que talvez você queira ver." if n3_gravou:

                mc tarado "Calma."

                eli "?"

                mc "Eu tenho algo aqui que com certeza você vai querer ver. Diz respeito a algo que você com certeza não quer que outros vejam."

                eli "Como? O que você quer dizer com isso?"

                eli "Abre a boca!"

                mc bravo "Ai!"

                jump nathan_e4_ameaca
            "Tudo bem...":


                "Não tenho nada que eu possa fazer."

                "Não consegui convencer ela a ficar do lado do [n]."

                "A situação dele está irregular. Parece que ele não tem muito apoio legal também."

                "Provavelmente ele vai se ferrar. Mas... eu não consegui..."

        mc desculpa "Ok. Até."

        hide juiza with dissolve

        "..."

        jump nathan_e4_incerto

    label nathan_e4_ameaca:

        $ juiza_fotos = True

        scene sala_juiza poltronas with vpunch

        "Agora não tem mais jeito. Vou ter que entregar o jogo."

        "Espero que eu não me arrependa de ameaçar essa mulher."

        show juiza brava with dissolve

        eli "Diga! O que você tem sobre mim?!"

        "Se eu fraquejar, ela não vai cair. Preciso ser firme. Força, [mc]!"

        mc tarado "Acho bom a senhora juíza tomar cuidado em como fala comigo. Eu tenho algo aqui que pode acabar com sua vida."

        eli "!"

        mc "Tome. Veja com seus próprios olhos."

        show juiza_bdsm1 with dissolve

        eli "Como?!"

        eli "Quem te deu essa foto?!"

        menu:
            "Uma amiga.":


                mc tarado "Uma amiga que aparentemente não vai muito com sua cara."

                mc "Ela sabia que talvez eu precisasse de uma pequena ajuda sua."

                eli "Amiga..."
            "Não interessa.":


                mc tarado "Não interessa."

                mc "Eu tenho outras cópias obviamente. E isso vai aparecer pra todo mundo."

                eli "Seu idiota..."

        eli "Isso é um absurdo!"

        hide juiza_bdsm1 with hpunch

        eli "O que eu faço ou não na minha vida privada não tem nada a ver com o tribunal!"

        mc tarado "Quero ver você explicar isso pros jornalistas que vão fazer fila na saída da prefeitura..."

        eli "Seu filho da puta..."

        eli "Tudo isso pra influenciar o caso do [nc]?!"

        mc "Exatamente. Amanhã você vai decidir que ele está legalmente no país, mesmo que não esteja!"

        mc "Ou do contrário essa foto vai estampar a capa da nossa revista."

        eli "Desgraçado..."

        eli "Você não é o primeiro que tenta me ameaçar, DESGRAÇADO!"

        eli "Você acha que aquele prefeitinho de merda não tentou fazer a mesma coisa?!"

        eli "Eu tô acostumada com o jeito dos fracos! O jeito dos sujos!"

        eli "Enfia essa foto no meio do seu cú! E sai daqui antes que eu te mande pra prisão!"

        "Merda! Merda! Ela tá pouco se fodendo pra foto! E agora?!"

        eli "Espero que nunca mais você apareça aqui!"

        menu:
            "...":


                mc bravo "..."
            "Espero que você teja pensando nas consequências.":


                mc bravo "Espero que você saiba o que tá fazendo..."

                mc "Jogar no lixo sua reputação. Você nunca mais vai ser olhada com os mesmos olhos."

                eli "FODA-SE! Eu não vou ser comprada por você, seu cretino!"

                eli "Agora saia da minha sala!"

        hide juiza with dissolve

        "Merda... deixa eu sair daqui."

        "..."

        jump nathan_e4_incerto

    label nathan_e4_incerto:

        play sound "audio/som_35_passos.mp3"

        $ renpy.pause(delay=1, hard=True)

        scene prefeitura geral with Dissolve(1.0)

        "..."

    if juiza_fotos:

        "A desgraçada não se dobrou pra minha ameaça..."

        "Ela vai ferrar a vida do [n] de propósito amanhã. Tenho certeza."

        "Acho que eu só ferrei ainda mais as coisas."

    "Agora é voltar pra casa e esperar a audiência amanhã."

    if juiza_sucesso:

        "Eu fiz tudo o que ela me obrigou. Me rebaixei de uma forma que eu nunca imaginei."

        "Mas isso não garantiu nada! Por que eu fiz tudo aquilo então?!"

        "No fundo ela realmente me tratou igual um... qualquer..."

    "Agora nem sei o que vai aco-"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    mc surpreso "É o [n] ligando!"

    mc desculpa "Oi, [n]."

    n "Oi, [mc]. O que houve? Você parece meio pra baixo."

    menu:
        "Não é nada.":


            mc envergonhado "Não esquenta. Não é nada."

            n "Sério?"
        "Estou preocupado com você amanhã.":


            mc desculpa "Só tô preocupado com você amanhã."

            "Além de não conseguir nada, talvez só tenha piorado tudo."

    n "Então. Queria te pedir se você não pode ir amanhã comigo pro tribunal."

    mc surpreso "Quê?!"

    n "Eu posso levar algumas pessoas. E eu queria que você estivesse lá. Você topa?"

    if juiza_fotos:

        "Depois da nossa briga, se eu aparecer aqui amanhã a [eli] vai mandar me prender."

        "O [n] vai ficar triste, mas não tem como eu aparecer aqui."

        jump nathan_e4_naopode

    mc "Sério?! Mas eu?"

    n "Você tem sido um parça pra mim."

    if nathan_beijo or nathan_e3_beijo:

        n "E depois do que rolou entre a gente. Você é mais que isso pra mim até."

    n "Eu queria muito que você estivesse comigo amanhã."

    menu:
        "Com certeza. Pode contar comigo.":


            $ nathan_audiencia = True

            mc normal "Claro. Pode contar comigo. Vou estar lá com você."

            "Se ele soubesse que eu tô aqui..."

            n "Muito obrigado, [mc]. Você é o cara!"

            n "Ia ser 15h, mas eles adiantaram para às 9h. Se você puder, chega uma hora antes."

            mc "Pode deixar. A gente se vê amanhã lá."

            n "Valeu mesmo. Abraço."

            mc "Até."

            "{i}Tchk{/i}"

            "Onde eu me meti?"

            "Deixa eu voltar pra casa. Amanhã vai ser um dia e tanto."

            scene black with Dissolve(2.0)

            $ dia += 1
            $ tempo = 1

            "{b}Um dia depois{/b}"

            jump nathan_e4_audiencia
        "Eu tenho medo de atrapalhar. Melho eu ficar em casa.":


            "Vai saber o que acontece se a juíza me vê lá com ele. Posso só ferrar tudo."

            label nathan_e4_naopode:

                mc desculpa "Eu prefiro não tá lá, [n]. Tenho muito medo de atrapalhar."

            n "Putz... tudo bem. Se você acha melhor."

            mc "Sim. Desculpa mesmo."

            n "Relaxa. Vai dar tudo certo."

            mc normal "Tenho certeza que vai dar tudo certo."

            n "Valeu, [mc]. Amanhã quando eu tiver a resposta eu te aviso."

            mc "Beleza. Boa sorte."

            n "Falou."

            "{i}Tchk{/i}"

            "Onde eu me meti?"

            "Deixa eu voltar pra casa. Amanhã vai ser um dia e tanto."

            scene black with Dissolve(2.0)

            $ dia += 1
            $ tempo = 1

            "{b}Um dia depois{/b}"

            scene ape_geral with Dissolve(1.0)

            "Que merda ficar aqui sem saber o que tá rolando."

            "Vou ter que esperar até a TV falar alguma coisa."

            "..."

            jump nathan_e4_casa

    label nathan_e4_audiencia:

        scene ape_geral with Dissolve(1.0)

        "Já tá na hora. Até eu pegar o busão e chegar lá, já vai ser depois das 8h."

    scene black with Dissolve(1.0)

    scene cidade onibus with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene cidade centro9 with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    play sound "audio/som_35_passos.mp3"

    scene prefeitura geral with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene prefeitura detector with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene prefeitura guarda with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    "Guarda" "Bom dia."

    mc normal "Fala ae."

    play sound "audio/som_35_passos.mp3"

    scene prefeitura geral2 with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    scene tribunal geral with Dissolve(1.0)

    $ renpy.pause(delay=1, hard=True)

    "Ufa..."

    "Será que o [n] tá aqui já?"

    n "[mc]?"

    mc normal "Oi, [n]."

    show nathan tribunal_paz with dissolve

    n "Tudo bem? Obrigado por ter vindo."

    mc "Nem precisa agradecer. Tomara que dê tudo certo hoje."

    show nathan tribunal_preocupado with dissolve

    n "{i}unff{/i}"

    n "É o que eu espero, cara."

    n "Nem sei o que eu vou fazer se ela der causa ganha pro Estado."

    n "Meu advogado explicou que como é um assunto que envolve leis federais, o processo já começa em segunda instância."

    n "Eu ainda poderia recorrer na última instância, mas isso seria feito já no meu país de origem, na Europa."

    mc preocupado "Nossa!"

    n "Provavelmente ela me mandaria pra fora do país em alguns dias..."

    if nathan_beijo or nathan_e3_beijo:

        "Depois daquele beijo, eu e o [n] começamos a desenvolver um lance."

        "Se ele for expulso do país assim... vai ser muito ruim."

    n "Eu tô realmente muito preocupado."

    menu:

        "Dar um beijo para acalmar ele" if nathan_beijo or nathan_e3_beijo:

            $ nathan_e4_beijo = True

            mc "Aqui."

            show nathan tribunal_beijo with Dissolve(1.0)

            pause

            n "[mc]..."



            mc "Você tá precisando..."

            n "Hmm..."

            n "Aqui é um lugar muito sério... a qualquer momento vai chegar mais pessoas..."

            menu:
                "Não tô nem aí. Vou beijar.":


                    mc "Não quero saber. Meu peguete tá precisando pensar em outra coisa agora..."

                    n "[mc]-"

                    scene black with dissolve

                    scene n4_premium8 with Dissolve(1.0)

                    pause

                    mc "Nem consigo imaginar o que eu vou fazer se você acabar tendo que sair do país..."

                    n "Você vai ficar sem isso aqui..."

                    mc "É isso que eu tô falando!"

                    n "Você vai ficar sem isso aqui também se o policial pegar a gente se catando assim aqui."

                    mc "Não quero saber. O medo de não ver mais você é pior."

                    mc "Eu preciso de mais."

                    n "[mc]... ok... eu também quero continuar com você. Eu vou te mostrar."

                    scene n4_premium9 with Dissolve(1.0)

                    pause

                    n "Hmm..."

                    mc "Ah..."

                    n "Eu quero que tudo se resolva logo e a gente possa sair juntos... curtir um ao outro completamente."

                    mc "Completamente, hm... gostei disso..."

                    n "Se tudo aqui acabar bem, a gente vai se aproveitar muito. Eu prometo."

                    mc "É isso que eu quero."

                    n "Mas a gente realmente tem que parar agora... ou pode dar ruim, ok?"

                    mc "Poxa... tá..."

                    scene black with dissolve

                    scene n4_premium10 with Dissolve(1.0)

                    pause

                    mc "Eu vou tá sempre do seu lado."

                    n "Valeu."

                    mc "Você se esforçou muito pra chegar aqui. E agora eles não podem te tirar isso."

                    n "Isso aí!"

                    mc "E se você tiver muito nervoso... eu posso ajudar..."

                    n "Sei..."

                    scene black with dissolve

                    scene tribunal geral with Dissolve(1.0)
                "Ok... eu paro.":


                    mc "Tá bom... eu entendo... um beijinho..."

            mc "Só pra você ficar mais calmo."

            mc "Vou estar esperando você voltar."

            n "..."

            show nathan tribunal_paz with dissolve

            n "Obrigado. Acho que eu precisava disso."

            mc safado "Que bom que ajudou."
        "Isso não vai acontecer. Você vai ganhar.":


            mc charmoso "Calma. Isso não vai contecer. Com certeza ela vai dar causa ganha pra você."

            n "É o que eu espero, [mc]..."

            n "Não consigo sentir essa confiança. Mas eu agradeço."
        "O que você acha que vai acontecer?":


            mc desculpa "Isso é uma merda..."

            mc "O que você acha que vai acontecer?"

            n "Difícil falar. Meu advogado disse que minhas chances são boas, mas não sei se ele fala isso pra todos os clientes dele..."

            n "Ele escreveu uma defesa baseada no tempo que passou desde que entrei no país, mas vai depender da juíza aceitar ou não os argumentos."

            mc "Difícil prever então..."

            n "Sim..."

    "Advogado" "Senhor [n]."

    show nathan tribunal_preocupado with dissolve

    n "Ah. Ok."

    n "Tenho que ir. Vai começar em alguns minutos."

    mc "Vai ficar tudo bem."

    n "Tomara."

    hide nathan with dissolve

    "Espero que dê tudo certo."

    scene tribunal visao with Dissolve(1.0)

    "..."

    "..."

    "Guarda" "Todos de pé."

    play sound "audio/som_36_cadeira.mp3"

    "..."

    "Aí vem a doida..."

    scene juiza_close1 with Dissolve(1.0)

    pause

    eli "Podem sentar."

    eli "Estamos em seção ordinária para deliberar quanto ao caso de número 204569 do ano vigente."

    eli "Estado contra [nc]."

    eli "A acusação é de imigração ilegal, seguida da não regularização da situação em subsequentes anos."

    eli "Senhor [n], por favor. Venha à frente."

    n "Eu? Mas meu advo-"

    eli "Senhor [n], esta é uma audiência simples. Não se sinta intimidado. Venha ao púlpito, por gentileza."

    n "S-sim, senhora."

    scene nathan_audiencia1 with Dissolve(1.0)

    n "Pronto."

    eli "Eu quero apenas lhe fazer algumas perguntas para que eu possa entender alguns detalhes que ficaram faltando da peça da defesa."

    eli "A primeira questão é com relação aos seus documentos."

    eli "Seu advogado alega que você possui documentação registrada como qualquer cidadão, e uma rápida pesquisa aponta para isso."

    eli "No entanto, a acusação alega que você não possui Certidão de Nascimento. E isso é verdade pelas informações que temos."

    eli "Isso confere, senhor [n]?"

    n "Si-sim..."

    eli "Então como foi possível para o senhor obter documentação sobre sua identidade nacional sem comprovação de nascimento?"

    scene nathan_audiencia2 with Dissolve(1.0)

    n "Meretíssima... eu não me lembro. Isso tudo aconteceu há muitos anos."

    eli "Essa é sua resposta, senhor [n]?"

    n "Eu gostaria de dar uma resposta melhor, mas... é a verdade, senhora. Eu realmente não me recordo."

    n "Eu ainda era muito jovem. Foi minha mãe que tirou minha documentação comigo."

    scene nathan_audiencia1 with Dissolve(1.0)

    eli "Entendo."

    eli "Minha segunda dúvida é com relação a sua atuação profissional."

    eli "Você trabalhou de forma oficial quando adolescente?"

    eli "Me refiro se você trabalhou com carteira assinada."

    scene nathan_audiencia2 with Dissolve(1.0)

    n "Não, senhora. Eu fiz bicos, mas minha intenção sempre foi trabalhar como modelo."

    n "Eu vivi às custas dos meus pais enquanto perseguia esse sonho."

    eli "E você conseguiu realizar seu sonho?"

    n "D-desculpe, meretíssima?"

    eli "Você realizou o sonho de se tornar modelo?"

    n "E-eu... eu consegui. Fechei meu primeiro contrato."

    scene nathan_audiencia1 with Dissolve(1.0)

    eli "Isso parece uma boa notícia, senhor [n]."

    n "Com certeza. Fiquei muito feliz. Mas-"

    scene juiza_close1 with Dissolve(1.0)

    eli "Eu sei que a pergunta parece fora de contexto, mas ela tem total ligação com seu caso, senhor [n]."

    eli "A peça da sua defesa se baseou no fato da passagem do tempo para defender sua causa."

    eli "Sua defesa afirma que após decorrido todo esse tempo, o Estado deve acatar sua cidadania."

    eli "Sim. Existe base legal para tal pedido, mas fica à critério do juíz em segunda instância a decisão sobre a validade do pedido."

    eli "Eu sou uma juíza que presa pelo predomínio irrestrito da Lei, e, para mim, tempo decorrido não é argumento."

    scene juiza_close2 with Dissolve(1.0)

    eli "A Lei é imutável, senhor [n]. O tempo não muda o fato do senhor ter entrado ilegalmente no país."

    eli "Portanto, minha decisão é que o senhor seja deportado para seu país de origem ou seja considerado um transgressor da soberania nacional."

    scene nathan_audiencia2 with vpunch

    n "M-mas, excelentíssima!"

    eli "Não existe meia Lei. Existe a Lei. E ela está aqui para ser cumprida."

    n "Merda..."

    scene nathan_audiencia1 with Dissolve(1.0)

    eli "O seu sonho de ser modelo se realizou em um momento que não poderia ser mais oportuno."

    eli "Ontem eu recebi informações legais sobre seu contrato com a empresa Blergh! fechado, como pontuado, recentemente."

    eli "Este é seu primeiro contrato de trabalho, não é mesmo?"

    n "Sim."

    eli "E esse fato foi omitido da peça da defesa. Provavelmente você não queria arrastar o nome da empresa para o meio desse problema."

    n "I-isso mesmo, senhora..."

    eli "Talvez justamente para não perder o emprego do seu sonho. O trabalho que você lutou tanto para conseguir."

    eli "Muito bem. Por azar, ou talvez sorte, como você verá, ontem eu recebi essas informações."

    scene juiza_close2 with Dissolve(1.0)

    eli "O dossiê trouxe todas as informações, como a quantidade de horas, duração do contrato, valor acertado."

    eli "Tudo isso assinado por você e pelo seu contratante, respondendo em nome da Blergh!."

    if cassia_nathan_entregou:

        "São as informações que eu entreguei pra [j]!"

        "Da primeira vez que eu conversei com o [n] no bar. As informações do contrato com a Blergh!!"

        "Co-como a juíza tem isso?!"

    eli "Pois bem. Por mais que isso vá contra seus interesses para com seu empregador..."

    eli "É graças a essas informações que você não será deportado do pais."

    scene nathan_audiencia2 with vpunch

    n "C-como?!"

    eli "Por favor, ordem, senhor [n]."

    n "Pe-perdão."

    scene nathan_audiencia1 with Dissolve(1.0)

    eli "Segundo a lei de número 1.257 de 2003, exercer trabalho devidamente registrado no país garante base para nacionalização de imigrantes."

    eli "Eu estipulo o prazo de 30 dias corridos para que você adquira a documentação necessária e dê entrada no processo."

    eli "Contanto que você cumpra o prazo estipulado, você será considerado um cidadão deste país."

    eli "Caso encerrado."

    play sound "audio/som_36_cadeira.mp3"

    scene tribunal visao with Dissolve(1.0)

    "Guarda" "Caso encerrado. Por favor, se retirem do tribunal em ordem."

    "Não acredito! Ele conseguiu!"

    "E graças às informações da Blergh! que ele me passou no bar! Como isso é possível?!"

    scene tribunal geral with Dissolve(1.0)

    mc feliz "[n]! Meus parabéns!"

    n "[mc]. Dei-"

    "Advogado" "Senhor [n], por favor. Vamos sair antes que a imprensa bloqueie as saídas. Não temos tempo."

    n "[mc]! Muito obrigado! Desculpa! Não posso falar agora!"

    mc envergonhado "Ok! Vai lá!"

    mc "Que loucura..."

    scene black with Dissolve(2.0)

    "Deixa eu voltar."

    jump nathan_e4_casa

    label nathan_e4_casa:

        scene ape_tv with Dissolve(1.0)

        "Será que vai demorar pra eles falarem do [n]?"

        play sound "audio/som_34_news.mp3"

        mc "Opa. Noticiário."

        show tv apresentador with dissolve

        "Apresentador" "Agora são 13 horas e está começando o FNEWS 13, seu boletim diário de informação."

        "Vinheta" "{b}Faux News: Nós somos a Notícia de Verdade{/b}"

        "Vinheta" "{b}LÁLÁ LÁ LÁÁÁ~{/b}"

        "Apresentador" "Abrimos o noticiário de hoje com informações sobre a audiência do modelo [nc]."

        "Apresentador" "A audiência já acabou e a sentença foi proferida."

        "Apresentador" "[nc] não será deportado."

        "Apresentador" "Sentença da juíza [eli] Richter livrou o acusado com base na lei de número 1.257 de 2003."

        "Apresentador" "[nc] se encaixou na lei após fechar contrato com a famosa marca Blergh! e se tornar um de seus modelos."

        "Apresentador" "A lei determina que imigrantes que trabalham com carteira assinada no país podem se tornar cidadãos."

        "Apresentador" "A juíza de segunda instância determinou ainda o prazo de 30 dias para Bryant entrar com o pedido de regularização."

        "Apresentador" "Segundo informações que recebemos do nosso repórter em campo, a juíza teve acesso às informações apenas ontem."

        "Apresentador" "O argumento da defesa, incrivelmente, não citava a lei que salvou o modelo."

        "Apresentador" "Nosso repórter afirma que a meretíssima Richter recebeu um dossiê com as informações sobre o contrato de terceiros."

        "Apresentador" "Independente da origem do dossiê, [nc] está livre da acusação, contanto que regularize a situação no prazo estipulado."

        "Apresentador" "E agora espo-"

        scene ape_tv with Dissolve(1.0)

        if not nathan_audiencia:

            "Ele conseguiu! Não acredito!"

            "Eu não estraguei tudo!"

            "Ufa... então acabou bem mesmo. Que bom, [n], cara... você merece."

        "Fico muito feliz por ele."

        if nathan_e4_beijo:

            "Aquele beijo no tribunal, na frente do advogado e dos procuradores haha..."

            "Até parece que foi algo oficial."

            "Espero não ter prejudicado ele."

            "Se bem que na hora eu sei que ele curtiu também."

        "Agora ele só precisa aguentar os jornalistas no pé dele por alguns dias e tá tudo resolvido."

        "Depois vou ligar pra ele e ver como ele tá."

        "Sem isso, ele vai finalmente curtir a vida boa."

        "E esse lance do dossiê que a [eli] recebeu? Quem pode ter sido?"

        if nathan_p1:

            $ nathan_dossie = True

            "Até agora eu tô com essas informações comigo."

            "Como mais alguém tem isso?"

        "Só sei que isso salvou a pele dele."

        "Bom, ainda tenho muita coisa pra fazer. Não adianta ficar aqui sentado. Tenho que sair pela cidade!"

        scene black with Dissolve(2.0)

        $ v20_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v20_fim","nathan","personagem")

    jump call_cidade

label nathan_evento5_pre:

    $ nathan_cel_msg4_resposta = True
    $ nathan_e5 = "pre"

    "Então parece que tudo acabou certo mesmo."

    "Eu fico feliz pelo [n]. Ele é um cara tão de boa. Não merece virar alvo da [j] desse jeito."

    "Essa mulher não tem limites. Ela vai acabar com a vida dele se as coisas continuarem assim."

    "A sorte é que pelo menos agora ela conseguiu o que queria. A grande matéria que ela tava esperando."

    "A reportagem dela foi até parar na Faux News. Reconhecimento nacional, tanto pelo revista como pela TV."

    "E o [n] que acabou se ferrando com toda essa história."

    "Fico pensando como é foda ser famoso. Qualquer coisa que acontece na sua vida vira assunto na boca de todo mundo."

    mc envergonhado "Tudo por causa de paparazzi igual eu..."

    "Mas por que as pessoas se interessam tanto pela vida dos outros?"

    mc zerado "Bando de xeretos..."

    "Bah. Deixa isso pra lá."

    "Quem sabe agora não é uma boa hora pra sair com o [n]. Comemorar que tudo deu certo e ele não vai precisar sair do país."

    if nathan_e3_beijo or nathan_beijo:

        $ nathan_quente = True

        if nathan_e3_beijo:

            "E até... depois do nosso beijo lá no bar do [gar]..."

            "Ele disse que a gente poderia falar sobre assumir um namoro quando isso acabasse."

        elif nathan_beijo:

            "E depois que a gente ficou lá no apartamento da [j]..."

            "Podia até rolar algo entre a gente, mas aconteceu tudo isso e a gente nem conseguiu ficar juntos depois direito."

        "Isso podia até acontecer hoje..."

        mc safado "Talvez até... algo mais que um beijo."
    else:


        "A gente podia curtir juntos e quem sabe até pegar umas minas."

    "Vou chamar ele pra fazer alguma coisa hoje à tarde."

    "Ah! Quem sabe aquela pizzaria do centro!"

    if v26_fim:

        "Aquela que eu fui com a [d] e acabei não pagando a pizza..."

        "Será que é uma boa ir lá?"

        "..."

        "Foda-se. Se pá eles nem vão lembrar."

        "E pensando bem... a gente pediu uma pizza vegetariana e mandaram calabresa. Nem mereciam receber mesmo."

    "Deixa eu falar com o [n]."

    "..."

    mc normal "Pronto."

    "..."

    "Ele respondeu."

    show screen celular_nathan

    pause

    "Massa. Então tenho que ir até a {b}pizzaria na parte da tarde{/b}."

    "A melhor forma de chegar lá é de busão. Daí vou até o centro e vou andando até a pizzaria. Não posso esquecer que é de {b}tarde{/b}."

    "Massa... pizzaria..."

    mc tarado "Eu sou um gênio."

    jump call_cidade

label nathan_evento5:

    scene cidade pizzaria_out_dia with Dissolve(1.0)

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n5_save", extra_info="n5_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ nathan_e5 = "evento"

    "Tô aqui. O [n] deve tá chegando logo."

    "???" "E aí, [mc]?"

    mc normal "Opa. Fala aí, [n]."

    "Bem na hora."

    show nathan n_normal with dissolve

    n "Gostei da sua ideia. Nunca tive tempo de vir aqui, mas o pessoal sempre comentou comigo."

    mc normal "Verdade. É um lugar bem famoso mesmo."

    n "Parece que a família que é dona da pizzaria é super tradicional aqui na capital."

    mc "Você sabe quem são?"

    n "Pra falar a verdade..."

    n "Não faço ideia..."

    mc feliz "Haha... nem eu."

    mc surpreso "Mas fala aí! E o lance da audiência?!"

    show nathan n_preocupado with dissolve

    if nathan_audiencia:

        n "Ué. Você tava lá, pô."

        mc normal "Eu sei, mas queria saber dos detalhes."
    else:


        n "Ah..."

        mc envergonhado "Desculpa não poder tá lá, queria muito saber como foi."

        n "Relaxa. Acabou dando tudo certo, mesmo não sendo fácil."

        mc normal "Que bom."

    n "Ah, mano... Desde que a [j] me procurou pela primeira vez ela já aprontou tanto comigo."

    n "Cada dia eu durmo preocupado pensando a notícia terrível que eu vou ter quando eu acordar. Isso se não me acordarem de madrugada."

    mc desculpa "Deve ser horrível, cara."

    show nathan n_vergonha with dissolve

    n "Não é fácil, [mc]. Mas obrigado por tá sempre sendo um apoio aí."

    menu:
        "Pode contar comigo. Sou seu parceiro.":


            $ nathan_amizade += 1

            mc normal "Você é um mano massa, [n]. Pode sempre contar comigo que a gente é parceiro."

            n "Valeu. Eu sinto que você é um parça mesmo."

            mc "Com certeza. Eu meio que me senti igual você quando cheguei aqui na ilha."

            n "Como assim?"

            mc envergonhado "Eu me sentia meio sozinho nessa ilha. Com o tempo eu fui encontrando a galera, celebridades e outras pessoas doidas..."

            mc "Mas no começo não foi assim."

            n "É foda, cara."
        "De boa.":


            mc normal "De boa. Não foi nada de mais."

            n "Foi sim. É quando a gente tá na merda que a gente mais precisa das pessoas."

            mc envergonhado "..."

        "Você sabe o que eu sinto por você." if nathan_quente:

            mc charmoso "Claro que você pode contar comigo. Você sabe o que eu sinto por você."

            n "Então é tudo com segundas intenções?"

            mc charmoso "Queria poder dizer que não, mas é."

            n "Haha... você passa uma segurança, [mc]. Isso é incrível. Tipo, você consegue falar o que quer, sem se preocupar."

            mc "Você também é assim. Desde o bar, eu vi que você era um cara seguro."

            n "Sei lá... não consigo achar isso."

            mc "Claro que é, [n]. É que essas coisas que aconteceram com você te deixaram meio abalado."

            n "Pode ser..."

    mc desculpa "Eu acho que nossa história é um pouco parecida."

    show nathan n_normal with dissolve

    n "Por que você acha isso?"

    mc normal "Tipo, nós dois viemos pra cá buscando uma coisa diferente na nossa vida."

    mc charmoso "Você tem o sonho de ser modelo, e tá fazendo tudo o que pode pra chegar lá."

    n "E foi assim com você também? Não sei se você seria um bom modelo."

    mc zerado "Ei..."

    mc "Claro que não exatamente igual."

    n "Tô zuando. Você queria ser um jornalista, né?"

    mc desconfiado "Não sei exatamente..."

    n "Como assim? Não é esse seu sonho?"

    mc "Hmmm..."

    menu:
        "Eu ainda não descobri meu sonho na verdade.":


            mc envergonhado "Acho que eu ainda não descobri qual é meu sonho na verdade."

            n "Entendo. Mas você não precisa ter pressa. Isso ainda vai aparecer pra você."

            mc "É o que eu espero..."
        "Meu sonho é encontrar uma pessoa especial.":


            mc normal "Na verdade, o que eu queria mesmo era encontrar uma pessoa especial na vida."

            n "Então temos um romântico aqui."

            if nathan_quente:

                mc charmoso "Talvez eu até tenha encontrado."

                n "E- quem seria?"

                mc "..."

                n "Ei, pare de me olhar assim e me deixar com vergonha."

                mc "Haha... ok."
            else:


                n "Não sei... acho que todo mundo pensa um pouco assim também."

                mc normal "Tem razão. Acho que muita gente quer encontrar alguém legal pra compartilhar as coisas."

                n "Eu espero que você encontre."

                mc "Tomara. E você também, cara."
        "Meu sonho é chegar ao topo e ter muito dinheiro.":


            mc charmoso "O que eu queria mesmo era me dar bem profissionalmente. Dominar a ilha e poder fazer o que quiser com meu dinheiro infinito."

            n "Caraca... falando assim parece bom mesmo!"

            mc "O amor pode ser importante, mas o sucesso pessoal é mais. Ser autossuficiente e bem sucedido. É isso que eu procuro pra minha vida."

            n "É. Não ter que fazer o que os outros mandam e poder viver a vida como quiser, parece um bom objetivo."

            mc "Né?"
        "Eu não tenho um sonho. Só quero ver onde a vida vai me levar.":


            mc normal "Olha... eu não penso muito nisso. Eu só quero poder viver com saúde, aproveitando cada minuto. Onde eu vou chegar, é pro eu do futuro."

            n "Então é um cuca fresca."

            mc zerado "Ei..."

            mc desconfiado "..."

            mc envergonhado "É... pode ser."

            n "Hahaha!"

            mc zerado "..."

            n "Mas não digo que você tá errado. Eu acho que eu me encaixaria aí também, sabe."

            mc normal "Sério?"

            n "Ficar pensando muito só dificulta ainda mais a vida. Querer ter tudo no nosso controle. Às vezes é só a insegurança falando."

            show nathan n_vergonha with dissolve

            n "Talvez foi assim que eu me meti onde eu tô..."

            mc envergonhado "Nem tudo é perfeito, né?"

            n "Pois é..."

    mc "Mas acho que a gente podia sentar, né? Dois tonto de pé."

    n "Haha... ok. Podemos sentar aqui fora?"

    mc "Claro."

    hide nathan with dissolve

    n "Deixa eu sentar."

    scene nathan_pizzaria1 with Dissolve(2.0)

    pause

    n "Bem agradável o lugar, não achou?"

    mc normal "Sim. Achei bem interessante aqui."

    n "Você já tinha vindo?"

    if v26_fim:

        mc "Eu vim uma vez, mas não sentei aqui fora."
    else:


        mc "Não. Nunca comi aqui."

    n "A tá."

    mc normal "Você quer pedir já?"

    n "Eu que decido?"

    mc charmoso "A gente tá aqui comemorando que você não vai deixar o país, caralho! Claro que é você quem escolhe!"

    n "Haha. Tá. Então eu queria conversar um pouco antes."

    mc normal "De boa."

    n "Acho que é a primeira vez que eu tô conseguindo parar e pensar em alguma coisa que não me preocupa."

    mc desculpa "Realmente não foi fácil pra você esses tempos, né?"

    n "Acho que..."

    scene nathan_pizzaria2 with Dissolve(1.0)

    n "Tudo começou quando eu encontrei a [j]. Só de pensar eu já fico puto com isso."

    mc serio "Com aquela não tem brincadeira mesmo."

    n "Se eu pudesse fazer alguma coisa contra ela... Acho que eu quebrava aquela cara de pau..."

    mc envergonhado "Aposto que muita gente tem essa vontade."

    mc serio "Pra falar a verdade, eu queria entender melhor como você e ela se encontraram."

    n "Falar da [j]? Quer arruinar nossa tarde?"

    "Não queria arruinar... mas eu nunca entendi direito a fixação da [j] pelo [n]. Acho que eu gostaria de saber disso."

    "Talvez ele pudesse me falar mais da [j] pra eu entender ela melhor e quem sabe se aproximar mais dela na redação."

    "Mas também não queria chatear ele."

    if nathan_quente:

        "Se eu quero ficar com ele, o melhor é a gente falar de outra coisa, sobre a gente..."

    "E agora?"

    menu:
        "Não quero te incomodar. Só quero entender tudo.":


            mc desculpa "Desculpa. Não queria te encher, mas é que eu ainda não entendi como tudo isso aconteceu."

            mc preocupado "Eu sinto que eu acabei entrando nisso mais do que eu devia, malz."

            n "Ai..."

            n "Nem sei o que falar, [mc]..."

            n "Mas se você realmente quer saber dela, acho que até vai ser bom eu desabafar um pouco."

            mc serio "..."

            label nathan_e5_cassia:

                n "É que, tipo, a [j] tá envolvida em alguma coisa grande."

            mc desconfiado "Como assim?"

            n "Não sei exatamente o que é. Mas ela não é só uma jornalista querendo matérias pra revista dela."

            mc zerado "Pra mim, ela só se importa com isso."

            n "A [j] é faminta por poder."

            mc "Agora você disse algo que eu entendo."

            n "E ser uma repórter de revista é pouco pra ela. Ela não tá satisfeita com isso."

            "Sempre que eu falei com a [j], principalmente no apartamento dela, ela sempre me falou que poder e dinheiro é o que importa."

            "Não tenho qualquer dúvida que a [j] faria qualquer coisa por poder. Até que faria sentido ela não se contentar em ser repórter..."

            mc desconfiado "Mas ela manda e desmanda naquele lugar. O que mais ela poderia querer?"

            n "Eu não sei como explicar direito, porque eu não tenho certeza do que eu vou falar agora."

            mc "Ok..."

            n "Quando eu comecei a despontar, a [j] veio falar comigo. Ela praticamente chegou se atirando em mim."

            mc zerado "Não me diga..."

            if nathan_e2 == "seducao":

                n "Não sei se você ainda lembra, mas lá no condomínio da [j] eu te disse que eu me encaixava no que as pessoas chamam de pansexual."

                mc normal "Lembro sim, claro."
            else:


                scene nathan_pizzaria1 with Dissolve(1.0)

                n "Eu nunca te contei, mas eu me encaixo em algo que as pessoas chamam de pansexual."

                n "Isso quer dizer que eu não me atraio somente por homens e mulheres, não existe essa barreira de gênero pra mim."

                n "Se eu gostar de você, não importa se você é homem, mulher ou trans."

                mc normal "Entendi. É algo interessante."

                n "Sim, é meio raro."

                mc envergonhado "Mas não se preocupe que não tenho preconceito e talz."

                n "Não esquente, eu sei que você não é assim. Você é de boa, [mc]."

                mc normal "Valeu."

            n "Mas então... a primeira coisa que eu senti pela [j] foi repulsa. Eu conseguia sentir que aquela mulher não era comum também."

            n "Por mais sexy que ela fosse, eu só conseguia sentir que na minha frente tinha um tipo de monstro."

            mc serio "Por isso você também nunca conseguiu confiar nela pra passar a informação do seu contrato com a Blergh!."

            n "Sim. E quanto mais ela tentava se aproximar, mais eu me afastava dela."

            scene nathan_pizzaria4 with Dissolve(1.0)

            n "Até que as visitas dela começaram a se tornar mais assédio do que um contato profissional."

            n "Ela começou a me ameaçar. Vivia dizendo que eu tava mexendo com a pessoa errada, que ela era grande."

            n "Isso me assustou. Eu tinha acabado de fechar o contrato que eu tanto queria e ela disse que podia acabar com minha vida."

            mc desculpa "Deve ter sido foda..."

            n "Daí meio que eu comecei a falar um pouco sobre mim. O mínimo possível, só pra ela sossegar."

            n "A gente acabou saindo também... algumas vezes."

            "Por isso ele sabia onde ela morava..."

            n "E com o tempo eu acabei passando quase tudo sobre minha vida pra ela. Eu só não falei duas coisas."

            mc serio "O contrato..."

            n "E o lance que eu não era legalizado no país."

            n "Nem eu sabia direito disso na época pra falar a verdade."

            mc "Sei..."

            n "A [j] meio que tava na minha. Ela realmente achou que tinha me dobrado. Eu tava abrindo o bico e transando com ela."

            mc zerado "Era tudo o que ela queria."

            n "E foi bem aí que ela falou algo bem estranho."

            mc desconfiado "Hm?"

            scene nathan_pizzaria2 with Dissolve(1.0)

            n "Ela falou de um grupo."

            mc desconfiado "Grupo?"

            n "Essa é a parte que eu não entendo bem. Ela disse algo tipo assim: 'Você tá sendo um bom menino, acho que você pode entrar pro grupo'."

            mc "E depois disso?"

            n "Daí eu perguntei o que era esse tal de 'grupo'."

            mc "E ela?"

            n "Ela disse que só quem faz parte do grupo, sabe o que é o grupo."

            n "Ela não ia poder falar nada pra mim antes que eu fizesse parte dele."

            mc surpreso "Como assim?!"

            mc envergonhado "Tipo um grupo secreto?"

            scene nathan_pizzaria4 with Dissolve(1.0)

            n "Você nem deve acreditar em mim..."

            "Essa história de 'grupo' é doideira mesmo..."

            if n3_gravou:

                "Pera! Pera!"

                "A [j] falou... aquele dia na redação. Ela falou alguma coisa de grupo..."

                "Clube! Ela falou de um clube!"

                "Aquele dia... não lembro exatamente... mas ela falou tipo 'clube dos adultos'..."

                n "[mc]?"

                mc surpreso "Ah!"

            mc envergonhado "É, [n]... não é que eu não acredite em você. Eu só não entendi direito o que você quer dizer."

            n "Tipo... que grupo é esse?"

            mc desconfiado "Isso que eu não entendi..."

            scene nathan_pizzaria2 with Dissolve(1.0)

            n "Por isso que falei. Eu tenho certeza que ela tá envolvida em alguma coisa."

            "Um grupo..."

            n "Queria muito saber o que é isso... mas não tô nem um pouco afim de me meter com ela de novo."

            n "Quero o máximo de distância possível dessa filha da puta."

            mc desculpa "É o melhor mesmo. E talvez..."

            mc charmoso "Talvez eu possa ver isso pela gente."

            n "Você..."

            scene nathan_pizzaria1 with Dissolve(1.0)

            n "Isso seria incrível, [mc]. Claro que você vai falar pra mim tudo o que você descobrir, né?"

            mc charmoso "Com certeza."

            mc angustiado "Mas agora vamos pedir que eu tô morrendo de fome!"

            n "Haha... claro."

            n "Ah. Assim que abaixar a poeira, eu vou ter mais a confiança da Blergh! e daí eu queria te chamar pra um lance."

            mc normal "O que?"

            n "O que você acha de ir em um desfile comigo? Eles fazem umas festas gigantes e chamam a gente pra desfilar só pra distrair."

            mc zerado "É foda ter dinheiro sobrando, hein?"

            n "Nem fala. Mas o que você acha?"

            menu:
                "Uou! Quem sabe ver umas modelos...":


                    mc tarado "Uou... você vai me apresentar umas modelos amigas suas?"

                    n "Claro. Todas que você quiser, a gente é parceiro."

                    mc surpreso "Então demorou!"

                    n "Hahaha... Vejo que você é um homem de cultura."

                    mc concentrando "Eu sou um homem simples. Eu vejo modelos, eu falo com elas."

                    n "Entendi."
                "Muito massa, cara. Me avisa quando der.":


                    mc normal "Seria legal, cara. Com certeza."

                    n "Então assim que eu sentir que a barra tá limpa lá eu peço um lugar pra você no próximo evento."

                    mc charmoso "Valeu mesmo, [n]."

            n "Agora é hora da comida!"

            mc surpreso "Siiim!"

            jump nathan_e5_final
        "Tem razão. Vamos falar de outra coisa.":


            mc charmoso "Você tá certo. Tem tanta coisa pra gente conversar."

            if nathan_quente:

                "Essa é inclusive a chance de começar algo sério com o [n]. Não posso jogar essa oportunidade fora."

                menu:
                    "Eu acho que a gente devia falar sobre a gente.":


                        $ nathan_e5_beijo = True

                        mc charmoso "Eu tenho um assunto muito melhor. Falar sobre o que tá rolando entre a gente."

                        n "Com certeza é muito melhor falar de você do que da [j]."

                        scene nathan_pizzaria3 with Dissolve(1.0)

                        n "Na verdade... acho que é sobre o que eu mais queria falar agora."

                        mc charmoso "Que bom."

                        n "E sobre o que você quer falar?"

                        if nathan_beijo:

                            n "Sobre nosso primeiro beijo?"

                        if nathan_e3_beijo:

                            n "Quem sabe sobre o beijo no bar do [gar]?"

                        if nathan_e4_beijo:

                            n "Talvez o beijo no tribunal, no meio de todo mundo?"

                            n "Onde você tava com a cabeça aquele dia?"

                        mc charmoso "Pode ser sobre qualquer um..."

                        n "Ou talvez você queira saber mais sobre nosso próximo beijo?"

                        mc surpreso "Próximo?"

                        n "Eu tô sentindo que vai acontecer daqui a pouco."

                        menu:
                            "Que sorte a minha.":


                                mc safado "Então eu tô sortudo hoje."

                                n "Que bom que você pensa assim."

                                mc "Bom pra você também..."

                                n "Não discordo."
                            "Você não perde tempo mesmo, hein?":


                                mc envergonhado "Você não perde tempo mesmo, hein?"

                                n "A vida é curta, [mc], e eu acabei de sair do inferno. Não vejo a hora de chegar no céu."

                                mc "T-tá..."

                        n "Desde que a gente se conheceu no bar aquela vez, quando você queria saber mais sobre mim por causa da [j]..."

                        n "Desde aquele dia acho que eu senti algo diferente por você."

                        mc charmoso "Aquelas garotas em cima de você, igual um sultão, e você nem ligava. Foi engraçado..."

                        mc surpreso "Você até me ofereceu uma!"

                        n "Aquelas garotas não estavam me despertando interesse suficiente. Só queria que elas fossem embora."

                        if nge == "Garotas":

                            n "Você inclusive não aceitou e quis só ficar conversando comigo."

                            mc charmoso "Você também me chamou muito mais a atenção do que elas naquela noite."

                        n "Seu jeito... a coragem de vir falar comigo... sei lá, alguma coisa me disse que você era mais interessante."

                        mc charmoso "E?"

                        n "Com certeza foi mais interessante."

                        mc envergonhado "É..."

                        if nathan_e3_beijo:

                            mc charmoso "Você... você disse que quando os problemas acabassem a gente poderia ficar juntos."

                            n "Você ainda não mudou de ideia?"

                            mc "Não..."

                        mc "Eu..."

                        "Por que eu parei de falar?"

                        "Eu preciso falar o que eu tô sentindo. Não posso ficar com medo agora."

                        n "Você?"

                        "Eu quero algo mais com o [n]. Quero ficar com ele, namorar com ele. Ir pra cama com ele..."

                        "Desde o começo. Um monte de mina apareceu na minha vida, mas ele é a pessoa que eu quero ficar de verdade."

                        "Eu preciso ter coragem e falar."

                        menu:
                            "Eu quero namorar você, [n].":


                                pass

                        mc charmoso "Eu quero namorar você, [n]."

                        mc "É isso que eu tô sentindo. E é isso que eu quero."

                        n "[mc]..."

                        n "Você me inspira, sabe? Você sempre foi verdadeiro comigo."

                        scene nathan_pizzaria4 with Dissolve(1.0)

                        n "Eu queria ter essa força também..."

                        mc charmoso "Mas você tem. Você nunca fugiu do que eu sentia por você. Você também sempre foi sincero comigo."

                        n "Você acha?"

                        mc "Claro."

                        n "Só que... acho que alguma coisa mudou em mim."

                        mc preocupado "Como assim?"

                        n "Eu fico pensando o que vai acontecer com a gente se a gente assumir alguma coisa nesse sentido."

                        mc "Alguma coisa ruim você quer dizer?"

                        n "Exatamente. Olha o que a [j] fez. As pessoas vão sempre ficar de olho na gente."

                        n "O povo é mesquinho. Eles querem saber mais dos outros do que da gente."

                        mc desculpa "Você tem medo disso?"

                        n "Tenho..."

                        n "Eu nunca tive problema com minha sexualidade. Depois que eu encarei e descobri que eu não era como a maioria, foi normal pra mim."

                        n "Eu não vi isso como um problema."

                        n "Nunca achei errado gostar de homens e mulheres. Não me importa se a maioria não é assim. Pra mim, o que vale é o que tá dentro."

                        n "Só que... depois de tudo isso..."

                        n "Não consigo parar de pensar que não importa o que eu penso de mim. As pessoas vão sempre olhar pra mim de forma diferente."

                        n "Elas não se importam com o que eu penso sobre mim. Se ELAS não me acham normal, elas me tratam de outra forma. E nunca é coisa boa."

                        mc desculpa "[n]..."

                        n "Você entende o que eu quero dizer? São os outros que falam que eu tô errado. Eu nunca pensei dessa forma."

                        n "Por que as pessoas precisam se meter na vida dos outros, [mc]?"

                        n "Droga..."

                        mc "Sabe, cara... eu acho que ninguém tá feliz com sua própria vida."

                        mc "Então as pessoas procuram problemas na vida dos outros. Desse jeito elas podem aguentar um pouco mais a própria desgraça."

                        mc "Quando elas tão discutindo os problemas dos outros, elas conseguem fechar os olhos e não ver suas próprias merdas."

                        mc charmoso "Você é incrível por causa disso. Você quer viver sua vida. Nunca fodeu ninguém."

                        mc "O que importa pras pessoas se você gosta de homem ou mulher? A vida é sua. Você não faz nada pra ninguém."

                        mc "Mas eles precisam encontrar problema em você. E não é porque realmente tem, mas porque eles precisam achar algo."

                        n "Mas... como que a gente vai ficar juntos nesse caso?"

                        mc charmoso "Ué. Mandando eles tomarem no cu."

                        n "Mas, tipo-"

                        mc "Eu sei. Não é fácil. Mas a gente acostuma. Vão falar merda, mas tanta merda, que uma hora você nem vai ligar."

                        mc "A [j] ferrou sua vida, mas você tá aqui. O importante é ter confiança que depois da merda, sempre vem..."

                        n "A descarga?"

                        mc envergonhado "É... podia ter usado uma metáfora melhor."

                        n "Com certeza..."

                        mc zerado "..."

                        scene nathan_pizzaria1 with Dissolve(1.0)

                        n "Você tem razão. Não dá pra gente ficar escondidos com medo dos outros."

                        n "Se a [j] me foder de novo, eu aguento. Eu sou um garoto crescido."

                        mc charmoso "Isso aí. Não perder a vontade de viver nunca, não importa quanto ruim as coisas pareçam hoje-"

                        n "Sempre vai ter a descarga pra levar a merda."

                        mc zerado "Você não vai esquecer isso mesmo."

                        n "Desculpa acabar com sua aula de auto ajuda."

                        mc "Cretino."

                        n "Hahaha!"

                        mc envergonhado "Mas eu me empolgo às vezes mesmo."

                        n "Não se preocupe com isso. Você falou tudo, cara."

                        n "Se a gente deixar os outros entrarem na nossa cabeça, a gente tá perdido. Mas não é fácil..."

                        mc desculpa "Sim... eu falo tudo isso, mas não consigo também."

                        mc "Eu já fiz muita merda desde que mudei pra cá. Inclusive com as pautas... será que eu não fiz o mesmo que-"

                        n "Ei! Não vai ficar triste agora."

                        mc "Acho que eu comecei a pensar em coisas que eu fiz que não foram tão legais..."

                        n "Para de pensar besteira. Você não pode deixar seu parceiro alegre e ficar triste ao mesmo tempo."

                        scene cidade pizzaria_out_dia with Dissolve(1.0)

                        n "Levanta. Vem aqui."

                        mc desculpa "O que você tá fazendo em pé."

                        n "Já falei, vem aqui. Eu sei como te alegrar."

                        mc surpreso "Ei!"

                        scene nathan_pizzaria_beijo with Dissolve(2.0)

                        pause

                        "Hmmm..."

                        "..."

                        "Quando eu beijo o [n] parece que eu fico tão ansioso que minha cabeça apaga."

                        "É uma sensação tão forte..."



                        label n5_premium1:

                            pass

                        n "É bom, né?"

                        mc "Com certeza. Você beija muito bem."

                        n "Então... eu faço outras coisas bem... você sabe..."

                        mc "Você tá me convidando pra alguma coisa?"

                        n "O que você acha de você ir no banheiro comigo?"

                        mc "S-sério? Aqui?"

                        n "Se você tiver afim... eu tô."

                        menu:
                            "Ir com ele pro banheiro":


                                if not premium:

                                    call mensagem_premium from _call_mensagem_premium_14

                                    jump n5_premium1

                                mc "Foda-se. Eu só quero curtir você."

                                n "Isso aí. Vem comigo. Acho que é por aqui."

                                scene black with Dissolve(1.0)

                                "Não acredito que eu aceitei isso..."

                                scene d4_premium1 with Dissolve(1.0)

                                pause

                                mc "A gente realmente vai..."

                                "{i}cleck{/i}"

                                n "Já tranquei a porta. Vem aqui."

                                scene black with dissolve

                                scene n5_premium1 with Dissolve(1.0)

                                pause

                                mc "N-Nathan..."

                                n "Fazia tempo que a gente não ficava."

                                mc "É verdade."

                                n "Você sabe que é com você que eu me sinto melhor."

                                n "Espero que você curta ficar comigo também."

                                menu:
                                    "Claro que eu curto.":


                                        mc "Você sabe que eu curto muito."

                                        n "Que bom."
                                    "É só você que eu quero.":


                                        mc "Eu só quero você, [n]. Você é minha pessoa."

                                        n "[mc]... eu fico tão... hmm... quando você fala assim."

                                        n "Eu também quero ser seu."

                                scene n5_premium2 with Dissolve(1.0)

                                pause

                                n "Continua me beijando assim então."

                                mc "Hmm..."

                                n "Você também fica quente quando a gente tá juntos assim?"

                                mc "Claro. Eu não vejo a hora de sentir seu corpo."

                                n "Então sente. Você sabe quem que sentir você, né?"

                                mc "Você tá falando dele?"

                                n "Claro. Pega nele por favor."

                                mc "T-tá..."

                                scene n5_premium3 with Dissolve(1.0)

                                pause

                                n "Ah... assim... sua mão no meu pau é tão boa."

                                mc "Você já tá tão duro."

                                n "Ficar com você me faz ficar assim."

                                mc "E você é tão grande também. Tão duro..."

                                n "Mas continua me beijando... não dá toda sua atenção pra ele."

                                mc "Ah..."

                                mc "Eu vou me dividir entre vocês dois..."

                                n "Isso... ah..."

                                scene n5_premium4 with Dissolve(1.0)

                                pause

                                mc "Q-quanto mais eu pego... maior e mais duro você fica..."

                                n "É porque você pega gostoso, [mc]..."

                                mc "Eu também tô ficando duro pra caralho."

                                n "Então tira essa calça... coloca ele pra fora também."

                                n "Deixa eu ver seu pau também. Ele me deixa com tesão."

                                mc "Tá... vou tirar..."

                                n "Isso."

                                scene n5_premium5 with Dissolve(1.0)

                                pause

                                n "Assim mesmo, [mc]... deixa eu olhar pra você."

                                mc "Nossos dois caralhos assim... hmm..."

                                n "E a gente no meio da pizzaria. Isso só deixa tudo mais excitante."

                                mc "Sim... aah..."

                                n "Se alguém vê a gente aqui, enquanto a gente tá se pegando.. hmm..."

                                mc "Você gosta quando eu mexo assim?"

                                n "Sim... pega em nós dois, [mc]. Usa essa mão gostosa pra fazer a gente gozar."

                                menu:
                                    "Fazer ele gozar antes":


                                        mc "O seu pedido é uma ordem, gostoso."

                                        scene n5_premium6 with Dissolve(1.0)

                                        pause

                                        mc "Deixa eu trabalhar esse caralhão delícia."

                                        n "A-ah... que delícia, [mc]."

                                        mc "Seu pau que é uma delícia esfregando no meu assim."

                                        n "Hmm... e falando desse jeito, você quer que eu goze na hora, é?!"

                                        mc "Eu quero!"

                                        n "Então vai, [mc]! Continua pegando em mim!"

                                        scene n5_premium7 with Dissolve(1.0)

                                        pause

                                        mc "Hmm!"

                                        n "Ah! Que delícia!"

                                        n "Assim!"

                                        n "Hmm! Aahh!"

                                        mc "Goza pra mim, gostoso!"

                                        n "AAAGGH!"

                                        scene n5_premium7 with vpunch

                                        n "Aah... que delícia, [mc]!"

                                        mc "Gostou, hm?"

                                        n "Ainda... aah... caralho... que gozada boa..."

                                        mc "Hmm... gostoso."

                                        n "Deixa eu cuidar de você agora."
                                    "Mandar ele fazer um oral":


                                        mc "Não. Eu quero gozar. Eu quero sua boca agora, [n]."

                                        n "Hmm... Não consegue esperar, é?"

                                        mc "Não..."

                                        n "Deixa comigo. Tudo pro meu gostoso."

                                scene black with dissolve

                                scene n5_premium8 with Dissolve(1.0)

                                pause

                                mc "A-ah..."

                                n "Assim que você gosta, é?"

                                mc "É... eu tô quase lá já."

                                n "Calma... deixa eu aproveitar esse pau também."

                                mc "Hmm..."

                                "O Nathan me mamando assim é uma delícia."

                                "Ele é tão gostoso."

                                mc "A-ah!"

                                n "Eu tô começando a ficar excitado, [mc]."

                                scene n5_premium9 with Dissolve(1.0)

                                pause

                                mc "Aah... t-tô percebendo."

                                n "Deixa eu fazer você sentir gostoso."

                                mc "D-deixo... pode fazer assim!"

                                n "Deixa eu pegar em tudo, que é uma delícia."

                                mc "É sim.... aaahhn..."

                                n "Vai gozar?"

                                mc "Se você continuar acelerando desse jeito!"

                                n "Eu quero que você goze. Hmm... vai..."

                                n "Pode dar tudo pra mim. Joga toda sua porra em mim, gostoso!"

                                mc "Isso! Não para!"

                                "Eu vou gozar! Ele vai me fazer gozar mesmo!"

                                mc "A-ah! AAHNN!"

                                mc "Toma tudo, [n]!"

                                scene n5_premium10 with vpunch

                                pause

                                mc "AAAHHH!!"

                                n "Hmm!"

                                mc "Assim! Aahnnn!!"

                                mc "Delícia... que delícia..."

                                mc "Aah..."

                                n "Você que é uma delícia..."

                                mc "Quanto tempo que eu não gozava assim..."

                                n "Vem aqui, homem."

                                scene black with dissolve

                                scene n5_premium11 with Dissolve(1.0)

                                pause

                                n "Então você curtiu a vinda no banheiro."

                                mc "Agora que eu lembrei que a gente tá aqui ainda..."

                                n "Haha... bom saber que toda sua atenção tava na nossa ação aqui."

                                mc "Claro..."

                                n "Você é uma pessoa muito intensa, [mc]. Eu acho pessoas assim incríveis."

                                mc "Você que me chamou pra cá... nem vem..."

                                n "Tipo, você vive realmente as coisas. É bacana tá do lado de alguém assim. Que não julga, só curte."

                                mc "Pode contar comigo pra toda presepada que você tiver no meio."

                                n "Você também. Eu tô aqui pra você, gato."

                                mc "Agora bora dar o fora que, né... já abusamos..."

                                scene black with dissolve

                                n "Aliás... você tava nervoso e eu ia te beijar pra fazer você melhorar..."
                            "Vamos parar aqui hoje.":


                                mc "Banheiro assim é demais pra mim... acho que eu vou ter que ficar na vontade."

                                n "É uma pena... mas o beijo já ajuda."

                                mc "Hmm..."

                        n "E aí? Funcionou?"

                        mc "Nem sei mais o que eu tava falando..."

                        scene cidade pizzaria_out_dia with Dissolve(1.0)

                        n "Então funcionou."

                        show nathan n_flertando with dissolve

                        n "Mas pra falar a verdade, nem eu lembro. Você beija bem, [mc]."

                        menu:
                            "Eu sei.":


                                mc tarado "Eu sei, nem precisa falar."

                                n "Haha! O que eu tô fazendo com esse homem?"

                                n "Auto estima de mais não é bom também."

                                mc "Será?"

                                n "Hahaha! O monstro tá completo."
                            "Você também.":


                                mc charmoso "Você também."

                                mc "Eu me sinto muito bem quando a gente tá juntos."

                                n "Eu sinto isso também."

                                n "Isso me dá mais confiança que esse é o caminho certo."

                                mc "Eu também."

                        mc charmoso "Vamos esquecer os outros e viver a nossa história. É isso que eu quero agora."

                        n "Eu também."

                        show nathan n_vergonha with dissolve

                        n "Acho que a gente meio que deixou o garçom sem jeito e ele picou a mula."

                        mc feliz "Azar o dele."

                        n "E se a gente desse uma volta juntos pelo centro ao invés de comer aqui?"

                        mc normal "Quer saber, acho que é melhor mesmo."

                        n "Então vamos."

                        hide nathan with dissolve

                        mc surpreso "Calma!"

                        jump nathan_e5_final
                    "Eu não quero nada assim com ele. Foi só aquele beijo e pronto.":


                        "Até rolou aquele beijo entre a gente, mas foi só aquela vez. Não quero mais nada do tipo com ele."

                        "Deixa eu puxar um assunto."

            mc "Qual são os planos pra agora?"

            n "Pior é que nem sei, cara. Desde que esse inferno começou nem tive tempo de pensar nos próximos passos."

            n "Cara... eu sei que disse que não queria falar da [j], mas posso só falar um lance?"

            mc envergonhado "Claro. Fique à vontade."

            jump nathan_e5_cassia

    label nathan_e5_final:

        scene black with Dissolve(1.0)

        "..."

        $ tempo += 1

        scene mc onibus_noite with Dissolve(1.0)

        if nathan_e5_beijo:

            "Foi massa. A gente jogou no arcade, tomamos sorvete. Foi tipo um encontro mesmo."

            "Foi a primeira vez que eu vi o [n] sorrindo tanto depois daquela noite que a gente se conheceu."

            "Acho que finalmente as coisas vão começar a dar certo pra ele."

            mc "E pra mim também..."

            "Ele é um cara especial. Além de gato, é famoso, engraçado e sensível. Não tem nem mais o que pedir em uma pessoa."

            "..."

            "Só que ainda fico meio preocupado por causa da [j]. Será que ela desistiu dele?"

            "Ela deixou uma marca muito profunda nele. A ponto dele ficar com medo de tudo por conta dos outros."

            "Mas eu acho que eu consegui ajudar ele com isso. Ele parecia bem mais tranquilo."

            "Não vejo a hora da gente sair de novo."

            "Tomara que seja logo."
        else:


            "Mano... como eu comi."

            "O [n] é muito foda. Acho que é o melhor amigo que eu tenho aqui na capital."

            "O que ele falou da [j] explica muita coisa, mas esse negócio de 'grupo' me deixou ainda mais cabreiro."

            "Talvez ela teja metida em algo pior do que parece."

            "Eu vou descobrir o que eu puder sobre ela. Preciso lembrar de tudo o que ela já me disse. Tudo o que eu sei sobre ela."

            "Juntando todas as peças, talvez eu consiga desvendar esse mistério."

            "Mas agora só quero chegar na ilha e hibernar que eu comi muito."



    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    $ tempo = 3

    $ v27_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v27_fim","final","local")

    jump call_cidade

label nathan_evento6:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n6_save", extra_info="n6_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ nathan_e6 = "evento"
    $ nathan_cel_msg5_resposta = True

    if nathan_e4_beijo or nathan_e5_beijo:

        $ nathan_quente = True

    "O que será que o [n] quer? Parece urgente."

    scene ape_geral with Dissolve(1.0)

    if nathan_e5_beijo:

        "Aquele dia na pizzaria a gente ficou e depois aquele passeio pela cidade... foi bem legal."

        "Eu sinto que a gente já saiu como namorados, mas, sei lá, não rolou nada oficial."

        "Inclusive eu perguntei pra ele e parece que ele mudou de assunto na hora."

        "Se bem que ele tava mó preocupado depois de todo o lance da [j] e o processo de extradição. Não é fácil ele assumir assim."

        menu:
            "Se ele não assumir logo... sei lá...":


                "Olha, eu sei que ele tem os problemas dele, mas se ele não assumir a gente logo eu não sei... a fila anda."
            "Eu sei que na hora certa ele vai responder.":


                "Eu vou esperar ele. Eu sei que na hora certa ele vai ter coragem. Não adianta eu pressionar."
    else:


        "Na pizzaria ele falou de um tal grupo da [j]. Isso aí parece ser coisa séria."

        "Depois de tudo o que eu vi nessa cidade, dá pra imaginar o que isso significa."

    "Aliás, a [j] parece que deixou o [n] em paz depois do julgamento."

    "Quem será que ajudou o [n]? Ele só foi liberado por causa do trabalho dele."

    if cassia_nathan_entregou:

        "Eu entreguei os documentos da Blergh! pra [j]."

        "Será que foi ela? Não faz sentido... ela mesma que entregou ele na matéria."
    else:


        "Eu não entreguei os documentos da Blergh! pra [j]. Quem será que teve acesso a isso?"

    "Tem coisa nisso tudo que eu ainda não entendi. Mas é melhor eu ligar pra ele logo."

    "..."

    scene ape_celular_falando with Dissolve(1.0)

    n "[mc]?"

    mc "Oi, [n]. Tudo legal?"

    n "É... tudo. E você?"

    "Ele tá parecendo meio sem jeito."

    menu:
        "Tudo bem também.":


            mc "Aqui tá tudo legal também."

            n "Que bom..."
        "Aconteceu alguma coisa?":


            mc "O que foi? Você parece estranho."

            n "Eu? Ah... você tá falando por causa da mensagem?"

            mc "Também, mas agora você parece meio quieto, sei lá."

            n "Então..."

    n "Desculpa escrever daquele jeito, parece algo super sério, mas não é nada tão assim."

    if nathan_quente:

        mc "Relaxa. Você sabe que eu fico feliz de falar com você."

        n "Eu também, [mc]. Às vezes as coisas ficam corridas, mas eu fico esperando pra poder escrever."

        mc "Então? A gente vai sair juntos?"
    else:


        mc "O que aconteceu?"

    n "É... eu ia te chamar pra sair."

    mc "Sério? Onde?"

    n "Lembra que eu comentei que quando tivesse uma festa ou algum desfile, alguma coisa assim, eu ia te falar?"

    mc "Opa!"

    n "Isso aí. A Blergh! vai dar uma festa, é um lance meio exclusivo. Vai ter um desfile, mas é tudo informal. Só pra festejar mesmo."

    mc "Lance exclusivo então?"

    n "É. São poucas pessoas. Gente rica que investe na marca, familiares dessa galera. Acho que até a presidente da Blergh! vai tá lá."

    mc "Orra."

    menu:

        "Mas a gente vai poder ficar lá?" if nathan_quente:

            mc "Mas e aí? A gente vai poder se beijar lá ou o quê?"

            n "Haha... eu quero também, mas não sei. Como eu falei, é um negócio meio restrito, pequeno. Não sei se vai ter lugar."

            mc "A gente encontra um lugarzinho."

            n "Tá legal."

        "Vai ter uma modelo gata?" if not nathan_quente:

            mc "Tu acha que vai ter uma amiga gata modelo lá?"

            n "Uma delas pelo menos vai estar lá, porque já tá certo que ela vai desfilar. Se pá eu apresento pra você."

            mc "Demorou. Isso que é ser brother."

            n "Pode deixar."
        "Vai ser legal, cara. Pode contar comigo.":


            mc "Pode contar comigo, acho que vai ser bem massa."

            n "Fechou. Eu sabia que você ia curtir."

            n "Quem sabe tu não consegue até uma pauta?"
        "Será que não tem problema eu ir?":


            mc "Será que não tem problema mesmo eu ir? É algo mais fechado igual você falou..."

            n "Claro que não. Você vai como meu convidado. Pode ficar tranquilo."

            mc "Então beleza."

    n "A festa vai ser no prédio da Blergh! no centro."

    mc "Ah. Eu sei onde é. É lá no bairro dos ricos, né? Aquele prédio preto bem alto."

    n "Haha... isso mesmo."

    if n1_ajuda:

        mc "É. Eu vi lá no contrato quando você me deu as informações do seu contrato com eles."

        n "Ha, verdade. Faz tanto tempo isso agora..."

        mc "Verdade."
    else:


        mc "Eu vi o pessoal comentando na TV quando tavam falando do seu julgamento."

        n "Pode crer..."

    n "Então a gente se vê lá às oito?"

    mc "Combinado. Oito horas."

    n "Seu nome completo é [mcc], né?"

    mc "Isso."

    n "Tá, vou deixar seu nome na recepção. Vai ser tranquilo, não precisa se preocupar."

    mc "Tá legal."

    if nathan_e5_beijo:

        mc "Beijo."

        n "Beijo, [mc]."
    else:


        mc "A gente se vê."

        n "Até."

    scene ape_geral with Dissolve(1.0)

    "Caraca... uma festança dessas. Por isso que é bom conhecer gente famosa."

    "Pensando bem... eu achava que os famosos odiavam os paparazzi. Até que eu tô me saindo bem nesse quesito."

    "Acho que até agora ninguém me odeia, pelo menos não nesse nível do ódio..."

    mc zerado "É o que eu acho."

    if tempo < 3:

        "Bom... ainda é cedo pra eu me arrumar. Deixa eu ver o que tá passando."

        scene ape_tv with Dissolve(1.0)

        mc "Deixa eu ver o que tá passando aqui..."

        "..."

        mc "Um velho com câncer produzindo droga pesada pra ganhar dinheiro?"

        show black with Dissolve(1.0)

        $ tempo = 3

        "..."

        mc "Mentira que o cara descobriu tudo enquanto tava soltando um barro..."

        mc "Que seriado merda. Certeza que ninguém assiste isso."

    mc "Opa. Já são seis e meia. Melhor eu tomar um banho e me aprontar."

    scene ape_chuveiro with Dissolve(1.0)

    "Tava pensando agora... Faz tempo que eu não vejo a [j] aprontando. Ela tá quieta."

    if n3_gravou:

        "Daquela vez eu fiquei do lado dela e gravei o [n]. Ela acabou usando isso numa matéria e a revista acabou ganhando um bom público."

        "Acho que essa foi a última vez que ela me mandou fazer uma dessas."
    else:


        "Faz muito tempo que ela não me pede nada ilegal ou imoral."

        "Não sei se ela quieta desse jeito é bom ou não."

    "A [j] tem aquele jeitão dela, mas não dá ponto sem nó. É uma mulher que com certeza a gente tem que ficar com os dois olhos abertos."

    if cassia_e1 == "seducao":

        "Eu lembro aquele dia que a gente transou na casa dela. Foi muito bom... pelo menos a parte que eu consigo lembrar foi boa."

        "Sem dúvidas ela é super sexy. Ela entra muito fácil na minha cabeça."

        "Bem que podia rolar alguma coisa de novo com ela. Eu não negava, não. Só espero que ela não cobre minha alma em troca um dia."

    "Tô cheirando bumbum de nenê já. Bora."

    "Ah. Esse evento parece ser mais chique. Eu devia usar uma roupa melhor."

    python:
        if renpy.android:
            roupa_blazer = PythonSDLActivity.pegaBlazer()
            roupa_blacktie = PythonSDLActivity.pegaBlacktie()

    if roupa_blazer:

        $ n6_blazer = True

        "Sorte que eu tenho meu blazer. Vou usar ele então."
    else:


        "Pena que eu não tenho um blazer pra usar. Tenho que dar uma passada na loja de roupas e comprar."

        if roupa_blacktie:

            "Bom... eu tenho meu Black Tie, que é muito mais chique que um blazer imbecil, mas é coisa demais."

            "O Black Tie é pro Cassino, pra um lugar onde todo mundo usa esse tipo de roupa."

        "Vou ter que ir com a roupa de sempre mesmo. Fazer o quê..."

    scene black with Dissolve(1.0)

    "..."

    call locomocao from _call_locomocao_6

    "O bairro dos ricos fica meio longe."

    "É lá que levantaram os condomínios de luxo e o pessoal importante da cidade vive."

    if v18_fim:

        "É onde [caio] mora também..."

    "Cheguei."

    scene cidade centro10 with Dissolve(2.0)

    pause

    "Tem uns prédios gigantes aqui."

    "Pensando agora, quem sabe um dia eu também não me mudo pra cá? Eu posso ser grande, ouviram?!"

    mc zerado "O que eu tô fazendo?"

    "O prédio da Blergh! fica aqui perto."

    scene black with Dissolve(1.0)

    "..."

    "Recepcionista" "Boa noite. Qual o nome do senhor?"

    mc normal "Meu nome é [mcc]. Prazer."

    "Recepcionista" "Seu nome está na lista. Por favor, pode subir."

    mc "Valeu."

    "..."

    if n6_blazer:

        scene n6_mc_chegando_blazer with Dissolve(1.0)
    else:


        scene n6_mc_chegando with Dissolve(1.0)

    pause

    "Uou... que lugar massa."

    "Tem uma galera animada ali, mas tem um pessoal mais sério também. É menos gente do que eu tava pensando."

    "Agora eu tenho que encontrar o [n]. Ele já deve tá aqui. Acho que eu vou mandar uma me-"

    j "Pombinho?"

    mc "Pombinho?!"

    mc "[j]?!"

    scene n6_cassia1 with Dissolve(1.0)

    j "Nossa... você não muda mesmo, hein? Sempre gritando desse jeito..."

    menu:
        "Cobrindo o evento?":


            mc "Você aqui? Tá cobrindo o evento?"

            j "Não vim a trabalho. Se bem que... tudo é trabalho se você souber olhar as coisas da forma certa."

            mc zerado "Você tá sempre planejando alguma coisa..."

            j "Eu nunca estou planejando nada."

            mc "Tá bom..."

            j "Tudo já foi planejado, eu só estou executando o plano da melhor forma possível."

            mc envergonhado "Dá na mesma..."
        "Não esperava ver você aqui.":


            mc envergonhado "Desculpa o grito. Não achei que você ia estar aqui."

            j "Por que? Você ainda não entendeu que eu tenho amigos poderosos, pombinho?"

            j "Você não acha que pautas caem do céu... ainda mais as do tipo que eu me interesso."

            mc "Você tem razão..."
        "Que bom que você veio.":


            mc charmoso "Você me pegou desprevinido, mas que bom que você tá aqui."

            j "Será que eu marquei você desse jeito mesmo?"

            mc "Talvez você queira fazer alguma coisa mais tarde?"

            j "Com você?"

            mc "Não tem interesse?"

            j "Vamos ver."

    j "Mas e você? O que veio fazer aqui? Não acho que vo- Ah! O [n]..."

    mc normal "Sim. Ele que me convidou."

    j "Vocês realmente viraram amigos... quem diria..."

    menu:

        "Mais que amigos pra falar a verdade." if nathan_quente:

            mc charmoso "Mais que amigos pra falar a verdade..."

            scene n6_cassia3 with Dissolve(1.0)

            j "Imaginei... quem diria que essa coca é fanta, hein?"

            mc charmoso "Ficou com ciúmes?"

            j "Não se acha muito, pombinho. Você pode ficar com quem quiser, mas eu espero que você saiba que é bom ser meu aliado."

            mc zerado "Eu sinto que você só quer me ferrar."

            j "Não seja mal agradecido. Eu já fiz muito por você. E posso fazer mais."

            mc "..."
        "Não chega a tanto. Mais conhecidos...":


            mc desculpa "Não diria amigos... somos mais conhecidos."

            scene n6_cassia3 with Dissolve(1.0)

            j "Será que ele pensa assim também?"

            mc "Não sei, mas de minha parte, você sabe que eu sempre fiquei mais do seu lado."

            if n3_gravou:

                j "Eu sei. A gravação que você fez dele me garantiu uma excelente matéria."
            else:


                j "Você fala isso, mas quando pedi pra você gravar ele, você se recusou."

            mc "Mas eu falo sério."

            j "Eu preciso que você lembre que enquanto você for meu aliado, coisas boas vão acontecer com você."
        "Sim. A gente se fala de vez em quando.":


            mc normal "Sim. A gente acabou virando amigo e tá se falando de vez em quando."

            scene n6_cassia3 with Dissolve(1.0)

            j "Isso é bom pra você."

            mc desconfiado "Você dando valor pra amizade?"

            j "Obviamente. O [n] está muito bem posicionado. Ele tem acesso a gente poderosa e conhecida. Isso pode dar muitos frutos."

            mc zerado "Eu devia ter imaginado..."

    j "O que eu vi é que você ficou preocupado com a questão do processo."

    mc desconfiado "Com certeza... o cara ia ter que deixar o país. Ainda não entendi por que você fez isso."

    j "Ué? Essa era a informação que importava, pombinho. O resto era só uma introdução."

    mc "Desde o começo você ia falar sobre isso?"

    j "Claro. Você é lerdo desse jeito mesmo?"

    mc zerado "Ei..."

    j "O motivo pelo qual eu queria fazer do [n] alguém de relevância era justamente por isso."

    j "Publicar que um zé ninguém está ilegal no país não tem valor notícia. Mas se for alguém famoso, muda de figura."

    mc desconfiado "Calma... você tá me dizendo que você planejou falar dele, pra ele conseguir o contrato e virar famoso pra depois expor ele?"

    j "Qual é a parte que não faz sentido pra você?"

    mc envergonhado "Tô custando a acreditar que você planejou tantos passos assim..."

    j "Não tem nada de mais nisso. É algo comum. Colocar alguém em uma novela, seriado, filme, é construir uma imagem que depois pode ser explorada."

    j "A diferença é que eu tenho coragem de levantar imagens para depois destruí-las. Mas obviamente essa abordagem exige que você tenha vários..."

    mc desconfiado "Vários? Tem mais pessoas na sua 'fábrica de notícias'?"

    j "Quem sabe um dia, quando você realmente provar sua lealdade, eu te explique como esse mundo funciona, pombinho."



    mc zerado "..."

    if n3_gravou or not nathan_e5_beijo:

        scene n6_cassia7 with Dissolve(1.0)

        pause

        mc desconfiado "Lealdade? Isso tem alguma coisa a ver com o tal do grupo?"

        j "Claro. Tudo o que acontece tem a ver com eles."

        mc envergonhado "Aposto que você não vai me dar nenhum detalhe, né?"

        j "Ainda não, [mc]. Mas em breve, dependendo do que você decidir."

        mc desconfiado "Hm? O que eu decidir?"

        j "Depende de pra quem você mostrar sua lealdade."

        menu:
            "Se isso me der acesso, eu vou ser leal.":


                mc serio "Eu quero saber mais sobre isso. Se for me dar acesso, eu quero fazer parte."

                j "É tão fofo ver você falando sério desse jeito..."

                mc "Eu tô falando sério, [j]."

                j "Calma... eu sei, pombinho. Mas cada coisa no seu tempo."

                mc "..."
            "Minha lealdade é só pra mim mesmo.":


                mc serio "Eu só tenho lealdade comigo mesmo."

                j "Não digo que você está errado, mas algumas pessoas precisam de seguidores leais. Eles não gostam muito ambição."

                j "Se você realmente quer entender esse círculo e fazer parte dele, você vai ter que aprender que cada pessoa tem seu lugar."

                mc "Vamos ver..."

    mc charmoso "Deixando isso um pouco de lado... eu queria te perguntar um negócio."

    scene n6_cassia2 with Dissolve(1.0)

    j "Pode perguntar. Se você vai ter uma resposta depende da pergunta."

    mc normal "Já deu pra perceber que você é uma pessoa ambiciosa. Você mesmo disse que tem tudo planejado e tudo o mais..."

    j "..."

    mc "Qual é seu objetivo com tudo isso?"

    j "Não é óbvio?"

    mc envergonhado "Eu sei que é poder, dinheiro e essas coisas... mas assim... sua vida é só isso?"

    j "Hm?"

    mc "Eu nunca escutei nada da sua vida mesmo. Você, pra mim, nem parece uma pessoa. Você é mais um vilão de filme, sabe?"

    j "..."

    mc zerado "Sempre executando um novo plano maléfico ou querendo se dar bem às custas do [n] e até de mim..."

    j "Pombinho... esse tipo de conversa tira todo o tesão da relação, você entende?"

    j "Quando a gente tá transando com alguém, a gente não quer saber dessas coisas. Tem certeza que você quer ir por esse caminho?"

    menu:

        "Eu prefiro continuar transando. Esquece o que eu disse." if not nathan_quente:

            mc tarado "Esquece. Melhor a gente continuar com a chance de se pegar."

            scene n6_cassia5 with Dissolve(1.0)

            j "Foi o que eu pensei, pombinho. É duro resistir, né? Você sabe que eu sei dar gostoso..."

            mc safado "Com certeza. Você dá como ninguém..."

            j "Quem sabe hoje depois na festa, concorda?"

            mc "Com certeza..."

            jump n6_cassia_depois
        "Você é sexy, mas eu tô curioso pra saber esse outro lado.":


            mc envergonhado "Olha... você é sexy, claro... mas eu também quero conhecer esse outro lado porque eu nunca ouvi você falando disso."

            scene n6_cassia4 with Dissolve(1.0)

            j "Sinceramente, não imaginei que você ia responder isso... olha o que você tá perdendo."

            mc "Eu não acho que é assim também. Não é porque a gente vai ter uma conversa mais séria e pessoal que o tesão vai acabar."

            j "Eu não teria tanta certeza..."

        "Eu nunca quis nada disso com você." if nathan_quente:

            mc zerado "Não sei por que você tá falando isso pra mim, eu nunca quis transar com você."

            scene n6_cassia4 with Dissolve(1.0)

            j "Nojentinho... mas é que você não gosta da fruta... é a única explicação. Se bem que eu já consegui pegar gays também, viu?"

            mc "..."

            mc desculpa "E então? Eu realmente tô curioso pra saber isso de você."

    j "Bom... se você realmente quer saber sobre isso, o que eu posso responder?"

    mc envergonhado "Não é uma entrevista também haha... só queria que você falasse alguma coisa pessoal. Tipo, você tem pais? Marido?"

    j "Todo mundo tem pais, pombinho."

    mc zerado "Você entendeu."

    j "Não sei o que você pretende, mas eu não tenho problema de falar sobre mim se é isso que tá passando pela sua cabeça."

    j "Eu nunca gostei da minha família. Eles eram uns caipiras sem nenhuma cultura ou ambição. Tipo de gentinha medílcre que eu desprezo."

    j "Não via a hora de sair daquele antro de coitadismo que eles chamavam de casa."

    j "Vim pra cá pra ser alguém na vida. Eu não ia ser igual essa gente. Nunca."

    mc envergonhado "Você conseguiu seu lugar aqui."

    j "Claro! Foi do meu jeito. E não me importa se você ou qualquer outro fracassado vir falar que não tá certo e o caralho."

    j "Eu fiz o que tinha que fazer pra estar aqui. E eu ainda não acabei. Ainda falta um último degrau nessa escada."

    mc desconfiado "Um último?"

    scene n6_cassia6 with Dissolve(1.0)

    j "E... o que você falou? A outra coisa? Ah! Marido."

    mc envergonhado "É."

    j "Marido. Pra que eu vou querer marido? Um homem que se sente no mesmo nível que eu? Que vai falar que a gente tem que equilibrar a relação?"

    j "Isso é ridículo. Não existe relação equilibrada. Não nesse mundo porco de gente porca que a gente vive, pombinho."

    j "A gente não sabe viver assim. O mundo é na base do manda e obedece. Inteligente quem falou do rebanho desorientado."

    j "Eu não preciso de homem querendo mandar igual eu. Eu preciso que vocês me obedeçam. E é pro próprio bem de vocês. Porque alguém precisa saber o que está fazendo."

    mc zerado "Você pode falar bonito e tudo o mais, mas tô achando que você tá só me chamando de idiota."

    j "Imagina. Bom... era isso que você queria saber?"

    mc envergonhado "Eu sinceramente não sei o que eu tava esperando... mas acho que era só isso..."

    j "Comigo não tem meias verdades, [mc]. Se você tiver bolas pra aguentar a verdade nua e crua, pode me perguntar o que quiser."

    mc envergonhado "Tá..."

    label n6_cassia_depois:

        "{i}Boa noite, senhores e senhoras.{/i}"

    mc desconfiado "Hm?"

    j "Acho que o show vai começar."

    scene n6_passarela_geral with Dissolve(1.0)

    "{i}É com grande prazer que recebemos todos os amigos da Blergh! para esta festividade.{/i}"

    "{i}Todos vocês que aqui estão são de inestimável valor para nossa empresa e ficamos extremamente felizes por contar com vocês.{/i}"

    "{i}Enquanto vocês apreciam o melhor da culinária francesa, iniciaremos uma pequena apresentação de uma de nossas modelos.{/i}"

    "{i}Fiquem à vontade para acompanhar ou apenas curtam a festa como desejarem. A Blergh! agradece sua colaboração.{/i}"

    j "Quer ver o desfile?"

    mc normal "Vamo."

    scene black with Dissolve(1.0)

    if n6_blazer:

        scene n6_cassia_mc_blazer with Dissolve(1.0)
    else:


        scene n6_cassia_mc with Dissolve(1.0)

    pause

    j "As pessoas nem param de falar e mexer no celular. Bando de porcos sem cultura."

    menu:
        "Concordo. Povo sem respeito.":


            mc "Verdade. Parece que a galera não respeita mais as coisas."

            j "Finalmente você falou alguma coisa certa hoje. As pessoas não respeitam mais rituais e tradições."

            mc "Pode crer."

            j "..."
        "Você tá parecendo uma velha.":


            mc "Você tá é parece uma velha falando desse jeito."

            j "Velha? Respeitar os outros agora é ser velha? Você é desses jovens que falam 'foda-se' pra tudo?"

            mc "E se eu for?"

            j "Não seria uma surpresa. Nunca esperei muito de você mesmo. Geração perdida."

    mc "Você não é tão velha quanto tá parecendo agora. Você tem quanto? Trinta e pouco?"

    j "Não interessa. Não tem nada a ver com idade. É só ter a cabeça no lugar."

    "{i}Boa noite, senhores e senhoras!{/i}"

    "{i}Apresentando peças confeccionadas especialmente para esta noite, recebam nossa incrível Roxane!{/i}"

    if n6_blazer:

        scene n6_desfile1_blazer with Dissolve(1.0)
    else:


        scene n6_desfile1 with Dissolve(1.0)

    pause

    "Opa... essa é a modelo? Que garota diferente."

    j "Olha pra essa garota."

    mc "Que foi?"

    j "Não sei por que eles gostam desse tipo de imagem tão artificial."

    mc "Você tá falando da roupa ou da moça?"

    j "Não passa vergonha, pombinho. Olha para essa garota. Muito provavelmente ela nem é daqui."

    mc "Você diz de outro país?"

    j "Quase certeza. Só pelo jeito dela dá pra ver."

    mc "Entendi."

    j "Mas é normal empresas de moda fazerem isso. Digo, contratar modelos de vários locais do mundo."

    mc "Por que você acha?"

    j "Eles trabalham com o exótico, com o novo, o diferente. Ter modelos de vários locais aguça essa percepção."

    j "A Blergh! não pensa pequeno. Eles com certeza cresceram muito com toda a mídia gerada pelo pombinho. Vai deixar os... enfim..."

    mc "Hmm... Acho que o [n] me disse quando a gente se conheceu que a empresa não é muito conhecida."

    scene n6_desfile2 with Dissolve(1.0)

    pause

    j "Na verdade eles estão começando agora, mas o caso do [n] com certeza atraiu muitos olhares."

    mc "Mesmo sendo um caso de polícia?"

    j "Tanto faz, já que a empresa não estava envolvida no problema, mas na solução. Além disso, não se esqueça que eu lancei um dossiê completo sobre ele e a Blergh!"

    if cassia_nathan_entregou:

        j "Informação que eu consegui graças a você. Você ganhou muitos pontos comigo."

        mc "Pra mim eu nem tinha outra escolha..."

        j "Você tava envolvido com a bonequinha, né?"

        if priscila_namoro:

            "Espero que ela não saiba que a gente tá namorando..."

        mc "É. Você parecia uma inimiga terrível naquela época."

        j "Você não me vê assim mais?"

        mc "Mais ou menos, é duro falar exatamente..."

        j "Hm..."

    elif cassia_nathan_naoajudou:

        j "De alguma forma você também colaborou."

        mc "Mas eu nem aceitei ajudar ele."

        j "É. Mas o que você conversou com ele no bar àquela noite fez ele entregar as informações pra mim."

        mc "Ah... você até falou sobre isso."

        j "No fim, você ainda ganhou alguns pontos comigo."
    else:


        j "Informação que eu tive que conseguir sem você é claro. Essa foi foda, pombinho. Até hoje não engoli."

        mc "Ah, não. Você veio me ameaçando daquele jeito. Eu não ia me dobrar assim."

        j "É bom ter sangue frio, mas entrar em uma briga que você não tem como vencer é burrice."

        mc "Mas pelo jeito você conseguiu do mesmo jeito."

        if not nathan_p1:

            j "Não ache que você vai entregar uma pauta para o velho sem eu saber."
        else:


            mc "E o interessante é que até agora eu não entreguei ela pro chefe. Como você descobriu?"

            j "É um pouco óbvio, mas se você não matou a charada, vou deixar você brincando mais um tempo."

            "Charada? O que será que eu não tô entendendo?"

    scene n6_desfile3 with Dissolve(2.0)

    pause

    j "De uma forma ou de outra, a Blergh! cresceu muito e o [n] trouxe a visibilidade que eles queriam. Proteger ele virou questão importante."

    mc "Por isso que eles não despediram ele quando explodiu?"

    j "Nunca que eles iriam demitir ele. A não ser que eles soubessem que ele não conseguiria resolver a situação."

    mc "Então eles tinham noção que ele iria conseguir?"

    j "Olha... é um pouco cansativo conversar com uma pessoa tão verde igual você."

    mc "Verde?"

    j "Você não entende nada, não capta nada. É como jogar três varetas na mesa e você não conseguir formar um triângulo..."

    mc "Não exagere."

    j "Eles nunca iriam investir no [n] se eles não tivessem sentido. Estamos falando do mundo corporativo, idiota. Eles não dão ponto sem nó."

    j "Ninguém assina um contrato grande com um funcionário que você não sabe de onde veio ou pra onde vai."

    mc "Você tá me dizendo que eles já sabiam de tudo desde o começo?"

    j "Chegue à conclusão que quiser. Ou melhor... na conclusão que essa sua cabecinha conseguir."

    "A [j] fala de um jeito como se tudo o que aconteceu com o [n] já tivesse sido planejado... mas não pode ser isso."

    "Como eles iriam saber do que ia acontecer com ele? Que ele ia ser indiciado?"

    if n6_blazer:

        scene n6_cassia_mc_blazer with Dissolve(1.0)
    else:


        scene n6_cassia_mc with Dissolve(1.0)

    pause

    j "Cuidado que sua cabecinha não tá acostumada a pensar demais."

    mc "Você brinca, mas eu vou chegar lá."

    j "Talvez um dia. Mas eu não vou esperar. Agora que acabou, eu vou falar com pessoas mais importantes."

    j "A gente pode se ver depois. Talvez."

    mc "Vai lá. Eu vou procurar o [n]."

    j "Beijos, pombinho."

    if n6_blazer:

        scene n6_mc_chegando_blazer with Dissolve(1.0)
    else:


        scene n6_mc_chegando with Dissolve(1.0)

    "Caraca, eu falei um monte com a [j] hoje, mas eu sinto que ela me despreza às vezes."

    "É tipo como se ela falasse com alguém de uma casta inferior. Como se ela visse eu e outras pessoas de cima."

    "É foda, mas o que eu vou fazer? A mulher manda e desmanda lá na revista. Eu sou só um paparazzo iniciando a carreira."

    "???" "[mc]?"

    mc "Opa!"

    scene n6_nathan1 with Dissolve(1.0)

    pause

    if nathan_quente:

        n "Oi, senhor."

        mc charmoso "E aí, senhor."
    else:


        mc normal "Fala aí, [n]. Tava te procurando, cara."

        n "Opa. Tava ajudando a Roxane lá atrás."

    n "O que achou do desfile dela?"

    menu:
        "Foi massa. Ela é muito bonita.":


            mc "Foi muito bom. Essa Roxane é linda."

            n "Sim. Também acho. Ela tem uns traços tão marcantes. Eu acho incrível o quanto ela é linda."

            mc "É legal como eles têm esse lance de trazer pessoas de fora."

            n "Sorte minha e dela, certo? Bom... eu meio que sou daqui, mas nasci fora."

            mc "Verdade."

        "Preferia ver você lá." if nathan_quente:

            mc charmoso "Na verdade eu preferia você lá, né?"

            n "Haha... valeu. Mas você ainda vai ver muitos desfiles meus eu espero."

            mc "É só você me chamar. E principalmente pra moda verão, beleza?"

            n "Pode deixar, safado."

            mc "Vou ficar esperando."
        "Normal. Nada de mais.":


            mc envergonhado "Sei lá. Normal. Falar a verdade, nem prestei a atenção direito."

            n "Ah... não curtiu a modelo?"

            mc "Achei ela meio estranha. Com todo o respeito, claro."

            n "Ela tem traços que não são comuns em modelos, mas pra mim é isso que torna ela tão linda."

            mc "Entendi."

    scene n6_nathan2 with Dissolve(1.0)

    n "E o visual? O que você achou?"

    menu:
        "Ficou bom. Eu gostei.":


            mc "Eu curti. Ficou bom em você."

            n "Valeu."

            if nathan_quente:

                n "Só bom?"

                mc charmoso "Ficou gostoso. Melhorou?"

                n "Agora, sim."
        "Prefiro você com a cabeça raspada.":


            mc envergonhado "Não tá feio, mas eu prefiro você com o cabelo raspado."

            n "Sério mesmo?"

            mc "Não sei se é porque eu conheci você assim, mas tá tão diferente."

            n "Tá legal. Vou lembrar disso."
        "Nem deu pra te reconhecer. Sério.":


            mc "Sério, nem deu pra reconhecer você. Se não fosse sua voz, eu ia passar batido."

            n "Você tá exagerando."

            mc "Nada."

    n "Quando tem festa da empresa ou desfile, eles pedem pra gente usar um estilo diferente. Isso vale pra Roxane também."

    mc "Bacana. Não sabia dessa."

    mc "Aliás, eu vi o desfile dela com a [j]. Ela tava aí também, mas saiu faz pouco tempo. Falou que ia conversar com pessoas que interessam."

    n "Ah... entendi... essa aí não pensa direito no que fala..."

    mc envergonhado "O pior é que eu acho que ela pensa demais."

    n "V-verdade..."

    mc "..."

    n "..."

    mc desconfiado "Oi? Você tá legal?"

    scene n6_nathan3 with Dissolve(1.0)

    n "Ah... tô sim, [mc]."

    mc "Você parece meio desligado, não sei. Aconteceu alguma coisa?"

    if nathan_e5_beijo:

        mc charmoso "Ou tudo isso é confusão pelo que rolou entre a gente na pizzaria?"

        n "N-não... você sabe que eu curti muito o que rolou lá."

        mc desculpa "Você curtiu... mas quando eu te pedi em namoro, você não respondeu."

        n "Eu... é... eu..."

        mc envergonhado "Você..."

        n "Eu... eu sei que eu não te respondi direito. Mas eu acho que ficou claro que eu realmente sinto algo especial por você."

        mc charmoso "Eu sei. Mas então..."

    n "[mc]... eu tenho que falar uma coisa pra você. Não dá pra esperar."

    mc preocupado "O que?"

    n "É sobre tudo isso que tá rolando comigo e com a [j]... e com você também."

    mc "Comigo?"

    n "É. Se fosse só comigo, eu não ia ligar, mas isso envolve você também e isso tá me matando..."

    if nathan_quente:

        n "Eu sei que tá rolando um lance entre a gente. E se você sente que não é oficial é por minha causa."

        n "A culpa é toda minha por a gente tá nessa situação."

    n "Mas eu queria que você viesse tanto aqui hoje porque eu pretendo resolver isso com você. Eu quero te contar tudo o que tá rolando."

    menu:
        "Tudo bem. Eu quero ouvir e entender tudo.":


            mc normal "Tá legal. Não precisa ficar assim. Eu vou ouvir e tudo vai ficar legal, você vai ver."

            n "Eu não sei, [mc]. Você é um cara muito gente boa, mas eu acho que não é assim tão simples."
        "[n], eu não quero me meter no rolo de vocês.":


            mc desculpa "Isso realmente tem a ver comigo? Eu não sei se eu quero me meter nesse rolo de vocês."

            n "Não tem essa, [mc]. Você já tá metido até o talo nisso que tá rolando. Você só não entendeu ainda."

            mc desconfiado "..."

    "Caraca... do jeito que o [n] tá falando parece um lance sério de verdade."

    "Será que ele descobriu alguma coisa sobre a [j]? Será que tem a ver com o que ela tava falando antes?"

    "Eu nem tive tempo pra processar tudo o que ela tava me falando antes e agora essa? Bom... eu tenho que escutar e ver o que é."

    mc serio "Certo. Parece sério de verdade, então vamos com calma."

    scene n6_nathan4 with Dissolve(1.0)

    n "Calmo é impossível pra mim, mas só me escuta por favor. Depois você pode me falar o que você quiser."

    mc "Tudo bem."

    n "Assim... eu não vou conseguir falar tudo certinho, na ordem, igual um texto de uma assessoria de imprensa. Mas é tudo verdade."

    n "Por mais louco que pareça, preciso que você acredite em mim."

    n "A verdade é que todo o rolo que a [j] fez sobre mim na verdade era pensando em você."

    mc desconfiado "Em mim? Como assim?"

    n "Espera. Só escuta."

    mc desculpa "Ok. Malz."

    scene n6_nathan5 with Dissolve(1.0)

    pause

    n "Eu menti pra você. Desde o começo. Eu e a [j]... a gente se conhece muito melhor do que a gente deu a entender."

    mc preocupado "..."

    n "Desde a primeira vez que a gente se viu no bar. Tudo já tava combinado. Tudo."

    mc preocupado "Como assim tudo? Até o negócio de você estar ilegal no país? Não acredito."

    n "Sim... tava..."

    mc "Mas você ficou muito puto quando viu a matéria!"

    n "Eu sei... mas ela que me pediu. Ela queria que eu fosse lá quando você estivesse e fizesse aquilo."

    mc desculpa "Não acredito..."

    n "Na verdade eu realmente fiquei um pouco com medo. Aquele nervoso que eu senti não era só encenação. Isso é verdade também."

    mc "[n]... isso... eu nem sei o que falar."

    scene n6_nathan6 with Dissolve(1.0)

    pause

    n "Olha... foi tudo um plano dela com os amigos dela. Eles queriam levantar a Blergh! e eu precisava de um emprego."

    n "Ela me prometeu que se eu fizesse minha parte, a Blergh! iria crescer e eu ia estar feito na capital pra sempre."

    mc "Quando você disse... que seu contrato tava atrelado ao quanto você pudesse trazer de visibilidade pra marca, você tava falando da extradição?"

    n "Também... desde o começo a [j] queria que isso fizesse parte. Mas eu fiquei com medo. Eu queria desistir..."

    n "Pra mim era impossível que a [j] tivesse tudo sob controle, daí eu surtei."

    mc desculpa "Mas ela tinha..."

    n "Sim... não sei se ela comprou a juíza ou sei lá, mas ela simplesmente aceitou o contrato com a Blergh! e tudo acabou rápido igual começou."

    mc serio "E no processo a Blergh! ganhou um monte de espaço na mídia e ainda saiu como a empresa que salvou você."

    n "Quando souberam que a Blergh! não me demitiu, eles receberam visitas de ativistas e grupos de apoio aos direitos dos trabalhadores..."

    n "O pessoal de esquerda adorou o fato que não me viram como problema. E a Blergh! capitalizou, claro."

    mc desculpa "Mal sabiam eles que desde o começo..."

    scene n6_nathan7 with Dissolve(1.0)

    n "Esse é o mundo dos negócios, [mc]. O que importa não é a verdade, mas o que as pessoas vêem."

    menu:
        "E o que isso tem a ver comigo?":


            mc "E o que tudo isso tem a ver comigo? Por que você disse que o principal era comigo?"

            n "Então... tudo o que eu queria era falar sobre isso."

            n "A [j] e o grupo dela estão planejando alguma coisa grande e envolve você."

            n "Ela queria, desde o começo, saber se você entraria no jogo deles. Ela precisava que você aceitasse as coisas."

            mc desconfiado "Tipo me testando?"

            n "Tipo isso. E até eu nem podia tá falando isso pra você. Eu não sei o que ela vai falar quando descobrir, mas eu cansei, sabe?"

            n "Olha, [mc]... quando a gente se conheceu lá no bar, eu não imaginava que as coisas iam acontecer como aconteceram."

            if nathan_quente:

                n "Eu nunca pensei que ia rolar alguma coisa entre a gente."

                if nathan_e5_beijo:

                    n "E depois de tudo o que a gente conversou na pizzaria, eu tenho certeza que eu quero ficar com você."

                    n "É isso que eu quero pra mim. Eu sei disso."

                n "Mas não dava pra eu ficar com você antes de te falar tudo. Antes de contar tudo o que eu sabia."

                mc desculpa "[n]... isso é muito sério..."

                n "Eu sei! Se eu soubesse que eu ia gostar de você desse jeito, eu nunca teria aceitado nada disso, [mc]! Acredita em mim!"
            else:


                n "A gente acabou virando amigos e a forma que você me ajudou no julgamento... Você só não merece isso, cara."

            n "Você não merece ser só um... sei lá... um brinquedo na mão dessa mulher."
        "Chega. Eu não quero mais saber disso.":




            mc desculpa "Tá. Sei lá se eu entendo, se eu concordo. Eu cansei. É coisa demais."

            n "Mas eu ainda não falei o que importa."

            mc serio "Não me interessa. Eu cansei."

            n "[mc]... eu..."

            mc "Para, por favor."

            n "T-tá..."

    mc preocupado "[n]... eu não sei direito o que falar..."

    n "Eu sei que é muita coisa... e eu também enganei você. Eu sei que você tá muito puto comigo agora."

    n "Mas se a gente vai continuar se falando..."

    if nathan_quente:

        n "... e talvez até alguma coisa a mais..."

    n "Então eu tinha que falar tudo isso pra você. Desculpa se eu tô sendo egoísta de jogar tudo isso em você agora."

    mc desculpa "Caralho..."

    "Como eu nunca pensei nisso? O [n] e a [j] juntos? Mas ele tava sempre falando mal dela."

    "Tem que ter alguma coisa errada nisso. E como eu posso confiar nele agora depois disso tudo?"

    scene n6_nathan8 with Dissolve(1.0)

    n "[mc]..."

    if nathan_e5_beijo:

        "Depois do nosso beijo na pizzaria eu tinha certeza que a gente ia ficar juntos..."
    else:


        "Cada vez mais eu tava vendo ele como um parça, coisa que eu nem tenho nessa merda de cidade."

    "Mas como? Como eu vou confiar em alguém que mentiu pra mim por tanto tempo?"

    "O que eu falo pra ele?"

    menu:
        "[n]... eu preciso de um tempo pra pensar...":


            mc desculpa "Eu preciso de um tempo pra pensar. Eu não quero mais falar com você até eu pensar direito sobre isso."

            n "Claro... me desculpa, [mc]. De verdade."

            mc "A gente vai conversar mais sobre isso outra hora, outro dia. Mas agora eu só quero entender."

            n "Tudo bem. Eu sei que não é simples. Eu não queria jogar tudo em você de uma vez, mas eu tinha, de verdade."

            mc "Calma. Eu não tô falando nada. Isso é um negócio sério e eu preciso pensar direito no que isso significa."

            mc "Por isso, não quero mais falar sobre isso hoje."

            n "Tá, eu entendo. Eu só queria falar mais uma coisinha."

            mc serio "Fala..."

        "Eu não me importo. Eu QUERO me unir à [j]." if n3_gravou or cassia_e1 != "nathan":

            mc concentrando "Olha... com certeza isso era algo que eu não esperava. Imaginar que você... esse tempo todo..."

            n "Eu sei... desculpa mesmo..."

            mc "Eu devia ficar muito puto com você, mas a verdade é que eu quero fazer parte do grupo da [j]."

            n "S-sério?!"

            mc serio "A [j] tem fontes poderosas e influência na revista. Acho que ela pode ser uma boa parceira."

            n "A [j] é uma víbora, [mc]. Você é louco de querer qualquer coisa com essa mulher."

            mc "Eu não posso, mas você aceitou ela rapidinho. Com você não teve problema, certo?"

            n "Não quero ficar de hipocrisia, mas eu não tinha nada, [mc]. Era isso ou nada. Você tá seguindo seu caminho."

            n "A [j] não é confiável. Ela só se preocupa com ela. Se ela achar que você tá atrapalhando, ela vai te jogar fora."

            mc concentrando "Não se preocupe que eu vou dar meu jeito."

            n "..."

        "Eu entendo... não quero que isso estrague o que a gente tem." if nathan_quente:

            mc desculpa "[n]... isso que você fez é muito sério... eu confiei em você. Como que você fala uma coisa dessas agora?"

            n "Eu sei... eu me senti muito mal com isso. Ainda mais por ser você, [mc]. Desculpa, de verdade."

            mc "Eu queria ter um lance sério com você. Agora você joga uma bomba dessas."

            n "Mas é por isso que eu tinha que falar! Você entende? Eu não tinha nada, [mc]. Era isso ou nada."

            n "Eu não quero justificar, eu sei que eu errei. Mas eu queria que você visse meu lado."

            scene n6_nathan9 with Dissolve(1.0)

            mc concentrando "Eu entendo... o pior é que não sei se eu posso julgar você, sendo que eu tive que fazer a mesma coisa."

            mc desculpa "Entregar segredos das pessoas que eu conheço não tá certo também."

            mc "Só que é claro que a confiança é abalada. Ainda mais quando é com alguém que a gente quer um lance sério."

            n "Eu sei... mas eu tô falando sério..."

            if nathan_e5_beijo:

                n "O que rolou no nosso último encontro foi real. Eu realmente quero algo sério com você."

                mc concentrando "Eu também quero isso..."

            n "E se a gente... esquecesse tudo isso por agora e só fosse pra um lugar mais reservado. Ah! Tem o camarim, não tem ninguém lá hoje."

            "Esquecer tudo? Será que tá certo só esquecer que ele mentiu pra mim e me manipulou... igual... igual a [j] faz?"

            "Eu gosto muito do [n], eu já cheguei nessa conclusão... eu quero ter algo sério com ele, de verdade."

            "Se fosse qualquer outro dia, eu ia aceitar ir pro camarim com ele na hora, mas depois do que ele me falou, eu não tenho certeza..."

            menu:
                "Vamos esquecer isso por hoje e sair daqui.":


                    $ nathan_e6 = "seducao"

                    mc concentrando "É... acho que é uma boa."

                    scene n6_nathan1 with Dissolve(1.0)

                    n "Ufa... Que bom, [mc]. Achei que você não ia aceitar. Mas eu quero começar tudo com você. Tudo legal agora."

                    mc charmoso "Bora. Vamos pra esse camarim aí."

                    n "Demorou."

                    scene black with Dissolve(1.0)

                    jump nathan_e6_seducao
                "Eu não posso. Eu preciso pensar.":


                    mc desculpa "Não dá pra só esquecer as coisas assim, [n]. Eu preciso pensar no que eu vou fazer agora."

                    n "[mc]... eu realmente não queria..."

                    mc "Tudo bem."

    n "Olha. A [j] tá planejando alguma coisa grande. Claro que ela não me contou tudo, e eu tô sendo sincero. Não sei o que é."

    n "Mas eu sei que ela precisa de você pra isso. Ela vai entrar em contato com você e vai ser um negócio grande. Então se prepara."

    mc serio "Ok... obrigado pelo aviso."

    "???" "Terminaram? Posso interromper os dois agora?"

    mc desconfiado "Hm?"

    scene n6_nathan_roxane with Dissolve(1.0)

    pause

    n "O-oi, [ro]..."

    ro "Não quero incomodar os dois. Só vim confirmar se esse é mesmo o tal do [mc] que você tá sempre falando."

    n "Sim... [mc], essa aqui é minha amiga e modelo da Blergh! também, [ro]."

    ro "Muito prazer. O [n] fala bastante de você. Só queria confirmar se você realmente era um homem ou uma espécie de deus."

    menu:
        "Mais um adorador eu passo pra esse estágio.":


            $ roxane_seducao += 1

            mc charmoso "Acho que mais um adorador, eu já troco de homem pra deus pelos meus cálculos. Quer fazer as honras?"

            ro "Por enquanto não, mas quem sabe no fim da noite?"

            mc "Se você me der uma chance, vai ver que eu mereço."

            ro "Engraçado você é, já é um começo."

            mc "Obrigado. "
        "O [n] que é bobo.":


            $ roxane_seducao += 1

            mc envergonhado "O [n] que é bobo. O famoso aqui é ele."

            ro "Humilde você."

            mc "É sério."

            n "O [mc] é super de boa. Eu falei isso pra você."

            ro "Isso é bacana. Tá em falta no mundo gente assim, que não quer aparecer."

            n "Com esse negócio de rede social, o que as pessoas mais gostam é aparecer."

            mc "Nem uso isso... mas é falta de tempo mesmo haha..."

            ro "Já ia pedir pra me add, então deixa."

            mc "Haha..."
        "Prazer.":


            mc desculpa "Prazer..."

            ro "Aconteceu alguma coisa?"

            n "Ah... é que a gente tava falando de um negócio pesado."

            ro "Ah... desculpa me intrometer."

            n "Nada. Tá tudo legal."

            ro "Então esse é o famoso [mc]?"

            mc "..."

            n "É, sim. Eu te falei dele, né?"

            ro "Até um pouco demais..."

            n "Exagerada."

            mc envergonhado "Hehe..."

    ro "Eu não quero ficar aqui atrapalhando vocês."

    n "Eu já tô de saída... eu conversei o que eu precisava com o [mc]. Só má notícia."

    ro "Que coisa..."

    mc desculpa "Não é nada de mais..."

    n "Vou nessa então. [mc], pensa com calma e depois a gente conversa. Até."

    mc "Tá bom. Até."

    ro "Ei."

    mc desconfiado "Hm?"

    scene n6_roxane with Dissolve(1.0)

    ro "Você tá parecendo meio pálido. Quer conversar?"

    if not nathan_quente:

        "Opa... uma linda dessas... Só um idiota recusaria isso. Mas justo hoje?"

    "Conversar com ela agora? Será que eu tô no clima?"

    menu:
        "Claro. Seria um prazer.":


            $ nathan_e6 = "roxane"

            $ roxane_seducao += 2

            mc charmoso "Quem negaria um convite desses? E eu preciso mesmo tirar um pouco a cabeça disso aqui."

            ro "Perfeito. Vem comigo. Eu quero tirar essa roupa aqui e falar com você mais à vontade."

            mc "Claro. Por aqui?"

            scene black with Dissolve(1.0)

            "..."

            ro "É aqui. Fica tranquilo que hoje não tem ninguém no camarim. Ele foi só pra mim."

            scene n6_camarim with Dissolve(1.0)

            pause

            mc normal "Muito bacana o lugar."

            ro "Ah, é bem legal mesmo. Eu vou trocar de roupa, se você puder não olhar pra este lado, tá?"

            mc surpreso "C-como?!"

            ro "Calma. É rapidinho."

            mc envergonhado "T-tá legal."

            "..."

            ro "Você ficou sem jeito mesmo?"

            mc "N-não tava esperando que você ia se trocar comigo aqui."

            ro "Não tem problema. Isso é normal. Geralmente tem tanta gente no camarim. Claro que são profissionais, mas eu acabei me desinibindo um pouco."

            mc envergonhado "Entendi. Interessante."

            "Não acredito que ela tá se trocando do meu lado... que mina doida..."

            "Será que ela vai notar se eu der uma olhadinha como quem não quer nada?"

            "Merda! O que eu tô pensando? Isso é muito coisa de tarado... de jeito nenhum..."

            "Mas..."

            menu:
                "Claro que não!":


                    $ roxane_seducao += 1

                    "Claro que não! Tenho que resistir!"

                    "Vou até fechar os olhos."

                    scene black with Dissolve(1.0)

                    pause

                    "..."

                    ro "Tá com o olho fechado? Que fofo... relaxa, moço."

                    mc envergonhado "T-tá tudo legal..."

                    "..."
                "Só uma olhadinha...":


                    "Talvez só uma olhadinha..."

                    mc tarado "..."

                    scene n6_roxane1 with Dissolve(2.0)

                    pause

                    mc surpreso "..."

                    ro "Oi?"

                    mc safado "A-ah! Você a-a-ainda não acabou?"

                    ro "Eu ia te avisar... mas relaxa. Deixa eu só sentar aqui."

                    mc tarado "Ok."

            ro "Vem aqui."

            scene n6_roxane2 with Dissolve(2.0)

            ro "Aaah... que delícia... Agora sou outra pessoa!"

            ro "Aquele sapato, aquela roupa me apertando... você nem tem noção como é."

            mc envergonhado "Imagino..."

            "Essa mina "

            ro "Agora deixa eu falar um negócio. O Pequeno Príncipe tava certo quando falou que o melhor de usar uma bota apertada é quando a gente tira."

            ro "Ufa... é simplesmente maravilhoso quando a gente sai dessa coisa que prende a gente."

            ro "Vocês homens deviam agradecer as mulheres que passam por isso pra ficarem bonitas."

            mc "Com certeza. A gente fica agradecido."

            ro "Mas me fala..."

            scene n6_roxane3 with Dissolve(1.0)

            pause

            mc envergonhado "O-opa..."

            ro "Você realmente trabalha para aquela revista que fica na ilha?"

            mc desconfiado "Hm? Sim, por que?"

            ro "É um trabalho bem interessante. O [n] me contou algumas coisas sobre você e aquela mulher [jc]."

            mc envergonhado "É um trabalho normal. Tem seus lados bons e ruins. Pelo menos eu posso viver aqui na capital."

            ro "Deve ser mais interessante do que o meu, que é só andar de um jeito estranho em cima de um palco."

            menu:
                "É... Eu acho que eu prefiro o meu mesmo.":


                    mc envergonhado "É. Aí vou ter que concordar. Eu prefiro o meu. Não seria um bom modelo."

                    ro "Tem certeza? Quando você faz um olhar confiante, você até que engana."

                    mc "Haha... obrigado, mas não mesmo."

                    ro "Hmm..."
                "Eu acho modelos super sexy.":


                    $ roxane_seducao += 2

                    mc charmoso "Andar estranho? Eu acho modelos super sexy. Vocês andam com tanta confiança."

                    ro "Dá vontade que a gente pise em você?"

                    mc envergonhado "Haha... aí são suas palavras."

                    ro "Tô brincando. E obrigada. É legal saber que você acha as modelos sexy."

                    mc charmoso "Quando você desfilou hoje, não conseguia parar de olhar pra você."

                    ro "E eu vi. Fiquei lisongeada."
                "Não é assim tão simples. Tenho certeza.":


                    $ roxane_seducao += 1

                    mc normal "Nem fala isso. Eu sei que não é assim tão simples. Vocês sofrem."

                    ro "Obrigada, mas só tava brincando. Eu gosto da minha profissão e me sinto super bem como modelo."

                    ro "E agora que a Blergh! tá crescendo, só vejo a coisa melhorando."

                    mc normal "Fico feliz. Você é linda e hoje eu vi você desfilando, achei incrível."

                    ro "Foi só por diversão hoje, mas obrigada."

            scene n6_roxane4 with Dissolve(1.0)

            ro "Só mais uma coisinha que eu não quero te segurar muito."

            ro "Eu sei foi você que ajudou o [n] a ganhar visibilidade na mídia. Você e a sua revista."

            ro "Isso foi realmente muito importante pra gente. Se algum dia eu puder fazer algo por você, pode me pedir."

            ro "Eu não tenho certeza se uma simples modelo pode fazer muito, mas se estiver ao meu alcance, pode contar comigo."

            mc "Valeu, [ro]."

            ro "Sabe, [mc]..."

            mc envergonhado "O-oi."

            ro "Às vezes Deus escreve certo por linhas tortas. Espero que a gente possa se encontrar de novo um dia."

            ro "Gostei muito de conversar com você."

            if roxane_seducao == 6:

                scene n6_roxane5 with Dissolve(1.0)

                pause

                ro "E acho que gostei mais do que eu imaginava. Você foi encantador esta noite."

                mc charmoso "Obrigado. Você também é... encantadora."

                mc "Vou estar ansioso pra gente se ver novamente."

                ro "Talvez eu esteja usando um pouco mais de roupa. Tudo bem pra você?"

                mc "Se você me compensar de outras formas, sem problemas."

                ro "Prometido."
            else:


                mc normal "Eu também. Vou esperar uma próxima chance da gente se ver."

                ro "Vai chegar logo."

            ro "Vai com Deus, moço."

            mc charmoso "Até."

            jump nathan_e6_depois
        "Desculpa, mas não tô no clima.":


            $ nathan_e6 = "nenhum"

            mc desculpa "Olha, eu normalmente não recusaria um convite desses, mas hoje eu realmente não tô no clima."

            ro "O [n] falou... fica tranquilo. Quem sabe um outro dia."

            mc envergonhado "Quem sabe? Seria massa."

            ro "Até outro dia."

            mc "Falous."

            scene black with Dissolve(1.0)

            "Deixa eu ir embora."

            jump nathan_e6_depois

    label nathan_e6_seducao:

        $ nathan_namoro = True

        "..."

        scene n6_camarim with Dissolve(1.0)

        pause

        n "Lar doce lar. A gente passa mais tempo aqui do que na passarela mesmo."

        mc envergonhado "Imagino..."

        if n6_blazer:

            n "Tira esse blazer e essa blusa. Fica à vontade, se não eu vou me sentir pelado aqui."

            mc charmoso "Haha... Beleza. Vou sentar aqui, tá?"

            n "Fica à vontade."

            scene n6_nathan_mc2 with Dissolve(1.0)

            pause
        else:


            n "Chega mais."

            mc "Posso sentar aqui na mesa?"

            n "Fica à vontade."

            scene n6_nathan_mc2 with Dissolve(1.0)

            pause

        mc charmoso "É a primeira vez que eu realmente vi como é seu trabalho..."

        n "Desculpa as coisas não terem saído melhor."

        mc desculpa "Tipo, por um lado eu fico feliz de você finalmente ter me falado tudo isso."

        n "Eu até ia falar antes, mas conforme a gente foi se conhecendo, eu fiquei com mais medo de contar. Achei que você não ia mais querer falar comigo."

        mc envergonhado "A [j] vai ficar doida quando ela descobrir que você contou tudo."

        n "Depois eu vejo isso. Essa mentira tava tirando meu sono. Eu sei que eu já falei isso, mas você não merece. Você é muito foda, [mc]."

        mc desculpa "Tudo bem. Depois a gente fala sobre isso."

        n "Tá legal..."

        mc charmoso "Agora eu quero saber como você vai se desculpar comigo por ter estragado a festa."

        if n6_blazer:

            scene n6_nathan_mc_blazer with Dissolve(1.0)
        else:


            scene n6_nathan_mc with Dissolve(1.0)

        n "Ah... não consigo pensar em nada..."

        mc "Nada mesmo?"

        n "Bom... talvez uma coisa..."

        mc "Antes, o que você tá achando de trabalhar na Blergh!? Era o que você esperava essa vida?"

        n "Sim, eu tô gostando. É um pouco corrido e eu viajo bastante. Depois que o rolo do processo acabou, dei uma porrada de entrevistas."

        n "Eu também tenho que mudar bastante o visual. A gente usa maquiagem, peruca, passa por sessão de uma porrada de coisa."

        n "Mas no geral eu tô gostando muito."

        mc "Que bom. Parece que não tem emprego perfeito, né?"

        n "Você também tem suas barras... eu tô ligado."

        mc "Opa. Se aparecer uma notícia aí, você tem obrigação de me falar."

        n "Pode deixar...."

        mc "É..."

        n "Bom... chegou a hora de eu me desculpar com você."

        mc "Chegou já?"

        mc "O-opa..."

        scene n6_nathan_mc3 with Dissolve(1.0)

        pause

        n "É que eu tô bastante arrependido e tô louco pra pedir desculpas."

        mc "Que garoto bonzinho você é... todo arrependido..."

        n "Viu só? Você fez a escolha certa de me escolher..."

        mc "Ainda não tenho certeza."

        n "Então acho que eu vou ter que me esforçar um pouco mais."

        mc "Você t-"

        scene n6_nathan_mc_beijo with Dissolve(1.0)

        pause

        "Hmm... eu tava precisando disso."

        "Tava precisando esquecer de toda essa história."

        "Nada como beijar o [n] pra ajudar..."

        window hide

        pause

        n "Calma que hoje eu quero mais."

        mc "M-ma-"

        scene n6_nathan_mc_beijo2 with Dissolve(1.0)

        pause

        n "Hoje eu só te solto quando você quiser namorar comigo de novo."

        mc "Eu sou um refém então?"

        n "Sim."

        window hide

        pause

        mc "Se é o único jeito..."

        scene n6_nathan_mc3 with Dissolve(1.0)

        n "Então a gente tá namorando? Eu tenho mais fôlego, hein?"

        mc "Haha... sim, por mim, sim. Mas é você que ainda não falou."

        n "Claro que eu quero. Eu quero namorar você e ser só seu, [mc]."

        mc "Tá... mas não precisa ser meloso desse jeito."

        n "Precisa, sim. Eu quero fazer tudo direitinho com você."

        mc "Bobo..."



        n "Depois do que a gente fez no encontro passado... o que você acha da gente arriscar aqui também?"

        mc "O q-que você tá pensando?"

        n "Você sabe o que eu tô pensando..."

        n "Eu sei que eu fico gato com essa roupa, mas você não me prefere pelado?"

        mc "É-é..."

        n "Vai... tira aqui..."

        "Por que sempre nos lugares assim? A gente não pode só ir pra de um?"

        "E agora?"

        label n6_premium1:

            pass

        menu:
            "Tirar a roupa dele":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_15

                    jump n6_premium1

                mc "Tá bom... mas só porque eu não resisto a você."

                n "Que sorte a minha, hein?"

                scene black with dissolve

                scene n6_premium1 with Dissolve(1.0)

                pause

                n "E aí? Qual a nota?"

                mc "Todas... você sabe..."

                n "Haha... obrigado, jurado."

                n "Talvez você queira olhar melhor. Pra ter certeza que não deixou passar nenhuma imperfeição."

                mc "Hmm..."

                menu:
                    "'Analisar' de perto":


                        mc "Deixa eu ver... pra coferir se você realmente merece um 10."

                        n "Isso."

                        scene n6_premium2 with Dissolve(1.0)

                        pause

                        mc "Hmm..."

                        n "E aí?"

                        mc "Ainda não sei... talvez só olhar não seja suficiente."

                        n "É... Talvez você tenha razão... faz sentido..."
                    "Agarrar ele":


                        mc "Eu não preciso ver mais nada."

                mc "Vem aqui!"

                scene n6_premium3 with hpunch

                pause

                n "Nngh!"

                mc "Eu quero sentir você de novo!"

                n "Eu tô aqui pra você, gostoso."

                mc "E não importa que a gente tá no meio do seu trabalho, né?"

                n "Foda-se. Eu só quero ficar com você."

                mc "Então vem, delíc-"

                scene n6_premium3 with hpunch

                "{i}TOC TOC{/i}"

                "???" "Nathan! Querem falar com você lá na festa!"

                "???" "Você é o queridinho do pessoal! Tão sentindo sua falta!"

                mc "N-nossa!"

                n "Que droga, [mc]..."

                n "Tá bom! Já tô indo lá!"

                "???" "Vem logo. Perto da passarela."

                n "Ok!"

                n "Desculpa, [mc]... a fama também tem seu preço..."

                mc "Tudo bem... a gente vai ter outra chance."

                n "Pode apostar. A próxima vai ser na minha casa então."

                mc "Lá dá pra gente, né..."

                n "Exatamente. Você aceita?"

                mc "Claro. Eu adoraria."

                n "Legal!"
            "É perigoso demais":


                mc "N-não. É perigoso demais, [n]."

                n "A próxima vai ser na minha casa então."

                mc "Lá dá pra gente, né..."

                n "Exatamente. Você aceita?"

                mc "Claro. Eu adoraria."

                n "Legal!"

                scene black with Dissolve(1.0)

        n "Então um beijo pra comemorar."

        mc "Outro?"

        n "Uhum..."

        pause

    label nathan_e6_depois:

        scene black with Dissolve(1.0)

        "..."

        scene cidade centro10 with Dissolve(2.0)

        "Ufa. Tô me sentindo melhor aqui."

        "Ainda não tô acreditando que tanto a [j] quanto o [n] vieram me falar sobre tudo isso."

        "Parece que realmente essa cidade tá cheia de mentiras em todos os lugares. Por que eu quero tanto viver aqui?"

        "É difícil entender, mas mesmo com tanta coisa desgraçada escondida, a capital tem uma atração que não dá pra resistir."

        if nathan_e6 == "seducao":

            "E agora eu e o [n] realmente tamo namorando. Mesmo com tudo isso, as coisas foram pra esse lado. Foi tudo tão rápido."

            "É duro entender como a gente saiu daquela vibe pra isso, mas não vou reclamar. Faz tempo que eu queria que a gente chegasse nisso."

            "Espero que dê tudo certo a partir de agora com a gente."

        elif nathan_e6 == "roxane":

            "E essa [ro]? Que garota misteriosa."

            "Ela disse que está devendo um favor pra mim... como será que eu posso usar isso?"

            "Talvez eu possa usar com ela mesmo... não seria uma má ideia. Mas é melhor eu pensar direito nisso."

        "O [n] disse que a [j] tá armando uma boa aí. Acho melhor eu ficar esperto com ela na redação."

        "Vou voltar pra casa, mas com tudo isso acontecendo vai ser foda dormir hoje."

    scene black with Dissolve(1.0)



    "Como será que ficou a festa? Tomara que o [n] esteja conseguindo aproveitar um pouco..."

    "E com a Cássia lá... que merda... e se eles se encontrarem?"

    menu:
        "Eu queria saber como tá.":


            "Se eu pudesse ver como tá lá... aaahhh!"

            scene black with dissolve

            scene n6_passarela_geral with Dissolve(1.0)

            pause

            n "Quem tava me procurando?"

            "???" "Aquela mulher alí. Ela trabalha na revista."

            n "D-droga..."

            n "Oi..."

            "???" "Pombinho!"

            scene black with dissolve

            scene n6_new1 with Dissolve(1.0)

            pause

            j "Onde você tava?"

            n "Eu? Tava com o pessoal da festa... parece que muita gente quer falar comigo..."

            j "Claro. Agora você é famoso aqui na capital. Graças a mim, claro."

            n "É... parece que sim... não sem você ter garantido o seu junto."

            j "Mas isso é óbvio. Eu não faço favores, querido. Bom... a não ser que eu ganhe algo em troca."

            n "Eu percebi isso."

            j "E já que você conseguiu esse emprego e essa fama graças a mim... tava pensando numa coisa aqui..."

            n "Nem vem, Cássia. Eu não quero ser grosso com você, mas o que eu tinha que fazer por você eu já fiz."

            j "Que garotinho malcriado. Desobedecendo a mamãe."

            n "Eu... eu tenho conversado com o [mc], sabe? E ele me disse umas coisas que abriram meus olhos."

            j "Hm... imagino o que saiu da cabecinha daquele moleque."

            n "A gente conseguiu que a gente queria. Eu tô empregado e vou seguir meu sonho. E você conseguiu sua matéria."

            n "Acho que nossa parceria foi um sucesso, mas agora eu quero seguir adiante. S-sem você."

            j "Eu tô ouvindo direito? Você quer me descartar?"

            n "N-não é isso. Eu acho que nós dois tivemos sucesso. E é melhor que a gente siga nosso caminho agora."

            j "Pombinho... as coisas não são assim. Você tá apenas começando."

            n "N-não! Nem fala uma coisa dessas."

            scene n6_new2 with Dissolve(1.0)

            pause

            j "Escuta bem. A Blergh!, onde você trabalha com tanto prazer, faz parte desse rolo que você acha que quer sair."

            n "..."

            j "É isso mesmo. Ela é só um dos pilares desse palácio gigante que a gente construiu na capital."

            j "É impossível escapar da sombra que essa construção imensa faz. Ela tá sobre toda a cidade."

            j "Não importa se você vai correr de mim, ela vai te alcançar logo ali adiante."

            n "E-eu..."

            j "O próprio [mc]. Você acha que ele também não tá de olho em um pedaço disso?"

            n "N-não acho. Ele não é igual eu e você. Ele quer viver a vida dele, mas sem entrar nesse buraco."

            n "Eu me sinto tão mal de ter enganado ele por todo esse tempo. Ele não merece isso!"

            n "É por ele também. Não quero mais enganar ele. E não quero mais me enganar. Eu tô fora!"

            j "Muito bem... parece que você tem certeza disso."

            n "C-claro que eu tenho!"

            j "Muito bem. Eu não te procuro mais e você pode conseguir o que você quer. Que é viver livre e feliz."

            n "O-obrigado."

            j "Eu só queria uma última coisinha de você..."

            n "..."

            j "Eu queria ver seu camarim. Você podia me mostrar ele?"

            n "Hm?"

            j "Sabe como é... um último momento só nós dois... uma visita rápida."

            j "Você aceita e tá livre de tudo, querido. É um preço pequeno, não acha?"

            n "Eu sei muito bem o que você quer dizer com 'visita'..."

            j "Melhor ainda. E então?"

            label n6_premium2:

                pass

            menu:
                "Ir com ela pro camarim":


                    if not premium:

                        call mensagem_premium from _call_mensagem_premium_16

                        jump n6_premium2

                    n "Vem... eu te mostro onde é..."

                    j "Excelente, pombinho... é assim que eu gosto..."

                    j "Melhor ainda se você me levar no seu colo, hm? Você é tão forte... aposto que não vai ser problema pra você."

                    n "..."

                    scene black with dissolve

                    scene n6_camarim with Dissolve(1.0)

                    n "É aqui..."

                    j "Maravilhoso. Agora me coloca aqui na mesa."

                    n "Cássia..."

                    j "Vai logo, bebê. É nossa última vez."

                    n "Vem."

                    scene black with dissolve

                    scene n6_premium4 with Dissolve(1.0)

                    pause

                    j "Ai, assim que a mamãe gosta. Me pegar parece tão fácil pra você."

                    n "Você é levinha."

                    j "Seus braços que são fortes, meu bem. Olha só pra isso aqui."

                    j "Eu adoro passar a mão pelo seu corpo musculoso. Você tem o corpo mais delicioso que eu já senti."

                    n "Obrigado. Você também é gostosa."

                    j "Então vem experimentar, querido. Me engole."

                    n "Sim..."

                    scene n6_premium5 with Dissolve(1.0)

                    pause

                    j "Ah... quanta força..."

                    n "Eu sei que você gosta quando eu pego firme."

                    j "Sim... você é o único que me pega com força desse jeito."

                    j "Não sei o que acontece com os outros... eles me respeitam demais."

                    n "Você engole eles, Cássia."

                    j "Mas você... você não tá nem aí pra mim..."

                    n "É diferente..."

                    j "Hmm... eu sei o que é..."

                    j "É o ódio. Você me maltrata no sexo porque quer me punir."

                    n "..."

                    scene n6_premium6 with Dissolve(1.0)

                    pause

                    j "Ahnn! Tá vendo?!"

                    n "Você não merece nada mesmo."

                    j "Eu mereço você... ahmm..."

                    n "Você não me merece, caralho nenhum."

                    j "Isso... me morde... me trata com raiva... hmm..."

                    n "..."

                    j "Aainn... eu sei que você gosta também. Não adianta fingir que não."

                    n "Eu não quero nada com você. Você só me tem na mão."

                    j "Eu tenho você na minha buceta, bebê. É de lá que você não quer sair."

                    j "E aqui também... nos meus peitões. Chupa eles, chupa?"

                    n "N-não... eu não quero isso. Eu só quero me livrar de você."

                    j "Pode falar o que quiser, querido. Agora mama aqui, mama."

                    menu:
                        "Tá bom...":


                            n "Tá... mas só pra você parar."

                            scene n6_premium7 with Dissolve(1.0)

                            pause

                            j "Hmm... quanta vontade."

                            n "N-não é vontade."

                            j "Você gosta do biquinho da mamãe? Você se diverte com ele, né, querido?"

                            n "Hmm!"

                            j "Ai... você me machuca de propósito..."

                            n "Porque eu sei que você quer."

                            j "Continua... aahnn... sendo malcriado..."

                            scene n6_premium8 with Dissolve(1.0)

                            pause

                            n "Essa teta falsa não vale nada."

                            j "Ai, seu cretino... aahn..."

                            n "Eu faço o que eu quiser com esses sacos de plástico. E o pior é que você fica ainda mais molhada."

                            j "Nnngh... você não é de nada. Você não passa de um garotinha idiota."

                            n "Você vai ver, sua vaca!"

                            j "Aain! Te irritei, é?!"

                            j "O que você vai fazer agora, machão?!"

                            scene n6_premium9 with hpunch

                            pause

                            n "Eu destruo esse peito!"

                            j "Isso! Hmm! Eu gosto de ver você assim!"

                            n "Cala a boca!"

                            j "Aainngh!"

                            n "É incrível como você se diverte enquanto eu mordo você desse jeito!"

                            j "Só você faz isso, bebê! Os outros são todos viadinhos. Você é meu homem!"

                            n "Eu não sou seu nada!"

                            j "Agora vem. Eu tô pronta pra você! Me joga na mesa e me fode!"

                            menu:
                                "Foder ela":


                                    n "Eu sei muito bem que você precisa de um caralho grosso pra gozar!"

                                    j "Então me dá meu caralho!"

                                    scene n6_premium10 with vpunch

                                    pause

                                    n "É isso que você quer?!"

                                    j "Isso! Dá pra sua dona! Mete na buceta safada dela!"

                                    n "Você vai prometer que vai parar então!"

                                    j "Se eu preciso pra sentir esse caralho, eu prometo!"

                                    n "Promete que você não vai mais correr atrás do meu caralho!"

                                    j "Eu prometo! Só me come agora!"

                                    n "É sua palavra, hein?!"

                                    j "ENFIA LOGO!"

                                    scene n6_premium11 with hpunch

                                    pause

                                    j "AAAIIINNH!"

                                    n "NNGH!"

                                    j "Isso! Era isso que eu tava esperando!"

                                    n "Não acredito que você tá me fazendo foder essa buceta arrombada!"

                                    j "AAhnn! Não fala assim!"

                                    n "Cala a boca! Todo mundo sabe que você dá ela pra qualquer um!"

                                    j "Nnngh! Qualquer um não! Só pra quem eu- NNHH! - eu quero!"

                                    n "E você é uma puta que quer qualquer um! Dá na mesma, sua puta!"

                                    j "Ainn! Quando ódio! Como você fode forte, caralho! AANNGH!"

                                    n "Você não viu nada, vadia!"

                                    scene n6_premium12 with hpunch

                                    pause

                                    j "ASSIM! FAZ ASSIM! NNNGHH!!"

                                    n "MMMHH!"

                                    j "AAIIH! Você parece um cavalo!"

                                    j "AANNNGH!! Me come igual um animal, NATHANN!!!"

                                    n "..."

                                    j "Que foi?! NNGH! Percebeu que tá gostando?! AANNN!"

                                    n "Você me obrigou a isso!"

                                    j "Obriguei, é?! AHN!!"

                                    n "C-claro!!!"

                                    j "Você sabe que eu- NNGHH!! - não obriguei nada!"

                                    n "Cala a boca, cadela!!! Eu vou acabar com você aqui atrás!"

                                    j "Nem pensa em foder meu cuzinho desse jeit-"

                                    scene n6_premium13 with hpunch

                                    pause

                                    j "AAAIIIIHHH!!!"

                                    n "Hmmmnn! Parece que você ainda não foi tão arrombada aqui!"

                                    j "Aainnh! Caaalma!! NNNGHHH!"

                                    n "Calma o caralhooo!! HMM!"

                                    j "ANNN! CARALHO!!! AANNNGH!!!"

                                    j "Porra de caralho no meu rabo! AANGHH!"

                                    n "Eu sei que quanto mais forte, mais você fica molhada!"

                                    j "Eu amo! NNGHH! Quando você me trata igual sua cachorra!"

                                    j "Continua me comendo, meu bebê!"

                                    n "MMMHNNN!!"

                                    j "Isso!"

                                    scene n6_premium14 with hpunch

                                    pause

                                    j "AAHNN! Olha pra sua cara! Você adora meu rabo! NNGH!"

                                    n "Aahh... ele é bom!"

                                    j "Finalmente a verdade! NNGH!"

                                    n "Goza logo, vadia!"

                                    j "Tá bom, querido! NGHH! Tô vendo que você tá - AAHN! - No limite também!"

                                    n "NHMMM!"

                                    j "Continu assim! AAHNN!"

                                    j "MAIS FORTE! ME ARROMBA! AAAGNNHH!!!"

                                    n "Vou gozar!!!! AAAGNNHH!!"

                                    j "EU TAMBÉM! AAHNN!! ME ENCHE!! AAAHNNNN!!!"

                                    scene n6_premium15 with vpunch

                                    j "AAAAAGHHHHH!!!"

                                    j "Tô gozando muito, filho da puta!!! AAAHNNN!!!"

                                    n "AAAHHH!!!"

                                    j "Caralho! Aahnn..."

                                    n "Aah..."

                                    scene n6_premium16 with Dissolve(1.0)

                                    pause

                                    j "Hmmm... que delícia..."

                                    n "Esse rabinho apertado... eu não queria..."

                                    j "Eu sei que você ama ele..."

                                    n "E-eu não..."

                                    j "Você não consegue tirar o sorriso bobo da cara."

                                    n "Você é terrível... mas agora eu tô livre, né?"

                                    j "Haha... você acha mesmo? Acha que eu vou ficar sem isso aqui?"

                                    j "Você é a melhor transa que eu tenho, pombinho... nunca eu vou deixar você ir."

                                    n "C-cássia..."

                                    j "Xii... não atrapalha meu momento... hmm..."

                                    n "Mas-"

                                    j "Quando eu precisar de você de novo eu te procuro, tá?"

                                    n "!"

                                    j "Você é meu brinquedo..."

                                    scene black with dissolve

                                    pause

                                    n "Tá..."
                                "Terminar ela com a mão":


                                    n "Você não merece meu pau! Você vai gozar com meu dedo!"

                                    j "Não! Ahnn! Não enfia assim com tudo! AANNGH!"

                                    n "Goza logo, vadia!"

                                    j "Não! AAHMM! Eu quero seu pau! AAANNGH!"

                                    n "Vai gozar, sim!"

                                    j "Filho da puta! NNGH! Eu vou gozar mesmo! AAHNN!"

                                    scene n6_premium9 with hpunch

                                    n "Goza, caralho!!!"

                                    j "NÃOOO! AANNGHH!! ASSIIMMM!!! NÃOO PAARA!!!"

                                    j "FILHO DA PUTAAAA!!! TÔ GOZANDOOO!!!"

                                    scene n6_premium9 with hpunch

                                    n "Isso..."

                                    j "Aah... aah...."

                                    j "Só você mesmo pra me fazer gozar assim..."

                                    j "Você sabe que eu nunca vou deixar você fugir de mim, né?"

                                    n "..."
                                "Se recusar e sair":


                                    n "Não. Você tá entendendo tudo errado. Eu só quero que você pare de me encher."

                                    j "Não importa. Só me come!"

                                    n "Não! Eu não quero! Chega! Eu já fiz o que você pediu! Adeus!"

                                    j "Não! Nem pense em parar agora!"

                                    n "ADEUS!"

                                    scene black with vpunch

                                    j "Ei! Volte aqui agora, cretino!"

                                    j "Você vai pagar caro por isso, pombinho... você vai ser meu enquanto eu quiser brincar com você..."
                        "Eu preciso parar!":


                            n "Não. Você tá entendendo tudo errado. Eu só quero que você pare de me encher."

                            j "Não importa. Só continua!"

                            n "Não! Eu não quero! Chega! Eu já fiz o que você pediu! Adeus!"

                            j "Não! Nem pense em parar agora!"

                            n "ADEUS!"

                            scene black with vpunch

                            j "Ei! Volte aqui agora, cretino!"

                            j "Você vai pagar caro por isso, pombinho... você vai ser meu enquanto eu quiser brincar com você..."
                "De jeito nenhum.":


                    n "Não me interessa, Cássia."

                    j "Você não era assim, pombinho. Você sabia me agradar."

                    n "Esse tempo acabou. O [mc] me mostrou que eu tenho escolha."

                    j "Você tá começando a me irritar, [n]."

                    n "Então se irrite. Passar bem."

                    scene black with dissolve

                    j "Volte aqui, garoto mimado! Não se esqueça quem te colocou aí!"

                    j "Garotos mimados, filhos da puta!"
        "Não ligo pra isso.":


            mc "Nah... tenho que focar no que EU vou fazer agora."



    label nathan_e6_final:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v35_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v35_fim","final","local")

    scene black with Dissolve(3.0)

    show tela continua with Dissolve(2.0)

    pause

    call checa_final from _call_checa_final_1

    jump call_cidade

label nathan_evento7:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n7_save", extra_info="n7_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ nathan_e7 = "evento"
    $ roxane_livre = False

    pause

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trr... trrr..."

    mc desconfiado "Hm?"

    mc surpreso "É o [n]!"

    "[n]... naquela outra noite ele disse um monte de coisa pra mim. Toda a verdade por trás de tudo o que aconteceu."

    "Desde o nosso encontro marcado pela [j] até a questão dele ser expulso do país. Tudo foi planejado desde o começo..."

    if nathan_e6 != "seducao":

        "Eu não sei como lidar com ele agora. Até que ponto eu posso confiar no [n] depois de saber tudo isso?"

        "Será que eu atendo ele? {w}Bom... é melhor eu falar com ele pelo menos."
    else:


        "Mesmo sabendo disso eu resolvi confiar nele e ficar com ele. Agora a gente tá namorando..."

        "Eu não quero saber do passado. Eu quero ficar com o [n] mesmo e foda-se."

        "Deixa eu atender ele logo."

    mc normal "Alô? [n]?"

    n "O-oi, [mc]..."

    if nathan_namoro:

        mc charmoso "Que bom que você ligou. Tava com saudades."

        n "Você? Eu também tava..."

        n "Ainda não acredito que a gente tá namorando sério... de verdade."

        mc "Claro que é de verdade."

        n "Ainda mais depois do que eu te falei aquele dia... você não é desse mundo, [mc]."

        mc "..."

    n "Eu sei que ficou um climão depois daquela conversa que a gente teve... e eu queria explicar tudo pra você."

    mc desculpa "[n]... não sei se tem necessidade da gente falar disso..."

    n "Eu preciso, [mc]. Mesmo que pra você isso não vá mudar nada, eu preciso te falar."

    if nathan_namoro:

        n "Eu não vou conseguir entrar de cabeça na nossa relação se eu não falar sobre isso."

        mc "Você sabe que eu aceitei ficar com você..."

        n "Mesmo assim..."

    mc "Se você acha que realmente precisa falar sobre isso..."

    n "Por favor. É muito importante pra mim."

    menu:
        "Tudo bem. Eu também quero falar com você.":


            mc normal "Ok. Eu também tava querendo passar um tempo com você depois de tudo aquilo."

            n "Que bom. Não quero deixar as coisas estranhas e a gente pode fazer alguma coisa juntos depois também."

            mc "Opa. Ia ser uma boa. Curtir também faz parte."

            n "Com certeza."
        "Se você precisa...":


            mc "Bom... se você realmente quer... eu tô aqui pra você."

            n "Muito obrigado, [mc]. Você é o cara."

            mc "Relaxa."

    mc "E como você quer fazer?"

    n "E se a gente fosse pro meu apê? É um lugar mais tranquilo pra gente conversar."

    if nathan_namoro:

        mc surpreso "Opa! Opa! Tá me chamando assim? Não vai nem pagar o jantar antes?"

        n "A gente tá no século vinte, [mc]. As coisas são assim agora."

        mc safado "Credo... que delícia..."
    else:


        mc "Tudo bem. Se é uma conversa séria, então acho que é melhor mesmo."

        n "Beleza."

    n "Eu tô fazendo um treino aqui na Blergh! pra um novo desfile que vai ter. Seria muito ruim você vir pra cá?"

    n "Assim que acabar a gente já vai pro meu prédio. Não fica muito longe. Dá uns 15 minutos a pé."

    mc desconfiado "A Blergh! é onde teve a festa, né?"

    n "Isso. Você já conhece aqui."

    mc normal "Então beleza. Eu tô indo aí e a gente já troca uma ideia."

    n "Ah. Ainda vai demorar um tempinho pra eu sair, então se quiser esperar uma ou duas horinhas antes de vir."

    mc zerado "Falar a verdade, eu não tenho nada pra fazer, sabe? Daí acho que vou esperar aí mesmo."

    n "Haha... beleza. Se é assim, sim."

    mc normal "A gente se vê então."

    if nathan_namoro:

        n "Beijo."

        mc charmoso "Beijo."
    else:


        n "Demorou. Até depois."

        mc "Até."

    "Quem sabe eu não encontro algum famoso interessante lá na Blergh? Uma pauta agora vai ajudar bastante com o chefe."

    call locomocao from _call_locomocao_7

    scene cidade centro10 with Dissolve(2.0)

    pause

    "Vai ser uma boa tirar essa história à limpo com o [n]."

    "É fácil julgar as pessoas de mentirosas e talz, mas com certeza ele teve as razões dele. O mínimo que eu posso fazer é ouvir."

    if nathan_namoro:

        "Ainda mais agora que a gente tá juntos, eu preciso ser um bom companheiro."

    "Mas... se ele mentiu pra mim uma vez, quem garante que ele não vai mentir de novo?"

    "O [n] é um cara bacana e ele queria ter uma carreira na moda. É o sonho dele."

    "Só que... como acreditar completamente em uma pessoa depois disso? Todo aquele show com a [j]... foi tudo armação deles."

    "E tudo pensando no bem da Blergh, uma empresa..."

    "O [n] pelo menos ia ganhar um emprego na área que ele queria... mas por que a [j] teria interesse em ajudar também?"

    "Será que tem mais coisa envolvida nisso aí? Será que é isso que ele quer conversar comigo hoje?"

    "Bom... cheguei."

    scene black with dissolve

    "Recepcionista" "Boa tarde. O que o senhor gostaria?"

    mc normal "Oi. Eu vim esperar o [n]. Ele tá terminando de ensaiar um novo desfile e ele pediu pra eu esperar."

    "Recepcionista" "Ah. Fique à vontade. Pode entrar por esta porta. É onde fica o salão."

    mc "Valeu."

    "Era a mesma garota da outra vez. Pelo que eu me lembro... o caminho era por aqui..."

    "???" "Eu não tô vendo aquele olhar!"

    mc desconfiado "Hm?"

    scene n7_img1 with Dissolve(1.0)

    pause

    "Opa. Tem umas pessoas aqui. Devem tá ensaiando também. Melhor eu ficar de bico calado."

    "Modelo" "Como assim? E-eu tô normal."

    "Mulher" "Normal? Você acha que 'normal' é suficiente? Você acha que é isso que vai vender nossos produtos?"

    "Modelo" "D-desculpa. Não sei, senhora..."

    "Mulher" "Desfilar tem a ver com energia. Eu falo isso pra você desde o começo, garota. Você não entende?"

    "Mulher" "Seu olhar, seu corpo, a forma como você anda. Presença é a palavra. Sua presença precisa transmitir sua verdade."

    "Modelo" "Transmitir minha verdade? Não sei se eu entendi..."

    "Mulher" "Claro que você não entendeu... não sei por que eu ainda tento..."

    "Mulher" "Você tem estilo, garota. Você tem personalidade. Foi isso que me conquistou. Mas ainda falta muito."

    "Nossa... essa mulher parece bem séria sobre isso... será que ela é alguma professora? Treinadora talvez..."

    "Mas parece ser um negócio bem interessante mesmo isso que elas tão fazendo."

    "Nunca imaginei que andar na passarela tivesse a ver com 'olhar' e 'presença'."

    "Fiquei com vontade de ver mais de perto... mas será que elas vão brigar comigo? Tô com medo de atrapalhar."

    "E agora?"

    menu:
        "Chegar perto da passarela":


            "Se eu ficar quieto acho que não tem problema, né? Vou dar uma olhada..."

            scene n7_img2 with Dissolve(1.0)

            pause
        "Melhor eu continuar aqui":


            "Melhor eu não causar com elas. Dá pra eu ver daqui."

    "Mulher" "Você tem confiança, [ro]. Eu vejo que você leva jeito pra isso. Mas você precisa colocar essa cabeça pra funcionar."

    "Mulher" "Estilo é importante. Personalidade é imprescindível quando a gente é a face de alguma coisa. E isso você tem."

    ro "O-obrigada, senhora. Desculpa qualquer coisa."

    "Mulher" "Não é questão de pedir desculpas, garota. É questão de entender o que eu quero dizer."

    "Mulher" "As mulheres querem sentir que estão vestindo roupas que dão poder. Que vão transformar elas em algo maior do que elas são."

    "Mulher" "As roupas da Blergh! vão empoderar as mulheres e trazer para elas a confiança necessária pra conquistar o que elas quiserem."

    ro "E-entendi."

    "Mulher" "Você pode falar que entendeu, mas não entendeu porcaria nenhuma! Pensa no que eu estou falando antes de responder!"

    ro "S-sim, senhora!"

    "Então essa mulher é da Blergh!. Ela deve ser consultora ou algo assim. Ela parece saber bastante sobre roupas."

    "Eu nunca parei pra pensar que roupa podia dar poder pra alguém... eu achei que o objetivo era deixar a gente bonito, sei lá."

    "E essa é a [ro]... [ro]... esse nome não me é estranho..."

    mc surpreso "Ah!"

    "Aquela garota que o [n] me apresentou. Ela era uma modelo igual ele."

    if nathan_e6 == "roxane":

        "Pior que eu vi ela de lingerie aquela noite... eu fui com ela até o camarim."

        "Ela agradeceu por alguma coisa e até disse que tava devendo um favor pra mim."

    "Nossa... mas ela tá tão diferente... O cabelo dela era comprido e loiro."

    "E por que caralhos ela tá com uma chupeta na boca?"

    ro "Eu prometo que vou me esforçar bastante."

    "Mulher" "Então vai. Respira fundo e entra de novo. Não se esqueça da palavra mágica."

    ro "Presença..."

    "Mulher" "Exatamente."

    "Será que vale à pena chegar mais perto pra ouvir o que ela tá falando?"

    "Queria dar uma olhada nessa mulher. Quem será que ela é..."

    menu:
        "Se aproximar da mulher":


            "Ela tá focada na [ro]. Ela nem vai perceber que eu tô aqui."

            scene n7_img3 with Dissolve(1.0)

            pause

            "Daqui eu consigo ouvir melhor."
        "Manter uma certa distância":


            scene n7_img2 with Dissolve(1.0)

            "Não vou chegar tão perto. Daqui tá bom."

    "Mulher" "Eu não tenho muito tempo. Então acho bom você acertar essa próxima."

    "Mulher" "Você precisa dominar o percurso e o básico. Quando você estiver desfilando na passarela, sua cabeça precisa estar focada."

    "Mulher" "Não dá pra ficar pensando se vai escorregar, com as câmeras, holofotes e outras coisas banais."

    "Mulher" "Quando uma mulher desfila, ela deve pensar na força que ela transmite para todas as outras que a estão vendo."

    "Mulher" "Você não está 'andando', você está empoderando milhares de mulheres que precisam sentir essa energia dentro delas."

    "Mulher" "Se você não passar essa confiança na sua face, no seu corpo e principalmente no seu olhar, então não adianta nada."

    "Mulher" "A Blergh! é mais que uma marca. É um estilo de vida. Quem usa nossas peças quer fazer parte do que nós representamos."

    "Mulher" "E você, garota, é nossa vitrine. Se você não demonstrar nossa verdade, ninguém vai ver. A empresa segue seus passos."

    "Caralho... a mulher fez mó discurso aqui. Acho que até eu fiquei com vontade de desfilar depois dessa."

    "Será que ela é coach? Eu já ouvi falar de pessoas que treinam os outros pra chegarem ao sucesso. Talvez a [ro] esteja treinando isso..."

    "Mulher" "Não! Ainda não é isso!"

    ro "D-desculpa..."

    "Mulher" "Não tenho mais tempo. Preciso resolver algo com o [n] antes dele sair."

    "Mulher" "Hoje você fica aqui pensando em tudo o que eu falei. Não adianta o exterior se você ainda não consegue entender a essência."

    ro "Ok..."

    scene n7_passarela with Dissolve(1.0)

    "Mulher" "Amanhã tentamos novamente."

    ro "Até amanhã, senhora..."

    ro "Ai... preciso sentar..."

    "O-opa! Ela tá vindo pra cá!"

    ro "Oi. Posso sentar aqui?"

    mc envergonhado "C-claro."

    scene n7_img4 with Dissolve(1.0)

    pause

    ro "Ei. Você é o amigo do [n], né?"

    mc normal "Isso."

    if nathan_e6 == "roxane":

        ro "A gente até desenvolveu um pouco aquela noite, né?"

        mc charmoso "Bom... ir com você no camarim e conversar com você só de lingerie foi um excelente desenvolvimento."

        ro "Haha... bobo."
    else:


        ro "Aquela noite a gente nem conseguiu conversar direito."

        mc "Verdade. Aquela noite tava uma loucura."

        ro "Sei..."

    ro "Mas não pensei que ia ver você aqui assim. A festa até entendo, mas por que hoje?"

    menu:
        "Eu vim esperar o [n].":


            mc "Eu vim esperar o [n]. Depois do trabalho a gente vai trocar uma ideia."

            ro "Nossa! Verdade! Nem pensei nessa possibilidade, que burra."

            ro "É que eu nunca tinha visto você aqui."

            mc "Verdade. É a primeira vez que eu venho. Normalmente a gente se encontra em outros lugares."

            ro "Pra ele te chamar pro trabalho dele, é porque a coisa tá ficando séria então."

            if nathan_namoro:

                mc charmoso "Você acha?"

                ro "É um bom sinal."
            else:


                mc envergonhado "V-você tá pensando demais. Não é nada disso."

                ro "Ah. Então tá. Mas vocês fariam um bom par."

                mc "Haha..."
        "Eu sou um paparazzo. Tem alguma pauta aí?":


            mc charmoso "Eu sou um paparazzo. Onde tem gente famosa eu me enfio. Inclusive, você não tem uma informação quente pra mim, não?"

            ro "Haha... aqui você não vai encontrar muita coisa, não. A Blergh! tá só começando."

            mc "Mas fiquei sabendo que vocês tão crescendo rápido."

            ro "Isso é verdade. Eu tô participando de bem mais eventos agora. Você realmente tem razão."

            mc "Então logo você já vai poder me ajudar."

            ro "Seria um prazer."

    ro "Aliás, você deve saber, claro, mas sua revista e a Blergh não se dão tão bem assim."

    mc desconfiado "Sério? Sabia disso, não."

    ro "Verdade. Tem uma marca de roupas que anuncia na sua revista. Ela é nossa maior rival."

    ro "'Nossa' que eu digo é da Blergh. Eu não tenho nada contra eles pessoalmente. Mas eu trabalho aqui, né? Haha..."

    mc normal "Então é isso..."

    ro "Tem uma jornalista na sua revista que queria até publicar coisa sobre a Blergh!, mas acho que ela não conseguiu."

    mc desconfiado "Hmmm..."

    ro "Mas, olha, eu não quero jogar nossa conversa falando de trabalho."

    mc envergonhado "Sério? E o que você quer falar?"

    scene n7_img5 with Dissolve(1.0)

    pause

    ro "Deixa eu pensar... Ah! O que você achou de mim?"

    mc "Q-que pergunta é essa?"

    ro "Sem a peruca e, sei lá, mais normal."

    menu:
        "Você é linda das duas formas.":


            mc charmoso "Eu achei você linda aquele dia na festa e hoje também."

            ro "V-você não tem nem vergonha de falar um negócio desses assim? Eu fico até um pouco sem jeito de ouvir..."

            mc "Você quem perguntou... e agora fica com vergonha?"

            ro "Não achei que você ia falar um negócio assim... achei que nem ia ter coragem de responder."

            mc "Eu sou um garoto crescido. Eu não tenho medo de nada."

            ro "Haha... tá legal."
        "Sinceramente, você é... exótica.":


            mc envergonhado "Espero que isso não pareça uma coisa negativa falando assim, mas eu achei você bem... exótica..."

            ro "Exótica?! Essa é a melhor palavra que você achou pra me descrever?!"

            mc surpreso "D-desculpa! Não falei no sentido ruim! Por favor!"

            ro "Eu tô brincando com você. Acho que 'exótica' é uma boa forma de me descrever."

            mc preocupado "Você tá falando sério? E-eu queria ser sincero, fiquei com medo de parecer um cuzão."

            ro "Você foi bem corajoso, isso sim. Eu sei que meu estilo não é pra todo mundo. Desenhar no cabelo não é pra qualquer mulher."

            mc charmoso "O que eu tenho certeza é que você passa muita personalidade. Você parece uma mulher e tanto."

            ro "Uou... isso foi inspirador."

            mc envergonhado "Exagerei, né? Às vezes eu me empolgo..."

            ro "Relaxa."
        "Eu não tenho como responder isso.":


            mc envergonhado "Tá doida? A gente não se conhece o suficiente pra eu responder uma pergunta dessas assim."

            ro "Haha... eu sei. Tô brincando com você só. Não é pra responder mesmo."

            mc "Ufa... eu fiquei meio nervoso aqui."

            ro "Era a intenção mesmo rsrs... mas eu fiquei um pouquinho envergonhada agora também."

            mc normal "O tiro saiu pela culatra?"

    ro "Eu tô tentando ser divertida, mas a verdade é que eu não sou tão boa assim pra conversar."

    mc "Na festa você pareceu bem descolada."

    ro "Eu tava alta aquela noite. Depois que eu desfilei eu entortei o caneco. Daí eu fico um pouco mais corajosa."

    mc envergonhado "Haha! Tá explicado..."

    ro "Normalmente a chefe pede pra gente interagir com o pessoal, daí normalmente eu dou aquela virada pra aguentar."

    mc "Não é fácil ser a garota propaganda da empresa, né?"

    ro "É bem cansativo. Você viu durante meu treino, né? A chefe é bem séria no trabalho dela."

    mc "Então ela é sua chefe... eu tava tentando advinhar quem ela era. Parecia saber bastante de desfile e tudo."

    scene n7_img8 with Dissolve(1.0)

    ro "Com certeza. Ela é a dona da Blergh!."

    mc surpreso "S-sério?! Ela é a dona?!"

    ro "Sim. A própria. O nome dela é [ve]."

    mc "E ela te treina assim pessoalmente?"

    ro "Sim. A senhora gosta de acompanhar tudo diretamente aqui na empresa."

    ro "Cada coleção de roupas tem seu tema, seu desfile, seus eventos exclusivos. Ela monta tudo isso e acompanha."

    mc normal "Que trabalheira."

    ro "Mas é super divertido."

    ro "Se bem que eu não tô indo tão bem quanto eu gostaria..."

    menu:
        "Eu escutei os comentários dela...":


            mc "Eu tava ouvindo os comentários dela... alguma coisa sobre olhar e personalidade."

            ro "A palavra é 'presença'..."

            mc "Haha... é verdade..."

            ro "O problema é que eu não entendi o que ela quer dizer. Eu... tô fazendo o que eu posso... só que... sei lá..."

            mc "Eu não manjo nada dessas coisas, desculpa."

            ro "Tranquilo. Não ia pedir dicas de passarela pra um jornalista."
        "Pra mim você foi perfeita nesse treino.":


            mc "Eu não sou um grande cara da moda, mas pelo que eu vi você desfilou super bem. Foi perfeita."

            ro "Obrigada... quem dera você fosse meu chefe e não ela..."

            mc "Haha... será que a Blergh ainda existiria se eu fosse o dono?"

            ro "Mas pelo menos você não ia viver falando mal da minha 'presença'..."

            mc "Isso taria garantido."

    mc "Mas, mesmo assim, talvez eu possa te ajudar com alguma coisa, não sei..."

    scene n7_img6 with Dissolve(1.0)

    pause

    ro "Hmmm... o que será que ela quer dizer com aquilo? Toda essa questão de 'presença'?"

    ro "Eu decidi ser modelo porque eu pensei que levava jeito pra isso, sabe? Eu tenho meu estilo e minha personalidade."

    mc "Ela falou bem disso. Que você tem personalidade."

    ro "Então... o que será que eu tô fazendo de errado?"

    mc "É duro saber..."

    ro "Olha eu falando de trabalho de novo..."

    mc "Tá de boa. Se é sobre isso que você quer falar, eu não me importo."

    ro "Mas não era sobre isso...{w} Sendo sincera, eu queria era sondar você e ver que tipo de cara você é."

    mc "Quer me entrevistar? É isso?"

    ro "Falando assim, eu pareço uma maluca, né? Mas seria mais rápido mesmo..."

    mc "Até o [n] sair, por mim a gente pode conversar de boa sobre o que você quiser. E se cada um fizer uma pergunta?"

    ro "Se você não acha loucura, eu topo. Mas eu começo."

    mc "As damas primeiro."

    ro "Tá bom... É... Você tá sério com alguém?"

    mc "É u-uma pergunta bem direta... você é uma entrevistadora que não amacia o alvo."

    call namorando from _call_namorando

    if namorando:

        "Será que é uma boa eu falar pra ela que eu já tô de rolo?"

        "Vai parecer que tô deixando claro que eu não quero nada com ela. Não sei se eu queria fechar todas as portas já..."

        "Mas mentir também assim na caruda... e agora?"
    else:


        "Eu não tô namorando ninguém mesmo. Não tenho porque mentir."

    menu:

        "Eu e o [n] tamo juntos." if nathan_namoro:

            mc "Eu tô sério com o [n] agora. Inclusive, a gente oficializou naquela festa aqui."

            ro "Sério?! Fico muito feliz por vocês!"

            ro "O [n] é um cara incrível. Além de super gato, ainda é sensível e sabe conversar."

            mc "Tirei a sorte grande, né?"

            ro "Com certeza. Mas o [n] é um homem que olha coração e não cara. Se ele curtiu você, é porque você é especial também."

            ro "Por que todos os caras foda são gays?"

            mc "Haha..."

        "Sim. Já tenho namorada." if namorando:

            mc "Eu tô de rolo com uma garota já. É um lance sério. Assim, de minha parte é sério, né? Espero que ela me leve a sério mesmo."

            ro "Com certeza. Você parece um cara direito, não tem por que uma garota fazer isso com você."

            mc "Verdade. A gente tem que confiar na pessoa que a gente gosta também, né?"

            ro "Isso aí. Se cada um fizer sua parte, não tem por que acontecer um lance negativo, sabe?"

            mc "Verdade. Valeu."

            ro "Que isso. Espero encontrar meu príncipe encantado um dia também."

            mc "Vai achar. Tenho certeza."
        "Não. Nada sério por enquanto.":


            $ roxane_livre = True

            mc "Nada sério. Só uma curtida aqui e ali."

            ro "Então você é esse tipo de homem. Galinha assumido."

            mc "Galinha, não... só não encontrei a pessoa certa ainda."

            ro "É... acho que eu entendo você. Eu também ainda não encontrei."

            ro "A diferença é que eu não fico saindo com todo mundo enquanto isso."

            mc "As pessoas são diferentes... mas eu tô brincando. Pra falar a verdade, eu nunca tive muito sucesso com as mulheres."

            ro "Não sei por que. Você até que é bonitinho..."

            mc "Bonitinho não é o tal do feio arrumadinho?"

            ro "N-não foi nesse sentido que eu falei. Desculpa..."

            mc "Tudo bem. Eu sei que eu não sou tudo isso."

            ro "Olha... eu sempre tive que ouvir besteira por causa da minha aparência."

            ro "Só porque eu gosto do meu cabelo assim, e ando de chupeta e tenho piercing, já tive que ouvir muita merda das pessoas."

            ro "Você é um cara normal. Não é um modelo de cinema, mas pelo menos nunca vai ouvir bosta por causa do seu jeito."

            mc "Mandando a verdade, as pessoas gostam de julgar os outros pela aparência."

            mc "Ainda mais hoje que os outros não têm paciência pra ouvir. Ninguém quer saber como a gente é por dentro."

            mc "Tem gente que quer brigar com o outro por causa da cor da camiseta hoje em dia. Nem sabe quem é a pessoa."

            ro "Você parece bem cabeça, isso sim..."

    ro "Aliás... eu não lembro seu nome agora... por favor desculpa!"

    mc "É [mcc]."

    ro "Isso. [mc]. E eu sou a [ro], tá?"

    mc "Eu lembrava."

    ro "Sabe, [mc]... não é que eu queira ficar te julgando sem conhecer... mas... tem uma coisa diferente sobre você."

    scene n7_img7 with Dissolve(1.0)

    pause

    mc "C-como assim?!"

    ro "Não sei... você só é meio misterioso..."

    mc "O q-que isso quer dizer?"

    ro "Não dá pra explicar... e eu sei que você vai me achar louca de falar disso assim... mas é que... seus olhos..."

    ro "Seus olhos parecem que tem uma energia diferente. Quando eu fixo neles... é como se eu ouvisse uma voz me chamando..."

    mc "Hm?"

    ro "Eu sinto um aperto no peito... igual quando a gente lembra de alguma coisa de quando a gente era criança..."

    mc "T-tudo isso só de olhar pra mim? Você tá bem, [ro]?"

    ro "É estranho... mas... é incrível também..."

    ro "Será que é isso que a [ve] tava querendo dizer? Conseguir causar isso em alguém só com os olhos?"

    mc "Você tava certa quando disse que ia parecer loucura."

    ro "..."

    mc "[ro]?"

    ro "Hmmm..."

    ve "Garota! Terminei com o [n]! Ele quer falar com você antes de sair!"

    ro "Ah!{w} D-desculpa, [mc]!"

    mc "T-tudo bem!"

    scene black with dissolve

    ro "Pera aí... deixa eu pegar minha chupeta."

    scene n7_img9 with Dissolve(1.0)

    pause

    ro "Desculpa p-por esse final meio estranho. Acho que você me ajudou a perceber uma coisa muito importante."

    mc envergonhado "Tudo bem... mas não sei o que eu fiz..."

    ro "Eu vou lá ver o que o [n] quer, mas eu prometo que vai ser rápido. Não vou segurar ele muito."

    mc normal "Valeu..."

    ro "Você acha que... tudo bem se a gente saísse um dia?"

    mc desconfiado "Sair? Só nós?"

    ro "É. Eu queria... continuar nossa entrevista."

    "Hmmm... a [ro] parece uma garota super bacana. Além de que ela vai ficar cada vez mais famosa com o crescimento da Blergh."

    "Não tenho por que não sair com ela."

    menu:
        "Eu topo. Vai ser legal.":


            mc normal "Eu topo. Você é boa de papo, mesmo falando que não é, [ro]. Vai ser divertido conversar contigo."

            ro "O-obrigada. E não precisa exagerar. Eu só... falei o que veio na minha cabeça."

            ro "Ah! E não precisa se preocupar que é só um encontro entre amigos."

            mc envergonhado "Não esquente. Eu sei. Não tava pensando em nada disso."

            ro "Então tá! Melhor deixar essas coisas claras bem cedo."

            mc normal "Verdade."
        "Só se for tipo um encontro.":


            mc charmoso "Tudo certo. Mas! Com uma condição. Eu quero que seja tipo um encontro entre nós dois."

            ro "Um encontro... tipo de pessoas querendo se conhecer p-pra... ai..."

            if roxane_livre:

                ro "Acho que... por mim pode ser... mas n-não tenho muita prática nesse tipo de coisa."

                mc charmoso "Não precisa de prática. É só você ser você. Igual hoje."

                ro "Então combinado. Isso é algo que eu consigo fazer. Eu aceito."
            else:


                ro "Mas você não disse que já tá comprometido?"

                mc "É. Mas... nunca se sabe se a gente pode encontrar o novo amor."

                ro "Olha, [mc]... acho que essa não é uma boa ideia. Não seria legal pra outra pessoa, né?"

                mc desculpa "Tem razão... desculpa..."

                ro "Mas a gente pode sair como amigos. Sem nenhuma segunda intenção. Você me ajudaria bastante a entender uma coisa."

                mc normal "Ok. Se vai te ajudar, eu não posso só falar não."

    mc "Então fica certo assim."

    ro "Valeu, [mc]. Você é o cara. Agora vou lá. Beijo!"

    mc "Beijo."

    scene n7_passarela with Dissolve(1.0)

    "A [ro] parecia uma pessoa bem diferente na festa. Ela é uma modelo... mas é tão acessível."

    "Quem dera todas as pessoas famosas fossem assim... humildes e bacanas."

    "O chefe podia beber um pouco dessa água aí."

    "Ainda não acredito que consegui esse emprego. Ter a chance de conhecer tantas pessoas interessantes assim."

    "Se eu ainda vivesse na minha cidade, eu n-"

    "???" "Ei! Quem é você?!"

    mc surpreso "E-eu?!"

    "Eita! A c-chefe da [ro]!"

    scene n7_img10 with Dissolve(1.0)

    pause

    ve "Quem é você? E o que você tá fazendo aqui? Você não é o rapaz do ar condicionado, né?"

    "Eita... a dona da Blergh. A [ro] disse que o nome dela era [ve]."

    menu:
        "Não. Eu tô esperando [n].":


            mc envergonhado "Não não. Eu sou um amigo do [n]. Só vim esperar ele sair mesmo."

            ve "Hmm... e a garota da recepção falou que você podia vir aqui?"

            mc "Eu falei que ia esperar ele, daí ela disse pra eu vir pra cá."

            ve "Depois eu vou ter uma conversa com ela."
        "Sou... mas esqueci o uniforme.":


            mc normal "Sou. Mas vim fazer uma visita rápida, por isso nem coloquei o uniforme. Desculpa."

            ve "..."

            mc envergonhado "É brincadeira. Eu sou um parça do [n]. Ele pediu pra eu vir."

            ve "Depois eu vou conversar com ele."

            "Ixi... acho que ela não curtiu a brincaidera..."

    ve "Aliás. Acho que eu vi você na festa que nós demos. Você é próximo do [n] mesmo?"

    mc normal "Sim. Meu nome é [mc] e eu trabalho como paparazzo na revista da ilha."

    ve "Sério? Naquela revistinha de quinta? E eu não quero saber de você tirando foto ou assediando meu pessoal, entendido?"

    mc envergonhado "Claro... eu não vim a trabalho. E eu não gosto de exagerar na abordagem também."

    ve "'Exagerar na abordagem'? Você tá ouvindo o que você tá falando, garoto? Seu trabalho não é conseguir furos sobre famosos?"

    mc normal "Sim. Essencialmente é isso."

    ve "Se você ficar dando voltas não vai conseguir nada. Eu, hein. Com essa mentalidade você não vai chegar longe."

    menu:
        "Eu só tô tentando ser educado...":


            mc zerado "E-eu tô tentando ser educado. Falando que não vou causar nada aqui na sua empresa."

            ve "Eu agradeço, mas você precisa repensar suas prioridades."

            mc desconfiado "Como assim?"

            ve "Você quer ser agradável às pessoas ou quer conquistar algo grande na sua vida?"

            mc zerado "E não pode ser os dois?"

            ve "Muito difícil. Conquistar coisas na vida exige focar no que se quer e não se preocupar com o que os outros pensam."
        "Eu conheço uma jornalista que ia gostar de você.":


            mc zerado "Olha... eu tenho uma conhecida jornalista que com certeza ia gostar de você."

            ve "Ela parece alguém interessante. Provavelmente ela deveria cobrir nossa marca, não você."

            mc "Ei... você não precisa falar assim."

            ve "Eu só estou seguindo o meu próprio conselho, senhor paparazzo."

            mc "Pior é que é verdade..."

            ve "E não é?"

    mc charmoso "Olha... a [ro] falou que você é a dona da empresa. Acho que pessoas que constroem coisas grandes precisam ser obstinadas."

    scene n7_img11 with Dissolve(1.0)

    ve "Pelo menos isso você entende."

    ve "Mas isso não é só pra quem lidera grandes iniciativas. Esse é o problema de pessoas como você."

    mc serio "..."

    ve "Se tem uma coisa que eu odeio, paparazzo, é lidar com pessoas sem personalidade e que não têm objetivos."

    ve "Comigo meio termo não existe. Eu quero estar do lado de pessoas ambiciosas, que pensam grande e são corajosas."

    ve "Coragem de fazer o que é preciso pra atingir o sonho deles. Pessoas que têm presença e não aceitam mediocridade."

    ve "E por que raios eu tô falando tudo isso pra você?!"

    mc envergonhado "Eu não me importo de ouvir... mas eu não sei também."

    ve "Deve ser esse seu jeito... essa coisa de não feder, nem cheirar."

    mc "Hah..."

    ve "Interessante..."

    mc desconfiado "Hm?"

    scene n7_img12 with Dissolve(1.0)

    pause

    ve "Eu aposto que você leva jeito com as mulheres, não leva?"

    mc envergonhado "Eu?"

    ve "É. Esse seu jeito de bom ouvinte... meio sem sal... sem açúcar. Você deixa elas falarem pelos cotovelos eu aposto."

    ve "Dá essa impressão que se importa com elas. Que elas podem confiar e contar tudo pra você. Que você não vai julgar."

    ve "Hah! Então esse é seu lance, paparazzo?! É assim que você descobre tudo o que você precisa?!"

    menu:
        "Não posso reclamar. Tá chovendo na horta.":


            mc safado "Agora que você falou, realmente tá chovendo na horta, sabe?"

            ve "Hahaha! Mas é óbvio! Esse jeitinho de bobo, essa carinha de pessoa que aceita tudo, humilde..."

            ve "Você não é o tipo que pega todas na festa, mas dois dias sozinha com você e qualquer garota cai aos seus pés!"

            ve "Essa foi muito boa. E quase que você me pegou também. Eu tava começando a falar de mim... incrível."

            ve "Estou impressionada, de verdade."

            mc charmoso "Se você quiser ver essa tática ao vivo, a gente pode sair um dia."

            ve "Tentador... quem sabe..."
        "Eu não uso isso pra conseguir as coisas. É sincero.":


            mc serio "Talvez você seja assim... mas eu escuto as pessoas de forma sincera. Eu não tenho interesses por trás."

            ve "Como se você fosse admitir. Mas pelo menos eu consegui fechar sua cara, né?"

            mc "{i}Hmf{/i}"

            ve "Veja, paparazzo. Você não precisa ser eternamente bonzinho e esconder seus sentimentos pras pessoas gostarem de você."

            ve "Seja honesto com você e com as pessoas ao seu redor."

            ve "Algumas vão te amar, outras não vão te suportar. Mas é impossível agradar todos. A vida é assim."

            mc "Eu não sei se gostei de você..."

            ve "Já é um começo. Lembre-se desse sentimento!"

    ve "Sem dúvidas foi mais interessante do que eu imaginava falar com você."

    ve "Não é à toa que as jóias mais raras se escondem no interior de uma camada de sujeira."

    ve "Quem dera eu conseguisse fazer a garota entender isso. Esse poder que existe no seu olhar..."

    ve "Essa energia que nos convida a abrir o bico e revelar nossos segredos mais obscuros, como uma voz que nos chama."

    ve "Sem dúvida você tá na profissão certa. Só tome cuidado para que os problemas dos outros não se tornem um peso pra você."

    ve "O [n] deve chegar logo. Aproveitem bem o encontro. Aquele garotão vale ouro."

    mc normal "A-até mais."

    ve "Provavelmente não nos veremos novamente. Por isso, prefiro um adeus."

    scene black with dissolve

    scene n7_passarela with Dissolve(1.0)

    "Caraca... que conversa foi essa?"

    "Essa [ve] com certeza é uma mulher única. Esse jeito dela... até sincera demais na minha opinião. Tenho dó do [n] e da [ro]."

    "Mas ela não é a primeira a falar sobre essa questão do 'peso' de saber dos problemas das pessoas. Quem é que já me falou disso mesmo?"

    "E será que eu realmente tenho um 'poder no olhar'?"

    mc zerado "Ou será que eu só tenho uma cara de palerma mesmo?"

    "Realmente essa Blergh tá cheia de pessoas diferentonas. Parece até que eu tô em outro país."

    n "[mc]!"

    mc normal "Ei, [n]!"

    n "Acabou aqui. Vamo pra casa?"

    mc "Opa. É o combinado."

    n "Lá a gente conversa melhor."

    if nathan_namoro:

        n "Seu gostoso..."

        mc envergonhado "O-opa!"

    scene black with dissolve

    "..."

    scene cidade centro2 with Dissolve(1.0)

    n "Desculpa ter feito você esperar tanto. A chefe quis trocar uma ideia comigo e ainda pediu pra eu falar com outra modelo."

    mc normal "De boa. Eu consegui conversar com a [ve] e a [ro] um pouco."

    n "Sério? E o que você achou da chefe?"

    menu:
        "A primeira impressão não foi muito boa.":


            mc envergonhado "Sei lá... acho que não foi a melhor das impressões. Ela parece bem rígida e se acha um pouco."

            n "Hah. Dá pra entender porque você achou isso. Ela é direta demais. É duro acostumar."
        "Parece uma pessoa inteligente.":


            mc normal "Eu achei ela uma mulher inteligente. Não é uma pessoa super agradável, mas dá pra ver que ela é bem interessante."

            n "Você tem a cabeça boa, né? É duro as pessoas gostarem dela logo de cara."

            n "A maioria vai falar que ela é chata, ignorante e talz. Mas aquela mulher sabe o que tá falando. Além de ser sincera."

    n "Se tem uma coisa que eu aprendi com ela é que a gente sempre pode ir além."

    mc desconfiado "Hmm..."

    n "A maioria das pessoas parece que se acomoda e aceita a vida que tem, sabe?"

    n "E ela é uma mulher que me ensinou que a gente não precisa ser assim. Que a gente sempre pode buscar mais."

    n "Seja lá qual for seu sonho. Se é amor, dinheiro, sucesso, tranquilidade, se a gente realmente focar e arriscar a gente pode conseguir."

    mc envergonhado "Você tá parecendo um herói de desenho falando."

    n "Hahaha! Pode crer, né? Acredite no seu coração e você conseguirá!"

    mc "Exatamente."

    n "Pareceu mesmo... mas é verdade. Só que é duro de explicar assim... deixa pra lá, a gente já tá chegando. Aqui é meu prédio."

    mc normal "Então é aqui que você mora. Parece bacana."

    n "Espera pra ver lá dentro. É pequeno, mas é massa."

    scene black with dissolve

    "..."

    $ tempo = 3

    scene n7_img13 with Dissolve(1.0)

    pause

    mc normal "Uou. Então esse é seu apê. Massa."

    n "Gostou mesmo?"

    mc "É incrível, [n]."

    if casa:

        mc charmoso "Agora eu tô vivendo em um maior, mas quando vim pra capital, meu apê era um ovo."
    else:


        mc angustiado "Você tem que ver o meu! Aquele ovo é um quadrado sem nada..."

        mc zerado "Um dia eu ainda vou mudar pra um lugar melhor você vai ver."

    n "Se sinta em casa, tá?"

    mc charmoso "Valeu."

    scene n7_img14 with Dissolve(1.0)

    pause

    n "Desculpa chamar você assim de uma hora pra outra. Mas é que eu precisava falar com você o mais rápido possível."

    mc desculpa "Aconteceu alguma coisa?"

    if nathan_namoro:

        n "Quando você aceitou namorar comigo lá na festa, eu nem acreditei... mesmo depois de eu ter contado tudo pra você, você confiou em mim."

        n "Só que isso só me deixou mais nervoso. Eu precisava falar com você assim que desse..."

    elif nathan_quente:

        n "Mesmo a gente não tendo nada sério, a gente já ficou antes. E eu tenho um carinho muito grande por você, [mc]."

        n "Eu quero deixar claro pra você tudo o que aconteceu."
    else:


        n "Você é um grande amigo. E eu sempre te vi assim. Não vou mentir que já teve vezes que eu até pensei em ter algo mais com você."

        n "Você é um cara legal que já me ajudou mais de uma vez. E em respeito a você e nossa amizade eu queria resolver esse clima."

    n "Acho que... o que eu tô querendo falar é que eu queria me desculpar com você por tudo."

    mc desculpa "Por que a gente não senta e você fala com calma tudo o que você tá pensando?"

    n "Acho que seria uma boa."

    n "Por favor, pode sentar aqui."

    mc "Com licença."

    scene n7_img15 with Dissolve(1.0)

    pause

    n "Então... talvez eu acabe repetindo umas coisas que eu já falei. Desculpa por isso. Mas é que eu não lembro o que eu te falei na festa."

    "O [n] parece bem nervoso."

    menu:
        "Eu estou aqui pra ouvir você.":


            mc "Relaxa. Eu vim aqui pra ouvir você. Pode falar tudo o que você precisar."

            n "Valeu, [mc]. E você mais uma vez vai me salvar dessa coisa ruim que eu me meti."
        "Seja o mais rápido possível, por favor.":


            mc "Se você puder, tente acelerar porque eu realmente só quero saber o essencial sobre isso."

            n "Ah! P-pode deixar. Desculpa... eu vou tentar acelerar o máximo."

            mc "Valeu."

    n "Eu queria que você soubesse que o que eu sinto por você é de verdade. Nossa amizade cresceu de uma forma verdadeira."

    mc "Mas, [n]. Se você realmente tava pensando em mim, por que não me contou nada?"

    mc "Você falou que desde o começo, desde o início de tudo, inclusive o lance de você ser expulso. Tudo já tava certo!"

    mc "Por que você me deixou preocupado, correndo atrás de uma juíza maluca?!"

    n "Eu sei... sei que isso foi foda. Eu enganei você. Eu assumo isso, de verdade! Me desculpa!"

    n "Quando a gente conversava, eu realmente tava mentindo! Eu tinha que fazer você acreditar! Tudo tinha que parecer real pra funcionar!"

    n "E a questão é que... eu acabei aceitando tudo o que me passaram."

    mc "Quem te passou o quê?"

    n "Não quero tirar minha culpa das coisas... e nem falar que eu tinha tudo no controle."

    n "As coisas foram mais confusas do que pode parecer, sabe? No fundo, era isso que eu queria falar pra você."

    "Ele tá falando que ele também não sabia direito o que tava acontecendo?"

    "Como? Como pode ele não saber exatamente o que tava acontecendo em um plano mirabolante desses..."

    "Eu não queria ser aquela pessoa cética que duvida dos outros... e se ele ainda estiver me enganando?"

    "Depois de tudo isso ele vem e fala que também não sabia das coisas 'completamente'?"

    "Será que eu vou acreditar no [n] agora?"

    menu:
        "Acho que eu acredito em você.":


            mc "Eu acredito em você, [n]. Se você tá falando que não tinha certeza do que tava acontecendo, eu tenho que acreditar."

            n "Sério, [mc]? Você acredita em mim mesmo?"

            mc "É o que eu tô tentando fazer. Tentar te dar o benefício da dúvida. Tentar ser menos negativo e pensar no seu lado."

            n "Você é um cara e tanto, [mc]... não sei outra pessoa que faria essa pra mim em uma condições dessas."

            if nathan_namoro:

                mc "Eu aceitei ter algo sério com você, né? Eu vou acreditar em você."
        "Não posso acreditar em você.":


            if nathan_namoro:

                mc "Olha, [n]... eu sei que a gente tá num relacionamento agora, mas isso que a gente tem, precisa ser construído na confiança."

            mc "Você tá falando que não sabia tudo o que tava acontecendo? Mas ao mesmo tempo tava me enganando na caruda."

            mc "Isso não faz muito sentido, faz? Como eu posso acreditar nisso agora?"

            mc "O que parece é que você só quer me enganar de novo!"

            n "[mc]... eu entendo..."

    scene n7_img16 with Dissolve(1.0)

    pause

    n "Eu sei que no fundo não faz sentido o que eu tô falando, mas é a verdade."

    n "No fundo, o que a gente acha não vale nada pra eles. Você acha que eles se preocupam com nossa amizade?"

    mc serio "De quem você tá falando? Da Blergh? Da [ve]?"

    n "Eu não sei..."

    mc desculpa "De novo isso?"

    n "[mc]... você é um homem diferente, sabe? Você é corajoso. Você vai entrando de cabeça nas coisas."

    n "Você ajuda as pessoas e se interessa de verdade pela gente. Mesmo nos rolos mais cabeludos. Parece que nada te dá medo."

    mc zerado "Não é bem assim, [n]... eu já me fodi muito nessa cidade."

    n "É sim. Só que nem todo mundo tem essa coragem que você tem. Pra mim, a maioria das pessoas só quer ser feliz, sabe?"

    n "Elas tão pouco se fodendo pros outros. Contanto que elas se deem bem, é o que importa."

    n "E é duro admitir isso, sabe? A gente quer falar que a gente não pode ajudar, que não tem como fazer alguma coisa."

    n "Mas a verdade é que a gente é tudo bundão mesmo. Você é corajoso de verdade e por isso você não entende."

    mc envergonhado "Valeu... mas não tô entendendo onde você quer chegar..."

    scene n7_img17 with Dissolve(1.0)

    n "Eu sei que eu não tô fazendo nenhum sentido agora. Mas é que eu não sou muito bom em falar as coisas que eu tô pensando."

    n "Mas... se meu carinho por você vale alguma coisa, eu queria te avisar de um negócio."

    mc desconfiado "Hm?"

    n "A Blergh! era um nada até um tempo atrás. E usando minha situação eles conseguiram bastante mídia."

    n "Mas não é só isso, sabe?"

    n "Eles tiveram apoio da Faux pra conseguir chegar da forma certa até as pessoas."

    n "Só que a sua revista não quis participar. Isso eu ouvi da própria [ve]. Ela odeia sua revista por causa disso."

    mc "Sério? Então o chefe não quis..."

    n "Parece que foi isso. Só que alguém lá conseguiu usar minha história pra falar da Blergh! mesmo assim."

    menu:
        "E você sabe quem é?":


            mc desconfiado "E quem é essa pessoa? Você sabe?"

            n "Óbvio que é a [j]."

            mc surpreso "Verdade! Ela fez seu perfil na revista!"
        "Eu tenho certeza quem é.":


            mc surpreso "A [j], claro!"

            n "É..."

    n "Por isso que eu disse que não é só a Blergh!. Tem alguma coisa muito grande por trás da [ve] e da marca."

    n "E eu não sei exatamente quem é. Mas com certeza tem a ver com a [j] e com a Faux. Mas tem mais coisa por trás."

    n "Mas eu acho que não é só a mídia. Eles têm dinheiro também. E talvez até alguma coisa na Justiça."

    n "Será que aquela juíza que me livrou realmente foi justa na decisão?"

    menu:
        "Impossível saber...":


            scene n7_img18 with Dissolve(1.0)

            pause

            mc "Não vai ter como a gente saber. Mas talvez ela também esteja envolvida nisso aí que você tá falando..."

            n "Eu acredito que ela tá..."
        "Aquela juíza é bem estranha.":


            scene n7_img18 with Dissolve(1.0)

            pause

            mc "Olha, pelo que eu vi, aquela juíza era uma pessoa bem diferente. Ela tinha um gostos bem particulares."

            mc "Mas não sei se tem a ver com as decisões dela."

    mc "Quando a gente conversou ela disse que a Justiça era suprema. Ela falou como uma pessoa honesta pelo menos."

    mc "Mas falar e fazer são coisas diferentes..."

    n "..."

    mc "Olha, [n]... a primeira vez que a gente se viu no bar, eu só fui falar com você por causa da [j]."

    mc "Ela tinha um lance contra mim que se eu não tivesse aceitado, eu ia me ferrar com uma celebridade."

    mc "Eu fiz a mesma coisa que você. Eu coloquei meus objetivos em primeiro lugar. Não pensei no que você tava sentindo de verdade."

    n "Mas é pouco, [mc]. Isso não é quase nada se comparado com o que eu fiz."

    mc "Então... o que eu quero dizer é que às vezes a gente se sente pressionado pelas pessoas que são maiores do que a gente."

    mc "É fácil falar que a gente tem que fazer o 'certo' não importa o que aconteça. Mas isso aqui não é filme de super herói."

    mc "A vida é mais complicada do que isso. Não é faz de conta. E às vezes a gente precisa mesmo colocar nossos objetivos na frente."

    mc "O que eu quero dizer é que... eu entendo você."

    n "[mc]... Valeu..."

    mc "Agora, o que vai rolar? Você conseguiu o emprego na Blergh. E a [ve] tá levantando a empresa. Acabou?"

    n "Eu não acho... eu acho que isso foi só o começo. A Blerg!h tem uma grande marca rival que domina o mercado nacional."

    n "A [ve] vai atrás deles, com a ajuda dessas pessoas que eu te falei."

    n "Inclusive, acho que tem coisa pra você aí."

    mc "Pra mim?!"

    n "Eles não podem saber que eu te falei isso... mas depois do que você fez por mim, eu tenho que te ajudar também."

    n "Eles sabem que hoje em dia mídia é muito importante. Jornais, TV, influenciadores. Eles querem controlar tudo, inclusive sua revista."

    n "Se a [ve] quiser algo com você... você aceitaria?"

    "Aceitar um lance com a Blergh!? Por que o [n] tá me perguntando isso agora?"

    "Eu tenho uma boa ideia de quem faz parte desse grupo... e parece que eles tão em todos os lugares..."

    "Todos os famosos com que eu converso... Parece que eles fazem sombra em todos os lugares."

    "O que eu vou fazer?"

    menu:
        "Eu aceitaria uma parceira com a Blergh!.":


            $ blergh_parceria = True

            mc "Ah, mano. Se a proposta for boa, acho que eu aceitaria algo com eles, sim."

            n "Sério mesmo?"

            mc "Por isso que eu falei que eu te entendo. Tá todo mundo querendo se dar bem, sabe?"

            n "Heh... certeza que a [ve] vai gostar de você. Você é bem pragmático e ela procura isso nas pessoas."

            mc "Mas espero que se pintar algo assim, seja algo bom. Não vou me vender por nada."

            n "Eles são poderosos, [mc]. Pode ter certeza que vai ser um lance grande."

            mc "Vamos ver..."
        "Eu nunca me juntaria a eles.":


            $ blergh_parceria = False

            mc "Tá louco? Depois do que eles fizeram com a gente? Impossível."

            n "Eu imaginei que você diria isso... você é um cara de valores, [mc]. Não um vendido igual eu..."

            mc "Não precisa ser duro assim com você também. Cada um é um."

            n "Verdade... e eu fico feliz de tá perto de alguém assim. Que tem coragem pra seguir aquilo que acredita."

            mc "Espero que isso não acabe comigo..."

            n "É... cada escolha tem seus pontos bons e ruins..."

    if nathan_namoro:

        n "Ufa... finalmente eu consegui tirar isso do peito."

        mc "Agora que você terminou, e se a gente namorasse um pouco?"

        n "Não tem problema por você? Eu tava precisando muito disso."

        mc "Eu vou te ajudar então."

    elif not nathan_namoro and nathan_quente:

        n "Ah... com isso fora do caminho..."

        mc "Hm?"

        scene n7_img19 with Dissolve(1.0)

        pause

        n "É... tem outra coisa que eu queria falar com você hoje..."

        n "E é mais por isso que eu queria tanto falar pra você tudo isso. Eu tinha que ser sincero com você sobre tudo isso."

        n "Porque... a gente já ficou antes... e eu realmente senti algo especial entre a gente, [mc]..."

        n "Por isso... eu quero perguntar uma coisa pra você..."

        mc "Ai..."

        n "Você... quer ficar comigo de forma séria? Assim... oficiais?"

        mc surpreso "N-nathan!"

        n "Eu sei que depois do que eu fiz eu vou precisar correr muito pra conquistar sua confiança de novo, mas eu tô pronto pra isso."

        n "Eu queria deixar isso pra trás e retomar aquele lance legal que a gente tinha..."

        mc desculpa "Eu não sei..."

        "Eu e o [n] realmente já ficamos... e ele com certeza é um cara legal..."

        "Será que eu vou conseguir superar essa traição dele? Porque não adianta aceitar e depois ficar falando sobre isso."

        "Perdoar é perdoar. Se eu quiser namorar ele, vai ser pra valer. É pra entrar de cabeça."

        "O que eu respondo?"

        menu:
            "Sim. Eu quero namorar você.":


                $ nathan_namoro = True

                mc charmoso "Com você falando desse jeito, não tem como eu resistir. Eu aceito."

                n "S-sério mesmo?"

                mc "Você mereceu depois de fazer essa carinha de cachorro arrependido. Eu tô pronto pra deixar isso tudo pra trás."

                n "Eu também, [mc]. O-obrigado."

                mc safado "Agora vem aqui."
            "Não. Eu quero ser seu amigo.":


                mc desculpa "Desculpa, cara, mas aquilo que rolou ficou no passado. Eu não conseguiria ter algo sério com você."

                mc "Você é um cara bacana, é gato pra caralho, mas depois de tudo isso, não acho que seria saudável."

                mc "Eu nunca ia ter confiança plena em você de novo e aposto que isso só ia acabar ferrando o que a gente tem."

                mc "Eu quero ser seu amigo, porque eu realmente acho você alguém interessante, s-se você aceitar, claro."

                n "Merda... eu sabia que ia ser impossível pra gente desde o começo... mas eu tinha que tentar... desculpa."

                mc "Não precisa pedir desculpas."

                n "E claro que eu vou querer ser seu amigo. Eu te admiro muito, [mc]."

                mc "Que bom. É..."

    elif not nathan_namoro and not nathan_quente:

        n "Bom... foi pra isso que eu te chamei. Obrigado por ter vindo. Ter tirado isso do peito foi muito importante pra mim."

        n "O gosto amargo de trair um amigo não vai embora rápido, mas só de você ter me ouvido ajuda muito."

        mc "Não se esquece que todos nós fazemos nossa dose de burradas. Tenta não pensar muito nisso."

        n "Valeu mesmo, [mc]."

    if nathan_namoro:

        $ nathan_e7 = "seducao"

        mc "Por que você não vem aqui comigo?"

        n "C-claro."

        scene black with dissolve

        scene n7_img20 with Dissolve(1.0)

        pause

        mc "Tanta coisa aconteceu. Eu só queria mesmo poder ficar assim com você por um tempo."

        n "Desculpa de novo por ser mais uma fonte de problemas pra você."

        mc "Não é problema. Se não fosse você, nem sei se eu ainda estaria por aqui. Você é minha força, isso sim."

        n "É o contrário, bobo. Sem você eu não teria conseguido nada. Nem meu emprego e nem estaria aqui no país."

        n "Você realizou meu sonho e agora eu quero que você realize o seu também."

        n "Tudo o que você precisar, eu vou fazer tudo o que eu puder pra te ajudar."

        mc "Obrigado. É muito bom poder contar com alguém."

        n "Essa cidade tá cheia de gente ruim, cheia de coisa pra foder a gente, mas eu vou ser um porto seguro pra você."

        n "Eu prometo que não vou deixar nada chegar perto de você."

        mc "[n]... eu só quero uma coisa agora."

        n "O quê? Pode falar. Se eu pude-"

        scene black with dissolve

        mc "Xiu. Cala a boca."

        scene n7_img21 with Dissolve(1.0)

        pause

        n "Hmm..."

        mc "O que eu quero agora é beijar você."

        n "N-nisso eu posso ajudar..."

        window hide

        pause

        n "Vem aqui mais perto."

        scene n7_img22 with Dissolve(1.0)

        pause

        n "Hoje a gente vai dormir juntos, certo?"

        mc "Se tiver ok pra você... a gente nem vai dormir..."

        n "!"

        n "Eu topo... eu topo muito."



        label n7_premium1:

            pass

        menu:
            "Eu quero brincar com você antes (+18)":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_17

                    jump n7_premium1

                mc "Antes de ir pra cama... deixa eu aproveitar você melhor."

                n "Hmm... eu sou todo seu."

                mc "Então tira a parte de baixo também."

                scene black with dissolve

                scene n7_premium1 with Dissolve(1.0)

                pause

                n "Hmm..."

                mc "Quantas vezes a gente já ficou, hein?"

                n "Quem tá contando? Cada vez fica mais gostoso."

                mc "Pra mim também."

                n "E a gente tá cada vez mais perto de resolver os problemas e podermos ser felizes juntos."

                mc "Você realmente tá pensando nisso?"

                n "Claro. Não importa onde seja, se você tiver comigo, eu quero tá lá."

                mc "[n]..."

                n "E você pode tirar tudo também."

                scene n7_premium2 with Dissolve(1.0)

                pause

                mc "O-opa."

                n "Mas não para de beijar."

                mc "Não paro. Eu quero passar a noite toda com você."

                n "Hmm... nem acredito que a gente chegou aqui."

                n "Nós dois... não é nenhum lugar perigoso, ninguém pode atrapalhar a gente."

                mc "Era o que eu tava esperando mesmo."

                n "Então aproveita, gostoso. Hoje é nosso dia."

                mc "Sim..."

                "Eu vou dar uma atenção pra ele ou quero tudo só pra mim."

                menu:
                    "Eu começo cuidando dele":


                        mc "Eu vou aproveitar você inteiro mesmo."

                        scene n7_premium3 with Dissolve(1.0)

                        pause

                        n "Hmm..."

                        n "Eu adoro quando você beija tudo."

                        mc "Eu quero fazer você sentir gostoso agora."

                        n "Então continua que tá funcionando... você é o melhor, [mc]."

                        mc "Você não viu nada, gato."

                        mc "Aqui é só o começo."

                        n "Eu tô gostando desse papo... pra onde que a gente vai agora?"

                        mc "Pro meu lugar preferido."

                        mc "Senta que eu vou me ajeitar..."

                        n "Ah... não fala assim que eu já fico arrepiado."

                        mc "Vem com ele..."

                        scene black with dissolve

                        scene n7_premium4 with Dissolve(1.0)

                        pause

                        mc "Hmm..."

                        n "Ah..."

                        mc "Deixa eu cuidar dele pra você."

                        n "Isso... assim mesmo... ah..."

                        mc "Eu vou devorar ele inteiro, [n]."

                        n "Ele é todo seu..."

                        mc "Vou começar por baixo, ok?"

                        n "Faz o que você quiser, gato... hmm... tá muito bom..."

                        mc "E agora o prato principal."

                        n "S-sim!"

                        scene n7_premium5 with Dissolve(1.0)

                        pause

                        mc "Hmm!"

                        n "Aaahh... você colocou ele qusae inteiro."

                        mc "Nnnghh!"

                        n "Se você continuar assim, [mc], eu não vou aguentar muito, não."

                        mc "Só vai, gato."

                        n "Você quer mesmo acabar comigo... hmm..."

                        mc "NMmmnm..."

                        n "Então vai... mais um pouco... aah..."

                        n "Você chupa tão gostoso, [mc]. Aahnn... continua assim..."

                        mc "Aahn..."

                        n "Isso... continua fazendo forte... assim... mais rápido... aah!"

                        n "Tá vindo, gostoso! HNn! Mais rápido! Vai! Não para! NNNGH!!"

                        n "AAAGHH!"

                        scene n7_premium6 with vpunch

                        pause

                        n "Aaaahghh!"

                        n "Tô gozando!"

                        mc "Mmnmmm!"

                        n "Aah... que delícia..."

                        mc "Gostou?"

                        n "Demais..."

                        mc "Essa foi só a primeira vez da noite, vai ter muito mais."

                        n "Calma aí que tem sua recompensa."
                    "Hoje ele só vai cuidar de mim":


                        mc "[n], eu preciso de você aqui em baixo."

                        n "Hmm... tá assim, é?"

                        mc "Vem... meu pau precisa de você."

                        n "Safado..."

                n "Pode deixar que eu vou fazer você sentir gostoso pra caralho."

                mc "T-tá..."

                scene black with dissolve

                scene n7_premium7 with Dissolve(1.0)

                pause

                n "Vou começar pegando aqui. Bem de leve."

                mc "A-ah..."

                n "Não se preocupa que eu sei cuidar bem de você."

                n "Você fez eu me sentir bem várias vezes, [mc]. Não só no sexo, mas na cabeça também."

                n "Várias vezes eu me senti preso e foi você que me tirou daquele lugar horrível."

                mc "E-eu nunca fiz nada..."

                n "Para de modéstia... você foi a pessoa mais importante que apareceu na minha vida aqui nessa cidade corrompida."

                n "Uma pequena luz no meio de toda a sombra."

                n "Eu quero que você tenha tudo do bom e do melhor. Você merece ser feliz por tudo o que você fez por mim."

                mc "E-essa é uma boa forma de você me agradecer..."

                n "Eu preciso agradecer mais ainda... pra você ter certeza que eu tô agradecido de verdade."

                mc "Sério? E como vai ser iss-"

                scene n7_premium8 with Dissolve(1.0)

                pause

                mc "Aah..."

                n "Fazendo você gozar muito gostoso em mim..."

                n "Eu vou tomar tudo o que você tem aí."

                mc "Aah... não fala assim que você deixa tudo mais quente ainda."

                n "Então vai... goza na minha boca, vai."

                n "Goza gostoso pro seu homem aqui."

                mc "Ah..."

                n "Isso... não precisa se segurar... jorra tudo em mim!"

                mc "Então vai! Eu tô quase lá!"

                scene n7_premium9 with hpunch

                pause

                n "NGH!"

                mc "Eu tô quase lá! Vai mais forte, gostoso!"

                mc "Usa essa boca gostosa pra me chupar que eu tô quase lá! Pelo amor! Ahh!"

                n "Nnnnghh!"

                mc "Mais um pouco. Aí!"

                mc "Vai!"

                scene n7_premium9 with hpunch

                mc "AAAHHH!!!"

                mc "GOZANDOO!!!"

                n "!!!"

                mc "Isso! Aah! Aaah..."

                n "Delícia..."

                mc "Aproveita tudo, gato... tem bastante pra você..."

                n "Eu quero tudo..."

                mc "Caralho... isso foi bom..."

                n "Que bom que você gostou. Bora pra cama agora?"

                mc "Bora!"

                scene black with dissolve

                mc "Hmm..."

                n "Hoje a gente não para..."

                scene n7_new1 with Dissolve(1.0)

                pause

                mc "Assim mesmo gostoso... me beija mais."

                n "Hoje você tá com um fogo."

                mc "E você também, não adianta reclamar."

                n "Eu tô é gostando, bobo. Deixa eu aproveitar."

                mc "Aproveita..."

                n "Ah..."

                mc "Hmm..."

                scene black with dissolve

                scene n7_premium10 with Dissolve(1.0)

                pause

                mc "Assim mesmo..."

                n "Aah..."

                mc "Eu tava precisando de um momento só nosso assim, pra saber que essa cidade vale alguma coisa."

                n "O que a gente viveu aqui essa noite vale por uma vida pra mim."

                mc "E pra mim, não? Tanta coisa aconteceu aqui, mas é tando do seu lado que eu senti que faz sentido tudo isso."

                n "[mc]... você sabe mesmo me deixar com vontade..."

                mc "Então vem. Eu ainda tenho energia."

                scene n7_premium11 with Dissolve(1.0)

                pause

                n "Ah..."

                mc "Hmm... assim mesmo..."

                n "Você gosta?"

                mc "Eu adoro... vai..."

                n "Não para de beijar..."

                mc "A gente vai acabar gozando de novo assim..."

                n "É minha intenção... mais uma... duas... três..."

                mc "Ah..."

                n "Hoje a gente vai acabar se tornando um só de tanto que a gente vai se pegar."

                mc "Isso... eu quero isso... e mais um pouco."

                n "Tarado..."

                mc "Por você..."

                scene black with Dissolve(1.0)
            "Vamos pra cama":


                mc "Então vem. Vamos pra cama"

                n "Opa..."

                window hide

                pause

                scene black with dissolve

                n "Tira tudo pra mim, [mc]."

                mc "E vem aqui pra eu te ajudar."

                scene n7_new1 with Dissolve(1.0)

                pause

                mc "Assim mesmo gostoso... me beija mais."

                n "Hoje você tá com um fogo."

                mc "E você também, não adianta reclamar."

                n "Eu tô é gostando, bobo. Deixa eu aproveitar."

                mc "Aproveita..."

                n "Ah..."

                mc "Hmm..."

                scene black with Dissolve(1.0)

        "..."

        $ dia += 1
        $ tempo = 1

        scene n7_img23 with Dissolve(1.0)

        pause

        n "Nossa... você capotou, hein..."

        mc "Deixa eu dormir..."

        n "Cansou de me usar?"

        mc "Não aguento mais. Deixa eu dormir até de noite."

        n "Haha... eu tenho que sair trabalhar."

        mc "Azar o seu. Antes de sair, você podia deixar algo pronto pra eu almoçar."

        n "Bebezão... mas você merece. Você foi uma delícia."

        mc "Você também. Agora tchau... quando eu acordar eu vou pra ilha, se não a chefinha vai pegar no meu pé."

        n "Que pena... você podia passar uns dias aqui."

        mc "As coisas tão meio corridas agora, mas quem sabe na próxima?"

        n "É uma promessa, hein?"

        show black with dissolve

        hide black with dissolve

        mc "Tá... mas agora eu não consigo mais falar... awwwnnn..."

        n "Bons sonhos, [mc]."

        mc "Valeu, [n]..."
    else:


        mc "Se era isso, acho que eu vou indo nessa, tudo bem?"

        n "T-tudo, bem."

        mc "Qualquer coisa me fala, tá? Eu ainda te considero um grande amigo e aposto que a gente ainda pode conseguir muita coisa."

        n "Valeu por ter vindo, [mc]. Você é meu parça, de verdade."

        mc "Até, cara."

        n "Até. E toma cuidado, ok? Qualquer coisa pode me chamar. Eu tô aqui pra você também."

        mc "Demorou. A gente se fala."

    scene black with Dissolve(1.0)

    "..."

    scene mc onibus_noite with Dissolve(1.0)

    if nathan_e7 == "seducao":

        "A noite com o [n] foi incrível. Pena que eu tenho que voltar pra ilha..."

        "Não vejo a hora de ver ele de novo."

    "A conversa com ele foi bem tensa... mas eu acho que ele foi sincero comigo."

    "A Blergh! então tá envolvida com gente ainda maior que eles. É o mesmo povo que tá envolvido em outros esquemas."

    "Essas pessoas parecem ser as donas da capital."

    "Eu sinto que a hora da verdade tá cada vez mais perto. Logo eu vou ter que decidir de que lado eu vou ficar."

    "Espero que eu faça a decisão certa... se é que existe certo ou errado nessa situação."



    label nathan_e7_final:

        pass

    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v45_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v45_fim","final","local")

    call checa_final from _call_checa_final_2

    jump call_cidade

label nathan_evento8:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("n8_save", extra_info="n8_save")

    $ iconchefe += 1
    $ estou_na_cidade = False
    $ nathan_e8 = "evento"
    $ distrito_liberou = True
    $ nathan_stifler = 0

    scene black with dissolve

    if tempo < 3:

        scene mc parque_sentado with Dissolve(1.0)
    else:


        scene mc parque_sentado_noite with Dissolve(1.0)

    "Caraca... tudo o que aconteceu no Cassino..."

    $ distrito_liberou = True

    "Meu coração ainda dá batendo."

    if black_salva > 0:

        "Eu quase morri."

        "E teria ido pra cova se o-"
    else:


        "Eu deixei a Diana lá e me aliei com os poderosos da ilha."

        "Claro que eu ainda não fui aceito no Grupo, mas o Tony me pediu ajuda com o Nathan."

        if grupo_nathan == 1:

            "E eu aceitei ajudar."

            "Eu tô cada vez mais perto deles."
        else:


            "Não quis ajudar com o Nathan, mas eu ainda preciso de um jeito de não morrer de novo."

        "Preciso ver a melhor forma de me manter vivo, isso sim."

    "???" "E aí, bro."

    scene n8_img1 with hpunch

    mc "[us]! Como você tá aqui?!"

    us "Você sempre passa por aqui, cara."

    mc "Isso é... tudo fica em volta da praça."

    us "Daí só te esperar aqui que uma hora tu passa, parceiro."

    mc "Previsível... se alguém quisesse me pegar nem ia ter trabalho."

    us "Tá aí algo pra tu pensar. Ainda mais agora que você tá se envolvendo com umas pessoas barra pesada aí."

    mc "Nem fala um negócio desses..."

    if black_salva > 0:

        us "Fica de boa. Hoje eu vim pra dar uma boa notícia."

        mc "Qual foi?"

        us "Consegui o que tu pediu pra mim lá no hospital."

        mc "Mentira!"

        if black_salva == 1:

            us "Sua barra tá limpa lá no Distrito. Pode ir lá quando quiser, beleza?"

            us "Tua moral tá alta lá depois dessa."
        else:


            us "A garota que tu pediu ajuda. Ela vai ficar segura."

            mc "Sério?! Mas como?!"

            us "Os carcamanos querem manter uma boa relação com o Distrito."

            us "Só tive que pedir pra Madame Nora gastar um pouco da moral dela."

            "Será que vai ser tão fácil assim?"

        mc "Valeu mesmo, [us]!"

        mc "Ufa... uma coisa a menos pra me preocupar."

        us "O que tu fez pela mana Diana não foi pouco."

        menu:
            "Vamos torcer pra Diana tá bem agora... seja lá onde ela tá agora.":


                pass

        us "A mana é esperta. Bora confiar nela, mano."

        mc "É..."

        us "Eu vou querer que tu faça a boa pra mim de novo."
    else:


        "O Black Cash também tem rolo com o Tony e os outros."

        "Tenho quase certeza que o Distrito e o Grupo tão juntos no comando da ilha."

        "Se eu conseguir me aproximar dos dois, melhor pra mim."

        us "Preciso da tua ajuda numa coisa."

        us "Você viu o que aconteceu com a Diana?"

        mc "Sei. A cantora do Cassino."

        us "Então. Quero tentar salvar outra mana nossa."

        mc "Salvar?"

    mc "Que tipo de 'boa'. Eu tô meio aqui de rolo."

    us "A gente tem outra mana precisando de ajuda. Do mesmo que aconteceu com a mana Diana."

    mc "Não é possível. Como pode?!"

    us "Será que tu pode salvar ela?"

    mc "E-eu?!"

    if black_salva > 0:

        us "Você salvou a mana de baixo do nariz do Barão."

        if d7_faca == 2:

            us "E ainda matou o desgraçado."

            mc "Matei mesmo?!"

            show black with dissolve

            show faca_barao with Dissolve(1.0)

            us "Matou. Ele não aguentou a facada que tu deu e morreu no hospital."

            menu:
                "Consegui, porra! Eu matei o filho da puta!":


                    pass

            us "Matou, cara. Na base da facada mesmo."

            mc "Porra... que foda... s-só que... mano... tô tremendo, cara!"

            us "Calma..."

            mc "E-eu tô fodido! A polícia! Vou passar a vida na cadeia!"

            us "Por quê? Tu acha que eles vão denunciar pra polícia?"

            mc "Ok... eles não podem chamar atenção, mas mesmo que eles não denunciem a polícia vai ter que descobrir."

            us "Esqueceu que eles mesmos controlam a polícia? Eles vão chegar na conclusão que ele caiu da escada."

            mc "Caraca, [us]... verdade? Tipo... acha que eu tô limpo?"

            us "Limpo não sei, cara. Mas com certeza não vai rolar um processo normal."

            menu:
                "Tô satisfeito de ter matado o FDP. Mas sinto que isso ainda vai voltar pra me foder de algum jeito...":


                    pass

            us "Foca aqui agora."

            mc "V-vou tentar..."

            hide faca_barao with dissolve

            hide black with dissolve

            us "Eu tava falando da Rox."

            mc "Beleza."

            "Não pensa demais nisso, [mc]. A coisa tá feita. Você tava protegendo a Diana."

            "Você não é um assassino. Era pra defesa!"

            "Isso... deixa eu focar no que ele tá falando da Roxane."
        else:


            us "Só faltou mesmo matar o Barão... ele merecia."

            mc "Eita..."

            "Será que se eu tivesse esfaqueado o Barão ele morria? Que loucura..."

            "Imagina o rolo que eu taria se eu tivesse assasinado alguém?"

    us "Ela tá trabalhando numa marca de roupa. Coisa fashion aí."

    mc "Não vai me dizer... a Blergh!..."

    us "Como você sabe?!"

    mc "O mundo é pequeno. Só chutei."

    us "Então nem preciso falar mais nada. Você sabe quem é. Uma das modelos deles que vive aqui na capital."

    menu:
        "A Roxane.":


            pass

    mc "Ela é amiga do Nathan. Tive a chance de falar com ela na festa e outro dia lá quando ela tava treinando com a Zaza."

    us "Essa mesma."

    scene black with dissolve

    scene n8_img2 with Dissolve(1.0)

    us "Quebra essa pra mim por favor. Dá um jeito de tirar ela de lá."

    us "Nem que você tenha que foder aquela Blergh!. Eles merecem pelo que fizeram com ela."

    if black_salva > 0:

        mc "[us]... isso é muito sério. E como que eu ia fazer isso?"

        us "A gente vai tá contigo, mano. Só faz a boa e o Distrito vai tá nas suas costas."

    mc "Mas pensei que vocês fossem parceiros. Não vai pegar mau vocês irem contra eles desse jeito?"

    us "É uma coisa complicada, [mc]. Faz o que eu tô falando pros seus irmãos. E a gente vai te ajudar a acabar com esses cretinos."

    "Acabar com esses 'cretinos'. De quem ele tá falando?"

    "Será que é real esse lance de um grupo que opera nas sombras da Capital? Isso parece muito coisa de filme, cara."

    "Mas... no Cassino. O jeito que eles tavam lá. Com certeza tem um bando de gente poderosa atuando pra garantir seus objetivos."

    "Será que é tão 'coisa de filme' assim um bando de gente rica e poderosa garantindo que eles continuem ricos e poderosos?"

    if black_salva > 0:

        "E se for verdade... depois do que aconteceu no Cassino, não sei se eles vão me querer do lado deles."
    else:


        "E depois daquela reunião com o Tony e o Barão, e do jeito que eles falaram com o prefeito. Realmente parece que eles são amiguinhos."

        "Toda essa história de Grupo. Tô começando a achar que ele realmente existe. No estilo filme de máfia mesmo..."

        "Caralho... que loucura..."

    "Mas é uma boa eu me meter com esse povo? Tipo... o que eu quero com eles?"

    menu:
        "Acabar com esses criminosos que mandam na capital":


            $ n8_grupo = True

            mc "Eu não vou ficar quieto vendo o que eles fazem com minhas amigas e meus amigos."

            mc "Muita gente sofreu na mão desses cretinos. E o que eu puder fazer pra ajudar eu vou."

            us "Caralho. Mandou a real agora, bro."
        "Ficar de boa na minha e não me arriscar com essa gente":


            mc "Eu só quero curtir e ter minha vida, entendeu?"

            us "Tô ligado. Mas então pensa na guria. Ela não marece aquilo."

            mc "Ninguém merece o que aconteceu com a Diana."
        "Eu quero fazer parte desse grupo com você e os italianos.":


            us "Heh... não pensei que você fosse desse tipo ambicioso."

            mc "Se você pode, por que eu não posso?"

            us "Se você tem sangue de barata pra isso."

    if black_salva > 0:

        mc "E não é só isso."

        "Eu realmente tô devendo uma pra ele. Mais do que uma."

        "Se o [us] não tivesse me achado no ponto de ônibus e levado pro hospital eu taria 7 palmos abaixo da terra agora."

    menu:
        "Eu vou lá na Blergh! e vejo o que dá pra fazer.":


            pass

    us "Tô contando com você, parça."

    if black_salva > 0:

        mc "E valeu por ter me salvado."

        us "É o que os amigos fazem. Pode sempre contar com o mano Black aqui."
    else:


        us "E não se preocupa com os carcamanos."

        us "Se você fizer essa por mim, eu garanto que eles vão olhar pra você. É sua chance de entrar no grupinho tosco deles."

        mc "Hmm..."

    mc "Falou, mano."

    if black_salva > 0:

        "O Distrito... e principalmente o mano Black Cash acabaram virando meus aliados nessa doideira."
    else:


        "O jeito que ele fala... a prefeitura e o Distrito realmente são aliados?"

    scene black with dissolve

    scene parque dia with Dissolve(1.0)

    "Vou ter que dá um pulo na Blergh! e ver lá como as coisas vão ser."

    if nathan_namoro:

        "A gente tá namorando sério já faz um tempinho, mas não paramos pra curtir até agora."

    "Vai ser minha chance de ver como ele tá."

    "Vou começar avisando ele ver se ele me libera pra entrar na Blergh!. E daí lá eu vejo a Roxane também."

    scene black with dissolve

    pause 1.0

    scene ape_celular_falando with Dissolve(1.0)

    pause 1.0

    mc "Nathan?"

    n "[mc]! Como tá indo!?"

    if nathan_namoro:

        n "Tava com uma saudades de você."

        mc "E eu não tava? Depois daquele dia no seu apê..."

        n "Nem fala, gostoso. Quer me deixar duro pelo telefone assim?"

        mc "Quer um nude pra ajudar?"

        n "Hmm..."

    if grupo_nathan == 1:

        "Eu tenho que confirmar que ele vai continuar na Blergh!. É o que o Tony quer de mim."

        "Se eu fizer essa boa... talvez eu tenha uma chance de ir pras cabeças."

    mc "Tava querendo te ver aí."

    n "Sério?! Claro! Onde você quer ir?"

    mc "Posso te esperar sair do trabalho."

    n "Hmmm... mas tá querendo falar comigo ou com a Roxane?"

    if not nathan_namoro:

        n "Se for por causa dela eu te ajudo, hein?"

        mc "Ajuda mesmo?"

        n "Brother é pra isso, né?"
    else:


        mc "Haha... claro que não, né, gato?"

    n "Então chega aí hoje. Eu vou ter uma conversa com a Zaza e daí a gente sai fazer alguma coisa."

    mc "A chefe vai tá aí?"

    n "Pois é..."

    "O tom da voz dele tá diferente..."

    menu:
        "Que que foi? Aconteceu alguma coisa?":


            n "N-não! Nada... bom... sei lá."

            n "Quando você tiver aqui a gente se fala."
        "Segura aí.":


            n "Vou te esperar."

    mc "Beleza. Tô chegando já."

    n "Até."

    "Então a Zaza tá lá. A dona da porra toda."

    "Do jeito que ela falou com o Barão e os outros lá, essa mulher tá com moral."

    "Por que a chefe ia dar as caras assim do nada?"

    "E o Nathan? O que tá rolando com ele, hein?"

    mc "Bora descobrir tudo isso."

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    scene n7_passarela with Dissolve(1.0)

    "Lugar chique. De noite então com as luzes acesas... essa Zaza tá cheia da grana."

    play sound som_35_passos

    "Opa... olha quem tá chegando aí."

    scene black with dissolve

    scene n8_img3 with Dissolve(1.0)

    pause 2.0

    ro "Você aqui também, maninho?"

    mc "E aí, [ro]. Como assim 'também'?"

    ro "Deixa pra lá. Eu devia ficar quieta hehe..."

    mc "Hmmm... e você?"

    menu:
        "Você tá linda, hein.":


            ro "E você sempre galanteador."

            if not roxane_livre:

                ro "Sua namorada não vai gostar."

                mc "E se for um namorado?"

                ro "O Nathan?"

                mc "Quem sabe."

                "Verdade... eu disse pra ela que tava namorando da outra vez."
            else:


                ro "Sorte que você é solteiro. Ou seu parceiro já não ia gostar, né."

                "Verdade... eu disse pra ela que não tava namorando da outra vez."

                mc "Sorte mesmo."
        "Com essa chupeta ainda? Coisa feia.":


            ro "Você não gosta de chupeta?"

            mc "Haha... depende da chupeta."

            ro "Para de ser careta, [mc]. Parece um velho."

            mc "Huh..."

    ro "Veio esperar o Nathan de novo?"

    if black_salva > 0:

        "Na verdade eu vim por sua causa... mas não sei se eu devo falar ainda."

        "Talvez o melhor seja eu levar o papo na boa por enquanto."

    mc "Sim. Tenho que falar uns negócio com ele. Mas me fala de você."

    mc "Como tão os treinos? A Zaza continua pegando no teu pé?"

    ro "SEMPRE! Aquela lá é fogo, [mc]."

    mc "Ela parece bem severa mesmo."

    ro "A Zaza é uma mulher diferente. Ela tem esse negócio de lutar pelas garotas."

    ro "Ela quer ver a gente dominando o mundo! Mulheres fortes e poderosas."

    mc "Só podia pegar mais leve."

    ro "Que nada. Ser criticada é ruim, mas depois é bom se a gente tem ouvido pra ouvir."

    mc "Você é uma mulher de personalidade. Deve ter uma boa autoestima."

    mc "Tem gente que já se sente todo doído com crítica."

    ro "Vem cá."

    scene black with dissolve

    scene n8_img4 with Dissolve(1.0)

    pause 2.0

    ro "Eu devo minha vida pra Zaza. Eu quero orgulhar ela."

    if black_salva > 0:

        "Deve a vida pra ela, né? Hmm... será que é disso que o [us] tava falando?"

    mc "Como assim? Ela te salvou de um acidente, sei lá?"

    ro "Para, seu bobo ksks..."

    ro "A Zaza é como uma mãe pra mim. Eu era pequena quando ela me pegou pra criar."

    ro "Teve paciência comigo. Desde pequena eu dava trabalho, sabe? Sempre tive personalidade forte."

    ro "E ela me pegou e me colocou pra trabalhar na empresa dela e me deu uma motivação pra fazer as coisas."

    ro "Pra ser a porra de uma pessoa decente, sabe?"

    menu:
        "Parece que você gosta dela de verdade, [ro].":


            ro "Eu vou fazer tudo pra ela."
        "Mas e se... a Zaza não for uma boa pessoa?":


            ro "Como assim? Do que você tá falando?"

            mc "Nada... eu que tô falando demais agora."

            ro "Hm..."

    "Será que ela imagina que a Zaza tá envolvida com aquelas pessoas?"

    "A Zaza foi outra que nem se mexeu pra ajudar a Diana. Sei lá o quanto ela se preocupa com as mulheres."

    "Acabar com a Zaza vai enfraquecer aquele grupo do prefeito."

    if black_salva > 0:

        "E depois das desgraças que eles fizeram com tanta gente... o certo é dar um jeito neles. Da forma que eu puder."
    else:


        "Eu não quero fazer isso. Eu quero entrar pro grupo."

    ro "[mc]..."

    scene black with dissolve

    scene n8_img5 with Dissolve(1.0)

    pause 2.0

    mc "Q-que que foi?"

    ro "Você... você não tá pensando em causar com a Zaza, né?"

    mc "Eu?"

    if black_salva > 0:

        ro "Eu fiquei sabendo o que aconteceu no Cassino."

        mc "Ouviu?"

        ro "Você tava no rolo todo. Até desafiou o Barão."
    else:


        ro "Eu fiquei sabendo o que aconteceu no Cassino."

        mc "Ouviu?"

        ro "Fiquei feliz que você não causou com eles."

    ro "Não faz nada com minha chefe, tá? Por favor."

    ro "Se você gosta de mim... se você quer que seja feliz, sei lá por que... não fode ela."

    mc "[ro]..."

    if black_salva > 0:

        mc "Você não é daqui, né?"

        ro "Hm?"

        mc "Você disse que a Zaza te pegou criança. Você lembra de onde você veio?"

        ro "Eu era órfã. E vivia aqui na Capital. Outra mulher cuidava de mim."

        ro "Mas eu não quero voltar pra lá. Eu gosto daqui. Eu quero ser modelo. Quero ser alguém."

        mc "Sei..."

        "Será que o [us] sabe disso? Que no fundo ela quer ficar aqui?"

        "É bem diferente do caso da Diana."

        "Mas e agora? O que eu faço? Vou deixar a Zaza por aí por causa da [ro]?"

        "E o Nathan?"

        mc "O Nathan... ele também gosta daqui?"
    else:


        mc "Pode deixar. Pelo contrário. As coisas vão ficar boas pra ela. Você vai ver."

        ro "Tá falando sério?"

        mc "Sim. Eles me mandaram aqui pra resolver um lance com o Nathan."

        ro "Ah!"

    ro "O Nathan... ele não tá normal."

    ro "A chefe tá aqui hoje pra falar com nosso amigo. Por isso que ela veio."

    mc "Ixi... então a coisa tá feia."

    ro "Tá chegando uma data muito especial. Vai ser o dia que a Blergh! vai entrar no mapa da moda."

    ro "Até agora a gente tava só se preparando. Juntando fama, treinando. Mas nosso próximo desfile..."

    ro "Daí, sim, vai ser a hora da verdade. Até a FAUX vai tá aqui pra botar a gente no mapa."

    "FAUX... claro. Não podia ser diferente."

    menu:
        "Por isso que você tá com essa roupa?":


            pass

    ro "Também. Eu vou ter uma tarefa especial no dia. De entreter um pessoal especial."

    mc "Entreter?"

    ro "Eu e minha bocona. Deixa pra lá hehe..."

    mc "Hmm..."

    mc "Então o Nathan tá com a Zaza?"

    ro "Acho que sim. A sala dela é seguindo pra lá."

    mc "Será que eu posso entrar lá?"

    ro "Se você não tem medo de morrer ksks..."

    scene black with dissolve

    scene n8_img6 with Dissolve(1.0)

    pause 2.0

    ro "Agora vou nessa. Tô o dia todo vestida de coelhinha."

    menu:
        "Devia vestir sempre. Você tá muito gata.":


            ro "Você devia olhar mais pra baixo na próxima."

            mc "Q-quê?!"

            ro "Ksks... fofo."
        "A gente se ve, Roxane.":


            pass

    ro "Bem que você podia vir aqui pra festa também. Eu ia gostar."

    mc "Quem sabe... se alguém me convidar."

    ro "Se eu pudesse eu te convidava agora. Mas sou só uma modelo mesmo."

    ro "Mesmo assim vou falar com a Zaza. Talvez eu descole um ingresso pra tu, mano."

    mc "Pô. Valeu mesmo, Rox! Você é pica."

    ro "Você também. Beijinhos, [mc]."

    mc "Vai lá, gata."

    play sound som_35_passos

    scene black with dissolve

    scene n7_passarela with Dissolve(1.0)

    if black_salva > 0:

        "A Rox não parece desesperada pra sair. Não sei o que o [us] quer comigo."

        "Ele quer tirar ela daqui contra a vontade dela? E agora?"

    "Então o Nathan tá estranho mesmo. E agora tá com a Zaza. Ela deve tá tentando fazer a cabeça dele."

    if black_salva == 0:

        "Por isso que o Tony precisa de mim."

        "Eu tenho que fazer a cabeça dele."

        "É minha chance de entrar de uma vez pro grupo."

    "Vou dar uma olhada lá ver o que eu acho."

    "Quem sabe não pego eles conversando?"

    play sound som_35_passos

    scene black with dissolve

    pause

    "???" "Falta muito pouco agora."

    "Aqui... nesta sala."

    scene n8_img7 with Dissolve(1.0)

    pause 2.0

    "???" "Você diria que já conseguiu, Zaza?"

    "Zaza?!"

    za "Com certeza. Com o Nathan e a Roxane, a gente vai conquistar o status que eles querem."

    "E-eita... com quem ela tá falando?"

    "???" "Espero que você lembre quem garantiu isso. Porque a Faux não queria comprar a história dele."

    za "Você se tornou uma mulher e tanto, [j]."

    "[j]!? Ela também tá aqui?!"

    j "Não fale como se você tivesse orgulhosa. Você não se contenta com pouco."

    za "Eu ESTOU orgulhosa. Você cresceu muito."

    j "Eu tive meus exemplos. Terríveis, mas tive."

    za "Espero que esteja falando do velho. Ele, sim, é um exemplo terrível."

    j "O velho tinha seu charme. Agora só virou uma página de um livro antigo."

    za "Ele não tem mais combustível pra queimar?"

    j "Não. O problema é a filhota dele."

    za "Isso é com você. Eu tenho meus próprios problemas."

    j "Nenhuma palavra de sabedoria?"

    za "Tá nostálgica? Você sabe que tudo o que você precisava ouvir eu te disse. Agora é hora de VOCÊ colocar em prática."

    j "Eu vou dar meu jeito. Ele VAI vender a revista."

    za "Excelente. Eu não quero chegar lá sozinha. Aqueles malditos usando as mulheres como bem entendem."

    j "Acha que vai acabar com o machismo do Grupo?"

    "Grupo?! De novo esse termo..."

    za "Sozinha não consigo. Mas eu, você e a Miranda, a cadela do prefeito. Aos poucos vamos conquistar nosso lugar."

    j "Eu tô pouco me fodendo pra isso. EU quero tá lá. Dar as cartas."

    "Agora a conta fecha. Por isso a Zaza tava no Cassino."

    "Ela faz parte do grupo do prefeito. O mesmo grupo que a [j] me falou há TANTO tempo."

    "A Cássia tem contato com eles. Mas ela mesma parece que não faz parte."

    menu:
        "Provavelmente a venda da revista é o ponto-chave pra ela.":


            pass

    if black_salva == 0:

        "Por isso também o Tony quer que eu faça a cabeça do Nathan. Ele também é 'propriedade' deles."
    else:


        "Agora, se a Blergh! é do grupo, então o Nathan também é 'propriedade' deles."

    "Igual a Pri, a Diana e não sei mais quem."

    menu:
        "Preciso dar o fora antes que elas me notem":


            pass
        "Elas ainda não terminaram. Preciso chegar mais perto!":


            $ roxane_ouviu = True

            "Só mais um pouco..."

            scene black with dissolve

            scene n8_sala_close with Dissolve(1.0)

            pause 2.0

            za "Falta pouco agora. Todo nosso esforço vai valer a pena."

            j "Nem me fale isso."

            za "Tá se sentindo mal, é? Ficou mole com o passar do tempo?"

            za "Eu tive que aceitar uma delas. Eu manchei minhas mãos de lama. Contra tudo o que eu acredito."

            za "Pelo menos fiz dela a modelo perfeita. Alguém que vai conquistar o mundo, como nós."

            j "Não acredito que eu tô ouvindo isso. Você foi 'contra o que acredita'?"

            j "EU TIVE QUE DAR MINHA FILHA POR CAUSA DESSES FILHOS DE UMA PUTA!"

            mc "A-ah!"

            za "..."

            j "Nem precisa falar. Eu sei o que você vai dizer."

            za "Se você sabe, então entende que isso ainda vai ser o motivo da sua queda."

            j "Eu deixei ela no passado."

            za "..."

    "Deixa eu dar o fora!"

    play sound som_hit

    scene n8_img8 with vpunch

    pause 2.0

    mc "A-ai!"

    "???" "Parece que você tava escutando o que não devia. E isso vai ter consequências."

    if roxane_ouviu:

        "Eu não devia ter chegado mais perto!"

    mc "A-ah! Não!"

    "???" "Paparazzo mais xereto..."

    "Não!"

    if roxane_ouviu:

        "Por que eu fiquei lá na porta ouvindo?!"

    "???" "Calma. Abre o olho, bobo."

    scene black with dissolve

    scene n8_img10 with Dissolve(1.0)

    pause 2.0

    n "Sou eu."

    mc "UFA! Caramba! Tu quase me matou do coração, cara!"

    n "Quem não deve não teme. Você tava mesmo xeretando, né?"

    mc "A-acho melhor a gente sair daqui antes de eu responder isso."

    n "Hahaha. Melhor mesmo. Bora. E eu tenho um lugar que eu queria ir contigo."

    mc "Onde?"

    n "Vem. Você vai saber no caminho."

    mc "Ok..."

    play sound som_35_passos

    scene black with dissolve

    pause 2.0

    scene hub_bar_fundo cenario with Dissolve(1.0)

    mc "Ah! Aqui..."

    n "Foi aqui que tudo começou, né?"

    mc "Verdade..."

    if nathan_namoro:

        n "Quem diria que a gente ia acabar se apaixonando."

        mc "Você gostoso desse jeito? Achei fácil."

        n "Você sabe elogiar. É um perigo com essa boca."

        mc "Hmm..."

    n "Vamos sentar ali."

    scene black with dissolve

    scene n8_img11 with Dissolve(1.0)

    pause 2.0

    mc "Ufa."

    n "E aí? O que você tava fazendo lá? Coisa de paparazzo?"

    mc "Tava tentanto te achar. A Roxane disse que você tava tomando bronca da Zaza."

    n "Ah... ela foi lá pra isso. Mas daí a [j] apareceu na Blergh! e eu fui chutado da sala."

    mc "Haha... coitado... Essas duas têm uma história, né?"

    n "Então... nunca soube na verdade. Com certeza elas se conhecem. Já vi as duas se falando."

    n "Mas falar que tem uma história. Aí tu que é o paparazzo."

    mc "Pelo que eu ouvi na sala ali, parece que a amizade das duas é de longe."

    menu:

        "Eu queria era namorar, sabe?" if nathan_namoro:

            n "Eu também... Fiquei feliz de saber que você vinha me pegar no trabalho."

            mc "Já tamo nessa fase?"

            n "Deixa eu viver minha fic aqui um pouquinho."

            mc "Bobo..."
        "E aquele lance que você tinha me falado pelo telefone?":


            n "Ah... aquilo..."

    scene black with dissolve

    scene n8_img12 with Dissolve(1.0)

    pause 2.0

    n "Queria tá numa boa contigo agora. Mas tá foda, [mc]."

    n "E o duro que só tenho você pra falar dessas coisas."

    mc "Nem a Roxane pode ajudar?"

    n "Não... ela não entende. Ela é muito puxa-saco da Zaza... mandando a real."

    mc "Foi o que eu senti falando com ela hoje. Ela gosta de ser modelo, né?"

    n "Esse é meu problema no fim. Eu também gosto."

    mc "Trabalhar com o que a gente ama é uma sorte que pouca gente tem o luxo, viu."

    n "Eu sei... não vou reclamar da oportunidade. Mas você entende as condições, né?"

    mc "Tudo o que você teve que fazer pra ter essa chance? Mentir pra mim!"

    n "Droga... isso ainda doi muito."

    menu:
        "A gente já superou isso da outra vez.":


            n "Valeu... mesmo assim..."
        "Você podia ter confiado mais em mim, né?":


            $ n8_convenceu += 1

            n "Eu sei! De todas as pessoas! Você é que eu devia ter confiado mais!"

            n "Quero ouvir mais você nas coisas agora. Quero confiar mais em você."

            mc "Muito bom."

    n "Eu não sou igual a Roxane. Que aceita todas essas condições e foca no que ela quer."

    scene black with dissolve

    scene n8_img13 with Dissolve(1.0)

    mc "Quer dizer que tu não é igual a Cássia?"

    n "Pensando bem... a Cássia e a Roxane até que são meio parecidas."

    mc "A Roxane também é uma manipuladora e descarada que ainda por cima usa o sexo pra conseguir o que quer?"

    n "Haha... não... não acho que a Roxane tá nesse nível da Cássia."

    n "Mas ela tem força pra aguentar. Não dá pra negar que a Cássia é obstinada. Ela faz o que tem que fazer."

    menu:
        "Tem o dedo da Zaza nisso aí.":


            n "Hmm... por isso a semelhança?"

            mc "Pra mim, a Zaza que ensinou essas duas sobre a vida."

            n "Mas a Zaza é bem diferente da Cássia. A Zaza é bem mais na dela."

            mc "Só que também tá disposta a fazer o que tem que fazer."

    scene black with dissolve

    scene n8_img12 with Dissolve(1.0)

    n "Eu vim aqui pra este país com uma razão. Um objetivo."

    n "E agora quero jogar tudo fora porque sou fraco."

    scene black with dissolve

    scene n8_img13 with Dissolve(1.0)

    mc "Ou talvez porque você tem um coração."

    mc "Eu conheci pessoas que seguiram os dois caminhos."

    mc "A Priscila, a modelo teen."

    n "Tô ligado quem é ela. Acho que todo mundo já ouviu falar da Pri."

    mc "Pois é. Ela sofreu a mesma coisa que você. Muito triste mesmo. E no fim ela resolveu continuar trabalhando pra eles."

    mc "Agora a Diana, até o fim, ela quis sair fora. Totalmente o contrário."

    scene black with dissolve

    scene n8_img12 with Dissolve(1.0)

    n "E eu? O que eu vou escolher?"

    if black_salva == 0:

        "Se eu quero ganhar pontos com o Tony e o Grupo, eu preciso convencer o Nathan a continuar."
    else:


        "Hoje eu confirmei que a Blergh! faz parte do portfólio do prefeito, igual a produtora do Gustav, o Cassino, o NBC."

        "Então se eu quero diminuir a influência do Grupo, fazer eles perderem o Nathan e possivelmente a Blergh! vai ser um golpe e tanto."

    "Ou eu posso parar de ser um egocêntrico manipulador de merda e só ajudar o Nathan naquilo que ele quer. É uma escolha também, né?"

    p rindo "O destino do Nathan está nas suas mãos."

    p "Se você vai ajudar ele a encontrar a verdade dele ou usar ele pros seus próprios objetivos... igual ele fez contigo."

    p "As duas opções são válidas e vão mudar o resultado da sua história. Talvez não só com o Nathan, mas com todo mundo."

    p "Você não vai saber para que lado uma escolha está influenciando. Mas tudo está sendo levado em consideração. Então fique de olho nos detalhes."

    p "Inclusive escolhas que você FEZ ANTERIORMENTE neste encontro já estão contando também tehee..."

    menu:
        "Só você pode tomar essa decisão.":


            scene black with dissolve

            scene n8_img15 with Dissolve(1.0)

            n "Eu sei... tá nas minhas mãos agora."
        "Eu vou te ajudar nessa. Pode confiar em mim.":


            $ n8_convenceu += 1

            scene black with dissolve

            scene n8_img15 with Dissolve(1.0)

            n "Não é pedir demais pra você? Ainda mais depois de tudo o que eu fiz?"

    n "Todas as mentiras que eu contei pra você e pros outros. Todas as merdas que eu tive que fazer."

    n "Eu não sou mais a mesma pessoa que chegou no país. Eu praticamente deixei todos meus objetivos pra trás."

    n "E eu não sei se eu quero continuar assim."

    menu:
        "Você passou pelo pior. Agora colha os frutos. Seja um modelo famoso.":


            $ n8_convenceu += 1

            n "Você acha que eu mereço? Mesmo que eu tenha conseguido isso enganando os outros?"

            mc "O que tá feito, tá feito. Agora é hora de aproveitar."

            mc "Faz o que eu tô falando."
        "Você ainda pode voltar às origens. Não abandonar o que você veio fazer.":


            n "Isso é... mas e se eu não quero mais seguir esse caminho?"

            mc "Não sei o que te falar. Você precisa pensar por você."

    n "Eu ainda poderia voltar pro meu país. Deixar tudo pra trás."

    mc "Essa é uma opção mesmo?"

    n "Sim. Minha família veio pra cá cedo, mas a gente nunca perdeu contato com o povo de lá."

    n "Eu podia só jogar tudo pra cima e ter uma vida boa lá."

    if nathan_namoro:

        $ n8_convenceu += 1

        scene black with dissolve

        scene n8_img14 with Dissolve(1.0)

        n "Com meu namorado. Seria incrível."

        mc "A gente ia fugir de tudo e viver assistindo Netflix e se pegando?"

        n "O que você acha? Bem abraçadinhos porque lá é um frio da porra."

        mc "Hmm... não é ruim, não."
    else:


        scene black with dissolve

        scene n8_img16 with Dissolve(1.0)

        n "Tem umas mulheres MUITO gostosas lá. A gente podia arranjar um pro outro."

        mc "Tá doido? Eu ia ser o amigo feio. Sai fora."

        n "Hahaha! Para de marra, [mc]. Vai sobrar pra nós dois."

        mc "Sei lá, viu..."

    n "Você é demais."

    mc "Mas é sério isso? Você tem essa possibilidade?"

    n "Ter eu tenho. Só precisaria da grana."

    mc "Tu é um modelo famoso agora! Tem grana, não tem?"

    n "Tenho nada."

    n "Minha bolada vai chegar depois do evento da Blergh!. O evento que vai lançar a gente pro mundo."

    mc "Hmm... a Roxane falou disso."

    n "A Zaza tá contando demais com a gente pra isso. Todo o lance de ser deportado foi por causa disso."

    n "Ninguém colocava a gente na mídia. Então a Cássia veio com a ideia de criar uma pauta."

    menu:
        "E pelo jeito deu certo. Agora você tá na Faux, na revista, em tudo que é canal.":


            pass

    n "Por isso a hora da festa. Precisa ser agora enquanto as pessoas ainda lembram quem sou eu."

    n "Vai ser a maior festa que essa cidade já viu. Eles tão investindo uma bolada na Blergh! pra dar esse start. E depois capitalizar em cima."

    "O Grupo não perde tempo mesmo... eles tão investindo pesado."

    mc "Se em uma hipótese a gente for dar fora mesmo, não pode ser antes da festa. Ia chamar muita atenção."

    n "Com certeza. Ainda mais agora que tá tão perto e a gente tá ensaiando pro grande dia."

    mc "Então precisa ser logo depois ou até DURANTE o evento. Pra eles só perceberem quando for tarde demais."

    n "A gente só precisaria da bufunfa pra pagar por toda a viagem e pra começar nossa vida lá."

    mc "Eu não tenho o suficiente pra pagar uma viagem pra dois, alugar casa, pagar pelas coisas."

    n "Muito menos eu. Ainda mais se eu der um golpe na Zaza."

    menu:
        "Golpe na Zaza? Hmm... Imagina se a gente pegasse o dinheiro que vão dar pra Blergh!?":


            pass

    if nathan_namoro:

        scene black with dissolve

        scene n8_img16 with Dissolve(1.0)

    n "I-imagina?! É uma bolada que provavelmente é de milhões, [mc]!"

    mc "Pena que não tem como a gente pegar essa grana."

    n "Só se a gente conseguisse a conta do banco dela. E transferir tudo pra gente."

    mc "Ideia viajada demais... melhor nem perder tempo com isso. Vamos ter dar outro jeito."

    n "É... Mas se a gente tivesse a grana... a gente podia jogar tudo pra cima e tentar a vida lá. Imagina ricos no exterior?!"

    mc "Que loucura, Nathan... mas milionários curtindo a vida viajando, não parece uma ideia tão ruim."

    n "Ruim? Tá doido, maluco?! É perfeita! O problema é que é impossível haha..."

    if nathan_namoro:

        "Imagina viver na riqueza só eu e o Nathan? Namorando e gastando?"

        "Eu e ele numa vida de luxo..."
    else:


        "Imaginar viver na riqueza? Eu podia até chamar ela pra ir comigo..."

        "Eu e {b}minha escolhida vivendo uma vida de luxo{/b}. Sem perigos, sem dor de cabeça. Os dois salvos."

    "Eu ia parar de apanhar adoidado de todo lado e começar realmente a curtir a vida."

    "Inclusive parar de meter as pessoas que gostam de mim em perigo. Tipo a Sofia."

    menu:
        "Nathan... a gente precisa dar um jeito de conseguir essa grana.":


            pass
        "Esquece isso. Vamos parar de sonhar e focar na realidade.":


            $ n8_convenceu += 1

    scene n8_img17 with hpunch

    gar "Com a licença dos nobres senhores."

    mc "A-aleluia, Fabrício! A gente quer beber alguma coisa."

    n "Olha o doido aí."

    gar "Se me concedem a oportunidade de impertinente intromissão, este servo deseja dirigir-vos singelas palavras."

    n "Você o quê?"

    mc "Acho que ele quer dar algum pitaco não solicitado."

    gar "Ora se o pomposo senhor [mc] não destila razão."

    mc "Você podia, por favor, tentar falar um pouco mais como outros seres humanos?"

    gar "Este mero e prolixo mortal tentará."

    n "Bebida que é bom cadê?"

    gar "Veja, senhor [n]. Nossa furtífera amizade se estende por tempo incontável. E não pude, de certa forma inconveniente, evitar de notar seus remarcos."

    gar "Sair assim desta amável terra, não seria, por justos motivos que sejam, deveras inconveniente para o quadro geral da sua posição?"

    menu:
        "Mas continuar vivendo aqui assim? Todo depressivo? Duvidando de tudo?":


            pass

    scene black with dissolve

    scene n8_img18 with Dissolve(1.0)

    pause 2.0

    gar "Sonhos são, por natureza, jornadas demasiadamente espinhosas. Há de se esperar atribulações."

    n "Tô pensando mais em vazar mesmo... acho que seria o melhor."

    gar "Se o senhor deseja... como fará com as necessidades materiais da empreitada?"

    mc "Essa é a questão. A Zaza não é boba. Ela não vai pagar o Nathan pra correr da capital."

    gar "Inteligência sem sabedoria transmuta em faca de dois gumes."

    n "A Zaza confia demais no taco dela. Naquela cabeça, ninguém melhor que ela pra cuidar de tudo."

    gar "Não poderia ser essa a faca de Brutus?"

    n "Não sei. Mas essa conversa perdeu o rumo agora com o [gar] aqui."

    gar "Perdoe minha insolência, nobre companheiro [n]. Retiro-me se é pelo bem geral."

    scene black with dissolve

    scene n8_img19 with Dissolve(1.0)

    pause 2.0

    n "Esse cara..."

    mc "Baita figura, hein. Mas normalmente ele fala coisa com coisa, viu. Mesmo sendo difícil de entender."

    n "Ignora esse maluco. Bora voltar no que a gente tava falando. Essa conversa me deu um novo gás, [mc]."

    mc "Que bom, cara... o que você tá pensando em fazer então?"

    n "Não sei. Não tenho certeza. Só que agora pelo menos eu posso pensar e decidir."

    n "Você me falou umas coisas hoje que tenho que refletir aqui. Preciso de um tempinho pra pensar."

    mc "Sei..."

    n "Imagina abandonar tudo e dar o fora? Ou só aceitar que as coisas são difíceis mesmo e realizar meu sonho profissional?"

    mc "Tá aí o que você tem que decidir."

    n "E você também. Já imaginou você deixar essa revista e essa doideira toda pra trás e a gente só vai pra outro país curtir?"

    if nathan_namoro:

        scene black with dissolve

        scene n8_img20 with Dissolve(1.0)

        pause 2.0

        n "Só nós dois. Namorando, se curtindo. Ia ser o sonho, fala aí."

        mc "Curtindo contigo? Bora."
    else:


        n "Várias gatas estrangeiras pra você aproveitar."

        mc "Elas vêm tudo pra falar contigo, isso sim."

        n "E eu encaminho todas pra tu. Você só aproveit."

        mc "Não parece tão ruim mesmo..."

    n "Pensa direito no que tu vai querer e bora pensar num plano."

    menu:
        "Mesmo que eu não vá, eu vou te tirar dessa. Pode ter certeza.":


            pass
        "Isso é loucura. Não desista do seu sonho assim. Falta tão pouco agora.":


            pass

    if nathan_namoro:

        n "A gente se fala, gato."

        mc "E quando vai rolar mais carinho, hein?"

        mc "Eu quero foder com você de novo, viu."

        n "Outra razão pra gente só abandonar tudo e ir se comer em paz."

        mc "Hmm..."

        n "Gostoso."
    else:


        n "Até mais, cara."

    mc "Até a próxima, [n]. Fica de olho."

    scene black with dissolve

    scene pub booth with Dissolve(1.0)

    "Caraca... que dia..."

    "Escutar a conversa da Zaza com a Cássia e agora o Nathan."

    "Tirando o rolo do Black Cash com a Roxane."

    "Imagina escapar de tudo e ir só curtir adoidado com o Nathan e muita grana?"

    mc "Mas e essa grana? Como a gente consegue?"

    scene n8_img21 with hpunch

    pause 2.0

    gar "Meretíssimo excelentíssimo senhor [mc]."

    mc "O-oi?"

    gar "Sei que é de grande inconveniência meu indesejado retorno, mas este servo necessita lhe revelar certas preocupações."

    mc "Que que foi, [gar]?"

    gar "Nosso inestimável companheiro Nathan aportou nesta abençoada terra com uma missão deveras clara."

    gar "Entretanto, sombras de nuvens carregadas de melancolia parecem ter anuviado a mente de nosso herói."

    mc "E se ele não quiser mais ser modelo? As pessoas mudam."

    gar "Mudam, sim, mudança e evolução são o DNA da Mãe-Terra. No entanto, planos podem mudar a vida de muitos."

    gar "Seus planos, bem-vindos por este servo obviamente, junto ao nosso parceiro mútuo, podem influenciar forças das mais grandiosas."

    menu:
        "O Nathan tem que pensar nele. E eu em mim. O que for melhor pra nós.":


            pass
        "Entendi... talvez ele mudar tudo em cima da hora pode prejudicar a Zaza, a Roxane, a Cássia...":


            gar "Pois não. E peças de um tabuleiro de proporções desconhecidas."

            mc "Não sei, [gar]... pensar nos outros numa hora dessas?"

            gar "É imprescindível pensar, nobre [mc]."

    gar "Determinante também meu companheiro fofoqueiro profissional avaliar as possibilidades também."

    gar "Vida cheia de prazeres o aguarda longe do olho do furacão. Disso não há discórdia."

    gar "Todavia, o furacão não cessa por estarmos distantes. Seu lastro de distruição continuará se nada for feito."

    mc "Eu nem sei mais do que você tá falando."

    gar "Aguardarei ansiosamente o futuro dos nobres amigos. Adelante, guerreiros!"

    mc "Falou..."

    "Deixa eu passar na redação."

    scene black with dissolve

    scene n8_img27 with Dissolve(1.0)

    pause 2.0

    "Caraca..."

    "Black Cash, Roxane, Zaza e Cássia, Nathan, Fabrício. Que dia, hein."

    if grupo_nathan == 1:

        "Minha tarefa era fazer a cabeça do Nathan pra continuar trabalhando na Blergh!."

        "Mas não sei se o que eu disse vai fazer a cabeça dele."

        "O Tony tá contando comigo. E se eu quero uma chance de sentar na ponta da mesa, isso tem que dar certo."

        "Como eu posso ter certeza que o Nathan vai fazer o que eu quero?"
    else:


        "Eu não sei se o que eu falei pro Nathan vai ajudar ele a dar o fora ou não."

        "E sobre a Roxane e o Black Cash... preciso falar com ele."

    "O que eu faço da minha vida agora?"

    "Tem tanta coisa em jogo aqui que até difícil de colocar tudo na balança agora."

    "???" "Pombinho."

    mc "C-cássia?"

    "Afe... será que ela me viu lá?"

    j "Vem comigo."

    mc "Opa."

    "Tô fodido."

    scene black with dissolve

    scene so5_img1 with Dissolve(1.0)



    j "Vai tomar um café, garota."

    "Renata" "S-sim, senhora."

    play sound som_35_passos

    scene black with dissolve

    scene n8_img22 with Dissolve(1.0)

    pause 2.0

    j "Olha, meu querido. Sua chefe tem um servicinho pra você."

    menu:
        "Minha única chefe é a Sofia. E o velho, claro.":


            j "Blá blá... vocês se merecem."
        "Que foi, gostosa? A gente vai se ajudar?":


            j "Você tá mais saidinho ultimamente."

            mc "Quando eu falo com uma delícia."

            j "Tô gostando desse pombinho mais safado."

    j "Lembra que eu te falei de um grupo exclusivo? Faz bastante tempo."

    j "Um grupo seleto de pessoas. Com um poder maior do que a gente podia imaginar?"

    mc "Acho que eu lembro algo mais ou menos assim."

    if black_salva == 0:

        "Se ela soubesse que eu tive uma reunião com o Tony e o Barão, ia pagar um pau danado."

        "Eu realmente evoluí bastante nesse tempo na Capital..."

        "Até ontem eu não sabia merda nenhuma dessas coisas. A Cássia parecia a rainha."

        "Hoje eu tô em reunião com quem ela lambe a bota e ela nem faz ideia."
    else:


        "Claro que eu lembro! Eles tão fodendo todo mundo na cidade."

    j "Então... o que você acha de fazer uma coisinha por eles? E por mim, claro."

    mc "Fazer o quê?"

    j "Parece que o docinho do Nathan não tá muito bem da cabeça atualmente."

    j "Lembra quando você foi no bar falar pra ele publicar a pauta pra mim?"

    mc "A armação que vocês fizeram, você quer dizer..."

    j "Tudo era parte de algo maior, pombinho. Não seja tão sensível. Esse mundo é de quem tem casca grossa."

    mc "Que seja. O que você quer que eu fale pro Nathan?"

    j "Só quero que você garanta que ele vai continuar na Blergh!. Ele nem deveria tá em dúvida. É o que ele sempre quis."

    j "Você podia fazer essa pela sua mamãe aqui? Prometo que você vai ser muito bem recompensado."

    if grupo_nathan == 1:

        "Não creio... isso é justamente o que o Tony queria que eu fizesse e eu já aceitei."
    else:


        "Como é?! Fazer a cabeça dele pra continuar na Blergh!? Tipo... enganar ele?"

        "Assim... seria a mesma coisa que ele e a Cássia fizeram comigo. Por um lado, eu taria dando o troco."

        "Mas ele já se desculpou. E tem muito mais coisa que isso."

        if nathan_namoro:

            "A gente tá até namorando."

        "É esse tipo de relação que eu quero ter com ele?"

    scene black with dissolve

    scene n8_img23 with Dissolve(1.0)

    pause 2.0

    "Tá na hora de eu definir isso."

    "Tá na graça do grupo ou não? Me juntar a eles e garantir que eu vou tá do lado dos vencedores."

    "Ou ficar no lado que provavelmente vai se foder e ser pé rapado pra vida inteira?"

    "Um lado é o melhor pra mim. Mas o outro é o que a gente aprende que é o certo."

    "E tem o Nathan ainda por cima. Eu taria manipulando ele se eu aceitasse."

    "Apesar que... eu posso falar algo pra ela agora e TENTAR MUDAR isso depois. Tipo, enganar a Cássia."

    menu:

        "Tá brincando? Essa já é minha missão." if grupo_nathan == 1:

            $ grupo_nathan = 3

            j "Como assim?"

            mc "O Tony me passou essa missão diretamente. E eu vou cumprir."

            j "Não acredito..."

            mc "O mundo dá voltas."

            j "Quem diria..."

            j "Então parece que nós dois vamos nos ajudar nessa."

            mc "Quem sabe. Você pode começar me explicando uma coisa."
        "Eu faço a cabeça dele. Pode contar comigo. Mas vou querer minha recompensa.":


            $ grupo_nathan = 2

            j "Perfeito. Você sabe como agradar sua chefe."

            "Eu vou entrar nessa só pra trepar com a Cássia mesmo? Parece uma boa hehe..."

            j "Então parece que nós dois vamos nos ajudar nessa."

            mc "Quem sabe. Você pode começar me explicando uma coisa."

            mc "Mas depois vou querer um pedaço seu."

            j "Vamos ver se você vai deixar sua mandante feliz. E o que você quer saber?"
        "Me tira dessa. Eu não quero saber de grupo. E nem de você.":


            j "Você tá perdendo uma chance enorme."

            mc "Não quero esse tipo de chance."

            j "Vamos deixar essa porta aberta. Quem sabe na hora as coisas acontecem de outra forma."

            mc "Muito difícil. Quase impossível."

            j "Você não quer nada de mim? Não me quer?"

            mc "Eu... me responde uma coisa."

    mc "O Nathan falou que a Blergh! tá recebendo um investimento pesado."

    j "É uma bolada que vai molhar a mão dele também. Se ele for um bom garoto."

    mc "É muita coisa, Cássia?"

    j "Não sei, pombinho. Quem sabe é a dona da Blergh!. Vai cair tudo na mão dela, em dinheiro vivo."

    mc "Dinheiro vivo!?"

    j "Por que eu abro minha boca com esses garotos inocentes? Não vai sair falando por aí uma coisa dessas."

    menu:
        "Eu prometo. Você tá falando sério? Dinheiro vivo?":


            pass

    scene black with dissolve

    scene n8_img24 with Dissolve(1.0)

    pause 2.0

    j "Se você quer fazer parte das grandes ligas, tem que aprender que nem tudo pode ser feito por cima da mesa."

    mc "O-opa..."

    j "Tem coisa que só por debaixo do pano, entendeu? Sem lastro."

    j "O Nathan vai receber assim também provavelmente. Mas pode avisar ele que a parte dele a chefe dele vai entregar."

    mc "Entendi..."

    "Dinheiro vivo? Então quer dizer que toda a grana que a Zaza vai receber do grupo vai ser em notas?"

    "Será que ele vai entregar no dia do evento?"

    "Talvez antes do dia do evento... pra Zaza poder pagar por tudo."

    "O Nathan falou que é uma festa que a capital nunca viu. A Zaza deve usar esse dinheiro aí."

    j "Pombinho, para de pensar e olha pra mim."

    menu:
        "Olhar pra 'ela'":


            scene black with dissolve

            scene n8_img25 with Dissolve(1.0)

            "Caraca... esses peitões deliciosos... vontade de meter a boca, viu..."
        "Tô bem assim.":


            pass

    j "Essa vai ser a participação mais importante da sua vida, entendeu?"

    j "Você tem a chance de tá do lado do time vencedor. Não jogue fora a oportunidade da sua vida, ok?"

    mc "Beleza... vou ver o que dá pra fazer."

    j "Eu vou tá na festa. Vou ver se consigo um ingresso pra você também. Se você fizer um bom trabalho."

    j "Quem sabe a gente não aproveita a noite cheia de bebida pra se divertir."

    mc "Quer se divertir comigo lá?"

    j "Se não tiver ninguém mais interessante."

    "Essa mulher..."

    mc "Vou nessa."

    j "Até mais, meu bem."

    play sound som_35_passos

    scene black with dissolve

    scene trabalho geral with Dissolve(1.0)

    "Então o grupo tá investindo na Blergh! com diheiro vivo pra esconder a transação."

    "Será que é dinheiro ilegal? Por que eles teriam que fazer isso?"

    "Mas isso abre uma janela do caramba! Onde que a Zaza tá guardando essa grana?"

    "ESPERA! Aquilo que o Fabrício falou no bar!"

    scene black with dissolve

    scene n8_fab with Dissolve(1.0)

    pause 2.0

    mc "A Zaza não é boba. Ela não vai pagar o Nathan pra correr da capital."

    gar "Inteligência sem sabedoria transmuta em faca de dois gumes."

    n "A Zaza confia demais no taco dela. Naquela cabeça, ninguém melhor que ela pra cuidar de tudo."

    gar "Não poderia ser essa a faca de Brutus?"

    mc "Porra!!!"

    "Será que tá lá?! Com ela?! Ela confia tanto no taco dela que deixou a grana por perto!"

    mc "O maldito do Fabrício pode ter razão! O fato da Zaza confiar demais no taco dela pode ser justamente o erro dela."

    "???" "Que gritaria é essa?"

    scene black with dissolve

    scene n8_img26 with Dissolve(1.0)

    pause 2.0

    mc "E-epa! Só tava lembrando de um negócio aqui!"

    w "Não perturbe o trabalho dos outros."

    mc "D-desculpa, chefinha!"

    w "'Chefinha'? Você sabe que essa é uma forma pejorativa de me chamarem, né?"

    mc "Desculpa de novo..."

    w "Enfim. O Ronaldo me trouxe uma pauta. Um evento da Blergh! que parece que vai balançar a cidade."

    menu:
        "Tô sabendo.":


            pass

    w "Se tá sabendo por que não me contou?!"

    mc "Eu ainda tava apurando. Eu sei que o Nathan e a Roxane, os principais modelos da empresa, vão desfilar."

    mc "E é o evento que vai lançar a marca deles mundialmente. Coisa grande mesmo."

    w "Tá sabendo demais... Hmf..."

    w "Enfim, parece que ninguém conseguiu um ingresso. E eles tão fechados com a Faux."

    "Faux... que surpresa."

    w "Você consegue arranjar um ingresso? Você é amigo desse modelo Nathan, não é?"

    mc "Você pode falar com a Cássia. Acho que ela tem fontes lá."

    w "A Cássia? Hmm... eu não quero ter que falar com ela. Mas se é o único jeito... eu falo."

    w "Mas se você descobrir alguma coisa, me avise. Um jornalista tem que saber usar seus contatos."

    mc "Tá bom. Vou dar uma olhada nisso."

    w "Se a gente conseguisse uma bomba sobre a Blergh! na frente da Faux... isso ajudaria bastante."

    menu:
        "Ajudaria com o quê?":


            pass

    w "Com a venda da revista, né? Os donos vão receber uma proposta logo logo."

    menu:
        "A Faux que vai comprar. Será que é tão ruim, assim?":


            w "Claro que seria... digo... nem sei."

            w "O Luca é meio pragmático demais... se é que você me entende. Não acho isso certo."
        "A gente tem que parar isso de qualquer jeito!":


            w "Né?! Por isso a gente precisa dessa bomba!"

            w "Vamos ter que mostrar pros donos que a gente pode fazer melhor que a Faux, mesmo sendo menores."

    w "Consiga esse ingresso. E me mande uma bomba sobre eles, [mc]!"

    w "Tô contando com seu esforço."

    w "Ei! Você! Vou te mostrar quantos erros de português tem no seu texto!"

    "Repórter" "A-agora não posso!"

    w "Volte aqui!"

    scene black with dissolve

    scene n8_img27 with Dissolve(1.0)

    "Uma bomba sobre a Blergh!... será que a Sofia tem noção de com quem ela tá mexendo?"

    "Se eu descobrir algo sobre a Blergh!... será que é seguro eu mandar pra ela?"

    "Todo mundo falando dessa festa. E eu não consegui um ingresso ainda."

    "Fazia tempo que não me metia num buraco grande desses. [us] e a Roxane, Nathan, Cássia e a Zaza, a Sofia e uma bolada milionária."

    "A aposta é grande, mas a recompensa pode ser imensa também se eu der os passos certos."

    "Mesmo que eu decida não sair da ilha. Talvez eu consiga uma {b}recompensa em dinheiro{/b} que pode mudar minha vida aqui."

    "Ok... considerando tudo isso. O que eu faço agora?"

    if black_salva > 0:

        "Primeiro de tudo eu tenho que conversar com o mano Cash. Ele tá dependendo de mim sobre a Roxane."

        "Ele precisa entender que a Roxane não tá afim de sair de lá."

        "E se eu foder a Blergh! eu vou tá ferrando ela também. Então é outra que eu tenho que pensar."

        if not nathan_namoro:

            "Se eu quiser algo com ela... hmm... será que se eu fizer a boa e não estragar o lance da Blergh! rola alguma coisa entre a gente?"

            "E-eu podia pensar nisso... a Roxane é uma garota fenomenal e vai virar uma estrela mundial logo logo. Rica e famosa."
    else:


        "Acho que vou começar pelo Distrito. Dando uma olhada no Black Cash."

        "Ele quer minha ajuda com a Roxane. Mas ela não quer sair de lá. Só que é uma chance de entrar na roda dos mandantes."

        "Porque se ele vai me colocar no Grupo igual ele tava insinuando... ela se ferrar é um preço bem pequeno pra mim."

        "Mas a relação dele com os italianos tá bem estranha. Melhor eu ver o que tá rolando."

    mc "Deixa eu falar com ele {b}lá no Distrito{/b}."

    if xiang_escape >= 5 and not xiang_fim:

        p "A entrada no Distrito está liberada para você novamente."

        p "Vê se consegue alguma delícia lá para mim também. Digo, para você."

    jump call_cidade

    label n8_distrito:



        show mc bdsm_blackcash with Dissolve(1.0)

        us "[mc]. E aí? Novidades, amigo? Da nossa operação de livrar a mana daquele vespeiro?"

        mc "Sim. Eu falei com ela. Só que não tem nada a ver com o caso da Diana."

        us "Como assim?"

        menu:
            "A Roxane não quer sair de lá. Ela gosta da Verônica Zaza e da Blergh!.":


                pass

        us "Que garota idiota! Eles entraram na cabeça dela! Só pode ser isso!"

        mc "A Diana odiava o Cassino. Mas a Roxane, não."

        scene black with dissolve

        show n8_img40 with Dissolve(1.0)

        us "Cara... esquece isso. Ela tem que tá com a família dela."

        mc "Esquecer o que ela quer fazer? Ela é adulta, [us]!"

        us "Olha aqui. Me escuta. Quando ela tiver longe de lá, ela vai entender. Vai ver os irmãos dela."

        mc "Não vou tirar ela de lá à força. Não faz sentido."

        us "Tem razão... se ela não quer sair de lá..."

        mc "Pronto. Você entendeu."

        us "O único jeito vai ter que ser acabar com a Blergh!. Sem essa carreira de modelo, ela vai ter que tomar o rumo dela."

        mc "Você vai destruir o sonho dela só pra ela voltar?"

        us "Ela é uma escrava deles, brother! Você não entende!?"

        menu:
            "Entendi. Concordo contigo. Vamos salvar ela do Grupo.":


                us "Boa, porra!"

                mc "Mas como eu faço isso? Como eu acabo com a Blergh!? Eu sou só um paparazzo. Teria que ser contigo."
            "Não concordo. A vida é dela, cara. Deixa ela ser feliz.":


                us "Mano... é tipo lavagem cerebral, entende?"

                us "Ela não tá no juízo perfeito dela."

                mc "Ok... calma... vamos deixar isso em aberto por agora."

                mc "Agora pensa comigo."

                mc "Se eu fosse fazer isso, como a gente acabaria com a Blergh!? Eu sou só um paparazzo. Teria que ser contigo."

        us "'Só um paparazzo'? Você ainda não vê toda a marra que tu tem, mano."

        mc "Minha arma são as pautas. Se eu tivesse algo da Blergh!..."

        mc "Mas até a grana que pode tá suja eles tão tomando cuidado."

        us "E a polícia tá com eles ainda. Nem dá pra tentar arrumar uma investigação."

        mc "Isso que eu tô falando. Precisou de um escândalo enorme gravado pro Barão cair."

        us "Heh... mano, mano... tu acha que eu não tenho nada? Confia no irmão aqui, bro!"

        us "Quando eu falei que eles pegaram a Rox da gente. Eles literalmente fizeram isso."

        scene black with dissolve

        scene n8_img29 with Dissolve(1.0)

        nora "Muito bem, meu filho. É isso mesmo."

        mc "Madame Nora..."

        nora "Eles pegaram nossa filha de nós. E nós temos uma prova."

        mc "Prova?! Que prova?"

        nora "Os carcamanos são lisos como aquele cabelinho penteado horrível deles."

        nora "Mas nós sabemos onde eles guardam as provas que vão foder aquele narizinho empinado deles."

        mc "Ok... mas cadê a prova?"

        nora "Pra cada acordo eles guardam uma cópia do contrato com cada parte. E uma terceira cópia fica protegida no banco."

        nora "A chefe da lojinha de roupa tem uma cópia. Eu tenho certeza."

        mc "O contrato da Roxane tá com a Zaza?"

        us "Agora você entendeu. É só você conseguir colocar a mão nesse contrato e botar a boca no trombone."

        menu:
            "É possível que o contrato esteja na sala da Zaza. Ela não deixa ninguém lá.":


                pass

        nora "Garoto esperto."

        us "Sua revista é a única que eles ainda não engarfaram, brother."

        if black_salva > 0:

            nora "Eu te dei o que você queria. Que você pediu pro meu filho aqui lá no hospital."

            nora "Agora nós precisamos da sua ajuda."

        us "Faz essa pra gente, [mc]. Nós vamos te ajudar a derrubar esses putos que fodem a capital e dominam tua ilha."

        nora "Os malditos italianos estão no poder há tempo demais."

        nora "Os Donatello fazem o que bem entendem por décadas. Tá na hora de termos pessoas melhores no comando."

        "Caraca... isso tá parecendo... uma briga do Distrito com o Grupo!"

        "E eles querem me colocar no meio dessa merda?! Merda fedida pra caralho ainda!"

        "Que sinuca de bico que eu entrei, hein..."

        if black_salva > 0:

            "Eu sobrevivi ao Cassino com um pé na cova. Foi muita sorte o Tony não ter me passado lá no ponto de ônibus."

            "Se eu aprontar de novo... é certeza que eu vou de arrasta pra cima."
        else:


            "O Tony e o prefeito vão adorar saber o que o Distrito pensa deles."

            "Parece que tem alguém querendo mais poder do que lhe cabe."

            "Eu vou continuar do lado dos italianos? Ou pego minha vaga nesse triângulo de poder pelo Distrito?"

        "Ou eu me fodo com um ou com o outro. Eles não vai aceitar meio termo agora."

        "Se eu disser que vou fazer agora... pra ficar bonito com o Distrito, eu vou ter que cumprir se eu colocar as mãos nesse contrato."

        "O que eu falo?"

        menu:
            "Ok. Eu vou tirar essa foto e denunciar a Blergh!.":


                $ blergh_foto = True

                scene black with dissolve

                scene n8_img9 with Dissolve(1.0)

                nora "Esse é nosso garoto. Tá vendo, filho?!"

                us "Porra, mano! Valeu!"

                mc "O Grupo merece. Por tudo o que eles fizeram."

                nora "A cidade vai ser um lugar melhor graças a você."

                us "E o Distrito vai ser um amigo muito importante pra tu no final."

                mc "Essa seria uma boa... principalmente depois de eu denunciar aqueles malditos."

                us "A gente vai garantir tua proteção, cara. Confia em mim."

                nora "Isso aí. O Montanha bate de frente com o gigante deles."

                menu:
                    "Tô louco pra ver esse duelo. Mas espero que nunca aconteça.":


                        pass

                us "Haha! Demorou."

                mc "Vou indo nessa, gente. Tenho que dar um jeito de entrar naquele evento."

                nora "Se esforça, garoto. Muita gente depende de você."

                us "Vai lá, herói."
            "Não posso entrar nessa briga de vocês. É demais pra mim.":


                nora "Que decepção. Você não passa de outro carcamano."

                us "Foda, cara. Pensei que a gente podia contar contigo."

                mc "Não tô falando que tô do lado deles. Só é briga de cachorro grande demais."

                nora "É fácil vir com palavras. O duro é ser amigo de verdade e salvar nossa filha."

                us "Pode ir, cara."

                mc "Mas... se eu conseguir algo eu falo pra vocês."

                us "Falou."

                nora "..."

        scene black with dissolve

        scene n8_img28 with Dissolve(1.0)

    "Parece que tá tudo nos eixos. Agora só tenho que entrar nessa festa."

    "Eu PRECISO desse convite pra fazer o que eu preciso."

    "Acho que vou dar outro pulo na Blergh! e ver se a Roxane ou o Nathan conseguiram."

    "Eu também tenho que falar com ele. Garantir que tamo na mesma página. Tem gente grande dependendo de mim e do Nathan agora."

    play sound som_35_passos

    scene black with dissolve

    pause 1.0

    scene n7_passarela with Dissolve(1.0)

    "De novo eu aqui."

    "???" "Olha só quem voltou."

    scene black with dissolve

    scene n8_img30 with Dissolve(1.0)

    pause 2.0

    mc "E aí, Roxane."

    ro "De novo você por aqui? Esse namoro com o Nathan tá rendendo frutos, hein?"

    menu:
        "Já falei que não namoro ele. Meu rolo é com outra pessoa.":


            ro "Hmm... outra pessoa? Que não sou eu também pelo jeito."

            mc "Não haha..."

            ro "Por enquanto."

            mc "Eita, mulher..."
        "Não posso reclamar. Ele é um cara e tanto.":


            ro "Eu sei. Muito sensível e gente boa."

            ro "Pena que toda essa sensibilidade dele trava ele um pouquinho."

            mc "Hmm... bom... eu que não quero ficar travado."

            ro "Travado, é?"
        "Tô aqui por você e não por ele.":


            ro "Verdade..."

            scene black with dissolve

            scene n8_img32 with Dissolve(1.0)

            pause 2.0

            mc "S-sim... olha só pra você... de coelhinha assim..."

            mc "Vontade de te levar pra casa agora."

            ro "Quem sabe depois do evento..."

            mc "Vou cobrar. Pode ter certeza."

            ro "Mas então você não vai causar igual causou no Cassino, né?"

            mc "[ro]..."

    mc "Eu queria saber se rolou aquele convite pra mim? Pra eu poder ir na festa."

    ro "Eita... rolou nada, [mc]. Desculpa. Eu pedi pra Zaza, mas ela disse que tão contadíssimos os ingressos."

    mc "Merda... nem pra você ela tem?"

    ro "A lista tá fechada já faz um tempo, ela disse. Agora só pessoal que vai trabalhar no dia do evento."

    mc "Ferrou. Se a lista tá fechada, como que eu venho?"

    ro "Desculpa, viu... eu ia querer te ver aqui."

    menu:
        "Você tentou, pô. Eu só posso agradecer.":


            pass

    ro "Mas vamos marcar de sair um dia, tá? Quem sabe não roubo você do Nathan?"

    mc "Haha... vamos, sim, Rox."

    menu:
        "Você... não tem saudades de onde você veio?":


            ro "Como assim, gato?"

            mc "Você falou que foi pega criança pela Zaza. Você lembra de onde você veio? Tem saudades?"

            ro "Não."

            ro "Eu não lembro exatamente como era. Eu era bem pequena. Mas nunca olhei pra trás."

            ro "Minha vida de modelo é a coisa mais importante pra mim."

            ro "E... não sei se tô certa... mas eu acho que eu sou a coisa mais importante pra Zaza também."

            mc "Aquele dia... ela sendo severa com você. No fundo ela se importa com você, né?"

            ro "A Zaza tem uma coisa que eu nunca vi, [mc]. Ela se preocupa com outras pessoas e não só com ela."

            mc "Hmm..."

            scene black with dissolve

            scene n8_img31 with Dissolve(1.0)

            pause 2.0

            ro "A Verônica quer ver as mulheres fortes e poderosas. Ela sai da linha pra conseguir isso. Mesmo que ela se ferre."

            ro "Eu senti um pouco disso em você também. Que você se preocupa com os outros."

            ro "Mas ela é diferente. Eu sinto que ela faz isso por princípio. Que a vida dela é ver as mulheres se dando bem."

            mc "Entendo..."

            ro "Mas mesmo assim eu acho que eu sou mais importante hehe..."

            mc "Tá se achando um pouco, hein."

            ro "Tô! Haha!"

            mc "Mas tá certo."
        "Não vou falar nada":


            pass

    mc "Se eu conseguir um convite a gente se vê no evento."

    ro "Vou lá! Beijinho!"

    scene black with dissolve

    scene n8_img33 with Dissolve(1.0)

    pause 2.0

    ro "Olha só quem tá aqui. O escolhido."

    ro "Pronto pra grande noite? A chefe tá contando com a gente. Fala pra ele, [mc]."

    n "Eu sei... deixa comigo..."

    ro "Sei não, viu... você parece meio lelé das ideias, Nathan. Você é perfeito, mas precisa de personalidade."

    n "Tá passando tempo demais com a Zaza."

    ro "Ksks... tá parecendo mesmo. Bom namoro pros dois."

    n "Vai lá."

    ro "Bye bye, garotos."

    "Fodeu. Se a lista tá fechada eu tô ferrado. Ninguém vai conseguir convite pra mim."

    "A não ser que eu consiga o ingresso de alguém. Mas de quem?"

    mc "O Nathan é minha chance agora."

    n "Chance do quê?"

    if nathan_namoro:

        n "Chance de ter prazer na cama? Eu sou sua melhor chance, delícia."

        mc "E não é? Falou tudo, gato."

        mc "Quem dera fosse isso..."

    mc "Tava falando do convite pro dia da festa."

    scene black with dissolve

    scene n8_img34 with Dissolve(1.0)

    pause 2.0

    n "Ixi, [mc]... ferrou..."

    mc "Não acredito... nem você?"

    n "Nem eu e nem ninguém. A Zaza falou que todos os convidados foram fechados faz tempo já."

    mc "Mesma coisa que a Roxane disse..."

    n "Que saco, hein? Fiquei triste agora..."

    mc "Calma que ainda tem a Cássia. Ela é amiguinha da Zaza."

    n "A Cássia? Dever favor pra aquela víbora, cara?"

    mc "Vai ser o único jeito se eu quiser vir aqui."

    n "E nosso plano de ficar milionários e viver aproveitando o mundo depende disso."

    menu:
        "Haha... Ainda tá pensando nisso?":


            pass

    n "Tô pensando direto. De verdade."

    if grupo_nathan > 1:

        "Saco. Eu preciso do Nathan trabalhando pra Zaza e não sonhando em fugir pelo mundo."

        "Como eu faço a cabeça desse cara pro que eu preciso?!"

        "Talvez... jogar o jogo dele por um tempo. Ou cortar logo esse sonho idiota?"

        mc "Nathan, você precisa focar no teu futuro, cara. Confia em mim. Não viaja."

        n "Só que..."

        mc "Você não fez nada de errado. Você só lutou pelo que você queria."

        n "Mesmo que eu tenha enganado você e os outros? Pessoas que eram importantes pra mim."

        mc "Todo mundo vai entender."

        n "Não sei, [mc]..."

        "Parece que ele ainda não tá certo."

        "Eu preciso tá aqui no dia do evento pra garantir que ele não faça cagada."
    else:


        n "A única pena é que não tem como a gente pegar essa grana."

        mc "Hmmm... tu não vai acreditar. Mas alguém muito improvável pode ter dado o que a gente precisava."

        n "Não vai falar que foi a Cássia."

        mc "Ela mesmo. Ela disse que o dinheiro que vão dar pra Zaza vai ser em espécie."

        n "Só pode ser faz de conta isso..."

        mc "Ela até deu as razões dela lá. Dinheiro sujo e tal..."

        n "Não sei se dá pra confiar na Cássia. Odeio aquela mulher. A gente pode dá de cara na parede."

        menu:
            "Pensando agora... tem uma boa chance mesmo.":


                n "Tem TODAS as chances. Vê se fica esperto."
            "Vamo ter que confiar nela nessa. É a única chance.":


                n "Eu tô aqui por causa da Cássia, mas eu não quero confiar nela nunca mais."

                n "O preço na nossa cabeça de fazer a coisa errada é caro demais."

        mc "Se ela tá falando a verdade, eu tenho uma ideia de como fazer isso."

        n "Manda, cabeça."

        mc "Você vai agir normalmente até a noite do evento. A Zaza não pode suspeitar de nada ou ela vai tirar a grana do cofre."

        mc "Tudo vai acontecer normalmente. Até o desfile vai acontecer normalmente e você vai tá lá na passarela."

        mc "No meio do rolo todo eu vou na sala dela e pego a grana. Daí depois do seu desfile a gente dá o fora."

        scene black with dissolve

        scene n8_img35 with Dissolve(1.0)

        pause 2.0

        n "Legal... gostei, líder. Só que como você vai entrar na sala dela? Nem eu tenho chave."

        mc "Hmm... tem isso, né? Talvez a Roxane?"

        n "Sei não... a Zaza gosta dela, mas é igual eu. Ela gosta da gente até certo ponto só."

        mc "Bom... uma coisa de cada vez."

        n "Isso aí. Vamos sonhando até o dia do evento hehe..."

        "Será que esse plano realmente faz sentido?"

        "Tá na cara que isso é grande demais pra gente. Tamo falando de roubo na cara dura. E de milhões ainda."

        menu:
            "Deixa essa missão louca de lado e vamos focar no que importa.":


                $ n8_convenceu += 1

                n "Talvez seja melhor mesmo..."

                mc "Bora focar no seguro. E não viajar demais. Pelo menos agora."

                n "Você tem razão..."
            "Não. Eu quero tentar essa doideira. Mesmo que eu morra tentando.":


                n "Tá falando sério?!"

                mc "Imagina?! Grana infinita pra nós dois!"

                mc "Eu já tive a sensação de ter a carteira com grana quase infinita! Você não sabe como é bom."

                mc "Pena que era um erro..."

                n "Então você vai querer seguir nessa loucura mesmo."

                mc "Com certeza!"

    mc "Agora, como eu consigo esse ingresso?"

    mc "Vou lá falar com a Cássia. Ela precisa servir pra alguma coisa."

    if nathan_namoro:

        n "Boa sorte, gostoso. Pra mim vai ser muito bom se você conseguir. E desculpa não conseguir pra você, meu gato."

        mc "Relaxa, delícia."
    else:


        n "Boa sorte, amigo. Pra mim vai ser muito legal se você tiver aqui nesse momento fundamental. E desculpa não conseguir pra você."

    mc "Vou dar meus pulos. Não vou ficar fora desse evento."

    mc "A gente se vê no dia. Pode ter certeza."

    n "Vou contar contigo lá."

    scene black with dissolve

    scene ilha base with Dissolve(1.0)

    "Nada... minhas duas melhores chances eram a Roxane e o Nathan."

    "Agora... só falta a Cássia..."

    if grupo_nathan > 1:

        "Nós dois estamos trabalhando juntos pra fazer a cabeça do Nathan."

        "O mínimo que ela pode fazer é me garantir entrada."
    else:


        "Será que eu vou ter que me dobrar pra ela?"

    "Bora fechar isso de uma vez."

    scene black with dissolve

    scene n8_img36 with Dissolve(1.0)

    pause 2.0

    j "Você, pombinho?"

    if grupo_nathan > 1:

        j "Fez a cabeça do nosso garotinho?"
    else:


        j "Mudou de ideia sobre o que eu te ofereci?"

    menu:
        "Eu preciso de um convite pro dia do desfile.":


            pass

    if grupo_nathan > 1:

        mc "Se você quer que eu faça a cabeça dele, eu preciso dessa ajuda agora. Os ingressos acabaram."

        j "Acabaram? Que pena. Eu peguei o meu."

        mc "Você tá brincando?!"

        j "Se você quer fazer parte do grupo, tem que saber cuidar do teu, pombinho."

        j "Não pode vir pra mamãe chorar toda vez que precisar fazer algo. Pra isso, eles não precisam de você."

        j "Cada um é medido pelo tanto que faz a roda girar."

        menu:
            "Entendi... eu vou dar meus corres.":


                ""
            "Isso não é justo! Você quer ajuda e não faz porra alguma!":


                j "Pode fazer birra. Não muda nada."

                mc "Saco!"

        j "Hehe..."
    else:


        j "Quem sabe se você tivesse aceitado minhas condições eu pudesse te ajudar agora."

        mc "[j]... por favor... você é minha única chance. Eu tô quase ajoelhando aqui!"

        j "Da próxima vez, pense melhor com quem você vai se aliar."

        mc "Desgrama..."

        j "Bobinho..."

        mc "Saco!"



    scene black with dissolve

    pause

    scene n8_img37 with Dissolve(1.0)

    pause 2.0

    mc "Acabou..."

    mc "Não existe mais chance de entrar lá..."

    gar "Veja se não é nosso soturno companheiro das causas impossíveis."

    menu:
        "Não tô com cabeça pros seus papinhos hoje. Mal aí.":


            pass

    scene black with dissolve

    scene n8_img38 with Dissolve(1.0)

    pause 2.0

    gar "Decepção e frustração. Sua áura emana desgosto e cheira a pão embolorado."

    if grupo_nathan < 2:

        mc "É complicado... eu quis fazer a coisa certa e não ferrar meu amigo."

        mc "E agora fiquei de fora."

        gar "O certo sempre será recompensado pelos justos, benigno amigo."

        mc "Me dá um convite pro evento da Blergh! então."

        gar "Infelizmente, isso este humilde servo não poderá fazer."

        mc "Tá vendo... cadê a recompensa dos justos agora?"

        gar "Todavia, há de se considerar que o oculto usa traços tortos para desenhar linhas retas."
    else:


        mc "Os caras são foda. Eles querem que eu faça algo, mas não me dão as ferramentas."

        gar "Quanto maior o pico, maior a subida."

        mc "Não sei se consigo subir tudo isso."

        gar "Fracos de espírito pouco atingem na vida, na humilde opinião deste servo."

        mc "Eu só queria uma ajuda. Uma forma de tentar conseguir. Não ligo de ralar, só que preciso de uma ajuda."

        gar "Se seu senhores não lhe dão as oportunidades que seu espírito ambicioso busca, permita que este humilde servo o faça."

        mc "Me dá um convite pro evento da Blergh! então."

    gar "Convite? Este servo não tem pompa para tanto. Mas uma entrada no paraíso da porta larga? A chave ele tem."

    mc "Entendi porra nenhuma."

    gar "Permita este pobre espírito se traduzir: posso colocar você dentro do evento."

    mc "C-como?! Consegue?!"

    gar "O humilde antro de prazeres em que nos encontramos agora foi chamado para atender o evento do qual meu companheiro fala."

    mc "Sério?! Você vai trabalhar lá?!"

    gar "Acredito ser feito de nosso amigo mútuo, o honorável modelo de cabelo raspado."

    mc "Entendi... o Nathan conseguiu pra você. Você... pode me levar como seu funcionário?"

    gar "É o que proponho, se estiver disposto a aceitar as oblíqua e dissimulada sugestão deste amigo dos momentos baixos."

    mc "Que outra chance eu tenho? Todo mundo me abandonou. Nem meu jornal, nem meus amigos, nem meus inimigos."

    menu:
        "Eu vou com você. Muito obrigado, [gar].":


            pass

    gar "Enche meu coração de felicitações tais palavras, meu nobílissimo senhor."

    mc "Nem acredito que eu vou poder ir pra festa realizar meus planos."

    gar "Quais objetivos tem essa sua mente abençoada?"

    if grupo_nathan > 1:

        mc "Meu objetivo até que é bem simples. Eu tenho que garantir que o Nathan continue com a Blergh!."

        mc "Eu falei umas coisas pra ele, mas vou precisar garantir que ele não estrague tudo na noite mais importante."

        gar "O trabalho de babá é deveras importante."

        mc "Nem fala..."
    else:


        mc "Tem muita coisa em jogo. Tu nem tem ideia."

        mc "Muita grana, o Distrito, o Grupo, o Nathan, a chance de uma vida melhor, a Roxane, a Cássia, a Zaza, a Sofia e meu trabalho como paparazzo."

        mc "Cara... sinceramente, eu já me meti em muito buraco na cidade. Mas igual esse... nunca."

        mc "Esse vai ser o evento com mais coisas em jogo desde que eu entrei nesta vida."

    gar "Me parece um prato cheio, inestimável amigo."

    gar "Desejo para você o melhor."

    mc "Valeu. Graças a você eu vou poder ter uma chance de resolver isso."

    gar "Ah... falando nisso, tenho um porém para o senhor."

    gar "Para trabalhar comigo lá, você deverá estar devidamente trajado."

    menu:
        "Isso é o de menos. Eu uso essa roupa sua aí.":


            pass

    scene black with dissolve

    scene n8_img39 with Dissolve(1.0)

    pause 2.0

    gar "Sua humildade é invejável. No entanto, outro porém existe."

    gar "Terei que encomendar uma para o seu tamanho."

    menu:
        "Beleza. Manda fazer uma bem bonita.":


            gar "Excelente! Entusiasmo do mais alto nível!"

            mc "Opa! Temo que tá no grau pra uma festança daquelas."

            gar "Apoiado."
        "Precisa, não. A sua tá bom demais. Mesmo que falte ou sobre um pouco.":


            gar "De jeito maneira, companheiro de labuta. É imperativo que estejamos devidamente trajados ao máximo de nossa capacidade."

            gar "Estamos nos referindo à maior festa já presenciada pela cidade."

            mc "Ok... e o que você precisa de mim?"

    gar "Vou precisar apenas de {b}C$ 1.000{/b} para garantir sua vestimenta."

    mc "MILÃO?!"

    gar "Teremos que representar a mais pura finesse na fatídica noite."

    mc "Eu imagino quanto um convite desse não custaria... ainda vai sair barato."

    gar "Pois bem, esse é o espírito resignado dos santos."

    mc "Se você falar isso de novo eu rasgo teu uniforme e tu vai ter que pagar também."

    gar "Ora, este servo calar-se-á."

    gar "Quando estiver dotado do dote, por favor se dirija a este parceiro de jornada trabalhista para que ele faça o pedido do seu traje de batalha."

    mc "Ok... vou pegar a grana e te encontro aqui no bar."

    mc "E daí é só esperar o dia do evento."

    gar "Será um evento como nenhum outro. Isso há de ser garantido pelas estrelas."

    mc "Te vejo logo, [gar]."

    gar "Que o bom vento lhe leve."

    scene black with dissolve

    scene n8_img37 with Dissolve(1.0)

    "Pegar a grana e voltar aqui no bar."

    $ n8_roupa = 1

    "E daí me preparar pra grande noite."

    "Vai ser minha última chance de pensar como eu vou querer que tudo acabe."

    "Eu tenho várias oportunidades. Qual será que vai me dar uma vida mais foda?"

    "E o Nathan? Qual caminho ele vai ser mais feliz?"

    $ n8_roupa = 1

    scene black with dissolve

    $ tempo += 1

    jump call_cidade

label nathan_evento8_parte2:

    $ nathan_e8 = "evento2"

    "Chegou o dia da festa da Blergh!... Vou me encontrar com o Fabrício no bar e bora lá."

    scene black with dissolve

    $ tempo = 3

    pause 2.0

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    scene n8i1 with Dissolve(2.0)

    mc "Caraca..."

    gar "Chegamos, meu caro [mc]. Bem-vindo ao Olimpo dos Deuses da Moda."

    mc "É... parece que é isso mesmo."

    "Nunca vi tanta gente chique junta. E as roupas... quanta ostentação."

    "Acho que eu nunca me senti tão deslocado em toda a minha vida. Nem com essa roupa do [gar]."

    mc "Valeu mesmo por ter me trazido, [gar]."

    mc "Essa roupa tá..."

    menu:
        "Horrível. Parece um uniforme de presidiário.":


            gar "Gostos são como bundas, cada um tem a sua."

            mc "..."
        "Interessante. Gostei do estilo.":


            gar "Agradeço a gentileza, nobre companheiro. Finesse é fundamental nestes eventos."
        "Diferente. Chama a atenção.":


            mc "Chama a atenção, com certeza."

            gar "A discrição é uma virtude dos fracos, meu caro."

            mc "E você é forte, é?"

    gar "Mas falando sobre assuntos mais importantes. Você já está livre para realizar seus intentos."

    mc "Sério?"

    gar "Sim. Apenas lhe peço que evite causar qualquer problema que possa manchar a reputação deste humilde servo."

    mc "De boa. Pode deixar."

    gar "Então, me retiro para realizar minhas nobres funções de garçom. Boa sorte com suas empreitadas, [mc]."

    mc "Valeu, [gar]."

    scene black with dissolve

    scene n8i2 with Dissolve(1.0)

    pause 2.0

    "O Fabrício sumiu no meio da multidão... nunca vi ele se movimentar tão rápido."

    "Agora é a hora da verdade. Tenho que encontrar o Nathan e colocar nosso plano em prática."

    "Só de pensar no que a gente tá pra fazer... roubar MILHÕES da Zaza... isso me dá um frio na barriga."

    "E se a gente for pego? A Zaza não é boba. E a Cássia... ela com certeza vai tentar me ferrar de algum jeito."

    "Mas agora não tem mais volta. Eu preciso fazer isso. Pelo Nathan... e por mim também."

    "Eu posso ficar milionário e nunca mais ter que me meter em roubada. Só ser feliz com a pessoa que eu escolher."

    "Seria um final digno pra quem sofreu tanto tempo nesta maldita cidade."

    "Mas antes de sonhar, preciso encontrar o Nathan antes que a festa comece pra valer."

    "Cadê ele, merda?! Ele já devia tá aqui."

    "???" "IO!"

    mc "Aleluia!"

    scene black with dissolve

    scene n8i3 with Dissolve(1.0)

    pause 2.0

    n "Xii... não vira pra cá."

    n "Você conseguiu entrar mesmo, hein? Você tá afim de fazer isso."

    menu:
        "Claro! Eu quero grana, sombra e água fresca!":


            n "Isso aí!"
        "A gente vai falar sobre isso... mas não assim.":


            n "Hmm... ok..."

    n "E aí? Tá pronto pra ação?"

    mc "Cara... você tá... com aquela roupa..."

    n "Haha... é o que a Zaza chama de 'presença'."

    mc "Entendi... mas e aí? T-tá nervoso?"

    n "Tô... mas não posso fraquejar agora. A gente precisa fazer isso."

    "Parece que ele também tá contando com o plano agora..."

    mc "Sim... mas como a gente vai se encontrar? A Zaza não pode ver a gente juntos."

    n "Eu vou te encontrar no banheiro."

    mc "Tá... mas e a grana? Como eu vou saber onde ela tá?"

    n "A Zaza tem um cofre na sala dela. É o único lugar que ela guarda coisas importantes, lembra?"

    mc "E como eu vou entrar lá?"

    n "A Roxane... ela tem a chave."

    mc "Eu não sei se a Roxane..."

    n "A gente não tem escolha. Se a gente quer ficar rico e dar o fora desta merda, essa é a única chance."

    n "Eu também tô nervoso. Mas a gente precisa confiar um no outro."

    mc "Sim... vamos fazer isso."

    n "Eu vou trocar uma ideia com uns figurões. Já te encontro lá e acertamos tudo. Te vejo no banheiro depois."

    mc "Boa sorte."

    scene black with dissolve

    scene n8i2 with Dissolve(1.0)

    mc "Merda..."

    "Se encontrar no banheiro... Melhor eu ir pra lá antes que fique cheio de gente."

    "Ou talvez eu possa... tentar descobrir algo com alguém por aqui? Talvez achar a Roxane."

    menu:
        "Ir direto para o banheiro":


            pass
        "Procurar a Roxane na festa":


            "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

            mc "Deixa eu dar uma olhada nesse povo. Quem sabe eu não encontro ela..."

            "Mesas cheias de comida e bebida. Parece que não economizaram em nada."

            "Tem gente dançando, conversando, bebendo. Acho que até vi o prefeito Donatello ali no canto. Cercado de seguranças, claro."

            "Parece que a nata da sociedade da Capital tá reunida aqui. Acho que até vi a mulher do programa de culinária da Faux News."

            label nathan8_festa_roxane:

                pass

            scene black with dissolve

            scene n8i5 with Dissolve(1.0)

            pause 2.0

            mc "Eita! A Roxane!"

            "Ela tá ali no cantinho, conversando com aquele cara. Com aquela roupa de coelheinha..."

            "Pensando bem, não sei se é a melhor ideia ela me ver aqui. Pode dar bandeira demais."

            "Melhor eu sair de fininho antes que ela me veja. Não vai ser bom se ela fizer perguntas de como eu entrei."

            "Vou tentar ser discreto..."

            play sound som_hit

            scene n8i5 with hpunch

            mc "Ai!"

            "Tacaram alguma coisa em mim!"

            ro "Eu tô te vendo! Vem cá!"

            mc "Ai..."

            scene black with dissolve

            scene n8i6 with Dissolve(1.0)

            pause 2.0

            ro "Você aqui, [mc]?!"

            mc "E-e aí, Roxane..."

            ro "M-mas como? A lista de convidados tava fechada! A Zaza vai te matar se te encontrar aqui!"

            mc "Calma... eu..."

            ro "Me fala!"

            menu:
                "Eu tenho meus contatos...":


                    mc "Eu tenho meus contatos. Relaxa."

                    ro "Contatos? Com essa roupa de..."

                    ro "..."

                    mc "Que foi? Não gostou?"

                    ro "Digamos que... é um visual... diferente... parece com os garçons. Idêntico na verdade."

                    mc "Você prefere a roupa de coelhinha? Aquela vez..."

                    if roxane_seducao > 2:

                        $ roxane_seducao += 1

                        ro "Você não esquece mesmo, né?"

                        mc "Claro que não. Foi inesquecível."

                        ro "Hmm... quem sabe a gente não repete a dose depois da festa."

                        mc "Sério? Vou esperar ansioso."

                        ro "Mas agora eu preciso voltar pros clientes... digo, investidores. Eles... tão de olho em mim."

                        mc "Tá legal. Te vejo depois então."

                        ro "Pode deixar. Eu vou te encontrar."
                    else:


                        ro "Não muda de assunto. Que contatos você tem que te colocaram aqui com essa roupa?"

                        mc "Me deixa, Roxane. Tá tudo certo."

                        "Talvez se eu tivesse flertado mais com ela... ela brincaria junto."

                        ro "Hmmm..."
                "Deixa pra lá. Preciso falar com o Nathan.":


                    mc "Deixa pra lá. Preciso falar com o Nathan. Você viu ele?"

                    ro "Hmm... tá escondendo algo. Mas tudo bem, eu descubro depois."

            $ roxane_observando = True

            ro "[mc]... só mais uma coisa... sai daqui antes que alguém te veja... Você não devia estar aqui."

            ro "Eu sei que tem algo de errado."

            "Ela tá sussurrando... ela tá tentando me proteger?"

            mc "Eu só vim..."

            ro "Você prometeu que não ia se meter. Que ia me deixar seguir meu sonho."

            mc "Mas a Zaza..."

            ro "Eu não me importo! Eu quero ficar aqui! Eu quero ser modelo!"

            mc "Mas e o Distrito? Sua família?"

            ro "Não me fale do Distrito! Eles me abandonaram! A Zaza é a única família que eu tenho!"

            mc "Roxane, você não precis-"

            ro "Por favor, [mc]. Vai embora. Por mim. As coisas tão boas do jeito que tão."

            "Esse rolo da Roxane, Distrito, Zaza... me lembra muito o que aconteceu com outras garotas..."

            "Se eu conseguir chegar no escritório da Zaza... talvez eu consiga descobrir se ela também..."

            menu:
                "Fica tranquila. Eu vou cuidar de você. Vou descobrir a verdade.":


                    $ roxane_seducao += 1

                    ro "Q-quê? Como assim?"

                    mc "Não importa o que aconteça."

                    ro "[mc]... você promete? Promete que não vai estragar tudo?"

                    mc "P-prometo..."

                    ro "Obrigada, [mc]. Você é um cara legal."

                    mc "Tudo bem. A gente se vê depois."
                "Tá legal. Vou te deixar em paz.":


                    mc "Tá legal. Vou te deixar em paz. Desculpa."

                    ro "Obrigada, [mc]."

            scene black with dissolve

            scene n8i5 with Dissolve(1.0)

            "Droga... a Roxane tá realmente decidida a ficar com a Zaza."

            "Eu sinto que tô fazendo a coisa errada, roubando a Blergh!. Mas e o Nathan? E nosso futuro?"

            "Preciso me concentrar no plano. Agora não é hora de pensar nisso."
        "Falar com alguém na festa":


            scene black with dissolve

            scene n8i4 with Dissolve(1.0)

            pause 2.0

            "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

            mc "Vou tentar me enturmar um pouco... quem sabe eu não consigo alguma informação útil."

            "Preciso encontrar alguém interessante pra puxar conversa."

            "Mulher" "Olá..."

            mc "O-oi. Com licença, posso me juntar a você?"

            "Mulher" "Claro. Sente-se."

            mc "Obrigado. Meu nome é [mc], prazer."

            "Mulher" "Prazer, [mc]. Eu sou a [fn], trabalho na Faux News."

            mc surpreso "Na Faux News? Sério?"

            fn "Sim. Você parece surpreso."

            mc "É que... bom... não é todo dia que a gente encontra alguém da Faux."

            fn "Ksks... Entendo. E você? O que faz?"

            mc "Eu sou jornalista. Trabalho naquela revista da ilha."

            fn "Ah, sim! Sempre leio. Eu vi alguns furos que você descobriu. Você tem talento, sabia?"

            mc "Sério? Valeu."

            fn "Você tem um faro bom. E um olhar... penetrante."

            mc envergonhado "O-olhar?"

            fn "Sim. Seus olhos... eles têm algo... especial."

            "E-eita... o que ela tá fazendo se aproximando assim?"

            mc "Hã... obrigado?"

            fn "Não precisa ficar tímido. Eu gosto de homens confiantes."

            "Caramba... essa mulher tá dando em cima de mim? Justo agora?"

            menu:
                "Falar que tá ocupado":


                    mc "Olha, [fn], você é muito gentil, mas agora eu tô meio ocupado. Quem sabe a gente conversa depois?"

                    fn "Eu adoraria..."

                    mc "Foi um prazer te conhecer."

                    fn "O prazer foi meu, [mc]. Espero te ver de novo."

                    "Ufa... escapei por pouco. Melhor eu ir pro banheiro antes que aconteça outra coisa."
                "Ignorar o flerte":


                    mc "Hã... legal. Bom, eu preciso ir..."

                    fn "Ah... tudo bem."

                    mc "Tchau."

                    "Essa mulher não desiste fácil... mas eu não tenho tempo pra isso agora."

                    "Preciso achar o Nathan."

            jump nathan8_festa_roxane

    scene black with dissolve

    scene n8i7 with Dissolve(1.0)

    pause 2.0

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    mc "Cheguei. O Nathan já deve tá vindo."

    "A gente combinou tudo no bar do Fabrício. O plano é simples, mas arriscado pra caralho."

    "Eu tenho que entrar na sala dela, pegar a grana que tá no cofre e dar o fora daqui."

    "Mas e se a gente for pego? A Zaza vai ficar furiosa. E o Grupo? Eles não vão deixar barato."

    "E se o plano der errado e a gente não conseguir fugir? A gente vai acabar preso, ou pior... o que o Tony vai fazer comigo."

    "Não posso pensar nisso agora. Preciso me concentrar."

    "Preciso ser forte... pelo Nathan..."

    if nathan_namoro:

        mc "Pelo nosso futuro juntos..."

    "???" "Que cara é essa?"

    mc "Hm?!"

    scene black with dissolve

    scene n8i8 with Dissolve(1.0)

    pause 2.0

    mc "Nathan!"

    n "[mc]! Você veio mesmo..."

    mc "Claro que eu vim. Não ia te deixar na mão, né?"

    n "Valeu, cara. Tô nervoso pra caralho."

    mc "Eu também. Mas a gente consegue."

    n "Você conseguiu a chave com a Roxane?"

    mc "Não adianta. Ela não vai aceitar. Ela não quer sair da Blergh!. Ela ama a Zaza."

    n "Merda... e agora?"

    "A gente tá ferrado... sem a chave, não tem como abrir o cofre."

    menu:
        "Espera... e se...":


            pass

    n "Se o quê?"

    mc "A Cássia... lembra que eu te falei que ouvi ela falando com a Zaza na sala dela?"

    n "Sim. Quando tu caiu de susto. E daí?"

    mc "A Zaza e a Cássia pareciam unha e carne."

    n "Sim... eu acho que elas têm algo, sim. Mas... o que isso tem a ver com a chave?"

    mc "E se ela tiver a chave? E se a Cássia for igual a Roxane? Alguém que ela confia?"

    n "Hmm... faz sentido..."

    mc "Mas... se nem a Roxane aceita, como a gente vai fazer a Cássia abrir a sala pra gente?"

    "A Cássia não é boba. Ela não vai cair numa armadilha fácil."

    n "Hehe... Deixa isso comigo. Eu tenho um plano."

    mc "Que plano?"

    n "Eu vou seduzir a Cássia."

    mc "Seduzir? Como assim?"

    n "Eu vou levar ela pra sala da Zaza. E vou trepar com ela lá."

    mc "Você tá falando sério?!"

    n "Claro. Ela me deseja pra caralho. É só usar isso contra ela."

    menu:
        "Ela vai ter o que merece. Ser manipulada.":


            n "Né?! Essa maldita merece."
        "Não quero ver você com aquela mulher.":


            n "Aww... não precisa se preocupar comigo."

    n "Relaxa. Eu vou lá ficar com ela na sala. E daí deixar a porta aberta pra você entrar."

    mc "Caramba... você realmente vai fazer isso?"

    n "Se for pra gente conseguir a grana e ser livre, eu faço qualquer coisa."

    mc "..."

    if diana_grupo:

        if grupo_nathan >= 1:

            "Eu prometi pro Tony que ia fazer a cabeça dele."

            "Eu joguei o jogo do Nathan. Fingi que tava interessado nisso tudo. Ele confia em mim."

            "É hora de tirar isso da cabeça dele e fazer ele ser o cachorrinho do Tony, da Cássia, da Zaza e do Grupo."

            "E eu vou me tornar o próximo na lista. Vou provar meu valor e conquistar meu lugar na mesa."

            "As coisas vão continuar como sempre foram na Capital. Com ordem e controle. E eu vou criar as regras também."

            "Mas... esse sou eu mesmo? Manipular ele pro meu próprio ganho? Foi isso que eu me tornei?"

            "Toda vez que vou por esse caminho algo me diz que eu tô me tornando o vilão."

            "É esse caminho que eu quero mesmo?"
    else:


        "Ele tá falando sério... usar a Cássia desse jeito..."

        "Mas ele tem razão. Essa pode ser nossa única chance se eu quiser tirar ele daqui."

        "Só que... eu vou ser cúmplice disso? Até ontem eu era um jornalista me mantendo na Capital."

        "E agora eu tô tentando roubar a dona de uma grife pra fugir do país?"

        "Primeiro a Diana no Cassino... agora isso... COMO AS COISAS CHEGARAM NISSO!?"

    "E o que eu vou fazer?"

    label nathan_final_escolha1:

        pass

    menu:
        "VAMOS DESISTIR. Isso é loucura demais, Nathan... eu sou só um cara normal.":


            mc "Nathan, você tá louco? E se pegarem a gente? A gente vai pra cadeia!"

            n "Relaxa, [mc]. Eu sei o que tô fazendo. Ela nunca vai desconfiar."

            mc "Mas e se..."

            n "[mc], confia em mim. Vai dar tudo certo."

            "Caralho..."
        "Nathan... vamos parar de brincadeira. O Grupo vai realizar seu sonho.":


            jump nathan_final3



            mc "Nathan, você quer colocar tudo a perder? É isso que você quer?"

            n "N-não... Eu só quero a grana pra gente poder sumir daqui."

            mc "Fugir? Pra quê? Você tem tudo aqui! Você é um modelo famoso, tá na mídia, tem contatos..."

            n "Mas..."

            mc "Pensa bem, Nathan. Você lutou tanto pra chegar onde tá. E agora você quer jogar tudo fora?"

            n "É que... a Zaza... a Cássia... elas me manipularam. Eu não quero mais ser um peão no jogo delas."

            mc "Eu entendo. Mas você pode virar o jogo. Você pode usar a Blergh! e o Grupo a seu favor."

            n "Como?"

            mc "Imagina, você como o rosto da Blergh!, famoso no mundo inteiro. Você pode ter tudo o que sempre quis: dinheiro, fama, poder."

            n "Mas... e a minha liberdade?"

            mc "Você não precisa se prender a elas. Você pode ter seus próprios planos. Você pode ser o dono do seu destino."

            n "Você realmente acha isso?"

            mc "Claro. Você tem talento, carisma, beleza. Você tem tudo pra ser um astro. E o Grupo pode te ajudar a chegar lá."

            n "Mas e se eles me usarem de novo?"

            mc "Você não vai deixar. Você vai ser esperto. Você vai usar eles antes que eles te usem."



            mc "(Chegando mais perto, com um olhar intenso) Nathan, você pode ter tudo. Imagina: você, no topo do mundo, ditando as regras, realizando todos os seus sonhos."

            n "(Olhando nos olhos do MC, sentindo a ambição crescendo dentro dele)..."

            mc "E eu vou estar do seu lado. A gente vai conquistar essa cidade juntos. A gente vai ter tudo."

            n "(Com um sorriso determinado) Você tá certo, [mc]. Eu não vou fugir. Eu vou lutar. Eu vou mostrar pra Zaza e pra Cássia quem é que manda."

            mc "Isso aí, Nathan. Esse é o cara que eu conheci."

            n "Valeu, [mc]. Você me deu a força que eu precisava."

            mc "Agora vamos voltar pra festa. E vamos mostrar pra esse povo quem são os verdadeiros jogadores."

            n "Vamos."

            $ nathan_grupo = True
        "A gente precisa fazer o certo. Acabar com um dos pilares do Grupo, a Blergh!.":




            mc "Derrubar eles vai deixar a Capital um passo mais livre dessa corja."

            n "Você... você realmente parece um herói falando assim."

            mc "Haha... não é nada tão grande. Só... tô fazendo o que qualquer pessoa deveria fazer."
        "Eu só quero viver uma vida boa, cara. Rico, longe daqui.":


            mc "Nathan, se é pra gente ter uma vida dessas, eu topo qualquer coisa. Mesmo que seja errado."

            n "Valeu, [mc]. Você é o cara. A gente vai curtir muito!"

            mc "Espero não me arrepender..."

    mc "Então a gente vai continuar com isso mesmo."

    "O que eu tô fazendo?"

    mc "Eu tô decidido. Agora, o que você tá sentindo? Você realmente quer fazer isso?"

    menu:
        "Você tem certeza que quer fugir?":


            mc "Nathan, você tem certeza que quer fugir? Abandonar tudo?"

            n "Eu não sei mais, [mc]. É muita coisa pra pensar."

            n "Eu sempre quis ser modelo... mas agora... depois de tudo..."

            n "Eu não sei se quero viver nesse mundo de mentiras e traições."

            mc "Eu entendo."
        "Se você tá com medo, a gente pode desistir.":


            mc "Nathan, se você tá com medo, a gente pode desistir. Não precisa fazer isso."

            n "[mc], eu... eu não sei. Eu queria tanto ter uma vida diferente..."

            n "Mas agora eu tô com medo. Medo de perder tudo. Medo de me ferrar."

            mc "Eu tô aqui com você. Não importa o que você decidir."

            n "Valeu, [mc]."
        "A gente precisa ser forte agora.":


            mc "Nathan, a gente precisa ser forte agora. Não podemos deixar o medo nos dominar."

            n "Você tem razão. A gente já chegou até aqui. Não podemos desistir agora."

            mc "Isso aí. Vamos conseguir."

    label nathan_recupera_final3:

        pass

    n "A gente vai conseguir, [mc]."

    mc "Sim. A gente vai."

    n "E depois... a gente vai ser livre."

    if nathan_namoro:

        n "Vamos poder viver nosso amor sem medo."

        mc "É isso que eu mais quero."

    n "Eu vou voltar pra festa agora. Vou procurar a Cássia. Você dá um tempo, e tenta seguir a gente."

    mc "Caralho... eu vou tá logo atrás."

    n "Deixa comigo. Ela ama o que eu tenho pra ela."

    if nathan_namoro:

        mc "N-nathan!"

        scene black with dissolve

        scene n8i9 with Dissolve(1.0)

        pause 2.0

        "A gente tá fazendo isso por nós... pelo nosso futuro juntos."

        mc "Nathan... eu..."

        n "Ei... o que foi? Você tá pálido."

        mc "Eu só... não quero que você se arrisque tanto assim."

        n "Relaxa, meu amor. Vai dar tudo certo. Eu prometo."

        mc "Mas essas pessoas... elas... você tem que ver o que elas fizeram com a Diana..."

        n "Eles não vão desconfiar de nada. Eu sei como lidar com esse povo."

        mc "Mas..."

        scene black with dissolve

        scene n8i10 with Dissolve(1.0)

        pause 2.0

        n "[mc]... confia em mim. Eu tô fazendo isso por nós. Pra gente poder finalmente ser feliz."

        mc "Hmm..."

        n "Imagina só... a gente, longe daqui, em uma praia paradisíaca, só curtindo a vida."

        mc "Sem a Zaza, sem a Cássia, sem o Grupo..."

        n "Só a gente... nosso amor... nossa liberdade..."

        mc "Nathan..."

        n "Eu te amo tanto, [mc]... você nem imagina o quanto."

        mc "Eu também te amo, Nathan. Mais do que tudo."

        menu:
            "Mas... e a Cássia? Você vai mesmo t-transar...?":


                n "Não se preocupa com isso, meu amor. É só um jogo. Eu não sinto nada por ela."

                mc "Mas..."

                n "Relaxa. Você é o único que eu amo. É só você que eu quero."

                mc "Hmm..."
            "Eu te amo, Nathan. A gente vai conseguir.":


                n "Eu também te amo, [mc]. Mais do que tudo."

        scene black with dissolve

        scene n8i9 with Dissolve(1.0)

        n "Agora eu preciso ir. Te encontro aqui depois do desfile."

        mc "Tá bom. Vai com cuidado."

        n "Eu te amo."

        mc "Eu também te amo."

        "Meu coração tá batendo tão forte... Eu amo o Nathan. E ele me ama também."

        "A gente vai conseguir. A gente vai ser feliz. Juntos."

    scene black with dissolve

    scene n8i11 with Dissolve(1.0)

    pause 2.0

    "O Nathan parece mais confiante agora. Mas eu ainda tô com um mau pressentimento..."

    "Preciso encontrar a Roxane e ter certeza que ela vai ajudar a gente."

    "E a Cássia... onde será que ela tá? Ela com certeza vai tentar atrapalhar."

    "Essa noite vai ser longa..."

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    "Agora é torcer pro Nathan conseguir enganar a Cássia a abrir a porta. Tenho que ficar de olho nos dois."

    "DJ" "Atenção! A batida vai parar porque nossa chefe, a grande Verônica Zaza tem um pronunciamento a fazer!"

    "{i}Clap clap clap{/i}"

    "Eita! Todo mundo batendo palmas pra ela... ela realmente é a dona da porra toda aqui."

    "Eu não posso perder isso!"

    scene black with dissolve

    scene n8i12 with Dissolve(1.0)

    pause 2.0

    za "Boa noite, senhores e senhoras."

    za "É com grande prazer que recebo todos vocês aqui nesta noite tão especial."

    za "Esta festa é mais do que uma simples celebração. É um marco na história da Blergh!. É o início de uma nova era."

    za "A Blergh! está pronta para se tornar uma marca global. E isso só foi possível graças ao apoio de pessoas muito especiais."

    za "Pessoas que acreditaram em nosso potencial. Pessoas que investiram em nosso sonho."

    za "E eu gostaria de agradecer especialmente ao prefeito Donatello, que está aqui presente, por sua confiança e apoio."

    za "A Capital é uma cidade única. Uma cidade vibrante, cheia de vida e de oportunidades."

    za "Mas também é uma cidade que precisa de proteção. Uma cidade que precisa de pessoas fortes e determinadas para guiá-la."

    za "Pessoas que não têm medo de tomar decisões difíceis. Pessoas que estão dispostas a fazer o que for preciso para proteger nossa cidade."

    za "Eu acredito que a Blergh! pode ser um desses pilares de força."

    za "Desde que eu fundei ela no dia 13 de Maio de 2007. Um dia depois de encontrar a coisa mais importante pra mim."

    "Ela tá olhando pra Roxane... então ela fundou a Blergh! um dia depois de encontrar a Roxane..."

    za "Aqui na Blergh! nós temos a visão, a ambição e a coragem para ajudar a construir um futuro melhor para a Capital."

    za "E eu, Verônica Zaza, estou pronta para fazer parte desse futuro."

    za "Eu sei que alguns de vocês podem ter dúvidas sobre mim. Mas eu quero que vocês saibam que eu estou disposta a fazer o que for preciso para proteger nossa cidade."

    za "Eu tenho a força, a inteligência e a determinação para fazer parte do Grupo."

    za "E eu espero que vocês me deem essa chance."

    "{i}Clap clap clap{/i}"

    "DJ" "Isso aí! E agora música!"

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    "Caramba... a Zaza não tá brincando."

    "Ela realmente quer fazer parte do Grupo..."

    "E-epa! Parece que o prefeito e a Natasha também tão aqui!"

    menu:
        "Chegar perto tentando não ser visto":


            "Eu preciso tentar..."

            scene black with dissolve

            scene n8i13 with Dissolve(1.0)

            pause 2.0

            za "Prefeito, 0 senhor está gostando da festa?"

            pr "Está tudo muito bem organizado, Verônica. Parabéns."

            za "Obrigada. E o que o senhor achou do meu discurso?"

            pr "Foi... inspirador. Você realmente tem uma visão para a Blergh!."

            za "Eu acredito que a Blergh! pode ser um pilar de força para a Capital. E eu espero que o senhor e o Grupo concordem comigo."

            na "..."

            pr "Verônica, você sabe que o Grupo é uma organização... tradicional."

            za "Tradicional..."

            pr "Sim. Nós valorizamos a experiência, a sabedoria. E, para ser franco, você ainda é muito... inexperiente."

            za "Mas eu tenho a força, a inteligência e a determinação para fazer parte do Grupo."

            pr "Eu não duvido disso. Mas o Grupo precisa de pessoas que... que saibam seu lugar."

            za "O que o senhor quer dizer com isso?"

            pr "Quero dizer que... o Grupo precisa de pessoas que... que não queiram mudar as coisas."

            za "Mas eu quero mudar as coisas para melhor! Eu quero tornar a Capital um lugar melhor para todos!"

            pr "E quem decide o que é melhor para a Capital?"

            za "O Grupo, é claro. Mas eu acredito que posso ser uma voz importante dentro do Grupo."

            pr "Verônica, você é uma... mulher... ambiciosa. Mas o Grupo não precisa de ambição. O Grupo precisa de estabilidade."

            za "Mas..."

            pr "Não se preocupe. Você ainda vai entender. Tem muito tempo para aprender como as coisas funcionam."

            scene black with dissolve

            scene n8i14 with Dissolve(1.0)

            pause 2.0

            na "Com licença, senhor prefeito, mas a senhora Zaza tem razão. A Blergh! está crescendo rapidamente e se tornando uma força importante na cidade."

            pr "Natasha, você sabe que eu valorizo sua opinião, mas o Grupo já decidiu."

            na "Sim, senhor. Mas eu acredito que seria um erro subestimar a senhora Zaza e a Blergh!."

            na "O senhor é a voz mais sensata e... dominante. Eles vão te ouvir."

            za "..."

            pr "Muito bem. Verônica, eu vou reconsiderar sua proposta. Mas não espere uma resposta imediata."

            za "Obrigada, prefeito."

            pr "Agradeça ao olhar da Natasha. Ela tem um feeling que dificilmente erra."

            pr "Agora me deem licença."

            scene black with dissolve

            scene n8i15 with Dissolve(1.0)

            pause 2.0

            za "Obrigada por me defender, Natasha."

            na "Não foi nada. Eu só disse o que eu acho que é certo."

            za "Você é uma mulher corajosa."

            na "Eu aprendi com os melhores."

            za "Heh..."

            za "Espero que um dia você possa se juntar a mim, Cássa e à Miranda. Juntas, podemos mudar a forma como o Grupo vê as mulheres."

            na "Eu... eu vou pensar sobre isso."

            za "Você sabe o que eles fazem."

            na "..."

            za "Não precisa fazer essa cara. Eu não estou em lugar para julgar ninguém."

            za "Mas nem todas as tradições são positivas. Será que não é hora de mudar?"

            na "Você sabe minha opinião."

            za "Eu sei. Ele me disse."

            na "Ele não devia ter dito... eu... eu não tenho nada com isso."

            "Do que elas tão falando? Quem é 'ele'?"

            za "Talvez eu possa ajudar. Mas... você precisa decidir."

            na "Apenas... deixe as coisas como estão."

            za "Se você quer assim..."

            scene black with dissolve

            scene n8i16 with Dissolve(1.0)

            "O prefeito realmente escuta a Natasha. Ela até parece aquele conselheiro do rei em O Senhor dos Anéis, falando no ouvido dele."

            "A Natasha com certeza é um mistério. Qual o objetivo dela nisso tudo?"

            na "[mc]... você também tá aqui."

            mc "E-epa."

            na "Não precisa se assustar. Só estou... surpresa."

            mc "É... surpresa... haha..."

            "Caralho... a Natasha... ela me viu!"

            "Ela tava lá com o prefeito... e agora tá aqui comigo..."

            "E essa roupa ridícula... ela deve tá rindo de mim por dentro..."

            na "Pode me ajudar?"

            mc "O-opa..."

            scene black with dissolve

            scene n8i17 with Dissolve(1.0)

            pause 2.0

            "Segurar a mão dela assim... tá gelada."

            na "Primeiro o Cassino do Barão... agora a festa da Blergh!... você realmente gosta de se misturar com a alta sociedade, não é, [mc]?"

            "Droga... o que eu falo pra ela?"

            "Essa história da mão foi pra me desarmar? N-não posso deixar tudo acabar assim!"

            menu:
                "Tô fazendo um bico como garçom. Preciso da grana.":


                    mc "Haha... tô fazendo um bico como garçom, sabe? Preciso da grana..."

                    na "Sério? Você? Garçom?"

                    mc "É... a vida não tá fácil... haha..."

                    na "Entendo..."

                    "Ela não acreditou em mim... mas pelo menos desviou do assunto..."
                "Tô atrás de uma pauta.":


                    mc "Esses eventos são cheios de podres, sabe como é..."

                    na "Hmm... imagino..."

                    na " E pelo visto você já encontrou algo interessante..."

                    mc "É... a noite tá só começando..."

                    na "Espero que você esteja pronto para as consequências..."

                    "Ela tá me ameaçando?"
                "Vim acompanhar um amigo.":


                    mc "Ele é modelo da Blergh!."

                    na "Ah, sim... interessante..."

                    na "Espero que seu amigo esteja ciente de com quem está se metendo..."

                    "Ela tá falando do Grupo?"

                    mc "É... ele é meio ingênuo..."

                    na "Todos nós somos, no começo..."

                    "O que ela quis dizer com isso?"

            if diana_final2:

                mc "Hmm..."

                "A Natasha... ela me levou até o ponto de ônibus... e o Tony e o Marco apareceram logo depois..."

                "Será que... foi ela que avisou eles?"

                "Não é possível... ela ia me trair desse jeito? Depois de salvar a Diana? Impossível."

                "Ela disse que ia me ajudar... que ia falar com o prefeito..."

                "Mas... e se ela tiver me enganado?"

                "Aquela ligação que ela fez..."

                "Pra quem ela ligou?"

                "Será que... foi pro Tony?"

                "Não... não pode ser..."

                "Eu confiei nela..."

                "Mas... e se eu tiver errado? E se ela no fundo realmente não tiver coração?"

                menu:
                    "Natasha... foi você que avisou o Tony?":


                        mc "Natasha... foi você que avisou o Tony?"

                        "Eu encaro aqueles olhos claros penetrantes... sem se alterar, tudo o que ela faz é apenas arquear uma sobrancelha."

                        na "Do que você está falando, [mc]?"

                        "Ela tá tão calma... será que é só uma máscara?"

                        mc "Você me deixou no ponto de ônibus... e eles apareceram logo depois..."

                        na "Eles?"

                        mc "Você sabe... eu quero saber... você fez uma ligação antes da gente voltar pra ilha."

                        na "Sim. Eu fiz. E daí?"

                        mc "Pra quem você ligou? Pro Tony? Foi você que me entregou?"

                        na "Eu trabalho pro prefeito, não pro Tony. Você realmente acha que eu arriscaria minha posição?"

                        mc "Mas-"

                        na "O prefeito Donatello tem seus acordos com o Tony, sim. Mas isso não me torna uma traidora."

                        scene black with dissolve

                        scene n8i18 with Dissolve(1.0)

                        pause 2.0

                        "Os olhos dela... eles parecem me atravessar... como se ela pudesse ler meus pensamentos..."

                        na "Eu liguei para o prefeito. Precisava avisá-lo que eu estava usando o avião dele para... resolver um assunto pessoal."

                        mc "O avião... a Diana... então foi por isso."

                        na "Sim. Eu não podia arriscar que ele descobrisse da forma errada. A segurança do aeroporto é leal a ele, como você deve saber."

                        mc "..."

                        "Ela tá falando a verdade? Ou é só mais uma mentira?"

                        "Ela é uma atriz e tanto... eu não consigo decifrar."

                        "Meu futuro... depende dessa decisão."

                        menu:
                            "Eu acredito em você, Natasha.":


                                "Forço um sorriso, tentando afastar o medo."

                                mc "Tudo bem... eu acredito em você, Natasha."

                                na "Inteligente..."
                            "Você tá mentindo.":


                                mc "(Apertado a mochila com força, sentindo a raiva me dominar) Eu não acredito em você, Natasha. Você tá mentindo."

                                na "(Com um sorriso frio e ameaçador) Cuidado com suas acusações, [mc]. Você não sabe com quem está lidando..."

                "Mas isso não explica a Diana. Por que ela continua sendo secretária dele?"

                "Não era pro Donatello ter punido ela por ajudar a Diana a fugir?"

                "A Diana é uma sacerdotisa! Uma peça importante pros planos do Grupo!"

                if black_salva == 2:

                    "Será que foi o Distrito? O Black Cash salvou ela igual ele me prometeu?"

                "A Natasha... ela arriscou tudo pra ajudar a gente... mas por quê?"

                "E como que ela se safou dessa?"

                mc "Natasha... como você conseguiu se safar? O prefeito... ele não te puniu?"

                na "Donatello é um homem pragmático, [mc]... ele sabe reconhecer o valor de uma aliada leal... mesmo quando ela toma decisões... questionáveis."

                "Ela tá me enrolando... não tá me contando a verdade..."

                "O que ela fez? O que ela ofereceu ao prefeito em troca da liberdade dela?"

                "A Natasha... ela sempre foi um mistério... mas agora..."

                "Ela parece ainda mais perigosa..."

                mc "O que você fez, Natasha?"

                na "Isso não é da sua conta, [mc]. Mas acredite... eu sempre consigo o que quero."

                mc "Hm?!"

                "Eu... nunca vi ela falando assim. Me deixou sem resposta... com a pulga atrás da orelha."

                "A Natasha... ela não é só uma secretária... ela é uma jogadora."

                "E eu não sei se ela tá do meu lado... ou contra mim..."
            else:


                na "[mc]... você também tá aqui."

                "Caralho... a Natasha... ela me viu!"

                na "Pode me ajudar?"

                mc "O-opa..."

                scene black with dissolve

                scene n8i17 with Dissolve(1.0)

                pause 2.0

                "Segurar a mão dela assim... tá gelada."

                na "Não precisa se assustar. Só estou... surpresa."

                mc "É... surpresa... haha..."

                "Surpresa? Ela deve estar é se divertindo com essa minha roupa ridícula..."

                na "Primeiro o Cassino do Barão... agora a festa da Blergh!... você realmente gosta de se misturar com a alta sociedade, não é, [mc]?"

                mc "Haha... é... tô tentando expandir meus horizontes, sabe como é..."

                na "Parece que você está se saindo bem... principalmente com esse uniforme charmoso de garçom."

                mc "Haha... é... tô me virando..."

                "Ela tá me provocando... mas eu não posso vacilar... ela é a secretária do prefeito, e faz parte do Grupo..."

                na "Você sabe que o prefeito Donatello está de olho em você, não sabe?"

                mc "O prefeito? De olho em mim?"

                mc "Sério? Mas... por quê?"

                na "Você tem talento, [mc]. E coragem. Qualidades que o Grupo admira..."

                mc "O Grupo... então eles estão me avaliando mesmo?"

                if diana_grupo:

                    "Eu fui pra reunião com o Tony e o Barão, eu sabia que aquilo não era um convite comum."

                    "Eles realmente querem me dar uma chance!"

                    if grupo_nathan >= 1:

                        "E eu ter aceitado fazer a cabeça do Nathan... isso vai contar MUITOS pontos."

                "Caralho... será que essa é minha chance?"

                "Entrar pro Grupo... ter o poder da cidade nas minhas mãos..."

                if grupo_nathan < 1:

                    "Mas... e o Nathan? E o nosso plano?"

                    "Não... eu não posso desistir agora... mas também não posso ignorar essa oportunidade..."

                na "Você precisa tomar cuidado, [mc]. Essa cidade não é para amadores. Se você quer jogar esse jogo, precisa conhecer as regras."

                mc "Eu... eu tô aprendendo..."

                scene black with dissolve

                scene n8i18 with Dissolve(1.0)

                pause 2.0

                na "Eu posso te ensinar..."

                "Ela tá flertando comigo? Sério?"

                menu:
                    "Eu adoraria aprender com você, Natasha.":


                        mc "Eu adoraria aprender com você, Natasha."

                        "Ela se aproxima ainda mais, com um olhar penetrante."

                        na "Quem sabe um dia desses... depois que você provar seu valor..."

                        mc "Eu vou provar..."
                    "Eu prefiro aprender sozinho.":


                        mc "Eu prefiro aprender sozinho, Natasha. Obrigado pela oferta."

                        na "Como quiser, [mc]. Mas não diga que eu não avisei..."

            na "Enfim... Donatello precisa de mim."

            "Ela diz com um tom de voz baixo e intenso, quase um sussurro."

            na "Me diga, [mc]... você realmente sabe o que está fazendo?"

            "O que ela quer dizer com isso?"

            "Ela tá me avaliando... analisando cada movimento meu..."

            na "Trabalhar ou desafiar essas pessoas... o Grupo... é um contrato faustiano, sabia?"

            "Faustiano?"

            na "Você precisa estar pronto para doar a alma."

            "Olha o olhar dela... distante... melancólico... como se estivesse revivendo alguma lembrança dolorosa."

            "Será que... ela se arrepende de ter se juntado ao Grupo?"

            "A Natasha... essa mulher fria e calculista... ela também tem seus demônios?"

            na "Só digo... para que você tenha certeza. Para que não se arrependa depois."

            "Ela tá lutando pra conquistar seu lugar... lutando pra ser a secretária do prefeito... talvez a mulher mais poderosa da capital..."

            "Será que ela teve que pagar um preço por isso?"

            na "Adeus, [mc]."

            mc "Adeus..."

            scene black with dissolve

            scene n8i16 with Dissolve(1.0)

            "Qual foi o preço, Natasha? Eu quero saber..."
        "Ir atrás do Nathan e da Cássia":


            scene black with dissolve

            scene n8i16 with Dissolve(1.0)

            "Eu não tenho tempo pra isso. Preciso encontrar o N-"

    mc "Hm?!"

    "Caralho! Olha lá! O Nathan e a Cássia."

    "Eles tão conversando... bem próximos... ela tá rindo do que ele tá falando."

    "Parece que o plano dele tá funcionando..."

    "Tomara que ele não se esqueça do que a gente combinou."

    menu:
        "Se aproximar para tentar ouvir a conversa dos dois":


            "Eu preciso ver..."

            scene black with dissolve

            scene n8i19 with Dissolve(1.0)

            pause 2.0

            n "Cássia, você tá deslumbrante esta noite."

            j "Obrigada, Nathan. Você também tá um tesão, pombinho."

            n "Eu queria poder conversar com você a sós."

            "Cássia levanta uma sobrancelha."

            j "Sobre o quê?"

            n "Sobre... o futuro."

            j "O futuro? Que futuro?"

            n "O futuro da Blergh!. O futuro... nosso."

            j "Você está me provocando, Nathan?"

            n "Talvez."

            j "E o que você quer de mim?"

            n "Eu quero... que você me ajude a realizar meu sonho."

            j "E qual é o seu sonho?"

            n "Eu quero ser um modelo de sucesso. Eu quero ser famoso. Eu quero ter tudo."

            j "E você acha que eu posso te ajudar com isso?"

            n "Eu sei que você pode. Você é uma das pessoas mais lindas e influentes da Capital."

            scene black with dissolve

            scene n8i20 with Dissolve(1.0)

            pause 2.0

            j "E o que eu ganho com isso?"

            n "Você ganha... a mim."

            "Cássia ri."

            j "Você é um tesão, Nathan. Mas eu não sou uma idiota que se deixa levar por um bebê gostoso."

            "Merda! Ela não vai cair nessa! Ela é esperta demais."

            n "Eu sei que você não é. Mas eu também sei que você me quer."

            "Cássia desvia o olhar."

            n "Eu posso ver em seus olhos."

            j "E o que você quer que eu faça?"

            n "Eu quero que você me leve em um lugar sem ninguém.."

            j "Por quê?"

            n "Eu preciso... te mostrar uma coisa. Uma coisa que eu tenho aqui só pra você."

            j "E o que é, meu amor?"

            n "É... uma surpresa."

            j "Você é sedutor, Nathan. Mas eu não sou idiota."

            n "Eu sei. Mas eu também sei que você não pode resistir a mim."

            scene black with dissolve

            scene n8i19 with Dissolve(1.0)

            "Cássia se inclina no Nathan de novo seus lábios roçando os dele."

            j "Você está certo."

            mc "Q-quê?!"

            n "Você não vai se arrepender."

            j "Eu sei que só tem desgraça pra mim neste caminho... mas... você sempre foi minha fraqueza."

            n "Xiii... guarda energia. Vem."

            j "Safado..."
        "Manter distância e esperar":


            "Melhor não correr riscos desnecessários."

            "Vou esperar até que... hm?!"

    "Droga... eles tão saindo pela porta. Será que ele conseguiu? Vai levar ela na sala da Zaza?!"

    scene black with dissolve

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    scene n8i21 with Dissolve(1.0)

    pause 2.0

    "Preciso ser discreto. Se a Zaza, Roxane ou alguém me pegar aqui..."

    "O corredor tá vazio, só garotas andando pra cá e pra lá. E uns quadros estranhos na parede. Parece até um museu."

    "Ei... aquela porta ali tá aberta..."

    "Consigo ouvir vozes femininas... modelos? Se trocando?! O que elas tão falando?"

    menu:
        "Parar e tentar olhar pela fresta...":


            "Vou dar uma olhada rápida..."

            scene black with dissolve

            scene n8i22 with Dissolve(1.0)

            pause 2.0

            "Modelo Loira" "A Zaza é incrível, né? Ela me ensinou tanta coisa..."

            ro "Verdade. Ela me deu a coragem de seguir meu sonho de ser modelo. Meus pais nunca ligaram pra mim..."

            "Roxane?!"

            "Modelo Loira" "A minha família também não apoiava minha carreira. Mas a Zaza me mostrou que eu podia ser uma mulher forte e independente."

            ro "Ela é tipo uma mãe pra gente, né? Sempre cuidando e dando conselhos."

            "Modelo Loira" "Lembra da Mel? Ela tava toda insegura no começo. A Zaza deu a maior força pra ela. E ela arrasou!"

            ro "Verdade! Ela foi um exemplo... pena que... enfim. Ela é um exemplo pra todas nós."

            "Modelo Loira" "A Zaza realmente se importa com a gente. Ela quer ver todas nós brilhando."

            ro "Eu sou muito grata a ela por tudo."

            "Zaza... quem não te conhece que te compre."

            play sound som_35_passos

            scene black with dissolve

            "Preciso ir... o Nathan e a Cássia..."

            scene n8i21 with Dissolve(1.0)
        "Agora não é hora disso! Prosseguir":


            mc "Melhor não perder tempo. Preciso focar no Nathan."

    "Cada passo ecoa no corredor... parece que o som tá amplificado. Tô suando frio..."

    "???" "Ei, você! Garçom!"

    mc "!!!"

    "Modelo" "Pode me trazer uma taça de champanhe? Essa festa tá me matando de sede."

    mc angustiado "Eu... hã..."

    menu:
        "Claro, amor.":


            mc "Claro. Já trago pra você."

            "Modelo" "Obrigada. Eu tô ali naquela porta, viu?"

            mc "Pode deixar! Hehe..."

            "Preciso achar a cozinha... e rápido..."

            "Não... o que eu tô falando?!"
        "Desculpa, mas eu não sou garçom.":


            "Modelo" "Não? Mas essa roupa... Ah... tá. Desculpa."

            "Será que eu me ferrei?"

    play sound som_35_passos

    "Preciso continuar seguindo o Nathan e a Cássia... antes que eu perca minha chance."

    "Eles entraram naquela porta ali... a sala da Zaza."

    "Meu coração tá disparado... se alguém me pegar agora..."

    scene black with dissolve

    scene n8_img7 with Dissolve(2.0)

    "A porta tá... entreaberta..."

    "Merda... ele tá mesmo fazendo isso..."

    menu:
        "Ficar aqui e olhar pela fresta da porta (+18)":


            show black with dissolve

            mc "Não acredito... eles tão..."

            scene black with dissolve

            scene nathan_extra1 with Dissolve(1.0)

            j "Nathan... o que você tá fazendo? Do nada você resolveu me trazer aqui? Pensei que você me odiasse."

            n "Você sabe que não é bem assim, Cássia..."

            j "Não? Você sempre me tratou com desdém. Como se eu fosse um inseto no seu sapato impecável."

            n "Você me fascina, Cássia. Sempre fascinou."

            "Eu sempre soube que a Cássia tinha algo com o Nathan..."

            j "Ah, Nathan... você é tão bom em mentir. Mas eu gosto disso em você."

            n "Não estou mentindo. Você me intriga. Essa força, essa sua ambição..."

            j "Pare de mentir. Você gosta do pombinho, o jornalista, aquele [mc]."

            n "Mas ele não me atrai como você. Vem cá."

            j "Você realmente acha isso atraente? A maioria dos homens foge de mulheres como eu."

            n "Eu não sou como a maioria dos homens. Eu gosto de mulheres que sabem o que querem. Mulheres que não têm medo de tomar o poder."

            j "E o que você quer, Nathan?"

            scene black with dissolve

            scene nathan_extra2 with Dissolve(1.0)

            j "Ai..."

            n "Eu quero você, Cássia. Aqui. Agora."

            "Se ele nunca deu bola pra ela... por que ela ia acreditar agora?"

            j "Você acha que eu sou boba. Você não é um homem movido pelo desejo dessa forma."

            n "O que você tem a perder?"

            j "..."

            n "Agora posso te mostrar o que você tem a ganhar..."



            j "Safado. ME mostra então, Nathan..."

            "Caralho... ele não tá brincando..."

            scene black with dissolve

            scene nathan_extra3 with Dissolve(1.0)

            j "Nathan... por que você tá fazendo isso? Do nada você resolveu ficar comigo?"

            n "Cássia... cala a boca e aproveita."

            j "Mas... eu não entendo... você parecia me odiar. Será que esse ódio todo era só tesão?"

            n "Você fala demais... para com isso."

            j "Você me lembra uma garota que trabalha comigo... ela também fala que me odeia, mas..."

            n "Já falei pra calar a boca! Agora vem aqui e chupa meu pau."

            menu:
                "Continuar olhando o que acontece (+18)":




                    "Eles só não podem me ver aqui..."

                    "A Cássia ajoelhada na frente dele... olhando pra ele com esse olhar faminto... como se quisesse devorar ele inteiro."

                    n "Isso... chupa minha rola, Cássia... quero sentir sua boca nela."

                    j "Com prazer, meu homem."

                    show black with dissolve

                    "Ela abriu a boca... e... caralho..."

                    scene nathan_extra4 with Dissolve(1.0)

                    j "Hmmm... você é tão gostoso, Nathan... tão grande..."

                    n "Porra... Cássia... você chupa bem pra caralho..."

                    j "Hmmm... adoro chupar um pau gostoso... ainda mais de um homem que sabe ser grosso."

                    n "Aah... mais rápido... me fode com essa boca gostosa."

                    "Ela tá acelerando... os gemidos dela tão cada vez mais altos... ele tá quase gozando..."

                    n "Cássia... eu vou... aahh..."

                    j "Não aguenta a boca da sua puta, é?"

                    n "Ahn... isso... continua..."

                    "A Cássia é sempre tão autoritária, mandona. Por que ela tá entrando nessa onda?"

                    "Ela tá chupando ele com tanta vontade... com tanta força... parece que quer engolir ele inteiro."

                    "E eu aqui... assistindo tudo... caralho... meu pau ficando duro dentro da calça..."

                    j "Aah... Nathan... você me deixa tão molhada com essa rola enorme, esses músculos, essa voz rouca de macho."

                    n "E você geme pra mim, sua vadia. Quero ouvir você gostando."

                    scene black with dissolve

                    scene nathan_extra5 with Dissolve(1.0)

                    j "Hmm... quer ver eu gozar com você na minha boca?"

                    "Ela tá acelerando... chupando com mais força... ele tá quase..."

                    n "Cássia... eu vou... aahh..."

                    j "Goza na minha boca, Nathan... me enche com sua porra."

                    scene nathan_extra5 with hpunch

                    n "Aaaaaahhh!!!"

                    "Ele gozou... na boca dela... ela engoliu tudo..."

                    j "Hmmm... delícia..."

                    j "Hmmm... adoro o gosto da sua porra..."

                    n "Agora é sua vez, Cássia..."

                    j "Nathan... me fode... me fode agora..."

                    n "Aqui não, Cássia. A Zaza..."
                "Se esconder e esperar uma chance de entrar":


                    "Eu não vou ver isso."

                    scene black with dissolve

                    scene n8i22 with Dissolve(1.0)
        "Se esconder e esperar uma chance de entrar na sala":


            scene black with dissolve

            scene n8i22 with Dissolve(1.0)

            "Vou ficar aqui. Esperar eles saírem."

    j "Foda-se a Zaza! Eu quero você dentro de mim! Agora!"

    mc "A-ah!"

    n "Mas..."

    j "Você não tá duro? Uma vez foi suficiente? Não quer me foder?"

    n "Claro que eu quero... mas..."

    j "Então vem..."

    n "Tá bom... vamos. Mas não aqui. Não onde a Zaza possa pegar a gente."

    j "Você quer mesmo me comer no banheiro?"

    n "Quer meu caralho nessa buceta suja ou não?"

    j "Você é terrível, gostoso. Vem logo!"

    "Ops..."

    show black with dissolve

    play sound som_35_passos

    pause 2.0

    "Eles saíram correndo da sala... a porta ficou aberta..."

    mc "Ele conseguiu! É minha chance!"

    scene n8i23 with Dissolve(1.0)

    pause 2.0



    "Entrei. Vou fechar aqui pra ninguém desconfiar."

    "E se eles voltarem? Pior e se a Zazá vier pra cá? Preciso ser rápido."

    "A sala é enorme... e luxuosa... parece até a sala de um filme."

    "Tem quadros abstratos nas paredes, móveis de design... e um tapete gigante que deve custar mais que meu salário anual."

    "Mas cadê o cofre? Ela não ia deixar uma coisa dessas à vista, né?"

    "Vou ter que procurar..."

    label n8_procura_cofre:

        pass

    menu:
        "Atrás dos quadros":


            "{i}Tchak tchak{/i}"

            mc "Não!"

            jump n8_procura_cofre
        "Embaixo do tapete":


            "{i}Tchak tchak{/i}"

            mc "Não!"

            jump n8_procura_cofre
        "Em baixo do móvel":


            pass

    "Droga... onde essa mulher escondeu essa porra?!"

    "Espera... ali..."

    scene black with dissolve

    scene n8i24 with Dissolve(1.0)

    "Um cofre... não parece tão grande... mas com certeza bem seguro."

    "Preciso da senha... qual será que é?"

    menu:
        "A Roxane disse que ela é a coisa mais importante da Zaza.":


            pass

    "Que elas são mãe e filha."

    "Será que... será que a senha do cofre tem algo a ver com a Roxane?"

    "Mas o quê?"

    "A Roxane... a chupeta que ela usa... sempre fiquei pensando nisso."

    "Talvez ela nunca tenha superado a infância. Ou ela usa pra lembrar..."

    "Lembrar do dia que elas se conheceram. O dia que ela conheceu quem mudou a vida dela."

    "A Roxane tava no orfanato... e a Zaza foi lá buscar ela... salvar ela. A Roxane nunca esqueceu isso."

    "Droga... preciso me acalmar... a senha... tem que ter alguma lógica."

    "E se... a senha for a data que a Zaza conheceu a Roxane? Quando as duas iniciaram sua família?"

    mc "A chupeta... a Roxane usa pra lembrar do dia que foi adotada... isso não sai da minha cabeça. É uma forma de honraria."

    "E a senha é a forma que a Zaza honra a Roxane."



    mc surpreso "E SE?!"

    "É isso! A senha é a data que a Zaza pegou a Roxane no orfanato!"

    menu:
        "Faz todo sentido!":


            "Sim! A Roxane é tudo pra ela! A data que elas se conheceram... essa deve ser a senha!"
        "Não... a Zaza não é sentimental... ela é ambiciosa. É a Blergh!.":


            "A Zaza... ela é fria, calculista... não acho que ela usaria algo tão pessoal como senha."

            "A Roxane disse que a Zaza a criou... mas no discurso ela disse que a Blergh! é como uma filha pra ela."

            "Ela é obcecada pela Blergh!... e se a senha for a data de fundação da empresa?"

            "Eu ouvi ela falando no discurso dela..."

    "Pensa, [mc], pensa..."

    "Faz sentido... a Roxane é a filha dela... e a Blergh! também... as duas são como filhas gêmeas."

    "Apenas uma das duas é a certa. Se eu errar, talvez toque um alerta e tudo vá pro esculacho."

    "Preciso escolher..."

    "Tudo vai ser resolvido nesta escolha."

    menu:
        "A data que a Roxane foi adotada":


            mc "É isso! A data que a Zaza pegou a Roxane no orfanato! Tem que ser!"

            mc "A Roxane é como uma filha pra ela... a senha tem que ser essa!"

            mc "Deixa eu ver... são 6 dígitos. 12 de maio de 2007... 12... 05... 07..."

            "Bip... bip... bip..."
        "A data da fundação da Blergh!":


            mc "Não... a Zaza não é sentimental! Ela é obcecada pela Blergh!! A senha tem que ser a data de fundação!"

            mc "Foi o que ela disse no discurso... são 6 dígitos. 13 de maio de 2007... 13... 05... 07..."

            "Bip... bip... bip..."

    $ renpy.block_rollback()



    scene n8i25 with hpunch

    mc "AAAH!"

    ro "[mc]?!"

    mc "R-roxane?!"

    ro "O que você tá fazendo aqui?!"

    "Merda... ela me pegou..."

    ro "Eu sabia que você tava aprontando! Eu te vi saindo da festa com o Nathan!"

    mc "Eu... eu posso explicar..."

    ro "Explicar o quê?! Que você tá tentando roubar a Zaza?!"

    mc "Não... eu..."

    ro "Você é um traidor! Você prometeu que ia me deixar em paz!"

    mc "Roxane, por favor... você não tá entendendo..."

    ro "Não tô entendendo o quê?! Que você é um mentiroso?! Que você só quer se dar bem?!"

    mc "Não é isso! Eu tô fazendo isso pelo Nathan! A gente só qu-"

    ro "Eu não acredito mais em você! Você é igual a todos os outros! Só quer usar a gente!"

    ro "A Zaza é como uma mãe pra mim. Ela me deu tudo. Eu não posso deixar você fazer isso com ela."

    ro "Eu era órfã, [mc]. Eu não tinha ninguém. A Zaza me acolheu, me deu um lar, me ensinou tudo o que eu sei."

    ro "Ela me ensinou a ser forte, a ser independente, a lutar pelos meus sonhos."

    ro "Eu não posso deixar você destruir tudo o que ela construiu."

    mc "Roxane, me escuta..."

    mc "Roxane... você não entende. A Zaza... ela faz parte do Grupo."

    scene black with dissolve

    scene n8i26 with Dissolve(1.0)

    pause 2.0

    ro "E daí?! Ela não faz nada de ruim!"

    mc "Não? Essas são pessoas complicadas... que controlam a cidade. Eles estão por trás de tudo o que aconteceu com o Nathan."

    ro "Mas... a Zaza... ela me ajudou..."

    mc "Eu sei. Mas ela também tá envolvida com pessoas que exploram, ameaçam, prostituem, com drogas, coisa ruim de verdade!"

    ro "Mas... a Zaza não faz nada disso."

    mc "Eu... eu sei. Mas eu sei que o que eles tão fazendo não tá certo."

    ro "Ela é minha mãe, [mc]. Eu não posso simplesmente abandonar ela."

    ro "O que você quer que eu faça?"

    mc "Eu quero que você volte pro Distrito. Pra sua família."

    ro "Mas eu não quero voltar! Eu quero ser modelo! Eu quero ficar com a Zaza!"

    mc "Roxane... por favor..."

    ro "Sai daqui! AGORA!"

    mc "Mas..."

    ro "Se você não sair, eu vou chamar a segurança! E vou contar tudo pro Grupo! Você vai se arrepender de ter nascido!"

    mc "..."

    "Ela tá falando sério... se eu não der o fora daqui agora..."

    "Mas e o Nathan? E nosso plano? E a nossa liberdade?"

    "Eu não posso desistir agora... mas também não quero acabar na cadeia..."

    "O que eu faço?"

    label nathan_final_roxane1:

        pass

    menu:
        "Confrontar Roxane e continuar com o plano":


            mc "Roxane, eu vou fazer isso!"

            ro "O quê?!"

            mc "Você não vai me impedir de fazer isso!"

            ro "Você tá louco! Você vai se arrepender!"

        "Desistir do plano, trair Nathan e não arriscar a liberdade" if not nathan_final_desistiu2:

            $ nathan_final_desistiu = True

            "Eu não vou fazer essa loucura. Eu vou convencer o Nathan a ficar na Blergh!"

            "É traidor... mas eu não arrisco minha vida. E ainda posso me dar bem com a Zaza."

            mc "Roxane... você tem razão. Eu... eu fiz uma besteira."

            ro "Sai daqui então! E nunca mais volte!"

            "Vou pegar o Nathan na festa e falar a sós com ele no banheiro."

            scene black with dissolve

            scene n8i37 with Dissolve(1.0)

            mc "N-nathan! Presta atenção!"

            n "Hm?! [mc]?"

            mc "Vem cá!"

            n "O-ok..."

            scene black with dissolve

            scene n8i7 with Dissolve(1.0)

            "Não acredito que eu vou fazer ele ficar na Blergh... ok... tá decidido."

            n "[mc]?"

            mc "[n]!"

            jump nathan_final3





    scene n8i24 with hpunch

    ro "Não acredito! Você..."

    mc "A Zaza e o Grupo merecem isso!"

    ro "Você... você é um monstro! Eu confiei em você!"

    mc "Eu não tenho tempo pra isso, Roxane!"

    ro "Eu vou te denunciar! Pra polícia! Pro Grupo!"

    mc "Pode fazer o que quiser! Eu não ligo mais!"

    "Agora é terminar os 3 dígitos!"

    "Bip... bip... bip...!"

    "{i}DERÓN{/i}"

    mc "NÃO!"

    ro "Hm?! Você não sabe a senha?! E-eu tinha certeza..."

    ro "Hahaha! Que patético! Você realmente achou que ia conseguir?!"

    scene black with dissolve

    scene n8i28 with Dissolve(1.0)

    pause 2.0

    mc "Não... não pode ser..."

    ro "Você contou com os ovos antes da galinha, meu bem. A Zaza não é idiota."

    mc "A senha... errei a senha... era a outra!"

    "Acabou... tudo acabou..."

    "Eu falhei... com o Nathan... comigo mesmo."

    "A Roxane vai me entregar pro Grupo... eles vão me matar..."

    "O Tony... o prefeito... a Cássia... a Zaza..."

    "Eles vão me torturar... me fazer sofrer... e eu vou morrer..."

    "E tudo por causa da minha ambição... da minha estupidez."

    "Eu devia ter ficado na ilha... com a minha vida... eu não devia ter me metido nessa."

    "Achando que eu sou um tipo de agente..."

    "Agora é tarde demais..."

    "Eu tô... com tanto medo..."

    "Não quero morrer..."

    "Alguém... me ajuda..."

    "..."

    ro "[mc]..."

    scene black with dissolve

    scene n8i27 with Dissolve(1.0)

    pause 2.0

    ro "Levanta daí, cara."

    mc "Roxane..."

    "Ela... ela não tá rindo de mim?"

    ro "Você sempre foi legal comigo. Mesmo eu dizendo 'não', você tentou me levar pro Distrito pra me ajudar."

    mc "Eu só queria..."

    ro "Eu sei... você queria me ajudar. Queria que eu voltasse pra minha comunidade."

    mc "Heh... Você não parece a Cássia e nem a Zaza sendo legal assim."

    ro "A Cássia... ela sempre foi assim. Fria, ambiciosa. Ela aprendeu com a Zaza a ser implacável."

    mc "Mas você também..."

    ro "A Zaza nos ensina a sermos mulheres fortes e determinadas, sim. Mas ela também diz que temos que ser nós mesmas."

    ro "Eu nunca vou ser como elas. Eu sempre vou ter um coração."

    mc "Roxane..."

    "Eu acho... que ela tá sendo sincera... eu consigo ver nos olhos dela."

    "Ela não tá mentindo... ela realmente se importa comigo."

    ro "E além do mais... eu não quero perder um peguete em potencial."

    mc "Haha..."

    ro "Que tal a gente esquecer tudo isso e tomar uma champanhe? Pra comemorar que você ainda tá vivo?"

    mc "Você diz... não envolver a Zaza e nem outros?"

    ro "Isso aí. Ninguém precisa saber o que rolou aqui."

    "Eu não acredito... ela tá me dando uma chance?"

    "Mas... e o Nathan? E o nosso plano?"

    "Eu posso trair ele... depois de tudo o que ele fez por mim?"

    "Aceitar o carinho da Roxane e deixar tudo de lado? Ou tentar a outra senha?"

    "Preciso escolher..."

    label nathan_final_roxane2:

        pass

    menu:

        "Aceitar as pazes com a Roxane" if not nathan_final_desistiu2:

            $ nathan_final_desistiu = True

            "Eu não vou fazer essa loucura. Eu vou convencer o Nathan a ficar na Blergh!"

            "É traidor... mas eu não arrisco minha vida. E ainda posso me dar bem com a Zaza."

            mc "Tá legal, Roxane. Champanhe parece uma boa ideia."

            ro "Ótimo. Vem comigo."

            mc "Eu só preciso... resolver uma coisa antes."

            ro "Ok..."

            "Vou pegar o Nathan na festa e falar a sós com ele no banheiro."

            scene black with dissolve

            scene n8i37 with Dissolve(1.0)

            mc "N-nathan! Presta atenção!"

            n "Hm?! [mc]?"

            mc "Vem cá!"

            n "O-ok..."

            scene black with dissolve

            scene n8i7 with Dissolve(1.0)

            "Não acredito que eu vou fazer ele ficar na Blergh... ok... tá decidido."

            n "[mc]?"

            mc "[n]!"

            jump nathan_final3
        "Insistir na outra senha":


            mc "Roxane, eu agradeço a oferta... mas eu ainda não terminei aqui."

            ro "Você tá louco! Eu devia te entregar pra Zaza agora mesmo!"

            mc "Eu sei... mas eu preciso fazer isso. Pelo Nathan."

            ro "O Nathan? Ele não vale a pena! Ele só quer usar você!"

            mc "Eu sei o que eu tô fazendo, Roxane. Por favor, me deixa em paz."

            ro "Você é um idiota! Você vai se arrepender disso!"

            mc "Preciso tentar a outra senha!"

    scene n8i24 with vpunch

    "Bip... bip... bip...!"

    ro "Pare!"

    mc "Roxane?! Eu não posso!"

    ro "Você... você não sabe a senha. Não é o que você tá pensando."

    mc "..."

    "Ela... ela sabe a senha?"

    scene black with dissolve

    scene n8i29 with Dissolve(1.0)

    pause 2.0

    ro "Por que você tá fazendo isso, [mc]? Por que você tá se arriscando tanto?!"

    mc "..."

    "Eu... eu não tenho escolha..."

    "Preciso contar a verdade pra ela..."

    "Mas... será que ela vai acreditar?"

    menu:
        "Roxane... eu... eu acredito que você é uma sacerdotisa.":


            pass

    ro "O quê?!"

    "É a única justificativa pra tudo o que tá acontecendo. Pra uma garota do Distrito tá aqui."

    "Posso tá falando merda... mas é minha única chance."

    mc "Se o que eu aprendi antes é verdade... então... dentro desse cofre... tem um contrato."

    ro "Contrato? Que contrato?"

    mc "Um contrato... firmado com seus pais... pra passar sua guarda pra Zaza."

    ro "Impossível! Meus pais... eles... eu tava no orfanato..."

    mc "Eu acho que isso é mentira, Roxane. Eles te venderam pra Zaza."

    scene n8i29 with hpunch

    ro "Não! Isso não é verdade! A Zaza me salvou! Ela me tirou do orfanato! Ela me deu uma vida!"

    mc "Roxane... pensa bem... a Zaza... ela é poderosa, influente... ela faz parte do Grupo..."

    mc "Por que ela ia adotar uma criança do nada? Sem querer nada em troca?"

    ro "..."

    "Ela tá... pensando..."

    "Será que eu consegui?"

    "Mas... e se eu tiver errado? E se não tiver nenhum contrato?"

    "Eu tô arriscando tudo... minha vida... minha liberdade..."

    "Mas essa é minha única chance..."

    mc "Roxane... eu sei que é difícil de acreditar... mas eu tô falando sério."

    mc "Eu vi como o Grupo opera. Eles usam as pessoas... manipulam... exploram."

    mc "Eles não se importam com ninguém... só com poder... com dinheiro."

    mc "A Zaza... ela pode ter te dado uma vida... mas a que preço?"

    mc "Ela te tirou da sua família... da sua comunidade... da sua identidade..."

    mc "Ela te transformou em... em um produto... uma ferramenta."

    mc "Ela te usa pra conseguir o que ela quer."

    mc "Roxane... você precisa abrir esse cofre... você precisa saber a verdade."

    ro "..."

    "Ela tá me olhando... com um olhar... indecifrável..."

    "Eu não sei se ela vai acreditar em mim..."

    "Mas eu preciso tentar..."

    mc "Roxane... por favor..."

    scene black with dissolve

    scene n8i30 with Dissolve(1.0)

    pause 2.0

    ro "{i}Puuufff...{/i}"

    ro "Me fala... qual é a senha? A senha que você ia tentar."

    mc "A senha... é a data-"

    ro "Não... não é isso."

    mc "Mas-"

    ro "A Zaza não é sentimental desse jeito. A senha... é algo muito mais importante pra ela."

    mc "O quê?"

    ro "É... meu corpo."

    mc "S-seu corpo?"

    ro "A Zaza... como estilista... ela sempre teve uma obsessão pelo meu corpo. Pelas minhas medidas."

    mc "..."

    ro "Ela diz que eu sou a personificação da beleza feminina... que minhas curvas são perfeitas..."

    ro "Ela atualiza a senha do cofre... pra minhas medidas... em centímetros."

    "Não acredito... ela tá falando sério?"

    ro "Noventa... sessenta... noventa."

    mc "Noventa... sessenta... noventa?"

    ro "Essas são minhas medidas. Busto, cintura, quadril. Em centímetros. Essa é a senha."

    mc "Então a senha é... 90 60 90?"

    ro "Sim. Digita essa senha no cofre."

    "90... 60... 90... essa combinação... faz sentido... a obsessão da Zaza pela perfeição..."

    "Por isso a Roxane é tão importante pra ela. Ela é a mulher perfeita."

    ro "Mas escuta bem, [mc]. Se você estiver mentindo... se não tiver nenhum contrato nesse cofre..."

    ro "Eu vou entregar sua cabeça de bandeja pro Grupo."

    ro "Eu não vou aceitar ter sido enganada dessa forma."

    mc "..."

    "Ela tá falando sério... eu consigo ver nos olhos dela..."

    "Eu arrisquei tudo... e agora..."

    "Preciso escolher..."

    label nathan_final_roxane3:

        pass

    menu:
        "Continuar e digitar a senha":


            mc "Ok... Eu não tô mentindo, Roxane. Confia em mim."

            scene black with dissolve

            scene n8i24 with Dissolve(1.0)

            "Bip bip bip..."

            ro "..."

            mc "..."

            "{i}CLICK{/i}"

            "Abriu!"

        "Parar e desistir do plano" if not nathan_final_desistiu2:

            $ nathan_final_desistiu = True

            "Eu não vou fazer essa loucura. Eu vou convencer o Nathan a ficar na Blergh!"

            "É traidor... mas eu não arrisco minha vida. E ainda posso me dar bem com a Zaza."

            mc "Roxane... eu... eu acho que eu prefiro o champagne."

            ro "Q-quê?!"

            mc "Não... eu... eu só..."

            ro "Você não pode falar uma coisa dessas e simplesmente desistir assim!"

            mc "Me escuta. Vai ser melhor pra todo mundo."

            ro "Você tem certeza?"

            mc "Sim. Sempre foi uma loucura. Você tá feliz, o Nathan também vai ficar."

            ro "Ok..."

            "Vou pegar o Nathan na festa e falar a sós com ele no banheiro."

            scene black with dissolve

            scene n8i37 with Dissolve(1.0)

            mc "N-nathan! Presta atenção!"

            n "Hm?! [mc]?"

            mc "Vem cá!"

            n "O-ok..."

            scene black with dissolve

            scene n8i7 with Dissolve(1.0)

            "Não acredito que eu vou fazer ele ficar na Blergh... ok... tá decidido."

            n "[mc]?"

            mc "[n]!"

            jump nathan_final3

    scene black with dissolve

    scene n8i31 with Dissolve(1.0)

    pause 2.0

    "Meu Deus..."

    "É dinheiro... muito dinheiro..."

    "Nunca vi tanto dinheiro na minha vida..."

    "Notas de 100... de 200..."

    "Pilhas e pilhas..."

    "A Roxane tinha razão... a Zaza guarda tudo aqui..."

    ro "Cadê o contrato, [mc]?"

    mc "Tô procurando..."

    "Dinheiro... mais dinheiro..."

    "Uma maleta... com mais dinheiro... e desenhos... parecem ser rascunhos da Zaza."

    "Modelos de roupas... estilos que ela criou..."

    "Caramba... ela é realmente talentosa..."

    "Mas... e o contrato?"

    menu:
        "Roxane... eu não tô encontrando...":


            pass
        "Ficar calado e continuar olhando":


            pass

    ro "Procura direito, [mc]. Você não me fez abrir esse cofre à toa."

    "Preciso achar esse contrato... antes que ela perca a paciência..."

    "Uma pasta embaixo da grana na maleta... essa é mais fina..."

    "Deixa eu ver... uma foto?"

    scene black with dissolve

    scene n8i33 with Dissolve(1.0)

    pause 2.0

    ro "S-sou eu... essa criança negra... de olhos arregalados... sou eu..."

    mc "Roxane..."

    "Atrás da foto... uma folha de papel amarelada... com letras miúdas e desbotadas..."

    mc "Tá vendo aqui?"

    ro "Lê... lê o que tá escrito aí! Vai!"

    menu:
        "Ler o contrato":


            mc "Contrato de entrega de *REMOVIDO* à custódia de *REMOVIDO* no processo do ritual *REMOVIDO*."

            ro "Sou eu e a Zaza..."

            mc "Todos os dados foram removidos de ambientes digitais. Apenas duas versões impressas do contrato ficaram disponíveis."

            mc "Uma para cada parte do acordo."

            mc "As partes se comprometem a manter sigilo absoluto quanto à transação, sob pena de sanções em caso de vazamento."

            mc "As partes reconhecem que este contrato não tem e não pode ter qualquer respaldo legal devido à natureza da transação."

            mc "O passado da garota também foi apagado para evitar que a mesma tenha qualquer chance de vazar o ocorrido."

            mc "Verônica ficará responsável por fazer a proteção da sacerdotisa."

            mc "O acordo firmado entre o Distrito e o Grupo estabelece que ambas as partes deverão receber uma promessa de fidelidade."

            mc "Dessa forma, a Cidade Chinesa funcionará como mediadora da transação."

            mc "A família *REMOVIDO* já entregou sua parte para os cuidados do mediador, que repassará assim que receber a contrapartida."

            mc "No caso da família *REMOVIDO*, o pagamento de propina mensal para a organização criminosa *REMOVIDO*, sediada no Distrito, foi acordado como contrapartida."

            mc "Parte do acordo estabelece que a família deverá deixar a capital e ir para local não descriminado."

            mc "A família também renega qualquer direito de contato com a parte a partir da assinatura deste instrumento."

            mc "A parte do Grupo do contrato ficará protegida em no cofre de um banco de segurança máxima."

            mc "Uma pessoa de confiança será designada para fazer a segurança pessoal e deverá responder caso o documento seja perdido."

            mc "Por fim, Verônica deverá fazer relatórios periódicos do desenvolvimento da sacerdotisa."

            mc "Ela deve apresentar plena saúde e desenvolvimento físico, mental e psicológico."

            mc "Falha em atender qualquer um dos parâmetros acordados acarretará em sanções extrajudiciais."

            mc "E, por estarem assim justos e contratados, firmam o presente contrato em duas vias de igual teor e forma."

            mc "E na presença das testemunhas, que subscrevem, obrigam-se, por si e seus sucessores, a cumprir o aqui disposto."

            mc "Roxane..."

            "Eu tava certo... ela é mesmo uma sacerdotisa..."

            "Eu sou um gênio!"

    menu:
        "Esse é o contrato que te vendeu pra Zaza.":


            pass

    if blergh_foto:

        "Preciso tirar uma foto disso... como prometi pro Black Cash e pra Madame Nora..."

        show white with dissolve

        hide white with dissolve

        "Pronto... agora eles têm a prova que precisam..."

        "Espero que isso realmente ajude a Roxane..."

    ro "Isso... isso é real?"

    mc "É, Roxane. É real."

    ro "Meus pais... eles... me venderam?"

    mc "Parece que sim."

    ro "Eu... eu não acredito..."

    scene black with dissolve

    scene n8i32 with Dissolve(1.0)

    pause 2.0

    mc "Roxane... escuta... não é a primeira vez que eu vejo isso."

    if julia_segredo:

        mc "A Júlia... a família dela fez a mesma coisa."

    if diana_final2:

        mc "A Diana também..."

    ro "O quê?"

    mc "Existem outras como você... sacerdotisas."

    ro "Sacerdotisas?"

    mc "Eu não sei exatamente o que isso significa... mas parece que o Grupo precisa de vocês pra alguma coisa."

    mc "Eles fazem contratos com as famílias... pagam propina pro Distrito... usam a Cidade Chinesa como mediadora."

    mc "Eles apagam o passado delas... as controlam... mas também as protegem."

    mc "Mas pra quê? Qual é o objetivo deles?"

    ro "..."

    "Ela tá em choque... sem conseguir processar tudo isso."

    "Eu não faço nem ideia do que ela tá sentindo..."

    mc "Roxane... a Zaza... ela nunca te disse nada sobre isso?"

    ro "Não... nunca..."

    "Uma lágrima escorre pelo rosto dela... ela tá tão frágil..."

    ro "Então... ela... ela nunca me amou? Ela só tava... seguindo ordens?"

    mc "..."

    "Essa pergunta... me corta o coração..."

    "Como eu posso responder isso?"

    "Eu não sei o que a Zaza sente... mas..."

    mc "Roxane... eu... eu não sei o que dizer..."

    mc "Mas... eu sei o que você precisa fazer."

    mc "Roxane... você precisa decidir. Você quer continuar do lado da Zaza... ou quer voltar pro Distrito?"

    ro "Eu preciso falar com ela. Preciso... colocar tudo isso em panos limpos."

    mc "Roxane... você tem certeza? E se ela-"

    ro "Eu não me importo mais com o Grupo! Com a Blergh!... com nada!"

    ro "Eu só quero saber a verdade! Quero saber se... se tudo o que ela me deu... foi só uma farsa!"

    "Ela tá em cacos... preciso sair daqui antes que a Zaza chegue..."

    mc "Roxane... me escuta... se a Zaza descobrir que eu tô aqui... que eu abri o cofre..."

    mc "Ela vai me matar! Ela... ela vai me entregar pro Grupo..."

    ro "Pega o dinheiro, [mc]. Foge com o Nathan."

    mc "O quê?"

    ro "Pega o dinheiro... e vai embora. Esquece essa cidade... esquece a gente..."

    mc "Espera... o que você tá dizendo?"

    "Ela tá... me deixando levar o dinheiro?"

    "Depois de tudo... depois de eu ter enganado ela... traído a confiança dela?"

    "Eu não acredito..."

    mc "Roxane... mas... e você?"

    ro "Eu vou dar um jeito... não se preocupa comigo..."

    ro "Aqui... pega a minha mochila... cabe mais dinheiro nela..."

    "Eu não consigo acreditar... ela tá... fazendo isso por mim?"

    mc "Roxane... eu... eu não sei o que dizer..."

    "Minha garganta tá seca... as palavras não saem..."

    ro "Só vai... [mc]... antes que seja tarde demais..."

    scene black with dissolve

    scene n8i31 with Dissolve(1.0)

    "Eu peguei o dinheiro... todo o dinheiro... e coloquei na mochila."

    "A mochila da Roxane... ela tá mais pesada do que eu imaginava..."

    "Mas não é só o peso do dinheiro..."

    "É o peso de ter explodido uma bomba no colo dela e agora estar dando o fora."

    scene black with dissolve

    scene n8i34 with Dissolve(1.0)

    pause 2.0

    mc "Roxane... eu... eu sinto muito..."

    ro "Não precisa sentir... você fez o que acha certo. A Zaza estaria orgulhosa de você."

    ro "Só... promete que vai cuidar dele... do Nathan..."

    mc "Eu prometo."

    ro "E... nunca mais voltem pra Capital... vocês não são bem-vindos aqui..."

    mc "Eu sei..."

    ro "Adeus, [mc]..."

    mc "Tô torcendo pra você conseguir lidar com os fantasmas do passado."

    mc "Você não tem culpa do que fizeram com você."

    ro "Deixa comigo. Agora vai."

    menu:
        "Adeus, Roxane.":


            pass

    scene black with dissolve

    pause 2.0

    scene n8i35 with Dissolve(1.0)

    pause 2.0

    "Preciso sair daqui... rápido..."

    "A mochila tá pesada... o dinheiro... a culpa..."

    "Roxane..."

    "Ela ficou lá... sozinha... sem esperança."

    "Eu devia ter ficado... devia ter ajudado ela."

    if blergh_foto:

        "Eu prometi pro Black Cash que ia tirar ela da Blergh!..."

    "Mas e o Nathan? E a nossa liberdade?"

    "Eu não posso voltar atrás agora... não posso... não com isso nas costas."

    "Cada passo ecoa mais alto que a música do DJ... parece que o som tá me perseguindo..."

    "Preciso encontrar o Nathan... a gente tem que dar o fora daqui..."

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    "Mas onde ele tá?"

    "Tem tanta gente... tanta confusão..."

    "Ali... perto do palco... a Zaza..."

    scene black with dissolve

    scene n8i36 with Dissolve(1.0)

    pause 2.0

    "Merda... o Nathan tá com a Zaza! Bem ali, no canto do salão!"

    "Eles tão sorrindo, conversando, brindando... como se nada tivesse acontecendo..."

    "Mas eu tô carregando a porra de uma FORTUNA na mochila da Roxane!"

    "Se a Zaza me vir aqui... com essa mochila... com essa roupa ridícula."

    "Ela vai desconfiar na hora! Ela vai me interrogar! Ela vai descobrir que este é toda a grana que o Grupo deu pra Blergh!!"

    "E a Roxane? O que tá acontecendo lá na sala dela? E se ela aparecer gritando?"

    "O tempo tá passando... a cada segundo que passa, o risco aumenta..."

    "Preciso avisar o Nathan... preciso tirar ele dali... antes que seja tarde demais!"

    "Mas como? Não posso simplesmente gritar o nome dele no meio dessa gente toda..."

    "A Zaza tá grudada nele... como se fosse um carrapato."

    "Preciso criar uma distração... algo que chame a atenção dele... que o afaste da Zaza."

    menu:
        "Mas o quê?!":


            pass

    "Olha a quantidade de gente aqui... a música tá alta... as luzes piscando... as conversas... o burburinho..."

    "Preciso de algo que se destaque. Algo que corte essa barreira sensorial... algo que grite: 'Nathan, corre!'"

    "O Fabrício! A bebida... a porra da bebida!"

    scene black with dissolve

    mc "Me dá essa bandeja, Fabrício!"

    gar "S-senhor [mc], o que acontece de tamanha euforia exigindo destreza deste calibre?!"

    mc "D-desculpa!"

    gar "Ei! Minha honorável bebida!"

    play sound som_35_passos

    scene n8i37 with Dissolve(1.0)

    "Preciso chegar perto deles... sem levantar suspeitas..."

    if nathan_namoro:

        "Desculpa, Zaza... mas o Nathan é meu..."

    mc "Senhoritas..."

    "Garota Linda" "Obrigada, querido."

    "Garota Fantástica" "Você é um anjo."

    "Anjo? Se elas soubessem..."

    mc "Meu Deus! Esta bebida tá quente! Preciso ir para a cozinha o mais rápido possível! Essa bandeja vai pegar fogo!"

    "O Nathan tá olhando pra trás, confuso. Acorda, degrama! Olha a mochila nas minhas costas e a expressão de pânico que eu tô fazendo!"



    "Nathan, por favor... entende a merda que a gente tá... a gente precisa vazar! AGORA!"

    n "Zaza, com licença... preciso... me refrescar um pouco. Essa festa tá quente demais!"

    za "Haha! Vá em frente, querido. Aproveite para circular e fazer contatos. Você é o rosto da Blergh! esta noite!"

    n "Valeu, Zaza..."

    "Ela deu corda! Ele tá vindo!"

    n "Vem, [mc]!"

    scene black with dissolve

    scene n8i38 with Dissolve(1.0)

    pause 2.0

    "Música de Festa" "{i}Tum tum tum... tum tum...{/i}"

    n "Cara, você me assustou! Que merda foi aquela com o som? E essa mochila?!"

    mc "Consegui a grana! Tá tudo aqui na mochila!"

    n "Sério?! Você é o cara! A gente vai ficar rico!"

    mc "A Zaza e o Grupo que se fodam! A gente vai viver como reis!"

    n "Vamos dar o fora daqui agora! Antes que alguém perceba..."

    "???" "PAREM!"

    "Essa voz..."

    scene n8i39 with hpunch

    pause 2.0

    mc "Zaza..."

    za "Você... você é o jornalista que estava no Cassino outro dia!"

    "Ela me reconheceu!"

    za "E você estava na Blergh! também, esperando o Nathan! O que você está fazendo aqui? E com essa mochila?"

    za "Eu reconheço essa mochila... Roxane?"

    "Merda... ela ligou os pontos..."

    "A gente tá ferrado..."

    "Meu corpo inteiro congelou. O ar ficou denso, a música da festa se transformou em um zumbido distante."

    "A Zaza... ela me pegou. Ela sabe que eu tô aqui. Ela viu a mochila."

    "Droga... e o Nathan? Ele tá pálido... suando frio..."

    za "O que vocês dois estão fazendo aqui? [mc]? Você não devia estar aqui. E você, Nathan, por que não está se preparando para o desfile?"

    "O olhar dela... frio, calculista... como se estivesse analisando cada movimento nosso."

    "Ela está esperando uma resposta. Mas que resposta eu posso dar? Que eu tô roubando ela?"

    n "A gente vai embora, Zaza. Pra sempre."

    za "O quê?!"

    "O Nathan... ele respondeu. Com uma voz firme... decidida..."

    scene black with dissolve

    scene n8i40 with Dissolve(1.0)

    pause 2.0

    n "Eu cansei, Zaza. Cansei de você, da Cássia, da Blergh!, dessa cidade, desse Grupo!"

    za "Nathan... o que você está dizendo? Você está sendo manipulado por ele?"

    n "Manipulado?! Você fala de manipulação? Depois de tudo o que eu passei? Depois de tudo o que vocês fizeram comigo?"

    n "Você me usou desde o começo! Me prometeu fama, sucesso, uma vida de luxo! E o que eu ganhei? Uma vida de mentiras, de traições, de medo!"

    za "Nathan, pare agora... você não está pensando direito... está parecendo um fraco!"

    n "Não?! Você me obrigou a seduzir a Cássia! Me usou como um brinquedo sexual para conseguir o que queria! Me transformou em um fantoche para seus planos!"

    "Ele tá falando sério... a raiva dele... a mágoa..."

    "E a Zaza... ela parece surpresa... como se não estivesse esperando essa reação."

    n "E você, [mc]! Você também foi enganado por mim! Eu menti pra você, te manipulei, te usei pra aparecer na mídia!"

    n "Me desculpe, [mc]! Eu não queria te fazer mal! Eu só queria realizar meu sonho! Mas agora eu vejo... o preço foi alto demais!"

    "Ele tá... se desculpando comigo... na frente da Zaza..."

    "A voz dele tá embargada... ele tá chorando..."

    "Eu nunca vi o Nathan assim... tão vulnerável, mas também tão certo."

    n "Eu me prostitui para a Cássia! Me rebaixei! Me humilhei! Tudo para conseguir um lugar neste mundo podre!"

    "A Zaza... ela não consegue desviar o olhar... como se estivesse presa às palavras do Nathan..."

    n "E você, Zaza, você me prometeu que ia me proteger! Que ia cuidar de mim! Mas você me jogou aos lobos! Me expôs! Me deixou à mercê da mídia e da polícia!"

    n "Eu vivi com medo de ser deportado! Medo de perder tudo! Medo de acabar na rua! E você... você não fez nada!"

    n "Você só se importa com a Blergh!, com a porra do Grupo, com o poder! Você não se importa com as pessoas! Você é fria, calculista, egoísta!"

    za "..."

    "A Zaza... ela tá sem palavras."

    "Ela não consegue responder... ela tá em choque!"

    n "Eu tô indo embora, Zaza! Voltando pro meu país! Onde eu posso ser quem eu sou, sem medo! E você fique com a porra do seu poder!"

    "Ele se virou para mim, com os olhos vermelhos, cheios de lágrimas."

    scene black with dissolve

    scene n8i41 with Dissolve(1.0)

    pause 2.0

    n "Vem comigo, [mc]! Vamos recomeçar nossas vidas! Longe dessa cidade! Longe dessas pessoas!"

    if nathan_namoro:

        n "Só nós dois, juntos!"
    else:


        n "Você sim é um amigo de verdade. Um cara firmeza que merece uma vida boa longe disso tudo!"

        n "Você vai ter todo o dinheiro que você quiser, e eu vou ser parceiro pra tu pega todas as gatas que tu aguentar comer."

        mc "Haha... Nathan."

    "Ele tá olhando pra mim... esperando uma resposta..."

    "Eu olho para a mochila, pro dinheiro... pra Zaza... pro Nathan..."

    "Minha vida... meu futuro... tudo depende da minha próxima decisão..."



    za "..."

    "Silêncio total no ar, pesado igual chumbo. A música da festa, antes vibrante, agora soava distante, abafada pela tensão."

    "A Zaza não sabia da grana. Ainda."

    "O Nathan esperando minha resposta. Seus olhos vermelhos, marejados, fixos em mim."

    "A Zaza... ela tava em choque. As palavras do Nathan a atingiram como um golpe certeiro. Aquela mulher toda poderosa estava a um golpe de cair."

    "Mas... por trás da surpresa... o rosto dela... é mágoa?"

    "É possível que a Zaza sinta algo além da ambição fria e calculista?"

    "Não... não pode ser. Ela é a dona da Blergh!, a mentora por trás de todo esse esquema. Ela usou o Nathan, usou a mim, usou a Roxane..."

    "Seus olhos então se fixaram na mochila. Na mochila da Roxane, abarrotada de dinheiro."

    za "C-como... como você conseguiu isso?"

    "Sua voz, antes firme e imponente, agora soava frágil, quase um sussurro."

    "Ela entendeu... ela sabe que eu tô roubando ela. Ela sabe que eu sou a 'faca de Brutus'."

    mc "O Nathan não é o único que se voltou contra você, Zaza. Tem alguém na sua sala que descobriu a verdade."

    "As palavras saíram da minha boca antes que eu pudesse pensar. Uma coragem... uma ousadia inesperada."

    "Tô começando a sentir que o plano vai dar certo. Será que é isso?"

    scene black with dissolve

    scene n8i42 with Dissolve(1.0)

    pause 2.0

    za "N-não...."

    "Ela cambaleou para trás, como se tivesse levado um soco no estômago. A máscara de poder que ela usava se estilhaçou, revelando seu ponto fraco."



    "Seus olhos... por trás dos óculos... eles estavam marejados... vermelhos..."

    "Ela estava... sofrendo?"

    menu:
        "Jogar na cara dela sobre a Roxane":


            mc "Eu consegui muito mais que dinheiro, Zaza. Eu consegui uma garantia pra sair daqui."

            na "[mc]..."



            "Por que eu estava fazendo isso? Por que eu tava jogando na cara dela assim?"

            "Eu quero que ela saiba. Mostrar que eu não era mais o 'garoto inocente' que chegou na cidade. Que eu também podia ser cruel."

            "Ou talvez... para me vingar por tudo o que ela fez com a gente."

            mc "Agora você entendeu?"
        "Ficar em silêncio":


            mc "..."

    za "A Roxane... o contrato..."

    "Ela sussurrou, com a voz embargada. Sua máscara de poder se dissolveu por completo, revelando uma mulher... derrotada."

    "O contrato... ela entendeu. Ela sabe que eu tenho a prova de que o grupo deu a Roxane dela pra ela cuidar. Tráfico de pessoas."

    "Ela sabe que eu posso destruir a vida dela... destruir a Blergh!... e jogar o Grupo no fogo com uma notícia."

    menu:
        "Mas... por que eu não tô sentindo satisfação?":


            pass

    "Por que essa sensação de vazio no meu peito?"

    "Olhando pra ela agora... pra mulher que levantou uma empresa do zero, que cuidou da Roxane na mulher forte que é hoje, que ensinou sabe lá quantas outras modelos..."

    "Que enfrentou o prefeito sobre o papel das garotas no Grupo junto da Natasha..."

    "No fundo... o que a Zaza realmente fez de errado? Ela não é o Barão, ela não é o Tony e muito menos o Gustav."

    "Ela realmente... merece perder tudo que ela construiu em quase 20 anos?"

    menu:
        "Sim. Ela se aliou às pessoas erradas":


            "Eu não posso fraquejar agora."
        "Não... eu tô fazendo isso por mim e pelo Nathan":


            "Eu só conseguia sentir... pena?"

    za "Eu estava... tão perto... tão perto de mudar isso tudo."

    "A Zaza, abatida, encarava o chão, os ombros curvados pelo peso da derrota."

    "Ela tava há poucos segundos de cair no chão."

    "O Nathan... seus olhos estavam fixos em mim. Ele depositou todas as fichas em mim. Em nós."

    "Eu... eu sentia o peso da mochila nas costas, o dinheiro roubado, o contrato que podia destruir a Blergh!, a vida da Zaza... e a minha também."

    "De repente, passos apressados quebrando o silêncio. Uma figura familiar surgindo no corredor, com a testa franzida e um olhar preocupado."

    scene black with dissolve

    scene n8i48 with Dissolve(1.0)

    pause 2.0

    na "Zaza?!! O que está acontecendo?! Por que você não tá..."

    if diana_final2:

        "Natasha. A 'secretária'. A mulher que me ajudou a escapar do Cassino, mas que continua do lado deles."

    "Seu olhar percorreu a cena... a Zaza abatida, o Nathan com os olhos vermelhos, eu com a mochila abarrotada..."

    "Ela entendeu."

    za "O [mc]... ele pegou o dinheiro. E o contrato. A Roxane ajudou ele."

    "A Zaza disse com a voz fraca, derrotada."

    "No fundo ela sabia que tinha perdido. Que a Roxane, o Nathan e eu... nós éramos as peças que faltavam pra queda dela."

    "Mas... a Natasha... ela não tava nem um pouco abatida."

    "Ela se virou pra mim, seus olhos verdes agora quase azuis, gélidos, penetrantes."

    scene black with dissolve

    scene n8i47 with Dissolve(1.0)

    pause 2.0

    na "Você entende, [mc], contra quem está comprando briga?"

    "Sua voz, normalmente suave e sedutora, agora era cortante, ameaçadora."

    "Meu corpo inteiro tremeu. Um arrepio percorreu minha espinha. O medo... aquele medo visceral que eu senti no Cassino... ele voltou."

    "A realidade parece que voltou pra mim. Eu sei que minha vida tá por um fio."

    menu:
        "Você também faz parte disso, Natasha!":


            mc "Você também faz parte desse Grupo! Você não tem o direito de me julgar!"

            na "Eu sirvo ao prefeito Donatello. E ele não tolera traidores."

            mc "Você traiu a Diana! Se aliou com os captores dela!"

            na "Eu fiz o que era necessário. E você também vai ter que fazer escolhas difíceis, [mc]."
        "Não... eu...":


            mc "E-eu..."

            "Minha voz falhou. As palavras não saíam. O medo me paralisava."

            na "[mc], você é um jornalista. Um observador. Você deveria saber como as coisas funcionam nesta cidade."

    na "Você e o Nathan podem até conseguir fugir. Mas o Marco vai encontrar vocês. Não importa pra onde vocês forem."

    "O Marco... o homem que já quase me matou várias vezes..."

    "Ele vai me perseguir... me caçar... até me encontrar."

    "Não importa pra onde a gente vá... a sombra deles vai me acançar..."

    "Eu olho pro Nathan. Ele também tá apavorado. Seus olhos arregalados, buscando uma saída, uma esperança..."

    "Mas não havia saída. Não havia esperança."

    na "Mas... existe outro caminho. Um caminho onde todos nós podemos ser amigos."

    na "Nathan, você ainda se lembra do seu objetivo?"

    "Seu objetivo?"

    scene black with dissolve

    scene n8i43 with Dissolve(1.0)

    pause 2.0

    "O Nathan... ele estremeceu. Seus olhos se desviaram dos meus, se fechando. Tentando guardar algo só pra si."

    "O que a Natasha tinha dito? O que tinha atingido o Nathan dessa forma?"

    "E o que ela queria dizer com 'sermos amigos'? Que tipo de amizade ela oferecia?"

    "Eu sentia que estava no centro de um jogo de xadrez... um jogo com peças que eu não conseguia entender... um jogo onde minha vida era a aposta..."

    "E agora... eu tinha que fazer minha jogada final."

    menu:
        "Que história é essa, Nathan? Que objetivo?":


            pass

    n "..."

    "A Natasha tinha mexido com algo fundo no Nathan, algo que eu nunca tinha percebido."

    "A Zaza, ainda em choque, observava a cena com um olhar perdido, como se tivesse se tornado uma espectadora de algo ainda maior."

    mc "Nathan... que história é essa? Do que a Natasha tá falando?"

    "Eu preciso de uma resposta, uma explicação. Mas não ele não fala nada."

    na "O Nathan veio pra este país com uma missão, [mc]. Uma missão que ele está prestes a abandonar."

    "A voz da Natasha era fria, cortante, como se estivesse pronunciando uma sentença. Uma sentença pro Nathan, e talvez para mim também."

    mc "Uma missão? O Nathan? Mas que missão? Ele era um modelo, um cara que queria fama e sucesso. Que tipo de missão é essa?"

    mc "Não tô entendendo mais porra nenhuma!"

    "???" "E como seria diferente?"

    mc "V-você!?"

    scene black with dissolve

    scene n8i44 with Dissolve(1.0)

    pause 2.0

    gar "Verdade cristalina, minha cara e perspicaz colega de labuta. O jovem Nathan carrega em seus ombros um fardo deveras importante para o destino desta urbe."

    mc "Fabrício?!"

    "O Fabrício... ele surgiu do nada, como um fantasma. Igual sempre..."

    mc "Um fardo? Que fardo? Você tá confirmando a história da Natasha? O que tá acontecendo aqui?"

    n "[mc]..."

    "Eu me sentia cada vez mais perdido."

    gar "Há tempos imemoriais, um plano foi traçado para que a Cidade Dourada atingisse seu ápice."

    gar "E o jovem Nathan, com sua beleza e carisma, foi escolhido como a chave para abrir as portas do futuro."

    mc "A Cidade Dourada? Você tá falando da Capital ou tipo Eldorado alguma coisa assim?"

    na "Sim. Como Eldorado, um lugar de promessas e riquezas."

    mc "Mas que plano é esse? E por que o Nathan é a chave?"

    gar "Entretanto, a melancolia e o desânimo se apoderaram de nosso amigo, levando-o a renegar seu destino e a buscar uma vida medíocre longe de suas responsabilidades."

    mc "Que responsabilidades? Ele vai salvar o mundo?"

    "Eu precisava de respostas. Precisava entender."

    mc "Nathan... me explica. O que tá acontecendo?"

    scene black with dissolve

    scene n8i45 with Dissolve(1.0)

    pause 2.0

    n "Eu... eu quero deixar tudo isso para trás, [mc]. Essa vida de mentiras, de manipulação, de medo..."

    mc "Você quer fugir de toda essa merda? Recomeçar?"

    n "Eu quero uma vida normal, simples. Quero ser feliz. E quero que você seja feliz comigo."

    n "Por favor, me entenda. Deixe isso tudo pra trás."

    mc "Fugir... recomeçar... longe da Capital, longe do Grupo, longe da Zaza, da Cássia, do Fabrício... longe de tudo isso."

    mc "Mas... e sua missão? E esse plano aí traçado pra tal Cidade Dourada?"

    n "Esquece isso."

    "Esquecer tudo isso e só curtir milhões longe disso tudo."

    "Eu tinha que decidir. Agora."

    menu:
        "Sim, vamos fugir. Longe de tudo isso.":


            pass
        "Espera. Antes eu quero entender isso.":


            mc "Nathan... eu preciso entender. Que missão é essa? Que plano? O que tá acontecendo?"

            "Minha voz saiu firme, decidida."

            mc "Eu não poosso fugir sem saber a verdade. Sem entender o que tá em jogo."

            mc "Uma missão? Um plano pra Cidade Dourada? Você entende que tudo isso parece piada?"

            n "É complicado, [mc]. Tem muita coisa que eu não posso te contar. Coisas que... que colocam muita gente em risco. Você entende?"

            n "E não é só isso. São coisas que eu quero deixar pra trás. Não quero... falar disso."

            mc "Você tá escondendo algo. Algo grande."

            mc "Mas... a Natasha... o Fabrício... eles sabem?"

            mc "Você vai esconder coisas de mim até agora?!"

            n "Não!"

            na "Sim..."

            gar "Pois sim, meu caro e perspicaz amigo."

            gar "A verdade, por mais obscura que possa parecer, é que existem aqueles que vieram de terras distantes para ajudar a Capital."

            gar "Ajudar esta terra a se livrar da Sombra que a assola há séculos. E o jovem Nathan... ele é um dos inestimáveis guerreiros da luz."

            mc "Guerreiros da luz? Sombra? Você não pode falar direito nem num caso destes?"

    za "Nathan... você... você nunca me disse nada sobre isso..."

    n "Isso nunca foi meu sonho, Zaza. Eu nunca quis ser um 'guerreiro da luz', um salvador da pátria."

    n "Eu só queria ser um modelo, ter uma vida normal, simples."

    scene black with dissolve

    scene n8i46 with Dissolve(1.0)

    pause 2.0

    n "Mas então... eu conheci o [mc]."

    mc "E-eu?"

    if nathan_namoro:

        n "[mc]... você me mostrou o que é o amor de verdade. Um amor que não pede nada em troca."

        n "Um amor que me aceita como eu sou, com meus medos, minhas fraquezas."

        "Ele disse com a voz embargada, segurando minha mão. A intensidade do seu olhar me atravessava, me aquecia."

        mc "Nathan..."

        "Ele podia não me contar tudo. Ter suas razões."

        "Mas o nosso amor... ele era real."

        n "Você me deu força para enfrentar tudo isso. Para lutar pelos meus sonhos. Para ser quem eu realmente sou."

        "Ele apertou minha mão, seus dedos entrelaçados nos meus. A força do seu toque me transmitia segurança, esperança."

        n "Eu não quero mais viver essa vida de farsas, de traições."

        n "Eu quero uma vida com você, [mc]. Uma vida simples, honesta, cheia de amor."

        n "O que eu sinto por você é a única coisa verdadeira no meio desse mar de mentiras e manipulações."

        "Ele me escolheu. Ele escolheu o nosso amor."
    else:


        n "[mc]... você luta pelos seus sonhos com tanta garra, com tanta paixão."

        n "Você não desiste, não importa quantos obstáculos apareçam no seu caminho."

        n "Eu te admiro. A força da sua determinação me inspirava, me contagiava."

        n "Você me mostrou que é possível ser feliz sendo quem a gente é, sem se curvar aos poderosos, sem se corromper."

        n "Eu não quero mais ser um peão nesse jogo sujo. Eu quero ter a coragem de lutar pelos meus sonhos, como você."

        "Ele me via como um exemplo? Eu? Mas eu era apenas um jornalista, um paparazzo tentando sobreviver na Capital."

        "Mas... talvez ele estivesse certo. Eu nunca desisti. Eu sempre lutei pelo que eu queria."

        "E agora... o Nathan queria fazer o mesmo."

    n "Eu quero ir embora, [mc]. Quero recomeçar. E quero que você venha comigo."

    "Ele me olhou nos olhos, sua expressão séria, decidida. A decisão tá nas minhas mãos."

    "Fugir... com o dinheiro, com o contrato, com o Nathan... Longe da Capital, longe do Grupo, longe de tudo isso..."

    "Ou eu quero ficar aqui e descobrir tudo? Descobrir a verdade do Fabrício, da Natasha, do Nathan e sabe-se lá quem!"

    "O que você vai escolher, [mc]?"

    mc "Meu Deus..."

    label nathan_final_escolha:

        pass

    menu:

        "Vamos, amor. Ficar ricos e deixar tudo isso pra trás." if nathan_namoro:

            $ nathan_final = 1

            "Fugir... com o dinheiro... com o Nathan... com a promessa de uma nova vida..."

            "Era isso que eu queria? Era esse o meu sonho?"

            "A mochila pesava nas minhas costas, o dinheiro roubado, o contrato da Roxane... o peso da minha decisão..."

            "Mas... olhando para o Nathan, para seus olhos cheios de esperança, para o sorriso que iluminava seu rosto..."

            "Eu sabia que tinha feito a escolha certa."

            scene black with dissolve

            scene n8i49 with Dissolve(1.0)

            pause 2.0

            mc "Sim, Nathan. Vamos embora. Vamos ser felizes."

            "As palavras saíram da minha boca com uma força que eu não sabia que possuía. A decisão tomada, a incerteza se dissipou, dando lugar a uma determinação inabalável."



            n "[mc]!!!"



            n "A gente vai conseguir! Vamos ser livres! Vamos ser ricos! Obrigado, [mc]! Obrigado!"

            "Ele parece tão feliz! Parece uma criança."

            "Eu também tô muito feliz. Feliz por ele, por nós. A promessa de uma nova vida, longe da Capital, longe do Grupo, longe de toda essa loucura... é muito foda."

            jump nathan_final1



            call final_bloqueado

            call ajuda_itchio

            jump nathan_final_escolha

        "Bora, parça. Ficar ricos e curtir as minas desse mundão." if not nathan_namoro:

            $ nathan_final = 1

            scene black with dissolve

            scene n8i49 with Dissolve(1.0)

            pause 2.0

            mc "Bora, parça. Ficar ricos e curtir as minas desse mundão."

            n "É isso aí! Vamo nessa!"

            "A adrenalina bombava nas veias. A mochila cheia de dinheiro nas costas parecia leve como uma pena. A gente ia conseguir. A gente ia ser livre."

            "A gente ia ser rico!"

            jump nathan_final1



            call final_bloqueado

            call ajuda_itchio

            jump nathan_final_escolha
        "Eu não quero deixar a Capital. Eu quero ficar.":


            $ nathan_final = 2

            jump nathan_final2

            call final_bloqueado

            call ajuda_itchio

            jump nathan_final_escolha

label nathan_final1:

    scene black with dissolve

    scene n8_img41 with Dissolve(1.0)

    gar "Ora, vejam se não é nosso nobre amigo a abandonar o barco antes de aportarmos em terras nativas após a missão concluída."

    mc "O que foi agora Fabrício?!"

    "Ele tá com essa cara... impossível de entender o que ele tá pensando."

    "Do outro lado, a Natasha, impassível, apenas observava a cena. Seus olhos opacos, sombrios."

    gar "Parece que a cobiça e o deslumbre toldaram a mente de nosso amigo, levando-o a renegar compromissos ancestrais."

    na "Nathan... por que você tá fazendo isso? A gente veio pra cá com um propósito! A gente tem que... a gente..."

    "Ela realmente tava demonstrando emoção? Ou era uma fachada pra convencer a gente?"

    n "Eu... me desculpem... mas eu não consigo mais. Eu preciso viver... e viver de verdade."

    gar "Viver?! Acaso não estamos nós vivos neste exato momento? Acaso a vida não pulsa em nossas veias, levando-nos para o clímax da existência?"

    n "Não é isso, Fabrício... Eu encontrei... encontrei algo que me faz querer..."

    "Ele olhou pra mim, seus olhos azuis brilhando com uma intensidade que nunca tinha visto."

    "Era como se ele estivesse se agarrando em mim como a um bote salva-vidas."

    n "Eu não posso... não consigo mais viver nesse mundo de mentiras. Eu preciso de algo real. De algo..."

    mc "..."

    "Eu não posso deixar ele tomar essa decisão sozinho. Ele precisa de mim."

    label nathan_final1_escolha1:

        pass

    "É minha última chance de decidir o que acontece com a gente."

    menu:
        "Eu entendo você, Nathan. A gente não precisa ser herói pra ninguém.":


            mc "Vem. Bora."

            n "[mc]... bora."

            scene black with dissolve

            scene n8_img42 with Dissolve(1.0)

            mc "Nathan... eu te entendo, cara. Essa vida não é fácil... essa cidade... esses jogos de poder..."

            mc "A gente só quer ter uma vida normal, porra! Curtir, viajar, dar risada. Sem essa pressão toda... sem essa porra de 'missão'."

            mc "A gente não precisa ser herói pra ninguém. Foda-se o mundo, foda-se o 'Grupo', foda-se o Fabrício, foda-se a Natasha!"

            mc "A gente merece ser feliz. Só a gente... curtindo essa grana... longe de tudo isso."
        "Nathan, eles têm razão. Você não pode desistir. Eles tão contando com você.":








            mc "Nathan... escuta... eu sei que você tá cansado... sei que você tá sofrendo. Mas você não pode desistir agora."

            mc "Vocês vieram de longe... pra ajudar a mudar essa cidade... pra lutar contra esse povo."

            mc "Você é a porra da 'chave' pra tudo dar certo, lembra? Você não pode abandonar eles."

            n "[mc]..."

            mc "A gente não pode desistir. Não agora... A gente tem que ser forte. Tem que lutar. Por eles... pela cidade... pelo futuro..."

            jump nathan_final2

    mc "A gente vai conseguir, Nathan. Longe dessa merda toda."

    "A Natasha e o Fabrício observam a cena em silêncio, suas expressões indecifráveis. Eles perderam. A gente venceu."

    mc "É hora de ir."

    "Cada passo parece um passo para longe dessa vida de merda."

    za "Meu dinheiro... meu sonho..."

    menu:
        "Adeus, Zaza.":


            pass

    scene black with dissolve

    pause

    "E assim..."

    scene n8_img43 with hpunch

    na "PAREM!!!"

    "A voz da Natasha, gélida. A gente para. Seus olhos como de uma gata caçadora."

    na "Se vocês realmente querem ir, vão. Mas vão sem o dinheiro."

    mc "Como é?"

    na "Ele não te pertence! Você pode renegar tudo, mas não pode sair com o que é nosso!"

    "Ela aponta pra mochila, pra fortuna roubada da Zaza."

    na "Vocês podem ser covardes, podem ser ingratos... mas não podem ser ladrões. Deixem o dinheiro."

    n "A gente precisa da grana, [na]! Como vamos viver sem ela?"

    na "Vivam como sempre viveram: ralando, suando, lutando. Vocês não merecem essa riqueza."

    mc "Natasha... por favor... a gente já decidiu..."

    na "Não, [mc]. Você não decidiu nada. Você ainda não entendeu o que está em jogo."

    na "Se quiserem esse dinheiro... terão que lutar por ele."

    "Impossível que ela vai querer lutar com a gente aqui. Por causa da Zaza e do prefeito? Mas ela não..."

    n "Natasha, sai da frente. A gente não quer brigar com você."

    na "Então deixem a mochila. É simples assim."

    n "Eu não vou fazer isso. E eu posso te vencer, Natasha. Você sabe disso."

    "Caralho, que tensão... a adrenalina, a respiração acelerada. A gente tá a um passo de uma batalha."

    "O que eu vou fazer? Fugir sem a grana ou lutar contra a Natasha?"

    "Isso depende de mim!"

    menu:
        "Nathan, a Natasha tem razão. Vamos deixar a grana e sair daqui.":


            mc "Nathan... ela tem razão. A gente não precisa dessa merda pra ser feliz. Deixa pra lá."

            n "[mc]..."

            mc "Vamos."

            n "Não! De jeito nenhum! A gente precisa disso e não é ela que vai me parar!"

            na "Tem certeza?!"
        "Ela não vai nos impedir. A gente precisa do dinheiro pra recomeçar!":


            mc "A gente precisa dessa grana pra ter uma vida nova, Natasha! Sai da frente ou a gente vai te tirar!"

            na "Então é isso. Vocês escolheram."

    scene n8_img44 with hpunch

    na "Você que vai lutar? Eu sempre fui mais forte que você, parceiro."

    n "Não importa. Dessa vez eu tô lutando por uma coisa que eu realmente quero."

    na "Falou bonito, mas você tem força pra vencer?"

    scene n8_img45 with vpunch

    n "Cala a boca!"

    na "AAAIIH!"

    menu:
        "Boa, caralho! A gente precisa da grana!":


            mc "Vai, Nathan!"

            n "Eu vou fazer essa pela gente!"
        "Cuidado com ela, cara! Ela é uma mulher!":


            n "Essa mulher mataria nós dois sem pensar duas vezes!"

            mc "E-eita..."

    na "Você realmente parece mais forte."

    n "Eu não quero acabar com você, amiga."

    na "Você não vai acabar comigo, idiota!"

    n "HM!?!"

    scene n8_img46 with vpunch

    mc "Nathan!"

    na "Eu avisei. Vocês não têm chance."

    n "Ah... desde quando você... é tão forte?"

    na "Acabou, Nathan. Você perdeu."

    "Que bosta! A Natasha venceu."

    na "E agora..."

    scene black with dissolve

    scene n8i50 with Dissolve(1.0)

    "E-ela tá me olhando! E isso só pode significar uma coisa... o próximo sou eu."

    na "Você viu o que aconteceu com ele, [mc]? Ninguém pode contra o prefeito Donatello. Ninguém."

    "Se nem o Nathan conseguiu, o que vai ser de mim?!"

    "Essa Natasha... ela não é só uma secretária. Eu tenho cada vez mais certeza disso."

    "Eu não tenho chance contra essa mulher. Eu vou acabar igual ao Nathan, no chão, derrotado."

    "Pensa, [mc]! Tem que ter um jeito!"

    "Você é um jornalista! Você não sabe lutar, mas alguma coisa boa você tem!"

    menu:
        "Fabrício!":


            pass

    mc "Fabrício! Pelo amor de Deus, cara, me ajuda! Você não pode só ficar aí parado!"

    gar "Calma, meu caro [mc]. Agitação e desespero são conselheiros nefastos. Analisemos a conjuntura com a frieza de um cientista."

    mc "Que conjuntura?! A Natasha vai me arrebentar! Ela vai..."

    gar "O que esperas que este humilde servo faça, senhor [mc]? A força bruta não é compatível com minha natureza."

    mc "Não é força bruta, Fabrício! É... é sobre o que é certo! A Natasha, ela... ela tá cega! Ela não vê que tá do lado errado!"

    gar "Cega? A senhorita [na]? Que disparate, meu caro."

    "Olho pro Nathan, caído no chão, gemendo de dor. Se eu não fizer alguma coisa, vai tudo pro saco."

    scene black with dissolve

    scene n8i51 with Dissolve(1.0)

    mc "A gente vai perder tudo! A gente vai acabar preso! Ou pior..."

    gar "Temor e covardia são emoções indignas de um homem de fibra. Acaso não almeja o senhor uma vida de liberdade e prosperidade?"

    gar "Acaso não deseja a companhia do jovem Nathan longe desta cidade corrompida?"

    "Ele tem razão. Eu não posso desistir. Não agora. Não quando a gente tá tão perto."

    mc "Ela tá sendo usada, Fabrício! Manipulada! Você não vê?"

    mc "Donatello, o Tony, o Grupo... eles tão destruindo essa cidade! Eles tão destruindo vidas!"

    gar "..."

    "O Fabrício tá me ouvindo. Tá pensando."

    mc "O Nathan, a Roxane, a Diana... e a Júlia! Eles tão todos sofrendo! E você... você tá ajudando essa gente! Você tá sendo cúmplice disso!"

    gar "Cúmplice?! Este servo?! Absurdo, senhor [mc]! Estamos aqui justamente para combater tamanha atrocidade."

    mc "Você tem certeza? Ouviu o que ela disse?"

    menu:
        "Ela falou que ninguém pode com o Donatello.":


            pass

    gar "Isso é deveras preocupante..."

    mc "Então! Faça alguma coisa! Não faça como eles! Você tem que... tem que escolher um lado! O lado certo!"

    "Nem eu sabia o que eu tava falando. Eu só não queria tomar uma bicuda dela."

    gar "O certo... o lado certo..."

    mc "A Natasha, ela... ela precisa da gente, Fabrício! Ela precisa ver a verdade! Ela precisa..."

    na "Eu não preciso de nada que você possa me dar."

    gar "Você ouviu a senhorita."

    mc "Fabrício... eu entendi que vocês tão aqui pra uma missão. Mas... você tem certeza que a Natasha ainda tá?"

    gar "Não coloque caraminholas na mente deste humilde e simplório escravo da justiça. Natasha é nossa principal arma."

    mc "Não é caraminhola! Olha pra ela! Ela tá protegendo a Zaza, o Donatello!"

    na "Eu..."

    mc "Fabrício... me escuta..."

    "Vou chegar bem perto pra só ele me ouvir."

    menu:
        "Se a Natasha trocar de lado... imagina o que vai acontecer?":


            pass

    gar "Oh... nobre companheiro... seria horrorível... uma mistura de horror com horrível."

    mc "Não seria melhor tirar ela daqui... antes que seja tarde demais?"

    gar "Ora, ora... estou certo disto. Muito bem. Qual é seu plano?"

    mc "Vocês dois precisam entender o que o Nathan entendeu. Que vocês podem ser felizes longe disso aqui!"

    na "!"

    "Eu grito com uma força inesperada. E eu acredito nelas. Eu sinto a verdade nelas."

    gar "..."

    menu:
        "Eu sei que vocês têm essa missão. Seus propósitos. Mas pensem em vocês agora!":


            pass

    mc "Até esses dias eu também não esperava que ia roubar milhões e tentar minha vida em outro lugar."

    n "Eu sinto que eu que coloquei essa ideia na cabeça dele."

    mc "E foi a melhor ideia! Pra que ficar vivendo aqui!? Nesse antro de gente idiota!"

    "Eu olho pra Zaza, mas ela não tá mais lá. Parece que ela não quer se intrometer nessa história. Ela desistiu."

    "Fabrício... Natasha... tudo dependia deles agora."

    "Imagina se eles se juntassem a gente e a gente não precisasse lutar?! Eu ia merecia um Nobel da Paz por essa!"

    scene black with dissolve

    scene n8i52 with Dissolve(1.0)

    na "Eu... eu..."

    "Ela tá com a voz presa, os olhos cheios de lágrimas."

    na "Mas... como? Como podemos simplesmente abandonar tudo? A missão... o Donatello... tudo o que eu..."

    n "Natasha, a gente não tá abandonando nada. A gente tá escolhendo a nossa vida. A nossa felicidade."

    gar "A liberdade é um direito inato, senhorita [na]. Não um privilégio concedido por aqueles que se consideram acima da lei natural."

    na "Você vai entrar nessa com eles?!"

    gar "Este humilde servo se encontra deveras preocupado."

    mc "Natasha, você se sacrificou esse tempo todo. Aguentou o Donatello, o Tony... se humilhou... pra quê? Pra ter uma vida de merda?"

    na "Mas... mas o que eu conquistei? O meu lugar... a minha..."

    gar "O nobre [mc] está certo afinal. Você tem passado tempo demais sob a sombra, minha cara amiga de labuta."

    na "Fabrício... você não entede..."

    mc "Natasha, com a grana da Zaza a gente não precisa mais disso! A gente pode ter tudo o que quiser! Sem ter que lamber a bota de ninguém!"

    gar "Liberdade e prosperidade, senhorita [na]."

    gar "Imagine... a senhorita, livre das garras do prefeito, navegando em um mar de riquezas, realizando seus sonhos... sem correntes, sem amarras..."

    n "A gente pode viajar pelo mundo, Natasha! Conhecer lugares novos, pessoas novas... viver de verdade! Sem medo, sem ter que se esconder!"

    "Ela tá olhando pra mochila, pra promessa de riqueza e liberdade."

    na "E se eles vierem atrás da gente? O Grupo... o Tony... eles..."

    menu:
        "Aí fodeu...":


            n "Haha... pior que é verdade."
        "A gente vai lutar!":


            mc "Que venham! A gente luta! Vale a pena lutar pela liberdade, Natasha! Vale a pena arriscar tudo pra ter uma vida que realmente importa!"

    gar "A vida é uma jornada, senhorita [na]. Uma jornada repleta de desafios e obstáculos."

    gar "Mas a vitória só é alcançada por aqueles que têm a coragem de enfrentar seus medos e lutar por seus sonhos."

    na "..."

    scene black with dissolve

    scene n8i53 with Dissolve(1.0)

    "É a hora da verdade. Ela olha pra cada um de nós, seus olhos agora brilhando com uma nova luz."

    mc "Você..."

    na "Sim... vocês têm razão. Eu... eu vou com vocês. Vou ser livre."

    n "Natasha!"

    mc "E você Fabrício?"

    gar "Este servo sabe que é demasiada loucura, mas não é a vida uma caixinha de surpresas? Contem comigo."

    menu:
        "Agora sim! Bora pra porra dessa nova vida! Adeus, Zaza! Adeus cidade de merda!":


            pass

    mc "Zaza?"

    "Verdade... ela tinha sumido... coitada... a grana do sonho dela..."

    n "E a Zaza? Faz tempo que ela não fala nad-"

    gar "Se ela foi chamar a cavalaria, em breve estaremos fadados à uma morte trágica."

    mc "Vamos sair daqui antes qu-{nw}"

    prc "Aonde pensam que vão?"

    na "!"

    gar "Ora, ora..."

    scene black with dissolve

    scene n8i54 with Dissolve(1.0)

    "A voz do prefeito Donatello ecoou pela sala fria e cortante. Ele estava ali nos encarando com a fúria de um deus traído."

    prc "Natasha... você... você realmente vai me trair? Depois de tudo o que eu fiz por você? Vai abandonar a cidade? A SUA cidade?"

    "A Natasha não sabe o que faz, ela tá olhando pra mim, pro Nathan, pro Fabrício."

    "Parece que ela não sabe como lidar com ele."

    na "Eu... eu..."

    prc "Olhe para você, Natasha. Você tem a cidade na palma da sua mão. O poder... a influência... a riqueza... tudo ao seu alcance."

    prc "E você vai jogar isso fora? Vai fugir como um rato?"

    "O jeito que ele fala, imponente, com essa aura de poder. Então ele é a lei na Capital..."

    na "Senhor, eu..."

    "Ela parece tão frágil e hesitante na frente dele."

    prc "Natasha, você é inteligente. Você é forte. Você é... especial. Você não precisa desses tolos. Você não precisa dessa vida miserável que eles oferecem."

    scene black with dissolve

    scene n8i55 with Dissolve(1.0)

    "Essa voz dele, suave e hipnótica, como o canto de uma sereia atraindo um marinheiro para o abismo."

    prc "Volte para mim, Natasha. Volte para o seu lugar. Volte para a glória."

    "Ela fechou os olhos, a respiração acelerada, o corpo tremendo. Não é possível que ela vai sucumbir ao poder dele."

    menu:
        "Natasha! Não cai nessa! Nós tamo com você!":


            "Eu queria gritar, mas as palavras não saíam. Se ele soubesse que eu tava com a grana, era nosso fim."
        "Melhor eu ficar quieto":


            pass

    $ renpy.notify("Natasha está pensando em sua história...")

    mc "..."

    "O que ela vai escolher?!"

    na "Sim... senhor..."

    mc "Não..."

    na "Eu... eu nunca trairia o senhor. Nunca."

    "MERDA! O que eu podia ter feito pra mudar as coisas com a Natasha?"

    if natasha_e2 == "negativo":

        "Será que eu devia ter contado pra ela o que eu descobri sobre o Barão aquele dia?"

        "Ela... ela teria confiado mais em mim?"

    "Tudo tá perdido. A Natasha nunca vai deixar a gente fugir com o dinheiro. Fodeu!"

    "Donatello venceu. Será que ele sempre vence?"

    prc "Excelente. Sabia que você faria a escolha certa, Natasha."

    n "Não..."

    gar "..."

    prc "E você veio sem calcinha, do jeito que eu mandei."

    na "Claro, senhor..."

    prc "Você sempre vai ser minha boa garota."

    na "E o senhor trouxe sua pistola, como sempre. Eu consigo sentir ela."

    prc "Qual das duas você tá falando?"

    na "Aquela que deixa um buraco enorme cheio de líquido quente..."

    prc "Hahaha..."

    "Que merda! Que raiva! Donatello tinha vencido. Ele sempre...{nw}"

    $ renpy.vibrate(1)

    play sound som_17_tiro

    scene n8i56 with hpunch

    "{i}BANG{/i}"

    "Um estampido. Um grito. Um baque surdo."

    "O prefeito Donatello! Seus olhos arregalados. A arma na mão da Natasha."

    prc "Na...ta...sha..."

    na "Você... você me usou... me manipulou... me fez... me fez acreditar que eu era... especial..."

    na "Você me fez de... de objeto... de brinquedo... de puta. Uma vadia pra você e seus amiguinhos usarem e descartarem."

    prc "Akh... sua vaca... eu vou..."

    $ renpy.vibrate(1)

    play sound som_17_tiro

    scene n8i57 with hpunch

    na "Você vai calar a boca apodrecer no inferno, escória."

    prc "..."

    gar "Senhorita... você realmente..."

    na "Sim. Acabou, [mc]. A missão acabou. Ele... ele tá morto."

    n "Não acredito... a gente devia ter feito isso antes."

    gar "Hohoho..."

    na "Vamos. Agora a gente pode fugir. De verdade."

    "O corpo do prefeito Donatello jazia no chão, o sangue formando uma poça vermelha ao seu redor. O cheiro de morte e pólvora pairava no ar."

    gar "Minha nossa... que reviravolta inusitada..."

    "Ele parecia atônito, seus olhos arregalados, a boca entreaberta."

    n "Vamos, [mc]! É a nossa chance!"

    mc "BORA!"

    $ nathan_final1 = True

    scene black with Dissolve(2.0)

    pause

    play sound som_12_gaivota

    scene black with dissolve

    scene n8i58 with Dissolve(1.0)

    if nathan_namoro:

        "Praia... em um país da Europa que eu nem lembro o nome. Longe da Capital. Longe do Grupo. Longe de tudo."

        n "É... a gente conseguiu."

        mc "Conseguimos. Finalmente."

        n "Você tá feliz, amor?"

        mc "Feliz? Eu tô... radiante. E você?"

        n "Eu nunca imaginei que pudesse me sentir assim. Tão... completo. Mesmo deixando tudo pra trás."

        mc "Você merece, Nathan. Você merece ser feliz também."

        n "E eu devo tudo isso a você, sabia? Se não fosse por você, eu ainda estaria lá... preso naquela vida... naquela mentira..."

        scene black with dissolve

        scene n8i61 with Dissolve(1.0)

        mc "Shh... esquece isso. Agora a gente tá aqui. Juntos."

        n "Você me mostrou que eu também merecia, [mc]. Que eu podia... podia ter uma vida de verdade. Uma vida com amor."

        n "Eu tava tão perdido... tão cego... A Cássia, a Zaza... eles me fizeram acreditar que eu era só... uma ferramenta. Que eu não tinha direito de ser feliz."

        "Ele respira fundo, a voz embargada."

        menu:
            "Aquela cidade tem esse poder. De sugar a gente em uma vida que a gente não quer.":


                pass

        n "É... Mas você... você me mostrou o contrário. Você me mostrou que eu era... especial."

        n "Você me viu no meio daquilo tudo. E você me perdoou. Eu não sei quantas pessoas teriam essa capacidade."

        mc "Eu sei que você tava confuso. Cássia, seu sonho de ser modelo, e agora todo esse lance de Herói da Cidade de Ouro."

        mc "Não consigo imaginar o tanto de coisa que você tinha na cabeça."

        scene black with dissolve

        scene n8i59 with Dissolve(1.0)

        mc "O-opa... hmmm..."

        n "Tudo isso é passado agora."

        "Um beijo carregado de amor e gratidão."

        n "Obrigado, [mc]. Obrigado por me libertar. Obrigado por me amar."

        mc "Eu te amo, Nathan. Mais do que tudo."

        scene black with dissolve

        scene n8i60 with Dissolve(1.0)

        "Esse beijo... ele me faz esquecer de tudo. De toda aquela merda que eu deixei pra trás."

        n "A gente tem tanta coisa pra fazer agora, né?"

        mc "Tem. A gente pode viajar o mundo, conhecer lugares novos, experimentar comidas diferentes... viver tudo o que a gente sempre quis."

        n "E a gente pode fazer tudo isso juntos. Só a gente... sem ninguém pra nos dizer o que fazer, sem ninguém pra nos controlar."

        mc "A gente vai ser livre. Pra sempre."

        n "E a gente vai ser feliz. Pra sempre."
    else:


        "Praia... em um país da Europa que eu nem lembro o nome. Longe da Capital. Longe do Grupo. Longe de toda aquela loucura."

        n "Mano... que vista..."

        mc "É... a gente conseguiu, hein."

        n "Conseguimos, cara! E você... você tá feliz?"

        mc "Feliz? Tô mais que feliz! Tô... sei lá... aliviado. Livre. E você?"

        n "Cara... eu nunca imaginei que pudesse me sentir assim... tão... leve."

        mc "Você merece, Nathan. Você passou por tanta coisa..."

        n "E eu devo tudo isso a você, sabia? Se não fosse por você... cara... nem sei o que seria de mim."

        mc "Que isso, mano! Amigos são pra essas coisas."

        n "Você é mais que um amigo, [mc]. Você é... você é a porra do meu irmão."

        n "Lembra daquela noite no bar? Quando a gente se conheceu? Eu tava todo cagado de medo da Cássia e você chegou com aquele papo de 'repartir o pão'..."

        mc "Hahaha! E você ainda me ofereceu uma das gatas! Como eu ia recusar?"

        n "E depois, no meio daquela loucura toda do julgamento, você tava lá, me dando força. Me ajudando a encarar aquela juíza maluca."

        mc "A [eli]... puta merda... ela era das brabas."

        n "Mas você me ajudou a passar por tudo aquilo. E agora... a gente tá aqui. Livre. Rico. E pronto pra curtir a vida adoidado!"

        mc "É isso aí! E você sabe que vai ter gata pra caralho! De todas as cores e sabores! Loiras, morenas, ruivas... altas, baixas, cheinhas..."

        n "Você vai ter que me ensinar a lidar com essa mulherada toda! Eu sempre fui meio lerdo pra essas coisas..."

        mc "Deixa comigo, parça. Eu vou te transformar no rei da pegação!"

        "A gente tava livre. A gente tava feliz. E o mundo... o mundo era nosso."

    scene black with dissolve

    scene n8i62 with Dissolve(1.0)

    gar "Ora, ora, vejam se não são nossos companheiros de jornada a desfrutar das benesses da vida contemplativa."

    mc "E aí! Chegaram bem na hora! Hmm... vocês parecem felizes."

    n "Parece que a gente não é os únicos que tão curtindo essa vida nova!"

    na "Que paz... nunca imaginei que pudesse me sentir assim... mas..."

    n "Mas nada, mulher. Curte aí."

    na "Penso se eles realmente vão deixar as coisas assim."

    menu:
        "Donatello tá morto. Eles vão ter que colocar as coisas em ordem antes de pensar na gente.":


            pass

    na "Tem razão. Acho que eu vou só curtir... um pouco dessa sensação."

    gar "A sensação é deveras inebriante, não é mesmo, senhorita [na]?"

    gar "Como se tivéssemos finalmente nos libertado de grilhões invisíveis que nos aprisionavam a uma existência medíocre."

    mc "E aí, Fabrício? Se acostumando com essa vida boa?"

    gar "A adaptação tem sido um processo deveras interessante, meu caro."

    gar "A ausência de responsabilidades e a abundância de recursos têm proporcionado uma miríade de novas experiências."

    na "Experiências? Você quer dizer 'tomar banho de sol sem ser usada pelo prefeito'? Ou 'beber um coquetel sem ter que anotar as falas de um mafioso'?"

    gar "Suas palavras destilam sarcasmo e ironia, senhorita [na]. Mas confesso que compartilho de seu júbilo. A simplicidade da vida tem um encanto singular."

    mc "E você, Natasha? Tá curtindo a liberdade?"

    na "Tô começando a achar que vocês tinham razão, [mc]. Fugir... foi a melhor coisa que a gente fez."

    "Ela sorriu, um sorriso genuíno. Era bom ver ela assim, relaxada, feliz. Uma Natasha que eu não conhecia."

    gar "E o senhor Nathan? Parece radiante como um girassol a desabrochar sob a luz do sol. O amor tem esse efeito transformador sobre as almas sensíveis."

    n "Haha... me deixa, maldito."

    "Agora somos nós quatro. E a cada dia eu sinto que a gente tá se aproximando."

    "O jeito que a Natasha me olha, o Fabrício... eu acho que podia tentar algo com eles..."

    if nathan_namoro:

        "Apesar que eu tô com o Nathan, né... pode dar merda..."
    else:


        "Eu tô sozinho agora mesmo. A gente tem que curtir."

    menu:
        "Falar com o Fabrício":


            mc "Vou falar com o Fabrício."

            n "Vai lá."

            scene black with dissolve

            scene n8i75 with Dissolve(1.0)

            mc "E aí, Fabrício? Refletindo sobre os mistérios do universo?"

            gar "A vastidão do cosmos é deveras instigante, meu caro [mc]."

            gar "Mas confesso que meus pensamentos estavam voltados para... assuntos mais terrenos."

            mc "Tipo?"

            gar "A beleza efêmera da natureza. O encanto singular do sol. E... a graça inegável de certos... espécimes."

            mc "Espécimes? Você tá falando... talvez... de mim?"

            gar "Ora, senhor [mc], a perspicácia é um de seus atributos mais admiráveis."

            gar "Acaso não percebeu o fascínio que sua presença exerce sobre este humilde servo?"

            "Será que ele realmente tá flertando comigo? Sério?"

            menu:
                "Eu... eu não... quer dizer...":


                    pass

            gar "Não precisa se constranger, meu caro. A atração entre seres humanos é algo natural... e, em certos casos, irresistível."

            mc "Fabrício... eu..."

            gar "Shh... deixe que as palavras se percam na brisa praiana. O que importa agora são... as sensações."

            gar "O que acha de acompanhar este humilde apaixonado para outro lugar?"

            menu:
                "Acho melhor mantermos na amizade, como sempre.":


                    gar "Uma decisão deveras frustrante, senhor [mc]. Mas faremos como desejar."

                    mc "Valeu. Eu sou mais chegado em garotas, sabe?"

                    gar "Espécimes fêmeas são agradáveis, não posso discordar."

                    mc "Hahaha... que bom que você me entende."
                "Vamos... antes que eles vejam a gente.":


                    gar "Logo atrás do senhor..."

                    scene black with dissolve

                    scene n8i76 with Dissolve(1.0)

                    mc "Hmm..."

                    "Ele me beijou com vontade, sua língua explorando minha boca, seu corpo contra o meu."

                    "Caralho... o Fabrício... até que ele beija bem..."

                    "Nunca imaginei que ele fosse assim... tão... intenso... não parecia"

                    gar "Hmmm... seus lábios... tão convidativos..."

                    mc "Fabrício... você... você é..."

                    "Aquele garçom todo formal... ele tinha sumido. Na minha frente tava um homem sedutor... irresistível..."

                    gar "Sou apenas um humilde servo do prazer, meu caro [mc]... à disposição para saciar seus desejos mais..."

                    "Ele não conseguiu terminar a frase. Suas mãos deslizaram pelo meu peito,tirando minha camisa com uma rapidez surpreendente."

                    "Ele tá com pressa. E eu... eu também."

                    mc "Fabrício... eu..."

                    gar "Shh... não perca tempo com palavras... o que importa agora são as ações."

                    scene black with dissolve

                    scene n8i77 with Dissolve(1.0)

                    "Meu Deus... ele vai mesmo... fazer isso..."

                    mc "Ahh..."

                    gar "Hmmm... tão belo... tão... magnífico."

                    "Ele tá passando a língua na cabeça... aah... caralho... que delícia..."

                    "Ele tá me engolindo! Com uma vontade..."

                    gar "Hmmm... delicioso... tão... suculento..."

                    "Que delícia! Ele sabe mesmo o que tá fazendo! Essa língua..."

                    "Eu não vou aguentar muito tempo assim..."

                    mc "Fa-Fabrício... eu..."

                    gar "Shh... apenas relaxe... e... desfrute do prazer."

                    gar "Era o destino, desde a primeira vez que nossos olhos nos encontraram no bar, quando o senhor desejava a senhorita modelo."

                    "Ele tá acelerando... e falando com essa voz rouca... puta que pariu..."

                    mc "Aah... eu... eu vou..."

                    gar "Sim, meu caro... se entregue ao êxtase."

                    scene black with dissolve

                    scene n8i78 with vpunch

                    mc "AAAH!"

                    "Eu explodi. Uma onda de prazer! Meu corpo tremendo..."

                    mc "Aah... que delícia."

                    "Ele engoliu tudo. Até a última gota. E continuou me chupando, a língua quente e úmida me provocando..."

                    gar "Hmmm... tão excitante, meu delicioso parceiro... tão..."

                    mc "Aah... Fabrício..."

                    gar "O senhor é... surpreendente, meu caro [mc]. E ainda temos um longo caminho a percorrer..."

                    gar "Essa nossa amizade... é deveras interessante... desejo ver quais frutos nascerão dela a partir de agora."

                    mc "Se você continuar me mamando desse jeito... hmm... vai ser uma delícia."

                    gar "Este dia... é apenas o começo, meu caro..."

                    mc "Sorte a minha... haha..."
        "Falar com a Natasha":


            mc "Vou falar com a Natasha."

            "O Fabrício observava o mar, perdido em pensamentos."

            "Ele parecia um monge em meditação, buscando a iluminação nas ondas quebrando na areia. E o Nathan curtindo a vista."

            scene black with dissolve

            scene n8i63 with Dissolve(1.0)

            mc "Oi, Natasha. Tudo bem?"

            na "Oi, [mc]. Tudo ótimo. E você?"

            mc "Melhor impossível. Essa brisa, o sol, essa vista... e você aqui."

            na "Você é um charmoso, sabia? Sempre foi, direto e corajoso."

            "Finalmente um sorriso sincero. A tensão que normalmente tava com ela desapareceu. Ela tá relaxada, receptiva."

            "Até um pouco demais. Mas acho que ser rica e viver de férias faz isso com a gente hahaha..."

            mc "Só tô sendo sincero. Acho que nunca te vi tão... relaxada."

            na "É a liberdade, [mc]. Ela faz maravilhas."

            mc "E você merece, depois de tudo o que passou."

            na "Você... no fim você foi muito corajoso, [mc]. Enfrentar o Donatello, a Zaza e todo o Grupo daquele jeito..."

            mc "Você também, Natasha. Atirar nele... aquilo foi..."

            na "Foi necessário. Ele não nos deixaria ir. Ele nunca nos deixaria ser livres. Só espero que seja suficiente."

            "Um calafrio percorre minha espinha. A lembrança do prefeito Donatello caindo no chão, o sangue manchando sua roupa..."

            "A gente tinha escapado por um fio."

            na "Só espero que seja o suficiente pra ela."

            mc "Hm?"

            scene black with dissolve

            scene n8i64 with Dissolve(1.0)

            na "Não vamos falar mais disso. Não foi pra isso que você veio aqui, foi?"

            mc "Não. Agora a gente tá livre. E a gente vai ficar bem."

            na "Eu... eu espero que sim, [mc]."

            "Ela desviou o olhar, ficando um pouco vermelha. Ela tava com vergonha? Nervosa?"

            mc "Natasha... eu..."

            na "O que foi, [mc]?"

            "Foda-se. É agora ou nunca."

            menu:
                "Não é nada. Só queria garantir que você tava bem.":


                    na "Hm... ok... obrigada. Eu vou ficar, prometo."

                    mc "Qualquer coisa que precisar estou por aqui. Vai ser bacana curtir essa nova vida com você."

                    na "Digo o mesmo. Agora vamos aproveitar."

                    mc "Vamos."
                "Eu... queria te beijar.":


                    na "Aqui? Agora?"

                    mc "Sim... aqui... agora."

                    na "Você é um homem de atitude, [mc]. Eu gosto disso."

                    "Ela tem jeito que gosta mesmo..."

                    mc "E você, Natasha... você é..."

                    "Nem sei o que eu tô falando, eu só quero ela."

                    na "Você vai ter seu beijo. Mas não aqui. Vamos pra um lugar mais... reservado."

                    mc "Vamos."

                    scene black with dissolve

                    scene n8i65 with Dissolve(1.0)

                    mc "Hmm... Natasha..."

                    na "Hmmm..."

                    "Parece que ela tava esperando por isso... hmm... faz tempo que eu queria experimentar essa mulher desse jeito."

                    na "Você beija bem, [mc]."

                    mc "Você também, Natasha."

                    na "Vai ser assim agora os nossos dias? Dinheiro, praias, e prazer?"

                    mc "Natasha... eu quero... eu quero você."

                    "Ela tá sorrindo enquanto me beija, um sorriso malicioso e convidativo."

                    na "Eu também quero você, [mc]. Me mostra o quanto."

                    scene black with dissolve

                    scene n8i66 with Dissolve(1.0)

                    "Suas mãos deslizaram pelas minhas costas, me puxando pra mais perto. Tô sentindo os peitos dela pressionados, os mamilos duros me provocando pelo biquíni."

                    na "Ahnn... isso..."

                    mc "E essas mãos no meu shorts, hein?"

                    na "Deixa eu sentir você, [mc]..."

                    mc "Natasha... eu... aah..."

                    "Ela tá abaixando meu shorts e... caraca..."

                    na "Hmm... você tá pronto pra mim..."

                    mc "Tô... mas e você?"

                    scene black with dissolve

                    scene n8i67 with Dissolve(1.0)

                    "Meu Deus... ela vai mesmo fazer isso comigo? Aqui? No meio da praia?"

                    na "Eu nasci pronta, [mc]..."

                    mc "Ah... puta que pariu..."

                    mc "Natasha... você... ah..."

                    "Essa mulher é inacreditável! Que boquinha quente! Ela sabe o que tá fazendo!"

                    na "Hmmm... você é gostoso... adoro seu cheiro... seu gosto."

                    "Ela tá me engolindo inteiro! Se continuar assim..."

                    scene black with dissolve

                    scene n8i69 with Dissolve(1.0)

                    mc "Natasha... eu vou... eu vou..."

                    na "Goza pra mim, [mc]... me enche com sua porra... quero sentir tudo..."

                    "Caralho! Ela tá falando sério! Eu vou gozar na boca dela! Nessa boquinha perfeita..."

                    mc "Natasha... aahh... eu..."

                    scene black with dissolve

                    scene n8i68 with hpunch

                    mc "AAAHHH!!!"

                    "Eu explodi. Uma onda de prazer, meu corpo tremendo, aah... que delícia..."

                    na "Hmmm... isso... me dá tudo..."

                    "Ela engoliu tudo... até a última gota. Que mulher..."

                    na "Hmmm... delicioso..."

                    mc "Natasha... você... você é..."

                    na "Shh... agora é minha vez..."

                    scene black with dissolve

                    scene n8i70 with Dissolve(1.0)

                    "Ela é a mulher mais linda que eu já vi na minha vida."

                    na "Você gosta do que vê, [mc]?"

                    mc "Gostar? Eu... eu tô..."

                    "As palavras fugiram. Eu não conseguia falar. Só olhar. Só desejar."

                    na "Vem cá..."

                    na "Eu quero sentir você dentro de mim, [mc]. Agora."

                    mc "Natasha..."

                    scene black with dissolve

                    scene n8i71 with Dissolve(1.0)

                    na "Isso... aahnn... mexe... me fode..."

                    mc "Natasha... você é... tão gostosa..."

                    na "Você também, [mc]... tão forte... tão... ah..."

                    mc "Isso. Vou te foder do jeito que você merece!"

                    na "Isso! Com força!"

                    scene black with dissolve

                    scene n8i72 with Dissolve(1.0)

                    mc "Natasha... ahnn... eu... eu vou..."

                    na "Goza dentro de mim, [mc]... me enche... me faz sua!"

                    scene n8i73 with hpunch

                    "Eu explodi de novo! Tudo dentro dela!"

                    na "Aaahhh... [mc]... ah... ah!"

                    na "Eu... eu nunca... nunca me senti assim antes... tão amada e desejada... de verdade."

                    mc "Nem eu, Natasha... nem eu..."

                    scene black with dissolve

                    "A gente se vestiu em silêncio, o sol se pondo no horizonte, tingindo o céu com tons de rosa e laranja. Um novo dia. Uma nova vida."

                    "A gente tinha fugido. A gente tinha vencido. E a gente... a gente tava junto."

                    window hide

                    pause

                    pause

                    na "Sim..."

                    na "Me dê mais alguns dias."

                    na "Ele não consegue evitar de me foder. O babaca é Igualzinho ao prefeito."

                    na "Não se preocupe, Cobra."
        "Nah... vamos só curtir a vida boa como amigos":


            if nathan_namoro:

                "Eu não vou trair o Nathan."

    scene black with dissolve

    scene n8i74 with Dissolve(1.0)

    "Caraca... eu consegui mesmo."

    "Acabei com a Zaza, peguei a grana do Grupo. E o prefeito... nem acredito que ele morreu."

    "Parece até um sonho... eu, aqui, longe da Capital, com dinheiro infinito praticamente, sem ter que me preocupar com mais nada."

    "E pensar que tudo começou por causa de uma matéria sobre a Priscila..."

    "A Pri... a Sayuri... a Júlia... a Diana... a Natasha... Sofia..."

    "Tantas mulheres incríveis que eu tive a chance de conhecer... Tantas histórias... tanta coisa que eu passei."

    "Acho que eu nunca vou esquecer delas. Elas mudaram minha vida. Me mostraram um mundo que eu nunca imaginei que existisse."

    "Um mundo de glamour, de poder, de sedução... mas também de dor, de sofrimento, de traição..."

    "A Capital... aquela cidade maldita... ela me apunhalou, mas me ensinou muita coisa. Me fez crescer. Me fez... ser quem eu sou hoje."

    "Eu não sou mais aquele garoto inocente que chegou na ilha. Aquele jornalista que só queria um emprego, sem ideais, sem vontade."

    "Eu vivi muita coisa. Vi o lado obscuro da humanidade. Eu vi... como o mundo é de verdade."

    "E essa verdade me libertou."

    "Eu escolhi meu caminho. Eu escolhi a minha felicidade. E eu não me arrependo."

    "Acho que elas vão ficar bem."

    "O Grupo... o Tony... eles vão continuar lá. Controlando a cidade, mas agora sem o prefeito."

    "Eles são grandes demais. Eles vão continuar manipulando vidas. Mas eu não tô mais no jogo deles. Eu tô fora. Então foda-se."

    "Agora é só curtir essa nova vida. Viajar o mundo. Aproveitar cada segundo ao lado dos meus amigos, dos meus amores. Ser feliz."

    "Eu mereço."

    "A gente merece."

    "A gente conquistou isso."

    "E ninguém vai tirar isso da gente."

    "Ninguém."

    scene black with Dissolve(3.0)

    pause

    $ persistent.nathan_final1 = True

    "{i}FIM{/i}"

    pause

    p "Essa foi uma escolha digna de um jogador! No meu mundo, fada só fica com um macho de cada vez, e eu ainda tô tentando me livrar do meu..."

    p "Mas você sabe que essa história com o Nathan pode ter outros finais. Se você voltar e fizer outras escolhas..."

    p "O que será que acontece se o [mc] decidir ficar do lado da Natasha e do Fabrício e lutar contra o prefeito?"

    p "E a Zaza? O que será que aconteceu com ela? Ela vai perdoar você e o Nathan?"

    p lecionando "Junte todas as peças do quebra-cabeça! Descubra os outros finais! E se prepare para surpresas de outro mundo!"

    p "Você também pode ver todos os finais que você já conquistou no menu Personagens! Só clicar na fotinho dele e você terá acesso aos seus incríveis feitos!"

    p "Até a próxima, jogador! ;)"

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 1 do Nathan! Você pode acessar o menu Personagens e apertar no botão dele para ver sua conquista!{/b}"

    scene white with dissolve

    $ renpy.full_restart()





    "Mas... a Natasha..."

    "Ela observava a cena com um olhar frio, calculista. Sua alegria era contida, distante."





    na "Espero que vocês aproveitem bem essa felicidade, porque ela vai ser curta."

    "Sua voz cortou o ar, gélida, como um vento cortante. A ameaça dela me atingiu como um balde de água fria, apagando a chama de euforia que me aquecia."

    na "O Grupo não vai deixar isso barato. Eles vão encontrar vocês. Não importa para onde vocês fujam."

    "O medo voltou, me apertando o peito, me sufocando. O Marco... a vingança deles..."

    "Eu tinha feito a escolha errada? Tinha condenado o Nathan e a mim a uma vida de fuga, de medo?"

    "Olhei para o Nathan. Seu sorriso se apagou, a alegria em seus olhos se transformou em apreensão. Ele também sentiu o peso da ameaça da Natasha."

    mc "Eu tenho certeza."

    "As palavras saíram da minha boca antes que eu pudesse pensar. Certeza? Que certeza eu tinha? Mas eu não podia demonstrar medo. Não podia fraquejar."

    na "Certeza? Você tem certeza do quê?"

    "Seu olhar penetrante me analisava, buscando qualquer sinal de dúvida, de hesitação."

    mc "Eu tenho o contrato da Roxane. O contrato que prova que a Zaza comprou ela. O contrato que pode destruir a Blergh!."

    "Eu disse com a voz firme, sem vacilar. Era minha única arma. Minha única chance."

    "A Natasha... seus olhos se arregalaram, a máscara de poder se estilhaçando por um instante. Ela estava surpresa."

    mc "Se você levar a gente até o aeroporto, eu não vou entregar ele pra revista."

    "A proposta estava feita. Um contrato pela nossa liberdade."

    na "..."

    "O silêncio dela era ensurdecedor. Ela estava pensando, calculando os riscos, as consequências."

    "Eu prendi a respiração, esperando sua resposta. Minha vida, o futuro do Nathan... tudo dependia da decisão dela."

    menu:
        "Eu tenho certeza.":


            na "Muito bem, [mc]. Você venceu. Vamos."

            "Ela disse com um suspiro resignado. Ela tinha aceitado o acordo."

            "Eu soltei o ar que nem sabia que estava prendendo. Uma onda de alívio me inundou, me deixando fraco, quase sem forças."

            "Olhei para o Nathan. Ele estava radiante, um sorriso enorme iluminando seu rosto. Ele tinha recuperado a esperança."

            "E a Zaza..."



            za "Seja feliz, Nathan. E parabéns por lutar pelos seus sonhos. Estou orgulhosa."

            "Ela disse com um sorriso triste, melancólico. Era um adeus. Um reconhecimento de sua derrota."

            "Eu não conseguia sentir raiva dela. Nem ódio. Só pena."









            "A Natasha dirigiu até o aeroporto da prefeitura. Em silêncio. Sem trocar uma palavra."

            "O Nathan segurava minha mão, seus dedos entrelaçados nos meus. Ele não precisava dizer nada. Sua presença era o suficiente."

            "A Capital... a cidade que tinha me acolhido... que tinha me dado oportunidades... que tinha me mostrado o lado obscuro da humanidade..."

            "Eu estava deixando ela para trás. Para sempre."

            "Mas eu não estava triste. Eu estava livre."
        "Preciso pensar melhor.":




            jump nathan_final_escolha



    n "Você acredita que a gente tá aqui?"

    mc "Às vezes eu ainda acho que tô sonhando."

    n "Eu também."

    mc "Mas é real. A gente tá aqui. Juntos."

    n "E com grana pra caralho."

    mc "Haha... verdade."

    n "A Zaza deve tá uma fera com a gente."

    mc "A Cássia também."

    n "Mas foda-se. A gente tá bem."

    mc "É o que importa."



    mc "Hmm..."

    n "Eu te amo, [mc]."

    mc "Eu também te amo, [n]."



    n "Sabe... eu nunca imaginei que ia ser tão feliz."

    mc "Eu também não."

    n "Você mudou minha vida, [mc]."

    mc "Você também mudou a minha."

    n "Pra melhor, claro."

    mc "Com certeza."



    n "Sabe, [mc]... quando eu te dei aquela pauta pra você entregar pra Cássia, eu achei que tava realizando meu sonho."

    mc "Ser modelo?"

    n "Sim. Era tudo o que eu queria. Ser famoso, ter dinheiro, viajar pelo mundo."

    mc "E você conseguiu."

    n "Consegui. Mas não foi do jeito que eu imaginava."

    mc "Por causa da Cássia?"

    n "Por causa dela e por causa de mim também. Eu me deixei levar pela ambição. Eu queria tanto realizar meu sonho que acabei me perdendo no caminho."

    mc "Mas você se encontrou de novo."

    n "Graças a você."



    n "Você me mostrou que a vida boa não é feita de fama e dinheiro. A vida boa é feita de momentos simples, de amor, de companheirismo."

    mc "Eu também aprendi muito com você."

    n "Aprendeu o quê?"

    mc "Que às vezes nossos sonhos são apenas armadilhas. Que a verdadeira felicidade está nas coisas mais simples da vida."

    n "Uau..."

    mc "Não precisa tirar sarro!"

    n "Haha... Sabe o que eu tava pensando?"

    mc "O quê?"

    n "Que a gente podia viajar pelo mundo. Conhecer lugares novos."

    mc "Eu topo."

    n "Sério?"

    mc "Claro. Com você, eu vou pra qualquer lugar."

    n "Eu também."



    mc "Hmm..."

    n "Eu te amo tanto..."

    mc "Eu também te amo..."

label nathan_final2:

    mc "Nathan, escuta..."

    n "Eu sei... eu sei que é loucura. Mas..."

    mc "Não é questão de loucura! Seria uma boa fugir de tudo, mas esta é a sua chance de fazer a diferença, cara!"

    n "Mas fugir... com essa grana... com você... a gente podia..."

    mc "Você não pode, Nathan! Você não pode abandonar a sua missão! E eu também não quero sair assim."

    n "[mc]..."

    mc "Eu sei que tá sendo difícil. A Cássia, a Zaza... elas tão te manipulando, te usando. Mas você não pode deixar elas vencerem!"

    scene black with dissolve

    scene n8i79 with Dissolve(1.0)

    pause 2.0

    mc "Você é mais forte que isso, Nathan! Você tem um propósito! Você tem uma missão! E eu vou te ajudar a cumprir ela!"

    n "Você... você tá falando sério, [mc]?"

    mc "Claro que eu tô! A gente vai lutar junto! A gente vai acabar com essa merda de Grupo e libertar essa cidade!"

    gar "Excelentes palavras, meu caro [mc]! Excelentes palavras! O espírito de luta reacendeu em vossas almas!"

    gar "A chama da justiça, antes mortiça, agora arde com a intensidade de mil sóis! Que os desígnios obscuros tremam diante de vossa determinação!"

    na "Mas... [mc]... você... você tem certeza disso? Você viu o que eles são capazes de fazer."

    "Natasha... qual é a sua, hein?"

    mc "Tenho. E eu não vou deixar o medo me controlar. A gente vai acabar com essa palhaçada!"

    mc "A gente vai garantir que eles não usem mais garotas como a Roxane, a Diana, a Priscila... a gente vai libertar todas!"

    n "E-eu... eu não sei o que dizer, [mc]. Você... você me inspira. Eu também vou lutar! A gente vai vencer essa porra!"

    na "Vocês... vocês não fazem ideia."

    gar "Essa expressão usada em demasia deixará rugas em sua linda cute, parceira de labuta."

    menu:
        "Mesmo que não dê em nada. Eu... eu não tô pronto pra sair da cidade e abandonar tudo.":


            pass

    n "[mc]..."

    za "Meu dinheiro..."

    mc "Zaza."

    scene black with dissolve

    scene n8i80 with Dissolve(1.0)

    pause 2.0

    za "Se vocês não vão fugir, eles vão matar vocês."

    "Ela tá certa... eu roubei o Grupo. Se eles descobrirem..."

    menu:
        "Eu vou te devolver o dinheiro.":


            pass

    mc "Mas você tem que prometer que não vai falar nada sobre o que aconteceu aqui."

    za "Você... você tá falando sério?"

    mc "Tô. Mas essa é a única condição. Você vai ficar quieta. Por enquanto."

    za "..."

    "Ela hesita por um instante, os olhos fixos na mochila, no dinheiro."

    za "Eu aceito. Me dê o dinheiro."

    za "Mas... eu quero saber... o que está acontecendo? Que missão é essa?"

    mc "Eu também. Eu quero saber que merda é essa que envolve o Nathan, o Fabrício e a Natasha."

    n "Bom... É hora de você saber a verdade, [mc]. A verdade sobre a gente... e sobre o que a gente tá fazendo aqui."

    "A verdade... então realmente tá acontecendo algo aqui. Aquela história de Cidade Dourada é verdade?"





    menu:
        "Quem são vocês?":


            pass



    scene black with dissolve

    scene n8i81 with Dissolve(1.0)

    pause 2.0

    na "A gente não é daqui. A gente veio de longe. Da Rússia."

    menu:
        "Rússia?! Mas... por quê?!":


            pass

    n "A gente foi enviado pela Interpol, [mc]. Pra investigar o Grupo. Pra acabar com essa rede de corrupção e tráfico que domina a Capital."

    mc "Interpol?! A polícia internacional?!"

    gar "Meu caro [mc], o senhor Nathan está lhe revelando a mais pura e cristalina verdade! O destino desta urbe encontra-se em nossas mãos!"

    gar "E a justiça, como um rio caudaloso, em breve inundará as vielas escuras da corrupção!"

    n "Cidade Dourada. Esse é o codinome da missão. E a gente tá aqui pra tirar o poder do Grupo e devolver a Capital ao povo."

    mc "Cidade Dourada... Grupo... mas... mas..."

    n "Você tem alguma pergunta?"

    menu:
        "O que é a Interpol?":


            n "A Interpol é a maior organização policial do mundo. Eles atuam em mais de 190 países e lutam contra todo o tipo de crime."

            gar "Exatamente! Sua missão primordial é combater o crime organizado transnacional. Facilitamos a cooperação policial entre nações."

            mc "Se você tá falando de crimes transnacionais... isso quer dizer que o 'Grupo' aqui da capital tem conexões internacionais?"

            na "Sim. A Interpol já vinha investigando o Donatello, o Barão e os Alighieri por anos. Mas eles precisavam de uma equipe pra atuar de dentro."

            mc "E por que vocês?"

            n "Fomos treinados pra isso. Somos agentes de elite."

            na "Somos os melhores. E a Capital precisa dos melhores."
        "Como vocês vieram parar aqui?":


            n "A gente tava em uma missão na Europa e a Interpol nos recrutou. A gente se encaixava no perfil... jovens, discretos."

            n "E com habilidades... A gente tava pronto pra uma nova aventura, hehe..."

            gar "Pois bem! Após meses de treinamento, fomos enviados à capital para nos infiltrarmos e coletarmos provas contra o Grupo. Uma tarefa deveras desafiadora!"
        "Por que vocês estão me contando isso?":


            n "Você é importante pra gente, [mc] e a Zaza também. Você pode ser nossa aliada. Você tem informações, você tem contatos..."

            n "Vocês podem nos ajudar a acabar com essa merda de uma vez por todas."

            gar "Exatamente! Precisamos de pessoas como a senhora para desmantelar essa organização criminosa! Una-se à nossa causa e lute pela justiça!"

    mc "Mas a Natasha? Ela não trabalha pro prefeito? Ela é..."

    scene n8i82 with hpunch

    pause 2.0

    za "[na]! Você... você também?!"

    "A Zaza encarou a Natasha, a voz trêmula, incrédula."

    na "..."

    za "Você... você está enganando o prefeito Donatello? Você está... mentindo pra ele esse tempo todo?"

    na "Sim, Zaza. É verdade."

    mc "!"

    mc "Natasha..."

    "A Natasha... a secretária fria e calculista... ela tava lutando contra o Grupo esse tempo todo?"

    gar "Meus parabéns, senhorita Natasha! Sua coragem é inspiradora! Enfrentar o Leviatã da Corrupção disfarçada de beleza e poder! É um ato digno dos maiores heróis!"

    na "Não... não sou heroína. Eu só quero terminar o trabalho."

    na "Eu sei que você está chocada, Zaza. Tudo o que eu passei na mão deles, tudo o que eu passo até agora, é com foco no objetivo."

    menu:
        "Acabar com o Grupo.":


            pass

    gar "Corretíssimo como sempre, inestimável companheiro. Estes estrumes prejudicaram vidas inocentes incontáveis e não irão cessar."

    za "Roxane..."

    mc "Então... você realmente tá do nosso lado, Natasha?"

    na "Sim, [mc]. Eu estou. "

    gar "Estamos todos unidos nesta batalha contra a iniquidade! Avante, guerreiros da justiça! Que a luz da verdade ilumine nossos caminhos!"

    n "Mas... e agora, [mc]? Você... você vai entrar nessa com a gente?"

    scene n8i83 with hpunch

    pause 2.0

    mc "E-eu?! Envolvido com a Interpol?!"

    "O jeito que ele me olha... seus olhos azuis fixos nos meus, a expressão séria."

    "Que merda é essa?! Eu nunca... como eu ia saber que eu tava me envolvendo nisso?! Eu sou só um paparazzo!"

    n "Você viu o que a gente tá enfrentando. O Tony, a Cássia, o prefeito... eles não vão hesitar em te eliminar se você ficar do nosso lado."

    "A mochila... eu ainda tava com ela. O dinheiro, eu ainda posso fugir. Chamar a Natasha, o Fabrício, o Nathan... e fugir de toda esta merda."

    mc "Meu Deus..."

    "Eu tenho que fazer a escolha mais importante da minha vida. A escolha que vai definir meu destino."

    menu:
        "Nathan, eu já escolhi. Eu vou lutar com vocês.":


            pass
        "Nathan... isso é loucura demais. Vamos pegar o dinheiro e fugir.":


            $ nathan_final = 1

            mc "Eu não aguento isso!"

            n "[mc]..."

            mc "Você viu o que aconteceu com a Nona! Você viu o que o Tony fez com ela! Eu não quero acabar daquele jeito!"

            gar "Ora, meus caros! Acaso a liberdade não tem um preço? Acaso a justiça não exige sacrifícios? Acaso a verdade não precisa ser conquistada?"

            mc "Não, Fabrício! Não dessa vez! Eu não quero ser um herói! Eu só quero viver!"

            mc "Vamos embora, Nathan. Vamos pegar o dinheiro e fugir. Vamos recomeçar nossas vidas. Longe daqui. Longe de tudo isso."

            jump nathan_final1

    $ nathan_final = 2

    $ nathan_final2 = True

    n "Então... você prefere ficar e lutar do que sair vazado e viver no bem bom? Tem certeza?"

    mc "Tenho. Eu sei que eu sou só um jornalista, mas... até hoje eu nunca fugi da Capital. Foda-se, eu vou ficar e lutar."

    scene black with dissolve

    scene n8i84 with Dissolve(1.0)

    pause 2.0

    za "Mesmo com o apoio da Interpol isso é loucura. Vocês têm ideia de quem são essas pessoas? Do poder que eles têm?"

    n "A gente sabe, Zaza. A gente tá investigando eles há anos. A gente sabe como eles operam."

    za "Investigando? Anos? Mas... mas isso é impossível! Ninguém desafia o Grupo e sai impune!"

    za "Eles controlam tudo! A prefeitura, a polícia, os tribunais... a mídia! Eles estão em todos os lugares!"

    za "A família Donatello... eles estão na política há gerações! Desde a fundação da capital!"

    za "Eles têm conexões com a máfia italiana, com políticos corruptos, com empresários inescrupulosos... eles são intocáveis!"

    menu:
        "Ela tem um ponto. Talvez eu deva só ficar quieto e não entrar nessa briga.":


            "Ficar pianinho pode ser a melhor escolha pra alguém normal igual eu."

            "Nem contra, nem a favor."
        "A gente sabe, Zaza. Mas a gente não vai desistir. A gente vai derrubar eles.":


            za "Quem é você pra afirmar isso?"

            mc "Eu sou o [mc]. E eu podia ter te derrubado se eu quisesse."

            gar "Ora, ora."

            n "Toma..."

            za "..."

    za "Derrubar? Mas como? Vocês são só... três! E um deles ainda é um simples jornalista! Vocês não têm chance!"

    na "A gente tem, Zaza. A gente tem a verdade do nosso lado. E a gente tem você."

    na "Você viu o que eles estão fazendo. Com a Roxane, inclusive... com tantas outras. Você vai ficar parada, vendo eles destruírem vidas? Você vai se calar?"

    na "Eu pensei que você estivesse falando honestamente, quando defendeu as mulheres."

    za "Eu... eu quero ajudar, Natasha. Mas... eles são poderosos demais. Se eu me voltar contra eles... eles vão destruir a Blergh! e vão destruir a mim."

    scene black with dissolve

    scene n8i85 with Dissolve(1.0)

    pause 2.0

    mc "Pensa, Zaza. Eles já estão destruindo você. Eles estão te usando, te manipulando, te controlando. Você não vê?"

    mc "Você queria entrar pro Grupo. Você queria o poder deles. Mas olha o preço que você está pagando!"

    mc "Você está sacrificando seus valores, sua integridade... você está se perdendo!"

    gar "Senhora Zaza, permita que este humilde servo lhe diga: a serpente da corrupção já se enroscou em seu corpo."

    gar "Seus dentes venenosos a lhe injetar o veneno da ambição desmedida! Liberte-se dessas amarras nefastas e abrace a luz da justiça!"

    za "Mas... como? Como podemos derrotar essa força quase milenar? Eles são..."

    menu:
        "Isso aí é com eles três...":


            pass

    n "Eles não são invencíveis, Zaza. Eles têm seus pontos fracos. A gente vai derrubar eles por dentro."

    mc "Uma coisa eu sei. Eles nunca vão mudar, Zaza. Eles nunca vão te dar o que você quer. Eles nunca vão te aceitar de verdade."

    mc "Você viu o que aconteceu na festa. O prefeito nem sequer te ouviu!"

    mc "Ele te humilhou, Zaza! Ele te tratou como se você fosse... insignificante! Ele nunca vai te dar o respeito que você tá buscando!"

    "Eu tô vendo nos olhos dela. A raiva e a frustração."

    mc "Eles nunca vão mudar, Zaza. Eles nunca vão dar chance pras mulheres. Pra eles, vocês não passam de uma etapa do Ritual."

    za "..."

    za "Nem acredito que eu vou dizer isso. Mas... Você... você tá certo, [mc]."

    za "Se algo ficou claro hoje, é que eles não se importam comigo. Não importa o quanto eu rale, eles nunca vão me dar um lugar na mesa."

    mc "Então você vai nos ajudar, Zaza?"

    za "Sim, [mc]. Eu vou. Eu vou lutar com vocês. Eu vou ajudar a derrubar o Grupo."

    n "Zaza!"

    scene black with dissolve

    scene n8i86 with Dissolve(1.0)

    pause 2.0

    gar "Glória! Glória! A união faz a força! A justiça prevalecerá! Que os céus abençoem essa aliança improvável!"

    za "Agora, deixa eu falar. [mc]... Você tem o dom das palavras. Você consegue tocar o coração das pessoas. Você consegue... abrir os olhos delas."

    mc "E-eu?"

    za "Desde a primeira que eu te vi aqui na Blergh!. Eu senti sua energia. Eu lhe disse, que você era bom em tirar a verdade das pessoas."

    mc "Eu... nunca pensei nisso."

    za "Esse dom de convencer... isso é muito mais valioso que qualquer força, que qualquer arma."

    n "Esse é o [mc]. Concordo totalmente."

    menu:
        "Eu... valeu, gente.":


            pass

    gar "Nosso homem prodígio! Salvador da pátria!"

    "A Natasha sorri pra mim. Ela parece orgulhosa de mim, mas eu também sinto outra coisa em seus olhos."

    n "Nem acredito que eu acabei falando a verdade pra Zaza... e ela tá do meu lado."

    za "Nathan, Nathan... quem diria que além de um corpo gostoso você tinha todo esse mistério."

    n "..."

    na "Mais importante, como vocês esperam que ela ajude a gente? A Zaza não tem poder dentro do Grupo."

    mc "Zaza?"

    za "Deixe comigo, [mc]. Eu tenho meus métodos."

    za "Quando chegar a hora, eu vou garantir que o Donatello não tenha o que precisa."

    mc "Como você vai fazer isso?"

    za "Ele não vai ter mais a Blergh!. Esse é o primeiro passo."

    za "Mas isso não é o suficiente. Os outros pilares precisam cair... ou se juntar a nós."

    za "Vocês vão ter que derrubar todos os pilares que sustentam o Grupo antes da eleição."

    menu:
        "Derrubar os pilares? Antes da eleição?":


            pass

    za "O Basílio... ele não pode ter ajuda de ninguém. Nem dinheiro, nem influência, nem a mídia."

    za "Todos os aliados dele precisam cair. O Barão, o Tony, o Gevanni... a Jidao, a Sayuri... talvez até o Distrito... a Faux News..."

    za "Se ele tiver dinheiro de ao menos uma dessas fontes... ele ainda tem chance de ser reeleito. A gente precisa cortar as asas dele antes que ele voe!"

    mc "Caralho... você tá falando sério?"

    "Eu me sinto sufocado. O peso da missão, da responsabilidade... é esmagador."

    "O Barão... o Tony... o Gevanni... a Jidao, a Sayuri... talvez até o Distrito... a Faux News... todos eles?"

    "Como a gente pode fazer isso? É impossível!"

    menu:
        "Isso é loucura, Zaza! A gente não tem como derrubar todos eles!":


            n "A gente tem, [mc]! A gente tem que ter! Não podemos deixar eles vencerem! Eles vão destruir tudo se a gente não fizer nada!"

            mc "Mas... por onde a gente começa? Quem a gente ataca primeiro?"

            na "A gente precisa pensar em um plano. Um plano infalível. A gente precisa ser inteligentes... a gente precisa ser..."
        "A gente tem que tentar. Não podemos desistir.":


            mc "A Nona não desistiu. Ela arriscou tudo pra tentar mudar essa cidade."

            n "Mas a Nona... ela..."

            mc "Ela tava sozinha. Mas a gente não tá. A gente tem a Natasha lá dentro. A gente tem um ao outro."

            za "Você... você realmente acredita que a gente pode fazer isso?"

            mc "Acredito. E eu vou lutar com vocês até o fim."

            za "..."
        "A gente precisa de um plano. E a gente precisa agir rápido.":


            mc "Ok. Eu tô com vocês. Mas a gente precisa de um plano. E a gente precisa agir rápido."

            n "Sim... você tem razão. A gente não pode perder tempo."

    gar "Meus caros! Que este humilde servo possa contribuir com sua insignificante sabedoria!"

    gar "Devemos traçar uma estratégia minuciosa, como um general a preparar suas tropas para a batalha!"

    gar "Cada passo, cada movimento, deve ser calculado com a precisão de um relógio!"

    scene black with dissolve

    scene n8i87 with Dissolve(1.0)

    pause 2.0

    na "Eu concordo com o Fabrício. A gente precisa ser inteligentes. A gente não pode agir por impulso"

    n "A gente vai fazer isso, [mc]. A gente vai acabar com eles. Juntos."

    mc "Juntos."

    za "Eu... eu também. Eu não vou deixar eles vencerem."

    na "Eu vou fazer o que precisa ser feito. Podem contar comigo."

    "Ela diz isso com um olhar frio e determinado. Ela não está brincando. "

    menu:
        "Ok... então... por onde a gente começa?":


            pass

    za "Primeiro passo... tudo precisa voltar ao normal. O Donatello não pode nem sonhar que o dinheiro correu risco."

    za "E ele jamais pode saber que a Natasha quer o pescoço dele."

    na "Pode deixar que ele não vai saber por mim."

    za "Nathan, você precisa voltar a trabalhar. Focar na Blergh!. Fazer o Basílio ter certeza de que ele está seguro com a marca, com você."

    n "Mas..."

    za "Sem 'mas', Nathan. Você precisa se dedicar. Mostrar pra ele que você é o modelo perfeito. O rosto da Capital."

    gar "Exato, senhor Nathan! Vossa Magnificência precisa cegar o Basílio com o brilho de vossa estrela!"

    gar "Ele precisa se sentir seguro, confiante... precisa acreditar que a vitória é iminente!"

    na "Você vai ter minha ajuda, amigo. Eu vou garantir que ele acredite nisso."

    na "Vou fazer a cabeça dele pra que ele se sinta o todo poderoso, o único capaz de liderar a Capital."

    gar "Magnífico! Ele não pode procurar salvaguardas! Precisa acreditar que a eleição está ganha, que não precisa de alianças!"

    za "E vocês dois... [mc], Nathan... vocês precisam se afastar. Por enquanto."

    "Eu sabia que isso ia acontecer, mas... a ficha caindo dói."

    n "Mas a gente..."

    za "É o melhor pra todos, Nathan. Você precisa focar no trabalho. E o [mc]... ele precisa se proteger."

    na "O Tony sabe quem você é, [mc]. Ele está de olho em você. Se ele descobrir que você está envolvido com a gente..."

    mc "..."

    n "Mas, Zaza..."

    na "Nathan. É preciso. Pela missão. Pela gente. "

    scene black with dissolve

    if nathan_namoro:

        scene n8i89 with Dissolve(1.0)

        pause 2.0

        n "[mc]... eu não queria que as coisas fossem assim..."

        "Sua voz é um sussurro, cheia de tristeza."

        mc "Eu sei, amor. Eu também não."

        "Meu coração dói. Eu não quero me afastar dele."

        n "Eu vou sentir tanta saudade..."

        mc "Eu também. Mas a gente vai se ver de novo. Eu prometo."

        "Eu o abraço de volta, sentindo o cheiro do seu perfume, o calor do seu corpo. Quero gravar esse momento na memória."

        scene black with dissolve

        scene n8i90 with Dissolve(1.0)

        pause 2.0

        mc "Hmm..."

        n "Eu te amo, [mc]."

        mc "Eu também te amo, Nathan."

        gar "Não seria esse o momento de separação árdua no clímax de uma novela?!"

        za "Cala a boca."
    else:


        scene n8i88 with Dissolve(1.0)

        n "Cara... que merda, hein?"

        mc "É... que merda."

        n "Você... você vai ficar bem?"

        mc "Vou. E você também."

        n "A gente não vai se perder, prometo."

        mc "Isso aí. A gente é parceiro, lembra?"

        n "Parceiro até o fim."

    gar "Pois bem, meus caros! O destino nos compele a agir com a presteza de um falcão e a sutileza de uma pantera!"

    gar "Que o manto da discrição nos envolva, enquanto a tempestade se aproxima!"

    za "Ele tem razão. É hora de voltarmos aos nossos postos e fingirmos que nada aconteceu."

    na "Concordo. Quanto antes essa reunião acabar, melhor."

    n "Então vamos lá."

    mc "Vamos."

    za "Adeus."

    "A Zaza... ela... ela precisa"

    scene n8i91 with hpunch

    pause 2.0

    mc "Zaza, espera."

    za "Hm?"

    mc "Tem uma última coisa que você precisa resolver antes de voltar ao 'normal'."

    za "O que você quer dizer?"

    mc "A Roxane. Ela sabe."

    za "Sabe? Sabe do quê?"

    mc "Ela sabe sobre o contrato. Sobre a verdade."

    za "Ela é forte. Ela vai entender."

    mc "Ela merece uma conversa. Uma explicação."

    za "Eu não preciso me justificar para ela."

    mc "Talvez não precise. Mas você deveria."

    "A Zaza me encara, seus olhos frios e impassíveis. Ela não gosta de ser contrariada."

    za "Vamos."

    scene black with dissolve

    pause 1.0

    scene n8i92 with hpunch

    pause 2.0

    ro "Você me usou!!!"

    ro "Você... você me tirou da minha família! Apagou meu passado! Me transformou em... em um produto! Uma ferramenta para seus planos ambiciosos!"

    za "..."

    "Caraca... a Zaza nem se mexe."

    ro "Você... você me enganou esse tempo todo! Me fez acreditar que você me amava! Que você se importava comigo!"

    ro "E agora... agora eu descubro que tudo foi uma farsa! Que eu não passo de uma... de uma..."

    za "Roxane... acalme-se. Você precisa se controlar."

    "A Zaza nem se mexe... ela não cede à fúria da Roxane. Ela a encara de frente, sem se intimidar."

    scene n8i93 with hpunch

    ro "Controlar?! Como você pode me pedir pra me controlar?! Você destruiu a minha vida! Me roubou da minha família! Me fez esquecer quem eu sou!"

    za "Eu fiz o que precisava ser feito. E você vai entender. Com o tempo."

    ro "Entender?! Você acha que eu posso simplesmente 'entender' uma coisa dessas?! Você acha que eu posso esquecer o que você fez comigo?!"

    za "Roxane... eu sei que é difícil. Mas você é forte. Você vai superar isso."

    ro "Superar? Como eu posso superar uma coisa dessas? Como eu posso confiar em você de novo? Como eu posso..."

    za "Roxane. Você precisa ser forte. A vida é feita de escolhas difíceis."

    za "E às vezes a gente precisa fazer o que é necessário, mesmo que doa. Mesmo que... machuque."

    ro "..."

    ro "Você... você realmente acredita nisso?"

    za "Acredito. E você também vai acreditar. Um dia."

    ro "..."

    scene n8i94 with hpunch

    ro "[mc]... você... você precisa me ajudar."

    "Eu?! Eu só queria confirmar que a Zaza ia conversar com a Roxane..."

    mc "Roxane... eu... eu não sei se sou a pessoa certa pra..."

    ro "Você é! Você que me mostrou a verdade! Você viu o contrato! Você sabe o que ela fez comigo!"

    ro "Eu confio em você, [mc]. Me diz... o que eu devo fazer? "

    za "..."

    "A Zaza tá quieta. Ela confia na força da Roxane. Mas será que confia em mim?"

    ro "Eu devo voltar? Voltar pro Distrito? Pra minha... origem? Pra minha... raiz?"

    ro "Ou eu devo... perdoar a Zaza? Continuar com a Blergh!? Realizar meu sonho de ser uma modelo internacional?"

    scene black with dissolve

    scene n8i95 with Dissolve(1.0)

    pause 2.0

    "Caralho... que responsabilidade. A decisão que eu tomar vai mudar a vida da Roxane pra sempre."

    "O Distrito... a promessa de resgatar sua identidade, sua história, sua família... mas desistir do seu sonho."

    "A Zaza... a chance de brilhar nos palcos, de conquistar o mundo da moda..."

    "... mas também a sombra da manipulação, do controle, estar com a pessoa que te tirou da sua família e escondeu tudo."

    "E não é só ela. Distrito ou Zaza? Quem eu quero ajudar? Isso pode mudar minha própria história!"

    "Qual caminho eu vou escolher pra ela?"

    menu:
        "Roxane, você precisa voltar para o Distrito. Para sua família.":


            $ roxane_distrito = True

            mc "Roxane, você precisa voltar para o Distrito. Para sua família. Você precisa descobrir quem você é, de onde você veio."

            ro "Mas... e a Zaza? E a Blergh!?"

            mc "A Zaza vai entender. E a Blergh!?... A Blergh! não é o mais importante agora. Você precisa se encontrar. Encontrar suas raízes."

            ro "Eu... eu não sei..."

            mc "Roxane, eu sei que é difícil. Mas é a decisão certa."

            mc "Você precisa se libertar desse passado que te assombra. Você precisa voltar pra casa."

            scene black with dissolve

            scene n8i97 with Dissolve(1.0)

            pause 2.0

            ro "Você tem razão, [mc]. Eu vou. Eu vou voltar pro Distrito."

            ro "Obrigada por tudo, Zaza. Mas agora... agora eu preciso seguir meu próprio caminho."

            "A Zaza a encara, os olhos frios, mas com um brilho de tristeza. Ela assente com a cabeça, sem dizer uma palavra."

            mc "Eu vou te ajudar, Roxane. Vou te levar até o Black Cash. Ele vai te ajudar a se readaptar."

            "Eu sei que fiz a escolha certa. Eu libertei a Roxane do passado. E agora... ela está livre para encontrar seu futuro."

            za "Adeus, Roxane. Seja a garota forte que você sempre foi."

            ro "Adeus, Zaza. Eu serei."
        "Roxane, você precisa seguir seu sonho. Ficar com a Blergh!.":


            $ roxane_distrito = False

            mc "Roxane, você precisa seguir seu sonho. Ficar com a Blergh!. Você tem talento, você tem potencial... você pode conquistar o mundo!"

            ro "Mas... e o meu passado? A minha família?"

            mc "O passado não pode te controlar, Roxane. Você precisa se libertar dele. Você precisa construir seu futuro. E a Zaza... a Zaza pode te ajudar."

            mc "Ela te trouxe até aqui. Agora é com você."

            ro "Mas... e o Distrito?"

            mc "O Distrito sempre vai estar lá, Roxane. Mas você não precisa voltar pra lá pra ser feliz. Você pode ser feliz aqui. Com a Blergh!. Com a Zaza."

            ro "Eu... eu não sei, [mc]..."

            mc "Roxane, confia em mim. Fica. Você não vai se arrepender."

            scene black with dissolve

            scene n8i97 with Dissolve(1.0)

            pause 2.0

            ro "Você tem razão, [mc]. Eu fico. Eu vou ficar com a Blergh!."

            ro "Obrigada, Zaza. Obrigada por acreditar em mim."

            za "Sempre, minha querida. Vamos dominar o mundo, você e eu."

            ro "Você e eu."

            za "Agora tenho uma festa para encerrar, depois de tudo o que aconteceu."

            za "Depois nos falamos... filha."

    za "Adeus, [mc]."

    mc "A-até..."

    show black with dissolve

    "Ela se foi. Somos só eu e a Roxane agora."

    hide black with dissolve

    ro "Obrigada, [mc]. Obrigada de verdade por me ajudar."

    mc "Eu sei que você vai ser feliz, Roxane. Você é linda, inteligente, determinada... você tem tudo pra..."

    mc "!"

    scene n8i96 with hpunch

    pause 2.0

    mc "R-Roxane..."

    ro "Desculpa... eu... só me deu vontade de te beijar depois de tudo o que você fez por mim."

    "Seu olhar é intenso, provocante. Ela tá realmente grata."

    "A Roxane... ela é linda, sexy, irresistível. E ela está bem aqui, na minha frente, me desejando."

    "Eu tenho que me controlar. Não posso..."

    menu:
        "Roxane... melhor a gente parar por aqui...":


            mc "Roxane... é melhor a gente parar por aqui. A Zaza... ela pode..."

            ro "Eu sei... você tem razão. Desculpa..."

            "Eu perdi a chance. Mas talvez seja melhor assim."

            scene black with dissolve

            scene n8i97 with Dissolve(1.0)
        "Eu não consigo resistir a você...":


            mc "Roxane... eu... eu não consigo resistir a você..."

            ro "Ah... [mc]... me lambe... eu preciso disso."

            mc "Sua gostosa. Eu quebro essa pra você..."

            ro "Ahnn... p-por favor..."

            scene black with dissolve

            scene n8i98 with Dissolve(1.0)

            pause 2.0

            "Ah... que xotinha delícia..."

            ro "Hmm... [mc]... chupa... chupa mais forte... me deixa louca..."

            mc "Você é tão gostosa... tão molhada... tão..."

            "Ai... [mc]... você... você é tão grande..."

            mc "Cala a boca e goza pra mim, delícia..."

            ro "Ah... [mc]... mais, mais forte... me fode com essa línguia, me fode até eu..."

            mc "Goza, vadia... goza pra mim..."

            ro "Ah... [mc]... eu preciso de você... preciso sentir você..."

            mc "Roxane... aqui... agora..."

            ro "Sim... aqui... na mesa da Zaza... quero que ela saiba... que eu não sou mais a bonequinha dela..."

            mc "Você é uma deliciosa... tão gostosa..."

            scene black with dissolve

            scene n8i99 with Dissolve(1.0)

            pause 2.0

            ro "Me chama de vadia de novo... fala... fala que você quer foder a vadia da Roxane..."

            mc "Você sabe que eu te quero, cadela."

            ro "Ah... [mc]... você... você chupa bem pra caralho..."

            mc "Você gosta? Gosta da minha boca nessa buceta? Quer que eu engula ela inteira?"

            ro "Sua boca... sua língua... porra... você..."

            mc "Quero que você goze na minha boca, bem aqui, na mesa da Zaza..."

            ro "E-eu vou! Eu vou!"

            scene n8i99 with hpunch

            ro "Aainnhnhh!"

            ro "Ah... aah... agora vem... vem me comer, vem!"

            scene black with dissolve

            scene n8i100 with Dissolve(1.0)

            pause 2.0

            mc "Roxane... você... você é..."

            ro "Sou sua vadia, [mc]... a vadia que você quer foder... a vadia que quer engolir seu gozo..."

            mc "Ah... caralho... que bucetinha gostosa..."

            ro "Você gosta? Gosta de sentir minha bucetona quente no seu pau? Quero sentir ele pulsar... quero sentir você gozar..."

            mc "Ahnn..."

            mc "Roxane... eu... eu vou..."

            ro "Goza, [mc]... goza na minha xotinha... me enche com a sua porra... me suja..."

            mc "Aaaahhh... tô quase"

            ro "Agora... eu quero agora, vaiinn! Me fode, [mc]... me fode aqui... na mesa da Zaza..."

            mc "Você é louca..."

            ro "Louca por você... por essa sua rola... quero sentir ela dentro de mim... me enchendo... me fodendo..."

            scene n8i102 with hpunch

            pause 2.0

            mc "O que tem aqui? Na mesa da Zaza?"

            ro "Quero que ela saiba que eu não sou mais a bonequinha dela... aah... que eu sou sua agora... sua putinha..."

            mc "Sua buceta... tão molhada... tão gostosa..."

            ro "Você gosta? Gosta de foder minha bucetinha, gosta? Então vem... entra em mim... me fode..."

            ro "Ah... [mc]... isso... isso... mais forte... me fode mais forte..."

            mc "Você é tão gostosa... tão apertada..."

            ro "Me xinga... me chama de puta... de vadia... de cachorra... quero ouvir você falando essas coisas enquanto me fode..."

            mc "Sua puta... sua vadia... vou te foder até você implorar pra eu parar..."

            ro "Não para... não para nunca... me fode... me fode... aaahhh..."

            mc "Caralho, Roxane! Você é demais! Eu vou gozarrrr!"

            ro "AAAAHHH! ME ENCHEEE!"

            scene n8i101 with hpunch

            pause 2.0

            mc "AAAAGHHH!"

            ro "Hmmmnnn! Tô sentindo... nas minhas costas... escorrendo..."

            mc "Porra... gozei pra caralho!"

            ro "Que delícia..."

            scene black with dissolve

            scene n8i103 with Dissolve(1.0)

            pause 2.0

    ro "Eu... eu não sei o que dizer..."

    mc "Você não precisa dizer nada, Roxane. O importante é que você tá feliz."

    ro "Eu... eu tô. Obrigada, [mc]. Obrigada por tudo."

    mc "Eu sei que não foi fácil. Mas você foi forte. Você fez a escolha certa. E agora... agora você está livre."

    ro "Livre..."

    if roxane_distrito:

        ro "Eu... eu vou sentir saudades."

        mc "Saudades?"

        ro "Da Zaza... da Blergh!... dos meus sonhos..."

        mc "Você vai realizar seus sonhos, Roxane. Você vai encontrar seu próprio caminho. E você vai brilhar. Eu sei disso."

        ro "Você acha?"

        mc "Tenho certeza. Você é forte, Roxane. Você tem a força da sua família, a força das suas raízes. E você tem... você tem eu. Eu vou tá aqui."
    else:


        ro "Eu tô livre do meu passado, do ressentimento, pra continuar indo atrás do meu sonho."

        mc "Isso aí. Às vezes nossos pais fazem coisas que não entendemos. Mas tenho certeza que eles tinham suas razões."

        mc "Não viva no passado. E olhe pro futuro. E se precisar de alguma coisa, eu tô sempre aqui."

        "Ela sorri, um sorriso genuíno, radiante. O sorriso de uma mulher livre. Livre do passado. Livre para ser quem ela realmente é."

    ro "..."

    ro "Obrigada, [mc]. Você me deu a força que eu precisava. A coragem pra recomeçar."

    mc "Você sempre teve essa força, Roxane."

    ro "Obrigada, [mc]. Você é... especial."

    "..."

    "Eu sei que a gente vai se encontrar de novo. Em algum lugar. Em algum momento."

    "Mas, por enquanto, é hora de deixar ela seguir seu caminho. E eu... eu preciso seguir o meu."

    scene black with dissolve

    scene n8i21 with Dissolve(1.0)

    "Música de Festa" "{i}tum tum tum... tum tum...{/i}"

    "... "

    "O corredor... as luzes... a música... tudo parece irreal. Eu me sinto como se fosse um sonho."

    "Eu vim aqui com o Fabrício, roubei a grana, descobri sobre a Roxane, acabei devolvendo a grana. Mano... que dia!"

    "Interpol? Russos? Em que momento minha vida ficou TÃO complicada?"

    j "Você não passa de uma vadia ingrata! Você acha que pode simplesmente abandonar o Grupo depois de tudo o que eles fizeram por você?!"

    za "Eu não estou abandonando ninguém, Cássia! Eu só estou... escolhendo meu próprio caminho!"

    mc "!"

    "As vozes... vindo do fim do corredor... Cássia e Zaza. Elas tão brigando?"

    scene black with dissolve

    scene n8i104 with Dissolve(1.0)

    pause 2.0

    j "Seu próprio caminho?! Você está louca! Eles vão te destruir! Você vai acabar na sarjeta! Sem nada!"

    za "Eu não tenho medo deles, Cássia. Eu não sou uma marionete. E eu vou fazer o que eu acho certo."

    j "Certo?! Você acha que existe 'certo' nesse mundo?! Acorda, Zaza! A única coisa que existe é poder! E quem tem o poder, faz as regras!"

    j "Foi você quem me ensinou isso!"

    za "Eles não vão ter o poder pra sempre, Cássia. A gente vai derrubar eles."

    j "Você é uma idiota! Você tá sonhando! Eles tão no comando há séculos!"

    j "Você acha que três estrangeiros e um paparazzo idiota vão mudar isso?"

    za "É a Interpol, Cássia. O Grupo chamou a atenção de gente grande."

    za "E você pode se juntar a gente. Ou pode se afundar com eles."

    menu:
        "Parece que a Zaza realmente tá do nosso lado. Será que a Cássia também pode vir com a gente?":


            pass

    j "Eu não vou abandonar o Grupo! Eu apostei demais! Eu não me joguei no inferno pra desistir agora!"

    za "É uma pena, Cássia. Mas essa é a sua escolha. E você precisa estar preparada para as consequências."

    j "Consequências?! Você está me ameaçando, Zaza?! Você acha que eu tenho medo de você?!"

    za "Não. Você não tem medo de mim. Mas você deveria ter medo deles."

    j "Eu sou a única que está sendo leal! Leal ao Grupo! Leal ao poder! Você precisa ter medo deles!"

    za "A lealdade cega te leva à ruína, Cássia. Você precisa abrir os olhos. Lá não é nosso lugar."

    za "Se você quer o poder, não é com eles que você vai ter. Eles nunca vão aceitar uma mulher como nós."

    j "Quer saber?! A verdade é que você está fraca, Zaza! Você está se iludindo!"

    j "Você acha que pode mudar o mundo? Você acha que pode derrotar o Grupo?!"

    za "Eu apostei minhas fichas naquele paparazzo. Ele tem algo que... eu nunca vi antes."

    scene black with dissolve

    scene n8i105 with Dissolve(1.0)

    pause 2.0

    j "O pombinho do [mc]?!"

    za "Ele tem algo que não existe mais no mundo."

    j "Você tá delirando."

    za "Pode ser. Não é algo racional. Eu só acredito nele. Ele me soa verdadeiro, autêntico."

    menu:
        "Eu? Eu sou um fraco que só apanha. Será que eu realmente... tenho um poder?":


            pass

    j "Você é patética..."

    j "Você realmente acha que o prefeito e os outros vão deixar você ter o poder que você quer?"

    j "Você é uma sonhadora, Zaza. E sonhadores... sonhadores sempre acabam mal."

    za "Boa sorte, Cássia. Você vai precisar."

    j "Eu não preciso da sua sorte. Eu tenho o que é preciso pra vencer. E você vai ver..."

    j "Você vai ver como eu vou acabar com a Sofia... com o velho... e tomar revista... não adianta vir chorando."

    za "..."

    menu:
        "A revista?! Eles vão dar o golpe na revista agora?!":


            pass

    "Essa briga entre Cássia e Zaza... a traição, a ameaça... a certeza de que a guerra está apenas começando."

    "A Cássia... ela vai ser um problema. E a Sofia... o chefe... a revista... eles estão em perigo. "

    "Merda."

    "A revista... A Faux News... O Grupo..."

    "A sombra deles parece estar em todos os lugares. E a revista... a revista é o próximo alvo."

    "Eu tenho que tomar uma decisão. Eu vou ajudar a Sofia e o chefe a impedir a compra? Ou vou ficar do lado da Cássia e da Faux?"

    "Se a Faux comprar a revista, a Sofia vai perder tudo. O trabalho que ela ama, a chance de mudar a revista, o legado do pai dela... Tudo."

    "E o chefe? Ele vai acabar na sarjeta, amargurado, sem nada pra fazer. A vida dele é a revista. Se tirarem ela dele..."

    "Mas... se eu ajudar a vender a revista... eu ganho um cargo melhor na Faux. Um salário maior, mais poder, mais influência..."

    "{b}E eu não vou precisar mais me preocupar com pautas{/b}, com deadlines, com o chefe... Vou poder escrever o que eu quiser. Vou poder ser... livre."

    if venda_revista >= 3:

        "Eu já dei vários toques na Sofia que eu concordo com a venda. Isso deve ajudar o Grupo."
    else:


        "Eu fui claro que não era pra Sofia vender. Disse que ia ajudar ela a impedir a venda. Ela confia em mim."

    scene black with dissolve

    scene n8i16 with Dissolve(1.0)

    pause 2.0

    "Como isso vai influenciar essa venda?"

    "Não importa. Eu tenho que escolher um lado. E eu tenho que escolher logo."

    "A batalha pela revista... ela será a próxima. E vai ser a hora de resolver minhas pendências com a Cássia."

    "Vai ser a hora de decidir... o que vai ser de mim."

    "Preciso sair daqui. Preciso respirar."

    if not roxane_distrito:

        "Hm?"

        scene black with dissolve

        scene n8i106 with Dissolve(1.0)

        pause 2.0

        n "A Zaza disse que a gente vai pra Milão! Pra semana de moda!"

        ro "A gente vai ARRASAR lá, Nathan! Vou mostrar pra aquelas modelos europeias como se desfila de verdade!"

        n "Com certeza! Você tá cada vez melhor, Roxane! A Zaza tá te treinando bem."

        ro "Ela é durona, mas sabe o que tá fazendo."

        ro "Ela me disse que eu tenho que ter mais 'presença', que eu tenho que 'dominar a passarela'..."

        n "E você tem! Você já é incrível, Roxane. Só precisa acreditar mais em você mesma."

        ro "Eu acredito! E eu vou mostrar pra todo mundo do que eu sou capaz!"

        "A felicidade deles... essa esperança... me deixa desconcertado."

        mc "..."

        "Como uma empresa tão errada... uma empresa do Grupo... pode fazer pessoas tão felizes?"

        "A Blergh! deu ao Nathan a chance de realizar seu sonho de ser modelo. Deu à Roxane uma família, um futuro."

        "E se destruir o Grupo... for a decisão errada? E se tirar os Donatello do poder... só piorar a cidade?"

        "E se... e se a gente ocasionar um cataclismo? E se tudo... for pro saco?"

        "A sombra do Grupo... ela parece estar em todos os lugares. Mas... e se a sombra... for a única coisa que mantém a cidade de pé?"

        "Eu preciso pensar. Preciso ter certeza. A decisão... a decisão é minha. E ela vai mudar tudo."

    scene black with dissolve

    play sound notificacao

    $ renpy.notify("Você conquistou um novo final")

    "{b}Você conquistou o Final 2 do Nathan! Você pode acessar o menu Personagens e apertar no botão dele para ver sua conquista!{/b}"

    "{b}Novos diálogos com o Fabrício foram desbloqueados no bar{/b}"

    $ tempo = 4

    jump call_cidade

label nathan_final3:

    mc "Nathan, você tá sendo ingênuo, cara. Você tem tudo aqui! Fama, sucesso... a chance de ser o maior modelo do país!"

    n "Mas a que custo, [mc]? Eu não quero ser um fantoche nas mãos deles! Eu quero ser livre!"

    mc "Livre?! E fugindo você acha que vai conseguir isso? O plano de roubar a Zaza... a gente sabe que no fundo é loucura."

    n "..."

    mc "O Grupo... eles podem te dar a liberdade que você procura, Nathan. Eles podem te dar o mundo!"

    n "Você... você realmente acredita nisso?"

    scene black with dissolve

    scene n8n1 with dissolve

    pause 2.0

    mc "Acredito. Você tem talento, Nathan. Você tem carisma. Você tem tudo pra chegar no topo."

    mc "E quando você tiver lá... no topo... ninguém vai poder te controlar. Você vai ser o dono do seu próprio nariz."

    n "[mc]... eu... eu não sei..."

    "Ele tá confuso. Uma luta entre o sonho de liberdade e o medo do Grupo."

    "Eu preciso empurrar ele. Garantir que o grupo tenha o que eles querem. E eu ganhar com isso também."

    menu:
        "Você não pode deixar o medo te dominar. E eu vou te ajudar.":


            pass

    mc "Nathan... me escuta. Eu sei que você tá com medo. Mas você precisa lutar pelos seus sonhos."

    n "Mas... e se eu tiver que fazer coisas erradas pra conseguir isso? E se eu tiver que... me corromper?"

    mc "Às vezes, a gente precisa fazer escolhas difíceis, Nathan. A gente precisa jogar o jogo. E a gente vai vencer."

    n "Mas... e se eu me perder no caminho? E se eu me tornar... um deles?"

    mc "E-eu..."

    "Ele tem razão. O que eu tô fazendo?!"

    "Eu vou mesmo ficar do lado do Tony, do Barão... da Sayuri... de todos os poderosos. E o que vai ser da minha consciência?"

    menu:
        "Eu não vou fraquejar agora. Eu vou chegar no topo custe o que custar.":


            mc "Olha pra mim. Eu também tinha dúvidas, mas agora eu tô certo."

            n "Tá?"

        "Eu ainda posso me redimir. Eu vou roubar a grana e fugir" if not nathan_final_desistiu:

            $ nathan_final_desistiu2 = True

            mc "Nathan! Calma!"

            mc "Espera..."

            n "Que foi?"

            mc "Eu não vou fazer o errado. E você não devia também."

            n "Quer dizer... você quer roubar a grana?! E fugir?"

            mc "Depois vemos direito essa coisa de fugir, mas qualquer coisa é melhor que aceitar esses caras."

            n "[mc]... eu concordo!"

            jump nathan_recupera_final3

    mc "Você não vai ficar igual eles. Você tem um bom coração. E eu vou estar do seu lado. Sempre."

    mc "A gente vai fazer isso juntos. A gente vai chegar no topo. E a gente vai mudar esse jogo sem se tornar mesquinhos."

    n "Eu... eu ainda não sei, [mc]..."

    mc "Nathan, você disse que queria ser livre. E é isso que eu tô te oferecendo."

    mc "A chance de ser livre de verdade. Livre pra realizar seus sonhos. Livre pra ser quem você realmente é."

    n "..."

    n "Tá legal, [mc]. Acho que vou ficar... Mas eu não vou fazer isso sozinho. Você vai estar comigo, né?"

    mc "Sempre, Nathan. Sempre."

    n "Mas... tem uma coisa que você precisa saber..."

    mc "O que foi?"

    n "Eu... eu não sou só um modelo, [mc]."

    mc "Como assim?"

    n "Eu... eu sou um agente da Interpol."

    mc "!!!"

    scene n8n3 with hpunch

    pause 2.0

    "Interpol?! O Nathan?! Mas... como?"

    n "Eu... eu fui enviado pra cá pra investigar o Grupo. Pra desmantelar essa rede de corrupção... de tráfico..."

    label nathan_f3_perguntas:

        n "Tem algo que você queira saber?"

    menu:
        "Como você veio parar aqui?":


            mc "Na Capital? Como modelo?"

            n "A Interpol... eles me recrutaram há alguns anos. Eu tava na Rússia. Eles me disseram que eu tinha o perfil que eles procuravam."

            n "Jovem, bonito, charmoso... e com um passado... complicado. Sem nada a perder."

            mc "Complicado?"

            n "Meu pai... ele foi morto pela máfia russa. A Interpol... eles me ofereceram uma chance de vingança. De lutar contra a corrupção... de fazer a diferença."

            mc "E você aceitou."

            n "Sim. Eu aceitei. Eles me treinaram, me deram uma nova identidade... e me enviaram pra cá. Pra me infiltrar na Blergh!. Pra me aproximar do Grupo."

            jump nathan_f3_perguntas
        "O que você sabe sobre o Grupo?":


            mc "Esse Grupo... quem são eles? O que eles fazem?"

            n "Eles são os donos da cidade, [mc]. Os Donatello, os Alighieri, a Cidade Chinesa, o Distrito..."

            n "Eles controlam tudo. A política, a economia, a mídia... Eles estão em todos os lugares."

            "A polícia sabe de tudo... que caralho."

            mc "E o que eles querem? Qual é o objetivo deles?"

            n "Eles querem poder, [mc]. Dinheiro, influência... Eles querem controlar tudo e todos. No fim, o plano deles é manter o status quo."

            "Faz sentido. E eu vou fazer parte disso. Eu serei parte do status quo."

            jump nathan_f3_perguntas
        "Você tá sozinho nessa?":


            n "Eu não devia responder isso, mas eu confio em você."

            mc "Pode confiar."

            n "Os loiros. Todos nós viemos da Rússia."

            mc "L-loiros? A Natasha... o Fabrício... eles também são da Interpol?"

            n "Sim. Eles são meus parceiros. A gente veio pra cá juntos. Pra cumprir a missão."

            mc "Mas... por que eles não me contaram nada?"

            n "A gente não podia arriscar, [mc]. Você não tava pronto. É provável que você nunca descobrisse."

            mc "..."

            jump nathan_f3_perguntas
        "Eu não tenho mais nada pra perguntar.":


            pass

    mc "Você disse que seu sonho era ser modelo... era tudo mentira?"

    scene black with dissolve

    scene n8n2 with dissolve

    pause 2.0

    n "Era... mas algo eu não menti. Meu verdadeiro sonho... é ser livre."

    n "Livre pra viver minha vida sem medo... sem ter que me esconder... sem ter que mentir..."

    n "Eu toparia... fugir com você. Com a grana e não olhar pra trás."

    mc "Nathan..."

    menu:
        "Você pode ser livre, Nathan. Mas precisa confiar em mim.":


            mc "Escuta, Nathan. Você pode ser livre. Livre de verdade. Mas você precisa confiar em mim."

            n "Confiar em você? Mas como?"

            mc "Você precisa continuar com a Blergh!. Você precisa se tornar o rosto da marca."

            n "Mas... e a Interpol? E a missão?"

            mc "Foda-se a missão! Você precisa pensar em você! Você precisa se proteger!"
        "Se aliar ao Grupo é o único caminho pra sua liberdade.":


            mc "Nathan, se aliar ao Grupo é o único caminho pra sua liberdade. Eles têm o dinheiro, a influência, o poder... eles podem te proteger!"

            n "Me proteger? Mas eles são os criminosos!"

            mc "E você acha que a Interpol vai te proteger deles? Você acha que eles vão se importar com você quando tudo isso acabar?"

            n "..."

            mc "Você precisa ser esperto, Nathan. Você precisa jogar o jogo. E você precisa vencer."

    n "E se... e se eu tiver que fazer coisas erradas pra conseguir isso? E se eu tiver que me aliar a pessoas como... como a Cássia?"

    mc "Às vezes a gente precisa sujar as mãos pra alcançar algo maior. Pra conquistar a nossa liberdade."

    n "..."

    n "Eu... eu não posso fazer isso, [mc]. Eu não posso abandonar a missão. A Interpol... eles estão contando comigo."

    mc "E eu estou contando com você, Nathan. Você é meu amigo. Meu..."

    if nathan_namoro:

        scene black with dissolve

        scene n8n4 with dissolve

        pause 2.0

        mc "...amor. Você não pode me deixar. Não agora. A gente tem um futuro juntos. Uma vida pra viver. E eu preciso de você aqui. Comigo."

        n "[mc]..."

        "O amor que eu sinto por ele... a dor de pensar em perder ele... nós vamos fazer algo errado, se aliar com os inimigos, mas vamos ficar juntos."

        mc "Eu sei que a missão é importante pra você. Mas a gente... a gente é mais importante."

        mc "A gente pode ser feliz juntos, Nathan. Aqui. Na Capital. A gente só precisa... de um pouco de tempo."

    elif nathan_e1 == "amizade" or nathan_e2 == "amizade" or nathan_e4_beijo or nathan_e5_beijo:

        mc "...parceiro. A gente já passou por tanta coisa juntos, cara. Aquele lance no bar... a bebida do Fabrício... as garotas... o lance da sua extradição..."

        n "[mc]..."

        "As lembranças dos momentos que a gente compartilhou... dos risos, das confidências, da amizade que a gente construiu..."

        mc "Você não pode jogar tudo isso fora, Nathan. A gente é um time. A gente se protege. E a gente vai conseguir. Juntos. Você e eu... contra o mundo. "
    else:


        mc "...conhecido. Um... sei lá... alguém que se importa com você. Você não pode simplesmente abandonar tudo e fugir."

        mc "Não depois de tudo o que você conquistou. Você tá tão perto de realizar seu sonho!"

    n "Mas... e a Roxane? A Diana? E todas as outras?"

    mc "A gente vai dar um jeito nelas, Nathan. Juntos. Mas, primeiro... você precisa ficar. Você precisa se fortalecer. Você precisa..."

    menu:
        "Você precisa se tornar um deles, Nathan. Pra poder destruir eles por dentro.":


            mc "Você precisa ganhar a confiança deles, subir na hierarquia... e quando você tiver o poder nas suas mãos..."

            mc "Aí sim, a gente vai poder fazer a diferença. Se é esse caminho que você quer seguir."
        "A Blergh! é sua melhor chance. Você vai ter tudo o que precisa e pode se unir a eles.":


            mc "A Blergh! é sua melhor chance, Nathan. Você vai ter o dinheiro, a influência, os contatos..."

            mc "Você vai ter tudo o que precisa pra ser livre. Pra proteger quem você ama. Pra fazer justiça."

            mc "Ou se aliar de vez em favor do grupo."

    n "Você... você realmente acha isso, [mc]?"

    mc "Tenho certeza. Confia em mim."

    scene black with dissolve

    scene n8n5 with dissolve

    pause 2.0

    n "Tá legal, [mc]. Você venceu. Eu fico. Eu fico com a Blergh!."

    n "Mas... promete que você vai estar do meu lado? Que você não vai... me abandonar?"

    mc "Eu nunca vou te abandonar, Nathan. A gente é um time. Lembra?"

    n "Lembro."

    "Ele sorri, um sorriso aliviado, cheio de gratidão. Eu consegui. Eu o convenci. "

    if grupo_nathan == 1 or grupo_nathan == 3:

        "O Tony... ele vai ficar satisfeito. Eu tô cumprindo minha promessa. Eu tô me mostrando um aliado valioso. Eu tô... entrando no jogo."

        "Se eu entrar pro Grupo... eu tô feito!"

        if grupo_nathan == 3:

            "Eu ainda ganhei uns pontos com a Cássia. O que será que eu ganho com ela?"

    elif grupo_nathan == 2:

        "A Cássia... ela vai me recompensar. Eu tô cumprindo minha parte do acordo. E eu vou cobrar o meu preço. Eu vou... subir na hierarquia."

        "Eu ajudei ela e ela tem que me pagar, com poder, influência... e sexo."

    mc "Bom, agora que a gente já se acertou, a gente precisa falar com a Cássia e a Zaza."

    n "Parece que sim... se agora a gente vai ser os cachorrinhos delas."

    mc "Mostrar pra elas que a Blergh! continua no caminho certo. Que você tá com elas."

    n "Sim, você tem razão. Vamos."

    scene black with Dissolve(1.0)

    pause 1.0

    scene n8n6 with Dissolve(1.0)

    pause 2.0

    mc "Zaza, Cássia. A gente precisa conversar."

    j "O que foi, pombinho? Vocês resolveram marcar o dia do casório? Que desperdício, dois gays..."

    mc "Não é hora pra isso, Cássia. É sobre o Nathan."

    za "O Nathan? O que tem ele?"

    mc "Ele decidiu ficar. Ele vai continuar com a Blergh!."

    za "E desde quando ele ia sair? Ser modelo não é seu sonho, garoto?"

    n "Sim, Zaza. Eu fico. Mas... de uma forma diferente."

    za "Hm?"

    n "Você não precisa entender."

    j "Que papo é esse? Fale, [mc]. Que que tá acontecendo?"

    mc "Eu mostrei pra ele que a Blergh! é a melhor chance dele conseguir o que quer. A liberdade que ele tanto procura. Não é, Nathan?"

    n "Sim... a liberdade..."

    mc "Na verdade, tem algo mais. Algo que vocês precisam saber. Nathan?"

    n "!!!"

    scene black with dissolve

    scene n8n7 with dissolve

    pause 2.0

    "Nathan tá perdidinho. Ele não esperava por isso."

    j "Do que você está falando, [mc]?"

    menu:
        "Nathan, é hora de provar sua lealdade. Conte a verdade.":


            n "[mc]... eu..."

            mc "Elas tão do nosso lado agora. Pode confiar nelas."

            n "..."

            "Ele respira fundo, fecha os olhos por um instante, e então..."

            n "Eu sou um agente da Interpol. Fui enviado pra cá pra investigar as atividades do Grupo."

            n "O codinome da missão é 'Cidade Dourada', e meu objetivo... é desmantelar essa organização criminosa."

            scene n8n8 with hpunch

            j "Interpol?! Aqui?! Mas como...?"

            za "Cidade Dourada... a ovelha negra do Tony... vocês..."

            n "A Interpol monitora as atividades do Grupo há anos."

            n "Eles sabiam do envolvimento do prefeito Donatello pai, do Barão, dos Alighieri..."

            n "Eles precisavam de alguém por dentro. Alguém que pudesse se infiltrar, coletar provas, desmascarar essa corja."

            j "E você... você se infiltrou na Blergh!? Usou a gente esse tempo todo?!"

            za "A Interpol... isso é... um problema."

            menu:
                "Não mais, Cássia. Agora ele tá com a gente de verdade. Não é, Nathan?":


                    pass

            n "S-sim..."

            j "Um problema?! É uma oportunidade, Zaza! O prefeito... ele precisa saber disso! Ele vai nos recompensar por essa informação!"

            za "Sim... você tem razão. O [mc]... ele..."

            j "O pombinho nos trouxe umas informação valiosa... ele mostrou o valor dele."

            za "Até que nos prestou um grande serviço."

            "Elas tão sendo sinceras. Eu me sinto poderoso. Eu manipulei o Nathan, joguei com seus medos e seus sonhos, e agora... agora eu estou no centro do jogo."

            "Eu podia ter entregado tudo. Podia ter contado sobre a Natasha e o Fabrício. Podia ter ganhado ainda mais pontos com o Grupo."

            "Mas... vamos deixar isso pra outra hora."
        "Quer saber... deixa pra lá.":


            pass

    scene black with dissolve

    scene n8n9 with dissolve

    pause 2.0

    "A Cássia, a Zaza... elas me devem uma. Elas me veem como um aliado. E eu vou usar isso a meu favor."

    "Eu vou subir. Eu vou... conquistar o meu lugar."

    n "Eu quero crescer com a Blergh!. Quero ser o rosto da marca, quero ter sucesso... quero tudo o que você me prometeu."

    mc "Ele merece, Zaza. Olha o que ele fez pela Blergh! depois daquela matéria da Cássia."

    mc "Ele trouxe visibilidade, ele atraiu investidores... ele é a chave pro seu sucesso! A Geração Z e os progressistas amam ele!"

    za "Hm..."

    "Ela observa o Nathan, seus olhos escuros e penetrantes analisando cada detalhe da sua expressão. Ela parece satisfeita."

    za "Normalmente, eu não ajudo homens. Eles precisam conquistar seu lugar no mundo sozinhos."

    za "Mas... vou abrir uma exceção. Pelos serviços prestados... por vocês dois. Espero grandes coisas de você conosco, Nathan."

    za "Seja bem-vindo ao time, Nathan. Agora de verdade."

    n "Obrigado, Zaza. Você não vai se arrepender."

    scene black with dissolve

    scene n8n10 with dissolve

    pause 2.0

    n "A gente conseguiu, [mc]! A gente tá dentro!"

    mc "Eu te falei que ia dar certo. Confia em mim."

    n "Confio. Mais do que nunca."

    n "Agora... eu vou voltar pra festa. Preciso garantir mais uns investimentos pra Blergh!. Vem comigo, [mc]?"

    za "O [mc] fica."

    mc "?"

    j "A gente precisa conversar. Em particular."

    n "Mas a gente..."

    za "Vá, Nathan. Eu cuido do [mc]."

    n "Ok... te vejo depois, [mc]."

    mc "..."

    "Ficar aqui... com elas? Sozinho? O que será que elas estão planejando? Eu me sinto... excitado. E com medo."

    menu:
        "Eu fico, Zaza. (+18)":


            mc "Eu fico."

            j "Ótima escolha, pombinho. Você não vai se arrepender."

            "Esse sorriso dela me arrepia. Ela me olha com uma promessa de... prazer e perigo."

            n "A gente se fala, cara."

            mc "Beleza. Vai lá."

            scene black with dissolve

            scene n8n11 with dissolve

            pause 2.0

            j "Você fez um excelente trabalho com o Nathan. Sabe, eu gosto de recompensar quem me serve bem."

            za "Você provou que pode ser útil, [mc]. Agora vamos ver se você é bom o bastante pra gente... em outros aspectos."

            mc "Do que vocês tão falando?"

            j "Deixa de ser sonso, [mc]. Você sabe muito bem o que a gente quer."

            za "Você tá pronto pra continuar servindo suas donas?"

            menu:
                "Eu não sirvo. Mas eu quero sentir vocês.":


                    mc "Eu não sei se... isso é certo... aqui... com vocês..."

                    j "Certo? Quem se importa com o que é certo? Você acha que a gente chegou onde chegou seguindo regras?"

                    za "Você quer poder, [mc]? Quer fazer parte do nosso mundo? Então pare de se fazer de santinho."

                    j "Se ajoelha."

                    mc "Tá..."

                    "Eu vou jogar o jogo delas... e vou poder foder essas duas. Elas parecem tão excitadas."
                "Sim... O que eu tenho que fazer?":


                    za "Se ajoelha."

                    mc "Sim... senhora Zaza."

                    "Essas duas... elas passam essa vibe de poder... me dá tanto tesão."

            scene black with dissolve

            scene n8n18 with dissolve

            pause 2.0

            za "Isso... bom garoto... Você aprende rápido..."

            j "Você gosta de ser nosso brinquedinho, não gosta? De ter duas mulheres poderosas te usando? Admite... você é um safado..."

            mc "Eu..."

            za "Você quer mais, [mc]? Quer sentir a gente? Quer provar a gente?"

            menu:
                "Sim. Eu quero.":


                    mc "Sim... eu quero... quero sentir vocês... fazer o que vocês quiserem."

                    scene black with dissolve

                    scene n8n19 with dissolve

                    pause 2.0

                    j "Quero o quê? Fala, [mc]! Quero ouvir você implorar."

                    mc "Quero... chupar vocês... lamber... quero sentir suas bucetas na minha boca..."

                    za "Bom garoto... você vai ter o que quer..."
                "Me dá logo essa buceta.":


                    j "Tá falando assim porque tá com medo da gente, pombinho? De se entregar ao prazer de ser um pedaço de carne?"

                    za "Não seja idiota, [mc]. Relaxa e aproveita. A gente vai te mostrar o que é bom."

                    mc "Eu..."

            j "Chega de conversa. Abre a boca."

            scene black with dissolve

            scene n8n20 with dissolve

            pause 2.0

            j "A Zaza adora quando lambem a bucetinha dela bem devagarinho, sabia, [mc]?"

            za "Faça o que ela tá mandando."

            mc "S-sim..."

            j "Você tem que chupar ela com vontade, mostrar pra ela como você é bom nisso."

            mc "Hmmm..."

            za "Isso... assim... mais fundo... quero sentir sua língua..."

            j "Você tá babando, [mc]! Que nojento! Você é um inútil."

            za "Até que ele sabe lamber. Você tá aproveitando a Capital, não tá, cachorrinho?"

            j "Você quer chupar minha buceta também, não quer? Admite... você tá louco pra me provar..."

            menu:
                "Sim, Cássia...":


                    mc "Sim, Cássia... quero chupar você... quero sentir sua buceta na minha boca..."

                    j "Bom garoto... vem cá..."

                    scene black with dissolve

                    scene n8n22 with dissolve

                    pause 2.0

                    za "Olha como ele fica feliz servindo. Aposto que ele tá duro igual uma pedra agora. Homens..."

                    j "Hmmm... você tem razão, Zaza. Esse filho da puta sabe chupar uma xota."

                    za "Ele nasceu pra isso."

                    j "Aah..."

                    "Lamber essas duas tá me deixando cada vez mais duro."
                "Não... eu quero a Zaza...":


                    mc "Não... a Zaza... ela..."

                    za "Eu o quê, [mc]? Fala! Quero ouvir você dizer o quanto você me deseja... o quanto você precisa da minha buceta..."

                    scene black with dissolve

                    scene n8n21 with dissolve

                    pause 2.0

                    mc "Você... você é deliciosa, Zaza... sua buceta... ela é tão quente... tão molhada..."

                    za "Ele não quer parar de me lamber. Que lindo."

                    j "Filho da puta."

                    za "Hahaha... eles sabem quem manda."

                    j "..."

            za "Chega de boca, [mc]. A gente quer sentir você de outro jeito."

            j "Mostra pra gente o seu pau... quero ver se ele é tão bom quanto sua língua."

            mc "E-eu... "

            za "Você tá tremendo, [mc]? Tá com medo?"

            mc "Não..."

            j "É que o quê? Tá duro pra gente? Tá louco pra foder a gente?"

            mc "Sim... eu... eu tô duro... quero foder vocês..."

            za "Então mostra pra gente. Tira a calça."

            scene black with dissolve

            scene n8n23 with dissolve

            pause 2.0

            za "Olha só pra isso. Não é grande, mas tá duro..."

            j "Que pauzinho... mas se ele souber usar..."

            j "Ele tá pulsando na sua mão, Zaza. Ele tá louco pra te foder."

            za "E você, [mc]? Acha que aguenta a gente?"

            mc "Eu..."

            j "Você o quê, [mc]? Vai se gabar agora? Quero ver você provar."

            za "Deita no chão."

            mc "Mas..."

            "Não tem espaço pra negociação. Eu obedeço, me deitando no chão frio do escritório."

            j "Você é um bom garoto, [mc]. Um brinquedo obediente."

            j "Vou te deixar pronto pra Zaza... pombinho."

            scene black with dissolve

            scene n8n24 with dissolve

            pause 2.0

            mc "Ah... Cássia... você..."

            j "Você gosta? Gosta da minha boca no seu pau? De sentir minha língua te lambendo... te chupando... te engolindo?"

            mc "Hmmm... sim... que delícia, safada..."

            za "Você ouviu isso, Cássia? Que patético. Os homens são todos iguais. Seres inferiores que só pensam em buceta."

            j "Deixa ele, Zaza. Ele tá perdido no prazer... na minha boca..."

            mc "Cássia... eu... eu vou..."

            j "Goza, [mc]... goza na minha boca... me deixa provar seu gozo... quero sentir você se esvaziando pra mim..."

            mc "Aaaaah..."

            j "Hmmm... gostoso..."

            za "Chega de preliminares. Sai de cima, Cássia. Agora é minha vez."

            menu:
                "E-eu ainda não me recuperei...":


                    za "Não perguntei. Se esse pau broxar você tá fodido. Vou enfiar o dedo no teu cu pra ele subir."

                    mc "E-eu..."

                    j "Aposto que ele ia adorar."
                "Vem. Senta que ele ainda tá duro pra você.":


                    za "Gosto assim."

            scene black with dissolve

            scene n8n25 with dissolve

            pause 2.0

            za "É pra isso que os homens servem, [mc]. Pra dar prazer pras mulheres. Pra serem usados. Pra serem... fodidos."

            za "E o pior é que você gosta disso, não gosta? De sentir uma mulher poderosa te dominando? De ser o brinquedinho dela?"

            mc "Zaza... eu..."

            za "Cala a boca e me fode, [mc]. Me fode com força! Me mostra o que você vale!"

            mc "Zaza... você... você é..."

            za "Eu sou o quê, [mc]? Fala!"

            menu:
                "Você é incrível, Zaza... Me fode, me fode mais forte...":


                    "Eu não consigo pensar em mais nada... só no prazer, na sensação da sua buceta me apertando..."

                    j "Tá gostando, é? Eu sei que tá."

                    mc "Sim... eu gosto... me fode, Zaza... me usa... me domina..."
                "Você fala demais Zaza.":


                    mc "Cala a boca e goza logo, vadia."

                    "Eu tô deixando ela me usar por enquanto... Mas eu vou cobrar meu preço."

                    "Elas vão me pagar por essa humilhação... com prazer..."

                    za "Seu insolente... você acha que pode falar assim comigo?"

                    mc "Eu falo o que eu quiser... puta... você não passa de uma vadia que precisa de um pau pra gozar..."

            za "Você é meu, [mc]... você me pertence... você vai me servir... sempre..."

            j "Ele tá aguentando bem, não tá, Zaza? Esse filho da puta adora ser usado pelas donas dele."

            scene black with dissolve

            scene n8n26 with dissolve

            pause 2.0

            za "Os homens... eles são todos iguais... no fundo, eles só querem servir... ser dominados..."

            menu:
                "Desafiar as duas":


                    mc "E vocês... vocês falam, falam... mas no fundo, precisam de um pau fodendo suas bucetas... não precisam?"

                    j "Seu atrevido... você acha que pode..."

                    za "Deixa ele, Cássia. Ele tá certo. A gente precisa de um pau... e a gente vai ter. Os dois."
                "Continuar sendo um garoto obediente":


                    mc "Hmmm..."

            j "Enquanto a Zaza te fode, eu vou brincar com você, [mc]..."

            za "Isso... me fode, [mc]... me fode com força..."

            j "Você gosta de ser fodido pela Zaza, não é, [mc]? De sentir ela te usando... te dominando... igual a putinha que você é?"

            mc "Zaza... você... você é..."

            za "Eu sou o quê, [mc]? Fala! Quero ouvir você implorando... me chamando de vadia... de puta... de dona..."

            menu:
                "Você é... uma deusa, Zaza... me fode... me possui...":


                    mc "Você é... uma deusa, Zaza... me fode... me possui..."

                    "Ela tá me destruindo... me usando... e eu tô adorando..."

                    j "Ele gosta de ser seu escravo, Zaza. De se humilhar pra você..."

                    za "Hmmm... eu sei... todos os homens são assim... no fundo... eles anseiam por submissão..."
                "Quer calar a boca e gozar logo?":


                    za "Seu insolente... você vai se arrepender de ter falado assim comigo..."

                    j "Olha como ele te desafia, Zaza. Ele quer te ver perder o controle... ele quer te humilhar..."

                    za "E ele vai ter o que merece."

            scene black with dissolve

            scene n8n27 with dissolve

            pause 2.0

            j "Abre a boca, [mc]... tenho uma forma melhor de você usar ela do que falar besteira. Quero que você me coma..."

            mc "Cássia..."

            j "Isso... chupa... chupa a minha buceta, [mc]... serve pra alguma coisa nessa bosta, inútil."

            za "Inútil! Você gosta de ter a Cássia na sua boca enquanto eu te fodo."

            mc "Hmmm... Cássia... Zaza..."

            j "Eu sou o quê, [mc]? Uma vadia? Uma puta? Uma delicia? Fala!"

            mc "Aahh..."

            za "Ele não aguenta mais. Ele vai gozar de novo."

            j "Goza, [mc]... goza pra Zaza... deixa ela sentir seu gozo quente..."

            scene n8n28 with hpunch

            pause 2.0

            "Eu me contraio, meu corpo tremendo. A explosão. Eu gozo. Dentro da Zaza. "

            za "Patético..."

            j "Hmmm... ele gozou dentro de você, Zaza... que desperdício..."

            za "Ele vai te foder também, Cássia. E você vai gozar pra ele. Como a puta que você é."

            j "Eu vou! Vou melar essa cara patética!"

            za "ISSO!"

            scene n8n29 with vpunch

            pause 2.0

            j "AAAAHHH!"

            za "Hnnngg..."

            j "Hmmm... isso... [mc]... você me fez gozar. Até que não é completamente inútil."

            za "Lembre-se disso, [mc]. Lembre-se de quem manda aqui. E lembre-se do prazer... da humilhação... porque você não vai ter isso em lugar nenhum."

            mc "..."

            "Como... como eu pude sentir tanto prazer? Sendo usado... humilhado... dominado..."

            "O poder delas, a submissão, o tesão... só isso importava."
        "Vou com o Nathan. A gente tem que trabalhar.":


            mc "Desculpa, Zaza, mas eu preciso ir com o Nathan. A gente tem que... trabalhar."

            za "Hm..."

            "Parece que ela tá avaliando minhas palavras, meu comportamento."

            j "Deixe ele ir, Zaza. Ele ainda não entendeu como as coisas funcionam por aqui."

            za "Faça o que quiser, [mc]."

            "Suas palavras... elas soam como uma ameaça. Ou uma promessa? Eu não sei. Mas uma coisa é certa, eu me meti em algo muito maior do que eu jamais imaginei."

            j "Só uma coisa, [mc]..."

            mc "Já te encontro, Nathan."

            n "Beleza."

    play sound som_roupas

    scene black with Dissolve(1.0)

    scene n8n12 with Dissolve(1.0)

    pause 2.0

    j "A gente ainda não terminou, pombinho."

    mc "Cássia... eu..."

    j "Você fez um bom trabalho hoje. A Zaza conseguiu o que queria. Agora... é a minha vez."

    mc "Sua vez?"

    j "A Faux News... a revista... você ainda se lembra da nossa conversa, não se lembra?"

    mc "Sim... mas a Sofia... ela não vai querer vender. Ela tá treinando pra assumir a revista no lugar do pai dela."

    j "E você acha que o velho manda alguma coisa? Ele é um dinossauro. Ele não enxerga que o mundo mudou."

    j "A mídia impressa tá morrendo. E a internet é dos grandes grupos. A Faux... a Faux é o futuro."

    mc "Mas a Sofia..."

    j "A Sofia é uma idealista. Uma sonhadora. Ela acha que pode mudar o mundo com palavras bonitas e reportagens investigativas."

    j "Ela não entende como as coisas funcionam de verdade."

    menu:
        "E como elas funcionam?":


            pass

    j "Poder, [mc]. Dinheiro. Influência. Quem tem isso, faz as regras. E a Faux... a Faux tem tudo isso. E mais um pouco."

    mc "..."

    j "Se a Faux comprar a revista, a gente vai controlar o último veículo de mídia que com relevância nesse país que ainda falta."

    j "Vamos controlar a narrativa. Apenas matérias boas sobre Basílio e sua família, investigação só contra os inimigos."

    j "A gente vai ter o poder completo. E você... você vai estar do nosso lado."

    mc "Eu...?"

    scene black with dissolve

    scene n8n13 with dissolve

    pause 2.0

    j "Sim, você. Eu vou te dar um cargo de editor. Você vai poder escrever o que quiser, investigar quem você quiser..."

    j "Você vai ter poder, [mc]. Poder de verdade. Um poder que nunca a pombinha ou o velho te darão."

    "Editor... sem deadlines... sem ter que me preocupar com as vontades do chefe... sem ter que caçar pautas... sem ter que..."

    mc "!!!"

    menu:
        "E as pautas? Eu não vou precisar mais entregar pautas?":


            j "Pautas? Pra quê? Você vai ser um editor, pombinho. Você vai estar no comando."

            j "Você vai decidir o que entra e o que não entra na revista."

            j "Nada nem ninguém vai te tirar desse emprego. Você vai poder fazer o que bem entender."

            mc "Não acredito... sem pautas..."
        "A Sofia... o que vai acontecer com ela?":


            j "A princesinha? Ela vai ter que aprender a se virar. O mundo real não é um conto de fadas."

            j "Ela vai ter que encarar as consequências das suas escolhas. Assim como você."

            mc "Ou seja... ela vai se ferrar."

            j "..."

    "O poder... a influência... a liberdade... a oferta da Cássia é tentadora demais. Eu não posso..."

    menu:
        "Só uma coisa...":


            pass

    mc "Você viu como o prefeito falou com a Zaza hoje? Você ainda acha que vocês terão um lugar na mesa?"

    j "O Donatello? Ele vai ter que nos engolir, pombinho. Nós vamos forçar ele a nos aceitar."

    mc "Mas..."

    j "O Grupo me preparou pra esse momento, [mc]. Foram anos."

    j "A Zaza... o Luca... eles me treinaram pra isso. Pra dar o golpe. Pra conseguir a revista."

    j "Pode ter certeza, pombinho... eu vou ter o meu lugar. E você... você vai ter a sua recompensa."

    mc "Luca... você disse Luca? Luca Alighieri?"

    j "Sim. Ele é o nosso..."

    mc "O mesmo sobrenome da pizzaria... Tony Alighieri... eles têm o mesmo sobrenome..."

    j "Você é mais esperto do que eu pensei, pombinho. Tá começando a entender como as coisas funcionam."

    menu:
        "Agarrar a bunda dela":


            scene black with dissolve

            scene n8n14 with dissolve

            pause 2.0

            mc "Tô, né?"

            j "Hmhmm..."
        "Não vou fazer isso. Vou focar na conversa":


            pass

    mc "O Tony... ele é parente do Luca."

    j "Ele se casou com uma Alighieri. A falecida filha do Luca. Foi assim que ele entrou no jogo. Mas ele não é um dos nossos."

    j "Ele não é italiano. Nem o nome dele é italiano. Ele gosta de usar 'Tony' pra disfarçar."

    mc "Mas ele..."

    j "...ele não passa de um Zé Ninguém que deu sorte. Um capacho que limpa as sujeiras do Grupo."

    j "O Luca... ele é o verdadeiro poder. O patriarca da família Alighieri. Ele pode te dar tudo o que você quiser, [mc]. Tudo."

    mc "E o Tony?"

    j "O Tony? Ele não é nada perto do Luca. Ele é só... o lixeiro. Entendeu?"

    menu:
        "Sim...":


            pass

    menu:
        "Pode contar comigo. A revista será sua e do Grupo.":


            mc "Pode contar comigo, Cássia. Eu vou fazer o que for preciso pra garantir que o poder continue... onde ele deve estar."

            mc "Eu vou tirar a Sofia da jogada."
        "Vou fazer o possível com a Sofia... mas não garanto nada.":


            pass

    j "Quero ver você provar sua utilidade, pombinho. Palavras... são apenas palavras."

    mc "..."

    j "Agora vai... nossa batalha tá prestes a começar."

    scene black with Dissolve(1.0)

    scene n8i16 with Dissolve(1.0)

    pause 2.0

    "A música da festa continua, o som da euforia e da decadência. Eu caminho pela multidão, observando os rostos embriagados, os corpos suados, os olhares vazios."

    "Eu não pertenço a este mundo. Mas eu vou dominar todos eles."

    "O Nathan... A Blergh!, o Grupo... eles vão dar a ele tudo o que ele sempre quis."

    "Mas será que ele vai ser feliz? Será que ele vai conseguir... se encontrar?"

    "E a Sofia... ela vai lutar. Ela vai lutar pela revista, pelo legado do pai dela... pelos seus ideais."

    "Mas ela vai perder. Ela não tem chance contra o Grupo. Contra mim."

    "Eu... eu escolhi meu lado. E eu não vou voltar atrás. Eu vou subir. Eu vou chegar ao topo. Custe o que custar."

    mc "Agora deixa eu sair daq-"

    scene n8i17 with hpunch

    na "Onde você pensa que vai?"

    mc "Natasha..."

    na "O Nathan me contou sobre a sua decisão... sobre o seu... acordo com a Cássia e a Zaza."

    mc "Você... você também é, não é?"

    na "Sim, [mc]. Eu sou."

    mc "É... eu devia ter descoberto. Vocês são a ovelha negra."

    na "Mas eu não vou julgar você. Nem o Nathan. Vocês dois... vieram de uma situação difícil... querer uma vida boa... ao lado do Grupo..."

    na "É uma escolha que eu entendo... e até que eu já pensei em tomar também."

    "Ela sabe o que eu tô sentindo, o que eu quero. Ela já sentiu isso também."

    na "Só... preciso que vocês tenham certeza do que estão fazendo, [mc]. Isso... isso não é brincadeira."

    mc "Você também... você também está pensando em... abandonar a missão? Se juntar ao Donatello de vez?"

    na "..."

    na "Eu não posso revelar a minha vida assim, [mc]. Mas... dependendo do lado que você escolher... a gente vai ser... amigo. Ou inimigo."

    mc "..."

    menu:
        "Amiga ou inimiga... você continua sendo a mulher mais linda que eu já vi.":


            na "Você é um homem ousado, [mc]."

            mc "E você é uma mulher... perigosa. E eu... eu adoro isso em você."

            scene black with dissolve

            scene n8i18 with dissolve

            pause 2.0

            na "Hmmm... perigosa, é? Você acha que eu seria capaz de... machucar você, [mc]?"

            mc "Eu... eu não sei, Natasha. Mas eu quero descobrir."

            na "Então... escolha seu lado, [mc]."
        "Eu não quero ser seu inimigo, Natasha.":


            mc "Eu não quero ser seu inimigo, Natasha."

            "Ela me encara, seus olhos verdes me fitando com uma tristeza profunda. Ela respira fundo, e então..."

            na "Eu também não, [mc]. Mas... às vezes a gente não tem escolha."

            mc "..."

    na "Hmmm... isso... [mc]... você é bom... muito bom..."

    mc "Você também, Natasha... você é..."

    na "Eu sou o quê? Fala... quero ouvir..."

    mc "Você é... incrível... perfeita..."

    na "Perfeita, é? Você acha mesmo que eu sou perfeita, [mc]?"

    mc "Acho... você é a mulher mais viciante que eu já conheci..."

    na "Você é um mentiroso, [mc]. Mas eu gosto disso em você."

    na "A gente se encontra de novo. Do mesmo lado. Ou do lado oposto. Mas a gente se encontra."

    menu:
        "Vou tá te esperando.":


            pass

    "Essa mulher... de que lado ela tá? Agente da Interpol ou cadelinha do prefeito?"

    mc "Agora eu saio da-"

    n "[mc]!"

    scene black with dissolve

    scene n8n16 with Dissolve(1.0)

    mc "Nathan."

    n "[mc]! Ainda aqui?"

    mc "Que bom que eu te achei. Eu preciso falar com você antes de eu ir."

    n "Claro. O que foi?"

    mc "Eu..."

    n "Você não precisa se explicar, [mc]. Eu sei o que você fez. E eu agradeço."

    mc "Agradece?"

    n "Sim. Você me mostrou... que eu podia escolher meu próprio caminho. Que eu não precisava ser... o que os outros esperavam de mim."

    mc "..."

    n "Eu sempre quis ser livre, [mc]. Achei que como agente eu ia encontrar isso. Mas, no fim, não era esse o caminho."

    n "Ser um cachorrinho da Zaza e da Cássia ou da Polícia Internacional? Qual a diferença?"

    n "Você me deu coragem, [mc]. E eu apostei que com o Grupo eu vou ser livre."

    n "Eu vou lutar pela minha vida. Pela minha felicidade. E eu não vou esquecer disso."

    if nathan_namoro:

        scene black with dissolve

        scene n8n17 with dissolve

        pause 2.0

        mc "Eu te amo, Nathan. As coisas tão turbulentas e a gente não vai se ver muito."

        mc "Mas no fim... a gente vai poder ficar juntos."

        n "Eu também te amo, [mc]. A gente vai. Eu vou tá esperando esse dia."

    elif nathan_e1 == "amizade" or nathan_e2 == "amizade" or nathan_e4_beijo or nathan_e5_beijo:

        scene black with dissolve

        scene n8i88 with dissolve

        pause 2.0

        mc "A gente é parceiro, Nathan. Parceiro até o fim."

        n "Até o fim, [mc]."

    mc "Eu tô bastante confiante no nosso futuro agora. Por um momento, eu não imaginava que você... que você fosse capaz de..."

    n "De me juntar ao Grupo? De trair a Interpol? De virar a casaca?"

    mc "..."

    n "Nem eu, [mc]. Nem eu. Mas... às vezes a vida nos leva por caminhos que a gente nunca imaginou."

    n "E a gente precisa... se adaptar. Sobreviver. Foi o que você me ensinou."

    n "Você se ferrou muito nesta cidade também. Mas você luta. Você sempre se levanta. E isso é uma inspiração pra todo mundo que tá no seu lado."

    n "É fácil lutar quando se é poderoso, forte, rico. Mas lutar quando o mundo todo tá contra a gente. Isso sim é incrível."

    mc "Poxa... valeu, cara. Então... você tá feliz, Nathan?"

    n "Eu... eu acho que sim, [mc]. Eu tô lutando pela minha vida. Pela minha liberdade. E isso... isso me faz feliz."

    mc "Eu fico feliz por você."

    n "A gente se vê por aí, [mc]. Se cuida. Essa galera não é brincadeira."

    n "Se esse é o caminho que você escolheu, então siga até o fim. Não mude, não jogue pros dois lados. Vá com ele do começo ao fim."

    mc "Pode deixar."

    n "Muita força pra tu, cara."

    mc "Você também, Nathan."

    scene black with Dissolve(3.0)

    scene capital_final with Dissolve(3.0)

    "A cidade... as luzes... o barulho... tudo parece diferente agora."

    "Eu fiz minha escolha. Eu me juntei ao Grupo. E agora... agora eu preciso jogar o jogo."

    "O que vai acontecer com a Sofia? Com o chefe? Com a revista?"

    "E a Natasha... a gente vai se encontrar de novo? De que lado ela vai estar?"

    "A Cássia... ela me prometeu poder, influência... ela vai cumprir sua promessa?"

    "E eu... eu vou conseguir o que eu quero? Ou eu vou me perder... nesse mar de sombras e mentiras?"

    "O embate na revista. É ali que tudo vai ser decidido."

    play sound notificacao

    scene black with dissolve

    $ renpy.notify("Você conquistou um novo final")

    $ persistent.nathan_final3 = True

    $ nathan_final = 3

    $ nathan_final3 = True

    "{b}Você conquistou o Final 3 do Nathan! Você pode acessar o menu Personagens e apertar no botão dele para ver sua conquista!{/b}"

    p rindo "Este é apenas um dos possíveis finais da sua história com o Nathan! Volte e faça escolhas diferentes para descobrir novos caminhos e desvendar todos os segredos!"

    jump call_cidade

label final_bloqueado:

    p rindo "Este caminho ainda não está disponível nesta atualização."

    p "Para caprichar bastante em cada final, o RB preferiu se dedicar totalmente a um caminho antes de fazer os outros."

    p "Mês que vem você poderá escolher esta opção e ver como a história continua por aqui!"

    p lecionando "Veja todos os finais para juntar os pedaços do mistério e descobrir todos os caminhos!"

    p "Inclusive, você pode ver quais finais você já conseguiu no menu, apertando na foto do personagem!"

    return

label ajuda_itchio:

    show black with dissolve

    p rindo "Aliás, sabia que CH agora está saindo em inglês para todo o mundo?! Chegamos longe, hein?"

    p "O RB disse que nada disso seria possível sem vocês, apesar que eu tenho certeza que você não está nem aí para ele. Você só quer saber de comer essas delícias."

    p "Mesmo assim, você pode ajudar CH ter sucesso globalmente dando uma avaliação 5 estrelas pra ele na loja internacional."

    p "E como eu sei que ninguém é legal, eu sugeri que ele desse créditos para quem pudesse fazer isso. Então, além de ajudar CH a fazer sucesso, tu ganha grana!"

    p "Se você puder dar uma olhadinha e deixar suas 5 estrelas, está tudo muito bem explicado em uma postagem que ele fez."

    menu:
        "Com certeza, bebê. Me passa isso aí.":


            p "Você é o melhor, amor. Vou abrir o site agora. Não assuste."

            $ renpy.run(OpenURL('https://apoia.se/geiko/contents/view/De-5-Estrelas-pro-jogo-da-Pri-ajude-a-Geiko-na-gringa-e-ganhe-creditos-BrR1lObCy'))
        "Outra hora":


            p "Tudo o que você quiser, vida."

    p "Nos vemos na próxima atualização. Quando será que ele continua Fadolândia, hein? Que saco!"

    hide black with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
