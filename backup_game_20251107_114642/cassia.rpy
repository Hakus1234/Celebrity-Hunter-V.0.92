

label cassia_cel_msg1_resposta:

    "..."



    label trabalho_cassia:

        if cassia_evento1:

            jump cassia_evento1
        else:


            if nathan_e1 != "nada" and not cassia_nathan1:

                "Agora que eu falei com o [n], tenho que acertar as coisas com a [j]."

                jump cassia_nathan1

            mc zerado "Não tenho nada pra falar com ela agora...."

            if cassia_aceitou and not cassia_nathan1:

                mc angustiado "Preciso conseguir alguma coisa sobre o tal do [nc] antes de falar com ela."

            jump cenario_trabalho



    label cassia_evento1:

        $ cassia_evento1 = False

        $ tempo += 1

        "..."

        "Eu tenho quase certeza que vou encontrar aquela mulher da máquina fotográfica aqui."

        "Ela trabalha na mesma revista."

        "Na verdade, ela é uma das principais paparazzo da revista. Eu não conheço ela direito obviamente..."

        mc zerado "Ninguém fala comigo aqui..."

        "Mas ela já tem muitos anos trabalhando aqui. Conseguiu furos incríveis. Agora ela só trabalha quando quer e as pautas dela sempre viram grandes matérias."

        mc desconfiado "Será que ela está atrás da [c]?"



        "A redação não é grande. A sala dela é a última antes da cozinha."

        "Estou com um péssimo pressentimento sobre isso tudo..."

        $ jc = "Cássia Roitman"

        "Se eu não me engano, o nome dela é [jc]..."





        scene trabalho cassia with Dissolve(2.0)

        pause

        mc surpreso "!"

        "E-ela está olhando diretamente pra mim."



        "Olha essa roupa! Eu consigo ver tudo..."

        j "..."

        "Tem tanta coisa na minha cabeça agora. Não sei nem por onde começar..."

        "Não posso ficar parado igual um idiota sem falar nada! Fale alguma coisa, [mc]!"

        mc concentrando "..."

        menu:
            "Olá.":


                mc envergonhado "O-oi..."

                j "Oi, bebê."
            "Você sabia que dá pra ver seu sutiã com essa blusa?":


                mc tarado "Você sabia que dá pra ver seu sutiã com essa blusa?"

                j "Sério?"

                j "E qual nota você dá pro que tá vendo?"

                mc envergonhado "..."

        mc desculpa "Seu nome é... Cássia Roitman, não é?"

        j "Isso mesmo. E não precisa ter tanto medo. Eu não mordo."

        j "A não ser que você peça com jeitinho..."

        mc surpreso "..."

        j "O que foi? Todo o sangue foi pra cabeça que não pensa?"

        mc envergonhado "Eu... só queria..."

        j "Eu sei o que você quer."

        scene trabalho sala_cassia with Dissolve(1.0)



        mc envergonhado "Sa-sabe?"

        j "Obviamente."

        scene cassia sentada_foto with Dissolve(1.0)

        j "Você quer saber o que eu estava fazendo na praça apontando isso pra você e pra sua bonequinha."

        "Bonequinha?"

        mc desculpa "Isso."

        j "Eu estava fazendo meu trabalho."

        mc desconfiado "Você tá atrás da [c]?"

        j "Não, bebê. Não estou."

        j "Mas quando tem uma celebridade literalmente na sua porta você não pode deixar passar."

        j "{b}Vocês{/b} vão virar matéria logo logo."

        mc surpreso "Você{b}s{/b}!?"



        scene cassia sentada_rindo with Dissolve(1.0)

        j "Obviamente."

        j "Você é parte fundamental."

        mc desconfiado "Eu?"

        j "Sim. O título será: {i}Princesa das baixinhas vira mulher nas mãos de paparazzo{/i}."

        mc surpreso "Que?!"

        j "É a reportagem perfeita."

        j "As pessoas adoram falar mal dos famosos. Ficam esperando que eles façam qualquer coisa no mínimo questionável para que possam cair em cima."

        j "E o que seria melhor do que a pura [c] dando para um zé ninguém de um paparazzo?"

        mc bravo "Que?"

        j "Amor é que não é, concorda?"

        j "Já consigo imaginar as mães: 'esse rapaz deve ter um negócio bem grande pra ela querer transar com ele'."

        mc bravo "..."

        j "Talvez eu acabe até te ajudando..."

        menu:
            "Mas... mas isso não é verdade!":


                mc angustiado "Mas nada disso é verdade! Não fizemos nada!"

                mc angustiado "Você nos viu na praça! Não demos nenhum beijo sequer!"
            "Mentirosa! Como você poderia saber isso?!":


                mc irritado "É óbvio que você está inventando isso!"

                mc irritado "..."

        j "Calma, bebê. Não precisa gritar."





        scene cassia sentada_explicando with Dissolve(1.0)

        j "Para as pessoas e para a revista, não importa se algo aconteceu ou não."

        j "Qualquer foto de vocês um do lado do outro..."

        if priscila_e2 == "seducao":

            j "E eu tenho uma foto sua prensando ela na grade da praça..."

        elif priscila_e2 == "amizade":

            j "E eu consegui pegar vocês bem na hora que ela te abraçou..."
        else:


            j "E vocês estavam rindo juntos bem animadinhos..."

        j "Isso é o suficiente para gerar uma dúvida razoável."

        j "E o boato muitas vezes tem mais força do que a verdade, sabia?"

        j "O que as pessoas discutem mais? Sobre o crime comprovado ou sobre se fulano devia ser preso ou não?"

        j "O povo quer algo simples pra eles ficarem remoendo com os amigos, pois pensar na própria vida é trabalhoso demais."

        j "Pense que vocês estarão ajudando as pessoas."

        menu:
            "Isso é completamente antiético!":


                mc bravo "Isso é um absurdo!"

                mc "Você está admitindo que vai mentir para todos os leitores!"

                j "Você só sabe falar gritando?"

                j "Ética é uma palavra bonita que inventaram pra colocar os idiotas dentro de um cercadinho."

                j "Eu faço o que eu preciso pra conquistar o que eu quero."
            "Você acha que ela vai deixar isso barato? Ela vai vir atrás de você.":


                mc triste "Mas com certeza isso não vai acabar bem pra você e também pra revista."

                mc "Ela tem recursos. É óbvio que ela vai acionar advogados e vir atrás da gente."

                j "Você realmente acha isso?"

                mc angustiado "Claro!"

                j "Não é bem assim que acontece, bebê."

                j "Você acha que compensa para os famosos cutucar a ferida?"

                j "NÓS temos a opinião pública do nosso lado. Se eu escrever que a [c] veio nos processar por uma matéria, só vai aumentar o problema."

                j "Pra ela não compensa dar mais ibope pra situação. Pode ter certeza."
            "Bom... Eu sou um paparazzo também, então acho que entendo.":


                mc concentrando "Eu sou um paparazzo também, então acho que entendo."

                mc "Eu não concordo, mas faz sentido o que você diz."

                j "Fico feliz que pense dessa forma. Quanto mais cedo você entender isso, maiores suas chances de se dar bem aqui."



        scene cassia sentada_rindo with Dissolve(1.0)

        j "Não é nada pessoal, querido."

        j "Você só estava no lugar errado, na hora errada."

        mc bravo "..."

        "Tenho certeza que essa matéria vai acabar com minha relação com a [c]."

        "Ela vai se afastar de mim para negar os boatos. Tudo o que eu conquistei com ela até agora vai por água abaixo graças a essa vaca..."

        "E o pior é que eu não posso fazer nada contra ela..."

        "Se eu quiser continuar vendo a [c] preciso fazer alguma coisa!"

        mc bravo "..."

        j "Se me permite, tenho uma matéria pra escrever..."

        mc bravo "Espere!"

        j "Hm?"

        mc bravo "Tem algo que eu possa fazer pra que você desista de publicar a matéria?"



        scene cassia sentada_explicando with Dissolve(1.0)

        j "Será que tem?"

        j "..."

        mc bravo "..."

        j "O quanto você quer continuar esse romancezinho com a bonequinha?"

        mc bravo "Não importa. Diga o que você quer e podemos negociar."

        j "..."

        j "Olha, na verdade... Tem algo que TALVEZ você possa me ajudar. E daí QUEM SABE eu desista da [c]."

        mc bravo "..."

        j "Eu estou há alguns meses trabalhando em um especial sobre um novo modelo. É uma delícia de rapaz."

        j "Estou pronta para finalizar. Provavelmente será um dos meus trabalhos mais famosos."

        j "O problema é que preciso de algum podre dele para finalizar minha matéria. E o desgraçado não se abre comigo."

        j "Eu já tentei de tudo. Até mesmo dar pra ele eu já tentei diversas vezes."

        j "Mas nem isso ele aceita. Ele recusa todas minhas investidas. É a primeira vez que isso acontece comigo."



        scene cassia sentada_rindo with Dissolve(1.0)

        j "SE você conseguir algum podre sobre ele que eu ainda não tenha, eu deixo você e a bonequinha de lado."

        j "Você aceita?"

        mc bravo "..."

        "Se eu não aceitar, é praticamente certeza que a [c] vai deixar de falar comigo por um bom tempo, no mínimo."

        "Talvez ela nunca mais possa se aproximar de mim."

        "Se eu aceitar eu ainda vou poder me aproximar desse modelo e quem sabe conseguir mais pautas."

        "E talvez ganhar alguns pontos com a [j] não seja o pior negócio. Ela tem bastante influência na revista."

        "Mas, mesmo com todos esses pontos positivos, não sei se quero ajudar essa desgraçada."

        "Essa é uma decisão muito importante e preciso pensar com muito cuidado, pois vai influenciar muito o meu futuro."

        j "E então, bebê? Aceita ou não?"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v2_fim","inicio","local")

        menu:
            "Sim. Me fale mais sobre o modelo.":


                jump cassia_aceitou
            "Não. Não quero me envolver com você.":


                mc bravo "Não! Não quero me envolver em nada que tenha você no meio."



                scene cassia sentada_irritada with Dissolve(1.0)

                j "Você sabe que esse é o fim da sua paquera com ela, certo?!"

                j "E que eu posso transformar sua vida em um inferno aqui dentro, não sabe?!"

                j "Você realmente vai me desafiar?!"

                show black with dissolve

                p lecionando "Recusar a proposta da [j] vai impedir que você veja os próximos eventos dela."

                p "Você também poderá ficar sem encontrar outros personagens que estão ligados à história dela."

                p "Eu sei que a mulher é o capeta, mas se esta é sua primeira vez jogando, não recomendo deixar esta oportunidade passar."

                hide black with dissolve

                p rindo "Mas, como sempre, é você quem escolhe."

                menu:
                    "Foda-se você e suas ameaças. Adeus!":


                        $ cassia_aceitou = False
                        $ cassia_evento = False

                        mc irritado "Foda-se você e suas ameaças. Adeus!"

                        j "Você não passa de um coitado, seu merda!"

                        j "Acha que pode falar..."

                        "..."

                        scene trabalho mesa with dissolve

                        "Deixei ela falando sozinha."

                        "Todos os outros olharam ela gritando igual uma louca."

                        "Acho que é a primeira vez que contrariam ela. Mulher mimada, isso sim."

                        jump cassia_nao_aceitou
                    "Pensando bem, eu vou aceitar sua proposta.":


                        mc desculpa "Pensando bem..."

                        jump cassia_aceitou

        label cassia_aceitou:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassia_proposta_aceitou","resultado","evento")

            $ cassia_aceitou = True

            mc bravo "Eu vou aceitar sua proposta."

            scene cassia sentada_rindo with Dissolve(1.0)



            mc "Mas quero que você saiba que é apenas porque não quero que você publique a matéria."

            j "Eu entendo. Cada um tem seus motivos."

            j "E não precisa mais fazer essa cara. Agora estamos do mesmo lado."

            mc concentrando "..."

            "Ela tem razão. Se eu for entrar nessa, preciso dar o meu melhor."

            mc normal "Ok. Espero que eu não me arrependa."

            j "Os amigos de [jc] têm apenas coisas boas reservadas para eles no futuro."




            "É o que eu espero..."

            scene cassia sentada_foto with Dissolve(1.0)

            j "Bom, o que você precisa saber para o trabalho é que o nome dele é [nc]."

            j "Ele nasceu fora, mas está no país desde os cinco anos, então é como se fosse daqui."

            j "A fama dele ainda não chegou no ápice. Ele está começando como modelo, mas ele tem grande potencial."

            j "Eu consigo ver ele dominando as passarelas e outdoors internacionais muito em breve."

            mc desculpa "Mas se nem você conseguiu, por que eu conseguiria algo dele?"

            j "Eu sei, bebê. É um tiro no escuro."

            j "Mas eu confio no meu instinto. E ele está me dizendo que você pode conseguir ir longe com o [n] se você se esforçar."

            j "Você conseguiu conquistar uma das celebridades mais reservadas da atualidade."

            j "Confie mais no seu taco."

            mc normal "Ok. Obrigado."

            j "Agradeça trazendo algo sobre o [n]."

            j "E dependendo do seu desempenho, quem sabe eu não deixe você aproveitar outras coisas que eu posso te dar."

            menu:
                "Estou ansioso para aproveitar tudo.":


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("cassia_seducao_aceitou","sim","aceitou")

                    $ cassia_seducao = True

                    mc tarado "Estou ansioso para aproveitar tudo o que você quiser me dar."



                    j "A é? Olha aqui."

                    scene cassia sentada_provocando with Dissolve(1.0)

                    pause

                    j "Assim que se fala, bebê."

                    mc surpreso "!"

                    j "Um homem que sabe aproveitar as oportunidades deixa qualquer mulher molhada."

                    j "Eu tenho certeza que eu posso fazer você se sentir muito bem."

                    j "Mas primeiro você precisa conquistar esse direito."

                    j "E pode ter certeza que vai ser bem diferente do seu lenga-lenga com a bonequinha."

                    j "Fico te esperando."

                    mc envergonhado "O-ok..."

                    "..."
                "De jeito nenhum. Isso aqui é apenas profissional.":


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("cassia_seducao_negou","nao","aceitou")

                    $ cassia_seducao = False

                    j "Tudo bem. Mas você não sabe o que está perdendo."

                    mc serio "..."












            scene trabalho mesa with Dissolve(1.0)

            "Essa mulher com certeza sabe o que quer."

            "Eu estou tremendo de falar com ela."

            label cassia_nao_aceitou:

                if cassia_aceitou:

                    "Eu decidi que vou conseguir algo sobre o tal do [nc], então agora não posso voltar atrás."

                    if cassia_seducao:

                        "Eu também aceitei o convite dela para uma relação fora dos limites profissionais."

                        "Será que eu fiz certo? Tenho que tomar cuidado com essa mulher."
                    else:


                        "Eu deixei claro que nossa relação é apenas profissional."

                        "Quero o mínimo de contato possível com ela."
                else:


                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("cassia_proposta_negou","nao","aceitou")

                    "Eu decidi não aceitar a proposta dela. Então tenho que estar preparado para as consequências."

                    "Preciso falar com a [c] o mais rápido possível pra que ela saiba o que está por vir."

                    "Tomara que ela não queira se distanciar de mim. Mas provavelmente é isso que vai acontecer."

                    "Também preciso ver se a [j] vai prejudicar minha vida no trabalho de alguma forma."

                    "Eu comprei briga com peixe grande. Tenho que estar pronto pro futuro."

        $ v2_fim = True

        $ dia_cassia = dia + 1

        call priscila_out_1

        "..."

        jump call_cidade

label cassia_nathan1:

    $ cassia_nathan1 = True

    scene trabalho sala_cassia with Dissolve(2.0)





    mc serio "Oi, [j]."

    if n1_ajuda and not nathan_p1:



        scene cassia sentada_irritada with vpunch

        j "Oi?! {size=30}OI?!{/size}"

        mc triste "..."

        j "Você deu informações sobre o [n] diretamente pro idiota! Você passou por cima de mim!"

        mc desculpa "Eu..."

        label cassia_acordo_nao:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("cassia_acordo_fracasso","inicio","local")

            $ cassia_aceitou = False

            j "Sua parte era me trazer algo que eu pudesse usar sobre ele!"

            mc desculpa "Mas eu ainda posso..."

            j "Agora é tarde demais, idiota!"

            j "Você tá fudido comigo, moleque! Pode dizer adeus ao seu romancezinho com a bonequinha!"

            "Meu Deus... Ela tá possessa!"

            mc envergonhado "Calma, [j]... Eu..."

            j "Calma o caralho!"

            j "Acho bom você avisar a bonequinha, antes que ela saiba tudo diretamente pela revista!"

            j "Agora SAI FORA!"



            scene trabalho geral with vpunch

            mc angustiado "Ai!"

            "..."

            "Eu não fiz minha parte do nosso acordo..."

            "Eu tinha que ter dado as informações sobre o contrato pra ela..."

            if nathan_atencao > 0:

                "Mas eu mesmo dei a informação para o chefe."

                "Ganhei pontos com ele, ganhei mais dias para conseguir outras pautas..."

                "Mas será que valeu a pena?"
            else:


                "Agora que nosso acordo foi quebrado, posso fazer o que quiser com a informação."

                "Posso entregar para o chefe quando ele for me despedir."

                "Ou posso só segurar a informação e não deixar a revista publicar."

            "O problema é que agora a [j] vai publicar a reportagem sobre eu e a [c]. Provavelmente ela não vai poder mais falar comigo."

            mc triste "Tenho que ver como lidar com isso."

            "Melhor começar avisando a [c]..."

            jump call_cidade

    elif n1_ajuda and nathan_p1:

        show trabalho cassia with dissolve

        j "Oi, pombinho. Tem alguma coisa pra mim?"

        mc serio "Eu..."

        j "Você não está esquecendo sua parte no nosso acordo, né?"

        j "Se você não tiver algo que eu possa usar sobre o [n], pode dizer adeus a sua relação com a bonequinha."

        "Ela tem razão. Não posso colocar tudo a perder com a [c] agora que estamos indo tão bem."

        if priscila_seducao_evento > 0:

            "Eu tô no caminho certo para seduzir ela. Sinto que vou poder avançar logo logo."

        elif priscila_amizade_evento > 0:

            "A gente tá aumentando nossa amizade a cada encontro. Não posso jogar tudo isso no lixo."

        "Mas por outro lado eu tenho medo do que pode acontecer com o [n]."

        "E agora o que eu faço?"

        j "E então?"

        mc triste "..."

        menu:
            "Entregar as informações sobre o [n] para a [j]":


                jump cassia_acordo_sim
            "Mentir e dizer que você não tem nada":


                mc desculpa "Por favor, me desculpe, mas não consegui nada sobre o [n]..."

                show cassia sentada_irritada with hpunch

                j "Quê?!"

                j "Você tem certeza que você vai seguir por esse caminho, pombinho?"

                j "Se você não me passar essas informações, eu vou publicar a matéria sobre você e a [cc]."

                j "Você tá entendendo isso?!"

                mc triste "..."

                menu:
                    "Não estou mentindo. Não tenho nada pra você.":


                        mc serio "Não estou brincando. Não tenho nada para você."

                        jump cassia_acordo_nao
                    "Ok. Você venceu! Tenho informações sobre o primeiro contrato dele.":


                        jump cassia_acordo_sim

    elif not n1_ajuda:

        $ cassia_nathan_naoajudou = True

        scene cassia sentada_explicando with dissolve

        j "Oi, pombinho."

        mc desculpa "Não consegui nada sobre o [n]..."

        mc serio "Você vai mesmo publicar a matéria? Pense bem! Você nã..."

        j "Calma, bebê."

        j "Eu não vou publicar sua matéria com a bonequinha."

        mc surpreso "Sério?!"

        j "..."

        mc serio "Mas..."

        j "O [n] me ligou ontem de madrugada. Ele tava meio alterado o menino."

        j "Ele disse que conversou com você e você deu coragem para ele fazer o que tinha que fazer."

        j "Não lembro as exatas palavras dele, mas foi essa a ideia."

        scene cassia sentada_rindo with dissolve

        j "O que importa é que de uma forma ou de outra você conseguiu a informação que eu precisava."

        j "Ele vai assinar um contrato com a Blergh! e com isso posso finalizar minha matéria."

        mc serio "..."

        mc "Você vai fazer isso se voltar contra ele?"

        j "Não interessa, pombinho."

        j "Você e a bonequinha estão livres para continuar esse romancezinho de vocês."

        if cassia_seducao:

            scene cassia sentada_provocando with dissolve

            j "E não tem nada que me excita mais do que um homem que faz o que eu preciso."

            j "O que acha de durante a noite você ir até o meu apartamento?"

            j "Tenho um trabalhinho para você lá também."

            mc safado "..."

            j "Depois te mando o endereço."

        j "Agora pode continuar com sua vidinha."

        j "Tenho que terminar minha reportagem sobre o [n]. Ela vai ser muito boa pra ele também, você vai ver."

        mc desculpa "Ok..."

        scene trabalho geral with Dissolve(1.0)

        "..."

        "Espero que eu tenha feito a coisa certa..."

        jump v4_fim

        jump call_cidade

    label cassia_acordo_sim:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cassia_acordo_sucesso","inicio","local")

        $ pautas -= 1
        $ nathan_p1 = False
        $ cassia_nathan_entregou = True

        mc serio "Certo! Pode parar de me ameaçar. Você venceu!"



        show cassia sentada_rindo with dissolve

        j "E então?"

        mc desculpa "Aqui estão todas as informações sobre o contrato dele com a Blergh!"

        j "Excelente... Era justamente o que eu precisava para fechar minha matéria."

        mc serio "Você precisa me prometer que não vai fazer nada de ruim com ele. Ele confiou em mim."

        j "Você não está em posição de pedir nada, pombinho."

        mc bravo "..."

        j "Você fez um bom trabalho. E como eu disse, os amigos de [jc] só têm coisas boas esperando."

        j "Agora você pode ficar tranquilo. Sua matéria com a bonequinha já é coisa do passado."

        j "Tenho coisa muito mais interessante para publicar."

        if cassia_seducao:



            j "Ah! Só mais uma coisa."

            show cassia sentada_provocando with dissolve

            pause

            j "E não tem nada que me excita mais do que um homem que faz o que eu preciso."

            j "O que acha de durante a noite você ir até o meu apartamento?"

            j "Tenho um trabalhinho para você lá também."

            mc safado "..."

            j "Depois te mando o endereço."

        j "Agora pode continuar com sua vidinha."

        j "Tenho que terminar minha reportagem sobre o [n]. Ela vai ser muito boa pra ele também, você vai ver."

        mc desculpa "Ok..."

        scene trabalho geral with Dissolve(1.0)

        "..."

        "Espero que eu tenha feito a coisa certa..."

        jump v4_fim

        jump call_cidade

label cassia_cel_msg3_resposta:

    $ cassia_cel_msg3_resposta_check = True

    "..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("c1_save", extra_info="c1_save")

    $ iconchefe += 1

    mc preocupado "Essa mulher de novo?"

    "Da outra vez que eu me envolvi com ela não foi fácil de se livrar."

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "Para conseguir ela, você vai ter que se juntar à parte mais cruel e narcisista deste lugar."

        p "Vai deixar o amor ou a amizade de alguém bacana de lado. E ainda negar os desejos da carne."

        p "Isso mesmo... negar os seus desejos... você consegue?"



    if cassia_nathan_naoajudou:

        "Ela disse que o [n] ligou pra ela e passou as informações."

        "Eu não quis resolver as coisas por ele. Não achei certo. Ele que precisava decidir o que era melhora pra ele."
    else:


        "Eu acabei entregando as informações sobre o contrato do [n] com a Blergh!."

        "Isso ajudou a [j] e escrever a matéria sobre ele."

    "Aparentemente as coisas estão indo bem. O [n] não me mandou mensagem depois disso."

    "E agora a [j] diz que a matéria tá bombando. Quem sabe as coisas só não terminam bem?"

    mc zerado "Até parece..."

    "Um convite pra casa dela. Será que realmente é bom pra mim continuar se envolvendo com essa mulher?"

    if cassia_seducao:

        "O pior é que eu aceitei as provocações dela."

        mc tarado "E quem recusaria?"
    else:


        "Eu disse pra ela que nossa relação é estritamente profissional."

        "Mas não posso confiar que ela realmente não vá tentar nada."

    "E agora? Eu aceito o convite dela ou não?"

    menu:
        "É mais seguro não se envolver com ela":


            $ cassia_cel_msg3_r = "recusou"

            mc serio "Vai ser muito melhor não me envolver com essa vaca aproveitadora."

            "..."

            "Pronto. Agora espero que ela dê uma folga."

            mc surpreso "Quê?!"

            show screen celular_cassia

            "..."

            mc zerado "..."

            menu:
                "De jeito nenhum. Não quero nada com ela.":


                    $ cassia_e1 = "recusou"

                    "Eu sinto que essa mulher mimada não tá acostumada a levar não na cara."

                    mc serio "É bom ela começar a se acostumar."

                    "Nem vou responder."

                    "Agora é voltar pro que eu tava fazendo."

                    jump call_cidade
                "Acho que vale a pena arriscar.":


                    jump cassia_e1_aceitou
        "Não tenho nada a perder falando com ela":


            mc desculpa "Acho que não vai me matar apenas comemorar com ela."

            label cassia_e1_aceitou:

                "Mesmo ela sendo uma desgraçada, não tenho nada a perder falando com ela."

                "O que ela fez comigo e com a [c] não estava certo. Mas como paparazzo, talvez no fundo eu acabe entendendo um pouco."

                mc serio "Droga, não posso me rebaixar desse jeito."

                "Eu prometo que nunca serei um profissional antiético igual a ela!"
        "Com certeza":


            mc tarado "Não perderia essa por nada."

            jump cassia_e1_aceitou

    "Deixa eu responder ela."

    "..."

    "Enviado."

    "..."

    $ cassia_cel_msg3_rA = True

    "Ela já respondeu."

    show screen celular_cassia

    "..."

    mc envergonhado "Essa mulher não enrola mesmo."

    "Agora é tarde demais pra desistir."

    if tempo < 3:

        "Ainda tá cedo pra sair. Vou esperar escurecer."

        scene black with Dissolve(1.0)

        "Vou assistir esse programa aqui sobre mulheres comprando vestidos de noiva."

        "..."

        $ tempo = 3

        scene mapa cidade_noite with Dissolve(1.0)

        "Agora, sim. Vamos lá."
    else:


        label cassia_ponte_jump:

            "Opa. Já tá na hora de sair."

        "Melhor eu me apressar. Nem sei onde fica esse condomínio Gênesis."

    scene cidade onibus_noite with Dissolve(1.0)

    play sound "audio/som_14_onibus.mp3"

    $ renpy.pause(delay=5, hard=True)

    "..."

    "Escutei um burburinho aí sobre uma estação de trem que vai ligar a ilha até o centro da cidade."

    "Seria bem interessante se fosse verdade. Não aguento mais andar de ônibus."

    "..."

    "Acho que o condomínio é aquele ali."

    mc surpreso "!"

    play sound "audio/som_5_cidadenoite.mp3"

    scene condominio angulo1 with Dissolve(3.0):
        xalign 1.0

    scene condominio angulo1 at cenario_esquerda




    $ renpy.pause(delay=5, hard=True)

    "Olha só pra isso aqui. Que diferença pro meu prédio."

    mc triste "O que eu não daria pra morar em um lugar assim!"

    "Certeza que a galera que vive aqui caga dinheiro, inclusive a [j]."

    "..."

    "Não adianta ficar cobiçando as coisas alheias. Quem sabe eu ainda chego lá?!"

    mc envergonhado "Um dia talvez..."

    "A [j] escreveu Bloco 3, Ap 6."

    "Interessante como a gente pode andar por aqui e ninguém tá nem aí."

    "A vida nesses condomínios não tem nada a ver com a vida real."

    scene black with Dissolve(1.0)

    "..."

    "Apartamento 6. Acho que cheguei."

    scene cassia_ap porta with Dissolve(3.0)

    "Vamos ver o que ela vai aprontar comigo desta vez."

    play sound "audio/som_15_campainha.mp3"

    "..."

    "..."

    play sound "audio/som_15_campainha.mp3"

    mc zerado "Só falta ela não tá em casa."

    "..."

    "Epa. Parece que a porta tá aberta."

    mc desconfiado "..."

    menu:
        "Abrir a porta e entrar":


            mc envergonhado "A culpa foi dela de não vir me atender."

            jump cassia_e1_cama
        "Tocar a campainha novamente e esperar":


            play sound "audio/som_15_campainha.mp3"

            mc desculpa "Não vou invadir a casa dela."

            "..."

            "..."

            menu:
                "Foda-se. Vou entrar.":


                    mc serio "Não vou ficar igual a um idiota aqui."

                    jump cassia_e1_cama
                "Vou ligar pra ela.":


                    "Melhor eu ligar e falar que tô aqui."

                    "Smartphone" "Tuu... Tuuuu..."

                    j "Oi, pombinho."

                    mc normal "Tô na porta da sua casa. Você não tá aqui?"

                    j "Estou te esperando."

                    j "Pode entrar. A porta está aberta."

                    mc envergonhado "..."

                    menu:
                        "Não quero invadir sua casa. Você pode vir me atender?":


                            mc serio "Não vou invadir sua casa. Você poderia descer me atender?"

                            j "Mas eu tô deitada aqui tão gostosa."

                            mc zerado "Não me interessa."

                            j "Tudo bem, pombinho. Se você prefere assim, tô descendo."

                            "Essa mulher tá com alguma coisa na cabeça. É melhor eu tomar cuidado com o que eu faço."

                            "..."

                            jump cassia_e1_conversa
                        "Ok... Tô subindo...":


                            mc desculpa "Ok. Se é isso que você quer."

                            j "É isso que eu quero."

                            mc "Tá. Tô entrando."

                            jump cassia_e1_cama

    label cassia_e1_conversa:

        show cassia n_provocando with dissolve

        j "Por que não quis entrar?"

        mc surpreso "..."

        j "Não precisa fazer essa cara. Já vim aqui, agora vem comigo pro quarto."

        mc "Pro pro pro quarto?"

        show cassia n_costas with dissolve

        j "Tá frio aqui. E acho que você já reparou que minha roupa é um pouco leve."

        mc zerado "..."

        jump cassia_e1_conversa2

    label cassia_e1_cama:

        "Bom, se a porta tava aberta, às vezes foi ela mesma quem abriu pra eu entrar."

        "Espero que não dispare nenhum alarme."

        scene cassia_ap geral with Dissolve(3.0)

        pause

        mc surpreso "Uou! Que foda!"

        "Não dava pra esperar menos de um apartamento deste condomínio."

        mc zerado "Que diferença pra onde eu vivo..."

        "Ela não está por aqui. Vou subir as escadas..."

        "Acho que estou ouvindo alguma coisa lá em cima."

        "..."

        scene black with Dissolve(1.0)

        mc "[j]? Tá aí?"

        mc surpreso "..."

        scene cassia cama with Dissolve(3.0)

        pause

        "Caramba..."

        menu:
            "Ei, [j]! Estou aqui.":


                "Essa mulher não tem jeito..."
            "Que visão! Vou ficar quieto e aproveitar":


                mc tarado "..."

                "Essa [j] é muito gostosa mesmo, hein?"

                "Eu sei que a roupa que ela normalmente usa na redação não deixa muito pra imaginação, mas vendo ela assim de penas abertas é outra coisa."

                "Quer dizer, pernas abertas."

                mc safado "..."

                window hide

                pause

        mc envergonhado "[j]? Estou aqui..."

        j "Oi, pombinho."

        j "A cama tá tão boa... Tô achando difícil de levantar."

        mc "..."

        menu:
            "Quer que eu te ajude a levantar?":


                mc safado "Quer que eu te ajude a levantar?"

                j "Muito obrigada, mas não precisa."

                j "Só precisava de um tempinho deitada."
            "Sem pressa. Vou te esperar lá na sala.":


                mc desculpa "Não preocupe, vou te esperar lá na sala, tudo bem?"

                j "Não precisa, querido. Já estou levantando."

                j "Aii... que preguiça..."

                scene cassia cama_levantando with Dissolve(2.0)

                pause

                j "Tem dia que você também se sente todo manhoso desse jeito?"

                mc envergonhado "Não sei..."

                j "Eu sou uma mulher muito batalhadora, você sabe. Mas às vezes eu fico assim, precisando de ajuda."

                mc envergonhado "..."

                mc "Acho que eu vou..."

                j "Não... Pronto..."

    label cassia_e1_conversa2:

        scene cassia_ap quarto with Dissolve(1.0)

        show cassia n_provocando with dissolve

        j "Boa noite, [mc]."

        mc serio "Boa noite..."

        mc desculpa "Enfim... Sem querer ser grosso, mas por que me chamou?"

        j "Preciso de um motivo pra chamar um amigo de trabalho pra vir em casa?"

        mc desculpa "A gente não é o que eu chamaria de AMIGOS, [j]."

        show cassia n_pensando with dissolve

        j "Pra mim o que passou, passou."

        j "Acho que você deveria esquecer também e focar no que a nossa relação pode trazer de bom pra você a partir de agora."

        menu:
            "Você foi antiética e me manipulou. Não vou esquecer isso.":


                mc bravo "Você só pode tá brincando."

                mc "Você quase acabou com minha relação com a [c]! E com base em uma invenção sua!"

                j "Eu sei, bobinho. Mas eu já te expliquei isso, não expliquei?"

                mc "Uma explicação muito fraca."

                j "Eu não tenho paciência pra esse tipo de conversa."

                show cassia n_proposta with dissolve

                j "Você é um homem. Um adulto. Você sabe que a vida é assim."

                j "Não vou deixar nada ficar entre mim e meu sucesso. As celebridades, a revista, você, são só pedras no meu caminho."

                j "Vou usar todas pedras como uma escada pra que um dia eu esteja no topo, olhando vocês se debatendo pra viver."

                j "Melhorou?"

                mc zerado "O que você está dizendo é um absurdo, mas você fala de forma tão sincera que é impossível não entender."

                j "Então vamos pular esta parte e ir logo ao que importa."
            "Você tem razão. O passado fica no passado.":


                mc desculpa "Acho que você está certa. Não adianta ficar chorando pelo leite derramado."

                j "Agora você tá falando igual a um homem de verdade."
            "Depende do que eu for ganhar de você.":


                mc tarado "E o que eu vou ganhar a partir de agora? Dependendo do que for, podemos conversar."

                show cassia n_explicando with dissolve

                j "Ganhar de mim? Eu posso te dar MUITAS coisas, pombinho."

                j "Prazer, influência na revista, informações confidenciais... A lista é longa."

        show cassia n_costas with dissolve

        if not cassia_seducao:

            j "Na redação da revista você disse que não queria nada comigo fora do trabalho."

            j "Você ainda tem certeza disso?"

            menu:
                "Sim. Não quero nada pessoal com você.":


                    mc serio "Tenho certeza. Posso ter te ajudado, mas eu tinha meus motivos como eu disse."

                    mc "Não tenho nenhuma intenção de ver você de outra forma."

                    j "É uma pena. Tem algo em você que me atrai muito. Não sei como explicar."
                "Vendo você assim, é impossível não mudar de ideia.":


                    $ cassia_seducao = True

                    mc safado "Vendo você assim, é impossível não mudar de ideia."

                    j "Eu sei. É o que todos dizem."
        else:


            j "Eu lembro que você ficou todo animadinho quando eu disse que eu tinha uma recompensa pra você."

            j "Tenho certeza que o amiguinho também adorou a ideia de poder chegar mais perto disso aqui."

            "É verdade. Eu aceitei os avanços sexuais dela na redação da revista..."

            "Será que realmente vale a pena se envolver sexualmente com essa mulher?"

            menu:
                "Não compensa. Prefiro {b}não{/b} ter nada sexual com ela.":


                    $ cassia_seducao = False

                    mc serio "Eu mudei de ideia sobre isso. Posso ter te ajudado, mas eu tinha meus motivos como eu disse."

                    mc "Não tenho nenhuma intenção de ver você de outra forma."

                    j "É uma pena. Tem algo em você que me atrai muito. Não sei como explicar."
                "Claro que compensa. Eu quero levar ela pra cama.":


                    $ cassia_seducao = True

                    mc safado "Vendo você assim, é impossível achar outra coisa."

                    mc safado "É claro que o amigo aqui adorou."

                    j "Eu sei. É o que todos dizem."

        show cassia n_proposta with dissolve

        j "Mas prazer não é tudo. Ter um amigo como [jc] não lhe trará nenhum malefício."

        j "O poder de um homem é medido pelos amigos poderosos que ele tem. Você já ouviu isso?"

        mc desconfiado "Pra falar a verdade não."

        j "É uma frase muito real. Ela significa que aquele que possui fortes aliados é o verdadeiro poderoso."

        j "E me ter como aliada é tudo o que você precisa pra se dar bem na revista."

        j "Tem gente que diz que trabalho e dinheiro não é tudo. Sabe o que eu acho disso?"

        mc zerado "Que quem fala isso é burro?"

        j "Exatamente."

        mc "..."

        j "Dinheiro e poder SÃO tudo. Pois com eles você pode ter todo o resto."

        j "Uma vez o personagem de um seriado disse: idiotas são os que acham que o dinheiro vale mais que o poder."

        j "O que ele não disse é que É possível ter ambos."

        mc desculpa "..."

        "O jeito dessa mulher me assusta. É como se eu tivesse falando com um leão pronto pra devorar tudo, sei lá."

        show cassia n_pensando with dissolve

        j "Mas não fique assustado, pombinho."

        j "Você deu o primeiro passo. Que é ter vindo aqui me ver."

        j "Agora só precisamos esperar..."

        scene cassia_ap quarto with vpunch

        "Homem gritando" "CÁSSIA!!"

        j "Ele está aqui."

        scene nathan cena_ap with Dissolve(3.0)

        n "EU SEI QUE VOCÊ TÁ AÍ!"

        mc surpreso "[n]!"

        n "[mc]?!"

        n "O-o que você tá fazendo aqui?!"

        mc "Eu... eu..."

        n "Você sabia de tudo?!"

        mc angustiado "Não sei do que você tá falando, [n]!"

        n "Droga..."

        n "Cadê a desgraçada?!"

        j "Eu estou aqui, [n] querido."

        n "Não me chame de querido!"

        n "Você vai acabar comigo desse jeito!"

        "Meu Deus... O que tá acontecendo aqui?! Algo me diz que tem algo a ver com a matéria dela..."

        if cassia_nathan_entregou:

            "E como eu entreguei as informações dele pra ela..."

            "Isso quer dizer que eu também estou envolvido nisso.."

            mc triste "..."

        elif cassia_nathan_naoajudou:

            "Eu não quis ajudar o [n] pra ele resolver as coisas sozinho..."

            "Por um lado eu também tô envolvido em tudo isso. Será que eu devia ter ajudado?"
        else:


            "Por sorte eu não tenho nada a ver com a matéria dela."

            "Eu não passei nenhuma informação pra ela."

        mc "Eu vou descer aí."

        n "Não! Não quero saber de nada disso! Podem ir os dois pro inferno!"

        n "Adeus!"

        scene black with vpunch

        "{i}BLAM!{/i}"

        scene cassia_ap quarto with Dissolve(1.0)

        mc triste "Que merda foi essa?"

        show cassia n_pensando with dissolve

        j "Eu também não sei. Mas provavelmente ele não gostou de alguma coisa que escrevi na matéria dele."

        if cassia_nathan_entregou:

            mc bravo "Eu não entreguei as informações dele pra você fazer isso!"

            j "Cala a boca, pombinho. Isso não tem nada a ver com o contrato. É outra coisa."

            mc desconfiado "Então o que é?"

        j "Você não tem tempo pra ficar falando comigo. Vai logo atrás dele."

        mc desconfiado "Quê?!"

        j "Eu pensei que vocês tivessem se aproximado durante o bar."

        mc serio "Droga. Você tem razão. Melhor eu tentar falar com ele."

        j "[mc]. Espera."

        mc desconfiado "Que foi?"

        j "Estou contando com você. Faça seu trabalho direito e vou te recompensar."

        mc serio "..."

        "..."

        scene cassia_ap porta with slideleft

        mc angustiado "Vou ter que correr se eu quiser encontrar ele ainda."

        scene black with slideleft

        if n1_avaliacao == "amigo":

            "No bar eu decidi que ia considerar ele como um amigo."

            "Mas agora que vi ele de novo, não sei se meus sentimentos mudaram."

            menu:
                "Não mudaram. Eu quero apenas amizade":


                    "Ele é bonito, mas acho melhor ficar só na amizade mesmo."
                "Pensando melhor, acho que vou querer ir além da amizade":


                    $ n1_avaliacao = "seducao"

                    "Ele tá mais gato do que antes. Se ele também sentir atração por mim, vou querer ser mais que um amigo."

            if nathan_e1 == "amizade":

                "Ainda por cima a gente bebeu juntos. Eu senti que realmente ele me viu como amigo também."

            "De qualquer forma, não posso deixar ele sozinho agora."

        elif n1_avaliacao == "nada":

            "Desde o bar eu não fui com a cara dele. Nem sei porque eu tô indo atrás desse cara."

            "Ou será que de alguma forma eu tô vendo ele diferente?"

            menu:
                "Pensando melhor, acho que vou querer ser amigo dele.":


                    $ n1_avaliacao = "amigo"

                    "Não tenho porque odiar o sujeito. Acho que posso ser amigo dele."
                "Nada disso. Ele continua um zé roela pra mim.":


                    "Sem comentários pra esse cara..."

            "Bom... se eu quiser ajudar a [j] de alguma forma vou precisar tratar ele como um amigo."

            "Eu acho que eu sei o que a [j] quer de mim. Aquela manipuladora..."

        elif n1_avaliacao == "seducao":

            "Lá no bar eu achei ele gato, mas agora ele tá mais lindo ainda."

            "Eu decidi que quero algo mais com ele. Mas será que eu continuo sentindo a mesma coisa?"

            menu:
                "Sim. Eu quero mais que amizade":


                    "Tenho certeza. Se ele também sentir atração por mim, vou querer ser mais que um amigo."
                "Pensando melhor, acho que vou querer apenas amizade":


                    $ n1_avaliacao = "amigo"

                    "Ele é bonito, mas acho melhor ficar só na amizade mesmo."

            "Como amigo ou algo mais, tenho que ajudar ele de qualquer jeito."

            if nathan_e1 == "amizade":

                "E ainda a gente bebeu juntos. Não quero que nada de ruim aconteça com ele."

        "..."

        "Ufa! Ele tá ali."

        scene nathan cena_s_condominio with Dissolve(3.0)

        mc preocupado "Fala ae, [n]."

        n "É você, [mc]? Acho que não tô afim de falar agora, brother."

        mc triste "Eu entendo."

        if cassia_nathan_entregou:

            mc desculpa "Na verdade... não sei se eu entendo. Eu não sei como ela usou as informações da Blergh! contra você."

            n "Não. Não é isso, mano."

            n "O problema não tem nada a ver com isso."

            n "As informações que você passou pra ela não é o que vai foder minha vida."
        else:


            mc preocupado "Não sei o que tá acontecendo. Mas acho que tem a ver com aquela informação do contrato, né?"

            n "O problema não tem nada a ver com isso."

        mc preocupado "O que que tá rolando então?"

        n "Só de pensar..."

        n "Só de lembrar eu tenho vontade de matar a [j]!"

        menu:
            "Esse ódio não vai fazer bem pra você.":


                $ nathan_perdoa += 2

                mc desculpa "Eu entendo que você tá puto agora, mano. Só que isso não vai te fazer bem."

                mc preocupado "O ódio só vai te atrapalhar a tomar a melhor decisão."

                n "Acho que você tem razão. Preciso tentar me acalmar."
            "Você pode pelo menos me explicar o que tá rolando?":


                $ nathan_perdoa += 1

                mc preocupado "Você poderia pelo menos tentar me explicar? Eu me sinto parte disso também."

                n "Tudo bem. Acho que você tem razão. Talvez te falar vai acabar me ajudando."
            "A [j] não tem culpa de nada.":


                mc envergonhado "Eu entendo que você tá se sentindo frustrado, mas a [j] não é a culpada."

                n "Como assim não é a culpada?! Tá louco, brother?!"

                mc "E-eu..."

                n "Ela é a ÚNICA responsável por isso!"

                mc "Ok, eu entendo."

        scene condominio angulo1 with Dissolve(1.0)

        show nathan discutindo with dissolve

        n "A [j] é uma filha da puta! Ela escreveu na matéria dela que eu estou ilegalmente no país."

        mc surpreso "Quê?! E isso é verdade?"

        n "E o pior é que ela tá certa. A vaca descobriu isso de alguma forma e agora revelou pro país inteiro!"

        "Eu não acredito que a [j] fez uma coisa dessas. Ela queria que ele fosse grande, por que acabar com a vida do cara?"

        "Será que a história de querer fazer ele ficar grande era mentira?"

        "Tô começando a achar que ela ter me chamado aqui hoje não foi coincidência."

        mc preocupado "Isso é terrível. O que vai acontecer com você?"

        show nathan preocupado with dissolve

        n "Já tem pessoa na internet dizendo que é inadimissível eu continuar no país, que eu estou zombando da polícia."

        n "É óbvio que a polícia vai vir atrás de mim. Talvez eu seja deportado."

        n "Eu vou ter que deixar o país sem nada. Vou perder tudo o que eu conquistei, [mc]!"

        mc triste "Que merda, [n]..."

        menu:
            "A [j] precisa pagar pelo que ela fez.":


                $ nathan_perdoa += 1

                mc bravo "Isso é imperdoável! A [j] precisa pagar pelo que ela fez."

                n "Obrigado por ficar do meu lado, brother."

                mc preocupado "Só que você não pode perder o controle."

                n "Você tem razão. Eu preciso pensar nisso de forma racional."
            "Você que causou isso, não a [j].":


                mc desculpa "Desculpa por falar isso, mas não foi a [j] que causou isso na sua vida. Ela apenas revelou."

                mc "É pra isso que os jornalistas existem."

                show nathan discutindo with dissolve

                n "O que criar esse problema pra mim vai ajudar as pessoas, [mc]?!"

                n "Ela só queria fama. Sem dar a mínima pro que ia acontecer comigo. Isso não tá certo!"

                mc preocupado "Mas..."
            "Não adianta você ficar bravo com a [j].":


                $ nathan_perdoa += 2

                mc preocupado "Ficar bravo com a [j] não vai resolver seu problema. Podemos nos vingar dela depois."

                mc "Agora a gente precisa focar em como resolver essa parada que ela te meteu."

                n "Você tem razão. Ficar perdendo tempo com a [j] não vai resultar em nada."

        n "O que eu preciso agora é de uma forma de evitar que isso ganhe proporções incontroláveis."

        n "Sua revista é grande, mas ela vende principalmente aqui no estado. Mas se isso cair em rede nacional eu me ferro."

        n "Mesmo estando na internet, a matéria é acessada mais por aqui."

        n "Se eu conseguisse estancar essa sangria..."

        "A [j] disse que se eu fizer meu trabalho direito, ela vai me recompensar. Que trabalho é esse?"

        "Qual é o objetivo dela fazendo eu falar com o [n]?"

        "Droga... O cara passando por mó barra e eu pensando na [j]. Eu preciso decidir o que é mais importante pra mim."

        "Eu quero me dar bem com a [j] ou quero ficar do lado do [n]?"

        menu:

            "Vou ficar do lado do [n]" if not n1_avaliacao == "nada":

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("escolheu_nathan","cassia","personagem")

                $ c1_escolheu = "nathan"

                mc desculpa "Eu sei que as coisas parecem impossíveis agora..."

                mc charmoso "Mas eu não quero que você vá embora. Eu vou fazer tudo o que eu puder pra te ajudar."

                n "[mc]..."

                mc "Eu sei que a gente se conhece a pouco tempo."

                if nathan_e1 == "amizade":

                    mc "Só que depois de compartilhar a bebida especial do [gar] não tem mais volta."

                if n1_avaliacao == "amigo":

                    mc "Você é um grande amigo pra mim e vou fazer o possível pra que você consiga sair dessa."

                    n "Eu também sinto que você é um brother pra mim, [mc]."

                    mc "Vamos ser brothers pra sempre."

                elif n1_avaliacao == "seducao":

                    mc "Eu te acho um cara incrível. Além de bonito, é gente fina. Você realmente me atrai."

                    mc "E não quero que você vá pra longe de mim ainda."

                    show nathan seduzido with dissolve

                    n "Eu não imaginei que você me visse dessa forma, [mc]."

                    n "Já que você está sendo sincero, também quero ser. Você também chama minha atenção."

                    mc charmoso "Que bom. Mas podemos falar sobre isso depois."

                mc "Agora precisamos dar um jeito nisso..."

                show nathan preocupado with dissolve

                n "Mas como?"
            "Vou ficar do lado da [j]":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("escolheu_cassia","cassia","personagem")

                $ c1_escolheu = "cassia"

                $ nathan_perdoa += 2

                "O [n] pode até ser um cara legal, mas eu tenho mais a ganhar ficando do lado da [j]."

                if cassia_seducao:

                    "Eu tenho certeza que que posso me dar muito bem com ela... na cama também."

                    "Do jeito que ela tava me provocando também. Eu sei que ela vai querer."
                else:


                    "E mesmo que eu não queira nada sexual com ela, eu posso ganhar muitos outros benefícios."

                    "Quem sabe ela não pode até mesmo me dar umas pautas."

                mc preocupado "A situação que você tá é horrível. E eu quero te ajudar a sair dessa."

                mc "Eu entendo que você tá puto com a [j] e com razão. Ela passou a perna em você."

                mc serio "Mas não é indo contra ela que você vai resolver esse problema."

                mc "Neste momento você precisa de aliados e não de inimigos."

                show nathan bravo with dissolve

                n "Isso é um absurdo, [mc]."

                mc "Eu sei."

                n "Você sabe? Então..."

                mc "Mas situações únicas exigem pensamento fora da caixa. Você precisa fazer o que é melhor pra você."

                show nathan preocupado with dissolve

                n "Mas, [mc]... Confiar na [j] de novo..."

                mc "Não estou falando pra você confiar na [j]. A gente foi idiota de confiar nela da primeira vez."

        mc "Eu tenho uma ideia."

        n "Sério?"

        menu:
            "Vamos usar a influência da [j] ao seu favor.":


                mc serio "Vamos fazer algo impensável."

                $ renpy.notify("Nathan está avaliando seus argumentos")

                n "Como assim?"

                mc "Vamos usar a [j] ao nosso favor."

                show nathan bravo with dissolve

                n "Já disse que isso não faz nenhum sentido, [mc]!"

                n "E mesmo que isso fosse resolver meu problema, eu não quero nada com aquela víbora."

                mc concentrando "E você tem toda a razão."

                mc tarado "Mas isso vai resolver o seu problema. Ou, no mínimo, tem uma grande chance de te tirar dessa."

                mc charmoso "E é esse meu objetivo. Não ficar de birrinha com a [j]."

                if nathan_perdoa >= 4:

                    $ renpy.notify("Nathan acredita em você e aceitou sua ideia")

                    show nathan preocupado with dissolve

                    n "Por mais que isso seja extremamente viajado, talvez você tenha razão..."

                    n "Não adianta eu ficar de birra e ser deportado do país com uma mão na frente e outra atrás."

                    n "Qual é sua ideia?"

                    "O pior é que eu não tenho ideia nenhuma..."

                    mc preocupado "Você passou por muito nervoso hoje. Não adianta tomarmos qualquer decisão agora."

                    mc charmoso "O importante pra hoje é que você está aberto a fazer o que for preciso pra sair dessa."

                    n "Tá certo, [mc]. Vou pra casa e tentar respirar um pouco."

                    mc normal "É o melhor que você faz."

                    n "Obrigado por toda a ajuda."

                    mc "Não precisa me agradecer. Vou conversar com a [j] e em breve vou te falar o que fazer."

                    n "Ok. Boa noite."

                    mc preocupado "Boa..."

                    hide nathan with dissolve

                    mc triste "..."

                    scene black with Dissolve(1.0)

                    "O que foi que eu fiz?"

                    jump cassia_e1_final
                else:


                    $ renpy.notify("Nathan não confia no seu plano o suficiente para aceitar")

                    show nathan preocupado with dissolve

                    n "Eu realmente entendo seu lado, [mc]. Mas não tô confiante desse seu plano."

                    mc preocupado "Mas..."

                    n "Eu acho que temos que resolver isso sem ela. Você pode me ajudar?"

                    "Meu plano de ficar do lado da [j] não funcionou. Então pelo menos vou ajudar o [n] a sair dessa."

                    mc charmoso "Pode contar comigo."

                    show nathan seduzido with dissolve

                    n "Muito obrigado, [mc]."

                    jump cassia_e1_final_nathan
            "Vamos esquecer a [j] e resolver isso juntos.":


                mc charmoso "Esquece essa desgraçada. Essa vaca não merece nossa atenção. Vamos focar em tirar você dessa."

                mc "Não precisamos dela. E você pode contar comigo pro que precisar."

                show nathan seduzido with dissolve

                n "Falando assim parece que você vai conseguir me salvar dessa, [mc]."

                mc normal "Eu falei que você pode confiar em mim, não falei?"

                n "Vou tentar fazer isso."

label cassia_e1_final_nathan:

    $ cassia_e1 = "nathan"



    scene nathan cena_s_condominio with Dissolve(1.0)

    n "Mas a situação não tá nada boa, [mc]. De verdade."

    n "Assim que os policiais começarem a fuçar meu registro nacional, eles vão ver que eu não tenho permissão pra ficar no país."

    mc preocupado "Não quero te deixar mais preocupado, mas como isso tudo aconteceu?"

    n "Eu não posso falar com certeza. Eu me mudei para o país com apenas alguns anos. Eu nem tenho lembranças de quando cheguei aqui."

    n "Aparentemente meus pais conseguiram se regularizar, mas eu não tive a mesma sorte."

    n "Na verdade, eu nunca me preocupei com isso. Eu nem sabia que estava irregular. E também não faço a mínima ideia de quem contou isso pra [j]."

    n "Eu descobri isso hoje à tarde quando li o perfil que a [j] publicou sobre mim."

    n "Eu tô tremendo, [mc]... Eu não sei o que fazer..."

    mc triste "[n]..."

    mc "Posso me sentar do seu lado?"

    n "Claro..."

    scene nathan cena_con_mb_banco with Dissolve(3.0)

    mc "Eu não menti pra você. Eu vou fazer o que for possível pra te ajudar."

    if n1_avaliacao == "seducao":

        $ nathan_e2 = "seducao"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("nathan_e2_seducao","nathan","personagem")

        mc "Você me chamou a atenção desde o bar."

        if nge == "Garotas":

            mc "Lembra inclusive que eu não quiser ficar com nenhuma das garotas?"

            n "É verdade. Achei aquilo estranho."

            mc "É que eu queria ficar com você, [n]."

        mc "Eu sempre quis ficar com você."

        mc "Eu sei que agora não é a melhor hora, mas eu queria que você soubesse disso."

        n "[mc]... Eu..."

        mc "Eu sei! Talvez você não sinta por mim a mesma coisa. Eu não me importo. Isso não vai estragar a nossa amizade."

        mc "Mas eu tinha que falar isso pra você. Tirar isso de dentro."

        n "Sabe... Eu sei que admitir que gostar de alguém do mesmo sexo pode ser difícil."

        n "E não é todo mundo que vai aceitar seu jeito. Infelizmente tem muita pessoa cabeça dura no mundo."

        n "E ainda por cima tem os que, além de cabeça dura, são maldosos e vão querer te prejudicar."

        n "Por isso eu entendo perfeitamente você sentir esse medo de que eu vá te rejeitar."

        n "Só que eu sou ainda mais diferente do que você."

        mc "Como assim?"

        n "Eu me encaixo no que as pessoas chamam de pansexual."

        n "Isso quer dizer que eu não me atraio somente por homens e mulheres, não existe essa barreira de gênero pra mim."

        n "Se eu gostar de você, não importa se você é homem, mulher ou trans."

        n "E sendo bem sincero, você me atraiu desde o começo também."

        mc "[n]..."

        menu:
            "Eu quero te beijar.":


                mc "Eu quero te beijar."

                n "Eu também."

                "..."
            "Por hoje acho que está muito bom":


                mc "Fiquei muito feliz de saber que você sente isso por mim também."

                mc "Acho que podemos focar no seu problema agora."

                n "Pra você só declarar seus sentimentos pode estar bom, mas pra mim não."

                n "Vem aqui que eu quero beijar você."

                mc "[n]!"

        scene nathan cena_s_beijo with Dissolve(3.0)

        pause

        "..."

        "Nem acredito que tô beijando um cara desses. O [n] é tão incrível. Ele é gato e ainda por cima um cavalheiro."

        "..."

        window hide

        pause



        n "Que delícia, [mc]. Eu quero mais."

        mc "Eu também."

        n "Então vem."

        scene n2_premium1 with Dissolve(1.0)

        pause

        n "Você beija muito bem."

        mc "Valeu. Você também."

        n "Eu não tenho muita experiência. Mas eu tenho paixão."

        mc "Hmm..."

        n "[mc]... eu posso ver seu corpo? Igual lá no bar?"

        mc "No bar? Tanto faz... Quer deixar esse beijo mais quente?"

        n "Sim... eu preciso hoje."

        "A gente já vai apimentar as coisas assim? Parece tão no começo..."

        menu:
            "Tirar a sua camisa e a dele":


                mc "Eu também quero ver você sem nada. Deixa eu te ajudar."

                n "Ah... isso..."

                scene black with dissolve

                scene n2_premium2 with Dissolve(1.0)

                pause
            "Recusar e continuar beijando":


                mc "Eu não tô pronto pra isso ainda. Vamo devagar."

                n "[mc]... eu não tô aguentando, cara..."

                mc "Vem. Me beija."

        n "Hmmm..."

        n "Você é incrível, [mc]."

        mc "Hmmm... sua língua que é... como você sabe usar ela..."

        n "Não me deixa mais excitado do que eu já tô."

        mc "Você gosta..."

        n "Ah... eu... hmmm..."

        mc "Que foi?"

        n "Não aguento mais."

        scene n2_premium3 with Dissolve(1.0)

        pause

        mc "Mmmm! E-ei!"

        n "Eu não sei porque, mas eu tô tão quente agora. Eu preciso de você."

        mc "Foi tudo o que aconteceu. Você precisa de algo bom."

        n "Não. Foi você que aconteceu. Você é gostoso demais."

        mc "Hmm..."

        n "Eu não quero parar aqui."

        mc "Como assim?"

        n "Você tem razão... eu preciso de um alívio... tirar essa coisa de dentro."

        mc "Sei... e o que você quer fazer?"

        n "Quero fazer algo muito safado. Se você topar, claro..."

        mc "Fala."

        n "Eu quero que você me faça gozar."

        mc "Aqui?!"

        n "É. É a casa da Cássia mesmo. Se der problema, azar o dela."

        mc "Nathan... isso é doideira."

        n "Rapidinho... eu tiro minhas calças... e você me ajuda. Por favor."

        mc "Isso é louco... mas é quente..."

        n "Não é? Eu prometo que eu te recompenso depois. Eu tenho que me aliviar!"

        label nathan2_premium:

            "Ele tá falando sério? Masturbar ele aqui... no meio do estacionamento?"

        "Eu vou aceitar isso?"

        menu:
            "Tudo bem. Tira ele pra fora.":








                mc "Isso é locura, mas eu topo. Tira ele pra fora."

                n "Ah... só de ouvir você falando assim eu já fico excitado."

                scene black with dissolve

                call dados_essenciais from _call_dados_essenciais_2

                scene n2_premium4 with Dissolve(1.0)

                pause

                mc "Uau..."

                n "Gostou?"

                mc "Você é bem dotado..."

                n "Haha... acho que eu tive sorte nesse quesito."

                mc "Só nesse? Você é perfeito, maldito."

                n "E você também, do seu jeito."

                mc "Que romântico."

                n "Se você gostou tanto dele assim, então ajoelha e olha de pertinho."

                n "Ele é seu esta noite."

                mc "Hmmm..."

                scene black with dissolve

                scene n2_premium5 with Dissolve(1.0)

                pause

                mc "De perto ele parece ainda mais suculento..."

                n "Fico feliz que você gostou."

                mc "Você tem muita confiança no seu corpo, né? Nem uma hesitação..."

                n "Eu já fui muito elogiado eu acho... eu realmente me sinto perfeito hoje em dia."

                mc "Caralho... queria eu ter essa confiança toda."

                n "Eu posso te falar um pouco sobre isso um dia. Mas não hoje. Hoje você só cuida do meu pau..."

                mc "Hm... vai ser um prazer."

                n "Então para de olhar e pega nele logo."

                mc "Tá..."

                scene black with dissolve

                scene n2_premium6 with Dissolve(1.0)

                pause

                n "Ah... onde você tá..."

                mc "Deixa eu curtir um pouco..."

                n "Maldade..."
                scene nnew_ani32 with Dissolve(1.0)
                mc "Só de pegar nas suas bolas, você já tá crescendo..."

                n "Não judia de mim, [mc]. Pega logo nele. Não era você que tava preocupado?"

                mc "Querendo usar isso contra mim agora, é?"

                n "Mmm..."

                mc "Você gosta... tô vendo..."

                n "Eu gosto, só qu-"

                mc "Tá bom, tá bom. Deixa eu pegar logo nesse monstro..."

                scene n2_premium7 with Dissolve(1.0)

                pause

                n "Aah..."

                mc "Era isso que você queria?"

                n "Sim... bem isso..."

                mc "Você gosta da minha mão nele?"

                n "Muito. Você pega forte."

                mc "Um pau duro desses... e eu ainda não acredito no tamanho dele. Olha essa grossura..."

                n "Se você mexer nele assim... eu vou..."
                scene nnew_ani26 with Dissolve(1.0)
                mc "Mas já?"

                n "É gostoso demais."

                mc "Então se eu continuar assim..."

                n "Mnnnhngg!"

                "Ver o Nathan se contorcer assim também tá me deixando excitado."

                "Pena que a gente tá aqui nesse lugar nada a ver... se não a gente já podia..."

                n "[mc]... eu..."

                "Bom... eu posso surpreender ele agora..."

                "Ele pediu um carinho com a mão... mas eu posso usar a boca também."

                "Aposto que esse caralho é uma delícia."

                menu:
                    "Chupar ele":


                        mc "Segura mais um pouco. Não acabei ainda."

                        n "Hm?!"

                        scene n2_premium8 with vpunch

                        pause

                        n "A-ahhh! [mc]!"

                        mc "MMHMMM!!!"

                        n "Isso é bom demais! Ahnn!"
                        scene nnew_ani28 with Dissolve(1.0)
                        mc "Mnnnghh!"

                        n "Mais um pouco! Enfia mais!"

                        mc "Nnnghh!"

                        n "Eu preciso de mais, [mc]!!"

                        scene n2_premium9 with vpunch

                        pause

                        n "Ahhh!"

                        mc "Mgnnh!"

                        n "Isso! Assim mesmo!"

                        n "Eu preciso muito disso hoje, [mc]! Por favor!"

                        n "Continua me chupando!"
                        scene nnew_ani27 with Dissolve(1.0)
                        mc "NHnn!"

                        n "Tá vindo! Eu tô sentindo!"

                        mc "Vemm!"

                        n "Eu vou gozar em você! Sua boca é gostosa demais!"

                        mc "MNGNHH!!"

                        n "Assim! NNGHH!!"

                        n "Vou GOZAR!!!"

                        scene n2_premium10 with vpunch

                        pause

                        n "AAAAAAGHH!!!"

                        mc "MMMMBGH!!"

                        n "Tô gozando! Não para! Aah.... ah..."

                        mc "Ah..."

                        n "Foi incrível... você foi demais..."

                        mc "Q-que bom que você gostou..."

                        n "Eu prometo que eu vou te compensar... e você vai amar..."

                        n "Nem acredito..."
                    "Continuar com as mãos":


                        scene n2_premium7 with vpunch

                        n "Ahhh!"

                        mc "Mgnnh!"

                        n "Isso! Assim mesmo!"

                        n "Eu preciso muito disso hoje, [mc]! Por favor!"

                        n "Continua assim!"
                        scene nnew_ani26 with Dissolve(1.0)
                        mc "Pode deixar! Pode gozar!"

                        n "Tá vindo! Eu tô sentindo!"

                        mc "Vemm!"

                        n "Eu vou gozar em você! Suas mãos são boas demais!"

                        mc "Goza!!!"

                        n "Assim! NNGHH!!"

                        n "Vou GOZAR!!!"

                        scene n2_premium7 with vpunch

                        n "AAAAAAGHH!!!"

                        mc "Uou!"

                        n "Tô gozando! Não para! Aah.... ah..."

                        mc "Ah..."

                        n "Foi incrível... você foi demais..."
                        scene nnew_ani26 with Dissolve(1.0)
                        mc "Q-que bom que você gostou..."

                        n "Eu prometo que eu vou te compensar... e você vai amar..."

                        n "Nem acredito..."

                n "Aah..."

                mc "Vamo se arrumar... você não precisava urrar desse jeito."

                n "Precisava... foi intenso demais..."
            "É perigoso demais.":


                mc "É demais, [n]. O beijo vai ter que servir por hoje."

                n "Tudo bem... então me beija. Eu preciso esquecer essa noite."

                mc "Com certeza. Vem!"

                n "Hmmm!"

        scene black with Dissolve(2.0)

        "..."





        scene n2_premium11 with Dissolve(1.0)

        pause

        n "Obrigado, [mc]. Eu tava precisando disso."

        mc "Eu também tava."

        n "Mas e agora? O que eu faço?"

        mc "Você passou por muito nervoso hoje. Não adianta tomarmos qualquer decisão agora."

        mc "O importante pra hoje é que a gente decidiu que vamos resolver isso juntos e se livrar da [j]."

        n "Tá certo, [mc]. Vou pra casa e tentar respirar um pouco."

        mc "É o melhor que você faz."





        n "Obrigado por toda a ajuda."

        mc charmoso "Vou fazer tudo pra você continuar aqui, comigo."

        n "Eu espero que nosso lance não termine nesse beijo."

        mc "Eu também."

        n "Boa noite, [mc]."

        mc "Boa noite. E nós vamos te tirar dessa."



        scene black with dissolve

        scene condominio e_noite with Dissolve(3.0)

        "Eu decidi ficar do lado do [n]. Não adianta eu voltar pra falar com a [j] agora."

        "Vou direto pra casa."

        "Hoje foi uma noite muito complicada. A [j] não podia ter feito isso com o [n]."

        "Essa mulher só pensa no próprio sucesso. Todos os outros são apenas pedaço de lixo."

        mc desconfiado "Que estranho... a noite parece tão clara hoje."

        "Eu fico imaginando o que aconteeria se eu não ficasse com o Nathan e voltasse pra casa mais cedo..."

        "Bom... Hora de pegar o busão."

        scene black with Dissolve(1.0)

        $ tempo += 1

        jump v9_fim

    elif n1_avaliacao == "amigo":

        $ nathan_e2 = "amizade"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("nathan_e2_amizade","nathan","personagem")

        mc "Você é meu brother, não é?"

        mc "A revista com a matéria nem saiu ainda. Isso tá só na internet por enquanto."

        mc "Nós ainda podemos fazer alguma coisa enquanto isso. Podemos tentar impedir a publicação."

        mc "E só com a matéria da internet a coisa nunca vai ganhar olhares nacionais. Vai ser algo muito restrito."

        n "Ve-verdade... Não tinha pensado nisso ainda..."

        n "Isso seria incrível."

        mc "Não seria, vai SER, [n]!"

        scene condominio angulo1 with Dissolve(1.0)

        show nathan seduzido with dissolve

        n "É verdade... Acho que você tem razão, [mc]."

        menu:
            "A gente ainda vai pegar muita mina juntos!":


                mc normal "A gente ainda vai sair pra pegar muita mina!"

                n "Tu curte dá uma galinhada, fala ae."

                mc desconfiado "E você não?"

                n "Sou mais do tipo romântico, vamos dizer assim."

                mc zerado "..."

                n "Mas não quer dizer que eu não vá ser seu parceiro de cantada!"

                n "Vou te ajeitar várias garotas!"

                mc feliz "Assim que se fala, mano!"
            "Nós vamos curtir muitas baladas juntos ainda!":


                mc "A gente vai sair muito juntos ainda."

                n "Com certeza! Pode contar comigo."

                mc "E vamos tomar aquele treco do [gar] mais vezes! Aquele bagulho dá uma viagem massa."

                n "Só você pra me fazer me sentir animado assim, "

        n "Obrigado por me animar, brother."

        mc normal "Você é suavera demais pra ficar pra baixo desse jeito. Se anima e vamos resolver isso."

        n "Valeu mesmo, cara. Mas e agora?"

        mc preocupado "Você passou por muito nervoso hoje. Não adianta tomarmos qualquer decisão agora."

        mc charmoso "O importante pra hoje é que a gente decidiu que vamos resolver isso juntos e se livrar da [j]."

        n "Tá certo, [mc]. Vou pra casa e tentar respirar um pouco."

        mc normal "É o melhor que você faz."

        n "Obrigado por toda a ajuda."

        n "Boa noite, [mc]."

        mc "Boa noite. E nós vamos te tirar dessa."

        hide nathan with dissolve

        "Eu decidi ficar do lado do [n]. Não adianta eu voltar pra falar com a [j] agora."

        "Vou direto pra casa."

        jump xeena_encontro_especial

label cassia_e1_final:

    "..."

    scene cassia_ap geral with Dissolve(1.0)

    mc preocupado "Estou de volta..."

    show cassia n_explicando with dissolve

    j "Pelo tom da sua voz tô vendo que você não conseguiu nada."

    mc concentrando "Pelo contrário."

    j "Hm?"

    mc "Convenci ele que a melhor chance dele evitar ser deportado é usando você."

    show cassia n_provocando with dissolve

    j "Não creio..."

    mc desculpa "Só que eu tô me sentindo um merda. Isso parece tão horrível..."

    if cassia_seducao:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cassia_e1_seducao","cassia","personagem")

        $ cassia_e1 = "seducao"

        j "Não estrague o tesão que eu tô sentindo por você agora dando uma de escoteiro."

        j "Eu adoro um homem que faz o que eu preciso."

        show cassia n_costas with dissolve

        j "Eu prometo que você não vai se arrepender do seu prêmio."

        j "Você tá pronto pra vir pegar ele?"

        mc safado "Eu tô."

        j "Então vem pegar, pombinho. Aqui na cama..."

        hide cassia with dissolve

        "Era isso que eu tava esperando desde o começo..."

        scene cassia_ap quarto with Dissolve(1.0)

        show cassia n_costas with dissolve

        j "Não fique com vergonha. Só deitar e tirar a roupa."

        j "Deixa que eu vou cuidar de você direitinho esta noite."

        mc surpreso "O-ok!"

        hide cassia with dissolve

        "Nem acredito que eu finalmente vou transar!"

        scene black with Dissolve(1.0)

        j "Isso. Agora tira a roupa."

        mc safado "Claro..."







        scene cassia2_premium1 with Dissolve(1.0)

        pause

        j "É isso que você queria?"

        mc "Sim..."

        j "Eu disse que do meu lado você só vai ter coisa boa. Inclusive, muito prazer."

        mc "..."

        j "Vai ficar só olhando assim?"

        mc "Claro que não."

        j "Vem aqui e tira minha roupa. Vai olhando tudo enquanto isso."

        mc "Eu quero olhar tudo mesmo."

        j "Mas ainda não pode tocar, pombinho. Você só vai ver o que tem pra você."

        mc "Não brinca comigo."

        j "Brinco. Eu brinco com todos. Mas você vai gostar da brincadeira, isso eu tenho certeza."

        j "Vai logo, vem aqui e tira minha camisola."

        mc "Tá..."

        scene black with dissolve

        scene cassia2_premium2 with Dissolve(1.0)

        pause

        j "Melhor assim?"

        mc "Com certeza!"

        j "Você gosta do que tá vendo?"

        mc "Muito."

        j "Você tá ansioso pra experimentar logo, né?"

        menu:
            "Sim!":


                mc "Sim! Deixa eu comer você logo! Eu mereço!"

                j "Que garoto mimado que eu peguei..."

                mc "Como vai ser?"

                j "Vai ser assim. Eu vou falar e você vai fazer o que eu disser. E você vai aproveitar desse jeito."

                mc "Hm..."
            "Eu posso ir devagar.":


                mc "Eu posso ir devagar... tô curtindo tudo."

                j "Agora estou surpresa. Eu imaginava você mais... agitado depois de me ver assim."

                mc "Você sabe que eu quero, mas eu sei curtir também."

                j "Muito bem. Siga minhas ordens e você vai curtir muito."

                mc "Ok..."

        j "Eu quero que você veja muito bem... chega mais perto."

        mc "Sem-"

        j "Sem tocar..."

        mc "Ok..."

        scene cassia2_premium3 with Dissolve(1.0)

        pause

        j "O que você acha?"

        mc "Muito quente."

        j "Ela é linda, né?"

        mc "Sim. Linda... imagino como é gostosa."

        j "Olha bem. Me cheira. É a buceta mais linda que você vai ver na vida."

        mc "A é?"

        j "Por isso dinheiro é importante. Ele pode resolver os problemas que Deus te deu."

        j "Peitos, bunda, buceta... eu posso ser como eu quiser. Ser minha própria deusa."

        j "Com a ajuda das mãos habilidosas de um cirurgião, é claro. Mas, com meu dinheiro, eu posso ter quem eu quiser."

        mc "Você realmente sabe o que quer..."

        j "Eu quero tá no topo do mundo."

        mc "E eu quero tá no topo de você."

        j "Haha... desista. Eu sempre fico por cima, pombinho."

        j "Mas não quer dizer que você não vai ter sua recompensa. Vem logo."

        j "Pode acariciar minha bucetinha perfeita."

        mc "Com todo o prazer."

        scene black with dissolve

        scene cassia2_premium4 with Dissolve(1.0)

        pause

        j "Hmmm! Assim mesmo, pombinho! Pode mexer nela!"

        mc "Sim."

        j "Não precisa ter medo! Pode bagunçar minha buceta à vontade! Eu posso arrumar ela quando quiser!"

        j "AHHN! Assim mesmo!"

        mc "Eu vou ser o melhor parceiro que você já teve!"

        j "Haha! Quero ver, pombinho! Eu gosto de você animado assim! Hmm!"

        j "Pode enfiar! Assim! Nnngh!"

        j "Eu gosto de homem forte! Força, [mc]!"

        mc "Então toma!"

        scene cassia2_premium4 with vpunch

        j "HMMN!"

        j "Agora eu senti! Assim mesmo!"

        mc "Eu vou fazer você gozar só com meus dedos!"

        j "Annhh!"

        mc "Gostou, né?"

        j "Adorei! Mas não precisa parar nos dedos, querido!"

        j "Pode usar sua boca também! Me lambe!"

        mc "Sim, senhora!"

        scene black with dissolve

        scene cassia2_premium5 with Dissolve(1.0)

        pause

        mc "Hmmm!"

        j "Delícia! Enfia em tudo aí!"

        mc "Você gosta assim, é?!"

        j "Assim mesmo, querido! Com força!"

        j "Continua socando e lambendo!"

        mc "Aqui atrás também?!"

        j "Pode mexer aí também! Tudo pode! NNNGHH!"

        j "Se você continuar assim você vai conseguir me deixar molhada de verdade, pombinho!"

        mc "Eu tô sentindo você muito molhada. Não adianta falar que não, você tá adorando, Cássia."

        j "Não fica se achando... falta muito pra você levar uma mulher de verdade ao clímax."

        mc "Você vai ver, gostosa."

        mc "Só deixa eu usar meu pau em você e você vai ver o que é bom."

        j "Quem sabe. Mas agora você vai continuar me lambendo desse jeitinho."

        j "Deixa eu me ajeitar melhor, assim eu posso apertar melhor essa sua boquinha com a minha buceta."

        mc "Hm?"

        scene black with dissolve

        scene cassia2_premium6 with Dissolve(1.0)

        pause

        j "Isso mesmo, pombinho. Usa essa língua."

        mc "Agh!"

        j "Não aguenta uma buceta na sua cara, hm?!"

        mc "E-eu! Você não precisa sentar assim!"

        j "Cala a boca! Você aguenta! Toma tudo!"
        scene nnew_ani03 with Dissolve(1.0)
        "Essa mulher! Até na cama ela quer me humilhar!"

        "Eu vou aguentar isso mesmo?!"

        menu:
            "Ficar calado e continuar":


                "Eu vou só aguentar, eu sei que eu vou aproveitar depois."

                mc "Mhmmm!"

                j "Que bom que você sabe seu lugar!"
            "Parar com tudo agora":


                "Eu não vou aguentar isso!"

                mc "Chega, Cássia! Eu não quero assim!"

                j "Ounnn, bebezinho não aguenta?!"

                mc "Você não precisa transformar sexo em uma humilhação!"

                j "O que é sexo se não uma demonstração de poder? Se você não aguenta, então pode cair fora, idiota."

                mc "Eu caio mesmo."

                scene black with dissolve

                j "Idiota... vou ter que chamar aquele mocinho."

                mc "Faça o que quiser."

                jump cassia2_premium_depois

        j "Continua assim. E aperta minha bunda com força! Você é mulher, é?!"

        mc "NNghh!"

        j "Melhorou! Você até merece um carinho também."

        scene cassia2_premium7 with Dissolve(1.0)

        pause

        j "Mmm... você parece até mais animado com essa língua."

        mc "A-ah... você vai pegar no meu pau."

        j "Não, não... só nas suas bolas mesmo."

        mc "Isso é maldade!"

        j "Não é bom?"

        mc "É, mas só me deixa mais excitado!"

        j "E isso é perfeito. Eu quero você igual uma rocha."

        mc "Você..."
        scene nnew_ani01 with Dissolve(1.0)
        j "Se você vai me comer com esse pauzinho, é melhor você tá bem duro ou não vou sentir nada."

        mc "Cala a boca!"

        j "Haha! Alguém tá ficando cada vez mais excitado!"

        mc "Eu vou te comer ou não?!"

        j "Não. Eu vou usar seu pau como eu quero, só isso."

        j "Mas eu tenho que ter certeza que você tá o mais duro possível!"

        mc "Eu tô! Eu juro!"

        j "Hmm... mais um pouco de massagem..."

        mc "Aah..."

        j "Mais buceta na sua cara!"

        mc "AAGGH!"

        j "Agora acho que você tá pronto!"

        j "Se ajeita. Deixa eu subir em você."

        scene black with dissolve

        scene cassia2_premium8 with Dissolve(1.0)

        pause

        j "Assim... mmhmmmm..."





        j "Tô vendo que você tá pronto pra fazer um estrago em mim, pombinho... ah..."

        mc "Com certeza. Hmm... Você me preparou bem..."

        j "Isso que eu gosto de ouvir... nnnghh!"

        j "Tá entrando... e você tá duro mesmo."

        mc "Você é gostosa mesmo..."

        j "Eu disse... hmm... é a melhor buceta que o dinheiro pode comprar! Aproveita!"













        mc "Mas... ah... eu queria te pegar em outra posição depois."
        scene nnew_ani17 with Dissolve(1.0)
        j "Quê?!"

        j "Você acha mesmo que eu vou te deixar ficar por cima?!"

        j "Hoje você vai aprender quem é que manda, pombinho... você ainda não entendeu?"

        mc "[j]... Não tô gostando desse papo... eu fiz tudo o que você falou!"

        j "Tarde demais... hoje você vai experimentar coisas que você... mmm... nunca sentiu antes!"









        j "Agora para de papo e fica parado pra eu te usar, querido!"

        scene cassia2_premium9 with vpunch

        pause

        j "Assim! NNGH!"

        mc "AH!"

        j "Isso! Faz assim!"

        j "Ah! Aiii!"

        j "Isso!"

        scene cassia2_premium9 with vpunch

        mc "AGH! Você vai quebrar meu pau!"

        j "Foda-se! NNGHH! Delícia!"

        j "Tá vindo, pombinho!"
        scene nnew_ani13 with Dissolve(1.0)
        mc "Eu não vou conseguir gozar se você continuar assim!"

        j "Eu não me importo! EU vou gozar!!!"

        mc "AGHH!"

        j "Tá vindo! Minha buceta perfeita vai GOZARRR!"

        mc "E eu vou morr-"

        scene cassia2_premium10 with vpunch

        pause

        j "AAAAAAHHHNN!!!"

        j "Tô gozando, filho da puta!!!"

        mc "E eu vou-"

        j "AAIINNHH! Que delícia!!!"

        j "{i}puf puf{/i}"

        mc "Parou?!"

        j "Eu gozei... foi o suficiente... você fez um bom trabalho. Bom, seu pinto fez..."
        scene nnew_ani16 with Dissolve(1.0)
        mc "Mas e eu?"

        j "Você? Hmm..."

        j "Normalmente eu não me importo com o prazer dos homens, mas... como é sua primeira vez, eu vou te ajudar."

        mc "Obrigado, Cássia. Eu tô quase... Só não força tanto, vamos devagar no começo."

        j "Que lindinho... Deixa comigo, pombinho."

        scene black with dissolve

        scene cassia2_premium11 with Dissolve(1.0)

        pause

        mc "Ah... isso que eu preciso..."

        j "Você gosta, né?"

        mc "Eu gosto muito..."

        j "Que bom... eu quero que você se sinta bem também."

        mc "Então continua assim por favor... aah..."

        j "Claro."

        mc "Mmnnhh..."

        "Até que a Cássia sabe agradar quando ela quer..."

        "Nem tá parecendo ela..."

        mc "Pode acelerar agora. Tá ficando muito bom."

        j "Só assim é pouco, né?"

        mc "Um pouco mais de força e vai ficar perfeito."

        j "Eu vou deixar isso um pouco mais interessante."

        mc "Interessante?"

        j "Olha aqui."

        scene cassia2_premium12 with hpunch

        pause

        mc "C-Cássia! Que essa mão tá fazendo aí?!"

        j "Não se preocupe. Você vai gostar do que eu vou fazer..."

        mc "E-e-e-ei!"

        j "Se você quer gozar, então vai ter que ser assim."

        mc "Por quê?!"

        j "Porque é uma chance única na sua vida de ter uma experiência como essa."

        j "E eu quero que você experimente."

        mc "Não sei, não!"

        j "Eu não vou te forçar então. Você quer gozar do meu jeito ou não?"

        "Ela tá falando sério? Eu nunca fiz isso antes! Mas eu tô tão excitado! Parar agora?!"

        "O que eu faço?!"

        menu:
            "Eu tô afim de experimentar.":


                mc "Ok... eu quero experimentar. Ver se é bom mesmo..."
            "Se é o único jeito...":


                mc "Se é o único jeito de eu gozar... vai ter que ser. Não consigo parar agora."
            "De jeito nenhum! Quero parar!":


                mc "N-nem pensar! Pode parando aí! Nesse lugar ninguém mexe!"

                j "Que masculinadade frágil... você não sabe o que tá perdendo. Tem certeza?"

                mc "Sei, sim! Tenho certeza!"

                j "Que seja... Eu já consegui o que eu queria. Você quem perde."

                jump cassia2_premium_depois

        j "Boa, garoto! Deixa comigo. Eu vou cuidar de você."

        mc "Vamos ver..."

        scene black with dissolve

        j "Só curte."

        scene cassia2_premium13 with Dissolve(1.0)

        pause

        mc "A-ah..."

        j "Hmmm..."

        mc "T-trabalho completo?"

        j "Claro... shlup... no seu caralho, nas bolas e no rabo."

        mc "Aahn..."

        j "É intenso, não é?!"

        mc "S-sim!"

        j "Seu pau já tá tremendo."

        mc "É demais! Eu vou gozar!"

        j "Huhu... que bonitinho... pode gozar, pombinho."

        mc "Ah!!!"

        mc "Nnghh!"

        j "Goza pra mamãe!"

        mc "É coisa demais! NNGH!!"

        mc "AAAHH!"

        scene cassia2_premium14 with vpunch

        pause

        mc "GOZANDOOOO!!!"

        scene cassia2_premium14 with vpunch

        mc "AAAAGHHH!!!"

        j "Hmnnn! Que delícia!"

        mc "Ah... aah..."

        j "Nunca gozou assim, hm?"

        mc "Não sei! Ahnn... mas foi demais..."

        j "Não esquece de me agradecer."

        mc "O-obrigado..."

        scene black with Dissolve(1.0)

        scene cassia2_premium15 with Dissolve(1.0)

        pause

        j "Gostou, né?"

        mc "Deixa pra lá..."

        j "Você devia tá feliz demais. É difícil eu fazer um homem gozar."

        mc "Você é terrível. Uma mulher ruim pra cacete."

        j "HAHAHA! E você é um garotinho mimado."

        j "Ao invés de reclamar dos outros, por que você não toma meu lugar?"

        mc "Hm?"

        j "Tenha todo o poder e faça o que quiser com os outros ao invés de reclamar de quem te usa."

        j "O mundo é diferente pra todo mundo. Uns começam mais fácil, outros mais difícil. Mas tudo depende do seu tesão."

        j "Use a raiva, a ambição, a gula, a luxúria... tudo. Direcione tudo para seu objetivo."

        j "E quem sabe um dia você pode mandar em uma mulher como eu mando em você."

        menu:
            "Um dia eu chego lá.":


                mc "Um dia eu vou chegar lá! Eu vou comandar a porra toda!"

                j "Isso... sonhe grande... mas sonhar não é suficiente. Faça o que tem que fazer. Igual a mim."

                mc "Eu vou fazer! Você vai ver!"

                j "Pombinho..."
            "E se eu achar isso errado?":


                mc "E se eu não quiser? E se eu achar isso errado?"

                j "Então você será usado pelos outros. Não existe lugar para os 'bonzinhos' no mundo. Empatia é um ponto fraco."

                j "Olhe pra mim. Eu tenho tudo o que eu quero... cedo ou tarde."

                mc "Você é louca, isso sim."

                j "Sua opinião não me importa. Eu escolhi esse caminho anos atrás. Quando eu tive que trocar..."

        j "Enfim... Não precisa ir pra sua casa. Pode ficar aqui. Descanse e vá para o trabalho amanhã cedo."

        mc "Valeu... eu tô morto mesmo..."

        label cassia2_premium_depois:

            pass

        j "Bebezão..."



















        scene black with Dissolve(3.0)



        $ dia += 1
        $ tempo = 1

        $ renpy.block_rollback()

        window hide

        pause

        scene mc cama_cassia with Dissolve(2.0)

        "Uou!"

        "Já é de dia... Parece que a [j] não tá por aqui."

        "Que noite louca nós tivemos ontem."

        "Eu disse coisas que nem me lembro mais."

        "E devo ter feito algumas coisas que eu não me lembro também."

        "Bom... Hora de voltar pra cidade e continuar a vida."

        "Depois eu penso no lance do [n]. Tô me sentindo mega culpado, mas acho que ainda temos como ajudar ele."

        "E quem sabe eu não consiga mais algumas noitadas com a [j]?"

        jump v9_fim
    else:


        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("cassia_e1_amizade","cassia","personagem")

        j "Ora... pare de chorar igual uma criança. Vê se cresce."

        $ cassia_e1 = "amizade"
        $ favor_cassia_pauta = True
        $ pautas += 1

        j "Você foi muito bem esta noite e merece um prêmio."

        show cassia n_proposta with dissolve

        j "Como você deixou claro que não quer transar comigo... provavelmente porque é gay..."

        mc zerado "Não é porque não quero transar contigo que sou gay..."

        j "Que seja. Já que não posso te recompensar dando pra você, vou te dar outra coisa."

        j "Deixarei na redação uma pauta exclusiva que eu consegui esses dias e vou falar que foi você que conseguiu."

        j "Quando o velho maldito te chamar pedindo pautas, você pode falar pra ele usar a que eu deixei lá."

        mc surpreso "Isso vai me ajudar muito!"

        j "Eu sei. Eu disse que os amigos de [jc] só têm coisas a ganhar, nunca a perder."

        j "Agora pode sair que já que você não vai me satisfazer, vou procurar outro que faça."

        mc zerado "..."

        mc "Tchau."

        j "..."

        scene black with Dissolve(3.0)

        jump xeena_encontro_especial

label xeena_encontro_especial:

    $ tempo += 1
    $ xeena_encontro = True

    scene condominio e_noite with Dissolve(3.0)

    "Hoje foi uma noite muito complicada. A [j] não podia ter feito isso com o [n]."

    "Essa mulher só pensa no próprio sucesso. Todos os outros são apenas pedaço de lixo."

    mc desconfiado "Que estranho... a noite parece tão clara hoje. A lua parece grande demais e..."

    mc surpreso "!"

    scene xeena cena_lua with Dissolve(3.0)

    pause

    mc surpreso "Mas que porra é essa?! Tem uma moça ali! E essa lua?!"

    mc angustiado "Que loucura! Isso não existe!"

    "Deixa eu fechar os olhos e tudo vai sumir... só pode ser miragem essa porra."

    menu:
        "Fechar os olhos":


            "Vou fechar..."

            scene black with dissolve

            mc concentrando "..."

            mc "Com muita calma agora... abrindo..."
        "Forçar a vista":


            "Não! Não posso ter medo! O que é isso?!"

            scene black with dissolve

            scene xeena_new1 with Dissolve(1.0)

            pause

            "Parece uma mulher jovem... olhando pra lua gigante..."

            "Com uma roupa bem estranha... que ainda por cima brilha... Essa não pode ser a última moda da Blergh!"

            "Acho que essa é a coisa mais surreal que eu já vi na vida."

            scene black with dissolve

            scene xeena_new2 with Dissolve(1.0)

            pause

            "Ela tá segurando alguma coisa..."

            "Onde eu já vi isso antes?"

            "Eu queria poder olhar melhor pro rosto dela."

            "Como ela chegou lá? {nw}"

            scene white with dissolve

    scene condominio e_noite with Dissolve(0.5)

    mc desconfiado "Huh?"

    mc concentrando "Ufa... não tem mais nada lá."

    show xeena ola with moveinbottom

    x "Olá, humano."

    mc angustiado "Po-porra!"

    x "Digo... boa noite, senhor."

    mc triste "..."

    x "Assustei o senhor?"

    mc zerado "O que você acha?"

    mc preocupado "Da onde você veio, sua...?"

    $ x_nome = "Zeena"

    x "Meu nome é Zeena, senhor. E o seu nome, por favor?"

    mc desculpa "[mc]... Me-meu nome é [mcc]..."

    x "Não é meu objetivo deixar o [mc] assustado."

    mc concentrando "Acho que estou me sentindo melhor."

    x "Isso me deixa feliz."

    mc desconfiado "O que você tava fazendo em cima do poste?"

    show xeena pensando with dissolve

    x "Hmm..."

    x "Eu estava observando a lua."

    mc "Como você chegou ali em cima?"

    x "Hmm..."

    x "Subindo pela árvore, [mc]."

    x "Por que você faz tantas perguntas?"

    mc envergonhado "Desculpa. É que eu tô um pouco assustado ainda."

    x "Você não deveria ficar assustado por conta de uma garota inofensiva."

    x "Isso não é o comum."

    mc zerado "..."

    show xeena despedida with dissolve

    x "Agora eu tenho que ir."

    x "Tenho que..."

    x "Hmm..."

    x "Ir pra piscina."

    mc desconfiado "Essa hora?"

    x "Sim. Não está vendo minhas roupas?"

    mc "O que eu vejo é várias luzes saindo da sua roupa."

    x "São apenas detalhes para deixá-la mais bonita."

    mc zerado "Se você diz..."

    x "Boa noite, [mc]."

    mc normal "Boa noite... é..."

    x "[x]."

    mc "Desculpa. Boa noite, [x]."

    hide xeena with dissolve

    mc zerado "Tenho que ir direto pra casa. Essa noite foi louca demais."

    jump v9_fim

label v9_fim:

    $ v9_fim = True
    $ dia_cassia = dia + 2

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v9_fim","cassia","personagem")





    jump call_cidade

label cassia_ponte:

    $ cassia_ponte = True

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("c1_save", extra_info="c1_save")

    scene trabalho geral with Dissolve(1.0)

    "Olha quem vem vindo aí... a maldita..."

    show cassia provocando with dissolve

    j "Oi, traidor."

    mc desculpa "Eu não..."

    j "Tudo bem. Isso já é assunto do passado."

    j "Eu publiquei a matéria do [n] com ou sem a sua ajuda."

    j "Claro que sem as informações do contrato não foi a mesma coisa, mas ficou boa o suficiente."

    mc serio "Fico feliz por você."

    j "Bom..."

    j "Acho que está na hora da gente tentar deixar nossas desavenças no passado."

    j "O que acha da gente se encontrar hoje a noite na minha casa e comemorar que a matéria tá dando certo?"

    mc desconfiado "Se encontrar na sua casa?"

    j "Sim. Como dois jornalistas tentando resolver suas pendências."

    mc "Hmm..."

    menu:
        "Certo. Apenas para tentar resolver nossas diferenças.":


            mc concentrando "Tudo bem. Mas apenas para resolvermos nossas diferenças."
        "Sinceramente, não quero me envolver com você.":


            mc bravo "Não me leve a mal, mas depois do que houve, não quero mais nada com você."

            j "Eu entendo, pombinho. Mas quero deixar algo bem claro."

            j "Se você não falar comigo hoje, nunca mais vai poder ver o [n]."

            "Droga... se eu quiser continuar vendo o [n] vou ter que aguentar ela."

            "E agora?"

            menu:
                "Não interessa. Não vou na sua casa nunca.":


                    mc bravo "Não me importo. Não vou na sua casa de forma alguma."

                    j "A decisão é sua. Mas ser cabeça dura não vai ter levar longe na vida."

                    j "Boa sorte com suas pautas."

                    mc bravo "..."

                    jump call_cidade
                "Ok. Vou ver você, mas por causa do [n].":


                    mc concentrando "Tudo bem. Mas só por causa do [n]."

    if cassia_seducao:

        j "Você fala isso agora, mas bem que você gostou quando eu te provoquei no outro dia."

        mc safado "..."

        j "Seu olhar não me engana."

    j "Certo. Aparece na minha casa às oito horas. Eu moro no condomínio Gênesis, bloco 3, apartamento 6."

    mc normal "Combinado. Até lá."

    j "Até, pombinho."

    hide cassia with dissolve

    "Espero que eu tenha resolvido a coisa certa."

    "Ainda é cedo. Vou fazer uma hora em casa antes de ir pra lá."

    if tempo == 1:

        scene apartamento dia with Dissolve(1.0)
    else:


        scene apartamento tarde with Dissolve(1.0)

    "Vou assistir alguma coisa aqui até dar a hora de sair."

    "..."

    scene apartamento noite with Dissolve(1.0)

    jump cassia_ponte_jump
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
