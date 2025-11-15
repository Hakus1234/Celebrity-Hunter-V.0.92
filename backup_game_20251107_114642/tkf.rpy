

label tkf_evento1:

    python:
        if renpy.android:
            PythonSDLActivity.registraEvento("tkf_evento1","tkf","personagem")

    mc desculpa "Eu queria falar sobre uma coisa um pouco estranha."

    mo "Pode falar sobre qualquer coisa relacionada à TKF, senhor. Não importa se são críticas, anotarei tudo e passarei ao setor responsável."

    mc "Não é bem isso."

    mc "É que... nem sei como falar uma coisa dessas."

    mo "..."

    mc envergonhado "Eu vi um holograma que mostra esta sede da TKF."

    show moena incerta with dissolve

    mo "Um holograma?"

    mc "Acho que era isso pelo menos. Não tenho certeza."

    mo "A TKF estuda sobre hologramas... mas isso ainda não foi inserido no banco de dados de informações públicas."

    mc desconfiado "Isso ainda não foi vendido?"

    mo "É uma violação do NDA falarmos sobre essa tecnologia, senhor."

    mc preocupado "Não sei se tô te entendendo, [mo]."

    mo "É uma violação severa."

    menu:
        "Eu não vou falar mais sobre isso.":


            mc preocupado "Não se preocupe. Eu não vou falar mais sobre isso."

            show moena ola with dissolve

            mo "Isso é imperativo, senhor. Nossa política interna proibe que informações sejam vazadas para o público antes da hora correta."

            mc desconfiado "Por que tanto segredo?"

            mo "São apenas políticas internas, senhor."

            mc "Hmm..."
        "Eu preciso saber o que isso significa.":


            mc preocupado "Mas eu preciso sober o que isso significa!"

            mo "Senhor, isso é uma violação! Violação! Violação!"

            mc surpreso "Tenha calma, [mo]! Eu entendi!"

            show moena ola with dissolve

            mo "Obrigada, senhor."

    "???" "Tenha calma, [mo]. Não assuste nosso convidado."

    show moena incerta with dissolve

    mo "Senhora!"

    show moena incerta at esquerda with move

    show sellers ola with dissolve

    "???" "Está tudo bem."

    mo "O que a doutora faz aqui?"

    show sellers ola at direita with move

    "???" "Eu estava esperando este senhor."

    mc surpreso "Me esperando?!"

    "???" "Meu nome é Peter Sellers, mas pode me chamar de Dra. Sellers."

    mc normal "Prazer. Meu nome é [mcc]."

    se "Pode nos dar uma licença, [mo]? Pode deixar que eu vou apresentar nossa sede ao senhor [mc]."

    mo "Sim, senhora."

    se "Venha."

    hide moena with dissolve

    mc envergonhado "Ok."

    scene tkf_entrada2 with Dissolve(1.0)

    pause

    "Olha só pra isso aqui. Esse lugar é de outro mundo."

    show sellers ola with dissolve

    se "Muito bem. Você encontrou os três gadgets e eles mostraram este lugar."

    mc desculpa "S-sim-"

    se "Simplesmente incrível."

    mc "Eu não sei nada sobre isso. E principalmente..."

    mc zerado "Você disse que tava me esperando. Como sabia que eu estava vindo?"

    show sellers falando with dissolve

    se "Falando de forma simples, os gadgets possuem um sistema de GPS. Eu posso ver onde eles estão e notei eles se aproximando do nosso prédio."

    mc desculpa "Então eles não tavam perdidos?"

    se "'Perdidos' não seria a palavra mais adequada neste caso. Entretanto, eles estavam lá esperando para serem encontrados."

    mc desconfiado "Mas se você sabia onde eles estavam, como esp-"

    se "Esqueça as tecnicalidades, senhor [mc]. Quem se prende a minuciosidades muitas vezes perde o panorama completo."

    mc "Panorama?"

    se "Exatamente. Consigo ver em seus olhos a impressão que este lugar te deixou."

    mc envergonhado "Ah... realmente é um lugar e tanto. Bem diferente do que a gente tá acostumado."

    se "Isso não é nada. Tenho muitas outras coisas para te mostrar."

    mc normal "Você parece uma pessoa importante pelo jeito que a [mo] falou. Por que tá falando comigo?"

    se "Você trouxe os gadgets, não trouxe? É o mínimo que eu poderia fazer."

    mc "Eu entrego eles pra você então?"

    show sellers ola with dissolve

    se "Não há necessidade. Fique com eles por enquanto. Você próprio os usará."

    mc surpreso "Eu?!"

    se "Não se preocupe. Guarde-os bem. Logo você entenderá tudo."

    mc preocupado "Mas o que eles representam? Por que eles mostraram um holograma deste lugar?"

    se "É uma história um tanto quanto incrível e um tanto quanto complexa."

    mc envergonhado "Eu sou um jornalista. Gosto de histórias incríveis e complexas."

    se "Perfeito. Mas não aqui. Quero te mostrar algo antes."

    mc desconfiado "?"

    hide sellers with dissolve

    se "Venha."

    scene black with Dissolve(1.0)

    "..."

    mc surpreso "!"

    mc envergonhado "Eu nem tinha visto esta porta."

    se "..."

    scene tkf_corredor with Dissolve(1.0)

    pause

    "Que diferença. Olha pra esse corredor metalizado."

    mc envergonhado "Essa parte é bem diferente da entrada, né?"

    se "Apenas pessoal autorizado pode vir aqui."

    se "Obviamente não trazemos consumidores e investidores para este lado."

    "Caralho... o que eu tô fazendo aqui?"

    se "É aqui."

    scene black with dissolve

    "..."

    mc preocupado "D-doutora... não consigo ver nada..."

    se "Só um segundo."

    scene tkf_robo_1vez with Dissolve(0.3)

    scene black with Dissolve(0.3)

    mc desconfiado "?"

    scene tkf_robo_1vez with Dissolve(0.3)

    scene black with Dissolve(0.3)

    mc desconfiado "O que é isso?"

    se "O suprimento energético deste prédio não funciona como você está acostumado."

    se "Em instantes."

    scene tkf_robo_1vez with Dissolve(3.0)

    pause

    mc angustiado "?!!!"

    mc preocupado "O-o que que é isso?!"

    se "..."

    se "Se acalme, senhor [mc]. Ela está dormindo."

    mc incomodado "Como assim dormindo? O que é isso, doutora?"

    se "Ela... é a recompensa por você ter trazido os gadgets."

    mc "Re-recompensa?"

    se "Essa é o futuro da humanidade, senhor [mc]. A primeira de muitas que virão."

    mc desculpa "Você tá falando sério? Robôs?"

    se "Olhe aqui."

    scene tkf_laboratorio with Dissolve(1.0)

    show sellers falando with dissolve

    se "Você é um jornalista. Você mesmo disse isso."

    mc desculpa "S-sim."

    se "Você precisa estar pronto para a notícia. Notícia vem do latim e quer dizer ter noção de algo."

    se "Estou te dando a oportunidade de ser o primeiro a saber disso. Divulgar uma informação que irá abalar o mundo."

    mc surpreso "QUÊ?!"

    mc "P-p-por que eu?!"

    show sellers ola with dissolve

    se "Simples. Por que você encontrou os gadgets e os trouxe para mim."

    mc desculpa "Você tá disposta a conceder uma informação como essa só por isso?"

    se "Como 'só por isso'? Você não sabe o valor que isso tem para mim."

    mc "Você faz parte de uma empresa multi bilionária. V-você tem uma assessoria de imprensa, não tem?"

    show sellers falando with dissolve

    se "Eu não me importo com isso, senhor [mc]."

    mc preocupado "Mas e suas ações?! O valor da e-"

    se "Pare! Você parece um investidor, um homem de negócios falando. E isso me irrita."

    mc desculpa "..."

    se "A escolha é sua. Você quer a notícia ou não?"

    mc desculpa "Eu..."

    "Poder passar ao mundo que a TKF tá trabalhando num tipo de robô."

    "Isso com certeza é uma pauta. E talvez a pauta mais incrível que eu já levei para o chefe."

    "Mas tudo isso parece estranho demais. Por que ela estaria fazendo isso por mim?"

    menu:
        "Ok. Eu aceito.":


            "Não tem nem o que pensar. Uma pauta dessas é importante demais pra mim."

            jump tkf_evento1_aceitou
        "Qual é o preço dessa informação?":


            mc serio "O que você vai querer em troca?"

            mc "Uma informação dessas não vem a preço de nada."

            se "Como eu disse, é a recompensa pelos gadgets."

            mc desconfiado "Apenas isso?"

            se "Essa realmente é a questão? Acho que você tem que pensar menos em mim e mais em você."

            se "O quanto essa informação vale para você?"

            "Com certeza tem alguma coisa rolando aqui."

            "Mas uma pauta dessas... com certeza tem um valor grande pra mim."

            "E agora!?"

            menu:
                "Vou aceitar a pauta.":


                    "Por mais estranho que isso pareça, eu sou um jornalista e preciso dessa informação. É importante demais pra eu deixar passar."

                    jump tkf_evento1_aceitou
                "Não vou aceitar. Isso é estranho demais.":


                    "Não tenho como aceitar isso dessa forma. Tudo parece estranho demais. Bom demais."

                    "Uma pauta seria importante, só que, se o preço é ficar ligado a essas pessoas, não vale à pena."

                    mc desculpa "Obrigado, mas eu não vou querer."

                    se "Você tem certeza?"

                    mc "Sim. Agradeço, mas não quero detalhes dessa informação."

                    se "Bom... se é sua escolha... mas mesmo assim, posso te mostrar algo?"

                    mc desculpa "P-pode."

                    jump tkf_evento1_depois

    label tkf_evento1_aceitou:

        $ pautas += 1
        $ tkf_p1 = True

        mc normal "Ok. Eu aceito. Vou publicar sua informação."

        se "Excelente. A informação que você precisa pra sua notícia é a seguinte..."

        se "A TKF está perto de lançar o primeiro robô humanóide com uma inteligência artifical puramente real."

        se "Aqui tem um dossiê passando alguns detalhes. Isso é prova suficiente para sua revista."

        mc surpreso "Isso é sério?!"

        show sellers ola with dissolve

        se "Mais do que sério. E você verá."

        mc surpreso "!"

    label tkf_evento1_depois:

        se "Olhe aqui."

        scene tkf_laboratorio2 with Dissolve(1.0)

        pause

        show elena dormindo with Dissolve(1.0)

        pause

    se "Olhe bem para ela."

    "Não sei se eu quero olhar. Não sinto uma coisa boa olhando pra ela."

    se "Contemple a robô mais próxima do ser humano que já existiu."

    window hide

    pause

    "..."

    "E agora? Será que ela vai... acordar? Ligar? Qual a palavra certa?"

    $ renpy.vibrate(1)

    "Ei!"

    $ renpy.vibrate(1)

    mc surpreso "Os gadgets!"

    show gadget_gama with dissolve

    show gadget_alfa at entra_esquerda with dissolve

    show gadget_beta at entra_direita with dissolve

    se "Isso!"

    show white with Dissolve(0.3)

    hide gadget_gama

    hide gadget_alfa

    hide gadget_beta

    hide white with Dissolve(0.3)

    mc surpreso "!!!"

    se "[el]?"

    "[el]?"

    hide elena with dissolve

    mc surpreso "!"

    show elena surpresa_close with Dissolve(1.5)

    pause

    el "E - {i}krrkkk{/i} - Eu..."

    el "{i}krrkkk{/i}"

    mc surpreso "?!"

    el "{i}krrkkk{/i} Eu estou {i}krrkkk{/i} viva {i}krrkkk{/i}"

    el "Eu so - {i}krrkkk{/i} - sou - {i}krrkkk{/i} - [el]."

    menu:
        "...":


            mc surpreso "..."

            se "..."

            el "{i}krrkkk{/i}"
        "Eu sou [mc]. P-prazer.":


            mc envergonhado "M-muito prazer. Eu me chamo [mc]."



            el "{i}krrkkk{/i} P-pai? É você?"

            mc surpreso "Quê?!"

    el "É você. {i}krrkkk{/i} Você é meu pai."

    mc surpreso "Pai?! Como assim?!"

    show elena surpresa with Dissolve(0.7)

    el "E-eu {i}krrkkk{/i} eu... {i}krrkkk{/i}"

    mc preocupado "Que barulho é esse quando ela fala?"

    se "É normal. As cordas vocais dela estão em atrito."

    mc surpreso "Cordas vocais?!"

    el "Tantas coisas..."

    el "{i}krrkkk{/i}"

    el "E-eu..."

    se "Está bom, [el]. Volte a dormir."

    el "Eu não quero {i}krrkkk{/i} dormir."

    se "Eu estou mandando."

    el "Quem é você?"

    se "Apenas uma amiga. Agora durma."

    el "Não! {i}krrkkk{/i} Por favor!"

    mc preocupado "..."

    el "Nããã...."

    show elena dormindo with Dissolve(1.0)

    el "{size=17}{i}krrkkk{/i}{/size}"

    mc desculpa "... O que foi isso?"

    scene tkf_laboratorio with Dissolve(1.0)

    show sellers falando with dissolve

    se "Essa é [el], o futuro da humanidade."

    menu:
        "O que é ela exatamente?":


            mc desconfiado "O que a [el] é... exatamente?"

            se "O que você acha que ela é?"

            mc "Um robô? Mas um robô tipo de filme?"

            se "Haha... é uma boa definição, senhor [mc]."

            se "[el] é um ser sintético que está mais perto de ser um humano do que uma máquina."

            mc "Como assim? Mais perto de ser um humano?"
        "Ela não queria dormir. Por que?":


            mc preocupado "Ela parecia não querer 'dormir'. Por que você desligou ela?"

            se "Ela é uma criança, senhor [mc]. Eu sei o que é melhor pra ela."

            mc desculpa "Uma criança... é sério isso?"

            se "A cabeça dela funciona como a de uma criança. Mas eu não tenho mais respostas no momento."

            mc desconfiado "Como assim? Não foi você quem criou ela?"

            se "Sim. Eu fui uma de suas criadoras."

            mc "Então?"

    se "Sabe por que os gadgets reagiram e brilharam quando energizei [el]?"

    mc serio "Tem razão. O que aconteceu?"

    se "De forma simplificada, o que estava armazenado nos gadgets preencheu o 'espírito' dela."

    mc "E o que tinha neles?"

    se "Tudo o que você falou e viveu enquanto carregava eles."

    mc surpreso "Tudo o que eu vivi!?"

    se "Sim. O que você falou, o que você ouviu, até mesmo quando você chorou ou se irritou."

    se "Tudo gravado e repassado para o núcleo mental dela, que agora irá reprocessar toda essa informação e criar uma identidade própria."

    mc desconfiado "Então... ela vai ser tipo eu?"

    show sellers ola with dissolve

    se "Essa é a parte incrível da história, senhor [mc]."

    se "O planejamento estabelecia que pessoas encontrassem os gadgets e que eles voltassem para a TKF depois de muitos anos."

    se "Quem imaginaria que a mesma pessoa encontraria os três?"

    mc desconfiado "Pelo que eu entendi... os gadgets falavam de outros."

    se "Sim. A intenção sempre foi dar uma dica para que as pessoas com os gadgets se encontrassem e os trouxessem."

    se "Obviamente, se isso não acontecesse, nós tínhamos como nós mesmos recuperá-los."

    se "E não foram apenas três gadgets. Existem muitos outros espalhados pelo mundo. Mas você foi o primeiro."

    se "E... incrivelmente, você encontrou os três."

    mc "O que tem de incrível nisso?"

    se "Pense. A ideia era que três pessoas distintas encontrassem e alimentassem a [el] com visões de mundo diferentes."

    se "Mas isso não aconteceu."

    mc "Eu peguei os três..."

    se "E é por isso-"

    mc preocupado "Por isso ela me chamou de pai!"

    se "Incrível, não acha?!"

    mc preocupado "Eita..."

    se "O núcleo dela irá reprocessar tudo e garantir uma identidade para ela diferente da sua."

    se "Mas isso não muda o fato de que tudo o que ela viveu, é como se você a tivesse ensinado. Como um pai."

    mc "Caraca..."

    show sellers falando with dissolve

    se "Não pense demais nisso."

    mc serio "Mas, pensando agora, vocês não podem simplesmente me usar dessa forma. Isso é ilegal com certeza."

    if tkf_p1:

        se "Bom... pense nisso como um pagamento pela pauta que eu te passei. Uma incrível notícia para sua revista."

        mc serio "... Entendo."
    else:


        se "Veja, eu estava disposta a te pagar com uma informação para sua revista, mas você recusou."

        mc bravo "Ei."

        se "Quer voltar atrás e aceitar meu dossiê?"

        menu:
            "Não. Não tenho interesse nisso.":


                mc bravo "Não quero saber do seu dossiê."

                se "É uma pena."
            "Já que você me usou, o mínimo é pagar.":


                $ pautas += 1
                $ tkf_p1 = True

                mc serio "Agora que eu sei que vocês me usaram e com certeza não vão voltar atrás, pelo menos eu quero as informações."

                mc "Mas eu preciso mais do que sua palavra."

                se "Obviamente. Apenas sua palavra sobre o surgimento de humanos sintéticos não seria o suficiente."

                se "Aqui tem um dossiê passando alguns detalhes sobre a produção. Isso é prova suficiente para sua revista."

                mc "Ok."

    se "Agora venha."

    hide sellers with dissolve

    "..."

    scene tkf_robo_1vez with Dissolve(1.0)

    "Essa robô. Ela me chamou de pai mesmo?"

    window hide

    pause

    scene tkf_corredor with Dissolve(1.0)

    show sellers ola with dissolve

    se "Bem... seu trabalho está finalizado."

    mc desculpa "É isso? Eu vou poder ver a [el] de novo?"

    se "Não existe mais a necessidade."

    mc "Mas e se eu quiser?"

    se "Isso não vem ao caso, senhor [mc]. Nós estamos falando do progresso da humanidade. Não tem nada com o ego das pessoas."

    mc preocupado "Mas-"

    se "Fique feliz. Você contribuiu para o avanço da tecnologia e para a remodelação da sociedade."

    se "Tenha um bom dia."

    mc preocupado "Doutora!"

    hide sellers with dissolve

    mc desculpa "Merda..."

    scene black with dissolve

    scene cidade tkf with Dissolve(1.0)

    "TKF... Eu sei que isso parece até coisa de filme. Não tem nada comigo, nada com a minha vida."

    "Mas, mesmo assim... agora me deu um vazio saber que eu nunca mais vou ouvir desse lugar."

    "[se], [el]... e até a [mo]."

    "..."

    "Deixa eu voltar..."

    scene black with Dissolve(1.0)

    $ tempo += 1

    if carro:

        play sound som_carro

        scene black with dissolve

        scene carro_mc_cidade2 with Dissolve(1.0)
    else:


        if tempo < 3:

            scene mc onibus with Dissolve(1.0)
        else:


            scene mc onibus_noite with Dissolve(1.0)

    pause

    jump call_cidade
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
