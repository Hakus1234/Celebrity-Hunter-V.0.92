

label academia_maria_cancelar:

    call pre_tela from _call_pre_tela

    if maria_namoro:

        mc "Só vim ver minha namorada mesmo."

        ma "Que fofo."
    else:


        mc "Só vim dar um alô mesmo."

        ma "A tá."

    ma "Quando tiver afim de malhar comigo, só me chamar. Tô sempre aqui pra você."

    mc "Valeu."

    jump cidade_academia

label academia_maria:

    call pre_tela from _call_pre_tela_1

    if maria_namoro:

        "A [ma] tá ali. Ela é mesmo muito linda. Deixa eu falar com ela."
    else:


        "Olha a [ma] ali. Deixa eu falar com ela."

    scene maria_academia_sentada with Dissolve(1.0)

    pause

    if maria_namoro:

        mc charmoso "Bom dia, linda."

        ma "Fala, gato. Vamo treinar?"
    else:


        mc normal "Fala aí, [ma]. Tudo bem?"

        ma "Tudo. E você?"

        mc "Tudo legal."

        ma "Bora treinar?"

    $ area = "academia_maria"

    show screen cidade_tela
    with dissolve

    pause

label maria_academia_treino:

    call pre_tela from _call_pre_tela_2

    mc charmoso "Vim pra gente malhar juntos."

    if maria_academia == 4:

        ma "[mc], eu não tô me sentindo muito legal esses dias. Não vou conseguir treinar com você. Você me perdoa?"

        mc preocupado "Claro. Não precisa nem falar isso."

        mc charmoso "Não se preocupa comigo porque eu venho de tarde aqui e treino qualquer coisa."

        ma "Obrigada. É só por um tempo. Não sei onde eu peguei essa desgraça, e nem é nada horrível, só preciso descansar um pouco."

        mc "Relaxa."

        if maria_namoro:

            mc "E pode contar comigo, ok? Na saúde e na doença, lembra?"

            ma "Isso é só depois do casamento. Por enquanto só quero que você veja meu lado saudável."

            mc envergonhado "Haha... ok."

        "{b}A história da [ma] continuará em atualizações futuras. Fique de olho nas notificações e redes sociais para saber mais{/b}"

        show screen cidade_tela
        with dissolve

        pause

    $ proibido_salvar = True
    $ show_quick_menu = False

    call checa_logado from _call_checa_logado_3

    ma "Pronto pra mais um dia puxado?"

    call anuncio from _call_anuncio_4

    ma "Você sabe que eu não vou pegar leve com você."

    mc "Ok..."

    mc "Você acha que eu já posso treinar?"

    $ renpy.choice_for_skipping()

    call checa_tempo from _call_checa_tempo_4

    python:
        if renpy.android:
            mttempo = PythonSDLActivity.checkMTtempoNext()

    if not mttempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        ma "Acho que é melhor você dar mais um tempinho. É perigoso você se machucar se treinar de novo muito rápido."

        if maria_namoro:

            ma "E eu não vou querer ver meu herói machucado, tá? Quero você foda pra gente pegar pesado juntos."

            mc charmoso "Pode deixar."

        show black with Dissolve(1.0)

        p rindo "O [mc] pode treinar com a [ma] uma vez a cada 1 hora do mundo real."

        label academia_maria_coins:

            p "Use o app Relógio no celular do [mc] para ver quando o próximo treino estará disponível."

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        p "Ou você pode liberar o próximo treino agora mesmo usando Celebrity Coins."

        if persistent.coins >= 100:

            p "Liberar o próximo treino usará 100 Celebrity Coins."

            menu:
                "Usar {b}100 Celebrity Coins{/b} e liberar o próximo treino":


                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaMTTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    p "Legal! Você usou 100 Celebrity Coins para liberar o próximo treino!"

                    $ renpy.block_rollback()

                    hide black with dissolve

                    ma "Pensando bem, acho que a gente já esperou o suficiente. Dá pra treinar já."

                    mc "Sério?"

                    jump maria_academia_pronto
                "Agora não. Vou esperar o tempo.":


                    p "Sem problemas. Só esperar uma hora e voltar, tá?"

                    hide black with dissolve

                    show screen cidade_tela
                    with dissolve

                    pause
        else:


            p lecionando "Você precisa de ao menos 100 Celebrity Coins para liberar o treino."

            p "Você pode adquirir Celebrity Coins vendo vídeos."

            p "Você pode comprar Celebrity Coins com dinheiro do {b}seu{/b} mundo."

            p "Assim você pode continuar a história agora mesmo e ainda colabora com o desenvolvimento de CH."

            menu:
                "Ok. Quero comprar.":


                    p rindo "Legal!"

                    call comprar_coins from _call_comprar_coins_3

                    p "Se você comprou, agora pode avançar o tempo usando Celebrity Coins."

                    hide black with dissolve

                    jump academia_maria_coins
                "A vida é dura. Tô sem grana pra isso agora.":


                    p rindo "Não tem problema."

                    p "Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja mais tarde. Acesse o Menu para saber mais."

                    jump cidade_academia

            label maria_academia_sair:

                hide black with Dissolve(1.0)

                ma "Então amanhã você volta e continuamos o treinamento, ok?"

                mc "Ok. Vou seguir as dicas da minha personal trainer."

                ma "Isso mesmo."

                jump cidade_academia
    else:


        label maria_academia_pronto:

            $ proibido_salvar = True
            $ show_quick_menu = False

            ma "Com certeza."

        python:
            if renpy.android:
                PythonSDLActivity.setMTtempoNext()
                
                renpy.block_rollback()

    label academia_maria_introducao:

        if maria_academia == 0:

            ma "Hoje é seu primeiro dia treinando comigo, então prometo que vou pegar leve, ok?"

            mc normal "Valeu, treinadora."

            ma "Antes de qualquer atividade, tem que começar alongando sempre, hein?"

            if maria_relacao:

                mc safado "A-alongamento!"

                ma "Ei! Eu tô vendo essa cara aí."

                mc envergonhado "Bom... é que..."

                ma "Eu sei exatamente o que você tá pensando. Mas a gente vai T R E I N A R, ouviu? Treino em primeiro lugar."

                mc angustiado "Quê?! Como assim?!"

                ma "Mas é um bobo mesmo..."

                mc envergonhado "Bom... se você tá falando..."

                ma "Você vai sobreviver."

            ma "Vem. Deixa eu te mostrar."

            mc charmoso "Tô logo atrás."

        elif maria_academia == 1:

            ma "Você parece animado. Realmente tá curtindo malhar, hein."

            if maria_relacao:

                mc charmoso "Acho que eu curto mais você mesmo."

                ma "Safado."
            else:


                mc normal "Acho que tô pegando gosto pela coisa."

            ma "Pronto pra mais um dia?"

            mc "Bora pro alongamento."

            ma "Já tá sabendo."

        elif maria_academia == 3:

            ma "Que bom que você veio."

            mc normal "Já tá virando minha atividade preferida na manhã."

            if maria_namoro:

                ma "Verdade? Mas por causa do treino ou pra ver sua namorada gostosa?"

                mc envergonhado "Não sei... deixa eu pensar."

                ma "Ai, como é engraçadinho! Você vai ver o que eu vou fazer com você hoje!"

                mc surpreso "N-não! Tava brincando!"

            ma "Vem pro alongamento."

            mc concentrando "Droga..."

            ma "Nada de droga."

    label academia_maria_alongamento:

        scene maria_academia_alongamento with Dissolve(1.0)

        pause

        if maria_academia == 0:

            ma "Primeira coisa que você tem que fazer quando tá se alongando é pensar quais músculos você pretende usar no treino."

            ma "Hoje a gente vai correr na esteira, então bora alongar bem as pernas."

            ma "Olha direitinho pra depois você fazer igual."

            if maria_relacao:

                mc tarado "Você sabe que nessa parte eu tô treinado."

                ma "Haha... engraçadinho."

                if maria_namoro:

                    ma "Pelo menos agora a gente tá juntos, né? Não é só mais um tarado."

                    mc zerado "Ei... eu nunca fui um tarado."

                    ma "Não, imagina..."

            ma "Pegou como eu faço?"

            mc normal "Sim. Tranquilo."

        elif maria_academia == 1:

            ma "Quando for se alongar, não é pra fazer correndo e nem ter preguiça."

            ma "Precisa durar, pelo menos, cinco minutos. Pode durar mais, mas tenta não fazer menos do que isso."

            mc "Certo."

            ma "Fica um minutinho em cada grupo muscular. Assim você garante que não vai se maxucar em rotinas mais puxadas."

            if maria_relacao:

                ma "E como sempre, você atento olhando direitinho em mim."

                mc safado "..."

                ma "Nem tá me ouvindo."

                mc desconfiado "Como?"

                ma "Nada, tonto..."

                mc "?"

        ma "Viu? Sem preguiça."

    scene cidade academia2 with Dissolve(1.0)

    ma "Terminado o alongamento, bora pra esteira."

    if maria_academia == 0:

        ma "Você pode sempre usar a roupa que você ganhou aqui da academia. Ela já foi feita pra treinar."

        mc normal "Legal."

        ma "Só não esquece de lavar ela sempre que der, né? Porque..."

        mc zerado "..."

        ma "Haha. Não precisa fazer essa cara."

    scene maria_academia_esteira1 with Dissolve(1.0)

    pause

    if maria_academia == 0:

        ma "Vamos alternar trote e corrida por 30 minutos hoje."

        mc "Tá louca?!"

        ma "Você ganhou de mim correndo no meu máximo, não preciso pegar leve com você."

        mc "Mas-"

        ma "Eu sei que agora são coisas diferentes. Aqui não se trata de velocidade, mas resistência."

        ma "Mas pode confiar em mim que eu sei que você consegue."

        mc "O-ok..."

        "{b}Para ser bem sucedido na esteira com a [ma] e ganhar pontos de físico, você precisa aguentar o treino{/b}"

        "{b}Da mesma forma que as corridas no parque, tudo o que você precisa fazer é apertar o botão no canto inferior direito{/b}"

        "{b}Entretanto, ao invés de apertar o mais rápido que puder, você precisa manter o ritmo por um longo período de tempo{/b}"

        "{b}Se você correr rápido demais, o [mc] vai acabar com a cara no chão, literalmente{/b}"

        "{b}Encontrar o equilíbrio entre velocidade e conforto é a chave para se dar bem na esteira{/b}"

        "{b}Boa sorte!{/b}"

    elif maria_academia == 1:

        ma "Como você se saiu bem no primeiro treino, vou programar um roteiro mais puxado."

        ma "Você acha que aguenta?"

        mc "Sei não..."

        ma "Como assim não sabe? Você não tá treinando?"

        mc "Ah, tô só brincando. Claro que eu aguento."

        ma "Isso mesmo."

        if maria_namoro:

            ma "Você namora com uma dona de academia. Quero ver você dando seu melhor."

            mc "Pode deixar."

    elif maria_academia == 3:

        mc "[ma]... você levantou tudo isso aqui sozinha?"

        ma "A academia você diz?"

        mc "Isso."

        ma "Sim."

        mc "Como você conseguiu?"

        ma "Haha... parece impossível, né?"

        mc "Exatamente."

        ma "Não foi de uma hora pra outra. Desde a faculdade eu guardo dinheiro."

        ma "Eu queria muito ter minha própria academia e oferecer um espaço com um preço acessível pra quem quisesse."

        mc "Caraca... e você conseguiu."

        ma "Não foi assim fácil também. Eu trabalhei muitos anos como personal trainer e sempre fui juntando um pouco por mês."

        ma "Mesmo quando eu tava com meu noivo, eu tinha meu próprio dinheiro. Eu ajudava nas contas, claro, mas sempre mantendo aquele valor guardado."

        ma "Eu sabia que um dia eu ia conseguir. E quando eu achei esse espaço aqui eu fiz um empréstimo e comprei os equipamentos."

        ma "Daí o aluguel e outras despesas do lugar eu uso minhas reservas e também o dinheiro que vem dos membros. Ainda tá no começo, só que tá dando certo por enquanto."

        mc "Incrível mesmo. É realmente inspirador."

        ma "Valeu."

    ma "Vamos começar?"

    mc "Vamos."

    python:
        if renpy.android:
            mc_fisico = PythonSDLActivity.pegaFpontos()

        else:
            
            mc_fisico = 20

    if maria_academia == 0:

        $ menos_folego = 4
        $ esteira_tempo = 30
        $ fisico_recompensa = 10

    elif maria_academia == 1:

        $ menos_folego = 10
        $ esteira_tempo = 35

    elif maria_academia == 2:

        $ menos_folego = 15
        $ esteira_tempo = 35

    elif maria_academia == 3:

        $ menos_folego = 20
        $ esteira_tempo = 37

    elif maria_academia == 4:

        $ menos_folego = 25
        $ esteira_tempo = 40

    $ esteira_velo = 0.5
    $ folego = 150
    $ mc_folego = mc_fisico // 10
    $ treinando_sozinho = False

    show screen academia_esteira
    show screen esteira_tempo
    show screen esteira_reduz_folego
    call screen esteira_base

    pause

screen academia_esteira():
    tag academia

    modal True



    imagebutton auto "mapa/treino_maria_%s.png":
        xalign 0.955
        yalign 0.99
        xanchor 0.5
        action Jump("esteira_aumenta_folego")



    bar:
        bar_vertical True
        xalign 0.9
        yalign 0.224
        xsize 40
        ysize 250
        value folego
        range 300

    vbox:

        spacing 10
        xalign 0.1
        yalign 0.85

        text "Tempo"

        bar:
            xsize 350
            ysize 30
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=esteira_tempo)

screen esteira_reduz_folego():
    tag esteira_folego


    timer esteira_velo repeat True action Jump("esteira_reduz_folego")

screen esteira_tempo():
    tag esteira_tempo


    timer esteira_tempo action Jump("termina_esteira")

screen esteira_base():
    tag esteira_base


label esteira_aumenta_folego:

    $ folego += mc_folego

    if folego >= 300:

        jump termina_esteira

    pause

label esteira_reduz_folego:

    $ folego -= menos_folego

    if folego <= 0:

        jump termina_esteira

    pause

label termina_esteira:

    hide screen academia_esteira
    hide screen esteira_tempo
    hide screen esteira_reduz_folego
    hide screen esteira_base

    $ renpy.block_rollback()

    if folego <= 0 or folego >= 300:

        if treinando_sozinho:

            jump academia_treino_finalizar

        "Uou!"

        scene academia_mc_caido with vpunch

        pause

        mc "Argh!"

        ma "[mc]!"

        if maria_namoro:

            ma "Tá tudo legal, amor? Você tá bem?"
        else:


            ma "Tudo bem?!"

        if folego <= 0:

            mc "Ai... sim... acho que não aguentei a velocidade."
        else:


            mc "Sim... acho que corri rápido demais..."

        ma "Vem aqui."

        scene cidade academia2 with Dissolve(1.0)

        mc "Ai."

        show maria a_triste with dissolve

        ma "Desculpa. Acho que peguei pesado demais com você."

        mc charmoso "Relaxa. Eu vou pegar o jeito e treinar mais, ok?"

        ma "Tá."

        mc "Eu não sou um fraco que vai desistir assim. Eu ganhei ou não de você na corrida?"

        ma "Ganhou..."

        show maria a_feliz with dissolve

        ma "É verdade. Você vai se sair bem. Eu acredito em você."

        mc charmoso "Pode ter certeza."

        "Hmmm... não quero que a [ma] pegue leve comigo. Dá pra ver que ela dá muito valor pro meu desempenho."

        "Talvez eu devesse vir aqui na parte da tarde que ela não tá e treinar no meu ritmo até conseguir acompanhar ela."

        "Na parte da tarde ela não vai tá, então dá pra eu praticar bastante sem ela me achar um bundão."
    else:


        python:
            if renpy.android:
                PythonSDLActivity.addFCustomPontos(fisico_recompensa)

        $ renpy.block_rollback()

        if treinando_sozinho:

            jump academia_treino_finalizar

        if maria_academia == 2:

            $ maria_academia = 3

        ma "Você tá aguentando bem, viu."

        mc "Isso aqui não é nada."

        if maria_namoro:

            ma "Assim que se fala. Meu namorado não pode ser bundão."

            mc "Haha... Pode ter certeza que não é."
        else:


            ma "Gostei de ver."

        ma "Vamos aumentar o treino até o limite."

        "{i}gulp{/i}"

        mc "Ok!"

        "{i}Pii pii pii{/i}"

        ma "Deu o tempo."

        "Ufa..."

        play sound "extra/carta.mp3"

        "{b}O físico do [mc] melhorou [fisico_recompensa] pontos{/b}"

        scene cidade academia2 with Dissolve(1.0)

    if maria_academia == 0:

        $ maria_academia = 1

    elif maria_academia == 1:

        $ maria_academia = 2

    elif maria_academia == 3:

        $ maria_academia = 4

    show maria a_satisfeita with dissolve

    ma "Ufa. Hoje foi um bom treino. Eu gosto muito de treinar com você, [mc]."

    mc charmoso "Eu também."

    ma "Já tá ficando tarde. Vejo você logo?"

    if maria_namoro:

        mc charmoso "Não posso deixar minha namorada sozinha aqui."

        ma "Seu fofo."

    ma "Te espero."

    hide maria with dissolve

    "Cristo... essa mina ainda vai me matar."

    scene black with dissolve

    $ tempo = 2

    jump cidade_academia

label maria_academia_evento:

    ma "!"

    show maria a_feliz with dissolve

    if maria_namoro:

        ma "Oi, lindo. Que bom que você veio! Pronto pra virar membro?"
    else:


        ma "Oi, [mc]. Pronto pra fazer parte da minha academia?"

    "Uou! Ela tá muito gata!"

    if maria_namoro:

        "Sorte a minha namorar uma delícia dessas..."

    ma "[mc]?"

    mc surpreso "O-pa. Com certeza."



    python:
        if renpy.android:
            academia = PythonSDLActivity.pegaAcademia()

    if academia:

        jump academia_comprada

    if not academia_maria_evento:

        ma "E aí? O que achou?"

        mc normal "Incrível. O lugar é realmente muito bacana."

        ma "Que bom que você gostou. Ainda tá no começo. As primeiras pessoas começaram a entrar nela esses dias."

        mc "Então eu vou ser um dos primeiros. Massa."

        if maria_namoro:

            ma "Ainda mais agora que a gente tá junto, né? Tem que fazer parte."

            mc envergonhado "Haha... verdade."

        mc normal "E como funciona? Quanto é a mensalidade?"

    label maria_academia_comprar:

        ma "Você precisa pagar um único valor de C$ 250 e a academia estará aberta pra você pra sempre."

        if not academia_maria_evento:

            $ academia_maria_evento = True

            mc surpreso "Nunca vou precisar pagar de novo?!"

            ma "Não. Só uma vez."

            menu:
                "Parece uma boa proposta.":


                    mc charmoso "Uou. Pagar só uma vez e ter acesso pra sempre. Parece bom demais pra ser verdade."

                    ma "Haha... é bom mesmo, mas é verdade."

                "Você vai cobrar até do seu namorado?!" if maria_namoro:

                    mc envergonhado "Sério mesmo que você vai cobrar até do namorado?"

                    ma "Amigos, amigos, negócios à parte, meu querido."

                    ma "Falando sério, seria legal se você pudesse contribuir, porque tá começando agora e toda ajuda... ajuda."

                    mc normal "Eu tava brincando. Claro que eu vou pagar. Não ia me sentir bem me aproveitando da nossa relação."

                    ma "Obrigada, [mc]. Você é um fofo."
                "Mas todo mundo cobra por mês. Você não vai falir assim?":


                    mc desconfiado "Mas como assim só uma vez pra sempre? Toda academia cobra por mês pra ganhar mais. Você não vai falir?"

                    ma "Na verdade, isso é baseado em um estudo. Aparentemente a maioria das pessoas começam e abandonam a academia em poucos meses."

                    ma "Fazendo assim, eu recebo o que eu ganharia em cerca de 6 meses, mas em média cada pessoa usará nem 3."

                    ma "Claro que algumas pessoas usarão mais do que seis meses, mas é uma pequena parcela."

                    mc desconfiado "Caraca... que interessante..."

                    ma "O que acontece é que a maioria das academias tenta colocar a pessoa no cartão de crédito e ela fica pagando mesmo sem usar."

                    ma "Eu acho isso muita sacanagem. E mesmo que seja parte culpa da pessoa que não cancela, a academia também poderia ser mais ética."

                    mc desculpa "Você tem razão... e não é só academia que faz isso..."

                    mc zerado "Nem sei quantas vezes paguei coisa que nem usava mais na internet..."

                    ma "Bem assim."

        ma "E aí? Posso iniciar seu cadastro então?"

    $ renpy.choice_for_skipping()

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()

    "Hmmm... C$ 250..."

    if cash >= 250:

        "Um único pagamento de C$ 250 pra ter entrada vitalícia em uma academia é realmente pouco."

        "Bom... eu tenho dinheiro pra comprar. E realmente quero poder me aproximar da [ma] além de dar uma tunada."

        menu:

            "Se tornar membro da academia por {b}C$ 250{/b}" if cash >= 250:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraAcademia()
                        
                        academia = PythonSDLActivity.pegaAcademia()
                        
                        renpy.choice_for_skipping()

                mc charmoso "Tá aqui."

                ma "Perfeito! Muito obrigada!"

                ma "Só um instantinho..."

                hide maria with dissolve

                "..."

                show maria a_feliz with dissolve

                ma "Agora só assinar aqui."

                mc charmoso "Pronto."

                ma "Tudo certo!"
            "Deixar para outra hora":


                jump academia_comprada_nao
    else:


        "Um único pagamento de C$ 250 pra ter entrada vitalícia em uma academia é realmente pouco."

        "Só que nem isso eu tenho comigo aqui. Aaahhhh!"

        "Vou ter que dar um jeito de trabalhar e conseguir essa grana antes."

        show black with Dissolve(1.0)

        p lecionando "Ixi. O [mc] tá pobre que só ele..."

        p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

        p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

        p "Você ganhará acesso à academia, poderá continuar a história da [ma] e ainda contribui com o desenvolvimento de CH."

        p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

        menu:
            "Sim. Tô com uma graninha sobrando aqui.":


                p rindo "Que bom!"

                call comprar_cash from _call_comprar_cash_2

                hide black with dissolve

                "Pensando bem... acho que eu tenho um dinheiro guardado aqui."

                mc normal "Como é mesmo?"

                jump maria_academia_comprar
            "Não. Tô pobre igual a ele...":


                p rindo "Não esquente."

                p "Trabalhe sempre que possível no bar e vá juntando seus Celebrity Reais. Logo logo você já vai estar com grana suficiente."

                p "Demora, mas vale a pena!"

                hide black with dissolve

                jump academia_comprada_nao

    label academia_comprada:

        ma "Tô vendo aqui e sua papelada tá ok. O pagamento também. Já tá tudo nos conformes pra você começar a usar."

        ma "Bem vindo à academia, [mc]!"

        mc feliz "Valeu!"

        ma "A gente não abre à noite, mas você pode usar sempre que quiser, na parte da manhã ou da tarde."

        ma "Nem precisa parar na recepção nem nada. Só vir direto pra cá. Como são poucos membros, o pessoal se conhece."

        mc normal "Beleza. Valeu."

        ma "Você pode treinar sozinho durante a tarde, mas eu sempre tô aqui na parte da manhã."

        if maria_namoro:

            ma "Se você quiser treinar com sua namorada gostosa pra cacete, só vir de manhã e a gente malha juntos."

            mc safado "Com certeza..."
        else:


            ma "Se você quiser treinar comigo, eu sempre tô aqui na parte da manhã, tá?"

            mc normal "Claro."

        if tempo == 2:

            ma "Agora já tá meio tarde pra mim, tô saindo fora. Mas pode treinar sozinho e amanhã logo cedo já tô aqui."
        else:


            ma "Inclusive já vou começar o treino logo logo. Se quiser começar."

        ma "Ah! Como brinde pela sua filiação, a gente dá uma roupa exclusiva pra treino. Toma."

        mc surpreso "Uou!"

        ma "Legal, né?"

        mc normal "Então vou me trocar aqui caso eu já vá começar."

        ma "Isso. Venha sempre com ela. Assim não perde tempo e dinheiro com roupa."

        mc charmoso "Bacana."

        ma "Então é isso. Tô realmente ansiosa pros nosso treinos."

        mc "Eu também. Assim que eu for começar te chamo."

        ma "Demais. Beijo."

        mc "Beijo."

        hide maria with dissolve

        "Uma academia... quem diria que eu pensar nisso..."

        mc zerado "Parece que tudo o que acontece comigo nessa cidade tem a ver com mulher..."

        $ area = "academia"
        $ mapa = "academia1"

        scene academia academia1 with Dissolve(1.0)

        call pos_tela from _call_pos_tela

        pause

    label academia_comprada_nao:

        mc charmoso "Eu não tô com a grana aqui agora. Mas pode ir iniciando a papelada que eu volto esses dias e a gente finaliza."

        ma "Não tem pressa. Só de você ter interesse, já é incrível pra mim."

        mc "Claro que eu tenho, tá louca? Não vejo a hora de começar."

        mc normal "Agora eu vou indo nessa. Parabéns de novo pela academia."

        ma "Valeu, [mc]. Você é muito fofo mesmo."

        if maria_namoro:

            mc charmoso "Tchau, linda."

            ma "Tchau, gato."
        else:


            mc normal "Tchau!"

        jump cidade4

label maria_treino:

    "Opa! Tô vendo a [ma] ali. Ela sempre chega antes..."

    mc charmoso "Bom dia."

    show maria falando with dissolve

    ma "Bom dia, [mc]. Pronto pro treino de hoje?"

    mc "Com certeza."

    ma "Vamos lá pro parque então."

    ma "Só seguir!"

    jump maria_menu

label maria_menu:

    scene mc corrida_preparacao_maria with Dissolve(2.0)

    mc "Ufa... chegamos."

    ma "Sinto que você tá cada vez melhor."

    label maria_menu_escolha:

        ma "O que vamos fazer hoje?"

    menu:
        "Apostar corrida com a [ma]":


            $ proibido_salvar = True
            $ show_quick_menu = False

            jump maria_preparacao
        "Treinar para melhorar minha aptidão":


            jump maria_treinamento
        "Pode me explicar como o treino funciona?":


            mc "Você pode me explicar de novo como o treino funciona?"

            ma "Claro. É importante entender a teoria."

            ma "Cada manhã que você vier treinar, podemos fazer duas coisas."

            ma "{b}Treinar para melhorar sua aptidão{/b} ou a gente pode {b}apostar corrida{/b}."

            ma "Quando você treina, você tem uma chance de melhorar seu {b}Físico{/b}."

            ma "Sua musculatura precisa de descanso, ou às vezes você estará cansado demais."

            ma "Então nem sempre você vai melhorar. O importante é você não perder o foco e continuar treinando todas as manhãs."

            ma "Quanto mais você melhorar seu {b}físico{/b}, mais fácil será me vencer em uma corrida."

            if maria_relacao:

                ma "Conforme você for me vencendo, mais vou ver que você tem capacidade, e talvez eu até deixe você me alongar..."

                ma "Eu sei que você iria adorar..."

                mc "Com certeza."

            ma "Quando você me desafiar, você pode escolher se você quer que eu corra de forma leve, moderada ou com toda minha força."

            ma "Vamos ver se você consegue me derrotar quando eu estiver correndo em toda minha velocidade."

            ma "Entendeu?"

            mc "Sim, valeu."

            jump maria_menu_escolha

label maria_treinamento:

    ma "Certo. Então hoje você vai querer treinar."

    mc "Isso aí."

    $ proibido_salvar = True
    $ show_quick_menu = False

    call checa_logado from _call_checa_logado_4

    ma "Perfeito. Você precisa treinar bastante se quiser me vencer."

    call anuncio from _call_anuncio_5

    ma "Não esquece que a cada treino eu vou adicionar 300 metros a mais."

    mc "Ok..."

    mc "Podemos ir?"

    $ renpy.choice_for_skipping()

    call checa_tempo from _call_checa_tempo_5

    python:
        if renpy.android:
            mttempo = PythonSDLActivity.checkMTtempoNext()

    $ renpy.pause(delay=1, hard=True)

    if not mttempo:

        $ proibido_salvar = False
        $ show_quick_menu = True

        ma "A questão é que você ainda não deu tempo dos seus músculos se recuperarem."

        ma "Você precisa dar uma descansada e outro dia a gente treina, ok?"

        show black with Dissolve(1.0)

        "{b}O [mc] pode treinar com a [ma] uma vez a cada 1 hora do mundo real{/b}"

        "{b}Use o app Relógio no celular do [mc] para ver quando o próximo treino estará disponível{/b}"

        python:
            if renpy.android:
                persistent.coins = PythonSDLActivity.pegaMoedas(0)

        "{b}Ou você pode liberar o próximo treino agora mesmo usando Celebrity Coins{/b}"

        if persistent.coins >= 100:

            "{b}Liberar o próximo treino usará 100 Celebrity Coins{/b}"

            menu:
                "Usar {b}100 Celebrity Coins{/b} e liberar o próximo treino":


                    python:
                        if renpy.android:
                            PythonSDLActivity.avancaMTTempo()

                    $ renpy.block_rollback()

                    play sound "extra/carta.mp3"

                    "{b}Você usou 100 Celebrity Coins para liberar o próximo treino{/b}"

                    "{b}[mc] será levado ao começo do treino e você poderá continuar seu treinamento com a [ma]{/b}"

                    $ renpy.block_rollback()

                    hide black with Dissolve(1.0)

                    jump maria_treinamento
                "Agora não. Vou esperar o tempo.":


                    "{b}Você escolheu não liberar o próximo treinamento{/b}"

                    jump maria_treinamento_sair
        else:


            "{b}Você precisa de ao menos 100 Celebrity Coins para liberar o treino{/b}"

            "{b}Você pode adquirir Celebrity Coins vendo vídeos ou comprando em nossa Loja. Acesse o Menu para saber mais{/b}"

            label maria_treinamento_sair:

                hide black with Dissolve(1.0)

                ma "Então amanhã você volta e continuamos o treinamento, ok?"

                mc "Tudo bem. Se você tá dizendo..."

                jump maria_corrida_finalizar
    else:


        python:
            if renpy.android:
                PythonSDLActivity.setMTtempoNext()

            renpy.pause(delay=1, hard=True)

        if treino_sucesso:

            python:
                if renpy.android:
                    PythonSDLActivity.addFpontos()

                renpy.block_rollback()

        ma "Podemos."

        ma "Vou começar com o alongamento."

        jump maria_treino_alongamento

label maria_treino_alongamento:

    $ proibido_salvar = True
    $ show_quick_menu = False

    mc "Ok."

    if maria_relacao:

        ma "Eu sei que no fundo é sua parte preferida do treino."

        mc "Falo nada..."
    else:


        ma "Presta atenção pra você ir aprendendo. Alongar é muito importante."

        mc "Ok."

    if maria_lvl2:

        if maria_treinamento_lv2 == 0:

            ma "Agora só resta você me vencer contra todo meu potencial, acredita?"

            mc "Acredito nada..."

            ma "Rsrs... você conquistou isso. Parabéns."

            if maria_relacao:

                ma "Depois de todo seu esforço, eu tô te olhando com outros olhos, [mc]."

                mc "Você sabe que eu também te vejo assim, né?"

                ma "Eu pensei nisso..."

                mc "..."

            if maria_treinamento_lv1 == 3:

                ma "Mas chega de papo! Vamos alongar!"

                scene maria lv2_1 with Dissolve(2.0)

                $ renpy.pause(delay=3, hard=True)

                mc "Espero que você esteja pronta pro alongamento especial."

                ma "Sim. Faz logo..."

                scene maria lv2_2 with Dissolve(2.0)

                $ renpy.pause(delay=3, hard=True)

                scene maria lv2_3 with Dissolve(2.0)

                $ renpy.pause(delay=3, hard=True)

                "Depois da minha vitória contra ela correndo, tenho que aproveitar e levar as coisas além."

                "Ela também disse que tá me vendo com outros olhos."

                "Se eu não fizer algo agora, vou parecer um banana."

                ma "Vou levantar."

                mc "Ok..."

                scene maria lv3_1 with Dissolve(2.0)

                $ renpy.pause(delay=3, hard=True)

                pause

                ma "Hmmm... você não tá muito perto, não?"

                mc "Algum problema?"

                ma "Não... mas... o que é isso que eu tô sentindo na minha bunda?"

                mc "É como você me deixa..."

                ma "Ai, safado... quer me deixar mais molhada ainda?"

                mc "Quero."

                ma "..."

            $ maria_treinamento_lv2 = 1

        elif maria_treinamento_lv2 == 1 and maria_treinamento_lv1 == 3:

            ma "Você tá cada vez mais saidinho nos nossos treinamentos..."

            mc "Só porque você gosta."

            ma "Vai usar minha fraqueza contra mim, né?"

            mc "Eu não..."

            ma "Foda-se. Vem logo aqui e pega em mim."

            mc "Com todo o prazer."

            scene maria lv2_3 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Ai... eu nem tenho alongado direito mais."

            mc "Verdade, a gente tá indo direto pra parte boa..."

            ma "..."

            scene maria lv3_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Lá vem você me pegar de costas de novo..."

            mc "Pegar você? Você não viu nada ainda."

            "Tá na hora de eu acabar com ela de uma vez."

            ma "Não sei se-"

            scene maria lv3_2 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Ai... hmmm... que é isso, [mc]?"

            mc "Nada..."

            ma "Você tá pegando na minha... hmmmm... ah..."

            mc "Só aproveita."

            ma "Ai... ah..."

            ma "Mas alguém pode-"

            mc "Já falei que não tem ninguém."

            ma "Chega. Tá bom."

            mc "Certeza que vo-"

            ma "Tá bom!"

            mc "Ok."

            scene mc corrida_preparacao_maria with Dissolve(1.0)

            mc "Desculpa. Não queria forçar..."

            ma "Tudo bem. Eu adorei. Só não quero que ninguém veja."

            ma "Você é muito bom com a mão..."

            mc "Valeu."

            ma "Mas agora a gente tem que correr."

            mc "Vamos."

            $ maria_treinamento_lv2 = 2

        elif maria_treinamento_lv2 == 2:

            ma "O que será que você vai aprontar hoje? Já fico ansiosa antes do treino."

            mc "Hehe... fico feliz que você esteja gostando."

            ma "Todo mundo precisa de um pouco de diversão."

            ma "Sua vez vai chegar também."

            mc "Eu tô me divertindo bastante, já. Pode acreditar."

            ma "Safado..."

            ma "Agora vem aqui."

            scene maria lv2_2 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            mc "Um pouco de cócegas pra melhorar o clima."

            ma "Só tá me deixando mais excitada."

            mc "Agora vem aqui."

            ma "Tá... mas vê se não tem ninguém..."

            "Hoje eu vou preparar ela antes. Tá na hora de eu provar essa mulher."

            mc "Só vem aqui."

            scene maria lv3_3 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            pause

            ma "Hmmm..."

            ma "Você quer me deixar louca de tesão..."

            ma "Não aguento mais. Pega em mim logo."

            mc "Com todo o prazer."

            scene maria lv3_2 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Ai, [mc]... você aperta os lugares certos..."

            mc "..."

            ma "Ai.. ai!"

            ma "{i}puf puf{/i}"

            ma "Hmmm...."

            ma "Ai, vai! Não para!"

            ma "AAH!"

            ma "{i}puf puf{/i}"

            ma "Preciso sentar..."

            scene track um with Dissolve(1.0)

            ma "Ufa... minhas pernas..."

            mc "Deixa eu sentar com você."

            scene mc maria_sentados with Dissolve(1.0)

            ma "O que foi isso, [mc]? Você acabou comigo..."

            mc "Foi bom?"

            ma "Claro... Eu amei. Você realmente sabe o que tá fazendo."

            mc "Que bom que você gostou."

            ma "Eu adorei... nem sei se quero correr mais hoje..."

            mc "Temos que correr, tá doida?!"

            ma "Você só quer judiar de mim agora."

            mc "Pode levantando. Vamos nessa."

            ma "Ok..."

            $ maria_treinamento_lv2 = 3

        elif maria_treinamento_lv2 == 3:

            ma "Já fizemos de tudo nesse alongamento. Nem sei o que esperar dessa sua cabeça..."

            mc "Hoje..."

            menu:
                "Ver a [ma] se alongando sozinha":


                    ma "Na verdade, hoje eu quero me alongar sozinha. Você só olha."

                    mc "Que pena..."

                    scene maria alongamento with Dissolve(1.0)

                    $ renpy.pause(delay=3, hard=True)

                    scene maria alongamento_dois with Dissolve(1.0)

                    $ renpy.pause(delay=3, hard=True)

                    scene maria alongamento_tres with Dissolve(1.0)

                    $ renpy.pause(delay=3, hard=True)

                    ma "Terminei."
                "Ajudar a [ma] a se alongar":


                    ma "Você pode me ajudar no alongamento? Daquele jeito..."

                    mc "Com certeza."

                    scene maria lv2_1 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    mc "Hora do alongamento especial."

                    scene maria lv2_2 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    scene maria lv2_3 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    ma "Tá bom demais..."
                "Ir direto para a pegação":


                    mc "Hoje quero fazer outra coisa."

                    ma "Também quero."

                    scene maria lv3_1 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    ma "Vem."

                    scene maria lv3_3 with Dissolve(2.0)

                    ma "Isso. Me beija."

                    $ renpy.pause(delay=3, hard=True)

                    scene maria lv3_2 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    ma "Assim!"

                    ma "AAH!"

                    "..."

                    mc "Vamos sentar?"

                    ma "Obrigada."

                    scene mc maria_sentados with Dissolve(1.0)

                    "..."

                    ma "Tô legal. Vamos?"

                    mc "Bora."

        if maria_treinamento_lv1 < 3:

            ma "Me ajuda aqui?"

            mc "Claro."

            scene maria lv2_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Pronto."

        "..."

    elif maria_lvl1:

        if maria_treinamento_lv1 == 0:

            scene maria alongamento with Dissolve(1.0)

            $ renpy.pause(delay=3, hard=True)

            scene maria alongamento_dois with Dissolve(1.0)

            $ renpy.pause(delay=3, hard=True)

            scene maria alongamento_tres with Dissolve(1.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Seu progresso está sendo incrível. Você tá pronto pra me ajudar no meu alongamento."

            if maria_relacao:

                ma "Mas sem pensar besteira, hein?"

                mc safado "Claro que não..."

                "Nem acredito que vou pegar nesse corpo..."

            scene maria lv2_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Isso. Levanta bem minhas pernas."

            ma "Assim... pressiona bem."

            if maria_relacao:

                ma "Tá gostando do meu corpo?"

                mc "Você é incrível."

                ma "Obrigada. Continua pegando assim..."

                ma "Ai... isso, aperta com força..."

                "Eu sei que é só um alongamento, mas isso tá me deixando meio louco..."

            ma "Pronto. Vou levantar."

            $ maria_treinamento_lv1 = 1

        elif maria_treinamento_lv1 == 1:

            ma "Você pode me ajudar a me longar hoje também?"

            mc "Não precisa nem pedir."

            scene maria lv2_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Assim."

            "..."

            if maria_relacao:

                "Eu decidi que eu quero algo mais com a [ma]. A gente tá se aproximando tanto."

                "Talvez agora seja a hora certa pra mostrar pra ela minhas intenções."

                menu:
                    "Fazer cócegas nela":


                        mc "Mas hoje o alongamento vai ter uma etapa a mais."

                        ma "Como assim?"

                        mc "Você já vai ver!"

                        scene maria lv2_2 with Dissolve(2.0)

                        $ renpy.pause(delay=3, hard=True)

                        pause

                        mc "Toma aqui!"

                        ma "Hahaha! [mc]!"

                        ma "Que você tá fazendo?!"

                        mc "Tô aplicando meu alongamento secreto."

                        ma "Hmmm... você só tá pegando nas minhas coxas, safado."

                        mc "Eu? Imagina!"

                        ma "Mas pode apertar mais. Tá gostoso..."

                        mc "..."

                        ma "Ai... tá bom, [mc]. Vamos correr."

                        mc "Que pena..."

                        $ maria_treinamento_lv1 = 2
                    "Melhor não":


                        "Melhor não fazer nada. Não quero parecer um esquisito."

        elif maria_treinamento_lv1 == 2:

            ma "Eu adorei nosso alongamento ontem."

            mc "Eu também. Pode deixar que hoje tem mais."

            ma "Já tô ansiosa..."

            mc "Pode deitar."

            scene maria lv2_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            mc "Hora do alongamento especial."

            scene maria lv2_2 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            ma "Hmmm..."

            "Ela tá gostando dessa pegação toda. Hoje vou arriscar um pouco mais."

            "Ou será que eu estaria indo longe demais?"

            menu:
                "Melhor não arriscar.":


                    "Melhor não fazer nada. Não quero ser um tarado."
                "Tentar excitar ela durante o alongamento":


                    "Tô pronto pra deixar ela molhadinha só alongando..."

                    mc "Hoje vou fazer um movimento novo, hein? Tá preparada?"

                    ma "Cuidado comigo, doutor..."

                    mc "..."

                    scene maria lv2_3 with Dissolve(2.0)

                    $ renpy.pause(delay=3, hard=True)

                    pause

                    ma "Ai, [mc]..."

                    mc "Vamos alongar esta região aqui..."

                    ma "Aaahh... alguém pode ver a gente..."

                    mc "Só tem a gente aqui essa hora todo dia. Relaxe..."

                    ma "Ai, safado... Hmmm..."

                    mc "Deixa olhar com calma pra ver se tá alongado direitinho."

                    ma "O meio das minhas pernas tá bem alongado, doutor?"

                    mc "Ainda não... deixa eu alongar pra você."

                    ma "Isso..."

                    ma "Agora acho que tá alongado, doutor."

                    mc "Verdade. Agora tá tudo certo."

                    mc "Deixa eu te ajudar a levantar."

                    ma "{size=15}Você me deixou louca, seu safado...{/size}"

                    mc "Era a intenção."

                    $ maria_treinamento_lv1 = 3

        elif maria_treinamento_lv1 == 3:

            ma "Vamos repetir a rotina?"

            mc "Vai querer o alongamento especial?"

            ma "Com certeza..."

            scene maria lv2_1 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            mc "Hora da mágica."

            scene maria lv2_2 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            scene maria lv2_3 with Dissolve(2.0)

            $ renpy.pause(delay=3, hard=True)

            mc "Prontinho."

            ma "Muito obrigada."

        "..."
    else:


        ma "Se você conseguir me vencer fazendo cooper, eu deixo você me ajudar a alongar, certo?"

        ma "Por enquanto você só olha."

        mc "Ok..."

        scene maria alongamento with Dissolve(1.0)

        $ renpy.pause(delay=3, hard=True)

        scene maria alongamento_dois with Dissolve(1.0)

        $ renpy.pause(delay=3, hard=True)

        scene maria alongamento_tres with Dissolve(1.0)

        $ renpy.pause(delay=3, hard=True)

    scene mc maria_preparacao with Dissolve(1.0)

    ma "Estou pronta. Vamos correr?"

    mc "Demorou."

    "..."

    scene maria correndo_mc with Dissolve(1.0)

    mc "{i}puf puf{/i}"

    ma "E aí? Acha que hoje vai dar pra ir até o fim?"

    if treino_sucesso:

        mc "Acredito que sim! Bora lá!"

        "..."

        scene mc corrida_preparacao_maria with Dissolve(1.0)

        mc "Nem acredito que aguentei."

        ma "Parabéns! Você aguentou, mesmo eu extendo nossa rotina por mais 300 metros."

        ma "Da próxima vez vou adicionar mais 300 metros."

        mc "Não faça isso..."

        ma "Quando você ganhar de mim na corrida, você vai agradecer."

        mc "Ok..."

        ma "Vamos nessa?"

        mc "Vamos."

        show black with Dissolve(1.0)

        play sound "extra/carta.mp3"

        "{b}[mc] aumentou sua aptidão física em 1 ponto e agora pode correr mais rápido{/b}"

        jump maria_corrida_finalizar
    else:


        mc "Sei não... já tô quase parando..."

        ma "Mas ainda faltam 600 metros."

        mc "Aahhh..."

        scene mc corrida_cansado with Dissolve(1.0)

        mc "Hoje eu não rendi. Tô quase morrendo."

        ma "Isso é normal acontecer."

        ma "Descanse um pouco e tentamos em um outro dia."

        mc "Beleza. Vamos voltar?"

        ma "Certeza."

        jump maria_corrida_finalizar

label maria_preparacao:

    ma "Então você vai realmente querer apostar uma corrida?"

    mc "Com certeza."

    ma "Você vai querer uma colher de chá ou velocidade total?"

    $ maria_tempo = 2.0
    $ maria_esquerda = 1
    $ mc_esquerda = 0
    $ maria_point = 0.05
    $ mc_point = 0.05

    python:
        if renpy.android:
            mc_fisico = PythonSDLActivity.pegaFpontos()

    $ mc_velocidade = mc_fisico / float(1000)

    menu:
        "Corrida contra a [ma] fazendo cooper":


            $ maria_velocidade = 0.05
            $ maria_lvl = 1

            ma "Perfeito. Até você pegar o jeito, ir devagar é o melhor."

        "Corrida contra a [ma] correndo" if maria_lvl1:

            $ maria_velocidade = 0.12
            $ maria_lvl = 2

            ma "Será que você já tá pronto pra isso? Eu vou correr de verdade, hein?"

            mc "Estou pronto."

            ma "Ok."

        "Corrida contra a [ma] em velocidade máxima" if maria_lvl2:

            $ maria_velocidade = 0.30
            $ maria_lvl = 3

            ma "Você tá louco? Eu vou dar o melhor de mim!"

            mc "Eu sei, e eu quero justamente isso."

            ma "Eu acho loucura, mas se é o que você quer..."

label maria_minigame:

    $ proibido_salvar = True
    $ show_quick_menu = False

    $ renpy.choice_for_skipping()

    $ renpy.block_rollback()

    scene mc maria_preparacao with Dissolve(1.0)

    ma "Tudo pronto?"

    mc "Quando você quiser."

    ma "{cps=6}{i}3... 2... 1...{/i}{/cps}{w=1.0}{nw}"

    ma "Vai!"

    show screen maria_corrida

    scene black

    $ renpy.pause()

    "..."

screen maria_corrida():
    tag maria_corrida

    zorder 100
    modal True
    predict False

    add "images/pista corrida.jpg" at cidade_trans

    if maria_esquerda <= 1:

        add "images/maria correndo_top_esquerda.png":

            yalign 0.5
            at maria_anda_facil

    else:

        add "images/maria correndo_top_direita.png":

            yalign 0.5
            at maria_anda_facil

    if mc_esquerda <= 5:

        add "images/mc correndo_top_esquerda.png":
            xalign mc_point
            yalign 0.65
            at cidade_trans

    else:

        add "images/mc correndo_top_direita.png":
            xalign mc_point
            yalign 0.65
            at cidade_trans

    imagebutton auto "extra/botao_correr_%s.png":
        xalign 0.05
        yalign 0.95
        at cidade_trans
        action Call("anda_esquerda")







    timer maria_tempo repeat True action Call("maria_anda")

label anda_esquerda:

    $ mc_point += mc_velocidade

    if mc_esquerda <= 5:

        $ mc_esquerda += 1
    else:


        $ mc_esquerda += 1

        if mc_esquerda >= 10:

            $ mc_esquerda = 0

    if mc_point >= 0.95:

        jump maria_corrida_resultado

    "..."

label maria_anda:

    $ maria_point += maria_velocidade

    if maria_esquerda <= 1:

        $ maria_esquerda += 1
    else:


        $ maria_esquerda += 1

        if maria_esquerda >= 2:

            $ maria_esquerda = 1

    if maria_point >= 0.95:

        jump maria_corrida_resultado

    "..."

label maria_corrida_resultado:

    hide screen maria_corrida

    $ renpy.block_rollback()

    $ proibido_salvar = False
    $ show_quick_menu = True

    scene black with Dissolve(1.0)

    "..."

    if mc_point >= maria_point:

        jump maria_corrida_mc_ganhou
    else:


        jump maria_corrida_maria_ganhou

label maria_corrida_maria_ganhou:

    "..."

    ma "Ganhei!"

    if maria_evento == 4:

        jump maria_primeira_corrida

    if maria_lvl == 1:

        scene maria lvl1_ganhou with Dissolve(1.0)

        pause

        ma "Força, [mc]..."

        mc "{i}puf puf{/i}"

        "Impossível que eu não consigo ganhar dela nem com ela só no cooper..."

        ma "Você ainda tá no começo do seu treinamento. Não desanime."

        ma "A cada novo treino bem sucedido, vai ser mais fácil de você vencer."

        ma "Treine mais alguns dias e me desafie de novo!"

    elif maria_lvl == 2:

        scene maria lvl2_ganhou with Dissolve(1.0)

        pause

        ma "Muito fácil, [mc]."

        mc "{i}puf puf{/i}"

        ma "Ainda tem chão pra você. Mas eu já tô correndo a metade do que eu posso."

        ma "Tenho que admitir que você já superou minhas expectativas. Não desista e você vai melhorar. "

        ma "Se bem que ganhar de mim, acho que vai ser impossível."

    elif maria_lvl == 3:

        scene maria lvl3_ganhou with Dissolve(1.0)

        pause

        mc "AAARGHH!"

        mc "Que canseira!"

        ma "{i}puf puf{/i}"

        ma "Hah! Não é hoje que o aluno supera a mestre!"

        ma "Mas eu corri o máximo que eu posso, [mc]."

        ma "Você tá quase virando um oponente à minha altura. Não consigo acreditar nisso..."

        ma "Seu potencial é incrível! Eu sinto que com mais um pouco de treino você pode correr até mais do que eu!"

    ma "Essa corrida me cansou também. Vamos voltar?"

    mc "{i}puf puf{/i}"

    mc "Vamos..."

    "Na próxima eu pego ela. Não vou desistir até vencer com a [ma] dando o máximo!"

    jump maria_corrida_finalizar

label maria_corrida_mc_ganhou:

    $ renpy.block_rollback()

    "..."

    mc feliz "Venci!"

    scene mc ganhando_normal with Dissolve(2.0)

    pause

    if maria_lvl == 1:

        if not maria_lvl1:

            mc "Eu sei que você tava só trotando, mas... mas... mesmo assim!"

            ma "Você foi incrível, [mc]! Parabéns!"

            ma "Uns dias atrás você não chegava nem perto! Olha agora!"

            mc "Hehe... obrigado."

            scene mc conversando_maria with Dissolve(2.0)

            pause

            mc "Mas eu ainda tô meio cansado..."

            ma "Claro que tá. Você se esforçou bastante."

            if maria_relacao:

                ma "Depois de todo esse tempo com você me secando enquanto eu me alongo e essa sua vitória..."

                ma "Acho que vou deixar você me ajudar nos alongamentos."

                ma "Você quer?"

                menu:
                    "Sim. Sem dúvidas.":


                        mc "Sim. Sem dúvidas. Podemos começar agora."
                    "Claro que eu quero.":


                        mc "Claro que eu quero. Bora lá!"
                    "Com certeza!":


                        mc "Com certeza! Pode se ajeitar agora mesmo."

                ma "Calma rsrs..."

                ma "Na próxima vez que a gente treinar então eu deixo você me ajudar, ok?"

                mc "Combinado."

            mc "[ma]... Você realmente é bem ligada nesse lance de malhação. Isso é só um hobby?"

            ma "Na verdade eu trabalho com preparação física. Eu sou formada em Educação Física."

            mc "Sério?!"

            mc "Quer saber, vamos sentar aqui?"

            ma "Aqui no meio?"

            mc "Não sei se tenho força pra ir pra outro lugar."

            ma "Rsrs... acho que você mereceu."

            scene mc maria_sentados with Dissolve(2.0)

            mc "Então você é dessa área mesmo."

            ma "Sim. Eu trabalho como personal trainer de algumas pessoas e este ano eu abri uma academia."

            mc "Uou! Uma empreendedora."

            ma "Rsrs... micro empreendedora. É algo pequeno."

            mc "Assim mesmo, meus parabéns."

            ma "Obrigada. Eu sempre gostei de exercícios e malhação desde jovem. Sou feliz de poder trabalhar com isso hoje."

            mc "É bem legal isso. Trabalhar com aquilo que você ama."

            mc "Acho que é por isso que você tem essa aura de mulher bem resolvida."

            ma "Não exagere, [mc]. Mas obrigada."

            mc "..."

            ma "Acho que conversamos bastante. Olha a hora! Dessa vez ficamos a manhã toda treinando."

            mc "Eu gostei."

            ma "Eu também."

            if maria_relacao:

                ma "Aliás... lembra que eu falei do meu noivo?"

                mc "Sei..."

                ma "Quem sabe você não consegue me derrotar também?"

                mc "..."

                mc "Vou me esforçar. Por enquanto foi só você fazendo cooper, mas ainda vou te vencer com você dando o máximo."

                ma "Quero só ver."

            ma "Vamos voltar?"

            mc "Vamos."

            $ maria_lvl1 = True
            $ tempo += 1
        else:


            mc "Ganhar de você trotando já tá fácil, [ma]."

            ma "Realmente é incrível como você evoluiu."

            ma "Continue sempre assim. E vamos continuar com nossos treinos."

            mc "Com certeza."

            ma "Ah! E quando quiser que eu vá mais rápido me avise, tá?"

            mc "Pode deixar..."

    elif maria_lvl == 2:

        if not maria_lvl2:

            mc "Aha! Consegui!"

            ma "Uou!"

            mc "Você não reduziu, né?!"

            ma "Eu não! Eu mantive a mesma velocidade do começo ao fim. E eu tava indo rápido, viu?"

            mc "Sério? Mesmo?"

            ma "Pode acreditar em mim! Rsrs..."

            ma "Não precisa ficar tão desconfiado. Mas eu te entendo. Eu também fiquei surpresa!"

            mc "Nem acredito."

            mc "Mas eu ainda tenho energia, viu?!"

            ma "Ei! Calma!"

            scene mc maria_cavalinho with Dissolve(2.0)

            pause

            ma "Haha! Você ainda tem tudo isso de energia?"

            mc "Claro! Ainda não tô acreditando que eu realmente ganhei de você. Até esses dias parecia impossível!"

            ma "Opa. Cuidado me derrubar."

            mc "Ah tah. Pode deixar."

            if maria_relacao:

                ma "Hmmm... seu cabelo cheira gostoso."

                mc "Mas eu tava correndo. Deve tá horrível."

                ma "Não tá. Hmm... Deixa eu cheirar mais?"

                mc "Claro..."

                ma "..."

                "Eu tô sentindo os peitos dela nas minhas costas..."

                "É uma sensação incrível..."

                "..."

                ma "[mc]?"

                mc "O-oi?"

                ma "Tudo bem aí? Você deu uma apagada. Não vai desmaiar..."

                mc "Ah, não! Hehe..."

            ma "Você tá melhorando tanto... Acho que você merece me desafiar com todo meu esforço."

            mc "Sério?!"

            ma "Claro. Não tem mais o que eu te ensinar. Agora é só você treinar, treinar e finalmente me vencer."

            ma "[mc]?"

            mc "Opa. Acho que eu preciso sentar."

            ma "Claro. Deixa eu descer."

            scene mc maria_sentados with Dissolve(1.0)

            mc "Ufa... {i}puf{/i}"

            ma "Tenta não exagerar. Não quero que você caia morto aí."

            mc "Tá tudo sobre controle. Eu sou um garotão forte."

            ma "E eu acredito nisso."

            mc "Todo esse meu progresso é graças a você."

            ma "De forma alguma. Isso é graças ao seu esforço e seu comprometimento."

            ma "Tem muita gente que quer treinar, fazer academia ou um esporte, mas vivem começando e desistindo no meio."

            ma "É preciso muito esforço pra continuar até o fim."

            mc "Obrigado."

            ma "E eu falo sério. Eu sei que tem dia que a gente não tá com vontade, mas a gente precisa aprender a se auto estimular."

            ma "Pra mim, o mundo é dividido entre as pessoas que fazem e as que não fazem."

            ma "Não importa os problemas. Se você é uma pessoa que faz, você supera a preguiça e conquista aquilo que quer."

            mc "Uou... falou bonito agora."

            ma "Rsrs... desculpe pelo sermão."

            mc "Que nada. Você falou verdades."

            mc "Vamos voltando?"

            ma "Sim. Já tá ficando de tarde. Às vezes a gente exagera."

            mc "Mas eu gosto. Upa!"

            scene mc conversando_maria with Dissolve(1.0)

            mc "Olha. Sobre o que você tava falando antes."

            mc "Nada na vida é fácil, né? Mas qualquer coisinha a gente desiste dos nossos planos."

            ma "Isso que eu falo! Problemas sempre vão ter. O importante é a gente ter força pra fazer aquilo que queremos fazer."

            ma "Não tem problema se a gente falha uma vez ou outra. A gente é humano."

            ma "Mas a gente não pode desistir nunca. Pelo menos é o que eu penso."

            mc "Você realmente é bem determinada, [ma]. Você podia fazer palestras motivacionais."

            ma "Para de falar besteira, bobo."

            mc "Mas era verdade..."

            $ maria_lvl2 = True
            $ tempo += 1
        else:


            mc "Os treinos realmente tão fazendo a diferença. Já tô conseguindo vencer você de boa nessa velocidade."

            ma "Eu tô realmente impressionada com seu avanço. Sempre achei que você ia desistir antes disso."

            mc "Que nada! Agora só falta bater você usando toda sua capacidade."

            ma "Agora que a coisa vai pegar!"

            mc "Nem me fala..."

    elif maria_lvl == 3:

        if not maria_lvl3:

            mc "Ganhei? Sério? Eu ganhei mesmo?!"

            ma "..."

            mc "..."

            ma "Ganhou... você... você ganhou de mim de verdade, [mc]..."

            mc "Ganhei..."

            mc "Eu..."

            if maria_relacao:

                scene mc beijando_maria with vpunch

                $ renpy.pause(delay=5, hard=True)

                pause

                ma "Hmmm..."

                mc "Hmmm..."

                "Ela tá me beijando com tanta vontade."

                "..."

                ma "Me beija mais forte, [mc]."

                "..."

                ma "Tá bom. Vamos sentar?"

                mc "Tô precisando."

                window hide

                pause

                scene mc sentado_maria_beijo with Dissolve(2.0)

                pause

                ma "Você é incrível, [mc]."

                mc "Não quero me gabar, mas ganhar de você não foi fácil, não."

                ma "Também não quero me achar, mas sei que foi complicado. Eu sou uma corredora treinada."

                ma "E mesmo assim... você ganhou de mim. Foi incrível. Não caiu a ficha ainda."

                mc "Posso contar uma coisa? Mas não vai rir de mim..."

                ma "Rir de você? Claro que não. O que foi?"

                mc "Eu fiz tudo isso porque eu queria te impressionar."

                ma "Não creio... seu bobo..."

                mc "Ei! Você dis-"

                ma "Mas você conseguiu. Você foi melhorando a cada dia e conseguiu."

                ma "Me venceu e me impressionou, de verdade."

                "Essa é a hora. Se eu quero oficializar as coisas com a [ma], tem que ser agora."

                "Eu disse que não queria brincar com ela, mas será que é isso que eu quero mesmo?"

                menu:
                    "Pedir a [ma] em namoro":


                        $ maria_namoro = True

                        mc "Eu sei que depois dos nossos amassos no treino isso é óbvio."

                        mc "Mas toda essa jornada com você tem sido incrível."

                        mc "E eu quero aproveitar que finalmente eu cheguei ao 'fim do curso' e pedir meu presente de graduação."

                        ma "..."

                        mc "[ma], você aceita namorar comigo?"

                        ma "..."

                        ma "Claro que eu aceito, bobo!"

                        ma "Você é o rapaz mais incrível que eu vi na vida."

                        ma "Vai ser incrível ser sua parceira."

                        ma "E agora deixa eu te beijar mais."

                        mc "Ei!"

                        scene mc deitado_maria_beijo with Dissolve(3.0)

                        $ renpy.pause(delay=5, hard=True)

                        pause

                        "..."

                        "Hmmm... a gente já tá se pegando a um bom tempo..."

                        "Uma pá de gente já passou e ficou olhando. Parece que a [ma] não tá nem aí."

                        "Ainda não acredito que uma garota perfeita como ela aceitou namorar comigo."

                        "Ela é linda, cheirosa, inteligente e decidida. E tá aqui, me beijando..."

                        "Simplesmente incrível..."

                        scene black with Dissolve(6.0)

                        mc "Vamos voltar, linda?"

                        ma "Sim. Posso segurar sua mão?"

                        mc "Claro."

                        "..."
                    "Não assumir o compromisso de namorar":


                        mc "Nossa competição, nossos treinos e nossa pegação também. Tudo tá sendo incrível."

                        ma "Pra mim também, [mc]. Você é um rapaz incrível. E depois de hoje, só consigo pensar que quero te ver de novo."

                        ma "Eu queria que nossa relação não parasse nos treinos. Você entende?"

                        mc "Eu entendo. Mas ainda é muito cedo pra mim. Eu tô curtindo nosso lance, mas não tô pronto pra algo mais sério."

                        ma "Você não gosta de mim dessa forma?"

                        mc "Não é isso. É só que tá tudo tão difícil pra mim agora. Mas quando a poeira do meu trabalho abaixar..."

                        ma "Não vou pressionar você. Agora você sabe como eu me sinto. Se você quiser, estarei aqui."

                        mc "Obrigado, [ma]."

                        mc "Independente disso, quero que você continue confiando em mim. Acima de tudo, sou seu parceiro de treino."

                        ma "Tá..."

                        ma "Vamos pra casa?"

                        mc "Tá na hora. Vamos."
            else:


                ma "Não engasga, homem! Você conseguiu!"

                mc "Consegui, né?"

                ma "Sim! Você superou sua mestra!"

                mc "Haha! Não creio!"

                scene mc corrida_preparacao_maria with Dissolve(1.0)

                ma "Você conseguiu encerrar seu curso e com louvor."

                ma "Você é incrível, [mc]."

                mc "Não quero me gabar, mas ganhar de você não foi fácil, não."

                ma "Também não quero me achar, mas sei que foi complicado. Eu sou uma corredora treinada."

                ma "E mesmo assim... você ganhou de mim. Foi incrível. Não caiu a ficha ainda."

                mc "Né?! Hehe!"

                ma "Depois dessa não tem mais o que a gente nem treinar."

                mc "Quê?!"

                ma "Você é um corredor profissional agora. Sua aptidão, sua velocidade, sua resistência."

                ma "Tá na hora de você alçar voos mais altos. O que acha de treinar na minha academia?"

                mc "Eu acho demais! Com certeza!"

                ma "Então você vai continuar seu treino lá."

                ma "Obrigado pela companhia e pela amizade, [mc]. Nunca vou esquecer isso."

                mc "Calma que a gente vai se ver muito ainda. Vou te derrotar em tudo!"

                ma "Quero só ver!"

                ma "Então vamos voltar?"

                mc "Vamo lá."

            $ maria_lvl3 = True
            $ maria_evento = 6
            $ tempo += 1

    jump maria_corrida_finalizar

label maria_corrida_finalizar:

    $ dia_maria = dia + 1
    $ proibido_salvar = False
    $ show_quick_menu = True


    $ renpy.block_rollback()

    jump call_cidade

label maria_evento7:

    $ maria_evento = 8

    mc normal "E como eu começo?"

    ma "O lugar fica no centro, perto do bairro chinês e da pizzaria."

    mc "Acho que eu já passei lá na frente."

    ma "Então você sabe. Quando você for lá, a gente conversa, tá? E daí já dá pra você começar. Você vai ser um dos meus primeiros membros."

    mc charmoso "É uma honra."

    ma "Eu vim só pra te avisar, porque com a academia agora não vai dar mais pra eu correr por aqui."

    mc "Relaxa, a gente vai se ver lá na academia agora."

    if maria_namoro:

        ma "Então eu te vejo lá, gato."

        mc "Com certeza."

        ma "Agora um beijo."

        hide maria with dissolve

        "{i}smack{/i}"

        mc "Tchau."
    else:


        ma "Então te vejo lá. Até."

        hide maria with dissolve

        mc "Tchau."

    "Vou dar uma passada lá no centro quando der. Não vejo a hora de dar uma olhada na academia... e na [ma] talvez..."

    jump call_cidade

label maria_evento6:

    $ dia_maria = dia + 1
    $ maria_evento = 7

    if maria_relacao:

        mc safado "Bom dia, gata."

        show maria excitada with dissolve
    else:


        mc normal "Bom dia, [ma]."

        show maria falando with dissolve

    ma "Bom dia..."

    mc "E agora? Pronta pra correr?"

    ma "Depois que você me venceu não tem mais o que a gente nem treinar."

    mc surpreso "Quê?!"

    ma "Você é um corredor profissional agora. Sua aptidão, sua velocidade, sua resistência."

    ma "Tá na hora de você alçar voos mais altos. O que acha de treinar na minha academia? Ela acabou de abrir."

    mc feliz "Eu acho demais! Com certeza!"

    ma "Então você vai continuar seu treino lá."

    jump maria_evento7



    if maria_namoro:

        ma "A gente vai poder namorar muito lá também."

        mc safado "É o que eu quero fazer."

        ma "Até lá, vou sentir saudades da sua boca."

        mc "E eu da sua."
    else:


        ma "Obrigado pela companhia e pela amizade, [mc]. Nunca vou esquecer isso."

    mc charmoso "Mas calma que a gente vai se ver muito ainda. Vou te derrotar em tudo!"

    ma "Quero só ver!"

    show maria falando with dissolve

    ma "Assim que eu montar seu treino eu te aviso, ok? Até lá, vai se preparando."

    ma "E tem a mensalidade. Então guarda uma grana aí."

    mc desconfiado "Ei! Vai cobrar até de mim?"

    ma "Claro."

    ma "Vou indo nessa, que até eu vou dar um tempo nos treinos. A academia tá pegando todo meu tempo."

    mc normal "Tá legal. Estou ansioso pra começar."

    ma "Fica mesmo. Até a próxima."

    if maria_namoro:

        ma "Beijos, gatinho."

        mc "Até, linda."

    jump call_cidade

label maria_evento5:

    "Hoje cheguei antes da [ma]."

    ma "Bu!"

    show maria falando with dissolve

    ma "Bom dia."

    mc normal "Achei que tinha chegado antes."

    ma "Acabei de chegar também. Ainda não tô acreditando que você não desistiu."

    mc charmoso "Já falei que não vou desistir."

    ma "Tô começando a acreditar."

    ma "Bom. Vamos lá pro parque?"

    mc "Depois da senhora."

    ma "Siga a mestre!"

    hide maria with dissolve

    "Ela parece bem animada hoje."

    if maria_relacao:

        "Eu resolvi ter algo a mais com a [ma] e a forma mais fácil de impressionar parece ser derrotar ela em uma corrida."

        "Mas pra isso a gente precisa competir. Eu não consigo nem treinar direito, por que ela aceitaria competir comigo?"
    else:


        "Eu sinto que tô melhorando nos treinos. Tô louco pra desafiar ela numa corrida."

        "Vai ser difícil no começo, mas quem sabe?! Posso até mesmo superar minha mestra!"

    scene track um with Dissolve(1.0)

    show maria falando with dissolve

    ma "Você tá aguentando a caminhada até aqui muito bem."

    mc normal "Verdade."

    ma "No começo não era assim. Você já tá melhorando. Legal, né?"

    mc charmoso "Com certeza. Inclusive, eu tava pensando aqui..."

    mc "Você disse que apostava corrida com seus amigos, né?"

    show maria tadinho with dissolve

    ma "Sim. Na verdade eu tenho um pouco de vergonha rsrs... Mas eu realmente apostava corrida com eles."

    mc normal "Eu acho que essa seria uma excelente forma de medir meu progresso."

    ma "Como assim?"

    mc charmoso "Eu quero desafiar você em uma corrida."

    ma "Você tá doido, [mc]?"

    mc envergonhado "Mas é que eu queria medir meu desempenho... quem sabe isso me motivaria mais..."

    if maria_relacao:

        show maria excitada with dissolve

        ma "Falando assim você fica muito sexy, sabia?"

        mc charmoso "Por que?"

        ma "Não sei, querendo melhorar e até me vencer. Isso precisa de muita coragem."

    ma "Ok! Acho que você tá certo! Mesmo a gente tando meio velhos pra esse tipo de coisa, é uma boa ideia."

    mc normal "Sério?! Você topa?"

    ma "Sim. Se isso vai te motivar, é mais do que o suficiente pra mim."

    show maria tadinho with dissolve

    ma "Mas não adianta eu correr o máximo que eu posso. Seria injusto."

    ma "Então eu vou deixar você escolher se eu vou fazer um trote leve, se eu vou correr moderadamente ou dar o melhor de mim."

    ma "Assim você vai progredindo devagar e tendo a sensação de que você tá melhorando."

    mc charmoso "Perfeito!"

    ma "Mas não vou deixar você ganhar. Mesmo só com um trote, vai ser complicado você me vencer."

    mc zerado "Aí você também tá me zuando."

    show maria falando with dissolve

    ma "De forma alguma. Você vai ter que continuar treinando muito antes de ganhar de mim pela primeira vez."

    ma "Continue treinando e só me desafie quando realmente se sentir preparado, tá?"

    "Impossível que eu não vou ganhar nem dela fazendo um cooper..."

    mc charmoso "Vamos ver."

    mc "Então, só pra gente testar, eu quero correr hoje uma vez contra você."

    ma "Mas já?"

    mc "Sim."

    ma "Se você quer, então tá."

    ma "Pode se preparar."

    scene mc maria_preparacao with Dissolve(1.0)

    pause

    ma "Vamos sair daqui, dar uma volta no parque todo, passando pela área asfaltada, e chegar aqui de novo, certo?"

    $ maria_tempo = 2.0
    $ maria_esquerda = 1
    $ mc_esquerda = 0
    $ maria_point = 0.05
    $ mc_point = 0.05

    $ maria_velocidade = 0.05
    $ mc_velocidade = 0.001

    mc "Combinado."

    ma "Tudo pronto?"

    mc "Quando você quiser."

    ma "{cps=6}{i}3... 2... 1...{/i}{/cps}{w=1.0}{nw}"

    ma "Vai!"

    show screen maria_corrida nopredict

    $ renpy.pause()

    "..."

    label maria_primeira_corrida:

        scene mc corrida_cansado with Dissolve(1.0)

        mc "{i}puf puf{/i}"

        mc "Impossível..."

        mc "{i}puf puf{/i}"

        ma "Calma. É só sua primeira vez."

        mc "Você... não tá nem ofegante..."

        mc "{i}puf puf{/i}"

        ma "Haha! Vai demorar um pouco pra você me deixar sem ar."

        mc "..."

        ma "Acho que hoje foi um excelente treino."

        ma "Não esqueça de treinar antes de me chamar para correr de novo."

        ma "A cada treino você vai aguentar correr mais rápido e logo logo você vai conseguir me derrotar."

        ma "Eu acho..."

        mc "Engraçadinha... mas não tô com energia pra brigar com você agora."

        ma "Rsrs... Vamos voltar."

    $ maria_evento = 5
    $ dia_maria = dia + 1

    jump call_cidade

label maria_evento4:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("ma1_save", extra_info="ma1_save")

    "Opa. A [ma] já tá aqui. Acho que ela tava me esperando."

    menu:
        "Bom dia. Tava me esperando?":


            mc normal "Bom dia, [ma]. Tava me esperando?"

            show maria falando with Dissolve(1.0)

            ma "Bom dia, [mc]."

            ma "Eu tava um pouco preocupada que talvez você não fosse aparecer."

            mc normal "Eu falei que viria."
        "Bom dia, linda.":


            $ maria_seducao += 1

            mc charmoso "Bom dia, linda."

            if maria_seducao >= 3:

                show maria excitada with Dissolve(1.0)

                ma "Se fosse qualquer outro falando isso, eu ia reclamar."

                ma "Mas você tá fazendo por merecer... nem acredito que você realmente veio treinar."

                mc charmoso "Claro que eu vim. Você sabe que eu tô interessado em você."

                mc charmoso "Quer dizer, tô interessado nos treinos."

                ma "Entendi..."
            else:


                show maria falando with Dissolve(1.0)

                ma "Bom dia..."

                ma "Eu tava um pouco preocupada que talvez você não fosse aparecer."

                mc normal "Eu falei que viria."

    ma "E então? Pronto pra começar seus treinos?"

    mc charmoso "Com certeza. Vou melhorar meu fôlego rapidinho."

    ma "Nós chamamos de aptidão física. Quanto mais você treinar, maior ela será."

    mc normal "Pode ter certeza que logo já vou te acompanhar. E te passar também."

    show maria tadinho with dissolve

    ma "Vamos ver..."

    ma "Bom, vamos então?"

    mc "Com certeza."

    ma "Pode vir atrás de mim."

    hide maria with dissolve

    "..."

    scene track geral with Dissolve(1.0)

    pause

    show maria falando with dissolve

    ma "Aqui é o melhor lugar pra correr em altas velocidades."

    mc normal "Depois do viaduto ali é onde fica aquele outro parque com a ponte e aquele lago."

    ma "Isso mesmo. A gente já vai pra lá. Mas aqui, como é asfaltado, é melhor pra fazer corridas."

    mc desconfiado "Corrida?"

    show maria excitada with dissolve

    ma "Eu e uns amigos às vezes apostávamos corrida aqui pra ver quem era mais rápido."

    mc envergonhado "O louco. Isso já aparece meio avançado pra mim."

    ma "Sei que é meio loucura pra alguém da nossa idade, mas foi assim que meu noivo me conquistou."

    mc surpreso "Você é casada?!"

    show maria tadinho with dissolve

    ma "Não, não. A gente nem chegou a casar."

    ma "No fundo ele não passava de um idiota que me traía com outras garotas."

    mc desculpa "Que droga, [ma]..."

    menu:
        "Eu nunca faria isso com você.":


            $ maria_seducao += 1

            show maria excitada with dissolve

            ma "Nunca faria, né?"

            ma "Mas você precisa ser meu parceiro pra não me trair, certo? Senão não importa com quem você fica..."

            mc charmoso "..."
        "Se precisar falar sobre isso...":


            mc desculpa "Se precisar falar sobre isso, pode me chamar, ok?"

            ma "Então você é meu melhor amigo agora? Rsrs..."

    if maria_seducao >= 3:

        "Eu tenho dado em cima da [ma] nesses últimos dias."

        "Tenho a impressão que ela também tá gostando... Mas depois de saber esse lance, não quero brincar com ela."

        if priscila_namoro:

            "Não posso esquecer que eu falei pra [c] que eu quero namorar com ela."

            "Seria certo com ela?"

        if sayuri_e4 == "namoro":

            "Depois daquele beijo, as coisas com a [s] estão caminhando para algo mais sério."

            "Como que eu fico com ela?"

        label maria_decisao_relacao:

            "Preciso decidir se eu quero ir além com a [ma] ou não..."

        menu:
            "Eu quero algo mais com a [ma]":


                "Certeza que eu vou querer seguir o caminho da {b}sedução{/b} com ela?"

                "Eu acredito que não vou poder trocar minha escolha nunca mais."

                menu:
                    "Certeza. Quero algo mais com ela":


                        $ maria_relacao = True

                        python:
                            if renpy.android:
                                PythonSDLActivity.registraEvento("maria_relacao","maria","personagem")

                        "Com certeza. Ela tá mexendo muito comigo."
                    "Não. Melhor eu pensar um pouco mais":


                        "Ixi... agora não sei... Deixa eu pensar um pouco..."

                        jump maria_decisao_relacao
            "Eu serei apenas um amigo para a [ma]":


                "Certeza que eu vou querer seguir o caminho da {b}amizade{/b} com ela?"

                "Eu acredito que não vou poder trocar minha escolha nunca mais."

                menu:
                    "Certeza. Serei apenas um amigo.":


                        "Com certeza. Não tenho segundas intenções com ela."
                    "Não. Melhor eu pensar um pouco mais":


                        "Ixi... agora não sei... Deixa eu pensar um pouco..."

                        jump maria_decisao_relacao
    else:


        "Eu e a [ma] estamos virando bons amigos. Tô gostando bastante de como as coisas estão progredindo."

        "Não tenho segundas intenções com ela e tenho certeza que ela será uma incrível treinadora."

    ma "Então... eu e meu ex-noivo começamos a treinar juntos, até que ele conseguiu me vencer na corrida."

    ma "Não sei o que aconteceu, mas depois disso eu fiquei caidinha por ele."

    if maria_relacao:

        "Então o cara conquistou ela vencendo ela na corrida? Com certeza não foi só isso, mas mesmo assim é estranho."

        "Hmmm... Essa deve ser a melhor forma de impressionar ela..."

    ma "Acho que foi ver como ele cresceu e melhorou, não sei. Ele parecia um homem tão bem sucedido."

    mc charmoso "Entendo."

    show maria tadinho with dissolve

    ma "Mas chega de falar de mim e do meu passado depressivo."

    mc "Relaxa. Eu gosto de saber sobre você."

    ma "Acho que tá bom por uma manhã. Vamos correr."

    hide maria with dissolve

    "Acho que ela ficou com vergonha. Que gracinha."

    "..."

    scene track um with Dissolve(1.0)

    mc concentrando "Ufa, chegamos."

    show maria tadinho with dissolve

    ma "Já cansou?"

    mc envergonhado "Claro que não."

    ma "Então vamos alongar e daí correr."

    show maria alongando with Dissolve(1.0)

    pause

    ma "Hmm..."

    scene maria alongamento with Dissolve(1.0)

    pause

    ma "Haa..."

    ma "?"

    ma "E você? Vai alongar ou vai ficar só olhando?"

    if maria_relacao:

        mc safado "Prefiro ficar olhando você mesmo."

        ma "A é?"

        ma "Então olha direitinho pra aprender..."

        mc "Com certeza..."
    else:


        "Tô vendo se aprendo como faz."

    scene maria alongamento_dois with Dissolve(1.0)

    pause

    if maria_relacao:

        mc charmoso "Você quer ajuda? Eu posso alongar você se você quiser."

        ma "Você é tão prestativo, [mc]..."

        mc "Claro."

        ma "Quem sabe quando você realmente souber alongar alguém."

        mc envergonhado "Ok..."

        ma "Vai olhando por enquanto."

    "..."

    ma "Estou pronta. Bora correr?"

    mc normal "Vamos."

    "..."

    scene maria correndo_mc with Dissolve(1.0)

    pause

    "..."

    mc "{i}puf puf{/i}"

    mc "Nós tamo correndo... mais que da... outra vez..."

    mc "{i}puf puf{/i}"

    ma "Claro. Cada dia vamos correr 300 metros a mais."

    mc "Quê?!"

    ma "Você quer melhorar ou não?"

    mc "Claro! Conte... comigo..."

    ma "Assim que se fala."

    mc "{i}puf puf{/i}"

    mc "Na verdade... pera..."

    scene mc corrida_cansado with Dissolve(1.0)

    mc "Acho que vou ter que parar por aqui hoje."

    ma "Tudo bem."

    mc "{i}puf puf{/i}"

    mc "Malz por atrapalhar..."

    ma "Não esquente. Isso é normal em um treino puxado. Se você foi até o limite, isso que importa."

    mc "Beleza..."

    mc "{i}puf puf{/i}"

    ma "Por hoje está excelente. Vamos voltar?"

    mc "Só me dá 1 minuto."

    ma "Você merece uns três."

    mc "..."

    $ maria_evento = 4
    $ dia_maria = dia + 1

    jump call_cidade

label maria_evento3:

    show mc pensando with dissolve

    "Estou muito entusiasmado pra correr com a [ma]. Só espero que eu aguente o tranco."

    "Do jeito que ela disse da outra vez, ela vira o demônio durante o treino."

    "Opa. Ela tá vindo aí."

    hide mc with dissolve

    "..."

    show maria falando with Dissolve(1.0)

    ma "Bom dia, [mc]. Pronto pra começar?"

    mc charmoso "Com certeza."

    if maria_seducao >= 2:

        show maria excitada with dissolve

        ma "No outro dia você parecia mais interessado em me ver com a roupa de treino do que treinar mesmo."

        mc envergonhado "Não, não. Foi só impressão sua."

        ma "Será mesmo?"

        mc safado "Bom... se-"

        ma "Pode parando por aí, safado."

        mc "..."

    show maria falando with dissolve

    ma "Hoje a gente vai fazer uma caminhada até o outro parque e de lá vamos correr um pouco, ok?"

    if v31_fim:

        "Eu fui uma vez lá com a [c]. Eu lembro."

        mc "Ah! Eu sei qual é."

    mc normal "Tô pronto."

    show maria tadinho with dissolve

    ma "Você tem certeza que você vai aguentar?"

    mc charmoso "Com certeza. Pode estar certa disso."

    ma "Então tá... Vamos nessa."

    hide maria with dissolve

    mc surpreso "Ei! Espera!"

    "..."

    scene black with Dissolve(1.0)

    "Caraca. Não conhecia esse caminho, não."

    "..."

    scene track geral with Dissolve(2.0)

    mc normal "Nunca tinha vindo pra cá."

    show maria falando with dissolve

    ma "Seguindo pra lá chega no Condomínio das Águas. E pra lá é o aeroporto."

    mc desconfiado "Então quer dizer que a ilha continua pra fora do centro?"

    ma "Com certeza. A maioria das pessoas só conhecem essa área central, mas a ilha é muito maior do que isso."

    ma "Mas vamos continuar. Estamos quase lá."

    hide maria with dissolve

    mc normal "Ok."

    "..."

    scene track um with Dissolve(2.0)

    mc normal "Que lugar bacana. É coisa nova pra mim."

    show maria tadinho with dissolve

    ma "Você precisa sair mais de casa, [mc]. Dar umas voltas e tal."

    mc envergonhado "Você tem razão."

    show maria excitada with dissolve

    ma "Mas só de você vir aqui já é um passo importante. Vamos mudar esse seu estilo de vida."

    mc "Combinado."

    ma "Eu vou me alongar, e você faz o mesmo."

    hide maria with dissolve

    "A [ma] vai se alongar bem aqui... será que eu devo dar uma espiada?"

    menu:
        "Observar ela se alongando":


            $ maria_seducao += 1

            "Só dar uma olhadinha..."

            scene maria alongamento with Dissolve(2.0)

            pause

            mc surpreso "!"

            "Essa [ma] é realmente gostosa pra caramba."

            ma "Vai continuar?"

            mc envergonhado "Continuar?"

            ma "Olhando pra mim desse jeito..."

            mc "Ah! Só quero apre-"

            ma "Só pra aprender. É verdade."

            mc safado "..."
        "Não olhar na direção dela":


            "Melhor eu me comportar. Ou ela vai me achar um tarado."

            "..."

    scene track um with Dissolve(1.0)

    show maria excitada with dissolve

    ma "Pronto pra suar?"

    mc charmoso "Com certeza."

    ma "Go!"

    hide maria with moveoutleft

    mc serio "Vamos lá!"

    "..."

    "{b}O desempenho físico de [mc] é sofrível e logo ele se cansa{/b}"

    scene maria correndo_mc with Dissolve(1.0)

    ma "Cadê toda aquela confiança agora?"

    mc "Tá- tudo... bem... tá- {i}puf{/i} tudo- legal..."

    ma "Acho que tá bom por hoje."

    scene track um with Dissolve(1.0)

    show maria tadinho with dissolve

    ma "Tudo legal? Não vai ter um infarto..."

    mc concentrando "Tá legal..."

    mc desculpa "Desculpa atrapalhar seu treino."

    ma "Relaxa. É sua primeira vez. Com o tempo você vai melhorando."

    ma "Só não desistir."

    mc charmoso "Com certeza eu não vou."

    ma "Assim que se fala. Vamos voltar?"

    mc "Vamos."

    scene black with dissolve

    p rindo "Treinar com a [ma] vai fortalecer cada vez mais o [mc]."

    p "Continue treinando com ela para aumentar seu desempenho durante os treinos e assim liberar novos eventos."

    p "Boa sorte!"

    $ maria_evento = 3
    $ dia_maria = dia + 1

    jump call_cidade

label maria_evento2:

    show maria cooper with dissolve

    "Ops, a [ma] tá aqui correndo na praça de novo."

    menu:
        "Melhor não interromper o exercício dela":


            "Não vou incomodar ela agora. Seria meio desespero."

            hide maria with moveoutleft

            "..."

            mc surpreso "!"

            mc zerado "Ela foi embora..."

            jump call_cidade
        "Interromper a caminhada e falar com ela":


            "..."

            mc normal "Olá, [ma]."

            ma "Opa!"

    hide maria

    show maria falando with Dissolve(1.0)

    ma "Oi, [mc]."

    mc charmoso "Lembrou meu nome?"

    ma "Sim. Não quero passar carão de novo."

    menu:
        "Você que é inesquecível, não eu.":


            $ maria_seducao += 1

            mc charmoso "Não tem nada de errado em você errar meu nome. Você que é inesquecível, não eu."

            show maria excitada with Dissolve(1.0)

            ma "Inesquecível, é?"

            mc "Pra mim você foi."

            if nge == "Maria":

                mc safado "Nunca vou esquecer nossa conversa no bar."

                ma "Você quer conversar comigo outra vez?"

                mc safado "Adoraria."

            ma "Você xaveca todas as garotas que você encontra?"

            mc charmoso "Só as que que valem o esforço."

            ma "..."
        "Que nada. Tá de boa.":


            mc normal "Relaxa. Não ligo pra isso."

            ma "Ah... mas eu ligo. Passar vergonha sempre é chato. Fica aquele silêncio..."

            mc feliz "Nisso você tem razão."

    mc envergonhado "Tô atrapalhando seu exercício de novo."

    show maria falando with dissolve

    ma "Não tem problema. Pra falar a verdade, tô meio cansada já."

    mc normal "Você malha sozinha sempre?"

    ma "Até já teve amigo que tentou vir comigo, mas ninguém consegue acompanhar meu ritmo."

    ma "Eu sou meio vidrada em exercício."

    menu:
        "Eu tô precisando fazer exercício também.":


            mc normal "Pra falar a verdade eu tô precisando malhar também."

            if v10_fim:

                "Quem sabe dar umas porradas no Marco?"

            ma "Sério, mesmo?"

            mc "Sim. Às vezes companhia é o que tava faltando pra eu realmente começar."
        "Pra poder ver você vestida assim vale muito à pena.":


            $ maria_seducao += 1

            mc tarado "Eu vou poder ver você vestida assim sempre se eu treinar com você?"

            ma "Essa é minha roupa de malhação, ué? Vai poder..."

            mc "Então vale muito à pena."

            show maria excitada with dissolve

            ma "Vai correr todo dia só pra me ver com essa roupa coladinha?"

            mc safado "Com certeza."

            ma "..."

    ma "Só que..."

    show maria tadinho with Dissolve(1.0)

    ma "Já aviso que minha carga de treino é super puxada. Se você enrolar te deixo pra trás."

    mc charmoso "Combinado. Não vou te atrasar, não."

    ma "Então dá próxima vez que a gente se encontrar aqui no parque você vêm comigo."

    mc "Combinado."

    show maria falando with dissolve

    ma "Então agora vou alongar um pouco e voltar."

    mc normal "Beleza."

    menu:
        "Posso ver você se alongando?":


            $ maria_seducao += 1

            mc safado "Posso ver você se alongando? Quem sabe não aprendo alguma coisa."

            show maria excitada with dissolve

            ma "Só pra aprender, né?"

            mc safado "Com certeza."

            ma "Hmm..."

            ma "Ok."

            ma "Olha bem... por todos os ângulos."

            show maria alongando with Dissolve(1.0)

            pause

            "Caraca, que mina gostosa."

            "Só de pensar que eu vou poder ver isso todo dia que eu treinar com ela..."

            ma "Tá aprendendo?"

            mc "Tô, claro."

            ma "..."

            "Bom, já sequei ela demais."

            mc charmoso "Até a próxima, [ma]."

            ma "Beijão."

            "..."
        "Não vou te atrapalhar. A gente se fala.":


            mc normal "Vou te deixar aí de boa então. A gente se vê, [ma]."

            ma "Legal, [mc]. Beijo!"

            mc "Beijos."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("maria_evento_2","maria","personagem")

    $ maria_evento = 2
    $ dia_maria = dia + 1

    jump call_cidade

label maria_evento1:

    "..."

    mc charmoso "Opa. Uma mina fazendo cooper logo cedo?"

    show maria cooper with dissolve

    pause

    "Parece bem gata..."

    "..."

    if nathan_e1 != "nada":

        mc desconfiado "Espera... acho que já vi essa mulher em algum lugar..."

        mc surpreso "!"

        "É aquela garota que eu vi no bar com o [n]!"

        if nge == "Maria":

            mc tarado "E a gente até conversou..."

        hide maria with dissolve

        "O nome dela era [ma] se não me engano."

    mc surpreso "!"

    "Ela tá se alongando..."

    menu:
        "Olhar para ela":


            show maria alongando with dissolve

            pause

            mc safado "Quem perderia uma visão dessas?"

            "O corpo dela é bem sarado. Ela deve se esforçar na vida fit."
        "Desviar o olhar":


            mc envergonhado "Não vou ficar incarando igual um tarado..."

            "Mas deu pra ver que ela tem um corpo em boa forma. Ela deve pegar pesado nos treinos."

    "É uma chance de ouro eu poder falar com ela."

    hide maria with dissolve

    mc normal "Oi. Bom dia..."

    show maria falando with dissolve

    ma "Bom dia."

    if nathan_e1 != "nada":

        ma "Ah! Eu conheço você..."

        mc envergonhado "Sim. A gente se viu no bar."

        if nge == "Maria":

            ma "Eu diria que a gente fez mais que se ver..."

            mc safado "Verdade..."

        elif nge == "Ana":

            ma "Você conversou com a minha amiga, Ana."

            mc normal "Isso mesmo."
        else:


            ma "A gente teve que sair porque você e o [n] tinham que resolver um negócio."

            mc desculpa "Verdade... peço desculpas por embaçar o esquema de vocês."

            ma "Relaxa. Já passou."

    mc normal "Você costuma correr sempre por aqui?"

    ma "Sempre que dá tempo. Não é uma coisa certa."

    mc normal "Bacana."

    menu:
        "É importante a gente cuidar da saúde.":


            mc normal "É importante a gente cuidar da saúde."

            ma "Concordo. É algo que eu levo bem a sério. Mesmo não vindo aqui todos os dias, sempre malho em algum lugar."
        "Dá pra ver que você malha bastante.":


            mc charmoso "Dá pra ver que você se esforça bastante no treino. Com todo o respeito, seu corpo é muito bem definido."

            ma "Valeu. Eu realmente gosto do meu corpo. Eu me esforço bastante mesmo."

    ma "Falando nisso, tenho que ir trabalhar agora."

    mc normal "Tá certo. Tomara que a gente se veja mais vezes. Eu moro aqui perto."

    ma "Então talvez a gente se veja. Eu corro aqui de manhã sempre que dá. Foi legal ver você de novo. Seu nome era..."

    mc "[mc]."

    if nathan_e1 != "nada":

        mc "E você é a [ma], né?"

        ma "Lembrou meu nome? Desculpa não ter lembrado o seu."
    else:


        ma "Meu nome é [ma]."

    mc normal "Tranquilo. Até outra hora, [ma]."

    ma "Beijos!"

    hide maria with dissolve

    "Legal saber que ela treina por aqui. Talvez se eu vier aqui mais vezes na parte da manhã eu encontre ela."

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("maria_evento_1","maria","personagem")

    $ maria_evento = 1
    $ dia_maria = dia + 1

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
