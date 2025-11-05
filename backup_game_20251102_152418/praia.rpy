label praia_especial:

    hide screen cidade_tela
    with dissolve

    if not praia_especial_1vez:

        $ praia_especial_1vez = True

        p rindo "E aí, pessoinha? Curtindo a viagem?"

        p "Não quero interromper você, mas tenho que lhe explicar algo importante."

        p "Essa opção que você escolheu permite que você chame uma garota ou garoto que você goste para passar um tempo com eles na praia."

        p "Alguns você precisa estar namorando, outros não. Isso varia de pessoa para pessoa, meu bem."

        p "Outra coisa! Esse é um evento opcional com sua pessoa especial, e não altera o desenvolvimento do restante da história dela."

        p "Esses eventos servem para que você conheça melhor sua alma gêmea... {i}pfff{/i} tá bom... como se você só tivesse uma."

        p "Com o passar das atualizações, mais e mais personagens ganharão seu evento especial na praia."

        p "O evento custa {b}Celebrity Reais{/b}, pois o [mc] precisa preparar tudo perfeitamente para deixar aquela impressão! TOPZERA!"

        p "Você pode ganhar {b}C${/b} trabalhando no bar e em outros bicos espalhados pela cidade. Você também pode comprar com dinheiro do seu mundo."

        p "Os encontros na praia são {b}super quentes{/b}, com várias cenas com as personagens de biquíni e em poses sugestivas. Fan service total! Então aproveita!"







        p "Boa praia e boa pegação!"

    "Bem que eu podia passar um dia especial na praia com alguém hoje."

    if tempo >= 2:

        "Só que pra dar tempo de tudo e talz tem que ser de manhã, quando o sol ainda tiver nascendo pra eu poder preparar tudo."

        "Quem sabe amanhã."

        show screen cidade_tela
        with dissolve

        pause

    menu:
        "Chamar alguém para um evento especial na praia":


            "Isso mesmo. Seria massa."
        "Deixar para outro dia":


            "Nah. Outro dia que eu tiver com mais vontade eu preparo algo assim."

            show screen cidade_tela
            with dissolve

            pause

    "Quem eu vou chamar?"

    menu:
        "Priscila":


            if not priscila_namoro:

                "Eu queria fazer algo mais quente... eu e a [c] somos só amigos."

                "{b}Se a gente estivesse namorando{/b}, daí sim..."

                "Bom... bola pra frente."

                show screen cidade_tela
                with dissolve

                pause

            if not praia_priscila_local:

                mc charmoso "Vai ser muito massa passar um tempo sozinho com a Pri na praia."

                jump praia_especial_priscila
            else:


                "Eu e a [c] já viemos aqui na praia aquele dia. A gente curtiu muito, se pegou... foi muito bom."

                mc safado "Seria incrível se a gente pudesse vir de novo..."

                "Tenho que pensar em algo diferente que a gente possa fazer antes de convidar ela outra vez."

                "O que será que eu poderia fazer?"

                show screen cidade_tela
                with dissolve

                pause
        "Sayuri":


            if not sayuri_namoro:

                "Eu queria fazer algo mais quente... eu e a [s] somos só amigos."

                "{b}Se a gente fosse namorados{/b}... Deus do céu..."

                "Bom... bola pra frente."

                show screen cidade_tela
                with dissolve

                pause

            if not praia_sayuri_local:

                mc charmoso "Só de pensar em passar um tempo com a [s] na praia, já tô ficando doido.."

                jump praia_especial_sayuri
            else:


                "Eu e a [s] já viemos aqui na praia aquele dia. Foi incrível! A gente se beijou, a gente curtiu..."

                mc safado "Não vejo a hora da gente fazer isso de novo!"

                "Mas não vou ficar fazendo as mesmas coisas. Quero pensar em outras coisas pra apimentar nossa relação."

                "O que será que a gente poderia fazer?"

                show screen cidade_tela
                with dissolve

                pause
        "Júlia":


            if julia_final2:

                "Júlia... onde você tá?"

                "Até agora eu não sei se você tá viva ou não!"

                show screen cidade_tela with Dissolve(0.5)

                pause

            if not julia_namoro:

                if julia_seducao > 7 and v8_fim:

                    "Bom... eu e a [g] não tamo namorando, mas acho que ela não ia negar uma farrinha na praia. Eu conheço essa menina."
                else:


                    "Eu queria fazer algo sexy com ela, não queria sair igual amigos. E eu nunca tive essa intenção com ela, então é melhor não provocar."

                    "Eu tenho que vir aqui com as pessoas que eu realmente quero algo a mais. Bola pra frente!"

                    show screen cidade_tela
                    with dissolve

                    pause
            else:


                "Agora que eu e a [g] tamo namorando a gente precisa fazer algo especial aqui na praia. Um lance bem quente e sexy."

            if not praia_julia_local:

                mc charmoso "Com o sol da praia, a [g] vai pegar mais fogo do que ela já pega normalmente. Já dá um arrepio só de pensar."

                jump praia_especial_julia
            else:


                "Só que eu e a [g] já viemos aqui na praia. Foi muito bom. Já tô sentindo o passarinho acordar só de lembrar."

                mc safado "Seria incrível se a gente pudesse vir de novo..."

                "Tenho que pensar em algo diferente que a gente possa fazer antes de convidar ela outra vez."

                "O que será que eu poderia fazer?"

                show screen cidade_tela
                with dissolve

                pause
        "Diana":


            if diana_rompeu:

                "Eu abandonei a Diana no Cassino. Ela tá presa pra sempre e a gente não namora mais."

                "Por que o destino foi assim?"

                show screen cidade_tela with Dissolve(1.0)

                pause

            elif diana_final2:

                "A Diana não tá mais aqui..."

                "Espero que ela esteja bem... seja lá onde ela esteja."

                show screen cidade_tela with Dissolve(1.0)

                pause

            if not praia_diana_local:

                mc charmoso "Vai ser muito massa passar um tempo sozinho com a Diana na praia."

                jump praia_especial_diana
            else:


                "Eu e a [d] já viemos aqui na praia. Foi um dia incrível"

                mc safado "Seria foda fazer de novo..."

                "Tenho que pensar em algo diferente que a gente possa fazer antes de convidar ela outra vez."

                "O que será que eu poderia fazer?"

                show screen cidade_tela
                with dissolve

                pause
        "Nathan":


            if not nathan_namoro:

                if nathan_quente:

                    "Bom... eu e o [n] não tamo namorando, mas a gente já ficou antes. Eu acho que ele vai curtir mais uma chance de dar uns pegas."
                else:


                    "Eu e o [n] nunca ficamos. Seria estranho tentar algo mais quente com ele assim."

                    "Eu tenho que vir aqui com as pessoas que eu realmente quero algo a mais. Talvez mais pra frente!"

                    show screen cidade_tela
                    with dissolve

                    pause
            else:


                "Agora que eu e o [n] tamo namorando tô afim de fazer algo especial com ele aqui na praia. Um encontro mais quente..."

            if not praia_nathan_local:

                mc charmoso "Com o sol da praia, vai ser a chance perfeita pra eu e o [n] se pegar. Já dá um arrepio só de pensar."

                jump praia_especial_nathan
            else:


                "Eu e o [n] já viemos aqui na praia. Foi bem massa."

                mc tarado "Seria incrível se a gente pudesse vir de novo..."

                "Tenho que pensar em algo diferente que a gente possa fazer antes de convidar ele outra vez."

                "Hmmm..."

                show screen cidade_tela
                with dissolve

                pause

        "Sofia" if v36_fim:

            if not praia_sofia_local:

                mc angustiado "Chamar a [w] pra um encontro quente na praia? Eu tô com merda na cabeça!?"

                jump praia_especial_sofia
            else:


                "É difícil de acreditar, mas eu realmente vi a [w] de biquíni... e foi incrível."

                "A chance de isso acontecer de novo é a mesma de um raio cair na minha cabeça agora."

                show black with dissolve

                "{i}Trrrrrduummmm{/i}"

                hide black with dissolve

                mc surpreso "E-eita!"

                "Quem sabe um dia..."

                show screen cidade_tela
                with dissolve

                pause

        "Natasha" if v22_fim and not praia_natasha_local:

            jump praia_especial_natasha

        "Nona" if v52_fim and nona_e3 != "morta" and not praia_nona_local:

            jump praia_especial_nona
        "Não chamar ninguém":


            "Pensando bem, outro dia que eu tiver com mais vontade eu preparo algo assim."

            show screen cidade_tela
            with dissolve

            pause

label praia_especial_priscila:

    $ praia_escolhida = "priscila"

    "Essa é a primeira vez que a gente vai curtir a praia como namorados."

    "Vou comprar um biquini pra ela usar, pagar um bom lanche pra matar a larica, mais algumas bebidas..."

    python:
        if renpy.android:
            praia_priscila = PythonSDLActivity.pegaPraiaPriscila()

    "..."

    if praia_priscila:

        "{b}Você já pagou para levar a [c] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_priscila_evento
    else:


        jump praia_especial_grana

label praia_especial_sayuri:

    $ praia_escolhida = "sayuri"

    "Essa é a primeira vez que a gente vai curtir a praia como namorados."

    "Vou comprar um maiô massa pra ela e garantir uma tarde muito boa..."

    python:
        if renpy.android:
            praia_sayuri = PythonSDLActivity.pegaPraiaSayuri()

    "..."

    if praia_sayuri:

        "{b}Você já pagou para levar a [s] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_sayuri_evento
    else:


        jump praia_especial_grana

label praia_especial_julia:

    $ praia_escolhida = "julia"

    "Essa é a primeira vez que a gente vai curtir a praia juntos."

    "Vou comprar um biquini super sexy pra ela e ter um dia que ela não vai esquecer."

    python:
        if renpy.android:
            praia_julia = PythonSDLActivity.pegaPraiaJulia()

    "..."

    if praia_julia:

        "{b}Você já pagou para levar a [g] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_julia_evento
    else:


        jump praia_especial_grana

label praia_especial_diana:

    $ praia_escolhida = "diana"

    "Opa... vai ser massa curtir a praia com a [d]."

    if not diana_namoro:

        "A gente não tá namorando, mas eu acho que pode rolar algo quente entre a gente mesmo assim."
    else:


        "Ainda mais que a gente tá namorando... com certeza vai rolar um lance quente."

    "A [d] é outro nível. Eu vou comprar um biquíni de marca e uns drinks bem caprichados."

    python:
        if renpy.android:
            praia_diana = PythonSDLActivity.pegaPraiaDiana()

    "..."

    if praia_diana:

        "{b}Você já pagou para levar a [d] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_diana_evento
    else:


        jump praia_especial_grana

label praia_especial_nathan:

    $ praia_escolhida = "nathan"

    "Opa... vai ser massa curtir a praia com o [n]."

    if not nathan_namoro:

        "Eu e o [n] não temos nada sério ainda, mas nada impede a gente de se 'conhecer melhor' seminus aqui na praia."
    else:


        "Ainda mais agora que a gente tá namorando. A gente precisa de um tempo juntos longe dos problemas."

    "O [n] é um cara muito bacana. Eu me sinto bem perto dele. Eu quero esquecer todos os rolos e só curtir um dia massa junto com ele."

    python:
        if renpy.android:
            praia_nathan = PythonSDLActivity.pegaPraiaNathan()

    "..."

    if praia_nathan:

        "{b}Você já pagou para levar o [n] para a praia uma vez. Mas neste gameplay você ainda não levou ele.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_nathan_evento
    else:


        jump praia_especial_grana

label praia_especial_sofia:

    $ praia_escolhida = "sofia"

    "Ir pra praia com a [w]... será que é possível?"

    "Eu tô achando que ela nunca aceitaria vir na praia com um homem."

    "Mas não custa tentar, né? Ou talvez custe... caralho... que dúvida cruel."

    python:
        if renpy.android:
            praia_sofia = PythonSDLActivity.pegaPraiaSofia()

    "..."

    if praia_sofia:

        "{b}Você já pagou para levar a [w] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_sofia_evento
    else:


        jump praia_especial_grana

label praia_especial_natasha:

    $ praia_escolhida = "natasha"

    if not v49_fim:

        "Eu e a [na] já conversamos um bocado, mas eu ainda não tenho intimidade suficiente pra chamar ela pra vir pra praia comigo."

        "É melhor eu continuar saindo com ela mais um pouco."

        "Onde será que eu acho ela?"

        if not v37_fim:

            "{b}Depois de conhecer a [na] no Cassino e terminar o primeiro evento com ela, você pode encontrar ela novamente no Distrito durante a noite{/b}"

            if not v29_fim:

                "{b}Não é preciso encontrar o Barão para ver ela no Distrito. Apenas vá lá durante a noite e o evento começará{/b}"

                "{b}Após encontrar a [na] no Distrito, você poderá fazer o próximo evento dela indo na redação na parte da manhã{/b}"

        show screen cidade_tela with Dissolve(0.5)

        pause

    "Depois que eu e a [na] se encontrou no Distrito e eu descobri sobre ela e o prefeito, a gente acabou se aproximando muito mais."

    if natasha_e4 == "seducao" or na1_beijo or na3_beijo:

        "A gente acabou até se pegando."

    "Talvez seja a hora ideal de chamar ela pra cá e ter um lance mais quente com ela."

    "A [na] sem dúvida é muito gata. Ela também tem um ar misterioso e eu sempre fico coisado quando tô com ela."

    "Ver ela de biquíni e todinha pra mim aqui na praia vai ser incrível. Eu preciso disso na minha vida! Urgente!"

    python:
        if renpy.android:
            praia_natasha = PythonSDLActivity.pegaPraiaNatasha()

    "..."

    if praia_natasha:

        "{b}Você já pagou para levar a [na] para a praia uma vez. Mas neste gameplay você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_natasha_evento
    else:


        jump praia_especial_grana

label praia_especial_nona:

    $ praia_escolhida = "nona"

    "Depois que eu salvei a [h] do [to] aquela vez, a gente se aproximou pra caramba."

    "A gente conversou sobre várias coisas e deu pra ver como ela é incrível."

    if nona_interesse:

        "Eu até resolvi tentar alguma coisa a mais com ela. Não pra ignorar uma mina dessas. Só um idiota ia ser só amigo dela por vontade própria."

        if no2_especial:

            "E o mais incrível é que eu beijei ela e ela não me deu um tapa. Acho até que ela gostou."

            "A gente tá longe de um lance sério, mas é um começo."

        "Ia ser incrível passar um tempo com ela aqui. Quem sabe o que não dá pra rolar só nós dois no calor da praia."

        "Poder dar uns pega nela, beijar, passar a mão... tô ficando louco só de pensar. Eu preciso chamar ela."
    else:


        "Eu decidi ser só amigo dela. Mas não quer dizer que a gente não pode se divertir juntos na praia."

    python:
        if renpy.android:
            praia_nona = PythonSDLActivity.pegaPraiaNona()

    "..."

    if praia_nona:

        "{b}Você já pagou para levar a [na] para a praia uma vez. Mas nesta linha do tempo você ainda não levou ela.{/b}"

        "{b}Como em CH não é preciso pagar duas vezes pela mesma coisa, você pode rever o evento sem pagar novamente.{/b}"

        jump praia_especial_nona_evento
    else:


        jump praia_especial_grana

label praia_especial_grana:

    "Pra fazer o que eu tô pensando, vou precisar de mais ou menos uns {b}C$ 200{/b}"

    python:
        if renpy.android:
            cash = PythonSDLActivity.pegaCash()

    $ renpy.choice_for_skipping()

    "Eu tô com {b}C$ [cash]{/b}..."

    $ renpy.choice_for_skipping()

    if cash >= 200:

        "Eu tenho dinheiro suficiente."

        python:
            if renpy.android:
                praia_priscila = PythonSDLActivity.pegaPraiaPriscila()

        menu:

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [c]?" if cash >= 200 and praia_escolhida == "priscila" and not praia_priscila:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaPriscila()
                        PythonSDLActivity.registraEvento("praia_especial_priscila","a","a")

                    renpy.block_rollback()

                jump praia_especial_priscila_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [s]?" if cash >= 200 and praia_escolhida == "sayuri" and not praia_sayuri:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaSayuri()
                        PythonSDLActivity.registraEvento("praia_especial_sayuri","a","a")

                    renpy.block_rollback()

                jump praia_especial_sayuri_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [g]?" if cash >= 200 and praia_escolhida == "julia" and not praia_julia:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaJulia()
                        PythonSDLActivity.registraEvento("praia_especial_julia","a","a")

                    renpy.block_rollback()

                jump praia_especial_julia_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [d]?" if cash >= 200 and praia_escolhida == "diana" and not praia_diana:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaDiana()
                        PythonSDLActivity.registraEvento("praia_especial_diana","a","a")

                    renpy.block_rollback()

                jump praia_especial_diana_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com o [n]?" if cash >= 200 and praia_escolhida == "nathan" and not praia_nathan:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaNathan()
                        PythonSDLActivity.registraEvento("praia_especial_nathan","a","a")

                    renpy.block_rollback()

                jump praia_especial_nathan_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [w]?" if cash >= 200 and praia_escolhida == "sofia" and not praia_sofia:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaSofia()
                        PythonSDLActivity.registraEvento("praia_especial_sofia","a","a")

                    renpy.block_rollback()

                jump praia_especial_sofia_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [na]?" if cash >= 200 and praia_escolhida == "natasha" and not praia_natasha:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaNatasha()
                        PythonSDLActivity.registraEvento("praia_especial_natasha","a","a")

                    renpy.block_rollback()

                jump praia_especial_natasha_evento

            "Usar {b}C$ 200{/b} para viver o evento na praia com a [h]?" if cash >= 200 and praia_escolhida == "nona" and not praia_nona:

                python:
                    if renpy.android:
                        PythonSDLActivity.compraPraiaNona()
                        PythonSDLActivity.registraEvento("praia_especial_nona","a","a")

                    renpy.block_rollback()

                jump praia_especial_nona_evento
            "Deixar para outra hora":


                "Deixa quieto. Não vou gastar essa grana agora. Deixa pra outro dia."

                show screen cidade_tela
                with dissolve

                pause
    else:


        label praia_especial_pobre:

            "Com isso não vai dar pra pagar tudo o que eu quero fazer."

            mc desculpa "..."

            show black with Dissolve(1.0)

            p lecionando "Ixi. O [mc] tá pobre que só ele..."

            p "Não esqueça de colocar o [mc] para trabalhar sempre que possível para juntar grana para essas horas."

            p rindo "Mas {b}você{/b} pode ajudar o [mc] com dinheiro do seu mundo."

            p "Além de ver essa incrível história, você ainda contribui com o desenvolvimento de CH."

            p "Você quer comprar Celebrity Reais e ajudar o [mc]?"

            menu:
                "Sim. Tô com uma graninha sobrando aqui.":


                    p rindo "Que bom!"

                    call comprar_cash from _call_comprar_cash_6

                    p "Vou mandar o [mc] de volta no tempo para ele poder continuar com os afazeres dele."

                    hide black with dissolve

                    jump praia_especial_grana
                "Não. Tô pobre igual a ele...":


                    p rindo "Não esquente."

                    p "Trabalhe sempre que possível no bar e vá juntando seus Celebrity Reais. Logo logo você já vai estar com grana suficiente."

                    p "Demora, mas vale a pena!"

                    hide black with dissolve

                    "Vou continuar com os bicos e depois eu chamo ela."

                    show screen cidade_tela
                    with dissolve

                    pause





label praia_especial_priscila_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("pex1_save", extra_info="pex1_save")

    $ estou_na_cidade = False

    $ praia_priscila_local = True

    "Certo. Então eu vou fazer isso. Vou preparar algo bem bacana e avisar a Pri."

    "Primeira coisa eu preciso ir lá na loja de roupas e comprar um biquini bem legal pra ela."

    mc zerado "Vão me passar a faca de novo, mas é a vida."

    scene black with Dissolve(1.0)

    "..."

    scene boutique roupa with Dissolve(1.0)

    mc desconfiado "Hmm..."

    "Tem uns biquinis aqui... mas não sei qual ela vai gostar."

    ate "Boa tarde."

    mc normal "Oi."

    show atendente normal with dissolve

    ate "Posso ajudar com alguma coisa? Você tá procurando um biquini?"

    mc "Sim. É pra minha namorada."

    ate "Qual é o estilo dela? Ela prefere algo mais reservado ou mais ousado?"

    menu:
        "Ela é uma modelo e veste coisas ousadas.":


            mc charmoso "Ela trabalha como modelo. É rotina pra ela usar coisa ousada, mesmo na frente das pessoas."

            ate "Puxa, que partidão o senhor arranjou, hein. Você pode falar quem é?"

            mc "Melhor não. Ela prefere que seja segredo por enquanto."

            ate "Entendi. Que relacionamento cheio de mistério."

            mc "Haha..."
        "Eu sinceramente não faço ideia.":


            mc desconfiado "Olha... não tenho ideia. Ela é uma garota bem legal, mas não qual tipo ela ia preferir."

            ate "Hmm... isso não ajuda muito."

            mc normal "Ela tem uma roupa que ela gosta que tem um decote até bem grande."

            ate "Entendi. Então ela deve preferir uma roupa mais ousada."

    ate "Você sabe qual é o tamanho dela?"

    mc envergonhado "Hmm... ela é normal, quase do meu tamanho, é magra. Mas com um corpão."

    ate "Entendi. Acho que eu tenho um biquini perfeito pra ela. Ah! Você sabe que cor que ela gosta?"

    menu:
        "Rosa":


            mc desconfiado "Acho que é rosa..."

            ate "Puxa, não tenho essa cor. Mas tenho uma parecida."
        "Roxo":


            mc charmoso "Ela gosta de roxo. Certeza."

            ate "Muito bom! Eu tenho um roxo aqui que ela vai amar."
        "Vermelho":


            mc desconfiado "Se eu não me engano é vermelha."

            ate "Uma pena, não tenho essa cor. Mas tenho outra aqui que ela vai gostar."
        "Sei não...":


            mc envergonhado "Sei não..."

            ate "Fica tranquilo que eu tenho um aqui que ela vai amar."

    mc normal "Beleza. Valeu."

    ate "Vou pegar."

    mc "Ah! Você pode pegar um shorts de praia pra mim também?"

    ate "Claro, senhor. Você vai querer provar?"

    mc "Não precisa."

    ate "Então vou pegar os dois e levo no caixa."

    mc "Tá."

    hide atendente with dissolve

    "Comprar coisas pros outros não é fácil..."

    scene boutique caixa with Dissolve(1.0)

    mc normal "Quanto ficou?"

    ate "Eu nem sabia e esse biquini tá em promoção. Tudo ficou R$ 150."

    mc surpreso "!"

    mc zerado "Tá aqui."

    ate "Obrigada, volte logo."

    "Facada..."

    "Mas tomara que ela goste."

    scene black with dissolve

    scene mc onibus with Dissolve(1.0)

    "Vou passar no hotel que ela fica e deixar com o porteiro. Vou escrever um recado também pra ela me encontrar na praia."

    "Acho que ela vai curtir a surpresa."

    scene black with dissolve

    scene hotel recepcao with Dissolve(1.0)

    "..."

    mc normal "Então você só liga pro apê dela e fala que tem uma coisa pra ela aqui. Não fala que fui eu."

    "Porteiro" "Eu não sei quem é o senhor mesmo."

    mc zerado "..."

    mc normal "Obrigado."

    "Certo. Agora eu vou pra praia me preparar pra encontrar ela. Espero que dê certo..."

    play sound "audio/som_13_praia.mp3"

    scene ilha praia with Dissolve(1.0)

    pause

    "Agora é só esperar ela."

    "..."

    "O porteiro falou que ela tava lá. Então não tem erro."

    "..."

    "..."

    "Daqui a pouco já é meio dia. Será que ela não vai conseguir vir?"

    "Ela podia pelo menos ter me avisado por mensagem."

    "Será que eu mando algo pra ela? Só que daí ia estragar um pouco a magia da surpresa... sei lá..."

    menu:
        "Enviar uma mensagem pra ela":


            mc desculpa "Deixa eu perguntar se acont-"

            "???" "Perguntar o que?"
        "Continuar esperando":


            mc concentrando "Não vou encher o saco. Ela já deve tá chegando."

            "???" "Tá mesmo."

    mc surpreso "!"

    scene priscila_praia_chegou with Dissolve(2.0)

    pause

    c "Oi, [mc]."

    mc surpreso "O-o-oi..."

    c "Obrigada pelo presente."

    menu:
        "Eu que agradeço...":


            mc tarado "Eu que agradeço..."

            c "Agora eu entendi. Esse presente era pra mim ou pra você?"

            mc "Eu queria dizer que é pra você... mas..."

            c "Bobo... eu adorei. Fico feliz que você tá gostando também."

            mc safado "Muito."
        "Você ficou linda nele.":


            mc surpreso "Você ficou linda nele!"

            c "Fiquei, né? Também achei."

            c "Essa é a vantagem de fazer academia, yoga, dieta e tratamento toda semana."

            mc envergonhado "Não é fácil..."

            c "Fácil não é. Mas quando a gente deixa nosso namorado com essa cara, vale à pena."

            mc "Hehe..."

    c "Eu nem acreditei quando eu vi que era coisa sua. O porteiro falou que tinha uma roupa pra mim lá em baixo. Daí achei que fosse de trabalho."

    c "Quando li sua cartinha falando pra te encontrar aqui, fiquei tão feliz."

    mc charmoso "Eu achei que a gente precisava de um tempo só nosso depois de tudo o que tá rolando."

    c "Eu também! Fico com saudades da gente sair mais, só que eu sei que não é fácil. Você tá sempre correndo, né?"

    mc envergonhado "Sim, mas você também tá haha..."

    c "Verdade. Mais eu tô sempre pensando em você, [mc]. Eu não vejo a hora de ver você e sair com você de novo."

    mc charmoso "Eu também, [c]."

    c "Só que hoje eu tô animada! O que você quer fazer?"

    mc "Deixa eu pensar."

    mc "E se a gente for até o quiosque lá no meio do mar?"

    c "Legal! Tem umas cadeiras que a dá pra gente tomar sol lá."

    mc "Fechou. As senhoritas na frente."

    c "Com licença."

    scene black with Dissolve(1.0)

    scene ilha praia_gazebo with Dissolve(1.0)

    mc normal "Só aqui mesmo pra construírem tudo isso e deixarem pra gente usar."

    c "Verdade. Essa ilha é realmente diferente."

    c "Eu já visitei vários lugares em muitos países. E é difícil encontrar um lugar igual este aqui."

    c "Opa!"

    scene priscila_praia_gazebo with Dissolve(2.0)

    pause

    c "Aaahhh.... que delícia, [mc]..."

    c "Não lembro a última vez que eu tive tempo pra colocar um biquini e deitar tranquila assim."

    menu:
        "Você não coloca biquini nos ensaios?":


            mc normal "Nos ensaios que você faz não rola foto de biquini?"

            c "É o que mais rola, né! Haha... mas é bem diferente."

            mc "A é?"

            c "Com certeza. Quando a gente tá trabalhando as coisas, tudo mesmo, dá outro sentimento."

            c "Quando eu tô em um ensaio, eu preciso ficar pensando em poses, em passar sensualidade na medida certa. Tudo isso é muito complicado."

            mc envergonhado "Não é só ficar toda gostosa lá?"

            c "Quem dera! Hahaha!"
        "Que bom que você tá curtindo.":


            mc charmoso "Fico feliz que você tá curtindo."

            c "Eu precisava disso, [mc]. Eu precisava de um tempo longe das câmeras, das luzes e da pressão também eu acho."

            mc desculpa "Tudo isso é muito cansativo, né?"

            c "Sim. Mas aqui não tem nada disso. Só o sol e a gente."

            mc normal "Verdade."

    c "Mas e o seu trabalho? Como as coisas tão indo?"

    mc envergonhado "O meu? Não tem nada de divertido no meu trabalho."

    c "Para de ser bobo. Claro que tem. Me conta."

    mc "Você sabe que eu não sou uma celebridade igual você. Eu só corro atrás de celebridades haha..."

    c "Você é um {b}Caçador de Celebridades{/b}? Ah! Pensando bem... eu acho que caí na sua rede... então você realmente é um caçador de celebridades."

    c "Epa! Espero que seja de celebridade, no singular. Né?!"

    mc envergonhado "Haha... claro!"

    if sayuri_namoro or maria_namoro or julia_namoro:

        "Caralho... que merda... se ela soubesse..."
    else:


        "A Pri é minha única namorada. Tô salvo nessa."

    c "Eu nem sempre tô com você, mas eu tenho gente te seguindo."

    mc surpreso "Como é?!"

    c "Bobo! rs..."

    mc envergonhado "..."

    c "Por mais que eu gostasse de ficar aqui o dia todo, não vou fazer você ficar me olhando."

    mc safado "Pra mim não seria problema nenhum."

    c "O que você quer fazer agora?"

    mc "Eu-"

    c "Ah! Eu deixei uma coisa com o rapaz do quiosque. Eu vou pegar lá!"

    mc normal "Tá legal. Vamo lá."

    scene black with Dissolve(1.0)

    scene ilha praia with Dissolve(1.0)

    c "Espera aqui um segundinho que eu vou pegar."

    mc normal "Ok."

    "O que será que ela deixou no quiosque? Por que eu não podia ver?"

    "..."

    c "[mc]! Olha!"

    scene priscila_praia_bola with Dissolve(1.0)

    pause

    mc surpreso "Aquela bola!"

    c "Minha bolona!"

    mc envergonhado "Haha... você guardou desde aquele dia? Ainda tem ela?"

    c "Claro! Foi a primeira bolona que eu ganhei. Eu fiquei tão feliz aquele dia quando você me deu ela."

    mc "Quando você falou isso daquela vez eu não acreditei muito, sabe..."

    c "Por que é um tonto! Eu até pedi pra [a] encher ela algumas vezes. E se furar alguma coisa eu mando arrumarem."

    mc "Não compensa... melhor comprar o-"

    c "A bolona é minha eu faço o que eu quero! Me deixa!"

    mc "Ok..."

    c "Agora vai pra lá. Vamos jogar."

    mc normal "Tá."

    scene priscila_praia_bola_volei with Dissolve(1.0)

    c "Meu pai nunca jogou bola comigo."

    mc desconfiado "Sério? Por que?"

    c "É. Tipo... ele dizia que jogar bola não é coisa de menina. Ele me comprava bonecas, mas ele não gostava de brincar com elas."

    c "Daí eu acabava brincando sozinha, porque minha mãe tava sempre trabalhando."

    mc normal "E suas amigas?"

    c "Eu tinha, claro, mas meu pai não gostava muito de bagunça, então eu só via elas na escola, então quase que a gente nem brincava."

    c "Depois eu conheci a [a] e a gente virou amigas. Ela é mais velha, claro, mas ela se interessou por mim, sei lá porquê."

    c "Ela vivia dizendo que eu era linda. E graças a ela que eu acabei participando de um concurso de modelo pra adolescente."

    mc charmoso "Foi assim que você começou sua carreira?"

    c "Foi, acredita? Eu venci o concurso, lógico. Daí os juízes vieram falar comigo depois."

    c "[mc], pera. Eu não vou conseguir jogar essa bolona pela rede. Vem aqui."

    mc normal "Haha... tá."

    scene priscila_praia_volei with Dissolve(1.0)

    c "Agora sim. Pega!"

    mc normal "Opa!"

    mc "Mas continua contando a história."

    c "Ah tá. Então... os juízes me chamaram pra uma sala lá e quiseram saber mais de mim."

    c "Eles me perguntaram um monte de coisa e me deram umas roupas pra vestir lá."

    c "Depois eles falaram que eu era linda e muito carismática, engraçada e tinha a energia certa pra ser modelo."

    c "Eu conversei com a [a] e ela disse que eu não podia perder essa chance. Ela disse que ia ser minha agente pra eu não me preocupar com nada."

    c "Eu lembro que ela veio aqui pra capital conversar com algumas pessoas e depois voltou dizendo que tava tudo certo."

    c "Ela tinha arranjado um primeiro ensaio pra mim."

    c "{i}puf puf{/i}"

    c "Cansei."

    mc concentrando "Eu também..."

    scene priscila_praia_bola_sentada with Dissolve(1.0)

    pause

    c "Ufa."

    menu:
        "Pedir para ela continuar a história":


            "Não quero cortar ela na metade."

            mc normal "E aí?"

            c "Ah... {i}puf puf{/i}"

            c "Daí eu vim pra cá com ela. Eu tirei algumas fotos."

            c "Na época eu ainda era menor, então era coisa bem tranquila, por mais que alguns me pedissem pra mostrar um pouco mais."

            mc "E a [a]?"

            c "Ela sempre colocou minha carreira na frente. Me pedia pra esquecer algumas coisas, que o mercado era difícil e eu tinha que me esforçar."

            mc desculpa "Sei..."

            c "Mas nunca fizeram nada comigo. A grande maioria dos contratantes são super profissionais. E a [a] sempre tava lá pra me proteger."

            mc normal "Legal."

            c "E daí foi isso. Uma boa história, né?"

            mc charmoso "Com certeza. E incrível como você nunca parou."

            c "Verdade..."
        "Tá bom por agora":


            "Acho que eu já matei ela de fôlego."

            "Bora tomar alguma coisa."

    mc charmoso "E se agora a gente tomar alguma coisa ali no quiosque? A gente merece depois do jogo."

    c "Com certeza! Eu aceito!"

    mc "Mas eu tô pagando tudo, hein?"

    c "Que cavalheiro. Eu aceito, senhor."

    mc "Então vem."

    scene priscila_praia_quiosque with Dissolve(1.0)

    mc "O que você vai querer?"

    c "Hmm... acho que alguma coisa com álcool."

    mc "Sério? Você pode? Eu lembro que você disse que não podia por coisa de contrato e talz."

    c "Xiu, [mc]. Se você beber comigo eu tomo."

    menu:
        "Eu prefiro que a gente beba só um suco.":


            mc "Sem querer ser chatão, mas é melhor a gente ficar só no suco mesmo."

            c "Sério, [mc]?! Mas eu tava junto forças pra isso..."

            mc "Relaxa. Bebida não tem nada de diferente. A gente não precisa disso."

            c "O-obrigada... não queria estragar as coisas com meu trabalho. Eu não quero que nossa relação gire em torno de mim."

            mc "Pode ficar tranquila. Você é muito bacana e atenciosa, Pri."

            c "Você acha?"

            mc "Sim. Além de fofa, linda e gostosa."

            c "Obrigada... linda e gostosa eu sabia, mas fofa ainda tenho minhas dúvidas."

            mc "Vou gravar da próxima vez que você tiver com a bolona pra você ver como você é fofa."

            c "Haha... tá bom."
        "Ok. A gente fica alto juntos.":


            mc "Opa! Então vou te acompanhar e a gente fica alto juntos."

            c "Eba!"

            mc "Oi, com licença. Me vê um drink bacana pra gente por favor. Pode escolher um que você ache bom."

            "Atendente" "Opa, pode deixar."

            "..."

            "Atendente" "Aqui. No capricho. E aqui a conta."

            mc "Obrigado."

            c "Deixa eu pegar o meu. Licença."

            scene priscila_praia_bebida with Dissolve(1.0)

            pause

            c "Olha, [mc]. Tem um peixinho na taça. Que fofinho."

            mc normal "Bonitinho mesmo."

            c "Obrigada por pedir pra gente."

            mc charmoso "Aproveita."

            c "Tá uma delícia."

    c "Quando a gente veio aqui na praia da outra vez foi incrível, mas eu tô me sentindo bem diferente dessa vez."

    mc "Sério?"

    c "Eu acho que eu me apaixonei por você desde aquela noite no bar, sabia?"

    c "Você mexeu comigo, eu me senti muito especial aquela noite."

    mc "Que bom. Eu gostei muito também."

    c "Daí quando a gente veio pra cá, eu queria muito ficar com você. Meu coração tava super apertado!"

    c "Eu ainda não tinha certeza se você gostava de mim só como amiga ou se você também queria alguma coisa a mais."

    c "E tinha tanta coisa acontecendo."

    scene priscila_praia_quiosque with Dissolve(1.0)

    mc "Eu sempre soube que você era uma garota especial. Você é sincera e não tem medo de mostrar o que tá sentindo."

    mc "O que eu vejo é que as pessoas têm muito medo de falar o que elas tão sentindo."

    c "É que as pessoas não sabem como os outros vão reagir, [mc]."

    mc "Como assim?"

    c "Quando você gosta de alguém, ou, tipo assim, quer impressionar uma pessoa, você tem medo que ela não goste de algo que você falar."

    c "Daí as pessoas têm medo de falar a verdade. Isso é normal."

    mc "Sei..."

    c "Mas isso que é incrível em você. Eu sinto que não importa o que eu falar, você nunca vai me julgar."

    c "Você sabe tanta coisa sobre mim, e mesmo assim você continua me olhando com o mesmo carinho. Isso dá coragem pra gente falar com você."

    c "As pessoas vivem julgando os outros. Mas você não é assim. Você escuta e deixa a gente ser quem a gente é. Isso é, tipo... libertador."

    c "Eu já contei coisas pra você que nunca contei nem pra [a], nem pros meus pais. É tipo um poder seu."

    mc "Nunca tinha pensado nisso..."

    c "Continue sempre assim, [mc]. Eu tenho muita sorte de ter agarrado você."

    mc "Haha..."

    c "Ficou seu jeito né?"

    mc "..."

    "Talvez agora seja uma boa hora pra dar um beijo nela... Será que eu devo?"

    menu:
        "Tentar beijar ela":


            mc "Se tudo isso que você falou é verdade... talvez eu mereça um prêmio."

            c "Um prêmio? Qual?"

            mc "Deixa eu chegar mais perto de você, porque é segredo."

            c "Sei..."

            scene black with Dissolve(1.0)

            mc "Meu prêmio..."

            scene priscila_praia_quiosque_beijo with Dissolve(2.0)

            pause

            c "Hmmm... mas o prêmio é pra quem?"

            mc "Pra mim, ué."

            c "Se você tá falando..."

            window hide

            pause
        "Deixar para outra hora":


            "Melhor não arriscar agora. As coisas estão indo super bem."

            c "Não precisa ficar sem jeito assim, bobo."

            c "Eu não devo ser a única que fala que você é um cara estranho. Tenho certeza."

            mc "Ei..."

            c "Hahaha! Sabia!"

            c "Mas não quero ficar te deixando com vergonha só pra rir da sua cara. Vamos pra areia!"

            mc "Tá."

    scene black with Dissolve(1.0)

    scene ilha praia_quiosque with Dissolve(1.0)

    c "Eu trouxe uma esteira pra ficar na areia. Mas se você achar chato..."

    mc charmoso "Claro que não. Eu quero que você aproveite o máximo."

    c "Tá... Então senta comigo."

    scene priscila_praia_deitada with Dissolve(1.0)

    pause

    mc surpreso "!"

    c "Que foi?"

    mc envergonhado "Acho que essa ideia foi melhor do que você imaginava."

    c "Haha... entendi. Você tem quantos anos? 12?"

    mc "Me deixa... a culpa é sua..."

    c "Você que comprou o biquini pra mim."

    mc "Mas a culpa é sua de ficar tão bem nele."

    c "Bom... se você pensar... as pessoas pagam um dinheirão pra me ver assim. E você vê de graça."

    mc safado "..."

    c "Ah! Isso me deu uma ideia!"

    mc desconfiado "O que?"

    c "Vamos fazer um ensaio na praia. Eu faço poses e você tira foto com seu celular mesmo. Daí você fica com um book exclusivo meu. Topa?"

    mc charmoso "Com certeza."

    c "Então pode começar, fotógrafo."

    mc charmoso "Pera..."

    show white with Dissolve(0.2)
    hide white with Dissolve(0.2)

    mc "Pronto."

    c "Agora assim..."

    scene priscila_praia_pose1 with Dissolve(2.0)

    pause

    mc "Perfeita..."

    c "Tá aprendendo como os fotógrafos fazem já."

    mc "Haha..."

    show white with Dissolve(0.2)
    hide white with Dissolve(0.2)

    mc "Tá linda."

    c "Pega uma por trás agora."

    mc envergonhado "T-tá."

    c "Não precisa ter vergonha, [mc]. É o seu trabalho pegar os ângulos mais sensuais que você puder. É o que pessoal quer ver, entende?"

    scene priscila_praia_pose2 with Dissolve(2.0)

    pause

    mc "Incrível. Seu corpo é incrível, Pri."

    c "Não é pra ficar só secando. Tira a foto também."

    mc "Opa."

    show white with Dissolve(0.2)
    hide white with Dissolve(0.2)

    mc "Ficou perfeita."

    c "Agora assim."

    scene priscila_praia_pose3 with Dissolve(2.0)

    pause

    mc surpreso "!!"

    c "A foto..."

    show white with Dissolve(0.2)
    hide white with Dissolve(0.2)

    mc safado "Pronto..."

    c "E mais uma. Vem bem pertinho..."

    scene priscila_praia_pose4 with Dissolve(2.0)

    pause

    "Uou... ela tá muito sexy..."

    c "[mc]?"

    mc "Opa!"

    show white with Dissolve(0.2)
    hide white with Dissolve(0.2)

    mc envergonhado "Pronto..."

    c "Não tá aguentando me ver assim?"

    mc "Não tá fácil..."

    scene black with Dissolve(1.0)

    c "Acho que você merece mesmo um bônus pelo bom trabalho."

    mc surpreso "!"

    scene priscila_praia_beijo with Dissolve(2.0)

    pause

    mc "Que delícia de bônus..."

    c "Aproveita. Você mereceu, bobo..."

    window hide

    pause

    scene priscila_praia_despedida with Dissolve(1.0)

    pause

    c "Hmmm... que delícia, [mc]. Fiquei até meio sem ar..."

    mc "Você também me deixa assim."

    c "Já tá caindo o sol..."

    mc "Você gostou do passeio?"

    c "Muito... mas ainda não acabou, né? Você me acompanha até o hotel? A gente pode ir andando."

    mc "Claro."

    c "Obrigada, lindo. Vamos."

    mc "Vamo."

    c "Foi um dia incrível, [mc]. Obrigada por tudo. Quando der me chama pra outra coisa."

    mc "Com certeza."

    scene black with Dissolve(1.0)

    mc "Ah! E não esquece sua bolona."

    c "Nunca!"

    "..."

    $ tempo = 3

    jump call_cidade



label praia_especial_sayuri_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("sex1_save", extra_info="sex1_save")

    $ estou_na_cidade = False

    $ praia_sayuri_local = True

    "Com toda essa loucura que tá rolando na Cidade Chinesa, da [s], da [fen]... a gente quase nem namorou."

    "Pô! A gente merece esquecer um pouco a parte ruim e focar na gente. Ter um dia bacana, diferente."

    "É isso que eu vou fazer. Vou tentar esquecer tudo o que tá rolando e me divertir com a [s]. Finalmente namorar com ela de verdade."

    "Quem sabe assim ela até se abre mais comigo e eu entendo melhor o que tá rolando."

    "Não! Não posso pensar nisso hoje. O foco é curtir com ela. Aproveitar nosso namoro."

    "Vou fazer tudo perfeito. Comprar um maiô que eu ache que combine com ela. Depois vou fazer uma surpresa e marcar um encontro aqui."

    "A [s] é super reservada e sei que ela não tá acostumada com isso. Só tomara que ela não recuse."

    "Vai ser uma coisa super diferente pra ela. E eu vou ver ela de maiô..."

    mc safado "Esse sim é o objetivo..."

    "Agora bora pra loja de roupas ser esfaqueado... DE NOVO."

    scene black with Dissolve(1.0)

    call locomocao from _call_locomocao_14

    scene cidade centro1 with Dissolve(1.0)

    "Tem que ser aqui. A única loja de roupas que eu conheço."

    "Mano... devem ter tantas lojas aqui na capital. Até na ilha se pá. Eu tenho que tirar uma hora e conhecer outras."

    scene boutique roupa with Dissolve(1.0)

    "Certo... então preciso encontrar uma roupa de banho pra ela usar."

    "A [s] é meio tímida, então é melhor eu não exagerar. Se fosse a [c] ou a [g], ou até outra garota menos títimda."

    ate "Olá, senhor."

    mc normal "Opa. Bom dia."

    show atendente normal with dissolve

    ate "Bom dia. É bom ver o senhor novamente."

    menu:
        "É bom ver você de novo também.":


            mc charmoso "Digo o mesmo. Você é uma das causas que eu gosto tanto de comprar aqui."

            ate "O senhor gosta do meu atendimento?"

            mc "Isso também..."

            ate "Senhor..."
        "Quando eu vejo você minha carteira treme.":


            mc preocupado "Deus... minha carteira tem medo de você. Quando você chega ela já começa a tremer."

            ate "Que exageiro, senhor."

            mc concentrando "Fala isso pro dono do banco que cobra os juros do cheque especial."

            ate "..."

    mc normal "Bom. Eu queria comprar um traje de banho pra minha namorada."

    if praia_priscila_local:

        ate "O senhor não comprou um biquini esses tempos atrás?"

        mc surpreso "Ah!"

        mc envergonhado "É... era pra outra pessoa."

        ate "Não se preocupe, senhor. Só estou falando que lembro de você."

        mc "Entendi..."

    ate "E como ela é? Pode me falar um pouco sobre ela?"

    mc normal "Ela é uma atleta e é uma pessoa reservada, tímida. Nem sei como vou fazer ela ir pra praia ainda hehe..."

    ate "Entendi. Então é melhor a gente não pegar pesado. Vamos com algo que cubra mais."

    menu:
        "Isso. Ela vai se sentir melhor.":


            mc normal "Bacana. Não quero que ela se sinta desconfortável."

            ate "O senhor é um cavalheiro."

            mc "Haha... não adianta nada preparar uma surpresa se o surpreendido não se sentir bem, né?"

            ate "Não é todo homem que pensa assim... o que é uma pena."
        "Infelizmente é o jeito...":


            mc envergonhado "Infelizmente, tem que ser assim com ela..."

            ate "Não se preocupe. Não é porque tem mais pano, que não pode ser sexy e provocante."

            mc desconfiado "Sério?"

            ate "Claro. Às vezes esconder é mais interessante do que mostrar."

            mc "Se você diz..."

            ate "Pode confiar em mim."

    ate "Eu acho que tenho uma peça que ela vai gostar. E o preço cabe no bolso."

    mc normal "Sério? Quanto é?"

    ate "Na promoção sai por apenas C$ 200."

    mc zerado "Só pode tá brincando..."

    ate "É um maiô de grande qualidade, senhor. Pode ter certeza que vai valer muito à pena."

    ate "Ele não vai deixar ela descorfortável e nem se sentindo exposta demais, mas vai mostrar bem as curvas dela."

    mc envergonhado "Do jeito que você fala, parece que a gente tá armando uma armadilha pra ela."

    ate "Talvez... agora venha até o caixa."

    hide atendente with dissolve

    mc angustiado "..."

    scene boutique caixa with Dissolve(1.0)

    mc concentrando "Tá aqui o dinheiro."

    ate "Tenha um bom passeio e espero que vocês aproveitem a praia."

    mc "Valeu. Até a próxima."

    ate "Espero que seja logo."

    "Não sei se eu quero que seja ou não..."

    scene black with Dissolve(1.0)

    scene cidade centro4 with Dissolve(1.0)

    "Certo... a entrada da Cidade Chinesa fica aqui perto. É nesse ponto que ela se liga com o centro."

    scene cidade centro6 with Dissolve(1.0)

    "Agora mais um pouco..."

    scene black with Dissolve(1.0)

    scene chinatown geral with Dissolve(1.0)

    mc concentrando "Ufa... que caminhada."

    "Meu plano é deixar o presente dela com um cartão no portal e daí aquela mina da entrada entrega pra ela."

    scene chinatown caminho with Dissolve(1.0)

    "É aqui perto."

    scene chinatown portal with Dissolve(1.0)

    "Isso. Agora vou jogar lá perto e sair correndo. Tomara que ela veja."

    mc surpreso "UPA!"

    scene chinatown portal with vpunch

    "Caiu lá! Agora TCHAU!"

    "..."

    show xiangu normal with dissolve

    xu "Hmm..."

    scene black with Dissolve(1.0)

    "..."

    $ tempo = 2

    scene mapa cidade_tarde with dissolve

    mc concentrando "Ufa... cheguei..."

    scene mc parque_sentado with Dissolve(1.0)

    mc "Caraca... que dia. Fiquei o tempo todo andando praticamente."

    mc "Isso quando eu não tava correndo da maluca com a espada. Como pode?"

    "Agora é torcer pra [s] receber meu presente. Se ela receber ela v-"

    "{i}Trr trrr{/i}"

    mc "É ela!"

    scene mapa cidade_tarde with dissolve

    mc normal "A-alô? [s]?"

    s "O-o-oi..."

    menu:
        "Tudo bem, amor?":


            mc charmoso "Tudo bem com você, amor?"

            s "A-a-a-amor? T-t-tudo bem..."

            "Ela fica fofa toda envergonhada desse jeito."
        "Como você tá?":


            mc normal "Como você tá? Tudo bem?"

            s "Estou, sim. E você?"

            mc "Que bom. Eu também."

    mc charmoso "Recebeu meu presente?"

    s "S-sim... p-por isso liguei..."

    mc "O que você achou?"

    s "T-tudo bem... e-eu aceito..."

    mc preocupado "Tá tudo legal? Se você não quiser, tudo bem, ok?"

    s "N-não é isso... é só que... eu recebi o presente e experimentei..."

    mc normal "E? O que achou?"

    s "E-eu achei ele lindo. É da minha cor preferida! Nem sei como você descobriu..."

    mc charmoso "Eu sempre vejo você vestindo essa cor, então pensei que você ia gostar."

    s "É verdade... Obrigada, [mc]."

    mc "Você leu meu cartão? Eu queria que a gente tivesse um dia pra gente!"

    s "E-eu também quero. Vai ser muito bom. P-por mim pode ser amanhã."

    mc "Perfeito! Então amanhã cedo te encontro aqui na praia. Você sabe chegar?"

    s "Sim... eu sei."

    mc "Tá legal. Até amanhã então. Beijo."

    s "B-b-beijo..."

    "Tudo correu bem."

    scene black with Dissolve(1.0)

    "Amanhã vai ser um grande dia!"

    $ dia += 1
    $ tempo = 1

    scene ape_cama with Dissolve(1.0)

    "Hmmm..."

    "Nossa... dormi tão ansioso com hoje que nem sonhei com aquela desgraça de sempre."

    "Ainda são 8h... mas acho que já vou me preparar e sair. A [s] tem cara que chega cedo."

    scene black with Dissolve(1.0)

    "..."

    play sound "audio/som_13_praia.mp3"

    scene ilha praia with Dissolve(1.0)

    mc normal "Uaahh! A praia! Dia de folga! E com minha namorada linda e deliciosa!"

    "Vou comprar algo pra ela beber quando chegar. Quero que o dia já comece perfeito pra ela."

    "Tô ansioso pra ver como ela vai tá. Nem eu vi a peça que eu comprei... a moça só me deu embrulhado."

    "Eita, porra. E se for um-"

    mc desconfiado "Hm? Quem tá ali?"

    scene sayuri_praia_gazebo with Dissolve(1.0)

    pause

    mc surpreso "!"

    "A [s] já chegou... é a cara dela chegar cedo nos lugares. Se pá ela até pensou a mesma coisa que eu e ia comprar algo pra gente beber."

    "Deixa eu chamar ela."

    "Opa opa opa... pera... talvez seja melhor deixar ela lá mais um pouquinho..."

    menu:
        "Chamar ela":


            "Preciso parar de pensar besteira."
        "Continuar olhando":


            "Pensando bem... não tenho nenhuma pressa."

            window hide

            pause

            "Isso sim que é uma praia bonita."

            "..."

            "Acho que já sequei demais."

    mc normal "Oi, [s]. Bom dia."

    s "[mc]!"

    s "Ah, [mc]... Bom dia... estava procurando o vendedor deste quiosque, mas não consigo ver ninguém..."

    mc "Ele deve ter dado uma saidinha."

    s "V-verdade..."

    scene sayuri_praia_gazebo_falando with Dissolve(1.0)

    pause

    s "..."

    mc desconfiado "Que foi? Tudo bem?"

    s "O-o que você achou?"

    mc "Hm?"

    s "D-de como seu p-presente ficou em mim..."

    mc surpreso "Ah!"

    menu:
        "Você ficou uma delícia nele.":


            mc safado "Você ficou uma delícia nele."

            s "Ah! ..."

            mc "Tô falando sério."

            s "T-tá... e-eu..."

            mc charmoso "E fica melhor ainda com você envergonhada desse jeito."

            s "V-você é mau, [mc]..."

            mc charmoso "Eu quero que você saiba que eu olho pra você como uma mulher. Você é minha namorada."

            s "Ai..."

            mc envergonhado "Mas não quero que você fique toda vermelha, só se for de se divertir no sol hehe... o que você achou dele?"

            s "Ah... eu..."
        "Você ficou linda. Combinou muito com você.":


            mc charmoso "Você ficou linda. Ele combinou muito com você eu achei."

            s "S-sério mesmo?"

            s "E-eu não estou acostumada a usar esse tipo de roupa. M-mais nas competições que tinha um traje parecido."

            mc "Não precisa ficar preocupada, você ficou perfeita nele."

            s "O-obrigada..."

    s "Eu adorei a cor."

    mc charmoso "Eu sabia que você era fã de vermelho. Só não sabia que era sua cor preferida."

    s "É sim."

    mc envergonhado "Não é à toa, né? É praticamente a cor da China."

    s "S-sim... eu tenho muito orgulho do meu país. Mas eu realmente acho a cor vermelha bonita."

    s "É uma cor muito viva e acho que por ser a cor do sangue, ela me dá muita determinação."

    mc charmoso "É a cor da paixão também."

    s "S-sim... é v-verdade..."

    mc "E como tá sendo pra você isso? Nosso namoro?"

    mc envergonhado "Eu sei que a gente não conseguiu aproveitar muito ainda com tantas coisas acontecendo..."

    mc normal "Por isso mesmo que eu quis marcar esse dia especial pra gente."

    s "E-eu fiquei muito feliz... mas meu coração ainda aperta e eu fico meio sem ar quando eu penso nisso."

    s "N-não quero que você fique triste... mas é uma coisa muito nova pra mim."

    mc charmoso "Relaxa. Vamos só dar tempo e curtir isso. Não é sempre que a gente passa por um momento assim."

    s "V-verdade..."

    mc desculpa "Bom, parece que ninguém vai aparecer. Vamos lá pro sol? Eu trouxe uma toalha pra você poder deitar."

    s "Claro. Vamos."

    scene ilha praia with Dissolve(1.0)

    mc normal "Acho que aqui é um bom lugar. Deixa eu colocar a toalha pra você. O bom é que aqui sempre parece uma praia particular."

    s "..."

    mc desconfiado "[s]?"

    scene sayuri_praia_sol with Dissolve(1.0)

    pause

    s "O sol tá tão bonito, [mc]..."

    mc "Verdade."

    s "Eu não lembro a última vez que eu fui na praia... deve ter sido com meus pais quando era criança... fazem tantos anos..."

    mc "..."

    s "O clima é totalmente diferente. Não sei, parece que a praia tem uma energia diferente do resto dos lugares."

    mc "Também acho isso."

    s "Eu sinto uma energia muito boa aqui. E poder passear com a pessoa que você gosta... é a-algo incrível, [mc]."

    menu:
        "Quem diria... você falando uma coisa dessas.":


            mc "Olha só... a [s], toda envergonhada, falando uma coisa dessas..."

            s "... E-eu... a-acho que foi por sua causa, [mc]. Você que me ajudou a ter mais confiança nas coisas..."

            mc "Que nada. Eu não fiz quase nada. Você quem chegou nisso, tá?"

            s "M-mas não sozinha... tenho certeza."

            mc "Se você quer me dar esse crédito, eu aceito."

            s "Hihi..."
        "É incrível mesmo.":


            mc "Poder curtir isso com você é incrível. Eu nunca pensei que a gente realmente ia chegar a namorar."

            s "E-eu também... e mesmo depois de a gente... sabe... eu ainda não acredito direito..."

            mc "Haha... só você, [s]."

            s "..."

    s "E agora? Vamos aproveitar esse sol?"

    mc normal "Com certeza. Pode deitar na toalha. Vou sentar aqui do seu lado."

    s "Tá."

    scene sayuri_praia_deitada with Dissolve(1.0)

    pause

    s "Hmmm... tá uma delícia aqui."

    mc normal "Que bom."

    s "E você vai ficar na areia mesmo?"

    mc normal "Tá bom aqui."

    s "Lembra da primeira vez que a gente se viu lá no templo?"

    mc charmoso "Claro que eu lembro. Você tava treinando fazendo uns movimentos muito bacanas lá."

    if sayuri_stalker:

        s "Eu tomei foi um susto quando você chegou sem falar nada."

        mc envergonhado "Haha... desculpa... mas eu não queria incomodar você."
    else:


        s "Foi bom que você pelo menos me chamou e eu não passei tanta vergonha."

        mc envergonhado "Eu lembro que eu tive que respirar fundo pra ter coragem de chegar e falar com você."

    s "Não sabia que você era tímido assim."

    mc "Bom... eu nunca tive muita sorte com as garotas."

    s "Esse é um problema q-que ficou pra trás..."

    mc charmoso "Fazendo piadinhas sobre isso assim? Pelo jeito não sou só eu que mudou, hein."

    s "N-não me faz ficar com vergonha de novo."

    mc envergonhado "Haha... desculpa..."

    scene sayuri_praia_deitada2 with Dissolve(1.0)

    pause

    s "Ah. Falando sobre nosso primeiro encontro. Você esperava que eu ia te mandar mensagem mesmo depois?"

    menu:
        "Não. De jeito nenhum.":


            mc envergonhado "Haha... com certeza não. Achei que você tinha pedido meu número só pra me dispensar."

            s "Que coisa horrível, [mc]!"

            mc "Mas é verdade. Você foi bem séria comigo na nossa primeira conversa, lembra?"

            s "Acho que eu fui... Só que eu não estava acostumada. Você entende, né?"

            mc "Hoje eu entendo, mas na época, né?"

            s "Verdade..."
        "Eu achei que sim.":


            mc normal "Eu achei que sim. Pelo menos era minha esperança, né?"

            s "Haha... pessoa confiante você."

            mc envergonhado "Acho que eu sou meio otimista..."

            s "Acabou dando certo."

    s "E daí eu passei aquela vergonha mandando aquela mensagem toda estranha!"

    mc normal "Haha! Verdade."

    s "Antes da gente se conhecer, eu pedia pra [g] responder tudo no meu lugar. Inclusive eu passava o telefone dela pras pessoas."

    s "Ela sempre me ajudou nisso. E no que era sobre as competições, eu sempre tive assessoria, né? Então eles respondiam tudo pra mim."

    mc charmoso "Então você realmente comprou o celular pra falar comigo..."

    s "Ei! N-não vale jogar isso na cara agora! Mas é verdade..."

    mc charmoso "Eu só achei isso incrível."

    s "Alguma coisa em você, do jeito que você falou comigo no templo... não sei explicar direito... você falou comigo de forma despretensiosa."

    mc desconfiado "Que que tem?"

    s "Isso me pegou meio desprevinida. Normalmente as pessoas não me tratam assim, com essa 'normalidade' toda."

    s "Quando você falou desse jeito comigo, eu achei muito interessante. Eu tive uma conversa 'normal' depois de tanto tempo..."

    s "D-daí meio que eu quis viver isso de novo... quem sabe..."

    mc charmoso "E acabou dando certo?"

    s "S-sim..."

    mc "Acho que você merece um prêmio por ser uma namorada tão fofa."

    s "P-prêmio?"

    mc "O que acha de uma massagem?"

    s "S-sério? Você sabe fazer?"

    if mc_massagem >= 5 and mc_massagem < 10:

        mc "Eu tô fazendo um curso. Tenho certeza que você vai gostar."

        s "A-acho que eu aceito então..."

    elif mc_massagem == 10:

        mc "Com certeza! Você vai pirar na minha técnica que tem até diploma."

        s "Uou..."
    else:


        mc "Na verdade eu não tenho uma noção tão técnica... mas eu vou dar meu melhor."

        s "E-eu não posso arriscar meu corpo, [mc]... eu preciso dele sempre 100%% entende?"

        mc envergonhado "Então tá legal... quem sabe um outro dia."

        s "V-verdade..."

    if mc_massagem >= 5:

        mc charmoso "Ok... se prepare pra melhor massagem da sua vida."

        s "O que eu faço?"

        mc "Só deitar de barriga pra baixo e deixe o resto com o mestre."

        scene sayuri_praia_deitada with Dissolve(1.0)

        s "T-tá bom... por favor toma cuidado, eu não posso arriscar me machucar, tá? Meu corpo é muito importante pro meu trabalho."

        mc "C-claro... pode deixar comigo."

        "Afe... só falta eu machucar a mina e tirar ela das competições ou dos treinamentos... foco, [mc]."

        mc "Vamos lá."

        scene sayuri_praia_massagem with Dissolve(1.0)

        pause

        mc "Vou começar pelos seus pés."

        "É o mais seguro."

        s "Hmm... s-só de sentir sua mão, j-já senti um choque..."

        mc "Calma que a gente tá só começando."

        s "..."

        mc "..."

        s "V-você está indo muito bem... você segura com força, mas sem machucar."

        mc "Isso se chama A Técnica Suprema da Massagem. Minha professora que me ensinou."

        s "P-puxa..."

        s "Ai... muito gostoso."

        mc "Agora eu vou correr com uma mão pelas suas pernas, tá? Não vai assustar."

        s "T-tá..."

        window hide

        pause

        scene sayuri_praia_massagem2 with Dissolve(1.0)

        pause

        s "Hmmm... tá realmente muito gostoso, [mc]..."

        mc "Só relaxe e curta o momento."

        s "Certo..."

        mc "Isso..."

        s "..."

        "Eu acho que tô indo muito bem. Ela tá curtindo e parece bem relaxada. Tô mandando bem."

        s "Ai, [mc]..."

        mc "Que foi?"

        s "Q-quando sua mão passa p-perto da m-minha... e-eu..."

        menu:
            "Continuar massageando a região toda.":


                mc "Não se preocupe. Você tá nas mãos de um profissional."

                s "A-ai... vo-você... ah!"

                mc "..."

                s "Ah..."

                s "E-eu... ah!"

                mc "Prooonto... tá mais relaxada?"

                s "S-sim...T-t-tô... o-obriga... da..."
            "Voltar para os pés.":


                mc "Não esquente. Deixa eu voltar pro seu pé."

                scene sayuri_praia_massagem with Dissolve(1.0)

                pause

                s "A-acho que é melhor... se não... é... é melhor..."

                mc "Pronto, pronto. Gostoso?"

                s "Muito..."

                s "..."

                mc "E aí? Relaxou?"

                s "Com certeza. Deixa eu me ajeitar."

        scene sayuri_praia_deitada with Dissolve(1.0)

        pause

        s "Eu adorei, [mc]... você fez um excelente trabalho. Eu não imaginava que você era bom de massagem assim."

        mc charmoso "Vivendo e aprendendo."

        s "Agora eu que vou mostrar uma coisa incrível pra você."

        mc surpreso "Sério?! O que?"
    else:


        s "Mas em compensação, eu vou te mostrar algo incrível."

        mc desconfiado "O que?"

    s "Eu quero que você lembre aquela vez no templo e veja meus movimentos... O-o que você acha?"

    mc charmoso "Com certeza. Vou achar incrível."

    s "Então se prepara. Vou começar!"

    scene sayuri_praia_movimento with Dissolve(1.0)

    pause

    s "Opa!"

    mc surpreso "UOU!"

    s "Isso é simples, [mc]. É só pra aquecer."

    s "Agora eu caio assim!"

    window hide

    pause

    scene sayuri_praia_movimento2 with Dissolve(1.0)

    pause

    mc surpreso "!"

    mc angustiado "Ai minhas costas!"

    s "Hihi."

    s "Agora um movimento de ponte."

    window hide

    pause

    scene sayuri_praia_movimento3 with Dissolve(1.0)

    pause

    mc charmoso "Esse parece bem artístico."

    s "É uma posição do Yoga. Mas ela te garante equilíbrio para emendar o próximo movimento."

    s "Que é..."

    window hide

    pause

    scene sayuri_praia_movimento4 with Dissolve(1.0)

    pause

    s "Iaaahh!"

    mc safado "Uou... que visão incrível..."

    s "C-como?!"

    mc surpreso "!!"

    mc "[s]! C-cuidado!"

    s "ÂH?! [mc]! Sai da-"

    scene sayuri_praia_caida with vpunch

    pause

    s "A-ai!"

    mc "ARGH!"

    s "[mc]! Você tá legal?"

    mc "A-acho que sim... tem alguma coisa macia e fofinha no meu rosto..."

    s "!!!"

    scene sayuri_praia_caidos with Dissolve(1.0)

    pause

    s "É-é... d-desculpa..."

    mc "F-foi tudo bem..."

    s "A g-gente t-tá tão perto..."

    mc "P-pois é..."

    "Eu consigo sentir a respiração da [s]... e ela continua aqui... acho que essa é minha chance... m-mas e se ela recusar?"

    menu:
        "Beijar a [s]":


            "É agora ou nunca. Não dá pra jogar essa chance fora."

            mc "[s]... eu queria aproveitar que a gente tá assim... pra fazer uma coisa..."

            s "O-o que, [mc]?"

            mc "S-senta aqui que eu vou mostrar..."

            s "!"

            scene sayuri_praia_beijo with Dissolve(1.0)

            pause

            s "Hmmm!"

            mc "..."

            "Ela tá beijando de volta... ufa..."

            s "[mc]... não para..."

            window hide

            pause

            scene sayuri_praia_beijo2 with Dissolve(1.0)

            pause

            "Caraca... a [s] gostou mesmo de beijar..."

            s "Ai, [mc]... só mais um pouquinho..."

            mc "C-claro... vem aqui..."

            window hide

            pause

            "A gente tá se beijando sei lá por quanto tempo..."

            s "{i}puf puf{/i}"

            s "E-eu... c-com licença..."

            scene sayuri_praia_tchau_dia with Dissolve(1.0)

            pause

            s "O-obrigada pelo passeio, [mc]... m-mas acho que eu vou voltar agora."

            mc preocupado "Sério?! Já?!"

            s "S-sim... eu tenho que... que... tenho que treinar!"

            mc desconfiado "Hm?"

            s "M-mas eu adorei tudo. De verdade. Foi um dia incrível."

            s "Se desse... eu queria sair de n-novo com você... c-como na-na-namorados..."

            mc charmoso "Claro... mas eu t-"

            s "Seria incrível."

            mc preocupado "Eu posso acompanhar você at-"

            s "N-não precisa. Eu vou mais rápido s-sozinha... a-até mais!"

            $ tempo = 1

            scene ilha praia with Dissolve(1.0)

            "Eita... já foi..."

            "O que será que houve que ela saiu correndo?"

            "Ela não parecia envergonhada com o beijo... será que com a massagem e o beijo... ela... Quem sabe..."

            "Bom... tudo acabou dando certo."
        "Ajudar ela a levantar":


            "Melhor não arriscar e acabar estragando nosso dia."

            mc "D-deixa eu ajudar você..."

            s "O-opa..."

            scene sayuri_praia_deitada2 with Dissolve(1.0)

            pause

            s "Hihi... d-desculpa, [mc]."

            mc envergonhado "Não foi nada."

            s "Essa foi boa... M-mas foi tudo culpa sua! Você falou que... a visão estava incrível com uma expressão m-muito... daí eu me assustei!"

            mc "Então foi isso..."

            s "Foi isso!"

            mc charmoso "Mas não vou reclamar... o que aconteceu não foi ruim, não."

            s "!!"

            s "E-eu também não achei ruim..."

            mc normal "E se agora a gente andasse um pouco? Tem aquela parte de madeira que a gente não foi ainda."

            s "Claro! Vamos sim!"

            scene black with Dissolve(1.0)

            "Opa! A [s] tá me dando a mão. Agora a gente realmente parece dois namorados passeando."

            "{b}Uma hora depois{/b}"

            scene sayuri_praia_tchau_tarde with Dissolve(1.0)

            pause

            s "Puxa... a praia é tão bonita, [mc]. Eu adorei nosso passeio."

            mc charmoso "Eu também. Andar por aqui sozinho e com a pessoa que você gosta é totalmente diferente."

            s "V-você achou mesmo?"

            mc "Sim."

            s "Q-que bom... Quando você me chamou pra vir pra cá naquele bilhete junto com o maiô... e-eu fiquei muito nervosa."

            s "..."

            s "E-eu não tinha certeza se eu ia ser uma boa namorada pra isso. Eu tinha minhas dúvidas se eu ia saber fazer tudo direito..."

            s "Daí eu fiquei super preocupada. M-mas acho que deu tudo certo..."

            mc charmoso "Para de ser boba, [s]... não existe isso."

            s "Não existe? O que você quer dizer?"

            mc "Não tem jeito certo de namorar ou ser um namorado... pelo menos pra mim."

            mc "Quando a gente tá com alguém que a gente realmente gosta, a gente quer que essa pessoa se sinta bem e seja feliz. É só isso."

            mc "E como namoro é uma troca, a gente também tem que estar feliz e bem. Não adianta só um dos lados."

            mc "A gente se esforça pra que seja um dia legal, mas não precisa se preocupar. Se a gente realmente se gosta, só de tá perto é o suficiente."

            s "E-eu concordo... obrigada, [mc]."

            mc "Obrigada você, por ter aceitado sair comigo. E posso acompanhar você até a Cidade Chinesa?"

            s "C-claro. Vamos!"

            scene black with Dissolve(1.0)

            $ tempo = 2

    "Esse encontro na praia foi uma ideia incrível. Deu pra ver como a [s] é uma mulher incrível, sensível, bacana..."

    "Eu sei que tem muita coisa acontecendo na vida dela, mas, seja como for, eu prefiro acreditar que todas as pessoas podem ser boas."

    "Às vezes a gente faz coisa errada, mas, todo mundo, até as pessoas mais horríveis, podem ter uma chance se a gente acreditar nelas."

    "Eu quero conhecer mais a [s] e entender tudo o que acontece e estar do lado dela pro que der e vier."

    "É isso aí."

    $ tempo = 2

    jump call_cidade



label praia_especial_julia_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("jex1_save", extra_info="jex1_save")

    $ estou_na_cidade = False

    $ praia_julia_local = True

    "Não sei como eu nunca tinha pensado em trazer a [g] sozinha pra um encontro na praia."

    "Das duas uma: ou a gente vai pros finalmentes ou eu tenho um ataque do coração. Ou a gente vai pros finalmentes e eu tenho um ataque..."

    "De uma forma ou de outra vale à pena arriscar. Só de ver ela em um biquini apertadinho já vai fazer meu dia."

    "Eu vou comprar um biquini que eu ache que ela vai gostar..."

    mc tarado "Mas principalmente que EU vou gostar. Tem que ser o menor e mais transparente possível. Eu tenho certeza que ela não vai negar."

    "Ok... deixa eu ir lá na loja."

    scene black with Dissolve(1.0)

    call locomocao from _call_locomocao_15

    scene cidade centro1 with Dissolve(1.0)

    "Bora ser roubado mais um pouquinho, porque pior que ser roubado, é continuar voltando, né?"

    scene boutique roupa with Dissolve(1.0)

    mc normal "Bom dia."

    show atendente normal with dissolve

    ate "Bom dia, senhor."

    if praia_priscila_local or praia_sayuri_local:

        ate "Espera... o senhor já veio aqui comprar biquinis, não veio?"

        mc envergonhado "Sim, eu vim... e pretendo comprar mais um hoje..."

        ate "Puxa, que bom. Parece que as coisas dão certo no amor, hein? É melhor o senhor ficar longe do Cassino por um tempo."

        mc envergonhado "Haha... é verdade..."
    else:


        ate "Como posso ajudar?"

        mc normal "Eu queria de comprar um biquini."

        ate "Queria? Não quer mais?"

        mc zerado "..."

    ate "E como o senhor gostaria desse biquini? Um mais tradicional, mais reservado ou-"

    mc safado "A outra opção."

    ate "Uma coisa mais... audaciosa?"

    mc charmoso "Sim. Quero a mais audaciosa que você tiver."

    ate "Eu tenho algo bem legal aqui para o senhor então. É coisa nova, importada."

    mc desconfiado "Hmm... Como funciona?"

    ate "Além dele ser bem curtinho e tapar bem pouco, ele ainda tem uma tecnologia que fica meio transparente no sol."

    mc surpreso "T-transparente?!"

    ate "Sim. É tecnologia de ponta diretamente da maior empresa de tecnologia de... ponta."

    mc charmoso "Parece incrível. Vou querer..."

    mc desconfiado "Espera! Quanto é isso?"

    ate "Tem certeza que o senhor quer saber?"

    mc zerado "Acho que não..."

    ate "Muito bem, vamos para o caixa."

    hide atendente with dissolve

    mc "..."

    scene boutique caixa with Dissolve(1.0)

    ate "Viu só? Não ficou tão caro assim."

    mc angustiado "..."

    scene black with Dissolve(1.0)

    scene cidade centro1 with Dissolve(1.0)

    "Por que eu me meto nessas coisas? Bom... agora eu tenho que dar pra ela. Onde eu deixo? Na faculdade?"

    "Lá é perigoso demais... a galera vai é zoar tudo. Melhor eu deixar direto na casa dela e da [s]."

    "Mas e se a [s] não tiver no templo bem na hora? Não quero que ela saiba que eu tô dando esse tipo de presente pra irmã dela."

    if sayuri_namoro:

        "Ainda mais porque a gente tá namorando! Aaahh o que eu tenho na cabeça?!"

        "Um dia isso ainda vai dar muito errado..."

    "Vou deixar um recado como se uma amiga da [g] tivesse deixado pra ela..."

    mc tarado "Ideia de gênio."

    scene black with Dissolve(1.0)

    "Eu tenho o endereço aqui. Sorte que aquele dia eu fui ver o evento da premiação da [s] lá."

    "..."

    "Deve ser por aqui. Opa!"

    scene casa_sayuri with Dissolve(2.0)

    pause

    "É aqui mesmo. Eu lembro."

    "Agora é só deixar aqui, tocar a campainha e..."

    mc surpreso "Falous, turma!"

    scene black with hpunch

    $ tempo = 2

    "..."

    scene mapa_cidade with Dissolve(1.0)

    mc concentrando "Ufa... agora é só-"

    $ renpy.vibrate(1)

    "Smartphone" "Trr... Trrr..."

    mc charmoso "[g]?"

    g "Eu ameiiii!"

    if julia_namoro:

        g "Você é o melhor namorado do mundo!"

        mc safado "Que bom que você gostou..."
    else:


        mc charmoso "Recebeu minha encomenda?"

    g "Ele é tão safado, [mc]! Amei!"

    mc charmoso "Que bom que você gostou."

    g "Eu quero usar ele amanhã pra você!"

    menu:
        "Eu vou adorar ver você nele.":


            mc normal "Não vejo a hora de ver você nele também."

            g "Eu tô muito gata! Você vai pirar!"

            mc "Que bom."
        "Tenho certeza que você vai ficar uma delícia.":


            mc tarado "Sei que você vai ficar uma delícia nele."

            g "Eu tô! Você nem imagina... você vai querer muito me morder."

            mc "Imagino..."

    g "Então combinado! A gente se vê amanhã! Beijo no pinto!"

    mc charmoso "Beijos."

    scene ape_geral with Dissolve(1.0)

    "Agora é só matar o tempo até amanhã. Esse encontro com a [g] vai ser foda."

    "Tenho que tá preparado pra amanhã. Sem pornô hoje. Nadinha!"

    scene black with Dissolve(1.0)

    $ tempo = 1
    $ dia += 1

    "..."

    scene ape_geral with Dissolve(1.0)

    mc concentrando "Hmmm... ainda tá meio cedo, mas já vou acordar. Prefiro chegar lá antes dela."

    "Agora é tomar aquele banho pra chegar cheiroso."

    "Se bem que nesse calor já vou chegar lá como? Pingando. Mas foda-se, vou dar meu melhor pela [g]."

    scene black with Dissolve(1.0)

    "..."

    play sound "audio/som_13_praia2.mp3"

    scene ilha praia with Dissolve(1.0)

    "Sorte que o dia tá super bonito. Quero só ver se aquele negócio de transparência vai dar certo."

    mc zerado "Se aquela mina falou qualquer coisa só pra me vender vou ficar muito pu-"

    g "Eiii!!"

    if julia_namoro:

        g "Namoradooooo!"
    else:


        g "[mc]!"

    "Nossa! A [g] já tá aqui."

    scene jp_julia1 with Dissolve(2.0)

    pause

    g "Aqui, [mc]!"

    "Provavelmente ela ia beber alguma coisa, mas pra variar não tem ninguém no quiosque."

    mc normal "Tô aqui."

    g "Vem logo ver como ficou."

    mc envergonhado "Calma... tô chegando."

    scene jp_julia2 with Dissolve(1.0)

    pause

    g "E aí? Como eu tô?"

    menu:
        "Gostosa pra caralho.":


            mc safado "Tá gostosa pra caralho, [g]."

            g "Assim que eu gosto de ouvir. Se não falar pelo menos um 'gostosa pra caralho', você sabe que tem alguma coisa errada."
        "Tá muito linda.":


            if julia_namoro:

                mc charmoso "Você é a namorada mais linda do mundo. Eu tenho muita sorte de estar com você."
            else:


                mc charmoso "Você tá linda. O biquini caiu super bem em você."

            g "Owwnn... você é muito fofo, [mc]. Obrigada."

    g "Eu queria tá gata pra você. Eu sei que ele não foi barato."

    mc envergonhado "Não foi, mas eu queria comprar algo bacana pra você."

    g "Fala a verdade, foi esse negócio dele ficar transparente, né?"

    mc "C-claro que não... Transparente?"

    "Claro que ela ia perceber. Tá na cara que dá pra ver quase tudo dela com isso."

    g "Para de se fazer de bobo. Ninguém ia vender pra você um biquini desse sem avisar antes. Dá pra ver meio peito e minha bunda certinho."

    mc safado "Que coisa, hein..."

    if julia_namoro:

        g "Se meu namorado não liga dos outros ficarem olhando pra namorada dele e vendo ela inteirinha assim..."

        mc surpreso "Ei!"

        menu:
            "De jeito nenhum. Não tem ninguém aqui.":


                mc serio "Ei. Nada disso. É que não tem ninguém aqui. Você é só pra mim."

                g "Calma... é só uma olhadinha... ninguém vai me morder."

                mc zerado "Não..."

                g "Bobo..."
            "Eles podem ver, mas só eu pego.":


                mc charmoso "Eles podem ver, mas só eu posso pegar."

                g "Isso aí. Confiança é tudo, [mc]. Ainda mais namorando uma gata igual eu."

                mc "Agora tá se achando muito, já."

                g "Ei..."
    else:


        g "Você e os rapazes aqui da praia vão aproveitar bastante, hein?"

        mc zerado "Ei... que 'rapazes'? Sorte que só tem eu aqui."

        g "Que pena... o mundo tá perdendo de ver uma obra prima."

        mc "..."

    scene jp_julia3 with Dissolve(1.0)

    g "Mas eu gostei bastante do presente e do seu convite. Eu queria muito sair com você assim."

    mc charmoso "Que bom. Eu também acho que a gente pode se divertir bastante."

    g "Com certeza... eu quero me divertir bastante com você hoje..."

    g "Mas você tem que ser um cavalheiro, hein?"

    menu:
        "Com certeza. Só o melhor pra você hoje.":


            mc charmoso "Pode ter certeza. Hoje só o melhor pra minha senhorita."

            g "Já tô me derretendo... assim vai ser fácil demais pra você me pegar..."

            "A [g] não tem jeito mesmo... parece que tudo com ela vira conversa sobre sexo."

            mc "Haha... fácil ou díficil, a gente vai chegar lá."

            g "Tô esperando essa hora..."
        "Isso não importa. O que importa é como eu te pegar.":


            mc safado "O que vai importar é a pegada que eu vou dar em você depois. Quero ver você aguentar."

            g "Ai, [mc]. Desde quando você ficou safado desse jeito?"

            mc "É culpa sua..."

            g "Então vai ser culpa minha se você me atacar?"

            mc "Claro. Quem mandou você ser gostosa desse jeito?"

            g "Hmmm..."

    scene jp_julia_sentada1 with Dissolve(1.0)

    pause

    g "Aaahhh! Queria tomar alguma coisa com muito álcool agora!"

    mc envergonhado "Nunca tem ninguém nesse quiosque aí."

    g "Tá tão calor... e eu quero me soltar um pouco mais, [mc]! Bebida sempre dá aquela ajuda, né?"

    menu:
        "Chegar mais perto":


            scene jp_close1 with Dissolve(1.0)

            pause

            "Uou.... que delícia..."

            g "[mc]?"

            mc "Ah... é..."
        "Continuar prestante atenção":


            "Melhor eu só continuar falando."

    mc "Se soltar mais?"

    g "Claro, seu chato. Eu queria ter coragem de ficar pelada..."

    mc surpreso "C-como?!"

    g "Não que eu vou ficar, tonto... mas eu quero ter coragem pra fazer se eu quiser. Eu odeio ter medo."

    mc envergonhado "Hmm..."

    scene jp_julia_sentada2 with Dissolve(1.0)

    g "Mas tudo bem. Vai ter que ser sem álcool mesmo."

    mc charmoso "Você consegue. Você é desinibida o suficiente sem isso."

    g "Tá me chamando de puta, é?"

    menu:
        "Puta, não... só uma garota dada...":


            mc safado "Puta? Claro que não... só uma garota dada, né?"

            g "Haha... engraçadinho... além de que as putas são trabalhadoras. Já você fica fazendo piadinha de cretino."

            mc envergonhado "Era só brincadeira, calma..."

            g "Hmnf!"
        "C-claro que não!":


            mc preocupado "N-não é isso, Ju! Desculpa... era só sobre seu jeito. Não queria falar q-que você-"

            g "Calma, fofo. Tô brincando com você. Eu sei que eu sou alegrinha. Não vejo problema nenhum nisso, tá?"

            mc envergonhado "Ufa... não queria que você me entendesse errado."

            g "Relaxa. Você é fofo demais pra falar uma coisa dessas."

            mc "..."

    g "Assim... não tem problema a gente gostar de sexo, certo? Eu gosto, ué? Qual o problema?"

    if julia_namoro:

        mc envergonhado "Espero que a agora que a gente tá namorando você se procure satisfazer esse gosto todo comigo."

        g "Foi o que eu falei pra você na festa, [mc]. Enquanto você tiver só comigo, eu vou ser só sua também."

        if priscila_namoro or sayuri_namoro or maria_namoro or nathan_namoro or diana_namoro:

            "Ops... espero que ela não descubra nada."

            "A [g] vai sair com todo mundo se ela descobrir que eu tô namorando outra."

            mc envergonhado "Então combinado..."

            g "Tô de olho, hein?"
        else:


            mc charmoso "Combinado. Monogamia é a nova onda."

            g "Infelizmente..."

            mc zerado "Você vai ver que não tem nada de errado nisso."

    g "Ai... falei muito..."

    scene jp_julia_sentada3 with Dissolve(2.0)

    pause

    "Nossa... como essa [g] é gata. O corpo dela é perfeito... ela só tem 18 aninhos ainda por cima..."

    "Poder sair com uma mina dessas... o que eu fiz pra merecer isso?"

    g "Alooouuu..."

    mc surpreso "O-oi!"

    g "Tudo bem aí? Você tava fazendo uma cara estranha..."

    mc envergonhado "Cara estranha?"

    g "É... meio de... tarado... Tava pensando no que?"

    mc "Eu? Nada, não..."

    g "Sei..."

    scene jp_julia_sentada4 with Dissolve(1.0)

    pause

    g "Tava pensando em como eu sou gostosa, né? Eu sei..."

    menu:
        "Vou ser sincero... é isso mesmo...":


            mc envergonhado "Sinceridade... é isso mesmo. Você deitada desse jeito tá me deixando louco, [g]."

            g "Acho bom... porque com esse biquini e essa minha pose bem na sua frente... é o mínimo."

            mc safado "Será que vai rolar alguma coisa hoje?"

            g "Você ia gostar bastante de pegar em mim com esse biquini... talvez tirar ele e me encochar... é isso?"

            mc "Isso..."

            g "Não sei... mas vamos ver se rola um clima."
        "N-não. Tava pensando no trabalho.":


            mc envergonhado "N-não... tava lembrando de um negócio do trabalho aqui."

            g "Não acredito que você tá pensando nisso com uma gostosa abrindo as pernas na sua frente."

            mc charmoso "É que hoje eu quero te tratar igual uma dama. Não ficar olhando assim."

            g "Ai... que romântico, [mc]. Pontos pra você, viu?"

            mc "Vamos contando."

            g "Vamos. Se chegar a 100 pontos, você ganha eu peladinha de presente."

            mc surpreso "O-ok!"

    g "Olha... não precisa se preocupar de ficar olhando pra mim. Eu gosto quando ficam me secando, sabia?"

    g "Pode ser homem ou mulher... tanto faz pra mim... quando me olham eu sinto uma coisa boa, sabe?"

    if julia_namoro:

        g "Agora que a gente tá junto... eu me sinto muito bem quando você olha pra mim..."

        g "É diferente de quando qualquer outra pessoa olha."

    g "Eu queria muito que voce me achasse gostosa. Por isso que eu fiquei super feliz com o presente."

    mc charmoso "Que bom. E eu acho você realmente muito linda."

    g "Deixa eu levantar."

    scene jp_julia4 with Dissolve(1.0)

    pause

    mc surpreso "!"

    g "Então... olha... parece que você comprou o biquini e hoje você veio aqui só pra me ver, sabe?"

    g "Tudo isso só pra poder ver meu corpo quase pelado... isso mexe bastante comigo..."

    g "Não sei por que... mas eu fico muito feliz de saber que você tá aqui só pra olhar pra mim."

    mc envergonhado "[g]..."

    "Não sei se é legal isso que ela sente... mas se eu der um sermão agora, vai matar o clima."

    "O que eu falo pra ela?"

    menu:
        "Olha... deixa eu falar um negócio...":


            mc envergonhado "Olha... eu sei que você não vai gostar, mas eu queria só falar um negocinho."

            g "Não é uma das suas aulas, né?"

            mc "..."

            scene jp_julia5 with Dissolve(1.0)

            g "Tava demorando... o que foi?"

            mc normal "Eu não quero dar uma de psicólogo aqui. Cada pessoa tem um monte de merda na cabeça e não é fácil saber por que a gente faz as coisas."

            g "Certo..."

            mc charmoso "Mas eu queria que você soubesse que você não precisa do seu corpo pra chamar a atenção das pessoas."

            mc "Eu sei que é bom quando as pessoas prestam atenção na gente. Quase todo mundo é assim."

            mc desculpa "E tem pessoas que são atraídas por coisas assim igual corpo, dinheiro, ou porque você faz piada com os outros..."

            mc desculpa "Esse tipo de gente que gosta de você por isso, no fundo não gostam de você de verdade."

            g "..."

            mc charmoso "Se a gente só for a gente mesmo, uma hora ou outra vão aparecer pessoas que realmente gostam da gente pela gente."

            mc "Que vão querer ficar do nosso lado pelo que a gente oferece de verdade. E essas sim são as companhias que duram."

            g "Sei lá, [mc]... parece tudo muito bonito. Mas eu consegui muito mais amigos usando uma saia curtinha..."

            mc envergonhado "Eu sei que é mais fácil. Mas quantas dessas pessoas você realmente pode falar que te conhecem?"

            mc "Ou melhor. Quantas dessas pessoas você realmente colocaria sua vida nas mãos delas?"

            g "Sei lá... que pergunta..."

            mc charmoso "Pois é. Eu sei que não é fácil. Mas pensa nisso."

            g "Tá... eu já acostumei que você é um cara diferente, [mc]."

            if julia_namoro:

                mc "Foi isso que te conquistou?"

                g "Acho que sim. Claro que seu beijo ajudou, mas essa cabecinha realmente foi o principal."

                mc "Ah. E só pra ficar claro, óbvio que você é gata, mas o que me conquistou foi você ser divertida e ser uma incrível companhia."

                mc "Então talvez não seja tão difícil encontrar pessoas que gostem da gente assim..."

                g "Owwnn... se você não tivesse cortado o clima completamente, eu até te dava agora."
            else:


                mc "Ah. E só pra ficar claro, óbvio que você é gata, mas eu sou seu amigo porque você é divertida e é uma incrível companhia."

                mc "Então talvez não seja tão difícil encontrar pessoas que gostem da gente assim..."

                g "Owwnn... se você não tivesse cortado o clima completamente, eu até te dava agora."

            mc envergonhado "Haha..."
        "Vamos aproveitar essa felicidade e curtir.":


            "Primeiro deixa eu chegar mais perto..."

            scene jp_close2 with Dissolve(1.0)

            pause

            g "Que foi?"

            mc "Só tô admirando..."

            g "Gostou tanto assim, é?"

            mc "Mais do que você imagina... você é a mina mais gostosa que eu já vi, [g]."

            g "Não exagera, bobo..."

            mc "É sério. Por que a gente não aproveita pra curtir um pouquinho?"

            scene jp_julia_mc1 with Dissolve(1.0)

            pause

            g "[mc]..."

            mc "Só uma curtidinha, Ju... você não fica excitada quando eu fico te olhando?"

            g "Fico, só que... e se alguém ver a gente?"

            menu:
                "Não tem problema. A gente para na hora.":


                    mc "Não pensa nisso. Se a gente ver alguém a gente para."

                    g "Sério? Promete?"

                    mc "Claro, só chega aqui pertinho."

                    g "..."
                "Eu sei que isso te deixa mais louca.":


                    mc "Nem vem. Eu sei que isso te deixa com mais vontade ainda."

                    g "Não... não deixa..."

                    mc "Para de mentir. Você curte um negócio errado."

                    g "Ai..."

            scene jp_julia_mc2 with Dissolve(1.0)

            pause

            mc "Só uma encochadinha assim na sua bunda... eu sequei tanto ela... só quero dar uma sentida."

            g "Ah... você já tá duro desse jeito?"

            mc "É tudo porque você tá muito gostosa com esse biquini."

            g "Não fala que eu te deixo duro que eu já fico molhada..."

            mc "Mas você deixa..."

            g "Chega... tá bom já. Acho que tem alguém ali."

            menu:
                "Cala a boca e vem aqui! Eu sei que você quer.":


                    $ renpy.block_rollback()

                    mc "Cala a boca que eu sei que você quer. Vem aqui logo."

                    g "Não... para..."

                    mc "Vem logo!"

                    scene jp_julia7 with hpunch

                    g "Eu mandei parar!"

                    mc serio "Que foi?!"

                    g "Eu falei que eu não quero..."

                    mc concentrando "[g]... você me provocou esse tempo todo..."

                    g "Não gostei do jeito que você tá falando comigo. Vamos fazer outra coisa, tá?"

                    mc preocupado "Outra coisa? O que?"

                    scene jp_julia5 with Dissolve(1.0)

                    g "Vamos... dar um pulo no mar!"

                    mc angustiado "Pulo no mar?!"

                    g "Sim! Vai ser legal... pra gente esfriar a cabeça... vem por aqui."

                    mc desculpa "..."
                "Não tem ninguém. Eu tô olhando.":


                    $ julia_sexo_praia = True

                    mc "Calma, não tem ninguém. Eu tô de olho."

                    g "Tá... pega em mim... tira minha calcinha..."

                    mc "Tá."

                    scene jp_julia_mc3 with Dissolve(2.0)

                    pause

                    g "Isso... tá gostoso... me aperta..."

                    mc "Hmm... Tô sentindo você aqui em baixo..."

                    g "Eu tô sentindo você também... eu já tô molhada... pode enfiar."

                    mc "Hmm.."

                    scene jp_julia_mc4 with Dissolve(1.0)

                    pause

                    g "Isso... devagar... ai, [mc]... sem pressa..."

                    mc "Tá muito gostoso."

                    g "Tá, sim. Isso... vai devagar... me beija... me aperta..."

                    mc "..."

                    g "Isso... assim... agora vai mais rápido."

                    g "Hmmm... seu gostoso... mais rápido. Vai, mais forte!"

                    scene jp_julia_mc5 with Dissolve(2.0)

                    pause

                    g "Isso! Assim!"

                    mc "Eu vou gozar, [g]!"

                    g "Não para até eu mandar! Eu tô quase!"

                    g "Isso! Mais!"

                    g "Aaahh!"

                    mc "Agh!"

                    scene black with Dissolve(3.0)

                    "..."

                    scene jp_julia_sentada5 with Dissolve(2.0)

                    pause

                    g "Não acredito que você acabou me comendo..."

                    mc concentrando "Eu não sei quem acabou comendo quem ali no final... eu só segui suas ordens..."

                    g "Você veio chegando... chegando... isso não se faz, [mc]."

                    mc charmoso "Eu adorei. Você é incrível."

                    g "Eu gostei muito também... obrigada pelo seu bom trabalho. Estou satisfeita."

                    g "Vamo correr até a água agora?"

                    scene black with Dissolve(1.0)

                    mc angustiado "Correr? Agora?!"

                    g "Claro! Vai dizer que cansou?!"

                    mc "..."

    scene jp_julia6 with Dissolve(2.0)

    pause

    g "Vem, [mc]! Vamos na água um pouco!"

    mc envergonhado "Meu Deus..."

    g "Quê?!"

    mc surpreso "[g]! Cuidado! Na sua fr-"

    scene jp_julia_caindo with vpunch

    pause

    g "Aaahhh!"

    mc surpreso "[g]!"

    g "Aaaiiiieeee!"

    scene black with Dissolve(3.0)

    "..."

    g "Ai..."

    mc normal "Calma que eu te levo pra casa."

    g "Madeira desgraçada filha de uma puta..."

    mc envergonhado "Calma... a gente vem mais vezes..."

    g "Promete?"

    mc normal "Com certeza."

    "Infelizmente a gente vai ter que cancelar o passeio... mas é melhor... a perna da mina tá sangrando."

    "Mas foi bacana. E não é que o biquini era transparente mesmo?"

    $ tempo = 2

    jump call_cidade



label praia_especial_diana_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("dex1_save", extra_info="dex1_save")

    $ estou_na_cidade = False

    $ praia_diana_local = True

    "Bom. Então tá certo. Eu vou fazer algo com a [d] hoje."

    if diana_namoro:

        "A gente começou a namorar e eu quero passar um tempo com ela. Aproveitar nosso lance da melhor forma possível."
    else:


        "A gente tá na amizade por enquanto, mas eu sinto que pode rolar alguma coisa maior entre a gente."

    "Eu vou ter que dar uma passada na boutique pra arranjar um biquíni legal pra ela."

    "A [d] é uma mulher fina. Não vai dar pra comprar qualquer merda..."

    mc zerado "Hora de botar a mão no bolso."

    scene black with Dissolve(1.0)

    call locomocao from _call_locomocao_16

    scene boutique geral with Dissolve(2.0)

    "Um dia eu ainda vou achar uma loja mais barata pra comprar presente."

    "Se bem que desta vez eu realmente tô disposto a comprar algo um nível acima."

    if diana_namoro:

        "Quero só o melhor pra minha namorada chique."

    ate "Bom dia, senhor."

    mc normal "Opa. Bom dia."

    scene atendente_ola with Dissolve(1.0)

    ate "É bom ver o senhor novamente."

    mc zerado "Nem me fala..."

    ate "Como posso ajudar hoje?"

    mc normal "Eu tô procurando um biquíni para dar de presente pra uma garota."

    ate "Certo."

    mc charmoso "Mas ela é uma mulher muito fina e até famosa aqui na capital."

    scene atendente_explicando with Dissolve(1.0)

    ate "Hmm... não vou perguntar quem é. Mas acho que eu tenho o que o senhor precisa aqui."

    mc "Sério?"

    ate "Sim. Um biquíni sensual, só que não vulgar, além de ter uma cor da realeza e é de uma marca internacional."

    mc envergonhado "Vai custar toda minha realeza, né?"

    ate "Claro que não. Ele está na promoção. Vai sair por algo em torno de C$ 200. Mas vale muito à pena."

    menu:
        "Tudo isso por dois pedacinhos de pano?":


            mc zerado "200 pilas por um pedaço de pano? Sério mesmo?"

            ate "Isso é muito mais que um pedaço de pano. É um símbolo de realeza e status. Riqueza não é só ter dinheiro, mas viver como rico."

            mc envergonhado "Se você diz..."

            ate "Com certeza. Fazer parte da alta sociedade não é só ter um valor no banco, mas usar as roupas certas, como esta aqui."
        "Tudo bem. Vai valer à pena.":


            mc normal "Ok. É um pouco salgado, mas vai valer à pena."

            ate "Esse é o pensamento, senhor. Isto é mais que só costura, é um símbolo de status. Ela vai adorar."

            mc charmoso "É o que eu tô esperando."

    ate "Então eu vou pegar e pode passar no caixa para acertar e já te entrego."

    mc normal "Ok."

    scene black with Dissolve(1.0)

    "..."

    scene atendente_caixa with Dissolve(1.0)

    pause

    ate "Muito obrigada pela sua compra, senhor."

    mc normal "Valeu pelo desconto."

    ate "Desc- ah, sim! O senhor merece."

    ate "Sempre que precisar de alguma coisa, pode me procurar. Nossa loja tem tudo para a garota, ou garotas, dos seus sonhos."

    mc envergonhado "Pode deixar..."

    ate "Se me permite... o senhor tem uma energia muito interessante."

    mc desconfiado "Energia? O que você quer dizer?"

    ate "Quando eu falo com você eu sinto algo diferente. Uma vontade de falar mais... de me abrir pra você... estranho, né?"

    mc envergonhado "Pois é..."

    ate "Temos que conversar mais. Aqui ou no Cassino. Quando tiver tempo, venha falar comigo."

    mc charmoso "Pode deixar. Até mais."

    ate "Até."

    scene boutique geral with Dissolve(1.0)

    "O que deu nessa mina?"

    "Bom... agora eu tenho que entregar pra [d]. Vou deixar lá no Cassino."

    "Seria melhor entregar pra ela direto, mas acho que vou dar pra Ana. Mesmo que o Barão acabe xeretando, não tem nada de mais em um biquíni..."

    "Mas vou ter que esperar ficar à noite. Vou dar uma passada no fliperama pra gastar um tempo."

    scene black with Dissolve(1.0)

    "..."

    scene mapa_cidade_noite with Dissolve(1.0)

    "Boa. Já deve tá aberto. Agora só encontrar a Ana."

    scene black with Dissolve(1.0)

    scene ana mesa1 with Dissolve(1.0)

    ana "Entregar pra [d]?"

    mc normal "Isso. Você pode quebrar essa pra mim, [ana]?"

    ana "Tá legal. Só entregar então."

    mc "Isso. Aí tem um presente e um recado pra [d]. Só entregar pra ela por favor."

    ana "Ok. Pode ficar tranquilo que guardo aqui e entrego pra ela. Inclusive hoje tem show dela, mas vai demorar umas horinhas ainda."

    mc charmoso "Tranquilo. Valeu mesmo."

    ana "Boa noite. E não deixa de vir jogar aqui e receber seus prêmios comigo."

    mc charmoso "Pode deixar. Até a próxima."

    ana "A gente se vê, senhor."

    scene mapa_cidade_noite with Dissolve(1.0)

    "Resolvido. Agora é só esperar até amanhã."

    "Já tô ficando ansioso com essa ideia de ir na praia sozinho com a [d]."

    if diana_namoro:

        "Ter um tempo como namorados vai ser bom pra gente. Tirar a cabeça desses rolos todos."

    "Vou até dormir cedo pra acordar disposto amanhã."

    scene black with Dissolve(1.0)

    "..."

    scene ape_geral with Dissolve(1.0)

    "Ufa. O dia nasceu."

    scene ape_celular with Dissolve(1.0)

    "Hmm... nenhuma mensgem da [d]. Será que ela não recebeu o que eu mandei?"

    "É complicado esse negócio. Eu sinto que ela tá sempre se escondendo. Que ela tá sempre fugindo. Deve ser muito complicado viver desse jeito."

    "Bom... se ela não puder sair comigo... não dá pra culpar ela. A pena é nunca ver ela com o biquíni..."

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "{cps=6}{i}Trr... trrr...{/i}{/cps}{w=1.0}{nw}"

    mc "Opa! É ela!"

    scene ape_celular_falando with Dissolve(1.0)

    mc "Oi, [d]."

    d "Oi, [mc]. Estou aqui na praia. Você vem?"

    mc "V-você já tá aí?!"

    d "Sim."

    mc "Chego em 15 minutos!"

    d "Tô esperando. Beijo."

    mc "Beijo!"

    "BORA!"

    show black with moveinright

    scene ilha praia_gazebo

    show black

    "..."

    hide black with moveoutleft

    mc angustiado "{i}puf puf{/i}"

    "Tô chegando, [d]..."

    "Deixar uma dama esperando... isso é algo imperdoável..."

    "Eu sei... eu sou um gado à moda antiga... fazer o quê!"

    "Onde será que ela tá me esperando? Se ela não tá no gazebo, deve ser no quiosque."

    "..."

    mc normal "Acertei de segunda."

    scene dp_quiosque1 with Dissolve(1.0)

    pause

    "A [d] é muito gata mesmo. Tudo é perfeito nessa mulher, Deus..."

    mc charmoso "Bom dia."

    d "[mc]. Vem sentar aqui comigo."

    mc "Claro."

    scene dp_quiosque2 with Dissolve(1.0)

    pause

    d "Espero não ter assustado você hoje de manhã."

    mc charmoso "Claro que não."

    menu:
        "Tava preocupado que você não poderia.":


            mc envergonhado "Eu tava era preocupado que você não ia poder."
        "Tava louco esperando você confirmar.":


            mc charmoso "Tava é louco esperando você me avisar que ia poder."

    d "Você sabe que comigo é sempre assim."

    if diana_namoro:

        d "Inclusive, você sabia no que estava se metendo quando resolveu começar algo sério comigo."

        mc charmoso "Com certeza. Sabia mesmo. Não se preocupe que isso não é problema pra mim."

        d "Eu sei. Por isso eu aceitei."

    d "Não é fácil estar sempre nessa constante dinâmica de caça e caçador, mas são como as coisas são."

    mc charmoso "Isso com certeza deixa você uma garota bem mais misteriosa."

    scene dp_quiosque3 with Dissolve(1.0)

    pause

    d "Então é algo positivo pra você. Mistério é tudo na vida."

    mc charmoso "Você realmente gosta dessa vibe."

    d "As coisas não têm graça sem significado. Tem pessoas que aceitam a vida pelo seu sentido prático, mas não eu."

    d "Pra mim a vida é muito mais do que acordar, trabalhar, comer, transar e dormir."

    d "Se tudo isso não tiver um mistério, um significado que justifique, então é o mesmo que comer tofu sem shoyo."

    d "E você?"

    mc envergonhado "E-eu? É..."

    menu:
        "Eu sou um cara mais prático.":


            mc charmoso "Acho que eu sou um cara mais prático. Pra mim comer é comer e sexo é sexo. Não precisa muito mais pra existir."

            d "Você não acha isso sem graça?"

            mc "Não. Acho que as coisas existem pra existir e pronto. Ficar pensando demais no porquê das coisas só deixa a vida mais complicada."

            d "Por um lado faz sentido mesmo. Mas é um pensamento que eu simplesmente não poderia pegar para mim."
        "Eu concordo. O significado é mais importante.":


            mc charmoso "Sendo sincero mesmo, eu concordo. Fazer só por fazer é como se nem tivesse feito. Se não tiver um motivo pra isso, entende?"

            d "Claro que eu entendo."

            mc "Tem gente que só liga pra ter 'mais'. Mais dinheiro, mais seguidores, mais amigos. Agora, quem se preocupa com o qualitativo?"

            mc "Tipo, seu dinheiro é honesto? Seus amigos são de verdade? Por que as pessoas te seguem? Isso parece que tá esquecido..."

            d "Eu não tava planejando todo esse pensamento filosófico, mas concordo com você."

    scene dp_quiosque4 with Dissolve(1.0)

    d "Eu gosto de refletir bastante sobre as coisas, [mc]. Talvez você me ache uma companhia um tanto massante."

    mc surpreso "Tá louca?!"

    mc charmoso "Você é incrível, [d]. Quando eu converso com você eu sinto que eu tô tipo em outro mundo."

    d "E que mundo é esse?"

    mc "Sei lá. O mundo dos ricos, das pessoas importantes... famosas..."

    d "Não tem nada de diferente nesse mundo, [mc]."

    mc zerado "Como não?"

    d "Seja naqueles becos da capital, na ilha ou no hotel do Cassino do Barão, as pessoas são só pessoas. Ninguém sabe direito pra onde está indo."

    d "O ser humano é uma criatura triste. A maioria é mesquinha e egoísta. Só se preocupa em como sair do buraco em que se meteu."

    mc charmoso "Mas você não é assim."

    scene dp_quiosque5 with Dissolve(1.0)

    pause

    d "Pelo contrário. Eu sou mais mesquinha e egoísta que a maioria. A diferença é que eu tenho consciência disso."

    d "É normal do ser humano ter medo de admitir que está errado. A maioria vai morrer achando que viveu certo, que a culpa do fracasso foi o mundo."

    d "Não quero livrar de culpa governo, as empresas e os demais agentes da sociedade. Cada um tem seu papel na derrocada do mundo."

    d "Mas não podemos ignorar também que as pessoas são seus próprios algozes. São escravas de seus próprios desejos."

    mc envergonhado "Você não tá sendo um pouco severa com as pessoas?"

    scene dp_quiosque6 with Dissolve(1.0)

    pause

    d "Talvez... mas a severidade realmente faz o que eu estou dizendo ser menos verdade?"

    d "Mas eu não julgo as pessoas, [mc]. Eu não falo sobre fulano ou beltrano, mas sobre nossa raça no geral."

    mc charmoso "Entendi. Acho que pensar sobre nossa natureza é um pouco de você ser uma artista, né?"

    d "Ou o contrário. Talvez eu tenha virado uma cantora justamente por olhar o mundo por dentro."

    mc "Verdade. Mas, seja lá o que veio primeiro, o que importa é que você é uma cantora linda, sexy e de sucesso."

    scene dp_quiosque7 with Dissolve(1.0)

    pause

    d "E qual desses é o mais importante pra você? Linda, sexy ou de sucesso?"

    mc charmoso "Opa... que pergunta, hein?"

    d "Será que eu deixei o [mc] sem resposta?"

    menu:
        "Linda.":


            mc charmoso "Pra mim, o mais importante é que você é a garota mais linda que eu já vi."

            scene dp_quiosque8 with Dissolve(1.0)

            pause

            d "Será que você é parâmetro pra isso? Tenho a impressão que você não tem muito sucesso com as garotas."

            mc zerado "Isso não vem ao caso."
        "Sucesso.":


            mc charmoso "Seu sucesso é o que mais me chama atenção. Estar do lado de uma mulher que conseguiu tudo isso."

            scene dp_quiosque8 with Dissolve(1.0)

            pause

            d "Será que o sucesso é tão importante assim? Ou será que é porque você não tá tão bem nesse departamento?"

            mc zerado "Isso não vem ao caso."
        "Sexy.":


            mc safado "Sem dúvida o mais importante é que você é muito sexy. Você mexe comigo demais."

            scene dp_quiosque8 with Dissolve(1.0)

            pause

            d "E você não tem medo de ficar vulnerável contra uma coisa que você quer muito?"

            mc safado "Não... eu só quero pegar você e-"

            mc preocupado "Se bem que agora que você falou..."

            d "Haha..."
        "Todos.":


            mc charmoso "Tudo isso. Beleza, sedução, sucesso e dinheiro..."

            d "Eu perguntei qual é o MAIS IMPORTANTE."

            mc envergonhado "Hmmm... não consigo escolher."

            d "Se você não sabe, então vai ficar sem qualquer um."

            mc angustiado "M-mas!"

    d "Tô brincando, tonto. Você é um rapaz diferente, [mc]. Um que eu jamais pensei que fosse encontrar."

    mc "S-sério?"

    d "Eu tento entender sua forma de pensar desde a primeira vez, mas eu não consigo..."

    d "Existe só outra pessoa que eu já vi com a energia como a sua. É realmente uma coisa rara."

    mc charmoso "Tá vendo por que você gosta de mim? Eu sou um mistério."

    d "Isso com certeza tem a ver."

    d "E o que você acha de a gente passar o resto do dia andando pela praia?"

    mc envergonhado "Acabou o mistério desse quiosque, né?"

    d "Acho estranho que ele deixe aqui vazio sem ninguém. Isso é realmente um mistério."

    mc desconfiado "O quê?"

    d "Esquece. Vamos?"

    mc charmoso "Claro. Vamos, sim. As damas primeiro."

    d "Com licença."

    scene black with Dissolve(2.0)

    "..."

    play sound "audio/som_13_praia2.mp3"

    $ tempo += 1

    scene praia tarde with Dissolve(2.0)

    pause

    mc "O sol já tá abaixando..."

    scene dp_praia17 with Dissolve(2.0)

    pause

    "Caralho... olha pra [d]. Ela tá gata demais."

    "Essa mina é perfeita."

    if diana_namoro:

        "Nem acredito que eu tô namorando essa deusa."

    mc "Este lugar... é familiar..."

    d "Sim... aliás, foi de manhã... mas nosso encontro aconteceu aqui, não foi?"

    mc desconfiado "Hm?"

    scene dp_praia1 with Dissolve(1.0)

    pause

    d "Eu reconheço este lugar. Eu costumava tomar sol aqui de manhã."

    mc "É! É isso mesmo! Eu lembro que eu tava andando por aqui um dia de manhã. Caraca... eu lembro desse negócio de pedra aqui atrás."

    d "Traz lembranças..."

    mc "Verdade... A ilha não é tão grande, mas tá cheia de lugar marcante. Tipo o Cassino, essa praia aqui, aquela praça com uma estátua esquisita."

    d "Ah, sim. A praia foi criada pra isso mesmo. Quem idealizou isso tudo com certeza foi criativo."

    mc "Do jeito que você fala, parece que a ilha foi criada por uma pessoa."

    d "Claro que foi criada por pessoas, [mc]."

    mc "S-sim. Digo. Por uma pessoa."

    d "Ora... Por que não?"

    mc "Hm?"

    scene dp_praia2 with Dissolve(1.0)

    pause

    d "É tão impressionante assim se uma pessoa idealizou e realizou tudo isso aqui?"

    menu:
        "Eu acho meio sem noção.":


            mc "Sendo sincero, acho que é meio viagem achar que uma pessoa sozinha iria criar algo desse tamanho."

            d "E os parques de diversões gigantes? Alguns devem ser maiores que a ilha."

            mc "Hmm... mas é diferente. Aqui as pessoas vivem, trabalham, existem prédios residenciais. Tipo, igual uma cidade comum."

            d "Tem razão... realmente não é a mesma coisa."
        "Se for uma pessoa muito rica...":


            mc "Bom... se a pessoa for muito rica, talvez ela consiga..."

            d "Acredito que não é só uma questão de dinheiro. Alterar uma ilha deve envolver governo e outros órgãos ambientais."

            mc "Isso é verdade..."

            d "Teria que ser alguém realmente poderoso."

    mc "Você fica pensando nessas coisas de vez em quando?"

    d "Você fica?"

    mc "Mais do que eu devia eu acho..."

    d "É. Eu também... essa ilha sempre me impressionou."

    mc "Eu não era daqui. Eu vim pra capital pra estudar. Já tinha ouvido falar, claro, mas não conhecia a ilha."

    scene dp_praia3 with Dissolve(1.0)

    pause

    d "Eu também não nasci aqui. Mas eu vim pra cá muito pequena. Eu sempre vivi na ilha. Pra falar a verdade, nem lembro como é estar longe daqui."

    mc "Você não tem vontade de viajar?"

    d "Imagina... é meu sonho. Por isso eu queria ter uma música de sucesso nacional."

    mc "Mas você é rica. Por que não vai?"

    d "Certos... compromissos me... prendem aqui. É impossível pra mim."

    mc "Isso não parece certo, [d]."

    d "Ser errado nunca impediu ninguém de fazer alguma coisa, [mc]. Para algumas pessoas, ética não está no topo da lista de prioridades."

    mc "Eu sei. Não quero parecer inocente. Mas é que eu fico surpreso como uma mulher não pode tirar férias por um tempo."

    d "É... não parece legal mesmo. Mas não é só uma realidade só minha. Muitas pessoas vivem assim."

    mc "Pra falar a verdade... desde que eu comecei a trabalhar na revista nunca fui pra outro lugar de férias."

    mc "M-mas não é a mesma coisa que o seu caso."

    scene dp_praia4 with Dissolve(1.0)

    pause

    d "..."

    mc surpreso "D-diana?!"

    d "Eu não quero que nosso passeio fique nessa vibe por muito tempo."

    if diana_namoro:

        d "Agora que a gente está namorando, a gente precisa de um tempo juntos, pra gente se curtir."

        mc charmoso "Concordo."
    else:


        d "Você é um excelente parceiro filosófico, [mc]. Mas acho que a gente não precisa ficar só nisso."

        mc charmoso "Concordo..."

    d "Eu quero que você curta minha inteligência e sensibilidade, mas também meu corpo e o resto que vem no pacote."

    mc surpreso "O-o-ok!"

    d "Eu adorei o presente que você me deu. Ele é fino, sexy e combinou muito comigo. Obrigada."

    mc charmoso "Não foi nada."

    d "E você? O que achou?"

    mc "Eu achei que ficou incrível."

    d "Obrigada."

    scene dp_praia5 with Dissolve(1.0)

    pause

    d "Esse sol do fim da tarde é igual o sol da manhã... é o melhor na minha opinião."

    d "A vista aqui é incrível, né?"

    mc "S-sim... a vista tá incrível."

    d "Poucas pessoas têm a chance de ver este lado do continente. É preciso dar a volta quase na ilha toda."

    mc "É verdade. É uma visão bem rara..."

    "Será que ela tá fazendo de propósito? O jeito que ela tá inclinando... parece que ela tá convidando eu pra dar uma olhada..."

    menu:
        "Acho que vou dar uma conferida...":


            "Quem não chora não mama. Só uma olhadinha..."

            scene dp_praia6 with Dissolve(1.0)

            pause

            "Uou... que bunda que essa [d] tem."

            "Mesmo com tantas garotas lindas aqui na ilha, acho que essa aqui é a vencedora..."

            d "[mc]?"

            mc "O-oi!"

            d "Você gostou mesmo da vista."

            mc "Sim! Q-quero dizer..."

            scene dp_praia5 with Dissolve(2.0)

            pause
        "Melhor não arriscar.":


            "As coisas tão dando certo. Melhor eu não dar uma de tarado agora."

            mc "Uma vez acho que eu vi dois caras andando por aqui. E mais ninguém..."

            d "Sim. Deve ser muito raro."

    mc "Você tá sentindo com a água tá quentinha hoje? Normalmente não tá assim."

    d "Verdade. Eu não ligo de entrar na água, mas quero aproveitar. Senta comigo um pouco na areia?"

    mc "Claro."

    scene dp_praia7 with Dissolve(2.0)

    pause

    d "Ahh... o sol, a água... está tudo perfeito hoje. Você não podia ter escolhido um dia melhor, [mc]."

    mc "Que bom que você tá curtindo."

    d "Espero que você esteja gostando também."

    mc "Com certeza."

    window hide

    pause

    scene dp_praia8 with Dissolve(2.0)

    pause

    d "Esse biquíni não deve ter sido barato. Não imaginei que você tivesse cacife pra isso."

    if roupa_blacktie:

        mc "Você não lembra do meu Black Tie? Eu tô podendo mais do que você me dá crédito."

        d "Tem razão. Peço desculpas. Aparentemente logo você vai passar de caçador de famoso para famoso. Eles que se cuidem."

        mc "Exatamente. Um dia talvez eu chegue lá. Se eu quiser..."
    else:


        mc "Eu dou meu jeito. O importante é que você gostou."

        d "Você é um cavalheiro mesmo."

    window hide

    pause

    scene dp_praia9 with Dissolve(2.0)

    pause

    "Uou... ela tá bem ousada..."

    d "Hmmm... que delícia."

    d "Eu realmente precisava de um tempo assim. Longe do Cassino e de todas as coisas. Só curtindo um tempo pra mim."

    mc "E-eu também tô curtindo bastante."

    window hide

    pause

    "..."

    scene dp_praia10 with Dissolve(2.0)

    pause

    d "Hmm... Adorei o passeio, [mc]. Foi melhor do que eu imaginava. Foi algo simples, mas extremamente prazeroso."

    mc "Já pretende puxar o carro?"

    d "Ainda temos que voltar e, pra falar a verdade, não lembro se tenho ou não show no Cassino hoje."

    mc "Tá certo..."

    if diana_namoro:

        "Eu e a [d] agora tamo namorando. Eu preciso ter coragem e tomar a iniciativa."

        "Ela é super reservada. Se não rolar algo entre a gente aqui, duvido que ela vá aceitar mais perto do centro da ilha."

        mc "É... [d]... eu só queria falar uma coisa..."

        d "Sim?"

        scene dp_praia11 with Dissolve(1.0)

        pause

        mc "Aquele dia no bar... lá no Aquarius... eu fiquei muito feliz da gente assumir um relacionamento."

        d "Eu também. Você sempre foi sincero sobre o que sentia por mim. Você foi muito corajoso."

        mc "Obrigado. Você também."

        mc "E agora... nós dois aqui nesta praia... eu queria chegar mais perto de você."

        d "[mc]..."

        mc "O-oi."

        d "Não foi com esse tipo de pergunta que você me conquistou. Só faça o que quer fazer."

        mc "Então..."

        scene dp_praia12 with Dissolve(2.0)

        pause

        d "Então era isso..."

        d "Era isso que você queria desde o começo. Um pedacinho de mim."

        mc "..."

        d "Você não vai falar mais nada?"

        d "Vai só fazer o que quer?"

        mc "..."

        d "Não era bem isso-"

        scene dp_praia13 with vpunch

        pause

        d "O-opa! Que mão é essa?"

        mc "..."

        d "[mc]... você tá me provocando..."

        d "Hmmm... você vai pegar no meu corpo inteiro mesmo?"

        mc "..."

        d "Tudo bem. Você venceu."

        d "Só que dois podem jogar esse jogo."

        window hide

        pause

        scene dp_praia14 with Dissolve(1.0)

        pause

        mc "Hmmm..."

        d "Por essa você não esperava."

        mc "Fazer o que quer também vale pra você?"

        d "Óbvio. Vale principalmente pra mim."

        mc "Gostei..."

        d "Agora só me beija."

        window hide

        pause

        scene dp_praia15 with Dissolve(2.0)

        pause

        mc "Satisfeita?"

        d "Você beija bem. Mas acho que foi sua mão apertando minha bunda que me deixou excitada."

        mc "Você inteira me deixou excitado. O que você acha da gen-"

        d "Xii... A gente ainda vai ter nossa chance. Não hoje."

        mc "T-tá."

        d "Hoje se divirta pegando em mim."

        mc "Com todo o prazer."

        window hide

        pause

    scene dp_praia16 with Dissolve(2.0)

    pause

    d "O sol já está quase se pondo. Eu vou acabar me atrasando."

    mc charmoso "Tudo vale à pena quando a alma não é pequena."

    d "Tem razão. Eu adorei nosso passeio."

    mc "Posso te acompanhar até o Cassino?"

    d "Até um ponto. Não quero que você pense que eu estou te convidando pra subir."

    mc envergonhado "Boba..."

    scene black with Dissolve(1.0)

    "..."

    $ tempo += 1

    d "Até uma próxima."

    mc charmoso "Até."

    "Não vejo a hora de fazer algo de novo com ela. Essa mulher mexe muito comigo."

    "Agora bora dar um rumo pra vida."

    jump call_cidade



label praia_especial_nathan_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("nex1_save", extra_info="nex1_save")

    $ estou_na_cidade = False

    $ praia_nathan_local = True

    "Então tá decidido. Vou chamar o [n] pra gente curtir esse praião que tem aqui na ilha."

    "Primeira coisa vai ser comprar algo pra ele usar. Vou fazer direitinho, uma coisa bem especial."

    "Vou dar um pulo lá na loja de roupas e ver o que a moça consegue pra mim. Quero algo que seja confortável, mas né... nem tanto."

    "O objetivo é dar uns pegas nele e dar uma olhada no material. Bom, deixa eu ir."

    scene black with dissolve

    call locomocao from _call_locomocao_17

    scene cidade centro1 with Dissolve(1.0)

    "Eu preciso encontrar outra loja de roupa urgente. Não aguento mais pagar os olhos da cara aqui."

    "Bom, pelo menos as roupas são boas. Só que tá meio fora da minha faixa... enfim, chega de falar sozinho."

    scene boutique geral with Dissolve(2.0)

    if nathan_namoro:

        "Mas é legal porque, agora que a gente tá namorando, pelo menos eu vou tá fazendo algo pra valorizar ele."

    "É importante a gente dar uma moral pra quem a gente gosta. Tenho que aprender a chorar menos."



    scene atendente_explicando with Dissolve(1.0)

    ate "Tudo bem, senhor? Você tava parado olhando pro nada..."

    mc envergonhado "Ah... só tava pensando."

    ate "Entendi... Posso ajudar com alguma coisa?"

    mc charmoso "Eu tô procurando um traje de banho pra dar de presente."

    ate "É pra uma amiga, namorada ou alguém da família?"

    if nathan_namoro:

        mc "Na verdade é pro meu namorado. É um rapaz."
    else:


        mc "Na verdade é pra um rapaz que eu tô querendo ficar."

    ate "Ah. Então só vou te perguntar uma coisa.{w} O presente é pra ele ou pra você?"

    mc desconfiado "Hm? Como assim?"

    ate "Pensa. Você quer que o presente seja pra ele ou pra você ver nele?"

    mc surpreso "Oh!"

    mc envergonhado "É... pensando aqui... acho que eu quero que seja mais pra mim do que pra ele."

    ate "Então eu tenho aqui uma peça que o senhor vai amar!"

    mc safado "Já fiquei empolgado."

    ate "Pode ir pro caixa que eu te levo lá."

    mc "Ok."

    scene black with Dissolve(1.0)

    "..."

    scene atendente_caixa with Dissolve(1.0)

    pause

    mc zerado "Espera... eu nem sei o preço e nem vi. Por que eu já tô aqui pagando?"

    ate "Eu tenho certeza que o senhor vai amar. Ela é na medida certa pro tipo de presente que o senhor quer."

    ate "E ainda tá em promoção. Só C$ 200."

    mc surpreso "D-duzentos?!"

    ate "É um nanomaterial composto de liga de carbono com seda de alta densidade que vai-"

    mc zerado "Ok, ok. Eu já aceitei. Tá aqui o cartão. Passa no débito."

    ate "Obrigado, senhor. Bom passeio e tenho certeza que vocês dois irão gostar."

    mc normal "Valeu. Até outro dia."

    scene black with Dissolve(1.0)

    "..."

    scene cidade centro10 with Dissolve(2.0)

    "Agora eu vou deixar o pacote na Blergh! pra ele receber. Vou deixar também um bilhete chamando pra ele ir na praia amanhã."

    "Tomara que ele veja e fique empolgado. Ficar empolgado sozinho é meio vergonha alheia..."

    scene black with Dissolve(1.0)

    "..."

    "Pronto. Agora é voltar."

    "..."

    scene mapa cidade_tarde with Dissolve(1.0)

    "Ufa... tudo pronto pra amanhã. Não vejo a hora."

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    mc normal "Opa. O [n]!"

    mc charmoso "Oi! Tudo bem?"

    n "Oi, [mc]. Tô legal. Tô ligando pra falar que eu recebi sua encomenda aqui. O pessoal da portaria me deu."

    mc "O que você achou?"

    n "Adorei! Eu topo! Com certeza!"

    mc charmoso "Acho que vai ser uma boa a gente esquecer e só curtir a praia amanhã."

    n "Concordo... tá acontecendo todas essas coisas. A gente precisa de um descanso."

    mc "Isso. Amanhã então cedo na praia aqui da ilha. Vai dar pra você?"

    n "Com certeza. A gente se vê amanhã."

    if nathan_namoro:

        mc "A gente se vê... namorado..."

        n "Haha... eu ainda fico com vergonha quando eu penso."

        mc "Isso é bom. Só mostra como você é fofo."
    else:


        mc "A gente se vê então. Fica bem."

    n "Você também. Até amanhã."

    $ tempo = 2

    "..."

    scene ape_geral with Dissolve(1.0)

    "Agora é só esperar até amanhã. Não vejo a hora."

    "Ver o [n] de sunga... eu vou sonhar com isso hoje."

    scene black with Dissolve(1.0)

    $ tempo = 1
    $ dia += 1

    "..."

    scene ape_geral with Dissolve(1.0)

    "Hmm... Opa. Já são nove... Tô super empolgado pra encontrar o [n]."

    "Eu acho que nós dois tamo precisando de um tempo longe do trabalho e dos problemas."

    "Quero que hoje o dia seja incrível pra ele. Que ele se sinta bem e de boa comigo."

    if nathan_namoro:

        "É pra isso que os namorados servem também, certo? Não é só pra beijar."

    "Acho que já vou me arrumar e ir pra lá."

    scene black with dissolve

    "..."

    scene ilha praia_gazebo with Dissolve(1.0)

    "O dia tá super bonito. Mas tem umas nuvens vindo... tomara que não chova."

    mc safado "Tô louco pra ver o [n] naquela sunga... espero que dê pra ver o-"

    n "Ver o quê?"

    mc surpreso "V-ver o sol!"

    scene nex1_evento1 with Dissolve(1.0)

    pause

    n "Cheguei atrasado? Não tinha hora, né?"

    menu:
        "Eu acabei de chegar também.":


            mc normal "Deu certinho. Eu acabei de chegar também."

            n "Que bom."
        "A hora que você chega é sempre a hora certa.":


            mc charmoso "A hora certa é sempre a hora que você chega."

            n "Então não vai ter nem preliminares? Já vamos começar desse jeito?"

            mc "Essas são as minhas preliminares."

            n "Antes do bom dia?"

            mc "Haha..."

    n "E você tem razão, dá pra ver o sol. O dia ajudou nosso passeio."

    mc envergonhado "Verdade... o sol, né? Se for chover vai ser depois."

    n "Sim. Vai dar pra gente curtir bastante, [mc]."

    if nathan_namoro:

        n "Nunca vi namoro que a gente não consegue fazer nada juntos."

    n "A gente tava precisando de um tempo assim."

    mc charmoso "Exatamente. Isso que eu tava pensando hoje quando eu acordei."

    scene nex1_evento2 with Dissolve(1.0)

    pause

    n "Acho que a gente nunca conversou sobre coisas do dia-a-dia. Tipo, como é sua vida aqui na capital?"

    n "Eu sou uma companhia terrível. A gente já se conhece há tanto tempo e acho que nunca perguntei nada..."

    menu:
        "Eu sinto um pouco falta de conversa assim.":


            mc desculpa "Eu sinto um pouco falta de conversar essas coisas com você mesmo."

            mc "Pode falar sobre as coisas do dia e saber o que tá rolando com você também."

            n "Imagino... desde que a gente se conheceu só foi pedreira atrás de pedreira."

            mc "Bom, mas hoje não, né?"

            n "Com certeza."
        "Relaxa. A gente tá sempre correndo.":


            mc "Não pensa demais nisso. As coisas são assim. A vida não é fácil."

            n "Às vezes parece adulto demais, [mc]."

            mc "Que nada, é só tá aqui na praia contigo que me deixa mais zen."

            n "E ainda por cima encontra timing pra dar em cima. Só você..."

    n "Estar com alguém que entende a gente e fica do nosso lado é incrível, sabe? Eu queria conseguir passar isso pra você também."

    mc safado "Você já passa muita coisa sendo gostoso desse jeito."

    n "Ei, [mc]... hoje você não quer brincar."

    mc charmoso "Pelo contrário. Hoje eu quero. Mas falando sério, faz bastante tempo que eu queria passar um tempo assim contigo."

    mc "E eu tenho que admitir que você é mais bonito do que eu imaginava. Eu tô meio bobo ainda."

    n "Você vai falar qualquer coisa pra me conquistar. É o que eu tô sentindo."

    mc envergonhado "Dessa vez é sério. Seu corpo é perfeito..."

    n "Então olha aqui."

    scene nex1_evento3 with Dissolve(1.0)

    pause

    n "Assim você gosta?"

    menu:
        "Exatamente assim...":


            mc safado "Desse jeito..."

            n "Acho que é a primeira vez que alguém fala alguma coisa assim pra mim."

            mc charmoso "Que absurdo. O que esse povo tem na cabeça?"

            n "Você que tá fissurado demais... mas eu fico feliz."

            n "E assim?"

            window hide

            pause

            scene nex1_evento4 with Dissolve(1.0)

            pause

            mc "Perfeito."

            mc "Quem dera eu tivesse um corpo desses."

            n "Você também é gato, [mc]."

            mc envergonhado "Obrigado, mas eu tenho espelho..."

            n "Você só precisa de alguém pra falar isso pra você sempre, igual você tá fazendo comigo."

            mc "Eu acho que não é só isso não..."

            n "Para de ser bobo."
        "Agora você tá se achando demais.":


            mc safado "Acho que eu aumentei sua autoestima demais..."

            n "Haha... tô fazendo papel de bobo agora?"

            mc "De jeito nenhum..."

            n "Agora você me deixou com vergonha."

    scene nex1_evento5 with Dissolve(1.0)

    pause

    n "Eu sei que eu sou bonito. Depois de passar a vida toda ouvindo isso, parece que a gente só acredita."

    n "E é óbvio que ser bonito ajuda. Parece que as pessoas são mais legais mesmo que você não faça nada."

    mc envergonhado "Deve ser bom..."

    n "Mas isso é só no começo, viu?"

    n "Se você for babaca com elas, elas vão te mandar pastar igual."

    mc "Sei..."

    n "Mas eu sou muito mais você, [mc]. Você sabe ouvir, sabe apoiar a gente."

    n "Em nenhum momento eu lembro de você falando qualquer coisa negativa pra mim. Nunca julgou ou falou nada, sabe..."

    mc envergonhado "Você tá exagerando."

    n "Que nada."

    scene nex1_evento6 with Dissolve(1.0)

    pause

    if nathan_namoro:

        n "Eu tive muita sorte de você aceitar namorar comigo. Eu acho isso de verdade."
    else:


        n "Eu tenho sorte de poder sair com alguém igual você."

    mc charmoso "Que isso... eu que tive essa sorte. Olha pra você."

    n "É sério, [mc]. Parece que tá cada vez mais encontrar pessoas legais no mundo."

    n "Mas quando eu tô com você, eu sinto de verdade que eu tô de boa."

    mc "Você sempre foi de boa."

    n "Você lembra lá no bar quando a gente se conheceu? Eu com aquelas garotas?"

    mc normal "Lembro."

    n "Então... pode parecer que eu tinha tudo sob controle. Mas manter aquilo é super difícil pra mim."

    n "Quer dizer assim, quando eu tô com outras pessoas, eu sinto que isso me cansa, entende?"

    n "Mas quando eu tô contigo, eu não sinto isso. Eu sinto que eu posso só ser eu e você não vai se cansar de mim."

    menu:
        "Eu nunca vou me cansar de você.":


            mc charmoso "Como assim me cansar? Você é super de boa, [n]. Eu nunca vou me casar de você."

            n "Valeu, [mc]. Você é um cara e tanto."

            mc "Pode parar de se preocupar com isso. Vamos só curtir esse tempo."

            n "Concordo."
        "Isso não é nada de mais...":


            mc "Não acho que seja nada tão assim. Eu sou só um cara de boa."

            n "Não faça pouco caso disso, não. É tipo um poder especial seu."

            mc envergonhado "Pode especial, é?"

            n "Tipo de super herói."

            mc "Haha... tá legal."

    n "Ei. Você viu como o sol tá forte? Vamos lá pro quiosque?"

    mc charmoso "Claro, bora."

    scene black with dissolve

    scene nex1_evento7 with Dissolve(1.0)

    pause

    n "Ufa... melhorou um pouco. Eu sofro um pouco no sol."

    mc charmoso "É. Você é bem branco..."

    n "Arde pra caramba mesmo quando eu fico demais no sol."

    mc "Foi tipo uma armadilha de trazer aqui pra praia?"

    n "Nada. Eu gostei, pô. Não fica pensando nisso. E eu ainda tive a chance de ter ver assim, quase sem roupa."

    mc safado "E eu então? Gostou do presente?"

    n "Verdade, nem agradeci. Mas você comprou a menor que tinha também, né?"

    mc "A moça falou que era confortável e os caralho lá."

    n "É mesmo. Dá pra ver que é coisa de qualidade. Deve ter custado os olhos da cara."

    mc charmoso "Valeu à pena. Ficou bem em você."

    scene nex1_evento8 with Dissolve(1.0)

    pause

    if nathan_namoro:

        n "Quer dizer que meu namorado já tá me sustentando..."

        mc "Haha... eu? Tá louco."

    n "A revista dá uma boa grana, [mc]? Sem querer me meter demais. Se não quiser não precisa falar."

    mc "Olha, a revista até que paga bem. Não dá pra reclamar."

    mc "A questão é que viver aqui na ilha é caro demais."

    if casa:

        mc "Eu tenho meu próprio apê, mas o condomínio, IPTU e o custo de vida de forma geral é demais."
    else:


        mc "Somando aluguel, as contas, IPTU e o custo de vida de forma geral é demais."

    mc "O dinheiro acaba indo todo pelo ralo, sabe?"

    n "É... morar aqui na ilha também, você deu uma boa sorte. Isso aí foda pra caramba. Só gente muito pesada mesmo pra morar aqui."

    mc envergonhado "E eu, né?"

    mc charmoso "Mas fazendo uns bicos aqui e ali eu consigo juntar uma grana pra fazer umas doideiras."

    n "Tipo gastar pra ver um homem gostoso de sunga?"

    mc safado "Exatamente..."

    scene nex1_evento9 with Dissolve(1.0)

    pause

    n "Eu não vou mentir. Eu ganho uma boa grana na Blergh!, só que tô igual você. Eu tô gastando muito também."

    n "Eu ainda tô pagando advogado e um monte de coisa."

    mc desculpa "A [j] ainda acabou ferrando mais ainda você."

    n "Pois é... aquela mulher é um perigo. E você tá lá no ninho dela. Você precisa tomar cuidado."

    mc charmoso "Pode deixar. E obrigado por se preocupar."

    n "Não posso deixar que meu sugar daddy que me dá presentes assim acabe nas mãos daquela mulher."

    mc "Haha..."

    n "Mas eu espero que as coisas melhorem daqui pra frente."

    scene nex1_evento10 with Dissolve(1.0)

    pause

    n "Eu tô adorando o trabalho de modelo. Viajar por aí, desfilar, tirar foto. É um mimo..."

    mc charmoso "Isso é bom."

    n "Eu queria poder só continuar assim, sabe? Sem ter que me preocupar com a merda que os outros fazem."

    mc desculpa "Sei como é."

    n "Às vezes parece que as pessoas só fodem a gente, sabe? Os caras não fazem uma..."

    n "Tipo, tem dia que eu tenho pesadelo e acordo pensando. Qual vai ser a próxima desgraça que vão aprontar."

    mc "Deve ser horrível."

    n "E assim, uma das coisas que me preocupam é que essas merdas possam atrapalhar a gente, sabe?"

    if nathan_namoro:

        n "Principalmente depois que você resolveu namorar comigo. Eu nem acreditei."

        n "Depois de tudo o que eu fiz pra você. Você, sei lá como, você só aceitou e superou tudo aquilo."

        n "Até agora eu fico pensando como você conseguiu. Eu não sei se eu ia aguentar..."

        mc charmoso "[n]... você é um cara do bem. Isso é o que eu sinto de verdade, dentro de mim."

        mc "Eu sinto que você é um cara foda. Não é só lindo e gostoso... você é de boa, você é legal, good vibes."

        mc "Só que foram essas pessoas que complicaram sua vida. Não foi você. Você só caiu em uma armadilha."

        mc "Pode ser que eu esteja aqui passando pano, mas é o que eu sinto, de verdade."

    scene nex1_evento11 with Dissolve(1.0)

    pause

    n "Você não acha que se pintar outra merda dessa é o fim pra gente?"

    n "Porque isso é uma coisa que eu penso muito."

    mc preocupado "Tadinho... por isso que eu falo que você é legal, [n]."

    mc charmoso "Não sei se eu fico triste por você viver preocupado assim ou se acho fofo esse seu jeito."

    n "Eu tô falando sério, [mc]..."

    n "A [j] pode voltar a qualquer hora. Acho difícil ela ter ficado satisfeita. Ela deve tá cavocando alguma coisa."

    n "E se da próxima vez sobrar pra você? Ela não tá sozinha. Ela pode ferrar você dentro da redação e até fora."

    n "Se ela ou qualquer outra pessoa te ferrar por minha causa, eu sei lá o que eu faço..."

    mc preocupado "[n]..."

    scene nex1_evento12 with Dissolve(1.0)

    pause

    mc "Pare de pensar demais nessas coisas. Cadê o [n] de boa? Aquele cara livre que queria curtir a vida?"

    n "Não sei, [mc]... eu não sei o que aconteceu comigo."

    mc "O que aconteceu é que essas pessoas entraram na sua cabeça. Elas tiraram sua vontade de viver."

    mc "Elas falaram tanta merda e fizeram tanta merda com você que agora você vive com medo."

    mc "Valeu por querer me defender, mas pensar nisso só vai piorar a situação pra você."

    mc "Só vai deixar você mais ansioso e mais, sabe... bloqueado. Com mais medo da vida."

    n "Eu sei, mas é o que eu sinto..."

    mc "Olha, primeiro, eu sei me cuidar. Quero que você não se esqueça disso. Eu sou grandinho."

    mc "Segundo, você não pode deixar que as outras pessoas digam o que você pode gostar e o que você deve sentir."

    mc "Eu gosto de você e foda-se. Não importa se alguém fala merda pra mim. Eu ignoro eles."

    mc "A gente não tem que provar nada pra ninguém. Deixa eles com o ódio deles."

    n "Eu queria pensar assim, mas o mundo não é simples assim, [mc]. As pessoas são más. Elas são cruéis."

    mc "Eu sei..."

    scene nex1_evento13 with Dissolve(1.0)

    pause

    mc "Não tô falando que é fácil e que tudo vai ser tranquilo. O que eu tô falando que você pode controlar o que você sente."

    mc "Ter medo e ódio dessas pessoas só vai dar mais razão pra elas. Foda-se elas."

    mc "A gente vai ser feliz não importa o que elas jogarem em cima da gente. E eu não vou desejar o mal pra elas."

    mc "Eu tô pouco me fodendo pro que eles acham. Eu não vou viver com medo e com ódio por causa deles."

    n "Eu queria... eu queria ter essa sua força, [mc]."

    mc "Mas você pode ter!"

    n "Eu sei... mas eu não consigo. Eu tô nervoso agora só de pensar nisso tudo."

    "O [n] tá precisando que eu tome as rédeas dessa situação."

    "Ele é grande e musculoso, mas por dentro ele continua muito assustado."

    "Se eu não acalmar ele, eu sinto que ele vai sofrer isso pra sempre."

    menu:
        "Dar um beijo nele":


            "Só falar não vai adiantar nada. Eu vou mostrar pra ele como se sentir seguro comigo."

            mc "[n], não adianta só ouvir. Emoção e razão são coisas diferentes. Então olha bem nos meus olhos."

            n "Certo. O que vo-"
        "Melhor agora não":


            "O [n] não tá legal. Deixa pra outro dia."

            mc "Não adianta eu ficar falando aqui um monte de coisa. Eu só quero que você saiba que eu vou tá com você."

            mc "Enquanto você quiser que eu fique do seu lado eu vou ficar."

            if nathan_namoro:

                mc "Agora que a gente tá sério, eu quero que você saiba disso. Eu tô com você, pra tudo."
            else:


                mc "Eu sei que a gente não tem nada sério ainda, mas pra mim não importa. Eu realmente gosto de você."

            n "Eu também gosto de você e quero ficar com você, [mc]. Acho que no fundo é só isso que eu quero."

            n "Valeu... já tô me sentindo melhor."

            mc "Isso aí."

            n "Agora vem aqui."

            mc "Opa!"

            scene nex1_evento14 with Dissolve(1.0)

            pause

            jump nathan_ex1_final

    scene nex1_evento15 with Dissolve(1.0)

    pause

    n "Hmmm!"

    mc "..."

    n "É assim que você vai me mostrar?"

    mc "Deu pra ver?"

    n "Não."

    window hide

    pause

    scene nex1_evento16 with Dissolve(1.0)

    pause

    mc "!"

    n "Agora sim..."

    mc "Hmmm..."

    "Que delícia poder beijar o [n] assim."

    n "Só você pra me fazer me sentir bem assim, [mc]..."

    window hide

    pause

    scene nex1_evento17 with Dissolve(1.0)

    pause

    mc "N-nathan?!"

    n "Que foi? Só quero te fazer um carinho..."

    mc "V-você tá pegando-"

    n "Não tá certo só você me fazer me sentir bem... eu quero contribuir."

    mc "M-mas-"

    n "Shhh... é só um carinho..."

    mc "E-eu..."

    n "É ruim?"

    mc "N-não..."

    scene nex1_evento18 with Dissolve(1.0)

    pause

    mc "Tá muito b-bom..."

    n "Eu imaginei... agora deixa tudo comigo."

    mc "Ah..."

    n "..."

    mc "Ah!"

    n "Isso..."

    mc "{i}puf puf{/i}"

    mc "O-obrigado... e você?"

    n "Eu já tô muito legal."

    mc "Mas-"

    n "Relaxa, [mc]. Não é assim que você fala? Vem aqui."

    scene nex1_evento14 with Dissolve(1.0)

    pause

    n "Eu curti nosso beijo. Fique até meio sem ar."

    mc "V-você que deixou... eu não... esperava alguma coisa assim..."

    n "A gente ainda vai ter outros encontros... isso é só o começo, [mc]."

    mc "Tô gostando de onde isso tá indo..."

    label nathan_ex1_final:

        n "Esse passeio tá sendo bem o que eu precisava. Eu sabia que você era incrível."

    mc "Ei, eu tô curtindo muito também. Você precisa entender logo que você é a dama e eu o vagabundo da relação."

    n "Apos que é mais uma das suas referências de 50 anos atrás..."

    mc "Você não conhece a Dama e o Vagabundo?"

    n "Nunca ouvi falar."

    mc "Caraca..."

    show white with Dissolve(0.3)

    hide white with Dissolve(0.3)

    mc "Uou..."

    n "Parece que vai chover. É meio perigoso a gente ficar na praia com raio."

    mc "Tem razão. É melhor a gente ir."

    n "Você me acompanha até o centro?"

    mc "Claro."

    n "Antes de eu te soltar, você tem que me prometer que a gente vai sair assim de novo."

    n "Tipo, um passeio igual hoje. Sem problema, só pra gente curtir. Eu prometo que eu não vão chorar no seu ombro de novo."

    mc "Você pode chorar pra mim sempre que quiser, [n]. E claro que eu prometo. A gente vai sair muito ainda."

    n "Então tá. Vou acreditar em você."

    scene black with Dissolve(1.0)

    mc "Você vai até em casa?"

    n "Não. Eu vou resolver uns assuntos no centro. Se você ir comigo?"

    mc "Parece coisa de marido e mulher esse negócio de resolver coisa..."

    n "Quem sabe? Pode ser um treino pro futuro..."

    mc "Só se tiver AQUELE casamento."

    n "Sem problemas pra mim."

    mc "Vou pensar no seu caso..."

    "..."

    "Uou... esse encontro foi melhor do que eu imaginava..."

    "Não vejo a hora de sair com o [n] de novo."



    $ tempo = 3

    jump call_cidade



label praia_especial_sofia_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("soex1_save", extra_info="soex1_save")

    $ estou_na_cidade = False

    $ praia_sofia_local = True

    "O que eu vou falar pra [w] pra fazer ela vir pra praia comigo?"

    "A gente se aproximou bem mais nos últimos tempos, mas pra ela vir de biquíni sensual na praia comigo... acho que é muito."

    "Minha vontade era deixar um biquíni de presente pra ela com uma cartinha chamando ela pra vir, mas é arriscado demais."

    "Eu ia gastar os olhos da cara naquela loja de roupa e ela só ia botar fogo no presente e ainda comer meu coro."

    "Acho melhor eu ligar pra ela antes."

    "..."

    w "Alô?"

    mc normal "[w]? Aqui é o [mc], tudo bem?"

    w "Sim. O que você precisa?"

    mc envergonhado "Direta como sempre."

    w "Claro. Não tenho tempo pra perder com ladainha."

    mc "Então..."

    menu:
        "Quer vir na praia comigo?":


            mc charmoso "Vou ser direto. Eu tava afim de vir na praia contigo."

            w "Praia?!"

            mc envergonhado "É-é... eu sei que-"

            w "Pera..."

            w "Eu aceito."

            mc "Eu sabia, mas valeu a tentativa mesmo assim, n...-{nw}"

            mc surpreso "Q-quê?! S-sim?!"

            w "Sim."
        "E se... a gente tirasse uma folga?":


            mc normal "Tava pensando se você não ia querer dar uma volta. As coisas tão meio tensas na redação."

            w "Não nego que tá meio pesado o clima aqui, igual sempre..."

            mc "Será que não seria uma boa a gente beber alguma coisa talvez?"

            w "Beber? Você tá louco?"

            w "Mas... quem sabe..."

            mc desconfiado "Hm? Que foi?"

            w "E se a gente for na praia?"

            mc surpreso "P-praia?!"

            w "É."

    w "Eu tenho que ir aí. Mas eu tenho uma condição."

    mc surpreso "Q-qualquer coisa!"

    w "Você paga o almoço pra mim, que eu sei que é caríssimo comer aí."

    menu:
        "Claro.":


            mc charmoso "Pode deixar. Claro que eu ia pagar pra você, né?"

            w "Sei lá... não imagino você com dinheiro pra gastar com essas coisas. Não quero abusar também."

            mc zerado "Tá me chamando de pobre?"

            w "Desculpa... não era a intenção."

            mc "Sei..."
        "Mas você que é a chefe aqui...":


            mc zerado "Não é você que é a chefe?"

            w "É. Mas eu não ganho o suficiente pra almoçar aí."

            mc "E eu ganho?"

            w "Então não dá?"

            mc "..."

            mc "Ok. É por minha conta hoje."

    w "Então tá combinado! Eu vou terminar aqui um negócio, vou pra casa e já te encontro lá."

    mc surpreso "Q-quê?! Agora?!"

    w "É, ué. Minha agenda é apertada e eu quero resolver isso o mais rápido possível."

    mc desconfiado "Resolver? Resolver o quê?"

    w "Eu te conto quando a gente se ver."

    mc "T-tudo bem! Vou me trocar também!"

    w "Tá. Tchau."

    "Não acredito... ela realmente aceitou sair na praia comigo! Como assim?!"

    "Foi até fácil demais...{w} Será que tem caroço nesse angu?"

    "Não adianta ficar matutando isso agora. Esse dia precisa ser perfeito!"

    scene black with dissolve

    "..."

    scene ape_geral with Dissolve(1.0)

    "Não tenho tempo pra mais nada. Só colocar o shorts mesmo!"

    "Gogogogo!"

    "[w] na praia... ainda não tô acreditando..."

    scene black with dissolve

    "..."

    scene ilha praia_gazebo with Dissolve(2.0)

    pause

    "Tô aqui. A [w] deve chegar logo."

    "..."

    "Ver a [w] de biquíni... a chefinha... a mulher mais casca grossa que eu já conheci..."

    "Tá bom demais pra ser verdade! Eu tô muito ansioso!"

    w "[mc]."

    "Chegou a hora!"

    "[w] de biquíni!"

    scene black with dissolve

    w "[mc]? O que você tá fazendo de olho fechado?"

    mc concentrando "Estou saboreando esse momento..."

    w "Que momento?"

    mc "Shiu. Me deixa."

    w "Você tá bem estranho."

    mc "Tô pronto."

    mc surpreso "!!!"

    scene soex1_imagem1 with Dissolve(1.0)

    pause

    w "Olá."

    mc zerado "..."

    w "Que foi?"

    menu:
        "Legal ver você com uma roupa diferente.":


            mc envergonhado "Não é nada..."

            w "Você tá com uma cara meio estranha. Você tava esperando alguma coisa?"

            mc charmoso "C-claro que não. É que você ficou bem nessa roupa. Acho que é a primeira vez que te vejo mais casual assim."

            w "Minha roupa do trabalho não é casual?"

            mc zerado "Aquela roupa não conta. Você usa ela TODO dia. Você lava ela?"

            w "Quê?! Claro que eu lavo, idiota... é que eu tenho mais de uma..."
        "Por que você não tá de biquíni?":


            mc angustiado "Por que você não tá de biquíni?!"

            w "E-eu tô de biquíni..."

            mc desconfiado "Tá?"

            w "Tá por baixo..."

            mc safado "E você vai tirar a roupa pra aproveitar?"

            w "Claro que não."

            mc zerado "Mas..."

            w "..."

            mc "Ok..."

    mc normal "Então... vamos curtir o sol um pouco?"

    w "Curtir? Não sei, [mc]... Eu não gosto muito de sol..."

    mc zerado "O que você veio fazer aqui então?"

    w "Você tem razão. Acho que é melhor eu voltar pra redação."

    mc surpreso "C-como assim?! Você acabou de chegar!"

    w "Eu pensei que... vindo aqui com alguém conhecido eu ia conseguir fazer... mas... é impossível."

    mc desconfiado "Não tô entendendo porra nenhuma..."

    w "A verdade é que apareceu uma proposta pra revista... mas pra dar certo depende de mim."

    mc normal "É coisa boa?"

    w "Sim. É muito boa. Envolve um bom patrocínio. É de uma marca que compete com a Blergh! aqui na capital."

    mc "Marca de roupa?"

    w "É. Eles são maiores que a Blergh!, mas eles tão crescendo muito, e essa marca agora quer reforçar sua presença."

    mc "Isso é incrível pra revista. Que beleza."

    scene soex1_imagem2 with Dissolve(1.0)

    pause

    w "Só que... o foco da campanha deles é o empoderamento da mulher. Aí que tá..."

    mc preocupado "E qual o problema? Você não concorda com isso?"

    w "Claro que eu concordo, sem noção. Eu sou uma mulher que sofreu muito pra conquistar o respeito na revista..."

    mc desconfiado "Então não entendi o problema..."

    w "O problema... é que a marca só aceita anunciar na revista se EU for a modelo..."

    mc surpreso "C-como?!"

    w "Eles querem usar a minha trajetória como uma história pra inspirar a campanha..."

    "Meu Deus..."

    menu:
        "Hahahaha! Se fodeu!":


            "A [w] como modelo?! Essa foi de cair o cu da bunda!"

            mc feliz "Hahaha! Caralho! Essa foi demais, [w]!"

            w "..."

            mc "Não consigo parar de rir! A chefinha modelo ?!"

            w "Acabou a graça?"

            mc envergonhado "D-des... haha... desculpa... mas me pegou meio de surpresa."

            w "Eu sei que não faz sentido... por isso que... eu vou desistir dessa coisa. Não tem nada a ver comigo."

            mc normal "Calma. Não precisa desistir assim. Você nem tentou ainda."

            w "Nem preciso..."
        "Isso é incrível, [w]!":


            "Por mais sem noção que isso pareça, melhor eu não preocupar ela ainda mais..."

            mc charmoso "Isso é incrível, [w]. É um reconhecimento de todo seu trabalho. Além de ser uma inspiração pra outras mulheres."

            mc "Era pra você tá orgulhosa. Parabéns, garota."

            w "Eu sei... se fosse qualquer outra coisa... tipo dar uma palestra ou até assinar um livro..."

            w "Só que... modelo... ainda mais de roupa de banho?"

            mc envergonhado "É... coisa de louco mesmo..."

    "Ela não pode desistir. Pelo bem da revista e pelo meu bem! Eu não saio dessa praia antes de ver ela de biquíni!"

    mc envergonhado "Você tá super certa de ficar incomodada... realmente não tem nada a ver com você isso."

    w "Eu sei... não precisa ficar falando..."

    mc charmoso "Só que tem uma questão aí. A luta das mulheres sempre foi de superar o status quo, certo?"

    mc desculpa "Elas não podiam votar, depois tinham que ficar em casa, e até hoje é difícil, às vezes ganhando menos que homens fazendo a mesma coisa."

    mc charmoso "Talvez, o que essa marca quer, é realmente desafiar uma mulher. Mostrar que você pode ir contra o que tá estabelecido."

    w "Você tá falando isso só pra me convencer?"

    mc envergonhado "Claro que não... eu acho que-"

    w "Tá bom! Eu tiro!"

    mc surpreso "S-sofi-"

    scene soex1_imagem3 with hpunch

    pause

    mc surpreso "..."

    w "Você tem razão. Eu não sou mais criança. Não vou ficar com birra por causa de uma roupa idiota. Eu faço o que eu tenho que fazer."

    mc "..."

    w "Que foi?"

    menu:
        "Isso aí! Conseguiu!":


            mc normal "Parabéns! Isso que é determinação!"

            w "É só uma roupa que toda mulher usa na praia, certo?"

            mc "Sim. Não tem nada de mais."

            w "Ainda é um pouco demais pra mim, mas se eu não tirasse a roupa logo, ia acabar desistindo."

            mc "Você teve coragem. Parabéns mesmo."
        "Uou... você tá incrível...":


            mc tarado "Caraca... você tá incrível com esse biquíni..."

            w "Você realmente quer que eu vá embora, né?"

            mc angustiado "N-não! É um elogio!"

            w "Elogio o escambau. Para de ficar olhando pra mim que eu só me sinto pior."

            mc concentrando "Ok..."

            w "Não precisa fechar os olhos também... não quero que você caia de cara na areia. Só não ficar me secando."

            mc envergonhado "Vou tentar..."

    w "A sorte é que a praia também tá meio vazia... tem um gato pingado aqui e lá... mas eu achei que ia ter mais gente."

    mc normal "Normalmente aqui é tranquilo. A ilha é pequena, né? Só gente de grana que vem pra cá."

    w "É... mesmo assim... eu tô me sentindo meio vulnerável... não sei explicar..."

    "Ainda não acredito que eu tô vendo a [w] de biquíni. Não achei que fosse possível..."

    "Tenho que aproveitar o máximo pra guardar essa imagem na cabeça. Certeza que eu nunca vou ter outra chance."

    "Mas se eu ficar olhando pra ela, certeza que vou tomar um cascudo. E agora?"

    menu:
        "Dar uma boa conferida na [w]":


            "Foda-se."

            show soex1_imagem4 with Dissolve(1.0)

            pause

            "Olha só pra isso. Até que a chefinha tem um corpo bacana. Ela é magrinha, a pele dela parece de criança. É perfeita."

            "Ela não tem um corpão, mas é tudo bem equilibrado. Ela é magrinha, com um peito bacana, não tem muito quadril... mas não é tábua."

            w "[mc]? Que que você tá fazendo?!"

            window hide

            pause

            hide soex1_imagem4 with Dissolve(1.0)

            mc envergonhado "D-desculpa... acho que eu viajei um pouco."

            w "Você tava olhando pro chão?"

            mc "Sei lá... tava só viajando mesmo."

            w "Hmm... nem ouviu nada do que eu disse, né?"

            mc "Desculpa..."

            w "Idiota..."
        "Não vou fazer isso com ela":


            "Não vou causar. Melhor eu participar da conversa."

            mc charmoso "Não é uma coisa que você tá acostumada. Por isso que você tá com essa impressão."

            mc "Eu tô de shorts e você tá me vendo quase pelado também."

            w "É... isso é verdade... eu só preciso me acostumar."

            w "Sabe... é raro, mas às vezes você fala a coisa certa. Obrigada."

            mc zerado "Como assim é raro?"

            w "Eu tô te elogiando. Não se apague a detalhes."

            mc "..."

    scene soex1_imagem5 with Dissolve(1.0)

    pause

    w "Certo... agora eu tô de biquíni... eu preciso me acostumar com essa sensação."

    mc desconfiado "Assim... você vai ser modelo da marca mesmo? Vai ter que aceitar que eles tirem foto de você e tudo?"

    w "É, né? Usar o biquíni é só a primeira parte. Mas se eu não conseguir me acostumar com ele, o resto não adianta."

    mc normal "Tem razão. Depois de um dia na praia, certeza que você vai sair daqui de boa."

    w "Vamos ver..."

    w "Mas agora é hora de você me pagar o almoço."

    mc envergonhado "Você ainda lembra disso?"

    w "Claro. Eu vou querer tudo do bom e do melhor daquele quiosque alí."

    mc normal "Mas nunca tem ningué-"

    mc surpreso "O cara tá lá hoje!"

    w "Não entendi nada, mas bora comer."

    "Um almoço aqui vai custar os olhos da cara..."

    mc angustiado "..."

    scene black with dissolve

    w "Eu vou querer uma porção de camarão com catupiry original por favor."

    mc surpreso "!"

    "Rapaz do Quiosque" "Pode deixar! Uma de camarão saindo!"

    mc envergonhado "Eu não vou querer nada... valeu..."

    "..."

    "Rapaz do Quiosque" "Eu vou ali atrás, qualquer coisa depois eu volto, hein."

    w "Obrigada."

    scene soex1_imagem6 with Dissolve(1.0)

    pause

    mc normal "Gostou?"

    w "Hmm... tava uma delícia. Você não quis pedir nada pra você?"

    mc zerado "Tô sem fome..."

    w "O preço é meio salgado mesmo, mas vale à pena. É uma coisa única pra fazer de vez em quando, né?"

    mc "..."

    w "Eu adoro refri... eu sei que faz mal, mas é bom."

    mc normal "Haha..."

    w "Que foi?"

    mc "Você parece uma criança aproveitando o lanchinho. Toda feliz aí por causa de um refrigerante."

    w "Mas é gostoso mesmo. Sua voz tá atrapalhando esse momento maravilhoso."

    mc "Toma tranquila aí então."

    scene soex1_imagem7 with Dissolve(1.0)

    pause

    "Quem diria que a [w] ia gostar tanto assim de uma coisa tão simples."

    "Às vezes ela é meio séria, mas no fundo acho que ela é igual todo mundo. Tem seus pontos fracos também."

    w "Se você fica quieto desse jeito também eu sinto que você tá tramando alguma coisa."

    mc "Você quer que eu fale ou não?"

    w "É melhor você ficar em algum lugar que eu possa ver você. Pra ter certeza que você não tá fazendo nada sacana."

    menu:
        "Calma. Eu só tô aproveitando a vista.":


            mc safado "Eu só tô aproveitando a vista. Nada de mais."

            w "{i}Hmpf{/i}"

            mc "Que foi?"

            w "Quando você fala assim eu sinto que você tá pensando besteira."

            mc envergonhado "Eu? Imagina..."

            w "Vem logo pra cá."

            mc "Ok..."

            window hide

            pause
        "Eu vou aí.":


            mc "Tudo bem. Eu vou aí. Mas tu gosta de mandar mesmo, hein?"

            w "Eu gosto das coisas certas, só isso."

    scene soex1_imagem8 with Dissolve(1.0)

    pause

    w "Eu sei que é o que a gente tinha combinado, mas mesmo assim, obrigada por pagar o almoço."

    w "Eu não costumo sair muito."

    mc normal "Acho que todo mundo sabe disso."

    w "Por isso que eu acho que eu tô aproveitando até um pouco demais. Valeu."

    menu:
        "Valeu a pena pra ver você de biquíni.":


            mc tarado "Valeu pra ver você de biquíni."

            w "Você não consegue responder sem falar alguma coisa idiota?"

            mc "Me falaram que a gente tem que ser sincero com as pessoas."

            w "Você tá levando isso à risca demais. Nem tudo você precisa falar. Principalmente esse tipo de coisa."

            mc charmoso "Vou lembrar pras próximas vezes."
        "A gente precisa fazer mais vezes.":


            mc charmoso "A gente podia fazer isso mais vezes. Curtir um pouco mais tudo o que tem aqui na ilha."

            w "É... às vezes eu penso que seria bom. Quem sabe."

            mc "Já é um avanço. Se fosse quando a gente se conhecer você só ia sair andando."

    mc normal "Inclusive, eu sinto que você tá se abrindo bem mais."

    w "Sério? Eu não acho."

    mc charmoso "É sério. Você mudou bastante, [w]."

    w "Hmm..."

    scene soex1_imagem9 with Dissolve(1.0)

    pause

    w "Só sei que esse almoço deu um sono agora... e se a gente voltar?"

    mc surpreso "Q-quê?! Já?!"

    w "Eu tô cheia e até esqueci do biquíni pra falar a verdade..."

    "Não! A gente não pode ir ainda! Nem rolou nada entre a gente e ela tá muito gata com esse biquíni."

    mc preocupado "Tá louca? Esqueceu nada."

    w "Eu já tô super de boa com ele."

    mc zerado "Eu fiquei cinco segundos sem falar nada do seu lado e você já não aguentou."

    w "Saco... a gente já comeu. O que eu faço agora?"

    mc normal "Calma. Tem muita coisa pra fazer na praia ainda. Além de que você é muito branca."

    mc "E se a gente tomar um sol?"

    w "Eu já falei que não gosto de sol, [mc]... e nem de praia... e nem de usar uma roupa que me deixa quase pelada."

    mc "Para de reclamar. É pelo bem da revista. Você tem que fazer o melhor por todos que trabalham lá."

    w "Credo... você sabe ser convincente quando você quer. Ok. O que eu faço?"

    mc "Vem comigo. Vou pegar umas cadeiras pra gente."

    w "..."

    scene black with dissolve

    "..."

    mc "Pode sentar."

    scene soex1_imagem10 with Dissolve(1.0)

    pause

    w "E agora?"

    mc "Agora a gente fica aqui um pouco tomando sol."

    w "Sério mesmo que as pessoas perdem tempo fazendo isso?"

    mc "Você nem sabe como é. Talvez você goste."

    w "Acho difícil. Além de que nem tudo a gente precisa fazer pra saber que não gosta. Tipo tomar um sopapo na cara."

    menu:
        "Nisso você tem razão.":


            mc "Pode ser que você esteja certa, só que comparar um tapa com tomar sol na praia é um pouco exagerado."

            w "Hmm..."
        "Um tapinha não dói...":


            mc "Nunca ouviu aquela... 'um tapinha não dói?'. E se você gostar?"

            w "Para de ser ridículo, [mc]. Você fala cada uma."

            mc "Haha..."

    mc "Eu só tô querendo dizer que você precisa se abrir pras coisas. No fundo, isso aqui não é justamente sobre isso?"

    w "Tem razão. No fundo você tá certo. Eu preciso me abrir mais pras coisas."

    mc "Isso aí."

    w "E agora? A gente fica aqui? E volta cheio de bolha e ardendo pra casa?"

    mc "Ah. Você precisa passar protetor. Mas eu não trouxe..."

    "Que merda... seria uma boa chance de passar nela... s-se ela aceitasse..."

    w "Eu trouxe. Tá junto com a minha roupa. Eu deixei lá no quiosque."

    mc "Vou pegar."

    scene black with dissolve

    "..."

    scene soex1_imagem12 with Dissolve(1.0)

    pause

    w "Falar a verdade... eu não lembro de ter feito isso na vida..."

    menu:
        "Sério? Você não teve infância?":


            mc zerado "Como assim? Você não teve infância, não?"

            w "Pelo que você conhece do meu pai... você realmente acha que a gente ia bastante na praia?"

            mc envergonhado "Bom... falando desse jeito..."

            w "Quando eu falo que é uma coisa nova pra mim, realmente é. Tudo isso aqui."

            mc "Não é à toa que seu coração acabou virando de pedra com os anos..."

            w "Calado..."
        "Se quiser, eu posso ajudar.":


            mc charmoso "Se você não tá acostumada, eu posso ajudar."

            w "Sério? Mas você sabe?"

            "Isso! Tenha calma, [mc]... não assuste ela."

            mc "É que quando outra pessoa passa, dá pra ver melhor onde ficou faltando. É mais seguro."

            w "Verdade... é melhor tomar cuidado com essas coisas, né?"

            mc "Com certeza."

            w "Por isso que eu gosto de sair com você, [mc]. Sempre pensando em mim primeiro."

            mc envergonhado "Não é nada de mais... só pra ajudar mesmo."

            w "Verdade... além de tudo é humilde."

            mc normal "Pode me passar o protetor?"

            w "Não é possível que você tava acreditando, né?"

            mc angustiado "Aaah!"

            w "Essa ladainha pode funcionar com essas garotas que você sai, mas aqui não, inocente."

            "Tava bom demais pra ser verdade..."

    w "Mas é bem simples. Eu li as instruções e até pedi dicas pro vendedor quando eu fui comprar."

    mc envergonhado "Claro que você fez isso..."

    w "É importante tá sempre preparada, né?"

    mc "Até pra ir pra praia..."

    w "Aliás, você não vai sentar, não?"

    "Que pena... a vista tava boa..."

    scene black with dissolve

    scene soex1_imagem11 with Dissolve(1.0)

    pause

    mc desconfiado "Que foi agora?"

    w "Quanto tempo a gente vai ter que ficar aqui?"

    mc zerado "[w]... você tá parecendo uma criança pentelha."

    w "..."

    "Na redação a [w] parece tão certa do que tá fazendo. Ela tá totalmente diferente aqui."

    mc normal "Seria bom você ficar o dia todo. Pra ter certeza que vai ficar à vontade quando for tirar as fotos."

    w "Então a gente só fica quieto aqui sentado e as passam e olham pra gente?"

    mc envergonhado "A gente pode conversar sobre alguma coisa..."

    w "E sobre o que você quer falar?"

    mc "Sei lá... você que não quer ficar quieta tomando sol. Fala você alguma coisa."

    w "Tá. É..."

    w "Eu queria te perguntar uma coisa, só que eu não sei se é uma boa. A gente ainda trabalha juntos, entende?"

    mc "[w]... depois do que aconteceu no bar, não tem muito o que a gente possa estragar mais..."

    w "Sério? Eu não lembro direito o que aconteceu..."

    mc "Melhor pra você."

    mc normal "Mas pode ficar tranquila. Só me fala o que você tá pensando."

    scene soex1_imagem13 with Dissolve(1.0)

    pause

    w "É... você acha que eu tô fazendo papel de ridícula?"

    mc desconfiado "Por que ridícula?"

    w "Olha pra mim, [mc]... isso não tem nada a ver comigo. Olha pro meu cabelo. Não lembro a última vez que eu penteei ele."

    w "Eu não passo maquiagem, não cuido do meu corpo. Eu sou desengonçada, meu nariz é meio vermelho... nada a ver, sabe?"

    w "Por que alguém ia pedir pra eu ser modelo? E se for uma piada?"

    mc desculpa "..."

    w "Você também acha que é?"

    mc "Não é isso. Eu tô pensando também por que teriam chamado você pra ser modelo. Não faz muito sentido."

    w "T-também acho. Tudo isso é uma besteira."

    mc normal "Mas eu não acho que uma empresa famosa do tamanho dessa marca aí ia gastar uma grana preta pra fazer piada."

    w "Eu sei... então por que?"

    menu:
        "Eles querem desafiar as expectativas.":


            mc charmoso "Eu acho que eles querem no fundo é desafiar o que tá aí. Justamente trazer uma coisa diferente."

            mc "A maioria das modelos são atrizes ou garotas lindas, perfeitas, mas que não tem conteúdo ou história."

            mc "Mesmo que você não seja uma profissional dessa área, você tem um nome. Você é uma das chefes da revista."

            mc "Uma mulher que passou por muita coisa estudando fora e agora voltou e assumiu o controle de uma empresa gigante."

            mc "Muito mais que sua aparência, o que eles querem é esse conteúdo que você traz com você."

            w "[mc]... você tem razão... eu também acho que é isso."

            mc "E isso não é ser piada ou ridícula, certo?"

            w "Você tem bastante jeito com as palavras quando você se esforçar. Talvez você devesse deixar de ser paparazzo e virar redator."

            mc surpreso "Você acha que eu teria chances?"

            w "Com certeza. Se você parar de idiotice e ser assim sempre, concentrado e preocupado com o que tá falando, com certeza."

            mc zerado "Não sei se você tá me elogiando ou não..."
        "Você é mais gostosa do que pensa.":


            mc charmoso "Olha... eu sei que você não curte esse tipo de comentário, mas presta atenção."

            scene soex1_imagem14 with Dissolve(1.0)

            pause

            mc "Pra mim, você tá se dando pouco valor. Pode ser que você realmente não se cuide tanto quanto outras pessoas que você tá se baseando."

            mc "Mas isso não quer dizer que você é gata e gostosa."

            mc "Quando eu olho pra você, eu acho seu corpo muito bonito e você não é feia, nem de longe."

            mc "Você pode não se achar perfeita igual essas modelos, mas isso não quer dizer que você é ridícula e é uma piada deles."

            mc "Além de que dependendo do que eles querem com essa campanha, talvez uma mulher 'normal', quero dizer, com uma beleza mais real..."

            mc "Talvez uma mulher igual você, que é bonita e gostosa, mas sem aquela pinta de modelo, seja a melhor escolha pra eles."

            w "É sério que você tá falando tudo isso e nem olha nos meus olhos?"

            scene soex1_imagem13 with hpunch

            pause

            mc surpreso "D-desculpa!"

            w "Bom... mesmo parecendo um tarado, talvez você tenha razão. Se eles me querem, é por causa de alguma coisa."

            mc charmoso "É isso que eu quero dizer."

    w "Esse papo me deixou meio ansiosa. E se a gente fosse andar?"

    mc normal "Claro. A praia é perfeita pra andar."

    scene black with dissolve

    "..."

    scene soex1_imagem15 with Dissolve(1.0)

    pause

    w "Ufa... cansei..."

    mc concentrando "Também... a gente andou em tudo o que é lugar."

    w "Acho que foram 30 minutos só."

    mc "Impossível..."

    w "Mas eu cansei também. Acho que eu vou deitar um pouco e depois voltar."

    w "A vista aqui é perfeita. É raro hoje em dia ir em um lugar onde você pode olhar pra frente e não ver nada..."

    mc normal "Verdade. A gente é sortudo de ter um lugar desse tão perto."

    w "Algumas coisa boa essa cidade tinha que ter, né?"

    menu:
        "Dar uma conferida na [w]":


            scene soex1_imagem16 with Dissolve(1.0)

            pause

            "Hoje mais cedo eu nem podia sumir da vista dela que ela já cutucava. Dá até pra aproveitar..."
        "Continuar prestando atenção":


            pass

            "A [w] realmente se soltou. Parece que ela nem tá ligando mais pro biquíni."

            "Nem por isso também eu vou abusar."

    mc normal "Você tem algum problema com a cidade?"

    w "Não com a cidade em si, mas eu já li muita coisa sobre o prefeito Donatello. O que acontece na capital é praticamente um reinado."

    w "Quando não é ele, é alguém da família dele. E assim eles ficam na prefeitura pra sempre."

    w "Não que seja algo ruim, mas tem muita história mal contada. Existem histórias de empresas que foram beneficiadas com dinheiro público."

    mc desculpa "Parece algo complicado..."

    w "Mas outro dia a gente fala disso. Agora eu vou deitar um pouco que esse lugar parece confortável."

    mc normal "Fique à vontade."

    scene black with dissolve

    scene soex1_imagem17 with Dissolve(1.0)

    pause

    w "É melhor eu repassar... a gente tá no sol faz muito tempo."

    mc envergonhado "Mas precisa passar TANTO assim? Olha a camada de meleca na sua perna."

    w "Quanto maior a camada, maior a proteção. E minha pele é super sensível."

    mc "Eu não sei se é assim que funciona..."

    w "A perna é minha, [mc]. Para de ser mala."

    mc "Tá tudo escorrendo aí na cadeira de tomar sol."

    w "Depois eu limpo. Agora deixa eu tomar meu sol."

    window hide

    pause

    scene soex1_imagem18 with Dissolve(1.0)

    pause

    w "Hmmm... até que o sol não é tão ruim assim. E talvez eu até ganhe uma corzinha."

    mc normal "Você preocupada com isso?"

    w "Quando a gente tá na chuva, a gente faz bem de se molhar, né?"

    w "Falar a verdade, fazia tempo que eu não tirava um dia pra fazer nada."

    mc zerado "Já falei pra você pegar mais leve."

    w "Hoje eu comi bem, bebi o que eu queria... tomei sol... relaxei... andei na praia..."

    mc charmoso "E a companhia?"

    w "Hmm... nota 7."

    mc zerado "Por que não foi 10? Faltou mais camarão?"

    w "Eu estou brincando. Não posso dar nota pra você assim. Na verdade você foi muito bacana vindo comigo."

    scene soex1_imagem19 with Dissolve(1.0)

    pause

    w "Aliás, você que me ligou pra sair, né?"

    mc normal "Sim."

    w "Você... não tava pensando que esse seria um 'encontro', né? Tipo, de duas pessoas que se gostam e tal."

    menu:
        "Não tava pensando nisso não.":


            mc envergonhado "Nah. Eu só pensei que você podia curtir um pouco e se salvar na redação."

            w "Hmm... eu não sou muito boa em ler as pessoas. É duro pra mim saber se tão mentindo."

            mc "Mas eu tô falando a verdade."

            w "Tá bom... é melhor assim. Ninguém criando expectativas demais."

            mc "Concordo."
        "É o que eu pretendia...":


            mc envergonhado "Era o que eu tava pensando, né? Te chamar pra uma coisa a dois e tal..."

            w "T-tá falando sério?"

            mc "Tô, poxa... mas nada sem compromisso. Só pra gente ter uma conversa mais pessoal, sabe?"

            w "[mc]... você sabe que a minha vida é uma doideira..."

            w "Eu não queria que você ficasse criando expectativa... eu nem consigo pensar em uma coisa assim agora."

            mc charmoso "Tudo bem. Relaxa. Ninguém aqui tem pressa. A gente vai ter outras oportunidades."

            w "Era p-pra você desistir dessa ideia doida..."

            mc "Ainda não."

    mc charmoso "Mas o importante é que hoje eu consegui curtir um dia bacana com você."

    mc "Deita aí e curte o sol mais um pouco. Eu vou deitar também."

    w "Você tem razão. Vai saber quando eu vou poder sair assim de novo."

    scene soex1_imagem20 with Dissolve(1.0)

    pause

    "Será que eu teria uma chance com a [w]? Pelo menos um dia?"

    "Eu sinto que ela tá se abrindo mais comigo, só que mesmo assim... às vezes eu tenho a impressão que é impossível."

    "Ela é totalmente desligada desse tipo de coisa de namoro, romance e até de um lance mais casual."

    "É um desperdício... porque olha pra ela..."

    w "Hmmm... se continuar assim eu vou dormir aqui."

    mc envergonhado "Se você tá até pensando em dormir, então realmente se deu bem com o biquíni, hein?"

    w "Verdade... eu até esqueci um pouco dele."

    w "Quer saber? Eu vou fazer uma pose."

    mc surpreso "Pose?! Aqui!?"

    scene soex1_imagem21 with Dissolve(1.0)

    pause

    w "Eu estou totalmente relaxada quanto ao meu corpo! Eu sou livre, leve e solta!"

    mc zerado "Deu a louca?"

    w "N-não! Eu tô bem! Tô super bem! Imagina aquele monte de câmera e um cara me pedindo pra fazer poses?!"

    w "Haha! Eu tô super de boa com isso, sabia?! Olha pra mim como eu sou m-maravilhosa!"

    mc preocupado "[w]... calma... um passo de cada vez..."

    w "Eles querem fazer o quanto antes! Mas eu consigo! Eu sou a melhhh..."

    mc "[w]! Tudo legal?"

    w "F-foi só uma tontur-"

    scene soex1_imagem22 with vpunch

    pause

    mc "S-sofia?! C-cuidado!"

    w "T-tem alguma coisa aqui escorregaaaaaan-"

    mc "A merda do protetor que es-"

    w "Aaaah!"

    w "Me segura!"

    mc "E-eu te segur"

    scene soex1_imagem23 with vpunch

    pause

    mc "ARGH!"

    w "AI!"

    w "Eu disse pra você me segurar, idio-"

    scene soex1_imagem24 with vpunch

    pause

    w "AAAHH!"

    mc "E-eu te seguro!"

    w "Eu não quero cair na água!"

    mc "C-calma! T-te peguei!"

    scene soex1_imagem25 with Dissolve(1.0)

    pause

    w "{i}puf puf{/i}"

    mc "Deu... acho que tá segura agora."

    w "Brigada... valeu... {i}puf puf{/i}"

    mc "Eu falei que você não devia ter colocado tanto protetor..."

    w "T-tem razão..."

    w "É... a-acho que eu vou levantar... Minha perna tá meio mole..."

    mc "Não tem pressa... você é levinha..."

    w "O-obrigada..."

    "Eu tô sentindo o corpo inteiro da [w]... inclusive lá em baixo... tá apertando..."

    "N-não sei se eu vou aguentar sem que o amigão acorde..."

    "O que você tá pensando, [mc]?! Foi um acidente! M-mas ele não entende! Tem uma mulher quase nua em cima de mim!"

    "Não aguento mais! Ele tá crescendo!"

    "Ela vai sentir! Por favor, não não não! Aaaahhh!"

    w "Hm?!"

    w "[mc]?!"

    mc "Q-q-que que foi?"

    scene soex1_imagem26 with vpunch

    pause

    w "Q-que que foi?!Que que tá acontecendo aqui em baixo, seu tarado?!"

    mc "Não é culpa minha! Ele não entende!"

    w "Eu caí em cima de você! Eu podia ter morrido! E você pensando besteira!"

    mc "Eu não pensei nada! É automático!"

    w "Bem conveniente pra você, tarado!"

    mc "É... v-você ainda tá em cim-"

    w "Ah!!!"

    w "Safado!"

    scene black with hpunch

    "{i}plaft{/i}"

    mc angustiado "ARGH!"

    w "D-desculpa! Doeu muito?!"

    mc envergonhado "Você é magrinha... mas que tapão..."

    "..."

    scene soex1_imagem27 with Dissolve(1.0)

    pause

    w "Acho que eu exagerei um pouquinho..."

    mc zerado "Um pouco? Minha bochecha tá latejando... Eu disse que foi sem querer..."

    w "Acho que eu fiquei um pouco nervosa com a situação... não imaginei que ia sentir seu..."

    mc envergonhado "Não precisa falar. Eu entendi..."

    w "Mas acho que deu tudo certo... tá bom por hoje."

    mc "E a campanha? Vai fazer?"

    w "Ainda não sei... mas eu dei um bom passo hoje. Foi diferente de tudo o que eu tinha pensado."

    mc normal "Eu gostei. Obrigado por aceitar o passeio."

    w "Eu que agradeço, [mc]. Você é a única pessoa que eu consigo me sentir à vontade pra fazer uma coisa assim."

    w "Talvez... a gente podia vir aqui de novo um dia... mas só como um passeio de dois... duas... é..."

    mc charmoso "Eu entendi. Que bom que você gostou. Vamos pegar o resto das suas coisas e voltar."

    w "Tá."

    scene black with dissolve

    "Essa [w] é uma peça."

    "..."

    $ tempo = 2

    jump call_cidade



label praia_especial_natasha_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("naex1_save", extra_info="naex1_save")

    $ estou_na_cidade = False

    $ praia_natasha_local = True

    "Certo. Então eu vou fazer isso mesmo."

    "A [na] é uma mulher super reservada. Ela é bem séria e direta também. Eu não posso ficar enrolando com ela."

    "Eu tenho que ser sincero e apostar que ela vai aceitar. Querer enganar ela, enrolar, aposto que ela vai sacar na hora."

    "Eu vou pra casa e vou ligar pra ela. Aproveitar que eu peguei o cartão dela aquele dia na prefeitura."

    scene black with dissolve

    "..."

    scene ape_celular_falando with Dissolve(1.0)

    pause

    mc "Oi. É a [na]?"

    na "[mc]?"

    mc "É. Sou eu. Como você sabe?"

    na "Eu... reconheci a sua voz."

    mc "Caraca. Seu ouvido é bom mesmo, hein?"

    na "Sua voz que é marcante. Não é fácil pra uma mulher esquecer."

    mc "Ei ei... falando assim fica muito fácil de você me levar pra cama."

    na "Você tá fácil desse jeito, [mc]?"

    menu:
        "Vai ser preciso mais que isso.":


            mc "Haha... não tão fácil assim. Vai ser preciso mais que umas palavras pra eu entregar minha flor pra você."

            na "Não esperava menos de você."
        "Pra você eu tô fácil.":


            mc "Pra você depende do que você quiser. Se você quiser eu fácil, eu tô."

            na "Fácil é rápido, mas nem sempre é o mais gostoso. Eu prefiro jogar um pouco mais com você."

    mc "Olha... depois daquela nossa conversa na prefeitura, eu vi que você tava muito cansada com tudo o que tá acontecendo."

    na "Eu estou, mas não precisa se preocupar comigo. Não era essa minha intenção."

    mc "Eu sei. Mas eu queria oferecer uma oportunidade de ouro pra você."

    na "Vai me chamar pra uma bebida no Distrito?"

    mc "Não é uma ideia ruim, não, mas eu pensei em outra coisa. Uma coisa mais... sei lá, clara."

    na "Coisa mais clara? O que isso quer dizer?"

    "Por que eu tô me enrolando pra falar uma coisa tão simples?"

    mc "A gente já teve muito encontro durante a noite. No Distrito, no Cassino. Eu tava pensando em variar um pouco."

    na "Eu não costumo beber de manhã... se é isso que você tá pensando."

    menu:
        "Não é isso.":


            mc "Não. Não é bem isso. Uma coisa totalmente diferente."

            na "Certo. O que é então?"
        "Você só pensa em beber?":


            mc "Haha! Não! Você só pensa em beber, é?"

            na "Encontro entre adultos sem álcool? A gente tá tentando abaixar a classificação indicativa?"

            mc "[na]..."

    mc "O que eu tava pensando mesmo era em mudar o estilo completamente. Chamar você pra curtir a praia."

    na "Praia? Você tá falando sério?"

    "Ixi..."

    mc "É. Uma manhã, só nós dois, conversando, tomando um sol."

    na "[mc]... eu não sei se eu tenho interesse em sair desse jeito."

    mc "Vai ser divertido. Eu prometo."

    na "Sua companhia não é ruim, mas praia? Praia é coisa de crianças e adolescentes. Tomar sol? Pra quê?"

    mc "Você tá esquecendo que praia não é só sol e brincar na areia. A gente pode ter um encontor mais adulto na praia."

    na "Agora você só tá tentando me convencer."

    mc "É sério! Se você me der uma chance, eu prometo que você vai sentir algo que você nunca sentiu em outros lugares."

    na "Uma chance... aliás, quem disse que eu nunca fui na praia?"

    mc "Nunca foi comigo. É uma experiência totalmente diferente."

    na "Olha, você tem confiança, isso eu tenho que admitir. Mas eu nem tenho roupa pra usar na praia."

    mc "Não esquenta. Eu vou deixar um biquíni pra você embalado na prefeitura hoje mesmo. Você pode usar ele."

    na "Você realmente quer isso..."

    mc "Combinado? Amanhã cedo aqui na praia da ilha?"

    na "Certeza que você não prefere beber comigo no Cassino?"

    mc "Certeza. Estamos combinados, então? Você pega o pacote que eu deixar. Amanhã vem pra praia e eu aposto que você vai curtir muito."

    na "..."

    na "Tá. Tudo bem. Eu topo."

    mc "Boa! Você vai ver que massa que é!"

    na "Ainda não acredito que eu aceitei isso. Mas agora eu estou ansiosa. Nos vemos amanhã."

    mc "Fechou. Até amanhã, [na]."

    scene ape_celular with Dissolve(1.0)

    mc "Ufa! Achei que ela não ia aceitar!"

    "Agora eu tenho que cuidar do resto. Comprar o biquíni, deixar pra ela e encontrar ela amanhã."

    "Vai ser foda. Bora bora!"

    scene black with dissolve

    "..."

    scene atendente_explicando with Dissolve(1.0)

    pause

    ate "Então. Temos um biquíni perfeito pra você que quer presentear uma garota especial."

    mc envergonhado "Ela é uma garota séria. Talvez um maiô que cubra mais ela se sinta mais à vontade."

    ate "E qual seria a graça, senhor? Nós temos que garantir que ela se sinta a garota mais gostosa do mundo."

    mc "Não sei..."

    ate "Vai ser melhor para o senhor também, obviamente."

    menu:
        "Ok. Manda brasa nesse biquíni!":


            mc safado "Ok... A vida é curta. A gente tem que aproveitar."

            ate "E você vai aproveitar muito poder ver ela usando isso aqui."
        "Não tenho certeza...":


            mc envergonhado "Não sei... tenho medo que ela não se sinta a vontade."

            ate "E se eu disser que eu faço um desconto especial pra você nele?"

            mc surpreso "Desconto?! Aí é bom!"

    ate "Vou pegar para o senhor. Pode me esperar no caixa."

    scene black with dissolve

    scene atendente_caixa with Dissolve(1.0)

    pause

    mc envergonhado "Ele não é assim... tão pequeno, né?"

    ate "Você tá perguntando se existe um biquíni maior do que esse na história?"

    mc zerado "Não foi isso que eu perguntei."

    ate "Eu diria que é possível, sim, que existam maiores..."

    mc "Você tá me zoando, né? Que ele é tão pequ-"

    ate "O pagamento foi aprovado. Obrigada pela sua compra!"

    mc "..."

    scene black with dissolve

    "Espero que a [na] não desista..."

    $ tempo = 2

    scene cidade centro9 with Dissolve(1.0)

    pause

    "Certo. Agora é deixar aqui pra ela. Não vou deixar remetente nem nada. Só vou entrar pro policial lá."

    scene black with dissolve

    "Tudo pronto."

    "..."

    $ tempo = 3

    scene ape_cama with Dissolve(1.0)

    mc "Mano... imagina se tudo der certo e eu ver a [na] nesse biquíni..."

    "Será que é tão pequeno igual a vendedora fez parecer? Ela deve tá exagerando..."

    "Amanhã a gente vai ver... se ela aparecer mesmo. Se ela me der o bolo a culpa é toda daquela vendedora..."

    scene black with dissolve

    $ dia += 1
    $ tempo = 1

    "..."

    scene ape_geral with Dissolve(1.0)

    mc "Amanheceu! Tenho que correr pra lá!"

    "Nenhuma mensagem da [na]... não sei se isso é bom ou não."

    "Vou pra lá e esperar ela aparecer. Chegar antes de uma dama é o mínimo. O mundo pode ter mudado, mas os bons modos continuam os mesmos."

    scene black with dissolve

    scene ilha praia_quiosque with Dissolve(1.0)

    pause

    mc normal "Legal. Agora é só torcer pra ela aparecer."

    show black with dissolve

    "..."

    hide black with dissolve

    "Hmm... já faz um tempo que eu tô aqui."

    mc preocupado "Será que se eu tivesse falado outras coisas na nossa conversa no telefone ela teria vindo?"

    mc concentrando "Não adianta chorar agora. Deixa eu voltar pra casa."

    scene ilha praia with Dissolve(1.0)

    pause

    "???" "Andando sozinho aí?"

    mc surpreso "!"

    scene na_p1 with Dissolve(1.0)

    pause

    na "Você tava indo embora?"

    menu:
        "Claro que não.":


            mc charmoso "Nada. Só tava andando enquanto te esperava."

            na "Que bom. Achei que tivesse demorado muito."

            "E demorou, mas, né? Tenho que mostrar confiança."
        "Pensei que tinha tomado bolo.":


            mc envergonhado "Já tava achando que tinha levado bolo."

            na "Desculpa a demora."

            mc "Tá tudo legal."

    na "Em parte a culpa foi sua."

    mc desconfiado "Hm?"

    na "Olha pra esse biquíni que você me deu. Quase eu deixei de vir por causa dele."

    na "Uma pessoa diz que não está acostumada com algo e você ajuda oferecendo o menor biquíni que existe?"

    menu:
        "Foi a moça da loja...":


            mc envergonhado "Desculpa. Foi a moça da loja que recomendou. Eu nem tinha visto o tamanho."

            na "Imagino sua expressão enquanto explicava pra ela pra ela te sugerir uma roupa de banho assim."

            mc "Haha..."
        "Ficou muito bom em você.":


            mc charmoso "Desculpa, mas, pra mim, ele ficou perfeito em você."

            na "Agora que eu vim pode falar assim. Mas se eu tivesse desistido, a história seria outra."

            mc "A gente precisa apostar às vezes, né?"

    na "Se eu não tivesse encontrado uma tanga pra cobrir a parte de baixo, eu desistiria."

    na "Mas eu não quero ficar dando bronca em você. É só para você ficar esperto para uma próxima vez."

    mc charmoso "Então vamos ter uma próxima?"

    scene na_p2 with Dissolve(1.0)

    pause

    na "Vai depender de hoje. Se você realmente me provar que não foi um erro eu ter aceitado seu convite."

    window hide

    pause

    "Meu Deus... a [na] tá incrível. Esse biquíni não cobre quase nada."

    "[mc]... força... você não pode ficar secando ela assim. Você precisa tirar o olho dos peitos dela ou ela vai perceber!"

    mc charmoso "E-eu aposto que você vai adorar. Conversa boa, boa companhia, o mar, o sol, que não tá forte agora."

    na "Isso eu tenho que te agradecer. Eu sofro muito no sol. Mas neste horário ele parece bem fraco."

    mc "Quer que eu passe protetor em você?"

    na "Não se preocupe. Eu passei antes de vir. E não acho que vou ficar tempo suficiente pra precisar reaplicar."

    "Ouch... às vezes eu esqueço como essa mulher é direta."

    mc normal "Eu sei que você acabou de chegar, mas qual tá sendo sua impressão até agora?"

    na "Eu nunca tinha vindo nesta parte da ilha. Eu nem sabia que a praia pertencia ao Barão pra falar a verdade."

    mc desconfiado "Ela é dele? Hmm..."

    na "Me disseram que antigamente ele fechava ela durante a noite, pra garantir que as pessoas fossem pro Cassino."

    na "Mas não sei se é verdade ou só lenda mesmo."

    mc zerado "Como que uma pessoa pode comprar uma praia e abrir e fechar ela quando bem entender?"

    na "Essa ilha é como um conto de fadas, [mc]. Acontecem coisas aqui que pessoas de fora nunca vão entender."

    menu:
        "Tem muita coisa errada aqui.":


            mc desculpa "A verdade é que tem muita coisa errada aqui. Quanto mais eu cavuco, mais defunto eu acho enterrado nesse lugar."

            scene na_p3 with Dissolve(1.0)

            pause

            na "Mesmo sendo tranquilo, você também chegou a essa conclusão."

            mc "Depois de ver certas coisas, é impossível não perceber isso."

            na "Seu senso jornalístico vai te ajudar muito aqui."
        "Eu tô curtindo muito a vida aqui.":


            mc normal "Sim. Realmente é um negócio de outro mundo. Mas eu tô curtindo muito esse lugar, sabia?"

            mc charmoso "Onde mais eu encontraria uma garota linda igual você pra trazer pra uma praia dessas?"

            na "Eu sei que você é um homem desse tipo... você tem um olhar bem particular das coisas."

            mc envergonhado "Acho que eu gosto de ver o lado bom, só isso."

            na "Eu acho que é mais do que isso. É um dom na minha opinião."

            na "Mas você não pode fechar seus olhos pra verdade."

            scene na_p3 with Dissolve(1.0)

            pause

            mc "Como assim?"

    na "Esta cidade tá cheia de conchavos criminosos, relações criadas por debaixo dos panos."

    na "É desse ambiente longe dos olhos das pessoas que a maioria das coisas acontecem aqui na capital."

    mc "Deu pra perceber..."

    "Será que a [na] tá ligada que o chefe dela é um dos grandes responsáveis por tudo isso?"

    na "Que foi?"

    mc "Nada..."

    na "Pode falar."

    "Eu não trouxe ela aqui pra ficar falando dessas coisas. Será que eu realmente falo sobre isso? E o clima? Como fica?"

    menu:
        "Não é nada...":


            mc "Não quero ficar falando sobre esses assuntos pesados. Eu prometi que você ia curtir a praia."

            na "Não vejo problemas e falar sobre isso. Acho um assunto instigante até."

            mc "Sério?"

            na "Eu sei que é mais fácil ignorar os problemas e só se voltar pro que é satisfatório, mas essa não é a realidade de um adulto."

            mc "T-tem razão."

            na "Nós precisamos abrir nossos olhos pra realidade e encarar os problemas de frente."

            mc "Concordo plenamente."

            "Melhor eu ficar calado que minha interpratação tá horrível."
        "O prefeito é um dos culpados...":


            mc "Sem querer causar com você e tal, mas o prefeito é um dos culpados pela cidade ser assim."

            na "Culpado como?"

            mc "Ele tá envolvido nesse grupo que dá as cartas na cidade por debaixo do pano igual você falou."

            na "Eu acho que isso é algo que precisa ser provado. Por enquanto, nada definitivo apareceu."

            mc "Nada definitivo... mas as conversas são outras... parecem bem convincentes."

            na "Existe muito falatório pela cidade, mas nada que realmente prove alguma coisa."

    na "Mas eu sei que você já viu por aí. Existem muitas coisas espalhadas pela cidade."

    na "Não é só aqui na ilha onde você vive ou no centro da cidade. Existem pessoas fora da lei nos quatro cantos."

    mc "Foi por isso que você foi no Distrito aquele dia?"

    na "Eu não posso falar de tudo o que eu tenho que fazer... perdão..."

    mc "Tudo bem. Não quero invadir suas coisas também. É que eu lembrei disso depois do que você falou."

    na "O Distrito com certeza tem seu pedaço no bolo de problemas que acontecem aqui."

    na "A prefeitura precisa saber o que acontece nos bairros. É isso que uma administração séria faz. Ela não ignora a cidade."

    scene na_p4 with Dissolve(1.0)

    pause

    na "O que você acha dos políticos, [mc]? Você confia neles? Acha que eles são necessários?"

    "Agora a gente tá falando de política? Conversar com a [na] nunca é fácil. O que eu respondo?"

    menu:
        "Políticos são ladrões.":


            mc "Pra mim, políticos são ladrões. A maioria não faz porra nenhuma e ganham um monte de coisa, tirando o que eles pegam por fora."

            na "Você realmente acha isso? Não é só o que você escutou por aí?"

            mc "Sei lá... eu nunca precisei deles pra nada. Eu sinto que tudo o que eles fazem é pegar nosso dinheiro com impostos."

            na "Eu não esperava essa resposta de você, mas faz sentido."
        "Eles são necessários pra democracia.":


            mc "Se o modelo que a sociedade segue é a democracia, então representantes eleitos pelo povo são necessários."

            mc "Sem comando, seríamos uma anarquia. Por isso que pessoas que representam multidões são necessárias pra sociedade."

            na "Essa é a resposta mais óbvia que eu consigo pensar. Mas, sem dúvida, é a necessária."

            na "Reclamar das coisas sem entender o porquê algo existe é extremamente infantil. É como reclamar de remédio porque tem gosto ruim."

            mc "A maioria das pessoas é assim..."
        "Eu não penso nisso.":


            mc "Pra falar a verdade, eu nem penso nisso, sabe? É um assunto que não me atrai e não quero perder tempo com isso."

            na "Parece uma coisa distante. Acho que a maioria pensa como você."

            mc "Você tá certa. Não parece que é uma coisa que eu posso fazer diferença. No máximo um voto."

            na "Essa reação é comum. Ainda mais com relação a política."

    na "É normal isso. As pessoas perderam a fé no poder político porque elas sentem que não são representadas."

    na "É duro ter confiança em alguém, quando tudo em volta parece tão fora de controle."

    mc "Além de que a gente tem péssimos exemplos em todo lugar. Por que alguém iria acreditar neles?"

    na "Faz sentido. Mas quantas pessoas realmente sabem como essa engrenagem gira?"

    na "Quem tem experiência interna de tudo isso? Matérias de jornais? Isso não é informação de verdade, com todo o respeito."

    mc "Haha... ok..."

    na "Entender como a roda gira é o primeiro passo pra quem quer falar sobre algo. Quer falar, então saiba como funciona primeiro."

    mc "Parece ser um assunto complicado pra você..."

    na "Você acha?"

    mc "Você não costuma falar assim."

    na "Hmm..."

    mc "Tudo bem. Pode falar pra mim o que te incomoda."

    na "Eu não me sinto bem me expondo desse jeito. Parece que eu faço isso mais vezes quando estou falando com você."

    mc "Relaxa. Eu não vou te achar pior porque você trabalha com um político. Você não é seu trabalho."

    na "Eu não sou meu trabalho..."

    mc "Não. Você é a [na]. Você é a assistente do [pr], mas também é uma loiraça, é uma mulher inteligente, séria, bacana."

    na "Acho que... você tem razão..."

    mc "Acha? É difícil escutar você falando isso. Normalmente você é bem certa das coisas."

    na "?"

    scene na_p5 with Dissolve(1.0)

    pause

    na "Ai, [mc]... às vezes você fala umas coisas que eu nem acredito."

    mc envergonhado "..."

    na "Só você pra reparar uma coisa dessas. E falar umas coisas dessas também..."

    menu:
        "Se eu fiz você rir, tá valendo.":


            mc charmoso "Se você tá se sentindo melhor agora, então eu acertei."

            na "Às vezes eu sinto que eu tô na sua mão... é uma coisa muito estranha."

            mc "Estranho... mas é ruim?"

            na "Não necessariamente..."

            "Caralho. Eu tô indo muito bem com ela. Eu não posso deixar a bola cair agora."
        "Não sei do que você tá falando.":


            mc envergonhado "Não sei do que você tá falando..."

            na "Você faz tudo isso naturalmente... é incrível."

            mc normal "Eu só quero que você fique à vontade, só isso."

            na "Você está indo bem então."

    na "Sabe... eu tinha certeza que não ia vir na praia com você."

    na "Mas agora que eu tô aqui, com esse biquíni que não esconde quase nada... é um pouco libertador..."

    na "Eu não lembro a última vez que eu me senti leve desse jeito."

    "Se ela tá se sentindo à vontade comigo nesse biquíni, alguma coisa muito certa eu tô fazendo."

    mc charmoso "A gente tá só começando. Eu quero fazer uma coisa especial com você agora."

    na "Aproveita que eu estou de bom humor. Só não exagera."

    mc "Vem comigo que eu vou te mostrar."

    na "Eu tô achando que eu vou me arrepender..."

    mc "Vem logo."

    scene black with dissolve

    mc charmoso "Aqui."

    scene na_p6 with Dissolve(1.0)

    pause

    na "..."

    mc "A gente vai surfar."

    na "..."

    mc "Que foi. Você não parece empolgada."

    na "A chance de eu fazer isso é mais perto de zero do que... o resto."

    mc "Hoje é um dia de tentar coisas novas."

    na "Vir na praia com você foi novo o suficiente, eu garanto."

    mc "Se te deixa mais calma, eu também não sei surfar. A gente vai fazer um lance básico."

    na "De jeito nenhum."

    menu:
        "Bora, [na]! Viver a vida!":


            mc "Bora lá, mulher! A vida é só uma!"

            na "Eu já disse não. E é bom você parar de tentar antes que o clima acabe."

            mc "Opa. Ok."
        "Se você não quer, tudo bem.":


            mc "Se você não tá afim, tudo bem."

            na "Um passo por vez."

            mc "Você tem razão. Vamos devagar."

    mc "Poxa..."

    na "Você queria tanto assim que eu fosse surfar contigo?"

    mc "Eu queria fazer uma coisa de diferente pra você. Pra você sair daqui achando que foi algo incrível, sabe?"

    na "Heh... Às vezes você parece uma criança."

    mc "Ei..."

    na "Ver você tão empenhado em querer fazer meu dia melhor é uma prova de que você se importa."

    na "Qualquer uma acharia esse gesto digno de apreciação."

    mc "É... Não sei se eu entendi o que você quis dizer."

    na "O que eu quis dizer é..."

    scene na_p7 with Dissolve(1.0)

    pause

    mc surpreso "!"

    na "Quero dizer que você merece uma recompensa por ter tentado me impressionar."

    mc envergonhado "..."

    na "Como você acha que eu ficaria na prancha?"

    mc charmoso "Vocês foram feitas uma pra outra."

    na "Sério? Mesmo eu não querendo levar ela pra água?"

    mc "Pensando bem... acho que ficou melhor assim, sabe?"

    na "Você mudou de ideia?"

    mc safado "Mudei... aqui a gente pode ver melhor como você e a prancha foram feitas uma pra outra."

    na "Então a gente fica perfeitas juntas?"

    mc "Com certeza. Só tem um pequeno problema..."

    na "Qual?"

    mc "Essa sua tanga não tá combinando perfeitamente. Eu acho que ficaria melhor sem ela."

    na "Você tem certeza? Você não só querendo me ver sem ela, né? Porque esse biquíni é realmente bem pequenininho..."

    "M-meu Deus... a [na] tá mesmo me provocando?"

    "Eu não posso errar nos próximos passos. "

    na "Então? Você tá sendo sincero comigo?"

    menu:
        "Eu quero ver você melhor...":


            mc envergonhado "Eu não queria dar na cara, né? Mas claro que eu quero... ver você, né?"

            na "Se é assim..."

            scene na_p8 with Dissolve(1.0)

            pause

            mc safado "Uou..."

            na "Era isso que você queria?"

            mc "Exatamente..."

            na "Você pode só pedir, [mc]. Eu vim aqui hoje por você. Eu vesti isso por você. Eu quero que você veja seu presente em mim."

            na "Valeu a pena comprar esse presente pra mim?"

            mc charmoso "Com certeza. Não tinha como eu imaginar você mais linda do que isso. Você é perfeita, [na]."

            na "Obrigada. Essa é sua recompensa por ser sincero comigo."

            na "Se tem uma coisa que eu não suporto é mentira. De você, eu só quero ouvir o que você realmente pensa."

            mc charmoso "Pode contar com isso."

            na "Se você mentir... quer saber? Deixa pra lá."

            mc desconfiado "..."

            mc "Aconteceu alguma coisa?"

            na "Acho que eu vou sentar aqui, tá?"

            mc preocupado "Claro."
        "Eu tô sendo sincero. Vai combinar mais.":


            mc tarado "Eu tô falando sério. Vai combinar mais com você."

            na "Você acha que eu sou boba, [mc]?"

            mc "Claro que não."

            na "Você não tem coragem de falar a verdade? Por que precisa mentir sobre uma coisa assim?"

            mc preocupado "E-era só uma brincadeira, [na]."

            na "Eu não gosto que mintam pra mim dessa forma. Ainda mais com essa cara."

            mc desculpa "Não é isso... eu... foi mal."

            na "..."

            na "Eu tô super reagindo, né?"

            mc desculpa "Um pouco. Mas foi culpa minha também."

            na "Não foi. Deixa eu tirar isso aqui. Senta comigo?"

            mc surpreso "C-claro."

    scene na_p9 with Dissolve(1.0)

    pause

    mc "Que foi?"

    na "Não é nada. Eu só lembrei de uma coisa."

    mc "Pode falar pra mim. É bom colocar as coisas pra fora às vezes."

    na "Não é da sua conta. É uma coisa pessoal."

    mc "Ah, tudo bem."

    na "Não. Perdão. Não queria ser grosseira."

    na "Depois de tanto tempo, eu acabei acostumando a lidar com meus problemas sozinha."

    na "Quando alguém pergunta sobre minha vida, eu fico em uma espécie de defensiva. Eu realmente não estou acostumada."

    mc "Você não tem amigos ou parentes? É duro viver sozinho."

    na "Com você não é a mesma coisa?"

    mc "Bom... eu moro sozinho, mas eu não me sinto sozinho. Eu tenho vários conhecidos aqui na ilha."

    na "E são pessoas que você realmente confia?"

    mc "Acho que sim... nunca pensei tanto nisso."

    na "Entendo..."

    mc "Assim... se você tiver precisando de alguém pra conversar, pode sempre falar comigo."

    na "Estranhamente, eu sei disso."

    mc "Haha..."

    "Se a gente continuar nesse clima, não vai sair nada daqui. Eu quero um lance quente com ela, então eu tenho que tomar a iniciativa."

    mc "Eu tava pensando... é..."

    scene na_p10 with Dissolve(1.0)

    pause

    na "Hah..."

    mc "Que foi?"

    na "Você tá tentando pensar no que falar pra não me deixar assim, né?"

    mc "Quê?! Como você sabe?"

    na "Eu consigo ler sua expressão. Você é mais fácil de entender do que você pensa."

    mc "Eu acho que isso é mais você do que eu. Você é esperta, [na]... esperta demais, até."

    na "Esperta demais? Você tá exagerando."

    menu:
        "Certeza que você não é treinada?":


            mc "Certeza que você não é uma espiã treinada, não? Esse negócio de ler expressões, seu jeito... sei lá..."

            na "De novo essa história? Eu já falei que isso é da sua cabeça."

            na "Eu sou só uma secretária que tem alguma habilidade em ler expressões corporais."
        "Você sempre parece um passo à frente.":


            mc "Parece que você tá sempre um passo na frente. Tipo, como se fosse um jogo de xadrez e você tá pensando o próximo movimento."

            na "Isso seria mesmo possível? Digo, levando em consideração que as pessoas são tão impresíveis."

            mc "Hmm... você tá querendo me despistar?"

            na "Eu? Você que tá pensando demais sobre isso."

    mc "Sei..."

    "Parece que não importa o que eu falo, a conversa sempre dá uma volta e a gente tá de novo no zero a zero."

    "O único momento que realmente pintou alguma coisa foi naquela hora da prancha."

    "Acho que não tem jeito... eu não consigo despertar desejo nela."

    na "Posso falar uma coisa?"

    mc "Ahn? Claro."

    na "O problema, [mc], é que você pensa demais nas coisas. Você planeja demais."

    scene na_p11 with Dissolve(1.0)

    pause

    na "Foi você mesmo que me disse que às vezes a gente só precisa seguir as coisas e deixar elas acontecerem."

    mc "Eu que te chamei aqui. Eu queria que fosse incrível pra você. Queria que você ficasse impressionada comigo."

    na "E esse dia tem sido incrível. Mas o mais incrível é quando coisas inesperadas acontecem."

    mc "Tipo quando eu te chamei pra surfar? Uma coisa muito nada a ver?"

    na "Haha... exatamente. Chamar uma mulher igual eu pra surfar não é o melhor caminho, mas nem sempre o melhor caminho é o mais indicado."

    na "Você é especial porque você tem seu jeito de ser. Seu jeito diferente cativa as pessoas."

    na "Eu disse que eu fico lisonjeada por você se esforçar pra me agradar. Isso mostra o quanto é um cavalheiro."

    na "Mas querer controlar todos os atos pra chegar onde você quer. Nem sempre isso vai funcionar."

    "Ela tem razão. Não adianta que eu não vou manipular ela pra pegar ela. Que se foda."

    "Será que é melhor eu arriscar alguma cartada máxima ou só ir pelo seguro?"

    menu:
        "Quero te fazer uma massagem especial.":


            mc "Você tem razão. Chega de falar. Eu vou garantir que você tenha um dia diferenciado com a minha massagem especial."

            scene na_p12 with Dissolve(1.0)

            pause

            na "Massagem... não sei se a gente já chegou nesse estágio de intimidade, [mc]."

            if mc_massagem >= 9:

                mc "Eu sou um mestre na arte da massagem. Eu completei um curso sério com uma garota que é profissional."

                na "Por essa eu não esperava. Você realmente fez um curso. Impressionante."

            elif mc_massagem > 2:

                mc "Eu tô no meio do curso de massagem profissional. Tô faznedo aulas e tudo."

                na "Por essa eu não esperava. Você está fazendo um curso mesmo."
            else:


                mc "Eu não sou profissional, né? Mas eu aposto que posso fazer você se sentir muito bem."

                na "Hmm... não sei, [mc]..."

            mc "Você vai ver como minhas mãos são incríveis."

            mc "Você só precisa deitar nessa prancha aí e eu cuido do resto. Pelo menos não vai precisar se equilibrar nela."

            na "Um pouco da culpa é minha por falar pra gente improvisar."

            mc "Exatamente. Totalmente sua. O mínimo é você aceitar."

            na "Hmm..."

            na "Tudo bem."

            mc surpreso "S-sério?!"

            na "Nem você acreditava nessa."

            mc envergonhado "C-claro que eu acreditava. Você vai adorar. Pode se ajeitar aqui."

            scene black with dissolve

            scene na_p13 with Dissolve(1.0)

            pause

            na "Eu não espero que menos que o excelente de você."

            mc "P-pode deixar."

            "[mc]! Agora não é hora de ficar nervoso! Massagem é tudo sobre confiança e movimentos precisos!"

            if mc_massagem > 1:

                "Não vai esquecer do que a Karli te ensinou."

            "Certeza que essa massagem pode evoluir pra alguma coisa a mais se eu caprichar."

            if natasha_e4 == "seducao" or na1_beijo or na3_beijo:

                "Eu e a [na] já ficamos antes. Se rolou daquela vez, pode rolar de novo."

                "Eu só preciso caprichar na massagem."

            mc "Ok. Vou começar."

            na "Bom trabalho."

            scene na_p14 with Dissolve(1.0)

            pause

            mc "Eu vou começar bem devagar. Vou identificar os pontos em que você que precisam de mais pressão."

            na "Você fala igual um profissional. Quero ver na prática."

            mc "Agora você precisa ficar em silêncio e focar nas sensações que você vai sentir."

            na "..."

            "Bora começar."

            window hide

            pause

            scene na_p15 with Dissolve(1.0)

            pause

            na "Hmmm..."

            "Parece que ela tá gostando. Eu preciso continuar assim."

            na "[mc]..."

            mc "O-oi."

            na "Só toma cuidado onde você vai colocar essa mão."

            mc "Não se preocupe, faz tudo parte do serviço profissional."

            na "..."

            "Melhor eu tomar cuidado. Provavelmente ela não vai falar de novo."

            "Mais um pouco aqui nas costas e vai chegar a hora..."

            window hide

            pause

            "Ok... Se eu realmente quero que isso aqui evolua pra algo mais, eu tenho que dar o próximo passo."

            mc "Muito bem. Agora eu preciso que você vire de barriga pra cima pra eu poder continuar."

            na "Tudo bem."

            scene na_p16 with Dissolve(1.0)

            pause

            na "Tenho que admitir, foi melhor do que eu imaginava."

            "Caralho... que mulher..."

            "Eu podia ficar o dia inteiro olhando pra ela desse jeito."

            na "[mc]... você vai perder a profissionalidade se continuar olhando pra sua paciente dessa forma."

            mc surpreso "Opa!"

            mc envergonhado "D-digo... eu vou começar a massagear suas pernas e vou subindo. Continue tranquila igual antes."

            na "Tudo bem. Eu vou seguir suas recomendações. Você é o profissional aqui."

            mc charmoso "Isso mesmo. Agora deixa eu começar."

            scene black with dissolve

            scene na_p17 with Dissolve(1.0)

            pause

            "Nem acredito que eu tô pegando na [na] desse jeito."

            "A pele dela é perfeita. Parece que veio de outro planeta. É macia, tem carne na medida certa..."

            "Se eu continuar pensando nessas coisas eu vou pular em cima dela. Tenho que segurar. Se eu fizer merda agora, nunca mais."

            na "Hm."

            "Parece que ela tá curtindo."

            "Tá chegando na hora de eu dar o bote. Eu já peguei nela quase inteira. Na coxa, no abdomen... falta só os pontos principais..."

            "Será que eu devo arriscar?"

            menu:
                "Pegar nas 'partes principais'":


                    "Se eu quero que alguma coisa aconteça, eu vou ter que arriscar. Se ela aceitar... ela vai tá literalmente na minha mão."

                    "Vou pegar aqui na virilha... bem de leve..."

                    "E vou subir a mão a-{nw}"

                    na "[mc]... o que você tá fazendo?"

                    mc "É parte da massagem. É a última etapa. Você vai gostar mais do que antes..."

                    if mc_massagem >= 5:

                        na "Olha... você mostrou que realmente sabe como massagear."

                        na "Se você está falando, eu acredito. Pode... fazer sua mágica."

                        "Perfeito! É hora de deixar ela doida!"

                        mc "Só relaxe e deixa que eu cuido do resto..."

                        scene black with dissolve

                        na "!"

                        scene na_p18 with Dissolve(1.0)

                        pause

                        na "Ai... ah!"

                        "Ela tá deixando eu pegar onde eu quero. Que beleza!"

                        "Tomara que ela aproveite tanto quanto eu tô aproveitando pra pegar nela heh..."

                        na "Ai!"

                        "Parece que ela tá."

                        "Eu não tenho porque parar a aqui também. Eu já tô pegando nela inteirinha..."

                        "Ela não vai negar uma pegação agora."

                        na "[mc]... sua massagem... t-tá boa demais... m-mas... meu biquíni..."

                        mc "Tudo bem... depois a gente ajeita ele."

                        na "P-para um segundo!"

                        scene na_p19 with Dissolve(1.0)

                        pause

                        mc "O que foi?"

                        na "Você tá extrapolando nessa massagem... eu tô quase sem roupa..."

                        mc "Que que tem? Você não tá gostando?"

                        na "Eu tô, mas... não sei se eu quero continuar isso."

                        mc "A gente só precisa deixar as coisas acontecerem. Não pensa demais. Você que falou isso."

                        na "Hmmm..."

                        if natasha_e4 == "seducao" or na1_beijo or na3_beijo:

                            na "Mesmo querendo, não consigo negar você."

                            mc "É a magia da massagem secreta especial."

                            na "Pode ser... mas acho que são seus olhos. Eles me... não sei explicar... eles me atraem..."

                            mc "Seja lá o que for... se eu puder beijar você é o que importa."

                            na "Só que eu tô quase nua..."

                            mc "Espera aí. Isso não é problema."

                            scene na_p20 with Dissolve(1.0)

                            pause

                            na "Você tá pelado?!"

                            mc "Completamente."

                            na "E se tiver alguém vindo?"

                            mc "Então é melhor a gente começar logo, certo?"

                            na "..."

                            na "Vem..."

                            window hide

                            pause

                            scene na_p22 with Dissolve(1.0)

                            pause

                            "Finalmente... finalmente eu tô sentindo direito o gosto dessa mulher."

                            "..."

                            "A [na] é toda na dela, mas ela beija bem pra caralho."

                            window hide

                            pause

                            scene na_p21 with Dissolve(1.0)

                            pause

                            "A mina não perde o fôlego por nada. Sei lá quanto tempo a gente tá se beijando."

                            mc "{i}puf{/i}"

                            na "Se a gente tivesse naquele motel agora..."

                            mc "Nem me fala uma coisa dessas."

                            na "Quem sabe na nossa próxima missão?"

                            mc "Mas a praia não é tão ruim assim... o que você acha?"

                            na "Você é gostoso, [mc]. Você beija bem. Mas não vai rolar aqui."

                            mc "É... Eu imaginei..."

                            na "Areia e sexo só combinam nos filmes."

                            mc "Haha... Deixa eu só curtir você mais um pouquinho então."

                            na "..."

                            window hide

                            pause

                            scene black with Dissolve(1.0)

                            "..."
                        else:


                            na "Eu sei, mas... eu..."

                            na "Não estou no clima. Desculpa."

                            mc "Você vai entrar no clima. Tenho certeza."

                            na "Você foi um cara incrível hoje, mas não vai acontecer mesmo."

                            mc "Sem chances?"

                            na "Pelo menos não agora."

                            mc "Ok..."

                            "Droga... o que será que não rolou?"

                            "Talvez a [na] não me veja desse jeito. A gente {b}nunca se beijou antes{/b}."

                            "Se eu tivesse ficado com ela em outras oportunidades, talvez agora ela tivesse mais segura disso."

                            mc "Foi uma boa tentativa..."

                            na "E foi uma excelente massagem. Fazia muito tempo que eu não me sentia assim."

                            mc "Não precisa levantar minha bola também."

                            na "Eu não faço isso. Vem aqui. Senta comigo."

                            scene black with dissolve

                            jump natasha_praia_amizade
                    else:


                        na "Eu não acho que isso seja muito profissional de sua parte..."

                        mc "Eu sei o que tô fazendo. Relaxa..."

                        na "Eu não acho que você saiba."

                        na "Hmm... Eu adorei o seu trabalho, mas vamos parar por aqui."

                        mc envergonhado "J-já está bom?"

                        na "Foi incrível."

                        mc "Que bom que você curtiu."

                        na "Fazia muito tempo que eu não me sentia relaxada desse jeito."

                        "Droga! Se eu {b}soubesse mais sobre massagem{/b}, certeza que ela aceitaria. Eu tenho que fazer mais aulas..."

                        na "Não faz essa cara. Vem aqui comigo agora."

                        mc desculpa "Opa."

                        scene black with dissolve

                        jump natasha_praia_amizade
                "Continuar como está":


                    "Melhor eu não exagerar."

                    "Vou continuar fazendo um bom trabalho..."

                    window hide

                    pause

                    na "Hmm... perfeito, [mc]. Eu adorei."

                    mc envergonhado "J-já está bom?"

                    na "Foi incrível."

                    mc "Que bom que você curtiu."

                    na "Fazia muito tempo que eu não me sentia relaxada desse jeito."

                    na "Vem aqui comigo agora."

                    mc normal "Opa."

                    scene black with dissolve

                    jump natasha_praia_amizade
        "Vamos só bater um papo.":


            "Acho que eu vou só bater um papo. A [na] é uma mulher cheia das ideias. Acho que é uma boa forma de aproveitar."

            mc "Acho que a gente podia trocar uma ideia então. Você ainda é um mistério pra mim."

            na "Mistério? Haha... Mas eu concordo."

            label natasha_praia_amizade:

                scene na_p11 with Dissolve(1.0)

                pause

                na "Passar um tempo com alguém que a gente acha interessante, é uma excelente forma de ter um dia interessante."

                na "Desde a primeira vez que a gente se viu no Cassino, você chamou minha atenção."

                mc envergonhado "Com a minha cara de pau?"

                na "Eu vejo como algo positivo. Por mais que você tenha me enfadado um pouco quando tentou falar comigo..."

                mc "Eu sabia..."

                na "Logo eu percebi que você era um homem de boas intenções. Seu papo era bom e desde o começo você se mostrou interessado em mim."

                mc normal "Isso é normal. Mostrar interesse nos outros."

                na "Não. Isso é cada vez mais raro. Eu noto as pessoas. Elas querem falar, falar, mostrar sua vida. Poucos realmente querem saber dos outros."

                na "Essa capacidade de ter interesse pelo outro é cada vez mais raro."

                mc desculpa "Se todo mundo só falasse e ninguém ouvisse, não adiantar nada falar também..."

                na "Exatamente. Mas não é assim nas redes sociais? Todo mundo postando de suas vidas o dia todo? Será que alguém realmente presta atenção?"

                mc "Com certeza dar um like ou fazer um comentário genérico não é garantia que alguém realmente prestou atenção."

                na "É o que eu penso também."

                na "Por isso que o fato de você ter se dedicado tanto pra que eu tivesse um bom dia aqui, é algo que eu vou guardar com muito carinho."

                mc envergonhado "Não foi nada."

                na "Mesmo as coisas não acontecendo exatamente como planejávamos, não quer dizer necessariamente que foi ruim."

                mc "Acho que você tem razão."

                na "Bom... vou levantar."

                mc "Eu te ajudo."

                scene black with dissolve

                "..."

    scene na_p23 with Dissolve(1.0)

    pause

    na "Sem dúvida a vinda na praia foi melhor do que eu tinha imaginado quando eu concordei."

    mc charmoso "Eu disse que seria inesquecível."

    na "Vou ficar ansiosa esperando pelo seu próximo convite."

    mc "A gente se vê logo. E toma cuidado com todo mundo lá na prefeitura."

    na "O Donatello, mesmo com as coisas dele, é um bom homem. Ele vai levar nossa cidade longe."

    mc envergonhado "Vamos ver..."

    na "Obrigada por se preocupar comigo, mas eu vou ficar bem."

    mc "Pensando aqui, eu com certeza me daria pior do que você. Você parece ter mais a cabeça no lugar."

    na "Não duvide de você também, [mc]. Você fica muito mais sexy quando tá confiante."

    mc surpreso "E-eu vou lembrar disso!"

    na "Você me acompanha até o centro?"

    mc charmoso "Com certeza. Vem."

    scene black with dissolve

    "..."

    "Sem dúvida a [na] é uma mulher especial. Como que uma garota dessas tem vontade de passar tempo comigo?"

    "Acho que ela tem razão. Eu tenho que ser mais confiante. Talvez, eu seja um cara bacana até."



    $ tempo = 3

    jump call_cidade



label praia_especial_nona_evento:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("hex1_save", extra_info="hex1_save")

    $ estou_na_cidade = False

    $ praia_nona_local = True

    $ nona_praia_beijo = False
    $ nona_pp = 0

    "Isso, [mc]! Coragem! A [h] é uma hacker internacional, que derruba governos e mega empresas m-mas... ela é um ser humano normal igual você."

    "Quem eu tô enganando? Eu e a [h] tamo em níveis completamente diferentes. Eu só quero um emprego normal, ela é procurada em vários países."

    "Por que ela daria atenção pra mim?"

    "Mas, assim... se ela negar, negou, se eu nem tentar, é uma negação automática. Eu tenho que tentar."

    if nona_interesse and no2_especial:

        "E se ela não tivesse pelo menos uma quedinha por mim, ela não ia ter aceitado meu beijo no bar, certo?"

        "Certo certo certo... tenho certeza. Faz todo o sentido, sim sim."

    mc charmoso "Ok, vou mandar mensagem pra ela."

    "..."

    mc zerado "Eu não sei nada sobre ela."

    "Aquela vez ela me mandou uma mensagem no celular... mas não dá pra responder aquilo. Nem aparece o campo pra digitar. Coisa maluca."

    "Como eu falo com ela?"

    "Hmm... talvez o [gar]. Ela tá morando na casa dele agora. Ou pelo menos lá perto."

    "Vou dar um pulo lá."

    scene black with dissolve

    "..."

    scene hub_bar_fundo cenario with Dissolve(1.0)

    mc "[g]? Tá aí?"

    gar "Preparado para aprimorar o corpo e afiar a alma em ação construtiva, senhor [mc]?"

    mc zerado "Nem pense nisso. Eu não vim trabalhar."

    gar "Hmmm... qual motivo o senhor teria para aprumar-se em minha área física de atuação a esta hora?"

    mc envergonhado "Eu queria pedir um favor pra você."

    gar "Pois venha e discutiremos em detalhes suas aflições."

    scene nop_img1 with Dissolve(1.0)

    pause

    gar "Sou todo ouvidos. Lamurie."

    mc "Não precisa fazer todo esse escândalo por causa disso. Eu só queria te pedir uma coisinha."

    gar "Pois não."

    mc "A [h] tá ficando na sua casa, né?"

    gar "Sim, senhorita está dormindo com minha pessoa nos últimos dias."

    menu:
        "Então você pode dar um recado?":


            $ nona_pp += 1

            mc "Tem como você entregar um recado pra ela?"

            gar "Não seria impossível."

            mc "Seria difícil?"

            gar "A senhorita não gosta de ser incomodada, nem por mim, tanto por outrem."

            mc "Então não dá?"

            gar "Devo reconhecer que irá depender do conteúdo da sua mensagem."

            mc "Certo..."
        "Dormindo com ela? Em que sentido?":


            mc "D-dormindo com ela? Em que sentido você tá falando? Você não quer dizer..."

            gar "Ora, meu lorde, sua cabeça parece estar sempre voltada para os prazeres carnais."

            gar "Este fato o faz ver coisas inexistentes e tirar conclusões inverossímeis."

            mc "Então não tá rolando nada..."

            gar "O senhor carece de autoestima, senhor. Deve ser mais direto quando se é necessário."

            mc "Tá. Então tá..."

            gar "Não vejo a hora de dizer sobre isto a senhorita."

            mc "Não! Não fale!"

            gar "..."

            mc "Foda-se..."

    mc "O que eu queria era que você falasse pra ela é que eu queria convidar ela para um encontro na praia amanhã."

    mc "Eu vou tá esperando ela na praia de manhã. Lá pelas nove, dez horas. Se ela teria interesse de ir comigo."

    gar "Então o senhor planeja cortejá-la."

    menu:
        "Eu quero pegar ela logo.":


            $ nona_pp += 1

            mc "Eu não vejo a hora de pegar ela de jeito, [gar]. Eu acho a [h] incrível. Ela tá me deixando louco!"

            gar "Tenha calma, lorde [mc]. Guarde um pouco de sangue para as outras funções de seu corpo."

            mc "A gente tem que focar no que é mais importante."
        "Não é bem isso...":


            mc "N-não é bem isso! Eu só queria passar um tempo com ela e tudo o mais... conversar e talz..."

            gar "Seria somente isso mesmo?"

            mc "Você que tá pensando besteira. Eu sou inocente!"

    gar "Então devo transmitir vossa mensagem. Serei Hermes, o viajor grego a levar suas palavras até a senhorita."

    gar "Por favor, esteja alerta às necessidades desta moderna taverna."

    mc "Ok. Vou esperar aqui e fico dando uma olhada."

    gar "Logo voltarei."

    scene hub_bar_fundo cenario with Dissolve(1.0)

    "O melhor seria se eu mesmo falasse com ela, mas não sei se ia rolar. Eles tão cheio de segredos."

    "Tomara que ela pelo menos entenda o que o [gar] vai falar..."

    "É duro acreditar que esse cara fala desse jeito mesmo. Mais ninguém fala assim, mano. Por que usar aquelas palavras?"

    "E se ele veio de outro lugar? Ou é só louco mesmo..."

    gar "Senhor [mc]."

    mc surpreso "Opa."

    scene no3_img1 with Dissolve(1.0)

    mc "E aí?"

    gar "Senhorita não se disponibilizava a me ouvir... Sinto que ela tem algo contra as humildes palavras deste servo."

    "Eu sabia..."

    gar "Mas terminar a missão era imprescindível, portanto insisti até que a algoz cedeu e ouviu meu apelo."

    mc "Sério?! E aí?"

    gar "Ela aceita a proposta."

    mc "Não acredito!"

    gar "Mas ela demanda que dois pedidos sejam aceitos."

    mc "Hm? C-certo. O que ela quiser."

    gar "Em primeiro, você precisará prover roupa adequada ao evento, pois ela carece de tal artefato."

    mc "Então uma roupa de banho... tudo bem."

    gar "O segundo é que o encontro aconteça durante a noite, pois ela evita os raios solares. E tem que ser hoje."

    mc "Ir na praia a noite? Hoje?!"

    gar "É a única forma."

    mc "Se ela quer... ok..."

    mc "Valeu pela ajuda, [gar]. Eu vou lá então na loja de roupa que tem que tá tudo certo pra de noite."

    gar "Desejo-lhe sorte, lorde [mc]. Senhorita pode ser um tanto quanto fechada, um tanto quanto difícil."

    mc "Pois é..."

    gar "Pode ser de incrível inteligente, grande garra. Um nível acima do que você jamais sonhou."

    mc "Você tá me deixando mais nervoso."

    gar "Mas, em realidade, coração e cabeça não são o mesmo. Grande cabeça, pequeno coração. E é pelo coração que se conquista."

    mc "Mesmo me deixando nervoso, você tá dizendo que eu tenho uma chance? Valeu..."

    gar "Suas chances são infinitamente minúsculas, entretanto elas existem. Boa sorte."

    mc "... Falou."

    scene black with dissolve

    "Agora é ser roubado lá na boutique."

    call locomocao from _call_locomocao_18

    scene atendente_caixa with Dissolve(1.0)

    ate "Prontinho, senhor. Foi aprovado."

    mc preocupado "Que bom. Achei que não ia passar o cartão, não."

    ate "O senhor é um excelente cliente. Sempre escolhendo nossa loja e ajudando na minha comissão hehe..."

    menu:
        "Acho que eu mereço um desconto.":


            mc normal "Tá na hora de eu ganhar um desconto ou um cupom de fidelidade, hein?"

            ate "A gente não tem isso aqui. Desculpa. Mas você ia merecer."

            mc "Haha..."
        "E se você me agredecer tomando uma comigo?":


            mc charmoso "Um dos motivos que eu gosto de comprar aqui é que você que me atende."

            ate "Eu?"

            mc "E se você agradecesse saindo comigo? A gente podia tomar um sorvete comigo? Ou uma cerva."

            ate "Ai... isso é meio do nada, né? Não sei."

            mc "É do nada, mas o que você acha? Sem compromisso. Só pra gente conversar."

            ate "A gente vê, tudo bem? Não é um não, é só um depois."

            mc "Combinado."

    mc "Agora eu vou nessa. Obrigado."

    ate "Tenho certeza que ela vai gostar do presente. E você também."

    mc safado "..."

    scene black with dissolve

    "Agora é só voltar e dar pro [gar]."

    "..."

    $ tempo += 1

    scene hub_bar_fundo cenario with Dissolve(1.0)

    mc normal "Tá aqui. Pode entregar pra ela?"

    gar "Seu pedido é uma ordem, lorde [mc]. Desejo-lhe toda a sorte do mundo esta noite."

    mc envergonhado "Valeu. Eu vou precisar com essa aí..."

    mc normal "Falou."

    gar "Nos vemos em breve."

    scene black with dissolve

    "..."

    scene ape_geral with Dissolve(1.0)

    pause

    "Eu não tenho muito tempo até acabar o sol. Vou tomar um banho e vou correr pra lá. Eu tenho que chegar antes dela."

    "Tomara que dê tudo certo! Eu quero passar um tempo legal com ela."

    if nona_interesse:

        "E quem sabe tirar uma casquinha... a [h] é muito gata, pelo amor..."

    scene black with dissolve

    "..."

    scene ilha praia_quiosque with Dissolve(1.0)

    pause

    mc normal "Legal. Ainda tá de tarde. Ainda vai demorar uma horinha pro sol sumir completamente."

    "Vou dar uma andada."

    scene praia tarde with Dissolve(1.0)

    "..."

    $ tempo += 1

    scene ilha praia with Dissolve(1.0)

    "Ufa... acho que deu pra dar uma pensada na vida. Pelo menos eu decidi o que eu vou jantar. É um progresso."

    "E nem sinal da [h]. Já não tem sol nenhum faz um tempo, e ela não apareceu."

    "Hoje tá calor pelo menos. Eu não vou passar frio só de shorts."

    "Mas eu realmente queria ver ela..."

    "Ela devia tá só me zoando."

    "O que eu faço?"

    menu:
        "Chamar ela no bar":


            "Não adianta eu ficar aqui esperando e esperando. Assim a noite vai acabar e daí que não vai rolar nada mesmo."

            "Quem quer que aconteça tem que fazer acontecer. É isso aí."

            mc charmoso "Bora lá."

            "???" "Ei! Tá indo onde?!"

            mc surpreso "!"

            scene nop_img2 with Dissolve(1.0)

            pause

            h "Tava indo embora já?"

            mc envergonhado "N-não... eu ia no bar ver se você ia vir mesmo."

            h "Tudo isso é medo de eu não aparecer? Tenha piedade de você mesmo, homem."

            mc "Calma lá também, né? Quando a gente tem um compromisso a gente tem que cumprir."
        "Continuar esperando":


            $ nona_pp += 1

            "Eu não tenho porque apressar ela. A noite só tá começando. Eu sei que ela vai aparecer."

            "..."

            "Eu acho."

            "???" "Boa noite, senhor."

            mc charmoso "Uou!"

            scene nop_img2 with Dissolve(1.0)

            pause

            h "Demorei?"

            mc "Nah. Eu sabia que você ia chegar logo. Daí dei uma andada e talz."

            h "Boa."

    h "Tipo, eu queria ter vindo antes, mas eu quase nem vim. Colocar esse biquíni não foi fácil."

    mc charmoso "Mas eu tenho que falar. Você ficou perfeita nele."

    "A vendedora tinha razão quando disse que ela ia gostar... e eu também. Isso é minúsculo!"

    h "Eu não lembro a última vez que eu fui numa praia. Deve ter sido durante aquela revolução..."

    mc desconfiado "Revolução?"

    h "É. Uma vez..."

    menu:
        "Tenho que prestar atenção na história!":


            $ nona_pp += 2

            "Para de pensar besteira. Como ela vai confiar em você se você tratar ela desse jeito?"

            mc charmoso "C-certo. O que aconteceu mesmo?"

            h "Eu nem comecei a falar ainda."

            mc envergonhado "Opa. Malz."

            h "Faz um tempo, estavam tentando dar um golpe militar em um país na América Central. E me chamaram pra ajudar a impedir."

            h "Eu passei vários dias escondida em uma praia, hackeando servidores oficiais do governo militar."

            mc envergonhado "Como assim... certeza que não é um filme?"

            h "É sério. No fim, a gente vazou pra imprensa vários documentos confidenciais com fotos e vídeos de pessoas sendo torturadas."

            h "Tinha gente sendo eletrocutada, perdendo as unhas, sendo mantida em celas com ratos... coisas horríveis."

            mc desculpa "Caralho..."

            h "Veio à tona também que o governo tava gastando muito mais do que podia, fazendo dívidas por baixo do pano. Uma esculhambação."

            h "Quando o povo descobriu, o apoio do governo caiu muito, o suficiente pras pessoas irem pra rua e daí foi uma bola de neve."

            mc desconfiado "E você fez isso tudo sozinha?"

            h "Não foi bem assim... tinham outras pessoas envolvidas. Elas me deram um lugar pra ficar, comida e tudo o que eu precisava."

            mc charmoso "Entendi. Mesmo assim, você teve o papel central. Isso foi bem incrível, [h]..."

            scene nop_img3 with Dissolve(1.0)

            pause

            h "Não foi nada..."
        "Focar nos peitos dela...":


            "Eu preciso..."

            scene nop_img4 with Dissolve(1.0)

            pause

            "{i}gulp{/i}"

            "Cara, eu não consigo parar de olhar pra ela. Ela sempre teve esse peitão?"

            "Eles tão perfeitos nesse biquíni. O decote, a lateral... a pele dela... é tudo perfeito."

            window hide

            pause

            mc safado "..."

            scene nop_img3 with hpunch

            h "Ei! Você tá ouvindo?"

            mc surpreso "D-desculpa! E-eu me perdi um pouco!"

            h "Eu sabia que usar esse biquíni não era uma boa ideia. Nenhuma mulher consegue chamar a atenção pra mais nada com isso aqui."

            mc charmoso "É que você tá gostosa demais... não é culpa minha."

            h "Ah. Cala a boca, seu idiota. Eu vou embora."

            mc desculpa "C-calma! Desculpa! Foi mal. Eu fiquei empolgado demais. Desculpa..."

            h "Mais uma babaquice dessas e eu vou colocar você na coluna dos babacas."

            mc "Tá legal..."

    h "Desde a época desse trabalho eu não usava um biquíni. E eu tenho certeza que esse é ainda menor. Eu devia ter especificado o tamanho..."

    mc envergonhado "Agora é tarde demais."

    h "Um ponto pra você. Pelo menos tem umas luas e umas estrelas nele. Eu achei bem atencioso você ter notado esse detalhe."

    mc envergonhado "Haha... legal, né?"

    "Eu nem tinha reparado nisso."

    h "Mas mesmo me vendo assim, não quero que você fique tendo ideias."

    mc charmoso "Relaxa. Eu não sou um idiota. Eu só quero fazer uma coisa diferente com você."

    mc desculpa "Eu sei que você vive nas suas coisas, em um mundo totalmente diferente do meu. Por isso que eu pensei nisso..."

    mc normal "Quem sabe um dia na praia não mostre alguma coisa diferente e você acabe curtindo?"

    h "É... diferente... Hmm..."

    mc desconfiado "Que foi?"

    h "Você falou diferente, tava pensando num negócio aqui."

    scene black with dissolve

    mc surpreso "Ei!"

    scene nop_img5 with Dissolve(1.0)

    pause

    mc desconfiado "Onde você tá indo?"

    h "Eu tava pensando que pelo caminho que eu tomei pra chegar até aqui. Andando naquela estrada..."

    mc "Que que tem?"

    h "Você nunca reparou que não importa pra que lado a gente olha, não dá pra ver a ilha daqui?"

    mc "Hmm... é verdade..."

    mc "A gente tá bem perto dela. Não era pra ela desaparecer no horizonte."

    h "Só que ela não desapareceu. Desapareceu não é a palavra certa."

    mc "Então cadê a cidade? Vai falar que eu sou cego?"

    h "Não, bobo. A ilha tá depois destas pedras aqui."

    mc envergonhado "Essas pedras tão cheias de coisa de praia... é meio nojento."

    h "Para de frescura. A gente só precisa escalar elas e ver por cima."

    mc preocupado "Você tá falando sério mesmo?"

    h "É, ué. Vem!"

    scene black with dissolve

    mc surpreso "!"

    scene nop_img6 with Dissolve(1.0)

    pause

    mc angustiado "Q-que você tá fazendo?!"

    h "Vem logo!"

    "Subir nisso aí? É mais fácil ela cair e arruinar nosso encontro."

    "Essa mina só faz o que ela quer. Eu preciso... droga... o que eu faço?"

    menu:
        "Tentar escalar a pedra":


            $ nona_pp += 1

            mc angustiado "O-ok! Eu vou subir!"

            h "Você já fez isso antes?!"

            mc "Claro que não!"

            h "Toma cuidado onde você vai se apoiar! É meio escorregadio! Bota bastante força nas mãos e nas pernas!"

            mc "E-eu vou dar um jeito! Pode deixar!"

            h "Se você cair aqui de cima, vai machucar, hein?! Toma cuidado!"

            mc "Que merda..."
        "Falar pra ela descer":


            mc preocupado "Isso é perigoso, [h]! Desce daí! Tem outras coisas pra ver na praia!"

            h "Você disse que queria fazer uma coisa diferente! Isso aqui é diferente!"

            mc zerado "Você precisa parar de se apegar às palavras desse jeito..."

            mc normal "Eu só quero ter um tempo legal com você. Se você cair daí já era!"

            h "Eu não vou cair!"

            mc "Essa pedra é super íngrime!"

            h "E daí?! É só ter força nos braços! Vem logo!"

            mc concentrando "Não vai ter jeito... se eu desistir agora é o fim do encontro."

            h "Que foi?! Não te escutei!"

            mc preocupado "Eu vou subir! E toma cuidado pra não cair, louca!"

            h "Tá legal! Então vem comigo!"

            mc "Ai..."

    scene black with dissolve

    "..."

    h "Isso!"

    h "Consegui!"

    scene nop_img7 with Dissolve(1.0)

    pause

    h "Uou! Olha só pra isso, [mc]!"

    h "Eu disse que ia te mostrar uma coisa diferente, não disse?!"

    h "Olha só pra essa vista! Dá pra ver sua ilha inteirinha daqui!"

    h "O posto de gasolina que fica do lado do bar do [gar]! E tem o prédio do Cassino!"

    h "E também o prédio do NBC do idiota do Gevanni! Eu não piso lá nunca mais!"

    h "É legal, né?! Não é diferente igual você tinha falado?"

    h "[mc]?"

    mc angustiado "[h]!"

    h "Você achou alguma coisa legal aí?!"

    mc "[h]!!! Vem aqui!"

    h "Nada que você achou aí é melhor do que o que eu tô vendo agora... É tão incrível..."

    mc "[h]!!!"

    h "Nossa... espero que seja bom mesmo."

    scene nop_img8 with Dissolve(1.0)

    pause

    h "[mc]!"

    mc "Aleluia!"

    h "O que aconteceu?!"

    mc "Eu não consigo subir! Eu travei!"

    h "Segura na pedra e força pra cima."

    mc "E-eu sei! Mas onde eu pego tá escorregando! Nenhum lugar eu consigo puxar!"

    h "Ah... isso pode acontecer mesmo."

    mc "Como você subiu tão fácil?!"

    h "Sei lá. Eu só prestei atenção onde tinha musgo e o material da rocha parecia mais estável."

    mc "Como que uma pessoa que fica o dia todo no computador pode ser tão boa em escalar uma pedra?!"

    h "Você tá surtando por pouco..."

    h "Se você admitir que você perdeu pra uma garota que fica o dia todo no PC eu te ajudo."

    mc "Agora não é hora de lavar roupa suja! Eu tô caindo de verdade!"

    h "Admita."

    "Merda! Admitir que eu sou mais fraco que uma garota nerd?!"

    menu:
        "Nunca! Eu vou dar meu jeito!":


            mc "De jeito nenhum! Eu vou dar meu jeito!"

            h "Haha! Vai ser divertido ver você cair!"

            mc "Cala a boca! Eu só tenho que..."

            "Ok! Eu só preciso colocar a mão em tudo e ver onde dá pra eu puxar sem escorregar... O problema é que eu já fiz isso e não achei!"

            "Se eu puxar rápido talvez dê pra eu pegar lá na beirada. Eu tô perto do fim!"

            "Isso aqui não é força. É jeito... Ok! Respira e VAI!"

            scene red with vpunch

            mc angustiado "Não!"

            h "[mc]!"

            scene nop_img9 with vpunch

            pause

            h "Seu idiota!"

            mc "Meu Deus! Eu quase caí!"

            h "Se eu não tivesse segurado sua mão você ia se esborrachar!"

            mc "V-valeu!"
        "Eu admito! Agora me ajuda!":


            $ nona_pp += 1

            mc "Tá bom! Só me ajuda antes que eu me esborrache!"

            h "Então admita! Vai! Fala!"

            mc "Eu admito que eu perdi pra uma garota! Socorro!"

            h "Haha! Calma! Me dá sua mão!"

            scene nop_img9 with Dissolve(1.0)

            pause

            h "Isso. Agora empurra com os pés."

    h "Eu vou te puxar pra cima! Vem com força pra me ajudar!"

    mc "Tá!"

    h "Bastante força nas pernas, se não eu vou te soltar! Eu não aguento seu peso sem sua ajuda!"

    mc "T-tá bom!"

    h "No três! 1, 2, 3!"

    h "PULA!!!"

    mc "Iaaah!!"

    scene nop_img10 with vpunch

    pause

    mc "Aaahh!"

    h "Ai!"

    h "Você colocou força de mais!"

    mc "Desculpa! Você que falou!"

    h "É! Mas não precisava exagerar! Você precisa saber calcular essas coisas!"

    mc "Quem no mundo sabe calcular uma coisa dessas?!"

    h "Eu bati minha cabeça..."

    mc "Foi mal... eu não queria forçar."

    "Nossa... eu tô no meio das pernas dela. Eu consigo sentir ela bem colada em mim..."

    "Acho que ela nem percebeu ainda."

    h "Isso que dá querer ajudar os outros. Por isso que eu faço as coisas sozinhas..."

    mc "Se não fosse por você eu ia... ter me ferrado lá no chão. Valeu."

    h "Como que você não sabia como subir? É tão fácil..."

    mc "Fácil pra você... parece que você sabe fazer tudo."

    h "Hmf... ok... Ei!"

    "Ixi."

    h "O que você tá fazendo me abraçando ainda? Levanta."

    if nona_interesse:

        "Eu consigo sentir a respiração dela. Ela tá ofegante. E o cheiro da [h] é tão bom..."

        "Será que eu posso... tipo, a gente tá tão perto... e se eu tentasse..."

        h "Vai. Dá licença logo..."

        menu:
            "Eu vou ficar aqui mais um pouco.":


                mc "E se eu ficar aqui mais um pouquinho?"

                h "Quê?"

                scene nop_img11 with Dissolve(1.0)

                pause

                mc "Quando eu te chamei pra esse passeio, eu não pensei que ia ter a chance de ficar assim com você."

                h "F-foi um acidente."

                mc "Não importa. Eu tô tão colado em você agora... eu tô sentindo seu cheiro, e você tá me deixando doido."

                h "Você tá entendendo tudo errado."

                mc "E daí se foi um acidente? A gente não pode aproveitar?"

                mc "Eu tô no meio das suas pernas, com a boca pertinho da sua... por que a gente só não aproveita?"

                h "[mc]..."

                mc "Eu sei que você gosta de mim também. Se não você não teria aceitado vir. Só vamo, [h]."

                h "Sai de cima de mim agora."

                "Eita!"

                mc "Ma-"

                h "Se você não sair agora eu hackeio você e mando pro seu chefe."

                mc "E-e-ei! Era só brincadeira hahaha!"

                "Credo! Que medo!"

                h "Eu sei. A gente tá na praia, eu salvei sua vida, mas vai com calma."

                mc "Hehe... ok. Desculpa se eu exagerei."

                h "Tá tudo bem."

                scene black with dissolve

                mc angustiado "{i}gulp{/i}"

                "Droga. Eu não devia ter ido com tanta sede ao pote. [mc] burro! Você vai acabar ficando sem nada se continuar assim."

                h "Até meu biquíni saiu tudo aqui. Deixa eu me ajeitar."
            "Melhor eu levantar.":


                $ nona_pp += 2

                "Melhor eu não abusar. Não posso perder nenhum ponto com ela. As coisas já tão difíceis fazendo tudo certo."

                "Se eu tiver calma a oportunidade vai aparecer."

                jump nona_praia_parte_saiu
    else:

        label nona_praia_parte_saiu:

            pass

        mc "Opa. Deixa eu levantar."

        h "Isso... Até meu biquíni saiu tudo aqui. Deixa eu me ajeitar."

        scene black with dissolve

    mc envergonhado "Haha..."

    scene nop_img13 with Dissolve(1.0)

    pause

    h "Quando você disse que não sabia subir, você tava sendo bem sincero..."

    mc zerado "Eu falei."

    h "Mas olha aqui do meu lado. Valeu ou não a pena?"

    mc normal "Uou. Ver a ilha daqui é foda mesmo."

    h "Bota foda nisso. Aposto que quase ninguém sabe desse lugar aqui."

    mc "Eles deviam tirar essas pedras, pra gente poder ver a ilha da praia normal."

    h "Pois é. A não ser que eles não queiram que a gente veja ela."

    mc desconfiado "Hm? Por que eles não iam querer?"

    h "Sei lá. Foi só uma coisa que passou na minha cabeça."

    mc "Hmmm... parece meio teoria da conspiração isso."

    h "Com certeza. Mas olhando daqui, você percebeu como essa ilha é meio diferente?"

    mc "Diferente como?"

    h "Ela é muito 'certinha'. Não tem montanha ou terra ou alguma floresta ou até irregularidades."

    h "Olhando daqui, dá pra ver que a área construída ocupa toda a extensão da ilha."

    mc "Estranho. Até parece que dá pra pessoa pular da ilha no mar, de tão perto que fica."

    h "Obviamente não é assim também. Da onde a gente tá não dá pra ver os detalhes."

    h "Mas mesmo assim tudo parece bem feito demais. Parece que ela foi criada exatamente pra isso."

    mc zerado "Tá falando que a ilha na verdade foi construída por alguém? Dá pra fazer isso?"

    h "Existem ilhas artificiais, mas não são exatamente assim."

    mc envergonhado "Essa conversa parece de louco, [h]."

    h "Acho que sim..."

    mc charmoso "A gente veio pra curtir, você precisa deixar seus planejamentos de lado enquanto a gente tá aqui."

    h "Você tá certo... combinado."

    scene nop_img14 with Dissolve(1.0)

    pause

    mc "Opa. Se aconchegou aqui do lado. Agora gostei."

    h "Aposto que não foi fácil me chamar pra vir aqui, né? Eu não sou a pessoa mais fácil de conviver. Eu sei disso."

    mc "Eu tava com medo que você não fosse aceitar. Parecia meio fora demais do seu jeito."

    h "É... se fosse outra pessoa chamando provavelmente eu nunca viria. Mas eu nunca tive a chance de agradecer você."

    mc "Pelo quê?"

    h "Por você ter me salvado. Aquela noite e tudo o que aconteceu depois foi tão corrido. Eu não consegui."

    h "Daí eu pensei que hoje podia ser uma boa chance."

    menu:
        "Não precisa agradecer.":


            mc "Você não tem que agradecer nada. Eu só fiz o que eu queria aquela noite com o [to]."

            h "Obrigada, mas eu realmente devo minha vida a você. Se não fosse você, eu teria morrido lá."

            mc "A gente nem precisa falar disso mais. É coisa do passado. Foi um lance pesado."

            h "Tem razão. A gente tá aqui pra se divertir."
        "Ver você de biquíni foi um começo.":


            $ nona_pp += 1

            mc "Com todo o respeito, ver você com esse biquíni tá sendo um bom começo..."

            h "Não foi o suficiente? Não foi fácil pra mim colocar isso aqui e aparecer na sua frente."

            h "Eu não tô nada acostumada com esse tipo de coisa."

            mc "Tá sendo bacana poder apreciar você, mas meu preço é mais alto. Vamos ver se até o fim da noite você consegue."

            h "Eu também posso dar o calote. É uma opção."

            mc "Haha... sacanagem isso..."

    mc "Sem querer ficar te aperriando, mas você causou comigo várias vezes."

    h "Eu?"

    mc "Você."

    mc "Quando hackeou meu celular, transferiu dinheiro pra minha conta, me usou no assalto ao NBC. Eu só sofri na sua mão."

    h "Falando assim... eu realmente joguei bastante coisa em você."

    mc "Eu sou cara normal ainda por cima. Eu não derrubo governos. Eu só consigo pautas pra manter meu emprego."

    h "E mesmo assim você quis sair comigo? Você é masoquista?"

    mc "Haha... não sei. Talvez eu seja."

    if nona_interesse:

        mc "Mas tem outra razão..."

        scene nop_img15 with Dissolve(1.0)

        pause

        h "Hm?"

        mc "Aquele dia no bar eu disse que queria um lance a mais com você."

        h "Tudo isso pra ficar comigo?"

        mc "Se eu realmente ficar com você, tudo isso vai ser pouco."

        h "Até ser laranja em um esquema de roubar banco?"

        mc "Até isso..."

        h "Você parece um rapaz bem determinado quando o assunto é paquerar."

        mc "Eu sou determinado quando o assunto é você."

        h "..."

        mc "Parece que finalmente eu consegui te deixar sem jeito."

        h "É..."

    h "[mc]... você parece um cara simplão, sabe?"

    mc "Já vai começar o bullying?"

    h "Espera. Eu quero falar algo legal sobre você. É que você não é o que você parece."

    h "Você parece simples, até meio banal às vezes, correndo atrás das suas coisas. Mas depois que a gente conversou, eu mudei de ideia."

    h "Eu nunca consegui falar muito com alguém. Eu sempre preferi fazer as coisas sozinha."

    mc "O [gar] tem até medo de falar com você."

    h "É sempre assim... e como eu tô sempre viajando, isso só piora minha situação."

    h "Mas o jeito que você fala comigo aqui. É como se eu fosse só uma pessoa normal, sabe?"

    mc "Pacata? Banal? Simples?"

    h "É... e ao mesmo tempo eu nunca imaginei que ser pacata podia ser tão... bom."

    h "Parar de pensar em códigos e esquemas nacionais, e só curtir uma noite agradável com um cara legal."

    h "O que eu quero dizer é... obrigada por ter lutado pra me trazer aqui."

    h "É a primeira vez que eu vejo alguém fazendo tudo isso só pra ficar comigo."

    if not nona_interesse:

        mc "F-ficar no bom sentido, né?"

        h "Sim, bobo..."

        scene nop_img16 with Dissolve(1.0)

        pause

        h "Eu sempre tive parceiros que me ajudaram em vários países. Pessoas que possibilitaram fazer tudo o que eu fiz."

        h "Mas nunca eu tive um amigo de verdade. Alguém que não tá com você por uma situação prática."

        mc normal "Sei. Alguém que fica do seu lado porque gosta de você. Não porque tem um motivo."

        h "Isso."

        mc "É mais uma coisa do coração e menos da cabeça."

        h "V-você se sente assim comigo?"

        mc "Não sei. Acho que a gente não se conhece há tanto tempo pra dizer com certeza. Mas eu gostei muito do nosso tempo aqui hoje."

        mc "E eu me sinto bem do seu lado. Talvez seja o tal do santo bateu."

        h "Nunca tinha ouvido falar disso."

        mc envergonhado "Ah! Quer dizer que a gente deu certo, mesmo sem ter passado muito tempo junto ainda. A gente só se gosta, sabe?"

        h "Haha... então acho que o nosso santo bateu mesmo. É assim que fala?"

        mc normal "Isso aí."

        h "É... Tem uma coisa que eu não contei pra você ainda. Mas agora que a gente é amigos, eu meio que fiquei com vontade de falar."

        mc desconfiado "Hm?"

        h "Eu tô aqui na capital do seu país porque um grupo me chamou. Pessoas que querem acabar com o domínio das famílias Donatello e Alighieri."

        mc "Sério?!"

        h "É. Eles me provaram que todo esse avanço da capital é mentiroso. O governo do Donatello esconde a realidade por muitos anos."

        h "Superfaturando obras caríssimas e privilegiando parceiros nos negócios, eles criaram um Clube dos Escolhidos."

        h "Esse Clube tem empresas de várias áreas, desde comunicação até moda, e juntos eles garantem um monopólio nacional."

        h "Só que por baixo dos panos tem muita gente sofrendo aqui. Desemprego, fome, falta de saúde, educação, trabalho ilegal."

        h "Toda essa parte tá sendo encoberta com a ajuda de uma mídia que faz parte do Clube."

        mc "Então toda essa teoria da conspiração sobre o governo é verdade?"

        h "Não sei se tudo é verdade, mas se a gente não fizer alguma coisa, uma hora essa bomba vai explodir, e seu país vai tá quebrado."

        h "A gente precisa fazer nossa parte e revelar o que eles tão escondendo e deixar que a sociedade decida o que fazer."

        mc "Então é isso que você veio fazer..."

        h "É. Esse é o meu trabalho. Eu tô torcendo pra que a gente consiga fazer tudo dar certo aqui também."

        mc charmoso "Valeu por confiar em mim e me contar. Espero que você consiga."

        h "Talvez eu acabe contando com sua ajuda de novo..."

        mc envergonhado "Contanto que eu não acabe preso..."

        h "Não dá pra prometer nada..."

        mc zerado "Sabia."

        h "Amanhã eu tenho que acordar cedo pra fazer uma coisa. Tudo bem se a gente voltar?"

        mc desculpa "Tava massa, mas tudo bem."

        mc normal "Só se eu puder acompanhar você até o bar."

        h "Eu já ia pedir isso."

        mc "Então vamo."

        scene black with Dissolve(3.0)

        scene mapa cidade_noite with Dissolve(1.0)

        pause

        "Foi massa sair com a [h] hoje. Eu sinto que a gente pode ser grandes amigos."

        "Agora eu quero ver o que ela vai aprontar pra cima do [to], do Donatello e toda a gangue..."

        "Esse duelo final entre eles vai ser um negócio grande. Eu preciso tá aqui pra ver isso!"
    else:


        mc "Se você tá falando ficar no sentido de te beijar... de te agarrar... senti-"

        h "Eu entendi... você é um safado."

        h "Assim... eu vou falar a verdade. Isso até me deu uma vontade de fazer uma coisa safada hoje."

        menu:
            "O que você quer fazer?":


                mc "Sério? Tipo o quê? Eu posso participar?"

                h "Claro que você pode. É pra você mesmo que eu quero fazer."

                mc "O-ok."
            "Eu topo qualquer coisa.":


                $ nona_pp += 1

                mc "O que você quiser fazer eu tô dentro."

                h "Eu tava achando isso também."

                mc "Você não sabe como eu tô louco em você, [h]."

                h "Hmm..."

        h "Você gostou de me ver de biquíni."

        mc "Claro. Você tá tão gata nele."

        h "Eu quero fazer uma coisa que até hoje eu nunca fiz. E-eu quero fazer um homem ficar excitado."

        "Q-quê?!"

        h "Eu quero fazer isso pra você. V-você topa?"

        mc "Claro."

        h "Então olha pra mim... vai ser um show só pra você."

        scene black with dissolve

        h "Preparado?"

        mc safado "Com certeza..."

        scene nop_img17 with Dissolve(1.0)

        pause

        h "..."

        h "Nem acredito que eu tô fazendo uma coisa dessas."

        mc charmoso "Você tá indo bem. Tá sensual pra caralho."

        h "Não vai mentir pra mim. Eu não quero fazer papel de idiota."

        mc "É verdade. Pode acreditar em mim. Você tá conseguindo me deixar com mais vontade ainda."

        h "Calma. Você vai ver agora."

        window hide

        pause

        scene nop_img18 with Dissolve(1.0)

        pause

        mc tarado "Você tá muito gata, [h]."

        h "Isso é o suficiente pra você? Eu esperava mais..."

        mc "Eu não vou reclamar se você continuar me provocando desse jeito."

        h "Eu quero fazer mais pra você. Eu quero ver você não aguentando mais."

        h "Eu nunca vi alguém me olhando com esses olhos de desejo..."

        mc "Eu podia comer você agora mesmo."

        h "Ai... é isso que eu quero... continua me querendo assim."

        h "Agora olha pra cá."

        window hide

        pause

        scene nop_img19 with Dissolve(1.0)

        pause

        h "Olha pro meu corpo bem de pertinho... você quer ele?"

        mc safado "Com certeza. Eu quero agora."

        h "Você só pode ver agora."

        mc "Não judia de mim assim."

        h "Isso é judiar? Poder ver o corpo da garota mais gostosa que você já conheceu?"

        h "E esse biquíni ainda cobre tão pouquinho... dá pra você ver meus peitos, minhas coxas, minha barriguinha sexy..."

        mc "Você é perfeita..."

        h "E agora... a melhor parte..."

        window hide

        pause

        scene nop_img20 with vpunch

        pause

        h "Boo! Acabou!"

        mc "Acabou? E a melhor parte?"

        h "A melhor parte é ter terminado um bom serviço."

        mc "Até acho que foi uma boa. Eu t-tava quase te atacando."

        h "Você é um cara legal demais pra fazer uma coisa dessas. Eu não sei por que, [mc], mas eu tenho confiança em você."

        menu:
            "Vai nessa. Uma hora eu te pego.":


                mc "Vai nessa de confiança, que uma hora eu te pego de jeito aí."

                h "A é? Será que é melhor eu ir embora então? Eu não sei se eu quero ficar do lado de um cara que não sabe se controlar."

                mc "Não precisa. Pode ficar aí. Tá tudo sob controle agora."
            "Que bom. Pode confiar em mim.":


                $ nona_pp += 1

                mc "Eu nunca ia fazer uma coisa que você não tivesse de acordo."

                h "É engraçado como eu acredito em você quando você fala isso."

                mc "Deve ser minha voz suave e segura."

                h "Não exagera."

        h "Mas foi divertido brincar com você assim. Eu fiquei nervosa, mas depois eu gostei bastante."

        mc "Eu gostei bastante também."

        h "Gostou mesmo ou só tá me agradando? Eu fui idiota, não fui?"

        mc "De jeito nenhum. Você tava sexy de verdade."

        mc "E eu acho incrível como você é perfeita."

        h "A-ah?"

        scene nop_img21 with Dissolve(1.0)

        pause

        mc "É sério. Eu fico impressionado como você é linda, gostosa, inteligente, engraçada, tem experiência de vida..."

        mc "Eu nunca vi uma mulher igual você antes. E tão nova ainda."

        mc "O cara que tiver a chance de ficar com você, vai ser o cara que venceu a vida."

        h "Será que eu sou tudo isso mesmo? Você provavelmente tá exagerando. Perfeito é uma palavra que não admite qualquer erro."

        h "Eu tenho medo de algumas coisas, igual a maioria das pessoas."

        mc "Eu toparia qualquer defeito seu pra poder ficar contigo. Isso eu tenho certeza."

        h "[mc]... você não tem medo de dar em cima de alguém que você acha perfeito?"

        mc "Um pouco eu tenho. Às vezes eu penso como deve ser ridículo um cara super normalzão igual eu querendo criar asa pra cima de você."

        mc "Mas, sei lá, eu só falo o que vem na cabeça."

        mc "E-eu tô fazendo papel de ridículo?"

        h "Não. Não tá. P-pode falar mais... e-eu gosto de ouvir você..."

        mc "Então..."

        scene nop_img22 with Dissolve(1.0)

        pause

        h "E-ei! Você tá perto demais."

        mc "Eu quero que você escute melhor o que eu vou te falar agora."

        h "..."

        mc "Eu sei que você vive uma vida completamente diferente da minha. Fugindo de mafiosos e ditadores."

        mc "Eu sou só um cara querendo uma vida melhor na cidade grande. Sem nenhuma ambição muito grande."

        mc "Mas eu acho que, no fundo, todos nós temos os mesmos desejos no coração."

        mc "A gente quer ser amado, desejado, compreendido... e isso é igual pra todo mundo."

        mc "E por mais que eu não possa te ajudar em tudo na sua vida, eu posso atender esses desejos do seu coração."

        h "Você vai salvar meu coração..."

        mc "Isso. Eu vou fazer de você uma mulher completa por dentro, pra que você possa fazer tudo o que tem que fazer por fora."

        mc "Eu quero ser seu porto seguro, pra quando você voltar ferida, alguém esteja lá te esperando pra ouvir."

        mc "E claro... alguém que possa melhorar seu dia te dando muito prazer, e atendendo seus desejos de mulher..."

        h "Ai..."

        scene nop_img23 with Dissolve(1.0)

        pause

        mc "Tira esse óculos e deixa eu ver a [h] de verdade... completamente exposta."

        h "M-meu coração tá batendo tão forte agora. Eu n-não consigo pensar direito. I-isso é perigoso."

        mc "Não é não. Só se entrega pra mim. Eu vou cuidar de você."

        mc "Você vai ter uma aventura que você nunca teve e você vai gostar muito."

        h "Ai... E-eu não sei..."

        h "{i}puf puf{/i}"

        mc "Deixa eu mostrar pra você o que você ainda não sabe."

        h "E-eu não consigo respirar, minha cabeça tá z-zonza... eu nunca senti isso antes."

        mc "Xiii... deixa tudo comigo agora."

        if nona_pp >= 7:

            $ nona_praia_beijo = True

            h "T-tá... c-cuida de mim, [mc]..."

            mc "Com todo o prazer."

            scene nop_img24 with Dissolve(1.0)

            pause

            h "Ah... Hmm..."

            mc "Sua boca é tão gostosa, [h]."

            h "A sua t-também."

            "Quem imaginou que eu ia ter a [h] assim nos meus braços desse jeito, inteirinha pra mim."

            "Eu tô passando a língua na boca dela e ela tá gostando."

            h "Hm... ah..."

            "Eu não preciso parar aqui. A gente tá sozinhos aqui na praia, nesse lugar escondido."

            "Eu duvido que eu vou ter outra chance de transar com ela. Tem que ser hoje."

            mc "Hoje você vai ser minha mulher."

            h "Ah! Vou..."

            mc "Eu vou pegar em você inteira."

            scene nop_img25 with Dissolve(1.0)

            pause

            h "Hm!"

            mc "Seu peito é tão macio... você é muito gostosa mesmo."

            h "Ai... não aperta aí."

            mc "Eu vou massagear você gostoso."

            h "E-eu tô... não... ah... ai!"

            h "Ai, [mc]! Não b-brinca comigo assim! Ah!"

            mc "Só me beija!"

            h "I-isso é demais... eu vou e-explodir assim!"

            mc "Isso. Eu quero ver você gritando de prazer!"

            h "Ah! Não! N-não! Ai! Aah! Chega! Não!"

            "Mais um pouco!"

            label nona_praia_caiu:

                pass

            h "N-não!!"

            mc "[h]!"

            scene nop_img26 with vpunch

            h "Eu d-disse chega! Aaaahhh!"

            mc "U-uouuuuu!"

            mc "[h]! Socorro!"

            h "[mc]! Você vai cair fora da pedra!"

            mc "Aaaaaahhh!"

            scene nop_img27 with vpunch

            pause

            mc "Nonaaaaaaaaaaa!"

            h "Ixi..."

            h "Sorte que esse é o lado da água..."

            h "Só cuidado não bater a cabeça na pedra!"

            mc "Socorrrrrrrooooooo!"

            scene red with vpunch

            pause

            "{i}TCHIBUUMN{/i}"

            mc "{i}glob glub glob{/i}"

            h "[mc]!"

            scene nop_img28 with vpunch

            pause

            mc "{i}Puuuuaaah{/i}"

            h "O homem tá vivo!"

            mc "Eu tô vivo!"

            h "Ebaaa!"

            mc "[h]! A correnteza tá me levando!"

            h "Nossa..."

            mc "Tá forte demais pra eu nada!"

            h "Tente se manter boiando e veja pra onde ela vai te levar!"

            mc "Você é louca?! Eu vou morrer!"

            if nona_praia_beijo:

                h "Pelo menos você me beijou! Foi uma boa vida!"

            mc "Eu sou novo demais pra morrer!"

            scene black with Dissolve(3.0)

            "..."

            scene mapa cidade_noite with Dissolve(1.0)

            "Sorte que a correnteza acabou me levando pra areia e eu consegui voltar."

            "A [h] podia ter falado alguma coisa melhor ao invés de só ficar rindo igual uma idiota."

            "Eu sabia que um encontro com a [h] na praia ia ser diferente de tudo o que eu já tinha visto."

            if nona_praia_beijo:

                "Mas a gente acabou se pegando. Caralho... aquilo foi muito bom."

                "Pena que ela não deixou as coisas continuarem. Acho que é cedo demais pra ela."

                "Talvez ela seja virgem... e e-eu tenha a chance de ser o primeiro. Isso seria incrível..."
            else:


                "Infelizmente eu não consegui beijar ela. Talvez se eu tivesse levado o encontro de outra forma... ter sido mais de boa..."

            "Mas foi incrível! Não vejo a hora de fazer alguma outra coisa com ela."
        else:


            h "N-não, [mc]."

            mc "Você fala isso porque tá com medo."

            h "C-chega. E-eu não quero fazer isso com você."

            mc "Eu vou mostrar pra você como você precisa desse lado também."

            h "Não!"

            jump nona_praia_caiu

    $ tempo = 4

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
