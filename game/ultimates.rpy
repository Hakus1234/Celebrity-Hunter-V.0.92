label stifler_evento1:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("us1_save", extra_info="us1_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    if premium:

        p rindo "Atenção! Como você está jogando a versão premium, eu tenho uma dica especial para você!"

        p lecionando "Tem uma pauta neste encontro! Você pode pegar ela ou não, dependendo das suas escolhas."

        p "É muito simples. Aceite conversar com a delícia e entre nesse rolo que... provavelmente não vai acabar bem."

        p rindo "E aí? Você vai preferir a pauta ou tem medo de morrer? Aqui, você decide! Boa sorte!"

    "Tô cansado de sair nos mesmos lugares. Acho que hoje vou dar um pulo lá no centro da capital."

    "Bora pegar o busão."

    "..."

    scene cidade onibus_noite with Dissolve(1.0)

    "Esse ponto onde eu pego o ônibus aqui não é muito movimentado."

    "Será que o prefeito está pouco se lixando pro transporte público igual acontece-"

    scene cidade onibus_noite with vpunch

    "???" "CALA A BOCA E PÕE A MÃO NA CABEÇA!"

    mc "Quê?!"

    "???" "Mandei calar a boca! Põe logo a mão na cabeça!"

    menu:
        "Obedecer e colocar as mãos na cabeça":


            "..."

            show mc desesperado with Dissolve(1.0)

            mc "O-ok! Já coloquei!"

            "???" "Isso aí. Se você obedecer direitinho as coisas vão acabar bem pra você. Ninguém aqui precisa se machucar."

            "Droga... o que esse merda quer comigo? Será que ele tá armado?"

            "???" "Agora vira bem devagar e continua com a mão na cabeça."

            mc "Certo..."

            "O que esse idiota vai fazer agora? Será que eu consigo fugir dele?"

            mc "Tô virando."

            hide mc with dissolve
        "Se recusar e virar para trás":


            "Eu não tenho medo desse cretino. Eu só vou virar e ver do que se trata."

            "..."

            scene mc onibus_caido with vpunch

            pause

            mc "ARGH!"

            "Que merda... o idiota me empurrou!"

            "???" "Mandei não virar. É assim que você lida com assaltos? Eu podia te dar umas dicas."

            "Que idiota! Espero que ele deixe eu levantar pelo menos."

            mc "Vou levantar."

            "???" "Pode levantar. Acho que isso já foi longe de mais..."

            show cidade onibus_noite with moveinbottom

            hide cidade onibus_noite

            scene cidade onibus_noite

            mc "Quem..."

    "..."

    show stifler normal with Dissolve(1.0)

    us "E aí, [mc]?"

    mc bravo "Filho da put-"

    mc surpreso "Quê?!"

    "Espera! Acho que eu conheço esse cara..."

    us "Não lembra de mim, desgraçado?"

    mc serio "..."

    $ us_nome = "Douglas"

    mc surpreso "[us]! É você!?"

    us "É estranho ouvir alguém me chamando assim... mas é isso aí."

    mc desconfiado "Mano! Nem sei o que falar... você tá diferente..."

    show stifler ola with Dissolve(1.0)

    us "É óbvio, [mc]. Já são quantos anos? Mais de 10 pelo menos..."

    mc normal "Verdade... por aí."

    mc "E o que você fez todos esses anos? A gente precisa conversar, mano."

    us "Muita coisa. Não sei se vai dar pra falar tudo agora."

    mc desconfiado "E eu acredito. Cara, você mudou muito. Você deve ter passado por uns lances diferentes..."

    us "Nem fala. Tem umas ocorrências aí que iam ser foda até pra você publicar na sua revista."

    mc "Você sabe que eu escrevo?"

    us "Sim. Eu já vi coisa sua no site."

    mc envergonhado "Você não tem cara de quem lê esse tipo de coisa."

    us "Digamos que eu tenho uns amigos que gostam de estar de olho no que o pessoal da ilha faz."

    us "Você chamou a atenção de algumas pessoas importantes, [mc]."

    mc desconfiado "Chamei? Como assim?"

    show stifler normal with dissolve

    us "Deixa isso pra outra hora. Acho que a gente precisa colocar o papo em dia. Você tem um tempo agora?"

    menu:
        "Claro. A gente precisa conversar.":


            mc normal "Com certeza. A gente precisa colocar o papo em dia."

            label stifler_e1_aceitou:

                mc normal "Não ia fazer nada essa noite mesmo. Vamos conversar em nome dos velhos tempos."

                us "Assim que se fala, mano."

                us "Tem um lugar que eu quero que você conheça. Tenho certeza que você nunca foi lá."

                mc desconfiado "Como pode ter certeza?"

                us "Não é um lugar que pessoas como você costumam visitar."

                mc "Pessoas como eu?"

                us "Sem preconceito, chefe."

                mc "..."

                mc normal "Bom. Bora lá, então."

                us "Só vamos."
        "Hoje não vai dar.":


            "Sinceramente, não sei se quero me envolver com o [us] agora. Ele nem parece a mesma pessoa."

            "Só que se eu perder a chance de falar com ele agora, provavelmente eu não vou ver mais ele nunca."

            "Será que eu nunca mais quero ver ele?"

            menu:
                "Não quero contato com esse cara nunca mais":


                    $ stifler_e1 = "desistiu"

                    p "Você vai perder MUITA COISA tomando esta decisão. Se você não sabe o que está fazendo, recomendo voltar."

                    mc desculpa "Infelizmente não vai dar, cara. Desculpa aí."

                    show stifler serio with Dissolve(1.0)

                    us "..."

                    us "Beleza, chefe. Você quem manda."

                    us "Quem sabe a gente tromba por aí."

                    mc "Valeu. Boa sorte aí."

                    us "Falou."

                    hide stifler with dissolve

                    "Sei que é complicado ignorar um amigo de longa data, mas não tô com cabeça pra isso."

                    "Espero que fique tudo bem com ele."

                    $ stifler_conheceu = True

                    jump call_cidade
                "Vou dar uma chance pra ver o que acontece.":


                    "Não adianta eu sair julgando. Vou dar uma chance pra ver o que vai rolar."

                    jump stifler_e1_aceitou

    us "Foda que a gente vai ter que esperar o busão."

    mc concentrando "Isso é um saco mesmo."



    "..."

    play sound "audio/som_14_onibus.mp3"

    scene onibus parado_noite with Dissolve(3.0)

    pause

    mc "Finalmente chegou..."

    $ renpy.pause(delay=3, hard=True)

    "..."

    scene black with Dissolve(1.0)

    "..."

    mc normal "Enquanto isso, por que você não fala o que aconteceu com você nesses anos?"

    us "Eu prefiro contar quando a gente estiver bebendo."

    mc "Verdade."

    us "É que muita coisa aconteceu. Eu acabei virando uma celebridade, como vocês gostam de falar."

    mc surpreso "Sério?!"

    us "Pois é. Mas vamos deixar pra depois. Chegamos."

    mc surpreso "Quêêê?!"

    us "Bem-vindo ao meu distrito."

    stop sound

    mc "..."

    scene distrito geral with Dissolve(3.0)

    pause

    "Uou! É tipo uma zona. Eu nem sabia que existia um lugar assim na capital."

    show stifler ola with dissolve

    us "Eu falei que você não conhecia."

    mc envergonhado "Realmente você acertou. Nunca tinha vindo pra este lado."

    us "Tem gente que chama de Zona, tem gente que fala Distrito dos Prazeres. Mas nós chamamos apenas de Distrito."

    mc desconfiado "Como assim nós?"

    show stifler normal with dissolve

    us "Essa uma das coisas que eu vou querer te contar hoje. Mas não aqui fora."

    us "Temos muito o que conversar."

    mc "Onde você tá pensando em ir?"

    us "Tem um clube de strip e sadomasoquismo que é de um amigo meu."

    mc surpreso "Sa-sado-"

    show stifler serio with dissolve

    us "Você não tem problema com isso, tem?"

    "E agora? O [us] volta depois de anos e me traz pra um lugar desses? O que será que ele tá querendo com isso?"

    "A gente não se fala há tanto tempo. Não sei se ele é companhia pra mim."

    "E agora?"

    menu:
        "Não tenho problema nenhum. Vamos lá.":


            mc normal "Não pensei que ia visitar um lugar assim hoje, mas tô de boa. Bora lá."

            show stifler normal with dissolve

            us "Fechou. Tenho certeza que você vai curtir."

            "Espero que eu não me arrependa de entrar em um lugar assim."
        "Pelo contrário. Bora curtir esse clube.":


            mc tarado "Pelo contrário. Estou louco pra conhecer melhor esse clube."

            show stifler normal with dissolve

            us "Assim que se fala. Tenho certeza que você vai curtir pra caralho."

            mc safado "Também tô achando."
        "Sinceramente, não tô afim de ir em um lugar assim.":


            $ stifler_e1 = "puritano"

            mc desculpa "Eu concordei em sair com você pra gente colocar o papo em dia, mas não quero visitar esse tipo de lugar."

            us "Você virou um puritano, [mc]?"

            mc "Não é isso. É só que-"

            us "Eu entendo. Talvez o caminho que eu tomei me fez aceitar certos tipos de coisa que ainda não são comuns para todos."

            mc normal "Não vai ficar coisado comigo, né?"

            show stifler normal with dissolve

            us "Claro que não."



            jump stifler_e1_clube_after

    us "Pode vir atrás de mim. A dona é uma parça minha e a gente vai curtir tudo na faixa."

    mc normal "Boa, [us]."

    show stifler serio with dissolve

    us "Ah. Aqui todos me conhecem como {b}Black Cash{/b}. Talvez pegasse melhor se você me chamasse assim."

    us "Mas se você preferir, pode me chamar de [us] mesmo. Tô pouco me fudendo pra isso."

    menu:
        "Tudo bem. Vou te chamar de Black Cash.":


            $ us_nome = "Black Cash"

            mc normal "De boa. Vou te chamar de [us] então. Se é assim que o resto das pessoas te chama."

            show stifler normal with dissolve

            us "Valeu, [mc]."
        "Me sinto mais à vontade te chamando de Douglas.":


            mc desculpa "Se você não se importar, prefiro continuar te chamando de [us] mesmo."

            us "De boa."

    us "Vamos nessa."

    hide stifler with dissolve

    "..."

    "Segurança" "Boa noite, Black Cash. Veio curtir as garotas?"

    us "Fala, mano. Na verdade hoje é a noite {b}dela{/b}. Melhor não, fala ae."

    "Segurança" "Tá repreendido. Tô contigo."

    us "Esse é meu mano [mc]."

    "Segurança" "Boa noite, [mc]."

    mc normal "Boa noite..."

    us "Mas não deixa ele muito à vontade, não. Se ele voltar aqui é pra cobrar."

    "Segurança" "Que pena, maninho. Vai ter que pagar."

    mc zerado "..."

    us "Bora."

    "..."

    scene distrito_clube geral with Dissolve(3.0)

    pause

    "Eita! Que porra é essa?"

    "Essas barras de metal, essas correntes... E essas jaulas?!"

    show stifler ola with dissolve

    us "Assustou?"

    mc envergonhado "Nã-não..."

    mc "É só que é um pouco novidade pra mim."

    us "Relaxa. Ninguém come criancinha aqui. E eu falo literalmente e figuradamente também."

    mc "..."

    show stifler explicando with Dissolve(1.0)

    us "Tem regras que até a gente daqui segue. Inclusive já tiveram pessoas que tentaram vender crianças no Distrito."

    us "Foram parar a sete palmos do chão."

    mc serio "Que bom que as coisas são assim."

    us "Com certeza. Todo mundo tem um desejo ou outro que não tá certo, mas tem limite pra tudo."

    mc "Concordo."

    mc desculpa "O que eu não entendo é que você fala 'a gente'. E não só agora."

    mc "Parece que de alguma forma você se inclui nesses assuntos. Você, por acaso, também trabalha aqui?"

    show stifler serio with dissolve

    us "Sim. Eu trabalho."

    us "Mas eu quero curtir um pouco antes de falar de negócios. Vamos falar mais sobre isso depois."

    show stifler normal with dissolve

    us "O que acha da gente sentar e beber alguma coisa? O show dela está pra começar."

    mc desconfiado "Por mim tudo bem. Mas quem é 'ela'?"

    us "Você já vai ver."

    us "Vem sentar aqui."

    scene distrito_clube banco with Dissolve(3.0)

    mc normal "Ufa."

    show stifler sentado_deboa with dissolve

    us "Nem acredito que consegui te trazer pra cá."

    mc normal "Como assim?"

    us "Olha só pra esse lugar. Quem diria que o [mcc] iria passar a noite aqui?"

    mc concentrando "Se eu contar pra você o que tem acontecido comigo nos últimos tempos..."

    us "Tô ligado."

    "Eu não sei nada sobre este lugar. E parece que o [us] tá envolvido nessa coisa toda."

    "Pode ser minha chance de saber mais sobre esse canto misterioso da cidade."

    label stifler_e1_perguntas:

        "E agora? O que será que eu pergunto pra ele?"

    menu:
        "[us], o que você fez nos últimos anos?":


            mc normal "Queria saber o que aconteceu com você nos últimos anos."

            mc envergonhado "Você parece tão... tão-"

            us "Diferente?"

            mc "É."

            show stifler sentado_explicando with dissolve

            us "Muitas coisas. Nem sei por onde começar, [mc]."

            mc serio "Me fala o que você fez depois que abandonou a escola."

            us "Bom... se você quer mesmo saber, esse foi meu melhor período."

            us "Ter deixado a escola foi a melhor coisa que eu fiz na vida."

            us "Você lembra. Eu caí fora do colegial e fui direto pro mundo da música, que era meu sonho."

            mc normal "Eu lembro."

            show stifler sentado_deboa with dissolve

            us "Eu comecei a cantar rap em festas e logo minhas letras sobre a vida na biboca ficaram famosas."

            us "Um figura da cena me pegou e eu assinei um contrato em troca de grana. Eles fizeram o que quiseram comigo."

            us "Em pouco tempo me transformaram em uma estrela. Eu me apresentava nas festas de famosos e logo tava fazendo shows."

            us "Eu escolhi o nome Black Cash."

            mc envergonhado "Acho que consigo imaginar o porquê..."

            us "Você é esperto. Eu nunca fui daquele mundo. Mas o dinheiro falou mais alto."

            us "E foi então que a merda aconteceu."

            us "Mas vou deixar pra te contar sobre isso outra hora."

            mc desculpa "Ok. Mal fazer você reviver essas coisas."

            us "Relaxa."
        "O que significa este {b}Distrito{/b}?":


            mc desconfiado "Você pode me falar um pouco sobre este lugar? Distrito você disse, né?"

            us "Isso aí. Distrito é este lugar controlado pelos meus amigos."

            us "Fazemos praticamente tudo relacionado ao mundo do desejo sexual. Atendemos desde o pedido mais simples até os fetiches mais estranhos."

            show stifler sentado_explicando with dissolve

            us "Eu sei que parece obscuro, mas é a forma que encontramos de gerar grana pra manter nosso esquema."

            mc "Esquema?"

            us "É algo grande, [mc]. Vou falar sobre isso uma outra hora."

            mc normal "De boa."

            mc "Então é tudo pelo dinheiro?"

            us "Não apenas dinheiro. Tem gente famosa que visita o Distrito. Nossas garotas e garotos descobrem segredos que você nem pensa."

            "Segredos? Talvez este lugar esteja cheio de pautas pra mim. Não posso esquecer disso."

            mc desculpa "Informação às vezes é melhor do que dinheiro."

            show stifler sentado_deboa with dissolve

            us "Com certeza. E tenho certeza que você sabe muito bem disso."

            us "Então o Distrito funciona pra nós por esses motivos. Mas não só isso. Só que não vou entrar em detalhes agora."

            mc "De boa."
        "Como você tá envolvido nisso tudo?":


            mc desculpa "Sei que é algo pessoal, mas, se você puder me falar, como você tá no meio disso tudo?"

            us "Não vejo problemas em falar pra você. Mas claro que é um segredo. Não vai publicar isso na revista."

            mc envergonhado "Pode ficar tranquilo."

            us "..."

            us "Bom... tudo começou quando eu deixei o mundo do rap. Pelo menos da mainstream."

            us "Ainda acerto uns versos aí, mas só pros chegados."

            mc feliz "Quero ouvir."

            us "Sei lá... Enfim."

            show stifler sentado_explicando with dissolve

            us "Quando eu perdi meus contratos e fui para no meio da rua-"

            mc surpreso "Como?!"

            us "Não é uma história cheia de glamour, [mc]. Eu deixei muita merda no caminho."

            mc desculpa "..."

            us "Quando as coisas ficaram feias pro meu lado, eu acabei chegando ao Distrito por acaso."

            us "Eu fui reconhecido na hora, e eles me acolheram muito bem. O tempo foi passando e eu acabei entrando pro grupo."

            mc desconfiado "Mas que grupo é esse?"

            show stifler sentado_deboa with dissolve

            us "Isso vai ficar pra outra hora. É coisa demais pra falar antes da gente molhar o bico."

            mc normal "Beleza."
        "Quem está interessado em mim?":


            mc desculpa "Antes você disse que eu tinha atraído a atenção de certas pessoas. O que você quis dizer?"

            us "Não falei isso pra te assustar. Só queria dizer que sua revista tem um grande poder."

            us "Talvez você ainda não tenha se dado conta disso, mas você tem uma grande arma nas mãos."

            if priscila_namoro:

                "Pensando bem, eu consegui sobreviver ao Marco no outro dia usando o poder da revista como chantagem."

                "Talvez o [us] tenha razão e a revista tenha mais relevância do que eu imaginava."

                mc "Entendo..."
            else:


                mc desconfiado "Você acha?"

                us "Claro."

            show stifler sentado_explicando with dissolve

            us "As pessoas certas dariam muito pra poder ter influencia dentro de uma revista como a sua."

            us "O poder de elevar ou acabar com a moral de uma pessoa. É esse o poder que vocês têm."

            mc serio "O nosso reencontro... ele tem algo a ver com isso?"

            us "Não quero que você desconfie de mim, [mc]."

            mc envergonhado "Não é nada disso, mas-"

            show stifler sentado_deboa with dissolve

            us "Talvez depois eu possa te explicar tudo isso melhor."

            mc desculpa "Ok..."

    $ stifler_e1_perguntas += 1

    if stifler_e1_perguntas < 2:

        jump stifler_e1_perguntas
    else:


        if stifler_e2_perguntas:

            jump stifler_e2_perguntas

        "Tô com medo de dar um fora aqui. Melhor não me meter demais nas coisas dele."

        "Já fiz perguntas demais."

    $ stifler_e1 = "completo"

    us "O que foi, [mc]? Ficou quieto..."

    mc envergonhado "Não é nada, não..."

    us "É só esse seu interesse jornalístico? Imaginei que você te-"

    us "Opa! Se eu fosse você, olhava pra trás. Tem algo que você provavelmente vai querer ver."

    "Atrás de mim?"

    scene striper pole1 with Dissolve(2.0)

    pause

    mc surpreso "Uou!"

    mc safado "Quem é essa garota?!"

    us "É uma das nossas garotas."

    menu:
        "Essa mina é perfeita.":


            mc tarado "Essa mulher é perfeita, [us]."

            us "Perfeita mesmo. Mas tenho que te alertar de algo-"

            mc "Peraí que ela vai começar!"

            us "Ok..."
        "Ela não faz meu tipo. Sou mais chegado em rapazes.":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("stifler_e1_homossexual","stifler","personagem")

            $ stifler_mc_homens = True

            mc normal "Ela é linda, mas na verdade eu sou chegado em rapazes."

            us "Sério? Não tinha percebido isso na época. Muito bom você ter essa consciência sobre você."

            us "Já que você tá falando disso, eu já saí com homens também."

            mc "Sério?"

            us "Sim."

            mc "Opa. Ela tá começando o show."

            us "Vamos ver."

        "Gata, mas eu já tô comprometido com uma garota." if priscila_namoro or sayuri_e4 == "namoro":

            if priscila_namoro:

                "Agora eu tô namorando a [c]. Não quero trair ela com outras garotas."

            if sayuri_e4 == "namoro":

                "Eu e a [s] nos beijamos na Cidade Chinesa. Não quero trair a confiança dela com uma garota de programa."

            mc normal "Essa mulher é perfeita, mas eu já tô de rolo aí."

            us "E daí? Só pode ver uma garota?"

            mc envergonhado "É..."

            us "Olha lá. Ela vai começar o show."

    us "Quer ver de perto?"

    menu:
        "Claro. Vamos lá ver.":


            $ stifler1_striper = True

            mc tarado "E eu ia perder isso por qual motivo? Bora lá ver, mano."

            us "Bora."

            scene striper pole2 with Dissolve(3.0)

            pause

            "Uou... essa garota é gata mesmo."

            "E tão sexy..."

            us "Cuidado ter um treco aí e cair duro."

            mc tarado "Duro eu já tô..."

            us "E quem não fica duro vendo ela?"

            mc charmoso "Essa mina é incrível mesmo."

            us "Ela tá só começando. Olha aí."

            scene striper pole3 with Dissolve(3.0)

            pause

            mc surpreso "!"

            us "Eu falei..."

            us "E isso não é nada amigo. Eu trouxe você no nível 1. Se você quiser, tem muitas outras coisas pra você aqui."

            mc envergonhado "Não sei se tô pronto pra coisas mais avançadas."

            us "Vai de cada um. Quando você estiver preparado você vai saber."

            mc surpreso "Mais um movimento!"

            scene striper pole4 with Dissolve(3.0)

            pause

            mc "Demais!"

            "Striper" "Rsrs..."

            mc envergonhado "Acho que ela me ouviu..."

            mc zerado "Que vergonha..."

            us "Pode ter certeza que ela tá acostumada."

            "Eu preciso aprender a me controlar. Vou acabar pagando muito mico nesse tipo de lugar se eu não tomar cuidado."

            us "É sua primeira vez vendo uma garota fazendo pole dance eu acredito..."

            mc normal "Sim. Tenho que dizer que curti bastante."

            us "Dá pra ver seus olhos brilhando."

            mc feliz "Haha!"

            us "Vamos sentar?"

            mc normal "Ok."

            "..."
        "Tô de boa aqui.":


            mc normal "Tô de boa. Dá pra ver bem daqui."

            us "Se você prefere. Eu já vi o show dela várias vezes."

            mc normal "Ela é uma regular aqui?"

            us "Mais ou menos. Ela é uma striper de luxo vamos dizer assim."

            mc normal "De luxo?"

            scene distrito_clube banco with Dissolve(1.0)

            show stifler sentado_explicando with dissolve

            us "Ela não faz todo tipo de coisa. Ela faz só pole dance. Ela não atende clientes de forma mais direta, se é que me entende."

            mc desconfiado "Entendo. E por que? É por escolha dela?"

            us "Ela tem um passe-livre pra fazer o que bem entender."

    scene distrito_clube visao with Dissolve(3.0)

    us "Opa. Parece que ela terminou."

    mc normal "Verdade. Realmente ela-"

    "Ela tá vindo pra cá! Tenha calma, [mc]!"

    "..."

    show striper visao1_ola with Dissolve(1.0)

    ce "Boa noite, garotos."

    us "Boa noite, garota."

    ce "Gostaram do show?"

    menu:
        "Foi legal.":


            mc normal "Foi legal. Foi uma experiência nova pra mim."

            if stifler1_striper:

                ce "Você parecia bem animadinho lá na frente."

                mc envergonhado "Ah... desculpa por aquilo..."

                ce "Eu gostei de ver você animado, bobo."
        "Eu adorei. Você foi incrível.":


            mc charmoso "Você foi incrível. Achei muito bom seu show."

            if stifler1_striper:

                ce "Realmente eu vi que você estava gostando bastante."

                mc envergonhado "Hehe..."

                ce "Eu adoro quando minha platéia gosta do meu show."
            else:


                ce "Você devia ter chego mais perto."

                mc normal "É verdade. Devia mesmo."

    ce "É legal ver sangue novo aqui no clube. Ainda mais com uma carinha de bebê igual à sua."

    ce "Dá vontade de lamber ela."

    mc envergonhado "Hehe..."

    ce "E como é seu nome, mocinho?"

    mc "Eu sou [mc]. Muito prazer."

    $ ce_nome = "Celeste"

    ce "Pode me chamar de [ce]."

    mc normal "Esse é seu nome de verdade?"

    show striper visao1_interessada with Dissolve(1.0)

    ce "Você é engraçado."

    mc desconfiado "Ah?"

    ce "O que você acha da gente conversar um pouco depois?"

    mc normal "Eu tô com meu mano aqui."

    ce "O Black Cash não vai se importar se eu roubar você um pouquinho, né?"

    us "Ele é todo seu."

    ce "Você me acompanha, mocinho?"

    menu:
        "Não quero deixar meu amigo sozinho.":


            mc normal "Eu adoraria bater um papo contigo, mas não quero deixar meu parceiro aqui."

            ce "Vai ser coisa rápida. Por favor?"

            "Ela parece realmente querer falar comigo... Será que eu devo?"

            menu:
                "Eu realmente não posso agora.":


                    "Melhor manter uma distância segura. Não quero me envolver em nada com ela agora."

                    mc desculpa "Realmente não vai dar."

                    ce "Sem problemas. Até uma outra vez, [mc]. Espero ver você no clube de novo."

                    mc normal "Pode deixar."
                "Tudo bem. Se é coisa rápida...":


                    mc desculpa "Se é coisa rápida, acho que eu posso."

                    jump celeste_e1_conversa
        "Claro. Vamos lá":


            mc charmoso "Com certeza. Vamos lá?"

            label celeste_e1_conversa:

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("stifler_e1_pauta","stifler","personagem")

                $ celeste_fotos = True
                $ pautas += 1
                $ celeste_p1 = True

                ce "Vem comigo."

            scene distrito_clube geral with Dissolve(1.0)

            mc charmoso "Queria só dizer de novo que achei sua apresentação incrível."

            show striper determinada with Dissolve(1.0)

            ce "É a intenção. 99 por cento dos héteros gostam do meu show."

            mc envergonhado "..."

            ce "Eu vou ser sincera com você, [mc]. Sua vinda aqui não é coincidência."

            mc desconfiado "Como assim não é coincidência?"

            ce "Não temos muito tempo. Você precisa acreditar em mim."

            ce "Seu amigo de infância não voltou depois de 10 anos por pura coincidência. Tem algo muito maior em jogo aqui."

            mc desculpa "Você precisa entender que ouvir isso de uma pessoa que eu nunca vi não é assim tão simples."

            show striper incerta with Dissolve(1.0)

            ce "Eu sei, [mc]. Mas você também achou estranho, não achou?"

            mc "Realmente, o [us] me falou algumas coisas que me deixaram um pouco cabreiro. Mas-"

            ce "A gente não tem muito tempo. Só de eu tá falando com você aqui já vão estranhar."

            mc preocupado "Então por que você tá-"

            ce "Você é minha única chance. Eu preciso que você faça uma coisa por mim."

            mc "Tenha calma, [ce]..."

            ce "Não! Preciso que você escreva na sua revista uma coisa."

            "Uma pauta!"

            show striper determinada with dissolve

            ce "Diga que o diretor financeiro do Banco Central foi visto no Distrito dos Prazeres."

            ce "Só isso."

            mc desconfiado "Ah? Só isso?"

            show striper incerta with dissolve

            ce "Como assim só isso?"

            mc desculpa "Sua informação é muito vaga. Sem provas, é só sua palavra. Não posso passar pro chefe."

            ce "O-ok... O que acha, disso aqui?"

            mc surpreso "Fotos!"

            ce "Sim. Eu tenho imagens dele e outros funcionários do banco aqui no clube. Toma!"

            "Talvez ela realmente tenha algo que eu possa publicar na revista. Não sei se eu-"

            ce "Pega logo! Por favor!"

            "Depois eu penso melhor no que fazer com isso."

            mc preocupado "Ok. Dá aqui."

            play sound "extra/carta.mp3"

            "{b}[mc] recebeu fotos que provam que o diretor financeiro do Banco Central esteve no Distrito{/b}"

            ce "Estou contando com você, [mc]. Até."

            hide striper with moveoutright

            "Que loucura..."

            "Essa moça, falando algo dessa gravidade assim? Ela parecia desesperada. O que será que houve?"

            if not celeste_falou:

                "Ela foi embora. O que eu faço agora?"

                return

            "Melhor pensar sobre isso depois. Tenho que falar com o [us]."

    scene distrito_clube banco with Dissolve(1.0)

    show stifler sentado_deboa with dissolve

    us "E aí? O que achou dela?"

    mc normal "Uma garota incrível."

    if celeste_fotos:

        us "E o que ela queria com você? Tenho que dizer que é a primeira vez que eu vejo ela fazendo isso."

        mc desconfiado "Fazendo o que exatamente?"

        us "Chamando um cliente pra conversar de forma particular assim."

        "Tá tudo acontecendo rápido demais. Não sei ainda o que pensar. Não quero que o [us] saiba de nada."

        "Vou ter que enrolar ele, pelo menos por enquanto."

        mc envergonhado "Não foi nada de mais. Ela só me perguntou coisas... do show dela. Coisas sobre poses e etc."

        us "Entendi. Foda."
    else:


        us "Obrigado por ter recusado falar com ela por minha causa, mas eu acho que você devia ter ido falar com ela."

        if stifler_mc_homens:

            mc normal "Eu falei que meu negócio é sair com rapazes, né? Acredito que eu não tenha perdido nada."

            us "Verdade."

            mc normal "Além do mais..."

        mc normal "Eu vim aqui pra falar contigo e não com ela."

        us "De boa."

    us "A [ce] deve ser a garota mais requisitada de todo o Distrito. Já ofereceram uma grana boa pra deitarem com ela."

    us "Mas até agora ela nunca aceitou."

    mc desconfiado "E por que será?"

    us "Ela realmente não precisa da grana. Não posso falar tudo pra você agora, mas digamos que ela tem seus contatos."

    mc "..."

    show stifler sentado_explicando with dissolve

    us "Já passaram algumas horas. O que acha da gente voltar?"

    mc normal "Boa. Já tô meio cansado inclusive."

    us "Tá perdendo o gás..."

    mc concentrando "Eu tô gastando gás demais, isso sim..."

    us "Bora."

    scene distrito geral with Dissolve(1.0)

    show stifler normal with dissolve

    label stifler_e1_clube_after:

        us "Eu sei que tudo parece muito estranho agora, mas eu espero que a gente tenha outras oportunidades de se ver."

        mc normal "Com certeza. Eu moro na ilha. Bem perto do ponto de ônibus que você me fez cuzãozisse."

        show stifler ola with dissolve

        us "Haha! Mals por aquilo. Mas você tinha que ver sua cara."

        mc serio "Imagino, seu trouxa."

        mc normal "Mas foi legal te ver depois de todo esse tempo."

        mc "Marca meu telefone. Qualquer coisa me liga depois."

        us "Valeu, [mc]. Toca aqui, bro!"

        scene distrito geral

        show stifler mc_toque with Dissolve(1.0)

        us "Tem uns lances rolando aí e eu vou querer te passar melhor tudo isso depois."

        mc "Contanto que você não me coloque em furada, tá valendo."

        us "Fica sussa que é coisa pouca pra você."

        mc "Vamos ver."

        us "Você sabe voltar, né?"

        mc "Pode deixar."

        us "Valeu, [mc]. A gente se vê."

        mc "Até."

        hide stifler with dissolve

        "Distrito... uma zona dos prazeres... e o [us] tem algo a ver com tudo isso."

        "Melhor eu voltar pra casa antes que fique tarde demais."

        "O busão me espera."

        scene mc onibus_noite with Dissolve(2.0)

        "Rever o [us] depois de todos esses anos foi maneiro. Ele parece bem, mesmo estando completamente diferente."

        if not stifler_e1 == "puritano":

            "E esse clube de striptease... Aquele cenário me assustou um bocado."

            "E o [us] disse que é só o começo..."

        if stifler_mc_homens:

            "Eu falei pra ele que tenho interesse em homens e ele parece não ter preconceito nenhum com isso."

            "Até disse que ele já saiu com outros caras."

            "Quem sabe até pode rolar algo entre a gente no futuro..."

        if celeste_fotos:

            "A questão agora vai ser esse negócio que a [ce] me falou."

            "Essas fotos sobre o diretor financeiro do Banco Central. Que porra é essa?"

            "Quem será esse cara? E por que ela quer que eu publique sobre isso na revista?"

        "Alguma coisa nessa história toda de Distrito me parece complicada. Eu tenho que tomar muito cuidado em como eu vou lidar com essas pessoas."

        if v10_fim:

            "Não quero me meter em outra roubada, tipo a do [mar] e o [gus]."

            "É a última coisa que eu preciso agora."

    "Opa. Cheguei."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("stifler_e1_fim","stifler","personagem")

    $ tempo += 1

    $ stifler_conheceu = True

    "{b}[mc] agora pode visitar o Distrito durante a noite sempre que quiser. Para chegar lá, você precisa pegar o ônibus.{/b}"

    jump call_cidade

label stifler_evento2:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("us2_save", extra_info="us2_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    mc "Tô de boa."

    menu:
        "Vim só beber uma ou duas.":


            mc "A ilha tava chata e resolvi vim tomar uma ou duas aqui no distrito."

            us "Você sabe como curtir da forma certa, mano."

            mc "Com certeza."
        "Vim aqui ver se te encontrava de novo.":


            mc "Vim dar uma olhada aqui pra ver se te achava."

            us "Então tu curtiu nossa parada aqui."

            mc "Com certeza. Foi massa nossa saída da outra vez."

        "Tava louco pra ver o show da Celeste de novo." if stifler_e1 != "puritano":

            mc "Depois de ver aquele show da Celeste, não consegui dormir por uns dias. Tinha que ver de novo."

            us "Te entendo, cara. Mas isso é raro, viu? É difícil ela se apresentar daquele jeito."

            mc "É uma pena..."

    us "O que você acha da gente sentar lá e esperar o show de hoje?"

    mc "Demorou. Vamos lá."

    scene distrito_clube visao with Dissolve(1.0)

    mc surpreso "Opa!"

    show xiang andando with Dissolve(1.0)

    i "?"

    show xiang at esquerda with move

    show stifler ola with dissolve

    show stifler ola at direita with move

    $ i_nome = "Xiang"

    us "Fala aí, [i]."

    i "[us]..."

    us "Este é o [mc]. Ele é um mano, meu."

    i "Hmm..."

    hide xiang with dissolve

    mc zerado "Parece que ela não foi com a minha cara..."

    show stifler ola at centro with move

    us "Pelo contrário."

    mc desconfiado "Hm?"

    show stifler normal with Dissolve(1.0)

    us "A forma que ela parou e olhou pra você. A [i] viu alguma coisa interessante."

    mc desconfiado "Sério?"

    menu:
        "Ficar quieto e olhar para a stripper se afastando":


            mc desculpa "Só um segundo, [us]."

            hide stifler with dissolve

            show xiang costas with dissolve

            pause

            "Uou... o corpo dessa mina é perfeito."

            menu:
                "Focar na tatuagem das costas.":


                    $ xiang_flor = True

                    "Essa tatuagem..."

                    show xiang_close costas_acima with Dissolve(1.0)

                    pause

                    "Uma flor... O que será que ela significa?"
                "Focar mais pra baixo...":


                    mc safado "..."

                    show xiang_close costas_close with Dissolve(1.0)

                    pause

                    "Meu Deus! Será que eu consigo pagar um show particular dessa mina?"

                    "Ela pode cobrar quanto ela quiser, se eu tiver tá valendo."

            "Eita."

            "Que estranho... parece que ela tá olhando pra mim, mesmo não olhando..."

            "Que sensação esquisita..."

            hide xiang_close with dissolve

            us "[mc]?"

            hide xiang with dissolve

            mc normal "Opa."
        "E quem é ela?":


            mc normal "E quem é essa stripper? Ela é stripper, né?"

            us "É, sim. Inclusive ela tá aqui desde antes de eu chegar no Distrito."

            mc desconfiado "Todo esse tempo?"

            us "Sim. A direção me contou a história dela. Se você tiver interesse, posso te contar."

            mc normal "Por favor. Eu tô interessado."

            us "Não não. Agora não. É uma história complicada. Deixa pra outra hora."

            mc desconfiado "Ok..."

    us "Chega aqui."

    mc normal "Tô indo."

    if celeste_fotos:

        "O [us] tá sendo legal comigo de novo. Ele parece ser um cara bacana mesmo."

        "Só fico pensando no que a Celeste me disse..."

        "Será que foi coincidência ele ter me encontrado no ponto depois de tanto tempo?"

        "Não sei o que pensar sobre isso."

    us "[mc]?"

    mc surpreso "Opa."

    scene distrito_clube banco with Dissolve(1.0)

    mc normal "Cheguei."

    show stifler sentado_deboa with dissolve

    us "Dorme não, cara."

    mc envergonhado "Tô de boa."

    us "Então. Da outra vez você me fez umas perguntas. Não tem mais nada que você quer saber?"

    mc normal "Eu não quis parecer muito mala da outra vez."

    us "Haha! Para de ficar todo tenso, mano. A gente é amigo, não é?"

    mc envergonhado "Ok..."

    us "Então. Tem algo mais que você queira saber?"

    $ stifler_e1_perguntas = 0
    $ stifler_e2_perguntas = True

    jump stifler_e1_perguntas

    label stifler_e2_perguntas:

        "Acho que agora já sei tudo o que eu precisava sobre ele."

        mc normal "Valeu, [us]. E desculpa a xeretisse."

    us "Relaxa aí, cara. Eu queria que você perguntasse tudo o que você quisesse. Quero que você confie em mim."

    mc desconfiado "Confiar em você? Como assim? Tipo, a gente ja não é amigo?"

    show stifler sentado_explicando with dissolve

    us "Sim, mas não tô falando desse tipo de confiança. Eu tô falando de confiança de verdade."

    us "Tipo de você deixar sua vida nas minhas mãos."

    mc preocupado "Mas pra que isso?"

    mc "Tem algo a ver com o Distrito? Com tudo isso em que você tá metido?"

    show stifler sentado_deboa with dissolve

    us "Não precisa fazer essa cara. É justamente pra você ficar de boa que estamos aqui e eu estou respondendo tudo."

    mc envergonhado "Entendo, malz."

    us "Só relaxa."

    us "E sim. Tem a ver com o Distrito."

    mc surpreso "Quê?!"

    us "Mas eu vou te falar sobre isso depois. Hoje eu quero que você conheça algumas pessoas. Uma pessoa em particular."

    mc desconfiado "Certo..."

    us "Mas primeiro, eu vi que você ficou interessado na [i]. E se a gente chamar ela pra fazer um show pra gente?"

    "Um show particular daquela garota de cabelo roxo..."

    menu:
        "Na verdade, eu prefiro passar esse tempo com você.":


            mc normal "Pra falar a verdade, acho que eu preciso conversar com você."

            us "Certeza, mano?"

            mc charmoso "Certeza."

            jump stifler_e2_conversa

        "Demorou! Só não sei se tenho grana..." if cash < 100:

            mc surpreso "Demorou!"

            mc envergonhado "Mas não sei se tenho grana pra isso..."

        "Agora sim você falou algo que presta. Bora." if cash >= 100:

            mc charmoso "Com certeza. Agora sim você falou minha lingua."

            mc "E quanto que vai ser?"

    us "Pode deixar essa por minha conta. Mas se você vier aqui depois daí tu desembolsa a grana."

    mc normal "Beleza."

    jump stifler_e2_xiang

label stifler_e2_xiang:

    $ stifler2_xiang = True

    us "Eu vou chamar ela. Pode ficar de boa."

    mc normal "Ok."

    hide stifler with dissolve

    "O [us] não precisa pagar pra entrar aqui... e ainda mais... ele pode dizer quem paga ou não."

    "A impressão que eu tenho é que ele tá longe de ser apenas um cliente conhecido."

    "Digo... parece que ele tem algum cargo, como se ele também fizesse parte da 'direção'."

    "E parece que ele tá bem interessado em mim... ou no poder da revista..."

    "Eu tenho a impressão que ele tá me preparando pra alguma coisa com essa conversa toda."

    "Provavelmente ele vai me pedir algum favor. É a única coisa que eu consigo pensar."

    "Tenho que pensar muito bem no que eu vou responder quando essa hora chegar."

    us "Aqui está."

    "Opa!"

    scene distrito_clube visao with dissolve

    mc envergonhado "O-olá."

    show xiang andando with dissolve

    i "..."

    us "[mc], deixa ela passar que tem toda uma preparação ali."

    mc surpreso "Ah! Desculpa..."

    i "..."

    hide xiang with dissolve

    "..."

    show stifler normal with dissolve

    us "Você vai ter que ser mais atento se você for querer vir pra cá sozinho."

    mc envergonhado "... Pode deixar."

    us "Bom, eu vou deixar você curtir sozinho aí com ela."

    mc surpreso "Sério?! Mas você vai perder a apresentação dessa gata?"

    us "Eu já sei tudo o que ela faz. Tu vai gostar, vai por mim."

    mc desconfiado "Ok..."

    mc safado "Valeu mano. Deixa eu curtir aqui."

    us "Aproveita."

    hide stifler with dissolve

    "Por que será que o [us] não quis ver a apre-"

    i "Pronta..."

    mc surpreso "O-ok!"



    mc surpreso "{i}Glup{/i}"

    scene xiang show1_1 with Dissolve(2.0)

    $ renpy.pause(5)

    pause

    "Que mina gata demais..."

    menu:
        "Você é gata demais.":


            mc charmoso "Você é gata demais..."

            i "..."
        "...":


            mc charmoso "..."

            i "..."

    i "..."

    window hide

    pause

    scene xiang show1_2 with Dissolve(2.0)

    $ renpy.pause(5)

    pause

    "Uou... olha só pra..."

    mc safado "..."

    menu:
        "Focar na tatuagem das costas.":


            show xiang_close costas_acima with Dissolve(1.0)

            pause

            if not xiang_flor:

                "Essa tatuagem..."

                "Uma flor... O que será que ela significa?"
            else:


                "Quero prestar bastante atenção nessa flor de novo..."

                "Será que é algo somente estético?"

            $ xiang_flor = True
        "Focar mais pra baixo...":


            mc safado "..."

            show xiang_close costas_close with Dissolve(1.0)

            pause

            "É impossível não olhar pra essa bunda perfeita dela..."

    hide xiang_close with dissolve



    "Será que eu posso me aproximar mais dela pra ver melhor?"

    menu:
        "Melhor não arriscar e ficar por aqui mesmo":


            "Não vou causar. Essa mina me dá um pouco de medo."

            mc "Você é incrível, [i]. É [i], né?"

            i "..."

            mc envergonhado "O-ok..."
        "Quem não arrisca não petisca. Quero ver ela melhor":


            "Não vou perder a chance de ver ela mais de perto."

            window hide

            pause

            scene xiang show1_3 with Dissolve(2.0)

            $ renpy.pause(5)

            pause

            "Simplesmente incrível..."

            i "..."

            if xiang_flor:

                i "Você gostou da flor?"

                mc surpreso "Qu-quê?!"

                i "..."

                mc envergonhado "A flor?"

                i "..."

                mc surpreso "!"

                "Ela tá falando da tatuagem de flor! Sua mula!"

                mc charmoso "Sim, achei incrível. Muito sexy."

                i "..."

                mc "..."

                i "..."

    "Opa! Ela tá saindo da jaula. Deve ter acabado."

    "Deixa eu me levantar."

    scene distrito_clube visao with Dissolve(1.0)

    mc envergonhado "É..."

    show xiang andando with dissolve

    mc charmoso "Você foi incrível."

    i "..."

    show xiang costas with dissolve

    i "..."

    if xiang_flor:

        i "Pode olhar para a flor..."

        mc desconfiado "Hm?"

    hide xiang with dissolve

    "Tenho a impressão que eu vi mais a bunda do que o rosto dessa garota."

    "Sem dúvidas ela é uma peça. Talvez eu devesse vir mais vezes aqui e tentar me encontrar com ela."

    "Ah! O [us] tá me esperando no bar. Deixa eu correr lá."

label stifler_e2_conversa:

    scene distrito_clube pub with dissolve

    if stifler2_xiang:

        mc normal "Fala aí, [us]."

    us "Senta aí."

    show mc bdsm_blackcash with Dissolve(1.0)

    if stifler2_xiang:

        us "E aí, curtiu o show da [i]?"

        mc "Achei incrível."

        mc "Na verdade, ela é meio estranha, né?"

        us "Haha! Com certeza! Eu nunca vi ela falando qualquer coisa com ninguém."

        if xiang_flor:

            mc "Ué... ela me disse algo sobre a tatuagem de flor nas costas dela."

            us "Como assim?"

            mc "Ela disse que eu podia olhar pra flor se eu quisesse..."

            us "Sério mesmo? Tá me zoando..."

            mc "Tô falando, cara!"

            us "Eu... acho que nunca ouvi ela falando nada além do meu nome..."

            mc "..."

        us "Mas é loucura! Você devia vir aqui mais vezes e pedir um show dela."

        mc "Tô pensando nisso mesmo."
    else:


        mc "Fala aí. Como tão as coisas?"

        us "Correria, cara. Muita correria."

        mc "..."

        us "Tipo, muito trabalho, o dia todo."

        us "Às vezes eu tenho saudades do tempo de rapper. Criar as músicas, fazer a galera ficar doida com seu som. Muito dinheiro..."

        mc "Eu imagino..."

        us "Isso agora é passado."

        us "Eu tô muito feliz aqui também, cara. E não dá pra reclamar da grana."

        mc "Ricão..."

        us "Haha! Não é pra tanto, mas dá pra comprar quase tudo o que você quiser."

        mc "Uou..."

        us "Mas tem que ralar!"

        mc "Ralar eu ralo, só tá faltando a parte da grana."

        us "Nem sempre grana é o mais importante."

        mc "Na maioria das vezes é, sim."

        us "Se você diz..."

    nora "O que os meninos estão falando?"

    show mc bdsm_nora with Dissolve(1.0)

    mc "Senhora..."

    show stifler bdsm_bar with dissolve

    $ nora_nome = "Madame Nora"

    us "[nora]. Boa noite."

    nora "Boa noite, Black Cash. Você tem coisa pra fazer hoje, não tem?"

    us "Na verdade eu tô quase saindo. Só entrei porque o [mon] avisou que meu mano [mc] tava aqui."

    nora "Entendo... Toma cuidado para não montarem em você."

    us "Tá tudo tranquilo."

    nora "Eu vou deixar vocês conversarem."

    us "Na verdade, [nora]. Este é o rapaz que eu vinha te falando."

    nora "O da revista?"

    us "Esse mesmo. Ele é um parça meu de muitos anos. Eu coloco minha mão no fogo por ele."

    nora "Sei..."

    us "O nome dele é [mcc] e ele mora na ilha. Mas ele não tem nada com os italianos."

    nora "..."

    "Como assim nada com os italianos? O que ele quer dizer com isso?"

    nora "E o que o senhor [mc] está achando do Distrito?"

    "Hmm... o que eu acho daqui?"

    menu:
        "É o tipo de entretenimento que eu adoro.":


            mc "Sem dúvida, é o tipo de entretenimento que eu mais gosto, se é que você me entende."



            nora "Magnifíco. Espero que o Black Cash esteja sendo um bom anfitrião."

            mc "Com certeza. Aos poucos ele tá me falando do que aconteceu com ele e como ele chegou aqui."

            nora "Fico feliz de ouvir isso. Não tenha pressa, logo você saberá mais sobre o Distrito."
        "O [us] ainda está me mostrando tudo.":


            mc "Acho que ainda é cedo pra julgamentos. O [us] tá me mostrando tudo com calma."

            nora "O Distrito é um lugar complexo. Sei que pode parecer paradoxal a forma como tudo acontece."

            nora "Ainda mais pra quem vem de fora, tudo pode parecer um tanto quanto sombrio. Mas..."
        "Não sei se é minha praia, não...":


            mc "Espero não estar sendo rude, mas não sei se esse é o tipo de lugar pra mim."

            nora "Eu reconheço que o Distrito não é pra todos. Não se preocupe em ser sincero comigo."

            nora "Mas o Black Cash é seu amigo. Continue conversando com ele."

    nora "Estou certa que você vai gostar do que oferecemos."

    mc "Ok..."

    nora "Bom. Se os garotos me dão licença, eu tenho que resolver alguns problemas."

    us "Até, Madame."

    mc "Tchau, senhora."

    nora "Por favor, me chame de [nora]."

    mc "Ok, [nora]. Até mais."

    nora "Com licença."

    show mc bdsm_angulo_sul with Dissolve(1.0)

    mc "Essa senhora..."

    us "Não julgue ela por essa forma humilde e educada. Na verdade, ela é uma das cabeças do Distrito."

    mc "Essa senhora?!"

    us "A [nora] é incrível, [mc]. Espero que você tenha outras chances de falar com ela."

    mc "Certo..."

    "Mas... eu achei que ela fosse só uma garçonete sem nenhum senso de estilo..."

    us "Como eu falei pra ela, eu só vim dar uma passada aqui mesmo porque o [mon] disse que você tava aqui."

    us "Tenho que resolver uns negócios hoje. Mas nós vamos nos falar de novo com certeza."

    mc "Pode deixar."

    us "Agora você encontrou o caminho daqui, tenho a impressão que você não vai querer sair."

    mc "Hehe..."

    if stifler2_xiang:

        us "Ainda mais depois do show da [i], né, safado?"

        mc "Que isso! Tá me ofendendo!"

        us "Haha!"

    us "O que você precisa agora é de uma roupa mais caprichada. Mais no estilo, entende?"

    mc "Você diz, mais chique, tipo um blazer?"

    us "Claro que não, mano! Isso é roupa dos italianos que vem passar vergonha aqui."

    us "Tô falando disso aqui, mano. Um lance mais a cara do Distrito."

    us "Olha aqui pra mim. Um lance assim, entendeu?"

    mc "Pode ser uma boa mesmo..."

    us "Com certeza vai ser, cara. Não só eu, mas todos aqui vão te olhar com outros olhos. Vai por mim."

    mc "Beleza. Vou dar uma olhada lá."

    us "Fechou então."

    mc "Pera que eu vou com você até a entrada."

    us "Bora."

    scene distrito_clube geral with Dissolve(1.0)

    show stifler mc_toque with Dissolve(1.0)

    us "Quero ver você aqui mais vezes. Sempre que dá, eu dou uma passada aqui. Vamos trocar uma ideia."

    mc "Com certeza, vamos tomar uma bebida juntos."

    us "Demorou, parça. Até a próxima."

    mc "Valeu, [us]."

    hide stifler with dissolve

    "..."

    "Bom, eu queria conversar mais com a [nora], e quem sabe até saber algo a mais sobre a [i]. Mas hoje já tá tarde."

    "Vou sair e volto outro dia."

    "..."

    scene distrito esquina with Dissolve(1.0)

    mc normal "[mon], vou indo nessa."

    show montanha normal with dissolve

    mon "Boa noite, maninho. Valeu pela visita."

    mc "A gente se fala."

    mon "Com certeza."

    mc "Falous!"

    hide montanha with dissolve

    show black with Dissolve(1.0)

    p rindo "O [mc] pode visitar o Distrito todas as noites. Cada noite, um personagem diferente estará no Clube de BDSM."

    p "Você precisa de dinheiro para entrar no bar, então não deixe de trabalhar no bar sempre que possível."

    p "Para não gastar dinheiro à toa, você pode perguntar pro [mon] quem está no bar naquela noite."

    p "Assim você entra só quando os personagens que você quer conversar estiverem no clube."

    p "Bom jogo!"

    $ stifler_e2_fim = True

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
