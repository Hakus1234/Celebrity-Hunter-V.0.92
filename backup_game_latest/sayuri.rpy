

label sayuri_cel_msg1_resposta:

    $ sayuri_cel_msg1_resposta_check = False

    mc desconfiado "Que tipo de mensagem é essa?"

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s2_save", extra_info="s2_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    "Por que será que ela está falando comigo dessa forma? Será que ela tá brincando comigo?"

    "Mas e se alguém pegou o celular dela e está brincando comigo?"

    "O que eu devo responder?"

    menu:
        "...":


            $ sayuri_cel_msg1_r = "zoado"

            "Não vou falar nada. Não gostei do jeito que ela escreveu."

            "Não é porque ela é uma medalhista olímpica que ela pode falar comigo como se eu fosse um idiota."

            "Mas pode ser que seja alguém brincando ou algo assim, então não vou falar nada."

            "..."
        "Tudo bem, Sayuri?":


            $ sayuri_cel_msg1_r = "amizade"

            $ sayuri_amizade += 1

            "E se ela estiver com algum problema? Talvez eu possa ajudar..."

            "Enviei."

            "..."

    "Ela respondeu."

    show screen celular_sayuri

    "..."

    if estou_na_cidade:

        call call_cidade from _call_call_cidade_2
    else:


        return

label sayuri_cel_msg2_resposta:

    $ sayuri_cel_msg2_resposta_check = False

    mc muitofeliz "HAHAHA!"

    mc feliz "Não consigo parar de rir..."

    mc feliz "Tadinha... Primeira vez usando o WhatsApp? Será que isso é realmente possível?"

    mc normal "Meu Deus... Essa foi boa."

    "Acho que vai ser impossível conversarmos assim..."

    "Eu posso eu mesmo ligar, mas acho que eu iria assustar ela. Talvez seja melhor só esperar... Não sei..."

    menu:
        "Concordar com a ligação dela":


            $ sayuri_amizade += 1

            "Se ela quer falar por voz, tudo bem por mim."

            "..."

            "..."

            "Smartphone" "Trrr... Trrr..."
        "Você mesmo fazer a ligação":


            "Claro que podemos falar por voz. E melhor ainda, eu mesmo vou ligar."

            "Tenho que mostrar proatividade se eu realmente quero tomar as rédeas da relação."

            "..."









    mc normal "Alô? [s]?"

    s s_assustada "Olá. Senhor [mcc]?"

    mc feliz "Não precisa me chamar de senhor, [s]."

    mc normal "Apenas [mc] está excelente."

    s "... Ok."

    s "..."

    menu:
        "...":


            mc zerado "..."

            s "..."

            "Voz feminina no fundo" "{size=15}Fala alguma coisa!{/size}"

            mc desconfiado "..."
        "E então? O que você queria?":


            mc normal "E então? O que você queria falar?"

    s "É..."

    s "Desculpa por antes. Eu não sou acostumada a usar o celular..."

    s "Quando eu tenho que mandar mensagem pra alguém, minha irmã que manda..."

    "Voz feminina no fundo" "{size=15}Fala pra ele que você comprou o celular só pra falar com ele!{/size}"

    s "Ssshhhh..."

    s "É... É..."

    "Meu Deus! Olha essa mina..."

    "E agora? Posso fingir que não ouvi ou tentar avançar..."

    menu:
        "Verdade? Você me deixa lisongeado, [s].":


            mc surpreso "Puxa! Você comprou o celular só pra falar comigo?"

            s "..."

            mc normal "Isso é realmente muito legal da sua parte. Obrigado."

            s "Não! Não foi nada... eu tava precisando mesmo."

            mc safado "Mesmo assim, espero poder recompensar você um dia."

            s "..."
        "Sério que você não tinha celular?!":


            mc desconfiado "Sério que você não tinha celular até hoje?"

            s "Ah! E agora? ..."

            s "Eu..."

            mc feliz "Não se preocupe! Não tem nada tão incrível no celular assim. Só é algo que a gente não costuma ver sempre."

            s "Sei..."

            s "{size=15}Ele ouviu! Eu vou te matar sua intrometida...{/size}"
        "Acho que eu ouvi uma voz no fundo, mas não entendi...":


            $ sayuri_amizade += 1

            "Melhor mentir e aliviar as coisas para ela..."

            mc normal "Parece que eu escutei uma voz no fundo. Mas não entendi o que disseram."

            s "Ah! Que bom... Quer dizer! Não é nada... É só minha irmã..."

    s "Então... Eu tava pensando se você gostaria de conversar comigo."

    mc normal "Hmm... Acho que é o que estamos fazendo agora..."

    s "Digo! Conversar juntos! É... Em algum lugar..."

    mc desconfiado "..."

    "Voz feminina no fundo" "{size=20}Ela tá te chamando pra sair o tonto!{/size}"

    mc surpreso "..."

    s "... {size=15}Sai pra lá!{/size}"

    "Ela quer sair comigo!"

    "Isso é incrível! Tenho a chance de sair com uma atleta olímpica!"

    "Não tenho o que perder saindo com ela. Ela é linda, bem-sucedida e mesmo que ela acabe sendo uma terrível companhia, ainda posso conseguir pautas para o chefe..."

    menu:
        "Você tá me chamando pra um encontro?":


            mc charmoso "Por acaso você está me chamando para um encontro?"

            s "Ah! É! Não!"

            mc charmoso "Porque é o que tá parecendo..."

            s "..."

            mc charmoso "Mas é claro que eu aceito. Quem recusaria o convite de uma garota linda como você?"

            s "Ok..."

            "Parece que ela fica com muita vergonha quando falo assim..."
        "Claro que eu aceito.":


            $ sayuri_amizade += 1

            mc normal "Claro que eu aceito."

            mc normal "Estou mesmo precisando conversar com alguém. Acho uma boa ideia."

            s "Que bom! Eu também acho."

            "Se ela não achasse não estaria me convidando... Essa garota é estranha..."
        "Infelizmente não vou poder sair com você.":


            "Tenho coisas mais urgentes para fazer no momento."

            "Talvez a gente possa sair em uma outra hora."

            mc triste "Olha, [s]. Infelizmente não vou poder sair com você."

            mc normal "Estou correndo com umas coisas aqui. Fica para a próxima, ok?"

            s "..."

            s "Tudo... Tudo bem. Tchau."

            mc triste "... Ela parece ter ficado bem chateada."

            mc feliz "Fazer o quê. Quem sabe em uma próxima..."

            jump priscila_out_1

            if estou_na_cidade:

                call call_cidade from _call_call_cidade_3
            else:


                return

    "..."

    mc normal "Sabe? Eu tenho um lugar que eu acho que você vai adorar."

    s "É?"

    mc normal "Sim! Tem tudo a ver com você. E eu sempre quis ir lá."

    mc normal "O nome do lugar é Canto Tadaima."

    s "Ca.. Canto Ta.. Tadaima? Mas..."

    mc "Isso! Tenho certeza que você vai adorar."

    s "É... Ok."

    mc "Legal! O que acha de irmos agora?"

    s "Ah... Tudo bem. Já estou..."

    "Voz feminina no fundo" "{size=15}Nada disso! Fala pra ele esperar algumas horas!{/size}"

    s "Mas daqui algumas horas você..."

    "Voz feminina no fundo" "{size=15}Por isso mesmo!{/size}"

    s "Mas..."

    mc zerado "[s]? Ainda está aí?"

    s "Ah! Perdão! Eu estava... Então a gente se encontra lá em duas horas."

    mc normal "Combinado. Te espero lá!"

    s "Ok..."

    mc "Até."

    s "Tchau."

    "..."

    mc feliz "Excelente! Quem imaginaria que ela ligaria pra mim! Parece que minha sorte na vida finalmente está mudando!"

    mc triste "Mas não é hora de ficar sonhando... Preciso me preparar. O Tadaima fica meio perto de casa, então vou começar indo pra lá."





    jump sayuri_evento2

label sayuri_cel_msg3_resposta:

    mc surpreso "Uou! A [s] realmente melhorou muito! Ela tá até escrevendo certinho igual eu faço."

    "Ela deve ter realmente levado à sério esse negócio de treino."

    "Caramba! Então quer dizer que a [g] já contou pra ela sobre o lance da faculdade..."

    "O bom é que parece que a [s] tá levando numa boa."

    if julia_e1 == "seducao":

        "Só espero que a [g] não tenha contado tudo o que a gente fez lá no parque."

        mc incomodado "Por favor, [g]. Quebra essa pra mim por favor..."

    "Vou agir como se nada tivesse acontecido."

    "..."

    "Pronto. Tomara que ela realmente não saiba de nada."

    "Eu não sei quais são minhas intenções ainda com elas. Ainda não tenho certeza que tipo de relação eu quero com elas."

    if sayuri_e2 == "amizade":

        "Lá no Tadaima a [s] se abriu comigo e tudo o mais. Achei que ela foi super sincera."

    if julia_e1 == "seducao":

        "Mas eu também tive aquele lance com a [g] no parque..."

    if julia_conversou:

        "Eu ainda acabei conversando com ela e descobri que mesmo sendo peralta desse jeito ela também tem um passado complicado."

    "Provavelmente eu não posso ter uma relação íntima com as duas..."

    mc tarado "Ou será que eu posso?"

    "Não sei se a melhor coisa é arriscar. Se eu acabasse conquistando as duas e uma delas descobrir a [s] ficaria muito mal."

    mc zerado "A outra acho que nem ia ligar..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s3_save", extra_info="s3_save")

    $ iconchefe += 1

    "Mas não é..."

    $ renpy.vibrate(1)



    $ sayuri_cel_msg3_r = "iniciando"

    "Opa. Ela respondeu."

    show screen celular_sayuri

    "..."

    mc desconfiado "O que é isso?!"

    "Acho que a [s] tirou uma foto sem querer..."

    mc feliz "Acho que ela não tá tão bem assim no celular como parece."

    "Epa... ela tá escrevendo..."

    $ sayuri_cel_msg3_r = "continuando"

    show screen celular_sayuri

    "..."

    "E agora? A menina tá tendo um surto. O que eu vou falar pra ela?"

    "A [s] é toda envergonhada. Tenho que pensar a melhor forma de abordar isso."

    "Eu vou escrever..."

    menu:
        "Você tá linda!":


            "Caraca! Eu nunca reparei como a [s] é bonita. Será que eu tenho uma tara por orientais?"

            "Não vou ter medo. Vou falar a verdade pra ela."

            "..."

            "Ela respondeu."

            $ sayuri_cel_msg3_r = "linda"

            show screen celular_sayuri

            "..."

            "Ela ficou toda envergonhada... Mas não vou pegar leve com ela."

            "Preciso ser confiante se eu quero que ela me veja como algo mais do que um amigo."
        "O que foi? Não tô vendo nada.":


            $ sayuri_amizade += 1

            "Vou só fingir que não vi nada."

            "Ela não sabe nada de celular mesmo."

            $ sayuri_cel_msg3_r = "mentira"

            show screen celular_sayuri

            "..."

            "Funcionou. Só espero que ela não se lembre disso quando aprender mais sobre o WhatsApp."
        "Não se preocupe. Isso acontece.":


            $ sayuri_amizade += 2

            "Fazer o quê. Isso é normal. Não posso fazer disso algo gigante."

            "Ela vai se sentir melhor se eu agir naturalmente."

            $ sayuri_cel_msg3_r = "normal"

            show screen celular_sayuri

            "..."

            "Ufa... Acho que ela entendeu. Ela até mandou um emoji!"

    "..."

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Epa. Ela tá me ligando."

    "Eu sinto que ela tá ficando mais à vontade ao falar comigo. Isso é muito bom."

    mc normal "Alô? [s]?"

    s s_assustada "O-oi!"

    s "Estou incomodando?"

    mc "Claro que não."

    s "Tá. Desculpa ligar. É que..."

    mc desconfiado "O que foi?"

    s "Esse negócio da foto me deixou um pouco assustada. Não quero mais escrever mensagem."

    mc feliz "Não se preocupe muito com isso, [s]."

    s "O-ok."

    s "..."

    mc normal "..."

    s "É..."

    if sayuri_e2 == "amizade":

        s "Não sei como falar isso..."

        mc "Pode só falar. Eu sou seu amigo."

        s "Tá... É sobre isso mesmo que eu queria falar."

        s "Lá no Canto Tadaima eu... eu falei um monte de coisas estranhas. Me desculpa."

        mc preocupado "Não precisa pedir desculpas. Eu fiquei feliz de você ter desabafado comigo."

        s "..."

        s "Eu realmente tive confiança que você era um cara legal... Faz tempo que eu não sentia isso."

        s "Você ficou do meu lado e me ouviu, mesmo com minha irmã [g] tentando atrapalhar."

        s "Obrigada."

        mc normal "Não precisa se desculpar e nem agradecer. Eu só fiz o que eu quis, ok?"

        s "Ok..."

        s "Eu..."

    elif sayuri_e2 == "fracasso":

        s "Sabe no Canto Tadaima?"

        mc preocupado "Sei..."

        s "Eu... acho que a gente não começou com o pé direito."

        s "Minha irmã [g] queria te afastar de mim e ela tava atrapalhando nossa conversa."

        "Espero que ela não saiba nada do que eu e a [g] fizemos..."

        menu:
            "Desculpa se eu não dei o máximo de atenção pra nossa conversa.":


                $ sayuri_amizade += 1

                mc "Eu sei. Me desculpa também por não ter dado o máximo de atenção pro nosso encontro."

                s "Tu-tudo bem. Não precisa se desculpar."
            "Ela realmente estragou tudo. É culpa dela.":


                mc serio "Tem razão. Foi tudo culpa da [g] querendo separar a gente."

                s "É... é... Eu entendi... mas no fundo a [g] é uma pessoa boa."

                s "Independente disso..."

        s "Você foi o primeiro cara em muito tempo que conversou comigo por tanto tempo desse jeito."

        mc normal "Que bom que você ainda quer falar comigo."

        s "Sim! Eu... eu queria que a gente tentasse outra vez."

        mc "Com certeza!"

        s "Então... se você também acha legal..."

    s "E-eu queria te chamar pra fazer uma coisa."

    mc desconfiado "Certo..."

    s "É que... eu vou participar de um evento. Uma premiação para esportistas..."

    s "Eu vou... receber um prêmio... não sei direito..."

    s "E eu preciso escolher... uma roupa... de... gala..."

    s "Só que... eu não tenho coragem..."

    s "..."

    "Uma coisa que seria tão simples pra maioria das pessoas parece um inferno na vida dela."

    "Parece que tudo o que ela faz ela tem medo. Deve ser muito difícil viver assim..."

    menu:
        "É só um evento. Não faça disso o fim do mundo.":


            mc normal "É só um evento. Não é nada de mais. Não precisa fazer disso o fim do mundo."

            s "Ah..."

            mc "Eu tenho certeza que vai dar tudo certo."

            s "T-tá..."
        "Parabéns. Você merece pelo seu esforço como atleta.":


            $ sayuri_amizade += 2

            mc feliz "Fico muito feliz em ouvir que você vai receber um prêmio. Você merece."

            s "O-obrigada, [mc]."

            s "Não é nada tão grande. Mas os atletas medalhistas olímpicos do país vão receber uma homenagem."

            mc normal "Parece realmente legal."
        "Você vai ficar incrível com roupa de gala...":


            $ sayuri_amizade += 1

            mc safado "Você vai ficar incrível usando um traje de gala. Tenho certeza."

            s "E-e-eu... não sei..."

            mc charmoso "Não precisa ficar preocupada. Tenho certeza que você vai se sair tão bem quanto os outros atletas."

            s "Verdade?"

            mc "Sim."

            s "T-tá..."

    mc normal "Olha. O que você precisar de mim, vou estar aqui."

    s "Tá. Obrigada, [mc]. Acho que tô mais calma agora."

    mc "Que bom."

    s "É..."

    s "..."

    mc normal "Que foi?"

    s "Nã-não é nada. Até outra hora."

    mc "Até, [s]."

    "..."

    "Parecia que ela queria me falar alguma coisa antes de desligar..."

    "Bom... espero que eu tenha realmente ajudado ela a ter..."

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Meu celular de novo. A [s] deve ter esquecido de..."

    if tempo < 3:

        scene mapa cidade with hpunch
    else:


        scene mapa cidade_noite with hpunch

    g emburrada "Você é idiota?!"

    mc desconfiado "Quê?! Pera! É você, [g]?"

    g "Quem mais?!"

    mc zerado "Por que tá gritando comigo?"

    g "Você é burro?!"

    mc "..."

    g "A [s] não vai conseguir escolher a roupa pro evento! Você precisa ajudar ela!"

    mc preocupado "Mas..."

    g "Eu odeio ter que admitir isso! Quero você o mais longe dela possível!"

    g "Só que não vou conseguir sozinha. Você vai ter que ir junto!"

    mc "Tudo bem, mas..."

    g "Pega um ônibus agora e vem aqui pro centro. No Calçadão tem uma loja chamada Boutique Hinata."

    g "Você tem uma hora!"

    "{i}TCHACK{/i}"

    "{i}Tu... tu... tu...{/i}"

    "A [g] é extremamente desagradável às vezes..."

    mc zerado "Ela é tão diferente da [s]..."

    "Não adianta eu ficar aqui à toa. Se eu quero evoluir minha relação com elas preciso ir pra lá."

    if carro:

        play sound som_carro

        scene black with dissolve

        scene carro_mc_cidade1 with Dissolve(1.0)

        pause

        scene black with dissolve
    else:


        "Tenho que pegar o ônibus até o Calçadão..."

        $ tempo += 1

        scene black with Dissolve(2.0)

        play sound "audio/som_14_onibus.mp3"

        $ renpy.pause(delay=5, hard=True)

        "..."

        "Demora uns 30 minutos pra chegar até o Calçadão."

        "Morar em uma ilha paradisíaca é massa, só que ter que pegar esse busão toda vez pra chegar ao centro da cidade é bem chato..."

        "{b}30 minutos depois{/b}"

    play sound "audio/som_11_cidadedia_2.mp3"

    "Agora é encontrar a loja..."

    "Hinata... Boutique..."

    "Aqui!"

    "Acho que já vou entrar..."

    scene boutique geral with Dissolve(3.0)

    "Lugar de gente rica... Será que elas são bem de vida?"

    "Epa! A [s] tá ali conversando com a atendente."

    scene boutique caixa with Dissolve(3.0)

    show atendente normal with dissolve

    "Atendente" "Você é a [sc], né?"

    show atendente normal at direita with move

    show sayuri incerta with dissolve

    show sayuri incerta at esquerda with move

    s "Si-sim. Muito prazer."

    "Atendente" "Fiquei sabendo que amanhã vai ter uma super festa aqui na capital pra vocês atletas."

    s "Não é nada muito..."

    "Atendente" "Deve ser muito bom poder andar nesses lugares cheio de gente chique, comida cara, coisa rica..."

    show sayuri assustada with dissolve

    s "A-ah... Nã-não..."

    "Parece que ela tá prestes a ter um ataque de pânico..."

    "E por que a [g] não tá aqui com ela?"

    "E agora? Será que eu interrompo?"

    menu:
        "Se intrometer na conversa":


            $ sayuri_amizade += 1

            "Não posso deixar ela ficar mais nervosa do que ela já tá."

            "..."

            mc normal "Olá, garotas."

            s "[mc]!"

            mc "Oi, [s]. Tudo bem?"

            s "O o o que você está fazendo aqui?"

            mc "Eu tava fazendo compras e vi você aqui dentro."

            "Atendente" "Vocês são amigos?"

            if sayuri_e2 == "amizade":

                $ sayuri_amizade += 1

                show sayuri incerta with dissolve

                s "Si-sim..."
            else:


                show sayuri pensando with dissolve

                s "..."

                menu:
                    "Ainda não somos amigos, mas vamos chegar lá.":


                        $ sayuri_amizade += 1

                        mc normal "Somos conhecidos. Não chegamos na amizade ainda, né?"

                        mc "Mas com certeza vamos virar bons amigos."

                        show sayuri incerta with dissolve

                        s "Acho que sim..."
                    "A gente é mais do que amigos, se é que me entende...":


                        mc tarado "A gente é mais que amigos. Dá pra entender o que eu tô falando?"

                        show sayuri assustada with dissolve

                        s "Q-quê?!"

                        "Atendente" "..."

            "Atendente" "Ok. Eu tava falando pra ela que..."

            mc charmoso "Não se preocupe que está tudo ok. A [s] vai pegar uma roupa linda hoje e vai ser super tranquilo. Né?"

            show sayuri incerta with dissolve

            s "Tomara que sim."

            mc feliz "Claro que vai."

            mc normal "Vamos ali?"

            s "Ok."

            "..."
        "Deixar ela se virar sozinha":


            "A [s] já é grande. Talvez ela acabe ganhando mais experiência assim."

            s "E-eu não sei..."

            "Atendente" "Como não sabe? Essas festanças são o sonho de qualquer um. O glamour, a nobreza... Você não tá acostumada?"

            s "Nobreza? Glamour?"

            "Atendente" "Claro! É tudo tão chique... Tão diferenciado..."

            s "Diferenciado..."

            show sayuri zonza with dissolve

            s "Eu..."

            s "Ah... aah..."

            "Atendente" "Ei! [s]! Você tá bem?!"

            s "Eu..."

            "Atendente" "Vou chamar um médico!"

            "Meu Deus! O que eu tava na cabeça!"

            mc surpreso "[s]! Pode deixar que eu cuido dela."

            s "[mc]..."

            s "Eu estou um pouco tonta..."

            mc preocupado "Não se preocupe. Vamos ali sentar e ela vai ficar bem."

            "Atendente" "Certeza?"

            mc "Sim. Pode deixar comigo."

            mc preocupado "Vai ficar tudo legal, [s]..."

            s "O que... você está fazendo aqui?"

            mc "Eu tava fazendo compras no Calçadão e vi você aqui na loja. Daí vim dar um alô."

            s "... Que bom... Parece que você veio só pra me salvar."

            menu:
                "É pra isso que servem os amigos.":


                    $ sayuri_amizade += 1

                    mc normal "É pra isso que servem os amigos, né?"

                    if sayuri_e2 == "amizade":

                        s "Si-sim..."
                    else:


                        s "..."
                "Não posso deixar uma donzela em perigo.":


                    mc charmoso "Não posso deixar uma donzela em perigo sozinha."

                    s "..."

                    mc preocupado "Tá tudo legal..."

            mc preocupado "Vamos ali sentar..."

            s "Ok..."

    scene boutique geral with Dissolve(1.0)

    show sayuri envergonhada with dissolve

    s "Acho que estou me sentindo melhor. Obrigada por me salvar."

    mc normal "Não esquente."

    mc "Então você veio mesmo comprar sua roupa de gala?"

    s "Si-sim... mas..."

    s "Tudo parece tão estranho, [mc]. Eu não te falei no telefone, mas eu ia te chamar pra vir aqui."

    mc desconfiado "Sério?"

    s "Sim. E agora você está aqui. Chegou quase junto comigo, como se Deus tivesse te mandado..."

    menu:
        "Realmente, eu recebi uma mensagem de Deus.":


            mc normal "Hehe... Tenho que te falar a verdade. Foi realmente Deus que me falou pra vir te salvar."

            s "Não brinque comigo..."

            mc envergonhado "..."

            menu:
                "Foi só coincidência.":


                    mc envergonhado "Foi só coincidência mesmo. E que bom que eu resolvi fazer compras hoje."

                    s "Eu... gostei também..."

                    mc normal "Nunca imaginei que ia encontrar você bem nesta loja."

                    s "Foi bem surpreendente mesmo. Eu tomei um belo susto..."

                    mc feliz "..."
                "Foi a [g] que falou que você estaria aqui.":


                    jump sayuri_e3_julia
        "Na verdade não foi Deus. Foi a [g].":


            label sayuri_e3_julia:

                $ sayuri_amizade += 1

                mc envergonhado "Na verdade foi a [g] que me ligou e disse que você estaria aqui. Não é Deus..."

                show sayuri incerta with dissolve

                s "A [g] é impossível... Obrigada por me contar."

                mc normal "Ela parece gostar muito de você."

                if julia_conversou:

                    $ sayuri_amizade += 1

                    mc desculpa "Quando eu tava acompanhando ela até a universidade ela me contou que teve alguns problemas de relacionamento."

                    mc "Ela disse que você foi a única que ficou do lado dela."

                    show sayuri assustada with dissolve

                    s "A [g] te contou tudo isso?!"

                    mc desconfiado "Sim. Por que o espanto?"

                    s "É que... que..."

                    show sayuri pensando with dissolve

                    s "Eu acho que ela nunca contou nada disso pra ninguém..."

                    s "Se ela falou essas coisas com você é porque ela deve confiar em você."

                    mc envergonhado "Não sei se é pra tanto..."

                    s "Eu..."

                    show sayuri incerta with dissolve

                    s "[mc], eu fico muito feliz de você ter conversado com ela."

                    s "A [g] é uma garota problemática, mas ela tem um bom coração. Muito obrigada."

                    mc desculpa "Não precisa agradecer. Foi só uma conversa."

                    mc preocupado "Mas e sobre sua roupa?"
                else:


                    s "Sim. Ela tem uma relação um pouco complicada comigo."

                    s "Você viu lá no Tadaima, né?"

                    mc envergonhado "Pois é..."

                    s "Mas ela é uma garota especial. Ela teve alguns problemas no passado e por isso ela é assim."

                    s "Mas se você tiver uma chance de passar um tempo com ela de novo tente conversar com ela."

                    mc desconfiado "Conversar?"

                    s "Sim! Tente ignorar um pouco esse jeito... como posso falar... agressivo..."

                    s "Se você conseguir não cair nessa fachada dela, tenho certeza que você vai encontrar alguém muito especial."

                    s "Uma verdadeira amiga muito diferente dessa criatura superficial que ela aparenta ser."

                    mc normal "Ok. Vou tentar."

                    "Não sei como... A menina só pensa em safadeza. Talvez eu devesse ir com mais calma com ela..."

                    mc preocupado "Mas e sobre sua roupa?"

    show sayuri pensando with dissolve

    s "Então... Agora vou ter que escolher uma roupa..."

    s "..."

    show sayuri zonza with dissolve

    s "Eu fico nervosa só de pensar..."

    mc preocupado "Cuidado. Você ainda tá fraca. Sente aqui."

    s "O-ok..."

    hide sayuri with dissolve

    mc normal "Melhor assim, né?"

    s "Si-sim... Obrigada. Mas e você?"

    mc "Eu sento aqui no chão mesmo."

    s "Mas..."

    scene sayuri boutique_sentados with Dissolve(2.0)

    mc "Viu? Não tem problema nenhum..."

    s "Você faz cada uma, [mc]..."

    if julia_conversou:

        mc "Vai me chamar de esquisito igual a [g]?"

        s "Mas você é... um pouco..."

        mc "Ei..."

    s "E sobre esse evento? Eu..."

    s "O... o que eu faço?"

    "Como eu vou saber uma coisa dessas? Eu só uso a mesma roupa amassada todos os dias."

    "Droga... Não posso falar isso pra ela. Se eu quiser ajudar ela e ganhar alguns pontos no processo vou ter que me esforçar."

    "Vou precisar criar uma linha de raciocínio que convença ela a pelo menos experimentar a roupa."

    s "[mc]?"

    mc "Desculpa. Eu tava pensando como seria a melhor forma de você escapar dessa enrascada."



    s "Enrascada?!"

    "Droga! Tenho que tomar cuidado com as palavras que eu uso."

    mc "É só um modo de falar. Porque isso deixa você nervosa, entende?"



    s "Si-sim..."

    mc "Olha..."

    menu:
        "Já falei pra você não se preocupar com isso.":


            mc "Já falei pra você não se preocupar demais com isso."

            mc "Você só vai ser mais uma atleta no meio de outros. Não tem motivo pra pânico."

            s "..."
        "Por que isso te deixa tão assustada?":


            $ sayuri_amizade += 1

            mc "Por que isso te deixa tão nervosa?"

            s "Eu..."

    s "Eu sei que eu não estou agindo como a maioria das pessoas."

    s "Minha reação não é normal, eu sei disso."

    s "Só que..."

    s "..."

    mc "Por favor, confie em mim, [s]. Pode falar."

    s "..."

    s "É que..."

    s "A ginástica é tudo pra mim. Ser ginasta é a única coisa que me restou na vida."

    s "É por causa da ginástica que as pessoas gostam de mim, que elas me ouvem e me dão atenção."

    s "A [g] é a única que me escuta. Só que... só ela não é suficiente."

    s "Eu quero que as pessoas me respeitem e tenham orgulho de mim."

    mc "Mas as pessoas têm orgulho de você. Você é uma atleta reconhecida nacionalmente, muldialmente!"

    s "Exatamente! E tudo isso por causa da ginástica."

    s "Sem a ginástica eu não sou nada... não tenho ninguém..."

    s "Meus pais me amam por causa da ginástica e todas as outras pessoas também."

    menu:
        "Mas isso é normal. As pessoas se inspiram no que fazemos de bom.":


            mc "Isso não é só com você. É o que a gente faz de especial que inspira as pessoas."

            s "Esse é o problema, [mc]."

            s "Se as pessoas só ligam pra você por causa de uma coisa..."
        "Não é a ginástica que me fez gostar de você.":


            $ sayuri_amizade += 1

            mc "Não foi a ginástica que fez eu querer te conhecer melhor. Não é por causa dela que eu tô aqui."

            s "Você está mentindo..."

            mc "Não tô! Eu me aproximei de você por causa da ginástica, pra pegar uma matéria pra revista."

            mc "Mas não tô aqui agora por causa dela. Estou aqui porque eu gosto de você."

            s "..."

            s "Não acredito. Me desculpa, [mc]. Mas não consigo acreditar!"

    s "Se eu perder a ginástica você e todos os outros vão se afastar de mim..."

    s "É por isso... é por isso que não consigo... não consigo escolher a merda dessa roupa idiota..."

    s "Se eu fracassar nisso, posso perder tudo..."

    mc "[s]..."







    s "..."

    "É por isso que ela tá tão nervosa. É como se ela fosse perder tudo se ela não escolher a roupa certa."

    "Eu preciso fazer alguma coisa. Preciso dar uma outra perspectiva pra ela."

    "Não adianta só dizer que eu vou estar ao lado dela."

    "Ela precisa acreditar que os outros vão continuar amando ela mesmo sem a ginástica."

    "Pra convencer ela disso, não posso enrolar demais. Preciso falar a coisa certa, mas sem parecer uma aula."

    "Tenho que escolher minhas palavras o mais rápido possível para que pareça natural."

    "Também tenho que tomar cuidado pra não falar nenhuma palavra que deixe ela assustada."

    "E principalmente minha argumentação precisa provar o ponto que eu quero fazer."

    "Preciso levar em conta o que eu sei sobre ela. Isso é muito importante."

    "Certo. Acho que tô pronto pra falar com ela."

    mc "[s]."

    s "Oi..."

    mc "Vem aqui. Levanta."

    s "T-tá..."

    "..."

    label sayuri_e3_minigame:

        scene sayuri cena_convencer with Dissolve(2.0)

        $ s3_mini = 0

        $ timeout_label = "sayuri_e3_minigame_fail"
        $ timeout = 12.0

        mc "Eu tenho uma coisa muito importante pra falar pra você. Presta atenção."

        s "O-ok..."

        "Certo. Preciso convencer a [s] a escolher uma roupa e participar da homenagem."

        "Com qual entonação eu devo falar com ela?"

        menu:
            "Séria":


                mc serio "..."
            "Feliz":


                $ s3_mini += 1

                mc normal "..."
            "Confiante":


                $ s3_mini += 1

                mc charmoso "..."
            "Preocupado":


                mc preocupado "..."

        "Concentração... Vamos lá!"

    menu:
        "Eu tenho a solução pro seu problemão.":


            mc "Eu sei como resolver esse problemão que você se meteu."

            s "Pro-problemão?"

            mc "..."
        "Eu pensei muito sobre essa questão da roupa.":


            $ s3_mini += 1

            mc "Eu pensei muito sobre essa questão da roupa, e acho que sei como te ajudar."
        "Eu não sei muito bem como te ajudar.":


            mc "Essa questão de roupa não é meu forte e eu não sei muito bem como te ajudar."
        "Se eu fosse você...":


            $ s3_mini += 1

            "Eu entendo que isso não é fácil, e se eu fosse você eu faria o seguinte."

    menu:
        "Infelizmente o ser humano é uma criatura egoísta.":


            $ s3_mini += 1

            mc "Infelizmente o ser humano é egoísta. Ele sempre pensa primeiro nele."

            mc "Todos nós temos um pouco de egoísmo dentro da gente. Isso faz parte."

            mc "Por isso a gente precisa entender os erros dos outros e os nossos também."
        "Você precisa ignorar todas as pessoas.":


            mc "Não adianta tentar ficar buscando amor e aceitação. Você é a única que importa."

            mc "Apenas ignore os outros e viva do jeito que você quiser."
        "Só se preocupe com as pessoas que te amam de verdade.":


            mc "As únicas pessoas que importam são as que nos amam de verdade."

            mc "Nós conseguimos ver claramente quando alguém ama a gente."

            mc "Apenas ignore o resto das pessoas."
        "Não é o que os outros pensam da gente que importa.":


            $ s3_mini += 1

            mc "Todos nós buscamos aceitação. E isso faz parte de viver com os outros."

            mc "Mas não é o que os outros pensam da gente que realmente importa."

            mc "Nós precisamos ter uma opinião própria sobre nosso valor."

    menu:
        "Você é especial por vários motivos.":


            $ s3_mini += 1

            mc "Eu sei que a ginástica é sua principal conquista, mas não é a única."

            mc "Você é uma pessoa de bom coração, e uma excelente companhia. E isso também conta."
        "Você vai ser a melhor ginasta para sempre.":


            mc "Eu tenho certeza que você vai conseguir ser uma ginasta profissional pra sempre."

            mc "E depois você pode virar técnica. Assim você sempre será amada. Não se preocupe."
        "Nós criamos pensamentos falsos pra justificar nossos medos.":


            $ s3_mini += 1

            mc "Às vezes a gente tem medo de encarar a realidade, e daí vamos criando medos falsos pra nos proteger."

            mc "Muitos anos se passaram. Como você sabe que as pessoas não vão te amar?"

            mc "Hoje você é uma mulher incrível e as coisas podem ser diferentes."
        "A roupa que você usa não importa pra essa gente.":


            mc "Seu desempenho como atleta que importa. Foda-se a roupa que você usa."

            mc "Eles não tão nem aí pra isso e se eu fosse você nem iria nessa festa."

            mc "Você é uma atleta olímpica, é nas competições que você precisa vencer."

    menu:
        "Se esforçe cada vez mais para que continuem te amando.":


            mc "Se você continuar se esforçando, você vai sempre vencer e as pessoas vão te amar."

            mc "Eu tenho certeza que você vai conseguir superar tudo e todos."
        "Acredite em você e dê uma nova chance para as pessoas.":


            $ s3_mini += 1

            mc "Quando a gente se ama, nós temos mais coragem de sermos nós mesmos."

            mc "E aparecem pessoas que pensam como a gente em nossa vida."

            mc "Tenha mais confiança em você e pessoas que se identificam com você vão aparecer, como eu apareci."
        "Não é quantidade de pessoas que nos amam que importa.":


            $ s3_mini += 1

            mc "E mesmo que no fim seu pior medo aconteça, você tem pelo menos a [g] que se importa com você de verdade."

            mc "E você vai ver que eu também gosto da sua companhia e não da sua fama ou das suas habilidades na ginástica."

            mc "Como a gente, outros amigos verdadeiros vão aparecer."

            mc "Não é a quantidade que importa, mas o verdadeiro carinho que vale."
        "Você pode viver sozinha pra sempre. Você tem essa força.":


            mc "E mesmo que tudo dê errado, você não precisa de ninguém. Viva sozinha pra sempre."

            mc "Confie no seu poder próprio e ignore as pessoas."

            mc "Você só precisa de você pra ser feliz."

    menu:

        "{b}Então confie em mim e vamos superar isso juntos.{/b}" if s3_mini >= 3:

            scene sayuri cena_convencer

            $ timeout_label = None

            mc "Então confie em mim e vamos superar isso juntos. Por mais difícil que seja, vamos conseguir."

            $ renpy.notify("Sayuri está ponderando suas palavras...")

            s "[mc]..."

            s "Você... Isso..."

            mc "..."

            s "..."

            s "Eu..."

            $ renpy.notify("Sayuri está se sentindo confiante.")

            s "Eu confio em você. Não custa nada te-tentar, certo?"

            mc "É assim que se fala."

            s "Muito obrigada... por segurar minha mão e... não rir do meu problema bobo."

            mc "Seu problema não é bobo. E o importante é que você resolveu tentar."

            s "Sim..."

            jump sayuri_e3_continua
        "Por isso você deve superar esse medo e participar do evento.":


            mc normal "Por isso você tem que superar essa coisa ruim que você tá sentindo e participar do evento."

            $ renpy.notify("Sayuri está ponderando suas palavras...")

            label sayuri_e3_minigame_fail:

                $ timeout_label = None

                s "..."

                s "Eu..."

                s "Eu não posso, [mc]."

                $ renpy.notify("Sayuri não se sente confiante o suficiente.")

                mc triste "..."

                s "Eu agradeço todo seu esforço em querer me ajudar, mas não consigo. Me perdoe."

                mc preocupado "Não precisa se desculpar, [s]..."

                "Droga... Não consegui convencer ela..."

                "E agora?"

                scene black with Dissolve(1.0)

                p lecionando "Ixi. Ajudar a [s] a participar do evento é muito importante pra você progredir com ela."

                p "Você deseja usar meu poder para voltar no tempo e tentar novamente?"

                menu:
                    "Sim.":


                        p rindo "Sábia escolha. Boa sorte!"

                        jump sayuri_e3_minigame
                    "Não. Quero continuar dessa forma.":


                        p lecionando "Tem certeza? Você perderá cenas importantes deste encontro."

                        menu:
                            "Tenho certeza.":


                                p rindo "Opa! Às suas ordens, capitão!"

                                jump sayuri_e3_badending
                            "Pensando melhor, vou tentar mais uma vez.":


                                p rindo "Sábia escolha. Boa sorte!"

                                jump sayuri_e3_minigame

    label sayuri_e3_badending:

        scene sayuri cena_convencer with Dissolve(1.0)

        $ sayuri_e3 = "horrivel"

        s "Eu vou só esquecer esse evento. Obrigado por tentar, [mc]."

        s "Mas eu tenho muito medo."

        mc triste "..."

        mc desculpa "Me desculpa por não conseguir ajudar mais."

        s "Não fale uma coisa dessas. Você foi muito atencioso vindo até aqui e falando comigo."

        mc "..."

        s "A gente... vai se ver de novo."

        mc preocupado "Com certeza."

        s "Até mais, [mc]."

        mc "Até, [s]. Fica bem."

        "..."

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("sayuri_e3_horrivel","fim","local")

        jump call_cidade

    label sayuri_e3_continua:

        mc "E agora? Vamos escolher uma roupa?"

        scene boutique geral with Dissolve(1.0)

        show sayuri incerta with dissolve

        s "Na verdade eu já tenho uma roupa em mente."

        mc normal "Sério?"

        s "Sim... Eu já tô de olho nela faz um tempo, mas nunca tive coragem de comprar."

        s "É diferente de tudo o que eu uso..."

        mc "Posso ver?"

        show sayuri assustada with dissolve

        s "Nã-não!"

        s "Quer dizer..."

        show sayuri incerta with dissolve

        s "Quero que você veja... eu usando ela..."

        "Uou! Não sei porque, mas isso soou meio sexy."

        mc charmoso "Ok."

        s "Quando eu estiver pronta eu te chamo."

        mc "Certo. Vou tá aqui esperando."

        s "Tá. Já te chamo."

        hide sayuri with dissolve

        "..."

        "As coisas estão progredindo muito bem com a [s]. Nem acredito que consegui convencer ela."

        "Eu sinto que estou me aproximando cada vez mais dela. A questão agora é se ela confia em mim o suficiente..."

        "E eu também tenho que decidir quais serão minhas intenções com ela. Isso é muito 'muito' importante."

        "A [s] é uma garota introvertida, mas muito doce e especial."

        "Pelo que eu entendi, ela não procura um amor, mas se eu conquistar ela..."

        "Certo. Tenho que decidir agora."

        label sayuri_e3_intencoes:

            "Quais serão minhas intenções com a [s]?"

            menu:
                "Quero ser um amigo.":


                    "Esta é uma decisão muito importante e vai influenciar como eu vou tratar ela daqui pra frente."

                    "Será que eu quero ser apenas um amigo mesmo?"

                    menu:
                        "Sim. É isso que eu quero.":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("s3_escolheu_amizade","sayuri","personagem")

                            $ sayuri_intencao = "amizade"

                            "Estou decidido. Quero ela como minha amiga."
                        "Não. Vou pensar melhor.":


                            jump sayuri_e3_intencoes
                "Quero ser {b}mais{/b} que um amigo.":


                    "Esta é uma decisão muito importante e vai influenciar como eu vou tratar ela daqui pra frente."

                    "Será que eu realmente quero ser mais do que um amigo e aprofundar nossa relação?"

                    menu:
                        "Sim. É isso que eu quero.":


                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("s3_escolheu_namoro","sayuri","personagem")

                            $ sayuri_intencao = "namoro"

                            "Estou decidido. Quero aprofundar nossa relação."
                        "Não. Vou pensar melhor.":


                            jump sayuri_e3_intencoes

    "..."

    "Ela tá demorando... Espero que ela não tenha desistido. Deixa eu ver se tá tudo legal."

    "..."

    scene sayuri boutique_trocando with Dissolve(3.0)

    pause

    mc surpreso "..."

    "E-e-ela não fechou a porta completamente!"

    "Deve tá tão nervosa que nem percebeu..."

    "Ela tá parada olhando pro espelho. Isso tudo deve ser realmente difícil pra ela."

    "Meu Deus... Eu não devia... mas tem algo me fazendo querer chegar mais perto e olhar ela inteira só de calcinha..."

    "Não, [mc]! Você está ganhando a confiança dela aos poucos. Se ela te pegar talvez nunca mais ela fale com você!"

    "E agora? O que eu faço?!"

    menu:
        "Tentar espiar sem ser visto":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("se3_pelada","sayuri","personagem")

            $ se3_pelada = True

            "Não aguento!"

            "Preciso dar uma olhada. Se eu for bem devagarzinho..."

            "..."

            scene black with Dissolve(1.0)

            scene sayuri trocando_close with Dissolve(2.0)



            "..."

            "Isso... bem devagar..."

            "Cristo! Ela tá fazendo poses pro espelho."

            "Olha isso... Ela pode não ter muito peito, mas esse traseiro...."

            "O corpo dela é perfeito!"

            "Claro. Ela é uma atleta. O corpo dela é demais."

            label say3_premium2:

                pass

            menu:
                "Continuar olhando":








                    "Eu preciso ver mais um pouco..."

                    scene black with dissolve

                    scene sayuri_boutique1 with Dissolve(1.0)

                    pause

                    "Olha pra essa bunda! Que perfeição..."

                    "E tem gente que fala que oriental é tábua..."

                    "Será que foi a vida de ginasta que fiz isso com ela? Abençoadas sejam as Olimpíadas..."

                    window hide

                    pause

                    scene sayuri_boutique2 with Dissolve(1.0)

                    pause

                    "U-uou! Ela tirou tudo..."
                    scene snew_ani17 with Dissolve(1.0)
                    "Parece que ela tá curtindo bastante esse lance de posar pro espelho..."

                    "E ela nem percebeu que tem uma frestinha na porta do trocador... que sorte..."

                    window hide

                    pause

                    scene sayuri_boutique3 with Dissolve(1.0)

                    pause

                    "Parece que ela tá um pouco incomodada com os peitos... Será que ela acha eles pequenos?"

                    "Se ela soubesse que ela é perfeita assim..."

                    "Às vezes os filmes e talz deixam a gente inseguro que o peito tem que ser imenso, mas isso é mentira."

                    "A [s] não precisa de peitos. Ela é gostosa desse jeito."

                    "Se eu pudesse pegar nessa bunda dela... ah... [s]..."
                "Melhor eu sair daqui enqu-":


                    pass

            "Só de pensar nela e eu faze-"

            scene sayuri_boutique4 with vpunch

            s "[mc]!"



            mc "Ah!"



            s "O que você tá fazendo?!"

            mc surpreso "E-eu..."

            s "Você tava me espionando!?"

            menu:
                "Claro que não! Só vim ver se você precisava de ajuda.":


                    $ sayuri_amizade -= 3

                    mc preocupado "Claro que não, [s]. É que você tava demorando e eu vim ver se você precisava de algo."

                    s "Mas você tava agachado olhando pela fresta!"

                    mc "E-eu... Escorreguei..."

                    s "E ainda por cima tá inventando desculpas sem noção?!"

                    mc triste "Não... Eu..."

                    s "Eu tô começando a confiar em você e você dá uma dessas?"

                    mc desculpa "Desculpa. Eu não aguentei... Foi mais forte do que eu..."

                    s "Isso não se faz, [mc]. É muito desrespeito!"

                    mc "Eu sei... Malz..."

                    s "Se você pelo menos tivesse dito a verdade, seria menos ruim."

                    mc "..."
                "Sim. Eu não resisti. Me desculpa...":


                    $ sayuri_amizade -= 2

                    mc desculpa "Sim... Eu tentei não olhar, mas foi mais forte do que eu. Me desculpa, [s]."

                    s "Isso é muito desrespeitoso, [mc]. Justo agora que eu tava começando a confiar em você..."

                    mc "Por favor, foi só um deslize. Você sabe que eu quero que confie em mim."

                    s "Eu sei... Mas é que isso é muito grave."

                    mc "Malz..."

                    s "Pelo menos você me contou a verdade. Isso pelo menos é um ponto positivo."

                    mc "Sim. Não quero que pense que sou um mentiroso."

                    s "Pelo menos isso..."
                "Como você pode pensar uma coisa dessas de mim?!":


                    $ sayuri_amizade -= 4

                    mc serio "Claro que não! Como você pode pensar algo assim de mim?"

                    s "Que?! Como assim?! Você tava agachado olhando pela fresta!"

                    mc "Sim, mas não tava olhando pra você. Eu tinha escorregado."

                    s "Você acha que eu sou idiota, [mc]?!"

                    s "Ainda por cima quer colocar a culpa em mim?!"

                    mc "E-eu..."

                    s "Isso é golpe baixo!"

                    mc desculpa "..."

                    mc "Você tem razão... Me desculpa. Mas eu não queria olhar, eu juro."

                    mc "A porta tava aberta e eu só queria te avisar."

                    s "Não acredito em você."

                    s "Se você pelo menos admitisse e me falasse a verdade."

                    s "Isso é muito desrespeitoso, [mc]. Justo agora que eu tava começando a confiar em você..."

                    mc "Não quero que isso atrapalhe nossa relação."

                    s "Eu acho isso algo muito sério. Mas não quer dizer que não vou mais falar com você."

                    mc "Ok. Obrigado."

                    s "..."

            s "Agora espera aqui que eu vou terminar e já te chamo."

            mc "Ok..."



            scene boutique trocador with Dissolve(1.0)

            "Caraca... Ela ficou muito brava. Também, olha a merda que eu fui fazer."

            "Não podia só ter esperado ela?! Maldita cabeça de baixo..."

            "Espero que isso não dificulte demais eu conquistar a confiança dela."
        "Esperar ela do lado de fora":


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("se3_pelada_nao","sayuri","personagem")

            "Preciso me conter. Não adianta jogar tudo pelos ares agora que eu tô progredindo tão bem com ela."

            "Seria uma falta de respeito com ela tentar se aproveitar dela assim."

            "Vou só me afastar, ficar em um ângulo que eu não possa ver ela e esperar."

            scene boutique trocador with Dissolve(3.0)

            "Aqui é melhor. Mesmo com a porta aberta não consigo ver nada."

            "Assim não coloco nossa relação em risco."

            "Além disso, eu sou um cavalheiro. Se eu for ver ela pelada, vai ser quando eu fizer ela querer ficar pelada pra mim."

            "Não sou um cachorro no cio."

            "..."

    scene black with Dissolve(1.0)

    "{b}Alguns minutos depois{/b}"

    scene boutique trocador with Dissolve(1.0)

    s "Estou pronta! Mas não sei se eu quero que você veja!"

    mc charmoso "Depois de tudo é o mínimo que eu mereço, não acha?"

    s "..."

    s "Tá certo. Você tem razão..."

    s "Mas... e se você rir de mim e me achar uma tonta? Não combina comigo!"

    mc "Eu tenho certeza que você vai estar linda."

    s "Ai..."

    s "Tá. Vou fazer rápido antes que eu perca a coragem."

    s "3... 2... 1..."

    scene sayuri trocando_final with Dissolve(3.0)

    pause

    mc surpreso "..."

    s "O que você achou? Fala alguma coisa..."

    mc "Achei demais..."

    s "Chique demais?"

    mc charmoso "Nã-não! Ficou perfeita em você."

    s "Sé-sério?"

    mc normal "Claro! Ele marca muito bem seu corpo. Ficou excelente e não é exagerado."

    s "Ele não é um vestido de gala, mas eu achei ele bem estiloso..."

    mc "Eu tenho certeza que vai fazer muito sucesso."

    s "Mu-muito obrigada, [mc]."

    mc "..."

    s "Eu... acho que vou conseguir ir lá no evento amanhã."

    mc surpreso "Sério?!"

    s "Você acha que eu não devo?"

    mc feliz "Claro que deve. Só estou feliz por você."

    s "..."

    s "Eu vou me trocar e já saio."

    mc normal "Ok."

    "..."

    scene boutique trocador with Dissolve(1.0)

    "..."

    show sayuri incerta with dissolve

    s "Ufa, pronto. Nem acredito que vou levar..."

    mc charmoso "Você foi muito bem hoje."

    s "[mc]... Você sabe que eu não teria conseguido sem você."

    mc "Você foi muito corajosa, isso sim."

    show sayuri pensando with dissolve

    s "..."

    mc desconfiado "Que foi?"

    s "Eu estava pensando..."

    $ renpy.notify("Sayuri está avaliando suas ações durante o encontro...")

    s "Por que você fez tudo isso por mim? A gente se conhece há tão pouco tempo."

    "Essa é a hora que eu tava esperando."

    if sayuri_intencao == "namoro":

        "Eu decidi que quero aprofundar nossa relação e é isso que eu vou fazer."

        "Preciso ser confiante e deixar claro minhas intenções."

        mc charmoso "Você é uma garota especial pra mim."

        s "Co-como assim?"

        mc "Eu quero que você tenha confiança em mim, porque eu não quero ser só seu amigo."

        show sayuri assustada with hpunch

        s "Q-q-q-quê?!"

        mc "Isso mesmo. Eu gosto da sua companhia e te acho linda. Não quero ser apenas um amigo. Quero mais do que isso."

        show sayuri desesperada with hpunch

        s "E-e-e-eu..."

        s "Aii..."

        mc charmoso "Não precisa ficar assim, [s]. Só estou sendo sincero com você."

        s "..."

        s "Eu..."

        s "[mc]..."

        mc "Você acha isso uma péssima ideia?"

        s "Eu não... eu..."

        mc "Me dá sua mão. Por que você não vem aqui comigo?"

        s "E-e-eu..."



        if sayuri_amizade >= 15:

            $ sayuri_e3 = "beijo"

            $ renpy.notify("Sayuri está sentindo uma mistura intensa de emoções")

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("sayuri_e3_namoro","sayuri","personagem")

            hide sayuri with dissolve

            mc "Vamos entrar aqui no trocador."

            s "..."

            scene black with Dissolve(1.0)

            mc "Segura minha mão igual aquela hora."

            s "Ai, [mc]... Eu não..."

            mc "Não precisa falar nada..."

            mc "Só fecha os olhos e confia em mim..."

            s "Aii..."

            "..."

            scene sayuri boutique_beijo with Dissolve(3.0)

            pause

            "..."

            "Não acredito que tô beijando a [s]."

            "Ela tá tremendo... E eu tô muito nervoso também."

            s "Hmmm..."

            mc "..."

            mc "Deixa eu te beijar mais?"

            s "Hmmmm..."

            scene sayuri boutique_beijo_dois with Dissolve(2.0)

            pause

            "São só uns selinhos, mas mesmo assim, fazer isso com a [s] é tão quente..."

            s "Aii..."

            window hide
            with dissolve

            pause

            scene boutique trocador with Dissolve(1.0)

            mc charmoso "..."

            mc charmoso "Eu adorei te beijar, [s]."

            show sayuri desesperada with dissolve

            s "Ah.. ahh..."

            mc "O que você achou? Foi bom?"

            s "Eu..."

            mc normal "..."

            s "E-eu preciso ir pra casa! Obrigada por tudo!"

            hide sayuri with moveoutleft

            mc surpreso "Ei! [s]!"

            "Caraca, ela saiu correndo."

            "Bom... melhor deixar ela ir. Talvez eu tenha avançado as coisas rápido demais."

            "Mas se não fosse assim talvez a gente nunca saísse do zero a zero."

            "Tudo que aconteceu foi massa demais. Fico ansioso pra saber até onde eu posso ir com ela."

            if priscila_e3_beijo or priscila_e3_sexo:

                "Só preciso tomar cuidado com o fato de que eu e a [c] temos um lance."

                "Pelo que eu conheço ela e a [s] nenhuma das duas gostaria de ter um relacionamento com um galinha."

                "Minha vida tá ficando enrolada..."

                mc tarado "Mas não dá pra reclamar..."

            jump sayuri_e3_final
        else:


            jump sayuri_e3_fracasso

    elif sayuri_intencao == "amizade":

        "Eu escolhi ser o melhor amigo dela. E agora é a hora de provar que eu sou um homem de verdade."

        mc normal "Você sabe porque eu fiz tudo isso."

        s "Hã?"

        mc "É porque você é minha amiga. De verdade."

        show sayuri assustada with dissolve

        s "A-amiga?"

        mc "Sim. E é isso que os amigos fazem."

        mc "A gente se preocupa com o bem-estar dos nossos amigos e quer que eles sejam felizes."

        mc "É só isso que eu quero. Que você seja feliz, [s]."

        show sayuri pensando with dissolve

        s "[mc]..."

        s "Você sabe o quanto... eu sou complicada..."

        s "Tem certeza que quer ser meu amigo?"

        mc serio "Certeza absoluta. Não falo isso brincando."

        mc normal "Eu quero você perto de mim e quero estar perto quando você precisar."

        s "..."

        mc "O que você acha disso? Quer ser minha amiga?"

        s "..."

        if sayuri_amizade >= 15:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("sayuri_e3_amizade","sayuri","personagem")

            $ sayuri_e3 = "amizade"

            show sayuri incerta with dissolve

            $ renpy.notify("Sayuri vê você como um verdadeiro amigo")

            s "E-eu adoraria..."

            mc feliz "..."

            s "Você é o rapaz mais legal que eu conheci na vida, [mc]."

            mc envergonhado "Não é pra tanto, [s]..."

            s "Eu falo sério. Você se preocupa comigo e me ajudou tanto hoje."

            s "Você tem paciência com meu jeito medroso. Não se irrita comigo."

            s "Eu sinto que não preciso fingir que está tudo bem quando estou com você."

            show sayuri sorrindo with Dissolve(1.0)

            s "Você realmente me faz feliz, [mc]."

            mc surpreso "!"

            s "Que foi?"

            mc normal "Acho que é a primeira vez que eu vejo você sorrindo desse jeito."

            show sayuri incerta with dissolve

            s "É-é..."

            mc "Durou pouco, mas foi bom ver você sorrindo de verdade."

            s "... Você tá me deixando sem jeito."

            mc "Amigos são pra isso também."

            s "..."

            s "Então se prepare que eu também vou fazer você passar vergonha algum dia."

            mc feliz "Ver a [s] fazendo piada? Vou poder morrer em paz daí."

            show sayuri sorrindo with dissolve

            s "Ei! Eu sei contar piadas muito boas!"

            mc envergonhado "Eu imagino que sim."

            s "Eu percebi sua ironia!"

            mc "..."

            s "E não faça essa ca..."

            "Smartphone" "{i}TRÓ LÓ LÓ! TRÓ LÓ LÓ!{/i}"

            show sayuri incerta with dissolve

            s "Desculpa. É o meu. Rapidinho."

            hide sayuri with dissolve

            s "Alô? [g]?"

            "Claro que tinha que ser a maldita bem agora..."

            s "QUÊ?! Ela já tá aí?!"

            s "Vou sair correndo! Em cinco minutos tô em casa!"

            s "Tchau!"

            show sayuri desesperada with hpunch

            s "[mc]! A minha técnica tá em casa!"

            mc desconfiado "E por que você tá tão afoita?"

            s "Se ela esperar mais de 5 minutos ela vai acabar comigo nos treinos."

            s "Ela vai me fazer dar 666 voltas na quadra!"

            mc zerado "Que exageiro..."

            s "Desculpa sair assim, mas eu não tenho escolha!"

            s "Obrigada por tudo! A gente se fala!"

            hide sayuri desesperada with moveoutleft

            "Uou. Essa treinadora deve ser o cão chupando manga..."

            "Mas hoje o dia foi demais. Eu me aproximei da [s] e a gente virou amigos de verdade."

            "Não sei se vou ver ela como amiga para sempre, mas por hora é como eu quero que as coisas sigam."

            "Quero ajudar ela a ter menos medo das coisas e quem sabe ela até não me leve pra ver ela nas olimpíadas?"

            "Isso seria demais!"

            jump sayuri_e3_final
        else:


            jump sayuri_e3_fracasso

    label sayuri_e3_fracasso:

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("sayuri_e3_fracasso","sayuri","personagem")

        $ sayuri_e3 = "fracasso"

        show sayuri desesperada with dissolve

        s "Nã-não!"

        $ renpy.notify("Sayuri não confia em você o suficiente")

        s "Por favor me desculpe, [mc]. Mas eu não posso!"

        mc preocupado "O que foi, [s]?"

        s "E-eu tenho muito medo. Medo de que aconteça igual das outras vezes."

        mc "..."

        s "Obrigada por tudo! Nunca vou esquecer o que você fez por mim hoje."

        s "Mas eu preciso de um tempo sozinha. Por favor, não venha atrás de mim."

        hide sayuri with moveoutleft

        mc "[s]..."

        "Que droga! Eu não consegui... Não consegui fazer com que ela confiasse em mim."

        "O que será que eu fiz de errado?"

        if se3_pelada:

            "Se pelo menos eu não tivesse desrespeitado ela olhando pela fresta enquanto ela se trocava..."

            "Por que eu sou tão idiota?!"

        "Talvez outras respostas que eu dei durante o dia também não foram as melhores."

        "Eu preciso repensar o que eu fiz hoje se eu quiser ter uma chance com ela no futuro..."

        jump sayuri_e3_final

    label sayuri_e3_final:

        show atendente normal with dissolve

        "Atendente" "Senhor..."

        mc surpreso "Opa!"

        "Atendente" "Desculpe..."

        mc serio "Mano, que susto..."

        mc normal "Que foi?"

        "Atendente" "Só gostaria de lembrar o senhor de acertar os produtos que a senhorita levou."

        mc desconfiado "Como?"

        "Atendente" "A senhorita saiu correndo agora há pouco com os produtos da loja. Eu imaginei que o senhor iria acertar os valores."

        mc zerado "..."

        mc "Quanto que eu devo?"

        "Atendente" "Por sorte aqueles itens estavam em promoção."

        mc concentrando "Ufa..."

        "Atendente" "Fica em apenas R$ 499 à vista no dinheiro ou débito..."

        mc surpreso "Quê?!"

        "Atendente" "... pela blusa. A calça ficou em mais..."

        mc zerado "Caralho..."

        scene black with Dissolve(2.0)

        pause

        scene sayuri_quarto with Dissolve(1.0)

        label say3_premium1:

            pass

        menu:
            "O que será que a [s] tá pensando?":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_43

                    jump say3_premium1

                s "Sai de cima, [g]!"

                scene sayuri_quarto7 with Dissolve(1.0)

                g "Me conta logo como foi!"

                s "Você tá me deixando nervosa, [g]!"

                g "Vocês dois sozinhos! Sem eu lá pra proteger você dele! Aposto que ele tentou de tudo com você!"

                s "N-nãoo!"

                g "Eu sou sua mana! Você não precisa ficar assim comigo!"

                s "C-calma... eu vou contar!"

                g "Espera! Posso me ajeitar em você?"

                s "[g]..."

                g "Só tem a gente aqui! E eu tô com saudades da minha mana."

                menu:
                    "Melhor não.":


                        s "Melhor a gente continuar assim."

                        g "Sem graça..."
                    "Ok... vem aqui...":


                        s "Tudo bem... vem aqui."

                        g "Eba!"

                        scene sayuri_quarto8 with Dissolve(1.0)

                        g "Eu adoro ficar assim com você, mana."

                        s "Olha o que você fez com a camisola..."
                        scene snew_ani08 with Dissolve(1.0)
                        g "Não esquenta com isso. Eu tenho dois desses igual você."

                        s "Você é impossível..."

                g "Então vai, fala."

                if sayuri_e3 == "beijo":

                    s "A gente... ai meu Deus... não tenho coragem de contar."

                    g "Vocês ficaram?!"

                    s "Ele me levou pro lugar onde troca... o t-trocador..."

                    g "Tá tá. E aí?! Ele te comeu?!"

                    s "Claro que não! Não fala assim!"

                    s "Ele me deu... um beijo."

                    g "Um beijo?!"

                    s "É. Você acredita?!"

                    g "Não... não acredito..."

                    s "Foi nosso segundo encontro..."

                    g "Esse cara é um banana, mana! Se fosse eu, arrancava sua roupa lá mesmo e te tacava na parede!"

                    s "Tá louca, [g]?!"

                elif sayuri_e3 == "amizade":

                    s "Ele disse que... queria ser meu amigo. Foi incrível."

                    g "A-amigo?! Você tá falando sério?!"

                    g "Esse cara é um banana, mana! Se fosse eu, arrancava sua roupa lá mesmo e te tacava na parede!"

                    s "Tá louca, [g]?!"
                else:


                    s "Ele foi bacana comigo... mas não rolou nada de mais."

                    s "Ele até falou um negócio lá... mas eu não senti confortável pra aceitar qualquer coisa."

                    g "Hmm... que pena..."

                    s "É..."

                    g "Esse cara é um banana, mana! Se fosse eu, arrancava sua roupa lá mesmo e te tacava na parede!"

                    s "Tá louca, [g]?!"

                g "Até parece que eu ia deixar um mulherão igual você escapar assim!"

                g "Você sabe que você é incrível, né, mana? Você é gostosa, linda, talentosa... a mulher perfeita."

                s "J-júlia... "

                g "É sério. Se você aceitasse, eu ficava com você agora mesmo. O que você acha?"

                menu:
                    "A-ah...":


                        s "A-ah... [g]..."

                        g "Posso pegar você?"

                        s "N-não fala assim... você vive falando essas coisas..."

                        g "É verdade..."
                    "Não brinca com isso.":


                        s "Haha... n-não começa com essas brincadeiras, [g]."

                        g "Eu tô falando sério. E-"

                s "Tá bom. Agora chega. Você tá me deixando desconfortável."

                g "Será que você não sente nem um pouquinho de atração por garotas?"

                s "Eu não vou falar isso com a minha irmã!"

                g "Você é chata... mas eu não vou desistir."

                s "Agora sai do meu quarto. E f-fecha a porta quando sair."

                g "Por que? Vai fazer alguma coisa?"

                s "N-não te interessa! Só fecha!"

                g "Tá bom... Boa noite, mana."

                s "Boa noite. Dorme bem."

                scene black with dissolve

                scene sayuri_quarto9 with Dissolve(1.0)

                "Essa [g]... o que passa na cabeça dessa garota?"

                "E ela fica me atazanando ainda por cima... só piora minha situação."

                "Hmm..."
                scene snew_ani09 with Dissolve(1.0)
                "Aahh... o que tá acontecendo comigo?"

                "Eu não consigo parar de pensar besteira esses tempos. Será que é culpa da [g]? O-ou será o [mc]?"

                menu:
                    "Melhor eu ir tomar um banho":


                        "Melhor eu parar com isso agora antes que piore. Eu sei muito bem onde isso vai dar. Eu vou tomar um banho."
                    "Continuar pensando no [mc]":


                        "[mc]... desde que você apareceu lá no templo e-eu tenho ficado cada vez mais t-tarada..."

                        "Você foi comigo trocar de roupa... e-eu tava pelada do seu lado..."

                        "Só uma portinha separando a gente... ahh..."

                        "Quanto mais eu penso nisso... e-eu não aguento mais. Eu tenho que pegar..."

                        scene sayuri_quarto10 with Dissolve(1.0)

                        "E-eu tava de costas pra você..."

                        "Só de calcinha... v-você podia ver tudo. Hmmm... v-você viu?"

                        "Você tava olhando pela fresta? E-eu sempre esqueço de fechar as portas... n-não sei porque..."

                        "E você não aguentou e ficou olhando pra mim? Pra minha bunda?"

                        "Ah... ahh... v-você gostou dela, [mc]?"

                        "Ela é tão redondinha... de tanto que eu treinei... ela ficou assim..."

                        "E-eu acho ela tão bonita... ela é g-gostosa... a-ah..."

                        "Falar assim tá me deixando ainda mais quente... e-esse tipo de palavra... bunda d-deliciosa..."

                        "Eu quero que você pega nela, [mc]. E-eu vou te ajudar..."

                        scene sayuri_quarto11 with Dissolve(1.0)

                        "Hm-hmmm!"

                        "E-eu nunca peguei aqui... m-mas eu tô queimando, [mc]! E-eu não aguento!"

                        "D-desculpa ser uma garota assim! E-eu não queria, m-mas... hggmm... é bom demais... só de tocar assim..."
                        scene snew_ani18 with Dissolve(1.0)
                        "V-você tá pensando na minha bunda agora? Tá?"

                        "Você t-tá se aliviando pensando nela? Apertando ela? Hmnhha!"

                        "E-eu não aguento mais, [mc]! Posso gozar?!"

                        scene sayuri_quarto12 with Dissolve(1.0)

                        s "Hnng! A-ahh!"

                        s "{i}puf puf{/i}"

                        s "A-assim.... v-vai..."
                        scene snew_ani19 with Dissolve(1.0)
                        "Mete s-seu negócio em mim, [mc]! Onde você quer colocar você coloca! Nnhhg!"

                        s "Ah! Aaagh!"

                        s "V-vaiii!!"

                        s "Aaannnng!"

                        scene black with dissolve

                        scene sayuri_quarto13 with hpunch

                        "Eu sabia, mana!"

                        s "Annh!"

                        "Você não tá aguentando mais. Você precisa de alguém pra aliviar você."

                        "Eu fico triste de ver você assim, mas você tá muito sensual! Tá me dando tanto tesão, mana!"
                        scene snew_ani01 with Dissolve(1.0)
                        "Como eu queria satisfazer você! E-eu sei que você gosta de caras, mas eu te conheço mais."

                        "Eu ia fazer você gozar igual uma cadela no cio, mana! Ahn!"

                        "Só de pensar nisso eu já tenho vontade de te comer... hmm... como eu tô molhada..."

                        "Me dá só uma chance, mana..."

                        scene sayuri_quarto14 with Dissolve(1.0)

                        "Eu também não tô mais aguentando!"

                        g "Mnm!"

                        "Eu queria que você entendesse meu amor por você! E me quisesse como sua parceira."
                        scene snew_ani02 with Dissolve(1.0)
                        g "Mnnnh..."

                        "Eu ia chupar você, me esfregar em você, na sua buceta, no seu cu. Aghh!"

                        "Eu vô gozar de te ver gozando, mana! Agnn!"

                        g "AANNNHH!"

                        s "?!"

                        "Merda!"
            "Deixa pra lá":


                pass

        scene black with dissolve

        $ tempo = 4

        $ dia_julia = dia + 1

        $ v7_fim = True

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v7_fim","sayuri","personagem")

        jump call_cidade

label sayuri_cel_msg4_resposta:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s4_save", extra_info="s4_save")

    $ iconchefe += 1

    mc desconfiado "Ué... ir no Tadaima?"

    "Será que ela quer que eu fale com a [g]? Eu tenho medo dessa menina..."

    if julia_e2 == "seducao":

        "Na outra noite a gente acabou ficando na casa dela."

        mc zerado "E mais uma vez eu fiquei na mão. {size=15}Literalmente...{/size}"

        if j2_sayuri_traida:

            "Eu não avisei a [s] que eu ia na casa dela e ela saiu da sala daquele jeito..."

            mc preocupado "Será que ela ainda tá cheteada comigo?"
    else:


        "A gente viu a premiação da [s] na casa delas na outra noite, e foi uma loucura como sempre."

        "Mas a gente acabou não se pegando, o que foi muito bom pra minha relação com a [s]."

    "O que será que ela quer que eu fale com essa garota?"

    mc concentrando "Bom... Fazer o quê?"

    "Se eu quero me aproximar da [s], não posso perder uma chance dessas. Tudo o que ela quiser eu tô aceitando."

    menu:
        "No Tadaima? Com certeza, [s].":


            $ sayuri_cel_msg4_r = "errado"

            mc safado "Ver a [s] e ainda ter a chance de dar uma olhadinha na [g]?"

            "Com certeza!"
        "Só se você estiver lá também.":


            $ sayuri_amizade += 1

            $ sayuri_cel_msg4_r = "certo"

            mc desconfiado "Não sei se quero passar lá e encontrar a [g] sozinho. Não sei o que ela vai aprontar..."

    "Deixa eu responder ela..."

    "..."

    "Ela já respondeu."

    show screen celular_sayuri

    "..."

    "Certo..."

    if tempo < 3:

        "Ainda é cedo. A [g] sai só no fim da tarde. Vou dar uma passada em casa enquanto isso."

        scene black with Dissolve(1.0)

        "..."

        if casa:

            scene ap mc_assistindo with Dissolve(1.0)
        else:


            scene apartamento tv with Dissolve(1.0)

        "Deixa eu ver este seriado aqui enquanto isso..."

        "A rainha transando com o irmão dela?"

        "Espera! O menino!"

        "Eita... Esse já era..."

        $ tempo = 3

        if casa:

            scene ap mc_dormindo3 with Dissolve(1.0)
        else:


            scene apartamento noite with Dissolve(1.0)

        "Opa. Já deu a hora."

        "Sorte que o Tadaima é aqui pertinho."

    elif tempo == 3:

        "Já são sete... A [g] já deve estar saindo. Melhor eu já ir pra lá."

    "..."

    scene restaurante jap_fora with Dissolve(2.0)

    "Esse lugar é muito pomposo mesmo..."

    scene tadaima restaurante with Dissolve(1.0)

    mc normal "Oii..."

    show garconete bemvindo with dissolve

    g "Olha quem tá aqui..."

    mc envergonhado "Oi, [g]."

    show garconete bemvindo at esquerda with move

    show sayuri meudeus with dissolve

    s "Oi, [mc]..."

    show sayuri meudeus at direita with move

    mc normal "Fala aí, [s]. Tudo bem?"

    s "Tudo sim..."

    "Uou... essas duas são lindas."

    "Por que eu tenho a impresão que todas as garotas da cidade são bonitas?"

    "Isso é muito estranho."

    "E elas conversando comigo assim..."

    "Parece que de uns tempos pra cá só acontecem coisas boas comigo..."

    mc desconfiado "..."

    show garconete perguntando with vpunch

    g "Ele tá fazendo uma cara estranha, mana! Ele tá tramando alguma coisa!"

    show sayuri surpresa with vpunch

    s "!"

    s "Que susto, [g]..."

    mc surpreso "Ah! Perdão..."

    mc envergonhado "Desculpa... Eu tava pensando em um negócio, só isso."

    show garconete charmosa with dissolve

    g "Tava pensando em sacanagem... com certeza..."

    mc surpreso "Cla-cla-claro que não!"

    if julia_e1 == "seducao" or julia_e2 == "seducao":

        g "Deve tá pensando naquela vez que a gente se..."

        "Meu Deus! Ela vai contar que a gente se beijou!"

        mc surpreso "[g]!"

        s "Como?"

        g "Não é nada não, mana."

        mc envergonhado "Hehe... ela ia falar alguma besteira, certeza..."

        s "Hmmm..."
    else:


        g "Tá bom... acredito..."

    g "Enfim, vou deixar vocês conversarem. Tenho que terminar aqui pra poder escapar da minha prisão."

    g "Beijos, [mc]."

    mc envergonhado "Até mais, [g]."

    hide garconete with dissolve

    if j2_sayuri_traida:

        show sayuri infeliz at centro with move

        s "E-eu... no outro dia..."

        "A [s] deve tá triste comigo por causa da outra noite."

        "Eu não devia ter ido escondido na casa dela e ainda por cima ter ficado com a [g]..."

        mc triste "[s]... desculpa pelo outro dia. Eu devia ter avisado que ia na sua casa."

        if sayuri_intencao == "namoro":

            if sayuri_e3 == "beijo":

                s "É... é que a gente... no provador... e você..."
            else:


                s "É que você disse... que quer ser mais... que... um... amigo..."

        elif sayuri_intencao == "amizade":

            s "É que a gente tá sendo... amigos agora... e eu pensei... que você ia me contar..."

        mc preocupado "Eu entendo. Eu devia ter te contado. Me perdoe."

        mc "Não quero que nossa relação piore por causa disso."

        show sayuri interessada with dissolve

        s "Tu-tudo bem, [mc]. Eu aceito suas desculpas..."

        mc normal "Que bom! Obrigado."
    else:


        show sayuri interessada at centro with move

        s "O-o-oi..."

        mc normal "Oi."

    menu:
        "Que bom que a [g] deu um tempo pra gente.":


            $ sayuri_amizade += 2

            mc normal "Que bom que a [g] teve que trabalhar. A gente ganhou um tempo sozinhos."

            s "Sim... E-eu gosto de conversar com você, [mc]."

            mc normal "Eu também gosto de passar tempo com você."

            s "I-isso é bom, né?"

            mc desconfiado "É sim, por que?"

            s "Não! Nada... É que se a gente realmente..."

            show sayuri surpresa with dissolve

            s "Nã-não! Não é nada!"

            mc desconfiado "Como?"

            show sayuri interessada with dissolve

            s "Não é nada... Vamos mudar de assunto."

            mc "Ok..."
        "Eu acho você linda com essa roupa.":


            $ sayuri_amizade += 1

            mc charmoso "Eu acho que você fica tão linda nessa roupa."

            show sayuri surpresa with dissolve

            s "Li-linda! Ma-mas..."

            "Pelo jeito parece que a [s] ainda não consegue lidar muito bem com elogios assim."

            "Melhor eu continuar pegando leve com ela."

            mc normal "Tá tudo bem. É só um elogio..."

            show sayuri interessada with dissolve

            s "O-ok..."
        "Uma pena que a [g] tem que trabalhar, né?":


            mc desculpa "Uma pena que a [g] tenha que trabalhar..."

            s "É verdade... Você gostaria de passar mais tempo com ela?"

            mc normal "Ela é uma garota divertida. Eu gosto de conversar com ela. Mesmo sendo meio louquinha também."

            s "Ela é. Eu gosto muito dela também."

    mc normal "E por que você veio aqui hoje? Veio acompanhar a [g] na faculdade?"

    s "Sim. Ela tava se sentindo um pouco sozinha hoje e pediu se eu podia acompanhar ela."

    show sayuri meudeus with dissolve

    s "Mas por favor não fale que eu contei... Ela não ia gostar nem um pouco."

    menu:
        "Você sabe o que aconteceu com ela?":


            mc preocupado "Se sentindo sozinha? Você sabe o que aconteceu?"

            show sayuri c_incerta with dissolve

            s "Não sei se eu devo falar pra você. E se ela ficar chateada?"

            mc charmoso "Eu só quero ajudar. Pode confiar em mim."

            s "..."

            if sayuri_amizade >= 15:

                s "Tá. Mas não fala nada pra ela."

                mc charmoso "Claro."

                s "Então..."

                show sayuri meudeus with dissolve

                s "Pode parecer estranho pra gente, mas a [g] está passando por um momento complicado."

                s "Ela... como posso dizer... sempre deu em cima dos rapazes, né?"

                mc envergonhado "Entendo..."

                s "Só que agora ela está meio que mudando... querendo algo mais, não sei exatamente..."

                s "E isso está deixando ela meio assustada, com medo..."

                mc desconfiado "Que coisa..."

                show sayuri interessada with dissolve

                s "Sim. É uma novidade pra ela. Mas eu acho que vai ser uma coisa boa."

                mc normal "Também acho."

                s "Que bom."
            else:


                s "Melhor eu não arriscar. Ela pode ficar muito triste. Desculpa."

                mc triste "Tudo bem. Você que sabe o que é melhor pra ela."

                "Parece que a [s] não confia plenamente em mim ainda."

                show sayuri interessada with dissolve
        "E você? Como você tá?":


            $ sayuri_amizade += 2

            show sayuri surpresa with dissolve

            s "E-eu?!"

            mc desconfiado "Sim. Você..."

            s "É... Por que tá interessado em mim?"

            mc "Só quero saber se você tá legal."

            show sayuri meudeus with dissolve

            s "Eu estou sim... Obrigada por perguntar."

            mc normal "Tem certeza? Não tá escondendo nada de mim, né?"

            show sayuri surpresa with dissolve

            s "E-e-escondendo?!"

            mc "Calma, só tô brincando."

            show sayuri infeliz with dissolve

            s "Ok..."

            s "..."

            "Ué? Parece que a [s] não curtiu muito minha brincadeira."

            "Será que aconteceu alguma coisa?"

            "Melhor eu tentar mudar o clima."

            mc "Eu fico feliz de você estar bem. Comigo também tá tudo legal."

            mc zerado "Tirando meu chefe que é um pé no saco..."

            show sayuri interessada with dissolve

            s "Você se mete em cada uma por causa do trabalho..."

            mc "Nem me fala..."

            s "Coitado..."
        "Pode deixar. Não vou falar nada.":


            $ sayuri_amizade += 1

            mc normal "Não se preocupe. Não vou falar nada."

            s "Obrigada. A [g] é muito reservada e eu não quero que ela perca a confiança em mim."

            mc "Essa cumplicidade que vocês têm é incrível."

            s "..."

    mc normal "Pela hora a [g] já deve tá acabando."

    s "Sim..."

    s "É... [mc]..."

    mc normal "Oi?"

    s "Eu queria te chamar..."

    show garconete e_provocando at entra_esquerda with moveinbottom

    g "Olá!"

    show sayuri surpresa at direita with move

    s "Jú-Júlia!?"

    g "O que você ia falar, mana?"

    s "Nada não!"

    g "Ok..."

    hide garconete e_provocando with dissolve

    show garconete e_provocando with dissolve

    g "Olhem aqui."

    show garconete e_sexy with dissolve

    g "E aí? Tô ou não tô gata?"

    if julia_seducao >= 9:

        "Droga! Só de ver a [g] eu já fico louco!"

        "Mas não sei seria uma boa dar brecha agora que a [s] tá aqui."

        "Vou é ficar quieto."

    show sayuri meudeus with dissolve

    s "Você está linda, [g]. Como sempre."

    g "Valeu, mana!"

    g "E você, coiso? Tô ou não tô uma delícia?"

    show sayuri surpresa with dissolve

    s "Nã-não fale assim com o [mc], [g]! Que vergonha..."

    if julia_seducao >= 15:

        "Não consigo resistir a ela!"

        "Mesmo não querendo, só consigo pensar nessa gostosa da [g]!"

    menu:
        "Tá uma delícia!":


            $ sayuri_amizade -= 2

            mc safado "Tá uma delícia!"

            s "?!"

            show sayuri infeliz with dissolve

            s "..."

            g "Eu sabia que você ia adorar..."

            "Que merda... a [s] ficou super triste com o que eu disse."

            "Mas não consigo resistir à [g]. Ela me deixa louco demais."

        "Como a [s] disse, voce tá linda." if julia_seducao <= 15:

            $ sayuri_amizade += 1

            mc normal "Como a [s] disse, você tá linda."

            show garconete e_resignada with dissolve

            g "Mas só 'linda'?"

            mc zerado "Só."

            "Se ela acha que eu vou cair nessa e chamar ela de delícia na frente da [s], ela tá é drogada."

            g "Se você diz..."

            show sayuri meudeus with dissolve

            s "Para de provocar o [mc], [g]. Ele é um rapaz direito."

            g "Desculpa, mana..."

        "Você é só uma fedelha." if julia_seducao < 9:

            $ sayuri_amizade += 2

            mc charmoso "Você é só uma fedelha querendo sensualizar."

            show sayuri meudeus with dissolve

            s "Hehe... viu, só? O [mc] é um rapaz sério."

            show garconete e_emburrada with dissolve

            g "Eii! Não vale vocês se juntarem pra me zoar!"

            mc normal "Então se comporte."

            g "{i}Grr{/i}"

    show garconete e_provocando with dissolve

    g "Ok. Podemos ir."

    show garconete e_provocando at esquerda with move

    s "Você também vai, [mc]?"

    "Será que é uma boa eu acompanhar elas?"

    if julia_seducao >= 15:

        "Quero passar tempo com elas, mas eu não consigo resistir à [g]."

        "Quanto mais tempo eu passar junto delas, maior a chance disso dar merda."

        "E agora?"

    menu:
        "Vou acompanhar vocês.":


            mc normal "Se não for problema pra vocês, eu gostaria de ir."

            show sayuri meudeus with dissolve

            s "Se-seria legal se você fosse."

            g "Pra mim dá na mesma."

            mc zerado "..."

            g "Então chega de papo e vamos lá!"

            jump sayuri_e4_faculdade
        "Deixa pra outro dia.":


            mc desculpa "Na verdade eu tô um pouco cansado hoje, acho que é melhor eu deixar pra próxima."

            show sayuri infeliz with dissolve

            s "Tudo bem. Eu entendo..."

            show garconete e_emburrada with dissolve

            g "Que mala..."

            g "Até outro dia, idiotão!"

            mc envergonhado "Boa noite, gente..."

            scene black with Dissolve(1.0)

            "É perigoso demais ficar com as duas muito tempo. Vai acabar dando merda pra mim."

            "Vou pra casa e descansar."

            jump sayuri_e4_continua

label sayuri_e4_faculdade:

    scene cidade onibus_noite with Dissolve(1.0)

    "..."

    mc zerado "Não aguento mais esse negócio de pegar ônibus."

    show garconete e_emburrada with dissolve

    g "Você?! E eu que tenho que vir e voltar todos os dias!?"

    mc envergonhado "Tem razão..."

    show garconete e_emburrada at direita with move

    show sayuri meudeus with dissolve

    s "Calma, [g]."

    show sayuri meudeus at esquerda with move

    s "Não seja mal educada..."

    g "Você protege muito ele, mana. Homens não foram feitos pra gente proteger."

    show garconete e_provocando with dissolve

    g "A gente precisa usar eles e depois descartar como se fossem lixo."

    g "Só nós duas que somos verdadeiras almas gêmeas."

    s "Não fale assim, [g]. O [mc] não é assim."

    show garconete e_resignada with dissolve

    g "Ele é igualzinho todos os outros, mana. Só muda um pouco a cara de otário e o cabelo."

    show sayuri c_incerta with dissolve

    s "Para, [g]! Eu não aceito que você fale assim do [mc]. Ele sempre foi legal com a gente."

    g "É o que você acha?"

    s "Não acho. Tenho certeza."

    if sayuri_e2 == "amizade":

        s "Ele foi muito legal comigo no Tadaima. Foi a primeira vez que alguém ficou do meu lado daquele jeito."

        s "E depois ele te levou na faculdade, mesmo com você querendo sabotar nosso e-e-encontro."

    if not sayuri_e3 == "horrivel":

        s "O [mc] ainda me ajudou com a roupa pro evento. Ele foi super paciente e atencioso comigo."

    s "Só tenho coisas boas pra falar dele!"

    g "Você é muito boba, isso sim."

    show sayuri surpresa with dissolve

    s "Jú-Júlia?! Por que você está falando isso?"

    hide garconete

    show julia e_putassa at entra_direita with vpunch

    if sayuri_intencao == "namoro":

        g "Porque você tá toda caidinha por esse idiota!"

        if sayuri_e3 == "beijo":

            g "Só porque vocês se beijaram uma vez!"
        else:


            g "Só porque ele disse que quer ser mais que um amigo!"

            g "Nem sei o que isso quer dizer!"

            g "Você nem teve coragem de beijar ele! Porque ele não merece!"

        s "Nã-não!"

        g "Si-sim! Você tá me deixando de lado por causa desse idiota!"

        g "E ele não é tão legal como você tá pensando, não! Ele é um idiota babaca estúpido e tarado!"

        show sayuri infeliz with dissolve

        s "[g]... você..."

        g "Não! Espera! Eu vou provar pra você!"

        "Eu não tô gostando nem um pouco do rumo que essa história tá tomando. Tudo o que aconteceu com a [g]..."

        if julia_e1 == "seducao" or julia_e2 == "seducao":

            if julia_e1 == "seducao":

                g "Eu podia te falar o que aconteceu quando ele me levou na faculdade... lá na praça..."

            if julia_e2 == "seducao":

                g "E se eu te contasse o que aconteceu lá na nossa casa no dia do evento!"

            g "Só que... pensando bem..."

        g "Eu nem preciso falar nada pra provar que esse cara é um babaca."

        hide sayuri with dissolve

        hide julia with dissolve

        scene cidade onibus_noite

        show julia se4_provocando with Dissolve(1.0)

        mc "Uou!"

        mc "Jú-Júlia..."

        g "Que foi, bobinho? Você não gosta quando eu esfrego minha bunda em você, assim?"

        g "Você não gosta do meu cheiro? Não gosta da minha boca?"

        mc "Ah-aah..."

        if julia_seducao >= 9:

            mc "{size=10}Isso é loucura! A [s] não pode saber de nada!{/size}"

            if julia_seducao >= 15:

                mc "{size=10}Você sabe que eu sou louco por você, mas...{/size}"

        mc "Sai de cim..."

        g "Eu vou falar uma vez só, [mc]."

        g "Se você me rejeitar agora, nunca mais você vai ter qualquer coisa disso aqui."

        if julia_seducao >= 15:

            "Ficar sem a [g]!? Tá doido?!"

            "Desculpa, [s], mas não tem como. Eu não resisto a esta delícia aqui."

        menu:

            "Sai de cima, [g]!" if julia_seducao < 15:

                mc bravo "Sai de cima, [g]! Já falei!"

                show julia e_putassa with vpunch

                g "Que foi, seu merda?! Virou santo agora?!"

                jump se4_julia_goodending
            "...":


                $ sayuri_e4 = "badending"

                mc "..."

                g "Acho bom mesmo..."

                g "Você merece até uma recompensa. Quer me sentir melhor? Na frente da [s]?"

                g "Pra ela ver como eu te deixo louco?"

                window hide

                show julia se4_esfregando with Dissolve(1.0)

                pause

                g "Hmmm..."

                g "É bom sentir minha bunda, né?"

                mc "..."

                g "Pode sentir... você mereceu..."

                hide julia

                show sayuri surpresa with vpunch

                s "Ma-mas... [mc]... Por que?!"

                s "Vo-você! Você disse..."

                show sayuri infeliz with dissolve

                s "Não acredito..."

                show sayuri infeliz at esquerda with move

                show garconete e_provocando with dissolve

                show garconete e_provocando at direita with move

                g "Viu, mana?"

                g "Não passa de um tarado idiota."

                s "..."

                g "Vamos deixar ele aí e ir pra casa. Eu vou matar aula pra gente ficar juntas."

                s "{size=15}Vamos...{/size}"

                menu:
                    "Mas, [g]...":


                        mc triste "[g] eu escolhi você, você..."

                        g "Você achou mesmo que eu queria alguma coisa com você, otário?"
                    "[s]! Não é o que você tá pensando...":


                        mc angustiado "Não, [s]! Você não..."

                        hide garconete

                        show julia e_putassa at entra_direita with vpunch

                        g "Cala a boca, otário!"

                        g "A gente tá indo nessa. Nunca mais fale com minha mana. Falei?!"

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("se4_badending","sayuri","personagem")

                mc bravo "[g]... você..."

                hide julia

                show garconete e_provocando at entra_direita with dissolve

                g "Hah! Foi bom pegar numa novinha enquanto você podia, né?!"

                g "Otário!"

                g "Vamos, mana."

                hide garconete with dissolve

                s "[mc]... Por que..."

                hide sayuri with dissolve

                "Não acredito! Que merda eu fiz?!"

                "Deixei a [g] me dominar... caí na dela e ela acabou comigo..."

                "Ela só queria me fazer ficar longe da [s] desde o começo."

                mc irritado "Filha de uma puta!"

                scene black with Dissolve(1.0)

                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("v11_fim","sayuri","personagem")

                $ v11_fim = True

                $ tempo = 4

                jump call_cidade
    else:


        g "Porque agora ele é seu melhor amigo e não eu!"

        s "Claro que não, sua boba!"

        g "É sim! Você só fala dele! É [mc] pra cá! É [mc] pra lá! Parece um papagaio quebrado!"

        mc zerado "Acho que você misturou as..."

        g "Cala a boca! Você estragou tudo!"

        s "[g]... você ainda é minha melhor amiga no mundo. A pessoa que eu mais amo."

        g "Cala a boca você também! Não minta só porque tem dó de mim!"

        s "[g]..."

        g "Fica de amizade com esse aí! Ele vai te abandonar, tonta! Vai ser deixada pra trás de novo!"

        mc triste "[g]... você..."

        g "PAREM DE FALAR!!"

        s "..."

        jump se4_julia_goodending

label se4_julia_goodending:

    $ s4_julia_good = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("se4_julia_good","sayuri","personagem")

    mc bravo "Você tá fora de controle!"

    show julia e_putassa at esquerda with move

    g "Vocês que tão! Vocês não sabem nada de amizade e muito menos de namoro! Acham que é tudo coisa de filme!"

    show sayuri infeliz with dissolve

    show sayuri infeliz at direita with move

    s "[g]... você não tá legal. Não tá pensando direito..."

    g "Parem de tentar ser superiores! Vocês dois são uns otários!"

    g "Não dá pra viver desse jeito que vocês tão tentando!"

    g "Acham que podem confiar nas pessoas! Que elas vão ficar com vocês pra sempre!"

    g "Não é assim... vocês vão..."

    g "Droga! Vocês..."

    show julia e_chorando with dissolve

    g "Vo-vocês... vocês vão sofrer... e... e... vai ser muito triste..."

    g "Drogaaa... vocês vão acabar infelizes e... eu avisei..."

    mc preocupado "..."

    s "[g]..."

    g "Idiotas..."

    s "Vem aqui, [g]."

    hide julia with dissolve

    hide sayuri with dissolve

    scene cidade onibus_noite

    show julia sayu_chorando with Dissolve(1.0)

    pause

    g "Droga, mana... nem sei porque tô falando tudo isso..."

    s "Não fica assim. Eu sempre vou estar com você."

    g "Você sabe que... eu não te acho uma idiota, né?"

    s "Eu sei, boba..."

    g "Eu tô me sentindo tão triste ultimamente... transar não tá resolvendo o problema..."

    s "[g]... você sempre vai ter eu pra conversar. E agora você tem o [mc] também."

    g "Mas ele é só um idiota..."

    s "Não é não. Ele gosta de você de verdade."

    if julia_conversou or julia_e2_conversou:

        s "Não foi você mesma que me disse que pôde conversar com ele no outro dia?"

        g "Xiu... ele vai ficar se achando..."

        mc zerado "..."

    s "Não seja cabeça dura."

    g "Tá..."

    g "Acho que já passei vergonha o suficiente por uma noite."

    s "Também acho."

    hide julia with dissolve

    show garconete e_emburrada with dissolve

    g "Ei!"

    show garconete e_emburrada at esquerda with move

    show sayuri interessada with dissolve

    s "Estou brincando com você."

    g "É... tô vendo... sua mala."

    mc normal "Fico feliz que você esteja melhor, [g]."

    mc "Você fica mais bonita sorrindo."

    show garconete e_provocando with dissolve

    g "Bah! Seu xavequeiro..."

    s "Ele tem razão."

    g "Não tô gostando de vocês se juntando contra mim..."

    mc feliz "Como você é boba..."

    show garconete e_emburrada with dissolve

    g "Tá se achando muito já!"

    g "Bom... agora já perdi o ônibus, eu vou é pra casa."

    s "Vamos então. Hoje você merece um descanso."

    show garconete e_provocando with dissolve

    g "Eba!"

    g "... Agora vou dar um tempinho pra vocês até o próximo ônibus passar."

    g "Falous, mala!"

    mc normal "Até, pirralha."

    hide garconete with dissolve

    mc "A [g] é uma peça mesmo."

    show sayuri meudeus with dissolve

    s "Às vezes ela fala umas coisas... mas no fundo ela é só uma criança."

    s "Ela tá passando por uns problemas agora. Espero que ela consiga colocar a cabeça no lugar."

    s "Se você também puder ajudar, eu ficaria muito agradecida."

    menu:
        "Claro. Qualquer coisa pela [g].":


            mc charmoso "Com certeza. Eu faço qualquer coisa pela [g]."

            s "Que bom que você gosta dela..."
        "Ela é sua irmã. Pode contar com minha ajuda.":


            $ sayuri_amizade += 1

            mc normal "Ela é sua irmã e quero te ajudar no que eu puder."

            s "Obrigada, [mc]."

    s "..."

    mc envergonhado "..."

    s "É..."

    mc normal "Oi?"

    s "Eu queria... queria... chamar você pra..."

    show garconete e_resignada at entra_esquerda with hpunch

    g "O ônibus!"

    show sayuri surpresa with hpunch

    s "!"

    mc surpreso "O motorista não tá reduzindo!"

    g "Ei!! Para!"

    mc bravo "Para aí!"

    g "Corre atrás dele!"

    hide garconete e_puta with moveoutright

    s "Tchau, [mc]!"

    hide sayuri with moveoutright

    mc surpreso "Até!"

    scene black with Dissolve(1.0)

    "Hora de ir pra casa..."

    jump sayuri_e4_continua

label sayuri_e4_continua:

    if casa:

        scene ap mc_cozinhando2 with Dissolve(1.0)
    else:


        scene apartamento noite with Dissolve(1.0)

    "Uma noite com a [s] e a [g] ao mesmo tempo não é moleza."

    if s4_julia_good:

        "E que doidera que foi esse lance com a [g]? Ela meio que surtou."

        "Eu fiquei impressionado com a [s] também. Mesmo sendo tímida, ela foi incrível com a [g]."

        "Eu nunca vi a [s] tão confiante e tão firme nas palavras... Bom, ela é a principal atleta do país. Às vezes eu esqueço isso."

    "Parecia que a [s] queria me contar alguma coisa, mas a oportunidade nunca apareceu."

    if casa:

        scene ap mc_tv_quarto with Dissolve(1.0)
    else:


        scene apartamento cama with Dissolve(1.0)

    "Fazer o quê? Agora é dormir."

    if casa:

        scene ap mc_tv_quarto with hpunch
    else:


        scene apartamento cama with hpunch

    $ renpy.vibrate(1)

    $ julia_cel_msg4 = True

    "Opa... mensagem..."

    if not casa:

        scene apartamento cama_celular with Dissolve(1.0)

    mc "Mensagem da [g]..."

    show screen celular_julia

    "..."

    "Então era isso que a [s] queria me falar e não conseguiu."

    "Vou seguir a recomendação da [g] e ligar pra ela. Ela vai se assustar certeza."

    if casa:

        scene ap quarto with Dissolve(1.0)
    else:


        scene apartamento cama with Dissolve(1.0)

    "Smartphone" "Tuu... Tuuu..."

    s "A-alô?"

    show mc cueca_telefone with dissolve

    mc "Oi, [s]. É o [mc], tudo bem?"

    s "O-oi! Aconteceu alguma coisa?"

    mc "Não... eu tava pensando aqui... quer fazer alguma coisa amanhã?"

    s "!"

    s "..."

    mc "Ééé... tava pensando que a gente podia dar uma volta na Cidade Chinesa..."

    s "!"

    mc "[s]?"

    s "Ah... é que... é incrível, [mc]."

    mc "Como incrível?"

    s "Eu tava pensando justamente nisso. É... como se você tivesse lido minha mente."

    menu:
        "Acho que a gente tá ligado.":


            $ sayuri_amizade += 2

            mc "Falando assim parece que a gente tá conectado um no outro."

            s "Vo-vo-você acha?! Mas isso é tão-tão..."

            mc "Isso vai acontecer mais e mais, [s]."

            if sayuri_intencao == "namoro":

                mc "Eu já te disse que eu quero ser mais do que um amigo."

                s "..."

                s "Eu..."

                mc "Não precisa ficar nervosa. Você vai entender meus sentimentos com o tempo."

                s "O-obrigada, [mc]. E desculpa ser assim..."

                mc "Não fale isso. Eu gosto de você por causa do seu jeito."

                s "..."
            else:


                mc "Você sabe que eu quero ser seu melhor amigo. E por isso a gente tá ligados."

                s "Eu fico tão feliz, [mc]. Eu... nunca tive um amigo assim..."

                s "É especial..."

                mc "Eu também acho, [s]. Também acho muito especial."

            mc "Mas então? Você topa?"
        "Na verdade foi a [g] que falou.":


            mc "Na verdade foi a [g] que me disse que você queria me falar isso hoje, mas não conseguiu."

            s "S-sim! Eu queria... queria... é..."

            mc "Me chamar pra sair, né?"

            s "I-i-isso!"

            mc "Você ainda está com vontade de sair comigo?"

    s "Si-sim..."

    s "Eu quero sair com você..."

    mc "Que bom! Então amanhã cedo? Onde a gente se encontra?"

    s "Sabe o primeiro ponto assim que você chega no bairro?"

    mc "Sei, sim. É onde eu sempre paro."

    s "Pode ser lá?"

    mc "Perfeito. Então está fechado. É um encontro."

    s "E-encontro... ok!"

    mc "Boa noite, [s]."

    s "Boa noite, [mc]..."

    if not casa:

        scene apartamento cama_celular with Dissolve(1.0)
    else:


        scene ap mc_tv_quarto with Dissolve(1.0)

    "A [s] é realmente uma garota diferente. A dificuldade que ela tem em se relacionar..."

    "Fico pensando que tipo de coisas ela passou na vida pra ter ficado assim... tão medrosa, sei lá..."

    "Bom, já pensei demais. Preciso estar cheio de energia pra amanhã."

    if casa:

        scene ap mc_dormindo2 with Dissolve(1.0)
    else:


        scene mc dormindo with Dissolve(1.0)

    if sayuri_intencao == "namoro":

        "Amanhã vai ser a primeira vez que eu e a [s] vamos sair totalmente sozinhos..."

        "Talvez seja a hora ideal pra eu finalmente tornar nossa relação em algo mais."

        if sayuri_e3 == "beijo":

            "Depois do nosso beijo aquele dia... sinto que estou indo muito bem."
        else:


            mc angustiado "Espero que ela também queira algo mais comigo..."

    "Não tô conseguindo desligar a cabeça..."

    "Não..."

    $ dia += 1
    $ tempo = 1

    scene black with Dissolve(2.0)

    "..."

    scene fadolandia geral_bot with Dissolve(1.0)

    mc desconfiado "Este lugar?"

    show pixie bonitinha with dissolve

    p "Oie!"

    p "Como vai, [mc]?"

    mc "Você?"

    mc zerado "Me chamando de novo? Espero que não seja nada urgente..."

    show pixie desconfiada with dissolve

    p "Olha... você tem a péssima mania de se envolver com pessoas perigosas."

    mc desconfiado "Como é?"

    p "Eu te dei o poder perfeito e você tem toda a população mundial para se embrenhar, mas você escolhe só as armadilhas."

    mc envergonhado "Juro que não é de propósito..."

    p "{i}Grrr{/i}"

    if v6_fim:

        p "Primeiro foi aquela garota [c] e agora essa chinesinha."

    p "Vou falar uma vez só. Tome cuidado. Tome cuidado para não cair duro!"

    mc preocupado "Esse seu jeito de falar tá me deixando preocupado."

    p "Todas suas escolhas têm consequências, [mc]. Você tá cansado de saber disso."

    p "E o rio só anda para frente. Sua sorte é que você tem a fada mais sexy do mundo ao seu lado."

    p "Agora dá o fora que só de olhar para você já tá me cansando!"

    p "Pelo menos vê se come ela!"

    if sayuri_intencao == "amizade":

        mc desculpa "Mas eu decidi só ser amigo dela."

        p "AAAAAAAAAHHHHHHHH!"

    scene black with Dissolve(0.2)

    if casa:

        scene ap mc_tv_quarto with Dissolve(1.0)
    else:


        scene apartamento cama with hpunch

    mc surpreso "UOU!"

    "Mano... que susto..."

    if not casa:

        scene apartamento cama_celular with Dissolve(1.0)

    "Já são 9 horas... E eu não vou fazer a [s] me esperar de forma alguma."

    "Bora bater aquele banho e dar o fora."

    play sound "audio/som_16_chuveiro.mp3"

    if casa:

        scene ap mc_chuveiro with Dissolve(1.0)
    else:


        scene mc banho with Dissolve(1.0)

    $ renpy.pause(5)

    "..."

    stop sound

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento dia with Dissolve(1.0)

    if not carro:

        "Agora já tô cheiroso. Tenho que pegar o busão até a Cidade Chinesa."

        scene black with Dissolve(1.0)

        scene cidade onibus with Dissolve(1.0)

        "..."

        "E pra variar esperar esse busão que nunca passa nos horários certos."

        call cena_onibus from _call_cena_onibus_6
    else:


        "Agora já tô cheiroso. Bora dirigir até a Cidade Chinesa."

        play sound som_carro

        scene black with dissolve

        scene carro_mc_cidade1 with Dissolve(1.0)

        pause

        scene black with dissolve











    "Opa. Cheguei no ponto."

    stop sound

    play sound "audio/som_7_cidade_chinesa.mp3"

    scene c_chinesa geral with Dissolve(3.0)

    "Mano... olha pra este lugar... Quem ia querer passear num lugar como este?"

    "Por que eu chamei ela pra vir justo aqui?"

    mc zerado "..."

    s "Olá."

    mc surpreso "[s]!"

    show sayuri normal with dissolve

    s "O-oi, [mc]."

    menu:
        "Cumprimentar ela com um abraço":


            mc normal "Vem aqui. Deixa eu te dar um abraço."

            show sayuri assustada with vpunch

            s "A-abraço?!"

            if sayuri_amizade >= 24:

                $ sayuri_amizade += 2

                show sayuri abraco with Dissolve(1.0)

                if sayuri_intencao == "namoro":

                    mc charmoso "Você tá bem?"

                    s "A-ai... [mc]..."

                    mc "Tá tudo legal. Não é bom dar um abraço?"

                    s "S-sim..."

                    s "Eu tô legal. E você?"

                    mc "Eu também. Tava ansioso pra te ver hoje."

                    s "Que bom. Eu também."
                else:




                    mc normal "Não é bom abraçar os amigos?"

                    s "É, sim."

                    mc "Tudo legal com você?"

                    s "Eu tô legal. E você?"

                    mc "Eu também. Tava ansioso pra te ver hoje."

                    s "Eu também."
            else:


                s "E-e-eu não posso!"

                mc preocupado "Ué, por que?"

                show sayuri pensando with dissolve

                s "De-desculpa, mas..."

                mc envergonhado "Tá tudo legal, [s]. Eu entendo. Não precisar ficar nervosa."

                show sayuri normal with dissolve

                s "Obrigada, [mc]."

                "Parece que ela não confia em mim o suficiente para isso. Vou ter que ser uma boa companhia pra ela hoje se eu quiser mudar isso."

                "Também não posso exagerar nas investidas. Preciso aumentar a intimidade dela comigo primeiro."
        "Cumprimentar normalmente sem abraçar":


            $ sayuri_amizade += 1

            mc normal "Tudo bem com você?"

            s "Sim. Estava ansiosa pro nosso e-e-encontro."

            mc "Eu também."

            if sayuri_intencao == "namoro":

                mc charmoso "Eu quero que hoje seja um dia bem especial pra gente."

                s "É..."

                "Ela continua muito nervosa. Tenho que pensar bem como abordar este encontro."
            else:


                mc normal "Pronta pra muita diversão?"

                s "Eu estou!"

                mc "Vai ser um dia muito bacana. Você vai ver."

    if s4_julia_good:

        show sayuri triste with dissolve

        s "Antes de qualquer coisa, queria te pedir desculpas por ontem."

        s "A [g] não tava legal."

        mc desculpa "Não esquenta com isso."

        s "O-obrigada..."

        mc normal "Ela tá melhor?"

        s "Tá sim. Acho que ela colocou tudo pra fora ontem."

        s "Parece que hoje ela vai sair com um rapaz."

        mc "Entendi..."

        mc "Mas, falando da gente!"

    mc envergonhado "Eu queria levar você em um lugar bacana, mas você deve conhecer aqui muito melhor do que eu."

    show sayuri pensando with dissolve

    s "Eu fico nervosa quando tenho que escolher coisas para os outros, por isso eu prefiro que você escolha..."

    s "Se-se não for muito incômodo, claro!"

    "Caraca... não faço a mínima ideia de como andar neste lugar. Nem consigo ler as placas..."

    "Olha a merda em que eu fui me meter."

    mc triste "..."

    s "Tudo bem, [mc]?"

    "Droga! Não posso deixar ela ficar desconfortável. A [s] deve tá fazendo um grande esforço pra estar aqui."

    "Eu preciso fazer a minha parte."

    mc charmoso "Está sim. Pode deixar comigo."

    mc normal "O que você acha da gente começar comendo alguma coisa?"

    show sayuri normal with dissolve

    s "Eu estava nervosa demais pra comer quando acordei. Acho que eu gostaria."

    mc "Perfeito. Vamos então?"

    s "Sim!"

    "Que Deus me ajude..."

    scene c_chinesa rua with Dissolve(3.0)

    "Várias e várias lojas. E não faço a mínima ideia pra que servem..."

    "Pelo menos uma dessas está em inglês. É uma drogaria... Mas e as outras?"

    show sayuri normal with dissolve

    s "Tudo legal, [mc]?"

    mc envergonhado "Si-sim! Só tô pensando o que seria legal a gente comer."

    s "O-obrigada por decidir isso pela gente."

    mc "Hehehe... De nada..."

    "Droga! Não posso perguntar pra [s]. Vou ter que arriscar alguma delas."

    label se4_escolher_loja:

        scene c_chinesa rua with Dissolve(1.0)

        "Qual eu vou escolher?"

    menu:
        "Tentar a loja de letreiro colorido":


            "Essa aqui me chamou bastante a atenção."

            mc normal "Vamos ver nesta aqui com o letreiro?"

            show sayuri normal with dissolve

            s "Essa é uma loja que vende coisas por 99 centavos."

            s "Você acha que vai ter algo legal pra comer aí?"

            mc surpreso "Com certeza não!"

            s "Hehe... também acho..."

            mc envergonhado "É que eu pensei que talvez eles pudessem vender outras coisas."

            s "Essas lojas vendem de tudo. Inclusive muitos chineses vão para outros lugares do mundo e abrem lojas como essa."

            show sayuri triste with dissolve

            s "Os chineses são um povo muito lutador. Mas muitas pessoas têm preconceito. Dizem que o que fazemos e vendemos é de má qualidade."

            mc desculpa "Isso é ruim..."

            s "Por isso que eu preciso orgulhar meu país acima de tudo. Vou fazer o que for preciso para provar que os chineses são incríveis."

            mc normal "Você é realmente incrível."

            show sayuri assustada with dissolve

            s "Isso não é nada de mais! É só minha obrigação."

            mc charmoso "Eu acho incrível."

            s "E-e-eu..."

            mc normal "Vamos continuar."

            s "O-ok..."

            jump se4_escolher_loja
        "Tentar a loja de fachada branca":


            mc feliz "Já sei! Vamos nesta aqui! Parece bem limpa e com certeza..."

            show sayuri incerta with dissolve

            s "Essa é uma loja de vestidos de luxo..."

            mc envergonhado "Eu pensei que fosse..."

            s "A única coisa que tem aí pra comer são uns docinhos que eles te dão pra você se sentir à vontade."

            mc envergonhado "E daí gastar toda sua grana em um vestido que custa milhões."

            show sayuri desesperada with dissolve

            s "Vo-você acha que eles tão dando um golpe?!"

            mc surpreso "Não! O povo chinês nunca faria algo assim!"

            show sayuri normal with dissolve

            s "Você acha de verdade?"

            mc envergonhado "Claro! Eu só tava fazendo uma piadinha sem compromisso..."

            s "Obrigada, [mc]. Não quero que você pense mal dos chineses."

            show sayuri triste with dissolve

            s "Só de pensar que existem pessoas do meu povo fazendo coisas erradas, eu fico muito triste."

            s "Me dá um aperto no peito..."

            mc desculpa "Não pensei nisso."

            mc normal "Eu tenho certeza que eles dão esses docinhos só pra pessoa se sentir melhor. É uma coisa boa!"

            s "E-eu acredito em você..."

            jump se4_escolher_loja
        "Tentar a loja com porta pequena":


            "Se eu parecer animado talvez eu passe mais confiança..."

            mc surpreso "Então vamos comer nesta aqui! É bem pequenas, só que parece muito legal! Uoooohh!"

            show sayuri assustada with vpunch

            s "E-e-eu acho que esse é um cinema de fi-filmes... fi-filmes..."

            mc desconfiado "Filmes do quê?"

            s "Fi-fi-filmes!"

            mc surpreso "Filmes adultos?!"

            show sayuri zonza with dissolve

            s "Si-si-si..."

            mc envergonhado "Ok ok! Entendi."

            mc "Está tudo bem, [s]."

            s "Vo-vo-vo você... quer... ver..."

            mc surpreso "Nã-não! Não quero assistir."

            s "Ah tah..."

            mc envergonhado "Não. Pornografia é coisa avançada demais pra mim."

            "Até parece..."

            show sayuri normal with dissolve

            s "Que bom, [mc]... Pra mim também é a-avançado..."

            s "Às vezes a [g] quer ver comigo, e daí..."

            show sayuri desesperada with dissolve

            s "Que-que que eu tô falando?!"

            s "E-eu..."

            show sayuri zonza with dissolve

            s "..."

            mc desconfiado "..."

            s "..."

            "Acho que ela quebrou..."

            mc "Vamos continuar que a gente ganha mais."

            s "..."

            jump se4_escolher_loja
        "Continuar andando":


            "Sinto que nenhuma loja dessa rua é o que a gente tá procurando."

            "Vou tentar seguir reto."

            mc normal "Acho que nada aqui me agradou. Vamos continuar procurando?"

            show sayuri normal with dissolve

            s "Claro, [mc]. Podemos comer onde você achar melhor."

            "O problema é que eu nem sei o que eu acho melhor..."

            jump sayuri_e4_lamen

label sayuri_e4_lamen:

    "..."

    scene c_chinesa lamen with Dissolve(3.0)

    pause

    mc surpreso "Comida!"

    mc envergonhado "..."

    "Não! Não é possível que depois de levar a [s] pro Tadaima agora a gente vai comer macarrão instantâneo!"

    "Mas... e se não tiver nenhum outro lugar pra comer?"

    show sayuri normal with dissolve

    s "Você está pensando em comer lámen?"

    mc surpreso "Eu?! Eu?! É..."

    menu:
        "De forma alguma! De onde você tirou isso?":


            $ sayuri_amizade += 1

            mc surpreso "Comer lámen?!"

            mc envergonhado "Claro que não... Eu não sou desses que leva uma garota pra comer lámen de barraquinha."

            s "Eu não me importaria de comer aqui. O senhor dono que serve lámen aqui é muito conhecido."

            mc "Mas macarrão instantâneo?"

            s "É muito diferente do que você tá pensando. Não é a mesma coisa daqueles miojos de três minutos."

            mc "Não é?"

            s "Claro que não! Aqui ele é feito com muita técnica e esforço."

            mc normal "Ok! Você me convenceu. Vamos comer esse miojo profissional."

            show sayuri zonza with dissolve

            mc envergonhado "Quer dizer... esse lámen especial!"
        "Seria interessante comermos esse prato original chinês.":


            mc feliz "Eu achei que seria simples demais, mas pensando bem é uma boa chance de comer um prato da incrível culinária chinesa."

            show sayuri triste with dissolve

            s "Mas lámen é um prato japonês, [mc]."

            mc surpreso "Sé-sério?!"

            s "Você continua tendo problemas pra diferenciar chinês de japonês."

            mc envergonhado "Aparentemente sim..."

            show sayuri normal with dissolve

            s "Lámen é um prato japonês. Mas ele é famoso na china também. Ah! E ele é feito com macarrão chinês."

            mc normal "Entendi. Não sabia disso."

            s "Você tem vontade de comer, então?"

            "Vontade, vontade eu não tenho... mas e se eu não encontrar nenhum lugar pra comer com ela?"

            mc normal "Eu tenho, sim. Mas e você?"

            s "Faz bastante tempo que eu não como. Eu adoraria."

            mc "Então tá combinado!"
        "Seria uma boa. Eu nunca comi lámen em um lugar assim.":


            $ sayuri_amizade += 2

            mc normal "Eu nunca comi em um lugar assim, então tenho curiosidade. Mas não quero que seja chato pra você."

            show sayuri incerta with dissolve

            s "Não vai ser nada chato. Eu adoro lámen e fico feliz de você comer em um lugar tão tradicional da Cidade Chinesa."

            mc desconfiado "Tradicional? Esse carrinho velho aí?"

            s "Sim! Esse senhor está aí há vários anos e ele é tão legal comigo. Sempre me dava lámen de graça quando eu treinava."

            mc normal "Que bacana."

            s "Parece que ele vive sozinho... mas ele nunca me explicou direito a história dele."

            mc "Podemos tentar tirar algo dele hoje."

            s "Vamos tentar!"

    mc "Vamos lá."

    hide sayuri with dissolve

    "..."

    mc normal "Bom dia, senhor."

    show bao normal with dissolve

    chi "Bom dia, jovem."

    chi "Oh! Veja se não é minha querida Ai Fen!"

    show bao normal at esquerda with move

    show sayuri normal with dissolve

    $ chi_nome = "Bao Chang"

    s "Bom dia, senhor [chi]."

    show sayuri normal at direita with move

    chi "Não é necessária tamanha formalidade. Me chame de vô Bao."

    s "O senhor sabe que não me sinto bem..."

    chi "Eu entendo, filha."

    mc desconfiado "Do que ele te chamou?"

    s "O senhor [chi] sempre me chama de Ai Fen... não sei por que."

    chi "Eu só acho que Ai Fen tem mais sua cara do que [sc]."

    s "Senhor..."

    chi "Não brigue com este velho por coisa tão pequena, Ai."

    s "Ok..."

    chi "E o que posso fazer pelos dois jovens enamorados?"

    show sayuri assustada with hpunch

    s "Nã-não!"

    if sayuri_e3 == "beijo":

        s "Fo-foi só um bei... Digo!"

        s "Não!"

    show sayuri zonza with dissolve

    chi "Pelo que vejo, a Ai continua com esse problema..."

    mc normal "A [s] é um pouco envergonhada, senhor."

    chi "Infelizmente existem feridas que não cicatrizam tão cedo, não é querida Ai?"

    show sayuri triste with dissolve

    s "Senhor [chi]... por favor..."

    chi "Não se preocupe, Ai. Este velho não fará nada que vá contra sua vontade."

    s "..."

    "Parece que ficou um climão de uma hora pra outra..."

    mc normal "Estou muito ansioso para experimentar seu lámen!"

    chi "Você tem uma oportunidade divina, jovem."

    mc "Sério? Qual?"

    chi "Muitos gostariam de voltar no tempo e terem novamente a experiência de comer meu lámen pela primeira vez."

    chi "Alguns dariam toda sua riqueza por uma oportunidade como essa."

    mc zerado "Acho que o senhor está exagerando um pouco."

    show sayuri normal with dissolve

    s "Ele diz a verdade, [mc]. Você vai ver."

    chi "Vou preparar dois especiais no capricho. Me deem licença, crianças."

    hide bao normal with moveoutleft

    show sayuri normal at centro with move

    s "Tenho certeza que você vai adorar."

    mc normal "Você diz que faz tempo que você não come. Por que parou? Não está mais treinando?"

    show sayuri pensando with dissolve

    s "Claro que estou!"

    s "Inclusive as Olimpíadas são este ano... As classificatórias são logo mais..."

    mc feliz "É verdade! Vai ser muito legal ver você competindo."

    s "É... eu ainda não sei se vou competir."

    mc desconfiado "Como assim?"

    s "I-isso é meio complicado, [mc]. É que tem outra garota... e talvez..."

    show bao normal at entra_esquerda with vpunch

    chi "Os lámens estão prontos, crianças!"

    s "Eu vou lavar as mãos. Com licença..."

    hide sayuri with moveoutleft

    "Eita... a [s] saiu correndo."

    "Será que esse lance de Olimpíadas chateou ela?"

    hide bao with dissolve

    show bao normal with dissolve

    chi "Seu nome é [mc], certo?"

    mc desconfiado "Isso mesmo. O senhor quer alguma coisa?"

    chi "Não precisa fazer essa cara, [mc]. Eu só estou um pouco preocupado com você, só isso."

    mc preocupado "O senhor está ME deixando preocupado agora..."

    chi "Você parece conhecer a [s] há algum tempo. Você deve ter percebido que ela não tem muitos amigos."

    mc concentrando "Não lembro dela ter falado em amigos..."

    chi "Ela não pode falar sobre o que não existe."

    chi "A [s] é uma atleta de ponta, e praticamente toda comunidade chinesa se espelha nela. Ela carrega um grande fardo."

    mc desculpa "Eu imagino que não seja fácil..."

    chi "Você não imagina. Não tem como imaginar. Tudo isso está distante demais da sua realidade."

    if julia_e2_conversou:

        mc desculpa "O senhor não estaria se referindo a tal da organização chinesa..."

        chi "Quê?! Você sabe da tríade?"

        mc desconfiado "Tríade?"

        chi "Do que você está falando?"

        mc desculpa "A irmã da [s] me falou sobre uma organização."

        mc "É um grupo que, pelo que ela falou, ajudou a [s] virar uma atleta de ponta."

        chi "Incrível..."

        chi "Alguém de fora como você saber de algo assim. Talvez você tenha uma chance."

        chi "Talvez você possa livrar minha pobre Ai Fen de tudo isso."

        mc preocupado "Livrar? Por que ela ia querer se livrar das pessoas que treinaram ela?"

        chi "Tudo vai se encaixar no momento correto, jovem. E uma última recomendação."

        chi "Leve em consideração que grandes amores e grandes realizações envolvem grandes riscos."
    else:


        mc preocupado "Eu realmente não sei sobre o que você tá falando."

        chi "Você está mexendo em um vespeiro de grandes vespas. Mesmo assim..."

        chi "Leve em consideração que grandes amores e grandes realizações envolvem grandes riscos."

        chi "Eu lhe desejo boa sorte."

    mc desconfiado "O senhor..."

    show sayuri normal with moveinbottom

    s "Voltei. Desculpa a demora..."

    show bao normal at direita with move

    chi "Eu vou deixar vocês apreciarem esta maravilha."

    hide bao with moveoutright

    s "Estou com fome..."

    mc desculpa "Eu também..."

    show sayuri desesperada with dissolve

    s "Que foi, [mc]? Você tá triste?"

    mc surpreso "Nã-não foi nada!"

    mc normal "Vamos comer?"

    show sayuri normal with dissolve

    s "Vamos, sim..."

    "O que esse velho quis dizer?"

    "Impossível não ficar cabreiro depois de tudo isso..."

    "Droga! Não posso ficar pensando nisso agora. A [s] vai perceber."

    mc normal "Deixa eu dar uma olhada nesse meu lámen mega especial."

    hide sayuri with dissolve

    show lamen with dissolve

    mc desconfiado "O que vai nisso?"

    "Tirando o macarrão e o ovo nem sei o que vai nisso... Que carne será essa?"

    mc desconfiado "Bora botar pra dentro!"

    scene sayuri lamen with Dissolve(3.0)

    mc "{i}glup glup{/i}"

    s "O cheiro do meu é incrível!"

    s "Eu tava com tanta saudades de comer o lámen do senhor [chi]."

    s "Tudo é tão..."

    s "Você tá bem, [mc]?"

    mc "É estranho... nem sei o que tô comendo, mas é uma delícia!"

    s "Eu te falei."

    mc "Ele desce quente, e gelado, e salgado, e doce, e azedo, e amargo e é líquido e sólido e..."

    s "Eu entendi hihi..."

    s "A primeira vez que a gente come é inesquecível."

    mc "{i}Puuaahhh{/i}"

    mc "Delicioso..."

    mc "[s]! Você ainda nem começou a comer?"

    s "De-desculpa... É que eu fiquei entretida vendo você comer... você estava comendo com tanta vontade..."

    mc "Então pare de me xeretar e coma o seu!"

    s "Hihi... tu-tudo bem..."

    "..."

    scene c_chinesa lamen with Dissolve(1.0)

    show sayuri normal at entra_esquerda with dissolve

    s "Estava uma delícia. Como sempre."

    mc normal "Também achei. Simplesmente incrível."

    show bao normal at entra_direita with dissolve

    chi "É gratificante saber que vocês gostaram. Voltem sempre que quiserem."

    mc normal "Com certeza."

    mc "Agora vamos continuar nosso passeio. Pronta, [s]?"

    s "Sim..."

    scene c_chinesa predios with Dissolve(3.0)

    mc "Este bairro é tão diferente do restante da cidade. São tantos prédios, tantas pessoas..."

    s "Sim. É realmente uma vista única."

    mc "Você pode me falar um pouco sobre este lugar?"

    s "Eu adoraria. Tem alguma coisa específica que você quer saber?"

    label sayuri_e4_cchinesa:

        mc "Deixa eu ver..."

    menu:
        "Você sabe como este bairro surgiu?":


            $ se4_cidade = True

            s "Essa é uma história antiga que todos os chineses que vivem aqui precisam conhecer."

            s "A Cidade Chinesa é um dos primeiros bairros da cidade, acredita?"

            mc "Sério?"

            s "Sim. Quando os primeiros imigrantes chegaram havia um grupo de chineses entre eles. Logo em seguida alguns grupos europeus se juntaram."

            s "Pelo que eu sei, durante a fundação, os chineses e os italianos dividiram a cidade em duas metades."

            s "Mas os italianos descumpriram o acordo e começaram a ameaçar as famílias chinesas. Como eles eram maioria, empurraram essas famílias para cá."

            mc "Caraca, que barra."

            s "Sim. Com essa pequena área, de péssima localização ainda, os chineses tiveram que construir um bairro vertical para acomodar todos."

            s "Os italianos dominam a maior parte da capital até hoje. Alguns dizem até que eles possuem máfias que controlam vários pontos importantes."

            mc "Isso parece coisa de filme..."

            s "Verdade. Melhor não ficarmos dando atenção a essas coisas..."

            s "Você quer saber mais alguma coisa?"

            jump sayuri_e4_cchinesa
        "O que é aquela entrada lá embaixo?":


            $ se4_chinatown = True

            mc "Eu consigo ver uma espécie de corredor ali embaixo. Onde aquilo vai?"

            s "Onde?"

            scene c_chinesa entrada_chinatown with Dissolve(2.0)

            mc "Ali, perto do esgoto, com uma placa escrita em chinês."

            s "Ah! É... não é nada..."

            mc "Como assim não é nada?"

            s "É só uma área que não é usada. Deve ser um depósito de lixo ou algo assim. Acho que eu nunca fui pra lá..."

            mc "Hmm..."

            s "Não precisa pensar muito sobre aquilo. É melhor que você nem desça até aquela área. O esgoto é bem fedido."

            mc "Anotado..."

            "Por que ela parece meio reticente sobre aquele lugar?"

            "Longe de mim duvidar da [s], mas algo aqui não tá cheirando bem. E não é o esgoto..."

            "..."

            scene c_chinesa predios with Dissolve(1.0)

            s "É... você quer perguntar mais alguma coisa?"

            jump sayuri_e4_cchinesa
        "Nada, não. Vamos continuar o passeio.":


            mc "Acho que tá bom por agora. Estou ansioso pra continuar nosso passeio."

            s "Eu também."

label sayuri_e4_fenju:

    scene c_chinesa rua_dois with Dissolve(3.0)

    mc normal "Quando a gente tava olhando os prédios eu vi um lugar que pareceu bem legal."

    mc "Eu queria te levar lá."

    show sayuri pensando with dissolve

    s "Lu-lugar? Que lugar?"

    mc charmoso "Não precisa se preocupar. É um lugar bem bacana."

    s "E-eu não gosto muito de..."

    hide sayuri

    show fenju desesperada with hpunch

    fen "Sa-[s]!"

    show sayuri assustada at entra_direita with dissolve

    $ fen_nome = "Fen Ju"

    s "[fen]?! O que está fazendo aqui?"

    show fenju desesperada at esquerda with move

    fen "Nã-não, [s]! Eu prometo que eu tô treinando! E-eu só precisava de uma pausa!"

    fen "Po-por favor não ba..."

    show sayuri desesperada with vpunch

    s "Te-tenha calma, [fen]! Está tudo bem."

    s "Pode descansar um pouco."

    show fenju acuada with dissolve

    fen "Ve-verdade? Ou você só tá..."

    s "É verdade, [fen]. Pode ir."

    fen "Mas a mestra. Você não..."

    s "Eu prometo que não vou fazer nada. E não falo nada pra ela também."

    fen "O-obrigada, [s]. Me desculpa por ser uma folgada..."

    s "Não diga isso. E agora vai."

    fen "Ma-mas você te-tem certeza que eu..."

    s "Já falei pra ir, [fen]."

    fen "Desculpa! Já t-tô indo..."

    fen "..."

    hide fenju with dissolve

    hide sayuri with dissolve

    show sayuri triste with dissolve

    s "..."

    menu:
        "O que foi isso? Quem era ela?":


            $ se4_fenju = True

            mc desconfiado "O que foi isso? Quem era essa garota?"

            s "É só uma conhecida..."

            mc desconfiado "Ela parecia assustada... e machucada... será que ela tá bem?"

            s "Ela tá. Ela é criança... eles... vivem se machucando por aí."

            mc desculpa "Tem certeza que era de brincar?"

            show sayuri desesperada with dissolve

            s "Co-com certeza! Ela é bem peralta."

            mc normal "Então deve ser mesmo. Ufa..."

            mc "E como você conhece ela?"

            s "É-é... ela treina no mesmo lugar que eu."

            mc feliz "Então ela quer ser atleta também?"

            s "Sim..."

            s "Vo-você tava falando que encontrou um lugar bacana..."
        "Podemos continuar nosso passeio?":


            $ sayuri_amizade += 1

            "O que aconteceu aqui? Seja lá o que for, tenho certeza que a [s] não vai querer falar sobre isso."

            mc desculpa "Podemos continuar nosso passeio?"

            s "..."

            s "T-tá..."

            show sayuri normal with dissolve

            s "Obrigada, [mc]..."

            mc desculpa "..."

            mc normal "Só quero ter um tempo legal com você."

            s "E-eu também..."

    mc normal "Ah! Eu encontrei um lugar muito bacana pra gente relaxar e passar um tempo legal juntos."

    mc "Se eu entendi direito, temos que subir até lá em cima!"

    show sayuri normal with dissolve

    s "Cuidado se perder..."

    mc charmoso "Pode confiar em mim."

    scene c_chinesa predios with Dissolve(1.0)

    mc "Sobe aqui essa escadaria..."

    mc "É por aqui! {size=10}Eu acho...{/size}"

    "..."

    s "Acho que a gente já passou por este lugar."

    mc "Não passou, não."

    "..."

    mc "Acho que achei!"

    $ tempo += 1

    scene c_chinesa ofuro_entrada with Dissolve(3.0)

    mc feliz "É bem aqui! Eu disse que eu sabia... {i}puf puf{/i}"

    show sayuri normal with dissolve

    s "Cansou?"

    mc zerado "Nem todo mundo é um atleta de ponta..."

    s "Ixi... olha a hora, [mc]. Já está ficando de tarde."

    mc normal "E daí?"

    show sayuri triste with dissolve

    s "Nosso passeio tá tão bacana..."

    mc preocupado "O que foi?"

    s "É que eu preciso ir... Eu combinei de me encontrar quatro da tarde com a minha treinadora."

    mc "Puxa... mas justo agora?"

    s "É que ela vai ficar... brava... se eu não aparecer na hora combinada."

    "Eu não quero que nosso encontro acabe ainda. Eu tô só começando."

    if sayuri_intencao == "namoro":

        "Eu decidi que eu quero sair da amizade com ela. E ainda não fiz nada pra aprofundar nossa relação."

    label sayuri_e4_ofuro:

        "É complicado... mas eu quero que ela fique. Pelo menos mais um pouco..."

    "Ou será que é melhor não causar com ela e só deixar ela ir?"

    menu:
        "O que você prefere fazer?":


            mc desculpa "O que você prefere fazer?"

            show sayuri pensando with dissolve

            s "E-eu não sei..."

            s "Eu... queria muito ficar com você. O dia está sendo incrível."

            s "Só que minha treinadora é... é... ela não aceita que eu faça nada fora do combinado."

            mc desconfiado "Todo mundo faz coisa errada de vez em quando... Isso é normal."

            s "Nã-não! Não posso, [mc]! Ela vai ficar uma fera!"

            show sayuri triste with dissolve

            s "E agora?"

            menu:
                "Você precisa ficar. Vai ser legal.":


                    jump sayuri_e4_ofuro_sim
                "Eu entendo. É melhor você ir.":


                    "Não posso ser egoísta agora..."

                    jump sayuri_e4_ofuro_antes
        "Eu quero que você fique, só mais um pouco.":


            label sayuri_e4_ofuro_sim:

                mc envergonhado "Eu sei que é um pouco egoísta da minha parte, mas eu queria que você ficasse."

                show sayuri assustada with dissolve

                s "Ma-mas... minha treinadora!"

                mc desculpa "Eu sei que talvez você tenha problemas com ela, mas eu tenho certeza que vai valer a pena."

                mc normal "E você disse que quer ficar também!"

                s "Eu quero... mas..."

                mc charmoso "Eu prometo que você não vai se arrepender."

                s "Ai, [mc]..."

                s "..."

                s "E-eu..."

                if sayuri_amizade >= 27:

                    $ sayuri_e4 = "amizade"

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("sayuri_e4_amizade","pixie","personagem")

                    s "Eu acho que vou ficar..."

                    show sayuri envergonhada with dissolve

                    s "Ai, [mc]! Essa é a primeira vez que e-eu vou fazer algo assim!"

                    mc charmoso "E o que você tá sentindo?"

                    s "Eu tô com vergonha... e medo... e muito feliz!"

                    mc normal "Isso é muito legal. Fazer uma coisa errada de vez em quando é preciso. A gente sente essa adrenalina."

                    s "Sim!"

                    mc charmoso "E é claro que eu vou fazer você ficar aqui valer à pena. Você vai ver."

                    s "T-tá..."

                    jump sayuri_e4_ofuro_cena
                else:


                    show sayuri triste with dissolve

                    s "Eu... realmente não posso..."

                    s "Eu não consigo ir contra ela, [mc]."

                    show sayuri zonza with dissolve

                    s "Por favor me entenda!"

                    mc triste "..."

                    menu:
                        "Desculpa, mas eu não entendo...":


                            mc serio "Desculpa, mas eu não entendo..."

                            mc "Você precisa ter livre arbítrio pra escolher o que quer. Não tá certo isso."

                            s "Você me odeia..."

                            mc serio "Eu não tô bravo com você, [s]... Mas com a situação. Não é justo..."
                        "Claro que eu entendo...":


                            mc preocupado "Claro que eu entendo... não é sua vontade. Mas é um esforço que você tem que fazer."

                            mc "É o preço que você tem que pagar pra ser essa pessoa incrível nos esportes que você é."

                            mc desculpa "Não digo que eu concordo, mas eu te entendo de verdade."

                    show sayuri triste with dissolve

                    s "Então você não me o-odeia?"

                    mc normal "Claro que não."

                    jump sayuri_e4_ofuro_fim
        "Melhor você ir então...":


            label sayuri_e4_ofuro_antes:

                p lecionando "Opa! Tomar essa decisão fará com que o encontro acabe antes do esperado e você perca cenas importantes com a [s]."

            p "Por outro lado, você vai evitar que VOCÊ e a [s] tenham problemas com a treinadora. Você está certo disso?"

            menu:
                "Sim. Encerrar encontro.":


                    $ sayuri_amizade += 3

                    mc desculpa "Eu não quero te prejudicar. Acho melhor você ir então..."

                    show sayuri desesperada with dissolve

                    s "Você acha?!"

                    mc "Não quero que você tenha problemas com sua treinadora."

                    label sayuri_e4_ofuro_fim:

                        mc normal "Vamos ter outras oportunidades no futuro pra sairmos."

                    python:
                        if renpy.android:
                            PythonSDLActivity.registraEvento("sayuri_e4_fracasso","sayuri","personagem")

                    $ sayuri_e4 = "fracasso"

                    show sayuri abraco with dissolve

                    s "Muito obrigada, [mc]. Você é um cara incrível."

                    "Uou. Ela realmente veio me abraçar..."

                    mc charmoso "Eu me diverti muito hoje."

                    s "Eu também."

                    show sayuri normal with dissolve

                    s "Muito obrigada por um dia tão incrível."

                    mc normal "Eu que agradeço."

                    s "Até outra chance, [mc]."

                    mc "Até, [s]."

                    s "Ah! Você precisa de ajuda para sair?"

                    mc envergonhado "Pode ficar tranquila que ainda vou dar uma volta antes de sair."

                    mc "Acho que eu me acho."

                    s "Ah o-ok. Até mais."

                    mc normal "Até."

                    hide sayuri with dissolve

                    mc desculpa "Não queria ter encerrado o encontro ainda, mas é importante pra ela..."

                    jump sayuri_e4_chinatown
                "Não. Quero escolher outra opção.":


                    "Acho que prefiro pensar um pouco mais..."

                    jump sayuri_e4_ofuro

label sayuri_e4_ofuro_cena:

    mc normal "Me espere aqui que eu vou entrar lá e preparar tudo."

    s "Tá."

    mc normal "Já volto."

    hide sayuri with dissolve

    "A [s] escolheu ficar comigo. Eu preciso fazer o final do nosso passeio ser incrível!"

    scene black with Dissolve(1.0)

    mc normal "Eu gostaria de reservar um banho para dois."

    "Atendente" "Claro, senhor. Espere cinco minutos, chame sua companhia e entre por aquela porta. Vamos preparar tudo pra você."

    mc "Obrigado."

    "..."

    scene c_chinesa ofuro_entrada with Dissolve(3.0)

    mc normal "Voltei. Está tudo pronto."

    show sayuri pensando with dissolve

    s "Oi. Sabia que eu não sei o que tem aí? O letreiro só diz banho... Como assim banho?"

    mc normal "Não se preocupe que quando a gente tava olhando os prédios eu consegui ver ali dentro. Tenho certeza que você vai adorar."

    mc charmoso "Certo. Agora feche os olhos e vamos entrar."

    show sayuri desesperada with dissolve

    s "E-eu realmente não gosto de ficar com os olhos fechados... Parece que alguma..."

    mc charmoso "Não seja boba, [s]. Confie em mim."

    s "..."

    show sayuri normal with dissolve

    s "T-tá..."

    mc "Fechou?"

    hide sayuri with dissolve

    s "Uhum..."

    mc "Me dá sua mão."

    s "Ai."

    mc "Que foi?"

    s "Nada. Só assustei..."

    mc "Certo. Agora vem por aqui."

    scene black with Dissolve(1.0)

    mc normal "Opa. Agora passa aqui."

    s "Tá."

    mc "Estamos quase lá."

    scene c_chinesa ofuro with Dissolve(3.0)

    "Uou! O lugar é incrível. Tão simples, mas tão incrível..."

    mc charmoso "Certo. Pode abrir os olhos."

    s "Ufa..."

    show sayuri assustada with dissolve

    s "Nossa! O que é isto, [mc]?"

    mc charmoso "É um banho zen. Você vai poder aproveitar um momento de relaxamento incrível. Só pra você."

    show sayuri normal with dissolve

    s "Você fez isso só pra eu relaxar?"

    mc envergonhado "Não é nada de mais..."

    "Tirando os C$ 299 que eu tive que pagar por uma hora... não foi nada..."

    mc normal "Agora você tem que ir ali naquela salinha e se preparar. A moça vai te ajudar."

    s "Tô um pouco nervosa..."

    mc normal "Fique tranquila. Ela vai te ajudar."

    s "Já volto."

    hide sayuri with dissolve

    "..."

    scene c_chinesa ofuro with hpunch

    s "Qu-quêêê?!"

    mc surpreso "!"

    s "{size=12}Eu não tenho coragem de usar isso...{/size}"

    "Eu consigo ouvir elas conversando..."

    s "{size=12}De jeito nenhum...{/size}"

    "Atendente" "{size=12}É normal, senhorita. Todo mundo usa.{/size}"

    s "{size=12}Nã-não...{/size}"

    "Atendente" "{size=12}E é uma forma de você agradar seu acompanhante também...{/size}"

    "Atendente" "{size=12}Com esse seu corpo perfeito, é impossível ele não adorar ver você vestindo isso.{/size}"

    s "{size=12}E-ele vai gostar?{/size}"

    s "{size=12}Hmm..{/size}"

    mc surpreso "..."

    if sayuri_intencao == "namoro":

        if sayuri_amizade >= 35:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("sayuri_e4_furdo","pixie","personagem")

            $ s4_ofuro = True

            s "{size=12}Tu-tudo bem...{/size}"

            s "{size=12}Se o [mc] vai gostar, eu faço por ele.{/size}"

            mc surpreso "!"

            s "{size=12}Vou me trocar. Pode ir, obrigada.{/size}"
        else:


            s "{size=12}Não tenho coragem! Me desculpe!{/size}"

            "Atendente" "{size=12}Tenha calma. Está tudo certo.{/size}"

            jump se4_ofuro_biquini
    else:


        s "{size=12}O [mc] é meu amigo. Ele não pensa nessas coisas quando está comigo.{/size}"

        label se4_ofuro_biquini:

            "Atendente" "{size=12}Se você prefere assim, pode usar este aqui então.{/size}"

        s "{size=12}Mas esse também...{/size}"

        s "{size=12}Ok. Eu aceito. Obrigada.{/size}"

    "..."

    s "[mc]? Estou saindo."

    mc envergonhado "O-ok!"

    if s4_ofuro:

        show sayuri f_desesperada with Dissolve(1.0)
    else:


        show sayuri b_assustada with Dissolve(1.0)

    pause

    s "E-e-eu!"

    mc surpreso "Uou!"

    s "Eles me obrigaram colocar essa roupa, [mc]..."

    mc envergonhado "E que que tem?"

    s "E-e-eu..."

    if sayuri_intencao == "namoro":

        mc charmoso "Não precisa ficar assim, [s]."

        mc "Você tá linda. Não quero parecer cafona, mas nunca fiquei tão sem palavras na minha vida igual agora."

        s "Estou... linda?"

        mc "Sim. Você tá incrível. Só de olhar pra você me deixa..."

        s "!"

        mc envergonhado "Desculpa..."

        s "Não!"

        if s4_ofuro:

            show sayuri f_aceitou with Dissolve(1.0)
        else:


            show sayuri b_vergonha with Dissolve(1.0)

        pause

        s "Eu... fiquei feliz, [mc]."

        s "É a primeira vez que alguém fala uma coisa assim pra mim..."

        s "Nunca... um homem me fez me sentir assim..."

        mc charmoso "Eu sou o homem mais sortudo do mundo de poder estar aqui agora vendo você."

        mc "Se todos os outros soubessem o que estão perdendo..."

        s "Você t-tá me deixando com muita vergonha..."

        mc "Tudo bem. Não é minha intenção. Só estou falando o que eu realmente tô sentindo."

        s "Ai..."

        mc normal "Mas eu quero quero que você relaxe. É por isso que tamo aqui."
    else:


        mc normal "Você não tem porque ficar envergonhada, [s]. Eu sou seu amigo."

        mc "Quero que você sinta confiança do meu lado."

        s "Eu também, mas é tão difícil..."

        s "Eu nunca me vesti perto assim de ninguém, [mc]. Nem meus pais... Só a [g] que me vê assim..."

        mc "Não seja boba. A gente vai se aproximar cada vez mais. Se quiser posso ficar só de cueca."

        if s4_ofuro:

            show sayuri f_aceitou with Dissolve(1.0)
        else:


            show sayuri b_vergonha with Dissolve(1.0)

        pause

        s "Não precisa! Seu bobo... hihi..."

        mc feliz "Agora sim."

        s "Obrigada, [mc]. Estou me sentindo melhor."

        mc normal "A maioria das garotas iriam se matar pra ter um corpo igual ao seu. Não precisa ter vergonha."

        s "Não me deixe mais envergonhada..."

        mc "Fechado. Deixa eu ficar quieto."

    mc feliz "Vem aqui sentir este banho incrível!"

    s "Tenho que confessar que eu estou empolgada. Parece realmente especial."

    mc normal "Com certeza."

    "Pelo preço é melhor que seja..."

    s "Vou entrar."

    if s4_ofuro:

        scene sayuri banheira_fudo with Dissolve(3.0)
    else:


        scene sayuri banheira_biquini with Dissolve(3.0)


    pause

    s "Aahh..."

    mc envergonhado "É bom?"

    s "É muito bom..."

    s "Eu tô me sentindo incrível, [mc]."

    s "Mu-muito obrigada."

    mc charmoso "Quero que você relaxe."

    s "Eu realmente estava precisando disso."

    mc desculpa "Sabe, [s]..."

    s "O que foi?"

    mc "Você carrega uma grande responsabilidade. Ser uma espécie de inspiração para todo um povo."

    mc "É uma coisa que eu nem imagino como é. Por isso..."

    mc normal "Por isso eu quero ser alguém que vai te ajudar a aguentar essa barra."

    mc charmoso "Quero que você confie em mim e se apoie em mim. Sempre que precisar."

    s "[mc]..."

    mc "Mas agora chega disso! Quero que você descanse e relaxe!"

    s "Hmm... tá muito gostoso aqui..."

    mc "É essa a ideia."

    label say4_premium1:

        pass

    menu:
        "Vou deixar você sozinha (+18)":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_44

                jump say4_premium1

            mc charmoso "Vou dar um tempo pra você relaxar em paz."

            mc "Quando acabar o tempo eu te aviso, tá?"

            s "T-tá..."

            if s4_ofuro:

                scene sayuri_ofuro_new1 with Dissolve(1.0)
            else:


                scene sayuri_ofuro_new2 with Dissolve(1.0)

            pause

            "O [mc] foi muito legal preparando tudo isso pra mim..."

            "Sorte que eu decidi ficar aqui mais um tempo com ele. Agora a Mestra... n-não vou pensar nela agora."

            "Eu tenho que relaxar agora."

            if s4_ofuro:

                scene sayuri_ofuro3 with Dissolve(1.0)

                pause

                "Não acredito que eu tive coragem de usar isso aqui na frente dele..."

                "Onde eu tô com a cabeça? Será que é culpa dele? Ele tá fazendo isso comigo?"

                "Ou será que é a [g] que tá fazendo eu ter mais coragem sobre esse tipo de coisa?"

            "De uns tempos pra cá eu tô sentindo umas coisas tão diferentes..."

            "Até hoje eu só foquei na ginástica, no meu treino, nas coisas da Cidade Chinesa..."

            "Só que agora... eu tô sentindo umas coisas diferentes... umas vontades que eu nunca tive antes."

            "As coisas que eu fiz no quarto... nossa... ah... só de pensar..."

            "Saber que o [mc] me viu vestida assim... eu tô sentindo de novo..."

            "Será que... hmm... ele disse que eu ia ficar sozinha..."

            menu:
                "Eu tenho que fazer...":


                    scene black with dissolve

                    scene sayuri_ofuro4 with Dissolve(1.0)

                    pause

                    "Eu não sei o que eu faço... o [mc] tá aqui do lado... me esperando..."

                    "Aposto que ele ia querer entrar aqui comigo. Tenho certeza."

                    "Ele tava aqui do lado enquanto eu tava aqui... com essa roupa escandalosa..."
                    scene snew_ani05 with Dissolve(1.0)
                    "Ahnn..."

                    "Ele tava me olhando praticamente sem roupa... aposto que ele adorou..."

                    "Ah... eu tava provocando ele... nnhhg... eu quando eu penso nisso..."

                    "... eu tenho vontade de tocar aqui..."

                    menu:
                        "Bem rapidinho...":


                            scene sayuri_ofuro5 with Dissolve(1.0)

                            pause

                            "Se for só um pouco... n-não tem problema..."

                            "Eu tenho que ficar quieta... pro [mc] não me ouvir... enquanto eu... aahnn!"

                            "Se ele descobrisse que eu me sinto assim... ele ia achar que eu sou uma safada..."

                            "Ahnn! N-não, [mc]! Eu não sou assim... e-eu..."

                            scene sayuri_ofuro6 with Dissolve(1.0)

                            pause

                            "Eu não consigo... você tem que entender, [mc]... é mais forte que eu..."

                            "Eu nunca fui assim, mas agora... a culpa é sua... você me faz ficar assim!"
                            scene snew_ani06 with Dissolve(1.0)
                            "Agora não reclama! Você vai ter que ficar com uma tarada! Aaannhh!"

                            "Assim! Você vai ter que me ajudar!"

                            "Nnhg!"

                            "Mais rápido, [mc]!"

                            scene sayuri_ofuro7 with vpunch

                            pause

                            "Assim! Nesse lugar que eu gosto!"

                            "I-isso! Com jeitinho! Nnng!"
                            scene snew_ani10 with Dissolve(1.0)
                            "O que eu t-tô fazendo?! E-eu tenho que parar!"

                            s "Isso! Não para! Continua, [mc]!"

                            s "Nng! Nhaanng! AANNG!!"

                            scene sayuri_ofuro8 with vpunch

                            pause

                            s "AANNNNG!!!"

                            s "{i}puf puf{/i}"

                            s "Aaah...."
                            scene snew_ani07 with Dissolve(1.0)
                            s "Que delícia..."

                            mc "[s]? Você me chamou?!"

                            s "N-não!"

                            "Minha nossa! Cadê minha roupa?!"

                            scene black with vpunch
                        "Pode parando aqui!":


                            scene sayuri_ofuro4 with vpunch

                            "N-nem pense nisso, [s]! O que a Mestre ia achar de você!?"

                            "E-eu... eu preciso parar com isso..."

                            "Eu vou... me trocar e relaxar... é isso..."

                            scene black with dissolve

                            "Fechar os olhos..."

                            pause
                "Eu preciso me controlar!":


                    "O que eu tô pensando?! Num lugar assim?!"

                    "[s]... coloca a cabeça no lugar. Isso é loucura."

                    "Eu vou relaxar..."

                    scene black with dissolve

                    "Fechar os olhos..."

                    pause
        "Vou ficar aqui do lado":


            "Vou ficar quieto e só deixar ela relaxar."

            window hide
            with dissolve

            pause

            "..."

            "..."

            "Talvez ela tenha dormido..."

            "Epa. Já passou uma hora. Melhor eu acordar ela."

    mc envergonhado "[s]... Acho que acabou o tempo..."

    s "Ah!"

    s "Hmmmm...."

    s "A-acho que eu dormi."

    mc normal "Não tem problema. Era essa a ideia."

    s "Vou levantar."

    scene c_chinesa ofuro with Dissolve(1.0)

    if s4_ofuro:

        show sayuri f_aceitou with Dissolve(1.0)
    else:


        show sayuri b_vergonha with Dissolve(1.0)

    s "Foi muito bom, [mc]. Muito obrigada."

    mc normal "Você tá parecendo renovada mesmo."

    s "Sim. Eu tô-"

    if s4_ofuro:

        show sayuri f_desesperada with hpunch
    else:


        show sayuri b_assustada with hpunch

    s "!"

    if s4_ofuro:

        show sayuri f_desesperada at direita with move
    else:


        show sayuri b_assustada at direita with move

    mc desconfiado "Que foi?"

    show mestra normal with Dissolve(1.0)

    mes "Olá, [s]. Se divertindo?"

    s "Me-mestra?! Po-po-por quê?! Como?!"

    $ mes_nome = "Mestra"

    mes "Você vai mesmo se dirigir a mim nesse traje?"

    s "Me-me perdoe!"

    hide sayuri with moveoutright

    mes "E você?"

    mc serio "..."

    show fenju acuada at entra_esquerda with dissolve

    fen "..."

    mes "Quem deixou você entrar, [fen]?"

    fen "Eu só queria..."

    mes "Calada. Vai me desrespeitar também?"

    fen "..."

    mes "Você está sendo uma péssima influencia para a [s]."

    mes "Eu sei que você acha que gosta dela, que faz ela feliz, mas não se engane."

    mes "Ela só está usando você para escapar da realidade. Como se fosse viciada em uma droga."

    mc bravo "..."

    mes "Você não passa de uma muleta. Um refúgio. Não se sinta especial. Podia ser qualquer um."

    menu:
        "...":


            mc bravo "..."

            "Essa desgraçada tá me deixando puto, mas xingar ela só vai piorar a situação. Eu tenho que me controlar pela [s]."

            mes "Pode fazer essa cara o quanto quiser."
        "Cale a boca!":


            $ s4_mestra_xingou = True

            mc bravo "Cale a sua boca, velha. Eu não quero saber da sua opinião sobre nada."

            "Eu sei que tratar ela assim só vai piorar as coisas, mas não aguento."

            show mestra diabolica with dissolve

            mes "Que graça. Acha mesmo que suas palavras têm qualquer peso?"

    mes "Você não passa de um qualquer que está sendo usado pela minha aluna indisciplinada."

    mes "Meu assunto é com a [s] e não com você."

    mes "Vou pegá-la. E você tome cuidado com ele, [fen]."

    hide mestra with dissolve

    hide fenju with dissolve

    show fenju acuada with dissolve

    fen "..."

    mc desconfiado "Você é a garota que a gente encontrou antes..."

    fen "Senhor..."

    mc "Oi?"

    fen "E-eu... vi a senhora [s] na banheira e falando com você. E eu nunca vi a [s] sorrindo antes."

    fen "Eu acho que a [mes]... e-ela tá errada sobre isso."

    mc "Você nunca viu a [s] sorrir?"

    fen "Nã-não! Nunca! Ela... ela... é minha disciplinadora... ela não pode..."

    mc "Disciplinadora? Como assim?"

    fen "Ela-"

    show mestra normal with moveinbottom

    show sayuri pensando at entra_direita with dissolve

    mes "Calada, [fen]."

    show fenju acuada at esquerda with move

    fen "Si-sim, [mes]!"

    mes "Chega dessa palhaçada toda. Vocês duas estão passando dos limites aceitáveis."

    mes "Ah! E você vai se ver comigo, [s]. Você vai... Faz tempo a última vez que eu tive que te corrigir."

    s "N-não, [mes]! Por favor!"

    mes "Calada!"

    show sayuri triste with dissolve

    s "..."

    "Essa velha é uma desgraçada... Corrigir? Que merda isso quer dizer? Ela deixou a [s] desesperada."

    mc bravo "..."

    mes "E acho bom a [fen] ver. Porque a hora dela vai chegar também depois de hoje."

    fen "{size=15}Aiin...{/size}"

    "Alguma coisa tá me deixando muito triste, desesperado, não sei. Vou ter que deixar a [s] sozinha com essa velha maldita?"

    if v6_fim:

        "Vou ter que deixar ela ir igual a [c] aquela vez na praia quando o Gustav e o Marco levaram ela?"

    mc irritado "Não!"

    "[mes], [fen] e [s]" "?!"

    mc bravo "Vem comigo, [s]! Me dá sua mão! Vamos correr daqui!"

    show sayuri assustada with hpunch

    s "[mc]! E-espera!"

    mc "Não! Vem comigo!"

    s "Ei!"

    hide sayuri assustada with moveoutright

    show black with moveinleft

    mes "Voltem aqui vocês dois!"

    mc serio "Vem, [s]!"

    scene black with hpunch

    s "O que você tá fazendo, [mc]?!"

    scene black with hpunch

    mc "Vem comigo!"

    scene black with hpunch

    "..."

    scene black with hpunch

    "..."

    scene c_chinesa rua with hpunch

    show sayuri desesperada with hpunch

    s "Para, [mc]! Minhas pernas tão tremendo! Não consigo mais..."

    mc triste "[s]..."

    mc serio "Eu vou te carregar. Não quero parar agora. Quero ir o mais longe possível dessa velha."

    mc preocupado "Por favor... vem comigo..."

    s "[mc]! Isso é loucura!"

    mc "Por favor..."

    s "..."

    s "Tá..."

    hide sayuri with dissolve

    scene c_chinesa rua

    show sayuri cavalinho with Dissolve(1.0)

    pause

    mc "Vem! Vamos sair daqui!"

    s "O que você tá pensando!?"

    mc "Eu vou te salvar dela, [s]!"

    show sayuri cavalinho with hpunch

    s "[mc]..."

    show sayuri cavalinho with hpunch

    "..."

    show sayuri cavalinho with hpunch

    s "Você tá indo rápido demais."

    "Eu preciso salvar ela! Não quero ver ela com essa maldita!"

    "O senhor do lámen tá contando comigo!"

    show sayuri cavalinho with hpunch

    s "Cuidado, [mc]! Eu vou-"

    scene sayuri caindo with hpunch

    s "Ai!"

    mc angustiado "[s]!"

    s "Aiii..."

    "Droga! O que eu tô fazendo?!"

    mc "[s] por favor me desculpa. Eu vou te ajudar..."

    s "Opa!"

    scene c_chinesa lateral with Dissolve(1.0)

    show sayuri pre_beijo with Dissolve(1.0)

    pause

    mc "De-desculpa... Eu..."

    s "Tudo bem, [mc]..."

    mc "Eu não sei o que deu em mim. Eu só queria..."

    mc "Proteger você daquela velha..."

    s "..."

    mc "..."

    if sayuri_intencao == "namoro":

        $ sayuri_e4 = "namoro"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("sayuri_e4_namoro","pixie","personagem")

        "A gente tá tão perto... mas ela continua colada em mim..."

        "Ela tá tremendo... eu também..."

        "Por que eu tive que estragar tudo?"

        "Se eu não tivesse ferrado tudo, talvez eu pudesse beijar ela ago-"

        scene sayuri c_beijo with Dissolve(3.0)

        pause

        mc "Say..."

        s "Me beija..."

        "..."

        "..."

        scene sayuri c_beijo_dois with Dissolve(2.0)

        pause

        "Tão frágil, mas tão forte."

        "Nem sei por quanto tempo a gente tá se beijando."

        "Eu sinto tanta paixão, mas tão delicada... Como se este é o primeiro e também o último beijo que a gente vai dar."

        "É doce, mas tão terrível..."

        window hide

        pause

    scene c_chinesa lateral with Dissolve(1.0)

    show sayuri normal with dissolve

    s "Eu preciso ir."

    mc preocupado "[s]..."

    s "Obrigada, [mc]."

    hide sayuri with dissolve

    mc "..."

    "Não falei nada. Não consegui."

    "Não tinha nada pra falar."

    "..."

    scene c_chinesa predios with Dissolve(1.0)

    "Ela se foi... provavelmente voltar pra velha filha de uma puta..."

    "E eu só fiquei olhando ela ir..."

    if v6_fim:

        "Mais uma vez eu deixei uma garota ser levada sem poder fazer nada..."

    "O que será que vai acontecer com ela?"

    "Será que eu devia ter feito tudo isso? Ter fugido da velha com ela? Eu fiquei tão nervoso na hora."

    "Ela me agradeceu... mas agradeceu pelo quê?"

label sayuri_e4_chinatown:

    "Agora só me resta dar o fora daqui e voltar pra ilha."

    $ tempo += 1

    scene black with Dissolve(1.0)

    "..."

    scene c_chinesa entrada_chinatown with Dissolve(1.0)

    "Aquela entrada parece bem misteriosa..."

    if s4_chinatown:

        "A [s] disse pra eu não ir lá. Mas eu não senti nenhuma firmeza no jeito dela."

        "Parece que ela queria me esconder alguma coisa."

    "Será que eu devo dar uma olhada?"

    menu:
        "Tô cansado. Melhor não me meter em mais furada.":


            mc concentrando "Tô cansadão... vou é voltar pra casa e deixar essas teorias pra outra hora."

            jump sayuri_e4_finalizar
        "Tenho que investigar isso.":


            mc desconfiado "Esse lugar me deixou intrigado de verdade. Tá meio tarde, mas acho que vou dar uma passada rápida."

    "..."

    scene chinatown entrada with Dissolve(2.0)

    pause

    "Uou. Parecia menor lá de cima."

    mc desconfiado "Ué... Tem um portão fechado."

    "Tem várias luzes saindo do outro lado desse corredor... que estranho."

    show bao normal with moveinbottom

    chi "Oi, jovem."

    mc surpreso "AH!"

    mc "Se-senhor do lámen!"

    chi "Boa noite."

    mc concentrando "O senhor me assustou."

    chi "O que faz aqui?"

    mc desculpa "Achei esta entrada estranha e resolvi dar uma olhada."

    chi "Você realmente tem um talento natural para se embrenhar em encrenca, não é?"

    mc desconfiado "Por que encrenca?"

    mc "Seja como for, o portão tá fechado. Não adianta pensar muito sobre isso."

    chi "Ele está fechado, mas não por muito tempo."

    mc "Como?"

    chi "Estou aqui justamente para abrir."

    mc surpreso "O senhor?!"

    chi "Com licença."

    hide bao with dissolve

    "..."

    "{i}Grraack! Inheeeek{/i}"

    "..."

    show bao normal with dissolve

    chi "Pronto."

    mc surpreso "..."

    hide bao with dissolve

    chi "Você vem?"

    mc "E-eu?!"

    menu:
        "Entrar no corredor com o velho":


            $ s4_chinatown_visita = True

            mc preocupado "Eu vou sim."

            "Espero que eu não teja indo pra minha cova..."

            scene black with Dissolve(1.0)

            "..."

            "Muito barulho. Muita luz..."

            scene chinatown arco with Dissolve(2.0)

            chi "Isso. Agora vire aqui."

            "O barulho está ficando ensurdecedor. Música, pessoas gritando..."

            "As luzes estão ficando mais intensas..."

            chi "Assim como meu lámen, sua primeira visita à China Negra é inesquecível."

            "..."

            chi "Chegamos."

            mc surpreso "!"

            scene chinatown normal with Dissolve(3.0)

            pause

            mc surpreso "O-o-o... que lugar é esse?"

            show bao normal with dissolve

            chi "Sua reação é natural. Logo você acostuma."

            chi "Mas agora tenho que te deixar pois tenho o bar para abrir."

            chi "Inclusive. Vou pedir que você vá. Não é bom que você faça sua primeira visita sozinho."

            mc serio "Mas eu quero-"

            chi "Não seja cabeça dura, jovem. Escute este velho."

            chi "Lhe trarei aqui em uma próxima oportunidade."

            mc desculpa "Certo..."

            chi "Agora vá. Quero ver você saindo."

            "Esse velho é esperto..."

            mc normal "Obrigado por me mostrar até aqui."

            chi "Não estou fazendo isso por você. Mas pela minha querida Ai."

            mc desconfiado "Qual é sua relação com a..."

            chi "Deixemos isso para outra hora."

            mc desculpa "Ok... Vou indo."

            chi "Boa noite."

            mc "Até."

            hide bao with dissolve

            "..."

            scene chinatown arco with Dissolve(1.0)

            "Um lugar como este... escondido embaixo da Cidade Chinesa..."

            "O que isso quer dizer?"

            jump sayuri_e4_finalizar
        "Dar o fora enquanto há tempo":


            mc desculpa "Na verdade acho que é melhor eu dar o fora, viu."

            chi "Eu acho uma excelente ideia. O que tem depois deste corredor não é para qualquer um."

            chi "Boa noite, jovem."

            mc envergonhado "Boa noite, velho."

            jump sayuri_e4_finalizar

label sayuri_e4_finalizar:

    "..."

    scene black with Dissolve(1.0)

    "..."

    play sound "audio/som_5_cidadenoite.mp3"

    scene mapa cidade_noite with Dissolve(1.0)

    "Meu encontro com a [s] foi muito especial. Foi a primeira vez que a gente passou tanto tempo juntos."

    "Conseguimos conversar sobre várias coisas."

    "Conhecemos o senhor do lámen e ela me falou sobre a cidade também. Tive um pouco de contato com a cultura dela."

    if sayuri_e4 == "amizade" or sayuri_e4 == "namoro":

        "Eu tentei relaxar ela com um banho zen, mas a chegada da treinadora dela acabou com tudo."

        "Aquele final foi dramático."

        if sayuri_e4 == "namoro":

            "A gente acabou se beijando... Foi incrível."

        "Mas eu sinto que nosso encontro acabou de forma abrupta. Ela saiu sem falar nada."

        "A mestra... a tal da [fen] também."

        "A [s] parece estar envolvida com algo muito muito grande."

    "As Olimpíadas estão chegando e ela disse que talvez não participe. Será que ela não está em forma pra competir?"

    "..."

    mc desculpa "Espero que tudo acabe bem."

    $ v11_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v11_fim","sayuri","personagem")

    scene black with Dissolve(1.0)



    scene sayuri_quarto with Dissolve(1.0)

    label say4_premium2:

        pass

    menu:
        "O que será que a [s] tá pensando?":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_45

                jump say4_premium2

            s "Nem acredito que hoje eu tive um encontro com o [mc]."

            "Eu consegui mostrar a Cidade Chinesa pra ele... foi tão legal."

            "Eu tenho tanto orgulho do nosso lugar. E poder mostrar isso..."

            "{i}toc toc{/i}"

            s "Q-quem é?"

            g "Sou eu, mana."

            s "[g]... pode entrar."

            scene sayuri_quarto2 with Dissolve(1.0)

            g "Que bom que você não dormiu ainda. Eu queria assistir um filme com você."

            s "F-filme?"

            g "Não pode? Faz tanto tempo que a gente não tem um tempo pra gente... você parece ocupada esses dias..."

            "A [g] parece mais carente esses dias... será que é por que eu tô saindo com o [mc]?"

            "Ela fica me agarrando pela casa... às vezes até passa do razoável..."

            "Às vezes pode até passar a impressão errada pras pessoas. A gente não é irmã de sangue, mas isso não importa."

            "Não quero que os outros achem que a gente é estranhas... alguma coisa assim... credo..."

            "Mas eu sei que é o jeito dela. No fundo ela gosta de mim... eu não quero afastar ela também. E agora?"

            menu:
                "Aceitar assistir o filme":


                    s "{i}pufff{/i}"

                    s "Tem razão. A gente precisa do nosso tempo também."

                    g "Eba! Eu trouxe meu notebook."

                    scene black with dissolve

                    scene sayuri_quarto15 with Dissolve(1.0)

                    pause

                    g "Faz tanto tempo que a gente não assiste um filme assim..."

                    s "J-júlia? Você t-tá sem roupa?"

                    g "Eu tirei... tava incomodando a alça..."

                    s "Não é possível, [g]... imagina se alguém bate aqui e vê a gente assim?"

                    g "Qual o problema? A gente só tá vendo um vídeo juntas abraçadinhas..."

                    s "Essa é a questã-"

                    "Filme" "A-ahnn!"

                    s "!!!"

                    s "Q-que filme é esse, [g]?"

                    g "É uma comédia de adolescente. Tem umas cenas assim, mas é pouca coisa..."

                    s "Minha nossa..."

                    "Esse tipo de filme... a [g] não percebe essas coisas? Será que eu que tenho a mente poluída demais?"

                    "Às vezes ela não tem noção mesmo... ela só quer ficar comigo e eu fico pensando besteira..."

                    g "Mana..."

                    s "Hm?"

                    g "Olha aqui."

                    s "Q-que foi?"

                    scene sayuri_quarto16 with Dissolve(1.0)

                    pause

                    g "Tá gostando?"

                    s "S-sim... t-tem umas cenas... mas..."

                    g "Eu tô adorando."

                    s "Q-que bom..."

                    g "Principalmente porque eu tô com você."

                    s "Haha... eu também..."

                    g "Você é a pessoa que eu mais gosto no mundo."

                    s "O-obrigada... eu também gosto de você, [g]..."

                    g "Eu sei que você tem suas coisas... mas eu não quero que você me esqueça, tá?"

                    s "Eu não vou... não precisa ficar assim comigo... eu sempre vou ser sua irmã."
                    scene snew_ani11 with Dissolve(1.0)
                    g "A gente não é irmã de verdade, mana..."

                    s "[g]... você..."

                    g "Não. Eu não fico triste com isso. Você é minha mana do coração. Pra mim é melhor ainda."

                    s "Isso aí..."

                    g "Só que você... parece meio incomodada, sei lá... você não gosta de ficar assim comigo?"

                    menu:
                        "Você gruda demais. Melhor parar.":


                            s "O p-problema é que você gruda demais, [g]."

                            s "É melhor a gente parar por aqui hoje. E da próxima vez venha usando uma roupa decente por favor."

                            g "T-tudo bem, mana... não fica... brava comigo, tá? Eu não quero que você parede de gostar de mim."

                            s "Não vou parar. Boa noite."

                            g "B-boa noite."
                        "T-tudo bem...":


                            s "N-não é isso... é só que... tudo bem..."

                            g "Certeza?"

                            "Eu não posso ficar pensando besteira e descontar nela."

                            s "Tá tudo bem... a gente se gosta... é normal fazer carinho."

                            g "Você me entende, mana... eu gosto... tanto de ficar com você."

                            s "Eu também..."

                            g "Ah... vem aqui..."

                            scene black with dissolve

                            s "J-júlia?!"

                            scene sayuri_quarto17 with Dissolve(1.0)

                            g "Ai, mana... quando você fala assim..."

                            s "[g]... v-você tá perto demais..."

                            g "Eu adoro ficar pertinho de você assim... sentir seu cheiro, mana..."

                            s "Esse tipo de coisa..."

                            g "Eu sei que pode parecer estranho... mas agora eu sei que você gosta de ficar comigo também..."

                            s "S-só não podemos levar pro lado err-"
                            scene snew_ani12 with Dissolve(1.0)
                            g "Eu quero passar cada vez mais tempo com você... mais perto... você me entende, né?"

                            s "É..."

                            g "Fala que você me entende. Que você vai ficar comigo, fala."

                            s "S-sim..."

                            g "Que bom... você me deixa tão feliz... eu sinto uma coisa aqui... hmm..."

                            s "[g]... não tem problema a gente ficar juntas... abraçadas... só q-"

                            g "Eu preciso abraçar você, mana!"

                            s "J-júlia?!"

                            scene black with vpunch

                            g "Eu quero sentir seu coração!"

                            s "O que você tá fazendo, louca?!"

                            g "Hahaha!"

                            scene sayuri_quarto18 with vpunch

                            pause

                            g "Você é gostosa, mana! Sabia?!"

                            s "Me solta, [g]!"

                            g "Eu deixo você sentiu o meu depois!"

                            s "E-eu não quero! Me solta!"

                            g "Mana! Por favor!"

                            s "Eu disse me solta! Agora!"

                            g "!!!"

                            g "D-desculpa!"

                            scene black with vpunch

                            g "E-eu não sei o que deu em mim! Desculpa!"

                            s "N-não! E-"

                            g "Boa noite, mana!"

                            scene sayuri_quarto19 with Dissolve(1.0)

                            s "[g]! Espera!"

                            "{i}KABLAM{/i}"

                            s "Ai! A porta!"

                            "Por que ela saiu correndo desse jeito?"

                            "E o que foi tudo isso... o que que passa na cabeça dessa menina?"

                            "A [g]... sempre foi super apegada em mim, só que... nunca desse jeito..."

                            "Eu não imaginei que eu sair com o [mc] ia deixar ela tão estranha assim..."

                            "Será que é isso? É bom eu tomar cuidado com ela... mas sem deixar ela se sentir sozinha e desamparada..."

                            "Não vai ser fácil..."

                            "E por que eu deixei ela fazer tudo isso comigo? Quando ela tava perto..."

                            "D-deixa eu dormir... é m-melhor que ficar pensando besteira..."
                "Melhor não":


                    "Eu sei que se eu aceitar ela vai vir com alguma coisa estranha."

                    "É melhor eu cortar logo no começo."

                    s "Desculpa, [g], mas eu tô cansada de hoje. Pode ser outro dia?"

                    g "Tudo bem... mas não esquece de mim, tá?"

                    s "Claro. Eu nunca vou esquecer."

                    g "Então tá..."
        "Deixa pra lá...":


            pass

    scene black with Dissolve(1.0)

    $ tempo += 1

    jump call_cidade



label sayuri_evento1:

    show black with dissolve

    mc triste "..."

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s1_save", extra_info="s1_save")

    $ iconchefe += 1

    "{i}puf{/i}"

    scene chinatown caminho with Dissolve(2.0)

    pause

    mc angustiado "..."

    "{i}puf{/i}"

    mc angustiado "O que o [mc] de uma hora atrás tinha na cabeça quando resolveu vir pra cá andando?"

    "Não é à toa que ninguém nunca encontrou esse lugar..."

    "É preciso subir tipo 10 quilômetros de montanha pra chegar aqui perto. E ainda nem consigo..."

    scene black with dissolve

    "..."

    mc surpreso "UOoOoU!"

    scene chinatown templo with Dissolve(2.0)

    play sound "audio/som_10_templo.mp3"

    mc surpreso "Olha só pra isso!"

    "É como se eu tivesse num filme japonês!"

    "Nunca vi nada parecido... Nunca imaginei que existissem construções assim em nosso país."

    "É realmente um achado. Se eu contar isso pro meu chefe ele vai pirar."

    "..."

    scene chinatown templo_lateral with Dissolve(1.0)

    pause

    "É realmente muito bonito."

    "O estranho é que não tem ninguém aqui. O lugar está vazio. Parece o cenário de um filme de terror."

    "E o vento... muito forte. Parece que o assobio tá dentro do meu ouvido."

    mc surpreso "..."

    mc surpreso "Tem alguém ali!"

    scene sayuri cena_templo with Dissolve(2.0)

    pause

    mc surpreso "É..."

    mc surpreso "Uma garota!"

    "É uma garota. Parece que ela tá dançando."

    "O jeito que ela dança é tão leve. Parece que tá voando sei lá."

    "Só ela... nessa imensidão de lugar."

    "Parece algo surreal. O que ela está fazendo aqui?"

    "Não sei se eu devo interromper ela... ou se eu chego perto sem chamar a atenção... Tenho que tomar cuidado, porque a primeira impressão é a que fica."

    menu:
        "Chegar mais perto e falar com ela":


            $ sayuri_amizade += 1

            "Seria estranho se ela visse um panaca parado em silêncio olhando para ela."

            "Eu ia parecer um tarado... Melhor falar com ela de uma vez."

            mc concentrando "Inspira... Tenha coragem [mc]."

            scene templo normal with Dissolve(1.0)

            show sayuri dancando
            with dissolve

            "..."

            mc normal "Olá?"

            mc normal "Tudo bem?"

            "Garota" "!"
        "Aproximar-se em silêncio":


            $ sayuri_seducao += 1

            $ sayuri_stalker = True

            "É melhor eu não chamar atenção. Ela pode ficar brava comigo se eu interromper o exercício dela."

            "Vou apenas chegar perto sem incomodar."

            scene templo normal with Dissolve(1.0)

            show sayuri dancando
            with dissolve

            "..."

            "Os movimentos são tão naturais."

            "Parecem aqueles exercícios de artes marciais."

            "Ela é magra, mas definida... E ela parece tão confiante, como se fizesse isso há anos."

            "..."

            show sayuri dancando_close
            with dissolve

            "Caraca! Ela é tão linda!"

            "O rosto é delicado, mas ao mesmo tempo ela tem uma expressão muito forte."

            "Eu reconheço esse rosto! É a [sc]!"

    show sayuri encrencada
    with hpunch

    mc surpreso "!"

    "Garota" "Socorro!"

    mc surpreso "Não! Não grite por favor!"

    "Garota" "Que-quem é você?! Se afaste!"

    mc triste "Ok! Não se preocupe. Meu nome é [mcc] e eu estou apenas visitando o templo."

    "Garota" "Você estava me observando?"

    if sayuri_stalker:

        mc preocupado "Eu tentei me aproximar, mas tive medo de atrapalhar."

        mc normal "Não era nada de mais. Eu juro."

        "Garota" "Quer dizer que você ficou me olhando, se-seu... e-e-e-esquisitão?!"

        mc desculpa "Me desculpe, eu só não sabia como eu devia chamar sua atenção."

        "Garota" "E eu ainda tô usando esse chapéu!"

        "Garota" "!"

        "Garota" "Você me viu dançando!"

        mc normal "Sim, me desculpe. Você estava tão linda dançando."

        "Garota" "!"
    else:


        mc normal "Não. Assim que te vi dançando eu te chamei."

        mc normal "Fiquei com medo que você me achasse um tarado."

        "Garota" "..."

        "Garota" "Ok... Obrigada por ter me chamado. Às vezes eu fico concentrada demais e acabo não vendo as coisas ao meu lado."

        mc normal "Eu entendo."

        "Garota" "De-deixa eu tirar meu chapéu..."

    show sayuri infeliz with dissolve

    "Garota" "..."

    mc desculpa "..."

    mc normal "Deixa eu começar de novo..."

    mc normal "Meu nome é [mcc]."

    menu:
        "Sou um jornalista que trabalha para uma revista sobre famosos.":


            $ sayuri_seducao += 1

            mc normal "Sou um jornalista que trabalha para uma revista sobre famosos."

            mc normal "Vim aqui checar a informação de que [sc] estava aqui. E aparentemente eu a encontrei..."

            s "..."

            s "Eu agradeço sua sinceridade."

            s "Mas e agora? O que pretende fazer sobre isso?"

            s "Vai revelar meu segredo para todo mundo?"

            s "..."
        "Ouvi falar sobre o templo e tive que vir conhecer.":


            $ sayuri_amizade += 1

            mc normal "Ouvi falar sobre o templo e tive que vir conhecer."

            mc normal "Nunca imaginei que encontraria a [sc] aqui."

            s "..."

            show sayuri surpresa with dissolve

            s "Ve-verdade?"

            "Melhor não contar toda a verdade pra ela. Ela ainda tá muito assustada comigo."

            mc "Sim. Eu ouvi falarem do templo enquanto andava pela Cidade Chinesa e fiquei curioso."

            s "Entendi..."

            s "É bastante raro alguém vir aqui."

            mc normal "Inclusive bem no meio da avenida principal tem uma placa sobre este templo. Não tô lembrando o nome agora..."

            s "Templo Jian Zi-Hao."

            mc feliz "Isso mesmo!"

            show sayuri c_incerta with dissolve

            s "Este templo é conhecido por poucos, mesmo estando perto da capital."

            s "Alguns monges que vivem na Cidade Chinesa revezam para manter o local limpo."

            s "Eu também ajudo de vez em quando."

            s "Eu gosto daqui porque é afastado das pessoas. É um lugar onde posso treinar em paz."

            s "Até hoje ninguém havia conseguido me ver aqui..."

    if sayuri_p1:

        $ sayuri_seducao += 1
        $ sayuri_amizade += 1

        mc charmoso "Não se preocupe, seu segredo ainda não vazou."

        mc charmoso "Não contei para ninguém ainda."

        s "Verdade?!"

        mc charmoso "Sim. Pode confiar em mim."

        s "Muito obrigada... Isso é realmente muito importante pra mim."

        mc normal "Não quero que sua vida vire um inferno por minha causa."

    s "Eu agradeceria muito se você não contasse sobre isso para ninguém..."

    if not sayuri_p1:

        "Se ela soubesse que eu já entreguei ela pro chefe..."

        "Mas não tenho como falar isso pra ela agora. Acabaria com qualquer chance de me aproximar dela."

        mc desculpa "Ok..."
    else:


        menu:
            "Não vou contar pra ninguém. Você tem minha palavra.":


                mc charmoso "Não vou contar a ninguém. Você tem minha palavra."

                label sayuri_e1_naoconta:

                    s "Sé-sério?!"

                $ sayuri_seducao += 1
                $ sayuri_amizade += 2
                $ sayuri_templo_abraco = True

                $ pautas -= 1
                $ sayuri_p1 = False

                mc desculpa "Eu percebi como o templo é importante pra você, então não vou contar pra ninguém."

                mc "Mesmo que isso complique minha vida no trabalho."

                s "..."

                scene sayuri templo_abraco with Dissolve(3.0)

                pause

                mc surpreso "..."

                mc "Sa-sa..."

                s "Mu-muito obrigada! O templo é tão importante pra mim!"

                s "Você não sabe como é complicado ter que ser a melhor ginasta do mundo..."

                s "O templo é tudo o que eu tenho..."

                s "Eu..."

                scene templo normal with hpunch

                s "Ai meu Deus! E-e-e-eu!"

                mc envergonhado "Calma calma..."

                s "E-e-eu... tava te te abraçando..."

                s "Me-me-me desculpe!"

                mc "Não se preocupe."

                mc normal "Você só ficou feliz. Tudo bem."

                s "..."

                show sayuri interessada with dissolve

                s "Mu-muito obrigada. Eu te devo uma."

                s "Isso é realmente muito importante para mim."

                mc normal "Eu entendo. Seu segredo está seguro comigo."

                "Depois de prometer isso, não vou poder mais entregar essa pauta pro chefe."

                "Uma pauta a menos pra me segurar no emprego..."
            "Me desculpe, mas não posso garantir. É o meu trabalho.":


                s "..."

                show sayuri infeliz with dissolve

                s "... Eu acho que entendo."

                mc normal "Mas não quero que isso seja um empecilho para a gente se conhecer."

                s "... Ok..."
            "Mesmo me prejudicando no trabalho, vou quebrar esse galho.":


                mc charmoso "Meu trabalho é conseguir informações sobre as celebridades, mas vou fazer essa pra você."

                jump sayuri_e1_naoconta

    mc normal "Independente disso, eu gostei bastante do templo."

    mc normal "Parece um lugar desconectado do resto da cidade. Como se eu tivesse entrado em outra dimensão."

    show sayuri meudeus with dissolve

    s "Não exagere..."

    mc feliz "É sério! Olhe para essa construção. Nunca tinha visto algo assim antes!"

    s "Talvez você tenha razão... Para quem nunca viu um templo chinês antes..."

    menu:
        "Chinês!? Certeza que não é japonês?":


            mc desconfiado "Chinês!? Certeza que não é japonês?"

            show sayuri infeliz with dissolve

            s "Tenho..."

            menu:
                "Eu já assisti anime demais para saber que não é chinês.":


                    mc concentrando "Eu já assisti anime demais para saber que não é chinês."

                    show sayuri c_incerta with dissolve

                    s "Aparentemente sua cultura é bem limitada, como eu havia imaginado."

                    s "Com licença, mas tenho que ir embora agora."

                    mc angustiado "Ei! Espere..."

                    s "Com licença..."

                    jump end_y
                "Eu acredito em você.":


                    mc desconfiado "Eu não sou tão ligado em cultura oriental. Já tinha visto alguma coisa sobre Japão."

                    s "Sim. A cultura japonesa é mais famosa que a chinesa no ocidente, mas isso está mudando."
        "Mesmo tendo visto em fotos, é a primeira vez ao vivo.":


            $ sayuri_amizade += 1

            mc feliz "Mesmo tendo visto em fotos, é a primeira vez ao vivo."

            s "Eu entendo."

            s "A cultura chinesa ainda está aos poucos chegando ao ocidente."

    s "Eu me mudei para cá e me naturalizei muito nova, mas sempre quis manter as raízes com a China, que é onde eu nasci."

    mc charmoso "Eu acho incrível."

    s "Obrigada, mas realmente é o mínimo que eu posso fazer."

    "..."

    s "Olha a hora. Tenho que ir pra casa."

    mc desculpa "Desculpa por ter estragado seu exercício."

    show sayuri interessada with dissolve

    s "Tudo bem."

    s "Na verdade, fazia tempo que uma pessoa não falava comigo assim."

    mc desconfiado "Assim como?"

    s "Como uma pessoa normal."

    s "A maioria das pessoas que vem até mim querem tirar foto ou que eu autografe alguma coisa."

    s "É muito raro alguém conversar comigo como uma pessoa qualquer."

    mc feliz "..."

    s "Foi... agradável."

    s "Hmm... Uma última coisa."

    mc normal "Pode falar."

    s "Será que eu podia... ter seu telefone?"

    mc desconfiado "?"

    s "Seu número quero dizer..."

    mc feliz "Ah! Com certeza!"

    mc normal "..."

    mc normal "Aqui está."

    s "Não vou incomodar?"

    mc normal "Claro que não."

    s "Ok. Se... eu quiser conversar com alguém de novo eu te aviso."

    mc normal "Tudo bem. Pode me mandar uma mensagem quando quiser."

    s "..."

    hide sayuri with dissolve

    "..."

    "Que garota estranha..."

    "Ela parece não ter muito jeito com as pessoas."

    "Eu achei que tudo correu bem. Tomara que eu tenha causado uma boa primeira impressão."

    scene templo frente with dissolve

    "Bom... Esse templo já deu o que tinha que dar."

    "Tô pronto pra voltar pra cidade."

    "Pensando bem... Acho que eu devia ter pego o número dela também..."

    "E se ela nunca mais falar comigo?"

    $ sayuri_evento1_check = False

    mc zerado "..."

    scene black with Dissolve(2.0)

    pause

    scene sayuri_quarto with Dissolve(1.0)

    menu:
        "O que será que a [s] tá pensando?":


            "Ufa..."

            "Ter que falar com aquele moço no templo quase acabou comigo... eu preciso deitar um pouco."

            scene sayuri_quarto1 with Dissolve(1.0)

            "Fazia tempo que eu não falava com um estranho daquele jeito... eu fiquei com tanto medo."

            "Pensando bem... até que ele foi legal. Pra alguém de fora, ele foi bem respeitoso..."

            "Depois de tanto tempo sem conversar com alguém assim... eu não sei o que deu em mim aquela hora."

            "Eu acabei pedindo o telefone dele. Ai... o que eu vou fazer com isso agora? Eu nem tenho telefone."

            "E eu não quero emprestar de novo... que burrada..."

            "{i}toc toc{/i}"

            "???" "Posso entrar?"

            s "C-claro."

            scene sayuri_quarto2 with Dissolve(1.0)

            s "V-você tá andando com essa roupa pela casa?"

            "???" "Que que tem? Não é tão diferente da sua."

            s "Ai! M-mas eu tô só aqui. Eu não saio assim por aí."

            "???" "Deixa disso. Por que você tava com uma cara estranha?"

            s "C-como assim cara estranha? Você tava me... é... xeretando?"

            "???" "Você tem essa mania de deixar a porta aberta. Daí de vez em quando..."

            s "Esse é um péssimo hábit-"

            "???" "Eu sei! Eu sei! Mas eu não consigo!"

            s "Então... eu conheci um rapaz hoje n-"

            "???" "Rapaz? Hmm..."

            s "P-para! A gente só conversou um pouquinho!"

            "???" "E mesmo assim você ficou com essa cara. Faz tempo que você não fala com um possível peguete, né?"

            s "P-possível peguete?"

            "???" "Eu conheço você, mana. Eu sei que esse rapaz fez alguma coisa aí."

            s "Impossível... a gente nem se conhece direito."

            "???" "Bom... tem razão. Vocês se verem de novo é praticamente impossível."

            s "B-bom... e-eu peguei o telefone dele..."

            scene sayuri_quarto2 with vpunch

            "???" "Q-quê?! Você pediu o telefone dele?!"

            s "E-eu também não sei por que eu fiz isso!"

            "???" "Uau... até eu fiquei molhada agora."

            s "Q-que... n-não fala essas coisas..."

            "???" "A gente vai comprar um telefone pra você e você vai ligar pra ele!"

            s "Comprar? Eu nunca tive telefone..."

            "???" "Você não vai querer ligar do meu pro seu namorado, né?"

            s "N-namorado?!"

            "???" "A gente vai resolver isso amanhã. E daí você marca com ele. Eu prometo que eu vou te ajudar, mana."

            s "Não sei, Ju-"

            "???" "Deixa comigo. Eu vou resolver tudo pra você. Pode confiar em mim."

            s "T-tá... mas olha lá... não vai exagerar..."

            scene black with Dissolve(1.0)

            "Pode deixar, mana. Eu vou resolver tudinho pra você. Depois dessa, a gente vai ensinar uma lição pra esse idiota."
        "Deixa pra lá...":


            pass

    $ dia += 2
    $ tempo = 1

    "{b}Dois dias depois{/b}"

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with Dissolve(1.0)

    mc desculpa "As coisas estão meio paradas. A [s] não me ligou obviamente..."

    mc "Também não encontrei nenhuma nova celebridade."

    mc normal "Pelo menos o chefe ainda não me despediu."

    if tempo <= 3:

        mc triste "Preciso fazer alguma coisa. Deixa eu dar uma saída pela ilha."
    else:


        mc concentrando "Preciso fazer alguma coisa, mas tô com tanto sono."

        mc "Acho que eu vou tentar sair..."

        jump cenario_casa

    jump call_cidade

label sayuri_evento2:

    $ estou_na_cidade = False

    $ tempo += 1

    if casa:

        scene ap sala with Dissolve(1.0)
    else:


        scene apartamento geral with dissolve

    "Muito bem."

    "Ela me pediu algumas horas, então tenho algum tempo até começar a me preparar. O que eu devo fazer?"

    "Ah! Claro... Ela é uma atleta. Vou pesquisar sobre o esporte dela e ter o que falar enquanto a gente come."

    menu:
        "Pesquisar sobre patinação":


            $ sayuri_estudou = "patinação"

            "Vou ler tudo o que eu puder sobre o tema."
        "Pesquisar sobre ginástica":


            $ sayuri_estudou = "ginastica"

            "Vou ler tudo o que eu puder sobre o tema."
        "Pesquisar sobre atletismo":


            $ sayuri_estudou = "atletismo"

            "Vou ler tudo o que eu puder sobre o tema."

    "..."

    "Toda vez que vou sair com alguém fico muito nervoso."

    "Mas claro!"

    "Minha história com as garotas não é nada boa..."

    mc zerado "Até hoje, acho que o máximo que eu falei com uma garota foi no encontro com a Priscila."

    "E ela é uma garota bem fácil de conversar. Ela é desinibida e acho que na maioria das vezes foi ela que puxou o assunto."

    mc triste "A [s] é uma história totalmente diferente..."

    "Ela é na dela e talvez seja ainda pior do que eu nessa questão de conversa."

    "Eu não faço a mínima ideia de como as coisas vão se sair nesse encontro."

    "Eu preciso pensar muito bem em como eu vou encaminhar nossa conversa. Pelo que eu percebi, ela é fechada, então uma {b}Abordagem{/b} muito direta pode assustar..."

    mc concentrando "Talvez o melhor seja eu ir devagar..."

    mc tarado "Por outro lado, talvez seja justamente isso que ela esteja buscando..."

    "Pensando bem, tenho que definir minhas intenções. Ela pode ser uma boa amiga, ou até algo mais..."

    "Se ela for mala, eu posso só usar ela como fonte de pautas. Eu pareço um cuzão pensando isso, mas eu preciso de pautas para o chefe."

    "..."

    mc surpreso "Olha a hora!"

    mc triste "Acabei enrolando demais... Bora tomar um banho e sair rapidão."

    "..."

    "..."





    scene restaurante jap_fora with Dissolve(2.0)

    "Eu ouvi sobre este lugar quando me mudei pra cá."

    "Precisava de algo pra comer enquanto não tinha fogão ainda e acabei gastando R$ 200 em um almoço."

    mc angustiado "..."

    "Ele é caro, mas acho que vale a pena neste caso."

    "..."

    scene tadaima restaurante with Dissolve(2.0)

    "O lugar é pequeno, mas é muito chique."

    "Opa, acho que é a garçonete."

    show garconete bemvindo
    with dissolve

    g "Bem-vindo, senhor. Deseja uma mesa?"

    mc normal "Na verdade eu tô esperando uma amiga. Eu queria reservar uma daquelas salas separadas, porque ela..."

    g "Ah! Acho que ela já está aqui, senhor."

    mc desconfiado "Sério?! Achei que tinha chegado cedo..."

    g "{size=15}Até que você é gato...{/size}"

    mc desconfiado "Hã? O que você disse?"

    g "Nada, senhor. Por favor, vou te levar até uma de nossas salas vip."

    "Eu tenho quase certeza que ela me chamou de gato. Será que tô ficando louco?"

    g "Sua amiga é uma jovem bem famosa. Por isso nós reservamos para ela uma sala especial."

    mc normal "Na verdade essa era minha ideia também. Eu achei que tivesse chegado antes dela."

    show garconete charmosa
    with dissolve

    g "Você parece ser um cavalheiro. Sua 'amiga' tem muita sorte de sair contigo."

    mc desculpa "Haha... Obrigado."

    g "Só estou falando a verdade. E a carcaça não é de se jogar fora."

    menu:
        "Muito obrigado. Você é linda também.":


            $ julia_seducao += 1

            mc charmoso "Muito obrigado. Você também é linda."

            mc charmoso "E esse quimono..."

            $ renpy.notify("A garçonete parece interessada em você...")

            g "Ele mexe com a imaginação, né?"

            mc charmoso "Pode apostar que sim."
        "Ah... Ok.":


            mc desconfiado "Ok..."

            g "..."

    "..."

    scene tadaima porta
    with dissolve

    g "Aqui estamos."

    show garconete charmosa
    with dissolve


    g "Aqui é a entrada da sala que reservamos para ela."

    mc normal "Valeu."

    g "Qualquer coisa que precisar, estou à sua completa disposição."

    "O que ela quer dizer com isso?"

    menu:
        "...":


            mc zerado "..."

            g "Qualquer coisa me chame."
        "Vou me lembrar disso.":


            $ julia_seducao += 1

            mc safado "Vou me lembrar disso."

            g "Pode me cobrar."

            mc safado "..."

    hide garconete with Dissolve(0.5)

    "Essa garota tá brincando comigo... Só pode."

    "Mas eu não tô aqui por causa dela. Preciso me concentrar na [s] ou vai dar merda."

    "Se bem que essa garçonete é linda e parece ter se interessado por mim."

    "Chega de pensar nela! A [s] já está aqui me esperando."

    mc concentrando "Vamos lá!"

    scene sayuri chegada with Dissolve(2.0)

    pause

    s "O-oi..."

    mc normal "Oi, [s]."

    menu:
        "Você está linda.":


            mc charmoso "Você está linda."

            s "Ah! Ah... O-obrigada..."

            "..."

            "Ela ficou meio sem jeito."
        "Que bom que você veio.":


            $ sayuri_amizade += 1

            mc normal "Que bom que você veio."

            s "Você também."

    s "Eu tava com um pouco de medo que você não viesse."

    mc normal "Por que eu não viria?"

    s "Não sei. Deixa pra lá."

    menu:
        "Esses bolinhos de arroz parecem muito bons...":


            $ sayuri_amizade += 1

            mc normal "Você viu na mesa? Esses bolinhos de arroz... hmm..."

            s "Parecem gostosos mesmo. Pra falar a verdade eu estou com fome."

            mc normal "Que bom. Você vai adorar a comida deles. Eu só comi uma vez, mas foi inesquecível."

            s "Sério?"

            mc normal "Sim."

            "Mais pelo preço do que pelo sabor..."

            "Mas não vou comentar isso e passar meu atestado de pobreza..."
        "Nenhum homem recusaria um encontro com uma garota como você.":


            mc charmoso "Pode ter certeza que menhum homem recusaria um encontro com uma garota como você."

            s "Ah!"

            s "..."

            mc charmoso "É sério. Você é famosa, bonita e tenho certeza que é inteligente ainda por cima."

            s "O-obrigada..."

            mc desconfiado "..."

            "Tudo o que eu falo ela fica envergonhada. Não sei se tô no caminho certo..."

            mc normal "Vamos comer esse bolinho de arroz?"

            s "Bo-boa ideia."

    scene tadaima vip with Dissolve(2.0)

    pause

    mc normal "Esses bolinhos de arroz parecem bons."

    s "Sim..."

    show sayuri interessada
    with dissolve

    s "..."

    s "São bons mesmo!"

    mc normal "Eu disse que você ia gostar."

    mc "Então, [s]. Sabe por que eu escolhi este lugar?"

    s "Não. Por que?"

    menu:
        "Por causa da sua origem japonesa.":


            mc normal "Por causa da sua origem japonesa, claro."

            s "..."

            show sayuri meudeus
            with dissolve

            s "Mas eu sou chinesa, [mc]."

            mc surpreso "Ah! É..."

            s "Mas eu agradeço por você tentar."

            s "Eu já percebi que você tem problema pra diferenciar as duas culturas."

            mc desculpa "Você vai me achar um idiota."

            s "Não! Não pense nisso..."
        "Porque aqui ninguém vai incomodar a gente.":


            $ sayuri_amizade += 1

            mc normal "Porque aqui é um lugar bem reservado."

            mc "Eu sei como pode ser cansativo ser conhecido."

            mc desculpa "Na verdade eu não sei, sei, mas eu devo imaginar como cansa."

            show sayuri surpresa with dissolve

            s "Isso..."

            s "Isso foi muito legal, [mc]. Muito obrigada."

            s "Eu acho que... Essa é uma das coisas mais gentis que já fizeram pra mim."

            mc normal "Acho que não é pra tanto, mas fico feliz."

            s "..."

    show sayuri infeliz with dissolve

    s "Na verdade, é bem raro eu fazer algo que eu goste."

    mc desculpa "Como assim?"

    s "..."

    s "Eu tenho os treinos, os campeonatos... É tanta coisa que eu preciso fazer..."

    mc preocupado "Isso é complicado, [s]... Venha, senta aqui comigo."

    s "Tá."

    scene tadaima local with Dissolve(2.0)

    mc preocupado "Você tava dizendo..."

    s "Ah..."

    s "É minha responsabilidade trazer..."

    "Meu Deus... Ela tá falando e nem reparou que nessa posição a saia não tá escondendo nada."

    mc envergonhado "Será que eu devo?"

    menu:
        "Olhar para baixo":


            $ sayuri_calcinha = True

            "Não tenho como evitar."

            "Seria até um desrespeito com ela ignorar um presente como este, não é verdade?"

            scene sayuri tadaima_calcinha with Dissolve(1.0)

            pause

            mc safado "..."

            "Essa situação tá me deixando doido. Se isso continuar eu..."
        "Continuar prestando atenção no que ela diz":


            "Não é hora de pensar em sacanagem!"

            "Ela está falando algo sério..."

            show sayuri infeliz with dissolve

            s "... medalhas para nosso país."

            s "Minha vida é praticamente a ginástica. E por isso eu acabo não conseguindo fazer coisas que talvez eu gostasse."

            mc desculpa "Deve ser realmente difícil. Mas agora a gente..."



    scene tadaima vip

    show garconete limpando with vpunch

    g "Olá!"

    mc surpreso "Ah!"

    g "Vocês estão precisando de algo?"

    s "..."

    menu:
        "Não estamos precisando de nada.":


            mc bravo "Você quase me matou do coração, isso sim."

            mc bravo "Não se preocupe que se precisarmos de algo eu lhe chamo."

            show garconete limpando with move:
                linear 0.5 xpos 300

            show sayuri interessada with dissolve

            show sayuri interessada with move:
                linear 0.8 xpos 1050

            s "Acho... acho que eu gostaria de algo para beber."

            g "E o que você quer, linda?"

            s "Um suco de morango, por favor."

            mc normal "Então, ok. Vou querer algo também."

            g "Vou trazer um sakê especial que temos para você."

            mc "Mas..."
        "Pode nos trazer uma bebida, linda?":


            $ julia_seducao += 1

            mc charmoso "Que bom que você veio."

            mc charmoso "Pode trazer uma bebida?"

            $ renpy.notify("A garçonete parece interessada em você...")

            g "Vou trazer um sakê especial que temos pra você."

            mc safado "Perfeito."

            g "Só isso que você quer de mim?"

            mc charmoso "..."

            mc "Por hora é isso."

            g "{size=15}Que pena...{/size}"

            if sayuri_calcinha:

                g "{size=15}E eu reparei você olhando bem no meio das pernas dela quando eu cheguei, viu?{/size}"

                mc envergonhado "..."

    g "Volto em breve."

    hide garconete with dissolve

    hide sayuri with dissolve

    show sayuri interessada with dissolve

    if julia_seducao < 1:

        mc bravo "Não estou gostando desta funcionária. Muito intrometida..."

        s "Ah... Acho que ela não faz por mal..."

        mc normal "Você que é legal demais."

    s "..."

    "Agora é uma boa hora para falar sobre o que eu pesquisei hoje."

    mc "Voltando ao nosso papo..."

    if sayuri_estudou == "ginastica":

        $ sayuri_amizade += 1

        mc normal "Eu estava lendo sobre ginástica esses dias."

        mc "Achei realmente incrível o que você e as outras atletas conseguem fazer."

        hide sayuri

        scene sayuri tadaima_surpresa with Dissolve(1.0)

        s "E-eu?!"

        mc feliz "Claro!"

        s "..."

        s "O-obrigada... Não é nada incrível, de verdade."

        mc charmoso "Você está sendo humilde demais. E olha que no seu caso é ainda mais grave."

        s "Mais grave?"

        mc "Sim. Você tem três medalhas olímpicas. Você é a atleta de maior sucesso no país inteiro!"

        s "Ah! E-eu..."

        mc "Não precisa ficar com vergonha. Você merece."

        scene sayuri tadaima_feliz with Dissolve(1.0)

        s "Obrigada, [mc]. Muitas pessoas me dão parabéns e torcem por mim, mas ouvindo você falar assim, parece diferente, especial."

        s "Na-na verdade! De-desculpa se eu falei algo estranho..."

        mc charmoso "Não falou nada estranho. Fiquei feliz por você sentir isso."

        s "..."
    else:


        scene tadaima local with Dissolve(1.0)

        mc normal "Eu estava lendo sobre [sayuri_estudou] esses dias."

        show sayuri meudeus with dissolve

        s "A é? É realmente um esporte bem bacana. Nunca tive tempo para ler sobre, mas parece legal quando eu vejo."

        mc triste "Como assim?"

        s "Como eu me dedico muito à ginástica, quase não sobra tempo para estudar a fundo outros esportes."

        "Não acredito! Li sobre o esporte errado! Eu sou uma mula!"

        mc desculpa "Haha! Eu imagino. A ginástica ocupa muito do seu tempo, né?"

        hide sayuri

        show sayuri infeliz with dissolve

        s "Nem me fale. É realmente uma grande parte da minha vida. Quase toda na verdade..."

        "Parece que ela está ficando triste. Melhor mudar de assunto."

    s "Falando nisso... "

    if sayuri_atencao > 0:

        scene tadaima local with Dissolve(1.0)

        show sayuri infeliz with dissolve

        s "Eu vi outros jornalistas no templo..."

        s "Você... contou sobre meu segredo para os outros?"

        mc angustiado "..."

        "Droga! É óbvio que isso ia acontecer! O chefe deve ter mandado outros confirmarem minha história."

        "E agora? Isso pode acabar com minha relação com ela. Tenho que tomar muito cuidado com o que vou falar agora."

        menu:
            "Sim. Me desculpe, [s].":


                $ sayuri_amizade -= 2
                $ sayuri_seducao -= 2

                mc triste "Sim. Eu... eu contei pro meu chefe."

                show sayuri infeliz with dissolve

                s "..."

                mc angustiado "Por favor, me escute, [s]!"

                mc desculpa "Me desculpa... Eu... Eu não queria ter que contar seu segredo."

                s "Você sabia que era um lugar especial pra mim."

                mc desculpa "Eu sei. Só que é como se eu tivesse sido obrigado."

                s "..."

                mc "Eu trabalho em uma revista de fofoca. É a única forma que eu tenho de viver aqui na capital."

                mc "Eu sei que eu fui um cuzão com você e estraguei seu lugar especial. Mas se eu não fizesse isso, eu ia perder meu emprego."

                mc "Eu ficaria sem dinheiro e teria que voltar pra a casa dos meus pais. Ficaria sem ver você."

                mc "Não quero que isso aconteça."

                show sayuri surpresa with dissolve

                s "Não... não quer... ficar sem me ver?"

                mc "Eu conheci você e outras pessoas interessantes aqui na capital."

                mc "Se eu perder esse emprego, eu vou ter que deixar você e todo o resto pra trás."

                mc "Não tô falando que eu tinha o direito de fazer o que eu fiz..."

                mc "Só queria que você entendesse que não fiz porque te odeio ou porque não ligo pra você."

                s "Eu..."

                show sayuri c_incerta with dissolve

                s "Acho que eu te entendo..."

                s "Eu fiquei muito triste com você. Mas esse é o seu trabalho."

                s "Se... Se eu quiser continuar vendo você, eu preciso me lembrar disso."

                mc "Obrigado. Obrigado por entender minha situação."

                menu:
                    "Prometo não fazer mais isso.":


                        $ sayuri_amizade += 1

                        mc "Mas eu prometo que eu não vou fazer isso com você de novo."

                        mc normal "Quero que você confie em mim."

                        mc "Você pode tentar? Pelo menos me dar uma chance?"

                        s "Eu... Vou te dar uma chance."

                        mc normal "Muito obrigado, [s]."
                    "...":


                        mc desculpa "..."

                s "..."

                "..."

                "O clima tá horrível. Preciso fazer alguma coisa ou tudo vai pro buraco."
            "Não. Eu nunca contaria seu segredo.":


                $ sayuri_p1_mentira += 1

                mc bravo "Claro que não!"

                mc desculpa "O segredo do templo está muito bem guardado, pode ficar tranquila."

                mc "Eu sei que é uma grande coincidência, mas você precisa acreditar em mim."

                show sayuri surpresa with dissolve

                s "Não... Não precisa ficar assim."

                s "Eu acredito em você, [mc]."

                s "Va-vamos mudar de assunto."
    else:


        scene sayuri tadaima_feliz with Dissolve(1.0)

        $ sayuri_amizade += 2

        s "Eu queria agradecer você."

        mc desconfiado "Me agradecer?"

        s "Eu ainda não vi nenhum jornalista ou pessoa estranha no templo depois que a gente conversou."

        s "Parece que você não contou meu segredo para ninguém."

        mc normal "Com certeza! Eu sei o quanto o templo é especial pra você. Eu não pretendo estragar isso."

        s "A gente ainda não se conhece direito, mas você parece um amigo, [mc]."

        mc "É isso que eu quero. Quero que você confie em mim e me veja como um verdadeiro companheiro que está do seu lado."

        s "O-obrigada..."

        "..."

        "Ela ficou com vergonha de novo..."

    "Meu Deus! Cadê nossa bebida? Seria a hora perfeita pra garçonete chegar..."

    "..."

    mc normal "Ah! Eu não sei se eu devia falar sobre isso, mas eu ri muito hoje conversando com você pelo WhatsApp."

    scene tadaima local with Dissolve(2.0)

    show sayuri surpresa with dissolve

    s "Ah! Nã-não fale sobre isso!"

    mc feliz "Não precisa ficar com vergonha! Foi uma gracinha."

    s "Nã-nã-não!"

    show sayuri infeliz
    with dissolve

    s "Não é justo... Eu nunca tinha usado esse programa e queria te ligar, mas minha irmã me forçou a adicionar você."

    mc normal "Não se preocupe. Você vai se acostumar com o tempo."

    s "Não sei se eu quero usar isso de novo..."

    mc "Você tem que usar! Todo mundo usa WhatsApp hoje em dia."

    s "Hmm..."

    show sayuri celular
    with dissolve

    s "Não sei se consigo entender isto aqui."

    mc "Olha! E se eu te ajudar a usar ele?"

    s "Me ajudar?"

    mc "Sim! Posso te dar algumas dicas e você manda mensagem pra mim pra praticar."

    s "..."

    mc "Pense nisso como se fosse um novo exercício de ginástica que você precisa masterizar."

    s "O-ok..."

    mc "Sério?!"

    s "Sim. Eu aceito."

    mc "Que legal! Você não v..."

    "Quê?!"

    scene sayuri tadaima_julia with Dissolve(2.0)

    mc surpreso "!"

    "A garçonete tá... tá me..."

    "Acho que ela tá tentando falar alguma coisa pra mim..."

    g "{size=10}Vem... aqui...{/size}"

    "Não entendi..."

    s "Eu até acho que vai ser bom eu aprender..."

    g "{size=15}Vem comigo...{/size}"

    "Ela tá me chamando!"

    "Essa garota tá me dando bola desde que eu cheguei aqui. Mas e a [s]? Isso não seria certo..."

    "E agora? O que eu faço?"

    menu:
        "Ignorar a garçonete":


            "Eu não preciso desse drama na minha vida."

            if julia_seducao > 1:

                "Mas ela tá me provocando desde que eu cheguei, e eu meio que tô aceitando as provocações dela."

                "Será que não vale a pena pelo menos conferir?"

                menu:
                    "Aceitar o convite da garçonete":


                        jump garconete_aceitar
                    "Recusar e ignorar a garçonete":


                        "Não! Uma provocação ou outra até vai, mas deixar a [s] é demais."

                        "Não é por isso que eu vim aqui."

                        jump garconete_recusar
        "Falar que vai até o banheiro":


            mc safado "..."

            jump garconete_aceitar

    label garconete_recusar:

        "Eu vou só ignorar e ela vai ver que eu não quero nada com ela."

        mc normal "Então, [s]. Seus dedos são pequenos. Você não vai ter problemas para usar o teclado virtual."

        s "Você acha?"

        mc "Com certeza. Você só precisa de prática mesmo."

        mc "Me envie uma mensagem, algo bem simples."

        s "O-ok."

        "..."

        scene tadaima local with Dissolve(2.0)

        show sayuri celular with dissolve

        "Ela foi embora..."

        "Que garçonete mais atrevida."

        "Quem trocaria uma atleta perfeita como a [s] pra dar uns amassos com uma coitada?"

        jump sayuri_e2_continua

    label garconete_aceitar:

        "Essa mina é linda e sexy. A [s] não vai nem perceber se eu for rápido."

        "Vou acenar que sim pra ela."

        mc safado "{size=10}Já estou indo...{/size}"

        scene tadaima local with Dissolve(2.0)

        show sayuri celular with dissolve

        mc desculpa "É... [s]."

        s "?"

        mc "Eu vou no banheiro rapidinho e vou aproveitar pra ver porque nossos sucos ainda não chegaram."

        s "Ah ok."

        mc "Aproveita para ir treinando as mensagens, ok?"

        s "Pode deixar. E obrigada por ver isso. Tá realmente demorando..."

        mc "..."





        hide sayuri

        scene tadaima vip
        with dissolve

        "Vou voltar pra aquele corredor com a porta e procurar por ela."

        scene tadaima porta
        with dissolve

        "Ela deve estar por aq..."

        scene tadaima salinha
        with hpunch

        g "Vem aqui!"

        mc surpreso "Uou!"

        show garconete charmosa
        with dissolve

        g "Olá..."

        g "Estava me procurando?"

        menu:
            "Sim. Vim ver se você está à minha disposição.":


                mc charmoso "Sim. Vim ver se você realmente está completamente à minha disposição como você disse."
            "Estava indo para o banheiro...":


                g "Não precisa mentir pra mim, gato."

                g "Eu sei que você veio me procurar."

                mc desculpa "..."

                g "Não se preocupe. Ninguém pode ouvir a gente aqui."

                mc charmoso "Você disse que estava à minha disposição se eu precisasse de alguma coisa..."

        g "E se eu estiver? O que você vai querer?"

        mc charmoso "De você? O que você está disposta a me dar?"

        show garconete provocando
        with dissolve

        if julia_seducao > 1:

            g "Você aceita minhas provocações durante a tarde toda... E agora me olha assim e fala essas coisas..."
        else:


            g "Você não aceitou minhas investidas antes... Mas agora me olha assim e fala essas coisas..."

        g "Só que e a garota na outra sala?"

        menu:
            "Você tem razão. Isto é um erro.":


                mc desculpa "Acho que você tem razão. Isto é um erro."

                g "Só agora você percebeu isso?"

                show garconete cena
                with dissolve

                g "Mas será que você consegue dizer não pra mim?"

                g "Você não quer sentir meu gosto?"
            "Ela não importa agora.":


                mc tarado "Ela não importa agora."

                mc "Será que você estava só me provocando? Agora que estamos aqui não tem mais coragem?"

                show garconete cena
                with dissolve

                g "Isso aqui é o suficiente pra você?"

                g "Ou você quer sentir meu gosto também?"

        "Essa garota não tá pra brincadeira."

        "A coisa tá ficando séria de verdade. Será que isso é certo?"

        g "E então? Agora que você tem uma gostosa nos seus braços, pronta pra você, o que vai ser?"

        menu:
            "Beijar ela":


                python:
                    if renpy.android:
                        PythonSDLActivity.registraEvento("julia_beijo","beijo","local")

                $ julia_seducao += 4

                mc charmoso "O que você acha?"



                show julia_tadaima1 with Dissolve(1.0)

                pause

                g "Hmm..."

                "..."

                g "Assim..."

                "..."

                g "Não precisa parar. Eu tô aqui pra você."

                "Não sei se consigo parar agora..."

                menu:
                    "Já passou tempo demais, a [s] vai notar.":


                        hide julia_tadaima1 with Dissolve(1.0)



                        mc bravo "Já estamos muito tempo aqui. Ela vai notar."

                        g "Tem certeza?"

                        g "Você pode ter tudo o que você quiser..."

                        mc safado "... E agora?"

                        menu:
                            "Recusar a garçonete":


                                mc charmoso "Tenho certeza. Você é deliciosa, mas não posso deixar ela me esperando mais."

                                g "Hmm... Que pena..."

                                mc charmoso "Até um dia."

                                jump voltar_sayuri
                            "Tirar as roupas dela":


                                jump garconete_cena_continuar
                    "Não consigo parar agora.":


                        label garconete_cena_continuar:

                            python:
                                if renpy.android:
                                    PythonSDLActivity.registraEvento("julia_beijo_mais","beijo_mais","local")

                            $ julia_seducao += 4

                            $ sayuri_e2_beijo_julia = True

                            "Não tem como eu parar agora."

                            scene tadaima salinha with Dissolve(1.0)

                            g "Isso! Tira minha roupa!"



                            scene black with dissolve

                            scene julia_tadaima2 with Dissolve(1.0)

                            pause

                            g "Assim!"

                            g "Ah!"

                            g "Me beija!"

                            g "Me abraça mais forte!"

                            g "Ah!"

                            "..."

                            mc safado "Você é deliciosa..."

                            g "Então me beija mais."

                            "..."

                            scene tadaima salinha
                            with hpunch

                            "{size=32}{i}TOC TOC{/i}{/size}"

                            g "!"

                            mc surpreso "!"

                            hide garconete
                            with dissolve

                            "Voz Masculina" "Ei! Júlia, você tá aí?!"

                            "..."

                            g "{size=15}Sai de cima!{/size}"

                            mc bravo "..."

                            g "Estou terminando de limpar a sala!"

                            "Voz Masculina" "Então termina logo que tem cliente esperando lá na frente!"

                            g "Um segundo e tô indo lá."

                            "..."

                            show garconete charmosa
                            with dissolve

                            g "Vamos ter que deixar a continuação pra um outro dia."

                            mc envergonhado "Não sei se eu tenho cacife pra voltar aqui tão cedo..."

                            g "Não precisa ser aqui. Eu tenho seu número."

                            mc desconfiado "Que? Como?"

                            g "A barra tá limpa. Pode dar o fora. Vai!"

                            mc "Ok! Mas..."

                            g "Vai logo!"

                            jump voltar_sayuri
            "Empurrar ela e deixar a sala":


                "Isso é demais! Não está certo fazer isso enquanto a [s] está aqui do lado me esperando."

                show garconete perguntando
                with hpunch

                g "Ei!"

                label voltar_sayuri:

                    "..."

                    hide garconete
                    with dissolve

                    show tadaima porta
                    with dissolve

                    mc triste "Pff... Pfff..."

                    "Preciso voltar pra nossa sala o quanto antes."





                    scene tadaima vip
                    with dissolve

                    mc desculpa "Oi, [s]."

                    if julia_seducao >= 8:

                        $ sayuri_amizade -= 6

                        show sayuri infeliz with dissolve

                        s "Puxa, que demora, [mc]. Achei que tivesse ido embora."

                        mc "Não não. Eu acabei brigando com eles porque eles se esqueçeram das nossas bebidas e aquela garçonete não quis admitir."

                        s "Verdade? Ela fez isso?"

                        mc "Sim. Desculpa a demora... De verdade..."

                        s "Tudo bem... Eu que sou muito insegura eu acho..."

                        mc triste "Não! Não é isso. Eu que demorei, não é culpa sua!"

                        "Droga... Ter ficado tempo demais com ela na salinha realmente deixou a [s] triste."

                        "Isso pode prejudicar meu encontro..."

                        s "..."

                    elif julia_seducao >= 4:

                        $ sayuri_amizade -= 3

                        show sayuri meudeus with dissolve

                        s "Onde você tava, [mc]? Demorou..."

                        mc "Desculpa, eu fui no banheiro, e na volta fui falar com eles sobre nossa bebida. Aparentemente demorou mais do que eu esperava."

                        "Ela ficou um pouco incomodada, mas sorte que eu voltei rápido."

                        "Talvez eu perca alguns pontos com ela, mas seria pior se eu tivesse demorado ainda mais."

                        s "Tudo bem..."
                    else:


                        show sayuri surpresa with dissolve

                        s "Já voltou?!"

                        mc normal "Sim. Sou rápido, né?"

                        show sayuri interessada with dissolve

                        s "Sim!"

                        s "Obrigada por voltar rápido. Eu... não gosto muito de ficar sozinha."

                        mc "Pode deixar que aqui a gente não deixa uma dama esperando."

                        s "Assim que se faz hehe..."

                        "Acho que é a primeira vez que ela sorri pra mim dessa forma."

                        "Foi muito importante eu ter negado a garçonete e voltado o quanto antes. Beleza!"

                    mc "Deixa eu me sentar do seu lado."

                    hide sayuri with dissolve

                    scene tadaima local with dissolve

                    jump sayuri_e2_continua

    label sayuri_e2_continua:

        $ sayuri_amizade += 6

        "..."

        show sayuri celular with dissolve

        s "Hmm..."

        s "Ainda é muito difícil."

        mc "Calma. Você tá só começando seu treino."

        $ renpy.notify("Sayuri está avaliando suas ações no encontro...")

        mc "Vamos conversar muito pelo celular ainda."

        show sayuri surpresa with dissolve

        s "Sé-sério?!"

        mc desculpa "Digo... Só se você quiser, claro."

        if sayuri_amizade > 9:

            $ renpy.notify("Sayuri achou você confiável...")

            s "Eu... Eu acho que eu gostaria, sim."

            show sayuri celular with dissolve

            s "Se você não se cansar de mim."

            mc normal "Claro que não. Eu tô adorando passar tempo com você."

            s "Mas eu escrevo tudo errado e demoro uma eternidade..."

            mc "Para de ser boba. Você vai se acostumar rapidinho. Eu vou te esperar, não importa o tempo que você precisar."

            s "O-obrigada, [mc]."
        else:


            $ renpy.notify("Sayuri está com dúvidas sobre você...")

            s "..."

            show sayuri infeliz with dissolve

            s "..."

            mc incomodado "Não se preocupe. Veja o que você acha."

            s "..."

            "Eu acho que eu ainda não consegui passar a confiança que eu precisava pra ela..."

            if julia_seducao >= 4:

                "Talvez ter ido atrás da garçonete não tenha sido a melhor das ideias..."

        mc incomodado "Pelo jeito nossa bebida não vai chegar mesmo. Imagina pedir algo pra comer."

        mc normal "A gente podia puxar o carro, o que acha?"

        show sayuri surpresa with dissolve

        s "Ir embora?"

        mc normal "Isso."

        if sayuri_amizade > 9:

            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("sayuri_e2_amizade","amizade","resultado")

            $ sayuri_e2 = "amizade"
            $ sayuri_amizade_evento += 1

            s "Mas já?!"

            mc normal "Fico feliz que esteja gostando do nosso passeio."

            s "Eu... Eu estou. Mas..."

            mc triste "..."

            s "Eu não... quero que acabe."

            mc triste "[s]..."

            mc "A gente vai poder sair no futuro."

            scene sayuri tadaima_triste with Dissolve(2.0)

            s "Não!"

            s "É isso que eles me disseram!"

            mc triste "..."

            s "Eles me falaram isso também. Só que nunca voltaram."

            s "Todos me odeiam... Porque eu sou uma atleta olímpica."

            s "Todos dizem que eu me acho e que eu só tenho olhos pro meu sucesso."

            s "Na internet, eles me enchem de comentários maldosos! Se descobrem meu telefone toda hora passam trote..."

            mc "[s]..."

            s "São todos horríveis... Meus pais só querem saber do meu desempenho. Minha técnica a mesma coisa."

            s "Não tenho amigos, nem namorado! Olha minha idade! Você acha certo uma garota dessa idade ser virgem?!"

            s "E agora você também vai me deixar..."

            s "Minha irmã é a única que gosta de mim... Que me suporta..."

            menu:
                "Não podemos ficar aqui pra sempre.":


                    mc triste "[s], eu não sabia que você se sentia assim."

                    mc "Mas não podemos ficar aqui pra sempre. Essa não é a solução."
                "Eu não vou te deixar.":


                    mc triste "Eu não quero te deixar, [s]. Não é isso que estou tentando fazer."

                    mc "Eu quero continuar vendo você, se você quiser me ver também."

            scene sayuri tadaima_surpresa with Dissolve(1.0)

            pause

            s "..."

            mc desculpa "Desculpa se eu soar meio grosso, mas não me importa o que aconteceu com você antes."

            mc "Eu te conheci só agora. E tenho que te falar que você é incrível mesmo."

            mc "Quando te vi dançando no templo, pensei como você tinha confiança nos movimentos."

            mc "E seu passado só aumenta ainda mais minha admiração por você."

            mc "Só que algumas pessoas, eu acho, precisam diminuir as outras pra se sentirem bem."

            mc "Infelizmente elas miram pessoas como você. Você é o que todas elas queriam ser, mas a maioria nunca vai conseguir nem metade."

            s "..."

            mc feliz "Mas eu não tenho inveja de você. E também não tenho medo de você."

            mc desculpa "Eu me aproximei de você porque eu queria uma pauta pra minha revista. E isso foi errado."

            if sayuri_atencao > 0 and sayuri_p1_mentira < 1:

                mc triste "Ainda por cima acabei com seu lugar de treino."

                mc "Isso é imperdoável, mas você ainda por cima disse que ia tentar me perdoar."

            mc feliz "Mas eu não tô mais aqui por causa disso. Eu quero realmente conhecer você melhor."

            mc "E eu acho que nesse tempo que a gente conversou você viu como eu realmente quero te conhecer."

            scene sayuri tadaima_feliz with Dissolve(1.0)

            s "Sim..."

            mc "Então não quero que fique pensando nisso. Eu prometo que vou falar com você pelo celular sempre que quiser."

            s "{size=20}Ve-verdade?{/size}"

            mc feliz "Claro! E nossos treinos de WhatsApp?!"

            s "{size=18}Hehe... Você realmente tá levando isso a sério.{/size}"

            mc bravo "Claro que tô! Eu não brinco em serviço."

            s "{size=15}Ainda não tô acreditando... que...{/size}"

            mc angustiado "Tudo bem com você, [s]?"

            scene sayuri tadaima_triste with Dissolve(1.0)

            s "{size=15}Eu tô meio... com falta de ar... e tá tudo... rodando...{/size}"

            mc "Você passou muito nervoso. Acho que..."

            mc "Ei! Cuidado!"

            scene sayuri desmaio with Dissolve(2.0)

            pause

            mc surpreso "[s]!"

            s "O-obrigada..."

            mc angustiado "Você tá legal?!"

            s "Eu..."

            mc triste "Calma."

            mc desculpa "Não precisa falar nada. Só descanse aqui. Eu vou chamar alguém."

            s "{size=18}Não... Fica comigo...{/size}"

            mc triste "Mas..."

            s "..."

            mc desculpa "Ok. Estou aqui com você."

            s "..."

            s "{i}zzzz{/i}"

            mc "[s]?"

            mc "Ela tá respirando. Deve ter desmaiado."

            mc concentrando "Pelo jeito ela só tá dormindo agora. Preciso chamar alguém. Mas como vou sair daqui?"

            scene tadaima vip with dissolve

            show garconete perguntando with hpunch

            g "Ei! O que está havendo aqui?!"

            mc triste "Ela desmaiou..."

            g "O que você fez com ela, seu monstro?!"

            mc "Calma! Não fiz nada. Ela..."

            g "[s]! Você tá legal?!"

            scene sayuri desmaio with dissolve

            s "..."

            g desconfiada "[s]!"

            $ gnome = "Júlia"

            s "Calma, [g]..."

            g "Calma o caralho!"

            g "Você vai morrer!"

            s "Eu não vou morrer..."

            g "E é tudo culpa desse idiota!"

            s "Ele que me ajudou. Senão eu ia cair com a cabeça..."

            mc desculpa "Calma as duas. Não tá vendo que ela tá cansada?"

            g "Humph! E o que você sabe de qualquer coisa?"

            s "Acho... acho que estou me sentindo melhor."

            mc "Tem certeza?"

            s "Sim. Me ajuda a sentar por favor?"

            g "..."

            mc normal "Claro. Aqui vai."

            scene tadaima local with dissolve

            show garconete provocando with dissolve

            g "O que esse idiota sabe de qualquer coisa?"

            show garconete provocando with move:
                linear 0.5 xpos 300

            show sayuri meudeus with dissolve

            show sayuri meudeus with move:
                linear 0.8 xpos 1050

            s "Não fale assim com ele, [g]."

            g "Por que você tá protegendo esse coitado?"

            if julia_seducao > 4:

                g "Você sabe o que ele fez aquela hora que ele saiu da..."

                s "Calma, [g]!"

                g "..."

            s "O [mc] é um amigo meu."

            g "Amigo igual aos outros? Que te deixaram?"

            s "..."

            show sayuri interessada with dissolve

            s "Eu acho... Acho que não."

            g "Que?!"

            s "Eu... acredito que ele não vai sumir."

            mc normal "..."

            g "Você mal conhece esse... Como pode dizer isso?!"

            if julia_seducao > 4:

                g "Na primeira oportunidade ele vai te trocar por outra!"

                g "Ele só quer saber de um pedaço de carne pra atacar!"

                mc desculpa "..."

            s "Eu acredito nele. Foi o que eu escolhi fazer."

            g "..."

            g "Parece que eu não vou conseguir mudar sua cabeça, né?"

            show garconete charmosa with dissolve

            g "Então tudo bem."

            s "Obrigada, [g]. Eu sabia que você ia ficar do meu lado."

            g "Mas quando ele deixar você, não venha correndo pra mim."

            s "Ok..."

            mc normal "Isso não vai acontecer, pirralha."

            s "Haha..."

            g "Veremos..."

            mc "Vamos lá pra frente?"

            s "Ok."
        else:


            python:
                if renpy.android:
                    PythonSDLActivity.registraEvento("sayuri_e2_fracasso","fracasso","resultado")

            $ sayuri_e2 = "fracasso"

            show sayuri infeliz
            with dissolve

            s "Tudo bem..."

            s "Estou pronta."

            mc incomodado "Ok. Vamos lá."

            "Parece que algo não está certo... Será que eu estraguei tudo?"

            scene tadaima vip
            with dissolve

            show garconete bemvindo
            with dissolve

            g "Já estão indo? Nem trouxe o suco ainda."

            show garconete bemvindo with move:
                linear 0.5 xpos 300

            show sayuri infeliz with dissolve

            show sayuri infeliz with move:
                linear 0.8 xpos 1050

            $ gnome = "Júlia"

            s "Oi, [g]. Deixa o suco pra próxima."

            mc desconfiado "Hã?"

            g "Que pena, mana. Parece que ele não era tão legal assim."

            s "Fica quieta, [g]. Que vergonha!"

            g "Vai indo na frente, mana."

            s "Ok..."

            hide sayuri
            with dissolve

            hide garconete
            with dissolve

            show garconete provocando
            with dissolve

            if julia_seducao > 4:

                g "Espero que você tenha aproveitado, otário."

                mc desconfiado "Quê?"

                g "Você não é homem suficiente pra ser amigo da minha mana."

            g "Não quero ver você perto dela, ouviu?"

            mc "Mas..."

            g "Você não vai ferir ela. Muitos já fizeram isso. Não vou deixar nenhum idiota chegar perto dela."

            g "E agora vai andando."

            if julia_seducao > 4:

                "Essa pirralha... Era tudo um plano dela?"

                "Como eu pude..."

        scene tadaima restaurante with Dissolve(2.0)

        show sayuri irmas with Dissolve(2.0)

        g "A gente não é linda juntas?"

        g "Esquece esse tonto, mana."

        s "Para de falar assim, [g]. Eu te amo, mas você não pode afastar as pessoas de mim."

        g "Por que não? A gente só precisa uma da outra. Os outros são todos babacas."

        s "..."

        if sayuri_e2 == "amizade":

            mc normal "Foi um prazer sair com você, [s]."

            s "O-obrigada, [mc]."

            mc "Você vai me escrever?"

            s "Vou... Vou tentar."

            g "Bah! Vamos parar com essa história melequenta?"

        mc normal "Vou indo nessa. Até a próxima."

        "Sayuri e Júlia" "Até!"

        if tempo < 3:

            scene mapa cidade
            with dissolve
        else:


            scene mapa cidade_noite
            with dissolve

        pause

        "Uou. Que loucura foi essa?"

        "A [s] é uma graça, mas a... irmã? Como pode ser irmã? Ela nem é oriental... Elas não se parecem nem um pouco. Como eu ia advinhar isso?"

        if julia_seducao > 4:

            mc tarado "Aliás, aquele lance na sala foi incrível. Será que a tal da [g] toparia fazer algo assim de novo no futuro?"

        "Aliás, por que raios ela daria em cima do amigo da irmã?"

        "Parece que ela queria me afastar da [s]... Mas por que?"

        mc zerado "Espero que não seja um tipo de complexo..."

        mc "Deixando isso de lado..."

        $ resultado_encontro = "sayuri"

        show screen menu_pontos
        with dissolve

        if sayuri_amizade_evento > 0:

            "Esse encontro com a [s] foi muito bacana. Eu conheci ela muito melhor."

            mc incomodado "Ela tem esse problema de confiança com as pessoas."

            "Ela deve ter passado alguma barra muito pesada no passado pra sentir essa desconfiança."

            "Ela não quer um romance agora. Ela quer um amigo. Alguém que ajude ela a confiar nas pessoas outra vez."

            "Quem sabe no futuro isso não possa mudar?"

            "Eu quero ajudar ela a superar esse trauma. E pra isso eu preciso que ela continue confiando em mim."

            "Não posso pisar na bola. Tenho que tomar cuidado com o lance da revista."

            if sayuri_atencao > 0:

                mc desculpa "Eu já ferrei ela uma vez."

                "Tenho que tomar muito cuidado porque se eu entregar ela de novo, talvez ela pare de confiar em mim pra sempre."

                if sayuri_p1_mentira:

                    "E eu ainda por cima menti pra ela, dizendo que não entreguei a pauta pro chefe."

                    "Quanto mais eu demorar pra contar, pior vai ser quando ela descobrir."

                    mc tarado "SE.... Ela descobrir."

            "Tenho que conversar com ela pelo celular e torcer pra que ela tenha gostado do nosso encontro."

            "Eu acho que ela gostou."

            mc zerado "Mesmo com a tal da [g] tentando estragar tudo."
        else:


            mc incomodado "Meu encontro com a [s] começou bem, mas eu sinto que a coisa não terminou da melhor forma..."

            if julia_seducao > 9:

                mc safado "Meu enrosco com a [g] com certeza complicou as coisas."

                "Eu deixei ela esperando um tempão. Ela até achou que eu poderia ter ido embora."

                "Será que realmente valeu a pena?"

                mc tarado "Talvez sim..."

            elif julia_seducao > 4:

                mc desculpa "Meu enrosco com a [g] deve ter complicado as coisas."

                "Eu demorei pra voltar na sala. Talvez isso tenha despertado algo ruim nela."
            else:


                "Mesmo recusando a [g] ela não conseguiu confiar em mim."

                "Talvez o lance da pauta... Talvez eu tenha deixado ela assustada com minha abordagem sexualizada."

            "Eu preciso repensar minha {b}Abordagem{/b}... Se eu pudesse voltar no tempo pelo menos..."

            "Ou não! Talvez a [s] nem seja tão interessante assim."

        hide screen menu_pontos
        with dissolve



        "..."

        $ dia_sayuri = dia + 1
        $ tempo = 4

        scene black with Dissolve(2.0)

        pause

        scene sayuri_quarto with Dissolve(1.0)

        label say2_premium1:

            pass

        menu:
            "O que será que a [s] tá pensando?":








                "Nossa... que que aconteceu hoje?"

                "Ainda não tô acreditando. Só de pensar eu já fico vermelha."

                scene sayuri_quarto3 with Dissolve(1.0)

                "Eu realmente tive um encontro... com um garoto... minha nosa..."

                "Eu tava tremendo... eu nem conseguia falar no começo."

                "Mas ele foi tão legal comigo... ele percebeu meu jeito e falou comigo tão normal."

                "Alguém conversar com você assim... é tão gostoso... tão natural... foi super confortante pra mim..."

                if sayuri_amizade_evento > 0:

                    "No final eu ainda fiz um papelão... chorando... até desmaiei... nem acredito."

                    "Acabei vomitando um monte de coisa nele, sobre amigos e tudo. Que vergonha!"

                    "Ainda não acredito que ele ficou ouvindo tudo e ainda falou daquele jeito... aquelas palavras..."

                    "O [mc] parece ser um rapaz especial... o tipo de homem que eu t-tava esperando..."

                    "[mc]... eu... eu nunca namorei na vida... e você foi perfeito... o homem que eu queria f-ficar..."
                else:


                    "E eu não acredito que a [g] fez aquilo com ele."

                    "E ele ainda caiu! Ele tava indo tão bem... mas me deixar lá pra ficar com ela? Isso não foi legal..."

                    "Eu tava apostando tudo em você, [mc]... por que você tinha que fazer isso?"

                    "Você não tá vendo que eu tô precisando de ajuda?"

                "Eu queria que você fosse perfeito pra que eu pudesse me entregar pra você..."

                "N-não é porque eu não namoro que eu não tenho desejos, [mc]..."

                "Eu tenho muitos desejos... às vezes é demais pra eu controlar..."

                "Q-que nem agora... tá começando..."

                menu:
                    "Eu tenho que me controlar":


                        "E-eu preciso me segurar. Eu sou uma garota direita."

                        "Eu vou ter que... aguentar mais um pouco... acho melhor eu tomar outro banho e parar de pensar nisso."
                    "Eu não consigo aguentar!":


                        "E-eu preciso descarregar toda essa frustração, [mc]..."

                        scene sayuri_quarto4 with Dissolve(1.0)

                        "Ah... meu corpo tá queimando... meus peitos são tão sensíveis... eu fico arrepiada só de pegar neles..."

                        "Aqui embaixo... eu preciso..."

                        "O que você ia pensar se soubesse que eu tenho todos esses desejos, [mc]? Você não ia querer nada comigo?"
                        scene snew_ani16 with Dissolve(1.0)
                        "Você ia falar que eu sou impura?"

                        "Mas eu não consigo... eu preciso disso. Senão eu vou explodir! Eu preciso sentir meu corpo."

                        "Eu queria que fosse você pegando em mim... com suas mãos fortes..."

                        "Ah... só tocar assim não é o suficiente, [mc]... v-você pode pegar aqui em baixo também? E-eu te ajudo."

                        scene sayuri_quarto5 with Dissolve(1.0)

                        "A-ah... que delícia..."

                        "Quando eu toco em mim assim... hmm... eu sei exatamente o que eu faço..."

                        "Eu tô no limite... se eu continuar assim eu vou chegar lá na hora..."

                        "[mc]... se fosse você aqui... me tocando assim... eu ia gozar em você... hmmm!"

                        "Um lado de mim queria que você... que você soubesse que eu tô muito excitada... ah..."
                        scene snew_ani22 with Dissolve(1.0)
                        "Eu não posso mais parar. Eu vou tirar tudo..."

                        "Eu vou deitar e me divertir... pensando em você..."

                        s "Hmm!"

                        scene black with dissolve

                        "Hm?"

                        scene sayuri_quarto6 with Dissolve(1.0)

                        s "Hm! Ahh!"

                        "???" "Não acredito..."

                        "Então ela... eu não acredito..."

                        "Eu achei que hoje não tinha... então o que aconteceu hoje fez ela ficar assim..."

                        "Se eu soubesse que você tava assim... eu teria cuidado melhor de você..."

                        "Mas eu tô aqui pra você... vou ficar aqui te... p-protegendo..."

                        "???" "Hmm..."

                        window hide

                        pause

                scene black with Dissolve(1.0)
            "Deixa pra lá":


                pass



        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v3_fim","final","local")

        jump call_cidade

label sayuri_evento5:

    $ sayuri_e5 = "continua"

    python:
        renpy.notify("A Pixie salvou este momento. Use o menu Encontros para voltar aqui.")
        renpy.save("s5_save", extra_info="s5_save")

    $ iconchefe += 1

    "Hmmm..."

    "Desde aquele nosso passeio pela Cidade Chinesa, eu não escutei mais nada da [s]."

    scene ape_tv with Dissolve(1.0)

    "Ela não me escreveu mais no celular. Eu também não tive coragem de falar nada pra ela."

    "A [g] também nem pra dar uma ajuda."

    if sayuri_e4 == "badending":

        "Aquele lance que a [g] fez no ponto de ônibus foi sem noção."

        "Eu não sei onde eu tava com a cabeça. Eu podia ter me controlado, mas eu simplesmente não consegui!"

        "Eu fodi minha relação com a [s] e provavelmente ela nunca vai me perdoar."

        "Que saco..."

        scene black with dissolve

        p rindo "Isso o [mc] tem razão. Depois da cagada no ponto de ônibus, nunca mais você vai ver a [s]."

        p rindo "Se você quer ver o resto da história dela, eu recomendo você usar a aba Encontros no menu e escolher outra opção."

        p "Se você não tá nem aí, só continuar jogando. Quem escolhe como o jogo acontece é você."

        $ v17_fim = True
        $ sayuri_e5 = "badending"

        python:
            if renpy.android:
                PythonSDLActivity.registraEvento("v17_fim","sayuri","personagem")
                PythonSDLActivity.registraEvento("se5_badending","sayuri","personagem")

        jump call_cidade

    elif not sayuri_e4 == "fracasso":

        "Tenho certeza que ela curtiu pra caramba o banho de saúde e beleza."

        "Só que aquela 'mestra' dela chegou e acabou com tudo. Mulher insuportável."

        "Eu também caguei um pouco derrubando ela no chão hehe..."

        "Mas no fim acabou tudo bem... eu acho..."

        if sayuri_e4 == "namoro":

            $ sayuri_beijo = True

            "Ela até me beijou..."

            "Mas depois ela só saiu e eu nem falei nada. Que saco isso, mano."
    else:


        "Ela quis encerrar o encontro antes da minha surpresa."

        "Mas acho que isso acabou sendo melhor, porque pelo menos ela não vai se encrencar com a treinadora dela."

    "Espero que fique tudo bem."

    "..."

    "Quer saber!? Acho que vou dar um pulo na Cidade Chinesa!"

    "Talvez eu possa falar algo com o [chi]. Saber um pouco mais sobre a [s]. Pelo que eu me lembro ele chama ela de outro nome."

    "Por que ele faria isso? Com certeza ele sabe alguma coisa dela."

    "E também teve aquela garota. Aquela menina que tava machucada..."

    "Ela até tinha um jeito meio parecido com o da [s] parece. Mas ela só tem uns 13 ou 14 anos, no máximo uns 15."

    "Fechou. Vou dar um pulo lá."

    scene black with Dissolve(1.0)

    $ proibido_salvar = True
    $ show_quick_menu = False

    p lecionando "Opa opa!"

    p "Temos um problema... parece que meus poderes estão falhando..."

    p "Você vai ter que ir neste encontro com a [s] sem poder manipular o tempo."

    p rindo "Hehe! Isso vai ser divertido. Boa sorte!"

    "..."

    scene onibus parado with Dissolve(1.0)

    pause

    "É um bom rolê até lá, mas vai valer muito a pena."

    scene black with Dissolve(1.0)

    "..."

    play sound "audio/som_7_cidade_chinesa.mp3"

    scene chinatown geral with Dissolve(1.0)

    "O carrinho do [chi] é logo ali."

    scene chinatown lamen with Dissolve(1.0)

    "Parece que ele tá bem tranquilo agora."

    "E aí, [chi]. Tudo beleza?"

    show bao pensando with dissolve

    if bao_evento > 0:

        chi "Bom dia, [mc]."
    else:


        chi "Bom dia, jovem."

    mc desconfiado "Algum problema? Você parece cansado."

    chi "..."

    show bao normal with dissolve

    chi "Nada demais. Só as mesmas dificuldades de sempre."

    python:
        if renpy.android:
            bao_pontos = PythonSDLActivity.pegaBao()

    if bao_pontos > 0:

        chi "Desde que eu te ensinei a preparar os lámens, você tem me ajudado bastante."

        mc normal "Não é nada. Mas..."

    mc desconfiado "Que tipo de problema você diz?"

    chi "Não pense nisso. As coisas vão acontecer naturalmente para você."

    mc envergonhado "Você fala tipo o Mestre dos Magos..."

    chi "Mestre dos Magos?"

    mc "Haha... acho que você não conhece..."

    chi "..."

    mc normal "É... eu vim perguntar pro senhor da [s]."

    chi "O que tem a Ai Fen?"

    mc normal "Não é nada. É que faz um tempo que a gente não se fala e daí eu queria-"

    if sayuri_e4 != "fracasso":

        show bao falando with dissolve

        chi "Foi bom você falar sobre isso."

        mc desconfiado "Âh?"

        chi "Eu vi a... treinadora dela muito irritada há um tempo. Você sabe algo sobre isso?"

        "Droga. Não sei se eu devo falar pra ele que eu desafiei a velha lá no banho."

        if sayuri_beijo:

            "Sobre o beijo então..."

        menu:
            "Eu fiz a [s] desobedecer a treinadora dela.":


                $ renpy.block_rollback()

                mc desculpa "Por minha causa a [s] desobeceu a treinadora dela. A gente tava tipo em um encontro-"

                chi "Entendo. Então foi isso..."
            "Não sei o que pode ter rolado.":


                $ renpy.block_rollback()

                mc envergonhado "Sei não o que aconteceu. A gente até saiu juntos, mas nada assim... sabe."

                chi "Sei..."

                "Tenho a impressão que ele não acreditou no que eu disse."

        chi "Sabe, [mc]. Aquela mulher... e outros aqui da Cidade Chinesa... têm uma forma muito peculiar de fazer as coisas."

        chi "Quero dizer que eles fazem as coisas de uma forma diferente do que você está acostumado."

        chi "Você precisa medir suas ações com o dobro de cuidado."

        chi "Suas atitudes podem influenciar a vida da Ai fen, entende?"

        mc desculpa "Entendo. Pode deixar."

        mc charmoso "Não vou fazer nada que possa prejudicar a [s]."

        chi "..."

        show bao normal with dissolve

        chi "Você é uma boa pessoa. Mas tome cuidado."

        mc "Pode deixar."

    chi "Certo."

    chi "Tenho uma boa notícia para você então."

    mc desconfiado "O que?"

    chi "A Ai Fen está no templo treinando."

    mc surpreso "Sério?!"

    mc normal "Vou dar uma passada lá."

    show bao pensando with dissolve

    chi "Boa sorte."

    mc "Ok. Até."

    hide bao with dissolve

    "Boa sorte? Por quê?"

    "..."

    scene chinatown caminho with Dissolve(1.0)

    "Lá vamos nós subir essa montanha. Eu tenho a impressão que já ouvi alguém falar o nome daqui, mas não tô lembrando agora."

    scene black with Dissolve(1.0)

    scene chinatown templo with Dissolve(1.0)

    "Ufa..."

    "{size=10}Hah! Heyah!{/size}"

    mc normal "Será que ela tá treinando?"

    "Vai ser bem legal ver isso."

    "..."

    scene chinatown treino_fenju with Dissolve(2.0)

    pause

    "Acho que tô vendo ela."

    show treino_sayuri sayuri1 with dissolve

    "[s]!"

    "Continua linda como sempre."

    mc desconfiado "Âh? E quem é aquela?"

    show treino_fenju fenju1 with dissolve

    pause

    "Parece aquela garota que eu vi da outra vez. Como era mesmo o nome dela?"

    menu:
        "Ao Fen":


            $ renpy.block_rollback()

            "Ao Fen?"

            "Acho que esse é o nome que o [chi] chama a [s]. Ou não?"

            "Sei lá..."
        "Ayumi":


            $ renpy.block_rollback()

            "Ayumi? Da onde eu tirei isso? Não deve nem ser chinês esse nome."
        "Ai amu":


            $ renpy.block_rollback()

            "Acho que eu misturei uma pá de coisa agora."

            "Sem comentários..."
        "Fen Ju":


            $ renpy.block_rollback()

            "Fen Ju! Fen... será que era isso?"

            "Pera! Não! Era isso mesmo! Fen Ju!"

            "Ponto pra mim!"
        "Chinesinha":


            $ renpy.block_rollback()

            "Chinesinha? Que preconceito..."

            "Pior que esse é o máximo que eu consigo lembrar..."

            mc angustiado "..."

    s "{size=15}Eu não falei pra você parar. Pode fazer de novo.{/size}"

    fen "{size=15}O-ok.{/size}"

    s "{size=15}Vai.{/size}"

    show treino_fenju fenju2 with dissolve

    pause

    "Parece que a [s] não tá treinando. Acho que ela tá ensinando aquela menina na verdade."

    "Será que eu aviso ela que tô aqui ou assisto um pouco do treino sem avisar?"

    "Eu quero muito ver um treino pra saber como é."

    "E se elas perceberem e acharem que eu tô espionando? Sei lá..."

    menu:
        "Assistir o treino sem avisar as garotas":


            $ renpy.block_rollback()

            "Eu tô curioso demais. Espero que não fique estranho se elas me verem."

            s "{size=15}Corrige a postura. Você ainda tá muito dura.{/size}"

            fen "{size=15}Tá.{/size}"

            show treino_fenju fenju1 with dissolve

            pause

            show treino_sayuri sayuri2 with dissolve

            s "{size=15}Quem mandou você parar?{/size}"

            fen "{size=15}Desculpa.{/size}"

            s "{size=15}Não é pra pedir desculpas. Só faz a posição.{/size}"

            fen "{size=15}...{/size}"

            show treino_fenju fenju2 with dissolve

            pause

            "A [s] fica bem séria no treino."

            "Bom... ela é uma atleta olímpica. A maior esportista do país. Ela deve saber o que tá fazendo."

            menu:
                "Continuar vendo o treino escondido":


                    $ renpy.block_rollback()

                    $ s5_rigida = True

                    "Só mais um pouco."

                    show treino_fenju fenju1 with dissolve

                    s "{size=15}Por que parou?{/size}"

                    fen "{size=15}Já t-tava doendo...{/size}"

                    s "{size=15}Não melhorou nada. Você continua rígida.{/size}"

                    s "{size=15}Tem certeza que você tá se esforçando?{/size}"

                    fen "{size=15}Claro!{/size}"

                    s "{size=15}Não parece, [fen]. Tá horrível. É vergonhoso ver você assim!{/size}"

                    fen "{size=15}Desculpa...{/size}"

                    "Nossa. Ela realmente pega pesado. Parece até outra pessoa hehe."

                    "Sorte que eu não sou discípulo da [s]."

                    s "{size=15}Vamos tentar um movimento diferente.{/size}"

                    fen "{size=15}Tá. Posso só sentar um pouqui-{/size}"

                    s "{size=15}Para de falar e faz o segundo movimento.{/size}"

                    fen "{size=15}...{/size}"

                    show treino_fenju fenju3 with dissolve

                    pause

                    s "{size=15}NÃO!{/size}"

                    fen "{size=15}!{/size}"

                    show treino_sayuri sayuri1 with dissolve

                    s "{size=15}Quantas vezes já falei?! O pé é o mais importante! Você é burra?!{/size}"

                    show treino_fenju fenju1 with dissolve

                    fen "{size=15}Desculpa...{/size}"

                    s "{size=15}E quem mandou você parar?! Você não aprende?!{/size}"

                    fen "{size=15}T-tá!{/size}"

                    show treino_fenju fenju3 with dissolve

                    s "{size=15}Não sei o que eu faço com você, [fen]...{/size}"

                    "Nossa. A [s] real-"

                    s "{size=15}Ah?!{/size}"

                    "Caralho! Acho que ela me viu!"

                    hide treino_sayuri with dissolve

                    s "[mc]?"

                    "Afe. E agora? Ela tá vindo pra cá."

                    show treino_sayuri close2 with dissolve

                    s "Você tava aqui?!"

                    mc envergonhado "E-eu..."

                    menu:
                        "Não! Acabei de chegar!":


                            $ renpy.block_rollback()

                            $ sayuri_amizade -= 2

                            mc surpreso "Nã-não! Acabei de chegar!"

                            mc envergonhado "Nem deu tempo de avisar."

                            show treino_fenju fenju1 with dissolve

                            s "Sé-sério?!"

                            mc "Sim."

                            show treino_sayuri close1 with dissolve

                            s "Afa... que bom."

                            mc "Hehe."

                            "Será que ela realmente acreditou?"
                        "Sim. Fiquei curioso com o treinamento.":


                            $ renpy.block_rollback()

                            $ sayuri_amizade -= 5

                            mc desculpa "Sim. Eu cheguei e não falei nada."

                            show treino_fenju fenju1 with dissolve

                            mc envergonhado "Eu tava muito curioso pra ver o treinamento de vocês."

                            s "Mas então! Vo-vo-você..."

                            mc normal "Se for sobre o treino não esquente. Eu sei que às vezes a gente tem que pegar pesado."

                            show treino_sayuri close3 with dissolve

                            s "..."

                            s "Ne-nem sei o que falar..."

                            mc desculpa "Desculpa. Não queria me intrometer."

                            s "..."
                "Avisar que você chegou":


                    $ renpy.block_rollback()

                    "Já xeretei demais. Acho que é melhor avisar que eu cheguei."

                    jump s5_avisar
        "Chamar a [s] e avisar que você chegou":


            $ renpy.block_rollback()

            "Não vou ficar fuçando nas coisas delas. Deixa eu chamar a [s]."

            label s5_avisar:

                mc feliz "[s]! Oi!"

                s "[mc]?!"

                hide treino_sayuri with dissolve

                "..."

                show treino_sayuri close2 with dissolve

                s "O-oi! Nossa..."

                mc normal "Que foi?"

                show treino_sayuri close1 with dissolve

                s "Nada. Só fiquei surpresa em ver você aqui."

                show treino_fenju fenju1 with dissolve

                s "Tudo bem?"

                mc normal "Sim. E você? Tá fazendo o que?"

                s "Ah... tô treinando."

                mc "Que bacana."

    s "Nunca imaginei que você viria pra cá."

    show treino_fenju fenju2 with dissolve

    mc feliz "O [chi] disse que você tava aqui. Queria muito ver você."

    s "Ah... não fale assim, [mc]."

    mc envergonhado "Haha. Não queria te deixar com vergonha."

    s "Tá."

    mc desculpa "Tô te atrapalhando?"

    show treino_sayuri close2 with dissolve

    s "Nã-não!"

    s "Você lembra da [fen], né?"

    mc normal "Sim."

    show treino_fenju fenju1 with dissolve

    s "Estamos só repassando alguns exercícios."

    mc "Entendi. Será que eu atrapalho se eu ficar aqui um pouco?"

    show treino_sayuri close3 with dissolve

    s "Cla-claro que não."

    s "Vamos treinar só mais um pouco e depois podemos conversar."

    if sayuri_beijo:

        mc safado "Só conversar?"

        show treino_sayuri close2 with dissolve

        s "Q-q-que?!"

        s "É..."

        mc charmoso "Tô só brincando com você."

        show treino_sayuri close1 with dissolve

        s "Tá..."

        "A [s] ainda não tá lidando tão bem com nosso beijo. Essa questão de intimidade realmente é difícil pra ela."

        "Mas não tenho pressa. Vou dar o tempo que ela precisar."

    s "Então vou lá, tudo bem?"

    mc normal "Claro. Vou ficar aqui olhando vocês."

    show treino_sayuri close3 with dissolve

    s "Certeza que não vai te atrapalhar? Pode me esperar lá na cidade."

    mc "Fica tranquila. Eu quero ver vocês."

    s "Não quero te incomodar."

    mc charmoso "Já falei que vai ser um prazer ver vocês."

    show treino_fenju fenju3 with dissolve

    s "Tá. Até daqui a pouco."

    hide treino_sayuri with dissolve

    "Tomara que eu realmente não atrapalhe elas."

    show treino_sayuri sayuri1 with dissolve

    s "{size=15}{/size}"

    s "{size=15}Voltei. Você ficou segurando o exercício o tempo todo?{/size}"

    fen "{size=15}É! Si-sim!{/size}"

    s "{size=15}Cuidado que vai te machucar.{/size}"

    fen "{size=15}?{/size}"

    s "{size=15}Pode descansar.{/size}"

    fen "{size=15}T-tá.{/size}"

    show treino_fenju fenju1 with dissolve

    "..."

    if s5_rigida:

        s "{size=15}Às vezes eu falo sério com você porque eu quero que você melhore, tudo bem?{/size}"

        fen "{size=15}?{/size}"

        s "{size=15}Você sabe que eu gosto muito de você e quero que você seja a melhor ginasta do mundo.{/size}"

        fen "{size=15}Tá.{/size}"

        "Então a [s] realmente gosta da [fen]."

        "Fiquei meio assustado com o jeito dela, mas é só pra melhorar o treino da garotinha."

    "Com certeza não é fácil ser uma medalhista olímpica. A [fen] é muito sortuda de ter a experiência da [s] pra ajudar ela."

    s "{size=15}Tá se sentindo melhor?{/size}"

    fen "{size=15}Tô.{/size}"

    s "{size=15}O que acha de tentar o primeiro movimento de novo?{/size}"

    fen "{size=15}Tá.{/size}"

    show treino_sayuri sayuri2 with dissolve

    s "{size=15}Não esqueça dos pés.{/size}"

    show treino_fenju fenju2 with dissolve

    pause

    s "{size=15}O pé é tudo em quase todos os movimentos. A forma como você pisa, a força que você coloca.{/size}"

    s "{size=15}O quadril é essencial também, porque ele é seu ponto central de equilíbrio. Todo o resto do corpo depende dele.{/size}"

    fen "{size=15}{i}puf puf{/i}{/size}"

    fen "{size=15}Tá.{/size}"

    s "{size=15}Cansou? Pode parar.{/size}"

    fen "{size=15}?{/size}"

    fen "{size=15}Eu... aguento...{/size}"

    fen "{size=15}{i}puf puf{/i}{/size}"

    s "{size=15}Só cuidado se machucar.{/size}"

    fen "{size=15}...{/size}"

    show treino_sayuri sayuri5 with dissolve

    "..."

    show treino_fenju fenju1 with dissolve

    "..."

    show treino_fenju fenju2 with dissolve

    "..."

    show treino_sayuri sayuri2 with dissolve

    "..."

    show treino_fenju fenju1 with dissolve

    "..."

    show treino_fenju fenju2 with dissolve

    "..."

    "Caraca... já faz umas duas horas que a gente tá nessa. Elas não cansam, não?"

    mc zerado "Até eu já cansei..."

    show treino_sayuri sayuri5 with dissolve

    s "{size=15}...{/size}"

    s "{size=15}Está bom por agora. Pode ficar na pose e me esperar pra gente continuar.{/size}"

    fen "{size=15}Eu queria só-{/size}"

    s "{size=15}[fen].{/size}"

    fen "{size=15}Tá...{/size}"

    show treino_fenju fenju5 with dissolve

    hide treino_sayuri with dissolve

    "..."

    show treino_sayuri close1 with dissolve

    s "Oi."

    mc normal "Oi de novo."

    s "Pronto pra dar uma volta?"

    mc charmoso "Claro."

    mc normal "Ah. Achei bem puxado o treino de vocês."

    show treino_sayuri close2 with dissolve

    s "Puxado?"

    mc desculpa "Sim. Já faz duas horas mais ou menos. E isso que quando eu cheguei vocês já tavam treinando. E olha como tá o sol."

    s "Sei..."

    show treino_sayuri close3 with dissolve

    s "Realmente é bem puxado..."

    s "Mas não fique pensando nisso. Isso é algo que toda atleta de ponta aprende a suportar."

    s "Chegar ao topo exige muito da gente, [mc]."

    mc "Entendo..."

    hide treino_fenju with dissolve

    "Hã? A [fen] saiu fora."

    "Pra onde ela tá indo?"

    menu:
        "Avisar a [s] que a [fen] saiu":


            $ renpy.block_rollback()

            $ sayuri_amizade += 2

            "Melhor eu falar pra ela."

            mc desculpa "Sei que não é da minha conta. Mas a [fen] saiu do lugar."

            show treino_sayuri close2 with dissolve

            s "Quê?"

            hide treino_sayuri with dissolve

            s "Essa menina."

            "..."

            "..."

            show treino_sayuri sayuri2 with dissolve

            s "{size=15}E não saí daí!{/size}"

            show treino_fenju fenju5 with dissolve

            fen "{size=15}De-desculpa...{/size}"

            hide treino_sayuri with dissolve

            "..."

            show treino_sayuri close3 with dissolve

            s "Obrigada, [mc]. Essa menina é um problema às vezes."

            mc envergonhado "De nada."

            s "Então, o que eu tava falando..."
        "Não falar nada":


            $ renpy.block_rollback()

            $ fenju_naocontou = True

            "Eu sei que é mancada com a [s], mas acho que a [fen] precisa de uma pausa."

            "E além disso eu nem tenho nada a ver. Se ela tá se comportando ou não não é responsabilidade minha."

            mc desculpa "Sei..."

    s "Não importa o que você faz. Ser o melhor exige muita força de vontade, persistência e principalmente resignação."

    mc desconfiado "Resignação?"

    s "Sim. Tem horas que você vai se revoltar contra as coisas. Que você vai achar que tá errado, que estão te enganando..."

    s "Só que é nessa hora que você precisa colocar seu objetivo na frente. Você precisa pensar o que é mais importante."

    s "É desse jeito que a gente arranca força pra continuar. Não importa quanto tempo, não importa o sol ou a dor no corpo."

    mc desculpa "Puxa, [s]. Parece realmente complicado."

    show treino_sayuri close1 with dissolve

    s "É que você é bonzinho e se preocupa com as pessoas, [mc]."

    mc envergonhado "Sei lá. Parece tão diferente do meu dia a dia."

    s "Talvez não seja tão diferente assim. Você se esforça bastante também, né?"

    mc "Haha. Não sei se igual vocês... mas pensando bem até que eu passo por poucas e boas também."

    s "Tá vendo? As coisas são assim."

    menu:
        "Você tem razão.":


            $ renpy.block_rollback()

            $ sayuri_amizade += 2

            mc charmoso "Acho que você tem razão. Se a vida fosse fácil, tava todo mundo paradão sem fazer nada."

            s "Hihi..."

            mc desconfiado "Que foi?"

            s "Seu comentário foi engraçado."

            mc "Ei..."
        "Mas... a [fen] é só uma menina ainda.":


            $ renpy.block_rollback()

            mc desculpa "Eu entendo... só que a [fen] é só uma garota. Ela tem o que? 14 anos?"

            show treino_sayuri close3 with dissolve

            s "Ela tem 13 anos."

            mc "Então."

            s "Mas pra uma ginasta essa é a hora certa. Se ela perder a oportunidade, tudo vai pro buraco."

            s "Quanto antes ela chegar no pico, mais tempo ela terá para refinar seus movimentos e maior a chance dela conquistar o mundo."

            mc "..."

            s "Eu sei que isso pode ser difícil de entender. Mas ela escolheu isso."

            mc "Sei..."

            s "..."

            mc envergonhado "Não quero estragar nosso passeio com isso."

    mc normal "Bom. Vamos nessa?"

    if fenju_naocontou:

        show treino_fenju fenju5 with dissolve

        "Opa. A [fen] voltou. Que sorte."

        s "Sim.... [mc]?"

        mc envergonhado "Ah! Vamos."
    else:


        s "Sim."

    menu:
        "A [fen] vai ficar ali no sol?":


            $ renpy.block_rollback()

            $ sayuri_amizade -= 2

            mc desconfiado "A [fen] vai ficar ali?"

            show treino_sayuri close2 with dissolve

            s "Ah? Sim, vai."

            mc "Ela tá tanto tempo no sol. Isso não faz mal?"

            show treino_sayuri close3 with dissolve

            s "..."

            mc "..."

            s "Faz parte do treino dela, [mc]."

            mc desculpa "Então tá. Desculpa me intrometer."

            s "Tu-tudo bem."
        "Então bora.":


            $ renpy.block_rollback()

            mc normal "Tô ansioso. Vamo lá."

            s "Vamos."

    scene chinatown templo with Dissolve(1.0)

    mc preocupado "Vai ser um bom passeio só pra chegar até o centro do bairro."

    show sayuri normal with dissolve

    s "Já cansou só de pensar?"

    mc zerado "Engraçadinha. Tá passando tempo demais com a [g]."

    s "Acho que é verdade. Ela tá meio carente nos últimos tempos."

    mc triste "Que droga. O que será que houve?"

    s "Vamos andando e te falo."

    mc normal "Tá."

    scene black with dissolve

    "..."

    play sound "audio/som_7_cidade_chinesa.mp3"

    scene chinatown rua with Dissolve(1.0)

    pause

    mc concentrando "E não é que a gente chegou?"

    show sayuri normal with dissolve

    s "Você tá precisando fazer um pouco de exercício, [mc]."

    python:
        if renpy.android:
            mc_fisico = PythonSDLActivity.pegaFpontos()

    if mc_fisico > 4:

        mc normal "Pior é que eu tô correndo bastante de manhã, viu?"

        s "Que legal."

        mc zerado "Mas acho que ainda não é o suficiente pra aguentar a Cidade Chinesa."

        s "Haha. Bobo."
    else:


        mc envergonhado "Preciso mesmo."

    mc desculpa "Então. Você tava falando da [g]."

    show sayuri triste with dissolve

    s "Não sei se eu devo falar das coisas dela. Eu tenho medo que ela fique brava comigo."

    menu:
        "É melhor você não contar então.":


            $ renpy.block_rollback()

            $ sayuri_amizade += 2

            mc desculpa "Então acho melhor você não falar. Ela confia em você."

            show sayuri normal with dissolve

            s "Obrigada, [mc]. Você sempre entende minhas coisas."

            mc envergonhado "Relaxa."
        "Você sabe que pode confiar em mim.":


            $ renpy.block_rollback()

            mc charmoso "Você sabe que pode confiar em mim."

            s "Hmmm..."

            if sayuri_amizade >= 27:

                $ sayuri_contou_caio = True

                s "Ok. Mas por favor não fala nada pra ela."

                mc normal "Prometo."

                s "..."

                s "É que tem um rapaz que não larga do pé dela..."

                if j3_ouviu_p4:

                    s "O nome dele-"

                    mc bravo "É Caio, né?"

                    show sayuri desesperada with dissolve

                    s "Co-como você sabe?"

                    "Ixi. Como vou explicar pra ela que eu ouvi a [g] falando disso com a Carol enquanto tomava banho na faculdade?"

                    "A [s] vai acabar comigo."

                    mc envergonhado "Foi a [g] que me falou quando eu fui com ela na faculdade."

                    s "Ah... Entendi..."

                    show sayuri triste with dissolve
                else:


                    s "O nome dele é Caio."

                    mc desculpa "Entendi."

                s "E esse Caio é um babaca. Eu já falei pra [g] parar de dar atenção pra ele."

                s "Só que..."

                mc desculpa "Ela continua vendo ele."

                s "Eu sei que ela nem quer, mas sei lá, a [g] é assim."

                mc "..."

                s "Daí essas coisas acontecem e ela vai ficando cada vez mais triste."

                "Droga. Tadinha da [g]. Eu vou tentar ajudar ela de algum jeito."
            else:


                s "Desculpa, mas acho que é melhor não, [mc]."

                mc desculpa "Não esquenta."

                "Que droga. A [s] não confia em mim o suficiente pra contar um segredo desses."

                "Preciso fazer ela se sentir mais segura comigo."

    mc normal "Deixando isso de lado. E se a gente comer alguma coisa no [chi]?"

    show sayuri normal with dissolve

    s "Eu adoraria. Fico feliz que você não tenha mais preconceito com lámen."

    if bao_pontos > 0:

        mc "Muito mais do que só comer..."

        s "Como assim?"

        mc envergonhado "Eu tenho ajudado o [chi] com os lámens."

        s "Verdade?!"

        mc "Sim."

        show sayuri envergonhada with dissolve

        s "Que legal, [mc]! Não sabia!"

        mc "Não é nada demais. Ele só precisava de uma força."

        s "Achei bem legal mesmo. Vou passar uma hora lá pra comer um lámen que você preparar."

        mc feliz "Haha! Combinado."
    else:


        mc envergonhado "Desde nosso último encontro eu não tenho mais isso."

        s "Fico muito feliz."

        mc normal "..."

    mc normal "Sei até o caminho. Siga o mestre."

    s "Certo!"

    hide sayuri with dissolve

    "..."

    scene chinatown lamen with Dissolve(1.0)

    pause

    mc "Viu só? Já sei o caminho."

    show bao normal with dissolve

    chi "Bom dia, crianças."

    show bao normal at direita with move

    show sayuri normal with dissolve

    s "Oi, senhor [chi]."

    show sayuri normal at esquerda with move

    s "Tudo bem?"

    chi "Ai Fen! Que surpresa!"

    show sayuri incerta with dissolve

    s "Senhor [chi]..."

    chi "Já disse para não se incomodar com os devaneios deste velho."

    show sayuri normal with dissolve

    s "..."

    show bao falando with dissolve

    chi "Ah. E a [fen] não estava com você, Fen?"

    s "?"

    s "Ela tá no templo treinando."

    chi "Certeza? Não faz nem dois minutos eu vi ela passando ali pelo outro lado."

    show sayuri pensando with hpunch

    s "QUÊ?!"

    chi "Ela passou correndo na direção do templo."

    s "Não acredito! Aquela pestinha!"

    s "Desculpa, [mc]. Nosso passeio vai ter que ficar pra outro dia!"

    mc preocupado "[s]. Você va-"

    s "Não posso deixar ela-"

    hide sayuri with moveoutright

    chi "Opa."



    show bao pensando with dissolve

    chi "Tadinha dela..."

    mc preocupado "O que aconteceu?"

    chi "..."

    mc serio "Fala o que tá acontecendo, [chi]!"

    chi "Calma, [mc]."

    chi "Acho que você vai entender tudo agora."

    mc desconfiado "Entender?"

    show fenju k_incerta at entra_esquerda with dissolve

    mc surpreso "[fen]!"

    fen "!"

    show bao falando with dissolve

    chi "Eu disse para ter calma, [mc]. Vai acabar assustando ela."

    mc desculpa "Desculpa. Não quero te assustar, [fen]."

    fen "..."

    mc preocupado "O que isso significa? Por que você enganou a [s]?"

    chi "As coisas não são simpl-"

    mc bravo "Já tô cansado desse seu jeito, velho! Para de me enrolar!"

    fen "!"

    chi "..."

    fen "Eu..."

    show bao normal with dissolve

    chi "Calma, [fen]. Vai ficar tudo bem."

    chi "[mc]. Eu entendo que você pode estar meio confuso, mas confie em mim."

    chi "Logo a Ai Fen vai voltar e a [fen] não pode estar mais aqui."

    mc serio "Por que?"

    chi "Só escute."

    chi "Preciso que você leve ela daqui."

    mc surpreso "Como?!"

    fen "!"

    mc envergonhado "Desculpa..."

    "Droga. Tudo o que eu falo assusto essa menina. Ela consegue ser pior que-"

    chi "Leve ela com você para a ilha. Passe o dia todo com ela. Se possível, deixe ela dormir na sua casa e voltar só amanhã."

    mc surpreso "Por que tudo isso?!"

    chi "Eu prometo que te contarei tudo em outra oportunidade. Você pode ou não fazer isso?"

    mc "..."

    fen "..."

    "Droga. Esta é uma decisão muito séria. Isso pode influenciar minha relação com a [s]."

    "O mais fácil seria eu só negar. Pra que me envolver nesse rolo todo?"

    "Só que o [chi] parece tão preocupado. E olha o estado dessa menina. Eles precisam muito de mim..."

    label s5_fenju_escolha:

        "Ajudar eles ou não? Que merda eu escolho?"

        menu:
            "Tudo bem. Vou ficar com ela.":


                $ renpy.block_rollback()

                $ s5_ajudou = True

                mc desculpa "Tudo bem. Pode deixar ela comigo."

                show fenju k_sorrindo with dissolve

                fen "!"

                show bao pensando with dissolve

                chi "Ufa..."

                mc "Vou quebrar essa pra vocês. Mas depois o senhor vai ter que me explicar tudo sobre isso aqui."

                chi "Obrigado, [mc]. Realmente ficarei te devendo essa."

                jump s5_fenju
            "Não quero nada com essa tramóia":


                $ renpy.block_rollback()

                "Isso tá me cheirando muito mal. Não quero fazer parte disso."

                fen "..."

                chi "..."

                "Droga! Eles tão me olhando com esses olhos desesperados!"

                "Certeza que eu não vou ajudar eles?"

                menu:
                    "Certeza. Não vou ajudar eles.":


                        $ renpy.block_rollback()

                        "Não posso arriscar minha relação com a [s] por causa deles."

                        mc desculpa "Desculpa [chi], [fen]. Eu quero ajudar vocês, mas não posso assim."

                        fen "!"

                        chi "É uma pena, [mc]. Mas vamos dar um jeito. Venha, [fen]. Não temos muito tempo."

                        hide bao with dissolve

                        fen "..."

                        mc desculpa "Desculpa, [fen]."

                        fen "..."

                        hide fenju with dissolve

                        "Eu sei que é complicado. Mas não tenho o que fazer."

                        "Vou procurar a [s]."

                        "Não preciso contar pra ela o que eles tão armando. Não vou ajudar, mas também não quero atrapalhar."

                        "..."

                        jump s5_apos_fenju
                    "Espera... deixa eu pensar de novo.":


                        $ renpy.block_rollback()

                        "Droga! Não consigo decidir. Deixa eu pensar..."

                        "..."

                        jump s5_fenju_escolha

    label s5_fenju:

        fen "Obrigada..."

        mc charmoso "Finalmente você falou comigo."

        fen "!"

        show fenju k_incerta with dissolve

        fen "..."

        mc zerado "Já te assustei, né?"

        show bao falando with dissolve

        chi "Não temos mais tempo. A [s] vai chegar em breve."

        chi "[mc]. Aqui tem uma troca de roupas pra ela. Não precisa fazer nada fora do comum. Apenas dar um banho, alimentar, como qualquer criança."

        mc envergonhado "Faz bastante tempo que eu não cuido de criança..."

        chi "Não importa. Agora vão."

        mc normal "Ok. Pode ficar tranquilo. A gente volta amanhã."

        chi "Perfeito."

        hide bao with dissolve

        mc normal "Vamos."

        fen "..."

        hide fenju with dissolve

        mc zerado "Isso vai ser mais difícil do que parece..."

        scene black with Dissolve(1.0)

        "..."

        "..."

        $ tempo = 2

        scene cidade onibus with Dissolve(1.0)

        mc normal "Chegamos."

        show fenju k_incerta with dissolve

        fen "..."

        mc normal "Acho que podemos ir direto pro meu apê. Você precisa de um banho."

        fen "..."

        mc zerado "Você treinou a manhã toda. Deve tá fedendo."

        fen "!"

        show fenju k_sorrindo with dissolve

        fen "Hihi..."

        mc desconfiado "O que foi?"

        show fenju k_incerta with dissolve

        fen "..."

        mc zerado "..."

        menu:
            "Você não vai falar nada?":


                $ renpy.block_rollback()

                mc zerado "Você não vai falar nada mesmo?"

                show fenju k_falando with dissolve

                fen "E-e-e..."

                fen "..."

                mc envergonhado "Bom... pelo menos você tá tentando."

                show fenju k_sorrindo with dissolve

                fen "Hihi..."
            "Só me seguir.":


                $ renpy.block_rollback()

                mc normal "Bom. Só me seguir."

                fen "..."

        mc envergonhado "O [chi] chamou você de criança, né? Mas você já tem 13 anos. Já é uma mocinha."

        fen "..."

        mc "Não vou pedir pra você me dar a mão, mas toma cuidado."

        show fenju k_sorrindo with dissolve

        fen "Hihi..."

        fen "Tá."

        mc surpreso "!"

        "Ela falou! Mas é melhor eu fingir que nem ouvi pra ela não se assustar."

        scene black with dissolve

        scene ilha parque with Dissolve(1.0)

        mc normal "Tamo quase lá."

        mc desconfiado "[fen]?"

        show fenju k_falando with dissolve

        fen "Bonito."

        mc normal "Você gostou?"

        show parque dia with dissolve

        mc desconfiado "Eu nunca entendi direito essa estátua. Eu acho que é um polvo."

        fen "É um polvo. A gente come bastante no templo."

        hide parque with dissolve

        mc normal "Que bacana. Você vive no templo?"

        fen "!"

        fen "..."

        mc tarado "Esqueceu que não é pra falar comigo, né? Haha!"

        show fenju k_incerta with dissolve

        fen "..."

        mc normal "Não tem problema. Pode ir no seu tempo."

        show fenju k_sorrindo with dissolve

        fen "..."

        mc "Meu apartamento é logo ali."

        scene ape_geral with Dissolve(1.0)

        mc normal "Lar doce lar."

        if casa:

            mc charmoso "É um apê top de linha. Claro que eu não tinha dinheiro pra comprar, mas consegui por conta de uns rolos aí."
        else:


            mc envergonhado "É pequeno, mas... é aconchegante..."

        mc normal "Fique à vontade, tá?"

        show fenju k_incerta with dissolve

        fen "O-obrigada..."

        mc normal "Você quer tomar um banho agora?"

        fen "Si-sim."

        mc normal "Tá. O banheiro é logo ali."

        if not casa:

            mc normal "Aqui está sua roupa que o [chi] deixou comigo."

            mc envergonhado "Como a casa não tem cômodo, eu vou esperar você lá fora. Volto em 10 minutos."

            fen "Tá."

            scene black with Dissolve(1.0)

            mc zerado "Se eu tivesse uma casa maior não precisaria passar por essas coisas..."
        else:


            mc normal "Vem aqui."

            scene ap banheiro with Dissolve(1.0)

            mc normal "Aqui é o banheiro. Eu vou estar lá na sala. Pode ficar tranquila."

            show fenju k_sorrindo with dissolve

            fen "Obrigada."

            mc normal "Relaxa."

            mc "Aqui estão suas roupas. Bom banho."

            scene ap quarto with Dissolve(1.0)

            "Agora eu fecho a porta aqui e ela fica tranquila."

            scene ape_tv with Dissolve(1.0)

            "A melhor coisa que eu fiz foi ter me mudado pra este apê."

            play sound "audio/som_16_chuveiro.mp3"

            "Espero que ela aproveite bem a estadia. A menina tá precisando."

            "..."

        scene ape_geral with Dissolve(1.0)

        mc normal "Tudo pronto?"

        fen "Sim."

        show fenju acuada with dissolve

        fen "Obrigada."

        mc normal "Não tem o que agradecer. Você parece outra pessoa agora."

        fen "..."

        if casa:

            mc envergonhado "Ah! Aproveitei que tava em casa e acabei ficando à vontade também."

            fen "Tudo bem."

        mc normal "Você tá com fome? Podemos sair pra comer."

        fen "Agora não."

        mc "Ok. Então fique à vontade."

        fen "[mc]."

        mc surpreso "O-oi!"

        fen "É..."

        if casa:

            mc normal "Senta aqui."

            fen "Tá."

            scene fenju ap_conversando with Dissolve(2.0)

            pause
        else:


            show fenju falando with dissolve

            mc normal "..."

        fen "..."

        mc "Pode ir com calma. Eu não tenho pressa."

        if fenju_naocontou:

            fen "Obrigada por não ter contado pra [s] aquela hora."

            mc desconfiado "Aquela hora?"

            mc surpreso "Ah! Quando ela mandou você ficar sentada lá no templo."

            fen "..."

            mc envergonhado "Não esquente com isso."

            fen "Você foi muito legal comigo."

            mc "Não foi nada de mais..."
        else:


            "..."

            mc envergonhado "Já que você não vai falar, eu falo."

            mc desculpa "Desculpa por ter avisado a [s] que você saiu da posição aquela hora no templo."

            fen "!"

            fen "Tu-tudo bem..."

            mc "Desculpa mesmo. Não queria ferrar seu esquema."

            fen "..."

        mc "Inclusive, eu achei seu treino um pouco puxado demais."

        if s5_rigida:

            mc desculpa "Até a [s] que é tão de boa parecia outra pessoa falando com você."

            mc "É como se ela tivesse falando com, sei lá... deixa pra lá."

            fen "..."

        mc "Até essas marcas de machucado. Você não tá pegando pesado demais, não?"

        mc "Isso não faz mal pra você? Digo assim, no futuro não pode te prejudicar?"

        if not casa:

            show fenju acuada with dissolve

        fen "..."

        fen "Eu... vou ser a maior ginasta... do mundo. Tudo isso faz parte do meu treino."

        fen "É isso que meus pais queriam."

        mc "Seu pais?"

        fen "Sim. Quando eles me levaram pro templo... já faz muitos anos."

        mc desconfiado "Como é? Seus pais te levaram pro templo? Você não mora com eles?"

        fen "Não. Desde que eles me deixaram, eu nunca mais vi eles."

        mc "Você não sente saudades?"

        fen "Acho que um pouco. Mas eu vou poder voltar pra casa quando terminar meu treinamento."

        mc desculpa "Sei..."

        if casa:

            scene fenju ap_conversando_feliz with Dissolve(2.0)

            pause
        else:


            show fenju sorrindo with dissolve

        fen "Quando eu voltar pra casa... queria um dia ir pra praia."

        mc "Praia? Por que a praia?"

        fen "Porque ela é bem diferente. Eu nunca consegui ver a praia."

        mc "Quê?! Sério mesmo que você nunca foi na praia?!"

        if not casa:

            show fenju acuada with dissolve

        fen "..."

        mc envergonhado "Não quero acabar com seu sonho, mas a praia não tem nada de incrível."

        fen "Toda aquela areia, as ondas, a água... as pessoas felizes..."

        mc desculpa "..."

        fen "A praia é o lugar mais incrível do mundo."

        mc "..."

        mc charmoso "Então tá!"

        if casa:

            mc "Levanta."

        fen "?!"

        mc "Nós vamos agora pra praia."

        scene ape_geral

        show fenju desesperada with hpunch

        fen "Agora?!"

        mc feliz "Calma. Não é nada de outro mundo. Só vamos na praia e aproveitamos pra comer algo por lá."

        show fenju falando with hpunch

        fen "Mas! Mas!"

        mc "Para de ser tonta. Vamos lá."

        mc "Vem."

        hide fenju falando with moveoutleft

        fen "Ei!"

        scene black with dissolve

        "..."

        scene ilha praia_entrada with Dissolve(1.0)

        pause

        mc normal "Tamo chegando. Agora é só descer aqui a rampa e já tamo na areia."

        fen "..."

        "..."

        play sound "audio/som_13_praia.mp3"

        scene ilha praia with Dissolve(2.0)

        pause

        mc feliz "Tcharãã!"

        fen "..."

        mc normal "E aí?"

        fen "..."

        mc desconfiado "Fala alguma coisa, [fen]."

        show fenju acuada with dissolve

        fen "..."

        mc preocupado "Não gostou?"

        fen "..."

        fen "A praia é tão... bonita."

        mc feliz "!"

        fen "Eu consigo sentir a areia no meu pé. Só é um pouco quente..."

        mc "Haha! Fica de sandália."

        fen "Não. Eu quero sentir."

        mc normal "Vamos dar um pulo na água agora?"

        show fenju desesperada with hpunch

        fen "Nã-Não!!"

        mc desconfiado "Qual o problema?"

        show fenju falando with dissolve

        fen "Eu nunca fui na água. É perigoso."

        mc feliz "Haha! Para de ser boba, [fen]."

        mc normal "É só não ir muito pro fundo."

        fen "Não. A areia tá bom por hoje..."

        fen "E-e-eu tô com fome!"

        show fenju acuada with dissolve

        fen "Posso comer alguma coisa?"

        mc zerado "Você tá falando isso só pra eu te deixar em paz..."

        fen "..."

        mc normal "Bom. Você quem manda."

        mc "Vamos comer ali naquele quiosque."

        fen "Tá."

        scene black with dissolve

        "..."

        mc normal "Uma coca e uma salada de frutas por favor."

        "Rapaz" "Saindo, senhor."

        scene fenju praia_quiosque with Dissolve(2.0)

        pause

        fen "Eu não..."

        fen "Eu não posso tomar refrigerante..."

        menu:
            "Tudo bem. Pode deixar aí que eu tomo.":


                mc "Não tem problema. Pode deixar que eu tomo."

                fen "Mas obrigada."
            "Pode tomar. É um dia especial.":


                $ fenju_coca = True

                mc "Haha! É um dia especial! A gente até fugiu da Cidade Chinesa."

                fen "..."

                fen "T-tá. Verdade. Eu não lembro o gosto do refrigerante."

                mc "Então aproveita."

        fen "Nem acredito que eu vim pra praia. Ainda parece tão estranho."

        mc "E eu ainda não acredito que você tá falando."

        fen "!"

        fen "..."

        mc "Nã-não!"

        fen "Brincadeira."

        mc "Ufa..."

        fen "É..."

        mc "Que foi?"

        fen "Desculpa. Mas como é seu nome?"

        mc "Você não sabe meu nome?"

        fen "..."

        mc "É [mcc]. Prazer."

        fen "[mcc]..."

        mc "Mas pode me chamar só de [mc]."

        fen "Tá."

        fen "É... [mc]..."

        scene fenju praia_converando_triste with Dissolve(2.0)

        pause

        fen "Vo-você... me acha chata?"

        mc "Como assim? Claro que não. Por que chata?"

        fen "É... É que é a primeira vez que eu falo tanto com alguém na minha vida."

        mc "Só nas últimas horas, né? Porque antes..."

        fen "Eu não gosto muito de falar. Eu tenho medo de falar as coisas erradas e as pessoas se zangarem comigo."

        fen "E se as pessoas não me acharem legal? E se as pessoas não gostarem do que eu falar?"

        mc "Sei..."

        fen "Eu sempre achei mais fácil só ficar quieta e só falar o que fosse muito importante."

        fen "Só que você é a pessoa mais legal que eu já vi. Você parece que não liga pra nada."

        mc "Mais legal? Haha! Ei! E como assim não ligo pra nada?!"

        fen "..."

        fen "Você deixa eu falar o que eu quero. E não fica bravo comigo."

        menu:
            "As pessoas ficam bravas com você?":


                mc "Por que eu ia ficar bravo com você? As pessoas brigam com você lá?"

                fen "..."

                fen "Sim."

                mc "Isso é ruim, [fen]."

                fen "Mas eu tô acostumada. Eu sei que elas querem que eu seja a melhor na ginástica."

                mc "Mesmo assim..."
            "Claro que não vou ficar bravo.":


                mc "Claro que não vou brigar com você. Você é só uma adolescente."

                mc "Eu sei que adolescentes são meio chatos às vezes, mas a gente espera que os adultos segurem a barra, né?"

                fen "..."

        scene fenju praia_quiosque with Dissolve(2.0)

        fen "Você é diferente, [mc]. Você é diferente de tudo que eu vi."

        mc "Você também é bem diferente do que eu tinha imaginado."

        fen "Co-como assim?"

        mc "Você é super articulada, [fen]. Pra quem nem falava nada, você fala muito bem."

        fen "Não sei..."

        mc "É sim. Você até fala de um jeito meio culto. Bem melhor que eu haha!"

        mc "Falando nisso, você até me lembra um pouco a [s] nesse sentido."

        fen "Sé-sério?!"

        mc "Sim! Olha aí!"

        fen "O que?"

        mc "Vocês duas falam super bem, mas quando alguma coisa deixa vocês nervosas, vocês gaguejam na primeira palavra da frase."

        fen "E-eu nunca... acho que você tá certo..."

        mc "Hahaha!"

        fen "Hihi."

        fen "Será que teria algum problema se eu nunca mais voltasse pro templo?"

        mc "QUÊ?!"

        fen "..."

        fen "Ta-talvez... eu pudesse só deixar a ginástica e viver na praia."

        mc "Essa é uma decisão meio complicada, [fen]."

        fen "É que hoje foi tão diferente de tudo! A vida longe da Cidade Chinesa parece tão incrível! Tão tão bacana!"

        mc "Entendo..."

        mc "E se a gente pensar sobre isso amanhã? O sol tá quase se pondo, a gente precisa voltar pra casa."

        fen "Mas já?!"

        fen "Eu quero outra salada de frutas!"

        if fenju_coca:

            fen "E o-outra coca!"
        else:


            fen "E dessa vez vo-vou querer uma coca gelada!"

            $ fenju_coca = True

        mc "Ok! Calma."

        "Acho que é a primeira vez que eu vejo ela se comportando igual uma criança..."

        scene black with Dissolve(1.0)

        "..."

        $ tempo = 3

        scene ilha praia with Dissolve(1.0)

        pause

        mc normal "Caraca. Já tá super escuro e eu nem tinha notado."

        show fenju falando with dissolve

        fen "A gente já vai voltar, né?"

        mc "Você precisa descansar, mocinha."

        fen "Tá..."

        show fenju sorrindo with dissolve

        fen "Eu gostei muito de vir na praia. Foi mais legal do que eu imaginei."

        mc feliz "Que bom. Fico feliz."

        show fenju acuada with dissolve

        fen "Será que... u-um dia a gente podia vir de novo?"

        mc normal "Claro."

        fen "Então tá combinado."

        mc "Ok. Combinado."

        mc "Agora vamos."

        fen "Tá..."

        hide fenju with dissolve

        "Bora pra casa."

        scene black with Dissolve(1.0)

        "..."

        scene ape_geral with Dissolve(1.0)

        if casa:

            mc normal "Pode dormir na minha cama que eu vou ficar no sofá."

            mc "Vai se ajeitando que eu já vou ver como você tá."

            fen "Tá."

            scene ap mc_cozinhando1 with Dissolve(1.0)

            "Vou preparar um hamburguer pra ela comer. Tô achando que ela passou o dia todo só com a salada de frutas."

            "..."

            "Pronto."

            scene ap sala with Dissolve(1.0)

            mc normal "[fen]. Preparei um lanchi-"

            scene fenju ap_dormindo with dissolve

            "Eita... já dormiu."

            "Deve ter sido um dia cansativo pra ela."

            "O que esse pessoal do templo tá na cabeça? Fazer uma garota desse tamanho passar por tudo isso."

            "Crianças precisam de tempo. Elas precisam de espaço pra crescer... não de toda essa pressão."

            "Eu sei que não deve ser fácil cuidar de uma criança ou de um adolescente."

            "Mas se nós que somos adultos não vamos fazer o certo, o que podemos pedir deles que ainda são tão jovens?"

            "Não é com violência e gritaria que se ajuda um jovem. É com suporte e carinho. Criar um ambiente que eles se sintam seguros e não isto aqui!"

            "Melhor ginasta do mundo o caralho! Esse povo tá doido!"

            "E pensar que a [s] pode tá envolvida nisso também..."

            scene ap mc_dormindo3 with Dissolve(1.0)

            "Espero que a [fen] se sinta um pouquinho melhor depois de hoje."

            scene black with Dissolve(1.5)

            "..."
        else:


            mc normal "Pode dormir tranquila na minha cama."

            mc "Eu vou dar uma passada no bar e ficar por lá até ficar de manhã."

            show fenju acuada with dissolve

            fen "Nã-não precisa, [mc]. A casa é sua. Não quero-"

            mc normal "Só relaxa. Eu preciso conversar com o [gar], que é o dono do bar também."

            mc "Fecha a porta pelo lado de dentro e só abre depois que você acordar."

            mc "Descansa bem."

            fen "Tá. Até amanhã."

            mc "Até."

            scene ilha parque with Dissolve(1.0)

            "É melhor que eu deixe ela tranquila."

            "Se eu tivesse um {b}apartamento com mais cômodos{/b} até daria pra ser diferente."

            "Mas não tem problema. Vou encher o [gar] até o sol raiar."

            "E quando for hora daquelas festas loucas dele, eu dou uma andada por aí."

            "..."

            scene mc bar_celular with Dissolve(1.0)

            "Deve ter sido um dia cansativo pra [fen]."

            "O que esse pessoal do templo tá na cabeça? Fazer uma garota desse tamanho passar por tudo isso."

            "Crianças precisam de tempo. Elas precisam de espaço pra crescer... não de toda essa pressão."

            "Eu sei que não deve ser fácil cuidar de uma criança ou de um adolescente."

            "Mas se nós que somos adultos não vamos fazer o certo, o que podemos pedir deles que ainda são tão jovens?"

            gar "[mc]. Vamos fechar."

            mc "Beleza."

            "..."

            scene mc parque_sentado_noite with Dissolve(1.0)

            "Não é com violência e gritaria que se ajuda um jovem. É com suporte e carinho. Criar um ambiente que eles se sintam seguros e não isto aqui!"

            "Melhor ginasta do mundo o caralho! Esse povo tá doido!"

            "E pensar que a [s] pode tá envolvida nisso também..."

            "..."

            scene mc parque_sentado with Dissolve(1.0)

            "..."

            "O dia amanheceu. Hora de voltar."

        $ dia += 1
        $ tempo = 1

        scene ape_geral with Dissolve(1.0)

        mc normal "Bom dia!"

        show fenju sorrindo with dissolve

        fen "Bom dia."

        mc desculpa "Pronta pra voltar?"

        fen "Sim."

        mc normal "Você não parece tão triste com a Cidade Chinesa hoje."

        fen "..."

        show fenju acuada with dissolve

        fen "Eu tô me sentindo muito melhor hoje. O-obrigada por tudo."

        fen "Não quero mais fugir do meu treino."

        fen "Falta pouco pra minha primeira competição e se eu conseguir medalha de ouro poderei ver meus pais."

        mc preocupado "..."

        fen "Eu só preciso me esforçar nesse finalzinho e tudo vai dar certo."

        mc desculpa "Sei... E se..."

        mc normal "Se você precisar de alguma coisa, pode contar comigo."

        fen "T-tá."

        mc normal "E com certeza o [chi] gosta muito de você também."

        mc normal "Você não precisa enfrentar isso sozinha. Procure as pessoas que gostam de você de verdade."

        fen "T-tá."

        mc desconfiado "Que foi?"

        show fenju falando with dissolve

        fen "Só que... e se as pessoas ficarem cansadas de mim? Por causa que eu só tenho problemas?"

        mc charmoso "Não seja boba. Quem gosta de você de verdade, nunca vai cansar de você."

        mc "Você é uma jovem incrível, [fen]. E é normal a gente se sentir com problemas às vezes."

        mc normal "Nós adultos passamos por essas coisas também. E por isso a gente vai poder te ajudar."

        fen "..."

        mc "Faça as coisas no seu tempo e quando precisar de alguém, fale com o [chi] e ele me avisa também."

        fen "Tá."

        mc "Agora vamos."

        scene black with Dissolve(1.0)

        "..."

        play sound "audio/som_7_cidade_chinesa.mp3"

        scene chinatown geral with Dissolve(1.0)

        pause

        mc normal "Chegamos. Vamos procurar o [chi]."

        fen "..."

        scene chinatown lamen with Dissolve(1.0)

        mc normal "Bom dia, [chi]. Sua encomenda. Entregue sem avarias."

        show bao normal with dissolve

        chi "Que bom ver vocês."

        chi "Tudo ocorreu bem?"

        mc "Sim. A [fen] se comportou muito bem."

        chi "É verdade, [fen]?"

        fen "..."

        fen "Eu vou pra casa do [chi]. Tchau."

        mc desconfiado "O que deu nela?"

        show bao pensando with dissolve

        chi "Crianças..."

        scene bao mc_conversando with Dissolve(1.0)

        mc "Eu juro que não fiz nada! Não sei porque ela tá assim!"

        chi "Calma, [mc]. Está tudo bem. É fácil ver porque ela ficou cabisbaixa."

        mc "Fácil pra você..."

        chi "Eu queria te agradecer por tudo o que você fez. Você realmente ajudou a [fen]."

        mc "[chi]... o que eles tão fazendo com essa menina não é certo."

        chi "Eu sei que você tá incorfomado, mas me escute."

        chi "As coisas aqui são diferentes do que você está acostumado."

        mc "Só qu-"

        chi "Não. Você não pode olhar com os seus olhos para todas as pessoas."

        mc "Quê?"

        chi "Existem vários tipos de pessoas, [mc]. Cada uma com sua verdade. Você não pode impor a sua verdade para todos."

        mc "Não sei se eu entendi, mas essa menina tá em sofrimento!"

        chi "Sim. Eu não vou te impedir de fazer o que você quer fazer. Mas não se esqueça, nada é tão simples."

        mc "..."

        chi "A Ai Fen está aqui na Cidade Chinesa procurando a [fen] ainda. Vá atrás dela."

        mc "Sério?! Preciso falar com ela agora!"

        chi "Boa sorte, [mc]."

        scene chinatown esquina with Dissolve(1.0)

        pause

        "Preciso achar ela. Não acredito que o [chi] deixou a [s] procurando esse tempo todo."

        "..."

        jump s5_apos_fenju

    label s5_apos_fenju:

        scene black with Dissolve(1.0)

        "..."

        $ tempo = 2

        scene chinatown rua with Dissolve(1.0)

        "Onde será que a [s] tá? Sei lá quantas horas que eu tô procurando ela. Cristo! O sol já tá se pondo."

        "..."

        show sayuri assustada with hpunch

        s "[mc]!"

        mc surpreso "[s]!"

        s "Eu tenho que-"

        mc bravo "Calma!"

        s "!"

        mc desculpa "Desculpa, mas tá tudo bem. A [fen] tá legal."

        s "Como você sabe?!"

        mc "O [chi] me falou. Ele viu ela de novo."

        show sayuri pensando with dissolve

        s "Não, [mc]. Você não sabe! Não posso perder ela de vista se não-"

        mc preocupado "Se não o quê?"

        s "Na-nada."

        menu:
            "Eu já to cansado! Fala o que vai acontecer [s]!":


                $ renpy.block_rollback()

                $ sayuri_amizade -= 2

                "Eu já tô cansado dessa enrolação toda. Por que ninguém me fala o que tá havendo?!"

                mc serio "Fala pra mim o que vai acontecer, [s]!"

                s "!"

                show sayuri zonza with dissolve

                s "Eu não posso, [mc]! Eu não posso!"

                mc preocupado "[s]... Eu sou seu amigo."

                if sayuri_intencao == "namoro":

                    mc "Não só amigo! Eu já disse que quero ser mais que um amigo pra você!"

                mc "Por que você não pode me contar?"

                s "Você! Você não vai entender, [mc]!"

                mc triste "Como você sabe?"

                s "O mundo não entende. As pessoas não entendem o que eu tive que passar. O que eu TENHO que passar."

                s "É medonho, [mc]! Eu não tenho coragem!"

                mc "[s]..."
            "Tudo bem. Calma.":


                $ renpy.block_rollback()

                mc desculpa "Calma. Vai ficar tudo legal."

                s "Não..."

        mc desculpa "Eu só quero falar uma coisa."

        s "..."

        mc concentrando "Eu sei que você precisa resolver isso. Que é urgente. Mas, só me deixa falar uma coisa."

        s "..."

        "Calma, [mc]."

        "Pensa. Esse é o ponto mais importante desde que você conheceu a [s]."

        "Você sabe que tem alguma merda acontecendo aqui."

        "O medo nos olhos da [s]."

        if sayuri_e4 != "fracasso":

            "O jeito que a treinadora dela falou aquele dia no banho."

        if s5_rigida:

            "A forma como a [s] trata a [fen] durante os treinos."

        if s5_ajudou:

            $ sayuri_amizade -= 2

            "Tudo o que eu descobri sobre a [fen] ontem. O jeito que aquela garota tava."

            "Machucada, desesperada..."

        "É impossível negar que tem alguma coisa muito foda acontecendo aqui. Alguma coisa muito suja... muito terrível."

        scene sayuri mc_declaracao with Dissolve(2.0)

        pause

        mc "[s]..."

        "O que eu falar pra [s] agora vai mudar tudo o que acontece entre a gente. Vai mudar meu futuro com ela."

        "Mas não é só isso. Eu vou fazer parte desse círculo? Eu vou aceitar o que fizeram com ela e com a menina?"

        "E minha ética? E o que tá dentro de mim? Eu vou compactuar com o que eles fazem aqui na Cidade Chinesa?"

        label s5_escolha_final:

            "Eu só tenho uma escolha."

        menu:

            "Não importa o que vocês fazem. Eu quero ficar com você." if sayuri_intencao == "namoro":

                $ renpy.block_rollback()

                "Se eu escolher ficar com a [s], eu vou permitir que eles continuem fazendo o que eles fazem."

                "É óbvio que uma pessoa sozinha igual eu não vai conseguir mudar todo esse sistema."

                "Não posso ter uma esperança irreal."

                "Eu realmente quero fazer parte disso?"

                menu:
                    "Sim. Pela [s].":


                        $ renpy.block_rollback()

                        "Sim! Eu estou disposto a passar por cima disso pra ficar com a [s]. Ela é o mais importante pra mim agora."
                    "Não. Preciso pensar um pouco mais":


                        "Não sei! Preciso pensar um pouco."

                        jump s5_escolha_final

                label s5_namoro:

                    mc "Eu sei que a Cidade Chinesa é um mundo diferente. Eu sei que tem alguma coisa aqui que não é normal."

                    mc "É tudo tão diferente da minha realidade. É outro mundo praticamente."

                    mc "Mas, sabe... eu não saberia nada disso se não fosse por você."

                    mc "Pra mim, o que importa sempre foi você, [s]. Tudo isso só faz sentido por sua causa."

                    mc "Eu disse pra você, lá na loja de roupas, que eu queria ser mais que um amigo. E eu falei sério."

                    mc "Não importa o inferno que você tá metida. Eu quero você. Você me quer também?"

                    s "[mc]..."

                if sayuri_amizade >= 25:

                    $ sayuri_namoro = True

                    s "Sim! Eu quero!"

                    s "P-por favor! Fica comigo, [mc]!"

                    if sayuri_e4 == "namoro":

                        "Da outra vez ela me beijou. Só que hoje eu tô pronto."

                    mc "Vem aqui."

                    scene sayuri mc_beijo_namoro with Dissolve(2.0)

                    pause

                    pause

                    "Dessa vez eu não tô com medo."

                    "Dessa vez eu vou segurar você e não vou deixar você fugir, [s]."

                    "Não quero mais que você sofra sozinha."

                    "Eu tô com você."

                    window hide

                    pause

                    scene sayuri mc_declaracao with Dissolve(2.0)

                    mc "Só pra deixar claro. Agora é oficial."

                    s "S-s-s-s..."

                    mc "Sim?"

                    s "S-sim..."

                    jump s5_final
                else:


                    s "[mc]..."

                    s "V-você é a pessoa mais especial que eu tenho agora. Você é a única pessoa que eu tenho..."

                    s "Eu preciso de você e você falar essas coisas pra mim..."

                    s "M-mas eu não posso ser mais que sua amiga agora."

                    "Droga! Por que?! O que será que eu fiz de errado?!"

                    s "Você pode ser meu amigo? P-por favor?"

                    "Não tenho como negar isso pra ela. Mesmo quebrando meu coração, eu gosto dela demais pra negar..."

                    mc "Eu entendo, [s]..."

                    jump s5_amizade

            "Eu posso ser seu amigo, mas não posso aceitar o que vocês fazem." if sayuri_intencao != "namoro":

                $ renpy.block_rollback()

                "Se eu escolher ser amigo da [s], eu vou permitir que eles continuem fazendo o que eles fazem."

                "É óbvio que uma pessoa sozinha igual eu não vai conseguir mudar todo esse sistema."

                "Não posso ter uma esperança irreal."

                "Eu realmente quero fazer parte disso?"

                menu:
                    "Sim. Pela [s].":


                        $ renpy.block_rollback()

                        "Sim! Eu estou disposto a passar por cima disso pra ser amigo dela. Ela é o mais importante pra mim agora."
                    "Não. Preciso pensar um pouco mais":


                        "Não sei! Preciso pensar um pouco."

                        jump s5_escolha_final

                mc "Eu sei que a Cidade Chinesa é um mundo diferente. Eu sei que tem alguma coisa aqui que não é normal."

                s "[mc]..."

                label s5_amizade:

                    mc "Mas isso não me importa. Eu quero ser seu amigo. Eu quero tá com você pra superar tudo isso."

                    mc "Você é uma mulher incrível e eu quero estar do seu lado, como seu melhor amigo, pra viver isso com você."

                    mc "Não quero que você se sinta sozinha nunca mais."

                    mc "Quando você precisar de alguém pra te defender, ou só pra te dar força pra continuar. Eu vou estar lá."

                    mc "Você, a [fen] também. Vocês vivem em um inferno. Eu consigo ver isso, não sou burro."

                    mc "Eu vou fazer tudo o que eu puder pra ajudar vocês... e até se for possível, salvar vocês disso tudo."

                    s "Eu não mereço você, [mc]... Alguém como você..."

                    s "Alguém que tá disposto a deixar tudo e confiar em mim. Confiar nas minhas decisões."

                    s "Eu não preciso ser salva, mas eu preciso de alguém do meu lado. Que me dê força pra continuar."

                    mc "Eu vou ser esse alguém, [s]. Pode confiar em mim."

                    s "Muito obrigada, [mc]. Por ter me escolhido e ficar do meu lado, mesmo depois de tudo."

                    jump s5_final
            "Eu não posso fazer parte dessa loucura. O que vocês fazem é errado.":


                $ renpy.block_rollback()

                "Se eu escolher não aceitar o que eles fazem, minha relação com a [s] com certeza vai sofrer."

                "Eu não vou compactuar com esta loucura, mas muito provavelmente ela vai se {b}afastar de mim{/b}."

                "Essa é minha decisão?"

                menu:
                    "Sim. Não posso fazer parte disto.":


                        $ renpy.block_rollback()

                        "Sim! Tudo isso aqui é errado. Não posso aceitar o que acontece aqui, mesmo que isso me afaste da [s]."
                    "Não sei... Preciso pensar um pouco mais":


                        "Não sei! Preciso pensar um pouco."

                        jump s5_escolha_final

                $ sayuri_adeus = True

                mc "Eu sei que você, sua técnica, e todos os outros que eu nem conheço tem suas razões."

                mc "Mas certas coisas não estão certas. O que a [fen] passa, até o jeito que você vive... sempre com medo de tudo."

                mc "Eu não posso compactuar com isso. Eu... eu não consigo entender! Tá longe demais do que é aceitável!"

                mc "Eu gosto muito de você. Você é uma pessoa incrível, mas você precisa enxergar o que tá acontecendo na sua volta!"

                mc "Olhe pra [fen]! Ela é uma criança!"

                s "[mc]..."

                mc "E por gostar demais de você. Eu não posso aceitar isso."

                mc "Eu não vou te abandonar. Mas eu não posso aceitar as coisas como elas estão agora."

                mc "Eu preciso de um tempo. Eu preciso pensar. Eu quero te ajudar, mas ainda preciso descobrir como fazer isso."

                mc "Você entende?"

                s "..."

                s "E-eu não preciso dessa ajuda que você tá falando."

                s "Quero alguém que possa me entender. Que possa me dar força e não questionar o que eu faço."

                s "Você não entende nada, [mc]!"

                s "Você vem com essa história de ajudar, mas você não sabe de nada!"

                s "Sai daqui!"

                scene chinatown rua with hpunch

                mc angustiado "[s]!"

                jump s5_finalizar

    label s5_final:

        s "Minha cabeça tá girando. Eu preciso ir."

        mc "Cla-claro! Você procurou a [fen] esse tempo todo! Ela tá bem. Vai pra casa descansar."

        s "T-tá..."

        mc "Eu vou estar com você quando você precisar. Pode confiar em mim."

        s "Tá."

        s "Até depois, [mc]."

        mc "Até, [s]. Fica bem."

    label s5_finalizar:

        scene chinatown rua with Dissolve(1.0)

        "Ela foi embora..."

        "Espero que eu tenha tomado a decisão certa."

        "Deixa eu voltar."

        "..."

        scene mc onibus with Dissolve(1.0)

        pause

        "Tudo que aconteceu... foi demais até pra mim eu acho."

        if s5_ajudou:

            "Tudo o que eu descobri sobre a [fen]. Desde o começo eu sabia que essa menina não tava legal."
        else:


            "Eu acabei não ajudando o [chi] e a [fen]. Espero que eles fiquem bem."

            "Talvez eu devesse ter ajudado, ainda mais sabendo que tem alguma coisa muito ruim acontecendo na Cidade Chinesa."

        if sayuri_namoro:

            "E eu finalmente tô namorando com a [s]. Nem acredito que ela aceitou."

            "Ela é a coisa mais importante pra mim. Não importa o que eles fazem lá. Ela que me interessa."

            "Droga... por que mesmo pensando assim eu ainda sinto que fiz algo errado?"

            "Não posso pensar assim!"

        elif not sayuri_adeus:

            "Mesmo assim eu vou ser o apoio que a [s] precisa. A vida que elas levam nesse lugar parece terrível."

            "Ela precisa apoio. Ela precisa de alguém que possa dar força pra ela e estar lá quando precisar."

            "Eu vou ser esse apoio, não importa o que aconteça."

            "Droga... por que mesmo pensando assim eu ainda sinto que fiz algo errado?"

            "Não posso pensar assim!"
        else:


            "Esse povo é maluco. Eu não vou compactuar com isso. Com esse erro."

            "Não posso permitir que eles continuem tratando a [s] e a [fen] da forma como eles tratam."

            "O [chi] diz que nada é simples, mas tem coisas que passam a linha do aceitável."

            "A [s] é uma mulher incrível, mas não vou acabar com a minha moral por causa dela."

            "Eu me sinto bem comigo mesmo. Isso que importa."

    "De uma forma ou de outra, tudo isso ainda é muito misterioso pra mim."

    "O que eles realmente fazem lá? E como a [s], a [fen] e até o [chi] estão metidos nisso tudo?"

    "Eu preciso descobrir. Preciso saber tudo sobre essa Cidade Chinesa!"

    "Eu sou um paparazzo e acima de tudo eu sou um jornalista. E minha função é trazer a verdade pro mundo!"

    scene black with Dissolve(2.0)

    mc zerado "E não ser despedido... claro..."

    window hide



    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()



    $ v17_fim = True

    $ proibido_salvar = False
    $ show_quick_menu = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v17_fim","sayuri","personagem")



    scene sayuri_banheiro with Dissolve(1.0)

    s "Ufa... finalmente um banho..."

    "Aconteceu tanta coisa hoje..."

    label say5_premium1:

        pass

    menu:
        "Será que a [s] tá legal?":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_46

                jump say5_premium1

            "Fiquei o dia todo atrás da pestinha... acho que deu mais de 24 horas procurando ela..."

            "Só que depois..."

            if not sayuri_adeus:

                scene sayuri_banheiro1 with Dissolve(1.0)

                "O [mc] resolveu ficar do meu lado... isso foi tão legal..."

                "Eu sei que é difícil pras pessoas de fora entenderem, mas ele me aceitou e aceitou a cultura do nosso bairro."

                "Eu fiquei tão feliz..."

                if sayuri_namoro:

                    "E-e-e-e-e... depois... a g-gente..."

                    "Será que é o-oficial agora? A gente tá namorando mesmo?"
                else:


                    "Ele quis ser meu amigo... de verdade..."

                    "Mas esse é um passo... s-se a gente se conhecer melhor... t-talvez..."

                s "Agora eu tenho qu-"

                scene sayuri_banheiro2 with hpunch

                g "Oi, mana!"

                s "J-júlia?!"

                g "Você entrou agora no banho, né?"

                s "S-sim... o que você tá fazendo aqui?"

                g "Mana... eu queria tomar um banho com você..."

                menu:
                    "Por quê?":


                        s "C-como assim? Por quê?"

                        g "Eu achei que a gente ficou meio mal depois daquele dia no quarto..."

                        s "Você passou um pouco do ponto comigo, [g]. Tirar minha roupa e me a-apalpar..."

                        g "Era só uma brincadeira, mana..."

                        s "Mesmo assim. Esse tipo de brincadeira..."

                        g "E-eu sei! Por isso eu queria vir aqui e pedir desculpas."

                        s "Só que no banho?"

                        g "Aqui você não pode fugir de mim!"

                        s "Cada uma... o que eu faço com você, [g]?"

                        g "Deixa eu entrar aí com você?"

                        s "A-aqui? Agora?"

                        g "É!"

                        menu:
                            "Se você se comportar.":


                                s "Tudo bem... mas só se você se comportar, tá?"

                                g "Eu prometo!"

                                scene black with dissolve

                                "{i}splash splosh{/i}"

                                g "Ebaaa!"

                                s "C-cuidado..."

                                scene sayuri_banheiro3 with Dissolve(1.0)

                                pause

                                s "A gente tá tão perto..."

                                g "Você lembra que a gente tomava banho assim antes?"

                                s "Sim... mas a gente ainda não era adultas, né?"

                                g "Eu não acho que as coisas precisam mudar... meu amor por você não mudou nesse tempo."

                                s "O m-meu também... mas você tem que entender que as pessoas podem pensar coisas..."

                                g "A gente nunca precisou dos outros, mana. Você sempre tava lá pra mim. E isso que importa."

                                s "[g]..."

                                s "Eu sei que não foi fácil pra você... e eu continuo gostando muito de você. Mas não é a mesma coisa."

                                g "Mas você acha ruim quando eu fico com você assim?"

                                "Hmm... o que eu sinto?"

                                s "N-não sei... mas não é essa a questão. É o que as pessoas vão pensar."

                                g "E eu quero saber o que VOCÊ acha. Porque é você que me importa, mana."

                                s "Eu... não é que me incomode... mas é que tem uma coisa acontecendo..."

                                g "Uma coisa? É o [mc], né?"

                                s "A-ah..."

                                g "Eu conheço você, mana. Você tá gostando dele. Até onde vocês foram?"

                                s "N-não sei se eu consigo falar sobre isso..."

                                scene sayuri_banheiro4 with Dissolve(1.0)

                                g "Ei... eu sou sua maninha. Você pode contar tudo pra mim, lembra?"

                                s "J-júlia... a-ah..."

                                g "Aposto que eu posso ajudar você também."

                                s "Huh?!"

                                g "Eu tenho muito mais experiência que você com garotos. Eu posso te ensinar como fazer a cabeça deles."

                                s "E-eu... eu não sei se eu quero fazer a cabeça dele..."

                                g "Você quer, mana... eu aposto que você quer. É assim que você conquista um homem."

                                s "Eu tô ficando com vergonha..."

                                g "Quer que eu te ensine como você beija?"

                                scene sayuri_banheiro4 with hpunch

                                s "Quê?!"

                                g "Eu vou te mostrar como beijar uma boca e ele não vai resistir..."

                                s "Não sei, [g]... isso parece algo pessoal demais... não acho que eu deva aprender com você..."

                                g "Para de ser boba... vem aqui... eu vou te mostrar."

                                "A [g] tem mais experiência, só que... isso não parece certo... e agora?"

                                menu:
                                    "Eu vou aprender por mim.":


                                        s "Acho melhor eu aprender essas coisas sozinha."

                                        g "Mas e se ele não gostar?"

                                        s "E-então ele vai ter paciência comigo. Eu não tenho que ter medo desse tipo de coisa."

                                        g "Você é realmente uma campeã, mana... tanta confiança... eu queria ser assim também."

                                        s "Obrigada. Agora vamos sair?"

                                        g "É uma pena... bora..."
                                    "Tudo bem... como é?":


                                        s "Se você acha que é uma boa... ok..."

                                        g "Fecha os olhos."

                                        s "Hm?"

                                        g "Fecha logo. Você vai entender."

                                        s "T-tá..."

                                        scene black with dissolve

                                        s "Pronto."

                                        g "Você faz assim... chega bem perto dele..."

                                        g "Daí você para um pouquinho... pra criar aquela tensão... sempre com muita calma."

                                        "E-eu tô sentindo a respiração dela... ai..."

                                        g "E daí sim você..."

                                        scene sayuri_banheiro5 with Dissolve(1.0)

                                        pause

                                        s "Hm?!"

                                        g "Hmmm..."

                                        s "Ju-"

                                        g "Só fica quietinha... abre a boca um pouquinho..."

                                        s "Nnnhh...."
                                        scene snew_ani21 with Dissolve(1.0)
                                        g "Assim, mana... sente minha boca..."

                                        "O que eu tô fazendo... o beijo da [g] tá... eu não consigo..."

                                        g "Só que vocês são adultos, então você não pode parar num beijinho desses."

                                        s "N-na-"

                                        g "Daí ele vai querer mais... ele vai descer assim..."

                                        scene sayuri_banheiro6 with Dissolve(1.0)

                                        g "E pegar em você."

                                        s "Ah-ahh!?"

                                        g "Se ele partir pra cima, você só aceita, fica quietinha enquanto ele se aproveita."

                                        s "Ju- Angh!"

                                        g "Você é maravilhosa, mana. Nenhum homem ia aguentar não se aproveitar de você assim."

                                        "O que ela tá fazendo?!"

                                        menu:
                                            "Chega, [g]!":


                                                s "Chega, [g]! Nng! I-isso é demais!"

                                                g "Você não pode ir contra, mana! Eu tô te en-"

                                                s "Sai! Agora!"

                                                g "!!!"

                                                s "Eu tô falando sério!"

                                                scene black with vpunch

                                                g "Mana!"

                                                s "Você exagerou, [g]!"

                                                g "Manaaa!"
                                            "Não consigo falar...":


                                                s "Aannh..."

                                                g "É gostoso, não é?"

                                                "Eu... não consigo respirar direito... meu corpo..."

                                                s "Ahn... ahnn..."

                                                g "Assim mesmo, mana... só deixa comigo que eu vou cuidar de você."

                                                s "{i}puf puf{/i}"

                                                g "Você é deliciosa..."

                                                g "Mas quando ele tiver te pegando, ele não vai parar enquanto você não falar."

                                                g "Ele vai querer mais que seu pescoço, que sua boca... ele vai querer você inteirinha..."

                                                s "?!"

                                                scene sayuri_banheiro7 with Dissolve(1.0)

                                                g "Ele vai mamar em você... e usar seu corpo inteiro pra se satisfazer!"

                                                s "Ahhnn! Ag!"

                                                g "Isso, mana! A gente se gosta, vamos aproveitar!"
                                                scene snew_ani20 with Dissolve(1.0)
                                                s "Jú-júlia... Ai... v-você... ahn..."

                                                g "Eu sei... eu também tô gostando bastante. É muito bom ficar com quem a gente ama, né?"

                                                s "Agnn!"

                                                scene sayuri_banheiro8 with Dissolve(1.0)

                                                g "Eu quero que você goze, mana. Eu quero te dar muito prazer!"

                                                s "Ahn! AAHN!"

                                                g "Isso! Se solta, mana!"

                                                s "Júlia! ANNNGG!!"

                                                scene sayuri_banheiro8 with vpunch

                                                g "ISSO! AAGNN!"

                                                s "Ah..."
                                                scene snew_ani03 with Dissolve(1.0)
                                                g "Mana..."

                                                s "{i}puf puf{/i}"

                                                g "O q-que eu fiz?"

                                                s "Hm?"

                                                g "Não! Não era isso!"

                                                s "[g]?!"

                                                g "NÃOO!"

                                                scene sayuri_banheiro9 with vpunch

                                                s "[g]! O que foi?!"

                                                g "Desculpa! Eu sou uma idiota! Adeus!"

                                                s "A-ah! Q-quê?!"

                                                g "{i}Buaah{/i}"

                                                s "!?"

                                                "O que... que deu nela?"

                                                "E o que foi isso? Eu e ela... como que eu deixei uma coisa dessas acontecer?"

                                                if sayuri_namoro:

                                                    "E justo agora que eu e o [mc] tamo namorando..."

                                                "Se alguém descobrir isso vai ser um escândalo..."

                                                "Mas não foi culpa dela. Eu também deixei as coisas acontecerem..."

                                                "Tá na cara que tem alguma coisa errada acontecendo com ela..."

                                                "E eu tenho que cortar isso. Pode ser que ela fique triste... mas a gente não pode fazer isso de novo."

                                                "Eu sou mais velha. Eu tenho que parar com isso agora."
                            "Melhor não.":


                                s "N-não, [g]. É melhor você ir. Eu vou tomar um banho rápido e já tô indo."

                                g "Mas, mana..."

                                s "Por favor, [g]."

                                g "D-desculpa... t-tá..."

                                "O que passa na cabeça dessa garota?"
                    "Por favor, sai daqui!":


                        s "E-eu não me sinto bem com você me vendo assim, [g]. Sai por favor!"

                        g "Mas, mana..."

                        s "Sai, [g]!"

                        g "D-desculpa... t-tá..."

                        "O que passa na cabeça dessa garota?"
            else:


                "... o [mc] decidiu ficar contra mim... e o nosso bairro..."

                "Eu pensei que ele ia ficar do meu lado... mas ele não conseguiu enxergar nossa verdade."

                "Acho que... a gente nunca vai se falar de novo..."

                "Nem tô com vontade de tomar banho. Acho que vou direto pra cama."
        "Não me interesssa.":


            pass

    scene black with dissolve

    jump call_cidade

label sayuri_evento6:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s6_save", extra_info="s6_save")

    $ iconchefe += 1
    $ estou_na_cidade = False

    $ sayuri_cel_msg5_r = "começado"

    hide screen celular

    "Opa. A [s]..."

    if sayuri_adeus:

        "Eu fui bem duro com ela no outro dia. Eu disse que não ia tolerar as coisas que eles tavam fazendo."

        "Ela ficou super brava e parecia bem decepcionada comigo."

        "Mas não tinha como eu ficar quieto e só fingir que nada daquilo tava acontecendo."

        "Eu ainda acho que fiz a coisa certa."
    else:


        "Mesmo sabendo que tem algo de estranho na Cidade Chinesa e que a [s] tá envolvida de alguma forma, eu fiquei do lado dela."

        if sayuri_namoro:

            "A gente ainda assumiu nossa relação. A gente começou a namorar oficialmente."
        else:


            "Eu disse que ficaria do lado dela como um verdadeiro amigo. Não posso dar pra trás agora."

        "Eu preciso entender melhor o que tá acontecendo com ela, com a garotinha, a mestra e até como o [chi] tá envolvido."

        "Só depois eu vou poder julgar o que eles fazem."

    "Deixa eu responder ela."

    "..."

    $ sayuri_cel_msg5_r = "respondido"

    "Pronto."

    "Agora deixa eu ligar pra ela agora."

    "{i}Tuuu... Tuuuu...{/i}"

    if sayuri_adeus:

        s "Alô? [mc]?"

        mc serio "Oi."

        s "E-eu... queria conversar com você."

        s "Eu acho que a gente n-não acabou bem aquele dia e e-e-eu queria conversar melhor com você."

        mc desculpa "Ok. Eu também acho. A gente precisa conversar."

        s "Você pode vir até a Cidade Chinesa agora de manhã?"

        mc "Sim. Tô indo pra aí."

        s "Obrigada. Até logo."

        mc "Até."
    else:


        s "O-oi..."

        if sayuri_namoro:

            mc charmoso "Oi, linda."

            s "L-l-li-li-linda?"

            mc "Calma, [s]. Agora a gente tá namorando, certo? Isso é normal."

            s "T-t-t-tá..."
        else:


            mc normal "Fala aí, [s]. Tudo bem?"

            s "T-tudo..."

            s "É..."

            s "E-eu ainda não acostumei com alguém, assim, me conhecendo tão bem..."

            mc desculpa "Você não tem muitos amigos, né?"

            s "N-não..."

            mc normal "Mas eu vou valer por vários! Você vai ver."

            s "Haha... T-tá."

        s "..."

        mc "Você pediu pra eu ligar, bem..."

        s "Ah... É..."

        "Até hoje ela tem uma certa dificuldade com o telefone. Muito fofa."

        s "Aquele dia v-você disse que vai ficar do meu lado, mas que queria saber mais sobre tudo."

        mc charmoso "Isso."

        s "E-então... eu conversei com minha mestra e ela permitiu que você viesse conhecer onde a gente vi-vive."

        "Onde eles vivem? Como assim? E quem é a 'gente'?"

        mc desconfiado "O que você quer dizer?"

        s "É... v-você vai ver."

        s "Você pode vir até a Cidade Chinesa agora de manhã?"

        mc "Sim. Posso passar aí agora."

        s "Ah! Obrigada. E-então a gente se vê."

        if sayuri_namoro:

            mc charmoso "Beijo."

            s "!!!"

            s "B-b-b-b-bb-beb-be..."

            "..."

            "{i}Tu tu tu-{/i}"

            mc envergonhado "Desligou..."

    "Eu tenho a impressão que ela quer falar algo muito importante pra mim."

    "Tenho que ir pra lá urgente."

    "Só que antes... eu vou dar um trato no look."



    scene black with dissolve

    "E a [s]?"

    scene sayuri_quarto with Dissolve(1.0)

    label say6_premium1:

        pass

    menu:
        "O que será que a [s] tá pensando?":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_47

                jump say6_premium1

            scene sayuri_quarto3 with Dissolve(1.0)

            s "Nem acredito que eu vou ver o [mc]... ele aceitou conhecer a Cidade Chinesa!"

            if sayuri_adeus:

                "Ele falou aquelas coisas negativas pra mim, mas quando ele ver como a coisa funciona eu tenho certeza que ele vai mudar de ideia."

            "A gente tem se aproximado cada vez mais... e eu tenho cada vez mais vontade de..."

            "{i}toc toc{/i}"

            s "Hm?"

            g "Mana?"

            s "J-júlia..."

            "A gente não se falou direito desde aquele dia no banho... com que cara eu olho pra ela agora?"

            g "Eu posso... falar com você agora?"

            "Bem agora?"

            menu:
                "Ok... pode entrar...":


                    s "Ok... pode vir."

                    g "Ok..."

                    scene black with dissolve

                    scene sayuri_quarto20 with Dissolve(1.0)

                    pause

                    s "Eu vou sair daqui a pouco. Se você puder falar rápido."

                    g "Pode deixar, mana. Eu não quero te atrapalhar."

                    g "Eu queria... só pedir desculpa por eu ter invadido seu banho aquele dia."

                    s "[g]... você-"

                    g "Eu sei. Eu tô exagerando esses tempos. Eu não sei o que tá acontecendo comigo."

                    s "Tem a ver com o [mc]?"

                    g "Quê?! Com aquele tonto?! C-claro que não!"

                    s "Tem certeza?"

                    g "Tenho, mana... eu juro... eu tenho minhas coisas também. Não tá fácil na faculdade."

                    s "É aquele menino?"

                    g "Ele também... mas tem a Carol também..."

                    s "[g]... eu já te falei isso várias vezes. A vida não é fácil, mas você complica ela mais do que já é."

                    g "Eu sei! Mas... não é de propósito..."

                    s "Você precisa ser responsável pelo que você faz. Não pode colocar a culpa na 'vida' como se ela fosse injusta."

                    g "Mas a vida é injusta!"

                    s "Não importa. Você é a responsável pela sua vida. Precisa reconhecer suas responsabilidades e agir como adulta."

                    g "Só que... as coisas vão acontecendo..."

                    s "A maioira das pessoas é assim. Faz as coisas sem pensar e quando dá merda reclama que a vida é difícil."

                    g "Você é séria demais, mana... Deve ser por isso que você é tão bem sucedida."

                    s "Você sabe que eu também tenho minhas coisas, mas eu não posso usar isso de desculpa pra fazer coisa errada."

                    s "Não importa se a faculdade tá díficl ou se seus 'amigos' dão problema. Você precisa me respeitar."

                    g "Eu sei... desculpa... eu vou fazer o possível... você me perdoa? Não vai fugir de mim?"

                    s "Claro que não vou fugir de você, [g]... você é minha irmã querida."

                    g "Eba! Posso te abraçar?"

                    s "P-pode."

                    scene sayuri_quarto21 with Dissolve(1.0)

                    pause

                    g "Que delícia... eu tava com medo que você não quisesse mais ser minha mana."

                    s "Que absurdo. Eu sempre vou ser sua irmã."

                    g "Promete?"

                    s "Prometo."

                    g "Hmm... então tá..."

                    s "Agora eu vo-"

                    g "É... eu queria me desculpar com você. Posso?"

                    s "Como assim? Eu já te desculpei."

                    g "Não. Eu quero fazer algo pra você. Posso te fazer uma massagem?"

                    "A [g] fala as coisas... mas parece que ela quer se aproveitar de mim de novo falando assim..."

                    "O que eu faço? Eu aceito?"

                    menu:
                        "Tudo bem...":


                            s "T-tudo bem..."

                            g "Que bom, mana!"

                            scene sayuri_quarto22 with Dissolve(1.0)

                            pause

                            g "..."

                            s "O-oi?"

                            g "Mana... Quando eu tô com você eu sinto uma coisa diferente no meu peito."

                            s "[g]..."

                            g "Eu sei que é estranho, mas eu queria que você soubesse como você é importante pra mim."

                            g "Toda vez que a gente tá perto eu tenho vontade de sentir você."

                            s "A-ah... e-eu não sei o que... falar..."
                            scene snew_ani23 with Dissolve(1.0)
                            g "Não precisa falar nada. Eu só quero que você aceite meu amor."

                            s "Mas-"

                            g "Eu quero fazer uma massagem em você. Eu posso, né?"

                            s "P-pode."

                            g "Eu quero que você tire a roupa. Pra não atrapalhar."

                            s "Q-quê?!"

                            g "Vai logo, mana."

                            "Eu sinto que as coisas tão saindo do controle de novo... e-eu obedeço ela?"

                            menu:
                                "Tirar a roupa":


                                    s "C-como você é mimada às vezes..."

                                    g "Isso. Eu adoro quando você me mima, mana."

                                    s "Eu vou tirar... m-mas olha só, hein."

                                    g "Tá. Tira logo."

                                    "Ai..."

                                    scene black with dissolve

                                    scene sayuri_quarto23 with Dissolve(1.0)

                                    pause

                                    s "Hmm..."

                                    g "Tá bom?"

                                    s "Tá melhor do que eu imaginava... você realmente sabe massagear, Jú."

                                    g "Claro que eu sei. Pegar nos outros é uma das minhas especialidades..."

                                    s "Ah..."

                                    g "Seu corpo é perfeito, mana."

                                    s "Você acha?"

                                    g "Você é magrinha, mas sua bunda é grande. Essa vida de atleta ajudou, né?"

                                    s "É... eu nunca me preocupei com isso. Acho que é natural."

                                    g "O que ia ter de mulher puta contigo por falar assim. A maioria de nós se mata pra isso, viu?"

                                    s "Hmm... desculpa..."
                                    scene snew_ani13 with Dissolve(1.0)
                                    g "Eu vou me aproveitar bastante de você..."

                                    s "Ai, [g]... precisa falar assim?"

                                    g "Mas você não acha melhor assim? Saber que eu tô me divertindo com você?"

                                    s "C-como é?"

                                    g "Nós duas peladas aqui... eu pegando em você inteira assim..."

                                    s "J-júlia!"

                                    g "Eu sei que você também gosta, mana. Não precisa esconder de mim. Eu não vou pensar errado de você."

                                    s "Você... t-tá entendendo errado. E-eu..."

                                    g "Vira aqui."

                                    scene sayuri_quarto24 with Dissolve(1.0)

                                    g "Você quer, não quer? Se fosse tudo bem..."

                                    s "E-ah..."

                                    g "Você lembra na banheira? Foi gostoso, não foi?"

                                    s "I-isso não é certo, [g]..."

                                    g "Não pensa nisso, mana. Pensa no que você quer."

                                    s "E-eu gosto do-"
                                    scene snew_ani14 with Dissolve(1.0)
                                    g "Sshh... você não gosta de mim também?"

                                    s "M-"

                                    g "Então aproveita..."

                                    s "J..."

                                    g "Fica quietinha..."

                                    s "N-"

                                    scene sayuri_quarto24 with vpunch

                                    s "Não! Agora não! Eu não posso!"

                                    g "Tem certeza?"

                                    s "T-tenho... [g]... a gente conversa depois..."

                                    g "Promete?"

                                    s "P-prometo..."

                                    g "Então tá. Eu vou cobrar, tá?"
                                    scene snew_ani14 with Dissolve(1.0)
                                    s "T-tá..."

                                    g "O que você vai fazer agora?"

                                    s "Agora eu tenho que sair pra encontrar o... você sabe... eu tô atrasada..."

                                    g "Vocês tão se vendo muito ultimamente. Será que eu tenho que me preocupar de verdade?"

                                    s "N-não seja boba..."
                                "Parar por aqui":


                                    s "N-não... melhor a gente parar por aqui..."

                                    g "Por que, mana?"

                                    s "Já tá tudo certo entre a gente. Eu prometo. Não precisa fazer isso."

                                    g "Tem certeza? Mas eu queria..."

                                    s "O-outra hora, Ju. Agora eu tenho que sair pra encontrar o... você sabe..."

                                    g "Vocês tão se vendo muito ultimamente. Será que eu tenho que me preocupar de verdade?"

                                    s "N-não seja boba..."
                        "Outra hora.":


                            s "O-outra hora, Ju. Agora eu tenho que sair pra encontrar o... você sabe..."

                            g "Vocês tão se vendo muito ultimamente. Será que eu tenho que me preocupar de verdade?"

                            s "N-não seja boba..."

                    scene black with dissolve

                    scene sayuri_quarto with dissolve

                    g "Se você vai encontrar ele... você precisa se arrumar."

                    s "Eu tava pensando mesmo em dar uma mudada na aparência. Eu queria... mostrar uma nova pessoa pra ele."

                    g "Uau... isso parece sério. Mas eu tenho uma ideia pra você então. A gente vai ter que fazer algo com seu cabelo."

                    s "Com meu cabelo?"

                    g "Seu cabelo é maravilhoso, mas se você quer parecer uma pessoa nova, a gente pode deixar você mais adulta."

                    g "Ou será que ele prefere uma novinha?"

                    s "C-claro que não!"

                    g "Então pode deixar que eu vou cuidar de você."

                    s "Mas e se eu demorar?"

                    g "Demorar faz parte, mana. Se ele sabe algo sobre mulheres, ele vai esperar quietinho. Você quem manda na relação."

                    s "J-júlia... rsrs..."
                "A gente conversa outro dia.":


                    s "Desculpa... mas eu tô com pressa agora."

                    g "Mana..."

                    s "A gente vai conversar outra hora, tá?"

                    g "Ok..."

                    "Agora eu tenho que me preparar pra ver o [mc]!"
        "Deixa pra lá":


            pass

    scene black with dissolve

    scene ape_chuveiro with Dissolve(1.0)

    "Acho que tá bom. Agora deixa eu ir pra lá."

    "A Sayuri deve tá me esperando."

    call locomocao from _call_locomocao_11

    scene chinatown rua with Dissolve(1.0)

    "A [s] disse pra eu vir pra cá, mas será que ela tá no templo?"

    s "O-oi, [mc]..."

    mc surpreso "[s]!!"

    show sayuri n_sorrindo with Dissolve(1.0)

    s "Oi..."

    mc surpreso "!"

    s "..."

    mc "..."

    s "V-você tá me deixando sem jeito..."

    mc envergonhado "Desculpa... mas você tá tão d-diferente..."

    s "Eu só cortei um pouco e prendi o cabelo..."

    "Será que é só isso mesmo? Caraca, parece tão diferente."

    mc charmoso "Você ficou linda."

    s "Ah! O-obrigada..."

    if sayuri_adeus:

        show sayuri n_triste with dissolve

        s "Q-que bom que você veio. Eu tinha que conversar com você depois do que aconteceu."

        mc desculpa "Sei... eu também queria falar com você."

        s "Primeiro, eu queria pedir desculpas pelo jeito que eu falei com você. Eu fiquei muito irritada na hora, não sei por que..."

        mc envergonhado "Tudo bem. Isso n-"

        s "Não. Eu não devia ter falado daquele jeito. Me desculpa?"

        mc "C-claro, [s]."

        show sayuri n_sorrindo with dissolve

        s "Obrigada, de verdade."

        mc normal "Não foi nada."

        s "Mas não quero ficar só nas desculpas. Eu quero que você conheça mais tudo aqui antes de tomar uma decisão."

        mc desconfiado "Como assim?"
    else:


        s "E-eu te chamei porque tem algo muito importante que eu quero falar com você."

        mc preocupado "Certo."

    show sayuri n_incerta with dissolve

    s "Eu não sei o que o [chi] te falou. Eu não sei o que você viu ou ouviu, mas as coisas não são assim como parecem."

    s "E-eu não fui totalmente sincera com você. E eu queria, de verdade, que você visse mais sobre a Cidade Chinesa antes de julgar tudo."

    mc desculpa "Eu não quero que você tenha que passar por isso. Eu-"

    s "Não! Eu realmente quero..."

    show sayuri n_triste with dissolve

    s "Você é uma pessoa incrível, [mc]. O que você fez por mim durante esse tempo que a gente tá junto."

    s "Todas as pessoas que eu conheci já tinham me deixado depois desse tempo todo. E você, não."

    if sayuri_namoro:

        s "Eu nem acredito que a ge-gente t-t-t-tá... tá... a gente tá..."

        mc envergonhado "Namorando?"

        s "I-i-isso!"

    elif not sayuri_adeus:

        s "Eu não acredito como você quis ser meu amigo e me apoiar mesmo depois do que você pode ter visto."

    mc desculpa "Eu não fiz nada de mais..."

    show sayuri n_incerta with dissolve

    s "Você fez muito mais do que eu poderia pedir de alguém. Muito mais."

    s "E o mínimo que eu posso fazer agora é mostrar pra você o meu lado."

    s "Eu não vou falar que eu vou te mostrar a verdade. Eu só quero que você me acompanhe e veja."

    s "E você mesmo vai tomar sua decisão. E se no fim você achar que pode me apoiar, eu seria a mulher mais feliz do mundo!"

    menu:
        "Tudo bem. Eu quero ouvir seu lado.":


            mc desculpa "Eu quero ouvir seu lado mesmo..."

            mc "Não quero julgar algo sem antes saber a história toda."
        "Não sei se eu me sinto bem com isso.":


            $ sayuri_amizade += 2

            mc desculpa "[s]... Eu não sei se eu me sinto bem com isso."

            mc "Parece que eu sou um tipo de juíz, que vai decidir se algo tá certo ou não. Não é isso que eu quero."

            mc charmoso "Eu, mesmo quando pareço contra você, é porque eu quero seu bem. Eu quero ver você feliz."

            mc "Em nenhum momento eu disse que era contra você, ou até mesmo sua mestra."

            mc desculpa "Eu só não consigo entender tudo isso que está no entorno de vocês. Tipo, essa energia, essa máquina, sei lá como falar..."

            s "[mc]... eu entendo... mas é por isso que eu te peço. Venha comigo e veja com seus próprios olhos."

            mc concentrando "..."

    mc charmoso "Ok. Eu vou ver tudo."

    show sayuri n_sorrindo with dissolve

    s "Muito obrigada, [mc]."

    s "Você vai ver que a Cidade Chinesa é um lugar muito especial."

    s "Podemos não ser como outros lugares que você está acostumado, mas temos nossos pontos positivos, que superam e muito o outro lado."

    mc normal "Ok. Eu acredito em você. E pra onde vamos?"

    s "Ah... Vamos pra direção do templo. Venha."

    hide sayuri with dissolve

    menu:

        "Segurar a mão dela" if sayuri_namoro:

            $ sayuri_amizade += 2

            mc charmoso "Opa."

            s "E-ei! [mc]?!"

            mc "A gente é namorados agora, lembra?"

            s "S-sim... Tá..."
        "Acompanhar ela":


            "O que será que ela quer me mostrar?"

            "Tô ficando ansioso..."

    scene black with Dissolve(1.0)

    "..."

    scene chinatown caminho with Dissolve(1.0)

    mc normal "É aqui que vamos pro templo, né?"

    show sayuri n_sorrindo with dissolve

    s "Isso mesmo."

    s "Subindo aqui, você chega no pátio do templo. É lá que eu e a [fen] treinamos."

    mc desconfiado "Sempre no pátio?"

    s "Nem sempre. Temos o dojo também."

    mc "Do jô?"

    s "Isso. Dojo é um espaço em templos ou academias orientais onde a gente pode treinar ou meditar sem interferência."

    mc envergonhado "Não fazia ideia do que era."

    s "O dojo é bem diferente das academias que você está acostumado. Espero poder levar você lá um dia também."

    mc normal "Eu adoraria."

    s "Agora vamos por aqui. Estamos chegando."

    mc "Tá."

    scene chinatown portal with Dissolve(1.0)

    if xiangu_evento > 0:

        "Eita... aqui é onde fica aquela doida sentada..."

        "Ela não me deixa passar daqui de jeito nenhum."

    xu "Você não p-"

    show sayuri n_sorrindo with dissolve

    s "Oi."

    show sayuri n_sorrindo at esquerda with move

    s "Sou eu."

    show xiangu normal with dissolve

    xu "Ah. Perdão, [s]."

    show xiangu normal at direita with move

    s "Tudo bem."

    if xiangu_evento == 0:

        "E quem é essa? Com uma espada..."

        mc desconfiado "..."

    xu "E ele?"

    s "Não precisa se preocupar. Tenho autorização da Mestra pra trazer ele."

    xu "Isso é sério?"

    s "Sim. Foi um pedido pessoal meu e ela atendeu."

    xu "Isso é raro."

    s "Eu sei. Mas a situação exige."

    xu "Entendo... Podem passar."

    s "Obrigada. Vamos, [mc]."

    xu "..."

    hide xiangu with dissolve

    "Que formalidade foi essa? E como assim raro?"

    if xiangu_evento > 0:

        "Eu não consegui passar por esse portal de jeito nenhum antes. Mas parece que a [s] só precisou falar com ela."

    "Autorização da Mestra?"

    "Será a treinadora da [s]? Ela tipo permite que as pessoas passem por aqui?"

    s "[mc]?"

    mc normal "Ah, claro. Vamos, sim."

    scene black with Dissolve(1.0)

    "..."

    mc desconfiado "É minha primeira vez nesta parte do bairro."

    s "Obviamente."

    s "Agora cuidado com a escada."

    scene vila_triade entrada with Dissolve(1.0)

    pause

    mc surpreso "Uou!"

    s "Que foi? Impressionado?"

    menu:
        "Claro. Parece tipo um cenário de filme.":


            $ sayuri_amizade += 2

            mc surpreso "Parece um lugar de filme, sei lá."

            s "Haha... [mc]... e você não viu nada ainda."

            mc envergonhado "Desculpa. Não quero passar vergonha ao vivo."

            show sayuri n_interessada with dissolve

            s "Você é engraçado..."

            mc "Ei."

            s "N-não falo como brincadeira. É verdade. Você me diverte, [mc]."

            mc "Que bom..."
        "O lugar parece meio acabado...":


            mc desconfiado "Tá parecendo meio acabado... Isso é normal?"

            s "[mc]..."

            mc "Que foi? É sério!"

            show sayuri n_sorrindo with dissolve

            s "Ai ai..."

    s "Esta é uma área bem especial da Cidade Chinesa."

    s "As construções foram criadas quando o bairro foi criado, há centenas de anos."

    mc surpreso "S-sério?! Centenas?!"

    s "Sim. E o máximo que fizeram nas construções iniciais foi para manter as estruturas seguras."

    s "Quero dizer, foram estas construções que nossos antepassados criaram quando fundaram a cidade e nós as preservamos até hoje."

    mc normal "Isso é incrível, [s]."

    s "Eu também acho. Os chineses têm muito orgulho de seu passado e da sua história. Somos um povo muito ligado às nossas raízes."

    menu:
        "Isso é legal, mas mudança e melhora são importantes.":


            mc envergonhado "Isso é muito bacana na cultura, mas a gente precisa tá pronto pra mudanças também, né?"

            mc normal "Ficar preso no passado e não aproveitar o que foi descoberto é um desperdício, não acha?"

            show sayuri n_incerta with dissolve

            s "E-eu... não sei..."

            s "Desde pequena, nossa comunidade aprende a reverenciar nossa raíz e respeitar nossas tradições."

            s "É dito que um povo sem passado, é um povo sem futuro. É nisso que eu acredito."

            mc normal "Entendo. É realmente um ensinamento bem bonito."

            s "Não é verdade? Eu gosto muito dele."
        "Eu concordo completamente com isso.":


            $ sayuri_amizade += 2

            mc charmoso "Eu concordo completamente com isso."

            mc "No mundo de hoje as pessoas estão cada vez mais imediatistas. Sempre de olhos no futuro."

            mc "Acho muito legal quem consegue ver valor e preservar o que foi conquistado."

            s "Sim! Você entende isso também, [mc]. Isso me deixa feliz."

            s "Desde cedo a gente aprende que um povo sem passado, é um povo sem futuro. Eu concordo com isso."

            mc "Eu também. Muito legal."

    s "Mas vamos entrar. Você tem que ver tudo."

    mc normal "Claro. Vai na frente."

    hide sayuri with dissolve

    "..."

    scene vila_triade geral with Dissolve(1.0)

    pause

    "Olha pra esse lugar..."

    "Parece que eu viajei no tempo e no espaço pra um lugar desconhecido em uma era desconhecida."

    s "Lindo, não é?"

    mc envergonhado "Com certeza."

    s "Vem aqui. Tira seu sapato e vem aqui comigo."

    mc surpreso "T-tá!"

    s "Senta aqui comigo."

    mc surpreso "!"

    scene sayuri_vila_triade_sentada with Dissolve(1.0)

    pause

    "Ver a [s] vestida assim em um lugar como esse. Parece até um quadro."

    s "Q-que foi, [mc]? Por que você tá parado aí... m-me olhando?"

    menu:
        "Você tá linda, [s].":


            $ sayuri_amizade += 2

            mc charmoso "Sentada aí, com esse fundo... você tá tão linda, [s]."

            s "Q-quê?!"

            s "[mc]!"

            mc "Que foi?"

            s "Você... tá me deixando sem jeito... não faça isso por favor..."

            mc desculpa "T-tudo bem... desculpa."

            s "Mas obrigada..."

            mc charmoso "..."
        "N-não é nada...":


            mc envergonhado "Não é nada. Só achei o lugar realmente bonito."

            s "Eu sabia que você ia gostar."

            mc normal "Impossível não curtir, certo?"

            s "Certo."

    s "Sabe..."

    s "Desde que eu era muito pequena... eu sempre gostei deste lugar aqui."

    mc normal "Você nunca me falou sobre sua infância."

    s "Não é nada demais."

    mc "Eu gostaria de saber, se não tiver problema, claro..."

    s "Falar de mim assim... não sei..."

    s "Ok. A-acho que eu posso falar alguma coisa sem ser chata."

    mc "Ouvir sobre você nunca vai ser chato. Deixa eu me ajeitar aí."

    scene sayuri_ponte_mc1 with Dissolve(1.0)

    pause

    mc "Opa. Pronto."

    s "Hmm..."

    s "N-não tenho muito o que falar. Nunca fiz nada de especial..."

    mc "Tá brincando? Você é a maior atleta do país, [s]. Você se esquece disso?"

    s "E-eu sei... mas não tem nada de tão incrível nisso. É apenas o resultado do meu treino."

    s "Eu treino desde criança pra isso."

    s "Essas paredes... esse rio... eu me lembro deles desde que eu comecei a entender que eu tava viva."

    mc "Tão cedo assim?"

    s "Logo que eu completei a idade mínima, eu fui aceita como discípula do templo e meu treinamento começou."

    mc "Você e a [g] não passaram tempo juntas quando eram crianças?"

    s "Muito novas, não. Eu passei muito tempo longe da minha família. Esta era minha casa."

    mc "Não deve ter sido fácil..."

    s "Não foi fácil, ainda mais para uma criança. Mas era importante para meu crescimento."

    s "Minha mestra nunca foi fã de relacionamentos interpessoais..."

    mc "Como assim?"

    s "Como eu posso falar sem parecer leviana... Assim..."

    s "Ela acha que família, amigos e pessoas com as quais nos importamos nos deixam mais fracos e tiram nosso foco."

    s "Uma atleta precisa estar em seu máximo, tanto física como mentalmente. Como diz o ditado, mente sã, corpo são."

    menu:
        "Ela não tá exagerando?":


            $ sayuri_amizade += 2

            mc "Isso não é um pouco exagerado? Todo mundo precisa de companhia."

            s "Você acha?"

            mc "Claro. Os seres humanos são seres sociáveis, não são? A gente precisa trocar experiências. Bom... é o que eu acho."

            mc "Mas eu não sou mestre em nada..."

            s "N-não. Talvez você esteja certo."
        "Sim. Acho que é isso mesmo.":


            mc "Eu acho que ela tem razão. É preciso manter o foco, né?"

            s "V-você pensa assim?"

            mc "A-acho que sim. Não tenho certeza..."

            s "Ela deve saber o que está nos ensinando. Ela tem bastante experiência."

            mc "Concordo."

            s "Só que..."

    scene sayuri_ponte_mc2 with Dissolve(1.0)

    s "É... assim... eu nunca concordei completamente com isso."

    s "Eu me sentia muito sozinha. Mas eu sempre achei que isso era o que eu tinha que passar pra ser a atleta que a Cidade Chinesa precisava."

    s "Mas será que eu tinha que passar por isso mesmo?"

    s "Eu só pude começar a falar com os outros fora daqui depois que ganhei minha primeira medalha de ouro olímpica."

    s "M-mas era tarde demais... as pessoas já não me tratavam como uma pessoa normal."

    mc "..."

    s "Eu sentia que ou elas queriam se aproximar porque eu era famosa e depois de um tempo elas perdiam o interesse."

    s "Ou elas só me tratavam mal porque eu me achava melhor do que os outros."

    s "M-mas eu nunca pensei isso, [mc]! Você acredita em mim?"

    mc "C-claro, [s]. Eu conheço você há bastante tempo já. Você nunca se gabou sobre essas coisas."

    s "Q-que bom..."

    mc "Eu nem consigo imaginar como é passar por toda essa pressão."

    mc "Eu só consigo pensar que eu queria ter te conhecido antes. Não que você precisa de ajuda, você provou pro mundo todo que é forte..."

    mc "Mas quem sabe estar com você pra te apoiar. Porque todo mundo precisa disso. Por mais forte que seja."

    s "Você quer dizer que as pessoas podem fortalecer a gente?"

    mc "A-acho que sim."

    scene sayuri_ponte_mc1 with Dissolve(1.0)

    s "Então, no fundo, você não concorda com a minha mestra."

    mc "Ah... acho que não... haha! Agora eu pareço um mané."

    s "Hahaha... você é muito sábio, [mc]. Eu ainda não consigo entender como você consegue falar as coisas certas do jeito que você faz."

    mc "Eu?"

    s "Sim. Antes... antes de eu conhecer você eu me sentia muito sozinha."

    s "A [g] sempre foi minha melhor amiga, mas ela tem as coisas dela."

    s "Mas depois que a gente se conheceu no templo, você veio e conversou comigo, como qualquer pessoa."

    s "Isso foi tão estranho no começo. Mas depois eu fui me acostumando."

    s "Até que eu não sei se eu ia aguentar perder você, [mc]."

    if sayuri_adeus:

        scene sayuri_ponte_mc3 with Dissolve(1.0)

        s "P-por isso eu fiquei tão alterada quando você disse que não ia aceitar o que eu fazia."

        s "Eu fiquei tão assustada achando que eu ia perder a pessoa mais importante que eu tenho hoje."

        mc "[s]... eu não ia te deixar... Não foi isso que eu quis dizer aquele dia."

        mc "Eu só quero ter certeza que nem você e nem ninguém está sendo, tipo, esmagado pelo lugar em que vocês vivem."

        s "E-eu sei! Eu acho que eu sei..."

        s "Mas você tá vendo? Tá vendo como aqui é lindo? Não é tudo ruim, [mc]. Você acredita em mim?"

        mc "Eu... quero acreditar."

        s "..."
    else:


        s "E daí quando você falou que ia ficar do meu lado. Eu nem sabia o que pensar."

        s "Fiquei tão tão tão feliz, [mc]..."

        if sayuri_namoro:

            s "E ainda... d-depois ainda... a g-g-gente... a gente..."

            mc "Tudo bem. Eu entendi, boba."

            s "O-o-obrigada. Desculpa não conseguir falar..."

            mc "Haha! Não esquenta... A gente continua namorando mesmo assim."

            s "T-tá..."

            "Eu sinto que eu vou ter que ter uma paciência de jó com a [s]."

            "Ela tá muito longe de ficar à vontade com nossa relação."

            s "[mc]..."

            mc "Oi."

            s "Eu go-gos... gosto muito de você. Vo-você é a pessoa mais importante pra mim."

            "Que linda... talvez não tão longe assim..."

            menu:
                "Beijar ela":


                    $ s6_beijo1 = True

                    $ sayuri_amizade += 2

                    mc "Eu também gosto muito de você. Quer ver?"

                    s "V-ver?"

                    s "Oh!"

                    scene sayuri_ponte_mc_beijo with Dissolve(1.5)

                    pause

                    s "Hmmm..."

                    s "[mc]..."

                    mc "Eu também gosto muito de você."
                "Não forçar a barra por agora":


                    "Melhor eu não forçar as coisas por agora. Ela tá sensível."

            "A [s] é a garota mais doce que eu já conheci."

            "Ela não fala muito dela, mas sempre que ela fala, parece tão sincero. E isso é tão raro."

            "Eu quero ser um cara especial pra ela."

            scene sayuri_ponte_mc1 with Dissolve(1.0)

            if s6_beijo1:

                s "V-você me pegou desprevenida..."

                mc "Eu sei."

                s "Você é fogo, [mc]..."

                mc "Haha! E você é muito fofa."

                s "N-não sou..."

            s "..."
        else:


            s "Você é, com certeza, meu melhor amigo. A pessoa mais importante que eu tenho."

            s "Mais importante que minha mestra, que minha discípula, que minha família."

            mc "[s]..."

            s "Eu não quero ser injusta com todos eles... m-mas é assim que eu me sinto. Eu sou horrível?"

            mc "Claro que não. E eu fico muito feliz de saber disso. Quero ser um cara especial pra você, igual você é pra mim."

            s "Muito obrigada, [mc]."

            s "Ter você do meu lado é o que me dá forças agora."

            mc "Por que? Tá acontecendo alguma coisa?"

            scene sayuri_ponte_mc3 with Dissolve(1.0)

            s "N-não! Não tem nada acontecendo."

            mc "Certeza?"

            s "Só o de sempre. Não se preocupe..."

            mc "Ok."

            "O que será que ela não quer me contar?"

            s "..."

    "{i}Tump tump{/i}"

    scene vila_triade geral with Dissolve(1.0)

    mc desconfiado "Hm?"

    mc "Tem algu-"

    if s5_ajudou:

        "{i}Tump tump tump{/i}"

        scene fenju_vila_cavalinho with vpunch

        pause

        fen "[mc]!"

        mc "Uou!"

        mc "Q-quem é?!"

        s "[fen]! O que você tá fazendo?!"

        fen "Eu só tô-"

        mc "Uoooooooooou!"

        fen "Aiiiiieeeeee!"

        scene fenju_vila_colo with vpunch

        pause

        mc "Upa. Tudo bem?"

        fen "Que susto..."

        mc "Haha... Você é doida?"

        fen "E-eu só queria assustar você, [mc]."

        mc "E você conseguiu."

        s "[mc]... pode colocar ela no chão."

        mc "Verdade."
    else:


        s "Ah. É a [fen]."

        mc "Aquela garotinha que tava treinando com você?"

        s "I-isso."

    scene fenju_sayuri_ponte_mc with Dissolve(1.0)

    pause

    s "Bom dia, [fen]."

    fen "Bom dia, mestra..."

    s "Está indo para o templo?"

    fen "s-sim..."

    s "Você está atrasada para o treino. Já era para você ter começado há uns 15 minutos, não é?"

    fen "S-sim! Por favor, me desculpe. Não precis-"

    s "Não se preocupe."

    s "Hoje o [mc] está aqui. Não é um dia comum."

    fen "Verdade. Por que ele tá aqui?"

    s "Isso são modos, [fen]?"

    mc "Não se p-"

    fen "P-perdão! Eu só-"

    s "O [mc] veio fazer uma visita à nossa vila."

    fen "Mas como ele conseguiu entrar?"

    s "Eu pedi permissão pra minha mestra e ela concedeu acesso."

    fen "Que legal! Será que... deixa pra lá."

    menu:
        "...":


            $ sayuri_amizade += 2

            "Melhor ficar na minha..."

            "..."
        "Será que o quê?":


            mc "Será que o quê?"

            s "Não se preocupe, [mc]."

            s "E você. Você ainda não está pronta para esse tipo de coisa."

            fen "Mas-"

            s "[fen], sem 'mas'."

            fen "S-sim, senhora."

    s "Agora vá para o templo e siga sua rotina."

    fen "Tá..."

    "..."

    "..."

    "A [fen] não tá indo..."

    s "Algum problema, [fen]?"

    fen "Não... é só que..."

    fen "É..."

    "Tô achando que ela não quer treinar hoje."

    "Será que eu me intrometo nessa?"

    "Pelo jeito que a [fen] ficou animada com poder chamar alguém, talvez ela se sinta sozinha."

    "E ver alguém diferente talvez tenha dado uma alegria pra ela."

    "Mas provavelmente eu estaria passando por cima da [s]... E agora?"

    menu:
        "E se a [fen] passear com a gente?":


            $ s6_fenju = True

            mc "[s]... e se a [fen] tirar um dia de folga e sair com a gente?"

            "[s] e [fen]" "Quê?!"

            s "[mc]..."

            fen "Por favor! Por favor!"

            mc "Eu tenho certeza que ela tá se esforçando bastante. Ela merece, não merece?"

            s "..."

            s "Você tá falando sério?"

            mc "Claro. Ela é uma boa garota, não é? Ela podia ter uma folguinha... por favor?"

            s "..."

            s "Ok. Tudo bem."

            fen "Sério?!"

            s "S-sim..."

            s "Mas só por um tempo. E você vai repor o treino perdido, cedo ou tarde."

            fen "T-tá! Eu prometo! Muito obrigada, Sa- digo- mestra."

            s "..."
        "Melhor não falar nada":


            $ sayuri_amizade += 2

            "Não vou me meter nisso. Elas que se entendam."

            "Eu queria ajudar a [fen] a ter um tempo legal, mas minha prioridade é a [s]."

            "Ter um tempo sozinho com ela vai ser incrível."

            s "Então bom treino. Até outro dia."

            fen "A-até..."

    scene vila_triade geral with Dissolve(1.0)

    show sayuri n_interessada with dissolve

    s "Eu tava pensando em te levar em um lugar ainda mais especial, [mc]."

    mc desconfiado "Mais?"

    if s6_fenju:

        fen "Você tá falando do..."

        s "Não estrague a surpresa!"

        fen "T-tá..."

    s "Sim. É um lugar bem especial e apenas algumas pessoas podem ir lá."

    s "Minha mestra está fazendo algo extremamente incomum permitindo que alguém de fora da vila possa visitar o lugar."

    mc envergonhado "Certeza que isso não vai dar problema?"

    s "Não. Está tudo certo."

    mc normal "Então beleza. Tô ansioso pra ver."

    s "Vamos?"

    mc "Claro."

    if s6_fenju:

        mc "Vamos, [fen]?"

        fen "V-vamos."

        show sayuri n_incerta with dissolve

        s "..."

    hide sayuri with dissolve

    "..."

    scene black with Dissolve(1.0)

    s "Ah! [mc]. Eu quero que você feche os olhos e me dê a mão."

    mc desconfiado "Hm?"

    s "É surpresa!"

    if s6_fenju:

        fen "Isso! Vai ser legal."

    mc concentrando "O-ok..."

    "A [s] tá me deixando mais nervoso. Que lugar será esse?"

    mc concentrando "C-cuidado."

    s "Pode deixar."

    if s6_fenju:

        fen "Hihi..."

        "Por que a [fen] tá rindo? O que essas duas tão aprontando?"

    s "Estamos bem perto."

    mc "Ufa."

    s "Agora eu vou deixar você um instantinho e já volto."

    mc "Quê? Eu vou ficar sozinho?"

    if s6_fenju:

        mc "A [fen] vai ficar comigo?"

        fen "Não. Eu vou com a mestra."

        mc "P-por que?"

        fen "Hihi. Não seja bundão, [mc]."

        s "[fen]! Olha essa boca!"

        fen "D-desculpa..."

        s "Voltamos logo. Não abre os olhos."
    else:


        s "Eu volto logo. Não vai abrir o olho."

    mc "T-tá."

    "Por que eu tô com um pressentimento terrível?"

    "Será que eu abro os olhos?"

    "Eu não tenho certeza se eu confio na [s]. Droga... por que eu não confio completamente nela?"

    "Ficar com olhos fechados tá me dando algo muito ruim."

    "Eu pre-"

    "!"

    s "Pronto."

    "Ufa! Eu senti alguém chegando. Era a [s]."

    s "Pode abrir os olhos."

    mc "Ok. Tô abrindo."

    if s6_fenju:

        scene sayuri_fenju_ofuro with Dissolve(1.0)

        pause

        mc surpreso "[s]!"

        s "E e-então? G-gostou?"

        "Tá na cara que a [s] não se sente completamente à vontade com isso. Ela nem tá me olhando nos olhos."

        mc charmoso "Você tá linda."

        if sayuri_namoro:

            mc "A namorada mais linda do mundo."

            s "A-ai, [mc]..."

        fen "E eu?"

        s "[fen]..."

        mc normal "Você tá muito fofa, [fen]."

        s "..."

        fen "O-obrigada."

        s "Aqui é o nosso pequeno paraíso."

        s "Um lugar onde a gente pode relaxar e aproveitar à vontade."

        mc normal "É realmente incrível."

        s "[fen]. Se você puder ir pra lá. Eu e o [mc] vamos aproveitar o ofurô."

        fen "A g-gente pode ir todos pro spa."

        s "Não. Você vai pra lá. Deixa a gente sozinhos aqui. Vai."

        fen "T-tá."

        mc desculpa "..."

        scene ofuro_triade geral with Dissolve(1.0)

        pause

        s "Agora vamos entrar aqui. Você vai ver que incrível que é."

        s "Deixa eu fazer as honras."

        scene sayuri_ofuro1 with Dissolve(1.0)

        pause
    else:


        scene sayuri_ofuro1 with Dissolve(1.0)

        s "Tô aqui... sentada."

        mc surpreso "[s]!"

        s "E a-aí? G-gostou?"

        "Tá na cara que a [s] não se sente completamente à vontade com isso."

        mc "O lugar é incrível. E você tá linda de biquini."

        s "Q-que bom que você achou."

        s "Aqui é o nosso pequeno paraíso."

        s "Um lugar onde a gente pode relaxar e aproveitar à vontade."

        mc normal "É realmente incrível."

    s "Aaahh..."

    s "Você vai entrar também, né?"

    mc envergonhado "Eu não trouxe roupa de banho..."

    s "P-pode ficar à vontade. Só tirar sua calça jeans e sua c-camiseta."

    mc "Bom..."

    "Se ela tá falando... não deve ter nada de mais."

    if sayuri_namoro:

        "E a gente tá namorando ainda por cima. Não vou perder essa chance."

        "Quem sabe as coisas não esquentam..."

        "Seria o lugar perfeito pra rolar alguma coisa."

    mc normal "Ok. Vou tirar e entrar."

    s "T-tá..."

    "..."

    mc normal "Com licença."

    scene sayuri_ofuro2 with Dissolve(1.0)

    pause

    s "Tudo bem?"

    mc envergonhado "S-sim! Claro."

    s "Então... era isso que eu queria que você visse, [mc]."

    s "Eu queria que você sentisse o lado bom da Cidade Chinesa e de ser uma escolhida."

    mc desconfiado "Escolhida? São as pessoas treinadas no templo?"

    s "Mais ou menos isso."

    s "Esta vila, o templo e todo o bairro, é parte de algo muito bem organizado."

    s "Esse controle é o que torna a vida aqui tão boa. Pode reparar que não temos pedintes ou desabrigados."

    s "A vida dos chineses na capital é a melhor possível. Um exemplo pra todas as comunidades do país."

    mc normal "Você realmente parece bem orgulhosa. E com razão. É algo muito bacana."

    s "Mas pra chegar a isso é preciso de um controle central. É importante ter pessoas capazes organizando tudo isso."

    mc "Entendi."

    if s6_fenju:

        s "Por isso-"

        fen "{size=17}[mc]!{/size}"

        mc desconfiado "Hm? A [fen] tá chamando."

        s "Essa menina..."

        scene ofuro_triade geral with Dissolve(1.0)

        show fenju b_feliz with dissolve

        fen "[mc]... mestra... será que vocês podem vir comigo aqui?"

        fen "Queria mostrar uma coisa pra vocês."

        s "[fen], agora a gente tá conversando algo sério. Vá pra lá e fique calada."

        fen "Mas é que-"

        s "[fen]!"

        show fenju b_incerta with dissolve

        fen "S-sim, senhora."

        "Por que a [s] fala assim com a [fen]?"

        "Normalmente ela é uma garota tão sensível, tão meiga. Mas ela fica tão diferente quando tá com a [fen]..."

        fen "E-eu vou pra lá."

        menu:
            "Espera. Eu vou ver rapidinho o que a [fen] quer.":


                $ s6_fenju_spa1 = True

                mc envergonhado "Espera. Eu vou com você, [fen]."

                s "[mc]!"

                fen "Sério?"

                mc normal "Sim. É rapidinho, né?"

                show fenju b_feliz with dissolve

                fen "S-sim!"

                s "A gente tava conversando."

                mc envergonhado "{size=17}Ela é só uma criança. Deve tá querendo atenção. Eu volto logo.{/size}"

                s "T-tá..."

                mc normal "Vamos lá?"

                fen "Vem!"

                hide fenju with dissolve

                "..."

                jump s6_fenju_spa
            "Depois a gente conversa [fen].":


                $ sayuri_amizade += 2

                mc normal "Não esquente, [fen]. Depois a gente conversa."

                fen "T-tá."

                hide fenju with dissolve

label s6_ofuro_juntos:

    $ s6_ofuro_juntos = True

    if s6_fenju:

        mc charmoso "Bom. Agora deixa eu voltar pra essa delícia de ofurô."

    s "[mc]..."

    mc normal "Oi."

    s "Senta aqui do meu lado. A água tá mais quentinha."

    mc envergonhado "{i}gulp{/i}"

    mc envergonhado "T-tá..."

    scene sayuri_ofuro_mc1 with Dissolve(1.0)

    pause

    "Uou... eu tô tão perto da [s]."

    if sayuri_namoro:

        "Mesmo a gente namorando, ainda é muito no começo."

        "Tenho que aproveitar ao máximo essa oportunidade."

    s "[mc]..."

    mc "O-oi!"

    s "E-eu tô tão nervosa..."

    mc "Acho que eu também... Mas isso é normal."

    s "Você acha?"

    mc "Sim. Estar perto de alguém que a gente não tem muita intimidade é sempre um desafio..."

    s "Certo..."

    s "Hmm..."

    mc "Que foi?"

    scene sayuri_ofuro_mc2 with Dissolve(1.0)

    s "Daqui a pouco vai ficar tarde e a gente vai terminar nosso encontro..."

    mc "Que que tem? A gente vai se encontrar de novo, né?"

    s "..."

    if sayuri_adeus:

        s "É... é isso que tá me deixando tão nervosa."

        mc "Como assim?"

        s "Eu queria te mostrar esta vila e as maravilhas que nós temos, pra convencer você que aqui é um bom lugar."

        s "Mas não sei se eu consegui..."

        mc "[s]..."

        s "Aquele dia você foi tão incisivo. Eu até gritei com você. Fiquei com tanta vergonha depois..."

        mc "Tudo bem."

        s "Como assim?"

        mc "Ué. É normal a gente brigar com quem a gente gosta também."

        s "V-você acha? Mas você não vai me abandonar pra sempre?"

        mc "Claro que não, [s]."

        mc "Minha intenção nunca foi abandonar você."

        s "Mas! O q-que você achou? Você ainda acha que aqui é um lugar horrível?"

        "A [s] pode ter me mostrado um lado bem incrível da Cidade Chinesa, e parece que elas também se divertem."

        "Mas a [fen] continua machucada. Eu ainda consigo ver as marcas de agressão nela."

        "E ela tão bem vermelhas. Não são antigas. Então no fundo acho que nada mudou..."

        "Só que... o [chi] disse que é mais complexo do que eu posso imaginar. Pra eu não olhar com meus olhos."

        "O que será que ele quis dizer com isso?"

        s "[mc]?"

        mc "Ah... eu..."

        menu:
            "Desculpa, mas eu não acho que tá tudo bem.":


                $ sayuri_adeus = True
                $ sayuri_adeus_manteve = True

                mc "Desculpa, [s]. Mas eu ainda olho pra [fen] e até pra você e vejo garotas assustadas."

                mc "Essa vila é linda, este banho é incrível, e você realmente parece muito bem, mas isso não acaba com os problemas."

                scene sayuri_ofuro_mc3 with Dissolve(1.0)

                s "..."

                s "Eu sabia..."

                mc "Mas você sabe que pode contar comigo, né?"

                s "..."

                mc "[s]..."

                s "E-eu acho que eu preciso ir..."

                scene ofuro_triade geral with Dissolve(1.0)

                mc angustiado "[s]!"

                mc "Volta aqui!"

                "..."

                mc desculpa "Droga... e agora?"

                "A Cidade Chinesa é tão importante pra [s]. Por que eu tinha que falar isso pra ela?"

                "Mas eu também não podia só mentir. Falar que tá tudo legal."

                "Nem tenho mais o que fazer aqui. Eu acabei estragando tudo... Deixa eu voltar."

                "Que merda..."

                jump sayuri_e6_final
            "Eu mudei de ideia. Eu acho que a Cidade Chinesa está certa.":


                $ sayuri_adeus = False
                $ se6_mudanca = True

                mc "Olha... eu ainda não tenho certeza do que achar. E igual eu falei, não quero ficar julgando."

                mc "Mas me deixou mais tranquilo ver tudo isso."

                mc "Ver você bem, ver a [fen] se divertindo ali... este lugar tão foda. Realmente, parece que não é horrível."

                scene sayuri_ofuro_mc3 with Dissolve(1.0)

                s "..."

                mc "Eu reconheço que eu posso ter exagerado. Que a Cidade Chinesa não quer só ferrar vocês."

                s "Você pensa assim mesmo?!"

                mc "Depois de hoje, sim. Pensando bem, talvez vocês tenham uma forma diferente de treinar, de educar, sei lá."

                mc "Eu só queria que você prestasse bem a atenção. Resultado não é tudo. Educar agredindo fisicamente ou psicologicamente alguém..."

                mc "Que tipo de educação é essa? Que tipo de treino é esse que coloca o objetivo na frente da pessoa?"

                mc "Você realmente acha que isso vale à pena?"

                mc "Mas isso é só minha opinião. E eu não acho que você tá errada se você não pensa como eu."

                s "[mc]..."

                s "..."

                s "O-obrigada... obrigada por falar isso..."

                mc "O que foi, [s]?"

                s "..."

                "O que será que eu fiz pra ela?"
    else:


        mc "Eu disse que vou ficar sempre do seu lado, não importa o que aconteça. Você não se lembra disso?"

        s "Mesmo se eu não merecer?"

        mc "Não fala bobeira. Por que você não mereceria? Você é a garota mais meiga, mais sincera que eu conheci."

        scene sayuri_ofuro_mc3 with Dissolve(1.0)

        s "Isso não é verdade, [mc]. Eu queria que fosse, mas não é."

        s "A verdade é muito mais escura do que você viu..."

        mc "Você tá falando d-"

        s "..."

    mc "[s]..."

    s "..."

    mc "Fala pra mim o que foi."

    s "E-eu nunca me senti tão feliz. Ter você aqui do meu lado..."

    s "Eu queria que esse momento durasse pra sempre."

    mc "Por que você tá chorando? Não tô entendendo."

    s "[mc]... Esta cidade é maldita."

    s "{i}hic{/i}"

    s "A Cidade Chinesa não é diferente. A sujeira tá aqui também."

    mc "[s]..."

    "Ela tá chorando. Ela tá tremendo."

    "Seja lá o que ela quer dizer, a [s] é uma garota muito machucada. Não consigo imaginar o que aconteceu pra deixar ela assim."

    "Ela precisa de mim mais do que nunca."

    if sayuri_namoro:

        "Eu sou o namorado dela. Eu tenho que fazer alguma coisa."

        "Eu quero que ela saiba que tô aqui pra ela."

        mc "[s]..."

        mc "Você sabe o quanto você significa pra mim, né? Você é minha namorada."
    else:


        if sayuri_intencao == "namoro":

            "A [s] não é minha namorada, mas desde que eu ajudei ela a comprar a roupa àquele dia, eu quero ter algo a mais com ela."

            "Talvez eu possa mostrar isso pra ela. Talvez revelar meus sentimentos ajude de alguma forma..."

            "Eu não quero me aproveitar dela. Só quero que ela tenha certeza que tem alguém que gosta dela."

            menu:
                "Falar que quer namorar com ela.":


                    $ s6_declarou = True

                    mc "[s]... você sabe que eu gosto de você, né?"

                    mc "E eu gosto de verdade. Mais do que só uma amiga."

                    s "!"

                    mc "Desculpa se parecer que eu tô abusando de você estar assim, frágil, mas eu queria que você soubesse disso."

                    s "E-eu..."

                    s "{i}hic{/i}"

                    mc "Não precisa falar nada agora. Mas queria que você soubesse disso."
                "Não falar nada.":


                    "Agora não é a hora de falar disso."

                    "Ela precisa de um amigo e não de alguém assediando ela."

    mc "Eu vou tá sempre aqui do seu lado."

    mc "Quando a gente gosta de alguém, a gente fica do lado dela. Depois a gente pensa nas outras coisas."

    mc "Esse negócio de certo, de errado. Isso aí a gente vê depois."

    mc "Agora, eu só quero que você melhore e se sinta bem, tá? Não pense demais."

    mc "Pode chorar, pode desabafar."

    if ( sayuri_namoro or s6_declarou ) and sayuri_amizade >= 38:

        $ s6_beijo2 = True

        scene sayuri_ofuro_mc2 with Dissolve(1.0)

        s "{i}hic{/i}"

        s "..."

        s "[mc]... E-eu posso te beijar?"

        mc "Hm?"

        mc "Sa-"

        scene sayuri_ofuro_mc_beijo with Dissolve(2.0)

        pause

        s "Hmmmm!"

        "Uou... a [s] tá me apertando muito forte."

        s "Ai, [mc]..."

        "Hmmm... Isso que é um beijo de verdade."

        window hide

        pause

        "Essa é a hora. Eu vou pegar ela aqui e agora."

        "Ou será que ainda é muito cedo? Eu não quero assustar ela... O que eu faço?"

        menu:
            "Pegar ela de jeito":


                mc "[s]... eu quero mais."

                s "Hmm... [mc]... tá..."

                scene sayuri_ofuro_mc4 with Dissolve(1.0)

                pause

                s "Ah! [mc]..."

                mc "Eu quero sentir você, [s]. Você é muito gostosa."

                s "An ahgn.."

                mc "Eu quero pegar em você inteira."

                s "M-mas e a- ahn!"

                mc "Não esquenta. Ninguém vai ver a gente."

                mc "Você também quer, não quer?"

                s "Eu q-quero... eu quero sentir você, [mc]..."

                mc "Eu também quero sentir você."

                window hide

                pause

                mc "Eu vou tirar seu biquíni. Eu quero pegar em você."

                s "Ah..."

                scene sayuri_ofuro_mc5 with Dissolve(1.0)

                pause

                s "Eu não consigo... ah..."

                mc "Eu tô querendo fazer isso com você faz tanto tempo."

                s "E-então faz... faz o que você q-quiser comigo... eu sou sua."

                mc "Ai, [s]. Você tá me deixando louco."

                s "E-eu também... eu não consigo pensar."
                scene snew_ani15 with Dissolve(1.0)
                s "Eu quero que você me aperte."

                mc "Me pega também. Aproveita tudo."

                s "Aahnn!"

                s "[mc]... me aperta embaixo por favor."

                s "Pega na minha... bu... é..."

                mc "T-tá... pode deixar."

                s "Ah.. isso... Tira a calcinha e m... p-pega... na b-"

                scene sayuri_ofuro_mc6 with vpunch

                s "Aiin!"

                mc "Assim?!"

                s "É! Ah!"

                s "Me beija e me aperta aí! Eu quero s-sentir aínn!!"

                s "Ahnn!"

                mc "Sua bunda é uma delícia, [s]. Ela é incrível."

                s "Ahnn! Pode apertar forte!"

                "Uau... a [s] parece com tanta vontade... eu nunca ia imaginar..."
                scene snew_ani04 with Dissolve(1.0)
                "Eu tenho que aproveitar."

                mc "[s]... posso sentir sua bunda com ele?"

                s "Hm? C-com ele? Com... ahhn!!!"

                s "[mc]... não sei... tá... tá bom... faz o que você quiser. Eu tô pronta."

                "Finalmente... eu vou poder transar com a [s]. Nem acredito."

                mc "[s]... eu vou..."

                s "T-tudo bem... tira toda a calcinha."

                mc "Tá."
            "Melhor não forçar":


                "Melhor eu ir devagar com a [s]. Ela é muito tímida e talz..."

                mc "Sa-"

        s "Eu-"
    else:


        s "E-eu queria te falar uma coisa. Pra mim, voc-"

    if not s6_fenju:

        scene sayuri_ofuro_mc2 with Dissolve(1.0)

        s "..."

        mc "Q-que foi? O que aconteceu?"

        s "N-não foi nada."

        if s6_beijo2:

            mc "Você não gostou do nosso b-"

            s "Nã-não é nada disso, [mc]..."

        s "Eu só me lembrei da [fen] e..."

        mc "O que tem ela?"

        s "Nã-não se preocupe... Eu e a [fen] temos uma relação complicada."

        mc "Sério?"

        jump s6_sem_fenju
    else:


        fen "[mc]!"

        s "!"

        scene ofuro_triade geral with vpunch

        mc "Uou!"

        show fenju b_incerta with dissolve

        fen "T-tô atrapalhando vocês?"

        show fenju b_incerta at esquerda with move

        mc envergonhado "N-não! Tá tudo legal."

        show sayuri b_incomodada with dissolve

        s "[fen]. O que foi dessa vez?"

        show sayuri b_incomodada at direita with move

        fen "S-sa... você tá bem?"

        s "Eu tô bem, sim. O que foi?"

        fen "E-eu só queria saber se vocês não querem ir comigo lá..."

        s "Daqui a pouco o [mc] precisa ir embora e você continua incomodando a gente."

        fen "D-desculpa..."

        s "..."

        "A [fen] tá querendo uma atenção. Tá na cara. A [s] não vai ceder. Eu que vou ter que resolver isso..."

        menu:
            "Eu queria ver aquele outro lado também.":


                mc normal "[s]."

                s "O-oi?"

                mc "Eu queria dar uma olhada de novo lá."

                s "Sério?"

                mc envergonhado "Eu gostaria, se não for problema pra você."

                s "..."

                s "Ok."

                show fenju b_feliz with dissolve

                fen "Isso! Venham! Vem, [s]!"

                s "[fen]!"

                fen "D-desculpa... vem, mestra."

                s "... Tá. Vamos lá."

                "..."

                scene spa_triade geral with Dissolve(1.0)

                jump s6_fenju_spa2
            "...":


                $ se6_goodending = True

                "Melhor deixar elas se resolverem."

                "Eu tô curtindo meu tempo com a [s] e não quero saber da pestinha agora."

                "Vou ficar aqui até a gente ter que sair."

                fen "E-eu vou pra lá então. Quando for a hora de ir me avisem, tá?"

                s "Pode deixar."

                hide fenju with dissolve

                s "Ufa. Agora a gente pode voltar. Vem."

                mc normal "Tá."

                scene sayuri_ofuro_mc1 with Dissolve(1.0)

                s "Essa menina não tem jeito mesmo..."

                s "Ela é bastante talentosa, mas ainda precisa colocar certas coisas na cabecinha dela."

                if s6_beijo2:

                    "Merda! A [fen] acabou com o clima!"

                    "Eu tava pronto pra... não é possível... AAHHH!"
                else:


                    "Pelo menos a [fen] deu uma mudada no clima. A [s] parece melhor agora."

                "Bom... agora é continuar daqui."





                label s6_sem_fenju:

                    mc "Aliás, qual é sua relação com a [fen]? Você é treinadora dela?"

                s "Hmmm..."

                scene sayuri_ofuro_mc2 with Dissolve(1.0)

                s "Basicamente seria isso. Mas no nosso caso é um pouco mais complexo."

                mc "Certo..."

                s "Aqui, o treinamento não é focado somente no esporte. No caso, eu ensino diversas técnicas de ginástica pra ela."

                s "Mas minhas responsabilidades não param por aí. Eu preciso ensinar ela sobre história, sobre a cultura da Cidade Chinesa também."

                s "Inclusive questões como moral e ética. No caso, é como se a [fen] fosse uma 'díscipula para a vida'."

                s "Tudo o que acontece com ela é minha responsabilidade."

                mc "Parece uma responsabilidade e tanto."

                s "Nem me fala..."

                mc "V-você... gosta dela?"

                s "Como assim?"

                mc "Digo, você sente algum carinho, sei lá, afeição pela [fen]?"

                s "É... difícil responder isso, [mc]. Minhas responsabilidades para com ela não passam por afeto."

                mc "Eu sei, mas pessoalmente eu digo."

                s "..."

                mc "..."

                "Que climão..."

                if s6_beijo2 and not s6_fenju:

                    s "[mc]... d-desculpa ter cortado todo o clima naquela hora do beijo."

                    mc "Tudo bem... Fiquei feliz de você não ter falado que achou horrível."

                    s "C-claro que não. Digo... ai..."

                mc "D-deixando a conversa de lado, acho que a gente devia aproveitar mais essa delícia de ofurô."

                scene sayuri_ofuro_mc1 with Dissolve(1.0)

                s "S-sim..."

                s "Aproveite que não é sempre que você vai ter uma maravilha como esta."

                mc "É verdade."

                scene black with Dissolve(1.0)

                "..."

                scene ofuro_triade geral with Dissolve(1.0)

                show sayuri b_interessada with dissolve

                s "Que delícia que foi."

                mc charmoso "Sim. Foi uma tarde incrível, [s]. Muito obrigado."

                s "Fico feliz mesmo que você tenha gostado."

                s "Ah. É uma pena, mas a gente tem que ir. O horário que eu acertei com a minha mestra já tá quase acabando."

                mc charmoso "Tudo bem. Eu entendo."

                mc "Quem sabe algum dia eu não posso voltar?"

                s "S-seria incrível."

                s "Posso te deixar sozinho pra voltar? Eu vou pegar a [fen] e a gente vai se trocar ainda e o tempo tá meio apertado."

                mc envergonhado "C-claro. Aqui é pequeno. Eu sei voltar."

                s "Tá. Obrigada, [mc]."

                if sayuri_namoro:

                    s "V-você é o melhor... na-na... na-morado do mundo."

                    mc surpreso "!"

                    mc "Eu ouvi bem?! Você me chamou de 'namorado'?!"

                    s "Ai..."

                    mc charmoso "Você que é, [s]. Não vejo a hora de te ver de novo."

                    mc "Beijo."

                    s "B-b-be..."

                    mc envergonhado "Até."

                    s "A-até, [mc]."
                else:


                    mc normal "Até a próxima, amigona."

                    s "Até, a-amigão..."

                jump sayuri_e6_final

label s6_fenju_spa:

    scene spa_triade geral with Dissolve(1.0)

    "..."

    mc normal "Uou. Aqui é bem bonito também."

    fen "Vem aqui sentar na água comigo, [mc]."

    mc envergonhado "Cl-claro."

    scene fenju_spa_sentada with Dissolve(1.0)

    fen "É bom?"

    mc normal "Muito gostoso."

    fen "Não é quentinha igual a água do ofurô, mas é gostosa, né?"

    mc "É, sim."

    fen "..."

    mc envergonhado "..."

    mc "É..."

    fen "..."

    mc desconfiado "Que foi?"

    fen "N-nada. Só tô olhando."

    mc envergonhado "Ok."

    mc normal "Você... você gosta de morar aqui, [fen]?"

    fen "Se eu gosto?"

    mc normal "Sim."

    fen "N-não sei..."

    mc envergonhado "Pode pensar um pouco antes de responder."

    fen "Hmmm... eu nunca pensei nisso, mas acho que eu gosto, sim."

    mc normal "Ah. Que bom."

    mc desconfiado "Mas como assim? Você nunca pensou se você gosta de onde você vive?"

    mc "Nunca pensou se é legal ou chato?"

    fen "A-acho que não... nunca ninguém me perguntou... e eu estou aqui pra treinar e se uma ginasta."

    mc desculpa "Entendo. Você se esforça bastante pra isso, né?"

    fen "Claro. É pra isso que eu existo. Pra representar minha comunidade e a Cidade Chinesa nas Olimpíadas."

    mc "Certo... E você não gosta de mais nada?"

    fen "Hihi..."

    mc desconfiado "Que foi?"

    fen "Nada... é que você fica perguntando se eu gosto disso ou daquilo."

    mc envergonhado "Haha..."

    "Não sei qual é a graça nisso."

    mc normal "Mas você parece feliz."

    fen "Sim! Fazia tempo que eu não conversava assim com alguém de fora da vila."

    mc serio "Sério?"

    fen "Acho que a última vez foi aquele dia com você e o [chi]."

    if s5_ajudou:

        fen "Ah! Aquele dia na praia... você foi tão legal comigo."

        fen "Eu me diverti tanto!"

        mc normal "Que bom."

        mc "Quem sabe a gente não pode fazer isso de novo logo?"

        fen "Tomara!"

    mc normal "Eu sei que treinar é importante, mas você também precisa falar com as pessoas."

    fen "Você acha?"

    mc normal "Claro. Existe muita coisa. Ainda mais você que é criança. Você tem que brincar, se divertir!"

    fen "Hihi. [mc]..."

    mc desconfiado "Que foi?"

    fen "Você fala cada coisa..."

    mc "..."

    scene spa_triade geral with Dissolve(1.0)

    mc normal "Bom. Melhor eu voltar antes que a [s] sinta falta de mim."

    show fenju b_triste with dissolve

    fen "Já?"

    mc normal "Depois eu e ela voltamos aqui, tá?"

    fen "Fica mais um pouco comigo."

    mc desculpa "Desculpa, mas eu vim aqui pela [s]. Não quero deixar ela sozinha, tudo bem?"

    fen "Por favor!"

    menu:
        "A gente vai estar aqui do lado, tá?":


            mc normal "A gente vai tá logo aqui."

            fen "Aauu... tá bom."

            mc "Depois vai lá também."

            fen "Posso?"

            mc "Claro."

            show fenju b_feliz with dissolve

            fen "T-tá."

            hide fenju with dissolve

            "Essa menina... eu sinto que ela precisa urgente de companhia."

            "Não sei o que pode acontecer com a cabeça dela se ela continuar assim."

            "Bom, mas eu tô aqui com a [s]. Não sou pai dela e não tô aqui pra isso."

            "..."

            scene ofuro_triade geral with Dissolve(1.0)

            mc normal "Voltei."

            s "Ufa."

            jump s6_ofuro_juntos
        "Ok ok. Vou ficar mais.":


            $ s6_fenju_direto = True

            mc envergonhado "Calma, calma. Eu vou ficar aqui com você."

            show fenju b_feliz with dissolve

            fen "Sério?!"

            mc "Vou. Mas a gente tá logo ali. Não sei por-"

            fen "Hihi! Vem aqui comigo, [mc]!"

            jump s6_fenju_spa2

label s6_fenju_spa2:

    $ s6_fenju_spa2 = True

    fen "Aqui! Aqui!"

    mc envergonhado "..."

    scene fenju_spa_feliz with Dissolve(1.0)

    fen "Hihi..."

    mc normal "Você gosta mesmo daqui, né, [fen]?"

    fen "Ainda não acredito que eu tô aqui com você e a [s]."

    if s6_fenju_direto:

        mc envergonhado "O que tem de tão incrível?"

        fen "Nós três aqui. Aproveitando o banho..."

        fen "Acho que é a primeira vez que eu venho aqui com a [s]."

        mc desconfiado "Sério?"

        fen "S-"

        s "Falou de mim?"

        fen "M-mestra! Vem aqui também!"
    else:


        mc envergonhado "O que tem de tão incrível?"

        fen "Nós três aqui. Aproveitando o banho..."

        s "..."

    fen "Hihi! Nós três aqui... eu nem acredito."

    "A menina tá que não se aguenta."

    s "E então? O que você queria [fen]?"

    fen "E-eu?"

    s "Não... claro! Você chamou o [mc] aqui. Eu também estou aqui. O que tanto você queria mostrar?"

    scene sayuri_spa_brigando with Dissolve(1.0)

    fen "E-eu..."

    s "Você sabe o que eu tive que fazer pra trazer o [mc] aqui?!"

    s "Eu queria passar um dia com ele! Mostrar a vila pra ele! Convencer ele que a Cidade Chinesa era legal com a gente!"

    s "Mas você tinha que aparecer e estragar tudo!"

    fen "S-say-"

    s "Não me chama de [s], menina!"

    fen "P-por que? Ele te c-"

    s "Eu sou sua mestra! Você é minha discípula, entendeu?!"

    s "Você é minha responsabilidade e tem que me obedecer!"

    fen "D-desculpa, me-"

    s "Não adianta vir com esse jeito falso! Isso me deixa louca! Eu sei que você não é assim de verdade!"

    s "Você não é nada! É uma monstra! Você acha que tem talento?! Você não passa de uma MONSTRA!"

    fen "P-por f-"

    s "CALA A BOCA!"

    scene sayuri_spa_bate_fenju with hpunch

    pause

    fen "AI!"

    mc angustiado "!"

    s "Eu faço isso pelo seu bem! Pra você aprender!"

    fen "Ai..."

    s "Droga! Olha o que você me fez fazer?!"

    scene spa_triade geral with hpunch

    mc angustiado "[s]! Calma!"

    scene ofuro_triade geral with vpunch

    mc angustiado "[s]!"

    "..."

    "Que porra foi essa? Ela bateu na coitada da [fen]."

    "A [s] perdeu a cabeça? O que foi isso?"

    fen "[mc]..."

    mc preocupado "[fen]... você tá bem?"

    show fenju b_triste with dissolve

    fen "Eu tô..."

    mc "A gente precisa ver seu machucado. Não tá doendo?"

    fen "Não..."

    mc "Como não? Ela te agrediu!"

    show fenju b_incerta with dissolve

    fen "E-eu tô acostumada, [mc]..."

    mc angustiado "..."

    mc irritado "Que merda! Esse povo é louco!"

    fen "A [s]... ela sabe como nã-"

    mc preocupado "Não se preocupe, [fen]. A gente vai tirar você daqui."

    fen "Quê?!"

    mc "Eu vou falar com o [chi]. A gente vai dar um jeito em tudo. Você não pode continuar aqui nessas condições."

    fen "Não..."

    mc angustiado "Como 'não'?!"

    fen "Por favor, não faça nada, [mc]."

    mc "Quê?!"

    fen "Eu quero continuar meu treinamento. Eu preciso."

    mc bravo "Isso é ridículo, [fen]. Isso tá longe de ser treinamento!"

    fen "Para! Por favor... não faça nada. Deixa a gente."

    mc preocupado "[fen]! Eu quero te ajudar."

    fen "Eu sei! Mas não faça nada disso que você está pensando."

    mc "Mas-"

    fen "Olha. Me escuta por favor."

    mc desculpa "T-tá..."

    fen "Perdoa a [s]."

    mc "Nem sei o que pensar sobre a [s]..."

    fen "A [s] não é ruim, [mc]. Ela sabe o que tá fazendo."

    mc "[fen]... Eu-"

    fen "Calma. Perdoa ela. E não se meta mais com a vila."

    show fenju b_feliz with dissolve

    fen "Eu gostei tanto de hoje. Foi o melhor dia que eu tive em um tempão."

    fen "Por favor, se você puder, vamos fazer isso de novo."

    fen "Não se afaste da minha mestra, [mc]. Fique perto da gente. Por favor."

    fen "E você tem que ir embora. Eu não sei o que vai acontecer com você se você ficar aqui."

    mc preocupado "Não se preocupe comigo."

    fen "E você não se preocupe comigo. Agora vai."

    mc "Só que e se-"

    fen "Vai, [mc]. Vai logo!"

    mc bravo "..."

    mc "Droga!"

    scene black with Dissolve(1.0)

    "..."

label sayuri_e6_final:

    scene vila_triade saida with Dissolve(1.0)

    if s6_fenju_spa2:

        "Que merda tá acontecendo?!"

        "A [s] agrediu a menina na minha frente. E as coisas que ela falou."

        "A [fen] parece nem ligar. Como se fosse normal uma criança apanhar desse jeito."

        "A Cidade Chinesa, a 'vila', esse templo, as mestras."

        "Tudo isso é um absurdo. Nem parece coisa de verdade."

    elif sayuri_adeus_manteve:

        "Não tenho como mudar minha opinião sobre a Cidade Chinesa assim só com um passeio."

        "Agressão, a pressão, é quase um terrorismo que fazem com essas meninas. A [s] também."

        "Quantas outras pesssoas não estão envolvidas nesse sistema?"

        "Eu preciso desvendar tudo isso, mesmo que elas não entendam."

    elif se6_goodending:

        "Uou. Hoje foi um dia incrível."

        "Eu e a [s] nos aproximamos tanto."

        if sayuri_namoro:

            "Tò curtindo muito ficar com ela. Acho que a gente ainda vai se dar muito bem."

            "Nossa relação tem tudo pra crescer e se fortalecer."

        elif s6_declarou:

            "Eu me declarei pra ela."

            "Ela tava abalada e nem me respondeu, mas eu sinto que ela sente algo por mim também."
        else:


            "Nossa amizade tá mais forte do que nunca."

            "Quero ser um amigo que ela possa contar. Quero ajudar ela e a [fen] a aguentarem esse povo doido da Cidade Chinesa."

            "Ela tem muito orgulho deste lugar, mas eu ainda sinto que tem coisas muito estranhas acontecendo aqui."

        if s6_beijo2:

            "E depois a gente acabou se beijando no ofurô. Foi um beijo tão apaixonado."

            "Não sabia que a [s] tinha esse lado quente também."

            mc safado "Ela até sentou no meu colo..."

        "Não vejo a hora da gente se ver de novo."

    "Só que agora eu tenho que sair daqui. Tô com um pressentimento terrível."

    "Eu sinto que tem alguém me olhando."

    scene black with Dissolve(1.0)

    "[s]... [fen]..."

    $ renpy.choice_for_skipping()
    $ renpy.block_rollback()

    pause

    $ v24_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v24_fim","sayuri","personagem")

    jump call_cidade

label sayuri_evento7_pre:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s7_save", extra_info="s7_save")

    $ estou_na_cidade = False

    $ sayuri_e7 = "pre"

    scene ape_celular with Dissolve(1.0)

    "Cara... aquele dia na parte secreta da Cidade Chinesa..."

    if s6_fenju_spa2:

        "Ainda não tô acreditando que a [s] bateu na [fen]..."

        "A [s] sempre foi uma garota tão meiga... tão sensível... agora explodir daquele jeito e agredir uma criança?"

        "Isso não dá pra aceitar assim, mano..."

        "Eu sei que o Bao falou pra eu tentar não ver com os meus olhos. Que cada cultura tem uma forma de fazer suas coisas..."

        "Só que tem coisas que a gente evoluiu. Antigamente os europeus falavam que escravos não tinham alma. Isso é um absurdo hoje."

        "Agora, bater em criança? Achei que isso fosse algo que a gente deixou pra trás. Isso dá cadeia, inclusive."

    elif sayuri_adeus_manteve:

        "Eu disse pra ela que eu não ia continuar concordando com o que eles fazem."

        "Eu sei que o Bao falou pra eu tentar não ver com os meus olhos. Que cada cultura tem uma forma de fazer suas coisas..."

        "Só que tem coisas que a gente evoluiu. Antigamente os europeus falavam que escravos não tinham alma. Isso é um absurdo hoje."

        "E o que eles fazem com a [fen] e o medo que a [s] tem da mestra dela. Isso só pode ser merda. Com certeza."
    else:


        "Aquele dia com a [s] no banho foi muito bacana. A gente se falou e teve um dia massa. Eu tô curtindo muito a presença dela."

        "Eu sinto que a gente se aproximou mais, eu vi a [fen] também."

        "Espero que a menina esteja bem. Sempre com aqueles machucados..."

    "Eu gosto muito da [s]..."

    "Só que a [fen] é uma adolescente, e dá pra ver que ela tá fazendo tudo o que é possível pra ser uma boa ginasta."

    "O tanto que aquela menina treina não é brincadeira."

    "E pelo que eu entendi ela foi afastada da família dela. Ela mora lá no templo... isso não deve ser bom pra uma criança."

    menu:
        "Eu acho que a [s] e a mestra estão 100%% erradas.":


            "Não dá pra aceitar o que esse pessoal tá fazendo, pelo menos pelo que eu vi até agora..."

            "A gente não avançou em direitos e essas coisas pra ser permitido fazerem isso com uma garotinha."

            "Isso é o que eu acredito. E acho que eu posso fazer algo com isso usando a revista."

            "Eu posso denunciar essas pessoas. Talvez esse seja o certo depois de ver o que acontece naquele templo."
        "Ainda não dá pra chegar em uma conclusão...":


            "Por um lado eu sei que tem coisa errada aí, mas eu não quero julgar a [s] e os outros sem saber tudo antes. Se eu conseguisse mais informações..."

            "Talvez eu pudesse até usar isso tudo na revista. Uma matéria sobre os mistérios da Cidade Chinesa."

    "Uma matéria sobre essa vida, sobre essa cultura tão diferente... Só que acho que ainda é muito cedo."

    "Nós jornalistas trabalhamos com fatos, dados e entrevistas. Se eu tivesse algum tipo de acesso..."

    "Será que teria alguma forma de chegar até lá? Só que o melhor seria sem estar acompanhado da [s] ou de ninguém. Eu poder xeretar à vontade."

    "Se eu conseguisse ver um treino da [s] e da [fen] sem ela saber... igual aquela vez, mas do começo ao fim... talvez ver a mestra da [s]..."

    "Conseguindo uma gravação ou fotos ou até um vídeo sobre o que acontece lá... isso seria uma arma e tanto nas minhas mãos."

    "Eu ia ganhar pontos na revista e quem sabe até fazer meu nome aí no jornalismo. Sair de paparazzo para ser um jornalista investigativo..."

    "Seria incrível! Eu podia escrever um livro e as pessoas viriam e falariam. '{i}Cof cof{/i} poderia me dar um au-'"

    play sound "audio/som_3_celular.mp3"

    $ renpy.vibrate(1)

    "Smartphone" "Trrrr… trrrr…"

    "Opa..."

    scene black with dissolve

    mc "A [s] me ligando!"



    scene ape_celular_falando with Dissolve(1.0)

    mc "Alô?"

    if s6_fenju_spa2 or sayuri_adeus_manteve:

        s "O-oi... desculpa ligar..."

        mc "Oi... tudo bem... Você tá legal?"

        if sayuri_namoro:

            "Caraca... a gente tá namorando e nem parece..."

        "O clima tá mó pesado..."
    else:


        s "Oi. Tudo bem, [mc]?"

        mc "Tudo sim, e você?"

    s "Mais ou menos..."

    mc "O que foi?"

    s "A [fen] desapareceu."

    mc "Como?!"

    s "Eu não tô encontrando ela. Aconteceu a mesma coisa uma outra vez..."

    if s5_ajudou:

        "Será que ela tá falando daquela vez que eu trouxe a Fen Ju pra cá? Ixi..."

    mc "S-sei..."

    s "Ela precisa voltar logo antes que as pessoas sintam a falta dela. Isso pode ser muito ruim."

    "Muito ruim?"

    mc "Ela não falou nada?"

    s "Não... igual da outra vez. Mas ela voltou uma hora, só que já era tarde demais. Ela não pode perder os treinos dela, entende?"

    menu:
        "Provavelmente ela só deu uma saidinha.":


            mc "Será que ela não foi só dar um passeio, sei lá? Ela é adolescente. Às vezes eles fazem essas coisas, não fazem?"

            s "N-não, [mc]... não foi assim que a [fen] cresceu. Ela sabe as responsabilidades dela."

            s "É uma situação bem grave. Isso eu posso falar."

            mc "Entendi... E como eu ajudo?"

            s "É..."
        "Eu posso ajudar em alguma coisa?":


            mc "Entendo... [s]. Tem alguma coisa que eu posso fazer pra te ajudar?"

            s "Ah! Obrigada... você sempre me ajudando, [mc]. Mas eu não quero te ocupar."

            if sayuri_namoro:

                mc "Tá louca? Eu sou seu namorado, não sou?"

                s "S-sim..."

            mc "Eu vou te ajudar, claro."

            s "O-obrigada..."

    s "Eu estou andando por toda a Cidade Chinesa, mas até agora nem sinal dela. O [chi] não soube dar qualquer dica..."

    s "Eu achei estranho porque normalmente ela vai atrás dele quando desaparece. Mas não desta vez..."

    s "Daí... daí eu pensei que ela poderia ter ido falar com você."

    mc "Comigo?!"

    s "Sim... ela tem falado cada vez mais sobre você..."

    "Será que ela tá vindo pra cá?"

    mc "Eu não vi ela, [s]. Desculpa."

    s "Não? Ufa... tudo bem."

    mc "Mas eu posso ajudar você a procurar por ela. Posso dar uma olhada aqui na ilha ou até lá no continente."

    s "N-não. Não precisa fazer tudo isso."

    menu:
        "Eu quero fazer isso por você, [s].":


            mc "Ei. Eu quero fazer isso por você. Não quero que fique preocupada desse jeito, tá? Pode confiar em mim."

            s "[mc]..."

            mc "Não vai ser trabalho nenhum pra mim. Pode deixar que se ela tiver por aqui eu vou achar."
        "Não quero que algo aconteça com a [fen].":


            mc "Eu também fico preocupado com a [fen]. Ela ainda é muito nova, vai saber o que pode acontecer."

            s "... Verdade."

            mc "Pode contar com minha ajuda."

    s "Tá. Obrigada mesmo."

    mc "Nem precisa agradecer."

    s "Então eu vou continuar procurando por aqui. E se você encontrar qualquer coisa me avise, por favor."

    s "É importante que você me avise assim que achar ela, tá?"

    mc "Claro. Não quero que você fique preocupada à toa."

    s "Até depois, [mc]."

    if sayuri_namoro:

        menu:
            "Um beijo.":


                mc "Um beijo. Tô com saudades de você."

                s "!!!"

                s "E-eu também... b-beijo..."
            "Até, [s].":


                mc "Até, [s]. Depois a gente se fala."
    else:


        mc "Até, [s]. Depois a gente se fala."

    "{i}Tuu... tuu...{/i}"

    scene ape_geral with Dissolve(1.0)

    "Se a [fen] não tá na Cidade Chinesa, então ela pode tá por aqui na ilha. Eu vou dar uma olhada."

    scene black with Dissolve(1.0)

    "..."

    scene cidade dia with Dissolve(1.0)

    pause

    "{i}puf puf{/i}"

    "A ilha não é lá tão grande, mas dá uma canseira..."

    "Nem sinal dela pelas ruas."

    scene mc parque_sentado with Dissolve(1.0)

    mc "Deixa eu tomar um ar."

    "A [fen] escapou... de novo... e se dessa vez é pra valer?"

    "E se a menina cansou dessa vida e só foi pra longe? Será que ela teria uma vida melhor longe disso tudo?"

    "A [s] disse que o [chi] não sabia onde ela foi, mas quem acredita? Da outra vez foi ele que pediu pra eu tirar ela de lá."

    "Pensando agora... por que será que ele queria que eu tirasse ela de lá bem naquele dia?"

    "Um dia longe da Cidade Chinesa não ia resolver nada... então por que?"

    "Se ele sabe onde a [fen] foi, mas não contou pra [s], então o Bao não confia na [s]..."

    "Será que a [s] é má então?"

    if s6_fenju_spa2:

        "Depois daquilo que aconteceu no banho... aquela agressão..."

    "Teve aquele dia que elas tavam treinando e a [s] foi rígida com a [fen]... pra falar o mínimo."

    "Mas então por que o próprio velho disse pra eu não julgar com meus olhos?"

    "Pensar nisso só tá me deixando mais confuso. Acho que vou {b}procurar a menina lá no centro{/b}."

    "Tenho que {b}pegar o busão até o continente{/b} e andar por lá até achar ela. Tenho que fazer isso agora, de {b}manhã{/b}."

    "Se alguém encontrar ela andando por aí antes de mim, vai saber o que vão fazer com a garota."

    jump call_cidade

label sayuri_evento7:

    $ iconchefe += 1

    $ sayuri_e7 = "evento"

    "{i}puf puf{/i}"

    mc "Afe!!! Cadê ela?!"

    "Ainda não acredito que eu decidi andar pelo centro inteiro procurando uma menina que eu mal conheço."

    "Se eu descobrir que ela tá dentro do carrinho do [chi] eu vou soltar a macaca."

    "Opa opa opa!"

    scene fenju_cidade_andando with Dissolve(2.0)

    pause

    "Esse chapéu... quem anda com isso pela rua?"

    "O tamanho... confere... é magrinha igual a [fen]... só pode ser ela..."

    "Se não for, vão me chamar de tarado. Mas qualquer coisa eu falo que ia pedir as horas."

    mc normal "Oi. Bom dia."

    "???" "Hm?"

    mc "[fen]?"

    "???" "!!!"

    mc "Calma, sou eu, o [mc]."

    scene fenju_cidade_vergonha with Dissolve(1.0)

    fen "[mc]!"

    menu:
        "Tá tudo legal, garota?":


            mc normal "Fala, [fen]. Tá tudo bacana?"

            fen "..."

            mc "É... bom dia?"

            fen "..."
        "Que estranho ver você aqui.":


            mc desconfiado "E aí? É estranho ver você aqui, fora da Cidade Chinesa."

            fen "..."

            mc envergonhado "Você não acha?"

            fen "..."

    mc zerado "Voltamos à estaca zero?"

    fen "E-eu..."

    mc desculpa "Você tá preocupada que eu te achei?"

    fen "..."

    mc normal "Não esquenta. Não vou falar pra ninguém que você tava aqui, tá bom?"

    fen "!"

    fen "N-nem pra [s]?"

    "Ixi... eu fiquei de avisar a [s] caso eu visse ela... Só que e se ela sair correndo quando eu ligar?"

    menu:
        "Nem pra [s]. Pode ficar tranquila.":


            mc normal "Pra ninguém. Nem pra [s]. Você fica mais de boa assim?"

            fen "S-sim... o-obrigada..."

            mc envergonhado "Não quero me meter nas coisas de vocês. Eu confio que você vai saber se cuidar."

            fen "..."
        "A [s] tá preocupada com você. Vamos avisar ela?":


            mc desculpa "E se a gente só avisar a [s]? Ela deve tá preocupada com você."

            fen "N-não! Por favor..."

            mc preocupado "Mas ela não é responsável por você, [fen]?"

            fen "S-sim... m-mas... eu... eu não queria. Por favor!"

            mc concentrando "Tudo bem... eu vou fazer como você tá pedindo."

            fen "O-obrigada..."

            mc "Mas e agora?"

            fen "..."

    mc "Da outra vez que a gente se viu lá na vila você tava mais falante... aconteceu alguma coisa?"

    fen "É que... ..."

    mc desconfiado "Queeee....?"

    fen "..."

    mc zerado "eeeee....."

    fen "T-tá... eu falo."

    mc normal "Ok."

    scene fenju_cidade_chapeu_close with Dissolve(1.0)

    fen "N-não era pra eu estar aqui."

    mc envergonhado "Imaginei..."

    fen "V-você me achou por coincidência?"

    mc desculpa "Na verdade a [s] me ligou e disse que você tava desaparecida. Daí eu procurei você pela ilha e daí vim pra cá."

    mc envergonhado "Andei um bocadinho..."

    fen "V-você fez tudo isso pra... me achar?"

    mc surpreso "Ah! Não foi nada de mais!"

    fen "..."

    fen "Mas como você descobriu que era eu?"

    mc zerado "Como assim? Esse chapéu aí..."

    fen "Q-quê?! P-por que o chapéu? Ele esconde meu rosto..."

    mc "[fen]... esse chapéu chama muita atenção."

    fen "M-mas..."

    mc "Sério que você pensou que ia se esconder usando ele?"

    fen "..."

    mc normal "Você pode ser boa de pirueta, mas ainda tá longe de aprender a arte de uma ninja."

    fen "... Vou tirar ele então..."

    mc envergonhado "Mas e agora? O que você pretende fazer?"

    fen "Eu..."

    fen "..."

    mc desconfiado "?"

    fen "Ai... "

    scene fenju_cidade_semjeito with Dissolve(1.0)

    fen "Eu estou indo em um lugar escondido... n-ninguém sabe..."

    mc surpreso "!"

    "Um lugar que ninguém sabe?!"

    menu:
        "Por que escondida?":


            mc desculpa "Por que você precisa ir lá escondida?"

            fen "..."

            mc "Não posso saber também?"

            fen "N-não é isso..."

            mc "Então por que?"

            fen "..."

            fen "A [s] e a m-mestra não entenderiam."

            mc desconfiado "..."

            "Que rolo será que essa garota se envolveu?"
        "Que lugar é esse?":


            mc envergonhado "Sem querer ser intromerido, mas já sendo... que lugar é esse?"

            fen "É..."

            mc desconfiado "..."

            fen "..."

            mc zerado "..."

            mc "Não vai falar?"

            fen "A-ai... desculpa..."

            mc concentrando "Ok... calma..."

    "Tá na cara que eu tô atrapalhando ela. E agora? Se eu deixar ela ir sozinha, vou decepcionar a [s], mas eu tô assustando ela..."

    "A menina fez tudo isso pra conseguir em um lugar secreto. Não quero atrapalhar tudo."

    "E agora?"

    "Espera! E se eu for com ela?! Eu continuo de olho nela e nem entrego ela pra [s]. Será que ela vai topar?"

    mc envergonhado "[fen]..."

    fen "O-oi..."

    mc "E se eu fosse com você pra esse lugar secreto?"

    scene fenju_cidade_surpresa with Dissolve(1.0)

    fen "C-comigo?!"

    mc "Não dá?"

    fen "E-eu não sei... eu... espera..."

    mc normal "..."

    fen "[mc]... melhor você não ir... D-desculpa..."

    menu:
        "Por que? Você não confia em mim?":


            mc desculpa "Você não confia em mim?"

            fen "N-não! Quer dizer... sim... digo..."

            mc envergonhado "Haha... calma..."

            fen "D-desculpa..."
        "Relaxa. Não quero te atrapalhar.":


            mc desculpa "Tudo bem... não quero te atrapalhar."

            fen "N-não é isso... é... que vai ser chato..."

            mc "Chato?"

    fen "É que... meninos... não é coisa de homem, entende?"

    mc normal "Como assim? Eu tenho certeza que eu vou adorar."

    fen "V-você... acha?"

    mc normal "Não importa o que é. Tenho certeza que eu vou gostar muito."

    fen "..."

    fen "É que sempre me falaram que tem coisa que é pra homem e coisa que é pra mulher..."

    mc normal "Quem falou isso pra você não sabe nada sobre mim. E se eu gostar?"

    fen "S-será?"

    mc charmoso "Tenho certeza. Eu gosto de tudo. Até injeção na testa."

    "O que eu tô falando?! Onde será que essa menina tá indo?"

    scene fenju_cidade_sorrindo with Dissolve(1.0)

    fen "Hihi... então tá..."

    mc surpreso "Sério?! Posso ir mesmo?!"

    fen "S-sim..."

    mc normal "Então bacana."

    mc envergonhado "E se você não quer que te vejam, o primeiro passo é não andar mais de chapéu..."

    fen "Ah! Ok..."

    scene fenju_cidade_semjeito with Dissolve(1.0)

    fen "Eu não pensei que ele ia chamar tanta atenção... bastante gente usa..."

    mc zerado "Ninguém usa isso, [fen]..."

    mc surpreso "Ah! Na Cidade Chinesa você tá falando!"

    fen "..."

    mc normal "Por isso que você pensou... mas isso não é comum aqui na rua. Você não sabia?"

    fen "N-não... foi depois que você falou que eu estou reparando... ninguém usa mesmo..."

    mc envergonhado "Você realmente precisa de umas aulas de convivência em sociedade."

    fen "Preciso?"

    mc "Tô brincando..."

    "Ou não."

    fen "Hihi..."

    "Agora ela parece melhor."

    if s6_fenju_spa2:

        "Eu não sei quando vou ter outra chance de falar com ela sozinhos. Eu podia aproveitar agora pra perguntar sobre o lance da [s] no banho."

        "Por um lado eu sei que é coisa delas e eu não devia me intrometer. Mas por outro... será que eu posso simplesmente deixar isso acontecendo?"

        menu:
            "Sobre aquele dia no banho...":


                mc desculpa "Eu queria falar com você sobre aquele dia que a gente foi no banho..."

                fen "Ah! Foi tão legal... d-desculpa por ter atrapalhado você e a mestra, mas eu queria tanto ir..."

                mc normal "Tá doida? Foi muito legal que você foi. Bem mais divertido."

                fen "Verdade?"

                mc "Claro. Você animou bastante."

                scene fenju_cidade_triste with Dissolve(1.0)

                fen "Mas a mestra não gostou muito..."

                mc desculpa "É sobre isso que eu queria falar... a [s] te bateu... não te machucou?"

                fen "C-claro que não... não fique pensando nisso. Foi tudo muito legal."

                "Por que ela continua falando isso?"

                mc serio "Olha, [fen]... nada disso é culpa sua, tá? Não precisa ficar preocupada com o que pode acontecer."

                mc "Você acha que é normal uma menina igual você apanhar assim?"

                fen "..."

                mc preocupado "Você acha que eu nunca reparei nos machucados no seu rosto?"

                fen "!"

                mc "Eu me preocupo com você..."

                fen "Isso... isso não é nada, [mc]. Não fica pensando nisso."

                mc serio "Esse é o problema. Você achar que tá tudo bem. NÃO tá tudo bem um jovem apanhar de adultos."

                mc serio "Em nenhum caso... nem pra 'ensinar'. Não existe 'educação na porrada'. Isso é um absurdo, [fen]."

                fen "Não é isso..."

                mc concentrando "Não é? Como assim?"

                fen "A mestra gosta de mim, [mc]."

                mc "A [s]?"

                fen "Sim... ela quer que eu termine meu treino e seja uma grande ginasta. Pra poder sair do templo e ser feliz."

                mc "[fen]..."

                fen "Você não pode pensar coisa ruim dela. Ela não é má. Tudo o que ela faz, é por mim."

                fen "V-você acredita em mim?"

                "Merda... ela não entende. Ela continua achando que tudo isso tá certo... Mas ela é só uma adolescente. Não dá pra eu forçar isso nela."

                mc normal "Claro que eu acredito."

                fen "Verdade?!"

                mc "Sim, ué. Se você tá falando."

                fen "É-é sim..."

                scene fenju_cidade_sorrindo with Dissolve(1.0)

                fen "O-obrigada, [mc]. Aquele dia no banho foi muito muito bacana. Eu gostei muito de conversar com você."

                mc normal "Eu também."

                fen "Quem sabe a gente não faz isso de novo um dia, né?"

                mc "Com certeza. Aquela vila que vocês moram é muito bonita. Eu quero dar uma andada lá de novo se der."

                fen "É... seria legal mesmo..."
            "Melhor não falar nada":


                "Pensando bem, a menina acabou de dar um sorriso. Não vou matar o clima falando sobre isso."

                "Eu tenho minha opinião sobre o que aconteceu. Não preciso importunar a [fen] com isso."

                "Bola pra frente."

    mc normal "Então vamos aí nesse lugar secreto?"

    fen "T-tá..."

    scene fenju_cidade_mc with Dissolve(1.0)

    pause

    mc "Ué? E seu chapéu?"

    fen "Eu joguei."

    mc "Só jogou?"

    fen "É. Ele é feio mesmo."

    mc "Haha... não era feio, não. Só era meio chamativo."

    fen "Sei lá... só achei ele feio mesmo. Talvez eu compre um boné."

    mc "Ia ficar muito bonitinha."

    fen "S-sério?!"

    mc "Eu acho. Se você quiser, a gente podia ir juntos. Ah! Eu conheço uma loja de roupas."

    fen "Hihi... ia ser bem legal."

    mc "Então tá fechado. Vai ser um presente meu."

    fen "Um presente... mas pelo quê?"

    mc "Hmmm..."

    mc "Pelo seu esforço em ser uma grande ginasta e aguentar aquele monte de treino no templo! Isso é incrível, [fen]. Merece uns dez bonés!"

    fen "D-dez?!"

    mc "Será que a gente consegue escolher dez bonés bonitos diferentes?"

    fen "Hihi... é muito boné, [mc]."

    mc "Quem sabe..."

    fen "A gente tá chegando. É nesse próximo prédio."

    "Ainda não dá pra saber do que se trata isso aí. Um lugar secreto... será que ela tá pensando em mudar de casa? A família dela talvez?"

    "Se for a família dela, o que eu vou falar? A gente nem é amigo nem nada... Talvez eu possa falar que sou o segurança."

    fen "Pode entrar."

    mc surpreso "O-ok."

    scene black with Dissolve(1.0)

    mc normal "Licença."

    scene salao_ballet geral with Dissolve(1.0)

    pause

    mc desconfiado "Chegamos?"

    fen "Sim."

    "???" "[fen]? É você que chegou?"

    fen "Sim!"

    "???" "Vem aqui trocar de roupa. Eu tô aqui também."

    fen "T-tá!"

    fen "Eu já volto, [mc]."

    mc normal "Tudo bem. Eu tô aqui."

    "Certo... Deixa eu ver..."

    "Essas barras aqui... parece ser alguma coisa de exercício. Ou pra colocar roupa no cabide... mas é meio baixa."

    "Ah! Aqueles quadros! Aqueles movimentos... e o close nos pés... são pessoas dançando."

    "Será que aqui é um salão de dança?"

    fen "[mc]..."

    mc surpreso "O-oi!"

    mc "!!!"

    scene fenju_shoshana_ola with Dissolve(1.0)

    pause

    mc envergonhado "O-oi..."

    "???" "Bonjour, senhor. Você veio com a [fen]?"

    mc "A-a... s-sim. Eu encontrei ela na rua e acompanhei ela até aqui. Vocês se conhecem?"

    "???" "Oui."

    "Que bosta de pergunta foi essa? E o que ela quis dizer?"

    fen "D-desculpa... ela é minha professora de ballet, [mc]. O nome dela é [sh]."

    mc normal "Muito prazer, [sh]. Eu sou o [mc]. Mas ela já disse... hehe..."

    sh "Bienvenu ao meu estúdio, monsieur [mc]."

    "Que massa o jeito que ela fala! O sotaque é tão diferente..."

    mc "Obrigado."

    sh "Mademoiselle [fen] está aprendendo a fina arte do ballet."

    mc surpreso "Ballet! Esse era o segredo?"

    fen "S-sim..."

    sh "Segredo?"

    fen "N-não é nada..."

    "Opa... acho que eu falei demais."

    "M-mas olha pra essa mina..."

    window hide

    pause

    "[sh]... que nome estranho... mas essa loira é incrível. E ela deve ser de outro país e tudo... Uma garota exótica pra caramba..."

    sh "Tudo bem, monsieur [mc]? Alguma pergunta?"

    mc surpreso "Ah!"

    "Caralho, eu tô olhando direto pra ela que nem um tarado, sei lá."

    menu:
        "Desculpa... É que eu achei você muito bonita.":


            mc charmoso "Desculpa. Não queria ficar encarando. É que eu achei você muito bonita, [sh]."

            sh "Hmmm... Les choses de la vie, monsieur [mc]."

            mc desconfiado "Como é?"

            sh "Hihi..."

            fen "Às vezes ela fala em francês assim..."

            mc envergonhado "Ah! Haha..."
        "Nada não! Malz!":


            mc angustiado "D-d-desculpa! Eu s-só tava... sei lá!"

            "Fen Ju e Shoshana" "Hihi..."

            sh "Sourir é muito bom, não é, amiga [fen]?"

            fen "O [mc] é muito legal, professora."

            sh "Posso ver... ele ficou todo vermelho."

            mc envergonhado "Haha..."
        "Fiquei impressionado que a [fen] tá no ballet.":


            $ shoshana_amizade += 1

            mc charmoso "Caraca. Fiquei impressionado que a [fen] tá no ballet."

            sh "Por que?"

            mc "Ela tem uma rotina bem corrida e ainda encontra tempo pra isso. É incrível, [fen]."

            fen "A-a..."

            sh "Miam-miam, mademoiselle [fen]. Eu não sabia dessa correria toda."

            fen "N-não é nada de mais, professora..."

            mc normal "Como não?"

            fen "..."

    mc envergonhado "Mas então! Como essas aulas começaram? Não sabia de nada disso."

    scene fenju_shoshana_close with Dissolve(1.0)

    sh "Mademoiselle se interessou pelas minhas aulas, mas nunca tinha tempo, não é mesmo?"

    fen "S-sim... obrigada por aceitar dar aulas pra mim desse jeito."

    sh "Mon Dieu! Não fale uma coisa dessas, menina. Você é minha amiga e é claro que eu ia aceitar."

    sh "Ballet é meu amour e você merece. É uma excelente aluna. Você precisa de um pouco mais de bonheur na sua vida."

    fen "..."

    mc normal "Você parece uma garota bem entusiasmada com ballet, [sh]."

    sh "Ballet é minha vida. É a arte em movimento. A fala do corpo e da alma."

    sh "Aquele que quer aprender a voar um dia precisa primeiro aprender a ficar de pé, caminhar, correr, escalar e dançar."

    mc charmoso "Que bonito..."

    sh "A mademoiselle já sabe fazer quase tudo. Por isso agora ela estuda ballet."

    fen "..."

    sh "Oui... acho que falamos demais. Por que você não começa o aquecimento, [fen]?"

    fen "O-ok. O que eu faço hoje?"

    sh "Pode começar pela barra, como sempre. Você acha que dá conta de Demi-plíés e battements tendus?"

    fen "Acho que sim..."

    sh "Então pode começar. Enquanto isso vou falar com o monsieur [mc] por um momento, oui?"

    fen "T-tá."

    "Falar comigo? O que eu fiz? Bom... não vou reclamar de falar com essa garota. Não é todo dia que a gente fala com uma gata dessas."

    sh "Pode vir comigo?"

    mc normal "C-claro."

    sh "Merci."

    mc desconfiado "?"

    scene salao_ballet geral with Dissolve(1.0)

    mc normal "Eu não sei o que raios ela quer que você faça, [fen], mas boa sorte."

    fen "Hihi... obrigada."

    sh "Por aqui. Aqui perto da minha sala vamos dar um espaço a ela."

    mc "Tá."

    scene shoshana_mc_conversando with Dissolve(1.0)

    pause

    sh "Que bom que você apareceu, monsieur."

    mc "Por que?"

    sh "Estou preocupada com a situação da mademoiselle. Mon Dieu! Olhe para aqueles machucados!"

    mc "Eu sei..."

    sh "Vou tentar falar baixo, mas essa situação está me deixando aflita, monsieur [mc]."

    mc "Pode me chamar só de [mc]."

    sh "Merci, [mc]. Eu estou preocupada com o stress que vive a garota. Ela é jovem e as coisas não devem estar fáceis onde ela vive."

    menu:
        "Concordo com você.":


            mc "Concordo com você. É uma situação delicada."

            sh "Oui. E eu sofro muito pensando que queria fazer algo para ajudar a pobrezinha. Mas o que?"

            mc "Entendo que é difícil para você fazer alguma coisa..."

            sh "Sim."
        "Você sabe alguma coisa sobre ela?":


            $ shoshana_amizade += 1

            mc "Você tem alguma informação sobre ela?"

            sh "Infelizmente não. A mademoiselle não se abre. Entra muda e sai calada das aulas."

            mc "Ela é assim comigo também. Eu queria muito saber mais sobre a situação dela."

            sh "Eu também! É uma pena..."

    "Não sei se quero contar pra [sh] o que acontece com a [fen]. Eu sei muito pouco sobre ela ainda."

    sh "Eu acredito que ela está sob forte stress e isso acaba influenciando ela de uma forma muito negativa."

    sh "Eu consigo ver nos olhos dela o quanto ela ama o ballet, mas ela não pode participar de todas as aulas."

    sh "Ela só está conseguindo aprender pois eu aceitei dar aulas particulares neste único dia que ela pode."

    mc "Entendi..."

    sh "C’est impossible! Como uma garota dessa idade pode ter tantos afazeres que não pode fazer uma aula de ballet?!"

    "Se a [sh] soubesse que a [fen] tá sendo treinada pra substituir a [s] na delegação chinesa de ginástica..."

    "Parece que ela realmente tá preocupada com a [fen]... será que eu devia contar isso pra ela?"

    "Mas se ela própria não falou nada pra professora de ballet... talvez ela não quer que descubram... aaahhhh o que eu faço?!"

    menu:
        "Melhor guardar segredo":


            "Deixa quieto. Se nem a [fen] contou, não sou eu que vou dar com a língua nos dentes. Deixa que ela conta."

            mc "É duro... mas não sei o que pode ser também..."

            sh "Merde..."
        "Contar sobre o treinamento da [fen]":


            $ shoshana_amizade += 1

            scene shoshana_mc_conversando2 with Dissolve(1.0)

            mc "Assim... ela participa de um treinamento muito sério."

            sh "Hmm..."

            mc "A [fen] está sendo preparada para substituir a ginasta [sc] na delegação chinesa das olimpíadas."

            sh "Mon Dieu!"

            mc "Pois é... por isso ela praticamente não tem tempo pra nada. Não é fácil pra ela. É bastante pressão."

            sh "Isso explica muita coisa, [mc]. Pra mim é muito importante saber isso. Merci."

            mc "Eu percebi que você é gente boa e tá preocupada com ela. A [fen] precisa de toda a ajuda que puder achar."

            sh "Oui..."

            sh "Então é por isso..."

            mc "Hm?"

    sh "A [fen] não é uma garota comum, [mc]."

    mc "Em que sentido você diz?"

    sh "Olhe pra ela."

    scene fenju_bailarina_pose1 with Dissolve(1.0)

    pause

    sh "Esta deve ser a terceira ou quarta aula dela. E eu já estou pensando em trocar ela para um nível avançado."

    mc "S-sério?!"

    sh "Mademoiselle tem um controle sem igual dos fundamentos. Uma vez explicado, ela executa praticamente com maestria."

    "Claro... sendo treinada a vida toda..."

    sh "O controle que ela tem sobre o corpo é impressionante. Eu nunca vi isso em uma aluna antes."

    mc "Isso é tão incrível assim?"

    sh "Oui, [mc]. Isso não é apenas prática. Isso vem da mente também."

    mc "Da mente? Tipo, inteligência?"

    sh "Não apenas inteligência, mas a memória, a capacidade de interpretação do que é passado, como ela lida com o emocional..."

    sh "Se fosse possível, eu diria que mademoiselle [fen] não é humana."

    mc "C-como assim?!"

    scene fenju_bailarina_pose2 with Dissolve(1.0)

    pause

    sh "Não quero parecer uma louca, mas mesmo na minha escola da França, com garotas extremamente talentosas em ballet, nenhuma se aproxima dela."

    sh "Quando me mudei e comecei a dar aulas aqui, eu sabia que estaria longe do ballet no mais alto nível, mas tudo bem... les choses de la vie..."

    sh "Entretanto, mademoiselle foi além de todas minhas expectativas. Eu não tenho dúvidas que ela é um gênio."

    mc surpreso "Uou..."

    "Eu nunca tinha pensado na [fen] desse jeito. Um gênio?"

    "Será que é por isso que ela é tão importante pra Cidade Chinesa?"

    if s6_fenju_spa2:

        "Será que é por isso que a [s] chamou ela de monstro daquela vez?"

        "Pareceu uma palavra tão forte... mas será que a [s]... tava com inveja dela?"

        "Mas a [s] é a maior atleta do país! Eu sei que ela representa a China, mas nunca ninguém que vive aqui conseguiu o que ela conseguiu."

        "Ela deve ser um gênio também... certo?"

    sh "[mc]?"

    scene shoshana_mc_conversando2 with Dissolve(1.0)

    pause

    mc "D-desculpa... eu tava pensando no que você disse."

    sh "Uma garota com essa capacidade... talvez tudo isso seja demais pra ela. E ela precisa se livrar desse stress de alguma forma."

    sh "E é por isso que ela... você entende, né?"

    mc "Claro... não é fácil."

    sh "Bom... Tourner la page. Eu fiquei feliz de saber que ela pode contar com alguém como o monsieur."

    menu:
        "Eu sou mais amigo da [s]. Por ela que conheci a [fen].":


            mc "Eu sou mais amigo da [s] pra falar a verdade. Eu conheci a [fen] por ela."

            sh "Oh. Então foi isso. Mas se você está aqui, pode fazer alguma coisa por ela."

            mc "Vou tentar fazer o máximo que eu puder, mas também não pretendo me intrometer demais."

            sh "Entendi."
        "Pode deixar que eu vou proteger ela.":


            $ shoshana_amizade += 1

            mc "Pode deixar. Eu vou cuidar dela e garantir que ela passe por isso."

            sh "Merci. Fico muito mais tranquila sabendo disso."

            sh "Você parece ser um monsieur bem confiável e atencioso, [mc]. Não costumo ver isso."

            mc "Eu só quero ajudar ela no que der."

            sh "Oui."

    sh "Agora deixa eu fazer a minha parte."

    if shoshana_amizade >= 3:

        $ shoshana_beijo = True

        sh "Ah! Mas antes..."

        mc "Hm?"

        scene shoshana_mc_beijo with Dissolve(1.0)

        pause

        mc "!!!"

        sh "Une bise."

        mc "O-oi?"

        sh "Por ser um grande amigo da mademoiselle [fen]."

        sh "Não seria um problema pra mim ter você aqui em outras aulas, ok?"

        mc "A-ah... t-tá!"

        sh "Fofo."

    scene salao_ballet geral with Dissolve(1.0)

    sh "Muito bem, mademoiselle. Pronta para a aula de verdade?"

    fen "Sim... eu aqueci."

    sh "Muito bem. Força nas pernas. E 1, e 2, e 3... música!"

    scene fenju_shoshana_treino with Dissolve(1.0)

    sh "Força nas pernas, garota. Vai vai vai!"

    fen "S-sim!"

    "..."

    "Ver o treino da [fen] aqui é bem diferente lá do templo. A [sh] parece tão atenciosa com ela, mas não tem aquela vibração pesada."

    "Não sei se é só minha cabeça, mas eu acho que ela tá mais feliz aqui que praticando ginástica rítmica."

    "Eu fico pensando se realmente foi ela que quis participar da Olímpiada. E se alguém colocou ela nisso? Seria pior ainda..."

    "Pensando nisso agora... e a [s]? Será que ela queria deixar as competições pra dar lugar pra [fen]? E se ela ainda queria ser uma atleta?"

    "Aquela vez, se eu tô lembrando certo, ela disse que não sabia se ia participar, mas ela pareceu meio pra baixo. Ela não parecia aliviada."

    "Acho que eu podia perguntar isso pra ela um dia. Tentar entender essa relação das duas melhor."

    sh "Já está cansando?"

    fen "N-não!"

    sh "Está sim, que eu sei..."

    fen "..."

    fen "{i}puf puf{/i}"

    fen "A-ainda tá torto..."

    sh "Ei! Calma, [fen]."

    fen "..."

    sh "Mon Dieu!"

    fen "O-oi?"

    sh "Você não precisa fazer tudo certo nas suas primeira aulas, garota."

    fen "M-mas-"

    sh "M-m-mas nada. Dançar é uma arte, não uma maldição. Quando você deixa de fazer por gosto pra fazer por obrigação, perde a essência."

    fen "Mas eu preciso fazer certo, professora."

    sh "Fazer certo é fazer com gosto e alegria."

    fen "Como assim?"

    sh "C’est impossible! Ouça sua professora e chega por hoje."

    fen "T-tá..."

    sh "A gente vai se ver muito ainda, boba. E eu não vou deixar você parar de dançar até estar feliz com seu desempenho. A gente não precisa ter pressa, entendeu?"

    fen "Então não tem problema? Posso continuar da outra vez..."

    sh "Oui, mademoiselle. Temos muito tempo pela frente, certo?"

    fen "Ok. Obrigada, professora."

    sh "Agora vai se trocar."

    fen "Tá."

    scene salao_ballet geral with Dissolve(1.0)

    sh "Logo ela volta."

    sh "E eu vou aproveitar para me arrumar tambem. Mas mansieur não precisa sair. Apenas espere virado para lá por favor."

    "S-sério? Será que é costume do país dela ser aberta desse jeito..."

    mc envergonhado "N-não quero incomodar. Vou esperar ela lá fora."

    sh "Sua escolha. Espero ver você de novo."

    mc charmoso "Pode deixar. Foi um prazer. Au revoir, [sh]."

    sh "Au revoir, monsieur [mc]."

    scene black with Dissolve(1.0)

    "Hmm..."

    "Ela deixou a sala pra Fen Ju se trocar e ela vai se arrumar no próprio salão?"

    "Se eu desse uma olhadinha pela porta..."

    "S-será que dá pra ver alguma coisa?!"

    "Não... é melhor eu não ficar de taradisse agora."

    label say7_premium1:

        pass

    "Ou será que..."

    menu:
        "Dar uma olhada...":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_48

                jump say7_premium1

            "Só uma olhadinha..."

            scene black with dissolve

            "{i}inheeec{/i}"

            scene say7_p1 with Dissolve(1.0)

            pause

            "Opa... parece que elas ainda vão conversar um pouco..."

            sh "Quem é era esse rapaz?"

            fen "Ah... e-ele... é um amigo da minha mestra."

            sh "Hmm..."

            sh "Por que ficou assim, mademoiselle?"

            fen "Hm-hm?!"

            sh "Você parece diferente... sua voz... quando falou desse homem."

            fen "N-não, professora!"

            sh "{i}tsc tsc{/i}"

            sh "Você sofre de amor impossível... Diou..."

            "Q-quê?! N-não é possível..."

            fen "Ah..."

            scene say7_p2 with Dissolve(1.0)

            sh "Quando eu tinha mais ou menos sua idade eu senti a mesma coisa por um professor."

            sh "Eu sonhava com ele e queria ficar com ele..."

            fen "Ahn?!"

            sh "Um dia eu aproveitei uma festa na escola pra entregar um recado pra ele contando que eu gostava dele."

            fen "E o q-que aconteceu?"

            sh "Passou um tempo e ele veio falar comigo depois de uma aula. A gente tava sozinhos."

            sh "Ele disse que eu era uma garota muito especial. E daí..."

            fen "?"

            sh "Ele disse que a gente não podia ficar juntos."

            fen "P-por quê?!"

            sh "Ele não explicou muito, mas pediu pra eu parar de pensar nesses tipos de coisa."

            sh "Eu fiquei muito triste aquele dia. Foi a primeira vez que eu tinha levado um fora... e doía muito, pequena."

            fen "..."

            scene black with dissolve

            scene say7_p3 with Dissolve(1.0)

            sh "Hoje eu entendo ele perfeitamente, Fen Ju. E eu sou muito agradecida por ele ter feito isso."

            fen "Hm?"

            sh "Você ainda é uma adolescente e vai demorar pra você entender o que eu vou falar. Mas é bem simples."

            sh "Os adultos precisam se responsabilizar pelas crianças. Não tá errado uma garotinha gostar de um homem."

            sh "Mas os mais velhos precisam entender que crianças ainda tão aprendendo... e não podem se aproveitar dessa inocência."

            sh "Seria fácil pra aquele professor se aproveitar da minha paixonite quando eu era mais nova. Mas não ia ser certo."

            fen "Hmm..."

            sh "Os adultos precisam proteger os mais jovens. E evitar que eles façam coisas que prejudiquem a vida deles."

            scene say7_p4 with Dissolve(1.0)

            sh "Por isso hoje eu sou muito agradecida por ele ter me protegido."

            sh "Foi muito ruim aqueles dias... parecia que meu coração tinha sido despedaçado."

            sh "Mas hoje eu vejo como ele foi bacana comigo. Seria muito pior se ele tivesse aceitado qualquer coisa comigo."

            sh "Então... eu espero que esse rapaz entenda o que ele tem que fazer também."

            fen "E eu?"

            sh "Você ainda tá entendendo suas emoções e sentimentos... não se preocupe. Você vai aprender com o tempo."

            sh "Agora, os adultos responsáveis por você têm que garantir que você vai crescer feliz e protegida."

            sh "Você vai ser uma mocinha muito talentosa. E eu quero que você seja muito feliz, do seu jeito, mademoiselle."

            fen "M-mas eu..."

            sh "Acho bom você pensar no ballet e menos em outras coisas, ok?"

            fen "O-ok..."

            "Tadinha da Fen Ju... será que ela realmente sente isso? Espero que ela encontre um garoto da idade dela."

            "Agora... Uau... a Shoshana é incrível... linda... e pelada desse jeito então..."

            "Eu tenho que dar um jeito de falar com ela de novo."

            "Como será que eu consigo isso?"
        "Ir embora.":


            "Melhor eu não arriscar... eu posso perder pontos com ela assim."

            "Vou esperar a Fen Ju lá fora."

    scene cidade centro3 with Dissolve(1.0)

    "Então era isso..."

    "Todo o segredo da [fen] era ir no ballet. Ainda não tô crendo nisso."

    "Por que uma pessoa teria que fazer tudo isso só pra fazer uma aula de dança? Será que até isso proibem ela?"

    "Ou será que ela tem outro motivo? Será que ela não quer que o pessoal da Cidade Chinesa saiba? E o Bao? Será que ele tá ligado disso?"

    "Bom... agora eu sei o segredo dela. Tenho que pensar o que eu vou fazer com relação à [s]. Ela deve tá louca atrás da menina até agora."

    "Talvez o melhor seja avisar ela, mesmo que a [fen] não queira."

    fen "[mc]... terminei."

    mc normal "Opa."

    scene fenju_cidade_sorrindo with Dissolve(1.0)

    fen "Obrigada por vir comigo. O-o que você achou? N-não foi muito chato?"

    mc normal "Chato? Claro que não."

    fen "Hihi... você é estranho, [mc]."

    mc zerado "Estranho? Como assim? Por que?"

    fen "Eu não imaginei que um rapaz pudesse gostar de ballet."

    mc envergonhado "Ah..."

    menu:
        "Não tô falando que gosto de ballet.":


            mc envergonhado "Não que eu goste de ballet... mas não foi chato acompanhar você. Foi bem rápido."

            fen "Ah tá..."
        "Eu gostei, sim. Você foi incrível.":


            mc normal "Eu gostei, sim. Você fez aqueles movimentos e aquela professora falando em francês. Foi divertido."

            fen "Viu? Falei que você é estranho hihi..."

            mc zerado "Ei..."

            fen "Você... parece que você não se preocupa tanto com o que os outros vão pensar. Você... parece corajoso."

            mc envergonhado "Só por que eu fui no ballet?"

            fen "É. Mas quando eu falei com o Bao sobre isso, ele disse que ballet não é coisa pra homem."

            mc "Sério? Acho que ele é velho... só isso."

            fen "Como assim?"

            mc normal "Pessoas mais velhas pensam um pouco diferente da gente. Eles nasceram em uma outra época, onde essas 'coisas de homem e mulher' eram mais restritas."

            mc "Só que a cabeça das pessoas mudou com o tempo. Hoje, essa linha é menos definida. Tem mulher fazendo coisas que antes 'eram de homens' e vice-versa."

            fen "E-entendi. Eu não sabia disso. O pessoal da vila é quase todos velhos e eles quase nem falam..."

            mc "Não tem problema. Quando você sair de lá, você vai ver como é mundo de verdade."

            fen "Puxa... p-parece bem legal, [mc]."

            mc normal "Com certeza."

    mc desconfiado "Mas e agora? Pra onde a gente vai?"

    fen "Ah. Eu vou voltar pra casa."

    mc "Sério?"

    fen "Sim. Eles devem estar preocupados comigo. Fazem horas que eu saí."

    fen "A mestra deve estar me procurando até agora..."

    fen "[mc]..."

    mc normal "Oi?"

    fen "Quer ir comigo? A gente p-podia ir conversando..."

    "Tenho nada pra fazer agora. Por que não?"

    mc normal "Vamos. Eu acompanho a mademoiselle."

    fen "Hihi... bobo."

    scene black with Dissolve(1.0)

    scene cidade centro4 with Dissolve(1.0)

    mc desconfiado "Ah. Dá pra chegar na Cidade Chinesa por aqui, né?"

    fen "Sim. A gente só tem que andar um pouquinho."

    mc normal "Sem problemas. Posso não ser um atleta, mas uma caminhada eu aguento."

    scene cidade centro6 with Dissolve(1.0)

    if mc_fisico < 200:

        mc concentrando "{i}puf puf{/i}"

        mc "Bota caminhada nisso, hein?"

        fen "Hihi... ainda falta metade, [mc]."

        mc angustiado "Aaahhh..."
    else:


        mc normal "Bacana este lugar."

        fen "Puxa... até que você tem resistência, hein..."

        mc "Ir na academia tem suas vantagens, né."

        fen "Ah. Então você também faz exercício. Isso é bom."

        mc normal "Sim."

    scene black with Dissolve(1.0)

    $ tempo = 2

    scene chinatown geral with Dissolve(1.0)

    mc surpreso "Aleluia!"

    mc zerado "Você não tá nem suando... Isso que você acabou de fazer aula."

    fen "I-isso não é nada, [mc]."

    if mc_fisico >= 200:

        fen "Mas você também não cansou. Parabéns."

        mc charmoso "Muito treino correndo na esteira haha..."

    fen "Daqui eu vou pra vila. Obrigada por vir comigo."

    mc envergonhado "Ah... eu não posso ir lá, né?"

    show fenju cidade with dissolve

    fen "S-só com a permissão dos líderes. Da outra vez a [s] deve ter convencido eles."

    mc "Entendi..."

    fen "V-você queria ir lá, [mc]?"

    mc "Pois é... eu tava pensando em dar uma olhadinha naquela vila antiga de novo..."

    fen "Hmmm..."

    mc normal "Foi tão legal aquele dia e também, pra ser sincero, eu tava pensando em saber um pouco mais sobre isso, talvez pra revista."

    fen "Escrever uma matéria sobre a Cidade Chinesa?"

    mc "Tipo isso. Não seria legal?"

    fen "N-não sei... o pessoal aqui é tão... quieto..."

    mc concentrando "Por isso mesmo. Seria uma coisa muito incrível pra mim poder escrever sobre isso, já que é tão secreto."

    fen "E-entendi... s-se você acha isso tão legal e é tão importante pro seu trabalho... eu acho que posso te ajudar."

    mc surpreso "S-sério?!"

    fen "Acho que sim..."

    mc preocupado "Mas isso não é ruim pra você?"

    fen "Não precisa ficar preocupado. Eu vivo fazendo coisa errada... Ia ser mais uma..."

    mc envergonhado "Haha... entendi."

    "A [fen] pode me ajudar a entrar na vila secreta da Cidade Chinesa. E talvez sozinho. Se eu tomar cuidado, dá pra tentar encontrar vários segredos."

    "Mas usar uma jovenzinha igual ela pra conseguir o que eu preciso? Será que eu tô indo longe demais?"

    "Mas seria um dos meus primeiros trabalhos investigativos de verdade! Deixar essa vida de fuxico e ir realmente atrás das matérias que importam."

    "Se eu aceitar, posso continuar, mas se eu não tiver a ajuda [fen], vou ter que parar aqui e voltar pra casa."

    "Aaahhh! O que eu faço?!"

    menu:
        "Tudo bem. Eu vou aceitar sua ajuda, [fen].":


            $ s7_continua = True

            mc concentrando "Ok... eu não quero te ferrar... então pense bem se tudo bem fazer isso."

            mc normal "Porque, por mim, eu vou aceitar sua ajuda, [fen]."

            fen "T-tudo bem, [mc]. Você me ajudou muito também."

            if s5_ajudou:

                fen "Aquele dia que a gente foi na praia... até hoje eu lembro disso. Foi um dos dias mais felizes da minha vida."

                mc desculpa "Mas não foi quase nada..."

                fen "Claro que foi."

            fen "Hoje você foi no ballet comigo e não contou pra mestra. Eu vou ficar feliz de ajudar você também."

            mc normal "Tá legal. Valeu mesmo, [fen]."
        "Melhor eu voltar pra casa.":


            $ sayuri_e7 = "casa"

            mc normal "Valeu, [fen]. Mas é melhor eu não fazer isso. Não quero te colocar em uma encrenca."

            fen "Mas-"

            mc charmoso "Relaxa, menina. Você é muito bacana. Sou eu que não quero, ok? Pensando bem, nem seria uma matéria tão incrível assim."

            fen "..."

            mc normal "Foi muito legal ir no ballet hoje com você. Se cuida, tá?"

            fen "Obrigada, [mc]..."

            fen "É... sabia... eu sempre quis ter um irmão... e você parece um irmão..."

            mc "Ounn... e você é minha maninha. Toma cuidado, tá legal? Eu vou fazer de tudo pra proteger você. Qualquer coisa é só falar comigo."

            fen "T-tá.... obrigada."

            fen "[mc]..."

            mc normal "Que foi?"

            scene fenju_mc_abraco with Dissolve(1.0)

            pause

            fen "..."

            mc "..."

            fen "Eu gosto de você..."

            mc "E-eu também... n-não precisa ficar assim..."

            fen "Você é meu melhor... m-meu único amigo."

            mc "Pode contar comigo. Qualquer problema me fala."

            fen "T-tá..."

            mc "Fica bem, tá legal?"

            fen "Eu vou dar o meu melhor."

            mc "Tudo bem. Mas se cuida. Não exagera. Lembra do que a [sh] disse."

            fen "T-tá... Tchau..."

            mc "A-até."

            scene black with Dissolve(1.0)

            "..."

            jump sayuri_e7_final

    mc desconfiado "Mas como você vai me colocar pra dentro? Será que os líderes vão aceitar seu pedido?"

    fen "N-não... Eles nunca vão aceitar se eu pedir."

    mc "Ué..."

    fen "Você vai ter que entrar escondido."

    mc surpreso "Como é?!"

    fen "A vila é super vazia. Você viu quando tava com a [s] lá. Não tinha ninguém. Normalmente os moradores estão fazendo coisas importantes."

    fen "O único problema é a guardiã..."

    mc desconfiado "..."

    fen "Ela consegue saber que tem gente chegando no portal, mas não sabe quem é. Se a gente chegar juntos, mas só eu falar com ela, ela não vai saber de você."

    fen "Daí eu atraio ela pra fora do portão e você passa."

    mc envergonhado "E-esse é o plano?"

    fen "S-sim..."

    "Se isso não der certo a mestra da [s] vai me matar."

    "Esse povo é totalmente diferente do que a gente tá acostumado. É bem possível que eles queiram fazer justiça aqui mesmo."

    "{i}glup{/i}"

    mc concentrando "Bom... se é o melhor jeito..."

    fen "É o único jeito eu acho..."

    mc charmoso "Ok. Quem não chora não mama. Quem não cola não sai da escola, certo?"

    fen "Q-quem não cola?"

    mc zerado "Nada, não..."

    scene black with Dissolve(1.0)

    fen "Vem. Vamos pro portal."

    scene chinatown caminho with Dissolve(1.0)

    fen "Daqui a guardiã pode saber que tem gente chegando. Passa bem do meu lado pra ela não achar que tem duas pessoas."

    mc preocupado "Tá."

    "Não tô gostando nada disso. Essa mina me dá medo..."

    "..."

    scene chinatown portal with Dissolve(1.0)

    fen "Certo. Agora aqui vai pra lá. Quando você ver que a gente saiu de perto do portal, você passa rápido, tá?"

    mc "Ok."

    show fenju cidade with dissolve

    fen "Eu posso esperar você vo-"

    mc normal "Não quero que a gente se fale mais hoje. Porque se alguém me ver, não quero que te coloquem no rolo."

    fen "M-mas como você vai sair?"

    mc "Eu dou meu jeito."

    fen "M-mas, [mc]... se eles te peg-"

    mc "Relaxa. Eu vou dar meu jeito, ok?"

    fen "..."

    mc zerado "Ei. Não precisa fazer essa cara. Eu mereço um pouco de confiança."

    fen "T-tá... então vai. Ela não pode ver você."

    mc charmoso "Pode deixar. Valeu pela ajuda e se cuida!"

    hide fenju cidade with dissolve

    "Vou esperar aqui enquanto ela arranca a mina do portal. Daí é só sair correndo e passar por lá."

    "Opa. Ela chegou."

    scene fenju_xiangu_portal with Dissolve(1.0)

    pause

    "Aquela espada..."

    fen "O-oi... voltei..."

    xu "Senhorita [fen]. É bom vê-la. Estavam procurando pela senhorita."

    fen "Ahh... desculpa... e-eu... me perdi."

    xu "Se perdeu? Onde?"

    fen "Eu... tava treinando no templo e daí quis comer um lámen com o senhor Bao, mas daí errei o caminho e acabei lá no centro da cidade."

    xu "Senhorita! Que perigo... você precisa tomar cuidado."

    fen "M-mas deu tudo certo. Eu encontrei o caminho de volta. Só demorou um pouco..."

    xu "O importante é que a senhorita está bem. Você deve entrar logo e avisar a todos."

    fen "Ah! Será que você pode me ajudar com isso? Eu p-perdi... meu... pingente! E queria procurar por ele. Você pode avisar todo mundo?"

    xu "Mas, senhorita, o portal-"

    fen "Não se preocupe com isso. Eu ficarei de guarda no seu lugar."

    xu "..."

    fen "Por favor?"

    xu "Sem problemas. Farei pela senhorita."

    "A [fen] também tem uma lábia... nunca que eu ia imaginar isso..."

    fen "Muito obrigada!"

    scene chinatown portal with Dissolve(1.0)

    "Opa. Elas saíram do portal. É minha chance!"

    scene black with vpunch

    "Gogogogo!"

    "..."

    scene chinatown vila_entrada with Dissolve(1.0)

    "Ufa... consegui! Entrei!"

    "Tô aqui. Uma chance de dar uma olhada neste lugar incrível sem ninguém no meu pé. Só preciso tomar cuidado pra ninguém me pegar."

    "Eu não quero que ela me corte em dois e nem que a mestra da [s] me pegue invadindo a propriedade deles."

    "Pensando bem... o que a [s] ia pensar de mim se ela me pegasse aqui invadindo a 'casa' dela sem ser chamado? Isso não ia pegar bem."

    "Por isso todo cuidado é pouco."

    label s7_vila:

        "Ok. Pra onde eu vou agora?"

    menu:
        "Portal":


            $ s7_vila += 1

            scene chinatown vila_saida with Dissolve(1.0)

            "Eu lembro daqui. É por aqui que eu chego e posso ir embora também."

            "Da outra vez eu saí e ninguém falou nada depois que eu fui embora. Provavelmente a [s] já tinha acertado tudo sobre minha visita."

            "Mas agora é diferente. Eu entrei sem aviso. Não sei se vão deixar eu sair assim tão de boa."

            "Preciso ficar esperto."

            jump s7_vila
        "Centro":


            $ s7_vila += 1

            scene chinatown vila_geral with Dissolve(1.0)

            "Daqui dá pra ver a vila toda. É realmente um lugar bem diferenciado. O ar aqui tem uma coisa meio mística, sei lá..."

            "Eu lembro de ter sentado naquele degrau de madeira com a [s]. A gente conversou sobre várias coisas."

            "Depois a [fen] chegou. Ela parecia bem animada e queria ir com a gente pro banho."

            "Pensando agora, ela parece um pouco carente... ela queria porque queria ir com a gente."

            "Não deve ser fácil passar por esse treinamento em um lugar tão diferente do resto do mundo. E as duas passam por isso."

            "Eu queria ter coragem de perguntar pra elas, pra valer, se elas realmente gostam de fazer isso e insistir até elas falarem a verdade."

            "Que coisa..."

            jump s7_vila
        "Escada":


            $ s7_vila += 1

            scene chinatown vila_escada with Dissolve(1.0)

            "Opa... este lugar aqui eu não conheço."

            "Acho que eu até cheguei a perguntar pra [s], mas ela disse que a gente não podia ir pra lá."

            "Tô achando que é lá que eu tenho que ir. Mas não agora. Primeiro eu quero dar uma olhada melhor por aqui."

            "Eu quero o máximo de informações que eu puder sobre esta vila. Não posso deixar passar nada."

            jump s7_vila
        "Gazebo":


            $ s7_vila += 1

            scene chinatown vila_gazebo with Dissolve(1.0)

            "Este gazebo aqui... é a construção mais destacada do lugar. Dá pra ter uma boa vista da vila toda daqui."

            "Eu consigo até imaginar um mestre chinês parado ali falando pra todos os moradores em volta... quem sabe a uns 500 anos atrás."

            "Os chineses estão aqui na capital desde a fundação praticamente. Talvez esta vila seja uma das construções mais antigas do país."

            if s7_vila >= 4:

                "{i}tchec tchec{/i}"

                "Esse barulho. Tem alguém vindo! P-preciso me esconder."
            else:


                jump s7_vila

    scene black with Dissolve(1.0)

    mc surpreso "!"

    "N-não acredito!"

    scene sayuri_mestra_vila1 with Dissolve(1.0)

    pause

    "A [s]..."

    if sayuri_e4 != "fracasso":

        "E aquela é a mestra dela! Eu lembro que eu vi ela aquela vez quando levei a [s] no banho de saúde e beleza!"
    else:


        "E quem é aquela senhora com ela?"

    "A [s] não parece muito à vontade com ela... ela parece envergonhado, sei lá."

    "Tenho que fazer uma forcinha pra ouvir..."

    $ mes_nome = "Mestra"

    s "{size=17}Sim, mestra. Está indo tudo bem.{/size}"

    mes "{size=17}Você entende a importância disso, não entende? Não foi fácil assumir essa responsabilidade.{/size}"

    s "{size=17}Claro, eu entendo. A [fen] está indo muito bem.{/size}"

    mes "{size=17}E que história é essa que ela desapareceu hoje? A He Xiangu me avisou que ela voltou agora há pouco.{/size}"

    s "{size=17}P-pois é... ela tinha desaparecido. Mas bom saber que ela já está de volta.{/size}"

    mes "{size=17}Não estou sentindo firmeza nessa sua fala, [s]. Foi você quem pediu isso, não foi?{/size}"

    s "{size=17}Sim, mestra. Não se preocupe. Eu vou fazer dela aquilo que a Cidade Chinesa precisa.{/size}"

    mes "{size=17}Tenho minhas dúvidas. Quando eu treinei você, você não tinha esses problemas. Você nunca fugiu igual a ela.{/size}"

    s "{size=17}E-eu sei...{/size}"

    mes "{size=17}Se você acha que não dá conta. Eu posso ensiná-la.{/size}"

    scene sayuri_mestra_vila2 with Dissolve(1.0)

    s "{size=17}N-não! Por favor, deixa eu continuar. A [fen] está cada vez melhor. Ela tem mais talento do que eu para a ginástica.{/size}"

    mes "{size=17}Talento... sei... esse talento não custa barato, [s]. Ela não pode falhar.{/size}"

    s "{size=17}Eu sei. Ela não vai.{/size}"

    mes "{size=17}E aquele problema dela?{/size}"

    s "{size=17}Eu acho que é de toda a pressão. Talvez a saudade da família.{/size}"

    mes "{size=17}Mas é muita frescura mesmo essa menina. Se eu fosse responsável por ela, ela ia ver o que é 'saudades da família'.{/size}"

    s "{size=17}...{/size}"

    mes "{size=17}Eu quero acreditar em você, mas se ela não mostrar os resultados nas qualificatórias, terei que assumir.{/size}"

    s "{size=17}Entendido. Nós teremos ela como primeira colocada sem falta.{/size}"

    mes "{size=17}Muito bem. Agora sobre outro assunto...{/size}"

    scene sayuri_mestra_vila3 with Dissolve(1.0)

    mes "{size=17}Esse garoto que você trouxe da outra vez.{/size}"

    s "{size=17}Q-que que tem ele?{/size}"

    mes "{size=17}Como é o nome dele mesmo?{/size}"

    s "{size=17}É [mc], mestra.{/size}"

    mes "{size=17}Sim. Eu ouvi sobre ele. Parece que ele trabalha na revista da ilha.{/size}"

    s "{size=17}S-sim, mestra...{/size}"

    mes "{size=17}Ele é perigoso, [s]. Principalmente se ele estiver de conchavo com o pessoal da ilha.{/size}"

    s "{size=17}E-eu acredito que não. Ele é diferente.{/size}"

    mes "{size=17}Não vai dizer que está apaixonada por esse rapaz...{/size}"

    s "{size=17}C-claro que não, mestra. Meu foco continua no meu objetivo.{/size}"

    mes "{size=17}Acho bom. Isso será bom para você, [s]. E você sabe do seu valor para nós.{/size}"

    mes "{size=17}Em breve eu pretendo subir e quero levar você comigo.{/size}"

    s "{size=17}É o que eu mais quero, mestra.{/size}"

    mes "{size=17}Muito bem. Agora me fale sobre a rotina que você pretende usar nas qualificatórias.{/size}"

    s "{size=17}C-certo.{/size}"

    scene sayuri_mestra_vila1 with Dissolve(1.0)

    "..."

    "Essa conversa..."

    if sayuri_namoro:

        "Ela disse que não tá apaixonada por mim... mas então... por que a gente tá namorando?"

        "S-será que ela... só tá me usando?"

        "Esse aperto no peito... tô com vontade de voltar pra casa agora."

    "Elas falaram tanta coisa... nem consigo pensar em tudo. Eu não reconheço essa [s]. Parece tão fria e calculista. Tão diferente da garota meiga que eu conheci."

    "Ela sempre foi quieta... será que ela... nunca falou a verdade pra mim?"

    "Quero sair daqui. Tem alguma coisa me falando pra ir embora o mais rápido possível."

    "Deixa eu sair daqui enquanto elas tão se falando."

    scene chinatown vila_saida with Dissolve(1.0)

    "Espera! Tem um lugar que eu não vi ainda. Subindo aquelas escadas."

    "É meio arriscado ir lá agora... mas não dá pra voltar sem ver o que tem ali. Acho que eu nunca vou ter outra chance igual esta aqui."

    menu:
        "Subir as escadas até o local desconhecido":


            "Bora ver o que tem lá."

    scene chinatown vila_escada with Dissolve(1.0)

    "É subindo aqui. As escadas parece que vão até um lugar mais afastado desse centro da vila."

    "Preciso ficar esperto pra ninguém me ver subindo."

    "..."

    "Dá pra ver um portão. Parece que tem... será que é uma árvore do outro lado?"

    "Caralho. Acho que tá aberto."

    scene chinatown jardim_geral with Dissolve(1.0)

    pause

    mc surpreso "Uou..."

    "Um verdadeiro jardim oriental... olha só pra isso!"

    "Parece que tem aquelas portas de correr, igual de filme! E..."

    "{i}zum zum zum{/i}"

    "Acho que eu tô ouvindo uns sons. Acho que tem pessoas conversando."

    "Ai, caramba! Acho que eles moram aqui!"

    "Essas portas... devem ser casas ou quartos individuais, tipo hotel. Então é aqui... é aqui que a [s] e a [fen] ficam quando tão treinando."

    "Será que a mestra mora aqui também? E a mina do portal? E talvez até o Bao?"

    "Caralho caralho! Deve ter muita coisa pra descobrir aqui. Mas não dá. Eu tô com cagaço demais."

    "Preciso sair daqui. Eu sinto que vão me ver a qualquer hora. Valeu, falo-"

    "???" "Ei."

    mc angustiado "A-ah?!"

    "???" "[mc]?"

    mc "Q-quem?!"

    scene sayuri_jardim_inteira with Dissolve(1.0)

    pause

    mc angustiado "[s]!"

    s "O que você faz aqui?"

    "Fodeu! Ela me pegou!"

    mc "E-eu?!"

    s "..."

    menu:
        "Eu só vim trazer a [fen] e ela me ajudou a entrar...":


            mc desculpa "Eu encoontrei a [fen] na cidade e trouxe ela. Daí ela me ajudou a entrar aqui na vila."

            s "Ela te ajudou?"

            mc "Sim... ela me ajudou a passar pela guardiã do portão prometendo que ia ficar de olho."

            s "..."
        "Eu aproveitei que vocês tavam procurando a [fen] e entrei.":


            mc desculpa "Eu aproveitei que tava todo mundo procurando a [fen] e esperei uma chance de entrar."

            s "A [fen] então não sabe disso?"

            mc "Não... eu só aproveitei minha chance..."

    s "Mas por que você fez isso?"

    mc concentrando "Eu só queria saber mais sobre este lugar... o que acontece com você e a [fen]."

    mc desculpa "Desculpa... eu não queria invadir onde vocês moram nem nada ruim..."

    s "Isso tem alguma coisa a ver com a revista?"

    mc "Como assim com a revista?"

    s "Todo esse seu interesse é por causa dela? Pra fazer uma matéria?"

    menu:

        "Eu sou seu namorado! Eu me preocupo com você!" if sayuri_namoro:

            mc preocupado "Por que você tá pensando isso de mim? Eu sou seu namorado, não sou?! Eu não posso me preocupar com você?!"

            scene sayuri_jardim_assustada with Dissolve(1.0)

            s "É p-por isso, [mc]?"

            mc desculpa "Eu sei que não tá certo... mas eu queria saber que tava tudo bem com você."

            mc "Você sabe que tudo isso é muito estranho pra mim... eu preciso saber que você tá legal aqui."

            s "[mc]... eu falei pra você que as coisas são assim aqui. Eu preciso que você confie em mim."

            mc "Mas olha o que acontece com a [fen]! Esse treinamento todo! A menina nem pode sair daqui..."

            s "..."

        "Você é minha amiga!" if not sayuri_namoro:

            mc preocupado "Você é minha amiga, né?! Eu não posso me preocupar com você?!"

            scene sayuri_jardim_assustada with Dissolve(1.0)

            s "É p-por isso, [mc]?"

            mc desculpa "Eu sei que não tá certo... mas eu queria saber que tava tudo bem com você."

            mc "Você sabe que tudo isso é muito estranho pra mim... eu preciso saber que você tá legal aqui."

            s "[mc]... eu falei pra você que as coisas são assim aqui. Eu preciso que você confie em mim."

            mc "Mas olha o que acontece com a [fen]! Esse treinamento todo! A menina nem pode sair daqui..."

            s "..."

        "Eu tô preocupado com a [fen]." if s6_fenju_spa2:

            mc desculpa "A verdade é que eu tô preocupado com a [fen] depois de tudo o que aconteceu... eu precisava saber um pouco mais do que acontece aqui."

            s "A [fen]? Por que toda essa preocupação? Ah!"

            scene sayuri_jardim_assustada with Dissolve(1.0)

            s "P-por causa do que aconteceu no banho..."

            mc preocupado "Aquilo não foi normal, [s]..."

            s "..."
        "Sim, é pra uma matéria...":


            mc concentrando "Sim... é uma matéria. O que acontece aqui é tão diferente do que as pessoas tão acostumadas..."

            mc "Todo esse mistério, o templo, os treinamentos... tudo isso deveria ser visto pelo mundo na minha opinião."

            scene sayuri_jardim_seria with Dissolve(1.0)

            s "Então é isso? Você acha que isso aqui é só um parque de diversões?"

            mc desculpa "Eu sei que você pode pensar assim... mas não é só isso. Não é só entretenimento."

            s "Então o que é?!"

            mc serio "As pessoas precisam saber o que acontece aqui. Eu acho que tem muita coisa errada rolando e isso não pode ficar escondido."

            mc desculpa "Você sabe que eu me importo com você e agora com a [fen] também. Eu acho que vocês precisam de proteção também."

            s "[mc]..."

    scene sayuri_jardim_seria with Dissolve(1.0)

    s "Eu ainda não acredito nisso tudo... você aqui... no Lanchi Gong. Isso seria simplesmente impensável pra mim há um tempo..."

    s "Isso mostra o quanto você entrou na minha vida."

    mc desculpa "..."

    s "Desde aquela vez que a gente se viu no templo. Depois nosso passeio, você conheceu a [g]... me ajudou na loja de roupas..."

    s "E então você chegou aqui na Cidade Chinesa... primeiro foi só um passeio, lámen... e olha agora..."

    s "Você tá no coração da nossa cultura. O Jardim das Orquídeas, na língua que a gente fala neste país."

    s "É onde os escolhidos vivem. Nunca, nenhuma pessoa de fora colocou os pés aqui."

    mc envergonhado "S-sério? Caraca..."

    s "Você não entende, [mc]? A tradição diz que eu deveria chamar a He Xiangu para que eliminasse os impuros do jardim."

    "Eliminar os impuros?! Acho que eu entendi o que ela tá falando."

    s "Você entende a gravidade disso?"

    mc desculpa "Sim... Eu entendi. Eu vou embora antes que alguma coisa ruim aconteça comigo."

    mc "Adeus..."

    s "..."

    scene sayuri_jardim_triste with Dissolve(1.0)

    s "[mc]! Espera!"

    mc desculpa "?"

    s "Por que a gente não pode só continuar o que a gente tinha no começo?"

    mc "Como assim?"

    s "Você não pode esquecer o que acontece aqui? Antes de tudo isso, eu sinto que a gente se dava tão bem..."

    mc preocupado "Esquecer? Como assim esquecer, [s]?"

    if sayuri_namoro:

        mc "Eu sou seu namorado. E eu falo namorado de verdade. Não é uma brincadeira pra mim."

        mc "Onde já se viu um namorado que desconhece a parte mais importante da vida da pessoa que ele ama?"

        s "!"

        mc "Não é essa relação que eu quero com você. Não é ficar só com o passeio de final de semana. Eu quero tudo, as partes boas e as partes ruins."

        mc "Namorar não é só beijar e abraçar quando tá com vontade. É compartilhar sua vida com alguém e receber a vida dela em troca também."

        mc "É se preocupar se ela tá legal, se tem alguma coisa deixando ela triste ou preocupada. É compartilhar tudo de verdade."
    else:


        mc "É essa amizade que você quer comigo?"

    mc "Eu quero saber sobre você. Quero saber onde você mora, sobre seus sonhos e seus medos. Isso é se preocupar com alguém, entende?"

    mc desculpa "Por isso... eu não posso fechar os olhos para o que acontece aqui."

    mc "A não ser que você queira ser só uma 'conhecida', aquele tipo de pessoa que você encontra em festa só pra beber alguma coisa juntos."

    s "[mc]..."

    s "Por que... você se preocupa tanto comigo?"

    s "O que importa não é que eu sou famosa? Meu desempenho nas competições? Não é por isso que as pessoas ligam pra mim?"

    s "Por que alguém se preocuparia com o resto da minha vida? E-eu não sei o que te falar, [mc]..."

    s "O que muda na SUA vida se eu sofro ou não? Ou se a [fen] sofre? Se a gente se ver e se divertir, o que interessa o que acontece nas nossas vidas?"

    scene sayuri_jardim_mc with Dissolve(1.0)

    pause

    mc "Não sei se foi assim que trataram você sua vida toda, [s]... mas EU não vou tratar você assim."

    mc "Você é importante pra mim, e se você sofre, eu sofro também. Eu quero que você seja feliz, não só comigo, mas 'sem migo', sozinha!"

    s "Mas e se você não gostar... do que eu tenho dentro de mim? E se você achar nojento essa parte que tá... escondida?"

    mc "Pode ser... mas eu prometo que não importa o que eu ache, eu nunca vou abandonar você. Eu vou tá com você até você enjoar de mim."

    if sayuri_namoro:

        mc "Esse é o namorado que eu quero ser."
    else:


        mc "Isso que é amizade de verdade pra mim."

        if s6_declarou:

            s "Q-quando você disse no banho no outro dia... que você queria namorar comigo... você falou de verdade?"

            s "Mesmo depois de tudo, você ainda quer namorar comigo?"

            "Por enquanto eu e a [s] somos amigos, mas eu sinto algo diferente por ela. Por isso eu me declarei na banheira aquele dia."

            "Mas será que depois desse tempo eu ainda quero namorar com ela?"

            menu:
                "Sim. Quero namorar ela.":


                    $ sayuri_namoro = True

                    mc "Sim. Claro que é sério. Eu quero namorar você, com certeza."

                    s "E-eu também q-quero... faz muito tempo que eu quero."

                    mc "Isso é incrível, [s]. É muito bom saber que você sente por mim a mesma coisa que eu por você."

                    mc "Pode ter certeza que eu vou fazer o possível pra gente se dar bem e ser um verdadeiro companheiro pra você."

                    s "Ai... e-eu também, [mc]."
                "Não. Quero continuar amigo.":


                    mc "Eu pensei muito sobre isso, [s], e quero ser totalmnte sincero com você. Eu sinto um carinho muito grande por você, mas é como um amigo."

                    s "V-verdade? Amigo...?"

                    mc "Sim. Isso não muda o quanto eu gosto de você e que eu quero fazer parte da sua vida, ok?"

                    s "O-ok... Ai... eu entendo, [mc]."

                    s "O que eu sinto não muda também... você continua sendo uma pessoa muito especial pra mim, tá?"

                    mc "Que bom..."

    if sayuri_namoro:

        $ sayuri_e7 = "namoro"

        s "[mc]... eu... eu quero passar a noite com você."

        mc "C-como?!"

        s "J-já tá ficando tarde... por que você não passa a noite comigo aqui?"

        mc "N-não é perigoso, [s]?"

        s "Não importa... eu entendi o que você quis dizer. E você é meu namorado. Eu... quero dar esse passo e quero que você fique comigo hoje."

        mc "T-tudo bem... se você quer que eu fique, eu também quero."

        s "Q-que bom... eu tô nervosa, mas é o que eu quero, [mc]. Eu sinto que é isso que eu mais quero agora."

        s "Eu tô sentindo tanta coisa, mas isso é a única coisa que eu tenho certeza. Não me deixa sozinha hoje, por favor."

        mc "Claro. Eu vou ficar."

        s "T-tá... o que acha da gente ir pra lá? Vem conhecer meu quarto."

        mc "O-ok..."
    else:


        $ sayuri_e7 = "amizade"

        s "[mc]... então é assim que você pensa... você não quer me abandonar mesmo se eu fizer algo horrível?"

        mc "Olha... tem uma frase famosa que fala que a gente precisa combater a doença e não o doente."

        mc "Pra mim, você é uma pessoa boa, e mesmo que você tenha feito qualquer coisa que você ache horrível, eu vou te dar o tempo que você quiser."

        mc "Tempo pra você aprender mais sobre você e ver se você quer continuar nessa ou não."

        mc "Na vida, tudo tem consequências, mas não sou eu que vai julgar suas ações. Eu vou apoiar você, não importa o que aconteça."

        s "Entendi... mas e se na minha cabeça eu não ver problema no que eu faço?"

        mc "Depois que você se abrir comigo e eu entender tudo, daí eu posso dar minha opinião. Mas antes eu preciso que você confie em mim."

        s "T-tá... o-obrigada... você é o homem mais estranho que eu já vi na vida, [mc]."

        mc "E-estranho?"

        s "O jeito que você pensa, que você fala... eu sinto que com você eu não estou sozinha. I-isso é muito bom."

        mc "Então é um estranho bom?"

        s "Com certeza. Aliás, por que você não fica aqui esta noite? V-você poderia?"

        mc "Dormir com você aqui?!"

        s "É. Não tem perigo. Eu resolvo tudo depois. Por favor..."

        mc "C-claro... se não tem problema e você quer."

        s "Obrigada, [mc]. Vem aqui."

        mc "T-tá."

    scene chinatown jardim_porta with Dissolve(1.0)

    s "Meu quarto é este deste lado..."

    mc "Certo..."

    "Não acredito... vou dormir sozinho com a [s] no quarto dela... aqui neste jardim super secreto. Como assim?!"

    "Eu tenho minhas dúvidas que isso vai acabar bem..."

    if sayuri_namoro:

        "Merda?! O que eu tô pensando?! A gente tá namorando e ela quer 'passar a noite comigo'. Isso só pode significar uma coisa..."

        "Finalmente a gente vai..."

        "{i}gulp{/i}"

    s "[mc]? Você vem?"

    mc surpreso "Claro!"

    scene black with Dissolve(1.0)

    s "Espero que você goste."

    mc surpreso "!"

    scene sayuri_quarto_mc with Dissolve(1.0)

    pause

    mc "Caraca... eu nunca ia imaginar que tinha um quarto desses dentro dessa porta de madeira velha..."

    s "Não gostou?"

    menu:
        "Achei incrível!":


            mc "Tá brincando?! Achei incrível, [s]!"

            mc "É tudo tão perfeito e bem organizado... e tem a sua cara. Parece um quarto de filme, de verdade..."

            s "Não é pra tanto..."

            mc "Claro que é. Olha pra decoração, tudo combinando, com a mesma cor. Os vazos com as letras... caraca... incrível mesmo."

            s "O-obrigada..."
        "Eu nunca vi um quarto assim antes...":


            mc "Sendo sincero, eu nunca vi um quarto igual esse aqui antes."

            s "Isso quer dizer que é bom ou ruim?"

            mc "Bom, claro. Não sei se todo mundo iria gostar, mas ele é tão temático e especial."

            s "V-verdade..."

    mc "Então é aqui que você dorme quando tá aqui..."

    s "s-sim... eu passo a maior parte do tempo aqui por conta do treinamento. Antes era eu... agora é pra treinar a [fen]..."

    mc "Então ela mora aqui no jardim também?"

    s "Sim. Bem perto daqui. Mas ela não vai vir, não se preocupe. Não é costume um morador bater na casa do outro."

    mc "Por que?"

    s "As pessoas aqui são bem reservadas, e seu local de descanso é sagrado e muito particular."

    "Pensando nisso... o fato dela querer dividir o quarto comigo só mostra o quanto ela tá confiando em mim."

    mc "Entendi... vai ser um prazer dormir aqui hoje."

    s "E-espero que você goste... Só um segundo..."

    mc "Certo..."

    "Que nervoso que tá dando... só tem uma cama..."

    "..."

    s "Voltei. Pronto."

    if sayuri_namoro:

        s "V-você sabe por que eu te chamei..."

        mc "Sim..."

        s "S-se você quiser... o banheiro é aqui do lado. Deixei uma toalha e uma troca de roupa pra você."

        mc "T-tá..."

        s "Eu posso usar depois de você?"

        mc "Claro. Com licença..."
    else:


        s "Eu deixei uma troca de roupas pra você no banheiro."

        mc "Opa. Obrigado."

        s "Fique à vontade."

        mc "Então vou lá."

    scene black with Dissolve(1.0)

    scene quarto_chines_banheiro with Dissolve(1.0)

    if sayuri_namoro:

        "Então realmente tá acontecendo. Eu e a [s]..."

        "Quero que seja uma noite inesquecível pra ela..."

        "Tô ficando muito nervoso. Vou tomar um banho gelado pra parar de pensar."

        scene black with Dissolve(1.0)

        "Carai! Tá gelado mesmo!"
    else:


        "Que banheiro massa... aqui é tudo fino mesmo."

        "Ela deixou uma roupa pra mim aqui..."

    "..."

    scene quarto_chines_banheiro_mc with Dissolve(1.0)

    pause

    $ tempo = 3

    if sayuri_namoro:

        "Essa roupa aqui... até que eu fiquei bem nela."

        "Imagina viver aqui na Cidade Chinesa? Eu podia até virar um rei ou alguma coisa do tipo."

        "Quem sabe até assumir a barraquinha do Bao..."

        "Bom... eu tô viajando demais. Deixa eu sair pra [s] poder usar."

        scene black with Dissolve(1.0)

        mc "Say-"

        s "C-com licença..."

        mc surpreso "Opa!"

        "{i}Gatchak{/i}"

        "Eita... ela passou correndo."

        "Ela deve tá nervosa também..."

        scene quarto_chines_mc_cama with Dissolve(1.0)

        mc "Ufa... agora é só esperar ela se aprontar..."

        "Eu acho que a [s] entendeu o que eu queria passar pra ela. Mas não vai ser fácil fazer ela se abrir."

        "Bom... vou deixar isso pra outro dia. Hoje eu vou aproveitar."

        "Quero fazer a [s] esquecer de tudo isso... fazer ela se sentir muito bem esta noite."

        "E eu também vou me sentir muito bem, obviamente..."

        "..."

        "{i}Gatchak{/i}"

        s "[mc]..."

        mc "O-oi..."

        scene sayuri_quarto_pronta with Dissolve(1.0)

        pause

        s "E-eu estou pronta..."

        mc "T-tá..."

        s "Eu quero sentir que a gente finalmente está juntos. De corpo e alma."

        mc "E-eu também."

        scene sayuri_quarto_pronta_close with Dissolve(1.0)

        pause

        s "P-por favor... tenha c-cuidado comigo..."

        mc "Pode deixar..."

        "Será que ela tá nervosa? Porque eu tô muito..."

        s "Mas eu estou pronta... não quero que deixe nada de fora. Quero ser sua mulher hoje."

        mc "{i}gulp{/i}"

        mc "[s]..."

        window hide

        pause

        scene sayuri_quarto_mc_beijo with Dissolve(1.0)

        pause

        s "Ai... era isso que eu queria, [mc]..."

        mc "Você é linda, [s]..."

        s "..."

        mc "Hoje vai ser uma noite inesquecível pra gente."

        s "Eu sei..."

        window hide

        pause

        scene sayuri_quarto_mc_beijo_close with Dissolve(1.0)

        pause

        s "Pode tirar minha roupa, [mc]..."

        s "Eu quero muito isso."

        mc "Eu também."

        s "Ah..."

        mc "Você tá toda arrepiada."

        s "S-sim... é você que tá... ai... fazendo isso..."

        mc "..."

        s "V-vamos deitar?"

        mc "Claro..."

        scene black with Dissolve(1.0)

        s "[mc]..."

        scene sayuri_quarto_posando with Dissolve(2.0)

        pause

        s "Pode vir."

        "Meu Deus! Meu coração vai sair pela boca."

        "A [s] tá tão sexy assim..."

        mc "Você tá incrível, [s]... n-nem nos meus sonhos eu pensei em ver você assim."
    else:


        "Uou... até que ficou bom."

        "Vou pedir pra ela me d-"

    "{i}TOC TOC{/i}"

    if sayuri_namoro:

        s "?!"

        mc "?!"

        scene black with hpunch

        pause

        mc "O-o que houve?!"

        s "{size=17}Calma... eu apaguei a luz...{/size}"

        s "{size=17}Eu não lembro a última vez que alguém veio aqui assim... quem pode ser?{/size}"

        label say7_premium2:

            pass

        "Hmm... eu tô num momento mega quente com a Sayuri."

        "Se eu vou atender a porta agora a gente vai perder o clima e eu perco minha chance de ficar com ela!"

        "O que eu faço?!"

        menu:
            "Continuar com a Sayuri":


                if not premium:

                    call mensagem_premium from _call_mensagem_premium_49

                    jump say7_premium2

                mc "Espera... parece que pararam..."

                s "S-será?"

                mc "Eu não quero parar com você agora."

                s "[mc]? V-você?"

                mc "Deita aqui."

                scene black with dissolve

                scene say7_p5 with Dissolve(1.0)

                pause

                s "A-ah..."

                mc "A gente tava no meio da nossa noite... eu não vou perder essa chance com você."

                s "M-mas..."

                mc "Você também quer, não quer? Você que falou."

                s "É q-que... ah... ok... você tem razão..."

                s "Hoje é nossa noite, [mc]. Vem... fica comigo."

                scene black with dissolve

                scene say7_p6 with Dissolve(1.0)

                mc "Hmm..."

                s "Hmm... ah..."

                mc "É isso que eu quero, [s]. Nada vai atrapalhar a gente hoje."

                s "Ahn... tá... eu sua, [mc]..."

                s "Hmm... hoje... a gente tá sozinhos aqui... eu quero..."

                mc "?"

                s "Hm... p-por favor..."

                "Acho que ela não tem coragem de falar... mas eu sei o que elar quer."

                "Eu tô pronto pra ir pros finalmentes com a Sayuri?"

                menu:
                    "Eu tô mais que pronto.":


                        "Hoje eu não vou parar no beijo. Eu quero ir até o fim com a Sayuri."

                        mc "Sayuri... hoje eu quero você inteira..."

                        s "T-tá... aah..."

                        mc "Eu vou tirar seu quimono."

                        s "A-ah..."

                        scene say7_p7 with Dissolve(1.0)

                        pause

                        mc "Você é maravilhosa."

                        s "N-não olha desse jeito pra mim, [mc]..."

                        mc "Não precisa ter vergonha. Você é maravilhosa. E seu corpo é perfeito."

                        s "Ah..."

                        mc "Eu não vou só olhar. Eu quero experimentar você também, [s]."

                        s "Ai, [mc]..."

                        mc "Eu vou preparar você pra me receber inteiro."

                        s "M-minha... ahn..."

                        mc "Isso mesmo. Abre suas pernas que eu vou cuidar de você, gostosa."

                        scene say7_p8 with Dissolve(1.0)

                        pause

                        s "Ain, [mc]!"

                        mc "Hmm!"

                        s "Ahn! É t-tão... agnn!"

                        "A Sayuri tá tremendo... deve ser bem intenso pra ela."

                        s "N-nunca! Aahn! N-nunca eu senti assim aí! AAHN!"

                        mc "{i}slhup sllhupp{/i}"

                        s "S-se você continuar... e-eu!"

                        "Já?! Será que ela já tá chegando no limite?"

                        mc "Eu vou fazer se sentir muito bem, Say. Muito mesmo!"

                        s "Ahn! N-não aceler- aAAHN!"

                        scene say7_p9 with vpunch

                        s "AHHNGN!"

                        mc "{i}slhup slhup{/i}"

                        s "AAHNNNNN!!"

                        s "E-eu! [mc]!"

                        mc "Pode gozar gostoso, Sayuri! Goza pra mim!"

                        "É tão! Tão gosts-"

                        s "AANNNGG!"

                        scene say7_p9 with vpunch

                        s "Aah! Aahhn..."

                        mc "A gente só tá começando."

                        s "[mc]... e-eu gosto quando você... aperta minha... bunda..."

                        mc "Você gosta aqui atrás, é?"

                        s "Ahn! S-sim!"

                        "Será que a Sayuri gosta que brinquem com a bunda dela?"

                        "Eu posso me divertir bastante lá atrás também. Ou será que é demais pra mim?"

                        menu:
                            "Eu vou te pegar por trás.":


                                mc "Eu acho que eu posso te ajudar com isso..."

                                s "Ahn... p-pode?"

                                mc "Vem aqui."

                                scene black with dissolve

                                scene say7_p10 with Dissolve(1.0)

                                pause

                                s "Ai, m-minha nossa, [mc]! Anh!"

                                mc "Aqui?"

                                s "Aí! Ahnn!"

                                mc "É tão gostoso assim?"

                                s "Ah! É! Aí!"

                                mc "Você sempre teve uma bunda deliciosa, [s]... nunca imaginei que ela era sensível desse jeito."

                                s "Ela é... anng... p-por favor... aanh!"

                                mc "Tá bom?"

                                s "T-tá... não para, [mc]... mexe mais aí..."

                                mc "Eu posso fazer mais que mexer..."

                                s "M-mais?!"

                                mc "Acho que você vai gostar."

                                scene say7_p11 with Dissolve(1.0)

                                pause

                                mc "Assim?"

                                s "AAaNG!"

                                mc "{i}sllhup{/i}"

                                s "A-aannh! N-não! Aah!"

                                s "Assim! É bom, [mc]! Lambe minha b-bunda por favor! Annggh!"

                                s "Ahnn! AAh!"

                                mc "Vai gozar, é?"

                                s "Vô! V-você vai me fazer gozar!"

                                s "A-assim! Mais!"

                                mc "Tá bom. É o suficiente."

                                s "N-não!"

                                scene say7_p7 with vpunch

                                s "P-por quê?!"

                                mc "Eu quero que você guarde um pouco desse tesão pro clímax."

                                s "Ah! M-minha nossa..."

                                mc "Eu quero fazer você gozar com meu pau."

                                s "Ah... t-tá..."
                            "É minha vez agora.":


                                pass

                        mc "Agora é minha vez. Eu também quero um agrado."

                        s "C-claro... eu quero fazer isso pra você também."

                        mc "Isso, vem aqui."

                        scene black with dissolve

                        scene say7_p12 with Dissolve(1.0)

                        pause

                        mc "Assim mesmo..."

                        s "Eu n-não sei... e-eu nunca..."

                        mc "Faz devagar... usa sua mão e sua boca... bem devagar..."

                        s "S-sim..."

                        mc "Você tá indo muito bem... ah..."

                        mc "Lambe ele, [s]... desse jeito mesmo."

                        s "Hm-hmm! A-assim?"

                        mc "Incrível... você é perfeita... ah..."

                        s "O-obrigada."

                        mc "Agora coloca sua boca nele por favor. Eu quero sentir ela inteira nele."

                        scene say7_p13 with Dissolve(1.0)

                        pause

                        mc "Isso mesmo! Ahn!"

                        s "{i}slhup{/i}"

                        mc "Desse jeito, [s]! Sua boa é uma delícia!"

                        s "Nnh!"

                        mc "Hm! Aah! Assim!"

                        s "Você tá tão duro..."

                        mc "Eu tô! Porque sua boca é uma delícia!"

                        mc "Eu tô quase lá, [s]! P-para."

                        s "G-goza, [mc]!"

                        mc "N-não! Espera..."

                        s "Hm?"

                        mc "Eu quero sentir outra parte sua antes."

                        s "!!!"

                        mc "Vira."

                        scene black with dissolve

                        scene say7_p14 with Dissolve(1.0)

                        pause

                        s "[mc]..."

                        mc "Você tá pronta... e eu também."

                        s "É a-agora?"

                        mc "Sim... a gente vai finalmente fazer isso. Eu não consigo esperar mais. Você vai ser minha."

                        s "Q-quando a gente fizer isso... a gente vai ser... finalmente... um casal."

                        mc "E-exatamente. A gente vai ter dividido toda nossa intimidade. Você tá pronta?"

                        s "S-sim! Eu... eu quero muito isso, [mc]... e-eu quero ser sua hoje!"

                        menu:
                            "Eu vou ser seu também.":


                                mc "E eu vou ser seu, [s]."

                                s "A-ah... i-isso..."
                            "Isso mesmo. Você é minha.":


                                mc "Isso aí. Você vai ser minha!"

                                s "A-ah..."

                        s "Então vai... faz isso!"

                        mc "Deixa comigo!"

                        scene say7_p14 with vpunch
                    "Melhor parar aqui hoje.":


                        mc "[s]... esses beijos foram o suficiente pra mim essa noite."

                        s "V-verdade? M-mas quando a gente vai ter outra chance dessas, [mc]?"

                        mc "A gente não precisa ter pressa. Confia em mim."

                        s "M-mas..."

                "{i}TOC TOC TOC{/i}"

                s "D-de novo?!"
            "Atender a porta":


                pass

        mc serio "{size=17}Eu vou ver.{/size}"

        s "{size=17}Você?!{/size}"

        mc "{size=17}Você disse que ninguém daqui faz isso... e se for alguém de fora? Pode ser perigoso.{/size}"

        mc "{size=17}Deixa comigo.{/size}"

        s "{size=17}[mc], não!{/size}"
    else:


        s "Que estranho... alguém na porta."

        scene black with Dissolve(1.0)

        mc "Ué?"

        s "Vou ver quem é."

        mc "Tá..."

        "..."

        s "Você?!"

        mc "[s]? Tudo bem?"

        s "..."

        "Deixa eu ver quem é..."

    scene fenju_pijama_porta with Dissolve(1.0)

    fen "O-oi..."

    mc "[fen]!"

    fen "Oi, [mc]..."

    mc "O que você tá fazendo aqui?"

    fen "S-será que eu posso dormir com vocês?"

    mc "Como é?!"

    "Se a [s]-"

    s "[fen]? O que você está fazendo aqui?!"

    fen "O-oi, mestra... s-será que eu posso... dormir aí também?"

    s "Você endoidou?! Vai ago-"

    fen "..."

    s "..."

    s "Tudo bem..."

    fen "S-sério?! Você tá falando sério?!"

    s "Sim... pode entrar..."

    fen "S-será que o [mc] pode pegar o colchão da minha cama e trazer aqui?"

    s "[fen]..."

    mc "Não tem problema, [s]. Eu vou lá."

    s "..."

    fen "O-obrigada..."

    scene black with Dissolve(1.0)

    "Como que as coisas acabaram assim?"

    scene sayuri_fenju_mc_quarto with Dissolve(1.0)

    pause

    fen "O-obrigada..."

    mc "T-tudo bem, [fen]... você já agradeceu umas trinta vezes..."

    s "..."

    fen "E-eu vi você entrando bem na hora que cheguei... daí..."

    s "Não precisa se explicar. Eu entendo você querer vir aqui. Não é normal ver alguém de fora, né?"

    fen "Sim! Como que ele tá aqui?!"

    s "Eu que chamei o [mc]."

    fen "Mas e a-"

    s "Calma. A gente dá um jeito de colocar ele pra fora amanhã cedo."

    fen "Pode contar comigo!"

    mc "Valeu, garotas..."

    fen "Hihi..."

    s "Você parece de bom humor, [fen]... faz tempo que eu não te via assim."

    fen "É... ainda não tô acreditando que a gente tá aqui."

    s "'Tô'? Você tá andando muito com o [mc]..."

    fen "D-desculpa..."

    s "Tudo bem... foi bonitinho."

    fen "O-obrigada!"

    scene sayuri_fenju_quarto1 with Dissolve(1.0)

    fen "M-mestra... você parece diferente hoje..."

    s "Como assim?"

    fen "Não sei... você parece de bom humor também... Aconteceu alguma coisa?"

    if sayuri_namoro:

        s "Ah!!! N-não!! Não aconteceu nada, né, [mc]?"

        "Não aconteceu mesmo..."

        mc "Pois é..."
    else:


        s "Pode ter sido a visita do [mc]..."

        fen "Hmm..."

    s "[fen]... a gente não conversa muito... Mas eu não acho sua companhia ruim, viu?"

    fen "Tá..."

    s "Eu sei que o treinamento é puxado... mas pra mim, mais que uma discípula, você é uma amiga. Qualquer coisa que acontecer, pode contar pra mim."

    fen "Amiga?"

    scene sayuri_fenju_quarto2 with Dissolve(1.0)

    s "S-se você quiser, claro... ser minha amiga."

    fen "E-eu quero! Quero, sim!"

    s "Então tá, amiga..."

    fen "S-sayuri... eu... quer dizer, mestra..."

    s "Tudo bem. Pode me chamar de [s] se você preferir."

    fen "T-tá, [s]..."

    menu:
        "Olha só pra você duas... parecem irmãs.":


            mc "Olha só pra vocês duas..."

            scene sayuri_fenju_quarto1 with Dissolve(1.0)

            s "Que que foi?"

            mc "Parecem até irmãs..."

            fen "V-verdade?!"

            mc "Sim."

            s "Irmãs... tá falando que a gente é parecida? Isso é preconceito, [mc]."

            mc surpreso "N-não foi nesse sentido!"

            s "Haha... tô brincando, bobo."

            fen "[s]... você falou 'tô'."

            s "Ahh! Culpa de vocês."

            fen "Hihi..."
        "...":


            "Melhor ficar quieto e deixar elas conversando."

            s "Acho que a gente pode melhorar seus treinos, [fen], pra você ter mais tempo de folga."

            fen "M-mas..."

            s "Não se preocupe. Deixa que eu vou resolver tudo, tá?"

            fen "Mestra... por que?"

            s "Eu sei que as coisas não são fáceis, por isso às vezes a gente fica nervosa de vez em quando."

            s "Por isso quero que você fique mais tranquila e confie em mim."

            fen "S-sayuri..."

            s "Que foi?"

            fen "Desculpa eu ter fugido hoje... Eu vou pagar tudo o que eu tiver..."

            s "Não se preocupe. Vamos fingir que isso não aconteceu."

            fen "Sério?!"

            s "Nós somos amigas, certo?"

            fen "S-sim..."

            scene sayuri_fenju_quarto1 with Dissolve(1.0)

    s "E o [mc] vai acabar dormindo no seu colchão..."

    mc "Não tem problema."

    fen "É por minha causa... desculpa, [mc]..."

    mc "É melhor as senhoritas dormirem juntas na cama e eu fico aqui. Tá bom demais pra mim."

    s "O [mc] aceita tudo..."

    mc "Ei..."

    fen "Verdade... ele é tão bonzinho."

    mc "Tão tirando sarro de mim..."

    s "Eu não entendo como que você é desse jeito, [mc]..."

    fen "Eu também... eu nunca tinha visto um moço igual ele antes."

    mc "Tão fazendo duplinha contra mim... isso é bullying..."

    "Fen Ju e Sayuri" "Hihi..."

    scene sayuri_fenju_mc_quarto with Dissolve(1.0)

    s "O papo está bom, mas amanhã cedo a gente precisa evacuar ele sem ninguém ver."

    fen "Não vai ser fácil passar pela He Xiangu."

    s "Então vamos dormir pra pensar em alguma coisa bem cedinho."

    s "Vou apagar a luz, tá?"

    fen "Tá."

    mc "Obrigado pela ajuda, pessoal."

    scene black with Dissolve(1.0)

    s "Não se preocupe. A gente não vai deixar ela cortar você em dois."

    mc angustiado "..."

    $ dia += 1
    $ tempo = 1

    "..."

    label sayuri_e7_final:

        if carro:

            scene carro_mc_cidade1 with Dissolve(1.0)
        else:


            scene mc onibus with Dissolve(1.0)

        if not s7_continua:

            "Eu não queria causar problemas pra [fen]. A coitada já passa por várias dificuldades, agora, eu complicar ela mais ainda..."

            "Não tenho mais dúvidas de que o pessoal da Cidade Chinesa é duro demais com ela."

            "Os machucados continuam iguais e ela não tem tempo nem pra fazer o que gosta... vive com medo de tudo e tem que fugir pra ver a cidade."

            "Eu não sei o que a [s] e esse povo tem na cabeça."

            "Eu não vou ficar julgando a [s] demais. Não sou eu que tenho que fazer isso."

            if sayuri_namoro:

                "Além do mais, a gente tá namorando e eu quero ficar do lado dela. Eu vou acreditar nela e ser o apoio que ela precisa."

            "Quando eu tiver uma chance eu vou conversar direito com ela e pedir explicações de tudo..."
        else:


            "Ufa... cheguei são e salvo no busão. A [s] e a [fen] trabalhando juntas pra enganar a moça do portal foi demais haha..."

            "Caraca... nem acredito que aconteceu tudo isso em um dia..."

            "Encontrar a [fen] andando pela cidade, descobrir que ela faz ballet, depois invadir a vila secreta..."

            "Aquela conversa da [s] com a mestra dela... eu preciso tentar me lembrar bem do que elas falaram. Parecia algo bem importante."

            "E aquela conversa da gente no jardim... eu não sei direito o que pensar sobre isso."

            if sayuri_e7 == "namoro":

                "E depois aquele lance quente com a [s] no quarto... caraca... eu fico com tesão só de lembrar."

                mc "E depois a [fen] chegou... fala sério."
            else:


                "E eu acabei dormindo lá e a [fen] chegou depois... foi uma noite divertida."

            "Mas elas até que se dão bem... sei lá... o encontro delas não foi o que eu esperava."

            "Eu acho que tem mais nessa relação do que eu tô imaginando. Elas pareciam tão ligadas juntas..."

        "Eu conheci também aquela [sh] do ballet. É uma garota interessante... tomara que ela seja maior de idade..."

        "D-digo... quero dizer... não que eu tenha segundas intenções. Mas, né?"

        "Seja como for, eu tô ansioso pra entender de uma vez por todas o que a [s] e a [fen] tão vivendo."

        "Não posso deixar passar da próxima vez que eu ver elas. Preciso ter uma conversa de verdade com a [s]."

        "E se a Cidade Chinesa tiver mesmo pressionando as duas a esse ponto, eu quero fazer alguma coisa sobre isso."

        "Hoje em dia eu sei que eu tenho minhas armas também. E se aquela 'mestra' e os outros acham que eu não posso fazer nada, eles tão muito errados."

        "[mc]... o paparazzo que derrotou os opressores... já consigo imaginar o título do livro..."



    scene black with Dissolve(3.0)

    $ tempo = 4

    $ v32_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v32_fim","final","local")







    call checa_final from _call_checa_final_9

    jump call_cidade

label sayuri_evento8:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s8_save", extra_info="s8_save")

    $ estou_na_cidade = False

    $ sayuri_e8 = "evento"

    scene black with Dissolve(2.0)

    scene sayuri_quarto with Dissolve(1.0)

    label say8_premium2:

        pass

    menu:
        "O que será que a [s] tá pensando?":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_50

                jump say8_premium2

            "???" "AAAGH!!"

            scene say7_p15 with vpunch

            s "Não acredito!!!"

            s "Dessa vez eu tava tão perto!"

            s "A gente tava se pegando na cama! A gente... fez tanta coisa... safada..."

            s "Até aquela maldita pirralha aparecer! Ai que ódio!"

            "Eu queria tanto ter ido até o fim com o [mc]..."

            "Quando eu vou ter outra cha-"

            "{i}toc toc{/i}"

            "???" "Mana? Tudo bem?"

            scene black with dissolve

            scene say7_p16 with Dissolve(1.0)

            s "O que você tá fazendo aqui?!"

            g "D-desculpa... eu escutei sua voz... fiquei preocupada."

            s "A-ah... pensei que eu tivesse sozinha essa hora."

            g "É... só tá eu aqui."

            s "Ah..."

            g "Quer contar o que aconteceu? Você parecia bem... brava, sei lá..."

            menu:
                "Hmm... ok...":


                    s "Hmm... eu sempre te contei as coisas... acho que tudo bem falar disso também..."

                    s "É a-algo bem... pessoal... íntimo..."

                    g "Entendi... deixa eu deitar aí e você me conta..."

                    s "T-tá..."

                    scene black with dissolve

                    scene say7_p17 with Dissolve(1.0)

                    g "Conta pra mim, mana..."

                    s "M-melhor eu me tr-"

                    g "Não precisa... a porta tá fechada e só tá nós aqui. Vai ser rapidinho."

                    s "Que seja... eu tô estressada demais."

                    g "Isso. Só fala."

                    s "Sabe o... [mc], né?"

                    g "Claro. Aquele babaca."

                    s "J-júlia! A gente tá... sabe..."

                    g "Sei..."

                    s "Então, a gente... fez... aquilo..."

                    g "Não acredito! Sério?!"

                    s "Então... não dá pra explicar, ele apareceu lá na vila e tinha que ficar lá pra não ser pego..."

                    s "Daí as coisas foram acontecendo... eu tava com tanta vontade... mas... a gente teve que parar!"

                    g "Hmm... então você tá na vontade até agora..."

                    s "S-... ah... s-sim... eu... a gente tava quase... daí... aah! Que droga!"

                    g "Mana... eu sei como é essa frustração... é a pior do mundo..."

                    scene say7_p18 with Dissolve(1.0)

                    g "hm... eu sei como resolver isso."

                    s "Hmm... o que você tá fazendo, [g]?!"

                    g "Eu sei... {i}smack{/i}... é horrível, né?"

                    s "Muito... hmm... é... hmm... J-júlia..."

                    g "Eu vou te ajudar, mana... ah... uhum..."

                    s "N-não... e-eu sei onde... hmm... esses b-beij- hmm... ah..."

                    g "Vai piorar antes de melhorar... hmm... uhum..."

                    "Os beijos da [g] tão fazendo aquele calor voltar... e-eu não posso continuar com isso."

                    "Eu tô com tanta vontade agora... e ela tá fazendo eu sentir tudo aquilo de novo ah..."

                    "E-eu... se eu deixar isso continuar... do jeito que eu tô... onde vai parar?"

                    menu:
                        "Vamos parar agora!":


                            s "Chega, [g]! E-eu não posso."

                            g "Mana... vai melhorar... você vai ver."

                            s "N-não! Isso não tá certo! Por favor!"

                            g "M-mas!"

                            s "SAI!"

                            scene black with vpunch

                            g "A-ai... ok... sua chata... fica com isso aí então."

                            s "E-eu vou dar meu jeito... tchau..."

                            g "Mhpf..."
                        "N-não consigo... eu preciso":


                            "Eu não sei mais o que eu tô fazendo... mas os beijos dela... são tão bons..."

                            "Só mais um pouco... daí eu paro com tudo... só uns beijos..."

                            s "[g]... ah... hmm..."

                            g "Isso, mana... é bom... sua boca é boa... logo vai passar..."

                            s "T-tá... m-me ajuda..."

                            g "Vem aqui."

                            scene say7_p19 with Dissolve(1.0)

                            g "Eu vou cuidar de você, mana. Só aceita meu beijo."

                            "Ela tá no meio das minhas pernas... sem roupa..."

                            "A [g] tá tão quente... esfregando em mim..."

                            s "Ah! V-você tá."

                            g "Xii... só me beija, mana. Põe a língua na minha boca."

                            g "Sente meu corpo no meio das suas pernas."

                            s "A-ah! I-isso..."

                            "Eu não consigo mais pensar... eu tô voando... a [g]... o que eu faço?"

                            g "Sente gostoso!"

                            s "Ahn... [g]..."

                            g "Eu tô só começando, mana. Hoje eu vou sentir você inteirinha!"

                            s "E-eu..."

                            "Me sentir inteira? O que ela... não... isso não tá certo!"

                            "Mas é tão gostoso..."

                            scene say7_p20 with Dissolve(1.0)

                            pause

                            s "A-aah!"

                            g "Você tá toda arrepiada! Minha língua é tão gostosa assim?!"

                            g "Ou será que é eu apertando seu peito, hm?!"

                            s "[g]! Aahnn!"

                            "Tão gostoso, ela faz tão firme! Meu corpo tá..."

                            s "Ain! C-cuidado!"

                            g "Você vai gostar, mana! Bem forte! Eu sei!"

                            s "Aahn!"

                            g "Sente minha coxa esfregando em você! Eu tô sentindo você ficando molhada!"

                            "O jeito que ela fala! É tão.. mas me deixa mais louca ainda!"

                            s "S-sim! T-tô sentindo!"

                            g "Você não vai aguentar muito desse jeito... deixa eu pegar você de jeito."

                            scene say7_p21 with Dissolve(1.0)

                            pause

                            s "Minha nossa, [g]! AAhh!"

                            g "Você tá pronta, mana!"

                            s "O-onde você tá colocando e-es- AAH!"

                            g "Eu sei que você gosta lá atrás também! Eu escutei!"

                            s "V-você escut- AAH!"

                            g "Sim! Sente meus dedos entrando você! É gostoso, não é?!"

                            "É muito gostoso! Enfiando na minha buceta! Na minha bunda também!"

                            "Isso é tão errado, mas é tão bom!"

                            s "S-se conti-"

                            scene say7_p22 with Dissolve(1.0)

                            g "Isso! Pode gozar!"

                            s "A-ahn!"

                            g "Sente meus dedos nos seus dois buraquinhos!"

                            s "N-não! S-se... aahhnn! A-aahn! AAHN!"

                            g "Goza, mana!"

                            s "J-j-[g]! AAIHN!"

                            scene say7_p22 with vpunch

                            g "Isso! Assim!"

                            "Minha nossa! O que é isso?! Tão!"

                            s "AAHNNN!"

                            g "Intenso, hein?"

                            s "Ah..."

                            s "{i}puf puf{/i}"

                            "Esse foi meu... primeiro orgasmo com alguém..."

                            "Eu queria que tivesse sido com o [mc]... mas a [g]... minha nossa..."

                            "Ela fez eu me sentir tão gostoso... eu queria que ela também sentisse..."

                            s "[g]... eu quero que você sinta também."

                            g "S-sério, mana? N-não precisa..."

                            s "Eu quero. O q-que eu faço?"

                            g "Você pode... me lamber?"

                            s "E-eu..."

                            g "Deita aqui... eu vou guiar você."

                            s "Tá..."

                            scene black with dissolve

                            scene say7_p23 with Dissolve(1.0)

                            pause

                            g "Hmm... isso.. com a língua..."

                            "Não acredito que eu tô fazendo isso com a [g]... mas ela merece..."

                            g "Tão gostoso, mana... nem nos meus sonhos eu... hmm..."

                            s "Q-que bom..."

                            g "É gostoso ouvir você falando. Fala mais."

                            s "E-eu..."

                            g "Você tá gostando da minha buceta?"

                            s "S-sim..."

                            g "Que bom! Então chupa ela!"

                            scene say7_p24 with Dissolve(1.0)

                            s "Hmm!"

                            g "Assim! Mais forte! Enfia a boca nela!"

                            s "HM-hm!!!"

                            g "Você vai aguentar, mana! Chupa com força!"

                            s "{i}SHLUP{/i}"

                            g "Assim! AHN!"

                            g "Deixa eu abusar de você!"

                            s "Hm-hmm!"

                            scene say7_p25 with Dissolve(1.0)

                            g "Deixa eu abusar de você mais!"

                            s "NNHG!"

                            g "Dói mais é gostoso, mana! Eu adoro usar você!"

                            "A [g] tá beliscando!"

                            "Não sei porque, mas tá me dando vontade de sentir de novo!"

                            g "Continua me chupando! Eu tô quase lá!"

                            s "Ahn!"

                            g "Você tá se tocando também, safada?!"

                            s "!!!"

                            scene say7_p26 with Dissolve(1.0)

                            g "Não acredito! Você é uma safada!"

                            s "Ahnn!"

                            g "Não para de lamber! Você vai sentir eu chegar lá na sua boca!"

                            "Quando a [g] abusa de mim! Eu sinto!"

                            s "HMM!"

                            g "Vamo gozar, mana! Continua!"

                            s "Hm! HMM! AAHNN!"

                            g "NNNHNGGG! PORRA!"

                            scene say7_p26 with vpunch

                            g "ISSO! TÔ GOZANDO, VACAA!!"

                            s "AAhnn!"

                            g "Delícia... preciso deitar. Vem aqui."

                            scene black with Dissolve(2.0)

                            scene say7_p27 with Dissolve(1.0)

                            pause

                            g "Foi incrível, mana..."

                            s "[g]... minha nossa... o que a gente fez?"

                            g "Fez uma delícia..."

                            s "Isso... eu me deixei levar..."

                            g "O sentimento de culpa depois do prazer... você vai se acostumar com isso logo logo."

                            s "Ah... e-eu..."

                            g "Imagina viver sem isso? Você vai querer de novo... eu tenho certeza."

                            g "E eu vou te satisfazer de novo, mana... sempre..."

                            s "[g]..."

                            g "Posso voltar no seu quarto amanha?"

                            s "!"

                            "Eu sei muito bem o que ela quer dizer..."

                            menu:
                                "De jeito nenhum.":


                                    s "Nem pense nisso."

                                    g "Q-quê?!"

                                    s "Eu tive uma recaída... mas agora eu aprendi. Eu não quero fazer isso de novo."

                                    g "Você não gostou?"

                                    s "Isso não importa. Eu quero ter um amante, mas não quero que seja você."

                                    s "Eu sou sua irmã... sua amiga... não sua parceira de cama."

                                    g "Mas você pode ser!"

                                    s "[g]... eu sei que às vezes a gente pode se perder nos sentimentos..."

                                    s "Mas a gente precisa colocar os dois pés no chão. Precisamos tomar a decisão que sabemos ser a melhor."

                                    s "Mesmo que isso não seja o mais prazeroso no curto prazo. Temos que ser responsáveis."

                                    s "Eu gosto muito de você. Mas não assim. Espero que você entenda."

                                    g "Você é sem graça, mana..."

                                    s "Hehe..."

                                    g "Ok, boba... mas não me abandona."

                                    s "Nunca."
                                "Pode...":


                                    s "Pode... eu vou... deixar a porta aberta."

                                    g "Perfeito."

                                    p "Eu tenho certeza que você vai adorar."

                                    s "Não sei..."

                                    g "Agora eu vou sair. Amanhã eu volto. Se prepara pra mim."

                                    s "T-tá..."

                                    scene black with dissolve

                                    "A [g] não esperou o próximo dia..."

                                    "Naquele dia à noite ela voltou... tava sem roupa... e a gente fez de novo."

                                    "E no outro dia... e no outro... e duas vezes no próximo... e no próximo..."

                                    scene say7_p28 with Dissolve(2.0)

                                    pause

                                    "Quando eu percebi... eu ficava na cama esperando a [g] voltar."

                                    "Eu nem ligava mais a luz e nem saía do quarto... ela me trazia tudo."

                                    "Eu dormia e esperava ela me acordar pra me usar."

                                    "Ela fazia o que queria comigo e as coisas só foram aumentando."

                                    "Era terrível..."

                                    "Mas extremamente delicioso..."

                                    "Esperar a [g] pra sentir aquele prazer de novo era a minha razão agora."

                                    "O que tinha acontecido com os outros? Com meus pais? Com o [mc]?"

                                    "E daí?"

                                    "Será que a [g] ia aparecer de novo hoje?"

                                    scene black with Dissolve(3.0)

                                    pause

                                    $ renpy.vibrate(1)

                                    scene say7_p29 with vpunch

                                    s "AAH!"

                                    s "Q-que foi isso!?"

                                    s "Um sonho... um... pesadelo?"

                                    "Então nada daquilo aconteceu?! Eu não sei... quando eu dormi."

                                    "Mas eu não enlouqueci... que bom... ufa..."

                                    "Isso só pode ser um sinal... eu e a [g] não podemos nos perder..."

                                    "Não podemos confundir as coisas que a gente sente uma pela outra."

                                    "Nós somos amigas, irmãs de coração... não amantes!"

                                    "Eu preciso ajudar ela com o que ela precisa, que é uma irmã que dê um chão pra ela."

                                    "Não alguém que abuse dos problemas dela pra se sentir bem..."

                                    "Eu preciso ser adulta... e entender meus sentimentos também."

                                    "Ainda tem tempo..."
                "É coisa pessoal. Pode ir.":


                    s "É coisa minha, [g]... pode deixar."

                    g "Certeza? Eu posso-"

                    s "Eu prefiro que você saia. Eu tô sem roupa."

                    g "Mas, mana..."

                    s "Por favor, [g]..."

                    g "Ok..."

            scene black with Dissolve(1.0)

            "Eu preciso ligar pro [mc]."

            "Eu quero ver ele de novo... o mais rápido possível."
        "Deixa pra lá":


            scene black with Dissolve(1.0)

    $ renpy.vibrate(1)

    play sound "audio/som_3_celular.mp3"

    "Smartphone" "Trr... trrr..."

    mc normal "É o número da [s]. Oi!"

    s "Oi, [mc]... T-tudo bem?"

    if sayuri_namoro:

        mc charmoso "Tudo bem, gata."

        s "G-g-ga..."

        mc desconfiado "Gagá?"

        s "N-nada..."
    else:


        mc normal "Tudo sim. E você?"

        s "Que bom. Eu também."

    scene ape_celular_falando with Dissolve(1.0)

    if sayuri_e7 == "namoro" or sayuri_e7 == "amizade":

        s "Estou com s-saudades... depois daquela noite que você passou aqui."

        mc "Eu também..."

        s "Foi muito divertida nossa conversa. E acabou ajudando bastante, sabia?"

        mc "Com o quê?"

        s "Eu e a [fen] conseguimos ter um tempo legal juntas... graças a você."

        mc "Que bom. Mas não foi nada de mais, a gente só conversou, né?"

        s "E-eu sei! Mas é que... nós duas nunca tínhamos conversado desse jeito... a gente nunca tinha rido juntas."

        mc "Puxa, [s]..."

        s "Depois daquela noite a gente conseguiu se falar outras vezes. Eu sinto que as coisas tão mudando."

        mc "Isso é muito bom."

    s "E-eu liguei pra te convidar pra uma coisa..."

    s "É que agora que eu e a [fen] estamos tentando conversar mais... eu chamei ela pra vir na minha casa."

    mc "Sério?!"

    s "É... ela reclama que fica só na área de treino... daí eu consegui arrumar pra eu passar o dia com ela na minha casa no centro."

    mc "Que bom! Ela vai adorar!"

    s "Também achei. E ela pareceu empolgada. E-ela nem acreditou na hora que eu falei."

    mc "Que bonitinha... ela deve tá louca pra conhecer aí."

    s "Daí... eu tava pensando... é..."

    menu:
        "Que foi?":


            mc "Que foi?"

            s "Ah! É..."
        "...":


            "..."

            s "É..."

            mc "..."

    s "S-será que você não quer... vir aqui com a gente?"

    mc "Ir na sua casa você tá falando?"

    s "I-isso! A [fen] gosta de você. Ela vive falando seu nome quando a gente conversa."

    mc "Haha..."

    s "Eu acho... que ia ser legal pra ela. O q-que você acha?"

    "Passar o dia na casa da [s] com as duas..."

    menu:
        "Você gostaria que eu fosse?":


            mc "Você ia gostar se eu fosse? Por você eu digo."

            s "E-eu?! Eu..."

            s "Eu ia gostar, sim. Eu gosto de passar tempo com você, [mc]. Q-quer dizer... v-você entendeu!"

            mc "Acho que eu entendi, sim."

            mc "Se você é à favor e quer que eu participe, então pode contar que eu vou."

            s "Obrigada, [mc]! Eu sempre posso contar com você! Igual um h-herói..."

            mc "Não exagere haha..."
        "Se é pra ajudar a [fen] eu gostaria de ir.":


            mc "Se você acha que isso vai ajudar a [fen], então pode contar comigo."

            s "Eu tenho medo que ela se sinta meio fora de casa... com você lá acho que ela vai ficar melhor."

            mc "Ok. Se é assim, então eu vou com certeza."

            s "Ufa... ela vê você como um amigo. Ela vai adorar."

    s "Então eu tô esperando você aqui. Você lembra o endereço de casa, né?"

    mc "Sim. Eu lembro ainda."

    if sayuri_namoro:

        s "Então eu tô te esperando... B-b-beijo!"

        mc "Um beijo pra minha gata."

        s "!"

        "{i}Tu tu tu-{/i}"

        "Essa [s]... eu sinto que ela tá melhorando, mas acho que ainda é a pessoa mais tímida que eu já vi."
    else:


        s "Até daqui a pouco."

        mc "Até. A gente já se vê."

        s "Tá."

        "{i}Tu tu tu...{/i}"

    scene ape_pensando with Dissolve(1.0)

    "Hmm... {w}Passar um dia com a [s] e a [fen]..."

    "Se eu posso ajudar na relação delas, não tenho por que não ir. Elas precisam te toda ajuda que puderem arranjar."

    "Eu sei que a menina tem uma vida difícil lá. Eu sei que a [s] também vive uma situação delicada."

    "Nem sei mais quantas vezes eu pensei nessa história da Cidade Chinesa."

    "Quanto mais eu conheço sobre o que acontece lá, mas eu fico na dúvida se eles são horríveis ou eu que não entendo..."

    "Eu sei que não tá certo uma garota ter que fugir pra fazer uma aula que ela quer."

    "Mas também eu não faço ideia de como é pesado o treinamento de outros atletas olímpicos. Será que todos passam por isso?"

    "Chegar ao topo de alguma coisa... ser quase perfeito naquilo que você quer ser bom... com certeza não é fácil."

    "Até que ponto se matar por um objetivo ainda é certo? Será que dá pra dividir isso em certo ou errado?"

    "E se chegar uma hora que eu tenha que decidir se vou ou não denunciar o que acontece com ela?"

    "A [fen] tá sempre com aqueles machucados... e eles parecem que eles nunca melhoram!"

    if s6_fenju_spa2:

        "Depois daquele dia no spa acho que eu tenho uma boa ideia do que acontece com ela..."

    "Além de que ela tá afastada da família... eu fico incomodado só de pensar."

    "Tem que ter alguma coisa que eu posso fazer... mas e a [s]? Como ela vai ficar se eu decidir fazer alguma coisa?"

    "Com a revista eu posso expor pra todo mundo o que rola lá. Mas com certeza isso vai acabar com muita coisa."

    "A [s] vai... certeza que ela vai ficar muito decepcionada comigo..."

    "O que eu faria se tivesse que escolher?"

    "Bom... {w}Não adianta pensar nisso agora. Melhor eu me preparar pra sair."

    scene black with dissolve

    "..."

    call locomocao from _call_locomocao_12

    "..."

    scene black with dissolve

    "A casa dela era por aqui..."

    "Achei!"

    scene casa_sayuri with Dissolve(2.0)

    pause

    "Continua a mesma coisa. Esse bairro parece bem tranquilo."

    "Por que será que a [s] e a família dela não moram na Cidade Chinesa?{w} Será que tem alguma coisa com a [g]?"

    "Bom... tomara que eu não tenha demorado demais."

    "{i}Ding dong{/i}"

    s "[mc]. Bom dia."

    mc "Oi, [s]."

    s "Pode entrar, por favor."

    mc "Licença."

    scene s8_sayuri1 with Dissolve(1.0)

    pause

    s "Faz um tempo que você não vinha, né?"

    if praia_sayuri_local:

        mc charmoso "Eu passei aquela vez pra deixar um biquíni pra gente ir na praia, mas não entrei."

        s "Verdade... Antes disso..."

    mc "Eu vim aquela vez pra assistir a entrega do seu prêmio, lembra?"

    if j2_sayuri_traida:

        s "Eu lembro que eu fiquei bem triste com você porque você veio aqui sem me falar."

        mc desculpa "Eu lembro... desculpa..."

        s "Tudo bem. Isso passou."
    else:


        s "Tem razão. Eu fiquei feliz por você e a [g] terem visto."

    mc charmoso "Eu achei super massa você ter sido chamada. Apareceu na TV e tudo."

    s "V-verdade..."

    "A [s] ainda parece nervosa quando a gente conversa. Eu sinto que sempre que ela fala dela, ela fica assim."

    menu:
        "Reparar nas mãos dela":


            "Hmm..."

            show s8_sayuri2 with Dissolve(1.0)

            pause

            "Só de olhar dá pra ver como ela tá nervosa com o que vai rolar hoje."

            "Esse negócio de ficar mexendo nas unhas... isso aí é sinal de que ela tá ansiosa."

            "Pelo menos tá tudo bem feitinha. Ela não deve ficar roendo."

            window hide

            pause

            hide s8_sayuri2 with Dissolve(1.0)
        "Continuar olhando nos olhos":


            "Bom, acho que isso vai passar. Ela precisa de mais confiança, só isso."

            "Não sou eu que tenho que ficar reparando nisso. Minha tarefa é ajudar ela no que der."

    mc "E o que você tá pensando pra hoje?"

    scene s8_sayuri3 with Dissolve(1.0)

    s "Ah... só um encontro normal. Uma conversa casual com ela, você... você acha ruim?"

    mc "Eu?"

    menu:
        "Não seria melhor ir em algum lugar?":


            mc envergonhado "Assim... ela é adolescente, né? Será que não era melhor a gente fazer alguma coisa?"

            s "Você diz como?"

            mc normal "Sei lá, ir no cinema ou em algum parque ou até no fliperama que tem no centro."

            s "Entendi... mas não sei se seria bom nesse caso."

            s "Eu não sou psicóloga, então não sei como funciona exatamente, mas eu queria reforçar nosso laço, sabe?"

            s "Não queria só levar ela em um lugar e deixar ela brincando. Queria realmente me aproximar."

            mc charmoso "Entendi. Isso é muito legal, [s]."
        "Eu acho que tá de bom tamanho.":


            mc charmoso "Eu acho que se o objetivo é vocês se aproximarem, uma coisa assim mais pessoal é melhor."

            s "Você acha mesmo?"

            mc normal "Sim. Porque aqui vocês vão realmente curtir uma a outra. Vão conversar e tudo."

            s "Foi isso que eu pensei também."

    s "Eu e a [fen] só se conhece do ambiente de treino. A gente não tem uma 'amizade' ou nada assim."

    if sayuri_e7 == "namoro" or sayuri_e7 == "amizade":

        s "Naquela noite que você passou na Vila dos Escolhidos, eu sinto que alguma coisa mudou entre a gente."

        s "Como se alguma chavinha tivesse ligado da minha cabeça."

        mc desconfiado "Por que será?"

        s "Não sei... mas eu olhei pra ela de outro jeito."

    scene s8_sayuri4 with Dissolve(1.0)

    pause

    s "Nossa relação nunca foi fácil. Eu sou a mestra dela e ela é minha discípula. A [fen] é minha resposabilidade."

    s "E o peso de ter a próxima revelação da ginástica nas minhas mãos... acho que isso mexeu comigo."

    mc "Os treinamentos com a [fen] sempre foram puxados, né? Eu lembro lá do templo."

    if s5_rigida:

        mc desculpa "Desculpa ser intrometido, mas eu vi o jeito que você falou com ela lá..."

        s "Ah! Eu... eu não queria que você tivesse visto aquilo, [mc]... me desculpa..."

        mc "Eu fiquei assustado com seu jeito lá. Eu nunca tinha imaginado..."

        s "E-eu nunca ia querer te assustar... é que..."

    mc "A [fen]... dá pra ver no jeito dela que os treinos são difíceis. Ela tá sempre assustada, miudinha..."

    mc "E aqueles machucados, [s]..."

    s "[mc]... lembra que a gente conversou na Cidade Chinesa?"

    if sayuri_adeus:

        mc "Sim. Eu lembro de ter falado que não ia aceitar o que vocês faziam."

        s "Eu sei..."

        if s6_mudanca:

            mc "Depois eu mudei de ideia. Depois daquele nosso passeio pelo lugar proibido, eu mudei."

            s "Eu fiquei muito feliz com isso."

    s "As coisas não são fáceis pra gente. Com certeza não é fácil pra [fen], mas não é pra mim também."

    mc serio "Eu imagino... mas não posso só aceitar isso, entende? Isso não tá certo, [s]."

    mc desculpa "Não dá pra saber até que ponto eu tenho que respeitar sua cultura, quando ela faz isso com uma criança!"

    if s5_ajudou:

        mc "Teve aquela vez que ela passou o dia todo comigo... ela disse cada coisa que me deixou sem saber o que pensar."

        s "..."

    s "Eu sei que não é fácil de entender. Eu sei..."

    if sayuri_namoro:

        mc "Você é minha namorada. Eu gosto tanto de você, [s]... mas tudo isso me preocupa muito. Eu quero fazer a coisa certa."


    s "Você é um homem incrível, [mc]. Você é uma pessoa de bem, honesta... e-eu imagino como tudo isso deve deixar você maluco."

    mc concentrando "Não sei se eu sou tão honesto... mas eu fico louco com isso, de verdade..."

    mc "Não sei quantas vezes eu já me peguei pensando em tudo isso. O que é certo... o que é errado..."

    scene s8_sayuri3 with Dissolve(1.0)

    s "Mas agora chega, [mc]. Eu quero mudar tudo isso, entendeu?"

    s "Eu nunca entendi a [fen]. Esse foi um dos nossos maiores problemas."

    menu:
        "Como assim não entendeu?":


            mc "Como assim? O que você não entendeu?"

            s "A [fen]... ela... sempre foi muito diferente de mim."

            s "Quando eu tinha a idade dela, eu obedecia minha mestra em tudo o que ela requisitava. Totalmente diferente."

            s "Eu sabia que ela queria que eu aprendesse e fosse a melhor versão de mim mesma. A melhor atleta possível."

            s "A [fen] não entende isso. Ela discorsa e vai contra o que eu digo. Ela foge, desaparece, se recusa a colaborar."

            s "Eu nem imagino o que minha mestra faria com uma garota igual ela... isso é..."

            s "Sinceramente, a-acho que nunca vi uma garota teimosa igual a [fen] em toda minha vida."

            mc "Então ela é fogo desse jeito..."
        "Você era a responsável. Tinha que entender!":


            mc serio "Mas, [s]. Você é a responsável por ela. Além de que você é a adulta da relação. Você tinha que entender!"

            s "Eu sei... eu errei nisso... me p-perdoa, [mc]."

            mc desculpa "Não é pra mim que vocÊ tem que pedir perdão..."

    s "Eu sempre fui bater de frente com ela. Eu tinha que usar o que eu tinha aprendido com a mestra. Deu certo comigo."

    s "Só que vendo você e ela juntos... eu entendi uma coisa..."

    mc desconfiado "..."

    s "Cada criança é diferente. Assim como cada pessoa, no geral, é diferente. Não adianta querer ensinar todas do mesmo jeito."

    s "Enquanto eu tratar a [fen] igual a minha mestra me tratou, a gente nunca vai avançar em nada."

    scene s8_sayuri4 with Dissolve(1.0)

    s "Eu preciso esquecer o que eu passei, preciso me livrar de tudo o que eu lembro de ruim do meu treinamento..."

    s "É o único jeito. Eu tenho que virar a professora que a [fen] precisa e não exigir que ela seja a aluna que eu quero."

    s "É só desse jeito que eu vou ensinar ela o que ela precisa saber..."

    mc "Isso parece incrível, [s]. Eu... eu torço pra que dê certo."

    mc "Eu nem imagino o que você passou no seu treinamento, mas se você percebeu que a [fen] é diferente, então é isso mesmo."

    mc "Ela tá machucada. Por dentro e por fora. E, por mais que eu queira proteger ela, só você pode fazer isso."

    s "E-eu sei... e é o q-que eu quero, [mc]..."

    s "Eu já fiz muitas coisas diferentes da minha mestra. Principalmente nos castigos físicos..."

    s "Não quero nem lembrar como era. E eu nunca levantei uma mão pra [fen]."

    "Nunca levantou uma mão?"

    if s6_fenju_spa2:

        "E aquele soco lá no spa da vila proibida?"

    "E todas as feridas que a [fen] sempre carrega? A [s] acha que eu sou cego?"

    mc "Você... pode falar a verdade pra mim, [s]."

    s "Eu s-sempre quero falar a verdade pra você, [mc]. Mas nem sempre eu... t-tenho coragem..."

    "Eu não entendo a [s]. Às vezes ela parece tão verdadeira e meiga... mas também às vezes..."

    "Será que ela tá sendo sincera agora? {w}Eu quero que ela confie em mim e me fale tudo. Não esconda de mim as coisas."

    menu:
        "Dar um beijo no rosto dela":


            "Eu acho que assim ela vai saber que eu tô do lado dela."

            if sayuri_namoro:

                "E não só como amigo, mas como namorado e parceiro também."

            mc "[s]..."

            s "Hm?"

            scene black with dissolve

            scene s8_sayuri6 with Dissolve(1.0)

            pause

            s "[mc]!"

            mc "Eu quero que você confie em mim."

            if sayuri_namoro:

                mc "Eu não sou só um amigo e alguém que quer que você seja feliz. Eu sou seu namorado também."

                mc "Vou tá sempre do seu lado, sempre que você precisar, tá?"

            mc "Eu acredito no que você tá falando... Que você quer fazer a coisa certa com a [fen]."

            mc "Pode sempre me falar tudo. Toda a verdade. Eu não vou te julgar."
        "Você precisa fazer o que é certo.":


            mc "Eu sei que a gente passou pelas nossas merdas quando a gente era menor. E alguns passam muito mais que outros."

            mc "Eu não vou querer falar aqui que eu e você tivemos as mesmas oportunidades. Isso aí é ridículo."

            mc "Olhando pra como a gente cresceu, é fácil ver que não é a mesma coisa."

            scene s8_sayuri7 with Dissolve(1.0)

            mc "Mas, mesmo assim, eu quero acreditar que você vai fazer a coisa certa."

            mc "A gente não é perfeito. Todo mundo faz suas cagadas aqui e ali. Eu também. Mas tem um limite, sabe?"

            mc "Por isso eu quero acreditar que você vai fazer o que é ético no caso da [fen]."

            mc "Que ela não vai mais aparecer com esses machucados e mais feliz, sorrindo e confiante."

            s "Eu... eu quero isso também..."
        "Eu vou tá sempre do seu lado.":


            mc "O que eu acho é que só você sabe o que você passou e o que você passa."

            mc "É muito fácil pros outros olhar de fora e falar que tem coisa errada acontecendo sem entender a história."

            scene s8_sayuri7 with Dissolve(1.0)

            mc "Eu não quero te julgar. E também vou tá sempre do seu lado, sempre que você precisar."

            mc "Eu quero acreditar no que você tá falando... Que você quer fazer a coisa certa com a [fen]."

            mc "Pode sempre me falar tudo. Toda a verdade. Eu não vou te julgar."

    s "Eu quero poder falar pra você tudo de tudo... e eu quero fazer a coisa certa, [mc]."

    s "Mas o que é certo pra um não é pra outro. Cada pessoa tem uma visão diferente das coisas."

    mc "Eu sei... é verdade... mas tem certas coisas que a gente pode olhar na Lei. Se for crime, então não pode."

    s "É verdade. Mas eu juro que não tem crime. Talvez antes... mas nunca com a [fen]. Ninguém chegou a isso."

    mc "Mas, [s]. E os machucados dela? Ela tá sempre machucada nos mesmos lugares!"

    s "Isso, [mc]... Isso é o resultado do que ela{nw}"

    scene s8_julia1 with hpunch

    g "Oieeee!"

    s "J-júlia!?"

    g "Por que vocês tão com essa cara?! Que bosta, hein?!"

    mc zerado "..."

    s "A gente tava falando um assunto sério."

    g "Verdade? Foda-se.{w} Agora EU sou o assunto. A estrela do dia! A mina mais gata do... epa epa epa..."

    g "O [mc] tá aqui? Não acredito! Que que vai ter?! Por que você não me falou?"

    s "Eu chamei ele e minha discípula pra uma reunião aqui em casa."

    g "Que bacana! Finalmente eu vou conhecer a guria que você vive falando."

    scene s8_julia2 with Dissolve(1.0)

    pause

    g "Essa pirralhinha dá trabalho, né? Eu já falei pra você dar uns croques nela."

    s "J-júlia! Não fale isso assim!"

    g "Que foi? Criança que dá trabalho tem que aprender as coisas."

    s "Você precisa pensar melhor antes de falar as coisas. Você só vai falando... ainda vai se ferrar com isso."

    g "Olha, mana... você não tem que viver como se o mundo tivesse uma câmera vendo tudo o que você faz."

    g "É normal a gente cagar e sentar em cima. Eu sei que você é toda perfeitinha, mas os humanos são assim, meio desgraçados."

    s "[g]..."

    g "Que foi? Tô mentindo, [mc]?"

    menu:
        "A [g] tá certa. As pessoas erram.":


            mc charmoso "Eu concordo com a [g]. As pessoas são assim, [s]. A gente é emotivo, daí acaba fazendo burrada mesmo."

            mc envergonhado "Querer viver tudo certinho é cansativo demais e você vai acabar criando rugas na testa."

            g "Tá vendo? É isso aí que eu tô falando, mana! Rugas! Já imaginou?! Eca!"

            s "Vocês dois..."

            mc "Hehe..."
        "A [s] tá certa. A gente tem que fazer o certo.":


            mc normal "A [s] tá certa, [g]. A gente não pode só sair fazendo o que a gente quer. A gente não é animal."

            mc "Quem só consegue fazer o que quer, sem respeitar as regras, é escravo tanto quem tá preso."

            g "Você pode soltar todos esses sons, mas pra mim é só baboseira de velho."

            s "[g]! Não fala assim com ele. Ele tá certo."

            g "Vocês podem dar a mão e ir pro cemitério. Eu sou jovem demais pra aguentar."

            mc zerado "..."
        "Eu não vou me meter nessa...":


            mc zerado "Nem vem que eu não vou me meter nessa briga de vocês..."

            g "Nossa, que bundão, esse [mc]!"

            s "Ele tem razão, [g]. Você parece uma adolescente falando."

            g "Eu não sou velha igual vocês. Talvez seja por isso."

            s "Que absurdo..."

    g "Ei! Pera!"

    scene s8_julia3 with Dissolve(1.0)

    pause

    g "Que blusa é essa?"

    s "N-não sei. Q-qualquer uma que tinha aí."

    g "Mentirosa. Eu nunca vi você com ela."

    s "Ela é nova... m-mas é uma blusa normal."

    g "Nanananana... Nem vem. Olha pra esse decote, mana! Quem diria, hein?!"

    s "N-não fala assim, [g]! Que vergonha..."

    g "Olha como ela tá te apertando. Seu peito tá mó grande nessa blusa. Parece até maior que o meu!"

    g "Gente, não tá doendo isso, não?"

    s "[g]! Pelo amor! M-meu busto sempre foi assim..."

    g "Até parece que você colocou silicone. Tudo isso é por causa do [mc]?"

    s "N-não! Chega! E o-olha pra SUA roupa! Você acha que é assim que a gente se veste!?"

    g "É minha roupa de dormir, ué."

    s "Mas é meio dia, [g]!"

    g "Hoje eu vou ficar em casa o dia todo. Por que eu vou me trocar pra me trocar de novo pra dormir depois?"

    "Que tipo de pensamento preguiçoso é esse?"

    s "N-não vou nem comentar. Mas a gente tem visita. E a [fen] vai chegar logo logo."

    g "É bom pro [mc] ver que nem você e nem a garotinha tem chance contra mim. Eu sou a mais gostosa daqui."

    s "Ela é adolescente, [g]! Para de falar absurdo."

    g "É bom ela aprender desde cedo quem é que manda. Voc-"

    "{i}Ding dong{/i}"

    g "Falando na diabinha..."

    scene s8_sayuri8 with Dissolve(1.0)

    s "Ai. Eu vou lá atender ela. Eu vou falar um pouco com ela lá fora. Mas daqui a pouco eu volto."

    mc normal "Tá bom. Isso vai ser bom pra vocês. Aproveita."

    s "Sim. A gente precisa conversar um pouco sozinhas..."

    s "E você cuidado com a [g]. Ela... tudo bem, você entende."

    g "Ei. Eu não sou um animal raivoso..."

    s "[g]... se comporta."

    scene black with dissolve

    scene s8_julia4 with Dissolve(1.0)

    g "Ei. Gostoso. Vem aqui pra eu falar uma coisa com você."

    if julia_namoro:

        mc "Tava com saudades da minha gata."

        g "E eu de você. Nem acredito que você veio aqui."

    mc "Mas a [s] tá aí. É melhor a gente não aprontar nada."

    g "Quem disse que eu quero aprontar?"

    mc zerado "Eu te conheço, [g]. Quanto mais proibido, melhor pra você."

    g "Não vou negar que sou louca por uma baguncinha. Só que agora a mana tá nervosa... não vou complicar mais ainda."

    mc envergonhado "Puxa, a [g] pensando nos outros?"

    g "Só pela mana, babaca."

    if julia_namoro:

        g "Eu só queria te falar uma coisa..."

        scene s8_julia5 with Dissolve(1.0)

        pause

        mc "Q-que foi?"

        g "Você sabe que agora que a gente tá junto não é pra você sair com outras, né?"

        menu:
            "Claro que eu sei.":


                mc "Claro que eu sei... não precisa se preocupar com isso."

                g "Acho bom."
            "Vale pra você também, né?":


                mc "Sei... mas espero que isso também conte pra você, né?"

                g "Claro... eu sou um poço de honestidade."

                g "E eu quero a mesma coisa de você. Porque se você não se comportar, vai foder tudo."

        g "Só tem uma coisa... uma exceção. Que eu te falei lá na festa que a gente fechou a parceria."

        mc "Hm?"

        g "Eu deixo você namorar com a mana."

        mc "Sério?"

        g "Ela viu você primeiro. Não ia ser justo eu roubar você dela. Daí eu não vou reclamar se você ficar com ela."

        if not sayuri_namoro:

            mc "Ok... mas não esquenta com isso, porque eu e a [s] somos só amigos mesmo."

            g "Sério que você tá perdendo um mulherão daqueles? A mana é perfeita."

            mc "Eu sei que a [s] é incrível. Não precisa fazer propaganda dela."

            g "Tá... mas eu não entendo por que você não pega ela logo."
        else:


            mc "Então... a gente tá numa pegada séria eu e ela."

            g "Eu sabia, né? Ela fala de você, fica vermelha, sonhando acordada... ela tá de paixonite."

            g "É muito fofo ver ela assim. Quem dera eu tivesse um primeiro amor desse jeito."

            mc "Certeza que você não liga?"

            g "Se for ela eu não ligo. Agora... talvez eu provoque você um pouco na frente dela."

            mc "Tá louca?!"

            g "Só pra eu ficar um pouco molhada... eu adoro isso, [mc]..."

            mc "[g]... você é maluca."

            g "E a mana é inocente. Pra ela entender, só se a gente transar completamente pelados na frente dela."

            mc "Sei não..."

            g "Não importa o que você acha. E se der ruim, fazer o quê. Viver perigosamente é assim."

            mc "[g]!"

            g "E claro que eu ia ficar do lado dela e falar que você me forçou a tudo... eu amo a mana mais que você."

            mc "Valeu..."

    g "A mana gosta muito de você mesmo. E ela tá super nervosa com tudo isso que tá rolando."

    scene s8_julia6 with Dissolve(1.0)

    pause

    g "A mana mudou de uns tempos pra cá. Deve ser por causa disso tudo."

    mc "Como ela tá agora?"

    g "Ela tá mais nervosa, sei lá... meio irritada também. Mas deve ser por causa dessa transição dela."

    menu:
        "Deve ser mesmo. Tá suave.":


            mc normal "É... esse negócio de ser técnica não é fácil. Mas ela vai dar um jeito."

            mc "A [s] é uma pessoa incrível e ela pode contar com a gente, certo?"

            g "É... é o que eu tô torcendo, né? Eu queria ajudar mais, mas a mana é meio fechada pra essas coisas."

            g "Nem eu sei direito o que tá rolando naquela parada. Esse povo é doidão mesmo."

            mc envergonhado "Nem fala... eu só tô preocupado com a garota e até com a [s]."
        "Você sabe o que acontece na Cidade Chinesa?":


            mc desculpa "[g]... você sabe o que acontece lá na Cidade Chinesa? A história da [s] e da [fen], a vila proibida..."

            g "Um pouco... a mana é meio fechada. Ainda mais com essas coisas da China dela."

            g "Eu sei que ela tá treinando a menina e a garota é meio terrível. Ela foge, não obedece direito..."

            mc desculpa "Mas e sobre o treino? A menina tá sempre machucada..."

            g "Isso é normal, tonto. A mana sofreu muito quando ela tava treinando. Mesmo depois que ela ganhou medalha."

            g "Elas caem, se ralam tudo."

            mc "Eu acho que não é isso, [g]... a garota tá sempre com medo e teve que sair fugida de lá pra fazer ballet."

            g "O que você tá querendo dizer com isso?"

            mc "Talvez o treino tá duro demais. E se a [s] tiver agredindo a [fen]?"

            g "Que absurdo, [mc]! Não acredito que você tá falando isso da mana!"

            mc preocupado "Só qu-"

            g "Nada disso, bocozão. A mana é uma pessoa boa. Ela nunca ia fazer isso."

            mc concentrando "[g]..."

    g "Olha bem no meu olho e fala que você acredita que a mana podia tá fazendo qualquer coisa de errado."

    mc desconfiado "Seu olho... seu olho é amarelo, [g]?"

    g "Hm?"

    mc "Agora que eu tô reparando. Teu olho é amarelo. Você tem problema no fígado?"

    g "Que problema no fígado, maluco? E como assim só agora você percebeu? Meu olho sempre foi assim."

    mc "Pois é... mas só agora que eu realmente notei."

    scene s8_julia7 with Dissolve(1.0)

    pause

    g "Você é muito anta, [mc]. Sempre isso é uma das primeiras coisas que falam pra mim. E você só disse agora?"

    mc "Tá, entendi. Você quer dizer que eu sou lerdo. Mas o que é isso?"

    g "É...{w} lente. Só isso."

    mc normal "Lente? Não acredito que você precisa de óculos."

    g "Preciso e daí? Olha minha cara de que eu ia ficar igual a [o] com aquele trambolho no rosto."

    g "Daí eu acabei pegando lente pra mim. Como eu já ia usar, dei uma mudada e peguei uma amarela assim."

    mc "Tá explicado. Acho que não dá pra imaginar você de outro jeito agora. Já acostumei."

    g "Quem dera eu tivesse aquele olho azul maravilhoso da mana."

    mc "Agora que você falou... não é normal chineses terem olho azul, né?"

    g "Você tá falando que a mana é uma aberração?"

    mc "Não! Não é isso... só tô falando que não é comum. Seu pai e sua mãe são chineses?"

    g "Os da [s] são. Eles são meus pais de criação, eu não conheço meus pais de verdade."

    mc "É... malz falar sobre isso."

    g "Relaxa. Mas os olhos da mana são bem bonitos."

    g "Mas é uma pena que ela tá chegando com a tontinha. A gente podia se beijar aqui agora..."

    menu:
        "Acho que dá tempo se for rápido.":


            mc "E se a gente for bem rapidinho?"

            g "Já falei que não vou fazer nada. Não me tente."

            mc "Mas você que falou..."

            g "Bobo..."
        "Melhor você parar de besteira.":


            mc "Você mesmo disse que não er-"

            g "Como você é mala, [mc]. É pra você aceitar e daí eu nego. Você não sabe nada sobre mulher."

            mc "Mas-"

            g "Se você não fosse legal, ia acabar sozinho."

    mc "Vai entender..."

    s "Oi. Chegamos."

    mc "O-opa!"

    scene s8_fensay1 with Dissolve(2.0)

    pause

    mc normal "Oi, garotas."

    g "Aí estão mãe e filha. Elas não são igualzinhhas, [mc]?"

    menu:
        "Igualzinhas...":


            mc normal "Elas são parecidas mesmo. Quem sabe irmãs separadas no nascimento?"

            s "[mc]..."

            g "Daria uma boa novela!"

            fen "O-oi!"
        "Sabia que isso é preconceito?":


            mc zerado "[g]... sabia que isso é preconceito, né?"

            g "Como assim?"

            mc "Só porque elas são de outra etnia, falar que são iguais."

            g "Afe, [mc]! Tudo é preconceito hoje! Não pode nem falar de loira, de preto, de estrangeiro. Afe..."

            fen "E-eu não ligo..."

            g "Tá vendo? A guria não liga."

            mc "[g]... só cala a boca."

            g "Tá..."

    mc envergonhado "Oi, [fen]. Tudo bem?"

    fen "Oi..."

    s "[fen], essa aqui é a minha casa. O [mc] você conhece. E essa outra aqui é a minha irmã, a [g]."

    g "Fala, pirralha! Tudo legal?"

    fen "T-tudo... muito prazer..."

    g "Olha como ela é educada... ainda existe criança assim?"

    s "C-claro, [g]. A [fen] é uma garota muito especial. Ela tá se esforçando bastante pra ser uma atleta."

    s "Ela é super regrada e teve uma excelente educação da família e lá no templo também."

    fen "O-obrigada."

    mc normal "Isso eu posso falar. A [fen] sempre foi uma boa garota."

    fen "..."

    scene s8_fensay2 with Dissolve(1.0)

    pause

    s "Nossos treinos tão cada vez melhores. A [fen] tá se esforçando bastante e daí ele merecia um descanso."

    s "Daí pensei em juntar a gente aqui pra gente passar um tempo... legal... juntos."

    fen "É-é..."

    mc normal "Vai ser bem bacana, [fen]."

    g "E se tem festa eu quero participar também."

    s "T-tá legal, [g]."

    fen "Eu fiquei feliz de vir aqui com vocês. O-obrigada, mestra."

    s "Eu falei pra você que se você ficasse firme e se esforçasse, eu ia te recompensar, né?"

    fen "V-verdade. Eu me esforcei bastante essa semana."

    s "Foi mesmo. E as coisas vão melhorar cada vez mais."

    fen "Sim..."

    scene s8_fensay3 with Dissolve(1.0)

    pause

    s "Você tava meio triste esses dias, né?"

    fen "S-sim..."

    s "Eu fiquei preocupada com você, [fen]."

    fen "D-desculpa... eu não queria preocupar a mestra e todos os outros..."

    s "Tudo bem... agora tá passando. Isso que importa."

    fen "É..."

    s "Você... tá querendo ser uma atleta ainda?"

    fen "Hm? C-como assim, mestra?"

    s "Isso foi uma coisa que eu nunca perguntei. Você ainda quer ser uma ginasta de ponta e concorrer nas Olimpíadas?"

    fen "C-claro!"

    s "Isso é bom, mas eu preciso que você seja sincera comigo. Porque a gente nunca falou sobre isso."

    s "Até hoje eu não sei como você chegou no templo. Por que você foi escolhida? Você queria?"

    fen "E-eu..."

    menu:
        "Depois a gente vê isso. Vamos curtir.":


            mc normal "E se a gente deixar essa conversa pra depois, [s]? A gente veio se divertir, né?"

            s "A-ah... você acha uma boa?"

            mc "Sim. A [fen] quer sentar, relaxar, falar sobre as coisas boas da vida."

            s "Tem razão."
        "Vou deixar elas converarem...":


            mc desconfiado "..."

            fen "Foi mais a minha família... eles queriam... fazer parte..."

            s "Ah... entendi."

            fen "E daí o jeito era el-"

            s "Entendi, entendi. Mas vamos deixar essa conversa pra outro dia."

    scene s8_fensay4 with Dissolve(1.0)

    pause

    s "Hoje a gente precisa se divertir. A gente vai passar um tempo legal. A gente vai... é... fazer coisas divertidas."

    fen "L-legal..."

    g "A [s] sabe de diversão tanto quanto aqueles guardas da Inglaterra que ficam parados o dia todo..."

    mc zerado "[g]... você abre a boca só pra falar merda?"

    g "E você como sempre muito chatonildo. Eu só tô querendo melhorar o clima, só isso..."

    s "A [g] tá certa. A gente precisa melhorar nosso clima. E se a gente sentar?"

    g "Sentar? Isso é uma festa ou reunião de condomínio?"

    mc envergonhado "[g]... pouco ajuda quem não atrapalha."

    s "Desculpa se eu não sei muito bem me divertir."

    fen "Tá tudo legal, mestra. Eu queria muito muito conhecer onde você mora."

    fen "Eu acho tão legal como são as coisas fora da Cidade Chinesa. Tudo parece tão diferente."

    fen "As ruas são maiores, e aqui onde fica sua casa é tão bonito. Não tem um monte de casa uma em cima da outra."

    s "Haha... é legal, né?"

    fen "Não vejo a hora da nossa família ganhar uma casa assim."

    fen "E-eu sei que depende de mim... p-por isso eu vou me esforçar."

    "Hmm... ganhar uma casa? Como assim?"

    s "Não vamos entrar nessas coisas agora."

    g "Pelos deuses do babado... sorte que eu tô aqui. Vocês são terríveis em se divertir. Vocês duas e você também"

    mc zerado "Mas eu não tô fazendo nada..."

    g "Exatamente!"

    g "Vocês vão vir aqui agora. Vem logo!"

    scene black with dissolve

    g "Você senta aqui. Você aqui. Você aqui e você ali."

    g "Pronto."

    scene s8_todos1 with Dissolve(1.0)

    pause

    g "Eu acho que a gente devia ir pra uma balada."

    mc "Você tá louca?! A [fen] é muito nova."

    g "Eu sei. Como a gente vai ter que ficar aqui por causa da novinha, a gente vai brincar de alguma coisa."

    g "O que vocês acham de 'O Senhor Mandou'!?"

    s "Que brincadeira é essa, [g]?"

    mc "Eu não sei se é uma boa ideia a gente deixar a [g] decidir o que a gente vai fazer."

    fen "..."

    g "Eu aposto que o [mc] vai adorar essa brincadeira."

    mc "Eu aposto que eu vou odiar essa brincadeira."

    g "Você nem sabe que brincadeira que é ainda e já tá reclamando. Quantos anos você tem? 60?"

    s "[g]... pare de ofender as pessoas. Qual o problema de ter 60 anos?"

    g "Você também, mana?!"

    fen "Hihi..."

    g "Até a outra aqui tá rindo de mim agora.{w} Quer saber? Foda-se. Escutem aqui."

    g "A brincadeira é assim. O [mc] é o 'Senhor' e ele vai fazer uma pergunta pra cada uma. Só uma pergunta."

    s "Uma pergunta?! Qualquer pergunta?!"

    g "É. Ele vai perguntar uma coisa, qualquer coisa que ele quiser. E a gente é obrigada a responder."

    g "Não pode mentir e nem falar 'não'. Tem que responder com a verdade e nada mais que a verdade."

    fen "É..."

    g "Que foi, garota?"

    fen "E s-se alguém mentir?"

    g "Se alguém mentir, todo mundo tem que tentar ver se é mentira mesmo. Se for mentira e ficar provado, vai ter que responder outra."

    g "Se mentir de novo e for descoberta, vai ter que responder de novo! Até que a pessoa fale a verdade ou não seja descoberta."

    fen "T-tá..."

    g "E tem uma última coisa. Se o [mc] conseguir fazer a gente mentir pelo menos uma vez, ele pode escolher um castigo pra uma de nós."

    mc "Posso pedir pra vocês fazerem alguma coisa?"

    g "É. Mas só uma."

    mc "Vai ser você provavelmente..."

    g ""

    g "Haha! Idiota... {w}Todo mundo entendeu?"

    scene s8_todos2 with Dissolve(1.0)

    pause

    s "Não sei, não, [g]... entrar assim na intimidade das pessoas... será que é uma boa?"

    g "Quem não deve não teme, mana."

    menu:
        "Eu não vou perguntar nada difícil.":


            mc "Não precisa se preocupar que eu não vou fazer nenhuma pergunta complicada. É só uma brincadeira."

            g "Nanana! Só tem graça se você deixar a gente sem reação, [mc]! A brincadeira é pra isso!"

            g "Vai pensando nas coisas mais cabulosas que você conseguir!"

            mc "[g]... não exagere..."
        "Acho bom vocês se prepararem!":


            mc "Acho bom vocês se prepararem!"

            s "[mc]?!"

            g "Assim que se faz, [mc]! Tem que ser do caralho!"

            fen "Ai meu Deus..."

            g "A coisinha ficou até assustada! Que fofa!"

    s "Não sei... eu tô nervosa com isso..."

    g "Deixa ela pra lá, [mc]. A brincadeira é assim. Você tem que escolher uma garota pra perguntar. Vai. Escolhe uma."

    "Uma garota que eu queira perguntar... de quem eu quero saber alguma coisa?"

    $ s8_sayuri = False
    $ s8_sayuri1 = False
    $ s8_sayuri2 = False
    $ s8_sayuri3 = False
    $ s8_julia = False
    $ s8_julia1 = False
    $ s8_julia2 = False
    $ s8_julia3 = False
    $ s8_fenju = False
    $ s8_julia2m = False

    label s8_pergunta_base:

        scene s8_todos3 with Dissolve(1.0)

    pause

    menu:

        "Sayuri" if not s8_sayuri:

            $ s8_sayuri = True

            mc "Eu vou perguntar pra [s]."

            s "P-pra mim?"

            g "Você foi a escolhida da vez, mana. Boa sorte."

            jump s8_pergunta_sayuri

        "Júlia" if not s8_julia:

            $ s8_julia = True

            mc "Eu quero fazer as perguntas pra [g]."

            g "Então vai ser a minha vez, né? Foda-se. Não tenho medo."

            s "[g]... não esquece que tem uma menor de idade aqui na sala."

            g "Como se ela nunca tivesse escutado pinto, bunda, caralho, buceta antes."

            mc "Melhor eu perguntar logo."

            jump s8_pergunta_julia

        "Fen Ju" if not s8_fenju:

            $ s8_fenju = True

            mc "É a vez da [fen]."

            fen "A-ai!"

            g "Não é pra maneirar só porque ela é novinha, hein?"

            jump s8_pergunta_fenju

    label s8_pergunta_sayuri:

        scene s8_mcsay1 with Dissolve(2.0)

        pause

        g "Qual vai ser a pergunta pra mana, [mc]?"

        "Eu vou perguntar..."

        g "Não esquece que você quer que ela tenha que mentir, pra você fazer mais perguntas."

        menu:

            "Qual é seu tipo de homem perfeito?" if not s8_sayuri1:

                $ s8_sayuri1 = True

                mc "Eu quero saber qual seu tipo de homem perfeito. O que ele tem que ter e o que não pode ter."

                g "Adorei! Excelente pergunta!"

                fen "Homem perfeito..."



                s "E-eu tenho que responder isso mesmo?"

                g "Claro, mana! O jogo é assim. Vai, fala logo!"

                s "Tá...{w} Pra mim, o homem perfeito... eu quero que ele seja um companheiro. Um cara legal que me apoie."

                s "Não precisa ser lindo... nem importa que roupas ele veste... eu me preocupo mais com o jeito dele."

                g "E que jeito é esse?"

                s "Já falei. Companheiro... que me entenda e me apoie nas minhas coisas. Que ele seja calmo, não brique comigo..."

                fen "Uma pessoa assim... s-seria legal..."

                mc "Haha..."

                s "Eu tenho meus objetivos. Então eu queria alguém que pudesse ficar do meu lado e me ajudasse com as minhas coisas."

                mc "Muito legal, [s]. Tá respondido."

                g "Nanana! Pera aí!"

                scene s8_jufen1 with Dissolve(1.0)

                g "E aí, garota? Você acha que essa resposta dela valeu?"

                fen "Ah?! Ah... v-valeu... eu acho..."

                g "Eu achei muito sem graça... mas se a maioria acha que valeu, então tá bom."

                s "Ufa..."

                if not s8_julia or not s8_fenju:

                    g "Pra quem você vai perguntar agora, [mc]?"

                    jump s8_pergunta_base
                else:


                    g "Nós três já respondemos."

                    jump s8_depois_jogo

            "O que você acha da [fen]?" if not s8_sayuri2:

                $ s8_sayuri2 = True

                mc "Já que a [fen] tá visitando, então vou fazer uma pegunta sobre ela."

                fen "S-sobre mim?"

                mc "Eu quero que você fale o que você acha da [fen]. Como atleta e como pessoa também."

                g "Nossa... que perguntinha sem graça..."

                s "[mc]..."

                mc "{size=20}É uma boa chance pra vocês se aproximarem. Vai por mim.{/size}"

                s "É... a [fen]... ela é uma garota incrível. Ela é talentosa, ela é esforçada e é uma boa menina."

                s "Eu sei que ela vai ter uma grande carreira pela frente. Vai trazer muito orgulho pra família e pro país dela."

                s "Quanto mais a gente conversa, mais eu vejo como ela é uma pessoa direita e me enche de orgulho mesmo."

                g "Isso aí é um discurso de formatura? Buuuu...."

                fen "[mc]... p-posso falar uma coisa?"

                scene s8_jufen1 with Dissolve(1.0)

                mc "Claro, [fen]. O que foi?"

                fen "Eu acho que ela tá m-mentindo."

                mc "Q-quê?!"

                s "[fen]..."

                g "Opa opa opa! Deixa e menina falar!"

                fen "Eu me escondi no jardim esses dias e escutei ela e a mestra dela falando de mim."

                fen "A mestra tava bem preocupada comigo... ela sabia que eu não tava indo bem. Eu tô muito longe das outras..."

                fen "A gente sabe que se eu não melhorar, eu não vou conseguir competir nas eliminatórias e não vou pra competição."

                mc "Que coisa, [fen]..."

                s "..."

                g "Péééhhhh! Errou! Mentiu! Vai ter que responder outra, mana! Sinto muito!"

                s "O-ok..."

                mc "[g]... isso é coisa séria."

                g "São as regras, querido. Já pensa na próxima."

                mc "Ai ai..."

                jump s8_pergunta_sayuri

            "Quais são seus planos pro futuro?" if not s8_sayuri3:

                $ s8_sayuri3 = True

                mc "É... o que você planeja pro futuro?"

                g "Nossa... que merda..."

                mc "Eu que tô perguntando... me deixa. Só 'siga o senhor'."

                g "Espertinho..."

                s "Hm... eu nunca pensei muito no futuro."

                scene s8_mcsay2 with Dissolve(1.0)

                pause

                s "Por um tempo, eu sempre achei que eu fosse ser a mesma coisa pra sempre."

                s "Ser uma competidora olímpica, com a cabeça naquele objetivo e focada no que eu tinha que fazer pra ganhar."

                s "Eu tinha a impressão que as coisas seriam assim por muito e muito tempo... mas o tempo passa rápido."

                s "Eu sinto que os anos foram meses... e agora eu não vou competir mais."

                s "Meu desempenho não é mais o mesmo... e a [fen] é a nova estrela da Cidade Chinesa. Muito mais nova e melhor."

                s "Mas... se eu tiver que falar, eu tô feliz. Eu tenho a chance de ser a professora dela."

                s "Ajudar ela a seguir esse caminho e quem sabe fazer mais sucesso do que eu."

                s "E depois... eu quero... parar com tudo isso, né? Quem sabe? Ter minha família e me afastar de tudo."

                s "É isso. Deixar isso pra trás e ter minha família, com a pessoa que eu gosto... e viver..."

                mc "Parece um bom sonho."

                g "Ah, mana! Para com isso!"

                s "Q-que foi agora, [g]?"

                g "Ter uma 'família e se afastar de tudo isso'? Sério?"

                scene s8_jufen1 with Dissolve(1.0)

                g "Ei, garota. Você já escutou a [s] falando isso alguma vez na sua vida?"

                fen "N-não... até já escutei ela f-falando que quer ocupar o lugar da mestra dela um dia."

                g "Aha! Tá vendo?!"

                s "[fen]! Por que você tá fazendo isso?!"

                fen "A mestra quer ajudar nosso templo a melhorar. Acho que é isso q-que ela quer fazer pra sempre."

                g "Eu também acho! A [s] já me falou alguma coisa assim outras vezes! REFUTADA!"

                s "Vocês..."

                g "A comissão diz que você não foi sincera e vai ter que responder outra!"

                mc "Mas, voc-"

                g "Você calado! Só quero que você me fale uma coisa."

                jump s8_pergunta_sayuri

    label s8_pergunta_julia:

        scene s8_julia8 with Dissolve(1.0)

        g "O que você vai querer saber, [mc]?"

        menu:

            "Como foi seu primeiro beijo?" if not s8_julia1:

                $ s8_julia1 = True

                mc "Conta aí [g] como foi seu primeiro beijo."

                g "Você acha que eu tenho 13 anos, [mc]? Falar de beijo?"

                fen "B-beijo?"

                g "Você realmente tá interessada nisso, guria? Você já tem idade pra fazer coisa mais gostosa do que beijar..."

                fen "C-como?"

                s "[g]! Olha o que você tá falando pra ela!"

                g "Presta atenção, menina."

                fen "T-tá."

                scene s8_jufen2 with Dissolve(1.0)

                pause

                g "Você tem que aprender que desde cedo a gente tem que saber o que a gente quer."

                g "Não tem essa de que você é nova demais pra isso ou pra aquilo. É você que tem que saber isso."

                mc zerado "Não acredito que é isso que você quer ensinar pra ela."

                fen "E-eu quero saber, [mc]."

                mc "Claro que você quer. Criança adora aprender o que não pode."

                g "Que criança?! Olha pra essa garota! Ela já é adolescente, quase adulta. Na idade dela eu já sabia tudo praticamente."

                g "É você quem manda na sua vida, menina. Não é ele e nem a mana."

                g "Ela pode ser sua professora, mestra, sei lá, de ginástica, mas é só isso. A vida é tua e é você quem manda."

                fen "S-sei... m-minha própria vida..."

                g "Isso aí. Você entendeu. E pode ficar tranquila que fazer cagada é normal. Você vai se foder muito na vida."

                g "Sofrer faz parte. Chorar, ficar triste, se arrepender das burradas. Isso aí a gente faz todo dia."

                g "Só não sofre quem nunca tentou nada."

                fen "É..."

                mc envergonhado "[fen]... isso é meio irresponsável, viu?"

                s "Meio? A [g] é uma pessoa com um coração maravilhoso, mas sem cabeça."

                s "Aliás... isso não tem nada a ver com o que o [mc] perguntou."

                g "Verdade... Acho que eu vou ter que responder outra..."

                mc "..."

                jump s8_pergunta_julia

            "No que você gostaria de trabalhar?" if not s8_julia2:

                $ s8_julia2 = True

                mc normal "Quero saber no que você quer trabalhar quando você terminar a faculdade."

                g "Sei lá. Em qualquer coisa."

                mc zerado "Essa é a resposta?"

                s "Não vale, [g]!"

                g "É que... eu só quero trabalhar, sabe? Eu quero ter minha vida e minha casa o mais rápido que der."

                s "Você não gosta daqui?"

                g "Claro que eu adoro, mana! Mas por sua causa, né? Se a gente pudesse só viver juntas pra sempre..."

                fen "..."

                g "Eu gosto muito dessa casa aqui, mas eu quero logo ter minhas coisas."

                g "Eu quero terminar a facul e daí fazer qualquer coisa. Não importa o que for."

                g "Pronto. Respondido?"

                s "[mc]. Olha aqui."

                scene s8_mcsay2 with Dissolve(1.0)

                mc "Que foi?"

                s "Eu não acredito nela."

                g "Como assim? Que saco..."

                s "Ela tá querendo falar desse jeito, mas eu conheço a [g]. Ela já falou várias vezes que ela queria ser bióloga."

                s "Ela já contou que queria muito viajar pelo mundo procurando coisas que ninguém achou. Estudar lugares diferentes..."

                s "Eu não acho que ela tá sendo completamente sincera nessa resposta."

                mc "Hmm... eu acho que eu já ouvi ela falando alguma coisa assim também."

                g "Ei! Não vai na dela, [mc]! Você quem decide! Você ia aceitar!"

                menu:
                    "Eu acredito na [g].":


                        $ s8_julia2m = False

                        mc "Eu acredito na [g]. Acho que pra ela o que mais vale é realmente ter a vida dela igual ela tá falando."

                        g "Ufa... me livrei."

                        if not s8_sayuri or not s8_fenju:

                            g "Pra quem você vai perguntar agora, [mc]?"

                            jump s8_pergunta_base
                        else:


                            g "Nós três já respondemos."

                            jump s8_depois_jogo
                    "Ela tá querendo enganar a gente.":


                        $ s8_julia2m = True

                        mc "A [s] tá certa. Você tá enrolando a gente, [g]."

                        g "Aaaahhh não! Fala alguma coisa, garota!"

                        fen "E-eu não sei..."

                        mc "Para de encher o saco dela."

                        g "Afff...."

                        jump s8_pergunta_julia

            "O que você acha da [s]?" if not s8_julia3:

                $ s8_julia3 = True

                mc charmoso "Quero que você seja sincera e fale o que você realmente acha da [s]."

                g "Da mana?!"

                mc "É e é pra ser sincera, sem enrolar."

                g "Essa é fácil. A mana é a pessoa mais incrível do mundo. A perfeição do universo."

                g "A mana me salvou de tudo e me ensinou que o mundo não é uma merda completa."

                g "Ela é linda, tem o corpo perfeito, um peitinho caprichado, uma bunda redondinha..."

                s "[g]!"

                fen "A m-mestra..."

                g "Além de que ela é talentosa, esforçada, e super meiga... ufa."

                g "E aí? Gostou?"

                mc envergonhado "Ela parece a melhor pessoa do mundo."

                g "Sem dúvida ela é."

                if sayuri_namoro:

                    mc charmoso "Sorte que ela é MINHA namorada, né?"

                    s "[mc]..."

                    g "Por enquanto..."

                    s "Ei vocês... p-por favor parem..."

                g "Quem sabe um dia ela aceita fugir comigo pra bem longe."

                mc zerado "Bom, acho que a gente já entendeu. A resposta tá excelente. Todo mundo concorda?"

                s "S-sim..."

                fen "..."

                g "Eu falei que era fácil. Eu sou nota 10 na matéria mana."

                if not s8_sayuri or not s8_fenju:

                    g "Pra quem você vai perguntar agora, [mc]?"

                    jump s8_pergunta_base
                else:


                    g "Nós três já respondemos."

                    jump s8_depois_jogo

    label s8_pergunta_fenju:

        scene s8_fenju1 with Dissolve(1.0)

        g "O que você vai tirar da guria?"

        fen "A-ai..."

        mc envergonhado "Calma, [fen]. Eu vou de boa."

        menu:
            "Fale uma pessoa que você admira.":


                $ renpy.block_rollback()

                mc normal "Eu quero que você fale de alguém que você admira. Quem seria essa pessoa?"

                fen "Que eu admiro..."
            "Você gosta de treinar com a [s]?":


                $ renpy.block_rollback()

                mc normal "O que você tá achando de treinar com a [s]? Você gosta dela como sua treinadora?"

                fen "A m-mestra?! É..."
            "Com quem você se dá bem na sua família?":


                $ renpy.block_rollback()

                mc normal "Com quem você se dá melhor na sua família?"

                fen "Hmmm... da minha f-família?"

                mc "É. Seu pai, sua mãe, irmãos, tia, vó, não sei..."

        g "Pera! Deixa eu mudar a pergunta.{w} Eu quero que você fale pra gente de quem você gosta."

        mc zerado "Ei. Eu que tenho que fazer a pergunta."

        g "Eu que ensinei o jogo. Vocês fazem o que eu falo."

        mc "..."

        g "Eu só vou usar esse poder quando você perguntar coisa nada a ver. Eu prometo."

        mc "Isso é super subjetivo. 'Nada a ver' pra quem?"

        g "Pra mim, ué. Eu sou a deusa da brincadeira."

        g "Deixa esse cara pra lá, menina. Responda o que eu perguntei. De quem você gosta?"

        fen "D-de quem eu gosto? Como assim?"

        g "Da pessoa que você gosta pra dar uns pega, entendeu?"

        fen "C-co-como é?!"

        scene s8_todos3 with Dissolve(1.0)

        s "[g]... não exagere. A [fen] é muito nova pra isso."

        g "Você sabia que já tem gente que tem filho com essa idade, né? Eu tô falando algo mais tranquilo..."

        s "Mesmo assim, ela se dedica à ginástica em primeiro lugar. Ela não tem tempo pra isso."

        g "Tá bom. Deixa ELA responder... pode falar, garota."

        fen "É-é..."

        scene s8_mcfen1 with Dissolve(1.0)

        fen "E-eu gosto de todo mundo na Cidade Chinesa. Esse é o pessoal que eu gosto mais..."

        mc "De quem você gosta lá?"

        fen "Eu gosto da mestra, das pessoas que limpam nossas coisas... eu gosto do Bao Chang... ele é bem legal."

        mc "Bacana."

        g "Nada de bacana. Obviamente que ela não tá respondendo direito! Olha pra cara dela, seu mula."

        mc "Mula é você..."

        g "Menina, o que você acha do [mc]?"

        fen "D-do [mc]?! Q-que que tem?"

        g "Você gosta dele?"

        fen "E-eu... eu gosto..."

        s "..."

        g "Mas como amigo ou algo mais?"

        fen "E-eu... eu não sei..."

        g "Aha! Tamo chegando em algum lugar! Claro que sabe! Fala!"

        fen "E-eu-"

        mc "Chega. Cala a boca, [g]."

        g "Ei! Calma aí. É só uma brincadeira!"

        mc "Não tá vendo que ela tá nervosa?{w} Esquece ela, [fen]."

        fen "Mas... eu gosto de você... i-isso é verdade."

        mc "Eu sei... eu também gosto de você."

        fen "S-sério?!"

        mc "Claro. Você é uma garota bacana, muito resiliente, esforçada e talentosa."

        fen "E-eu?"

        mc "É. Por isso que eu gosto de você. Mas não desse jeito que a [g] tá falando."

        mc "A gente é amigos e a gente pode contar um com o outro quando a gente precisar."

        fen "M-mas... [mc]... v-você nunca vai gostar de mim... como... mais que amiga?"

        s "!"

        g "..."

        scene s8_mcfen2 with Dissolve(1.0)

        pause

        mc "Nunca. E isso por-"

        fen "P-por que eu sou feia?!"

        mc "Claro que não. Você é muito fofinha. E tenho certeza que vai crescer e ser uma mulher linda."

        fen "Ai..."

        mc "Mas eu não consigo olhar pra você assim. Mesmo que os anos passem, você sempre vai ser minha amiguinha."

        mc "Quando a gente é mais novo, às vezes os sentimentos vão aparecendo e a gente não sabe muito bem o que é."

        mc "Você pode olhar pra mim e achar que gosta de mim assim, mas talvez você só esteja confundindo as coisas."

        fen "S-será?"

        mc "Depois que a gente cresce, a gente entende melhor tudo isso. Quando a gente é jovem é mais difícil."

        mc "E por isso que nesses casos sou eu que tenho que proteger você. Eu que tenho que ser o adulto aqui, né?"

        g "Óbvio, olha pra essa cara já criando ruga."

        mc "Calada..."

        mc "Eu preciso entender que seria errado gostar de alguém tão mais nova do que eu. Que é quase uma criança."

        mc "E não é só uma questão de lei. Porque isso é proibido. Mas também é uma questão da gente fazer o certo."

        mc "Entender que nessa idade você pode tá confusa. E você precisa de tempo pra amadurecer tudo isso que você sente."

        mc "Se aproveitar de uma pessoa menor, mesmo que pareça que ela quer, não tá certo. Isso devia ser óbvio pra qualquer um."

        mc "Não tem nada a ver com você ser feia ou qualquer coisa com você. Podia ser qualquer garota. Você entende?"

        fen "A-acho que sim... mas... é que... e-eu ainda tô meio triste, sabe? D-desculpa..."

        fen "E-eu queria... q-queria que você... d-desculpa, [mc]..."

        mc "Não precisa pedir desculpas. Tá tudo legal."

        s "[fen]..."

        g "Olha aqui, [fen]."

        scene s8_jufen2 with Dissolve(1.0)

        pause

        g "O que o cabeça de bagre falou é verdade. Vai ter muito homem pra você dar em cima na sua vida."

        g "Você é nova. Olha eu. Até hoje eu tô correndo atrás aí e eu sou um tantinho mais velha que você."

        g "Tomar um fora dói. Ixi se dói. Mas passa."

        mc desculpa "Não é um fora, [g]... é mais complexo que is-"

        g "Xiu! Querendo ou não, claro que ela gostava de você e não vai rolar. Isso é tomar um fora."

        fen "..."

        g "Tem muito cara melhor que esse palerma, [fen]. E eu sei que ele tem essa cara de bobo e é meio bonzinho."

        fen "É... hihi..."

        g "Mas tá cheio de gente assim. E você vai achar um rapazote do seu tamanho e muito mais bonito."

        mc zerado "..."

        g "Eu prometo que quando você terminar seu treino, a gente vai sair eu, você, a [o] e a [s]."

        g "A gente vai atrás de um monte de homem. Combinado?"

        s "[g]! Eu não quero sair atrás de um monte homem!"

        g "Calma, mana. É pela [fen]. Você topa?"

        fen "A-acho que sim... s-se eu não for atrapalhar vocês..."

        g "Uma garota linda igual você? Só vai ajudar aparecer um monte de homem pra gente. Mas deixa um pra mim."

        fen "T-tá! Hihi..."

        scene s8_todos2 with Dissolve(1.0)

        mc "Essa pergunta valeu. Mais sincera do que essa conversa impossível."

        g "Tá certo. Essa eu vou ter que concordar."

        if not s8_sayuri or not s8_julia:

            g "Pra quem você vai perguntar agora, [mc]?"

            jump s8_pergunta_base
        else:


            g "Nós três já respondemos."

            jump s8_depois_jogo

    label s8_depois_jogo:

        pass

    mc "Verdade."

    scene s8_todos2 with Dissolve(1.0)

    s "Nossa... essa brincadeira me deixou tensa..."

    g "Foi divertido, não foi?"

    menu:
        "Foi sim. Eu gostei.":


            mc "Foi massa. As coisas ficaram meio sérias, mas no fim foi legal, não foi, [fen]?"

            fen "..."
        "Sei lá... mais ou menos...":


            mc "Pra uma ideia da [g], acho que tá bom."

            g "Ei! A menina pelo menos gostou, né? Hen?"

            fen "..."

    g "A garota tá em choque!"

    s "Ela tá cansada, só isso. A gente falou um monte."

    mc "Verdade."

    g "Ai... foi só uma brincaideira..."

    if ( s8_sayuri1 or s8_sayuri2 ) and ( s8_julia1 or s8_julia2m ):

        mc "Mas não esquente que eu tenho um jeito de melhorar a vibe de todo mundo."

        g "Hm?"

        mc "Eu lembro da última regra que você passou. Que se eu fizesse vocês mentirem uma vez, eu poderia escolher alguém pra causar."

        g "Certo..."

        mc "E vai ser você!"

        g "Mas a [fen] só respondeu uma pergunta, espertão."

        mc "Eu sei... mas lembra que você mesmo falou que a pergunta já tinha tido mentira e verdade de uma vez."

        s "Eu concordo com ele, [g]... você mesma apontou a mentira dela na hora."

        fen "..."

        g "Aff... e o que vai ser?"

        mc "Eu quero que você suba aqui na mesa e dance um funk proibidão."

        g "Funk? Proibidão ainda por cima? Melhor ainda. Vocês vão ver que quadradinho de oito não é nada."

        scene black with dissolve

        scene s8_todos4 with Dissolve(1.0)

        pause

        mc "E não é que ela gostou da ideia?"

        s "A [g] sabe dançar muito bem. Desde criança ela gosta."

        g "{i}Essa lomba, lomba - essa lomba, lomba!{/i}"

        mc "Que raios ela tá cantando?"

        s "Vai saber..."

        fen "..."

        mc "Haha! Ela tá empolgada."

        s "Foi um bom castigo esse. Obrigada, [mc]."

        g "E agora vem a pirueta!"

        window hide

        pause

    scene black with dissolve

    s "E se a gente levantar e comer alguma coisa?"

    g "A mana podia cozinhar! Ela sabe fazer uns pratos incríveis."

    s "E se a gente esquecer a comida tradicional e comer pizza? Acho que a [fen] nunca comeu pizza..."

    fen "..."

    scene casa_sayuri2 with Dissolve(2.0)

    mc normal "Eu topo. Eu vou ajudar a rachar."

    g "Claro que vai. Vai comer também."

    g "Eu vou levar a maninha conhecer a casa enquanto vocês pedem."

    mc zerado "E você não vai pagar?"

    g "Claro que não. Você e a mana são os mais velhos. Eu e a [fen] somos crianças."

    mc "Sei..."

    s "Tudo bem. Eu e o [mc] resolvemos."

    g "Vem, maninha. Vem comigo."

    fen "Tá..."

    s "Eu vou pedir alguma coisa mais leve porque acho que a [fen] não tá acostumada, tudo bem?"

    mc charmoso "Claro."

    mc "O que é isso aqui, [s]? Esse painel aqui?"

    s "Ah. Esse é um biombo decorativo. Minha mãe que comprou pro quarto dela. Ele não vai ficar aí. Mas ela teve que sair correndo."

    s "Essa imagem aí, na verdade, é uma replica de um item muito importante pra cultura chinesa."

    mc "Sério?"

    scene casa_sayuri3 with Dissolve(1.0)

    pause

    s "É. É uma imagem do Ba Xian ou 'OITO IMORTAIS', como é conhecido aqui no ocidente."

    mc "Oito imortais..."

    s "São figuras muito importantes na cultura chinesa. E esse biombo foi pintado na época em que tudo aconteceu, na China medieval."

    mc "Uou!"

    s "O verdadeiro, claro. Esse aí é só uma cópia. O interessante é que o verdadeiro tá aqui na capital, acredita?"

    mc "Aqui na cidade?"

    s "Sim. Foi um presente que a China deu pelos nossos esforços em propagar a cultura pelo mundo."

    s "Ele tá guardado em um local secreto, muito bem protegido. Nem eu sei onde fica. Mas minha mestra sabe."

    mc "Caraca. Parece bem misterioso e especial."

    s "Pois é. Olha, já pedi a pizza. Vamos com elas ver se elas tão bem?"

    mc envergonhado "A [g] é complicada, né?"

    s "E-eu não quero duvidar dela... m-mas..."

    mc "Eu te entendo. Bora comer!"

    scene black with Dissolve(2.0)

    "..."

    "{i}chomp chomp{/i}"

    "{i}gulp{/i}"

    "..."

    "Hoje o dia foi bacana."

    "Fazia tempo que eu não tinha uma tarde tão bacana e 'normal' com as pessoas assim."

    "Sem rolo, sem complicação. Só um jogo bobo e diversão. Não vejo a hora de fazer isso de novo."

    pause

    g "Pizza é muito bom!"

    s "Estava uma delícia. Obrigada a todos."

    mc envergonhado "Não precisa agradecer, [s]. A gente que pagou pra ela..."

    g "Você nunca vai esquecer isso agora, né? Quer que eu te chupe por uma pizza de queijo?"

    s "[g]! Na frente de uma criança?!"

    g "Ela nem tá aqui."

    mc desconfiado "Ué? Cadê ela?"

    g "Acho que ela disse que ia no banheiro. Ela pegou alguma coisa aí por cima e saiu."

    s "Talvez tenha sido cansativo demais pra ela... daqui a pouco já vou levar ela pro quarto."

    mc normal "Eu vou ver como ela tá. Tudo bem, [s]?"

    s "Claro. Ela gosta de você, [mc]. Qualquer coisa chama a gente."

    mc "Tá."

    scene casa_sayuri4 with Dissolve(1.0)

    pause

    mc desconfiado "[fen]?"

    "Será que ela voltou pra sala? Mas tá tudo escuro pra cá."

    "E se ela só foi no banheiro?"

    menu:
        "Bater no banheiro":


            mc "Deixa eu ver no banheiro primeiro."

            "{i}toc toc{/i}"

            mc normal "[fen]? Tudo bem?"

            "..."

            "Nada. Também não dá pra ouvir nada lá dentro. Será aqui que eles deixam a porta fechada?"

            "Melhor eu não abrir. Vou pra sala."
        "Entrar na sala":


            "Vou dar uma olhada aqui na sala antes."

    scene black with dissolve

    "{i}sssss{/i}"

    scene s8_final1 with Dissolve(1.0)

    pause

    "Nossa. Tá escuro aqui."

    "Não tô vendo ela..."

    "Pera!{w} Ali no canto... [fen]?"

    "É ela mesmo? O que ela tá fazendo?"

    scene s8_final2 with Dissolve(1.0)

    pause

    "O que é isso na mão dela? Será que ela não percebeu que eu tô aqui?"

    fen "Ai... Hmm... {i}shiuf{/i}"

    "Ela tá chorando?"

    mc preocupado "[fen]?"

    fen "!!!"

    "{i}kbaumpt{/i}{nw}"

    scene s8_final3 with vpunch

    pause

    fen "[mc]!"

    mc preocupado "[fen]! O q-que é isso?!"

    fen "E-eu! Eu!"

    mc "Seu rosto... tá sangrando. Por quê?! Isso é uma faca!?"

    fen "..."

    mc "Você tava... se cortando?"

    scene s8_final4 with Dissolve(1.0)

    fen "..."

    mc "[fen]... fala comigo. O que tá acontecendo?"

    fen "[mc]... v-vai embora por favor..."

    mc "Como assim? Por quê?"

    fen "Por f-favor... só vai e-embora agora..."

    fen "P-por favor... não f-fala pra mestra... e-eu já tô voltando..."

    mc "[fen]... tá bom... eu não falo nada."

    fen "V-verdade? Não vai falar?"

    mc "Não. Se você não quer, eu não vou falar."

    "Ela tá sangrando! O que eu faço?!"

    fen "P-por favor... só vai embora... eu v-vou arrumar... {i}shiuf{/i}... tudo antes que a mestra venha."

    menu:
        "Tudo bem. Eu vou esperar você terminar.":


            mc desculpa "Tudo bem. Faça suas coisas, eu vou esperar você terminar."

            fen "N-não! E-eu..."
        "Eu não vou pra lugar nenhum.":


            mc preocupado "Eu não vou deixar você aqui assim."

            fen "P-por quê? E-eu preciso..."

            mc "Eu sou seu amigo, [fen]. E você tá precisando de um amigo agora."

    fen "[mc]... e-eu não consigo..."

    scene s8_final5 with Dissolve(1.0)

    pause

    fen "E-eu não consigo... parar..."

    mc "[fen]... pode falar pra mim... o que tá rolando?"

    fen "N-não..."

    mc "Tudo bem. Não precisa falar se não quiser."

    fen "E-eu odeio... eu odeio eles..."

    mc "O que você odeia? Quem tá fazendo coisa ruim com você?"

    fen "M-meus olhos, [mc]... eu odeio eles... e-eu queria tirar eles..."

    menu:
        "Seus olhos são lindos.":


            mc "Seus olhos são lindos, [fen]. Po-"

            fen "Não! Eles não são!"
        "Qual o problema com eles?":


            mc "Qual o problema com seus olhos?"

    fen "Eles são estranhos... eles não são normais! Olha pra eles, [mc]... eles são olhos de um monstro..."

    fen "É tudo culpa deles... e-eu nunca quis fazer isso... e-eu só queria treinar... igual a mestra..."

    fen "Mas eles queriam... que eu fosse melhor... eu não era boa de verdade..."

    mc "..."

    fen "E agora... eu sou um monstro... eles sabem... a mestra sabe que eu sou um monstro..."

    fen "Não importa se eu treinar... não é nada de verdade... é tudo culpa daquele negócio... que eles me dão."

    "O que ela tá falando? Eu não tô entendendo porra nenhuma."

    "O que eu posso falar pra ela nessas condições? Não dá nem pra falar que tudo vai ficar bem. Eu não sei..."

    mc "[fen]... vem aqui."

    fen "!"

    scene s8_final6 with Dissolve(1.0)

    pause

    mc "Eu tô com você, tá? Pelo menos agora... eu tô aqui."

    mc "Não sei o que tá rolando. Mas eu tô do seu lado. Eu tô com você."

    fen "[mc]... você não entende?"

    fen "Você vai ficar do lado de uma garota que não é mais normal? V-você não entendeu o que eu disse?"

    mc "Eu sei quem é você, [fen]. A garota que eu conheci na Cidade Chinesa. Que é super tímida, mas muito fofa."

    mc "Que quer fazer ballet, que admira a treinadora dela... que quer ver a família..."

    mc "Essa é a [fen] que eu conheci e que eu gostei muito. Que acabou virando minha amiga... de verdade."

    fen "Mas e-era mentira..."

    mc "O que eu gosto em você não tem nada a ver com ginástica. Isso aí, pra falar a verdade, nem ligo muito."

    fen "!"

    mc "Eu gosto dessa garotinha fofa que uma hora ou outra dá um sorrisinho lindo."

    fen "Hihi... v-verdade?"

    mc "Tá vendo? Essa risadinha aí que me conquistou. E isso é seu, de verdade, não é?"

    fen "É... é, sim. É sim, [mc]..."

    mc "Agora vem aqui. Vamos limpar seu rosto."

    fen "C-como? V-vai manchar tudo..."

    mc "Na minha camiseta. Daí você vai pra cozinha e eu vou pra casa. Fala pra elas que eu tive uma emergência."

    mc "A revista me chamou."

    fen "Mas é de noite..."

    mc "Vida de paparazzo é assim. Às coisas acontecem de noite. Elas vão acreditar."

    fen "T-tá..."

    scene black with dissolve

    "..."

    scene s8_final7 with Dissolve(1.0)

    fen "Acho que tá bom, né?"

    mc normal "Tá. Não sujou muito. Talvez a camiseta um pouco..."

    fen "Que bom... mas olha sua roupa..."

    mc "Tá tudo certo."

    fen "Eu tô cansada..."

    mc "A [s] falou que você ia pra cama logo. Descansa bastante."

    mc "E fica tranquila que eu não vou falar nada pra ninguém antes de você deixar, tá?"

    fen "Obrigada..."

    mc "Mas as coisas não podem ficar assim, ok? A gente precisa fazer alguma coisa."

    fen "Tá..."

    mc desculpa "Eu tenho a revista. E se for preciso a gente vai acabar com tudo isso, [fen]."

    fen "..."

    mc "Eu vou fazer tudo o que eu puder pra você e a [s] ficarem bem. De verdade."

    fen "T-tá..."

    mc "Agora vai lá antes que eles venham pra cá. Até outro dia."





    s "[mc]! [fen]!"

    mc angustiado "S-say!"

    scene black with dissolve

    scene say7_p30 with Dissolve(1.0)

    s "O q-que tá acontecendo aqui?"

    fen "M-mestra..."

    s "Você... não me diga que..."

    mc "[s]... tá tudo ok..."

    s "[mc]..."

    mc "Tá tudo bem agora."

    s "S-se você diz..."

    s "A gente precisa trocar sua camisa. Vamos experimentar uma lá no quarto."

    fen "T-tá."

    s "Você... podia passar a noite aqui?"

    mc "S-sério?"

    s "Eu adoraria..."

    mc "Não vai incomodar?"

    s "Você pode ficar aqui na sala e nós ficaremos no quarto..."

    s "Infelizmente a gente não vai poder conversar muito... mas só de saber que você tá aqui, eu ficaria feliz."

    fen "P-por favor?"

    "Ficar aqui na casa da [s]..."

    if sayuri_namoro:

        "Seria uma boa chance da gente ficar..."

    "Só que a [g] tá aqui também... eu sinto que pode dar muita merda."

    label say8_premium1:

        pass

    "E agora?"

    menu:
        "É melhor eu ir embora.":


            mc "Acho melhor eu ir embora, [s]. Deixar as garotas se divertindo aí."

            s "T-tem certeza?"

            fen "Ah..."

            mc "Não precisam ficar assim. A gente vai ser ver logo, ok? Fiquem bem."

            s "O-ok... A-até mais, [mc]."

            fen "Tchau."

            mc "Tchau, meninas."

            scene black with Dissolve(1.0)

            $ tempo = 4



            if carro:

                scene carro_mc_cidade2 with Dissolve(1.0)
            else:


                scene mc onibus_noite with Dissolve(2.0)

            pause
        "Ok. Vou ficar.":


            if not premium:

                call mensagem_premium from _call_mensagem_premium_51

                jump say8_premium1

            mc "Bom... se você acha que é uma boa, [s]... eu não quero incomodar a noite das meninas."

            s "V-você não vai. Tudo bem você dormir no sofá?"

            mc "Claro."

            s "Então é isso... eu vou... cuidar dessa aqui e... ir pro quarto. Boa noite."

            mc "Boa noite, Say. Até amanhã."

            fen "Até amanhã."

            mc "Boa noite, Fen Ju."

            s "Agora vamos, senhorita."

            scene black with dissolve

            scene sayuri_casa geral with dissolve

            "Ok... vou passar a noite aqui..."

            if sayuri_namoro and julia_namoro:

                "E eu tô ficando com as duas irmãs... como pode? Eu não sei onde eu tava com a cabeça quando aceitei isso."
            else:


                if sayuri_namoro:

                    "Eu e a Say tamo num lance sério. Seria legal se a gente passasse um tempo juntos aqui..."

                if julia_namoro:

                    "Eu e a [g] tamo namorando de verdade... fico imaginando a baguncinha que a gente podia fazer aqui hoje..."

            "Só tomara que dê tudo certo."

            "Vou arrumar aqui..."

            scene sayuri_casa geral with hpunch

            "{i}inheeeec{/i}"

            "Pronto... acho que deu pra improvisar uma cama."

            scene black with dissolve

            scene say7_p31 with Dissolve(1.0)

            "Boa..."

            "Não é o lugar mais confortável, mas pelo menos eu tô ajudando a [s] e a [fen]."

            "O que aconteceu hoje aqui não foi brinc-"

            "{i}zuzuzu{/i}"

            "Hm? Tá vindo um barulho de lá..."

            "{i}hahaha hohoho{/i}"

            "Parece que elas tão se divertindo pra caramba..."

            menu:
                "O que será que elas tão fazendo?":


                    "Ah... a curiosidade tá me matando..."

                    "Eu quero ver o que elas tão fazendo!"

                    "Eu não aguento... eu tenho que dar uma olhada... com certeza não é nada de mais..."

                    scene black with dissolve

                    "Opa... a porta do quarto tá aberta..."

                    "Hm?"

                    scene say7_p32 with Dissolve(1.0)

                    g "E o desfile tá começando! Vamo começar com a melhor!"

                    fen "Uhulll!"

                    s "[g]..."

                    g "É só um desfile, mana. Coisa de menina."

                    s "Não sei..."

                    g "Eu vou ensinar vocês como andar igual uma mulher poderosa."

                    fen "Haha..."

                    g "Que você tá rindo, pirralha?!"

                    fen "N-nada!"

                    g "E depois de andar, você para e pose!"

                    scene say7_p33 with Dissolve(1.0)

                    g "Isso vai deixar qualquer homem aos seus pés!"

                    fen "Ho-homens?! M-mais que um?!"

                    g "Claro, garota. Você quer impressionar o máximo possível!"

                    g "Agora que você viu que com o [mc] não vai rolar, você precisa começar a procurar uns garotos aí."

                    g "O primeiro passo é usar umas roupas bem decotadas, shortinhos, mostrar bastante carne, sabe?"

                    fen "C-carne...?"

                    s "Não escute o que ela tá falando, Fen Ju..."

                    g "Vamos ver quem pegou mais homem pra poder falar, mana!"

                    s "N-não quero competir nisso!"

                    g "Agora que você sabe como chegar no menino e as roupas que você tá usando, eu vou te dar outras dicas."

                    scene say7_p34 with Dissolve(1.0)

                    s "Eu não sei se essa é uma boa..."

                    g "A garota teve uma desilução amorosa, mana... ela precisa colocar esses sentimentos pra fora."

                    fen "A [g] é divertida, mestra."

                    g "Pode parando aí, menina! Ela pode ser sua mestra de ginástica, mas aqui eu sou a mestra."

                    s "[g]... nem... ah..."

                    "Parece que nem a [s] tá conseguindo domar a [g] ultimamente..."

                    g "Homem não tem nada na cabeça. Eles só querem saber de se aproveitar das mulheres."

                    fen "S-sério?"

                    g "Com certeza. E agora que você sabe dá pra usar isso pra fazer eles de trouxa."

                    s "Não é certo fazer ninguém de trouxa..."

                    g "O que eles querem é seu corpo. Olhar, pegar. Então é só você ir dando trela devagar."

                    g "Nunca deixe um homem pressionar você. Você sabe o que ele quer, então é só você garantir que ele continue atiçado."

                    g "É só fingir que você tá caindo na dele... deixe ele dar uma olhadas, dê uma risadinha, como se você tivesse adorando a atenção."

                    g "Você é só uma garota inocente e ele o lobo mau. Mas ele não sabe que no fundo quem tá entrando na armadilha é ele!"

                    fen "P-puxa..."

                    scene say7_p35 with Dissolve(1.0)

                    s "É isso que você ensinar pra ela, [g]? Que visão distorcida da relação entre homem e mulher!"

                    g "Você é inocente demais, mana... os homens não merecem você. Você devia ficar com uma garota."

                    s "!"

                    fen "G-garota?"

                    s "N-não escute ela..."

                    s "Eu acho que pode existir respeito mútuo entre homens e mulheres. Esse joguinho só é necessário quando não há respeito."

                    s "Quero dizer... não podemos só fazer o certo com as pessoas? Precisamos sempre seguir nossos desejos instintivos?"

                    g "Os homens são animais, mana... não espere que eles respeitem você mais do que a vontade de te comer."

                    s "Júlia! Olha o palavrão!"

                    g "Ok..."

                    s "Só pra terminar... eu acho que a gente pode se esforçar pra não machucar os outros só pra gente fazer o que quer."

                    s "Mesmo que um homem queira se aproveitar de uma mulher, ele podia pensar 'será que isso é legal?' E optar por não fazer."

                    g "Só nos seus sonhos..."

                    scene say7_p35 with vpunch

                    g "Ah! Tive uma ideia!"

                    g "Vamos colocar lingerie sensuais!"

                    s "P-pra quê?!"

                    g "Garotas fazem isso, mana! Eu prometo que é só isso e daí eu vou pra cama!"

                    s "Não sei da onde veio isso, [g]..."

                    g "Por favor! Eu queria mostrar pra menina aqui!"

                    s "Você vai deixar ela fora disso. É o mínimo! A [fen] ainda não é uma mulher!"

                    fen "Eu vou fazer 16 anos, mestra..."

                    s "Quando você tiver 18 anos a gente conversa sobre isso."

                    g "Você é uma estraga prazeres, mana... mas tudo bem... começa assim, garota. Depois a gente vê."

                    fen "T-tá..."

                    s "Parem de armar coisas. Eu tô ouvindo tudo!"

                    g "Vai pegar a sua, mana."

                    s "Tá bom..."

                    scene black with dissolve

                    g "O meu tá aqui também."

                    s "Por que sua lingerie tá no meu quarto?"

                    g "Sei lá..."

                    s "..."

                    "Epa... elas vão colocar lingerie? Acho que é uma boa hora pra eu dar o fora daqui."

                    "E perder a [s] e a [g] com quase nada? Aah... e agora?"

                    menu:
                        "Voltar pra sala":


                            mc "Melhor eu sair daqui."

                            scene black with dissolve

                            scene say7_p31 with Dissolve(1.0)
                        "Ficar mais um pouco":


                            scene black with dissolve

                            scene say7_p36 with Dissolve(1.0)

                            g "Não é gostoso se sentir sexy?"

                            s "Não sei... ainda não entendi porque isso é normal..."

                            fen "Vocês tão lindas!"

                            s "[fen]..."

                            g "Valeu, guria. Daqui uns anos você vai poder se juntar a gente também."

                            fen "Hehe..."

                            s "Eu nunca senti nenhuma vontade de fazer essas coisas."

                            g "Porque você nunca teve uma referência, mana. Se eu fosse a irmã mais velha e a gente ficasse mais junto você ia ver."

                            s "Hmm... pode ser..."

                            g "A garota aqui tá com os olhos brilhando!"

                            s "Esse é o problema."

                            scene say7_p37 with Dissolve(1.0)

                            g "Você precisa entender que toda mulher sente certas coisas, mana."

                            s "Eu não sinto nada disso..."

                            g "Claro que sente. Você só tenta esconder lá no fundo. Eu sei disso."

                            s "Calada..."

                            g "A gente é amiga aqui, não é, guria?"

                            fen "Sim!"

                            s "Para de arrastar a Fen Ju pro meio das suas... depravações..."

                            g "Sentir vontades não é depravação, mana... você é tão maravilhosa..."

                            s "Para..."

                            g "Ela não é, menina?"

                            fen "S-sim..."

                            s "Parem vocês duas... tão me deixando com vergonha..."

                            g "Segura ela."

                            fen "Hm-hm?"

                            scene say7_p38 with Dissolve(1.0)

                            g "Se você me desse chances, mana... eu nunca ia deixar você escapar de mim..."

                            fen "!"

                            fen "M-mas... você é garota..."

                            g "E daí? Vocês são muito do passado. Duas garotas podem se gostar também."

                            fen "Mas vocês... são..."

                            g "Não existe barreiras pro amor!"

                            s "C-chega d-disso tudo! Sai daquí, [g]!"

                            g "Tá bom... tá bom... mas acho que essa foi uma boa licão pras duas..."

                            fen "..."

                            s "Nada de licão! Só sai do meu quarto! A gente vai dormir as duas aqui. Você vai dormir no seu!"

                            g "Ok... tô indo... obrigada pela noite. Foi divertida."

                            g "Tchau, guria."

                            fen "Tcha-tchau..."

                            scene black with dissolve

                            s "Essa [g]... não dê atenção pra ela, Fen Ju."

                            fen "Hmm..."

                            "A [g] realmente é fogo{nw}"

                            scene say7_p39 with hpunch

                            mc "ARGH!"

                            g "Você... hmm..."

                            s "[g]?"

                            g "Desculpa, mana! Eu tropecei."

                            s "Ok..."

                            "Ela saiu correndo... eu devia ter saído mais rápido!"

                            g "Xeretando a gente, hmm..."

                            menu:
                                "N-não! B-banheiro!":


                                    mc "E-e-eu! B-b-banheiro!"

                                    g "Sei... banheiro... você sabe onde fica o banheiro."

                                    mc "V-verdade!"

                                    g "Não precisa se cagar que eu não vou falar nada."

                                    mc "N-não?"

                                    g "Hmm... vendo você... até que me deu uma ideia..."

                                    g "A mana me deixou meio no clima, sabe? Mas ela não vai me satisfazer."

                                    mc "C-certo..."

                                    g "Foi você que sobrou. Deixa eu usar seu pau?"

                                    mc "Q-quê?!"

                                    g "Vai logo."

                                    if julia_namoro:

                                        g "Você é meu namorado. É sua obrigação."

                                    menu:
                                        "Ok...":


                                            mc "S-se você quer... tudo bem..."

                                            g "Tira a calça, eu quero ter um papo com 'ele'."

                                            scene black with dissolve

                                            scene say7_p40 with Dissolve(1.0)

                                            mc "A-ah..."

                                            g "Hmmm... ele tá gostoso..."

                                            g "Mas cresce logo que eu quero ele duro na minha boca."

                                            mc "Faz sua parte então."

                                            g "Ele devia ficar duro só de me ver."

                                            mc "M-mas elas tão aqui do lado..."

                                            g "Para de pensar nelas, tem uma mina te chupando, seu bocó."

                                            mc "O-ok..."

                                            scene say7_p41 with Dissolve(1.0)

                                            g "Agora sim... tá melhorando... hmm..."

                                            mc "Ahh... sua boca..."

                                            g "Eu sei, ela é gostosa, né?"

                                            mc "Muito."

                                            g "Vai ficar melhor ainda, seu safado."

                                            g "Foca na minha boca molhada no seu caralho que vai melhorar."

                                            mc "A-ah... isso..."

                                            g "{i}slhup{/i}"

                                            g "Ele ainda não tá no máximo... hmm... eu quero ele maior pra mim."

                                            g "Quero ele na minha garganta."

                                            mc "Se você continuar falando e chupando assim!"

                                            g "Isso! Isso!"

                                            scene say7_p42 with Dissolve(1.0)

                                            g "Hmm... cof... axxim!"

                                            g "{i}slhup gullopp{/i}"

                                            g "Enfhia! HMM!"

                                            mc "Ah, [g]! Se continuar assim!"

                                            g "Gozza!"

                                            mc "Vou gozar na sua garganta, sua puta!"

                                            g "Ixxo! Vai!"

                                            scene say7_p42 with vpunch

                                            mc "AAAHHH!"

                                            mc "Ah! Ah..."

                                            g "Hmmm... {i}gulp{/i}"

                                            g "Delícia..."

                                            s "[g]?! O que você tá fazendo aí?"

                                            g "E-eu achei que tinha derrubado uma coisa mana, já tô indo pro quarto."

                                            s "Todo esse tempo?"

                                            g "Vem! Vamo pro meu quarto!"

                                            mc "Seu quarto?! Tá louca?!"

                                            if sayuri_namoro:

                                                mc "Eu não posso! Você sabe!"
                                            else:


                                                mc "Mesmo que eu e ela não teja juntos, ela nunca ia perdoar a gente!"

                                            mc "Eu vou pra sala!"

                                            g "Cagão!"

                                            scene black with vpunch

                                            scene black with dissolve

                                            scene say7_p31 with Dissolve(1.0)

                                            "Essa garota é louca! Não dá! Eu fiquei aqui pra ajudar a [s] e a [fen]."

                                            "Eu vou ter outras chances de ficar com a [g]..."
                                        "Agora não. É perigoso.":


                                            mc "D-de jeito nenhum! Ela tão aqui do lado!"

                                            g "E daí? Vai logo."

                                            mc "É perigoso demais. Eu não vou fazer."

                                            g "Caralho, hein? Nem pra isso você serve? Pelo amor..."

                                            mc "Vai logo pro seu quarto. Eu vou voltar pra sala."

                                            g "Que seja..."

                                            scene black with dissolve

                                            scene say7_p31 with Dissolve(1.0)

                                            "Ufa... a [g] é maluca... mas é melhor ter recusado."
                                "Fingir que é sonâmbulo":


                                    mc "zzzZzZzz"

                                    g "Hm? [mc]?"

                                    mc "rrrrooonnccc"

                                    scene black with dissolve

                                    g "Ei... sair andando não vai resolver nada..."

                                    mc "zzZzzzZ"

                                    "Eu tenho que voltar pra sala... e vai parecer que eu sou um sonâmbulo."

                                    g "Que que deu nesse cara?"

                                    scene black with dissolve

                                    scene say7_p31 with Dissolve(1.0)

                                    "Será que colou?"

                                    "Eu não queria ter que falar com ela. Eu não sei como ela vai lidar com isso."

                                    "Ficar de papo com a [g] só ia piorar minha situação."
                "Melhor eu só ficar aqui":


                    "Nah... vou ficar por aqui mesmo."

                    "Não ia ser certo invadir a intimidade delas... eu sou um cavalheiro... além disso..."

            "Assim eu não corro nenhum risco desnecessário... mais do que eu já corri..."

            "O lance da Fen Ju é sério... eu preciso ficar de olho nelas."

            if sayuri_namoro:

                show black with dissolve

                hide black with dissolve

                mc "Opa... que sono..."

                s "Oi?"

                mc "Hm?!"

                s "Tá acordado?"

                mc "O-oi! T-tô."

                s "Posso..."

                mc "O-o-opa!"

                scene black with dissolve

                scene say7_p43 with Dissolve(1.0)

                mc "Que visita boa."

                s "Eu tava com tanta vontade de ver você."

                menu:
                    "Eu também tava.":


                        mc "Eu quer tava! Não queria te incomodar, mas queria muito ver você."

                        s "Eu não queria que a [fen] ou a [g] visse a gente, mas não aguentei ficar lá sabendo que você tava aqui em casa."

                        mc "Hehe... que bom."
                    "E a Fen Ju?":


                        mc "E a Fen Ju?"

                        s "Ela tá dormindo no meu quarto."

                        mc "Ah..."

                        s "Não precisa se preocupar. Ela tá bem. A [g] deu um jeito de animar ela... no maior estilo Júlia, claro."

                        mc "Haha... Legal."

                        s "Mais ou menos 'legal' haha..."

                s "E-eu... eu não vou poder ficar muito, então só queria ver como você tava mesmo."

                mc "Ah..."

                s "É p-perigoso."

                mc "Eu entendo... não quero complicar as coisas pra você. Só queria ficar com você um pouco."

                s "A-ah! Eu também queria... mas se alguém ver a gente eu não sei o que eu ia fazer..."

                mc "Sei..."

                s "E-então... b-boa noite. Vou tá no quarto pensando em você."

                mc "S-sayuri-"

                s "Hm?"

                menu:
                    "Deixar ela ir":


                        mc "N-nada. Boa noite."

                        s "Pra você também, [mc]."

                        mc "Beijo."
                    "Puxar ela pra você":


                        mc "Ainda não!"

                        scene say7_p44 with vpunch

                        pause

                        s "Hm-Hm!!"

                        mc "Desculpa, mas eu não vou aguentar deixar você ir sem me aproveitar de você um pouquinho..."

                        s "A-ah... hmm..."

                        mc "Hmm..."

                        mc "Você é muito gostosa."

                        s "Aah..."

                        mc "Vamos continuar?"

                        s "N-não! P-por favor!"

                        mc "Tudo bem... eu vou deixar você ir agora..."

                        s "Hm..."

                        mc "Boa noite, gata."

                        s "A-ah..."

                s "Pra você também, [mc]."

                mc "Beijo."

                s "B-beijo."

                scene black with Dissolve(1.0)

                scene say7_p31 with Dissolve(1.0)

                "Uou... que legal que a Sayuri veio aqui. Minha recompensa por ter ficado hehe..."

                "Não vejo a hora de poder ficar com ela pra valer... continuar o que a gente começou essa noite..."
            else:


                "Talvez se eu e a Sayuri tivesse juntos... agora seria um bom momento pra gente se ver..."

                "Pelo menos é que o eu gostaria que acontecesse... mas né..."

            "Hoje foi um dia e tanto..."

            show black with dissolve

            hide black with dissolve

            "Uaaah..."

            scene black with Dissolve(2.0)

            $ tempo = 2



            if carro:

                scene carro_mc_cidade2 with Dissolve(1.0)
            else:


                scene mc onibus with Dissolve(2.0)

            pause

            "Passar a noite lá foi bem legal... elas ficaram bem agradecidas e até encomendaram café da manhã pra mim..."

            "Muito bonitinhas..."

            "Mas e ontem?"

    "O que será que a [fen] quis me dizer? E por que será que ela tava se cortando?"

    "Acho que eu tinha entendido tudo errado..."

    "Eu preciso conversar com a [s] sobre tudo isso. E talvez a mestra... ela sabe sobre o biombo... deve saber de tudo."

    "E se eu precisar acabar com tudo isso. Eu vou explodir eles denunciando tudo isso pra mundo."

    "As coisas não vão ser fáceis..."



    python:

        del s8_sayuri
        del s8_sayuri1
        del s8_sayuri2
        del s8_sayuri3
        del s8_julia
        del s8_julia1
        del s8_julia2
        del s8_julia3
        del s8_fenju

    $ v41_fim = True

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("v41_fim","final","local")

    scene black with Dissolve(3.0)

    $ tempo = 4

    call checa_final from _call_checa_final_10

    jump call_cidade

label sayuri_evento9_pre:

    $ estou_na_cidade = False

    $ sayuri_e9 = "pre"

    "O que foi aquilo com a [fen]?"

    scene black with dissolve

    scene ape_tv with Dissolve(1.0)

    "Eu não consigo tirar aquela imagem da cabeça. Ela se cortando no canto da sala da [s]..."

    "Como que as coisas chegaram nesse ponto? Uma jovem daquela... se mutilando dessa forma!"

    "Não é possível que nenhum adulto tenha visto isso! Ninguém se preocupa com a garota, caralho?!"

    if sayuri_namoro:

        "A [s] é minha namorada... ela tá no meio disso tudo. Será que eu vou colocar minha relação com ela a perder?"
    else:


        "Eu e a [s] não tamo namorando. Não tem nada lá que eu vá perder."

    "Eu tenho que fazer alguma coisa! Seja como jornalista, seja como uma pessoa decente!"

    mc "Alguém nesta ilha tem que ter a cabeça no lugar! Um pingo de juízo pelo menos!"

    "Se eu chegar no fundo disso... vai ser a maior matéria que eu já descobri. A maior pauta da história da revista."

    if sayuri_namoro:

        "E pode ser o fim do meu namoro com a [s]..."

    "Eu preciso pensar muito bem no que eu vou fazer agora. Isso com certeza vai mudar minha vida de uma forma que não dá pra voltar atrás."



    mc "Por onde eu vou começar?"

    "O primeiro passo é falar com a [s]..."

    "Ela é a pessoa que tá comigo desde o começo. Foi por causa dela que eu descobri todo esse enrosco da Cidade Chinesa."

    "Vai ser uma conversa difícil... mas não tem como eu fugir."

    "Eu vou até a {b}Cidade Chinesa de manhã{/b} e tirar tudo a limpo com a [s]."

    jump call_cidade

label sayuri_evento9:

    python:
        renpy.notify("A Pixie salvou esta memória. Use o menu Encontros para voltar aqui.")
        renpy.save("s9_save", extra_info="s9_save")

    $ iconchefe += 1

    $ estou_na_cidade = False

    $ sayuri_e9 = "evento"

    "A [s] deve tá no templo treinando a [fen]. Eu preciso falar com ela. Mas precisa ser sozinha. Não quero que a menina escute."

    "???" "[mc]."

    mc "Hm?! Quem é?"

    "???" "Venha aqui."

    mc "O senhor!"

    scene black with dissolve

    play sound som_35_passos

    pause 1.0

    scene sayuri9_bao1 with Dissolve(1.0)

    pause

    chi "Vejo um brilho diferente nos seus olhos. O que você veio fazer aqui hoje?"

    menu:
        "Eu vim tirar tudo a limpo.":


            chi "Hmm... obrigado por confiar em mim e revelar. Mas você não precisava nem dizer."
        "Não te interessa, velho.":


            chi "Ora, vejo que está determinado. Não quer contar com a ajuda deste velho?"

            mc "São coisas particulares. Foi mal."

            chi "Você não precisa nem dizer, garoto."

    chi "Finalmente chegou a hora. A hora final."

    mc "Hora final?"

    chi "Desde a primeira vez que eu te vi com a Ai Fen... eu sabia que seria você a fazer isso."

    chi "Apenas alguém que veio de fora, fora do bairro, fora da cidade, fora deste mundo, poderia fazê-lo."

    mc "Você tá fazendo isso parecer maior do que é."

    chi "Pelo contrário. Você não entende a dimensão que suas ações terão na vida de milhares de pessoas."

    mc "N-não! Como assim?!"

    menu:
        "Eu estou fazendo isso pela Sayuri.":


            mc "A [s] é que me importa. Eu não tô nem aí pra essa história de milhares de pessoas."

            chi "Movido pela paixão..."

            if sayuri_namoro:

                mc "A gente tá namorando e eu vou até o fim por ela."
            else:


                mc "Ela é uma grande amiga. Não é paixão. É gostar de verdade de alguém."
        "Eu faço isso pela Fen Ju.":


            mc "Eu quero salvar a Fen Ju dessas pessoas horríveis. Antes que aconteça o pior com ela!"

            chi "Você tem um bom coração..."
        "Eu tô fazendo isso porque sou jornalista.":


            mc "Eu quero chegar no fundo dessa história. Desvendar esse mistério. Esse é meu trabalho."

            chi "Entendo... então essa é sua motivação."

    chi "Eu acredito no que diz. E é por isso que repito: você não tem ideia de como tudo isso é grandioso."

    chi "Suas ações vão provocar uma mudança profunda em toda a Cidade Chinesa."

    chi "Não acredita? Como uma pessoa pode fazer tudo isso? Essa é sua dúvida?"

    chi "Pois pense. Em um castelo de cartas, remova uma das cartas da base e tudo desmoronará."

    chi "Você está lidando com um dos pilares de toda nossa comunidade. Se você derrubá-lo, tudo cairá sobre nossas cabeças."

    mc "E-eu não imaginava... então a Sayuri... ela é uma peça fundamental assim?"

    chi "Ela... a jovem [fen] e a aquela que está sobre elas."

    mc "A Mestra..."

    chi "A senhora é uma Imortal. Uma das cabeças que comanda a Cidade Chinesa. Talvez a mais importante hoje."

    chi "Não importa qual você diga ser seu objetivo, para atingí-lo você terá que passar por ela."

    chi "Ela guarda as chaves do cofre que guarda todas as verdades e todas as vidas enclausuradas."

    mc "Todas as vidas... como assim?"

    chi "O que eu quero dizer é... não existe saída para a [s] ou para a [fen] sem que você consiga as chaves."

    chi "As chaves estão com Jidao. Você precisa delas. Esse precisa ser seu primeiro passo."

    mc "Jidao... esse é o nome da Mestra. Eu preciso falar com ela..."

    menu:
        "Os olhos delas, [chi]...":


            pass

    mc "[chi]... o que fizeram com a [fen]... os olhos dela..."

    scene black with dissolve

    scene sayuri9_bao3 with Dissolve(1.0)

    pause

    chi "Eu lhe disse isso uma vez, garoto. Não veja tudo com seus próprios olhos. A Cidade Chinesa vive uma realidade só dela."

    chi "Não nos cabe julgar. Muito menos condenar os outros pelo que fizeram. Nosso dever é estar bem com nossa própria consciência."

    chi "Eu vi o que você viu. Há dezenas de anos. E eu não julguei meus irmãos e minhas irmãs. Eu tomei o meu caminho."

    chi "Eu renunciei a tudo o que tinha. Ne tornei um vendedor de lamén, sem espólios ou condecorações."

    chi "Entretanto, minha consciência agora está limpa. Deixei a vida cheia, para viver cheio de vida."

    chi "Você terá que fazer o mesmo. Se você quer chegar ao fim desta história cheio de vida, você precisa entender isso."

    chi "A xícara cheia não aceita mais líquido. Esvazie sua xícara, para que você possa enchê-la com o que virá."

    chi "Você entende isso? Pode prometer isso para mim?"

    "Prometer que não vou fazer nada? Mas e se o que a Mestra Jidao faz... a [s] faz... for terrível?"

    "Eu vou permitir que tudo continue assim? Como eu vou ficar de consciência limpa assim?"

    menu:
        "Sim. Eu não vou me vingar e nem acusar ninguém.":


            mc "Tudo bem... eu vou seguir seu conselho e não fazer nada... mas eu não tenho certeza se isso é o certo, [chi]..."

            chi "Eu agradeço. E garanto que será o melhor para você também."
        "Não posso prometer isso.":


            mc "Desculpa, [chi], mas eu não tenho como garantir isso pra você agora. Eu preciso ver com meus próprios olhos antes."

            chi "Não deixe que seu orgulho seja sua ruína."

    chi "Existem mais camadas do que você pode imaginar, [mc]."

    chi "Quando você achar que entendeu, ainda existirá toda uma caverna de escuridão."

    chi "Você vai questionar a própria realidade antes de chegar ao fim."

    mc "Você tá falando da lenda da He Xiangu?"

    chi "E não é?"

    if xiang_escape >= 6:

        mc "Você sabe que eu fui até o final dessa história... eu vi tudo acontecendo na minha frente."

        chi "Lá eu te perguntei o que você achava. Será que você estava certo?"
    else:


        mc "Eu ainda não terminei todo esse rolo..."

        chi "Você ainda verá muita coisa aqui, jovem... se você for atrás."

    scene black with dissolve

    scene sayuri9_bao2 with Dissolve(1.0)

    pause

    mc "Então... você quer sugerir que a história é verdadeira? Que realmente existe uma imortal?"

    chi "Eu apenas quero que você esvazie sua xícara. Permita que uma nova realidade seja derramada sobre você sem transbordar."

    mc "Não sei... o mundo parece muito descoberto já. Se existissem imortais... todo mundo saberia."

    chi "Não seja tolo. Não é tão simples como você imagina. Não é preto ou branco, [mc]. Entre os dois existe uma gama de cores."

    chi "Um filósofo do seu ocidente disse que quanto mais sabia, mais sabia que nada sabia. Essa é a postura da xícara vazia."

    mc "Não sei se eu entendi... mas eu vou lembrar das suas palavras, velho."

    chi "Você também precisa do seu tempo. Eu falei demais. Agora vá. Fale com Jidao. É a única forma."

    mc "E eu lá tenho coragem pra isso?! E mesmo que eu tivesse... como eu vou chegar até ela?"

    mc "Você deve saber que eu não posso acessar aquela área especial dos escolhidos."

    chi "E mesmo sem poder você esteve lá mais de uma vez, não esteve..."

    mc "Bem... talvez... mas..."

    chi "Você saberá o que fazer. Estarei de olho em você, jovem."

    chi "Você andou muito até aqui. Falta o momento final. Não desista."

    mc "Ok... eu vou chegar no fim disso. Eu não vou desistir."

    mc "Vou procurar a Mestra Jidao e falar com ela. Saber a verdade e pegar essas tais chaves."

    chi "Estarei aqui se precisar de mim. Mas pouco posso fazer além de ensinar."

    chi "Foi esse o papel que o destino me deu. É o poder me sobrou depois de todos esses anos. Até mais, [mc]. E tenha cuidado."

    mc "Cuidado?"

    chi "Agora saida daqui que eu tenho um cliente para atender."

    scene black with dissolve

    play sound som_35_passos

    scene chinatown geral with Dissolve(1.0)

    mc "Ei! Volta aqui! Cuidado com o quê?!"

    "Legal... como se a situação já não fosse tensa, ele tinha que sair depois de soltar uma bomba dessas. 'Cuidado'... velho maldito."

    "Então ele acha melhor eu falar com a Mestra Jidao antes de decidir tudo com a Sayuri?"

    "A gente podia só sair correndo desse lugar aqui, não podia? Seria bem mais fácil..."

    "Eu tenho que pensar sobre tudo isso..."

    scene black with dissolve

    scene chinatown caminho with Dissolve(1.0)

    pause

    "Se tudo der certo ela engravidaria e eu poderia ter três filhos..."

    scene black with dissolve

    scene chinatown templo_lateral with Dissolve(1.0)

    "Mas... e se ela me mata? Daí eu não teria filhos..."

    mc "HUH?!"

    "Eu tava tão concentrado que vim andando até aqui..."

    "???" "[mc]!"

    mc "Quem é agora me chamando assim..."

    scene black with dissolve

    scene sayuri9_fen1 with Dissolve(1.0)

    pause

    fen "Oi..."

    mc "[fen]... você tá aí? Você e a Sayuri tão treinando?"

    fen "Não. Já acabou, mas ela me deixa aqui pra eu deixar meu corpo sempre pronto."

    mc "O treino é puxado, né..."

    fen "Eu tô acostumada. E... você sabe que eu nem precisava treinar tanto assim..."

    mc "[fen]... você tá falando..."

    fen "[mc]... desculpa pelo que aconteceu aquela noite. Eu não pensei que você ia me ver lá..."

    mc "Não precisa pedir desculpas por causa disso, boba."

    fen "Preciso, sim."

    mc "Tô falando que não precisa. É bom desabafar."

    fen "Não. Não é por isso."

    mc "Hm?"

    fen "Agora que você sabe meu segredo, a Mestra provavelmente vai querer te matar."

    scene black with dissolve

    scene sayuri9_fen2 with hpunch

    pause

    mc "QUÊ?!!"

    fen "Me desculpa! Eu não pensei nisso na hora!"

    mc "Você tá falando que é um segredo tão sério que ela ia me matar por causa disso?!"

    fen "Sim... ninguém sabe disso..."

    menu:
        "Eu nem sei direito qual é o segredo!":


            mc "Eu juro que nem entendi direito qual é o segredo!"
        "Eu juro que não conto pra ninguém!":


            mc "Eu prometo que não vou contar nada pra ninguém!"

    fen "I-isso não faz diferença, [mc]..."

    fen "Se ela descobrir que você sabe, com certeza ela vai ter que tomar providências..."

    mc "Então eu tô fodido."

    fen "Por isso que eu não posso sair daqui também... elas têm medo que alguém descubra."

    fen "Mas eu sou egoísta! Eu não consigo ficar quieta! Eu coloco as pessoas em risco e agora vou te matar!"

    scene black with dissolve

    scene sayuri9_fen3 with Dissolve(1.0)

    pause

    fen "D-droga! {i}Buaaahhh{/i}"

    mc "Ei, ei! Calma..."

    mc "Ela não sabe nada ainda, sabe?"

    fen "N-não... mas se ela me perguntar eu não posso mentir... ou ela..."

    "Ferrou. O que eu falo pra ela?"

    mc "Por que você não pode mentir? É uma mentirinha pequena... pra me salvar..."

    fen "Porque... se eu mentir... e-eu..."

    mc "Entendi. Ela vai te machucar, né?"

    fen "N-não... é..."

    "E agora? Eu não quero forçar ela, mas é da minha vida que a gente tá falando aqui..."

    menu:
        "Não se preocupe. Eu vou dar um jeito.":


            mc "Não fique preocupada... eu sou adulto. Eu vou saber me proteger."

            fen "T-tem certeza?"

            mc "Claro. Eu não quero que você minta, tá?"

            fen "Tá..."
        "Você tem que mentir. A gente precisa se ajudar.":


            mc "[fen]... eu sei que isso é complicado, mas a gente precisa agir juntos. Você tem que me proteger."

            fen "M-mas..."

            mc "Ela nunca vai descobrir a verdade. Você pode fazer essa por mim por favor?"

            fen "Tá..."

    mc "Agora, eu preciso entender tudo isso direito. Porque eu tô pensando em falar com a Mestra Jidao."

    fen "Huh..."

    fen "F-falar com ela? Você quer que fique mais fácil dela te pegar? Você quer despistar ela?"

    mc "N-não! Nem uma coisa nem outra... esquece essa história dela me matar."

    mc "O [chi] me disse que só falando com ela eu vou conseguir ajudar você e a Sayuri. Então..."

    fen "O [chi] é inteligente... ele sempre tá certo. Mas eu não sei, não..."

    mc "Eu preciso saber a verdade. O segredo por trás de tudo. Da sua habilidade, dos seus olhos, dos seus machucados..."

    mc "Dá pra ver que tem alguma coisa acontecendo. Tá na cara isso. Mas eu não vou conseguir decifrar tudo sem ajuda."

    scene black with dissolve

    scene sayuri9_fen4 with Dissolve(1.0)

    pause

    fen "[mc]..."

    mc "Você viveu muita coisa ruim aqui. Coisa que uma jovem da sua idade não devia ter passado."

    mc "E não tinha ninguém pra te ajudar. Mas agora eu tô aqui. Você pode confiar em mim."

    mc "Juntos a gente pode acabar com tudo isso."

    mc "O que você me diz? Posso contar com sua ajuda?"

    fen "..."

    fen "Não."

    mc "Não?! Por quê?!"

    fen "Eu não posso te contar isso. Eu sei que eu fiz errado naquela noite. Mas eu não tava pensando direito."

    fen "Eu nunca vou poder revelar essas coisas. Eu iria contra a minha professora... eu não posso."

    mc "[fen]... eu sinto que eu tô tão perto de descobrir tudo. Mas eu preciso de ajuda! Eu preciso da sua confirmação!"

    fen "D-desculpa! Eu não posso!"

    menu:
        "Mesmo depois de tudo o que eles fizeram?!":


            mc "[fen]! Não é questão de honra aqui! É muito maior que isso! É parar toda essa violência!"

            fen "N-não! Elas confiam em mim! Eu prometi que nunca ia falar! Por favor, [mc]!"

            mc "Não seja cabeça dura! Eu tô do lado certo! E eu preciso da sua ajuda! Para de defender eles!"

            fen "Não grita comigo! Eu já falei que eu não vou falar!"

            mc "Droga, [fen]!"

            fen "D-desculpa..."

            mc "Tudo bem..."
        "Tudo bem... eu fico sem a resposta...":


            mc "Se você não pode falar... tudo bem... eu fico sem sua confirmação. Eu não quero te forçar."

            fen "Obrigada... e desculpa por decepcionar você..."

            mc "De jeito nenhum. Você quer ser uma mulher honrada. Eu respeito isso. Agora..."

    mc "Eu preciso te falar uma coisa."

    mc "Como eu posso aceitar a Cidade Chinesa se eles fazem mal pra uma garota da sua idade?"

    mc "Dizem que eu tenho que manter a cabeça aberta, mas o que é errado é errado em qualquer lugar, [fen]."

    mc "Olha pra você... essas feridas... no rosto... no corpo todo... eu não consigo aceitar isso!"

    fen "Não... não é isso..."

    mc "Não é o quê? Quando eu vi você com a faca se cortando na sala da [s], eu fiquei totalmente confuso. É sobre isso?"

    fen "É..."

    mc "Você tá dizendo que foi você que se machucou? Tudo?"

    fen "..."

    scene black with dissolve

    scene sayuri9_fen3 with Dissolve(1.0)

    pause

    fen "Dói..."

    mc "Hm?"

    fen "N-não..."

    mc "Pode me falar, [fen]. Eu sou seu amigo. Eu quero te ajudar."

    fen "Tudo dói... dói demais... o que é um corte perto de tudo o que dói no meu coração, [mc]?"

    fen "Dói porque eu sou uma fraude... que só ganha porque fizeram essas coisas comigo..."

    fen "Dói porque eu queria dançar balé, mas eu sei que eu nunca vou poder fazer isso..."

    fen "Dói porque eu queria trazer honra pra minha família, mas meu coração quer outras coisas."

    fen "E dói... porque eu amo alguém... que nunca vai poder ficar comigo..."

    fen "Quando eu me machuco... é quando eu esqueço a dor do coração. É meu único momento de paz..."

    scene black with dissolve

    scene sayuri9_fen5 with Dissolve(1.0)

    pause

    mc "[fen]..."

    fen "!"

    mc "Obrigado por me contar tudo isso. Eu não consigo imaginar o quanto é difícil pra você."

    mc "Se eu puder... eu vou ser seu amigo pra sempre. E você vai poder me contar sempre que tiver doendo."

    fen "Aaah... hmm... {i}buaahh{/i}"

    mc "Todos nós precisamos de ajuda quando tá doendo. Ajuda dos amigos... ajuda profissional..."

    mc "Se eu puder, eu prometo que eu vou tá sempre do seu lado."

    mc "Eu só posso ser seu amigo, mas eu prometo que vou ser seu melhor amigo."

    fen "Hmmmnng..."

    mc "O que você me diz?"

    fen "T-tudo bem... obrigada, [mc]..."

    mc "A gente vai ser feliz. Eu tenho certeza. Ainda mais você que é tão nova. Tanta coisa vai acontecer ainda."

    mc "Eu queria poder te falar alguma coisa pra fazer você se acalmar, mas eu nem consigo imaginar como é pesado pra você."

    fen "T-tudo bem... eu tô bem..."

    mc "Você é forte. Isso qualquer pessoa vê."

    mc "Então esses machucados... a [s]... não bate em você? Nem a Mestra?"

    fen "E-eu não posso falar sobre isso, [mc]... m-meus treinos são segredo também..."

    mc "Ok..."

    fen "Mas... se você fica mais tranquilo... meus treinos nunca foram o problema. Não é isso, tá?"

    mc "Tem certeza?"

    fen "Não precisa odiar elas e os outros aqui por causa de mim. Eu não quero isso. E eu amo eles de verdade."

    menu:
        "Então eles não maltratam ela. Isso é bom":


            "Então a [s] e a Mestra não maltratam ela. O treino é puxado, mas não acontece agressão. Isso é excelente!"

            "É normal se machucar um pouco em atividade física. Mas os maiores foram causados por ela mesma... que coisa..."
        "Não acredito. A [fen] só tá protegendo eles":


            "A [fen] tem muito respeito por essas pessoas. Eu acho que ela não tá sendo sincera. Ela só quer proteger eles."

            "Pra mim tá na cara que ela apanha. Eu não tenho provas, mas eu acredito nisso."
        "É impossível saber a verdade pelo que ela disse":


            "O que ela falou não garante nem que ela apanha e nem que não apanha. Não dá pra ter certeza de nada."

            "O mistério continua... não é com ela que eu vou conseguir essa resposta."

    mc "Tá... se você tá falando..."

    mc "Eu tenho uma última pergunta. Desculpa encher seu saco, mas não é segredo, não é nada..."

    scene black with dissolve

    scene sayuri9_fen6 with Dissolve(1.0)

    pause

    fen "O quê?"

    mc "Você quer substituir a [s]? Você quer ser uma atleta olímpica?"

    fen "E-eu?!"

    fen "Eu... t-treinei a vida toda pra isso..."

    mc "Não interessa. Você QUER fazer isso?"

    fen "Não é isso... querer não é tudo... as pessoas tão contando comigo... a Cidade Chinesa tá."

    mc "Você ainda é uma adolescente, [fen]. Você não devia tá carregando um peso desse tamanho nas costas. Qualquer um sabe disso."

    mc "Mas não tô falando de obrigação. Deixa eu mudar a pergunta. Se você pudesse escolher... qual seria seu sonho?"

    fen "Meu sonho... hmm... s-se fosse uma outra vida... um outro mundo... meu sonho é ser uma dançarina de balé."

    fen "É... balé... eu adoraria ser uma dançarina... uma artista..."

    fen "Eu não queria competir... porque se eu não competisse, o que fizeram comigo não ia fazer diferença, não é verdade?"

    fen "Os artistas não tão lá uns contra os outros. São amigos, então tudo bem, né?"

    mc "Claro que tudo bem... você é uma garota como qualquer outra, [fen]. O que fizeram com você nunca vai mudar o que tem dentro de você."

    fen "Hm..."

    mc "Valeu por me responder. Saber que você quer fazer balé me dá mais certeza do que eu tô fazendo."

    scene black with dissolve

    scene sayuri9_fen7 with Dissolve(1.0)

    pause

    fen "[mc]... você tem certeza que você vai falar com a Mestra Jidao?"

    mc "Sim... eu tô seguindo o que o [chi] disse."

    fen "Toma cuidado com ela, tá? Ela não é uma mulher normal."

    mc "Como assim? Ela fez a mesma coisa que você?"

    fen "N-não... ela é diferente. Ela tem um poder sagrado que veio dos antepassados."

    menu:
        "Você diz igual a lenda da He Xiangu?":


            mc "Você tá falando que ela tem um poder igual a He Xiangu? A lenda da imortalidade?"

            fen "Isso!"
        "Eu não acredito nessas coisas.":


            mc "Não esquenta. Eu não acredito nesse tipo de coisa. Eu tenhos os pés no chão."

            fen "Isso não é fantasia! É verdade, [mc]!"

            mc "Tudo bem, calma... o que você ia falar?"

            fen "É... escuta..."

    fen "A Mestra Jidao, a espadachim da flor de lótus He Xiangu e o professor Lu Dongbin, o Bao Chang."

    fen "Todos eles se tornaram imortais. Eles são figuras sagradas pra nossa cultura."

    mc "O Bao Chang também?!"

    fen "Eu não entendo... acho que ele não é mais... mas eu escutei a Mestra falando um dia que ele também era."

    mc "Então ele deixou de ser um imortal pra ter aquele carrinho de lámen..."

    fen "É... eu não sei o que aconteceu, mas ele brigou com a Mestra Jidao."

    mc "Ele chama a Sayuri de outro nome... Ai Fen, se eu não me engano. É parecido com o seu nome, né?"

    fen "S-sim... eu também vou ter que mudar de nome."

    mc "Mudar de nome? Por quê?"

    fen "Não sei... mas a professora teve que fazer isso e já me falaram que eu também vou, quando eu for competir."

    mc "Tudo isso fica cada vez mais estranho, [fen]..."

    scene black with dissolve

    scene sayuri9_fen8 with Dissolve(1.0)

    pause

    fen "D-desculpa que eu não posso falar mais..."

    mc "Esquece isso. Eu vou falar com a Mestra e ver se eu consigo chegar no fundo disso."

    fen "S-se você tem certeza... só tome cuidado, [mc]. A Mestra tem poderes..."

    mc "Não se preocupa comigo. Eu vou tomar cuidado, tá?"

    mc "Eu só preciso que você faça uma coisa pra mim."

    fen "C-claro. Eu quero te ajudar em qualquer coisa que eu puder!"

    mc "Lembra aquela vez que você chamou a atenção da He Xiangu pra eu passar pelo portal?"

    mc "Você pode fazer isso de novo por favor? Pra eu poder encontrar a Mestra Jidao?"

    fen "Hmm..."

    menu:
        "Por favor.":


            mc "Por favor, [fen]."
        "...":


            mc "..."

            "Tomara que ela aceite! Por favor... quebra essa, [fen]!"

    fen "Tá."

    mc "Ufa! Valeu..."

    fen "A gente vai fazer igual da outra vez. E toma cuidado, tá?"

    fen "Se ela descobrir... elas vão..."

    mc "Eu prometo que elas não vão descobrir. Elas não vão punir você, tá?"

    fen "N-não se preocupa... vamos."

    scene black with dissolve

    play sound som_35_passos

    scene chinatown caminho with Dissolve(1.0)

    pause

    scene black with dissolve

    play sound som_23_passos1

    scene chinatown portal with Dissolve(1.0)

    fen "Quando você escutar eu falando com ela, você pode passar. Vai rápido, mas não faz barulho."

    mc "Combinado. Deixa comigo."

    fen "E boa sorte com a Mestra. Eu quero ver você de novo, [mc]."

    play sound som_23_passos1

    "Ela realmente tá preocupada comigo... eu não posso decepcionar a Fen Ju. Isso aqui é por ela também."

    fen "Ei! Olha o que eu aprendi a fazer! YAHHH!!!"

    "He Xiangu" "S-senhorita! Tome cuidado!"

    "Essa é minha deixa!"

    scene black with dissolve

    play sound som_23_passos1

    scene chinatown vila_entrada with Dissolve(1.0)

    pause

    mc "Consegui. Seu sacrifício não séria em vão, [fen]."

    "Eu tenho que encontrar a Mestra e dar o fora antes que alguém descubra que foi ela que me ajudou."

    "Não quero nem pensar o que vão fazer com a menina se descobrirem que ela-{nw}"

    $ renpy.vibrate(1)

    scene sayuri9_xiangu1 with hpunch

    "???" "Parado!"

    $ xu_nome = "He Xiangu"

    mc "!!!"

    xu "Esta área é proibida para pessoas comuns!"

    "FODEU!"

    mc "E-eu sei..."

    xu "Diga! O que está fazendo aqui!?"

    mc "Eu vim falar com a Mestre Jidao. Por favor, não me interrompa."

    xu "Como você conseguiu... ah... foi a senhorita, não foi? Diga a verdade!"

    menu:
        "Não! Ela não sabia de nada.":


            mc "Não. Eu estava de olho no portal. Quando ela foi te mostrar o movimento eu aproveitei. Ela não sabia."

            xu "Hmm... então você é um ladrão."

            mc "Não sou um ladrão! Só quero poder falar com a Mestra!"
        "A gente quer salvar todos. Você também.":


            mc "Eu e a [fen] queremos salvar todo mundo aqui! Inclusive você! Ajuda a gente, [xu]!"

            xu "Mancomunados... traindo a Cidade Chinesa..."

            mc "Não! A gente não tá traindo! Por favor, não culpe ela!"

            xu "Ela receberá o tratamento que merece. Isso eu te garanto."

            mc "Espere, [xu]! Me escuta! Só quero poder falar com a Mestra!"
        "Eu não acredito em lendas! Enfia a espada no cu!":


            mc "Eu cansei de toda essa história! Você não manda nada! Você nem sabe usar isso! Pega essa espada e enfia no cu!"

            $ renpy.block_rollback()

            scene sayuri9_xiangu2 with hpunch

            xu "Então esse é o caminho que você escolhe..."

            mc "O que você vai fazer com isso?! Tentar me espetar?! Vem aqui que eu vou te ensinar!"

            xu "Perdoem-me deuses... pois usarei o poder que me foi concedido para matar..."

            mc "Ainda essa palhaçada?"

            xu "Zan... gan... ken..."

            mc "Sério mesmo que você deu um nome pro seu golpe?"

            play sound som_espada

            scene sayuri9_xiangu3 with hpunch

            pause

            mc "!!!???"

            play sound som_espada

            show zanganken with vpunch

            pause

            xu "NI-NO-TACHIIII!!!"

            play sound som_grito

            mc "UUAAAAGHHHH!"

            scene red with hpunch

            $ renpy.full_restart()

    mc "O único lugar que eu posso encontrar ela é aqui! Por favor!"

    xu "Você desrespeita nossa terra sagrada... e ainda quer pedir favores?"

    xu "Se você não pode falar com a Mestra Jidao, é porque existe um motivo sagrado para isso."

    xu "Você não pode negar nossa cultura, nossas tradições, só porque você quer algo."

    "Droga... essa espada..."

    "Se eu tomar uma decisão errada aqui já era. Eu sinto que tem muita coisa em jogo."

    "Eu preciso falar com a Mestra de qualquer jeito! Essa é minha única chance!"

    "Mas eu também não posso morrer aqui! O que eu falo?!"

    menu:

        "Lembra que eu trouxe a Xiang? Eu respeito suas tradições." if xiang_escape >= 6:

            mc "Lembra quando eu trouxe a Xiang? Eu ouvi a história dela... eu falei o [chi], com a Liling e até com você."

            mc "Eu sempre estiveraberto pra escutar toda a história da Cidade Chinesa."

            mc "Se eu acredito nela ou não, vai depender de mim, mas eu sempre respeitei vocês."

            scene black with dissolve

            scene sayuri9_xiangu4 with Dissolve(1.0)

            pause

            xu "Isso é verdade... eu achei incrível sua postura em tudo aquilo..."

            xu "Me fez pensar em muitas coisas... sobre o que está acontecendo aqui."

            mc "Inclusive, o [chi] falou justamente sobre isso... que eu tinha que esvaziar minha xícara."

            xu "Então você está pronto pra respeitar que aqui é um solo sagrado?"

            mc "Eu preciso esquecer o que eu sei e aprender a verdade de vocês."

            mc "Se realmente aqui é um solo sagrado... eu vou dar o fora. Se você ver a Mestra... diga que eu quero conversar com ela."

            xu "Eu vou ver se você merece falar com minha Mestra... não ache que você pode pedir e será atendido."

            xu "Agora saia, antes que eu tenha que tomar uma medida drástica."

            mc "Tudo bem. Eu volto aqui um dia desses pra ver se você fal-"

            xu "Eu entendi. Agora saia."
        "Eu entendi... você tem razão. Eu vou embora.":


            mc "Você tem toda razão... o [chi] falou justamente sobre isso... que eu tinha que esvaziar minha xícara."

            scene black with dissolve

            scene sayuri9_xiangu4 with Dissolve(1.0)

            pause

            xu "Huh..."

            mc "Eu preciso esquecer o que eu sei e aprender a verdade de vocês."

            mc "Se realmente aqui é um solo sagrado... eu vou dar o fora. Se você ver a Mestra... diga que eu quero conversar com ela."

            xu "Eu vou ver se você merece falar com minha Mestra... não ache que você pode pedir e será atendido."

            xu "Agora saia, antes que eu tenha que tomar uma medida drástica."

            mc "Tudo bem. Eu volto aqui um dia desses pra ver se você fal-"

            xu "Eu entendi. Agora saia."
        "A tradição de vocês não passa de uma mentira!":


            mc "Você não enxerga que tá sendo enganada?! Todas vocês! Essa lenda é uma mentira!"

            xu "Claro que você acha isso... todo cheio de si. Cheio de suas próprias verdades."

            xu "Você nunca vai ter humildade pra aceitar algo diferente do que você acredita."

            mc "Eu quero te ajudar! Eu não posso desistir agora!"

            xu "Talvez a única forma de abrir seus olhos seja por meio da minha espada..."

            mc "Você realmente acredita que é a He Xiangu?! Que pode me matar com uma espada?!"

            $ renpy.block_rollback()

            mc "Você ainda não entendeu que tudo isso não passa de uma história pra boi dormir?!"

            scene sayuri9_xiangu2 with hpunch

            xu "Então esse é o caminho que você escolhe..."

            mc "O que você vai fazer com isso?! Tentar me espetar?! Vem aqui que eu vou te ensinar!"

            xu "Perdoem-me deuses... pois usarei o poder que me foi concedido para matar..."

            mc "Ainda essa palhaçada?"

            xu "Zan... gan... ken..."

            mc "Sério mesmo que você deu um nome pro seu golpe?"

            play sound som_espada

            scene sayuri9_xiangu3 with hpunch

            pause

            mc "!!!???"

            play sound som_espada

            show zanganken with vpunch

            pause

            xu "NI-NO-TACHIIII!!!"

            play sound som_grito

            mc "UUAAAAGHHHH!"

            scene red with hpunch

            $ renpy.full_restart()

    mc "Até mais..."

    scene black with dissolve

    play sound som_23_passos1

    scene chinatown portal with Dissolve(1.0)

    "Eu não consegui falar com a Mestra Jidao... será que eu podia ter feito alguma coisa diferente?"

    "Poxa... a [xu] podia quebrar essa pra mim... Ou eu devia ter forçado?"

    "E a [fen]? Será que vai acontecer alguma coisa com ela? Será que eu dei a resposta certa?"

    "Eu preciso {b}voltar aqui no Portal um dia desses de manhã{/b}."

    "A [xu] é minha única chance agora. Pelo menos foi esse o caminho que eu escolhi."

    "Ou será que tem outra forma de chegar lá? Ou eu devo desistir de falar com a Mestra totalmente?"

    "O que eu faço?"

    scene black with dissolve

    $ tempo = 3

    jump call_cidade

label sayuri_evento9_parte2:

    $ estou_na_cidade = False

    $ sayuri_e9 = "parte2"

    "Não tenho como ficar enrolando com essa história. Eu preciso ver isso o quanto antes."

    mc "[xu]!"

    scene black with dissolve

    play sound som_23_passos1

    scene chinatown portal_xiangu with Dissolve(1.0)

    pause

    xu "Você..."

    mc "O-oi..."

    xu "Por que tá com essa cara?"

    mc "Você é minha única chance de falar com a Mestra... você..."

    xu "Veja, [mc]... é esse seu nome, né?"

    mc "S-sim..."

    scene chinatown xiangu_ameaca with vpunch

    mc "Opa."

    xu "Eu sempre achei você um sujeitinho de nariz empinado, sabe?"

    mc "E-eu?"

    xu "Vindo até nossas terras e achando que tudo precisa ser como você acha ou é faz de conta. Como se sua cabeça comandasse o mundo."

    xu "Existem realidades diferentes da sua. Ângulos que sua cabeça de vento nem podem começar a compreender."

    menu:
        "Na minha vida eu tenho que seguir minha cabeça.":


            mc "Mas a gente tá falando da minha vida... as coisas precisam fazer sentido pra mim! Eu só posso olhar com meus olhos!"

            xu "E o que você não vê então não existe? Você vê? Tão cheio de si..."

            xu "E é por isso que eu sempre tive um pé atrás com você. Por conta da sua visão limitada."

            xu "Você nunca entenderia nossas vidas."

            xu "Só que... aconteceu uma coisa. Quando você aceitou que a Vila dos Escolhidos é um local sagrado e foi embora..."
        "Eu sei. O mundo é grande demais pra eu saber tudo.":


            mc "Eu sei... o mundo é tão grande. É impossível que eu saiba tudo... eu preciso aceitar isso."

            xu "S-sim... eu... você realmente parece que mudou sua postura..."

            mc "Se eu não entender que eu não sei, como eu vou aprender coisas novas?"

            xu "Exatamente. Igual quando você aceitou que a Vila dos Escolhidos é um local sagrado e foi embora..."

    scene black with dissolve

    scene sayuri9_xiangu5 with Dissolve(1.0)

    pause

    xu "Foi a primeira vez que eu vi você reconhecendo nossa verdade, nossa cultura."

    xu "'Aquele idiota que se acha tem salvação'. Foi o que eu pensei na hora."

    xu "E foi por isso que eu falei com a Mestra. Naquela hora você me mostrou que você merecia."

    mc "V-verdade?! Obrigado!"

    xu "Tenha calma. Eu fiz isso porque eu posso ver que você tem sua verdade."

    xu "Eu falei com ela e ela aceitou."



    mc "Muito obrigado! Eu prometo que eu vou me comportar!"

    xu "É o mínimo que eu espero. Você vai poder entrar na Vila desta vez."



    xu "Ela disse que tem algo para te dizer. Algo sobre tudo o que você tem feito."

    mc "Ela... é... disse nesse tom ameaçador?"

    xu "Acredito que foi exatamente neste tom que ela falou."

    mc "Você acha que ela aprova o que eu fiz aqui?"

    xu "Não. Acho que ela desaprova veementemente."

    mc "Foi o que eu pensei mesmo..."

    xu "Você só tem esta chance. Se for covarde, perderá sua única oportunidade de falar com ela pra sempre."

    xu "E então?"

    menu:
        "Eu aceito, né?":


            mc "O que eu posso fazer? Você não me deixou outra escolha."

    xu "Você pode fugir e nunca mais aparecer. Parar de querer enfiar sua verdade nas pessoas daqui. Nosso bairro vai muito bem sem você."

    mc "Eu não quero mexer com a cabeça de ninguém. Só quero saber a verdade."

    xu "Porque você é um jornalista?"

    menu:
        "Sim. Esse é meu trabalho.":


            mc "Meu trabalho como jornalista é chegar na verdade dos fatos. Descobrir o que tá escondido."

            mc "Eu não vou parar enquanto eu não descobrir tudo o que vocês têm aqui."
        "Não. É pelas pessoas daqui.":


            mc "Não tem a ver com o trabalho. Eu quero ajudar a [s], a [fen] e até você."

            xu "Eu não preciso da sua ajuda. Eu não estou em perigo."

            mc "Você perguntou e eu respondi."
        "Não te interessa.":


            mc "Você não é muito xereta, não?"

            xu "A-ah!"

    scene black with dissolve

    scene sayuri9_xiangu6 with Dissolve(1.0)

    pause

    xu "Hmf... cada um com seus objetivos. Eu posso respeitar uma pessoa que tem um objetivo. Todos nós temos nossa missão."

    mc "Sua missão é ficar aqui? Protegendo este portal?"

    xu "Eu sou a imortal He Xiangu. Eu sou um símbolo para as pessoas que vivem aqui. Esse é meu destino desde séculos atrás."

    mc "Eu não sei o que pensar sobre isso... mas se você tá feliz assim, é o que interessa, certo?"

    xu "Nem tudo é sobre felicidade ou prazer. Nós temos deveres e não apenas direitos."

    mc "Não é a primeira vez que eu escuto alguém falando isso aqui..."

    xu "Aquele que só faz o que quer, é escravo de seus desejos. Para ser livre, é preciso conseguir fazer o que não quer."

    mc "Hmm... parece um paradozo... mas faz sentido..."

    xu "Eu avisarei a Mestra Jidao que você está aqui. Ela te encontrará no gazebo no centro da Vila dos Escolhidos."

    xu "E, garoto... se você faltar com respeito com a Mestra... ela não terá a paciência que eu tive com você até hoje."

    xu "Ela é a líder de nossa comunidade e de todos os chineses aqui no país. Trate ela com o respeito que ela merece."

    mc "F-farei isso..."

    xu "Pode passar. Você sabe onde o gazebo fica, certo? Não tente nenhuma gracinha."

    play sound som_23_passos1

    scene black with dissolve

    scene chinatown portal with Dissolve(1.0)

    "'Garoto'... do jeito que ela fala parece que ela é uma velha..."

    "Bom, deixa isso pra lá. Preciso manter a calma e o foco. Bora."

    play sound som_23_passos1

    scene black with dissolve

    scene chinatown vila_entrada with Dissolve(1.0)

    pause

    play sound som_23_passos1

    scene black with dissolve

    scene chinatown vila_gazebo with Dissolve(1.0)

    pause

    mc "É aqui... a hora final."

    "Chegou a hora de descobrir tudo e dar um jeito de livrar todas essas pessoas dessa mentira."

    "Ela deve tá puta pelo que eu fiz. Eu me intrometi na vida da [s] e da [fen]. Baguncei tudo."

    "Mas eu não posso deixar a peteca cair agora. Eu tenho que ser firme."

    "Por mais poderosa que essa mulher seja, ela tá fazendo mal pra elas. Isso tem que parar."

    "Mas o [chi] também falou pra eu não julgar... merda... como eu vou abordar a situação?"

    play sound som_23_passos1

    "???" "Então você teve coragem de aparecer."

    $ mes_nome = "Mestra Jidao"

    mc "S-senhora..."

    scene black with dissolve

    scene sayuri9_mestra1 with Dissolve(1.0)

    pause

    mes "Você sabe que está em solo sagrado, não sabe? Que está na presença de uma imortal."

    mc "S-sim..."

    mes "Então trate-me da forma correta. Curve-se."

    label s9_p1:

        pass

    menu:
        "Se curvar":


            mc "Sim, senhora."
        "Permanecer ereto":


            jump s9_p1

    mes "Você me tratará com o devido respeito ou eu vou me retirar."

    mc "Certo."

    mes "Entendida sua posição aqui, eu falarei. Você irá escutar com total atenção."

    mes "Você tem sido um problema para minhas discípulas nos últimos tempos. E isso tem me desagradado."

    mes "Portanto, cesse sua relação imediatamente com as duas e nunca mais apareça na Cidade Chinesa."

    mes "Desobedecer este simples comando resultará em punição. Estamos entendidos?"

    "Por que cada frase dela parece que eu tô sendo atingido por um tiro de escopeta?"

    mc "S-senhora..."

    mes "Estamos entendidos, garoto?"

    label s9_p2:

        pass

    menu:
        "Sim, senhora.":


            mc "Sim, senhora."
        "Não. Calma!":


            jump s9_p2

    "O que eu tô falando?! Por que eu não consig-"

    mes "Nossa reunião chegou ao fim. Remova-se da Vila dos Escolhidos o quanto antes. Sua presença desonra nossos antepassados."

    scene black with dissolve

    scene sayuri9_mestra2 with Dissolve(1.0)

    pause

    mes "Até nunca mais."

    "Eu não disse nada do que eu queria! Eu tô paralisado! Eu não consigo nem olhar pro rosto dela direito!"

    "Essa energia... ela realmente é uma imortal?!"

    "Calma! Eu preciso! Eu tenho que falar alguma coisa! Força, [mc]!"

    "..."

    "Não consigo! MERDA! Por que eu não consigo?! O que eu fiz de errado?!"

    "Eu vou desistir de tudo por que eu nem tenho coragem de tentar?! Eu vou deixar minha vida passar assim sem eu fazer nada?!"

    "Eu não quero desistir sem tentar! Pelo menos tentar! Eu preciso fazer alguma coisa!"

    "Alguma coisa tem que me ajudar. Alguma coisa dentro de mim! Alguma coisa que eu acredito! Eu só tenho UMA chance!"

    menu:

        "Pelo amor que eu sinto pela [s]!" if sayuri_namoro:

            $ renpy.block_rollback()

            "Tudo o que eu sinto pela [s]! Eu preciso focar nisso!"

            "Eu não quero que nossa história acabe assim! Eu não quero dar adeus sem fazer nada!"

            "SAYURI!!! POR FAVOR ME AJUDE!!!"
        "Por tudo o que eu vivi na capital!":


            $ renpy.block_rollback()

            "Eu não sou mais aquele idiota inocente que chegou na capital! Eu passei por muita coisa nesse inferno!"

            "Eu enfrentei muita gente e sofri pra caralho! Eu não sou mais um pateta medroso!"

            "TUDO O QUE EU VIVI ME FEZ UM NOVO HOMEM PORRA!!"
        "Pixie! Me ajuda!":


            $ renpy.block_rollback()

            "Pixie! Se você existe de verdade! Por favor me ajude!"

            "Eu nunca fui totalmente com sua cara, mas eu preciso de você agora! Por favor!"

            play sound som_magia

            show white with dissolve

            hide white with dissolve

    "AAAGHH!!!"

    menu:
        "SENHORA! ME ESCUTE!!!":


            pass

    scene sayuri9_mestra3 with hpunch

    pause

    mes "!"

    mc "..."

    mes "Nossa conversa terminou. E não eleve seu tom de voz quando se dirigir a mim."

    mc "D-desculpa. Eu pedi pra [xu] falar de mim, porque eu preciso falar com a senhora."

    mes "Nós já falamos tudo o que tínhamos a dizer. Eu tenho outros afazeres que requerem minha atenção."

    mc "Eu ainda não consegui falar com a senhora."

    mes "Nunca vi alguém com tamanha petulância..."

    mes "Realmente é muito atrevido. Não é à toa que tem causado tanto tumulto aqui."

    mes "Nossa conversa termina quando eu digo. Seus interesses não têm qualquer valor neste solo sagrado. Muito menos para mim."

    mc "A senhora tá errada."

    mes "Como é?! Que audácia!"

    mc "Eu e a [s] temos uma ligação mais forte do que a senhora imagina."

    if sayuri_namoro:

        mc "Nós estamos namorando."

        mes "Você fala sério? A [s] não tem o direito de namorar! Ela vai responder por isso!"
    else:


        mc "Nós temos uma amizade de verdade. Real."

    mc "Eu me envolvi com ela, com a irmã dela, com a [fen]... não vai ser tão simples você apagar minha memória."

    scene black with dissolve

    scene sayuri9_mestra4 with Dissolve(1.0)

    pause

    mes "Você é o sujeito mais atrevido que eu vi nos últimos anos. Você não nota minha autoridade?"

    mc "A s-senhora não imagina... e-eu quase nem consegui abrir a boca..."

    mes "Mesmo assim, continua abrindo... como se houvesse algum valor naquilo que diz."

    mc "Eu falo sério. Tudo começou de forma inocente, eu querendo uma pauta pra revista."

    mc "Descobri sobre uma tal atleta fuçando o celular de uma famosa..."

    mes "Mesquinho..."

    mc "Eu sei... eu não me orgulho disso. Mas eu fiz o que eu tinha que fazer. Era isso ou ser demitido."

    mes "Morrer com honra é muito melhor do que viver na desgraça. Se soubesse disso não teria errado."

    mc "O-ok... voltando... Tudo começou assim, mas as coisas foram acontecendo e eu e a [s] não somos mais conhecidos."

    if sayuri_namoro:

        mc "Eu realmente amo ela e quero ficar com ela."
    else:


        mc "Ela é uma das minhas melhores amigos hoje."

    mc "E eu acho que ela sente o mesmo por mim."

    mes "Eu nunca concordarei com as palavras de um... ordinário. Não sei por que me diz tudo isso."

    mc "Quero dizer... eu tenho mais valor pra senhora do seu lado do que longe daqui."

    mes "Está tentando me subornar?"

    mc "C-claro que não! Só quero dizer que a senhora pode me usar."

    mes "Que valor você teria para mim? Responda."

    mc "Você sabe que eu tenho uma influência sobre a [s]. Agora também sobre a [fen]."

    mes "Pode parar aí. Entendi onde quer chegar. Não, eu não preciso de você."

    $ mes_nome = "Jidao Quan"

    mes "Eu tenho meus métodos milenares de disciplina. Você parece não saber com quem está falando."

    scene black with dissolve

    scene sayuri9_mestra6 with Dissolve(1.0)

    pause

    mes "Eu sou [mes], a líder dos Oito Imortais, Ba Xian, e meu poder é transformar pedras comuns em ouro puro."

    mc "P-poder?"

    mes "Deixe qualquer rocha, por mais bruta e sem valor que ela seja, e eu transformarei em uma pedra preciosa."

    mc "Ah... foi isso que você fez com a [s]?"

    mes "Não apenas com ela, mas com centenas de outras que passaram pelas minhas mãos."

    mes "Pessoas sem valor algum, sem qualquer relevância ou talento. Eu os transformei em verdadeiros seres humanos."

    mes "Até mesmo você... eu poderia transformar até mesmo um ser ínfimo como você em algo de valor."

    mc "É sobre isso que eu vim falar."

    mes "Como abre a boca... é a primeira vez em muito tempo que vejo alguém ordinário se dirigir a palavra a mim dessa forma."

    mes "Você realmente deve estar ligado em tudo isso... se tem tanta necessidade de colocar para fora tantos absurdos."

    label s9_p3:

        pass

    menu:
        "Desculpa...":


            mc "Perdão, senhora."
        "Não é absurdo! É a verdade!":


            mc "É VERDADE!!!"

            mes "!"

    mes "Muito bem... eu posso ver que você é uma pedra bruta. Mas existe algo dentro. Algo com o que eu posso trabalhar."

    mes "Preste atenção. Eu nunca fiz isso com alguém de fora. Mas você é único, portanto, direi apenas uma vez."

    mes "Faça minhas discípulas seguirem o destino delas e você, também, se tornará ouro em minhas mãos."

    mc "O que você quer dizer com 'ouro'?"

    mes "Tamanha insolência!"

    mc "A-ah!"

    mes "Estou te dando a chance de se tornar ouro por meio do meu poder e você ainda titubeia? Quanta insolência!"

    mc "E-entendi..."

    mes "Diga logo que aceita e você se tornará um dos meus escolhidos. Eu tirarei suas impurezas e então brilhará valioso como o ouro."

    "Uma proposta... ela tá me chamando pro lado dela, se é que eu entendi direito."

    "Ajudar ela a fazer a [s] e a [fen] continuarem o destino delas. Ou seja, parar de encher o saco."

    "Em contrapartida ela vai me transformar em 'ouro'. Eu também serei um Escolhido! Talvez eu até possa viver aqui!"

    "Como eu vou escolher uma coisa dessas assim?! Do nada?! Eu preciso tempo pra pensar!"

    scene black with dissolve

    scene sayuri9_mestra5 with Dissolve(1.0)

    pause

    mes "Perdeu o ímpeto? Acabou a coragem? Por que o silêncio?"

    "Merda! Droga! Cacete! Eu não tenho pra pensar! Eu preciso decidir agora!"

    "A decisão mais difícil! A {b}escolha que vai mudar tudo a partir de agora{/b}!"

    mc "Eu não quero desrespeitar a senhora, Mestra Jidao Quan, mas eu preciso perguntar sobre esse 'ouro'."

    mes "Incrível... o que você tem que me faz perder meu tempo com um mero ser humano comum?"

    mes "Irei indulgenciar... me fale... o que é mais importante para você, que você gostaria de ter?"

    mc "A senhora... estaria desposta a me dar?"

    mes "Eu sou detentora de riquezas materiais e espirituais sem tamanho. E você também pode aproveitar dos meus poderes."

    mes "Não existe limite para o que eu posso te dar. Me peça o que é importante para você. Tudo que quiser."

    "É tentador demais..."

    "Mas o que é mais importante pra mim agora? Bom... ela disse que não tem limite... então posso pedir tudo o que eu quiser."

    "E o mais importante... se eu aceitar, posso me tornar um Escolhido e talvez até um Imortal!"

    "Eu não precisaria me preocupar mais com nada. Adeus revista, adeus aluguel. Serei um ricaço poderoso na Cidade Chinesa!"

    "Será que um futuro desses realmente é possível pra um pé rápido igual eu?"

    "Ok... eu vou pedir pra ela... o que eu quero?"

    "Só tenho que tomar cuidado... se for tentador demais... vai ser difícil resistir."

    label s9_decisao_mestra:

        pass

    menu:

        "Eu quero poder casar com a Sayuri." if not s9_pedido1:

            mc "Eu quero poder viver com a [s]. E ter sua benção vai ser muito importante."

            mc "Eu não quero que você atrapalhe nosso amor. Eu quero ficar com ela, talvez até me casar com ela."

            scene black with dissolve

            scene sayuri9_mestra7 with Dissolve(1.0)

            pause

            mes "Suas intenções com minha discípula são verdadeiras?"

            mc "Sim! Ela será minha esposa e nós viveremos dentro da tradição da Cidade Chinesa! Por favor!"

            mes "Minha discípula herdará minhas responsabilidades. Tenha isso em mente."

            mc "Ela vai ser sua sucessora?!"

            mes "Lapido para que ela abandone seu nome desgraçado e se torne novamente Ai Fen."

            mes "Ela será responsável por esmerar não apenas sua aluna atual, mas todas as rochas que encontrar."

            mes "Ao lado dela, você terá uma grande responsabilidade de manter a Cidade Chinesa em seu primor."

            mes "Aceite estas condições e vocês terão minha benção. Eu permiterei que você despose a jovem Ai Fen."

            mc "Muito obrigado, Mestra Jidao... eu fico tão feliz de saber que eu vou poder ficar com ela!"

            mes "Como Escolhido, eu tornarei você o homem perfeito para auxiliá-la na tarefa de comandar a Cidade Chinesa."

            mes "Seu desejo será garantido. Esse é seu último pedido?"

            "Tem mais alguma coisa que eu quero?"

            $ s9_pedido1 = True
            $ s9_pedidos += 1

            jump s9_decisao_mestra

        "Liberte a Fen Ju. Ela quer ser bailarina." if not s9_pedido2:

            mc "Eu quero que você liberte a Fen Ju! Ela não quer competir! Ela não acha que é justo! Ela-"

            "Melhor eu não falar o que eu sei... eu não quero que ela me mate..."

            mc "E-eu vi ela dançando balé! Ela nasceu pra isso, Mestra Jidao! Por favor! Deixe ela ser feliz!"

            scene black with dissolve

            scene sayuri9_mestra8 with Dissolve(1.0)

            pause

            mes "Aquela fraca... eu sabia que tinha algo errado com ela!"

            mes "A [s] escondeu a verdade de mim. As duas serão punidas de acordo."

            mc "N-não! Eu tô pedindo isso! Deixa a garota ser feliz! A [s] pode competir! Ela é perfeita!"

            mes "Cale-se!"

            mc "..."

            mes "O destino da menina é seguir os passos de sua professora, que também seguirá os meus."

            mes "Não se meta em assuntos que não lhe cabem! Você nunca mais falará disso para mim ou para qualquer outra pessoa!"

            mes "E nem pense em revelar isso naquele monte de papel velho onde você trabalha! Estamos entendidos?!"

            mc "S-sim..."

            mes "A Fen Ju continuará sendo uma atleta e ela trará muita honra para sua casa e para sua família."

            mes "Quando estiver pronta, ela vai perceber quantas pessoas gostariam de ter a oportunidade dela e ser uma atleta respeitada."

            mc "Pelo menos... não brigue com elas..."

            mes "Sua audácia está me cansando! Mas isso pouco me importa. Elas escaparam de uma grande punição graças a você."

            mc "Ufa..."

            "Então eu não vou conseguir salvar a Fen Ju... mas ela vai ser uma atleta incrível."

            "E ela também parecia pronta pra esse destino. Não é algo horrível."

            "Os treinos vão melhorar. A Mestra Jidao me ouviu. Ela parece bem mais razoável do que eu pensei no começo..."

            mes "Agora diga. O que mais você deseja?"

            "Tem mais alguma coisa que eu quero?"

            $ s9_pedido2 = True
            $ s9_pedidos += 1

            jump s9_decisao_mestra

        "Eu quero a verdade sobre tudo!" if not s9_pedido3:

            mc "Eu quero descobrir tudo! Eu quero saber o que acontece com a Fen Ju, com a [s] e tudo por trás da Cidade Chinesa!"

            mc "Claro que daí eu vou fazer parte e nunca vou contar pra ninguém! Mas quando a senhora tiver confiança em mim, quero que me conte."

            scene black with dissolve

            scene sayuri9_mestra7 with Dissolve(1.0)

            pause

            mes "O que isso interessa?"

            mc "Eu preciso saber. Meu senso de jornalista me obriga a descobrir a verdade por trás das coisas. Por favor, senhora."

            mes "Quando você estiver pronto eu revelarei aquilo que eu julgar que você deve saber."

            mc "Obrigado... eu preciso saber a verdade..."

            mes "Você está me ouvindo? Eu já disse que lhe contarei aquilo que eu julgar ser justo."

            mes "Como um Escolhido... e quem sabe até mais... você terá privilégios que nunca imaginou. E carregar a verdade será uma de suas missões."

            mes "Terá acesso ao que lhe couber e deverá proteger e tornar imortal os conhecimentos dos antepassados da Cidade Chinesa."

            mes "Você fará isso com muito orgulho, como um membro de destaque da nossa sociedade."

            mc "Sim. Eu prometo que vou me esforçar para carregar esses segredos e que todos respeitem a história da Cidade Chinesa."

            mes "Não se preocupe que eu vou garantir que você será bem sucedido nesta tarefa."

            mes "Isso é tudo?"

            "Tem mais alguma coisa que eu quero?"

            $ s9_pedido3 = True
            $ s9_pedidos += 1

            jump s9_decisao_mestra

        "Eu quero ser seu amante." if not s9_pedido4:

            mc "Mestra Jidao... eu... tenho algo para pedir... mas não sei se tenho coragem..."

            mes "Fale de uma vez, garoto. Eu estou mandando."

            mc "S-sim... a senhora... tem uma figura incrível... com todo o respeito... eu gostaria..."

            mc "Eu gostaria de dividir a cama com a senhora! Pelo menos uma vez!"

            scene black with dissolve

            scene sayuri9_mestra9 with Dissolve(1.0)

            pause

            mes "Você... realmente é diferente de tudo o que eu já vi neste mundo. Tamanha audácia."

            if s9_pedido1:

                mes "Mesmo pedindo a mão da minha discípula você ainda deseja se deitar comigo? Isso é inescrupuloso."
            else:


                mes "Mesmo que você não estivesse comprometido. Isso é inescrupuloso."

            mc "Me desculpe... eu... estou sendo sincero com a senhora..."

            mes "Sua sinceridade me diverte. E se eu quiser ter com você durante a noite, você saberá."

            mc "Então... tem uma chance?"

            mes "Você será usado por mim como eu bem entender. Assim como seu corpo. Se eu quiser sua visita noturna, você atenderá."

            mc "Sim! Com todo o prazer, senhora!"

            mes "Portanto, esteja preparado para ser usado dessa forma também. Fazendo parte dos meus, você poderá ter essa função."

            mes "E não me importa se você estiver ou não comprometido. Minha palavra é máxima ordem neste lugar. E não aceitarei recusa."

            mes "Você virá até mim e será usado pelo tempo que eu decidir. Fazendo o que eu quiser que você faça."

            mes "Estamos entendidos?"

            mc "C-com certeza."

            mes "O que mais? Tem algo a mais para mim?"

            "Tem mais alguma coisa que eu quero?"

            $ s9_pedido4 = True
            $ s9_pedidos += 1

            jump s9_decisao_mestra

        "Eu aceito sua proposta. Eu quero ser um Imortal." if s9_pedidos > 0:

            "Eu vou mesmo aceitar a proposta dela? Vou desistir de ir contra a Cidade Chinesa?"

            "Vou seguir o conselho do [chi]? Esvaziar minha mente e aceitar a cultura deles? Me tornar alguém importante aqui?"

            if s9_pedidos < 4:

                "Eu ainda posso pedir mais coisas pra Mestra Jidao também."

            "Essa escolha pode mudar tudo pra mim... tudo o que eu vivi até agora com a [s], a [fen] e todos os outros."

            "Aceitar a proposta dela e tentar me tornar um Imortal. É isso que eu quero?"

            menu:
                "Sim. É isso que eu vou fazer.":


                    $ s9_mestra = 2

                    $ renpy.block_rollback()

                    "Está decidido. Não posso voltar atrás agora."

                    mc "Eu quero me tornar um Escolhido nas suas mãos. Por favor, me ensina tudo Mestra Jidao."

                    scene black with dissolve

                    scene sayuri9_mestra9 with Dissolve(1.0)

                    pause

                    mes "Está feito. A partir de agora você renuncia ao seu passado e sua história e será um comigo e a Cidade Chinesa."

                    mes "Suas ações agora são nossas e nossa história é sua. Você faz parte de uma comunidade milenar e imutável."

                    mes "Você passará pelo ritual em momento oportuno posteriormente."

                    mc "Ritual? C-certo..."

                    mes "O que eu quero de você agora é que fale com a minha discípula. Dê as notícias a ela. Ela vai ficar muito feliz."

                    mes "A cerimônia será preparada e você se tornará um Escolhido. Sua vida passada não existirá mais."

                    mes "Bem-vindo, [mc]. Você é um de nós agora."

                    if s9_pedido4:

                        mes "E não se esqueça que uma das suas obrigações será comigo."

                        mc "N-não vou esquecer..."

                        mes "Eu vou te procurar quando você for necessário. Agora vá."

                    mc "Obrigado... eu vou avisar a [s] agora."

                    play sound som_23_passos1

                    scene black with dissolve

                    scene chinatown vila_saida with Dissolve(1.0)

                    pause

                    "Eu sei onde fica a casa da [s]. Eu tenho que falar com ela!"

                    play sound som_35_passos

                    scene black with dissolve

                    scene chinatown jardim_geral with Dissolve(1.0)

                    pause

                    "{i}toc toc{/i}"

                    s "[mc]!"

                    mc "[s]... eu quero falar com você."

                    scene black with dissolve

                    scene sayuri9_say1 with Dissolve(1.0)

                    pause

                    s "O que você tá fazendo aqui?! Você não pode vir aqui!"

                    mc "Eu sei... mas logo logo eu vou poder. Logo logo eu vou ser um Escolhido também."

                    s "C-como assim?!"

                    mc "É... a Mestra Jidao me fez essa proposta e eu aceitei. Eu vou viver com vocês aqui."



                    jump sayuri9_final1
                "Ainda não tô pronto. Preciso pensar melhor.":


                    "Calma... tenho que pensar melhor."

                    jump s9_decisao_mestra

        "Eu não quero seu 'ouro'. Eu quero livrar todas de você!" if s9_pedidos < 3:

            "Eu vou contra ela mesmo? Jogar tudo na cara e desafiar a Cidade Chinesa?"

            "E o conselho do [chi]? Esvaziar minha mente e aceitar a cultura deles? Eu não sei se consigo perdoar o que eles fizeram."

            if s9_pedidos < 4:

                "Eu também posso pedir mais coisas pra Mestra Jidao... talvez..."

            "Essa escolha pode mudar tudo pra mim... tudo o que eu vivi até agora com a [s], a [fen] e todos os outros."

            "Negar ela e ir contra a Cidade Chinesa. Inclusive ir contra o que a [s] acredita. É isso que eu quero?"

            menu:
                "Sim. Eu vou contra a Cidade Chinesa.":












                    $ s9_mestra = 1

                    $ renpy.block_rollback()

                    "Está decidido. Não posso voltar atrás agora."

                    mc "Não me interessa o que a senhora vai me dar. O que a senhora vai me oferecer. Eu não vim aqui pra barganhar."

                    scene black with dissolve

                    scene sayuri9_mestra8 with Dissolve(1.0)

                    pause

                    mes "Exijo que você controle o tom da sua voz."

                    mc "Eu tô pouco me fodendo pra imortais e pro seu poder! O que você tá fazendo é errado!"

                    mc "Obrigar a [fen] a ser atleta! E agora fazer a [s] a seguir seus passos?! Obrigar ela a ser má com a garota?!"

                    mc "Eu conheço a [s] de verdade e eu sei que ela é uma boa pessoa! Ela quer ser amiga da [fen]!"

                    mc "Mas você estragou tudo! Você, e seus Imortais, vocês acabaram com a vida de muita gente aqui!"

                    mc "Eu vim aqui pra pegar as chaves! Eu vou libertar todo mundo do controle dos Imortais!"

                    mes "..."

                    mc "Não tem nada a dizer?!"

                    $ renpy.vibrate(1)

                    scene sayuri9_mestra10 with hpunch

                    mc "AKHH!!!"

                    mes "Você fala demais!"

                    mes "Muitas palavras e nenhuma ação. Isso é algo que eu vejo muito nos jovens de hoje."

                    mes "Eles querem ser contra isso, contra aquilo, mas o que você realmente faz para tornar o mundo melhor?"

                    mes "Minha cultura é milenar e graças a ela a sociedade sobrevive há milênios."

                    mes "Querer negar milhares de anos de conhecimento com essa cabecinha é uma criança querer questionar a fórmula de um matemático."

                    mes "Diferente de você, eu tenho poder para transformar o que eu acredito em realidade."

                    mes "E você... você vai sofrer pela sua insolência."

                    mc "N-não!"

                    $ renpy.vibrate(1)

                    scene sayuri9_mestra11 with hpunch

                    mc "AAAAAGHHHH!!!"

                    scene black with vpunch

                    play sound som_22_splash

                    pause 1.0

                    scene sayuri9_mestra12 with hpunch

                    mc "N-não!"

                    mes "Adeus, [mc]! Sem você, a Sayuri e a Fen Ju vão voltar a ser o que sempre foram."

                    mc "N-não consigo me mexer! Não consigo nadar!"

                    mes "Ah... esse é apenas um dos efeitos do golpe que eu apliquei."

                    mes "Os músculos do seu corpo não vão obedecer seu cérebro por alguns minutos."

                    mes "Você nunca conseguirá sair da água a tempo. Esse é o fim."

                    mc "A-aghhh!"

                    play sound som_22_splash

                    scene sayuri9_mestra12 with hpunch

                    mc "Nãããooo!!!"

                    scene black with dissolve

                    play sound som_22_splash

                    "Onde eu tava com a cabeça quando eu fui desafiar essa mulher assim?!"

                    play sound som_28_bolhas

                    "Eu devia ter pedido ajuda... por que eu tentei fazer tudo sozinho?"

                    "Eu devia ter pedido ajuda... ajuda de alguém que pudesse me salvar... que tivesse do meu lado..."

                    scene pixie primeira_vez with Dissolve(1.0)

                    mc "P-pixie?!"

                    p "Claro que não, mané."

                    play sound som_22_splash

                    scene sayuri9_say12 with vpunch

                    s "[mc]!"

                    s "Não solta minha mão! Eu vou te tirar da água."

                    mc "T-tá..."

                    s "Ufa... você tá seguro. Vamos sair devagar..."

                    mc "Se não fosse por você eu teria morrido, [s]! Você me salvou!"

                    s "O q-que aconteceu?!"

                    mc "Meu corpo... ele não respondia... a Mestra Jidao... ela me deu um golpe... parece que me paralisou..."

                    s "P-por que a Mestra fez isso?!"

                    mc "{i}cof cof{/i}"

                    s "Vem... vamos conversar lá em cima..."

                    mc "E-ela só não pode saber que eu sobrevivi..."

                    s "Tá... vem..."

                    play sound som_35_passos

                    scene black with dissolve

                    scene chinatown jardim_geral with Dissolve(1.0)

                    pause
                "Ainda não tô pronto. Preciso pensar melhor.":


                    "Calma... tenho que pensar melhor."

                    jump s9_decisao_mestra



    s "Eu não sei se aqui é um lugar seguro pra gente se falar. A casa da Mestra é logo ali."

    mc "Vai ter que ser aqui mesmo. Eu não tenho tempo."

    scene black with dissolve

    scene sayuri9_say1 with Dissolve(1.0)

    pause

    s "O que aconteceu, [mc]? Por que a Mestra iria tentar te matar?! E por que você tá aqui?!"

    mc "Eu vim resolver tudo, [s]! Eu vim salvar você e a [fen] de todo esse rolo!"

    s "Salvar a gente?!"

    mc "Eu juntei as peças com a ajuda do Bao, da Fen Ju, e dos outros! Até sua!"

    mc "O que a Mestra Jidao tá fazendo... isso não é certo!"

    mc "Ela usa o poder e a influência dela, a história dos Oito Imortais, pra escravizar todo mundo do bairro!"

    mc "Essas figuras fantásticas, a cultura milenar de vocês, ela se apossou de tudo e tá usando pros interesses dela!"

    mc "Tá na cara que ela fez algo com a Fen Ju! Os olhos dela! A menina mesmo me contou desesperada!"

    s "[mc]..."

    menu:
        "E tem mais! Eu sei o segredo da Fen Ju!":


            scene black with dissolve

            scene sayuri9_say13 with Dissolve(1.0)

            mc "Eu descobri que ela se mutila. Aqueles cortes! Pelo menos alguns deles! Isso se não foram vocês que fizeram os outros!"

            s "!"

            mc "Ela se sente um monstro! Ela sabe que as habilidades dela não são naturais!"

            mc "Até a professora de balé disse que nunca tinha visto alguém tão boa como ela! E a menina nunca tinha treinado balé!"

            mc "Eu ouvi vocês duas conversando uma vez no gazebo, que tinham investido caro nela!"
        "Melhor não mencionar o segredo dela":


            mc "E tem muito mais coisa que eu não quero nem te falar! Mas eu sei!"

            scene black with dissolve

            scene sayuri9_say13 with Dissolve(1.0)

    mc "Além de tudo que tá debaixo dos panos, envolvendo outros descendentes de chineses aqui do bairro!"

    mc "O Bao disse que a Mestra Jidao tem as chaves! Ela é o coração disso tudo!"

    s "E você... confrontou a Mestra sobre tudo isso?"

    mc "Sim! Ela ainda tentou me oferecer recompensas pra garantir que você e a Fen Ju continuassem jogando o jogo dela!"

    mc "Ela tem um plano pra vocês duas, ou melhor, pra todos aqui no bairro e todo mundo tem que dançar a música dela!"

    mc "Eu não aguentei descobrir tudo isso e não fazer nada! Eu tinha que pelo menos tentar alguma coisa!"

    mc "Mas não deu... eu entendi que eu sou fraco demais pra fazer qualquer coisa sozinho..."

    mc "Eu vou precisar de ajuda. Da sua ajuda, [s]. E talvez a gente precise do Bao e das outras!"

    s "[mc]... calma... eu sei que você tá correndo perigo aqui, mas tudo isso é grande demais."

    s "A gente tem que conversar com calma."

    mc "Eu não tenho tempo, [s]! Tem um ditado que diz: quando você ataca o rei, é melhor não errar."

    mc "Eu errei! A Mestra Jidao vai descobrir que eu tô vivo! E ela vai vir atrás de mim!"

    mc "Ela vai mandar a samurai dela me matar! Aquela He Xiangu não tem salvação!"

    mc "A gente tá num ponto que não tem o que conversar! A gente precisa acabar com o domínio dela. Só isso!"

    if sayuri_namoro:

        mc "Você é minha namorada! Eu te amo! Eu quero ficar com você!"

        mc "E eu preciso de ajuda pra te livrar disso e a gente ser felizes juntos!"
    else:


        mc "A gente sempre teve uma amizade muito forte! A gente passou por poucas e boas juntos!"

        mc "E eu preciso de ajuda pra te livrar disso! Pra que você e a Fen Ju possam ser felizes juntas!"

    s "Então... você não gostaria de viver aqui se as coisas continuassem assim?"

    mc "Se 'continuasse assim'? Não... eu recusei a Mestra Jidao por causa disso, [s]!"

    mc "É impossível que você não tá vendo o que ela tá fazendo!"

    label sayuri9_naoficar:

        pass

    scene black with dissolve

    scene sayuri9_say15 with Dissolve(1.0)

    s "Você acha que eu sou burra?"

    mc "Q-quê?"

    s "Que eu não sei o que tá acontecendo aqui? Você acha que eu precisava 'ser salva'? Por você?"

    mc "S-sayuri... e-eu não..."

    s "Desde o começo eu deixei claro como a Cidade Chinesa funcionava, [mc]."

    s "Eu sei que não fui clara e aberta com você sobre a Fen Ju e o treinamento dela, mas isso não tem a ver com você."

    s "Esse é meu trabalho, minha vida, e você acabou sendo sugado nisso por acaso. Pensa comigo."

    s "Quando a Fen Ju apareceu durante nosso passeio, quando ela desapareceu, quando ela quis vir pro banho com a gente e depois que ela fugiu pro balé."

    s "Eu nunca quis que você entrasse nessa. Aquele dia que eu te liguei pra pedir ajuda pra achar ela, eu tava desesperada."

    s "Mas, pensando agora, eu não imginei que essa história ia mexer assim com você. Te deixar tão consternado."

    s "O que a Mestra faz, o que nós, os Escolhidos, fazemos, isso diz respeito a nós e a nossa comunidade."

    if sayuri_namoro:

        mc "Mas se a gente tá namorando... se você ia querer ficar a sério comigo... eu teria que saber, né?"

    s "Eu imaginei que com o tempo você fosse entender nossa cultura. E um dia, quando eu achasse que você tava pronto, eu te daria mais detalhes."

    mc "[s]... isso quer dizer que você concorda com tudo? É isso que você tá falando?"

    mc "Com a lenda dos Imortais, a manipulação, forçar a Fen Ju fazer o que ela não quer, obrigar você a ser severa com ela. Tudo isso?"

    s "Eu sei que não somos perfeitos, eu sei que muita coisa podia melhorar aqui."

    s "Mas fora daqui o mundo é perfeito, [mc]? Você nunca mentiu pros seus amigos pra manter seu trabalho?"

    s "Nunca traiu ninguém, manipulou, ou fez mal para alguém para conseguir algo que você precisava?"

    menu:
        "Tem razão... Claro que eu fiz...":


            mc "Você tem razão... o mundo não é perfeito, claro... eu fiz muita merda."

            s "Você tá vendo?"
        "Eu fui obrigado a fazer essas coisas.":


            mc "Não é a mesma coisa. Eles me obrigaram a fazer isso!"

            s "Não seja hipócrita. Você sabe muito bem o que tá fazendo. Não coloque a culpa das suas decisões nos outros."

            mc "Você não me entende..."

    scene black with dissolve

    scene sayuri9_say16 with Dissolve(1.0)

    s "Tanto eu como você sabemos que tivemos que fazer coisas que não concordamos totalmente pra realizar nossos sonhos."

    mc "E qual é seu sonho?"

    s "Meu sonho é me tornar Mestra um dia."

    mc "Você diz, ocupar o lugar da Jidao?"

    s "Sim. Ela já fez a oferta pra mim. Em breve ela não vai estar mais aqui."

    s "Ela vai pra China, assumir uma posição de destaque no Partido. Eles estão impressionados pelo sucesso que ela teve na Cidade Chinesa."

    s "E eu sou a próxima. Meu sucesso nas Olimpíadas me tornou uma figura importante. E outras coisas que não vêm ao caso agora."

    s "Eu vou continuar o legado dela. E não tem honra maior pra mim. Esse é meu sonho."

    menu:
        "E a Fen Ju?":


            mc "E a Fen Ju? Você esqueceu dela?"
        "Você vai sacrificar o sonho da Fen Ju pelo seu!":


            mc "E a pobre da Fen Ju?! Você vai sacrificar o sonho dela de ser bailarina pra você ter o seu?!"

    s "Claro que não. Minha discípula tem um compromisso importante com a comunidade dela. Claro que ela vai ter que esquecer um pouco seus próprios desejos."

    s "Mas isso não acontece com todos nós? Às vezes não temos que desistir do que a gente queria porque a vida nos obriga a fazer outra coisa?"

    s "Além de que é possível que a Fen Ju continue o meu legado. Se ela quiser, ela pode ocupar o cargo de Mestra que eu vou ocupar."

    s "Ela é inteligente e terá um futuro brilhante. A menina ainda é uma adolescente, então ela ainda tem medo, mas ela vai crescer e entender."

    menu:
        "Eu não consigo concordar com isso.":


            scene black with dissolve

            scene sayuri9_say14 with Dissolve(1.0)

            mc "Nada disso faz sentido pra mim, [s]. Eu não consigo concordar com essa sua visão."

            s "Eu sei que pode ser cedo, mas você precisa entender que não tem nada horrível acontecendo."
        "Não parece tão ruim falando assim.":


            scene black with dissolve

            scene sayuri9_say14 with Dissolve(1.0)

            mc "O Bao falou que eu tinha que me abrir pra realidade daqui... e falando assim não parece tão horrível..."

            s "Claro que não é."

    s "Ninguém precisa ser salva aqui, [mc]. Isso foi algo que você criou na sua cabeça."

    s "Você sabe o quanto eu gosto de você."

    if sayuri_namoro:

        s "Você é o homem da minha vida. E eu quero viver com você pra sempre."
    else:


        s "Nós somos amigos... mas você sabe que eu sempre quis... s-ser sua namorada."

    s "Esqueça o pesadelo que você criou sobre a gente e viva a realidade. Aceite como somos. Uma cultura diferente da sua, nem melhor, nem pior."

    s "Se você esquecesse essa luta e ficasse do meu lado... eu ficaria tão feliz!"

    mc "Você diz... esquecer de ajudar a Fen Ju e todas as outras?"

    s "Elas não precisam de ajuda, [mc]."

    mc "Então tudo continuaria como está..."

    s "Sim. As coisas continuariam como sempre foram, que é algo muito bom. Porque a Cidade Chinesa sempre foi um símbolo desde a criação da capital."

    mc "[s]... eu não sei..."

    "Se eu aceitar, seria a mesma coisa de aceitar a proposta da Mestra Jidao. Permitir que tudo continue como está."

    "A Fen Ju continuaria infeliz, provavelmente continuaria se machucando..."

    "E o Bao, o banho, a história da He Xiangu... tudo isso vai continuar..."

    "Eu teria que desistir de ir contra os Oito Imortais."

    "Por outro lado, por que eu preciso lutar contra isso? E se a [s] tá falando a verdade? E se realmente tá tudo certo?"

    label sayuri9_escolha_final3:

        pass

    "Eu vou fazer o que a [s] pediu e deixar eles continuarem com isso... ou vou me opor a tudo e desbancar a Mestra Jidao?"

    "Essa é uma decisão só minha. E pode mudar a vida de todos eles pra sempre!"

    menu:
        "Eu aceito você, [s], e a Cidade Chinesa como são.":


            mc "Você tem razão."

            s "T-tenho?!"

            mc "Quem disse que eu sou algum herói e que vocês precisam ser salvas?"

            mc "Ver você, a Fen Ju, o Bao e todos aqui felizes devia ser o mais importante pra mim."

            mc "Eu vou parar com essa história idiota de salvar vocês."

            scene black with dissolve

            scene sayuri9_say18 with Dissolve(1.0)

            pause

            s "Você não sabe como isso me deixa aliviada, [mc]!"

            if sayuri_namoro:

                s "Foi por esse [mc] gentil que eu me apaixonei. Que deixa meu coração tão quentinho só de conversar!"

            if s9_mestra == 1:

                s "E... agora que você enxergou a verdade... eu tava pensando numa coisa."

                s "Eu vou ser a nova Mestra em breve... o que você acha... de ser um Escolhido?"

                mc "E-eu?!"

                s "Sim! Você seria o primeiro Escolhido que não é descendente chinês! Seria a maior honra da nossa comunidade!"

                if sayuri_namoro:

                    s "E já que a gente tá namorando... a gente poderia... você sabe... v-viver juntos..."

                mc "Eu... você sabe que eu recusei a proposta da Mestra... ela queria a mesma coisa..."

                s "Mas agora você entendeu a verdade, não entendeu?"

                mc "Ser um Escolhido..."

                s "Você viveria como um rei, [mc]! Esqueça seu trabalho, os problemas que você passa na ilha!"

                s "Aqui você viveria com tudo do bom e do melhor! Uma vida que poucos podem sequer sonhar!"

                "Viver como um Escolhido?! De novo essa oportunidade..."

                label sayuri9_escolha_final2:

                    pass

                s "O que você acha?"

                menu:
                    "Tudo bem. Eu aceito.":


                        mc "Eu aceito."

                        jump sayuri9_final1
                    "Eu recuso. Eu quero viver no mundo.":


                        mc "Não vai dar, [s]... eu não tô pronto pra deixar o mundo e vir pra cá. Tem muitas coisas que eu ainda quero realizar lá."

                        mc "Por pior que o mundo seja... com trabalho mal remunerado, pessoas terríveis, injustiça e tudo o mais, é lá que eu quero viver."

                        s "[mc]..."

                        jump sayuri_final3_pre
            else:


                jump sayuri_final3_pre
        "Eu não vou deixar vocês continuarem com isso.":


            $ sayuri9_contra = True

            "O que eu acho é que a [s] também tá sendo manipulada! Ela não tá vendo a verdade!"

            "Se eu acabar com o domínio da Jidao, ela vai enxergar o que tá acontecendo!"

            mc "[s]! Me escuta! A verdade é que você tá tentando me manipular com toda essa ladainha!"

            scene sayuri9_say16 with Dissolve(1.0)

            s "C-como é?!"

            mc "Não existe essa história de cultura diferente! O certo é o certo em todo lugar! E o errado é errado!"

            mc "Você tá cega demais pra ver isso?! Todo esse léro-léro te deixou louca?! Eu não compro isso!"

            mc "Quando eu acabar com a Mestra Jidao você vai ver a verdade! Vai ver que você também só tava sendo manipulada!"

            s "Você se acha tão superior assim que não consegue ouvir o que eu tô falando?!"

            s "Eu pensei que você fosse um cara legal, que ouvia as pessoas, [mc]?!"

            s "Quando que você se tornou esse cabeça de bagre que acha que sabe tudo?!"

            if sayuri_namoro:

                s "Eu não quero namorar com uma pessoa assim! Tá tudo acabado entre a gente!"
            else:


                s "Você sempre foi meu melhor amigo! Eu tinha sentimentos reais por você!"

            s "Você não passa de um idiota! Eu não quero nada com um cabeça oca igual você! Que acha que sabe mais do que todo mundo!"

            mc "Você ainda vai me agradecer, [s]! Eu te garanto!"

            s "Sai daqui! Sai daqui agora!"

            mc "Droga!!!"

            play sound som_35_passos

            pause 0.5

            scene sayuri9_say17 with vpunch

            s "[mc], seu idiota!"

            s "Eu te amava de verdade, se-seu... seu b-babaca!"

            s "{i}Uaaahhhh{/i}"

            play sound som_35_passos

            $ tempo = 2

            scene black with Dissolve(3.0)

            scene chinatown geral with Dissolve(1.0)

            mc "Eu não acredito que ela não consegue ver! A [s]! Uma garota tão inteligente!"

            mc "Ela vai jogar tudo o que a gente construiu juntos porque não vê a loucura que tão fazendo aqui!"

            "???" "Calma, jovem. Por que está gritando?!"

            mc "B-bao!"

            show bao normal with dissolve

            chi "Pelo que estou vendo... as coisas não foram como você esperava..."

            mc "Eu fiz o que você falou, Bao! Eu fui pegar as chaves com a Mestra Jidao!"

            show bao soco with dissolve

            chi "Nunca falei que você deveria pegar. Eu te falei que ela tinha as chaves, apenas isso."

            chi "Mas, se você se recorda, eu também disse que você deveria ir como uma xícara vazia."

            mc "Eu sei... mas eu não consigo. Eu não consigo aceitar o que a Mestra tá fazendo!"

            mc "A [s] não consegue ver! Eu tinha certeza que ela ficaria feliz quando eu dissesse que ia salvar ela dessa merda toda!"

            chi "'Salvar'? Quem disse que você era algum tipo de herói? Alguém pediu ajuda pra você?"

            menu:
                "Não... eu tô fazendo o que eu acho certo.":


                    mc "Não... ninguém me pediu pra salvar nada. Eu tô fazendo o que eu acho certo."

                    show bao pensando with dissolve

                    chi "Exatamente. Você está fazendo isso por você, não pela Ai Fen ou qualquer outro."

                    mc "Mas..."
                "E precisa?! É óbvio o que tá acontecendo aqui!":


                    mc "Não precisa pedir! Qualquer um com meio cérebro consegue entender o que acontece aqui!"

                    show bao pensando with dissolve

                    chi "Não discordo."

                    mc "Então?!"

                    chi "Eu repito a pergunta..."

            chi "Alguém falou que você deveria ir contra a Jidao e tentar destruir tudo o que é a Cidade Chinesa hoje?"

            chi "Ou você, do alto da sua moral, decidiu que era isso que deveria ser feito?"

            chi "Quando você faz algo por você, não espere que os outros se sintam agradecidos."

            menu:
                "Com ou sem elas, eu vou fazer isso.":


                    pass

            mc "Não importa se elas apoiam ou não. Eu já decidi o que eu vou fazer. Eu vou acabar com o domínio da Mestra Jidao."

            mc "Você também vai ficar no meu caminho, não vai? Você também não quer acabar com tudo."

            chi "Não e não. Eu não vou ficar no seu caminho, e não quero que você 'acabe com tudo'."

            mc "Mas..."

            show bao falando with dissolve

            chi "Existe um conto chinês antigo chamado O Velho e o Cavalo Branco. Pesquise sobre ele quando tiver interesse."

            chi "Nele, entendemos que a vida é complexa e não devemos limitá-la em boa ou ruim, certa ou errada. Não sabemos o que o futuro nos aguarda."

            chi "Se você deseja derrotar a Jidao, você pode tentar. Se seu fracasso ou sucesso será motivo para alegria ou tristeza, só o futuro dirá."

            chi "Pela nossa amizade, eu digo que ela é mais poderosa do que você imagina. Acreditando ou não em nossas lendas, você precisa respeitá-la."

            mc "Eu sei... sozinho eu não tenho chance contra ela... você tem alguma ideia?"

            chi "A resposta está nas flores. Você precisa da Flor-de-Lótus. Das duas. Apenas com as duas metades você vai conseguir o que você quer."

            mc "Duas Flores de Lótus?"

            chi "Pensa, [mc]..."

            scene black with dissolve

            scene sayuri9_xiangs with Dissolve(1.0)

            "Claro! As duas Flor-de-Lótus! Xiang e He Xiangu!"

            "Só pode ser isso!"

            chi "Vejo que você entendeu."

            chi "Quando você tiver certeza que as duas estão prontas para o momento final, {b}vá até o Portal de Pedra e fale com He Xiangu{/b}."

            chi "Eu estarei de olho em tudo. E boa sorte na sua jornada."

            scene black with dissolve

            scene chinatown geral with Dissolve(1.0)

            mc "Valeu, B-"

            mc "BAO?!!!"

            "O que acontece com esse velho? Como ele faz isso?!"

            "Agora é decisão é minha. Reunir as duas na Ponte de Pedra e desafiar a Mestra Jidao."

            "Ou continuar com a minha vida... e fingir que nada disso aconteceu."

            "Eu não quero morrer tentando parar a Mestra... mas será que eu consigo continuar sem resolver isso?"

            "O que eu vou fazer?"

            scene black with Dissolve(1.0)

            $ tempo = 3

            jump call_cidade

    jump sayuri9_final2

label sayuri9_final1:

    s "[mc]..."

    if s9_mestra == 1:

        s "O-olha minha roupa... toda transparente... mostrando... d-desculpa..."

        mc "N-não tem problema."

        s "E-eu pensei que fosse a... b-bom... não importa. O que aconteceu?"

    mc "Eu pensei que você fosse ficar mais feliz com a minha decisão..."

    scene black with dissolve

    scene sayuri9_say2 with Dissolve(1.0)

    pause

    s "Eu tô feliz, [mc]... nem acredito que isso tá acontecendo... só que..."

    s "Eu só quero que você tenha certeza do que você tá fazendo. De que você entendeu o que isso significa."

    mc "Eu sei... eu entendi. Vai ser igual você e a [fen]. Eu vou ter que viver aqui."

    s "É mais parecido com a [fen]. Eu conquistei o direito de poder viver fora daqui se eu quiser."

    s "Posso morar na casa dos meus pais, com a Júlia, e posso viver aqui também, quando tenho que trabalhar ou treinar."

    s "Você não vai ter essa liberdade por vários anos. Você vai viver aqui por muito tempo, antes de poder sair."

    mc "E-entendo..."

    s "Não é algo que qualquer um tá disposto a fazer. Nosso senso de comunidade aqui é muito grande. A comunidade vem antes da gente."

    s "O que o bairro precisar, você terá que fazer. E pra quem cresceu longe da nossa cultura, isso pode parecer um enorme sacríficio."

    s "As pessoas dizem que é falta de liberdade, mas nós que entedemos isso, vemos como responsabilidade em troca dos nossos direitos."

    s "Você tem certeza que você quer passar por isso? Você tá pronto pra isso?"

    "Abandonar tudo e me tornar um Escolhido da Cidade Chinesa?"

    if sayuri_namoro:

        mc "A gente tá namorando. Se eu quisesse... algo mais sério com você..."
    else:


        mc "Se eu quisesse namorar você... e até mais..."

    s "Ah! D-desculpa... v-você diz..."

    s "E-eu... é-é-é... seria incrível se nós dois pudéssemos viver aqui."

    s "Quando eu assumir as responsabilidades da Mestra Jidao eu vou ter que viver aqui... então..."

    s "M-meu p-parceiro teria... que... sim... v-viver aqui..."

    "Então é isso... se eu não quiser desistir da [s]...eu vou ter que viver aqui."

    menu:
        "Você gostaria?":


            pass

    mc "Você ia gostar? Se eu deixasse tudo pra trás e viesse pra cá?"

    scene black with dissolve

    scene sayuri9_say4 with Dissolve(1.0)

    pause

    s "É claro que eu gostaria! Seria a melhor notícia do mundo!"

    mc "Verdade?"

    s "Claro! Você não entende o que você significa pra mim?!"

    s "Eu gosto tanto de você, [mc]! E saber que você aceitou minha cultura e vai viver aqui comigo! A-ainda parece um sonho!"

    s "Desde a primeira vez que você me assustou no Templo... quando você me ajudou a receber meu prêmio de melhor ginasta."

    s "Você me ajudou com a [fen], e mesmo quando descobriu o que acontecia, você nunca me deixou pra trás."

    s "Você e a Júlia são as pessoas mais importantes da minha vida. E ter você aqui do meu lado... eu não consigo acreditar que essa é uma possibilidade!"

    if sayuri_namoro:

        s "Ainda mais porque a gente..."

        mc "Sim... ainda mais que a gente tá namorando, né?"

        s "É... cada vez mais parece um sonho, [mc]..."

        if s9_pedido1:

            mc "E eu tenho uma notícia melhor ainda..."

            s "Melhor que essa?"

            mc "A Mestra deu a benção dela pra gente ficar juntos..."

            s "Q-quê?! Você tá falando sério?! V-você falou disso com ela?!"
        else:


            "Eu não pedi pra Mestra a benção pra gente ficar juntos... mas eu não acho que ela recusaria..."

        "Acho que não tem hora mais perfeita pra eu finalmente dar esse passo."

        "Eu sinto que a [s] me ama. E eu acho que eu amo ela também. Nosso namoro superou tanta coisa."

        "Ela vai ser a chefe no futuro. E se eu tiver do lado dela... e agora eu vou ser um Escolhido também."

        "A gente seria o casal perfeito. Ou será que eu tô antecipando?"

        "Não sei... mas eu tô sentindo uma coisa tão forte agora. Uma vontade de me declarar pra ela."
    else:


        "Eu e a [s] não somos namorados, mas eu sinto que ela gosta tanto de mim. A gente tem uma química."

        "Se eu realmente decidir ser um Imortal... Será que não ia ser uma boa casar com ela de uma vez? Ser um Imortal, casado com outra."

        "Além de que a [s] vai ser a chefe no futuro. E se eu tiver do lado dela..."

        "Agora que eu aceitei a cultura deles e também quero me juntar... não posso aproveitar a [s] também?"

        if s9_pedido1:

            "E a Mestra deu a benção dela pra gente casar... eu não tenho nenhum empedimento."
        else:


            "Uma pena que eu não pedi pra Mestra a benção pra gente ficar juntos..."

            "Se eu tivesse a benção dela... eu poderia..."

    scene black with dissolve

    scene sayuri9_say5 with Dissolve(1.0)

    pause

    s "Que foi, [mc]? P-por que você ficou vermelho de repente?"

    "Esta é a decisão final. Eu quero passar toda minha vida aqui?"

    "Esquecer a revista, esquecer as celebridades e tudo o que me prendia naquele mundo."

    label sayuri9_escolha_final:

        pass

    "Ou eu ainda não tô pronto pra deixar a vida na Capital? Essa é a escolha que vai mudar minha vida. E a vida dela também."

    menu:

        "[s]. Eu te amo. Quer casar comigo?" if sayuri_namoro or s9_pedido1:

            $ sayuri_casamento = True

            scene black with dissolve

            scene sayuri9_say6 with Dissolve(1.0)

            pause

            mc "[s]..."

            s "O-oi?!"

            if sayuri_namoro:

                mc "Namorar você foi uma das melhores escolhas que eu fiz desde que cheguei na capital."

                s "A-ai... [mc]..."

                mc "E... depois de tudo o que a gente passou... eu não tenho mais como fugir da verdade."
            else:


                mc "A gente não namora oficialmente... mas é impossível negar que rola uma coisa entre a gente."

                mc "Quando eu falei com a Mestra Jidao, o mais importante pra mim foi pedir pra ela dar a benção dela pra gente."

                s "Q-quê?!"

                mc "Sim... eu percebi uma coisa com tudo isso... e eu não tenho mais como fugir da verdade."

            mc "Eu te amo."

            s "!!!"

            mc "Eu não posso jurar que meu amor seja imortal, mas eu quero que ele seja infinito enquanto durar."

            mc "Meu coração será seu todos os dias... de hoje até o final da minha vida. A verdade é que eu quero viver com você pra sempre."

            mc "Por isso... você... você aceita casar comigo?"

            s "E-eu..."

            mc "[s]?"

            scene sayuri9_say7 with hpunch

            mc "[s]!!!"

            s "..."

            mc "Cuidado!"

            scene black with dissolve

            scene sayuri9_say8 with vpunch

            pause

            s "[mc]... aah..."

            mc "Você tá bem?!"

            s "Não sei... eu não sinto minhas pernas... e eu acho que eu não tô... respirando..."

            mc "Haha... Calma..."

            mc "Lembra do Tadaima? Foi exatamente assim... você continua sendo a mesma [s] que eu conheci naquela época. Só cortou o cabelo."

            s "Não."

            mc "Não?"

            s "A [s] daquela época achava que nunca iam gostar dela de verdade..."

            s "Meus amigos do passado me olhavam com inveja... e ao mesmo tempo minha Mestra me tratava com desprezo..."

            s "Não importava o que eu fizesse... eu nunca ia satisfazer ninguém. Eu só queria trazer honra pra minha família."

            s "Por que eles não podiam se orgulhar do que eu me tornei?"

            s "E então você apareceu... você me viu. Me viu desmaiando... me viu chorando... com medo... com raiva..."

            s "E mesmo assim você ficou do meu lado. Não teve inveja, não me desprezou, só me amou. Como eu nunca achei que alguém faria."

            s "Você não me ama pelo que eu fiz. Você nem entende nada de ginástica. Você me amou pelo que eu sou."

            scene black with dissolve

            scene sayuri9_say9 with Dissolve(1.0)

            pause

            s "Eu não preciso que os outros me aceitem. Eu só quero que você me queira."

            mc "Eu te quero."

            s "Eu sei. Eu também te quero, [mc]."

            mc "Então..."

            s "A [s] do passado desmairia... mas ela nunca teria coragem de dizer 'sim'. Ela não tinha coragem de fazer o que queria."

            s "E eu quero ficar com você. Por isso eu aceito. Eu aceito seu pedido. Eu aceito me casar com você."

            s "E esse era todo o ar que eu tinha..."

            mc "Haha..."

            mc "Você só precisa de mais um pouquinho."

            s "Hm?"

            scene black with dissolve

            scene sayuri9_say10 with Dissolve(1.0)

            pause

            mc "Eu vou ficar com você pra sempre."

            mc "Como atleta... como Mestra... como mulher. Eu quero tá ao seu lado e ser seu apoio em tudo o que você fizer."

            s "Ah..."

            s "Você vai ser o Imortal mais incrível deste mundo, [mc]."

            mc "Eu não sei se-"

            s "Se eu vou ser uma Imortal... você também vai ser... e nós vamos tornar a Cidade Chinesa o melhor que ela pode ser."

            mc "Pode contar comigo."

            s "Eu sempre contei. E você nunca me deixou pra trás."

            scene black with dissolve

            scene sayuri9_say11 with Dissolve(1.0)

            pause

        "Eu serei um imortal, mas sem a [s]" if not sayuri_namoro or not s9_pedido1:

            scene black with dissolve

            scene sayuri9_say6 with Dissolve(1.0)

            pause

            mc "Eu decido ficar aqui. Eu vou ser um dos Escolhidos."

            s "Tá falando sério?!"

            mc "Eu vou viver com você, com a [fen], com a Mestra, o velho Bao! Eu quero ser uma lenda imortal também!"

            s "I-isso é incrível!"

            if sayuri_namoro:

                mc "E por querer me dedicar a isso, eu acho que a gente deve parar nosso namoro."

                s "Q-quê?! Mas agora que você tá aqui! Por quê?!"

                mc "Eu gosto muito de você... mas eu não tô pronto pra dar dois passos grandes desses na minha vida agora."

                mc "Eu quero primeiro ver como vai ficar minha vida aqui... e depois pensar nos meus sentimentos com uma mulher."

                s "E-eu entendi..."

                s "Eu tô tão feliz que você tá aqui... o resto a gente vê depois!"

                mc "Obrigado por entender."

            s "O meu maior sonho tá acontecendo! Ter o apoio da pessoa mais importante da minha vida!"
        "Eu não tô pronto pra desistir da capital e vir pra cá.":


            if s9_mestra == 2:

                mc "Não vai dar, [s]... eu não tô pronto pra deixar o mundo e vir pra cá. Tem muitas coisas que eu ainda quero realizar lá."

                mc "Por pior que o mundo seja... com trabalho mal remunerado, pessoas terríveis, injustiça e tudo o mais, é lá que eu quero viver."

                s "[mc]..."

                s "Mesmo você não aceitando... você não vai ficar contra a gente, né?"

                s "Não vai tentar se intrometer nas nossas coisas."

                "Será que tem uma chance de eu tirar a [s] daqui? Se eu desmontar o esquema da Mestra Jidao?"

                "Talvez... se eu salvar elas... eu posso ficar com ela sem ter que viver aqui!"

                "Ou é melhor eu só deixar elas em paz?"

                menu:
                    "Eu vou deixar tudo como tá. Você e a Mestra continuam no comando.":


                        mc "Não vou causar... vou deixar tudo como está... e deixar vocês aqui... pra sempre."

                        label sayuri_final3_pre:

                            pass

                        if sayuri_namoro:

                            s "Então... nossa história juntos acaba aqui?"

                            mc "Você não pode deixar esse mundo e viver comigo? Como minha mulher?"
                        else:


                            s "Então... nossa história juntos acaba aqui?"

                            mc "Você não pode continuar sendo minha amiga? Igual sempre?"

                        s "Eu adoraria... mas acho que eu penso igual você. Por pior que seja perder você, eu sinto que é aqui que eu quero viver."

                        mc "Então acho que é isso..."

                        s "Sim... i-isso... é... um... a-adeus..."

                        mc "[s]? Você tá legal?"

                        s "A-adeus..."

                        scene sayuri9_say7 with hpunch

                        mc "[s]!!!"

                        s "..."

                        mc "Cuidado!"

                        scene black with dissolve

                        scene sayuri9_say8 with vpunch

                        pause

                        s "[mc]... aah..."

                        mc "Você tá bem?!"

                        s "Não sei... eu não sinto minhas pernas... e eu acho que eu não tô... respirando..."

                        mc "Haha... Calma..."

                        mc "Lembra do Tadaima? Foi exatamente assim... você continua sendo a mesma [s] que eu conheci naquela época. Só cortou o cabelo."

                        s "Não."

                        mc "Não?"

                        s "A [s] daquela época achava que nunca iam gostar dela de verdade..."

                        s "Meus amigos do passado me olhavam com inveja... e ao mesmo tempo minha Mestra me tratava com desprezo..."

                        s "Não importava o que eu fizesse... eu nunca ia satisfazer ninguém. Eu só queria trazer honra pra minha família."

                        s "Por que eles não podiam se orgulhar do que eu me tornei?"

                        s "E então você apareceu... você me viu. Me viu desmaiando... me viu chorando... com medo... com raiva..."

                        s "E mesmo assim você ficou do meu lado. Não teve inveja, não me desprezou, só me amou. Como eu nunca achei que alguém faria."

                        s "Você não me ama pelo que eu fiz. Você nem entende nada de ginástica. Você me amou pelo que eu sou."

                        scene black with dissolve

                        scene sayuri9_say9 with Dissolve(1.0)

                        pause

                        s "Eu não preciso que os outros me aceitem. Eu só precisava de você."

                        s "E pensar que isso vai chegar ao fim assim..."

                        if sayuri_namoro:

                            menu:
                                "Vamos ficar uma última vez.":


                                    mc "[s]... nós vivemos tantas coisas juntos..."

                                    s "Sim..."

                                    mc "Nosso amor pode não ser imortal... mas a gente pode fazer ele ser intenso uma última vez."

                                    s "Você diz..."

                                    scene black with Dissolve(3.0)

                                    pause

                                    scene quarto_chines with Dissolve(3.0)

                                    pause

                                    s "Hmm... [mc]..."

                                    mc "Tira a roupa... hoje você vai ser minha."

                                    call sayuri_sexo_final
                                "Eu sempre vou torcer por você.":


                                    pass

                        mc "Eu nunca vou te esquecer, [s]... a gente pode nunca mais ficar... mas eu nunca vou te esquecer."

                        s "Nem eu... você sempre vai ser o homem da minha vida."

                        mc "Agora eu preciso ir..."

                        s "[mc]... Eu queria... eu posso te acompanhar até lá fora?"

                        mc "Claro... deixa eu me arrumar."

                        s "E-eu também..."

                        s "Eu quero passar esse último minuto com você."

                        jump sayuri9_final3
                    "Eu vou salvar você e a Fen Ju disso aqui.":


                        jump sayuri9_naoficar
            else:


                jump sayuri_final3_pre

    $ sayuri_final1 = True
    $ persistent.sayuri_final1 = True

    s "Eu não vejo a hora de ver seu ritual... vai ser o ritual mais incrível que a Cidade Chinesa já teve."

    mc "Você acha que vai dar tudo certo?"

    s "Claro que vai. Nossa comunidade precisa de pessoas como você. De bom coração e grande força de vontade."

    mc "Valeu..."

    s "Volte pra ilha. Prepare suas coisas. Eu vou te buscar quando for a hora."

    s "Quando você se tornar um Escolhido, você terá que abandonar certas coisas do mundo."

    mc "É o que acontece com a [fen], né? Ela não pode nem ver os pais."

    s "Sim... você terá que passar por esse tempo. Mas eu vou tá aqui com você."

    mc "Então eu realmente vou deixar minha vida no passado."

    s "Sim. Depois do ritual, sua vida vai se transformar completamente. E vai ser melhor do que nunca. Eu te prometo."

    mc "Ok... ufa... vou respirar fundo e arrumar tudo pro ritual."

    s "Boa sorte. E qualquer coisa... pode contar comigo..."

    if sayuri_casamento:

        s "Pode contar com sua n-noiva..."

        mc "[s]... eu não vejo a hora."

    scene black with Dissolve(3.0)

    scene cidade noite with Dissolve(1.0)

    pause

    "Pensar que eu não vou ver mais estes prédios... a careca do chefe... e tantas pessoas incríveis."

    "Vou deixar amores pra trás... será que eles vão ficar bem?"

    "Mas agora eu decidi meu caminho. Sem arrependimentos, [mc]. Você vai se tornar um Imortal."

    "O que mais este lugar teria pra mim se eu tivesse escolhido um caminho diferente?"

    "Tantas possibilidades... uma decisão pode mudar nossa vida completamente. E nós somos os únicos responsáveis pelo que escolhemos."

    "Eu escolhi meu caminho. Espero que cada um de vocês escolha o seu."

    "Adeus capital..."

    scene black with Dissolve(3.0)

    pause

    scene templo frente with Dissolve(3.0)

    pause

    mes "Nos encontramos aqui esta manhã para celebrar o surgimento de um novo pilar de nossa sociedade."

    scene black with dissolve

    scene sayuri9_dojo1 with Dissolve(1.0)

    pause

    mes "[mc]. A partir de agora você renuncia ao seu passado e sua história e será um comigo e a Cidade Chinesa."

    mes "Suas ações agora são nossas e nossa história é sua. Você faz parte de uma comunidade milenar e imutável."

    mes "Suas vontades não importam mais. Você vive para que nossa sociedade prospere e para que todos aqui sejam felizes."

    mes "Suas obrigações são tudo o que você carregará. Sua responsabilidade é árdua, mas sua recompensa infinita."

    mes "Você é um dos pilares que levantam nosso altar, a base onde se sustentam milhares de pessoas."

    "Essas palavras... eu sinto elas dentor de mim. São tão fortes e... corretas. Me dão até um calor no coração."

    "Agora eu faço parte de algo muito maior."

    mes "Você aceita se tornar um com todos nós?"

    menu:
        "Sim.":


            pass

    mes "Está feito. Você agora deixa de ser apenas um homem e se torna um Escolhido."

    s "Viva!"

    fen "Eba! Parabéns!"

    chi "Agora você é um de nós. Parabéns."

    mc "Obrigado, pessoal."

    chi "Que você se torne uma peça fundamental da Cidade Chinesa, mas nunca perca o coração de ouro que você tem."

    s "Ele não vai. Pode ter certeza."

    fen "..."

    scene black with Dissolve(3.0)

    pause

    scene sayuri9_dojo2 with Dissolve(3.0)

    pause

    "E assim começou minha nova vida, como um Escolhido. No meu caminho para me tornar um Imortal."

    "Com certeza não foi o caminho que eu imaginei quando eu me mudei pra capital. Mas é onde eu fui parar."

    "Às vezes a vida tem dessas. A gente planeja uma coisa, mas do nada as coisas simplesmente acontecem."

    "Pra um pé-rapado igual eu... que morava num muquifo, até que eu cheguei longe."

    "Às vezes eu fico pensando... como minha vida seria se eu tivesse mudado uma decisão importante sequer."

    "Bom... acho que isso eu nunca vou saber. Agora deixa eu ver como a [s] tá."

    scene black with Dissolve(3.0)

    pause

    scene sayuri9_dojo3 with Dissolve(3.0)

    pause

    s "Eu quero ver mais determinação aí! Coração mais força! Encontre o caminho entre os dois!"

    fen "S-sim, senhora!"

    "A [s] sem dúvida mudou. Eu vejo um novo brilho nos olhos dela."

    "Ela não é aquela garota frágil e medrosa que eu conheci. Mas ela não é violenta como um dia eu pensei que fosse."

    "A Mestra Jidao está cada vez mais passando as coisas pra ela, preparando pra viajar pra China. Agora praticamente é a [s] que comanda tudo aqui."

    "Desde que ela virou a nova Mestra, ela nunca mais foi ríspida com a [fen]. Ela é firme, mas eu sinto carinho nas palavras dela."

    "Ela vai começar uma nova era na Cidade Chinesa. E eu acho que todo mundo vai ser mais feliz."

    if sayuri_casamento:

        "E agora que a gente tá noivos, é questão de tempo até termos nossos filhos. Ela vai ser uma excelente mãe."

        "Falando em filho..."

    scene black with dissolve

    scene sayuri9_dojo4 with Dissolve(1.0)

    pause

    "É uma pena que a [fen] tenha que continuar sendo atleta..."

    "Ela teve que desistir do sonho de ser dançarina de balé. E eu consigo ver no rostinho dela como ela tá triste."

    "Eu espero que um dia ela possa escapar desse destino e finalmente possa fazer o que ela quer."

    "Mesmo não sendo o ideal, ela entende a função dela aqui na Cidade Chinesa. Todos nós entendemos."

    "Nossa responsabilidade com o coletivo é mais importante que nossas vontades individuais."

    "Se todo mundo fizer sua parte, todos nós seremos felizes juntos. E, mesmo sendo uma jovem, ela entende isso."

    "Eu tenho muito orgulho dela."

    s "[mc]."

    mc "O-oi."

    s "Eu terminei meu treino com ela..."

    mc "Ok. O que você acha de nós três comermos um lámen pra comemorar?! Faz tempo que a gente não vê o Bao!"

    fen "E-eu não posso... eu tenho qu-"

    mc "A Mestra não vai se importar se a gente quebrar as regras uma vez, certo, Mestra?"

    fen "..."

    scene black with dissolve

    scene sayuri9_dojo5 with Dissolve(1.0)

    pause

    s "Tudo bem... mas amanhã exercício dobrado então!"

    fen "S-sim, senhora!"

    mc "Bora lá!"

    "É tão legal ver como a [s] tá mudando com a [fen] também."

    "Os treinos continuam puxados, mas eu sinto que ela mudou como pessoa."

    "E agora que a Mestra Jidao deixa a maioria das coisas na mão da [s], eu sinto que isso mudou bastante também."

    "Poder ver isso mudando... me dá uma esperança que a gente pode mudar as coisas."

    fen "Vocês vão ficar pra trás!"

    mc "O-opa!"

    scene black with Dissolve(3.0)

    scene sayuri9_bao4 with Dissolve(3.0)

    pause

    chi "Vejam só... acho que é a primeira vez que eu vejo vocês aqui juntas."

    s "V-vamos tentar vir aqui mais vezes, senhor."

    chi "Já falei para você parar de me chamar de 'senhor'. Eu sou seu avô."

    chi "Agora você é a nossa líder. Não precisa mais esconder a verdade."

    s "Sim, se- v-vô."

    mc "Como assim?"

    chi "Isso é algo que ficou no passado, certo, garotas?"

    s "Sim."

    fen "É! A gente veio comer!"

    chi "Nem precisam dizer os sabores. E você, [mc]? Será que pode me ajudar?"

    menu:
        "Claro, velho. Pelos velhos tempos.":


            mc "Com certeza. Não é porque eu sou um Imortal-"

            if sayuri_casamento:

                s "Casado com a líder, diga-se de passagem."

                fen "..."

                mc "Exatamente. Casado com a líder."

            mc "Mesmo assim, eu não posso deixar esse velho fazer o trabalho todo."

            chi "Gostei de ouvir, garoto. Mantenha sempre a xícara vazia."

            mc "Com certeza."
        "Agora eu só dou ordens e como.":


            mc "Passo, [chi]. Agora que eu só dou ordens e como. Chega de fazer lámens pra mim."

            chi "Haha! Veja a pompa desse garoto."

            fen "Tá chique agora!"

    scene black with dissolve

    scene sayuri9_bao5 with Dissolve(1.0)

    pause

    chi "Muito bem! Três pratos saindo!"

    fen "Eba!"

    s "E a senhorita vê se manera!"

    fen "Você não manda em mim! Eu vou comer igual uma porca e queimar tudo amanhã!"

    s "!"

    s "I-isso é jeito de falar? Onde essa garota aprende essas coisas?!"

    chi "Já ouviu falar das redes sociais?"

    s "Eu sabia que tinha uma razão pra Mestra proibir isso!"

    fen "T-tarde demais! Não pode voltar atrás agora!"

    s "A gente vai cair em desgraça assim..."

    mc "Hahaha!"

    fen "Hahahaha!"

    chi "Como tudo mudou... e para melhor."

    if sayuri_casamento:

        s "Depois que a gente terminar, [mc]... você... quer me acompanhar?"

        "Talvez tenha chegado a hora da gente ter nosso filho..."

        mc "Com certeza, amor."

        s "Vem..."

        scene black with Dissolve(3.0)

        pause

        scene quarto_chines with Dissolve(3.0)

        pause

        s "Hmm..."

        label say9_premium1:

            s "[mc]..."

        menu:
            "Hoje vai ser diferente. Eu quero fazer TUDO com você.":


                if not premium:

                    call mensagem_premium

                    jump say9_premium1

                mc "Tira a roupa. Hoje você vai ser minha."

                call sayuri_sexo_final
            "Eu não tô aguentando de tesão.":








                mc "Tira a roupa. Hoje você vai ser minha."

                scene black with dissolve

                scene sayuri9_premium13 with vpunch

                pause

                s "Você sabe que eu gosto atrás! Assim mesmo!"

                mc "AAGHH! SAYURI!!!"

                s "Goza na minha vagina por favor!"

                mc "Claro! Eu vou te engravidar!"

                s "AAAIINNNGHH!"

                mc "GOZANDOO!!! AAAGGHHHH!!!"

                scene black with dissolve

                pause 1.0

                scene sayuri9_quarto1 with Dissolve(1.0)

                mc "Aah..."
            "Vamos se abraçar na cama? Sem sexo.":


                mc "Hoje eu quero te abraçar..."

                s "[mc]... eu também te amo..."

                scene black with dissolve

                scene sayuri9_quarto1 with Dissolve(1.0)

                pause

        s "Eu gostei tanto o que você fez hoje... eu senti uma coisa diferente..."

        mc "Foi tão bom assim?"

        s "Foi... você é perfeito na cama. Mas não é isso. Eu acho que aconteceu."

        mc "N-nosso filho?! Q-que incrível, [s]!"

        s "N-não fica tão feliz ainda. Não tem como ter certeza, né..."

        s "M-mas... não sei... eu tô me sentindo diferente..."

        mc "Esse é o primeiro passo pra gente criar nossa dinastia."

        s "Dinastia? Tá falando sério?"

        mc "Imagina nossos herdeiros sendo mestres e mestras da Cidade Chinesa por milênios?"

        s "Eu não me importo tanto com isso... eu quero só poder viver meu tempo aqui da melhor forma possível."

        s "Eu quero que a Cidade Chinesa seja próspera e que eu possa fazer um bom trabalho... com você ao meu lado."

        s "Quero aproveitar você o máximo que eu puder."

        mc "Isso eu também quero."

        s "E f-fazer essas coisas com você... eu quero mais e mais..."

        mc "Olha só..."

        s "N-não me deixa com vergonha..."

        mc "Hmm..."

        s "Eu quero... fizar assim... pra sempre..."

        "Ainda não consigo acreditar que eu cheguei aqui... com essa mulher perfeita nos meus braços..."

        "Ter vindo pra Cidade Chinesa foi a melhor escolha que eu fiz na minha vida."

        s "{i}zZzZzZz{/i}"

        "Pode ficar tranquila, meu amor."

        if s9_pedido4:

            mc "[s]?"

            s "..."

            "Com licença, linda..."
    else:


        scene black with Dissolve(3.0)

        pause

        scene quarto_chines with Dissolve(3.0)

        pause

        "Ah... o dia foi incrível..."

        "Cada dia aqui tem sido um mais perfeito que o outro."

        "Eu ganhei um quarto especial também... ser um Imortal com certeza deixou a vida uma delícia..."

        "Ter vindo pra Cidade Chinesa foi a melhor escolha que eu fiz na minha vida."

    if s9_pedido4:

        "Hoje ela quer me ver... é melhor eu não deixar ela esperando."

        scene black with dissolve

        scene chinatown jardim_geral with Dissolve(1.0)

        pause

        "{i}TOC TOC{/i}"

        "???" "Entra."

        play sound som_35_passos

        scene black with dissolve

        scene sayuri9_quarto2 with Dissolve(1.0)

        pause

        mes "Aí está meu garoto."

        mc "Você sabe que quando você chamar eu sempre vou vir."

        if sayuri_casamento:

            mes "Excelente. Ela pode ser sua esposa, mas eu sou sua mestra."
        else:


            mes "O que eu mais gostei é que você trocou a inocente da minha discípula para ficar com a mestra de verdade."

            mes "Se você continuar me satisfazendo assim, quem sabe eu não permito que você seja meu consorte verdadeiro?"

        mc "Sim, senhora."

        if sayuri_casamento:

            mes "Agora venha aqui e sirva sua mestra como você nunca faz com sua esposa."
        else:


            mes "Agora venha... eu preciso do caralho do meu escolhido."

        mc "..."

        mes "Vem logo... começa igual você sempre faz."

        scene black with dissolve

        if premium:

            scene mestra_premium1 with Dissolve(2.0)

            pause

            mes "Hmm... é assim que você gosta, né?"

            mc "É... mamando o peito da minha mestra."

            mes "Você não consegue passar uma noite sem mamar?"

            mc "Não. Eu não consigo sem mamar na sua teta gostosa."

            mes "Ahn... é pra isso que ela serve... pra alimentar meu escolhido."

            mc "As duas?"

            mes "Claro... as duas tetas são suas. Você sabe disso."

            mc "Eu vou mamar elas mais forte então. Eu vou morder, fazer o que eu quiser com suas tetas."

            mes "Pode fazer. Foi pra isso que eu te escolhi. Pra te dar tudo o que você quer. Hmm..."

            scene mestra_premium2 with Dissolve(1.0)

            pause

            mes "Isso... lambe, chupa, morde... nnnghh... eu gosto quando você mama com vontade."

            mc "Sempre me dá tesão quando você deixa eu fazer o que eu quiser com suas tetas de vaca."

            mes "Nngh... olha... não seja mal criado. Não pode falar assim."

            mc "Eu falo como eu quiser na cama com você."

            mes "Ah... ai... que boca suja. Sorte sua que sua boca é uma delícia me chupando assim."

            mc "Você disse que eu posso fazer o que eu quiser."

            mes "Não pode exagerar. Agora continua chupando, assim mesmo... hmmm..."

            menu:
                "Continuar chupando":


                    mc "Me dá tudo... deixa eu mamar tudinho."

                    mes "Sim... mama tudinho... igual você fez todo dia."

                    mc "Ah..."

                    mes "Nnghh..."
                "Morder o peito dela com força.":


                    scene mestra_premium3 with vpunch

                    mes "Ai! Que é isso?!"

                    mc "Eu disse que eu faço o que eu quero com suas tetas de vaca!"

                    mes "Nnghh! O que eu faço com você?! Me tratando desse jeito?!"

                    mc "Você não consegue ficar brava comigo."

                    mes "Ai... você sabe que eu não consigo... mesmo quando você mastiga meu mamilo assim."

            mes "Mas agora tá bom... deixa eu fazer carinho em você agora, deixa?"

            mc "Tá bom... deixa eu deitar."

            scene black with dissolve

            scene mestra_premium4 with Dissolve(1.0)

            pause

            mc "Ah... eu adoro quando você pega nas minhas bolas e massageia elas, mestra."

            mes "Que bom. Eu quero agradar você... fazer você sentir gostoso."

            mes "Eu vou cuidar das suas bolas... do seu pênis... enquanto eu te lambo."

            mc "S-sim... nngh..."

            mes "Tudo pro meu garoto preferido."

            mc "Deixa eu pegar na sua bunda gorda enquanto você faz carinho em mim."

            mes "Claro... ela é sua também."

            mc "Você me trata tão bem aqui, mestra..."

            mes "Hmm... claro... tudo do melhor pra você."

            mc "Eu quero pegar no seu peito também."

            scene black with dissolve

            scene mestra_premium5 with Dissolve(1.0)

            pause

            mes "A-ah... por que tanta força? Quer tirar leite de mim, é?"

            mc "É. Eu gosto de pegar em você."

            mes "Então pega... nnghh... pega bem gostoso... eu quero ver você bem duro pra mim."

            mc "É por isso que você me agrada tanto? Você gosta do meu caralho tanto assim?"

            mes "Eu te agrado porque você merece... ahn... porque você é meu escolhido... e eu... hmm... amo cuidar de você."

            mc "E a [s]?"

            mes "Que que tem aquela garota mimada?"

            mc "Ela não merece?"

            mes "Claro que não. Nenhuma delas merece você. Eu sou a única que pode dar o que você quer."

            scene mestra_premium6 with Dissolve(1.0)

            pause

            mes "Só de pensar que você tá aqui comigo... ah... minhas partes começam a pegar fogo."

            mc "Esse carinho todo me deixou duro. Eu adoro quando você me lambe assim."

            mes "Eu cuido de você... e você cuida de mim agora também."

            mes "Sua mestra quer sentir sua lingua gostosa no meio das coxas dela."

            mc "E se eu não quiser?"

            mes "Não seja mal comigo. Eu faço tudo pra você."

            menu:
                "Tem razão. Eu vou ser bonzinho com você.":


                    pass
                "Quero ouvir você implorar antes. Igual uma cadela.":


                    mes "Você gosta de ser mal criado comigo..."

                    mc "Eu adoro."

                    mes "Nggh... por favor... lambe sua mestra com essa boquinha deliciosa, por favor..."

                    mc "Você não aguenta ficar sem?"

                    mes "Não... eu imploro... me lambe por favor."

            mc "Eu vou ser bonzinho com você... mas só porque você sabe que eu faço que eu quero."

            mes "Claro... tudo o que você quiser, meu amor."

            scene black with dissolve

            scene mestra_premium7 with Dissolve(1.0)

            pause

            mes "Assim.... ahnn... essa língua me lambendo assim... nnnghhh..."

            mc "Eu vou te deixar mais molhada ainda."

            mes "Isso... ah... eu não resisto quando meu amor me chupa assim."

            mc "Abre mais as pernas. Deixa eu lamber melhor."

            mes "C-claro... aah..."

            scene mestra_premium8 with Dissolve(1.0)

            pause

            mes "Ai... como chupa gostoso minha... aah..."

            mc "Esses gemidos seus me deixam mais louco, mestra."

            mes "Então... nnnfhh... eu vou gemer mais ainda... aah.... pra você..."

            mc "Isso. Fala como você ama minha língua dentro da sua buceta necessitada."

            mes "Eu amo! Eu amo sua língua! NNGHH!"

            mc "Agora chega. Eu quero te comer."

            mes "Só mais um pouco! Por favor!"

            menu:
                "Nada disso. Senta aqui agora.":


                    mc "Não não não. Você disse que eu mando. Então vem aqui agora."

                    mes "Tem razão... você quem manda."
                "Tá bom...":


                    mc "Só mais um pouquinho."

                    scene mestra_premium9 with Dissolve(1.0)

                    pause

                    mes "Ahh! Obrigada! Nnggh! Eu adoro tanto!"

                    mc "Nnnghh..."

                    mes "Isso! Isso! Agora sim!"

                    mes "Eu preciso do seu pênis em mim agora."

            mc "Então vem. Deixa eu sentir essa buceta molhada pulando no meu caralho."

            scene black with dissolve

            scene mestra_premium10 with Dissolve(1.0)

            pause

            mes "Aagh! Entrou!"

            mc "Entrou fãcil de tanto que você deseja meu pau te comendo!"

            mes "Sim! Nngh! Eu preciso dele! Ahnn! Eu preciso do seu pau!"

            mc "Então vai! Ah! Me dá prazer, mestra! Esfrega sua buceta em mim!"

            mes "Sim! Nngh! Tudo o que você quiser! Meu corpo é seu! Aahh! Ele serve pra te dar prazer sempre que você quiser!"

            mc "Sempre que eu mandar!"

            mes "Isso! Manda na minha buceta! NGHHH!!"

            mc "Me dá mais leite também!"

            scene mestra_premium11 with Dissolve(1.0)

            pause

            mes "NGHHH! I-isso! AAHHNN!"

            mc "Sua teta e sua buceta são uma delícia, mestra! Eu adoro te foder assim!"

            mes "Fode! Fode mais! Ahnn!"

            mc "Eu vou foder mais forte!"

            mes "Faz como você quiser! Aiinn! Faz como seu caralho quiser! Aaghhh!"

            scene mestra_premium12 with vpunch

            pause

            mes "Eu vou gozar! Aiin! Tá vindo!"

            mc "Eu também! Eu quero jogar toda minha porra em você! Ahnnn!"

            mes "ISSO! JORRA TUDO EM MIM! AAHNNN!!"

            mc "TOMA! TOMA TODA MINHA PORRA, SUA VACA!!!"

            mes "AAAAINGHH!!!"

            scene mestra_premium13 with vpunch

            mc "AAHHHH!!!"

            mes "AAHN! AAHHHNNN!"

            mes "Aahh..."

            mc "Ai..."

            mes "Assim que eu gosto..."

            mc "Demais..."

            mes "Agora sai pra lá."

            mc "T-tá..."

            scene black with Dissolve(2.0)
        else:


            scene mestra_premium13 with Dissolve(1.0)

            pause

            mes "Assim mesmo! Mete gostoso! Seu pau é meu!"

            mc "S-sim! Toma tudo!"

            mes "Aahh! Aannnghh!"

            scene black with dissolve

        pause 1.0

        scene sayuri9_quarto3 with Dissolve(2.0)

        pause

        mes "Deixar seu caralho aqui é o único motivo que eu ainda não fui para a China."

        mc "Verdade?"

        mes "Talvez eu leve você comigo. Para me servir quando eu precisar."

        mc "S-senhora... m-mas."

        mes "Cale a boca. Você sabe que eu estou brincando."

        mc "Senhora... por que você me trata assim e na cama parece outra pessoa?"

        mes "E-eu! Digo... Passar tempo demais aqui tá fazendo você criar asinhas."

        if sayuri_casamento:

            mes "Agora pode ir. Ela não pode descobrir que você serve a outra mestra."
        else:


            mes "Agora pode ir."

            mc "Eu não posso dormir com a senhora? Eu sou um homem sem compromisso."

            mes "Mesmo assim... você é apenas meu gigolô. Eu não tô pronta pra me assumir com você. Saia."

        if s9_pedido3:

            mc "Senhora... você lembra quando você me fez a promessa de viver aqui..."

            mc "Uma das coisas que eu pedi era saber a verdade de tudo..."

            mc "Eu sou muito agradecido por poder viver aqui. É muito melhor do que eu tinha imaginado."

            mc "Mas eu sempre quis saber a verdade."

            mes "Você tem certeza que isso interessa agora?"

            mc "Sim..."

            mes "Você tem me dado muito prazer esses tempos. Eu posso compartilhar com você um pouco sobre isso."

            mc "Obrigado... eu queria saber da [fen]. O que aconteceu com ela?"

            mes "Os detalhes você teria que falar diretamente com eles. Mas nós temos um acordo com uma empresa da capital."

            mes "Essa empresa melhorou o desempenho da garota com uma tecnologia irrastreável."



            mc "Por isso ela tem os olhos com uma cor... rara?"

            mes "Esse é o único efeito colateral do processo. Mas isso é algo que nunca os juízes olímpicos perceberão."

            mc "E a [s]?"

            mes "Eu não vou falar dela."

            mc "T-tudo bem..."

            mes "Nós faremos o que for preciso para manter a relevância e o poder da nossa comunidade. Você é um de nós agora."

            mc "Sim... eu entendo perfeitamente. E isso tem a ver com o nome delas?"

            mes "Claro. Se algo desse errado, tínhamos que nos livrar delas e fazê-las usar um nome que não fosse chinês tornaria tudo mais fácil."

            mc "Entendo..."

            mes "Existem muito mais coisas. Mas, ou você decifra sozinho, ou esquece de uma vez. Me incomoda falar sobre essas coisas."

            mes "Pode sair. Você fez o que tinha que fazer."

        mc "S-sim. Estou indo. Quando precisar do meu pau de novo... é só me avisar."

        mes "Obviamente eu farei isso. Agora vá."

    scene black with Dissolve(3.0)

    pause

    scene sayuri9_mc1 with Dissolve(3.0)

    pause

    "Um Imortal da Cidade Chinesa."

    "Quem imaginou que eu viveria assim?"

    "Às vezes eu penso em como tudo teria sido diferente se eu tivesse recusado vir pra cá."

    "Mas quando eu olho pro lado e vejo o que eu conquistei, eu sei que fiz a escolha certa."

    "Amor, riqueza, poder, respeito... o que mais um homem pode querer?"

    "Daquele garoto que chegou sem nada nessa capital imensa... tendo que aguentar todo mundo tirando sarro de mim..."

    "... em um Imortal da Cidade Chinesa. O posto mais alto dessa cultura milenar."

    if sayuri_casamento:

        "E uma esposa incrível que eu amo."

    "Caraca... eu ainda não acredito..."

    "Essa é a história que eu construi pra mim. Minha história. A história de [mcc]."

    scene black with Dissolve(3.0)

    pause

    "{i}FIM{/i}"

    pause

    p "Parabéns por chegar ao final... mas que finalzinho... hein?"

    p "Imortal... qual a graça de viver imutável dessa forma?"

    p "A vida é cheia de possibilidades. Por que você se colocaria em uma gaiola como essa?"

    p "Pensa em todas as mulheres e homens que você pode conhecer, todas as intensas emoções que te esperam."

    p "Quais outras dezenas de finais diferentes existem no seu futuro?"

    p "Eu permito que você volte e tente outros destinos. Destinos que serão muito interessantes para você."

    p "Mas principalmente para mim."

    p "Aqui mesmo na sua relação com a Sayuri... existem tantas possibilidades. Não aceite a primeira!"

    p "Vou continuar de olho em você, gato!"

    $ renpy.full_restart()

label sayuri9_final2:

    $ sayuri_fim = True

    mc "[xu]!"

    scene black with dissolve

    scene sayuri9_xiangu5 with Dissolve(1.0)

    xu "Olhando pra você... fico imaginando como continua vivo depois de desafiar a Mestra..."

    mc "Não é comigo que você vai falar."

    xu "Você!"

    play sound som_23_passos1

    scene black with dissolve

    scene sayuri9_xiang1 with Dissolve(1.0)

    pause

    xu "Voltou aqui para negar tudo o que eu acredito?"

    i "A [i] não acredita que você continua tonta desse jeito."

    xu "Quem é tonta aqui?! Você acha mesmo que vindo aqui uma vez você ia mudar tudo o que eu aprendi?!"

    i "Você pelo menos pensou no que a [i], o [mc] e o velho disseram?"

    xu "Claro... eu refleti muito sobre tudo aquilo... mas ainda não cheguei numa resposta..."

    xu "Por um lado, eu sinto que os Escolhidos podem ser só uma forma para manipular as pessoas aqui."

    xu "Por outro, nossa luta... suas lembranças do passado... só me provam que a lenda é verdadeira."

    xu "Aquela vez você disse que decidiu viver sua vida longe daqui, uma nova vida!"

    i "Sim. A [i] agora vive a vida dela."

    xu "E eu decidi... que mesmo que eu não seja a verdadeira He Xiangu... eu posso ser ela a partir de agora!"

    mc "A partir de agora? O que você quer dizer?"

    xu "Mesmo que eu não seja uma imortal, as pessoas da Cidade Chinesa não podem perder a figura da He Xiangu."

    xu "Ela traz esperança pra toda essa gente. E, mesmo que eu saiba a verdade no meu coração, viverei essa mentira por eles!"

    i "Então... você aceita viver uma vida que não é a sua. A [i] nunca mais quer fazer isso."

    xu "Você seguiu seu caminho, eu vou seguir o meu."

    i "A [i] respeita sua decisão."

    xu "Obrigada."

    menu:
        "Eu fico feliz por você, [xu].":


            mc "Meu plano era ter você do meu lado, [xu]... mas se essa é sua verdade, eu fico feliz por você."

            xu "O-obrigada..."
        "Xiang! Era pra ela ajudar a gente!":


            mc "Xiang! Não era pra vocês se entenderem! Ela pra trazer ela pro nosso lado!"

            i "Ela escolheu o caminho dela, [mc]. Não podemos interferir. Você escolhe o seu e eu o meu e ela o dela."

            mc "Droga..."

    mc "Eu só preciso de uma coisa, [xu]. E eu vou ser bem sincero com você."

    xu "Hm?"

    mc "Eu vim derrotar a Mestra Jidao. Eu e a Xiang."

    xu "Repita se tiver coragem!"

    mc "A-aaghh!"

    scene sayuri9_xiang2 with Dissolve(1.0)

    pause

    i "Esse é o caminho que ele escolheu. E se você entrar no meio... a [i] vai desbloquear."

    xu "Ugh! N-nós sabemos o resultado dessa batalha..."

    xu "Por que você quer fazer isso com a Mestra?"

    mc "Eu não posso concordar com o que ela fez com vocês. Com você, e a Fen Ju, a Sayuri e todos os outros do bairro."

    mc "Alguma coisa me diz que vocês vão ser mais felizes sem a Mestra."

    xu "[mc]... você... tá fazendo isso pela gente?"

    mc "Não. Antes eu pensava que sim, mas a verdade é que eu só tô fazendo isso por mim mesmo. Porque eu acho o certo."

    xu "Entendi..."

    menu:
        "E aí? O que vai ser?":


            pass

    mc "E então? Vai deixar a gente passar?"

    xu "Minha missão é proteger a vila dos Escolhidos... mas eu não tenho chances contra ela."

    mc "Então você se rende?"

    xu "Sim. Mas... mesmo que eu fosse párea pra essa garota... eu não tenho vontade de defender a Mestra contra vocês."

    i "..."

    xu "Vocês falaram comigo de uma forma que a Mestra nunca fez. Não me manipularam e respeitaram minha escolha."

    xu "Eu não quero ser inimiga de vocês... pelo contrário..."

    xu "A verdade... é que se fosse possível... talvez eu queria viver com vocês..."

    mc "Viver?!"

    i "Tudo bem."

    mc "Tudo bem o quê?! Você entendeu?!"

    i "Quando acabarmos aqui... você pode voltar com a gente. Vamos morar os três juntos."

    xu "Você... permitiria?"

    i "Sim. Eu sei que o [mc] daria conta de nós duas. Ele é esse tipo de homem."

    scene sayuri9_xiang3 with hpunch

    pause

    mc "Vocês tão decidindo uma coisa dessas sem falar comigo?!"

    xu "Eu... não pensei que isso fosse realmente possível... mas... se os Escolhidos vão acabar com o fim da Mestra..."

    xu "[mc]... você aceitaria me levar? Eu quero conhecer o mundo como ela fez."

    i "Por favor, [mc]. Você fez tão bem pra [i]. Por favor, ajuda ela também!"

    mc "Isso é um absurdo..."

    i "Por favor..."

    "Isso é sério? O que eu falo?!"

    menu:
        "Isso não faz sentido. Descubra sua vida por você.":


            mc "Eu não sou a pessoa pra fazer isso, He Xiangu."

            mc "Fico feliz de você correr atrás das suas coisas e aposto que você vai conseguir."

            i "Ele tá com vergonha... a [i] vai convencer ele e daí você vai poder transar com ele também."

            xu "A-ah..."
        "Tudo bem... eu posso... mostrar o mundo pra você.":


            $ xiangu_namoro = True

            mc "S-se você tá afim... e-eu..."

            i "Eba! A gente vai poder transar os três juntos!"

            mc "[i]!"

            xu "A-ah! E-eu!"

    xu "Ah! Podem passar. A Mestra está na ponte sobre o rio."

    if s9_mestra == 1:

        mc "Aquele rio que ela quase me afogou..."

    mc "O que ela tá fazendo lá? Matando o tempo é que não deve ser... não combina com uma pessoa como ela."

    xu "Não... ela está esperando a [fen]. Elas se encontram toda semana neste horário. Mas a menina sempre se atrasa..."

    mc "O que será que ela quer com a [fen]?"

    xu "..."

    xu "Boa sorte pra vocês dois. A Mestra é a Escolhida mais poderosa, de maior contato com os deuses."

    xu "Eu sei que você é forte... mas ela está em outro nível."

    i "Obrigada. A [i] só vai fazer o que ela sempre faz."

    mc "Vamos torcer pra que eu e a Xiang consiga dar conta dela..."

    xu "Estarei torcendo por vocês. Mas se não nos vermos novamente, eu nunca esquecerei sua coragem."

    mc "..."

    play sound som_23_passos1

    scene black with dissolve

    scene chinatown vila_escada with Dissolve(1.0)

    pause

    mc "[i]... você tá pronta?"

    i "Sim."

    mc "Vamos lá!"

    scene black with dissolve

    scene sayuri_final1 with Dissolve(1.0)

    mes "Fen Ju? Garota, você está atrasada de n-"

    mc "Não é a Fen Ju! Você nunca mais vai falar com ela!"

    mc "Jidao! Eu voltei!"

    if s9_mestra == 1:

        mes "Você?! Como você tá vivo?! Era pra você ter morrido afogado!"

        mc "Dizem que vaso ruim não quebra!"

    mc "Eu vim salvar a Cidade Chinesa do seu julgo!"

    mc "A história de controle e dominação dos Escolhidos que começou lá na época da verdadeira He Xiangu!"

    mc "A família poderosa matou a verdadeira! E criou essa lenda falsa que é usada pelos milênios para escravizar!"

    mc "Esse poder nefasto que começou com aquela He Xiangu inocente que queria o bem da China e que vem manipulando todos até hoje!"

    mc "Eu vou acabar com isso!"

    if s9_mestra == 1:

        mes "Lembra do que eu disse da outra vez? Muita fala... nenhuma ação..."

        mes "Desta vez eu vou garantir que você não sobreviva."
    else:


        mes "Eu pensei que seria mais fácil dobrar você... mas... acho que eu estou ficando mole demais."

    mes "Irei mostrar o que acontece com aqueles que desafiam MEU PODER!"

    mc "Eu sei que não posso vencer você sozinho! Eu sou só um jornalista! Não tenho poderes ou treinos milenares!"

    mc "Mas eu trouxe alguém que tem! Alguém que você despojou quando não precisou mais!"

    mc "E ela voltou pra ser seu pior pesadelo! Xiang! Agora!"

    mes "AAHHN?!!"

    scene sayuri_final2 with vpunch

    i "A [i] não gosta da senhora!"

    mes "Eu sabia que você ainda ia voltar pra me atormentar, criatura do inferno!"

    mes "Você nunca vai me vencer! Você não passa de um monstro!"

    i "A [i] é só a [i]! Você que é feia!"

    mes "Eu treinei minha vida toda para ocupar este lugar! Eu nunca vou deixar uma garota tirar isso de mim!"

    i "Cala a boca e luta!"

    mes "AAAAAAHHH!!!"

    play sound som_hit

    show red with hpunch

    scene sayuri_final3 with hpunch

    mes "UUUGHHH!!!"

    i "Toma essa!!!"

    mc "Xiang! V-você! Você conseguiu! Derrubou ela!"

    mes "Como?!"

    i "Você é forte, mas a [i] é mais."

    scene sayuri_final4 with vpunch

    mes "IDIOTA! Você acha que eu realmente acredito nisso?! Nessa besteira?!"

    i "A [i] não entende o que você tá falando..."

    mes "Não se faça de estúpida! Você se acha a verdadeira He Xiangu, não se acha?!"

    mes "Esse jeito estranho de falar, de agir... como se tivesse fora do lugar! Eu sei que tudo isso é encenação!"

    i "A [i] n-"

    mes "Cala a boca! Por que eles não se livraram de você depois que te usaram?!"

    mes "Eles nunca deviam ter deixado você sair daquele quarto, daquela cama!"

    i "A [i] saiu do quarto branco... e não quer voltar mais lá! Nunca mais!"

    mes "Você pode morrer! Você não me interessa mais! Sua função neste mundo acabou!"

    i "De jeito nenhum. A [i] não vai sumir. A vida começou agora. E isso graças ao [mc]."

    i "Então a [i] vai ajudar ele a fazer o que ele quer. E ele quer acabar com você."

    mes "Haha... ridículo..."

    mes "Muito bem... minha família está no controle da comunidade desde o começo da lenda."

    mes "Nós acabamos com a He Xiangu uma vez... vamos acabar com ela de novo..."

    mes "Eu vou fazer o que eu tiver que fazer... pra garantir que a ordem e a prosperidade continue!"

    mes "Isso aqui era pra menina... mas... vai acabar ficando"

    mes "Não imaginei que eu teria que usar isso também... mas você não me deixa alternativa."

    scene black with dissolve

    scene sayuri_final5 with Dissolve(1.0)

    mes "Se eu preciso do seu poder para derrotar você, eu aceito."

    menu:
        "Eu preciso ver o que acontece...":


            "O que ela tá bebendo?"

            mes "{i}glub glob{/i}"

            "Isso que ela tá tomando... só poder ser a mesma coisa que eles deram pra-"

            i "Não importa o que você tome. A [i] vai continuar lutando!"

            mes "Claro que vai... agora venha... vamos continuar, garota."

            i "Sim!"
        "Xiang! Não deixa ela tomar!":


            mc "Xiang! Ataca ela! Não deixa ela tomar!"

            i "Sim!"

            mes "Hm?!"

    scene sayuri_final6 with hpunch

    mes "Sou a líder dos Oito Imortais, Jidao Zhongli, aquela que pode transformar tudo em ouro."

    mes "Esse é meu poder final, eu vou transformar a mim mesma em ouro. E despertar toda minha capacidade!"

    i "Você falou demais! A [i] tá cansada."

    mes "HAHAHAHA!"

    scene sayuri_final7 with hpunch

    i "Aaiiii! Isso dói!"

    mes "Claro que dói! Isso é poder de verdade!"

    mes "Eu sinto! O resultado do meu investimento!"

    mes "Se essa droga faz aquilo com uma adolescente completamente incompetente, imagina com uma mulher como eu!?"

    mes "Eu sou imparável!"

    i "É... parece que a [i] não é párea pra ela assim, [mc]. E agora?"

    "Isso não é bom! Se nem a [i] conseguir dar um jeito nela, quem que vai?!"

    "Eu tenho que fazer alguma coisa também! Eu não posso ser apenas um peso morto aqui!"

    "Se eu atacar ela agora que ela tá ocupada com a [i], eu posso fazer a diferença."

    "Mas se não der certo... ela pode me matar..."

    "Ou tem outra forma que eu possa ajudar? Algo que eu sou melhor?"

    "Tudo o que eu fiz aqui pode decidir a coisa toda de um lado ou pro outro! E agora, [mc]?!"

    menu:
        "Atacar ela":


            "Não importa se eu sou só um paprazzo que nunca lutou na vida! Eu preciso fazer minha parte!"

            mc "A [i] não tá sozinha! Se prepare!"

            mes "Que piada!"

            mc "Você tem um olho nas costas?!"

            mes "Idiota! Você não passa de um inseto!"
        "Conversar com ela":


            $ sayuri9_mc_fala = True

            "Não adianta eu atacar... eu não sou como elas... eu sou um paparazzo... eu só ia passar vergonha."

            "O que não quer dizer que eu não posso fazer nada..."

            scene black with dissolve

            scene sayuri_final8 with Dissolve(1.0)

            mc "Se eu entendi bem, Jidao... você é descendente da família que matou a verdadeira He Xiangu."

            mes "Incrível que você conheça essa história. Não é isso que ensinamos pra [i] e nem pra outra coitada."

            mc "A [i] lembrou quando pegou no quimono. Ela sabe a verdade que se passou há milhares de anos."

            mes "Vai me dizer que você também acredita nessa história de imortal..."

            mc "Não é essa a questão... se você realmente é daquela família... e sabia de tudo..."

            mc "Você sempre fez a He Xiangu achar que era a verdadeira... mesmo sabendo que ela tava morta."

            mes "A imagem da He Xiangu precisa existir pra deixar todos em seus lugares. A boa, a bela, a perfeita He Xiangu."

            mes "Quem controla a imagem da He Xiangu controla a verdade da religião e a mente do povo!"

            mes "O que aquela pobre garota ia sofrer é pouco perante o que eu ia conseguir!"

            mc "Você nem ligou pros sentimentos dela! Assim como você não ligou pra Xiang! Nem pra Fen Ju! E nem a Sayuri!"

            mc "Pra você, todos são só peças no seu tabuleiro! Pra você usar como lhe convém!"

            mes "Diga o que quiser! Eu faço o que preciso pelo bem da Cidade Chinesa! Nossa comunidade é mais importante que qualquer um individualmente!"

            mc "A He Xiangu falou isso pra gente hoje... que ela continuaria com a mentira pra salvar todos..."

            mc "Ela tava pronta pra assumir essa responsabilidade. E a Fen Ju se esforça, ela também se preparou pra desistir do sonho pelo bairro."

            mc "Até o Bao que era alguém grande aqui, agora tem um novo papel e tá confortável."

            mc "Sem falar da Sayuri, que vai assumir o lugar da senhora."

            mc "Todo mundo aqui está se doando pela comunidade. E você? O que VOCÊ deixou pra trás em prol dos outros?"

            mes "!!!"

            mc "Porque eu só vejo a senhora manipulando. Você mesma não acredita na capacidade dos outros! Você vive controlando e obrigando!"

            mc "Eu aposto que a Cidade Chinesa seria muito mais próspera fora do seu controle!"

    play sound som_hit

    scene red with vpunch

    scene sayuri_final21 with vpunch

    mc "Ai!"

    mes "Eu vou te matar, idiota!"

    mc "D-desculpa!"

    "Eu devia ter pensado melhor! Ela vai me matar de verdade!"

    mc "Eu fiz o que eu achei certo! E n-não tenho medo de morrer!"

    mes "Bom pra você!"

    play sound som_espada

    scene red with vpunch

    mc "!!!"

    scene sayuri_final9 with vpunch

    mes "O que você pensa que tá fazendo?!"

    xu "Você não vai matar ele!"

    if sayuri9_mc_fala:

        xu "O que ele falou é verdade!"

        "Ela tava escutando! Eu sabia! Meu plano deu certo!"

        mes "Tudo o que ele fala é descartável."

        xu "Exatamente... é isso que você pensa de todas nós. Somos só peças pra você."

        xu "E você vem fazendo isso desde o começo!"
    else:


        xu "O [mc] e essa garota me respeitaram como você nunca fez!"

        xu "Pra você, todas nós somos descartáveis! Apenas peças!"

    xu "Eu entendi a verdade sobre mim hoje! Eu amo a Cidade Chinesa, mas isso não quer dizer que eu amo você, Jidao!"

    mes "EU sou a Cidade Chinesa! Sem mim, não existe nada!"

    mc "Não é verdade! A sua cultura é milenar! Você mesmo disse isso!"

    mc "Você é apenas uma página nessa história! Uma página que nós vamos virar hoje!"

    mes "E como vocês pretendem fazer isso?! Todos vocês! Todos vocês serão passado!"

    scene sayuri_final10 with vpunch

    xu "Ah... eu devia saber que eu não teria chance..."

    menu:
        "Você ou a Xiang sozinhas não. Mas juntas vai dar bom!":


            pass

    mc "Confia em mim, [xu]! O Bao Chang disse que vocês duas juntas podiam fazer isso! As duas Flor-de-Lótus!"

    i "O velho..."

    xu "Se ele disse..."

    scene black with dissolve

    scene sayuri_final11 with Dissolve(1.0)

    i "A [i] vai tentar de novo."

    xu "E dessa vez eu tô com você!"

    mes "Não importa se é uma de cada vez ou juntas! O resultado vai ser o mesmo!"

    mes "Vocês três morrem aqui! E a Cidade Chinesa vai continuar seu caminho pra prosperidade!"

    scene sayuri_final12 with vpunch

    i "Você fala demais!"

    xu "É hora de tomar uma atitude!"

    mes "AAAARRRGGH!!!"

    mes "Venham, traidoras inúteis!"

    "Velho Bao! Eu confiei em você! Isso tem que funcionar!"

    mc "Força, garotas!"

    mes "Eu não vou morrer aqui! Eu não posso perder! Eu sou a líder! A verdadeira escolhida!"

    xu "IAAAHHHH!!!"

    i "Iá..."

    mes "VENHAMMM!!!!"

    play sound som_espada

    scene red with vpunch

    pause

    i "Aiii!"

    xu "Aaaghh!!"

    mc "!!!"

    play sound som_hit

    scene sayuri_final13 with vpunch

    pause

    mes "KAH!!!"

    mc "Isso! Vocês conseguiram!"

    xu "Nós três conseguimos."

    i "Mas a [i] que fez mais."

    xu "Verdade..."

    mc "Hahaha..."

    mes "Não... não foi pra isso que eu trabalhei todos esses anos..."

    mes "Eu estou tão perto... de ir pra China... de me tornar alguém... "

    mc "Você só tá colhendo o que plantou. Você tratou todos como objetos descartáveis, não espere carinho agora."

    mes "Ugh..."

    i "O que você vai fazer com ela, [mc]? Matar?"

    xu "Tenha piedade, [mc]. Ela sempre cuidou do bairro... mesmo que tenha sido do jeito distorcido dela."

    menu:
        "Vamos expulsar ela da Cidade Chinesa.":


            mc "Se a gente expulsar ela, nos livramos do controle e é o suficiente. Ela nunca vai poder manipular as pessoas de novo."
        "Vamos matar pra que ela não se vingue.":


            mc "Uma pessoa maliga como ela não pode ter uma segunda chance. Vamos matá-la!"

            "???" "MATAR?! Você tá se ouvindo?!"

            mc "?!"

    "???" "Vocês ficaram loucos?!"

    mc "!!!"

    scene sayuri_final14 with hpunch

    pause

    s "O que significa isso?!"

    mc "S-sayuri..."

    s "[mc]! O que você tá fazendo aqui?! Mestra?!"

    mc "Eu vim fazer o que eu disse. Colocar um fim nisso tudo. A chave tá com a Jidao, então eu tô tomando dela!"

    s "Isso é um absurdo! Isso é contra a lei! Agredir uma pessoa assim!"

    mc "[s]! O que ela faz é contra todas as leis! Não é essa a questão!"

    i "Além de que ela merece..."

    s "Você tá se ouvindo, [mc]?! Atacando uma senhora porque você discorda do que ela tá fazendo?!"

    menu:
        "Você sabe que é muito mais que isso!":


            mc "Quem dera fosse simples assim! Você sabe tudo o que ela fez!"

            mc "Ela mesma admitiu falando com a gente!"
        "Eu não admito que você me torne o vilão!":


            mc "Eu não sou o vilão aqui, [s]! Não adianta você querer virar o jogo!"

            mc "Essa velha é o problema da Cidade Chinesa! Nem vem!"
        "Será que ela tem razão?":


            "Será que a [s] tá certa? Eu... cruzei alguma linha?"

    scene black with dissolve

    scene sayuri_final15 with Dissolve(1.0)

    s "Independente se o que ela faz é certo ou errado! O que eu vejo aqui são três adultos atacando uma senhora!"

    s "Em que mundo vocês acham que vocês vivem?! Em um filme?!"

    mc "A gente tá do lado certo! E você tá protegendo a abusadora!"

    s "Então é isso?! Como você acha que tá do lado certo, você pode vir aqui e atacar uma pessoa?!"

    s "Eu não sei o que deu em você, mas esse não é o [mc] que eu conheço."

    s "Quando eu te conheci, você era um cara bacana, preocupado com os outros. Você não saía por aí batendo nas pessoas!"

    mc "Esse é o único jeito de salvar a Cidade Chinesa! Você não vê porque a Mestra te cegou!"

    s "Você tá tão cheio de si que até quem discorda de você só pode tá cego... que decepção, [mc]."

    xu "..."

    i "Por um lado ela tem razão, [mc]... a [i] só tá batendo nela porque ele pediu."

    mc "[i]!"

    s "O que me deixa com mais desgosto é pensar quem te deu o direito pra agir como um vingador em nosso nome!"

    s "Eu nunca te pedi isso! E aposto que a [xu] também e nem a [fen]!"

    s "Você decidiu que ia fazer isso e pro inferno os outros! Você é um mesquinho egoísta!"











    menu:
        "E o que você sugere? Parar tudo aqui?":


            pass

    scene black with dissolve

    scene sayuri_final16 with Dissolve(1.0)

    mc "Você quer que a gente pare e vá pra casa? É isso que você tá falando? Desistir agora?!"

    s "Claro! Acabar com essa bagunça! Com essa justiça com as próprias mãos!"

    s "O que vocês me dizem, meninas?"

    i "A [i] faz o que o [mc] falar. A [i] tá aqui pra ajudar ele."

    xu "Eu entendo o que você diz, [s]... mas eu tomei minha decisão. Eu quero ficar do lado do [mc]."

    mc "Valeu, garotas."

    s "Tá tudo nas suas mãos, [mc]. Seja um adulto e tome a decisão responsável."

    mc "Eu não acredito que você viu toda essa questão assim, [s]..."

    mc "Você que era uma garota tão meiga. Eu sei que no fundo você também tava preocupada com a Fen Ju."

    mc "Até a [i] e a [xu] que tiveram uma educação muito mais fechada e intensa que a sua abriram os olhos."

    mc "Tudo isso é pelo poder? Pra ocupar o lugar da Mestra?"

    s "De novo você tá querendo me julgar?"

    mc "Você tem razão! Eu posso tá puxando o gatilho rápido demais aqui."

    mc "Então me explica! Por que você quer manter o que tá aí sabendo de tudo o que a Jidao fez?!"

    s "..."

    s "No começo, eu tinha medo da Mestra. Principalmente quando eu era criança. O jeito severo dela me assustava."

    s "Mesmo me esforçando nos treinamentos, eu me revoltava contra ela. Eu não achava justo muita coisa que acontecia."

    s "Com o tempo, esse sentimento mudou. E foi você que me ajudou a entender isso, [mc]."

    s "Você me ensinou que eu não precisava correr atrás da aprovação de ninguém. Você me deu força pra seguir meu caminho."

    s "E quando eu olhei pra dentro de mim... eu vi que a Mestra tinha me transformado em uma mulher completa."

    s "Eu tinha vencido na vida, e não só profissionalmente na ginástica, mas ela tinha me dado força pra encarar tudo."

    s "Comecei a olhar meu passado de outra forma. A jornada foi árdua, mas ela fez de mim uma pessoa plena."

    s "Eu só precisava ver isso. Eu só precisava ter coragem de olhar pra mim e ver o que eu tinha conquistado."

    s "E pra isso você foi fundamental... você me mostrou que eu já era completa."

    if sayuri_namoro:

        s "Você se tornou meu namorado, não por causa da ginástica ou qualquer coisa. Você me amou pelo que eu era."
    else:


        s "Você se tornou meu melhor amigo, não por causa da ginástica ou qualquer coisa. Você me respeitou pelo que eu era."

    s "E quando eu me respeitei, eu respeitei minha Mestra e tudo o que ela fez por mim."

    s "Eu não quero seguir a Mestra exatamente como ela é. Eu sei que eu posso ser ainda melhor do que ela."

    s "Mas, pra isso, eu não posso negar o caminho que ela trilhou. Destruir as pontes que ela construiu."

    s "Eu quero seguir o caminho dela, do meu jeito, mas sem abandonar tudo de bom que ela fez pra mim."

    s "Podem ter certeza... eu respeito a [i] e a [xu]. Eu respeito a tristeza e o ódio que elas têm pela Mestra."

    s "Não consigo imaginar como elas sofreram e se sentiram rejeitadas. E eu não vou passar a mão na cabeça da Mestra por isso."

    s "É por isso que eu quero fazer diferente. Só que bater nela? Implodir tudo pra começar do zero? Como isso é melhor?"

    s "Você perguntou qual era minha sugestão. Eu repito: deixe tudo como está."

    s "A Mestra vai pra China. Vai continuar a missão dela. E eu serei a nova responsável pela Cidade Chinesa. E vou continuar a minha."

    s "Todos nós poderemos continuar nossos sonhos."

    xu "Essa parece ser uma decisão honrada."

    mc "E a Fen Ju?"

    s "Ela continua treinando. Ela pode não querer hoje, mas no futuro ela vai entender a responsabilidade dela."

    s "Quando crescer, ela também poderá seguir o sonho dela."

    s "Pare de se achar o justiceiro, o correto. E deixe sua 'justiça' pra lá. Pense no que é bom pra todo mundo aqui."

    "Será que a [s] tem razão?"

    "Ou ela tá tentando me manipular? Será que ela é uma versão ainda mais poderosa que a Jidao?"

    "Talvez eu esteja sendo paranóico. O melhor é eu confiar no que ela tá falando?"

    if sayuri_namoro:

        "Será que eu ainda consigo salvar meu namoro com ela? Será que a gente fica junto se eu aceitar?"

    "Mas se eu quero fazer a minha parte pra acabar com os pederosos da ilha... eu vou deixar tudo continuar como tá?"

    label sayuri9_escolha_final4:

        pass

    "Essa é minha decisão final. O que eu faço?"

    menu:
        "A Cidade Chinesa vai mudar. Jidao e Sayuri pra fora!":


            $ sayuri_fim = True
            $ sayuri_final2 = True
            $ persistent.sayuri_final2 = True

            "As coisas não podem continuar como tão. Essa é minha chance de fazer algo por esta cidade."

            "Vai ser triste acabar com a vida da [s]... ela não merecia... mas agora é tarde demais pra ela."

            scene black with dissolve

            scene sayuri_final17 with Dissolve(1.0)

            mc "A Cidade Chinesa vai mudar! Esta cidade tá cheia de pessoas que querem que tudo fique como tá!"

            mc "Eu não vou fazer parte disso! Eu quero quebrar essas amarras!"

            mc "[s]! Jidao! Vocês duas estão expulsas do comando da Cidade Chinesa!"

            s "Ah!!!"

            mes "F-fedelho!"

            xu "!!!"

            i "..."

            s "Como você pode fazer isso?!"

            mc "É tarde demais pra você, [s]! Me perdoe! Você é uma pessoa incrível, mas tá perdida demais nas palavras da Jidao."

            mc "Eu não posso vocês duas continuarem fazendo o que querem por aqui... me desculpe..."

            mc "Se a escolha é minha... eu tenho que escolher o que eu acho certo. E o certo, pra mim... é acabar com tudo."

            mc "Dar uma nova chance pra este bairro recomeçar. Sem o controle de pessoas como a Jidao."

            mc "Foi a família dela que matou a He Xiangu há milhares de anos e ela vai continuar matando a esperança pra continuar mandando."

            scene black with dissolve

            scene sayuri_final18 with Dissolve(1.0)

            s "Isso é um absurdo... quem você pensa que é pra fazer uma coisa dessas?! Você é só um paparazzo!"

            s "Vá escrever suas baboseiras para que os outros percam o tempo delas lendo!"

            xu "[s]..."

            s "[xu]! Você não vai ficar do lado desse inútil, vai?!"

            xu "Você... você tá fora de si agora..."

            s "Claro! Como você pode?! Depois de todos esses anos?!"

            xu "Essa foi minha decisão. Respeite ela, [s]."

            i "Se o [mc] decidiu. Então está feito. As duas! Estão banidas pra sempre!"

            xu "Vocês podem pegar suas coisas..."

            s "Como..."

            mes "..."

            mc "Então é isso... vamos..."

            s "[mc]..."

            scene black with Dissolve(3.0)

            scene sayuri_final19 with Dissolve(3.0)

            "Com a ajuda das duas, eu consegui limpar a Cidade Chinesa da família que dominava o bairro há tanto tempo."

            "O que a Mestra fez contra as duas, usando elas como objetos, acabou sendo a própria derrota dela."

            "Sozinho, eu não tinha como fazer qualquer coisa. Mas com as duas... parece que nada é impossível."

            "O Bao não ficou nem triste e nem feliz com o resultado... só disse que eu tenho que viver com as consequências do que eu escolhi."

            "A Xiang e a He Xiangu querem viver comigo... "

            if xiangu_namoro:

                "Eu decidi que vou namorar a He Xiangu também... mostrar o mundo lá fora."

                "E agora as duas querem viver comigo... onde eu fui me meter?"

                if casa:

                    "Sorte que eu tenho um apê gigante que dá pra morar nós três."
                else:


                    "Meu apartamento não cabe nós três!"

                    "Assim que eu conseguir um apê maior eu chamo as duas."
            else:

                "Eu não aceitei ficar com a He Xiangu, então espero que ela consiga trilhar o caminho dela sozinha."

                "Agora... a Xiang... essa vai ser difícil de largar do meu pé..."

            "A Xiang planeja ir pra China descobrir a história da He Xiangu verdadeira, que viveu milhares de anos atrás."

            "Eu ainda não consigo entender o que passa com essa aí."

            "Será que eu ainda vou descobrir que tal de sala branca é essa que ela falou? O que fizeram com ela?"

            "Já a He Xiangu ainda tem coisas a fazer parece... conhecer o mundo é apenas a primeira delas."

            "Eu sinto que ainda tem um pedaço no quebra-cabeça dela..."

            scene black with Dissolve(3.0)

            scene sayuri_final20 with Dissolve(3.0)

            pause

            "Quanto a [s]... eu nem sei o que dizer..."

            "Eu nunca imaginei que aquela garota tímida e incerta ia se tornar uma mulher assim."

            "Não posso negar que ela cresceu e encontrou seu caminho. Ver ela defendendo o que ela acreditava daquela forma... foi até inspirador."

            "Uma pena que ela escolheu o caminho errado..."

            "Eu não sei o que vai ser dela e da Mestra agora. Se elas vão pra China... ou tentar ter uma vida normal."

            if sayuri_namoro:

                $ sayuri_namoro = False
                $ sayuri_terminou = True

                "Claro que nosso namoro foi pro saco também..."

            "Fico pensando se eu ainda vou encontrar ela um dia. Se a gente vai ter a chance de conversar sobre tudo isso."

            "Por que a Mestra escolheu ela? Será que ela também pelo mesmo processo da Fen Ju? Por isso ela era tão boa na ginástica?"

            "Bom... esse é o fim da minha relação com ela. Até que o futuro traga alguma surpresa."

            "Adeus, [s]."

            scene black with Dissolve(3.0)

            pause

            "???" "Mademoiselle! Non! Non!"

            scene sayuri_final22 with Dissolve(3.0)

            pause

            "Logo depois, eu descobri que a Fen Ju tinha voltado pra casa dos pais. Eles não entenderam o que aconteceu, mas ficaram felizes."

            "Ela contou que eles não sabiam nada que acontecia. Acharam que os machucados eram só coisa dos treinos puxados."

            "A primeira coisa que ela fez foi voltar pro balé. Ela e a professora Shoshana se tornaram grandes amigas."

            "Ela estranhou como as habilidades da Fen Ju tinham regredido em tão pouco tempo... ela estava com certas dificuldades motoras."

            "E não foi só isso. Com o tempo... eu notei que os machucados dela desapareceram... assim como a cor dos seus olhos estava diferente."

            fen "Eu nunca gostei da cor deles... eu queria ter uma cor igual da minha treinadora e da Mestra. Eles eram tão lindos!"

            "Eu nunca tinha notado que a Sayuri e a Jidao tinham a mesma cor... tinha mais alguém com essa cor lá. Era a He Xiangu? Não... não lembro agora."

            "Enfim... foi muito legal ver a Fen Ju feliz! Finalmente ela vai poder realizar o sonho dela!"

            "Isso se ela conseguir dançar balé agora que é uma 'garota comum'..."

            "Tomara que dê tudo certo pra ela!"

            "Já eu... vou tomando meu rumo."

            mc "Até mais, garotas! Semana que vem eu passo aqui!"

            fen "T-tá! Até semana que vem, [mc]!"

            "Shoshana" "Estarei esperando! Au revoir!"

            scene black with Dissolve(3.0)

            pause

            scene c_chinesa predios with Dissolve(3.0)

            "Por enquanto... minha jornada na Cidade Chinesa chegou ao fim. Foi uma aventura e tanto."

            "Será que eu fiz o certo? Será que eu livrei o bairro do mal ou destruí a base que fazia tudo dar certo?"

            "Certo ou não... esse foi apenas um dos rolos que eu me meti."

            "Essa cidade ainda tem muita coisa pra eu resolver."

            "Sem a Mestra, a Capital perde um de seus poderosos. Quantos faltam? Será que eu vou conhecer os outros?"

            "E se eu... de alguma forma... pudesse derrubar todos eles?"

            "Será que esta cidade corrupta pode mudar?"

            "Ou seria melhor parar de sonhar e pensar em um destino que seja bom pra mim? Mesmo que seja do lado deles?"

            "Ainda falta muita coisa pra mim. A capital que me aguarde. [mcc] vai deixar sua marca."

            "A Cidade Chinesa viu do que eu sou capaz. Quem vai ser o próximo?"

            scene black with Dissolve(3.0)

            $ tempo = 4

            jump call_cidade
        "A Sayuri vai continuar o legado e tudo fica como tá.":



            $ sayuri_namoro = False

            mc "Você tem razão. Destruir tudo não é a melhor forma de ajudar todo mundo."

            mc "O Bao disse que eu tenho que esvaziar a xícara e aceitar vocês também. Então eu vou fazer isso."

            s "Então... ainda tem um pouco do [mc] que me... conquistou... dentro de você."

            xu "Eu estou de acordo. O que a Jidao fez foi errado, mas o bem da Cidade Chinesa vem em primeiro lugar."

            i "A [i] só tá acompanhando o [mc]. Então... tanto faz."

            mes "Nng..."

            mc "E você... vê se aprende algo com isso."

            mes "Não tente ser engraçado, fedelho... você pode ter dado sorte hoje, mas isso não acaba aqui."

            s "Mestra..."

            "Será que realmente foi uma boa eu deixar ela livre?"

            s "[mc]... será... que eu podia falar com você a sós?"

            "O que será que a [s] quer agora?"

            mc "Sim..."

            s "Vem... vem aqui comigo."

            mc "Bom... agora que tudo está resolvido... eu vou conversar com ela e daí vamos pra casa, tá?"

            i "Sim! Vamos comemorar transando no chuveiro!"

            mc "X-xiang! D-do que você tá falando?!"

            if sayuri_namoro:

                s "Bom saber... que você fazia esse tipo de coisa, [mc]... enquanto a gente namorava..."

                mc "[s]! Você vai acreditar em tudo o que essa doidinha fala?!"

                s "..."

            mc "E você, [xu]?"

            if xiangu_namoro:

                xu "É..."

                i "Você disse que ia mostrar o mundo pra ela!"

                mc "Se você quiser..."

                xu "E-eu... eu quero..."

                i "Legal!"

                if casa:

                    i "Vamo todo mundo pro apartamento gigante do [mc]!"

                    mc "Ok..."
                else:


                    mc "Meu apartamento não cabe nós três!"

                    mc "Assim que eu conseguir um apê maior eu chamo as duas."

                    i "A Xiang e a He Xiangu vão tá te esperando então! Você vem comigo enquanto isso, né?"

                    i "Eu vou te ensinar como ganhar dinheiro na rua."

                    mc "X-xiang!"

                xu "Então... eu vou com a [i]..."

                mc "Quero só ver como vai ficar isso..."
            else:


                xu "Como o [mc] disse que não poderia me... mostrar o mundo... então... eu seguirei meu destino sozinha."

                xu "Se as coisas vão continuar como estão... eu pretendo continuar aqui."

                xu "Eu quero ajudar a [s] a escrever essa nova página da Cidade Chinesa."

            mc "Ok..."

            i "Fica bem, amiga."

            xu "Você também... obrigada mais uma vez a vocês dois."

            xu "E... venham me visitar um dia."

            i "Ok. A gente se vê depois, [mc]!"

            jump sayuri9_final3

label sayuri9_final3:

    $ sayuri_fim = True
    $ sayuri_final3 = True
    $ persistent.sayuri_final3 = True

    scene black with Dissolve(3.0)

    play sound som_23_passos1

    pause 2.0

    scene sayuri_final3_img1 with Dissolve(2.0)

    pause

    mc "Então..."

    if s9_mestra == 1:

        s "Você foi contra a Mestra Jidao... fez toda aquela farra... duvidou da gente..."

        mc "Sayuri..."

        s "Mas no final você aceitou a gente. Eu... eu só posso agradecer você por isso."

        menu:

            "E o nosso namoro? A gente não pode ter outra chance?" if sayuri_namoro:

                mc "Eu quero saber da gente. Do nosso amor. A gente não pode ter outra chance?"

                s "Não... por favor... não torne isso mais doloroso do que já tá sendo. Não..."

                s "Eu agradeço por você ter ouvido a razão, mas eu não consigo mais ver você com os mesmos olhos."

                s "O que eu sinto por você nunca vai mudar. E eu nunca vou esquecer você."

                mc "Olha aí!"

                s "Espera... E e-eu espero que eu tenha mudado você de alguma forma também."

                s "Mas agora a gente vai seguir por caminhos diferentes."

            "E a nossa amizade? Vai tudo acabar aqui mesmo?" if not sayuri_namoro:

                mc "S-sayuri... e nossa amizade?"

                s "Eu agradeço por você ter ouvido a razão, mas eu não consigo mais ver você com os mesmos olhos."

                s "O que eu sinto por você nunca vai mudar. E eu nunca vou esquecer você."

                mc "Olha aí!"

                s "Espera... E e-eu espero que eu tenha mudado você de alguma forma também."

                s "Mas agora a gente vai seguir por caminhos diferentes."
            "...":


                pass

        mc "Tudo bem... então esse é o fim..."
    else:


        s "No fundo eu sabia que você não ia aceitar viver pra sempre aqui com a gente."

        s "Você é um espírito livre, [mc]. E eu vejo um destino incrível pra você."

        mc "[s]..."

        if sayuri_namoro:

            mc "É uma pena que a gente não possa continuar namorando..."

            s "Sim... você me perdoa? Pra mim... esse é o destino que eu escolhi pra mim."

            mc "Claro que eu entendo... eu só... queria poder continuar com você."
        else:


            mc "É uma pena que a gente não possa continuar nossa amizade... igual sempre foi."

            s "Sim... você me perdoa? Pra mim... esse é o destino que eu escolhi pra mim."

            mc "Claro que eu entendo... eu só... queria poder continuar igual sempre!"

        s "Olha..."

    s "Eu... queria que você soubesse que você foi muito muito importante pra mim."

    s "Tudo teria sido diferente sem você. Eu não teria me tornado a mulher que eu me tornei."

    s "Mesmo seguindo rumos diferentes, você com a sua vida, e eu com a minha, um pedacinho seu sempre vai tá comigo."

    s "Tomara que um pedacinho meu também vá com você..."

    mc "Eu... parece que você encontrou seu caminho... escolheu um destino que te faz feliz."

    mc "Mas eu... eu não me tornei um Imortal e nem mudei a Cidade Chinesa. Eu sinto... que eu não conquistei nada!"

    mc "Será que me falta coragem? Será que, no fundo, eu ainda sou aquele garoto que não sabe nada que chegou na ilha?"

    s "[mc]... pensar assim não tá certo..."

    mc "Mas essa é a verdade, [s]... eu termino tudo isso sem você, e sem ter mudado nada. Eu..."

    mc "A verdade, é que às vezes eu me sinto um palerma... um medroso... um fraco... no fundo... eu não sou um homem de verdade."

    s "Não fala isso, [mc]. Nada disso é verdade."

    mc "Pode parar aí. Eu não quero que você me console. Seria ainda pior pra mim."

    scene black with dissolve

    scene sayuri_final3_img2 with Dissolve(1.0)

    pause

    s "Você tá parecendo eu de antigamente."

    mc "Eu? C-como assim?"

    s "Vencer as Olimpíadas e meu esforço nos treinos... era uma forma de conquistar fora aquilo que eu não tinha dentro."

    s "Eu sentia que precisava mostrar pros outros que era bem sucedida, porque, no fundo, eu me sentia um lixo."

    s "Você me mostrou que eu tinha valor. Eu não precisava da ginástica, medalhas, de sucesso, pra ser uma pessoa de valor."

    s "Você acha que pra ter seu valor você precisa acabar casado com a mocinha? Ou derrotar o vilão?"

    s "Não precisa de nada disso, [mc]. Você tem valor pelo que você é."

    s "Um homem incrível, doce, amável, atencioso, que consegue enxergar os outros."

    menu:
        "Eu não quero ser amável. Eu sou um homem, porra!":


            s "E-eu não entendo muito de homens... você... é o primeiro homem que eu amei de verdade."

            s "Mas... eu posso falar por mim..."
        "Você só tem pena de mim...":


            s "Nada disso. Depois de tão bem que você fez por mim, você não pode pensar assim."

    s "O que me conquistou foi justamente seu jeito. Eu não queria que você fosse nem um pouquinho diferente."

    s "Eu falo do fundo do meu coração. Se você quisesse ter se tornado um Imortal, eu aceitaria ter sido sua pra sempre."

    s "Igual eu disse, eu não sei como pensam as outras mulheres, se elas querem machões, homens frios e violentos."

    s "Pra mim, você é o homem perfeito. A coragem que você teve pra me ajudar durante todo esse tempo... você não vê porque não quer."

    s "A verdade... é que eu fico até com inveja de pensar... que... você vai passar o resto da sua vida com uma mulher que não sou eu."

    s "Ela vai ter um homem de verdade, corajoso, de bom coração, que vai amar ela pelo que ela é, que foi o que você fez comigo."

    mc "Isso se eu não acabar sozinho..."

    s "Só se você quiser."

    mc "Haha..."

    s "É sério!"

    scene black with dissolve

    scene sayuri_final3_img3 with Dissolve(1.0)

    pause

    mc "Não sei se você só tá querendo ser legal comigo... mas o que você disse me deu um novo gás, sabia?"

    s "Se você não tá feliz com alguma coisa em você, sempre dá pra mudar. Eu sei que você tem força pra isso."

    s "Mas... pra mim... você sempre vai ser o homem mais incrível que eu conheci na minha vida. Um homem de verdade."

    mc "Valeu."

    s "E qual caminho você vai seguir agora?"

    mc "Eu não sei. Ainda tem muita coisa pra eu viver aqui na capital."

    mc "Eu ainda não decidi como eu quero que minha história termine. Mas eu quero continuar procurando."

    s "E você vai achar! Uma pena que não seja aqui na Cidade Chinesa, mas vai ser em outro lugar, com outra pessoa."

    s "E... quando você se sentir pra baixo, não esquece o que eu te falei hoje. Você é um homem incrível."

    s "Você mudou a minha vida e isso eu nunca vou esquecer. E eu aposto que você ainda vai mudar a vida de muita gente!"

    s "Nunca perca esse olhar! Esse olhar que vê os outros e não só seus próprios problemas."

    s "Se você continuar assim, quando você finalmente descobrir o seu caminho, o tanto de gente que você vai ter ajudado vai ser enorme!"

    s "Quem dera a gente tivesse outros homens e mulheres como você..."

    mc "Valeu mesmo, [s]. Pode ter certeza que eu nunca vou me esquecer do que a gente passou junto."

    mc "São memórias incríveis que eu vou levar pra sempre comigo."

    mc "E você também. Segue seu sonho e faça o bem pra todas as pessoas aqui!"

    s "Pode apostar. Eu não vou jogar fora o futuro que eu escolhi pra mim."

    s "E não esquece. A Cidade Chinesa vai continuar aberta pra você sempre que você quiser vir aqui."

    s "Espero que um dia você tenha certeza que tomou a decisão certa hoje."

    s "Nós seremos uma comunidade próspera, feliz e honrada. E eu sempre vou ser grata a você."

    s "E agora... chegou a hora... m-mas eu..."

    mc "Eu tô ansioso pra ver o que o futuro reserva pra nós dois! [s]... cuide bem da [fen]."

    s "Eu vou ajudar ela a encontrar o valor dela, dentro dela. Eu te prometo."

    mc "Adeus, [s]."

    s "A-adeus, [mc]..."

    scene black with Dissolve(3.0)

    scene c_chinesa predios with Dissolve(2.0)

    pause

    "Acho que vai ser a última vez que eu vejo a [s]."

    "Agora eu só posso torcer pra que ela seja feliz no caminho que ela escolheu."

    "Eu também vou encontrar meu caminho, [s]. Continue torcendo por mim. E seja feliz pra sempre."

    scene black with Dissolve(3.0)

    jump call_cidade

label sayuri_sexo_final:

    scene black with Dissolve(1.0)

    scene sayuri9_premium1 with Dissolve(2.0)

    pause

    mc "Finalmente eu tenho você aqui... e ninguém pra atrapalhar a gente..."

    s "Não foi só você... eu esperei esse momento por muito tempo também..."

    mc "Eu quero que esta seja a noite mais inesquecível da nossa vida, [s]."

    mc "Uma noite que vai ficar marcada pra sempre."

    s "Ai, [mc]... sempre foi com você que eu quis ter esta noite. A pessoa que eu sempre vou amar..."

    s "Por favor... faz essa ser a melhor noite da minha vida. Eu tô nos seus braços."

    mc "Não só nos braços... você tá nas minhas mãos."

    s "S-sim..."

    mc "Você vai ver o que elas vão fazer com você."

    s "O que el-"

    label say9_premium1_1:

        pass

    menu:
        "Fazer amor e transar intensamente":


            if not premium:

                call mensagem_premium

                jump say9_premium1_1

            scene black with dissolve

            scene sayuri9_premium2 with Dissolve(1.0)

            pause

            s "A-ah!"

            mc "Por mais que eu ame você... essa noite vai ser de outra coisa."

            s "A-ah... s-sim... eu também quero... não quero amor... eu quero tesão, prazer, [mc]!"

            s "Aahnn!"

            mc "Se é o que você quer, eu vou te dar."

            menu:
                "Continuar massageando o clítoris dela":


                    mc "Eu vou começar só te tocando..."

                    s "Ah... nnmm..."

                    mc "É assim que você quer?"

                    s "E-eu... eu quero mais, [mc]..."

                    mc "Entendi..."

                    scene black with dissolve

                    scene sayuri9_premium3 with Dissolve(1.0)

                    pause

                    s "Ngghha!"

                    mc "ASsim, é?"
                "Enfiar os dedos nela":


                    scene sayuri9_premium3 with vpunch

                    pause

                    s "Aiii!"

                    mc "Hoje você quer que eu trate você como você merece, não é?"

                    s "S-sim!"

                    mc "Foi o que eu pensei."

            s "Nnghhh... assim mesmo que eu quero! Eu quero sentir o que eu nunca senti antes!"

            mc "Eu vou dar pra você o que ninguém mais vai te dar! Você vai ver."

            s "Isso! Nngh!"

            mc "A gente nem começou e você já tá ensopada desse jeito!"

            s "A-annghh! N-não fala, assim! E-eu pareço uma safada!"

            mc "E você não é?"

            s "Nggh!"

            mc "Eu sei que você gosta de sentir em outro lugar..."

            s "[mc]... e-eu... ahnn..."

            mc "Gosta, não gosta?"

            s "E-eu..."

            mc "Pode falar... você quer sentir atrás, não quer?"

            s "A-ainn!"

            mc "Se você admitir... eu prometo que eu te coloco de quatro e te dou o que você quer."

            s "Ai... E-eu quero... eu quero sentir no meu outro buraquinho.... nnghh..."

            mc "Eu sabia. Vem aqui, safada."

            scene black with dissolve

            scene sayuri9_premium4 with Dissolve(1.0)

            pause

            s "Isso! Aí! Bem aí!"

            mc "Você sente gostoso assim aqui?"

            s "S-sim! Pode apertar mais!"

            mc "Também... com esse bundão que você tem... sensível desse jeito ainda..."

            s "Nnnmm! N-não fala da minha b-bunda..."

            mc "Ela é maravilhosa, [s]... dá uma vontade de pegar... de apertar... de bater."

            s "Ainn... n-não bate..."

            menu:
                "Eu sei que você quer! Toma!":


                    scene sayuri9_premium5 with hpunch

                    s "Aiinn!!!"

                    mc "Toma um tapão nessa bunda gorda!"

                    s "Ai, [mc]!"

                    mc "Doeu?"

                    s "S-sim! Nnghh!"

                    mc "E aí?!"

                    s "B-bate de novo por favor! Mais forte!"

                    mc "Não acredito como essa bunda é gulosa!"

                    scene sayuri9_premium6 with hpunch

                    s "Aaiiii!"

                    mc "Assim que você queria?!"

                    s "É! Forte assim!"

                    scene sayuri9_premium6 with hpunch

                    s "Aahhhnn!"

                    mc "E agora o prato principal?"

                    s "Hm?"

                    scene black with dissolve
                "Eu vou fazer outra coisa...":


                    mc "Se você não quer que bata... então..."

            scene sayuri9_premium7 with Dissolve(1.0)

            pause

            s "Nnnghhh..."

            mc "Eu tô gostando de ver a verdadeira [s] desse jeito."

            s "A-ahn..."

            mc "Você não sabe como eu tô ficando excitado de transar assim você."

            s "E-eu também... m-minhas pernas tão quase... aah..."

            mc "Imagina quando você sentir meu caralho entrando nesse buraquinho aqui."

            s "Não fala asism... ah... eu n-não quero só imaginar..."

            mc "Verdade? Você quer sentir ele arrombando sua bunda, quer?"

            s "Isso... nnmm... a-arrombando aí atrás... p-por favor..."

            menu:
                "Vem aqui me chupar então. Pra eu entrar gostoso.":


                    mc "Então vem... beija meu pau... pra ele ficar lisinho pra você, vem..."

                    s "Eu quero... eu quero sentir você, [mc]."

                    scene black with dissolve

                    scene sayuri9_premium8 with Dissolve(1.0)

                    pause

                    mc "Nggh... agora sim eu tô curtindo..."

                    s "Ele é meu... eu vou cuidar bem dele..."

                    mc "Isso... beija ele... lambe... nnnghh... que boquinha mais gostosa, [s]."

                    s "V-verdade?"

                    mc "Sim. Continua assim que você vai ganhar uma medalha."

                    s "É a medalha que eu mais quero, meu amor... hmm..."

                    scene sayuri9_premium9 with Dissolve(1.0)

                    pause

                    mc "Ah... assim mesmo..."

                    s "Te chupar tá me deixando ainda mais quente, [mc]."

                    mc "Do jeito que você tá hoje, qualquer coisa vai te deixar excitada, linda."

                    s "Ngh..."

                    mc "Eu prometo que você vai ser recompensada."

                    s "E-eu... n-não aguento... e-eu preciso..."

                    mc "Precisa do quê?"

                    s "P-preciso sentir aqui atrás... entrando em mim..."

                    menu:
                        "Calma. Ele vai entrar. Mas primeiro chupa gostoso.":


                            mc "Não para ainda. Chupa com vontade que logo logo ele vai tá dentro dessa bunda gostosa."

                            s "Nnghh!"

                            scene sayuri9_premium10 with Dissolve(1.0)

                            pause

                            s "{i}sssllhhpp{/i}"

                            mc "A-ah! Assim mesmo, [s]!"

                            mc "Onde você aprendeu mamar desse jeito? Que delícia!"

                            s "Mmnnnhh..."

                            mc "N-não precisa responder. Só continua assim! Ah!"

                            s "Nnnghhh!"

                            mc "É tão gostoso assim mamar meu caralho? Você tá gemendo tanto."

                            s "Uhumm..."

                            mc "Hm?"

                            scene black with dissolve

                            scene sayuri9_premium11 with Dissolve(1.0)

                            pause

                            s "Ah... nnghh..."

                            mc "O que você tá fazendo enquando me chupa, hein?"

                            s "Nhhããoo..."

                            mc "Certeza que não tá fazendo nada? Não tá brincando sozinha, não?"

                            s "N-nanã... ahn..."

                            mc "É assim que você faz sozinha, é?"

                            s "Ah... aahnn..."

                            s "E-eu... não faço... nnghh... nada assim..."

                            mc "Não enfia seus dedinhos no seu cuzinho, não?"

                            s "N-não... ah..."

                            scene sayuri9_premium12 with Dissolve(1.0)

                            pause

                            mc "Você fica excitada assim, é?"

                            s "Ah... não... nnghh!"

                            mc "Naquele seu quarto... pensando em safadeza... se tocando a noite toda..."

                            s "Anghh... e-eu não faço isso sozinha... n-não me masturbo..."

                            mc "Verdade?"

                            scene black with dissolve

                            scene sayuri9_premium13 with Dissolve(1.0)

                            pause

                            s "O-olha pra mim... v-você acha que eu ia fazer algo assim?"

                            mc "Hmm..."

                            s "É por isso que eu preciso de você, [mc]... e-eu preciso agora agora."

                            mc "Com essa carinha... quem vai recusar?"
                        "Se você não aguenta, então vem aqui!":


                            pass
                "Eu vou enfiar rasgando mesmo!":


                    pass

            mc "Se sua bunda precisa do pau desse jeito... você vai ter o que você quer."

            s "Isso! Eu não aguento mais!"

            mc "Vem aqui."

            scene black with dissolve

            scene sayuri9_premium14 with Dissolve(1.0)

            pause

            mc "Seu buraquinho tá pedindo..."

            s "Vai... eu n-nunca senti um... pênis... aí..."

            mc "Então sua espera acabou..."

            mc "Depois de brincar com ele igual eu brinquei... aposto que ele tá pronto pra me aguentar."

            s "Sim... ele tá... ele te quer, [mc]."

            mc "Um pouco de saliva... e..."

            scene black with dissolve

            scene sayuri9_premium15 with Dissolve(1.0)

            pause

            s "AAAAHHH!"

            mc "Ah! Tô dentro!"

            s "NNGHH!"

            mc "Seu rabo é uma delícia, [s]!"

            s "ISSO! ISSO QUE EU QUEROO!!!"

            mc "Eu vou te comer agora!"

            s "VAI!!! COMEEE!!!"

            scene sayuri9_premium16 with vpunch

            pause

            s "Ahnn! AHNN! Tá comendo minha bunda!"

            mc "S-sim! E ela é uma delícia! NNGHH!!"

            s "Eu vou gozar, [mc]!"

            mc "Calma! Mais um pouco!"

            s "N-não consigo!"





            mc "Que tesão! Você é uma delícia, [s]!"

            s "Ahnn! AAHNNN!!"

            mc "Isso! Geme gostoso que eu fico ainda mais duro!"

            s "Ahnn! AIINN! Eu vou desmaiar assim!!"

            scene sayuri9_premium18 with vpunch

            pause

            s "AAINNMNN!!!"

            mc "Isso! Eu também vou gozar!!"

            s "Ahnn! AAHNN!"

            s "Por favor! Goza na minha bunda! Deixa eu sentir n-nela por favor!"

            mc "Eu tirei a virgindade da sua bunda. Deixa eu tirar a sua virgindade também."

            s "Ai... [mc]... m-mas eu queria... sentir aqui atrás... nngh..."

            s "Além de que... é perigoso... a-ah... eu posso... e-engravidar..."

            menu:
                "Eu quero te engravidar, [s]!":


                    mc "É isso mesmo que eu quero, [s]! Eu quero sua virgindade e engravidar você!"

                    s "Ai, [mc]! E-eu quero ser sua pra sempre!"

                    scene black with dissolve

                    scene sayuri9_premium20 with Dissolve(1.0)

                    pause

                    mc "Ahh!"

                    s "Nngghh!"

                    mc "Não acredito que eu sou seu primeiro, [s]!"

                    s "Sim! Você é meu primeiro e único, [mc]!"

                    mc "Eu tô no meu limite!"

                    s "Então vai! Eu quero fazer você sentir prazer!"

                    mc "Vou gozar!"

                    scene sayuri9_premium21 with hpunch

                    pause 1.0

                    mc "Tomaaa!"

                    mc "NNGHHH!"

                    mc "AAAGHHHH!!! TÔ GOZAANDOOO, SUA GOSTOSA!!!"
                "Tudo bem! Toma seu leitinho no cuzinho então!":


                    mc "Se é aqui que você quer! Então toma! Toma toda minha porra na sua bunda, safada!"

                    s "I-ISSOO!!!"

                    scene sayuri9_premium19 with hpunch

                    pause 1.0

                    mc "AAAGHHHH!!! TÔ GOZAANDOOO, SUA GOSTOSA!!!"

                    s "AAAAIIHH!!!"

                    s "Ai! T-tô sentindo! Tô sentindo em mim! Nnghhh!"

                    s "G-gozando! AAINN! D-de novo!!!"
        "Fazer amor":


            scene black with Dissolve(1.0)

            mc "Que tesão! Você é uma delícia, [s]!"

            s "Ahnn! AAHNNN!!"

            mc "Isso! Geme gostoso que eu fico ainda mais duro!"

            s "Ahnn! AIINN! Eu vou desmaiar assim!!"

            s "AAINNMNN!!!"

            mc "Isso! Eu também vou gozar!!"

            s "Ahnn! AAHNN!"

            menu:
                "Eu quero te engravidar, [s]!":


                    mc "É isso mesmo que eu quero, [s]! Eu quero sua virgindade e engravidar você!"

                    s "Ai, [mc]! E-eu quero ser sua pra sempre!"

                    mc "Ahh!"

                    s "Nngghh!"

                    mc "Não acredito que eu sou seu primeiro, [s]!"

                    s "Sim! Você é meu primeiro e único, [mc]!"

                    mc "Eu tô no meu limite!"

                    s "Então vai! Eu quero fazer você sentir prazer!"

                    mc "Vou gozar!"

                    mc "Tomaaa!"

                    mc "NNGHHH!"

    s "Aahh..."

    mc "Aahh..."

    mc "Nossa... essa..."

    scene black with Dissolve(2.0)

    scene sayuri9_quarto1 with Dissolve(1.0)

    pause

    mc "Essa foi incrível, [s]..."

    s "O que eu fiz hoje... eu só tive coragem graças a vocês... Obrigada, [mc]..."

    mc "Essa deve ter sido a melhor noite da minha vida... eu nunca vou esquecer isso aqui."

    s "Eu também... nunca vou esquecer você..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
